#!/usr/bin/env python3
"""
Terminal/position_ratchet_daemon.py
===================================
Always-on background microsecond sentry for active positions and resting orders.
Automatically enforces the institutional Step 10 Microstructure Exit Ratchet:
- Stage 1 (Early-BE): At +0.75R0 excursion, moves SL to Entry + 0.10R0 (Locks BE+ and releases buffer capacity).
- Stage 2 (Profit Lock): At +1.50R0 excursion, moves SL to Entry + 0.80R0.
- Synchronizes Data/telemetry/mt5_account_telemetry.json whenever state changes.
"""

import time
import json
import pathlib
import logging
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import MetaTrader5 as mt5
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s][RatchetDaemon] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(ROOT / "Data" / "ratchet_daemon.log", encoding="utf-8")
    ]
)
logger = logging.getLogger("RatchetDaemon")

def sync_telemetry():
    try:
        acc = mt5.account_info()
        pos = mt5.positions_get()
        orders = mt5.orders_get()
        if not acc:
            return
        td = {
            "account": {
                "login": acc.login,
                "balance_usd": acc.balance,
                "equity_usd": acc.equity,
                "margin_free_usd": acc.margin_free,
                "margin_used_usd": acc.margin,
                "hard_floor_cushion_usd": acc.equity - 4600.0,
                "operating_buffer_cushion_usd": acc.equity - 4650.0
            },
            "open_positions_count": len(pos) if pos else 0,
            "open_positions": [
                {
                    "ticket": p.ticket, "symbol": p.symbol, "volume": p.volume,
                    "direction": "BUY" if p.type == 0 else "SELL",
                    "price_open": p.price_open, "sl": p.sl, "tp": p.tp, "profit": p.profit
                } for p in (pos or [])
            ],
            "pending_orders_count": len(orders) if orders else 0,
            "pending_orders": [
                {
                    "ticket": o.ticket, "symbol": o.symbol, "volume": o.volume_initial,
                    "direction": "BUY_LIMIT" if o.type == 2 else "SELL_LIMIT" if o.type == 3 else "PENDING",
                    "price_open": o.price_open, "sl": o.sl, "tp": o.tp
                } for o in (orders or [])
            ]
        }
        p = ROOT / "Data" / "telemetry" / "mt5_account_telemetry.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(td, indent=2), encoding="utf-8")
    except Exception as e:
        logger.warning(f"Telemetry sync error: {e}")

def run_loop():
    logger.info("Starting Position Ratchet Daemon...")
    bridge = MT5ExecutionBridge()
    if not bridge.ensure_connected():
        logger.error("Failed to connect to MT5.")
        return

    last_sync = 0
    while True:
        try:
            now = time.time()
            if now - last_sync >= 10:
                sync_telemetry()
                last_sync = now

            positions = mt5.positions_get()
            if positions:
                for p in positions:
                    ticket = p.ticket
                    sym = p.symbol
                    pos_type = p.type
                    entry = p.price_open
                    current_sl = p.sl
                    tick = mt5.symbol_info_tick(sym)
                    if not tick:
                        continue

                    # For Short positions (SELL)
                    if pos_type == mt5.ORDER_TYPE_SELL:
                        bid = tick.bid
                        r0 = abs(current_sl - entry) if current_sl > entry else 300.0
                        gain = entry - bid
                        
                        # Stage 1: Early-BE (+0.75R0 excursion)
                        # Ratchet SL to entry - 0.10R0 (locked profit + commissions)
                        if gain >= 0.75 * r0:
                            target_sl = round(entry - 0.10 * r0, 2)
                            if current_sl > target_sl:
                                logger.info(f"RATCHET TRIGGER (Early-BE): {sym} #{ticket} gain={gain:.1f} >= 0.75R0 ({0.75*r0:.1f}). Ratcheting SL {current_sl} -> {target_sl}")
                                bridge.modify_position_sltp(ticket, new_sl=target_sl)
                        
                        # Stage 2: Profit Lock (+1.50R0 excursion)
                        # Ratchet SL to entry - 0.80R0
                        if gain >= 1.50 * r0:
                            target_sl = round(entry - 0.80 * r0, 2)
                            if current_sl > target_sl:
                                logger.info(f"RATCHET TRIGGER (Profit Lock): {sym} #{ticket} gain={gain:.1f} >= 1.50R0 ({1.50*r0:.1f}). Ratcheting SL {current_sl} -> {target_sl}")
                                bridge.modify_position_sltp(ticket, new_sl=target_sl)

                    # For Long positions (BUY)
                    elif pos_type == mt5.ORDER_TYPE_BUY:
                        ask = tick.ask
                        r0 = abs(entry - current_sl) if current_sl < entry else 10.0
                        gain = ask - entry
                        
                        if gain >= 0.75 * r0:
                            target_sl = round(entry + 0.10 * r0, 5)
                            if current_sl < target_sl:
                                logger.info(f"RATCHET TRIGGER (Early-BE): {sym} #{ticket} gain={gain:.5f} >= 0.75R0. Ratcheting SL {current_sl} -> {target_sl}")
                                bridge.modify_position_sltp(ticket, new_sl=target_sl)

                        if gain >= 1.50 * r0:
                            target_sl = round(entry + 0.80 * r0, 5)
                            if current_sl < target_sl:
                                logger.info(f"RATCHET TRIGGER (Profit Lock): {sym} #{ticket} gain={gain:.5f} >= 1.50R0. Ratcheting SL {current_sl} -> {target_sl}")
                                bridge.modify_position_sltp(ticket, new_sl=target_sl)

            time.sleep(2.0)
        except Exception as e:
            logger.error(f"Error in ratchet loop: {e}")
            time.sleep(5.0)

if __name__ == "__main__":
    run_loop()
