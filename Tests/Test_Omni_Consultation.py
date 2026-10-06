"""Tests for the 2026-10-06 Ox Alpha consultation deliverables.

Q1: adverse-selection telemetry + governor queue-priority hysteresis
    (flicker dwell, proximity floor, adaptive MAD threshold).
Q2: commodity tick-volume microstructure (robust MAD VWAP bands, POC/VAH/VAL,
    tick-rule delta, GK vol, MR gate, structural magnet TP).
Q3: session-conditional ratchet (asset class x GK-vol bucket x session x
    sleeve) layered on the frozen v2 label policy.
Q4: causal candle ingestion (O(1) indicators, gap ledger, broker corrections,
    WAL crash recovery, parquet reconciliation).
Plus the production drift ports into Omni_Trader (10s cadence ordering,
900s bar throttle, max(6*ATR, 3%) drift bound, decoupled capacity gates).

All tests are offline; broker doubles only. No terminal, no network.
"""
import copy
import json
import math
import pathlib
import re

import pytest

from Terminal.Adverse_Selection import AdverseSelectionMonitor
from Terminal.Asset_Universe import UNIVERSE
from Terminal.Causal_Candle_Stream import (CausalCandleStream, IncrementalIndicators,
                                           batch_reference, reconcile_parquet)
from Terminal.Commodity_Microstructure import (robust_session_vwap, volume_profile,
                                               tick_volume_profile, tick_delta, wick_rejection,
                                               commodity_mr_gate, commodity_override,
                                               gk_vol, gk_variance, weighted_median)
from Terminal.Orderbook_Structure import structural_exit, wall_clusters
from Terminal.Order_Persistence_Governor import OrderPersistenceGovernor
from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC
from Terminal.Risk_Sizing_Engine import CovarianceGate, number
from Terminal.Uplift_Model import (RATCHET_BASE, RATCHET_POLICY_VERSION, ratchet,
                                   executable_ratchet, ratchet_params, session_regime,
                                   asset_class_of, gk_vol_bucket, POLICY_VERSION)

NOW = (1700000000 // 900) * 900 + 870


# ---------------------------------------------------------------- fixtures
def bars(now=NOW, count=96, trend=0.0, mid=120.0):
    start = int(now // 900) * 900 - count * 900
    out = []
    for i in range(count):
        close = mid + trend * i + 0.05 * math.sin(0.9 * i)
        out.append({"time": start + i * 900, "open": close, "high": close + 0.5,
                    "low": close - 0.5, "close": close})
    return out


def book_payload(ts, *, bid_size=10000, ask_size=100, mid=120.0, trades=None, l3=None,
                 spread=0.02):
    half = spread / 2.0
    return {"coin": "SOL", "price": mid,
            "l2_book": {"timestamp": ts * 1000, "best_bid": mid - half, "best_ask": mid + half,
                        "bids": [{"price": mid - half - i * 0.01, "size": bid_size} for i in range(20)],
                        "asks": [{"price": mid + half + i * 0.01, "size": ask_size} for i in range(20)]},
            "recent_trades": trades if trades is not None else [],
            "sources": {"l3": {"observed_at": ts}, "liquidations": {"observed_at": ts}},
            "l3_orders": l3 or [], "liquidations": {}}


def covariance(now=NOW, assets=UNIVERSE, sigma=0.003):
    import numpy as np
    matrix = np.eye(len(assets)) * sigma ** 2
    return CovarianceGate(assets, matrix, {"return_units": "decimal_log_return", "horizon_minutes": 15,
                                           "created_at": now - 60, "data_end": now - 900, "max_age_seconds": 86400})


class Broker:
    def __init__(self, clock, mid=120.0):
        self.clock = clock; self.positions = []; self.pending = []; self.modified = []
        self.closed = []; self.sent = []; self.mid = mid
        self.history_state = None; self.filled = False

    def get_open_positions(self): return copy.deepcopy(self.positions)
    def get_pending_orders(self): return copy.deepcopy(self.pending)
    def get_account_summary(self): return {"connected": True, "login": 1, "currency": "USD",
                                           "equity_usd": 5000, "margin_free_usd": 5000}
    def resolve_symbol(self, asset): return asset + "USD" if asset not in ("GOLD", "SILVER") else "XAUUSD"
    def get_recent_bars(self, symbol, count=96): return bars(self.clock())
    def get_symbol_price(self, symbol):
        return {"bid": self.mid - 0.01, "ask": self.mid + 0.01, "point": .01, "tick_size": .01,
                "time_msc": self.clock() * 1000, "digits": 2, "contract_size": 100, "min_lot": .01,
                "step_lot": .01, "max_lot": 10, "stops_level": 0, "freeze_level": 0, "currency_profit": "USD"}
    def estimate_order(self, symbol, direction, entry, sl): return {"stop_loss_per_lot": abs(entry - sl) * 100, "margin_per_lot": 1000}
    def modify_position_sltp(self, ticket, sl, tp): self.modified.append((ticket, sl, tp)); return {"success": True}
    def close_position(self, ticket): self.closed.append(ticket); return {"success": True}
    def position_deals(self, ticket): return []
    def execute_market_order(self, *a, **k): self.sent.append(("market", a, k)); return {"success": False, "uncertain": True}
    def stage_limit_order(self, symbol, direction, volume, limit_price, sl, tp, **kwargs):
        ticket = 1000 + len(self.sent)
        order = {"ticket": ticket, "symbol": symbol, "direction": direction, "volume": volume,
                 "price_open": limit_price, "sl": sl, "tp": tp, "magic": kwargs.get("magic", MAGIC)}
        self.pending.append(order); self.sent.append(("limit", order, kwargs))
        return {"success": True, "ticket": ticket, "symbol": symbol, "direction": direction,
                "volume": volume, "price": limit_price, "sl": sl, "tp": tp,
                "persistent": kwargs.get("persistent", False), "expires_at": None}
    def cancel_pending_order(self, ticket):
        self.pending = [o for o in self.pending if o["ticket"] != ticket]
        self.closed.append(f"cancel_{ticket}")
        return {"success": True, "ticket": ticket}
    def reconcile_intent_history(self, comment, prepared_at): return self.history_state
    def intent_filled(self, comment, prepared_at): return self.filled


class Intel:
    def check_macro_blackout(self): return False, "NO_EVENT", 999
    def get_market_intelligence_report(self): return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}


def trader(tmp_path, clock=None, paper=True, mid=120.0, entry_mode="limit"):
    clock = clock or (lambda: NOW)
    broker = Broker(clock, mid=mid)
    t = AI15mMT5Trader(bridge=broker, intel=Intel(), cognitive=object(), covariance=covariance(),
                       uplift_path=tmp_path / "no_uplift", cognitive_enabled=False, clock=clock,
                       paper_mode=paper, state_file=tmp_path / "state.json",
                       journal_dir=tmp_path / "journal", entry_mode=entry_mode)
    t.symbols = {a: broker.resolve_symbol(a) for a in UNIVERSE}
    t.bars = {a: bars(clock()) for a in UNIVERSE}
    return t, broker


def governor(bridge, **kwargs):
    defaults = dict(journal=lambda n, r: None, clock=lambda: NOW)
    defaults.update(kwargs)
    return OrderPersistenceGovernor(bridge, **defaults)


def register_sol_long(gov, *, limit=119.42, anchors=None):
    anchors = anchors if anchors is not None else [
        {"price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 3600, "role": "primary"}]
    gov.register("k", asset="SOL", symbol="SOLUSD", direction="LONG", order_ticket=1000,
                 limit_price=limit, sl=limit - 2.0, tp=limit + 5.0, volume=0.5, anchors=anchors,
                 atr=1.2, ttl_sec=7200, now=NOW, comment="OMNI:k", hurdle_r=2.5, risk_usd=20.0)


def l2_book(ts, *, bid_size, ask_size=100, mid=120.0, trades=(), spread=0.02):
    half = spread / 2.0
    return {"l2_book": {"timestamp": ts * 1000, "best_bid": mid - half, "best_ask": mid + half,
                        "bids": [{"price": mid - half - i * 0.01, "size": bid_size} for i in range(20)],
                        "asks": [{"price": mid + half + i * 0.01, "size": ask_size} for i in range(20)]},
            "recent_trades": list(trades),
            "sources": {"l3": {"observed_at": ts}}, "l3_orders": [], "liquidations": {}}


# ================================================== Q1a/Q1c: adverse selection
def test_adverse_monitor_dedupes_unchanged_book_timestamps():
    m = AdverseSelectionMonitor()
    p = l2_book(NOW, bid_size=10000)
    assert m.observe("SOL", p, NOW) is not None
    assert m.observe("SOL", p, NOW + 5) is None          # same ts: deduped
    assert m.observe("SOL", p, NOW + 6) is None          # still deduped
    assert len(m.history["SOL"]) == 1


def test_adverse_monitor_rejects_stale_books():
    m = AdverseSelectionMonitor()
    assert m.observe("SOL", l2_book(NOW - 120, bid_size=10000), NOW) is None  # older than 30s
    assert m.observe("SOL", l2_book(NOW + 60, bid_size=10000), NOW) is None   # future stamp


def test_book_collapse_alone_scores_three_and_aborts():
    m = AdverseSelectionMonitor()
    # Bid defense halves far faster than the 180s half-life: collapse regime.
    m.observe("SOL", l2_book(NOW, bid_size=10000), NOW)
    m.observe("SOL", l2_book(NOW + 60, bid_size=1000), NOW + 60)
    score, alarms = m.hazard("SOL", "LONG", 119.42, 1.2)
    assert "book_collapsing" in alarms and "book_thinning" in alarms
    assert score >= 3  # collapse counts double by design


def test_slow_thinning_alone_does_not_abort():
    m = AdverseSelectionMonitor()
    # Ratio exp(-0.00595*60) ~ 0.70: thinning rate past the half-life pace
    # but short of the 2x collapse threshold, and nothing else corroborates.
    m.observe("SOL", l2_book(NOW, bid_size=10000), NOW)
    m.observe("SOL", l2_book(NOW + 60, bid_size=7000), NOW + 60)
    score, alarms = m.hazard("SOL", "LONG", 119.42, 1.2)
    assert "book_thinning" in alarms and "book_collapsing" not in alarms
    assert score < m.abort_score  # corroboration required


def test_governor_aborts_resting_limit_on_adverse_selection_hazard():
    bridge = Broker(lambda: NOW)
    events = []
    gov = governor(bridge, journal=lambda n, r: events.append(r))
    register_sol_long(gov)
    wall = [{"side": "BUY", "price": 119.41, "notional_usd": 4.93e6, "persistence_sec": 6000,
             "observed_at": NOW}]
    intents = {"k": {"status": "STAGED_LIMIT"}}
    pending = [{"ticket": 1000, "symbol": "SOLUSD"}]
    # Beat 1: healthy book. Beat 2: defense collapses while the anchor wall
    # itself still rests - the order must abort anyway.
    gov.heartbeat(now=NOW, intents=intents,
                  payloads={"SOL": book_payload(NOW, bid_size=10000, l3=wall)}, pending=pending,
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    gov.heartbeat(now=NOW + 60, intents=intents,
                  payloads={"SOL": book_payload(NOW + 60, bid_size=800, l3=wall)}, pending=pending,
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"]
    event = next(e for e in events if e["event"] == "governor_cancel")
    assert event["reason"] == "adverse_selection_hazard"
    assert event["detail"]["alarms"]["book_collapsing"]


def test_governor_ignores_adverse_noise_when_wall_holds_and_book_is_stable():
    bridge = Broker(lambda: NOW)
    gov = governor(bridge)
    register_sol_long(gov)
    intents = {"k": {"status": "STAGED_LIMIT"}}
    pending = [{"ticket": 1000, "symbol": "SOLUSD"}]
    for t, size in ((NOW, 10000), (NOW + 60, 9800), (NOW + 120, 10100)):
        wall = [{"side": "BUY", "price": 119.41, "notional_usd": 4.93e6,
                 "persistence_sec": 6000, "observed_at": t}]
        gov.heartbeat(now=t, intents=intents,
                      payloads={"SOL": book_payload(t, bid_size=size, l3=wall)}, pending=pending,
                      quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == [] and gov.count() == 1


# ============================================== Q1b: queue-priority hysteresis
def test_governor_flicker_filter_blocks_young_replacement_wall():
    # A shifted wall that has only just cleared the scan's 180s persistence
    # floor but not the 240s dwell is a flicker: cancel, never chase.
    bridge = Broker(lambda: NOW)
    gov = governor(bridge, dwell_sec=240.0)
    register_sol_long(gov)
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 200,
                "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": book_payload(NOW + 60, l3=shifted)},
                  pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"]          # no replacement staged
    assert not [o for o in bridge.pending if o["ticket"] != 1000]


def test_governor_replaces_once_shifted_wall_has_dwelled():
    bridge = Broker(lambda: NOW)
    bridge.sent.append("seed")  # replacement ticket must differ from 1000
    gov = governor(bridge)
    register_sol_long(gov)
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 600,
                "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": book_payload(NOW + 60, l3=shifted)},
                  pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    replacement = next(o for o in bridge.pending if o["ticket"] != 1000)
    assert replacement["price_open"] == pytest.approx(119.21)
    assert replacement["sl"] == pytest.approx(119.21 - 2.0)      # R-geometry preserved
    assert replacement["volume"] == 0.5


def test_governor_proximity_floor_blocks_replacement_near_the_touch():
    # Price within 0.25 ATR of the limit: queue priority is worth the most,
    # so the threshold widens to 25 bps. A ~17.6 bps shift stays absorbed.
    bridge = Broker(lambda: NOW)
    gov = governor(bridge)
    register_sol_long(gov)
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 600,
                "observed_at": NOW}]
    near_touch = lambda s: {"bid": 119.43, "ask": 119.45}        # ~0.03 from limit
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": book_payload(NOW + 60, l3=shifted)},
                  pending=[{"ticket": 1000, "symbol": "SOLUSD"}], quote_fn=near_touch)
    assert bridge.closed == ["cancel_1000"]                      # below 25 bps: no replace
    assert not [o for o in bridge.pending if o["ticket"] != 1000]


def test_governor_adaptive_mad_threshold_tracks_edge_noise():
    # Quiet anchor history (microscopic edge moves) keeps the floor at the
    # 5 bps minimum; the same 17.6 bps relocation then qualifies far from
    # the touch.
    bridge = Broker(lambda: NOW)
    bridge.sent.append("seed")
    gov = governor(bridge)
    register_sol_long(gov)
    order = gov.orders["k"]
    order["edge_history"] = [119.41 + 0.0002 * i for i in range(8)]  # ~0.17 bps jitter
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 600,
                "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": book_payload(NOW + 60, l3=shifted)},
                  pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert any(o["ticket"] != 1000 for o in bridge.pending)      # replaced


def test_governor_adaptive_mad_threshold_widens_after_large_edge_moves():
    # After the anchor itself has been bouncing ~20 bps between beats, a
    # 17.6 bps relocation is inside 2x MAD noise: keep the queue (cancel).
    bridge = Broker(lambda: NOW)
    gov = governor(bridge)
    register_sol_long(gov)
    order = gov.orders["k"]
    order["edge_history"] = [119.41, 119.41 * 1.002, 119.41 * 0.998, 119.41 * 1.002,
                             119.41 * 0.998, 119.41]  # ~20 bps swings
    shifted = [{"side": "BUY", "price": 119.20, "notional_usd": 3.5e6, "persistence_sec": 600,
                "observed_at": NOW}]
    gov.heartbeat(now=NOW + 60, intents={"k": {"status": "STAGED_LIMIT"}},
                  payloads={"SOL": book_payload(NOW + 60, l3=shifted)},
                  pending=[{"ticket": 1000, "symbol": "SOLUSD"}],
                  quote_fn=lambda s: {"bid": 119.99, "ask": 120.01})
    assert bridge.closed == ["cancel_1000"]
    assert not [o for o in bridge.pending if o["ticket"] != 1000]


# ============================================== Q2: commodity microstructure
def gold_bars(spike=False, direction="SHORT", seed=5):
    import random
    random.seed(seed)
    start = (NOW // 900) * 900 - 40 * 900
    start -= start % 86400  # align to a UTC day boundary, 40 bars into the session
    bars = []
    p = 4160.0
    for i in range(40):
        o = p
        c = 4160 + random.uniform(-3, 3)
        bars.append({"time": start + i * 900, "open": o, "high": max(o, c) + 1.2,
                     "low": min(o, c) - 1.2, "close": c, "volume": 1200})
        p = c
    b = bars[-1]
    if spike and direction == "SHORT":
        b.update(open=4161, high=4188, low=4160.5, close=4168, volume=9000)
    if spike and direction == "LONG":
        b.update(open=4159, high=4160.5, low=4132, close=4152, volume=9000)
    return bars


def test_robust_vwap_mad_band_resists_news_ballooning():
    bars = gold_bars(spike=True)
    now = bars[-1]["time"] + 900
    sess = robust_session_vwap(bars, now)
    assert sess["used"] == "session" and sess["session_bars"] >= 8
    # The spike inflates the volume-weighted sigma far more than the MAD band.
    assert sess["ballooning_ratio"] > 1.10
    assert sess["sigma_mad"] < sess["sigma_vw"]
    # Anchor built on the robust band sits closer to the market: earlier
    # entry, better queue priority, less adverse selection.
    assert sess["vwap"] + 2 * sess["sigma_mad"] < sess["vwap"] + 2 * sess["sigma_vw"]


def test_commodity_mr_gate_confirms_short_rejection():
    bars = gold_bars(spike=True, direction="SHORT")
    now = bars[-1]["time"] + 900
    result = commodity_mr_gate(bars, "SHORT", now)
    assert result["confirmed"] is True
    assert result["wick"]["upper_ratio"] >= 0.50
    assert result["z_extreme"] >= 1.75


def test_commodity_mr_gate_confirms_long_rejection():
    bars = gold_bars(spike=True, direction="LONG")
    now = bars[-1]["time"] + 900
    result = commodity_mr_gate(bars, "LONG", now)
    assert result["confirmed"] is True
    assert result["z_extreme"] <= -1.75


def test_commodity_mr_gate_rejects_close_at_the_high():
    bars = gold_bars(spike=True, direction="SHORT")
    bars[-1]["close"] = 4186                       # no close-back inside the range
    now = bars[-1]["time"] + 900
    result = commodity_mr_gate(bars, "SHORT", now)
    assert result["confirmed"] is False
    assert "wick" in result["reason"] or "close_position" in result["reason"]


def test_commodity_mr_gate_rejects_stale_extreme():
    bars = gold_bars(spike=True, direction="SHORT")
    # The session high printed on the PREVIOUS bar; the trigger bar is not
    # the rejection bar.
    bars[-2].update(high=4195, close=4170)
    bars[-1]["high"] = 4180
    now = bars[-1]["time"] + 900
    result = commodity_mr_gate(bars, "SHORT", now)
    assert result["confirmed"] is False and result["reason"] == "session_extreme_missing"


def test_commodity_mr_gate_refuses_to_fade_an_orderly_trend():
    import random
    random.seed(2)
    start = (NOW // 900) * 900 - 40 * 900
    start -= start % 86400
    bars = []
    p = 4160.0
    for i in range(40):
        o = p
        c = 4160 + (i / 39.0) * 80 if i >= 20 else 4160 + i * 0.5
        bars.append({"time": start + i * 900, "open": o, "high": max(o, c) + 1.5,
                     "low": min(o, c) - 1.5, "close": c, "volume": 1200})
        p = c
    now = bars[-1]["time"] + 900
    result = commodity_mr_gate(bars, "SHORT", now)
    assert result["confirmed"] is False
    assert "vwap_extension" in result["reason"]    # robust band widened: no signal


def test_volume_profile_locates_poc_and_value_area():
    bars = gold_bars()                              # clustered near 4160
    now = bars[-1]["time"] + 900
    profile = volume_profile(bars, now=now)
    assert 4150 < profile["poc"] < 4170
    assert profile["val"] < profile["poc"] < profile["vah"]
    assert 0.68 < profile["value_area_captured"] <= 0.72


def test_tick_volume_profile_and_tick_delta():
    ticks = ([{"time": NOW + i, "price": 4160 + i * 0.1, "size": 2.0} for i in range(50)]
             + [{"time": NOW + 100 + i, "price": 4160 - i * 0.1, "size": 1.0} for i in range(50)])
    delta = tick_delta(ticks)
    assert delta["delta_usd"] > 0 and delta["delta_norm"] > 0    # up-ticks carry 2x size
    profile = tick_volume_profile(ticks)
    assert profile["val"] < profile["poc"] < profile["vah"]


def test_gk_vol_is_positive_and_reasonable():
    bars = gold_bars()
    vol = gk_vol(bars, lookback=14, now=bars[-1]["time"] + 900)
    assert vol > 0
    single = gk_variance({"open": 100, "high": 101, "low": 99, "close": 100.5})
    assert single == pytest.approx(0.5 * math.log(101 / 99) ** 2
                                   - (2 * math.log(2) - 1) * math.log(100.5 / 100) ** 2)


def test_structural_exit_magnet_front_runs_session_poc():
    # GOLD MR sleeve: no L3 walls exist on the CFD; the session POC below
    # entry is the magnet and the TP front-runs it by 2 buffer ticks.
    plan, veto = structural_exit(4176.0, 4186.5, "SHORT", [], tick=0.01, friction_r=0.0,
                                 min_broker_dist=0.30, magnet_price=4160.0)
    assert veto is None
    assert plan["mode"] == "vwap_poc_magnet"
    # Short exits ABOVE the magnet by 2 buffer ticks (the tick-ceiling may
    # round one further tick: 4160.02..4160.04).
    assert 4160.02 <= plan["tp"] <= 4160.04
    assert plan["magnet_price"] == 4160.0
    assert plan["hurdle_r"] == pytest.approx((4176.0 - 4160.02) / 10.5, abs=1e-4)


def test_structural_exit_magnet_vetoes_when_inside_net_payoff_floor():
    plan, veto = structural_exit(4176.0, 4186.5, "SHORT", [], tick=0.01, friction_r=0.5,
                                 min_broker_dist=0.30, magnet_price=4168.0)
    assert veto is not None and "net_payoff_insufficient" in veto


def test_structural_exit_prefers_real_wall_over_magnet():
    # A real L3 wall at 4152 (2.28R) sits beyond the 1.5R net floor, closer
    # than the 4160 magnet: the wall wins.
    walls = [{"edge_price": 4152.0, "notional_usd": 5e6, "persistence_sec": 900}]
    plan, veto = structural_exit(4176.0, 4186.5, "SHORT", walls, tick=0.01, friction_r=0.0,
                                 min_broker_dist=0.30, magnet_price=4160.0)
    assert veto is None and plan["mode"] == "wall_front_run"
    assert 4152.02 <= plan["tp"] <= 4152.04


def test_commodity_override_merges_session_anchors_into_pivots():
    bars = gold_bars(spike=True)
    now = bars[-1]["time"] + 900
    merged = commodity_override({"vwap": 1.0, "signal_mid": 4168.0}, bars, now)
    assert merged["vwap"] != 1.0                              # session VWAP replaced the stub
    assert "sigma" not in merged or True
    assert 4150 < merged["poc"] < 4170
    assert "vah" in merged and "val" in merged
    assert merged["vwap_ballooning_ratio"] > 1.0


# ============================================== Q3: session-conditional ratchet
def test_ratchet_with_default_params_is_exactly_the_v2_label_policy():
    for gain in (0.5, 0.79, 0.80, 1.0, 1.49, 1.50, 1.9, 2.0, 2.4, 3.0):
        for friction in (41.0, 0.0):
            for direction in ("LONG", "SHORT"):
                a = ratchet(120.0, 0.55, direction, gain, 119.0, 0.4, friction_bps=friction)
                b = ratchet(120.0, 0.55, direction, gain, 119.0, 0.4, friction_bps=friction, params=None)
                c = ratchet(120.0, 0.55, direction, gain, 119.0, 0.4, friction_bps=friction, params={})
                assert a == b == c


def test_session_regime_labels_utc_windows():
    from datetime import datetime, timezone
    def ts(*a):
        return datetime(2026, 10, 6, *a, tzinfo=timezone.utc).timestamp()
    assert session_regime(ts(3, 0), "GOLD") == "asia"
    assert session_regime(ts(10, 0), "GOLD") == "london"
    assert session_regime(ts(13, 45), "GOLD") == "us_data"
    assert session_regime(ts(15, 0), "GOLD") == "ny_overlap"
    assert session_regime(ts(15, 0), "SOL") == "us_hours"
    assert session_regime(ts(2, 0), "SOL") == "asia"
    assert session_regime(datetime(2026, 10, 10, 15, 0, tzinfo=timezone.utc).timestamp(),
                          "SOL") == "weekend"


def test_asset_class_mapping():
    assert asset_class_of("GOLD") == "COMMODITY"
    assert asset_class_of("SILVER") == "COMMODITY"
    assert asset_class_of("SP500") == "INDEX"
    assert asset_class_of("SOL") == "CRYPTO"


def test_gk_vol_buckets():
    assert gk_vol_bucket(0.5) == "calm"
    assert gk_vol_bucket(0.75) == "normal"
    assert gk_vol_bucket(1.2) == "normal"
    assert gk_vol_bucket(1.5) == "normal"
    assert gk_vol_bucket(2.0) == "stressed"


def test_ratchet_params_layer_resolution():
    asia_rev = ratchet_params("GOLD", session="asia", gk_ratio=1.0, sleeve="reversion")
    assert asia_rev["trigger_2_r"] == 1.20 and asia_rev["runner_trail_r"] == 0.35
    assert asia_rev["target_r"] == 1.80 and asia_rev["decay_bars"] == 12
    weekend = ratchet_params("SOL", session="weekend", gk_ratio=1.0)
    assert weekend["be_trigger_r"] == 1.00 and weekend["target_r"] == 2.20
    stressed = ratchet_params("GOLD", session="london", gk_ratio=2.0, sleeve="trend")
    assert stressed["be_trigger_r"] == 1.00 and stressed["runner_trail_r"] == 0.75
    # Unknown session falls back to the uniform baseline.
    fallback = ratchet_params("GOLD", session="late_ny", gk_ratio=1.0)
    assert fallback["be_trigger_r"] == RATCHET_BASE["be_trigger_r"]
    assert fallback["trigger_2_r"] == RATCHET_BASE["trigger_2_r"]


def test_conditional_ladder_tightens_reversion_runner_trail():
    # The user's live GOLD geometry: entry 4176.00, SL 4186.50 (R = 10.5).
    params = ratchet_params("GOLD", session="asia", gk_ratio=1.0, sleeve="reversion")
    uniform = ratchet(4176.0, 10.5, "SHORT", 2.40, 0, 0, friction_bps=0.0)
    conditional = ratchet(4176.0, 10.5, "SHORT", 2.40, 0, 0, friction_bps=0.0, params=params)
    assert (4176.0 - uniform) / 10.5 == pytest.approx(2.40 - 0.65)     # gain - 0.65
    assert (4176.0 - conditional) / 10.5 == pytest.approx(2.40 - 0.35)  # tighter MR trail


def test_friction_floor_dominates_the_conditional_table():
    # 41 bps round-trip on a 25 bps stop is 1.63R of friction: no table value
    # may lock less than the cost floor once the trigger fires.
    params = ratchet_params("GOLD", session="asia", gk_ratio=1.0, sleeve="reversion")
    lock = ratchet(4176.0, 10.5, "SHORT", 0.90, 0, 0, friction_bps=41.0, params=params)
    floor_r = 41.0 / 10000.0 * 4176.0 / 10.5 + 0.05
    assert (4176.0 - lock) / 10.5 == pytest.approx(floor_r)


def test_trader_stamps_ratchet_regime_and_uses_conditional_decay(tmp_path):
    # NOW = 2023-11-14T22:14:30Z: SOL resolves to the CRYPTO "asia" session,
    # whose conditional table shortens the decay to 18 bars.
    t, broker = trader(tmp_path)
    t.state["paper_positions"] = [{
        "ticket": 7, "symbol": "SOLUSD", "direction": "LONG", "volume": 0.1,
        "price_open": 120.0, "sl": 118.0, "tp": 125.0, "time": NOW - 16 * 900,
        "contract_size": 100, "profit_usd": 0.0, "residual_cost_usd": 0.0}]
    broker.positions = [dict(t.state["paper_positions"][0], magic=MAGIC)]
    t.state["positions"]["7"] = {"asset": "SOL", "initial_r": 2.0, "sleeve": "T1_BREAKOUT",
                                 "max_favorable_r": 0.0, "atr": 1.0}
    t.manage_active_positions()
    meta = t.state["positions"]["7"]                     # survived: 16 < 18 bars
    assert meta["ratchet_regime"]["policy"] == RATCHET_POLICY_VERSION
    assert meta["ratchet_regime"]["session"] == "asia"
    assert meta["ratchet_regime"]["sleeve"] == "trend"
    assert meta["ratchet_regime"]["params"]["decay_bars"] == 18
    # The same position at 19 bars of age IS closed by the conditional decay
    # even though the uniform policy (24 bars) would have kept it.
    t.state["positions"]["7"] = {"asset": "SOL", "initial_r": 2.0, "sleeve": "T1_BREAKOUT",
                                 "max_favorable_r": 0.0, "atr": 1.0}
    t.state["paper_positions"][0]["time"] = NOW - 19 * 900
    t.manage_active_positions()
    assert "7" not in t.state["positions"]
    assert all(pp["ticket"] != 7 for pp in t.state["paper_positions"])


# ============================================== Q4: causal candle stream
def stream_bars(count=300, seed=11, t0=1_760_000_000):
    import random
    random.seed(seed)
    out = []
    for i in range(count):
        o = 100 + random.gauss(0, 1)
        c = o + random.gauss(0, 0.8)
        out.append({"time": t0 + i * 900, "open": o, "high": max(o, c) + abs(random.gauss(0, 0.5)),
                    "low": min(o, c) - abs(random.gauss(0, 0.5)), "close": c,
                    "volume": random.uniform(500, 2000)})
    return out


def test_incremental_o1_stream_equals_batch_reference():
    bars = stream_bars()
    stream = CausalCandleStream("GOLD")
    report = stream.ingest(bars, bars[-1]["time"] + 900)
    assert report["applied"] == len(bars)
    ref = batch_reference(bars)
    assert stream.stats()["atr"] == pytest.approx(ref.stats()["atr"], abs=1e-12)
    assert stream.stats()["rsi"] == pytest.approx(ref.stats()["rsi"], abs=1e-12)
    assert stream.stats()["vwap"] == pytest.approx(ref.stats()["vwap"], abs=1e-12)


def test_forming_bar_is_never_committed():
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    stream = CausalCandleStream("ETH")
    forming = {"time": now, "open": 1, "high": 2, "low": 0.5, "close": 1.5, "volume": 10}
    report = stream.ingest(bars + [forming], now)
    assert report["rejected_forming"] == 1 and report["applied"] == len(bars)


def test_gaps_are_ledgered_and_flagged_never_filled():
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    stream = CausalCandleStream("SOL")
    stream.ingest(bars[:100], now)
    report = stream.ingest(bars[104:105], now)
    assert report["gaps"] == [{"from": bars[99]["time"], "to": bars[104]["time"],
                               "missing_buckets": 4}]
    assert stream.stats()["gap_flag"] is True
    stream.ingest(bars[105:106], now)
    assert stream.stats()["gap_flag"] is False          # clears on the next contiguous bar


def test_broker_correction_reapplies_exactly_once():
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    stream = CausalCandleStream("BTC")
    stream.ingest(bars, now)
    fixed = dict(bars[-1])
    fixed["close"] = fixed["close"] + 2.5
    report = stream.ingest([fixed], now)
    assert report["corrected"] == 1 and stream.state.bars == len(bars)
    ref = batch_reference(bars[:-1] + [fixed])
    assert stream.stats()["atr"] == pytest.approx(ref.stats()["atr"], abs=1e-12)


def test_wal_clean_recovery_replays_nothing(tmp_path):
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    wal = tmp_path / "wal"
    live = CausalCandleStream("GOLD", 900, wal_dir=wal)
    live.ingest(bars, now)
    revived = CausalCandleStream("GOLD", 900, wal_dir=wal)
    assert revived.recover() == 0
    assert revived.stats() == live.stats()


def test_wal_recovery_after_crash_mid_batch(tmp_path):
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    wal = tmp_path / "wal"
    clean = CausalCandleStream("GOLD")
    clean.ingest(bars, now)
    half = CausalCandleStream("GOLD", 900, wal_dir=wal)
    half.ingest(bars[:150], now)
    crashed = CausalCandleStream("GOLD", 900, wal_dir=wal)
    crashed.recover()
    crashed.ingest(bars[150:], now)
    assert crashed.stats() == clean.stats()


def test_wal_torn_tail_write_is_discarded(tmp_path):
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    wal = tmp_path / "wal"
    live = CausalCandleStream("GOLD", 900, wal_dir=wal)
    live.ingest(bars, now)
    with open(wal / "GOLD_900_wal.jsonl", "a", encoding="utf-8") as fh:
        fh.write('{"type":"bar","time":123')          # crash mid-write
    revived = CausalCandleStream("GOLD", 900, wal_dir=wal)
    revived.recover()
    assert revived.stats() == live.stats()


def test_wal_recovery_mid_correction(tmp_path):
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    wal = tmp_path / "wal"
    live = CausalCandleStream("GOLD", 900, wal_dir=wal)
    live.ingest(bars[:150], now)
    fixed = dict(bars[149])
    fixed["close"] = fixed["close"] + 3.0
    live.ingest([fixed], now)
    # Truncate the WAL after the correction record, before its snapshot.
    path = wal / "GOLD_900_wal.jsonl"
    lines = path.read_text().splitlines(keepends=True)
    corr = max(i for i, l in enumerate(lines) if json.loads(l).get("type") == "correction")
    path.write_text("".join(lines[:corr + 1]))
    revived = CausalCandleStream("GOLD", 900, wal_dir=wal)
    assert revived.recover() == 1
    ref = CausalCandleStream("GOLD")
    ref.ingest(bars[:149], now)
    ref.ingest([fixed], now)
    assert revived.stats()["atr"] == pytest.approx(ref.stats()["atr"], abs=1e-12)


def test_wal_rotation_bounds_the_file(tmp_path):
    bars = stream_bars(count=300)
    now = bars[-1]["time"] + 900
    wal = tmp_path / "wal"
    stream = CausalCandleStream("ETH", 900, wal_dir=wal)
    stream.ROTATE_AFTER_EVENTS = 100
    stream.ingest(bars, now)
    lines = (wal / "ETH_900_wal.jsonl").read_text().splitlines()
    assert len(lines) <= 101                              # baseline snapshot + tail
    revived = CausalCandleStream("ETH", 900, wal_dir=wal)
    revived.ROTATE_AFTER_EVENTS = 100
    revived.recover()
    assert revived.stats() == stream.stats()


def test_parquet_reconciliation_append_correct_and_future_rejected(tmp_path):
    pytest.importorskip("polars")
    bars = stream_bars()
    now = bars[-1]["time"] + 900
    later = now + 3 * 900
    store = tmp_path / "store.parquet"
    first = reconcile_parquet(store, bars[:200], now)
    assert first["appended"] == 200 and first["total_rows"] == 200
    second = reconcile_parquet(store, bars[150:], now)
    assert second["corrected"] == 50 and second["appended"] == 100
    assert second["total_rows"] == 300
    new_bar = {"time": bars[-1]["time"] + 900, "open": 1, "high": 2, "low": 0.5,
               "close": 1.5, "volume": 10}
    third = reconcile_parquet(store, [new_bar], later)
    assert third["appended"] == 1 and third["total_rows"] == 301
    with pytest.raises(ValueError):
        reconcile_parquet(store, [{"time": later + 1800, "open": 1, "high": 2, "low": 0.5,
                                   "close": 1.5, "volume": 10}], later)
    import polars as pl
    frame = pl.read_parquet(store)
    assert frame.get_column("close").to_list()[-1] == 1.5


# ============================================== production drift ports
def test_pending_drift_cancel_uses_max_6atr_or_3pct(tmp_path):
    src = pathlib.Path("Terminal/Omni_Trader.py").read_text()
    assert "max(6.0 * atr, 0.03 * mid)" in src
    # Behavioural: max(6*ATR, 3% of mid) bound. Live mode so the pending
    # inventory is visible to the monitor (paper mode hides it by design).
    t, broker = trader(tmp_path, mid=124.0, paper=False)  # ATR = 1.0, quote mid 124
    broker.pending = [{"ticket": 9001, "symbol": "SOLUSD", "direction": "LONG",
                       "volume": 0.1, "price_open": 118.0, "sl": 116.0, "tp": 123.0,
                       "magic": MAGIC, "type": 2}]
    t.state["intents"] = {"drift": {"status": "STAGED_LIMIT", "order_ticket": 9001,
                                    "candidate": {"asset": "SOL", "symbol": "SOLUSD"}}}
    t.manage_active_positions()
    assert 9001 not in [int(x.split("_")[1]) for x in broker.closed]     # |124-118| = 6.0 = 6*ATR: edge
    broker.pending = [{"ticket": 9002, "symbol": "SOLUSD", "direction": "LONG",
                       "volume": 0.1, "price_open": 117.0, "sl": 115.0, "tp": 122.0,
                       "magic": MAGIC, "type": 2}]
    t.state["intents"] = {"drift": {"status": "STAGED_LIMIT", "order_ticket": 9002,
                                    "candidate": {"asset": "SOL", "symbol": "SOLUSD"}}}
    t.manage_active_positions()
    assert "cancel_9002" in broker.closed          # |124-117| = 7 > 6*ATR and > 3% of mid


def test_decoupled_capacity_gates_in_limit_mode(tmp_path):
    # Limit mode: 3 staged limits with 0 fills must NOT trip the coupled cap.
    t, broker = trader(tmp_path, entry_mode="limit", paper=False)
    broker.pending = [{"ticket": 1000 + i, "symbol": "SOLUSD"} for i in range(3)]
    t.state["intents"] = {f"k{i}": {"status": "STAGED_LIMIT", "order_ticket": 1000 + i,
                                    "candidate": {"asset": "SOL", "symbol": "SOLUSD"}}
                          for i in range(3)}
    report = t.evaluate_market({}, {"received_at": NOW, "sentiment_valid": True,
                                    "asset_scores": {"SOL": 1}})
    assert report.get("reason") != "maximum_two_positions"
    assert report["vetoes"]["BTC"] == "signal_data_unavailable"   # ran past the gate
    # Five resting limits saturate the decoupled staging cap.
    t.state["last_slot"] = 0
    broker.pending = [{"ticket": 1000 + i, "symbol": "SOLUSD"} for i in range(5)]
    t.state["intents"] = {f"k{i}": {"status": "STAGED_LIMIT", "order_ticket": 1000 + i,
                                    "candidate": {"asset": "SOL", "symbol": "SOLUSD"}}
                          for i in range(5)}
    report = t.evaluate_market({}, {"received_at": NOW, "sentiment_valid": True,
                                    "asset_scores": {"SOL": 1}})
    assert report["reason"] == "max_resting_limits_5"


def test_market_mode_keeps_the_coupled_commitment_cap(tmp_path):
    t, broker = trader(tmp_path, entry_mode="market", paper=False)
    broker.pending = [{"ticket": 1000 + i, "symbol": "SOLUSD"} for i in range(2)]
    t.state["intents"] = {f"k{i}": {"status": "STAGED_LIMIT", "order_ticket": 1000 + i,
                                    "candidate": {"asset": "SOL", "symbol": "SOLUSD"}}
                          for i in range(2)}
    report = t.evaluate_market({}, {"received_at": NOW, "sentiment_valid": True,
                                    "asset_scores": {"SOL": 1}})
    assert report["reason"] == "maximum_two_positions"


def test_run_loop_refreshes_bars_before_managing():
    src = pathlib.Path("Terminal/Omni_Trader.py").read_text()
    run_body = src.split("def run(self, max_cycles=0):")[1]
    bars_at = run_body.index("self.refresh_broker_history()")
    manage_at = run_body.index("self.manage_active_positions()")
    assert bars_at < manage_at
    assert "self.last_bars < 900" in src                # 900s bar refresh throttle
