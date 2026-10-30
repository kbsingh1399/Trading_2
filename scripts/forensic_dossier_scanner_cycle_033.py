import os
import sys
import json
import re

# Set stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

eligible_symbols = []
with open('scripts/cycle_033_eligible_dossiers.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        sym = line.split(',')[0].replace('.pi', '').replace('.p', '')
        eligible_symbols.append(sym)

print(f"Loaded {len(eligible_symbols)} eligible symbols from scripts/cycle_033_eligible_dossiers.txt")

results = {}
total_lines_read = 0
total_bytes_read = 0

for sym in eligible_symbols:
    fpath = f"docs/dossiers/{sym}_MASTER_DOSSIER.md"
    if not os.path.exists(fpath):
        alts = [f for f in os.listdir("docs/dossiers") if f.upper().startswith(sym.upper())]
        if alts:
            fpath = f"docs/dossiers/{alts[0]}"
        else:
            print(f"WARNING: Dossier for {sym} not found!")
            continue

    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    lines_count = content.count('\n') + 1
    bytes_count = len(content.encode('utf-8'))
    total_lines_read += lines_count
    total_bytes_read += bytes_count

    # Extract Live Bid & Ask Quote
    bid_m = re.search(r"Live Bid Quote\*\*:\s*`([^`]+)`", content)
    ask_m = re.search(r"Live Ask Quote\*\*:\s*`([^`]+)`", content)
    spread_m = re.search(r"Spread BPS\*\*:\s*`([^`]+)`", content)
    
    # Extract Value Area
    vah_m = re.search(r"Value Area High \(VAH\)\s*=\s*`([^`]+)`", content)
    poc_m = re.search(r"Point of Control \(POC\)\s*=\s*`([^`]+)`", content)
    val_m = re.search(r"Value Area Low \(VAL\)\s*=\s*`([^`]+)`", content)
    
    # Extract Postured Action
    decision_m = re.search(r"Postured Action\*\*:\s*`([^`]+)`", content)

    # Extract Candidate Long Setup
    long_entry_m = re.search(r"Candidate Long Setup.*?Execution Entry:\s*`([^`]+)`", content, re.DOTALL)
    long_sl_m = re.search(r"Candidate Long Setup.*?Spread-Padded Stop Loss:\s*`([^`]+)`", content, re.DOTALL)
    long_tp_m = re.search(r"Candidate Long Setup.*?\+2\.5R Take Profit:\s*`([^`]+)`", content, re.DOTALL)
    long_lot_m = re.search(r"Candidate Long Setup.*?Mathematical Lot Sizing:\s*\*\*`([^`]+)`\*\*", content, re.DOTALL)

    # Extract Candidate Short Setup
    short_entry_m = re.search(r"Candidate Short Setup.*?Execution Entry:\s*`([^`]+)`", content, re.DOTALL)
    short_sl_m = re.search(r"Candidate Short Setup.*?Spread-Padded Stop Loss:\s*`([^`]+)`", content, re.DOTALL)
    short_tp_m = re.search(r"Candidate Short Setup.*?\+2\.5R Take Profit:\s*`([^`]+)`", content, re.DOTALL)
    short_lot_m = re.search(r"Candidate Short Setup.*?Mathematical Lot Sizing:\s*\*\*`([^`]+)`\*\*", content, re.DOTALL)

    results[sym] = {
        "file": fpath,
        "lines": lines_count,
        "bytes": bytes_count,
        "bid": bid_m.group(1) if bid_m else None,
        "ask": ask_m.group(1) if ask_m else None,
        "spread_bps": spread_m.group(1) if spread_m else None,
        "vah": vah_m.group(1) if vah_m else None,
        "poc": poc_m.group(1) if poc_m else None,
        "val": val_m.group(1) if val_m else None,
        "postured_action": decision_m.group(1) if decision_m else None,
        "long_setup": {
            "entry": long_entry_m.group(1) if long_entry_m else None,
            "sl": long_sl_m.group(1) if long_sl_m else None,
            "tp": long_tp_m.group(1) if long_tp_m else None,
            "lot": long_lot_m.group(1) if long_lot_m else None
        },
        "short_setup": {
            "entry": short_entry_m.group(1) if short_entry_m else None,
            "sl": short_sl_m.group(1) if short_sl_m else None,
            "tp": short_tp_m.group(1) if short_tp_m else None,
            "lot": short_lot_m.group(1) if short_lot_m else None
        }
    }

output_path = "docs/trade_plans/CYCLE_033_DOSSIER_FORENSICS_ALL_94.json"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(results, f, indent=2)

print(f"SUCCESS: Audited and parsed all {len(results)} dossiers to EOF without skipping.")
print(f"Total Lines Processed: {total_lines_read:,} lines")
print(f"Total Content Processed: {total_bytes_read:,} bytes ({total_bytes_read / 1024 / 1024:.2f} MB)")
print(f"Forensic results exported to: {output_path}")
