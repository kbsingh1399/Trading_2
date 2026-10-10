#!/usr/bin/env python3
"""
Terminal/Data_Factory/scrape_hyperdash_telegram_history.py
===========================================================
Deep Scraper & Parser for @hyperdashflows in Telegram Web.
Extracts message history via Chrome DevTools Protocol (CDP),
scrolls backwards to collect historical flow alerts,
parses structured data (TWAPs, Liquidations, Whale Deposits),
and saves both JSON and Parquet archives.
"""

import asyncio
import json
import os
import pathlib
import re
import sys
import time
import urllib.request
import websockets
import pandas as pd

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parents[2]
OUT_DIR = ROOT / "Data" / "Hyperdash_Flows"
OUT_DIR.mkdir(parents=True, exist_ok=True)
JSON_OUT = OUT_DIR / "hyperdash_flows_history.json"
PARQUET_OUT = OUT_DIR / "hyperdash_flows_history.parquet"

CDP_HTTP_URL = "http://127.0.0.1:9222"

def _clean_num(val_str: str, unit: str = "") -> float:
    cleaned = str(val_str).replace(",", "").strip()
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(unit.upper(), 1.0)
    return float(cleaned) * mult

def parse_flow_message(raw_text: str, links: list) -> dict:
    """Parse raw Telegram alert text into structured quant features."""
    cleaned = raw_text.replace("\ueb1f", "").replace("\u200b", "").strip()
    
    # Extract wallet address from links
    wallet_address = None
    asset_slug = None
    for link in links:
        href = link.get("href", "")
        if "/address/0x" in href:
            match = re.search(r"address/(0x[a-fA-F0-9]{40})", href)
            if match:
                wallet_address = match.group(1).lower()
        elif "/asset/" in href:
            match = re.search(r"asset/([A-Za-z0-9_:#]+)", href)
            if match:
                asset_slug = match.group(1)

    # 1. TWAP Alert Pattern
    # e.g.: #xyz:CRCL TWAP Started: Buy $10.16M over 120.5h ($1.40K/min) (118.6K) [dash] [chart]
    twap_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+TWAP\s+Started:\s+(Buy|Sell)\s+\$([\d,\.]+)([KMBkmb]?)\s+over\s+([\d,\.]+)h\s+\(\$([\d,\.]+)([KMBkmb]?)/min\)",
        cleaned,
        re.IGNORECASE
    )
    if twap_match:
        coin = twap_match.group(1).split(":")[-1]
        side = twap_match.group(2).upper()
        total_usd = _clean_num(twap_match.group(3), twap_match.group(4))
        duration_h = float(twap_match.group(5).replace(",", ""))
        rate_per_min = _clean_num(twap_match.group(6), twap_match.group(7))

        return {
            "type": "TWAP_STARTED",
            "coin": coin.upper(),
            "side": side,
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": duration_h,
            "rate_usd_per_min": rate_per_min,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 2. Imminent Liquidation Alert Pattern (supports commas like $82,547.96)
    # e.g.: #BTC Imminent Long Liquidation: $10.45M @ 1.0% away (liq: $82,547.96) [dash] [chart]
    imminent_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+Imminent\s+(Short|Long)\s+Liquidation:\s+\$([\d,\.]+)([KMBkmb]?)\s+@\s+([\d,\.]+)%\s+away\s+\(liq:\s+\$([\d,\.]+)\)",
        cleaned,
        re.IGNORECASE
    )
    if imminent_match:
        coin_raw = imminent_match.group(1).split(":")[-1]
        pos_type = imminent_match.group(2).upper()
        total_usd = _clean_num(imminent_match.group(3), imminent_match.group(4))
        dist_pct = float(imminent_match.group(5).replace(",", ""))
        liq_px = float(imminent_match.group(6).replace(",", ""))

        return {
            "type": "IMMINENT_LIQUIDATION",
            "coin": coin_raw.upper(),
            "side": "SHORT_IMMINENT" if pos_type == "SHORT" else "LONG_IMMINENT",
            "market_impact": "IMMINENT_BUY_CASCADE" if pos_type == "SHORT" else "IMMINENT_SELL_CASCADE",
            "notional_usd": total_usd,
            "distance_pct": dist_pct,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": liq_px,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin_raw,
            "raw_text": cleaned
        }

    # 3. Confirmed Liquidation Alert Pattern
    # e.g.: #NEAR Liquidated Short: $135.53K at $5.4416 [dash] [chart]
    liq_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+Liquidated\s+(Short|Long):\s+\$([\d,\.]+)([KMBkmb]?)\s+at\s+\$([\d,\.]+)",
        cleaned,
        re.IGNORECASE
    )
    if liq_match:
        coin = liq_match.group(1).split(":")[-1]
        pos_type = liq_match.group(2).upper() # Short liquidated = forced buy; Long liquidated = forced sell
        total_usd = _clean_num(liq_match.group(3), liq_match.group(4))
        liq_px = float(liq_match.group(5).replace(",", ""))

        return {
            "type": "LIQUIDATION",
            "coin": coin.upper(),
            "side": "SHORT_LIQUIDATED" if pos_type == "SHORT" else "LONG_LIQUIDATED",
            "market_impact": "BUY_PRESSURE" if pos_type == "SHORT" else "SELL_PRESSURE",
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": liq_px,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 4. Large Whale Execution / Spot or Perp Order
    # e.g.: #BTC Sell: $51.33M at $84,199.72 [dash] [chart]
    # e.g.: #xyz:SILVER Sell: $11.62M at $60.8384 [dash] [chart]
    trade_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+(Buy|Sell):\s+\$([\d,\.]+)([KMBkmb]?)\s+at\s+\$([\d,\.]+)",
        cleaned,
        re.IGNORECASE
    )
    if trade_match:
        coin = trade_match.group(1).split(":")[-1]
        side = trade_match.group(2).upper()
        total_usd = _clean_num(trade_match.group(3), trade_match.group(4))
        fill_px = float(trade_match.group(5).replace(",", ""))
        return {
            "type": "WHALE_TRADE",
            "coin": coin.upper(),
            "side": side,
            "market_impact": "BUY_PRESSURE" if side == "BUY" else "SELL_PRESSURE",
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": fill_px,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 5. Whale Position Close / PnL Realization
    # e.g.: #xyz:SILVER trader closed $12.80M short, realizing +$502.22K profit [dash] [chart]
    close_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+trader\s+closed\s+\$([\d,\.]+)([KMBkmb]?)\s+(short|long),\s+realizing\s+([\+\-]?\$?[\d,\.]+)([KMBkmb]?)\s+profit",
        cleaned,
        re.IGNORECASE
    )
    if close_match:
        coin = close_match.group(1).split(":")[-1]
        pos_type = close_match.group(4).upper()
        size_usd = _clean_num(close_match.group(2), close_match.group(3))
        pnl_str = close_match.group(5).replace("$", "")
        pnl_mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(close_match.group(6).upper(), 1.0)
        pnl_usd = float(pnl_str.replace(",", "")) * pnl_mult
        return {
            "type": "WHALE_POSITION_CLOSE",
            "coin": coin.upper(),
            "side": f"CLOSED_{pos_type}",
            "market_impact": "BUY_COVER" if pos_type == "SHORT" else "SELL_COVER",
            "notional_usd": size_usd,
            "realized_pnl_usd": pnl_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 6. Volume Surge Alert Pattern
    # e.g.: #xyz:SILVER 5m Volume Surge [chart] $85.18M vs $352.29K avg Δ -$28.39M sells
    vol_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+(\d+m)\s+Volume\s+Surge.*?\$([\d,\.]+)([KMBkmb]?)\s+vs\s+\$([\d,\.]+)([KMBkmb]?)\s+avg.*?[Δ\u0394]\s*([+\-]?)\$?([\d,\.]+)([KMBkmb]?)\s+(buys|sells)",
        cleaned,
        re.IGNORECASE | re.DOTALL
    )
    if vol_match:
        coin = vol_match.group(1).split(":")[-1]
        timeframe = vol_match.group(2)
        surge_vol = _clean_num(vol_match.group(3), vol_match.group(4))
        avg_vol = _clean_num(vol_match.group(5), vol_match.group(6))
        sign = -1.0 if vol_match.group(7) == "-" else 1.0
        delta_usd = sign * _clean_num(vol_match.group(8), vol_match.group(9))
        direction = vol_match.group(10).upper()
        return {
            "type": "VOLUME_SURGE",
            "coin": coin.upper(),
            "timeframe": timeframe,
            "side": "BUY_VOLUME" if "BUY" in direction else "SELL_VOLUME",
            "notional_usd": surge_vol,
            "avg_volume_usd": avg_vol,
            "delta_volume_usd": delta_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 7. Open Interest Surge Pattern
    # e.g.: #BTC OI Surge [chart] +$26.27M in 5m 8.9x avg
    # e.g.: #HYPE OI Surge [chart] -$16.36M in 5m 9.5x avg
    oi_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+OI\s+Surge.*?([+\-]?)\$?([\d,\.]+)([KMBkmb]?)\s+in\s+(\w+)\s*([\d,\.]+)x\s+avg",
        cleaned,
        re.IGNORECASE | re.DOTALL
    )
    if oi_match:
        coin = oi_match.group(1).split(":")[-1]
        sign = -1.0 if oi_match.group(2) == "-" else 1.0
        oi_delta_usd = sign * _clean_num(oi_match.group(3), oi_match.group(4))
        timeframe = oi_match.group(5)
        multiple = float(oi_match.group(6).replace(",", ""))
        return {
            "type": "OI_SURGE",
            "coin": coin.upper(),
            "side": "OI_INCREASE" if oi_delta_usd > 0 else "OI_DECREASE",
            "notional_usd": abs(oi_delta_usd),
            "oi_delta_usd": oi_delta_usd,
            "timeframe": timeframe,
            "surge_multiple": multiple,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 8. Funding Surge Pattern
    # e.g.: #xyz:DRAM Funding Surge [chart] -222% APR
    fund_match = re.search(
        r"#([A-Za-z0-9_:#]+)\s+Funding\s+Surge.*?([+\-]?[\d,\.]+)%\s+APR",
        cleaned,
        re.IGNORECASE | re.DOTALL
    )
    if fund_match:
        coin = fund_match.group(1).split(":")[-1]
        apr_pct = float(fund_match.group(2).replace(",", ""))
        return {
            "type": "FUNDING_SURGE",
            "coin": coin.upper(),
            "side": "NEGATIVE_FUNDING_SHORT_SQUEEZE_RISK" if apr_pct < 0 else "POSITIVE_FUNDING_LONG_CROWDED",
            "apr_pct": apr_pct,
            "notional_usd": None,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": asset_slug or coin,
            "raw_text": cleaned
        }

    # 9. Large Deposit / Inflow Pattern
    dep_match = re.search(r"Large\s+Deposit\s*-\s*\$([\d,\.]+)([KMBkmb]?)", cleaned, re.IGNORECASE)
    if dep_match:
        total_usd = _clean_num(dep_match.group(1), dep_match.group(2))
        return {
            "type": "LARGE_DEPOSIT",
            "coin": "USDC",
            "side": "INFLOW",
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": None,
            "raw_text": cleaned
        }

    # 10. Large Withdrawal / Outflow Pattern
    with_match = re.search(r"Large\s+Withdrawal\s*-\s*\$([\d,\.]+)([KMBkmb]?)", cleaned, re.IGNORECASE)
    if with_match:
        total_usd = _clean_num(with_match.group(1), with_match.group(2))
        return {
            "type": "LARGE_WITHDRAWAL",
            "coin": "USDC",
            "side": "OUTFLOW",
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": None,
            "raw_text": cleaned
        }

    # 11. Large Staking / Unstaking Pattern
    # e.g.: Large HYPE Unstake Initiated: 170.6K HYPE ($15.18M) [dash] [chart]
    # e.g.: Large HYPE Staked: 108.8K HYPE ($9.91M) [dash] [chart]
    stake_match = re.search(
        r"Large\s+([A-Za-z0-9]+)\s+(Unstake\s+Initiated|Unstake\s+Finalized|Staked).*?\$([\d,\.]+)([KMBkmb]?)\)",
        cleaned,
        re.IGNORECASE | re.DOTALL
    )
    if stake_match:
        coin = stake_match.group(1).upper()
        action = stake_match.group(2).upper().replace(" ", "_")
        total_usd = _clean_num(stake_match.group(3), stake_match.group(4))
        return {
            "type": "STAKING_FLOW",
            "coin": coin,
            "side": action,
            "notional_usd": total_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": wallet_address,
            "asset_slug": coin,
            "raw_text": cleaned
        }

    # 12. Hyperdash Market Summary Pattern
    # e.g.: Hyperdash Market Summary - Mon, Sep 28   HL 24h Volume $7.5B (+108.5%) Liquidated $63.7M (+270.0%) OI $16.7B (-3.9%)
    summary_match = re.search(
        r"Hyperdash\s+Market\s+Summary.*?Volume\s+\$([\d,\.]+)([KMBkmb]?).*?Liquidated\s+\$([\d,\.]+)([KMBkmb]?).*?OI\s+\$([\d,\.]+)([KMBkmb]?)",
        cleaned,
        re.IGNORECASE | re.DOTALL
    )
    if summary_match:
        vol_usd = _clean_num(summary_match.group(1), summary_match.group(2))
        liq_usd = _clean_num(summary_match.group(3), summary_match.group(4))
        oi_usd = _clean_num(summary_match.group(5), summary_match.group(6))
        return {
            "type": "MARKET_SUMMARY",
            "coin": "HYPERLIQUID_EXCHANGE",
            "side": "MACRO_SUMMARY",
            "volume_24h_usd": vol_usd,
            "liquidations_24h_usd": liq_usd,
            "open_interest_usd": oi_usd,
            "notional_usd": vol_usd,
            "distance_pct": None,
            "duration_hours": None,
            "rate_usd_per_min": None,
            "price": None,
            "wallet_address": None,
            "asset_slug": None,
            "raw_text": cleaned
        }

    # Generic unparsed flow
    return {
        "type": "GENERAL_FLOW",
        "coin": "UNKNOWN",
        "side": "UNKNOWN",
        "notional_usd": None,
        "distance_pct": None,
        "duration_hours": None,
        "rate_usd_per_min": None,
        "price": None,
        "wallet_address": wallet_address,
        "asset_slug": asset_slug,
        "raw_text": cleaned
    }

async def cdp_call(ws, req_id: int, method: str, params: dict = None) -> dict:
    payload = {"id": req_id, "method": method, "params": params or {}}
    await ws.send(json.dumps(payload))
    while True:
        raw = await asyncio.wait_for(ws.recv(), timeout=10.0)
        msg = json.loads(raw)
        if msg.get("id") == req_id:
            return msg

async def scrape_history():
    print(f"Connecting to Chrome CDP at {CDP_HTTP_URL}...", flush=True)
    req = urllib.request.Request(f"{CDP_HTTP_URL}/json")
    with urllib.request.urlopen(req, timeout=3) as resp:
        tabs = json.loads(resp.read().decode("utf-8"))
    
    tg_tab = next((t for t in tabs if "web.telegram.org/k/#@hyperdashflows" in t.get("url", "") or ("web.telegram.org" in t.get("url", "") and "hyperdash" in t.get("url", ""))), None)
    if not tg_tab:
        tg_tab = next((t for t in tabs if "web.telegram.org" in t.get("url", "")), None)
    if not tg_tab:
        print("ERROR: Telegram Web tab not found in Chrome!", file=sys.stderr, flush=True)
        return False

    ws_url = tg_tab["webSocketDebuggerUrl"]
    print(f"Attached to Telegram tab: {tg_tab['title']}", flush=True)

    async with websockets.connect(ws_url, max_size=50_000_000) as ws:
        collected_messages = {}
        last_count = 0
        no_change_iterations = 0

        print("Starting backwards scroll on .bubbles-scrollable to scrape complete history...", flush=True)
        for iteration in range(1, 150):
            # Extract currently rendered messages
            extract_js = """
            (() => {
                const bubbles = Array.from(document.querySelectorAll('.bubble'));
                const results = [];
                let currentDate = '';
                for (const b of bubbles) {
                    if (b.classList.contains('service') && b.classList.contains('is-date')) {
                        const dateText = b.innerText ? b.innerText.trim() : '';
                        if (dateText) currentDate = dateText;
                        continue;
                    }
                    if (b.classList.contains('bubble-service') || b.querySelector('.service-msg')) continue;
                    
                    const text = b.innerText ? b.innerText.trim() : '';
                    if (!text || text.length < 5) continue;
                    
                    const timeEl = b.querySelector('.time, .bubble-time');
                    const timeStr = timeEl ? timeEl.innerText.trim() : '';
                    const links = Array.from(b.querySelectorAll('a')).map(a => ({ text: a.innerText, href: a.href }));
                    const mid = b.getAttribute('data-mid') || b.getAttribute('data-msg-id');
                    
                    results.push({
                        id: mid || text.substring(0, 50),
                        mid: mid,
                        text: text,
                        time: timeStr,
                        date_heading: currentDate,
                        links: links
                    });
                }
                return results;
            })()
            """
            resp = await cdp_call(ws, iteration * 10, 'Runtime.evaluate', {'expression': extract_js, 'returnByValue': True})
            items = resp.get('result', {}).get('result', {}).get('value', [])

            for item in items:
                mid = item.get('id')
                if mid and mid not in collected_messages:
                    collected_messages[mid] = item

            current_count = len(collected_messages)
            if current_count == last_count:
                no_change_iterations += 1
            else:
                no_change_iterations = 0
            last_count = current_count

            print(f"Iteration {iteration:03d}: {current_count} unique messages collected (new this step: {len(items)} rendered)...", flush=True)

            if no_change_iterations >= 8:
                print(f"History top reached (no new messages loaded for 8 iterations).", flush=True)
                break

            # Scroll .bubbles-scrollable container to 0
            scroll_js = """
            (() => {
                const scroller = document.querySelector('.bubbles-scrollable');
                if (scroller) {
                    scroller.scrollTop = 0;
                    return true;
                }
                return false;
            })()
            """
            await cdp_call(ws, iteration * 10 + 1, 'Runtime.evaluate', {'expression': scroll_js, 'returnByValue': True})

            # Wait for Telegram's async network request to fetch older messages
            await asyncio.sleep(0.85)

        print(f"\nScraping complete! Total unique messages scraped: {len(collected_messages)}", flush=True)

        # Parse all records into structured format
        structured_records = []
        for mid, item in collected_messages.items():
            parsed = parse_flow_message(item["text"], item.get("links", []))
            parsed["msg_id"] = mid
            parsed["time_label"] = item.get("time", "")
            parsed["date_heading"] = item.get("date_heading", "")
            structured_records.append(parsed)

        # Save to JSON
        JSON_OUT.write_text(json.dumps(structured_records, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Saved structured JSON to {JSON_OUT} ({len(structured_records)} items)")

        # Save to Parquet
        try:
            df = pd.DataFrame(structured_records)
            df.to_parquet(PARQUET_OUT, index=False)
            print(f"Saved structured Parquet to {PARQUET_OUT} ({df.shape[0]} rows, {df.shape[1]} cols)")
        except Exception as e:
            print(f"Warning: Could not save Parquet: {e}")

        # Summary Statistics
        df = pd.DataFrame(structured_records)
        type_counts = df['type'].value_counts().to_dict()
        print("\n--- HYPERDASH FLOW SUMMARY STATISTICS ---")
        for t, cnt in type_counts.items():
            print(f"  * {t:<20}: {cnt} alerts")

        if 'notional_usd' in df:
            valid_notionals = df[df['notional_usd'].notnull()]
            print(f"\nTotal Notional Volume Tracked: {valid_notionals['notional_usd'].sum():,.2f} USD")
            
        print("\nSample Parsed Records:")
        for r in structured_records[:3]:
            print(json.dumps({k: v for k, v in r.items() if k != 'raw_text'}, indent=2))

        return True

if __name__ == "__main__":
    asyncio.run(scrape_history())
