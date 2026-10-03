"""
Terminal/Dump_History.py
========================
Full historical data dump for a given coin + timeframe.

Downloads and fuses:
  • OHLCV candles (Hyperliquid REST — all available history, typically ~52 days of 15m)
  • Liquidation band landscape per candle (Hyperdash GraphQL, hourly snapshots, 7d)
  • Stop-loss band landscape per candle (Hyperdash GraphQL, hourly snapshots, 7d)
  • Funding rate history (Hyperliquid REST, configurable days)

Output: single Parquet file at Data/Hyperdash_Historical/{COIN}_{TF}_full_dump.parquet

Usage:
    python Terminal/Dump_History.py --coin BTC --tf 15m
    python Terminal/Dump_History.py --coin BTC --tf 15m --liq-days 7 --funding-days 90
"""

import sys
import os
import time
import datetime
import bisect
import argparse
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

import polars as pl
from Terminal.Api_Client import HyperdashClient

# ── Config ─────────────────────────────────────────────────────────────────
OUTPUT_DIR   = pathlib.Path("Data/Hyperdash_Historical")
RATE_PAUSE   = 2.5   # seconds between GraphQL calls (Cloudflare 429 guard)
MAX_RETRIES  = 4
RETRY_WAIT   = 30    # seconds to wait after a 429

client = HyperdashClient(timeout=25)


def _ts_to_dt(epoch_sec: float) -> str:
    return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(epoch_sec))


def _retry_call(fn, *args, **kwargs):
    """Call fn with exponential back-off on 429."""
    for attempt in range(MAX_RETRIES):
        try:
            return fn(*args, **kwargs)
        except RuntimeError as e:
            if "429" in str(e) and attempt < MAX_RETRIES - 1:
                wait = RETRY_WAIT * (2 ** attempt)
                print(f"  ⚠  Rate-limited (429). Waiting {wait}s before retry {attempt+2}/{MAX_RETRIES}…")
                time.sleep(wait)
            else:
                raise


# ── Step 1: Download all available OHLCV candles ──────────────────────────
def fetch_all_candles(coin: str, interval: str) -> list[dict]:
    """
    Paginate backward from now to collect all available 15m candles.
    Hyperliquid caps each batch at ~5000 candles; we iterate until empty.
    """
    print(f"\n{'='*60}")
    print(f"STEP 1 — Downloading {coin} {interval} OHLCV candles")
    print(f"{'='*60}")

    import json, urllib.request
    HL_INFO = "https://api.hyperliquid.xyz/info"
    HEADERS = {"Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    all_raw = []
    now_ms  = int(time.time() * 1000)
    curr_end = now_ms
    page = 0

    while True:
        start_ms = curr_end - (90 * 24 * 3600 * 1000)  # 90d window per call
        payload  = {
            "type": "candleSnapshot",
            "req": {"coin": coin, "interval": interval,
                    "startTime": start_ms, "endTime": curr_end}
        }
        body = json.dumps(payload).encode()
        req  = urllib.request.Request(HL_INFO, data=body, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=15) as r:
                batch = json.loads(r.read())
        except Exception as e:
            print(f"  Page {page}: FETCH ERROR: {e}")
            break

        if not batch:
            print(f"  Page {page}: empty → reached genesis, stopping")
            break

        # Only keep timestamps strictly before curr_end to avoid overlap
        new = [c for c in batch if c["t"] < curr_end]
        if not new:
            break

        first_dt = datetime.datetime.fromtimestamp(min(c["t"] for c in new) / 1000,
                                                    datetime.timezone.utc)
        last_dt  = datetime.datetime.fromtimestamp(max(c["t"] for c in new) / 1000,
                                                    datetime.timezone.utc)
        print(f"  Page {page}: {len(new):5d} candles │ {first_dt.strftime('%Y-%m-%d')} → {last_dt.strftime('%Y-%m-%d')}")
        all_raw.extend(new)

        curr_end = min(c["t"] for c in new)  # move window back
        page += 1

        if len(batch) < 200:
            print(f"  Page {page-1}: small batch ({len(batch)}) → reached genesis")
            break
        time.sleep(0.15)

    # Deduplicate and format
    seen, candles = set(), []
    for c in all_raw:
        if c["t"] not in seen:
            seen.add(c["t"])
            candles.append({
                "timestamp": c["t"],
                "datetime":  _ts_to_dt(c["t"] / 1000),
                "open":      float(c["o"]),
                "high":      float(c["h"]),
                "low":       float(c["l"]),
                "close":     float(c["c"]),
                "volume":    float(c["v"]),
                "trades":    int(c.get("n", 0)),
            })

    candles.sort(key=lambda x: x["timestamp"])
    print(f"\n  ✅ {len(candles)} unique {interval} candles")
    if candles:
        t0 = candles[0]["datetime"]
        t1 = candles[-1]["datetime"]
        print(f"     Range: {t0} → {t1}")
    return candles


# ── Step 2: Fetch liquidation + stop landscape ─────────────────────────────
def fetch_liq_stop_snapshots(coin: str, candles: list[dict], lookback_days: int = 7):
    """
    Fetch GraphQL liquidation + stop band landscapes.
    Returns (liq_snapshots, stop_snapshots) as dict[datetime_str → list[band]]
    where each band has {min_px, max_px, mid_px, amount}.
    GraphQL data is hourly; we later carry-forward to fill 15m gaps.
    """
    print(f"\n{'='*60}")
    print(f"STEP 2 — Fetching liquidation + stop landscapes ({lookback_days}d lookback)")
    print(f"{'='*60}")

    if not candles:
        return {}, {}

    # Use median close price as reference for the price range
    closes  = sorted(c["close"] for c in candles)
    mid_px  = closes[len(closes)//2]
    min_px  = mid_px * 0.65   # ±35% wide band to capture all levels
    max_px  = mid_px * 1.35
    print(f"  Price range: ${min_px:,.0f} → ${max_px:,.0f} (mid: ${mid_px:,.0f})")

    liq_snap, stop_snap = {}, {}

    # Liquidations
    print(f"  Fetching liquidation bands…")
    try:
        liq_data = _retry_call(client.fetch_liquidations, coin, min_px, max_px,
                               lookback_days=lookback_days)
        liq_snap = liq_data.get("candle_snapshots", {})
        print(f"  ✅ Liq snapshots: {len(liq_snap)} hourly timestamps | "
              f"{len(liq_data.get('bands', []))} price bands")
    except Exception as e:
        print(f"  ⚠  Liq fetch failed: {e}")

    time.sleep(RATE_PAUSE)

    # Stops
    print(f"  Fetching stop-loss bands…")
    try:
        stop_data = _retry_call(client.fetch_stops, coin, min_px, max_px,
                                lookback_days=lookback_days)
        stop_snap = stop_data.get("candle_snapshots", {})
        print(f"  ✅ Stop snapshots: {len(stop_snap)} hourly timestamps | "
              f"{len(stop_data.get('bands', []))} price bands")
    except Exception as e:
        print(f"  ⚠  Stop fetch failed: {e}")

    return liq_snap, stop_snap


# ── Step 3: Fetch funding rate history ─────────────────────────────────────
def fetch_funding_history(coin: str, days: int = 90) -> dict:
    """Returns dict[datetime_str → funding_rate] for the given lookback."""
    print(f"\n{'='*60}")
    print(f"STEP 3 — Fetching funding rate history ({days}d)")
    print(f"{'='*60}")

    import json, urllib.request
    HL_INFO = "https://api.hyperliquid.xyz/info"
    HEADERS = {"Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    now_ms = int(time.time() * 1000)
    start_ms = now_ms - (days * 24 * 3600 * 1000)
    payload  = {"type": "fundingHistory", "coin": coin, "startTime": start_ms}

    try:
        body = json.dumps(payload).encode()
        req  = urllib.request.Request(HL_INFO, data=body, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as r:
            records = json.loads(r.read())
    except Exception as e:
        print(f"  ⚠  Funding fetch failed: {e}")
        return {}

    result = {}
    for rec in (records or []):
        dt_str = _ts_to_dt(rec["time"] / 1000)
        result[dt_str] = float(rec.get("fundingRate", 0.0))

    print(f"  ✅ {len(result)} funding rate entries")
    return result


# ── Step 4: Fuse everything at each candle ─────────────────────────────────
def _carry_forward(dt_str: str, snap: dict, sorted_keys: list) -> list:
    """Return exact match or most-recent preceding entry (carry-forward)."""
    exact = snap.get(dt_str)
    if exact is not None:
        return exact
    idx = bisect.bisect_right(sorted_keys, dt_str) - 1
    if idx >= 0:
        return snap[sorted_keys[idx]]
    if sorted_keys:
        return snap[sorted_keys[0]]
    return []


def fuse_candles(candles, liq_snap, stop_snap, funding_hist) -> pl.DataFrame:
    print(f"\n{'='*60}")
    print(f"STEP 4 — Fusing {len(candles)} candles with liq / stop / funding data")
    print(f"{'='*60}")

    liq_keys  = sorted(liq_snap.keys())
    stop_keys = sorted(stop_snap.keys())
    fund_keys = sorted(funding_hist.keys())

    records = []
    for c in candles:
        dt  = c["datetime"]
        px  = c["close"]

        # ── Liquidation aggregates ─────────────────────────────────────────
        liq_levels  = _carry_forward(dt, liq_snap, liq_keys)
        long_liq    = 0.0
        short_liq   = 0.0
        peak_liq_px = 0.0
        peak_liq_am = 0.0
        total_liq   = 0.0
        liq_bands_n = len(liq_levels)

        for lvl in liq_levels:
            amt    = abs(float(lvl.get("amount", 0.0)))
            mid    = float(lvl.get("mid_px", 0.0))
            total_liq += amt
            if mid < px:
                long_liq += amt
            else:
                short_liq += amt
            if amt > peak_liq_am:
                peak_liq_am = amt
                peak_liq_px = mid

        # ── Stop-loss aggregates ───────────────────────────────────────────
        stop_levels  = _carry_forward(dt, stop_snap, stop_keys)
        buy_stops    = 0.0
        sell_stops   = 0.0
        peak_stop_px = 0.0
        peak_stop_am = 0.0
        total_stops  = 0.0
        stop_bands_n = len(stop_levels)

        for lvl in stop_levels:
            amt    = abs(float(lvl.get("amount", 0.0)))
            mid    = float(lvl.get("mid_px", 0.0))
            total_stops += amt
            if mid > px:
                buy_stops += amt
            else:
                sell_stops += amt
            if amt > peak_stop_am:
                peak_stop_am = amt
                peak_stop_px = mid

        # ── Funding rate (nearest preceding) ──────────────────────────────
        fund_rate = 0.0
        fund_idx  = bisect.bisect_right(fund_keys, dt) - 1
        if fund_idx >= 0:
            fund_rate = funding_hist[fund_keys[fund_idx]]

        # ── Combined liq/stop cascade signal ──────────────────────────────
        # Imbalance: positive = more long-side pressure, negative = short-side
        cascade_imbalance = (long_liq - short_liq) / (total_liq + 1.0)
        stop_imbalance    = (buy_stops - sell_stops) / (total_stops + 1.0)

        records.append({
            # Core OHLCV
            "timestamp":          c["timestamp"],
            "datetime":           dt,
            "open":               c["open"],
            "high":               c["high"],
            "low":                c["low"],
            "close":              c["close"],
            "volume":             c["volume"],
            "trades":             c["trades"],
            # Liquidation microstructure
            "liq_total_usd":      total_liq,
            "liq_long_usd":       long_liq,
            "liq_short_usd":      short_liq,
            "liq_peak_price":     peak_liq_px,
            "liq_peak_amount":    peak_liq_am,
            "liq_bands_count":    liq_bands_n,
            "liq_cascade_imbal":  cascade_imbalance,
            # Stop-loss microstructure
            "stop_total_usd":     total_stops,
            "stop_buy_usd":       buy_stops,
            "stop_sell_usd":      sell_stops,
            "stop_peak_price":    peak_stop_px,
            "stop_peak_amount":   peak_stop_am,
            "stop_bands_count":   stop_bands_n,
            "stop_imbalance":     stop_imbalance,
            # Funding
            "funding_rate":       fund_rate,
        })

    df = pl.DataFrame(records).sort("timestamp")

    # ── Quick coverage stats ───────────────────────────────────────────────
    n_liq_filled  = df.filter(pl.col("liq_bands_count") > 0).height
    n_stop_filled = df.filter(pl.col("stop_bands_count") > 0).height
    n_fund_filled = df.filter(pl.col("funding_rate") != 0.0).height

    print(f"  Liq data coverage:  {n_liq_filled}/{len(records)} candles "
          f"({n_liq_filled/len(records)*100:.1f}%)")
    print(f"  Stop data coverage: {n_stop_filled}/{len(records)} candles "
          f"({n_stop_filled/len(records)*100:.1f}%)")
    print(f"  Funding coverage:   {n_fund_filled}/{len(records)} candles "
          f"({n_fund_filled/len(records)*100:.1f}%)")
    return df


# ── Main entry point ────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Dump full historical data for a coin/timeframe.")
    parser.add_argument("--coin",         default="BTC",  help="Coin symbol (default: BTC)")
    parser.add_argument("--tf",           default="15m",  help="Timeframe (default: 15m)")
    parser.add_argument("--liq-days",     type=int, default=7,  help="Lookback days for liq/stops GraphQL (max ~7)")
    parser.add_argument("--funding-days", type=int, default=90, help="Funding rate lookback days")
    args = parser.parse_args()

    coin = args.coin.upper()
    tf   = args.tf

    start_wall = time.time()
    print(f"\n{'█'*60}")
    print(f"  HYPERDASH HISTORICAL FULL DUMP")
    print(f"  Asset: {coin} | Timeframe: {tf}")
    print(f"  Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'█'*60}")

    # 1. Candles
    candles = fetch_all_candles(coin, tf)
    if not candles:
        print("ERROR: No candles. Aborting.")
        sys.exit(1)

    # 2. Liq + Stop snapshots
    liq_snap, stop_snap = fetch_liq_stop_snapshots(coin, candles, lookback_days=args.liq_days)

    # 3. Funding
    funding_hist = fetch_funding_history(coin, days=args.funding_days)

    # 4. Fuse
    df = fuse_candles(candles, liq_snap, stop_snap, funding_hist)

    # 5. Save
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_file = OUTPUT_DIR / f"{coin}_{tf}_full_dump.parquet"
    df.write_parquet(out_file)

    elapsed = time.time() - start_wall
    size_kb  = out_file.stat().st_size / 1024

    print(f"\n{'='*60}")
    print(f"  ✅  DUMP COMPLETE")
    print(f"{'='*60}")
    print(f"  File:    {out_file}")
    print(f"  Rows:    {len(df):,} candles")
    print(f"  Columns: {len(df.columns)}")
    print(f"  Size:    {size_kb:.1f} KB")
    print(f"  Time:    {elapsed:.1f}s")
    print()
    print("  Columns written:")
    for col in df.columns:
        print(f"    • {col}")

    print(f"\n  First 3 rows:")
    print(df.head(3))
    print(f"\n  Last 3 rows:")
    print(df.tail(3))

    # Cleanup scratch probe
    try:
        pathlib.Path("scratch/probe_history.py").unlink(missing_ok=True)
    except Exception:
        pass

    return str(out_file)


if __name__ == "__main__":
    main()
