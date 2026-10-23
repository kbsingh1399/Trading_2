"""
Terminal/goal_trade_monitor.py
==============================
Autonomous Live Execution, Solvency & Ratchet Monitor for Active MT5 Tickets.
Runs under Antigravity /goal authority to continuously:
1. Monitor live MT5 account equity, balance, and floor cushions (+210 USD floor, +160 USD buffer).
2. Audit open positions and enforce dynamic piecewise profit ratchets:
   - Phase Early-BE (+0.75R to +1.00R gain): Advance SL to Entry + 0.15R0 (risk eliminated).
   - Phase 1 (+1.65R gain): Advance SL to Entry + 1.00R0 (locks in +1.00R guaranteed banked profit).
   - Phase 2 (>= +2.20R gain): Advance SL to Entry + 1.60R0 (locks in +1.60R runner profit).
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

HARD_FLOOR_USD = 4600.00
OPERATING_BUFFER_USD = 4650.00

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


def run_monitor(max_cycles: int = 20, sleep_sec: int = 15, daemon: bool = False):
    if not mt5 or not mt5.initialize():
        log.error("MetaTrader 5 init failed: %s", mt5.last_error() if mt5 else "MT5 not installed")
        return

    mode_str = "DAEMON (INFINITE)" if daemon else f"{max_cycles} cycles"
    log.info("Goal Trade Monitor initialized on MT5 Account #5064568. Mode: %s | Gap: %ds", mode_str, sleep_sec)
    log_event("MONITOR_STARTED", {"account": 5064568, "daemon": daemon, "max_cycles": max_cycles, "interval_sec": sleep_sec})

    initial_r0_cache: dict[int, float] = {}
    last_known_positions: set[int] = set()

    cycle = 0
    while True:
        cycle += 1
        if not daemon and cycle > max_cycles:
            break
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
            current_tickets = {p.ticket for p in positions}

            # Check if any tracked position closed
            closed_tickets = last_known_positions - current_tickets
            for c_ticket in closed_tickets:
                log_event("POSITION_CLOSED", {"ticket": c_ticket, "balance": bal, "equity": eq})
                log.info("Position ticket #%d closed. New Balance: %.2f USD | Equity: %.2f USD", c_ticket, bal, eq)
                if c_ticket in initial_r0_cache:
                    del initial_r0_cache[c_ticket]
            last_known_positions = current_tickets

            # 1. Audit running positions for dynamic piecewise ratchets
            for p in positions:
                ticket = p.ticket
                sym = p.symbol
                profit = float(p.profit)
                open_p = float(p.price_open)
                cur_p = float(p.price_current)
                cur_sl = float(p.sl)
                cur_tp = float(p.tp)
                is_buy = (p.type == 0)

                # Initialize & preserve immutable R0 risk distance
                if ticket not in initial_r0_cache:
                    if cur_sl > 0:
                        calc_r0 = (open_p - cur_sl) if is_buy else (cur_sl - open_p)
                        if calc_r0 > 0:
                            initial_r0_cache[ticket] = calc_r0
                        else:
                            initial_r0_cache[ticket] = 400.0 if "BTC" in sym else 10.0
                    else:
                        initial_r0_cache[ticket] = 400.0 if "BTC" in sym else 10.0
                    log.info("Ticket #%d registered with immutable R0: %.2f pts", ticket, initial_r0_cache[ticket])

                r0_pts = initial_r0_cache[ticket]
                gain_pts = (cur_p - open_p) if is_buy else (open_p - cur_p)
                r_mult = round(gain_pts / r0_pts, 3) if r0_pts > 0 else 0.0

                # Compute intended target stop loss based on ratchet phase
                target_sl = None
                ratchet_phase = None

                # Stage 3: Runner Lock (+2.20R gain -> Lock +1.60R)
                if r_mult >= 2.20:
                    target_sl = round(open_p + (r0_pts * 1.60), 5) if is_buy else round(open_p - (r0_pts * 1.60), 5)
                    ratchet_phase = "RATCHET_STAGE3_RUNNER"
                # Stage 2: Profit Lock (+1.65R gain -> Lock +1.00R)
                elif r_mult >= 1.65:
                    target_sl = round(open_p + (r0_pts * 1.00), 5) if is_buy else round(open_p - (r0_pts * 1.00), 5)
                    ratchet_phase = "RATCHET_STAGE2_PROFIT"
                # Stage 1: Early-BE Lock (+0.75R gain -> Lock +0.15R0)
                elif r_mult >= 0.75:
                    target_sl = round(open_p + (r0_pts * 0.15), 5) if is_buy else round(open_p - (r0_pts * 0.15), 5)
                    ratchet_phase = "RATCHET_STAGE1_EARLY_BE"

                # Check if target_sl tightens the current SL
                if target_sl is not None and ratchet_phase is not None:
                    should_modify = False
                    if is_buy:
                        should_modify = (cur_sl == 0 or cur_sl < target_sl)
                    else:
                        should_modify = (cur_sl == 0 or cur_sl > target_sl)

                    if should_modify:
                        req = {
                            "action": mt5.TRADE_ACTION_SLTP,
                            "position": ticket,
                            "sl": target_sl,
                            "tp": cur_tp,
                        }
                        res = mt5.order_send(req)
                        if res.retcode == mt5.TRADE_RETCODE_DONE:
                            log_event(ratchet_phase, {
                                "ticket": ticket,
                                "sym": sym,
                                "old_sl": cur_sl,
                                "new_sl": target_sl,
                                "r_mult": r_mult,
                                "profit": profit,
                            })
                            log.info("%s on #%d (%s): SL updated from %.2f -> %.2f (r_mult: %.2fR)",
                                     ratchet_phase, ticket, sym, cur_sl, target_sl, r_mult)
                        else:
                            log.warning("Failed to modify SL for #%d: retcode=%s", ticket, res.retcode)

            # Heartbeat log every 2 cycles (30s)
            if cycle % 2 == 0 or cycle == 1:
                log.info(
                    "[Cycle %d] Equity: %.2f USD | Balance: %.2f USD | Cushion to Buf: +%.2f USD | Positions: %d | Pending: %d",
                    cycle, eq, bal, buf_cush, len(positions), len(orders)
                )

        except Exception as e:
            log.error("Cycle %d error: %s", cycle, e)

        time.sleep(sleep_sec)

    mt5.shutdown()
    log.info("Goal Trade Monitor finished cleanly after %d cycles.", cycle)
    log_event("MONITOR_COMPLETED", {"cycles": cycle})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Goal Trade Monitor")
    parser.add_argument("--cycles", type=int, default=20, help="Number of monitoring cycles (ignored if --daemon)")
    parser.add_argument("--gap", type=int, default=15, help="Sleep seconds between cycles")
    parser.add_argument("--daemon", action="store_true", help="Run indefinitely as a persistent daemon")
    args = parser.parse_args()
    run_monitor(max_cycles=args.cycles, sleep_sec=args.gap, daemon=args.daemon)
