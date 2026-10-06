"""Multi-agent deliberation contract for the Arena Brain (OX_ALPHA_61 D3).

Tri-specialist swarm - every perspective is a bounded, deterministic
transform of the same sealed factory data the local engine sees (the LLM
agents fill the identical schema; the deterministic analysts below are the
offline/no-LLM path and the attestation baseline):

  Agent 1  ORDERFLOW ANALYST    session VWAP z-scores, CVD 1m/5m/15m
                               divergence, L2 20-level skew, L3 resting whale
                               walls (>= 150k USD persisting >= 180 s)
  Agent 2  POSITION MANAGER    open positions, R-multiples, 3-phase ratchet
                               state (0.80R BE lock, 1.50R profit lock,
                               2.00R runner trail), MAX_CONCURRENT = 2
  Agent 3  MACRO RISK ANALYST  Tier-1 calendar blackouts, source-weighted
                               sentiment, cross-asset correlation, cushion
                               vs the 4,775.00 USD hard floor

SYNTHESIS: the three perspectives never bypass anything - they are fused
through the unchanged PioneerDecisionEngine conviction vector (orderflow 30%,
cascade 25%, stops 15%, whale 15%, macro 15%) and the final SELECT/HOLD is
an attested response under Terminal/Headless/llm_contract.py (exact numeric
echoes, invariant digest, sealed hashes). A specialist cannot invent a
number: every driver cites a JSON pointer that must resolve in the request.
"""
from __future__ import annotations

import math
from typing import Dict, List, Optional

from Terminal.Risk_Sizing_Engine import number

SWARM_VERSION = "omni.arena_swarm.v1"

SPECIALISTS = [
    {"agent": 1, "name": "Orderflow Analyst",
     "mandate": "Session VWAP z-scores, CVD 1m/5m/15m divergence, L2 20-level "
                "skew, L3 resting whale walls >= 150k USD persisting >= 180s.",
     "output_schema": {"perspective": "ORDERFLOW", "conviction": "[-1,1]",
                       "drivers": ["<=5 strings citing /payload pointers"]}},
    {"agent": 2, "name": "Position Manager",
     "mandate": "R-multiples of open positions, 3-phase ratchet state "
                "(0.80R BE lock, 1.50R profit lock, 2.00R runner trail), "
                "MAX_CONCURRENT = 2 capacity.",
     "output_schema": {"perspective": "POSITIONS", "conviction": "[-1,1]",
                       "drivers": ["<=5 strings citing /positions pointers"]}},
    {"agent": 3, "name": "Macro Risk Analyst",
     "mandate": "Tier-1 economic calendar blackouts, source-weighted sentiment, "
                "cross-asset correlation, portfolio cushion vs the 4,775.00 USD "
                "hard floor.",
     "output_schema": {"perspective": "MACRO", "conviction": "[-1,1]",
                       "drivers": ["<=5 strings citing /macro pointers"]}},
]

HARD_FLOOR_USD = 4775.0
RATCHET_PHASES = {"be_trigger_r": 0.80, "profit_trigger_r": 1.50, "runner_trigger_r": 2.00}
MAX_CONCURRENT = 2


def _clamp(x, lo=-1.0, hi=1.0):
    return max(lo, min(hi, float(x)))


# ------------------------------------------------- Agent 1: orderflow analyst
def orderflow_analyst(payload: Dict) -> Dict:
    """Deterministic Agent 1. Conviction from the live tape + book + walls."""
    of = payload.get("orderflow") or {}
    drivers, conviction_parts = [], []

    cvd1, cvd5, cvd15 = of.get("cvd_1m"), of.get("cvd_5m"), of.get("cvd_15m")
    if cvd1 is not None and cvd5 is not None:
        divergence = _clamp(number(cvd1) / 5.0 - number(cvd5) / 5.0, -1.0, 1.0) \
            if abs(number(cvd5)) > 0 else 0.0
        # Divergence sign: recent pace ABOVE the 5m average = buying pressure.
        conviction_parts.append(0.35 * _clamp(number(cvd1) / 5.0 / max(abs(number(cvd5)) / 5.0, 1e-9)
                                              if number(cvd5) != 0 else 0.0))
        drivers.append(f"/payload/orderflow/cvd_1m={number(cvd1):.0f} vs "
                       f"/payload/orderflow/cvd_5m={number(cvd5):.0f}")

    depth_imb = of.get("depth_imbalance")
    if depth_imb is not None:
        conviction_parts.append(0.30 * _clamp(number(depth_imb)))
        drivers.append(f"/payload/orderflow/depth_imbalance={number(depth_imb):.3f}")

    walls = payload.get("l3_orders") or []
    persistent = [w for w in walls
                  if number(w.get("notional_usd")) >= 150_000.0
                  and number(w.get("persistence_sec")) >= 180.0]
    if persistent:
        bid_usd = sum(number(w.get("notional_usd")) for w in persistent
                      if str(w.get("side")).upper() == "BUY")
        ask_usd = sum(number(w.get("notional_usd")) for w in persistent
                      if str(w.get("side")).upper() == "SELL")
        if bid_usd + ask_usd > 0:
            wall_skew = (bid_usd - ask_usd) / (bid_usd + ask_usd)
            conviction_parts.append(0.35 * _clamp(wall_skew))
            drivers.append(f"/payload/l3_orders persistent walls bid_usd={bid_usd:.0f} "
                           f"ask_usd={ask_usd:.0f}")
    if not conviction_parts:
        return {"perspective": "ORDERFLOW", "conviction": 0.0, "drivers": [],
                "available": False}
    return {"perspective": "ORDERFLOW",
            "conviction": round(_clamp(sum(conviction_parts)), 6),
            "drivers": drivers[:5], "available": True}


# ------------------------------------------------ Agent 2: position manager
def position_manager(positions: List[Dict], *, asset: Optional[str] = None,
                     correlation: Optional[float] = None) -> Dict:
    """Deterministic Agent 2. Conviction reflects whether the BOOK has room
    and agrees with the candidate (R-multiples + ratchet state + capacity)."""
    rows = [p for p in (positions or []) if p]
    if not rows:
        return {"perspective": "POSITIONS", "conviction": 0.0, "drivers": [],
                "available": False, "filled": 0, "capacity_open": True}
    drivers, conviction = [], 0.0
    for p in rows:
        entry = number(p.get("price_open"))
        sl = number(p.get("sl")) or entry
        initial_r = max(abs(entry - sl), 1e-9)
        # R-multiple from the current quote if provided, else from profit.
        quote_price = number(p.get("current_price"), 0.0)
        if quote_price > 0:
            gain_r = (quote_price - entry) / initial_r if p.get("direction") == "LONG" \
                else (entry - quote_price) / initial_r
        else:
            notional = abs(number(p.get("volume")) * number(p.get("contract_size", 100.0)))
            gain_r = number(p.get("profit_usd")) / max(notional * initial_r / max(entry, 1e-9), 1e-9) \
                if entry > 0 else 0.0
        phase = ("RUNNER" if gain_r >= RATCHET_PHASES["runner_trigger_r"]
                 else "PROFIT_LOCK" if gain_r >= RATCHET_PHASES["profit_trigger_r"]
                 else "BE_LOCK" if gain_r >= RATCHET_PHASES["be_trigger_r"] else "OPEN")
        drivers.append(f"/positions/{p.get('ticket')} gain_r={gain_r:.2f} phase={phase}")
        # A profitable, ratchet-protected book supports continuation; a
        # bleeding book argues against adding correlated risk.
        conviction += _clamp(gain_r / 2.0)
    conviction = _clamp(conviction / max(len(rows), 1))
    capacity_open = len(rows) < MAX_CONCURRENT
    if asset and any(str(p.get("symbol", "")).startswith(str(asset)) for p in rows):
        drivers.append(f"/positions already holds {asset}: MAX_CONCURRENT guard")
        conviction = 0.0
    if correlation is not None and abs(number(correlation)) >= 0.60:
        conviction *= 0.5
        drivers.append(f"cross_asset_correlation={number(correlation):.2f}")
    return {"perspective": "POSITIONS", "conviction": round(conviction, 6),
            "drivers": drivers[:5], "available": True,
            "filled": len(rows), "capacity_open": capacity_open}


# ------------------------------------------------ Agent 3: macro risk analyst
def macro_risk_analyst(macro: Dict, *, equity_usd: float = 5000.0) -> Dict:
    """Deterministic Agent 3. Blackout, sentiment, and the floor cushion."""
    source = macro or {}
    if source.get("data_factory") and not source.get("blackout_active") and \
            "blackout_active" not in source:
        source = {**source.get("data_factory", {}), **source}
    drivers, conviction, blocked = [], 0.0, bool(source.get("blackout_active"))
    if blocked:
        drivers.append("/macro/blackout_active=True: Tier-1 window, no new risk")
        return {"perspective": "MACRO", "conviction": 0.0, "drivers": drivers,
                "available": True, "blocked": True}

    scores = source.get("asset_scores") or {}
    if scores:
        values = [number(v) for v in scores.values() if number(v) != 0]
        if values:
            sentiment = _clamp(sum(values) / len(values))
            conviction += 0.4 * sentiment
            drivers.append(f"/macro/asset_scores mean={sentiment:.3f}")
    premium = number(source.get("coinbase_premium_bps"), 0.0)
    if premium:
        conviction += 0.3 * _clamp(premium / 10.0)
        drivers.append(f"/macro/coinbase_premium_bps={premium:.2f}")
    etf = number(source.get("etf_net_flow_musd_1d"), 0.0)
    if etf:
        conviction += 0.3 * math.tanh(etf / 500.0)
        drivers.append(f"/macro/etf_net_flow_musd_1d={etf:.1f}")

    cushion = number(equity_usd) - HARD_FLOOR_USD
    drivers.append(f"cushion_vs_floor={cushion:.2f} USD "
                   f"(floor {HARD_FLOOR_USD:.2f})")
    if cushion <= 0:
        return {"perspective": "MACRO", "conviction": 0.0, "drivers": drivers,
                "available": True, "blocked": True}
    if cushion < 50.0:                     # thin cushion: halve conviction
        conviction *= 0.5
    return {"perspective": "MACRO", "conviction": round(_clamp(conviction), 6),
            "drivers": drivers[:5], "available": True, "blocked": False,
            "cushion_usd": round(cushion, 2)}


# ------------------------------------------------------------- deliberation
def deliberate(payload: Dict, positions: List[Dict], macro: Dict, *,
               equity_usd: float = 5000.0, correlation: Optional[float] = None) -> Dict:
    """Run the full tri-specialist deliberation deterministically.

    Returns the deliberation record: three perspectives + the synthesis note
    that feeds PioneerDecisionEngine + llm_contract. The pioneer conviction
    itself is computed by the UNCHANGED PioneerDecisionEngine.evaluate (the
    synthesis never re-weights or overrides it)."""
    perspectives = [orderflow_analyst(payload),
                    position_manager(positions, correlation=correlation),
                    macro_risk_analyst(macro, equity_usd=equity_usd)]
    blocked = any(p.get("blocked") for p in perspectives)
    capacity_open = all(p.get("capacity_open", True) for p in perspectives)
    return {"swarm_version": SWARM_VERSION, "specialists": SPECIALISTS,
            "perspectives": perspectives,
            "blocked": blocked, "capacity_open": capacity_open,
            "synthesis": {"engine": "PioneerDecisionEngine",
                          "weights": {"orderflow": 0.30, "cascade": 0.25,
                                      "stops": 0.15, "whale": 0.15, "macro": 0.15},
                          "note": "Perspectives are evidence only; the conviction "
                                  "vector and the SELECT/HOLD attestation are "
                                  "computed by PioneerDecisionEngine.evaluate and "
                                  "validated by llm_contract (exact numeric echoes)."}}


def build_brain_request(*, as_of: float, asset: str, payload: Dict, features: Dict,
                        pioneer: Optional[Dict], candidate: Dict,
                        positions: List[Dict], macro: Dict,
                        equity_usd: float = 5000.0) -> Dict:
    """The full request the Arena Brain deliberates over: snapshot + swarm
    perspectives + llm_contract consultation envelope (one structure, three
    specialists, one deterministic synthesis)."""
    from Terminal.Headless.llm_contract import build_consultation_request

    deliberation = deliberate(payload, positions, macro, equity_usd=equity_usd)
    consultation = build_consultation_request(as_of=as_of, asset=asset,
                                               features=features, pioneer=pioneer,
                                               candidate=candidate)
    # The deliberation record rides inside the consultation envelope (the
    # validated surface): specialist drivers are citeable as
    # /deliberation/perspectives/N/... by the attested response.
    consultation["deliberation"] = deliberation
    return {"as_of": float(as_of), "asset": str(asset).upper(),
            "payload": payload, "positions": positions, "macro": macro,
            "deliberation": deliberation, "consultation": consultation}
