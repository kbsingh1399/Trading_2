# scripts/test_full_43_dump.py
import polars as pl
import time
import pathlib
import concurrent.futures

t0 = time.time()
feeds_dir = pathlib.Path("Data/feeds")
files = sorted(list(feeds_dir.glob("*.parquet")))
SYMBOL_COLS = ["symbol", "base_asset", "asset", "Asset", "Symbol", "coin", "Ticker", "Broker_Symbol", "market_pair", "pair", "instrument"]

def load_one(p):
    df = pl.read_parquet(p)
    return p.name, df

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    raw_dfs = dict(pool.map(load_one, files))

t1 = time.time()
print(f"Read all {len(raw_dfs)} DataFrames in {t1 - t0:.3f}s")

# Index all rows
indices = {}
for fname, df in raw_dfs.items():
    indices[fname] = {}
    cols = df.columns
    matching_cols = [c for c in cols if c in SYMBOL_COLS]
    if not matching_cols:
        continue
    for r in df.iter_rows(named=True):
        val_set = set()
        for mc in matching_cols:
            v = r.get(mc)
            if v is not None:
                vs = str(v).upper().strip()
                if vs:
                    val_set.add(vs)
                    clean_v = vs.replace(".PI", "").replace(".P", "")
                    if clean_v != vs:
                        val_set.add(clean_v)
        for vs in val_set:
            if vs not in indices[fname]:
                indices[fname][vs] = []
            indices[fname][vs].append(r)

t2 = time.time()
print(f"Indexed all 43 files in {t2 - t1:.3f}s (Total: {t2 - t0:.3f}s)")

# Test rendering BTC tables
btc_liq = indices.get("14_Liquidation_Matrix.parquet", {}).get("BTCUSDT", [])
print(f"BTC Liquidation Matrix rows: {len(btc_liq)}")

t_table_0 = time.time()
table_lines = [
    "| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol | OKX Vol | Bybit Vol | Venue Tier |",
    "|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|"
]
for r in btc_liq:
    px = r.get("price_level") or 0.0
    vol = r.get("liquidation_vol_usd") or 0.0
    cum = r.get("cumulative_liq_usd") or 0.0
    bv = r.get("binance_vol_usd") or 0.0
    ov = r.get("okx_vol_usd") or 0.0
    byv = r.get("bybit_vol_usd") or 0.0
    table_lines.append(f"| `{r.get('timeframe', '-')}` | `{r.get('side', '-')}` | `{px:,.2f}` | {vol:,.2f} USD | {cum:,.2f} USD | {bv:,.2f} | {ov:,.2f} | {byv:,.2f} | `{r.get('venue_tier', '-')}` |")

table_str = "\n".join(table_lines)
t_table_1 = time.time()
print(f"Rendered {len(btc_liq)} rows ({len(table_str)} characters) in {t_table_1 - t_table_0:.3f}s")
