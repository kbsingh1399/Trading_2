import MetaTrader5 as mt5
import json

def punch_orders():
    if not mt5.initialize():
        print(f"MT5 Init failed: {mt5.last_error()}")
        return

    orders_to_punch = [
        {
            "symbol": "BTCUSD.pi",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 81084.00,
            "sl": 81446.00,
            "tp": 80180.00,
            "comment": "TC_BTC_VAH_Fade"
        },
        {
            "symbol": "USDJPY.pi",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.13,
            "price": 157.970,
            "sl": 158.080,
            "tp": 157.710,
            "comment": "TC_UJ_VAH_Fade"
        },
        {
            "symbol": "BNBUSD.p",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.05,
            "price": 753.30,
            "sl": 757.20,
            "tp": 743.50,
            "comment": "TC_BNB_Wall_Fade"
        },
        {
            "symbol": "XAUUSD.pi",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 4040.50,
            "sl": 4049.50,
            "tp": 4018.00,
            "comment": "TC_XAU_VAH_Fade"
        },
        {
            "symbol": "NAS100.p",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 29535.00,
            "sl": 29620.00,
            "tp": 29320.00,
            "comment": "TC_NAS_VAH_Fade"
        },
        {
            "symbol": "DJ30.p",
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 52638.00,
            "sl": 52732.00,
            "tp": 52402.00,
            "comment": "TC_DJ_VAH_Fade"
        },
        {
            "symbol": "USWTI.p",
            "type": mt5.ORDER_TYPE_BUY_LIMIT,
            "volume": 0.01,
            "price": 101.550,
            "sl": 100.990,
            "tp": 102.930,
            "comment": "TC_WTI_VAL_Fade"
        }
    ]

    results = []
    for req_data in orders_to_punch:
        sym = req_data["symbol"]
        mt5.symbol_select(sym, True)
        tick = mt5.symbol_info_tick(sym)
        if not tick:
            print(f"No tick for {sym}")
            results.append({"symbol": sym, "status": "NO_TICK"})
            continue

        request = {
            "action": mt5.TRADE_ACTION_PENDING,
            "symbol": sym,
            "volume": req_data["volume"],
            "type": req_data["type"],
            "price": req_data["price"],
            "sl": req_data["sl"],
            "tp": req_data["tp"],
            "deviation": 20,
            "magic": 20261030,
            "comment": req_data["comment"],
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }

        res = mt5.order_send(request)
        if res and res.retcode == mt5.TRADE_RETCODE_DONE:
            msg = f"SUCCESS: Punched #{res.order} {sym} {req_data['volume']} lots @ {req_data['price']} | SL: {req_data['sl']} | TP: {req_data['tp']}"
            print(msg)
            results.append({"symbol": sym, "status": "PUNCHED", "ticket": res.order, "price": req_data["price"], "volume": req_data["volume"], "sl": req_data["sl"], "tp": req_data["tp"]})
        else:
            err_msg = f"FAILED {sym}: retcode={getattr(res, 'retcode', -1)}, comment={getattr(res, 'comment', 'N/A')}"
            print(err_msg)
            results.append({"symbol": sym, "status": "FAILED", "retcode": getattr(res, "retcode", -1), "comment": getattr(res, "comment", "N/A")})

    mt5.shutdown()
    with open("Data/punched_orders_receipt.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

if __name__ == "__main__":
    punch_orders()
