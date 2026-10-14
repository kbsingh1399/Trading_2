#!/usr/bin/env python3
"""Cycle 105: 24-asset dual-engine classification matrix with hard numbers."""
import json

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']

FRICTION_ADMIT = {  # playbook 7.4 admitted universe friction %
    'SP500.p': 0.8, 'NAS100.p': 1.0, 'XAUUSD.pi': 1.2, 'BTCUSD.pi': 1.7, 'DJ30.p': 1.5,
    'GER40.p': 2.0, 'USWTI.p': 3.5, 'ETHUSD.pi': 8.1, 'SOLUSD.p': 13.8,
    'EURUSD.pi': 0.5, 'GBPUSD.pi': 0.5, 'USDJPY.pi': 0.5,
}
WALL_FLOOR = {  # Gate R-2 calibration (USD)
    'BTCUSD.pi': 5.0e6, 'ETHUSD.pi': 5.0e6,
    'SP500.p': 1.0e6, 'NAS100.p': 1.0e6, 'DJ30.p': 1.0e6, 'GER40.p': 1.0e6,
    'XAUUSD.pi': 0.75e6, 'USWTI.p': 0.75e6, 'XAGUSD.pi': 0.75e6,
    'EURUSD.pi': 0.5e6, 'GBPUSD.pi': 0.5e6, 'USDJPY.pi': 0.5e6,
}

print(f"{'SYM':7} {'BROKER':10} {'MID':>12} {'SPRD':>6} {'Z':>6} {'RSI':>6} {'ATR%':>6} {'REGIME':>12} "
      f"{'VEL':>6} {'bestPersBid':>12} {'bestPersAsk':>12} {'wallFloor':>10}")
for s, a in AM.items():
    q, ci = a['quotes'], a['causal_indicators']
    ob = a.get('orderbook_live_depth', {})
    walls = ob.get('whale_walls_l3') or []
    pg = a.get('pullback_geometry', {})
    pers = [w for w in walls if (w.get('persist_s') or 0) >= 180]
    bb = max([w['notional_usd'] for w in pers if w['side'] == 'BUY'] or [0])
    ba = max([w['notional_usd'] for w in pers if w['side'] == 'SELL'] or [0])
    fl = WALL_FLOOR.get(a['symbol_broker'])
    print(f"{s:7} {a['symbol_broker']:10} {q['mid']:>12,.4f} {q['spread_bps']:>6.2f} {ci['vwap_z_score']:>6} "
          f"{ci['rsi_14']:>6} {ci['atr_pct']:>6} {ci['trend_regime']:>12} {str(pg.get('velocity_ratio')):>6} "
          f"${bb/1e6:>10.3f}M ${ba/1e6:>10.3f}M {(('$%.2fM' % (fl/1e6)) if fl else 'n/a'):>10}")

print()
print("=== PER-ASSET: nearest material (>=0.50M) band above/below mid, and contiguous-band span ===")
for s, a in AM.items():
    ob = a.get('orderbook_live_depth', {})
    vb = ob.get('venue_basis') or {}
    basis = (vb.get('HYPERLIQUID') or {}).get('basis_median')
    if basis is None:
        basis = ob.get('basis_median')
    if basis is None:
        print(f"{s:7} no basis -> cannot map perp levels to MT5")
        continue
    mid, atr = a['quotes']['mid'], a['causal_indicators']['atr_14']
    sc, rl = a['structural_stop_clusters'], a['reconstructed_liquidations']

    def up(lo, hi, n):  # for shorts: fuel above
        return (lo + basis, hi + basis, n)
    def dn(lo, hi, n):  # for longs: fuel below
        return (lo + basis, hi + basis, n)
    def comb(l1, l2):
        d = {}
        for b in (l1 or []) + (l2 or []):
            k = (round(b['min_price'] + basis, 6), round(b['max_price'] + basis, 6))
            d[k] = d.get(k, 0) + b['notional_usd']
        return sorted(d.items(), key=lambda kv: kv[0][0])
    above = comb(sc.get('nearest_buy_stop_clusters_above'), rl.get('nearest_short_squeeze_bands_above'))
    below = comb(sc.get('nearest_sell_stop_clusters_below'), rl.get('nearest_long_cascade_bands_below'))
    mat_a = [(k, n) for k, n in above if n >= 0.5e6]
    mat_b = [(k, n) for k, n in below if n >= 0.5e6]
    # contiguity of the above ladder
    def span(lst):
        if not lst:
            return None
        lo = lst[0][0][0]; hi = lst[0][0][1]
        n_bins = 1
        for (l2_, h2_), _ in lst[1:]:
            if abs(l2_ - hi) < 1e-6:
                hi = h2_; n_bins += 1
            else:
                break
        return lo, hi, n_bins
    sp_a = span(above)
    sp_b = span(sorted(below, key=lambda kv: -kv[0][0]))
    fa = f"{(mat_a[0][0][0]):,.4f} ${mat_a[0][1]/1e6:.2f}M" if mat_a else "NONE>=0.5M"
    fb = f"{(mat_b[0][0][1]):,.4f} ${mat_b[0][1]/1e6:.2f}M" if mat_b else "NONE>=0.5M"
    ca = f"{sp_a[0]:,.4f}->{sp_a[1]:,.4f} ({sp_a[2]} bins, {(sp_a[1]-sp_a[0])/atr:.2f} ATR)" if sp_a else "n/a"
    cb = f"{sp_b[1]:,.4f}<-{sp_b[0]:,.4f} ({sp_b[2]} bins, {(sp_b[0]-sp_b[1])/atr:.2f} ATR)" if sp_b else "n/a"
    print(f"{s:7} basis={basis:>10.4f}  firstMatAbove={fa:>26}  firstMatBelow={fb:>26}")
    print(f"{'':7} contiguous ladder above: {ca}")
    print(f"{'':7} contiguous ladder below: {cb}")
