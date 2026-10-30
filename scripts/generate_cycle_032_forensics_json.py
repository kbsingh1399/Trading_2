import os
import sys
import json
import re
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.stdout.reconfigure(encoding='utf-8')

dossier_dir = ROOT / 'docs' / 'dossiers'
dossier_files = os.listdir(dossier_dir)

df = pd.read_parquet(ROOT / 'Data' / 'feeds' / '00_MT5_Account_Telemetry.parquet')
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

results = []
read_count = 0
total_lines_read = 0
total_bytes_read = 0

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
        
    fp = dossier_dir / target_f
    size_bytes = os.path.getsize(fp)
    
    with open(fp, 'r', encoding='utf-8', errors='replace') as f:
        full_text = f.read()
        
    lines = full_text.splitlines()
    line_count = len(lines)
    read_count += 1
    total_lines_read += line_count
    total_bytes_read += size_bytes
    
    vah = None
    val = None
    poc = None
    for l in lines:
        if 'VAH' in l and ('Value Area High' in l or 'Daily VAH' in l or 'Weekly VAH' in l or 'PD_VAH' in l):
            m = re.findall(r"[-+]?\d*\.\d+|\d+", l)
            if m:
                try: vah = float(m[-1])
                except: pass
        if 'VAL' in l and ('Value Area Low' in l or 'Daily VAL' in l or 'Weekly VAL' in l or 'PD_VAL' in l):
            m = re.findall(r"[-+]?\d*\.\d+|\d+", l)
            if m:
                try: val = float(m[-1])
                except: pass
        if 'POC' in l and ('Point of Control' in l or 'Daily POC' in l or 'Weekly POC' in l):
            m = re.findall(r"[-+]?\d*\.\d+|\d+", l)
            if m:
                try: poc = float(m[-1])
                except: pass

    sec10_idx = full_text.find('## 10. Quantitative Trade Formulation')
    if sec10_idx == -1:
        sec10_idx = full_text.find('SECTION 10')
    if sec10_idx == -1:
        sec10_idx = full_text.find('Quantitative Trade Formulation')
        
    sec10_text = full_text[sec10_idx:] if sec10_idx != -1 else ""
    
    has_buy = 'BUY_LIMIT' in sec10_text or 'Order Type: `BUY' in sec10_text
    has_sell = 'SELL_LIMIT' in sec10_text or 'Order Type: `SELL' in sec10_text
    
    decision = "STAND_ASIDE_MONITOR"
    if 'PASSIVE_MAKER_LIMIT_ARMED' in sec10_text:
        decision = "PASSIVE_MAKER_LIMIT_ARMED"
    elif 'DENIED_FAIL_CLOSED' in sec10_text:
        decision = "DENIED_FAIL_CLOSED"
        
    entry_val = None
    sl_val = None
    tp_val = None
    for l in sec10_text.splitlines():
        if 'Execution Entry:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m: entry_val = m[0]
        elif 'Spread-Padded Stop Loss:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m: sl_val = m[0]
        elif 'Take Profit:' in l or '+2.5R Take Profit:' in l:
            m = re.findall(r"`([^`]+)`", l)
            if m: tp_val = m[0]

    record = {
        'symbol': s,
        'clean_sym': clean_sym,
        'sector': row['Macro_Sector'],
        'dossier_file': target_f,
        'bytes': size_bytes,
        'lines': line_count,
        'bid': float(row['Bid_Quote']),
        'ask': float(row['Ask_Quote']),
        'mid': float(row['Mid_Price']),
        'spread_bps': float(row['Spread_BPS']),
        'threshold_bps': float(row['Threshold_BPS']),
        'vah': vah,
        'val': val,
        'poc': poc,
        'decision': decision,
        'has_buy_setup': has_buy,
        'has_sell_setup': has_sell,
        'entry': entry_val,
        'sl': sl_val,
        'tp': tp_val
    }
    results.append(record)

out_file = ROOT / 'docs' / 'trade_plans' / 'CYCLE_032_DOSSIER_FORENSICS_ALL_92.json'
out_file.parent.mkdir(parents=True, exist_ok=True)
with open(out_file, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print(f"Generated {out_file} with {len(results)} dossiers examined.")
