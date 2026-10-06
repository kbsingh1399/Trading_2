# OX_ALPHA_62 Deliberate Trade Plan — SOL Long Limit, 2026-10-07

**Plan ID:** OXALPHA62-SOL-LONG-20261007A | **Version:** omni.trade_plan.v1
**Author:** Arena Brain (OX_ALPHA, multi-source deliberation authorized by the OX_ALPHA_62 closing directive)
**Status:** Validated offline; awaiting fail-closed staging via `Terminal/Headless/stage_trade_plan.py`
**Discipline:** This document carries only deterministic, source-attributed numbers. No statistic in it is fabricated; every derived figure is recomputed by the stager at stage time.

---

## 1. Executive Summary

Stage a **passive LONG limit on SOLUSD.p at 119.95** (0.15 lots, risk 10.50 USD, SL 119.25, TP 121.70 = 2.50R, 24-bar TTL), a trend-continuation dip-buy at the structural 24-hour low retest of the strongest-momentum major in the 24-asset universe, against a risk-on macro regime. The GOLD short #18576872 stays untouched apart from its automated ratchet (phase 0 is live-imminent; see section 8).

## 2. Multi-Source Data Foundation

Three independent sources were fused; all cross-check within tolerance.

| Source | As-of | Key readings |
| --- | --- | --- |
| Repo candle factory (`Data/Candles/*_15m.parquet`, live telemetry-synced) | last bar 2026-10-06 19:30 UTC | SOL close 120.39, Wilder ATR(14) 0.46123, 24h low 119.99, 96-bar range position 0.55; GOLD close 4169.00 ATR 6.11; ETH 2685.80 ATR 6.80; DOGE 0.09260 ATR 0.00037 |
| Live web quotes (Economic Times crypto desk; Investing.com XAU/USD) | 2026-10-07 00:57 IST | BTC ~85.4k USD (−0.2 pct), ETH ~2,686 USD (−0.8 pct), SOL ~120.4-120.8 USD (+0.7 pct), DOGE weak; GOLD 4,166.79 / 4,167.13, day range 4,103.70-4,179.72 |
| Macro calendar and event data (fedratecalc, Admiral Markets, VT Markets) | 2026-10-05/07 | FOMC minutes TODAY 2026-10-07 18:00 UTC; Sep FOMC hiked 25 bp to 3.75-4.00 pct (12-0); Oct 28 decision ~80 pct priced hold; Sep NFP +29k vs +90k expected, unemployment 4.2 pct; core PCE 3.0 pct y/y (below ~3.3 consensus); JOLTS −256k; CPI due Oct 14, PPI/retail Oct 15, FOMC Oct 28, GDP/PCE Oct 29 |

Cross-validation: the repo candle closes and the web quotes agree to within a few tenths of a percent on every overlapping asset (SOL 120.39 vs ~120.4-120.8; ETH 2685.8 vs ~2,686; GOLD 4169 vs 4,166.8/4,167.1). The two datasets corroborate each other; neither is used alone.

## 3. Macro Regime Read (Specialist 3 lens)

- **Labour market cracking:** September payrolls +29k against a ~+90k consensus, July-August revisions −60k, unemployment up to 4.2 pct, JOLTS down 256k.
- **Inflation cooling at the margin:** core PCE 3.0 pct y/y printed below the ~3.3 pct consensus.
- **Policy path:** the September hike (to 3.75-4.00 pct) is done; futures price roughly an 80 pct hold for October 28. The marginal direction of surprise has shifted from hawkish to neutral-softer.
- **Risk assets responding:** S&P 500 above 7,830 intraday and Nasdaq 100 at a record 31,076 on the AI complex; gold bid (+0.7 pct on the day) on the softer dollar.
- **Implication:** dips in trending risk assets are buyable into a regime where the Fed's next move is priced as a hold and the dollar's interest-rate support is eroding. The one scheduled landmine is **today's FOMC minutes at 18:00 UTC** — the plan's staging window expires at 12:00 UTC and its blackout covers 17:00-18:30 UTC, so the order is staged early with TTL headroom or not at all.

## 4. Candidate Ranking (Specialist 1 lens)

All three spec-listed candidates were priced with identical geometry (SL = entry − 1.5 x ATR(14), TP = 2.50R, risk floored into the 10-20 USD band). ATR and structure from the live-synced 15m candles.

| Candidate | Limit | ATR(14) | SL | TP | Volume | Risk | Notional | Stop as pct of price | Read |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **SOL (primary)** | 119.95 | 0.46123 | 119.25 | 121.70 | 0.15 | 10.50 USD | 1,799 USD | 0.58 pct | Strongest trend (1M +13.79 pct), mid-range (0.55), limit sits at the 119.99 24h-low retest. Best stop-to-friction ratio of the three. |
| ETH (alternate) | 2,672.00 | 6.80212 | 2,661.80 | 2,697.51 | 0.98 | 10.00 USD | 2,618 USD | 0.38 pct | Bottom of range (0.10), weaker 1D (−0.79 pct): mean-reversion profile, narrower stop hurts the friction ratio. Reassess only post-FOMC with fresh data. |
| DOGE (pass) | 0.09210 | 0.00037 | 0.09154 | 0.09348 | 17.86 | 10.00 USD | 1,645 USD | 0.61 pct | Weakest momentum (−1.91 pct on the day, 1Y −49 pct); falling-knife profile at 0.10 range position. Declined despite the spec listing it. |

Selection logic: at a fixed 2.50R target with a 1.5 x ATR stop, expectancy differentiates through (a) trend quality — SOL leads the 1M and 1W columns, (b) structural entry — the limit is the prior-day low, a level that has already auctioned once, and (c) friction efficiency — SOL's stop is the widest fraction of price among the majors considered, so a given spread costs the least in R units. GOLD itself was declined for the new slot: the book is already short GOLD, the metal just rallied 0.7 pct on the macro read, and doubling the same direction in the same asset concentrates exactly the risk the MAX_CONCURRENT and OCO invariants exist to prevent.

## 5. The Order

| Field | Value |
| --- | --- |
| Symbol | SOLUSD.p (SOL perpetual CFD, contract 100, tick 0.01, min/step lot 0.01) |
| Direction | LONG (passive limit) |
| Limit price | 119.95 (0.37 pct below last close; rests 0.04 under the 119.99 24h low) |
| Stop loss | 119.25 (0.70 = 1.52 x ATR(14); above the 1.5 x ATR adaptive floor) |
| Take profit | 121.70 (2.50R; inside the 2.50R-3.14R band, no moonshot) |
| Volume | 0.15 lots (notional 1,799.25 USD; margin at 1:100 leverage ~18 USD against 4,422 USD free) |
| Risk | 10.50 USD (inside the 10-20 USD band; hard cap 20.00 USD enforced again muscle-side) |
| TTL | 24 bars (6 h) via `expiration_seconds` 21,600 |
| Comment | ARENA:PLAN_v1 (journal-tracked; purge via `--purge-expired`) |

**Invariant compliance checklist** (each re-verified client-side by the stager, then again muscle-side):

- Risk 10.50 USD within 10-20 USD band; hard 20.00 USD cap respected.
- SL distance 1.52 x ATR(14) — adaptive-stop floor respected.
- TP at 2.50R — inside the 2.50R-3.14R target band.
- Volume above min lot, aligned to step lot; every price on the 0.01 tick grid.
- Exactly 1 filled position live (GOLD short) with 1 open slot; 1 filled + this resting limit is within both the MAX_CONCURRENT 2 (fills) and the 5-order decoupled resting ceiling (first-fill OCO).
- Equity cushion: 4,839.88 − 10.50 (existing GOLD worst case at current SL) − 10.50 (this plan) = 4,818.88 USD, i.e. +43.88 USD above the 4,775.00 floor under simultaneous worst-case stopouts.
- Passive entry only: the limit must rest below the live ask at stage time (marketable limits are refused both here and muscle-side).

## 6. Friction Accounting and Expectancy

Mandated conservative bound (41 bps round-trip on notional, as in all sizing/payoff math):

- Friction: 0.0041 x 1,799.25 = 7.38 USD = 0.70R.
- Net win at TP: +2.50R − 0.70R = +1.80R (+18.87 USD). Net loss at SL: −1R − 0.70R = −1.70R (−17.88 USD).
- Breakeven win rate at the conservative bound: 48.7 pct.

Live-spread case (the stager gates on the ACTUAL tunnel quote at stage time; assumption shown for illustration only, spread 0.09 round trip):

- Friction: 0.09 / 0.70 = 0.13R. Net win +2.37R (+24.88 USD); net loss −1.13R (−11.86 USD).
- Breakeven win rate: 32.2 pct.

The gap between the two bounds is the honest statement of uncertainty: under the backtest-grade haircut the setup is close to symmetric and must be carried by the trend thesis; under live crypto-CFD spreads it carries a normal institutional margin. This is why sizing sits at the bottom of the risk band (10.50 of a permitted 20.00 USD) and why the stager refuses to stage if the live round-trip spread exceeds 0.35R. No win-rate claim is made in either direction — the plan documents geometry and breakevens only.

## 7. Management Once Filled (Specialist 2 lens)

The continuous brain's ratchet governs automatically (omni.ratchet.session_conditional.v1, 15-second ticks):

| Phase | Trigger | Action (LONG, R = 0.70, entry 119.95) |
| --- | --- | --- |
| 0 — break-even lock | gain ≥ 0.80R (price ≥ 120.51) | SL → 120.055 (entry + 0.15R; tick-aligned 120.06) |
| 1 — profit lock | gain ≥ 1.50R (price ≥ 121.00) | SL → 120.545 (entry + 0.85R; tick-aligned 120.55) |
| 2 — runner lock | gain ≥ 2.00R (price ≥ 121.35) | trail SL at 0.65R behind price, re-armed per 0.05R improvement |
| Exit | +2.50R | TP 121.70 (band ceiling 3.14R = 122.15 not chased) |
| Decay | gain < 0.20R after 24 bars | close at market (reason time_decay_24bars) |

## 8. Existing GOLD Short #18576872 — No New Action Required

- Live bid 4,166.79 against entry 4,176.00 and R = 10.50: the position is at **+0.877R, already through the +0.80R phase-0 trigger** (trigger price 4,167.60). The continuous brain's next 15-second tick will dispatch `modify_sltp(ticket=18576872, sl=4174.425)` (entry − 0.15R; tick-aligned 4,174.42-4,174.43), locking friction-free profit. No manual override.
- TP 4,143.00 = +3.14R sits 0.55 under the 24h low 4,143.55 — expect the auction to test it; the phase-2 trail manages the exit if it stalls first.
- The expired ARENA:TEST_LIMIT_v1 at 4,182.00 (day high 4,179.72 never reached it; 24-bar TTL elapsed) needs no restage: the macro read is gold-positive on the soft dollar, and the new risk budget is allocated to the uncorrelated SOL long instead.

## 9. Governance and Execution Procedure

1. **Stage (dry run first):**
   `python -m Terminal.Headless.stage_trade_plan docs/trade_plans/OX_ALPHA_62_SOL_Long_20261007.json`
2. **Stage (live, explicit):**
   `python -m Terminal.Headless.stage_trade_plan docs/trade_plans/OX_ALPHA_62_SOL_Long_20261007.json --execute`
   The stager re-validates every section-5 invariant offline, then live-verifies over the signed tunnel: transport health, state freshness (120 s), macro blackout clear, equity cushion above 4,775.00 USD after worst-case stopouts, capacity (fewer than 2 filled; fewer than 5 total resting), quote presence, contract-spec match, passive (non-marketable) entry, and the live-spread friction gate (at most 0.35R). Any failure = NO TRADE, reported, journaled. The muscle re-enforces the risk cap and capacity again on arrival.
3. **Housekeeping:** `python -m Terminal.Headless.stage_trade_plan --purge-expired` cancels lapsed ARENA:PLAN_v1 tickets using the journal at `Data/Omni/brain/plan_journal.jsonl`.
4. **Windows:** the plan itself expires at 2026-10-07 12:00 UTC (staging after that requires a fresh plan from post-event data); the declared blackout 17:00-18:30 UTC brackets the FOMC minutes.

## 10. Invalidation and Reassessment

- **Pre-fill:** if SOL trades through 119.25 before filling (i.e. the structural low breaks decisively), the limit simply rests unfilled and the TTL (or plan expiry) retires it — no chase, no re-quote lower.
- **Post-fill:** management is fully delegated to the ratchet (section 7); the only manual override permitted by doctrine is a macro blackout close.
- **Regime:** a hawkish FOMC-minutes surprise (dissent language on the September hike, renewed hike bias for October 28) invalidates the soft-dollar leg of the thesis — reassess with fresh candle and calendar data before staging anything new (next Tier-1: CPI Oct 14).

## 11. Provenance and Disclaimers

- Candle analytics: `Data/Candles/SOL_15m.parquet` (512 x 15m, telemetry-synced through 2026-10-06 19:30 UTC), Wilder ATR(14).
- Live quotes and macro: the six sources listed in the plan JSON `provenance` block (Economic Times crypto desk, Investing.com XAU/USD, Admiral Markets FOMC preview, VT Markets week-ahead, fedratecalc October calendar, Coinpaper equities desk).
- Account state (balance 4,833.15 / equity 4,839.88 / floor 4,775 / GOLD short #18576872) from the OX_ALPHA_62 specification and the live trader state file.
- This plan is a deliberated risk budget, not a guarantee of profit; the geometry, breakevens and cushions above are the full and honest statement of its edge and its cost.
