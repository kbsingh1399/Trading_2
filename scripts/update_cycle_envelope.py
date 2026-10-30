import json
import uuid
import datetime
import MetaTrader5 as mt5

def update_envelope():
    if not mt5.initialize():
        print("Failed to initialize MT5")
        return

    acc = mt5.account_info()
    positions = mt5.positions_get()
    orders = mt5.orders_get()
    
    pos_list = []
    if positions:
        for p in positions:
            pos_list.append({
                'ticket': p.ticket,
                'time': p.time,
                'time_msc': p.time_msc,
                'time_update': p.time_update,
                'time_update_msc': p.time_update_msc,
                'type': p.type,
                'magic': p.magic,
                'identifier': p.identifier,
                'reason': p.reason,
                'volume': p.volume,
                'price_open': p.price_open,
                'sl': p.sl,
                'tp': p.tp,
                'price_current': p.price_current,
                'swap': p.swap,
                'profit': p.profit,
                'symbol': p.symbol,
                'comment': p.comment,
                'external_id': p.external_id
            })

    ord_list = []
    if orders:
        for o in orders:
            ord_list.append({
                'ticket': o.ticket,
                'time_setup': o.time_setup,
                'time_setup_msc': o.time_setup_msc,
                'time_done': o.time_done,
                'time_done_msc': o.time_done_msc,
                'time_expiration': o.time_expiration,
                'type': o.type,
                'type_time': o.type_time,
                'type_filling': o.type_filling,
                'state': o.state,
                'magic': o.magic,
                'position_id': o.position_id,
                'position_by_id': o.position_by_id,
                'reason': o.reason,
                'volume_initial': o.volume_initial,
                'volume_current': o.volume_current,
                'price_open': o.price_open,
                'sl': o.sl,
                'tp': o.tp,
                'price_current': o.price_current,
                'price_stoplimit': o.price_stoplimit,
                'symbol': o.symbol,
                'comment': o.comment,
                'external_id': o.external_id
            })

    envelope_file = 'Data/cycle_envelope.json'
    try:
        with open(envelope_file, 'r', encoding='utf-8') as f:
            d = json.load(f)
    except Exception:
        d = {}

    utc_now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    d['cycle_id'] = 'Cycle_025'
    d['uuid'] = str(uuid.uuid4())
    d['dispatch_nonce'] = str(uuid.uuid4())
    d['cutoff_utc'] = utc_now
    d['inventory'] = {
        'account_login': acc.login,
        'server': 'BlueberryMarketsSVG-Live',
        'currency': 'USD',
        'balance': acc.balance,
        'equity': acc.equity,
        'margin_used': acc.margin,
        'margin_free': acc.margin_free,
        'margin_level': acc.margin_level,
        'active_positions_count': len(pos_list),
        'pending_orders_count': len(ord_list),
        'active_positions': pos_list,
        'pending_orders': ord_list
    }
    
    # Update solvency
    hard_floor = 4775.00
    operating_buffer = 4795.00
    d['solvency'] = {
        'hard_floor_usd': hard_floor,
        'operating_buffer_usd': operating_buffer,
        'base_capital_usd': acc.balance,
        'equity_usd': acc.equity,
        'hard_floor_cushion_usd': acc.equity - hard_floor,
        'operating_buffer_cushion_usd': acc.equity - operating_buffer,
        'capital_mode': 'TIER_0_DEFENSIVE',
        'risk_min_usd': 10.0,
        'risk_max_usd': 10.0,
        'nominal_risk_capacity_usd': 0.0,
        'max_concurrent_tickets': 4,
        'new_risk_admissible': False,
        'admission_scope': 'CAPITAL_ONLY_REQUIRES_ALL_HARD_GATES_AND_BROKER_CHECK'
    }
    
    with open(envelope_file, 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=2)

    print("Updated cycle_envelope.json for Cycle_025! Equity:", acc.equity)
    mt5.shutdown()

if __name__ == '__main__':
    update_envelope()
