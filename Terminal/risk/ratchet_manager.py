"""Terminal/risk/ratchet_manager.py
=========================================
P0 FIX — Automated Phase 0/1/2 ratchet manager.

INCIDENT PREVENTION:
  Phase 0 BE lock was previously triggered only when a subagent manually
  noticed the floating gain in a cron cycle. If the cron fired late or a
  subagent errored, the ratchet was missed — leaving asymmetric risk on.

  This module runs an automated polling loop (every 30 seconds) inside
  mt5-trader mode, checking all open positions and pending orders against
  their registered ratchet states, and firing SL modifications automatically.

RATCHET SPEC (from ACTIVE_CONTEXT.md):
  Phase 0 (BE Lock):    At +0.80R gain → move SL to entry + 0.15R (locking friction/spread, guaranteed profit)
  Phase 1 (Profit Lock):At +1.50R gain → move SL to entry + 0.80R gain
  Phase 2 (Trail):      At +2.00R gain → trail SL to entry + 1.50R
  Time Decay:           Exit at market if < +0.20R within 24 bars (6 hours)
  Target:               +2.50R exit (TP set at staging)
"""
from __future__ import annotations

import logging
import math
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import IntEnum
from typing import Dict, Optional

from Terminal.risk.risk_kernel import RATCHET_LADDER

logger = logging.getLogger("RatchetManager")


class RatchetPhase(IntEnum):
    OPEN      = 0   # No ratchet fired yet
    BE_LOCKED = 1   # Phase 0: SL at entry - 0.25R (75% risk reduction with 0.25R breathing room)
    PROFIT_1  = 2   # Phase 1: SL at entry + 0.80R (guaranteed profit lock)
    TRAIL_2   = 3   # Phase 2: Running trail at Peak - 0.75R
    CLOSED    = 9   # Position closed


# Ratchet thresholds in units of R (imported from canonical Terminal/risk/risk_kernel.py)
# Empirical 1,044-trade replay: avoids choking 86.7% of normal 15m entry retests at +0.8R
_PHASE_0_R_TRIGGER      = RATCHET_LADDER["phase_0"]["trigger_r"]     # 1.25
_PHASE_1_R_TRIGGER      = RATCHET_LADDER["phase_1"]["trigger_r"]     # 1.65
_PHASE_2_R_TRIGGER      = RATCHET_LADDER["phase_2"]["trigger_r"]     # 2.00
_PHASE_TARGET_R_TRIGGER = 2.30   # Target extension safeguard

# SL offsets in units of R
_PHASE_0_SL_OFFSET      = RATCHET_LADDER["phase_0"]["sl_offset_r"]   # -0.25 (Entry - 0.25R)
_PHASE_1_SL_OFFSET      = RATCHET_LADDER["phase_1"]["sl_offset_r"]   # +0.80 (Entry + 0.80R)
_PHASE_2_SL_OFFSET      = 1.50   # Entry + 1.50R minimum floor on Phase 2
_PHASE_TARGET_SL_OFFSET = 1.85   # Entry + 1.85R on Target extension

# Time-decay exit: exit at market if gain < +0.20R after 24 bars (6 hours)
_TIME_DECAY_MIN_R   = RATCHET_LADDER["time_decay"]["min_r"] # 0.20
_TIME_DECAY_BARS    = RATCHET_LADDER["time_decay"]["bars"]  # 24
_BAR_SECONDS        = 900    # 15-minute bars


@dataclass
class PositionState:
    """Ratchet state for a single open position."""
    ticket: int
    symbol: str
    entry: float
    initial_sl: float
    tp: float
    direction: int          # +1 = long, -1 = short
    staged_at: float = field(default_factory=time.time)  # Unix timestamp
    phase: RatchetPhase = RatchetPhase.OPEN
    last_modified: float = 0.0

    @property
    def r_size(self) -> float:
        """1R in price units."""
        return abs(self.entry - self.initial_sl)

    def trigger_price(self, phase_r: float) -> float:
        """Price at which a phase triggers."""
        return self.entry + self.direction * phase_r * self.r_size

    def sl_at_phase(self, phase_r: float) -> float:
        """SL price after ratchet fires for a given offset in R."""
        return self.entry + self.direction * phase_r * self.r_size

    def floating_r(self, current_price: float) -> float:
        """Current floating gain in R units."""
        return self.direction * (current_price - self.entry) / max(self.r_size, 1e-12)

    def age_bars(self) -> float:
        """How many 15m bars old this position is."""
        elapsed = time.time() - self.staged_at
        return elapsed / _BAR_SECONDS


class RatchetManager:
    """Automated ratchet engine: polls all open positions and fires SL mods.

    Designed to run in a background thread inside OF_Strategy.py (mt5-trader
    mode). The MT5 bridge must be passed in so the manager uses the same
    connection and account context.

    Usage:
        manager = RatchetManager(bridge)
        manager.register(ticket=18652155, symbol="BTCUSD.pi",
                         entry=83880.0, sl=84430.0, tp=82505.0,
                         direction=-1)   # -1 = short
        # Run the polling loop in a thread:
        manager.run_loop(interval_seconds=30)
    """

    def __init__(self, bridge=None):
        self._bridge = bridge
        self._positions: Dict[int, PositionState] = {}

    def register(
        self,
        ticket: int,
        symbol: str,
        entry: float,
        sl: float,
        tp: float,
        direction: int,
        staged_at: Optional[float] = None,
    ) -> PositionState:
        """Register a new position for automated ratchet management."""
        state = PositionState(
            ticket=ticket,
            symbol=symbol,
            entry=entry,
            initial_sl=sl,
            tp=tp,
            direction=direction,
            staged_at=staged_at or time.time(),
        )
        self._positions[ticket] = state
        logger.info(
            "Registered ticket %d %s entry=%.2f sl=%.2f tp=%.2f dir=%s  1R=%.2f",
            ticket, symbol, entry, sl, tp,
            "SHORT" if direction == -1 else "LONG",
            state.r_size,
        )
        return state

    def unregister(self, ticket: int) -> None:
        """Remove a closed position from tracking."""
        self._positions.pop(ticket, None)

    def check_position(self, ticket: int, current_price: float) -> Optional[dict]:
        """Evaluate one position and fire a ratchet if the threshold is hit.

        Returns:
            dict with keys {action, phase_new, sl_new, r_gain} if a ratchet fired.
            None if no action was taken.
        """
        state = self._positions.get(ticket)
        if state is None or state.phase == RatchetPhase.CLOSED:
            return None

        gain_r = state.floating_r(current_price)

        # ------------------------------------------------------------------ #
        # Target Extension Safeguard (gain >= +2.30R)                         #
        # ------------------------------------------------------------------ #
        if gain_r >= _PHASE_TARGET_R_TRIGGER and state.phase < RatchetPhase.TRAIL_2:
            new_sl = state.sl_at_phase(_PHASE_TARGET_SL_OFFSET)
            ok = self._modify_sl(state, new_sl)
            if ok:
                state.phase = RatchetPhase.TRAIL_2
                state.last_modified = time.time()
                logger.info(
                    "[RATCHET Target Extension] Ticket %d %s: +%.2fR >= +2.30R -> SL %.2f->%.2f (1.85R profit locked)",
                    ticket, state.symbol, gain_r, state.initial_sl, new_sl,
                )
                return {"action": "phase_target_lock", "phase_new": state.phase,
                        "sl_new": new_sl, "r_gain": round(gain_r, 3)}

        # ------------------------------------------------------------------ #
        # Phase 2 — Trail (gain >= +2.00R)                                   #
        # ------------------------------------------------------------------ #
        if gain_r >= _PHASE_2_R_TRIGGER and state.phase < RatchetPhase.TRAIL_2:
            new_sl = state.sl_at_phase(_PHASE_2_SL_OFFSET)
            ok = self._modify_sl(state, new_sl)
            if ok:
                state.phase = RatchetPhase.TRAIL_2
                state.last_modified = time.time()
                logger.info(
                    "[RATCHET Phase 2] Ticket %d %s: +%.2fR >= +2.00R -> SL %.2f->%.2f (1.50R trail locked)",
                    ticket, state.symbol, gain_r, state.initial_sl, new_sl,
                )
                return {"action": "phase_2_trail", "phase_new": state.phase,
                        "sl_new": new_sl, "r_gain": round(gain_r, 3)}

        # ------------------------------------------------------------------ #
        # Phase 1 — Profit Lock (gain >= +1.65R)                             #
        # ------------------------------------------------------------------ #
        if gain_r >= _PHASE_1_R_TRIGGER and state.phase < RatchetPhase.PROFIT_1:
            new_sl = state.sl_at_phase(_PHASE_1_SL_OFFSET)
            ok = self._modify_sl(state, new_sl)
            if ok:
                state.phase = RatchetPhase.PROFIT_1
                state.last_modified = time.time()
                logger.info(
                    "[RATCHET Phase 1] Ticket %d %s: +%.2fR >= +1.65R -> SL %.2f->%.2f (1.00R profit locked)",
                    ticket, state.symbol, gain_r, state.initial_sl, new_sl,
                )
                return {"action": "phase_1_profit", "phase_new": state.phase,
                        "sl_new": new_sl, "r_gain": round(gain_r, 3)}

        # ------------------------------------------------------------------ #
        # Phase 0 — Breakeven Lock (gain >= +1.25R)                           #
        # ------------------------------------------------------------------ #
        if gain_r >= _PHASE_0_R_TRIGGER and state.phase < RatchetPhase.BE_LOCKED:
            new_sl = state.sl_at_phase(_PHASE_0_SL_OFFSET)
            ok = self._modify_sl(state, new_sl)
            if ok:
                state.phase = RatchetPhase.BE_LOCKED
                state.last_modified = time.time()
                logger.info(
                    "[RATCHET Phase 0] Ticket %d %s: +%.2fR >= +1.25R -> SL %.2f->%.2f (BE+0.20R locked)",
                    ticket, state.symbol, gain_r, state.initial_sl, new_sl,
                )
                return {"action": "phase_0_be", "phase_new": state.phase,
                        "sl_new": new_sl, "r_gain": round(gain_r, 3)}

        # ------------------------------------------------------------------ #
        # Time-decay exit                                                     #
        # ------------------------------------------------------------------ #
        if (state.phase == RatchetPhase.OPEN
                and state.age_bars() >= _TIME_DECAY_BARS
                and gain_r < _TIME_DECAY_MIN_R):
            logger.warning(
                "[TIME DECAY] Ticket %d %s: %d bars old, gain only +%.2fR < +0.20R -> market close",
                ticket, state.symbol, int(state.age_bars()), gain_r,
            )
            if self._close_at_market(state):
                state.phase = RatchetPhase.CLOSED
                return {"action": "time_decay_exit", "phase_new": state.phase,
                        "r_gain": round(gain_r, 3)}
            logger.error("[TIME DECAY] Ticket %d close failed; retaining OPEN for retry", ticket)
            return {"action": "time_decay_exit_failed", "phase_new": state.phase,
                    "r_gain": round(gain_r, 3)}

        return None

    def run_once(self) -> list[dict]:
        """Run one poll cycle across all registered positions. Returns list of actions fired."""
        try:
            import MetaTrader5 as mt5
            if not mt5.terminal_info():
                if not mt5.initialize():
                    logger.error("Ratchet MT5 terminal unavailable and re-initialization failed")
                    return []
                logger.info("Ratchet MT5 terminal re-initialized successfully")
            results = []
            raw_positions = mt5.positions_get()
            if raw_positions is None:
                raise RuntimeError("MT5 positions_get failed; do not mark positions closed")
            positions = {p.ticket: p for p in raw_positions}
            # Discover new fills every poll, not only at process start.
            for ticket, p in positions.items():
                if ticket not in self._positions and float(p.sl) > 0:
                    direction = 1 if p.type == mt5.ORDER_TYPE_BUY else -1
                    self.register(ticket, p.symbol, float(p.price_open), float(p.sl),
                                  float(p.tp), direction, staged_at=float(p.time))
            for ticket, state in list(self._positions.items()):
                live = positions.get(ticket)
                if live is None:
                    # Position closed externally
                    state.phase = RatchetPhase.CLOSED
                    logger.info("Ticket %d %s closed externally -- unregistering.", ticket, state.symbol)
                    self.unregister(ticket)
                    continue
                current_price = float(live.price_current)
                action = self.check_position(ticket, current_price)
                if action:
                    results.append({"ticket": ticket, **action})
            return results
        except Exception as exc:
            logger.error("RatchetManager.run_once error: %s", exc)
            return []

    def run_loop(self, interval_seconds: int = 30) -> None:
        """Blocking loop — run in a background thread."""
        logger.info("RatchetManager polling loop started (interval=%ds).", interval_seconds)
        while True:
            try:
                actions = self.run_once()
                if actions:
                    for a in actions:
                        logger.info("RatchetManager action: %s", a)
            except Exception as exc:
                logger.error("RatchetManager loop error: %s", exc)
            time.sleep(interval_seconds)

    # ------------------------------------------------------------------
    # Private MT5 helpers
    # ------------------------------------------------------------------
    def _modify_sl(self, state: PositionState, new_sl: float) -> bool:
        """Tighten a native stop only; verify broker acceptance and readback."""
        try:
            import MetaTrader5 as mt5
            live = mt5.positions_get(ticket=state.ticket)
            if not live or len(live) != 1:
                return False
            pos = live[0]
            info = mt5.symbol_info(state.symbol)
            if info is None:
                return False
            tick = float(getattr(info, "trade_tick_size", 0) or info.point)
            if tick <= 0:
                return False
            new_sl = round(round(new_sl / tick) * tick, int(info.digits))
            current = float(pos.sl)
            if current <= 0 or (state.direction == 1 and new_sl < current) or (state.direction == -1 and new_sl > current):
                return False
            if self._bridge is not None:
                result = self._bridge.modify_position_sltp(
                    ticket=state.ticket, new_sl=new_sl, new_tp=None
                )
                if not result.get("success", False):
                    return False
            else:
                res = mt5.order_send({
                    "action": mt5.TRADE_ACTION_SLTP,
                    "position": state.ticket, "symbol": state.symbol,
                    "sl": new_sl, "tp": float(pos.tp),
                })
                if res is None or res.retcode != getattr(mt5, "TRADE_RETCODE_DONE", 10009):
                    return False
            confirmed = mt5.positions_get(ticket=state.ticket)
            return (confirmed is not None and len(confirmed) == 1 and
                    abs(float(confirmed[0].sl) - new_sl) <= tick * 0.51)
        except Exception as exc:
            logger.error("_modify_sl error for ticket %d: %s", state.ticket, exc)
            return False

    def _close_at_market(self, state: PositionState) -> bool:
        """Market-close a position for time-decay exit."""
        try:
            if self._bridge is not None:
                return self._bridge.close_position(state.ticket).get("success", False)
            import MetaTrader5 as mt5
            pos = mt5.positions_get(ticket=state.ticket)
            if not pos:
                return False
            p = pos[0]
            close_type = (mt5.ORDER_TYPE_SELL if p.type == mt5.ORDER_TYPE_BUY
                          else mt5.ORDER_TYPE_BUY)
            tick = mt5.symbol_info_tick(state.symbol)
            price = tick.bid if close_type == mt5.ORDER_TYPE_SELL else tick.ask
            req = {
                "action": mt5.TRADE_ACTION_DEAL,
                "position": state.ticket,
                "symbol": state.symbol,
                "volume": float(p.volume),
                "type": close_type,
                "price": price,
                "deviation": 20,
                "magic": 100895,
                "comment": "time_decay_exit",
                "type_filling": mt5.ORDER_FILLING_IOC,
            }
            res = mt5.order_send(req)
            ok = res is not None and res.retcode == getattr(mt5, "TRADE_RETCODE_DONE", 10009)
            if ok:
                logger.info("Time-decay closed ticket %d %s at %.2f", state.ticket, state.symbol, price)
            return ok
        except Exception as exc:
            logger.error("_close_at_market error for ticket %d: %s", state.ticket, exc)
            return False


# ---------------------------------------------------------------------------
# Module-level singleton for easy access from OF_Strategy / Omni_Trader
# ---------------------------------------------------------------------------
_global_manager: Optional[RatchetManager] = None


def get_ratchet_manager(bridge=None) -> RatchetManager:
    """Return the global RatchetManager instance, creating it if needed."""
    global _global_manager
    if _global_manager is None:
        _global_manager = RatchetManager(bridge)
    elif bridge is not None and _global_manager._bridge is None:
        _global_manager._bridge = bridge
    return _global_manager
