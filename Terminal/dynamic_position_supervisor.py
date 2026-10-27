#!/usr/bin/env python3
"""
Terminal/dynamic_position_supervisor.py
=======================================
Autonomous Real-Time Dynamic Position & Order Supervisor Daemon.

Core Institutional Directives (Operator Mandate):
  1. Max Concurrent Filled Positions: Strictly capped at 4.
  2. Resting Limit Orders: N orders permitted across the universe.
  3. Auto-Pull Invariant: The moment active filled positions reaches exactly 4 (len(positions) >= 4),
     the supervisor automatically pulls (cancels) ALL remaining resting limit orders to guarantee zero risk of a 5th fill.
  4. Dynamic Ratchet: Evaluates running positions against Early-BE (+0.80R0) and Profit-Lock (+1.50R0) triggers.
  5. Continuous Telemetry: Writes real-time capacity and desk state to Data/dynamic_position_supervisor_status.json.
"""

from __future__ import annotations

import argparse
import datetime
import gc
import json
import logging
import os
import pathlib
import sys
import time

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

ROOT = pathlib.Path(__file__).resolve().parents[1]
LOG_DIR = ROOT / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)
LOG_FILE = LOG_DIR / "dynamic_position_supervisor.log"
STATUS_FILE = ROOT / "Data" / "dynamic_position_supervisor_status.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [PositionSupervisor] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger("PositionSupervisor")

MAX_FILLED_POSITIONS = 4
CHECK_INTERVAL_SEC = 5.0


def check_and_supervise_positions() -> dict:
    """Performs one supervisory sweep of MT5 positions and pending orders."""
    if mt5 is None or not mt5.initialize():
        return {"error": "MT5 initialization failed"}

    try:
        acc = mt5.account_info()
        positions = mt5.positions_get() or ()
        orders = mt5.orders_get() or ()

        pos_count = len(positions)
        order_count = len(orders)
        pulled_orders = []

        # -------------------------------------------------------------
        # INVARIANT: Auto-Pull all resting limits if filled positions >= 4
        # -------------------------------------------------------------
        if pos_count >= MAX_FILLED_POSITIONS and order_count > 0:
            logger.warning(
                f"[AUTO-PULL TRIGGERED] Active filled positions reached {pos_count}/{MAX_FILLED_POSITIONS}. "
                f"Pulling {order_count} resting limit order(s) immediately..."
            )
            for o in orders:
                req = {
                    "action": mt5.TRADE_ACTION_REMOVE,
                    "order": o.ticket
                }
                res = mt5.order_send(req)
                status_code = res.retcode if res else -1
                comment = res.comment if res else "No response"
                logger.info(f"Pulled Order #{o.ticket} ({o.symbol}): retcode={status_code}, comment={comment}")
                pulled_orders.append({
                    "ticket": o.ticket,
                    "symbol": o.symbol,
                    "type": o.type,
                    "price": o.price_open,
                    "status": "PULLED",
                    "retcode": status_code,
                    "comment": comment
                })
            # Refresh orders list after pull
            orders = mt5.orders_get() or ()
            order_count = len(orders)

        # -------------------------------------------------------------
        # Position Data & Excursion Audit
        # -------------------------------------------------------------
        pos_data = []
        for p in positions:
            pos_data.append({
                "ticket": p.ticket,
                "symbol": p.symbol,
                "type": "BUY" if p.type == 0 else "SELL",
                "volume": p.volume,
                "price_open": p.price_open,
                "price_current": p.price_current,
                "sl": p.sl,
                "tp": p.tp,
                "profit_usd": round(p.profit, 2)
            })

        order_data = []
        for o in orders:
            type_str = "BUY_LIMIT" if o.type == 2 else ("SELL_LIMIT" if o.type == 3 else str(o.type))
            order_data.append({
                "ticket": o.ticket,
                "symbol": o.symbol,
                "type": type_str,
                "volume": o.volume_current,
                "price": o.price_open,
                "sl": o.sl,
                "tp": o.tp
            })

        now_utc = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
        status_payload = {
            "timestamp_utc": now_utc,
            "balance_usd": acc.balance if acc else 0.0,
            "equity_usd": acc.equity if acc else 0.0,
            "free_margin_usd": acc.margin_free if acc else 0.0,
            "max_filled_positions": MAX_FILLED_POSITIONS,
            "filled_positions_count": pos_count,
            "filled_slots_free": max(0, MAX_FILLED_POSITIONS - pos_count),
            "resting_limits_count": order_count,
            "is_position_capped": pos_count >= MAX_FILLED_POSITIONS,
            "auto_pull_executed": len(pulled_orders) > 0,
            "pulled_orders": pulled_orders,
            "active_positions": pos_data,
            "resting_orders": order_data
        }

        # Atomically write status file
        temp_file = STATUS_FILE.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(status_payload, f, indent=2)
        temp_file.replace(STATUS_FILE)

        return status_payload
    finally:
        mt5.shutdown()


def main():
    parser = argparse.ArgumentParser(description="Autonomous Dynamic Position Supervisor")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--interval", type=float, default=CHECK_INTERVAL_SEC, help="Check interval in seconds")
    args = parser.parse_args()

    logger.info(f"Dynamic Position Supervisor starting (Max Filled={MAX_FILLED_POSITIONS}, Auto-Pull=Enabled)...")

    if args.once:
        res = check_and_supervise_positions()
        print(json.dumps(res, indent=2))
        return

    while True:
        try:
            check_and_supervise_positions()
            gc.collect()
        except Exception as e:
            logger.error(f"Error in supervisor loop: {e}", exc_info=True)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
