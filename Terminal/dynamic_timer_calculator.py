"""Dynamic Timer Calculator for Sovereign Antigravity Execution Desk.
Computes the exact dynamic sleep duration (in seconds) between cycle completions
based on real-time MT5 inventory, orderfill proximity, volatility, and candle boundaries.
"""

import time
import datetime
import math
import json
import MetaTrader5 as mt5

def calculate_dynamic_cycle_interval() -> dict:
    """Calculate the optimal dynamic sleep duration in seconds for the next cycle wakeup."""
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    seconds_in_m15 = (utc_now.minute % 15) * 60 + utc_now.second
    seconds_to_m15_close = 900 - seconds_in_m15
    
    # Target waking up 30 seconds before the candle close to prepare telemetry and order decisions
    candle_sync_target = max(45, seconds_to_m15_close - 30)

    if not mt5.initialize():
        return {
            "duration_seconds": 300,
            "regime": "FALLBACK_NO_MT5",
            "reason": "MT5 initialization unavailable; default 5m fallback."
        }
    
    try:
        # Check running positions
        positions = mt5.positions_get()
        num_positions = len(positions) if positions else 0
        
        # Check pending orders
        orders = mt5.orders_get()
        num_orders = len(orders) if orders else 0
        
        # 1. Active Running Position Supervision (Highest Velocity)
        if num_positions > 0:
            # We have running capital at risk; wake up frequently to supervise ratchet & decay
            return {
                "duration_seconds": 90,
                "regime": "POSITION_SUPERVISION",
                "reason": f"{num_positions} active position(s) running; high-frequency 90s supervision.",
                "candle_sync_seconds": candle_sync_target,
                "num_positions": num_positions,
                "num_orders": num_orders
            }
            
        # 2. Pending Limit Order Proximity (Proximity-Adaptive Velocity)
        if num_orders > 0:
            min_dist_pips = float('inf')
            closest_symbol = None
            closest_ticket = None
            
            for o in orders:
                sym_info = mt5.symbol_info(o.symbol)
                tick = mt5.symbol_info_tick(o.symbol)
                if sym_info and tick:
                    point = max(float(sym_info.point), 1e-6)
                    # 1 pip = 10 points for FX / JPY, 0.1 for Gold
                    pip_size = 0.01 if "JPY" in o.symbol else (0.0001 if sym_info.digits in (4, 5) else 0.1)
                    if o.type in (mt5.ORDER_TYPE_SELL_LIMIT, getattr(mt5, "ORDER_TYPE_SELL", 1)):
                        dist = max(0.0, (o.price_open - tick.ask) / pip_size)
                    else:
                        dist = max(0.0, (tick.bid - o.price_open) / pip_size)
                    
                    if dist < min_dist_pips:
                        min_dist_pips = dist
                        closest_symbol = o.symbol
                        closest_ticket = o.ticket
            
            # High proximity: limit order is imminent (< 5 pips)
            if min_dist_pips <= 5.0:
                return {
                    "duration_seconds": 60,
                    "regime": "ORDER_PROXIMITY_IMMINENT",
                    "reason": f"Pending order #{closest_ticket} ({closest_symbol}) is {min_dist_pips:.1f} pips from fill; 60s alert.",
                    "candle_sync_seconds": candle_sync_target,
                    "min_dist_pips": min_dist_pips,
                    "num_orders": num_orders
                }
            # Elevated proximity: limit order is in active sweep zone (5 - 15 pips)
            elif min_dist_pips <= 15.0:
                return {
                    "duration_seconds": 180,
                    "regime": "ORDER_PROXIMITY_ELEVATED",
                    "reason": f"Pending order #{closest_ticket} ({closest_symbol}) is {min_dist_pips:.1f} pips from fill; 3m dynamic check.",
                    "candle_sync_seconds": candle_sync_target,
                    "min_dist_pips": min_dist_pips,
                    "num_orders": num_orders
                }
            # Moderate proximity: resting limit waiting (> 15 pips)
            else:
                interval = min(candle_sync_target, 360)
                return {
                    "duration_seconds": interval,
                    "regime": "ORDER_PROXIMITY_MODERATE",
                    "reason": f"Pending order #{closest_ticket} ({closest_symbol}) is {min_dist_pips:.1f} pips away; sleeping {interval}s to next candle check.",
                    "candle_sync_seconds": candle_sync_target,
                    "min_dist_pips": min_dist_pips,
                    "num_orders": num_orders
                }

        # 3. Flat Market / Scanning State (Synchronized to 15m Candle Close)
        # Sleep until the next 15-minute bar forms (minus 30 seconds for computation)
        interval = max(60, min(candle_sync_target, 900))
        return {
            "duration_seconds": interval,
            "regime": "M15_CANDLE_SYNC",
            "reason": f"Zero positions and zero orders; sleeping {interval}s to synchronize with next M15 bar close.",
            "candle_sync_seconds": candle_sync_target,
            "num_positions": 0,
            "num_orders": 0
        }

    finally:
        mt5.shutdown()

if __name__ == "__main__":
    result = calculate_dynamic_cycle_interval()
    print(json.dumps(result, indent=2))
