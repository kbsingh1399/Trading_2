import MetaTrader5 as mt5

def update_orders():
    if not mt5.initialize():
        print("MT5 initialization failed")
        return
        
    orders = mt5.orders_get()
    if not orders:
        print("No active orders found")
        mt5.shutdown()
        return
        
    print(f"Found {len(orders)} active resting orders.")
    
    # Target updates:
    # 1. BTCUSD.pi (Ticket #19489155): Update SL from 81446.0 to 81680.0 (Above Max Pain 81494.86 and Liq band 81553.0)
    # 2. BNBUSD.p (Ticket #19489157): Update SL from 757.2 to 761.5 (Above Max Pain 758.31 and Liq band 759.90)
    
    for o in orders:
        d = o._asdict()
        ticket = d['ticket']
        symbol = d['symbol']
        price = d['price_open']
        sl = d['sl']
        tp = d['tp']
        vol = d['volume_current']
        
        new_sl = None
        if ticket == 19489155 or symbol == 'BTCUSD.pi':
            new_sl = 81680.0
            print(f"Modifying Ticket {ticket} ({symbol}): Old SL={sl} -> New SL={new_sl} (Cleared Max Pain 81494.86 & Liq 81553.0)")
        elif ticket == 19489157 or symbol == 'BNBUSD.p':
            new_sl = 761.50
            print(f"Modifying Ticket {ticket} ({symbol}): Old SL={sl} -> New SL={new_sl} (Cleared Max Pain 758.31 & Liq 759.90)")
            
        if new_sl is not None:
            request = {
                "action": mt5.TRADE_ACTION_MODIFY,
                "order": ticket,
                "price": price,
                "sl": new_sl,
                "tp": tp,
                "type_time": d['type_time'],
                "type_filling": d['type_filling']
            }
            res = mt5.order_send(request)
            if res.retcode == mt5.TRADE_RETCODE_DONE:
                print(f"SUCCESS: Ticket {ticket} modified! Retcode={res.retcode}, New SL={new_sl}")
            else:
                print(f"ERROR: Ticket {ticket} modification failed! Retcode={res.retcode}, Comment={res.comment}")
                
    # Print final orders
    updated_orders = mt5.orders_get()
    print("\n--- FINAL VERIFIED ACTIVE RESTING ORDERS ON MT5 ---")
    for o in updated_orders:
        d = o._asdict()
        print(f"Ticket: {d['ticket']}, Symbol: {d['symbol']}, Vol: {d['volume_current']}, Price: {d['price_open']}, SL: {d['sl']}, TP: {d['tp']}")
        
    mt5.shutdown()

if __name__ == "__main__":
    update_orders()
