#!/usr/bin/env python3
"""
Terminal/Data_Factory/coinglass_whale_orders_harvester.py
========================================================
Harvests asset-wise Whale Orders & Large Trades across our complete institutional crypto universe
from https://www.coinglass.com/large-orderbook-statistics via Chrome DevTools Protocol (CDP port 9222).

Dynamically interacts with the MuiAutocomplete symbol dropdown to traverse:
BTC, ETH, SOL, BNB, DOGE, XRP, ADA, LINK, AVAX, NEAR, LTC, BCH

Extracts for every single resting & executed whale order:
- Side (BUY / SELL)
- Order Status (Active vs Canceled)
- Price level (Float)
- Notional in USD (Normalized Float e.g. $4.62M -> 4,620,000 USD)
- Temporal Persistence / Duration (Raw string + Parsed numeric seconds/hours)

Saves active snapshot to Data/coinglass/latest/coinglass_whale_orders_snapshot.json
and archives to time_series_database (Data/history/coinglass_whale_orders/).
"""
from __future__ import annotations
import asyncio
import datetime
import json
import os
import pathlib
import re
import sys
import time
import urllib.request
import websockets

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

CDP_HTTP_URL = "http://127.0.0.1:9222"
TARGET_URL = "https://www.coinglass.com/large-orderbook-statistics"
OUTPUT_SNAPSHOT_DIR = ROOT / "Data" / "coinglass" / "latest"
OUTPUT_SNAPSHOT_FILE = OUTPUT_SNAPSHOT_DIR / "coinglass_whale_orders_snapshot.json"

TARGET_ASSETS = ["BTC", "ETH", "SOL", "BNB", "DOGE", "XRP", "ADA", "LINK", "AVAX", "SUI", "NEAR", "DOT", "LTC", "BCH", "APT", "OP", "ARB", "TRX"]


def parse_notional(val_str: str) -> float:
    """Converts strings like '$4.62M', '$790.81K', '$1.2B' into numeric USD floats."""
    val_str = val_str.replace("$", "").replace(",", "").strip()
    try:
        if val_str.endswith("B"):
            return float(val_str[:-1]) * 1_000_000_000.0
        elif val_str.endswith("M"):
            return float(val_str[:-1]) * 1_000_000.0
        elif val_str.endswith("K"):
            return float(val_str[:-1]) * 1_000.0
        return float(val_str)
    except Exception:
        return 0.0


def parse_duration_seconds(dur_str: str) -> float:
    """Converts strings like '11H 52m', '1D 23H', '47m 38s', '0m 18s' into numeric seconds."""
    total_sec = 0.0
    dur_str = dur_str.strip()
    
    # Days
    d_m = re.search(r'(\d+)\s*D', dur_str)
    if d_m:
        total_sec += float(d_m.group(1)) * 86400.0
    
    # Hours
    h_m = re.search(r'(\d+)\s*H', dur_str)
    if h_m:
        total_sec += float(h_m.group(1)) * 3600.0
        
    # Minutes
    m_m = re.search(r'(\d+)\s*m', dur_str)
    if m_m:
        total_sec += float(m_m.group(1)) * 60.0
        
    # Seconds
    s_m = re.search(r'(\d+)\s*s', dur_str)
    if s_m:
        total_sec += float(s_m.group(1))
        
    return total_sec


async def harvest_whale_orders(assets: list[str] = TARGET_ASSETS) -> dict:
    OUTPUT_SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    t_start = time.time()
    
    # Create ephemeral background target on CDP
    req = urllib.request.Request(f"{CDP_HTTP_URL}/json/new?{TARGET_URL}", method="PUT")
    tab = json.loads(urllib.request.urlopen(req, timeout=10).read().decode("utf-8"))
    ws_url = tab["webSocketDebuggerUrl"]
    tab_id = tab["id"]
    print(f"[WhaleOrdersHarvester] Connected to CDP background target {tab_id}")

    harvested_data: dict[str, dict] = {}

    try:
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            cur_id = 0
            async def send(method, params=None):
                nonlocal cur_id
                cur_id += 1
                await ws.send(json.dumps({"id": cur_id, "method": method, "params": params or {}}))
                while True:
                    raw = await ws.recv()
                    msg = json.loads(raw)
                    if msg.get("id") == cur_id:
                        return msg

            await send("Page.enable")
            # Wait for initial page hydration
            await asyncio.sleep(4.5)

            for idx, asset in enumerate(assets):
                t_asset_start = time.time()
                
                # Check if asset is already selected
                check_js = f"""(() => {{
                    const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                    return el ? (el.value || '').trim().toUpperCase() : '';
                }})()"""
                chk_res = await send("Runtime.evaluate", {"expression": check_js, "returnByValue": True})
                cur_val = chk_res.get("result", {}).get("result", {}).get("value", "")

                if cur_val != asset:
                    # Focus and select existing text
                    focus_js = """(() => {
                        const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                        if (!el) return false;
                        el.focus();
                        el.select();
                        return true;
                    })()"""
                    await send("Runtime.evaluate", {"expression": focus_js, "returnByValue": True})
                    await asyncio.sleep(0.2)

                    # Insert target symbol via CDP native input
                    await send("Input.insertText", {"text": asset})
                    await asyncio.sleep(0.6)

                    # Click matching option from MUI listbox (NO options[0] fallback: prevents mislabeling)
                    click_opt_js = f"""(() => {{
                        const targetSymbol = {json.dumps(asset)};
                        const listbox = document.querySelector('.MuiAutocomplete-popper, ul.MuiAutocomplete-listbox, div[role="listbox"]');
                        if (!listbox) return false;
                        const options = Array.from(listbox.querySelectorAll('li, div[role="option"]'));
                        const match = options.find(o => {{
                            const txt = (o.innerText || '').trim();
                            const firstToken = txt.split(/[\\s\\n]+/)[0].toUpperCase();
                            return firstToken === targetSymbol;
                        }});
                        if (match) {{
                            match.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                            match.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                            match.click();
                            return true;
                        }}
                        return false;
                    }})()"""
                    await send("Runtime.evaluate", {"expression": click_opt_js, "returnByValue": True})
                    await asyncio.sleep(1.8)

                    # Ensure popper is closed
                    close_popper_js = """(() => {
                        const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                        if (el) el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
                    })()"""
                    await send("Runtime.evaluate", {"expression": close_popper_js, "returnByValue": True})
                    await asyncio.sleep(0.3)

                # Extract all whale order rows with strict validation of currentInput === targetSymbol
                extract_js = f"""(() => {{
                    const targetSymbol = {json.dumps(asset)};
                    const searchInput = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                    const finalInputVal = (searchInput && searchInput.value ? searchInput.value : '').trim().toUpperCase();

                    if (finalInputVal !== targetSymbol) {{
                        return {{
                            error: 'Symbol mismatch: requested ' + targetSymbol + ' but active input is ' + finalInputVal,
                            currentInput: finalInputVal,
                            itemCount: 0,
                            items: []
                        }};
                    }}

                    const items = Array.from(document.querySelectorAll('.large-order-item')).map(el => {{
                        const rawLines = (el.innerText || '').split('\\n').map(s => s.trim()).filter(Boolean);
                        const isCanceled = Boolean(el.querySelector('span[class*="cancel"], div[class*="cancel"]') || rawLines.includes('C'));
                        const bgEl = el.querySelector('div[class*="item-bg"], div[class*="ovv2-item-bg"]');
                        const bgClass = bgEl ? bgEl.className : '';
                        let domSide = 'UNKNOWN';
                        if (bgClass.includes('-l') || bgClass.includes('long') || bgClass.includes('buy')) {{
                            domSide = 'BUY';
                        }} else if (bgClass.includes('-s') || bgClass.includes('short') || bgClass.includes('sell')) {{
                            domSide = 'SELL';
                        }}
                        return {{
                            lines: rawLines,
                            isCanceled: isCanceled,
                            domSide: domSide
                        }};
                    }});

                    return {{
                        symbol: targetSymbol,
                        currentInput: finalInputVal,
                        itemCount: items.length,
                        items: items
                    }};
                }})()"""

                res = await send("Runtime.evaluate", {"expression": extract_js, "returnByValue": True})
                val = res.get("result", {}).get("result", {}).get("value", {})
                if not val or val.get("error"):
                    if val and val.get("error"):
                        print(f"[{idx+1}/{len(assets)}] {asset:<5} -> WARNING: {val.get('error')}. Skipping.")
                    continue
                
                raw_items = val.get("items", [])
                parsed_orders = []
                buy_notional = 0.0
                sell_notional = 0.0
                max_order_usd = 0.0
                max_dur_sec = 0.0

                for it in raw_items:
                    lines = it.get("lines", [])
                    is_canc = it.get("isCanceled", False)
                    dom_side = it.get("domSide", "UNKNOWN")
                    if len(lines) >= 3:
                        # True side extracted from DOM background style class (.ovv2-item-bg-l = BUY, .ovv2-item-bg-s = SELL)
                        side_str = dom_side if dom_side in ("BUY", "SELL") else "UNKNOWN"
                        if "C" in lines:
                            is_canc = True
                        
                        # Find price, notional, and age
                        price = 0.0
                        notional_str = ""
                        dur_str = ""
                        
                        for tok in lines[1:]:
                            if tok == "C":
                                is_canc = True
                                continue
                            if tok.startswith("$"):
                                notional_str = tok
                            elif any(c in tok for c in ["m", "H", "D", "s"]) and re.search(r'\d', tok):
                                dur_str = tok
                            elif price == 0.0:
                                try:
                                    price = float(tok.replace(",", ""))
                                except Exception:
                                    pass

                        notional_usd = parse_notional(notional_str)
                        dur_sec = parse_duration_seconds(dur_str)

                        if side_str == "BUY":
                            buy_notional += notional_usd
                        elif side_str == "SELL":
                            sell_notional += notional_usd

                        if notional_usd > max_order_usd:
                            max_order_usd = notional_usd
                        if dur_sec > max_dur_sec:
                            max_dur_sec = dur_sec

                        parsed_orders.append({
                            "side": side_str,
                            "is_canceled": is_canc,
                            "price": price,
                            "notional_str": notional_str,
                            "notional_usd": notional_usd,
                            "duration_str": dur_str,
                            "duration_seconds": dur_sec,
                            "duration_hours": round(dur_sec / 3600.0, 2)
                        })

                elapsed = round(time.time() - t_asset_start, 2)
                has_buy = buy_notional > 0
                has_sell = sell_notional > 0
                side_parse_health = "HEALTHY" if (has_buy and has_sell) else (
                    "UNILATERAL_BOOK" if len(parsed_orders) < 5 else "SIDE_PARSE_DEGENERATE"
                )
                harvested_data[asset] = {
                    "asset": asset,
                    "orders_count": len(parsed_orders),
                    "side_parse_health": side_parse_health,
                    "total_notional_usd": round(buy_notional + sell_notional, 2),
                    "buy_notional_usd": round(buy_notional, 2),
                    "sell_notional_usd": round(sell_notional, 2),
                    "imbalance_ratio": round(buy_notional / max(sell_notional, 1.0), 3),
                    "max_single_order_usd": round(max_order_usd, 2),
                    "oldest_order_hours": round(max_dur_sec / 3600.0, 2),
                    "top_whale_walls": sorted(parsed_orders, key=lambda x: x["notional_usd"], reverse=True)[:5],
                    "all_orders": parsed_orders,
                    "scrape_duration_s": elapsed
                }
                print(f"[{idx+1}/{len(assets)}] {asset:<5} -> {len(parsed_orders):<3} Whale Orders | Notional: ${buy_notional + sell_notional:,.0f} | Oldest: {round(max_dur_sec/3600.0, 1)}h ({elapsed}s)")

    finally:
        try:
            close_req = urllib.request.Request(f"{CDP_HTTP_URL}/json/close/{tab_id}")
            urllib.request.urlopen(close_req, timeout=5)
            print(f"[WhaleOrdersHarvester] Closed ephemeral tab {tab_id}")
        except Exception as e:
            print(f"[WhaleOrdersHarvester] Note on closing tab: {e}")

    total_duration = round(time.time() - t_start, 2)
    grand_orders = sum(d["orders_count"] for d in harvested_data.values())
    grand_notional = sum(d["total_notional_usd"] for d in harvested_data.values())

    full_payload = {
        "harvest_timestamp_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "harvest_epoch": time.time(),
        "total_assets_scraped": len(harvested_data),
        "total_whale_orders": grand_orders,
        "grand_total_notional_usd": round(grand_notional, 2),
        "total_duration_seconds": total_duration,
        "assets": harvested_data
    }

    # Save active JSON snapshot atomically
    from Terminal.Data_Factory.time_series_database import atomic_write_text
    atomic_write_text(OUTPUT_SNAPSHOT_FILE, json.dumps(full_payload, indent=2))
    print(f"\n✅ Asset-Wise Whale Orders Harvest Complete!")
    print(f"Captured {grand_orders} Whale Orders (${grand_notional:,.0f} total notional) across {len(harvested_data)} assets in {total_duration}s")
    print(f"Saved snapshot to: {OUTPUT_SNAPSHOT_FILE}")

    # Archive to TimeSeriesDatabase if available
    try:
        from Terminal.Data_Factory.time_series_database import TimeSeriesDatabase
        db = TimeSeriesDatabase()
        db.record_snapshot("coinglass_whale_orders", full_payload)
        print("Archived into time_series_database (.json.gz + SQLite index).")
    except Exception as e:
        print(f"Note archiving to time_series_database: {e}")

    return full_payload


if __name__ == "__main__":
    asyncio.run(harvest_whale_orders())
