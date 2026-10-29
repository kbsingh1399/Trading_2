import polars as pl
import json
from pathlib import Path

feeds_dir = Path("Data/feeds")

# 1. Test stops ladder
stops_df = pl.read_parquet(feeds_dir / "15_Hyperdash_Stops_Map.parquet")
btc_stops = stops_df.filter(pl.col("asset") == "BTC")
print(f"Total BTC stops rows: {len(btc_stops)}")

parsed_stops = []
for r in btc_stops.iter_rows(named=True):
    raw_px = str(r.get("price", "")).replace("$", "").replace(",", "").strip()
    raw_cum = str(r.get("cumulative_stops", "")).replace("$", "").replace(",", "").strip()
    raw_buy = str(r.get("buy_stops", "")).replace("$", "").replace(",", "").strip()
    raw_sell = str(r.get("sell_stops", "")).replace("$", "").replace(",", "").strip()
    try:
        px = float(raw_px)
        parsed_stops.append({
            "price": px,
            "dist": r.get("distance_pct", "-"),
            "side": r.get("side", "-"),
            "cum": raw_cum,
            "buy": raw_buy,
            "sell": raw_sell
        })
    except ValueError:
        pass

# Filter within 76,000 to 85,000 (around 80,355)
tactical_stops = [s for s in parsed_stops if 78000 <= s["price"] <= 83000]
tactical_stops.sort(key=lambda x: x["price"])
print(f"Tactical BTC stops (78k-83k): {len(tactical_stops)} rows")
for s in tactical_stops[:5]:
    print(" ", s)

# 2. Test whale ladder
whale_df = pl.read_parquet(feeds_dir / "10_Whale_Orders.parquet")
btc_whales = whale_df.filter(pl.col("symbol").str.contains("BTC"))
print(f"Total BTC whale rows: {len(btc_whales)}")

parsed_whales = []
for r in btc_whales.iter_rows(named=True):
    raw_px = str(r.get("price", "")).replace("$", "").replace(",", "").strip()
    raw_val = str(r.get("notional_usd", r.get("initial_value_usd", 0.0))).replace("$", "").replace(",", "").strip()
    try:
        px = float(raw_px)
        val = float(raw_val)
        if val >= 50000:
            parsed_whales.append({
                "side": r.get("side", "-"),
                "price": px,
                "val": val,
                "amount": r.get("amount_btc", 0.0),
                "dur": r.get("order_duration", "-"),
                "ex": r.get("exchange", "-"),
                "id": r.get("order_id", "-")
            })
    except ValueError:
        pass

bids = [w for w in parsed_whales if "buy" in str(w["side"]).lower() or "bid" in str(w["side"]).lower()]
asks = [w for w in parsed_whales if "sell" in str(w["side"]).lower() or "ask" in str(w["side"]).lower()]
bids.sort(key=lambda x: x["price"], reverse=True)
asks.sort(key=lambda x: x["price"])
print(f"Qualifying BTC bids >= 50k: {len(bids)} | asks >= 50k: {len(asks)}")
print("Top 3 Bids:", bids[:3])
print("Top 3 Asks:", asks[:3])
