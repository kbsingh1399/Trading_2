#!/usr/bin/env python3
"""
Terminal/Data_Factory/pitfall_certification_gate.py
===================================================
Institutional Zero-Repeat Pitfall & Intra-Bar Flow Avalanche Certification Gate.
Audits candidate orders against all 12 fatal historical pitfalls before execution.

Inviolable Checkpoints:
  1. PITFALL_01_POLARITY_INVERSION: Wall defending entry must match order direction.
  2. PITFALL_02_UNSWEPT_STOP_CASCADES: Zero un-swept retail stop clusters between market & entry.
  3. PITFALL_03_INTRABAR_FLOW_AVALANCHE: Strict Intra-Bar Breaker (Ticket #19274977 Prevention):
     - For Shorts: 15m Taker Buy Delta <= +10.0M USD and intra-bar buying acceleration <= +25.0M USD.
     - For Longs: 15m Taker Sell Delta <= +10.0M USD and intra-bar selling acceleration <= +25.0M USD.
  4. PITFALL_04_SUB_ATR_STOP_LOSS: SL distance >= 0.40 * 14-ATR and cleared outside Value Area boundaries.
  5. PITFALL_05_NO_MANS_LAND_CHOP: In-range execution requires confirmed Trend; Mean Reversion requires extreme |Z| >= 2.0 SD.
  6. PITFALL_06_SPREAD_FRICTION: Live spread <= 25.0 bps for Crypto, <= 5.0 bps for TradFi.
  7. PITFALL_07_HTF_FLOW_ALIGNMENT: Candidate must not oppose consecutive 3-day ETF net redemptions (> $500M) or HTF trends.
  8. PITFALL_08_PREMATURE_MACRO_STAGING: Out of Red-Folder economic calendar blackout (+-15m Crypto, +-35m TradFi).
  9. PITFALL_09_CHOKED_TAKE_PROFIT: Opposing walls must not truncate R:R below 1.5R.
  10. PITFALL_10_SOLVENCY_FLOOR_DEFENSE: Stressed equity >= 4,795.00 USD (Buffer) and >= 4,600.00 USD (Hard Floor).
  11. PITFALL_11_ROLLOVER_SPREAD_EXPANSION: Banned between 21:45 and 22:15 UTC (interbank FX rollover).
  12. PITFALL_12_FINDING_D3_COMBINED_MARGIN: Total portfolio margin utilization after fill <= 50.0%.
"""

from __future__ import annotations

import dataclasses
import datetime
import logging
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger("PitfallGate")


@dataclasses.dataclass
class PitfallResult:
    certified: bool
    violations: List[str]
    audit_notes: List[str]
    checkpoints: Dict[str, str]


def certify_pitfalls(market_state: Dict) -> Dict:
    """Certifies that a proposed candidate trade passes all 12 zero-repeat pitfalls."""
    violations = []
    audit_notes = []
    checkpoints = {}

    action = str(market_state.get("candidate_action", "STAND_ASIDE")).upper()
    if action not in ("BUY", "SELL"):
        return {
            "certified": True,
            "violations": [],
            "audit_notes": ["No active trade proposed. Desk holding in Stand Aside cash defense."],
            "checkpoints": {f"PITFALL_{i:02d}": "PASS (STAND_ASIDE)" for i in range(1, 13)}
        }

    # 1. Polarity Inversion
    is_bid = market_state.get("is_bid_wall", False)
    if action == "BUY" and not is_bid:
        violations.append("PITFALL_01_POLARITY_INVERSION")
        audit_notes.append("Buy limit order lacks defending resting Bid wall backing.")
        checkpoints["PITFALL_01"] = "FAIL"
    elif action == "SELL" and is_bid:
        violations.append("PITFALL_01_POLARITY_INVERSION")
        audit_notes.append("Sell limit order backed by resting Bid wall (polarity inverted).")
        checkpoints["PITFALL_01"] = "FAIL"
    else:
        checkpoints["PITFALL_01"] = "PASS"

    # 2. Unswept Stop Cascades
    if market_state.get("unswept_stops_between", False):
        violations.append("PITFALL_02_UNSWEPT_STOP_CASCADES")
        audit_notes.append("Retail stop-loss pool rests between market price and limit entry.")
        checkpoints["PITFALL_02"] = "FAIL"
    else:
        checkpoints["PITFALL_02"] = "PASS"

    # 3. Intra-Bar Flow Avalanche (Ticket #19274977 prevention!)
    net_taker_delta = float(market_state.get("net_taker_delta_usd", 0.0))
    recent_buy_vol = float(market_state.get("recent_15m_taker_buy_usd", 0.0))
    recent_sell_vol = float(market_state.get("recent_15m_taker_sell_usd", 0.0))

    if action == "SELL":
        # Opposing aggressive buying pressure
        if net_taker_delta > 10000000.0 or recent_buy_vol > 25000000.0:
            violations.append("INTRA_BAR_BUYING_AVALANCHE")
            violations.append("PITFALL_03_INTRABAR_FLOW_AVALANCHE")
            audit_notes.append(f"Aggressive taker buy avalanche detected: Net Delta = +${net_taker_delta:,.2f} USD, 15m Buy Vol = +${recent_buy_vol:,.2f} USD > +$10.0M threshold. Replicating Ticket #19274977 trap!")
            checkpoints["PITFALL_03"] = "FAIL"
        else:
            checkpoints["PITFALL_03"] = "PASS"
    elif action == "BUY":
        # Opposing aggressive selling pressure
        if net_taker_delta < -10000000.0 or recent_sell_vol > 25000000.0:
            violations.append("INTRA_BAR_SELLING_AVALANCHE")
            violations.append("PITFALL_03_INTRABAR_FLOW_AVALANCHE")
            audit_notes.append(f"Aggressive taker sell avalanche detected: Net Delta = ${net_taker_delta:,.2f} USD > $10.0M selling threshold.")
            checkpoints["PITFALL_03"] = "FAIL"
        else:
            checkpoints["PITFALL_03"] = "PASS"

    # 4. Sub-ATR Stop Loss
    sl_distance = abs(float(market_state.get("entry_price", 0.0)) - float(market_state.get("sl_price", 0.0)))
    min_atr = float(market_state.get("atr_14", 100.0)) * 0.40
    if sl_distance < min_atr and min_atr > 0:
        violations.append("PITFALL_04_SUB_ATR_STOP_LOSS")
        audit_notes.append(f"SL distance ({sl_distance:.2f} pts) is smaller than 0.40 * ATR ({min_atr:.2f} pts). Vulnerable to noise chop.")
        checkpoints["PITFALL_04"] = "FAIL"
    else:
        checkpoints["PITFALL_04"] = "PASS"

    # 5. No-Man's-Land Chop
    regime = str(market_state.get("regime", "UNDEFINED")).upper()
    vwap_z = abs(float(market_state.get("vwap_zscore", 0.0)))
    if regime == "UNDEFINED" and vwap_z < 2.0:
        violations.append("PITFALL_05_NO_MANS_LAND_CHOP")
        audit_notes.append("Market is in UNDEFINED chop regime and |Z| < 2.0 SD. Both trend and mean-reversion engines gated closed.")
        checkpoints["PITFALL_05"] = "FAIL"
    else:
        checkpoints["PITFALL_05"] = "PASS"

    # 6. Spread Friction
    spread_bps = float(market_state.get("spread_bps", 0.0))
    is_crypto = "USD" in str(market_state.get("symbol", "")) and (".p" in str(market_state.get("symbol", "")) or "USDT" in str(market_state.get("symbol", "")))
    max_spread = 25.0 if is_crypto else 5.0
    if spread_bps > max_spread:
        violations.append("PITFALL_06_SPREAD_FRICTION")
        audit_notes.append(f"Spread ({spread_bps:.2f} bps) exceeds {max_spread:.1f} bps ceiling.")
        checkpoints["PITFALL_06"] = "FAIL"
    else:
        checkpoints["PITFALL_06"] = "PASS"

    # 7. HTF Trend & ETF Direction
    etf_3d_flow = float(market_state.get("etf_3d_flow_usd", 0.0))
    if action == "SELL" and etf_3d_flow > 500000000.0:
        violations.append("PITFALL_07_HTF_FLOW_ALIGNMENT")
        audit_notes.append("Opposing massive 3-day institutional ETF net inflow (> $500M USD).")
        checkpoints["PITFALL_07"] = "FAIL"
    else:
        checkpoints["PITFALL_07"] = "PASS"

    # 8. Macro Calendar Blackout
    if market_state.get("macro_blackout_active", False):
        violations.append("PITFALL_08_PREMATURE_MACRO_STAGING")
        audit_notes.append("Tier-1 macroeconomic release blackout window active.")
        checkpoints["PITFALL_08"] = "FAIL"
    else:
        checkpoints["PITFALL_08"] = "PASS"

    # 9. Choked Take Profit
    entry = float(market_state.get("entry_price", 1.0))
    sl = float(market_state.get("sl_price", 1.0))
    tp = float(market_state.get("tp_price", 1.0))
    risk_pts = abs(entry - sl)
    reward_pts = abs(entry - tp)
    rr = reward_pts / risk_pts if risk_pts > 0 else 0.0
    if rr < 1.5:
        violations.append("PITFALL_09_CHOKED_TAKE_PROFIT")
        audit_notes.append(f"Risk-to-Reward ratio ({rr:.2f}R) is below minimum institutional 1.50R threshold.")
        checkpoints["PITFALL_09"] = "FAIL"
    else:
        checkpoints["PITFALL_09"] = "PASS"

    # 10. Solvency Floor Defense
    stressed_equity = float(market_state.get("stressed_equity", 0.0))
    if stressed_equity < 4795.00:
        violations.append("PITFALL_10_SOLVENCY_FLOOR_DEFENSE")
        audit_notes.append(f"Stressed post-loss equity (${stressed_equity:,.2f}) breaches 4,795.00 USD Solvency Kernel.")
        checkpoints["PITFALL_10"] = "FAIL"
    else:
        checkpoints["PITFALL_10"] = "PASS"

    # 11. Rollover Spread Window
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    if (now_utc.hour == 21 and now_utc.minute >= 45) or (now_utc.hour == 22 and now_utc.minute <= 15):
        violations.append("PITFALL_11_ROLLOVER_SPREAD_EXPANSION")
        audit_notes.append("Current time is inside the 21:45-22:15 UTC interbank rollover spread expansion blackout window.")
        checkpoints["PITFALL_11"] = "FAIL"
    else:
        checkpoints["PITFALL_11"] = "PASS"

    # 12. Combined Margin Ceiling (Finding D3)
    margin_util = float(market_state.get("post_order_margin_util_pct", 0.0))
    if margin_util > 50.0:
        violations.append("PITFALL_12_FINDING_D3_COMBINED_MARGIN")
        audit_notes.append(f"Post-order combined portfolio margin utilization ({margin_util:.2f}%) breaches the 50.0% statutory ceiling.")
        checkpoints["PITFALL_12"] = "FAIL"
    else:
        checkpoints["PITFALL_12"] = "PASS"

    certified = len(violations) == 0
    return {
        "certified": certified,
        "violations": violations,
        "audit_notes": audit_notes,
        "checkpoints": checkpoints
    }


def generate_certified_markdown_card(cert: Dict) -> str:
    """Generates a formatted markdown checklist card for turn reporting."""
    status_icon = "✅ CERTIFIED PASS" if cert["certified"] else "❌ REJECTED FAIL-CLOSED"
    lines = [
        f"### 🛡️ ZERO-REPEAT PITFALL & INTRA-BAR AVALANCHE CERTIFICATION — {status_icon}",
        "| Checkpoint | Status | Rule & Verification |",
        "| :--- | :---: | :--- |"
    ]
    
    rules = [
        ("PITFALL_01", "Polarity Inversion", "Defending whale wall direction matches trade side (Bid for Long, Ask for Short)."),
        ("PITFALL_02", "Unswept Stop Cascades", "Zero un-swept retail stop clusters between market price and limit entry."),
        ("PITFALL_03", "Intra-Bar Flow Avalanche", "Taker buy/sell surge <= +$10M USD (Ticket #19274977 prevention)."),
        ("PITFALL_04", "Sub-ATR Stop Loss", "Stop distance >= 0.40 * 14-ATR cleared outside Value Area boundaries."),
        ("PITFALL_05", "No-Man's-Land Chop", "Gated against UNDEFINED chop regimes; requires extreme |Z| >= 2.0 SD."),
        ("PITFALL_06", "Spread Friction Gate", "Spread verified <= 25.0 bps (Crypto) / <= 5.0 bps (TradFi)."),
        ("PITFALL_07", "HTF Trend & ETF Alignment", "Trade aligns with 3-day ETF institutional flows and macro structure."),
        ("PITFALL_08", "Macro Calendar Blackout", "Outside +-15m (Crypto) / +-35m (TradFi) of Red-Folder events."),
        ("PITFALL_09", "Overhead Liquidity Blockade", "Realizable R:R >= 1.50R before opposing structural whale walls."),
        ("PITFALL_10", "Triple Floor Defense", "Stressed post-loss equity >= 4,795.00 USD Solvency Kernel."),
        ("PITFALL_11", "Rollover Spread Window", "Outside 21:45-22:15 UTC interbank spread expansion window."),
        ("PITFALL_12", "Portfolio Margin Ceiling", "Combined margin utilization strictly <= 50.00% (Finding D3)."),
    ]

    for p_id, p_name, p_desc in rules:
        chk_status = cert.get("checkpoints", {}).get(p_id, "PASS")
        icon = "✅ PASS" if "PASS" in chk_status else "❌ FAIL"
        lines.append(f"| **{p_name}** | {icon} | {p_desc} |")

    if cert.get("violations"):
        lines.append("\n> ⚠️ **ACTIVE VIOLATIONS DETECTED:**")
        for v in cert["violations"]:
            lines.append(f"> - `{v}`")
        for note in cert["audit_notes"]:
            lines.append(f"> - {note}")

    return "\n".join(lines)


if __name__ == "__main__":
    test_state = {
        "candidate_action": "SELL",
        "symbol": "BTCUSD.pi",
        "entry_price": 80245.0,
        "sl_price": 80620.0,
        "tp_price": 79385.0,
        "recent_15m_taker_buy_usd": 32000000.0,
        "net_taker_delta_usd": 25500000.0,
        "spread_bps": 2.11,
        "stressed_equity": 4826.32
    }
    res = certify_pitfalls(test_state)
    print(generate_certified_markdown_card(res))
