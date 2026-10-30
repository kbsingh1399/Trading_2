import pandas as pd
from pathlib import Path

df = pd.read_parquet('Data/feeds/00_MT5_Account_Telemetry.parquet')
passed = df[(df['Category'] == 'SPREAD_GATE') & (df['Gate_Status'] == 'PASS')].copy()

out_path = Path('scripts/cycle_033_eligible_dossiers.txt')
lines = []
for idx, r in passed.iterrows():
    lines.append(f"{r['Broker_Symbol']},{r['Spread_BPS']:.2f},{r['Bid_Quote']},{r['Ask_Quote']}")

out_path.write_text('\n'.join(lines), encoding='utf-8')
print(f"Cycle_033 Step 1: Filtered {len(passed)} spread-eligible assets.")
print(f"Saved manifest to {out_path}")
