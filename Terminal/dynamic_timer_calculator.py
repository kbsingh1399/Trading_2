"""Dynamic Timer Calculator for Sovereign Antigravity Execution Desk.
Computes the dynamic sleep duration between completed cycles.
Enforces the mandatory 20-Minute Relative Post-Completion Delay (T_finish + 20 min = 1,200 seconds)
per STANDARDIZED_TRADING_DECISION_CHAIN.md and Operator Mandate, while the persistent
background supervisor (dynamic_position_supervisor.py) autonomously guards active stops
and ratchets at high frequency (5.0s interval).
"""

from __future__ import annotations

import datetime
import json
import MetaTrader5 as mt5

CYCLE_INTERVAL_SECONDS = 1200  # Strict 20-minute separation between completed cycles


def calculate_dynamic_cycle_interval() -> dict:
    """Calculate the cycle sleep duration in seconds for the next cycle wakeup."""
    utc_now = datetime.datetime.now(datetime.timezone.utc)
    seconds_in_m15 = (utc_now.minute % 15) * 60 + utc_now.second
    seconds_to_m15_close = 900 - seconds_in_m15

    num_positions = 0
    num_orders = 0

    if mt5.initialize():
        try:
            positions = mt5.positions_get()
            num_positions = len(positions) if positions else 0
            orders = mt5.orders_get()
            num_orders = len(orders) if orders else 0
        finally:
            mt5.shutdown()

    return {
        "duration_seconds": CYCLE_INTERVAL_SECONDS,
        "duration_minutes": round(CYCLE_INTERVAL_SECONDS / 60.0, 1),
        "regime": "CYCLE_COMPLETION_20M",
        "reason": (
            f"Mandatory 20-minute separation between cycles ({CYCLE_INTERVAL_SECONDS}s). "
            f"Active positions ({num_positions}) and resting orders ({num_orders}) are "
            f"autonomously supervised in real time by dynamic_position_supervisor.py every 5.0s."
        ),
        "seconds_to_m15_close": seconds_to_m15_close,
        "num_positions": num_positions,
        "num_orders": num_orders,
    }


if __name__ == "__main__":
    result = calculate_dynamic_cycle_interval()
    print(json.dumps(result, indent=2))
