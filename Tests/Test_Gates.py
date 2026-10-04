import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from Terminal.Execution_Simulator import (
    BrokerExecutionSimulator,
    ExecutionRequest,
    SimQuote,
    SpreadSpike,
)
from Terminal.Orderflow_Replay import OrderflowReplayHarness, ReplayPolicy


def _snapshot(observed_at, decision_at, price=100.0):
    return {
        "observed_at": observed_at,
        "decision_at": decision_at,
        "price": price,
        "l2_book": {"bid_volume_usd": 300_000, "ask_volume_usd": 100_000},
        "liquidations": {"bands": [{"mid_px": 99.0, "amount_usd": 500_000}]},
        "l3_orders": [
            {"side": "BUY", "price": 99.5, "notional_usd": 200_000, "observed_at": observed_at}
        ],
        "recent_trades": [{"side": "BUY", "notional_usd": 80_000}],
        "cvd_history": [0.0, 100.0, 200.0],
    }


def test_gate3_replay_is_sorted_deterministic_and_age_aware():
    snapshots = [
        _snapshot(1000, 1040),  # stale
        _snapshot(1000, 1000),  # fresh
        _snapshot(1000, 1020),  # decayed
        _snapshot(1000, 999),   # future observation
    ]
    harness = OrderflowReplayHarness(ReplayPolicy(decay_tau_seconds=10, max_quote_age_seconds=30, fresh_age_seconds=5))
    result = harness.replay(snapshots)
    again = harness.replay(snapshots)

    assert result.input_digest == again.input_digest
    assert [r.source_hash for r in result.records] == [r.source_hash for r in again.records]
    assert [r.state for r in result.records] == ["FUTURE_OBSERVATION", "FRESH", "DECAYED", "STALE"]
    fresh = result.records[1]
    decayed = result.records[2]
    assert fresh.decay_weight == 1.0
    assert math.isclose(decayed.decay_weight, math.exp(-2.0), rel_tol=1e-9)
    assert fresh.features["long_score"] > decayed.features["long_score"]
    assert result.records[0].features["direction"] == "NONE"
    assert result.summary["state_counts"]["STALE"] == 1


def test_gate3_missing_timestamps_fail_closed_without_wall_clock():
    snapshot = _snapshot(None, None)
    snapshot.pop("observed_at")
    snapshot.pop("decision_at")
    result = OrderflowReplayHarness().replay([snapshot])
    assert result.records[0].state == "NO_OBSERVATION"
    assert result.records[0].decay_weight == 0.0
    assert result.records[0].features["direction"] == "NONE"


def _quotes():
    # Normal 1 bp spread, followed by a retrace. Point is 0.001.
    return [
        SimQuote(999.0, 100.000, 100.010, 0.001),
        SimQuote(1000.0, 100.000, 100.010, 0.001),
        SimQuote(1001.0, 99.999, 100.004, 0.001),
        SimQuote(1003.0, 99.999, 100.004, 0.001),
    ]


def test_gate4_five_x_open_spread_rejects_market_and_cancels_pending_limit():
    simulator = BrokerExecutionSimulator()
    comparison = simulator.stress_spread_open(
        _quotes(), symbol="SOLUSD.p", direction="LONG", volume=0.5,
        submitted_at=999.0, limit_price=100.005,
        spike=SpreadSpike(multiplier=5.0, candle_epoch=1000.0, open_window_seconds=2.0),
        route_latency_seconds=1.0, max_spread_points=20.0,
    )
    assert comparison.market.status == "REJECTED"
    assert comparison.market.reason == "spread_guard_at_execution"
    assert comparison.limit.status == "CANCELLED_SPREAD"
    assert comparison.limit.spread_points == 50.0


def test_gate4_limit_can_fill_after_retrace_while_market_pays_ask():
    simulator = BrokerExecutionSimulator()
    market = simulator.simulate(
        ExecutionRequest("SOLUSD.p", "LONG", 0.5, 999.0, mode="market", route_latency_seconds=0.0, max_spread_points=None),
        _quotes(),
    )
    limit = simulator.simulate(
        ExecutionRequest("SOLUSD.p", "LONG", 0.5, 999.0, mode="limit", limit_price=100.005, expiry_seconds=4.0, max_spread_points=None),
        _quotes(),
    )
    assert market.status == "FILLED"
    assert market.fill_price == 100.010
    assert limit.status == "FILLED"
    assert limit.fill_price == 100.004
    assert limit.adverse_slippage_points == 0.0


def test_gate4_deterministic_spread_transform():
    spike = SpreadSpike(multiplier=5.0, candle_epoch=1000.0, open_window_seconds=30.0)
    quote = SimQuote(1000.0, 100.0, 100.01, 0.001)
    stressed = spike.apply([quote])[0]
    assert stressed.spread_points == 50.0
    assert stressed.mid == quote.mid
