# Arena Council Dual-Track Ruling: 24-Asset Scan (briefing 2026-10-08 20:40:10 UTC)

**Telemetry basis:** `docs/telemetry/live_snapshot_latest.json`, as_of 2026-10-08 20:40:20 UTC (read from origin).
**Trade authorization in telemetry:** `DENIED_UNVERIFIED_ORDERFLOW`.
**Status:** advisory and dry-run. The desk executes. Nothing was placed or cancelled by the agent. No MT5 access.

## 0. Bottom line

1. **CAPACITY OVER CAP.** Telemetry shows 1 filled (ETH #18706769) and 4 pending. Max concurrent is 2. The status string reads OPEN, which contradicts the 20:25 FROZEN ruling. **Zero new punches.**
2. **Advise DELETE for three pending BUY_LIMIT orders.** They were placed after the 20:25 freeze, are absent from every ruling, and fail the geometry and the 1.5 ATR SL floor:
   - **18713408 USWTI.p BUY_LIMIT 0.2 @ 91.72** (SL 91.22, TP 93.00, placed 20:28:34). Entry is -0.56 ATR from mid, outside the 0.10 to 0.60 band. Not at EMA20 (92.60) or VWAP (92.61). SL is 1.19 ATR, below the 1.50 floor.
   - **18713432 SP500.p BUY_LIMIT 0.1 @ 7758.0** (SL 7748.0, TP 7783.0, placed 20:31:23). Entry is -0.90 ATR, outside the band. Not at EMA20 (7762.07) or VWAP (7770.33). SL is 0.95 ATR, below the floor.
   - **18713434 XAUUSD.pi BUY_LIMIT 0.01 @ 4124.0** (SL 4114.0, TP 4149.0, placed 20:31:41). Entry is -1.48 ATR, outside the band. Not at EMA20 (4128.44) or VWAP (4125.10). SL is 1.48 ATR, below the floor.
3. **KEEP 18713247 NERUSD.p SELL_LIMIT 1.0 @ 4.617** (20:25 ruling). Mid is 4.581, drift +0.46 ATR, under the 2.0 ATR trigger. **Desk sizing decision open:** 12.70 nominal and 18.29 stressed, both above the §2 cap.
4. **After the three deletes, capacity is 2/2** (ETH plus NERUSD), which is compliant.
5. **ETH #18706769 LONG 0.37 @ 2411.0: HOLD.** Mark 2467.9, floating +21.05 USD, telemetry R 2.42, SL 2434.52 (PHASE_1_PROFIT_LOCKED), TP 2484.5.
6. **Standby A: LTCUSD.pi SELL LIMIT 63.100**, SL 64.150, TP 60.475, 0.10 lot, risk 10.50 USD, stressed 15.12. Still in band (mid 63.015, +0.21 ATR). Persistence 12/12 at the 63.10 ask band (min 554k). **Standby only. Stage only after capacity clears.** Expires 21:58 UTC.
7. **Standby B: BTCUSD.pi SELL LIMIT 81,833 is downgraded to WATCH.** Mid 81,755 (+0.23 ATR, still in band). Persistence is 11/12 this cycle (one receipt at 115k), below the 12/12 standard. Never hold A and B together.
8. **Model 1: zero candidates** (no |Z| of 2.0 or more with its RSI gate).
9. **Briefing §2 and §4 are stale.** Telemetry governs. Equity 4,850.84 USD, balance 4,829.79 USD. The 4,813.99 figure is not used.

## 1. Account state (telemetry 20:40:20 UTC)

| Field | Value |
|---|---|
| Balance / Equity | 4,829.79 / 4,850.84 USD |
| Margin used | 446.04 USD |
| Hard floor / cushion | 4,775.00 USD / +75.84 USD |
| Buffer threshold / headroom | 4,795.00 USD / +55.84 USD |
| Capacity | 1 filled, 4 pending. **Over cap (max 2).** |

**If NERUSD fills and stops at 4.744:** 4,825.79 USD equity (stressed 4,820.20 USD). Both above the 4,795 buffer, but the stressed case uses the 18.29 sizing above the cap, which is the desk sizing decision.

## 2. Position and orders

### 2.1 ETH #18706769 (LONG 0.37 @ 2411.0)

Mark 2467.9, floating +21.05 USD, telemetry R 2.42, SL 2434.52 (locked), TP 2484.5. **Ruling: HOLD.**

### 2.2 Resting orders

| Ticket | Symbol | Side | Price | SL | TP | Placed (UTC) | Ruling |
|---|---|---|---|---|---|---|---|
| 18713247 | NERUSD.p | SELL_LIMIT 1.0 | 4.617 | 4.744 | 4.299 | 20:15 | **KEEP** (20:25 ruling). Drift +0.46 ATR, under 2.0. Sizing flagged: 12.70 nominal, 18.29 stressed |
| 18713408 | USWTI.p | BUY_LIMIT 0.2 | 91.72 | 91.22 | 93.00 | 20:28:34 | **DELETE.** -0.56 ATR, no EMA or VWAP shelf, SL 1.19 ATR |
| 18713432 | SP500.p | BUY_LIMIT 0.1 | 7758.0 | 7748.0 | 7783.0 | 20:31:23 | **DELETE.** -0.90 ATR, no shelf, SL 0.95 ATR |
| 18713434 | XAUUSD.pi | BUY_LIMIT 0.01 | 4124.0 | 4114.0 | 4149.0 | 20:31:41 | **DELETE.** -1.48 ATR, no shelf, SL 1.48 ATR |

The agent cannot cancel MT5 orders. The desk must delete the three tickets above and confirm who placed them.

## 3. Scan summary (24 assets)

- **Model 2 (trend pullback):** LTC A is the only admissible setup. BTC is on watch. NERUSD is already live.
- **Model 1 (|Z| at least 2.0):** zero candidates.
- **Crypto long candidates:** none in the scan. The trend regime is BEARISH across crypto.
- **CFD BUY candidates:** the three new orders above all fail. No other CFD BUY passed the Track 1 geometry.
- The per-asset table from earlier cycles is not restated here. Consult the 20:25 ruling and the standby JSON.

## 4. Blueprints

No blueprint may be punched while capacity is 2/2 or over. The only admissible standby is LTC A.

| Rank | Symbol | Direction | Entry | SL | TP | R | SL/ATR | Lot | Risk (USD) | Stressed (USD) | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | LTCUSD.pi | SELL LIMIT | 63.100 | 64.150 | 60.475 | 2.50 | 2.64 | 0.10 | 10.50 | 15.12 | Standby, frozen |
| (watch) | BTCUSD.pi | SELL LIMIT | 81,833 | 82,370 | 80,490.5 | 2.50 | 1.58 | 0.02 | 10.74 | 15.47 | Watch (11/12) |

Stage file: `docs/trade_plans/ARENA_LIMIT_STAGES_20261008_2040_STANDBY.json` (LTC A only, validated PASS in-process, not staged).

## 5. Governance

- **Capacity:** 1 filled + 4 pending, over max of 2. Delete USWTI 18713408, SP500 18713432, XAUUSD 18713434. Then 2/2 with NERUSD. **Zero new punches** until ETH or NERUSD clears.
- **NERUSD sizing exception:** expanded-only 12.70 nominal, 18.29 stressed, above the 15.80 cap. Desk decision.
- **Resting-order rule for 18713247:** DELETE triggers if the ask band thins by more than 50% or drift exceeds 2.0 ATR. Neither has occurred.
- **Retired:** DOGE 0.0840 (20:25). Do not re-enter SOL 109.10 SELL.

## 6. Open items

1. Desk: DELETE 18713408, 18713432, 18713434. Confirm who placed them.
2. Desk: NERUSD 18713247 sizing decision.
3. Next refresh: re-check telemetry capacity before any staging. LTC A stages only if capacity clears and it is still in band before 21:58 UTC.

## 7. Caveats

- The status string OPEN contradicts the 4-pending count. Verify MT5 directly.
- Causal indicators may be about 13 minutes old. Quotes are fresh.
- `scripts/arena_dual_track_scan_v2.py` hard-codes 4,813.99 USD equity and was not used.
