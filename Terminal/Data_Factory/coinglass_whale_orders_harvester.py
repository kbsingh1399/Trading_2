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
import uuid
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

# Price sanity bounds to physically prevent cross-asset mislabeling (F46)
PRICE_SANITY_BOUNDS = {
    "BTC": (25_000.0, 250_000.0),
    "ETH": (1_000.0, 15_000.0),
    "SOL": (10.0, 1_000.0),
    "BNB": (100.0, 3_000.0),
    "DOGE": (0.01, 3.0),
    "XRP": (0.10, 15.0),
    "ADA": (0.05, 10.0),
    "LINK": (2.0, 150.0),
    "AVAX": (5.0, 300.0),
    "SUI": (0.10, 30.0),
    "NEAR": (0.30, 60.0),
    "DOT": (1.0, 80.0),
    "LTC": (15.0, 600.0),
    "BCH": (40.0, 3_000.0),
    "APT": (1.0, 150.0),
    "OP": (0.10, 30.0),
    "ARB": (0.05, 20.0),
    "TRX": (0.02, 3.0),
}


def get_live_binance_prices() -> Dict[str, float]:
    """Fetch live market prices directly from Binance Futures API to dynamically eliminate all 100/153 overlap bands (F46/C186)."""
    url = "https://fapi.binance.com/fapi/v1/ticker/price"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            prices = {}
            for item in data:
                sym = item.get("symbol", "")
                if sym.endswith("USDT"):
                    asset = sym[:-4]
                    prices[asset] = float(item["price"])
            return prices
    except Exception as e:
        return {}


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


def match_heading_token(heading_text: str | None, target_symbol: str) -> tuple[bool, str]:
    """
    First-token exact match assertion:
    Prevents pair collisions (e.g. SOL/ETH matching ETH) and substring collisions
    (e.g. OP in STOP, LINK in BLINK, ARB in ARBITRUM). Fails closed on empty heading.
    """
    if not heading_text or not heading_text.strip():
        return False, f"Orderbook heading missing or empty: fail-closed for {target_symbol}"
    tokens = [t.upper() for t in re.split(r'[^A-Za-z0-9]+', heading_text.strip()) if t]
    target = target_symbol.upper()
    first_token = tokens[0] if tokens else ""
    exact_match = first_token in (target, f"{target}USDT", f"{target}USD")
    if not exact_match:
        return False, f"First-token mismatch: expected first token {target} in orderbook heading [{heading_text[:50]}] but found tokens [{', '.join(tokens[:10])}]"
    return True, "MATCH"


def match_cross_cycle_orders(
    cur_orders: list[dict],
    prev_orders: list[dict],
    cycle_interval_s: float = 180.0,
    ref_price: float | None = None,
    asset: str = "COIN"
) -> tuple[list[dict], dict]:
    """
    Global bipartite cross-cycle orderbook matching engine.
    - Zero external dependencies: pure Python standard library list-of-lists cost matrix.
    - Uses scipy.optimize.linear_sum_assignment if available; otherwise deterministic greedy edge fallback.
    - Grid-derived price tolerance (2.5 bps, ~20 USD at 80k) guarantees distinct levels never merge.
    - Continuous partial fill attribution: any reduction in notional is attributed as PARTIAL_FILL
      with exact fill_pct, filled_usd, and residual_pct; ZERO arbitrary cliff threshold.
    - Preserves unique track_ids across duration continuity and stacked-order tie breaks.
    - Microstructure attribution for lost orders: attributes FILLED_PRICE_CROSSED vs CANCELED_UNTOUCHED
      based on reference market price.
    """
    exact_matches = 0
    partial_fills = 0
    ambiguous_matches = 0
    new_orders = 0
    ambiguity_log = []
    matched_prev_indices = set()
    out_orders = [dict(o) for o in cur_orders]

    try:
        from scipy.optimize import linear_sum_assignment
        has_scipy = True
    except ImportError:
        has_scipy = False

    for side in ("BUY", "SELL"):
        cur_side_indices = [idx for idx, o in enumerate(out_orders) if o.get("side") == side]
        prev_side_indices = [idx for idx, p in enumerate(prev_orders) if p.get("side") == side]

        if not cur_side_indices or not prev_side_indices:
            for c_idx in cur_side_indices:
                o = out_orders[c_idx]
                cur_p = float(o.get("price", 0.0))
                o["track_id"] = f"{asset}_{o['side']}_{round(cur_p, 4)}_row{c_idx}_{uuid.uuid4().hex[:6]}"
                o["match_status"] = "NEW_ORDER"
                o["lineage"] = {"parent_track_id": None, "relation": "FRESH_BOOK_ENTRY"}
                new_orders += 1
            continue

        M = len(cur_side_indices)
        N = len(prev_side_indices)
        # Pure Python cost matrix: shape (M, N) initialized to 1e9 (zero numpy dependency)
        cost_matrix = [[1e9 for _ in range(N)] for _ in range(M)]

        for m_idx, c_idx in enumerate(cur_side_indices):
            o = out_orders[c_idx]
            cur_p = float(o.get("price", 0.0))
            cur_not = float(o.get("notional_usd", 0.0))
            cur_dur = float(o.get("duration_seconds", 0.0))
            tick_size = 0.0001 if cur_p < 1.0 else (0.01 if cur_p < 500.0 else 0.1)
            price_tol = max(2.0 * tick_size, 0.00025 * cur_p)

            for n_idx, p_idx in enumerate(prev_side_indices):
                prev_o = prev_orders[p_idx]
                prev_p = float(prev_o.get("price", 0.0))
                prev_dur = float(prev_o.get("duration_seconds", 0.0))

                p_diff = abs(cur_p - prev_p)
                p_dev = p_diff / max(prev_p, 1e-4)

                if p_diff <= price_tol or p_dev <= 0.00025:
                    exp_dur = prev_dur + cycle_interval_s
                    dur_err = abs(cur_dur - exp_dur)
                    norm_p = p_diff / max(price_tol, 1e-4)
                    norm_dur = min(dur_err / 180.0, 10.0)
                    cost_matrix[m_idx][n_idx] = norm_p * 1.0 + norm_dur * 0.25

        if has_scipy:
            row_ind, col_ind = linear_sum_assignment(cost_matrix)
        else:
            edges = []
            for r in range(M):
                for c in range(N):
                    if cost_matrix[r][c] < 1e6:
                        edges.append((cost_matrix[r][c], r, c))
            edges.sort(key=lambda x: (
                x[0],
                abs(float(out_orders[cur_side_indices[x[1]]].get("duration_seconds", 0.0)) - (float(prev_orders[prev_side_indices[x[2]]].get("duration_seconds", 0.0)) + cycle_interval_s)),
                -float(prev_orders[prev_side_indices[x[2]]].get("notional_usd", 0.0)),
                float(prev_orders[prev_side_indices[x[2]]].get("price", 0.0))
            ))
            assigned_r = set()
            assigned_c = set()
            row_ind = []
            col_ind = []
            for cost, r, c in edges:
                if r not in assigned_r and c not in assigned_c:
                    assigned_r.add(r)
                    assigned_c.add(c)
                    row_ind.append(r)
                    col_ind.append(c)

        matched_cur_indices = set()
        for r, c in zip(row_ind, col_ind):
            if cost_matrix[r][c] < 1e6:
                c_idx = cur_side_indices[r]
                p_idx = prev_side_indices[c]
                o = out_orders[c_idx]
                prev_o = prev_orders[p_idx]

                matched_cur_indices.add(c_idx)
                matched_prev_indices.add(p_idx)

                cur_p = float(o.get("price", 0.0))
                prev_p = float(prev_o.get("price", 0.0))
                c_not = float(o.get("notional_usd", 0.0))
                p_not = float(prev_o.get("notional_usd", 0.0))

                drift_usd = round(cur_p - prev_p, 4)
                drift_bps = round(abs(cur_p - prev_p) / max(prev_p, 1e-4) * 10000.0, 2)
                delta_notional = round(p_not - c_not, 2)

                # Continuous partial fill formulation (F103: zero cliff threshold across all sizes)
                if delta_notional > 0.0:
                    match_status = "PARTIAL_FILL"
                    fill_pct = round(delta_notional / max(p_not, 1e-4) * 100.0, 2)
                    o["fill_pct"] = fill_pct
                    o["filled_usd"] = delta_notional
                    o["residual_pct"] = round(c_not / max(p_not, 1e-4) * 100.0, 2)
                    partial_fills += 1
                elif delta_notional < 0.0:
                    match_status = "NOTIONAL_EXPANDED"
                    o["expanded_usd"] = round(abs(delta_notional), 2)
                    o["fill_pct"] = 0.0
                    exact_matches += 1
                elif drift_usd != 0.0:
                    match_status = "PRICE_DRIFT_ACCEPTED"
                    exact_matches += 1
                else:
                    match_status = "EXACT_SINGLE_MATCH"
                    exact_matches += 1

                # Tie detection (check if other candidates had tied cost within 0.05)
                tied_count = sum(1 for c2 in range(N) if c2 != c and abs(cost_matrix[r][c2] - cost_matrix[r][c]) < 0.05 and cost_matrix[r][c2] < 1e6)
                is_tied = (tied_count > 0)
                if is_tied:
                    match_status += "_TIED"
                    ambiguous_matches += 1
                    ambiguity_log.append({
                        "price": cur_p,
                        "side": side,
                        "tied_candidates": tied_count + 1,
                        "cost": round(float(cost_matrix[r][c]), 4),
                        "resolved_to_track_id": prev_o.get("track_id")
                    })

                o["track_id"] = prev_o.get("track_id", prev_o.get("row_id", f"{asset}_{o['side']}_{round(cur_p, 4)}"))
                o["match_status"] = match_status
                o["price_dev_bps"] = drift_bps
                o["lineage"] = {
                    "parent_track_id": o["track_id"],
                    "relation": match_status,
                    "price_drift_usd": drift_usd,
                    "price_drift_bps": drift_bps,
                    "global_assignment_cost": round(float(cost_matrix[r][c]), 4)
                }

        # Unassigned current orders become NEW_ORDER with unique IDs
        for m_idx, c_idx in enumerate(cur_side_indices):
            if c_idx not in matched_cur_indices:
                o = out_orders[c_idx]
                cur_p = float(o.get("price", 0.0))
                o["track_id"] = f"{asset}_{o['side']}_{round(cur_p, 4)}_row{c_idx}_{uuid.uuid4().hex[:6]}"
                o["match_status"] = "NEW_ORDER"
                o["lineage"] = {"parent_track_id": None, "relation": "FRESH_BOOK_ENTRY"}
                new_orders += 1

    # Track lost orders with microstructure attribution (FILLED_PRICE_CROSSED vs CANCELED_UNTOUCHED)
    lost_orders = []
    for p_idx, p_o in enumerate(prev_orders):
        if p_idx not in matched_prev_indices:
            p_side = p_o.get("side")
            p_px = float(p_o.get("price", 0.0))
            if ref_price is not None and ref_price > 0:
                if p_side == "BUY":
                    term_status = "FILLED_PRICE_CROSSED" if ref_price <= p_px else "CANCELED_UNTOUCHED"
                elif p_side == "SELL":
                    term_status = "FILLED_PRICE_CROSSED" if ref_price >= p_px else "CANCELED_UNTOUCHED"
                else:
                    term_status = "CANCELED_OR_FILLED"
            else:
                term_status = "CANCELED_OR_FILLED"

            lost_orders.append({
                "track_id": p_o.get("track_id", p_o.get("row_id")),
                "side": p_side,
                "price": p_px,
                "last_notional_usd": p_o.get("notional_usd"),
                "terminal_status": term_status
            })

    report = {
        "total_orders": len(out_orders),
        "exact_matches": exact_matches,
        "partial_fills": partial_fills,
        "ambiguous_matches": ambiguous_matches,
        "new_orders": new_orders,
        "lost_orders_count": len(lost_orders),
        "ambiguity_log": ambiguity_log,
        "lost_orders": lost_orders
    }
    return out_orders, report


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
    skipped_assets: dict[str, str] = {}
    live_binance_prices = get_live_binance_prices()
    if live_binance_prices:
        print(f"[WhaleOrdersHarvester] Fetched {len(live_binance_prices)} live Binance reference prices for dynamic price validation.")

    # Load previous snapshot for cross-cycle order tracking
    prev_snapshot_file = OUTPUT_SNAPSHOT_DIR / "coinglass_whale_orders_snapshot.json"
    prev_snapshot_data: dict[str, dict] = {}
    prev_harvest_epoch: float = 0.0
    cycle_interval_s: float = 180.0
    if prev_snapshot_file.exists():
        try:
            prev_snapshot_root = json.loads(prev_snapshot_file.read_text(encoding="utf-8"))
            prev_snapshot_data = prev_snapshot_root.get("assets", {})
            prev_harvest_epoch = float(prev_snapshot_root.get("harvest_epoch") or 0.0)
            if prev_harvest_epoch > 0:
                cycle_interval_s = max(30.0, min(3600.0, time.time() - prev_harvest_epoch))
        except Exception:
            prev_snapshot_data = {}

    try:
        async with websockets.connect(ws_url, max_size=50_000_000) as ws:
            cur_id = 0
            async def send(method, params=None):
                nonlocal cur_id
                cur_id += 1
                await ws.send(json.dumps({"id": cur_id, "method": method, "params": params or {}}))
                while True:
                    raw = await asyncio.wait_for(ws.recv(), timeout=25.0)
                    msg = json.loads(raw)
                    if msg.get("id") == cur_id:
                        return msg

            await send("Page.enable")
            await send("Page.bringToFront")
            # Wait for initial page hydration
            await asyncio.sleep(4.5)

            for idx, asset in enumerate(assets):
                t_asset_start = time.time()
                try:
                    # Check if asset is already selected
                    check_js = f"""(() => {{
                        const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                        return el ? (el.value || '').trim().toUpperCase() : '';
                    }})()"""
                    chk_res = await send("Runtime.evaluate", {"expression": check_js, "returnByValue": True})
                    cur_val = chk_res.get("result", {}).get("result", {}).get("value", "")

                    if cur_val != asset:
                        # Focus, click, and cleanly reset input via native setter for React/MUI state tracking
                        prepare_input_js = """(() => {
                            const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                            if (!el) return false;
                            el.focus();
                            el.click();
                            const nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
                            nativeSetter.call(el, '');
                            el.dispatchEvent(new Event('input', { bubbles: true }));
                            el.dispatchEvent(new Event('change', { bubbles: true }));
                            return true;
                        })()"""
                        await send("Runtime.evaluate", {"expression": prepare_input_js, "returnByValue": True})
                        await asyncio.sleep(0.2)

                        # Insert target symbol via CDP native input
                        await send("Input.insertText", {"text": asset})
                        await asyncio.sleep(0.6)

                        # Click matching option from MUI listbox (token-based match handles 'Chainlink LINK' and 'LINK')
                        click_opt_js = f"""(() => {{
                            const targetSymbol = {json.dumps(asset)};
                            const listbox = document.querySelector('.MuiAutocomplete-popper, ul.MuiAutocomplete-listbox, div[role="listbox"]');
                            if (!listbox) return {{ status: 'NO_LISTBOX' }};
                            const options = Array.from(listbox.querySelectorAll('li, div[role="option"]'));
                            const match = options.find(o => {{
                                const txt = (o.innerText || '').trim();
                                const tokens = txt.split(/[^A-Za-z0-9]+/).filter(Boolean).map(t => t.toUpperCase());
                                return tokens[0] === targetSymbol || tokens.includes(targetSymbol) || tokens.includes(targetSymbol + 'USDT');
                            }});
                            if (match) {{
                                match.dispatchEvent(new MouseEvent('mousedown', {{ bubbles: true }}));
                                match.dispatchEvent(new MouseEvent('mouseup', {{ bubbles: true }}));
                                match.click();
                                return {{ status: 'CLICKED', text: match.innerText.trim() }};
                            }}
                            return {{ status: 'NO_MATCH', options: options.map(o => o.innerText.trim()) }};
                        }})()"""
                        click_res = await send("Runtime.evaluate", {"expression": click_opt_js, "returnByValue": True})
                        val = click_res.get("result", {}).get("result", {}).get("value", {})
                        if val.get("status") != "CLICKED":
                            reason = f"Dropdown option matching '{asset}' not found or click failed: {val}"
                            print(f"[{idx+1}/{len(assets)}] {asset:<5} -> WARNING: {reason}. Skipping.")
                            skipped_assets[asset] = reason
                            # Ensure popper is closed before moving to next asset
                            close_popper_js = """(() => {
                                const el = document.querySelector('input.MuiAutocomplete-input, input[placeholder*="Search"]');
                                if (el) el.dispatchEvent(new KeyboardEvent('keydown', { key: 'Escape', bubbles: true }));
                            })()"""
                            await send("Runtime.evaluate", {"expression": close_popper_js, "returnByValue": True})
                            harvested_data[asset] = {
                                "asset": asset,
                                "heading_text": "",
                                "orders_count": 0,
                                "side_parse_health": "DROPDOWN_CLICK_FAILED",
                                "rejection_reason": reason,
                                "total_notional_usd": 0.0,
                                "buy_notional_usd": 0.0,
                                "sell_notional_usd": 0.0,
                                "imbalance_ratio": 1.0,
                                "max_single_order_usd": 0.0,
                                "oldest_order_hours": 0.0,
                                "top_whale_walls": [],
                                "all_orders": [],
                                "scrape_duration_s": round(time.time() - t_asset_start, 2)
                            }
                            continue
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

                        // Assert page heading on the orderbook container with first-token exact matching (closes pair and listbox-content gap)
                        const headingEl = document.querySelector('h1.cgj-typo-h1, div[class*="OrderHeatmap"] h1, div[class*="orderbook"] h1, h1[class*="sxTypography"]');

                        if (!headingEl) {{
                            return {{
                                error: 'Orderbook heading element missing: fail-closed for ' + targetSymbol,
                                currentInput: finalInputVal,
                                itemCount: 0,
                                items: []
                            }};
                        }}

                        const headingText = (headingEl.innerText || '').trim().toUpperCase();
                        if (!headingText) {{
                            return {{
                                error: 'Orderbook heading text empty: fail-closed for ' + targetSymbol,
                                currentInput: finalInputVal,
                                itemCount: 0,
                                items: []
                            }};
                        }}

                        // First-token exact match (prevents pair collision SOL/ETH matching ETH, and eliminates substring collisions OP/STOP, LINK/BLINK, ARB/ARBITRUM)
                        const tokens = headingText.split(/[^A-Za-z0-9]+/).filter(Boolean);
                        const firstToken = tokens.length > 0 ? tokens[0] : '';
                        const exactTokenMatch = (firstToken === targetSymbol || firstToken === targetSymbol + 'USDT' || firstToken === targetSymbol + 'USD');
                        if (!exactTokenMatch) {{
                            return {{
                                error: 'First-token mismatch: expected first token ' + targetSymbol + ' in orderbook heading [' + headingText.slice(0, 50) + '] but found tokens [' + tokens.slice(0, 10).join(', ') + ']',
                                currentInput: finalInputVal,
                                headingText: headingText,
                                itemCount: 0,
                                items: []
                            }};
                        }}

                        const items = Array.from(document.querySelectorAll('.large-order-item')).map((el, domIdx) => {{
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
                                domIndex: domIdx,
                                lines: rawLines,
                                isCanceled: isCanceled,
                                domSide: domSide
                            }};
                        }});

                        return {{
                            symbol: targetSymbol,
                            currentInput: finalInputVal,
                            headingText: headingText,
                            itemCount: items.length,
                            items: items
                        }};
                    }})()"""

                    res = await send("Runtime.evaluate", {"expression": extract_js, "returnByValue": True})
                    val = res.get("result", {}).get("result", {}).get("value", {})
                    extracted_heading = val.get("headingText", "") if val else ""
                    if not val or val.get("error"):
                        err_msg = val.get("error") if val else "No result from extraction script"
                        print(f"[{idx+1}/{len(assets)}] {asset:<5} -> WARNING: {err_msg}. Skipping.")
                        skipped_assets[asset] = err_msg
                        harvested_data[asset] = {
                            "asset": asset,
                            "heading_text": extracted_heading,
                            "orders_count": 0,
                            "side_parse_health": "EXTRACTION_EVAL_ERROR",
                            "rejection_reason": err_msg,
                            "total_notional_usd": 0.0,
                            "buy_notional_usd": 0.0,
                            "sell_notional_usd": 0.0,
                            "imbalance_ratio": 1.0,
                            "max_single_order_usd": 0.0,
                            "oldest_order_hours": 0.0,
                            "top_whale_walls": [],
                            "all_orders": [],
                            "scrape_duration_s": round(time.time() - t_asset_start, 2)
                        }
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
                                "row_id": f"{asset}_{side_str}_{it.get('domIndex', len(parsed_orders))}_{round(price, 4)}",
                                "side": side_str,
                                "is_canceled": is_canc,
                                "price": price,
                                "notional_str": notional_str,
                                "notional_usd": notional_usd,
                                "duration_str": dur_str,
                                "duration_seconds": dur_sec,
                                "duration_hours": round(dur_sec / 3600.0, 2)
                            })

                    # Dynamic Price Sanity Gate (Q1 / C186): eliminates all 100/153 overlap bands
                    if parsed_orders:
                        prices = [o["price"] for o in parsed_orders if o.get("price", 0.0) > 0.0]
                        if prices:
                            import statistics
                            median_px = statistics.median(prices)
                            rejection_reason = None
                            # Primary: Dynamic 15% check against live Binance price
                            ref_px = live_binance_prices.get(asset)
                            if ref_px and ref_px > 0:
                                dev = abs(median_px - ref_px) / ref_px
                                if dev > 0.15:
                                    rejection_reason = f"DYNAMIC_PRICE_SANITY: Median price {median_px:.4f} deviates by {dev*100:.1f}% from live Binance price {ref_px:.4f} (>15% threshold)"
                            if not rejection_reason:
                                # Secondary: Static canonical bounds check
                                min_p, max_p = PRICE_SANITY_BOUNDS.get(asset, (0.0, 1e9))
                                if not (min_p <= median_px <= max_p):
                                    rejection_reason = f"STATIC_PRICE_SANITY: Median price {median_px:.2f} is outside [{min_p}, {max_p}]"
                            if rejection_reason:
                                print(f"[{idx+1}/{len(assets)}] {asset:<5} -> REJECTED: {rejection_reason}. Skipping stale table.")
                                skipped_assets[asset] = rejection_reason
                                harvested_data[asset] = {
                                    "asset": asset,
                                    "heading_text": extracted_heading,
                                    "orders_count": 0,
                                    "side_parse_health": "PRICE_SANITY_REJECTED",
                                    "rejection_reason": rejection_reason,
                                    "total_notional_usd": 0.0,
                                    "buy_notional_usd": 0.0,
                                    "sell_notional_usd": 0.0,
                                    "imbalance_ratio": 1.0,
                                    "max_single_order_usd": 0.0,
                                    "oldest_order_hours": 0.0,
                                    "top_whale_walls": [],
                                    "all_orders": [],
                                    "scrape_duration_s": round(time.time() - t_asset_start, 2)
                                }
                                continue

                    # Cross-Cycle Global Bipartite Matching (Q2 / C191 / C194: zero-dependency Hungarian / greedy fallback)
                    prev_orders = prev_snapshot_data.get(asset, {}).get("all_orders", [])
                    ref_px = live_binance_prices.get(asset)
                    parsed_orders, ambiguity_report = match_cross_cycle_orders(
                        cur_orders=parsed_orders,
                        prev_orders=prev_orders,
                        cycle_interval_s=cycle_interval_s,
                        ref_price=ref_px,
                        asset=asset
                    )

                    elapsed = round(time.time() - t_asset_start, 2)
                    has_buy = buy_notional > 0
                    has_sell = sell_notional > 0
                    side_parse_health = "HEALTHY" if (has_buy and has_sell) else (
                        "UNILATERAL_BOOK" if len(parsed_orders) < 5 else "SIDE_PARSE_DEGENERATE"
                    )
                    harvested_data[asset] = {
                        "asset": asset,
                        "heading_text": extracted_heading,
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
                        "ambiguity_report": ambiguity_report,
                        "scrape_duration_s": elapsed
                    }

                    print(f"[{idx+1}/{len(assets)}] {asset:<5} -> Heading: '{extracted_heading}' | {len(parsed_orders):<3} Whale Orders | Notional: ${buy_notional + sell_notional:,.0f} | Oldest: {round(max_dur_sec/3600.0, 1)}h ({elapsed}s)")
                except Exception as asset_err:
                    reason = f"ASSET_EXTRACTION_EXCEPTION: {type(asset_err).__name__}: {asset_err}"
                    print(f"[{idx+1}/{len(assets)}] {asset:<5} -> ERROR: {reason}. Continuing to next asset.")
                    skipped_assets[asset] = reason
                    harvested_data[asset] = {
                    "asset": asset,
                    "heading_text": "",
                    "orders_count": 0,
                    "side_parse_health": "ERROR_DURING_EXTRACTION",
                    "rejection_reason": reason,
                    "total_notional_usd": 0.0,
                    "buy_notional_usd": 0.0,
                    "sell_notional_usd": 0.0,
                    "imbalance_ratio": 1.0,
                    "max_single_order_usd": 0.0,
                    "oldest_order_hours": 0.0,
                    "top_whale_walls": [],
                    "all_orders": [],
                    "ambiguity_report": {
                    "total_orders": 0,
                    "exact_matches": 0,
                    "partial_fills": 0,
                    "ambiguous_matches": 0,
                    "new_orders": 0,
                    "lost_orders_count": 0,
                    "ambiguity_log": [],
                    "lost_orders": []
                    },
                    "scrape_duration_s": round(time.time() - t_asset_start, 2)
                    }

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
        "total_assets_queried": len(assets),
        "total_assets_attempted": len(assets),
        "total_assets_dom_extracted": len(harvested_data),
        "total_assets_price_rejected": sum(1 for a, d in harvested_data.items() if d.get("side_parse_health") == "PRICE_SANITY_REJECTED"),
        "total_assets_ingested": sum(1 for a, d in harvested_data.items() if d.get("side_parse_health") in ["HEALTHY", "UNILATERAL_BOOK"] and d.get("orders_count", 0) > 0),
        "total_assets_with_orders": sum(1 for a, d in harvested_data.items() if d.get("orders_count", 0) > 0),
        "total_whale_orders": grand_orders,
        "grand_total_notional_usd": round(grand_notional, 2),
        "total_duration_seconds": total_duration,
        "skipped_assets": skipped_assets,
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
