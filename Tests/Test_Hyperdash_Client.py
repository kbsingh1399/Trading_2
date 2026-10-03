import sys
import pathlib

# Ensure workspace root is in sys.path
root_dir = pathlib.Path(__file__).parent.parent
sys.path.insert(0, str(root_dir))

from Terminal.Api_Client import HyperdashClient

def test_client():
    client = HyperdashClient()
    
    print("\n--- 1. Testing fetch_all_assets ---")
    assets = client.fetch_all_assets()
    assert len(assets) > 200, f"Expected >200 assets, got {len(assets)}"
    btc = [a for a in assets if a["coin"] == "BTC"][0]
    print(f"PASS: {len(assets)} assets loaded. BTC Mark Price: {btc['mark_px']} USD, 24h Vol: {btc['volume_24h']:,.0f} USD")

    print("\n--- 2. Testing fetch_l2_book ---")
    book = client.fetch_l2_book("BTC")
    assert len(book["bids"]) > 0 and len(book["asks"]) > 0, "Orderbook empty"
    print(f"PASS: BTC Best Bid: {book['best_bid']}, Best Ask: {book['best_ask']}, Spread: {book['spread']} ({book['spread_bps']:.2f} bps)")

    current_px = book["best_bid"]
    min_px = current_px * 0.98
    max_px = current_px * 1.02

    print("\n--- 3. Testing fetch_l3_orders (Whale Wallet Addresses) ---")
    orders = client.fetch_l3_orders("BTC", min_px, max_px)
    assert len(orders) > 0, "No L3 orders returned"
    print(f"PASS: Retrieved {len(orders)} Level 3 orders. Top whale address: {orders[0]['address']}, Size: {orders[0]['size']} BTC (${orders[0]['notional_usd']:,.0f})")

    print("\n--- 4. Testing fetch_liquidations ---")
    liqs = client.fetch_liquidations("BTC", current_px * 0.8, current_px * 1.2)
    assert liqs["total_long_size"] > 0 or liqs["total_short_size"] > 0, "Liquidations empty"
    print(f"PASS: Total Long Liqs: {liqs['total_long_size']:,.1f} BTC, Total Short Liqs: {liqs['total_short_size']:,.1f} BTC")
    if liqs["top_long_whales"]:
        print(f"  Top Long Liq Whale: {liqs['top_long_whales'][0]['address']} at ${liqs['top_long_whales'][0]['price']:,.1f}")

    print("\n--- 5. Testing fetch_stops ---")
    stops = client.fetch_stops("BTC", current_px * 0.8, current_px * 1.2)
    assert stops["total_buy_size"] > 0 or stops["total_sell_size"] > 0, "Stops empty"
    print(f"PASS: Total Buy Stops: {stops['total_buy_size']:,.1f} BTC, Total Sell Stops: {stops['total_sell_size']:,.1f} BTC")

    print("\n--- 6. Testing fetch_top_traders ---")
    top_traders = client.fetch_top_traders("BTC", limit=5)
    print(f"PASS: Retrieved {len(top_traders)} Top Trader Winner Positions.")
    if top_traders:
        print(f"  Top Winner: {top_traders[0]['address']}, Unrealized PnL: ${float(top_traders[0]['unrealizedPnl']):,.2f}")

    print("\n--- 7. Testing historical candle download ---")
    candle_file = client.download_historical_candles("BTC", interval="15m", days=1)
    assert pathlib.Path(candle_file).exists(), "Candle file not created"
    print(f"PASS: Historical candle file successfully created at {candle_file}")

    print("\n--- 8. Testing historical funding download ---")
    funding_file = client.download_historical_funding("BTC", days=3)
    assert pathlib.Path(funding_file).exists(), "Funding file not created"
    print(f"PASS: Historical funding file successfully created at {funding_file}")

    print("\n>>> ALL 8 API CLIENT TEST SUITES PASSED 100%! <<<")

if __name__ == "__main__":
    test_client()
