import MetaTrader5 as mt5
import pandas as pd

mt5.initialize()

for sym in ['NAS100.p', 'DJ30.p', 'AUDUSD.pi']:
    s = mt5.symbol_info(sym)
    t = mt5.symbol_info_tick(sym)
    print(f"Symbol: {sym} | Bid: {t.bid} | Ask: {t.ask} | Digits: {s.digits} | Point: {s.point} | Contract Size: {s.trade_contract_size} | Tick Value: {s.trade_tick_value}")

mt5.shutdown()
