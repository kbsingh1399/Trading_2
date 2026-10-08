# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 21:25:18 UTC)

**Status:** advisory and dry-run. The desk executes. Nothing was placed or cancelled by the agent. No MT5 access.
**Telemetry:** origin fresh at **21:25:20 UTC** (last 12 receipts through 21:25). Used for geometry, depth, persistence, and capacity.
**Trade authorization (telemetry):** `DENIED_UNVERIFIED_ORDERFLOW`.

## 0. Bottom line

1. **Account flat.** 0 positions, 0 pending, balance and equity 4,845.80, free margin 4,845.80. Telemetry capacity is `max_concurrent=12` (dynamic, free-margin based). Capacity is not the binding constraint. ETH is closed (the balance change matches an exit near 2,455).
2. **Candidates that pass geometry and Track 2 flow: one admitted, one on watch.**
   - **LTCUSD.pi SELL LIMIT 63.050** (EMA50 retest, +0.23 ATR). **Admitted on entry gates. TP anchor missing.**
   - **AVAXUSD SELL LIMIT 10.105** (EMA20 retest, +0.23 ATR). **Watch.** Persistence 11/12 at this price, below the 12/12 standard.
3. **The operator TP mandate blocks both.** TP must anchor to a verified liquidation cascade or stop sweep. Telemetry reports `UNAVAILABLE` for stops and liquidations on every asset. Sampled L2 walls are not persistent (the 180 s rule). For LTC the 2.5R target (61.690) sits between the POC (62.14) and VAL (60.82), in empty air. **No stage is admissible under the mandate today.**
4. **Recommendation: stand aside.** A punch with an unanchored TP breaks the operator rule. If the desk overrides, LTC is the only setup that passes the entry gates, at 0.20 lot. Both the override and the lot need explicit desk sign-off.
5. **Model 1: zero candidates.** Max |Z| is 1.66 (GBPUSD, below 2.0). NEARUSD is at Z -1.41 with RSI 37.7, but it is not at a shelf.

## 1. Discrepancies

| Item | Briefing 21:25 | Telemetry 21:25:20 | Used |
|---|---|---|---|
| LTC mid | 63.040 | 62.965 | Telemetry |
| ATR (LTC) | 0.3627 | 0.3627 | Agree |
| Capacity | "no artificial cap" | max 12, 0 filled, 0 pending | Agree |
| NEARUSD | no pending | no pending | Agree. Original 4.617 order is gone |

## 2. Scan result (all 24 assets, telemetry 21:25)

**SELL in BEARISH regime (shelf 0.10 to 0.60 ATR above mid):**
- **LTCUSD.pi:** EMA50 63.048 = +0.23 ATR. Ask band at 63.05 is 12/12 at or above 150k (min 314k). Imbalance is bid-heavy 1.34x (against). CVD last 5 bars -7.1k (supportive). **Passes entry gates.**
- **AVAXUSD:** EMA20 10.105 = +0.23 ATR. Ask-heavy 1.72x (supportive). CVD -6.9k (supportive). Ask band at 10.105 is **11/12** (min 106k). **Watch.** At 10.125 (+0.45 ATR, off the shelf) it was 12/12, but that is not the shelf.
- **BTCUSD.pi:** VAL 81,635 = +0.11 ATR. Ask band 10/12 (min 46k). Bid-heavy 2.2x (against). CVD -4.3M (supportive). L2 wall at 81,634 is sampled only, not persistent. **Not admitted.**
- **LNKUSD.p:** EMA50 at mid (-0.04). **Out of band.**
- **SP500.p:** VWAP +0.05. Below the 0.10 floor. **Out.**
- **USDJPY.pi:** VAL 157.91 = +0.57 ATR. 15m upper wicks 20% and 25% (below 30%). **Not admitted.**
- **SILVER:** VWAP +0.60 (boundary). Never tested in the last 3 bars. **Not admitted.**
- **NERUSD.p:** EMA20 +1.23. **Out.**
- **Others:** no shelf inside 0.10 to 0.60 ATR.

**BUY in BULLISH regime (shelf 0.10 to 0.60 ATR below mid):**
- **DJ30.p:** VAH 51,217.7 = -0.14 ATR. The 21:00 bar low of 51,214 closed at 51,220, giving a 13% wick (30% needed). **Not admitted.**
- **GOLD:** VAH -0.64. **Out.**
- **USWTI, EURUSD, GBPUSD:** no BUY shelf in band.

**Excluded by standing rules:** SOL (cut thesis), DOGE (retired 20:25).

## 3. Blueprints (desk override required for TP)

| Rank | Symbol | Side | Entry | Stop (1.5 ATR) | TP (2.5R) | Lot | Nominal | Stressed (1.44x) | TP anchor |
|---|---|---|---|---|---|---|---|---|---|
| 1 | LTCUSD.pi | SELL LIMIT | 63.050 | 63.594 | 61.690 | 0.20 | 10.88 | 15.67 | **Missing.** Between POC 62.14 and VAL 60.82 |
| (watch) | AVAXUSD | SELL LIMIT | 10.105 | 10.238 | 9.774 | 0.80 | 10.60 | 15.26 | **Missing.** VAL at about 10.10 (touching entry), no structure below |

LTC: broker contract size 100 units per lot (telemetry execution_specs), min lot 0.10, step 0.10. Stop distance 0.544. Nominal risk 10.88 at 0.20 lot.

## 4. Joint stress

If both fill and both stop out at stressed values: 4,845.80 - 15.67 - 15.26 = **4,814.87**. That is 19.87 above the 4,795 buffer, and 39.87 above the 4,775 floor. Nominal worst case: 4,824.32. Both are short alt-coin positions and are correlated.

## 5. Desk decision needed

- **Hold.** Recommended. No candidate meets the TP rule.
- **Override and stage LTC 63.050 at 0.20 lot.** Requires explicit sign-off on the unanchored TP.
- **AVAX:** watch only until 12/12 persistence at 10.105.

## 6. Governance

- **Pending orders:** none. No agent staging.
- **NERUSD:** no pending order in telemetry (21:25:20). The 4.617 order is no longer resting. Cause not verified.
- **ETH:** closed. Confirmed by telemetry (0 positions).
- **Retired / excluded:** DOGE, SOL.

## 7. Caveats

- Telemetry is fresh (21:25:20). Depth and persistence are measured through 21:25 only.
- CFD 15m bars are supplied in the briefing only. Track 1 volume and wick gates cannot be fully verified.
- Volume-profile VAL and POC are derived from MT5 bar volume, which is a proxy for exchange volume.
