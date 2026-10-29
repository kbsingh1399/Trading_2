import MetaTrader5 as mt5

if not mt5.initialize():
    print('MT5 Init Failed')
    quit()

acc = mt5.account_info()._asdict()
pos = [p._asdict() for p in mt5.positions_get()]
orders = [o._asdict() for o in mt5.orders_get()]
mt5.shutdown()

print('=== ACCOUNT ===')
print('Balance:', acc['balance'], 'Equity:', acc['equity'], 'FreeMargin:', acc['margin_free'])
print('=== POSITIONS ===')
for p in pos:
    print(p['ticket'], p['symbol'], p['type'], p['volume'], p['price_open'], p['price_current'], p['sl'], p['tp'], p['profit'])
print('=== ORDERS ===')
for o in orders:
    print(o['ticket'], o['symbol'], o['type'], o['volume_initial'], o['price_open'], o['sl'], o['tp'])
