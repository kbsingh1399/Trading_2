import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))

from Terminal.Quantitative_Governance import (
    PortfolioBetaRisk,
    classify_market_regime,
    compute_orderflow_features,
    front_run_offset,
    regime_allows,
)


def test_normalized_orderflow_adds_cvd_ticks_and_decays_stale_l3():
    data = {
        "l2_book": {"bid_volume_usd": 300_000, "ask_volume_usd": 100_000},
        "liquidations": {"bands": [{"mid_px": 99.0, "amount_usd": 500_000}]},
        "recent_trades": [
            {"side": "BUY", "notional_usd": 80_000},
            {"side": "SELL", "notional_usd": 10_000},
        ],
        "cvd_history": [0.0, 100.0, 220.0],
        "l3_orders": [
            {"side": "BUY", "price": 99.5, "notional_usd": 200_000, "timestamp": 990.0},
            {"side": "BUY", "price": 99.5, "notional_usd": 200_000, "timestamp": 0.0},
        ],
    }
    fresh = compute_orderflow_features(data, 100.0, now_seconds=1_000.0)
    assert fresh["l2_imbalance"] == 0.5
    assert fresh["tick_imbalance"] > 0.0
    assert fresh["cvd_available"] is True
    assert fresh["l3_bid_count"] == 1  # the timestamp-zero order is past TTL
    assert fresh["long_score"] > fresh["short_score"]


def test_front_run_offset_is_tick_valid_and_scale_aware():
    small = front_run_offset(price=1.5, atr=0.02, point=0.001, spread_points=4)
    large = front_run_offset(price=85_000, atr=900, point=0.01, spread_points=20)
    assert small >= 0.002
    assert large >= 0.20
    assert large < 90.0


def test_regime_vetoes_requested_setups():
    bars = []
    price = 100.0
    for i in range(80):
        price += 0.8
        bars.append({"open": price - 0.2, "high": price + 0.3, "low": price - 0.3, "close": price})
    regime = classify_market_regime(bars)
    assert regime["available"] is True
    allowed, reason = regime_allows(regime, "MEAN_REVERSION", "SHORT")
    assert not allowed
    assert "momentum" in reason or "shock" in reason


def test_beta_risk_is_signed_and_neutral_hedges_reduce_net_factor_risk():
    model = PortfolioBetaRisk(lookback=96, min_observations=4)
    for i in range(12):
        ts = float(i)
        btc = 100.0 * math.exp(0.002 * i)
        model.update("BTC", btc, ts)
        model.update("SOL", 50.0 * math.exp(0.004 * i), ts)
        model.update("XRP", 2.0 * math.exp(-0.002 * i), ts)
    assert model.beta("SOL") > 1.0
    result = model.check_candidate(
        [{"symbol": "SOLUSD.p", "direction": "LONG", "risk_usd": 10.0}],
        asset="XRP", direction="LONG", risk_usd=10.0, equity_usd=5_000,
        max_net_fraction=0.02, max_gross_fraction=0.05,
    )
    assert result["projected_net_beta_risk_usd"] < result["current_net_beta_risk_usd"]
