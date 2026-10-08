"""Terminal/risk/floor_defense.py
======================================
G-1 Hard Capital Floor Defense — pre-admission risk budget calculator.

Centralizes the math that was previously scattered across subagent prompts
and ACTIVE_CONTEXT.md prose into a single, testable, importable module.

Constants match ACTIVE_CONTEXT.md (Section 3):
  - HARD_FLOOR_USD  = 4,775.00 USD
  - BUFFER_USD      = 20.00 USD  (mandatory cushion above floor)
  - MAX_RISK_USD    = 20.00 USD  (per-trade risk cap)
  - MIN_RISK_USD    = 10.00 USD  (per-trade risk floor)
"""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import List, Optional

logger = logging.getLogger("FloorDefense")

HARD_FLOOR_USD    = 4_775.00
BUFFER_USD        =    20.00
MIN_RISK_USD      =    10.00
MAX_RISK_USD      =    20.00

# Cluster map for correlation governor
CLUSTER_MAP: dict[str, list[str]] = {
    "crypto":  ["BTCUSD.pi", "ETHUSD.pi", "SOLUSD.p", "BNBUSD.p", "ADAUSD.p",
                "DOTUSD.pi", "DOTUSD.p", "XRPUSD.pi", "BNBUSD.pi", "DOGEUSD.p", "DOGUSD.p",
                "LTCUSD.p", "LTCUSD.pi", "LINKUSD.p", "LNKUSD.p", "AVAXUSD.p",
                "AVXUSD.p", "NEARUSD.p", "NERUSD.p", "TRXUSD.p", "BCHUSD.p"],
    "energy":  ["USWTI.p", "UKOIL.p"],
    "indices": ["SP500.p", "NAS100.p", "UK100.p", "GER40.p", "JPN225.p"],
    "forex":   ["EURUSD.pi", "GBPUSD.pi", "USDJPY.pi", "AUDUSD.pi", "NZDUSD.pi",
                "USDCAD.pi", "USDCHF.pi"],
    "metals":  ["XAUUSD.pi", "XAGUSD.pi"],
}


@dataclass
class AdmissionResult:
    allowed: bool
    reason: str
    headroom_usd: float
    post_stopout_cushion: float
    proposed_risk_usd: float
    capacity_slots_free: int


class FloorDefense:
    """Capital floor defense and admission governor.

    Usage:
        fd = FloorDefense()
        result = fd.can_admit(
            balance=4811.62,
            open_risks=[11.0],         # list of USD risk on open positions
            proposed_risk=10.5,
            proposed_symbol="ETHUSD.pi",
            open_symbols=["BTCUSD.pi"],
        )
        if not result.allowed:
            print(result.reason)
    """

    def __init__(
        self,
        hard_floor: float = HARD_FLOOR_USD,
        buffer: float     = BUFFER_USD,
        min_risk: float   = MIN_RISK_USD,
        max_risk: float   = MAX_RISK_USD,
        max_concurrent: int = 6,
    ):
        self.hard_floor    = hard_floor
        self.buffer        = buffer
        self.min_risk      = min_risk
        self.max_risk      = max_risk
        self.max_concurrent = max_concurrent

    # ------------------------------------------------------------------
    # Main admission gate
    # ------------------------------------------------------------------
    def can_admit(
        self,
        balance: float,
        open_risks: List[float],
        proposed_risk: float,
        proposed_symbol: str = "",
        open_symbols: List[str] | None = None,
    ) -> AdmissionResult:
        """Check whether a new trade can be admitted under the floor defense.

        Args:
            balance:         Current account balance in USD.
            open_risks:      List of USD risk committed to currently open positions
                             (SL-distance × volume × contract_size).
            proposed_risk:   USD risk of the proposed new trade.
            proposed_symbol: MT5 symbol for correlation cluster check.
            open_symbols:    Symbols of currently open positions.

        Returns:
            AdmissionResult with allowed flag and full diagnostic breakdown.
        """
        open_symbols = open_symbols or []

        # 1. Validate proposed risk bounds
        if proposed_risk < self.min_risk:
            return AdmissionResult(
                allowed=False,
                reason=f"proposed_risk {proposed_risk:.2f} < min {self.min_risk:.2f} USD",
                headroom_usd=0.0,
                post_stopout_cushion=0.0,
                proposed_risk_usd=proposed_risk,
                capacity_slots_free=0,
            )
        if proposed_risk > self.max_risk:
            return AdmissionResult(
                allowed=False,
                reason=f"proposed_risk {proposed_risk:.2f} > max {self.max_risk:.2f} USD",
                headroom_usd=0.0,
                post_stopout_cushion=0.0,
                proposed_risk_usd=proposed_risk,
                capacity_slots_free=0,
            )

        # 2. Concurrent position cap
        n_open = len([r for r in open_risks if r > 0])
        slots_free = self.max_concurrent - n_open
        if slots_free <= 0:
            return AdmissionResult(
                allowed=False,
                reason=f"capacity exhausted: {n_open}/{self.max_concurrent} slots used",
                headroom_usd=0.0,
                post_stopout_cushion=0.0,
                proposed_risk_usd=proposed_risk,
                capacity_slots_free=0,
            )

        # 3. Worst-case floor math
        total_risk = sum(open_risks) + proposed_risk
        post_stopout = balance - total_risk
        cushion = post_stopout - self.hard_floor
        headroom = balance - self.hard_floor - self.buffer - sum(open_risks)

        if cushion < self.buffer:
            return AdmissionResult(
                allowed=False,
                reason=(
                    f"G-1 floor breach: balance {balance:.2f} - total_risk {total_risk:.2f} "
                    f"= {post_stopout:.2f} USD — cushion {cushion:.2f} < required {self.buffer:.2f} USD"
                ),
                headroom_usd=headroom,
                post_stopout_cushion=cushion,
                proposed_risk_usd=proposed_risk,
                capacity_slots_free=slots_free,
            )

        # 4. Correlation cluster governor
        if proposed_symbol:
            cluster_block = self._cluster_check(proposed_symbol, open_symbols)
            if cluster_block:
                return AdmissionResult(
                    allowed=False,
                    reason=cluster_block,
                    headroom_usd=headroom,
                    post_stopout_cushion=cushion,
                    proposed_risk_usd=proposed_risk,
                    capacity_slots_free=slots_free,
                )

        logger.info(
            "FloorDefense ADMIT: %s risk=%.2f USD | post-stopout cushion=+%.2f USD above floor",
            proposed_symbol or "?", proposed_risk, cushion,
        )
        return AdmissionResult(
            allowed=True,
            reason="all_gates_passed",
            headroom_usd=headroom,
            post_stopout_cushion=cushion,
            proposed_risk_usd=proposed_risk,
            capacity_slots_free=slots_free,
        )

    # ------------------------------------------------------------------
    # Risk budget: dynamic trailing floor escalation
    # ------------------------------------------------------------------
    def trailing_floor(self, balance: float) -> float:
        """Ratchet the floor upward as balance grows (locks in profits).

        Floor escalation:
          balance <= 5,000 USD  → 4,775 USD (hardcoded baseline)
          balance > 5,000 USD   → balance × 0.955 (4.5% max DD cap)
        """
        if balance <= 5_000.0:
            return HARD_FLOOR_USD
        return round(balance * 0.955, 2)

    # ------------------------------------------------------------------
    # Correlation cluster governor
    # ------------------------------------------------------------------
    def cluster_of(self, symbol: str) -> str:
        s = str(symbol).strip().upper()
        for cluster, members in CLUSTER_MAP.items():
            if s in members:
                return cluster
        base = s.split(".")[0]
        for cluster, members in CLUSTER_MAP.items():
            member_bases = [m.split(".")[0] for m in members]
            if base in member_bases:
                return cluster
            for m in members:
                coin = m.split(".")[0].replace("USD", "")
                if base == coin or base.startswith(coin):
                    return cluster
        return "other"

    def _cluster_check(self, proposed: str, open_syms: List[str]) -> Optional[str]:
        """Return a rejection reason if proposed symbol is in the same cluster as an open position."""
        pc = self.cluster_of(proposed)
        if pc == "other":
            return None   # unknown — no veto, let qualitative review decide
        for sym in open_syms:
            ec = self.cluster_of(sym)
            if ec == pc:
                return (
                    f"correlation_cluster_veto: {proposed} (cluster={pc}) conflicts "
                    f"with open position {sym} (same cluster)"
                )
        return None

    # ------------------------------------------------------------------
    # Phase 0 capacity liberation check
    # ------------------------------------------------------------------
    def phase0_liberates_slot(
        self,
        balance: float,
        open_risks_post_ratchet: List[float],
        proposed_risk: float,
        proposed_symbol: str = "",
        open_symbols: List[str] | None = None,
    ) -> AdmissionResult:
        """Re-check admission after a Phase 0 ratchet (risk[i] → 0.0)."""
        return self.can_admit(
            balance=balance,
            open_risks=open_risks_post_ratchet,
            proposed_risk=proposed_risk,
            proposed_symbol=proposed_symbol,
            open_symbols=open_symbols,
        )
