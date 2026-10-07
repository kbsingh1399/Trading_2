# OX_ALPHA_66 — Event Debrief (12:30 UTC): EURUSD Stop-Out, BTC Standby Promoted, USWTI Running

**Snapshot basis:** 12:30:52 UTC | equity 4,819.08 | cushion +44.08 | 1 filled + 1 pending = 2/2

## 1. EURUSD #18625675: STOPPED OUT at 1.11740 — −11.00 USD (−1.00R)
The exhaustion-reversion thesis never paid: EURUSD broke to 1.1169 (Z was −4 and extended further). The stop did exactly its job — disaster protection, no gap, no slippage beyond spread. Realized P&L on the trade: −11.00. Post-mortem honesty: a −4.06 sigma extreme kept extending; the fill at 1.11850 was 11 pips of premature bid on a falling knife session. The geometry (2.50R, 11.00 risk) was compliant; the edge was not there pre-FOMC. Balance now approx 4,814.14 realized.

## 2. BTC standby #1 PROMOTED: pending #18630694 @ 83,380
The muscle staged `OXALPHA66-BTC-LONG-POSTSWEEP-V2` exactly as committed (limit 83,380, SL 82,700 below the real 8.46M cascade floor, TP 85,080, risk 13.60 — cap exception accepted). Market 83,459/83,474: the limit rests approx 80 USD below the ask — a shallow retest of the swept zone fills it. Promotion order followed the council ranking.

## 3. USWTI #18625151: RUNNING at +0.46R (+5.64 USD)
Price 91.502/91.549 against entry 91.20. Phase-0 trigger 91.720 (approx 0.18 USD of upside). The shelf-reclaim thesis is working; ratchet armed.

## Book topology
| Item | State | Next event |
| --- | --- | --- |
| USWTI #18625151 | +0.46R, PHASE_0_PENDING | Phase 0 at 91.720 -> BE lock 91.298 |
| BTC #18630694 | Pending @ 83,380 (market 83,474) | Fill on retest; 16:55 purge if unfilled |
| EURUSD | Closed −1.00R | — |

Worst case now: USWTI 12.35 + BTC 13.60 = 25.95 -> equity approx 4,793.13 = +18.13 above floor. FOMC discipline unchanged: purge 16:55, blackout 17:00-18:30, flat-into-event preference stands unless phase-1 locks are secured.

*All figures from the 12:30:52 UTC authentic snapshot; no statistic is fabricated.*
