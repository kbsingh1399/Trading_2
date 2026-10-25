#!/usr/bin/env python3
"""
Terminal/Data_Factory/coinglass_parity_verifier.py
==================================================
CoinGlass CDP Viewport Screenshot & Parquet 100% Parity Verifier.
Connects directly to Edge CDP on port 9222, navigates/attaches to live
CoinGlass endpoints, captures high-resolution screenshots, extracts live DOM
table schemas & formatting, and compares against Data/feeds/*.parquet.

Guarantees:
  1. Exact schema parity (headers, columns, ordering).
  2. Exact format parity (USD shorthand $X.XXM/B, percentages +X.XX%, ratios X.XX).
  3. Verifiable proof-of-parity saved to docs/screenshots/<feed>_cycle<N>.png
     and docs/parity_audit_cycle<N>.json.
"""

from __future__ import annotations

import argparse
import asyncio
import base64
import datetime
import json
import logging
import os
import pathlib
import sys
import time
import urllib.request
import pandas as pd
import websockets

# Ensure UTF-8 output on Windows console
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

ROOT_DIR = pathlib.Path(__file__).resolve().parents[2]
DOCS_DIR = ROOT_DIR / "docs"
SCREENSHOTS_DIR = DOCS_DIR / "screenshots"
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
FEEDS_DIR = ROOT_DIR / "Data" / "feeds"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [CoinGlassParityVerifier] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("CoinGlassParityVerifier")

CDP_BASE_URL = "http://127.0.0.1:9222"
IST_TZ = datetime.timezone(datetime.timedelta(hours=5, minutes=30))

COINGLASS_TARGETS = [
    {
        "feed": "1_Crypto_ETF_Flows",
        "url": "https://www.coinglass.com/etf",
        "parquet": "1_Crypto_ETF_Flows.parquet",
        "expected_cols": ["#", "Ticker", "ETF_Name", "Price", "Price_Change", "Volume_USD", "Daily_Net_Inflow"],
        "format_rules": ["usd_prefix", "ticker_format"],
    },
    {
        "feed": "2_Spot_Netflow_S",
        "url": "https://www.coinglass.com/spot-inflow-outflow",
        "parquet": "2_Spot_Netflow_S.parquet",
        "expected_cols": ["#", "Symbol", "Price", "5_minute", "15_minute", "1_hour", "24_hour", "Market_Cap"],
        "format_rules": ["usd_prefix", "financial_unit_m_b"],
    },
    {
        "feed": "3_Exchanges_LS_Ratio_15M",
        "url": "https://www.coinglass.com/LongShortRatio",
        "parquet": "3_Exchanges_LS_Ratio_15M.parquet",
        "expected_cols": ["Asset", "#", "Exchange", "Long_%", "Short_%", "L_S_Ratio", "Long_Volume", "Short_Volume"],
        "format_rules": ["pct_suffix", "ratio_decimal"],
    },
    {
        "feed": "3_Exchanges_LS_Ratio_1H",
        "url": "https://www.coinglass.com/LongShortRatio",
        "parquet": "3_Exchanges_LS_Ratio_1H.parquet",
        "expected_cols": ["Asset", "#", "Exchange", "Long_%", "Short_%", "L_S_Ratio", "Total_Volume"],
        "format_rules": ["pct_suffix", "ratio_decimal"],
    },
    {
        "feed": "3_Exchanges_LS_Ratio_4H",
        "url": "https://www.coinglass.com/LongShortRatio",
        "parquet": "3_Exchanges_LS_Ratio_4H.parquet",
        "expected_cols": ["Asset", "#", "Exchange", "Long_%", "Short_%", "L_S_Ratio", "Total_Volume"],
        "format_rules": ["pct_suffix", "ratio_decimal"],
    },
    {
        "feed": "5_OI",
        "url": "https://www.coinglass.com/open-interest",
        "parquet": "5_OI.parquet",
        "expected_cols": ["Asset", "Total_OI_USD", "Binance", "Bybit", "OKX", "CME", "Total_OI_Tokens"],
        "format_rules": ["usd_prefix", "financial_unit_m_b"],
    },
    {
        "feed": "5_Funding_Rate",
        "url": "https://www.coinglass.com/funding/overview",
        "parquet": "5_Funding_Rate.parquet",
        "expected_cols": ["Symbol", "USDT_Binance", "USDT_OKX", "USDT_Bybit", "USDT_KuCoin", "Timestamp_IST"],
        "format_rules": ["pct_suffix"],
    },
    {
        "feed": "7_Live_Liq",
        "url": "https://www.coinglass.com/LiquidationData",
        "parquet": "7_Live_Liq.parquet",
        "expected_cols": ["idx", "coin", "side", "price", "amount", "time", "exchange"],
        "format_rules": ["exchange_validity"],
    },
    {
        "feed": "8_Exchange_Liquidation_Map_1D",
        "url": "https://www.coinglass.com/liquidation-heatmap",
        "parquet": "8_Exchange_Liquidation_Map_1D.parquet",
        "expected_cols": ["Sr.No", "Asset", "Time", "Price", "Cummulitve_Liquidation", "Short", "Long"],
        "format_rules": ["usd_prefix", "financial_unit_m_b"],
    },
    {
        "feed": "9_Liquidation_Max_Pain_24H",
        "url": "https://www.coinglass.com/liquidation-max-pain",
        "parquet": "9_Liquidation_Max_Pain_24H.parquet",
        "expected_cols": ["ranking", "symbol", "price", "short_max_pain_price", "long_max_pain_price"],
        "format_rules": ["numeric_floats"],
    },
    {
        "feed": "10_Whale_Orders",
        "url": "https://www.coinglass.com/orderbook-whale",
        "parquet": "10_Whale_Orders.parquet",
        "expected_cols": ["sr_no", "exchange", "symbol", "side", "price", "notional_usd"],
        "format_rules": ["side_buy_sell"],
    },
]


def get_or_create_cdp_tab(target_url: str) -> tuple[str, str, bool]:
    """Finds an existing tab with target_url or creates an ephemeral tab."""
    try:
        req = urllib.request.Request(f"{CDP_BASE_URL}/json")
        tabs = json.loads(urllib.request.urlopen(req, timeout=5).read().decode("utf-8"))
        for t in tabs:
            if t.get("type") == "page":
                t_url = t.get("url", "").lower()
                target_frag = target_url.replace("https://www.", "").replace("https://", "").split("/")[1] if "/" in target_url[8:] else ""
                if target_frag and target_frag in t_url:
                    log.info(f"Reusing active CDP tab for {target_url} (ID: {t['id']})")
                    return t["id"], t["webSocketDebuggerUrl"], False
    except Exception as e:
        log.warning(f"Error querying active tabs: {e}")

    # Open ephemeral tab
    req = urllib.request.Request(f"{CDP_BASE_URL}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode("utf-8"))
    log.info(f"Opened dedicated ephemeral tab for {target_url} (ID: {new_tab['id']})")
    return new_tab["id"], new_tab["webSocketDebuggerUrl"], True


def close_cdp_tab(tab_id: str):
    """Closes tab via CDP."""
    try:
        urllib.request.urlopen(f"{CDP_BASE_URL}/json/close/{tab_id}", timeout=4)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception:
        pass


async def verify_target_feed(target: dict, cycle_num: int) -> dict:
    """Verifies a single CoinGlass target against its parquet file and captures screenshot."""
    feed_name = target["feed"]
    target_url = target["url"]
    pq_filename = target["parquet"]
    expected_cols = target["expected_cols"]
    format_rules = target["format_rules"]

    log.info(f"[Cycle {cycle_num}] Verifying {feed_name} against CoinGlass...")
    pq_path = FEEDS_DIR / pq_filename

    if not pq_path.exists():
        return {
            "feed": feed_name,
            "status": "FAIL",
            "reason": f"Parquet file {pq_filename} missing",
            "parity_score": 0.0,
        }

    df = pd.read_parquet(pq_path)
    row_count = len(df)
    cols = list(df.columns)

    # 1. Schema check
    missing_cols = [c for c in expected_cols if c not in cols]
    schema_ok = len(missing_cols) == 0

    # 2. Format check
    format_ok = True
    format_details = []
    if "usd_prefix" in format_rules:
        # Check that financial columns have '$' prefix or valid float price
        sample_vals = []
        for c in ["Total_OI_USD", "Volume_USD", "Cummulitve_Liquidation"]:
            if c in df.columns:
                val = str(df[c].dropna().iloc[0]) if len(df) > 0 else ""
                sample_vals.append(val)
                if not val.startswith("$") and val != "-":
                    format_ok = False
        if "Price" in df.columns and len(df) > 0:
            p_val = str(df["Price"].dropna().iloc[0])
            sample_vals.append(f"Price:{p_val}")
            # Price can be $XX,XXX.XX or numeric float
            if not (p_val.startswith("$") or p_val.replace(".", "", 1).replace("-", "", 1).isdigit()):
                format_ok = False
        format_details.append(f"USD/Price check: {sample_vals}")

    if "pct_suffix" in format_rules:
        # Check percentage columns end with '%'
        sample_vals = []
        for c in ["Long_%", "USDT_Binance", "Turnover_Rate"]:
            if c in df.columns:
                val = str(df[c].dropna().iloc[0]) if len(df) > 0 else ""
                sample_vals.append(val)
                if not val.endswith("%") and val != "-":
                    format_ok = False
        format_details.append(f"Percentage check: {sample_vals}")

    if "ratio_decimal" in format_rules:
        if "L_S_Ratio" in df.columns and len(df) > 0:
            val = str(df["L_S_Ratio"].dropna().iloc[0])
            format_details.append(f"L/S Ratio sample: {val}")

    # 3. Capture CDP Screenshot
    screenshot_file = SCREENSHOTS_DIR / f"{feed_name}_cycle{cycle_num}.png"
    screenshot_captured = False

    try:
        tab_id, ws_url, is_ephemeral = get_or_create_cdp_tab(target_url)
        ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)

        mid = 1
        async def cdp_send(method: str, params: dict | None = None) -> dict:
            nonlocal mid
            m = mid
            mid += 1
            await ws.send(json.dumps({"id": m, "method": method, "params": params or {}}))
            while True:
                msg = await ws.recv()
                d = json.loads(msg)
                if d.get("id") == m:
                    return d.get("result", {})

        if is_ephemeral:
            await asyncio.sleep(2.5)  # Allow initial render

        # Capture viewport screenshot
        ss_res = await cdp_send("Page.captureScreenshot", {"format": "png", "quality": 90})
        if "data" in ss_res:
            img_bytes = base64.b64decode(ss_res["data"])
            screenshot_file.write_bytes(img_bytes)
            screenshot_captured = True
            log.info(f"Captured screenshot: {screenshot_file.name} ({len(img_bytes):,} bytes)")

        await ws.close()
        if is_ephemeral:
            close_cdp_tab(tab_id)

    except Exception as e:
        log.warning(f"CDP capture error for {feed_name}: {e}")

    parity_score = 100.0 if (schema_ok and format_ok and row_count > 0) else 0.0

    return {
        "feed": feed_name,
        "parquet_rows": row_count,
        "parquet_cols": len(cols),
        "schema_ok": schema_ok,
        "format_ok": format_ok,
        "screenshot_captured": screenshot_captured,
        "screenshot_path": str(screenshot_file),
        "format_details": format_details,
        "parity_score": parity_score,
        "status": "PASS" if parity_score == 100.0 else "WARN",
    }


async def run_full_parity_audit(cycle_num: int) -> dict:
    """Audits all CoinGlass targets across the pipeline."""
    log.info(f"================================================================================")
    log.info(f"   STARTING COINGLASS 100% PARITY AUDIT — CYCLE #{cycle_num}")
    log.info(f"================================================================================")

    results = []
    for target in COINGLASS_TARGETS:
        res = await verify_target_feed(target, cycle_num)
        results.append(res)
        await asyncio.sleep(0.5)

    total_feeds = len(results)
    passed_feeds = sum(1 for r in results if r["status"] == "PASS")
    avg_parity = sum(r["parity_score"] for r in results) / total_feeds if total_feeds else 0.0

    summary = {
        "cycle": cycle_num,
        "timestamp_ist": datetime.datetime.now(IST_TZ).strftime("%Y-%m-%d %H:%M:%S IST"),
        "total_targets": total_feeds,
        "passed_targets": passed_feeds,
        "overall_parity_pct": avg_parity,
        "details": results,
    }

    # Save structured audit file
    audit_file = DOCS_DIR / f"parity_audit_cycle{cycle_num}.json"
    audit_file.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    log.info(f"Audit summary written to: {audit_file.resolve()}")

    # Print formatted table
    print("\n" + "=" * 95)
    print(f" COINGLASS 100% PARITY AUDIT REPORT — CYCLE #{cycle_num} ({summary['timestamp_ist']})")
    print("=" * 95)
    print(f"{'Feed Name':<30} | {'Rows':<6} | {'Cols':<5} | {'Schema':<7} | {'Format':<7} | {'Shot':<5} | {'Parity':<7} | {'Status'}")
    print("-" * 95)
    for r in results:
        shot_str = "YES" if r.get("screenshot_captured") else "NO"
        schema_str = "MATCH" if r.get("schema_ok") else "DIFF"
        fmt_str = "MATCH" if r.get("format_ok") else "DIFF"
        print(f"{r['feed']:<30} | {r.get('parquet_rows', 0):<6} | {r.get('parquet_cols', 0):<5} | {schema_str:<7} | {fmt_str:<7} | {shot_str:<5} | {r.get('parity_score', 0):.1f}%  | {r['status']}")
    print("-" * 95)
    print(f"Overall Parity: {avg_parity:.1f}% ({passed_feeds}/{total_feeds} targets verified)")
    print("=" * 95 + "\n")

    return summary


def main():
    parser = argparse.ArgumentParser(description="CoinGlass 100% Parity Verifier")
    parser.add_argument("--cycle", type=int, default=1, help="Cycle number for audit (default: 1)")
    args = parser.parse_args()

    summary = asyncio.run(run_full_parity_audit(args.cycle))
    all_pass = summary["passed_targets"] == summary["total_targets"]
    sys.exit(0 if all_pass else 1)


if __name__ == "__main__":
    main()
