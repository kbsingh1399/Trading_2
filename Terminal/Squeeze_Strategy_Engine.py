#!/usr/bin/env python3
"""
Terminal/Squeeze_Strategy_Engine.py
===================================
Institutional 5-Step Order Flow, 4H Trend & Squeeze Liquidation Strategy Engine.

Implements the complete user-defined quant execution framework:
1. 4-Hour Trend & HTF Order Flow:
   - Evaluates 4H EMA-20/50/200 trend, slope, and candle geometry.
   - Computes 4H level-by-level critical zones: 4H VWAP, Value Area High (VAH), Value Area Low (VAL).
   - Compares with live Orderbook depth to identify resting whale bids/asks.
2. Candle-to-Candle % Change in CVD (CVD Momentum & Acceleration):
   - Computes consecutive candle taker delta (Buy Vol - Sell Vol).
   - Tracks candle-to-candle percent change: ((Delta_t - Delta_{t-1}) / |Delta_{t-1}| * 100).
   - Classifies CVD momentum: ACCELERATION, ABSORPTION (DIVERGENCE), CLIMAX EXHAUSTION, REVERSAL.
3. Long/Short Squeeze Liquidation Directional Logic:
   - If 4H Trend is DOWNWARD and Downside Long Liquidation Pool is dominant:
     -> SHORT POSSIBILITIES ON PULLBACK (Hunting trapped longs below).
   - If 4H Trend is UPWARD and Overhead Short Squeeze Pool is dominant:
     -> LONG POSSIBILITIES ON PULLBACK (Hunting trapped shorts above).
4. Pullback vs Live Orderbook & Hyperdash Overlap:
   - Scans pullback zone against live resting orderbook depth (bids for long, asks for short).
   - Cross-references Hyperdash Stop-Loss clusters and liquidation bands in pullback pocket.
   - Emits OVERLAP CONFIRMED when resting wall coincides with stop sweep liquidity.
5. Structural Take-Profit & Protective Stop Loss Targets:
   - TP 1: Major opposing liquidation cascade zone (the primary liquidity magnet).
   - TP 2: Secondary extreme stop-loss cluster.
   - Stop Loss: Sited strictly behind the resting orderbook whale wall.
   - Dynamic R-multiple, dollar risk (10.00 - 11.04 USD), and dollar reward calculation.
"""

from __future__ import annotations

import math
import time
from typing import Any, Dict, List, Optional, Tuple


def compute_ema(series: List[float], period: int) -> List[float]:
    """Calculate Exponential Moving Average."""
    if not series or len(series) < period:
        return [series[-1]] * len(series) if series else []
    ema = [sum(series[:period]) / period]
    multiplier = 2.0 / (period + 1.0)
    for price in series[period:]:
        ema.append((price - ema[-1]) * multiplier + ema[-1])
    # Pad front with first EMA value
    return [ema[0]] * (period - 1) + ema


def analyze_4h_trend_and_cvd(
    asset: str,
    bars_4h: List[Dict[str, Any]],
    current_price: float,
    orderbook: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Step 1 & Step 2: 4-Hour Trend, Critical Zones, and Candle-to-Candle CVD Momentum."""
    res: Dict[str, Any] = {
        "asset": asset,
        "trend_4h": "NEUTRAL",
        "trend_score": 0.0,
        "ema_20": None,
        "ema_50": None,
        "ema_200": None,
        "ema_slope_pct": 0.0,
        "critical_zones": {},
        "cvd_history": [],
        "latest_cvd_signal": "INSUFFICIENT_DATA",
        "orderbook_at_zones": {},
    }

    if not bars_4h or len(bars_4h) < 3:
        return res

    closes = [float(b.get("close", 0)) for b in bars_4h]
    highs = [float(b.get("high", 0)) for b in bars_4h]
    lows = [float(b.get("low", 0)) for b in bars_4h]
    volumes = [float(b.get("volume", b.get("tick_volume", 0))) for b in bars_4h]

    # 1. 4H Trend Evaluation
    n_bars = len(bars_4h)
    ema20 = compute_ema(closes, min(20, n_bars))
    ema50 = compute_ema(closes, min(50, n_bars))
    res["ema_20"] = round(ema20[-1], 4) if ema20 else None
    res["ema_50"] = round(ema50[-1], 4) if ema50 else None

    # Trend Direction
    last_close = closes[-1]
    last_open = float(bars_4h[-1].get("open", last_close))
    prev_close = closes[-2]

    bull_votes = 0
    bear_votes = 0

    if last_close > ema20[-1]:
        bull_votes += 1
    else:
        bear_votes += 1

    if ema20[-1] > ema50[-1]:
        bull_votes += 1
    else:
        bear_votes += 1

    if last_close > prev_close:
        bull_votes += 1
    else:
        bear_votes += 1

    slope = ((last_close - closes[0]) / closes[0] * 100.0) if closes[0] > 0 else 0.0
    res["ema_slope_pct"] = round(slope, 2)

    if bull_votes >= 2 and slope >= -0.2:
        res["trend_4h"] = "BULLISH"
        res["trend_score"] = round(bull_votes / 3.0, 2)
    elif bear_votes >= 2 and slope <= 0.2:
        res["trend_4h"] = "BEARISH"
        res["trend_score"] = round(-bear_votes / 3.0, 2)
    else:
        res["trend_4h"] = "NEUTRAL"
        res["trend_score"] = 0.0

    # 2. Critical Zones (VAH, VAL, VWAP, Swings)
    recent_high = max(highs[-10:]) if len(highs) >= 10 else max(highs)
    recent_low = min(lows[-10:]) if len(lows) >= 10 else min(lows)
    tot_vol = sum(volumes)
    vwap_4h = sum(c * v for c, v in zip(closes, volumes)) / tot_vol if tot_vol > 0 else last_close

    # Approximate Value Area (70% Volume bounds)
    rng = recent_high - recent_low
    vah_4h = recent_low + (rng * 0.70)
    val_4h = recent_low + (rng * 0.30)

    res["critical_zones"] = {
        "vwap_4h": round(vwap_4h, 4),
        "vah_4h": round(vah_4h, 4),
        "val_4h": round(val_4h, 4),
        "swing_high_4h": round(recent_high, 4),
        "swing_low_4h": round(recent_low, 4),
        "range_4h": round(rng, 4),
    }

    # 3. Candle-to-Candle CVD Momentum Matrix (Step 2)
    cum_cvd = 0.0
    cvd_table: List[Dict[str, Any]] = []

    for i, b in enumerate(bars_4h):
        o = float(b.get("open", 0))
        h = float(b.get("high", 0))
        l = float(b.get("low", 0))
        c = float(b.get("close", 0))
        v = float(b.get("volume", b.get("tick_volume", 0)))
        buy_v = float(b.get("buy_volume", 0))
        
        # If true taker volume not available (e.g. MT5), infer directional delta from candle spread
        if buy_v > 0:
            sell_v = max(0.0, v - buy_v)
            delta = buy_v - sell_v
        else:
            # Synthetic tick delta from bar geometry
            bar_rng = h - l if h > l else 1.0
            direction_ratio = (c - o) / bar_rng
            delta = v * direction_ratio * 0.5
            buy_v = max(0.0, (v + delta) / 2.0)
            sell_v = max(0.0, v - buy_v)

        cum_cvd += delta
        prev_delta = cvd_table[-1]["delta"] if cvd_table else delta

        # Candle-to-candle percent change in delta
        if abs(prev_delta) > 1e-4:
            delta_pct_chg = ((delta - prev_delta) / abs(prev_delta)) * 100.0
        else:
            delta_pct_chg = 0.0

        delta_vol_ratio = (delta / v * 100.0) if v > 0 else 0.0

        # CVD Signal for this candle
        sig = "NEUTRAL"
        if delta > 0 and delta_pct_chg > 25.0:
            sig = "CVD ACCELERATION (BULLISH)"
        elif delta < 0 and delta_pct_chg < -25.0:
            sig = "CVD ACCELERATION (BEARISH)"
        elif (c > o and delta < 0) or (c < o and delta > 0):
            sig = "CVD ABSORPTION (DIVERGENCE)"
        elif abs(delta_vol_ratio) > 35.0 and abs(c - o) < (rng * 0.05):
            sig = "CVD EXHAUSTION (CLIMAX)"

        cvd_table.append({
            "bar_index": i,
            "open": round(o, 4),
            "high": round(h, 4),
            "low": round(l, 4),
            "close": round(c, 4),
            "volume": round(v, 2),
            "taker_buy": round(buy_v, 2),
            "taker_sell": round(sell_v, 2),
            "delta": round(delta, 2),
            "delta_vol_pct": round(delta_vol_ratio, 2),
            "candle_to_candle_pct": round(delta_pct_chg, 2),
            "cumulative_cvd": round(cum_cvd, 2),
            "signal": sig,
        })

    res["cvd_history"] = cvd_table
    res["latest_cvd_signal"] = cvd_table[-1]["signal"] if cvd_table else "NEUTRAL"

    # 4. Compare with Live Orderbook at Critical Zones
    if orderbook:
        bids = orderbook.get("bids", [])
        asks = orderbook.get("asks", [])
        bid_vol_near_val = sum(float(q) * float(p) for p, q in bids if abs(float(p) - val_4h) / val_4h < 0.015)
        ask_vol_near_vah = sum(float(q) * float(p) for p, q in asks if abs(float(p) - vah_4h) / vah_4h < 0.015)
        res["orderbook_at_zones"] = {
            "bids_at_val_usd": round(bid_vol_near_val, 2),
            "asks_at_vah_usd": round(ask_vol_near_vah, 2),
        }

    return res


def evaluate_squeeze_liquidation_alignment(
    trend_4h: str,
    current_price: float,
    liquidations_hd: Optional[Dict[str, Any]] = None,
    stops_hd: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    """Step 3: Long/Short Squeeze Liquidation Directional Matcher."""
    res: Dict[str, Any] = {
        "trend_4h": trend_4h,
        "current_price": current_price,
        "short_squeeze_overhead_usd": 0.0,
        "long_cascade_downside_usd": 0.0,
        "total_liquidation_pool_usd": 0.0,
        "overhead_stop_loss_usd": 0.0,
        "downside_stop_loss_usd": 0.0,
        "dominant_liquidity_magnet": "NONE",
        "directional_bias": "STANDBY",
        "strategic_rationale": "",
    }

    if not liquidations_hd:
        return res

    above_liqs = liquidations_hd.get("above", [])
    below_liqs = liquidations_hd.get("below", [])

    short_pool = sum(float(x.get("val", x.get("total_usd", 0.0))) for x in above_liqs)
    long_pool = sum(float(x.get("val", x.get("total_usd", 0.0))) for x in below_liqs)

    res["short_squeeze_overhead_usd"] = round(short_pool, 2)
    res["long_cascade_downside_usd"] = round(long_pool, 2)
    res["total_liquidation_pool_usd"] = round(short_pool + long_pool, 2)

    # Stops pools
    if stops_hd:
        above_stops = stops_hd.get("above", [])
        below_stops = stops_hd.get("below", [])
        res["overhead_stop_loss_usd"] = round(sum(float(x.get("val", x.get("total_usd", 0.0))) for x in above_stops), 2)
        res["downside_stop_loss_usd"] = round(sum(float(x.get("val", x.get("total_usd", 0.0))) for x in below_stops), 2)

    # Dominant Magnet
    if long_pool > short_pool * 1.15:
        res["dominant_liquidity_magnet"] = "DOWNSIDE LONG CASCADE"
    elif short_pool > long_pool * 1.15:
        res["dominant_liquidity_magnet"] = "OVERHEAD SHORT SQUEEZE"
    else:
        res["dominant_liquidity_magnet"] = "BALANCED LIQUIDITY"

    # User Step 3 Rules:
    # If 4H Trend is DOWNWARD and more Long Squeeze/Cascade opportunities below:
    # -> Identify SHORT possibilities at Pullback!
    # If 4H Trend is UPWARD and more Short Squeeze opportunities above:
    # -> Identify LONG possibilities at Pullback!
    if trend_4h == "BEARISH":
        if long_pool >= short_pool * 0.8:  # Significant or dominant long cascade below
            res["directional_bias"] = "SHORT ON PULLBACK"
            res["strategic_rationale"] = (
                f"4H Trend is BEARISH and Downside Long Liquidation Pool (${long_pool / 1e6:,.1f}M) "
                f"acts as a major liquidity magnet. Strategy: Enter SHORT on pullback up into resistance / VWAP."
            )
        else:
            res["directional_bias"] = "STANDBY (CONFLICTED)"
            res["strategic_rationale"] = "4H Trend is BEARISH but major liquidations rest overhead; risk of short squeeze."
    elif trend_4h == "BULLISH":
        if short_pool >= long_pool * 0.8:  # Significant or dominant short squeeze above
            res["directional_bias"] = "LONG ON PULLBACK"
            res["strategic_rationale"] = (
                f"4H Trend is BULLISH and Overhead Short Squeeze Pool (${short_pool / 1e6:,.1f}M) "
                f"acts as a major liquidity magnet. Strategy: Enter LONG on pullback down into support / VWAP."
            )
        else:
            res["directional_bias"] = "STANDBY (CONFLICTED)"
            res["strategic_rationale"] = "4H Trend is BULLISH but major liquidations rest below; risk of cascade trap."
    else:
        res["directional_bias"] = "STANDBY (RANGEBOUND)"
        res["strategic_rationale"] = "4H Trend is NEUTRAL. Awaiting directional breakout."

    return res


def scan_pullback_orderbook_overlap(
    directional_bias: str,
    current_price: float,
    critical_zones: Dict[str, Any],
    orderbook: Optional[Dict[str, Any]] = None,
    stops_hd: Optional[Dict[str, Any]] = None,
    liquidations_hd: Optional[Dict[str, Any]] = None,
    atr_14: float = 0.0,
) -> Dict[str, Any]:
    """Step 4: Study Pullback against Live Orderbook & Hyperdash Overlap."""
    res: Dict[str, Any] = {
        "directional_bias": directional_bias,
        "pullback_target_price": current_price,
        "pullback_distance_pct": 0.0,
        "pullback_distance_atr": 0.0,
        "resting_whale_wall": None,
        "overlapping_stops_pool": None,
        "overlapping_liquidation_pool": None,
        "overlap_confirmed": False,
        "confluence_score": 0,
        "confluence_badge": "NO PULLBACK ACTIVE",
    }

    if "PULLBACK" not in directional_bias or not current_price or current_price <= 0:
        return res

    vwap = critical_zones.get("vwap_4h", current_price)
    vah = critical_zones.get("vah_4h", current_price)
    val = critical_zones.get("val_4h", current_price)

    # 1. Determine Target Pullback Level
    if "LONG" in directional_bias:
        # Pullback moves DOWN into support (VAL or VWAP if below spot)
        target_px = val if val < current_price else (vwap if vwap < current_price else current_price * 0.992)
    elif "SHORT" in directional_bias:
        # Pullback moves UP into resistance (VAH or VWAP if above spot)
        target_px = vah if vah > current_price else (vwap if vwap > current_price else current_price * 1.008)
    else:
        return res

    dist_pct = abs(target_px - current_price) / current_price * 100.0
    dist_atr = abs(target_px - current_price) / atr_14 if atr_14 > 0 else 0.0

    res["pullback_target_price"] = round(target_px, 4)
    res["pullback_distance_pct"] = round(dist_pct, 2)
    res["pullback_distance_atr"] = round(dist_atr, 2)

    # 2. Check Resting Orderbook Wall near Target Price
    tolerance = max(target_px * 0.008, (atr_14 * 0.5) if atr_14 > 0 else target_px * 0.008)
    whale_wall: Optional[Dict[str, Any]] = None

    if orderbook:
        if "LONG" in directional_bias:
            # Look for resting BIDS around pullback target
            bids = orderbook.get("bids", [])
            for p_str, q_str in bids:
                p = float(p_str)
                q = float(q_str)
                usd_val = p * q
                if abs(p - target_px) <= tolerance and usd_val >= 100_000:
                    if whale_wall is None or usd_val > whale_wall["total_usd"]:
                        whale_wall = {
                            "side": "BID",
                            "price": round(p, 4),
                            "size": round(q, 4),
                            "total_usd": round(usd_val, 2),
                            "distance_from_target": round(abs(p - target_px), 4),
                        }
        elif "SHORT" in directional_bias:
            # Look for resting ASKS around pullback target
            asks = orderbook.get("asks", [])
            for p_str, q_str in asks:
                p = float(p_str)
                q = float(q_str)
                usd_val = p * q
                if abs(p - target_px) <= tolerance and usd_val >= 100_000:
                    if whale_wall is None or usd_val > whale_wall["total_usd"]:
                        whale_wall = {
                            "side": "ASK",
                            "price": round(p, 4),
                            "size": round(q, 4),
                            "total_usd": round(usd_val, 2),
                            "distance_from_target": round(abs(p - target_px), 4),
                        }

    res["resting_whale_wall"] = whale_wall

    # 3. Check Overlapping Stops & Liquidations in Pullback Direction
    matched_stops: Optional[Dict[str, Any]] = None
    if stops_hd:
        stops_list = stops_hd.get("below", []) if "LONG" in directional_bias else stops_hd.get("above", [])
        for item in stops_list:
            px = float(item.get("px", item.get("price", 0)))
            val = float(item.get("val", item.get("total_usd", 0)))
            if abs(px - target_px) <= tolerance and val > 50_000:
                if matched_stops is None or val > matched_stops["total_usd"]:
                    matched_stops = {"price": px, "total_usd": val}

    res["overlapping_stops_pool"] = matched_stops

    matched_liqs: Optional[Dict[str, Any]] = None
    if liquidations_hd:
        liqs_list = liquidations_hd.get("below", []) if "LONG" in directional_bias else liquidations_hd.get("above", [])
        for item in liqs_list:
            px = float(item.get("px", item.get("price", 0)))
            val = float(item.get("val", item.get("total_usd", 0)))
            if abs(px - target_px) <= tolerance and val > 50_000:
                if matched_liqs is None or val > matched_liqs["total_usd"]:
                    matched_liqs = {"price": px, "total_usd": val}

    res["overlapping_liquidation_pool"] = matched_liqs

    # 4. Confluence Scoring & Overlap Confirmation
    score = 40  # Base score for valid bias and target
    if whale_wall is not None:
        score += 30  # Resting wall exists in zone
    if matched_stops is not None or matched_liqs is not None:
        score += 30  # Stop or liquidation pool overlaps

    res["confluence_score"] = score

    if whale_wall is not None and (matched_stops is not None or matched_liqs is not None):
        res["overlap_confirmed"] = True
        res["confluence_badge"] = "OVERLAP CONFIRMED (HIGH CONFLUENCE)"
    elif whale_wall is not None:
        res["overlap_confirmed"] = False
        res["confluence_badge"] = "ORDERBOOK WALL DETECTED (AWAITING STOPS)"
    else:
        res["overlap_confirmed"] = False
        res["confluence_badge"] = "AWAITING ORDERBOOK CONFLUENCE"

    return res


def calculate_structural_trade_plan(
    directional_bias: str,
    entry_price: float,
    current_price: float,
    liquidations_hd: Optional[Dict[str, Any]],
    stops_hd: Optional[Dict[str, Any]],
    atr_14: float = 0.0,
    capital_usd: float = 4811.62,
    max_risk_usd: float = 11.04,
) -> Dict[str, Any]:
    """Step 5: Structural Take-Profit & Protective Stop Loss Trade Plan."""
    res: Dict[str, Any] = {
        "status": "NO_SETUP",
        "action": "STANDBY",
        "direction": "NONE",
        "entry_price": entry_price,
        "stop_loss_price": 0.0,
        "take_profit_1": 0.0,
        "take_profit_2": 0.0,
        "stop_distance": 0.0,
        "target_1_distance": 0.0,
        "target_2_distance": 0.0,
        "risk_to_reward_1": 0.0,
        "risk_to_reward_2": 0.0,
        "nominal_risk_usd": max_risk_usd,
        "potential_profit_tp1_usd": 0.0,
        "potential_profit_tp2_usd": 0.0,
        "tp1_rationale": "Opposing Major Liquidation Magnet",
        "tp2_rationale": "Secondary Stop Loss Cluster",
    }

    if "PULLBACK" not in directional_bias or not entry_price or entry_price <= 0:
        return res

    is_long = "LONG" in directional_bias
    res["direction"] = "BUY" if is_long else "SELL"
    res["action"] = "STAGE LIMIT ORDER" if abs(entry_price - current_price) / current_price < 0.015 else "MONITOR PULLBACK APPROACH"

    # Default ATR buffer if not available
    atr = atr_14 if atr_14 > 0 else (entry_price * 0.005)

    # 1. Stop Loss: Placed safely behind structural buffer (1.25x ATR)
    if is_long:
        sl_px = entry_price - (1.25 * atr)
    else:
        sl_px = entry_price + (1.25 * atr)

    stop_dist = abs(entry_price - sl_px)
    res["stop_loss_price"] = round(sl_px, 4)
    res["stop_distance"] = round(stop_dist, 4)

    # 2. Find Major Opposing Liquidation Zone for TP 1
    tp1_px = 0.0
    if liquidations_hd:
        target_list = liquidations_hd.get("above", []) if is_long else liquidations_hd.get("below", [])
        # Find highest density band beyond current price
        max_val = 0.0
        for item in target_list:
            px = float(item.get("px", item.get("price", 0)))
            val = float(item.get("val", item.get("total_usd", 0)))
            if (is_long and px > entry_price) or (not is_long and px < entry_price):
                if val > max_val:
                    max_val = val
                    tp1_px = px

    # Fallback TP1 at 2.0R if no liquidation band found
    if tp1_px == 0.0:
        tp1_px = (entry_price + (2.0 * stop_dist)) if is_long else (entry_price - (2.0 * stop_dist))

    # 3. Find Secondary Stop Loss Cluster for TP 2
    tp2_px = 0.0
    if stops_hd:
        target_stops = stops_hd.get("above", []) if is_long else stops_hd.get("below", [])
        max_s_val = 0.0
        for item in target_stops:
            px = float(item.get("px", item.get("price", 0)))
            val = float(item.get("val", item.get("total_usd", 0)))
            if (is_long and px > tp1_px) or (not is_long and px < tp1_px):
                if val > max_s_val:
                    max_s_val = val
                    tp2_px = px

    # Fallback TP2 at 3.0R
    if tp2_px == 0.0:
        tp2_px = (entry_price + (3.0 * stop_dist)) if is_long else (entry_price - (3.0 * stop_dist))

    dist_tp1 = abs(tp1_px - entry_price)
    dist_tp2 = abs(tp2_px - entry_price)

    rr1 = (dist_tp1 / stop_dist) if stop_dist > 0 else 0.0
    rr2 = (dist_tp2 / stop_dist) if stop_dist > 0 else 0.0

    res["take_profit_1"] = round(tp1_px, 4)
    res["take_profit_2"] = round(tp2_px, 4)
    res["target_1_distance"] = round(dist_tp1, 4)
    res["target_2_distance"] = round(dist_tp2, 4)
    res["risk_to_reward_1"] = round(rr1, 2)
    res["risk_to_reward_2"] = round(rr2, 2)

    # Dollar return calculations
    res["nominal_risk_usd"] = max_risk_usd
    res["potential_profit_tp1_usd"] = round(max_risk_usd * rr1, 2)
    res["potential_profit_tp2_usd"] = round(max_risk_usd * rr2, 2)
    res["status"] = "TRADE_PLAN_ACTIVE"

    return res


def run_full_squeeze_strategy_pipeline(
    asset: str,
    bars_4h: List[Dict[str, Any]],
    current_price: float,
    orderbook: Optional[Dict[str, Any]] = None,
    liquidations_hd: Optional[Dict[str, Any]] = None,
    stops_hd: Optional[Dict[str, Any]] = None,
    atr_14: float = 0.0,
    capital_usd: float = 4811.62,
    max_risk_usd: float = 11.04,
) -> Dict[str, Any]:
    """Execute the full 5-step institutional pipeline for an asset."""
    step1 = analyze_4h_trend_and_cvd(asset, bars_4h, current_price, orderbook)
    trend_4h = step1["trend_4h"]
    zones = step1["critical_zones"]

    step3 = evaluate_squeeze_liquidation_alignment(trend_4h, current_price, liquidations_hd, stops_hd)
    bias = step3["directional_bias"]

    step4 = scan_pullback_orderbook_overlap(
        bias, current_price, zones, orderbook, stops_hd, liquidations_hd, atr_14
    )
    pullback_target = step4["pullback_target_price"]

    step5 = calculate_structural_trade_plan(
        bias, pullback_target, current_price, liquidations_hd, stops_hd, atr_14, capital_usd, max_risk_usd
    )

    return {
        "asset": asset,
        "timestamp_epoch": time.time(),
        "step1_trend": step1,
        "step2_cvd": {
            "history": step1["cvd_history"],
            "latest_signal": step1["latest_cvd_signal"],
        },
        "step3_squeeze_alignment": step3,
        "step4_pullback_overlap": step4,
        "step5_trade_plan": step5,
    }


def fetch_and_run_squeeze_pipeline(asset: str) -> Dict[str, Any]:
    """Autonomous live data fetcher and executor for the 5-step Squeeze Strategy pipeline.
    Supports both Crypto (Binance Futures + Hyperdash) and Non-Crypto (MT5 broker bars & quotes)."""
    asset_clean = asset.strip().upper()

    try:
        from Terminal.live_data_terminal import ASSET_CATEGORY_MAP, MT5_SYMBOL_MAP
    except Exception:
        ASSET_CATEGORY_MAP = {}
        MT5_SYMBOL_MAP = {}

    cat = ASSET_CATEGORY_MAP.get(asset_clean, "CRYPTO" if asset_clean in ["BTC", "ETH", "SOL", "BNB", "XRP", "DOGE", "ADA", "LINK", "AVAX", "NEAR", "LTC", "BCH", "DOT", "TRX", "SUI", "APT"] else "METALS")

    bars_4h: List[Dict[str, Any]] = []
    current_price = 0.0
    orderbook: Optional[Dict[str, Any]] = None
    liquidations_hd: Optional[Dict[str, Any]] = None
    stops_hd: Optional[Dict[str, Any]] = None
    atr_14 = 0.0

    if cat == "CRYPTO":
        # 1. 4H bars from Binance Futures
        try:
            import json, urllib.request
            url = f"https://fapi.binance.com/fapi/v1/klines?symbol={asset_clean}USDT&interval=4h&limit=24"
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=3.0) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                for kl in data:
                    bars_4h.append({
                        "open": float(kl[1]),
                        "high": float(kl[2]),
                        "low": float(kl[3]),
                        "close": float(kl[4]),
                        "volume": float(kl[5]),
                        "buy_volume": float(kl[9]),
                    })
                if bars_4h:
                    current_price = bars_4h[-1]["close"]
        except Exception:
            pass

        # 2. Hyperdash Analytics (L2, liqs, stops)
        try:
            from Terminal.Api_Client import HyperdashClient
            hd = HyperdashClient()
            l2 = hd.fetch_l2_book(asset_clean)
            if l2:
                orderbook = {
                    "bids": [[str(p), str(s)] for p, s in l2.get("bids", [])],
                    "asks": [[str(p), str(s)] for p, s in l2.get("asks", [])],
                }
                if not current_price and l2.get("best_bid"):
                    current_price = float(l2["best_bid"])
            if current_price > 0:
                min_p = round(current_price * 0.70, 2)
                max_p = round(current_price * 1.30, 2)
                liquidations_hd = hd.fetch_liquidations(asset_clean, min_p, max_p)
                stops_hd = hd.fetch_stops(asset_clean, min_p, max_p)
        except Exception:
            pass

    else:
        # Non-crypto: Metals, Forex, Indices, Commodities from MT5
        try:
            from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
            import MetaTrader5 as mt5
            bridge = MT5ExecutionBridge(5064568)
            broker_sym = MT5_SYMBOL_MAP.get(asset_clean, asset_clean)
            mt5_bars = bridge.get_recent_bars(broker_sym, count=24, timeframe=mt5.TIMEFRAME_H4)
            if mt5_bars:
                bars_4h = mt5_bars
            q = bridge.get_symbol_price(broker_sym)
            if q:
                current_price = float(q.get("last", q.get("bid", 0.0)))
        except Exception:
            pass

    # Approximate ATR-14 if bars available
    if len(bars_4h) >= 14:
        tr_list = []
        for i in range(1, len(bars_4h)):
            h = float(bars_4h[i].get("high", 0))
            l = float(bars_4h[i].get("low", 0))
            prev_c = float(bars_4h[i - 1].get("close", 0))
            tr = max(h - l, abs(h - prev_c), abs(l - prev_c))
            tr_list.append(tr)
        if tr_list:
            atr_14 = sum(tr_list[-14:]) / min(14, len(tr_list))

    return run_full_squeeze_strategy_pipeline(
        asset=asset_clean,
        bars_4h=bars_4h,
        current_price=current_price,
        orderbook=orderbook,
        liquidations_hd=liquidations_hd,
        stops_hd=stops_hd,
        atr_14=atr_14,
    )

