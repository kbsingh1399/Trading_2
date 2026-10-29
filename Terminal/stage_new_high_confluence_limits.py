"""
Terminal/stage_new_high_confluence_limits.py
Stages top high-confluence maker limit orders on MT5.
"""

import MetaTrader5 as mt5
import json

def stage_orders():
    if not mt5.initialize():
        print(f"MT5 Init failed: {mt5.last_error()}")
        return

    orders_to_stage = [
        {
            "symbol": "XAUUSD.pi",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 4064.50,
            "sl": 4088.50,
            "tp": 3995.00,
            "comment": "Antigravity Gold VAH Sweep Fade"
        },
        {
            "symbol": "NAS100.p",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 29740.00,
            "sl": 30025.00,
            "tp": 29230.00,
            "comment": "Antigravity Nasdaq POC Exhaustion"
        },
        {
            "symbol": "GBPUSD.pi",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.08,
            "price": 1.33480,
            "sl": 1.33640,
            "tp": 1.33120,
            "comment": "Antigravity Cable Resistance Fade"
        }
    ]

    for req_data in orders_to_stage:
        sym = req_data["symbol"]
        mt5.symbol_select(sym, True)
        tick = mt5.symbol_info_tick(sym)
        if not tick:
            print(f"No tick for {sym}")
            continue

        request = {
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": sym,
            "volume": req_data["volume"],
            "type": req_data["type"],
            "price": req_data["price"],
            "sl": req_data["sl"],
            "tp": req_data["tp"],
            "deviation": 10,
            "magic": 20261029,
            "comment": req_data["comment"],
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        res = mt5.order_send(request)
        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
            print(f"SUCCESS: Staged #{res.order} {sym} {req_data['volume']} @ {req_data['price']} | SL: {req_data['sl']} | TP: {req_data['tp']}")
        else:
            print(f"FAILED {sym}: retcode={getattr(res, 'retcode', -1)}, comment={getattr(res, 'comment', 'N/A')}")

    mt5.shutdown()

if __name__ == "__main__":
    stage_orders()
