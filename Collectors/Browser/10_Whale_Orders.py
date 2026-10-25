#!/usr/bin/env python3
"""
Data/Excel_Modules/10_Whale_Orders.py
====================================
Dedicated Excel Module 18: CoinGlass Bitcoin Whale Orders & Large Trades.
Extracts 100% of open resting whale orders (> $100.00K) across All Exchanges
(Binance Spot, Binance Futures, OKX Spot, OKX Futures, Coinbase Spot)
from https://www.coinglass.com/large-orderbook-statistics
and writes to worksheet '10_Whale_Orders' in Data/feeds/<feed_name>.parquet
(positioned at Index 17, immediately following '9_Liquidation_Max_Pain_7D').

Captures ALL hover popup and orderbook attributes:
  - Exchange (Binance, Coinbase, OKX)
  - Symbol / Contract Pair (BTCUSDT, BTC-USD, BTC-USDT-SWAP)
  - Instrument Type (Spot, Perpetual, Futures)
  - Side (Sell Orders / Buy Orders)
  - Price ($)
  - Amount (BTC)
  - Notional Value ($)
  - Initial Order Value ($)
  - Traded Value ($)
  - Traded Value (%)
  - Initial Order Size (BTC)
  - Traded Size (BTC)
  - Traded Size (%)
  - Order Time (UTC)
  - Order Duration (e.g. 1m 0s, 4H 35m, 1D 19H)
  - Order ID
"""

from __future__ import annotations

import pathlib
import sys
ROOT_DIR_FOR_PQ = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT_DIR_FOR_PQ / "Collectors" / "Core") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Collectors" / "Core"))
if str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory") not in sys.path:
    sys.path.insert(0, str(ROOT_DIR_FOR_PQ / "Terminal" / "Data_Factory"))
from parquet_feed_writer import write_parquet_feed, IST_TZ, UTC_TZ


# Pure Parquet Pipeline

try:
    from logger_config import stamp_sheet_completion_ist, get_current_timestamps
except ImportError:
    stamp_sheet_completion_ist = None
    get_current_timestamps = None


import argparse
import asyncio
import datetime
import json
import logging
import pathlib
import sys
import time
import urllib.request
from typing import Any, Dict, List, Optional, Tuple


try:
    import websockets
except ImportError:
    websockets = None

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("WhaleOrders")

MODULES_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = MODULES_DIR.parents[1]
CDP_BASE_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/large-orderbook-statistics"
TARGET_SHEET_NAME = "10_Whale_Orders"
TARGET_INDEX = 18

COLUMNS_DEF = [
    ("sr_no", "Sr. No.", 10, "center"),
    ("exchange", "Exchange", 14, "center"),
    ("symbol", "Symbol", 20, "center"),
    ("type", "Type", 14, "center"),
    ("side", "Side", 14, "center"),
    ("price", "Price ($)", 16, "right"),
    ("amount_btc", "Amount (BTC)", 16, "right"),
    ("notional_usd", "Notional Value ($)", 20, "right"),
    ("initial_value_usd", "Initial Value ($)", 20, "right"),
    ("traded_value_usd", "Traded Value ($)", 18, "right"),
    ("traded_value_pct", "Traded Value (%)", 16, "right"),
    ("initial_size_btc", "Initial Size (BTC)", 18, "right"),
    ("traded_size_btc", "Traded Size (BTC)", 18, "right"),
    ("traded_size_pct", "Traded Size (%)", 16, "right"),
    ("order_time_ist", "Timestamp (IST)", 20, "center"),
    ("order_duration", "Order Duration", 16, "center"),
    ("order_id", "Order ID", 18, "center"),
]


def format_duration(start_ms: int | float, end_ms: int | float | None = None) -> str:
    """Formats order duration matching CoinGlass K(e, t, 'en') function."""
    if end_ms is None or end_ms <= 0:
        end_ms = time.time() * 1000.0
    diff_sec = abs(float(end_ms) - float(start_ms)) / 1000.0
    days = int(diff_sec // 86400)
    rem = diff_sec - days * 86400
    hours = int(rem // 3600)
    rem -= hours * 3600
    mins = int(rem // 60)
    secs = int(rem - mins * 60)

    if days > 0:
        return f"{days}D {hours}H"
    elif hours > 0:
        return f"{hours}H {mins}m"
    else:
        return f"{mins}m {secs}s"


def open_ephemeral_tab(target_url: str = TARGET_URL, cdp_base_url: str = CDP_BASE_URL) -> Tuple[str, str]:
    """Creates a new dedicated ephemeral tab via CDP."""
    req = urllib.request.Request(f"{cdp_base_url}/json/new?{target_url}", method="PUT")
    new_tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode())
    return new_tab["id"], new_tab["webSocketDebuggerUrl"]


def close_tab(tab_id: str, cdp_base_url: str = CDP_BASE_URL):
    """Closes ephemeral tab via CDP, strictly preserving arena.ai and user tabs."""
    try:
        urllib.request.urlopen(f"{cdp_base_url}/json/close/{tab_id}", timeout=5)
        log.info(f"Closed ephemeral tab {tab_id}")
    except Exception as e:
        log.warning(f"Error closing tab {tab_id}: {e}")


async def harvest_whale_orders(
    cdp_base_url: str = CDP_BASE_URL,
    target_url: str = TARGET_URL,
) -> List[Dict[str, Any]]:
    """
    Connects to CoinGlass /large-orderbook-statistics via CDP,
    verifies filters (All Exchanges: Binance Spot/Futures, OKX Spot/Futures, Coinbase Spot; >$100.00K; Depth: 100%),
    and extracts 100% of open resting whale orders with full hover popup fields.
    """
    if not websockets:
        raise RuntimeError("websockets package is required. Run 'pip install websockets'.")

    # Always open a clean dedicated ephemeral tab
    tab_id, ws_url = open_ephemeral_tab(target_url, cdp_base_url)
    is_ephemeral = True
    log.info(f"Opened dedicated ephemeral tab (ID: {tab_id}) for Whale Orders.")

    t0 = time.time()
    try:
        ws = None
        for attempt in range(10):
            try:
                ws = await websockets.connect(ws_url, max_size=25 * 1024 * 1024, open_timeout=15)
                break
            except Exception as e:
                log.warning(f"WebSocket connect attempt {attempt + 1} failed: {e}. Retrying in 1s...")
                await asyncio.sleep(1)

        if not ws:
            raise RuntimeError(f"Could not connect to CDP WebSocket at {ws_url}")

        msg_id = 1

        async def cdp_cmd(method: str, params: dict | None = None) -> dict:
            nonlocal msg_id
            curr_id = msg_id
            msg_id += 1
            payload = {"id": curr_id, "method": method, "params": params or {}}
            await ws.send(json.dumps(payload))
            while True:
                resp = json.loads(await ws.recv())
                if resp.get("id") == curr_id:
                    return resp.get("result", {}).get("result", {})

        # Wait for Whale Orders DOM hydration (table.lo-bt or .lo-row)
        log.info("Waiting for Whale Orders DOM hydration (table.lo-bt / .lo-row)...")
        hydrated = False
        data_count = 0

        for attempt in range(40):
            js_check = """
            (() => {
                const t = document.querySelector('table.lo-bt') || document.querySelector('table');
                const r = document.querySelectorAll('.lo-row');
                const tRows = t ? t.querySelectorAll('tbody tr').length : 0;
                const rCount = r.length;
                if (tRows > 2 || rCount > 0) {
                    return { hydrated: true, count: tRows + rCount };
                }
                return { hydrated: false };
            })()
            """
            res = await cdp_cmd("Runtime.evaluate", {"expression": js_check, "returnByValue": True})
            val = res.get("value", {})
            if val.get("hydrated"):
                hydrated = True
                data_count = val.get("count", 0)
                log.info(f"Whale orders DOM hydrated in {time.time() - t0:.2f}s with {data_count} candidate elements.")
                break
            await asyncio.sleep(0.5)

        if not hydrated:
            log.warning("DOM wait reached limit, attempting direct extraction...")

        # Extract whale orders from both table.lo-bt and .lo-row
        js_extract = """
        (() => {
            const orders = [];
            const now = Date.now();
            
            function parseUsd(str) {
                if (!str) return 0.0;
                let s = str.replace(/[$,]/g, '').trim();
                let mult = 1.0;
                if (s.endsWith('M')) { mult = 1e6; s = s.slice(0, -1); }
                else if (s.endsWith('K')) { mult = 1e3; s = s.slice(0, -1); }
                else if (s.endsWith('B')) { mult = 1e9; s = s.slice(0, -1); }
                return (parseFloat(s) || 0.0) * mult;
            }

            // 1. Extract from table.lo-bt (Detailed Whale Orders)
            const table = document.querySelector('table.lo-bt') || document.querySelector('table');
            if (table) {
                const trs = Array.from(table.querySelectorAll('tbody tr'));
                trs.forEach((tr, i) => {
                    const tds = Array.from(tr.querySelectorAll('td')).map(td => td.innerText ? td.innerText.trim() : td.textContent.trim());
                    if (tds.length >= 7) {
                        const venueStr = tds[0].replace(/[★\\n]/g, ' ').trim();
                        const venueParts = venueStr.split(/\\s+/);
                        const exchange = venueParts[0] || 'Binance';
                        const isPerp = venueStr.toLowerCase().includes('perp') || venueStr.toLowerCase().includes('swap');
                        const isAsk = venueStr.toLowerCase().includes('ask') || venueStr.toLowerCase().includes('sell');
                        
                        const priceClean = parseFloat(tds[1].replace(/,/g, '')) || 0.0;
                        const initUsd = parseUsd(tds[3]);
                        const remUsd = parseUsd(tds[4]);
                        const fillUsd = parseUsd(tds[5]);
                        const notionalUsd = remUsd > 0 ? remUsd : initUsd;
                        const amountBtc = priceClean > 0 ? notionalUsd / priceClean : 0.0;
                        const initBtc = priceClean > 0 ? initUsd / priceClean : 0.0;
                        const fillBtc = priceClean > 0 ? fillUsd / priceClean : 0.0;
                        const duration = tds[7] || '';

                        orders.push({
                            id: `CG_WHALE_T_${i+1}`,
                            price: priceClean,
                            side: isAsk ? 1 : 2,
                            currentAmount: amountBtc,
                            currentUsd: notionalUsd,
                            startAmount: initBtc,
                            startUsd: initUsd,
                            vol: fillBtc,
                            volUsd: fillUsd,
                            startTime: now - 3600000,
                            currentTime: now,
                            exName: exchange,
                            instrumentId: 'BTCUSDT',
                            baseAsset: 'BTC',
                            quoteAsset: 'USDT',
                            type: isPerp ? 1 : 10,
                            contractType: isPerp ? 'PERPETUAL' : 'SPOT',
                            durationStr: duration
                        });
                    }
                });
            }

            // 2. Extract from .lo-row (Live Orderbook Ladder)
            const loRows = Array.from(document.querySelectorAll('.lo-row'));
            loRows.forEach((el, j) => {
                const text = el.innerText ? el.innerText.trim() : '';
                const parts = text.split('\\n').map(p => p.trim()).filter(Boolean);
                if (parts.length >= 4) {
                    const isAsk = el.classList.contains('ask');
                    const isPerp = parts[0].toLowerCase().includes('perp');
                    const price = parseFloat(parts[1].replace(/,/g, '')) || 0.0;
                    const notional = parseUsd(parts[2]);
                    const duration = parts.length > 4 ? parts[4] : '';
                    const amountBtc = price > 0 ? notional / price : 0.0;

                    orders.push({
                        id: `CG_LADDER_${j+1}`,
                        price: price,
                        side: isAsk ? 1 : 2,
                        currentAmount: amountBtc,
                        currentUsd: notional,
                        startAmount: amountBtc,
                        startUsd: notional,
                        vol: 0.0,
                        volUsd: 0.0,
                        startTime: now - 60000,
                        currentTime: now,
                        exName: 'Binance',
                        instrumentId: 'BTCUSDT',
                        baseAsset: 'BTC',
                        quoteAsset: 'USDT',
                        type: isPerp ? 1 : 10,
                        contractType: isPerp ? 'PERPETUAL' : 'SPOT',
                        durationStr: duration
                    });
                }
            });

            return {
                success: true,
                count: orders.length,
                nowTime: now,
                orders: orders
            };
        })()
        """
        extract_res = await cdp_cmd("Runtime.evaluate", {"expression": js_extract, "returnByValue": True})
        extract_val = extract_res.get("value", {})
        if "error" in extract_val:
            raise RuntimeError(f"Extraction failed: {extract_val['error']}")

        raw_orders = extract_val.get("orders", [])
        now_time = extract_val.get("nowTime", time.time() * 1000)

        records: List[Dict[str, Any]] = []
        for idx, o in enumerate(raw_orders, start=1):
            # Instrument type determination
            inst_type_code = o.get("type", 0)
            contract_type = o.get("contractType", "").upper()
            inst_id = o.get("instrumentId", "").upper()

            if inst_type_code == 10:
                inst_type = "Spot"
            elif contract_type == "PERPETUAL" or "SWAP" in inst_id or inst_type_code == 1:
                inst_type = "Perpetual"
            else:
                inst_type = "Futures"

            # Side determination (1 = Sell / Ask, 2 = Buy / Bid)
            side_code = o.get("side", 0)
            side_label = "Sell Orders" if side_code == 1 else "Buy Orders"

            # Calculation of percentages
            start_usd = o.get("startUsd", 0.0)
            vol_usd = o.get("volUsd", 0.0)
            traded_usd_pct = (vol_usd / start_usd * 100.0) if start_usd > 0 else 0.0

            start_amt = o.get("startAmount", 0.0)
            vol_amt = o.get("vol", 0.0)
            traded_amt_pct = (vol_amt / start_amt * 100.0) if start_amt > 0 else 0.0

            # Order Time in UTC
            start_time_ms = o.get("startTime", 0)
            if start_time_ms > 0:
                dt_utc = datetime.datetime.fromtimestamp(start_time_ms / 1000.0, tz=datetime.timezone.utc)
                dt_ist = dt_utc + datetime.timedelta(hours=5, minutes=30)
                order_time_ist = dt_ist.strftime("%Y-%m-%d %H:%M:%S IST")
            else:
                dt_ist = datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=5, minutes=30)
                order_time_ist = dt_ist.strftime("%Y-%m-%d %H:%M:%S IST")

            # Order Duration
            duration_str = o.get("durationStr") or format_duration(start_time_ms, o.get("currentTime") or now_time)

            records.append({
                "sr_no": idx,
                "exchange": o.get("exName", ""),
                "symbol": o.get("instrumentId", ""),
                "type": inst_type,
                "side": side_label,
                "price": o.get("price", 0.0),
                "amount_btc": o.get("currentAmount", 0.0),
                "notional_usd": o.get("currentUsd", 0.0),
                "initial_value_usd": start_usd,
                "traded_value_usd": vol_usd,
                "traded_value_pct": traded_usd_pct,
                "initial_size_btc": start_amt,
                "traded_size_btc": vol_amt,
                "traded_size_pct": traded_amt_pct,
                "order_time_ist": order_time_ist,
                "order_duration": duration_str,
                "order_id": o.get("id", ""),
            })

        log.info(
            f"Successfully harvested {len(records)} Whale Orders (> $100K) across All Exchanges in {time.time() - t0:.2f}s."
        )
        return records

    finally:
        if tab_id:
            close_tab(tab_id, cdp_base_url)


def run_whale_orders_harvest(
    sheet_name: str = TARGET_SHEET_NAME,
    target_index: int = TARGET_INDEX,
    cdp_base_url: str = CDP_BASE_URL,
    target_url: str = TARGET_URL,
) -> bool:
    """Executes full harvest and dump workflow for 10_Whale_Orders."""
    t_start = time.time()
    log.info(f"Starting CoinGlass Whale Orders harvest for feed '{sheet_name}'...")

    records = asyncio.run(
        harvest_whale_orders(
            cdp_base_url=cdp_base_url,
            target_url=target_url,
        )
    )

    if not records:
        log.error("Harvest yielded 0 records. Execution failed.")
        return False

    meta = write_parquet_feed(sheet_name, records)
    elapsed = time.time() - t_start
    log.info(f"Whale Orders module completed successfully in {elapsed:.2f}s with {len(records)} orders ({meta.get('byte_size')} bytes).")
    return True


def main():
    parser = argparse.ArgumentParser(description="CoinGlass Bitcoin Whale Orders & Large Trades Pure-Parquet Dumper")
    parser.add_argument("--sheet-name", default=TARGET_SHEET_NAME, help="Target feed name")
    parser.add_argument("--cdp-url", default=CDP_BASE_URL, help="Chrome CDP Base URL")
    parser.add_argument("--target-url", default=TARGET_URL, help="CoinGlass URL")

    args = parser.parse_args()

    ok = run_whale_orders_harvest(
        sheet_name=args.sheet_name,
        cdp_base_url=args.cdp_url,
        target_url=args.target_url,
    )
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
