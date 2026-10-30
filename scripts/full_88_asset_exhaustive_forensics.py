#!/usr/bin/env python3
"""
scripts/full_88_asset_exhaustive_forensics.py
=============================================
Exhaustive, asset-by-asset 15-pillar forensic analyzer for all 88 spread-cleared assets.
Reads individual master dossiers in docs/dossiers/<SYMBOL>_MASTER_DOSSIER.json.
Enforces the mandatory CoinGlass Footprint Signals standard.
Emits comprehensive analysis to docs/trade_plans/CYCLE_038_EXHAUSTIVE_88_ASSET_ANALYSIS.md
and docs/trade_plans/CYCLE_038_EXHAUSTIVE_88_ASSET_DATABASE.json.
"""

from __future__ import annotations
import datetime
import json
import pathlib
import sys
from typing import Any, Dict, List, Optional

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOSSIERS_DIR = ROOT / "docs" / "dossiers"
TRADE_PLANS_DIR = ROOT / "docs" / "trade_plans"
ELIGIBLE_FILE = ROOT / "scripts" / "cycle_038_eligible_dossiers.txt"

def find_dossier(symbol: str) -> Optional[pathlib.Path]:
    clean = symbol.replace(".pi", "").replace(".p", "").replace("/", "").upper()
    candidates = [
        f"{clean}_MASTER_DOSSIER.json",
        f"{clean}USD_MASTER_DOSSIER.json",
    ]
    if clean.endswith("USD"):
        base = clean[:-3]
        candidates.extend([f"{base}_MASTER_DOSSIER.json", f"{base}USD_MASTER_DOSSIER.json"])
    
    for c in candidates:
        p = DOSSIERS_DIR / c
        if p.exists() and p.stat().st_size > 50:
            return p
    return None

def analyze_asset(symbol: str, path: pathlib.Path) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)

    fm = d.get("footprint_and_macro", {})
    der = d.get("derivatives", {})
    liq = d.get("liquidations", {})
    wl2 = d.get("whales_and_l2", {})
    cvd = d.get("cvd", {})
    auc = d.get("auction", {})
    tech = d.get("technicals", {})
    telem = d.get("telemetry", {})
    specs = d.get("specs", {})

    # 1. Telemetry
    bid = telem.get("bid", 0.0)
    ask = telem.get("ask", 0.0)
    mid = telem.get("mid", (bid + ask)/2 if bid and ask else 0.0)
    spread_bps = telem.get("spread_bps", 0.0)
    contract_size = specs.get("contract_size", 1.0)
    point = specs.get("point", 0.01)

    # 2. Technicals
    vwap = tech.get("vwap", 0.0)
    vwap_z = tech.get("vwap_z", 0.0)
    rsi = tech.get("rsi_14", 50.0)
    atr = tech.get("atr_14", 0.0)
    u1 = tech.get("u1", 0.0)
    l1 = tech.get("l1", 0.0)

    # 3. Auction
    poc = auc.get("daily_poc", 0.0)
    vah = auc.get("daily_vah", 0.0)
    val = auc.get("daily_val", 0.0)
    regime = auc.get("auction_regime", "UNKNOWN")
    bias = auc.get("session_bias", "NEUTRAL")

    # 4. CVD
    cvd_table = cvd.get("table", []) or []
    cvd_5m = cvd_table[0].get("delta_pct", 0.0) if len(cvd_table) > 0 else 0.0
    cvd_1h = cvd_table[2].get("delta_pct", 0.0) if len(cvd_table) > 2 else 0.0
    cvd_bias = cvd_table[0].get("bias", "NEUTRAL") if cvd_table else "NEUTRAL"

    # 5. Whale & Stops
    whale_ladder = wl2.get("whale_ladder", []) or []
    hd_stops = liq.get("hd_stops_ladder", []) or []
    ob_ladder = wl2.get("ob_ladder", []) or []

    # 6. Liquidations
    mp_24h = liq.get("mp_24h", {}) or {}
    s_pain = mp_24h.get("short_max_pain_price") or 0.0
    l_pain = mp_24h.get("long_max_pain_price") or 0.0

    # 7. Derivatives
    funding_row = der.get("funding_row", {}) or {}
    bin_funding = funding_row.get("USDT_Binance") or "0.0100%"
    oi_row = der.get("oi_row", {}) or {}
    tot_oi = oi_row.get("Total_OI_USD") or "N/A"
    oi_chg = oi_row.get("24h_Total_Change") or "N/A"

    # 8. CoinGlass Footprint Signals (Mandatory Standard)
    signals = fm.get("signals", []) or []
    bull_absorp = [s for s in signals if "absorp" in str(s.get("type", "")).lower() and s.get("bias") == "BULLISH"]
    bear_absorp = [s for s in signals if "absorp" in str(s.get("type", "")).lower() and s.get("bias") == "BEARISH"]
    trapped_l = [s for s in signals if "trapped long" in str(s.get("type", "")).lower()]
    trapped_s = [s for s in signals if "trapped short" in str(s.get("type", "")).lower()]
    divergences = [s for s in signals if "div" in str(s.get("type", "")).lower()]
    exhaustions = [s for s in signals if "exhaust" in str(s.get("type", "")).lower()]

    # 9. Confluence Scoring & Dual-Model Trade Formulation (Model 1 Mean Reversion vs Model 2 Trend Pullback)
    score = 50.0  # baseline
    reasons = []

    # Detect Market Regime & Trend Alignment across Multiple Feeds
    ema_20 = tech.get("ema_20", 0.0) or 0.0
    ema_50 = tech.get("ema_50", 0.0) or 0.0
    ema_200 = tech.get("ema_200", 0.0) or 0.0
    fib_ote = auc.get("fib_ote", 0.0) or 0.0
    fib_gp_low = auc.get("fib_gp_low", 0.0) or 0.0
    fib_gp_high = auc.get("fib_gp_high", 0.0) or 0.0

    is_bull_trend = (
        ("BULL" in regime.upper() or "UP" in regime.upper() or "EXPANSION" in regime.upper()) or
        (mid > vwap > 0 and cvd_bias in ["BULLISH", "BUYING"]) or
        (ema_20 > ema_50 > ema_200 > 0 and mid > ema_50)
    )
    is_bear_trend = (
        ("BEAR" in regime.upper() or "DOWN" in regime.upper()) or
        (mid < vwap and vwap > 0 and cvd_bias in ["BEARISH", "SELLING"]) or
        (ema_20 < ema_50 < ema_200 and ema_200 > 0 and mid < ema_50)
    )
    is_range_bound = not (is_bull_trend or is_bear_trend) or "ROTATIONAL" in regime.upper() or "BALANCE" in regime.upper()

    # Footprint scoring (Mandatory Standard)
    if bull_absorp:
        score += 12.0
        reasons.append(f"Bullish Absorption ({len(bull_absorp)} clusters)")
    if bear_absorp:
        score += 8.0
        reasons.append(f"Bearish Absorption ({len(bear_absorp)} clusters)")
    if trapped_s:
        score += 10.0
        reasons.append("Trapped Shorts fuel squeeze")
    if trapped_l:
        score -= 5.0
        reasons.append("Trapped Longs overhead")
    if divergences:
        score += 8.0
        reasons.append(f"Delta Divergences ({len(divergences)})")

    # Whale defense
    if len(whale_ladder) >= 50:
        score += 10.0
        reasons.append(f"Whale Armor ({len(whale_ladder)} orders)")

    # Spread penalty / bonus
    if spread_bps > 20.0:
        score -= 10.0
    elif spread_bps < 3.0:
        score += 5.0

    score = max(10.0, min(98.0, score))
    digits = specs.get("digits", 2)
    effective_atr = max(atr, mid * 0.005 if mid else 1.0)

    # Formulate Action: DUAL-MODEL SELECTION
    action = "STAND_ASIDE_MONITOR"
    model_type = "NONE"
    entry = None
    sl = None
    tp = None
    rr = None

    if score >= 75.0:
        if is_bull_trend:
            # MODEL 2: Trend Continuation Pullback (Long)
            # Pullback to dynamic support: Session VWAP, POC, Fib Golden Zone, or EMA 20/50
            pullback_candidates = [lvl for lvl in [vwap, poc, fib_ote, fib_gp_low, ema_20, ema_50] if 0 < lvl < mid * 0.9995]
            if pullback_candidates:
                entry = round(max(pullback_candidates), digits)
                sl = round(entry - 1.5 * effective_atr, digits)
                dist = abs(entry - sl)
                tp = round(entry + 2.5 * dist, digits)
                rr = 2.50
                action = "MODEL_2_TREND_PULLBACK_BUY"
                model_type = "Model 2 Trend Pullback"
                reasons.append(f"Model 2 Bull Trend: Pullback to dynamic shelf ({entry:,.2f})")
        elif is_bear_trend:
            # MODEL 2: Trend Continuation Pullback (Short)
            pullback_res = [lvl for lvl in [vwap, poc, fib_ote, fib_gp_high, ema_20, ema_50] if lvl > mid * 1.0005]
            if pullback_res:
                entry = round(min(pullback_res), digits)
                sl = round(entry + 1.5 * effective_atr, digits)
                dist = abs(sl - entry)
                tp = round(entry - 2.5 * dist, digits)
                rr = 2.50
                action = "MODEL_2_TREND_PULLBACK_SELL"
                model_type = "Model 2 Trend Pullback"
                reasons.append(f"Model 2 Bear Trend: Pullback to dynamic resistance ({entry:,.2f})")
        
        # If not triggered by trend pullback, check MODEL 1: Mean Reversion Range Fade
        if action == "STAND_ASIDE_MONITOR":
            if val and (mid <= val * 1.005 or (l_pain and abs(mid - l_pain) / mid < 0.05)):
                # Buy sweep fade at VAL / Long Max Pain
                entry = round(min(val, l_pain if l_pain > 0 else val), digits)
                sl = round(entry - 1.5 * effective_atr, digits)
                dist = abs(entry - sl)
                tp = round(entry + 2.5 * dist, digits)
                rr = 2.50
                action = "MODEL_1_MEAN_REVERSION_BUY"
                model_type = "Model 1 Mean Reversion"
                reasons.append(f"Model 1 Mean Reversion: Probing range extreme / VAL ({val:,.2f})")
            elif vah and (mid >= vah * 0.995 or (s_pain and abs(mid - s_pain) / mid < 0.05)):
                # Sell sweep fade at VAH / Short Max Pain
                entry = round(max(vah, s_pain if s_pain > 0 else vah), digits)
                sl = round(entry + 1.5 * effective_atr, digits)
                dist = abs(sl - entry)
                tp = round(entry - 2.5 * dist, digits)
                rr = 2.50
                action = "MODEL_1_MEAN_REVERSION_SELL"
                model_type = "Model 1 Mean Reversion"
                reasons.append(f"Model 1 Mean Reversion: Probing range extreme / VAH ({vah:,.2f})")

    return {
        "symbol": symbol,
        "dossier_bytes": path.stat().st_size,
        "confluence_score": round(score, 1),
        "action": action,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "rr": rr,
        "reasons": reasons,
        "telemetry": {
            "bid": bid, "ask": ask, "mid": mid, "spread_bps": spread_bps,
            "contract_size": contract_size, "point": point
        },
        "technicals": {
            "vwap": vwap, "vwap_z": vwap_z, "rsi_14": rsi, "atr_14": atr, "u1": u1, "l1": l1
        },
        "auction": {
            "daily_poc": poc, "daily_vah": vah, "daily_val": val, "regime": regime, "bias": bias
        },
        "cvd": {
            "delta_5m": cvd_5m, "delta_1h": cvd_1h, "bias": cvd_bias
        },
        "whales": {
            "whale_count": len(whale_ladder), "stop_clusters_count": len(hd_stops), "ob_depth_count": len(ob_ladder)
        },
        "liquidations": {
            "short_max_pain": s_pain, "long_max_pain": l_pain
        },
        "derivatives": {
            "funding_binance": bin_funding, "total_oi": tot_oi, "oi_change_24h": oi_chg
        },
        "footprint_signals": {
            "total_count": len(signals),
            "bullish_absorptions": len(bull_absorp),
            "bearish_absorptions": len(bear_absorp),
            "trapped_longs": len(trapped_l),
            "trapped_shorts": len(trapped_s),
            "divergences": len(divergences),
            "exhaustions": len(exhaustions),
            "top_signals": [
                f"[{s.get('time')}] {s.get('tf')} · {s.get('type')} ({s.get('bias')}) @ {s.get('price')} | {s.get('headline')}"
                for s in signals[:3]
            ]
        }
    }

def main():
    symbols = [s.strip() for s in ELIGIBLE_FILE.read_text(encoding="utf-8").splitlines() if s.strip()]
    print(f"================================================================================")
    print(f"🔬 EXHAUSTIVE 88-ASSET 15-PILLAR & COINGLASS FOOTPRINT FORENSICS (CYCLE_038)")
    print(f"   Universe Size: {len(symbols)} Spread-Cleared Assets")
    print(f"================================================================================")

    audited = []
    missing = []
    for idx, sym in enumerate(symbols, 1):
        p = find_dossier(sym)
        if not p:
            missing.append(sym)
            continue
        res = analyze_asset(sym, p)
        audited.append(res)
        fp = res["footprint_signals"]
        print(f"[{idx:02d}/{len(symbols)}] {sym:<12} | Score: {res['confluence_score']:>4.1f}/100 | Action: {res['action']:<21} | Spread: {res['telemetry']['spread_bps']:>5.2f} bps | Whales: {res['whales']['whale_count']:>3} | FP Signals: {fp['total_count']:>2} (Abs:{fp['bullish_absorptions']}+{fp['bearish_absorptions']}, Trap:{fp['trapped_shorts']})")

    # Sort descending by confluence score
    audited.sort(key=lambda x: x["confluence_score"], reverse=True)

    print(f"\n================================================================================")
    print(f"🏆 TOP 10 HIGHEST CONFLUENCE CANDIDATES (RANKED ACROSS ALL {len(audited)} ASSETS):")
    print(f"================================================================================")
    for r_idx, c in enumerate(audited[:10], 1):
        fp = c["footprint_signals"]
        print(f"#{r_idx:02d}: {c['symbol']:<12} | Score: {c['confluence_score']}/100 | Action: {c['action']} | Entry: {c['entry']} | SL: {c['sl']} | TP: {c['tp']} | R:R: {c['rr']}")
        print(f"     Confluence: {', '.join(c['reasons'][:3])}")
        if fp["top_signals"]:
            print(f"     Footprint: {fp['top_signals'][0]}")

    # Write JSON Database
    db_file = TRADE_PLANS_DIR / "CYCLE_038_EXHAUSTIVE_88_ASSET_DATABASE.json"
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump({
            "cycle_id": "Cycle_038",
            "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
            "total_assets_audited": len(audited),
            "missing_dossiers": missing,
            "ranked_assets": audited
        }, f, indent=2)

    # Write Markdown Document
    md_file = TRADE_PLANS_DIR / "CYCLE_038_EXHAUSTIVE_88_ASSET_ANALYSIS.md"
    lines = [
        f"# 🔬 CYCLE_038: EXHAUSTIVE 88-ASSET 15-PILLAR & FOOTPRINT FORENSICS",
        f"**Universe**: {len(audited)} Assets Physically Audited | **Mandatory Standard**: CoinGlass Footprint Signals Invariant",
        f"**Timestamp**: {datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        "",
        "## 🏆 1. TOP RANKED CONFLUENCE CANDIDATES",
        "",
        "| Rank | Symbol | Score | Action | Limit Entry | Stop Loss | Take Profit | R:R | Spread (bps) | Whales | Footprint Signals | Key Confluence Rationale |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|"
    ]
    for r_idx, c in enumerate(audited[:15], 1):
        fp = c["footprint_signals"]
        fp_str = f"{fp['total_count']} (Abs:{fp['bullish_absorptions']}+{fp['bearish_absorptions']})"
        reasons_str = "; ".join(c["reasons"][:2])
        ent_str = f"`{c['entry']:,.2f}`" if c['entry'] else "N/A"
        sl_str = f"`{c['sl']:,.2f}`" if c['sl'] else "N/A"
        tp_str = f"`{c['tp']:,.2f}`" if c['tp'] else "N/A"
        rr_str = f"{c['rr']:.2f}R" if c['rr'] else "N/A"
        lines.append(f"| **#{r_idx}** | `{c['symbol']}` | **{c['confluence_score']}** | `{c['action']}` | {ent_str} | {sl_str} | {tp_str} | {rr_str} | {c['telemetry']['spread_bps']:.2f} | {c['whales']['whale_count']} | {fp_str} | {reasons_str} |")

    lines.append("\n---\n\n## 📊 2. COMPLETE 88-ASSET FORENSIC AUDIT TABLE\n")
    lines.append("| # | Symbol | Score | Action | Mid Price | VWAP | POC | VAL | VAH | Max Pain (S / L) | Whales | Footprint (Bull/Bear Abs, Trapped) |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|---|")
    for r_idx, c in enumerate(audited, 1):
        t = c["telemetry"]
        tech = c["technicals"]
        auc = c["auction"]
        liq = c["liquidations"]
        fp = c["footprint_signals"]
        lines.append(f"| {r_idx} | `{c['symbol']}` | {c['confluence_score']} | `{c['action']}` | `{t['mid']:,.2f}` | `{tech['vwap']:,.2f}` | `{auc['daily_poc']:,.2f}` | `{auc['daily_val']:,.2f}` | `{auc['daily_vah']:,.2f}` | `{liq['short_max_pain']:,.2f}` / `{liq['long_max_pain']:,.2f}` | {c['whales']['whale_count']} | BullAbs:{fp['bullish_absorptions']}, BearAbs:{fp['bearish_absorptions']}, TrapS:{fp['trapped_shorts']}, TrapL:{fp['trapped_longs']} |")

    with open(md_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"\n✅ Emitted Full Forensic Database: {db_file.name} ({db_file.stat().st_size:,} bytes)")
    print(f"✅ Emitted Full Forensic Markdown: {md_file.name} ({md_file.stat().st_size:,} bytes)")
    print(f"================================================================================")

if __name__ == "__main__":
    main()
