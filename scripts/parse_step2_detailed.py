import os
import sys
import json
import re
import pandas as pd

sys.stdout.reconfigure(encoding='utf-8')

dossier_dir = 'docs/dossiers'
dossier_files = os.listdir(dossier_dir)

# Load eligible symbols
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

sector_data = {}

for idx, row in passed.iterrows():
    s = row['Broker_Symbol']
    clean_sym = s.replace('.pi', '').replace('.p', '')
    
    master_f = f"{clean_sym}_MASTER_DOSSIER.md"
    dossier_360 = f"{clean_sym}_360_DOSSIER.md"
    target_f = None
    if master_f in dossier_files:
        target_f = master_f
    elif dossier_360 in dossier_files:
        target_f = dossier_360
    else:
        alts = [f for f in dossier_files if f.startswith(clean_sym + '_') or clean_sym.startswith(f.split('_')[0])]
        if alts:
            target_f = alts[0]
            
    if not target_f:
        continue
        
    fp = os.path.join(dossier_dir, target_f)
    with open(fp, 'r', encoding='utf-8', errors='replace') as f:
        full_text = f.read()
        
    lines = full_text.splitlines()
    line_count = len(lines)
    
    # Extract Section 2/3 Auction Structure
    vah, val, poc = "N/A", "N/A", "N/A"
    for l in lines:
        if 'Daily VAH' in l or 'Value Area High' in l:
            m = re.findall(r"`?(\d+\.?\d*)`?", l)
            if m: vah = m[-1]
        elif 'Daily VAL' in l or 'Value Area Low' in l:
            m = re.findall(r"`?(\d+\.?\d*)`?", l)
            if m: val = m[-1]
        elif 'Daily POC' in l or 'Point of Control' in l:
            m = re.findall(r"`?(\d+\.?\d*)`?", l)
            if m: poc = m[-1]
            
    # Extract Section 10 Execution Card
    sec10_idx = full_text.find('## 10. Quantitative Trade Formulation')
    sec10 = full_text[sec10_idx:] if sec10_idx != -1 else ""
    
    entry_long, sl_long, tp_long, lot_long = "N/A", "N/A", "N/A", "N/A"
    entry_short, sl_short, tp_short, lot_short = "N/A", "N/A", "N/A", "N/A"
    decision = "STAND_ASIDE"
    
    if 'PASSIVE_MAKER_LIMIT_ARMED' in sec10:
        decision = "PASSIVE_MAKER_LIMIT_ARMED"
    elif 'DENIED_FAIL_CLOSED' in sec10:
        decision = "DENIED_FAIL_CLOSED"
    elif 'STAND_ASIDE_MONITOR' in sec10:
        decision = "STAND_ASIDE_MONITOR"
        
    for l in sec10.splitlines():
        if 'Candidate Long Setup' in l: current_side = 'LONG'
        elif 'Candidate Short Setup' in l: current_side = 'SHORT'
        elif 'Execution Entry:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m:
                if current_side == 'LONG': entry_long = m[0]
                else: entry_short = m[0]
        elif 'Spread-Padded Stop Loss:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m:
                if current_side == 'LONG': sl_long = m[0]
                else: sl_short = m[0]
        elif 'Take Profit:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m:
                if current_side == 'LONG': tp_long = m[0]
                else: tp_short = m[0]
        elif 'Mathematical Lot Sizing:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m:
                if current_side == 'LONG': lot_long = m[0]
                else: lot_short = m[0]

    sector = row['Macro_Sector']
    if sector not in sector_data:
        sector_data[sector] = []
        
    sector_data[sector].append({
        'symbol': s,
        'dossier': target_f,
        'lines': line_count,
        'bid': row['Bid_Quote'],
        'ask': row['Ask_Quote'],
        'spread_bps': row['Spread_BPS'],
        'threshold_bps': row['Threshold_BPS'],
        'vah': vah,
        'val': val,
        'poc': poc,
        'decision': decision,
        'entry_long': entry_long,
        'sl_long': sl_long,
        'tp_long': tp_long,
        'lot_long': lot_long,
        'entry_short': entry_short,
        'sl_short': sl_short,
        'tp_short': tp_short,
        'lot_short': lot_short,
    })

# Save to disk for reference
with open('docs/trade_plans/CYCLE_029_STEP2_DETAILED_FORENSICS.json', 'w', encoding='utf-8') as f:
    json.dump(sector_data, f, indent=2)

print("Exported detailed forensics for all sectors.")
for sec, items in sector_data.items():
    print(f"{sec}: {len(items)} assets parsed.")
