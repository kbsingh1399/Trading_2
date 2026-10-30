import MetaTrader5 as mt5

if not mt5.initialize():
    print("MT5 Init failed:", mt5.last_error())
    exit(1)

orders = [
    {'symbol': 'BTCUSD.pi', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 81084.0, 'sl': 81446.0, 'tp': 80180.0, 'volume': 0.01},
    {'symbol': 'USDJPY.pi', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 157.970, 'sl': 158.080, 'tp': 157.710, 'volume': 0.13},
    {'symbol': 'BNBUSD.p', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 753.30, 'sl': 757.20, 'tp': 743.50, 'volume': 0.05},
    {'symbol': 'XAUUSD.pi', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 4040.50, 'sl': 4049.50, 'tp': 4018.00, 'volume': 0.01},
    {'symbol': 'NAS100.p', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 29535.0, 'sl': 29620.0, 'tp': 29320.0, 'volume': 0.01},
    {'symbol': 'DJ30.p', 'type': mt5.ORDER_TYPE_SELL_LIMIT, 'entry': 52638.0, 'sl': 52732.0, 'tp': 52402.0, 'volume': 0.01},
    {'symbol': 'USWTI.p', 'type': mt5.ORDER_TYPE_BUY_LIMIT, 'entry': 101.55, 'sl': 100.99, 'tp': 102.93, 'volume': 0.01}
]

for o in orders:
    sym = o['symbol']
    side = mt5.ORDER_TYPE_SELL if 'SELL' in str(o['type']) else mt5.ORDER_TYPE_BUY
    p_loss = mt5.order_calc_profit(side, sym, o['volume'], o['entry'], o['sl'])
    p_gain = mt5.order_calc_profit(side, sym, o['volume'], o['entry'], o['tp'])
    loss_usd = abs(p_loss) if p_loss is not None else 0.0
    gain_usd = p_gain if p_gain is not None else 0.0
    print(f"{sym:12} | Vol: {o['volume']:4.2f} | Risk: {loss_usd:5.2f} USD | Gain: {gain_usd:5.2f} USD")

mt5.shutdown()
