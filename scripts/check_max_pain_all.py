import pandas as pd

for tf in ['24H', '48H', '3D', '7D']:
    f = f'Data/feeds/9_Liquidation_Max_Pain_{tf}.parquet'
    df = pd.read_parquet(f)
    print(f"=== MAX PAIN {tf} ===")
    for sym in ['BTC', 'BNB', 'GOLD', 'NAS', 'DJ', 'AUD']:
        m = df[df['symbol'].str.contains(sym, case=False, na=False)]
        if len(m) > 0:
            for _, r in m.iterrows():
                print(f"  {r['symbol']} | Price: {r['price']} | Short Max Pain: {r.get('short_max_pain_price')} | Long Max Pain: {r.get('long_max_pain_price')}")
