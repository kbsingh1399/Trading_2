# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:55:01 IST` (`2026-10-30 11:25:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `283.36` | **Live Ask Quote**: `283.94` | **Mid Price**: `283.65`
- **Spread Points**: `580.00` | **Spread BPS**: `20.45 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `283.65` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `285.64` | Lower -3.00σ Band: `281.66`
  * Upper +2.51σ Band: `285.21` | Lower -2.51σ Band: `282.09`
  * Upper +2.01σ Band: `284.84` | Lower -2.01σ Band: `282.46`
  * Upper +2.00σ Band: `284.78` | Lower -2.00σ Band: `282.52`
  * Upper +1.28σ Band: `284.44` | Lower -1.28σ Band: `282.86`
  * Upper +1.00σ Band: `284.22` | Lower -1.00σ Band: `283.08`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`283.65` | EMA-20=`283.65` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.65` (Slope: `+0.0000`) | EMA-100=`283.65`
  * Institutional Anchors: EMA-144=`283.65` | EMA-200=`283.65` (Slope: `+0.0000`) | EMA-233=`283.65`
- **Range Boundaries**: 24H High=`286.49` | 24H Low=`280.81` | Weekly High=`289.32` | Weekly Low=`277.98`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `284.87` (Distance: `-0.38%`)
  * Point of Control (POC) = `283.88` (Distance: `-0.03%`)
  * Value Area Low (VAL) = `273.35` (Distance: `+3.82%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`275.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`287.26` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`287.26` | Low=`279.46`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `282.52` - `284.78`
  * Optimal Trade Entry (OTE 0.705): `284.22`
  * Structural Invalidation Anchor (0.786): `285.92`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `286.00` | `287.88` | `285.23` | `285.33` | `4,064` | 1,164,369.59 USD | -54,629.79 USD | `-4.69%` | -1,338,393.58 USD | `-0.97` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `285.40` | `286.52` | `285.20` | `285.32` | `1,376` | 393,395.20 USD | -19,805.00 USD | `-5.03%` | -1,358,198.58 USD | `-0.48` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `285.33` | `285.49` | `284.64` | `284.64` | `533` | 151,995.96 USD | -98,313.53 USD | `-64.68%` | -1,456,512.11 USD | `-1.34` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `281.72` | `284.99` | `281.56` | `284.76` | `4,953` | 1,404,905.07 USD | 153,177.98 USD | `+10.90%` | -1,448,967.42 USD | `+0.89` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `284.76` | `286.25` | `283.70` | `286.01` | `3,154` | 898,820.13 USD | 165,203.63 USD | `+18.38%` | -1,283,763.79 USD | `+0.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `286.00` | `287.88` | `284.64` | `284.64` | `5,974` | 1,709,967.68 USD | -172,955.26 USD | `-10.11%` | -1,456,719.05 USD | `-0.87` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `279.03` | `282.29` | `278.54` | `281.15` | `18,009` | 5,054,095.53 USD | -226,117.37 USD | `-4.47%` | -1,690,031.36 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `281.14` | `286.25` | `280.02` | `286.01` | `12,163` | 3,442,669.89 USD | 533,988.41 USD | `+15.51%` | -1,156,042.95 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `286.00` | `287.88` | `284.61` | `284.61` | `5,979` | 1,711,320.27 USD | -174,307.85 USD | `-10.19%` | -1,330,350.80 USD | `-0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `287.88` | `278.54` | `284.64` | `52,614` | 14,837,327.90 USD | 410,912.43 USD | `+2.77%` | -1,328,998.21 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `287.88` | `278.54` | `284.64` | `52,614` | 14,837,327.90 USD | 410,912.43 USD | `+2.77%` | -1,328,998.21 USD | `+0.53` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`283.65`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1945` | `0x12d2...f97f` | `LONG` | 1,032,458.45 USD | `3,627,243,000,000.00` | `303.26` | `284.53` | `0.000000` | -67,540.89 USD | `-6.54%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+1.71%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.53%`)
  * 48H Horizon: Short MP=`296.90` (Vol: 281,700.00 USD, Dist: `+4.55%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.53%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.69%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.51%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.69%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.51%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `57.50` | 2,360.00 USD | 211,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 832.17 USD | 209,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 105.91 USD | 208,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 534.54 USD | 208,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 353.43 USD | 207,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 207,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 206,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 200,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 195,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 1,480.00 USD | 195,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 121.50 USD | 194,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 194,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 194,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `132.50` | 1,990.00 USD | 193,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `133.50` | 3,340.00 USD | 191,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 188,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 2,690.00 USD | 187,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 184,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 182,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `154.50` | 1,170.00 USD | 181,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 180,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `163.50` | 8,180.00 USD | 180,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 172,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 171,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 171,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 171,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 170,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 170,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 169,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 169,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 168,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 167,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 166,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 982.30 USD | 165,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 164,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 164,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 163,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 6,440.00 USD | 163,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 157,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 41,790.00 USD | 156,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `208.50` | 625.50 USD | 115,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 114,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 114,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 110,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `222.50` | 5,300.00 USD | 110,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 31,290.00 USD | 104,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 482.23 USD | 73,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 73,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 288.24 USD | 71,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 71,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 1,190.00 USD | 71,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 69,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `235.50` | 640.32 USD | 69,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 68,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `238.50` | 3,790.00 USD | 45,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 41,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.90` | 10,680,000.00 USD | 10,680,000.00 USD | 887.27 USD | 588.60 USD | 27.54 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `240.50` | 7,120.00 USD | 40,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.70` | 10,680,000.00 USD | 10,680,000.00 USD | 2,780.00 USD | 0.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.10` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.50` | 10,670,000.00 USD | 10,670,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 1,770.00 USD | 33,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 10,660,000.00 USD | 10,660,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 10,640,000.00 USD | 10,640,000.00 USD | 36,130.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.70` | 10,570,000.00 USD | 10,570,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.10` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.50` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 31,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.90` | 10,540,000.00 USD | 10,540,000.00 USD | 30,790.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 29,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.70` | 10,490,000.00 USD | 10,490,000.00 USD | 836.88 USD | 4,470.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.10` | 10,480,000.00 USD | 10,480,000.00 USD | 599.05 USD | 28,580.00 USD | 3.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.50` | 10,450,000.00 USD | 10,450,000.00 USD | 4,450.00 USD | 6,920.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.90` | 10,440,000.00 USD | 10,440,000.00 USD | 11,770.00 USD | 10,460.00 USD | 0.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 10,410,000.00 USD | 10,410,000.00 USD | 11,640.00 USD | 11,210.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.70` | 10,380,000.00 USD | 10,380,000.00 USD | 4,590.00 USD | 0.00 USD | 8.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.10` | 10,380,000.00 USD | 10,380,000.00 USD | 14,580.00 USD | 17,540.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.50` | 10,340,000.00 USD | 10,340,000.00 USD | 9,000.00 USD | 4,870.00 USD | 19.16 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.90` | 10,330,000.00 USD | 10,330,000.00 USD | 555.60 USD | 310.87 USD | 3.04 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 10,330,000.00 USD | 10,330,000.00 USD | 5,130.00 USD | 2,370.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.70` | 10,310,000.00 USD | 10,310,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.10` | 10,210,000.00 USD | 10,210,000.00 USD | 16,180.00 USD | 31,600.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.50` | 10,160,000.00 USD | 10,160,000.00 USD | 46,460.00 USD | 32,910.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 10,070,000.00 USD | 10,070,000.00 USD | 45,500.00 USD | 13,210.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,980,000.00 USD | 9,980,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.50` | 5,340,000.00 USD | 5,340,000.00 USD | 13,910.00 USD | 7,570.00 USD | 12,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 23,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.70` | 9,920,000.00 USD | 9,920,000.00 USD | 34,190.00 USD | 60,940.00 USD | 36,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.90` | 5,310,000.00 USD | 5,310,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.10` | 9,790,000.00 USD | 9,790,000.00 USD | 42,800.00 USD | 51,050.00 USD | 12,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 5,270,000.00 USD | 5,270,000.00 USD | 26,340.00 USD | 22,320.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.50` | 9,680,000.00 USD | 9,680,000.00 USD | 12,810.00 USD | 63,290.00 USD | 36,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 5,190,000.00 USD | 5,190,000.00 USD | 27,330.00 USD | 43,370.00 USD | 13,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 9,570,000.00 USD | 9,570,000.00 USD | 86,720.00 USD | 56,690.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 5,110,000.00 USD | 5,110,000.00 USD | 16,350.00 USD | 5,490.00 USD | 12,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 9,390,000.00 USD | 9,390,000.00 USD | 51,260.00 USD | 25,300.00 USD | 12,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 5,080,000.00 USD | 5,080,000.00 USD | 11,020.00 USD | 1,620.00 USD | 6,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.70` | 9,300,000.00 USD | 9,300,000.00 USD | 46,920.00 USD | 19,890.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 5,060,000.00 USD | 5,060,000.00 USD | 772.10 USD | 2,430.00 USD | 1,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.10` | 9,220,000.00 USD | 9,220,000.00 USD | 12,990.00 USD | 27,180.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 5,050,000.00 USD | 5,050,000.00 USD | 12,560.00 USD | 9,050.00 USD | 14,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.50` | 9,180,000.00 USD | 9,180,000.00 USD | 26,490.00 USD | 36,470.00 USD | 44,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 5,020,000.00 USD | 5,020,000.00 USD | 20,160.00 USD | 15,410.00 USD | 12,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 9,070,000.00 USD | 9,070,000.00 USD | 25,260.00 USD | 29,760.00 USD | 22,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,970,000.00 USD | 4,970,000.00 USD | 1,650.00 USD | 7,170.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,990,000.00 USD | 8,990,000.00 USD | 40,680.00 USD | 32,450.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,950,000.00 USD | 4,950,000.00 USD | 8,310.00 USD | 11,590.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.70` | 8,910,000.00 USD | 8,910,000.00 USD | 48,210.00 USD | 37,690.00 USD | 85,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,930,000.00 USD | 4,930,000.00 USD | 9,050.00 USD | 12,090.00 USD | 97.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.10` | 8,730,000.00 USD | 8,730,000.00 USD | 3,010.00 USD | 12,610.00 USD | 25,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,910,000.00 USD | 4,910,000.00 USD | 9,910.00 USD | 15,990.00 USD | 27,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.50` | 8,690,000.00 USD | 8,690,000.00 USD | 50,170.00 USD | 5,330.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,850,000.00 USD | 4,850,000.00 USD | 17,660.00 USD | 25,900.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 8,620,000.00 USD | 8,620,000.00 USD | 7,460.00 USD | 20,140.00 USD | 30,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,790,000.00 USD | 4,790,000.00 USD | 10,050.00 USD | 21,990.00 USD | 17,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 8,560,000.00 USD | 8,560,000.00 USD | 46,870.00 USD | 9,520.00 USD | 22,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,740,000.00 USD | 4,740,000.00 USD | 8,450.00 USD | 21,060.00 USD | 13,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.70` | 8,480,000.00 USD | 8,480,000.00 USD | 31,480.00 USD | 11,630.00 USD | 54,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,700,000.00 USD | 4,700,000.00 USD | 6,970.00 USD | 6,030.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.10` | 8,380,000.00 USD | 8,380,000.00 USD | 14,870.00 USD | 9,760.00 USD | 20,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,680,000.00 USD | 4,680,000.00 USD | 11,120.00 USD | 13,350.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.50` | 8,340,000.00 USD | 8,340,000.00 USD | 19,860.00 USD | 10,920.00 USD | 23,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 101.20 USD | 20,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,640,000.00 USD | 4,640,000.00 USD | 2,380.00 USD | 4,780.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 8,280,000.00 USD | 8,280,000.00 USD | 17,330.00 USD | 7,290.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,630,000.00 USD | 4,630,000.00 USD | 19,830.00 USD | 2,310.00 USD | 46,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 8,250,000.00 USD | 8,250,000.00 USD | 98,040.00 USD | 34,930.00 USD | 71,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,560,000.00 USD | 4,560,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 544.40 USD | 20,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.70` | 8,050,000.00 USD | 8,050,000.00 USD | 100,340.00 USD | 4,180.00 USD | 36,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,500,000.00 USD | 4,500,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.10` | 7,910,000.00 USD | 7,910,000.00 USD | 19,700.00 USD | 17,770.00 USD | 26,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 4,420,000.00 USD | 4,420,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.50` | 7,840,000.00 USD | 7,840,000.00 USD | 5,720.00 USD | 34,490.00 USD | 17,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `259.50` | 1,300.00 USD | 19,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `259.70` | 4,380,000.00 USD | 4,380,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 7,780,000.00 USD | 7,780,000.00 USD | 95,750.00 USD | 56,770.00 USD | 97,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 4,290,000.00 USD | 4,290,000.00 USD | 39,470.00 USD | 8,640.00 USD | 6,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 7,540,000.00 USD | 7,540,000.00 USD | 25,040.00 USD | 11,780.00 USD | 60,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 4,230,000.00 USD | 4,230,000.00 USD | 19,000.00 USD | 1,900.00 USD | 27,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 18,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.70` | 7,440,000.00 USD | 7,440,000.00 USD | 15,620.00 USD | 46,940.00 USD | 60,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 4,190,000.00 USD | 4,190,000.00 USD | 9,090.00 USD | 50,950.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.10` | 7,310,000.00 USD | 7,310,000.00 USD | 6,540.00 USD | 64,780.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 4,110,000.00 USD | 4,110,000.00 USD | 8,200.00 USD | 29,340.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.50` | 7,230,000.00 USD | 7,230,000.00 USD | 15,880.00 USD | 97,480.00 USD | 43,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 4,040,000.00 USD | 4,040,000.00 USD | 15,340.00 USD | 60,900.00 USD | 51,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 7,070,000.00 USD | 7,070,000.00 USD | 54,070.00 USD | 37,130.00 USD | 46,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,910,000.00 USD | 3,910,000.00 USD | 13,720.00 USD | 28,450.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,930,000.00 USD | 6,930,000.00 USD | 43,400.00 USD | 76,260.00 USD | 40,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,850,000.00 USD | 3,850,000.00 USD | 21,220.00 USD | 5,730.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.70` | 6,770,000.00 USD | 6,770,000.00 USD | 55,510.00 USD | 49,160.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,810,000.00 USD | 3,810,000.00 USD | 629.76 USD | 12,730.00 USD | 19,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.10` | 6,640,000.00 USD | 6,640,000.00 USD | 37,610.00 USD | 13,710.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,780,000.00 USD | 3,780,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.50` | 6,580,000.00 USD | 6,580,000.00 USD | 179,320.00 USD | 1,880.00 USD | 83,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,700,000.00 USD | 3,700,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 6,320,000.00 USD | 6,320,000.00 USD | 236,080.00 USD | 629.16 USD | 34,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,590,000.00 USD | 3,590,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 6,050,000.00 USD | 6,050,000.00 USD | 39,870.00 USD | 1,170.00 USD | 112.61 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,510,000.00 USD | 3,510,000.00 USD | 1,300.00 USD | 20,340.00 USD | 23.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.70` | 6,010,000.00 USD | 6,010,000.00 USD | 33,280.00 USD | 21,870.00 USD | 124.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,490,000.00 USD | 3,490,000.00 USD | 33,390.00 USD | 2,430.00 USD | 53,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.10` | 5,950,000.00 USD | 5,950,000.00 USD | 94,300.00 USD | 2,340.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,400,000.00 USD | 3,400,000.00 USD | 65,040.00 USD | 2,840.00 USD | 12.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.50` | 5,820,000.00 USD | 5,820,000.00 USD | 195,260.00 USD | 1,420.00 USD | 14.32 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 2,150.00 USD | 16,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.70` | 3,330,000.00 USD | 3,330,000.00 USD | 436.52 USD | 812.59 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 5,630,000.00 USD | 5,630,000.00 USD | 58,470.00 USD | 0.00 USD | 117.36 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 3,330,000.00 USD | 3,330,000.00 USD | 16,410.00 USD | 13,470.00 USD | 5.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 5,570,000.00 USD | 5,570,000.00 USD | 194,070.00 USD | 2,170.00 USD | 182.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 3,300,000.00 USD | 3,300,000.00 USD | 14,430.00 USD | 9,090.00 USD | 4,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 5,370,000.00 USD | 5,370,000.00 USD | 86,630.00 USD | 63,260.00 USD | 41.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 3,270,000.00 USD | 3,270,000.00 USD | 18,470.00 USD | 23,750.00 USD | 7.21 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.10` | 5,220,000.00 USD | 5,220,000.00 USD | 117,200.00 USD | 26,850.00 USD | 181.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 3,230,000.00 USD | 3,230,000.00 USD | 33,620.00 USD | 70,000.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.50` | 5,080,000.00 USD | 5,080,000.00 USD | 102,500.00 USD | 61,270.00 USD | 38,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 2,220.00 USD | 14,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.70` | 3,120,000.00 USD | 3,120,000.00 USD | 10,460.00 USD | 36,440.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 4,870,000.00 USD | 4,870,000.00 USD | 233,930.00 USD | 25,100.00 USD | 106.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 3,040,000.00 USD | 3,040,000.00 USD | 19,060.00 USD | 28,480.00 USD | 60,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,610,000.00 USD | 4,610,000.00 USD | 144,970.00 USD | 124,980.00 USD | 95,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,930,000.00 USD | 2,930,000.00 USD | 18,310.00 USD | 18,920.00 USD | 69.78 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.70` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 18,320.00 USD | 38.38 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,900,000.00 USD | 2,900,000.00 USD | 21,330.00 USD | 11,500.00 USD | 284.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.10` | 4,230,000.00 USD | 4,230,000.00 USD | 23,340.00 USD | 1,560.00 USD | 232.27 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,860,000.00 USD | 2,860,000.00 USD | 11,120.00 USD | 2,950.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.50` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 2,540.00 USD | 8.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,840,000.00 USD | 2,840,000.00 USD | 6,590.00 USD | 19,580.00 USD | 13,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,800,000.00 USD | 2,800,000.00 USD | 17,110.00 USD | 13,590.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,770,000.00 USD | 2,770,000.00 USD | 48,700.00 USD | 3,090.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 12,140.00 USD | 12,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `270.70` | 4,200,000.00 USD | 4,200,000.00 USD | 33,050.00 USD | 970.20 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,710,000.00 USD | 2,710,000.00 USD | 612.40 USD | 17,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.10` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 957.20 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,690,000.00 USD | 2,690,000.00 USD | 12,710.00 USD | 2,140.00 USD | 16,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.50` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 61,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,660,000.00 USD | 2,660,000.00 USD | 8,650.00 USD | 36,810.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 4,100,000.00 USD | 4,100,000.00 USD | 61,810.00 USD | 7,250.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,600,000.00 USD | 2,600,000.00 USD | 21,980.00 USD | 24,560.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,540,000.00 USD | 2,540,000.00 USD | 8,490.00 USD | 41,370.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 3,980,000.00 USD | 3,980,000.00 USD | 25,660.00 USD | 17,630.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,440,000.00 USD | 2,440,000.00 USD | 66,940.00 USD | 15,170.00 USD | 80,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.10` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 147,420.00 USD | 137,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 2,280,000.00 USD | 2,280,000.00 USD | 30,950.00 USD | 123,250.00 USD | 43,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.50` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 114,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 2,080,000.00 USD | 2,080,000.00 USD | 60,550.00 USD | 67,190.00 USD | 69,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 3,460,000.00 USD | 3,460,000.00 USD | 337,830.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,880,000.00 USD | 1,880,000.00 USD | 152,290.00 USD | 44,080.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 3,030,000.00 USD | 3,030,000.00 USD | 380,220.00 USD | 46,000.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,670,000.00 USD | 1,670,000.00 USD | 165,560.00 USD | 44,750.00 USD | 63,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.70` | 2,520,000.00 USD | 2,520,000.00 USD | 427,250.00 USD | 22,090.00 USD | 68,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,400,000.00 USD | 1,400,000.00 USD | 54,360.00 USD | 22,510.00 USD | 20,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.10` | 2,000,000.00 USD | 2,000,000.00 USD | 139,440.00 USD | 0.00 USD | 10.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,300,000.00 USD | 1,300,000.00 USD | 11,720.00 USD | 3,760.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.50` | 1,860,000.00 USD | 1,860,000.00 USD | 2,590.00 USD | 19,960.00 USD | 109.48 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,270,000.00 USD | 1,270,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.90` | 1,840,000.00 USD | 1,840,000.00 USD | 1,950.00 USD | 23,010.00 USD | 82,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 1,150,000.00 USD | 1,150,000.00 USD | 172,570.00 USD | 3,340.00 USD | 7,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,730,000.00 USD | 1,730,000.00 USD | 218,450.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 970,360.00 USD | 970,360.00 USD | 11,920.00 USD | 16,150.00 USD | 18,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `276.50` | 451.52 USD | 451.52 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `276.70` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 5.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 923,600.00 USD | 923,600.00 USD | 37,290.00 USD | 25,410.00 USD | 33,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.10` | 1,410,000.00 USD | 1,410,000.00 USD | 44,670.00 USD | 0.00 USD | 122,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 826,990.00 USD | 826,990.00 USD | 17,610.00 USD | 22,050.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.50` | 1,240,000.00 USD | 1,240,000.00 USD | 123,610.00 USD | 235,540.00 USD | 59,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 769,530.00 USD | 769,530.00 USD | 13,750.00 USD | 16,920.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.90` | 825,910.00 USD | 825,910.00 USD | 0.00 USD | 1,830.00 USD | 60,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 718,540.00 USD | 718,540.00 USD | 16,630.00 USD | 103,670.00 USD | 95,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 764,070.00 USD | 764,070.00 USD | 24,750.00 USD | 35,270.00 USD | 155,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 503,080.00 USD | 503,080.00 USD | 93,830.00 USD | 76,370.00 USD | 65,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 548,670.00 USD | 548,670.00 USD | 51,310.00 USD | 49,750.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 267,040.00 USD | 267,040.00 USD | 23,710.00 USD | 14,630.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 223,210.00 USD | 223,210.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.50` | 423,660.00 USD | 423,660.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 182,120.00 USD | 182,120.00 USD | 0.00 USD | 0.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 157,790.00 USD | 157,790.00 USD | 15,540.00 USD | 59,700.00 USD | 49,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.30` | 421,000.00 USD | 421,000.00 USD | 0.00 USD | 22,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 32,610.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.70` | 398,920.00 USD | 398,920.00 USD | 29,850.00 USD | 54,170.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 24,800.00 USD | 24,800.00 USD | 0.00 USD | 0.00 USD | 14.16 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.10` | 247,450.00 USD | 247,450.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.50` | 153,630.00 USD | 153,630.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.90` | 31,240.00 USD | 31,240.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 9,560.00 USD | 9,560.00 USD | 8,260.00 USD | 0.00 USD | 5.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 10,540.00 USD | 10,540.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.10` | 7,020.00 USD | 7,020.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 1,300.00 USD | 1,300.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.90` | 3,570.00 USD | 3,570.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 15.61 USD | 15.61 USD | 0.00 USD | 0.00 USD | 15.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.30` | 1,570.00 USD | 1,570.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `284.50` | 394.60 USD | 846.13 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `284.70` | 65.52 USD | 65.52 USD | 0.00 USD | 0.00 USD | 65.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 18.94 USD | 18.94 USD | 0.00 USD | 0.00 USD | 18.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.10` | 327,980.00 USD | 327,980.00 USD | 125,000.00 USD | 137,110.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 78,310.00 USD | 78,310.00 USD | 36,620.00 USD | 0.00 USD | 41,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.50` | 402,850.00 USD | 402,850.00 USD | 5,350.00 USD | 69,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 80,020.00 USD | 80,020.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 406,730.00 USD | 406,730.00 USD | 1,200.00 USD | 2,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 84,420.00 USD | 84,420.00 USD | 4,360.00 USD | 0.00 USD | 30.67 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 409,070.00 USD | 409,070.00 USD | 0.00 USD | 2,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 99,900.00 USD | 99,900.00 USD | 11,720.00 USD | 3,760.00 USD | 4.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.70` | 411,710.00 USD | 411,710.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 170,140.00 USD | 170,140.00 USD | 45,630.00 USD | 24,600.00 USD | 14.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.10` | 418,970.00 USD | 418,970.00 USD | 3,620.00 USD | 3,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 309,730.00 USD | 309,730.00 USD | 108,880.00 USD | 30,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.50` | 424,640.00 USD | 424,640.00 USD | 3,420.00 USD | 2,150.00 USD | 103.44 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 958.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 366,010.00 USD | 366,010.00 USD | 22,860.00 USD | 33,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 427,250.00 USD | 427,250.00 USD | 2,580.00 USD | 0.00 USD | 23.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 458,400.00 USD | 458,400.00 USD | 21,420.00 USD | 26,660.00 USD | 44,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 470,460.00 USD | 470,460.00 USD | 0.00 USD | 1,550.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 576,920.00 USD | 576,920.00 USD | 52,260.00 USD | 29,840.00 USD | 36,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.70` | 731,850.00 USD | 731,850.00 USD | 123,610.00 USD | 15,650.00 USD | 122,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 652,250.00 USD | 652,250.00 USD | 44,740.00 USD | 30,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.10` | 793,810.00 USD | 793,810.00 USD | 1,170.00 USD | 932.60 USD | 59,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 767,800.00 USD | 767,800.00 USD | 17,220.00 USD | 47,120.00 USD | 51,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.50` | 820,920.00 USD | 820,920.00 USD | 0.00 USD | 27,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 1,050,000.00 USD | 1,050,000.00 USD | 71,760.00 USD | 86,660.00 USD | 121,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 1,140,000.00 USD | 1,140,000.00 USD | 52,840.00 USD | 73,930.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,290,000.00 USD | 1,290,000.00 USD | 65,110.00 USD | 58,580.00 USD | 114,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 1,250,000.00 USD | 1,250,000.00 USD | 34,580.00 USD | 49,750.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,490,000.00 USD | 1,490,000.00 USD | 32,450.00 USD | 123,930.00 USD | 52,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.70` | 1,310,000.00 USD | 1,310,000.00 USD | 30,940.00 USD | 861.99 USD | 32,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,640,000.00 USD | 1,640,000.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.10` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 18,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 1,740,000.00 USD | 1,740,000.00 USD | 27,020.00 USD | 25,140.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.50` | 1,520,000.00 USD | 1,520,000.00 USD | 27,390.00 USD | 78,710.00 USD | 19,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 6,980.00 USD | 7,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 1,870,000.00 USD | 1,870,000.00 USD | 28,390.00 USD | 71,460.00 USD | 30,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 1,790,000.00 USD | 1,790,000.00 USD | 25,610.00 USD | 175,760.00 USD | 67,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 1,910,000.00 USD | 1,910,000.00 USD | 6,710.00 USD | 15,850.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 1,860,000.00 USD | 1,860,000.00 USD | 1,240.00 USD | 72,680.00 USD | 25.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 1,960,000.00 USD | 1,960,000.00 USD | 29,880.00 USD | 3,650.00 USD | 17,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 1,950,000.00 USD | 1,950,000.00 USD | 887.27 USD | 87,810.00 USD | 30.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,050,000.00 USD | 2,050,000.00 USD | 62,510.00 USD | 27,920.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.10` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 145,540.00 USD | 9.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,130,000.00 USD | 2,130,000.00 USD | 27,950.00 USD | 15,280.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.50` | 2,130,000.00 USD | 2,130,000.00 USD | 33,580.00 USD | 694.90 USD | 38.07 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `293.50` | 157.02 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,320,000.00 USD | 2,320,000.00 USD | 76,710.00 USD | 47,640.00 USD | 70,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 2,270,000.00 USD | 2,270,000.00 USD | 53,080.00 USD | 21,610.00 USD | 65,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,420,000.00 USD | 2,420,000.00 USD | 21,460.00 USD | 25,650.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 2,620,000.00 USD | 2,620,000.00 USD | 202,860.00 USD | 22,540.00 USD | 121,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,680,000.00 USD | 2,680,000.00 USD | 96,690.00 USD | 80,200.00 USD | 85,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 2,810,000.00 USD | 2,810,000.00 USD | 16,110.00 USD | 93,810.00 USD | 89,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 2,780,000.00 USD | 2,780,000.00 USD | 33,490.00 USD | 17,570.00 USD | 48,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.10` | 3,090,000.00 USD | 3,090,000.00 USD | 48,390.00 USD | 16,140.00 USD | 214,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 2,970,000.00 USD | 2,970,000.00 USD | 18,010.00 USD | 65,340.00 USD | 102,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.50` | 3,700,000.00 USD | 3,700,000.00 USD | 167,940.00 USD | 155,660.00 USD | 280,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,230,000.00 USD | 3,230,000.00 USD | 106,670.00 USD | 16,690.00 USD | 137,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 3,930,000.00 USD | 3,930,000.00 USD | 59,330.00 USD | 114,600.00 USD | 60,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,450,000.00 USD | 3,450,000.00 USD | 55,060.00 USD | 128,640.00 USD | 38,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 4,160,000.00 USD | 4,160,000.00 USD | 27,350.00 USD | 78,210.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,550,000.00 USD | 3,550,000.00 USD | 33,430.00 USD | 22,420.00 USD | 41,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.70` | 4,460,000.00 USD | 4,460,000.00 USD | 119,280.00 USD | 4,410.00 USD | 173,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,690,000.00 USD | 3,690,000.00 USD | 24,280.00 USD | 28,310.00 USD | 90,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.10` | 4,640,000.00 USD | 4,640,000.00 USD | 89,710.00 USD | 62,630.00 USD | 27,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 3,830,000.00 USD | 3,830,000.00 USD | 69,150.00 USD | 24,320.00 USD | 40,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.50` | 4,800,000.00 USD | 4,800,000.00 USD | 16,090.00 USD | 83,510.00 USD | 68,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 3,870,000.00 USD | 3,870,000.00 USD | 15,920.00 USD | 11,900.00 USD | 15,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 4,950,000.00 USD | 4,950,000.00 USD | 47,790.00 USD | 42,380.00 USD | 54,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 3,980,000.00 USD | 3,980,000.00 USD | 52,050.00 USD | 10,350.00 USD | 41,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 5,100,000.00 USD | 5,100,000.00 USD | 32,250.00 USD | 45,480.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,050,000.00 USD | 4,050,000.00 USD | 5,990.00 USD | 1,730.00 USD | 64,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.70` | 5,180,000.00 USD | 5,180,000.00 USD | 69,820.00 USD | 11,780.00 USD | 4.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,180,000.00 USD | 4,180,000.00 USD | 28,550.00 USD | 5,830.00 USD | 94,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.10` | 5,270,000.00 USD | 5,270,000.00 USD | 1,800.00 USD | 3,050.00 USD | 85,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,230,000.00 USD | 4,230,000.00 USD | 34,220.00 USD | 11,020.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.50` | 5,300,000.00 USD | 5,300,000.00 USD | 3,930.00 USD | 27,060.00 USD | 76.34 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,280,000.00 USD | 4,280,000.00 USD | 8,350.00 USD | 12,170.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 5,380,000.00 USD | 5,380,000.00 USD | 54,340.00 USD | 11,070.00 USD | 19,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,400,000.00 USD | 4,400,000.00 USD | 20,020.00 USD | 37,720.00 USD | 64,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 5,390,000.00 USD | 5,390,000.00 USD | 866.20 USD | 1,190.00 USD | 128.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,450,000.00 USD | 4,450,000.00 USD | 23,270.00 USD | 1,650.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 2,470.00 USD | 10,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `300.70` | 5,500,000.00 USD | 5,500,000.00 USD | 25,350.00 USD | 71,120.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,480,000.00 USD | 4,480,000.00 USD | 444.05 USD | 1,220.00 USD | 29,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.10` | 5,680,000.00 USD | 5,680,000.00 USD | 25,570.00 USD | 33,490.00 USD | 119,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,510,000.00 USD | 4,510,000.00 USD | 693.10 USD | 15,110.00 USD | 20,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.50` | 5,910,000.00 USD | 5,910,000.00 USD | 85,980.00 USD | 88,000.00 USD | 59,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,560,000.00 USD | 4,560,000.00 USD | 19,840.00 USD | 8,470.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 6,120,000.00 USD | 6,120,000.00 USD | 51,660.00 USD | 123,250.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,620,000.00 USD | 4,620,000.00 USD | 25,190.00 USD | 30,660.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 6,240,000.00 USD | 6,240,000.00 USD | 1,560.00 USD | 126,650.00 USD | 44.13 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,690,000.00 USD | 4,690,000.00 USD | 13,920.00 USD | 13,700.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 6,430,000.00 USD | 6,430,000.00 USD | 71,700.00 USD | 72,000.00 USD | 41,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 4,710,000.00 USD | 4,710,000.00 USD | 1,440.00 USD | 2,520.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.10` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 42,380.00 USD | 61.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 4,740,000.00 USD | 4,740,000.00 USD | 21,400.00 USD | 2,940.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.50` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 173.09 USD | 75.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 4,740,000.00 USD | 4,740,000.00 USD | 248.72 USD | 573.99 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 6,550,000.00 USD | 6,550,000.00 USD | 21,140.00 USD | 11,740.00 USD | 45,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 4,810,000.00 USD | 4,810,000.00 USD | 22,000.00 USD | 1,990.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 6,560,000.00 USD | 6,560,000.00 USD | 2,070.00 USD | 4,320.00 USD | 153.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 4,860,000.00 USD | 4,860,000.00 USD | 9,670.00 USD | 2,380.00 USD | 44,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 6,580,000.00 USD | 6,580,000.00 USD | 2,950.00 USD | 12,510.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 4,880,000.00 USD | 4,880,000.00 USD | 9,920.00 USD | 8,610.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.10` | 6,920,000.00 USD | 6,920,000.00 USD | 128,400.00 USD | 128,260.00 USD | 84,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 4,880,000.00 USD | 4,880,000.00 USD | 83.23 USD | 172.52 USD | 1.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.50` | 7,080,000.00 USD | 7,080,000.00 USD | 93,400.00 USD | 19,010.00 USD | 48,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `305.50` | 3,140.00 USD | 13,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `305.70` | 4,900,000.00 USD | 4,900,000.00 USD | 6,340.00 USD | 3,650.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 7,190,000.00 USD | 7,190,000.00 USD | 56,810.00 USD | 53,540.00 USD | 3,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 4,920,000.00 USD | 4,920,000.00 USD | 7,500.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 7,340,000.00 USD | 7,340,000.00 USD | 29,420.00 USD | 57,910.00 USD | 63,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 4,930,000.00 USD | 4,930,000.00 USD | 4,330.00 USD | 6.13 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 7,480,000.00 USD | 7,480,000.00 USD | 27,190.00 USD | 44,210.00 USD | 69,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,000,000.00 USD | 5,000,000.00 USD | 19,810.00 USD | 35,610.00 USD | 18,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.10` | 7,750,000.00 USD | 7,750,000.00 USD | 74,130.00 USD | 89,830.00 USD | 98,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,070,000.00 USD | 5,070,000.00 USD | 11,240.00 USD | 32,670.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.50` | 7,980,000.00 USD | 7,980,000.00 USD | 62,450.00 USD | 114,390.00 USD | 54,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,120,000.00 USD | 5,120,000.00 USD | 24,280.00 USD | 20,210.00 USD | 3,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 8,260,000.00 USD | 8,260,000.00 USD | 125,550.00 USD | 101,520.00 USD | 59,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,150,000.00 USD | 5,150,000.00 USD | 14,750.00 USD | 4,740.00 USD | 12,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 8,540,000.00 USD | 8,540,000.00 USD | 128,880.00 USD | 41,210.00 USD | 109,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,150,000.00 USD | 5,150,000.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 8,660,000.00 USD | 8,660,000.00 USD | 67,430.00 USD | 31,490.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,160,000.00 USD | 5,160,000.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.10` | 8,780,000.00 USD | 8,780,000.00 USD | 38,660.00 USD | 39,620.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 5,170,000.00 USD | 5,170,000.00 USD | 3,240.00 USD | 2,300.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.50` | 8,970,000.00 USD | 8,970,000.00 USD | 47,160.00 USD | 51,160.00 USD | 95,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 5,190,000.00 USD | 5,190,000.00 USD | 10,120.00 USD | 7,750.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 9,170,000.00 USD | 9,170,000.00 USD | 19,540.00 USD | 106,330.00 USD | 75,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 5,220,000.00 USD | 5,220,000.00 USD | 13,080.00 USD | 4,100.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 9,420,000.00 USD | 9,420,000.00 USD | 61,040.00 USD | 107,890.00 USD | 76,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 5,230,000.00 USD | 5,230,000.00 USD | 176.40 USD | 5,020.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.70` | 9,530,000.00 USD | 9,530,000.00 USD | 60,380.00 USD | 50,820.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 5,240,000.00 USD | 5,240,000.00 USD | 5,080.00 USD | 73.70 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.10` | 9,720,000.00 USD | 9,720,000.00 USD | 59,270.00 USD | 59,630.00 USD | 72,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 5,240,000.00 USD | 5,240,000.00 USD | 257.90 USD | 3,110.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.50` | 9,800,000.00 USD | 9,800,000.00 USD | 55,980.00 USD | 6,680.00 USD | 13,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 5,270,000.00 USD | 5,270,000.00 USD | 7,980.00 USD | 10,410.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 9,870,000.00 USD | 9,870,000.00 USD | 39,900.00 USD | 11,610.00 USD | 19,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 5,290,000.00 USD | 5,290,000.00 USD | 299.35 USD | 10,630.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 9,930,000.00 USD | 9,930,000.00 USD | 23,020.00 USD | 11,240.00 USD | 27,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,340,000.00 USD | 5,340,000.00 USD | 17,660.00 USD | 11,130.00 USD | 17,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 9,970,000.00 USD | 9,970,000.00 USD | 8,290.00 USD | 19,990.00 USD | 12,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 5,360,000.00 USD | 5,360,000.00 USD | 9,040.00 USD | 1,710.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.10` | 10,040,000.00 USD | 10,040,000.00 USD | 28,080.00 USD | 11,540.00 USD | 29,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 5,380,000.00 USD | 5,380,000.00 USD | 3,700.00 USD | 18,390.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.50` | 10,090,000.00 USD | 10,090,000.00 USD | 13,630.00 USD | 116.35 USD | 27,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 5,400,000.00 USD | 5,400,000.00 USD | 4,610.00 USD | 4,610.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 10,160,000.00 USD | 10,160,000.00 USD | 32,050.00 USD | 1,450.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 2,760.00 USD | 8,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 10,240,000.00 USD | 10,240,000.00 USD | 51,980.00 USD | 4,720.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 5,440,000.00 USD | 5,440,000.00 USD | 7,350.00 USD | 9,390.00 USD | 12,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 10,280,000.00 USD | 10,280,000.00 USD | 433.10 USD | 8,840.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 3,750.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.10` | 10,290,000.00 USD | 10,290,000.00 USD | 17,280.00 USD | 258.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 5,450,000.00 USD | 5,450,000.00 USD | 2,100.00 USD | 1,550.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.50` | 10,310,000.00 USD | 10,310,000.00 USD | 478.19 USD | 181.20 USD | 12,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 5,460,000.00 USD | 5,460,000.00 USD | 1,850.00 USD | 0.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 10,400,000.00 USD | 10,400,000.00 USD | 39,580.00 USD | 33,520.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 5,470,000.00 USD | 5,470,000.00 USD | 2,100.00 USD | 0.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 10,460,000.00 USD | 10,460,000.00 USD | 451.45 USD | 19,680.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 5,470,000.00 USD | 5,470,000.00 USD | 20.15 USD | 3,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 10,520,000.00 USD | 10,520,000.00 USD | 18,110.00 USD | 20,380.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.90` | 5,500,000.00 USD | 5,500,000.00 USD | 12,960.00 USD | 2,360.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.10` | 10,520,000.00 USD | 10,520,000.00 USD | 1,810.00 USD | 1,110.00 USD | 171.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.30` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 2,190.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.50` | 10,540,000.00 USD | 10,540,000.00 USD | 14,400.00 USD | 574.27 USD | 76.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.60` | 5,520,000.00 USD | 5,520,000.00 USD | 8,410.00 USD | 8,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 10,570,000.00 USD | 10,570,000.00 USD | 21,020.00 USD | 8,660.00 USD | 143.05 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 10,630,000.00 USD | 10,630,000.00 USD | 3,320.00 USD | 31,110.00 USD | 32,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.70` | 10,670,000.00 USD | 10,670,000.00 USD | 9,900.00 USD | 17,490.00 USD | 14,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `321.50` | 1,110.00 USD | 14,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `323.50` | 686.79 USD | 15,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `324.50` | 2,220.00 USD | 17,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 43,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `346.50` | 1,390.00 USD | 44,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 45,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 46,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `369.50` | 40,650.00 USD | 86,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `406.50` | 10,640.00 USD | 97,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 143,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 144,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `535.50` | 352.36 USD | 144,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `552.50` | 195.03 USD | 144,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 145,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `57.50` | 211,410.00 USD | 0.00 USD | 2,360.00 USD | `-79.92%` | `41,012,000,000.00` |
| `Live` | `Long` | `63.50` | 209,050.00 USD | 0.00 USD | 832.17 USD | `-77.83%` | `13,105,000,000.00` |
| `Live` | `Long` | `67.50` | 208,220.00 USD | 0.00 USD | 105.91 USD | `-76.43%` | `1,569,000,000.00` |
| `Live` | `Long` | `74.50` | 208,110.00 USD | 0.00 USD | 534.54 USD | `-73.99%` | `7,175,000,000.00` |
| `Live` | `Long` | `93.50` | 207,580.00 USD | 0.00 USD | 353.43 USD | `-67.35%` | `3,780,000,000.00` |
| `Live` | `Long` | `95.50` | 207,220.00 USD | 0.00 USD | 920.05 USD | `-66.66%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 206,300.00 USD | 0.00 USD | 6,240.00 USD | `-64.56%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 200,070.00 USD | 0.00 USD | 4,080.00 USD | `-64.21%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 195,990.00 USD | 0.00 USD | 212.76 USD | `-61.77%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 195,770.00 USD | 0.00 USD | 1,480.00 USD | `-58.63%` | `12,491,000,000.00` |
| `Live` | `Long` | `121.50` | 194,290.00 USD | 0.00 USD | 121.50 USD | `-57.58%` | `1,000,000,000.00` |
| `Live` | `Long` | `122.50` | 194,170.00 USD | 0.00 USD | 124.46 USD | `-57.23%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 194,050.00 USD | 0.00 USD | 658.18 USD | `-55.83%` | `5,203,000,000.00` |
| `Live` | `Long` | `132.50` | 193,390.00 USD | 0.00 USD | 1,990.00 USD | `-53.74%` | `15,000,000,000.00` |
| `Live` | `Long` | `133.50` | 191,400.00 USD | 0.00 USD | 3,340.00 USD | `-53.39%` | `25,000,000,000.00` |
| `Live` | `Long` | `147.50` | 188,070.00 USD | 0.00 USD | 895.47 USD | `-48.50%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 187,170.00 USD | 0.00 USD | 2,690.00 USD | `-48.15%` | `18,127,000,000.00` |
| `Live` | `Long` | `149.50` | 184,480.00 USD | 0.00 USD | 2,370.00 USD | `-47.80%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 182,110.00 USD | 0.00 USD | 303.78 USD | `-46.75%` | `1,992,000,000.00` |
| `Live` | `Long` | `154.50` | 181,810.00 USD | 0.00 USD | 1,170.00 USD | `-46.06%` | `7,572,000,000.00` |
| `Live` | `Long` | `162.50` | 180,640.00 USD | 0.00 USD | 325.00 USD | `-43.26%` | `2,000,000,000.00` |
| `Live` | `Long` | `163.50` | 180,310.00 USD | 0.00 USD | 8,180.00 USD | `-42.91%` | `50,000,000,000.00` |
| `Live` | `Long` | `167.50` | 172,140.00 USD | 0.00 USD | 285.75 USD | `-41.52%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 171,850.00 USD | 0.00 USD | 426.25 USD | `-40.47%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 171,430.00 USD | 0.00 USD | 169.96 USD | `-39.07%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 171,260.00 USD | 0.00 USD | 516.67 USD | `-38.72%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 170,740.00 USD | 0.00 USD | 373.83 USD | `-38.38%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 170,370.00 USD | 0.00 USD | 808.66 USD | `-35.58%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 169,560.00 USD | 0.00 USD | 418.28 USD | `-34.19%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 169,140.00 USD | 0.00 USD | 694.75 USD | `-33.49%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 168,440.00 USD | 0.00 USD | 858.49 USD | `-33.14%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 167,590.00 USD | 0.00 USD | 1,490.00 USD | `-32.79%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 166,100.00 USD | 0.00 USD | 370.47 USD | `-31.74%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 165,730.00 USD | 0.00 USD | 982.30 USD | `-31.39%` | `4,999,000,000.00` |
| `Live` | `Long` | `199.50` | 164,750.00 USD | 0.00 USD | 548.03 USD | `-30.34%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 164,200.00 USD | 0.00 USD | 293.13 USD | `-30.00%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 163,910.00 USD | 0.00 USD | 420.39 USD | `-29.30%` | `2,076,000,000.00` |
| `Live` | `Long` | `204.50` | 163,490.00 USD | 0.00 USD | 6,440.00 USD | `-28.60%` | `31,500,000,000.00` |
| `Live` | `Long` | `205.50` | 157,040.00 USD | 0.00 USD | 191.53 USD | `-28.25%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 156,850.00 USD | 0.00 USD | 41,790.00 USD | `-27.90%` | `202,387,000,000.00` |
| `Live` | `Long` | `208.50` | 115,060.00 USD | 0.00 USD | 625.50 USD | `-27.20%` | `3,000,000,000.00` |
| `Live` | `Long` | `210.50` | 114,440.00 USD | 0.00 USD | 108.83 USD | `-26.50%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 114,330.00 USD | 0.00 USD | 3,800.00 USD | `-25.46%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 110,520.00 USD | 0.00 USD | 239.85 USD | `-24.76%` | `1,113,000,000.00` |
| `Live` | `Long` | `222.50` | 110,280.00 USD | 0.00 USD | 5,300.00 USD | `-22.31%` | `23,803,000,000.00` |
| `Live` | `Long` | `223.50` | 104,990.00 USD | 0.00 USD | 31,290.00 USD | `-21.97%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 73,700.00 USD | 0.00 USD | 482.23 USD | `-21.62%` | `2,148,000,000.00` |
| `Live` | `Long` | `226.50` | 73,210.00 USD | 0.00 USD | 1,240.00 USD | `-20.92%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 71,980.00 USD | 0.00 USD | 288.24 USD | `-20.57%` | `1,267,000,000.00` |
| `Live` | `Long` | `228.50` | 71,690.00 USD | 0.00 USD | 642.77 USD | `-20.22%` | `2,813,000,000.00` |
| `Live` | `Long` | `230.50` | 71,050.00 USD | 0.00 USD | 1,190.00 USD | `-19.52%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 69,860.00 USD | 0.00 USD | 295.86 USD | `-19.17%` | `1,278,000,000.00` |
| `Live` | `Long` | `235.50` | 69,560.00 USD | 0.00 USD | 640.32 USD | `-17.78%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 68,920.00 USD | 0.00 USD | 23,750.00 USD | `-17.08%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 45,170.00 USD | 0.00 USD | 3,790.00 USD | `-16.73%` | `15,877,000,000.00` |
| `Live` | `Long` | `239.50` | 41,380.00 USD | 0.00 USD | 1,030.00 USD | `-16.38%` | `4,281,000,000.00` |
| `Live` | `Long` | `240.50` | 40,360.00 USD | 0.00 USD | 7,120.00 USD | `-16.03%` | `29,590,000,000.00` |
| `Live` | `Long` | `241.50` | 33,240.00 USD | 0.00 USD | 1,770.00 USD | `-15.68%` | `7,317,000,000.00` |
| `Live` | `Long` | `243.50` | 31,470.00 USD | 0.00 USD | 1,850.00 USD | `-14.98%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 29,630.00 USD | 0.00 USD | 4,220.00 USD | `-14.63%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 25,400.00 USD | 0.00 USD | 1,030.00 USD | `-14.28%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,370.00 USD | 0.00 USD | 106.67 USD | `-13.59%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,270.00 USD | 0.00 USD | 595.16 USD | `-13.24%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 23,670.00 USD | 0.00 USD | 1,330.00 USD | `-12.54%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,350.00 USD | 0.00 USD | 268.35 USD | `-12.19%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 22,080.00 USD | 0.00 USD | 1,030.00 USD | `-11.84%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 21,050.00 USD | 0.00 USD | 548.45 USD | `-11.14%` | `2,155,000,000.00` |
| `Live` | `Long` | `257.50` | 20,500.00 USD | 0.00 USD | 101.20 USD | `-10.09%` | `393,000,000.00` |
| `Live` | `Long` | `258.50` | 20,400.00 USD | 0.00 USD | 544.40 USD | `-9.74%` | `2,106,000,000.00` |
| `Live` | `Long` | `259.50` | 19,850.00 USD | 0.00 USD | 1,300.00 USD | `-9.40%` | `5,000,000,000.00` |
| `Live` | `Long` | `260.50` | 18,560.00 USD | 0.00 USD | 2,040.00 USD | `-9.05%` | `7,839,000,000.00` |
| `Live` | `Long` | `265.50` | 16,510.00 USD | 0.00 USD | 2,150.00 USD | `-7.30%` | `8,101,000,000.00` |
| `Live` | `Long` | `267.50` | 14,360.00 USD | 0.00 USD | 2,220.00 USD | `-6.60%` | `8,301,000,000.00` |
| `Live` | `Long` | `270.50` | 12,140.00 USD | 0.00 USD | 12,140.00 USD | `-5.55%` | `44,886,000,000.00` |
| `Live` | `Short` | `276.50` | 451.52 USD | 451.52 USD | 0.00 USD | `-3.46%` | `1,633,000,000.00` |
| `Live` | `Short` | `284.50` | 846.13 USD | 394.60 USD | 0.00 USD | `-0.67%` | `1,387,000,000.00` |
| `Live` | `Short` | `287.50` | 958.25 USD | 112.12 USD | 0.00 USD | `+0.38%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 7,940.00 USD | 6,980.00 USD | 0.00 USD | `+1.78%` | `23,944,000,000.00` |
| `Live` | `Short` | `293.50` | 8,090.00 USD | 157.02 USD | 0.00 USD | `+2.48%` | `535,000,000.00` |
| `Live` | `Short` | `300.50` | 10,570.00 USD | 2,470.00 USD | 0.00 USD | `+4.92%` | `8,231,000,000.00` |
| `Live` | `Short` | `305.50` | 13,710.00 USD | 3,140.00 USD | 0.00 USD | `+6.67%` | `10,273,000,000.00` |
| `Live` | `Short` | `321.50` | 14,820.00 USD | 1,110.00 USD | 0.00 USD | `+12.25%` | `3,452,000,000.00` |
| `Live` | `Short` | `323.50` | 15,500.00 USD | 686.79 USD | 0.00 USD | `+12.95%` | `2,123,000,000.00` |
| `Live` | `Short` | `324.50` | 17,730.00 USD | 2,220.00 USD | 0.00 USD | `+13.30%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 43,260.00 USD | 25,530.00 USD | 0.00 USD | `+14.00%` | `78,189,000,000.00` |
| `Live` | `Short` | `346.50` | 44,640.00 USD | 1,390.00 USD | 0.00 USD | `+20.98%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 45,650.00 USD | 1,010.00 USD | 0.00 USD | `+25.17%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 46,100.00 USD | 445.52 USD | 0.00 USD | `+28.66%` | `1,209,000,000.00` |
| `Live` | `Short` | `369.50` | 86,740.00 USD | 40,650.00 USD | 0.00 USD | `+29.01%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 97,380.00 USD | 10,640.00 USD | 0.00 USD | `+41.93%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 143,630.00 USD | 46,250.00 USD | 0.00 USD | `+60.43%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 144,350.00 USD | 718.34 USD | 0.00 USD | `+74.05%` | `1,441,000,000.00` |
| `Live` | `Short` | `535.50` | 144,700.00 USD | 352.36 USD | 0.00 USD | `+86.97%` | `658,000,000.00` |
| `Live` | `Short` | `552.50` | 144,900.00 USD | 195.03 USD | 0.00 USD | `+92.91%` | `353,000,000.00` |
| `Live` | `Short` | `560.50` | 145,740.00 USD | 842.43 USD | 0.00 USD | `+95.70%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 467,800.00 USD | 0.00 USD | 210.94 USD | `-49.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 467,580.00 USD | 0.00 USD | 2,070.00 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 465,520.00 USD | 0.00 USD | 489.38 USD | `-42.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 465,030.00 USD | 0.00 USD | 2,530.00 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 462,500.00 USD | 0.00 USD | 490.59 USD | `-35.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 462,010.00 USD | 0.00 USD | 482.01 USD | `-31.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 461,530.00 USD | 0.00 USD | 189.07 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 461,340.00 USD | 0.00 USD | 441.60 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 460,900.00 USD | 0.00 USD | 299.96 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 460,600.00 USD | 0.00 USD | 715.29 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 459,880.00 USD | 0.00 USD | 638.36 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 459,240.00 USD | 0.00 USD | 740.85 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 458,500.00 USD | 0.00 USD | 478.48 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 458,020.00 USD | 0.00 USD | 389.48 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 457,630.00 USD | 0.00 USD | 812.38 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 456,820.00 USD | 0.00 USD | 220.64 USD | `-17.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 456,600.00 USD | 0.00 USD | 429.30 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 456,170.00 USD | 0.00 USD | 296.50 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 455,880.00 USD | 0.00 USD | 216.45 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 455,660.00 USD | 0.00 USD | 387.76 USD | `-15.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 455,270.00 USD | 0.00 USD | 18,080.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 437,190.00 USD | 0.00 USD | 1,630.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 435,560.00 USD | 0.00 USD | 2,700.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 432,860.00 USD | 0.00 USD | 2,940.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 429,920.00 USD | 0.00 USD | 4,560.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 425,360.00 USD | 0.00 USD | 1,850.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 423,510.00 USD | 0.00 USD | 231.54 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 423,280.00 USD | 0.00 USD | 109.26 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 423,170.00 USD | 0.00 USD | 1,780.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 421,400.00 USD | 0.00 USD | 51,300.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 370,100.00 USD | 0.00 USD | 250.81 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 369,840.00 USD | 0.00 USD | 5,510.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 364,330.00 USD | 0.00 USD | 269,800.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 94,540.00 USD | 0.00 USD | 3,600.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 90,940.00 USD | 0.00 USD | 199.17 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 90,740.00 USD | 0.00 USD | 2,180.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 88,560.00 USD | 0.00 USD | 241.98 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 88,320.00 USD | 0.00 USD | 219.35 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 88,100.00 USD | 0.00 USD | 107.40 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 87,990.00 USD | 0.00 USD | 29,530.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 58,460.00 USD | 0.00 USD | 541.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 57,920.00 USD | 0.00 USD | 620.38 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 57,300.00 USD | 0.00 USD | 13,500.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 43,810.00 USD | 0.00 USD | 136.20 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 43,670.00 USD | 0.00 USD | 667.86 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 43,000.00 USD | 0.00 USD | 275.50 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 42,730.00 USD | 0.00 USD | 553.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 42,170.00 USD | 0.00 USD | 326.34 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 41,850.00 USD | 0.00 USD | 5,040.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 36,800.00 USD | 0.00 USD | 21,990.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 14,810.00 USD | 0.00 USD | 139.69 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 14,670.00 USD | 0.00 USD | 3,100.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 11,570.00 USD | 0.00 USD | 2,350.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 9,230.00 USD | 0.00 USD | 8,040.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 1,190.00 USD | 0.00 USD | 137.98 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 1,050.00 USD | 0.00 USD | 1,050.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 280.77 USD | 280.77 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 7,190.00 USD | 6,910.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 7,450.00 USD | 261.96 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 7,980.00 USD | 530.36 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 8,190.00 USD | 212.36 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 33,470.00 USD | 25,280.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 33,620.00 USD | 147.71 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 34,610.00 USD | 992.62 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 36,630.00 USD | 2,020.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 41,360.00 USD | 4,730.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 41,470.00 USD | 110.37 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 41,860.00 USD | 388.95 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 42,010.00 USD | 153.94 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 52,790.00 USD | 10,780.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 57,890.00 USD | 5,110.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 71,450.00 USD | 13,550.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 74,100.00 USD | 2,650.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 74,380.00 USD | 282.89 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 88,880.00 USD | 14,500.00 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 89,030.00 USD | 155.25 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 90,070.00 USD | 1,030.00 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 95,710.00 USD | 5,650.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 96,250.00 USD | 534.59 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 96,570.00 USD | 321.50 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `323.50` | 97,470.00 USD | 899.33 USD | 0.00 USD | `+12.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 164,190.00 USD | 66,720.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 165,280.00 USD | 1,090.00 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 177,270.00 USD | 12,000.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 177,820.00 USD | 547.52 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 177,930.00 USD | 110.91 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 178,190.00 USD | 257.45 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 178,360.00 USD | 174.25 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 178,510.00 USD | 151.50 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 179,970.00 USD | 1,450.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 181,740.00 USD | 1,770.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 182,070.00 USD | 326.07 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 182,890.00 USD | 826.60 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 190,340.00 USD | 7,440.00 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 191,020.00 USD | 682.84 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 192,120.00 USD | 1,100.00 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 192,800.00 USD | 683.96 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 193,000.00 USD | 199.75 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 194,730.00 USD | 1,730.00 USD | 0.00 USD | `+39.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 195,770.00 USD | 1,040.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 196,150.00 USD | 376.71 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 196,310.00 USD | 158.86 USD | 0.00 USD | `+43.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 202,210.00 USD | 5,900.00 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 203,290.00 USD | 1,080.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 204,990.00 USD | 1,700.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 206,540.00 USD | 1,550.00 USD | 0.00 USD | `+50.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 207,930.00 USD | 1,380.00 USD | 0.00 USD | `+52.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 208,550.00 USD | 621.14 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 210,820.00 USD | 2,280.00 USD | 0.00 USD | `+53.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 211,050.00 USD | 222.75 USD | 0.00 USD | `+55.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 217,970.00 USD | 6,920.00 USD | 0.00 USD | `+57.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 223,880.00 USD | 5,920.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 225,010.00 USD | 1,130.00 USD | 0.00 USD | `+60.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 232,650.00 USD | 7,630.00 USD | 0.00 USD | `+68.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 233,620.00 USD | 975.00 USD | 0.00 USD | `+70.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 234,600.00 USD | 981.00 USD | 0.00 USD | `+71.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 235,100.00 USD | 499.50 USD | 0.00 USD | `+74.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,120,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+74.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,120,000.00 USD | 1,000.00 USD | 0.00 USD | `+75.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,120,000.00 USD | 1,040.00 USD | 0.00 USD | `+81.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,120,000.00 USD | 340.67 USD | 0.00 USD | `+82.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,120,000.00 USD | 638.86 USD | 0.00 USD | `+94.30%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `239.90` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 887.27 USD | 588.60 USD | 27.54 USD |
| `7D` | `240.70` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 2,780.00 USD | 0.00 USD | 4,570.00 USD |
| `7D` | `241.10` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD |
| `7D` | `241.50` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `241.90` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 19,010.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.30` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 36,130.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.70` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 1,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `243.10` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD |
| `7D` | `243.50` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 0.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `243.90` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 30,790.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.70` | 10,490,000.00 USD | 0.00 USD | 10,490,000.00 USD | 836.88 USD | 4,470.00 USD | 2,630.00 USD |
| `7D` | `245.10` | 10,480,000.00 USD | 0.00 USD | 10,480,000.00 USD | 599.05 USD | 28,580.00 USD | 3.94 USD |
| `7D` | `245.50` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 4,450.00 USD | 6,920.00 USD | 7,880.00 USD |
| `7D` | `245.90` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 11,770.00 USD | 10,460.00 USD | 0.56 USD |
| `7D` | `246.30` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 11,640.00 USD | 11,210.00 USD | 7,710.00 USD |
| `7D` | `246.70` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 4,590.00 USD | 0.00 USD | 8.17 USD |
| `7D` | `247.10` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 14,580.00 USD | 17,540.00 USD | 4,420.00 USD |
| `7D` | `247.50` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 9,000.00 USD | 4,870.00 USD | 19.16 USD |
| `7D` | `247.90` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 555.60 USD | 310.87 USD | 3.04 USD |
| `7D` | `248.30` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 5,130.00 USD | 2,370.00 USD | 6,400.00 USD |
| `7D` | `248.70` | 10,310,000.00 USD | 0.00 USD | 10,310,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,670.00 USD |
| `7D` | `249.10` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 16,180.00 USD | 31,600.00 USD | 7,090.00 USD |
| `7D` | `249.50` | 10,160,000.00 USD | 0.00 USD | 10,160,000.00 USD | 46,460.00 USD | 32,910.00 USD | 8,350.00 USD |
| `7D` | `249.90` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 45,500.00 USD | 13,210.00 USD | 30,830.00 USD |
| `7D` | `250.30` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 18,520.00 USD | 38,250.00 USD | 3,460.00 USD |
| `1D` | `250.50` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 13,910.00 USD | 7,570.00 USD | 12,300.00 USD |
| `7D` | `250.70` | 9,920,000.00 USD | 0.00 USD | 9,920,000.00 USD | 34,190.00 USD | 60,940.00 USD | 36,610.00 USD |
| `1D` | `250.90` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD |
| `7D` | `251.10` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 42,800.00 USD | 51,050.00 USD | 12,000.00 USD |
| `1D` | `251.30` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 26,340.00 USD | 22,320.00 USD | 23,580.00 USD |
| `7D` | `251.50` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 12,810.00 USD | 63,290.00 USD | 36,080.00 USD |
| `1D` | `251.70` | 5,190,000.00 USD | 0.00 USD | 5,190,000.00 USD | 27,330.00 USD | 43,370.00 USD | 13,910.00 USD |
| `7D` | `251.90` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 86,720.00 USD | 56,690.00 USD | 36,980.00 USD |
| `1D` | `252.10` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 16,350.00 USD | 5,490.00 USD | 12,440.00 USD |
| `7D` | `252.30` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 51,260.00 USD | 25,300.00 USD | 12,820.00 USD |
| `1D` | `252.50` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 11,020.00 USD | 1,620.00 USD | 6,020.00 USD |
| `7D` | `252.70` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 46,920.00 USD | 19,890.00 USD | 15,340.00 USD |
| `1D` | `252.90` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 772.10 USD | 2,430.00 USD | 1,380.00 USD |
| `7D` | `253.10` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 12,990.00 USD | 27,180.00 USD | 4,290.00 USD |
| `1D` | `253.30` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 12,560.00 USD | 9,050.00 USD | 14,150.00 USD |
| `7D` | `253.50` | 9,180,000.00 USD | 0.00 USD | 9,180,000.00 USD | 26,490.00 USD | 36,470.00 USD | 44,000.00 USD |
| `1D` | `253.70` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 20,160.00 USD | 15,410.00 USD | 12,960.00 USD |
| `7D` | `253.90` | 9,070,000.00 USD | 0.00 USD | 9,070,000.00 USD | 25,260.00 USD | 29,760.00 USD | 22,020.00 USD |
| `1D` | `254.10` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 1,650.00 USD | 7,170.00 USD | 5,880.00 USD |
| `7D` | `254.30` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 40,680.00 USD | 32,450.00 USD | 12,160.00 USD |
| `1D` | `254.50` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 8,310.00 USD | 11,590.00 USD | 3,590.00 USD |
| `7D` | `254.70` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 48,210.00 USD | 37,690.00 USD | 85,600.00 USD |
| `1D` | `254.90` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 9,050.00 USD | 12,090.00 USD | 97.42 USD |
| `7D` | `255.10` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 3,010.00 USD | 12,610.00 USD | 25,470.00 USD |
| `1D` | `255.30` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 9,910.00 USD | 15,990.00 USD | 27,920.00 USD |
| `7D` | `255.50` | 8,690,000.00 USD | 0.00 USD | 8,690,000.00 USD | 50,170.00 USD | 5,330.00 USD | 19,140.00 USD |
| `1D` | `255.70` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 17,660.00 USD | 25,900.00 USD | 17,680.00 USD |
| `7D` | `255.90` | 8,620,000.00 USD | 0.00 USD | 8,620,000.00 USD | 7,460.00 USD | 20,140.00 USD | 30,290.00 USD |
| `1D` | `256.10` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 10,050.00 USD | 21,990.00 USD | 17,020.00 USD |
| `7D` | `256.30` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 46,870.00 USD | 9,520.00 USD | 22,590.00 USD |
| `1D` | `256.50` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 8,450.00 USD | 21,060.00 USD | 13,900.00 USD |
| `7D` | `256.70` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 31,480.00 USD | 11,630.00 USD | 54,950.00 USD |
| `1D` | `256.90` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 6,970.00 USD | 6,030.00 USD | 10,290.00 USD |
| `7D` | `257.10` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 14,870.00 USD | 9,760.00 USD | 20,550.00 USD |
| `1D` | `257.30` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 11,120.00 USD | 13,350.00 USD | 15,490.00 USD |
| `7D` | `257.50` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 19,860.00 USD | 10,920.00 USD | 23,770.00 USD |
| `1D` | `257.70` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 2,380.00 USD | 4,780.00 USD | 4,830.00 USD |
| `7D` | `257.90` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 17,330.00 USD | 7,290.00 USD | 7,980.00 USD |
| `1D` | `258.10` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 19,830.00 USD | 2,310.00 USD | 46,990.00 USD |
| `7D` | `258.30` | 8,250,000.00 USD | 0.00 USD | 8,250,000.00 USD | 98,040.00 USD | 34,930.00 USD | 71,490.00 USD |
| `1D` | `258.50` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 100,340.00 USD | 4,180.00 USD | 36,960.00 USD |
| `1D` | `258.90` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,040.00 USD |
| `7D` | `259.10` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 19,700.00 USD | 17,770.00 USD | 26,390.00 USD |
| `1D` | `259.30` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD |
| `7D` | `259.50` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 5,720.00 USD | 34,490.00 USD | 17,010.00 USD |
| `1D` | `259.70` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,290.00 USD |
| `7D` | `259.90` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 95,750.00 USD | 56,770.00 USD | 97,270.00 USD |
| `1D` | `260.10` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 39,470.00 USD | 8,640.00 USD | 6,860.00 USD |
| `7D` | `260.30` | 7,540,000.00 USD | 0.00 USD | 7,540,000.00 USD | 25,040.00 USD | 11,780.00 USD | 60,860.00 USD |
| `1D` | `260.50` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 19,000.00 USD | 1,900.00 USD | 27,220.00 USD |
| `7D` | `260.70` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 15,620.00 USD | 46,940.00 USD | 60,150.00 USD |
| `1D` | `260.90` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 9,090.00 USD | 50,950.00 USD | 13,930.00 USD |
| `7D` | `261.10` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 6,540.00 USD | 64,780.00 USD | 16,020.00 USD |
| `1D` | `261.30` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 8,200.00 USD | 29,340.00 USD | 33,390.00 USD |
| `7D` | `261.50` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 15,880.00 USD | 97,480.00 USD | 43,170.00 USD |
| `1D` | `261.70` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 15,340.00 USD | 60,900.00 USD | 51,220.00 USD |
| `7D` | `261.90` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 54,070.00 USD | 37,130.00 USD | 46,190.00 USD |
| `1D` | `262.10` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 13,720.00 USD | 28,450.00 USD | 21,380.00 USD |
| `7D` | `262.30` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 43,400.00 USD | 76,260.00 USD | 40,510.00 USD |
| `1D` | `262.50` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 21,220.00 USD | 5,730.00 USD | 10,870.00 USD |
| `7D` | `262.70` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 55,510.00 USD | 49,160.00 USD | 26,820.00 USD |
| `1D` | `262.90` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 629.76 USD | 12,730.00 USD | 19,490.00 USD |
| `7D` | `263.10` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 37,610.00 USD | 13,710.00 USD | 5,990.00 USD |
| `1D` | `263.30` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,510.00 USD |
| `7D` | `263.50` | 6,580,000.00 USD | 0.00 USD | 6,580,000.00 USD | 179,320.00 USD | 1,880.00 USD | 83,210.00 USD |
| `1D` | `263.70` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,370.00 USD |
| `7D` | `263.90` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 236,080.00 USD | 629.16 USD | 34,770.00 USD |
| `1D` | `264.10` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,350.00 USD |
| `7D` | `264.30` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 39,870.00 USD | 1,170.00 USD | 112.61 USD |
| `1D` | `264.50` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 1,300.00 USD | 20,340.00 USD | 23.42 USD |
| `7D` | `264.70` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 33,280.00 USD | 21,870.00 USD | 124.07 USD |
| `1D` | `264.90` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 33,390.00 USD | 2,430.00 USD | 53,210.00 USD |
| `7D` | `265.10` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 94,300.00 USD | 2,340.00 USD | 33,870.00 USD |
| `1D` | `265.30` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 65,040.00 USD | 2,840.00 USD | 12.92 USD |
| `7D` | `265.50` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 195,260.00 USD | 1,420.00 USD | 14.32 USD |
| `1D` | `265.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 436.52 USD | 812.59 USD | 0.00 USD |
| `7D` | `265.90` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 58,470.00 USD | 0.00 USD | 117.36 USD |
| `1D` | `266.10` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 16,410.00 USD | 13,470.00 USD | 5.24 USD |
| `7D` | `266.30` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 194,070.00 USD | 2,170.00 USD | 182.70 USD |
| `1D` | `266.50` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 14,430.00 USD | 9,090.00 USD | 4,810.00 USD |
| `7D` | `266.70` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 86,630.00 USD | 63,260.00 USD | 41.29 USD |
| `1D` | `266.90` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 18,470.00 USD | 23,750.00 USD | 7.21 USD |
| `7D` | `267.10` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 117,200.00 USD | 26,850.00 USD | 181.13 USD |
| `1D` | `267.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 33,620.00 USD | 70,000.00 USD | 12,580.00 USD |
| `7D` | `267.50` | 5,080,000.00 USD | 0.00 USD | 5,080,000.00 USD | 102,500.00 USD | 61,270.00 USD | 38,650.00 USD |
| `1D` | `267.70` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 10,460.00 USD | 36,440.00 USD | 28,700.00 USD |
| `7D` | `267.90` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 233,930.00 USD | 25,100.00 USD | 106.37 USD |
| `1D` | `268.10` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 19,060.00 USD | 28,480.00 USD | 60,070.00 USD |
| `7D` | `268.30` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 144,970.00 USD | 124,980.00 USD | 95,890.00 USD |
| `1D` | `268.50` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 18,310.00 USD | 18,920.00 USD | 69.78 USD |
| `7D` | `268.70` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 0.00 USD | 18,320.00 USD | 38.38 USD |
| `1D` | `268.90` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 21,330.00 USD | 11,500.00 USD | 284.39 USD |
| `7D` | `269.10` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 23,340.00 USD | 1,560.00 USD | 232.27 USD |
| `1D` | `269.30` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 11,120.00 USD | 2,950.00 USD | 8,290.00 USD |
| `7D` | `269.50` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 0.00 USD | 2,540.00 USD | 8.52 USD |
| `1D` | `269.70` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 6,590.00 USD | 19,580.00 USD | 13,600.00 USD |
| `7D` | `269.90` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 0.00 USD | 2,250.00 USD | 0.00 USD |
| `1D` | `270.10` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 17,110.00 USD | 13,590.00 USD | 3,540.00 USD |
| `1D` | `270.50` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 48,700.00 USD | 3,090.00 USD | 4,930.00 USD |
| `7D` | `270.70` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 33,050.00 USD | 970.20 USD | 0.00 USD |
| `1D` | `270.90` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 612.40 USD | 17,770.00 USD | 0.00 USD |
| `7D` | `271.10` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 957.20 USD | 0.00 USD |
| `1D` | `271.30` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 12,710.00 USD | 2,140.00 USD | 16,960.00 USD |
| `7D` | `271.50` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 61,340.00 USD |
| `1D` | `271.70` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 8,650.00 USD | 36,810.00 USD | 8,910.00 USD |
| `7D` | `271.90` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 61,810.00 USD | 7,250.00 USD | 20,580.00 USD |
| `1D` | `272.10` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 21,980.00 USD | 24,560.00 USD | 19,760.00 USD |
| `7D` | `272.30` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 8,490.00 USD | 41,370.00 USD | 47,590.00 USD |
| `7D` | `272.70` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 25,660.00 USD | 17,630.00 USD | 77,650.00 USD |
| `1D` | `272.90` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 66,940.00 USD | 15,170.00 USD | 80,630.00 USD |
| `7D` | `273.10` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 147,420.00 USD | 137,700.00 USD |
| `1D` | `273.30` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 30,950.00 USD | 123,250.00 USD | 43,190.00 USD |
| `7D` | `273.50` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 114,750.00 USD |
| `1D` | `273.70` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 60,550.00 USD | 67,190.00 USD | 69,760.00 USD |
| `7D` | `273.90` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 337,830.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.10` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 152,290.00 USD | 44,080.00 USD | 12,160.00 USD |
| `7D` | `274.30` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 380,220.00 USD | 46,000.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 165,560.00 USD | 44,750.00 USD | 63,330.00 USD |
| `7D` | `274.70` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 427,250.00 USD | 22,090.00 USD | 68,450.00 USD |
| `1D` | `274.90` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 54,360.00 USD | 22,510.00 USD | 20,440.00 USD |
| `7D` | `275.10` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 139,440.00 USD | 0.00 USD | 10.44 USD |
| `1D` | `275.30` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 11,720.00 USD | 3,760.00 USD | 14,350.00 USD |
| `7D` | `275.50` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 2,590.00 USD | 19,960.00 USD | 109.48 USD |
| `1D` | `275.70` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD |
| `7D` | `275.90` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 1,950.00 USD | 23,010.00 USD | 82,420.00 USD |
| `1D` | `276.10` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 172,570.00 USD | 3,340.00 USD | 7,100.00 USD |
| `7D` | `276.30` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 218,450.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 970,360.00 USD | 0.00 USD | 970,360.00 USD | 11,920.00 USD | 16,150.00 USD | 18,690.00 USD |
| `7D` | `276.70` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 5.55 USD |
| `1D` | `276.90` | 923,600.00 USD | 0.00 USD | 923,600.00 USD | 37,290.00 USD | 25,410.00 USD | 33,920.00 USD |
| `7D` | `277.10` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 44,670.00 USD | 0.00 USD | 122,630.00 USD |
| `1D` | `277.30` | 826,990.00 USD | 0.00 USD | 826,990.00 USD | 17,610.00 USD | 22,050.00 USD | 17,800.00 USD |
| `7D` | `277.50` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 123,610.00 USD | 235,540.00 USD | 59,530.00 USD |
| `1D` | `277.70` | 769,530.00 USD | 0.00 USD | 769,530.00 USD | 13,750.00 USD | 16,920.00 USD | 20,310.00 USD |
| `7D` | `277.90` | 825,910.00 USD | 0.00 USD | 825,910.00 USD | 0.00 USD | 1,830.00 USD | 60,010.00 USD |
| `1D` | `278.10` | 718,540.00 USD | 0.00 USD | 718,540.00 USD | 16,630.00 USD | 103,670.00 USD | 95,180.00 USD |
| `7D` | `278.30` | 764,070.00 USD | 0.00 USD | 764,070.00 USD | 24,750.00 USD | 35,270.00 USD | 155,380.00 USD |
| `1D` | `278.50` | 503,080.00 USD | 0.00 USD | 503,080.00 USD | 93,830.00 USD | 76,370.00 USD | 65,840.00 USD |
| `7D` | `278.70` | 548,670.00 USD | 0.00 USD | 548,670.00 USD | 51,310.00 USD | 49,750.00 USD | 23,940.00 USD |
| `1D` | `278.90` | 267,040.00 USD | 0.00 USD | 267,040.00 USD | 23,710.00 USD | 14,630.00 USD | 5,500.00 USD |
| `1D` | `279.30` | 223,210.00 USD | 0.00 USD | 223,210.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD |
| `7D` | `279.50` | 423,660.00 USD | 0.00 USD | 423,660.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 182,120.00 USD | 0.00 USD | 182,120.00 USD | 0.00 USD | 0.00 USD | 24,330.00 USD |
| `1D` | `280.10` | 157,790.00 USD | 0.00 USD | 157,790.00 USD | 15,540.00 USD | 59,700.00 USD | 49,950.00 USD |
| `7D` | `280.30` | 421,000.00 USD | 0.00 USD | 421,000.00 USD | 0.00 USD | 22,070.00 USD | 0.00 USD |
| `1D` | `280.50` | 32,610.00 USD | 0.00 USD | 32,610.00 USD | 0.00 USD | 0.00 USD | 7,810.00 USD |
| `7D` | `280.70` | 398,920.00 USD | 0.00 USD | 398,920.00 USD | 29,850.00 USD | 54,170.00 USD | 67,450.00 USD |
| `1D` | `280.90` | 24,800.00 USD | 0.00 USD | 24,800.00 USD | 0.00 USD | 0.00 USD | 14.16 USD |
| `7D` | `281.10` | 247,450.00 USD | 0.00 USD | 247,450.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD |
| `1D` | `281.30` | 24,790.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 15,220.00 USD |
| `7D` | `281.50` | 153,630.00 USD | 0.00 USD | 153,630.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `7D` | `281.90` | 31,240.00 USD | 0.00 USD | 31,240.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.10` | 9,560.00 USD | 0.00 USD | 9,560.00 USD | 8,260.00 USD | 0.00 USD | 5.66 USD |
| `7D` | `282.30` | 10,540.00 USD | 0.00 USD | 10,540.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.10` | 7,020.00 USD | 0.00 USD | 7,020.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.30` | 1,300.00 USD | 0.00 USD | 1,300.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.90` | 3,570.00 USD | 0.00 USD | 3,570.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 15.61 USD | 0.00 USD | 15.61 USD | 0.00 USD | 0.00 USD | 15.61 USD |
| `7D` | `284.30` | 1,570.00 USD | 0.00 USD | 1,570.00 USD | 1,560.00 USD | 0.00 USD | 12.00 USD |
| `1D` | `284.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.70` | 65.52 USD | 65.52 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65.52 USD |
| `1D` | `284.90` | 18.94 USD | 18.94 USD | 0.00 USD | 0.00 USD | 0.00 USD | 18.94 USD |
| `7D` | `285.10` | 327,980.00 USD | 327,980.00 USD | 0.00 USD | 125,000.00 USD | 137,110.00 USD | 65,810.00 USD |
| `1D` | `285.30` | 78,310.00 USD | 78,310.00 USD | 0.00 USD | 36,620.00 USD | 0.00 USD | 41,670.00 USD |
| `7D` | `285.50` | 402,850.00 USD | 402,850.00 USD | 0.00 USD | 5,350.00 USD | 69,520.00 USD | 0.00 USD |
| `1D` | `285.70` | 80,020.00 USD | 80,020.00 USD | 0.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `285.90` | 406,730.00 USD | 406,730.00 USD | 0.00 USD | 1,200.00 USD | 2,690.00 USD | 0.00 USD |
| `1D` | `286.10` | 84,420.00 USD | 84,420.00 USD | 0.00 USD | 4,360.00 USD | 0.00 USD | 30.67 USD |
| `7D` | `286.30` | 409,070.00 USD | 409,070.00 USD | 0.00 USD | 0.00 USD | 2,340.00 USD | 0.00 USD |
| `1D` | `286.50` | 99,900.00 USD | 99,900.00 USD | 0.00 USD | 11,720.00 USD | 3,760.00 USD | 4.24 USD |
| `7D` | `286.70` | 411,710.00 USD | 411,710.00 USD | 0.00 USD | 2,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `286.90` | 170,140.00 USD | 170,140.00 USD | 0.00 USD | 45,630.00 USD | 24,600.00 USD | 14.24 USD |
| `7D` | `287.10` | 418,970.00 USD | 418,970.00 USD | 0.00 USD | 3,620.00 USD | 3,640.00 USD | 0.00 USD |
| `1D` | `287.30` | 309,730.00 USD | 309,730.00 USD | 0.00 USD | 108,880.00 USD | 30,710.00 USD | 0.00 USD |
| `7D` | `287.50` | 424,640.00 USD | 424,640.00 USD | 0.00 USD | 3,420.00 USD | 2,150.00 USD | 103.44 USD |
| `1D` | `287.70` | 366,010.00 USD | 366,010.00 USD | 0.00 USD | 22,860.00 USD | 33,420.00 USD | 0.00 USD |
| `7D` | `287.90` | 427,250.00 USD | 427,250.00 USD | 0.00 USD | 2,580.00 USD | 0.00 USD | 23.40 USD |
| `1D` | `288.10` | 458,400.00 USD | 458,400.00 USD | 0.00 USD | 21,420.00 USD | 26,660.00 USD | 44,310.00 USD |
| `7D` | `288.30` | 470,460.00 USD | 470,460.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD | 41,660.00 USD |
| `1D` | `288.50` | 576,920.00 USD | 576,920.00 USD | 0.00 USD | 52,260.00 USD | 29,840.00 USD | 36,410.00 USD |
| `7D` | `288.70` | 731,850.00 USD | 731,850.00 USD | 0.00 USD | 123,610.00 USD | 15,650.00 USD | 122,130.00 USD |
| `1D` | `288.90` | 652,250.00 USD | 652,250.00 USD | 0.00 USD | 44,740.00 USD | 30,590.00 USD | 0.00 USD |
| `7D` | `289.10` | 793,810.00 USD | 793,810.00 USD | 0.00 USD | 1,170.00 USD | 932.60 USD | 59,860.00 USD |
| `1D` | `289.30` | 767,800.00 USD | 767,800.00 USD | 0.00 USD | 17,220.00 USD | 47,120.00 USD | 51,200.00 USD |
| `7D` | `289.50` | 820,920.00 USD | 820,920.00 USD | 0.00 USD | 0.00 USD | 27,110.00 USD | 0.00 USD |
| `1D` | `289.70` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 71,760.00 USD | 86,660.00 USD | 121,600.00 USD |
| `7D` | `289.90` | 1,140,000.00 USD | 1,140,000.00 USD | 0.00 USD | 52,840.00 USD | 73,930.00 USD | 193,880.00 USD |
| `1D` | `290.10` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 65,110.00 USD | 58,580.00 USD | 114,510.00 USD |
| `7D` | `290.30` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 34,580.00 USD | 49,750.00 USD | 23,940.00 USD |
| `1D` | `290.50` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 32,450.00 USD | 123,930.00 USD | 52,120.00 USD |
| `7D` | `290.70` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 30,940.00 USD | 861.99 USD | 32,900.00 USD |
| `1D` | `290.90` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 57,770.00 USD | 47,340.00 USD | 41,080.00 USD |
| `7D` | `291.10` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 18,380.00 USD | 58,050.00 USD |
| `1D` | `291.30` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 27,020.00 USD | 25,140.00 USD | 42,930.00 USD |
| `7D` | `291.50` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 27,390.00 USD | 78,710.00 USD | 19,450.00 USD |
| `1D` | `291.70` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 28,390.00 USD | 71,460.00 USD | 30,410.00 USD |
| `7D` | `291.90` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 25,610.00 USD | 175,760.00 USD | 67,500.00 USD |
| `1D` | `292.10` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 6,710.00 USD | 15,850.00 USD | 19,300.00 USD |
| `7D` | `292.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 1,240.00 USD | 72,680.00 USD | 25.48 USD |
| `1D` | `292.50` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 29,880.00 USD | 3,650.00 USD | 17,460.00 USD |
| `7D` | `292.70` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 887.27 USD | 87,810.00 USD | 30.72 USD |
| `1D` | `292.90` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 62,510.00 USD | 27,920.00 USD | 3,560.00 USD |
| `7D` | `293.10` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 145,540.00 USD | 9.54 USD |
| `1D` | `293.30` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 27,950.00 USD | 15,280.00 USD | 32,300.00 USD |
| `7D` | `293.50` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 33,580.00 USD | 694.90 USD | 38.07 USD |
| `1D` | `293.70` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 76,710.00 USD | 47,640.00 USD | 70,140.00 USD |
| `7D` | `293.90` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 53,080.00 USD | 21,610.00 USD | 65,850.00 USD |
| `1D` | `294.10` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 21,460.00 USD | 25,650.00 USD | 52,800.00 USD |
| `7D` | `294.30` | 2,620,000.00 USD | 2,620,000.00 USD | 0.00 USD | 202,860.00 USD | 22,540.00 USD | 121,730.00 USD |
| `1D` | `294.50` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 96,690.00 USD | 80,200.00 USD | 85,230.00 USD |
| `7D` | `294.70` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 16,110.00 USD | 93,810.00 USD | 89,170.00 USD |
| `1D` | `294.90` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 33,490.00 USD | 17,570.00 USD | 48,710.00 USD |
| `7D` | `295.10` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 48,390.00 USD | 16,140.00 USD | 214,360.00 USD |
| `1D` | `295.30` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 18,010.00 USD | 65,340.00 USD | 102,520.00 USD |
| `7D` | `295.50` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 167,940.00 USD | 155,660.00 USD | 280,120.00 USD |
| `1D` | `295.70` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 106,670.00 USD | 16,690.00 USD | 137,430.00 USD |
| `7D` | `295.90` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 59,330.00 USD | 114,600.00 USD | 60,600.00 USD |
| `1D` | `296.10` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 55,060.00 USD | 128,640.00 USD | 38,410.00 USD |
| `7D` | `296.30` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 27,350.00 USD | 78,210.00 USD | 120,900.00 USD |
| `1D` | `296.50` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 33,430.00 USD | 22,420.00 USD | 41,240.00 USD |
| `7D` | `296.70` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 119,280.00 USD | 4,410.00 USD | 173,720.00 USD |
| `1D` | `296.90` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 24,280.00 USD | 28,310.00 USD | 90,450.00 USD |
| `7D` | `297.10` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 89,710.00 USD | 62,630.00 USD | 27,840.00 USD |
| `1D` | `297.30` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 69,150.00 USD | 24,320.00 USD | 40,960.00 USD |
| `7D` | `297.50` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 16,090.00 USD | 83,510.00 USD | 68,480.00 USD |
| `1D` | `297.70` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 15,920.00 USD | 11,900.00 USD | 15,990.00 USD |
| `7D` | `297.90` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 47,790.00 USD | 42,380.00 USD | 54,850.00 USD |
| `1D` | `298.10` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 52,050.00 USD | 10,350.00 USD | 41,590.00 USD |
| `7D` | `298.30` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 32,250.00 USD | 45,480.00 USD | 68,810.00 USD |
| `1D` | `298.50` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 5,990.00 USD | 1,730.00 USD | 64,000.00 USD |
| `7D` | `298.70` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 69,820.00 USD | 11,780.00 USD | 4.18 USD |
| `1D` | `298.90` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 28,550.00 USD | 5,830.00 USD | 94,680.00 USD |
| `7D` | `299.10` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 1,800.00 USD | 3,050.00 USD | 85,960.00 USD |
| `1D` | `299.30` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 34,220.00 USD | 11,020.00 USD | 12,340.00 USD |
| `7D` | `299.50` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 3,930.00 USD | 27,060.00 USD | 76.34 USD |
| `1D` | `299.70` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 8,350.00 USD | 12,170.00 USD | 27,690.00 USD |
| `7D` | `299.90` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 54,340.00 USD | 11,070.00 USD | 19,940.00 USD |
| `1D` | `300.10` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 20,020.00 USD | 37,720.00 USD | 64,340.00 USD |
| `7D` | `300.30` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 128.31 USD |
| `1D` | `300.50` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 23,270.00 USD | 1,650.00 USD | 17,170.00 USD |
| `7D` | `300.70` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 25,350.00 USD | 71,120.00 USD | 19,770.00 USD |
| `1D` | `300.90` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 444.05 USD | 1,220.00 USD | 29,460.00 USD |
| `7D` | `301.10` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 25,570.00 USD | 33,490.00 USD | 119,600.00 USD |
| `1D` | `301.30` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 693.10 USD | 15,110.00 USD | 20,930.00 USD |
| `7D` | `301.50` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 85,980.00 USD | 88,000.00 USD | 59,490.00 USD |
| `1D` | `301.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 19,840.00 USD | 8,470.00 USD | 15,530.00 USD |
| `7D` | `301.90` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 51,660.00 USD | 123,250.00 USD | 26,360.00 USD |
| `1D` | `302.10` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 25,190.00 USD | 30,660.00 USD | 10,490.00 USD |
| `7D` | `302.30` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 1,560.00 USD | 126,650.00 USD | 44.13 USD |
| `1D` | `302.50` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 13,920.00 USD | 13,700.00 USD | 38,400.00 USD |
| `7D` | `302.70` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 71,700.00 USD | 72,000.00 USD | 41,940.00 USD |
| `1D` | `302.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 1,440.00 USD | 2,520.00 USD | 13,980.00 USD |
| `7D` | `303.10` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 42,380.00 USD | 61.63 USD |
| `1D` | `303.30` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 21,400.00 USD | 2,940.00 USD | 9,360.00 USD |
| `7D` | `303.50` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 75.43 USD |
| `1D` | `303.70` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 248.72 USD | 573.99 USD | 0.00 USD |
| `7D` | `303.90` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 21,140.00 USD | 11,740.00 USD | 45,830.00 USD |
| `1D` | `304.10` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 22,000.00 USD | 1,990.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 6,560,000.00 USD | 6,560,000.00 USD | 0.00 USD | 2,070.00 USD | 4,320.00 USD | 153.40 USD |
| `1D` | `304.50` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 9,670.00 USD | 2,380.00 USD | 44,530.00 USD |
| `7D` | `304.70` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 2,950.00 USD | 12,510.00 USD | 2,160.00 USD |
| `1D` | `304.90` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 9,920.00 USD | 8,610.00 USD | 2,040.00 USD |
| `7D` | `305.10` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 128,400.00 USD | 128,260.00 USD | 84,430.00 USD |
| `1D` | `305.30` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 83.23 USD | 172.52 USD | 1.30 USD |
| `7D` | `305.50` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 93,400.00 USD | 19,010.00 USD | 48,240.00 USD |
| `1D` | `305.70` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 6,340.00 USD | 3,650.00 USD | 5,870.00 USD |
| `7D` | `305.90` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 56,810.00 USD | 53,540.00 USD | 3,470.00 USD |
| `1D` | `306.10` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 7,500.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 29,420.00 USD | 57,910.00 USD | 63,700.00 USD |
| `1D` | `306.50` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 4,330.00 USD | 6.13 USD | 5,670.00 USD |
| `7D` | `306.70` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 27,190.00 USD | 44,210.00 USD | 69,990.00 USD |
| `1D` | `306.90` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 19,810.00 USD | 35,610.00 USD | 18,570.00 USD |
| `7D` | `307.10` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 74,130.00 USD | 89,830.00 USD | 98,860.00 USD |
| `1D` | `307.30` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 11,240.00 USD | 32,670.00 USD | 22,250.00 USD |
| `7D` | `307.50` | 7,980,000.00 USD | 7,980,000.00 USD | 0.00 USD | 62,450.00 USD | 114,390.00 USD | 54,870.00 USD |
| `1D` | `307.70` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 24,280.00 USD | 20,210.00 USD | 3,730.00 USD |
| `7D` | `307.90` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 125,550.00 USD | 101,520.00 USD | 59,240.00 USD |
| `1D` | `308.10` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 14,750.00 USD | 4,740.00 USD | 12,420.00 USD |
| `7D` | `308.30` | 8,540,000.00 USD | 8,540,000.00 USD | 0.00 USD | 128,880.00 USD | 41,210.00 USD | 109,610.00 USD |
| `1D` | `308.50` | 5,150,000.00 USD | 5,150,000.00 USD | 0.00 USD | 3,040.00 USD | 212.94 USD | 2,510.00 USD |
| `7D` | `308.70` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 67,430.00 USD | 31,490.00 USD | 15,370.00 USD |
| `1D` | `308.90` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD |
| `7D` | `309.10` | 8,780,000.00 USD | 8,780,000.00 USD | 0.00 USD | 38,660.00 USD | 39,620.00 USD | 39,820.00 USD |
| `1D` | `309.30` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 3,240.00 USD | 2,300.00 USD | 1,370.00 USD |
| `7D` | `309.50` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 47,160.00 USD | 51,160.00 USD | 95,340.00 USD |
| `1D` | `309.70` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 10,120.00 USD | 7,750.00 USD | 1,420.00 USD |
| `7D` | `309.90` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 19,540.00 USD | 106,330.00 USD | 75,910.00 USD |
| `1D` | `310.10` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 13,080.00 USD | 4,100.00 USD | 12,940.00 USD |
| `7D` | `310.30` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 61,040.00 USD | 107,890.00 USD | 76,890.00 USD |
| `1D` | `310.50` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 176.40 USD | 5,020.00 USD | 5,870.00 USD |
| `7D` | `310.70` | 9,530,000.00 USD | 9,530,000.00 USD | 0.00 USD | 60,380.00 USD | 50,820.00 USD | 3,820.00 USD |
| `1D` | `310.90` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 5,080.00 USD | 73.70 USD | 2,100.00 USD |
| `7D` | `311.10` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 59,270.00 USD | 59,630.00 USD | 72,130.00 USD |
| `1D` | `311.30` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 257.90 USD | 3,110.00 USD | 1,480.00 USD |
| `7D` | `311.50` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 55,980.00 USD | 6,680.00 USD | 13,870.00 USD |
| `1D` | `311.70` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 7,980.00 USD | 10,410.00 USD | 4,140.00 USD |
| `7D` | `311.90` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 39,900.00 USD | 11,610.00 USD | 19,880.00 USD |
| `1D` | `312.10` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 299.35 USD | 10,630.00 USD | 15,040.00 USD |
| `7D` | `312.30` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 23,020.00 USD | 11,240.00 USD | 27,510.00 USD |
| `1D` | `312.50` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 17,660.00 USD | 11,130.00 USD | 17,680.00 USD |
| `7D` | `312.70` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 8,290.00 USD | 19,990.00 USD | 12,120.00 USD |
| `1D` | `312.90` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 9,040.00 USD | 1,710.00 USD | 6,510.00 USD |
| `7D` | `313.10` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 28,080.00 USD | 11,540.00 USD | 29,990.00 USD |
| `1D` | `313.30` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 3,700.00 USD | 18,390.00 USD | 3,670.00 USD |
| `7D` | `313.50` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 13,630.00 USD | 116.35 USD | 27,750.00 USD |
| `1D` | `313.70` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 4,610.00 USD | 4,610.00 USD | 8,220.00 USD |
| `7D` | `313.90` | 10,160,000.00 USD | 10,160,000.00 USD | 0.00 USD | 32,050.00 USD | 1,450.00 USD | 43,030.00 USD |
| `1D` | `314.10` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 2,760.00 USD | 8,290.00 USD |
| `7D` | `314.30` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 51,980.00 USD | 4,720.00 USD | 24,540.00 USD |
| `1D` | `314.50` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 7,350.00 USD | 9,390.00 USD | 12,050.00 USD |
| `7D` | `314.70` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 433.10 USD | 8,840.00 USD | 23,800.00 USD |
| `1D` | `314.90` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 3,750.00 USD | 4,830.00 USD |
| `7D` | `315.10` | 10,290,000.00 USD | 10,290,000.00 USD | 0.00 USD | 17,280.00 USD | 258.00 USD | 0.00 USD |
| `1D` | `315.30` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 2,100.00 USD | 1,550.00 USD | 1,620.00 USD |
| `7D` | `315.50` | 10,310,000.00 USD | 10,310,000.00 USD | 0.00 USD | 478.19 USD | 181.20 USD | 12,650.00 USD |
| `1D` | `315.70` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 1,850.00 USD | 0.00 USD | 8,270.00 USD |
| `7D` | `315.90` | 10,400,000.00 USD | 10,400,000.00 USD | 0.00 USD | 39,580.00 USD | 33,520.00 USD | 17,340.00 USD |
| `1D` | `316.10` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | 5,600.00 USD |
| `7D` | `316.30` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 451.45 USD | 19,680.00 USD | 43,450.00 USD |
| `1D` | `316.50` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 20.15 USD | 3,570.00 USD | 0.00 USD |
| `7D` | `316.70` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 18,110.00 USD | 20,380.00 USD | 18,370.00 USD |
| `1D` | `316.90` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 12,960.00 USD | 2,360.00 USD | 10,200.00 USD |
| `7D` | `317.10` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 1,810.00 USD | 1,110.00 USD | 171.23 USD |
| `1D` | `317.30` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 2,190.00 USD | 5,580.00 USD |
| `7D` | `317.50` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 14,400.00 USD | 574.27 USD | 76.60 USD |
| `1D` | `317.60` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 8,410.00 USD | 8,940.00 USD | 0.00 USD |
| `7D` | `317.90` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 21,020.00 USD | 8,660.00 USD | 143.05 USD |
| `7D` | `318.30` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 3,320.00 USD | 31,110.00 USD | 32,020.00 USD |
| `7D` | `318.70` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 9,900.00 USD | 17,490.00 USD | 14,050.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.68M` | Total OI Tokens: `1,079,593.3 BCH`
  * 1h OI Change: `+1.73%` | 4h OI Change: `+0.21%` | 24h OI Change: `+0.15%`
  * Exchange Breakdown: Binance=`89.04M` | Bybit=`38.35M` | OKX=`24.49M` | Hyperliquid=`7.30M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.30K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0090%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `37.64%` | `62.36%` | `0.60` | 11,710,000.00 USD |
| `15M` | `Binance` | `43.24%` | `56.76%` | `0.76` | 3,470,000.00 USD |
| `15M` | `OKX` | `26.21%` | `73.79%` | `0.36` | 1,180,000.00 USD |
| `15M` | `Bybit` | `33.24%` | `66.76%` | `0.50` | 1,540,000.00 USD |
| `15M` | `KuCoin` | `34.49%` | `65.51%` | `0.53` | 67,350.00 USD |
| `15M` | `Gate` | `20.73%` | `79.27%` | `0.26` | 289,010.00 USD |
| `15M` | `Bitget` | `41.69%` | `58.31%` | `0.71` | 556,150.00 USD |
| `15M` | `BingX` | `63.83%` | `36.17%` | `1.76` | 565,740.00 USD |
| `15M` | `MEXC` | `20.21%` | `79.79%` | `0.25` | 986,090.00 USD |
| `15M` | `Bitunix` | `63.68%` | `36.32%` | `1.75` | 217,630.00 USD |
| `15M` | `Hyperliquid` | `36.43%` | `63.57%` | `0.57` | 1,040,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.14%` | `46.86%` | `1.13` | 133,750.00 USD |
| `15M` | `Crypto.com` | `5.02%` | `94.98%` | `0.05` | 1,810.00 USD |
| `15M` | `WhiteBIT` | `36.97%` | `63.03%` | `0.59` | 1,600,000.00 USD |
| `15M` | `HTX` | `90.95%` | `9.05%` | `10.05` | 1,820.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `48.45%` | `51.55%` | `0.94` | 34,880.00 USD |
| `15M` | `Aster` | `61.4%` | `38.6%` | `1.59` | 3,030.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.1%` | `56.9%` | `0.76` | 29,650.00 USD |
| `15M` | `Whale Positions` | `43.24%` | `56.76%` | `0.76` | 3,470,000.00 USD |
| `15M` | `Global Accounts` | `37.64%` | `62.36%` | `0.60` | 11,710,000.00 USD |
| `1H` | `BCH` | `55.46%` | `44.54%` | `1.25` | 15,250,000.00 USD |
| `1H` | `Binance` | `52.75%` | `47.25%` | `1.12` | 5,070,000.00 USD |
| `1H` | `OKX` | `37.4%` | `62.6%` | `0.60` | 2,170,000.00 USD |
| `1H` | `Bybit` | `37.97%` | `62.03%` | `0.61` | 1,140,000.00 USD |
| `1H` | `KuCoin` | `58.09%` | `41.91%` | `1.39` | 75,160.00 USD |
| `1H` | `Gate` | `58.51%` | `41.49%` | `1.41` | 1,100,000.00 USD |
| `1H` | `Bitget` | `62.42%` | `37.58%` | `1.66` | 567,380.00 USD |
| `1H` | `BingX` | `50.95%` | `49.05%` | `1.04` | 1,770,000.00 USD |
| `1H` | `MEXC` | `33.8%` | `66.2%` | `0.51` | 350,820.00 USD |
| `1H` | `Bitunix` | `66.17%` | `33.83%` | `1.96` | 309,620.00 USD |
| `1H` | `Hyperliquid` | `23.87%` | `76.13%` | `0.31` | 91,310.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.7%` | `50.3%` | `0.99` | 466,360.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.28%` | `2.72%` | `35.76` | 1,890,000.00 USD |
| `1H` | `HTX` | `83.45%` | `16.55%` | `5.04` | 50,340.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `83.08%` | `16.92%` | `4.91` | 123,460.00 USD |
| `1H` | `Aster` | `70.48%` | `29.52%` | `2.39` | 44,270.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `9.45%` | `90.55%` | `0.10` | 31,690.00 USD |
| `1H` | `Whale Positions` | `52.75%` | `47.25%` | `1.12` | 5,070,000.00 USD |
| `1H` | `Global Accounts` | `55.46%` | `44.54%` | `1.25` | 15,250,000.00 USD |
| `4H` | `BCH` | `49.16%` | `50.84%` | `0.97` | 99,980,000.00 USD |
| `4H` | `Binance` | `47.91%` | `52.09%` | `0.92` | 37,030,000.00 USD |
| `4H` | `OKX` | `45.32%` | `54.68%` | `0.83` | 15,140,000.00 USD |
| `4H` | `Bybit` | `47%` | `53%` | `0.89` | 7,720,000.00 USD |
| `4H` | `KuCoin` | `57.01%` | `42.99%` | `1.33` | 1,910,000.00 USD |
| `4H` | `Gate` | `58.64%` | `41.36%` | `1.42` | 2,630,000.00 USD |
| `4H` | `Bitget` | `49.47%` | `50.53%` | `0.98` | 3,920,000.00 USD |
| `4H` | `BingX` | `27.56%` | `72.44%` | `0.38` | 5,700,000.00 USD |
| `4H` | `MEXC` | `49.93%` | `50.07%` | `1.00` | 13,840,000.00 USD |
| `4H` | `Bitunix` | `51.45%` | `48.55%` | `1.06` | 3,280,000.00 USD |
| `4H` | `Hyperliquid` | `35.73%` | `64.27%` | `0.56` | 2,190,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `54.29%` | `45.71%` | `1.19` | 1,100,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.49%` | `6.51%` | `14.36` | 4,470,000.00 USD |
| `4H` | `HTX` | `55.62%` | `44.38%` | `1.25` | 204,310.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `63.98%` | `36.02%` | `1.78` | 687,940.00 USD |
| `4H` | `Aster` | `45.89%` | `54.11%` | `0.85` | 96,370.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.57%` | `59.43%` | `0.68` | 87,090.00 USD |
| `4H` | `Whale Positions` | `47.91%` | `52.09%` | `0.92` | 37,030,000.00 USD |
| `4H` | `Global Accounts` | `49.16%` | `50.84%` | `0.97` | 99,980,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `281.21` | `280.32` | `281.21` | `281.29` | `278.55` | 1,960,555.94 USD | 896,979.92 USD | 1,063,576.02 USD | -166,596.10 USD | `-8.50%` | `26B / 22S` |
| `5:00 UTC` | `279.18` | `279.58` | `279.18` | `280.70` | `279.06` | 617,038.04 USD | 332,886.00 USD | 284,152.04 USD | 48,733.95 USD | `+7.90%` | `32B / 38S` |
| `0:00 UTC` | `279.30` | `281.19` | `279.30` | `282.30` | `278.88` | 2,044,095.31 USD | 958,971.19 USD | 1,085,124.12 USD | -126,152.93 USD | `-6.17%` | `39B / 29S` |
| `5:00 UTC` | `281.23` | `281.19` | `281.23` | `281.62` | `280.50` | 432,406.23 USD | 225,151.97 USD | 207,254.26 USD | 17,897.70 USD | `+4.14%` | `20B / 20S` |
| `0:00 UTC` | `281.00` | `280.46` | `281.00` | `281.14` | `280.02` | 480,699.25 USD | 262,884.90 USD | 217,814.34 USD | 45,070.56 USD | `+9.38%` | `19B / 14S` |
| `5:00 UTC` | `282.00` | `281.11` | `282.00` | `282.22` | `280.16` | 658,245.44 USD | 414,390.84 USD | 243,854.60 USD | 170,536.24 USD | `+25.91%` | `33B / 5S` |
| `0:00 UTC` | `283.69` | `283.66` | `283.69` | `284.99` | `281.57` | 1,404,905.07 USD | 779,041.52 USD | 625,863.54 USD | 153,177.98 USD | `+10.90%` | `46B / 26S` |
| `5:00 UTC` | `284.51` | `284.94` | `284.51` | `286.25` | `283.71` | 898,820.13 USD | 532,011.88 USD | 366,808.25 USD | 165,203.63 USD | `+18.38%` | `37B / 18S` |
| `0:00 UTC` | `285.98` | `286.01` | `285.98` | `287.86` | `284.40` | 1,993,515.84 USD | 980,794.98 USD | 1,012,720.85 USD | -31,925.87 USD | `-1.60%` | `44B / 32S` |
| `5:00 UTC` | `284.28` | `284.45` | `284.28` | `285.18` | `284.06` | 177,514.04 USD | 62,574.54 USD | 114,939.50 USD | -52,364.96 USD | `-29.50%` | `11B / 21S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:52` | `Range 1` | `Divergence` | **`BEARISH`** | Rally without taker buying | `294.56` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.50` | 3,900.00 USD | 0.00 USD |
| `10-28 18:42` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `295.29` | 0.00 USD | 0.00 USD |
| `10-28 16:40` | `Range 1` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `296.45` | 2,100.00 USD | 0.00 USD |
| `10-28 16:31` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.73` | 1,000.00 USD | 0.00 USD |
| `10-28 15:58` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `300.99` | 0.00 USD | 0.00 USD |
| `10-28 15:25` | `Volume 10K BCH` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `304.75` | 0.00 USD | 0.00 USD |
| `10-28 12:36` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.11` | 0.00 USD | 0.00 USD |
| `10-28 11:50` | `Volume 10K BCH` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,500.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Divergence` | **`BULLISH`** | Drop without taker selling | `298.39` | 0.00 USD | 0.00 USD |
| `10-28 11:49` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.58` | 1,100.00 USD | 0.00 USD |
| `10-28 11:32` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `298.10` | 0.00 USD | 0.00 USD |
| `10-28 11:24` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `299.42` | 0.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.64` | 1,000.00 USD | 0.00 USD |
| `10-28 10:10` | `Range 1` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `299.34` | 1,200.00 USD | 0.00 USD |
| `10-28 09:12` | `Range 1` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `297.13` | 0.00 USD | 0.00 USD |
| `10-28 08:27` | `Range 1` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `297.20` | 0.00 USD | 0.00 USD |
| `10-28 07:51` | `Range 1` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `293.25` | 2,500.00 USD | 0.00 USD |
| `10-28 07:41` | `Range 1` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `295.18` | 0.00 USD | 0.00 USD |
| `10-28 06:40` | `Volume 10K BCH` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `293.94` | 2,400.00 USD | 0.00 USD |
| `10-28 06:32` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.42` | 0.00 USD | 0.00 USD |
| `10-28 06:21` | `Range 1` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `293.97` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -29,230.00 USD | -128,080.00 USD | **`DISTRIBUTION`** |
| `15m` | -3,040.00 USD | -1,580,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 62,600.00 USD | -531,750.00 USD | **`DISTRIBUTION`** |
| `1h` | 171,660.00 USD | 159,960.00 USD | **`ACCUMULATION`** |
| `2h` | 261,110.00 USD | 207,480.00 USD | **`ACCUMULATION`** |
| `4h` | 115,780.00 USD | -258,790.00 USD | **`DISTRIBUTION`** |
| `6h` | 305,530.00 USD | -57,310.00 USD | **`ACCUMULATION`** |
| `8h` | 1,010,000.00 USD | -737,340.00 USD | **`ACCUMULATION`** |
| `12h` | 642,650.00 USD | -51,860.00 USD | **`ACCUMULATION`** |
| `24h` | 318,310.00 USD | -1,860,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 17,200.00 USD | -12,330,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,660,000.00 USD | -136,630,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-29.23K` | 15m=`-3.04K` | 1h=`+171.66K` | 24h=`+318.31K`
* Futures Capital Netflows: 5m=`-128.08K` | 15m=`-1.58M` | 1h=`+159.96K` | 24h=`-1.86M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `273.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `271.28` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `278.52`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `284.87` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `286.94` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `279.70`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`285.92`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
