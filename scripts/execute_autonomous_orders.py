import MetaTrader5 as mt5
import sys

def run_execution():
    if not mt5.initialize():
        print("MT5 initialization failed:", mt5.last_error())
        sys.exit(1)

    print("Account:", mt5.account_info().login)

    # 1. Cancel ticket #19489161 (USWTI.p)
    target_ticket = 19489161
    orders = mt5.orders_get()
    found = False
    if orders:
        for o in orders:
            if o.ticket == target_ticket:
                found = True
                req = {
                    "action": mt5.TRADE_ACTION_REMOVE,
                    "order": target_ticket
                }
                res = mt5.order_send(req)
                print(f"Cancel order #{target_ticket} ({o.symbol}): retcode={res.retcode}, comment={res.comment}")
                break
    if not found:
        print(f"Ticket #{target_ticket} not found or already closed/removed.")

    # 2. Check AUDUSD.pi specifications
    sym = "AUDUSD.pi"
    info = mt5.symbol_info(sym)
    if not info:
        print(f"Symbol {sym} not found on MT5!")
        mt5.shutdown()
        return

    if not info.visible:
        mt5.symbol_select(sym, True)
        info = mt5.symbol_info(sym)

    tick = mt5.symbol_info_tick(sym)
    print(f"{sym} info: Digits={info.digits}, Point={info.point}, MinLot={info.volume_min}, Step={info.volume_step}")
    print(f"{sym} live tick: Bid={tick.bid}, Ask={tick.ask}, Spread={(tick.ask - tick.bid)/info.point:.1f} pts")

    # 3. Stage AUDUSD.pi BUY_LIMIT
    # Price: 0.70270 | SL: 0.70150 | TP: 0.70570 | Lot: 0.08
    entry_price = round(0.70270, info.digits)
    sl_price = round(0.70150, info.digits)
    tp_price = round(0.70570, info.digits)
    lot_size = 0.08

    # Ensure entry is below current ask for a buy limit
    if entry_price >= tick.ask:
        print(f"Warning: Entry {entry_price} >= Ask {tick.ask}. Adjusting to ensure passive maker entry.")
        entry_price = round(tick.bid - 0.00050, info.digits)
        sl_price = round(entry_price - 0.00120, info.digits)
        tp_price = round(entry_price + 0.00300, info.digits)

    # Risk calculation: distance * contract_size * lot
    # contract_size = 100,000. 0.00120 * 100,000 * 0.08 = 9.60 USD
    risk_pts = abs(entry_price - sl_price)
    nominal_risk_usd = risk_pts * info.trade_contract_size * lot_size
    print(f"Proposed {sym} BUY_LIMIT: Entry={entry_price}, SL={sl_price}, TP={tp_price}, Lots={lot_size}, Risk={nominal_risk_usd:.2f} USD")

    req_order = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": sym,
        "volume": lot_size,
        "type": mt5.ORDER_TYPE_BUY_LIMIT,
        "price": entry_price,
        "sl": sl_price,
        "tp": tp_price,
        "deviation": 10,
        "magic": 20261030,
        "comment": "TriCouncil C11 AUDUSD",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN
    }

    res_order = mt5.order_send(req_order)
    print(f"Order Send Result: retcode={res_order.retcode}, order={res_order.order}, comment={res_order.comment}")

    # 4. Print final state of pending orders
    updated_orders = mt5.orders_get()
    print(f"\nTotal Pending Orders Active: {len(updated_orders) if updated_orders else 0}")
    if updated_orders:
        for u in updated_orders:
            print(f"  Ticket: {u.ticket} | {u.symbol} | Type: {u.type} | Lots: {u.volume_current} | Entry: {u.price_open} | SL: {u.sl} | TP: {u.tp}")

    mt5.shutdown()

if __name__ == "__main__":
    run_execution()
