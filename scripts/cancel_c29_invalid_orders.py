import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge

sys.stdout.reconfigure(encoding='utf-8')

bridge = MT5ExecutionBridge()
if not bridge.ensure_connected():
    print("ERROR: Failed to connect to MT5 terminal.")
    sys.exit(1)

tickets_to_cancel = [19489155, 19489157]
print(f"Executing cancellation of tickets failing 2.5R minimum mandate: {tickets_to_cancel}")

for ticket in tickets_to_cancel:
    res = bridge.cancel_pending_order(ticket)
    print(f"Ticket #{ticket} cancellation result: {res}")

# Check remaining orders
orders = bridge.get_pending_orders()
print(f"\nRemaining pending orders on MT5 ({len(orders)}):")
for o in orders:
    print(f"  Ticket #{o['ticket']}: {o['symbol']} {o['direction']} @ {o['price_open']} | SL: {o['sl']} | TP: {o['tp']}")
