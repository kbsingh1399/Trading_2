# Trading Desk Council — Cycle 92

## Executive verdict

**0 CANDIDATES / 9 WATCHLIST / 15 NO SETUP. Stage no new orders. Escalate existing BTC ticket #18892038 for structural-risk review; do not certify its current stop as a safe bunker. No mechanical ratchet is triggered, no automatic stop widening or target extension is justified, and no broker action was performed. Pending inventory: zero.**

This is an as-of analysis, not a streaming market assessment. An expired snapshot cannot authorize a subsequent order. WATCHLIST means a research direction, not a dormant execution instruction. The platform's transient AI-service error did not erase the saved audit; this report resumes that work, without claiming to repair the external service.

## 1. Ingestion, provenance and rule precedence

### Exact source recovered and distinguished from newer data

- Requested telemetry: **generation `d6da745fa2054555ac2b8cccfbdc8dd8`, as of 2026-10-14 11:00:24 UTC**, recovered through GitHub's API from commit [`49aa55fdb434bbf92a8e4923249c69ea5495c0a6`](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json). SHA-256: `e04cd120c2ef23b5fb0093e16dbfdda9a6d2e1bfec3c9bb4cd74a3a88995f2f6`. Size: 4,319,988 bytes; 149,300 text lines.
- The initially checked-out telemetry was **a different generation**, `417a67595077407c9609c4c0531f52fb`, at **11:05:27 UTC**, from base commit `3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24`. It is not overwritten or silently substituted into the Cycle 92 matrix.
- Playbook: [`docs/specs/TRADE_DECISION_PLAYBOOK.md`](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/docs/specs/TRADE_DECISION_PLAYBOOK.md), including §§3, 5, 7.1–7.4. Context: [ACTIVE_CONTEXT](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/.agents/rules/ACTIVE_CONTEXT.md), [session history](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/.agents/memory/session_chat_history.md), and [order desk](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md).
- The requested `arena/5c05910e-trading-2` desk was separately retrieved at remote commit `18902133bf4397b2dc821ed703fb3e061ca26783`; its bytes match the local pre-append desk. This session writes/pushes **only `arena/d6de1eb4-trading-2`**. No branch switch, main push, other-tab dispatch, or cross-branch synchronization is implied.
- Supplemental initial-risk ledger [`Data/initial_position_risk.json`](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/Data/initial_position_risk.json) confirms BTC's original SL 82,213 and frozen R0 1,010.

**Reading scope, stated accurately:** all required files were loaded completely for byte-level/line-indexed inspection; all JSON values were recursively traversed, with substantive per-asset and all-block analysis. The playbook, context and skill/rubric were substantively reviewed; the multi-megabyte historical desk/chat archives were fully indexed and relevant chronology/autopsies reviewed. This is not a claim of manually interpreting every one of roughly 74,000 historical archive lines. A literal human-style full-line reading of those archives and an independent-agent tournament were not completed. The accompanying evidence ledger records complete-source hashes, per-asset block coverage and calculated diagnostics, rather than substituting a copied prompt matrix for telemetry.

### What the exact snapshot actually says

| Item | User-supplied baseline | Requested 11:00:24 snapshot | Local 11:05:27 snapshot |
|---|---:|---:|---:|
| Balance USD | 4,869.65 | 4,869.65 | 4,869.65 |
| Equity USD | 4,870.70 | **4,871.20** | 4,870.36 |
| BTC position mark | 83,328 | **83,378** | 83,294 |
| BTC floating PnL USD | +1.05 | **+1.55** | +0.71 |
| Open / pending | 1 / 0 | 1 / 0 | 1 / 0 |

The exact snapshot's BTC quotes are bid **83,359**, ask **83,375**, mid **83,367**. Its position mark is a separately sampled observation, not a simultaneous executable quote. No arithmetic blends those observations.

The calendar reports **CPI at 12:30 UTC**, **`blackout_active=False`**, blackout **12:00–13:00 UTC**, purge **11:55 UTC**. At the requested timestamp this leaves **59m36s to blackout, 54m36s to purge, and 89m36s to release**. The earlier Bowman blackout having lifted does not remove CPI risk. Playbook §5's two-hour runway is not met. The calendar is repository-reported coverage, not independent verification of an official external calendar. Every asset is nevertheless analyzed below; macro is not used to skip the search.

### Explicit conflicts resolved

1. Current user instructions override older playbook language where they conflict: risk **7.50–14.50 USD**, §7.4 dynamic friction, §7.1 frozen-R0 ratchets, and **neither engine in RANGE_BOUND/UNDEFINED**. Playbook §7.3 instead makes Engine 1 range-only; both statements cannot be simultaneously obeyed. This report uses the user's current regime instruction and explicitly declines to claim universal, contradiction-free playbook compliance.
2. Engine 2 is evaluated independently at low absolute Z. Low Z never disqualifies Engine 2. Engine 1 needs an actual extreme plus exhaustion and permitted direction.
3. For Engine 2, the stronger **0.50–0.75 ATR shelf buffer** is retained, with the stop also outside known opposing bands and at least the general outer-edge buffer. A shelf buffer is not a replacement for a band-edge check.
4. Primary wall sizes: crypto 5M, indices 1M, commodities 0.75M, FX 0.50M USD; persistence evidence at least 180s. The broad crypto threshold in the current mandate is used for non-major crypto, where earlier wording specified majors only. Static example friction percentages are not contemporaneous calculations.
5. `trade_authorization`, `pioneer_microstructure_eval`, and retired `gate_g7_eligible` are recorded as producer annotations, **not used as trade-selection engines**. No retired decision-gate module was run. Required price/flow/risk evidence is independently analyzed.
6. A finite stressed-loss formula cannot guarantee an unconditional equity floor through unbounded gaps, broker failure or stop slippage. The stated capital invariant is a **modeled stress constraint**, not guaranteed capital protection.

## 2. Mandate 1 — separate two-engine assessment of every asset

All prices in this table are broker indicator/quote coordinates. External walls/bands are venue-mapped separately in the evidence appendix. The 15m EMA pair is not mislabeled as an independently warmed 1H/4H EMA stack. There are 95 completed 1H and 96 completed 4H bars per asset; diagnostic EMA20/50 are computed from those histories, but a fully warmed HTF EMA200 cannot be certified from them. Single RSI observations do not prove a return path toward 50.

| Asset / MT5 symbol | Engine 1 — extreme mean reversion | Engine 2 — trend pullback, independently evaluated | Final |
|---|---|---|---|
| BTC / BTCUSD.pi | **No trigger:** Z −0.25; not extreme. | Published BULLISH, but completed 1H/4H structures mixed; EMA20/50 83,362.7076 / 83,380.0232, VAL 83,121.38, weekly VWAP 83,104.9488 considered. Local CVD improves despite deeply negative session; velocity 1.4168 and no seasoned primary. Existing stop containment is a separate risk problem. | **WATCHLIST** |
| ETH / ETHUSD.pi | **No trigger:** Z +0.03. | BEARISH; 1H/4H close below EMA20 below EMA50 supports relief-short research. EMA50 2,503.0413 / VAH 2,508.732. Velocity 1.8586 and positive observed 5/15m CVD do not establish a quiet failed rally; 6.02M/11.75M asks are single observations. | **WATCHLIST** |
| SOL / SOLUSD.p | **No trigger:** Z −0.21; bearish-regime dip-buy prohibited. | BEARISH on both diagnostic HTFs; EMA50 107.0262 / VAH 107.6318. Positive session, weekly and local CVD oppose an immediate short; velocity 1.298. Primary 6.38M ask is unseasoned and mapped 108.75 is 3.88 ATR away. Need a held short shelf and net ≥2.5R. | **WATCHLIST** |
| BNB / BNBUSD.p | **No trigger:** Z −0.44. | BEARISH HTFs; EMA50 741.9045 / POC 743.943 / VAH 744.252. Bullish local CVD and velocity 1.0471 do not prove rally exhaustion; ten unseasoned L3 rows are not a primary shield. | **WATCHLIST** |
| XRP / XRPUSD.pi | **No trigger:** Z +1.43 and RANGE_BOUND. | RANGE_BOUND excludes trend entry; POC 1.3682 / VAH 1.37 still inspected. No L3 primary. Minimum 1 lot × 1,000 contract × 0.004 spread = **4 USD friction**, at least **27.59%** of a 14.50 risk budget. | **NO SETUP** |
| ADA / ADAUSD.p | **No trigger:** Z −0.22. | BEARISH; EMA50 0.2345 / VAH 0.2366 could be relief shelves, but current bullish local flow/no seasoned wall and **93.70 bps** spread fail; minimum-lot friction 11 USD, ≥75.86% of maximum risk. Operator-excluded. | **NO SETUP** |
| DOGE / DOGUSD.p | Z **+2.77 is numerically extreme**, but RANGE_BOUND prohibits both engines; no backed exhaustion proof. | No directional regime; EMA50 0.0834 / VAH 0.0838 do not create a trend. **248.96 bps**, minimum friction 21 USD, ≥144.83% of maximum risk. Operator-excluded. | **NO SETUP** |
| TRX / TRXUSD.p | **No trigger:** Z +1.47; bullish-regime short fade prohibited. | BULLISH label; EMA20/50 0.3320 / 0.3306. RSI 69.4 and velocity 2.8284 are not a quiet returning pullback; 4H stack mixed. Credit a 0.513M recurrent L2 bid, but it is not 5M primary support. Minimum friction **10 USD / 14.50 = 68.97%**. | **NO SETUP** |
| DOT / DOTUSD.pi | **No trigger:** Z −0.76. | BEARISH; EMA50 1.1441 / VAH 1.1674 checked, not rejected for Z. Local CVD positive, velocity 1.6347, no primary wall; **184.45 bps** and explicit operator exclusion remain. The historical 122% friction figure is not recomputed as current fact. | **NO SETUP** |
| LINK / LNKUSD.p | **No trigger:** Z +0.35. | BEARISH; EMA50 12.8768 / VAH 12.9447. Negative local CVD favors short-side research but does not cure **68.94 bps**, absent primary defense, velocity 1.234 or operator exclusion. BEARISH_EXHAUSTION alone is not a short-entry signal. | **NO SETUP** |
| BCH / BCHUSD.p | **No trigger:** Z +0.11. | BULLISH label; EMA20/50 277.8232 / 277.0690, quiet velocity 0.2704 and positive local CVD credited. However 4H close 277.66 lies between EMA20 276.8868 and EMA50 284.8297; recurrent 0.151M L2 is an **ask**, not the long shield. | **NO SETUP** |
| LTC / LTCUSD.pi | **No trigger:** Z +0.32. | BEARISH; EMA50 61.4309 / VAH 61.7922. Positive fast CVD/velocity 1.3505, no seasoned wall; spread **48.72 bps**. Minimum friction 3 USD, ≥20.69% of maximum risk. | **NO SETUP** |
| AVAX / AVXUSD.p | **No trigger:** Z −0.49. | BEARISH HTFs; EMA50 10.2156 / POC 10.2173 / VAH 10.313 explicitly considered. Velocity **2.2437**, positive local CVD, no primary wall, and broker stops_level 20 × point 0.01 require structural re-evaluation; no held shelf. Correct contract 100, min/step 0.01. | **NO SETUP** |
| NEAR / NERUSD.p | **No trigger:** Z +0.09. | BEARISH label but 4H EMA20 above EMA50; EMA50 5.0444 / VAH 5.0718 checked. Fast negative delta is not sustained across 15/30m. No shield, **59.21 bps**, minimum friction 3 USD (≥20.69%); operator-excluded. | **NO SETUP** |
| SP500 / SP500.p | **No trigger:** Z +0.28. | BULLISH completed 1H/4H; EMA50 **7,816.7681**, 1H EMA20 **7,813.1026**, VAH 7,814.4472 as a possible retest shelf. Quiet velocity 0.2141/L2 +0.4606 are favorable, but −81 synthetic ticks, unseasoned 1.638M bid and adjacent stop bands defeat certification. | **WATCHLIST** |
| NAS100 / NAS100.p | Z **−2.23** is extreme, but a mean-reversion long opposes BEARISH regime/4H and seller flow: **prohibited**. | Relief SHORT researched at EMA20/50 **30,572.5438 / 30,575.9977**, POC 30,550.3151. Quiet velocity 0.0905 and 1.0003M recurrent L2 ask are credited. 1H last close is marginally above EMA20, and one-band stop sizing already exceeds risk at the nearest qualifying wall; adjacent bands worsen it. | **WATCHLIST** |
| DJ30 / DJ30.p | **No trigger:** Z +0.68. | BULLISH HTFs; EMA50 51,802.4485 / prior-day POC 51,820.484 checked. Seller aggression and velocity 1.1489; **no observed depth, walls, basis or stop/liquidation bands**. Cheap spread is not a complete setup. | **NO SETUP** |
| GER40 / GER40.p | **No trigger:** Z +1.99 is below 2.00; do not round it into eligibility. Short fade also conflicts with BULLISH trend. | Bullish HTFs, buyer ticks, EMA20 **25,369.9426**, EMA50 **25,343.6847**. Mid 25,416.65 has not demonstrated a held deep pullback. No depth/wall/band/basis evidence. | **NO SETUP** |
| GOLD / XAUUSD.pi | **No trigger:** Z −1.89; bearish dip-buy prohibited even if subsequently extreme. | BEARISH HTFs, seller ticks. EMA20/50 **4,147.5259 / 4,153.7067** examined. Velocity **3.3781** not quiet; qualifying-size mapped ask **4,163.82** is unseasoned and **4.09 ATR** from current mid, beyond a near-term passive shelf. | **WATCHLIST** |
| SILVER / XAGUSD.pi | **No trigger:** Z −1.70, bearish dip-buy prohibited. | BEARISH HTFs; EMA20/50 **58.6670 / 58.9027**, prior-day VAL 60.1937 considered. Low velocity 0.0565 is favorable but **buyer aggression**, no seasoned primary and **6.16 bps > 5** prevent certification. | **NO SETUP** |
| USWTI / USWTI.p | **No trigger:** Z +1.91; bullish trend forbids short fade. | BULLISH HTFs. EMA20/50 **94.8831 / 94.7551** are **2.35 / 2.77 ATR** below current mid, not immediately stageable under §3 proximity. Mapped 1M bid **95.26275** is nearer but unseasoned; stop/target bands and mapped ask 95.89575 compress payoff. | **WATCHLIST** |
| EURUSD / EURUSD.pi | Z **−2.23** is extreme, but RANGE_BOUND prohibits both engines. | No confirmed trend; POC 1.1192 / VAL 1.1184 examined. Seller ticks and no seasoned primary. Five-digit quotes are rounded to four decimals; apparent zero spread is **not** verified free execution. | **NO SETUP** |
| GBPUSD / GBPUSD.pi | **No trigger:** Z −0.24. | BULLISH diagnostic HTFs; EMA20/50 **1.3265 / 1.3263**, quiet 0.1169 velocity, RSI 52.43, positive tick flow and OFI 0.016 are favorable. But largest L3 bid only **0.13255M**, recurrent L2 is an ask, bands too coarse and quotes rounded. | **WATCHLIST** |
| USDJPY / USDJPY.pi | **No trigger:** Z +1.03. | BULLISH label; EMA20/50 **158.3858 / 158.3468**, weekly VWAP 158.3337 checked. 1H EMA20 **158.328698 < EMA50 158.330294** is not aligned bullish. Largest relevant L3 bid 0.3165M; recurrent L2 bid 0.1609M, both below 0.50M primary. USD conversion needed. | **NO SETUP** |

### Flow and wall evidence: do not collapse horizons or venue types

There are **1,045 L3 rows**, all `persist_s=0`, `samples=1`, `SINGLE_SAMPLE`. Their wallet attribution is Hyperliquid, **not proof of Ethereum-chain limit orders or full order-ID L3**. There are **69 L2 wall rows**; 21 have elapsed `persist_s >=180`, so “all walls have zero persistence” would be false.

- **NAS100:** L2 ask 30,565, **1,000,294.64 USD**, span **219.1s**, presence **0.75**. Credit the numerical notional/duration thresholds. The observations do not prove uninterrupted defense; gaps/re-pegs require inspection. Regardless of that uncertainty, map by −18.545 to 30,546.455; one-band 0.50 ATR + half-spread SL 30,700.50 would cost **15.4045 USD at minimum 0.01 lot**, above 14.50, and sits in the next band [30,681.455,30,781.455]. Not a valid order.
- **TRX:** recurrent L2 bid 0.3330, **513,488.36 USD**, 1,770.1s, presence 0.8846. Credit it rather than applying an old eligibility boolean. It is below the adopted crypto primary threshold and minimum-lot friction independently fails. The 0.3325 bid is labeled persistent, but only 186,823.20 USD.
- **BCH / GBPUSD:** recurrent L2 walls are asks of 150,853.82 / 151,152.96 USD, not primary support for their proposed longs.
- **USDJPY:** recurrent bid is 160,899.11 USD; larger recurrent ask 460,843.20 USD is wrong-side long defense.

Crypto minute arrays contain 58 observations, ending at **10:58 UTC** (bucket ends 10:59). The last completed minute before the root timestamp, **10:59–11:00**, is absent. True snapshot-anchored 5/15/30m windows contain **4/14/29 observations**, not 5/15/30. Never impute that missing minute as zero. The following are sums of the **last observed** contiguous 5/15/30 buckets ending 10:59, distinctly labeled as lagged:

| Asset | Last observed 5m USD | 15m USD | 30m USD | Interpretation |
|---|---:|---:|---:|---|
| BTC | +793,101.73 | +1,367,053.47 | +2,087,170.95 | Previous observed 5m −666,124.02: genuine local improvement, not proof of price absorption or HTF trend repair. |
| ETH | +37,784.88 | +125,099.19 | −156,072.13 | Mixed horizons; immediate short needs failed rally, not label-only conviction. |
| SOL | +38,203.24 | +174,284.23 | +205,306.37 | Opposes immediate relief short. |
| BNB | +30,356.57 | +147,598.77 | +152,306.85 | Buyers active locally despite bearish HTFs. |
| LINK | −9,031.09 | −33,097.54 | −38,818.26 | Short-side flow, but cost/defense failures remain. |

BTC session **−77.083687M**, weekly **−28.369369M**, rolling 24h **−105.332033M** are not interchangeable with this recovering minute tape. Conversely a positive five-minute delta does not erase the session inventory imbalance. TradFi flow values are signed **ticks**, not USD taker volume: e.g. SP500 −81, NAS −41, GOLD −8; no exchange-volume absorption claim follows from them.

## 3. Mandate 2 — BTC #18892038, frozen-R0 and structural audit

Existing position: **BUY 0.01, entry 83,223, initial/current SL 82,213, TP 84,320, frozen R0 1,010 price units**. One price unit is not one MT5 point: `point=0.01`, so R0 is 101,000 broker points. Registry terminology says “pts”; ratchet arithmetic here consistently uses price units.

### Ratchet arithmetic

- User position mark 83,328: `(83,328−83,223)/1,010 = +0.103960R0`.
- Exact snapshot position mark 83,378: **+0.153465R0**.
- Exact snapshot executable-side bid 83,359: **+0.134653R0**, a different sampled mark.
- Local later position mark 83,294: **+0.070297R0**.

None reaches Phase 0. No independent peak-MFE/tick path is supplied, so this does not certify that no historical trigger was ever reached. The producer emits `r_multiple_basis=live_sl_distance` and `r_multiple_initial_risk=null`; use the initial-risk registry, not that unsafe generic field.

| Phase | Long trigger price | Conditional SL, not an order now |
|---|---:|---:|
| Phase 0 at +1.25R0 | **84,485.50** | **82,970.50** |
| Phase 1 at +1.65R0 | **84,889.50** | **84,031.00** |
| Phase 2 at ≥2.00R0 | **85,243.00** | Observed peak executable bid − **757.50**, monotonic only |

Current TP pays `(84,320−83,223)×0.01 = 10.97 USD`, **1.086139 gross R0**, below the Phase 0 trigger. Under ordinary fills the target closes the position before any phase can activate. That is a strategy-configuration inconsistency, **not permission to extend TP to manufacture 2R**. Existing-position de-risking is not subject to forcing a new-entry payoff ratio.

### Actual stop defect and wall-side proof

Use **Hyperliquid basis −49**, not Binance basis −74.27, for Hyperliquid bands:

`[82,200,82,300] + (−49) = [82,151,82,251]`.

The `top_long_cascade_bands_below` list contains **9,436,348.13 USD** in that band. **SL 82,213 is inside it**, 62 above the lower edge and 38 below the upper edge: Archetype 1 is currently present. The nearest-only subset does not reach the band; a nearest-only audit would miss it. Matching stop notional is not available in the published nearby/top subsets, so it is not silently imported from an older cycle or assumed zero.

The largest bid from wallet `0xf5a523b171032c060d49c39fbf2e9bec473e1286` is **19.255271M at source 82,263 → broker 82,214**, just **1 price unit in front of SL**. That is only 0.0044 ATR and smaller than the half-spread of 8. The same wallet also quotes 19.787601M ask at 84,548 → 84,499: two-sided market making, not proven directional sponsorship. Another 16.648379M bid at 82,792 → 82,743 is in-pocket, but all these walls are single-sample. Missing verified defense makes the verified overwhelm ratio **unavailable**, not a confidently calculated safe ratio or proof that actual liquidity is zero.

Basis uncertainty is economically material: simultaneous-column mid differences give a diagnostic Hyperliquid basis −68.5 versus the stored median −49, a **19.5** difference. These are not proven synchronized prints. Under either translation the current SL is inside the band; the biggest bid can move from just above SL to below it. No fixed-buffer guarantee should rest on the smoothed basis alone.

A **single-band illustration**, not a proposed modification: clearing the lower edge by 0.50 ATR plus half-spread gives `82,151−0.5×226.6285−8 = 82,029.68575`, outward-snapped to **82,029.68**. This would **widen** risk to 11.9332 USD at 0.01 lot; it does not prove clearance from other bands or persistent shielding. Keeping the original 10.10 risk would require about **0.00846 lots**, below the 0.01 minimum. Do not widen, remove the stop, invent a sub-minimum size, or prematurely tighten inside another sweep band.

### TP/magnet review

The strongest nearby published buy-stop magnet is **17,521,278.95 USD** at source [84,300,84,400] → **[84,251,84,351]**. Current TP 84,320 is inside it, not 5–10 bps ahead of its lower edge. The historical 25.55M figure is no longer this generation's notional.

A lower-edge 5–10 bps front-run with half-spread subtraction gives approximately **84,158.74–84,200.87** after conservative tick snapping. This is diagnostic geometry, **not a certified TP replacement**. There are intervening pools and an unseasoned **16.895113M ask at broker 83,970**, plus 0.822251M forced buy-stops in [83,851,83,951]; one cannot simply assume they will be cleared en route to 84,320. Reducing TP may be sensible for an explicitly chosen exit-on-bounce policy, but requires a fresh executable quote/basis and current barriers, not blindly copying an old mapped target.

**Position disposition:** urgent structural-risk / passive exit-on-bounce review; **no mechanically justified ratchet and no certified exact SL/TP replacement** from these asynchronous observations. Preserve the existing protective order while the operator/terminal evaluates an explicitly reduce-only, ticket-specific passive close. An opposite pending sell on a hedging MT5 account could create a second position, not close this ticket; do not stage it as an assumed exit. Minimum size also prevents an arbitrary half-close. No market exit is instructed, and no shelf break is asserted solely from absent persistence. The current risk is not recertified as safe; it remains fully reserved until broker acknowledgement.

## 4. Mandate 3 — unfilled orders

The exact snapshot and local later snapshot both contain **`pending_orders=[]`**. There are **no ticket-by-ticket WAIT/MODIFY/DELETE actions**. Historical SP500 #18892059 in the context card is stale relative to these inventories; absence establishes no current pending exposure, not a fabricated cancellation receipt. BTC #18892038 is filled, not pending. Closed historical deals are not added to balance again.

## 5. Portfolio stress and execution summary

Use unrounded decimal arithmetic:

- Capital base `min(balance,equity)` = **4,869.65 USD** for all three reported baselines.
- Existing BTC nominal risk **10.10**; stress `1.25×10.10+2` = **14.625**.
- Modeled joint-stop equity **4,855.025**; buffer headroom **60.025**; hard-floor headroom **80.025**.
- A new 14.50-risk ticket costs **20.125** stress. Two cost 40.250 → equity **4,814.775**, **19.775 above the operating buffer**. Three cost 60.375 → **4,794.650**, failing by **0.350**.
- Capacity 1/4 used, 3 slots available does not mean 3 maximum-risk additions. Three lower-risk tickets could fit the stress arithmetic, but the user's explicit maximum-two-new-ticket instruction is retained; no new candidate exists anyway.
- Exact-snapshot free margin **4,455.08**; if the playbook's 4,000 free-margin reserve is retained, only **455.08** is available above it. Cash-risk capacity does not imply margin capacity. New orders need native `order_calc_profit`, `order_calc_margin`, currencies, commissions and simultaneous-fill margin, none invoked here.

### Actionable execution summary — no new broker instruction

| Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **STAND ASIDE** | — | — | — | — | — | — | — | — | — | — | No complete entry coincidence across 24 assets; CPI runway <2h. Existing BTC requires structural-risk review, not an automatically executable replacement order. |

Stand-aside defends against Archetypes **1/3/5** by refusing band-contained or shallow-buffer stops, **2** by refusing contrary HTF/flow entries, and **4** by not treating single observations as persistent defense. This does not retroactively cure the existing BTC stop defect.

## 6. Five-perspective adversarial review and arena adaptation

Installed [SKILL](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/.agent/skills/arena/SKILL.md) and [rubric](https://github.com/kbsingh1399/Trading_2/blob/3ee602ad4b69d01ea39d3a68ba8b7a440d87ab24/.agent/skills/arena/rubric.md) inspected. The canonical process requires separately dispatched competitors and independent judges. This runtime exposes no Agent/Task dispatcher. **The following is a single-assistant, five-perspective adaptation**, not five independent agents, 100-agent execution, or a canonical tournament certification. Rubric: correctness 30%, completeness 25%, specificity 15%, robustness 20%, clarity 10%; verified fatal flaws override scores. Scores below grade the written hypotheses, not probability of profitable trades.

### Independent lenses, concise findings

1. **Orderflow / microstructure:** The strongest positive case is recovering BTC flow and NAS's qualifying-size recurrent L2 ask. Attack: stale session labels can hide recovery; zero eligible L3 does not mean no L2. Revision: credit both, report minute coverage and recurrence gaps, retain missing held-price/primary evidence. Static depth imbalance is not event-time OFI.
2. **Structural price action:** SP500 and GBPUSD offer genuine low-Z pullback research. Attack: quiet velocity and RSI near 50 are not a demonstrated shelf touch-and-hold, and a 15m label cannot certify 1H/4H EMA200. Revision: list EMA/profile/auction shelves with history limits; retain watch status, not order cards.
3. **Liquidation / stop-hunt:** BTC's band containment is verified numerically. Attack: moving 0.5 ATR beyond one bin can put the new SL into the next bin; adjacent bins often tile the price axis. Revision: union/top+nearest containment audit and no blind widening. The illustrative NAS SL is independently killed by both minimum-lot risk and adjacent-band containment.
4. **Macro / portfolio:** Cash stress allows two maximum-risk additions, not three. Attack: `blackout_active=False` and ample free margin do not authorize entry when CPI runway is under one hour and marginal margin is unknown. Revision: preserve full reserve, two-ticket cap and runway; do not convert modeled loss into a guarantee.
5. **Adversarial red team:** Assume a staged order is stopped. NAS fails stop geometry; BTC addition fails HTF/defense; SP suffers adjacent-band/short-magnet compression; ETH/SOL rally shorts face positive local buying. Assume existing BTC is held as 'safe': its SL already violates the sweep-band invariant. Revision: no new orders, urgent existing-risk review, no premature ratchet, no arbitrary TP extension, no fabricated broker action.

### Written hypothesis comparison

| Hypothesis after challenge | Correct | Complete | Specific | Robust | Clear | Weighted /100 | Standing flaw |
|---|---:|---:|---:|---:|---:|---:|---|
| H1 Add BTC long now because local CVD recovered | 4 | 6 | 7 | 2 | 8 | 49.5 | Fatal: mixed HTFs, unseasoned defense, no held quiet shelf; macro runway. |
| H2 Buy NAS100's −2.23Z extreme | 2 | 5 | 7 | 1 | 8 | 39.0 | Fatal: forbidden bearish-regime mean-reversion long. |
| H3 Stage NAS100 relief short at recurrent 1M ask | 5 | 7 | 9 | 2 | 8 | 58.0 | Fatal: nearest-wall minimum-lot risk and adjacent-band containment; macro. |
| H4 Stage SP500/GBPUSD quiet low-Z longs | 5 | 7 | 7 | 2 | 8 | 55.0 | Fatal: no complete primary-wall/geometry/held-shelf proof; macro. |
| H5 Stage ETH/SOL relief shorts immediately | 4 | 6 | 7 | 2 | 8 | 49.5 | Fatal: rally flow/velocity, persistence and safe payable geometry unresolved. |
| H6 Tighten BTC now or extend TP to unlock ratchets | 2 | 5 | 9 | 1 | 8 | 42.0 | Fatal: no R0 trigger, target extension unsupported. |
| H7 Certify BTC hold as structurally safe | 3 | 6 | 8 | 1 | 8 | 46.0 | Fatal: current SL lies inside observed liquidation band. |
| H8 No new order; existing-risk review with protection retained | 9 | 8 | 8 | 9 | 9 | **86.0** | No false trade certification; full archive semantics, live broker path and independent judge remain limitations. |

Adapted pairwise bracket: H1/H2→H1; H3/H4→H3; H5/H6→H5; H7/H8→H8. Semifinals H1/H3→H3, H5/H8→H8. Final H3/H8→**H8**. Advancing among flawed hypotheses never grants trade approval. Key conceded attacks: locally improving BTC flow; nonzero L2 recurrence; correct source-venue basis; exact-generation equity/mark differences. Unresolved limitations remain visible rather than being 'scored away'.

## 7. Institutional schema audit — concrete corrections, not more arbitrary gates

The exact JSON contains **14,227 dictionaries, 1,399 lists and 118,115 scalar values**, including **286 nulls**. All floating values are finite. Every supplied candle series has monotonic timestamps, valid OHLC containment and no close beyond the generation candle cutoff under the published timestamps. Twenty-two assets have 20 bids and 20 asks; DJ30/GER40 have no observed depth. Quote-age diagnostics also identify TRX 11.577s, DOT 12.429s and BCH 10.117s beyond the playbook's <10s freshness threshold; their observations are not executable fresh-quote receipts. Cent-level ladder/cumulative differences are rounding, not asserted corruption.

| Finding grounded in this snapshot | Concrete schema/feature change | Acceptance check |
|---|---|---|
| EURUSD spread_price 0.0 despite 0.09 bps; GBP bid 1.3264/ask 1.3265 but spread_price 0.0 and 0.08 bps. Generator lines 2102–2105 round all quotes to four decimals. | Preserve broker-digit/tick precision, ideally integer ticks plus decimal price strings; serialize spread from those same unrounded values. Include commission currency/rate, swap, tick-value loss/profit, contract currency, margin mode and broker calc receipts. | At 5-digit FX, exactly preserve a 0.00001 spread; bid ≤ ask, midpoint consistency and spread_bps reconciliation within declared rounding tolerance. Never infer zero cost from the rounded field. |
| Snapshot fields disagree in sampling time; generation takes about 93.4s. `local_receipt_time_epoch` and calibrated broker clocks need distinct labels. | Per-block event/receipt/availability timestamps, clock domain/error bound, sequence ID, heartbeat, coverage, and `decision_cutoff`. | No future-available block used in causal replay; freshness measured in its actual calibrated clock. Root timestamp alone cannot establish simultaneous data. |
| 1,045 L3 rows all single-sample; provider has no order IDs. Current publisher keys recurrence by asset/address/side/price. | Durable per-feed state, restart ID, raw observations, `continuous_observed_s`, `max_gap_s`, `presence_frac`, price/size re-peg lineage with confidence, pulled/refilled notional, cancellation hazard and two-sided-wallet exposure. | Replayed disappear/reappear sequences do not acquire fictitious continuous age; a price change does not imply withdrawal or verified identity by assumption. Retain `order_id=null` where unavailable. |
| Static book imbalance exists; event-time multi-level OFI does not. | For level k: `e_k = 1[b_t≥b_prev]q_b,t − 1[b_t≤b_prev]q_b,prev − 1[a_t≤a_prev]q_a,t + 1[a_t≥a_prev]q_a,prev`. Aggregate causal event increments with depth/distance weights, normalize by observed depth, publish 1/5/15/30m. | Sequence-gap detection and price-level identity; venue-specific units; no invented size from MT5 L1. |
| A single static mid/imbalance cannot measure drift or refill. | Microprice `μ=(ask×bid_qty + bid×ask_qty)/(bid_qty+ask_qty)`; drift `(μ−mid)/tick`, change/return correlations; impact curves at standardized cash sizes and resiliency half-life. | Keep venue and timestamp; never call a Hyperliquid microprice an executable MT5 fill. |
| No true MT5 exchange queue position; L3 is not order-ID complete. | Publish **external queue-depth proxy**, depletion/refill hazard and fill-probability model with venue-specific limitations, not a fabricated broker queue rank. | MT5 limit fills modeled from broker bid/ask and acknowledged fill records; no guaranteed execution from touching an external wall. |
| Crypto last closed minute missing; TradFi tick CVD shares `session_cvd_usd` naming. | Explicit window start/end, expected/observed buckets, missing durations, counts and units. Taker buy fraction `sum(buy)/(sum(buy)+sum(sell))`, signed ratio, delta-rate slope and acceleration for 1/5/15/30m. | Missing minute is null/partial coverage, not zero. Synthetic tick CVD never presented as cash notional or institutional taker flow. |
| `trapped_traders_signal` is only a label; no full `footprint_trapped_traders` block. | Price-bin aggressive buys/sells, delta, total volume, sweeps, retest outcome and replenishment. Long absorption score: `z(sell_volume) − z(max(0,−mid_return)/ATR) + z(bid_refill)`, conditioned on shelf hold; mirror for shorts. | Train standardizers on prior data only; large selling with a falling price is not automatically absorption. Label must link to raw footprint evidence. |
| No independently warmed 1H/4H EMA200; single RSI snapshot and some retrace >1 values. | Per-timeframe EMA20/50/200, warm-up counts/seed method and slopes; RSI history, closed-candle timestamps, shelf-touch/reclaim records, impulse/pullback definition and quality flags. | Warm-up/seed sensitivity disclosed; 15m EMA200 is not reused as HTF EMA200. A valid overshoot is distinguished from inconsistent retrace math. |
| GBP 0.01-wide bins are 20 ATR; USDJPY 1-wide bins ~18.94 ATR. Neighboring bins tile the axis. | Preserve raw stop/liquidation levels; adaptive tick-aligned bins `h=max(tick,min(0.10×ATR,0.0001×mid))` as a research starting point, multi-scale density with coverage/confidence, and clear `DISPLAY_BIN` vs `ESTIMATED_SWEEP_INTERVAL` semantics. | Bands follow actual observed support, not bin midpoints; no overlaps double-counted; an empty subset is not zero inventory. Do not silently weaken the current no-band-containment instruction. |
| Hyperliquid and Binance have different basis; stored medians differ from contemporaneous column differences. | Venue-keyed timestamp-paired basis distribution: rolling median, MAD, q05/q95/q99, sample count, last observation, latency and hedge/correlation error. | Translate each wall/cluster using its own venue. Quantify residual basis/spread stress; a smoothed median is not a guaranteed executable offset. |
| Stop/liq arrays overlap between nearest/top; wallet populations can overlap across mechanisms. | Stable band/position/order IDs, coverage range, unique contributor sets, overlapping-fuel upper/lower bounds and monotonic filter definitions. | No nearest+top summation without de-duplication; stop activation and later liquidation of the same position not double-counted as independent fuel. |
| Active risk field uses current-SL R while initial-R is null; no peak receipt. | `initial_sl`, `initial_r0_price`, `initial_risk_usd`, immutable ledger ID/hash, current executable-side R0, peak-MFE price/time, ratchet phase and broker acknowledgement. | Restart replay with a tightened SL gives exactly the same R0 and phase; no ATR fallback changes initial risk. |
| Hyperdash aggregate 'recent' liquidations include October 08 records; zero alert arrays have unclear coverage. | ISO event timestamps with timezone/year, receipt timestamp, query coverage, ingestion completeness, dedup ID; rolling-window aggregates alongside lifetime/10k-alert totals. | Historical liquidations cannot masquerade as current pressure. No alerts is only absence in observed coverage. |
| p_win 0.4197 uses only 17 trades and is explicitly uncalibrated. | Engine×asset×session calibration with sample counts, fill/cost conditional outcomes, time-to-target, block bootstrap/intervals and out-of-sample drift. | No 'institutional edge' or p_win certification from 17 potentially dependent observations. |

These are **proposed pipeline changes**, not code fixes claimed to be deployed in this report. Particularly, fixing FX serialization should be a small separately tested patch; the external AI-service error is unrelated.

### Other telemetry blocks, not discarded

Funding/current mark/index and eight funding-history observations are retained for crypto carry/basis context; unavailable predicted funding is not extrapolated as fact. All broker 15m/1H/4H/daily and exchange 4H arrays are inspected for geometry/time integrity. MT5 VWAP and profiles explicitly use tick-volume proxies, not exchange institutional volume. Global ETF observations show BTC +175.7M and ETH +24.8M for October 13, not instant intraday flow; Coinbase premium −6.52 bps; FNG is **null** in this exact generation. Hyperdash totals are 97.295267M historical liquidation volume, ratio 1.3 and zero observed active TWAP/imminent alert entries, not proof of no live hazard. The account server is null; execution specs have no fresh new-order margin receipt. Producer permission labels and p_win are not allowed to substitute for the above evidence.

## 8. Payable 2.0–2.5R construction and profitable-frequency research

### The algebra that prevents cosmetic R:R

For executable entry E, stop S and target T, let `r1` and `g1` be broker-valued per-lot adverse/favorable PnL magnitudes, with entry/exit quote sides treated consistently. Let `c_loss`/`c_win` be **only additional costs not already embedded** in those executable prices (commissions, expected slippage/financing). Require:

`R_net = (g1 − c_win)/(r1 + c_loss) >= R_required`.

Do not subtract the same spread twice. In a linear **mid-price research model**, where spread is not embedded, `D_T >= R_required×D_S + c_win_price + R_required×c_loss_price`. Thus a genuine 1.2 ATR stop needs at least 2.4–3.0 ATR gross room plus costs for 2–2.5R. The solution is a better structural entry after an observed sweep, not a stop inside it or a faraway target with no intraday fill probability.

Lot grid: enumerate `q = min_lot + n×step_lot`, retain broker-valued nominal risk within **7.50–14.50**, then stress/margin each simultaneous fill. Size down for wider valid stops, but if no discrete lot exists, there is no ticket. For linear CFDs, `spread friction = spread_price / stop_distance` when denominator is actual nominal stop risk; downsizing reduces cash costs and risk together and **does not improve their ratio**. Using the maximum budget rather than actual risk can understate friction. Minimum-lot cost/14.50 is only a lower-bound rejection test, not admission proof.

Expected return must include passive fills and failed entries: `EV_per_attempt = P(fill)×[p×net_gain − (1−p)×net_loss] − cancel/nonfill_cost`, with adverse selection conditional on fill. At a net payoff 2R, break-even win rate is 1/3; at 2.5R it is 2/7, but that is algebra, not an empirical claim that either rate is attainable here.

### Quantitative geometry falsification examples

- **SP500** has attractive trend/low-Z/quiet pullback. Mapped bid 7,810.31 is only **1.72 ATR** below current mid. Nearest ≥0.5M buy-stop target starts 7,821.31; a 5bps plus half-spread front-run gives **7,817.249345**, only **6.939345** of reward from that wall. Even the playbook's minimum **1.5 ATR = 6.8667** total index stop yields only **1.0106 gross R**, before further costs or deeper-band clearance. Moving the target past nearer obstacles solely to print 2R is not justified.
- **NAS100** at mapped recurrent ask 30,546.455 fails min-lot risk (15.4045) with even the inadequate one-band illustrative SL 30,700.50. At a deeper EMA entry a raw ratio may improve, but the SL remains inside the next published stop band. It is not an immediately payable card merely because the L2 duration/size thresholds pass.
- **ETH/SOL** require net ≥2.2R/2.5R under the mandate. Waiting for positive relief-rally delta to weaken at a seasoned ask, with measured price rejection, is an entry improvement; selling now and tightening into the buy-stop band is not.
- **GOLD** offers a favorable downtrend but nearest threshold-sized ask 4,163.82 is 4.09 ATR away; EMA50 4,153.7067 is itself 2.27 ATR away. A better future location must actually arrive; no resting distant order is certified.
- **FX** need full precision and sub-ATR structure. Broad 20-ATR display bins cannot simultaneously act as exact intraday exclusion zones while demanding a nearby 2R target. Repair granularity/semantics, then validate; do not bypass the present invariant by rebranding an inconvenient bin.

### Adaptive buffers and front-running, while preserving current minimums

Research a conditional empirical adverse-sweep quantile by asset, session, volatility, spread and event state. For a long, require both `SL <= shelf_low − b_shelf` and `SL <= governing_band_min − b_band`, then all-band containment recheck; reverse for a short. Use at least the current **0.50 ATR shelf / 0.35 ATR band** floors, choosing 0.50–0.75 ATR or larger if empirical sweep/basis/spread tails demand it. Model uncertainty terms in the same price units, account for correlations, and avoid mechanically double-counting components already inside empirical excursion data. Wider safety may require smaller size or no order.

For long TP, choose a verified reachable magnet's lower edge and subtract a tick-quantized front-run; for shorts use upper edge plus front-run. During the current policy, retain 5–10 bps and the specified spread treatment. Research replacing fixed bps with conditional latency/queue-depletion and spread/basis quantiles only through an explicit future playbook revision. Fixed 5bps is roughly 1.40 ATR on EURUSD and 1.50 ATR on USDJPY at this snapshot, so blindly applying it can consume the entire nearby target. Do not treat a proposed adaptive replacement as already authorized.

### Where frequency can improve — without staging now

Prioritize fresh post-event research in **SP500 and NAS100**, then **BTC**, **GOLD/USWTI**, then precision-repaired **GBPUSD**. ETH/SOL are conditional on higher net payoff and verified failed-rally flow. Keep BNB as lower-priority short-shelf research. DJ30/GER40 require a defensible structural-data source, not invented walls. Explicitly excluded alts remain excluded; XRP/TRX/LTC have independently demonstrated current minimum-lot friction failures.

Use near-shelf passive entries, fill-time thesis revalidation, expiry before applicable purge, wall-withdrawal cancellation, broker quote-side cost modeling and a ranking of **expected net USD per attempted order / margin-minute**, penalizing correlated dollar/crypto exposure. Do not chase missed fills or repeatedly repost an invalid thesis. After CPI, re-check the next calendar event, spreads, basis tails, current walls, account/inventory and actual reachable magnets; **13:00 is not automatic permission**.

Validate each proposed enhancement with causal walk-forward/replay, completed-bar joins, realistic bid/ask fills, gap-aware SL fills, transaction costs and held-out event sessions. Compare gross/net EV, fill rate, stop-before-TP rate, MAE/MFE, time-to-resolution, drawdown and turnover against the current policy and a risk-scaled benchmark. Correct for 24-asset/two-engine multiple testing and overlapping outcomes. No performance increase is claimed without that evaluation.

## 9. Publication and verification boundaries

This report and the companion evidence ledger are appended/referenced on the session branch only. Telemetry, live execution code, account orders, playbook rules and initial-risk registry are unchanged. No independent tab consensus, live broker acknowledgement, macro-feed refresh or platform-service repair is claimed.

Verification passed: exact generation/hash; all 24 assets; recursive scalar coverage; candle chronology/containment/cutoff; depth ordering; cash stress and R0 arithmetic; L3/L2 persistence counts; venue-specific band containment; table classification counts. See Appendix A and the evidence ledger for the per-asset receipts. Any later market action needs fresh source data and native execution validation.

## Appendix A — per-asset telemetry receipts

The following receipts are generated directly from the exact pinned JSON. They preserve source precision, disclose absent fields, cover every per-asset telemetry block and supplement rather than replace the two-engine verdicts above. Seeded diagnostic HTF EMAs are estimates over the supplied history, not a claim of a fully warmed 200-period stack. CVD 5/15/30 values here are the last observed complete-bucket windows ending 10:59; snapshot-anchored coverage is separately 4/14/29. External bands and walls remain identified by their own source venue; their raw bounds are not broker quotes.

### BTC — BTCUSD.pi — WATCHLIST

Source [lines 2409–17254](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L2409-L17254); JSON path `assets_matrix_24.BTC`.
- **Quotes/specs:** bid 83,359, ask 83,375, mid 83,367; reported spread 16, 1.92 bps; reported age 0.62030578s. Contract 1.0, lot min/step 0.01/0.01, max 100.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.16 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 83,413.5665, sigma 183.1326, Z -0.25, RSI 47.5, ATR 226.6285; 15m EMA20/50/200 83,362.7076/83,380.0232/83,239.3139, EMA200 3h slope 0.02%. POC/VAH/VAL 83,381.15/83,492.48/83,121.38. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 83,329.5/83,444.5/83,082.5/83,152.5; seeded EMA20/50 83,330.32383211/83,229.15774378; last 3 closes 83,485.5, 83,329.5, 83,152.5. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 83,663/84,061.5/83,209.5/83,329.5; seeded EMA20/50 83,187.06383705/83,368.56446491; last 3 closes 83,348, 83,663, 83,329.5. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.3526,"depth_sigma":0.0,"velocity_ratio":1.4168,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 82,444.795/83,179.76/80,879; prior week 82,952.7/83,625.9/82,358.7; weekly VWAP 83,104.9488. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-77083687.45,"weekly_cvd_usd":-28369369.47,"cvd_24h_usd":-105332033.17,"bar_delta_15m_usd":1033293.52,"divergence":"BEARISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-77083687.45,"flow_bias":"BEARISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 793,101.73 / 1,367,053.47 / 2,087,170.95 USD. Root-anchored partial sums 535,592.56 / 903,672.31 / 2,146,923.1 USD with 4/14/29 buckets. Root-anchored buy fractions 0.68210535 / 0.57508635 / 0.58782328; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 473,328.06/497,356.34; imbalance -0.0248; ladder sizes 20/20. L3 count 397, L3 elapsed>=180s 0; L2 count 2, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -74.27; HYPERLIQUID: -49. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xf5a523b171032c060d49c39fbf2e9bec473e1286, source 82,263, mapped 82,214, 19,255,270.8 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xf5a523b171032c060d49c39fbf2e9bec473e1286, source 84,548, mapped 84,499, 19,787,601.24 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [80,000, 80,100] / 54,795,504.53 USD; top_buy_stop_clusters_above: n=10, first [84,300, 84,400] / 17,521,278.95 USD; nearest_sell_stop_clusters_below: n=10, first [83,300, 83,400] / 44,895.81 USD; nearest_buy_stop_clusters_above: n=10, first [83,400, 83,500] / 534,854.09 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [80,200, 80,300] / 14,968,563.99 USD; top_short_squeeze_bands_above: n=3, first [83,700, 83,800] / 33,269.91 USD; nearest_long_cascade_bands_below: n=10, first [83,300, 83,400] / 13,247.05 USD; nearest_short_squeeze_bands_above: n=3, first [83,500, 83,600] / 930.31 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.71,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":83441.8,"index_price":83470.69}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `ACTIVE_FILLED`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### ETH — ETHUSD.pi — WATCHLIST

Source [lines 17255–26379](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L17255-L26379); JSON path `assets_matrix_24.ETH`.
- **Quotes/specs:** bid 2,502.5, ask 2,505.3, mid 2,503.9; reported spread 2.8, 11.18 bps; reported age 0.86056733s. Contract 1.0, lot min/step 0.01/0.01, max 100.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.028 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 2,503.7141, sigma 6.5234, Z 0.03, RSI 46.66, ATR 8.3093; 15m EMA20/50/200 2,500.7804/2,503.0413/2,506.936, EMA200 3h slope -0.0296%. POC/VAH/VAL 2,502.206/2,508.732/2,493.672. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 2,501.5/2,505.5/2,489.8/2,492.5; seeded EMA20/50 2,503.47920817/2,506.48631948; last 3 closes 2,506.9, 2,501.4, 2,492.5. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 2,510.9/2,525.8/2,493.6/2,501.4; seeded EMA20/50 2,510.2762518/2,542.78485477; last 3 closes 2,503.6, 2,510.9, 2,501.4. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.4622,"depth_sigma":0.0008,"velocity_ratio":1.8586,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 2,527.411/2,544.252/2,486.074; prior week 2,502.595/2,558.674/2,471.842; weekly VWAP 2,507.5465. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":5239349.76,"weekly_cvd_usd":-26317606.66,"cvd_24h_usd":-3677029.39,"bar_delta_15m_usd":211220.54,"divergence":"BULLISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":5239349.76,"flow_bias":"BULLISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 37,784.88 / 125,099.19 / -156,072.13 USD. Root-anchored partial sums 9,939.81 / 154,774.01 / -96,447.22 USD with 4/14/29 buckets. Root-anchored buy fractions 0.50854512 / 0.54436066 / 0.48865819; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 130,680.12/109,166.23; imbalance 0.0897; ladder sizes 20/20. L3 count 141, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -2.49; HYPERLIQUID: -1.15. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xab5e6f394951c28ab1873007e373202689cdbec3, source 2,469.2, mapped 2,468.05, 11,430,359.4 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xab5e6f394951c28ab1873007e373202689cdbec3, source 2,529.6, mapped 2,528.45, 11,750,550.79 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [2,400, 2,410] / 21,374,832.96 USD; top_buy_stop_clusters_above: n=10, first [2,560, 2,570] / 6,424,360.02 USD; nearest_sell_stop_clusters_below: n=10, first [2,500, 2,510] / 404,127.24 USD; nearest_buy_stop_clusters_above: n=10, first [2,510, 2,520] / 796,502.63 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [2,470, 2,480] / 18,344,100.55 USD; top_short_squeeze_bands_above: n=1, first [2,520, 2,530] / 199.43 USD; nearest_long_cascade_bands_below: n=10, first [2,500, 2,510] / 802.96 USD; nearest_short_squeeze_bands_above: n=1, first [2,520, 2,530] / 199.43 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.01,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":2506.47,"index_price":2507.47}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### SOL — SOLUSD.p — WATCHLIST

Source [lines 26380–33908](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L26380-L33908); JSON path `assets_matrix_24.SOL`.
- **Quotes/specs:** bid 106.9, ask 107.13, mid 107.015; reported spread 0.23, 21.49 bps; reported age 0.75031829s. Contract 100.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.23 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 107.1042, sigma 0.4339, Z -0.21, RSI 45.29, ATR 0.4468; 15m EMA20/50/200 106.8606/107.0262/107.681, EMA200 3h slope -0.1011%. POC/VAH/VAL 106.6801/107.6318/106.4038. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 106.76/107.03/106.25/106.36; seeded EMA20/50 107.06584331/107.64110711; last 3 closes 107.23, 106.76, 106.36. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 107.69/108.43/106.7/106.76; seeded EMA20/50 108.31583815/111.10116624; last 3 closes 107.2, 107.69, 106.76. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.3218,"depth_sigma":0.0125,"velocity_ratio":1.298,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 108.2944/109.0168/105.3016; prior week 109.4307/111.8952/105.6518; weekly VWAP 107.5685. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":5191169.72,"weekly_cvd_usd":21572398.44,"cvd_24h_usd":12862044.95,"bar_delta_15m_usd":196171.3,"divergence":"BULLISH_ABSORPTION","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":5191169.72,"flow_bias":"BULLISH_ABSORPTION"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 38,203.24 / 174,284.23 / 205,306.37 USD. Root-anchored partial sums 15,153.88 / 165,626.57 / 197,653.49 USD with 4/14/29 buckets. Root-anchored buy fractions 0.58537997 / 0.60558877 / 0.55135145; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 2,228,637.86/1,287,931.21; imbalance 0.2675; ladder sizes 20/20. L3 count 64, L3 elapsed>=180s 0; L2 count 7, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.14; HYPERLIQUID: -0.08. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xeac842b2214cfece3f0d288293da19f408d91ede, source 105.43, mapped 105.35, 6,183,115.26 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xeac842b2214cfece3f0d288293da19f408d91ede, source 108.83, mapped 108.75, 6,382,513.83 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [105, 106] / 15,001,549.32 USD; top_buy_stop_clusters_above: n=10, first [109, 110] / 502,659.58 USD; nearest_sell_stop_clusters_below: n=10, first [106, 107] / 267,084.11 USD; nearest_buy_stop_clusters_above: n=10, first [107, 108] / 127,400.97 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [103, 104] / 13,858,724.62 USD; top_short_squeeze_bands_above: n=1, first [107, 108] / 22,906.52 USD; nearest_long_cascade_bands_below: n=10, first [106, 107] / 903.4 USD; nearest_short_squeeze_bands_above: n=1, first [107, 108] / 22,906.52 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.63,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":107.138,"index_price":107.188}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### BNB — BNBUSD.p — WATCHLIST

Source [lines 33909–40261](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L33909-L40261); JSON path `assets_matrix_24.BNB`.
- **Quotes/specs:** bid 741.7, ask 742.2, mid 741.95; reported spread 0.5, 6.74 bps; reported age 3.49899554s. Contract 1.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 20. Minimum-lot spread cash diagnostic 0.005 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 742.538, sigma 1.3505, Z -0.44, RSI 44.78, ATR 1.5561; 15m EMA20/50/200 741.43/741.9045/743.0491, EMA200 3h slope -0.031%. POC/VAH/VAL 743.943/744.252/740.338. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 740.3/741.1/739.4/740.6; seeded EMA20/50 741.96440029/743.0521137; last 3 closes 742, 740.4, 740.6. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 744.5/745.9/740.2/740.4; seeded EMA20/50 744.51757218/751.632623; last 3 closes 743, 744.5, 740.4. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.2609,"depth_sigma":0.0011,"velocity_ratio":1.0471,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 743.861/747.67/734.778; prior week 741.599/758.796/729.146; weekly VWAP 742.0781. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":472610.96,"weekly_cvd_usd":-10085916.61,"cvd_24h_usd":-1482623.0,"bar_delta_15m_usd":156887.04,"divergence":"BULLISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":472610.96,"flow_bias":"BULLISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 30,356.57 / 147,598.77 / 152,306.85 USD. Root-anchored partial sums 20,712.33 / 149,581.17 / 169,745.88 USD with 4/14/29 buckets. Root-anchored buy fractions 0.66414389 / 0.79264395 / 0.66808079; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 153,189.72/100,030.49; imbalance 0.2099; ladder sizes 20/20. L3 count 10, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.875; HYPERLIQUID: -0.465. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x02fbbf39d1e3c142994b383af5ac3f2ad744cda9, source 739.3, mapped 738.835, 1,238,388.12 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x02fbbf39d1e3c142994b383af5ac3f2ad744cda9, source 745.74, mapped 745.275, 1,250,679.06 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [734, 735] / 10,247.54 USD; top_buy_stop_clusters_above: n=10, first [762, 763] / 354,428.08 USD; nearest_sell_stop_clusters_below: n=10, first [742, 743] / 149.26 USD; nearest_buy_stop_clusters_above: n=10, first [743, 744] / 103.96 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [715, 716] / 11,838.87 USD; top_short_squeeze_bands_above: n=6, first [758, 759] / 3,072.78 USD; nearest_long_cascade_bands_below: n=10, first [738, 739] / 2,557.43 USD; nearest_short_squeeze_bands_above: n=6, first [746, 747] / 1,210.4 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-0.47,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":742.5,"index_price":742.97}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### XRP — XRPUSD.pi — NO SETUP

Source [lines 40262–46289](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L40262-L46289); JSON path `assets_matrix_24.XRP`.
- **Quotes/specs:** bid 1.371, ask 1.375, mid 1.373; reported spread 0.004, 29.13 bps; reported age 4.21020937s. Contract 1000.0, lot min/step 1.0/1.0, max 100.0, tick 0.001, point 0.001, stops_level 20. Minimum-lot spread cash diagnostic 4 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** RANGE_BOUND; VWAP 1.3678, sigma 0.0037, Z 1.43, RSI 49.64, ATR 0.005; 15m EMA20/50/200 1.367/1.3673/1.3713, EMA200 3h slope -0.0333%. POC/VAH/VAL 1.3682/1.37/1.36. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 1.368/1.369/1.36/1.364; seeded EMA20/50 1.3667347/1.37098402; last 3 closes 1.37, 1.368, 1.364. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 1.372/1.383/1.359/1.368; seeded EMA20/50 1.37733552/1.4046971; last 3 closes 1.37, 1.372, 1.368. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.5,"depth_sigma":0.2708,"velocity_ratio":0.132,"bars_pullback":19,"bars_impulse":5,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 1.357/1.3795/1.3384; prior week 1.4003/1.4233/1.3621; weekly VWAP 1.3695. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":14078292.35,"weekly_cvd_usd":38170433.78,"cvd_24h_usd":37388241.78,"bar_delta_15m_usd":574806.66,"divergence":"BULLISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":14078292.35,"flow_bias":"BULLISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 296,739.38 / 453,282.22 / 756,488.22 USD. Root-anchored partial sums 246,896.67 / 431,887.32 / 744,143.98 USD with 4/14/29 buckets. Root-anchored buy fractions 0.81255647 / 0.64112985 / 0.65024895; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 694,192.67/667,521.26; imbalance 0.0196; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.0013; HYPERLIQUID: -0.00035. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [1.32, 1.33] / 203,906.82 USD; top_buy_stop_clusters_above: n=10, first [1.41, 1.42] / 3,584,882.97 USD; nearest_sell_stop_clusters_below: n=10, first [1.36, 1.37] / 60,380.71 USD; nearest_buy_stop_clusters_above: n=10, first [1.37, 1.38] / 21,694.47 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [1.34, 1.35] / 618,957.89 USD; top_short_squeeze_bands_above: n=1, first [1.37, 1.38] / 1,710.44 USD; nearest_long_cascade_bands_below: n=10, first [1.35, 1.36] / 9,081.15 USD; nearest_short_squeeze_bands_above: n=1, first [1.37, 1.38] / 1,710.44 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-1.05,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":1.3746,"index_price":1.3753}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### ADA — ADAUSD.p — NO SETUP

Source [lines 46290–52644](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L46290-L52644); JSON path `assets_matrix_24.ADA`.
- **Quotes/specs:** bid 0.2337, ask 0.2359, mid 0.2348; reported spread 0.0022, 93.7 bps; reported age 9.70984173s. Contract 5000.0, lot min/step 1.0/1.0, max 1000.0, tick 0.0001, point 0.0001, stops_level 20. Minimum-lot spread cash diagnostic 11 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 0.2351, sigma 0.0012, Z -0.22, RSI 43.34, ATR 0.0011; 15m EMA20/50/200 0.2339/0.2345/0.2375, EMA200 3h slope -0.2%. POC/VAH/VAL 0.2359/0.2366/0.2334. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 0.2335/0.2342/0.2327/0.2335; seeded EMA20/50 0.23489999/0.23770205; last 3 closes 0.2343, 0.2335, 0.2335. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 0.2357/0.2373/0.2328/0.2335; seeded EMA20/50 0.23970287/0.2445208; last 3 closes 0.2362, 0.2357, 0.2335. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.2,"depth_sigma":2.749,"velocity_ratio":0.8068,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 0.2407/0.2433/0.2293; prior week 0.252/0.2574/0.2353; weekly VWAP 0.2384. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":725939.63,"weekly_cvd_usd":-2102604.38,"cvd_24h_usd":1227970.42,"bar_delta_15m_usd":-5824.07,"divergence":"BULLISH_ABSORPTION","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":725939.63,"flow_bias":"BULLISH_ABSORPTION"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 5,026.57 / 4,443.17 / 25,273.87 USD. Root-anchored partial sums 3,437.29 / 4,204.45 / 25,221.13 USD with 4/14/29 buckets. Root-anchored buy fractions 0.74558107 / 0.54600511 / 0.62579032; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 580,404.03/540,158.7; imbalance 0.0359; ladder sizes 20/20. L3 count 10, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.0003; HYPERLIQUID: -0.0000875. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xeac842b2214cfece3f0d288293da19f408d91ede, source 0.2303, mapped 0.2302125, 1,637,086.4 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xeac842b2214cfece3f0d288293da19f408d91ede, source 0.2396, mapped 0.2395125, 1,702,739.94 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [0.225, 0.226] / 148,495.87 USD; top_buy_stop_clusters_above: n=10, first [0.241, 0.242] / 102,683.53 USD; nearest_sell_stop_clusters_below: n=10, first [0.234, 0.235] / 498.84 USD; nearest_buy_stop_clusters_above: n=10, first [0.235, 0.236] / 1,455.87 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [0.224, 0.225] / 14,719.23 USD; top_short_squeeze_bands_above: n=8, first [0.24, 0.241] / 4,038.19 USD; nearest_long_cascade_bands_below: n=10, first [0.234, 0.235] / 1,854.85 USD; nearest_short_squeeze_bands_above: n=8, first [0.235, 0.236] / 826.86 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-1.23,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.235,"index_price":0.2352}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### DOGE — DOGUSD.p — NO SETUP

Source [lines 52645–58786](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L52645-L58786); JSON path `assets_matrix_24.DOGE`.
- **Quotes/specs:** bid 0.0833, ask 0.0854, mid 0.0844; reported spread 0.0021, 248.96 bps; reported age 3.09767699s. Contract 10000.0, lot min/step 1.0/1.0, max 50.0, tick 0.0001, point 0.0001, stops_level 20. Minimum-lot spread cash diagnostic 21 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** RANGE_BOUND; VWAP 0.0836, sigma 0.0003, Z 2.77, RSI 42.99, ATR 0.0003; 15m EMA20/50/200 0.0833/0.0834/0.0837, EMA200 3h slope -0.0539%. POC/VAH/VAL 0.0834/0.0838/0.083. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 0.0833/0.0834/0.0829/0.0831; seeded EMA20/50 0.08342256/0.08364547; last 3 closes 0.0836, 0.0833, 0.0831. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 0.084/0.0845/0.0832/0.0833; seeded EMA20/50 0.08401444/0.08590417; last 3 closes 0.0835, 0.084, 0.0833. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.2222,"depth_sigma":11.0482,"velocity_ratio":0.8964,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 0.0837/0.0845/0.0813; prior week 0.0835/0.086/0.0816; weekly VWAP 0.0836. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-1650697.5,"weekly_cvd_usd":-13719815.11,"cvd_24h_usd":-3114386.04,"bar_delta_15m_usd":34842.3,"divergence":"BEARISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-1650697.5,"flow_bias":"BEARISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 15,264.52 / 37,429.79 / 18,116.19 USD. Root-anchored partial sums 19,442.66 / 34,549.8 / 25,862.56 USD with 4/14/29 buckets. Root-anchored buy fractions 0.67111601 / 0.63939263 / 0.55879904; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 343,600.53/656,684.77; imbalance -0.313; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 1, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.000085; HYPERLIQUID: -0.000073. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [0.0825, 0.0826] / 111,460.29 USD; top_buy_stop_clusters_above: n=10, first [0.0883, 0.0884] / 1,305,305.97 USD; nearest_sell_stop_clusters_below: n=10, first [0.0843, 0.0844] / 199.61 USD; nearest_buy_stop_clusters_above: n=10, first [0.0844, 0.0845] / 3,783.39 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [0.0802, 0.0803] / 10,437.23 USD; top_short_squeeze_bands_above: n=8, first [0.0861, 0.0862] / 4,699.71 USD; nearest_long_cascade_bands_below: n=10, first [0.0843, 0.0844] / 840.24 USD; nearest_short_squeeze_bands_above: n=8, first [0.085, 0.0851] / 745.25 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.55,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.0844,"index_price":0.0844}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### TRX — TRXUSD.p — NO SETUP

Source [lines 58787–64887](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L58787-L64887); JSON path `assets_matrix_24.TRX`.
- **Quotes/specs:** bid 0.3329, ask 0.3339, mid 0.3334; reported spread 0.001, 29.99 bps; reported age 11.57718182s. Contract 10000.0, lot min/step 1.0/1.0, max 50.0, tick 0.0001, point 0.0001, stops_level 20. Minimum-lot spread cash diagnostic 10 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 0.3308, sigma 0.0018, Z 1.47, RSI 69.4, ATR 0.0005; 15m EMA20/50/200 0.332/0.3306/0.3295, EMA200 3h slope 0.1179%. POC/VAH/VAL 0.3275/0.3306/0.3241. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 0.3324/0.3334/0.3321/0.3333; seeded EMA20/50 0.32985006/0.32940892; last 3 closes 0.3314, 0.3324, 0.3333. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 0.3305/0.3324/0.3298/0.3324; seeded EMA20/50 0.32960166/0.33101702; last 3 closes 0.3266, 0.3305, 0.3324. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"LONG","retrace":0.1579,"depth_sigma":3.3157,"velocity_ratio":2.8284,"bars_pullback":1,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 0.3293/0.3299/0.3273; prior week 0.3302/0.3327/0.3286; weekly VWAP 0.3295. Trap label TRAPPED_SELLERS_BELOW; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":11267107.55,"weekly_cvd_usd":514119.58,"cvd_24h_usd":5351030.64,"bar_delta_15m_usd":-173047.04,"divergence":"BULLISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":11267107.55,"flow_bias":"BULLISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 3,983.92 / -171,316.86 / -136,049.65 USD. Root-anchored partial sums 4,493.6 / -173,166.42 / -123,948.67 USD with 4/14/29 buckets. Root-anchored buy fractions 0.58985015 / 0.22167942 / 0.46926989; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 2,109,349.61/1,434,998.26; imbalance 0.1903; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 6, L2 elapsed>=180s 5. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.0001; HYPERLIQUID: -0.000095. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [0.327, 0.328] / 102,210.04 USD; top_buy_stop_clusters_above: n=10, first [0.336, 0.337] / 18,668.44 USD; nearest_sell_stop_clusters_below: n=10, first [0.332, 0.333] / 539.72 USD; nearest_buy_stop_clusters_above: n=10, first [0.333, 0.334] / 8,384.8 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [0.323, 0.324] / 11,335.41 USD; top_short_squeeze_bands_above: n=1, first [0.337, 0.338] / 136.35 USD; nearest_long_cascade_bands_below: n=10, first [0.325, 0.326] / 201.35 USD; nearest_short_squeeze_bands_above: n=1, first [0.337, 0.338] / 136.35 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":1.0,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.3332,"index_price":0.3335}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### DOT — DOTUSD.pi — NO SETUP

Source [lines 64888–70986](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L64888-L70986); JSON path `assets_matrix_24.DOT`.
- **Quotes/specs:** bid 1.128, ask 1.149, mid 1.1385; reported spread 0.021, 184.45 bps; reported age 12.42889714s. Contract 1000.0, lot min/step 0.01/0.01, max 40.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 0.21 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 1.1472, sigma 0.0114, Z -0.76, RSI 33.4, ATR 0.0058; 15m EMA20/50/200 1.1341/1.1441/1.1717, EMA200 3h slope -0.4472%. POC/VAH/VAL 1.1494/1.1674/1.1408. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 1.133/1.133/1.12/1.123; seeded EMA20/50 1.1512884/1.17327276; last 3 closes 1.14, 1.133, 1.123. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 1.155/1.155/1.132/1.133; seeded EMA20/50 1.18134984/1.18515167; last 3 closes 1.158, 1.155, 1.133. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.1463,"depth_sigma":0.6567,"velocity_ratio":1.6347,"bars_pullback":2,"bars_impulse":22,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 1.202/1.2099/1.1114; prior week 1.0931/1.2327/1.0731; weekly VWAP 1.1905. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-127420.04,"weekly_cvd_usd":-1318378.87,"cvd_24h_usd":-277983.81,"bar_delta_15m_usd":11988.24,"divergence":"BEARISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-127420.04,"flow_bias":"BEARISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 9,231.4 / 11,216.49 / 22,407.33 USD. Root-anchored partial sums 6,046.71 / 12,015.34 / 22,407.33 USD with 4/14/29 buckets. Root-anchored buy fractions 0.86302214 / 0.68877372 / 0.65788613; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 314,710.15/192,177.85; imbalance 0.2417; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.001; HYPERLIQUID: -0.00015. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [1.11, 1.12] / 152,087.25 USD; top_buy_stop_clusters_above: n=10, first [1.18, 1.19] / 7,486.81 USD; nearest_sell_stop_clusters_below: n=10, first [1.13, 1.14] / 12,172.77 USD; nearest_buy_stop_clusters_above: n=10, first [1.14, 1.15] / 148.67 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [1.08, 1.09] / 11,795.68 USD; top_short_squeeze_bands_above: n=7, first [1.19, 1.2] / 9,444.5 USD; nearest_long_cascade_bands_below: n=10, first [1.13, 1.14] / 326.17 USD; nearest_short_squeeze_bands_above: n=7, first [1.14, 1.15] / 425.51 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-0.37,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":1.139,"index_price":1.1402}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### LINK — LNKUSD.p — NO SETUP

Source [lines 70987–76972](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L70987-L76972); JSON path `assets_matrix_24.LINK`.
- **Quotes/specs:** bid 12.865, ask 12.954, mid 12.9095; reported spread 0.089, 68.94 bps; reported age 0.95227027s. Contract 100.0, lot min/step 0.1/0.1, max 100.0, tick 0.001, point 0.001, stops_level 10. Minimum-lot spread cash diagnostic 0.89 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 12.8928, sigma 0.0484, Z 0.35, RSI 48.08, ATR 0.0585; 15m EMA20/50/200 12.8652/12.8768/12.9161, EMA200 3h slope -0.0429%. POC/VAH/VAL 12.8502/12.9447/12.8313. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 12.873/12.93/12.816/12.842; seeded EMA20/50 12.87990674/12.91685762; last 3 closes 12.868, 12.874, 12.842. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 12.979/13.043/12.79/12.874; seeded EMA20/50 12.95112233/13.16495746; last 3 closes 12.898, 12.979, 12.874. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.3063,"depth_sigma":0.0783,"velocity_ratio":1.234,"bars_pullback":2,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 12.8842/13.1812/12.706; prior week 12.8345/13.2541/12.5704; weekly VWAP 12.9376. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-326965.83,"weekly_cvd_usd":-2248614.74,"cvd_24h_usd":-623811.33,"bar_delta_15m_usd":-28470.11,"divergence":"BEARISH_EXHAUSTION","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-326965.83,"flow_bias":"BEARISH_EXHAUSTION"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums -9,031.09 / -33,097.54 / -38,818.26 USD. Root-anchored partial sums -9,040.96 / -29,462.6 / -33,725.75 USD with 4/14/29 buckets. Root-anchored buy fractions 0.20992965 / 0.2759012 / 0.39094803; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 144,280.99/158,283.32; imbalance -0.0463; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.013; HYPERLIQUID: -0.00525. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [12.8, 12.9] / 181,712.16 USD; top_buy_stop_clusters_above: n=10, first [13.2, 13.3] / 18,718.4 USD; nearest_sell_stop_clusters_below: n=10, first [12.8, 12.9] / 181,712.16 USD; nearest_buy_stop_clusters_above: n=10, first [12.9, 13] / 149.91 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [12.6, 12.7] / 13,856.58 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [12.7, 12.8] / 1,393.15 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.19,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":12.921,"index_price":12.93}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### BCH — BCHUSD.p — NO SETUP

Source [lines 76973–83233](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L76973-L83233); JSON path `assets_matrix_24.BCH`.
- **Quotes/specs:** bid 277.96, ask 278.541, mid 278.2505; reported spread 0.581, 20.88 bps; reported age 10.11726141s. Contract 10.0, lot min/step 0.1/0.1, max 100.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 0.581 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 278.0869, sigma 1.4659, Z 0.11, RSI 46.26, ATR 1.1965; 15m EMA20/50/200 277.8232/277.069/275.6585, EMA200 3h slope 0.1042%. POC/VAH/VAL 273.61/277.36/266.86. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 277.56/278.16/276.137/277.26; seeded EMA20/50 275.99105623/275.46746306; last 3 closes 279.36, 277.66, 277.26. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 280.259/281.86/276.96/277.66; seeded EMA20/50 276.88678364/284.82966743; last 3 closes 276.26, 280.359, 277.66. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.1788,"depth_sigma":0.0015,"velocity_ratio":0.2704,"bars_pullback":4,"bars_impulse":6,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 270.8486/279.1008/267.9204; prior week 278.3776/284.9192/270.8296; weekly VWAP 275.0611. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":589487.88,"weekly_cvd_usd":-1130464.13,"cvd_24h_usd":823034.54,"bar_delta_15m_usd":35984.58,"divergence":"BULLISH_ABSORPTION","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":589487.88,"flow_bias":"BULLISH_ABSORPTION"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 5,634.01 / 36,171.45 / 32,967.32 USD. Root-anchored partial sums 5,480.64 / 36,171.45 / 33,471.25 USD with 4/14/29 buckets. Root-anchored buy fractions 0.88970281 / 0.96530245 / 0.66801559; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 343,335.98/454,680.5; imbalance -0.1395; ladder sizes 20/20. L3 count 10, L3 elapsed>=180s 0; L2 count 1, L2 elapsed>=180s 1. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.3; HYPERLIQUID: -0.1175. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x71d0e11ebb6150cebe20cf62f798be1a50108c26, source 273.24, mapped 273.1225, 87,981.37 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x71d0e11ebb6150cebe20cf62f798be1a50108c26, source 282.9, mapped 282.7825, 91,058.44 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [271, 272] / 158,170.12 USD; top_buy_stop_clusters_above: n=10, first [289, 290] / 6,869.36 USD; nearest_sell_stop_clusters_below: n=10, first [277, 278] / 73,298.49 USD; nearest_buy_stop_clusters_above: n=10, first [278, 279] / 182.97 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [270, 271] / 58,018.31 USD; top_short_squeeze_bands_above: n=2, first [303, 304] / 1,374.93 USD; nearest_long_cascade_bands_below: n=10, first [277, 278] / 832.98 USD; nearest_short_squeeze_bands_above: n=2, first [295, 296] / 496.56 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":0.83,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":278.48,"index_price":278.68}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### LTC — LTCUSD.pi — NO SETUP

Source [lines 83234–89374](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L83234-L89374); JSON path `assets_matrix_24.LTC`.
- **Quotes/specs:** bid 61.43, ask 61.73, mid 61.58; reported spread 0.3, 48.72 bps; reported age 4.01922774s. Contract 100.0, lot min/step 0.1/0.1, max 100.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 3 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 61.5028, sigma 0.2438, Z 0.32, RSI 44.72, ATR 0.1977; 15m EMA20/50/200 61.3937/61.4309/61.9188, EMA200 3h slope -0.1118%. POC/VAH/VAL 61.1753/61.7922/60.9166. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 61.45/61.52/61.1/61.245; seeded EMA20/50 61.46169145/61.91529535; last 3 closes 61.555, 61.45, 61.245. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 61.795/62.045/61.31/61.45; seeded EMA20/50 62.41391765/64.11544022; last 3 closes 61.285, 61.795, 61.45. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.1917,"depth_sigma":0.0088,"velocity_ratio":1.3505,"bars_pullback":3,"bars_impulse":21,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 61.2495/62.8074/60.1532; prior week 63.8584/64.914/61.1788; weekly VWAP 62.1173. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-590754.81,"weekly_cvd_usd":-2294031.4,"cvd_24h_usd":-1157174.53,"bar_delta_15m_usd":14731.95,"divergence":"BEARISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-590754.81,"flow_bias":"BEARISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 11,332.86 / 14,843.73 / -1,418.54 USD. Root-anchored partial sums 11,562.09 / 15,102.74 / -1,753.54 USD with 4/14/29 buckets. Root-anchored buy fractions 0.81741817 / 0.60682772 / 0.49395513; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 232,860.96/222,659.07; imbalance 0.0224; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.07; HYPERLIQUID: -0.044. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [59, 59.1] / 707,093.27 USD; top_buy_stop_clusters_above: n=10, first [64.6, 64.7] / 20,332.85 USD; nearest_sell_stop_clusters_below: n=10, first [61.5, 61.6] / 518.32 USD; nearest_buy_stop_clusters_above: n=10, first [61.6, 61.7] / 5,400.77 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [58.6, 58.7] / 677,098.45 USD; top_short_squeeze_bands_above: n=10, first [62.7, 62.8] / 177,772.98 USD; nearest_long_cascade_bands_below: n=10, first [61.5, 61.6] / 141.75 USD; nearest_short_squeeze_bands_above: n=10, first [61.7, 61.8] / 1,061.91 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-0.1,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":61.61,"index_price":61.65}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### AVAX — AVXUSD.p — NO SETUP

Source [lines 89375–95424](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L89375-L95424); JSON path `assets_matrix_24.AVAX`.
- **Quotes/specs:** bid 10.19, ask 10.22, mid 10.205; reported spread 0.03, 29.4 bps; reported age 8.19280696s. Contract 100.0, lot min/step 0.01/0.01, max 40.0, tick 0.01, point 0.01, stops_level 20. Minimum-lot spread cash diagnostic 0.03 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 10.2338, sigma 0.059, Z -0.49, RSI 47.94, ATR 0.0474; 15m EMA20/50/200 10.1818/10.2156/10.346, EMA200 3h slope -0.2181%. POC/VAH/VAL 10.2173/10.313/10.197. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 10.15/10.19/10.11/10.15; seeded EMA20/50 10.24055249/10.3478495; last 3 closes 10.17, 10.15, 10.15. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 10.32/10.32/10.13/10.15; seeded EMA20/50 10.40987952/10.56234626; last 3 closes 10.29, 10.32, 10.15. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.3182,"depth_sigma":0.084,"velocity_ratio":2.2437,"bars_pullback":3,"bars_impulse":21,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 10.4481/10.566/9.8586; prior week 10.314/10.8552/9.9368; weekly VWAP 10.4434. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":-143752.19,"weekly_cvd_usd":-892573.68,"cvd_24h_usd":949272.64,"bar_delta_15m_usd":7584.96,"divergence":"BULLISH_MOMENTUM","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-143752.19,"flow_bias":"BULLISH_MOMENTUM"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums 1,808.93 / 8,385.12 / 25,715.67 USD. Root-anchored partial sums 1,040.1 / 9,051.59 / 25,015.14 USD with 4/14/29 buckets. Root-anchored buy fractions 0.61959594 / 0.60770717 / 0.61712777; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 154,002.28/130,894.63; imbalance 0.0811; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.0125; HYPERLIQUID: -0.0045. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [10, 10.1] / 291,842.97 USD; top_buy_stop_clusters_above: n=10, first [10.6, 10.7] / 221,597.86 USD; nearest_sell_stop_clusters_below: n=10, first [10.1, 10.2] / 5,596.32 USD; nearest_buy_stop_clusters_above: n=10, first [10.2, 10.3] / 205.21 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [9.8, 9.9] / 189,941.28 USD; top_short_squeeze_bands_above: n=2, first [10.2, 10.3] / 199.69 USD; nearest_long_cascade_bands_below: n=10, first [10.1, 10.2] / 1,073.85 USD; nearest_short_squeeze_bands_above: n=2, first [10.2, 10.3] / 199.69 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":-0.36,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":10.212,"index_price":10.219}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### NEAR — NERUSD.p — NO SETUP

Source [lines 95425–101540](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L95425-L101540); JSON path `assets_matrix_24.NEAR`.
- **Quotes/specs:** bid 5.052, ask 5.082, mid 5.067; reported spread 0.03, 59.21 bps; reported age 1.01696396s. Contract 100.0, lot min/step 1.0/1.0, max 1000.0, tick 0.001, point 0.001, stops_level 20. Minimum-lot spread cash diagnostic 3 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 5.0626, sigma 0.0468, Z 0.09, RSI 51.43, ATR 0.0471; 15m EMA20/50/200 5.0287/5.0444/5.1728, EMA200 3h slope -0.3718%. POC/VAH/VAL 5.0395/5.0718/4.918. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 5.004/5.043/4.949/5.012; seeded EMA20/50 5.05826371/5.17430649; last 3 closes 5.021, 5.004, 5.012. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 5.067/5.131/4.97/5.004; seeded EMA20/50 5.20912531/5.17672013; last 3 closes 5.121, 5.067, 5.004. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 96, daily 96; pullback {"direction":"SHORT","retrace":0.511,"depth_sigma":0.1975,"velocity_ratio":0.7732,"bars_pullback":4,"bars_impulse":6,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 5.6134/5.6602/5.1174; prior week 5.0184/5.7839/4.8994; weekly VWAP 5.3058. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"session_cvd_usd":922785.54,"weekly_cvd_usd":1517896.71,"cvd_24h_usd":12570333.4,"bar_delta_15m_usd":73204.88,"divergence":"BEARISH_EXHAUSTION","bars_count":191}`. TradFi flow: `{"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":922785.54,"flow_bias":"BEARISH_EXHAUSTION"}`. Respect tick-vs-USD units.
- **Minute evidence:** last-observed 5/15/30 sums -25,737.62 / 78,370.69 / 116,590.56 USD. Root-anchored partial sums -31,261.72 / 82,069.46 / 127,407.85 USD with 4/14/29 buckets. Root-anchored buy fractions 0.43912465 / 0.56067597 / 0.55776047; final minute absent, not zero.
- **Book:** venue BINANCE_USDM_FUTURES_AND_HYPERLIQUID; bid/ask top20 cash 303,330.71/296,543.85; imbalance 0.0113; ladder sizes 20/20. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** BINANCE: -0.00225; HYPERLIQUID: 0.00025. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [4.9, 4.91] / 552,660.24 USD; top_buy_stop_clusters_above: n=10, first [5.29, 5.3] / 264,400.76 USD; nearest_sell_stop_clusters_below: n=10, first [5.06, 5.07] / 6,913.37 USD; nearest_buy_stop_clusters_above: n=10, first [5.07, 5.08] / 150.53 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [4.85, 4.86] / 793,693.93 USD; top_short_squeeze_bands_above: n=8, first [5.13, 5.14] / 163,655.18 USD; nearest_long_cascade_bands_below: n=10, first [5.06, 5.07] / 145,771.66 USD; nearest_short_squeeze_bands_above: n=8, first [5.07, 5.08] / 18,380.23 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `{"last_funding_rate_bps":1.0,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":5.0663,"index_price":5.0681}`; funding-history observations 8. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### SP500 — SP500.p — WATCHLIST

Source [lines 101541–107666](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L101541-L107666); JSON path `assets_matrix_24.SP500`.
- **Quotes/specs:** bid 7,818.02, ask 7,818.32, mid 7,818.17; reported spread 0.3, 0.38 bps; reported age 0.97394991s. Contract 10.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.03 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 7,816.7763, sigma 5.064, Z 0.28, RSI 49.37, ATR 4.5778; 15m EMA20/50/200 7,820.5882/7,816.7681/7,808.5649, EMA200 3h slope 0.0214%. POC/VAH/VAL 7,802.4818/7,814.4472/7,788.0408. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 7,819.21/7,825.55/7,817.54/7,824.71; seeded EMA20/50 7,813.10258295/7,807.50226372; last 3 closes 7,818.39, 7,819.22, 7,824.71. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 7,824.74/7,825.21/7,807.55/7,819.22; seeded EMA20/50 7,804.33231964/7,783.8033865; last 3 closes 7,810.24, 7,824.73, 7,819.22. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":1.0277,"depth_sigma":0.0,"velocity_ratio":0.2141,"bars_pullback":24,"bars_impulse":5,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 7,797.7869/7,809.6636/7,786.63; prior week 7,800.7082/7,827.2664/7,771.3544; weekly VWAP 7,808.8229. Trap label TRAPPED_SELLERS_BELOW; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-81.0,"divergence":"SELLER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-81.0,"15m_tick_cvd":-81.0,"5m_tick_cvd":-81.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 2,845,987.44/1,050,993.52; imbalance 0.4606; ladder sizes 20/20. L3 count 91, L3 elapsed>=180s 0; L2 count 10, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: 1.31. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x354bcb431a332079950d2ce3a4698745e0f66425, source 7,791.1, mapped 7,792.41, 1,999,998.74 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x354bcb431a332079950d2ce3a4698745e0f66425, source 7,846.1, mapped 7,847.41, 2,000,010.12 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [7,720, 7,730] / 3,290,139.66 USD; top_buy_stop_clusters_above: n=10, first [7,840, 7,850] / 3,683,092.17 USD; nearest_sell_stop_clusters_below: n=10, first [7,810, 7,820] / 29,913.77 USD; nearest_buy_stop_clusters_above: n=10, first [7,820, 7,830] / 1,740,839.25 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [7,660, 7,670] / 9,804,000.41 USD; top_short_squeeze_bands_above: n=1, first [7,820, 7,830] / 2,501.94 USD; nearest_long_cascade_bands_below: n=10, first [7,810, 7,820] / 2,470.66 USD; nearest_short_squeeze_bands_above: n=1, first [7,820, 7,830] / 2,501.94 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### NAS100 — NAS100.p — WATCHLIST

Source [lines 107667–114063](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L107667-L114063); JSON path `assets_matrix_24.NAS100`.
- **Quotes/specs:** bid 30,515.92, ask 30,516.98, mid 30,516.45; reported spread 1.06, 0.35 bps; reported age 0.7417419s. Contract 10.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.106 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 30,591.1536, sigma 33.5232, Z -2.23, RSI 41.26, ATR 37.0213; 15m EMA20/50/200 30,572.5438/30,575.9977/30,622.0814, EMA200 3h slope -0.0213%. POC/VAH/VAL 30,550.3151/30,602.3198/30,479.9558. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 30,558.07/30,586.94/30,520.82/30,571.82; seeded EMA20/50 30,570.73936623/30,618.71879201; last 3 closes 30,589.82, 30,558.19, 30,571.82. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 30,646.42/30,649.21/30,484.25/30,558.19; seeded EMA20/50 30,676.92291275/30,748.50619521; last 3 closes 30,589.21, 30,646.28, 30,558.19. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"SHORT","retrace":0.2709,"depth_sigma":0.0,"velocity_ratio":0.0905,"bars_pullback":18,"bars_impulse":6,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 30,666.6681/30,712.0578/30,419.5464; prior week 30,993.9557/31,304.0766/30,703.8426; weekly VWAP 30,625.5926. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-41.0,"divergence":"SELLER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-41.0,"15m_tick_cvd":-41.0,"5m_tick_cvd":-41.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 4,984,822.77/5,117,718.15; imbalance -0.0132; ladder sizes 20/20. L3 count 97, L3 elapsed>=180s 0; L2 count 23, L2 elapsed>=180s 11. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: -18.545. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xe724acd020fbd65ddb42a0f05dcfb65489480320, source 30,481, mapped 30,462.455, 1,084,017.14 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xe724acd020fbd65ddb42a0f05dcfb65489480320, source 30,660, mapped 30,641.455, 1,082,856.01 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [30,000, 30,100] / 913,011.91 USD; top_buy_stop_clusters_above: n=10, first [31,300, 31,400] / 1,082,965.75 USD; nearest_sell_stop_clusters_below: n=10, first [30,500, 30,600] / 73,163.41 USD; nearest_buy_stop_clusters_above: n=10, first [30,600, 30,700] / 379,196.43 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [29,100, 29,200] / 15,444,048.74 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [30,300, 30,400] / 163,983.69 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### DJ30 — DJ30.p — NO SETUP

Source [lines 114064–117171](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L114064-L117171); JSON path `assets_matrix_24.DJ30`.
- **Quotes/specs:** bid 51,832.31, ask 51,833.49, mid 51,832.9; reported spread 1.18, 0.23 bps; reported age 0.8163197s. Contract 10.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.118 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 51,778.4925, sigma 80.4914, Z 0.68, RSI 53.01, ATR 36.5318; 15m EMA20/50/200 51,841.2215/51,802.4485/51,783.1592, EMA200 3h slope 0.0207%. POC/VAH/VAL 51,776.11/51,923.36/51,628.86. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 51,851.16/51,932.66/51,848.66/51,922.66; seeded EMA20/50 51,798.2220271/51,765.06604639; last 3 closes 51,794.16, 51,850.16, 51,922.66. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 51,779.26/51,869.16/51,726.16/51,850.16; seeded EMA20/50 51,717.63294787/51,561.13586327; last 3 closes 51,668.66, 51,779.76, 51,850.16. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":0.4424,"depth_sigma":0.0,"velocity_ratio":1.1489,"bars_pullback":5,"bars_impulse":13,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 51,820.484/51,895.312/51,653.56; prior week 51,095.701/51,700.606/50,940.154; weekly VWAP 51,858.7467. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-27.0,"divergence":"SELLER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-27.0,"15m_tick_cvd":-27.0,"5m_tick_cvd":-21.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue None; bid/ask top20 cash unavailable/unavailable; imbalance unavailable; ladder sizes 0/0. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** unavailable. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=0, first none observed; top_buy_stop_clusters_above: n=0, first none observed; nearest_sell_stop_clusters_below: n=0, first none observed; nearest_buy_stop_clusters_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=0, first none observed; top_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### GER40 — GER40.p — NO SETUP

Source [lines 117172–120279](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L117172-L120279); JSON path `assets_matrix_24.GER40`.
- **Quotes/specs:** bid 25,416.25, ask 25,417.05, mid 25,416.65; reported spread 0.8, 0.31 bps; reported age 0.66409898s. Contract 10.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.08 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 25,343.3691, sigma 36.7556, Z 1.99, RSI 53.2, ATR 32.8046; 15m EMA20/50/200 25,369.9426/25,343.6847/25,284.1281, EMA200 3h slope 0.0491%. POC/VAH/VAL 25,302.36/25,350.2/25,250.36. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 25,370.1/25,425.1/25,357.05/25,423.1; seeded EMA20/50 25,329.6249913/25,277.42943621; last 3 closes 25,327.55, 25,371.1, 25,423.1. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 25,339.15/25,395.1/25,275/25,371.1; seeded EMA20/50 25,252.78960228/25,242.22970594; last 3 closes 25,287.15, 25,339.65, 25,371.1. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":0.3121,"depth_sigma":0.0,"velocity_ratio":0.8306,"bars_pullback":3,"bars_impulse":8,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 25,254.5085/25,288.172/25,215.666; prior week 25,248.1455/25,493.286/25,107.004; weekly VWAP 25,290.7111. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":11.0,"divergence":"BUYER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":11.0,"15m_tick_cvd":11.0,"5m_tick_cvd":15.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue None; bid/ask top20 cash unavailable/unavailable; imbalance unavailable; ladder sizes 0/0. L3 count 0, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** unavailable. Map source venue only; separate residual uncertainty from median.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=0, first none observed; top_buy_stop_clusters_above: n=0, first none observed; nearest_sell_stop_clusters_below: n=0, first none observed; nearest_buy_stop_clusters_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=0, first none observed; top_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### GOLD — XAUUSD.pi — WATCHLIST

Source [lines 120280–125638](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L120280-L125638); JSON path `assets_matrix_24.GOLD`.
- **Quotes/specs:** bid 4,141, ask 4,141.07, mid 4,141.035; reported spread 0.07, 0.17 bps; reported age 0.63099265s. Contract 100.0, lot min/step 0.01/0.01, max 50.0, tick 0.01, point 0.01, stops_level 0. Minimum-lot spread cash diagnostic 0.07 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 4,154.3049, sigma 7.0144, Z -1.89, RSI 42.66, ATR 5.5755; 15m EMA20/50/200 4,147.5259/4,153.7067/4,165.2173, EMA200 3h slope -0.0618%. POC/VAH/VAL 4,159.5214/4,170.286/4,145.6812. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 4,143.31/4,145.66/4,141.14/4,143.75; seeded EMA20/50 4,157.8210824/4,164.84322845; last 3 closes 4,149.5, 4,143.3, 4,143.75. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 4,165.62/4,166.17/4,141.41/4,143.3; seeded EMA20/50 4,164.36544694/4,167.92320815; last 3 closes 4,155.06, 4,165.74, 4,143.3. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"SHORT","retrace":0.1531,"depth_sigma":0.0002,"velocity_ratio":3.3781,"bars_pullback":1,"bars_impulse":22,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 4,167.1239/4,179.5814/4,158.6528; prior week 4,164.4375/4,178.005/4,111.675; weekly VWAP 4,173.68. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-8.0,"divergence":"SELLER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-8.0,"15m_tick_cvd":-8.0,"5m_tick_cvd":-8.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.006,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 1,278,751.06/1,529,166.89; imbalance -0.0892; ladder sizes 20/20. L3 count 58, L3 elapsed>=180s 0; L2 count 5, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: -1.18. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xee02fd4a30098447215ec0052e4236e077a7309d, source 4,076, mapped 4,074.82, 2,038,000 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x31dea2516beee92135b96f464eeec3cf292a13f2, source 4,178.2, mapped 4,177.02, 1,064,605.36 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [3,980, 3,990] / 10,645,251.76 USD; top_buy_stop_clusters_above: n=10, first [4,220, 4,230] / 399,496.61 USD; nearest_sell_stop_clusters_below: n=10, first [4,130, 4,140] / 488,428.91 USD; nearest_buy_stop_clusters_above: n=10, first [4,140, 4,150] / 26,384.41 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [4,090, 4,100] / 1,001,959.92 USD; top_short_squeeze_bands_above: n=4, first [4,160, 4,170] / 42,491.73 USD; nearest_long_cascade_bands_below: n=10, first [4,130, 4,140] / 263.92 USD; nearest_short_squeeze_bands_above: n=4, first [4,160, 4,170] / 42,491.73 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### SILVER — XAGUSD.pi — NO SETUP

Source [lines 125639–130971](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L125639-L130971); JSON path `assets_matrix_24.SILVER`.
- **Quotes/specs:** bid 58.442, ask 58.478, mid 58.46; reported spread 0.036, 6.16 bps; reported age 0.97016478s. Contract 5000.0, lot min/step 0.01/0.01, max 100.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 1.8 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BEARISH; VWAP 58.8794, sigma 0.2473, Z -1.7, RSI 42.99, ATR 0.1641; 15m EMA20/50/200 58.667/58.9027/59.6162, EMA200 3h slope -0.22%. POC/VAH/VAL 59.1363/59.4168/58.381. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 58.514/58.61/58.439/58.566; seeded EMA20/50 59.10740787/59.57885966; last 3 closes 58.653, 58.516, 58.566. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 59.313/59.317/58.381/58.516; seeded EMA20/50 59.80053613/60.40016965; last 3 closes 59.034, 59.313, 58.516. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"SHORT","retrace":0.2021,"depth_sigma":0.0048,"velocity_ratio":0.0565,"bars_pullback":18,"bars_impulse":5,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 60.5126/60.7134/60.1937; prior week 60.8954/61.6606/59.6928; weekly VWAP 60.0313. Trap label TRAPPED_BUYERS_ABOVE; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":14.0,"divergence":"BUYER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":14.0,"15m_tick_cvd":14.0,"5m_tick_cvd":13.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 1,425,157.52/1,066,123.89; imbalance 0.1441; ladder sizes 20/20. L3 count 53, L3 elapsed>=180s 0; L2 count 6, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: -0.0255. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x5a209e55c592687bb3f105f2f645c09238612d1b, source 58.135, mapped 58.1095, 833,608.81 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x5a209e55c592687bb3f105f2f645c09238612d1b, source 58.778, mapped 58.7525, 772,123.68 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [57.8, 57.9] / 382,157.44 USD; top_buy_stop_clusters_above: n=10, first [60.8, 60.9] / 452,161.05 USD; nearest_sell_stop_clusters_below: n=10, first [58.4, 58.5] / 256,744.07 USD; nearest_buy_stop_clusters_above: n=10, first [58.5, 58.6] / 30,617.62 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [57.4, 57.5] / 716,694.68 USD; top_short_squeeze_bands_above: n=10, first [58.5, 58.6] / 263,367.59 USD; nearest_long_cascade_bands_below: n=10, first [58.4, 58.5] / 113,361.61 USD; nearest_short_squeeze_bands_above: n=10, first [58.5, 58.6] / 263,367.59 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### USWTI — USWTI.p — WATCHLIST

Source [lines 130972–136089](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L130972-L136089); JSON path `assets_matrix_24.USWTI`.
- **Quotes/specs:** bid 95.586, ask 95.632, mid 95.609; reported spread 0.046, 4.81 bps; reported age 1.36118746s. Contract 100.0, lot min/step 0.01/0.01, max 100.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 0.046 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 94.9001, sigma 0.3709, Z 1.91, RSI 64.45, ATR 0.3085; 15m EMA20/50/200 94.8831/94.7551/93.8591, EMA200 3h slope 0.1289%. POC/VAH/VAL 94.2935/95.4864/94.0404. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 94.539/95.185/94.139/95.129; seeded EMA20/50 94.5353008/93.88779366; last 3 closes 94.409, 94.534, 95.129. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 94.896/94.996/94.18/94.534; seeded EMA20/50 93.48651722/92.98718941; last 3 closes 95.192, 94.891, 94.534. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":0.0165,"depth_sigma":0.0006,"velocity_ratio":0.0328,"bars_pullback":2,"bars_impulse":4,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 94.17/94.4688/93.0021; prior week 91.35/93.4542/90.1164; weekly VWAP 93.3973. Trap label TRAPPED_SELLERS_BELOW; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-3.0,"divergence":"NEUTRAL"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-3.0,"15m_tick_cvd":-3.0,"5m_tick_cvd":22.0,"flow_bias":"NEUTRAL","order_flow_imbalance_ofi":0.004,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 576,860.22/615,074.2; imbalance -0.0321; ladder sizes 20/20. L3 count 51, L3 elapsed>=180s 0; L2 count 2, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: 1.22075. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x354bcb431a332079950d2ce3a4698745e0f66425, source 94.042, mapped 95.26275, 999,998.62 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0x354bcb431a332079950d2ce3a4698745e0f66425, source 94.675, mapped 95.89575, 999,997.02 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [92.9, 93] / 942,886.89 USD; top_buy_stop_clusters_above: n=10, first [94.9, 95] / 329,285.88 USD; nearest_sell_stop_clusters_below: n=10, first [94.3, 94.4] / 160,319.71 USD; nearest_buy_stop_clusters_above: n=10, first [94.4, 94.5] / 7,659.54 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [90.7, 90.8] / 927,805.12 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [94.1, 94.2] / 5,043.24 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### EURUSD — EURUSD.pi — NO SETUP

Source [lines 136090–140354](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L136090-L140354); JSON path `assets_matrix_24.EURUSD`.
- **Quotes/specs:** bid 1.119, ask 1.119, mid 1.119; reported spread 0, 0.09 bps; reported age 1.74270749s. Contract 100000.0, lot min/step 0.01/0.01, max 100.0, tick 1e-05, point 1e-05, stops_level 0. Minimum-lot spread cash diagnostic unavailable USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** RANGE_BOUND; VWAP 1.1202, sigma 0.0005, Z -2.23, RSI 36.3, ATR 0.0004; 15m EMA20/50/200 1.1198/1.12/1.1194, EMA200 3h slope 0.0023%. POC/VAH/VAL 1.1192/1.1201/1.1184. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 1.11948/1.11981/1.11903/1.11935; seeded EMA20/50 1.11981756/1.119262; last 3 closes 1.11993, 1.1195, 1.11935. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 1.12092/1.12114/1.11949/1.1195; seeded EMA20/50 1.11943556/1.12216623; last 3 closes 1.12033, 1.12091, 1.1195. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"SHORT","retrace":0.1227,"depth_sigma":0.5584,"velocity_ratio":1.7197,"bars_pullback":1,"bars_impulse":14,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 1.1158/1.1179/1.1151; prior week 1.1195/1.1231/1.1183; weekly VWAP 1.1189. Trap label TRAPPED_SELLERS_BELOW; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-18.0,"divergence":"SELLER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":705,"session_tick_cvd":-18.0,"15m_tick_cvd":-19.0,"5m_tick_cvd":-4.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.001,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 514,085.95/432,464.32; imbalance 0.0862; ladder sizes 20/20. L3 count 14, L3 elapsed>=180s 0; L2 count 0, L2 elapsed>=180s 0. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: -0.00043. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0x2ac4880624dae9e823874d65e43bfeba97fc61b5, source 1.1027, mapped 1.10227, 551,350 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xfc667adba8d4837586078f4fdcdc29804337ca06, source 1.1341, mapped 1.13367, 243,064.85 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [1.11, 1.12] / 363,467.73 USD; top_buy_stop_clusters_above: n=10, first [1.13, 1.14] / 654,851.38 USD; nearest_sell_stop_clusters_below: n=10, first [1.11, 1.12] / 363,467.73 USD; nearest_buy_stop_clusters_above: n=10, first [1.12, 1.13] / 225,975.09 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [1.09, 1.1] / 881,011.63 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [1.11, 1.12] / 649,849.23 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### GBPUSD — GBPUSD.pi — WATCHLIST

Source [lines 140355–144417](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L140355-L144417); JSON path `assets_matrix_24.GBPUSD`.
- **Quotes/specs:** bid 1.3264, ask 1.3265, mid 1.3265; reported spread 0, 0.08 bps; reported age 1.87724519s. Contract 100000.0, lot min/step 0.01/0.01, max 100.0, tick 1e-05, point 1e-05, stops_level 0. Minimum-lot spread cash diagnostic unavailable USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 1.3266, sigma 0.0005, Z -0.24, RSI 52.43, ATR 0.0005; 15m EMA20/50/200 1.3265/1.3263/1.3246, EMA200 3h slope 0.0168%. POC/VAH/VAL 1.3243/1.3262/1.3238. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 1.32615/1.3269/1.32604/1.32668; seeded EMA20/50 1.32585164/1.32455411; last 3 closes 1.32595, 1.32615, 1.32668. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 1.32746/1.32749/1.32566/1.32615; seeded EMA20/50 1.32405136/1.32377603; last 3 closes 1.32613, 1.32745, 1.32615. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":2.6875,"depth_sigma":0.2815,"velocity_ratio":0.1169,"bars_pullback":23,"bars_impulse":1,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 1.3234/1.3238/1.3214; prior week 1.321/1.3247/1.3203; weekly VWAP 1.324. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":16.0,"divergence":"BUYER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":16.0,"15m_tick_cvd":16.0,"5m_tick_cvd":20.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.016,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 340,633.13/201,546.88; imbalance 0.2565; ladder sizes 20/20. L3 count 10, L3 elapsed>=180s 0; L2 count 1, L2 elapsed>=180s 1. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: -0.0001775. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xde0e9b1a35322a809165d09f0490cca3fa7562e5, source 1.3255, mapped 1.3253225, 132,550 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xde0e9b1a35322a809165d09f0490cca3fa7562e5, source 1.328, mapped 1.3278225, 132,800 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=7, first [1.26, 1.27] / 198,089.24 USD; top_buy_stop_clusters_above: n=5, first [1.33, 1.34] / 331,718.98 USD; nearest_sell_stop_clusters_below: n=7, first [1.32, 1.33] / 368.79 USD; nearest_buy_stop_clusters_above: n=5, first [1.33, 1.34] / 331,718.98 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [1.31, 1.32] / 126,134.45 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [1.32, 1.33] / 5,100.78 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

### USDJPY — USDJPY.pi — NO SETUP

Source [lines 144418–149298](https://github.com/kbsingh1399/Trading_2/blob/49aa55fdb434bbf92a8e4923249c69ea5495c0a6/docs/telemetry/live_snapshot_latest.json#L144418-L149298); JSON path `assets_matrix_24.USDJPY`.
- **Quotes/specs:** bid 158.437, ask 158.438, mid 158.4375; reported spread 0.001, 0.06 bps; reported age 1.5500133s. Contract 100000.0, lot min/step 0.01/0.01, max 100.0, tick 0.001, point 0.001, stops_level 0. Minimum-lot spread cash diagnostic 0.00631164 USD, not a full-cost/risk-qualified trade.
- **Causal/profile:** BULLISH; VWAP 158.3403, sigma 0.0946, Z 1.03, RSI 58.67, ATR 0.0528; 15m EMA20/50/200 158.3858/158.3468/158.3336, EMA200 3h slope 0.0076%. POC/VAH/VAL 158.3277/158.4753/158.2513. MT5 tick-volume proxies, not exchange contract volume.
- **htf_1h_ohlcv:** 95 completed observations; last O/H/L/C 158.462/158.483/158.405/158.442; seeded EMA20/50 158.32869838/158.33029422; last 3 closes 158.34, 158.462, 158.442. No warmed EMA200 certification.
- **htf_4h_ohlcv:** 96 completed observations; last O/H/L/C 158.148/158.463/158.113/158.462; seeded EMA20/50 158.29215303/158.14511912; last 3 closes 158.445, 158.148, 158.462. No warmed EMA200 certification.
- **Other bars/pullback:** broker15m 100, exchange4h 0, daily 0; pullback {"direction":"LONG","retrace":0.1324,"depth_sigma":0.0024,"velocity_ratio":0.3528,"bars_pullback":6,"bars_impulse":16,"source":"PRODUCED_15M_BARS"}. Structural direction does not automatically establish a completed hold.
- **Auction memory:** prior day POC/VAH/VAL 158.2828/158.6048/157.832; prior week 158.1439/158.4542/158.057; weekly VWAP 158.3337. Trap label BALANCED; label alone is not a price-bin footprint.
- **Multi-horizon flow:** `{"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":10.0,"divergence":"BUYER_AGGRESSION"}`. TradFi flow: `{"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":10.0,"15m_tick_cvd":10.0,"5m_tick_cvd":10.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.001,"source":"MT5_L1_TICK_STREAM"}`. Respect tick-vs-USD units.
- **Minute evidence:** exchange taker minute arrays unavailable; no 30m USD CVD fabricated from broker ticks.
- **Book:** venue HYPERLIQUID_HIP3_PERP_DEX; bid/ask top20 cash 854,854.9/1,097,322.81; imbalance -0.1242; ladder sizes 20/20. L3 count 39, L3 elapsed>=180s 0; L2 count 5, L2 elapsed>=180s 3. Elapsed count is not continuous-persistence certification.
- **Basis by venue:** HYPERLIQUID: 0.089. Map source venue only; separate residual uncertainty from median.
- **Largest L3 bid:** 0xde0e9b1a35322a809165d09f0490cca3fa7562e5, source 158.25, mapped 158.339, 316,500 USD, elapsed 0s, samples 1. Not authorized defense.
- **Largest L3 ask:** 0xa3555141f2ea7ed01e1d5a6589c4355ccaa31bf5, source 160.8, mapped 160.889, 1,608,000 USD, elapsed 0s, samples 1. Not authorized defense.
- **structural_stop_clusters:** top_sell_stop_clusters_below: n=10, first [155, 156] / 116,096.38 USD; top_buy_stop_clusters_above: n=10, first [161, 162] / 258,269.09 USD; nearest_sell_stop_clusters_below: n=10, first [157, 158] / 28,931.46 USD; nearest_buy_stop_clusters_above: n=10, first [158, 159] / 12,383.36 USD. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **reconstructed_liquidations:** top_long_cascade_bands_below: n=10, first [150, 151] / 1,496,229.89 USD; top_short_squeeze_bands_above: n=0, first none observed; nearest_long_cascade_bands_below: n=10, first [157, 158] / 4,411.77 USD; nearest_short_squeeze_bands_above: n=0, first none observed. Source bounds; every supplied band is retained in the evidence ledger, including top/nearest overlaps.
- **Funding/carry:** current `null`; funding-history observations 0. Missing predicted funding remains unknown. Macro CPI and stress constraints are shared, not recomputed from this asset's price label.
- **Producer annotations:** `UNAVAILABLE_UNVERIFIED_ORDERFLOW`; p_win=0.4197, calibrated=False, sample=17. Read as provenance only; no retired permission boolean supplies the engine verdict.

## Appendix B — input manifest and reproducibility

The full audit ledger is `CYCLE92_ASTRA_EVIDENCE.json`. Its derived calculations are diagnostics, not executable orders. Retrieve the primary raw JSON with GitHub API contents at the pinned commit, verify the SHA-256 above, and reproduce EMA20/50 using alpha=2/(n+1) seeded from the first supplied completed close. For root-anchored CVD use the floor of root as_of to the minute as the right edge, include only buckets with `ts >= end−60N` and `ts+60 <= end`, and report coverage. Last-observed windows explicitly end at the last supplied bucket end. For wall counts inspect actual duration, size, side, location and continuity; do not use a retired eligibility flag.

| Source before changes | Bytes | SHA-256 |
|---|---:|---|
| `docs/specs/TRADE_DECISION_PLAYBOOK.md` | 47450 | `48d64f5ee1e00f91672120bb53d6252d1eed6df80793768e4e46d9577b86187e` |
| `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` | 2807122 | `9cdd190108d6dca35ef1b9584a3954d8154f4b67ad338d65d1b42bf7e40fdd0f` |
| `.agents/rules/ACTIVE_CONTEXT.md` | 30965 | `1a5f24f9ff00a9b2922dd66cb2fcb854557e0d121d6cfb3b452e9337f4f9f5d2` |
| `.agents/memory/session_chat_history.md` | 3617333 | `0c9411d88dc108103b839e49e8c5f18f1c5f5ff54f4f13b1e4675263080dddd2` |
| `.agent/skills/arena/SKILL.md` | 19011 | `c06f9828566485d5bd6507150f454d6f37d49c2b02e5308b8f744a4a046bdf39` |
| `.agent/skills/arena/rubric.md` | 3717 | `3296801e01035f3ad8dc2b57f0c47d84d296bbc716bf8b36bdb02b426c2735a5` |

### Publication-time synchronization note

The first push was rejected because the session branch advanced remotely. A non-destructive merge preserved the incoming telemetry (11:18:01 UTC) and the other council report `ARENA_COUNCIL_REPORT_20261014_1100Z.md`. Both complete desk appendices are retained. That newer telemetry and the other council verdict were not substituted into this exact-generation analysis, and their arrival is not independent validation of this report.
