"""Fail-closed broker-side joint-fill admission for new positions and limits.

This is a pre-send check, not an OCO or a guarantee against unbounded gaps.
It deliberately reserves every currently resting pending's contingent loss.
"""
from __future__ import annotations

import math
from typing import Any

from Terminal.risk.floor_defense import HARD_FLOOR_USD, BUFFER_USD

MAX_FILLED = 2
MIN_RISK_USD = 10.0
MAX_RISK_USD = 20.0
# Stress allowance in addition to the broker-valued SL loss. This cannot
# guarantee a gap fill, but avoids the false $0-cost nominal-floor check.
STOP_STRESS_MULTIPLIER = 1.25
MIN_EXECUTION_COST_USD = 2.0


def _positive(value: Any, name: str) -> float:
    try:
        n = float(value)
        if math.isfinite(n) and n > 0:
            return n
    except (TypeError, ValueError):
        pass
    raise ValueError(f"risk_inventory_invalid_{name}")


def _loss(bridge, row: dict) -> float:
    symbol = str(row.get("symbol") or "")
    direction = str(row.get("direction") or "").upper()
    if direction in ("BUY", "LONG"):
        direction = "LONG"
    elif direction in ("SELL", "SHORT"):
        direction = "SHORT"
    else:
        raise ValueError("risk_inventory_invalid_direction")
    entry = _positive(row.get("price_open", row.get("entry")), "entry")
    sl = _positive(row.get("sl"), "sl")
    volume = _positive(row.get("volume"), "volume")
    if not symbol:
        raise ValueError("risk_inventory_invalid_symbol")
    # A *native* SL on the profit side releases nominal loss, but still
    # requires an execution-cost reserve. Never use telemetry's BE label.
    adverse = sl < entry if direction == "LONG" else sl > entry
    if adverse:
        estimate = bridge.estimate_order(symbol, direction, entry, sl)
        per_lot = _positive(estimate.get("stop_loss_per_lot"), "broker_valuation")
        return per_lot * volume * STOP_STRESS_MULTIPLIER + MIN_EXECUTION_COST_USD
    return MIN_EXECUTION_COST_USD


def assert_joint_fill_safe(bridge, symbol: str, direction: str, volume: float,
                           entry: float, sl: float, *, min_risk_usd: float = MIN_RISK_USD) -> dict:
    """Raise ValueError unless all simultaneous fills preserve floor + $20.

    Read all native inventories immediately before placing an order. A failed
    read, unprotected existing ticket or unsupported account currency refuses
    admission. In-process preflight is not atomic across trading processes;
    the deployment must serialize order submission and reconcile broker state.
    """
    account = bridge.get_account_summary()
    if not isinstance(account, dict) or not account.get("connected") or account.get("currency") != "USD":
        raise ValueError("risk_account_unavailable_or_non_usd")
    balance = _positive(account.get("balance_usd", account.get("balance")), "balance")
    equity = _positive(account.get("equity_usd"), "equity")
    positions = bridge.get_open_positions()
    pending = bridge.get_pending_orders()
    if positions is None or pending is None or not isinstance(positions, (list, tuple)) or not isinstance(pending, (list, tuple)):
        raise ValueError("risk_inventory_unavailable")
    if len(positions) >= MAX_FILLED or len(positions) + len(pending) >= MAX_FILLED:
        # Without proven atomic first-fill OCO, both resting limits can fill.
        raise ValueError("joint_fill_capacity_exceeded")
    direction = str(direction).upper()
    entry, sl = _positive(entry, "proposed_entry"), _positive(sl, "proposed_sl")
    if direction not in ("LONG", "SHORT") or not (sl < entry if direction == "LONG" else sl > entry):
        raise ValueError("proposed_protective_stop_invalid")
    # Validate min/max on nominal broker stop loss, not stressed loss.
    per_lot = _positive(bridge.estimate_order(symbol, direction, entry, sl).get("stop_loss_per_lot"),
                        "proposed_broker_valuation")
    nominal = per_lot * _positive(volume, "proposed_volume")
    if not min_risk_usd <= nominal <= MAX_RISK_USD:
        raise ValueError(f"proposed_risk_out_of_bounds:{nominal:.2f}")
    existing = sum(_loss(bridge, row) for row in [*positions, *pending])
    total = existing + nominal * STOP_STRESS_MULTIPLIER + MIN_EXECUTION_COST_USD
    post_loss = min(balance, equity) - total
    if post_loss < HARD_FLOOR_USD + BUFFER_USD:
        raise ValueError(f"joint_fill_floor_breach:post_loss={post_loss:.2f}"
                         f"<required={HARD_FLOOR_USD + BUFFER_USD:.2f}")
    # A second positively correlated active risk is not an orthogonal slot.
    from Terminal.risk.floor_defense import FloorDefense
    clusters = FloorDefense()
    own_cluster = clusters.cluster_of(symbol)
    if own_cluster == "other":
        raise ValueError(f"unknown_correlation_cluster:{symbol}")
    for row in [*positions, *pending]:
        if clusters.cluster_of(str(row["symbol"])) == own_cluster:
            raise ValueError(f"correlated_joint_fill:{symbol}:{row['symbol']}")
    return {"proposed_nominal_risk_usd": nominal, "stress_total_usd": total,
            "post_joint_stop_equity_usd": post_loss, "filled": len(positions),
            "pending": len(pending)}
