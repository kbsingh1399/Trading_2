# Trading Desk Council — Cycle 100

## 1. Ruling, exact provenance and scope

**0 CANDIDATES / 8 WATCHLIST / 16 NO SETUP. No immediate passive staging is certified.**

Research watches: **BTC, ETH, SP500, NAS100, GER40, GOLD, USWTI, USDJPY**. WATCHLIST is not a pending-order instruction. The other 16 assets are NO SETUP in this snapshot, not necessarily permanently untradeable.

- Exact generation: `fb54dfc6a60142a59ba3513985b4b79f`.
- As of: **2026-10-14 14:42:00 UTC**; not a claim of current real-time prices when this report is read.
- Pinned source: [live_snapshot_latest.json at ab45bf2e874a7baa9d2b5732d39fe84f3d2de6a4](https://github.com/kbsingh1399/Trading_2/blob/ab45bf2e874a7baa9d2b5732d39fe84f3d2de6a4/docs/telemetry/live_snapshot_latest.json). The telemetry-changing commit is `dc5bfc86752513d50443b089afa01b73c8ad613a`.
- Snapshot SHA-256: `326e26e61e28606da5d0e6b3dc09a2d5b24fa28cd0576d8fdb2e172edc151663`; 3,995,842 bytes, 141,907 lines.
- Account **5064568**, balance/equity/free margin **4,859.55 USD**, used margin **0**, **0 positions / 0 pending orders**.
- Calendar reports **Fed Beige Book, 2026-10-14 18:00 UTC**, `blackout_active=false`, `blackout_enforcement=DISABLED_BY_OPERATOR`, purge deadline and runway null. This is the snapshot's calendar, not an independent verification of the Fed schedule.
- **Macro enforcement remains permanently disabled. No calendar rejection, timed halt, purge or news-runway restriction is applied.** The stored historical blackout interval is informational only.
- Publication destination: session-fixed **`arena/d6de1eb4-trading-2`**, not requested `arena/5c05910e-trading-2`. The requested source branch still returned the older 13:47:10 generation during retrieval. Later telemetry on the session branch is not silently substituted for this pinned audit.

### Ingestion and rule precedence

All JSON nodes were recursively traversed: **126,599 values/containers**, covering all 24 assets and every telemetry block. Each per-asset block has a type/count/hash inventory in the companion evidence ledger. All supplied OHLCV arrays, CVD records, wall durations, top/nearest band lists, quotes, specs, profiles, funding, traps and global blocks were processed. This is full machine ingestion plus substantive analytical review, **not a claim that every raw JSON line or historical archive sentence was manually interpreted**.

The playbook and installed arena skill/rubric were read; ACTIVE_CONTEXT and complete desk/history files were retrieved and indexed, with relevant loss, policy and current-inventory passages reviewed. The multi-megabyte archive was not exhaustively semantically read. Both the pinned main desk and the requested branch's desk were retrieved. Source hashes and this limitation are retained in evidence.

Current operator instructions override conflicting older playbook passages: 7.50–14.50 USD envelope, crypto 35 bps/TradFi 5 bps ceilings, independent Engine 2 at any Z, RANGE_BOUND/UNDEFINED exclusion, and no macro halts. For Engine 2 the stronger 0.50–0.75 ATR shelf clearance applies, as well as exclusion from every known mapped band; older 0.25 ATR text does not authorize a tight stop. Section 7.4 actual cash friction takes precedence over illustrative historical ticker percentages. No producer authorization token, retired gate module, `gate_g7_eligible` or `htf_history.entry_eligible` is used to select trades.

## 2. Direct telemetry findings that change this cycle

### A. Defense has not been temporally verified

**659 L3 observations and 57 L2 wall records; zero records in either set have `persist_s >=180`. Every recorded duration is zero.** This conclusion is recomputed from raw fields, not from the prompt's eligibility counts. Single-sample observations cannot prove three-minute persistence. A large wall may be real at receipt and still be unqualified as a durable stop shield. This does not prove that every wall was newly placed or that the market has no liquidity.

All supplied source-specific `basis_median` values are null. Spot differences `MT5 mid − source mid` can be calculated and are explicitly labeled **illustrative**, not a calibrated basis distribution. They expose geometry problems but do not certify execution coordinates. DJ30/GER40 lack the external book/basis evidence altogether.

### B. CVD is usable with its actual endpoint—not a fictitious complete 14:42 window

All 14 crypto arrays end with the minute beginning **14:40 UTC**. Their complete 5/15/30-minute windows end **14:41 UTC**. Relative to the root's 14:42 timestamp, the 14:41–14:42 bucket is missing: snapshot-anchored coverage is **4/5, 14/15, 29/30**. Missing data is not zero and partial sums are not complete-window deltas.

Complete-window deltas, **ending 14:41 UTC**, in USD:

| Asset | 5m | 15m | 30m |
|---|---:|---:|---:|
| BTC | −1,008,243.64 | −587,133.55 | +794,354.10 |
| ETH | −2,285,809.87 | −5,035,897.38 | −8,846,825.61 |
| SOL | +8,675.67 | +281,769.99 | −602,314.41 |
| BNB | −47,413.62 | −55,399.03 | −227,792.75 |
| XRP | +89,922.20 | +198,101.06 | −29,690.80 |
| TRX | +48,582.11 | +15,743.90 | −412,641.72 |

BTC's positive 30m is credited; renewed negative fast flow does not demonstrate held absorption. ETH remains dominated by selling across all three observed windows. SOL's positive session CVD and fast recovery do not prove a bearish-regime long or a defended short shelf. All other crypto windows, coverage and aggressor ratios are in evidence.

TradFi flow is **signed broker ticks**, not exchange USD volume. SP500 +35, NAS100 +33, GOLD +55, GER40 +9 and oil +21 are the reported 15m readings; EURUSD −20, GBPUSD −12 and USDJPY +34. Several session/15m/5m values coincide under a 1,000-tick cap. Without window start/end coverage, these are not independent confirmations.

### C. HTF hierarchy must be distinguished from the regime label

Each asset supplies 96 completed 1H and 96 completed 4H bars. Seeded EMA20/50 diagnostics were independently calculated. The 15m EMA200 has a reported 800-bar warm-up; that does **not** supply a warmed 1H/4H EMA200.

- BTC, ETH, SOL, BNB, XRP, ADA, DOGE, DOT, LINK, LTC, AVAX, NAS100, GOLD, SILVER and EURUSD: bearish completed close/EMA20/50 diagnostics on both HTFs.
- GER40, USWTI and USDJPY: bullish on both.
- SP500, DJ30 and GBPUSD: mixed on both despite BEARISH producer labels.
- BCH: mixed 1H/bearish 4H. TRX: bullish 1H/mixed 4H. NEAR: bearish 1H/mixed 4H.

### D. Atomicity and precision findings

The global Hyperdash block is timestamped **14:42:16 UTC**, about 15.53 seconds after the root timestamp. Its aggregate alerts cannot be used as strictly causal evidence at 14:42:00. Receipt-age fields also need recomputation at publication/use, not blind reuse of a FRESH label.

EURUSD and GBPUSD have rounded equal bid/ask and zero `spread_price` while reporting positive spread bps. Their cash friction is **unresolved**, not zero-cost. Today's ETF flows remain null/NOT_YET_REPORTED. Coinbase premium is now reported **−5.13 bps**, rather than Cycle 95's unavailable value; it is context, not an entry trigger.

### E. Remaining telemetry blocks and context

Crypto last funding, in bps, is BTC +0.39, ETH −0.20, SOL −0.14, BNB +0.15, XRP +0.81, ADA +0.02, DOGE −0.03, TRX +0.48, DOT +0.84, LINK +0.49, BCH +1.00, LTC +0.62, AVAX +0.35 and NEAR +1.00. Each has eight funding-history records; predicted rates are unavailable. These modest observations are not proof of a squeeze or broker CFD financing costs. Open interest is a current contracts-level stock, not a verified change in positioning; different contracts must not be aggregated as USD. Crypto exchange 4H and daily arrays provide additional structural context, not a substitute for broker HTF alignment. TradFi equivalents/funding are unavailable, not zero.

All 9,696 supplied candles across the five OHLCV array types passed chronological and high/low/open/close consistency checks. Full prior-day/week auction profiles were considered separately from session volume profiles; both are broker-volume proxies, not exchange volume-at-price footprints. Psychological levels such as BTC 82,000, NAS100 30,300, SP500 7,750 and oil 95 are context only, not substitutes for resting defense. Trapped-trader labels and the producer's `pioneer_microstructure_eval` recommendations were inspected as outputs, not accepted as proof or used as admission shortcuts. Global alert totals are historical aggregates; empty TWAP/hazard arrays do not establish that no such activity exists.

## 3. Mandate 1 — separate engines for all 24 assets

E1 = extreme mean reversion; E2 = trend pullback. Every E2 review independently includes low-Z shelves. The EMA20/50 shelf values below are the supplied **15m** indicators; HTF diagnostics are separately stated. All rows also fail to demonstrate a seasoned stop shield in this exact generation.

| Asset / broker symbol | Engine 1 verdict | Engine 2 verdict | Final |
|---|---|---|---|
| BTC / BTCUSD.pi | Z −2.94 qualifies statistically; bearish HTFs prohibit the dip-buy. Fast selling has resumed, not verified exhaustion. | Bear/bear; EMA20/50 82,835.62 /83,125.20 are distant. A nearer 8.126M raw ask exists at 82,214, illustrative mapped 82,117; duration zero, no held relief. Velocity 0.7025 alone is insufficient. | WATCHLIST |
| ETH / ETHUSD.pi | Z −3.34; bearish long prohibited; all observed CVD windows negative. | Bear/bear; 2,476.08 /2,490.55 shelves are 4.17/5.18 ATR above mid. Velocity 0.3333 but negative retrace, no L3 or L2 wall records. | WATCHLIST |
| SOL / SOLUSD.p | Z −2.89; bearish long prohibited despite positive fast/session flow. | Bear/bear; 105.7991 /106.4516 distant. Raw 5.831M ask 104.45 is a nearer alternative, but single-sample; negative retrace and no confirmed hold. Not rejected by a fabricated universal min-lot cost ban. | NO SETUP |
| BNB / BNBUSD.p | Z −2.79; bearish long prohibited; CVD negative across observed windows. | Bear/bear; 738.2714 /740.2176, first EMA 2.90 ATR away; quiet velocity 0.1856 but negative retrace and no wall defense. | NO SETUP |
| XRP / XRPUSD.pi | Z −3.14; bearish long prohibited; positive fast delta is insufficient. | Bear/bear; 1.3578 /1.3632 distant, no shield. Minimum-lot spread 4 USD already exceeds 15% of maximum risk. | NO SETUP |
| ADA / ADAUSD.p | Z −2.06; bearish long prohibited. | Bear/bear; 0.2309 /0.2328 inspected; velocity 2.0908, no seasoned defense, 92.65 bps and explicit exclusion. | NO SETUP |
| DOGE / DOGUSD.p | Z −1.34: no extreme. | Bear/bear; 0.0824 /0.0830 and POC 0.0835 considered independently. 256.57 bps, 21 USD minimum spread cost, absent defense and exclusion. | NO SETUP |
| TRX / TRXUSD.p | Z +0.92: no extreme; bullish fade short not allowed. | Bull/mixed HTFs; EMA20/POC 0.3325 near, velocity 0.3896 and RSI 50.75 constructive. No primary; 39.04 bps and 13 USD minimum spread cost defeat the case. | NO SETUP |
| DOT / DOTUSD.pi | Z −1.50: no extreme. | Bear/bear; 1.1298 /1.1379 and POC 1.1503 assessed. Velocity 1.2133, no shield, 187.58 bps and exclusion. Low min-lot cash alone does not cure wide spread/volatility. | NO SETUP |
| LINK / LNKUSD.p | Z −3.20; bearish long prohibited. | Bear/bear; 12.6961 /12.7920 distant, velocity 1.7863, no walls; 69.07 bps and exclusion. | NO SETUP |
| BCH / BCHUSD.p | Z −2.91; bearish label/4H preclude a certified dip-buy; no exhaustion/defense proof. | Mixed/bear; 274.5888 /275.8916 distant, velocity 1.3282, no walls. Prior-day VAL 267.57 does not establish a short resistance hold. | NO SETUP |
| LTC / LTCUSD.pi | Z −2.39; bearish long prohibited. | Bear/bear; 60.3714 /60.9268 distant, no shield, 51.06 bps. Minimum spread 3 USD implies at least 20.69% friction. | NO SETUP |
| AVAX / AVXUSD.p | Z −2.53; bearish long prohibited. | Bear/bear; 10.0454 /10.1362 distant; velocity 2.4987, no persistent wall. 30.63 bps passes crypto ceiling, but no held setup. Contract 100, minimum/step 0.01, digits 2. | NO SETUP |
| NEAR / NERUSD.p | Z −2.06; bearish long not certified; mixed 4H and adverse flow. | Bear/mixed; 4.9895 /5.0217 considered; velocity 1.6558, no shield, 61.22 bps and exclusion; 3 USD minimum friction. | NO SETUP |
| SP500 / SP500.p | Z −2.06; current BEARISH label does not authorize an older range-fade thesis. Mixed HTFs, no durable bid absorption. | Mixed/mixed; EMA20/50 7,792.04 /7,804.71 distant; POC 7,777.99. The 9.131M bid at raw 7,744.50 is real sampled depth but zero-duration. Nearby ask 7,777.60 is also unseasoned. | WATCHLIST |
| NAS100 / NAS100.p | Z −1.94: below threshold; bearish long prohibited regardless. | Bear/bear; EMA20 30,422.76 is 2.34 ATR away, POC 30,343.95 nearer. Raw L2 ask 30,287 /1.648M exists, but zero-duration; velocity 1.1336 and buyer ticks do not prove a held rejection. | WATCHLIST |
| DJ30 / DJ30.p | Z −1.06: no extreme. | Mixed/mixed despite BEARISH label; EMA20 51,740.77, POC 51,676.07 and prior VAL 51,653.56 inspected. No external book, walls, bands or basis to certify the required structure. | NO SETUP |
| GER40 / GER40.p | Z −0.54: no extreme, but this does not exclude E2. | Bull/bull; POC 25,339.31 is at market; prior VAH 25,333.30 and weekly VWAP 25,302.52 are relevant. Quiet velocity 0.0303 and buyer ticks credited. Last completed bar closed 25,328.25 below prior VAH; no durable reclaim or external defense proof. | WATCHLIST |
| GOLD / XAUUSD.pi | Z −1.13: no extreme. | Bear/bear; EMA20 4,117.28 is 1.52 ATR away; prior-week VAL 4,111.675 closer. Buyer ticks +55 and velocity 1.1307: relief not yet confirmed rejection. L2 asks individually below 0.75M and all single-sample; no L3. | WATCHLIST |
| SILVER / XAGUSD.pi | Z −1.97: below 2.00; do not round into eligibility. | Bear/bear; 57.5775 /58.2633 distant. Near raw ask 56.610 /0.968M is unseasoned; velocity 1.0981, buyer ticks and 6.39 bps >5. | NO SETUP |
| USWTI / USWTI.p | Z +0.30: no extreme. | Bull/bull; 95.4235 /95.1439, raw primary bid 93.705 (illustrative mapped 95.1235). Velocity 0.2667, RSI 51.64 and positive ticks constructive. Single-sample shield, 5.24 bps, band containment and friction prevent staging. | WATCHLIST |
| EURUSD / EURUSD.pi | Z −1.17: no extreme. | Bear/bear; EMA20/50 1.1157 /1.1179 distant; POC 1.1123 nearby but no defended hold. Velocity 3.4896, no wall records, rounded quote-cost defect. | NO SETUP |
| GBPUSD / GBPUSD.pi | Z −1.96: no extreme. | Mixed/mixed despite BEARISH label; 1.3222 /1.3243 distant; velocity 1.3388. Ten unseasoned L3 observations, no primary; rounded quote-cost defect. | NO SETUP |
| USDJPY / USDJPY.pi | Z +1.36: no extreme; bullish fade short banned. | Bull/bull; EMA20 158.6574 is 1.56 ATR below mid, EMA50 158.5036 farther. Velocity 1.2503, no qualifying primary bid; only threshold L3 primary is a distant ask at raw 160.8. | WATCHLIST |

## 4. Closest hypotheses — why apparent geometry is not an execution card

The following are falsification examples only, using instantaneous basis differences. **They are not broker-validated levels or order instructions.** Full top/nearest raw bands are retained in evidence; duplicate top/nearest references must not be summed as independent fuel.

### SP500: the large bid is not permission to fade the decline

Raw bid **7,744.50 /9.131486M USD** maps illustratively to **7,744.42** at spot basis −0.08. It is single-sample. Completed 1H close/EMA20/EMA50 = **7,759.32 /7,805.7719 /7,805.0266**; 4H = **7,776.23 /7,801.6556 /7,783.3934**. Neither is a confirmed bullish stack, and neither matches strict bearish EMA20<EMA50 confirmation.

A naive stop below mapped [7,739.92,7,749.92], subtracting 0.5 ATR and half-spread, rounds down to **7,734.27**. It falls inside the adjacent **[7,729.92,7,739.92]** band. Thus positive +35 synthetic ticks and a large bid do not overcome archetypes 1/2/4/5. The old 7,764–7,771 peer coordinates are not fresh defense evidence.

### NAS100: a nearby primary-sized L2 ask exists, but is not seasoned

Raw ask **30,287 /1.648400M USD**, illustrative basis **−21.81**, maps to **30,265.19**. This must be credited; “no L3” does not mean no sizeable L2 ask.

Illustrative half-spread short entry **30,264.69** and stop beyond mapped overhead [30,278.19,30,378.19]:

`SL = ceil_tick(30,378.19 + 0.5 ×72.8132 +0.50) = 30,415.10`.

That SL is **inside the next [30,378.19,30,478.19] buy-stop band**, containing **2.343888M USD**. Minimum 0.01 lot × contract 10 ×150.41 distance risks **15.041 USD**, above 14.50 even before other costs. Moving farther out from the same entry cannot fix that minimum-lot failure. Moving entry elsewhere requires a new defended shelf, not arithmetic alone.

The nearer large bid at raw **30,265 /1.288251M** is an opposing barrier to a shallow short; reaching a distant downside stop pool is not automatically payable >=2R. The peer's **24,550–24,620** shelf is a wrong-scale/stale coordinate relative to the current 30,252.69 market and is discarded.

### USWTI: a genuine low-Z research case

Bullish HTFs, RSI near 50, quiet pullback velocity, buyer ticks and a roughly **1M USD** bid are constructive. The raw bid at **93.705** maps illustratively to **95.1235**, close to EMA50 **95.1439**. However it has zero measured persistence.

Using mapped [95.1185,95.2185] as the governing interval:

`SL = floor_tick(95.1185 −0.5 ×0.3578 −0.025) = 94.914`.

This lies inside another known interval **[94.8185,94.9185]**. An illustrative spread-adjusted entry of **95.149** gives a 0.235 stop distance: **0.50 lot risks 11.75 USD**, but spread cost is **2.50 USD /21.28%**. Downsizing does not change that percentage. Current **5.24 bps** separately exceeds 5. Even an attractive distant ask target cannot rehabilitate the invalid stop and unseasoned bid.

### GER40 and GOLD: low Z was not skipped

GER40 is actually near POC/prior VAH in bullish HTFs. Its last completed close broke below prior VAH; current mid has recovered, but a single quote is not a held reclaim. Missing external wall evidence prevents the requested bunker proof.

GOLD's two latest completed closes **4,093.30 →4,097.15** confirm relief toward the resistance zone, not a seller rejection. Nearby L2 asks at raw **4,105.5 /4,106.1 /4,106.2** total about 0.780M, but aggregation does not turn three zero-duration observations into a seasoned primary. Do not invent a duration exemption to increase frequency.

## 5. Peer audit, friction and historical loss corrections

### The blanket altcoin min-lot theorem is not supported

For linear USD-quoted CFDs, minimum spread cash is approximately `spread_price ×contract_size ×min_lot`. If that exceeds **2.175 USD =15% ×14.50**, the instrument cannot pass current friction at any allowed risk even at minimum volume. Passing this necessary bound is not full trade qualification.

| Asset | Minimum-lot spread USD | Minimum possible % of 14.50 risk |
|---|---:|---:|
| DOGE | 21.00 | 144.83% |
| TRX | 13.00 | 89.66% |
| ADA | 10.50 | 72.41% |
| XRP | 4.00 | 27.59% |
| LTC | 3.00 | 20.69% |
| NEAR | 3.00 | 20.69% |
| SOL | 0.23 | 1.59% |
| BNB | 0.007 | 0.048% |
| AVAX | 0.03 | 0.207% |

SOL/BNB/AVAX are counterexamples to the claim that every altcoin necessarily consumes >20% of maximum risk **at minimum lot**. Their actual trade lots, valid stop geometry, volatility friction, defense and payoff must still be assessed. Current SOL spread/ATR is about 30.90%, independently unfavorable under playbook §5; AVAX about 37.27%. DOGE/DOT/ADA/LINK/NEAR remain excluded under the operator's explicit rules. Clean-friction instruments retain research priority without skipping the rest of the mandatory 24-asset review.

### Autopsy lessons retained without repeating numerical errors

- **Archetype 1:** test stop containment against every known source-mapped interval after snapping, not only one selected band.
- **Archetype 2:** negative session flow alone does not prove exhaustion; bearish dip-buys and bullish short fades remain prohibited. Positive fast delta alone does not prove absorption either.
- **Archetype 3:** do not use 0.15 ATR buffers. Apply at least the stronger applicable policy clearance, plus spread/basis uncertainty.
- **Archetype 4:** current single-sample walls cannot establish >=180s defense. Wallet recurrence is not an exchange order ID or proof that liquidity cannot be withdrawn.
- **Archetype 5:** clear shelf overshoot and all adjacent bands; lot downsizing cannot fix a structural failure or a below-minimum required lot.

The supplied SOL example says 108.55 was inside [107.5,108.5]; numerically **it is 0.05 above the upper edge**, not inside. That still does not prove adequate ATR/basis clearance, and reported wall relocation above the stop is a separate valid concern. Historical ticket labels/outcomes are supplied narrative, not freshly reconciled closing-deal receipts. A tight stop raises stop-out susceptibility; it does not mathematically guarantee a loss.

## 6. Mandate 2 — active trades and frozen R0

**Exact snapshot: `active_positions=[]`, empty risk tickets, used margin 0. No running-position ratchet or TP/SL modification is needed.** Frozen initial R0 must be retained for any future active-position analysis, but no stale registry/history entry is treated as live exposure here.

The four historical banked profits in the prompt are not added to balance again. The new snapshot does not provide their native closing receipts. Older context describing BTC #18892038 or SP500 #18892059 as active/pending is superseded by the exact inventory, not fabricated as a new close/cancel acknowledgement.

## 7. Mandate 3 — pending orders

**Exact snapshot: `pending_orders=[]`. No WAIT/MODIFY/DELETE tickets exist.** No pending order was restaged and no macro purge was performed.

## 8. Capital and actionable execution summary

`1.25 ×14.50 +2.00 =20.125 USD` stressed loss per maximum-risk ticket. Preserve full precision rather than multiplying rounded 20.12.

| New maximum-risk tickets | Modeled post-stop equity USD | Surplus above 4,795 USD |
|---:|---:|---:|
| 0 | 4,859.550 | 64.550 |
| 1 | 4,839.425 | 44.425 |
| 2 | 4,819.300 | 24.300 |
| 3 | 4,799.175 | 4.175 |
| 4 | 4,779.050 | −15.950 |

Four open slots do not authorize four maximum-risk orders. Retain the operator's maximum three new-ticket instruction; no orders are proposed here. The initial joint stress is zero. Native proposed-order margin/profit calculations, commissions and correlated fill/gap scenarios remain necessary for eventual staging. **A finite stress formula is not an unconditional capital guarantee against unbounded gaps, slippage or broker failure.**

| Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| STAND ASIDE | — | — | — | — | — | — | — | — | — | — | No complete held-shelf, trend/flow, durable defense, valid stop and net-payoff combination. Single-sample L2/L3, unresolved basis calibration and asset-specific structural/cost flaws; not a macro halt. |

## 9. Five-perspective dialectic and written-rubric tournament

**Implementation disclosure:** the installed `SKILL.md` and `rubric.md` were used for attack/defense, fatal-flaw handling and weighted scoring. No independent Agent/Task runtime or independent judge is available here. This is a **single-assistant five-perspective adaptation**, not a 100-agent tournament, separate peer opinions or verified cross-tab consensus.

1. **Orderflow analyst:** Advocates BTC/SP500 relief research because BTC's 30m delta turned positive and SP500 has a 9.131M bid. Attack: BTC's fast flow is negative, SP500 ticks are not exchange absorption, and every wall duration is zero. Revision: retain research only; acknowledge actual L2 support on NAS rather than declaring it absent.
2. **Structure specialist:** Advocates GER40/oil low-Z longs: bullish HTFs and plausible POC/EMA shelves. Attack: GER40's completed close is below prior VAH; oil needs a deeper defended hold. Revision: neither low Z nor a POC touch is rejected in isolation, but neither is sufficient to stage.
3. **Liquidation forensic:** Tests NAS and oil buffered stops. Attack: each clears one band but lands inside the next; SP500 does likewise. Revision: require interval-wide clearance and revalue the actual executable geometry, not favorable midpoint distances.
4. **Portfolio governor:** Credits cheap index spreads and corrects the universal altcoin theorem. Attack: cheap spread cannot override minimum-lot risk, missing defense or correlated stress. Revision: reserve 20.125 per maximum-risk ticket, no four-ticket maximum-risk book; no macro halt.
5. **Red team:** Challenges the default no-trade verdict: is it merely a retired boolean or a stale peer assertion? Defense: raw durations, independently computed HTFs, complete observed CVD windows and exact containment examples supply substantive reasons. Remaining limitation: no independent judge or full semantic archive reading; no claim of profitability validation.

Criterion order: correctness/completeness/specificity/robustness/clarity, weights **30/25/15/20/10**. Scores are analytical quality judgments, not win probabilities.

| Hypothesis | Criterion scores /10 | Weighted /100 | Fatal for immediate staging? |
|---|---|---:|---|
| H1 Buy BTC/ETH extremes | 2/5/5/1/7 | 35.0 | Yes: countertrend and no verified shield |
| H2 Buy SP500 at large bid | 3/6/7/2/7 | 45.5 | Yes: missing regime/absorption/persistence, invalid naive stop |
| H3 Stage NAS short at nearby L2 ask | 4/7/8/2/8 | 53.5 | Yes: unseasoned defense, contained stop, minimum-lot risk |
| H4 Stage oil long at mapped bid | 4/7/8/2/8 | 53.5 | Yes: containment, friction and persistence |
| H5 Stage GER40 POC long | 5/6/7/2/8 | 52.5 | Yes: no durable hold or external shield proof |
| H6 Short gold's developing relief | 5/6/7/2/8 | 52.5 | Yes: no held rejection/seasoned primary |
| H7 Fill four maximum-risk slots | 1/4/8/0/8 | 33.0 | Yes: modeled buffer breach |
| H8 Remain flat; preserve eight explicit research watches | 9/8/8/9/9 | 86.0 | No identified fatal flaw in the snapshot recommendation |

Written bracket: H2 beats H1; H3 beats H4 on the tie-break (fewer additional cost-ceiling defects); H5 beats H6 on the tie-break (stronger HTF/shelf coincidence); H8 beats H7. H3 beats H2; H8 beats H5; **H8 beats H3** under the rubric's fatal rule. Losing hypotheses remain research hypotheses, not hidden orders. Full criterion arithmetic was checked.

## 10. Institutional schema and payable-frequency improvements

These are **proposals, not deployed production changes or demonstrated profitability gains**.

### A. Causal telemetry and microstructure

1. **Atomic generation manifest:** add per-block `event_time`, `receipt_time`, `available_at`, `source_sequence`, `generation_id`, latency and coverage. Finalize root `as_of` only after all included blocks, or exclude later blocks from historical decisions. This addresses the future-dated global flow block and stale-at-publication FRESH labels.
2. **Durable wall journal:** persist first/last seen and sequence across daemon restarts, with boot ID, outage gaps, samples, observation span, presence fraction, cancellations, replenishment and re-peg links. Investigate zero-duration recurrence as a reset/coverage issue; do not assert a restart cause without logs. Retain wallet/price-level semantics rather than label samples true order-ID L3.
3. **Wallet concentration and directionality:** publish defending-pocket HHI `sum(s_i^2)`, effective count `1/HHI`, two-sided quote share and withdrawal hazard. Discount correlated walls from the same wallet; do not sum repeated top/nearest records.
4. **Multi-level event OFI:** accumulate price-aware bid additions/depletions minus ask additions/depletions by level, normalized by local depth. Publish sequence-gap flags and event counts. Snapshot book imbalance and signed CFD quote ticks are not substitutes for true queue-event OFI.
5. **Microprice drift:** `microprice=(ask×bid_size +bid×ask_size)/(bid_size+ask_size)`; report lagged drift versus mid, spread and ATR, plus depth-impact curves by venue. MT5 execution quotes remain distinct from external predictive microprice.
6. **Queue decay/fill proxy:** where actual exchange queue IDs exist, track ahead-size cancellation/execution hazards; on OTC MT5 publish a clearly labeled fill-probability proxy, not invented queue position. Calibrate partial fills, fill latency and adverse selection.
7. **CVD endpoint contracts:** expose window start/end, expected/observed minutes, forming-bar exclusion, missing buckets and `taker_buy/(buy+sell)` for 1/5/15/30m. Retain separate latest-common complete and root-anchored partial windows. Do not manufacture a 30m TradFi USD series from ticks.
8. **Footprint absorption:** add price-bin buy/sell volume, price response, replenishment and post-sweep hold duration. Normalize aggressive opposite-side volume against volatility-adjusted price displacement; validate subsequent hold out of sample. `TRAPPED_BUYERS_ABOVE` alone is not a footprint.
9. **Multi-scale bands:** retain raw trigger prices, adaptive bin widths, confidence, observed versus inferred type, counts, wallet overlap and unique IDs. The repeated 10-point index/1-unit FX display bins can make naive buffered stops land in adjacent bins. Improve semantics, but do not silently ignore known intervals under the current instruction.
10. **HTF and shelf trajectories:** publish separately warmed 1H/4H EMA20/50/200, seed conventions, last completed times, shelf touch/reclaim times, RSI path and price-normalized pullback velocity. A 96-bar array cannot verify a warmed 200-period EMA.
11. **Native precision and valuation:** serialize quotes as integer broker ticks or decimal strings; require bid/ask/spread consistency. Add profit currency, tick-value profit/loss, commission, swap, freeze levels and proposed-order `order_calc_profit`/`order_calc_margin` receipts. Correct the EUR/GBP zero-spread artifact.
12. **Ledger/calibration hygiene:** reconcile initial-risk registry to current inventory and native deal IDs while freezing original R0. The reported probability lower bound is uncalibrated on 17 outcomes; it is not a validated model-specific probability.

### B. Construct net 2–2.5R without pretending a distant target is payable

For executable-side broker valuations, define loss L and gain G, then:

`R_net = (G − additional_win_costs)/(L + additional_loss_costs)`.

Do not subtract spread twice if it is already embedded in executable entry/exit prices. Require at least 2.0 net R generally, 2.2 for ETH and 2.5 for SOL, with the first material opposing barrier explicitly evaluated.

For linear CFDs, spread friction is approximately `spread_distance /stop_distance`; lot downsizing changes cash risk but not that ratio. First locate a swept-and-held deep shelf and valid stop; then solve the discrete lot grid. If no allowed lot fits 7.50–14.50 USD, reject that geometry. Do not stretch stops merely to dilute friction or place TP beyond unmodeled barriers to manufacture R.

Calibrate clearance from empirical adverse excursion conditional on regime, normalized volatility, depth and residual basis: `buffer=max(policy_floor, conditional_MAE_quantile, adverse_basis_and_spread_allowance)`, with compatible price units and no double counting. Engine 2 retains at least the applicable 0.50–0.75 ATR shelf buffer and every-band clearance. A 1.2 ATR executable stop needs roughly 2.4–3.0 ATR reachable reward plus costs; a 10 ATR target is not necessary if entry is genuinely improved, but no such complete card exists here.

Calibrate TP front-run against conditional fill probability and opposing depth, initially within the mandated 5–10 bps range. If the range itself is economically unsuitable for a narrow FX move, propose a separately tested policy revision—not an undocumented exception. Basis median plus residual quantiles is preferable to a single cross-venue subtraction.

### C. More payable trades, no macro halts

Continuously rank **qualified cards**, not tickers, by fill-conditional expected net USD per margin-time. Optimize limit location, valid stop, front-run target and discrete lots jointly; include unfilled opportunity cost and adverse selection. Enforce joint stress and native margin for every independently fillable ticket, without fake diversification credit for correlated crypto/index exposure.

Priority repairs are persistent wall histories, synchronized basis and quote precision: reducing these evidence gaps can expand legitimately assessable opportunities without weakening the loss protections. Validate by causal walk-forward replay with next-observation fills, spread regimes, fees, partial fills and stop gaps; report sample sizes, uncertainty, turnover, drawdown, net expectancy and same-capital buy-and-hold benchmark. No event-based halt, purge or runway rejection is introduced.

## 11. Verification and publication boundaries

The evidence ledger retains source hashes, global context, all 24 block inventories, raw structural/depth/spec/profile/flow blocks, independent HTF and complete/partial CVD diagnostics, friction arithmetic, classifications, geometry tests and rubric scores. Computational verification checks include exact generation/hash, finite values, candle order/integrity, CVD conservation tolerance, observed coverage, zero-duration wall counts, stop containment and Decimal stress arithmetic. Passing those checks means the computations match the snapshot, **not that the snapshot is defect-free or a trade is authorized**.

Only the council report, evidence ledger and append-only desk entry are publication changes. Existing desk bytes and earlier local-only reports are preserved. No broker order, ratchet, cancellation, runtime policy change, backtest, independent-agent dispatch or external AI-service repair is claimed.
