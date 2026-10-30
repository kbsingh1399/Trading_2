import MetaTrader5 as mt5
import json, sys, datetime

sys.stdout.reconfigure(encoding='utf-8')

print("=" * 80)
print("🚀 EXECUTING INSTITUTIONAL MAKER LIMIT ORDERS ON BLUEBERRY MARKETS MT5")
print("   Operator Mandate: Hard floor lifted. Active high-confluence trading active.")
print("=" * 80)

if not mt5.initialize():
    print(f"❌ MT5 initialization failed: {mt5.last_error()}")
    sys.exit(1)

acc = mt5.account_info()
print(f"Connected to Account: #{acc.login} ({acc.server})")
print(f"Balance: ${acc.balance:.2f} USD | Equity: ${acc.equity:.2f} USD | Free Margin: ${acc.margin_free:.2f} USD")

# Verify current open and pending orders
positions = mt5.positions_get()
orders = mt5.orders_get()
print(f"Current Active Positions: {len(positions)} | Current Pending Orders: {len(orders)}")

orders_to_punch = [
    {
        "symbol": "BTCUSD.pi",
        "action": mt5.ORDER_TYPE_BUY_LIMIT,
        "action_str": "BUY_LIMIT",
        "volume": 0.01,
        "price": 76350.00,
        "sl": 75850.00,
        "tp": 77600.00,
        "comment": "C35_BTC_2.5R_GVT",
        "expected_risk_usd": 5.00
    },
    {
        "symbol": "XMRUSD.p",
        "action": mt5.ORDER_TYPE_BUY_LIMIT,
        "action_str": "BUY_LIMIT",
        "volume": 0.01,
        "price": 585.50,
        "sl": 577.50,
        "tp": 605.50,
        "comment": "C35_XMR_2.5R_GVT",
        "expected_risk_usd": 8.00
    },
    {
        "symbol": "AVEUSD.p",
        "action": mt5.ORDER_TYPE_BUY_LIMIT,
        "action_str": "BUY_LIMIT",
        "volume": 0.07,
        "price": 122.50,
        "sl": 121.20,
        "tp": 125.75,
        "comment": "C35_AVE_2.5R_GVT",
        "expected_risk_usd": 9.10
    }
]

punched_results = []
for o in orders_to_punch:
    sym = o["symbol"]
    s_info = mt5.symbol_info(sym)
    if not s_info:
        print(f"❌ Symbol {sym} not found in MT5!")
        continue
    if not s_info.visible:
        mt5.symbol_select(sym, True)

    tick = mt5.symbol_info_tick(sym)
    print(f"\nStaging {o['action_str']} on {sym}:")
    print(f"  Live Mid: {(tick.bid + tick.ask)/2:.4f} (Bid {tick.bid} / Ask {tick.ask})")
    print(f"  Limit Price: {o['price']} | SL: {o['sl']} | TP: {o['tp']} | Lots: {o['volume']}")

    request = {
        "action": mt5.TRADE_ACTION_PENDING,
        "symbol": sym,
        "volume": o["volume"],
        "type": o["action"],
        "price": o["price"],
        "sl": o["sl"],
        "tp": o["tp"],
        "deviation": 20,
        "magic": 20261035,
        "comment": o["comment"],
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }

    result = mt5.order_send(request)
    if result.retcode == mt5.TRADE_RETCODE_DONE:
        print(f"  ✅ SUCCESS: Order placed! Ticket #{result.order} | Retcode: {result.retcode}")
        punched_results.append({
            "ticket": result.order,
            "symbol": sym,
            "action": o["action_str"],
            "volume": o["volume"],
            "price": o["price"],
            "sl": o["sl"],
            "tp": o["tp"],
            "retcode": result.retcode,
            "nominal_risk_usd": o["expected_risk_usd"],
            "status": "ACTIVE_RESTING_ORDER"
        })
    else:
        print(f"  ❌ FAILED: Retcode {result.retcode} ({result.comment})")
        punched_results.append({
            "symbol": sym,
            "retcode": result.retcode,
            "comment": result.comment,
            "status": "REJECTED"
        })

mt5.shutdown()

output_path = ROOT / "docs" / "trade_plans" / "CYCLE_035_EXECUTION_RECEIPTS.json"
output_path.write_text(json.dumps(punched_results, indent=2), encoding="utf-8")
print(f"\nExecution summary saved to {output_path}")
print("=" * 80)
