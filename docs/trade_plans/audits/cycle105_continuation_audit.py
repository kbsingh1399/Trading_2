"""Pinned Cycle 105 continuation research audit. No broker/admission actions.
Usage: python cycle105_continuation_audit.py SOURCE_DIRECTORY PREVIOUS_SNAPSHOT OUTPUT_JSON
The eighth, adjacent-generation receipt is a magnitude-change check, not an
independent venue verification. Research classifications are analyst judgments.
"""
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import sys

import cycle103_audit as base
import cycle105_audit as previous
from cycle104_audit import all_bands

COMMIT = 'eb0d611bf72b8ffb5398adaa7be70cefafe72a6e'
GENERATION = 'f21bb0ddf5ce4a4c993da82a4f1affc4'
PREVIOUS_COMMIT = 'b0824bb020e4294cafed69e44adc21b7b07f68b1'
PREVIOUS_SHA256 = 'd5feca3449d67884e8545ad9e31c076b913bfec16c87b43621c2b8234e7b7e77'
SOURCE_HASHES = dict(previous.SOURCE_HASHES)
SOURCE_HASHES[base.PATHS[0]] = 'b82635966554201664a9ee7237e4c5ee25eb6e5d17b80f137d570e1e40b4d22c'
SOURCE_HASHES[base.PATHS[4]] = '7328e052b98f2aea9300864c3238a0ba0f7d47160f04f22cfff6cebd4956f57d'
WATCHES = ('BTC', 'ETH', 'SP500', 'NAS100', 'GOLD')
REASONS = {
    'BTC': 'Bear/bear; primary ask duration recovered, but positive 5/15/30m taker flow and no demonstrated primary-shelf rejection.',
    'ETH': 'Bear/bear and selling; pending ticket separately DELETE: stop containment, friction, no primary-shelf touch/hold. Rebuild only after fresh qualification.',
    'SOL': 'Bear/bear, but positive taker flow; primary ask remote and selected-target R ceiling at the friction minimum below 2.5.',
    'BNB': 'Bear/bear; aged ask maximum below 5M, pullback velocity 1.1637, positive taker flow; quote age 26.63s.',
    'XRP': 'Minimum-lot spread cost 4 USD exceeds the maximum 2.175 USD friction budget.',
    'ADA': 'Explicit operator ban; spread and minimum-lot friction also fail.',
    'DOGE': 'Explicit operator ban; spread and minimum-lot friction also fail.',
    'TRX': 'Bull/mixed HTF; minimum-lot spread cost 9 USD exceeds 2.175 USD.',
    'DOT': 'Explicit operator ban; spread exceeds crypto cap.',
    'LINK': 'Explicit operator ban; spread exceeds crypto cap.',
    'BCH': 'Bear/bear; no aged 5M ask and no verified primary defended shelf.',
    'LTC': '50.05 bps exceeds crypto cap; minimum-lot spread cost 3 USD exceeds 2.175 USD.',
    'AVAX': 'Bear/bear; no aged 5M ask and no verified primary defended shelf.',
    'NEAR': 'Explicit operator ban; spread, minimum-lot friction and mixed HTF also obstruct.',
    'SP500': 'Bear/mixed HTF; relief retraces near EMA20 but primary ask not touched; selected nearby target not payable at 2R.',
    'NAS100': 'Bear/bear; near primary first seen inside latest completed candle, not a demonstrated retest; near geometry under 2R and deep geometry unconfirmed.',
    'DJ30': 'Bear/mixed HTF, not confirmed two-timeframe alignment.',
    'GER40': 'Mixed/bull HTF conflicts with bearish producer regime; neither allowed direction confirmed.',
    'GOLD': 'Bear/bear; two distinct-address asks total 0.7895M near EMA50, but the newer first appeared after the last completed candle. No confirmed joint defended retest.',
    'SILVER': 'Bear/bear; 6.48 bps exceeds 5 bps TradFi cap despite an aged 0.8442M ask.',
    'USWTI': 'Bull/bull and slow pullback; nearby bid sum has repeated address/size identities, support defense unconfirmed, and selected support-to-POC geometry fails friction and 2R.',
    'EURUSD': 'Bear/bear, but no aged 0.50M ask; broker-native spread precision unresolved, not zero-cost.',
    'GBPUSD': 'Bear/bear, but no aged 0.50M ask; broker-native spread precision unresolved, not zero-cost.',
    'USDJPY': 'Now BEARISH producer regime, not RANGE_BOUND; mixed/bull HTF and velocity 1.0663 defeat either aligned pullback interpretation.',
}


def risk_reserve(equity, nominal, margin):
    """Exact Decimal scenario; does not release a pending reserve on advice."""
    eq, n, m = map(lambda x: Decimal(str(x)), (equity, nominal, margin))
    stress = Decimal('1.25') * n + Decimal('2')
    full = Decimal('1.25') * Decimal('14.50') + Decimal('2')
    return {'pending_nominal_usd': str(n), 'pending_stress_usd': str(stress),
            'pending_margin_on_fill_usd': str(m), 'free_margin_after_fill_usd': str(eq-m),
            'post_joint_stop_equity_by_additional_full_risk_tickets':
                {str(k): str(eq-stress-k*full) for k in range(4)},
            'maximum_additional_full_risk_tickets_by_buffer_only':
                max(k for k in range(4) if eq-stress-k*full >= Decimal('4795')),
            'post_fill_above_playbook_4000': eq-m > Decimal('4000'),
            'reserve_released': False, 'stress_per_additional_full_risk_ticket_usd': str(full)}


def extract(source, previous_snapshot):
    source = Path(source)
    for path, expected in SOURCE_HASHES.items():
        if hashlib.sha256((source/path).read_bytes()).hexdigest() != expected:
            raise ValueError('Pinned source hash mismatch: '+path)
    e = base.extract(source, expected_generation=GENERATION, snapshot_commit=COMMIT,
                     context_commit=COMMIT, include_cycle103_geometry=False)
    d = json.loads((source/base.PATHS[0]).read_bytes())
    cutoff = int(d['generation_started_at_epoch']//60)*60
    for symbol, a in e['assets'].items():
        raw = d['assets_matrix_24'][symbol]
        walls = raw['orderbook_live_depth']['whale_walls_l3']
        a['all_unique_band_intervals'] = all_bands(a)
        a['analyst_classification'] = 'WATCHLIST' if symbol in WATCHES else 'NO SETUP'
        a['engine1_assessment'] = 'FAIL: abs(Z) < 2; other prerequisites cannot rescue the missing extreme.'
        a['engine2_assessment'] = REASONS[symbol]
        a['cvd_generation_cutoff_windows'] = {str(n): base.window(raw.get('cvd_1m_buckets') or [], cutoff, n) for n in (1,5,15,30)}
        a['wall_persistence_diagnostics'] = {
            'max_recorded_persist_s': max((w['persist_s'] for w in walls),default=0),
            'max_samples': max((w['samples'] for w in walls),default=0),
            'duration_is_not_continuous_defense': True,
            'producer_gate_used_as_admission_or_veto': False}
    # Retain real inventory instead of base.compact's list digest only.
    e['observed_inventory'] = {k:d[k] for k in ('active_positions','pending_orders','risk','capacity')}
    if d['active_positions'] or len(d['pending_orders']) != 1 or d['pending_orders'][0]['ticket'] != 18925596:
        raise ValueError('Pinned continuation inventory changed')
    p = d['pending_orders'][0]; receipt = d['risk']['tickets'][0]
    if receipt['ticket'] != p['ticket'] or receipt['status'] != 'BROKER_VALUED':
        raise ValueError('Missing matching pending valuation receipt')
    e['risk_math'] = risk_reserve(d['account']['equity_usd'],receipt['nominal_stop_loss_usd'],receipt['margin_on_fill_usd'])
    a=e['assets']['ETH']; raw=d['assets_matrix_24']['ETH']; spread=raw['quotes']['spread_price']
    distance=p['sl']-p['price_open']; bands=base.contains(p['sl'],a['all_unique_band_intervals'],a['basis']['median'])
    primary=next(w for w in raw['orderbook_live_depth']['whale_walls_l3'] if w['side']=='SELL' and w['price']==2450.3)
    mapped=primary['price']+a['basis']['median']
    bars_after=[b for b in raw['bars_15m_ohlcv'] if b['ts']>=base.epoch(primary['first_seen_utc'])]
    e['pending_review']={
        'ticket':p['ticket'],'recommendation':'DELETE','executed':False,'existing_order':p,
        'risk_distance':distance,'gross_R':(p['price_open']-p['tp'])/distance,
        'spread_usd_per_lot':spread*raw['execution_specs']['contract_size'],
        'friction_fraction':spread/distance,'minimum_distance_at_15pct_friction':spread/.15,
        'fixed_target_R_ceiling_at_friction_minimum':(p['price_open']-p['tp'])/(spread/.15),
        'contained_raw_bands':bands,
        'contained_mapped_intervals':[[b['min_price']+a['basis']['median'],b['max_price']+a['basis']['median']] for b in bands],
        'primary_ask':primary,'mapped_primary_ask':mapped,
        'primary_between_entry_and_stop':p['price_open']<mapped<p['sl'],
        'fully_subsequent_completed_15m_bars':bars_after,
        'primary_touched_by_fully_subsequent_completed_bar':any(b['low']<=mapped<=b['high'] for b in bars_after),
        'larger_ask_beyond_stop':next(w for w in raw['orderbook_live_depth']['whale_walls_l3'] if w['side']=='SELL' and w['price']==2461.7),
        'lot_reduction_changes_friction_ratio':False}
    cases={}
    for name,symbol,raw_entry,edge,target_edge in (
        ('BTC_primary','BTC',82164.,82200.,81600.),
        ('ETH_primary','ETH',2450.3,2460.,2420.),
        ('SOL_primary','SOL',105.94,106.,104.),
        ('SP500_near_subthreshold','SP500',7725.,7730.,7720.),
        ('SP500_primary','SP500',7741.,7750.,7720.),
        ('NAS100_near','NAS100',30039.,30100.,29900.),
        ('NAS100_deep','NAS100',30209.,30200.,29900.),
        ('GOLD_fresh_primary','GOLD',4126.3,4130.,4080.)):
        a=e['assets'][symbol]; b=a['source_blocks']; basis=a['basis']['median']
        atr=b['causal_indicators']['atr_14']; spread=b['quotes']['spread_price']
        entry=raw_entry+basis;stop=edge+basis+.5*atr+spread/2;target=(target_edge+basis)*1.0005
        index_floor=1.5*atr if b['category']=='INDICES' else None
        walls=[w for w in d['assets_matrix_24'][symbol]['orderbook_live_depth']['whale_walls_l3'] if w['side']=='SELL' and w['price']==raw_entry]
        cases[name]={'symbol':symbol,'research_entry':entry,'research_stop':stop,'research_target_5bps':target,
            'gross_R':(entry-target)/(stop-entry),'friction_fraction':spread/(stop-entry),'walls':walls,
            'contained_raw_bands':base.contains(stop,a['all_unique_band_intervals'],basis),
            'entry_distance_atr':abs(entry-b['quotes']['mid'])/atr,'index_minimum_distance':index_floor,
            'gross_R_at_index_minimum':(entry-target)/index_floor if index_floor else None,
            'R_ceiling_at_friction_minimum_to_selected_target':(entry-target)/(spread/.15),
            'executable':False}
    a=e['assets']['USWTI'];b=a['source_blocks'];basis=a['basis']['median'];atr=b['causal_indicators']['atr_14'];spread=b['quotes']['spread_price']
    # Fresh near bid, not the vanished 93.58 primary from Cycle 105.
    wall=next(w for w in d['assets_matrix_24']['USWTI']['orderbook_live_depth']['whale_walls_l3'] if w['side']=='BUY' and w['price']==93.843)
    entry=wall['price']+basis+spread/2;stop=93.8+basis-.5*atr-spread/2;target=b['volume_profile']['poc']*.9995
    cases['USWTI_subthreshold']={'symbol':'USWTI','wall':wall,'mapped_bid':wall['price']+basis,
        'research_entry':entry,'research_stop':stop,'research_target_5bps':target,
        'gross_R':(target-entry)/(entry-stop),'friction_fraction':spread/(entry-stop),
        'contained_raw_bands':base.contains(stop,a['all_unique_band_intervals'],basis),'executable':False}
    e['continuation_counterexamples']=cases
    e['composite_wall_checks']={}
    for symbol,side,lo,hi in (('GOLD','SELL',4113.4,4113.9),('USWTI','BUY',93.67,93.85)):
        rows=[w for w in d['assets_matrix_24'][symbol]['orderbook_live_depth']['whale_walls_l3']
              if w['side']==side and lo<=w['price']<=hi and w['persist_s']>=180]
        groups={}
        for w in rows:
            key=(w['address'],w['side'],w['size'])
            groups[key]=max(groups.get(key,0),w['notional_usd'])
        e['composite_wall_checks'][symbol]={'rows':rows,'naive_notional_sum':sum(w['notional_usd'] for w in rows),
            'distinct_address_side_size_count':len(groups),'conservative_signature_max_sum':sum(groups.values()),
            'latest_first_seen':max(w['first_seen_utc'] for w in rows),
            'unique_order_ids_available':False,
            'interpretation':'Diagnostic only: repeated address/size can be re-pegs or distinct same-sized orders; neither count nor continuous defense certified.'}
    prev_bytes=Path(previous_snapshot).read_bytes()
    if hashlib.sha256(prev_bytes).hexdigest()!=PREVIOUS_SHA256:
        raise ValueError('Pinned adjacent source hash mismatch')
    p=json.loads(prev_bytes)
    if p['generation_id']!='f214c940152c4deaa1d81de871342925':
        raise ValueError('Wrong adjacent generation')
    def band(snapshot):
        return next(b for b in snapshot['assets_matrix_24']['SP500']['structural_stop_clusters']['nearest_sell_stop_clusters_below'] if b['min_price']==7700 and b['max_price']==7710)
    old,new=band(p),band(d)
    e['adjacent_generation_check']={'commit':PREVIOUS_COMMIT,'generation':p['generation_id'],'as_of_utc':p['as_of_utc'],
        'sha256':hashlib.sha256(prev_bytes).hexdigest(),'bytes':len(prev_bytes),'old_SP500_band':old,'new_SP500_band':new,
        'notional_ratio':new['notional_usd']/old['notional_usd'],
        'independent_venue_verification':False,'over_100x_single_generation_jump':new['notional_usd']>100*old['notional_usd']}
    e['reading_disclosure']='All seven sources byte-read; full JSON traversal and automated block/array checks. Five unchanged context files hash-verified against prior audit; complete new history suffix reviewed. Not a claim of manual line-by-line interpretation of every leaf.'
    e['authority']='Research only. No broker calls, cancellation, placement, main update or PR merge.'
    e['council_adaptation']={'independent_agents_dispatched':False,'weights':[30,25,15,20,10],
        'options':{}}
    for name, scores, fatal in (
        ('WAIT unchanged',[2,5,8,1,8],True),
        ('MODIFY lots only',[3,5,7,2,8],True),
        ('NEW NAS deep with thin stop',[3,6,8,2,8],True),
        ('DELETE advice; retain reserve; no new admission',[9,8,9,9,9],False)):
        e['council_adaptation']['options'][name]={'scores':scores,'fatal':fatal,
            'weighted_total':sum(s*w for s,w in zip(scores,e['council_adaptation']['weights']))/10}
    return e


if __name__=='__main__':
    if len(sys.argv)!=4:
        raise SystemExit(__doc__)
    evidence=extract(sys.argv[1],sys.argv[2])
    Path(sys.argv[3]).write_text(json.dumps(evidence,indent=2)+'\n')
    print(json.dumps({'generation':evidence['generation'],'nodes':evidence['tree']['nodes'],
        'risk':evidence['risk_math'],'pending_action':evidence['pending_review']['recommendation']},indent=2))
