"""Read-only evidence audit, no broker/admission actions.
Usage: python cycle103_audit.py CANONICAL_SOURCE_DIRECTORY OUTPUT_JSON
The source directory contains repository paths retrieved from main's pinned
commits. Telemetry must be the exact Cycle 103 generation, not moving latest.
Large arrays are traversed in full, hashed and summarized rather than archived
again. Seeded HTF EMA20/50 diagnostics do not certify a warmed HTF EMA200.
"""
from collections import Counter
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

GENERATION = '9143e31d1f174e18b547aec55b927787'
SNAPSHOT_COMMIT = '7b001cb761276a0590416f3a64f0f545dfca4b5a'
CONTEXT_COMMIT = '4c42cb1dbb9ebb80021297e22255f18374f26b4a'
PATHS = ['docs/telemetry/live_snapshot_latest.json',
         'docs/specs/TRADE_DECISION_PLAYBOOK.md',
         'docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md',
         '.agents/rules/ACTIVE_CONTEXT.md', '.agents/memory/session_chat_history.md',
         '.agent/skills/arena/SKILL.md', '.agent/skills/arena/rubric.md']


def inventory(value):
    counts = Counter()
    def walk(v):
        counts[type(v).__name__] += 1
        if isinstance(v, dict):
            for child in v.values():
                walk(child)
        elif isinstance(v, list):
            for child in v:
                walk(child)
    walk(value)
    return {'nodes': sum(counts.values()), 'types': dict(counts)}


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def compact(value):
    if isinstance(value, dict):
        return {k: compact(v) for k, v in value.items()}
    if isinstance(value, list):
        return {'count': len(value), 'sha256': sha(value), 'inventory': inventory(value)}
    return value


def ema(xs, n):
    v = xs[0]
    for x in xs[1:]:
        v += 2 / (n + 1) * (x - v)
    return v


def window(rows, end, n):
    selected = [r for r in rows if end - n * 60 <= r['ts'] < end]
    expected = list(range(end - n * 60, end, 60))
    vol = sum(r['taker_buy_usd'] + r['taker_sell_usd'] for r in selected)
    return {'start': end - n * 60, 'end': end, 'n': len(selected), 'expected_n': n,
            'complete': sorted(r['ts'] for r in selected) == expected,
            'delta_usd': round(sum(r['cvd_delta_usd'] for r in selected), 2),
            'buy_ratio': sum(r['taker_buy_usd'] for r in selected) / vol if vol else None}


def wall_key(w):
    # Snapshot dedup diagnostic only; without order IDs identical orders may
    # represent duplicates or multiple orders, so exact queue identity is unknown.
    return tuple(w.get(k) for k in ('address', 'side', 'price', 'size', 'notional_usd'))


def epoch(text):
    return datetime.strptime(text, '%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc).timestamp()


def contains(price, bands, basis):
    return [b for b in bands if b['min_price'] + basis <= price <= b['max_price'] + basis]


def extract(source):
    source = Path(source)
    manifest = {}
    for p in PATHS:
        raw = (source / p).read_bytes()
        manifest[p] = {'commit': SNAPSHOT_COMMIT if p.endswith('.json') else CONTEXT_COMMIT,
                       'bytes': len(raw), 'lines': len(raw.splitlines()),
                       'sha256': hashlib.sha256(raw).hexdigest()}
    d = json.loads((source / PATHS[0]).read_bytes())
    if d['generation_id'] != GENERATION:
        raise ValueError('Wrong Cycle 103 generation')
    result = {'generation': GENERATION, 'manifest': manifest, 'tree': inventory(d),
              'root': {k: compact(v) for k, v in d.items() if k != 'assets_matrix_24'},
              'assets': {}}
    end = int(d['as_of_epoch'] // 60) * 60
    for s, a in d['assets_matrix_24'].items():
        q, c, book = a['quotes'], a['causal_indicators'], a['orderbook_live_depth']
        e = {'source_blocks': compact(a), 'block_inventory': {k: inventory(v) for k, v in a.items()},
             'bars': {}, 'htf': {}}
        for k, bars in a.items():
            if 'ohlcv' not in k or not bars:
                continue
            e['bars'][k] = {'n': len(bars), 'sha256': sha(bars),
                'nonmonotonic': sum(x['ts'] >= y['ts'] for x, y in zip(bars, bars[1:])),
                'invalid_ohlc': sum(not r['low'] <= min(r['open'], r['close']) <= max(r['open'], r['close']) <= r['high'] for r in bars),
                'close_after_cutoff': sum(r.get('close_ts', 0) > d['candle_cutoff_epoch'] for r in bars),
                'missing_close_ts': sum('close_ts' not in r for r in bars),
                'last_five': bars[-5:]}
        for tf in ('1h', '4h'):
            xs = [r['close'] for r in a['htf_' + tf + '_ohlcv']]
            e20, e50 = ema(xs, 20), ema(xs, 50)
            e['htf'][tf] = {'n': len(xs), 'close': xs[-1], 'ema20_seeded': e20,
                'ema50_seeded': e50, 'warmed_ema200_verified': False,
                'ordering': 'BEAR' if xs[-1] < e20 < e50 else 'BULL' if xs[-1] > e20 > e50 else 'MIXED'}
        rows = a.get('cvd_1m_buckets') or []
        e['cvd_windows'] = {str(n): window(rows, end, n) for n in (1, 5, 15, 30)}
        e['preceding_5m'] = window(rows, end - 300, 5)
        walls = book.get('whale_walls_l3') or []
        aged = [w for w in walls if w.get('persist_s', 0) >= 180]
        e['walls'] = {'count': len(walls), 'age180_count': len(aged),
            'status_counts': dict(Counter(w.get('persistence_status') for w in walls)),
            'duplicate_signature_excess': len(walls) - len(set(wall_key(w) for w in walls)),
            'age180_max_by_side': {side: max([w['notional_usd'] for w in aged if w['side'] == side], default=0) for side in ('BUY', 'SELL')},
            'all_ge500k': [w for w in walls if w['notional_usd'] >= 500000]}
        e['l2_walls'] = book.get('l2_wall_levels') or []
        e['book_ladders'] = {k: book.get(k) for k in ('bids_top20', 'asks_top20')}
        hl = (book.get('venue_basis') or {}).get('HYPERLIQUID') or {}
        e['basis'] = {'median': hl.get('basis_median'),
                      'spot': q['mid'] - hl['mid'] if hl.get('mid') is not None else None}
        e['bands'] = {block: {k: v for k, v in (a.get(block) or {}).items()
                             if k.startswith(('nearest_', 'top_')) and 'whale' not in k}
                      for block in ('structural_stop_clusters', 'reconstructed_liquidations')}
        raw_spread = q['ask'] - q['bid']
        implied_bps = raw_spread / q['mid'] * 10000
        e['quote_precision'] = {'bid_ask_difference': raw_spread,
                               'implied_bps': implied_bps,
                               'bps_error': implied_bps - q['spread_bps']}
        e['ema20_distance_atr'] = abs(q['mid'] - c['ema_20']) / c['atr_14']
        specs = a['execution_specs']
        e['serialized_min_lot_spread_usd'] = q['spread_price'] * specs['contract_size'] * specs['min_lot'] / (q['mid'] if s == 'USDJPY' else 1)
        if s in ('EURUSD', 'GBPUSD'):
            e['serialized_min_lot_spread_usd'] = None  # Both lose broker-native precision.
        result['assets'][s] = e
    geometry = {}
    # Counterexamples only. These are NOT executable order cards.
    for s, raw_entry, raw_edge in [('BTC', 82127., 82200.), ('ETH', 2459.3, 2460.),
                                    ('SP500', 7717.3, 7720.), ('NAS100', 30060., 30100.)]:
        a = result['assets'][s]; blocks = a['source_blocks']; basis = a['basis']['median']
        entry = raw_entry + basis
        stop = raw_edge + basis + .5 * blocks['causal_indicators']['atr_14'] + blocks['quotes']['spread_price'] / 2
        band_rows = a['bands']['structural_stop_clusters']['nearest_buy_stop_clusters_above']
        geometry[s] = {'hypothetical_entry': entry, 'hypothetical_stop': stop,
                       'distance': stop - entry, 'friction_fraction': blocks['quotes']['spread_price'] / (stop - entry),
                       'stop_contained_raw_intervals': contains(stop, band_rows, basis)}
    a = result['assets']['USWTI']; basis = a['basis']['median']; blocks = a['source_blocks']
    stop = 93.8 + basis - .5 * blocks['causal_indicators']['atr_14'] - blocks['quotes']['spread_price'] / 2
    geometry['USWTI'] = {'hypothetical_ema50_entry': blocks['causal_indicators']['ema_50'],
                         'hypothetical_stop': stop, 'primary_bid_mapped': 93.58 + basis,
                         'stop_contained_raw_intervals': contains(stop, a['bands']['structural_stop_clusters']['nearest_sell_stop_clusters_below'], basis)}
    result['geometry_counterexamples'] = geometry
    result['risk_math'] = {str(n): str(Decimal('4859.55') - n * (Decimal('1.25') * Decimal('14.50') + Decimal('2'))) for n in (0, 3, 4)}
    result['global_flow_seconds_after_root'] = d['hyperdash_flow_intelligence']['as_of_epoch'] - d['as_of_epoch']
    return result


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    result = extract(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'generation': result['generation'], 'nodes': result['tree']['nodes'],
                      'assets': len(result['assets']), 'risk': result['risk_math']}, indent=2))
