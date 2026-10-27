#!/usr/bin/env python3
"""
Terminal/dynamic_position_supervisor.py
=======================================
Autonomous Real-Time Dynamic Position & Order Supervisor Daemon.

Core Institutional Directives (Operator Mandate & Sol 6.1 Audit Hardening):
  1. Fail-Closed Supervision: Failed inventory reads NEVER treated as empty inventory.
  2. Account Identity Verification: Strictly verifies Blueberry Markets login #5064568 before any mutation.
  3. Max Concurrent Filled Positions: Strictly capped at 4.
  4. Auto-Pull Invariant: The moment active filled positions reaches exactly 4 (len(positions) >= 4),
     the supervisor automatically pulls (cancels) ALL remaining resting limit orders.
  5. Dynamic Ratchet Actuator:
     - Stage 1 (+0.80R): Ratchets stop to Entry +/- 0.15R (locks friction + breakeven).
     - Stage 2 (+1.50R): Ratchets stop to Entry +/- 0.80R (profit lock).
  6. Time Decay Actuator: Closes at market if position held >= 6 hours (24 M15 bars) and gain < +0.20R.
  7. State Persistence & Watchdog Heartbeat: Idempotent state in Terminal/.state/ratchet_state.json and heartbeat.
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
STATE_DIR = ROOT / "Terminal" / ".state"
STATE_DIR.mkdir(parents=True, exist_ok=True)
RATCHET_STATE_FILE = STATE_DIR / "ratchet_state.json"
HEARTBEAT_FILE = STATE_DIR / "heartbeat"

ACCOUNT_LOGIN = 5064568
MAX_FILLED_POSITIONS = 4
CHECK_INTERVAL_SEC = 5.0

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [PositionSupervisor] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ]
)
logger = logging.getLogger("PositionSupervisor")


def load_ratchet_state() -> dict:
    if RATCHET_STATE_FILE.exists():
        try:
            return json.loads(RATCHET_STATE_FILE.read_text(encoding="utf-8"))
        except Exception as e:
            logger.warning(f"Failed to load ratchet state file: {e}")
    return {}


def save_ratchet_state(state: dict):
    for attempt in range(3):
        try:
            temp = RATCHET_STATE_FILE.with_suffix(".tmp")
            temp.write_text(json.dumps(state, indent=2), encoding="utf-8")
            if RATCHET_STATE_FILE.exists():
                try:
                    os.remove(RATCHET_STATE_FILE)
                except Exception:
                    pass
            temp.replace(RATCHET_STATE_FILE)
            return
        except Exception:
            if attempt == 2:
                try:
                    RATCHET_STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")
                except Exception as ex:
                    logger.error(f"Failed to save ratchet state: {ex}")
            time.sleep(0.05)


def check_and_supervise_positions() -> dict:
    """Performs one supervisory sweep of MT5 positions and pending orders."""
    if mt5 is None or not mt5.initialize():
        return {"error": "MT5 initialization failed"}

    try:
        acc = mt5.account_info()
        if acc is None or acc.login != ACCOUNT_LOGIN:
            logger.error(f"Account check failed: {getattr(acc, 'login', None)} != {ACCOUNT_LOGIN}")
            return {"error": f"ACCOUNT_IDENTITY_MISMATCH: {getattr(acc, 'login', None)}"}

        raw_positions = mt5.positions_get()
        raw_orders = mt5.orders_get()

        if raw_positions is None:
            logger.error("positions_get() returned None — fail-closed, aborting sweep")
            return {"error": "POSITIONS_READ_FAILED"}
        if raw_orders is None:
            logger.error("orders_get() returned None — fail-closed, aborting sweep")
            return {"error": "ORDERS_READ_FAILED"}

        positions = list(raw_positions)
        orders = list(raw_orders)
        pos_count = len(positions)
        order_count = len(orders)
        pulled_orders = []

        # -------------------------------------------------------------
        # INVARIANT: Hard Reservation Cap & Drawdown Defense Sentry
        # 1. If Equity <= Operating Buffer (4,795.00 USD), pull ALL pending orders immediately.
        # 2. If filled positions >= MAX_FILLED_POSITIONS (4), pull ALL pending orders.
        # 3. If open + pending > MAX_FILLED_POSITIONS (4), prune excess pending orders.
        # -------------------------------------------------------------
        OPERATING_BUFFER = 4795.00
        is_defense_mode = (acc.equity <= OPERATING_BUFFER)

        if is_defense_mode and order_count > 0:
            logger.warning(
                f"[DEFENSE SENTRY TRIGGERED] Equity {acc.equity:.2f} <= {OPERATING_BUFFER:.2f} buffer. "
                f"Pulling ALL {order_count} resting limit order(s) to guarantee floor preservation..."
            )
            for o in orders:
                req = {"action": mt5.TRADE_ACTION_REMOVE, "order": o.ticket}
                res = mt5.order_send(req)
                status_code = res.retcode if res else -1
                comment = res.comment if res else "No response"
                logger.info(f"Pulled Order #{o.ticket} ({o.symbol}): retcode={status_code}, comment={comment}")
                pulled_orders.append({"ticket": o.ticket, "symbol": o.symbol, "status": "PULLED_DEFENSE"})
            orders = list(mt5.orders_get() or ())
            order_count = len(orders)

        elif pos_count >= MAX_FILLED_POSITIONS and order_count > 0:
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
            orders = list(mt5.orders_get() or ())
            order_count = len(orders)

        elif (pos_count + order_count) > MAX_FILLED_POSITIONS and order_count > 0:
            excess = (pos_count + order_count) - MAX_FILLED_POSITIONS
            logger.warning(
                f"[RESERVATION CAP EXCEEDED] Open ({pos_count}) + Pending ({order_count}) = {pos_count + order_count} > {MAX_FILLED_POSITIONS}. "
                f"Pruning {excess} excess pending order(s) to restore strict <= {MAX_FILLED_POSITIONS} invariant..."
            )
            for o in orders[:excess]:
                req = {"action": mt5.TRADE_ACTION_REMOVE, "order": o.ticket}
                res = mt5.order_send(req)
                logger.info(f"Pruned Excess Order #{o.ticket} ({o.symbol})")
                pulled_orders.append({"ticket": o.ticket, "symbol": o.symbol, "status": "PULLED_EXCESS"})
            orders = list(mt5.orders_get() or ())
            order_count = len(orders)

        # -------------------------------------------------------------
        # Dynamic Ratchet & Excursion Supervision
        # -------------------------------------------------------------
        ratchet_state = load_ratchet_state()
        now_ts = time.time()
        pos_data = []

        for p in positions:
            ticket_str = str(p.ticket)
            sym_info = mt5.symbol_info(p.symbol)
            digits = sym_info.digits if sym_info else 2
            is_buy = (p.type == mt5.ORDER_TYPE_BUY)

            # Initialize state for new ticket
            if ticket_str not in ratchet_state:
                initial_sl = p.sl
                is_sl_in_loss = (p.sl < p.price_open) if is_buy else (p.sl > p.price_open)
                if (not is_sl_in_loss or p.sl == 0):
                    # Query order history to recover the true initial protective stop
                    hist_orders = mt5.history_orders_get(position=p.ticket)
                    if hist_orders and len(hist_orders) > 0:
                        initial_sl = hist_orders[0].sl or p.sl
                initial_r = abs(p.price_open - initial_sl) if initial_sl > 0 else 0.0
                ratchet_state[ticket_str] = {
                    "ticket": p.ticket,
                    "symbol": p.symbol,
                    "type": "BUY" if is_buy else "SELL",
                    "price_open": p.price_open,
                    "initial_sl": initial_sl,
                    "initial_tp": p.tp,
                    "initial_r": initial_r,
                    "stage": 0,
                    "open_time": p.time,
                }

            p_state = ratchet_state[ticket_str]
            initial_r = p_state.get("initial_r", 0.0)
            if initial_r <= 0.0 and p.sl > 0:
                initial_r = abs(p.price_open - p.sl)
                p_state["initial_r"] = initial_r

            # Calculate current gain in R
            if is_buy:
                gain_price = p.price_current - p.price_open
            else:
                gain_price = p.price_open - p.price_current
            gain_r = round(gain_price / initial_r, 3) if initial_r > 0 else 0.0

            # --- Stage 1 Ratchet: +0.80R gain -> Lock Entry +/- 0.15R (Strictly Monotone) ---
            if gain_r >= 0.80 and p_state.get("stage", 0) < 1:
                target_sl = round(p.price_open + 0.15 * initial_r, digits) if is_buy else round(p.price_open - 0.15 * initial_r, digits)
                is_tighter = (target_sl > p.sl) if is_buy else (target_sl < p.sl)
                if p.sl == 0 or is_tighter:
                    logger.info(f"[RATCHET STAGE 1] Ticket #{p.ticket} reached +{gain_r:.2f}R. Moving SL from {p.sl} to tighter target {target_sl} (locking +0.15R)...")
                    mod_req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "position": p.ticket,
                        "sl": target_sl,
                        "tp": p.tp
                    }
                    res = mt5.order_send(mod_req)
                    if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                        logger.info(f"[RATCHET STAGE 1 SUCCESS] Ticket #{p.ticket} SL moved to {target_sl}")
                        p_state["stage"] = 1
                        p_state["ratchet_stage1_sl"] = target_sl
                    else:
                        logger.warning(f"[RATCHET STAGE 1 FAILED] Ticket #{p.ticket}: retcode={getattr(res, 'retcode', -1)}, comment={getattr(res, 'comment', 'N/A')}")
                else:
                    logger.info(f"[RATCHET STAGE 1 SKIPPED] Ticket #{p.ticket}: existing SL {p.sl} is already tighter than target {target_sl}. Advancing stage.")
                    p_state["stage"] = 1

            # --- Stage 2 Ratchet: +1.50R gain -> Lock Entry +/- 0.80R (Strictly Monotone) ---
            if gain_r >= 1.50 and p_state.get("stage", 0) < 2:
                target_sl = round(p.price_open + 0.80 * initial_r, digits) if is_buy else round(p.price_open - 0.80 * initial_r, digits)
                is_tighter = (target_sl > p.sl) if is_buy else (target_sl < p.sl)
                if p.sl == 0 or is_tighter:
                    logger.info(f"[RATCHET STAGE 2] Ticket #{p.ticket} reached +{gain_r:.2f}R. Moving SL from {p.sl} to tighter target {target_sl} (locking +0.80R)...")
                    mod_req = {
                        "action": mt5.TRADE_ACTION_SLTP,
                        "position": p.ticket,
                        "sl": target_sl,
                        "tp": p.tp
                    }
                    res = mt5.order_send(mod_req)
                    if res and res.retcode == mt5.TRADE_RETCODE_DONE:
                        logger.info(f"[RATCHET STAGE 2 SUCCESS] Ticket #{p.ticket} SL moved to {target_sl}")
                        p_state["stage"] = 2
                        p_state["ratchet_stage2_sl"] = target_sl
                    else:
                        logger.warning(f"[RATCHET STAGE 2 FAILED] Ticket #{p.ticket}: retcode={getattr(res, 'retcode', -1)}, comment={getattr(res, 'comment', 'N/A')}")
                else:
                    logger.info(f"[RATCHET STAGE 2 SKIPPED] Ticket #{p.ticket}: existing SL {p.sl} is already tighter than target {target_sl}. Advancing stage.")
                    p_state["stage"] = 2

            # --- Time Decay Check: 6 hours (21,600s) and gain < +0.20R ---
            pos_age_sec = now_ts - p.time
            if pos_age_sec >= 21600.0 and gain_r < 0.20:
                logger.warning(f"[TIME DECAY EXIT] Ticket #{p.ticket} age {pos_age_sec/3600:.1f}h >= 6h with stagnant gain {gain_r:.2f}R < +0.20R. Closing at market...")
                tick = mt5.symbol_info_tick(p.symbol)
                close_price = tick.bid if is_buy else tick.ask
                close_type = mt5.ORDER_TYPE_SELL if is_buy else mt5.ORDER_TYPE_BUY
                close_req = {
                    "action": mt5.TRADE_ACTION_DEAL,
                    "symbol": p.symbol,
                    "volume": p.volume,
                    "type": close_type,
                    "position": p.ticket,
                    "price": close_price,
                    "deviation": 20,
                    "magic": p.magic,
                    "comment": "Time decay exit (6h)",
                }
                res = mt5.order_send(close_req)
                logger.info(f"[TIME DECAY CLOSE RESULT] Ticket #{p.ticket}: retcode={getattr(res, 'retcode', -1)}, comment={getattr(res, 'comment', 'N/A')}")

            pos_data.append({
                "ticket": p.ticket,
                "symbol": p.symbol,
                "type": "BUY" if is_buy else "SELL",
                "volume": p.volume,
                "price_open": p.price_open,
                "price_current": p.price_current,
                "sl": p.sl,
                "tp": p.tp,
                "gain_r": gain_r,
                "ratchet_stage": p_state.get("stage", 0),
                "profit_usd": round(p.profit, 2)
            })

        # Purge closed tickets from state
        live_tickets = {str(p.ticket) for p in positions}
        for t in list(ratchet_state.keys()):
            if t not in live_tickets:
                del ratchet_state[t]
        save_ratchet_state(ratchet_state)

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

        # Atomically write status file & update heartbeat
        temp_file = STATUS_FILE.with_suffix(".tmp")
        with open(temp_file, "w", encoding="utf-8") as f:
            json.dump(status_payload, f, indent=2)
        try:
            for _ in range(5):
                try:
                    temp_file.replace(STATUS_FILE)
                    break
                except PermissionError:
                    time.sleep(0.05)
            else:
                with open(STATUS_FILE, "w", encoding="utf-8") as f:
                    json.dump(status_payload, f, indent=2)
        except Exception as write_err:
            logger.warning(f"Status file write warning: {write_err}")

        HEARTBEAT_FILE.write_text(str(time.time()), encoding="utf-8")

        return status_payload
    finally:
        mt5.shutdown()


def main():
    parser = argparse.ArgumentParser(description="Autonomous Dynamic Position Supervisor")
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    parser.add_argument("--interval", type=float, default=CHECK_INTERVAL_SEC, help="Check interval in seconds")
    args = parser.parse_args()

    logger.info(f"Dynamic Position Supervisor starting (Max Filled={MAX_FILLED_POSITIONS}, Auto-Pull=Enabled, Ratchet=Active)...")

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
