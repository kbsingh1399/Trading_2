"""
Terminal/Candle_Indicator_Engine.py
===================================
Institutional Historical Candle Persistence, Gap-Detection & Indicator Engine.

Key Responsibilities:
1. Persists completed 15m OHLCV candles to Data/Candles/{ASSET}_15m.parquet.
2. Performs gap audits: detects missing candles, non-monotonic timestamps, and weekend/session halts.
3. Computes deterministic causal indicators:
   - True Daily Session VWAP (resets 00:00 UTC) with +/-1, +/-2, +/-3 SD bands and vwap_z.
   - Rolling 24h VWAP (96-bar window) with continuous volatility bands.
   - EMA 20, EMA 50, EMA 200 and 3-hour slope.
   - ATR(14) and Wilder RSI(14).
4. Mean-Reversion Scanner: Identifies extreme deviations (>= +2 SD or <= -2 SD from VWAP)
   for Gold, Silver, and Institutional Crypto Perpetuals.
"""
from __future__ import annotations

import argparse
import math
import pathlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Tuple

import numpy as np
import pandas as pd

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from Terminal.Asset_Universe import UNIVERSE, EXTENDED_UNIVERSE, canonical_asset
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge

CANDLE_DIR = ROOT / "Data" / "Candles"
CANDLE_DIR.mkdir(parents=True, exist_ok=True)


class CandleIndicatorEngine:
    def __init__(
        self,
        bridge: Optional[MT5ExecutionBridge] = None,
        storage_dir: pathlib.Path = CANDLE_DIR,
        universe: Tuple[str, ...] = UNIVERSE,
    ):
        self.bridge = bridge or MT5ExecutionBridge(5064568)
        self.storage_dir = pathlib.Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)
        self.universe = list(universe)
        self.cache: Dict[str, List[Dict[str, Any]]] = {}

    def sync_candles(self, asset: str, count: int = 512) -> Dict[str, Any]:
        """Fetch completed 15m bars from MT5, audit gaps, persist to disk."""
        asset = canonical_asset(asset)
        symbol = self.bridge.resolve_symbol(asset)
        if not symbol:
            return {"asset": asset, "success": False, "error": f"Symbol unresolved for {asset}"}

        bars = self.bridge.get_recent_bars(symbol, count=count)
        if not bars:
            return {"asset": asset, "success": False, "error": "No bars returned by broker"}

        # Sort chronologically by open time
        ordered = sorted(bars, key=lambda b: float(b.get("time", 0.0)))

        # Gap detection & sanity audit
        times = [float(b["time"]) for b in ordered]
        gaps: List[Dict[str, Any]] = []
        for i in range(1, len(times)):
            delta = times[i] - times[i - 1]
            if delta > 900.0:
                missing_bars = int(round((delta - 900.0) / 900.0))
                gaps.append({
                    "start_utc": datetime.fromtimestamp(times[i - 1], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "end_utc": datetime.fromtimestamp(times[i], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
                    "delta_seconds": int(delta),
                    "missing_bars": missing_bars,
                })

        # Save to disk as Parquet for durable historical cache
        df = pd.DataFrame(ordered)
        df["datetime_utc"] = pd.to_datetime(df["time"], unit="s", utc=True)
        parquet_file = self.storage_dir / f"{asset}_15m.parquet"
        df.to_parquet(parquet_file, index=False)

        self.cache[asset] = ordered
        indicators = self.compute_indicators(ordered)

        return {
            "asset": asset,
            "symbol": symbol,
            "success": True,
            "bar_count": len(ordered),
            "first_bar_utc": datetime.fromtimestamp(times[0], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "latest_bar_utc": datetime.fromtimestamp(times[-1], tz=timezone.utc).strftime("%Y-%m-%d %H:%M"),
            "latest_close": ordered[-1]["close"],
            "gap_count": len(gaps),
            "gaps": gaps[-5:],  # Last 5 gaps if any (e.g. weekend closures on Gold/Silver)
            "indicators": indicators,
        }

    def sync_all(self, count: int = 512, max_workers: int = 6) -> Dict[str, Dict[str, Any]]:
        """Sync all assets in the universe concurrently."""
        results: Dict[str, Dict[str, Any]] = {}
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_asset = {
                executor.submit(self.sync_candles, asset, count): asset for asset in self.universe
            }
            for future in future_to_asset:
                asset = future_to_asset[future]
                try:
                    results[asset] = future.result()
                except Exception as exc:
                    results[asset] = {"asset": asset, "success": False, "error": str(exc)}
        return results

    @staticmethod
    def compute_indicators(bars: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Compute Session VWAP, Rolling VWAP, EMAs, ATR, RSI from historical bars."""
        if len(bars) < 14:
            return {}

        closes = np.array([float(b["close"]) for b in bars])
        highs = np.array([float(b["high"]) for b in bars])
        lows = np.array([float(b["low"]) for b in bars])
        times = np.array([float(b["time"]) for b in bars])
        volumes = np.array([float(b.get("volume") or b.get("tick_volume") or 1.0) for b in bars])

        # Typical price
        tps = (highs + lows + closes) / 3.0
        last_price = closes[-1]
        now_ts = times[-1] + 900.0  # Close of latest bar

        # Clean volume resolution (prioritize real volume, fall back to tick volume)
        vols_list = []
        for b in bars:
            v = float(b.get("real_volume") or 0.0)
            if v <= 0.0:
                v = float(b.get("volume") or 0.0)
            if v <= 0.0:
                v = float(b.get("tick_volume") or 1.0)
            vols_list.append(max(v, 1.0))
        volumes = np.array(vols_list)

        # -------------------------------------------------------------
        # 1. Daily Session VWAP (Anchored to 00:00:00 UTC of latest bar)
        # -------------------------------------------------------------
        latest_dt = datetime.fromtimestamp(times[-1], tz=timezone.utc)
        session_start_ts = datetime(
            latest_dt.year, latest_dt.month, latest_dt.day, 0, 0, 0, tzinfo=timezone.utc
        ).timestamp()

        session_mask = times >= session_start_ts
        if np.sum(session_mask) >= 3:
            s_tps = tps[session_mask]
            s_vols = volumes[session_mask]
            s_cum_vol = np.sum(s_vols)
            s_vwap = np.sum(s_tps * s_vols) / max(s_cum_vol, 1e-9)
            s_var = np.sum(s_vols * ((s_tps - s_vwap) ** 2)) / max(s_cum_vol, 1e-9)
            s_sigma = math.sqrt(max(0.0, s_var))
            s_bars_count = int(np.sum(session_mask))
        else:
            # Fall back to rolling 96 bars if early in session (< 1h)
            s_vwap = None
            s_sigma = None
            s_bars_count = 0

        # -------------------------------------------------------------
        # 2. Rolling 24-Hour VWAP (96 bars lookback)
        # -------------------------------------------------------------
        r_window = min(len(bars), 96)
        r_tps = tps[-r_window:]
        r_vols = volumes[-r_window:]
        r_cum_vol = np.sum(r_vols)
        r_vwap = np.sum(r_tps * r_vols) / max(r_cum_vol, 1e-9)
        r_var = np.sum(r_vols * ((r_tps - r_vwap) ** 2)) / max(r_cum_vol, 1e-9)
        r_sigma = math.sqrt(max(0.0, r_var))

        # Primary VWAP selection: prefer Session VWAP if >= 8 bars, else Rolling
        primary_vwap = s_vwap if (s_vwap is not None and s_bars_count >= 8) else r_vwap
        primary_sigma = s_sigma if (s_sigma is not None and s_bars_count >= 8) else r_sigma

        vwap_z = (last_price - primary_vwap) / primary_sigma if primary_sigma > 1e-8 else 0.0

        upper_1 = primary_vwap + primary_sigma
        lower_1 = primary_vwap - primary_sigma
        upper_2 = primary_vwap + 2.0 * primary_sigma
        lower_2 = primary_vwap - 2.0 * primary_sigma
        upper_3 = primary_vwap + 3.0 * primary_sigma
        lower_3 = primary_vwap - 3.0 * primary_sigma

        # -------------------------------------------------------------
        # 3. Moving Averages (EMA 20, 50, 200)
        # -------------------------------------------------------------
        def calc_ema(arr: np.ndarray, period: int) -> float:
            alpha = 2.0 / (period + 1.0)
            ema = arr[0]
            for val in arr[1:]:
                ema = alpha * val + (1.0 - alpha) * ema
            return float(ema)

        ema_20 = calc_ema(closes, 20)
        ema_50 = calc_ema(closes, 50)
        ema_200 = calc_ema(closes, 200) if len(closes) >= 200 else calc_ema(closes, min(len(closes), 96))

        # EMA 200 slope over past 12 bars (3 hours)
        if len(closes) >= 212:
            ema_200_prev12 = calc_ema(closes[:-12], 200)
            ema_200_slope_pct = (ema_200 - ema_200_prev12) / ema_200_prev12 * 100.0
        else:
            ema_200_slope_pct = 0.0

        # -------------------------------------------------------------
        # 4. Wilder Average True Range (ATR 14)
        # -------------------------------------------------------------
        tr = [highs[0] - lows[0]]
        for i in range(1, len(bars)):
            tr.append(max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1])))
        if len(tr) >= 14:
            atr = float(np.mean(tr[:14]))
            for i in range(14, len(tr)):
                atr = (atr * 13.0 + tr[i]) / 14.0
            atr_14 = float(atr)
        else:
            atr_14 = float(np.mean(tr))

        # -------------------------------------------------------------
        # 5. Wilder RSI (14)
        # -------------------------------------------------------------
        diffs = np.diff(closes)
        gains = np.maximum(diffs, 0.0)
        losses = np.maximum(-diffs, 0.0)
        if len(gains) >= 14:
            avg_gain = float(np.mean(gains[:14]))
            avg_loss = float(np.mean(losses[:14]))
            for i in range(14, len(gains)):
                avg_gain = (avg_gain * 13.0 + gains[i]) / 14.0
                avg_loss = (avg_loss * 13.0 + losses[i]) / 14.0
            rs = avg_gain / max(avg_loss, 1e-12)
            rsi_14 = 100.0 - (100.0 / (1.0 + rs))
        else:
            rsi_14 = 50.0

        # -------------------------------------------------------------
        # 6. Swing Extremes (24h / 96 bars)
        # -------------------------------------------------------------
        h24 = float(np.max(highs[-96:]))
        l24 = float(np.min(lows[-96:]))

        return {
            "last_price": float(last_price),
            "session_vwap": float(s_vwap) if s_vwap else None,
            "session_sigma": float(s_sigma) if s_sigma else None,
            "session_bars": s_bars_count,
            "rolling_vwap_24h": float(r_vwap),
            "rolling_sigma_24h": float(r_sigma),
            "active_vwap": float(primary_vwap),
            "active_sigma": float(primary_sigma),
            "vwap_z": float(vwap_z),
            "upper_1sd": float(upper_1),
            "lower_1sd": float(lower_1),
            "upper_2sd": float(upper_2),
            "lower_2sd": float(lower_2),
            "upper_3sd": float(upper_3),
            "lower_3sd": float(lower_3),
            "ema_20": float(ema_20),
            "ema_50": float(ema_50),
            "ema_200": float(ema_200),
            "ema_200_slope_pct": float(ema_200_slope_pct),
            "atr_14": float(atr_14),
            "atr_pct": float(atr_14 / last_price * 100.0),
            "rsi_14": float(rsi_14),
            "high_24h": h24,
            "low_24h": l24,
        }

    def scan_vwap_opportunities(self, z_threshold: float = 1.75) -> List[Dict[str, Any]]:
        """Identify assets stretched beyond +/- 2 SD from VWAP."""
        if not self.cache:
            self.sync_all()

        opportunities = []
        for asset, bars in self.cache.items():
            if not bars:
                continue
            ind = self.compute_indicators(bars)
            if not ind or "vwap_z" not in ind:
                continue

            z = ind["vwap_z"]
            px = ind["last_price"]
            vwap = ind["active_vwap"]
            sigma = ind["active_sigma"]
            atr = ind["atr_14"]
            rsi = ind["rsi_14"]

            # Extreme Overbought (>= +1.75 SD, target mean reversion SHORT)
            if z >= z_threshold:
                dist_pct = (px - vwap) / vwap * 100.0
                opp = {
                    "asset": asset,
                    "direction": "SHORT",
                    "bias": "EXTREME_OVERBOUGHT",
                    "current_price": px,
                    "vwap": vwap,
                    "upper_2sd": ind["upper_2sd"],
                    "vwap_z": round(z, 2),
                    "dist_to_vwap_pct": round(dist_pct, 2),
                    "rsi_14": round(rsi, 1),
                    "atr_14": round(atr, 4),
                    "suggested_sl": round(px + 1.5 * atr, 4),
                    "suggested_tp": round(vwap, 4),
                    "potential_r": round((px - vwap) / (1.5 * atr), 2) if atr > 0 else 0.0,
                    "confluence": "Look for Ask Whale Walls + Long Squeeze Sweeps",
                }
                opportunities.append(opp)

            # Extreme Oversold (<= -1.75 SD, target mean reversion LONG)
            elif z <= -z_threshold:
                dist_pct = (vwap - px) / vwap * 100.0
                opp = {
                    "asset": asset,
                    "direction": "LONG",
                    "bias": "EXTREME_OVERSOLD",
                    "current_price": px,
                    "vwap": vwap,
                    "lower_2sd": ind["lower_2sd"],
                    "vwap_z": round(z, 2),
                    "dist_to_vwap_pct": round(dist_pct, 2),
                    "rsi_14": round(rsi, 1),
                    "atr_14": round(atr, 4),
                    "suggested_sl": round(px - 1.5 * atr, 4),
                    "suggested_tp": round(vwap, 4),
                    "potential_r": round((vwap - px) / (1.5 * atr), 2) if atr > 0 else 0.0,
                    "confluence": "Look for Bid Whale Walls + Short Squeeze Sweeps",
                }
                opportunities.append(opp)

        # Sort by absolute deviation magnitude
        opportunities.sort(key=lambda x: abs(x["vwap_z"]), reverse=True)
        return opportunities


def main():
    parser = argparse.ArgumentParser(description="Candle Persistence & Indicator Engine")
    parser.add_argument("--sync", action="store_true", help="Sync all candles from MT5")
    parser.add_argument("--scan", action="store_true", help="Scan for VWAP 2 SD opportunities")
    parser.add_argument("--extended", action="store_true", help="Scan full 24-asset extended universe")
    parser.add_argument("--asset", type=str, default=None, help="Inspect specific asset")
    args = parser.parse_args()

    active_uni = EXTENDED_UNIVERSE if args.extended else UNIVERSE
    engine = CandleIndicatorEngine(universe=active_uni)

    if args.asset:
        res = engine.sync_candles(args.asset)
        print(f"\n=== CANDLE AUDIT FOR {args.asset} ===")
        print(f"Symbol: {res.get('symbol')} | Bars: {res.get('bar_count')} | Latest Close: {res.get('latest_close')}")
        print(f"Range: {res.get('first_bar_utc')} -> {res.get('latest_bar_utc')} UTC")
        print(f"Gaps Detected: {res.get('gap_count')}")
        if res.get("gaps"):
            for g in res["gaps"]:
                print(f"  Gap: {g['start_utc']} to {g['end_utc']} ({g['missing_bars']} bars)")
        ind = res.get("indicators", {})
        print("\n--- INDICATORS ---")
        print(f"Price: {ind.get('last_price')} | VWAP: {ind.get('active_vwap'):.2f} (Z: {ind.get('vwap_z'):.2f} SD)")
        print(f"Bands: Lower 2 SD = {ind.get('lower_2sd'):.2f} | Upper 2 SD = {ind.get('upper_2sd'):.2f}")
        print(f"EMA 200: {ind.get('ema_200'):.2f} (Slope: {ind.get('ema_200_slope_pct'):.3f}%) | RSI: {ind.get('rsi_14'):.1f} | ATR: {ind.get('atr_14'):.2f}")
        return

    print("\n[SYNC] Fetching and auditing completed 15m candles across universe...")
    t0 = time.time()
    results = engine.sync_all()
    t1 = time.time()
    print(f"[OK] Synced {len(results)} assets in {(t1 - t0):.2f}s.\n")

    print(f"{'Asset':<8} {'Price':<10} {'VWAP':<10} {'VWAP Z':<8} {'Upper 2SD':<10} {'Lower 2SD':<10} {'RSI':<6} {'Bars':<6} {'Gaps':<5}")
    print("-" * 80)
    for asset, r in results.items():
        if not r.get("success"):
            print(f"{asset:<8} ERROR: {r.get('error')}")
            continue
        ind = r.get("indicators", {})
        px = ind.get("last_price", 0.0)
        vwap = ind.get("active_vwap", 0.0)
        z = ind.get("vwap_z", 0.0)
        u2 = ind.get("upper_2sd", 0.0)
        l2 = ind.get("lower_2sd", 0.0)
        rsi = ind.get("rsi_14", 50.0)
        bars = r.get("bar_count", 0)
        gaps = r.get("gap_count", 0)
        print(f"{asset:<8} {px:<10.2f} {vwap:<10.2f} {z:<8.2f} {u2:<10.2f} {l2:<10.2f} {rsi:<6.1f} {bars:<6} {gaps:<5}")

    print("\n[SCAN] Scanning for extreme VWAP extensions (|Z| >= 1.75 SD)...")
    opps = engine.scan_vwap_opportunities()
    if not opps:
        print("No assets currently stretched beyond +/- 1.75 SD from VWAP.")
    else:
        print(f"Found {len(opps)} extreme VWAP opportunities:\n")
        for op in opps:
            print(f"  * {op['asset']} {op['direction']} ({op['bias']}):")
            print(f"    Current: {op['current_price']} | VWAP: {op['vwap']:.2f} | Z-Score: {op['vwap_z']} SD")
            print(f"    Suggested SL: {op['suggested_sl']} | Suggested TP: {op['suggested_tp']} | R:R: +{op['potential_r']}R")
            print(f"    Notes: {op['confluence']}\n")


if __name__ == "__main__":
    main()
