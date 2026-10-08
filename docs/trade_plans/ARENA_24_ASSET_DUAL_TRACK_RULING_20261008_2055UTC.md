# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 20:55:40 UTC)

**Status:** advisory and dry-run. The desk executes. Nothing was placed or cancelled by the agent. No MT5 access.
**Trade authorization (telemetry):** `DENIED_UNVERIFIED_ORDERFLOW`.

## 0. Bottom line

1. **ZERO ADMITTED PUNCHES.** Capacity is frozen (max 2 per the 20:25 ruling). Telemetry at 20:41:20 shows 1 filled and 4 pending, which is over cap. The briefing's "one slot available" conflicts with telemetry and is not used.
2. **Even if the desk has deleted the three CFD BUY orders** (USWTI 18713408, SP500 18713432, XAUUSD 18713434), the count is ETH plus NERUSD = 2/2. No slot.
3. **Only one slot opens if NERUSD 18713247 is removed.** Then stage at most ONE of the two candidates below. Never both.
4. **Top 2 LIMIT stages (ready when a slot is free, after a fresh-tick re-check):**
   - **#1 LNKUSD.p SELL LIMIT 12.651.** Track 2. Stop 12.803, target 12.271 (2.50R). 0.70 lot. Nominal 10.65, stressed 15.33.
   - **#2 LTCUSD.pi SELL LIMIT 63.100.** Track 2, standby A. Stop 64.150, target 60.475 (2.50R). 0.10 lot. Nominal 10.50, stressed 15.12.
5. **ETH #18706769: HOLD.** Telemetry SL 2434.52 (Phase-1 lock). Briefing SL 2455.1. **Desk must confirm the live MT5 SL.** If it is 2455.1, the lock is not applied.
6. **NERUSD 18713247: KEEP** (drift under 2.0 ATR, ask band above 1.0M in the latest receipt). Sizing flag stands: 12.70 nominal, 18.29 stressed.
7. **Model 1 (|Z| at least 2.0 with RSI gate): zero candidates.** Telemetry max |Z| is 1.74 (GBPUSD).

## 1. Data-integrity flags (read before acting)

| Item | Briefing 20:55:40 | Telemetry (origin) | Action |
|---|---|---|---|
| Telemetry freshness | cites 60 s auto-sync | last commit **20:41:27 UTC**, about 14 min before briefing | Desk to restart the sync. Geometry below is from 20:41 data and needs a fresh tick |
| Capacity | "1 slot available", margin 0.00, "100% cash flat" | 1 filled, 4 pending, margin 446.04 | Briefing account block is internally inconsistent (ETH is open, so margin cannot be 0). Telemetry governs |
| ETH SL | 2455.1 (R 1.33) | 2434.52 (R 2.47) | Confirm in MT5 |
| ETH mark | 2469.8 | 2469.0 | Close enough |
| LINK mid | 12.6575 | 12.618 | Briefing mid is 0.04 higher and conflicts with its own 20:30 bar close (12.58). At 12.6575 the EMA50 shelf (12.651) is -0.07 ATR, below mid. Re-check on a fresh tick |
| LTC mid | 63.065 | 63.035 | At 63.065, entry 63.10 is +0.09 ATR, just below the 0.10 floor. Re-check |
| SP500 VWAP | 7770.32 | 7770.33 | Agree. Entry at VWAP is +0.26 ATR from briefing mid |
| 48H VAH/VAL | briefing profiles | `volume_profile` in telemetry | Different. Telemetry used for shelves |

## 2. Model 2 (trend-pullback) scan, all 24 assets

Geometry uses telemetry EMA20, EMA50, VWAP, and VAH/VAL, with offsets in ATR (positive = above mid). Only shelves inside 0.10 to 0.60 ATR on the trade side qualify.

**SELL in BEARISH regime (shelves above mid):**
- **LNKUSD.p:** EMA50 +0.33. **PASS geometry.** Track 2 depth: ask band 858k vs bid band 573k (ask-heavy 1.50x). Ask band 12/12 at or above 150k (min 386k). CVD last 5 min +24.6k (mildly counter). Spread 70 bps (passive, exempt). **CANDIDATE #1.**
- **LTCUSD.pi:** EMA50 +0.09 (just under band). Entry 63.10 = +0.16 ATR (telemetry). Ask band 12/12 (min 554k). **CANDIDATE #2** (standby A, unchanged).
- **BTCUSD.pi:** EMA50 81,873 = +0.31 ATR. Ask band **8/12** (fails 12/12). Depth bid-heavy 2.6x, CVD last 5 min +8.4M (counter). **NOT ADMITTED.** BTC 81,833 (+0.23 ATR) ask band 11/12, watch.
- **SP500.p:** VWAP 7770.33 = +0.28 ATR. Track 1 wick: the 20:15 bar high 7770.61 with close 7766.78 gives a 39% upper wick (PASS). **Volume gate not verifiable** (only 3 bars supplied). Regime weak (slope -0.04%). **WATCH, not admitted.**
- **USDJPY.pi:** EMA20 157.93 = +0.40 ATR. Last 15m bar upper wick only 11% (FAIL). Slope -0.02% (flat). **NOT ADMITTED.**
- **SOLUSD.p:** VAL is +0.20 ATR, but SOL is excluded by the standing cut-thesis ruling (see 20:25). **EXCLUDED.**
- **DOGUSD.p:** VWAP +0.17 ATR. Retired at 20:25. **RETIRED.** Note that 1 lot is the minimum, so risk per lot is about 9 USD at 1.5 ATR.
- **NERUSD.p:** live resting order (EMA20 +0.22 ATR). Held per §3.
- Others: no SELL shelf inside 0.10 to 0.60 ATR. Examples: BNB EMA50 +2.73; XRP VWAP +0.80; ADA EMA50 +1.52; BCH VAL -0.44; AVAX EMA50 +1.71; NAS100 EMA20 +0.02; TRX EMA20 0.00 (at mid).

**BUY in BULLISH regime (shelves below mid):**
- **XAUUSD.pi:** VAH -0.60 (boundary, telemetry VAH 4129.6). No 15m bar in the briefing touched 4129.6 (lows 4132.1 to 4134.2). Track 1 wick untested. **WATCH, not admitted.**
- **DJ30.p:** VAH -0.29 (telemetry VAH 51,217). The 20:30 bar low 51,214 printed a 13% wick (FAIL). **NOT ADMITTED.**
- **USWTI.p:** VAL -0.02 (too close to mid, outside band). **NO SETUP.** The 20:40 CFD BUY orders remain DELETE.
- **EURUSD.pi, GBPUSD.pi:** EMA20 -1.00 and -0.87 (outside band). **NO SETUP.**

## 3. Model 1 (extreme mean-reversion)

Telemetry |Z| values: GBPUSD 1.74, EURUSD 1.68, DJ30 1.51, GOLD 1.25, NEAR -1.21, NAS100 -0.96. **None reach 2.0.** Zero candidates.

## 4. Track 2 (crypto) persistence, last 12 receipts (ask band within ±0.5 ATR)

| Level | Min (kUSD) | Count at or above 150k | Verdict |
|---|---|---|---|
| LNK 12.651 | 386 | 12/12 | PASS |
| LTC 63.10 | 554 | 12/12 | PASS |
| BTC 81,873 | 0 | 8/12 | FAIL |
| BTC 81,833 | 115 | 11/12 | WATCH |
| NEAR 4.617 | 0 | 11/12 | Live, held |

## 5. Blueprints

Stop distance is at least 1.50 ATR. Target is 2.50R. Nominal risk must be 10 to 15 USD, and stressed (1.44x) should stay at or below 15.80 USD.

| Rank | Symbol | Side | Entry | Stop | Target | R | SL/ATR | Lot | Nominal | Stressed | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | LNKUSD.p | SELL LIMIT | 12.651 | 12.803 | 12.271 | 2.50 | 1.50 | 0.70 | 10.65 | 15.33 | Ready on a free slot, after fresh-tick re-check |
| 2 | LTCUSD.pi | SELL LIMIT | 63.100 | 64.150 | 60.475 | 2.50 | 2.64 | 0.10 | 10.50 | 15.12 | Standby A, ready on a free slot |
| (watch) | SP500.p | SELL LIMIT | 7770.33 | 7786.08 | 7730.96 | 2.50 | 1.50 | 0.07 | 11.02 | 15.87 | Volume gate unverified. Stressed above 15.80 by 0.07. 0.06 lot is 9.45 nominal, below 10 |

**Notes on the LINK blueprint:** the stop is set at the 1.50 ATR floor, which is the minimum allowed. It is not a structural level. The desk should check that 12.803 sits beyond the nearest visible ask wall before staging.

**Notes on the LTC blueprint:** at 1.50 ATR (63.697), LTC cannot satisfy both the 10 to 15 nominal and the 15.80 stressed caps. The standby uses the structural stop at 64.15 (2.64 ATR), which satisfies both.

## 6. Governance

- **Capacity:** frozen. Zero new punches until a slot is free. Only one candidate may be staged at a time.
- **Pending orders:** the three CFD BUY orders (USWTI 18713408, SP500 18713432, XAUUSD 18713434) remain DELETE per the 20:40 ruling. The briefing shows them gone. Desk to confirm in MT5.
- **NERUSD 18713247:** KEEP. Sizing flag open (desk decision).
- **ETH 18706769:** HOLD. Confirm SL. If MT5 shows 2455.1, the Phase-1 lock at 2434.52 is not in place. That is a desk decision.
- **Retired / excluded:** DOGE 0.0840 (retired 20:25). SOL 109.10 SELL (excluded). BTC 81,833 watch only.

## 7. Caveats

- Telemetry is about 14 minutes old. Re-run geometry on a fresh tick before any punch.
- The briefing's account block is internally inconsistent (margin 0 with ETH open). Not used.
- Track 2 depth uses the telemetry snapshot. Persistence uses the last 12 telemetry receipts, not the briefing's orderbook (which is N/A).
- Track 1 volume gate cannot be verified from the 3-bar CFD data supplied.
