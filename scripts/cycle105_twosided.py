#!/usr/bin/env python3
"""Cycle 105: two-sided market-maker audit of the Hyperdash L3 feed."""
import json, sys
from collections import defaultdict

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']

print(f"{'SYM':8} {'totW':>5} {'persW':>6} {'2side':>6} {'persNot':>9} {'2sPers$':>9} {'share%':>7}  top two-sided wallets (addr: bid$ / ask$ / persist)")
for s, a in AM.items():
    ob = a.get('orderbook_live_depth', {})
    walls = ob.get('whale_walls_l3') or []
    if not walls:
        print(f"{s:8} {0:5} {0:6} {0:6} {'$0.00M':>9} {'$0.00M':>9} {0:7.1f}  (no L3 feed)")
        continue
    by_addr = defaultdict(lambda: {'BUY': 0.0, 'SELL': 0.0, 'bp': 0.0, 'sp': 0.0, 'nb': 0, 'ns': 0})
    for w in walls:
        e = by_addr[w['address']]
        e[w['side']] += w['notional_usd']
        e[({'BUY':'bp','SELL':'sp'}[w['side']])] = max(e[({'BUY':'bp','SELL':'sp'}[w['side']])], w.get('persist_s') or 0)
        e['n' + w['side'][0].lower()] += 1
    pers = [w for w in walls if (w.get('persist_s') or 0) >= 180]
    pers_not = sum(w['notional_usd'] for w in pers)
    two = {k: v for k, v in by_addr.items() if v['BUY'] > 0 and v['SELL'] > 0}
    two_pers_not = 0.0
    for w in pers:
        if w['address'] in two:
            two_pers_not += w['notional_usd']
    share = 100.0 * two_pers_not / pers_not if pers_not else 0.0
    top = sorted(two.items(), key=lambda kv: -(kv[1]['BUY'] + kv[1]['SELL']))[:3]
    desc = '  '.join(f"{k[:8]}: {v['BUY']/1e6:.2f}/{v['SELL']/1e6:.2f}/{max(v['bp'],v['sp']):.0f}s" for k, v in top)
    print(f"{s:8} {len(walls):5} {len(pers):6} {len(two):6} ${pers_not/1e6:8.2f}M ${two_pers_not/1e6:8.2f}M {share:7.1f}  {desc}")
