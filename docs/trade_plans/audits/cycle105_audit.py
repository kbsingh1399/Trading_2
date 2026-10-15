"""Read-only Cycle 105 source and calculation audit; no admission/broker calls.
Usage: python cycle105_audit.py PINNED_SOURCE_DIRECTORY OUTPUT_JSON
"""
import hashlib
import json
from pathlib import Path
import sys
import cycle103_audit as base
from cycle104_audit import all_bands

GENERATION = 'd14b626dfa5a47e0a641b86f6ba49dd0'
COMMIT = '82d50427c41ddbd8cbe21c605108bf05af7de229'
SOURCE_HASHES = dict(zip(base.PATHS, (
    'fa65b3ab5f948c093996d2ac6cc5fad5114229e2e5e357f350b52c41e2d45048',
    '48d64f5ee1e00f91672120bb53d6252d1eed6df80793768e4e46d9577b86187e',
    '792b0aee87c26c8f0470ecbdc49d58b2df2e2f320b5af6df4f43560359ab6007',
    '1a5f24f9ff00a9b2922dd66cb2fcb854557e0d121d6cfb3b452e9337f4f9f5d2',
    '7e18eb88049003a78d3001845e695895afc0a40c3e8c5032d87e445b2a71e3bb',
    'c06f9828566485d5bd6507150f454d6f37d49c2b02e5308b8f744a4a046bdf39',
    '3296801e01035f3ad8dc2b57f0c47d84d296bbc716bf8b36bdb02b426c2735a5',
)))
# Analyst research classifications; these are not automated admission decisions.
WATCHES = ('BTC', 'ETH', 'SP500', 'NAS100', 'GOLD', 'USWTI')


def extract(source):
    for path, expected in SOURCE_HASHES.items():
        if hashlib.sha256((Path(source) / path).read_bytes()).hexdigest() != expected:
            raise ValueError('Pinned source hash mismatch: ' + path)
    e = base.extract(source, expected_generation=GENERATION, snapshot_commit=COMMIT,
                     context_commit=COMMIT, include_cycle103_geometry=False)
    d = json.loads((Path(source) / base.PATHS[0]).read_bytes())
    cutoff = int(d['generation_started_at_epoch'] // 60) * 60
    for s, a in e['assets'].items():
        raw = d['assets_matrix_24'][s]
        walls = raw['orderbook_live_depth'].get('whale_walls_l3', [])
        a['all_unique_band_intervals'] = all_bands(a)
        a['analyst_classification'] = 'WATCHLIST' if s in WATCHES else 'NO SETUP'
        a['cvd_generation_cutoff_windows'] = {str(n): base.window(raw.get('cvd_1m_buckets') or [], cutoff, n) for n in (1, 5, 15, 30)}
        a['wall_persistence_diagnostics'] = {
            'max_recorded_persist_s': max((w['persist_s'] for w in walls), default=0),
            'max_samples': max((w['samples'] for w in walls), default=0),
            'earliest_first_seen': min((w['first_seen_utc'] for w in walls), default=None),
            'latest_first_seen': max((w['first_seen_utc'] for w in walls), default=None),
            'max_observed_at': max((w['observed_at'] for w in walls), default=None),
            'all_first_seen_after_last_completed_candle': bool(walls) and all(base.epoch(w['first_seen_utc']) > a['bars']['bars_15m_ohlcv']['last_five'][-1]['close_ts'] for w in walls)}
    cases = {}
    # No case below is executable: chronology, persistence and interval failures
    # are retained rather than silently importing an older generation's history.
    for name, symbol, raw_entry, edge, target_edge in (
            ('BTC_primary', 'BTC', 82166., 82200., 81600.),
            ('ETH_primary', 'ETH', 2450.3, 2460., 2420.),
            ('SOL_primary', 'SOL', 105.94, 106., 104.),
            ('SP500_near_subthreshold', 'SP500', 7724.6, 7730., 7700.),
            ('SP500_primary', 'SP500', 7741.4, 7750., 7700.),
            ('NAS100_near', 'NAS100', 30020., 30100., 29900.),
            ('NAS100_deep', 'NAS100', 30080., 30100., 29900.),
            ('GOLD_primary', 'GOLD', 4127.8, 4130., 4080.)):
        a = e['assets'][symbol]; b = a['source_blocks']; basis = a['basis']['median']
        atr = b['causal_indicators']['atr_14']; spread = b['quotes']['spread_price']
        entry = raw_entry + basis; stop = edge + basis + .5 * atr + spread / 2
        target = (target_edge + basis) * 1.0005
        walls = [w for w in d['assets_matrix_24'][symbol]['orderbook_live_depth']['whale_walls_l3'] if w['side'] == 'SELL' and w['price'] == raw_entry]
        cases[name] = {'symbol': symbol, 'research_entry': entry, 'research_stop': stop,
            'research_target_5bps': target, 'gross_R': (entry-target)/(stop-entry),
            'friction_fraction': spread/(stop-entry), 'walls': walls,
            'contained_raw_bands': base.contains(stop, a['all_unique_band_intervals'], basis),
            'entry_distance_atr': abs(entry-b['quotes']['mid'])/atr,
            'index_minimum_distance': 1.5*atr if b['category']=='INDICES' else None,
            'R_ceiling_at_friction_minimum_to_selected_target': (entry-target)/(spread/.15)}
    a=e['assets']['USWTI']; b=a['source_blocks']; basis=a['basis']['median']; spread=b['quotes']['spread_price']; atr=b['causal_indicators']['atr_14']
    wall=93.58+basis; entry=wall+spread/2; stop=93.5+basis-.5*atr-spread/2
    target=b['volume_profile']['poc']*.9995
    cases['USWTI_primary']={'symbol':'USWTI','mapped_bid':wall,'research_entry':entry,'research_stop':stop,
        'research_target_5bps':target,'gross_R':(target-entry)/(entry-stop),
        'friction_fraction':spread/(entry-stop),'contained_raw_bands':base.contains(stop,a['all_unique_band_intervals'],basis),
        'entry_distance_atr':abs(entry-b['quotes']['mid'])/atr,
        'last_completed_low':a['bars']['bars_15m_ohlcv']['last_five'][-1]['low']}
    e['cycle105_counterexamples']=cases
    e['inventory_baseline_verified']=not d['active_positions'] and not d['pending_orders'] and d['account']['balance_usd']==d['account']['equity_usd']==4859.55
    if not e['inventory_baseline_verified']:
        raise ValueError('Pinned risk scenario differs from account/inventory')
    return e


if __name__=='__main__':
    if len(sys.argv)!=3:
        raise SystemExit(__doc__)
    e=extract(sys.argv[1]);Path(sys.argv[2]).write_text(json.dumps(e,indent=2)+'\n')
    print(json.dumps({'generation':e['generation'],'nodes':e['tree']['nodes'],'watches':WATCHES},indent=2))
