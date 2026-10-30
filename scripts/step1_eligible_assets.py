import pandas as pd
import sys

sys.stdout.reconfigure(encoding='utf-8')

df = pd.read_parquet('Data/feeds/00_MT5_Account_Telemetry.parquet')
passed = df[(df['Category'] == 'SPREAD_GATE') & (df['Gate_Status'] == 'PASS')].copy()

def classify_sym(s):
    s_upper = s.upper()
    if any(m in s_upper for m in ['XAU', 'XAG', 'GAU', 'PLATINUM', 'PALLADIUM', 'COPPER', 'ALUMINIUM', 'NICKEL', 'ZINC', 'LEAD']):
        return 'Precious & Industrial Metals'
    elif any(idx in s_upper for idx in ['DJ30', 'NAS100', 'SP500', 'GER40', 'GER30', 'UK100', 'JP225', 'FR40', 'AU200', 'HK50', 'STOXX50', 'SWISS20', 'NETH25', 'US2000', 'CHINA50', 'CHINAH']):
        return 'Equity Indices'
    elif any(c in s_upper for c in ['BTC', 'ETH', 'SOL', 'BNB', 'XRP', 'DOGE', 'ADA', 'TRX', 'LINK', 'AVAX', 'SUI', 'NEAR', 'DOT', 'LTC', 'BCH', 'APT', 'OP', 'ARB', 'XMR', 'ZEC', 'DSH', 'YFI', 'XLM', 'AVE']):
        return 'Crypto Perpetuals & CFDs'
    elif any(e in s_upper for e in ['USWTI', 'UKBRENT', 'GAS']):
        return 'Energy & Commodities'
    else:
        return 'Forex Majors & Crosses'

passed['Macro_Sector'] = passed['Broker_Symbol'].apply(classify_sym)

print(f"=== TOTAL ELIGIBLE CANDIDATES: {len(passed)} ===")
for sector, grp in passed.groupby('Macro_Sector'):
    print(f"\n--- {sector} ({len(grp)}) ---")
    for _, row in grp.sort_values('Spread_BPS').iterrows():
        sym = row['Broker_Symbol']
        bid = row['Bid_Quote']
        ask = row['Ask_Quote']
        spread = row['Spread_BPS']
        thresh = row['Threshold_BPS']
        print(f"{sym:<12} | Bid: {bid:<10} | Ask: {ask:<10} | Spread: {spread:.2f} bps (Threshold: {thresh:.1f} bps) | PASS")
