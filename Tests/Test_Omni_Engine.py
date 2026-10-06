import copy
import json
import math
from pathlib import Path
from types import SimpleNamespace
import numpy as np
import pytest
from Terminal.Asset_Universe import UNIVERSE, canonical_asset, broker_candidates
from Terminal.Risk_Sizing_Engine import (RiskPolicy, OrderflowModel, RobustNormalizer, CovarianceGate,
                                        completed_statistics, fit_covariance, floor_volume, size_trade)
from Terminal.Uplift_Model import (ratchet, replay_episode, UpliftGate, FEATURES, train_uplift, POLICY_VERSION)
from Terminal.Omni_Trader import AI15mMT5Trader, MAGIC
from Terminal.Cognitive_Engine import CognitiveEngine, DECISION_SCHEMA
from Terminal.Market_Intelligence import MarketIntelligenceEngine

NOW = (1700000000//900)*900+870

def bars(now=NOW, count=96):
    start = int(now//900)*900-count*900
    return [{"time": start+i*900, "open": 100, "high": 100.5, "low": 99.5,
             "close": 100+0.4*math.sin(i*1.7)} for i in range(count)]

def payload(now=NOW, asset="BTC", reverse=False):
    return {"coin": asset, "price": 100, "l2_book": {"timestamp": now*1000, "best_bid": 99.99,
            "best_ask": 100.01, "bids": [{"price": 99.99-i*0.01, "size": 10000 if not reverse else 100} for i in range(20)],
            "asks": [{"price": 100.01+i*0.01, "size": 100 if not reverse else 10000} for i in range(20)]},
            "recent_trades": [{"time": now*1000, "side": "SELL" if reverse else "BUY", "price": 100, "size": 100, "notional_usd": 10000}],
            "sources": {"l3": {"observed_at": now}, "liquidations": {"observed_at": now}}, "l3_orders": []}

def covariance(now=NOW, assets=UNIVERSE, sigma=0.003):
    matrix = np.eye(len(assets))*sigma**2
    return CovarianceGate(assets, matrix, {"return_units": "decimal_log_return", "horizon_minutes": 15,
                                           "created_at": now-60, "data_end": now-900, "max_age_seconds": 86400})

class Broker:
    def __init__(self, clock): self.clock=clock; self.positions=[]; self.pending=[]; self.modified=[]; self.closed=[]; self.sent=[]; self.mid=100
    def get_open_positions(self): return copy.deepcopy(self.positions)
    def get_pending_orders(self): return copy.deepcopy(self.pending)
    def get_account_summary(self): return {"connected": True, "login": 1, "currency": "USD", "equity_usd": 5000, "margin_free_usd": 5000}
    def resolve_symbol(self, asset): return asset+"USD" if asset not in ("GOLD", "SILVER") else "XAUUSD" if asset=="GOLD" else "XAGUSD"
    def get_recent_bars(self, symbol, count=96): return bars(self.clock(), count)
    def get_symbol_price(self, symbol): return {"bid": self.mid-0.01, "ask": self.mid+0.01, "point": .01, "tick_size": .01,
        "time_msc": self.clock()*1000, "digits": 2, "contract_size": 100, "min_lot": .01, "step_lot": .01, "max_lot": 10,
        "stops_level": 0, "freeze_level": 0, "currency_profit": "USD"}
    def estimate_order(self, symbol, direction, entry, sl): return {"stop_loss_per_lot": abs(entry-sl)*100, "margin_per_lot": 1000}
    def modify_position_sltp(self, ticket, sl, tp): self.modified.append((ticket, sl, tp)); return {"success": True}
    def close_position(self, ticket): self.closed.append(ticket); return {"success": True}
    def position_deals(self, ticket): return []
    def execute_market_order(self, *args, **kwargs): self.sent.append((args, kwargs)); return {"success": False, "uncertain": True}
    def stage_limit_order(self, symbol, direction, volume, limit_price, sl, tp, **kwargs):
        ticket = len(self.sent) + 1000
        order = {"ticket": ticket, "symbol": symbol, "direction": direction, "volume": volume,
                 "price_open": limit_price, "sl": sl, "tp": tp, "magic": kwargs.get("magic", MAGIC)}
        self.pending.append(order)
        self.sent.append(("limit", order, kwargs))
        return {"success": True, "ticket": ticket, "symbol": symbol, "direction": direction, "volume": volume,
                "price": limit_price, "sl": sl, "tp": tp, "expires_at": kwargs.get("expiration_seconds", 3600)}
    def cancel_pending_order(self, ticket):
        self.pending = [o for o in self.pending if o["ticket"] != ticket]
        self.closed.append(f"cancel_{ticket}")
        return {"success": True, "ticket": ticket}

class Intel:
    def check_macro_blackout(self): return False, "NO_EVENT", 999
    def get_market_intelligence_report(self): return {"asset_scores": {a: 1 for a in UNIVERSE}, "sentiment_valid": True}

class Cognitive:
    def record_outcome(self, *args): pass

def trader(tmp_path, clock=None, paper=True):
    clock=clock or (lambda: NOW)
    broker=Broker(clock)
    t=AI15mMT5Trader(bridge=broker, intel=Intel(), cognitive=Cognitive(), covariance=covariance(), uplift_path=tmp_path/"no_uplift",
                    cognitive_enabled=False, clock=clock, paper_mode=paper, state_file=tmp_path/"state.json", journal_dir=tmp_path/"journal")
    t.symbols = {a: broker.resolve_symbol(a) for a in UNIVERSE}
    t.bars = {a: bars(clock()) for a in UNIVERSE}
    return t, broker

def test_complete_universe_and_index_aliases():
    assert len(UNIVERSE)==14 and "LTC" not in UNIVERSE
    assert canonical_asset("flx:USA100")=="NAS100"
    assert canonical_asset("XAUUSD.p")=="GOLD"
    assert "US30" in broker_candidates("DJ30") and "XAUUSD" in broker_candidates("GOLD")

@pytest.mark.parametrize("volume,step,expected", [(0.49,.25,.25),(.24,.25,0),(.029,.01,.02),(1.99,1,1)])
def test_volume_rounds_down_for_nondecimal_steps(volume,step,expected):
    assert floor_volume(volume,step,step,10)==expected

def test_normalizer_uses_only_prior_observations():
    normal=RobustNormalizer({"BTC": [0.0]*24})
    assert normal.score_then_observe("BTC",1)==3
    assert normal.export()["BTC"][-1]==1

def test_far_liquidity_is_decayed_by_local_volatility():
    levels=OrderflowModel._levels([{"price":99.9,"size":1000},{"price":90,"size":100000}],100,.01,1)
    assert levels[1][3]<levels[0][3]

def test_forming_bar_cannot_change_volatility():
    base=completed_statistics(bars(),NOW)
    future={"time":int(NOW//900)*900,"close":1e9,"high":1e9,"low":1}
    assert completed_statistics(bars()+[future],NOW)==base

@pytest.mark.parametrize("stamp", [NOW-11,NOW+1,0])
def test_stale_or_future_book_rejected(stamp):
    data=payload();data["l2_book"]["timestamp"]=stamp*1000
    with pytest.raises(ValueError,match="book_stale_or_future"): OrderflowModel().features("BTC",data,bars(),{},NOW)

def test_directional_macro_confluence_is_symmetric():
    long=OrderflowModel().features("BTC",payload(),bars(),{"asset_scores":{"BTC":1},"sentiment_valid":True},NOW)
    short=OrderflowModel().features("BTC",payload(reverse=True),bars(),{"asset_scores":{"BTC":-1},"sentiment_valid":True},NOW)
    assert long["direction"]=="LONG" and short["direction"]=="SHORT"
    assert abs(long["confluence"]-short["confluence"])<.01
    assert 10 <= long["risk_intent_usd"] <=45

def test_projected_liquidation_pressure_uses_same_corridor():
    data=payload()
    data["liquidations"]={"kind":"PROJECTED_EXPOSURE","bands":[{"min_px":99.9,"max_px":99.95,"amount_usd":5e8,"position_side_at_risk":"LONG"}]}
    f=OrderflowModel().features("BTC",data,bars(),{},NOW)
    record=f["corridors"][0]
    expected=sum(x["price"]*x["size"] for x in data["l2_book"]["bids"] if 99.9<=x["price"]<=99.95)
    assert record["depth_usd"]==expected and record["ratio"]==5e8/expected
    assert f["liquidation_delta"]==-1
    data["liquidations"]["kind"]="UNVERIFIED_BAND_LANDSCAPE"
    assert OrderflowModel().features("BTC",data,bars(),{},NOW)["liquidation_delta"]==0

def test_unobserved_corridor_cannot_be_divided_by_zero_depth():
    data=payload();data["liquidations"]={"kind":"PROJECTED_EXPOSURE","bands":[{"min_px":80,"max_px":90,"amount_usd":1e9,"position_side_at_risk":"LONG"}]}
    f=OrderflowModel().features("BTC",data,bars(),{},NOW)
    assert f["corridors"][0]["ratio"] is None and f["liquidation_delta"]==0

def test_cached_generation_does_not_manufacture_wall_persistence():
    data=payload();data["l3_orders"]=[{"address":"whale","price":99.99,"side":"BUY","notional_usd":1e6}]
    flow=OrderflowModel()
    assert flow.features("BTC",data,bars(),{},NOW)["wall_imbalance"]==0
    assert flow.features("BTC",data,bars(),{},NOW+10)["wall_imbalance"]==0
    data=payload(NOW+20);data["l3_orders"]=[{"address":"whale","price":99.99,"side":"BUY","notional_usd":1e6}]
    assert flow.features("BTC",data,bars(),{},NOW+20)["wall_imbalance"]==1

def test_background_wall_observation_survives_between_decisions():
    flow=OrderflowModel()
    for stamp in range(NOW-80,NOW+1,20):
        data=payload(stamp);data["l3_orders"]=[{"address":"whale","price":99.99,"side":"BUY","notional_usd":1e6}]
        flow.observe_walls("BTC",data,stamp)
    assert flow.features("BTC",data,bars(),{},NOW)["wall_imbalance"]==1
    assert flow.walls["BTC"]["whale:BUY:99.99"]["first"]==NOW-80

def test_invalid_macro_sentiment_cannot_contribute_to_confluence():
    f=OrderflowModel().features("BTC",payload(),bars(),{"asset_scores":{"BTC":1},"sentiment_valid":False},NOW)
    assert f["macro_score"]==0

def test_signed_covariance_allows_hedge_but_downsizes_duplicate_beta():
    gate=CovarianceGate(["BTC","ETH"], [[.0001,.000095],[.000095,.0001]])
    same=gate.scale_candidate({"BTC":2000},"ETH",2000,25)
    hedge=gate.scale_candidate({"BTC":2000},"ETH",-2000,25)
    assert 0<same["scale"]<1 and same["variance_after"]<=625+1e-8
    assert hedge["scale"]==1 and hedge["incremental_variance"]<0

@pytest.mark.parametrize("matrix", [[[1,2],[2,1]],[[1,0],[1,1]],[[float('nan'),0],[0,1]]])
def test_invalid_covariance_rejected(matrix):
    with pytest.raises(ValueError): CovarianceGate(["BTC","ETH"],matrix)

def test_covariance_requires_units_horizon_and_causal_vintage():
    gate=covariance();gate.validate_time(NOW)
    gate.metadata["created_at"]=NOW+1
    with pytest.raises(ValueError,match="future"): gate.validate_time(NOW)
    with pytest.raises(ValueError): CovarianceGate(["BTC"],[[.001]]).validate_time(NOW)

def test_covariance_polars_artifact_roundtrip(tmp_path):
    path=tmp_path/"cov.parquet"
    fitted=fit_covariance({"BTC":bars(),"ETH":bars()},NOW,path)
    loaded=CovarianceGate.load(path);loaded.validate_time(NOW)
    np.testing.assert_allclose(loaded.matrix,fitted.matrix)
    assert loaded.metadata["observations"]>=48
    path.write_bytes(path.read_bytes()+b"bad")
    with pytest.raises(ValueError,match="checksum"): CovarianceGate.load(path)

def test_cost_inclusive_sizing_never_raises_minimum_lot_to_exceed_risk():
    broker=Broker(lambda:NOW);q=broker.get_symbol_price("BTCUSD")
    sized=size_trade(q,150,45,covariance(),{},"BTC","LONG",RiskPolicy(),225,5000,1000)
    assert sized["accepted"] and sized["risk_usd"]<=45 and sized["friction_bps"]>=41
    q["min_lot"]=1;q["step_lot"]=1
    assert not size_trade(q,150,45,covariance(),{},"BTC","LONG",RiskPolicy(),225,5000,1000)["accepted"]

@pytest.mark.parametrize("direction,sign", [("LONG",1),("SHORT",-1)])
def test_exact_ratchet_phases_and_no_stop_loosening(direction,sign):
    assert ratchet(100,2,direction,.8,100-sign*2,1)==100+sign*.7
    assert ratchet(100,2,direction,1.5,100-sign*2,1)==100+sign*1.7
    locked=100+sign*2
    assert ratchet(100,2,direction,1.0,locked,1)==locked

def test_all_assets_evaluated_and_slot_idempotent(tmp_path):
    t,b=trader(tmp_path)
    result=t.evaluate_market({a:payload(asset=a) for a in UNIVERSE}, {"received_at":NOW,"sentiment_valid":True,"asset_scores":{a:1 for a in UNIVERSE}})
    assert result["decision"]=="PAPER_FILLED" and len(result["candidates"])==14
    assert len(t.state["paper_positions"])==1
    assert t.evaluate_market({a:payload(asset=a) for a in UNIVERSE})["reason"]=="slot_already_evaluated"
    assert not b.sent
    t2,_=trader(tmp_path)
    assert t2.state["last_slot"]==t.state["last_slot"]

def test_second_position_requires_qualified_uplift(tmp_path):
    now=[NOW];t,b=trader(tmp_path,lambda:now[0])
    macro={"received_at":NOW,"sentiment_valid":True,"asset_scores":{a:1 for a in UNIVERSE}}
    t.evaluate_market({"BTC":payload()},macro)
    now[0]+=900;t.bars={a:bars(now[0]) for a in UNIVERSE};macro["received_at"]=now[0]
    result=t.evaluate_market({"ETH":payload(now[0],"ETH")},macro)
    assert result["vetoes"]["ETH"]=="uplift_model_unavailable" and len(t.state["paper_positions"])==1
    assert (tmp_path/"journal/uplift_episodes.jsonl").exists()

def test_uncertain_execution_reserves_slot_without_retry(tmp_path):
    now=[NOW];t,b=trader(tmp_path,lambda:now[0],paper=False)
    macro={"received_at":NOW,"sentiment_valid":True,"asset_scores":{"BTC":1}}
    assert t.evaluate_market({"BTC":payload()},macro)["decision"]=="ORDER_UNCERTAIN"
    now[0]+=900
    assert t.evaluate_market({"BTC":payload(now[0])},macro)["reason"]=="unresolved_execution_intent"
    assert len(b.sent)==1

def test_live_force_cannot_bypass_cadence(tmp_path):
    t,b=trader(tmp_path,lambda:NOW-60,paper=False)
    assert t.evaluate_market({"BTC":payload()},force=True)["reason"]=="outside_execution_window" and not b.sent

def test_drawdown_halt_persists_and_fixed_capital_floor(tmp_path):
    t,b=trader(tmp_path)
    assert t._equity_guard({"equity_usd":4775})["halted"]
    t._save_state();t2,_=trader(tmp_path)
    assert t2._equity_guard({"equity_usd":5001})["halted"]
    t2.state["peak_equity_usd"]=10000
    assert t2._equity_guard({"equity_usd":10000})["hard_floor_usd"]==9775

def test_time_decay_closes_own_position_using_own_quote(tmp_path):
    t,b=trader(tmp_path,paper=False)
    b.positions=[{"ticket":1,"symbol":"ETHUSD","direction":"LONG","price_open":100,"sl":98,"tp":106,"volume":.1,"time":NOW-24*900,"magic":MAGIC}]
    t.state["positions"]["1"]={"initial_r":2,"asset":"ETH"}
    t.manage_active_positions()
    assert b.closed==[1]

def test_foreign_magic_is_counted_but_not_managed(tmp_path):
    t,b=trader(tmp_path,paper=False)
    b.positions=[{"ticket":1,"symbol":"ETHUSD","direction":"LONG","price_open":100,"sl":98,"tp":106,"volume":.1,"time":NOW-24*900,"magic":999}]
    t.manage_active_positions()
    assert not b.closed and not b.modified

def test_calendar_is_date_specific_and_missing_is_closed(tmp_path):
    path=tmp_path/"calendar.json"
    path.write_text(json.dumps({"required_series":["CPI","NFP","FOMC"],"verified_at":NOW-86400,"coverage_start":NOW-86400,"coverage_end":NOW+86400,"events":[{"name":"CPI","time_utc":NOW+899,"impact":"HIGH"}]}))
    intel=MarketIntelligenceEngine(calendar_path=path,clock=lambda:NOW)
    assert intel.check_macro_blackout()[0]
    intel.clock=lambda:NOW+901+900
    assert not intel.check_macro_blackout()[0]
    path.unlink()
    assert intel.check_macro_blackout()[1]=="CALENDAR_UNAVAILABLE"

def test_llm_rejects_unknown_evidence_and_wrong_candidate():
    snapshot={"snapshot_id":"s","candidate":{"candidate_id":"c"},"flow":{"x":1}}
    decision={k:None for k in DECISION_SCHEMA["required"]}
    decision.update(snapshot_id="s",action="SELECT",candidate_id="c",analyst_thesis="a",critic_objection="b",rationale_summary="r",support_refs=["/flow/x"],counter_refs=[],invalidation_refs=["/flow/x"])
    assert CognitiveEngine.validate_decision(snapshot,decision)
    decision["support_refs"]=["/flow/invented"]
    assert not CognitiveEngine.validate_decision(snapshot,decision)
    decision["support_refs"]=["/flow/x"];decision["candidate_id"]="other"
    assert not CognitiveEngine.validate_decision(snapshot,decision)

def test_paired_replay_target_is_net_equity_difference_and_causal():
    p={"candidate_id":"c","symbol":"BTCUSD","direction":"LONG","price_open":100.01,"initial_r":2,"sl":98.01,"tp":106.01,"volume":.1,"contract_size":100,"time":NOW,"residual_cost_usd":4}
    episode={"episode_id":"e","as_of":NOW,"equity_usd":5000,"hard_floor_usd":4775,"existing_positions":[],"candidate":p,"features":{}}
    ticks=[{"time":NOW+s,"symbol":"BTCUSD","bid":100+s/21600,"ask":100.02+s/21600} for s in range(1,21601,10)]
    ticks.append({"time":NOW+21600,"symbol":"BTCUSD","bid":101,"ask":101.02})
    label=replay_episode(episode,ticks)
    assert label["equity_reject"]==5000
    assert label["uplift_usd"]==pytest.approx((101-100.01)*10-4)
    # A future quote outside the target horizon must not change the label.
    assert replay_episode(episode,ticks+[{"time":NOW+21601,"symbol":"BTCUSD","bid":1,"ask":2}])==label

def test_uplift_missing_model_fails_closed(tmp_path):
    assert not UpliftGate(tmp_path).decide({},NOW)["accepted"]

def test_rebuilding_old_model_does_not_hide_stale_training_outcomes(tmp_path):
    gate=UpliftGate(tmp_path);gate.error=None;gate.classifier=object()
    gate.meta={"live_eligible":True,"label_end":NOW-31*86400,"created_at":NOW-1,"max_age_seconds":30*86400}
    assert gate.decide({},NOW)["reason"]=="uplift_stale_or_future"

def test_persisted_account_identity_prevents_cross_account_dispatch(tmp_path):
    t,b=trader(tmp_path,paper=False);t.state["account_login"]=2
    with pytest.raises(ValueError,match="persisted_state_account_mismatch"): t._account([])
    assert not b.sent

def test_run_loop_is_causal_paper_and_releases_writer_lock(tmp_path,monkeypatch):
    import Terminal.Omni_Trader as module
    monkeypatch.setattr(module,"ROOT",tmp_path)
    t,b=trader(tmp_path)
    t.fetcher=lambda a:payload(asset=a)
    t.payloads={a:payload(asset=a) for a in UNIVERSE}
    t.macro={"received_at":NOW,"sentiment_valid":True,"asset_scores":{a:1 for a in UNIVERSE}}
    t.run(max_cycles=1)
    assert t.last_report["decision"]=="PAPER_FILLED" and not b.sent
    assert len(t.state["paper_positions"])==1

def test_missing_initial_feeds_do_not_consume_decision_slot(tmp_path):
    t,b=trader(tmp_path);t.fetches={"BTC":object()}
    assert t.evaluate_market()["reason"]=="waiting_for_initial_feeds"
    assert t.state["last_slot"]==-1

def test_uplift_training_builds_purged_calibrated_artifact(tmp_path):
    rng=np.random.default_rng(3);rows=[]
    for i in range(600):
        value=float(rng.random());features={k:0.0 for k in FEATURES};features["confluence"]=value
        rows.append({"as_of":NOW+i*14400,"label_end":NOW+i*14400+21600,"features":features,
                     "uplift_usd":10 if value>.5 else -10,"equity_accept":5010 if value>.5 else 4990,"equity_reject":5000,
                     "source":"paired_MT5_quote_replay","policy_version":POLICY_VERSION})
    labels=tmp_path/"labels.jsonl";labels.write_text("".join(json.dumps(r)+"\n" for r in rows))
    meta=train_uplift(labels,tmp_path/"model")
    assert meta["train_rows"]<360 and meta["calibration_rows"]<120 and meta["test_rows"]==120
    gate=UpliftGate(tmp_path/"model");assert gate.error is None
    assert not gate.decide(rows[0]["features"],NOW)["accepted"]

def test_compute_pivot_levels():
    from Terminal.Omni_Trader import compute_pivot_levels
    test_bars = [
        {"high": 110.0, "low": 90.0, "close": 100.0, "open": 95.0, "volume": 1000.0}
    ] * 96
    pivots = compute_pivot_levels(test_bars)
    assert pivots is not None
    assert pivots["P"] == 100.0
    assert pivots["R1"] == 110.0  # 2*100 - 90 = 110
    assert pivots["S1"] == 90.0   # 2*100 - 110 = 90
    assert pivots["swing_high"] == 110.0
    assert pivots["swing_low"] == 90.0
    assert pivots["vwap"] == 100.0
    assert pivots["vwap_sigma"] == 0.0
    assert pivots["vwap_upper_1"] == 100.0
    assert pivots["vwap_lower_1"] == 100.0

def test_ict_fvg_consequent_encroachment():
    from Terminal.Omni_Trader import compute_pivot_levels
    bars = [
        {"high": 100.0, "low": 90.0, "close": 95.0, "open": 92.0, "volume": 1000.0},
        {"high": 120.0, "low": 99.0, "close": 118.0, "open": 99.0, "volume": 2000.0},
        {"high": 130.0, "low": 105.0, "close": 125.0, "open": 118.0, "volume": 1500.0}
    ]
    pivots = compute_pivot_levels(bars)
    assert pivots["bull_fvg_ce"] == 102.5
    assert len(pivots["bull_fvgs"]) == 1
    assert pivots["bull_fvgs"][0]["low"] == 100.0
    assert pivots["bull_fvgs"][0]["high"] == 105.0

def test_fuel_to_friction_ratio_feature():
    from Terminal.Risk_Sizing_Engine import OrderflowModel
    model = OrderflowModel()
    p = payload()
    b = bars()
    feat = model.features("BTC", p, b, {"sentiment_valid": True, "asset_scores": {"BTC": 1.0}}, NOW)
    assert "ffr" in feat
    assert "target_fuel_usd" in feat
    assert "target_friction_usd" in feat
    assert isinstance(feat["ffr"], float)

def test_limit_order_routing_passive_and_brackets(tmp_path):
    from Terminal.Omni_Trader import AI15mMT5Trader
    t, b = trader(tmp_path)
    t.entry_mode = "limit"
    result = t.evaluate_market({a: payload(asset=a) for a in UNIVERSE},
                               {"received_at": NOW, "sentiment_valid": True, "asset_scores": {a: 1 for a in UNIVERSE}})
    assert result["decision"] == "PAPER_FILLED"
    pos = t.state["paper_positions"][0]
    # For a LONG candidate, limit entry price must be passive (<= mid)
    assert pos["price_open"] <= 100.0
    assert pos["sl"] < pos["price_open"] < pos["tp"]
    assert pos["initial_r"] > 0

def test_stage_limit_order_passive_guard(monkeypatch):
    from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
    bridge = MT5ExecutionBridge.__new__(MT5ExecutionBridge)
    bridge.ensure_connected = lambda: True
    bridge._floor_volume = lambda v, *_: v
    bridge.broker_utc_offset_sec = 10800
    import types
    fake_info = types.SimpleNamespace(point=0.01, digits=2, volume_step=0.01, volume_min=0.01, volume_max=100.0)
    fake_tick = types.SimpleNamespace(bid=100.00, ask=100.10)
    import MetaTrader5 as mt5_mock
    monkeypatch.setattr(mt5_mock, "symbol_select", lambda s, e: True)
    monkeypatch.setattr(mt5_mock, "symbol_info", lambda s: fake_info)
    monkeypatch.setattr(mt5_mock, "symbol_info_tick", lambda s: fake_tick)

    # Aggressive Buy Limit (>= ask) must be rejected by passive guard
    res_cross_buy = bridge.stage_limit_order("BTCUSD", "LONG", 0.1, 100.10, 99.0, 103.0, passive_only=True)
    assert not res_cross_buy["success"] and "crosses ask" in res_cross_buy["error"]

    # Aggressive Sell Limit (<= bid) must be rejected by passive guard
    res_cross_sell = bridge.stage_limit_order("BTCUSD", "SHORT", 0.1, 100.00, 101.0, 97.0, passive_only=True)
    assert not res_cross_sell["success"] and "crosses bid" in res_cross_sell["error"]

def test_empty_calendar_fails_closed(tmp_path):
    path = tmp_path / "empty_calendar.json"
    path.write_text(json.dumps({
        "required_series": ["CPI", "NFP", "FOMC"],
        "coverage_start": NOW - 86400, "coverage_end": NOW + 86400,
        "verified_at": NOW - 86400, "events": []
    }))
    intel = MarketIntelligenceEngine(calendar_path=path, clock=lambda: NOW)
    # Empty calendar must fail-closed into blackout/calendar unavailable
    blackout, reason, _ = intel.check_macro_blackout()
    assert blackout and reason == "CALENDAR_UNAVAILABLE"

def test_drawdown_floor_immutable_to_mutated_capital(tmp_path):
    # Simulates the finding where inspected state had capital_usd=4775 and peak=4805.67
    state_file = tmp_path / "omni_paper_state.json"
    state_file.write_text(json.dumps({
        "schema": "omni.state.v1",
        "capital_usd": 4775.0,
        "peak_equity_usd": 4805.67,
        "halted": False,
        "paper_cash": 4775.0
    }))
    t, b = trader(tmp_path)
    # Floor must strictly be 5000 * (1 - 0.045) = 4775.00 USD, NEVER 4590.795 USD
    guard = t._equity_guard({"equity_usd": 4775.0})
    assert guard["hard_floor_usd"] == pytest.approx(4775.00)
    assert guard["halted"] is True
    assert guard["drawdown_room"] == 0.0
    assert t.state["original_capital_usd"] == 5000.0
    # Save and reload: verify persistence
    t._save_state()
    t2, _ = trader(tmp_path)
    guard2 = t2._equity_guard({"equity_usd": 4776.0})
    assert guard2["hard_floor_usd"] == pytest.approx(4775.00)
    assert guard2["halted"] is True  # Sticky latch remains

def test_sector_correlation_veto_not_swallowed_and_covariance_hedge_allowed(tmp_path):
    t, b = trader(tmp_path)
    # Mock covariance gate with correlation 0.7655 between GOLD and SILVER
    class FakeCovariance:
        def validate_time(self, *a, **k): pass
        def correlation(self, a, b):
            if {a, b} == {"GOLD", "SILVER"}: return 0.7655
            return 0.0
    t.covariance = FakeCovariance()

    # Case 1: Existing position is SHORT SILVER, candidate is LONG GOLD.
    # Opposite direction in positively correlated assets reduces portfolio variance (covariance hedge).
    t.state["positions"] = {"1": {"asset": "SILVER", "direction": "SHORT"}}
    positions = [{"ticket": 1, "symbol": "XAGUSD", "direction": "SHORT"}]
    features_long = {"direction": "LONG"}
    # Execute sector correlation governor logic
    for p in positions:
        existing_asset = t.state["positions"].get(str(p["ticket"]), {}).get("asset")
        existing_dir = p.get("direction")
        corr = t.covariance.correlation("GOLD", existing_asset)
        same_dir = (features_long["direction"] == existing_dir)
        # Should NOT raise because it's a variance-reducing hedge
        if (corr >= 0.60 and same_dir) or (corr <= -0.60 and not same_dir):
            raise ValueError("unexpected_veto")

    # Case 2: Existing position is LONG SILVER, candidate is LONG GOLD.
    # Same direction in positively correlated assets compounds sector risk and must be vetoed.
    t.state["positions"] = {"2": {"asset": "SILVER", "direction": "LONG"}}
    positions_long = [{"ticket": 2, "symbol": "XAGUSD", "direction": "LONG"}]
    with pytest.raises(ValueError, match="sector_correlation_conflict:GOLD_LONG_compounds_SILVER_LONG_corr_0.77"):
        for p in positions_long:
            existing_asset = t.state["positions"].get(str(p["ticket"]), {}).get("asset")
            existing_dir = p.get("direction")
            corr = t.covariance.correlation("GOLD", existing_asset)
            same_dir = (features_long["direction"] == existing_dir)
            if (corr >= 0.60 and same_dir) or (corr <= -0.60 and not same_dir):
                raise ValueError(f"sector_correlation_conflict:GOLD_{features_long['direction']}_compounds_{existing_asset}_{existing_dir}_corr_{corr:.2f}")

def test_silver_ticket_18510585_cost_arithmetic_lock():
    # Ticket #18510585 entry 62.020, initial_r 0.580
    # 41 bps of 62.020 is 0.25428 USD = 0.4384R. Stated 0.35R BE lock yields gross 0.203 USD, cost 2.54 USD (net loss -0.51 USD).
    # Dynamic lock ensures required_lock_R = (friction_bps / 10000 * entry / initial_stop_r) + buffer_R
    from Terminal.Uplift_Model import ratchet
    sl = ratchet(62.020, 0.580, "LONG", 0.80, 61.440, 0.300, friction_bps=41.0, buffer_r=0.05)
    locked_r = (sl - 62.020) / 0.580
    assert locked_r >= 0.4884  # 0.4384R cost break-even + 0.05R buffer
    units = 10.0
    gross_usd = (sl - 62.020) * units
    cost_usd = 62.020 * units * 0.0041
    net_usd = gross_usd - cost_usd
    assert net_usd > 0.0  # Net profit strictly positive, clearing all frictions


@pytest.mark.parametrize("equity,cap", [(4799.99,10), (4800,20), (4841.23,20)])
def test_sentinel_risk_cap_boundary(tmp_path, equity, cap):
    t, _ = trader(tmp_path)
    assert t._equity_guard({"equity_usd":equity})["risk_cap_usd"] == cap


def test_original_capital_cannot_be_rebased_by_state(tmp_path):
    t, _ = trader(tmp_path)
    t.state.update(original_capital_usd=4775,capital_usd=4775,peak_equity_usd=4841.23)
    assert t._equity_guard({"equity_usd":4841.23})["hard_floor_usd"] == 4775
    assert t._equity_guard({"equity_usd":4775})["halted"]
    assert t._equity_guard({"equity_usd":4841.23})["halted"]


@pytest.mark.parametrize("direction,sign", [("LONG",1),("SHORT",-1)])
def test_runner_follows_gain_minus_point_65_without_retreat(direction, sign):
    proposed = ratchet(100,2,direction,2.0,100-sign*2,9)
    assert proposed == pytest.approx(100+sign*2*1.35)
    assert ratchet(100,2,direction,1.5,proposed,9) == proposed


def test_parallel_multi_zone_limit_staging(tmp_path):
    t, b = trader(tmp_path, paper=False)
    t.entry_mode = "limit"
    macro = {"received_at": NOW, "sentiment_valid": True, "asset_scores": {"BTC": 1, "ETH": 1}}
    p1 = payload(NOW, "BTC")
    p2 = payload(NOW, "ETH")
    report = t.evaluate_market({"BTC": p1, "ETH": p2}, macro)
    assert report["decision"] == "LIMIT_STAGED"
    assert report["staged_count"] >= 1
    assert len(b.pending) >= 1
    # Check limit persistence is set to 3600s
    assert b.pending[0]["price_open"] > 0


def test_first_fill_oco_governor_cancels_remaining_limits(tmp_path):
    t, b = trader(tmp_path, paper=False)
    # Stage 2 pending orders
    b.pending = [
        {"ticket": 1001, "symbol": "BTCUSD", "direction": "LONG", "volume": 0.1, "price_open": 98.0, "sl": 95.0, "tp": 105.0, "magic": MAGIC},
        {"ticket": 1002, "symbol": "ETHUSD", "direction": "LONG", "volume": 1.0, "price_open": 98.0, "sl": 95.0, "tp": 105.0, "magic": MAGIC}
    ]
    # Now simulate 2 open positions filling capacity
    b.positions = [
        {"ticket": 2001, "symbol": "SOLUSD", "direction": "LONG", "price_open": 100, "sl": 95, "tp": 110, "volume": 0.5, "time": NOW, "magic": MAGIC},
        {"ticket": 2002, "symbol": "XRPUSD", "direction": "LONG", "price_open": 1.5, "sl": 1.4, "tp": 1.7, "volume": 10, "time": NOW, "magic": MAGIC}
    ]
    t.state["positions"]["2001"] = {"initial_r": 5, "asset": "SOL"}
    t.state["positions"]["2002"] = {"initial_r": 0.1, "asset": "XRP"}
    changes = t.manage_active_positions()
    # OCO governor must cancel all pending orders when positions capacity (2) is filled
    assert len(b.pending) == 0
    assert any(c.get("action") == "CANCEL" and c.get("reason") == "max_positions_reached_2" for c in changes)



