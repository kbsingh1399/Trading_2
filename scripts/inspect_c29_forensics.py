import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/trade_plans/CYCLE_029_DOSSIER_FORENSICS_ALL_96.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total records: {len(data)}")
decisions = {}
for d in data:
    dec = d['decision']
    decisions[dec] = decisions.get(dec, 0) + 1
print("Decisions summary:", decisions)

sectors = {}
for d in data:
    sec = d['sector']
    sectors[sec] = sectors.get(sec, 0) + 1
print("Sectors breakdown:", sectors)

active_setups = [d for d in data if d['decision'] == 'PASSIVE_MAKER_LIMIT_ARMED']
print(f"Active maker limit setups: {len(active_setups)}")
for a in active_setups[:25]:
    sym = a['symbol']
    sec = a['sector']
    entry = a['entry']
    sl = a['sl']
    tp = a['tp']
    risk = a['risk_usd']
    print(f"{sym:<12} | {sec:<28} | Entry: {entry} | SL: {sl} | TP: {tp} | Risk: {risk} USD")
