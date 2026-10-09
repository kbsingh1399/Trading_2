# Astra risk and final QA audit — 2026-10-09

The current risk implementation does not enforce the latest council protocol. The highest free margin admission path ignores existing pending order losses, removes the USD 20 operating cushion, and allows a fifth independent fill. A flat current snapshot is compatible with these defects; it does not prove the controls will hold after fills.

This is a read-only production audit. No broker orders, cancellations, closes, stop modifications, daemon changes, automation changes, production edits, commits, or parity synchronization were performed. The two artifacts reside in docs/reviews because a telemetry process was reported to auto-stage docs/audits. Raw account/spec/deal evidence, isolated probe outputs, and source SHA-256 values are in [the evidence JSON](C:/Users/SIGMA/Documents/Trading_2/docs/reviews/ASTRA_20261009_risk_qa_evidence.json). Source inspection and probe results below describe the measured checkout, not every possible branch or deployed process.

## Policy being audited

The latest [council protocol](C:/Users/SIGMA/Documents/Trading_2/docs/specs/ANTIGRAVITY_ARENA_THINKING_CHAIN_COUNCIL_PROTOCOL.md) requires a USD 5,000 baseline, USD 4,775 hard floor, USD 4,795 operating floor, up to four filled positions, reservation of open plus pending contingent risk, nominal risk USD 10–15, Phase 0 at +0.80R to +0.15R, Phase 1 at +1.50R to +0.80R, and target +2.0R–2.5R. It also claims Phase 0 guarantees profit and releases all downside risk. Those last two claims are not valid without a cost and execution model.

The scoped activation review read .agents/AGENTS.md, ACTIVE_CONTEXT.md, the latest council protocol, relevant Oct 9 history including the 14:12 stand-down, the roadmap tail, and relevant skills. The .venv-omni runtime has no graphify module; an attempted module query failed. The prebuilt graph JSON was queried with the standard library for the relevant risk symbols before source inspection. No graph or parity update ran. Ruflo/ToolSearch capabilities were not exposed in this subagent's tool inventory. Both primary Engine/forex_engine.py and Engine_2/Engine/forex_engine.py returned false from Test-Path; source for that claimed engine was unavailable here.

## Native MT5 facts

The initial read-only observation was 2026-10-09 14:16:48 UTC; full deal readback and inventory were repeated at 14:22:01 UTC. Both verified login 5064568 and currency USD before interpreting any numbers.

| Property | Native observation |
|---|---:|
| Account trade_mode | 0 = ACCOUNT_TRADE_MODE_DEMO |
| Server / company | BlueberryMarketsSVG-Live / Blueberry Markets (SVG) LLC |
| Balance / equity / free margin | USD 4,896.55 / 4,896.55 / 4,896.55 |
| Used margin / margin level | 0.00 / 0.00 |
| Leverage | 30 |
| Positions | Empty successful inventory |
| Pending orders | One successful inventory |
| Pending ticket | 18736422, magic 100895 |
| Symbol / side / volume | USDJPY.pi / BUY LIMIT / 0.12 |
| Entry / SL / TP | 158.180 / 158.040 / 158.530 |
| Native order_calc_profit at SL | -10.63 USD |

The runtime enum mapping was also queried: DEMO=0, CONTEST=1, REAL=2. A server name ending in “Live” does not override the account type. The account properties and profit valuation meanings follow [MetaQuotes account documentation](https://www.mql5.com/en/docs/constants/environment_state/accountinformation) and [order_calc_profit documentation](https://www.mql5.com/en/docs/python_metatrader5/mt5ordercalcprofit_py). This evidence does not substantiate funded real-money production certification.

The documented nominal calculation is arithmetically correct for this snapshot: 4,896.55 − 10.63 = 4,885.92, giving 110.92 above the hard floor and 90.92 above the operating floor. It is a nominal stop scenario. Applying the code's strict 1.25 stress multiplier plus USD 2 cost reserve gives contingent risk 15.2875, projected equity 4,881.2625, and cushions 106.2625 / 86.2625. Neither scenario bounds unbounded gaps.

The native pending time_setup was 1791549254, which corresponds to 12:34:14 when the server epoch is printed as UTC, or approximately 09:34:14 UTC after the inferred 10,800-second server offset. Native live ticks were about three hours ahead of the local UTC clock; the bridge itself declares 10,800 seconds at [MT5_Execution_Bridge.py:55](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:55). That offset is treated as an inference, preserved alongside raw timestamps. The pending order retains attached SL/TP and can still fill during a coordinator stand-down. Running local ratchet/queue supervision has not been established by this subagent; parent process inspection reported background daemons but no OF/Omni execution process.

## P0 — Admission abandons joint-fill floor reservation when free margin exceeds USD 200

[ live_admission.py:85 ](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:85) switches behavior on free margin. The high free margin branch at [line 105](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:105) sums only filled positions plus the proposed order. Existing pending orders are omitted, and [line 114](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:114) checks 4,775 instead of 4,795. The low/absent free margin branch at [line 118](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:118) reserves positions and pending orders and retains the cushion.

The isolated fake broker probe used balance/equity 4,800, free margin 3,000, and four pending longs in distinct BTC, energy, index, and metal clusters, each with USD 10 nominal stop risk. A proposed USDJPY long with USD 10 risk was accepted. The function reported only 14.50 stress and equity 4,785.50. The correct five-order stress under its own assumptions is 5 × (10 × 1.25 + 2) = 72.50, leaving 4,727.50. This violates both floor levels and produces five filled positions if all five independent orders fill. The same case with absent free margin was refused at 4,727.50 < 4,795.

A second probe showed that a pending inventory row with SL=0 was accepted in the high free margin branch. This branch never values or validates its pending protection before admission. Correlation checks still iterate pending rows, but cannot replace loss reservation.

Repair acceptance should require identical joint-fill accounting regardless of free margin: broker-valued loss for every filled and pending exposure, symbol-specific cost/stop execution reserves, and operating floor clearance. Free margin may add a margin gate; it cannot remove contingent loss or the safety cushion.

## P0/P1 — Position capacity has incompatible definitions and no shared account writer boundary

[ live_admission.py:13 ](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:13) sets MAX_FILLED=6. Its high free margin path allows 12 pending orders at [line 92](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:92). [FloorDefense:73](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/floor_defense.py:73) also defaults to six. Its [line 128](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/floor_defense.py:128) counts only positive-risk rows as positions. With max_concurrent=4 and four filled positions whose nominal risk has become zero, it accepts a fifth trade and reports four free slots. A stop ratchet releases some risk budget; it does not remove a filled position.

The Omni policy fixes two positions at [Risk_Sizing_Engine.py:42](C:/Users/SIGMA/Documents/Trading_2/Terminal/Risk_Sizing_Engine.py:42), while [Omni_Trader.py:706](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:706) permits up to five resting limits and [line 578](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:578) starts client-side cancellation after two fills. This is incompatible with the four-position protocol and is not a broker-atomic OCO guarantee.

[MT5_Execution_Bridge.py:677](C:/Users/SIGMA/Documents/Trading_2/Terminal/MT5_Execution_Bridge.py:677) calls admission before order_check and order_send, without an account-wide shared reservation lock. Admission explicitly acknowledges this lack of atomicity at [line 73](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:73). The OS lock at [Omni_Trader.py:1181](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:1181) protects that run loop and checkout-specific lock file, not every direct bridge caller or other execution process.

Repair acceptance needs a single four-filled-position policy, accounting for all independent pending fills that can occur before cancellation acknowledgement, plus account-scoped serialization and durable PREPARED/UNCERTAIN reservations. If unlimited pending limits remain a policy choice, the four-filled cap cannot be represented as unconditional without an enforceable broker mechanism.

## P1 — Fixed Phase 0 profit is neither net-cost proof nor a universal live ratchet

The standalone manager implements +0.80R to +0.15R at [ratchet_manager.py:43](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/ratchet_manager.py:43) and [line 48](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/ratchet_manager.py:48). For nominal R=USD 10, +0.15R locks only USD 1.50 gross. Even its admission module's USD 2 cost reserve makes that -USD 0.50 net in a simple cost example. The code correctly continues reserving USD 2 for profit-side native stops at [live_admission.py:64](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/live_admission.py:64); protocol zero-downside language contradicts that reserve.

Under the requested 41 bps notional stress assumption, native contract sizes independently verified as SP500=10 and ETH=1 give:

| Illustrative position | Initial stop risk | 41 bps cost reserve | +0.15R gross | Net after that reserve |
|---|---:|---:|---:|---:|
| SP500 entry 7,791.50, SL 7,778.50, volume 0.10 | 13.00 | 31.94515 | 1.95 | -29.99515 |
| ETH entry 2,494.50, SL 2,477.50, volume 0.70 | 11.90 | 7.159215 | 1.785 | -5.374215 |

These are stress-policy counterexamples, not assertions that the broker actually charged 41 bps. Observed native commissions and swap are separately recorded in the ledger. Costs embedded in executable bid/ask paths must not also be charged as the same spread again.

Ordinary stops do not guarantee a fill at the stop price. [Blueberry's own help centre](https://helpcentre.blueberrymarkets.com/en/what-happens-when-an-account-has-no-free-margin) states it cannot guarantee stop-loss fulfilment. Neither a positive stop offset nor maker entry establishes zero future execution loss.

The standalone manager uses a fixed +1.50R stop at Phase 2 at [line 194](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/ratchet_manager.py:194), not the protocol's 15m EMA20 shelf. Its if/elif ladder at lines 161/177/193 moves only one phase per poll. An isolated price jump to +2.5R produced three successive stops: +0.15R, +0.80R, +1.50R. With its [30-second loop](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/ratchet_manager.py:261), stronger protection can be delayed by two further polls.

New fill discovery at [line 242](C:/Users/SIGMA/Documents/Trading_2/Terminal/risk/ratchet_manager.py:242) takes the current native SL as initial SL. It does not recover immutable original risk from a durable record. A restart probe with entry 100 and an already ratcheted SL 101.50 reconstructed R=1.50, then proposed Phase 0 SL=100.225; the tightening guard refused it, leaving the state OPEN even at price 125. Original risk and ratchet phase need durable recovery.

Omni management uses a separate [session conditional policy](C:/Users/SIGMA/Documents/Trading_2/Terminal/Omni_Trader.py:537), with a baseline +0.35R / +0.85R lock and conditional targets at [Uplift_Model.py:32](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:32). Live and replay label versions are explicitly different at [line 24](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:24). A live policy change requires matching evaluation or evidence that earlier evaluation transports to the new policy.

Independent import probes confirmed that GOLD and SP500 are classified COMMODITY/INDEX, but session_regime reclassifies those class labels as CRYPTO at [line 51](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:51). At 14:00 UTC, both receive us_hours, which misses their commodity/index session table and falls back to base parameters. USWTI, USDJPY, and NAS100 themselves classify as CRYPTO at [line 46](C:/Users/SIGMA/Documents/Trading_2/Terminal/Uplift_Model.py:46). These examples are reproducible policy resolution defects, not a claim that every asset currently executes through Omni.

## P0/P1 — The chain certificate does not establish floor compliance

An independently AST-extracted execution of the actual [audit_broker_execution_and_floor](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:404) function with fake MT5 returned PASS for balance/equity 4,780, pending risk present, projected equity 4,780, cushion 5, and risk 0. It made zero calls to orders_get and never enforces the stated 20 cushion. A second probe returned PASS when positions_get returned None: [line 444](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:444) converts unknown inventory to empty inventory.

The function values positions using price difference × contract × volume at [line 459](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:459); that is not account-currency valuation for every symbol, notably JPY-quoted FX. It credits nominal stop profit, omits pending risk and fees, and labels a rolling 12-hour exit-profit-only query as “closed_deals_today” at [line 501](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:501).

An independently extracted verdict aggregator with all six audit layers set to SKIP returned CERTIFIED_100_PERCENT_PRISTINE. The [line 544](C:/Users/SIGMA/Documents/Trading_2/Terminal/chain_verification_360.py:544) branches only reject FAIL or WARN. Therefore the current certificate label is not a reliable admission or production readiness proof.

## Scorecard reconciliation

All 17 named closed position IDs were retrieved independently with history_deals_get(position=...). For each ID, net sums every available entry and exit deal's profit + commission + swap + fee. This follows [MetaQuotes position history API](https://www.mql5.com/en/docs/python_metatrader5/mt5historydealsget_py). Thirty-four raw deals are preserved.

| Scope | Completed positions | Net USD |
|---|---:|---:|
| The protocol's 17 listed positions, Oct 7–9 | 17 | 83.11 |
| Raw server-day Oct 9 | 9 | 66.76 |
| Oct 9 UTC after inferred 10,800-second correction | 8 | 50.75 |

The UTC-day subset is five wins and three losses. The early ETH close at server 00:06:09 belongs to Oct 8 21:06:09 UTC, explaining the server/UTC day count difference. An unadjusted today-to-local-now history query omitted later server-clock deals and returned only five closes; that partial result is not used as the final scorecard.

The 17 listed gross profits sum to 85.31. Recorded commissions sum to -1.89 and swap to -0.31, giving net 83.11. The protocol's 84.05 incorporates the GBPUSD commission but still omits USDJPY commission 0.56, ETH swap 0.31, and gold commission 0.07: together 0.94. Thus 84.05 − 0.94 = 83.11. The 17-position win rate remains 11/17 because these corrections do not change a win into a loss. The account balance is 103.45 below the mandated 5,000 baseline; the selected winning ledger is not an all-account return calculation.

## Tests actually run and limits

Command: .venv-omni/Scripts/python.exe -B -m pytest -p no:cacheprovider tests/Test_Live_Gates_Regression.py::TestJointFill tests/Test_Live_Gates_Regression.py::TestRatchetAndWall::test_failed_close_retries -q

Result: 4 passed in 0.10 seconds. Test source was read first. These cases use FakeBridge and a substituted failed close method; no native orders were sent. [FakeBridge account:95](C:/Users/SIGMA/Documents/Trading_2/Tests/Test_Live_Gates_Regression.py:95) omits free margin, so the three joint-fill regressions cover only the strict branch. The additional numeric, restart, session, and chain verdict probes used fake bridges or AST-extracted functions with fake MT5.

The full suite, a live trader loop, strategy walk-forward backtests, actual stop modifications, and cross-process race injection were not run. The account/spec/history reads establish current observations; they do not validate strategy expectancy or certify a deployment. Production controls must be repaired and evaluated before those broader claims become reviewable.

