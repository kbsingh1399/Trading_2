#!/usr/bin/env python3
"""
scripts/deep_forensic_asset_analyzer.py
Exhaustive 10-Section Deep Forensics Analyzer for High-Confluence Candidates.
Interrogates every single sub-data point: MTF CVD, Whales, Footprint, Multi-Horizon Max Pain, Netflow, and Funding.
"""

import datetime
import json
import os
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOSSIER_DIR = ROOT / "docs" / "dossiers"

def deep_analyze_asset(symbol):
    json_path = DOSSIER_DIR / f"{symbol}_MASTER_DOSSIER.json"
    if not json_path.exists():
        print(f"File not found: {json_path}")
        return None

    with open(json_path, "r", encoding="utf-8") as f:
        d = json.load(f)

    # 1. Telemetry & Specs
    specs = d.get("specs", {})
    telem = d.get("telemetry", {})
    mid = telem.get("mid", 0.0)
    spread_bps = telem.get("spread_bps", 0.0)

    # 2. Technical Profile & VWAP
    tech = d.get("technicals", {})
    vwap = tech.get("vwap") or tech.get("vwap_mid", 0.0)
    atr = tech.get("atr_14", 0.0)
    rsi = tech.get("rsi_14", 0.0)
    u2_51 = tech.get("u2_51", 0.0)
    l2_51 = tech.get("l2_51", 0.0)

    # 3. Auction Profile
    auc = d.get("auction", {})
    val = auc.get("daily_val", 0.0)
    poc = auc.get("daily_poc", 0.0)
    vah = auc.get("daily_vah", 0.0)
    regime = auc.get("auction_regime", "UNKNOWN")
    bias = auc.get("session_bias", "UNKNOWN")

    # 4. Multi-Timeframe CVD
    cvd_data = d.get("cvd", {})
    cvd_rows = cvd_data.get("table", []) if isinstance(cvd_data, dict) else []
    latest_5m_cvd = next((r for r in cvd_rows if r.get("timeframe") == "5m"), {})
    latest_15m_cvd = next((r for r in cvd_rows if r.get("timeframe") == "15m"), {})
    latest_1h_cvd = next((r for r in cvd_rows if r.get("timeframe") == "1h"), {})
    latest_4h_cvd = next((r for r in cvd_rows if r.get("timeframe") == "4h"), {})

    # 5. Whales & L2 Depth
    whales = d.get("whales_and_l2", {})
    whale_ladder = whales.get("whale_ladder", []) if isinstance(whales, dict) else []
    ob_ladder = whales.get("ob_ladder", []) if isinstance(whales, dict) else []
    big_bid_walls = [w for w in whale_ladder if "bid" in str(w.get("side", "")).lower() or float(w.get("bid_usd", 0.0) or 0.0) >= 100000]
    big_ask_walls = [w for w in whale_ladder if "ask" in str(w.get("side", "")).lower() or float(w.get("ask_usd", 0.0) or 0.0) >= 100000]

    # 6. Liquidations & Max Pain
    liq = d.get("liquidations", {})
    mp_24h = liq.get("mp_24h", {})
    mp_48h = liq.get("mp_48h", {})
    mp_7d = liq.get("mp_7d", {})

    # 7. Derivatives & Funding
    deriv = d.get("derivatives", {})
    funding = deriv.get("funding_rates", {}) if isinstance(deriv, dict) else {}
    ls_ratio = deriv.get("long_short_ratio", {}) if isinstance(deriv, dict) else {}

    # 8. Footprint & Macro Netflows
    fp = d.get("footprint_and_macro", {})
    footprint_signals = fp.get("footprint_signals", []) if isinstance(fp, dict) else []
    spot_netflow = fp.get("spot_netflow", {}) if isinstance(fp, dict) else {}
    fut_netflow = fp.get("fut_netflow", {}) if isinstance(fp, dict) else {}

    report = {
        "symbol": symbol,
        "broker_symbol": d.get("broker_sym"),
        "category": d.get("category"),
        "1_telemetry": {
            "mid": mid, "spread_bps": spread_bps, "digits": specs.get("digits"),
            "contract_size": specs.get("contract_size"), "min_lot": specs.get("min_lot")
        },
        "2_technicals": {
            "vwap": vwap, "atr_14": atr, "rsi_14": rsi, "u2.51": u2_51, "l2.51": l2_51
        },
        "3_auction": {
            "val": val, "poc": poc, "vah": vah, "regime": regime, "session_bias": bias
        },
        "4_cvd": {
            "5m_delta": latest_5m_cvd.get("delta"), "5m_regime": latest_5m_cvd.get("regime"),
            "15m_delta": latest_15m_cvd.get("delta"), "15m_regime": latest_15m_cvd.get("regime"),
            "1h_delta": latest_1h_cvd.get("delta"), "1h_regime": latest_1h_cvd.get("regime"),
            "4h_delta": latest_4h_cvd.get("delta"), "4h_regime": latest_4h_cvd.get("regime")
        },
        "5_whales": {
            "total_whale_records": len(whale_ladder),
            "big_bid_walls_count": len(big_bid_walls),
            "big_ask_walls_count": len(big_ask_walls)
        },
        "6_liquidations": {
            "24h_short_mp": mp_24h.get("short_max_pain_price") if isinstance(mp_24h, dict) else None,
            "24h_long_mp": mp_24h.get("long_max_pain_price") if isinstance(mp_24h, dict) else None,
            "48h_short_mp": mp_48h.get("short_max_pain_price") if isinstance(mp_48h, dict) else None,
            "48h_long_mp": mp_48h.get("long_max_pain_price") if isinstance(mp_48h, dict) else None,
            "7d_short_mp": mp_7d.get("short_max_pain_price") if isinstance(mp_7d, dict) else None,
            "7d_long_mp": mp_7d.get("long_max_pain_price") if isinstance(mp_7d, dict) else None
        },
        "7_derivatives": {
            "funding_summary": funding,
            "ls_ratio_summary": ls_ratio
        },
        "8_footprint_netflow": {
            "signals_count": len(footprint_signals),
            "sample_signals": [s.get("headline") for s in footprint_signals[:3]],
            "spot_netflow_1h": spot_netflow.get("1_hour"),
            "spot_netflow_24h": spot_netflow.get("24_hour"),
            "fut_netflow_1h": fut_netflow.get("1_hour"),
            "fut_netflow_24h": fut_netflow.get("24_hour")
        }
    }
    return report

def main():
    focus_assets = ["BTC", "ETH", "XAUUSD", "XMRUSD", "XLMUSD", "GER40"]
    print("=" * 80)
    print("🔬 COMPREHENSIVE 10-SECTION FORENSIC AUDIT REPORT")
    print("=" * 80)

    for sym in focus_assets:
        rep = deep_analyze_asset(sym)
        if rep:
            print(f"\n==================== {rep['symbol']} ({rep['broker_symbol']}) ====================")
            print(f"Category: {rep['category']} | Mid: {rep['1_telemetry']['mid']} | Spread: {rep['1_telemetry']['spread_bps']:.2f} bps")
            print(f"Auction Profile: VAL={rep['3_auction']['val']} | POC={rep['3_auction']['poc']} | VAH={rep['3_auction']['vah']} | Regime: {rep['3_auction']['regime']}")
            print(f"Technicals: VWAP={rep['2_technicals']['vwap']:.2f} | ATR-14={rep['2_technicals']['atr_14']:.2f} | RSI-14={rep['2_technicals']['rsi_14']:.1f}")
            print(f"Multi-Timeframe CVD Regimes:")
            print(f"  5m:  Delta={rep['4_cvd']['5m_delta']} | Regime={rep['4_cvd']['5m_regime']}")
            print(f"  15m: Delta={rep['4_cvd']['15m_delta']} | Regime={rep['4_cvd']['15m_regime']}")
            print(f"  1h:  Delta={rep['4_cvd']['1h_delta']} | Regime={rep['4_cvd']['1h_regime']}")
            print(f"  4h:  Delta={rep['4_cvd']['4h_delta']} | Regime={rep['4_cvd']['4h_regime']}")
            print(f"Liquidation Max Pain Strikes:")
            print(f"  24H: Long MP={rep['6_liquidations']['24h_long_mp']} | Short MP={rep['6_liquidations']['24h_short_mp']}")
            print(f"  48H: Long MP={rep['6_liquidations']['48h_long_mp']} | Short MP={rep['6_liquidations']['48h_short_mp']}")
            print(f"  7D:  Long MP={rep['6_liquidations']['7d_long_mp']} | Short MP={rep['6_liquidations']['7d_short_mp']}")
            print(f"Macro Capital Netflows:")
            print(f"  Spot: 1h={rep['8_footprint_netflow']['spot_netflow_1h']} | 24h={rep['8_footprint_netflow']['spot_netflow_24h']}")
            print(f"  Fut:  1h={rep['8_footprint_netflow']['fut_netflow_1h']} | 24h={rep['8_footprint_netflow']['fut_netflow_24h']}")
            print(f"Footprint Tape Signals: {rep['8_footprint_netflow']['signals_count']} detected: {rep['8_footprint_netflow']['sample_signals']}")

if __name__ == "__main__":
    main()
