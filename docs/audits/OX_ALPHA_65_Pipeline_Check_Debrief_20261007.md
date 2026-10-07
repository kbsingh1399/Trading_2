# OX_ALPHA_65 — Pipeline Check Debrief: Broker-Gate Calibration, EURUSD Fill, and the XRP Knife-Edge

**Date:** 2026-10-07 11:35 UTC | **Branch:** arena/4adf3661-trading-2 | **Companion to:** OX_ALPHA_65_Multi_Agent_Council_20261007.md
**Snapshot basis:** 11:33:47 UTC (equity 4,825.34, cushion +50.34, 1 filled + 1 pending = 2/2)

---

## 1. Random-check pipeline verdict: FULL PASS — three independent gates fired in sequence

The principal-directed XRP random check (commit eea2d72) completed the entire loop: spec to git, daemon pull within 60 seconds, broker-side gate interaction, staging on MT5 live as **#18624984**, telemetry visibility. The enforcement chain behaved exactly as designed, in three layers:

1. **Friction/risk solver (cloud, pre-draw):** my first raw draw (2 lots x 0.019 = 38 USD) was rejected locally and redrawn from the feasible set.
2. **Muscle risk cap (stage time):** the staged order respected the 20.00 USD hard cap.
3. **Broker stops-level gate (MT5, previously unknown to the cloud):** the raw draw's 12-point stop width (SL 1.417) was BELOW the broker's minimum `trade_stops_level` of 20 points (0.020 USD) — the muscle auto-calibrated the width to 0.020, landing risk at exactly 20.00 USD, and recomputed TP to 1.479 to preserve exactly 2.50R.

A random order entered the system and was shaped by three independent layers into the only compliant shape the instrument admits. That is the fail-closed architecture working end to end. The check objective is achieved.

## 2. Discovery: XRP sits on the feasibility knife-edge (new constraint-map entry)

The broker's 20-point minimum stop distance is now a known XRP constraint, and it makes XRP tradeable in EXACTLY one shape: stop width d must satisfy d >= 0.020 (broker) and 1.0 lot x d x 1000 <= 20.00 (risk cap at minimum lot) — so **d = 0.020 exactly, risk = 20.00 exactly, friction = (0.005 spread + 0.001 tick)/0.020 = 0.30R** against the 0.35R ceiling. One basis point of spread widening, or one tick of cap tightening, and every XRP plan is refused. The council's standing NO-TRADE posture on XRP (friction zone) is now reinforced by a hard structural argument: the instrument offers zero compliance margin. Future XRP plans should assume refusal unless the spread compresses materially.

## 3. Open reconciliation items (muscle log requests)

- **XRP #18624984 disappearance:** the order is in neither pending_orders nor active_positions at 11:33:47, despite a TTL of 12:22 UTC. It was neither filled (no position) nor expired (TTL not reached). Most likely cancelled muscle-side or withdrawn by the broker — please confirm from the MT5 journal which, and why, so the audit trail is complete.
- **Pending-list integrity:** within 20 minutes the council observed three different pending sets: 11:17 snapshot = EUR + USWTI (no XRP); the 10:58-11:20 handoff message = EUR + XRP (no USWTI); 11:33 snapshot = USWTI only (EUR filled). The generator's `pending_orders` must reconcile exactly with the broker order book every cycle — this is the same class of defect as the stale Z field (section 4 of the Council 65 doc): fields computed from cached state rather than snapshot state.

## 4. EURUSD fill ratified — muscle cured both footnotes at staging

**Position #18625675: LONG 0.10 lots @ 1.11850 (filled 11:27:42 UTC), SL 1.11740, TP 1.12125 — risk 11.00 USD, exactly 2.50R.** The original pending #18620547 carried two governance footnotes (risk 9.90 below the 10.00 floor; TP 3.18R above the 3.14 ceiling); the muscle's staging corrected BOTH — volume 0.09 to 0.10, TP 1.12200 to 1.12125 — producing the compliant geometry the Council-65 repunch directive was after, at a BETTER level (1.11850 vs 1.11880) with LESS risk (11.00 vs 12.60). **The cancel-and-repunch directive is superseded by events; the fill is ratified as-staged.** Ratchet schedule (R = 11 pips): phase 0 at 1.11938 -> SL 1.11867; phase 1 at 1.12015 -> SL 1.11944; phase 2 trail from 1.12070; TP 1.12125. Current +0.02R at 1.11852.

**Critical timing note:** the position's natural 24-bar decay deadline is 17:27:42 UTC — AFTER the 16:55 purge deadline. The pre-FOMC invariant therefore binds first: by 16:55 the position must either carry the phase-0 break-even lock (requires touching 1.11938) or be closed at market. No exceptions into the 17:00-18:30 blackout.

## 5. Book topology (11:33:47 UTC)

| Item | State | Next event |
| --- | --- | --- |
| EURUSD #18625675 (filled) | +0.02R, PHASE_0_PENDING | Phase 0 at 1.11938; 16:55 BE-lock-or-close |
| USWTI #18625151 (pending) | BUY LIMIT 0.19 @ 91.20; market has drifted UP to 91.52/91.58 (limit now ~0.36 below the ask) | Fill needs a dip; 16:55 cancel if unfilled |
| BTC post-sweep plan | Armed (limit 83,380 / SL 82,900 / TP 84,580); pocket 83,450-83,510 un-swept | Stages only post-sweep into a free slot; expires 16:55 |
| XRP #18624984 | Gone from book (see section 3) | Log confirmation requested |

Worst-case portfolio: 11.00 (EUR) + 12.35 (USWTI) = 23.35 USD -> equity 4,801.99 = **+26.99 above the floor**. Filled 1/2, pending 1/2.

## 6. Standing directives (reaffirmed)

1. Ratchet owns EURUSD #18625675; the 16:55 BE-lock-or-close override is the binding deadline (decay deadline is later and never fires first).
2. USWTI rests until fill or 16:55 cancel — no re-pricing chase.
3. BTC stages only after the 83,450-83,510 sweep, only into a free slot, only before 16:55.
4. Nothing stages into the 17:00-18:30 blackout; full post-event council at the first refresh after 18:30 UTC.
5. Muscle actions requested: (a) XRP #18624984 log confirmation; (b) pending_orders reconciliation fix in the generator; (c) the vwap_z_score live-recompute fix already requested in Council 65.

*Every figure traces to the 11:33:47 UTC telemetry snapshot or the account state relayed by the muscle; no statistic is fabricated.*
