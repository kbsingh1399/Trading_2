"""Read-only Cycle 102 evidence extraction; no execution or admission code.
Run: python docs/trade_plans/audits/cycle102_audit.py SNAPSHOT OUTPUT_JSON
Use snapshot from Git commit 30b7b0dfc5dcda9e4ed3ccce62956fe19c507ff3.
All recursive nodes are visited. Hashes/array diagnostics are not a claim of
manual sentence-by-sentence reading. EMA20/50 use first-close recursive seeds;
96 HTF bars cannot certify a warmed EMA200. Spot basis is not a median.
"""
import collections
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

EXPECTED = '8d668c7da4b24231853ca804213fad68'
SOURCES = ['docs/specs/TRADE_DECISION_PLAYBOOK.md',
           'docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md',
           '.agents/rules/ACTIVE_CONTEXT.md', '.agents/memory/session_chat_history.md',
           '.agent/skills/arena/SKILL.md', '.agent/skills/arena/rubric.md']


def inventory(value):
    counts = collections.Counter()
    def visit(v):
        counts[type(v).__name__] += 1
        if isinstance(v, dict):
            for child in v.values():
                visit(child)
        elif isinstance(v, list):
            for child in v:
                visit(child)
    visit(value)
    return {'nodes': sum(counts.values()), 'types': dict(counts)}


def digest(raw):
    return {'bytes': len(raw), 'lines': len(raw.splitlines()),
            'sha256': hashlib.sha256(raw).hexdigest()}


def ema(values, period):
    result = values[0]
    for value in values[1:]:
        result += 2 / (period + 1) * (value - result)
    return result


def cvd_windows(rows, cutoff):
    # Anchor at root's last completed UTC minute, not arbitrary last N rows.
    end = int(cutoff // 60) * 60
    result = {}
    for n in (5, 15, 30):
        selected = [r for r in rows if end - n * 60 <= r['ts'] < end]
        expected = list(range(end - n * 60, end, 60))
        total = sum(r['taker_buy_usd'] + r['taker_sell_usd'] for r in selected)
        result[str(n)] = {'start_epoch': end - n * 60, 'end_epoch': end,
            'observed': len(selected), 'expected': n,
            'complete': sorted(r['ts'] for r in selected) == expected,
            'delta_usd': round(sum(r['cvd_delta_usd'] for r in selected), 2),
            'taker_buy_ratio': sum(r['taker_buy_usd'] for r in selected) / total if total else None}
    return result


def extract(path):
    raw = Path(path).read_bytes()
    d = json.loads(raw)
    if d['generation_id'] != EXPECTED:
        raise ValueError('Wrong generation: do not mix snapshots')
    assert len(d['assets_matrix_24']) == 24
    result = {'source_commit': '30b7b0dfc5dcda9e4ed3ccce62956fe19c507ff3',
              'source': digest(raw), 'tree_inventory': inventory(d),
              'context_manifest_pre_append': {p: digest(Path(p).read_bytes()) for p in SOURCES},
              'root': {k: v for k, v in d.items() if k != 'assets_matrix_24'},
              'assets': {}}
    for symbol, a in d['assets_matrix_24'].items():
        entry = {'block_inventory': {k: inventory(v) for k, v in a.items()},
                 'source_blocks': {k: v for k, v in a.items() if 'ohlcv' not in k},
                 'bar_audit': {}, 'htf_diagnostics': {}}
        for key, rows in a.items():
            if 'ohlcv' not in key:
                continue
            if not rows:
                entry['bar_audit'][key] = {'count': 0, 'available': False}
                continue
            times = [r['ts'] for r in rows]
            entry['bar_audit'][key] = {'count': len(rows), 'available': True,
                'strictly_increasing': all(x < y for x, y in zip(times, times[1:])),
                'ohlc_invalid': sum(not (r['low'] <= min(r['open'], r['close']) <=
                    max(r['open'], r['close']) <= r['high']) for r in rows),
                'explicit_close_after_cutoff': sum(r.get('close_ts', 0) > d['candle_cutoff_epoch'] for r in rows),
                'missing_close_ts': sum('close_ts' not in r for r in rows),
                'first': rows[0], 'last_three': rows[-3:],
                'sha256': hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()}
        for tf in ('1h', '4h'):
            values = [r['close'] for r in a['htf_' + tf + '_ohlcv']]
            e20, e50 = ema(values, 20), ema(values, 50)
            entry['htf_diagnostics'][tf] = {'close': values[-1], 'ema20_seeded': e20,
                'ema50_seeded': e50, 'n': len(values), 'warmed_ema200_verified': False,
                'alignment': 'BEAR' if values[-1] < e20 < e50 else
                             'BULL' if values[-1] > e20 > e50 else 'MIXED'}
        entry['cvd_windows'] = cvd_windows(a.get('cvd_1m_buckets') or [], d['as_of_epoch'])
        b = a['orderbook_live_depth']
        walls = b.get('whale_walls_l3') or []
        aged = [w for w in walls if w.get('persist_s', 0) >= 180]
        entry['wall_diagnostics'] = {'total': len(walls), 'duration_ge180': len(aged),
            'note': 'Duration-qualified receipt recurrence is not full L3 continuity.',
            'statuses': dict(collections.Counter(w.get('persistence_status') for w in walls)),
            'duration_ge180_max_notional_by_side': {side: max(
                [w['notional_usd'] for w in aged if w['side'] == side], default=0)
                for side in ('BUY', 'SELL')}}
        q = a['quotes']; spec = a['execution_specs']
        hl = (b.get('venue_basis') or {}).get('HYPERLIQUID', {}).get('mid')
        entry['spot_hyperliquid_basis_estimate'] = q['mid'] - hl if hl is not None else None
        entry['zero_serialized_spread_positive_bps'] = q['spread_price'] == 0 and q['spread_bps'] > 0
        conv = 1 / q['mid'] if symbol == 'USDJPY' else 1
        entry['minimum_lot_spread_cost_usd_estimate'] = None if entry['zero_serialized_spread_positive_bps'] else q['spread_price'] * spec['contract_size'] * spec['min_lot'] * conv
        entry['ema20_distance_atr'] = abs(q['mid'] - a['causal_indicators']['ema_20']) / a['causal_indicators']['atr_14']
        result['assets'][symbol] = entry
    capital = Decimal('4859.55'); risk = Decimal('14.50')
    stress = Decimal('1.25') * risk + Decimal('2.00')
    result['risk_math'] = {'stress_per_max_risk_ticket': str(stress),
        'three_ticket_equity': str(capital - 3 * stress),
        'four_ticket_equity': str(capital - 4 * stress),
        'four_ticket_equal_nominal_ceiling': str(((capital - Decimal('4795')) - 8) / 5),
        'warning': 'Modeled stress, not guaranteed realized equity. Operator cap retained: three new tickets.'}
    assert result['risk_math']['stress_per_max_risk_ticket'] == '20.1250'
    assert not d['active_positions'] and not d['pending_orders']
    assert all(r['bar_audit']['htf_1h_ohlcv']['count'] == 96 for r in result['assets'].values())
    assert all(r['bar_audit']['htf_4h_ohlcv']['count'] == 96 for r in result['assets'].values())
    assert all(w['complete'] for a in result['assets'].values()
               if a['source_blocks']['category'] == 'CRYPTO' for w in a['cvd_windows'].values())
    # Keep reproducible diagnostics, not a second multi-megabyte market archive.
    def array_summary(rows):
        return {'count': len(rows), 'inventory': inventory(rows),
                'sha256': hashlib.sha256(json.dumps(rows, sort_keys=True).encode()).hexdigest()}
    flow = result['root']['hyperdash_flow_intelligence']
    for key, value in list(flow.items()):
        if isinstance(value, list):
            flow[key] = array_summary(value)
    for entry in result['assets'].values():
        blocks = entry['source_blocks']
        book = blocks['orderbook_live_depth']
        walls = book.get('whale_walls_l3') or []
        book['whale_walls_l3_audit'] = {
            **array_summary(walls),
            'all_observations_ge500k': [w for w in walls if w['notional_usd'] >= 500000]}
        book.pop('whale_walls_l3', None)
        for name in ('structural_stop_clusters', 'reconstructed_liquidations'):
            for key, value in list((blocks.get(name) or {}).items()):
                if isinstance(value, list) and 'whale' in key:
                    blocks[name][key] = array_summary(value)
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    result = extract(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'generation': result['root']['generation_id'],
        'nodes': result['tree_inventory']['nodes'], 'assets': len(result['assets']),
        'source': result['source'], 'risk': result['risk_math']}, indent=2))
