#!/usr/bin/env python3
"""Cycle 105 whale-wall inventory: persistent (>=180s) and large walls, per side."""
import json, sys

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']

for s in sys.argv[1:]:
    a = AM[s]
    ob = a.get('orderbook_live_depth', {})
    walls = ob.get('whale_walls_l3') or []
    mid = a['quotes']['mid']
    atr = a['causal_indicators']['atr_14']
    print('=' * 100)
    print(f"{s} mid={mid:,.5f} ATR={atr:,.5f}  total_walls={len(walls)}")
    for side in ('BUY', 'SELL'):
        sub = [w for w in walls if w['side'] == side]
        # persistent first
        pers = sorted([w for w in sub if (w.get('persist_s') or 0) >= 180],
                      key=lambda w: w['price'], reverse=(side == 'BUY'))
        print(f"  ### {side}: {len(pers)} walls with persist>=180s  (showing 12 closest to mid, then 6 largest)")
        for w in pers[:12]:
            print(f"     {w['price']:,.5f} ${w['notional_usd']/1e6:.4f}M pers={w.get('persist_s')}s frac={w.get('presence_frac')} samp={w.get('samples')} status={w.get('persistence_status')} d={w.get('distance_pct')}%")
        big = sorted(pers, key=lambda w: -w['notional_usd'])[:6]
        print(f"     -- largest persistent {side} --")
        for w in big:
            print(f"     {w['price']:,.5f} ${w['notional_usd']/1e6:.4f}M pers={w.get('persist_s')}s frac={w.get('presence_frac')} d={w.get('distance_pct')}%")
        big_any = sorted(sub, key=lambda w: -w['notional_usd'])[:5]
        print(f"     -- largest {side} regardless of persistence --")
        for w in big_any:
            print(f"     {w['price']:,.5f} ${w['notional_usd']/1e6:.4f}M pers={w.get('persist_s')}s frac={w.get('presence_frac')} d={w.get('distance_pct')}%")
        # aggregate persistent notional in 1-ATR buckets around mid
        print(f"     -- persistent {side} notional aggregated in 0.5-ATR buckets from mid --")
        for k in range(-6, 7):
            lo = mid + (k - 0.5) * 0.5 * atr
            hi = mid + (k + 0.5) * 0.5 * atr
            tot = sum(w['notional_usd'] for w in pers if lo <= w['price'] < hi)
            if tot > 0:
                print(f"        [{lo:,.4f},{hi:,.4f}) k={k:+d}: ${tot/1e6:.3f}M")
    l2 = ob.get('l2_wall_levels') or []
    if l2:
        print("  ### L2 wall levels (Binance aggregated)")
        for w in sorted(l2, key=lambda w: w['price']):
            print(f"     {w['side']} {w['price']:,.5f} ${w['notional_usd']/1e6:.4f}M pers={w.get('persist_s')}s status={w.get('persistence_status')} d={w.get('distance_pct')}%")
    print()
