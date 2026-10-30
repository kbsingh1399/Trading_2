import os, glob, re, json
import pandas as pd

# 1. Load Live Spread Telemetry from 00_MT5_Account_Telemetry
telem_path = 'Data/telemetry/mt5_account_telemetry.json'
with open(telem_path, 'r', encoding='utf-8') as f:
    telem = json.load(f)

# 2. Check Candidate Master Dossiers
dossier_dir = 'docs/dossiers'
order_symbols = ['BTCUSD', 'BNBUSD', 'XAUUSD', 'NAS100', 'DJ30', 'AUDUSD']

results = {}
for sym in order_symbols:
    # Look for MASTER or 360 dossier
    matches = glob.glob(f'{dossier_dir}/{sym}_*DOSSIER.md') + glob.glob(f'{dossier_dir}/{sym}.md')
    if matches:
        dossier_file = matches[0]
        with open(dossier_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        
        # Extract sections
        # VAH, VAL, POC
        vah_m = re.search(r'VAH[:\s]+([0-9.]+)', content)
        val_m = re.search(r'VAL[:\s]+([0-9.]+)', content)
        poc_m = re.search(r'POC[:\s]+([0-9.]+)', content)
        
        # Whale wall
        whale_m = re.search(r'Whale[:\s]+([^\n]+)', content) or re.search(r'Whale Armor[:\s]+([^\n]+)', content)
        
        # Section 10 Card
        sec10_idx = content.find('## 10.')
        sec10 = content[sec10_idx:sec10_idx+1200] if sec10_idx != -1 else 'Card Not Found'
        
        results[sym] = {
            'file': dossier_file,
            'size': len(content),
            'vah': vah_m.group(1) if vah_m else 'N/A',
            'val': val_m.group(1) if val_m else 'N/A',
            'poc': poc_m.group(1) if poc_m else 'N/A',
            'sec10': sec10[:500]
        }

print('Dossier interrogation results for active and candidate assets:')
for sym, r in results.items():
    print(f"=== {sym} ({r['file']}, {r['size']} bytes) ===")
    print(f"VAH: {r['vah']} | VAL: {r['val']} | POC: {r['poc']}")
    print(f"Section 10 snippet:\n{r['sec10']}\n")
