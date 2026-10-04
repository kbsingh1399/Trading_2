"""Generate a small deterministic Blueberry-style CFD quote fixture.

This is a policy fixture, not a capture of broker quotes.  It deliberately
covers the normal spread ranges supplied for SOL/XRP, 2x widening, and a 5x
candle-open spike.  The generated JSON is suitable for
``Terminal/Execution_Simulator.py --fixture``.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict, List


ASSETS = {
    "SOLUSD.p": {
        "asset": "SOL",
        "point": 0.01,
        "digits": 2,
        "mid": 121.00,
        "normal_spreads": [20, 30, 40],
    },
    "XRPUSD.pi": {
        "asset": "XRP",
        "point": 0.001,
        "digits": 3,
        "mid": 1.500,
        "normal_spreads": [20, 25, 30],
    },
}


def quote(timestamp: float, mid: float, spread_points: int, point: float, digits: int) -> Dict[str, float]:
    half = spread_points * point / 2.0
    return {
        "timestamp": timestamp,
        "bid": round(mid - half, digits),
        "ask": round(mid + half, digits),
        "point": point,
        "available_volume": 10.0,
    }


def make_case(symbol: str, config: Dict[str, object], direction: str, base_spread_points: int, multiplier: int, outcome: str, case_number: int) -> Dict[str, object]:
    point = float(config["point"])
    digits = int(config["digits"])
    base_mid = float(config["mid"])
    candle_epoch = 1_700_000_000.0 + case_number * 10_000.0
    submitted_at = candle_epoch - 1.0
    sign = -1.0 if direction == "LONG" else 1.0
    base_spread_price = base_spread_points * point

    # The raw mid moves favorably in two steps.  A normal spread fills at t+1;
    # a 2x spread requires the second step; 5x is cancelled by the guard first.
    first_move = 0.75 * base_spread_price if outcome == "retrace" else 0.0
    second_move = 1.50 * base_spread_price if outcome == "retrace" else 0.0
    quotes = [
        quote(submitted_at, base_mid, base_spread_points, point, digits),
        quote(candle_epoch, base_mid, base_spread_points, point, digits),
        quote(candle_epoch + 1.0, base_mid + sign * first_move, base_spread_points, point, digits),
        quote(candle_epoch + 2.0, base_mid + sign * second_move, base_spread_points, point, digits),
        quote(candle_epoch + 3.0, base_mid + sign * second_move, base_spread_points, point, digits),
    ]
    return {
        "case_id": f"{config['asset']}_{direction.lower()}_{base_spread_points}pt_{multiplier}x_{outcome}",
        "asset": config["asset"],
        "symbol": symbol,
        "direction": direction,
        "point": point,
        "base_spread_points": base_spread_points,
        "spread_bucket": "normal" if multiplier == 1 else f"{multiplier}x",
        "spike_multiplier": multiplier,
        "outcome": outcome,
        "volume": 0.50 if symbol == "SOLUSD.p" else 1.00,
        "submitted_at": submitted_at,
        "limit_price": round(base_mid, digits),
        "policy": {
            "expiry_seconds": 4.0,
            "route_latency_seconds": 1.0,
            "max_quote_age_seconds": 2.0,
            "max_spread_points": 40.0,
            "deviation_points": 100.0,
            "slippage_points": 0.0,
            "passive_only": True,
        },
        "spread_spike": {
            "multiplier": float(multiplier),
            "candle_seconds": 900.0,
            "open_window_seconds": 3.0,
            "candle_epoch": candle_epoch,
            "name": f"{multiplier}x_{config['asset']}_candle_open",
        },
        "quotes": quotes,
    }


def build_fixture() -> Dict[str, object]:
    cases: List[Dict[str, object]] = []
    case_number = 0
    for symbol, config in ASSETS.items():
        for direction in ("LONG", "SHORT"):
            for base_spread_points in config["normal_spreads"]:
                for multiplier in (1, 2, 5):
                    for outcome in ("retrace", "no_retrace"):
                        cases.append(make_case(symbol, config, direction, base_spread_points, multiplier, outcome, case_number))
                        case_number += 1
    return {
        "schema_version": "blueberry-cfd-policy-fixture-v1",
        "generated_by": "fixtures/generate_blueberry_quotes.py",
        "assumptions": {
            "purpose": "deterministic policy stress, not broker-captured market data",
            "normal_spreads": "SOL 20/30/40 points; XRP 20/25/30 points",
            "candle_open_spikes": "1x, 2x, and 5x for a 3-second open window",
            "max_spread_guard_points": 40,
            "point_units": "SOL point=0.01; XRP point=0.001",
            "quote_path": "same-mid spread widening plus favorable/no-retrace paths",
        },
        "cases": cases,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic Blueberry CFD quote fixture")
    parser.add_argument("--output", type=Path, default=Path("fixtures/blueberry_quotes.json"))
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build_fixture(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Wrote {len(build_fixture()['cases'])} cases to {args.output}")


if __name__ == "__main__":
    main()
