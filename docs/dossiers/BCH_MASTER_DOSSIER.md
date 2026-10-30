# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `278.76` | **Live Ask Quote**: `279.44` | **Mid Price**: `279.10`
- **Spread Points**: `680.00` | **Spread BPS**: `24.36 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `276.45` | VWAP Z-Score: `+0.51` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.13` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `45.28` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.27` | Lower -3.00σ Band: `257.63`
  * Upper +2.51σ Band: `292.20` | Lower -2.51σ Band: `260.70`
  * Upper +2.01σ Band: `289.06` | Lower -2.01σ Band: `263.84`
  * Upper +2.00σ Band: `289.00` | Lower -2.00σ Band: `263.90`
  * Upper +1.28σ Band: `284.48` | Lower -1.28σ Band: `268.42`
  * Upper +1.00σ Band: `282.72` | Lower -1.00σ Band: `270.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`281.79` | EMA-20=`281.55` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.43` (Slope: `+0.0000`) | EMA-100=`280.93`
  * Institutional Anchors: EMA-144=`281.78` | EMA-200=`283.33` (Slope: `-0.0379`) | EMA-233=`284.33`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `281.28` (Distance: `-0.76%`)
  * Point of Control (POC) = `276.23` (Distance: `+1.06%`)
  * Value Area Low (VAL) = `267.54` (Distance: `+4.34%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.76`
  * New York Session (13:00-21:00 UTC): High=`280.77` | Low=`277.43`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `277.98` - `280.22`
  * Optimal Trade Entry (OTE 0.705): `279.66`
  * Structural Invalidation Anchor (0.786): `281.33`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `281.87` | `281.93` | `281.05` | `281.09` | `1,396` | 392,870.66 USD | -158,202.83 USD | `-40.27%` | -1,667,961.56 USD | `-1.23` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `281.09` | `281.61` | `280.95` | `281.20` | `729` | 205,030.12 USD | -71,867.69 USD | `-35.05%` | -1,739,829.25 USD | `-0.49` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `281.18` | `281.18` | `280.71` | `280.94` | `193` | 54,281.43 USD | -21,142.71 USD | `-38.95%` | -1,760,971.96 USD | `-0.07` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `281.78` | `283.24` | `281.23` | `283.12` | `4,417` | 1,246,277.92 USD | 430,890.56 USD | `+34.57%` | -1,455,201.99 USD | `+2.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `283.12` | `283.64` | `281.85` | `281.86` | `3,177` | 898,717.53 USD | -54,556.74 USD | `-6.07%` | -1,509,758.73 USD | `-0.26` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `281.87` | `281.93` | `280.71` | `280.85` | `2,278` | 640,829.94 USD | -262,565.50 USD | `-40.97%` | -1,772,324.24 USD | `-1.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `283.83` | `285.70` | `282.63` | `283.67` | `9,521` | 2,702,124.82 USD | -222,954.35 USD | `-8.25%` | -1,541,902.84 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `283.68` | `284.86` | `280.79` | `281.78` | `11,868` | 3,357,238.13 USD | -360,522.64 USD | `-10.74%` | -1,902,425.48 USD | `-0.33` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `280.71` | `280.93` | `9,912` | 2,797,281.89 USD | 125,016.37 USD | `+4.47%` | -1,777,409.11 USD | `+0.26` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `280.71` | `280.93` | `9,912` | 2,797,281.89 USD | 125,016.37 USD | `+4.47%` | -1,614,894.27 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `280.71` | `280.93` | `9,912` | 2,797,281.89 USD | 125,016.37 USD | `+4.47%` | -1,614,894.27 USD | `+0.33` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1981` | `0x12d2...f97f` | `LONG` | 1,017,985.75 USD | `3,627,243,000,000.00` | `303.26` | `280.63` | `0.000000` | -82,013.59 USD | `-8.06%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+3.22%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--5.14%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.20%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.12%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.20%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.12%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+3.20%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--5.12%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `60.50` | 2,480.00 USD | 215,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 534.54 USD | 212,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 1,200.00 USD | 212,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 211,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 210,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 203,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 395.01 USD | 199,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 170.24 USD | 199,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 199,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 199,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 198,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 198,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `129.50` | 1,940.00 USD | 198,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 3,390.00 USD | 196,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 192,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 191,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 190,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 188,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 187,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 8,280.00 USD | 187,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 179,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 178,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 178,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 178,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 177,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 177,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 176,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 176,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 3,270.00 USD | 175,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 172,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 170,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 210.65 USD | 170,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 170,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 169,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 2,560.00 USD | 169,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 166,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 41,790.00 USD | 166,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `208.50` | 625.50 USD | 124,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 124,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 124,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 2,610.00 USD | 120,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `217.50` | 6,850.00 USD | 117,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 31,290.00 USD | 110,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 5,830.00 USD | 79,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 73,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 72,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 72,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 114.75 USD | 71,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 1,190.00 USD | 71,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 983.41 USD | 70,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `233.50` | 634.89 USD | 69,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `234.80` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 182.78 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 9,890,000.00 USD | 9,890,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 9,880,000.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 9,870,000.00 USD | 9,870,000.00 USD | 5,950.00 USD | 0.00 USD | 7,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 9,850,000.00 USD | 9,850,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 68,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 9,820,000.00 USD | 9,820,000.00 USD | 5,120.00 USD | 146.67 USD | 9.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 9,810,000.00 USD | 9,810,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `238.50` | 3,790.00 USD | 44,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `238.80` | 9,790,000.00 USD | 9,790,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 9,760,000.00 USD | 9,760,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 41,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 9,750,000.00 USD | 9,750,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 9,740,000.00 USD | 9,740,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 7,400.00 USD | 40,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 9,730,000.00 USD | 9,730,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 9,720,000.00 USD | 9,720,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 32,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 9,640,000.00 USD | 9,640,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 31,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 9,610,000.00 USD | 9,610,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.30` | 9,560,000.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 3.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 29,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 9,560,000.00 USD | 9,560,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 9,540,000.00 USD | 9,540,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 9,510,000.00 USD | 9,510,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 9,500,000.00 USD | 9,500,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 9,450,000.00 USD | 9,450,000.00 USD | 4,590.00 USD | 472.85 USD | 1,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 9,440,000.00 USD | 9,440,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,400,000.00 USD | 9,400,000.00 USD | 3,560.00 USD | 4,920.00 USD | 5.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,390,000.00 USD | 9,390,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,380,000.00 USD | 9,380,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,270,000.00 USD | 9,270,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,200,000.00 USD | 9,200,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,080,000.00 USD | 9,080,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 23,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.80` | 8,990,000.00 USD | 8,990,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 8,850,000.00 USD | 8,850,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,750,000.00 USD | 4,750,000.00 USD | 26,340.00 USD | 65,240.00 USD | 26,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.80` | 8,710,000.00 USD | 8,710,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,640,000.00 USD | 4,640,000.00 USD | 22,120.00 USD | 9,520.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 8,520,000.00 USD | 8,520,000.00 USD | 69,530.00 USD | 32,910.00 USD | 17,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,590,000.00 USD | 4,590,000.00 USD | 15,520.00 USD | 5,050.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 21,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,400,000.00 USD | 8,400,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,570,000.00 USD | 4,570,000.00 USD | 4,970.00 USD | 6,970.00 USD | 2,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,550,000.00 USD | 4,550,000.00 USD | 12,480.00 USD | 8,710.00 USD | 14,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,320,000.00 USD | 8,320,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,520,000.00 USD | 4,520,000.00 USD | 21,830.00 USD | 15,190.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,210,000.00 USD | 8,210,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,470,000.00 USD | 4,470,000.00 USD | 1,590.00 USD | 7,170.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,130,000.00 USD | 8,130,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,450,000.00 USD | 4,450,000.00 USD | 8,310.00 USD | 10,840.00 USD | 46.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,010,000.00 USD | 8,010,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,430,000.00 USD | 4,430,000.00 USD | 9,050.00 USD | 10,890.00 USD | 92.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,410,000.00 USD | 4,410,000.00 USD | 9,910.00 USD | 15,540.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 7,840,000.00 USD | 7,840,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,360,000.00 USD | 4,360,000.00 USD | 14,640.00 USD | 23,250.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 7,760,000.00 USD | 7,760,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,310,000.00 USD | 4,310,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 7,700,000.00 USD | 7,700,000.00 USD | 60,900.00 USD | 10,260.00 USD | 40,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,260,000.00 USD | 4,260,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.80` | 7,580,000.00 USD | 7,580,000.00 USD | 32,750.00 USD | 13,750.00 USD | 64,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,220,000.00 USD | 4,220,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,200,000.00 USD | 4,200,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 7,470,000.00 USD | 7,470,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 101.20 USD | 17,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,180,000.00 USD | 4,180,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,440,000.00 USD | 7,440,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,160,000.00 USD | 4,160,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,380,000.00 USD | 7,380,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,100,000.00 USD | 4,100,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 1,840.00 USD | 16,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,150,000.00 USD | 7,150,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,040,000.00 USD | 4,040,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 3,960,000.00 USD | 3,960,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 6,980,000.00 USD | 6,980,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 3,920,000.00 USD | 3,920,000.00 USD | 18,950.00 USD | 34,250.00 USD | 39,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 6,920,000.00 USD | 6,920,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 3,830,000.00 USD | 3,830,000.00 USD | 39,390.00 USD | 8,470.00 USD | 6,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 6,760,000.00 USD | 6,760,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,780,000.00 USD | 3,780,000.00 USD | 19,100.00 USD | 1,010.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 15,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.80` | 6,540,000.00 USD | 6,540,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,730,000.00 USD | 3,730,000.00 USD | 9,020.00 USD | 50,800.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,660,000.00 USD | 3,660,000.00 USD | 8,130.00 USD | 29,340.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,410,000.00 USD | 6,410,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,580,000.00 USD | 3,580,000.00 USD | 15,200.00 USD | 60,690.00 USD | 51,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,250,000.00 USD | 6,250,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,460,000.00 USD | 3,460,000.00 USD | 13,620.00 USD | 27,520.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,050,000.00 USD | 6,050,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,390,000.00 USD | 3,390,000.00 USD | 21,110.00 USD | 4,750.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 5,880,000.00 USD | 5,880,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,360,000.00 USD | 3,360,000.00 USD | 629.76 USD | 12,630.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,330,000.00 USD | 3,330,000.00 USD | 9,930.00 USD | 4,350.00 USD | 61,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 5,720,000.00 USD | 5,720,000.00 USD | 33,590.00 USD | 13,710.00 USD | 162.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,250,000.00 USD | 3,250,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 5,670,000.00 USD | 5,670,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,140,000.00 USD | 3,140,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,160,000.00 USD | 5,160,000.00 USD | 48,230.00 USD | 1,170.00 USD | 79.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,060,000.00 USD | 3,060,000.00 USD | 905.76 USD | 19,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,110,000.00 USD | 5,110,000.00 USD | 33,470.00 USD | 21,870.00 USD | 191.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,040,000.00 USD | 3,040,000.00 USD | 33,200.00 USD | 1,890.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 2,950,000.00 USD | 2,950,000.00 USD | 64,960.00 USD | 1,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,060,000.00 USD | 5,060,000.00 USD | 256,440.00 USD | 980.96 USD | 33,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.70` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 629.76 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 4,770,000.00 USD | 4,770,000.00 USD | 69,380.00 USD | 0.00 USD | 91.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 2,880,000.00 USD | 2,880,000.00 USD | 16,140.00 USD | 13,320.00 USD | 2.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 4,700,000.00 USD | 4,700,000.00 USD | 216,090.00 USD | 645.20 USD | 133.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 2,850,000.00 USD | 2,850,000.00 USD | 14,240.00 USD | 8,470.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 4,480,000.00 USD | 4,480,000.00 USD | 136,640.00 USD | 63,260.00 USD | 46.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 2,820,000.00 USD | 2,820,000.00 USD | 18,330.00 USD | 22,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 2,780,000.00 USD | 2,780,000.00 USD | 33,460.00 USD | 68,530.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,280,000.00 USD | 4,280,000.00 USD | 131,280.00 USD | 52,200.00 USD | 77.77 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.70` | 2,670,000.00 USD | 2,670,000.00 USD | 5,020.00 USD | 36,260.00 USD | 14,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,100,000.00 USD | 4,100,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,610,000.00 USD | 2,610,000.00 USD | 4,570.00 USD | 24,670.00 USD | 60,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 3,810,000.00 USD | 3,810,000.00 USD | 169,940.00 USD | 150,080.00 USD | 62,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 10,760.00 USD | 80.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,420,000.00 USD | 3,420,000.00 USD | 23,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,510,000.00 USD | 2,510,000.00 USD | 8,400.00 USD | 776.90 USD | 305.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,500,000.00 USD | 2,500,000.00 USD | 7,610.00 USD | 1,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 3,490.00 USD | 44.11 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,490,000.00 USD | 2,490,000.00 USD | 638.90 USD | 17,350.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,460,000.00 USD | 2,460,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,430,000.00 USD | 2,430,000.00 USD | 42,710.00 USD | 118.00 USD | 4.60 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,390,000.00 USD | 3,390,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,390,000.00 USD | 2,390,000.00 USD | 505.00 USD | 14,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,370,000.00 USD | 2,370,000.00 USD | 12,710.00 USD | 1,780.00 USD | 11,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,340,000.00 USD | 2,340,000.00 USD | 8,650.00 USD | 34,920.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,340,000.00 USD | 3,340,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,300,000.00 USD | 2,300,000.00 USD | 21,980.00 USD | 21,380.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,230,000.00 USD | 2,230,000.00 USD | 6,060.00 USD | 38,280.00 USD | 41,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,200,000.00 USD | 3,200,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,150,000.00 USD | 2,150,000.00 USD | 59,390.00 USD | 5,420.00 USD | 71,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 2,010,000.00 USD | 2,010,000.00 USD | 18,100.00 USD | 121,350.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 1,860,000.00 USD | 1,860,000.00 USD | 40,330.00 USD | 59,570.00 USD | 69,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 2,710,000.00 USD | 2,710,000.00 USD | 181,410.00 USD | 0.00 USD | 29,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,690,000.00 USD | 1,690,000.00 USD | 129,290.00 USD | 21,230.00 USD | 12,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,500,000.00 USD | 2,500,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,530,000.00 USD | 1,530,000.00 USD | 193,310.00 USD | 0.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 1,940,000.00 USD | 1,940,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,280,000.00 USD | 1,280,000.00 USD | 79,290.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 6,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,410,000.00 USD | 1,410,000.00 USD | 59,580.00 USD | 19,960.00 USD | 21.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,170,000.00 USD | 1,170,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,330,000.00 USD | 1,330,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 1,050,000.00 USD | 1,050,000.00 USD | 161,250.00 USD | 3,340.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,220,000.00 USD | 1,220,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 880,320.00 USD | 880,320.00 USD | 11,920.00 USD | 5,230.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 896,000.00 USD | 896,000.00 USD | 16,100.00 USD | 0.00 USD | 47.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 854,360.00 USD | 854,360.00 USD | 37,290.00 USD | 25,410.00 USD | 23,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 768,190.00 USD | 768,190.00 USD | 17,610.00 USD | 18,260.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 879,850.00 USD | 879,850.00 USD | 152,190.00 USD | 77,800.00 USD | 141,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 721,720.00 USD | 721,720.00 USD | 13,750.00 USD | 10,950.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 508,860.00 USD | 508,860.00 USD | 0.00 USD | 157,740.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 676,710.00 USD | 676,710.00 USD | 12,120.00 USD | 97,470.00 USD | 83,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 291,170.00 USD | 291,170.00 USD | 24,750.00 USD | 37,090.00 USD | 155,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 483,440.00 USD | 483,440.00 USD | 78,720.00 USD | 56,870.00 USD | 69,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 73,980.00 USD | 73,980.00 USD | 51,310.00 USD | 20,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 278,180.00 USD | 278,180.00 USD | 22,390.00 USD | 87,720.00 USD | 28,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 139,340.00 USD | 139,340.00 USD | 11,160.00 USD | 21,610.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 2,670.00 USD | 2,670.00 USD | 2,660.00 USD | 0.00 USD | 9.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 65,490.00 USD | 65,490.00 USD | 19,850.00 USD | 21,310.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.80` | 58,080.00 USD | 58,080.00 USD | 0.00 USD | 0.00 USD | 58,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.10` | 86,600.00 USD | 86,600.00 USD | 0.00 USD | 26,770.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.30` | 75,500.00 USD | 75,500.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.50` | 212,870.00 USD | 212,870.00 USD | 4,150.00 USD | 53,570.00 USD | 68,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.80` | 91,040.00 USD | 91,040.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.90` | 230,320.00 USD | 230,320.00 USD | 0.00 USD | 17,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.30` | 188,450.00 USD | 188,450.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.80` | 310,840.00 USD | 310,840.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.10` | 242,730.00 USD | 242,730.00 USD | 8,260.00 USD | 0.00 USD | 4,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.30` | 335,060.00 USD | 335,060.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.80` | 335,120.00 USD | 335,120.00 USD | 0.00 USD | 0.00 USD | 55.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.30` | 244,010.00 USD | 244,010.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.30` | 338,680.00 USD | 338,680.00 USD | 3,450.00 USD | 0.00 USD | 110.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.70` | 244,030.00 USD | 244,030.00 USD | 0.00 USD | 0.00 USD | 20.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 340,670.00 USD | 340,670.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.10` | 244,050.00 USD | 244,050.00 USD | 0.00 USD | 0.00 USD | 15.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 342,240.00 USD | 342,240.00 USD | 1,560.00 USD | 0.00 USD | 11.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 397,710.00 USD | 397,710.00 USD | 0.00 USD | 55,390.00 USD | 74.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 244,080.00 USD | 244,080.00 USD | 0.00 USD | 0.00 USD | 33.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 285,770.00 USD | 285,770.00 USD | 0.00 USD | 0.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 693,780.00 USD | 693,780.00 USD | 68,860.00 USD | 227,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 287,480.00 USD | 287,480.00 USD | 1,710.00 USD | 0.00 USD | 4.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 892,370.00 USD | 892,370.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 338,230.00 USD | 338,230.00 USD | 26,810.00 USD | 719.80 USD | 23,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 936,600.00 USD | 936,600.00 USD | 1,200.00 USD | 43,020.00 USD | 12.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 373,570.00 USD | 373,570.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,180,000.00 USD | 1,180,000.00 USD | 30,110.00 USD | 217,580.00 USD | 1.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 528,420.00 USD | 528,420.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 703,940.00 USD | 703,940.00 USD | 97,970.00 USD | 43,890.00 USD | 33,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,380,000.00 USD | 1,380,000.00 USD | 82,910.00 USD | 116,440.00 USD | 70.92 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 799,160.00 USD | 799,160.00 USD | 22,860.00 USD | 22,500.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,780,000.00 USD | 1,780,000.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 881,090.00 USD | 881,090.00 USD | 21,420.00 USD | 26,660.00 USD | 33,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 988,620.00 USD | 988,620.00 USD | 52,260.00 USD | 26,060.00 USD | 29,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 2,080,000.00 USD | 2,080,000.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 1,060,000.00 USD | 1,060,000.00 USD | 44,740.00 USD | 24,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 1,170,000.00 USD | 1,170,000.00 USD | 17,220.00 USD | 47,120.00 USD | 51,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 1,390,000.00 USD | 1,390,000.00 USD | 52,150.00 USD | 67,790.00 USD | 92,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,480,000.00 USD | 2,480,000.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,600,000.00 USD | 1,600,000.00 USD | 59,800.00 USD | 51,750.00 USD | 100,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,540,000.00 USD | 2,540,000.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,770,000.00 USD | 1,770,000.00 USD | 13,650.00 USD | 116,320.00 USD | 46,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,600,000.00 USD | 2,600,000.00 USD | 898.13 USD | 1,760.00 USD | 58,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,890,000.00 USD | 1,890,000.00 USD | 39,460.00 USD | 39,180.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 1,940,000.00 USD | 1,940,000.00 USD | 14,090.00 USD | 11,300.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,640,000.00 USD | 2,640,000.00 USD | 24,680.00 USD | 10,160.00 USD | 9.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 2,010,000.00 USD | 2,010,000.00 USD | 9,470.00 USD | 38,560.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 2,840,000.00 USD | 2,840,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 2,060,000.00 USD | 2,060,000.00 USD | 854.05 USD | 37,580.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 2,910,000.00 USD | 2,910,000.00 USD | 1,240.00 USD | 73,530.00 USD | 88.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 2,100,000.00 USD | 2,100,000.00 USD | 29,580.00 USD | 3,650.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 3,010,000.00 USD | 3,010,000.00 USD | 887.27 USD | 100,630.00 USD | 141.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 2,200,000.00 USD | 2,200,000.00 USD | 62,510.00 USD | 30,780.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 2,260,000.00 USD | 2,260,000.00 USD | 22,320.00 USD | 16,660.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,180,000.00 USD | 3,180,000.00 USD | 33,580.00 USD | 132,080.00 USD | 61.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,450,000.00 USD | 2,450,000.00 USD | 76,610.00 USD | 47,640.00 USD | 64,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,240,000.00 USD | 3,240,000.00 USD | 38,790.00 USD | 1,860.00 USD | 20,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,550,000.00 USD | 2,550,000.00 USD | 21,360.00 USD | 23,760.00 USD | 49,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,640,000.00 USD | 3,640,000.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,800,000.00 USD | 2,800,000.00 USD | 96,500.00 USD | 76,930.00 USD | 85,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,910,000.00 USD | 3,910,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 2,900,000.00 USD | 2,900,000.00 USD | 33,360.00 USD | 16,330.00 USD | 48,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 3,080,000.00 USD | 3,080,000.00 USD | 15,750.00 USD | 60,930.00 USD | 96,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,380,000.00 USD | 4,380,000.00 USD | 46,330.00 USD | 82,780.00 USD | 345,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 3,310,000.00 USD | 3,310,000.00 USD | 98,960.00 USD | 6,830.00 USD | 128,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 4,830,000.00 USD | 4,830,000.00 USD | 165,320.00 USD | 82,100.00 USD | 197,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 3,530,000.00 USD | 3,530,000.00 USD | 52,840.00 USD | 126,740.00 USD | 35,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 5,160,000.00 USD | 5,160,000.00 USD | 43,710.00 USD | 167,940.00 USD | 120,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,620,000.00 USD | 3,620,000.00 USD | 33,300.00 USD | 22,420.00 USD | 41,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,500,000.00 USD | 5,500,000.00 USD | 133,820.00 USD | 3,570.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,760,000.00 USD | 3,760,000.00 USD | 24,280.00 USD | 21,780.00 USD | 90,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 3,850,000.00 USD | 3,850,000.00 USD | 61,160.00 USD | 1,000.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,630,000.00 USD | 5,630,000.00 USD | 78,980.00 USD | 54,960.00 USD | 56.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 3,890,000.00 USD | 3,890,000.00 USD | 15,790.00 USD | 11,180.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 5,870,000.00 USD | 5,870,000.00 USD | 47,530.00 USD | 99,320.00 USD | 89,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 3,990,000.00 USD | 3,990,000.00 USD | 51,840.00 USD | 8,960.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 6,010,000.00 USD | 6,010,000.00 USD | 32,650.00 USD | 44,630.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 4,060,000.00 USD | 4,060,000.00 USD | 5,790.00 USD | 1,480.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,100,000.00 USD | 6,100,000.00 USD | 69,820.00 USD | 12,530.00 USD | 17.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 4,190,000.00 USD | 4,190,000.00 USD | 28,150.00 USD | 5,580.00 USD | 94,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 4,240,000.00 USD | 4,240,000.00 USD | 33,970.00 USD | 10,810.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,210,000.00 USD | 6,210,000.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 4,290,000.00 USD | 4,290,000.00 USD | 8,250.00 USD | 10,850.00 USD | 27,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,260,000.00 USD | 6,260,000.00 USD | 22,950.00 USD | 9,100.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 4,410,000.00 USD | 4,410,000.00 USD | 19,900.00 USD | 36,560.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,300,000.00 USD | 6,300,000.00 USD | 35,320.00 USD | 2,910.00 USD | 52.41 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 4,450,000.00 USD | 4,450,000.00 USD | 23,270.00 USD | 1,560.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,450,000.00 USD | 6,450,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 4,480,000.00 USD | 4,480,000.00 USD | 269.05 USD | 1,020.00 USD | 29,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 4,520,000.00 USD | 4,520,000.00 USD | 597.00 USD | 15,110.00 USD | 20,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 6,730,000.00 USD | 6,730,000.00 USD | 73,320.00 USD | 58,690.00 USD | 150,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 4,560,000.00 USD | 4,560,000.00 USD | 19,840.00 USD | 8,470.00 USD | 15,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 6,980,000.00 USD | 6,980,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,630,000.00 USD | 4,630,000.00 USD | 25,190.00 USD | 30,660.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 7,160,000.00 USD | 7,160,000.00 USD | 1,560.00 USD | 181,550.00 USD | 17.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,700,000.00 USD | 4,700,000.00 USD | 13,820.00 USD | 13,290.00 USD | 38,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `302.50` | 3,640.00 USD | 10,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,390,000.00 USD | 7,390,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 4,710,000.00 USD | 4,710,000.00 USD | 1,370.00 USD | 2,260.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 4,750,000.00 USD | 4,750,000.00 USD | 21,200.00 USD | 2,760.00 USD | 9,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 1,950.00 USD | 220.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 391.16 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,440,000.00 USD | 7,440,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 4,810,000.00 USD | 4,810,000.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,470,000.00 USD | 7,470,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 4,870,000.00 USD | 4,870,000.00 USD | 9,670.00 USD | 2,100.00 USD | 44,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,520,000.00 USD | 7,520,000.00 USD | 36,140.00 USD | 11,790.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 4,890,000.00 USD | 4,890,000.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 4,890,000.00 USD | 4,890,000.00 USD | 83.23 USD | 172.52 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 7,950,000.00 USD | 7,950,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 4,910,000.00 USD | 4,910,000.00 USD | 6,340.00 USD | 3,500.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,100,000.00 USD | 8,100,000.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 4,920,000.00 USD | 4,920,000.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,260,000.00 USD | 8,260,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 4,930,000.00 USD | 4,930,000.00 USD | 4,230.00 USD | 6.13 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,500,000.00 USD | 8,500,000.00 USD | 94,690.00 USD | 74,180.00 USD | 69,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 5,000,000.00 USD | 5,000,000.00 USD | 19,850.00 USD | 38,870.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 5,070,000.00 USD | 5,070,000.00 USD | 5,500.00 USD | 41,920.00 USD | 22,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 8,790,000.00 USD | 8,790,000.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 5,120,000.00 USD | 5,120,000.00 USD | 21,890.00 USD | 22,070.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,080,000.00 USD | 9,080,000.00 USD | 115,070.00 USD | 113,210.00 USD | 60,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 5,160,000.00 USD | 5,160,000.00 USD | 20,530.00 USD | 8,780.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,430,000.00 USD | 9,430,000.00 USD | 169,010.00 USD | 59,680.00 USD | 114,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 5,180,000.00 USD | 5,180,000.00 USD | 7,610.00 USD | 3,610.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,590,000.00 USD | 9,590,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 5,190,000.00 USD | 5,190,000.00 USD | 7,450.00 USD | 5,920.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 5,200,000.00 USD | 5,200,000.00 USD | 5,190.00 USD | 1,580.00 USD | 2,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 9,700,000.00 USD | 9,700,000.00 USD | 34,260.00 USD | 36,030.00 USD | 36,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 5,220,000.00 USD | 5,220,000.00 USD | 10,040.00 USD | 7,670.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,050,000.00 USD | 10,050,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 5,250,000.00 USD | 5,250,000.00 USD | 14,750.00 USD | 3,980.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,300,000.00 USD | 10,300,000.00 USD | 62,230.00 USD | 108,410.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 5,260,000.00 USD | 5,260,000.00 USD | 112.30 USD | 5,020.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,420,000.00 USD | 10,420,000.00 USD | 60,910.00 USD | 51,380.00 USD | 12,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 5,270,000.00 USD | 5,270,000.00 USD | 5,080.00 USD | 73.70 USD | 20.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 5,270,000.00 USD | 5,270,000.00 USD | 257.90 USD | 2,350.00 USD | 107.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,670,000.00 USD | 10,670,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 5,290,000.00 USD | 5,290,000.00 USD | 7,980.00 USD | 9,070.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 10,720,000.00 USD | 10,720,000.00 USD | 19,570.00 USD | 11,240.00 USD | 25,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 5,320,000.00 USD | 5,320,000.00 USD | 299.35 USD | 10,320.00 USD | 15,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 10,810,000.00 USD | 10,810,000.00 USD | 43,780.00 USD | 11,410.00 USD | 27,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 5,350,000.00 USD | 5,350,000.00 USD | 14,640.00 USD | 8,480.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,870,000.00 USD | 10,870,000.00 USD | 29,070.00 USD | 14,880.00 USD | 19,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 5,370,000.00 USD | 5,370,000.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 5,390,000.00 USD | 5,390,000.00 USD | 3,580.00 USD | 18,270.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 10,950,000.00 USD | 10,950,000.00 USD | 33,520.00 USD | 10,510.00 USD | 38,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 5,410,000.00 USD | 5,410,000.00 USD | 4,550.00 USD | 4,260.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 11,030,000.00 USD | 11,030,000.00 USD | 33,220.00 USD | 1,570.00 USD | 44,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 11,120,000.00 USD | 11,120,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,160,000.00 USD | 11,160,000.00 USD | 24,660.00 USD | 0.00 USD | 10,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 11,160,000.00 USD | 11,160,000.00 USD | 500.10 USD | 547.95 USD | 49.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,240,000.00 USD | 11,240,000.00 USD | 9,200.00 USD | 43,070.00 USD | 30,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,340,000.00 USD | 11,340,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,400,000.00 USD | 11,400,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,410,000.00 USD | 11,410,000.00 USD | 15,590.00 USD | 748.91 USD | 157.61 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,440,000.00 USD | 11,440,000.00 USD | 21,640.00 USD | 8,380.00 USD | 164.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 11,510,000.00 USD | 11,510,000.00 USD | 627.00 USD | 31,660.00 USD | 32,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 11,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `324.50` | 2,220.00 USD | 14,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 39,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `338.50` | 1,350.00 USD | 41,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 42,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 42,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `371.50` | 40,870.00 USD | 83,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `406.50` | 10,640.00 USD | 94,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 140,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 140,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 141,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `60.50` | 215,250.00 USD | 0.00 USD | 2,480.00 USD | `-78.52%` | `41,012,000,000.00` |
| `Live` | `Long` | `74.50` | 212,770.00 USD | 0.00 USD | 534.54 USD | `-73.55%` | `7,175,000,000.00` |
| `Live` | `Long` | `91.50` | 212,230.00 USD | 0.00 USD | 1,200.00 USD | `-67.52%` | `13,105,000,000.00` |
| `Live` | `Long` | `95.50` | 211,030.00 USD | 0.00 USD | 920.05 USD | `-66.10%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 210,110.00 USD | 0.00 USD | 6,240.00 USD | `-63.97%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 203,880.00 USD | 0.00 USD | 4,080.00 USD | `-63.61%` | `39,797,000,000.00` |
| `Live` | `Long` | `104.50` | 199,800.00 USD | 0.00 USD | 395.01 USD | `-62.90%` | `3,780,000,000.00` |
| `Live` | `Long` | `108.50` | 199,400.00 USD | 0.00 USD | 170.24 USD | `-61.48%` | `1,569,000,000.00` |
| `Live` | `Long` | `109.50` | 199,230.00 USD | 0.00 USD | 212.76 USD | `-61.13%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 199,020.00 USD | 0.00 USD | 212.35 USD | `-57.93%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 198,810.00 USD | 0.00 USD | 124.46 USD | `-56.51%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 198,680.00 USD | 0.00 USD | 658.18 USD | `-55.09%` | `5,203,000,000.00` |
| `Live` | `Long` | `129.50` | 198,020.00 USD | 0.00 USD | 1,940.00 USD | `-54.03%` | `15,000,000,000.00` |
| `Live` | `Long` | `130.50` | 196,080.00 USD | 0.00 USD | 3,390.00 USD | `-53.67%` | `26,000,000,000.00` |
| `Live` | `Long` | `147.50` | 192,690.00 USD | 0.00 USD | 895.47 USD | `-47.64%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 191,790.00 USD | 0.00 USD | 1,270.00 USD | `-47.28%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 190,530.00 USD | 0.00 USD | 2,370.00 USD | `-46.93%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 188,160.00 USD | 0.00 USD | 303.78 USD | `-45.86%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 187,860.00 USD | 0.00 USD | 325.00 USD | `-42.31%` | `2,000,000,000.00` |
| `Live` | `Long` | `165.50` | 187,530.00 USD | 0.00 USD | 8,280.00 USD | `-41.25%` | `50,000,000,000.00` |
| `Live` | `Long` | `167.50` | 179,260.00 USD | 0.00 USD | 285.75 USD | `-40.54%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 178,970.00 USD | 0.00 USD | 426.25 USD | `-39.47%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 178,540.00 USD | 0.00 USD | 169.96 USD | `-38.05%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 178,370.00 USD | 0.00 USD | 516.67 USD | `-37.70%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 177,860.00 USD | 0.00 USD | 373.83 USD | `-37.34%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 177,480.00 USD | 0.00 USD | 808.66 USD | `-34.50%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 176,680.00 USD | 0.00 USD | 418.28 USD | `-33.08%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 176,260.00 USD | 0.00 USD | 694.75 USD | `-32.37%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 175,560.00 USD | 0.00 USD | 3,270.00 USD | `-32.02%` | `17,082,000,000.00` |
| `Live` | `Long` | `192.50` | 172,290.00 USD | 0.00 USD | 1,490.00 USD | `-31.66%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 170,810.00 USD | 0.00 USD | 370.47 USD | `-30.60%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 170,440.00 USD | 0.00 USD | 210.65 USD | `-30.24%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 170,220.00 USD | 0.00 USD | 548.03 USD | `-29.17%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 169,680.00 USD | 0.00 USD | 293.13 USD | `-28.82%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 169,380.00 USD | 0.00 USD | 2,560.00 USD | `-28.11%` | `12,648,000,000.00` |
| `Live` | `Long` | `205.50` | 166,820.00 USD | 0.00 USD | 191.53 USD | `-27.04%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 166,630.00 USD | 0.00 USD | 41,790.00 USD | `-26.69%` | `202,387,000,000.00` |
| `Live` | `Long` | `208.50` | 124,840.00 USD | 0.00 USD | 625.50 USD | `-25.98%` | `3,000,000,000.00` |
| `Live` | `Long` | `210.50` | 124,210.00 USD | 0.00 USD | 108.83 USD | `-25.27%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 124,100.00 USD | 0.00 USD | 3,800.00 USD | `-24.20%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 120,300.00 USD | 0.00 USD | 2,610.00 USD | `-23.49%` | `12,132,000,000.00` |
| `Live` | `Long` | `217.50` | 117,690.00 USD | 0.00 USD | 6,850.00 USD | `-22.78%` | `31,500,000,000.00` |
| `Live` | `Long` | `223.50` | 110,830.00 USD | 0.00 USD | 31,290.00 USD | `-20.65%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 79,540.00 USD | 0.00 USD | 5,830.00 USD | `-20.30%` | `25,951,000,000.00` |
| `Live` | `Long` | `226.50` | 73,720.00 USD | 0.00 USD | 1,240.00 USD | `-19.59%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 72,480.00 USD | 0.00 USD | 174.49 USD | `-19.23%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 72,310.00 USD | 0.00 USD | 642.77 USD | `-18.88%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 71,670.00 USD | 0.00 USD | 114.75 USD | `-18.52%` | `500,000,000.00` |
| `Live` | `Long` | `230.50` | 71,550.00 USD | 0.00 USD | 1,190.00 USD | `-18.17%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 70,360.00 USD | 0.00 USD | 983.41 USD | `-17.81%` | `4,248,000,000.00` |
| `Live` | `Long` | `233.50` | 69,380.00 USD | 0.00 USD | 634.89 USD | `-17.10%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 68,740.00 USD | 0.00 USD | 23,750.00 USD | `-15.68%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 44,990.00 USD | 0.00 USD | 3,790.00 USD | `-15.33%` | `15,877,000,000.00` |
| `Live` | `Long` | `239.50` | 41,200.00 USD | 0.00 USD | 1,030.00 USD | `-14.97%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 40,180.00 USD | 0.00 USD | 7,400.00 USD | `-14.26%` | `30,633,000,000.00` |
| `Live` | `Long` | `242.50` | 32,780.00 USD | 0.00 USD | 1,520.00 USD | `-13.91%` | `6,274,000,000.00` |
| `Live` | `Long` | `243.50` | 31,260.00 USD | 0.00 USD | 1,850.00 USD | `-13.55%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 29,410.00 USD | 0.00 USD | 4,220.00 USD | `-13.20%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 25,190.00 USD | 0.00 USD | 1,030.00 USD | `-12.84%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,160.00 USD | 0.00 USD | 106.67 USD | `-12.13%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,050.00 USD | 0.00 USD | 595.16 USD | `-11.78%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 23,460.00 USD | 0.00 USD | 1,330.00 USD | `-11.07%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,130.00 USD | 0.00 USD | 268.35 USD | `-10.71%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 21,860.00 USD | 0.00 USD | 1,030.00 USD | `-10.36%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 20,830.00 USD | 0.00 USD | 548.45 USD | `-9.65%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 20,280.00 USD | 0.00 USD | 3,210.00 USD | `-8.94%` | `12,514,000,000.00` |
| `Live` | `Long` | `257.50` | 17,070.00 USD | 0.00 USD | 101.20 USD | `-8.58%` | `393,000,000.00` |
| `Live` | `Long` | `258.50` | 16,970.00 USD | 0.00 USD | 1,840.00 USD | `-8.23%` | `7,106,000,000.00` |
| `Live` | `Long` | `260.50` | 15,140.00 USD | 0.00 USD | 2,040.00 USD | `-7.52%` | `7,839,000,000.00` |
| `Live` | `Long` | `270.50` | 13,090.00 USD | 0.00 USD | 13,090.00 USD | `-3.97%` | `48,404,000,000.00` |
| `Live` | `Short` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | `+2.07%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 1,070.00 USD | 954.95 USD | 0.00 USD | `+3.49%` | `3,276,000,000.00` |
| `Live` | `Short` | `296.50` | 7,200.00 USD | 6,130.00 USD | 0.00 USD | `+5.26%` | `20,668,000,000.00` |
| `Live` | `Short` | `302.50` | 10,840.00 USD | 3,640.00 USD | 0.00 USD | `+7.39%` | `12,043,000,000.00` |
| `Live` | `Short` | `320.50` | 11,940.00 USD | 1,110.00 USD | 0.00 USD | `+13.78%` | `3,452,000,000.00` |
| `Live` | `Short` | `324.50` | 14,170.00 USD | 2,220.00 USD | 0.00 USD | `+15.20%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 39,700.00 USD | 25,530.00 USD | 0.00 USD | `+15.91%` | `78,189,000,000.00` |
| `Live` | `Short` | `338.50` | 41,050.00 USD | 1,350.00 USD | 0.00 USD | `+20.17%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 42,060.00 USD | 1,010.00 USD | 0.00 USD | `+27.27%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 42,510.00 USD | 445.52 USD | 0.00 USD | `+30.82%` | `1,209,000,000.00` |
| `Live` | `Short` | `371.50` | 83,370.00 USD | 40,870.00 USD | 0.00 USD | `+31.89%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 94,010.00 USD | 10,640.00 USD | 0.00 USD | `+44.31%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 140,260.00 USD | 46,250.00 USD | 0.00 USD | `+63.13%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 140,980.00 USD | 718.34 USD | 0.00 USD | `+76.97%` | `1,441,000,000.00` |
| `Live` | `Short` | `560.50` | 141,820.00 USD | 842.43 USD | 0.00 USD | `+98.98%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 461,680.00 USD | 0.00 USD | 210.94 USD | `-49.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 461,470.00 USD | 0.00 USD | 2,070.00 USD | `-48.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 459,400.00 USD | 0.00 USD | 489.38 USD | `-41.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 458,920.00 USD | 0.00 USD | 2,530.00 USD | `-36.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 456,390.00 USD | 0.00 USD | 490.59 USD | `-34.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 455,900.00 USD | 0.00 USD | 482.01 USD | `-30.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 455,410.00 USD | 0.00 USD | 189.07 USD | `-28.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 455,220.00 USD | 0.00 USD | 441.60 USD | `-25.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 454,780.00 USD | 0.00 USD | 299.96 USD | `-25.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 454,480.00 USD | 0.00 USD | 715.29 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 453,770.00 USD | 0.00 USD | 638.36 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 453,130.00 USD | 0.00 USD | 740.85 USD | `-20.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 452,390.00 USD | 0.00 USD | 478.48 USD | `-18.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 451,910.00 USD | 0.00 USD | 389.48 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 451,520.00 USD | 0.00 USD | 812.38 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 450,710.00 USD | 0.00 USD | 220.64 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 450,490.00 USD | 0.00 USD | 429.30 USD | `-15.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 450,060.00 USD | 0.00 USD | 296.50 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 449,760.00 USD | 0.00 USD | 216.45 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 449,550.00 USD | 0.00 USD | 387.76 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 449,160.00 USD | 0.00 USD | 18,080.00 USD | `-13.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 431,070.00 USD | 0.00 USD | 1,630.00 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 429,450.00 USD | 0.00 USD | 2,700.00 USD | `-12.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 426,750.00 USD | 0.00 USD | 2,940.00 USD | `-11.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 423,800.00 USD | 0.00 USD | 4,560.00 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 419,250.00 USD | 0.00 USD | 1,850.00 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 417,400.00 USD | 0.00 USD | 231.54 USD | `-10.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 417,170.00 USD | 0.00 USD | 109.26 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 417,060.00 USD | 0.00 USD | 1,780.00 USD | `-9.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 415,280.00 USD | 0.00 USD | 51,300.00 USD | `-8.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 363,980.00 USD | 0.00 USD | 250.81 USD | `-8.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 363,730.00 USD | 0.00 USD | 2,370.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 361,360.00 USD | 0.00 USD | 269,800.00 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 91,560.00 USD | 0.00 USD | 857.85 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 90,710.00 USD | 0.00 USD | 320.15 USD | `-6.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 90,390.00 USD | 0.00 USD | 199.17 USD | `-6.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 90,190.00 USD | 0.00 USD | 2,180.00 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 88,010.00 USD | 0.00 USD | 241.98 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 87,770.00 USD | 0.00 USD | 219.35 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 87,550.00 USD | 0.00 USD | 107.40 USD | `-4.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 87,440.00 USD | 0.00 USD | 29,530.00 USD | `-4.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 57,910.00 USD | 0.00 USD | 3,340.00 USD | `-3.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 54,570.00 USD | 0.00 USD | 620.38 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 53,950.00 USD | 0.00 USD | 13,500.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 40,450.00 USD | 0.00 USD | 1,010.00 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 39,440.00 USD | 0.00 USD | 667.86 USD | `-2.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 38,770.00 USD | 0.00 USD | 275.50 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 38,500.00 USD | 0.00 USD | 6,640.00 USD | `-1.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 31,850.00 USD | 0.00 USD | 326.34 USD | `-1.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 31,530.00 USD | 0.00 USD | 5,040.00 USD | `-1.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 26,490.00 USD | 0.00 USD | 21,990.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 4,500.00 USD | 0.00 USD | 1,390.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 3,100.00 USD | 0.00 USD | 3,100.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 2,940.00 USD | 2,940.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 10,980.00 USD | 8,040.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 12,990.00 USD | 2,010.00 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 14,040.00 USD | 1,050.00 USD | 0.00 USD | `+1.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 14,320.00 USD | 280.77 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 21,230.00 USD | 6,910.00 USD | 0.00 USD | `+2.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 21,490.00 USD | 261.96 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 22,020.00 USD | 530.36 USD | 0.00 USD | `+2.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 22,230.00 USD | 212.36 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 47,510.00 USD | 25,280.00 USD | 0.00 USD | `+3.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 47,680.00 USD | 167.89 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 48,670.00 USD | 992.62 USD | 0.00 USD | `+4.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 50,800.00 USD | 2,130.00 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 55,520.00 USD | 4,730.00 USD | 0.00 USD | `+4.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 55,640.00 USD | 110.37 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 56,020.00 USD | 388.95 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 56,180.00 USD | 153.94 USD | 0.00 USD | `+6.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 66,950.00 USD | 10,780.00 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 72,060.00 USD | 5,110.00 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 82,790.00 USD | 10,730.00 USD | 0.00 USD | `+8.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 85,440.00 USD | 2,650.00 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 85,720.00 USD | 282.89 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 100,220.00 USD | 14,500.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 100,850.00 USD | 634.04 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 101,880.00 USD | 1,030.00 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 107,530.00 USD | 5,650.00 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 108,070.00 USD | 534.59 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 108,390.00 USD | 321.50 USD | 0.00 USD | `+14.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 175,110.00 USD | 66,720.00 USD | 0.00 USD | `+15.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 176,200.00 USD | 1,090.00 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 188,190.00 USD | 12,000.00 USD | 0.00 USD | `+18.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 188,740.00 USD | 547.52 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 188,850.00 USD | 110.91 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 189,110.00 USD | 257.45 USD | 0.00 USD | `+23.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 189,280.00 USD | 174.25 USD | 0.00 USD | `+23.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 189,430.00 USD | 151.50 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 190,890.00 USD | 1,450.00 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 192,660.00 USD | 1,770.00 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 192,990.00 USD | 326.07 USD | 0.00 USD | `+28.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 193,810.00 USD | 826.60 USD | 0.00 USD | `+29.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 201,260.00 USD | 7,440.00 USD | 0.00 USD | `+29.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 201,940.00 USD | 682.84 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 203,040.00 USD | 1,100.00 USD | 0.00 USD | `+35.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 203,720.00 USD | 683.96 USD | 0.00 USD | `+40.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 203,920.00 USD | 199.75 USD | 0.00 USD | `+41.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 205,210.00 USD | 1,290.00 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 206,250.00 USD | 1,040.00 USD | 0.00 USD | `+43.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 206,630.00 USD | 376.71 USD | 0.00 USD | `+43.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 206,790.00 USD | 158.86 USD | 0.00 USD | `+45.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 212,690.00 USD | 5,900.00 USD | 0.00 USD | `+47.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 213,770.00 USD | 1,080.00 USD | 0.00 USD | `+50.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 215,470.00 USD | 1,700.00 USD | 0.00 USD | `+51.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 217,020.00 USD | 1,550.00 USD | 0.00 USD | `+52.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 218,410.00 USD | 1,380.00 USD | 0.00 USD | `+54.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 219,030.00 USD | 621.14 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 221,300.00 USD | 2,280.00 USD | 0.00 USD | `+56.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 221,530.00 USD | 222.75 USD | 0.00 USD | `+58.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 228,450.00 USD | 6,920.00 USD | 0.00 USD | `+59.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 234,360.00 USD | 5,920.00 USD | 0.00 USD | `+60.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 235,490.00 USD | 1,130.00 USD | 0.00 USD | `+63.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 243,130.00 USD | 7,630.00 USD | 0.00 USD | `+71.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 244,100.00 USD | 975.00 USD | 0.00 USD | `+73.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 245,080.00 USD | 981.00 USD | 0.00 USD | `+74.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 245,580.00 USD | 499.50 USD | 0.00 USD | `+77.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,130,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+77.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,130,000.00 USD | 1,000.00 USD | 0.00 USD | `+78.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,130,000.00 USD | 1,040.00 USD | 0.00 USD | `+84.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,130,000.00 USD | 340.67 USD | 0.00 USD | `+85.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,140,000.00 USD | 638.86 USD | 0.00 USD | `+97.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.80` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 0.00 USD | 182.78 USD | 3,080.00 USD |
| `7D` | `235.30` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 11,670.00 USD |
| `7D` | `236.30` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 5,950.00 USD | 0.00 USD | 7,720.00 USD |
| `7D` | `236.80` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD |
| `7D` | `237.30` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 5,120.00 USD | 146.67 USD | 9.84 USD |
| `7D` | `238.30` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD |
| `7D` | `238.80` | 9,790,000.00 USD | 0.00 USD | 9,790,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.80` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 8,740.00 USD | 0.00 USD | 4,920.00 USD |
| `7D` | `242.30` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD |
| `7D` | `243.30` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.30` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 3.00 USD |
| `7D` | `244.80` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.30` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,700.00 USD |
| `7D` | `246.80` | 9,450,000.00 USD | 0.00 USD | 9,450,000.00 USD | 4,590.00 USD | 472.85 USD | 1,740.00 USD |
| `7D` | `247.30` | 9,440,000.00 USD | 0.00 USD | 9,440,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.80` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 3,560.00 USD | 4,920.00 USD | 5.51 USD |
| `7D` | `248.30` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,400.00 USD |
| `7D` | `248.80` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,170.00 USD |
| `7D` | `249.30` | 9,270,000.00 USD | 0.00 USD | 9,270,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,540.00 USD |
| `7D` | `249.80` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,060.00 USD |
| `7D` | `250.30` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,620.00 USD |
| `7D` | `250.80` | 8,990,000.00 USD | 0.00 USD | 8,990,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,640.00 USD |
| `7D` | `251.30` | 8,850,000.00 USD | 0.00 USD | 8,850,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,110.00 USD |
| `1D` | `251.70` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 26,340.00 USD | 65,240.00 USD | 26,700.00 USD |
| `7D` | `251.80` | 8,710,000.00 USD | 0.00 USD | 8,710,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD |
| `1D` | `252.10` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 22,120.00 USD | 9,520.00 USD | 12,910.00 USD |
| `7D` | `252.30` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 69,530.00 USD | 32,910.00 USD | 17,400.00 USD |
| `1D` | `252.50` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 15,520.00 USD | 5,050.00 USD | 5,100.00 USD |
| `7D` | `252.80` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,330.00 USD |
| `1D` | `252.90` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 4,970.00 USD | 6,970.00 USD | 2,180.00 USD |
| `1D` | `253.30` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 12,480.00 USD | 8,710.00 USD | 14,790.00 USD |
| `7D` | `253.30` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,260.00 USD |
| `1D` | `253.70` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 21,830.00 USD | 15,190.00 USD | 11,010.00 USD |
| `7D` | `253.80` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,050.00 USD |
| `1D` | `254.10` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 1,590.00 USD | 7,170.00 USD | 5,880.00 USD |
| `7D` | `254.30` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,130.00 USD |
| `1D` | `254.50` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 8,310.00 USD | 10,840.00 USD | 46.90 USD |
| `7D` | `254.80` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,380.00 USD |
| `1D` | `254.90` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 9,050.00 USD | 10,890.00 USD | 92.51 USD |
| `1D` | `255.30` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 9,910.00 USD | 15,540.00 USD | 27,930.00 USD |
| `7D` | `255.30` | 7,840,000.00 USD | 0.00 USD | 7,840,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,500.00 USD |
| `1D` | `255.70` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 14,640.00 USD | 23,250.00 USD | 11,780.00 USD |
| `7D` | `255.80` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,160.00 USD |
| `1D` | `256.10` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD |
| `7D` | `256.30` | 7,700,000.00 USD | 0.00 USD | 7,700,000.00 USD | 60,900.00 USD | 10,260.00 USD | 40,850.00 USD |
| `1D` | `256.50` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD |
| `7D` | `256.80` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 32,750.00 USD | 13,750.00 USD | 64,340.00 USD |
| `1D` | `256.90` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,290.00 USD |
| `1D` | `257.30` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,750.00 USD |
| `7D` | `257.30` | 7,470,000.00 USD | 0.00 USD | 7,470,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,140.00 USD |
| `1D` | `257.70` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD |
| `7D` | `257.80` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,210.00 USD |
| `1D` | `258.10` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,960.00 USD |
| `7D` | `258.30` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,590.00 USD |
| `1D` | `258.50` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.80` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,250.00 USD |
| `1D` | `258.90` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,040.00 USD |
| `1D` | `259.30` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,030.00 USD |
| `1D` | `259.70` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 18,950.00 USD | 34,250.00 USD | 39,290.00 USD |
| `7D` | `259.80` | 6,920,000.00 USD | 0.00 USD | 6,920,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,150.00 USD |
| `1D` | `260.10` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 39,390.00 USD | 8,470.00 USD | 6,880.00 USD |
| `7D` | `260.30` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD |
| `1D` | `260.50` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 19,100.00 USD | 1,010.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 6,540,000.00 USD | 0.00 USD | 6,540,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,210.00 USD |
| `1D` | `260.90` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 9,020.00 USD | 50,800.00 USD | 13,930.00 USD |
| `1D` | `261.30` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 8,130.00 USD | 29,340.00 USD | 33,390.00 USD |
| `7D` | `261.30` | 6,410,000.00 USD | 0.00 USD | 6,410,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,620.00 USD |
| `1D` | `261.70` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 15,200.00 USD | 60,690.00 USD | 51,210.00 USD |
| `7D` | `261.80` | 6,250,000.00 USD | 0.00 USD | 6,250,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,170.00 USD |
| `1D` | `262.10` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 13,620.00 USD | 27,520.00 USD | 21,370.00 USD |
| `7D` | `262.30` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,990.00 USD |
| `1D` | `262.50` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 21,110.00 USD | 4,750.00 USD | 10,870.00 USD |
| `7D` | `262.80` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,810.00 USD |
| `1D` | `262.90` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 629.76 USD | 12,630.00 USD | 19,510.00 USD |
| `1D` | `263.30` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 9,930.00 USD | 4,350.00 USD | 61,480.00 USD |
| `7D` | `263.30` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 33,590.00 USD | 13,710.00 USD | 162.59 USD |
| `1D` | `263.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,380.00 USD |
| `7D` | `263.80` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,810.00 USD |
| `1D` | `264.10` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,360.00 USD |
| `7D` | `264.30` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 48,230.00 USD | 1,170.00 USD | 79.85 USD |
| `1D` | `264.50` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 905.76 USD | 19,920.00 USD | 0.00 USD |
| `7D` | `264.80` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 33,470.00 USD | 21,870.00 USD | 191.76 USD |
| `1D` | `264.90` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 33,200.00 USD | 1,890.00 USD | 53,200.00 USD |
| `1D` | `265.30` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 64,960.00 USD | 1,270.00 USD | 0.00 USD |
| `7D` | `265.30` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 256,440.00 USD | 980.96 USD | 33,940.00 USD |
| `1D` | `265.70` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 629.76 USD | 0.00 USD |
| `7D` | `265.80` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 69,380.00 USD | 0.00 USD | 91.66 USD |
| `1D` | `266.10` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 16,140.00 USD | 13,320.00 USD | 2.86 USD |
| `7D` | `266.30` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 216,090.00 USD | 645.20 USD | 133.68 USD |
| `1D` | `266.50` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 14,240.00 USD | 8,470.00 USD | 4,800.00 USD |
| `7D` | `266.80` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 136,640.00 USD | 63,260.00 USD | 46.14 USD |
| `1D` | `266.90` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 18,330.00 USD | 22,420.00 USD | 0.00 USD |
| `1D` | `267.30` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 33,460.00 USD | 68,530.00 USD | 12,580.00 USD |
| `7D` | `267.30` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 131,280.00 USD | 52,200.00 USD | 77.77 USD |
| `1D` | `267.70` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 5,020.00 USD | 36,260.00 USD | 14,930.00 USD |
| `7D` | `267.80` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,980.00 USD |
| `1D` | `268.10` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 4,570.00 USD | 24,670.00 USD | 60,040.00 USD |
| `7D` | `268.30` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 169,940.00 USD | 150,080.00 USD | 62,760.00 USD |
| `1D` | `268.50` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 0.00 USD | 10,760.00 USD | 80.42 USD |
| `7D` | `268.80` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 23,340.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `268.90` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 8,400.00 USD | 776.90 USD | 305.44 USD |
| `1D` | `269.30` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 7,610.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `269.30` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 3,490.00 USD | 44.11 USD |
| `1D` | `269.70` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 638.90 USD | 17,350.00 USD | 13,580.00 USD |
| `7D` | `269.80` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 0.00 USD | 1,920.00 USD | 0.00 USD |
| `1D` | `270.10` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD |
| `1D` | `270.50` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 42,710.00 USD | 118.00 USD | 4.60 USD |
| `7D` | `270.80` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 33,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `270.90` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 505.00 USD | 14,830.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 12,710.00 USD | 1,780.00 USD | 11,730.00 USD |
| `7D` | `271.30` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.70` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 8,650.00 USD | 34,920.00 USD | 5,300.00 USD |
| `7D` | `271.80` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD |
| `1D` | `272.10` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 21,980.00 USD | 21,380.00 USD | 19,750.00 USD |
| `7D` | `272.30` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 6,060.00 USD | 38,280.00 USD | 41,830.00 USD |
| `7D` | `272.80` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `272.90` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 59,390.00 USD | 5,420.00 USD | 71,650.00 USD |
| `1D` | `273.30` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 18,100.00 USD | 121,350.00 USD | 12,890.00 USD |
| `7D` | `273.30` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD |
| `1D` | `273.70` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 40,330.00 USD | 59,570.00 USD | 69,750.00 USD |
| `7D` | `273.80` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 181,410.00 USD | 0.00 USD | 29,020.00 USD |
| `1D` | `274.10` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 129,290.00 USD | 21,230.00 USD | 12,170.00 USD |
| `7D` | `274.30` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 193,310.00 USD | 0.00 USD | 54,030.00 USD |
| `7D` | `274.80` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `274.90` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 79,290.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.30` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 6,760.00 USD |
| `7D` | `275.30` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 59,580.00 USD | 19,960.00 USD | 21.00 USD |
| `1D` | `275.70` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD |
| `7D` | `275.80` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,340.00 USD |
| `1D` | `276.10` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 161,250.00 USD | 3,340.00 USD | 7,110.00 USD |
| `7D` | `276.30` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 880,320.00 USD | 0.00 USD | 880,320.00 USD | 11,920.00 USD | 5,230.00 USD | 8,810.00 USD |
| `7D` | `276.80` | 896,000.00 USD | 0.00 USD | 896,000.00 USD | 16,100.00 USD | 0.00 USD | 47.25 USD |
| `1D` | `276.90` | 854,360.00 USD | 0.00 USD | 854,360.00 USD | 37,290.00 USD | 25,410.00 USD | 23,470.00 USD |
| `1D` | `277.30` | 768,190.00 USD | 0.00 USD | 768,190.00 USD | 17,610.00 USD | 18,260.00 USD | 10,600.00 USD |
| `7D` | `277.30` | 879,850.00 USD | 0.00 USD | 879,850.00 USD | 152,190.00 USD | 77,800.00 USD | 141,020.00 USD |
| `1D` | `277.70` | 721,720.00 USD | 0.00 USD | 721,720.00 USD | 13,750.00 USD | 10,950.00 USD | 20,310.00 USD |
| `7D` | `277.80` | 508,860.00 USD | 0.00 USD | 508,860.00 USD | 0.00 USD | 157,740.00 USD | 59,940.00 USD |
| `1D` | `278.10` | 676,710.00 USD | 0.00 USD | 676,710.00 USD | 12,120.00 USD | 97,470.00 USD | 83,680.00 USD |
| `7D` | `278.30` | 291,170.00 USD | 0.00 USD | 291,170.00 USD | 24,750.00 USD | 37,090.00 USD | 155,350.00 USD |
| `1D` | `278.50` | 483,440.00 USD | 0.00 USD | 483,440.00 USD | 78,720.00 USD | 56,870.00 USD | 69,670.00 USD |
| `7D` | `278.80` | 73,980.00 USD | 0.00 USD | 73,980.00 USD | 51,310.00 USD | 20,000.00 USD | 0.00 USD |
| `1D` | `278.90` | 278,180.00 USD | 0.00 USD | 278,180.00 USD | 22,390.00 USD | 87,720.00 USD | 28,730.00 USD |
| `1D` | `279.30` | 139,340.00 USD | 0.00 USD | 139,340.00 USD | 11,160.00 USD | 21,610.00 USD | 41,080.00 USD |
| `7D` | `279.30` | 2,670.00 USD | 0.00 USD | 2,670.00 USD | 2,660.00 USD | 0.00 USD | 9.96 USD |
| `1D` | `279.70` | 65,490.00 USD | 0.00 USD | 65,490.00 USD | 19,850.00 USD | 21,310.00 USD | 24,330.00 USD |
| `7D` | `279.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.80` | 58,080.00 USD | 58,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 58,080.00 USD |
| `1D` | `280.10` | 86,600.00 USD | 86,600.00 USD | 0.00 USD | 0.00 USD | 26,770.00 USD | 59,820.00 USD |
| `7D` | `280.30` | 75,500.00 USD | 75,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD |
| `1D` | `280.50` | 212,870.00 USD | 212,870.00 USD | 0.00 USD | 4,150.00 USD | 53,570.00 USD | 68,550.00 USD |
| `7D` | `280.80` | 91,040.00 USD | 91,040.00 USD | 0.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `280.90` | 230,320.00 USD | 230,320.00 USD | 0.00 USD | 0.00 USD | 17,450.00 USD | 0.00 USD |
| `7D` | `281.30` | 188,450.00 USD | 188,450.00 USD | 0.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `7D` | `281.80` | 310,840.00 USD | 310,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 242,730.00 USD | 242,730.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 4,150.00 USD |
| `7D` | `282.30` | 335,060.00 USD | 335,060.00 USD | 0.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `7D` | `282.80` | 335,120.00 USD | 335,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 55.52 USD |
| `1D` | `283.30` | 244,010.00 USD | 244,010.00 USD | 0.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.30` | 338,680.00 USD | 338,680.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 110.18 USD |
| `1D` | `283.70` | 244,030.00 USD | 244,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 20.34 USD |
| `7D` | `283.80` | 340,670.00 USD | 340,670.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 244,050.00 USD | 244,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 15.61 USD |
| `7D` | `284.30` | 342,240.00 USD | 342,240.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 11.42 USD |
| `7D` | `284.80` | 397,710.00 USD | 397,710.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 74.94 USD |
| `1D` | `284.90` | 244,080.00 USD | 244,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 33.63 USD |
| `1D` | `285.30` | 285,770.00 USD | 285,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 41,680.00 USD |
| `7D` | `285.30` | 693,780.00 USD | 693,780.00 USD | 0.00 USD | 68,860.00 USD | 227,210.00 USD | 0.00 USD |
| `1D` | `285.70` | 287,480.00 USD | 287,480.00 USD | 0.00 USD | 1,710.00 USD | 0.00 USD | 4.02 USD |
| `7D` | `285.80` | 892,370.00 USD | 892,370.00 USD | 0.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD |
| `1D` | `286.10` | 338,230.00 USD | 338,230.00 USD | 0.00 USD | 26,810.00 USD | 719.80 USD | 23,220.00 USD |
| `7D` | `286.30` | 936,600.00 USD | 936,600.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 12.00 USD |
| `1D` | `286.50` | 373,570.00 USD | 373,570.00 USD | 0.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD |
| `7D` | `286.80` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 1.44 USD |
| `1D` | `286.90` | 528,420.00 USD | 528,420.00 USD | 0.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD |
| `1D` | `287.30` | 703,940.00 USD | 703,940.00 USD | 0.00 USD | 97,970.00 USD | 43,890.00 USD | 33,660.00 USD |
| `7D` | `287.30` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 70.92 USD |
| `1D` | `287.70` | 799,160.00 USD | 799,160.00 USD | 0.00 USD | 22,860.00 USD | 22,500.00 USD | 49,860.00 USD |
| `7D` | `287.80` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.10` | 881,090.00 USD | 881,090.00 USD | 0.00 USD | 21,420.00 USD | 26,660.00 USD | 33,850.00 USD |
| `7D` | `288.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD |
| `1D` | `288.50` | 988,620.00 USD | 988,620.00 USD | 0.00 USD | 52,260.00 USD | 26,060.00 USD | 29,210.00 USD |
| `7D` | `288.80` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD |
| `1D` | `288.90` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 44,740.00 USD | 24,620.00 USD | 0.00 USD |
| `1D` | `289.30` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 17,220.00 USD | 47,120.00 USD | 51,200.00 USD |
| `7D` | `289.30` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.70` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 52,150.00 USD | 67,790.00 USD | 92,100.00 USD |
| `7D` | `289.80` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD |
| `1D` | `290.10` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 59,800.00 USD | 51,750.00 USD | 100,740.00 USD |
| `7D` | `290.30` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 13,650.00 USD | 116,320.00 USD | 46,660.00 USD |
| `7D` | `290.80` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 898.13 USD | 1,760.00 USD | 58,030.00 USD |
| `1D` | `290.90` | 1,890,000.00 USD | 1,890,000.00 USD | 0.00 USD | 39,460.00 USD | 39,180.00 USD | 41,080.00 USD |
| `1D` | `291.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 14,090.00 USD | 11,300.00 USD | 24,320.00 USD |
| `7D` | `291.30` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 24,680.00 USD | 10,160.00 USD | 9.00 USD |
| `1D` | `291.70` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 9,470.00 USD | 38,560.00 USD | 22,150.00 USD |
| `7D` | `291.80` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 854.05 USD | 37,580.00 USD | 11,490.00 USD |
| `7D` | `292.30` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 88.06 USD |
| `1D` | `292.50` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 29,580.00 USD | 3,650.00 USD | 2,270.00 USD |
| `7D` | `292.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 887.27 USD | 100,630.00 USD | 141.42 USD |
| `1D` | `292.90` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 62,510.00 USD | 30,780.00 USD | 3,560.00 USD |
| `1D` | `293.30` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 22,320.00 USD | 16,660.00 USD | 27,360.00 USD |
| `7D` | `293.30` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 33,580.00 USD | 132,080.00 USD | 61.93 USD |
| `1D` | `293.70` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 76,610.00 USD | 47,640.00 USD | 64,920.00 USD |
| `7D` | `293.80` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 20,900.00 USD |
| `1D` | `294.10` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 21,360.00 USD | 23,760.00 USD | 49,200.00 USD |
| `7D` | `294.30` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD |
| `1D` | `294.50` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 96,500.00 USD | 76,930.00 USD | 85,210.00 USD |
| `7D` | `294.80` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,150.00 USD |
| `1D` | `294.90` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 33,360.00 USD | 16,330.00 USD | 48,710.00 USD |
| `1D` | `295.30` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 15,750.00 USD | 60,930.00 USD | 96,750.00 USD |
| `7D` | `295.30` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 46,330.00 USD | 82,780.00 USD | 345,570.00 USD |
| `1D` | `295.70` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 98,960.00 USD | 6,830.00 USD | 128,460.00 USD |
| `7D` | `295.80` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 165,320.00 USD | 82,100.00 USD | 197,400.00 USD |
| `1D` | `296.10` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 52,840.00 USD | 126,740.00 USD | 35,700.00 USD |
| `7D` | `296.30` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 43,710.00 USD | 167,940.00 USD | 120,990.00 USD |
| `1D` | `296.50` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 33,300.00 USD | 22,420.00 USD | 41,210.00 USD |
| `7D` | `296.80` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 133,820.00 USD | 3,570.00 USD | 201,410.00 USD |
| `1D` | `296.90` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 24,280.00 USD | 21,780.00 USD | 90,460.00 USD |
| `1D` | `297.30` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 61,160.00 USD | 1,000.00 USD | 31,670.00 USD |
| `7D` | `297.30` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 78,980.00 USD | 54,960.00 USD | 56.44 USD |
| `1D` | `297.70` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 15,790.00 USD | 11,180.00 USD | 12,060.00 USD |
| `7D` | `297.80` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 47,530.00 USD | 99,320.00 USD | 89,590.00 USD |
| `1D` | `298.10` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 51,840.00 USD | 8,960.00 USD | 41,570.00 USD |
| `7D` | `298.30` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 32,650.00 USD | 44,630.00 USD | 68,890.00 USD |
| `1D` | `298.50` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 5,790.00 USD | 1,480.00 USD | 56,400.00 USD |
| `7D` | `298.80` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 17.54 USD |
| `1D` | `298.90` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 28,150.00 USD | 5,580.00 USD | 94,680.00 USD |
| `1D` | `299.30` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 33,970.00 USD | 10,810.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD |
| `1D` | `299.70` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 8,250.00 USD | 10,850.00 USD | 27,690.00 USD |
| `7D` | `299.80` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 22,950.00 USD | 9,100.00 USD | 19,840.00 USD |
| `1D` | `300.10` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 19,900.00 USD | 36,560.00 USD | 64,330.00 USD |
| `7D` | `300.30` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 35,320.00 USD | 2,910.00 USD | 52.41 USD |
| `1D` | `300.50` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 23,270.00 USD | 1,560.00 USD | 17,170.00 USD |
| `7D` | `300.80` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,400.00 USD |
| `1D` | `300.90` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 269.05 USD | 1,020.00 USD | 29,480.00 USD |
| `1D` | `301.30` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 597.00 USD | 15,110.00 USD | 20,910.00 USD |
| `7D` | `301.30` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 73,320.00 USD | 58,690.00 USD | 150,710.00 USD |
| `1D` | `301.70` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 19,840.00 USD | 8,470.00 USD | 15,540.00 USD |
| `7D` | `301.80` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,260.00 USD |
| `1D` | `302.10` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 25,190.00 USD | 30,660.00 USD | 10,500.00 USD |
| `7D` | `302.30` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 1,560.00 USD | 181,550.00 USD | 17.37 USD |
| `1D` | `302.50` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 13,820.00 USD | 13,290.00 USD | 38,370.00 USD |
| `7D` | `302.80` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,650.00 USD |
| `1D` | `302.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 1,370.00 USD | 2,260.00 USD | 13,980.00 USD |
| `1D` | `303.30` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 21,200.00 USD | 2,760.00 USD | 9,350.00 USD |
| `7D` | `303.30` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD | 220.53 USD |
| `1D` | `303.70` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 0.00 USD | 391.16 USD | 1.44 USD |
| `7D` | `303.80` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,630.00 USD |
| `1D` | `304.10` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,450.00 USD |
| `1D` | `304.50` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 9,670.00 USD | 2,100.00 USD | 44,530.00 USD |
| `7D` | `304.80` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 36,140.00 USD | 11,790.00 USD | 4,060.00 USD |
| `1D` | `304.90` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD |
| `1D` | `305.30` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 83.23 USD | 172.52 USD | 0.00 USD |
| `7D` | `305.30` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,410.00 USD |
| `1D` | `305.70` | 4,910,000.00 USD | 4,910,000.00 USD | 0.00 USD | 6,340.00 USD | 3,500.00 USD | 5,880.00 USD |
| `7D` | `305.80` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD |
| `1D` | `306.10` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,870.00 USD |
| `1D` | `306.50` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 4,230.00 USD | 6.13 USD | 5,670.00 USD |
| `7D` | `306.80` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 94,690.00 USD | 74,180.00 USD | 69,940.00 USD |
| `1D` | `306.90` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 19,850.00 USD | 38,870.00 USD | 13,060.00 USD |
| `1D` | `307.30` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 5,500.00 USD | 41,920.00 USD | 22,610.00 USD |
| `7D` | `307.30` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD |
| `1D` | `307.70` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 21,890.00 USD | 22,070.00 USD | 4,060.00 USD |
| `7D` | `307.80` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 115,070.00 USD | 113,210.00 USD | 60,700.00 USD |
| `1D` | `308.10` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 20,530.00 USD | 8,780.00 USD | 12,900.00 USD |
| `7D` | `308.30` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 169,010.00 USD | 59,680.00 USD | 114,270.00 USD |
| `1D` | `308.50` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 7,610.00 USD | 3,610.00 USD | 1,590.00 USD |
| `7D` | `308.80` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD |
| `1D` | `308.90` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 7,450.00 USD | 5,920.00 USD | 3,480.00 USD |
| `1D` | `309.30` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 5,190.00 USD | 1,580.00 USD | 2,160.00 USD |
| `7D` | `309.30` | 9,700,000.00 USD | 9,700,000.00 USD | 0.00 USD | 34,260.00 USD | 36,030.00 USD | 36,590.00 USD |
| `1D` | `309.70` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 10,040.00 USD | 7,670.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,780.00 USD |
| `1D` | `310.10` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 14,750.00 USD | 3,980.00 USD | 10,960.00 USD |
| `7D` | `310.30` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 62,230.00 USD | 108,410.00 USD | 80,840.00 USD |
| `1D` | `310.50` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 112.30 USD | 5,020.00 USD | 5,870.00 USD |
| `7D` | `310.80` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 12,200.00 USD |
| `1D` | `310.90` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 5,080.00 USD | 73.70 USD | 20.44 USD |
| `1D` | `311.30` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 257.90 USD | 2,350.00 USD | 107.36 USD |
| `7D` | `311.30` | 10,670,000.00 USD | 10,670,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,780.00 USD |
| `1D` | `311.70` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 7,980.00 USD | 9,070.00 USD | 4,060.00 USD |
| `7D` | `311.80` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 19,570.00 USD | 11,240.00 USD | 25,490.00 USD |
| `1D` | `312.10` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 299.35 USD | 10,320.00 USD | 15,040.00 USD |
| `7D` | `312.30` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 27,560.00 USD |
| `1D` | `312.50` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 14,640.00 USD | 8,480.00 USD | 11,780.00 USD |
| `7D` | `312.80` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 29,070.00 USD | 14,880.00 USD | 19,250.00 USD |
| `1D` | `312.90` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD |
| `1D` | `313.30` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 3,580.00 USD | 18,270.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 10,950,000.00 USD | 10,950,000.00 USD | 0.00 USD | 33,520.00 USD | 10,510.00 USD | 38,400.00 USD |
| `1D` | `313.70` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 4,550.00 USD | 4,260.00 USD | 8,220.00 USD |
| `7D` | `313.80` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 33,220.00 USD | 1,570.00 USD | 44,110.00 USD |
| `7D` | `314.30` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `7D` | `314.80` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,330.00 USD |
| `7D` | `315.30` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 500.10 USD | 547.95 USD | 49.31 USD |
| `7D` | `315.80` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 9,200.00 USD | 43,070.00 USD | 30,000.00 USD |
| `7D` | `316.30` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,400.00 USD |
| `7D` | `316.80` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,370.00 USD |
| `7D` | `317.30` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 157.61 USD |
| `7D` | `317.80` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 164.80 USD |
| `7D` | `318.30` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 627.00 USD | 31,660.00 USD | 32,120.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `303.67M` | Total OI Tokens: `1,083,058.4 BCH`
  * 1h OI Change: `-0.24%` | 4h OI Change: `-1.56%` | 24h OI Change: `-0.20%`
  * Exchange Breakdown: Binance=`88.30M` | Bybit=`37.77M` | OKX=`23.74M` | Hyperliquid=`7.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.77K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0109%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0005%` | **USDT Bitget** | `0.0088%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `39.69%` | `60.31%` | `0.66` | 2,980,000.00 USD |
| `15M` | `Binance` | `40.98%` | `59.02%` | `0.69` | 622,370.00 USD |
| `15M` | `OKX` | `36.16%` | `63.84%` | `0.57` | 171,250.00 USD |
| `15M` | `Bybit` | `41.95%` | `58.05%` | `0.72` | 106,750.00 USD |
| `15M` | `KuCoin` | `47.01%` | `52.99%` | `0.89` | 82,790.00 USD |
| `15M` | `Gate` | `41.85%` | `58.15%` | `0.72` | 39,900.00 USD |
| `15M` | `Bitget` | `34.12%` | `65.88%` | `0.52` | 31,900.00 USD |
| `15M` | `BingX` | `6.86%` | `93.14%` | `0.07` | 530,140.00 USD |
| `15M` | `MEXC` | `32.14%` | `67.86%` | `0.47` | 163,890.00 USD |
| `15M` | `Bitunix` | `43.03%` | `56.97%` | `0.76` | 67,300.00 USD |
| `15M` | `Hyperliquid` | `5.69%` | `94.31%` | `0.06` | 17,680.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `48.95%` | `51.05%` | `0.96` | 907,680.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.69%` | `1.31%` | `75.34` | 189,720.00 USD |
| `15M` | `HTX` | `40.64%` | `59.36%` | `0.68` | 2,280.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `1%` | `99%` | `0.01` | 41,660.00 USD |
| `15M` | `Aster` | `13.9%` | `86.1%` | `0.16` | 646.49 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 1,750.00 USD |
| `15M` | `Whale Positions` | `40.98%` | `59.02%` | `0.69` | 622,370.00 USD |
| `15M` | `Global Accounts` | `39.69%` | `60.31%` | `0.66` | 2,980,000.00 USD |
| `1H` | `BCH` | `39.45%` | `60.55%` | `0.65` | 8,280,000.00 USD |
| `1H` | `Binance` | `41.65%` | `58.35%` | `0.71` | 1,920,000.00 USD |
| `1H` | `OKX` | `40.51%` | `59.49%` | `0.68` | 528,920.00 USD |
| `1H` | `Bybit` | `43.19%` | `56.81%` | `0.76` | 305,170.00 USD |
| `1H` | `KuCoin` | `49.68%` | `50.32%` | `0.99` | 426,930.00 USD |
| `1H` | `Gate` | `49.24%` | `50.76%` | `0.97` | 80,260.00 USD |
| `1H` | `Bitget` | `55.02%` | `44.98%` | `1.22` | 77,850.00 USD |
| `1H` | `BingX` | `9.64%` | `90.36%` | `0.11` | 1,930,000.00 USD |
| `1H` | `MEXC` | `53.98%` | `46.02%` | `1.17` | 389,790.00 USD |
| `1H` | `Bitunix` | `44.15%` | `55.85%` | `0.79` | 143,020.00 USD |
| `1H` | `Hyperliquid` | `10.85%` | `89.15%` | `0.12` | 94,910.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.5%` | `50.5%` | `0.98` | 1,820,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `96.64%` | `3.36%` | `28.76` | 464,300.00 USD |
| `1H` | `HTX` | `29.44%` | `70.56%` | `0.42` | 4,850.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `2.57%` | `97.43%` | `0.03` | 91,640.00 USD |
| `1H` | `Aster` | `13.74%` | `86.26%` | `0.16` | 694.68 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `81.27%` | `18.73%` | `4.34` | 2,040.00 USD |
| `1H` | `Whale Positions` | `41.65%` | `58.35%` | `0.71` | 1,920,000.00 USD |
| `1H` | `Global Accounts` | `39.45%` | `60.55%` | `0.65` | 8,280,000.00 USD |
| `4H` | `BCH` | `49.10%` | `50.90%` | `0.96` | 41,920,000.00 USD |
| `4H` | `Binance` | `49.62%` | `50.38%` | `0.98` | 12,790,000.00 USD |
| `4H` | `OKX` | `42.72%` | `57.28%` | `0.75` | 4,850,000.00 USD |
| `4H` | `Bybit` | `54.4%` | `45.6%` | `1.19` | 3,950,000.00 USD |
| `4H` | `KuCoin` | `50.78%` | `49.22%` | `1.03` | 396,650.00 USD |
| `4H` | `Gate` | `48.57%` | `51.43%` | `0.94` | 4,270,000.00 USD |
| `4H` | `Bitget` | `51.69%` | `48.31%` | `1.07` | 1,510,000.00 USD |
| `4H` | `BingX` | `41.6%` | `58.4%` | `0.71` | 8,580,000.00 USD |
| `4H` | `MEXC` | `47.42%` | `52.58%` | `0.90` | 1,050,000.00 USD |
| `4H` | `Bitunix` | `42.66%` | `57.34%` | `0.74` | 904,830.00 USD |
| `4H` | `Hyperliquid` | `45.17%` | `54.83%` | `0.82` | 428,700.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 1,240,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `88.6%` | `11.4%` | `7.77` | 1,840,000.00 USD |
| `4H` | `HTX` | `56.38%` | `43.62%` | `1.29` | 55,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.35%` | `61.65%` | `0.62` | 12,920.00 USD |
| `4H` | `Aster` | `41.03%` | `58.97%` | `0.70` | 17,280.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.91%` | `23.09%` | `3.33` | 14,820.00 USD |
| `4H` | `Whale Positions` | `49.62%` | `50.38%` | `0.98` | 12,790,000.00 USD |
| `4H` | `Global Accounts` | `49.10%` | `50.90%` | `0.96` | 41,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `285.00` | `284.61` | `285.00` | `285.70` | `284.11` | 545,839.06 USD | 236,872.05 USD | 308,967.02 USD | -72,094.97 USD | `-13.21%` | `24B / 34S` |
| `5:00 UTC` | `283.52` | `283.26` | `283.52` | `284.35` | `282.63` | 1,065,026.94 USD | 445,113.55 USD | 619,913.39 USD | -174,799.84 USD | `-16.41%` | `16B / 48S` |
| `0:00 UTC` | `284.50` | `283.96` | `284.50` | `284.69` | `283.25` | 675,487.52 USD | 439,670.02 USD | 235,817.50 USD | 203,852.52 USD | `+30.18%` | `42B / 21S` |
| `5:00 UTC` | `284.25` | `284.51` | `284.25` | `284.85` | `284.24` | 356,795.30 USD | 184,835.04 USD | 171,960.26 USD | 12,874.78 USD | `+3.61%` | `14B / 15S` |
| `0:00 UTC` | `282.15` | `283.00` | `282.15` | `284.87` | `281.41` | 1,285,912.66 USD | 419,903.43 USD | 866,009.23 USD | -446,105.80 USD | `-34.69%` | `7B / 53S` |
| `5:00 UTC` | `281.32` | `281.51` | `281.32` | `282.72` | `280.80` | 1,039,042.65 USD | 453,949.26 USD | 585,093.39 USD | -131,144.13 USD | `-12.62%` | `25B / 59S` |
| `0:00 UTC` | `281.50` | `282.15` | `281.50` | `283.26` | `281.24` | 1,246,277.92 USD | 838,584.24 USD | 407,693.68 USD | 430,890.56 USD | `+34.57%` | `32B / 6S` |
| `5:00 UTC` | `283.12` | `282.91` | `283.12` | `283.64` | `281.86` | 898,717.53 USD | 422,080.39 USD | 476,637.13 USD | -54,556.74 USD | `-6.07%` | `22B / 36S` |
| `0:00 UTC` | `280.81` | `281.09` | `280.81` | `281.94` | `280.02` | 959,751.07 USD | 348,775.30 USD | 610,975.78 USD | -262,200.48 USD | `-27.32%` | `10B / 71S` |
| `5:00 UTC` | `279.86` | `279.87` | `279.86` | `280.47` | `279.61` | 402,210.54 USD | 204,803.91 USD | 197,406.63 USD | 7,397.28 USD | `+1.84%` | `10B / 15S` |

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
| `5m` | -33,420.00 USD | -36,730.00 USD | **`DISTRIBUTION`** |
| `15m` | -91,460.00 USD | -513,530.00 USD | **`DISTRIBUTION`** |
| `30m` | -147,670.00 USD | -670,070.00 USD | **`DISTRIBUTION`** |
| `1h` | -54,840.00 USD | 360,940.00 USD | **`ACCUMULATION`** |
| `2h` | 155,430.00 USD | -350,590.00 USD | **`DISTRIBUTION`** |
| `4h` | 235,660.00 USD | 218,440.00 USD | **`ACCUMULATION`** |
| `6h` | 969,610.00 USD | -170,150.00 USD | **`ACCUMULATION`** |
| `8h` | 1,290,000.00 USD | 1,100,000.00 USD | **`ACCUMULATION`** |
| `12h` | 984,580.00 USD | -286,010.00 USD | **`ACCUMULATION`** |
| `24h` | 264,420.00 USD | -2,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -578,630.00 USD | -15,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,010,000.00 USD | -136,820,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-33.42K` | 15m=`-91.46K` | 1h=`-54.84K` | 24h=`+264.42K`
* Futures Capital Netflows: 5m=`-36.73K` | 15m=`-513.53K` | 1h=`+360.94K` | 24h=`-2.48M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `267.54` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `263.97` (Risk Distance: `3.57` pts)
  * +2.5R Take Profit: `276.47`
  * Mathematical Lot Sizing: **`2.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `281.28` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `284.85` (Risk Distance: `3.57` pts)
  * +2.5R Take Profit: `272.35`
  * Mathematical Lot Sizing: **`2.80 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`281.33`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
