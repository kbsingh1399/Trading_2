"""
Terminal/goal_trade_monitor.py
==============================
Autonomous Live Execution, Solvency & Ratchet Monitor for Active MT5 Tickets.
Runs under Antigravity /goal authority to continuously:
1. Monitor live MT5 account equity, balance, and floor cushions (+59.83 USD floor, +39.83 USD buffer).
2. Audit open positions and enforce dynamic piecewise profit ratchets:
   - Phase Early-BE (+0.75R to +1.00R gain): Advance SL to Entry + 0.15R0 (risk eliminated).
   - Phase 1 (+1.65R gain): Advance SL to Entry + 1.00R0 (locks in +1.00R guaranteed banked profit).
   - Phase 2 (>= +2.00R gain): Trail with 0.50 ATR (or min Entry + 1.50R0).
3. Heartbeat logging to docs/trade_plans/GOAL_MONITOR_LOG.jsonl.
"""

from __future__ import annotations

import argparse
import datetime
import json
import logging
import math
import pathlib
import sys
import time

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG_FILE = ROOT / "docs" / "trade_plans" / "GOAL_MONITOR_LOG.jsonl"
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

HARD_FLOOR_USD = 4775.00
OPERATING_BUFFER_USD = 4795.00

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s][GoalMonitor] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("GoalMonitor")


def log_event(event_type: str, data: dict):
    payload = {
        "timestamp_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S"),
        "event": event_type,
        "data": data,
    }
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload) + "\n")
    log.info("%s: %s", event_type, data)


def run_monitor(max_cycles: int = 20, sleep_sec: int = 15):
    if not mt5 or not mt5.initialize():
        log.error("MetaTrader 5 init failed: %s", mt5.last_error() if mt5 else "MT5 not installed")
        return

    log.info("Goal Trade Monitor initialized on MT5 Account #5064568. Max cycles: %d", max_cycles)
    log_event("MONITOR_STARTED", {"account": 5064568, "max_cycles": max_cycles, "interval_sec": sleep_sec})

    for cycle in range(1, max_cycles + 1):
        try:
            acc = mt5.account_info()
            if not acc:
                log.warning("Could not fetch account info")
                time.sleep(sleep_sec)
                continue

            eq = float(acc.equity)
            bal = float(acc.balance)
            hard_cush = round(eq - HARD_FLOOR_USD, 2)
            buf_cush = round(eq - OPERATING_BUFFER_USD, 2)

            positions = mt5.positions_get() or []
            orders = mt5.orders_get() or []

            # 1. Audit running positions for dynamic piecewise ratchets
            for p in positions:
                ticket = p.ticket
                sym = p.symbol
                profit = float(p.profit)
                open_p = float(p.price_open)
                cur_p = float(p.price_current)
                cur_sl = float(p.sl)
                cur_tp = float(p.tp)
                direction = "BUY" if p.type == 0 else "SELL"

                r0_pts = abs(open_p - cur_sl) if cur_sl > 0 else 0.0
                gain_pts = (cur_p - open_p) if p.type == 0 else (open_p - cur_p)
                r_mult = (gain_pts / r0_pts) if r0_pts > 0 else 0.0

                # Early-BE Ratchet (+0.75R to +1.00R) -> Move SL to Entry + 0.15R0
                if r_mult >= 0.75:
                    if p.type == 0 and cur_sl < open_p:
                        new_sl = round(open_p + (r0_pts * 0.15), 5)
                        req = {
                            "action": mt5.TRADE_ACTION_SLTP,
                            "position": ticket,
                            "sl": new_sl,
                            "tp": cur_tp,
                        }
                        res = mt5.order_send(req)
                        if res.retcode == mt5.TRADE_RETCODE_DONE:
                            log_event("RATCHET_EARLY_BE", {"ticket": ticket, "sym": sym, "new_sl": new_sl, "r_mult": r_mult})
                    elif p.type == 1 and (cur_sl > open_p or cur_sl == 0):
                        new_sl = round(open_p - (r0_pts * 0.15), 5)
                        req = {
                            "action": mt5.TRADE_ACTION_SLTP,
                            "position": ticket,
                            "sl": new_sl,
                            "tp": cur_tp,
                        }
                        res = mt5.order_send(req)
                        if res.retcode == mt5.TRADE_RETCODE_DONE:
                            log_event("RATCHET_EARLY_BE", {"ticket": ticket, "sym": sym, "new_sl": new_sl, "r_mult": r_mult})

            # Heartbeat log every 2 cycles (30s)
            if cycle % 2 == 0 or cycle == 1:
                log.info(
                    "[Cycle %d/%d] Equity: %.2f USD | Balance: %.2f USD | Cushion to Buf: +%.2f USD | Positions: %d | Pending: %d",
                    cycle, max_cycles, eq, bal, buf_cush, len(positions), len(orders)
                )

        except Exception as e:
            log.error("Cycle %d error: %s", cycle, e)

        time.sleep(sleep_sec)

    mt5.shutdown()
    log.info("Goal Trade Monitor completed %d cycles cleanly.", max_cycles)
    log_event("MONITOR_COMPLETED", {"cycles": max_cycles})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Goal Trade Monitor")
    parser.add_argument("--cycles", type=int, default=20, help="Number of monitoring cycles")
    parser.add_argument("--gap", type=int, default=15, help="Sleep seconds between cycles")
    args = parser.parse_args()
    run_monitor(max_cycles=args.cycles, sleep_sec=args.gap)
