"""OX_ALPHA_62: the continuous autonomous Arena Brain loop.

The relentless 24/7 decision brain for the hybrid architecture. Runs on any
always-on box (cloud worker, the laptop itself, a second machine) and drives
the laptop "muscle" exclusively through the signed tunnel protocol:

  every 15 seconds (tick):
      POST /api/v1/market_state -> live positions, orders, quotes, orderflow
      * Position Manager: exact R-multiples, 3-phase ratchet dispatch
        (signed MODIFY_SLTP, only-ever-tightening), 24-bar time decay
        (signed CLOSE_POSITION)
  at minute 14 of every 15-minute candle (:14:45 - after the muscle's own
  :14:30 execution window closes, so the brain sees this slot's outcome):
      POST /api/v1/evaluate_candle + market_state
      * full tri-specialist deliberation (Terminal/Headless/swarm.py)
      * staging policy: the brain supplements ONLY when the muscle abstained,
        capacity is open (filled + pending < 2), macro is CLEAR_TO_TRADE, the
        taker-delta exhaustion gate passes and |conviction| is extreme

Everything is fail-closed and error-isolated: a dead tunnel counts errors and
keeps looping; a refused command is journalled and never retried blindly; no
exception ever escapes the loop. All risk invariants are enforced MUSCLE-side
(the signed commands carry intent; apply_command enforces the caps).

CLI:
    python -m Terminal.Headless.arena_continuous_brain
    (ARENA_TUNNEL_URL / OMNI_API_SECRET override the configured defaults)
"""
from __future__ import annotations

import json
import os
import time
from typing import Callable, Dict, List, Optional

from Terminal.Risk_Sizing_Engine import number

BRAIN_VERSION = "omni.arena_continuous_brain.v1"
BRAIN_COMMENT = "ARENA:BRAIN_v1"

DEFAULT_TUNNEL_URL = "https://mailman-jumping-detailed-observation.trycloudflare.com"
DEFAULT_SECRET = ""          # pulled from OMNI_API_SECRET; never committed


class BrainPolicy:
    tick_interval: float = 15.0            # ratchet/position cadence
    deliberation_minute: int = 14          # minute-of-candle for deliberation
    deliberation_second: float = 45.0      # after the muscle's :14:30 window
    # 3-phase piecewise ratchet (OX_ALPHA_62 section 2.4)
    phase0_trigger_r: float = 0.80
    phase0_lock_r: float = 0.15
    phase1_trigger_r: float = 1.50
    phase1_lock_r: float = 0.85
    phase2_trigger_r: float = 2.00
    phase2_trail_r: float = 0.65
    trail_min_improvement_r: float = 0.05  # re-arm threshold for the runner trail
    # time decay
    decay_gain_r: float = 0.20
    decay_bars: int = 24
    decay_close: bool = True
    # staging
    conviction_threshold: float = 0.50     # extreme orderflow only
    stage_risk_usd: float = 10.00          # base budget (muscle caps at 20.00)
    stage_stop_atr: float = 1.5            # adaptive stop floor (with swing where known)
    stage_tp_r: float = 2.50               # target exit in R
    max_concurrent: int = 2                # filled + pending, fail-closed


class ContinuousBrain:
    """The endless loop. Everything injectable for deterministic tests."""

    def __init__(self, client, *, policy: Optional[BrainPolicy] = None,
                 clock: Callable = time.time, journal: Optional[Callable] = None):
        self.client = client
        self.policy = policy or BrainPolicy()
        self.clock = clock
        self.journal = journal
        self.ratchet_state: Dict[str, Dict] = {}     # ticket -> phase ledger
        self.last_deliberation_slot = -1
        self.stats = {"ticks": 0, "deliberations": 0, "modifications": 0,
                      "stages": 0, "closes": 0, "errors": 0, "refusals": 0}

    # ------------------------------------------------------------- journalling
    def _journal(self, event: str, **record):
        row = {"time": self.clock(), "brain": BRAIN_VERSION, "event": event, **record}
        if self.journal is not None:
            try:
                self.journal(row)
            except Exception:                             # noqa: BLE001
                pass
        return row

    # ------------------------------------------------------------- 15s tick
    def tick(self) -> Dict:
        """One position-management cycle. Never raises."""
        try:
            state = self.client.market_state()
        except Exception as exc:                          # noqa: BLE001 - loop isolation
            self.stats["errors"] += 1
            return self._journal("tick_error", error=repr(exc))
        if not isinstance(state, dict) or state.get("error") or state.get("http_status"):
            self.stats["errors"] += 1
            return self._journal("tick_error", error=str(state.get("error", "bad_state")))
        self.stats["ticks"] += 1
        actions = []
        positions = state.get("positions")
        if not isinstance(positions, list):
            positions = []                      # never trust a remote payload shape
        for position in positions:
            try:
                actions.extend(self._manage_position(position, state))
            except Exception as exc:                      # noqa: BLE001 - position isolation
                self.stats["errors"] += 1
                self._journal("manage_error", ticket=position.get("ticket"), error=repr(exc))
        self._journal("tick", positions=len(state.get("positions") or []),
                      actions=[a["event"] for a in actions])
        return {"actions": actions, "state": state}

    # ----------------------------------------------------- position management
    def _manage_position(self, position: Dict, state: Dict) -> List[Dict]:
        policy = self.policy
        ticket = str(position.get("ticket"))
        entry = number(position.get("price_open"))
        sl = number(position.get("sl"))
        direction = str(position.get("direction", "")).upper()
        symbol = str(position.get("symbol", ""))
        quote = (state.get("quotes") or {}).get(symbol) or {}
        if not entry or not sl or direction not in ("LONG", "SHORT") or not quote:
            return []
        price = number(quote.get("bid" if direction == "LONG" else "ask"))
        if price <= 0:
            return []

        ledger = self.ratchet_state.setdefault(ticket, {"phases": set(), "max_r": 0.0,
                                                        "initial_r": 0.0})
        # Initial risk from the first sight of an unprotected stop; a stop
        # already locked past entry implies the early phases are complete.
        if ledger["initial_r"] <= 0:
            locked = (direction == "LONG" and sl >= entry) or (direction == "SHORT" and sl <= entry)
            ledger["initial_r"] = abs(entry - sl)
            if locked or ledger["initial_r"] <= 0:
                ledger["phases"].add("0")
                ledger["phases"].add("1")
                if ledger["initial_r"] <= 0:
                    return []
        initial_r = ledger["initial_r"]
        sign = 1.0 if direction == "LONG" else -1.0
        gain_r = sign * (price - entry) / initial_r
        ledger["max_r"] = max(ledger["max_r"], gain_r)

        actions = []

        def _dispatch_sl(new_sl: float, event: str) -> Optional[Dict]:
            new_sl = round(new_sl, 8)
            # Only-ever-tightening, and never through the current price.
            tighter = (new_sl > sl + 1e-12) if direction == "LONG" else (new_sl < sl - 1e-12)
            valid = (new_sl < price) if direction == "LONG" else (new_sl > price)
            if not (tighter and valid):
                return None
            result = self.client.modify_sltp(ticket=int(float(ticket)), sl=new_sl)
            self.stats["modifications"] += 1
            self._journal(event, ticket=ticket, sl=new_sl, gain_r=round(gain_r, 4),
                          result=result)
            return {"event": event, "ticket": ticket, "sl": new_sl,
                    "result": result}

        # Phase 0: break-even lock at +0.80R -> entry +/- 0.15R
        if gain_r >= policy.phase0_trigger_r and "0" not in ledger["phases"]:
            lock = (entry + policy.phase0_lock_r * initial_r) if direction == "LONG" \
                else (entry - policy.phase0_lock_r * initial_r)
            if _dispatch_sl(lock, "ratchet_phase0_be_lock"):
                ledger["phases"].add("0")

        # Phase 1: profit lock at +1.50R -> entry +/- 0.85R
        if gain_r >= policy.phase1_trigger_r and "1" not in ledger["phases"]:
            lock = (entry + policy.phase1_lock_r * initial_r) if direction == "LONG" \
                else (entry - policy.phase1_lock_r * initial_r)
            if _dispatch_sl(lock, "ratchet_phase1_profit_lock"):
                ledger["phases"].add("1")

        # Phase 2: runner trail at +2.00R -> price -/+ 0.65R (re-armable)
        if gain_r >= policy.phase2_trigger_r:
            trail = (price - policy.phase2_trail_r * initial_r) if direction == "LONG" \
                else (price + policy.phase2_trail_r * initial_r)
            last_trail = ledger.get("last_trail_r", 0.0)
            if gain_r - last_trail >= policy.trail_min_improvement_r:
                if _dispatch_sl(trail, "ratchet_phase2_runner_trail"):
                    ledger["last_trail_r"] = gain_r

        # Time decay: no +0.20R within 24 bars -> exit at market
        age_sec = self.clock() - number(position.get("time"), 0.0)
        if policy.decay_close and ledger["max_r"] < policy.decay_gain_r \
                and age_sec >= policy.decay_bars * 900 and "decay" not in ledger["phases"]:
            ledger["phases"].add("decay")
            result = self.client.close_position(ticket=int(float(ticket)),
                                                reason=f"time_decay_{policy.decay_bars}bars")
            self.stats["closes"] += 1
            self._journal("time_decay_close", ticket=ticket, age_sec=age_sec,
                          max_r=round(ledger["max_r"], 4), result=result)
            actions.append({"event": "time_decay_close", "ticket": ticket,
                            "result": result})
        return actions

    # ------------------------------------------------- minute-14 deliberation
    def deliberate(self, state: Optional[Dict] = None) -> Dict:
        """Full tri-specialist deliberation for this candle slot."""
        now = self.clock()
        slot = int(now // 900)
        minute = int((now % 900) // 60)
        if minute != self.policy.deliberation_minute or slot == self.last_deliberation_slot:
            return {"skipped": True, "reason": "outside_window_or_already_deliberated"}
        self.last_deliberation_slot = slot
        if state is None:
            try:
                state = self.client.market_state()
            except Exception as exc:                      # noqa: BLE001
                self.stats["errors"] += 1
                return self._journal("deliberation_error", error=repr(exc))
        try:
            evaluation = self.client.evaluate_candle()
        except Exception as exc:                          # noqa: BLE001
            self.stats["errors"] += 1
            return self._journal("deliberation_error", error=repr(exc))
        if not isinstance(evaluation, dict) or evaluation.get("http_status") \
                or evaluation.get("error"):
            self.stats["errors"] += 1
            return self._journal("deliberation_error",
                                 error=str((evaluation or {}).get("error", "bad_eval")))

        # ---- tri-specialist deliberation over the live state
        from Terminal.Headless.swarm import deliberate as swarm_deliberate
        positions = state.get("positions") or []
        macro = dict(state.get("macro") or {})
        account = state.get("account") or {}
        equity = number(account.get("equity_usd"), 5000.0)
        deliberation = {"assets": {}}
        for asset, snapshot in (state.get("orderflow") or {}).items():
            deliberation["assets"][asset] = swarm_deliberate(
                {"orderflow": snapshot}, positions, macro, equity_usd=equity)
        self.stats["deliberations"] += 1

        # ---- macro governance verdict
        blocked = bool(macro.get("blackout_active")) or equity <= 4775.0
        verdict = "BLOCKED" if blocked else "CLEAR_TO_TRADE"

        # ---- staging policy (supplement only)
        staged = None
        muscle_decision = evaluation.get("decision")
        pending = state.get("pending_orders") or []
        capacity_open = len(positions) + len(pending) < self.policy.max_concurrent
        muscle_staged = muscle_decision in ("LIMIT_STAGED", "ORDER_FILLED", "PAPER_FILLED")
        conviction_vector = evaluation.get("pioneer_conviction_vector") or {}
        if not blocked and not muscle_staged and capacity_open:
            staged = self._maybe_stage(state, conviction_vector)
        self._journal("deliberation", slot=slot, verdict=verdict,
                      muscle_decision=muscle_decision, capacity_open=capacity_open,
                      conviction=conviction_vector, staged=staged)
        return {"slot": slot, "verdict": verdict, "muscle_decision": muscle_decision,
                "capacity_open": capacity_open, "deliberation": deliberation,
                "staged": staged}

    def _maybe_stage(self, state: Dict, conviction_vector: Dict) -> Optional[Dict]:
        """Stage ONE validated limit for an extreme-conviction asset the
        muscle abstained on. Every gate must pass; the muscle re-enforces
        the risk caps on arrival."""
        from Terminal.Orderbook_Structure import taker_delta_exhaustion
        policy = self.policy
        best = None
        for asset, advisory in (conviction_vector or {}).items():
            conviction = number(advisory.get("conviction"), 0.0)
            if abs(conviction) < policy.conviction_threshold:
                continue
            snapshot = (state.get("orderflow") or {}).get(asset)
            if not snapshot:
                continue
            direction = "LONG" if conviction > 0 else "SHORT"
            gate = taker_delta_exhaustion(snapshot, direction)
            if gate["status"] == "ENFORCED" and not gate["ok"]:
                self.stats["refusals"] += 1
                continue
            if best is None or abs(conviction) > abs(number(best[1])):
                best = (asset, conviction, direction, snapshot, gate)
        if best is None:
            return None
        asset, conviction, direction, snapshot, gate = best
        atr = number(snapshot.get("atr"), 0.0)
        if atr <= 0:
            return None
        symbol = self._symbol_of(state, asset)
        quote = (state.get("quotes") or {}).get(symbol) or {}
        price = number(quote.get("bid" if direction == "LONG" else "ask"))
        contract = number(quote.get("contract_size"), 0.0)
        if not symbol or price <= 0 or contract <= 0:
            return None
        entry = price                                   # passive: rest at the quote
        stop_distance = policy.stage_stop_atr * atr
        sl = entry - stop_distance if direction == "LONG" else entry + stop_distance
        tp = entry + policy.stage_tp_r * stop_distance if direction == "LONG" \
            else entry - policy.stage_tp_r * stop_distance
        min_lot = number(quote.get("min_lot"), 0.01)
        step_lot = number(quote.get("step_lot"), 0.01)
        volume = policy.stage_risk_usd / (stop_distance * contract)
        volume = max(0.0, volume - (volume % max(step_lot, 1e-12)))
        if volume < min_lot:
            self.stats["refusals"] += 1
            return None                                  # min-lot risk would exceed budget
        result = self.client.stage_order(symbol=symbol, direction=direction,
                                         volume=round(volume, 4), limit_price=entry,
                                         sl=round(sl, 8), tp=round(tp, 8),
                                         comment=BRAIN_COMMENT)
        self.stats["stages"] += 1
        self._journal("brain_stage", asset=asset, symbol=symbol, direction=direction,
                      conviction=round(conviction, 4), entry=entry, sl=sl, tp=tp,
                      volume=round(volume, 4), exhaustion_gate=gate, result=result)
        return {"asset": asset, "symbol": symbol, "direction": direction,
                "entry": entry, "sl": sl, "tp": tp, "volume": round(volume, 4),
                "result": result}

    @staticmethod
    def _symbol_of(state: Dict, asset: str) -> str:
        asset = str(asset).upper()
        mapping = state.get("symbols") or {}
        if mapping.get(asset):
            return str(mapping[asset])
        for row in list(state.get("positions") or []) + list(state.get("pending_orders") or []):
            symbol = str(row.get("symbol", ""))
            if symbol.upper().startswith(asset):
                return symbol
        return ""

    # ------------------------------------------------------------- main loop
    def run_forever(self, *, stop=None, sleep=time.sleep):
        """The endless loop: tick every interval, deliberate at minute 14."""
        while stop is None or not stop.is_set():
            try:
                state_result = self.tick()
                state = state_result.get("state") if isinstance(state_result, dict) else None
                self.deliberate(state)
            except Exception as exc:                      # noqa: BLE001 - never die
                self.stats["errors"] += 1
                self._journal("loop_error", error=repr(exc))
            sleep(self.policy.tick_interval)


# --------------------------------------------------------------------- CLI
def _main(argv=None):
    import argparse
    import signal
    import threading
    from pathlib import Path

    from Terminal.Headless.brain_client import BrainClient

    parser = argparse.ArgumentParser(description="OX_ALPHA_62 continuous Arena Brain")
    parser.add_argument("--url", default=os.environ.get("ARENA_TUNNEL_URL",
                                                        DEFAULT_TUNNEL_URL))
    parser.add_argument("--secret", default=os.environ.get("OMNI_API_SECRET",
                                                           DEFAULT_SECRET))
    parser.add_argument("--interval", type=float, default=BrainPolicy.tick_interval)
    parser.add_argument("--journal", default=str(Path("Data/Omni/brain/brain_journal.jsonl")))
    args = parser.parse_args(argv)
    if not args.secret:
        parser.error("OMNI_API_SECRET required (or --secret)")

    journal_path = Path(args.journal)
    journal_path.parent.mkdir(parents=True, exist_ok=True)

    def journal(row):
        with journal_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, default=str) + "\n")

    policy = BrainPolicy()
    policy.tick_interval = max(5.0, args.interval)
    brain = ContinuousBrain(BrainClient(args.url, args.secret), policy=policy,
                            journal=journal)
    stop = threading.Event()

    def _signal(_sig, _frame):
        stop.set()

    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            signal.signal(sig, _signal)
        except (ValueError, OSError):                    # pragma: no cover
            pass
    print(f"[arena-brain] {BRAIN_VERSION} -> {args.url} "
          f"(tick {policy.tick_interval:.0f}s, deliberate at :{policy.deliberation_minute:02d})",
          flush=True)
    brain.run_forever(stop=stop)
    print(f"[arena-brain] stopped: {brain.stats}", flush=True)


if __name__ == "__main__":
    _main()
