"""Execution failure tests use a fake IPC module; never connect to a terminal."""
import copy
import json
import time
from types import SimpleNamespace as NS
from datetime import datetime, timezone
import pytest
from Terminal import MT5_Execution_Bridge as module
from Terminal.Api_Client import HyperdashClient
from Terminal.Macro_Calendar import parse_bls, parse_fed, refresh_calendar
from Terminal.Uplift_Model import executable_ratchet

def ipc(monkeypatch, codes, check=0):
    sends=[]
    info=NS(digits=2,point=.01,volume_step=.25,volume_min=.25,volume_max=10,
            trade_stops_level=0,trade_freeze_level=0)
    tick=NS(bid=100.0,ask=100.02,time_msc=int(time.time()*1000))
    results=[NS(retcode=c,comment="fake",order=123,deal=456,volume=.25,price=100.02) if c is not None else None for c in codes]
    def send(request): sends.append(copy.deepcopy(request));return results.pop(0)
    fake=NS(terminal_info=lambda:NS(connected=True),
            account_info=lambda:NS(login=1, trade_mode=0, company="Blueberry", currency="USD",
                                   balance=5000.0, equity=5000.0, profit=0.0, margin=0.0, margin_free=5000.0, margin_level=0.0),
            positions_get=lambda *x:(), orders_get=lambda *x:(),
            order_calc_profit=lambda *x:-24.0, order_calc_margin=lambda *x:100.0,
            symbol_select=lambda *x:True,
            symbol_info=lambda *x:info,symbol_info_tick=lambda *x:tick,order_check=lambda x:NS(retcode=check,comment="check"),
            order_send=send,last_error=lambda:(0,"fake"),ORDER_TYPE_BUY=0,ORDER_TYPE_SELL=1,
            ORDER_TYPE_BUY_LIMIT=2,TRADE_ACTION_PENDING=5,
            TRADE_ACTION_DEAL=1,TRADE_ACTION_SLTP=6,ORDER_TIME_GTC=0,ORDER_FILLING_IOC=1,ORDER_FILLING_FOK=0,ORDER_FILLING_RETURN=2,
            TRADE_RETCODE_DONE=10009,TRADE_RETCODE_DONE_PARTIAL=10010,TRADE_RETCODE_INVALID_FILL=10030,TRADE_RETCODE_PLACED=10008)
    monkeypatch.setattr(module,"mt5",fake);monkeypatch.setattr(module,"MT5_AVAILABLE",True)
    bridge=module.MT5ExecutionBridge()
    # This fake IPC explicitly emits UTC timestamps, unlike the configured
    # Blueberry server-time default. Do not conflate clock and retry tests.
    bridge.broker_utc_offset_sec = 0
    bridge.broker_utc_offset_ms = 0
    # Model two advancing observations before testing the send/retry path.
    wall, mono = time.time(), time.monotonic()
    bridge.broker_clock.tick_age_seconds(tick.time_msc-1000, symbol="BTCUSD", now=wall-1, monotonic_now=mono-1)
    bridge.broker_clock.tick_age_seconds(tick.time_msc, symbol="BTCUSD", now=wall, monotonic_now=mono)
    return bridge,fake,sends


def test_pending_limit_rejects_broker_distance_without_sending(monkeypatch):
    bridge,fake,sends=ipc(monkeypatch,[10009])
    fake.symbol_info("XRP").trade_stops_level=20
    result=bridge.stage_limit_order("XRP","LONG",.5,99.90,99.0,101.0)
    assert result["error"]=="pending_entry_inside_broker_stops_level" and not sends


def test_pending_brackets_reject_broker_distance_without_sending(monkeypatch):
    bridge,fake,sends=ipc(monkeypatch,[10009])
    fake.symbol_info("XRP").trade_stops_level=20
    result=bridge.stage_limit_order("XRP","SHORT",.5,100.30,100.40,99.0)
    assert result["error"]=="pending_bracket_inside_broker_stops_level" and not sends


def test_pending_order_check_rejection_never_sends(monkeypatch):
    bridge,fake,sends=ipc(monkeypatch,[10009],check=10015)
    fake.TRADE_ACTION_PENDING=5
    result=bridge.stage_limit_order("XRP","LONG",.5,99.70,99.0,101.0)
    assert not result["success"] and result["retcode"]==10015 and not sends

@pytest.mark.parametrize("code",[None,10012,10031,10008])
def test_timeout_or_ambiguous_send_is_not_retried(monkeypatch,code):
    bridge,_,sends=ipc(monkeypatch,[code,10009])
    result=bridge.execute_market_order("BTCUSD","LONG",.5,98,106)
    assert not result["success"] and result["uncertain"] and len(sends)==1


@pytest.mark.parametrize("code", [None, 10012, 10031, 10010])
def test_pending_ambiguous_ack_never_becomes_confirmed_rejection(monkeypatch, code):
    bridge, _, sends = ipc(monkeypatch, [code])
    result = bridge.stage_limit_order("BTCUSD", "LONG", .5, 99, 98, 106)
    assert not result["success"] and result["uncertain"] and len(sends) == 1


def test_pending_send_exception_is_uncertain(monkeypatch):
    bridge, fake, sends = ipc(monkeypatch, [10009])
    def send(request):
        sends.append(request)
        raise RuntimeError("lost acknowledgment after submission")
    fake.order_send = send
    result = bridge.stage_limit_order("BTCUSD", "LONG", .5, 99, 98, 106)
    assert result["uncertain"] and len(sends) == 1

@pytest.mark.parametrize("mode", ["limit", "market"])
def test_entry_deadline_rechecked_after_broker_order_check(monkeypatch, mode):
    bridge, fake, sends = ipc(monkeypatch, [10009])
    checked = []
    fake.order_check = lambda request: checked.append(request) or NS(retcode=0, comment="ok")
    def expired():
        assert checked
        raise ValueError("execution_window_expired_or_clock_unverified")
    result = (bridge.stage_limit_order("BTCUSD", "LONG", .5, 99, 98, 106, entry_guard=expired)
              if mode == "limit" else bridge.execute_market_order("BTCUSD", "LONG", .5, 98, 106, entry_guard=expired))
    assert not result["success"] and not result.get("uncertain") and not sends
    assert result["error"].startswith("entry_guard_veto:")


def test_invalid_fill_retry_checks_deadline_again(monkeypatch):
    bridge, _, sends = ipc(monkeypatch, [10030, 10009])
    def guard():
        if sends:
            raise ValueError("execution_window_expired_or_clock_unverified")
    result = bridge.execute_market_order("BTCUSD", "LONG", .5, 98, 106, entry_guard=guard)
    assert not result["success"] and not result.get("uncertain") and len(sends) == 1


@pytest.mark.parametrize("mode", ["limit", "market"])
def test_successful_slow_guard_cannot_send_an_aged_quote(monkeypatch, mode):
    bridge, _, sends = ipc(monkeypatch, [10009])
    elapsed = [0.0]
    bridge.tick_age_seconds = lambda tick, symbol: 0.0
    monkeypatch.setattr(module.time, "monotonic", lambda: elapsed[0])
    def slow_guard():
        elapsed[0] += 3.0
    result = (bridge.stage_limit_order("BTCUSD", "LONG", .5, 99, 98, 106, entry_guard=slow_guard)
              if mode == "limit" else bridge.execute_market_order("BTCUSD", "LONG", .5, 98, 106, entry_guard=slow_guard))
    assert not result["success"] and not result.get("uncertain") and not sends
    assert result["error"] == "pre_send_quote_stale_or_clock_unverified"


@pytest.mark.parametrize("mode", ["limit", "market"])
def test_quote_cannot_age_during_broker_check_then_send(monkeypatch, mode):
    bridge, fake, sends = ipc(monkeypatch, [10009])
    checked = []
    fake.order_check = lambda request: checked.append(request) or NS(retcode=0, comment="ok")
    bridge.tick_age_seconds = lambda tick, symbol: 3.0 if checked else 0.0
    result = (bridge.stage_limit_order("BTCUSD", "LONG", .5, 99, 98, 106)
              if mode == "limit" else bridge.execute_market_order("BTCUSD", "LONG", .5, 98, 106))
    assert not result["success"] and not sends
    assert result["error"] == "pre_send_quote_stale_or_clock_unverified"


def test_only_invalid_fill_can_retry(monkeypatch):
    bridge,_,sends=ipc(monkeypatch,[10030,10009])
    result=bridge.execute_market_order("BTCUSD","LONG",.5,98,106)
    assert result["success"] and len(sends)==2
    assert sends[0]["type_filling"] != sends[1]["type_filling"]

def test_partial_fill_returns_actual_volume_without_resubmission(monkeypatch):
    bridge,_,sends=ipc(monkeypatch,[10010,10009])
    result=bridge.execute_market_order("BTCUSD","LONG",.5,98,106)
    assert result["success"] and result["partial"] and result["volume"]==.25 and len(sends)==1

def test_failed_order_check_never_sends(monkeypatch):
    bridge,_,sends=ipc(monkeypatch,[10009],check=10019)
    assert not bridge.execute_market_order("BTCUSD","LONG",.5,98,106)["success"]
    assert not sends

def test_missing_order_check_never_sends(monkeypatch):
    bridge,fake,sends=ipc(monkeypatch,[10009]);fake.order_check=lambda x:None
    assert not bridge.execute_market_order("BTCUSD","LONG",.5,98,106)["success"] and not sends

def test_failed_position_inventory_is_not_flat_account(monkeypatch):
    bridge,fake,_=ipc(monkeypatch,[]);fake.positions_get=lambda **k:None
    with pytest.raises(RuntimeError,match="inventory failed"): bridge.get_open_positions()

def test_ratchet_preserves_tp_and_cannot_remove_protection(monkeypatch):
    bridge,fake,sends=ipc(monkeypatch,[10009])
    position=NS(symbol="BTCUSD",sl=98,tp=106,type=0)
    fake.positions_get=lambda **k:[position]
    assert not bridge.modify_position_sltp(123,0)["success"]
    assert not bridge.modify_position_sltp(123,97)["success"]
    assert bridge.modify_position_sltp(123,99)["success"]
    assert sends[0]["tp"]==106

def test_freeze_distance_replay_matches_live_ratchet_constraint():
    assert executable_ratchet(100,1,"LONG",.8,99,.5,100.8,100.82,.01,.6)==99
    assert executable_ratchet(100,1,"LONG",.8,99,.5,100.8,100.82,.01,.01,friction_bps=0,buffer_r=0)==pytest.approx(100.35)
    assert executable_ratchet(100,1,"LONG",.8,99,.5,100.8,100.82,.01,.01)==pytest.approx(100.46)

def test_ratchet_clears_roundtrip_friction_for_silver():
    # Silver counterexample from microstructure audit (entry 62.02, initial_r 0.58)
    # Stated 41 bps friction requires 0.4384R to break even net.
    sl = executable_ratchet(62.02, 0.58, "LONG", 0.8, 61.44, 0.3, 62.6, 62.61, 0.001, 0.01, friction_bps=41.0, buffer_r=0.05)
    assert sl >= 62.02 + 0.4384 * 0.58
    locked_r = (sl - 62.02) / 0.58
    assert locked_r >= 0.487
    gross = (sl - 62.02) * 10.0
    cost = 62.02 * 10.0 * 0.0041
    assert gross - cost > 0

def test_hip3_names_are_observed_not_injected(monkeypatch):
    client=HyperdashClient()
    def post(url,payload):
        dex=payload.get("dex")
        coins=["BTC"] if dex is None else ["GOLD"] if dex=="xyz" else ["USA100","DJI"]
        return [{"universe":[{"name":c} for c in coins]},[{"markPx":"100","funding":".00001"} for c in coins]]
    monkeypatch.setattr(client,"_post_json",post)
    assets=client.fetch_all_assets()
    assert client._resolve_coin("NAS100")=="flx:USA100" and client._resolve_coin("DJ30")=="flx:DJI"
    assert "SILVER" not in client.universe and "SP500" not in client.universe
    assert client._resolve_coin("GOLD")=="xyz:GOLD"

def test_wallet_risk_uses_reported_leverage_exposure_and_explicit_stop_type(monkeypatch):
    client=HyperdashClient()
    def post(url,payload):
        if payload["type"]=="clearinghouseState":
            return {"assetPositions":[{"position":{"coin":"BTC","szi":"2","entryPx":"101","positionValue":"200","unrealizedPnl":"-2","liquidationPx":"99.9"}}]}
        return [{"coin":"BTC","isTrigger":True,"reduceOnly":True,"orderType":"Stop Market","side":"A","triggerPx":"99.95","sz":"2","oid":1},
                {"coin":"BTC","isTrigger":True,"reduceOnly":True,"orderType":"Take Profit Market","side":"A","triggerPx":"110","sz":"2"}]
    monkeypatch.setattr(client,"_post_json",post)
    risk=client.fetch_wallet_risk("BTC",["wallet"],{"best_bid":99.99,"best_ask":100.01})
    assert risk["liquidations"]["bands"][0]["amount_usd"]==199.8
    assert risk["positions"][0]["unrealized_pnl_usd"]==-2
    assert len(risk["stops"]["bands"])==1 and risk["liquidations"]["coverage"]=="SAMPLED_WALLETS"
    stop = risk["stops"]["bands"][0]
    assert stop["min_px"] == stop["max_px"] == stop["mid_px"] == 99.95
    assert risk["liquidations"]["bands"][0]["min_px"] == 99.9

def test_bls_parser_handles_eastern_dst():
    text="BEGIN:VEVENT\nSUMMARY:Consumer Price Index\nDTSTART;TZID=America/New_York:20261014T083000\nEND:VEVENT\nBEGIN:VEVENT\nSUMMARY:Employment Situation\nDTSTART;TZID=America/New_York:20261106T083000\nEND:VEVENT"
    events=parse_bls(text)
    assert events[0]["time_utc"]=="2026-10-14T12:30:00+00:00"
    assert events[1]["time_utc"]=="2026-11-06T13:30:00+00:00"

def test_fed_parser_only_uses_dated_fomc_section():
    html='<div><h4>FOMC Meetings</h4></div><div><div class="panel-body"><div><div>2:00 p.m.</div><div>FOMC Meeting</div><div>28</div></div></div></div><div><h4>Other</h4></div>'
    events=parse_fed(html,2026,10,"official")
    assert events==[{"name":"FOMC","time_utc":"2026-10-28T18:00:00+00:00","impact":"HIGH","source":"official"}]
    with pytest.raises(ValueError): parse_fed("<h4>Changed format</h4>",2026,10,"official")

def test_calendar_refresh_failure_preserves_previous_dated_file(tmp_path):
    path=tmp_path/"calendar.json";path.write_text("existing")
    def broken(url): raise OSError("provider down")
    with pytest.raises(OSError): refresh_calendar(path,datetime(2026,10,5,tzinfo=timezone.utc),broken)
    assert path.read_text()=="existing"

def test_server_does_not_freshen_failed_components_and_clears_empty_walls(monkeypatch):
    import Terminal.Chrome_Terminal as server
    now=time.time();past=now-300
    server.LIVE_ANALYTICS_CACHE["TEST"]={"sources":{"liquidations":{"observed_at":past},"stops":{"observed_at":past}},"l3_orders":[{"price":99,"side":"BUY"}]}
    def down(*args): raise RuntimeError("feed unavailable")
    fake=NS(fetch_liquidations=down,fetch_stops=down,fetch_l3_orders=lambda *a:[],fetch_l2_book=lambda *a:{},
            fetch_wallet_risk=lambda *a:{"observed_at":now,"positions":[],"liquidations":{},"stops":{}})
    monkeypatch.setattr(server,"CLIENT",fake)
    server._refresh_analytics_worker("TEST",100)
    result=server.LIVE_ANALYTICS_CACHE.pop("TEST")
    assert result["sources"]["liquidations"]["observed_at"]==past
    assert result["sources"]["stops"]["observed_at"]==past
    assert result["l3_orders"]==[]

def test_unverified_historical_heatmap_not_published_as_live_chart(monkeypatch):
    import Terminal.Chrome_Terminal as server
    monkeypatch.setattr(server, "get_heatmap_engine", lambda *args, **kwargs: (_ for _ in ()).throw(
        AssertionError("research heatmap must not be consulted by live endpoint")))
    result = server.api_heatmap("BTC", mode="stops")
    assert result["kind"] == "UNAVAILABLE_UNVERIFIED_ANALYTICS"
    assert result["heatmap_grid"] == [] and result["total_long_size"] is None


def test_empty_reported_cohort_never_invents_pnl_or_leverage(monkeypatch):
    import Terminal.Chrome_Terminal as server
    fake = NS(fetch_top_traders=lambda *args, **kwargs: [])
    monkeypatch.setattr(server, "CLIENT", fake)
    result = server.api_cohorts("BTC")
    assert result["cohorts"] == []
    assert result["status"].startswith("UNAVAILABLE")


def test_live_api_uses_book_mid_and_explicit_unknown_cohorts(monkeypatch):
    import Terminal.Chrome_Terminal as server
    book={"best_bid":99,"best_ask":101,"bids":[],"asks":[],"timestamp":time.time()*1000}
    fake=NS(fetch_l2_book=lambda *a:book,fetch_recent_trades=lambda *a:[{"px":"95","sz":"1","side":"?","time":1}])
    monkeypatch.setattr(server,"CLIENT",fake)
    monkeypatch.setattr(server,"get_universe",lambda:[{"coin":"BTC","mark_px":94,"signal_market":"BTC"}])
    monkeypatch.setattr(server,"get_live_analytics",lambda *a:{})
    result=server.api_live("BTC")
    assert result["price"]==100 and result["recent_trades"][0]["side"]=="UNKNOWN"
    assert result["cohort_summary"]["profit_traders_pct"] is None
    assert result["cohort_summary"]["total_traders"] is None  # missing report != zero traders



@pytest.mark.parametrize("state,initial,remaining,uncertain", [(None, 1, 1, True), (6, 1, 1, False), (6, 1, .5, True), (4, 1, 0, True)])
def test_empty_deal_history_cannot_prove_a_lost_submission_failed(monkeypatch, state, initial, remaining, uncertain):
    bridge, fake, _ = ipc(monkeypatch, [10009])
    fake.history_deals_get = lambda *args: []
    fake.history_orders_get = lambda *args: ([] if state is None else [NS(comment="OMNI:lost", magic=100895,
        state=state, volume_initial=initial, volume_current=remaining)])
    assert bridge.intent_filled("OMNI:lost", time.time()-300) is uncertain
