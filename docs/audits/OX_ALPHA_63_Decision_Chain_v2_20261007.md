# OX_ALPHA_63 — GitHub-Anchored Co-Pilot: Decision Chain v2 and Calibrated Plan Queue

**Date:** 2026-10-07 | **Branch:** arena/4adf3661-trading-2 | **Base tip verified:** 6e1bb32
**Deliverable set:** OX_ALPHA_63 specification, docs/prompts/Ox_Alpha_63.txt and docs/specs/OX_ALPHA_63_DECISION_CHAIN_SPECIFICATION.md

---

## 1. Git Synchronization (directive step 1)

`git fetch origin && git checkout arena/4adf3661-trading-2 && git pull` executed. The session workspace had rewound to 9c1cb2d with the prior tip's content uncommitted; a snapshot commit verified the tree bit-identical to the previous pushed state, then reset to the origin tip **6e1bb32** (c4230ca runtime symbol auto-resolution + live candle sync, then the OX_ALPHA_63 spec). Zero divergence; nothing reverted. The default brain tunnel URL now points at the current muscle endpoint (constantly-combines-collectables-script.trycloudflare.com), overridable via ARENA_TUNNEL_URL as always.

## 2. Ground Truth Acknowledged (directive step 2)

- Balance and equity 4,831.73 USD, 100% cash defense, 0.00 margin, 0 positions, 0 pending, 2 of 2 capacity slots open, cushion +56.73 USD above the 4,775.00 floor.
- GOLD short #18576872 closed **+20.80 USD** — the full lifecycle worked: entry 4,176.00, the phase-0 break-even lock at +0.80R guaranteed the floor, and the exit banked +1.98R.
- SOL long #18596013 stopped at 118.85 for **−12.00 USD (−1.00R)** in the overnight liquidation flush, zero excess slippage.
- Net realized from the pair: +8.80 USD. The account is flat and fully defended.

## 3. Forensic Autopsy of the OX_ALPHA_62 SOL Refusal — Endorsed

The local stager refused OXALPHA62-SOL-LONG-20261007A live with `marketable_limit`: by evaluation time SOL had fallen to 118.91 ask, so a 119.95 buy limit crossed the spread and the 119.25 stop would have been above market — an invalid-stops rejection (10016) waiting to happen. **The fail-closed gate operated with 100% fidelity and saved the account from an execution error.** This verdict is now encoded structurally: every plan below carries the passive-entry and stop-placement invariants in its provenance block, and the stager re-verifies them against the live quote at stage time. The SOL re-entry plan in this queue is the corrected successor: it bids 117.10, nearly 2 USD under the market, in front of a 14.62M USD whale shelf.

## 4. Decision Chain v2 (omni.decision_chain.v2) — Directive Step 3

`Terminal/Pioneer_Decision_Engine.py` now carries the six-pillar chain as a strict superset of the v1 Pioneer layer. The v1 engine is preserved verbatim (same five signals, same policy version, same digest rules); v2 extends it:

| Pillar | Factory source | Chain signal | v2 weight |
| --- | --- | --- | --- |
| P1 reconstructed liquidations | liquidation_engine.py | cascade (fuel asymmetry) | 0.20 |
| P2A structural stop clusters | liquidation_engine.py StopClusterEngine | stops (magnet) | 0.08 |
| P2B whale-wall persistence | factory.py _WallTracker | **walls (NEW)**: proximity-weighted resting-wall asymmetry, 180 s anti-spoof persistence re-verified | 0.16 |
| P3 on-chain whale flows | onchain.py / factory ingest | whale (cohort + flows) | 0.08 |
| P4 Farside ETF flows | macro.py FarsideETFFlows | macro (etf component) | 0.16 |
| P5 sentiment + Coinbase premium | macro.py FearGreedIndex, CoinbasePremiumIndex | macro (premium, contrarian F&G) | shared |
| P6 cross-source consistency | crosscheck.py CrossSourceValidator | **consistency (NEW)**: cross-venue consensus vs bus mid, fail-closed below 2 venues or on OI disagreement | 0.08 |
| orderflow (bus tape) | bus.py IntelligenceBus | orderflow (CVD windows, taker ratio) | 0.24 |

Mechanics: the `DecisionChainEngine` attaches the CrossSourceValidator block (venue prices, mid divergence, OI agreement) to every payload, evaluates the seven signals with weight renormalization on any unavailable pillar, stamps a 6-pillar availability manifest **inside the SHA-256 chained digest**, and inherits every fail-closed gate (stale book, macro blackout, quality floor, friction floor of 41 bps + slip + live spread, veto-only tradeability). It is a drop-in wherever `attach_pioneer` is used — the Omni_Trader hook needed zero changes. `OF_Strategy` gains a `--decision-chain {v2,v1}` flag (v2 default). Walls accumulate persistence only under continuous observation (a gap over 30 s resets the cluster — anti-spoof by design), which is exactly what the continuous brain's 15 s tick provides.

## 5. Calibrated Plan Queue — Directive Step 4

Three fresh plans in docs/trade_plans/, all validated by the fail-closed stager at a fixed reference time, all LONG passive dip-buys at persistent whale shelves, all risk within the 14.70 USD queue cap:

| Rank | Plan | Limit | SL | TP | Vol | Risk | SL x ATR | Friction (live) | Anchor |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | OXALPHA63-BTC-LONG | 83,750.00 | 83,443.00 | 84,517.50 (2.50R) | 0.04 | 12.28 USD | 1.50 | 0.049R | 25.05M USD mega bid at 83,500; stop under the wall; RSI 28.9 |
| 2 | OXALPHA63-GOLD-LONG | 4,131.00 | 4,119.50 | 4,159.75 (2.50R) | 0.01 | 11.50 USD | 2.21 | 0.010R | 975k USD bid at 4,120; VWAP 4,149.50 reversion; spread 0.24 bps |
| 3 | OXALPHA63-SOL-LONG | 117.10 | 116.40 | 118.85 (2.50R) | 0.17 | 11.90 USD | 1.73 | 0.329R | 14.62M USD bid at 117.00 + 6.90M at 116.67; stop under both |

Design notes:
- **BTC first**: the largest single persistent wall in the entire 24-asset book, the cleanest friction ratio, and a target that lands before the 19.03M ask wall at 84,866.
- **GOLD**: elite 0.24 bps spread; the entry sits inside the spec's suggested 4,131-4,133 band with the stop deliberately BELOW the 4,120 whale shelf (if the shelf breaks, the thesis is dead — the stop says so structurally). Session VWAP 4,149.50 is the +1.62R waypoint.
- **SOL**: the deliberate lesson-bearer. Its 18.66 bps spread is the widest of the queue, so the stop was widened to 1.73 x ATR purely to hold friction at 0.329R under the 0.35R ceiling. Passive limits only on this symbol — never market orders.
- All three: 24-bar TTL, ARENA:PLAN_v1 comment (journal-tracked, purge via `--purge-expired`), blackout window 17:00-18:30 UTC around today's FOMC minutes (18:00 UTC), plan expiry 20:00 UTC today. ATR basis is the live-synced 15m parquets through 06:45 UTC (Wilder ATR(14): GOLD 5.193, BTC 204.48, SOL 0.405).
- Queue doctrine: with 0 of 2 slots used and the 5-resting-order ceiling, all three may rest simultaneously under first-fill OCO; the muscle-side reconciler still refuses anything that breaches capacity or the 20.00 USD hard cap. EURUSD (Z = −1.78 SD, RSI 24.5) is flagged as the watchlist candidate for the next deliberation cycle.

## 6. Test Evidence — Directive Step 5

- NEW `Tests/Test_Decision_Chain_v2.py`: 16 deterministic offline tests — v1 backward compatibility (5 signals, unchanged policy), wall signal isolation with exact tanh geometry plus spoof/far-wall filtering, consensus signal with exact math plus fail-closed paths, single-pillar weight renormalization, the 6-pillar manifest inside the digest (recomputed hash equality), the full factory-to-advisory chain over the 15 s tick cadence, inherited fail-closed gates, friction floor, veto-only tradeability, and digest determinism.
- EXTENDED `Tests/Test_Stage_Trade_Plan.py`: every committed plan document now validates in a decay-proof parameterized test (fixed reference time, never the wall clock) — 27 tests total.
- Full offline regression: **319 passed / 4 permanent environment failures** (msvcrt, MetaTrader5, uvicorn x2 — Windows- and broker-terminal-bound, unrelated to this change). Zero regressions versus the 303/4 baseline at ffdf7c3.

## 7. Execution Procedure (muscle side, tunnel-reachable)

```
python -m Terminal.Headless.stage_trade_plan docs/trade_plans/OX_ALPHA_63_BTC_Long_20261007.json           # dry run
python -m Terminal.Headless.stage_trade_plan docs/trade_plans/OX_ALPHA_63_BTC_Long_20261007.json --execute # stage
python -m Terminal.Headless.stage_trade_plan --purge-expired                                                # housekeeping
```

Every gate is fail-closed: transport, freshness (120 s), macro blackout, equity cushion above 4,775.00 USD under worst-case stopouts, capacity (fewer than 2 filled, fewer than 5 resting), quote presence, contract-spec match, passive entry (limit strictly below the live ask), and the live-spread friction ceiling of 0.35R. Any failure means NO TRADE, reported and journaled; the muscle re-enforces every cap again on arrival. Once filled, the continuous brain's ratchet owns the position (0.80R/1.50R/2.00R phases, 24-bar decay).

Antigravity pulls this commit directly from GitHub — zero copy-paste. Plans expire at 20:00 UTC today; anything staged after the FOMC minutes requires a fresh deliberation from post-event data.
