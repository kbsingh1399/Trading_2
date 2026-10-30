import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/telemetry/live_snapshot_latest.json', 'r', encoding='utf-8') as f:
    snap = json.load(f)

print("Live snapshot timestamp:", snap.get("timestamp_utc"))
print("Account:", snap.get("account"))
print("Open positions count:", len(snap.get("open_positions", [])))
print("Pending orders count:", len(snap.get("pending_orders", [])))
for o in snap.get("pending_orders", []):
    print(f"  Ticket #{o.get('ticket')}: {o.get('symbol')} {o.get('type')} @ {o.get('price_open')} | SL: {o.get('sl')} | TP: {o.get('tp')}")
