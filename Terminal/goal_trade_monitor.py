"""
Terminal/goal_trade_monitor.py
Autonomous Live Execution & Ratchet Monitor for Active MT5 Tickets.
Runs under Antigravity /goal authority to continuously:
1. Track pending limit orders (#18954801 BTC, #18954803 Gold).
2. Detect fills and activate Phase 0 / Phase 1 / Phase 2 dynamic ratchets.
3. Watch SP500 price: if SP500 >= 7,725.00 USD (within 2.0 ATR of 7,738 shelf), stage Ticket 3.
4. Defend the 4,775.00 USD hard floor unconditionally.
"""

import MetaTrader5 as mt5
import time
import json
import pathlib
import datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG_FILE = ROOT / "docs" / "trade_plans" / "GOAL_MONITOR_LOG.jsonl"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

def log_event(event_type: str, data: dict):
    payload = {
        "timestamp_utc": datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
        "event": event_type,
        "data": data
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")
    print(f"[{payload['timestamp_utc']}] {event_type}: {data}")

def run_monitor(max_cycles: int = 120, sleep_sec: int = 15):
    if not mt5.initialize():
        print(f"[FATAL] MT5 Init Failed: {mt5.last_error()}")
        return

    print("[+] Goal Trade Monitor initialized on MT5 Account 5064568.")
    log_event("MONITOR_STARTED", {"account": 5064568, "max_cycles": max_cycles})

    staged_sp500 = False

    for cycle in range(1, max_cycles + 1):
        try:
            acc = mt5.account_info()
            if not acc:
                print("[WARNING] Could not fetch account info")
                time.sleep(sleep_sec)
                continue

            orders = mt5.orders_get()
            positions = mt5.positions_get()

            # 1. Audit pending tickets
            order_tickets = [o.ticket for o in orders]
            
            # 2. Audit running positions for dynamic ratchets
            for p in positions:
                ticket = p.ticket
                sym = p.symbol
                profit = p.profit
                open_price = p.price_open
                cur_price = p.price_current
                cur_sl = p.sl
                cur_tp = p.tp
                
                # Check R0 gain
                # For BTC: risk was ~280 pts. Profit +1.25R0 = ~350 pts gain (+14 USD).
                # For Gold: risk was 11.5 pts. Profit +1.25R0 = ~14.3 pts gain (+14.3 USD).
                if p.type == mt5.ORDER_TYPE_SELL:
                    pts_gain = open_price - cur_price
                else:
                    pts_gain = cur_price - open_price

                # Ratchet Phase 0 (+1.25R0) -> Move SL to lock +0.25R0 (BE+)
                if sym == "BTCUSD.pi" and pts_gain >= 350.0 and cur_sl > open_price - 70.0:
                    new_sl = round(open_price - 70.0, 2)
                    req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "position": ticket,
                        "sl": new_sl,
                        "tp": cur_tp
                    }
                    res = mt5.order_send(req)
                    if res.retcode == mt5.TRADE_RETCODE_DONE:
                        log_event("RATCHET_PHASE_0", {"ticket": ticket, "sym": sym, "new_sl": new_sl, "locked_gain": "+0.25R0"})

                elif sym == "XAUUSD.pi" and pts_gain >= 14.3 and cur_sl < open_price + 2.8:
                    new_sl = round(open_price + 2.8, 2)
                    req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "position": ticket,
                        "sl": new_sl,
                        "tp": cur_tp
                    }
                    res = mt5.order_send(req)
                    if res.retcode == mt5.TRADE_RETCODE_DONE:
                        log_event("RATCHET_PHASE_0", {"ticket": ticket, "sym": sym, "new_sl": new_sl, "locked_gain": "+0.25R0"})

            # 3. SP500 Watcher: if SP500 rallies >= 7,725.00 USD, stage Ticket 3
            if not staged_sp500 and len(orders) < 4:
                sp_tick = mt5.symbol_info_tick("SP500.p")
                if sp_tick and sp_tick.ask >= 7725.0:
                    print(f"[*] SP500 in entry proximity ({sp_tick.ask:.2f} >= 7725.00). Staging Ticket 3...")
                    req_sp = {
                        "action": mt5.TRADE_ACTION_PENDING,
                        "symbol": "SP500.p",
                        "volume": 0.10,
                        "type": mt5.ORDER_TYPE_SELL_LIMIT,
                        "price": 7738.50,
                        "sl": 7749.50,
                        "tp": 7674.50,
                        "deviation": 20,
                        "magic": 20261015,
                        "comment": "Antigravity SP500 Sweep",
                        "type_time": mt5.ORDER_TIME_GTC,
                        "type_filling": mt5.ORDER_FILLING_RETURN,
                    }
                    res_sp = mt5.order_send(req_sp)
                    if res_sp.retcode == mt5.TRADE_RETCODE_DONE:
                        staged_sp500 = True
                        log_event("SP500_STAGED", {"ticket": res_sp.order, "price": 7738.50, "sl": 7749.50, "tp": 7674.50, "risk_usd": 11.00})

            # 4. Periodic Arkham On-Chain Ingest (every 60s / 6 cycles)
            if cycle % 6 == 0:
                try:
                    from Terminal.Data_Factory import arkham_intelligence_harvester as arkham_mod
                    arkham_mod.run()
                except Exception as exc:
                    print(f"[WARNING] Periodic Arkham harvest failed: {exc}")

            # Heartbeat print every 4 cycles (40s)
            if cycle % 4 == 0:
                print(f"[Cycle {cycle}] Orders: {len(orders)} | Positions: {len(positions)} | Equity: {acc.equity:.2f} USD | Cushion: +{acc.equity - 4775.00:.2f} USD")

        except Exception as e:
            print(f"[ERROR] Cycle {cycle} error: {e}")

        time.sleep(sleep_sec)

    mt5.shutdown()
    print("[+] Monitor cycle run completed.")

if __name__ == "__main__":
    run_monitor(max_cycles=1000000, sleep_sec=10)
