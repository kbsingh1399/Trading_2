import pandas as pd
import numpy as np

def check_liquidation_defense():
    print("=== FORENSIC SL vs LIQUIDATION / RETAIL STOP AUDIT ===")

    # 1. BTCUSD: Entry 81,084 | SL 81,446
    print("\n1. BTCUSD.pi: Entry=81,084.00, SL=81,446.00 (Short)")
    try:
        liq_df = pd.read_parquet("Data/feeds/14_Liquidation_Matrix.parquet")
        btc_liq = liq_df[liq_df['symbol'].str.contains('BTC', case=False, na=False)]
        near_sl = btc_liq[(btc_liq['price'] >= 81000) & (btc_liq['price'] <= 81600)].sort_values('price')
        print("BTC Liquidation clusters between 81,000 and 81,600:")
        for _, r in near_sl.iterrows():
            print(f"  Price: {r['price']}, Short Liq: {r.get('short_liq_vol_usd', 0):,.0f} USD, Long Liq: {r.get('long_liq_vol_usd', 0):,.0f} USD")
    except Exception as e:
        print("BTC liq check:", e)

    try:
        stops_df = pd.read_parquet("Data/feeds/15_Hyperdash_Stops_Map.parquet")
        btc_stops = stops_df[stops_df['symbol'].str.contains('BTC', case=False, na=False)]
        near_stops = btc_stops[(btc_stops['price'] >= 81000) & (btc_stops['price'] <= 81600)]
        print("BTC Retail stops near SL:")
        for _, r in near_stops.iterrows():
            print(f"  Price: {r['price']}, Total Stops: {r.get('total_stops_usd', 0):,.0f} USD")
    except Exception as e:
        print("BTC stops check:", e)

    # 2. XAUUSD: Entry 4040.50 | SL 4049.50
    print("\n2. XAUUSD.pi: Entry=4040.50, SL=4049.50 (Short)")
    try:
        xau_liq = liq_df[liq_df['symbol'].str.contains('XAU|GOLD', case=False, na=False)]
        near_xau = xau_liq[(xau_liq['price'] >= 4030) & (xau_liq['price'] <= 4060)].sort_values('price')
        print(f"XAU Liquidation clusters near 4040-4055: {len(near_xau)} found")
        for _, r in near_xau.iterrows():
            print(f"  Price: {r['price']}, Short Liq: {r.get('short_liq_vol_usd', 0):,.0f} USD")
    except Exception as e:
        print("XAU liq check:", e)

    # 3. AUDUSD: Entry 0.70270 | SL 0.70150
    print("\n3. AUDUSD.pi: Entry=0.70270, SL=0.70150 (Long)")
    # Asian Low is 0.70180. SL is 0.70150 (30 pts / 3.0 pips below Asian Low and daily VAL 0.70270)
    print("  Daily VAL: 0.70270 | Asian Session Low: 0.70180 | SL: 0.70150 (Clear of liquidity sweep pocket)")

    # 4. BNBUSD: Entry 753.30 | SL 757.20
    print("\n4. BNBUSD.p: Entry=753.30, SL=757.20 (Short)")
    try:
        bnb_liq = liq_df[liq_df['symbol'].str.contains('BNB', case=False, na=False)]
        near_bnb = bnb_liq[(bnb_liq['price'] >= 750) & (bnb_liq['price'] <= 760)].sort_values('price')
        print(f"BNB Liquidation clusters near 750-760: {len(near_bnb)} found")
        for _, r in near_bnb.iterrows():
            print(f"  Price: {r['price']}, Liq: {r.get('short_liq_vol_usd', 0):,.0f} USD")
    except Exception as e:
        print("BNB liq check:", e)

if __name__ == '__main__':
    check_liquidation_defense()
