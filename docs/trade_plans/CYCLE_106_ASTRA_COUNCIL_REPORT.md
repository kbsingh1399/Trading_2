# Cycle 106 — pending ETH unchanged; wall-history discontinuity

## 1. Source scope and council method

**As-of snapshot:** 2026-10-14 **20:40:24 UTC** / October 15 **02:10:24 IST**. Canonical-main commit `d3020d8a84b577e4288f1683ac0376e2d1baefb8`; generation `e13af7f63a4b4473b5f5dc8b5953aca2`. This report supersedes the preceding snapshot assessment only where new observations differ; it is not a live broker-state guarantee at reading time.

All seven requested files were byte-read and SHA-256 checked: telemetry, playbook, canonical desk, active context, session history, arena skill and rubric. **All six context files are unchanged** from the preceding audit; no new history suffix exists. Full telemetry traversal covered **133,829 nodes and all 24 assets**, with per-block inventories, array hashes, candle checks and recomputed completed CVD. Targeted manual review covered inventory, risk, execution, liquidity, HTF/auction shelves, timing and counterexamples. This is **not** a claim of fresh manual line-by-line interpretation of every telemetry leaf. Full source manifests are in `audits/CYCLE_106_EVIDENCE.json`.

An additional pinned snapshot at commit `846791153d9364118d1e76047b1f70ae13f70459`, generation `b6833dccb15b44928f9b842c6946d72f`, **20:39:30 UTC**, was checked for persistence history. Published 20:22:47 evidence was separately hash-guarded. Neither is an independent venue or broker query.

### Five-persona dialectic, before the verdict

**Single-agent adaptation:** no independent agents or models were dispatched. These are analytical lenses, not independent votes.

| Lens | Challenge | Resolution |
|---|---|---|
| Trend / auction | ETH is bear/bear and selling; the largest ask is now inside the order's stop. Does that justify WAIT? | Credit the newly in-range 14.4296M ask. The existing stop remains inside the mapped sweep interval, and friction remains 30.53%. |
| Tape / persistence | Zero seasoned rows means every large wall vanished or is spoofed? | Rejected. Many exact large-wall signatures recur from the preceding audit. Current recurrence histories restarted/discontinued; the mechanism and continuous physical survival are unproven. |
| Execution / geometry | Shrink ETH lots; use deep NAS's high paper R for a new order. | Lot reduction leaves friction unchanged. Deep NAS retains possible reward at a wider distance, but its thin trial stop is contained and its defended retest is unverified. |
| Portfolio | The market is already below ETH's TP, so can the pending reserve be released? | No. The ticket remains pending, not a realized winner. Reserve 13.875 stressed dollars, 1223.75 margin-on-fill and one slot. |
| Adversarial / data integrity | Reuse the last report's positive BTC flow, fast JPY rejection and GOLD composite. | All three are stale: BTC selling returned, JPY velocity improved, and only one leg of the prior GOLD pair remains at those prices. |

Rubric: correctness/completeness/specificity/robustness/clarity, weights **30/25/15/20/10**. Scores judge research approaches, not trade win probabilities.

| Approach | Scores /10 | Weighted /100 | Fatal verified flaw |
|---|---|---:|---|
| WAIT on stronger in-range ETH ask | 2 / 5 / 8 / 1 / 8 | 40.5 | Existing stop and friction breaches |
| MODIFY lots only | 3 / 5 / 7 / 2 / 8 | 44.0 | Does not fix those breaches |
| Inherit prior wall age and admit NAS | 3 / 5 / 8 / 2 / 8 | 45.5 | Unsupported continuity and unsafe selected stop |
| DELETE advice; retain reserve; await fresh defense | 9 / 8 / 9 / 9 / 9 | **87.5** | None found in this as-of research conclusion; live execution remains unverified |

## 2. Verdict and three mandates

**0 new executable candidates; 5 research watches; 19 no-setup assets. Existing ETH #18925596: DELETE recommended, NOT executed.** Inventory remains **0 active / 1 pending**, not flat.

| Mandate | Finding | Action / status |
|---|---|---|
| New setups | No fully qualified dual-engine candidate | No new order cards or placements; watches are not dormant-order authorization |
| Active management | Zero active positions | No active TP/SL ratchets or invented initial R0. If the pending fills, refresh the fill and frozen original risk before active review. |
| Pending management | ETHUSD.pi #18925596, SELL_LIMIT, **1.00 lot**, entry **2447.50**, SL **2457.00**, TP **2425.00** | **DELETE advice only. No cancellation request or broker acknowledgment. Keep risk/margin/slot reserved.** |

Before any separately authorized action, verify that the ticket is still pending. If it has filled, pending-order advice does not substitute for position management. No market order, broker mutation, PR merge or macro purge occurred.

## 3. Pending ETH: update the defense, preserve the rejection

The order is unchanged from its **20:20:12 UTC** creation. Snapshot bid/ask **2417.20 / 2420.10**, mid **2418.65**, spread **2.90 / 11.99 bps**. Entry and volume remain on the serialized broker grid and the sell limit remains above the current ask. Nominal risk passes the operator's 7.50–14.50 range; that is not enough for admission.

**Sweep:** current median basis is **−2.20**, not −2.15. Raw **[2450,2460]** maps to **[2447.80,2457.80]**; the band reports **2,347,725.95 USD**. The existing **2457.00** stop is still inside it. ATR is now **10.3425**, and there is no required outside-edge ATR buffer.

**Friction:** `2.90 / (2457−2447.50) = 30.5263158%`, versus 15% maximum. The 35-bps crypto spread cap passes separately. Changing lots does not change this ratio.

**Reward:** gross `(2447.50−2425)/9.50 = 2.368421R`. At the same entry/target, friction alone requires distance `2.90/0.15 = 19.333333`; the gross-R ceiling then falls to **1.163793**. Do not widen the existing stop and call the same target a compliant repair. No spread double-counting is used to label a fabricated net R.

### Fresh large-ask locations

| Raw ask → broker mapped | Notional | Current recorded span | Relation to this pending order |
|---|---:|---:|---|
| 2439.10 → **2436.90** | **7,395,117.53** | **0s / 1 sample** | Below entry; not overhead protection after a 2447.50 sell fill |
| 2452.20 → **2450.00** | **14,429,638.63** | **131.3s / 2 samples** | **Between entry and SL**; credit its location, but no seasoned current-history defense |
| 2462.00 → **2459.80** | **5,038,492.11** | **0s / 1 sample** | Beyond SL; cannot protect a stop-out that happens first |

The previous report's statement that the largest ask was outside SL **must not be carried forward**. The same large wallet appears again at changed prices/sizes, but wallet identity without order IDs does not prove the same order survived or justify inherited age. Even granting uninterrupted defense, the independent sweep and friction failures remain.

**Unfilled is not profitable:** current ask **2420.10 is below the pending TP 2425.00**, but the order is still unfilled. The intended price area has been reached without an entry; there is no realized reward, no active trailing opportunity, and no reserve release. This observation alone does not make a future sell-limit TP mechanically invalid—it demands a fresh setup review.

ETH 5/15/30-minute taker CVD is now **−373,989.10 / −1,328,144.92 / −2,901,468.11 USD**. The latest completed 20:15–20:30 bar had high **2429.10**, low **2422.70**, close **2423.10**. Current recorded wall histories begin later than that bar. Selling and bearish HTF cannot establish a defended shelf by themselves.

## 4. Account risk and margin: reserve unchanged

Balance/equity **4859.55 USD**; hard floor **4775**; operating minimum **4795**. The source reports `BROKER_VALUED` risk, no valuation errors, and the same pending ticket:

- Nominal loss **9.50 USD**.
- Stressed loss `1.25×9.50 + 2 = 13.875 USD`.
- Pending margin-on-fill **1223.75 USD**.
- Current free margin **4859.55**, modeled after-fill free margin **3635.80**.

Current free margin exceeds the playbook's **4000 USD** reserve criterion; the modeled pending fill does **not** preserve it. The existing ticket nevertheless passes the separate stressed-equity floor test. These are different constraints.

| Additional tickets at 14.50 nominal risk each | Post-stop equity including existing ETH pending | 4795 minimum |
|---:|---:|---|
| 0 | **4845.675** | Pass |
| 1 | **4825.550** | Pass |
| 2 | **4805.425** | Pass |
| 3 | **4785.300** | **Fail** |

Each addition consumes exactly **20.125** stressed dollars. There are three slot openings, but only **two additional full-risk tickets** fit the buffer before margin, correlation and setup checks. None is approved. The 4799.175 flat-book three-ticket scenario becomes relevant only after confirmed cancellation and refreshed otherwise-flat inventory; it is not the current baseline.

## 5. Persistence: observed discontinuity, not proven liquidity disappearance

| Snapshot | L3 rows | L3 recorded span ≥180s | Maximum span | Maximum samples |
|---|---:|---:|---:|---:|
| Prior published 20:22:47 | 1055 | 645 | Earlier histories retained in prior evidence | Earlier histories |
| Adjacent 20:39:30 | 1031 | **0** | **0s** | **1** |
| Current 20:40:24 | 1020 | **0** | **131.3s** | **2** |

Current L2 likewise has **53 rows and zero ≥180s**. Every current recorded L3 `first_seen_utc` is between **20:37:52 and 20:40:05**, after the latest completed 15-minute close at **20:30**.

But **77 exact large-wall signatures**—address, side, price, size and notional—match the published 20:22:47 audit; **75 report shorter spans now**. Examples:

- BTC's **24,999,845.67** bid at raw 81196: prior **3290.9s**, current **76.5s**.
- SP500's **6,285,622.33** ask at raw 7741: prior **1986.9s**, current **72.8s**.
- Several unchanged GOLD asks likewise report reduced histories.

This establishes a **recurrence-history discontinuity/restart in the observations**, not its cause. Collector reset, loss of state, disappearance/reappearance or replacement at identical levels cannot be distinguished from these receipts alone. The adjacent snapshot's all-single-sample state supports the history finding; it does not independently prove a collector restart.

**Do not claim every physical wall is younger than 180s, disappeared, or is spoofed. Do not simply inherit old age either.** Cross-audit recurrence is credited, but uninterrupted survival and price-contact defense are not certified. The setup rejection is not based solely on a producer eligibility flag: unconfirmed contact, geometry, alignment and execution failures were evaluated independently.

## 6. All-24 dual-engine assessment

**Engine 1:** all 24 have `abs(Z)<2`, including NEAR at **1.93**, so none passes the required extreme. Negative CVD alone is not exhaustion. **Engine 2 was separately evaluated despite low Z.** No RANGE_BOUND/UNDEFINED trend setup is admitted.

The HTF diagnostic is independently recomputed close/seeded-EMA20/50 ordering from **96 bars each for 1H and 4H**. It does not verify a fully warmed HTF EMA200. All source blocks were parsed; displayed reasons are decisive findings, not an assertion that every block was manually discussed.

| Asset | Z | 1H / 4H diagnostic | Classification | Engine 2 finding |
|---|---:|---|---|---|
| BTC | -1.21 | bear/bear | WATCHLIST | Bear/bear; selling returned, but primary asks have only 76.5s recorded span, no current-history completed retest. |
| ETH | -1.41 | bear/bear | WATCHLIST | Bear/bear; pending DELETE separately. Larger ask now in range but 131.3s only; sweep and friction failures persist. |
| SOL | -1.25 | bear/bear | NO SETUP | Bear/bear; 5/15m selling, 30m positive; primary span 73.9s and selected-target friction-minimum R below 2.5. |
| BNB | -1.68 | bear/bear | NO SETUP | Bear/bear; no seasoned primary; velocity 1.009 and positive 5/15/30m flow do not confirm seller defense. |
| XRP | -1.46 | bear/bear | NO SETUP | Minimum-lot spread cost 3 USD still exceeds 2.175 USD maximum budget; no seasoned defense. |
| ADA | -0.87 | bear/bear | NO SETUP | Explicit ban; spread and minimum-lot friction also fail. |
| DOGE | -0.54 | bear/bear | NO SETUP | Explicit ban; spread and minimum-lot friction also fail. |
| TRX | +0.55 | bull/mixed | NO SETUP | Bull/mixed HTF; 9 USD minimum-lot spread cost and no seasoned defense. |
| DOT | -0.17 | bear/bear | NO SETUP | Explicit ban; 185.76 bps exceeds crypto cap. |
| LINK | -1.21 | bear/bear | NO SETUP | Explicit ban; 69.40 bps exceeds crypto cap. |
| BCH | -1.30 | bear/bear | NO SETUP | Bear/bear; no seasoned 5M primary ask or independently verified defended shelf. |
| LTC | -0.69 | bear/bear | NO SETUP | 50.33 bps exceeds crypto cap; minimum-lot spread cost 3 USD exceeds 2.175 USD. |
| AVAX | -0.87 | bear/bear | NO SETUP | Spread now 40.36 bps, above 35; no seasoned primary defense. |
| NEAR | -1.93 | bear/mixed | NO SETUP | Explicit ban; 69 bps, minimum-lot cost and mixed HTF also fail; abs(Z)=1.93 is still below 2. |
| SP500 | -1.16 | bear/mixed | WATCHLIST | Bear/mixed HTF; 72.8s primary span, buyer tick flow, latest high below EMA20 and primary; nearby target not payable at 2R. |
| NAS100 | -1.44 | bear/bear | WATCHLIST | Bear/bear; three ask shelves examined, all 131.1s. Near targets fail 2R at index floor; deeper paper reward lacks safe stop/retest. |
| DJ30 | -0.16 | bear/mixed | NO SETUP | Bear/mixed HTF and no seasoned primary defense. |
| GER40 | -1.74 | mixed/bull | NO SETUP | Mixed/bull HTF conflicts with bearish producer regime; no permitted aligned direction confirmed. |
| GOLD | -0.55 | bear/bear | WATCHLIST | Bear/bear; old 4113.5/4113.8 pair no longer intact, qualifying individual asks only 84.8s; no completed current-history retest. |
| SILVER | -1.38 | bear/bear | NO SETUP | 6.48 bps exceeds TradFi 5 bps cap; no seasoned defense. |
| USWTI | -0.15 | bull/bull | NO SETUP | Bull/bull, velocity 0.0306; no seasoned primary, mixed tick flow and fresh support-to-POC friction/reward failure. |
| EURUSD | +0.03 | bear/bear | NO SETUP | Bear/bear; no seasoned ask; equal rounded bid/ask and zero price spread conflict with 0.45 bps. |
| GBPUSD | -0.46 | bear/bear | NO SETUP | Bear/bear; no seasoned ask; equal rounded bid/ask conflict with nonzero 0.0001 price spread and 0.61 bps. |
| USDJPY | -0.71 | mixed/bull | NO SETUP | Velocity improved to 0.6154; reject for mixed/bull HTF, bearish producer regime and missing seasoned support, not stale fast-velocity failure. |

Explicit bans remain DOGE/DOT/ADA/LINK/NEAR. At maximum nominal risk, the spread-cost budget is exactly **2.175 USD**, not rounded 2.18. XRP's minimum-lot cost improved from 4 to **3 USD**, but still fails. ADA/DOGE/TRX/LTC/NEAR also fail that bound. AVAX's spread now independently breaches the crypto cap.

### Focus updates

- **BTC:** 5/15/30-minute CVD is now **−664,912.87 / −1,993,529.24 / −1,781,324.07 USD**, reversing the preceding audit's positive flow. That supports selling pressure, not automatic exhaustion. The nearer 6.097M raw 82000 ask maps to **81924**; the 8.978M raw 82164 ask maps to **82088**. Both report 76.5s. Latest completed high **81889** is below both. No completed retest with the current recorded history is demonstrated.
- **SOL:** 5/15-minute flow is **−11,423.67 / −79,143.52**, while 30-minute remains **+28,736.72**. Do not reuse the prior all-positive description. The >5M primary ask still has only 73.9s recorded span and poor friction-compliant target economics.
- **SP500:** EMA20 **7722.5059**; latest high **7719.01**; primary mapped ask **7740.91**, **6.286M / 72.8s**. H4 remains mixed; tick CVD +37/+37. A prior EMA brush is not current primary defense. The reported raw [7700,7710] concentration is **4.082009B**; it is not newly discovered or independently authenticated in this audit. Trigger semantics and notional provenance still require care.
- **NAS100:** current mapped asks **29960.715 / 30022.715 / 30192.715**, approximately **1.049 / 1.080 / 1.029M**, all **131.1s**. Latest completed high **29933.65** is below all three. Negative tick CVD −17/−17 is not a shelf-hold substitute.
- **GOLD:** of the prior raw 4113.5/4113.8 pair, only **4113.8 / 453,101.75 USD** remains at those exact prices. Do not retain the old 789,533.81 composite. Individual qualifying asks at raw **4126.1 / 4138.2** exist but record only **84.8s**. Price remains near broker POC 4099.5908; that alone does not establish overhead seller defense.
- **Oil:** bull/bull, Z **−0.15**, velocity **0.0306**, spread **4.83 bps**. These are positives, not automatic rejection for small Z. Current tick flow is mixed: **−5 over 5m / +7 over 15m**. EMA20/50 **95.3889 / 95.3169**, POC **95.4852**. The fresh raw 93.815 bid maps to **95.18375**, is only **202,145.62 USD**, and is single-sample. Its recorded first sighting follows the completed candle, so the earlier candle's low/close cannot prove that particular wall held.
- **JPY:** velocity improved from 1.0663 to **0.6154**, so the previous fast-pullback rejection is removed. Producer regime remains bearish while HTF is mixed/bull. Missing verified seasoned support and alignment still prevent either direction; a far-away 1.608M ask at raw 160.8 does not defend local support.

## 7. Fresh geometry tests — not executable cards

These are **unrounded research counterexamples**, not broker instructions. Current median bases translate foreign-venue levels once. Broker EMA/profile levels are not translated twice. Short targets front-run the selected lower magnet's upper edge by 5 bps; the oil target front-runs broker POC by 5 bps. Trial stops clear the selected edge by 0.50 ATR plus half-spread and are then checked against **all known deduplicated intervals**. They fail because clearing one interval is not clearing its neighbors.

| Example | Mapped entry | Trial stop | 5-bps target | Gross R | Friction | Containing raw interval |
|---|---:|---:|---:|---:|---:|---|
| BTC near | 81924.00000 | 82156.35770 | 81664.8120000 | 1.1155 | 6.8859% | [82200, 82300] |
| BTC primary | 82088.00000 | 82256.35770 | 81564.7620000 | 3.1079 | 9.5036% | [82300, 82400] |
| ETH in range primary | 2450.00000 | 2464.42125 | 2419.0089000 | 2.1490 | 20.1092% | [2460, 2470] |
| SOL primary | 105.82250 | 106.27670 | 103.9344412 | 4.1569 | 50.6385% | [106, 107] |
| SP500 primary | 7740.91000 | 7755.39025 | 7723.7699550 | 1.1837 | 2.3480% | [7750, 7760] |
| NAS100 nearest | 29960.71500 | 30017.43325 | 29898.6568575 | 1.0941 | 2.1510% | [30000, 30100] |
| NAS100 primary | 30022.71500 | 30117.43325 | 29898.6568575 | 1.3098 | 1.2880% | [30100, 30200] |
| NAS100 deep | 30192.71500 | 30217.43325 | 29898.6568575 | 11.8964 | 4.9356% | [30200, 30300] |
| GOLD primary | 4122.32500 | 4130.02645 | 4078.2631125 | 5.7212 | 2.5969% | [4130, 4140] |
| USWTI subthreshold | 95.20675 | 94.99970 | 95.4374574 | 1.1143 | 22.2169% | [93.6, 93.7] |

Every displayed trial stop is contained in another known mapped interval. Equity-index total spacing must also meet the playbook's **1.5 ATR** guard: **15.93075** for SP500, **99.32475** for NAS100. At that minimum, selected-target R is **1.0759** for SP500, **0.6248 / 1.2490** for near/middle NAS, and **2.9606** for deep NAS. Do not falsely reject every deep geometry on reward alone; the deep example still lacks a safe demonstrated stop and retest.

The fresh ETH primary example has **2.1490R / 20.1092% friction**, below the playbook's 2.2R ETH target requirement and above the friction cap. Oil gives **1.1143R / 22.2169% friction**. SOL's attractive thin-stop gross R does not survive the friction minimum. These selected failures do not prove every conceivable future geometry impossible; they establish that no displayed example is an executable card. Any future card needs tick rounding, discrete lot sizing, native broker profit/margin receipts, minimum stop/freeze checks and joint-book recalculation.

## 8. Timing, precision, calibration and institutional improvements

- Generation start **20:40:03.736 UTC**, root **20:40:24.241**; both completed-minute cutoffs are **20:40:00**. All crypto 1/5/15/30-minute grids are complete and both cutoff calculations agree. Grid coverage is not an independent upstream finalization receipt.
- Latest completed 15-minute close is **20:30**. No invalid OHLC, nonmonotonic bar timestamps or candle close beyond the serialized cutoff was found. Global-flow receipt is **3.81499 seconds after root**; the observation is not atomic across blocks.
- Quotes older than ten seconds include XRP **22.87s**, DOGE **13.60s**, TRX **18.04s**, DOT **22.96s**, LINK **14.47s**, LTC **11.43s**. Refresh quotes for execution; do not reuse the prior stale-symbol list.
- EURUSD has equal serialized bid/ask and zero price spread but **0.45 bps**. GBPUSD also has equal serialized bid/ask, yet reports **0.0001** price spread and **0.61 bps**. The prior statement that both price-spread fields are zero is no longer true; **both remain precision-inconsistent**. No exact admission lots or zero-cost execution are inferred.
- Producer win lower bound **0.4197**, from **11 wins / 17 observations**, is explicitly **uncalibrated**, with minimum sample 100. The council rubric is not a substitute probability estimate or validated positive expectancy.

### Prioritized changes recommended, not silently deployed

1. **Persist wall-history state with an epoch and reset reason.** Emit collector/process ID, warm-start status, state-restoration checksum, gaps and reset events. Test that a restart cannot silently turn an old recurring level into an apparently new wall or trigger unsupported age inheritance.
2. **Track order identity and contact chronology separately.** Preserve order IDs where available; otherwise label wallet/level signatures as recurrence, not queue continuity. Emit first/last seen, presence denominator, missing intervals, re-peg trajectory, refill/consumption and bid/ask touch times. Do not infer a fill-time defender from a same-wallet historical row.
3. **Inventory-first pending lifecycle.** Keep observed pending reserve until broker acknowledgment plus refreshed inventory. Distinguish recommendation, request, acknowledgment, pending removal and actual fill. A price crossing an unfilled order's TP is not realized P&L.
4. **Recompute geometry and economics together.** Rebuild mapped interval unions, round executable stops outward, verify all edge buffers, then recalculate target obstacles, friction, discrete lots, frozen initial risk and margin. Do not repair wide safe stops by silently reducing their structural distance.
5. **Native precision and time-coherent receipts.** Preserve broker-native FX decimals, exact tick values/currency conversion, per-block timestamps and finalized CVD watermarks. Obtain adequately warmed HTF histories. Validate oversized trigger notional/side semantics rather than automatically treating every bucket as executable forced-flow fuel.

This turn adds a **read-only audit, report, evidence and tests**, not a production trading-engine change.

## 9. Five loss archetypes and macro policy

| Archetype | Concrete defense |
|---|---|
| Stop inside sweep | ETH SL containment rechecked with new basis; every research stop checked against deduplicated interval sets |
| Countertrend | No bearish-HTF longs or bullish-HTF shorts; SP/DJ mixed and GER/JPY conflicts remain unresolved |
| Inadequate buffer | Existing ETH stress and slot retained; three additional full-risk tickets fail 4795 |
| Ephemeral / misidentified wall | History discontinuity diagnosed without alleging physical withdrawal; no inherited age, old GOLD composite or same-wallet continuity assumption |
| Pullback overshoot | Require actual shelf touch/hold and defended liquidity; small Z or improved JPY velocity alone cannot qualify a trade |

Macro blackout enforcement remains **DISABLED_BY_OPERATOR**. The snapshot still lists Bowman Bangkok at **2026-10-15 02:55 UTC**. There is **no news veto, purge, blackout or runway-based rejection**; event context was not independently queried here. ETH DELETE rests on structure/execution, not the calendar.

## 10. Reproduction, append safety and publication scope

```text
python docs/trade_plans/audits/cycle106_audit.py SOURCE_DIRECTORY ADJACENT_SNAPSHOT OUTPUT_JSON
python -m unittest discover -s docs/trade_plans/audits -p 'test_*audit.py'
```

Durable files: this report; `audits/cycle106_audit.py`; `audits/CYCLE_106_EVIDENCE.json`; `audits/test_cycle106_audit.py`; one append to `LIVE_COLLABORATIVE_ORDER_DESK.md`. Preserve the entire **3,589,567-byte** pre-Cycle106 local desk prefix, SHA-256 **3373a7485116e4805f73245aad12364337e3e2ee1303af001fc317f655bef337**, plus the canonical-main prefix. Large raw source downloads remain outside tracked deliverables.

Publish only to `arena/66c9be42-trading-2` / PR #2. **Main untouched; no PR merge and no broker action.** Executed test and publication receipts are provided with delivery rather than assumed from report creation.
