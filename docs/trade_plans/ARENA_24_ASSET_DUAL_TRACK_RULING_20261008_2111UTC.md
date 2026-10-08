# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 21:11:19 UTC)

**Status:** advisory and dry-run. The desk executes. Nothing was placed or cancelled by the agent. No MT5 access.
**Telemetry on origin:** last commit covers as_of **20:41:20 UTC**, about 30 minutes before this briefing. Stale. Telemetry-based geometry and depth are from 20:41. Briefing prices are from 21:11.

## 0. Bottom line

1. **No candidate is admissible under the new TP mandate as of now.** The mandate anchors TP to a verified liquidation, stop, or whale pool. Telemetry shows **UNAVAILABLE for every asset** (no stop-order feed, no liquidation feed, no L3 whale walls). The only verified structure is the volume-profile value area.
2. **Top 2 LIMIT stages (blocked on the TP anchor, ready otherwise):**
   - **#1 LNKUSD.p SELL LIMIT 12.651.** Stop 12.798 (1.55 ATR). Lot 0.70. Nominal 10.28, stressed 14.80. TP 2.50R = 12.284, which is beyond the value area low (about 12.38, roughly 1.8R). **TP unanchored.**
   - **#2 LTCUSD.pi SELL LIMIT 63.100.** Stop 64.150. Lot 0.10. Nominal 10.50, stressed 15.12. TP 2.50R = 60.475, which is beyond the value area low (about 61.78, roughly 1.3R). **TP unanchored.**
3. **Capacity:** briefing shows 0 open positions and 1 pending (NERUSD). Telemetry (stale) shows ETH open and 4 pending. The briefing's balance change (+16.01) is consistent with ETH closing near 2455, which matches the briefing's stop, but that is unverified. Under the max-2 cap (telemetry, and the 20:25 ruling's count), **one slot is free.** Only one of #1 or #2 may be staged.
4. **ETH #18706769:** briefing says closed, no open positions. Verify in MT5. If still open, telemetry SL 2434.52 and briefing SL 2455.1 conflict.
5. **NERUSD 18713247: KEEP.** Briefing price 4.519, entry 4.617, distance 0.098 = 1.37 ATR (ATR 0.0718). Under the 2.0 ATR trigger. Sizing flag stands (12.70 nominal, 18.29 stressed).
6. **Model 1: zero candidates.** Telemetry VWAP Z max |Z| 1.59 (GBPUSD). None at 2.0.
7. **Joint stress:** if NERUSD, LTC, and LINK all stop out at stressed values, equity is 4,845.80 - 18.29 - 15.12 - 14.80 = **4,797.59**. That is above the 4,795 buffer by 2.59, and above the 4,775 hard floor by 22.59. Nominal worst case is 4,812.

## 1. Discrepancies (read before acting)

| Item | Briefing 21:11 | Telemetry (20:41, stale) | Action |
|---|---|---|---|
| Positions | 0 open | ETH 0.37 long, open | Confirm in MT5 |
| Pending | NERUSD only | 4 (NERUSD + 3 CFD BUYs) | Confirm 3 CFD BUYs deleted |
| Balance / equity | 4,845.80 / 4,845.80 | 4,829.79 / 4,851.25 | Consistent with ETH closed (+16.01 realized) |
| Capacity policy | "no artificial 2-order cap" | max_concurrent 2 | Briefing policy not in telemetry. Ruling applies max 2 (conservative) |
| TP anchor data | Long Flush / Short Squeeze N/A | UNAVAILABLE all assets | TP anchor cannot be verified |
| NERUSD price | 4.519 | — | Used briefing |
| LINK mid / ATR | 12.638 / 0.0947 | 12.618 / 0.1014 | Used briefing ATR |
| LTC mid / ATR | 63.005 / 0.3675 | 63.035 / 0.3979 | Used briefing ATR |

## 2. Model 2 and Model 1 scan (24 assets)

**SELL shelves in BEARISH regime (0.10 to 0.60 ATR above mid):**
- **LNKUSD.p:** EMA50 12.651 = +0.14 ATR (briefing mid and ATR). **Passes geometry.** Depth at 20:41: ask band 858k, bid band 573k (ask-heavy 1.50x). Ask band 12/12 at or above 150k. **Candidate, TP unanchored.**
- **LTCUSD.pi:** entry 63.10 = +0.26 ATR (briefing). Ask band 12/12 at or above 554k. **Candidate, TP unanchored.**
- **BTCUSD.pi:** 81,833 = +0.56 ATR (briefing mid 81,656.5, ATR 315.5). Ask band 11/12 (min 115k). **WATCH.** Not admitted (fails 12/12). EMA50 81,873 is +0.69 ATR (out of band).
- **NERUSD.p:** live order, held (see §0).
- **SP500.p:** VWAP 7770.32 = +0.04 ATR. Below the 0.10 floor. **Dropped.**
- **USDJPY.pi:** EMA20 +0.87 ATR. Out of band. **Dropped.**
- **SOLUSD.p:** excluded by standing ruling.
- **DOGUSD.p:** retired at 20:25.
- Others: no SELL shelf inside 0.10 to 0.60 ATR.

**BUY shelves in BULLISH regime (0.10 to 0.60 ATR below mid):**
- **DJ30.p:** VAH 51,217 = -0.15 ATR (briefing mid 51,227.7, ATR 71.1). In band. **15m rejection wick 13%** on the 20:30 bar (low 51,214, close 51,220). Track 1 needs 30%. **NOT ADMITTED.**
- **XAUUSD.pi:** VAH 4129.6 = -0.64 ATR. Out of band. **Dropped.**
- **USWTI.p, EURUSD.pi, GBPUSD.pi:** no BUY shelf in band.

**Model 1 (|Z| at least 2.0 with RSI gate):** zero candidates.

## 3. Track 2 persistence (last 12 telemetry receipts, through 20:41)

| Level | Min kUSD | At or above 150k | Verdict |
|---|---|---|---|
| LNK 12.651 | 386 | 12/12 | PASS |
| LTC 63.10 | 554 | 12/12 | PASS |
| BTC 81,833 | 115 | 11/12 | WATCH |
| NEAR 4.617 | 0 | 11/12 | Live, held |

No receipts after 20:41 are available, so persistence is not extended to this briefing.

## 4. Blueprints

| Rank | Symbol | Side | Entry | Stop | TP (2.5R) | Lot | Nominal | Stressed | TP anchor status |
|---|---|---|---|---|---|---|---|---|---|
| 1 | LNKUSD.p | SELL LIMIT | 12.651 | 12.798 | 12.284 | 0.70 | 10.28 | 14.80 | Unanchored. VAL about 12.38 (~1.8R). Blocked |
| 2 | LTCUSD.pi | SELL LIMIT | 63.100 | 64.150 | 60.475 | 0.10 | 10.50 | 15.12 | Unanchored. VAL about 61.78 (~1.3R). Blocked |

Stop distance is 1.55 ATR for LINK and 2.86 ATR for LTC at briefing ATR. Both exceed the 1.50 floor.

## 5. Desk decision needed

Under the new TP mandate, neither candidate can be staged. Options for the desk:
1. **Hold** until a verified liquidation, stop, or whale feed is restored. Recommended.
2. **Accept the volume-profile value area as a TP anchor.** This gives roughly 1.3R to 1.8R, which fails the 2.0R minimum. Requires explicit desk override.
3. **Accept the unanchored 2.5R TP.** This violates the mandate. Requires explicit override.

Also note that both candidates are short crypto, along with NERUSD. The three are correlated. The joint stress above assumes all three stop out together.

## 6. Governance

- **Capacity:** one slot free under max 2. Zero orders staged by this agent.
- **NERUSD 18713247:** KEEP.
- **ETH 18706769:** verify closed. Telemetry is stale.
- **Telemetry:** the sync is stalled at 20:41:27 UTC. Restart before any staging.
- **Retired / excluded:** DOGE (retired 20:25), SOL (excluded).

## 7. Caveats

- Telemetry is about 30 minutes old. Depth and persistence need a fresh tick.
- The briefing's account and capacity state conflicts with telemetry. Not reconciled.
- The 15m bar for 20:45 is not supplied for the CFDs. Track 1 wick and volume gates cannot be fully verified.
