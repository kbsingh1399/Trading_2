import pandas as pd
import glob
import os

df = pd.read_parquet('Data/feeds/00_MT5_Account_Telemetry.parquet')
passed = df[(df['Gate_Status'] == 'PASS') & (df['Category'] == 'SPREAD_GATE')]
symbols = passed['Broker_Symbol'].tolist()

def clean_sym(s):
    return s.replace('.pi', '').replace('.p', '').replace('.i', '')

matched_files = []
for s in symbols:
    base = clean_sym(s)
    cand1 = f"c:\\Users\\SIGMA\\Documents\\Trading_2\\docs\\dossiers\\{base}_MASTER_DOSSIER.md"
    cand2 = f"c:\\Users\\SIGMA\\Documents\\Trading_2\\docs\\dossiers\\{base}USD_MASTER_DOSSIER.md" if not base.endswith('USD') else None
    cand3 = f"c:\\Users\\SIGMA\\Documents\\Trading_2\\docs\\dossiers\\{base[:-3]}_MASTER_DOSSIER.md" if base.endswith('USD') else None
    for c in [cand1, cand3, cand2]:
        if c and os.path.exists(c):
            if c not in matched_files:
                matched_files.append(c)
            break

print(f"Total unique dossier files: {len(matched_files)}")
with open('scripts/eligible_dossier_paths.txt', 'w', encoding='utf-8') as f:
    for path in matched_files:
        f.write(path + '\n')
print("Saved to scripts/eligible_dossier_paths.txt")
