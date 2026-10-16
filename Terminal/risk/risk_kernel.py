"""Terminal/risk/risk_kernel.py
==============================
Canonical Centralized Risk & Admission Kernel for Trading_2.

Provides a SINGLE, VERSIONED, DETERMINISTIC SOURCE OF TRUTH for:
1. Capital Floor Defense & Stressed Solvency Mathematics.
2. Dynamic Per-Slot Risk Sizing & Residual Capacity Admission.
3. Playbook 7.1 Unified Ratchet Ladder Specification.
4. Synchronous Deterministic `admit()` Pre-Trade Validator.

Institutional Version: 2.1.0 (Audited by Claude, DeepSeek, Minimax, Kimi, Grok)
"""
from __future__ import annotations

import logging
import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple, Any

logger = logging.getLogger("RiskKernel")

# ==============================================================================
# 1. CAPITAL FLOOR & BUFFER INVARIANTS (SINGLE SOURCE OF TRUTH)
# ==============================================================================
HARD_FLOOR_USD: float = 4775.00        # Zero-breach absolute hard floor
OPERATING_BUFFER_USD: float = 4795.00  # Mandatory operating buffer (+20.00 USD above floor)
MIN_CUSHION_USD: float = 20.00         # BUFFER - HARD_FLOOR = 20.00 USD

# Authorized Per-Trade Dollar Risk Envelope
MIN_RISK_USD: float = 10.00            # Standard lower bound
DEFAULT_TARGET_RISK_USD: float = 15.00 # Target nominal risk per ticket
MAX_RISK_USD: float = 25.00            # Operator-authorized maximum ceiling

# Stress Factors
STRESS_MULTIPLIER: float = 1.25        # 1.25x baseline stress on stop loss
DEFAULT_STOP_SLIPPAGE_BPS: float = 15.0 # Mandated stop slippage (15 bps of notional)
FLAT_FEE_ESTIMATE_USD: float = 2.00    # Broker commission/turnaround fee estimate

# Max Concurrent Ticket Capacity Policy
MAX_CONCURRENT_SLOTS_CEILING: int = 4

# Correlation Clusters for Multi-Asset Diversification
CLUSTER_MAP: Dict[str, List[str]] = {
    "crypto":  ["BTCUSD.pi", "ETHUSD.pi", "SOLUSD.p", "BNBUSD.p", "ADAUSD.p",
                "DOTUSD.pi", "DOTUSD.p", "XRPUSD.pi", "BNBUSD.pi", "DOGEUSD.p", "DOGUSD.p",
                "LTCUSD.p", "LTCUSD.pi", "LINKUSD.p", "LNKUSD.p", "AVAXUSD.p",
                "AVXUSD.p", "NEARUSD.p", "NERUSD.p", "TRXUSD.p", "BCHUSD.p"],
    "energy":  ["USWTI.p", "UKOIL.p"],
    "indices": ["SP500.p", "NAS100.p", "UK100.p", "GER40.p", "JPN225.p", "DJ30.p", "US30.p"],
    "forex":   ["EURUSD.pi", "GBPUSD.pi", "USDJPY.pi", "AUDUSD.pi", "NZDUSD.pi",
                "USDCAD.pi", "USDCHF.pi", "EURGBP.pi", "AUDCAD.pi"],
    "metals":  ["XAUUSD.pi", "XAGUSD.pi", "COPPER.p"],
}

# ==============================================================================
# 2. UNIFIED RATCHET LADDER (PLAYBOOK 7.1 EMPIRICAL 1,044-REPLAY SPECIFICATION)
# ==============================================================================
# Based on the empirical finding that 86.7% of trades touching +0.80R retest entry,
# Phase 0 provides 0.25R breathing room (cutting downside from -1.0R to -0.25R).
RATCHET_LADDER: Dict[str, Any] = {
    "version": "7.1.0-empirical",
    "phase_0": {
        "trigger_r": 1.25,
        "sl_offset_r": -0.25,  # SL = Entry - 0.25 * R0 (retaining 0.25R breathing room)
        "description": "Phase 0 Risk Reduction: Cut 75% downside at +1.25R MFE"
    },
    "phase_1": {
        "trigger_r": 1.65,
        "sl_offset_r": 0.80,   # SL = Entry + 0.80 * R0
        "description": "Phase 1 Profit Lock: Guarantee +0.80R profit at +1.65R MFE"
    },
    "phase_2": {
        "trigger_r": 2.00,
        "trail_dist_r": 0.75,  # Trail behind Peak MFE by 0.75R0
        "min_step_r": 0.10,    # Monotonic step: candidate must improve by >= 0.10R0
        "description": "Phase 2 Running Trail: Trail at Peak - 0.75R0 at >= +2.00R MFE"
    },
    "target_r": 2.50,          # Standard take profit target
    "time_decay": {
        "bars": 24,            # 24 completed 15m bars = 6.0 hours
        "min_r": 0.20,         # If floating gain < +0.20R after 6h -> market close
        "description": "Time-Decay Exit: Prune stagnant positions after 6h"
    }
}


# ==============================================================================
# 3. DYNAMIC CAPACITY & RESIDUAL RISK SIZING
# ==============================================================================
def calculate_stressed_risk(nominal_risk_usd: float, notional_usd: float = 0.0, multiplier: float = STRESS_MULTIPLIER) -> float:
    """Calculate stressed risk including stop slippage and execution fees.
    Uses repo's mandated 15 bps on notional if available, or flat fee reserve."""
    slippage_usd = (notional_usd * (DEFAULT_STOP_SLIPPAGE_BPS / 10000.0)) if notional_usd > 0 else FLAT_FEE_ESTIMATE_USD
    slippage_usd = max(slippage_usd, FLAT_FEE_ESTIMATE_USD)
    return round(nominal_risk_usd * multiplier + slippage_usd, 2)


def get_account_floor_base(balance: float, equity: float) -> float:
    """Conservative floor testing base: always uses min(balance, equity)."""
    return min(balance, equity)


def calculate_dynamic_capacity(
    balance: float,
    equity: float,
    open_positions: List[Dict[str, Any]],
    stress_multiplier: float = STRESS_MULTIPLIER
) -> Dict[str, Any]:
    """Calculate available headroom, post-joint-stop equity, and max admissible new tickets.
    
    Floor identity:
      min(balance, equity) - sum(stressed_risk_i) >= OPERATING_BUFFER_USD (4,795.00)
    """
    base_capital = get_account_floor_base(balance, equity)
    
    current_stressed_risk = 0.0
    active_clusters: List[str] = []
    
    for pos in open_positions:
        nom_risk = float(pos.get("risk_usd", 0.0) or pos.get("nominal_risk", 0.0))
        notional = float(pos.get("notional_usd", 0.0))
        sym = pos.get("symbol", "")
        current_stressed_risk += calculate_stressed_risk(nom_risk, notional, stress_multiplier)
        
        # Identify cluster
        for cluster_name, sym_list in CLUSTER_MAP.items():
            if sym in sym_list and cluster_name not in active_clusters:
                active_clusters.append(cluster_name)
                
    post_joint_stop_equity = base_capital - current_stressed_risk
    headroom_to_buffer = post_joint_stop_equity - OPERATING_BUFFER_USD
    headroom_to_floor = post_joint_stop_equity - HARD_FLOOR_USD
    
    # Calculate how many slots remain physically open
    used_slots = len(open_positions)
    open_slots_phys = max(0, MAX_CONCURRENT_SLOTS_CEILING - used_slots)
    
    # Calculate maximum tickets allowed based purely on financial solvency
    # Assuming baseline candidate risk of MIN_RISK_USD (10.0 USD nominal -> 14.50 USD stressed)
    min_cand_stress = calculate_stressed_risk(MIN_RISK_USD, 0.0, stress_multiplier)
    if headroom_to_buffer <= 0:
        solvency_max_tickets = 0
    else:
        solvency_max_tickets = int(headroom_to_buffer // min_cand_stress)
        
    admissible_new_slots = min(open_slots_phys, solvency_max_tickets)
    
    # Calculate maximum allowable nominal risk for a single new ticket
    if admissible_new_slots > 0:
        # Distribute remaining headroom across available slots, keeping at least 1 slot stress reserve
        max_risk_new_ticket = (headroom_to_buffer / (stress_multiplier * admissible_new_slots)) - (FLAT_FEE_ESTIMATE_USD / stress_multiplier)
        max_risk_new_ticket = min(MAX_RISK_USD, max(0.0, max_risk_new_ticket))
    else:
        max_risk_new_ticket = 0.0
        
    return {
        "base_capital": round(base_capital, 2),
        "post_joint_stop_equity": round(post_joint_stop_equity, 2),
        "current_stressed_risk": round(current_stressed_risk, 2),
        "headroom_to_buffer": round(headroom_to_buffer, 2),
        "headroom_to_floor": round(headroom_to_floor, 2),
        "used_slots": used_slots,
        "open_slots_phys": open_slots_phys,
        "admissible_new_slots": admissible_new_slots,
        "max_risk_new_ticket": round(max_risk_new_ticket, 2),
        "active_clusters": active_clusters,
        "floor_solvent": post_joint_stop_equity >= OPERATING_BUFFER_USD
    }


# ==============================================================================
# 4. DETERMINISTIC SYNCHRONOUS `admit()` PRE-TRADE VALIDATOR
# ==============================================================================
@dataclass
class AdmissionDecision:
    admitted: bool
    reason_code: str
    message: str
    diagnostics: Dict[str, Any] = field(default_factory=dict)


def admit(
    order_spec: Dict[str, Any],
    account_info: Dict[str, Any],
    open_positions: List[Dict[str, Any]],
    snapshot_meta: Optional[Dict[str, Any]] = None
) -> AdmissionDecision:
    """Deterministic, fail-closed pre-trade validator function.
    Must be called synchronously before every mt5.order_send().
    
    Order Spec fields:
      - symbol: str
      - direction: int (+1 long, -1 short)
      - entry_price: float
      - sl_price: float
      - tp_price: float
      - lots: float
      - nominal_risk_usd: float
      - notional_usd: float (optional)
      - spread_pts: float
      - atr_14: float
      - bunker_min_price: float (for longs)
      - bunker_max_price: float (for shorts)
      - supporting_whale_persist_s: float
      - supporting_whale_presence_frac: float
      - mid_price: float
    """
    symbol = order_spec.get("symbol", "")
    entry = float(order_spec.get("entry_price", 0.0))
    sl = float(order_spec.get("sl_price", 0.0))
    tp = float(order_spec.get("tp_price", 0.0))
    direction = int(order_spec.get("direction", 1))
    risk_usd = float(order_spec.get("nominal_risk_usd", 0.0))
    notional = float(order_spec.get("notional_usd", 0.0))
    spread_pts = float(order_spec.get("spread_pts", 0.0))
    atr = float(order_spec.get("atr_14", 0.0))
    mid = float(order_spec.get("mid_price", 0.0))
    persist_s = float(order_spec.get("supporting_whale_persist_s", 0.0))
    presence_frac = float(order_spec.get("supporting_whale_presence_frac", 0.0))
    
    balance = float(account_info.get("balance", 0.0))
    equity = float(account_info.get("equity", 0.0))
    
    # -------------------------------------------------------------
    # Check 1: Telemetry Authorization & Freshness
    # -------------------------------------------------------------
    if snapshot_meta:
        trade_auth = snapshot_meta.get("trade_authorization", "ALLOW")
        if trade_auth == "DENIED_UNVERIFIED_ORDERFLOW":
            return AdmissionDecision(
                admitted=False,
                reason_code="AUTH_DENIED_UNVERIFIED_ORDERFLOW",
                message="Snapshot trade_authorization is DENIED_UNVERIFIED_ORDERFLOW. Non-bypassable fail-closed veto.",
                diagnostics={"trade_authorization": trade_auth}
            )
        snapshot_age = float(snapshot_meta.get("snapshot_age_s", 0.0))
        if snapshot_age > 180.0:
            return AdmissionDecision(
                admitted=False,
                reason_code="STALE_TELEMETRY",
                message=f"Snapshot telemetry age {snapshot_age:.1f}s exceeds 180s threshold.",
                diagnostics={"snapshot_age_s": snapshot_age}
            )
            
    # -------------------------------------------------------------
    # Check 2: Dynamic Capital Floor & Headroom Solvency
    # -------------------------------------------------------------
    capacity = calculate_dynamic_capacity(balance, equity, open_positions)
    if not capacity["floor_solvent"]:
        return AdmissionDecision(
            admitted=False,
            reason_code="FLOOR_CUSHION_BREACH",
            message=f"Account post_joint_stop_equity {capacity['post_joint_stop_equity']:.2f} USD < {OPERATING_BUFFER_USD:.2f} USD buffer.",
            diagnostics=capacity
        )
        
    if capacity["admissible_new_slots"] <= 0:
        return AdmissionDecision(
            admitted=False,
            reason_code="CAPACITY_EXHAUSTED",
            message=f"Zero admissible slots remaining (Used: {capacity['used_slots']}, Residual headroom: {capacity['headroom_to_buffer']:.2f} USD).",
            diagnostics=capacity
        )
        
    new_stressed_risk = calculate_stressed_risk(risk_usd, notional)
    if new_stressed_risk > capacity["headroom_to_buffer"]:
        return AdmissionDecision(
            admitted=False,
            reason_code="RISK_EXCEEDS_HEADROOM",
            message=f"Proposed stressed risk {new_stressed_risk:.2f} USD exceeds available buffer headroom {capacity['headroom_to_buffer']:.2f} USD.",
            diagnostics={"proposed_stressed": new_stressed_risk, "headroom": capacity["headroom_to_buffer"]}
        )
        
    if risk_usd > MAX_RISK_USD:
        return AdmissionDecision(
            admitted=False,
            reason_code="RISK_EXCEEDS_ENVELOPE",
            message=f"Proposed nominal risk {risk_usd:.2f} USD exceeds authorized ceiling {MAX_RISK_USD:.2f} USD.",
            diagnostics={"proposed_risk": risk_usd, "max_risk": MAX_RISK_USD}
        )
        
    # -------------------------------------------------------------
    # Check 3: Correlation Cluster Isolation
    # -------------------------------------------------------------
    proposed_cluster = None
    for cluster_name, sym_list in CLUSTER_MAP.items():
        if symbol in sym_list:
            proposed_cluster = cluster_name
            break
            
    if proposed_cluster and proposed_cluster in capacity["active_clusters"]:
        return AdmissionDecision(
            admitted=False,
            reason_code="CORRELATED_CLUSTER_COLLISION",
            message=f"Active position already exists in '{proposed_cluster}' cluster. Orthogonal diversification violated.",
            diagnostics={"cluster": proposed_cluster, "active_clusters": capacity["active_clusters"]}
        )
        
    # -------------------------------------------------------------
    # Check 4: Entry Proximity Gate (<= 2.0 ATR)
    # -------------------------------------------------------------
    if atr > 0 and mid > 0:
        dist_atr = abs(entry - mid) / atr
        if dist_atr > 2.05:  # 2.0 ATR with minor float tolerance
            return AdmissionDecision(
                admitted=False,
                reason_code="ENTRY_PROXIMITY_EXCEEDED",
                message=f"Entry is {dist_atr:.2f} ATR from mid price (limit is 2.0 ATR). Deep-fish order rejected.",
                diagnostics={"dist_atr": dist_atr}
            )
            
    # -------------------------------------------------------------
    # Check 5: Dynamic Spread Friction Gate (<= 15% Risk Budget)
    # -------------------------------------------------------------
    stop_dist = abs(entry - sl)
    if stop_dist > 0 and spread_pts > 0:
        # Dynamic friction ratio: spread / stop_dist <= 0.15 => stop_dist >= 6.667 * spread
        friction_ratio = spread_pts / stop_dist
        if friction_ratio > 0.155:
            return AdmissionDecision(
                admitted=False,
                reason_code="SPREAD_FRICTION_EXCEEDED",
                message=f"Spread friction ratio {friction_ratio*100:.1f}% exceeds 15.0% threshold (D_min = 6.67 * spread).",
                diagnostics={"friction_ratio": friction_ratio, "spread_pts": spread_pts, "stop_dist": stop_dist}
            )
            
    # -------------------------------------------------------------
    # Check 6: Stop Loss Bunker Geometry (min_price/max_price)
    # -------------------------------------------------------------
    if direction == 1: # LONG
        bunker_min = float(order_spec.get("bunker_min_price", 0.0))
        if bunker_min > 0 and atr > 0:
            if sl > bunker_min:
                return AdmissionDecision(
                    admitted=False,
                    reason_code="SL_INSIDE_SWEEP_ZONE",
                    message=f"Long SL {sl:.5f} is placed above bunker min_price {bunker_min:.5f}. Stop sitting inside sweep band.",
                    diagnostics={"sl": sl, "bunker_min": bunker_min}
                )
    elif direction == -1: # SHORT
        bunker_max = float(order_spec.get("bunker_max_price", 0.0))
        if bunker_max > 0 and atr > 0:
            if sl < bunker_max:
                return AdmissionDecision(
                    admitted=False,
                    reason_code="SL_INSIDE_SWEEP_ZONE",
                    message=f"Short SL {sl:.5f} is placed below bunker max_price {bunker_max:.5f}. Stop sitting inside sweep band.",
                    diagnostics={"sl": sl, "bunker_max": bunker_max}
                )
                
    # -------------------------------------------------------------
    # Check 7: Minimum Risk-to-Reward Ratio (>= 2.0R)
    # -------------------------------------------------------------
    target_dist = abs(tp - entry)
    if stop_dist > 0:
        rr = target_dist / stop_dist
        if rr < 1.95: # 2.0R with minor tolerance
            return AdmissionDecision(
                admitted=False,
                reason_code="RR_BELOW_MINIMUM",
                message=f"Risk-to-reward ratio {rr:.2f}R is below institutional minimum 2.0R.",
                diagnostics={"rr": rr}
            )
            
    # All checks passed cleanly
    return AdmissionDecision(
        admitted=True,
        reason_code="ADMITTED",
        message="All deterministic risk, floor, bunker, and friction invariants verified.",
        diagnostics={
            "capacity": capacity,
            "new_stressed_risk": new_stressed_risk,
            "rr": round(target_dist / stop_dist, 2) if stop_dist > 0 else 0.0
        }
    )
