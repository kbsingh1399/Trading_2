"""Tests/Test_Telemetry_Data_Integrity.py
=========================================
Data-integrity regression suite for the telemetry generator, from the
OX_ALPHA_66 full-repository forensics audit (2026-10-07).

Guards against the four critical defects found by the audit:
  C1  stale candle indicators presented as live (staleness fields now emitted)
  C2  "ema_200" silently computed as a ~96-period proxy (now null below
      EMA200_MIN_BARS, with ema_200_bars_used)
  C3  fabricated account/quote fallback constants on MT5 loss (now fail-closed:
      error marker + non-zero exit, live snapshot untouched)
  C4  synthetic reconstructions relabeled "REAL" (coverage markers passed
      through; liquidation source renamed MODEL_RECONSTRUCTED_OI_COHORTS)

100% offline and deterministic: every network fetcher and macro scraper is
replaced with fakes; no MT5 terminal is required.
"""
from __future__ import annotations

import json
import pathlib
import sys
import time
from datetime import datetime, timezone

import pytest

REPO_ROOT = pathlib.Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

import Terminal.Data_Factory.generate_telemetry_snapshot as gts


# --------------------------------------------------------------------- fakes
class FakeConnectedBridge:
    """Deterministic MT5 stand-in: 2 open positions, live quotes, 800 bars."""

    initialized = True

    def __init__(self, n_bars: int = 800, fx_zero_spread: bool = True):
        self.n_bars = n_bars
        self.fx_zero_spread = fx_zero_spread

    # -- account ----------------------------------------------------------
    def get_account_summary(self):
        return {
            "connected": True, "login": 5064568,
            "currency": "USD",
            "balance_usd": 4813.44, "equity_usd": 4815.26,
            "margin_usd": 590.18, "margin_free_usd": 4225.08,
            "margin_level_pct": 815.9,
        }

    def get_open_positions(self):
        return [
            {"ticket": 18625151, "symbol": "USWTI.p", "direction": "LONG",
             "volume": 0.19, "price_open": 91.2, "price_current": 91.313,
             "sl": 90.55, "tp": 92.825, "profit_usd": 2.15,
             "time": datetime(2026, 10, 7, 11, 56, 6, tzinfo=timezone.utc).timestamp()},
            {"ticket": 18630694, "symbol": "BTCUSD.pi", "direction": "LONG",
             "volume": 0.01, "price_open": 83380.0, "price_current": 83347.0,
             "sl": 82700.0, "tp": 85080.0, "profit_usd": -0.33,
             "time": datetime(2026, 10, 7, 12, 51, 3, tzinfo=timezone.utc).timestamp()},
        ]

    def get_pending_orders(self):
        return []

    def estimate_order(self, symbol, direction, entry, sl):
        return {"stop_loss_per_lot": abs(entry - sl), "margin_per_lot": 100}

    # -- symbols / quotes -------------------------------------------------
    def resolve_symbol(self, asset):
        return {"BTC": "BTCUSD.pi", "USWTI": "USWTI.p", "SP500": "SP500.p",
                "GBPUSD": "GBPUSD.pi"}.get(asset, f"{asset}.p")

    def get_symbol_price(self, symbol):
        if symbol == "BTCUSD.pi":
            return {"bid": 83342.0, "ask": 83358.0, "last": 83350.0, "spread": 16}
        if symbol == "USWTI.p":
            return {"bid": 91.318, "ask": 91.373, "last": 91.345, "spread": 55}
        if symbol == "SP500.p":
            return {"bid": 7787.48, "ask": 7787.78, "last": 7787.63, "spread": 30}
        if symbol == "GBPUSD.pi" and self.fx_zero_spread:
            # raw-spread account: bid == ask, commission billed separately
            return {"bid": 1.3205, "ask": 1.3205, "last": 1.3205, "spread": 0}
        return {"bid": 100.0, "ask": 100.1, "last": 100.05, "spread": 10}

    # -- bars ---------------------------------------------------------------
    def get_recent_bars(self, symbol, count=96, timeframe=None):
        period = {16385: 3600, 16388: 14400}.get(timeframe, 900)
        now = int(time.time() // period) * period
        n = min(count, self.n_bars)
        bars = []
        base = 100.0
        for i in range(n):
            t = now - (n - i) * period
            c = base + (i % 7) * 0.25
            bars.append({
                "time": t, "open": c - 0.1, "high": c + 0.3,
                "low": c - 0.4, "close": c, "volume": 10.0 + (i % 5),
            })
        return bars


class FakeDisconnectedBridge:
    initialized = False

    def get_account_summary(self):
        return {"connected": False, "error": "MT5 not connected"}


class FakeFNG:
    def value(self):
        return {"value": 71, "classification": "Greed", "as_of": 1791331200}


class FakeFarside:
    """Configurable: 'reported', 'placeholder' (today's unreported 0.0 row),
    or 'unreachable' (no rows at all)."""

    def __init__(self, mode="placeholder"):
        self.mode = mode

    def refresh(self, asset="BTC"):
        if self.mode == "unreachable":
            return []
        if self.mode == "reported":
            return [{"date": "06 Oct 2026", "date_epoch": 1.0, "total_musd": 118.8}]
        today = datetime.now(timezone.utc).strftime("%d %b %Y")
        return [{"date": today, "date_epoch": time.time(), "total_musd": 0.0}]


@pytest.fixture()
def offline(monkeypatch, tmp_path):
    """Remove every network dependency and repo-path side effect."""
    monkeypatch.setattr(gts, "fetch_crypto_depth_and_oi", lambda a: (a, {}, {}, {}))
    monkeypatch.setattr(gts, "fetch_crypto_cvd_buckets", lambda a: (a, []))
    monkeypatch.setattr(gts, "fetch_crypto_htf_ohlcv", lambda a: (a, [], []))
    monkeypatch.setattr(gts, "fetch_crypto_funding_history", lambda a: (a, []))
    monkeypatch.setattr(gts, "fetch_hyperdash_microstructure", lambda client, a: ("UNAVAILABLE", {"reason": "offline test"}))
    monkeypatch.setattr(gts, "compute_live_coinbase_premium_bps", lambda prems=None: 0.0)
    monkeypatch.setattr(gts, "FearGreedIndex", lambda: FakeFNG())
    monkeypatch.setattr(gts, "CANDLE_DIR", tmp_path / "candles")
    monkeypatch.setattr(gts, "ERROR_MARKER_PATH", tmp_path / "telemetry" / ".generator_error.json")
    return tmp_path


def _generate(tmp_path, bridge, farside_mode="placeholder"):
    gts.FarsideETFFlows = lambda: FakeFarside(farside_mode)
    out = tmp_path / "telemetry" / "live_snapshot_latest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = gts.generate_full_snapshot(
        bridge=bridge, telemetry_path=out,
        whale_state_path=tmp_path / "telemetry" / ".whale_wall_state.json",
    )
    return payload, out


# --------------------------------------------------------------------- tests
def test_wrong_account_generation_preserves_previous_snapshot(offline):
    bridge = FakeConnectedBridge()
    original = bridge.get_account_summary
    bridge.get_account_summary = lambda: original() | {"login": 123456}
    out = offline / "telemetry" / "live_snapshot_latest.json"
    out.parent.mkdir(parents=True)
    out.write_text('{"previous": true}')
    with pytest.raises(RuntimeError, match="identity/currency mismatch"):
        gts.generate_full_snapshot(bridge=bridge, telemetry_path=out)
    assert json.loads(out.read_text()) == {"previous": True}


def test_fail_closed_on_mt5_loss_no_fabricated_account(offline):
    """C3: a disconnected bridge must abort with an error marker and must NOT
    overwrite the previous live snapshot (no fabricated equity, no empty
    positions list advertising open capacity)."""
    out = offline / "telemetry" / "live_snapshot_latest.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text('{"as_of_utc": "PREVIOUS SNAPSHOT", "sentinel": true}')

    with pytest.raises(RuntimeError, match="FAIL_CLOSED"):
        gts.generate_full_snapshot(
            bridge=FakeDisconnectedBridge(), telemetry_path=out,
            whale_state_path=offline / "telemetry" / ".whale_wall_state.json",
        )

    # snapshot untouched; error marker written and fatal
    assert json.loads(out.read_text())["sentinel"] is True
    marker = json.loads(gts.ERROR_MARKER_PATH.read_text())
    assert marker["fatal"] is True
    assert "MT5 account summary unavailable" in marker["reason"]


def test_no_fabricated_account_constants_in_output(offline):
    """C3: the old hardcoded fallbacks (4834.50 / 4831.73 / 412.50 / 1172.0)
    must never appear when the bridge is connected either."""
    payload, _ = _generate(offline, FakeConnectedBridge())
    acc = payload["account"]
    assert acc["equity_usd"] == 4815.26 and acc["balance_usd"] == 4813.44
    assert acc["margin_used_usd"] == 590.18 and acc["margin_level_pct"] == 815.9
    blob = json.dumps(payload)
    for fabricated in ("4834.5", "4831.73", "412.5", "1172.0"):
        assert fabricated not in blob, f"fabricated constant leaked: {fabricated}"


def test_capacity_uses_canonical_four_joint_fill_slots(offline):
    payload, _ = _generate(offline, FakeConnectedBridge())
    cap = payload["capacity"]
    assert cap["max_concurrent"] == 4
    assert cap["policy"] == "JOINT_FILL_CAPACITY_AND_FLOOR_DEFENSE"
    assert cap["filled"] == 2 and cap["pending"] == 0
    assert cap["used_joint_fill"] == 2 and cap["available"] == 2
    assert "2/4" in cap["status"]
    assert "OPEN" in cap["status"]


def test_all_assets_have_actual_completed_broker_htf_history(offline):
    payload, _ = _generate(offline, FakeConnectedBridge())
    for row in payload["assets_matrix_24"].values():
        for key, interval in (("1h", 3600), ("4h", 14400)):
            bars = row[f"htf_{key}_ohlcv"]
            quality = row["htf_history"][key]
            assert len(bars) == quality["completed_count"] == 96
            assert quality["source"] == "MT5_BROKER_COMPLETED_BARS"
            assert quality["status"] == "READY"
            assert quality["strategy_minimum"] >= 50
            assert all(b["close_ts"] <= payload["as_of_epoch"] for b in bars)
            assert all(b["close_ts"] == b["ts"] + interval for b in bars)
            assert bars[-1]["close"] == 100 + (95 % 7) * 0.25


def test_insufficient_htf_history_stays_insufficient_without_padding(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=20))
    row = payload["assets_matrix_24"]["SP500"]
    assert len(row["htf_1h_ohlcv"]) == len(row["htf_4h_ohlcv"]) == 20
    assert row["htf_history"]["1h"]["status"] == "INSUFFICIENT_HISTORY"
    assert row["htf_history"]["4h"]["status"] == "INSUFFICIENT_HISTORY"
    assert row["htf_history"]["entry_eligible"] is False


@pytest.mark.parametrize("inventory", ["get_open_positions", "get_pending_orders"])
def test_none_inventory_aborts_without_advertising_zero_capacity(offline, inventory):
    bridge = FakeConnectedBridge()
    setattr(bridge, inventory, lambda: None)
    out = offline / "live_snapshot_latest.json"
    out.write_text('{"sentinel": true}')
    with pytest.raises(RuntimeError, match="inventory unavailable"):
        gts.generate_full_snapshot(bridge=bridge, telemetry_path=out)
    assert json.loads(out.read_text()) == {"sentinel": True}


def test_pending_orders_reserve_joint_capacity_risk_and_margin(offline):
    class PendingBridge(FakeConnectedBridge):
        def get_pending_orders(self):
            return [{"ticket": t, "symbol": "GBPUSD.pi", "direction": "LONG", "type": 2,
                     "volume": 0.2, "price_open": 1.3, "sl": 1.2, "tp": 1.5}
                    for t in (10, 11)]
    payload, _ = _generate(offline, PendingBridge())
    cap = payload["capacity"]
    assert cap["used_joint_fill"] == 4 and cap["available"] == 0
    assert "HARD_ADMISSION_FREEZE" in cap["status"]
    risk = payload["risk"]
    expected = (0.65 * 0.19 + 680 * 0.01 + 2 * 0.1 * 0.2) * 1.25 + 4 * 2
    assert risk["total_contingent_stress_usd"] == pytest.approx(expected)
    assert risk["pending_margin_on_fill_usd"] == 40
    assert payload["account"]["margin_used_usd"] == 590.18


def test_unknown_broker_stop_valuation_freezes_capacity_and_keeps_risk_null(offline):
    class UnknownRisk(FakeConnectedBridge):
        def estimate_order(self, *args):
            raise ValueError("broker unavailable")
    payload, _ = _generate(offline, UnknownRisk())
    assert payload["risk"]["status"] == "UNAVAILABLE"
    assert payload["risk"]["total_contingent_stress_usd"] is None
    assert payload["capacity"]["available"] == 0
    assert "HARD_ADMISSION_FREEZE" in payload["capacity"]["status"]


def test_ema200_null_below_min_bars(offline):
    """C2: with 100 bars the engine would silently emit an EMA96 proxy — the
    generator must emit null + bars_used + INSUFFICIENT_HISTORY instead."""
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=100))
    ci = payload["assets_matrix_24"]["SP500"]["causal_indicators"]
    assert ci["ema_200"] is None
    assert ci["ema_200_slope_3h_pct"] is None
    assert ci["ema_200_bars_used"] == 100
    assert ci["trend_regime"] == "INSUFFICIENT_HISTORY"


def test_ema200_live_with_full_history_and_slope_not_dead(offline):
    """C2/H2: with 800 bars a real EMA200 is emitted and the slope computes
    (the audit found slope == 0.0 for 24/24 assets, making BEARISH impossible)."""
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    ci = payload["assets_matrix_24"]["SP500"]["causal_indicators"]
    assert ci["ema_200"] is not None
    assert ci["ema_200_bars_used"] == 800
    assert ci["ema_200_slope_3h_pct"] is not None
    assert ci["trend_regime"] in ("BULLISH", "BEARISH", "RANGE_BOUND")


def test_indicator_staleness_fields_present(offline):
    """C1: every asset must declare where its bars came from and how old the
    last bar close is, so a frozen feed can never look live."""
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    for name, entry in payload["assets_matrix_24"].items():
        ci = entry["causal_indicators"]
        assert ci["indicators_source"] in ("LIVE_BRIDGE", "PARQUET_FALLBACK", "NONE")
        assert ci["indicator_age_min"] is not None and ci["indicator_age_min"] >= 0
        assert ci["bars_last_close_utc"]


def test_as_of_utc_remains_a_string(offline):
    """Regression: the bar-sync block used to shadow the as_of string with a
    float epoch, corrupting payload['as_of_utc'] whenever bars flowed."""
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    assert isinstance(payload["as_of_utc"], str) and "UTC" in payload["as_of_utc"]


def test_live_snapshot_contains_no_model_stop_or_liquidation_levels(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    assert payload["protocol"] == "omni.telemetry.v3.observed_only"
    assert payload["trade_authorization"].startswith("DENIED")
    for asset, row in payload["assets_matrix_24"].items():
        stops = row["structural_stop_clusters"]
        liqs = row["reconstructed_liquidations"]
        assert stops["source"] == "UNAVAILABLE" and stops["coverage"] == "NONE"
        assert stops["total_sell_stops_usd"] is None and stops["total_buy_stops_usd"] is None
        assert stops["top_sell_stop_clusters_below"] == stops["top_buy_stop_clusters_above"] == []
        assert liqs["source"] in ("UNAVAILABLE", "NOT_APPLICABLE")
        assert liqs["max_pain"] is None and liqs["top_long_cascade_bands_below"] == []
        assert liqs["top_short_squeeze_bands_above"] == []
        assert row["orderbook_live_depth"]["whale_walls_l3"] == []
        assert row["pioneer_microstructure_eval"]["confluence_trade_setup"] is None


def test_binance_observed_book_and_oi_remain_separate_from_mt5_and_wallet_l3(offline, monkeypatch):
    def observed(asset):
        if asset == "BTC":
            return asset, {"bids": [["100.0", "2000"]], "asks": [["100.1", "2500"]]}, \
                {"openInterest": "123.5", "time": 1791408000000}, \
                {"lastFundingRate": "0.0001", "markPrice": "100.05", "indexPrice": "100.0"}
        return asset, {}, {}, {}
    monkeypatch.setattr(gts, "fetch_crypto_depth_and_oi", observed)
    data, _ = _generate(offline, FakeConnectedBridge())
    btc = data["assets_matrix_24"]["BTC"]
    assert btc["quotes"]["mid"] == 83350.0  # separate MT5 venue
    book = btc["orderbook_live_depth"]
    assert book["source"] in ("REAL_BINANCE_FUTURES_L2", "REAL_BINANCE_FUTURES_L2_AND_HYPERDASH_L3")
    assert book["binance_mid"] == 100.05 and book["venue"] in ("BINANCE_USDM_FUTURES", "BINANCE_USDM_FUTURES_AND_HYPERLIQUID")
    assert book["bids_top20"][0][2] == 200000.0
    assert book["whale_walls_l3"] == []
    assert book["l2_wall_levels"][0]["persistence_status"] == "SAMPLED_ONLY_NOT_CONTINUOUS"
    liq = btc["reconstructed_liquidations"]
    assert liq["binance_futures_open_interest_contracts"] == 123.5
    assert liq["open_interest_source"] == "BINANCE_FUTURES_PUBLIC_REST"
    assert liq["source"] == "UNAVAILABLE" and liq["max_pain"] is None
    assert btc["funding_and_rates"]["last_funding_rate_bps"] == 1.0


def test_missing_quote_and_volume_are_null_not_synthesized(offline):
    class NoQuoteOrVolume(FakeConnectedBridge):
        def get_symbol_price(self, symbol):
            return {}
        def get_recent_bars(self, symbol, count=96, timeframe=None):
            return [{**b, "volume": 0, "tick_volume": 0}
                    for b in super().get_recent_bars(symbol, count, timeframe)]
    payload, _ = _generate(offline, NoQuoteOrVolume())
    row = payload["assets_matrix_24"]["BTC"]
    assert row["quotes"]["quote_source"] == "UNAVAILABLE"
    assert row["quotes"]["bid"] is row["quotes"]["ask"] is row["quotes"]["spread_bps"] is None
    assert row["causal_indicators"]["session_vwap_utc"] is None
    assert row["volume_profile"]["source"] == "UNAVAILABLE_NO_OBSERVED_VOLUME"
    assert row["volume_profile"]["poc"] is None


def test_coinbase_premium_failure_is_null_not_binance_mark_index(monkeypatch):
    def down(*args, **kwargs):
        raise OSError("coinbase unavailable")
    monkeypatch.setattr(gts.urllib.request, "urlopen", down)
    assert gts.compute_live_coinbase_premium_bps(
        {"BTC": {"markPrice": 100, "indexPrice": 90}}) is None


def test_orderbook_unavailable_is_honest_for_crypto_without_depth(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    ob = payload["assets_matrix_24"]["BTC"]["orderbook_live_depth"]
    assert ob["source"] == "UNAVAILABLE_L1_ONLY"
    assert ob["bids_top20"] == [] and ob["whale_walls_l3"] == []


def test_etf_placeholder_is_null_not_zero(offline):
    """M1: Farside's current-day 0.0 row is a placeholder, not a reported
    zero flow."""
    payload, _ = _generate(offline, FakeConnectedBridge(), farside_mode="placeholder")
    etf = payload["macro_calendar"]["etf_net_flows"]
    assert etf["BTC_net_usd_millions"] is None
    assert etf["BTC_report_status"] == "NOT_YET_REPORTED"


def test_etf_reported_value_passes_through(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(), farside_mode="reported")
    etf = payload["macro_calendar"]["etf_net_flows"]
    assert etf["BTC_net_usd_millions"] == 118.8
    assert etf["BTC_report_status"] == "REPORTED"


def test_etf_unreachable_is_null(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(), farside_mode="unreachable")
    etf = payload["macro_calendar"]["etf_net_flows"]
    assert etf["BTC_net_usd_millions"] is None
    assert etf["BTC_report_status"] == "UNAVAILABLE"


def test_fx_zero_spread_flagged(offline):
    """H5: raw-spread FX quotes (spread 0.0, commission excluded) must carry
    the caveat so friction math never assumes a free round trip."""
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    g = payload["assets_matrix_24"]["GBPUSD"]["quotes"]
    assert g["quote_source"] == "MT5_L1_TICK"
    assert g.get("spread_caveat") == "RAW_ZERO_SPREAD_COMMISSION_EXCLUDED"


def test_quote_source_labeled(offline):
    payload, _ = _generate(offline, FakeConnectedBridge(n_bars=800))
    assert payload["assets_matrix_24"]["BTC"]["quotes"]["quote_source"] == "MT5_L1_TICK"
    assert "specs_source" in payload["assets_matrix_24"]["BTC"]["quotes"]


def test_held_plans_carry_stale_data_hold():
    """H1: both plans authored during the stale-indicator window must carry an
    explicit staging hold referencing the forensics audit."""
    for name in ("OX_ALPHA_66_SP500_Long_EMA200_20261007",
                 "OX_ALPHA_66_GBPUSD_Long_PostFOMC_20261007"):
        path = REPO_ROOT / "docs" / "trade_plans" / f"{name}.json"
        plan = json.loads(path.read_text())
        assert plan.get("staging_hold") is True, name
        assert "forensics audit" in plan.get("staging_hold_reason", "")
        assert plan.get("superseded_by_audit", "").endswith("Data_Forensics_Audit_20261007.md")
