#!/usr/bin/env python3
"""
scripts/inspect_us_cash_open.py
===============================
Inspect MT5 Account, Resting Orders, and US Equity Cash Open dynamics.
"""
import sys
import json
import pathlib
import polars as pl

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")

def main():
    # 1. Telemetry
    t_path = ROOT / "Data" / "feeds" / "00_MT5_Account_Telemetry.parquet"
    if t_path.exists():
        df_t = pl.read_parquet(t_path)
        symbols = ['NZDUSD.pi', 'BTCUSD.pi', 'SP500.p', 'DJ30.p', 'NAS100.p', 'XAUUSD.pi', 'EURUSD.pi']
        sub = df_t.filter(pl.col('Broker_Symbol').is_in(symbols))
        print("=== MT5 LIVE TELEMETRY AT US CASH OPEN ===")
        for r in sub.iter_rows(named=True):
            print(f"{r['Broker_Symbol']:<12} | Bid: {r['Bid_Quote']:<10} | Ask: {r['Ask_Quote']:<10} | Mid: {r['Mid_Price']:<10} | Spread: {r['Spread_BPS']:>5.2f} bps | Gate: {r['Gate_Status']}")

    # 2. Account equity snapshot
    eq_path = ROOT / "docs" / "telemetry" / "live_snapshot_latest.json"
    if eq_path.exists():
        with open(eq_path, "r", encoding="utf-8") as f:
            snap = json.load(f)
        acc = snap.get("account", {})
        print("\n=== ACCOUNT STATE ===")
        print(f"Balance: ${acc.get('balance', 0):,.2f} USD | Equity: ${acc.get('equity', 0):,.2f} USD | Free Margin: ${acc.get('free_margin', 0):,.2f} USD")
        print(f"Open Positions Count: {len(snap.get('open_positions', []))}")
        print(f"Pending Orders Count: {len(snap.get('pending_orders', []))}")
        for po in snap.get("pending_orders", []):
            print(f"  * Ticket #{po.get('ticket')}: {po.get('symbol')} {po.get('type')} {po.get('volume')} lots @ {po.get('price_open')} (SL: {po.get('sl')}, TP: {po.get('tp')})")

    # 3. Dynamic supervisor status
    sup_path = ROOT / "Data" / "dynamic_position_supervisor_status.json"
    if sup_path.exists():
        with open(sup_path, "r", encoding="utf-8") as f:
            sup = json.load(f)
        print("\n=== DYNAMIC POSITION SUPERVISOR ===")
        print(f"Timestamp: {sup.get('timestamp_ist')} | Active Runners: {sup.get('active_runners_count')} | Managed Orders: {sup.get('managed_orders_count')}")

if __name__ == "__main__":
    main()
