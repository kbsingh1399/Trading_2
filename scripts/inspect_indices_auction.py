#!/usr/bin/env python3
import sys, pathlib, polars as pl
try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass
ROOT = pathlib.Path(r"C:\Users\SIGMA\Documents\Trading_2")
auc = pl.read_parquet(ROOT / "Data" / "feeds" / "20_Auction_Market_Structure.parquet")
indices = auc.filter(pl.col('symbol').is_in(['SP500.p', 'DJ30.p', 'NAS100.p', 'US30.p', 'US500.p', 'USTEC.p', 'GER40.p']))
print("=== INDICES AUCTION STRUCTURE ===")
for r in indices.iter_rows(named=True):
    print(f"{r['symbol']:<10} | Price: {r['price']:<10} | POC: {r['daily_poc']:<10} | VAH: {r['daily_vah']:<10} | VAL: {r['daily_val']:<10} | Pos: {r['va_position']:<22} | Bias: {r['session_bias']}")
