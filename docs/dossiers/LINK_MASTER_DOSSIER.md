# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 16:24:41 IST` (`2026-10-30 10:54:41 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.03` | **Live Ask Quote**: `11.12` | **Mid Price**: `11.08`
- **Spread Points**: `85.00` | **Spread BPS**: `76.75 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `11.08` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `11.15` | Lower -3.00σ Band: `11.00`
  * Upper +2.51σ Band: `11.14` | Lower -2.51σ Band: `11.01`
  * Upper +2.01σ Band: `11.12` | Lower -2.01σ Band: `11.03`
  * Upper +2.00σ Band: `11.12` | Lower -2.00σ Band: `11.03`
  * Upper +1.28σ Band: `11.11` | Lower -1.28σ Band: `11.04`
  * Upper +1.00σ Band: `11.10` | Lower -1.00σ Band: `11.05`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.08` | EMA-20=`11.08` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.08` (Slope: `+0.0000`) | EMA-100=`11.08`
  * Institutional Anchors: EMA-144=`11.08` | EMA-200=`11.08` (Slope: `+0.0000`) | EMA-233=`11.08`
- **Range Boundaries**: 24H High=`11.19` | 24H Low=`10.96` | Weekly High=`11.30` | Weekly Low=`10.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.12` (Distance: `-0.33%`)
  * Point of Control (POC) = `10.96` (Distance: `+1.12%`)
  * Value Area Low (VAL) = `10.56` (Distance: `+4.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.79` | Weekly POC=`11.43` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.20`
  * London Session (08:00-16:00 UTC): High=`11.12` | Low=`10.89`
  * New York Session (13:00-21:00 UTC): High=`11.04` | Low=`10.93`
  * Initial Balance (First Hour): IB High=`11.09` | IB Low=`10.98`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.03` - `11.12`
  * Optimal Trade Entry (OTE 0.705): `11.10`
  * Structural Invalidation Anchor (0.786): `11.16`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `11.06` | `11.10` | `11.06` | `11.08` | `101,792` | 1,127,422.47 USD | 249,999.97 USD | `+22.17%` | -12,331,154.98 USD | `+2.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `11.08` | `11.09` | `11.05` | `11.08` | `22,786` | 252,239.35 USD | 12,321.32 USD | `+4.88%` | -12,318,833.66 USD | `+0.04` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `11.08` | `11.10` | `11.07` | `11.10` | `15,994` | 177,212.50 USD | 25,759.22 USD | `+14.54%` | -12,293,074.44 USD | `+0.15` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `10.99` | `11.06` | `10.98` | `11.02` | `87,422` | 963,211.20 USD | -51,730.34 USD | `-5.37%` | -12,827,818.91 USD | `-0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.02` | `11.10` | `11.01` | `11.08` | `332,021` | 3,673,451.57 USD | 555,106.73 USD | `+15.11%` | -12,272,712.18 USD | `+2.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.08` | `11.10` | `11.05` | `11.10` | `38,780` | 429,451.85 USD | 38,080.54 USD | `+8.87%` | -12,234,631.64 USD | `+0.12` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `11.04` | `11.11` | `10.99` | `11.01` | `546,831` | 6,037,228.26 USD | -347,696.97 USD | `-5.76%` | -12,182,060.85 USD | `+0.13` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `11.01` | `11.05` | `10.95` | `11.04` | `483,549` | 5,317,760.14 USD | -566,832.14 USD | `-10.66%` | -12,748,892.99 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.04` | `11.10` | `10.98` | `11.10` | `554,108` | 6,122,310.18 USD | 514,261.35 USD | `+8.40%` | -12,234,631.64 USD | `+0.54` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.10` | `1,582,691` | 17,457,346.88 USD | -407,258.45 USD | `-2.33%` | -12,282,363.73 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | 302,518.65 USD | `-1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.53` | `10.61` | `14,153,054` | 154,763,662.73 USD | -14,517,238.98 USD | `-9.38%` | -14,214,720.33 USD | `-1.40` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `10.61` | `10.98` | `10.25` | `10.96` | `7,670,898` | 80,878,558.69 USD | 1,692,510.64 USD | `+2.09%` | -12,522,209.69 USD | `+0.72` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `10.96` | `11.18` | `10.90` | `11.04` | `2,966,092` | 32,817,562.84 USD | 647,104.40 USD | `+1.97%` | -11,875,105.29 USD | `+0.49` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.04` | `11.11` | `10.95` | `11.10` | `1,582,691` | 17,457,346.88 USD | -407,258.45 USD | `-2.33%` | -12,282,363.73 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |

- **Deribit Institutional Options Max Pain & Volatility Surface (21_Tradfye_Orderflow.parquet)**:
  * Options Max Pain Price: `0.000000`
  * Call Wall Strike: `0.000000` | Put Wall Strike: `0.000000`

---

## 5. Institutional Whale Armor, Hyperdash Intel & L2 Depth Ladders
*(Sources: 10_Whale_Orders.parquet, 17_Orderbook.parquet, 12_Hyperdash.parquet, 13_Hyperliquid.parquet, 4_Hyperliquid_Analysis.parquet, 16_Hyperdash_telegram_Intel.parquet)*
- **Defending Resting Whale Walls (10_Whale_Orders.parquet)**:
  * Top Defending Bid Wall: `None` (Unarmored)
  * Top Defending Ask Wall: `None` (Unarmored)
| Side | Wall Price (USD) | Size (Coins) | Depth (USD) | Distance (%) | Persistence | Traded % | Venue | Order ID |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| --- | **`11.08`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `422` | `0xecb6...2b00` | `SHORT` | 5,249,955.65 USD | `473,737,200.00` | `10.66` | `11.08` | `75.93` | -200,555.54 USD | `-3.82%` | `10X Cross` |
| `506` | `0x73ce...8ce9` | `LONG` | 4,430,328.48 USD | `400,011,600.00` | `12.05` | `11.08` | `7.82` | -389,425.23 USD | `-8.79%` | `5X Cross` |
| `838` | `0xb83d...6e36` | `SHORT` | 2,684,650.21 USD | `242,013,000.00` | `12.93` | `11.08` | `426.13` | 445,243.98 USD | `+16.58%` | `3X Cross` |
| `884` | `0x458d...ab3b` | `LONG` | 2,515,987.61 USD | `227,156,700.00` | `13.13` | `11.08` | `9.34` | -466,242.79 USD | `-18.53%` | `3X Isolated` |
| `967` | `0xdd53...2b13` | `SHORT` | 2,288,365.75 USD | `206,475,300.00` | `11.92` | `11.08` | `295.90` | 172,857.18 USD | `+7.55%` | `3X Cross` |
| `990` | `0x3dc9...54b0` | `SHORT` | 2,217,400.00 USD | `200,000,000.00` | `7.56` | `11.08` | `93.18` | -706,241.58 USD | `-31.85%` | `10X Cross` |
| `1003` | `0x45d2...4029` | `SHORT` | 2,166,531.00 USD | `195,500,000.00` | `11.54` | `11.08` | `216.66` | 89,952.43 USD | `+4.15%` | `10X Cross` |
| `1190` | `0x6540...f7b7` | `LONG` | 1,855,340.75 USD | `167,404,200.00` | `12.40` | `11.08` | `6.70` | -220,465.36 USD | `-11.88%` | `5X Isolated` |
| `1260` | `0xeadc...9d55` | `LONG` | 1,742,019.11 USD | `157,691,600.00` | `9.43` | `11.08` | `0.000000` | 255,364.20 USD | `+14.66%` | `10X Cross` |
| `1463` | `0x5b5d...c060` | `SHORT` | 1,459,281.89 USD | `131,775,500.00` | `13.61` | `11.08` | `1085.41` | 333,976.08 USD | `+22.89%` | `3X Cross` |
| `1645` | `0xf6f3...47f8` | `SHORT` | 1,275,277.74 USD | `115,024,600.00` | `11.42` | `11.08` | `18.21` | 38,052.45 USD | `+2.98%` | `5X Cross` |
| `1839` | `0xfe7e...11b4` | `LONG` | 1,120,956.79 USD | `101,142,000.00` | `14.47` | `11.08` | `5.33` | -342,156.36 USD | `-30.52%` | `5X Isolated` |
| `1871` | `0x8af7...fa05` | `SHORT` | 1,093,462.08 USD | `98,661,200.00` | `14.08` | `11.08` | `201.37` | 295,720.46 USD | `+27.04%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.76 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.6000 USD [API] | `2026-10-29 12:19:39` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,643.29 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.64K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.60` | 5,464.72 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.5950 USD [API] | `2026-10-29 12:22:16` |
| `ANNOUNCEMENT` | `INFO` | `11.68` | 6,290.94 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.29K USD at 11.6780 USD [API] | `2026-10-29 13:02:36` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,599.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:46` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 5,597.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.60K USD at 11.6690 USD [API] | `2026-10-29 13:23:45` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 6,665.64 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 6.67K USD at 11.6410 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.64` | 7,507.80 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Short: 7.51K USD at 11.6400 USD [API] | `2026-10-29 13:32:47` |
| `ANNOUNCEMENT` | `INFO` | `11.27` | 23.67 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.02K USD at 11.2730 USD [API] | `2026-09-13 09:25:11` |
| `ANNOUNCEMENT` | `INFO` | `11.63` | 227.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.23K USD at 11.6300 USD [API] | `2026-09-09 22:09:04` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 63.68 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.06K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `12.02` | 12.02 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 0.01K USD at 12.0150 USD [API] | `2026-10-29 16:09:26` |
| `ANNOUNCEMENT` | `INFO` | `11.83` | 5,469.27 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 5.47K USD at 11.8280 USD [API] | `2026-10-29 17:21:54` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 6,883.73 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 6.88K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.71` | 8,500.40 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 8.50K USD at 11.7150 USD [API] | `2026-10-29 18:02:14` |
| `ANNOUNCEMENT` | `INFO` | `11.67` | 10,014.95 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 10.01K USD at 11.6670 USD [API] | `2026-10-29 19:26:32` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 6,067.82 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.07K USD at 11.7230 USD [API] | `2026-10-29 19:32:49` |
| `ANNOUNCEMENT` | `INFO` | `11.72` | 5,463.85 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale SELL: 5.46K USD at 11.7250 USD [API] | `2026-10-29 19:36:14` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.23` (Vol: 486,800.00 USD, Dist: `+1.46%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.85%`)
  * 48H Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.45%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.86%`)
  * 3D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.45%`) | Long MP=`10.31` (Vol: 866,700.00 USD, Dist: `--6.86%`)
  * 7D Horizon: Short MP=`11.22` (Vol: 486,800.00 USD, Dist: `+1.36%`) | Long MP=`10.30` (Vol: 866,700.00 USD, Dist: `--6.90%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.25` | 1,720.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 50,730.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.55` | 1,030.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 6,130.00 USD | 12,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 28,270.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 7,490.00 USD | 12,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 1,430.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.25` | 445.25 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 1,970.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,030.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 126.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,190.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 250.25 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.95` | 4,420.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 950.54 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.15` | 412.51 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 20,850.00 USD | 12,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 5,600.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 1,050.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.55` | 7,280.00 USD | 12,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 17,600.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 366,620.00 USD | 12,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 2,070.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 6,080.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 217.66 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.15` | 262.13 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 5,020.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 543,950.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 2,600.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 9,670.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,770.00 USD | 11,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 18,750.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 6,010.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 10,260.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 13,590.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 489.54 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 29,010.00 USD | 11,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 54,590.00 USD | 11,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,910.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 1,130,000.00 USD | 10,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 24,870.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 5,060.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 79,160.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 690,270.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 32,340.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 7,160.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 20,090.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 40,720.00 USD | 9,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 173,010.00 USD | 8,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 1,830.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 19,300.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,150,000.00 USD | 8,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 17,480.00 USD | 5,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 99,930.00 USD | 5,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 45,950.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 32,110.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 6,370.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 520,270.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 58,710.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,270.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 17,890.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 60,320.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 458,450.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 105,400.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 76,640.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 19,930.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.32` | 13,510,000.00 USD | 13,510,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.34` | 13,430,000.00 USD | 13,430,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.36` | 13,390,000.00 USD | 13,390,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.38` | 13,380,000.00 USD | 13,380,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.40` | 13,350,000.00 USD | 13,350,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.42` | 13,310,000.00 USD | 13,310,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.44` | 13,270,000.00 USD | 13,270,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.45` | 55,700.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.46` | 13,210,000.00 USD | 13,210,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.48` | 13,120,000.00 USD | 13,120,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.50` | 13,110,000.00 USD | 13,110,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.52` | 13,050,000.00 USD | 13,050,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.54` | 13,050,000.00 USD | 13,050,000.00 USD | 136.92 USD | 12,570.00 USD | 10.22 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.55` | 103,520.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.56` | 13,040,000.00 USD | 13,040,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.58` | 12,950,000.00 USD | 12,950,000.00 USD | 38,760.00 USD | 722.15 USD | 20.74 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.60` | 12,910,000.00 USD | 12,910,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.62` | 12,710,000.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 212.33 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.64` | 12,710,000.00 USD | 12,710,000.00 USD | 8,500.00 USD | 2,560.00 USD | 6,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.65` | 202,670.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.66` | 12,690,000.00 USD | 12,690,000.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.68` | 12,680,000.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.70` | 12,650,000.00 USD | 12,650,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.72` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.74` | 12,620,000.00 USD | 12,620,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 85,410.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.76` | 12,610,000.00 USD | 12,610,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.78` | 12,540,000.00 USD | 12,540,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.80` | 12,540,000.00 USD | 12,540,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.82` | 12,450,000.00 USD | 12,450,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.84` | 12,350,000.00 USD | 12,350,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 30,620.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 9,010,000.00 USD | 9,010,000.00 USD | 29,590.00 USD | 11,010.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.86` | 12,290,000.00 USD | 12,290,000.00 USD | 5,390.00 USD | 14,570.00 USD | 118.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.88` | 8,950,000.00 USD | 8,950,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.88` | 12,270,000.00 USD | 12,270,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 8,930,000.00 USD | 8,930,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.90` | 12,240,000.00 USD | 12,240,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 8,840,000.00 USD | 8,840,000.00 USD | 23,540.00 USD | 20,070.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.92` | 12,190,000.00 USD | 12,190,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 8,800,000.00 USD | 8,800,000.00 USD | 1,960.00 USD | 5,150.00 USD | 101.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.94` | 12,180,000.00 USD | 12,180,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 433,320.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 8,790,000.00 USD | 8,790,000.00 USD | 75,160.00 USD | 15,490.00 USD | 26,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.96` | 12,080,000.00 USD | 12,080,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 8,670,000.00 USD | 8,670,000.00 USD | 37,260.00 USD | 6,830.00 USD | 68,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.98` | 12,040,000.00 USD | 12,040,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 8,560,000.00 USD | 8,560,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.00` | 11,970,000.00 USD | 11,970,000.00 USD | 0.00 USD | 7,630.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.02` | 8,490,000.00 USD | 8,490,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.02` | 11,950,000.00 USD | 11,950,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 8,440,000.00 USD | 8,440,000.00 USD | 18,000.00 USD | 1,900.00 USD | 264.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.04` | 11,940,000.00 USD | 11,940,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 774,770.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 8,420,000.00 USD | 8,420,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.06` | 11,930,000.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.08` | 8,350,000.00 USD | 8,350,000.00 USD | 167,250.00 USD | 701.42 USD | 76,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.08` | 11,850,000.00 USD | 11,850,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.10` | 8,100,000.00 USD | 8,100,000.00 USD | 7,570.00 USD | 42,810.00 USD | 288.89 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.10` | 11,520,000.00 USD | 11,520,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 8,050,000.00 USD | 8,050,000.00 USD | 1,150.00 USD | 20,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.12` | 11,510,000.00 USD | 11,510,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 8,030,000.00 USD | 8,030,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.14` | 11,450,000.00 USD | 11,450,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 69,470.00 USD | 251,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 7,970,000.00 USD | 7,970,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.16` | 11,130,000.00 USD | 11,130,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 7,850,000.00 USD | 7,850,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.18` | 11,080,000.00 USD | 11,080,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 7,570,000.00 USD | 7,570,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.20` | 10,950,000.00 USD | 10,950,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 7,100,000.00 USD | 7,100,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.22` | 10,430,000.00 USD | 10,430,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 6,700,000.00 USD | 6,700,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.24` | 9,880,000.00 USD | 9,880,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 32,460.00 USD | 182,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 6,500,000.00 USD | 6,500,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.26` | 9,440,000.00 USD | 9,440,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 6,330,000.00 USD | 6,330,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.28` | 9,060,000.00 USD | 9,060,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 5,990,000.00 USD | 5,990,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.30` | 8,720,000.00 USD | 8,720,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 5,760,000.00 USD | 5,760,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.32` | 8,260,000.00 USD | 8,260,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 5,670,000.00 USD | 5,670,000.00 USD | 66,010.00 USD | 9,100.00 USD | 86,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.34` | 8,120,000.00 USD | 8,120,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 140,250.00 USD | 149,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 5,510,000.00 USD | 5,510,000.00 USD | 5,630.00 USD | 3,580.00 USD | 39.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.36` | 8,060,000.00 USD | 8,060,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 5,500,000.00 USD | 5,500,000.00 USD | 41,250.00 USD | 45,170.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.38` | 7,660,000.00 USD | 7,660,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 5,410,000.00 USD | 5,410,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.40` | 7,660,000.00 USD | 7,660,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 5,220,000.00 USD | 5,220,000.00 USD | 247,240.00 USD | 0.00 USD | 136.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.42` | 7,310,000.00 USD | 7,310,000.00 USD | 229,660.00 USD | 97,940.00 USD | 236.06 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 4,980,000.00 USD | 4,980,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.44` | 6,980,000.00 USD | 6,980,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 5,590.00 USD | 9,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 4,440,000.00 USD | 4,440,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.46` | 6,190,000.00 USD | 6,190,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 4,120,000.00 USD | 4,120,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.48` | 5,760,000.00 USD | 5,760,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 4,010,000.00 USD | 4,010,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.50` | 5,550,000.00 USD | 5,550,000.00 USD | 4,770.00 USD | 52,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 3,930,000.00 USD | 3,930,000.00 USD | 668.27 USD | 12,710.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.52` | 5,490,000.00 USD | 5,490,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 3,880,000.00 USD | 3,880,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.54` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 3,640,000.00 USD | 3,640,000.00 USD | 108,320.00 USD | 38,520.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.56` | 5,410,000.00 USD | 5,410,000.00 USD | 121,680.00 USD | 81,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 3,450,000.00 USD | 3,450,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.58` | 5,200,000.00 USD | 5,200,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 3,350,000.00 USD | 3,350,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.60` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 24,130.00 USD | 458.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 3,310,000.00 USD | 3,310,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.62` | 5,160,000.00 USD | 5,160,000.00 USD | 99,990.00 USD | 0.00 USD | 180.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 3,110,000.00 USD | 3,110,000.00 USD | 109,830.00 USD | 9,030.00 USD | 56,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.64` | 5,060,000.00 USD | 5,060,000.00 USD | 11,150.00 USD | 0.00 USD | 28,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.66` | 2,940,000.00 USD | 2,940,000.00 USD | 59,930.00 USD | 7,540.00 USD | 29,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.66` | 5,020,000.00 USD | 5,020,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,840,000.00 USD | 2,840,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.68` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,700,000.00 USD | 2,700,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.70` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 2,680,000.00 USD | 2,680,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.72` | 4,970,000.00 USD | 4,970,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 2,460,000.00 USD | 2,460,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.74` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.76` | 2,350,000.00 USD | 2,350,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.76` | 4,360,000.00 USD | 4,360,000.00 USD | 16,310.00 USD | 120,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 2,170,000.00 USD | 2,170,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.78` | 4,230,000.00 USD | 4,230,000.00 USD | 535,020.00 USD | 46,010.00 USD | 103,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,720,000.00 USD | 1,720,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.80` | 3,540,000.00 USD | 3,540,000.00 USD | 69,540.00 USD | 70,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,610,000.00 USD | 1,610,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.82` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 104,870.00 USD | 206,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,450,000.00 USD | 1,450,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.84` | 3,090,000.00 USD | 3,090,000.00 USD | 377,580.00 USD | 80,420.00 USD | 196,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.85` | 1,380.00 USD | 1,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 998,620.00 USD | 998,620.00 USD | 203,140.00 USD | 34,420.00 USD | 213,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.86` | 2,440,000.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 390,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 547,940.00 USD | 547,940.00 USD | 61,520.00 USD | 9,550.00 USD | 59,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.88` | 1,720,000.00 USD | 1,720,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 417,410.00 USD | 417,410.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.90` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 38,140.00 USD | 220,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 219,110.00 USD | 219,110.00 USD | 103,270.00 USD | 19,240.00 USD | 86.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.92` | 960,920.00 USD | 960,920.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 96,520.00 USD | 96,520.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.94` | 623,540.00 USD | 623,540.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `10.95` | 2,180.00 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 90,600.00 USD | 90,600.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.96` | 621,060.00 USD | 621,060.00 USD | 10,430.00 USD | 0.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.98` | 560,710.00 USD | 560,710.00 USD | 17,930.00 USD | 0.00 USD | 209,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.00` | 2,840.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 103.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.00` | 333,490.00 USD | 333,490.00 USD | 10,830.00 USD | 0.00 USD | 634.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.02` | 322,020.00 USD | 322,020.00 USD | 0.00 USD | 0.00 USD | 143,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.04` | 2,740.00 USD | 2,740.00 USD | 0.00 USD | 2,200.00 USD | 402.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.04` | 178,530.00 USD | 178,530.00 USD | 0.00 USD | 0.00 USD | 178,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.06` | 135.97 USD | 135.97 USD | 0.00 USD | 0.00 USD | 135.97 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.06` | 132,650.00 USD | 132,650.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.06` | 265,310.00 USD | 265,310.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.08` | 267,620.00 USD | 267,620.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.10` | 7,750.00 USD | 7,750.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.10` | 645,570.00 USD | 645,570.00 USD | 282,040.00 USD | 6,920.00 USD | 88,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.12` | 152,600.00 USD | 152,600.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.12` | 1,150,000.00 USD | 1,150,000.00 USD | 261,760.00 USD | 5,170.00 USD | 234,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.14` | 225,650.00 USD | 225,650.00 USD | 4,910.00 USD | 0.00 USD | 68,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.14` | 1,360,000.00 USD | 1,360,000.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.16` | 405,030.00 USD | 405,030.00 USD | 127,020.00 USD | 2,100.00 USD | 50,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.16` | 1,630,000.00 USD | 1,630,000.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.18` | 577,410.00 USD | 577,410.00 USD | 71,610.00 USD | 14,380.00 USD | 86,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.18` | 1,650,000.00 USD | 1,650,000.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.20` | 830,900.00 USD | 830,900.00 USD | 76,580.00 USD | 85,800.00 USD | 91,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.20` | 1,990,000.00 USD | 1,990,000.00 USD | 171,840.00 USD | 89,800.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.22` | 1,390,000.00 USD | 1,390,000.00 USD | 344,290.00 USD | 76,600.00 USD | 142,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.22` | 2,510,000.00 USD | 2,510,000.00 USD | 482,460.00 USD | 42,050.00 USD | 603.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.24` | 1,770,000.00 USD | 1,770,000.00 USD | 163,340.00 USD | 58,590.00 USD | 155,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.24` | 2,880,000.00 USD | 2,880,000.00 USD | 231,960.00 USD | 59,950.00 USD | 71,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.25` | 1,850.00 USD | 5,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.26` | 2,050,000.00 USD | 2,050,000.00 USD | 154,720.00 USD | 54,310.00 USD | 71,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.26` | 3,740,000.00 USD | 3,740,000.00 USD | 520,990.00 USD | 48,250.00 USD | 296,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 2,770,000.00 USD | 2,770,000.00 USD | 388,220.00 USD | 67,290.00 USD | 263,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.28` | 4,380,000.00 USD | 4,380,000.00 USD | 429,350.00 USD | 57,050.00 USD | 147,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 3,270,000.00 USD | 3,270,000.00 USD | 261,740.00 USD | 81,010.00 USD | 153,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.30` | 4,510,000.00 USD | 4,510,000.00 USD | 24,980.00 USD | 32,240.00 USD | 77,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 3,660,000.00 USD | 3,660,000.00 USD | 181,160.00 USD | 67,470.00 USD | 142,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.32` | 5,010,000.00 USD | 5,010,000.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 4,270,000.00 USD | 4,270,000.00 USD | 390,100.00 USD | 114,410.00 USD | 107,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.34` | 5,350,000.00 USD | 5,350,000.00 USD | 127,190.00 USD | 116,400.00 USD | 101,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.36` | 4,560,000.00 USD | 4,560,000.00 USD | 138,710.00 USD | 95,240.00 USD | 56,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.36` | 5,610,000.00 USD | 5,610,000.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 4,790,000.00 USD | 4,790,000.00 USD | 118,230.00 USD | 85,980.00 USD | 25,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.38` | 5,850,000.00 USD | 5,850,000.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 4,970,000.00 USD | 4,970,000.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.40` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 5,290,000.00 USD | 5,290,000.00 USD | 126,960.00 USD | 83,740.00 USD | 113,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.42` | 6,120,000.00 USD | 6,120,000.00 USD | 66,800.00 USD | 46,660.00 USD | 115,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 5,550,000.00 USD | 5,550,000.00 USD | 96,590.00 USD | 54,990.00 USD | 109,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.44` | 6,560,000.00 USD | 6,560,000.00 USD | 303,190.00 USD | 101,940.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 249.61 USD | 5,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 5,770,000.00 USD | 5,770,000.00 USD | 86,190.00 USD | 77,320.00 USD | 50,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.46` | 6,740,000.00 USD | 6,740,000.00 USD | 122,890.00 USD | 55,470.00 USD | 269.04 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 5,830,000.00 USD | 5,830,000.00 USD | 26,740.00 USD | 35,780.00 USD | 1,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.48` | 6,970,000.00 USD | 6,970,000.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 6,010,000.00 USD | 6,010,000.00 USD | 78,340.00 USD | 38,760.00 USD | 63,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.50` | 7,140,000.00 USD | 7,140,000.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 6,210,000.00 USD | 6,210,000.00 USD | 127,920.00 USD | 22,260.00 USD | 52,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.52` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 5,760.00 USD | 62,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 6,430,000.00 USD | 6,430,000.00 USD | 92,850.00 USD | 20,290.00 USD | 101,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.54` | 7,370,000.00 USD | 7,370,000.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 3,800.00 USD | 9,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 6,630,000.00 USD | 6,630,000.00 USD | 128,820.00 USD | 20,640.00 USD | 47,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.56` | 7,480,000.00 USD | 7,480,000.00 USD | 86,650.00 USD | 19,860.00 USD | 432.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 6,710,000.00 USD | 6,710,000.00 USD | 58,870.00 USD | 2,950.00 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.58` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 6,850,000.00 USD | 6,850,000.00 USD | 59,780.00 USD | 14,330.00 USD | 67,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.60` | 7,590,000.00 USD | 7,590,000.00 USD | 46,010.00 USD | 10,510.00 USD | 23,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 6,940,000.00 USD | 6,940,000.00 USD | 44,730.00 USD | 512.95 USD | 48,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.62` | 7,660,000.00 USD | 7,660,000.00 USD | 65,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.64` | 6,990,000.00 USD | 6,990,000.00 USD | 5,660.00 USD | 7,410.00 USD | 31,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.64` | 7,700,000.00 USD | 7,700,000.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 5,230.00 USD | 14,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.66` | 7,020,000.00 USD | 7,020,000.00 USD | 228.94 USD | 12,290.00 USD | 25,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.66` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 7,220,000.00 USD | 7,220,000.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.68` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 7,240,000.00 USD | 7,240,000.00 USD | 239.66 USD | 4,760.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.70` | 7,930,000.00 USD | 7,930,000.00 USD | 38,760.00 USD | 722.15 USD | 176.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 7,440,000.00 USD | 7,440,000.00 USD | 91,840.00 USD | 17,160.00 USD | 98,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.72` | 8,260,000.00 USD | 8,260,000.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 7,630,000.00 USD | 7,630,000.00 USD | 76,690.00 USD | 30,280.00 USD | 73,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.74` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.76` | 7,690,000.00 USD | 7,690,000.00 USD | 26,330.00 USD | 14,880.00 USD | 24,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.76` | 8,450,000.00 USD | 8,450,000.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 7,760,000.00 USD | 7,760,000.00 USD | 11,750.00 USD | 20,510.00 USD | 40,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.78` | 8,520,000.00 USD | 8,520,000.00 USD | 9,130.00 USD | 0.00 USD | 56,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 7,780,000.00 USD | 7,780,000.00 USD | 1,350.00 USD | 18,000.00 USD | 531.07 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.80` | 8,660,000.00 USD | 8,660,000.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 7,830,000.00 USD | 7,830,000.00 USD | 12,210.00 USD | 53.10 USD | 36,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.82` | 8,880,000.00 USD | 8,880,000.00 USD | 182,750.00 USD | 41,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 7,930,000.00 USD | 7,930,000.00 USD | 43,880.00 USD | 11,870.00 USD | 45,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.84` | 9,130,000.00 USD | 9,130,000.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 169.46 USD | 14,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 8,010,000.00 USD | 8,010,000.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.86` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 8,120,000.00 USD | 8,120,000.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.88` | 9,200,000.00 USD | 9,200,000.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 8,200,000.00 USD | 8,200,000.00 USD | 43,700.00 USD | 8,690.00 USD | 28,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.90` | 9,260,000.00 USD | 9,260,000.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 8,480,000.00 USD | 8,480,000.00 USD | 230,070.00 USD | 22,930.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.92` | 9,470,000.00 USD | 9,470,000.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 8,580,000.00 USD | 8,580,000.00 USD | 48,030.00 USD | 15,260.00 USD | 40,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.94` | 9,660,000.00 USD | 9,660,000.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.95` | 283.21 USD | 15,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.96` | 8,730,000.00 USD | 8,730,000.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.96` | 9,840,000.00 USD | 9,840,000.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 8,890,000.00 USD | 8,890,000.00 USD | 59,940.00 USD | 29,050.00 USD | 68,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.98` | 10,490,000.00 USD | 10,490,000.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 9,050,000.00 USD | 9,050,000.00 USD | 102,680.00 USD | 23,880.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.00` | 11,130,000.00 USD | 11,130,000.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 9,110,000.00 USD | 9,110,000.00 USD | 13,680.00 USD | 9,340.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.02` | 11,700,000.00 USD | 11,700,000.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 9,290,000.00 USD | 9,290,000.00 USD | 90,410.00 USD | 39,490.00 USD | 56,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.04` | 12,320,000.00 USD | 12,320,000.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 9,480,000.00 USD | 9,480,000.00 USD | 76,750.00 USD | 43,270.00 USD | 69,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.06` | 12,830,000.00 USD | 12,830,000.00 USD | 237,300.00 USD | 121,530.00 USD | 145,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 9,620,000.00 USD | 9,620,000.00 USD | 43,090.00 USD | 40,800.00 USD | 52,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.08` | 13,490,000.00 USD | 13,490,000.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 9,730,000.00 USD | 9,730,000.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.10` | 13,670,000.00 USD | 13,670,000.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 9,950,000.00 USD | 9,950,000.00 USD | 116,870.00 USD | 54,580.00 USD | 50,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.12` | 14,060,000.00 USD | 14,060,000.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 10,120,000.00 USD | 10,120,000.00 USD | 75,920.00 USD | 37,540.00 USD | 55,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.14` | 14,430,000.00 USD | 14,430,000.00 USD | 148,090.00 USD | 102,170.00 USD | 119,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 10,360,000.00 USD | 10,360,000.00 USD | 132,030.00 USD | 34,710.00 USD | 67,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.16` | 14,750,000.00 USD | 14,750,000.00 USD | 182,020.00 USD | 69,310.00 USD | 75,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 10,570,000.00 USD | 10,570,000.00 USD | 112,670.00 USD | 48,310.00 USD | 50,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.18` | 14,930,000.00 USD | 14,930,000.00 USD | 74,850.00 USD | 54,220.00 USD | 43,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 10,730,000.00 USD | 10,730,000.00 USD | 77,250.00 USD | 43,870.00 USD | 41,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.20` | 15,250,000.00 USD | 15,250,000.00 USD | 194,760.00 USD | 51,940.00 USD | 75,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 10,790,000.00 USD | 10,790,000.00 USD | 10,400.00 USD | 17,890.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.22` | 15,640,000.00 USD | 15,640,000.00 USD | 261,490.00 USD | 63,820.00 USD | 64,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.24` | 15,740,000.00 USD | 15,740,000.00 USD | 50,300.00 USD | 45,440.00 USD | 10,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 1,430.00 USD | 16,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.26` | 15,920,000.00 USD | 15,920,000.00 USD | 73,660.00 USD | 54,120.00 USD | 50,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.28` | 16,200,000.00 USD | 16,200,000.00 USD | 156,680.00 USD | 27,340.00 USD | 90,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.30` | 16,390,000.00 USD | 16,390,000.00 USD | 70,240.00 USD | 49,630.00 USD | 77,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.32` | 16,460,000.00 USD | 16,460,000.00 USD | 22,620.00 USD | 25,760.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.34` | 16,520,000.00 USD | 16,520,000.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 17,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `12.36` | 16,600,000.00 USD | 16,600,000.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.38` | 16,610,000.00 USD | 16,610,000.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.45` | 1,980.00 USD | 19,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.55` | 7,190.00 USD | 26,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.65` | 435.16 USD | 26,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.95` | 540.01 USD | 27,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,430.00 USD | 32,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 92,890.00 USD | 125,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.95` | 758.88 USD | 126,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 601.34 USD | 127,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.25` | 544.35 USD | 127,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.35` | 3,860.00 USD | 131,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.65` | 4,340.00 USD | 135,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 161,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 578.46 USD | 161,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 271.04 USD | 162,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 162,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.15` | 323.00 USD | 162,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.25` | 227.50 USD | 162,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,390.00 USD | 164,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 31,700.00 USD | 195,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.75` | 101,910.00 USD | 297,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 377,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 1,370.00 USD | 378,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.35` | 26,700.00 USD | 405,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.65` | 5,560.00 USD | 411,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249.90 USD | 411,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 251,080.00 USD | 662,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 664,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 692,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 2,130,000.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 186.50 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 850,790.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.55` | 1,090.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.75` | 359.45 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.15` | 1,260.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,770.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 7,250.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.85` | 114.68 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.05` | 202.08 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.35` | 217.77 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.75` | 65,060.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.25` | 12,270,000.00 USD | 0.00 USD | 1,720.00 USD | `-79.56%` | `766,500.00` |
| `Live` | `Long` | `2.35` | 12,270,000.00 USD | 0.00 USD | 50,730.00 USD | `-78.65%` | `21,585,500.00` |
| `Live` | `Long` | `2.55` | 12,220,000.00 USD | 0.00 USD | 1,030.00 USD | `-76.83%` | `402,300.00` |
| `Live` | `Long` | `2.65` | 12,220,000.00 USD | 0.00 USD | 6,130.00 USD | `-75.92%` | `2,314,300.00` |
| `Live` | `Long` | `2.75` | 12,210,000.00 USD | 0.00 USD | 28,270.00 USD | `-75.01%` | `10,281,800.00` |
| `Live` | `Long` | `3.05` | 12,190,000.00 USD | 0.00 USD | 7,490.00 USD | `-72.29%` | `2,454,900.00` |
| `Live` | `Long` | `3.15` | 12,180,000.00 USD | 0.00 USD | 1,430.00 USD | `-71.38%` | `454,900.00` |
| `Live` | `Long` | `3.25` | 12,180,000.00 USD | 0.00 USD | 445.25 USD | `-70.47%` | `137,000.00` |
| `Live` | `Long` | `3.35` | 12,180,000.00 USD | 0.00 USD | 1,970.00 USD | `-69.56%` | `586,600.00` |
| `Live` | `Long` | `3.45` | 12,170,000.00 USD | 0.00 USD | 8,030.00 USD | `-68.65%` | `2,327,300.00` |
| `Live` | `Long` | `3.55` | 12,170,000.00 USD | 0.00 USD | 126.73 USD | `-67.74%` | `35,700.00` |
| `Live` | `Long` | `3.65` | 12,170,000.00 USD | 0.00 USD | 2,190.00 USD | `-66.84%` | `600,000.00` |
| `Live` | `Long` | `3.85` | 12,160,000.00 USD | 0.00 USD | 250.25 USD | `-65.02%` | `65,000.00` |
| `Live` | `Long` | `3.95` | 12,160,000.00 USD | 0.00 USD | 4,420.00 USD | `-64.11%` | `1,118,500.00` |
| `Live` | `Long` | `4.05` | 12,160,000.00 USD | 0.00 USD | 950.54 USD | `-63.20%` | `234,700.00` |
| `Live` | `Long` | `4.15` | 12,160,000.00 USD | 0.00 USD | 412.51 USD | `-62.29%` | `99,400.00` |
| `Live` | `Long` | `4.25` | 12,160,000.00 USD | 0.00 USD | 20,850.00 USD | `-61.38%` | `4,905,100.00` |
| `Live` | `Long` | `4.35` | 12,140,000.00 USD | 0.00 USD | 5,600.00 USD | `-60.48%` | `1,287,000.00` |
| `Live` | `Long` | `4.45` | 12,130,000.00 USD | 0.00 USD | 1,050.00 USD | `-59.57%` | `235,700.00` |
| `Live` | `Long` | `4.55` | 12,130,000.00 USD | 0.00 USD | 7,280.00 USD | `-58.66%` | `1,599,800.00` |
| `Live` | `Long` | `4.65` | 12,120,000.00 USD | 0.00 USD | 17,600.00 USD | `-57.75%` | `3,784,500.00` |
| `Live` | `Long` | `4.75` | 12,110,000.00 USD | 0.00 USD | 366,620.00 USD | `-56.84%` | `77,183,100.00` |
| `Live` | `Long` | `4.85` | 11,740,000.00 USD | 0.00 USD | 2,070.00 USD | `-55.93%` | `426,800.00` |
| `Live` | `Long` | `4.95` | 11,740,000.00 USD | 0.00 USD | 6,080.00 USD | `-55.02%` | `1,228,100.00` |
| `Live` | `Long` | `5.05` | 11,730,000.00 USD | 0.00 USD | 217.66 USD | `-54.12%` | `43,100.00` |
| `Live` | `Long` | `5.15` | 11,730,000.00 USD | 0.00 USD | 262.13 USD | `-53.21%` | `50,900.00` |
| `Live` | `Long` | `5.25` | 11,730,000.00 USD | 0.00 USD | 5,020.00 USD | `-52.30%` | `956,800.00` |
| `Live` | `Long` | `5.35` | 11,720,000.00 USD | 0.00 USD | 543,950.00 USD | `-51.39%` | `101,672,700.00` |
| `Live` | `Long` | `5.45` | 11,180,000.00 USD | 0.00 USD | 2,600.00 USD | `-50.48%` | `477,300.00` |
| `Live` | `Long` | `5.55` | 11,180,000.00 USD | 0.00 USD | 9,670.00 USD | `-49.57%` | `1,741,600.00` |
| `Live` | `Long` | `5.65` | 11,170,000.00 USD | 0.00 USD | 35,770.00 USD | `-48.66%` | `6,330,200.00` |
| `Live` | `Long` | `5.75` | 11,130,000.00 USD | 0.00 USD | 18,750.00 USD | `-47.76%` | `3,260,900.00` |
| `Live` | `Long` | `5.85` | 11,110,000.00 USD | 0.00 USD | 6,010.00 USD | `-46.85%` | `1,026,700.00` |
| `Live` | `Long` | `5.95` | 11,110,000.00 USD | 0.00 USD | 10,260.00 USD | `-45.94%` | `1,724,100.00` |
| `Live` | `Long` | `6.05` | 11,100,000.00 USD | 0.00 USD | 13,590.00 USD | `-45.03%` | `2,245,800.00` |
| `Live` | `Long` | `6.15` | 11,080,000.00 USD | 0.00 USD | 489.54 USD | `-44.12%` | `79,600.00` |
| `Live` | `Long` | `6.25` | 11,080,000.00 USD | 0.00 USD | 29,010.00 USD | `-43.21%` | `4,642,000.00` |
| `Live` | `Long` | `6.35` | 11,050,000.00 USD | 0.00 USD | 54,590.00 USD | `-42.30%` | `8,596,600.00` |
| `Live` | `Long` | `6.45` | 11,000,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.40%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 10,990,000.00 USD | 0.00 USD | 2,910.00 USD | `-40.49%` | `444,300.00` |
| `Live` | `Long` | `6.65` | 10,990,000.00 USD | 0.00 USD | 1,130,000.00 USD | `-39.58%` | `169,295,200.00` |
| `Live` | `Long` | `6.75` | 9,860,000.00 USD | 0.00 USD | 24,870.00 USD | `-38.67%` | `3,684,700.00` |
| `Live` | `Long` | `6.85` | 9,840,000.00 USD | 0.00 USD | 5,060.00 USD | `-37.76%` | `738,400.00` |
| `Live` | `Long` | `6.95` | 9,830,000.00 USD | 0.00 USD | 79,160.00 USD | `-36.85%` | `11,389,500.00` |
| `Live` | `Long` | `7.05` | 9,750,000.00 USD | 0.00 USD | 690,270.00 USD | `-35.94%` | `97,910,200.00` |
| `Live` | `Long` | `7.15` | 9,060,000.00 USD | 0.00 USD | 32,340.00 USD | `-35.04%` | `4,522,900.00` |
| `Live` | `Long` | `7.25` | 9,030,000.00 USD | 0.00 USD | 7,160.00 USD | `-34.13%` | `986,900.00` |
| `Live` | `Long` | `7.35` | 9,020,000.00 USD | 0.00 USD | 20,090.00 USD | `-33.22%` | `2,734,000.00` |
| `Live` | `Long` | `7.45` | 9,000,000.00 USD | 0.00 USD | 40,720.00 USD | `-32.31%` | `5,465,700.00` |
| `Live` | `Long` | `7.55` | 8,960,000.00 USD | 0.00 USD | 173,010.00 USD | `-31.40%` | `22,914,800.00` |
| `Live` | `Long` | `7.65` | 8,790,000.00 USD | 0.00 USD | 1,830.00 USD | `-30.49%` | `239,400.00` |
| `Live` | `Long` | `7.75` | 8,790,000.00 USD | 0.00 USD | 19,300.00 USD | `-29.58%` | `2,490,300.00` |
| `Live` | `Long` | `7.85` | 8,770,000.00 USD | 0.00 USD | 3,150,000.00 USD | `-28.68%` | `400,988,000.00` |
| `Live` | `Long` | `7.95` | 5,620,000.00 USD | 0.00 USD | 17,480.00 USD | `-27.77%` | `2,198,500.00` |
| `Live` | `Long` | `8.05` | 5,600,000.00 USD | 0.00 USD | 99,930.00 USD | `-26.86%` | `12,413,400.00` |
| `Live` | `Long` | `8.15` | 5,500,000.00 USD | 0.00 USD | 45,950.00 USD | `-25.95%` | `5,638,000.00` |
| `Live` | `Long` | `8.25` | 5,460,000.00 USD | 0.00 USD | 32,110.00 USD | `-25.04%` | `3,892,000.00` |
| `Live` | `Long` | `8.35` | 5,430,000.00 USD | 0.00 USD | 6,370.00 USD | `-24.13%` | `762,600.00` |
| `Live` | `Long` | `8.45` | 5,420,000.00 USD | 0.00 USD | 520,270.00 USD | `-23.22%` | `61,570,800.00` |
| `Live` | `Long` | `8.55` | 4,900,000.00 USD | 0.00 USD | 58,710.00 USD | `-22.32%` | `6,866,700.00` |
| `Live` | `Long` | `8.65` | 4,840,000.00 USD | 0.00 USD | 15,270.00 USD | `-21.41%` | `1,765,700.00` |
| `Live` | `Long` | `8.75` | 4,820,000.00 USD | 0.00 USD | 17,890.00 USD | `-20.50%` | `2,044,100.00` |
| `Live` | `Long` | `8.85` | 4,810,000.00 USD | 0.00 USD | 60,320.00 USD | `-19.59%` | `6,816,200.00` |
| `Live` | `Long` | `8.95` | 4,750,000.00 USD | 0.00 USD | 458,450.00 USD | `-18.68%` | `51,223,800.00` |
| `Live` | `Long` | `9.05` | 4,290,000.00 USD | 0.00 USD | 105,400.00 USD | `-17.77%` | `11,646,400.00` |
| `Live` | `Long` | `9.15` | 4,180,000.00 USD | 0.00 USD | 76,640.00 USD | `-16.86%` | `8,376,000.00` |
| `Live` | `Long` | `9.25` | 4,110,000.00 USD | 0.00 USD | 19,930.00 USD | `-15.95%` | `2,154,800.00` |
| `Live` | `Long` | `9.35` | 4,090,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-15.05%` | `229,774,900.00` |
| `Live` | `Long` | `9.45` | 1,940,000.00 USD | 0.00 USD | 55,700.00 USD | `-14.14%` | `5,894,700.00` |
| `Live` | `Long` | `9.55` | 1,880,000.00 USD | 0.00 USD | 103,520.00 USD | `-13.23%` | `10,839,700.00` |
| `Live` | `Long` | `9.65` | 1,780,000.00 USD | 0.00 USD | 202,670.00 USD | `-12.32%` | `21,001,700.00` |
| `Live` | `Long` | `9.75` | 1,580,000.00 USD | 0.00 USD | 85,410.00 USD | `-11.41%` | `8,760,500.00` |
| `Live` | `Long` | `9.85` | 1,490,000.00 USD | 0.00 USD | 30,620.00 USD | `-10.50%` | `3,108,900.00` |
| `Live` | `Long` | `9.95` | 1,460,000.00 USD | 0.00 USD | 433,320.00 USD | `-9.59%` | `43,549,800.00` |
| `Live` | `Long` | `10.05` | 1,030,000.00 USD | 0.00 USD | 774,770.00 USD | `-8.69%` | `77,091,800.00` |
| `Live` | `Long` | `10.15` | 251,760.00 USD | 0.00 USD | 69,470.00 USD | `-7.78%` | `6,844,000.00` |
| `Live` | `Long` | `10.25` | 182,290.00 USD | 0.00 USD | 32,460.00 USD | `-6.87%` | `3,166,900.00` |
| `Live` | `Long` | `10.35` | 149,830.00 USD | 0.00 USD | 140,250.00 USD | `-5.96%` | `13,550,500.00` |
| `Live` | `Long` | `10.45` | 9,580.00 USD | 0.00 USD | 5,590.00 USD | `-5.05%` | `534,800.00` |
| `Live` | `Long` | `10.55` | 3,990.00 USD | 0.00 USD | 3,990.00 USD | `-4.14%` | `378,500.00` |
| `Live` | `Short` | `10.85` | 1,380.00 USD | 1,380.00 USD | 0.00 USD | `-1.42%` | `127,500.00` |
| `Live` | `Short` | `10.95` | 3,560.00 USD | 2,180.00 USD | 0.00 USD | `-0.51%` | `199,100.00` |
| `Live` | `Short` | `11.25` | 5,410.00 USD | 1,850.00 USD | 0.00 USD | `+2.22%` | `164,100.00` |
| `Live` | `Short` | `11.45` | 5,660.00 USD | 249.61 USD | 0.00 USD | `+4.03%` | `21,800.00` |
| `Live` | `Short` | `11.55` | 9,450.00 USD | 3,800.00 USD | 0.00 USD | `+4.94%` | `328,600.00` |
| `Live` | `Short` | `11.65` | 14,680.00 USD | 5,230.00 USD | 0.00 USD | `+5.85%` | `448,800.00` |
| `Live` | `Short` | `11.85` | 14,850.00 USD | 169.46 USD | 0.00 USD | `+7.67%` | `14,300.00` |
| `Live` | `Short` | `11.95` | 15,140.00 USD | 283.21 USD | 0.00 USD | `+8.58%` | `23,700.00` |
| `Live` | `Short` | `12.25` | 16,570.00 USD | 1,430.00 USD | 0.00 USD | `+11.30%` | `116,800.00` |
| `Live` | `Short` | `12.35` | 17,300.00 USD | 736.06 USD | 0.00 USD | `+12.21%` | `59,600.00` |
| `Live` | `Short` | `12.45` | 19,280.00 USD | 1,980.00 USD | 0.00 USD | `+13.12%` | `158,800.00` |
| `Live` | `Short` | `12.55` | 26,470.00 USD | 7,190.00 USD | 0.00 USD | `+14.03%` | `572,900.00` |
| `Live` | `Short` | `12.65` | 26,900.00 USD | 435.16 USD | 0.00 USD | `+14.94%` | `34,400.00` |
| `Live` | `Short` | `12.95` | 27,440.00 USD | 540.01 USD | 0.00 USD | `+17.66%` | `41,700.00` |
| `Live` | `Short` | `13.45` | 32,870.00 USD | 5,430.00 USD | 0.00 USD | `+22.21%` | `403,700.00` |
| `Live` | `Short` | `13.55` | 125,770.00 USD | 92,890.00 USD | 0.00 USD | `+23.11%` | `6,855,700.00` |
| `Live` | `Short` | `13.95` | 126,530.00 USD | 758.88 USD | 0.00 USD | `+26.75%` | `54,400.00` |
| `Live` | `Short` | `14.05` | 127,130.00 USD | 601.34 USD | 0.00 USD | `+27.66%` | `42,800.00` |
| `Live` | `Short` | `14.25` | 127,670.00 USD | 544.35 USD | 0.00 USD | `+29.47%` | `38,200.00` |
| `Live` | `Short` | `14.35` | 131,540.00 USD | 3,860.00 USD | 0.00 USD | `+30.38%` | `269,100.00` |
| `Live` | `Short` | `14.65` | 135,880.00 USD | 4,340.00 USD | 0.00 USD | `+33.11%` | `296,400.00` |
| `Live` | `Short` | `14.95` | 161,210.00 USD | 25,330.00 USD | 0.00 USD | `+35.83%` | `1,694,600.00` |
| `Live` | `Short` | `15.55` | 161,790.00 USD | 578.46 USD | 0.00 USD | `+41.29%` | `37,200.00` |
| `Live` | `Short` | `15.85` | 162,060.00 USD | 271.04 USD | 0.00 USD | `+44.01%` | `17,100.00` |
| `Live` | `Short` | `15.95` | 162,200.00 USD | 138.76 USD | 0.00 USD | `+44.92%` | `8,700.00` |
| `Live` | `Short` | `16.15` | 162,520.00 USD | 323.00 USD | 0.00 USD | `+46.74%` | `20,000.00` |
| `Live` | `Short` | `16.25` | 162,750.00 USD | 227.50 USD | 0.00 USD | `+47.65%` | `14,000.00` |
| `Live` | `Short` | `16.35` | 164,150.00 USD | 1,390.00 USD | 0.00 USD | `+48.56%` | `85,300.00` |
| `Live` | `Short` | `16.55` | 195,850.00 USD | 31,700.00 USD | 0.00 USD | `+50.37%` | `1,915,700.00` |
| `Live` | `Short` | `16.75` | 297,760.00 USD | 101,910.00 USD | 0.00 USD | `+52.19%` | `6,084,000.00` |
| `Live` | `Short` | `16.95` | 377,530.00 USD | 79,770.00 USD | 0.00 USD | `+54.01%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 378,900.00 USD | 1,370.00 USD | 0.00 USD | `+55.82%` | `79,700.00` |
| `Live` | `Short` | `17.35` | 405,600.00 USD | 26,700.00 USD | 0.00 USD | `+57.64%` | `1,539,000.00` |
| `Live` | `Short` | `17.65` | 411,150.00 USD | 5,560.00 USD | 0.00 USD | `+60.37%` | `314,800.00` |
| `Live` | `Short` | `17.85` | 411,400.00 USD | 249.90 USD | 0.00 USD | `+62.18%` | `14,000.00` |
| `Live` | `Short` | `17.95` | 662,480.00 USD | 251,080.00 USD | 0.00 USD | `+63.09%` | `13,987,600.00` |
| `Live` | `Short` | `18.05` | 664,450.00 USD | 1,970.00 USD | 0.00 USD | `+64.00%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 692,250.00 USD | 27,790.00 USD | 0.00 USD | `+65.82%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 2,820,000.00 USD | 2,130,000.00 USD | 0.00 USD | `+67.64%` | `115,242,000.00` |
| `Live` | `Short` | `18.55` | 2,820,000.00 USD | 185.50 USD | 0.00 USD | `+68.54%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 2,820,000.00 USD | 186.50 USD | 0.00 USD | `+69.45%` | `10,000.00` |
| `Live` | `Short` | `18.85` | 3,670,000.00 USD | 850,790.00 USD | 0.00 USD | `+71.27%` | `45,134,800.00` |
| `Live` | `Short` | `19.55` | 3,670,000.00 USD | 1,090.00 USD | 0.00 USD | `+77.63%` | `55,900.00` |
| `Live` | `Short` | `19.65` | 3,710,000.00 USD | 38,790.00 USD | 0.00 USD | `+78.54%` | `1,974,000.00` |
| `Live` | `Short` | `19.75` | 3,710,000.00 USD | 359.45 USD | 0.00 USD | `+79.45%` | `18,200.00` |
| `Live` | `Short` | `19.95` | 3,710,000.00 USD | 291.27 USD | 0.00 USD | `+81.26%` | `14,600.00` |
| `Live` | `Short` | `20.15` | 3,710,000.00 USD | 1,260.00 USD | 0.00 USD | `+83.08%` | `62,500.00` |
| `Live` | `Short` | `20.45` | 3,710,000.00 USD | 1,770.00 USD | 0.00 USD | `+85.81%` | `86,700.00` |
| `Live` | `Short` | `20.55` | 3,720,000.00 USD | 7,250.00 USD | 0.00 USD | `+86.72%` | `353,000.00` |
| `Live` | `Short` | `20.85` | 3,720,000.00 USD | 114.68 USD | 0.00 USD | `+89.44%` | `5,500.00` |
| `Live` | `Short` | `21.05` | 3,720,000.00 USD | 202.08 USD | 0.00 USD | `+91.26%` | `9,600.00` |
| `Live` | `Short` | `21.35` | 3,720,000.00 USD | 217.77 USD | 0.00 USD | `+93.99%` | `10,200.00` |
| `Live` | `Short` | `21.75` | 3,790,000.00 USD | 65,060.00 USD | 0.00 USD | `+97.62%` | `2,991,400.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.45` | 401,190.00 USD | 0.00 USD | 182.03 USD | `-77.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.85` | 401,010.00 USD | 0.00 USD | 221.45 USD | `-74.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `2.95` | 400,790.00 USD | 0.00 USD | 234.23 USD | `-73.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.15` | 400,560.00 USD | 0.00 USD | 209.48 USD | `-71.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.45` | 400,350.00 USD | 0.00 USD | 236.33 USD | `-68.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `3.55` | 400,110.00 USD | 0.00 USD | 431.68 USD | `-67.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 399,680.00 USD | 0.00 USD | 290.29 USD | `-58.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 399,390.00 USD | 0.00 USD | 120.22 USD | `-52.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.65` | 399,270.00 USD | 0.00 USD | 3,790.00 USD | `-48.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 395,470.00 USD | 0.00 USD | 251.68 USD | `-45.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.35` | 395,220.00 USD | 0.00 USD | 749.94 USD | `-42.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.45` | 394,470.00 USD | 0.00 USD | 772.71 USD | `-41.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 393,700.00 USD | 0.00 USD | 3,760.00 USD | `-40.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 389,940.00 USD | 0.00 USD | 133.00 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.95` | 389,800.00 USD | 0.00 USD | 1,320.00 USD | `-36.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 388,490.00 USD | 0.00 USD | 3,770.00 USD | `-35.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 384,720.00 USD | 0.00 USD | 2,070.00 USD | `-34.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 382,650.00 USD | 0.00 USD | 3,740.00 USD | `-32.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 378,900.00 USD | 0.00 USD | 1,050.00 USD | `-31.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 377,850.00 USD | 0.00 USD | 120.90 USD | `-29.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 377,730.00 USD | 0.00 USD | 146.80 USD | `-28.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 377,580.00 USD | 0.00 USD | 124.02 USD | `-27.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 377,460.00 USD | 0.00 USD | 5,000.00 USD | `-26.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 372,460.00 USD | 0.00 USD | 393.64 USD | `-25.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 372,060.00 USD | 0.00 USD | 10,560.00 USD | `-25.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 361,500.00 USD | 0.00 USD | 57,330.00 USD | `-24.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 304,170.00 USD | 0.00 USD | 1,480.00 USD | `-23.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 302,690.00 USD | 0.00 USD | 52,990.00 USD | `-22.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 249,700.00 USD | 0.00 USD | 186.84 USD | `-21.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 249,520.00 USD | 0.00 USD | 742.88 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 248,780.00 USD | 0.00 USD | 902.70 USD | `-19.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 247,870.00 USD | 0.00 USD | 1,570.00 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 246,300.00 USD | 0.00 USD | 3,440.00 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 242,860.00 USD | 0.00 USD | 194.90 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.25` | 242,660.00 USD | 0.00 USD | 1,360.00 USD | `-15.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 241,310.00 USD | 0.00 USD | 9,010.00 USD | `-15.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.45` | 232,300.00 USD | 0.00 USD | 518.80 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 231,780.00 USD | 0.00 USD | 19,590.00 USD | `-13.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 212,190.00 USD | 0.00 USD | 504.70 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 211,680.00 USD | 0.00 USD | 3,070.00 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 208,610.00 USD | 0.00 USD | 24,100.00 USD | `-10.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 184,510.00 USD | 0.00 USD | 3,450.00 USD | `-9.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 181,070.00 USD | 0.00 USD | 47,890.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 133,180.00 USD | 0.00 USD | 5,650.00 USD | `-7.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 127,520.00 USD | 0.00 USD | 30,030.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 97,490.00 USD | 0.00 USD | 3,480.00 USD | `-5.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 94,010.00 USD | 0.00 USD | 18,670.00 USD | `-5.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 75,340.00 USD | 0.00 USD | 23,690.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 51,660.00 USD | 0.00 USD | 5,170.00 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 46,490.00 USD | 0.00 USD | 28,310.00 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 18,180.00 USD | 0.00 USD | 15,000.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 3,180.00 USD | 0.00 USD | 3,180.00 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 5,030.00 USD | 5,030.00 USD | 0.00 USD | `+0.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 10,580.00 USD | 5,550.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 37,630.00 USD | 27,050.00 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 54,340.00 USD | 16,710.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 58,540.00 USD | 4,190.00 USD | 0.00 USD | `+4.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 84,410.00 USD | 25,870.00 USD | 0.00 USD | `+4.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 87,250.00 USD | 2,840.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 88,880.00 USD | 1,630.00 USD | 0.00 USD | `+6.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 96,010.00 USD | 7,130.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 100,300.00 USD | 4,300.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 130,580.00 USD | 30,280.00 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 132,510.00 USD | 1,930.00 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 225,800.00 USD | 93,280.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 226,390.00 USD | 597.74 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 231,050.00 USD | 4,650.00 USD | 0.00 USD | `+13.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 233,540.00 USD | 2,500.00 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 239,720.00 USD | 6,180.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 240,400.00 USD | 679.57 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 260,770.00 USD | 20,360.00 USD | 0.00 USD | `+16.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 261,220.00 USD | 451.95 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 279,420.00 USD | 18,200.00 USD | 0.00 USD | `+18.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 280,340.00 USD | 919.19 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 281,660.00 USD | 1,320.00 USD | 0.00 USD | `+20.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 289,440.00 USD | 7,790.00 USD | 0.00 USD | `+21.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 291,980.00 USD | 2,540.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 293,450.00 USD | 1,470.00 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 294,400.00 USD | 954.14 USD | 0.00 USD | `+24.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 313,950.00 USD | 19,550.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 319,590.00 USD | 5,640.00 USD | 0.00 USD | `+25.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 319,860.00 USD | 266.44 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 336,120.00 USD | 16,260.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 336,280.00 USD | 152.82 USD | 0.00 USD | `+28.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.25` | 340,550.00 USD | 4,280.00 USD | 0.00 USD | `+29.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 343,960.00 USD | 3,410.00 USD | 0.00 USD | `+30.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.45` | 357,630.00 USD | 13,670.00 USD | 0.00 USD | `+31.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 357,840.00 USD | 218.25 USD | 0.00 USD | `+32.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 359,700.00 USD | 1,850.00 USD | 0.00 USD | `+33.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 366,960.00 USD | 7,270.00 USD | 0.00 USD | `+34.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 367,910.00 USD | 950.82 USD | 0.00 USD | `+35.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 393,610.00 USD | 25,700.00 USD | 0.00 USD | `+36.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 396,060.00 USD | 2,450.00 USD | 0.00 USD | `+37.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 633,370.00 USD | 237,310.00 USD | 0.00 USD | `+38.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 634,290.00 USD | 924.07 USD | 0.00 USD | `+39.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 635,190.00 USD | 893.01 USD | 0.00 USD | `+40.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 659,930.00 USD | 24,740.00 USD | 0.00 USD | `+41.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 660,170.00 USD | 237.88 USD | 0.00 USD | `+42.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 663,460.00 USD | 3,290.00 USD | 0.00 USD | `+43.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 666,630.00 USD | 3,170.00 USD | 0.00 USD | `+44.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 671,760.00 USD | 5,130.00 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 687,200.00 USD | 15,440.00 USD | 0.00 USD | `+45.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 694,010.00 USD | 6,800.00 USD | 0.00 USD | `+46.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 700,510.00 USD | 6,500.00 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 707,050.00 USD | 6,540.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 713,630.00 USD | 6,580.00 USD | 0.00 USD | `+49.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 723,560.00 USD | 9,930.00 USD | 0.00 USD | `+50.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 827,540.00 USD | 103,980.00 USD | 0.00 USD | `+51.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 841,770.00 USD | 14,240.00 USD | 0.00 USD | `+52.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 926,130.00 USD | 84,360.00 USD | 0.00 USD | `+53.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 927,820.00 USD | 1,700.00 USD | 0.00 USD | `+54.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 935,190.00 USD | 7,370.00 USD | 0.00 USD | `+54.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 936,900.00 USD | 1,710.00 USD | 0.00 USD | `+55.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 939,210.00 USD | 2,300.00 USD | 0.00 USD | `+56.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 940,940.00 USD | 1,740.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 963,510.00 USD | 22,560.00 USD | 0.00 USD | `+58.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 967,890.00 USD | 4,390.00 USD | 0.00 USD | `+59.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 972,310.00 USD | 4,410.00 USD | 0.00 USD | `+60.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 976,740.00 USD | 4,440.00 USD | 0.00 USD | `+61.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 981,210.00 USD | 4,460.00 USD | 0.00 USD | `+62.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 981,650.00 USD | 448.75 USD | 0.00 USD | `+63.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,010,000.00 USD | 30,960.00 USD | 0.00 USD | `+64.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,010,000.00 USD | 453.75 USD | 0.00 USD | `+64.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,010,000.00 USD | 456.25 USD | 0.00 USD | `+65.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,010,000.00 USD | 458.75 USD | 0.00 USD | `+66.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,010,000.00 USD | 461.25 USD | 0.00 USD | `+67.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,020,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,020,000.00 USD | 466.25 USD | 0.00 USD | `+69.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,020,000.00 USD | 468.75 USD | 0.00 USD | `+70.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,020,000.00 USD | 471.25 USD | 0.00 USD | `+71.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,020,000.00 USD | 473.75 USD | 0.00 USD | `+72.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,090,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,090,000.00 USD | 574.50 USD | 0.00 USD | `+74.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,090,000.00 USD | 577.50 USD | 0.00 USD | `+74.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,090,000.00 USD | 2,710.00 USD | 0.00 USD | `+75.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,090,000.00 USD | 972.50 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,100,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,100,000.00 USD | 786.00 USD | 0.00 USD | `+78.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,100,000.00 USD | 790.00 USD | 0.00 USD | `+79.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,100,000.00 USD | 992.50 USD | 0.00 USD | `+80.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,100,000.00 USD | 997.50 USD | 0.00 USD | `+81.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,710,000.00 USD | 1,600,000.00 USD | 0.00 USD | `+82.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,710,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+84.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,710,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+86.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,710,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,710,000.00 USD | 1,040.00 USD | 0.00 USD | `+88.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,720,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,720,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,720,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,720,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,770,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+93.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,770,000.00 USD | 1,070.00 USD | 0.00 USD | `+94.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+95.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,770,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,770,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,780,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `22.05` | 3,780,000.00 USD | 1,100.00 USD | 0.00 USD | `+100.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.32` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 36,970.00 USD | 23,560.00 USD | 18,440.00 USD |
| `7D` | `9.34` | 13,430,000.00 USD | 0.00 USD | 13,430,000.00 USD | 27,630.00 USD | 8,000.00 USD | 6,840.00 USD |
| `7D` | `9.36` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 312.15 USD | 1,970.00 USD | 4,300.00 USD |
| `7D` | `9.38` | 13,380,000.00 USD | 0.00 USD | 13,380,000.00 USD | 13,520.00 USD | 7,170.00 USD | 10,370.00 USD |
| `7D` | `9.40` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 25,110.00 USD | 6,630.00 USD | 3,030.00 USD |
| `7D` | `9.42` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 7,360.00 USD | 4,610.00 USD | 33,660.00 USD |
| `7D` | `9.44` | 13,270,000.00 USD | 0.00 USD | 13,270,000.00 USD | 6,610.00 USD | 1,700.00 USD | 48,400.00 USD |
| `7D` | `9.46` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 94,230.00 USD | 0.00 USD | 217.03 USD |
| `7D` | `9.48` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 133.83 USD | 1,630.00 USD | 2,560.00 USD |
| `7D` | `9.50` | 13,110,000.00 USD | 0.00 USD | 13,110,000.00 USD | 58,490.00 USD | 1,680.00 USD | 2,880.00 USD |
| `7D` | `9.52` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 0.00 USD | 911.85 USD | 0.00 USD |
| `7D` | `9.54` | 13,050,000.00 USD | 0.00 USD | 13,050,000.00 USD | 136.92 USD | 12,570.00 USD | 10.22 USD |
| `7D` | `9.56` | 13,040,000.00 USD | 0.00 USD | 13,040,000.00 USD | 160.73 USD | 16,080.00 USD | 71,150.00 USD |
| `7D` | `9.58` | 12,950,000.00 USD | 0.00 USD | 12,950,000.00 USD | 38,760.00 USD | 722.15 USD | 20.74 USD |
| `7D` | `9.60` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 62,800.00 USD | 1,030.00 USD | 136,130.00 USD |
| `7D` | `9.62` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 0.00 USD | 0.00 USD | 212.33 USD |
| `7D` | `9.64` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 8,500.00 USD | 2,560.00 USD | 6,100.00 USD |
| `7D` | `9.66` | 12,690,000.00 USD | 0.00 USD | 12,690,000.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.68` | 12,680,000.00 USD | 0.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 31,480.00 USD |
| `7D` | `9.70` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 7,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.72` | 12,650,000.00 USD | 0.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 28,610.00 USD |
| `7D` | `9.74` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 2,070.00 USD | 0.00 USD | 487.81 USD |
| `7D` | `9.76` | 12,610,000.00 USD | 0.00 USD | 12,610,000.00 USD | 50,080.00 USD | 0.00 USD | 27,090.00 USD |
| `7D` | `9.78` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 0.00 USD | 671.70 USD | 475.94 USD |
| `7D` | `9.80` | 12,540,000.00 USD | 0.00 USD | 12,540,000.00 USD | 47,490.00 USD | 14,120.00 USD | 26,150.00 USD |
| `7D` | `9.82` | 12,450,000.00 USD | 0.00 USD | 12,450,000.00 USD | 84,900.00 USD | 10,390.00 USD | 0.00 USD |
| `7D` | `9.84` | 12,350,000.00 USD | 0.00 USD | 12,350,000.00 USD | 50,980.00 USD | 456.90 USD | 13,350.00 USD |
| `1D` | `9.86` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 29,590.00 USD | 11,010.00 USD | 11,110.00 USD |
| `7D` | `9.86` | 12,290,000.00 USD | 0.00 USD | 12,290,000.00 USD | 5,390.00 USD | 14,570.00 USD | 118.03 USD |
| `1D` | `9.88` | 8,950,000.00 USD | 0.00 USD | 8,950,000.00 USD | 6,450.00 USD | 14,200.00 USD | 9,220.00 USD |
| `7D` | `9.88` | 12,270,000.00 USD | 0.00 USD | 12,270,000.00 USD | 10,280.00 USD | 15,600.00 USD | 418.53 USD |
| `1D` | `9.90` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 39,790.00 USD | 32,360.00 USD | 12,610.00 USD |
| `7D` | `9.90` | 12,240,000.00 USD | 0.00 USD | 12,240,000.00 USD | 48,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.92` | 8,840,000.00 USD | 0.00 USD | 8,840,000.00 USD | 23,540.00 USD | 20,070.00 USD | 118.68 USD |
| `7D` | `9.92` | 12,190,000.00 USD | 0.00 USD | 12,190,000.00 USD | 0.00 USD | 12,280.00 USD | 650.74 USD |
| `1D` | `9.94` | 8,800,000.00 USD | 0.00 USD | 8,800,000.00 USD | 1,960.00 USD | 5,150.00 USD | 101.06 USD |
| `7D` | `9.94` | 12,180,000.00 USD | 0.00 USD | 12,180,000.00 USD | 15,590.00 USD | 60,600.00 USD | 26,390.00 USD |
| `1D` | `9.96` | 8,790,000.00 USD | 0.00 USD | 8,790,000.00 USD | 75,160.00 USD | 15,490.00 USD | 26,050.00 USD |
| `7D` | `9.96` | 12,080,000.00 USD | 0.00 USD | 12,080,000.00 USD | 17,170.00 USD | 11,410.00 USD | 12,480.00 USD |
| `1D` | `9.98` | 8,670,000.00 USD | 0.00 USD | 8,670,000.00 USD | 37,260.00 USD | 6,830.00 USD | 68,220.00 USD |
| `7D` | `9.98` | 12,040,000.00 USD | 0.00 USD | 12,040,000.00 USD | 4,830.00 USD | 598.17 USD | 60,020.00 USD |
| `1D` | `10.00` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 5,550.00 USD | 1,860.00 USD | 60,600.00 USD |
| `7D` | `10.00` | 11,970,000.00 USD | 0.00 USD | 11,970,000.00 USD | 0.00 USD | 7,630.00 USD | 12,870.00 USD |
| `1D` | `10.02` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 10,700.00 USD | 19,650.00 USD | 18,520.00 USD |
| `7D` | `10.02` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 8,880.00 USD | 317.30 USD | 506.80 USD |
| `1D` | `10.04` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 18,000.00 USD | 1,900.00 USD | 264.22 USD |
| `7D` | `10.04` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 7,200.00 USD | 1,210.00 USD | 154.66 USD |
| `1D` | `10.06` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 25,040.00 USD | 3,280.00 USD | 47,130.00 USD |
| `7D` | `10.06` | 11,930,000.00 USD | 0.00 USD | 11,930,000.00 USD | 0.00 USD | 0.00 USD | 83,590.00 USD |
| `1D` | `10.08` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 167,250.00 USD | 701.42 USD | 76,080.00 USD |
| `7D` | `10.08` | 11,850,000.00 USD | 0.00 USD | 11,850,000.00 USD | 218,980.00 USD | 351.10 USD | 110,480.00 USD |
| `1D` | `10.10` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 7,570.00 USD | 42,810.00 USD | 288.89 USD |
| `7D` | `10.10` | 11,520,000.00 USD | 0.00 USD | 11,520,000.00 USD | 6,580.00 USD | 0.00 USD | 251.39 USD |
| `1D` | `10.12` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 1,150.00 USD | 20,910.00 USD | 0.00 USD |
| `7D` | `10.12` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 10,140.00 USD | 559.40 USD | 55,910.00 USD |
| `1D` | `10.14` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 17,140.00 USD | 12,730.00 USD | 34,520.00 USD |
| `7D` | `10.14` | 11,450,000.00 USD | 0.00 USD | 11,450,000.00 USD | 174,100.00 USD | 71,300.00 USD | 74,260.00 USD |
| `1D` | `10.16` | 7,970,000.00 USD | 0.00 USD | 7,970,000.00 USD | 61,120.00 USD | 18,510.00 USD | 38,610.00 USD |
| `7D` | `10.16` | 11,130,000.00 USD | 0.00 USD | 11,130,000.00 USD | 20,010.00 USD | 13,680.00 USD | 10,760.00 USD |
| `1D` | `10.18` | 7,850,000.00 USD | 0.00 USD | 7,850,000.00 USD | 80,470.00 USD | 36,910.00 USD | 156,200.00 USD |
| `7D` | `10.18` | 11,080,000.00 USD | 0.00 USD | 11,080,000.00 USD | 70,160.00 USD | 31,470.00 USD | 31,630.00 USD |
| `1D` | `10.20` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 200,530.00 USD | 44,960.00 USD | 233,090.00 USD |
| `7D` | `10.20` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 129,300.00 USD | 55,910.00 USD | 335,630.00 USD |
| `1D` | `10.22` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 37,870.00 USD | 22,280.00 USD | 339,790.00 USD |
| `7D` | `10.22` | 10,430,000.00 USD | 0.00 USD | 10,430,000.00 USD | 258,900.00 USD | 30,360.00 USD | 253,070.00 USD |
| `1D` | `10.24` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 110,620.00 USD | 66,260.00 USD | 14,590.00 USD |
| `7D` | `10.24` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 160,020.00 USD | 39,580.00 USD | 247,540.00 USD |
| `1D` | `10.26` | 6,500,000.00 USD | 0.00 USD | 6,500,000.00 USD | 63,830.00 USD | 8,070.00 USD | 100,930.00 USD |
| `7D` | `10.26` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 41,640.00 USD | 34,680.00 USD | 305,470.00 USD |
| `1D` | `10.28` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 164,310.00 USD | 11,970.00 USD | 168,690.00 USD |
| `7D` | `10.28` | 9,060,000.00 USD | 0.00 USD | 9,060,000.00 USD | 81,210.00 USD | 10,410.00 USD | 242,490.00 USD |
| `1D` | `10.30` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 166,480.00 USD | 20,900.00 USD | 39,850.00 USD |
| `7D` | `10.30` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 458,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.32` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 12,090.00 USD | 1,310.00 USD | 71,710.00 USD |
| `7D` | `10.32` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 43,210.00 USD | 0.00 USD | 99,850.00 USD |
| `1D` | `10.34` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 66,010.00 USD | 9,100.00 USD | 86,060.00 USD |
| `7D` | `10.34` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 58,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.36` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 5,630.00 USD | 3,580.00 USD | 39.63 USD |
| `7D` | `10.36` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 294,520.00 USD | 0.00 USD | 103,760.00 USD |
| `1D` | `10.38` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 41,250.00 USD | 45,170.00 USD | 7,590.00 USD |
| `7D` | `10.38` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 7,980.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.40` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 88,080.00 USD | 31,210.00 USD | 66,800.00 USD |
| `7D` | `10.40` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 168,140.00 USD | 21,690.00 USD | 160,120.00 USD |
| `1D` | `10.42` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 247,240.00 USD | 0.00 USD | 136.88 USD |
| `7D` | `10.42` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 229,660.00 USD | 97,940.00 USD | 236.06 USD |
| `1D` | `10.44` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 200,830.00 USD | 27,590.00 USD | 305,440.00 USD |
| `7D` | `10.44` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 439,060.00 USD | 13,410.00 USD | 333,920.00 USD |
| `1D` | `10.46` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 276,000.00 USD | 31,370.00 USD | 18,120.00 USD |
| `7D` | `10.46` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 323,570.00 USD | 103,810.00 USD | 0.00 USD |
| `1D` | `10.48` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 51,060.00 USD | 2,200.00 USD | 55,100.00 USD |
| `7D` | `10.48` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 61,110.00 USD | 15,720.00 USD | 137,720.00 USD |
| `1D` | `10.50` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,230.00 USD | 36,830.00 USD | 25,170.00 USD |
| `7D` | `10.50` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 4,770.00 USD | 52,370.00 USD | 0.00 USD |
| `1D` | `10.52` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 668.27 USD | 12,710.00 USD | 38,150.00 USD |
| `7D` | `10.52` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 2,370.00 USD | 8,750.00 USD | 0.00 USD |
| `1D` | `10.54` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 15,560.00 USD | 72,720.00 USD | 153,390.00 USD |
| `7D` | `10.54` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 0.00 USD | 72,670.00 USD | 0.00 USD |
| `1D` | `10.56` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 108,320.00 USD | 38,520.00 USD | 37,770.00 USD |
| `7D` | `10.56` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 121,680.00 USD | 81,670.00 USD | 0.00 USD |
| `1D` | `10.58` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 54,810.00 USD | 32,040.00 USD | 22,000.00 USD |
| `7D` | `10.58` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 23,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.60` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 12,130.00 USD | 25,180.00 USD | 1,950.00 USD |
| `7D` | `10.60` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 0.00 USD | 24,130.00 USD | 458.05 USD |
| `1D` | `10.62` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 47,240.00 USD | 8,940.00 USD | 136,030.00 USD |
| `7D` | `10.62` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 99,990.00 USD | 0.00 USD | 180.54 USD |
| `1D` | `10.64` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 109,830.00 USD | 9,030.00 USD | 56,100.00 USD |
| `7D` | `10.64` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 11,150.00 USD | 0.00 USD | 28,630.00 USD |
| `1D` | `10.66` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 59,930.00 USD | 7,540.00 USD | 29,670.00 USD |
| `7D` | `10.66` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 9,470.00 USD | 0.00 USD | 146.60 USD |
| `1D` | `10.68` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 49,800.00 USD | 28,300.00 USD | 60,690.00 USD |
| `7D` | `10.68` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 21,500.00 USD | 0.00 USD |
| `1D` | `10.70` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 12,670.00 USD | 14,170.00 USD | 0.00 USD |
| `7D` | `10.70` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 15,010.00 USD | 0.00 USD |
| `1D` | `10.72` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 28,630.00 USD | 85,810.00 USD | 97,270.00 USD |
| `7D` | `10.72` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 433,250.00 USD | 73,710.00 USD | 0.00 USD |
| `1D` | `10.74` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 83,030.00 USD | 27,290.00 USD | 0.00 USD |
| `7D` | `10.74` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 877.75 USD | 99,850.00 USD |
| `1D` | `10.76` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 35,390.00 USD | 78,570.00 USD | 68,800.00 USD |
| `7D` | `10.76` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 16,310.00 USD | 120,930.00 USD | 0.00 USD |
| `1D` | `10.78` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 214,110.00 USD | 164,040.00 USD | 75,550.00 USD |
| `7D` | `10.78` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 535,020.00 USD | 46,010.00 USD | 103,760.00 USD |
| `1D` | `10.80` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 66,060.00 USD | 27,700.00 USD | 13,640.00 USD |
| `7D` | `10.80` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 69,540.00 USD | 70,260.00 USD | 0.00 USD |
| `1D` | `10.82` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 112,330.00 USD | 43,640.00 USD | 3,800.00 USD |
| `7D` | `10.82` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 104,870.00 USD | 206,380.00 USD |
| `1D` | `10.84` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 402,600.00 USD | 13,510.00 USD | 35,630.00 USD |
| `7D` | `10.84` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 377,580.00 USD | 80,420.00 USD | 196,240.00 USD |
| `1D` | `10.86` | 998,620.00 USD | 0.00 USD | 998,620.00 USD | 203,140.00 USD | 34,420.00 USD | 213,120.00 USD |
| `7D` | `10.86` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 323,850.00 USD | 3,610.00 USD | 390,880.00 USD |
| `1D` | `10.88` | 547,940.00 USD | 0.00 USD | 547,940.00 USD | 61,520.00 USD | 9,550.00 USD | 59,460.00 USD |
| `7D` | `10.88` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 111,430.00 USD | 39,120.00 USD | 346,720.00 USD |
| `1D` | `10.90` | 417,410.00 USD | 0.00 USD | 417,410.00 USD | 114,210.00 USD | 35,090.00 USD | 48,990.00 USD |
| `7D` | `10.90` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 0.00 USD | 38,140.00 USD | 220,890.00 USD |
| `1D` | `10.92` | 219,110.00 USD | 0.00 USD | 219,110.00 USD | 103,270.00 USD | 19,240.00 USD | 86.22 USD |
| `7D` | `10.92` | 960,920.00 USD | 0.00 USD | 960,920.00 USD | 226,910.00 USD | 0.00 USD | 110,480.00 USD |
| `1D` | `10.94` | 96,520.00 USD | 0.00 USD | 96,520.00 USD | 4,370.00 USD | 1,550.00 USD | 0.00 USD |
| `7D` | `10.94` | 623,540.00 USD | 0.00 USD | 623,540.00 USD | 2,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 90,600.00 USD | 0.00 USD | 90,600.00 USD | 0.00 USD | 0.00 USD | 87,750.00 USD |
| `7D` | `10.96` | 621,060.00 USD | 0.00 USD | 621,060.00 USD | 10,430.00 USD | 0.00 USD | 49,920.00 USD |
| `7D` | `10.98` | 560,710.00 USD | 0.00 USD | 560,710.00 USD | 17,930.00 USD | 0.00 USD | 209,290.00 USD |
| `1D` | `11.00` | 2,840.00 USD | 0.00 USD | 2,840.00 USD | 0.00 USD | 0.00 USD | 103.72 USD |
| `7D` | `11.00` | 333,490.00 USD | 0.00 USD | 333,490.00 USD | 10,830.00 USD | 0.00 USD | 634.90 USD |
| `7D` | `11.02` | 322,020.00 USD | 0.00 USD | 322,020.00 USD | 0.00 USD | 0.00 USD | 143,500.00 USD |
| `1D` | `11.04` | 2,740.00 USD | 0.00 USD | 2,740.00 USD | 0.00 USD | 2,200.00 USD | 402.88 USD |
| `7D` | `11.04` | 178,530.00 USD | 0.00 USD | 178,530.00 USD | 0.00 USD | 0.00 USD | 178,530.00 USD |
| `1D` | `11.06` | 135.97 USD | 0.00 USD | 135.97 USD | 0.00 USD | 0.00 USD | 135.97 USD |
| `7D` | `11.06` | 132,650.00 USD | 132,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD |
| `7D` | `11.06` | 265,310.00 USD | 265,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132,650.00 USD |
| `1D` | `11.07` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.08` | 267,620.00 USD | 267,620.00 USD | 0.00 USD | 0.00 USD | 1,810.00 USD | 506.80 USD |
| `1D` | `11.10` | 7,750.00 USD | 7,750.00 USD | 0.00 USD | 7,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.10` | 645,570.00 USD | 645,570.00 USD | 0.00 USD | 282,040.00 USD | 6,920.00 USD | 88,980.00 USD |
| `1D` | `11.12` | 152,600.00 USD | 152,600.00 USD | 0.00 USD | 6,320.00 USD | 2,260.00 USD | 136,280.00 USD |
| `7D` | `11.12` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 261,760.00 USD | 5,170.00 USD | 234,170.00 USD |
| `1D` | `11.14` | 225,650.00 USD | 225,650.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD | 68,140.00 USD |
| `7D` | `11.14` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 204,650.00 USD | 9,980.00 USD | 487.81 USD |
| `1D` | `11.16` | 405,030.00 USD | 405,030.00 USD | 0.00 USD | 127,020.00 USD | 2,100.00 USD | 50,270.00 USD |
| `7D` | `11.16` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 131,250.00 USD | 72,860.00 USD | 65,260.00 USD |
| `1D` | `11.18` | 577,410.00 USD | 577,410.00 USD | 0.00 USD | 71,610.00 USD | 14,380.00 USD | 86,390.00 USD |
| `7D` | `11.18` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 3,130.00 USD | 13,890.00 USD | 475.94 USD |
| `1D` | `11.20` | 830,900.00 USD | 830,900.00 USD | 0.00 USD | 76,580.00 USD | 85,800.00 USD | 91,110.00 USD |
| `7D` | `11.20` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 171,840.00 USD | 89,800.00 USD | 79,190.00 USD |
| `1D` | `11.22` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 344,290.00 USD | 76,600.00 USD | 142,440.00 USD |
| `7D` | `11.22` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 482,460.00 USD | 42,050.00 USD | 603.14 USD |
| `1D` | `11.24` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 163,340.00 USD | 58,590.00 USD | 155,350.00 USD |
| `7D` | `11.24` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 231,960.00 USD | 59,950.00 USD | 71,520.00 USD |
| `1D` | `11.26` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 154,720.00 USD | 54,310.00 USD | 71,490.00 USD |
| `7D` | `11.26` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 520,990.00 USD | 48,250.00 USD | 296,010.00 USD |
| `1D` | `11.28` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 388,220.00 USD | 67,290.00 USD | 263,100.00 USD |
| `7D` | `11.28` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 429,350.00 USD | 57,050.00 USD | 147,810.00 USD |
| `1D` | `11.30` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 261,740.00 USD | 81,010.00 USD | 153,180.00 USD |
| `7D` | `11.30` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 24,980.00 USD | 32,240.00 USD | 77,570.00 USD |
| `1D` | `11.32` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 181,160.00 USD | 67,470.00 USD | 142,340.00 USD |
| `7D` | `11.32` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 194,150.00 USD | 23,000.00 USD | 279,600.00 USD |
| `1D` | `11.34` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 390,100.00 USD | 114,410.00 USD | 107,170.00 USD |
| `7D` | `11.34` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 127,190.00 USD | 116,400.00 USD | 101,390.00 USD |
| `1D` | `11.36` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 138,710.00 USD | 95,240.00 USD | 56,330.00 USD |
| `7D` | `11.36` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 107,330.00 USD | 93,800.00 USD | 56,770.00 USD |
| `1D` | `11.38` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 118,230.00 USD | 85,980.00 USD | 25,380.00 USD |
| `7D` | `11.38` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 70,120.00 USD | 91,810.00 USD | 75,030.00 USD |
| `1D` | `11.40` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 39,080.00 USD | 34,800.00 USD | 104,510.00 USD |
| `7D` | `11.40` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 14,250.00 USD | 28,930.00 USD |
| `1D` | `11.42` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 126,960.00 USD | 83,740.00 USD | 113,690.00 USD |
| `7D` | `11.42` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 66,800.00 USD | 46,660.00 USD | 115,000.00 USD |
| `1D` | `11.44` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 96,590.00 USD | 54,990.00 USD | 109,190.00 USD |
| `7D` | `11.44` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 303,190.00 USD | 101,940.00 USD | 38,210.00 USD |
| `1D` | `11.46` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 86,190.00 USD | 77,320.00 USD | 50,780.00 USD |
| `7D` | `11.46` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 122,890.00 USD | 55,470.00 USD | 269.04 USD |
| `1D` | `11.48` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 26,740.00 USD | 35,780.00 USD | 1,910.00 USD |
| `7D` | `11.48` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 54,660.00 USD | 108,960.00 USD | 64,610.00 USD |
| `1D` | `11.50` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 78,340.00 USD | 38,760.00 USD | 63,740.00 USD |
| `7D` | `11.50` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 132,730.00 USD | 38,570.00 USD | 0.00 USD |
| `1D` | `11.52` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 127,920.00 USD | 22,260.00 USD | 52,220.00 USD |
| `7D` | `11.52` | 7,210,000.00 USD | 7,210,000.00 USD | 0.00 USD | 0.00 USD | 5,760.00 USD | 62,260.00 USD |
| `1D` | `11.54` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 92,850.00 USD | 20,290.00 USD | 101,050.00 USD |
| `7D` | `11.54` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 53,520.00 USD | 0.00 USD | 108,670.00 USD |
| `1D` | `11.56` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 128,820.00 USD | 20,640.00 USD | 47,760.00 USD |
| `7D` | `11.56` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 86,650.00 USD | 19,860.00 USD | 432.76 USD |
| `1D` | `11.58` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 58,870.00 USD | 2,950.00 USD | 17,790.00 USD |
| `7D` | `11.58` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 31,620.00 USD |
| `1D` | `11.60` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 59,780.00 USD | 14,330.00 USD | 67,580.00 USD |
| `7D` | `11.60` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 46,010.00 USD | 10,510.00 USD | 23,030.00 USD |
| `1D` | `11.62` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 44,730.00 USD | 512.95 USD | 48,190.00 USD |
| `7D` | `11.62` | 7,660,000.00 USD | 7,660,000.00 USD | 0.00 USD | 65,150.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.64` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 5,660.00 USD | 7,410.00 USD | 31,250.00 USD |
| `7D` | `11.64` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 39,380.00 USD | 1,790.00 USD | 508.36 USD |
| `1D` | `11.66` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 228.94 USD | 12,290.00 USD | 25,690.00 USD |
| `7D` | `11.66` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | 80,090.00 USD |
| `1D` | `11.68` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 126,110.00 USD | 35,770.00 USD | 31,850.00 USD |
| `7D` | `11.68` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 20,730.00 USD | 71,150.00 USD |
| `1D` | `11.70` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 239.66 USD | 4,760.00 USD | 15,790.00 USD |
| `7D` | `11.70` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 38,760.00 USD | 722.15 USD | 176.96 USD |
| `1D` | `11.72` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 91,840.00 USD | 17,160.00 USD | 98,120.00 USD |
| `7D` | `11.72` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 209,440.00 USD | 0.00 USD | 116,640.00 USD |
| `1D` | `11.74` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 76,690.00 USD | 30,280.00 USD | 73,130.00 USD |
| `7D` | `11.74` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 1,030.00 USD | 90,020.00 USD |
| `1D` | `11.76` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 26,330.00 USD | 14,880.00 USD | 24,830.00 USD |
| `7D` | `11.76` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 52,910.00 USD | 27,570.00 USD | 20,500.00 USD |
| `1D` | `11.78` | 7,760,000.00 USD | 7,760,000.00 USD | 0.00 USD | 11,750.00 USD | 20,510.00 USD | 40,030.00 USD |
| `7D` | `11.78` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 9,130.00 USD | 0.00 USD | 56,750.00 USD |
| `1D` | `11.80` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 1,350.00 USD | 18,000.00 USD | 531.07 USD |
| `7D` | `11.80` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 140,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 12,210.00 USD | 53.10 USD | 36,070.00 USD |
| `7D` | `11.82` | 8,880,000.00 USD | 8,880,000.00 USD | 0.00 USD | 182,750.00 USD | 41,910.00 USD | 0.00 USD |
| `1D` | `11.84` | 7,930,000.00 USD | 7,930,000.00 USD | 0.00 USD | 43,880.00 USD | 11,870.00 USD | 45,600.00 USD |
| `7D` | `11.84` | 9,130,000.00 USD | 9,130,000.00 USD | 0.00 USD | 178,690.00 USD | 40,640.00 USD | 31,750.00 USD |
| `1D` | `11.86` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 10,930.00 USD | 12,970.00 USD | 51,000.00 USD |
| `7D` | `11.86` | 9,140,000.00 USD | 9,140,000.00 USD | 0.00 USD | 0.00 USD | 6,180.00 USD | 50.72 USD |
| `1D` | `11.88` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 20,950.00 USD | 28,990.00 USD | 60,210.00 USD |
| `7D` | `11.88` | 9,200,000.00 USD | 9,200,000.00 USD | 0.00 USD | 10,340.00 USD | 1,710.00 USD | 51,860.00 USD |
| `1D` | `11.90` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 43,700.00 USD | 8,690.00 USD | 28,000.00 USD |
| `7D` | `11.90` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 40,470.00 USD | 14,650.00 USD | 98.18 USD |
| `1D` | `11.92` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 230,070.00 USD | 22,930.00 USD | 25,120.00 USD |
| `7D` | `11.92` | 9,470,000.00 USD | 9,470,000.00 USD | 0.00 USD | 130,170.00 USD | 14,370.00 USD | 65,810.00 USD |
| `1D` | `11.94` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 48,030.00 USD | 15,260.00 USD | 40,220.00 USD |
| `7D` | `11.94` | 9,660,000.00 USD | 9,660,000.00 USD | 0.00 USD | 17,060.00 USD | 24,020.00 USD | 148,320.00 USD |
| `1D` | `11.96` | 8,730,000.00 USD | 8,730,000.00 USD | 0.00 USD | 64,110.00 USD | 40,070.00 USD | 48,040.00 USD |
| `7D` | `11.96` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 13,850.00 USD | 2,170.00 USD | 162,200.00 USD |
| `1D` | `11.98` | 8,890,000.00 USD | 8,890,000.00 USD | 0.00 USD | 59,940.00 USD | 29,050.00 USD | 68,170.00 USD |
| `7D` | `11.98` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 393,900.00 USD | 48,820.00 USD | 215,650.00 USD |
| `1D` | `12.00` | 9,050,000.00 USD | 9,050,000.00 USD | 0.00 USD | 102,680.00 USD | 23,880.00 USD | 36,270.00 USD |
| `7D` | `12.00` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 379,630.00 USD | 31,630.00 USD | 222,020.00 USD |
| `1D` | `12.02` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 13,680.00 USD | 9,340.00 USD | 31,440.00 USD |
| `7D` | `12.02` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 288,770.00 USD | 47,870.00 USD | 235,330.00 USD |
| `1D` | `12.04` | 9,290,000.00 USD | 9,290,000.00 USD | 0.00 USD | 90,410.00 USD | 39,490.00 USD | 56,310.00 USD |
| `7D` | `12.04` | 12,320,000.00 USD | 12,320,000.00 USD | 0.00 USD | 292,690.00 USD | 151,910.00 USD | 179,840.00 USD |
| `1D` | `12.06` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 76,750.00 USD | 43,270.00 USD | 69,920.00 USD |
| `7D` | `12.06` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 237,300.00 USD | 121,530.00 USD | 145,810.00 USD |
| `1D` | `12.08` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 43,090.00 USD | 40,800.00 USD | 52,270.00 USD |
| `7D` | `12.08` | 13,490,000.00 USD | 13,490,000.00 USD | 0.00 USD | 375,670.00 USD | 121,690.00 USD | 165,280.00 USD |
| `1D` | `12.10` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 50,850.00 USD | 25,300.00 USD | 34,770.00 USD |
| `7D` | `12.10` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 81,060.00 USD | 75,230.00 USD | 26,160.00 USD |
| `1D` | `12.12` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 116,870.00 USD | 54,580.00 USD | 50,650.00 USD |
| `7D` | `12.12` | 14,060,000.00 USD | 14,060,000.00 USD | 0.00 USD | 174,090.00 USD | 79,520.00 USD | 130,690.00 USD |
| `1D` | `12.14` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 75,920.00 USD | 37,540.00 USD | 55,700.00 USD |
| `7D` | `12.14` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 148,090.00 USD | 102,170.00 USD | 119,290.00 USD |
| `1D` | `12.16` | 10,360,000.00 USD | 10,360,000.00 USD | 0.00 USD | 132,030.00 USD | 34,710.00 USD | 67,620.00 USD |
| `7D` | `12.16` | 14,750,000.00 USD | 14,750,000.00 USD | 0.00 USD | 182,020.00 USD | 69,310.00 USD | 75,200.00 USD |
| `1D` | `12.18` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 112,670.00 USD | 48,310.00 USD | 50,430.00 USD |
| `7D` | `12.18` | 14,930,000.00 USD | 14,930,000.00 USD | 0.00 USD | 74,850.00 USD | 54,220.00 USD | 43,550.00 USD |
| `1D` | `12.20` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 77,250.00 USD | 43,870.00 USD | 41,740.00 USD |
| `7D` | `12.20` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 194,760.00 USD | 51,940.00 USD | 75,220.00 USD |
| `1D` | `12.22` | 10,790,000.00 USD | 10,790,000.00 USD | 0.00 USD | 10,400.00 USD | 17,890.00 USD | 32,260.00 USD |
| `7D` | `12.22` | 15,640,000.00 USD | 15,640,000.00 USD | 0.00 USD | 261,490.00 USD | 63,820.00 USD | 64,370.00 USD |
| `7D` | `12.24` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 50,300.00 USD | 45,440.00 USD | 10,760.00 USD |
| `7D` | `12.26` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 73,660.00 USD | 54,120.00 USD | 50,600.00 USD |
| `7D` | `12.28` | 16,200,000.00 USD | 16,200,000.00 USD | 0.00 USD | 156,680.00 USD | 27,340.00 USD | 90,380.00 USD |
| `7D` | `12.30` | 16,390,000.00 USD | 16,390,000.00 USD | 0.00 USD | 70,240.00 USD | 49,630.00 USD | 77,910.00 USD |
| `7D` | `12.32` | 16,460,000.00 USD | 16,460,000.00 USD | 0.00 USD | 22,620.00 USD | 25,760.00 USD | 17,810.00 USD |
| `7D` | `12.34` | 16,520,000.00 USD | 16,520,000.00 USD | 0.00 USD | 27,830.00 USD | 18,250.00 USD | 13,120.00 USD |
| `7D` | `12.36` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 36,210.00 USD | 23,630.00 USD | 17,600.00 USD |
| `7D` | `12.38` | 16,610,000.00 USD | 16,610,000.00 USD | 0.00 USD | 2,300.00 USD | 6,800.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `511.11M` | Total OI Tokens: `46,116,928.6 LINK`
  * 1h OI Change: `+0.63%` | 4h OI Change: `-1.57%` | 24h OI Change: `-7.06%`
  * Exchange Breakdown: Binance=`100.55M` | Bybit=`68.94M` | OKX=`26.83M` | Hyperliquid=`55.89M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.52K` | Last 24h: `20.14K` | Last 3d: `92.68K` | Last 7d: `172.86K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0069%` |
| **USDT Bybit** | `0.0020%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0051%` | **USDT Bitget** | `0.0087%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `57.07%` | `42.93%` | `1.33` | 12,040,000.00 USD |
| `15M` | `Binance` | `61.64%` | `38.36%` | `1.61` | 3,850,000.00 USD |
| `15M` | `OKX` | `49.49%` | `50.51%` | `0.98` | 1,050,000.00 USD |
| `15M` | `Bybit` | `71.6%` | `28.4%` | `2.52` | 2,040,000.00 USD |
| `15M` | `KuCoin` | `48.43%` | `51.57%` | `0.94` | 186,530.00 USD |
| `15M` | `Gate` | `36.33%` | `63.67%` | `0.57` | 485,310.00 USD |
| `15M` | `Bitget` | `59.47%` | `40.53%` | `1.47` | 396,040.00 USD |
| `15M` | `BingX` | `71.33%` | `28.67%` | `2.49` | 163,690.00 USD |
| `15M` | `MEXC` | `47.48%` | `52.52%` | `0.90` | 115,880.00 USD |
| `15M` | `Bitunix` | `52.58%` | `47.42%` | `1.11` | 145,700.00 USD |
| `15M` | `Hyperliquid` | `74.01%` | `25.99%` | `2.85` | 269,650.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.03%` | `49.97%` | `1.00` | 60,150.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 3,070,000.00 USD |
| `15M` | `HTX` | `51.98%` | `48.02%` | `1.08` | 29,190.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.44%` | `73.56%` | `0.36` | 88,870.00 USD |
| `15M` | `Aster` | `96.09%` | `3.91%` | `24.58` | 46,510.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.61%` | `73.39%` | `0.36` | 40,860.00 USD |
| `15M` | `Whale Positions` | `61.64%` | `38.36%` | `1.61` | 3,850,000.00 USD |
| `15M` | `Global Accounts` | `57.07%` | `42.93%` | `1.33` | 12,040,000.00 USD |
| `1H` | `LINK` | `47.22%` | `52.78%` | `0.89` | 22,660,000.00 USD |
| `1H` | `Binance` | `53.33%` | `46.67%` | `1.14` | 7,460,000.00 USD |
| `1H` | `OKX` | `45.87%` | `54.13%` | `0.85` | 2,010,000.00 USD |
| `1H` | `Bybit` | `52.15%` | `47.85%` | `1.09` | 1,670,000.00 USD |
| `1H` | `KuCoin` | `36.72%` | `63.28%` | `0.58` | 90,550.00 USD |
| `1H` | `Gate` | `25.31%` | `74.69%` | `0.34` | 377,580.00 USD |
| `1H` | `Bitget` | `55.84%` | `44.16%` | `1.26` | 876,320.00 USD |
| `1H` | `BingX` | `12.17%` | `87.83%` | `0.14` | 2,440,000.00 USD |
| `1H` | `MEXC` | `49.44%` | `50.56%` | `0.98` | 5,120,000.00 USD |
| `1H` | `Bitunix` | `74.85%` | `25.15%` | `2.98` | 789,170.00 USD |
| `1H` | `Hyperliquid` | `33.25%` | `66.75%` | `0.50` | 350,390.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.19%` | `49.81%` | `1.01` | 1,020,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `43.1%` | `56.9%` | `0.76` | 55,530.00 USD |
| `1H` | `HTX` | `21.88%` | `78.12%` | `0.28` | 4,870.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `53.21%` | `46.79%` | `1.14` | 300,920.00 USD |
| `1H` | `Aster` | `87.68%` | `12.32%` | `7.12` | 78,750.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.02%` | `48.98%` | `1.04` | 16,300.00 USD |
| `1H` | `Whale Positions` | `53.33%` | `46.67%` | `1.14` | 7,460,000.00 USD |
| `1H` | `Global Accounts` | `47.22%` | `52.78%` | `0.89` | 22,660,000.00 USD |
| `4H` | `LINK` | `49.67%` | `50.33%` | `0.99` | 160,830,000.00 USD |
| `4H` | `Binance` | `49.61%` | `50.39%` | `0.98` | 66,540,000.00 USD |
| `4H` | `OKX` | `47.15%` | `52.85%` | `0.89` | 19,640,000.00 USD |
| `4H` | `Bybit` | `57.18%` | `42.82%` | `1.34` | 26,140,000.00 USD |
| `4H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 3,180,000.00 USD |
| `4H` | `Gate` | `44.43%` | `55.57%` | `0.80` | 6,590,000.00 USD |
| `4H` | `Bitget` | `56.89%` | `43.11%` | `1.32` | 6,050,000.00 USD |
| `4H` | `BingX` | `27.58%` | `72.42%` | `0.38` | 2,910,000.00 USD |
| `4H` | `MEXC` | `55.14%` | `44.86%` | `1.23` | 1,450,000.00 USD |
| `4H` | `Bitunix` | `51.32%` | `48.68%` | `1.05` | 2,280,000.00 USD |
| `4H` | `Hyperliquid` | `54.53%` | `45.47%` | `1.20` | 14,930,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.22%` | `49.78%` | `1.01` | 2,050,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `16.49%` | `83.51%` | `0.20` | 5,810,000.00 USD |
| `4H` | `HTX` | `50.14%` | `49.86%` | `1.01` | 396,530.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `78.07%` | `21.93%` | `3.56` | 895,790.00 USD |
| `4H` | `Aster` | `37.86%` | `62.14%` | `0.61` | 1,010,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `56.27%` | `43.73%` | `1.29` | 975,010.00 USD |
| `4H` | `Whale Positions` | `49.61%` | `50.39%` | `0.98` | 66,540,000.00 USD |
| `4H` | `Global Accounts` | `49.67%` | `50.33%` | `0.99` | 160,830,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.03` | `11.03` | `11.03` | `11.07` | `11.00` | 1,477,587.17 USD | 739,486.08 USD | 738,101.09 USD | 1,384.99 USD | `+0.09%` | `8B / 13S` |
| `5:00 UTC` | `11.00` | `11.01` | `11.00` | `11.05` | `10.99` | 1,128,540.66 USD | 513,281.75 USD | 615,258.92 USD | -101,977.17 USD | `-9.04%` | `14B / 18S` |
| `0:00 UTC` | `11.01` | `11.00` | `11.01` | `11.03` | `10.97` | 1,915,299.28 USD | 805,989.55 USD | 1,109,309.72 USD | -303,320.17 USD | `-15.84%` | `3B / 10S` |
| `5:00 UTC` | `10.97` | `10.99` | `10.97` | `11.01` | `10.96` | 1,089,442.23 USD | 506,886.53 USD | 582,555.71 USD | -75,669.18 USD | `-6.95%` | `5B / 8S` |
| `0:00 UTC` | `10.98` | `10.99` | `10.98` | `11.03` | `10.95` | 1,226,717.62 USD | 576,497.16 USD | 650,220.46 USD | -73,723.30 USD | `-6.01%` | `21B / 13S` |
| `5:00 UTC` | `11.03` | `11.02` | `11.03` | `11.05` | `10.99` | 1,086,301.02 USD | 486,090.76 USD | 600,210.26 USD | -114,119.49 USD | `-10.51%` | `11B / 6S` |
| `0:00 UTC` | `11.02` | `11.02` | `11.02` | `11.04` | `10.99` | 1,056,195.55 USD | 514,499.98 USD | 541,695.57 USD | -27,195.58 USD | `-2.57%` | `3B / 5S` |
| `5:00 UTC` | `11.00` | `11.02` | `11.00` | `11.06` | `10.99` | 963,211.20 USD | 455,740.43 USD | 507,470.77 USD | -51,730.34 USD | `-5.37%` | `9B / 12S` |
| `0:00 UTC` | `11.05` | `11.06` | `11.05` | `11.10` | `11.01` | 3,673,451.57 USD | 2,114,279.15 USD | 1,559,172.42 USD | 555,106.73 USD | `+15.11%` | `18B / 10S` |
| `5:00 UTC` | `11.07` | `11.07` | `11.07` | `11.09` | `11.05` | 230,844.14 USD | 119,059.12 USD | 111,785.02 USD | 7,274.09 USD | `+3.15%` | `9B / 9S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:46` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.58` | 0.00 USD | 0.00 USD |
| `10-28 20:46` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 59,000.00 USD | 0.00 USD |
| `10-28 20:39` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.52` | 49,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.47` | 46,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 250K LINK` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.67` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Volume 250K LINK` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Divergence` | **`BEARISH`** | Rally without taker buying | `11.75` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.05` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `11.69` | 55,000.00 USD | 0.00 USD |
| `10-28 08:00` | `Volume 250K LINK` | `Divergence` | **`BULLISH`** | Drop without taker selling | `11.65` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Volume 250K LINK` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `11.78` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 51,100.00 USD | 41,020.00 USD | **`ACCUMULATION`** |
| `15m` | 502,870.00 USD | 613,090.00 USD | **`ACCUMULATION`** |
| `30m` | 660,230.00 USD | 699,010.00 USD | **`ACCUMULATION`** |
| `1h` | 913,480.00 USD | 370,800.00 USD | **`ACCUMULATION`** |
| `2h` | 562,580.00 USD | -225,110.00 USD | **`ACCUMULATION`** |
| `4h` | 602,140.00 USD | -67,580.00 USD | **`ACCUMULATION`** |
| `6h` | 270,110.00 USD | -854,620.00 USD | **`DISTRIBUTION`** |
| `8h` | -67,700.00 USD | 892,470.00 USD | **`ACCUMULATION`** |
| `12h` | -4,150,000.00 USD | -1,340,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,460,000.00 USD | -22,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -19,690,000.00 USD | -41,830,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -77,740,000.00 USD | -193,790,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+51.10K` | 15m=`+502.87K` | 1h=`+913.48K` | 24h=`-10.46M`
* Futures Capital Netflows: 5m=`+41.02K` | 15m=`+613.09K` | 1h=`+370.80K` | 24h=`-22.85M`
- **Institutional Crypto ETF Capital Flows (1_Crypto_ETF_Flows.parquet)**:
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)
  * `-`: ETF Net Flow = 0.00 USD (Inflows: 0.00 USD, Outflows: 0.00 USD)

- **High-Impact Macro Economic Events (19_Calendar.parquet)**:
  * `Sun Oct 25` [CHF - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [EUR - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Sun Oct 25` [GBP - Low Impact]: Daylight Saving Time Shift (Forecast: , Previous: )
  * `Mon Oct 26` [NZD - Low Impact]: Bank Holiday (Forecast: , Previous: )
  * `Mon Oct 26` [AUD - Low Impact]: RBA Assist Gov Jones Speaks (Forecast: , Previous: )
  * `Mon Oct 26` [EUR - Low Impact]: German ifo Business Climate (Forecast: 90.0, Previous: 89.9)
  * `Mon Oct 26` [GBP - Low Impact]: CBI Realized Sales (Forecast: -47, Previous: -55)
  * `Tue Oct 27` [JPY - Low Impact]: SPPI y/y (Forecast: 3.7%, Previous: 3.5%)
  * `Tue Oct 27` [GBP - Low Impact]: BRC Shop Price Index y/y (Forecast: 1.6%, Previous: 1.4%)
  * `Tue Oct 27` [JPY - Low Impact]: BOJ Core CPI y/y (Forecast: 1.9%, Previous: 1.8%)
  * `Tue Oct 27` [EUR - Low Impact]: Spanish Unemployment Rate (Forecast: 9.9%, Previous: 9.9%)
  * `Tue Oct 27` [EUR - Low Impact]: M3 Money Supply y/y (Forecast: 3.5%, Previous: 3.5%)
  * `Tue Oct 27` [EUR - Low Impact]: Private Loans y/y (Forecast: 3.1%, Previous: 3.1%)
  * `Tue Oct 27` [USD - Low Impact]: ADP Weekly Employment Change (Forecast: , Previous: 17.5K)
  * `Tue Oct 27` [USD - Low Impact]: Core Durable Goods Orders m/m (Forecast: 0.6%, Previous: 0.2%)

- **Breaking Institutional News & Market Intelligence (19_News.parquet)**:
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


---

## 9. TradFi & Interbank Market Mechanics
*(Applicable to Foreign Exchange Majors, Precious Metals, Global Equity Indices, and Commodities)*
- **Central Bank Monetary Policy & Rate Differential**:
  * Prevailing Policy Stance: `Federal Reserve (4.75% - 5.00%) Neutral-Gradualist Stance`
  * 2-Year Sovereign Yield Spread Direction & 10-Year Real Yield Momentum.
- **Interbank Foreign Exchange Mechanics**:
  * London/NY Overlap Window (13:00 - 16:00 UTC): Prime Institutional Liquidity.
  * Rollover Spread Expansion Gate: Execution strictly prohibited between 21:15 UTC and 22:30 UTC.
- **Global Commodity & Index Pricing Drivers**:
  * Precious Metals (XAU/XAG): Real Yield Sensitivity & Geopolitical Safe-Haven Premium.
  * Equity Indices (US30, SP500, NAS100): E-mini Auction VWAP Dispersion & Institutional Gamma Profiles.

---

## 10. Quantitative Trade Formulation & Autonomous Broker Execution Card
*(Sources: Canonical Quant Rules, STANDARDIZED_TRADING_DECISION_CHAIN.md, 10 lethal traps)*
- **Candidate Long Setup (Model 1 / Model 2 VAL Sweep Fade)**:
  * Order Type: `BUY_LIMIT`
  * Execution Entry: `10.56` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `9.23` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `13.88`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.12` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `12.45` (Risk Distance: `1.33` pts)
  * +2.5R Take Profit: `7.80`
  * Mathematical Lot Sizing: **`7.53 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.16`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
