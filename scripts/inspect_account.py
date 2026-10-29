import polars as pl
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

df = pl.read_parquet('Data/feeds/00_MT5_Account_Telemetry.parquet')
capital = df.filter(pl.col('Category') == 'CAPITAL_STATE')
for row in capital.iter_rows(named=True):
    print(f"{row['Broker_Symbol']}: {row['Gate_Status']} | {row['Execution_Posture']} | {row['Order_Type_Allowed']}")

# Check BTC and NZDUSD
assets = df.filter(pl.col('Broker_Symbol').is_in(['BTCUSD.pi', 'NZDUSD.pi', 'US500.p', 'SPX500.pi', 'US30.pi', 'US30.p']))
for row in assets.iter_rows(named=True):
    print(f"Asset: {row['Broker_Symbol']} | Bid: {row['Bid_Quote']} | Ask: {row['Ask_Quote']} | Spread: {row['Spread_BPS']} bps | Gate: {row['Gate_Status']}")
