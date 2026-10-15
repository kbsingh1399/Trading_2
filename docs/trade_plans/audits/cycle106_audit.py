"""Cycle 106 pinned-source research audit; no broker/admission mutations.
Usage: python cycle106_audit.py SOURCE_DIRECTORY ADJACENT_SNAPSHOT OUTPUT_JSON
The earlier published evidence is a guarded comparison receipt, not inherited
wall age. Analyst watch classifications are not automated order authorization.
"""
import hashlib
import json
from pathlib import Path
import sys

import cycle103_audit as base
from cycle104_audit import all_bands
from cycle105_continuation_audit import SOURCE_HASHES as PRIOR_HASHES, risk_reserve

COMMIT = 'd3020d8a84b577e4288f1683ac0376e2d1baefb8'
GENERATION = 'e13af7f63a4b4473b5f5dc8b5953aca2'
ADJACENT_COMMIT = '846791153d9364118d1e76047b1f70ae13f70459'
ADJACENT_HASH = '7abb22088d2d8c93fe350ae7851e5863738bd6a0e004a56b14ddc337be46ebc4'
PRIOR_EVIDENCE_HASH = '7dfd91c7341fc9672b1d653494204e8ac0d6eb62687255091517c3c3243e90f8'
SOURCE_HASHES = dict(PRIOR_HASHES)
SOURCE_HASHES[base.PATHS[0]] = '81f0f3caee3f7c4e0680992b9ff67a2c6a1e014087e659157a5cffb265b42a68'
WATCHES = ('BTC', 'ETH', 'SP500', 'NAS100', 'GOLD')
REASONS = {
    'BTC': 'Bear/bear; selling returned, but primary asks have only 76.5s recorded span, no current-history completed retest.',
    'ETH': 'Bear/bear; pending DELETE separately. Larger ask now in range but 131.3s only; sweep and friction failures persist.',
    'SOL': 'Bear/bear; 5/15m selling, 30m positive; primary span 73.9s and selected-target friction-minimum R below 2.5.',
    'BNB': 'Bear/bear; no seasoned primary; velocity 1.009 and positive 5/15/30m flow do not confirm seller defense.',
    'XRP': 'Minimum-lot spread cost 3 USD still exceeds 2.175 USD maximum budget; no seasoned defense.',
    'ADA': 'Explicit ban; spread and minimum-lot friction also fail.',
    'DOGE': 'Explicit ban; spread and minimum-lot friction also fail.',
    'TRX': 'Bull/mixed HTF; 9 USD minimum-lot spread cost and no seasoned defense.',
    'DOT': 'Explicit ban; 185.76 bps exceeds crypto cap.',
    'LINK': 'Explicit ban; 69.40 bps exceeds crypto cap.',
    'BCH': 'Bear/bear; no seasoned 5M primary ask or independently verified defended shelf.',
    'LTC': '50.33 bps exceeds crypto cap; minimum-lot spread cost 3 USD exceeds 2.175 USD.',
    'AVAX': 'Spread now 40.36 bps, above 35; no seasoned primary defense.',
    'NEAR': 'Explicit ban; 69 bps, minimum-lot cost and mixed HTF also fail; abs(Z)=1.93 is still below 2.',
    'SP500': 'Bear/mixed HTF; 72.8s primary span, buyer tick flow, latest high below EMA20 and primary; nearby target not payable at 2R.',
    'NAS100': 'Bear/bear; three ask shelves examined, all 131.1s. Near targets fail 2R at index floor; deeper paper reward lacks safe stop/retest.',
    'DJ30': 'Bear/mixed HTF and no seasoned primary defense.',
    'GER40': 'Mixed/bull HTF conflicts with bearish producer regime; no permitted aligned direction confirmed.',
    'GOLD': 'Bear/bear; old 4113.5/4113.8 pair no longer intact, qualifying individual asks only 84.8s; no completed current-history retest.',
    'SILVER': '6.48 bps exceeds TradFi 5 bps cap; no seasoned defense.',
    'USWTI': 'Bull/bull, velocity 0.0306; no seasoned primary, mixed tick flow and fresh support-to-POC friction/reward failure.',
    'EURUSD': 'Bear/bear; no seasoned ask; equal rounded bid/ask and zero price spread conflict with 0.45 bps.',
    'GBPUSD': 'Bear/bear; no seasoned ask; equal rounded bid/ask conflict with nonzero 0.0001 price spread and 0.61 bps.',
    'USDJPY': 'Velocity improved to 0.6154; reject for mixed/bull HTF, bearish producer regime and missing seasoned support, not stale fast-velocity failure.',
}


def checked_bytes(path, expected, label):
    raw = Path(path).read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('Pinned source hash mismatch: ' + label)
    return raw


def persistence(snapshot):
    walls = [w for a in snapshot['assets_matrix_24'].values()
             for w in a['orderbook_live_depth']['whale_walls_l3']]
    l2 = [w for a in snapshot['assets_matrix_24'].values()
          for w in a['orderbook_live_depth']['l2_wall_levels']]
    return {'L3_rows': len(walls), 'L3_age180_rows': sum(w['persist_s'] >= 180 for w in walls),
            'L2_rows': len(l2), 'L2_age180_rows': sum(w['persist_s'] >= 180 for w in l2),
            'max_recorded_span_s': max(w['persist_s'] for w in walls),
            'max_samples': max(w['samples'] for w in walls),
            'earliest_first_seen': min(w['first_seen_utc'] for w in walls),
            'latest_first_seen': max(w['first_seen_utc'] for w in walls)}


def extract(source, adjacent_snapshot):
    source = Path(source)
    for path, expected in SOURCE_HASHES.items():
        checked_bytes(source/path, expected, path)
    adjacent_bytes = checked_bytes(adjacent_snapshot, ADJACENT_HASH, 'adjacent snapshot')
    prior_bytes = checked_bytes(Path(__file__).with_name('CYCLE_105_CONTINUATION_EVIDENCE.json'),
                                PRIOR_EVIDENCE_HASH, 'published preceding audit')
    d = json.loads((source/base.PATHS[0]).read_bytes())
    adjacent = json.loads(adjacent_bytes)
    prior = json.loads(prior_bytes)
    e = base.extract(source, expected_generation=GENERATION, snapshot_commit=COMMIT,
                     context_commit=COMMIT, include_cycle103_geometry=False)
    cutoff = int(d['generation_started_at_epoch']//60)*60
    for symbol, a in e['assets'].items():
        raw = d['assets_matrix_24'][symbol]
        walls = raw['orderbook_live_depth']['whale_walls_l3']
        a['all_unique_band_intervals'] = all_bands(a)
        a['analyst_classification'] = 'WATCHLIST' if symbol in WATCHES else 'NO SETUP'
        a['engine1_assessment'] = 'FAIL: abs(Z) < 2; no invented exhaustion override.'
        a['engine2_assessment'] = REASONS[symbol]
        a['cvd_generation_cutoff_windows'] = {
            str(n): base.window(raw.get('cvd_1m_buckets') or [], cutoff, n) for n in (1, 5, 15, 30)}
        last_close = a['bars']['bars_15m_ohlcv']['last_five'][-1]['close_ts']
        a['wall_timing'] = {'max_recorded_span_s': max((w['persist_s'] for w in walls), default=0),
            'all_first_seen_after_latest_completed_15m_close':
                all(base.epoch(w['first_seen_utc']) > last_close for w in walls),
            'inherited_age_or_producer_gate_used': False}
        old = {base.wall_key(w): w for w in prior['assets'][symbol]['walls']['all_ge500k']}
        matches = [(w, old[base.wall_key(w)]) for w in walls if base.wall_key(w) in old]
        a['cross_audit_exact_large_signature_recurrence'] = {
            'count': len(matches),
            'shorter_reported_span_count': sum(n['persist_s'] < o['persist_s'] for n, o in matches),
            'examples': [{'current': n, 'prior': o} for n, o in matches[:4]],
            'continuous_survival_proven': False}
    e['observed_inventory'] = {k: d[k] for k in ('active_positions', 'pending_orders', 'risk', 'capacity')}
    if d['active_positions'] or len(d['pending_orders']) != 1 or d['pending_orders'][0]['ticket'] != 18925596:
        raise ValueError('Unexpected pinned inventory')
    p = d['pending_orders'][0]
    receipt = d['risk']['tickets'][0]
    if receipt['ticket'] != p['ticket'] or receipt['status'] != 'BROKER_VALUED':
        raise ValueError('Pending receipt mismatch')
    e['risk_math'] = risk_reserve(d['account']['equity_usd'], receipt['nominal_stop_loss_usd'], receipt['margin_on_fill_usd'])
    eth = e['assets']['ETH']; raw_eth = d['assets_matrix_24']['ETH']; basis = eth['basis']['median']
    distance = p['sl']-p['price_open']; spread = raw_eth['quotes']['spread_price']
    bands = base.contains(p['sl'], eth['all_unique_band_intervals'], basis)
    asks = []
    for w in raw_eth['orderbook_live_depth']['whale_walls_l3']:
        if w['side'] == 'SELL' and w['notional_usd'] >= 5e6:
            mapped = w['price']+basis
            location = 'below_entry' if mapped < p['price_open'] else 'beyond_stop' if mapped > p['sl'] else 'between_entry_and_stop'
            asks.append({'wall': w, 'mapped_price': mapped, 'location': location})
    e['pending_review'] = {'ticket': p['ticket'], 'recommendation': 'DELETE', 'executed': False,
        'order': p, 'risk_distance': distance, 'gross_R': (p['price_open']-p['tp'])/distance,
        'friction_fraction': spread/distance, 'minimum_distance_at_15pct_friction': spread/.15,
        'fixed_target_R_ceiling_at_friction_minimum': (p['price_open']-p['tp'])/(spread/.15),
        'contained_raw_bands': bands,
        'contained_mapped_intervals': [[b['min_price']+basis,b['max_price']+basis] for b in bands],
        'large_ask_locations': asks, 'current_ask_below_pending_TP': raw_eth['quotes']['ask'] < p['tp'],
        'pending_is_not_realized_profit': True, 'age_inherited_from_same_wallet': False}
    e['persistence_comparison'] = {
        'current': persistence(d), 'adjacent': persistence(adjacent),
        'adjacent_receipt': {'commit': ADJACENT_COMMIT, 'sha256': ADJACENT_HASH,
                             'generation': adjacent['generation_id'], 'as_of_utc': adjacent['as_of_utc']},
        'published_prior_receipt': {'evidence_sha256': PRIOR_EVIDENCE_HASH, 'generation': prior['generation'],
            'as_of_utc': prior['root']['as_of_utc'],
            'L3_age180_rows': sum(a['walls']['age180_count'] for a in prior['assets'].values())},
        'cause': 'UNKNOWN: observed recurrence-history discontinuity/restart; collector reset versus disappearance/reappearance not established.',
        'liquidity_disappearance_or_spoofing_proven': False}
    cases = {}
    for name, symbol, raw_entry, edge, target_edge in (
        ('BTC_near', 'BTC', 82000., 82100., 81700.),
        ('BTC_primary', 'BTC', 82164., 82200., 81600.),
        ('ETH_in_range_primary', 'ETH', 2452.2, 2460., 2420.),
        ('SOL_primary', 'SOL', 105.94, 106., 104.),
        ('SP500_primary', 'SP500', 7741., 7750., 7720.),
        ('NAS100_nearest', 'NAS100', 29977., 30000., 29900.),
        ('NAS100_primary', 'NAS100', 30039., 30100., 29900.),
        ('NAS100_deep', 'NAS100', 30209., 30200., 29900.),
        ('GOLD_primary', 'GOLD', 4126.1, 4130., 4080.)):
        a = e['assets'][symbol]; b = a['source_blocks']; basis = a['basis']['median']
        atr = b['causal_indicators']['atr_14']; spread = b['quotes']['spread_price']
        entry = raw_entry+basis; stop = edge+basis+.5*atr+spread/2
        target = (target_edge+basis)*1.0005
        index_floor = 1.5*atr if b['category']=='INDICES' else None
        walls = [w for w in d['assets_matrix_24'][symbol]['orderbook_live_depth']['whale_walls_l3']
                 if w['side']=='SELL' and w['price']==raw_entry]
        if not walls:
            raise ValueError('Research wall missing: '+name)
        cases[name] = {'symbol':symbol, 'research_entry':entry, 'research_stop':stop,
            'research_target_5bps':target, 'gross_R':(entry-target)/(stop-entry),
            'friction_fraction':spread/(stop-entry), 'walls':walls,
            'contained_raw_bands':base.contains(stop,a['all_unique_band_intervals'],basis),
            'entry_distance_atr':abs(entry-b['quotes']['mid'])/atr, 'index_minimum_distance':index_floor,
            'gross_R_at_index_minimum':(entry-target)/index_floor if index_floor else None,
            'R_ceiling_at_friction_minimum_to_selected_target':(entry-target)/(spread/.15),
            'executable':False}
    a = e['assets']['USWTI']; b = a['source_blocks']; basis = a['basis']['median']
    atr = b['causal_indicators']['atr_14']; spread = b['quotes']['spread_price']
    wall = next(w for w in d['assets_matrix_24']['USWTI']['orderbook_live_depth']['whale_walls_l3'] if w['side']=='BUY' and w['price']==93.815)
    entry = wall['price']+basis+spread/2; stop = 93.8+basis-.5*atr-spread/2
    target = b['volume_profile']['poc']*.9995
    cases['USWTI_subthreshold'] = {'symbol':'USWTI', 'wall':wall, 'mapped_bid':wall['price']+basis,
        'research_entry':entry, 'research_stop':stop, 'research_target_5bps':target,
        'gross_R':(target-entry)/(entry-stop), 'friction_fraction':spread/(entry-stop),
        'contained_raw_bands':base.contains(stop,a['all_unique_band_intervals'],basis), 'executable':False}
    e['cycle106_counterexamples'] = cases
    gold = d['assets_matrix_24']['GOLD']['orderbook_live_depth']['whale_walls_l3']
    e['gold_prior_pair_current_rows'] = [w for w in gold if w['side']=='SELL' and w['price'] in (4113.5,4113.8)]
    e['council_adaptation'] = {'independent_agents_dispatched':False, 'weights':[30,25,15,20,10], 'options':{}}
    for name,scores,fatal in (
        ('WAIT on stronger in-range ETH ask',[2,5,8,1,8],True),
        ('MODIFY lots only',[3,5,7,2,8],True),
        ('Inherit prior wall age and admit NAS',[3,5,8,2,8],True),
        ('DELETE advice; retain reserve; await fresh defense',[9,8,9,9,9],False)):
        e['council_adaptation']['options'][name] = {'scores':scores, 'fatal':fatal,
            'weighted_total':sum(s*w for s,w in zip(scores,e['council_adaptation']['weights']))/10}
    e['source_reading'] = 'All seven sources byte-read and hash-checked; six context sources unchanged. Full JSON traversal and block/array checks, with targeted manual review. Not exhaustive fresh manual line-by-line interpretation.'
    e['authority'] = 'Research only; no broker cancellation, modification, placement, production admission change, main update or PR merge.'
    return e


if __name__=='__main__':
    if len(sys.argv)!=4:
        raise SystemExit(__doc__)
    evidence = extract(sys.argv[1],sys.argv[2])
    Path(sys.argv[3]).write_text(json.dumps(evidence,indent=2)+'\n')
    print(json.dumps({'generation':evidence['generation'], 'nodes':evidence['tree']['nodes'],
                      'persistence':evidence['persistence_comparison']['current'],
                      'recommendation':evidence['pending_review']['recommendation']},indent=2))
