import MetaTrader5 as mt5
import sys
import json
import time

sys.stdout.reconfigure(encoding='utf-8')

def punch_orders():
    if not mt5.initialize():
        print("Failed to initialize MT5")
        sys.exit(1)
        
    acc = mt5.account_info()
    print(f"MT5 Account #{acc.login} | Balance: {acc.balance} | Equity: {acc.equity}")
    
    # 3 High-Confluence Maker Limit Orders
    orders_to_place = [
        {
            "symbol": "BTCUSD.pi",
            "action": mt5.TRADE_ACTION_PENDING,
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.02,
            "price": 78962.0,
            "sl": 79318.0,
            "tp": 78072.0,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "comment": "C032_TriCouncil_BTC",
            "magic": 32001
        },
        {
            "symbol": "XAUUSD.pi",
            "action": mt5.TRADE_ACTION_PENDING,
            "type": mt5.ORDER_TYPE_SELL_LIMIT,
            "volume": 0.01,
            "price": 4007.50,
            "sl": 4017.00,
            "tp": 3983.70,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "comment": "C032_TriCouncil_XAU",
            "magic": 32002
        },
        {
            "symbol": "AUDUSD.pi",
            "action": mt5.TRADE_ACTION_PENDING,
            "type": mt5.ORDER_TYPE_BUY_LIMIT,
            "volume": 0.15,
            "price": 0.70240,
            "sl": 0.70180,
            "tp": 0.70390,
            "type_filling": mt5.ORDER_FILLING_IOC,
            "comment": "C032_TriCouncil_AUD",
            "magic": 32003
        }
    ]
    
    results = []
    for req in orders_to_place:
        sym = req["symbol"]
        # Check symbol info and tick
        s_info = mt5.symbol_info(sym)
        if not s_info:
            print(f"Error: Symbol {sym} not found on broker")
            continue
        if not s_info.visible:
            mt5.symbol_select(sym, True)
            
        tick = mt5.symbol_info_tick(sym)
        print(f"\nPunching {sym}: Type={'SELL_LIMIT' if req['type'] == mt5.ORDER_TYPE_SELL_LIMIT else 'BUY_LIMIT'} | Price={req['price']} | SL={req['sl']} | TP={req['tp']} | Vol={req['volume']}")
        print(f"Live Tick: Bid={tick.bid} | Ask={tick.ask}")
        
        # Adjust filling mode based on symbol execution modes
        filling_mode = s_info.filling_mode
        if filling_mode & mt5.ORDER_FILLING_IOC:
            req["type_filling"] = mt5.ORDER_FILLING_IOC
        elif filling_mode & mt5.ORDER_FILLING_FOK:
            req["type_filling"] = mt5.ORDER_FILLING_FOK
        else:
            req["type_filling"] = mt5.ORDER_FILLING_RETURN

        res = mt5.order_send(req)
        if res.retcode == mt5.TRADE_RETCODE_DONE or res.retcode == 10009:
            print(f"✅ SUCCESS: Ticket #{res.order} placed successfully on MT5! (retcode={res.retcode})")
            results.append({"symbol": sym, "ticket": res.order, "status": "ACTIVE_ON_BROKER", "price": req["price"], "sl": req["sl"], "tp": req["tp"], "volume": req["volume"]})
        else:
            print(f"❌ FAILED to place order on {sym}: retcode={res.retcode}, comment='{res.comment}'")
            
    mt5.shutdown()
    return results

if __name__ == "__main__":
    punch_orders()
