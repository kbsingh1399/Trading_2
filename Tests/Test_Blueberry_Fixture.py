import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from Terminal.Execution_Simulator import evaluate_fixture
from fixtures.generate_blueberry_quotes import build_fixture


def test_blueberry_fixture_covers_assets_spread_buckets_and_five_x_guard():
    fixture = build_fixture()
    report = evaluate_fixture(fixture)

    assert report["case_count"] == 72
    assert set(report["fill_rate_by_spread_bucket"]) == {"normal", "2x", "5x"}
    assert report["fill_rate_by_spread_bucket"]["normal"]["market"]["fill_rate"] == 1.0
    assert report["fill_rate_by_spread_bucket"]["5x"]["market"]["filled"] == 0
    assert report["fill_rate_by_spread_bucket"]["5x"]["limit"]["filled"] == 0
    assert report["five_x_spread_pass"]["pass"] is True


def test_blueberry_fixture_reports_limit_expiry_and_p95_slippage():
    report = evaluate_fixture(build_fixture())
    costs = report["limit_expiry_opportunity_cost"]

    assert costs["limit_expired_count"] == 16
    assert costs["limit_cancelled_spread_count"] == 40
    assert costs["market_filled_count"] == 32
    assert costs["missed_fill_count_vs_market"] == 16
    assert costs["missed_fill_rate_vs_market"] == 0.5
    assert costs["market_crossing_cost_points_mean"] == 15.25
    assert costs["market_crossing_cost_points_p95"] == 20.0
    assert report["p95_adverse_slippage_points"]["2x"]["market"]["p95_adverse_slippage_points"] == 10.0
