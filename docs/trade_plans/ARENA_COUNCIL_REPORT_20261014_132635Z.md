# Trading Desk Council — Cycle 95

## 1. Source verification and executive ruling

**0 CANDIDATES / 7 WATCHLIST / 17 NO SETUP. No new order is certified. Account flat: 0 open positions, 0 pending orders; no ratchet, SL/TP modification or cancellation is needed. These are structural/flow/geometry/friction conclusions, not macro-event vetoes.**

Exact primary source: [docs/telemetry/live_snapshot_latest.json at 22810273c5aa7d15aa5f42e79e79316909e1ad34](https://github.com/kbsingh1399/Trading_2/blob/22810273c5aa7d15aa5f42e79e79316909e1ad34/docs/telemetry/live_snapshot_latest.json).

- Generation **`db2eba4fe0f9443cbdb5bdc3b13b78a4`**, **2026-10-14 13:26:35 UTC**.
- SHA-256 **`6b650cf694a794ba90827ad1581252d98bd63c1892f4074228083a23fd2f3740`**.
- Playbook, order desk, ACTIVE_CONTEXT, session history, installed arena SKILL/rubric and initial-risk registry retrieved at the same commit. Full source hashes, per-asset block inventories and calculation receipts accompany this report in `ARENA_COUNCIL_EVIDENCE_20261014_132635Z.json`.
- Calendar: **Fed Beige Book, 18:00 UTC; blackout_active=false; blackout_enforcement=DISABLED_BY_OPERATOR; purge_deadline and runway null**. Event is descriptive context only; no timed halt/purge or event-based disqualification is applied. No claim of independently verifying the official calendar or auditing every remote enforcement daemon.
- Portfolio: balance/equity/free margin **4,859.55 USD**, used margin **0**, active/pending arrays empty, contingent stress **0**. Available slots **4**.

**Reading scope:** complete-file byte/line indexing and recursive all-value JSON traversal; substantive all-asset/all-block, playbook/skill and relevant historical/autopsy review. This is not a claim of manually interpreting every historical archive line. The required text sources except desk match previously reviewed copies; upstream history/context still contain stale BTC OPEN references. New telemetry takes precedence for inventory.

**Policy conflicts:** current user RANGE_BOUND/UNDEFINED exclusion overrides playbook §7.3's range-only Engine 1 language; disabled macro enforcement overrides older §5 runway rules; 7.50–14.50 risk overrides older 10 USD floors; §7.4 actual-ticket friction overrides copied historical percentages. Engine 2 is evaluated independently of |Z|. Model 2 requires the stronger 0.50–0.75 ATR shelf buffer plus outside-band placement; smaller generic buffers do not replace that obligation. No retired decision-gate module or producer eligibility boolean supplies a verdict.

This session is fixed to **arena/d6de1eb4-trading-2**. Publication, if successful, is to this branch only, not the requested differently named branch. No MT5 execution is performed here. This is a pinned historical-as-of analysis, not a fresh order receipt at the time of later reading.

## 2. Mandate 1 — complete dual-engine screen

Both engines are evaluated for every asset. WATCHLIST means future research, not an authorized resting limit. Shelf values below are broker indicators; external walls/bands are separately translated with their own venue basis. There are 96 supplied completed 1H and 4H bars per asset. Finite-history EMA20/50 diagnostics are computed, but a warmed 200-period HTF stack cannot be certified from those arrays.

| Asset / MT5 symbol | Engine 1: extreme mean-reversion verdict | Engine 2: trend-pullback verdict | Final |
|---|---|---|---|
| BTC / BTCUSD.pi | **Z −3.31**, extreme, but long prohibited by BEARISH regime/4H and severe adverse 15/30m flow. Five-minute recovery is not a confirmed absorbed flush. | BEARISH label, mixed 1H stack, bearish 4H. EMA20/50 **83,200.2016 /83,308.3314** are distant; nearer primary ask **82,880.5** is 1.22 ATR away. Velocity **1.2368**, retrace **−0.1359**, no held relief shelf; new stop/target geometry unproved. | **WATCHLIST** |
| ETH / ETHUSD.pi | **Z −3.13**, but long prohibited in bearish HTFs; all 5/15/30m deltas negative, no exhaustion proof. | BEARISH HTFs; EMA20/50 **2,494.4344 /2,499.6743**. Nearer seasoned ask **2,474.75** is within 0.79 ATR, so not discarded for distance. Velocity **3.2545**, negative retrace, illustrative stop in adjacent band and excessive friction prevent staging. | **WATCHLIST** |
| SOL / SOLUSD.p | **Z −2.69**, but bearish-regime long prohibited. Positive session/5m does not override negative 15/30m or HTFs. | BEARISH HTFs; EMA20/50 **106.5146 /106.8296**, primary ask **106.57** is **2.54 ATR** away. Velocity **2.8806**, negative retrace, no calm held rally; need net >=2.5R. | **WATCHLIST** |
| BNB / BNBUSD.p | **Z −2.40**, but bearish long prohibited; local flow negative. | BEARISH; EMA20/50 **740.3843 /741.3261**, first EMA **1.90 ATR** away. Velocity **2.1057**, no primary-sized seasoned wall; 1/10 seasoned rows is not a 5M shield. | **WATCHLIST** |
| XRP / XRPUSD.pi | **Z −2.59**, but bearish long prohibited despite positive local delta. | BEARISH HTFs; EMA20/50 **1.3659 /1.3670**, POC **1.3659** checked. No primary, velocity **1.5194**; minimum-lot spread cost **4 USD**, >=27.59% of max risk. | **NO SETUP** |
| ADA / ADAUSD.p | **Z −1.86**, not extreme; bearish dip-buy forbidden. | BEARISH; EMA50 **0.2338**, VAH **0.2360**. Quiet velocity 0.1894 does not fix **91.32 bps**, 10.50 USD minimum friction, absent shield or operator exclusion. | **NO SETUP** |
| DOGE / DOGUSD.p | **Z −0.57**, not extreme; no mean-reversion long. | BEARISH; EMA50 **0.0833**, VAH **0.0838**. Velocity 0.7318 and faster rebound do not cure **252.86 bps**, 21 USD minimum friction, absent defense and exclusion. | **NO SETUP** |
| TRX / TRXUSD.p | **Z +1.24**, not extreme; bullish short fade prohibited. | BULLISH label, mixed 4H; EMA20/50 **0.3325 /0.3313**, POC **0.3325**. Quiet 0.4919 velocity credited, but negative 5/15m, no crypto primary and **10 USD** minimum-lot friction. | **NO SETUP** |
| DOT / DOTUSD.pi | **Z −0.04**, not extreme. | BEARISH; EMA50 **1.1414**, POC **1.1492**, VAH **1.1761** explicitly considered at low Z. Velocity **4.1343**, no shield, **183.81 bps**, operator-excluded. | **NO SETUP** |
| LINK / LNKUSD.p | **Z −2.60**, but bearish long prohibited; persistent local selling. | BEARISH; EMA20/50 **12.8163 /12.8520**; first EMA **2.03 ATR** away. Velocity **2.2663**, no primary, **67.15 bps**, exclusion. | **NO SETUP** |
| BCH / BCHUSD.p | **Z −2.22**, but RANGE_BOUND excludes Engine 1 under current instruction. | RANGE_BOUND excludes Engine 2; POC **273.552**, EMA20/50 **276.8519 /276.9168** still inspected. No L3 defense; velocity **4.3549** is not a quiet trend retest. | **NO SETUP** |
| LTC / LTCUSD.pi | **Z −2.39**, but bearish long prohibited despite positive five-minute rebound. | BEARISH; EMA20/50 **61.0645 /61.2758**; first EMA **2.86 ATR** away. Velocity **2.9806**, no primary, **49.87 bps**, minimum friction **3 USD**. | **NO SETUP** |
| AVAX / AVXUSD.p | **Z −2.57**, but bearish long prohibited; all local deltas negative. | BEARISH; EMA20/50 **10.1409 /10.1876**; first EMA **2.52 ATR** away. Velocity **3.5219**, **40.12 bps >35**, no supplied stop/liq bands or primary. Contract 100/minimum lot 0.01 confirmed. | **NO SETUP** |
| NEAR / NERUSD.p | **Z −1.99**, below 2.00: do not round into eligibility; bearish long prohibited anyway. | BEARISH label, 4H mixed; EMA20/50 **5.0288 /5.0419**. Quiet velocity 0.2615 and fast positive delta credited, but negative retrace, no primary, **62.65 bps**, exclusion and minimum friction **3.10 USD**. | **NO SETUP** |
| SP500 / SP500.p | **Z −2.47**, but **RANGE_BOUND** excludes Engine 1. Peer example −2.67 is not current. | RANGE_BOUND excludes Engine 2; POC **7,801.7501**, VAL **7,773.58**, EMA20/50 **7,810.5478 /7,813.6546** inspected. +29 synthetic ticks and quiet 0.2705 velocity do not override regime. Nearby primaries are asks; threshold bid **7,631.33** is **16.05 ATR** away. | **NO SETUP** |
| NAS100 / NAS100.p | **Z −2.86**, but mean-reversion long prohibited by aligned bearish HTFs. | BEARISH HTFs; EMA20/50 **30,509.3807 /30,545.5862**. First EMA is **2.89 ATR** away, but seasoned ask **30,444.45** is a nearer **1.78 ATR** shelf; L2 ask **30,351.45** also examined. Velocity **2.5661**, no held low-velocity relief, adjacent-band SL and nearer bid barriers defeat immediate certification. | **WATCHLIST** |
| DJ30 / DJ30.p | **Z −1.94**, below threshold and RANGE_BOUND. | RANGE_BOUND; shelves **51,777.3768 /51,787.9507** and POC **51,695.468** inspected. No external depth/walls/bands/basis; +21 synthetic ticks not a trend setup. | **NO SETUP** |
| GER40 / GER40.p | **Z +0.93**, no extreme; bullish short fade prohibited. | BULLISH label, mixed 1H/bullish 4H. EMA20/50 **25,383.4386 /25,360.6625**, POC **25,366.1105**. Velocity **2.4986**, no external defense/bands/basis. Low Z is not the rejection. | **NO SETUP** |
| GOLD / XAUUSD.pi | **Z −2.32**, but bearish long prohibited; RSI23.46 alone is not absorption. | BEARISH HTFs; EMA20/50 **4,131.9718 /4,144.5754**, first EMA **3.87 ATR** away. Seller ticks −135 and quieter velocity 0.4568 credited. Only seasoned primary is a **2.038M bid at 4,072.55**, wrong side for short defense. | **WATCHLIST** |
| SILVER / XAGUSD.pi | **Z −3.16**, but bearish long prohibited despite buyer tick bias. | BEARISH; EMA20/50 **58.2774 /58.6494**, first EMA **5.01 ATR** away. Velocity **6.7784**, no seasoned commodity-sized primary, **6.35 bps >5**. | **NO SETUP** |
| USWTI / USWTI.p | **Z +1.08**, not extreme; bullish short fade prohibited. | BULLISH HTFs; EMA20/50 **95.4037 /95.0743**, seasoned bid **95.2925** at **1.03 ATR**; RSI51.69, quiet velocity0.4746 and fast +15 ticks credited. **5.02 bps** breaches stated ceiling; independently, all-band stop clearance/friction and nearby supply **95.8635** impede payable setup. | **WATCHLIST** |
| EURUSD / EURUSD.pi | **Z −1.92**, no extreme; bearish-regime long prohibited. | BEARISH label/4H, marginally mixed 1H. EMA20/50 **1.1179 /1.1191**; first EMA **5.60 ATR** away. Buyer ticks +13, no seasoned ask primary; 0.551M **bid** at **1.102195** is wrong side. Rounded quotes preclude exact cost certification. | **NO SETUP** |
| GBPUSD / GBPUSD.pi | **Z −2.49**, but RANGE_BOUND excludes Engine 1. | RANGE_BOUND excludes Engine 2; EMA20/50 **1.3249 /1.3257**, POC **1.3248** inspected. RSI12.67/quiet velocity/buyer ticks do not establish a permitted directional setup; no 0.50M primary, quote precision deficient. | **NO SETUP** |
| USDJPY / USDJPY.pi | **Z +2.78**, but mean-reversion short prohibited in bullish HTFs. | BULLISH HTFs; EMA20/50 **158.5265 /158.4243**, first EMA **4.92 ATR** away. RSI83.29, negative retrace despite low velocity0.3732: continuation extension, not a returning held shelf. Only threshold primary is distant **1.608M ask at 160.9035**, wrong side. | **NO SETUP** |

### Current flow and wall evidence

There are **988 L3 observations, 323 with recorded persist_s>=180**, and **52 L2 wall records**. The peer description of 70 BTC seasoned orders belongs to another cycle; this exact source has **BTC80 /SP50052 /NAS10047**. Counts do not prove correct-side, in-pocket, primary-sized defense. Sampled receipt recurrence is not order-ID L3 or a guarantee that liquidity remains. Hyperliquid 0x wallet attribution is not evidence of Ethereum-chain execution.

**Coverage improved:** crypto snapshot-anchored 5/15/30 windows now contain **5/15/30 completed buckets**, ending **13:26 UTC**. Do not carry Cycle 93's missing-minute defect into this generation. The 13:26–13:27 bucket is forming and is not used.

| Asset | 5m delta USD | 15m delta USD | 30m delta USD | Interpretation |
|---|---:|---:|---:|---|
| BTC | +674,599.81 | −8,392,610.20 | −5,301,872.86 | Fast rebound amid large adverse accumulated flow; not proof of absorbed downside. |
| ETH | −565,247.21 | −3,694,774.43 | −4,416,338.53 | Seller domination across all windows. |
| SOL | +113,428.53 | −1,092,298.39 | −748,465.82 | Session +4.898M/BULLISH_ABSORPTION label hides current adverse 15/30m. |
| BNB | −16,946.52 | −98,505.94 | −135,975.00 | Local seller pressure. |
| XRP | +255,739.62 | +17,045.87 | +144,744.27 | Favorable local flow cannot waive bearish long prohibition, absent defense or minimum-lot costs. |

TradFi tick CVD is signed **ticks**, not USD taker volume: SP500 +29, NAS100 −5/NEUTRAL, GOLD −135, SILVER +38, EURUSD +13. Single RSI/bias labels do not establish exhaustion, deceleration across generations or held-price absorption.

## 3. Closest hypotheses — falsifiable geometry, not automatic rejection

All illustrations below are **rejected research geometries**, not orders. Broker quotes/specs are used; source Hyperliquid bands use Hyperliquid basis. Complete top/nearest sets are checked, not just a convenient one-band buffer.

### NAS100: nearby asks do exist, but the seemingly payable card is invalid

Hyperliquid basis **−15.55** maps a **1.078043M /1,536.6s** L3 ask to **30,444.45** (1.78 ATR above mid). There is also an L2 ask source30,367→**30,351.45**, **1.291879M /187.2s**. These are credited, not discarded because Z is −2.86.

An illustrative spread-adjusted short entry at **30,443.92** below the larger L3 ask and stop beyond the governing band's upper edge gives:

`SL = ceil_tick(30,484.45 +0.50×58.5633 +0.53) = 30,514.27`.

But **30,514.27 lies inside the adjacent [30,484.45,30,584.45] buy-stop band**, which contains **1.531173M USD**. Archetypes 1/5 remain. At 0.02 lot, nominal risk would be **14.07 USD**, spread cash **0.212 USD**, friction about **1.51%**: cash sizing/cost are NOT the rejection. Fixing only the price-risk ratio does not fix the stop.

A farther >=0.5M stop magnet in **[30,084.45,30,184.45]** could make an apparent >3R card if intermediate obstacles were ignored. However a recurrent **1.667160M L2 bid at source30,344→30,328.45** is nearer. A 5bps-plus-half-spread approach target around **30,344.14** yields only about **1.42R** from that entry to the already-invalid stop. A seasoned 1.083283M L3 bid at **30,221.45** is also in the path. Velocity2.5661 and no held relief shelf add independent concerns. No safe, payable immediate short is certified.

### ETH: strongest local seller tape, but illustrative stop and friction fail

Hyperliquid basis **−1.65** maps seasoned asks to **2,474.75 /6.669926M /311.2s** and **2,490.55 /13.013995M /311.2s**. The nearer ask is a valid research location within two ATR even though the EMA20 is 2.48 ATR away.

Illustrative short entry **2,473.30** and buffered SL:

`ceil_tick(2,478.35 +0.50×11.6186 +1.45) = 2,485.61`.

**SL is inside [2,478.35,2,488.35]**, another buy-stop band. Spread/risk distance **2.9/12.31 =23.56%**, above15%, independently. A wider legitimate stop could lower that ratio but weakens reachable reward and must clear every adjacent band. The strong downside pool **[2,458.35,2,468.35]** has about **14.419M liquidation exposure** plus **1.455M stops** before contributor overlap adjustment; its front-run is much nearer than a fabricated distant >=2.2R target. Velocity3.2545 and negative retrace do not prove a calm failed rally.

### BTC and SOL: no renewed falling-knife entry

BTC primary ask **82,880.5 /15.980760M /247.5s** is a relief-short research level. Current long fade is forbidden. Nearest broker EMA20 is **2.20 ATR** above mid; 1H EMA20>EMA50 despite price below both, so do not call every HTF stack uniformly bearish. Bids at **81,871.5 /15.755262M** and **81,339.5 /20.618334M** are below market and do not validate a countertrend long. They are venue-mapped versions of the peer's source81,934/81,402, not new broker prices.

SOL's primary ask **106.57 /5.563509M /738.4s** is **2.54 ATR** away. Its positive session CVD is not current relief-rally exhaustion. Under current location/flow and net>=2.5R requirements, do not chase a breakdown or stage a distant order solely to restore activity.

### USWTI: serious low-Z long search, not a calendar veto

BULLISH HTFs, RSI51.69, velocity0.4746, primary bid **95.2925 /0.999997M /372.9s**, and EMA20 **95.4037** are constructive. The bid lies inside **[95.2905,95.3905]**, a **0.653377M** stop cluster.

A half-ATR-plus-half-spread buffer below that edge is **95.08445**, outward rounded **95.084**, which lies inside the published **[94.9905,95.0905] liquidation band**. A representative entry95.3165 would have spread/distance **0.048/0.2325 ≈20.65%**, over15%. Wider all-band clearance reduces cash friction but worsens payoff to the primary ask **95.8635 /1.000003M /372.9s**. The qualifying-size distant stop magnet **[97.6905,97.7905] /0.601525M** is about5.55 ATR above current mid, with intervening supply: not an automatically payable intraday target. Current **5.02bps** also breaches the stated5bps ceiling; no arbitrary macro reason is used.

### SP500: the peer example cannot override the current regime instruction

Current **RANGE_BOUND**, **Z−2.47**, RSI29.16. Both engines are excluded under the user's explicit regime rule. A modest positive tick reading is not exchange absorption. Nearby seasoned primaries are asks **7,781.33 /1.863917M** and **7,784.93 /2.212395M**; the threshold bid **7,631.33 /1.526M** is 16.05ATR away. Even a future change permitting range-fade Model1 would need actual local bid defense and exhaustion. No range exemption is silently introduced.

## 4. Mandate 2 — flat inventory and BTC autopsy

The exact source has **active_positions=[]**, risk tickets empty and used margin0. **No open-position ratchets or TP/SL modifications are needed. BTC #18892038 is not treated as still running.**

Balance declined from4,869.65 to4,859.55, exactly **10.10 USD**, consistent with the reported BTC stop loss. The operator reports a fill at82,213.00 after CPI. However this snapshot does **not** contain the native closing deal ID/time/reason, and retrieved `Data/initial_position_risk.json` still says **OPEN**. Therefore the flat inventory/balance are snapshot-confirmed; the exact exit execution remains operator-reported rather than independently broker-reconciled here. A stale registry must not resurrect an absent position or cause ratchet actions.

The prior, time-valid finding was SL82,213 inside Cycle93 mapped band **[82,159,82,259]**. Its adjacent **[82,259,82,359]** band invalidated simplistic tightening. Current Cycle95 basis−62.5 maps the original source band differently; do not use today's map to rewrite the historical stop decision. Preserve the original evidence bundle for the autopsy.

The **44.4M prior bids were real sampled wallet-attributed observations**, not proven fictitious orders. They were concentrated in one two-sided market-making wallet and did not establish durable directional defense or make an in-band SL safe. Calling them 'not true support' is a risk interpretation, not proof of spoofing or deliberate stop hunting. The reported loss is consistent with the predicted vulnerability, but does not establish a causal mechanism by itself.

**Lessons linked to archetypes:**

- **1 — Band containment:** validate all top/nearest opposing intervals after venue translation and tick snapping; no midpoint buffer.
- **2 — Countertrend:** extreme Z/low RSI cannot override bearish HTFs and unabsorbed adverse flow.
- **3/5 — Buffer/overshoot:** clearance belongs beyond the outer interval edge and structural shelf; expanding beyond one bin into the next is not repair.
- **4 — Concentrated/ephemeral defense:** distinguish sampled persistence from executable durability; monitor pulls/refills/re-pegs and wallet concentration.
- **Sizing:** minimum-lot constraints matter. A wider stop fitting14.50 USD is not automatically a risk-reducing repair if proportional downsizing is impossible.

Historical correction retained: 108.55 is **0.05 above**, not inside [107.5,108.5]; the inadequate buffer and wall relocation still illustrate failure. Avoid describing any finite buffer as guaranteed protection, or any tight stop as guaranteed to be hit.

## 5. Mandate 3 — pending orders

**pending_orders=[]**. No WAIT/MODIFY/DELETE tickets. No cancellation, macro purge or new pending order has been sent. Historical order references remain context only.

## 6. Capital floor, capacity and actionable summary

Full-precision stress arithmetic:

`stress_per_max_ticket =1.25×14.50+2.00 =20.125 USD`.

| Exposure | Modeled post-stop equity USD | Cushion above4795 USD |
|---|---:|---:|
| Flat | **4859.550** | **64.550** |
| One maximum-risk ticket | **4839.425** | **44.425** |
| Two | **4819.300** | **24.300** |
| Three | **4799.175** | **4.175** |
| Four | **4779.050** | **−15.950: fails operating buffer** |

Thus four free slots do not permit four maximum-risk trades. The user's maximum **three new tickets** is retained. Four lower-risk tickets could fit pure stress arithmetic, but that does not override the current explicit cap. Three maximum tickets leave only4.175 USD beyond the modeled operating reserve; capacity is not an instruction to exhaust it. Native order_calc_profit/order_calc_margin, commission, currency conversion and simultaneous-fill margin remain necessary for an eventual card. Closed profits are already in balance, not added again.

The hard floor remains a **modeled stress objective**, not unconditional capital protection. Stops and1.25×risk+2 cannot bound arbitrarily large gaps, discontinuous spreads, correlated shocks or broker failure. Flat currently means no open market-position exposure in this source, not risk-free capital under every circumstance.

| Action | Symbol | Side | Lots | Entry | SL Bunker | TP Magnet | Risk USD | R:R | Engine | Archetype Defense | Rationale |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **STAND ASIDE** | — | — | — | — | — | — | — | — | — | — | Both engines evaluated across24; no complete regime/held-shelf/defense/stop/friction/net-payoff combination. Flat and no pending orders; no modifications required. Not a macro halt. |

Stand-aside prevents new exposure to all five failure archetypes; it is not claimed to create positive expected returns by itself. No executable order card is issued, so hypothetical prices/lots in the falsification examples must not be routed to MT5.

## 7. Five-perspective adversarial tournament adaptation

Installed `.agent/skills/arena/SKILL.md` and `rubric.md` reviewed. No independent Agent/Task dispatcher or independent judge is available. The following is a **single-assistant five-perspective adaptation**, not a canonical100-agent tournament, separate model identities, or cross-tab consensus.

1. **Orderflow analyst:** BTC/SOL five-minute recovery is real; do not misreport all horizons as selling. Yet 15/30m remain deeply adverse, ETH all negative. L3 persistence323 rows is credited; primary-sized nearby NAS/ETH asks are not ignored. Low Z is not a selection prefilter.
2. **Structure specialist:** separates BEARISH labels from actual HTF stacks. BTC1H remains mixed; NAS/ETH/SOL bearish alignment stronger. SP500/BCH/GBP ranges cannot be offered as Model1 candidates under current instructions. NASnearerwall and oilnearbybid are legitimate alternatives to distant EMAs, but no held shelf is demonstrated.
3. **Stop/liq forensic:** invalidates NAS30514.27, ETH2485.61 and oil95.084 by explicit adjacent-band containment. Rejects disappearing-bin assumptions, double-counted nearest/top rows and historical-basis substitution. A float-based grossR is not certification.
4. **Portfolio governor:** acknowledges NAS0.02 hypothetical cash risk14.07 and low friction; therefore does not falsely reject on cash sizing. Three maximum tickets fit, but barely above reserve. Maintain current macros-disabled policy, with no event-based rejection. No guaranteed capital-floor language.
5. **Red team:** attacks the peer's SP500 example and stale BTCregistry. Concedes actual flat inventory and corrects outdatedZ/persistence values. Accepts reported loss as operator provenance, not fabricated native deal proof. No revenge re-entry or undeclared stop widening. Demands an observed held pullback plus a valid stop before any candidate label.

Rubric weights: correctness30%, completeness25%, specificity15%, robustness20%, clarity10%; each criterion0–10. Scores grade hypotheses, not probability of profitable trades; verified fatal flaws override totals.

| Hypothesis | Correct | Complete | Specific | Robust | Clear | Weighted/100 | Decisive attack |
|---|---:|---:|---:|---:|---:|---:|---|
| H1 Buy BTC/ETH extreme oversold | 2 | 5 | 8 | 1 | 8 | **40.5** | Fatal: forbidden bearish mean-reversion longs; no exhaustion proof. |
| H2 Buy SP500 Model1 at−2.47Z | 3 | 6 | 8 | 1 | 8 | **46.0** | Fatal: RANGE_BOUND excluded; nearest primary bids not local. |
| H3 Stage NAS relief short immediately | 6 | 7 | 9 | 3 | 8 | **63.0** | Fatal: proposed stop inside next band; nearer bid/barrier payoff. |
| H4 Stage ETH nearby ask short immediately | 5 | 7 | 9 | 2 | 8 | **58.0** | Fatal: contained stop, friction23.56%, unquiet extension. |
| H5 Stage USWTI low-Z long now | 5 | 7 | 8 | 2 | 8 | **56.5** | Fatal: contained stop and costs/payoff; spread ceiling independently fails. |
| H6 Short USDJPY extreme overbought | 2 | 5 | 8 | 1 | 8 | **40.5** | Fatal: bullish HTF countertrend fade prohibited. |
| H7 Fill all4 slots at14.50 risk | 2 | 6 | 9 | 1 | 8 | **44.5** | Fatal: violates4795 stress invariant and explicit3-ticket cap. |
| H8 Stay flat; preserve explicit research watches | 9 | 8 | 8 | 9 | 9 | **86.0** | No trade-certified falsely; live broker/independent-agent limitations explicit. |

Adapted bracket: H1/H2→H2; H3/H4→H3; H5/H6→H5; H7/H8→H8. Semifinals H2/H3→H3, H5/H8→H8. Final H3/H8→**H8**. Passing a bracket round is never trade approval. Full native execution, independent judges and literal full-history semantic reading remain limitations.

## 8. Institutional telemetry and profitability audit

### Actual current improvements and defects

All24assetblocks/all values traversed; finite-number, chronological OHLC/cutoff and delta-conservation checks applied. Current crypto minute windows are complete; do not repeat the previous missing-minute claim. The machine evidence preserves complete book/wall/band fields and summarized candles with methods, not a copied user matrix.

- **Inventory/ledger reconciliation:** live source flat, registry still OPEN. Add broker position ID, opening/closing deal IDs, reason, deal time, realized profit/commission/swap, initial-risk immutable ID and reconciliation status. Mark a position closed only from matching broker evidence; never overwrite frozenR0 as part of closure. Flat telemetry controls current actions while unreconciled history is flagged.
- **Quote precision:** five-digit EUR/GBP quotes still rounded to four decimals with serialized spread0 despite nonzero bps. Store integer price ticks/decimal strings, native bid/ask, quote currency and exact tick values. Test ask−bid, midpoint and bps consistency. Zero rounded spread must not imply free execution.
- **Temporal evidence:** per-source event, receipt, available-at, generation and clock-domain timestamps; sequence gaps, cache hashes, restart IDs, maximum observation gaps and wall re-peg confidence. Repeated cache payloads must not count as independent observations. Raw wallet/side/price snapshots are not full order-IDL3.
- **Wallet concentration:** compute share_i=verified defending notional_i/total and **HHI=sum(share_i²)**; also effective sponsors=1/HHI, same-wallet two-sided quote ratio, net directional quote exposure, withdrawal hazard and refill half-life. This is a reliability feature, not a new arbitrary wallet-count veto. A single large MM can provide liquidity, but not independent diversification.
- **Event-time multi-level OFI:** levelk increment `e_k=1[b_t>=b_prev]q_b,t−1[b_t<=b_prev]q_b,prev−1[a_t<=a_prev]q_a,t+1[a_t>=a_prev]q_a,prev`; sum causal events with distance/depth weights, normalize by observed depth, report1/5/15/30m and coverage. Static book imbalance and signed MT5ticks are not substitutes for size-based OFI.
- **Microprice/drift:** `mu=(ask*q_bid+bid*q_ask)/(q_bid+q_ask)`; report(mu−mid)/tick, drift, impact/depletion curves and recovery times with venue tags. External microprice is not an executable OTC price.
- **Queue decay:** external queue-depth proxy, cancel/depletion intensity, replenishment and conditional fill probability. True MT5exchange queue position is unavailable; never manufacture a queue rank or guarantee a fill because an external level traded.
- **CVD features:** explicit window start/end/coverage; taker buy ratio=sum(buy)/sum(buy+sell), normalized signed delta, slopes/acceleration, price-response elasticity and regime conditioning. Separate USDexchange flow from signed-tick units. CVDsign alone neither proves institutional identity nor absorption.
- **Footprint proof:** the scalar trapped label is not `footprint_trapped_traders` price-bin evidence. Add aggressive buy/sell/delta, swept-level ID, volume-at-price, reclaim/hold time and refill. Research long absorption score `z(sell_volume)−z(max(0,−return)/ATR)+z(bid_refill)` conditional on a held level; reverse signs/sides for short. Fit normalizers using past data only.
- **Band semantics:** supply raw levels/contributor IDs and distinguish coarse DISPLAY_BIN from estimated executable sweep interval. Tick-aligned multiscale bin widths, e.g. `max(tick,min(0.1ATR,1bp*mid))` as a research starting point, reduce coarse-bin ambiguity. Neighboring broad bins often tile the price axis; do not secretly waive the current any-band exclusion. Approve a documented schema/policy revision after validation instead. De-duplicate top/nearest and overlapping stop/liq contributors.
- **HTF/shelf trajectory:** publish timeframe-specific warmed EMA20/50/200 and seed/counts, RSI path, shelf touch/retest/hold timestamps, impulse/retrace definitions and quality flags. Negative retrace plus high velocity often represents ongoing extension, not a completed pullback. MT5 VWAP/profile volumes are broker tick proxies, not exchange institutional contracts.
- **Venue basis risk:** rolling source-specific median/MAD/quantiles, synchronized sampling, sample count and latency error. Use Hyperliquid basis for Hyperliquid walls and Binance basis for BinanceL2; missing basis means mapping unavailable. Map intervals, not just midpoints, and outward snap stops.
- **Global block discipline:** FNG62/Greed observed; October14 ETF flows now **NOT_YET_REPORTED/null**, not yesterday's+175.7M/+24.8M reused. Coinbase premium unavailable. Historical multi-alert liquidations **97.643484M**, long/short ratio1.35; zero activeTWAP/hazard arrays mean none observed, not no hazard. Crypto funding and eight-observation histories are retained; missing predicted funding is not extrapolated as fact.
- **Probability/calibration:** root p_win_lower_bound0.4197 on17trades remains uncalibrated. Publish engine×asset×session fill-conditional outcomes, uncertainty, time-to-target and regime drift; do not claim an institutional edge or guaranteed>=2Rpayoff from a small mixed sample.

These are proposed engineering improvements, **not production fixes deployed in this turn**. The external AI-service error is unrelated and is not claimed repaired.

### Payable2–2.5R construction

Use broker-valued executable-side gross risk L and reward G plus additional costs not already embedded in bid/ask:

`R_net=(G−c_win)/(L+c_loss)`.

Do not subtract spread twice. In mid-price research coordinates, require target_distance>=Rrequired*stop_distance+win_cost_price+Rrequired*loss_cost_price. A genuine1.2ATRstop needs at least2.4–3.0ATRgross room plus costs for2–2.5R. New entries need a measured deep sweep/retest and reachable first meaningful magnet, not a tight in-band stop or a remote target chosen to make the ratio pass. ETH>=2.2R/SOL>=2.5R remain current requirements.

Discrete lot enumeration: q=min_lot+n*step_lot; native loss valuation must land in7.50–14.50, after which full portfolio stress/margin is assessed. If no q exists, no card. For linear products, spread_cost/actual_nominal_risk≈spread_distance/stop_distance, so **downsizing alone does not lower the friction ratio**. Using14.50 as denominator instead of actual risk can understate cost. Minimum-lot spread/14.50 is only a lower-bound rejection test.

Choose shelf/band buffers using causal conditional adverse-sweep/MAE quantiles by asset, volatility, spread, depth and basis uncertainty while preserving current floors: Model2shelf>=0.50ATR, generalband>=0.35ATR, stronger when observed tails warrant. Recheck all known bands after outward tick snapping; incorporate residual uncertainty without double-counting excursions already captured by empiricalMAE. Widening may require fewer lots or no ticket, not unconditional safety language.

Current TP5–10bps front-running stays in force. Research adaptive offsets from spread/latency/queue-depletion quantiles with explicit policy revision and held-out tests; do not silently loosen the rule. A large fixed bps offset can consume an intraday FX target. Distinguish forced buy/sell-stop magnets from passive opposing walls; neither guarantees subsequent travel or fills.

### More opportunities without macro halts

Evaluate continuously across events; no calendar pause/purge is applied. Prioritize **NAS100/ETH relief shorts**, then **BTC** after a real held rally and stronger HTF agreement, **SOL/BNB/GOLD** when price returns to a defended shelf, and **USWTI** if actual cost and geometry resolve. SP500/BCH/GBP need a permitted directional regime first; do not force range fades. DJ30/GER40 need defensible external structure, not invented walls. High-friction exclusions remain.

Rank *qualified* cards by `EV_attempt=P(fill)*[p*net_gain−(1−p)*net_loss]−nonfill_cost`, divided by margin-time, with adverse selection conditional on fill and correlated exposure penalties. Maintain actual friction/geometry through news using continuously measured spread/depth/basis rather than a timed macro prohibition. More signals is not necessarily more net alpha.

Validate with causal walk-forward/replay, completed-bar joins, realistic broker passive fills, partial fills, gap SL fills, fees and swaps. Measure netEV, fill rate, stop-before-target, MAE/MFE, drawdown and holding time versus current policy and matched-risk benchmarks. Correct multiple testing across24assets×2engines. Report out-of-sample confidence rather than claimed profitability improvements without tests.

## 9. Publication and verification boundaries

The full report is intended for local storage and desk append, with push only to the fixed session branch. Existing local Cycle93 reports and prior desk contents are preserved. Telemetry, execution code, live orders, playbook and risk registry are not modified by this analysis. No independent-agent or peer-consensus claim is made.

Verification receipts below cover exact source/hash, every asset/block, numerical/candle/CVD integrity, wall counts, separate engine classifications, stress arithmetic, rubric weights and hypothetical stop containment. No backtest or broker order_calc_profit/order_calc_margin execution is claimed. Fresh broker receipts are required before any later actual trade; these rejected examples are not standing instructions.

## Appendix A — per-asset telemetry receipts

These diagnostics supplement both-engine verdicts. Full top/nearest bands, wall records, depth ladders, flow/specs and field inventories are retained in the evidence JSON. HTF triplets are last completed close / finite-history EMA20 / EMA50; no warmed HTFEMA200 assertion. All candles, funding history and other blocks were traversed.

### BTC / BTCUSD.pi

- Quote bid/ask/mid 82476/82491/82483.5, spread 1.82bps, reported age 0.93320394s; min-lot spread cash diagnostic 0.15 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 82644/83274.81375674/83217.40183094; htf_4h_ohlcv: 82644/83135.3527772/83343.12551182.
- Session VWAP/sigma/ATR 83365.586/266.5201/326.299; 15m EMA200 83234.5603; POC/VAH/VAL 83396.795/83486.62/83091.39; pullback {"direction":"SHORT","retrace":-0.1359,"depth_sigma":0.0,"velocity_ratio":1.2368,"bars_pullback":2,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 83147.805/83818.86/82412.84; prior week 83348.7/83625.9/82358.7; weekly VWAP 83110.3496; trap label BALANCED.
- Flow {"session_cvd_usd":-83921651.08,"weekly_cvd_usd":-49124696.07,"cvd_24h_usd":-115072606.3,"bar_delta_15m_usd":-7326375.51,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-83921651.08,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 674599.81, 5 buckets; 15m: -8392610.2, 15 buckets; 30m: -5301872.86, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 125658.74/858833.01USD, imbalance -0.7447; L3 total/duration>=180 319/80; recurrent primary receipts SELL 83597.5 /21182896.05USD /730.3s; BUY 81339.5 /20618333.74USD /730.3s; SELL 82880.5 /15980759.69USD /247.5s; BUY 81871.5 /15755261.74USD /730.3s.
- Source-specific basis {"BINANCE":{"mid":82583.485,"mid_ts":1791984393.509,"basis_median":-90.915},"HYPERLIQUID":{"mid":82548.5,"mid_ts":1791984393.509,"basis_median":-62.5}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [82337.5,82437.5] /1107013.36USD; nearest_buy_stop_clusters_above: [82437.5,82537.5] /6228133.26USD; nearest_long_cascade_bands_below: [82337.5,82437.5] /1651073.19USD; nearest_short_squeeze_bands_above: [82437.5,82537.5] /574673.77USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":1.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":0.01,"digits":2}; funding {"last_funding_rate_bps":0.66,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":82548.74,"index_price":82582.04}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### ETH / ETHUSD.pi

- Quote bid/ask/mid 2464.2/2467.1/2465.65, spread 11.76bps, reported age 1.35507035s; min-lot spread cash diagnostic 0.029 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 2472.4/2500.29796718/2504.87046284; htf_4h_ohlcv: 2472.4/2506.66876128/2539.95162356.
- Session VWAP/sigma/ATR 2500.3456/11.0831/11.6186; 15m EMA200 2505.6864; POC/VAH/VAL 2502.455/2513.794/2497.786; pullback {"direction":"SHORT","retrace":-0.1691,"depth_sigma":0.0003,"velocity_ratio":3.2545,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 2525.419/2537.758/2485.66; prior week 2502.595/2547.82/2464.606; weekly VWAP 2506.6795; trap label BALANCED.
- Flow {"session_cvd_usd":-731504.32,"weekly_cvd_usd":-24133601.2,"cvd_24h_usd":-10463764.93,"bar_delta_15m_usd":-1818196.45,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-731504.32,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: -565247.21, 5 buckets; 15m: -3694774.43, 15 buckets; 30m: -4416338.53, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 74904.6/164241.66USD, imbalance -0.3736; L3 total/duration>=180 171/30; recurrent primary receipts SELL 2490.55 /13013995.25USD /311.2s; BUY 2422.95 /12660995.46USD /311.2s; SELL 2474.75 /6669925.61USD /311.2s; BUY 2438.85 /6573232.69USD /311.2s.
- Source-specific basis {"BINANCE":{"mid":2468.695,"mid_ts":1791984394.272,"basis_median":-3.145},"HYPERLIQUID":{"mid":2467.35,"mid_ts":1791984394.272,"basis_median":-1.65}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [2458.35,2468.35] /1455029.36USD; nearest_buy_stop_clusters_above: [2468.35,2478.35] /296411.88USD; nearest_long_cascade_bands_below: [2458.35,2468.35] /14418701.9USD; nearest_short_squeeze_bands_above: [2468.35,2478.35] /43341.72USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":1.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":0.01,"digits":2}; funding {"last_funding_rate_bps":0.07,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":2467.6,"index_price":2468.77}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### SOL / SOLUSD.p

- Quote bid/ask/mid 104.87/105.11/104.99, spread 22.86bps, reported age 1.45079994s; min-lot spread cash diagnostic 0.24 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 105.24/106.87113891/107.49629528; htf_4h_ohlcv: 105.24/108.02285281/110.85584911.
- Session VWAP/sigma/ATR 106.8613/0.6962/0.6223; 15m EMA200 107.567; POC/VAH/VAL 107.1727/107.668/106.6774; pullback {"direction":"SHORT","retrace":-0.1489,"depth_sigma":0.0075,"velocity_ratio":2.8806,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 106.1765/108.62/105.724; prior week 107.2741/111.8938/105.8404; weekly VWAP 107.4945; trap label BALANCED.
- Flow {"session_cvd_usd":4897924.53,"weekly_cvd_usd":22187434.44,"cvd_24h_usd":12245680.03,"bar_delta_15m_usd":-277475.16,"divergence":"BULLISH_ABSORPTION","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":4897924.53,"flow_bias":"BULLISH_ABSORPTION"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 113428.53, 5 buckets; 15m: -1092298.39, 15 buckets; 30m: -748465.82, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 748048.09/1053255.88USD, imbalance -0.1694; L3 total/duration>=180 74/21; recurrent primary receipts SELL 106.57 /5563508.95USD /738.4s; BUY 103.1 /5390948.34USD /560.0s.
- Source-specific basis {"BINANCE":{"mid":105.105,"mid_ts":1791984394.46,"basis_median":-0.14},"HYPERLIQUID":{"mid":105.015,"mid_ts":1791984394.46,"basis_median":-0.04}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [103.96,104.96] /10372673.9USD; nearest_buy_stop_clusters_above: [104.96,105.96] /1686427.48USD; nearest_long_cascade_bands_below: [103.96,104.96] /1068710.35USD; nearest_short_squeeze_bands_above: [104.96,105.96] /103460.78USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":100.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding {"last_funding_rate_bps":0.25,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":105.054,"index_price":105.114}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### BNB / BNBUSD.p

- Quote bid/ask/mid 736.2/736.7/736.45, spread 6.79bps, reported age 1.42386699s; min-lot spread cash diagnostic 0.005 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 736/741.34362077/742.70027023; htf_4h_ohlcv: 736/743.70619342/750.96157595.
- Session VWAP/sigma/ATR 741.7036/2.1917/2.0715; 15m EMA200 742.7903; POC/VAH/VAL 743.791/744.79/740.572; pullback {"direction":"SHORT","retrace":-0.11,"depth_sigma":0.0007,"velocity_ratio":2.1057,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 743.959/747.508/737.68; prior week 741.599/758.796/731.518; weekly VWAP 741.9536; trap label BALANCED.
- Flow {"session_cvd_usd":-420769.73,"weekly_cvd_usd":-8895495.49,"cvd_24h_usd":-1893660.51,"bar_delta_15m_usd":-110921.65,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-420769.73,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: -16946.52, 5 buckets; 15m: -98505.94, 15 buckets; 30m: -135975, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 90773.09/54099.11USD, imbalance 0.2531; L3 total/duration>=180 10/1; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":737.265,"mid_ts":1791984394.527,"basis_median":-0.815},"HYPERLIQUID":{"mid":736.755,"mid_ts":1791984394.527,"basis_median":-0.35}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [735.65,736.65] /2132.91USD; nearest_buy_stop_clusters_above: [736.65,737.65] /1306.27USD; nearest_long_cascade_bands_below: [735.65,736.65] /2638.32USD; nearest_short_squeeze_bands_above: [737.65,738.65] /2537.38USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":1.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":20,"point":0.01,"digits":2}; funding {"last_funding_rate_bps":0.02,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":736.87,"index_price":737.21}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### XRP / XRPUSD.pi

- Quote bid/ask/mid 1.351/1.355/1.353, spread 29.56bps, reported age 3.63833928s; min-lot spread cash diagnostic 4 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 1.355/1.36647316/1.37045226; htf_4h_ohlcv: 1.355/1.37520678/1.40225409.
- Session VWAP/sigma/ATR 1.3672/0.0055/0.0071; 15m EMA200 1.3709; POC/VAH/VAL 1.3659/1.3718/1.3634; pullback {"direction":"SHORT","retrace":-0.1667,"depth_sigma":0.3672,"velocity_ratio":1.5194,"bars_pullback":2,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 1.3571/1.3682/1.3308; prior week 1.4028/1.4243/1.3642; weekly VWAP 1.3693; trap label BALANCED.
- Flow {"session_cvd_usd":14299497.91,"weekly_cvd_usd":41128166.39,"cvd_24h_usd":33327184.94,"bar_delta_15m_usd":-203951.95,"divergence":"BULLISH_ABSORPTION","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":14299497.91,"flow_bias":"BULLISH_ABSORPTION"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 255739.62, 5 buckets; 15m: 17045.87, 15 buckets; 30m: 144744.27, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 420142.85/424994.84USD, imbalance -0.0057; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":1.3542,"mid_ts":1791984394.567,"basis_median":-0.00165},"HYPERLIQUID":{"mid":1.3533,"mid_ts":1791984394.567,"basis_median":-0.00105}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [1.33895,1.34895] /60476.74USD; nearest_buy_stop_clusters_above: [1.34895,1.35895] /25587.25USD; nearest_long_cascade_bands_below: [1.33895,1.34895] /284531.64USD; nearest_short_squeeze_bands_above: [1.34895,1.35895] /328390.47USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":1000.0,"min_lot":1.0,"step_lot":1.0,"max_lot":100.0,"stops_level":20,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":0.84,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":1.3539,"index_price":1.3543}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### ADA / ADAUSD.p

- Quote bid/ask/mid 0.2289/0.231/0.2299, spread 91.32bps, reported age 3.91793036s; min-lot spread cash diagnostic 10.5 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 0.2287/0.23411952/0.23705048; htf_4h_ohlcv: 0.2287/0.23865457/0.24377148.
- Session VWAP/sigma/ATR 0.2341/0.0022/0.0017; 15m EMA200 0.237; POC/VAH/VAL 0.2342/0.236/0.2329; pullback {"direction":"SHORT","retrace":0.0206,"depth_sigma":0.3681,"velocity_ratio":0.1894,"bars_pullback":2,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 0.2407/0.2429/0.2317; prior week 0.252/0.2574/0.2346; weekly VWAP 0.2381; trap label BALANCED.
- Flow {"session_cvd_usd":318177.97,"weekly_cvd_usd":-2041635.7,"cvd_24h_usd":931971.97,"bar_delta_15m_usd":-62009.04,"divergence":"BULLISH_ABSORPTION","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":318177.97,"flow_bias":"BULLISH_ABSORPTION"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 36436.31, 5 buckets; 15m: -88603.3, 15 buckets; 30m: -151985.68, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 515322.18/461426.97USD, imbalance 0.0552; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":0.2301,"mid_ts":1791984394.599,"basis_median":-0.00025},"HYPERLIQUID":{"mid":0.23,"mid_ts":1791984394.599,"basis_median":-5.5e-05}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [0.228945,0.229945] /296.52USD; nearest_buy_stop_clusters_above: [0.229945,0.230945] /2932.49USD; nearest_long_cascade_bands_below: [0.228945,0.229945] /2923.05USD; nearest_short_squeeze_bands_above: [0.229945,0.230945] /4392.52USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.0001,"contract_size":5000.0,"min_lot":1.0,"step_lot":1.0,"max_lot":1000.0,"stops_level":20,"point":0.0001,"digits":4}; funding {"last_funding_rate_bps":0.34,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.2301,"index_price":0.2302}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### DOGE / DOGUSD.p

- Quote bid/ask/mid 0.082/0.0841/0.083, spread 252.86bps, reported age 30.88022065s; min-lot spread cash diagnostic 21 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 0.0821/0.08327648/0.08355719; htf_4h_ohlcv: 0.0821/0.08383211/0.08575283.
- Session VWAP/sigma/ATR 0.0833/0.0005/0.0004; 15m EMA200 0.0836; POC/VAH/VAL 0.0834/0.0838/0.0831; pullback {"direction":"SHORT","retrace":-0.08,"depth_sigma":3.8914,"velocity_ratio":0.7318,"bars_pullback":2,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 0.0837/0.0842/0.0819; prior week 0.0835/0.0863/0.0824; weekly VWAP 0.0835; trap label BALANCED.
- Flow {"session_cvd_usd":-3095370.03,"weekly_cvd_usd":-15154106.09,"cvd_24h_usd":-4847399.72,"bar_delta_15m_usd":-307520.47,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-3095370.03,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 52357.61, 5 buckets; 15m: -677718.81, 15 buckets; 30m: -841718.9, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 459506.48/295805.29USD, imbalance 0.2167; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":0.0832,"mid_ts":1791984394.631,"basis_median":-8.5e-05},"HYPERLIQUID":{"mid":0.0831,"mid_ts":1791984394.631,"basis_median":-5.35e-05}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [0.0829465,0.0830465] /3324.26USD; nearest_buy_stop_clusters_above: [0.0830465,0.0831465] /221.81USD; nearest_long_cascade_bands_below: [0.0829465,0.0830465] /118.34USD; nearest_short_squeeze_bands_above: [0.0830465,0.0831465] /2962.66USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.0001,"contract_size":10000.0,"min_lot":1.0,"step_lot":1.0,"max_lot":50.0,"stops_level":20,"point":0.0001,"digits":4}; funding {"last_funding_rate_bps":0.45,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.0831,"index_price":0.0832}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### TRX / TRXUSD.p

- Quote bid/ask/mid 0.3329/0.3339/0.3334, spread 29.99bps, reported age 32.73433256s; min-lot spread cash diagnostic 10 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 0.3324/0.3305857/0.3297824; htf_4h_ohlcv: 0.3324/0.32986813/0.33105837.
- Session VWAP/sigma/ATR 0.3312/0.0018/0.0005; 15m EMA200 0.3298; POC/VAH/VAL 0.3325/0.3335/0.3274; pullback {"direction":"LONG","retrace":0.4483,"depth_sigma":2.2568,"velocity_ratio":0.4919,"bars_pullback":10,"bars_impulse":11,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 0.3289/0.3297/0.3279; prior week 0.3302/0.3327/0.3286; weekly VWAP 0.3297; trap label BALANCED.
- Flow {"session_cvd_usd":10988918.45,"weekly_cvd_usd":600629.7,"cvd_24h_usd":8366539.76,"bar_delta_15m_usd":18386.55,"divergence":"BULLISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":10988918.45,"flow_bias":"BULLISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: -2553.56, 5 buckets; 15m: -6698.31, 15 buckets; 30m: 14262.94, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 1843824.45/1324848.91USD, imbalance 0.1638; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":0.3335,"mid_ts":1791984394.665,"basis_median":-0.00015},"HYPERLIQUID":{"mid":0.3335,"mid_ts":1791984394.665,"basis_median":-0.000145}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [0.332855,0.333855] /660.34USD; nearest_buy_stop_clusters_above: [0.333855,0.334855] /9817.39USD; nearest_long_cascade_bands_below: [0.324855,0.325855] /201.44USD; nearest_short_squeeze_bands_above: [0.336855,0.337855] /136.4USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.0001,"contract_size":10000.0,"min_lot":1.0,"step_lot":1.0,"max_lot":50.0,"stops_level":20,"point":0.0001,"digits":4}; funding {"last_funding_rate_bps":0.42,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":0.3333,"index_price":0.3335}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### DOT / DOTUSD.pi

- Quote bid/ask/mid 1.132/1.153/1.1425, spread 183.81bps, reported age 6.81011438s; min-lot spread cash diagnostic 0.21 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 1.134/1.14684607/1.16905516; htf_4h_ohlcv: 1.134/1.17683959/1.18290941.
- Session VWAP/sigma/ATR 1.143/0.0117/0.0097; 15m EMA200 1.1683; POC/VAH/VAL 1.1492/1.1761/1.1344; pullback {"direction":"SHORT","retrace":0.4545,"depth_sigma":1.3029,"velocity_ratio":4.1343,"bars_pullback":2,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 1.1616/1.206/1.105; prior week 1.0931/1.2327/1.0731; weekly VWAP 1.1877; trap label BALANCED.
- Flow {"session_cvd_usd":89643.43,"weekly_cvd_usd":-1015301.1,"cvd_24h_usd":-38625.77,"bar_delta_15m_usd":-18492.69,"divergence":"BULLISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":89643.43,"flow_bias":"BULLISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 519.8, 5 buckets; 15m: -41302.67, 15 buckets; 30m: -35620.92, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 294145.6/172146.22USD, imbalance 0.2616; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":1.1435,"mid_ts":1791984394.696,"basis_median":-0.001},"HYPERLIQUID":{"mid":1.1418,"mid_ts":1791984394.696,"basis_median":-0.00035}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [1.12965,1.13965] /1440.2USD; nearest_buy_stop_clusters_above: [1.13965,1.14965] /443.23USD; nearest_long_cascade_bands_below: [1.12965,1.13965] /326.88USD; nearest_short_squeeze_bands_above: [1.13965,1.14965] /426.44USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":1000.0,"min_lot":0.01,"step_lot":0.01,"max_lot":40.0,"stops_level":0,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":1.0,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":1.1426,"index_price":1.144}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### LINK / LNKUSD.p

- Quote bid/ask/mid 12.615/12.7/12.6575, spread 67.15bps, reported age 0.93936062s; min-lot spread cash diagnostic 0.85 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 12.65/12.85498212/12.90515655; htf_4h_ohlcv: 12.65/12.92247854/13.15580511.
- Session VWAP/sigma/ATR 12.8651/0.0799/0.0784; 15m EMA200 12.9058; POC/VAH/VAL 12.9041/12.9355/12.828; pullback {"direction":"SHORT","retrace":-0.1172,"depth_sigma":0.0475,"velocity_ratio":2.2663,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 12.8779/13.0953/12.7551; prior week 12.8577/13.244/12.5858; weekly VWAP 12.9303; trap label BALANCED.
- Flow {"session_cvd_usd":-991578.27,"weekly_cvd_usd":-2321091.42,"cvd_24h_usd":-1032425.13,"bar_delta_15m_usd":-112435.35,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-991578.27,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: -54767.82, 5 buckets; 15m: -74304.58, 15 buckets; 30m: -231911.78, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 56630.86/108132.11USD, imbalance -0.3126; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":12.6645,"mid_ts":1791984394.726,"basis_median":-0.013},"HYPERLIQUID":{"mid":12.6525,"mid_ts":1791984394.726,"basis_median":-0.005}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [12.595,12.695] /8064.7USD; nearest_buy_stop_clusters_above: [12.695,12.795] /10520.55USD; nearest_long_cascade_bands_below: [12.595,12.695] /13566.01USD; nearest_short_squeeze_bands_above: [12.695,12.795] /1363.94USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":100.0,"min_lot":0.1,"step_lot":0.1,"max_lot":100.0,"stops_level":10,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":0.7,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":12.657,"index_price":12.665}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### BCH / BCHUSD.p

- Quote bid/ask/mid 272.86/273.44/273.15, spread 21.23bps, reported age 1.03109956s; min-lot spread cash diagnostic 0.58 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 273.16/276.02656939/275.56253332; htf_4h_ohlcv: 273.16/276.53156289/284.27963676.
- Session VWAP/sigma/ATR 277.5935/2.0002/1.7589; 15m EMA200 275.7625; POC/VAH/VAL 273.552/277.644/269.46; pullback {"direction":"SHORT","retrace":-0.2247,"depth_sigma":0.0042,"velocity_ratio":4.3549,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 273.6954/276.9984/268.1904; prior week 278.6044/284.652/270.696; weekly VWAP 275.1123; trap label BALANCED.
- Flow {"session_cvd_usd":708642.05,"weekly_cvd_usd":-151935.63,"cvd_24h_usd":911173.57,"bar_delta_15m_usd":-53874.06,"divergence":"BULLISH_ABSORPTION","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":708642.05,"flow_bias":"BULLISH_ABSORPTION"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 12169.46, 5 buckets; 15m: -65634.27, 15 buckets; 30m: -64497.33, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 267996.4/184480.4USD, imbalance 0.1846; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":273.35,"mid_ts":1791984394.755,"basis_median":-0.3},"HYPERLIQUID":{"mid":273.205,"mid_ts":1791984394.755,"basis_median":-0.055}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [271.945,272.945] /4098.08USD; nearest_buy_stop_clusters_above: [272.945,273.945] /71906.19USD; nearest_long_cascade_bands_below: [271.945,272.945] /253.81USD; nearest_short_squeeze_bands_above: [273.945,274.945] /261.18USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":10.0,"min_lot":0.1,"step_lot":0.1,"max_lot":100.0,"stops_level":0,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":1.0,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":273.17,"index_price":273.35}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### LTC / LTCUSD.pi

- Quote bid/ask/mid 60.01/60.31/60.16, spread 49.87bps, reported age 2.30207992s; min-lot spread cash diagnostic 3 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 60.17/61.29978506/61.7964654; htf_4h_ohlcv: 60.17/62.20010942/63.92817094.
- Session VWAP/sigma/ATR 61.2946/0.4746/0.316; 15m EMA200 61.8316; POC/VAH/VAL 60.9017/61.6021/60.8776; pullback {"direction":"SHORT","retrace":-0.154,"depth_sigma":0.0156,"velocity_ratio":2.9806,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 60.6307/62.2246/59.23; prior week 63.9148/64.9132/61.2268; weekly VWAP 62.0473; trap label BALANCED.
- Flow {"session_cvd_usd":-948837.3,"weekly_cvd_usd":-2611571.35,"cvd_24h_usd":-1168758.99,"bar_delta_15m_usd":-190540.12,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-948837.3,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 15079.04, 5 buckets; 15m: -148437.77, 15 buckets; 30m: -225477.28, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 135624.45/190606.41USD, imbalance -0.1685; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":60.215,"mid_ts":1791984394.784,"basis_median":-0.07},"HYPERLIQUID":{"mid":60.1765,"mid_ts":1791984394.784,"basis_median":-0.022}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [60.078,60.178] /5832.91USD; nearest_buy_stop_clusters_above: [60.178,60.278] /2928.79USD; nearest_long_cascade_bands_below: [60.078,60.178] /1824.55USD; nearest_short_squeeze_bands_above: [60.178,60.278] /133.59USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":100.0,"min_lot":0.1,"step_lot":0.1,"max_lot":100.0,"stops_level":0,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":0.47,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":60.18,"index_price":60.21}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### AVAX / AVXUSD.p

- Quote bid/ask/mid 9.95/9.99/9.97, spread 40.12bps, reported age 6.24541259s; min-lot spread cash diagnostic 0.04 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 9.99/10.20752526/10.31968851; htf_4h_ohlcv: 9.99/10.36988428/10.53775304.
- Session VWAP/sigma/ATR 10.1997/0.0896/0.0679; 15m EMA200 10.3262; POC/VAH/VAL 10.2608/10.2944/10.16; pullback {"direction":"SHORT","retrace":-0.1818,"depth_sigma":0.0889,"velocity_ratio":3.5219,"bars_pullback":1,"bars_impulse":19,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 10.2168/10.564/10.0936; prior week 10.2156/10.8552/9.9368; weekly VWAP 10.4265; trap label BALANCED.
- Flow {"session_cvd_usd":-1246797.28,"weekly_cvd_usd":-1317855.5,"cvd_24h_usd":-552042.17,"bar_delta_15m_usd":-249976.96,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-1246797.28,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: -15238.78, 5 buckets; 15m: -238450.45, 15 buckets; 30m: -448139.59, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 125257.76/92479.62USD, imbalance 0.1505; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":9.9775,"mid_ts":1791984394.815,"basis_median":-0.0115},"HYPERLIQUID":{"mid":9.9664,"mid_ts":1791984394.815,"basis_median":-0.00315}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: none observed; nearest_buy_stop_clusters_above: none observed; nearest_long_cascade_bands_below: none observed; nearest_short_squeeze_bands_above: none observed. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":100.0,"min_lot":0.01,"step_lot":0.01,"max_lot":40.0,"stops_level":20,"point":0.01,"digits":2}; funding {"last_funding_rate_bps":0.08,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":9.969,"index_price":9.977}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### NEAR / NERUSD.p

- Quote bid/ask/mid 4.933/4.964/4.9485, spread 62.65bps, reported age 1.06001472s; min-lot spread cash diagnostic 3.1 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 4.957/5.04941277/5.15875432; htf_4h_ohlcv: 4.957/5.18509631/5.16264707.
- Session VWAP/sigma/ATR 5.0549/0.0535/0.0584; 15m EMA200 5.1602; POC/VAH/VAL 5.0554/5.0823/4.9746; pullback {"direction":"SHORT","retrace":-0.2548,"depth_sigma":0.1845,"velocity_ratio":0.2615,"bars_pullback":1,"bars_impulse":1,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 5.0626/5.4316/4.874; prior week 5.0524/5.7499/4.8994; weekly VWAP 5.2916; trap label BALANCED.
- Flow {"session_cvd_usd":-2714135.17,"weekly_cvd_usd":-2434919.54,"cvd_24h_usd":10378716.57,"bar_delta_15m_usd":-1289608.19,"divergence":"BEARISH_MOMENTUM","bars_count":191}; TradFi {"status":"CRYPTO_USES_BINANCE_TAKER_CVD","session_tick_cvd":-2714135.17,"flow_bias":"BEARISH_MOMENTUM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: 158392.71, 5 buckets; 15m: -157237.65, 15 buckets; 30m: -1021585.92, 30 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 251857.14/335428.31USD, imbalance -0.1423; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis {"BINANCE":{"mid":4.9425,"mid_ts":1791984394.843,"basis_median":-0.0025},"HYPERLIQUID":{"mid":4.9387,"mid_ts":1791984394.843,"basis_median":-0.0023}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [4.9277,4.9377] /42144.82USD; nearest_buy_stop_clusters_above: [4.9377,4.9477] /49417.13USD; nearest_long_cascade_bands_below: [4.9277,4.9377] /1608.55USD; nearest_short_squeeze_bands_above: [4.9377,4.9477] /246.94USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":100.0,"min_lot":1.0,"step_lot":1.0,"max_lot":1000.0,"stops_level":20,"point":0.001,"digits":3}; funding {"last_funding_rate_bps":1.0,"predicted_funding_rate_bps":null,"predicted_funding_source":"UNAVAILABLE_IN_PREMIUM_INDEX","mark_price":4.9404,"index_price":4.9422}; funding-history count 8. No proposed-order broker margin/profit receipt implied.

### SP500 / SP500.p

- Quote bid/ask/mid 7777.54/7777.84/7777.69, spread 0.39bps, reported age 0.91588211s; min-lot spread cash diagnostic 0.03 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 7776.23/7810.66232822/7807.11888795; htf_4h_ohlcv: 7776.23/7801.65555483/7783.39339249.
- Session VWAP/sigma/ATR 7811.4877/13.6928/9.1166; 15m EMA200 7808.5691; POC/VAH/VAL 7801.7501/7816.1226/7773.58; pullback {"direction":"SHORT","retrace":0.1348,"depth_sigma":0.0001,"velocity_ratio":0.2705,"bars_pullback":1,"bars_impulse":2,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 7807.5523/7814.5264/7797.2572; prior week 7800.7082/7830.062/7774.15; weekly VWAP 7808.3648; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":29.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":29.0,"15m_tick_cvd":29.0,"5m_tick_cvd":29.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 1717952.58/1656188.29USD, imbalance 0.0183; L3 total/duration>=180 89/52; recurrent primary receipts SELL 7784.93 /2212394.9USD /367.6s; SELL 7781.33 /1863916.84USD /678.0s; BUY 7631.33 /1526000USD /1987.3s.
- Source-specific basis {"HYPERLIQUID":{"mid":7776.15,"mid_ts":1791984394.874,"basis_median":1.33}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [7771.33,7781.33] /519019.13USD; nearest_buy_stop_clusters_above: [7781.33,7791.33] /27216.52USD; nearest_long_cascade_bands_below: [7771.33,7781.33] /175181.11USD; nearest_short_squeeze_bands_above: [7781.33,7791.33] /412.14USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":10.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### NAS100 / NAS100.p

- Quote bid/ask/mid 30339.5/30340.56/30340.03, spread 0.35bps, reported age 0.92052364s; min-lot spread cash diagnostic 0.106 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 30334.75/30542.87703812/30601.68886665; htf_4h_ohlcv: 30334.75/30644.34765911/30736.3228423.
- Session VWAP/sigma/ATR 30558.6955/76.353/58.5633; 15m EMA200 30609.4323; POC/VAH/VAL 30547.617/30613.8472/30488.3584; pullback {"direction":"SHORT","retrace":0.1419,"depth_sigma":0.0,"velocity_ratio":2.5661,"bars_pullback":1,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 30661.2023/30732.8978/30436.5564; prior week 30999.029/31301.5164/30675.6804; weekly VWAP 30617.3762; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-5.0,"divergence":"NEUTRAL"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-5.0,"15m_tick_cvd":-5.0,"5m_tick_cvd":-5.0,"flow_bias":"NEUTRAL","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 4836306.51/5200933.87USD, imbalance -0.0363; L3 total/duration>=180 105/47; recurrent primary receipts BUY 30135.45 /2582571.84USD /2236.0s; BUY 30221.45 /1083282.86USD /308.9s; SELL 30444.45 /1078043.37USD /1536.6s.
- Source-specific basis {"HYPERLIQUID":{"mid":30356.5,"mid_ts":1791984394.954,"basis_median":-15.55}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [30284.45,30384.45] /108570.02USD; nearest_buy_stop_clusters_above: [30384.45,30484.45] /97544.54USD; nearest_long_cascade_bands_below: [30284.45,30384.45] /61702.62USD; nearest_short_squeeze_bands_above: none observed. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":10.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### DJ30 / DJ30.p

- Quote bid/ask/mid 51552.76/51553.94/51553.35, spread 0.23bps, reported age 0.95170546s; min-lot spread cash diagnostic 0.118 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 51514.26/51778.02475612/51759.64033172; htf_4h_ohlcv: 51514.26/51698.23544325/51550.13634072.
- Session VWAP/sigma/ATR 51760.1553/106.6205/73.878; 15m EMA200 51781.6606; POC/VAH/VAL 51695.468/51875.984/51635.296; pullback {"direction":"SHORT","retrace":0.2253,"depth_sigma":0.0,"velocity_ratio":3.165,"bars_pullback":1,"bars_impulse":14,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 51816.76/51979.96/51653.56; prior week 51164.833/51735.172/50940.154; weekly VWAP 51848.6073; trap label TRAPPED_BUYERS_ABOVE.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":21.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":21.0,"15m_tick_cvd":21.0,"5m_tick_cvd":21.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask unavailable/unavailableUSD, imbalance unavailable; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis null.
- First mapped nearest intervals . All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":10.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### GER40 / GER40.p

- Quote bid/ask/mid 25394.2/25395/25394.6, spread 0.32bps, reported age 1.28756952s; min-lot spread cash diagnostic 0.08 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 25329.25/25341.77654869/25288.36576586; htf_4h_ohlcv: 25329.25/25260.06320685/25242.97627623.
- Session VWAP/sigma/ATR 25356.6846/40.8257/42.0298; 15m EMA200 25294.8898; POC/VAH/VAL 25366.1105/25368.344/25256.669; pullback {"direction":"LONG","retrace":0.4173,"depth_sigma":0.0,"velocity_ratio":2.4986,"bars_pullback":3,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 25255.4125/25333.3/25202.65; prior week 25248.1455/25493.286/25107.004; weekly VWAP 25298.1678; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":5.0,"divergence":"NEUTRAL"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":5.0,"15m_tick_cvd":5.0,"5m_tick_cvd":-2.0,"flow_bias":"NEUTRAL","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask unavailable/unavailableUSD, imbalance unavailable; L3 total/duration>=180 0/0; recurrent primary receipts none.
- Source-specific basis null.
- First mapped nearest intervals . All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":10.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### GOLD / XAUUSD.pi

- Quote bid/ask/mid 4087.27/4087.34/4087.305, spread 0.17bps, reported age 1.15497422s; min-lot spread cash diagnostic 0.07 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 4097.86/4149.19340677/4160.45439455; htf_4h_ohlcv: 4097.86/4158.03175677/4165.22740442.
- Session VWAP/sigma/ATR 4140.8192/23.0531/11.5491; 15m EMA200 4161.627; POC/VAH/VAL 4158.9944/4171.0548/4140.3556; pullback {"direction":"SHORT","retrace":0.0533,"depth_sigma":0.0001,"velocity_ratio":0.4568,"bars_pullback":2,"bars_impulse":17,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 4167.1239/4185.561/4150.68; prior week 4164.4375/4178.005/4111.675; weekly VWAP 4168.6164; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-135.0,"divergence":"SELLER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-135.0,"15m_tick_cvd":-135.0,"5m_tick_cvd":-135.0,"flow_bias":"SELLER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 1242995.16/1711003.13USD, imbalance -0.1584; L3 total/duration>=180 62/17; recurrent primary receipts BUY 4072.55 /2038000USD /2238.2s.
- Source-specific basis {"HYPERLIQUID":{"mid":4090.75,"mid_ts":1791984395.101,"basis_median":-3.45}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [4076.55,4086.55] /77904.65USD; nearest_buy_stop_clusters_above: [4086.55,4096.55] /307.22USD; nearest_long_cascade_bands_below: [4076.55,4086.55] /64564.31USD; nearest_short_squeeze_bands_above: [4086.55,4096.55] /9368.64USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.01,"contract_size":100.0,"min_lot":0.01,"step_lot":0.01,"max_lot":50.0,"stops_level":0,"point":0.01,"digits":2}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### SILVER / XAGUSD.pi

- Quote bid/ask/mid 56.719/56.755/56.737, spread 6.35bps, reported age 1.02970695s; min-lot spread cash diagnostic 1.8 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 57.446/58.84183036/59.41548616; htf_4h_ohlcv: 57.446/59.57630938/60.28904603.
- Session VWAP/sigma/ATR 58.5844/0.5854/0.3074; 15m EMA200 59.479; POC/VAH/VAL 59.1478/59.6206/58.4568; pullback {"direction":"SHORT","retrace":-0.3699,"depth_sigma":0.0317,"velocity_ratio":6.7784,"bars_pullback":1,"bars_impulse":18,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 60.5126/60.6661/60.1937; prior week 60.2714/61.4936/59.4743; weekly VWAP 59.8509; trap label TRAPPED_BUYERS_ABOVE.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":38.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":38.0,"15m_tick_cvd":38.0,"5m_tick_cvd":38.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 1265134.2/841611.06USD, imbalance 0.201; L3 total/duration>=180 52/8; recurrent primary receipts none.
- Source-specific basis {"HYPERLIQUID":{"mid":56.7515,"mid_ts":1791984395.168,"basis_median":-0.0375}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [56.6625,56.7625] /12089.77USD; nearest_buy_stop_clusters_above: [56.7625,56.8625] /7019.59USD; nearest_long_cascade_bands_below: [56.6625,56.7625] /38450.28USD; nearest_short_squeeze_bands_above: [56.7625,56.8625] /62452.19USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":5000.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":0.001,"digits":3}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### USWTI / USWTI.p

- Quote bid/ask/mid 95.645/95.693/95.669, spread 5.02bps, reported age 2.14749694s; min-lot spread cash diagnostic 0.048 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 95.84/94.86079645/94.10791904; htf_4h_ohlcv: 95.84/93.71072704/93.12099807.
- Session VWAP/sigma/ATR 95.1393/0.4902/0.3641; 15m EMA200 94.0372; POC/VAH/VAL 94.5059/95.5294/93.9372; pullback {"direction":"LONG","retrace":0.3716,"depth_sigma":0.008,"velocity_ratio":0.4746,"bars_pullback":7,"bars_impulse":9,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 94.1974/94.3957/92.8092; prior week 91.4018/93.6525/90.0824; weekly VWAP 93.5518; trap label TRAPPED_SELLERS_BELOW.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":-3.0,"divergence":"NEUTRAL"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":-3.0,"15m_tick_cvd":-3.0,"5m_tick_cvd":15.0,"flow_bias":"NEUTRAL","order_flow_imbalance_ofi":0.004,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 270939.5/620841.25USD, imbalance -0.3924; L3 total/duration>=180 45/25; recurrent primary receipts SELL 95.8635 /1000002.51USD /372.9s; BUY 95.2925 /999997.41USD /372.9s.
- Source-specific basis {"HYPERLIQUID":{"mid":94.3825,"mid_ts":1791984395.223,"basis_median":1.2905}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [95.5905,95.6905] /42287.23USD; nearest_buy_stop_clusters_above: [95.6905,95.7905] /12367.88USD; nearest_long_cascade_bands_below: [95.3905,95.4905] /5044.84USD; nearest_short_squeeze_bands_above: none observed. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":100.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":0.001,"digits":3}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### EURUSD / EURUSD.pi

- Quote bid/ask/mid 1.1123/1.1123/1.1123, spread 0.09bps, reported age 4.3336544s; min-lot spread cash diagnostic unavailable USD (not full-cost admission).
- HTF htf_1h_ohlcv: 1.1129/1.1190431/1.11903933; htf_4h_ohlcv: 1.1129/1.118813/1.12176182.
- Session VWAP/sigma/ATR 1.1181/0.003/0.001; 15m EMA200 1.1192; POC/VAH/VAL 1.1191/1.1208/1.1188; pullback {"direction":"SHORT","retrace":-0.0467,"depth_sigma":0.3465,"velocity_ratio":1.0791,"bars_pullback":1,"bars_impulse":23,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 1.1159/1.1183/1.1151; prior week 1.1191/1.1222/1.1177; weekly VWAP 1.1185; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":13.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":13.0,"15m_tick_cvd":13.0,"5m_tick_cvd":13.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 599368.81/384664.55USD, imbalance 0.2182; L3 total/duration>=180 13/11; recurrent primary receipts BUY 1.102195 /551350USD /2231.8s.
- Source-specific basis {"HYPERLIQUID":{"mid":1.1128,"mid_ts":1791984395.278,"basis_median":-0.000505}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [1.099495,1.109495] /842251.83USD; nearest_buy_stop_clusters_above: [1.109495,1.119495] /194142.05USD; nearest_long_cascade_bands_below: [1.099495,1.109495] /840586.71USD; nearest_short_squeeze_bands_above: [1.109495,1.119495] /597386.74USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":1e-05,"contract_size":100000.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":1e-05,"digits":5}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### GBPUSD / GBPUSD.pi

- Quote bid/ask/mid 1.3193/1.3193/1.3193, spread 0.08bps, reported age 1.10726547s; min-lot spread cash diagnostic unavailable USD (not full-cost admission).
- HTF htf_1h_ohlcv: 1.32041/1.32543513/1.32457401; htf_4h_ohlcv: 1.32041/1.3237044/1.32359204.
- Session VWAP/sigma/ATR 1.3253/0.0024/0.001; 15m EMA200 1.3246; POC/VAH/VAL 1.3248/1.3268/1.3241; pullback {"direction":"SHORT","retrace":-0.1381,"depth_sigma":0.6985,"velocity_ratio":0.277,"bars_pullback":1,"bars_impulse":2,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 1.3206/1.3234/1.3201; prior week 1.321/1.3245/1.3199; weekly VWAP 1.3239; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":10.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":10.0,"15m_tick_cvd":10.0,"5m_tick_cvd":10.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":-0.001,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 290249.27/179848.2USD, imbalance 0.2348; L3 total/duration>=180 10/7; recurrent primary receipts none.
- Source-specific basis {"HYPERLIQUID":{"mid":1.3199,"mid_ts":1791984395.317,"basis_median":-0.000655}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [1.309345,1.319345] /16063.18USD; nearest_buy_stop_clusters_above: [1.319345,1.329345] /205.9USD; nearest_long_cascade_bands_below: [1.309345,1.319345] /125497.41USD; nearest_short_squeeze_bands_above: [1.319345,1.329345] /1294.82USD. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":1e-05,"contract_size":100000.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":1e-05,"digits":5}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

### USDJPY / USDJPY.pi

- Quote bid/ask/mid 158.934/158.935/158.9345, spread 0.06bps, reported age 1.99962234s; min-lot spread cash diagnostic 0.0062919 USD (not full-cost admission).
- HTF htf_1h_ohlcv: 158.832/158.39588272/158.355273; htf_4h_ohlcv: 158.832/158.34357778/158.17549284.
- Session VWAP/sigma/ATR 158.4333/0.18/0.0829; 15m EMA200 158.356; POC/VAH/VAL 158.3247/158.4893/158.3012; pullback {"direction":"LONG","retrace":-0.034,"depth_sigma":0.0012,"velocity_ratio":0.3732,"bars_pullback":2,"bars_impulse":22,"source":"PRODUCED_15M_BARS"}.
- Prior day POC/VAH/VAL 158.2828/158.4208/157.832; prior week 158.1347/158.398/157.9822; weekly VWAP 158.3596; trap label BALANCED.
- Flow {"status":"TRADFI_USES_MT5_TICK_CVD","session_cvd_usd":37.0,"divergence":"BUYER_AGGRESSION"}; TradFi {"status":"CALCULATED_FROM_MT5_TICKS","tick_count_analyzed":1000,"session_tick_cvd":37.0,"15m_tick_cvd":37.0,"5m_tick_cvd":37.0,"flow_bias":"BUYER_AGGRESSION","order_flow_imbalance_ofi":0.0,"source":"MT5_L1_TICK_STREAM"}.
- 5/15/30m snapshot-anchored delta/coverage 5m: unavailable, 0 buckets; 15m: unavailable, 0 buckets; 30m: unavailable, 0 buckets. Missing TradFi taker arrays are not zero flow.
- Depth bid/ask 822543.66/978012.61USD, imbalance -0.0863; L3 total/duration>=180 38/24; recurrent primary receipts SELL 160.9035 /1608000USD /2231.8s.
- Source-specific basis {"HYPERLIQUID":{"mid":158.835,"mid_ts":1791984395.356,"basis_median":0.1035}}.
- First mapped nearest intervals nearest_sell_stop_clusters_below: [158.1035,159.1035] /14306.27USD; nearest_buy_stop_clusters_above: [159.1035,160.1035] /87209.95USD; nearest_long_cascade_bands_below: [156.1035,157.1035] /861503.57USD; nearest_short_squeeze_bands_above: none observed. All supplied intervals retained in ledger; do not sum top/nearest duplicates.
- Execution {"tick_size":0.001,"contract_size":100000.0,"min_lot":0.01,"step_lot":0.01,"max_lot":100.0,"stops_level":0,"point":0.001,"digits":3}; funding null; funding-history count 0. No proposed-order broker margin/profit receipt implied.

## Appendix B — verification and source manifest

All listed numerical/data checks passed. The original desk prefix is preserved during append; source telemetry and risk registry were not overwritten. Required sources at the pinned commit:

| Source | Bytes | SHA-256 |
|---|---:|---|
| `docs/specs/TRADE_DECISION_PLAYBOOK.md` | 47450 | `48d64f5ee1e00f91672120bb53d6252d1eed6df80793768e4e46d9577b86187e` |
| `docs/trade_plans/LIVE_COLLABORATIVE_ORDER_DESK.md` | 3080882 | `1dfa6242059ef165fe8afca4449e7508055a22f150a304a13cc2b8f92584b67e` |
| `.agents/rules/ACTIVE_CONTEXT.md` | 30965 | `1a5f24f9ff00a9b2922dd66cb2fcb854557e0d121d6cfb3b452e9337f4f9f5d2` |
| `.agents/memory/session_chat_history.md` | 3617333 | `0c9411d88dc108103b839e49e8c5f18f1c5f5ff54f4f13b1e4675263080dddd2` |
| `.agent/skills/arena/SKILL.md` | 19011 | `c06f9828566485d5bd6507150f454d6f37d49c2b02e5308b8f744a4a046bdf39` |
| `.agent/skills/arena/rubric.md` | 3717 | `3296801e01035f3ad8dc2b57f0c47d84d296bbc716bf8b36bdb02b426c2735a5` |
| `Data/initial_position_risk.json` | 2228 | `7f279768ebeeb3ec5763c33b2283b038865769b33423d1ac0111af5fc595cebd` |
