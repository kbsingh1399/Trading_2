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


# --------------------------------------------------------------------------- #
# EV target horizon -- the calibrated win rate is geometry-blind
# --------------------------------------------------------------------------- #

def test_ev_refuses_a_target_beyond_the_calibrated_horizon():
    """p_win_lower_bound carries no distance information, so the expectancy test
    gets more permissive as the target recedes. A 10.77 ATR target must be
    refused even though its raw RR is the best in the set.
    """
    entry, atr = 82_906.0, 104.3256
    sl = entry - 1.5 * atr
    tp = 84_030.0                      # named short-liquidation pool, 10.77 ATR out
    v = dg.model2_checklist(_base_ctx(
        atr=atr, entry=entry, sl=sl, tp=tp, sigma_bar=atr,
        regime="TREND_UP", wall=_wall(), risk_usd=15.0, round_trip_cost_usd=1.53,
    ))
    assert "EV_target_beyond_calibrated_horizon" in v.failures
    assert v.metrics["dist_tp_atr"] > 10.0
    # the driftless barrier probability must be surfaced so the inversion is visible
    assert 0.10 < v.metrics["p_barrier_driftless"] < 0.15


def test_ev_accepts_a_target_inside_the_calibrated_horizon():
    entry, atr = 82_906.0, 104.3256
    sl = entry - 1.5 * atr
    tp = entry + 2.5 * atr             # 2.5 ATR -- inside the 4.0 ATR policy bound
    v = dg.model2_checklist(_base_ctx(
        atr=atr, entry=entry, sl=sl, tp=tp, sigma_bar=atr,
        regime="TREND_UP", wall=_wall(), risk_usd=15.0, round_trip_cost_usd=1.53,
    ))
    assert "EV_target_beyond_calibrated_horizon" not in v.failures
    assert v.metrics["dist_tp_atr"] == pytest.approx(2.5, rel=1e-9)


def test_ev_target_horizon_bound_is_four_atr():
    assert dg.MAX_TARGET_DIST_ATR == 4.0
    entry, atr = 100.0, 1.0
    sl = entry - 1.5 * atr
    # exactly at the bound: allowed
    v = dg.model1_checklist(_base_ctx(atr=atr, entry=entry, sl=sl, tp=entry + 4.0 * atr))
    assert "EV_target_beyond_calibrated_horizon" not in v.failures
    # one tick past it: refused
    v = dg.model1_checklist(_base_ctx(atr=atr, entry=entry, sl=sl, tp=entry + 4.01 * atr))
    assert "EV_target_beyond_calibrated_horizon" in v.failures


# --------------------------------------------------------------------------- #
# Two-sided grid wallets -- the mirror test cannot see a ladder
# --------------------------------------------------------------------------- #

from microstructure_state import two_sided_grid_addresses  # noqa: E402


def _grid_row(addr, side, price, notional=1_005_000.0, persist=420.0):
    return {"address": addr, "side": side, "price": price, "notional_usd": notional,
            "persist_s": persist, "presence_frac": 1.0,
            "wall_class": "GENUINE", "gate_g7_eligible": True}


def test_grid_wallet_quoting_both_sides_is_identified():
    """The shape observed live on BTC at 23:53 UTC: one wallet laddering ~1.0M USD
    down the bid and up the ask at different prices. No pair sits within the 0.05%
    mirror tolerance, so every leg classifies GENUINE.
    """
    walls = [
        _grid_row("0xgrid", "BUY", 82_847.0),
        _grid_row("0xgrid", "BUY", 82_932.0, persist=180.0),
        _grid_row("0xgrid", "SELL", 82_989.0, persist=300.0),
        _grid_row("0xgrid", "SELL", 83_072.0),
    ]
    assert two_sided_grid_addresses(walls) == {"0xgrid"}


def test_one_sided_wallet_is_not_a_grid():
    walls = [
        _grid_row("0xwhale", "BUY", 82_900.0, notional=500_000.0),
        _grid_row("0xwhale", "BUY", 82_850.0, notional=500_000.0),
        _grid_row("0xother", "SELL", 83_200.0),
    ]
    assert two_sided_grid_addresses(walls) == set()


def test_bracket_with_fresh_opposite_leg_is_still_a_grid():
    """REGRESSION for the loophole that let 0x95995f30 through at 01:21:31 UTC.

    A 1.0M USD SELL leg is not a phantom because its persist_s happens to be 0.
    Two-sidedness is judged on notional presence, never on persistence: how long
    a leg has rested is an artefact of when the poller first saw it, not of the
    wallet's intent. Gating the bracket test on G-7 persistence let 28 of 119
    bracketed wallets (23.5%) escape classification matrix-wide, and the aged
    leg of each was then accepted as directional backing.
    """
    walls = [
        _grid_row("0xw", "BUY", 82_900.0),
        {"address": "0xw", "side": "SELL", "price": 83_100.0, "notional_usd": 1_000_000.0,
         "persist_s": 0.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": False},
    ]
    assert two_sided_grid_addresses(walls) == {"0xw"}


def test_live_0121_bracketed_wallet_is_not_directional_backing():
    """The exact 0x95995f30 footprint from the 2026-10-11 01:21:31 UTC snapshot.

    402,290 USD of bids against 402,788 USD of asks -- a ratio of 1.0012. Only
    the 240s-persisted BUY leg cleared G-7; the 60s asks did not, so the wallet
    escaped criterion (1) and its stale bid read as the sole clean wall behind
    mid. Both legs must be rejected.
    """
    walls = [
        {"address": "0x95995f30", "side": "BUY", "price": 82_920.0, "notional_usd": 201_110.0,
         "persist_s": 240.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
        {"address": "0x95995f30", "side": "BUY", "price": 82_949.0, "notional_usd": 201_180.0,
         "persist_s": 240.0, "presence_frac": 1.0,
         "wall_class": "MIRRORED_LEG", "gate_g7_eligible": False},
        {"address": "0x95995f30", "side": "SELL", "price": 83_020.0, "notional_usd": 201_353.0,
         "persist_s": 60.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": False},
        {"address": "0x95995f30", "side": "SELL", "price": 83_054.0, "notional_usd": 201_435.0,
         "persist_s": 60.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": False},
    ]
    assert two_sided_grid_addresses(walls) == {"0x95995f30"}
    ctx = _build(walls, direction="LONG", entry=82_924.5)
    assert ctx["wall"] is None
    assert ctx["wall_data_present"] is False


def test_asymmetric_hedge_below_bracket_band_is_not_criterion_two():
    """A 200k bid against a 5.0M ask is not bracketed inventory (ratio 25x).

    Criterion (2) requires comparable size. This wallet is only flagged when it
    also satisfies criterion (1), i.e. G-7 persistence on both sides -- which it
    does here, so it is caught, but by the persistent-grid test, not the band.
    """
    walls = [
        _grid_row("0xh", "BUY", 82_900.0, notional=200_000.0, persist=420.0),
        _grid_row("0xh", "SELL", 83_400.0, notional=5_000_000.0, persist=420.0),
    ]
    assert two_sided_grid_addresses(walls) == {"0xh"}
    # Drop the persistence on the ask and criterion (1) no longer applies; the
    # 25x ratio is outside the bracket band, so the bid stands as directional.
    walls[1]["persist_s"] = 0.0
    walls[1]["gate_g7_eligible"] = False
    assert two_sided_grid_addresses(walls) == set()


def test_small_opposite_side_below_notional_floor_is_not_bracketed():
    """A genuine directional whale may carry a sub-floor hedge."""
    walls = [
        _grid_row("0xd", "BUY", 82_900.0, notional=1_000_000.0),
        {"address": "0xd", "side": "SELL", "price": 83_300.0, "notional_usd": 140_000.0,
         "persist_s": 0.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": False},
    ]
    assert two_sided_grid_addresses(walls) == set()


def test_bracket_band_edges_are_inclusive():
    at_min = [
        _grid_row("0xa", "BUY", 82_900.0, notional=1_000_000.0, persist=0.0),
        _grid_row("0xa", "SELL", 83_100.0, notional=500_000.0, persist=0.0),
    ]
    at_max = [
        _grid_row("0xb", "BUY", 82_900.0, notional=500_000.0, persist=0.0),
        _grid_row("0xb", "SELL", 83_100.0, notional=1_000_000.0, persist=0.0),
    ]
    assert two_sided_grid_addresses(at_min) == {"0xa"}
    assert two_sided_grid_addresses(at_max) == {"0xb"}
    just_outside = [
        _grid_row("0xc", "BUY", 82_900.0, notional=1_000_000.0, persist=0.0),
        _grid_row("0xc", "SELL", 83_100.0, notional=499_000.0, persist=0.0),
    ]
    assert two_sided_grid_addresses(just_outside) == set()


def test_grid_detection_needs_an_address():
    walls = [_grid_row("", "BUY", 100.0), _grid_row("", "SELL", 101.0)]
    assert two_sided_grid_addresses(walls) == set()


def test_grid_detection_is_malformed_input_safe():
    assert two_sided_grid_addresses([]) == set()
    assert two_sided_grid_addresses(None) == set()
    assert two_sided_grid_addresses([None, 5, "x", {}]) == set()
    assert two_sided_grid_addresses([
        {"address": "0xa", "side": "BUY", "price": 1.0, "notional_usd": "bad",
         "persist_s": 400.0, "presence_frac": 1.0,
         "wall_class": "GENUINE", "gate_g7_eligible": True},
    ]) == set()


def test_context_excludes_grid_legs_and_keeps_the_one_sided_whale():
    """The live BTC case: 17 grid rows plus one genuinely directional 500k bid.
    Only the 500k bid may back the position.
    """
    walls = [_grid_row("0xgrid", "BUY", 82_940.0 + i, notional=400_000.0, persist=300.0)
             for i in range(6)]
    walls += [_grid_row("0xgrid", "SELL", 83_050.0 + i, notional=400_000.0, persist=300.0)
              for i in range(6)]
    walls.append({"address": "0x90cc9850", "side": "BUY", "price": 82_990.0,
                  "notional_usd": 500_000.0, "persist_s": 480.0, "presence_frac": 1.0,
                  "wall_class": "GENUINE", "gate_g7_eligible": True})
    wall = _build(walls, direction="LONG", entry=83_000.0)["wall"]
    assert wall is not None
    assert wall["usd"] == 500_000.0


def test_context_reports_no_wall_when_only_grid_inventory_is_behind_entry():
    walls = [_grid_row("0xgrid", "BUY", 82_990.0, notional=900_000.0, persist=600.0)]
    walls += [_grid_row("0xgrid", "SELL", 83_050.0, notional=900_000.0, persist=600.0)]
    ctx = _build(walls, direction="LONG", entry=83_000.0)
    assert ctx["wall"] is None
    assert ctx["wall_data_present"] is False


# --------------------------------------------------------------------------- #
# Live counterfactual validation of the two-sided grid filter, measured on
# production telemetry rather than a synthetic fixture.
#
# BTC, generation 372c3b6eb5ad42d6b9014559f70845ce (2026-10-11 05:50:09 UTC),
# mid 82,977.0, ATR 120.9956, 0.25 ATR band [82,946.75, 83,007.25]:
#
#   WITHOUT two_sided_grid_addresses: 20 BUY legs from 6 wallets, aggregate
#   5,597,913 USD, all gate_g7_eligible=True, all wall_class=GENUINE, persist
#   360-1,760s, presence_frac 1.000. The best sits at 82,977.00 -- exactly at
#   mid, dist 0.0000 ATR -- 373,383 USD, persist 1,279.9s.
#   WITH the filter: 0 legs, 0.00 USD.
#
# Every one of the 20 passes every authenticity test the producer applies. Only
# two-sidedness rejects them. Absent commit 91ffffc, G-7 would have PASSED on BTC
# this cycle on a market-making grid.
#
# Wallet 0xecb63caa47 illustrates the lag: at 05:20:51 it was BUY-only (13 legs,
# 150,152.09-150,156.46 USD, $152-156 above MIN_POOL_NOTIONAL_USD) and escaped the
# grid filter, refused only by the producer's MIRRORED_LEG / gate_g7_eligible=false
# veto. By 05:50:09 it had posted 4 SELL legs at 83,071-83,081 and the grid filter
# caught it. Neither layer alone covers both observations.
# --------------------------------------------------------------------------- #

_GRID_0550 = "0xcf3f419d08"
_LADDER_0550 = "0xecb63caa47"

# (address, side, price, notional_usd, persist_s, presence_frac, class, eligible)
_LIVE_0550_ROWS = [
    (_GRID_0550,   "BUY",  82_977.00,   373_383.0, 1279.9, 1.000, "GENUINE",      True),
    (_LADDER_0550, "BUY",  82_976.00,   150_155.0, 1760.0, 1.000, "GENUINE",      True),
    (_GRID_0550,   "BUY",  82_972.00,   196_553.0, 1519.9, 1.000, "GENUINE",      True),
    (_GRID_0550,   "BUY",  82_971.00,   373_356.0, 1279.9, 1.000, "GENUINE",      True),
    (_LADDER_0550, "BUY",  82_971.00,   150_158.0,  780.0, 1.000, "GENUINE",      True),
    (_LADDER_0550, "BUY",  82_969.00,   150_157.0,  780.0, 1.000, "GENUINE",      True),
    (_GRID_0550,   "BUY",  82_967.00,   196_541.0, 1279.9, 1.000, "GENUINE",      True),
    (_LADDER_0550, "BUY",  82_967.00,   150_158.0,  780.0, 1.000, "GENUINE",      True),
    (_GRID_0550,   "BUY",  82_966.00,   373_334.0, 1640.0, 1.000, "GENUINE",      True),
    (_LADDER_0550, "BUY",  82_963.00,   150_157.0,  720.0, 1.000, "GENUINE",      True),
    (_LADDER_0550, "SELL", 83_071.00,   150_160.0, 1399.9, 1.000, "GENUINE",      True),
    (_LADDER_0550, "SELL", 83_075.00,   150_161.0, 1579.9, 0.963, "GENUINE",      True),
    (_LADDER_0550, "SELL", 83_077.00,   150_160.0, 1340.0, 1.000, "GENUINE",      True),
    (_LADDER_0550, "SELL", 83_081.00,   150_160.0, 1080.0, 1.000, "GENUINE",      True),
    (_GRID_0550,   "SELL", 83_050.00,   373_400.0, 1279.9, 1.000, "GENUINE",      True),
]

_MID_0550 = 82_977.0
_ATR_0550 = 120.9956


def _rows_0550():
    return [{"address": a, "side": s, "price": p, "notional_usd": n,
             "persist_s": ps, "presence_frac": pf, "wall_class": c,
             "gate_g7_eligible": e}
            for a, s, p, n, ps, pf, c, e in _LIVE_0550_ROWS]


def _behind_mid_0550(walls, apply_grid):
    grid = two_sided_grid_addresses(walls) if apply_grid else set()
    out = []
    for w in walls:
        if str(w["address"]).strip() in grid:
            continue
        if w["gate_g7_eligible"] is not True or w["wall_class"] != "GENUINE":
            continue
        if w["notional_usd"] < 150_000.0 or w["persist_s"] < 180.0 or w["presence_frac"] < 0.9:
            continue
        dist = (_MID_0550 - w["price"]) / _ATR_0550
        if 0 <= dist <= 0.25:
            out.append((dist, w))
    out.sort(key=lambda x: x[0])
    return out


def test_without_the_grid_filter_the_live_0550_book_would_have_passed_g7():
    """20 legs / 5.6M USD qualified on the real book; the grid filter zeroes it."""
    walls = _rows_0550()
    unfiltered = _behind_mid_0550(walls, apply_grid=False)
    filtered = _behind_mid_0550(walls, apply_grid=True)
    assert len(unfiltered) >= 9
    assert sum(w["notional_usd"] for _, w in unfiltered) > 1_000_000.0
    # The best leg sits exactly at mid with 21 minutes of persistence.
    best_dist, best = unfiltered[0]
    assert best["price"] == 82_977.00
    assert best_dist == pytest.approx(0.0, abs=1e-9)
    assert best["notional_usd"] == 373_383.0
    assert best["persist_s"] == 1279.9
    # Every one of them passes the producer's own authenticity tests.
    assert all(w["gate_g7_eligible"] is True and w["wall_class"] == "GENUINE"
               for _, w in unfiltered)
    assert filtered == []


def test_the_ladder_wallet_was_one_sided_at_0520_and_two_sided_by_0550():
    """The escape and the catch, one cycle apart, from the same wallet."""
    buys_only = [{"address": _LADDER_0550, "side": "BUY", "price": p,
                  "notional_usd": 150_155.0, "persist_s": ps, "presence_frac": 1.0,
                  "wall_class": "GENUINE", "gate_g7_eligible": True}
                 for p, ps in ((82_963.0, 720.0), (82_967.0, 780.0), (82_969.0, 780.0),
                               (82_971.0, 780.0), (82_976.0, 1760.0))]
    assert two_sided_grid_addresses(buys_only) == set(), \
        "a one-sided ladder is invisible to the grid filter by construction"
    revealed = buys_only + [{"address": _LADDER_0550, "side": "SELL", "price": p,
                             "notional_usd": 150_160.0, "persist_s": ps,
                             "presence_frac": 1.0, "wall_class": "GENUINE",
                             "gate_g7_eligible": True}
                            for p, ps in ((83_071.0, 1399.9), (83_077.0, 1340.0),
                                          (83_081.0, 1080.0))]
    assert two_sided_grid_addresses(revealed) == {_LADDER_0550}


def test_a_freshly_posted_leg_still_cannot_launder_an_aged_opposite_leg():
    """Criterion (2): two-sidedness is judged without any persistence requirement.

    The live ladder posts legs at persist_s 0 / 60 / 120 alongside aged ones. If
    persistence gated the two-sidedness test, a fresh leg would hide the wallet and
    its aged opposite leg would be read as directional backing.
    """
    walls = [{"address": _LADDER_0550, "side": "BUY", "price": 82_970.0,
              "notional_usd": 400_000.0, "persist_s": 1200.0, "presence_frac": 1.0,
              "wall_class": "GENUINE", "gate_g7_eligible": True},
             {"address": _LADDER_0550, "side": "SELL", "price": 83_060.0,
              "notional_usd": 400_000.0, "persist_s": 0.0, "presence_frac": 1.0,
              "wall_class": "GENUINE", "gate_g7_eligible": False}]
    assert two_sided_grid_addresses(walls) == {_LADDER_0550}


def test_dg_context_excludes_the_live_0550_grid_book_end_to_end():
    """The real payload shape must yield ctx["wall"] is None and wall_data_present False."""
    day_start = 1_791_648_000  # 2026-10-11 00:00 UTC, same UTC day as the quote
    # The quote must post-date every bar close: _session_vwap rejects any history
    # whose bar has not yet closed at the observation instant.
    quote = {"bid": _MID_0550 - 8.0, "ask": _MID_0550 + 8.0, "tick_size": 0.01,
             "point": 0.01, "time_msc": (day_start + 40 * 900 + 9) * 1000}
    bars = []
    for i in range(40):
        ts = day_start + i * 900
        c = _MID_0550 + (i % 5) * 6.0 - 12.0
        bars.append({"open": c - 4.0, "high": c + 9.0, "low": c - 9.0, "close": c,
                     "time": ts, "close_ts": ts + 900, "volume": 100.0 + i})
    payload = {"orderbook_live_depth": {"whale_walls_l3": _rows_0550(),
                                        "l2_wall_levels": []}}
    ctx, missing = dg_context.build_dg_context(
        features={"direction": "LONG", "atr": _ATR_0550}, payload=payload,
        pivots=None, quote=quote, bars_15m=bars, entry=_MID_0550,
        sl=_MID_0550 - 1.5 * _ATR_0550, tp=_MID_0550 + 1.5 * _ATR_0550,
        sizing={"risk_usd": 15.0, "friction_usd": 1.2},
        regime="MEAN_REVERT", symbol="BTC")
    assert "session_vwap_history_unavailable" not in missing
    assert ctx["wall"] is None, "a two-sided grid must never satisfy whale backing"
    assert ctx["wall_data_present"] is False
