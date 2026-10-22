\n# QUANTITATIVE COUNCIL — CYCLE 273\n\n\n**Decision cutoff:** `2026-10-22 21:55:00 UTC`\n
**Ruling:** **HOLD FLAT — NAS100 promoted to armed post-reopen radar, but not stageable at cutoff.**\n\n```\nOpen positions:                 0
Pending orders:                 0
Orders authorized at 21:55:     0
Filled-position capacity:       4/4 free
Risk-bearing pending capacity:  maximum 1
Primary radar:                  NAS100.p short
US2000.p:                       downgraded by fresh negative 15m CVD
BTCUSD.pi:                      trigger-only; no static ticket
FX:                             embargoed until 22:30 UTC
Broker action by this council:  none\n```\n\n---\n\n## 1. Provenance and as-of discipline\n\n\nThe newest `main` commit not later than the decision cutoff was:\n\n- Commit: `8e97f5c8e1f22292b212776b5beb40ad8a2e87f1`\n- Synchronized: `2026-10-22 21:52:01 UTC`\n- Age at decision: `2m59s`\n\nA subsequent commit synchronized at `21:57:50 UTC` appeared during analysis. It was excluded because using it for a `21:55:00` ruling would introduce look-ahead bias.\n\nWorkbook:\n\n- Path: `Data/DataBase_Trading.xlsx`\n- Size: `13,878,598 bytes` / `13.24 MiB`\n- SHA-256: `e21f2f83e04f4d39ab8e658400cbdad97c54753f847934894d5815e32ded67a8`\n- ZIP members: `42`\n- CRC failure: none\n- Governance documents: checksum-identical to the previously reviewed versions\n\nPipeline activity is corroborated by successful repository events through:\n\n- CVD harvest: `21:47:57`\n- Auction harvest: `21:49:29`\n- News harvest: `21:50:30`\n- Calendar harvest: `21:51:25`\n\nThe external process identity `Task 109472` itself is not exposed in repository evidence; its activity is supported by the event sequence and `21:52:01` atomic sync.\n\n---\n\n# 2. Complete 33-sheet physical audit\n\n\nEvery physical coordinate in every worksheet was read.\n\n- Worksheets: `33/33`\n- Physical coordinates traversed: `1,668,543`\n- Populated cells: `1,651,217`\n- Blank coordinates: `17,326`\n- Formulas: `0`\n- Formula errors: `0`\n- Excel error cells: `0`\n- Required-header blanks: `0`\n\n## Dimension fingerprint\n\n\n```\n01 Crypto_ETF_Flows                 4140×18
02 1_Crypto_ETF_Flows                42×18
03 2_Spot_Netflow_S                  501×17
04 3_Exchanges_LS_Ratio_15M          349×11
05 3_Exchanges_LS_Ratio_1H           415×11
06 3_Exchanges_LS_Ratio_4H           217×11
07 4_Hyperliquid_Analysis           1995×20
08 5_OI                               372×21
09 5_Funding_Rate                     592×17
10 6_Funding_Fee_Settlement           930×10
11 7_Liq_Heapmap                       84×7
12 7_Live_Liq                        1004×8
13 8_Exchange_Liquidation_Map_1D     2298×11
14 8_Exchange_Liquidation_Map_7D     2641×11
15 9_Liquidation_Max_Pain_24H         750×11
16 9_Liquidation_Max_Pain_48H         750×11
17 9_Liquidation_Max_Pain_3D          750×11
18 9_Liquidation_Max_Pain_7D          750×11
19 10_Whale_Orders                    176×17
20 11_Technical                       224×48
21 12_Hyperdash                       494×8
22 13_Hyperliquid                     471×13
23 14_Hyperdash_Liq_Map              6004×12
24 15_Hyperdash_Stops_Map            3866×12
25 16_Hyperdash_telegram_Intel       1501×14
26 17_Orderbook                      5524×14
27 18_CVD                           50001×23
28 19_News                             34×11
29 19_Calendar                         38×12
30 00_MT5_Account_Telemetry           172×11
31 Top_Institutions                   602×6
32 ETF_Market_Overview                516×15
33 20_Auction_Market_Structure        173×36\n```\n\n## Auction corrections and defects\n\n\nThe fresh workbook has corrected Auction’s physical position:\n\n- `20_Auction_Market_Structure` is now physical sheet **33/33**, not sheet 30.\n- Row 1 has `36/36` populated and unmerged primary headers.\n- Primary Auction table: rows `1–85`, containing `84` assets.\n- Rows `86–87`: blank separators.\n- Row `88`: merged section title, range `A88:M88`.\n- Row `89`: 13-column pivot-table header.\n- Rows `90–173`: `84` institutional pivot records.\n\nTherefore, Row 1 satisfies the unmerged-header invariant, but the worksheet contains one later merged range.\n\nMaterial data-contract issues:\n\n1. A naïve parser that reads the entire sheet under Row-1 headers will treat the second pivot table as 84 malformed Auction records and overwrite the first table by symbol.\n2. Primary Auction still contains exactly `330` missing session-extreme values:
\n- London high/low: `55 + 55`\n- New York high/low: `55 + 55`\n- IB high/low: `55 + 55`\n\n3. Auction contains `2,392` blanks in total:
\n- `330` substantive primary-table session nulls\n- `2,062` structural blanks caused by the second 13-column section occupying a 36-column sheet\n\n4. Workbook Auction distance fields are stored as decimal fractions with Excel percentage formatting, while JSON emits percentage points. Parsers must normalize the `×100` representation difference.\n5. `2_Spot_Netflow_S` retains duplicated flat headers.\n6. `5_Funding_Rate` retains hierarchical repeated exchange headers.\n7. `19_Calendar` has contracted from 59 to 38 physical rows and now ends on Tuesday, October 20.\n\n**Workbook verdict:** structurally valid ZIP, zero formulas/errors and canonical sheet order now pass; atomic parsing, session completeness and calendar completeness do not.\n\n---\n\n# 3. Source freshness and change audit\n\n\nOnly four sheet XML payloads changed from Cycle 272:\n\n```\n18_CVD
19_News
19_Calendar
20_Auction_Market_Structure\n```\n\nThe other 29 worksheet payloads—including broker quotes, technicals, Orderbook, liquidation maps, stops, OI, funding and ETF sheets—are byte-identical to Cycle 272.\n\n| Source | Latest usable time | Age at 21:55 | Ruling |\n| --- | --- | --- | --- |\n| Auction primary JSON | `21:48:04` | `6m56s` | PASS |\n| CVD latest completed rows | `21:45:00` | `10m00s` | PASS now |\n| News | `21:48:34` | `6m26s` | Fresh, but not event-calendar clearance |\n| Technical matrix | `21:38:11` | `16m49s` | FAIL ≤15m execution standard |\n| Stops map | `21:41:45` | `13m15s` | Timestamp passes; values frozen |\n| Liquidation map | `21:40:44` | `14m16s` | Timestamp passes; values frozen |\n| Funding | `21:35:26` | `19m34s` | FAIL |\n| OI | `21:33:54` | `21m06s` | FAIL |\n| Hyperliquid positions | `21:32:50` | `22m10s` | FAIL |\n| ETF table | `21:31:52` | `23m08s` | FAIL |\n| Whale sheet | `21:24:24` | `30m36s` | FAIL |\n| Broker quote sheet | `21:03:09` | `51m50s` | FAIL |\n| Orderbook | no cell timestamp | unknown | FAIL |\n| Macro calendar | ends Oct 20 | incomplete | FAIL |\n\n\nThe pipeline logged an Orderbook harvest at `21:46:13`, but the sheet remains byte-identical and has no event timestamp. A successful job status is not proof of changed or live microstructure.\n\nThe embedded quotes in `mt5_full_symbol_universe.json` are materially inconsistent with the broker telemetry and have no usable timestamp:\n\n- NAS100: approximately `29,349` versus telemetry `28,907`\n- US2000: approximately `2,765` versus telemetry `2,780`\n- BTC: approximately `81,744` versus telemetry `81,172`\n\nThose untimestamped values cannot authorize a ticket. They also demonstrate why a current broker quote is indispensable: if the embedded NAS/US2000 numbers were current, both proposed limits would be marketable rather than passive.\n\n---\n\n# 4. Account reconciliation and mission arithmetic\n\n\nUser-confirmed live state agrees with the flat account telemetry:\n\n```\nBalance:       $4,818.51
Equity:        $4,818.51
Free margin:   $4,818.51
Positions:     0
Pending orders:0
Hard-floor cushion:      $43.51
Operating-buffer cushion:$23.51\n```\n\nBTC ticket `#19227609` remains successfully cancelled, retcode `10009`.\n\nMission gap:\n\n```\n$5,500.00 − $4,818.51 = $681.49
Required gain = 14.1432%\n```\n\nFrom `2026-10-22 21:55` to `2026-10-23 23:59` is **26h04m**, not approximately 21 hours.\n\nThe current floor permits maximum aggregate risk plus spread cost of:\n\n```\n((4,818.51 − 4,795.00) − 2.00) / 1.25
= $17.208\n```\n\nTherefore, the operator’s permission to increase nominal risk to `$25–35` is mathematically unavailable under the current operating floor. The floor, not the aspirational deadline, controls.\n\n---\n\n# 5. Full-universe affirmative discovery\n\n\nCurrent coverage:\n\n- Broker universe: `156`\n- Technical rows: `119`\n- Primary Auction assets: `84`\n- CVD assets: `28`\n- Baseline spread passes: `45`\n- Spread-disqualified: `111`\n- Assets simultaneously possessing spread pass, technicals and Auction: `32`\n\n## Fresh radar hierarchy\n\n\n| Rank | Candidate | Structural observation | Disposition |\n| --- | --- | --- | --- |\n| 1 | NAS100.p short | Strong bearish EMA hierarchy, trend-down Auction, DVAL retest ticket, fresh negative CVD | Primary post-reopen radar |\n| 2 | AU200.p short | Strong bearish, `−2.058σ`, DVAL `8,775.14`, only `0.938 ATR` away | Next-session radar; no current quote |\n| 3 | UKBRENT.p long | Strong bullish, trend-up acceptance, DVAH `113.595`, `0.817 ATR` from snapshot price | Radar; no current tape |\n| 4 | XMRUSD.p short | Bearish, `−2.147σ`, RSI `26.80`, below DVAL `592.50` | Crypto evidence insufficient: no fresh CVD/wall proof |\n| 5 | US2000.p long | Strong bullish and DPOC geometry | Downgraded by negative fresh 15m CVD |\n\n\nNo newly discovered candidate has complete live quote, macro clearance, dynamic spread and trigger evidence. No additional ticket is authorized.\n\n---\n\n# 6. Persona 1 — Orderflow, Auction, L2 and cascades\n\n\n## NAS100.p\n\n\nCurrent source-proven CVD is:\n\n| Horizon | Delta | Regime |\n| --- | --- | --- |\n| 5m | `−$237.820M` | AGGRESSIVE SELLING |\n| 15m | `−$803.995M` | AGGRESSIVE SELLING |\n| 1h | `−$3.43631B` | AGGRESSIVE SELLING |\n| 4h | `−$9.65555B` | AGGRESSIVE SELLING |\n\n\nThe prompt’s `−$997.6M / −$4.49B / −$11.07B` values are not present in the cutoff workbook and are not used.\n\nStructural geometry:\n\n- Auction price: `28,907.03`\n- Entry: `29,085`\n- DVAL: `29,087.86`\n- Entry below DVAL: `2.86 points`\n- ATR: `71.6608`\n- Entry distance from Auction price: `177.97`, or `2.484 ATR`\n- Fresh 5m CVD close: `28,914.10`\n- Entry distance from CVD close: `2.385 ATR`\n\nThe negative 5m condition now exists, but it occurred while price remained far below the intended entry. It does not prove rejection at DVAL.\n\nA pre-staged limit would fill before the required rejection can be observed. The correct sequence is:\n\n```\nReopen
→ live quote and spread normalize
→ retracement reaches 29,085–29,090
→ failed acceptance/rejection at DVAL
→ fresh negative 5m CVD accompanies downward response
→ stage 29,085 SELL_LIMIT for the retest\n```\n\n## US2000.p\n\n\n- Auction DPOC: `2,775.78`\n- Technical DPOC: `2,775.8391`\n- Entry: `2,776`\n- Strong bullish EMA hierarchy remains intact.\n\nFresh CVD now vetoes the long:\n\n| Horizon | Delta | Regime |\n| --- | --- | --- |\n| 5m | `+$0.361M` | NEUTRAL CHOP |\n| 15m | `−$14.791M` | AGGRESSIVE SELLING |\n| 1h | `−$10.129M` | DELTA ALIGNED |\n| 4h | `+$103.557M` | AGGRESSIVE BUYING |\n\n\nThe required positive 15m turn is absent. The 5m value is too small and explicitly classified neutral.\n\n## BTCUSD.pi\n\n\nCurrent Auction:\n\n- Price: `81,357.50`\n- DPOC: `81,339.50`\n- DVAH: `81,465.28`\n- DVAL: `81,306.40`\n- Regime: `ROTATIONAL_BALANCE`\n- Technical regime: `NEUTRAL / CHOP`\n- ATR: `207.5631`\n\nThe `80,450` trigger is `907.5` points or `4.372 ATR` below the current Auction price. No cascade has occurred.\n\nFresh CVD:\n\n| Horizon | Delta | Regime |\n| --- | --- | --- |\n| 5m | `−$4.338M` | AGGRESSIVE SELLING |\n| 15m | `−$4.211M` | BEARISH ABSORPTION |\n| 1h | `+$13.387M` | DELTA ALIGNED |\n| 4h | `+$30.306M` | BULLISH ABSORPTION |\n\n\nThis is short-term selling inside balance, not post-cascade exhaustion.\n\nUntimestamped L2 remains ask-heavy:\n\n- Bid depth: `$3.048M`\n- Ask depth: `$4.247M`\n- Ask share: `58.22%`\n- Book imbalance: `−16.44%`\n- Ask/bid ratio: `1.393`\n\nThe apparent L3 bids near `80,380`, `80,351` and `80,008` remain untimestamped and lack presence/cancellation proof.\n\nFrozen map totals:\n\n- `80,450`: `$12.06M` long liquidations + `$5.31M` sell stops = `$17.37M`\n- `80,050`: `$6.07M` long liquidations + `$22.64M` sell stops = `$28.71M`\n\nThe maps still use mark `81,264.50`, which is:\n\n- `93` below current Auction price, or `11.43 bps`\n- `155.1` below the 5m CVD close, or `19.05 bps`\n\nThe values are unchanged despite updated timestamps. They cannot support a static limit.\n\n## Persona 1 — Section 2.5 answer\n\n\n1. **Conjunctive sclerosis:** The 3-of-4 Tier-2 model is sound; current rejection is caused by Tier-1 data failures, not minor indicator disagreement. Crypto wall requirements must not be imposed on TradFi.\n2. **Static versus live:** Snapshot CVD cannot substitute for at-entry rejection. Candidate generation must promote setups early, then require live event-state transitions.\n3. **Limit adverse selection:** Limits should be staged on the retest after rejection/reclaim, not before the causal trigger. This prevents NAS filling into an unrejected rally and BTC filling before the cascade.\n4. **Specialization:** Indices use Auction, EMA hierarchy, cash-session state and futures delta. Crypto uses timestamped L2/L3, venue basis and liquidation sequencing.\n5. **Concrete improvement:** Implement `DISCOVERED → APPROACHING → TOUCHED → REJECTED/RECLAIMED → ARMED → STAGED`, with each transition timestamped. The current desk often jumps from discovered directly to staged.\n\n---\n\n# 7. Persona 2 — Exact sizing and solvency\n\n\n## NAS100.p contract arithmetic\n\n\n```\nSELL_LIMIT 0.03 @ 29,085
SL 29,130
TP 28,970

Contract size = 10
Risk          = 45 × 10 × 0.03 = $13.50
Reward        = 115 × 10 × 0.03 = $34.50
R:R           = 2.556R
Spread cost   = 1.42 × 10 × 0.03 = $0.426
Friction      = 1.42 / 115 = 1.235%
Stress        = ($13.50 + $0.426) × 1.25 + $2
              = $19.4075
Stressed equity = $4,799.1025
Buffer surplus  = $4.1025
Hard-floor surplus = $24.1025\n```\n\nSafe short-stop threshold:\n\n```\n29,087.86 + 0.50×71.6608 + 0.71
= 29,124.40\n```\n\n`SL 29,130` clears that threshold by `5.60 points`.\n\nThe submitted `$18.88` stress excludes spread cost. `0.04` lot would leave equity at approximately `$4,793.30`; therefore `0.03` is the maximum viable NAS size.\n\n## US2000.p contract arithmetic\n\n\n```\nBUY_LIMIT 0.30 @ 2,776.00
SL 2,771.50
TP 2,787.00

Contract size = 10
Risk          = 4.50 × 10 × 0.30 = $13.50
Reward        = 11 × 10 × 0.30 = $33.00
R:R           = 2.444R
Spread cost   = 0.32 × 10 × 0.30 = $0.96
Friction      = 0.32 / 11 = 2.909%
Stress        = ($13.50 + $0.96) × 1.25 + $2
              = $20.075
Stressed equity = $4,798.435
Buffer surplus  = $3.435
Hard-floor surplus = $23.435\n```\n\nSafe long-stop threshold:\n\n```\n2,775.78 − 0.50×5.68685 − 0.16
= 2,772.78\n```\n\n`SL 2,771.50` clears it.\n\n`0.35` lot is the mathematical ceiling:\n\n- Stress: `$23.0875`\n- Stressed equity: `$4,795.4225`\n- Remaining operating cushion: only `$0.4225`\n\n`0.36` lot fails with stressed equity `$4,794.82`. The defensible size remains `0.30`.\n\n## Aggregate pending-order capacity\n\n\nIf NAS and US2000 were simultaneously independently fillable:\n\n```\nAggregate stressed loss = $19.4075 + $20.075
                         = $39.4825
Stressed equity = $4,779.0275
Operating-buffer deficit = $15.9725\n```\n\nTherefore, only one risk-bearing pending order may exist.\n\n## Persona 2 — Section 2.5 answer\n\n\n1. **Conjunctive sclerosis:** Risk and floors remain Boolean. Secondary confluence should be probabilistic.\n2. **Static versus live:** Lot rights must be recalculated with the current broker spread and actual structural stop immediately before `order_check`.\n3. **Limit adverse selection:** Stop location comes first; lot size is derived afterward. Compressing a stop merely to obtain more size creates false solvency.\n4. **Specialization:** Contract multipliers, tick values and quote currencies must be handled per symbol. Equal lots are not equal risk.\n5. **Concrete improvement:** Rank candidates by expected return per dollar of stressed capacity, not raw setup score. Do not increase risk merely to chase the deadline.\n\n---\n\n# 8. Persona 3 — Macro, flows and session risk\n\n\n- The refreshed calendar contains only 37 events and terminates on Tuesday, October 20.\n- It contains no Wednesday–Friday coverage for the current decision.\n- Recent News rows are low-impact narrative items and cannot substitute for a sovereign economic calendar.\n- Therefore, the ±35-minute TradFi event window and ±15-minute crypto window cannot be affirmatively cleared.\n\nOther sources are stale:\n\n- ETF: `23m08s`\n- Hyperliquid positioning: `22m10s`\n- OI: `21m06s`\n- Funding: `19m34s`\n- Whale orders: `30m36s`\n\nIndex trading is additionally blocked by the opening-transition spread freeze. No order should be staged on the first reopen quote.\n\nFX remains under the stricter operator embargo:\n\n```\n21:15–22:30 UTC\n```\n\n## Persona 3 — Section 2.5 answer\n\n\n1. **Conjunctive sclerosis:** Missing crypto flow narratives should not veto an index trade, but event-calendar clearance is a Tier-1 requirement.\n2. **Static versus live:** ETF and CEX observations must decay to zero weight once stale; old flows must never be carried forward as current evidence.\n3. **Limit adverse selection:** Session-open and rollover limits are exposed to discontinuous repricing and spread expansion. Stage only after normalization.\n4. **Specialization:** Indices require cash-session/reopen models; FX requires rollover and sovereign-event models; crypto requires continuous venue/basis models.\n5. **Concrete improvement:** Maintain asset-class-specific clocks, event embargoes and freshness budgets rather than one universal scanner cadence.\n\n---\n\n# 9. Exact ticket dispositions\n\n\n## A. NAS100.p — ARMED RADAR; DO NOT PLACE AT 21:55\n\n\n```\nSELL_LIMIT 0.03 @ 29,085.00
SL 29,130.00
TP 28,970.00
Expiry: 12 completed 15m bars after placement\n```\n\nAll of the following are required:\n\n1. Broker session confirmed open.\n2. Current quote age ≤2 seconds.\n3. Live ask satisfies:
\n```\n28,941.68 ≤ ask < 29,085.00\n```\n
The upper bound preserves a genuinely passive sell limit.\n4. Current calendar verifies no high-impact event within ±35 minutes.\n5. Instantaneous and 60-second p95 spread pass.\n6. `spread_now <= 1.5 × median_5m`.\n7. Price touches or probes `29,085–29,090`.\n8. Failed acceptance/rejection at DVAL is observed.\n9. A newly completed 5m CVD interval remains negative during the downward response.\n10. `order_check` and broker profit calculation pass.\n\nThe current `21:45` CVD will be 20 minutes old by `22:05`; it cannot authorize a post-reopen entry without refresh.\n\n## B. US2000.p — REJECTED NOW; CONDITIONAL RADAR ONLY\n\n\n```\nBUY_LIMIT 0.30 @ 2,776.00
SL 2,771.50
TP 2,787.00
Expiry: 12 completed 15m bars after placement\n```\n\nReconsider only after:\n\n- fresh 15m CVD becomes materially positive rather than negative/neutral;\n- DPOC `2,775.78` is tested and reclaimed;\n- a post-reopen retest holds;\n- live ask remains above `2,776`;\n- live bid is no more than `2,787.37`, preserving the two-ATR distance rule;\n- all spread, calendar and broker checks pass.\n\nCurrent 15m CVD is `−$14.791M`; no long is authorized.\n\n## C. BTCUSD.pi — NO TICKET\n\n\n```\n80,650 sweep
→ 80,450 sweep
→ seller-delta deceleration
→ live bid replenishment/absorption
→ 5m reclaim above 80,500
→ retest
→ calculate entry, SL, TP and lot from the actual sweep low\n```\n\nNo `80,480` pre-staged limit and no reuse of `80,080` as a stop.\n\n## D. FX\n\n\n```\nNo FX order before 22:30 UTC.\n```\n\n---\n\n# 10. Mandatory 10-point pre-punch checklist\n\n\nLegend: `PASS` = geometry/source-proven now; `COND` = must be observed at trigger; `FAIL` = currently absent.\n\n| # | Verification | NAS100 | US2000 | BTC cascade long |\n| --- | --- | --- | --- | --- |\n| 1 | Wall polarity/persistence or asset-specific substitute | **COND**—post-open Auction rejection/depth | **COND**—DPOC hold | **FAIL**—walls untimestamped |\n| 2 | Stop-cascade/sweep clearance | **COND**—reopen path unknown | **COND**—retest not observed | **FAIL**—80,450 unswept |\n| 3 | CVD absorption/deceleration | **COND**—negative now, not at entry | **FAIL**—15m negative | **FAIL**—no post-sweep deceleration |\n| 4 | Safe structural SL | **PASS** | **PASS** | **FAIL**—no current ticket |\n| 5 | Causal Auction location | **PASS**—Model 2 DVAL retest | **PASS**—bull-trend DPOC pullback | **FAIL**—balanced, no extreme sweep |\n| 6 | Dynamic spread efficiency | **FAIL**—live/p95/median absent | **FAIL**—live/p95/median absent | **FAIL**—live basis/spread absent |\n| 7 | HTF hierarchy alignment | **PASS** | **PASS** | **FAIL/MIXED** |\n| 8 | Setup-specific trigger complete | **FAIL** | **FAIL** | **FAIL** |\n| 9 | TP runway and ≥2R | **PASS 2.556R** | **PASS 2.444R** | **FAIL**—undefined |\n| 10 | Stressed floor defense | **PASS at 0.03** | **PASS at 0.30** | **FAIL**—undefined |\n\n\nNo candidate has ten passes.\n\n## Execution-autopsy overlay\n\n\n| Gate | Status |\n| --- | --- |\n| Quote age | **FAIL** — `51m50s` |\n| Queue-ahead notional | **FAIL** — unavailable |\n| Partial-fill handling | Prospective only; recalculate risk on every fill |\n| Session-transition spread | **FAIL** — reopen not yet normalized |\n| BTC wall presence ≥180s | **FAIL** |\n| Correlation/capacity | **PASS only if one order is staged** |\n| Schema contract | **FAIL** — multi-table Auction parsing risk and incomplete calendar |\n\n\n---\n\n# Final council order state\n\n\n```\nAT 21:55 UTC:                 HOLD FLAT
NAS100.p:                     ARMED POST-REOPEN RADAR; NOT STAGED
US2000.p:                     REJECTED BY NEGATIVE 15m CVD
BTCUSD.pi:                    NO STATIC LIMIT; SWEEP/RECLAIM ONLY
FX:                           EMBARGO THROUGH 22:30 UTC
MAX RISK-BEARING LIMITS:      1
BROKER TRANSMISSION:          NONE
NEXT VALID INDEX ASSESSMENT:  after fresh quote, calendar clearance,
                              rejection/reclaim evidence and spread normalization\n```\n