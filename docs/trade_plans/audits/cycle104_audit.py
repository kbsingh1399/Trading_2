"""Read-only Cycle 104 audit. No admission engine, broker or network calls.
Usage: python cycle104_audit.py PINNED_MAIN_SOURCE_DIRECTORY OUTPUT_JSON
"""
import hashlib
import json
from pathlib import Path
import sys
import cycle103_audit as base

GENERATION = '8d5df9f2469d485bb7fefb740fb44ccf'
COMMIT = 'd06acd0739b3e0eb9b63c8f835937830f103d060'
SOURCE_HASHES = dict(zip(base.PATHS, (
    '90b05663639e48ad97f4cea1749e44130b630f45c69217e9321596011d835108',
    '48d64f5ee1e00f91672120bb53d6252d1eed6df80793768e4e46d9577b86187e',
    '792b0aee87c26c8f0470ecbdc49d58b2df2e2f320b5af6df4f43560359ab6007',
    '1a5f24f9ff00a9b2922dd66cb2fcb854557e0d121d6cfb3b452e9337f4f9f5d2',
    '0c9411d88dc108103b839e49e8c5f18f1c5f5ff54f4f13b1e4675263080dddd2',
    'c06f9828566485d5bd6507150f454d6f37d49c2b02e5308b8f744a4a046bdf39',
    '3296801e01035f3ad8dc2b57f0c47d84d296bbc716bf8b36bdb02b426c2735a5',
)))
# Explicit analyst classifications, NOT an automated decision-gate result.
WATCHES = ('BTC', 'ETH', 'SP500', 'GOLD', 'USWTI')


def all_bands(asset):
    """Deduplicate display intervals, retaining source and magnitude references."""
    result = {}
    for source, block in asset['bands'].items():
        for name, rows in block.items():
            for row in rows:
                key = (row['min_price'], row['max_price'])
                r = result.setdefault(key, {'min_price': key[0], 'max_price': key[1], 'sources': []})
                item = {'block': source, 'notional_usd': row['notional_usd']}
                if item not in r['sources']:
                    r['sources'].append(item)
    return sorted(result.values(), key=lambda b: b['min_price'])


def extract(source):
    for path, expected in SOURCE_HASHES.items():
        if hashlib.sha256((Path(source) / path).read_bytes()).hexdigest() != expected:
            raise ValueError('Pinned source hash mismatch: ' + path)
    e = base.extract(source, expected_generation=GENERATION, snapshot_commit=COMMIT,
                     context_commit=COMMIT, include_cycle103_geometry=False)
    d = json.loads((Path(source) / base.PATHS[0]).read_bytes())
    for s, a in e['assets'].items():
        b = a['source_blocks']; q = b['quotes']; atr = b['causal_indicators']['atr_14']
        basis = a['basis']['median']
        a['analyst_classification'] = 'WATCHLIST' if s in WATCHES else 'NO SETUP'
        a['all_unique_band_intervals'] = all_bands(a)
        a['aged_l3_nearby'] = [w for w in d['assets_matrix_24'][s]['orderbook_live_depth'].get('whale_walls_l3', [])
                             if basis is not None and w.get('persist_s', 0) >= 180
                             and abs(w['price'] + basis - q['mid']) <= 2 * atr]
    cases = {}
    for name, symbol, raw_entry, raw_edge, raw_target in (
            ('BTC_primary', 'BTC', 81904., 82000., 81500.),
            ('ETH_primary', 'ETH', 2446.1, 2460., 2420.),
            ('SOL_primary', 'SOL', 105.95, 106., 104.),
            ('SP500_near', 'SP500', 7710.4, 7720., 7700.),
            ('SP500_deep', 'SP500', 7732.8, 7740., 7700.),
            ('NAS100_subthreshold_pocket', 'NAS100', 29960., 30000., 29900.)):
        a = e['assets'][symbol]; b = a['source_blocks']; basis = a['basis']['median']
        atr = b['causal_indicators']['atr_14']; spread = b['quotes']['spread_price']
        entry = raw_entry + basis
        stop = raw_edge + basis + .5 * atr + spread / 2
        target = (raw_target + basis) * 1.0005
        walls = [w for w in d['assets_matrix_24'][symbol]['orderbook_live_depth']['whale_walls_l3']
                 if w['side'] == 'SELL' and w['price'] == raw_entry and w.get('persist_s', 0) >= 180]
        first = min(base.epoch(w['first_seen_utc']) for w in walls)
        bars = a['bars']['bars_15m_ohlcv']['last_five']
        cases[name] = {'symbol': symbol, 'research_entry': entry, 'research_stop': stop,
            'research_target_5bps': target, 'gross_R': (entry - target) / (stop - entry),
            'friction_fraction': spread / (stop - entry),
            'contained_raw_bands': base.contains(stop, a['all_unique_band_intervals'], basis),
            'walls_at_raw_entry': walls,
            'first_seen_after_last_completed_bar': first > bars[-1]['close_ts'],
            'completed_bars_overlapping_first_observation_or_later': [r for r in bars if r['close_ts'] > first],
            'entry_distance_atr': abs(entry - b['quotes']['mid']) / atr,
            'index_total_distance_minimum': 1.5 * atr if b['category'] == 'INDICES' else None,
            'friction_minimum_stop_distance': spread / .15,
            'R_upper_bound_at_friction_minimum_to_selected_target': (entry - target) / (spread / .15)}
    a = e['assets']['USWTI']; b = a['source_blocks']; basis = a['basis']['median']
    spread = b['quotes']['spread_price']; atr = b['causal_indicators']['atr_14']
    wall = 93.58 + basis
    entry = wall + spread / 2  # Diagnostic long entry above protective bid.
    stop = 93.5 + basis - .5 * atr - spread / 2
    first_target = (93.8 + basis) * .9995
    poc_target = b['volume_profile']['poc'] * .9995
    cases['USWTI_primary'] = {'symbol': 'USWTI', 'primary_bid_mapped': wall,
        'research_entry': entry, 'research_stop': stop,
        'friction_fraction': spread / (entry - stop),
        'contained_raw_bands': base.contains(stop, a['all_unique_band_intervals'], basis),
        'entry_distance_atr': abs(entry - b['quotes']['mid']) / atr,
        'last_completed_bar_low': a['bars']['bars_15m_ohlcv']['last_five'][-1]['low'],
        'first_small_pool_target': first_target, 'first_small_pool_gross_R': (first_target - entry) / (entry - stop),
        'POC_target_5bps': poc_target, 'POC_gross_R': (poc_target - entry) / (entry - stop)}
    e['cycle104_research_counterexamples'] = cases
    e['inventory_baseline_verified'] = e['root']['active_positions']['count'] == 0 and e['root']['pending_orders']['count'] == 0 and e['root']['account']['balance_usd'] == e['root']['account']['equity_usd'] == 4859.55
    if not e['inventory_baseline_verified']:
        raise ValueError('Pinned risk calculation does not match account/inventory')
    return e


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    e = extract(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(e, indent=2) + '\n')
    print(json.dumps({'generation': e['generation'], 'nodes': e['tree']['nodes'],
                      'assets': len(e['assets']), 'watches': WATCHES, 'risk_math': e['risk_math']}, indent=2))
