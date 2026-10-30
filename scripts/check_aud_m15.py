import MetaTrader5 as mt5
import datetime

if mt5.initialize():
    rates = mt5.copy_rates_from_pos('AUDUSD.pi', mt5.TIMEFRAME_M15, 0, 5)
    for r in rates:
        dt = datetime.datetime.fromtimestamp(r['time'], datetime.timezone.utc)
        print(f"{dt} UTC | High: {r['high']} | Low: {r['low']} | Close: {r['close']}")
    mt5.shutdown()
