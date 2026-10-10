"""Whale-wall authenticity enforcement for gates A3 (Model 1) and B5 (Model 2).

Operator mandate #4: GENUINE L3 walls require ``gate_g7_eligible=true``.
``MIRRORED_LEG`` and ``TOP_OF_BOOK`` rows are bracket legs and touch prints -- not
net directional inventory -- and can never satisfy whale backing, regardless of
notional size or persistence duration.

Before this test module the A3/B5 ``ctx["wall"]`` path had zero coverage, which is
how a 1.05M USD / 2,476s ``MIRRORED_LEG`` bracket leg came to be able to satisfy
G-7. Every test here is hermetic: no network, no broker, no runtime state files.
"""

import os
import sys

import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
for _p in (ROOT, os.path.join(ROOT, "Terminal")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import decision_gates_v3 as dg  # noqa: E402
import dg_context  # noqa: E402


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def _base_ctx(**over):
    """A ctx carrying only what A3/B5 read; other gates will also fail, which is
    fine -- these tests assert on the presence/absence of specific failure codes."""
    ctx = {
        "direction": "SHORT",
        "regime": "MEAN_REVERT",
        "atr": 100.0,
        "sigma_bar": 20.0,
        "session_bars": 60,
        "vwap_z": 1.5,
        "vwap_z_change_4bars": 0.2,
        "sweep_z": -2.4,
        "session_sigma": 120.0,
        "vwap_slope_sigma_per_bar": 0.01,
        "vol_ratio_4_96": 1.2,
        "vwap": 82750.0,
        "entry": 83000.0,
        "sl": 83100.0,
        "tp": 82700.0,
        "spread": 1.5,
        "tick": 0.1,
        "risk_usd": 10.0,
        "round_trip_cost_usd": 1.0,
        "stop_slip_r": 0.10,
        "p_win_lower_bound": 0.4197,
        "sweep_extreme": 83050.0,
        "reclaim_close": True,
        "structure_intact": True,
        "exhaustion_flags": {"vol_spike": False, "long_wick": False},
        "geometry": {"retrace": 0.382, "depth_sigma": 1.0, "velocity_ratio": 0.4,
                     "bars_pullback": 4, "bars_impulse": 8},
        "shelf": {"price": 83000.0, "confluence": 2},
        "first_obstacle": 83300.0,
        "allow_price_only_variant": True,
        "orderflow": None,
        "wall": None,
    }
    ctx.update(over)
    return ctx


def _wall(**over):
    w = {
        "usd": 500_000.0,
        "persist_s": 600.0,
        "presence_frac": 1.0,
        "dist_from_entry_atr": 0.05,
        "median_1m_traded_usd": 25_000.0,
        "wall_class": "GENUINE",
        "gate_g7_eligible": True,
    }
    w.update(over)
    return w


def _bars_15m(n=120, base=83000.0):
    """Deterministic synthetic 15m bars with enough range for a stable ATR."""
    out = []
    ts = 1_760_000_000
    for i in range(n):
        c = base + (i % 7) * 12.0 - 36.0
        out.append({
            "open": c - 5.0, "high": c + 20.0, "low": c - 20.0, "close": c,
            "open_ts": ts + i * 900, "close_ts": ts + i * 900 + 900,
            "volume": 100.0 + i, "quote_volume": (100.0 + i) * c,
            "taker_buy_quote_volume": (50.0 + i) * c,
        })
    return out


# --------------------------------------------------------------------------- #
# A3 -- Model 1 whale backing
# --------------------------------------------------------------------------- #

def test_a3_accepts_a_genuine_g7_eligible_wall():
    v = dg.model1_checklist(_base_ctx(wall=_wall()))
    assert "A3_wall_not_g7_eligible" not in v.failures
    assert "A3_wall_not_net_directional_inventory" not in v.failures
    assert "A3_wall_not_persistent" not in v.failures
    assert "A3_wall_not_behind_entry" not in v.failures


def test_a3_rejects_mirrored_leg_even_at_over_a_million_usd_and_2476s():
    """The exact shape observed live on BTC at 2026-10-10 20:52 UTC."""
    v = dg.model1_checklist(_base_ctx(wall=_wall(
        usd=1_054_906.0, persist_s=2476.7, presence_frac=1.0,
        wall_class="MIRRORED_LEG", gate_g7_eligible=False,
    )))
    assert "A3_wall_not_g7_eligible" in v.failures
    assert "A3_wall_not_net_directional_inventory" in v.failures


def test_a3_rejects_top_of_book_touch_print():
    v = dg.model1_checklist(_base_ctx(wall=_wall(
        usd=1_484_975.0, persist_s=900.0,
        wall_class="TOP_OF_BOOK", gate_g7_eligible=False,
    )))
    assert "A3_wall_not_g7_eligible" in v.failures
    assert "A3_wall_not_net_directional_inventory" in v.failures


def test_a3_rejects_a_wall_flagged_eligible_but_classed_as_bracket_leg():
    """Class and flag are independent inputs; either one failing must reject."""
    v = dg.model1_checklist(_base_ctx(wall=_wall(
        wall_class="MIRRORED_LEG", gate_g7_eligible=True,
    )))
    assert "A3_wall_not_net_directional_inventory" in v.failures


def test_a3_missing_presence_frac_fails_closed_not_open():
    """The old default was presence_frac -> 1.0, which passed the >=0.9 test with
    no observation behind it. Absent evidence must fail. The admission validator
    now rejects the wall before A3 is even reached, which is the stronger outcome.
    """
    wall = _wall()
    del wall["presence_frac"]
    v = dg.model1_checklist(_base_ctx(wall=wall))
    assert not v.passed
    assert "data_invalid:wall.presence_frac" in v.failures
    assert "A3_wall_not_persistent" not in v.failures  # never reached, not silently passed


def test_a3_fails_closed_when_whale_backing_is_knowable_but_absent():
    """Payload carried eligible walls elsewhere in the book, none behind entry."""
    v = dg.model1_checklist(_base_ctx(wall=None, wall_data_present=True))
    assert "A3_no_eligible_whale_wall_behind_entry" in v.failures


def test_a3_still_skips_for_venues_with_no_l3_data():
    """CFDs are quoted on another venue; absence of data must not be a rejection."""
    v = dg.model1_checklist(_base_ctx(wall=None, wall_data_present=False))
    assert "A3_no_eligible_whale_wall_behind_entry" not in v.failures


# --------------------------------------------------------------------------- #
# B5 -- Model 2 whale backing
# --------------------------------------------------------------------------- #

def test_b5_accepts_a_genuine_g7_eligible_wall():
    v = dg.model2_checklist(_base_ctx(regime="TREND_DOWN", wall=_wall()))
    assert "B5_wall_not_g7_eligible" not in v.failures
    assert "B5_wall_not_net_directional_inventory" not in v.failures


def test_b5_rejects_mirrored_leg_bracket():
    v = dg.model2_checklist(_base_ctx(regime="TREND_DOWN", wall=_wall(
        usd=1_007_286.0, persist_s=419.8,
        wall_class="MIRRORED_LEG", gate_g7_eligible=False,
    )))
    assert "B5_wall_not_g7_eligible" in v.failures
    assert "B5_wall_not_net_directional_inventory" in v.failures


def test_b5_rejects_top_of_book_touch_print():
    v = dg.model2_checklist(_base_ctx(regime="TREND_DOWN", wall=_wall(
        usd=167_612.0, persist_s=0.0,
        wall_class="TOP_OF_BOOK", gate_g7_eligible=False,
    )))
    assert "B5_wall_not_g7_eligible" in v.failures
    assert "B5_wall_not_persistent" in v.failures


def test_b5_fails_closed_when_whale_backing_is_knowable_but_absent():
    v = dg.model2_checklist(_base_ctx(regime="TREND_DOWN", wall=None, wall_data_present=True))
    assert "B5_no_eligible_whale_wall_behind_entry" in v.failures


def test_b5_still_skips_for_venues_with_no_l3_data():
    v = dg.model2_checklist(_base_ctx(regime="TREND_DOWN", wall=None, wall_data_present=False))
    assert "B5_no_eligible_whale_wall_behind_entry" not in v.failures


# --------------------------------------------------------------------------- #
# dg_context selection: non-eligible rows must be filtered BEFORE selection
# --------------------------------------------------------------------------- #

def _payload(walls, eligible_present=True):
    return {
        "orderbook_live_depth": {"whale_walls_l3": walls},
        "orderflow": {"median_1m_flow_usd": 25_000.0},
    }


def _build(walls, direction="SHORT", entry=83000.0):
    features = {
        "direction": direction,
        "vwap_z": 1.5,
        "atr_14": 100.0,
        "session_vwap": 82750.0,
        "session_sigma": 120.0,
        "session_bars": 60,
    }
    quote = {"bid": entry - 0.8, "ask": entry + 0.8, "mid": entry,
             "spread_price": 1.6, "spread_bps": 1.9, "ts": 1_760_001_000}
    ctx, _missing = dg_context.build_dg_context(
        features, _payload(walls), None, quote, _bars_15m(),
        sizing={"risk_usd": 10.0, "friction_usd": 1.0},
        entry=entry, sl=entry + 100.0, tp=entry - 300.0,
        regime="MEAN_REVERT", symbol="BTCUSD",
    )
    return ctx


def test_context_prefers_genuine_wall_over_a_larger_longer_lived_bracket_leg():
    """A 1.05M/2,476s MIRRORED_LEG sits closer to entry than a 166k GENUINE wall.
    Size and age must not win: only the GENUINE row may be selected."""
    walls = [
        {"side": "SELL", "price": 83001.0, "notional_usd": 1_054_906.0,
         "persist_s": 2476.7, "presence_frac": 1.0,
         "wall_class": "MIRRORED_LEG", "gate_g7_eligible": False},
        {"side": "SELL", "price": 83010.0, "notional_usd": 166_000.0,
         "persist_s": 300.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]
    wall = _build(walls)["wall"]
    assert wall is not None
    assert wall["wall_class"] == "GENUINE"
    assert wall["gate_g7_eligible"] is True
    assert wall["usd"] == 166_000.0


def test_context_returns_no_wall_when_only_bracket_legs_are_in_range():
    walls = [
        {"side": "SELL", "price": 83001.0, "notional_usd": 1_054_906.0,
         "persist_s": 2476.7, "presence_frac": 1.0,
         "wall_class": "MIRRORED_LEG", "gate_g7_eligible": False},
        {"side": "BUY", "price": 82900.0, "notional_usd": 900_000.0,
         "persist_s": 900.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]
    ctx = _build(walls, direction="SHORT")
    assert ctx["wall"] is None
    # ...but the desk must be told backing was knowable, so A3 fails rather than skips.
    assert ctx["wall_data_present"] is True


def test_context_wall_data_present_is_false_when_nothing_is_eligible():
    walls = [
        {"side": "SELL", "price": 83001.0, "notional_usd": 1_054_906.0,
         "persist_s": 2476.7, "presence_frac": 1.0,
         "wall_class": "MIRRORED_LEG", "gate_g7_eligible": False},
    ]
    assert _build(walls)["wall_data_present"] is False


def test_context_rejects_an_eligible_wall_with_no_measured_presence_frac():
    """Previously an eligible wall with no presence_frac was granted 1.0 for free,
    passing the >= 0.9 persistence test on fabricated evidence. It must now be
    rejected outright -- an unmeasured wall cannot back a position at all.
    """
    walls = [
        {"side": "SELL", "price": 83005.0, "notional_usd": 400_000.0,
         "persist_s": 600.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]
    ctx = _build(walls)
    assert ctx["wall"] is None
    # Nothing eligible survived, and nothing else in the book qualified either, so
    # this is a genuine absence of data rather than a knowable-but-absent wall.
    assert ctx["wall_data_present"] is False


def test_context_stamps_authenticity_keys_for_gate_reverification():
    """A3/B5 re-assert the producer's veto, so the keys must always be present."""
    walls = [
        {"side": "SELL", "price": 83005.0, "notional_usd": 400_000.0,
         "persist_s": 600.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]
    wall = _build(walls)["wall"]
    assert wall is not None
    assert wall["wall_class"] == "GENUINE"
    assert wall["gate_g7_eligible"] is True


def test_context_ignores_l2_touch_rows_without_a_g7_flag():
    """l2_wall_levels rows carry no gate_g7_eligible key and must never be selected."""
    payload_walls = []
    ctx_features = {"direction": "SHORT", "vwap_z": 1.5, "atr_14": 100.0,
                    "session_vwap": 82750.0, "session_sigma": 120.0, "session_bars": 60}
    quote = {"bid": 82999.2, "ask": 83000.8, "mid": 83000.0,
             "spread_price": 1.6, "spread_bps": 1.9, "ts": 1_760_001_000}
    ctx, _ = dg_context.build_dg_context(
        ctx_features,
        {"orderbook_live_depth": {"l2_wall_levels": [
            {"side": "SELL", "price": 83000.0, "notional_usd": 1_484_975.0,
             "persist_s": 120.0, "presence_frac": 0.6667,
             "wall_class": "TOP_OF_BOOK"},
        ]}},
        None, quote, _bars_15m(),
        sizing={"risk_usd": 10.0, "friction_usd": 1.0},
        entry=83000.0, sl=83100.0, tp=82700.0, regime="MEAN_REVERT", symbol="BTCUSD",
    )
    assert payload_walls == []
    assert ctx["wall"] is None
    assert ctx["wall_data_present"] is False


def test_context_selects_the_nearest_eligible_wall_not_the_largest():
    walls = [
        {"side": "BUY", "price": 82999.0, "notional_usd": 166_000.0,
         "persist_s": 300.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
        {"side": "BUY", "price": 82980.0, "notional_usd": 9_000_000.0,
         "persist_s": 900.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]
    wall = _build(walls, direction="LONG")["wall"]
    assert wall is not None
    assert wall["usd"] == 166_000.0
