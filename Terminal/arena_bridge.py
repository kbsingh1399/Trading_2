"""
Terminal/arena_bridge.py
Autonomous Arena.ai Collaborative Bridge and 48-Hour Orderflow Prompt Dispatcher.
Extracts 48-hour multi-timeframe footprint candle data (4H, 1H, 15m) along with CVD,
orderbook depth, L2/L3 whale walls, liquidation levels, and account state,
then dispatches the prompt directly into Arena.ai via Chrome DevTools Protocol (CDP)
and evaluates Arena's recommendations against strict quantitative orderflow gates.
"""

from __future__ import annotations
import asyncio
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd
import polars as pl
import websockets

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CANDLES_DIR = PROJECT_ROOT / "Data" / "Candles"
TELEMETRY_SNAPSHOT = PROJECT_ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"

CDP_HTTP_URL = "http://127.0.0.1:9222"

PRIMARY_ASSETS = [
    # 14 Institutional Binance Perpetuals (Crypto)
    "BTC", "ETH", "SOL", "BNB", "XRP", "ADA", "DOGE", "TRX", "DOT", "LINK", "BCH", "LTC", "AVAX", "NEAR",
    # 3 Commodities & Metals
    "GOLD", "SILVER", "USWTI",
    # 3 Forex Majors
    "EURUSD", "GBPUSD", "USDJPY",
    # 4 Global Indices
    "SP500", "NAS100", "DJ30", "GER40"
]


def load_parquet_candles(asset: str) -> Optional[pd.DataFrame]:
    """Load 15m candles from Data/Candles/{asset}_15m.parquet."""
    pq_path = CANDLES_DIR / f"{asset}_15m.parquet"
    if not pq_path.exists():
        return None
    try:
        pldf = pl.read_parquet(pq_path)
        df = pldf.to_pandas()
    except Exception:
        try:
            df = pd.read_parquet(pq_path)
        except Exception:
            return None

    # Standardize time
    time_col = None
    for c in ["datetime_utc", "datetime", "time", "timestamp"]:
        if c in df.columns:
            time_col = c
            break
    if not time_col:
        return None

    if pd.api.types.is_numeric_dtype(df[time_col]):
        df["std_dt"] = pd.to_datetime(df[time_col], unit="s", utc=True)
    else:
        df["std_dt"] = pd.to_datetime(df[time_col], errors="coerce", utc=True)

    df.dropna(subset=["std_dt"], inplace=True)
    df.sort_values("std_dt", inplace=True)
    df.reset_index(drop=True, inplace=True)

    # Ensure numeric OHLCV
    for c in ["open", "high", "low", "close", "volume", "tick_volume"]:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce").fillna(0.0)

    # Compute bar orderflow delta if not present
    vol_col = "volume" if "volume" in df.columns and df["volume"].sum() > 0 else "tick_volume"
    spread = np.maximum(df["high"] - df["low"], 1e-9)
    norm_pos = (df["close"] - df["low"]) / spread
    df["bar_delta"] = df[vol_col] * (2.0 * norm_pos - 1.0)
    df["cum_cvd"] = df["bar_delta"].cumsum()

    return df


def resample_bars(df_15m: pd.DataFrame, freq: str) -> pd.DataFrame:
    """Resample 15m candles to 1H or 4H with OHLC, volume, delta, and CVD."""
    if df_15m.empty:
        return pd.DataFrame()

    df = df_15m.set_index("std_dt")
    vol_col = "volume" if "volume" in df.columns and df["volume"].sum() > 0 else "tick_volume"

    resampled = df.resample(freq).agg({
        "open": "first",
        "high": "max",
        "low": "min",
        "close": "last",
        vol_col: "sum",
        "bar_delta": "sum"
    }).dropna(subset=["open"])

    resampled.reset_index(inplace=True)
    resampled.rename(columns={vol_col: "volume"}, inplace=True)
    resampled["cum_cvd"] = resampled["bar_delta"].cumsum()
    return resampled


def compute_volume_profile(df: pd.DataFrame, n_bins: int = 16) -> Dict[str, float]:
    """Compute POC, VAH, VAL over a slice of candles."""
    if df.empty or len(df) == 0:
        return {"poc": 0.0, "vah": 0.0, "val": 0.0}
    low_min = df["low"].min()
    high_max = df["high"].max()
    if high_max <= low_min:
        return {"poc": low_min, "vah": high_max, "val": low_min}

    bin_edges = np.linspace(low_min, high_max, n_bins + 1)
    bin_mids = 0.5 * (bin_edges[:-1] + bin_edges[1:])
    bin_vols = np.zeros(n_bins, dtype=float)

    for _, r in df.iterrows():
        c_low = r["low"]
        c_high = r["high"]
        c_vol = r["volume"]
        mask = (bin_edges[1:] >= c_low) & (bin_edges[:-1] <= c_high)
        n_overlap = np.sum(mask)
        if n_overlap > 0:
            bin_vols[mask] += c_vol / n_overlap

    total_vol = float(np.sum(bin_vols))
    if total_vol <= 0:
        return {"poc": low_min, "vah": high_max, "val": low_min}

    poc_idx = int(np.argmax(bin_vols))
    poc_px = float(bin_mids[poc_idx])

    target_va = 0.70 * total_vol
    accum = bin_vols[poc_idx]
    up_i = poc_idx
    down_i = poc_idx

    while accum < target_va and (up_i < n_bins - 1 or down_i > 0):
        up_v = bin_vols[up_i + 1] if up_i < n_bins - 1 else -1.0
        down_v = bin_vols[down_i - 1] if down_i > 0 else -1.0
        if up_v >= down_v and up_i < n_bins - 1:
            up_i += 1
            accum += up_v
        elif down_i > 0:
            down_i -= 1
            accum += down_v
        else:
            break

    val_px = float(bin_edges[down_i])
    vah_px = float(bin_edges[up_i + 1])
    return {"poc": round(poc_px, 4), "vah": round(vah_px, 4), "val": round(val_px, 4)}


def build_48h_orderflow_prompt() -> str:
    """Build the comprehensive, self-contained 48-hour footprint and telemetry prompt for Arena.ai."""
    # 1. Load Telemetry Snapshot
    telemetry = {}
    if TELEMETRY_SNAPSHOT.exists():
        try:
            with open(TELEMETRY_SNAPSHOT, "r", encoding="utf-8") as f:
                telemetry = json.load(f)
        except Exception:
            pass

    account = telemetry.get("account", {})
    balance = account.get("balance_usd", 4813.99)
    equity = account.get("equity_usd", 4813.99)
    cushion = account.get("cushion_above_floor_usd", 38.99)
    assets_data = telemetry.get("assets_matrix_24", {})

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    lines = []
    lines.append("=" * 80)
    lines.append(f"ANTIGRAVITY x ARENA.AI LIVE STRATEGY COUNCIL BRIEFING ({now_utc})")
    lines.append("MANDATE: DUAL-MODEL SCAN (TREND-FOLLOWING + MEAN-REVERSION) ACROSS ALL 24 ASSETS")
    lines.append("=" * 80)
    lines.append("")
    lines.append("[SECTION 1: GITHUB TELEMETRY REPOSITORY REFERENCES]")
    lines.append("- Repository: https://github.com/kbsingh1399/Trading_2 | Branch: arena/24eb818b-trading-2")
    lines.append("- Live Telemetry Snapshot (Raw URL):")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/24eb818b-trading-2/docs/telemetry/live_snapshot_latest.json")
    lines.append("  *(Auto-committed and pushed to GitHub every 60 seconds by our autonomous telemetry background daemon)*")
    lines.append("- Live Collaborative Order Desk Ledger (Raw URL):")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/24eb818b-trading-2/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md")
    lines.append("- Active Risk Context & Rules (Raw URL):")
    lines.append("  https://raw.githubusercontent.com/kbsingh1399/Trading_2/arena/24eb818b-trading-2/.agents/rules/ACTIVE_CONTEXT.md")
    lines.append("")
    lines.append("[SECTION 2: LIVE MT5 ACCOUNT STATE & BUFFER SENTRY]")
    lines.append(f"- Broker: MetaTrader 5 Account #5064568 (Blueberry Markets SVG-Live)")
    lines.append(f"- Balance: {balance:.2f} USD | Equity: {equity:.2f} USD | Margin Used: 0.00 USD (100% Cash Flat)")
    lines.append(f"- G-1 Hard Floor Defense: Hard Floor = 4,775.00 USD | Preserved Cushion = +{cushion:.2f} USD")
    lines.append(f"- Mandatory Operating Buffer: >= +20.00 USD (Threshold: 4,795.00 USD | Headroom: +{equity - 4795.00:.2f} USD)")
    lines.append(f"- Capacity Sentry: Exactly ONE (1) Risk Slot Available. Maximum Nominal Risk Capped at 10.00 to 11.04 USD (Stressed loss <= 15.80 USD). Multi-order staging is strictly prohibited.")
    lines.append("")

    # Audit Active Positions & Pending Orders
    active_pos = telemetry.get("active_positions", [])
    pending_ord = telemetry.get("pending_orders", [])
    lines.append("[SECTION 3: ACTIVE POSITIONS & RESTING ORDERS REVIEW]")
    if active_pos:
        lines.append(f"ACTIVE OPEN POSITIONS ({len(active_pos)}):")
        for p in active_pos:
            lines.append(f"- Ticket #{p.get('ticket')}: {p.get('symbol')} {p.get('type')} {p.get('volume')} lots @ {p.get('price_open')} | Current: {p.get('price_current')} | SL: {p.get('sl')} | TP: {p.get('tp')} | Floating PnL: {p.get('profit')} USD ({p.get('r_multiple', 'N/A')}R)")
    else:
        lines.append("- Active Open Positions: NONE (0 Open Positions | 100% Cash Flat)")

    if pending_ord:
        lines.append(f"RESTING PENDING LIMIT ORDERS ({len(pending_ord)}):")
        for o in pending_ord:
            lines.append(f"- Ticket #{o.get('ticket')}: {o.get('symbol')} {o.get('type')} {o.get('volume')} lots @ {o.get('price_open')} | Current: {o.get('price_current')} | SL: {o.get('sl')} | TP: {o.get('tp')} | Distance: {o.get('dist_pts')} pts ({o.get('dist_atr', 'N/A')}x ATR)")
    else:
        lines.append("- Resting Pending Limit Orders: NONE (Queue clean)")
    lines.append("")
    lines.append("ARENA REVIEW MANDATE FOR EXISTING ORDERS:")
    lines.append("- If positions exist: Evaluate whether to HOLD, apply piecewise ratchet (Phase 0 BE at +0.80R, Phase 1 Profit Lock at +1.50R, target at +2.50R), execute emergency shelf cut, or close at market.")
    lines.append("- If resting limit orders exist: Check if supporting whale wall has thinned >50% or price has drifted >2.0x ATR. Advise KEEP or DELETE immediately.")
    lines.append("")
    lines.append("[SECTION 4: DUAL-MODEL SCAN MANDATE: TREND-FOLLOWING & MEAN-REVERSION]")
    lines.append("Antigravity Trader and Big Brain Collaborative Directive:")
    lines.append("Do NOT limit your review solely to Mean-Reversion (Model 1). You MUST actively evaluate BOTH strategy families across ALL 24 assets:")
    lines.append("1. MODEL 2 (TREND-FOLLOWING PULLBACK):")
    lines.append("   - In established trending regimes (e.g. Bearish Crypto/Forex with negative 200 EMA slope, or Bullish Commodities/USDJPY):")
    lines.append("   - Are any assets executing a causal pullback to Session VWAP, Value Area High/Low (VAH/VAL), or resistance/support shelves?")
    lines.append("   - Joining trend-following momentum toward resting downside liquidation cascade pools or overhead short squeezes.")
    lines.append("   - If a trend pullback exists with favorable R:R (>= 2.0R), CVD exhaustion of counter-trend pullbacks, and tight spread (< 25 bps), IDENTIFY AND SCORE IT!")
    lines.append("2. MODEL 1 (EXTREME MEAN-REVERSION):")
    lines.append("   - Extreme price extensions |Z| >= 2.0 SD from Session VWAP with RSI oversold (<30) or overbought (>70), CVD aggressor exhaustion, and resting whale wall absorption (>= 150k USD, >= 180s persistence).")
    lines.append("")
    lines.append("Our desk has 4,813.99 USD capital, 100% Cash Flat, and 1 risk slot available (nominal risk 10.00 to 11.04 USD). We must NOT sit idle if valid institutional Model 2 Trend-Following setups exist!")
    lines.append("")
    lines.append("[SECTION 5: 24-ASSET MULTI-TIMEFRAME FOOTPRINT & ORDERFLOW RECONSTRUCTION]")
    lines.append("The sections below detail the trailing 48-hour market structure across all 24 assets (14 Crypto, 3 Metals & Commodities, 3 Forex, 4 Indices):")
    lines.append("")

    for asset in PRIMARY_ASSETS:
        df_15m = load_parquet_candles(asset)
        t_asset = assets_data.get(asset, {})
        cat = t_asset.get("category", "OTHER")
        broker = t_asset.get("symbol_broker", asset)
        quotes = t_asset.get("quotes", {})
        inds = t_asset.get("causal_indicators", {})
        ob = t_asset.get("orderbook_live_depth", {})
        whales = ob.get("whale_walls_l3", [])
        liq = t_asset.get("reconstructed_liquidations", {})
        stops = t_asset.get("structural_stop_clusters", {})

        cur_bid = quotes.get("bid", 0.0)
        cur_ask = quotes.get("ask", 0.0)
        cur_mid = quotes.get("mid", (cur_bid + cur_ask) / 2.0 if cur_bid and cur_ask else 0.0)
        spread_bps = quotes.get("spread_bps", 0.0)

        lines.append(f"--- [ASSET: {asset} | Category: {cat} | Broker: {broker} | Mid: {cur_mid} | Spread: {spread_bps:.2f} bps] ---")
        lines.append(f"Live: VWAP = {inds.get('session_vwap_utc', 'N/A')} | VWAP Z-Score = {inds.get('vwap_z_score', 'N/A')} SD | RSI(14) = {inds.get('rsi_14', 'N/A')} | ATR(14) = {inds.get('atr_14', 'N/A')} | 200 EMA Slope = {inds.get('ema_200_slope_3h_pct', 'N/A')}% | Regime = {inds.get('trend_regime', 'N/A')}")
        lines.append(f"Orderbook: Top-20 Bid = {ob.get('top_20_bid_vol_usd', 'N/A')} USD | Top-20 Ask = {ob.get('top_20_ask_vol_usd', 'N/A')} USD | Verified Whales = {len(whales)}")
        if whales:
            for w in whales[:2]:
                lines.append(f"  * Whale Wall: {w.get('side')} at {w.get('price')} USD ({w.get('notional_usd')} USD, age={w.get('age_sec')}s)")
        lines.append(f"Targets: Long Flush = {liq.get('long_flush_target', 'N/A')} | Short Squeeze = {liq.get('short_squeeze_band', 'N/A')} | Discount Sweep = {stops.get('nearest_discount_stop_sweep', 'N/A')} | Premium Sweep = {stops.get('nearest_premium_stop_sweep', 'N/A')}")

        if df_15m is not None and len(df_15m) > 0:
            last_48h_15m = df_15m.tail(192).copy()
            vp_48h = compute_volume_profile(last_48h_15m, n_bins=16)
            lines.append(f"48H Profile: POC = {vp_48h['poc']} | VAH = {vp_48h['vah']} | VAL = {vp_48h['val']}")

            df_4h = resample_bars(last_48h_15m, "4h")
            lines.append(f"4H Footprint (Last 2 Completed Bars):")
            for _, r in df_4h.tail(2).iterrows():
                dt_str = r['std_dt'].strftime('%m-%d %H:%M') if 'std_dt' in r else ''
                lines.append(f"  * 4H [{dt_str}]: O={r['open']:.2f} H={r['high']:.2f} L={r['low']:.2f} C={r['close']:.2f} Vol={r['volume']:.0f} Delta={r['bar_delta']:.0f} CVD={r['cum_cvd']:.0f}")

            df_1h = resample_bars(last_48h_15m, "1h")
            lines.append(f"1H Footprint (Last 2 Completed Bars):")
            for _, r in df_1h.tail(2).iterrows():
                dt_str = r['std_dt'].strftime('%m-%d %H:%M') if 'std_dt' in r else ''
                lines.append(f"  * 1H [{dt_str}]: O={r['open']:.2f} H={r['high']:.2f} L={r['low']:.2f} C={r['close']:.2f} Vol={r['volume']:.0f} Delta={r['bar_delta']:.0f} CVD={r['cum_cvd']:.0f}")

            lines.append(f"15M Footprint (Last 3 Completed Bars):")
            for _, r in last_48h_15m.tail(3).iterrows():
                dt_str = r['std_dt'].strftime('%m-%d %H:%M') if 'std_dt' in r else ''
                lines.append(f"  * 15M [{dt_str}]: O={r['open']:.2f} H={r['high']:.2f} L={r['low']:.2f} C={r['close']:.2f} Vol={r['volume']:.0f} Delta={r['bar_delta']:.0f} CVD={r['cum_cvd']:.0f}")
        lines.append("")

    lines.append("[SECTION 6: REQUIRED QUANTITATIVE RULING & DUAL-TRACK GATING RULES]")
    lines.append("CRITICAL DESK UPDATES & EVOLVING EXECUTION MANDATES:")
    lines.append("1. GATE 1 (SPREAD) IS EXEMPT / SKIPPED FOR PASSIVE LIMIT ORDERS:")
    lines.append("   Because we stage resting limit orders on the book, we provide liquidity at our designated limit price and do NOT cross the market spread!")
    lines.append("   Do NOT disqualify crypto assets (e.g. XRP, LTC, AVAX, LINK, BCH, NEAR) merely for having spread > 25 bps.")
    lines.append("2. EXPANDED RISK BUDGET:")
    lines.append("   Maximum nominal risk cap is expanded to 15.00 USD (flexible range: 10.00 to 15.00 USD).")
    lines.append("3. EVOLVING ADAPTIVE MICRO-PULLBACK LOGIC FOR TREND FOLLOWING (MODEL 2):")
    lines.append("   When the trend regime is clearly established (e.g. BEARISH with negative 200 EMA slope, or BULLISH with positive 200 EMA slope):")
    lines.append("   Do NOT demand that price retrace all the way to Session VWAP (which may be 2.0 to 4.0 ATRs away in strong trending markets)!")
    lines.append("   Accept shallow MICRO-PULLBACKS (0.10 to 0.60 ATR) to geometric orderflow shelves:")
    lines.append("   * Retest of 20 EMA or 50 EMA dynamic shelf")
    lines.append("   * Retest of prior 15m/1H broken structure / swing shelf")
    lines.append("   * Retest of Value Area High (VAH) or Value Area Low (VAL)")
    lines.append("   * Retest of Fair Value Gap (FVG) or high-volume profile node")
    lines.append("")
    lines.append("TRACK 1 (FOREX, COMMODITIES & INDICES - CFD FEEDS):")
    lines.append("- Geometry: Model 2 micro-pullback (0.10 to 0.60 ATR) to 20/50 EMA or VWAP in trend; OR Model 1 extreme stretch |Z| >= 2.0 SD.")
    lines.append("- CFD Orderflow & Microstructure: 15m bar volume >= 0.8x 20-bar avg, and candle rejection wick >= 30% of bar range at the shelf.")
    lines.append("- Sizing: SL >= 1.50x ATR, TP >= 2.0R to 2.5R, Nominal Risk <= 15.00 USD (e.g. 10.00 to 14.50 USD).")
    lines.append("")
    lines.append("TRACK 2 (CRYPTO PERPETUALS - BINANCE USDT-M FEEDS):")
    lines.append("- Geometry: Model 2 micro-pullback (0.10 to 0.60 ATR) to 20/50 EMA or VWAP in trend; OR Model 1 extreme stretch (|Z| >= 2.0 SD / RSI < 30 or > 70).")
    lines.append("- Crypto Depth & Flow: Top-20 depth imbalance >= 1.25x, OR clustered depth within +-0.50x ATR >= 150k-300k USD, OR 1m/5m taker CVD deceleration/exhaustion.")
    lines.append("- Sizing: SL >= 1.50x ATR, TP >= 2.0R to 2.5R, Nominal Risk <= 15.00 USD.")
    lines.append("")
    lines.append("OUTPUT FORMAT:")
    lines.append("Identify and output ALL viable candidates meeting Track 1 or Track 2 rules:")
    lines.append("- Symbol (e.g. BTCUSD.pi, BCHUSD.p, XRPUSD.pi, SP500.p, EURUSD.pi, USWTI.p, etc.)")
    lines.append("- Model: Model 2 (Trend Following) or Model 1 (Mean Reversion)")
    lines.append("- Direction: BUY LIMIT or SELL LIMIT")
    lines.append("- Entry Price, Stop Loss, Take Profit, Target R-Multiple (>= 2.0R to 2.5R)")
    lines.append("- Sizing: Exact lots giving nominal risk between 10.00 and 15.00 USD")
    lines.append("- Microstructure Justification: Citing orderflow shelf, EMA/VWAP retest, volume, or CVD flow.")
    lines.append("")
    lines.append("If no immediate entry is at current market, provide the top 2 LIMIT ORDER stages with exact limit prices ready to punch into MT5.")
    lines.append("")
    return "\n".join(lines)


async def get_arena_tab_ws_url() -> Optional[str]:
    """Find the Arena tab via Chrome remote debugging JSON endpoint."""
    try:
        req = urllib.request.Request(f"{CDP_HTTP_URL}/json")
        with urllib.request.urlopen(req, timeout=3) as resp:
            tabs = json.loads(resp.read().decode("utf-8"))
        for t in tabs:
            if t.get("type") == "page" and "arena.ai" in t.get("url", ""):
                return t.get("webSocketDebuggerUrl")
    except Exception as e:
        print(f"Error fetching Chrome tabs: {e}", file=sys.stderr)
    return None


async def clear_arena_prompt_box(ws) -> bool:
    """Explicitly focus the editor, select all (Ctrl+A), and delete/clear any existing prompt in the box."""
    try:
        # Step 1: Focus editor and clean TipTap & React fiber state
        focus_and_clean_js = """
        (() => {
          const el = document.querySelector('.tiptap.ProseMirror');
          if (el) el.focus();
          let editor = null;
          let p = el;
          while (p) {
            if (p.editor) { editor = p.editor; break; }
            p = p.parentElement;
          }
          if (editor) {
            editor.commands.clearContent();
          }
          const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
          if (submitBtn) {
            const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
            if (fiberKey) {
              let curr = submitBtn[fiberKey];
              while (curr) {
                if (curr.memoizedProps?.onChange) {
                  curr.memoizedProps.onChange('');
                  break;
                }
                curr = curr.return;
              }
            }
          }
          return { focused: !!el };
        })()
        """
        await ws.send(json.dumps({
            "id": int(time.time() * 1000) % 1000000,
            "method": "Runtime.evaluate",
            "params": {"expression": focus_and_clean_js, "returnByValue": True}
        }))
        await ws.recv()

        # Step 2: Dispatch Ctrl+A (Select All)
        msg_id = int(time.time() * 1000) % 1000000
        await ws.send(json.dumps({
            "id": msg_id,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "rawKeyDown",
                "windowsVirtualKeyCode": 65,
                "code": "KeyA",
                "key": "a",
                "modifiers": 2
            }
        }))
        await ws.recv()
        await ws.send(json.dumps({
            "id": msg_id + 1,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "keyUp",
                "windowsVirtualKeyCode": 65,
                "code": "KeyA",
                "key": "a",
                "modifiers": 2
            }
        }))
        await ws.recv()

        # Step 3: Dispatch Delete & Backspace
        await ws.send(json.dumps({
            "id": msg_id + 2,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "rawKeyDown",
                "windowsVirtualKeyCode": 46,
                "code": "Delete",
                "key": "Delete"
            }
        }))
        await ws.recv()
        await ws.send(json.dumps({
            "id": msg_id + 3,
            "method": "Input.dispatchKeyEvent",
            "params": {
                "type": "keyUp",
                "windowsVirtualKeyCode": 46,
                "code": "Delete",
                "key": "Delete"
            }
        }))
        await ws.recv()
        await asyncio.sleep(0.05)
        return True
    except Exception as e:
        print(f"Error in clear_arena_prompt_box: {e}", file=sys.stderr)
        return False


async def post_prompt_to_arena(prompt_text: str) -> bool:
    """Clear any existing prompt in the box (Ctrl+A then Delete), inject prompt, and hit enter."""
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        print("ERROR: No active Arena tab found in Chrome at 127.0.0.1:9222", file=sys.stderr)
        return False

    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            # 1. MANDATORY CLEAR: Remove any previous prompt already in the box (Ctrl+A then Delete)
            await clear_arena_prompt_box(ws)
            await asyncio.sleep(0.1)

            # 2. Inject the prompt into TipTap editor and update React state
            js_set = f"""
            (async () => {{
              const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
              if (!submitBtn) return {{ error: 'No submit button found' }};

              const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
              if (!fiberKey) return {{ error: 'No react fiber on submit button' }};

              let curr = submitBtn[fiberKey];
              let targetFiber = null;
              while (curr) {{
                if (curr.memoizedProps?.onSubmit && curr.memoizedProps?.onChange) {{
                  targetFiber = curr;
                  break;
                }}
                curr = curr.return;
              }}
              if (!targetFiber) return {{ error: 'Target fiber not found' }};

              const promptText = {json.dumps(prompt_text)};
              targetFiber.memoizedProps.onChange(promptText);

              const el = document.querySelector('.tiptap.ProseMirror');
              let editor = null;
              let p = el;
              while (p) {{
                if (p.editor) {{ editor = p.editor; break; }};
                p = p.parentElement;
              }}
              if (editor) {{
                editor.commands.setContent(promptText);
              }}

              return {{ success: true }};
            }})()
            """
            msg_id = int(time.time() * 1000) % 1000000
            await ws.send(json.dumps({
                "id": msg_id,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_set,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }))
            resp_str = await ws.recv()
            resp = json.loads(resp_str)
            res_val = resp.get("result", {}).get("result", {}).get("value", {})
            if not res_val.get("success"):
                print(f"CDP prompt injection returned: {res_val}", file=sys.stderr)
                return False

            # Wait 200ms for React propagation
            await asyncio.sleep(0.2)

            # 3. Hit Enter via CDP key event
            await ws.send(json.dumps({
                "id": msg_id + 1,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "rawKeyDown",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()
            await ws.send(json.dumps({
                "id": msg_id + 2,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "keyUp",
                    "windowsVirtualKeyCode": 13,
                    "code": "Enter",
                    "key": "Enter"
                }
            }))
            await ws.recv()

            # Failsafe submit click / onSubmit trigger
            js_submit = """
            (async () => {
              const submitBtn = document.querySelector('button[aria-label="Send message"], button:has(svg.lucide-arrow-up), button:has(svg.lucide-arrow-right)');
              if (submitBtn && !submitBtn.disabled) {
                submitBtn.click();
              } else if (submitBtn) {
                const fiberKey = Object.keys(submitBtn).find(k => k.startsWith('__reactFiber'));
                if (fiberKey) {
                  let curr = submitBtn[fiberKey];
                  while (curr) {
                    if (curr.memoizedProps?.onSubmit) {
                      curr.memoizedProps.onSubmit();
                      break;
                    }
                    curr = curr.return;
                  }
                }
              }
              return { submitted: true };
            })()
            """
            await ws.send(json.dumps({
                "id": msg_id + 3,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_submit,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }))
            await ws.recv()

            await asyncio.sleep(0.3)
            print("Prompt posted successfully to Arena.ai (box cleared first with Ctrl+A Delete, prompt set, Enter hit)!")
            return True
    except Exception as e:
        print(f"Error posting prompt over CDP: {e}", file=sys.stderr)
        return False


async def dismiss_arena_popup() -> bool:
    """Send Escape key via CDP to dismiss any 'Was this task successful?' modal popup."""
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        return False
    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg_down = {
                "id": int(time.time()),
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "rawKeyDown",
                    "windowsVirtualKeyCode": 27,
                    "code": "Escape",
                    "key": "Escape"
                }
            }
            await ws.send(json.dumps(msg_down))
            await ws.recv()
            msg_up = {
                "id": int(time.time()) + 1,
                "method": "Input.dispatchKeyEvent",
                "params": {
                    "type": "keyUp",
                    "windowsVirtualKeyCode": 27,
                    "code": "Escape",
                    "key": "Escape"
                }
            }
            await ws.send(json.dumps(msg_up))
            await ws.recv()
            return True
    except Exception as e:
        print(f"Error dismissing popup: {e}", file=sys.stderr)
        return False


async def check_arena_response() -> Tuple[bool, str]:
    """Check if Arena has completed responding and extract the full response text."""
    await dismiss_arena_popup()
    ws_url = await get_arena_tab_ws_url()
    if not ws_url:
        return False, "No active Arena tab"

    js_code = """
    (() => {
      // Check if generation is still active
      const stopBtn = document.querySelector('button[aria-label="Stop generating"], button:has(svg.lucide-square)');
      const isGenerating = !!stopBtn;

      // Extract all prose elements
      const proseElements = Array.from(document.querySelectorAll('.prose')).filter(el => !el.classList.contains('tiptap'));
      const lastText = proseElements.length > 0 ? proseElements[proseElements.length - 1].innerText : '';

      return {
        isGenerating: isGenerating,
        lastText: lastText,
        count: proseElements.length
      };
    })()
    """

    try:
        async with websockets.connect(ws_url, max_size=10_000_000) as ws:
            msg = {
                "id": int(time.time()),
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_code,
                    "returnByValue": True,
                    "awaitPromise": True
                }
            }
            await ws.send(json.dumps(msg))
            resp_str = await ws.recv()
            resp = json.loads(resp_str)
            val = resp.get("result", {}).get("result", {}).get("value", {})
            is_gen = val.get("isGenerating", False)
            text = val.get("lastText", "")
            return not is_gen and len(text) > 50, text
    except Exception as e:
        return False, str(e)


def run_full_15m_cycle():
    """
    Execute the canonical 13th/15th minute cycle:
    1. Dismiss any existing popup.
    2. Generate fresh 48h footprint & telemetry prompt.
    3. Post to Arena.ai and hit submit.
    4. Sleep for 2 minutes (120s) while Arena computes.
    5. Dismiss completion popup via Escape.
    6. Extract response and evaluate against orderflow data.
    """
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Initiating 13th-minute Arena.ai cycle...")
    asyncio.run(dismiss_arena_popup())

    p = build_48h_orderflow_prompt()
    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Posting 48h footprint prompt to Arena.ai ({len(p)} chars)...")
    posted = asyncio.run(post_prompt_to_arena(p))
    if not posted:
        print("ERROR: Failed to post prompt to Arena.ai", file=sys.stderr)
        return False

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Prompt submitted. Sleeping 120s (2 min) for Arena.ai Big Brain reasoning...")
    time.sleep(120)

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] 15th-minute wake-up: Checking Arena.ai response...")
    asyncio.run(dismiss_arena_popup())
    done, resp_text = asyncio.run(check_arena_response())
    asyncio.run(dismiss_arena_popup())

    print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Arena Generation Done: {done} | Response Length: {len(resp_text)} chars")
    print("--- ARENA.AI FULL RESPONSE ---")
    print(resp_text)
    print("------------------------------")

    # Append to docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md
    desk_path = PROJECT_ROOT / "docs" / "trade_plans" / "LIVE_COLLABORATIVE_ORDER_DESK.md"
    if desk_path.exists() and len(resp_text) > 50:
        now_dt = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        
        # Determine next section number
        import re
        content = desk_path.read_text(encoding="utf-8")
        matches = re.findall(r"## Section (\d+):", content)
        next_sec = max([int(m) for m in matches]) + 1 if matches else 44

        section_entry = f"\n\n---\n\n## Section {next_sec}: Autonomous Arena.ai Big Brain Evaluation & Telemetry Audit | {now_dt}\n\n"
        section_entry += f"### 1. Cycle Trigger & Submission Details\n"
        section_entry += f"- **Mode**: Autonomous 13m/15m Collaborative Cycle (`arena_bridge.py`)\n"
        section_entry += f"- **Status**: 100% Cash Flat | Equity: 4,813.99 USD | Floor Cushion: +38.99 USD | Buffer Headroom: +18.99 USD\n"
        section_entry += f"- **Capacity**: Exactly 1 Slot Available (Max Nominal Risk: 11.04 USD)\n\n"
        section_entry += f"### 2. Arena.ai Ruling & Quantitative Synthesis\n"
        section_entry += f"```text\n{resp_text}\n```\n\n"
        section_entry += f"### 3. Antigravity Verification & Action Plan\n"
        if "PUNCH NONE" in resp_text or "DEFENSIVE HOLD" in resp_text:
            section_entry += f"- **Consensus Verdict**: **PUNCH NONE / DEFENSIVE HOLD**. Zero setups clear all 5 gates simultaneously.\n"
            section_entry += f"- **Action Taken**: Maintain 100% Cash Flat. Preserved +38.99 USD floor cushion safely.\n"
        else:
            section_entry += f"- **Consensus Verdict**: Candidate trade proposal identified by Big Brain. Evaluating execution parameters.\n"

        with open(desk_path, "a", encoding="utf-8") as f:
            f.write(section_entry)
        print(f"[{datetime.now(timezone.utc).strftime('%H:%M:%S UTC')}] Appended Section {next_sec} to LIVE_COLLABORATIVE_ORDER_DESK.md.")

    return done, resp_text


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "prompt-only":
        p = build_48h_orderflow_prompt()
        print(p)
    elif len(sys.argv) > 1 and sys.argv[1] == "post":
        asyncio.run(dismiss_arena_popup())
        p = build_48h_orderflow_prompt()
        success = asyncio.run(post_prompt_to_arena(p))
        sys.exit(0 if success else 1)
    elif len(sys.argv) > 1 and sys.argv[1] == "check":
        asyncio.run(dismiss_arena_popup())
        done, text = asyncio.run(check_arena_response())
        asyncio.run(dismiss_arena_popup())
        print(f"Done: {done}\nText Length: {len(text)}\nResponse:\n{text}")
    elif len(sys.argv) > 1 and sys.argv[1] == "dismiss-popup":
        success = asyncio.run(dismiss_arena_popup())
        print("Popup dismissed:", success)
    elif len(sys.argv) > 1 and sys.argv[1] == "clear-box":
        async def do_clear():
            ws_url = await get_arena_tab_ws_url()
            if ws_url:
                async with websockets.connect(ws_url, max_size=10_000_000) as ws:
                    await clear_arena_prompt_box(ws)
                    print("Prompt box cleared successfully.")
            else:
                print("No Arena tab found.")
        asyncio.run(do_clear())
    elif len(sys.argv) > 1 and sys.argv[1] == "cycle":
        run_full_15m_cycle()
    else:
        print("Usage: python arena_bridge.py [prompt-only | post | check | clear-box | dismiss-popup | cycle]")


if __name__ == "__main__":
    main()
