"""Pinned post-Cycle-103 refresh; read-only, no execution.
Usage: python continuation103_audit.py SOURCE_DIRECTORY OUTPUT_JSON
All sources are from canonical main commit 6ea58c54cb2bca51a6002cd33ac7f57de1256d67.
"""
import hashlib
import json
from pathlib import Path
import sys
import cycle103_audit as base

GENERATION = 'edacf075b6e24de4a3c95dd1b61971db'
COMMIT = '6ea58c54cb2bca51a6002cd33ac7f57de1256d67'


SOURCE_HASHES = dict(zip(base.PATHS, (
    '8cede55b84df5316f7d2992f1efad55e74d1ce5ccf23cf15e88ed5c2d3978c08',
    '48d64f5ee1e00f91672120bb53d6252d1eed6df80793768e4e46d9577b86187e',
    '792b0aee87c26c8f0470ecbdc49d58b2df2e2f320b5af6df4f43560359ab6007',
    '1a5f24f9ff00a9b2922dd66cb2fcb854557e0d121d6cfb3b452e9337f4f9f5d2',
    '0c9411d88dc108103b839e49e8c5f18f1c5f5ff54f4f13b1e4675263080dddd2',
    'c06f9828566485d5bd6507150f454d6f37d49c2b02e5308b8f744a4a046bdf39',
    '3296801e01035f3ad8dc2b57f0c47d84d296bbc716bf8b36bdb02b426c2735a5',
)))


def extract(source):
    for path, expected in SOURCE_HASHES.items():
        if hashlib.sha256((Path(source) / path).read_bytes()).hexdigest() != expected:
            raise ValueError('Pinned source hash mismatch: ' + path)
    e = base.extract(source, expected_generation=GENERATION,
                     snapshot_commit=COMMIT, context_commit=COMMIT,
                     include_cycle103_geometry=False)
    cases = {}
    # Illustrative failed geometry only, not executable order cards.
    for symbol, raw_entry, raw_edge, target_edge in (
            ('BTC', 81904., 82000., 81600.),
            ('ETH', 2446.1, 2460., 2420.),
            ('SP500', 7712.9, 7720., 7700.),
            ('NAS100', 30081., 30100., 29900.)):
        a = e['assets'][symbol]; b = a['source_blocks']; basis = a['basis']['median']
        atr = b['causal_indicators']['atr_14']; spread = b['quotes']['spread_price']
        entry = raw_entry + basis
        stop = raw_edge + basis + .5 * atr + spread / 2
        target = (target_edge + basis) * 1.0005
        walls = a['walls']['all_ge500k']
        w = next(w for w in walls if w['side'] == 'SELL' and w['price'] == raw_entry)
        last_bars = a['bars']['bars_15m_ohlcv']['last_five']
        cases[symbol] = {'research_entry': entry, 'research_stop': stop,
            'research_target_5bps': target, 'gross_R': (entry - target) / (stop - entry),
            'friction_fraction': spread / (stop - entry),
            'contained_raw_bands': base.contains(stop, a['bands']['structural_stop_clusters']['nearest_buy_stop_clusters_above'], basis),
            'primary_wall': w,
            'first_seen_after_last_completed_bar': base.epoch(w['first_seen_utc']) > last_bars[-1]['close_ts'],
            'completed_bars_overlapping_or_after_first_seen': [r for r in last_bars if r['close_ts'] > base.epoch(w['first_seen_utc'])],
            'entry_distance_atr': abs(entry - b['quotes']['mid']) / atr}
    a = e['assets']['USWTI']; b = a['source_blocks']; basis = a['basis']['median']
    entry = 93.58 + basis
    stop = 93.5 + basis - .5 * b['causal_indicators']['atr_14'] - b['quotes']['spread_price'] / 2
    cases['USWTI'] = {'research_entry': entry, 'research_stop': stop,
        'friction_fraction': b['quotes']['spread_price'] / (entry - stop),
        'contained_raw_bands': base.contains(stop, a['bands']['structural_stop_clusters']['nearest_sell_stop_clusters_below'], basis),
        'entry_distance_atr': abs(entry - b['quotes']['mid']) / b['causal_indicators']['atr_14']}
    e['refresh_geometry_counterexamples'] = cases
    e['inventory_baseline_verified'] = e['root']['active_positions']['count'] == 0 and e['root']['pending_orders']['count'] == 0 and e['root']['account']['balance_usd'] == e['root']['account']['equity_usd'] == 4859.55
    if not e['inventory_baseline_verified']:
        raise ValueError('Pinned risk scenario does not match observed inventory/account')
    return e


if __name__ == '__main__':
    if len(sys.argv) != 3:
        raise SystemExit(__doc__)
    e = extract(sys.argv[1])
    Path(sys.argv[2]).write_text(json.dumps(e, indent=2) + '\n')
    print(json.dumps({'generation': e['generation'], 'nodes': e['tree']['nodes'],
                      'assets': len(e['assets']), 'risk_math': e['risk_math']}, indent=2))
