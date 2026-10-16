"""
Terminal/Data_Factory/history_query.py
=======================================
Historical Time-Travel & Behavioral Telemetry Replay CLI.

Enables instant retrieval and study of past market states from 2 days, 10 days,
or 30 days prior across all telemetry streams with sub-millisecond SQLite queries:
  1. coinglass (whales, liquidations, ETFs, long/short ratios, funding rates)
  2. telemetry (bid, ask, spread, RSI, Z-score, orderflow, regime, whale bunkers)
  3. forex_factory (macro calendar events & breaking geopolitical news)
  4. arkham (on-chain intelligence & entity fund flows)
  5. account_equity (MT5 equity, balance, margin, cushion above 4,775 floor)

Usage Examples:
  python Terminal/Data_Factory/history_query.py --summary
  python Terminal/Data_Factory/history_query.py --timeline USDJPY --hours 24
  python Terminal/Data_Factory/history_query.py --timeline BTC --hours 12
  python Terminal/Data_Factory/history_query.py --as-of "2026-10-14 18:00" --stream coinglass
  python Terminal/Data_Factory/history_query.py --whale "0x5b5d..60"
  python Terminal/Data_Factory/history_query.py --compare "2026-10-14 12:00" "2026-10-16 12:00" --stream telemetry --symbol BTC
  python Terminal/Data_Factory/history_query.py --correlate BTC --hours 6
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
    print(" Storage Compression: Gzip (Level 6) -> ~90% Disk Footprint Reduction")
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


def query_timeline(symbol: str, hours: float = 24.0):
    """Displays the chronological metric trajectory of a symbol over time."""
    clean_sym = symbol.replace(".pi", "").replace(".p", "")
    print(f"\nQuerying timeline for [{clean_sym}] over the last {hours} hours...")
    timeline = ts_db.query_symbol_timeline(clean_sym, hours)
    if not timeline:
        # Try exact input if clean_sym returned empty
        timeline = ts_db.query_symbol_timeline(symbol, hours)

    if not timeline:
        print(f"No telemetry records found for symbol '{symbol}' within {hours}h window.")
        return

    print("\n" + "=" * 110)
    print(f" [TIMELINE] {clean_sym} METRIC EVOLUTION OVER TIME ({len(timeline)} cycles)")
    print("=" * 110)
    print(f"{'Timestamp UTC':<20} | {'Price':<10} | {'Z-Score':<8} | {'RSI':<6} | {'Regime':<12} | {'Spread':<8} | {'Support Wall':<18} | {'Resistance Wall':<18}")
    print("-" * 110)
    for row in timeline[-25:]:  # Show recent 25 points
        p = f"{row.get('bid', 0.0):.4f}" if row.get("bid") is not None else "N/A"
        z = f"{row.get('z_score', 0.0):+.2f}" if row.get("z_score") is not None else "N/A"
        r = f"{row.get('rsi', 0.0):.1f}" if row.get("rsi") is not None else "N/A"
        reg = row.get("regime", "")[:12]
        sp = f"{row.get('spread_bps', 0.0):.1f} bps" if row.get("spread_bps") is not None else "N/A"

        supp = "None"
        if row.get("nearest_support_level"):
            supp = f"{row.get('nearest_support_level')} (${row.get('nearest_support_notional', 0)/1000:.0f}k)"

        res = "None"
        if row.get("nearest_resistance_level"):
            res = f"{row.get('nearest_resistance_level')} (${row.get('nearest_resistance_notional', 0)/1000:.0f}k)"

        print(f"{row.get('snapshot_utc', '')[:19]:<20} | {p:<10} | {z:<8} | {r:<6} | {reg:<12} | {sp:<8} | {supp:<18} | {res:<18}")

    print("=" * 110 + "\n")


def query_correlate(symbol: str, hours: float = 6.0):
    """Cross-references asset orderflow with macro calendar events, CoinGlass liquidations, and whales."""
    clean_sym = symbol.replace(".pi", "").replace(".p", "")
    print(f"\nRunning cross-stream correlation analysis for [{clean_sym}] over past {hours} hours...")

    # 1. Telemetry timeline
    timeline = ts_db.query_symbol_timeline(clean_sym, hours)
    # 2. CoinGlass Whales
    whales = ts_db.query_whale_history(clean_sym)
    # 3. Macro events
    min_epoch = datetime.datetime.now(datetime.timezone.utc).timestamp() - (hours * 3600.0)
    macro_events = []
    with ts_db._get_connection() as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT snapshot_utc, country, title, impact, actual, forecast, previous
            FROM macro_event_history
            WHERE snapshot_epoch >= ? AND impact IN ('HIGH', 'MEDIUM')
            ORDER BY snapshot_epoch DESC LIMIT 10
        """, (min_epoch,))
        macro_events = [dict(r) for r in cur.fetchall()]

    print("\n" + "=" * 90)
    print(f" [CORRELATION SYNTHESIS] {clean_sym} MULTI-PILLAR CROSS-STREAM ALIGNMENT")
    print("=" * 90)

    if timeline:
        first = timeline[0]
        latest = timeline[-1]
        p0, p1 = first.get("bid") or 0.0, latest.get("bid") or 0.0
        z0, z1 = first.get("z_score") or 0.0, latest.get("z_score") or 0.0
        r0, r1 = first.get("rsi") or 0.0, latest.get("rsi") or 0.0
        print("1. Orderflow & Price Progression:")
        print(f"   Price:   {p0:.4f} -> {p1:.4f} (Shift: {p1 - p0:+.4f})")
        print(f"   Z-Score: {z0:+.2f} -> {z1:+.2f} (Shift: {z1 - z0:+.2f})")
        print(f"   RSI:     {r0:.1f} -> {r1:.1f}")
        print(f"   Current Regime: {latest.get('regime')} | Spread: {latest.get('spread_bps', 0):.2f} bps")
        if latest.get("nearest_support_level"):
            print(f"   Support Defense: {latest.get('nearest_support_level')} (${latest.get('nearest_support_notional', 0)/1000:.0f}k notional)")
        if latest.get("nearest_resistance_level"):
            print(f"   Resistance Wall: {latest.get('nearest_resistance_level')} (${latest.get('nearest_resistance_notional', 0)/1000:.0f}k notional)")

    print("\n2. CoinGlass Whale Activity:")
    if whales:
        print(f"   Active Whale Wallets: {len(whales)}")
        for w in whales[:3]:
            print(f"   - {w.get('side')} User: {w.get('user')} | Notional: ${w.get('notional_usd', 0):,.0f} | Duration: {w.get('duration_days', 0):.1f} days")
    else:
        print("   No direct whale positions matching symbol in Hyperliquid ledger.")

    print("\n3. Macro Calendar Proximity (Forex Factory):")
    if macro_events:
        for ev in macro_events[:5]:
            print(f"   - [{ev.get('country')}] {ev.get('title')} ({ev.get('impact')}) | Actual: {ev.get('actual')} vs Forecast: {ev.get('forecast')}")
    else:
        print("   No HIGH/MEDIUM macro events released in recent hours.")

    print("=" * 90 + "\n")


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
        for sym in ["BTC", "ETH", "USDJPY", "GOLD", "USWTI", "SP500"]:
            if sym in matrix:
                info = matrix[sym]
                q = info.get("quotes", {})
                c = info.get("causal_indicators", {})
                print(f"  {sym:<8}: Price {q.get('bid')} | Z-Score: {c.get('vwap_z_score')} | RSI: {c.get('rsi_14')} | Regime: {c.get('trend_regime')}")

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

    clean_sym = symbol.replace(".pi", "").replace(".p", "")
    if stream == "telemetry" and clean_sym:
        m1 = s1.get("assets_matrix_24", {}).get(clean_sym, {})
        m2 = s2.get("assets_matrix_24", {}).get(clean_sym, {})
        if not m1 or not m2:
            print(f"Symbol {clean_sym} not found in both snapshots.")
            return
        p1 = float(m1.get("quotes", {}).get("bid") or m1.get("bid", 0))
        p2 = float(m2.get("quotes", {}).get("bid") or m2.get("bid", 0))
        z1 = float(m1.get("causal_indicators", {}).get("vwap_z_score") or m1.get("z_score", 0))
        z2 = float(m2.get("causal_indicators", {}).get("vwap_z_score") or m2.get("z_score", 0))
        r1 = float(m1.get("causal_indicators", {}).get("rsi_14") or m1.get("rsi", 0))
        r2 = float(m2.get("causal_indicators", {}).get("rsi_14") or m2.get("rsi", 0))
        reg1 = m1.get("causal_indicators", {}).get("trend_regime") or m1.get("regime")
        reg2 = m2.get("causal_indicators", {}).get("trend_regime") or m2.get("regime")

        print(f"Symbol: {clean_sym}")
        print(f"  Price:    {p1}  ->  {p2}  (Diff: {p2 - p1:+.5f})")
        print(f"  Z-Score:  {z1}  ->  {z2}  (Diff: {z2 - z1:+.2f})")
        print(f"  RSI:      {r1}  ->  {r2}  (Diff: {r2 - r1:+.2f})")
        print(f"  Regime:   {reg1}  ->  {reg2}")

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
    parser = argparse.ArgumentParser(description="Continuous Historical Time-Series Database & Behavioral Analytics CLI")
    parser.add_argument("--summary", action="store_true", help="Print summary of historical database")
    parser.add_argument("--timeline", type=str, help="Symbol to inspect chronological timeline for (e.g. USDJPY, BTC)")
    parser.add_argument("--hours", type=float, default=24.0, help="Hours window for timeline/correlation query (default: 24h)")
    parser.add_argument("--correlate", type=str, help="Symbol to cross-reference with macro, whales, and liquidations")
    parser.add_argument("--as-of", type=str, help="Timestamp to query (e.g. '2026-10-14 18:00' or ISO)")
    parser.add_argument("--stream", type=str, default="coinglass", choices=list(ts_db.SUPPORTED_STREAMS), help="Stream name")
    parser.add_argument("--whale", type=str, help="Whale user address to query history for")
    parser.add_argument("--gaps", action="store_true", help="Show all recorded offline gaps / downtime events")
    parser.add_argument("--compare", nargs=2, metavar=("T1", "T2"), help="Compare two historical timestamps")
    parser.add_argument("--symbol", type=str, default="", help="Symbol to inspect in comparison")

    args = parser.parse_args()

    if args.summary or len(sys.argv) == 1:
        print_summary()
    elif args.timeline:
        query_timeline(args.timeline, args.hours)
    elif args.correlate:
        query_correlate(args.correlate, args.hours)
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
