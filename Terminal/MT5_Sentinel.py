"""Broker-authoritative surveillance. Enforcement only reduces existing exposure."""
from __future__ import annotations
import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import urllib.request
import uuid

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from Terminal.Asset_Universe import UNIVERSE, canonical_asset
from Terminal.MT5_Execution_Bridge import MT5ExecutionBridge
from Terminal.Risk_Sizing_Engine import epoch
from Terminal.Uplift_Model import UpliftGate, executable_ratchet, POLICY_VERSION

ACCOUNT = 5064568
FLOOR = 4775.0

def next_wakeup(now):
    candidate = now.replace(second=0, microsecond=0)+timedelta(minutes=1)
    while candidate.minute not in (14,29,44,59): candidate += timedelta(minutes=1)
    return candidate.isoformat()

def last_record(path):
    if not path.exists(): return {}
    with path.open('rb') as stream:
        stream.seek(0,2); size=stream.tell(); stream.seek(max(0,size-262144))
        lines=stream.read().splitlines()
    for line in reversed(lines):
        try: return json.loads(line)
        except (ValueError, UnicodeDecodeError): continue
    return {}

def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+'.'+uuid.uuid4().hex+'.tmp')
    with temp.open('x', encoding='utf-8') as stream:
        json.dump(value, stream, allow_nan=False); stream.flush(); os.fsync(stream.fileno())
    os.replace(temp, path)

def feed_health(asset):
    try:
        with urllib.request.urlopen('http://127.0.0.1:8095/api/live/'+asset, timeout=4) as response:
            payload=json.load(response)
        book=payload.get('l2_book') or {}
        stamp=epoch(book.get('timestamp'))
        return {'asset':asset,'http_ok':True,'book_age_seconds':round(time.time()-stamp,3) if stamp else None,
                'has_two_sided_book':bool(book.get('bids') and book.get('asks'))}
    except Exception as exc: return {'asset':asset,'http_ok':False,'error':str(exc)}

def inspect_position(position, state, bridge, now):
    meta=state.get('positions',{}).get(str(position['ticket']),{})
    quote=bridge.get_symbol_price(position['symbol'])
    entry=position['price_open']; sign=1 if position['direction']=='LONG' else -1
    initial_r=meta.get('initial_r')
    result={**position,'initial_r':initial_r,'required_sl':None,'ratchet_verified':False,
            'modeled_net_lock_usd':None,'r_multiple':None,'tp_distance':None}
    if not quote: return dict(result,error='broker_quote_unavailable')
    mark=quote['bid'] if sign==1 else quote['ask']
    result['current_exit_price']=mark
    result['tp_distance']=sign*(position['tp']-mark) if position.get('tp') else None
    if position.get('sl'):
        units=position['volume']*quote['contract_size']
        result['modeled_net_lock_usd']=round(sign*(position['sl']-entry)*units-entry*units*.0041,4)
    if not initial_r or initial_r<=0: return dict(result,error='initial_r_unknown')
    gain=sign*(mark-entry)/initial_r; result['r_multiple']=gain
    distance=max(quote.get('stops_level',0),quote.get('freeze_level',0),1)*quote['point']
    tick=max(quote.get('tick_size',0),quote['point'])
    result['required_sl']=executable_ratchet(entry,initial_r,position['direction'],gain,position['sl'],
        meta.get('atr',initial_r*.5),quote['bid'],quote['ask'],tick,distance,friction_bps=41,buffer_r=.05)
    result['ratchet_verified']=sign*(position['sl']-result['required_sl'])>=-tick*.01
    result['age_bars']=(now.timestamp()-epoch(position['time']))/900
    return result

def collect(enforce=False):
    import MetaTrader5 as mt5
    now=datetime.now(timezone.utc)
    if not mt5.initialize(path=r'C:\Program Files\MetaTrader 5\terminal64.exe', timeout=10000):
        raise RuntimeError('MT5 initialization failed: '+str(mt5.last_error()))
    try:
        account=mt5.account_info()
        if account is None or account.login!=ACCOUNT or account.currency!='USD':
            raise RuntimeError('target_account_identity_unverified')
        state_path=ROOT/'Data/mt5_ai_trader_state.json'
        state=json.loads(state_path.read_text(encoding='utf-8'))
        bridge=MT5ExecutionBridge(account_id=ACCOUNT)
        positions=bridge.get_open_positions(); orders=bridge.get_pending_orders()
        decision=last_record(ROOT/'Data/Omni/live/decisions.jsonl')
        actions=[]
        if enforce and (account.equity<=FLOOR or state.get('halted') or (ROOT/'Data/Omni/live/emergency_halt.json').exists()):
            atomic_json(ROOT/'Data/Omni/live/emergency_halt.json',{'time_utc':now.isoformat(),'account':ACCOUNT,'equity':account.equity,'floor':FLOOR})
            latest=json.loads(state_path.read_text(encoding='utf-8')); latest['halted']=True
            atomic_json(state_path, latest)
            for order in orders: actions.append({'action':'cancel','ticket':order['ticket'],'result':bridge.cancel_pending_order(order['ticket'])})
            for position in positions: actions.append({'action':'emergency_close','ticket':position['ticket'],'result':bridge.close_position(position['ticket'])})
            positions=bridge.get_open_positions(); orders=bridge.get_pending_orders(); account=mt5.account_info()
            state=json.loads(state_path.read_text(encoding='utf-8'))
        elif enforce:
            for order in orders:
                intent=next((i for i in state.get('intents',{}).values() if i.get('order_ticket')==order['ticket']),None)
                if not intent: continue
                asset=intent.get('candidate',{}).get('asset',canonical_asset(order['symbol']))
                staged_slot=int(epoch(intent.get('prepared_at'))//900)
                if decision.get('slot',-1)>staged_slot and decision.get('vetoes',{}).get(asset)=='confluence_below_threshold':
                    actions.append({'action':'cancel_degraded_confluence','ticket':order['ticket'],'result':bridge.cancel_pending_order(order['ticket'])})
            orders=bridge.get_pending_orders()
        positions=bridge.get_open_positions(); orders=bridge.get_pending_orders(); account=mt5.account_info()
        if account is None or account.login!=ACCOUNT: raise RuntimeError('final_account_snapshot_unavailable')
        account_as_of=datetime.now(timezone.utc).isoformat()
        details=[inspect_position(p,state,bridge,now) for p in positions]
        deals=mt5.history_deals_get(now-timedelta(hours=2),now)
        history=mt5.history_orders_get(now-timedelta(hours=2),now)
        gate=UpliftGate(ROOT/'Data/Models/omni_uplift')
        xrp=bridge.resolve_symbol('XRP'); info=mt5.symbol_info(xrp) if xrp else None
        with ThreadPoolExecutor(max_workers=8) as pool: feeds=list(pool.map(feed_health,UNIVERSE))
        current=datetime.now(timezone.utc)
        return {'as_of_utc':current.isoformat(),'account_as_of_utc':account_as_of,'account':ACCOUNT,'balance_usd':account.balance,'floating_pnl_usd':account.profit,
            'equity_usd':account.equity,'floor_usd':FLOOR,'cushion_usd':round(account.equity-FLOOR,2),
            'margin_usd':account.margin,'margin_free_usd':account.margin_free,
            'margin_utilization_pct':round(account.margin/account.equity*100,4) if account.equity else None,
            'positions':details,'pending_orders':orders,'actions':actions,'halted':bool(state.get('halted')),
            'risk_cap_usd':10 if account.equity<4800 else 20,'configured_assets':list(UNIVERSE),
            'state':{k:state.get(k) for k in ('original_capital_usd','capital_usd','peak_equity_usd','last_slot')},
            'decision':decision,'decision_age_seconds':round(current.timestamp()-decision.get('time',0),3),
            'veto_counts':dict(Counter(decision.get('vetoes',{}).values())), 'feeds':feeds,
            'recent_closed_deals':None if deals is None else [{'ticket':d.ticket,'position_id':d.position_id,'symbol':d.symbol,
                'entry':d.entry,'profit_usd':d.profit,'swap_usd':d.swap,'commission_usd':d.commission,'fee_usd':d.fee,
                'net_usd':round(d.profit+d.swap+d.commission+d.fee,2)} for d in deals if d.entry in (1,2,3)],
            'recent_expired_orders':None if history is None else [{'ticket':o.ticket,'symbol':o.symbol,'state':o.state} for o in history if o.state==mt5.ORDER_STATE_EXPIRED],
            'xrp_broker_constraints':None if info is None else {'symbol':xrp,'stops_level_points':info.trade_stops_level,
                'point':info.point,'minimum_distance':info.trade_stops_level*info.point},
            'uplift_status':gate.error or 'loaded; inference still requires qualification','policy_version':POLICY_VERSION,
            'next_wakeup_utc':next_wakeup(current), 'profit_lock_basis':'Modeled net lock, not a guaranteed stop execution price'}
    finally: mt5.shutdown()

def persist(report, journal=False):
    folder=ROOT/'Data/Omni/sentinel'; folder.mkdir(parents=True,exist_ok=True)
    path=folder/(datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8]+'.json')
    data=json.dumps(report,sort_keys=True,indent=2,allow_nan=False).encode('utf-8')
    with path.open('xb') as stream: stream.write(data); stream.flush(); os.fsync(stream.fileno())
    record={'as_of_utc':report['as_of_utc'],'path':str(path),'sha256':hashlib.sha256(data).hexdigest()}
    with (folder/'audit.jsonl').open('a',encoding='utf-8') as stream:
        stream.write(json.dumps(record)+'\n'); stream.flush(); os.fsync(stream.fileno())
    if journal:
        text='\n\n### OMNI Sentinel — '+report['as_of_utc']+'\n\n'
        text+=f"Account {ACCOUNT}: balance {report['balance_usd']:.2f} USD; equity {report['equity_usd']:.2f} USD; cushion {report['cushion_usd']:.2f} USD; positions {len(report['positions'])}/2; pending {len(report['pending_orders'])}; halted {report['halted']}.\n"
        text+='Decision: '+json.dumps(report['decision'],sort_keys=True)+'.\n'
        text+='Actions: '+json.dumps(report['actions'])+'. Uplift: '+str(report['uplift_status'])+'.\n'
        text+='Audit: '+str(path)+'. SHA256: '+record['sha256']+'. Next wake UTC: '+report['next_wakeup_utc']+'.\n'
        with (ROOT/'.agents/memory/session_chat_history.md').open('a',encoding='utf-8') as stream:
            stream.write(text); stream.flush(); os.fsync(stream.fileno())
    return record

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--enforce',action='store_true',help='Emergency flatten and cancel degraded pending orders; never open positions')
    parser.add_argument('--journal',action='store_true',help='Append the surveillance record to session history')
    args=parser.parse_args()
    report=collect(args.enforce); record=persist(report,args.journal)
    print(json.dumps({'report':report,'audit':record},default=str))
