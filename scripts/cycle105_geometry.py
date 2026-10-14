#!/usr/bin/env python3
"""Cycle 105: basis-mapped geometry calculator. All levels converted to MT5 space."""
import json, sys

D = json.load(open('docs/telemetry/live_snapshot_latest.json'))
AM = D['assets_matrix_24']


def build(sym):
    a = AM[sym]
    ob = a.get('orderbook_live_depth', {})
    vb = ob.get('venue_basis') or {}
    hl = (vb.get('HYPERLIQUID') or {})
    # basis_median = MT5_mid - perp_mid  =>  MT5 = perp + basis
    basis = hl.get('basis_median')
    if basis is None:
        basis = ob.get('basis_median')
    perp_mid = hl.get('mid')
    return a, basis, perp_mid


def to_mt5(p, basis):
    return None if (p is None or basis is None) else p + basis


def show(sym):
    a, basis, perp_mid = build(sym)
    q, ci = a['quotes'], a['causal_indicators']
    mid, atr = q['mid'], ci['atr_14']
    sc, rl, ob = a['structural_stop_clusters'], a['reconstructed_liquidations'], a['orderbook_live_depth']
    print('=' * 112)
    print(f"{sym}: MT5 mid={mid:,.4f}  HL perp mid={perp_mid}  basis(HL)={basis}  ATR={atr:,.4f}")
    print(f"  instant basis check: MT5-perp = {None if perp_mid is None else round(mid-perp_mid,4)}   |basis - instant| in ATR = "
          f"{None if perp_mid is None else round(abs(basis-(mid-perp_mid))/atr,3)}")
    print(f"  EMA20={ci['ema_20']:,.4f} EMA50={ci['ema_50']:,.4f} EMA200={ci['ema_200']:,.4f} VWAP={ci['session_vwap_utc']:,.4f}")
    vp = a.get('volume_profile', {})
    print(f"  POC={vp.get('poc')} VAH={vp.get('vah')} VAL={vp.get('val')}")

    def conv(lst):
        out = []
        for b in (lst or []):
            out.append((to_mt5(b['min_price'], basis), to_mt5(b['max_price'], basis), b['notional_usd']))
        return out

    sb = conv(sc.get('nearest_sell_stop_clusters_below'))
    ba = conv(sc.get('nearest_buy_stop_clusters_above'))
    lb = conv(rl.get('nearest_long_cascade_bands_below'))
    sa = conv(rl.get('nearest_short_squeeze_bands_above'))
    print("  BUY-STOPS ABOVE (MT5):")
    for lo, hi, n in ba:
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M   ({(lo-mid)/atr:+.2f} to {(hi-mid)/atr:+.2f} ATR from mid)")
    print("  SHORT-SQUEEZE ABOVE (MT5):")
    for lo, hi, n in sa:
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M")
    print("  SELL-STOPS BELOW (MT5):")
    for lo, hi, n in sb:
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M   ({(lo-mid)/atr:+.2f} to {(hi-mid)/atr:+.2f} ATR)")
    print("  LONG-LIQ BELOW (MT5):")
    for lo, hi, n in lb:
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M")

    # combined downside magnets (stops+liq on same bin) and upside fuel
    def comb(sa_, sb_, sign):
        d = {}
        for lo, hi, n in (sa_ or []) + (sb_ or []):
            d.setdefault((round(lo, 6), round(hi, 6)), 0)
            d[(round(lo, 6), round(hi, 6))] += n
        return sorted(d.items(), key=lambda kv: kv[0][0], reverse=(sign < 0))
    print("  COMBINED DOWNSIDE MAGNET (sell-stops + long-liq, MT5):")
    for (lo, hi), n in comb(sb, lb, -1):
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M   ({(lo-mid)/atr:+.2f} ATR)")
    print("  COMBINED UPSIDE FUEL (buy-stops + short-squeeze, MT5):")
    for (lo, hi), n in comb(ba, sa, +1):
        print(f"     [{lo:,.4f} - {hi:,.4f}] ${n/1e6:.4f}M   ({(lo-mid)/atr:+.2f} ATR)")

    walls = ob.get('whale_walls_l3') or []
    for side in ('BUY', 'SELL'):
        pers = [w for w in walls if w['side'] == side and (w.get('persist_s') or 0) >= 180]
        print(f"  PERSISTENT(>=180s) {side} WALLS, MT5 space, sorted by distance from mid:")
        for w in sorted(pers, key=lambda w: abs(to_mt5(w['price'], basis) - mid))[:16]:
            mp = to_mt5(w['price'], basis)
            print(f"     {mp:,.4f} (perp {w['price']:,.4f})  ${w['notional_usd']/1e6:.4f}M pers={w.get('persist_s')}s frac={w.get('presence_frac')} "
                  f"d={((mp-mid)/atr):+.2f} ATR  addr={w.get('address','')[:10]}")
        print(f"     TOTAL persistent {side} notional = ${sum(w['notional_usd'] for w in pers)/1e6:.3f}M")
    print()


for s in (sys.argv[1:] or ['BTC']):
    show(s)
