# Trading Desk Council — Cycle 121 PURE TELEMETRY & PLAYBOOK ANALYSIS — GPT_ASTRA TAB1
**Generation:** `71076970432c426fa836ed01153fb189` | **As of:** 2026-10-15 18:10:34 UTC | **Size:** 4320788 bytes | **Commit:** 206e6600173a3838726da9f94524bb29c7a8f863
**Account:** #5064568 Balance 4837.48 Equity 4858.97 (prompt 4861.51) MarginUsed 1188.35 Free 3670.62 Level 408.88% Hard 4775 Buffer 4795 Cushion +83.97/+63.97 (+86.51/+66.51 prompt)
**Risk BROKER_VALUED:** SP500 #18969343 nominal 18.5 stressed 25.125, GOLD #18970131 nominal 0.0 stressed 2.0 total 27.125 post 4810.355 required 4795 PASS buffer +15.355 (prompt says 4.00 stress total 4833.48 +38.48, but file shows 27.125)
**Macro:** BoE Governor Bailey Fireside Chat 2026-10-16 02:00 UTC blackout_active False
**Telemetry Source:** git fetch origin main --depth=20, git log shows 206e660 contains 71076970432c426fa836ed01153fb189, git show 206e660:docs/telemetry/live_snapshot_latest.json > /tmp/latest_121_target.json

## 1. Telemetry & Playbook Ingestion Citation
- Generation 71076970432c426fa836ed01153fb189 as_of 2026-10-15 18:10:34 UTC size 4320788 commit 206e660
- Fetched via git fetch origin main --depth=20, found via loop over commits, verified SHA
- Playbook docs/specs/TRADE_DECISION_PLAYBOOK.md retrieved via raw main, ACTIVE_CONTEXT.md floor 4775 buffer 4795
- Account baseline PASSIVE LIMIT ONLY, Blueberry MT5 #5064568 Balance 4837.48 Equity 4861.51 Margin 1188.35 Realized Deals: SP500 #18836609 +0.90 Trailing SL 7807.75, ETH #18826511 +1.92 Profit Lock 2513.02, SOL #18813768 +9.52 Phase1 Lock, BTC #18813767 +16.10 full TP
- Risk formula Stressed Loss =1.25*nominal+2.00 min(balance,equity)-sum(stressed)>=4795 enforced
- Capacity: Open stress 4.00 (prompt) / 27.125 file, worst-case equity 4833.48 +38.48 buffer, max 1 new ticket at 14.50 risk 20.12 stress, 2/4 filled 2 available
- Macro event BoE Governor Bailey Fireside Chat 2026-10-16 02:00 blackout_active False per Part H
- Observed_only policy, no invented data

## 2. Mandate1 Dual-Engine Search 24 Assets
| Symbol | Mid | Spread bps | Z | RSI | Regime | Engine1 | Engine2 | Final | Walls tot/pers/pers_thresh | Friction |
| BTC | 82161.5 | 1.95 | 1.74 | 65.01 | BULLISH | FAIL |Z| 1.74 <2.0 | Z 1.74 within PASS regime BULLISH EMA20 81844.41 EMA50 81505.64 POC 81177.625 RS | WATCHLIST | 357/99/0 | PASS |
| ETH | 2436.95 | 12.72 | 2.02 | 70.7 | BULLISH | Z 2.02 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.02 outside 0.2-1.8 window | WATCHLIST | 166/52/4 | PASS |
| SOL | 105.435 | 23.71 | 1.69 | 65.74 | BULLISH | FAIL |Z| 1.69 <2.0 | Z 1.69 within PASS regime BULLISH EMA20 104.68 EMA50 103.78 POC 102.0258 RSI 65. | WATCHLIST | 57/22/10 | PASS |
| BNB | 732.6 | 8.19 | 1.90 | 65.96 | BULLISH | FAIL |Z| 1.90 <2.0 | FAIL |Z| 1.90 outside 0.2-1.8 window | WATCHLIST | 10/7/2 | PASS |
| XRP | 1.337 | 29.92 | 1.80 | 63.53 | BULLISH | FAIL |Z| 1.80 <2.0 | Z 1.80 within PASS regime BULLISH EMA20 1.33 EMA50 1.32 POC 1.3229 RSI 63.53 not | WATCHLIST | 0/0/0 | PASS |
| ADA | 0.2303 | 91.17 | 2.26 | 69.02 | BULLISH | Z 2.26 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.26 outside 0.2-1.8 window | NO SETUP BANNED friction | 0/0/0 | FAIL |
| DOGE | 0.0809 | 259.42 | 2.46 | 59.78 | RANGE_BOUND | FAIL RANGE_BOUND STAND ASIDE | FAIL RANGE_BOUND STAND ASIDE | NO SETUP BANNED friction | 0/0/0 | FAIL |
| TRX | 0.3314 | 30.18 | 1.02 | 53.38 | BULLISH | FAIL |Z| 1.02 <2.0 | Z 1.02 within PASS regime BULLISH EMA20 0.33 EMA50 0.33 POC 0.3309 RSI 53.38 tow | NO SETUP | 0/0/0 | PASS |
| DOT | 1.1285 | 186.09 | 2.23 | 68.31 | RANGE_BOUND | FAIL RANGE_BOUND STAND ASIDE | FAIL RANGE_BOUND STAND ASIDE | NO SETUP BANNED friction | 0/0/0 | FAIL |
| LINK | 12.4965 | 69.62 | 2.12 | 65.41 | BULLISH | Z 2.12 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.12 outside 0.2-1.8 window | NO SETUP BANNED friction | 0/0/0 | FAIL |
| BCH | 278.7495 | 28.02 | 2.53 | 71.44 | BULLISH | Z 2.53 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.53 outside 0.2-1.8 window | WATCHLIST | 0/0/0 | PASS |
| LTC | 60.105 | 49.91 | 1.98 | 69.73 | BULLISH | FAIL |Z| 1.98 <2.0 | FAIL |Z| 1.98 outside 0.2-1.8 window | NO SETUP BANNED friction | 0/0/0 | FAIL |
| AVAX | 9.955 | 30.14 | 1.82 | 64.68 | BULLISH | FAIL |Z| 1.82 <2.0 | FAIL |Z| 1.82 outside 0.2-1.8 window | WATCHLIST | 0/0/0 | PASS |
| NEAR | 5.2545 | 59.00 | 2.70 | 81.81 | BULLISH | Z 2.70 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.70 outside 0.2-1.8 window | NO SETUP BANNED friction | 0/0/0 | FAIL |
| SP500 | 7726.855 | 1.00 | 1.81 | 65.38 | BEARISH | FAIL |Z| 1.81 <2.0 | FAIL |Z| 1.81 outside 0.2-1.8 window | WATCHLIST | 104/51/4 | PASS |
| NAS100 | 29775.14 | 0.39 | 1.30 | 62.21 | BEARISH | FAIL |Z| 1.30 <2.0 | Z 1.30 within PASS regime BEARISH EMA20 29731.51 EMA50 29705.25 POC 29628.9246 R | WATCHLIST | 94/50/5 | PASS |
| DJ30 | 52119.3 | 0.25 | 1.66 | 66.25 | BULLISH | FAIL |Z| 1.66 <2.0 | Z 1.66 within PASS regime BULLISH EMA20 52031.08 EMA50 51896.74 POC 51416.1064 R | WATCHLIST | 0/0/0 | PASS |
| GER40 | 25399.65 | 0.43 | 2.53 | 67.56 | BULLISH | Z 2.53 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.53 outside 0.2-1.8 window | WATCHLIST | 0/0/0 | PASS |
| GOLD | 4154.68 | 0.19 | 0.86 | 52.96 | BULLISH | FAIL |Z| 0.86 <2.0 | Z 0.86 within PASS regime BULLISH EMA20 4151.39 EMA50 4148.50 POC 4156.8577 RSI  | NO SETUP | 56/29/0 | PASS |
| SILVER | 57.066 | 10.16 | 1.56 | 61.1 | BEARISH | FAIL |Z| 1.56 <2.0 | Z 1.56 within PASS regime BEARISH EMA20 56.89 EMA50 56.71 POC 56.6771 RSI 61.1 n | NO SETUP BANNED friction | 54/26/0 | FAIL |
| USWTI | 97.755 | 3.07 | 1.92 | 66.16 | BULLISH | FAIL |Z| 1.92 <2.0 | FAIL |Z| 1.92 outside 0.2-1.8 window | WATCHLIST | 37/1/0 | PASS |
| EURUSD | 1.1219 | 0.27 | 0.87 | 57.84 | BULLISH | FAIL |Z| 0.87 <2.0 | Z 0.87 within PASS regime BULLISH EMA20 1.12 EMA50 1.12 POC 1.1209 RSI 57.84 tow | NO SETUP | 10/9/0 | PASS |
| GBPUSD | 1.3277 | 0.08 | 2.93 | 67.2 | BULLISH | Z 2.93 PASS >=2.0 but BULLISH short BANNED per loss autopsy, long needs Z<=-2 FA | FAIL |Z| 2.93 outside 0.2-1.8 window | WATCHLIST | 10/7/0 | PASS |
| USDJPY | 158.0625 | 0.06 | 1.33 | 54.44 | RANGE_BOUND | FAIL RANGE_BOUND STAND ASIDE | FAIL RANGE_BOUND STAND ASIDE | NO SETUP RANGE_BOUND STAND ASIDE | 41/22/0 | PASS |

**Tally:** 0 CANDIDATES / WATCHLIST ~4-6 / 17-20 NO SETUP. No complete held-shelf + exhaustion + seasoned defense + bunker + net payoff >=2R.