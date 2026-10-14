"""Repo test for Terminal/arena_tournament.py: the council's arbitration engine.

Verifies the properties the desk relies on when a tournament is used to decide
whether a ticket is staged, held, modified or deleted:

  * the rubric weights in code mirror .agent/skills/arena/rubric.md
  * sweep-cluster union arithmetic (touching bins chain into one hazard run)
  * purchase-side hazard: for a short, the SL must clear the BUY-stop cluster above
  * the 15% dynamic friction ceiling is fatal, not advisory
  * the <= 2.0 ATR entry-proximity bound is fatal, not advisory
  * a TP parked inside an un-swept magnet pool is fatal
  * joint-fill capacity stress obeys stressed = 1.25 * nominal + 2.00 per ticket
    against the 4,795.00 USD operating buffer
  * the same snapshot + cards + seed reproduce the same bracket (determinism)
  * the live Cycle-106 cards resolve exactly as the council reported them

The live-snapshot test is skipped when docs/telemetry/live_snapshot_latest.json
is absent so the suite stays green in a thin checkout.
"""
import json
import os
import re
import sys

import pytest

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if REPO not in sys.path:
    sys.path.insert(0, REPO)

from Terminal import arena_tournament as at  # noqa: E402

RUBRIC_PATH = os.path.join(REPO, ".agent", "skills", "arena", "rubric.md")
SNAPSHOT_PATH = os.path.join(REPO, "docs", "telemetry", "live_snapshot_latest.json")
CARDS_PATH = os.path.join(REPO, "docs", "trade_plans", "arena_cards", "cycle106_20261014.json")


# --------------------------------------------------------------------------
# fixtures
# --------------------------------------------------------------------------
def _asset(symbol="BTCUSD.pi", mid=100.0, atr=10.0, spread_price=0.02, spread_bps=2.0,
           contract=1.0, min_lot=0.01, regime="BEARISH", buy_stops=None, sell_stops=None,
           cascades=None, squeeze=None, walls=None, session_cvd=-1_000_000.0, ask=None):
    return {
        "symbol_broker": symbol,
        "quotes": {"mid": mid, "ask": ask if ask is not None else mid + spread_price / 2,
                   "bid": mid - spread_price / 2, "spread_price": spread_price,
                   "spread_bps": spread_bps, "quote_freshness": "TEST"},
        "execution_specs": {"contract_size": contract, "min_lot": min_lot},
        "causal_indicators": {"atr_14": atr, "trend_regime": regime},
        "structural_stop_clusters": {
            "nearest_buy_stop_clusters_above": buy_stops or [],
            "top_buy_stop_clusters_above": [],
            "nearest_sell_stop_clusters_below": sell_stops or [],
            "top_sell_stop_clusters_below": [],
        },
        "reconstructed_liquidations": {
            "nearest_long_cascade_bands_below": cascades or [],
            "top_long_cascade_bands_below": [],
            "nearest_short_squeeze_bands_above": squeeze or [],
            "top_short_squeeze_bands_above": [],
        },
        "orderbook_live_depth": {"whale_walls_l3": walls or [], "l2_wall_levels": []},
        "multi_horizon_cvd": {"session_cvd_usd": session_cvd},
        "tradfi_orderflow": {},
    }


def _bin(lo, hi, notional):
    return {"min_price": lo, "max_price": hi, "notional_usd": notional}


def _snap(asset, balance=4859.55, stress=13.875, available=3):
    return {
        "generation_id": "TESTGEN", "as_of_utc": "2026-10-14 20:56:21 UTC",
        "trade_authorization": "TEST",
        "account": {"balance_usd": balance, "login": 5064568},
        "risk": {"total_contingent_stress_usd": stress, "required_post_stop_equity_usd": 4795.0},
        "capacity": {"available": available},
        "assets_matrix_24": {"SYNTH": asset},
    }


def _card(**kw):
    base = dict(id="c1", action="STAGE", asset="SYNTH", side="SHORT",
                entry=110.0, sl=113.5, tp=101.0, lots=1.0)
    base.update(kw)
    return at.Card(**base)


def _codes(ev):
    return {f.code for f in ev.findings}


# --------------------------------------------------------------------------
# rubric parity
# --------------------------------------------------------------------------
def test_rubric_weights_mirror_the_written_rubric():
    """The engine must score with the words in rubric.md, not its own idea of them."""
    assert os.path.exists(RUBRIC_PATH), "arena rubric is part of the desk governance"
    text = open(RUBRIC_PATH, encoding="utf-8").read()
    for name, weight in at.RUBRIC_WEIGHTS:
        pattern = re.compile(rf"\|[^|]*{name}[^|]*\|\s*{weight}\s*\|", re.IGNORECASE)
        assert pattern.search(text), f"{name} {weight} not found in rubric.md"
    assert sum(w for _, w in at.RUBRIC_WEIGHTS) == 100


def test_personas_are_the_five_council_seats():
    names = [n for n, _ in at.PERSONAS]
    assert names == [
        "Orderflow & Microstructure",
        "Structural Price Action",
        "Liquidation & Stop Forensic",
        "Macro Risk & Portfolio Governor",
        "Adversarial Pre-Mortem Red Team",
    ]


# --------------------------------------------------------------------------
# hazard mathematics
# --------------------------------------------------------------------------
def test_hazard_union_chains_touching_bins():
    bins = [(90.0, 92.0, 1e6), (92.0, 94.0, 2e6), (94.0, 96.0, 3e6), (80.0, 82.0, 9e6)]
    lo, hi, members = at.hazard_union(bins, 93.0)
    assert (lo, hi) == (90.0, 96.0)
    assert sum(m[2] for m in members) == 6e6  # the disconnected 80-82 bin is not swept in


def test_hazard_union_returns_none_when_price_sits_outside_every_bin():
    assert at.hazard_union([(90.0, 92.0, 1e6)], 200.0) == (None, None, [])


def test_short_sl_inside_the_purchase_side_cluster_is_fatal():
    """Operator directive: a stop may never sit inside the sweep pool. For a short the
    sweep pool is the BUY-stop cluster above the entry."""
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev = at.evaluate_card(_card(sl=113.5), _snap(asset), {})
    assert "SL_INSIDE_SWEEP" in _codes(ev)
    assert ev.fatal() and not ev.qualified
    f = next(f for f in ev.findings if f.code == "SL_INSIDE_SWEEP")
    assert f.purchase_side is True
    assert f.values["union"] == [113.0, 114.0]


def test_short_sl_clearing_the_cluster_by_a_full_atr_is_accepted():
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev = at.evaluate_card(_card(sl=124.0), _snap(asset), {})
    assert "SL_INSIDE_SWEEP" not in _codes(ev)
    assert ev.metrics["sl_clearance_atr"] == pytest.approx(1.0)


def test_thin_stop_buffer_under_035_atr_is_fatal():
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev = at.evaluate_card(_card(sl=114.1), _snap(asset), {})  # 0.01 ATR clearance
    assert "SL_BUFFER_THIN" in _codes(ev)
    assert ev.fatal()


def test_entry_parked_inside_unswept_purchase_side_fuel_is_flagged():
    asset = _asset(buy_stops=[_bin(109.0, 111.0, 2_000_000), _bin(113.0, 114.0, 4_000_000)],
                   sell_stops=[_bin(98.0, 99.0, 3_000_000)])
    ev = at.evaluate_card(_card(entry=110.0, sl=115.0, tp=98.5), _snap(asset), {})
    assert "ENTRY_IN_FUEL" in _codes(ev)


# --------------------------------------------------------------------------
# long-side orientation (the mirror image of the short doctrine)
# --------------------------------------------------------------------------
def test_long_hazard_is_the_sell_stop_belt_below_the_entry():
    """Regression: a LONG's sweep hazard is the SELL-stop cluster below, not the buy
    stops above. The first version of the engine crashed here (undefined `squeeze`)."""
    asset = _asset(regime="BULLISH", sell_stops=[_bin(88.0, 89.0, 5_000_000)],
                   buy_stops=[_bin(95.0, 96.0, 3_000_000)])
    ev = at.evaluate_card(_card(side="LONG", entry=90.0, sl=88.5, tp=95.9), _snap(asset), {})
    assert "SL_INSIDE_SWEEP" in _codes(ev)
    f = next(f for f in ev.findings if f.code == "SL_INSIDE_SWEEP")
    assert f.purchase_side is False
    assert f.values["union"] == [88.0, 89.0]
    assert ev.fatal()


def test_long_stop_clearing_the_lower_belt_is_accepted():
    asset = _asset(regime="BULLISH", sell_stops=[_bin(88.0, 89.0, 5_000_000)],
                   buy_stops=[_bin(95.0, 96.0, 3_000_000)])
    ev = at.evaluate_card(_card(side="LONG", entry=90.0, sl=84.0, tp=95.93, lots=2.0),
                          _snap(asset), {})
    assert "SL_INSIDE_SWEEP" not in _codes(ev)
    assert ev.metrics["sl_clearance_atr"] == pytest.approx(0.4)


def test_long_reward_magnets_are_the_buy_stops_above():
    asset = _asset(regime="BULLISH", sell_stops=[_bin(88.0, 89.0, 5_000_000)],
                   buy_stops=[_bin(95.0, 96.0, 3_000_000)])
    ev = at.evaluate_card(_card(side="LONG", entry=90.0, sl=84.0, tp=94.93, lots=2.0),
                          _snap(asset), {})
    assert ev.metrics["tp_governing_magnet"][0:2] == [95.0, 96.0]
    assert ev.metrics["tp_front_run_bps"] == pytest.approx(7.4, abs=0.6)
    assert "TP_INSIDE_MAGNET" not in _codes(ev)


def test_long_against_a_bearish_regime_is_fatal():
    asset = _asset(regime="BEARISH", sell_stops=[_bin(88.0, 89.0, 5_000_000)])
    ev = at.evaluate_card(_card(side="LONG", entry=90.0, sl=84.0, tp=95.9, lots=2.0),
                          _snap(asset), {})
    assert "COUNTER_TREND" in _codes(ev)


def test_long_against_negative_cvd_is_flagged():
    asset = _asset(regime="BULLISH", sell_stops=[_bin(88.0, 89.0, 5_000_000)],
                   session_cvd=-5_000_000.0)
    ev = at.evaluate_card(_card(side="LONG", entry=90.0, sl=84.0, tp=95.9, lots=2.0),
                          _snap(asset), {})
    assert "COUNTER_CVD" in _codes(ev)


# --------------------------------------------------------------------------
# friction, proximity, geometry
# --------------------------------------------------------------------------
def test_fifteen_percent_friction_ceiling_is_fatal():
    # spread 0.40 on a 2.00 stop = 20% of risk
    asset = _asset(spread_price=0.40, ask=100.2)
    ev = at.evaluate_card(_card(entry=102.0, sl=104.0, tp=96.0), _snap(asset), {})
    assert "FRICTION_BUDGET" in _codes(ev)
    assert ev.metrics["friction_pct"] == pytest.approx(20.0)
    assert ev.fatal()


def test_entry_further_than_two_atr_from_mid_is_fatal():
    asset = _asset(mid=100.0, atr=10.0)
    ev = at.evaluate_card(_card(entry=121.0, sl=124.0, tp=112.0), _snap(asset), {})
    assert "ENTRY_TOO_FAR" in _codes(ev)
    assert ev.metrics["entry_distance_atr"] == pytest.approx(2.1)


def test_tp_inside_a_magnet_pool_is_fatal_and_reports_the_pool():
    asset = _asset(sell_stops=[_bin(96.0, 97.0, 3_000_000)])
    ev = at.evaluate_card(_card(entry=110.0, sl=113.5, tp=96.5), _snap(asset), {})
    assert "TP_INSIDE_MAGNET" in _codes(ev)
    f = next(f for f in ev.findings if f.code == "TP_INSIDE_MAGNET")
    assert f.values["magnet"] == [96.0, 97.0]


def test_tp_seven_bps_outside_the_magnet_edge_is_a_clean_front_run():
    asset = _asset(sell_stops=[_bin(90.0, 91.0, 3_000_000)])  # front-run above 91.0
    ev = at.evaluate_card(_card(entry=110.0, sl=113.5, tp=91.0 * 1.00075), _snap(asset), {})
    assert "TP_INSIDE_MAGNET" not in _codes(ev)
    assert ev.metrics["tp_front_run_bps"] == pytest.approx(7.5, abs=0.05)


def test_magnet_ladders_are_merged_before_the_tp_front_run():
    """Regression (Cycle 110): contiguous magnet bins are one ladder. Front-running an
    INTERIOR bin parks the TP inside the neighbouring bin of the same ladder — a TP the
    engine's own TP_INSIDE_MAGNET gate rejects — and used to inflate asset ceilings."""
    ladder = [_bin(96.0, 97.0, 3_000_000), _bin(97.0, 98.0, 3_000_000), _bin(98.0, 99.0, 3_000_000)]
    asset = _asset(sell_stops=ladder)
    ev = at.evaluate_card(_card(entry=105.0, sl=112.0, tp=99.099), _snap(asset), {})
    # the front-run is taken from the ladder's near edge (99.0), never an interior bin
    assert ev.metrics["best_reachable_tp"] == pytest.approx(99.0 * 1.0010, abs=1e-6)
    assert "TP_INSIDE_MAGNET" not in _codes(ev)
    assert ev.metrics["tp_front_run_bps"] == pytest.approx(10.0, abs=0.05)

    # when mid sits INSIDE the ladder there is no front-runnable exit at all
    inside = _asset(mid=98.5, sell_stops=ladder)
    ev2 = at.evaluate_card(_card(entry=103.0, sl=110.0, tp=101.0), _snap(inside), {})
    assert "PRICE_INSIDE_MAGNET_LADDER" in _codes(ev2)
    assert "NO_REACHABLE_MAGNET" in _codes(ev2)


def test_unpayable_geometry_is_fatal():
    asset = _asset(sell_stops=[_bin(96.0, 97.0, 3_000_000)])
    # wide stop (9.5) against a 3 point reachable reward
    ev = at.evaluate_card(_card(entry=100.0, sl=109.5, tp=97.0), _snap(asset), {})
    assert "UNPAYABLE_GEOMETRY" in _codes(ev)


def test_bunker_wall_must_meet_the_asset_class_threshold():
    # crypto major needs >= 5.0M USD of verified wall inside the stop
    walls = [{"side": "SELL", "price": 113.0, "notional_usd": 2_000_000.0, "persist_s": 300.0,
              "address": "0xabc", "wall_class": "MM"}]
    asset = _asset(walls=walls, buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev = at.evaluate_card(_card(sl=114.5), _snap(asset), {})
    assert "BUNKER_WALL_THIN" in _codes(ev)


def test_wall_beyond_the_stop_is_not_shelter():
    """Gate R-2: only walls in the entry..SL corridor count. A verified wall above the stop
    cannot absorb momentum before the stop is touched."""
    walls_above_stop = [{"side": "SELL", "price": 120.0, "notional_usd": 9_000_000.0,
                         "persist_s": 900.0, "address": "0xfar", "wall_class": "MM"}]
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)], walls=walls_above_stop)
    ev = at.evaluate_card(_card(sl=114.5), _snap(asset), {})
    assert "NO_BUNKER_WALL" in _codes(ev)
    # the same wall moved into the corridor shelters the trade
    walls_in_corridor = [dict(walls_above_stop[0], price=113.5)]
    asset2 = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)], walls=walls_in_corridor)
    ev2 = at.evaluate_card(_card(sl=114.5), _snap(asset2), {})
    assert "NO_BUNKER_WALL" not in _codes(ev2)


def test_persistence_needs_180s_or_ledger_continuity():
    walls = [{"side": "SELL", "price": 113.0, "notional_usd": 9_000_000.0, "persist_s": 0.0,
              "address": "0xabc", "wall_class": "MM"}]
    asset = _asset(walls=walls, buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev = at.evaluate_card(_card(sl=114.5), _snap(asset), {})
    assert "PERSISTENCE_UNVERIFIED" in _codes(ev)
    # the same wallet seen in an earlier generation rescues it
    continuity = {("SYNTH", "0xabc"): {"age_s": 3600.0, "max_persist_s": 900.0,
                                       "prices": {112.0}}}
    ev2 = at.evaluate_card(_card(sl=114.5), _snap(asset), continuity)
    assert "PERSISTENCE_UNVERIFIED" not in _codes(ev2)


def test_range_bound_regime_gates_discretionary_cards():
    """Operator rule: when trend_regime is RANGE_BOUND neither engine applies — a
    discretionary card in noise is a forced trade (fatal), while a posture card may record
    the state without being struck down."""
    asset = _asset(regime="RANGE_BOUND")
    ev = at.evaluate_card(_card(), _snap(asset), {})
    assert "REGIME_GATED_STAND_ASIDE" in _codes(ev)
    assert ev.fatal()
    watch = at.Card(id="w1", action="WATCH", asset="SYNTH",
                    meta={"condition": "armed test trigger", "invalidation": "n/a"})
    ev2 = at.evaluate_card(watch, _snap(asset), {})
    assert "REGIME_GATED_STAND_ASIDE" in _codes(ev2)
    assert not ev2.fatal()


def test_jpy_quote_currency_converts_risk_to_usd():
    """A USDJPY point is JPY, not USD: risk/stress must be converted at the live rate or the
    engine overstates a JPY ticket's risk by ~158x and fabricates FLOOR_BREACH verdicts."""
    asset = _asset(symbol="USDJPY.pi", mid=150.0, atr=0.1, spread_price=0.003, spread_bps=0.2,
                   contract=100000.0, min_lot=0.01)
    ev = at.evaluate_card(_card(entry=150.5, sl=151.5, tp=149.0, lots=0.01), _snap(asset), {})
    assert ev.metrics["usd_factor"] == pytest.approx(1.0 / 150.0)
    assert ev.metrics["risk_usd"] == pytest.approx(1000.0 / 150.0, rel=1e-6)
    assert ev.metrics["reward_usd"] == pytest.approx(1500.0 / 150.0, rel=1e-6)
    # R-multiples are currency-invariant
    assert ev.metrics["rr_gross"] == pytest.approx(1.5, rel=1e-6)
    # a USD-quoted book keeps factor 1.0
    ev2 = at.evaluate_card(_card(), _snap(_asset()), {})
    assert ev2.metrics.get("usd_factor") in (None, 1.0)


def test_unverified_regime_blocks_any_trade_card():
    asset = _asset(regime="INSUFFICIENT_HISTORY")
    ev = at.evaluate_card(_card(), _snap(asset), {})
    assert "REGIME_UNVERIFIED" in _codes(ev)
    assert ev.fatal()


def test_counter_trend_short_in_a_bullish_regime_is_fatal():
    asset = _asset(regime="BULLISH")
    ev = at.evaluate_card(_card(), _snap(asset), {})
    assert "COUNTER_TREND" in _codes(ev)


# --------------------------------------------------------------------------
# governance arithmetic
# --------------------------------------------------------------------------
def test_stress_and_floor_math_uses_125x_plus_two_per_ticket():
    asset = _asset(sell_stops=[_bin(96.0, 97.0, 3_000_000)])
    card = _card(entry=110.0, sl=115.0, tp=97.0, lots=1.0, batch_count=1)
    ev = at.evaluate_card(card, _snap(asset, balance=4859.55, stress=13.875, available=3), {})
    assert ev.metrics["card_stress_usd"] == pytest.approx(1.25 * 5.0 + 2.0)
    assert ev.metrics["post_stop_equity_usd"] == pytest.approx(4859.55 - 13.875 - 8.25)


def test_three_new_max_risk_tickets_breach_the_operating_buffer():
    asset = _asset(sell_stops=[_bin(96.0, 97.0, 3_000_000)])
    card = _card(entry=110.0, sl=115.0, tp=97.0, lots=2.5, batch_count=3)
    ev = at.evaluate_card(card, _snap(asset), {})
    assert "FLOOR_BREACH" in _codes(ev)
    assert ev.metrics["post_stop_equity_usd"] < at.OPERATING_BUFFER_USD
    # the floor is the buffer, not the hard floor
    assert ev.metrics["post_stop_equity_usd"] > at.HARD_FLOOR_USD


def test_capacity_beyond_the_available_joint_fill_slots_is_fatal():
    asset = _asset(sell_stops=[_bin(96.0, 97.0, 3_000_000)])
    ev = at.evaluate_card(_card(entry=110.0, sl=115.0, tp=97.0, batch_count=4), _snap(asset), {})
    assert "CAPACITY_EXCEEDED" in _codes(ev)


# --------------------------------------------------------------------------
# recommendation semantics
# --------------------------------------------------------------------------
def test_hold_is_contradicted_by_a_fatally_misspecified_order():
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    card = at.Card(id="hold", action="HOLD", asset="SYNTH", target_ticket=1,
                   meta={"evaluates": {"asset": "SYNTH", "side": "SHORT", "entry": 110.0,
                                       "sl": 113.5, "tp": 101.0, "lots": 1.0}})
    ev = at.evaluate_card(card, _snap(asset), {})
    assert "HOLD_CONTRADICTED" in _codes(ev)
    assert "SL_INSIDE_SWEEP" in ev.metrics["probe_fatal_codes"]


def test_delete_is_justified_by_a_fatally_misspecified_order():
    asset = _asset(buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    card = at.Card(id="del", action="DELETE", asset="SYNTH", target_ticket=1,
                   meta={"evaluates": {"asset": "SYNTH", "side": "SHORT", "entry": 110.0,
                                       "sl": 113.5, "tp": 101.0, "lots": 1.0}})
    ev = at.evaluate_card(card, _snap(asset), {})
    assert "DELETE_UNJUSTIFIED" not in _codes(ev)
    assert not ev.fatal()
    assert "SL_INSIDE_SWEEP" in ev.metrics["delete_justification"]


def test_delete_of_a_clean_order_is_rejected():
    asset = _asset(sell_stops=[_bin(101.0, 102.0, 3_000_000)])
    card = at.Card(id="del", action="DELETE", asset="SYNTH",
                   meta={"evaluates": {"asset": "SYNTH", "side": "SHORT", "entry": 110.0,
                                       "sl": 113.0, "tp": 101.5, "lots": 1.0}})
    ev = at.evaluate_card(card, _snap(asset), {})
    if not ev.metrics["probe_fatal"] and ev.metrics["probe_majors"] == 0:
        assert "DELETE_UNJUSTIFIED" in _codes(ev)


def test_stand_aside_is_contradicted_when_a_candidate_clears_every_gate():
    clean_asset = _asset(sell_stops=[_bin(101.0, 102.0, 3_000_000)])
    snap = _snap(clean_asset)
    candidate = {"id": "clean", "action": "STAGE", "asset": "SYNTH", "side": "SHORT",
                 "entry": 110.0, "sl": 113.0, "tp": 101.5, "lots": 0.5}
    card = at.Card(id="sa", action="STAND_ASIDE", meta={"universe": [candidate]})
    ev = at.evaluate_card(card, snap, {})
    if not ev.metrics["qualified_candidates"]:
        assert "STAND_ASIDE_JUSTIFIED" in _codes(ev)
    else:
        assert "STAND_ASIDE_CONTRADICTED" in _codes(ev)


def test_watch_card_without_a_trigger_is_not_a_verified_trade():
    card = at.Card(id="w", action="WATCH", thesis="wait")
    ev = at.evaluate_card(card, _snap(_asset()), {})
    assert ev.qualified is False
    assert "NOT_EVALUATED" in _codes(ev)


def test_watch_card_documents_its_armed_trigger():
    card = at.Card(id="w", action="WATCH",
                   meta={"condition": "15m high >= 113.0 then close < 112.5"})
    ev = at.evaluate_card(card, _snap(_asset()), {})
    assert "CONDITIONAL_UNTRIGGERED" in _codes(ev)
    assert ev.metrics["armed_trigger"].startswith("15m high")


# --------------------------------------------------------------------------
# bracket + determinism
# --------------------------------------------------------------------------
def _entries_for_bracket():
    asset = _asset()
    snap = _snap(asset)
    cards = [
        at.Card(id="bad_stage", action="STAGE", asset="SYNTH", side="SHORT",
                entry=110.0, sl=113.5, tp=101.0, lots=1.0),
        at.Card(id="watch", action="WATCH", meta={"condition": "x"}),
        at.Card(id="watch_dup", action="WATCH", meta={"condition": "x"}),
    ]
    return at.evaluate_all(cards, snap, {})


def test_fatal_rule_beats_a_higher_rubric_total():
    entries = {e["id"]: e for e in _entries_for_bracket()}
    bad, watch = entries["bad_stage"], entries["watch"]
    res = at.head_to_head(bad, watch)
    if bad["fatal"] and not watch["fatal"]:
        assert res["winner"] == "watch"
    else:
        assert res["winner"] in (bad["id"], watch["id"])


def test_bracket_eliminates_down_to_one_winner():
    entries = _entries_for_bracket()
    bracket = at.run_bracket(entries, seed=7)
    assert bracket["winner"] in {e["id"] for e in entries}
    assert len(bracket["rounds"]) >= 1
    assert bracket["rounds"][-1]["survivors"] == [bracket["winner"]]


def test_tournament_is_deterministic_for_the_same_inputs(tmp_path):
    snap_path = tmp_path / "snap.json"
    cards_path = tmp_path / "cards.json"
    asset = _asset(sell_stops=[_bin(101.0, 102.0, 3_000_000)])
    snap_path.write_text(json.dumps(_snap(asset)), encoding="utf-8")
    cards_path.write_text(json.dumps({"cards": [
        {"id": "a", "action": "STAGE", "asset": "SYNTH", "side": "SHORT",
         "entry": 110.0, "sl": 113.5, "tp": 101.0, "lots": 1.0},
        {"id": "b", "action": "WATCH", "meta": {"condition": "y"}},
        {"id": "c", "action": "STAND_ASIDE", "meta": {"universe": []}},
    ]}), encoding="utf-8")
    out = tmp_path / "runs"
    r1 = at.run_tournament(str(snap_path), str(cards_path), str(out), seed=106, evidence_paths=[])
    r2 = at.run_tournament(str(snap_path), str(cards_path), str(out), seed=106, evidence_paths=[])
    assert r1["bracket"] == r2["bracket"]
    assert [e["total"] for e in r1["entries"]] == [e["total"] for e in r2["entries"]]
    assert r1["cards_sha256"] == r2["cards_sha256"]


def test_min_compliant_stop_walks_past_a_second_belt():
    """Regression (live XAGUSD.pi geometry): clearing the first cluster by 0.35 ATR can
    park the minimum compliant stop inside a second cluster just beyond it. The asset-level
    anchor must walk outward until the derived stop sits in free space."""
    magnet = _bin(98.0, 99.0, 3_000_000)
    stacked = _asset(atr=1.0, sell_stops=[magnet],
                     buy_stops=[_bin(113.0, 114.0, 5_000_000), _bin(114.3, 115.6, 5_000_000)])
    ev = at.evaluate_card(_card(entry=110.0, sl=116.0, tp=99.07), _snap(stacked), {})
    assert ev.metrics["min_compliant_stop_anchor"] == pytest.approx(115.6)
    assert ev.metrics["min_compliant_stop_points"] == pytest.approx(5.6 + 0.35)

    # a near-miss cluster whose near edge sits inside the buffer band is part of the same
    # sweep complex and must still be cleared
    nearmiss = _asset(atr=1.0, sell_stops=[magnet],
                      buy_stops=[_bin(113.0, 114.0, 5_000_000), _bin(114.5, 115.6, 5_000_000)])
    ev3 = at.evaluate_card(_card(entry=110.0, sl=116.0, tp=99.07), _snap(nearmiss), {})
    assert ev3.metrics["min_compliant_stop_anchor"] == pytest.approx(115.6)
    assert ev3.metrics["min_compliant_stop_points"] == pytest.approx(5.6 + 0.35)

    # the same geometry without the second belt anchors on the first belt's edge
    single = _asset(atr=1.0, sell_stops=[magnet], buy_stops=[_bin(113.0, 114.0, 5_000_000)])
    ev2 = at.evaluate_card(_card(entry=110.0, sl=116.0, tp=99.07), _snap(single), {})
    assert ev2.metrics["min_compliant_stop_anchor"] == pytest.approx(114.0)
    assert ev2.metrics["min_compliant_stop_points"] == pytest.approx(4.0 + 0.35)

    # a cluster far beyond the buffer does NOT extend the anchor
    faraway = _asset(atr=1.0, sell_stops=[magnet],
                     buy_stops=[_bin(113.0, 114.0, 5_000_000), _bin(117.0, 118.0, 5_000_000)])
    ev4 = at.evaluate_card(_card(entry=110.0, sl=116.0, tp=99.07), _snap(faraway), {})
    assert ev4.metrics["min_compliant_stop_anchor"] == pytest.approx(114.0)


def test_eth_and_sol_carry_the_mandated_higher_rr_floors():
    """Playbook 7.4: ETHUSD.pi (Grade B friction) requires >= 2.2R and SOLUSD.p
    (Grade B-) requires >= 2.5R; every other asset keeps the flat 2.0R floor."""
    assert at.RR_MIN_BY_ASSET == {"ETHUSD.pi": 2.20, "SOLUSD.p": 2.50}
    ev_eth = at.evaluate_card(_card(), _snap(_asset(symbol="ETHUSD.pi")), {})
    assert ev_eth.metrics["rr_min_required"] == pytest.approx(2.20)
    ev_sol = at.evaluate_card(_card(), _snap(_asset(symbol="SOLUSD.p")), {})
    assert ev_sol.metrics["rr_min_required"] == pytest.approx(2.50)
    ev_btc = at.evaluate_card(_card(), _snap(_asset(symbol="BTCUSD.pi")), {})
    assert ev_btc.metrics["rr_min_required"] == pytest.approx(2.00)


# --------------------------------------------------------------------------
# live snapshot (documented council expectations)
# --------------------------------------------------------------------------
@pytest.mark.skipif(not os.path.exists(SNAPSHOT_PATH), reason="no local telemetry snapshot")
def test_cycle106_tournament_reproduces_the_reported_rulings():
    cards = json.load(open(CARDS_PATH, encoding="utf-8"))["cards"]
    run = at.run_tournament(SNAPSHOT_PATH, CARDS_PATH, "/tmp/arena_test_runs",
                            seed=106, evidence_paths=[], run_id="pytest_cycle106")
    entries = {e["id"]: e for e in run["entries"]}

    # the live ETH ticket is fatally mis-specified, so HOLD/MODIFY are contradicted
    assert entries["eth_hold_18925596"]["fatal"] is True
    assert "HOLD_CONTRADICTED" in {f["code"] for f in entries["eth_hold_18925596"]["findings"]}
    assert "ENTRY_TOO_FAR" in entries["eth_hold_18925596"]["metrics"]["probe_fatal_codes"]
    assert "FRICTION_BUDGET" in entries["eth_hold_18925596"]["metrics"]["probe_fatal_codes"]
    assert "SL_INSIDE_SWEEP" in entries["eth_hold_18925596"]["metrics"]["probe_fatal_codes"]

    # the Argon BTC card carries the purchase-side hazard the desk flagged
    argon = entries["btc_stage_82190_argon"]
    assert argon["fatal"] is True
    assert "SL_INSIDE_SWEEP" in argon["metrics"].get("purchase_side_flagged", [])

    # three max-size tickets in the open capacity breach the operating buffer
    assert "FLOOR_BREACH" in {f["code"] for f in entries["desk_batch_3x_max_risk"]["findings"]}

    # the DELETE recommendation survives, justified by the probe's fatal codes
    delete = entries["eth_delete_18925596"]
    assert delete["fatal"] is False and delete["verified"] is True
    assert {"ENTRY_TOO_FAR", "FRICTION_BUDGET", "SL_INSIDE_SWEEP"} <= set(delete["metrics"]["delete_justification"])

    # the asset-level ceiling: no card on the three instrumented assets can pay 2.0R
    # against the minimum compliant stop in this generation. Cycle 110 revised BTC down
    # from the 1.88R first reported: that figure front-ran an INTERIOR bin of a contiguous
    # magnet ladder, parking the TP inside the next bin (a TP_INSIDE_MAGNET the engine's own
    # gate rejects). Ladder-merged, the honest ceiling is ~0.73R.
    assert entries["btc_stage_82190_argon"]["metrics"]["max_achievable_rr"] == pytest.approx(0.729, abs=0.02)
    assert entries["eth_hold_18925596"]["metrics"]["max_achievable_rr"] < 0.60
    assert entries["sp500_stage_short_7738"]["metrics"]["max_achievable_rr"] < 0.70

    # no ticket survives, and portfolio-level stand-aside wins the bracket
    assert all(e["fatal"] for e in run["entries"] if e["action"] in ("STAGE", "STAGE_BATCH"))
    assert run["bracket"]["winner"] == "desk_stand_aside_cycle106"
    assert entries["desk_stand_aside_cycle106"]["metrics"]["qualified_candidates"] == []
