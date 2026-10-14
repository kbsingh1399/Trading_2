#!/usr/bin/env python3
"""Cycle 105 deep geometry probe for the clean-friction universe."""
import json, sys

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']

SYMS = sys.argv[1:] or ['BTC', 'ETH', 'SP500', 'NAS100', 'GOLD', 'SILVER', 'USWTI']

for s in SYMS:
    a = AM[s]
    q, ci, vp = a['quotes'], a['causal_indicators'], a.get('volume_profile', {})
    ob = a.get('orderbook_live_depth', {})
    sc = a.get('structural_stop_clusters', {})
    rl = a.get('reconstructed_liquidations', {})
    vb = ob.get('venue_basis') or {}
    hl_b = (vb.get('HYPERLIQUID') or {}).get('basis_median')
    bn_b = (vb.get('BINANCE') or {}).get('basis_median')
    mid = q['mid']; atr = ci['atr_14']
    print('=' * 110)
    print(f"{s}  mid={mid:,.5f}  ATR={atr:,.5f}  Z={ci['vwap_z_score']}  RSI={ci['rsi_14']}  REGIME={ci['trend_regime']}")
    print(f"   basis: HL={hl_b}  BINANCE={bn_b}   (perp->MT5: MT5 = perp + basis)")
    print(f"   EMA20={ci['ema_20']:,.5f} EMA50={ci['ema_50']:,.5f} EMA200={ci['ema_200']:,.5f}  VWAP={ci['session_vwap_utc']:,.5f}")
    print(f"   POC={vp.get('poc')} VAH={vp.get('vah')} VAL={vp.get('val')}")
    pg = a.get('pullback_geometry', {})
    print(f"   pullback dir={pg.get('direction')} retrace={pg.get('retrace')} vel={pg.get('velocity_ratio')} bars={pg.get('bars_pullback')}/{pg.get('bars_impulse')}")
    print(f"   spread={q['spread_bps']}bps price={q['spread_price']}  contract={a['execution_specs']['contract_size']} minlot={a['execution_specs']['min_lot']} step={a['execution_specs']['step_lot']}")

    def bands(name, lst):
        print(f"   --- {name} (perp space) ---")
        for b in (lst or []):
            print(f"      [{b['min_price']:,.5f} - {b['max_price']:,.5f}]  ${b['notional_usd']/1e6:.4f}M  d={b.get('distance_pct')}%")
    bands('nearest_sell_stops_below', sc.get('nearest_sell_stop_clusters_below'))
    bands('nearest_buy_stops_above', sc.get('nearest_buy_stop_clusters_above'))
    bands('nearest_long_liq_below', rl.get('nearest_long_cascade_bands_below'))
    bands('nearest_short_squeeze_above', rl.get('nearest_short_squeeze_bands_above'))

    walls = ob.get('whale_walls_l3') or []
    for side in ('BUY', 'SELL'):
        sub = sorted([w for w in walls if w['side'] == side], key=lambda w: w['price'], reverse=(side == 'BUY'))
        print(f"   --- L3 {side} walls (perp space, sorted by favourability) ---")
        for w in sub[:14]:
            print(f"      {w['price']:,.5f}  ${w['notional_usd']/1e6:.4f}M  persist={w.get('persist_s')}s frac={w.get('presence_frac')} samples={w.get('samples')} status={w.get('persistence_status')} d={w.get('distance_pct')}% addr={w.get('address','')[:10]}")
    l2 = ob.get('l2_wall_levels') or []
    if l2:
        print("   --- L2 walls (Binance agg) ---")
        for w in sorted(l2, key=lambda w: -w['notional_usd'])[:10]:
            print(f"      {w['side']} {w['price']:,.5f} ${w['notional_usd']/1e6:.4f}M persist={w.get('persist_s')}s status={w.get('persistence_status')}")

    # recent 15m bars
    b15 = a.get('bars_15m_ohlcv') or []
    if b15:
        print("   --- last 10 x 15m bars (MT5) ---")
        for b in b15[-10:]:
            print(f"      O={b['open']:,.5f} H={b['high']:,.5f} L={b['low']:,.5f} C={b['close']:,.5f}")
    print()
