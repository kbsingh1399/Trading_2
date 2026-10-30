import MetaTrader5 as mt5
import pandas as pd
import json
import os
import glob
from datetime import datetime

if not mt5.initialize():
    print("MT5 init failed")
    exit(1)

account_info = mt5.account_info()._asdict()
print(f"ACCOUNT_ID: {account_info['login']}")
print(f"BALANCE: {account_info['balance']}")
print(f"EQUITY: {account_info['equity']}")
print(f"MARGIN: {account_info['margin']}")
print(f"MARGIN_FREE: {account_info['margin_free']}")

positions = mt5.positions_get()
print(f"\n--- OPEN POSITIONS ({len(positions) if positions else 0}) ---")
if positions:
    for p in positions:
        d = p._asdict()
        print(f"Position Ticket: {d['ticket']}, Symbol: {d['symbol']}, Type: {d['type']}, Volume: {d['volume']}, Open: {d['price_open']}, Current: {d['price_current']}, SL: {d['sl']}, TP: {d['tp']}, Profit: {d['profit']}")

orders = mt5.orders_get()
print(f"\n--- RESTING PENDING ORDERS ({len(orders) if orders else 0}) ---")
active_orders = []
if orders:
    for o in orders:
        d = o._asdict()
        order_type_str = "BUY_LIMIT" if d['type'] == 2 else ("SELL_LIMIT" if d['type'] == 3 else str(d['type']))
        print(f"Ticket: {d['ticket']}, Symbol: {d['symbol']}, Type: {order_type_str}, Vol: {d['volume_current']}, Price: {d['price_open']}, SL: {d['sl']}, TP: {d['tp']}")
        active_orders.append(d)

mt5.shutdown()
