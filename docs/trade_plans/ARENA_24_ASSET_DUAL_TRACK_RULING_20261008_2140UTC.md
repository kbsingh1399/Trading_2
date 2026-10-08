# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 21:40:15 UTC)

**Status:** advisory and dry-run. The desk executes. Nothing was placed or cancelled by the agent. No MT5 access.
**Telemetry:** origin fresh at **21:40:20 UTC** (last 12 receipts through 21:40). Used for geometry, depth, persistence, and capacity.

## 0. Bottom line

1. **Account flat.** 0 positions, 0 pending, equity 4,845.80, free margin 4,845.80. Telemetry capacity `max_concurrent=12`, dynamic. Capacity is not binding.
2. **No candidate is admissible.** Three reasons:
   - **TP anchor missing.** Telemetry reports `UNAVAILABLE` for stops and liquidations on every asset. Sampled L2 walls are not persistent (the 180 s rule). The operator rule forbids TP into empty air.
   - **Only one shelf in band:** AVAXUSD EMA20 at +0.13 ATR. Its flow now works against a short (see §2).
   - **Zero Model 1 candidates.** Max |Z| is 1.68 (GBPUSD), below 2.0.
3. **Recommendation: stand aside.**

## 1. Changes since 21:25

| Asset | 21:25 | 21:40 | Result |
|---|---|---|---|
| LTC | EMA50 +0.23 ATR (entry 63.05) | EMA50 -0.20 ATR (below mid) | Shelf lost. **Out.** |
| AVAX | EMA20 +0.23 ATR, ask-heavy 1.72x (supportive) | EMA20 +0.13 ATR, **bid-heavy 1.50x** and CVD +294k over 5 bars | Shelf still in band. Flow reversed. **Not admitted** |
| LINK | EMA50 at mid | EMA50 -0.55 ATR | **Out** |
| BTC | VAL +0.11 ATR, 10/12 | VAL -0.08 ATR (below mid) | **Out** |
| USDJPY | VAL +0.57 ATR | VAL +0.68 ATR (beyond band) | **Out** |

## 2. Scan result

**SELL, BEARISH, shelf 0.10 to 0.60 ATR above mid:**
- **AVAXUSD (EMA20 10.101, +0.13 ATR):** ask band at 10.101 is **12/12** at or above 150k (min 168k). But the band is bid-heavy 1.50x (bid 301k, ask 201k), and the last five 1m bars sum to CVD +294k (buying). **Flow works against the short. Not admitted.** Watch if the book flips.
- **SOLUSD (EMA50 +0.34):** excluded by the standing cut-thesis ruling.
- **DOGE (VWAP +0.20):** retired at 20:25.
- **SP500 (VWAP +0.05), SILVER (VWAP +0.60, untested), NEAR (EMA20 +0.79), ETH (EMA50 +0.63), BCH, XRP, BNB, ADA, TRX, DOT, NAS100:** no shelf in band, or outside it.

**BUY, BULLISH, shelf 0.10 to 0.60 ATR below mid:**
- **DJ30 (VAH -0.14):** 21:00 bar low 51,214 closed at 51,220, giving a 13% wick (30% needed). **Not admitted.**
- **GOLD (VAH -0.64):** outside band.
- **EURUSD, GBPUSD, USWTI:** no BUY shelf in band.

**Model 1:** zero candidates.

## 3. Sizing reference (AVAX, not staged)

If the desk overrides the flow and TP rules: entry 10.101, stop 10.230 (1.5 ATR), TP 9.777 (2.5R, unanchored; VAL 9.74 sits just beyond). Lot 0.80: nominal 10.36, stressed 14.91. Not recommended.

## 4. Governance

- **Pending orders:** none. No agent staging.
- **ETH:** closed (telemetry shows 0 positions).
- **Retired / excluded:** DOGE, SOL.
- **Next re-check:** telemetry at the next briefing. Admit only if (a) the TP anchor data is restored or the desk overrides it, (b) AVAX flow flips to ask-heavy, and (c) its ask band stays 12/12.
