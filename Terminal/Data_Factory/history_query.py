"""
Terminal/Data_Factory/history_query.py
=======================================
Historical Time-Travel & Telemetry Replay CLI.

Enables instant retrieval and study of past market states from 2 days, 10 days,
or 30 days prior across all telemetry streams:
  1. coinglass (whales, liquidations, ETFs, long/short ratios, funding rates)
  2. telemetry (bid, ask, spread, RSI, Z-score, orderflow, regime)
  3. forex_factory (macro calendar events & breaking geopolitical news)
  4. arkham (on-chain intelligence & entity fund flows)
  5. account_equity (MT5 equity, balance, margin, cushion above 4,775 floor)

Usage Examples:
  python Terminal/Data_Factory/history_query.py --summary
  python Terminal/Data_Factory/history_query.py --as-of "2026-10-14 18:00" --stream coinglass
  python Terminal/Data_Factory/history_query.py --whale "0x5b5d..60"
  python Terminal/Data_Factory/history_query.py --compare "2026-10-14 12:00" "2026-10-16 12:00" --stream telemetry --symbol BTCUSD.pi
  python Terminal/Data_Factory/history_query.py --gaps
"""

from __future__ import annotations
import argparse
import datetime
import json
import pathlib
import sys
from typing import Any, Dict, List

ROOT = pathlib.Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from Terminal.Data_Factory.time_series_database import ts_db


def print_summary():
    """Prints status of all recorded streams in the continuous database."""
    manifest_path = ts_db.manifest_path
    if not manifest_path.exists():
        print("Master manifest not found. Database is initializing.")
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    print("\n" + "=" * 80)
    print(" [DATABASE] CONTINUOUS HISTORICAL TIME-SERIES SUMMARY")
    print(f" Master Manifest Last Updated: {manifest.get('last_updated_utc')}")
    print("=" * 80)

    streams = manifest.get("streams", {})
    if not streams:
        print(" No streams recorded yet.")
        return

    print(f"{'Stream':<16} | {'Snapshots':<10} | {'Dates Available':<25} | {'Latest Timestamp':<24}")
    print("-" * 80)
    for name, info in streams.items():
        dates_str = ", ".join(info.get("dates_present", []))
        if len(dates_str) > 24:
            dates_str = dates_str[:21] + "..."
        print(f"{name:<16} | {info.get('total_snapshots', 0):<10} | {dates_str:<25} | {info.get('latest_recorded_utc', ''):<24}")

    print("=" * 80 + "\n")


def query_as_of(stream: str, target_time: str):
    """Retrieves and prints the snapshot as of a specified time."""
    print(f"\nSearching [{stream}] snapshot as of {target_time}...")
    res = ts_db.query_as_of(stream, target_time)
    if not res:
        print(f"No snapshot found for stream '{stream}' as of {target_time}.")
        return

    meta = res.get("_query_meta", {})
    print(f"Found matched snapshot: {meta.get('matched_file')}")
    print(f"Matched Time: {meta.get('matched_timestamp_utc')} (Delta: {meta.get('latency_seconds')}s)")
    print("-" * 60)

    # Pretty print summary based on stream type
    if stream == "coinglass":
        domains = res.get("domains", {})
        print(f"CoinGlass Domains Present: {list(domains.keys())}")
        if "hyperliquid_whales" in domains:
            whales = domains["hyperliquid_whales"].get("data", [])
            print(f"Whale Positions Count: {len(whales)}")
            print("\nTop 5 Whales at that moment:")
            for w in whales[:5]:
                print(f"  [{w.get('asset')}] {w.get('side')} User: {w.get('user')} | Notional: ${w.get('notional_usd', 0):,.0f} | Duration: {w.get('duration_days', 0):.1f} days")
        if "liquidation_maxpain" in domains:
            mp = domains["liquidation_maxpain"].get("data", [])
            print(f"\nLiquidation Max Pain Levels ({len(mp)} assets):")
            for m in mp[:5]:
                print(f"  {m.get('symbol')}: Current ${m.get('current_price')} | Short Max Pain: {m.get('short_max_pain_raw')} | Long Max Pain: {m.get('long_max_pain_raw')}")

    elif stream == "telemetry":
        acct = res.get("account", {})
        print(f"Account Balance: ${acct.get('balance_usd', 0):,.2f} | Equity: ${acct.get('equity_usd', 0):,.2f} | Cushion: +${acct.get('cushion_above_floor_usd', 0):,.2f}")
        matrix = res.get("assets_matrix_24", {})
        print(f"Assets Tracked: {len(matrix)}")
        for sym in ["BTCUSD.pi", "ETHUSD.pi", "USDJPY.pi", "XAUUSD.pi", "USWTI.p", "SP500.p"]:
            if sym in matrix:
                info = matrix[sym]
                print(f"  {sym:<10}: Price {info.get('bid')} | Z-Score: {info.get('z_score')} | RSI: {info.get('rsi')} | Regime: {info.get('regime')}")

    elif stream == "forex_factory":
        events = res.get("high_medium_calendar_events", [])
        news = res.get("breaking_news_stories", [])
        print(f"Macro Events: {len(events)} | Breaking Stories: {len(news)}")
        print("\nTop Events:")
        for ev in events[:5]:
            print(f"  [{ev.get('country')}] {ev.get('title')} ({ev.get('impact')}) | Actual: {ev.get('actual')} vs Forecast: {ev.get('forecast')}")

    elif stream == "arkham":
        entities = res.get("trending_institutional_entities", [])
        print(f"Tracked Institutional Entities: {len(entities)}")
        for ent in entities[:5]:
            print(f"  {ent.get('name')}: Balance ${ent.get('balance_usd', 0):,.0f}")

    print("\nFull snapshot accessible in Python via ts_db.query_as_of().\n")


def query_whale(user: str):
    """Prints history and duration for a whale address."""
    print(f"\nQuerying history for whale address matching '{user}'...")
    history = ts_db.query_whale_history(user)
    if not history:
        print(f"No history found for whale '{user}'.")
        return

    print(f"\nFound {len(history)} historical records for whale:")
    first = history[0]
    latest = history[-1]
    print(f"Asset: {latest.get('asset')} | Side: {latest.get('side')} | User: {latest.get('user')}")
    print(f"First Recorded: {first.get('snapshot_utc')} | Duration: {latest.get('duration_days', 0):.2f} days ({latest.get('duration_hours', 0):.1f} hours)")
    print(f"Latest Notional: ${latest.get('notional_usd', 0):,.0f} | Entry Price: {latest.get('entry_price')} | Status: {latest.get('status')}")
    print("\nTrajectory Progression:")
    for h in history[-10:]:
        print(f"  [{h.get('snapshot_utc')}] Notional: ${h.get('notional_usd', 0):,.0f} | Duration: {h.get('duration_days', 0):.2f}d | Status: {h.get('status')}")
    print()


def query_gaps(stream: str = ""):
    """Displays all shutdown and downtime gap events."""
    print("\n" + "=" * 80)
    print(" [RESUMPTION JOURNAL] SYSTEM SHUTDOWN & GAP RESUMPTION LOG")
    print("=" * 80)
    gaps = ts_db.query_gaps(stream if stream else None)
    if not gaps:
        print(" No offline gaps recorded. Database has operated continuously without interruption.")
        print("=" * 80 + "\n")
        return

    print(f"{'Stream':<16} | {'Last Recorded (Pre-Shutdown)':<24} | {'Resumed UTC':<24} | {'Downtime':<12}")
    print("-" * 80)
    for g in gaps:
        dur = f"{g.get('gap_duration_minutes', 0):.1f} min"
        print(f"{g.get('stream', ''):<16} | {g.get('last_recorded_utc', ''):<24} | {g.get('resumed_utc', ''):<24} | {dur:<12}")
    print("=" * 80 + "\n")


def compare_moments(t1: str, t2: str, stream: str, symbol: str = ""):
    """Compares metrics between two points in time."""
    print(f"\nComparing [{stream}] between t1={t1} and t2={t2}...")
    s1 = ts_db.query_as_of(stream, t1)
    s2 = ts_db.query_as_of(stream, t2)
    if not s1 or not s2:
        print(f"Could not retrieve snapshots for both timestamps (s1={bool(s1)}, s2={bool(s2)}).")
        return

    time1 = s1.get("_query_meta", {}).get("matched_timestamp_utc")
    time2 = s2.get("_query_meta", {}).get("matched_timestamp_utc")
    print(f"Snapshot 1: {time1}")
    print(f"Snapshot 2: {time2}")
    print("-" * 60)

    if stream == "telemetry" and symbol:
        m1 = s1.get("assets_matrix_24", {}).get(symbol, {})
        m2 = s2.get("assets_matrix_24", {}).get(symbol, {})
        if not m1 or not m2:
            print(f"Symbol {symbol} not found in both snapshots.")
            return
        p1, p2 = float(m1.get("bid", 0)), float(m2.get("bid", 0))
        z1, z2 = float(m1.get("z_score", 0)), float(m2.get("z_score", 0))
        r1, r2 = float(m1.get("rsi", 0)), float(m2.get("rsi", 0))
        print(f"Symbol: {symbol}")
        print(f"  Price:    {p1}  ->  {p2}  (Diff: {p2 - p1:+.5f})")
        print(f"  Z-Score:  {z1}  ->  {z2}  (Diff: {z2 - z1:+.2f})")
        print(f"  RSI:      {r1}  ->  {r2}  (Diff: {r2 - r1:+.2f})")
        print(f"  Regime:   {m1.get('regime')}  ->  {m2.get('regime')}")

    elif stream == "telemetry":
        a1 = s1.get("account", {})
        a2 = s2.get("account", {})
        eq1, eq2 = float(a1.get("equity_usd", 0)), float(a2.get("equity_usd", 0))
        cush1, cush2 = float(a1.get("cushion_above_floor_usd", 0)), float(a2.get("cushion_above_floor_usd", 0))
        print("Account Progression:")
        print(f"  Equity:  ${eq1:,.2f}  ->  ${eq2:,.2f}  (Net: {eq2 - eq1:+.2f} USD)")
        print(f"  Cushion: +${cush1:,.2f}  ->  +${cush2:,.2f}  (Net: {cush2 - cush1:+.2f} USD)")
    print()


def main():
    parser = argparse.ArgumentParser(description="Continuous Historical Time-Series Database Query Tool")
    parser.add_argument("--summary", action="store_true", help="Print summary of historical database")
    parser.add_argument("--as-of", type=str, help="Timestamp to query (e.g. '2026-10-14 18:00' or ISO)")
    parser.add_argument("--stream", type=str, default="coinglass", choices=list(ts_db.SUPPORTED_STREAMS), help="Stream name")
    parser.add_argument("--whale", type=str, help="Whale user address to query history for")
    parser.add_argument("--gaps", action="store_true", help="Show all recorded offline gaps / downtime events")
    parser.add_argument("--compare", nargs=2, metavar=("T1", "T2"), help="Compare two historical timestamps")
    parser.add_argument("--symbol", type=str, default="", help="Symbol to inspect in comparison")

    args = parser.parse_args()

    if args.summary or len(sys.argv) == 1:
        print_summary()
    elif args.gaps:
        query_gaps(args.stream if args.stream != "coinglass" else "")
    elif args.whale:
        query_whale(args.whale)
    elif args.compare:
        compare_moments(args.compare[0], args.compare[1], args.stream, args.symbol)
    elif args.as_of:
        query_as_of(args.stream, args.as_of)


if __name__ == "__main__":
    main()
