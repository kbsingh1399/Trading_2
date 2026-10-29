# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LINK
**Canonical Key**: `LINK` | **Broker Instrument**: `LNKUSD.p` | **Asset Class**: `Crypto DeFi`
**Timestamp**: `2026-10-30 02:57:59 IST` (`2026-10-29 21:27:59 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `11.17` | **Live Ask Quote**: `11.26` | **Mid Price**: `11.22`
- **Spread Points**: `94.00` | **Spread BPS**: `83.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `11.51` | VWAP Z-Score: `-1.84` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1302` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `28.42` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `12.18` | Lower -3.00σ Band: `10.84`
  * Upper +2.51σ Band: `12.08` | Lower -2.51σ Band: `10.95`
  * Upper +2.01σ Band: `11.96` | Lower -2.01σ Band: `11.06`
  * Upper +2.00σ Band: `11.96` | Lower -2.00σ Band: `11.06`
  * Upper +1.28σ Band: `11.80` | Lower -1.28σ Band: `11.23`
  * Upper +1.00σ Band: `11.74` | Lower -1.00σ Band: `11.29`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`11.32` | EMA-20=`11.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`11.55` (Slope: `+0.0000`) | EMA-100=`11.56`
  * Institutional Anchors: EMA-144=`11.55` | EMA-200=`11.52` (Slope: `-0.0826`) | EMA-233=`11.51`
- **Range Boundaries**: 24H High=`11.96` | 24H Low=`10.85` | Weekly High=`11.96` | Weekly Low=`10.85`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `11.24` (Distance: `-0.16%`)
  * Point of Control (POC) = `11.10` (Distance: `+1.13%`)
  * Value Area Low (VAL) = `11.04` (Distance: `+1.67%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`11.89` | POC=`11.77` | VAL=`11.42`
  * Prior Day Extremes: PDH=`11.96` | PDL=`10.85` | PDC=`10.96`
  * Monday Range Blueprint: High=`11.57` | Mid=`11.39` | Low=`11.21`
  * Developing Weekly Value Area: Weekly VAH=`11.60` | Weekly POC=`11.42` | Weekly VAL=`11.25`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`11.24` | Low=`10.91`
  * London Session (08:00-16:00 UTC): High=`11.26` | Low=`11.17`
  * New York Session (13:00-21:00 UTC): High=`11.28` | Low=`11.15`
  * Initial Balance (First Hour): IB High=`11.25` | IB Low=`11.18`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `11.17` - `11.26`
  * Optimal Trade Entry (OTE 0.705): `11.24`
  * Structural Invalidation Anchor (0.786): `11.31`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `10.98` | `11.11` | `10.96` | `11.11` | `319,827` | 3,534,911.88 USD | -331,139.21 USD | `-9.37%` | -6,918,226.17 USD | `-0.19` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.10` | `11.18` | `11.09` | `11.15` | `303,806` | 3,382,614.26 USD | -102,797.65 USD | `-3.04%` | -7,021,023.82 USD | `+0.22` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `11.15` | `11.16` | `11.14` | `11.16` | `3,919` | 43,712.03 USD | 8,699.81 USD | `+19.90%` | -7,012,324.01 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `11.09` | `11.19` | `10.87` | `10.99` | `1,617,019` | 17,839,742.46 USD | -1,008,665.90 USD | `-5.65%` | -6,401,806.18 USD | `-1.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `10.99` | `11.18` | `10.95` | `11.15` | `965,373` | 10,677,747.31 USD | -466,056.13 USD | `-4.36%` | -6,867,862.31 USD | `-0.25` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `11.15` | `11.16` | `11.14` | `11.16` | `3,919` | 43,712.03 USD | 8,699.81 USD | `+19.90%` | -6,859,162.50 USD | `+0.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `11.68` | `11.73` | `11.63` | `11.69` | `318,927` | 3,725,220.26 USD | -245,323.17 USD | `-6.59%` | -2,290,022.42 USD | `-0.30` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `11.69` | `11.69` | `10.87` | `10.99` | `3,805,467` | 42,673,690.41 USD | -4,269,954.14 USD | `-10.01%` | -6,559,976.56 USD | `-3.77` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `10.99` | `11.18` | `10.95` | `11.15` | `969,586` | 10,724,740.75 USD | -458,411.24 USD | `-4.27%` | -7,018,387.80 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `11.15` | `4,775,142` | 53,399,435.47 USD | -4,729,369.69 USD | `-8.86%` | -6,447,867.29 USD | `-1.83` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `11.39` | `11.61` | `11.35` | `11.36` | `1,494,144` | 17,147,912.14 USD | 35,814.13 USD | `+0.21%` | -2,314,397.87 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `11.36` | `11.64` | `11.36` | `11.62` | `1,461,597` | 16,828,194.13 USD | 293,381.62 USD | `+1.74%` | -2,021,016.25 USD | `+0.81` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.62` | `11.97` | `11.56` | `11.96` | `2,672,805` | 31,394,868.04 USD | 1,331,903.83 USD | `+4.24%` | -689,112.42 USD | `+1.12` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `11.96` | `12.01` | `11.62` | `11.69` | `2,069,523` | 24,399,480.64 USD | -1,029,385.18 USD | `-4.22%` | -1,718,497.60 USD | `-0.55` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `11.69` | `11.69` | `10.87` | `11.15` | `4,775,142` | 53,399,435.47 USD | -4,729,369.69 USD | `-8.86%` | -6,447,867.29 USD | `-1.83` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`11.22`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:55:39 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `501` | `0x73ce...8ce9` | `LONG` | 4,472,621.70 USD | `400,011,600.00` | `12.05` | `11.16` | `9.12` | -347,132.00 USD | `-7.76%` | `5X Cross` |
| `838` | `0xb83d...6e36` | `SHORT` | 2,713,720.81 USD | `242,013,000.00` | `12.93` | `11.16` | `587.50` | 416,173.38 USD | `+15.34%` | `3X Cross` |
| `885` | `0x458d...ab3b` | `LONG` | 2,550,742.58 USD | `227,156,700.00` | `13.13` | `11.16` | `9.34` | -431,487.81 USD | `-16.92%` | `3X Isolated` |
| `979` | `0xdd53...2b13` | `SHORT` | 2,314,146.26 USD | `206,475,300.00` | `11.92` | `11.16` | `294.62` | 147,076.67 USD | `+6.36%` | `3X Cross` |
| `1001` | `0x3dc9...54b0` | `SHORT` | 2,241,000.00 USD | `200,000,000.00` | `7.56` | `11.16` | `90.90` | -729,841.58 USD | `-32.57%` | `10X Cross` |
| `1019` | `0x45d2...4029` | `SHORT` | 2,192,290.08 USD | `195,500,000.00` | `11.54` | `11.16` | `206.58` | 64,193.35 USD | `+2.93%` | `10X Cross` |
| `1123` | `0x5b5d...c060` | `SHORT` | 1,986,146.94 USD | `177,429,600.00` | `13.61` | `11.16` | `947.75` | 428,391.76 USD | `+21.57%` | `3X Cross` |
| `1212` | `0x6540...f7b7` | `LONG` | 1,863,394.81 USD | `165,871,000.00` | `12.46` | `11.16` | `7.80` | -202,873.41 USD | `-10.89%` | `5X Isolated` |
| `1300` | `0xeadc...9d55` | `LONG` | 1,736,972.97 USD | `157,691,600.00` | `9.43` | `11.16` | `0.000000` | 250,318.07 USD | `+14.41%` | `10X Cross` |
| `1676` | `0xf6f3...47f8` | `SHORT` | 1,284,249.66 USD | `115,024,600.00` | `11.42` | `11.16` | `20.03` | 29,080.53 USD | `+2.26%` | `5X Cross` |
| `1705` | `0x9df2...c665` | `SHORT` | 1,256,460.89 USD | `112,344,500.00` | `11.48` | `11.16` | `279.35` | 33,694.17 USD | `+2.68%` | `10X Cross` |
| `1824` | `0xfe7e...11b4` | `LONG` | 1,136,734.94 USD | `101,142,000.00` | `14.47` | `11.16` | `5.33` | -326,378.21 USD | `-28.71%` | `5X Isolated` |
| `1865` | `0x8af7...fa05` | `SHORT` | 1,108,754.57 USD | `98,661,200.00` | `14.08` | `11.16` | `202.98` | 280,427.97 USD | `+25.29%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `11.52` | 6,666.62 USD | `-` | `NEWS_INTEL` | `-` | #LINK Whale BUY: 6.67K USD at 11.5200 USD [API] | `2026-10-28 13:52:39` |
| `ANNOUNCEMENT` | `INFO` | `13.19` | 10,315.36 USD | `-` | `NEWS_INTEL` | `-` | #LINK Liquidated Long: 10.32K USD at 13.1910 USD [API] | `2026-10-02 18:39:42` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`11.92` (Vol: 146,200.00 USD, Dist: `+3.39%`) | Long MP=`11.40` (Vol: 165,300.00 USD, Dist: `--1.15%`)
  * 48H Horizon: Short MP=`12.05` (Vol: 224,500.00 USD, Dist: `+4.50%`) | Long MP=`11.28` (Vol: 248,100.00 USD, Dist: `--2.18%`)
  * 3D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+5.97%`) | Long MP=`11.15` (Vol: 359,300.00 USD, Dist: `--3.29%`)
  * 7D Horizon: Short MP=`12.22` (Vol: 248,100.00 USD, Dist: `+5.98%`) | Long MP=`11.16` (Vol: 661,300.00 USD, Dist: `--3.26%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `2.35` | 486.45 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.45` | 1,230.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.65` | 4,150.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.75` | 27,030.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 2,620.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.05` | 6,390.00 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 961.07 USD | 12,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 592.95 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.45` | 8,190.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.55` | 2,510.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.65` | 2,630.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 3,750.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.85` | 13,360.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.05` | 6,300.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.35` | 12,630.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 4,470.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.65` | 17,540.00 USD | 12,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 50,880.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.85` | 239,270.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 883.08 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 91,360.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 886.73 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.35` | 541,800.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 20,990.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.55` | 748.14 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.65` | 35,600.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 1,520.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.85` | 22,830.00 USD | 11,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 790.76 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 68,690.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.15` | 9,240.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 80,020.00 USD | 11,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.35` | 23,300.00 USD | 11,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.45` | 9,150.00 USD | 11,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 2,710.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.65` | 9,260.00 USD | 11,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 7,650.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.85` | 34,470.00 USD | 11,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 37,510.00 USD | 11,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.05` | 14,440.00 USD | 11,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.15` | 686,800.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 8,460.00 USD | 10,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.35` | 52,130.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 9,870.00 USD | 10,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.55` | 19,770.00 USD | 10,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.65` | 9,240.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.75` | 14,100.00 USD | 10,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.85` | 3,010.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.95` | 171,890.00 USD | 10,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.05` | 1,410,000.00 USD | 10,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.15` | 29,940.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.25` | 35,750.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.35` | 7,780.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.45` | 53,810.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.55` | 21,580.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.65` | 15,370.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.75` | 312,090.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.85` | 28,570.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `8.95` | 505,780.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.05` | 76,580.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.15` | 3,720,000.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.25` | 41,710.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.35` | 2,150,000.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.45` | 26,730.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.55` | 12,490.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `9.65` | 9,080.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.69` | 7,380,000.00 USD | 7,380,000.00 USD | 5,240.00 USD | 0.00 USD | 18.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.71` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.73` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.75` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.75` | 54,360.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `9.77` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.85` | 19,550.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.86` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.89` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.90` | 3,230,000.00 USD | 3,230,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.92` | 3,210,000.00 USD | 3,210,000.00 USD | 13,840.00 USD | 5,510.00 USD | 118.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.93` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.94` | 3,190,000.00 USD | 3,190,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.95` | 7,300,000.00 USD | 7,300,000.00 USD | 14,920.00 USD | 10,650.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `9.95` | 760,400.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `9.96` | 3,190,000.00 USD | 3,190,000.00 USD | 7,630.00 USD | 5,510.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.97` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 370.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `9.98` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 6,510.00 USD | 11,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `9.99` | 7,260,000.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.00` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.01` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.04` | 3,150,000.00 USD | 3,150,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.05` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.05` | 647,590.00 USD | 989,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.06` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.07` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.09` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 7,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.11` | 7,240,000.00 USD | 7,240,000.00 USD | 279.85 USD | 0.00 USD | 5,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.12` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.13` | 7,230,000.00 USD | 7,230,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.14` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.15` | 7,170,000.00 USD | 7,170,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.15` | 28,910.00 USD | 342,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.16` | 3,130,000.00 USD | 3,130,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.17` | 7,120,000.00 USD | 7,120,000.00 USD | 56,890.00 USD | 3,240.00 USD | 21,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.18` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.19` | 7,040,000.00 USD | 7,040,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.20` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.21` | 6,980,000.00 USD | 6,980,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.22` | 3,120,000.00 USD | 3,120,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.23` | 6,870,000.00 USD | 6,870,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.24` | 3,090,000.00 USD | 3,090,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.25` | 6,570,000.00 USD | 6,570,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.25` | 35,700.00 USD | 313,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.26` | 3,030,000.00 USD | 3,030,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.27` | 6,450,000.00 USD | 6,450,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.28` | 3,020,000.00 USD | 3,020,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.29` | 6,270,000.00 USD | 6,270,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.30` | 2,970,000.00 USD | 2,970,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.31` | 6,190,000.00 USD | 6,190,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.32` | 2,950,000.00 USD | 2,950,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.33` | 6,000,000.00 USD | 6,000,000.00 USD | 58,810.00 USD | 28,270.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.34` | 2,900,000.00 USD | 2,900,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.35` | 5,890,000.00 USD | 5,890,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.35` | 14,650.00 USD | 277,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.36` | 2,860,000.00 USD | 2,860,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.37` | 5,820,000.00 USD | 5,820,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.38` | 2,830,000.00 USD | 2,830,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.39` | 5,780,000.00 USD | 5,780,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.40` | 2,810,000.00 USD | 2,810,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.41` | 5,700,000.00 USD | 5,700,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.42` | 2,780,000.00 USD | 2,780,000.00 USD | 20,220.00 USD | 10,800.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.43` | 5,560,000.00 USD | 5,560,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.44` | 2,740,000.00 USD | 2,740,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.45` | 5,490,000.00 USD | 5,490,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.45` | 16,780.00 USD | 262,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.46` | 2,670,000.00 USD | 2,670,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.47` | 5,400,000.00 USD | 5,400,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.48` | 2,650,000.00 USD | 2,650,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.49` | 5,320,000.00 USD | 5,320,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.50` | 2,620,000.00 USD | 2,620,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.51` | 5,270,000.00 USD | 5,270,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.52` | 2,580,000.00 USD | 2,580,000.00 USD | 29,580.00 USD | 4,150.00 USD | 31,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.53` | 5,180,000.00 USD | 5,180,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.54` | 2,510,000.00 USD | 2,510,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.55` | 5,140,000.00 USD | 5,140,000.00 USD | 55,490.00 USD | 18,800.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.55` | 68,110.00 USD | 246,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.56` | 2,510,000.00 USD | 2,510,000.00 USD | 58,790.00 USD | 23,780.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.57` | 5,050,000.00 USD | 5,050,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.58` | 2,420,000.00 USD | 2,420,000.00 USD | 37,820.00 USD | 16,800.00 USD | 21,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.59` | 4,940,000.00 USD | 4,940,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.60` | 2,350,000.00 USD | 2,350,000.00 USD | 15,350.00 USD | 5,500.00 USD | 3,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.61` | 4,840,000.00 USD | 4,840,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.62` | 2,320,000.00 USD | 2,320,000.00 USD | 41,350.00 USD | 12,840.00 USD | 46,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.63` | 4,680,000.00 USD | 4,680,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.64` | 2,220,000.00 USD | 2,220,000.00 USD | 13,350.00 USD | 20,950.00 USD | 12,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.65` | 4,600,000.00 USD | 4,600,000.00 USD | 20,460.00 USD | 3,850.00 USD | 32,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.65` | 40,290.00 USD | 177,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.66` | 2,170,000.00 USD | 2,170,000.00 USD | 48,910.00 USD | 16,150.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.67` | 4,550,000.00 USD | 4,550,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.68` | 2,070,000.00 USD | 2,070,000.00 USD | 17,480.00 USD | 3,750.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.69` | 4,510,000.00 USD | 4,510,000.00 USD | 18,290.00 USD | 793.25 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.70` | 2,050,000.00 USD | 2,050,000.00 USD | 37,930.00 USD | 9,600.00 USD | 11,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.71` | 4,490,000.00 USD | 4,490,000.00 USD | 16,910.00 USD | 0.00 USD | 7,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.72` | 1,990,000.00 USD | 1,990,000.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.73` | 4,460,000.00 USD | 4,460,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.74` | 1,970,000.00 USD | 1,970,000.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.75` | 4,430,000.00 USD | 4,430,000.00 USD | 17,290.00 USD | 4,890.00 USD | 318.86 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.75` | 50,130.00 USD | 137,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.76` | 1,900,000.00 USD | 1,900,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.77` | 4,410,000.00 USD | 4,410,000.00 USD | 16,290.00 USD | 22,040.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.78` | 1,880,000.00 USD | 1,880,000.00 USD | 86,290.00 USD | 57,540.00 USD | 57.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.79` | 4,360,000.00 USD | 4,360,000.00 USD | 57,970.00 USD | 1,400.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.80` | 1,730,000.00 USD | 1,730,000.00 USD | 73,580.00 USD | 27,960.00 USD | 25,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.81` | 4,270,000.00 USD | 4,270,000.00 USD | 86,860.00 USD | 80,110.00 USD | 120,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.82` | 1,610,000.00 USD | 1,610,000.00 USD | 30,650.00 USD | 1,080.00 USD | 68.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.83` | 3,990,000.00 USD | 3,990,000.00 USD | 193,560.00 USD | 98,340.00 USD | 113,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.84` | 1,580,000.00 USD | 1,580,000.00 USD | 54,340.00 USD | 15,320.00 USD | 69,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.85` | 3,580,000.00 USD | 3,580,000.00 USD | 231,680.00 USD | 23,820.00 USD | 82,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.85` | 86,320.00 USD | 87,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.86` | 1,440,000.00 USD | 1,440,000.00 USD | 976.86 USD | 30,860.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.87` | 3,240,000.00 USD | 3,240,000.00 USD | 110,460.00 USD | 43,170.00 USD | 164,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.88` | 1,400,000.00 USD | 1,400,000.00 USD | 64,750.00 USD | 42,700.00 USD | 82,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.89` | 2,930,000.00 USD | 2,930,000.00 USD | 235,210.00 USD | 36,770.00 USD | 133,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.90` | 1,210,000.00 USD | 1,210,000.00 USD | 23,940.00 USD | 4,880.00 USD | 0.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.91` | 2,520,000.00 USD | 2,520,000.00 USD | 274,660.00 USD | 1,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.92` | 1,180,000.00 USD | 1,180,000.00 USD | 97,980.00 USD | 43,900.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.93` | 2,240,000.00 USD | 2,240,000.00 USD | 418,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.94` | 1,020,000.00 USD | 1,020,000.00 USD | 98,180.00 USD | 17,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.95` | 1,830,000.00 USD | 1,830,000.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `10.95` | 1,240.00 USD | 1,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `10.96` | 902,260.00 USD | 902,260.00 USD | 96,940.00 USD | 23,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.97` | 1,520,000.00 USD | 1,520,000.00 USD | 165,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `10.98` | 782,310.00 USD | 782,310.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `10.99` | 1,350,000.00 USD | 1,350,000.00 USD | 44,540.00 USD | 36,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.01` | 1,270,000.00 USD | 1,270,000.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.02` | 768,980.00 USD | 768,980.00 USD | 0.00 USD | 37,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.03` | 1,260,000.00 USD | 1,260,000.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.05` | 1,250,000.00 USD | 1,250,000.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.07` | 1,250,000.00 USD | 1,250,000.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.09` | 1,240,000.00 USD | 1,240,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.10` | 731,430.00 USD | 731,430.00 USD | 0.00 USD | 0.00 USD | 106.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.11` | 1,230,000.00 USD | 1,230,000.00 USD | 5,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.12` | 731,330.00 USD | 731,330.00 USD | 632.30 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.13` | 1,230,000.00 USD | 1,230,000.00 USD | 6,820.00 USD | 162,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.14` | 730,700.00 USD | 730,700.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.15` | 1,060,000.00 USD | 1,060,000.00 USD | 2,410.00 USD | 123,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.15` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `11.16` | 728,800.00 USD | 728,800.00 USD | 337.20 USD | 27,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.17` | 933,220.00 USD | 933,220.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.18` | 700,820.00 USD | 700,820.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.19` | 929,250.00 USD | 929,250.00 USD | 4,050.00 USD | 0.00 USD | 63,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.20` | 653,080.00 USD | 653,080.00 USD | 43,350.00 USD | 39,010.00 USD | 98,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.21` | 861,830.00 USD | 861,830.00 USD | 319,760.00 USD | 0.00 USD | 282,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.22` | 472,040.00 USD | 472,040.00 USD | 262,690.00 USD | 587.72 USD | 43,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `11.23` | 259,840.00 USD | 259,840.00 USD | 201,470.00 USD | 0.00 USD | 58,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `11.24` | 165,710.00 USD | 165,710.00 USD | 69,220.00 USD | 399.60 USD | 96,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.25` | 495,720.00 USD | 495,720.00 USD | 332,220.00 USD | 2,180.00 USD | 161,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 99,790.00 USD | 99,790.00 USD | 28,620.00 USD | 815.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.26` | 199,580.00 USD | 199,580.00 USD | 28,620.00 USD | 815.00 USD | 70,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.27` | 943,160.00 USD | 943,160.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.28` | 443,040.00 USD | 443,040.00 USD | 38,150.00 USD | 18,580.00 USD | 186,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.29` | 1,100,000.00 USD | 1,100,000.00 USD | 104,970.00 USD | 0.00 USD | 55,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.30` | 545,480.00 USD | 545,480.00 USD | 0.00 USD | 60,470.00 USD | 41,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.31` | 1,410,000.00 USD | 1,410,000.00 USD | 28,170.00 USD | 43,020.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.32` | 734,070.00 USD | 734,070.00 USD | 63,250.00 USD | 66,390.00 USD | 58,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.33` | 1,490,000.00 USD | 1,490,000.00 USD | 54,410.00 USD | 8,920.00 USD | 18,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.34` | 987,060.00 USD | 987,060.00 USD | 197,970.00 USD | 55,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.35` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 60,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.35` | 6,720.00 USD | 456,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.36` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 98,460.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.37` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 50,580.00 USD | 99,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.38` | 1,210,000.00 USD | 1,210,000.00 USD | 51,260.00 USD | 55,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.39` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.41` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.42` | 1,530,000.00 USD | 1,530,000.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.43` | 2,050,000.00 USD | 2,050,000.00 USD | 133,220.00 USD | 65,620.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.44` | 1,650,000.00 USD | 1,650,000.00 USD | 42,610.00 USD | 18,500.00 USD | 52,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.45` | 2,300,000.00 USD | 2,300,000.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.45` | 99,610.00 USD | 556,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.46` | 1,750,000.00 USD | 1,750,000.00 USD | 34,610.00 USD | 51,530.00 USD | 12,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.47` | 2,390,000.00 USD | 2,390,000.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.48` | 1,770,000.00 USD | 1,770,000.00 USD | 14,310.00 USD | 4,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.49` | 2,530,000.00 USD | 2,530,000.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.50` | 1,840,000.00 USD | 1,840,000.00 USD | 19,080.00 USD | 19,160.00 USD | 34,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.51` | 2,570,000.00 USD | 2,570,000.00 USD | 40,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.52` | 1,880,000.00 USD | 1,880,000.00 USD | 29,340.00 USD | 13,170.00 USD | 418.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.53` | 2,660,000.00 USD | 2,660,000.00 USD | 48,860.00 USD | 5,190.00 USD | 32,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.54` | 1,960,000.00 USD | 1,960,000.00 USD | 31,460.00 USD | 16,150.00 USD | 29,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.55` | 2,110.00 USD | 558,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.56` | 2,040,000.00 USD | 2,040,000.00 USD | 64,190.00 USD | 635.25 USD | 15,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.57` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.58` | 2,100,000.00 USD | 2,100,000.00 USD | 45,400.00 USD | 335.85 USD | 17,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.59` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.60` | 2,300,000.00 USD | 2,300,000.00 USD | 124,870.00 USD | 7,320.00 USD | 67,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.61` | 2,760,000.00 USD | 2,760,000.00 USD | 44,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.62` | 2,380,000.00 USD | 2,380,000.00 USD | 42,200.00 USD | 0.00 USD | 34,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.63` | 2,790,000.00 USD | 2,790,000.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.65` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 877.75 USD | 306.68 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.65` | 60,080.00 USD | 618,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `11.67` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 22,340.00 USD | 61,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.68` | 2,470,000.00 USD | 2,470,000.00 USD | 59,600.00 USD | 28,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.69` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 381.10 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.70` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 313.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.71` | 3,080,000.00 USD | 3,080,000.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.72` | 2,720,000.00 USD | 2,720,000.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.73` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.74` | 2,850,000.00 USD | 2,850,000.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.75` | 3,110,000.00 USD | 3,110,000.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.75` | 2,100.00 USD | 620,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.76` | 2,900,000.00 USD | 2,900,000.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.77` | 3,250,000.00 USD | 3,250,000.00 USD | 30,810.00 USD | 27,570.00 USD | 76,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.78` | 2,980,000.00 USD | 2,980,000.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.79` | 3,320,000.00 USD | 3,320,000.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.80` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 14,340.00 USD | 394.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.81` | 3,490,000.00 USD | 3,490,000.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.82` | 3,020,000.00 USD | 3,020,000.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.83` | 3,620,000.00 USD | 3,620,000.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.84` | 3,150,000.00 USD | 3,150,000.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.85` | 3,830,000.00 USD | 3,830,000.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `11.85` | 2,440.00 USD | 623,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `11.86` | 3,230,000.00 USD | 3,230,000.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.87` | 3,860,000.00 USD | 3,860,000.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.88` | 3,320,000.00 USD | 3,320,000.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.89` | 3,920,000.00 USD | 3,920,000.00 USD | 40,020.00 USD | 16,380.00 USD | 71.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.90` | 3,380,000.00 USD | 3,380,000.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.91` | 4,000,000.00 USD | 4,000,000.00 USD | 82,030.00 USD | 0.00 USD | 397.61 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.92` | 3,550,000.00 USD | 3,550,000.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.93` | 4,070,000.00 USD | 4,070,000.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.94` | 3,610,000.00 USD | 3,610,000.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.95` | 4,310,000.00 USD | 4,310,000.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.96` | 3,730,000.00 USD | 3,730,000.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.97` | 4,930,000.00 USD | 4,930,000.00 USD | 354,730.00 USD | 35,140.00 USD | 223,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `11.98` | 3,890,000.00 USD | 3,890,000.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `11.99` | 5,320,000.00 USD | 5,320,000.00 USD | 242,400.00 USD | 17,110.00 USD | 130,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.00` | 3,990,000.00 USD | 3,990,000.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.01` | 5,730,000.00 USD | 5,730,000.00 USD | 164,140.00 USD | 5,360.00 USD | 247,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.02` | 4,090,000.00 USD | 4,090,000.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.03` | 6,390,000.00 USD | 6,390,000.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.04` | 4,470,000.00 USD | 4,470,000.00 USD | 209,440.00 USD | 65,620.00 USD | 97,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.05` | 7,040,000.00 USD | 7,040,000.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.06` | 4,890,000.00 USD | 4,890,000.00 USD | 187,660.00 USD | 88,160.00 USD | 147,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.07` | 7,610,000.00 USD | 7,610,000.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.08` | 5,100,000.00 USD | 5,100,000.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.09` | 7,900,000.00 USD | 7,900,000.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.10` | 5,170,000.00 USD | 5,170,000.00 USD | 36,180.00 USD | 16,940.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.11` | 8,170,000.00 USD | 8,170,000.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.12` | 5,430,000.00 USD | 5,430,000.00 USD | 138,630.00 USD | 60,020.00 USD | 63,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.13` | 8,440,000.00 USD | 8,440,000.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.14` | 5,620,000.00 USD | 5,620,000.00 USD | 92,340.00 USD | 33,200.00 USD | 55,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.15` | 9,040,000.00 USD | 9,040,000.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.16` | 5,850,000.00 USD | 5,850,000.00 USD | 126,410.00 USD | 37,730.00 USD | 67,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.17` | 9,180,000.00 USD | 9,180,000.00 USD | 26,820.00 USD | 61,400.00 USD | 53,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.18` | 6,040,000.00 USD | 6,040,000.00 USD | 112,590.00 USD | 42,390.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.19` | 9,510,000.00 USD | 9,510,000.00 USD | 196,200.00 USD | 58,580.00 USD | 79,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.20` | 6,190,000.00 USD | 6,190,000.00 USD | 77,890.00 USD | 43,590.00 USD | 31,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.21` | 9,910,000.00 USD | 9,910,000.00 USD | 200,760.00 USD | 62,900.00 USD | 128,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.22` | 6,250,000.00 USD | 6,250,000.00 USD | 12,890.00 USD | 16,780.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.23` | 10,120,000.00 USD | 10,120,000.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.24` | 6,280,000.00 USD | 6,280,000.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.25` | 10,420,000.00 USD | 10,420,000.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.25` | 552.48 USD | 623,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.26` | 6,370,000.00 USD | 6,370,000.00 USD | 43,220.00 USD | 22,010.00 USD | 21,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.27` | 10,650,000.00 USD | 10,650,000.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.28` | 6,510,000.00 USD | 6,510,000.00 USD | 83,960.00 USD | 17,410.00 USD | 37,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.29` | 11,170,000.00 USD | 11,170,000.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.30` | 6,610,000.00 USD | 6,610,000.00 USD | 57,170.00 USD | 16,300.00 USD | 36,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.31` | 11,410,000.00 USD | 11,410,000.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.32` | 6,620,000.00 USD | 6,620,000.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.33` | 11,680,000.00 USD | 11,680,000.00 USD | 165,330.00 USD | 96,930.00 USD | 5,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.34` | 6,670,000.00 USD | 6,670,000.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.35` | 11,830,000.00 USD | 11,830,000.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.35` | 736.06 USD | 624,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.36` | 6,710,000.00 USD | 6,710,000.00 USD | 19,360.00 USD | 16,550.00 USD | 5,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.37` | 11,900,000.00 USD | 11,900,000.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.38` | 6,750,000.00 USD | 6,750,000.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.39` | 12,440,000.00 USD | 12,440,000.00 USD | 160,660.00 USD | 42,040.00 USD | 338,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.40` | 6,800,000.00 USD | 6,800,000.00 USD | 18,820.00 USD | 12,140.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.41` | 12,660,000.00 USD | 12,660,000.00 USD | 80,100.00 USD | 25,020.00 USD | 113,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.42` | 6,880,000.00 USD | 6,880,000.00 USD | 57,750.00 USD | 13,980.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.43` | 13,250,000.00 USD | 13,250,000.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.44` | 6,920,000.00 USD | 6,920,000.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.45` | 13,670,000.00 USD | 13,670,000.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.46` | 6,930,000.00 USD | 6,930,000.00 USD | 269.21 USD | 9,440.00 USD | 4,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.47` | 13,840,000.00 USD | 13,840,000.00 USD | 66,870.00 USD | 29,080.00 USD | 75,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.48` | 6,940,000.00 USD | 6,940,000.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.49` | 14,010,000.00 USD | 14,010,000.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.50` | 6,960,000.00 USD | 6,960,000.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.51` | 14,250,000.00 USD | 14,250,000.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.52` | 7,020,000.00 USD | 7,020,000.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.53` | 14,560,000.00 USD | 14,560,000.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.54` | 7,030,000.00 USD | 7,030,000.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.55` | 14,810,000.00 USD | 14,810,000.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.55` | 1,870.00 USD | 626,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.56` | 7,080,000.00 USD | 7,080,000.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.57` | 15,000,000.00 USD | 15,000,000.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.58` | 7,100,000.00 USD | 7,100,000.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.59` | 15,120,000.00 USD | 15,120,000.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.60` | 7,120,000.00 USD | 7,120,000.00 USD | 15,910.00 USD | 3,320.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.61` | 15,250,000.00 USD | 15,250,000.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.62` | 7,150,000.00 USD | 7,150,000.00 USD | 13,530.00 USD | 9,530.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.63` | 15,420,000.00 USD | 15,420,000.00 USD | 64,120.00 USD | 28,270.00 USD | 81,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.64` | 7,200,000.00 USD | 7,200,000.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.65` | 15,610,000.00 USD | 15,610,000.00 USD | 76,240.00 USD | 26,110.00 USD | 90,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.65` | 527.51 USD | 626,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.66` | 7,230,000.00 USD | 7,230,000.00 USD | 4,470.00 USD | 3,450.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.67` | 15,920,000.00 USD | 15,920,000.00 USD | 65,670.00 USD | 16,240.00 USD | 223,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.68` | 7,250,000.00 USD | 7,250,000.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.69` | 16,160,000.00 USD | 16,160,000.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.70` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.71` | 16,260,000.00 USD | 16,260,000.00 USD | 31,960.00 USD | 43,220.00 USD | 24,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.72` | 7,280,000.00 USD | 7,280,000.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.73` | 16,350,000.00 USD | 16,350,000.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.74` | 7,310,000.00 USD | 7,310,000.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.75` | 16,420,000.00 USD | 16,420,000.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.76` | 7,380,000.00 USD | 7,380,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.77` | 16,510,000.00 USD | 16,510,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.78` | 7,400,000.00 USD | 7,400,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.79` | 16,600,000.00 USD | 16,600,000.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.80` | 7,430,000.00 USD | 7,430,000.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.81` | 16,620,000.00 USD | 16,620,000.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.82` | 7,440,000.00 USD | 7,440,000.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.83` | 16,650,000.00 USD | 16,650,000.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.84` | 7,470,000.00 USD | 7,470,000.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.85` | 16,730,000.00 USD | 16,730,000.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `12.85` | 138.78 USD | 627,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `12.86` | 7,510,000.00 USD | 7,510,000.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.87` | 16,770,000.00 USD | 16,770,000.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.88` | 7,520,000.00 USD | 7,520,000.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.89` | 16,860,000.00 USD | 16,860,000.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.90` | 7,540,000.00 USD | 7,540,000.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.91` | 16,960,000.00 USD | 16,960,000.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.92` | 7,550,000.00 USD | 7,550,000.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.93` | 16,980,000.00 USD | 16,980,000.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.94` | 7,550,000.00 USD | 7,550,000.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.95` | 17,000,000.00 USD | 17,000,000.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.96` | 7,560,000.00 USD | 7,560,000.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.97` | 17,030,000.00 USD | 17,030,000.00 USD | 13,890.00 USD | 10,560.00 USD | 10,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `12.98` | 7,600,000.00 USD | 7,600,000.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `12.99` | 17,100,000.00 USD | 17,100,000.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `13.00` | 7,630,000.00 USD | 7,630,000.00 USD | 11,890.00 USD | 7,680.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.01` | 17,110,000.00 USD | 17,110,000.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.03` | 17,120,000.00 USD | 17,120,000.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.05` | 17,120,000.00 USD | 17,120,000.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.05` | 1,520.00 USD | 628,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `13.07` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.09` | 17,130,000.00 USD | 17,130,000.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.11` | 17,160,000.00 USD | 17,160,000.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.13` | 17,160,000.00 USD | 17,160,000.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.17` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.19` | 17,190,000.00 USD | 17,190,000.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.21` | 17,210,000.00 USD | 17,210,000.00 USD | 13,890.00 USD | 213.60 USD | 8,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.23` | 17,220,000.00 USD | 17,220,000.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.25` | 17,290,000.00 USD | 17,290,000.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.27` | 17,320,000.00 USD | 17,320,000.00 USD | 10,290.00 USD | 8,420.00 USD | 10,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.29` | 17,320,000.00 USD | 17,320,000.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.31` | 17,350,000.00 USD | 17,350,000.00 USD | 12,560.00 USD | 6,580.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `13.33` | 17,360,000.00 USD | 17,360,000.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `13.45` | 5,280.00 USD | 633,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.55` | 2,990.00 USD | 636,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.05` | 347.04 USD | 637,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.45` | 541.88 USD | 637,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.75` | 321.55 USD | 638,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.95` | 25,330.00 USD | 663,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.15` | 368.14 USD | 663,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.55` | 838.14 USD | 664,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.85` | 56,350.00 USD | 720,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.95` | 138.76 USD | 721,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.35` | 1,530.00 USD | 722,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.55` | 17,510.00 USD | 740,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.85` | 10,770.00 USD | 750,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.95` | 79,770.00 USD | 830,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.15` | 2,330.00 USD | 832,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.45` | 121,870.00 USD | 954,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.75` | 5,480.00 USD | 960,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.85` | 249,580.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.95` | 621.07 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.05` | 1,970.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.25` | 27,790.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.45` | 3,890.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.55` | 185.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.65` | 72,830.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.75` | 707,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.85` | 456.17 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `18.95` | 16,250.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.65` | 38,790.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `19.95` | 291.27 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.35` | 2,340,000.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.45` | 1,270.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `20.55` | 10,800.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `21.95` | 17,530.00 USD | 4,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `2.35` | 12,670,000.00 USD | 0.00 USD | 486.45 USD | `-78.61%` | `207,000.00` |
| `Live` | `Long` | `2.45` | 12,670,000.00 USD | 0.00 USD | 1,230.00 USD | `-77.70%` | `502,600.00` |
| `Live` | `Long` | `2.65` | 12,670,000.00 USD | 0.00 USD | 4,150.00 USD | `-75.88%` | `1,567,100.00` |
| `Live` | `Long` | `2.75` | 12,660,000.00 USD | 0.00 USD | 27,030.00 USD | `-74.97%` | `9,829,500.00` |
| `Live` | `Long` | `2.85` | 12,630,000.00 USD | 0.00 USD | 2,620.00 USD | `-74.06%` | `920,000.00` |
| `Live` | `Long` | `3.05` | 12,630,000.00 USD | 0.00 USD | 6,390.00 USD | `-72.24%` | `2,096,000.00` |
| `Live` | `Long` | `3.15` | 12,630,000.00 USD | 0.00 USD | 961.07 USD | `-71.33%` | `305,100.00` |
| `Live` | `Long` | `3.35` | 12,620,000.00 USD | 0.00 USD | 592.95 USD | `-69.51%` | `177,000.00` |
| `Live` | `Long` | `3.45` | 12,620,000.00 USD | 0.00 USD | 8,190.00 USD | `-68.60%` | `2,373,100.00` |
| `Live` | `Long` | `3.55` | 12,620,000.00 USD | 0.00 USD | 2,510.00 USD | `-67.69%` | `707,000.00` |
| `Live` | `Long` | `3.65` | 12,610,000.00 USD | 0.00 USD | 2,630.00 USD | `-66.78%` | `719,500.00` |
| `Live` | `Long` | `3.75` | 12,610,000.00 USD | 0.00 USD | 3,750.00 USD | `-65.87%` | `1,000,000.00` |
| `Live` | `Long` | `3.85` | 12,610,000.00 USD | 0.00 USD | 13,360.00 USD | `-64.96%` | `3,469,700.00` |
| `Live` | `Long` | `4.05` | 12,590,000.00 USD | 0.00 USD | 6,300.00 USD | `-63.14%` | `1,554,700.00` |
| `Live` | `Long` | `4.35` | 12,590,000.00 USD | 0.00 USD | 12,630.00 USD | `-60.41%` | `2,903,200.00` |
| `Live` | `Long` | `4.45` | 12,570,000.00 USD | 0.00 USD | 4,470.00 USD | `-59.50%` | `1,005,500.00` |
| `Live` | `Long` | `4.65` | 12,570,000.00 USD | 0.00 USD | 17,540.00 USD | `-57.68%` | `3,772,100.00` |
| `Live` | `Long` | `4.75` | 12,550,000.00 USD | 0.00 USD | 50,880.00 USD | `-56.77%` | `10,712,500.00` |
| `Live` | `Long` | `4.85` | 12,500,000.00 USD | 0.00 USD | 239,270.00 USD | `-55.86%` | `49,334,900.00` |
| `Live` | `Long` | `4.95` | 12,260,000.00 USD | 0.00 USD | 883.08 USD | `-54.95%` | `178,400.00` |
| `Live` | `Long` | `5.05` | 12,260,000.00 USD | 0.00 USD | 91,360.00 USD | `-54.04%` | `18,091,700.00` |
| `Live` | `Long` | `5.25` | 12,170,000.00 USD | 0.00 USD | 886.73 USD | `-52.22%` | `168,900.00` |
| `Live` | `Long` | `5.35` | 12,170,000.00 USD | 0.00 USD | 541,800.00 USD | `-51.31%` | `101,271,900.00` |
| `Live` | `Long` | `5.45` | 11,630,000.00 USD | 0.00 USD | 20,990.00 USD | `-50.40%` | `3,850,700.00` |
| `Live` | `Long` | `5.55` | 11,610,000.00 USD | 0.00 USD | 748.14 USD | `-49.49%` | `134,800.00` |
| `Live` | `Long` | `5.65` | 11,610,000.00 USD | 0.00 USD | 35,600.00 USD | `-48.58%` | `6,300,800.00` |
| `Live` | `Long` | `5.75` | 11,570,000.00 USD | 0.00 USD | 1,520.00 USD | `-47.67%` | `263,500.00` |
| `Live` | `Long` | `5.85` | 11,570,000.00 USD | 0.00 USD | 22,830.00 USD | `-46.76%` | `3,901,800.00` |
| `Live` | `Long` | `5.95` | 11,550,000.00 USD | 0.00 USD | 790.76 USD | `-45.85%` | `132,900.00` |
| `Live` | `Long` | `6.05` | 11,550,000.00 USD | 0.00 USD | 68,690.00 USD | `-44.93%` | `11,354,000.00` |
| `Live` | `Long` | `6.15` | 11,480,000.00 USD | 0.00 USD | 9,240.00 USD | `-44.02%` | `1,502,600.00` |
| `Live` | `Long` | `6.25` | 11,470,000.00 USD | 0.00 USD | 80,020.00 USD | `-43.11%` | `12,802,500.00` |
| `Live` | `Long` | `6.35` | 11,390,000.00 USD | 0.00 USD | 23,300.00 USD | `-42.20%` | `3,669,800.00` |
| `Live` | `Long` | `6.45` | 11,360,000.00 USD | 0.00 USD | 9,150.00 USD | `-41.29%` | `1,418,300.00` |
| `Live` | `Long` | `6.55` | 11,350,000.00 USD | 0.00 USD | 2,710.00 USD | `-40.38%` | `414,300.00` |
| `Live` | `Long` | `6.65` | 11,350,000.00 USD | 0.00 USD | 9,260.00 USD | `-39.47%` | `1,391,800.00` |
| `Live` | `Long` | `6.75` | 11,340,000.00 USD | 0.00 USD | 7,650.00 USD | `-38.56%` | `1,133,600.00` |
| `Live` | `Long` | `6.85` | 11,340,000.00 USD | 0.00 USD | 34,470.00 USD | `-37.65%` | `5,031,900.00` |
| `Live` | `Long` | `6.95` | 11,300,000.00 USD | 0.00 USD | 37,510.00 USD | `-36.74%` | `5,397,100.00` |
| `Live` | `Long` | `7.05` | 11,260,000.00 USD | 0.00 USD | 14,440.00 USD | `-35.83%` | `2,047,600.00` |
| `Live` | `Long` | `7.15` | 11,250,000.00 USD | 0.00 USD | 686,800.00 USD | `-34.92%` | `96,055,400.00` |
| `Live` | `Long` | `7.25` | 10,560,000.00 USD | 0.00 USD | 8,460.00 USD | `-34.01%` | `1,167,100.00` |
| `Live` | `Long` | `7.35` | 10,550,000.00 USD | 0.00 USD | 52,130.00 USD | `-33.10%` | `7,092,500.00` |
| `Live` | `Long` | `7.45` | 10,500,000.00 USD | 0.00 USD | 9,870.00 USD | `-32.19%` | `1,324,400.00` |
| `Live` | `Long` | `7.55` | 10,490,000.00 USD | 0.00 USD | 19,770.00 USD | `-31.28%` | `2,618,600.00` |
| `Live` | `Long` | `7.65` | 10,470,000.00 USD | 0.00 USD | 9,240.00 USD | `-30.37%` | `1,208,100.00` |
| `Live` | `Long` | `7.75` | 10,460,000.00 USD | 0.00 USD | 14,100.00 USD | `-29.46%` | `1,819,600.00` |
| `Live` | `Long` | `7.85` | 10,450,000.00 USD | 0.00 USD | 3,010.00 USD | `-28.55%` | `383,000.00` |
| `Live` | `Long` | `7.95` | 10,450,000.00 USD | 0.00 USD | 171,890.00 USD | `-27.64%` | `21,621,200.00` |
| `Live` | `Long` | `8.05` | 10,270,000.00 USD | 0.00 USD | 1,410,000.00 USD | `-26.73%` | `174,682,100.00` |
| `Live` | `Long` | `8.15` | 8,870,000.00 USD | 0.00 USD | 29,940.00 USD | `-25.82%` | `3,673,500.00` |
| `Live` | `Long` | `8.25` | 8,840,000.00 USD | 0.00 USD | 35,750.00 USD | `-24.91%` | `4,333,100.00` |
| `Live` | `Long` | `8.35` | 8,800,000.00 USD | 0.00 USD | 7,780.00 USD | `-24.00%` | `932,100.00` |
| `Live` | `Long` | `8.45` | 8,790,000.00 USD | 0.00 USD | 53,810.00 USD | `-23.09%` | `6,368,100.00` |
| `Live` | `Long` | `8.55` | 8,740,000.00 USD | 0.00 USD | 21,580.00 USD | `-22.18%` | `2,523,600.00` |
| `Live` | `Long` | `8.65` | 8,720,000.00 USD | 0.00 USD | 15,370.00 USD | `-21.27%` | `1,777,300.00` |
| `Live` | `Long` | `8.75` | 8,700,000.00 USD | 0.00 USD | 312,090.00 USD | `-20.36%` | `35,667,200.00` |
| `Live` | `Long` | `8.85` | 8,390,000.00 USD | 0.00 USD | 28,570.00 USD | `-19.45%` | `3,228,700.00` |
| `Live` | `Long` | `8.95` | 8,360,000.00 USD | 0.00 USD | 505,780.00 USD | `-18.54%` | `56,512,000.00` |
| `Live` | `Long` | `9.05` | 7,860,000.00 USD | 0.00 USD | 76,580.00 USD | `-17.63%` | `8,462,300.00` |
| `Live` | `Long` | `9.15` | 7,780,000.00 USD | 0.00 USD | 3,720,000.00 USD | `-16.72%` | `406,248,000.00` |
| `Live` | `Long` | `9.25` | 4,060,000.00 USD | 0.00 USD | 41,710.00 USD | `-15.81%` | `4,509,300.00` |
| `Live` | `Long` | `9.35` | 4,020,000.00 USD | 0.00 USD | 2,150,000.00 USD | `-14.90%` | `229,832,900.00` |
| `Live` | `Long` | `9.45` | 1,870,000.00 USD | 0.00 USD | 26,730.00 USD | `-13.99%` | `2,829,000.00` |
| `Live` | `Long` | `9.55` | 1,850,000.00 USD | 0.00 USD | 12,490.00 USD | `-13.08%` | `1,307,500.00` |
| `Live` | `Long` | `9.65` | 1,830,000.00 USD | 0.00 USD | 9,080.00 USD | `-12.17%` | `940,600.00` |
| `Live` | `Long` | `9.75` | 1,820,000.00 USD | 0.00 USD | 54,360.00 USD | `-11.26%` | `5,575,400.00` |
| `Live` | `Long` | `9.85` | 1,770,000.00 USD | 0.00 USD | 19,550.00 USD | `-10.35%` | `1,985,100.00` |
| `Live` | `Long` | `9.95` | 1,750,000.00 USD | 0.00 USD | 760,400.00 USD | `-9.44%` | `76,422,600.00` |
| `Live` | `Long` | `10.05` | 989,720.00 USD | 0.00 USD | 647,590.00 USD | `-8.53%` | `64,436,800.00` |
| `Live` | `Long` | `10.15` | 342,130.00 USD | 0.00 USD | 28,910.00 USD | `-7.62%` | `2,848,100.00` |
| `Live` | `Long` | `10.25` | 313,230.00 USD | 0.00 USD | 35,700.00 USD | `-6.71%` | `3,482,600.00` |
| `Live` | `Long` | `10.35` | 277,530.00 USD | 0.00 USD | 14,650.00 USD | `-5.80%` | `1,415,900.00` |
| `Live` | `Long` | `10.45` | 262,880.00 USD | 0.00 USD | 16,780.00 USD | `-4.89%` | `1,606,100.00` |
| `Live` | `Long` | `10.55` | 246,090.00 USD | 0.00 USD | 68,110.00 USD | `-3.98%` | `6,456,000.00` |
| `Live` | `Long` | `10.65` | 177,980.00 USD | 0.00 USD | 40,290.00 USD | `-3.07%` | `3,782,800.00` |
| `Live` | `Long` | `10.75` | 137,690.00 USD | 0.00 USD | 50,130.00 USD | `-2.16%` | `4,663,700.00` |
| `Live` | `Long` | `10.85` | 87,560.00 USD | 0.00 USD | 86,320.00 USD | `-1.25%` | `7,955,900.00` |
| `Live` | `Long` | `10.95` | 1,240.00 USD | 0.00 USD | 1,240.00 USD | `-0.34%` | `113,000.00` |
| `Live` | `Short` | `11.15` | 450,140.00 USD | 450,140.00 USD | 0.00 USD | `+1.48%` | `40,371,500.00` |
| `Live` | `Short` | `11.35` | 456,860.00 USD | 6,720.00 USD | 0.00 USD | `+3.30%` | `591,900.00` |
| `Live` | `Short` | `11.45` | 556,480.00 USD | 99,610.00 USD | 0.00 USD | `+4.21%` | `8,700,000.00` |
| `Live` | `Short` | `11.55` | 558,580.00 USD | 2,110.00 USD | 0.00 USD | `+5.12%` | `182,300.00` |
| `Live` | `Short` | `11.65` | 618,660.00 USD | 60,080.00 USD | 0.00 USD | `+6.03%` | `5,156,700.00` |
| `Live` | `Short` | `11.75` | 620,760.00 USD | 2,100.00 USD | 0.00 USD | `+6.94%` | `178,700.00` |
| `Live` | `Short` | `11.85` | 623,200.00 USD | 2,440.00 USD | 0.00 USD | `+7.85%` | `206,300.00` |
| `Live` | `Short` | `12.25` | 623,750.00 USD | 552.48 USD | 0.00 USD | `+11.50%` | `45,100.00` |
| `Live` | `Short` | `12.35` | 624,490.00 USD | 736.06 USD | 0.00 USD | `+12.41%` | `59,600.00` |
| `Live` | `Short` | `12.55` | 626,360.00 USD | 1,870.00 USD | 0.00 USD | `+14.23%` | `149,100.00` |
| `Live` | `Short` | `12.65` | 626,890.00 USD | 527.51 USD | 0.00 USD | `+15.14%` | `41,700.00` |
| `Live` | `Short` | `12.85` | 627,030.00 USD | 138.78 USD | 0.00 USD | `+16.96%` | `10,800.00` |
| `Live` | `Short` | `13.05` | 628,540.00 USD | 1,520.00 USD | 0.00 USD | `+18.78%` | `116,200.00` |
| `Live` | `Short` | `13.45` | 633,830.00 USD | 5,280.00 USD | 0.00 USD | `+22.42%` | `392,900.00` |
| `Live` | `Short` | `13.55` | 636,810.00 USD | 2,990.00 USD | 0.00 USD | `+23.33%` | `220,300.00` |
| `Live` | `Short` | `14.05` | 637,160.00 USD | 347.04 USD | 0.00 USD | `+27.88%` | `24,700.00` |
| `Live` | `Short` | `14.45` | 637,700.00 USD | 541.88 USD | 0.00 USD | `+31.52%` | `37,500.00` |
| `Live` | `Short` | `14.75` | 638,020.00 USD | 321.55 USD | 0.00 USD | `+34.25%` | `21,800.00` |
| `Live` | `Short` | `14.95` | 663,360.00 USD | 25,330.00 USD | 0.00 USD | `+36.07%` | `1,694,600.00` |
| `Live` | `Short` | `15.15` | 663,730.00 USD | 368.14 USD | 0.00 USD | `+37.89%` | `24,300.00` |
| `Live` | `Short` | `15.55` | 664,560.00 USD | 838.14 USD | 0.00 USD | `+41.53%` | `53,900.00` |
| `Live` | `Short` | `15.85` | 720,910.00 USD | 56,350.00 USD | 0.00 USD | `+44.26%` | `3,554,900.00` |
| `Live` | `Short` | `15.95` | 721,050.00 USD | 138.76 USD | 0.00 USD | `+45.17%` | `8,700.00` |
| `Live` | `Short` | `16.35` | 722,580.00 USD | 1,530.00 USD | 0.00 USD | `+48.81%` | `93,700.00` |
| `Live` | `Short` | `16.55` | 740,090.00 USD | 17,510.00 USD | 0.00 USD | `+50.63%` | `1,058,000.00` |
| `Live` | `Short` | `16.85` | 750,860.00 USD | 10,770.00 USD | 0.00 USD | `+53.36%` | `639,000.00` |
| `Live` | `Short` | `16.95` | 830,630.00 USD | 79,770.00 USD | 0.00 USD | `+54.27%` | `4,706,300.00` |
| `Live` | `Short` | `17.15` | 832,960.00 USD | 2,330.00 USD | 0.00 USD | `+56.09%` | `136,100.00` |
| `Live` | `Short` | `17.45` | 954,830.00 USD | 121,870.00 USD | 0.00 USD | `+58.82%` | `6,984,000.00` |
| `Live` | `Short` | `17.75` | 960,320.00 USD | 5,480.00 USD | 0.00 USD | `+61.55%` | `309,000.00` |
| `Live` | `Short` | `17.85` | 1,210,000.00 USD | 249,580.00 USD | 0.00 USD | `+62.46%` | `13,982,000.00` |
| `Live` | `Short` | `17.95` | 1,210,000.00 USD | 621.07 USD | 0.00 USD | `+63.37%` | `34,600.00` |
| `Live` | `Short` | `18.05` | 1,210,000.00 USD | 1,970.00 USD | 0.00 USD | `+64.29%` | `109,300.00` |
| `Live` | `Short` | `18.25` | 1,240,000.00 USD | 27,790.00 USD | 0.00 USD | `+66.11%` | `1,523,000.00` |
| `Live` | `Short` | `18.45` | 1,240,000.00 USD | 3,890.00 USD | 0.00 USD | `+67.93%` | `210,800.00` |
| `Live` | `Short` | `18.55` | 1,240,000.00 USD | 185.50 USD | 0.00 USD | `+68.84%` | `10,000.00` |
| `Live` | `Short` | `18.65` | 1,320,000.00 USD | 72,830.00 USD | 0.00 USD | `+69.75%` | `3,905,000.00` |
| `Live` | `Short` | `18.75` | 2,020,000.00 USD | 707,620.00 USD | 0.00 USD | `+70.66%` | `37,739,700.00` |
| `Live` | `Short` | `18.85` | 2,030,000.00 USD | 456.17 USD | 0.00 USD | `+71.57%` | `24,200.00` |
| `Live` | `Short` | `18.95` | 2,040,000.00 USD | 16,250.00 USD | 0.00 USD | `+72.48%` | `857,700.00` |
| `Live` | `Short` | `19.65` | 2,080,000.00 USD | 38,790.00 USD | 0.00 USD | `+78.85%` | `1,974,000.00` |
| `Live` | `Short` | `19.95` | 2,080,000.00 USD | 291.27 USD | 0.00 USD | `+81.58%` | `14,600.00` |
| `Live` | `Short` | `20.35` | 4,420,000.00 USD | 2,340,000.00 USD | 0.00 USD | `+85.22%` | `115,024,600.00` |
| `Live` | `Short` | `20.45` | 4,420,000.00 USD | 1,270.00 USD | 0.00 USD | `+86.13%` | `62,300.00` |
| `Live` | `Short` | `20.55` | 4,430,000.00 USD | 10,800.00 USD | 0.00 USD | `+87.04%` | `525,500.00` |
| `Live` | `Short` | `21.95` | 4,450,000.00 USD | 17,530.00 USD | 0.00 USD | `+99.78%` | `798,800.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `3.55` | 583,520.00 USD | 0.00 USD | 431.68 USD | `-67.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.55` | 583,080.00 USD | 0.00 USD | 290.29 USD | `-58.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.25` | 582,790.00 USD | 0.00 USD | 120.22 USD | `-52.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.05` | 582,670.00 USD | 0.00 USD | 107.09 USD | `-44.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.55` | 582,570.00 USD | 0.00 USD | 3,760.00 USD | `-40.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.65` | 578,800.00 USD | 0.00 USD | 133.00 USD | `-39.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.05` | 578,670.00 USD | 0.00 USD | 3,770.00 USD | `-35.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 574,900.00 USD | 0.00 USD | 2,070.00 USD | `-34.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.45` | 572,830.00 USD | 0.00 USD | 3,740.00 USD | `-32.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.55` | 569,090.00 USD | 0.00 USD | 1,050.00 USD | `-31.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.85` | 568,030.00 USD | 0.00 USD | 146.80 USD | `-28.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 567,890.00 USD | 0.00 USD | 5,000.00 USD | `-26.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 562,890.00 USD | 0.00 USD | 564.79 USD | `-25.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.25` | 562,320.00 USD | 0.00 USD | 10,660.00 USD | `-24.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 551,660.00 USD | 0.00 USD | 1,360.00 USD | `-23.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 550,300.00 USD | 0.00 USD | 30,250.00 USD | `-22.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.65` | 520,050.00 USD | 0.00 USD | 186.84 USD | `-21.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.75` | 519,860.00 USD | 0.00 USD | 742.88 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.85` | 519,120.00 USD | 0.00 USD | 196.47 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.95` | 518,930.00 USD | 0.00 USD | 1,320.00 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.05` | 517,610.00 USD | 0.00 USD | 2,240.00 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.15` | 515,360.00 USD | 0.00 USD | 194.90 USD | `-16.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.35` | 515,170.00 USD | 0.00 USD | 7,050.00 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.55` | 508,120.00 USD | 0.00 USD | 10,530.00 USD | `-13.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.65` | 497,590.00 USD | 0.00 USD | 3,550.00 USD | `-12.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.75` | 494,040.00 USD | 0.00 USD | 6,490.00 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.85` | 487,560.00 USD | 0.00 USD | 23,380.00 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `9.95` | 464,180.00 USD | 0.00 USD | 299,650.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.05` | 164,520.00 USD | 0.00 USD | 2,590.00 USD | `-8.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.15` | 161,930.00 USD | 0.00 USD | 1,050.00 USD | `-7.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.25` | 160,880.00 USD | 0.00 USD | 92,770.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.35` | 68,110.00 USD | 0.00 USD | 7,610.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.45` | 60,500.00 USD | 0.00 USD | 21,220.00 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.55` | 39,280.00 USD | 0.00 USD | 24,160.00 USD | `-3.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.65` | 15,130.00 USD | 0.00 USD | 2,300.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.75` | 12,820.00 USD | 0.00 USD | 6,800.00 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.85` | 6,020.00 USD | 0.00 USD | 5,870.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `10.95` | 148.92 USD | 0.00 USD | 148.92 USD | `-0.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.05` | 18,860.00 USD | 18,860.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.15` | 19,820.00 USD | 958.90 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.25` | 81,850.00 USD | 62,030.00 USD | 0.00 USD | `+2.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.35` | 82,880.00 USD | 1,030.00 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.45` | 83,170.00 USD | 287.39 USD | 0.00 USD | `+4.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.55` | 83,290.00 USD | 116.66 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.65` | 84,020.00 USD | 732.79 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.75` | 88,480.00 USD | 4,460.00 USD | 0.00 USD | `+6.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.85` | 89,130.00 USD | 651.75 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.95` | 89,290.00 USD | 156.55 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.05` | 137,400.00 USD | 48,110.00 USD | 0.00 USD | `+9.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.15` | 139,280.00 USD | 1,880.00 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.25` | 155,260.00 USD | 15,980.00 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.35` | 155,910.00 USD | 649.61 USD | 0.00 USD | `+12.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.45` | 156,770.00 USD | 859.05 USD | 0.00 USD | `+13.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.55` | 277,070.00 USD | 120,300.00 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.65` | 327,310.00 USD | 50,240.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.75` | 340,470.00 USD | 13,170.00 USD | 0.00 USD | `+16.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.85` | 360,530.00 USD | 20,060.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.95` | 360,990.00 USD | 461.02 USD | 0.00 USD | `+17.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.05` | 367,180.00 USD | 6,190.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.15` | 368,230.00 USD | 1,050.00 USD | 0.00 USD | `+19.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.25` | 369,550.00 USD | 1,320.00 USD | 0.00 USD | `+20.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.35` | 374,280.00 USD | 4,730.00 USD | 0.00 USD | `+21.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.45` | 376,470.00 USD | 2,200.00 USD | 0.00 USD | `+22.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.55` | 376,640.00 USD | 165.31 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.65` | 378,790.00 USD | 2,150.00 USD | 0.00 USD | `+24.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.75` | 380,850.00 USD | 2,060.00 USD | 0.00 USD | `+25.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.85` | 385,200.00 USD | 4,350.00 USD | 0.00 USD | `+26.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.95` | 385,460.00 USD | 266.44 USD | 0.00 USD | `+26.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.05` | 410,250.00 USD | 24,790.00 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.15` | 410,760.00 USD | 506.57 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.35` | 414,170.00 USD | 3,410.00 USD | 0.00 USD | `+30.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.55` | 414,390.00 USD | 218.25 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.65` | 417,000.00 USD | 2,610.00 USD | 0.00 USD | `+33.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.75` | 429,920.00 USD | 12,920.00 USD | 0.00 USD | `+34.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.95` | 430,880.00 USD | 950.82 USD | 0.00 USD | `+36.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.05` | 443,490.00 USD | 12,620.00 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.15` | 445,700.00 USD | 2,200.00 USD | 0.00 USD | `+37.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.25` | 678,740.00 USD | 233,040.00 USD | 0.00 USD | `+38.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.35` | 679,920.00 USD | 1,180.00 USD | 0.00 USD | `+39.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.45` | 680,810.00 USD | 893.01 USD | 0.00 USD | `+40.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.55` | 681,200.00 USD | 388.75 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.65` | 682,150.00 USD | 949.96 USD | 0.00 USD | `+42.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.75` | 684,480.00 USD | 2,330.00 USD | 0.00 USD | `+43.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 689,820.00 USD | 5,340.00 USD | 0.00 USD | `+44.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.95` | 695,170.00 USD | 5,350.00 USD | 0.00 USD | `+45.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.05` | 704,340.00 USD | 9,170.00 USD | 0.00 USD | `+46.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.15` | 711,140.00 USD | 6,800.00 USD | 0.00 USD | `+46.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.25` | 729,900.00 USD | 18,760.00 USD | 0.00 USD | `+47.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.35` | 764,130.00 USD | 34,220.00 USD | 0.00 USD | `+48.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.45` | 770,710.00 USD | 6,580.00 USD | 0.00 USD | `+49.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.55` | 780,640.00 USD | 9,930.00 USD | 0.00 USD | `+50.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.65` | 793,960.00 USD | 13,320.00 USD | 0.00 USD | `+51.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.75` | 808,200.00 USD | 14,240.00 USD | 0.00 USD | `+52.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.85` | 892,550.00 USD | 84,360.00 USD | 0.00 USD | `+53.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 894,250.00 USD | 1,700.00 USD | 0.00 USD | `+54.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.05` | 906,740.00 USD | 12,500.00 USD | 0.00 USD | `+55.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.15` | 908,460.00 USD | 1,710.00 USD | 0.00 USD | `+56.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.25` | 910,760.00 USD | 2,300.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.35` | 1,010,000.00 USD | 98,330.00 USD | 0.00 USD | `+57.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.45` | 1,030,000.00 USD | 18,030.00 USD | 0.00 USD | `+58.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.55` | 1,030,000.00 USD | 4,390.00 USD | 0.00 USD | `+59.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.65` | 1,040,000.00 USD | 4,410.00 USD | 0.00 USD | `+60.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.75` | 1,040,000.00 USD | 4,440.00 USD | 0.00 USD | `+61.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.85` | 1,040,000.00 USD | 4,460.00 USD | 0.00 USD | `+62.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.95` | 1,050,000.00 USD | 448.75 USD | 0.00 USD | `+63.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.05` | 1,080,000.00 USD | 35,590.00 USD | 0.00 USD | `+64.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.15` | 1,080,000.00 USD | 453.75 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.25` | 1,080,000.00 USD | 830.38 USD | 0.00 USD | `+66.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.35` | 1,080,000.00 USD | 458.75 USD | 0.00 USD | `+67.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.45` | 1,080,000.00 USD | 461.25 USD | 0.00 USD | `+67.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.55` | 1,090,000.00 USD | 4,540.00 USD | 0.00 USD | `+68.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.65` | 1,090,000.00 USD | 466.25 USD | 0.00 USD | `+69.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.75` | 1,090,000.00 USD | 468.75 USD | 0.00 USD | `+70.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.85` | 1,090,000.00 USD | 471.25 USD | 0.00 USD | `+71.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `18.95` | 1,090,000.00 USD | 473.75 USD | 0.00 USD | `+72.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.05` | 1,160,000.00 USD | 67,000.00 USD | 0.00 USD | `+73.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.15` | 1,160,000.00 USD | 574.50 USD | 0.00 USD | `+74.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.25` | 1,160,000.00 USD | 577.50 USD | 0.00 USD | `+75.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.35` | 1,160,000.00 USD | 2,710.00 USD | 0.00 USD | `+76.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.45` | 1,160,000.00 USD | 972.50 USD | 0.00 USD | `+77.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.55` | 1,170,000.00 USD | 7,680.00 USD | 0.00 USD | `+77.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.65` | 1,170,000.00 USD | 1,680.00 USD | 0.00 USD | `+78.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.75` | 1,170,000.00 USD | 1,690.00 USD | 0.00 USD | `+79.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.85` | 1,170,000.00 USD | 992.50 USD | 0.00 USD | `+80.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `19.95` | 1,170,000.00 USD | 997.50 USD | 0.00 USD | `+81.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.05` | 2,790,000.00 USD | 1,610,000.00 USD | 0.00 USD | `+82.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.15` | 2,790,000.00 USD | 1,010.00 USD | 0.00 USD | `+83.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.25` | 2,790,000.00 USD | 1,010.00 USD | 0.00 USD | `+84.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.35` | 2,790,000.00 USD | 1,020.00 USD | 0.00 USD | `+85.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.45` | 2,790,000.00 USD | 1,020.00 USD | 0.00 USD | `+86.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.55` | 2,790,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.65` | 2,790,000.00 USD | 1,030.00 USD | 0.00 USD | `+87.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.75` | 2,800,000.00 USD | 1,860.00 USD | 0.00 USD | `+88.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.85` | 2,800,000.00 USD | 1,410.00 USD | 0.00 USD | `+89.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `20.95` | 2,800,000.00 USD | 1,050.00 USD | 0.00 USD | `+90.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.05` | 2,800,000.00 USD | 4,000.00 USD | 0.00 USD | `+91.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.15` | 2,800,000.00 USD | 1,060.00 USD | 0.00 USD | `+92.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.25` | 2,810,000.00 USD | 1,060.00 USD | 0.00 USD | `+93.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.35` | 3,850,000.00 USD | 1,050,000.00 USD | 0.00 USD | `+94.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.45` | 3,850,000.00 USD | 1,070.00 USD | 0.00 USD | `+95.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.55` | 3,850,000.00 USD | 1,080.00 USD | 0.00 USD | `+96.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.65` | 3,860,000.00 USD | 1,080.00 USD | 0.00 USD | `+97.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.75` | 3,860,000.00 USD | 1,090.00 USD | 0.00 USD | `+97.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.85` | 3,860,000.00 USD | 3,280.00 USD | 0.00 USD | `+98.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `21.95` | 3,860,000.00 USD | 1,100.00 USD | 0.00 USD | `+99.78%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `9.69` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 5,240.00 USD | 0.00 USD | 18.90 USD |
| `7D` | `9.71` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 8.80 USD |
| `7D` | `9.73` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 16,420.00 USD |
| `7D` | `9.75` | 7,360,000.00 USD | 0.00 USD | 7,360,000.00 USD | 0.00 USD | 33.95 USD | 16,970.00 USD |
| `7D` | `9.77` | 7,340,000.00 USD | 0.00 USD | 7,340,000.00 USD | 0.00 USD | 2,150.00 USD | 20,310.00 USD |
| `1D` | `9.86` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 0.00 USD | 142.30 USD | 10,300.00 USD |
| `7D` | `9.89` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 107.02 USD |
| `1D` | `9.90` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 17,040.00 USD | 7,240.00 USD | 0.00 USD |
| `1D` | `9.92` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 13,840.00 USD | 5,510.00 USD | 118.68 USD |
| `7D` | `9.93` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 10,090.00 USD | 12,060.00 USD |
| `1D` | `9.94` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 1,820.00 USD | 163.00 USD | 0.00 USD |
| `7D` | `9.95` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 14,920.00 USD | 10,650.00 USD | 13,780.00 USD |
| `1D` | `9.96` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 7,630.00 USD | 5,510.00 USD | 8,600.00 USD |
| `7D` | `9.97` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 0.00 USD | 370.70 USD | 0.00 USD |
| `1D` | `9.98` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 0.00 USD | 6,510.00 USD | 11,790.00 USD |
| `7D` | `9.99` | 7,260,000.00 USD | 0.00 USD | 7,260,000.00 USD | 0.00 USD | 0.00 USD | 13,100.00 USD |
| `1D` | `10.00` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 254.10 USD | 0.00 USD |
| `7D` | `10.01` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 0.00 USD | 317.30 USD | 0.00 USD |
| `1D` | `10.04` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 10,250.00 USD | 115.90 USD | 0.00 USD |
| `7D` | `10.05` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 154.66 USD |
| `1D` | `10.06` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 39.83 USD |
| `7D` | `10.07` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 0.00 USD | 351.10 USD | 0.00 USD |
| `7D` | `10.09` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 0.00 USD | 7,230.00 USD | 0.00 USD |
| `7D` | `10.11` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 279.85 USD | 0.00 USD | 5,980.00 USD |
| `1D` | `10.12` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 0.00 USD | 7,510.00 USD | 0.00 USD |
| `7D` | `10.13` | 7,230,000.00 USD | 0.00 USD | 7,230,000.00 USD | 27,980.00 USD | 10,860.00 USD | 18,110.00 USD |
| `1D` | `10.14` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 0.00 USD | 104.05 USD | 0.00 USD |
| `7D` | `10.15` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 32,930.00 USD | 8,310.00 USD | 14,460.00 USD |
| `1D` | `10.16` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 5,950.00 USD | 0.00 USD | 21.54 USD |
| `7D` | `10.17` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 56,890.00 USD | 3,240.00 USD | 21,610.00 USD |
| `1D` | `10.18` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 29.65 USD | 0.00 USD |
| `7D` | `10.19` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 10,880.00 USD | 9,020.00 USD | 34,710.00 USD |
| `1D` | `10.20` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 0.00 USD | 3,080.00 USD | 4,210.00 USD |
| `7D` | `10.21` | 6,980,000.00 USD | 0.00 USD | 6,980,000.00 USD | 42,540.00 USD | 15,950.00 USD | 51,400.00 USD |
| `1D` | `10.22` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 536.32 USD | 4,320.00 USD | 16,460.00 USD |
| `7D` | `10.23` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 150,290.00 USD | 35,270.00 USD | 118,210.00 USD |
| `1D` | `10.24` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 28,420.00 USD | 5,020.00 USD | 26,520.00 USD |
| `7D` | `10.25` | 6,570,000.00 USD | 0.00 USD | 6,570,000.00 USD | 52,490.00 USD | 15,200.00 USD | 49,810.00 USD |
| `1D` | `10.26` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 13,990.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `10.27` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 77,310.00 USD | 32,240.00 USD | 72,500.00 USD |
| `1D` | `10.28` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 26,250.00 USD | 9,320.00 USD | 10,080.00 USD |
| `7D` | `10.29` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 40,640.00 USD | 30,040.00 USD | 10,080.00 USD |
| `1D` | `10.30` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 6,030.00 USD | 1,030.00 USD | 10,880.00 USD |
| `7D` | `10.31` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 50,440.00 USD | 43,620.00 USD | 95,080.00 USD |
| `1D` | `10.32` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 28,010.00 USD | 12,850.00 USD | 11,710.00 USD |
| `7D` | `10.33` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 58,810.00 USD | 28,270.00 USD | 25,780.00 USD |
| `1D` | `10.34` | 2,900,000.00 USD | 0.00 USD | 2,900,000.00 USD | 30,770.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `10.35` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 30,630.00 USD | 26,030.00 USD | 8,890.00 USD |
| `1D` | `10.36` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 4,360.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `10.37` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 6,980.00 USD | 12,460.00 USD | 25,010.00 USD |
| `1D` | `10.38` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 7,450.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `10.39` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 4,240.00 USD | 6,160.00 USD | 63,790.00 USD |
| `1D` | `10.40` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 13,220.00 USD | 8,470.00 USD | 9,150.00 USD |
| `7D` | `10.41` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 60,840.00 USD | 28,080.00 USD | 52,950.00 USD |
| `1D` | `10.42` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 20,220.00 USD | 10,800.00 USD | 7,000.00 USD |
| `7D` | `10.43` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 32,710.00 USD | 22,700.00 USD | 15,270.00 USD |
| `1D` | `10.44` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `10.45` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 34,550.00 USD | 11,060.00 USD | 42,160.00 USD |
| `1D` | `10.46` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `10.47` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 53,010.00 USD | 22,760.00 USD | 6,560.00 USD |
| `1D` | `10.48` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 12,430.00 USD | 4,750.00 USD | 13,130.00 USD |
| `7D` | `10.49` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 22,510.00 USD | 183.20 USD | 24,920.00 USD |
| `1D` | `10.50` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 26,810.00 USD | 9,280.00 USD | 9,870.00 USD |
| `7D` | `10.51` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 58,340.00 USD | 18,130.00 USD | 13,760.00 USD |
| `1D` | `10.52` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 29,580.00 USD | 4,150.00 USD | 31,110.00 USD |
| `7D` | `10.53` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 13,040.00 USD | 6,560.00 USD | 21,130.00 USD |
| `1D` | `10.54` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 740.06 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `10.55` | 5,140,000.00 USD | 0.00 USD | 5,140,000.00 USD | 55,490.00 USD | 18,800.00 USD | 21,160.00 USD |
| `1D` | `10.56` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 58,790.00 USD | 23,780.00 USD | 1,810.00 USD |
| `7D` | `10.57` | 5,050,000.00 USD | 0.00 USD | 5,050,000.00 USD | 67,670.00 USD | 15,540.00 USD | 23,410.00 USD |
| `1D` | `10.58` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 37,820.00 USD | 16,800.00 USD | 21,000.00 USD |
| `7D` | `10.59` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 33,510.00 USD | 35,040.00 USD | 34,450.00 USD |
| `1D` | `10.60` | 2,350,000.00 USD | 0.00 USD | 2,350,000.00 USD | 15,350.00 USD | 5,500.00 USD | 3,180.00 USD |
| `7D` | `10.61` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 63,970.00 USD | 47,830.00 USD | 44,840.00 USD |
| `1D` | `10.62` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 41,350.00 USD | 12,840.00 USD | 46,730.00 USD |
| `7D` | `10.63` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 43,710.00 USD | 9,460.00 USD | 22,840.00 USD |
| `1D` | `10.64` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 13,350.00 USD | 20,950.00 USD | 12,940.00 USD |
| `7D` | `10.65` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 20,460.00 USD | 3,850.00 USD | 32,540.00 USD |
| `1D` | `10.66` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 48,910.00 USD | 16,150.00 USD | 34,150.00 USD |
| `7D` | `10.67` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 21,160.00 USD | 6,740.00 USD | 5,300.00 USD |
| `1D` | `10.68` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 17,480.00 USD | 3,750.00 USD | 1,550.00 USD |
| `7D` | `10.69` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 18,290.00 USD | 793.25 USD | 5,490.00 USD |
| `1D` | `10.70` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 37,930.00 USD | 9,600.00 USD | 11,070.00 USD |
| `7D` | `10.71` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 16,910.00 USD | 0.00 USD | 7,840.00 USD |
| `1D` | `10.72` | 1,990,000.00 USD | 0.00 USD | 1,990,000.00 USD | 7,920.00 USD | 3,150.00 USD | 7,370.00 USD |
| `7D` | `10.73` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 28,700.00 USD | 5,730.00 USD | 209.75 USD |
| `1D` | `10.74` | 1,970,000.00 USD | 0.00 USD | 1,970,000.00 USD | 12,810.00 USD | 6,780.00 USD | 57,630.00 USD |
| `7D` | `10.75` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 17,290.00 USD | 4,890.00 USD | 318.86 USD |
| `1D` | `10.76` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 12,370.00 USD | 4,090.00 USD | 2,640.00 USD |
| `7D` | `10.77` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 16,290.00 USD | 22,040.00 USD | 8,860.00 USD |
| `1D` | `10.78` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 86,290.00 USD | 57,540.00 USD | 57.12 USD |
| `7D` | `10.79` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 57,970.00 USD | 1,400.00 USD | 25,120.00 USD |
| `1D` | `10.80` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 73,580.00 USD | 27,960.00 USD | 25,730.00 USD |
| `7D` | `10.81` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 86,860.00 USD | 80,110.00 USD | 120,390.00 USD |
| `1D` | `10.82` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 30,650.00 USD | 1,080.00 USD | 68.68 USD |
| `7D` | `10.83` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 193,560.00 USD | 98,340.00 USD | 113,710.00 USD |
| `1D` | `10.84` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 54,340.00 USD | 15,320.00 USD | 69,300.00 USD |
| `7D` | `10.85` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 231,680.00 USD | 23,820.00 USD | 82,810.00 USD |
| `1D` | `10.86` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 976.86 USD | 30,860.00 USD | 3,820.00 USD |
| `7D` | `10.87` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 110,460.00 USD | 43,170.00 USD | 164,110.00 USD |
| `1D` | `10.88` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 64,750.00 USD | 42,700.00 USD | 82,790.00 USD |
| `7D` | `10.89` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 235,210.00 USD | 36,770.00 USD | 133,520.00 USD |
| `1D` | `10.90` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 23,940.00 USD | 4,880.00 USD | 0.39 USD |
| `7D` | `10.91` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 274,660.00 USD | 1,590.00 USD | 0.00 USD |
| `1D` | `10.92` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 97,980.00 USD | 43,900.00 USD | 22,140.00 USD |
| `7D` | `10.93` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 418,090.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.94` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 98,180.00 USD | 17,060.00 USD | 0.00 USD |
| `7D` | `10.95` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.96` | 902,260.00 USD | 0.00 USD | 902,260.00 USD | 96,940.00 USD | 23,010.00 USD | 0.00 USD |
| `7D` | `10.97` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 165,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `10.98` | 782,310.00 USD | 0.00 USD | 782,310.00 USD | 13,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `10.99` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 44,540.00 USD | 36,150.00 USD | 0.00 USD |
| `7D` | `11.01` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 10,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.02` | 768,980.00 USD | 0.00 USD | 768,980.00 USD | 0.00 USD | 37,550.00 USD | 0.00 USD |
| `7D` | `11.03` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.05` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 6,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.07` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 7,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.09` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 4,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.10` | 731,430.00 USD | 0.00 USD | 731,430.00 USD | 0.00 USD | 0.00 USD | 106.40 USD |
| `7D` | `11.11` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 5,790.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.12` | 731,330.00 USD | 0.00 USD | 731,330.00 USD | 632.30 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.13` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 6,820.00 USD | 162,470.00 USD | 0.00 USD |
| `1D` | `11.14` | 730,700.00 USD | 0.00 USD | 730,700.00 USD | 1,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.15` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 2,410.00 USD | 123,230.00 USD | 0.00 USD |
| `1D` | `11.16` | 728,800.00 USD | 0.00 USD | 728,800.00 USD | 337.20 USD | 27,640.00 USD | 0.00 USD |
| `7D` | `11.17` | 933,220.00 USD | 0.00 USD | 933,220.00 USD | 3,970.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.18` | 700,820.00 USD | 0.00 USD | 700,820.00 USD | 0.00 USD | 47,740.00 USD | 0.00 USD |
| `7D` | `11.19` | 929,250.00 USD | 0.00 USD | 929,250.00 USD | 4,050.00 USD | 0.00 USD | 63,370.00 USD |
| `1D` | `11.20` | 653,080.00 USD | 0.00 USD | 653,080.00 USD | 43,350.00 USD | 39,010.00 USD | 98,690.00 USD |
| `7D` | `11.21` | 861,830.00 USD | 0.00 USD | 861,830.00 USD | 319,760.00 USD | 0.00 USD | 282,230.00 USD |
| `1D` | `11.22` | 472,040.00 USD | 0.00 USD | 472,040.00 USD | 262,690.00 USD | 587.72 USD | 43,050.00 USD |
| `7D` | `11.23` | 259,840.00 USD | 0.00 USD | 259,840.00 USD | 201,470.00 USD | 0.00 USD | 58,370.00 USD |
| `1D` | `11.24` | 165,710.00 USD | 0.00 USD | 165,710.00 USD | 69,220.00 USD | 399.60 USD | 96,090.00 USD |
| `7D` | `11.24` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.25` | 495,720.00 USD | 495,720.00 USD | 0.00 USD | 332,220.00 USD | 2,180.00 USD | 161,310.00 USD |
| `1D` | `11.26` | 99,790.00 USD | 99,790.00 USD | 0.00 USD | 28,620.00 USD | 815.00 USD | 70,350.00 USD |
| `1D` | `11.26` | 199,580.00 USD | 199,580.00 USD | 0.00 USD | 28,620.00 USD | 815.00 USD | 70,350.00 USD |
| `7D` | `11.27` | 943,160.00 USD | 943,160.00 USD | 0.00 USD | 256,120.00 USD | 0.00 USD | 191,320.00 USD |
| `1D` | `11.28` | 443,040.00 USD | 443,040.00 USD | 0.00 USD | 38,150.00 USD | 18,580.00 USD | 186,730.00 USD |
| `7D` | `11.29` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 104,970.00 USD | 0.00 USD | 55,980.00 USD |
| `1D` | `11.30` | 545,480.00 USD | 545,480.00 USD | 0.00 USD | 0.00 USD | 60,470.00 USD | 41,980.00 USD |
| `7D` | `11.31` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 28,170.00 USD | 43,020.00 USD | 236,970.00 USD |
| `1D` | `11.32` | 734,070.00 USD | 734,070.00 USD | 0.00 USD | 63,250.00 USD | 66,390.00 USD | 58,940.00 USD |
| `7D` | `11.33` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 54,410.00 USD | 8,920.00 USD | 18,940.00 USD |
| `1D` | `11.34` | 987,060.00 USD | 987,060.00 USD | 0.00 USD | 197,970.00 USD | 55,020.00 USD | 0.00 USD |
| `7D` | `11.35` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 60,280.00 USD | 0.00 USD |
| `1D` | `11.36` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 98,460.00 USD | 22,140.00 USD |
| `7D` | `11.37` | 1,700,000.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 50,580.00 USD | 99,100.00 USD |
| `1D` | `11.38` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 51,260.00 USD | 55,490.00 USD | 0.00 USD |
| `7D` | `11.39` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 20,400.00 USD | 16,820.00 USD |
| `1D` | `11.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 24,030.00 USD | 65,480.00 USD |
| `7D` | `11.41` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 16,010.00 USD | 34,700.00 USD |
| `1D` | `11.42` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 106,690.00 USD | 45,130.00 USD | 78,840.00 USD |
| `7D` | `11.43` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 133,220.00 USD | 65,620.00 USD | 55,710.00 USD |
| `1D` | `11.44` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 42,610.00 USD | 18,500.00 USD | 52,860.00 USD |
| `7D` | `11.45` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 177,620.00 USD | 38,970.00 USD | 37,930.00 USD |
| `1D` | `11.46` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 34,610.00 USD | 51,530.00 USD | 12,800.00 USD |
| `7D` | `11.47` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 17,370.00 USD | 39,960.00 USD | 30,160.00 USD |
| `1D` | `11.48` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 14,310.00 USD | 4,700.00 USD | 0.00 USD |
| `7D` | `11.49` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 37,290.00 USD | 70,390.00 USD | 34,450.00 USD |
| `1D` | `11.50` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 19,080.00 USD | 19,160.00 USD | 34,640.00 USD |
| `7D` | `11.51` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 40,840.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.52` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 29,340.00 USD | 13,170.00 USD | 418.82 USD |
| `7D` | `11.53` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 48,860.00 USD | 5,190.00 USD | 32,690.00 USD |
| `1D` | `11.54` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 31,460.00 USD | 16,150.00 USD | 29,470.00 USD |
| `1D` | `11.56` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 64,190.00 USD | 635.25 USD | 15,160.00 USD |
| `7D` | `11.57` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 793.25 USD | 31,620.00 USD |
| `1D` | `11.58` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 45,400.00 USD | 335.85 USD | 17,790.00 USD |
| `7D` | `11.59` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 22,780.00 USD |
| `1D` | `11.60` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 124,870.00 USD | 7,320.00 USD | 67,340.00 USD |
| `7D` | `11.61` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 44,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.62` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 42,200.00 USD | 0.00 USD | 34,290.00 USD |
| `7D` | `11.63` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 34,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `11.65` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 877.75 USD | 306.68 USD |
| `7D` | `11.67` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 22,340.00 USD | 61,970.00 USD |
| `1D` | `11.68` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 59,600.00 USD | 28,810.00 USD | 0.00 USD |
| `7D` | `11.69` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 381.10 USD | 0.00 USD |
| `1D` | `11.70` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 313.96 USD |
| `7D` | `11.71` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 146,640.00 USD | 0.00 USD | 49,310.00 USD |
| `1D` | `11.72` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 222,070.00 USD | 13,260.00 USD | 19,780.00 USD |
| `7D` | `11.73` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 21,220.00 USD |
| `1D` | `11.74` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 35,580.00 USD | 17,540.00 USD | 73,090.00 USD |
| `7D` | `11.75` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 17,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.76` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 24,330.00 USD | 14,970.00 USD | 10,450.00 USD |
| `7D` | `11.77` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 30,810.00 USD | 27,570.00 USD | 76,870.00 USD |
| `1D` | `11.78` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 18,910.00 USD | 18,740.00 USD | 39,930.00 USD |
| `7D` | `11.79` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.80` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 14,340.00 USD | 394.16 USD |
| `7D` | `11.81` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 164,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `11.82` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 11,070.00 USD | 0.00 USD | 18,420.00 USD |
| `7D` | `11.83` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 81,180.00 USD | 45,270.00 USD | 229.90 USD |
| `1D` | `11.84` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 76,470.00 USD | 11,830.00 USD | 44,350.00 USD |
| `7D` | `11.85` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 178,690.00 USD | 39,240.00 USD | 90.06 USD |
| `1D` | `11.86` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 232.40 USD | 33,990.00 USD | 37,980.00 USD |
| `7D` | `11.87` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 438.10 USD | 4,980.00 USD | 23,210.00 USD |
| `1D` | `11.88` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 19,640.00 USD | 25,990.00 USD | 45,870.00 USD |
| `7D` | `11.89` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 40,020.00 USD | 16,380.00 USD | 71.80 USD |
| `1D` | `11.90` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 44,160.00 USD | 8,750.00 USD | 13,110.00 USD |
| `7D` | `11.91` | 4,000,000.00 USD | 4,000,000.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | 397.61 USD |
| `1D` | `11.92` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 133,700.00 USD | 22,470.00 USD | 11,970.00 USD |
| `7D` | `11.93` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 18,580.00 USD | 15,510.00 USD | 38,820.00 USD |
| `1D` | `11.94` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 18,740.00 USD | 15,450.00 USD | 28,550.00 USD |
| `7D` | `11.95` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 6,130.00 USD | 23,810.00 USD | 209,090.00 USD |
| `1D` | `11.96` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 40,140.00 USD | 33,530.00 USD | 38,010.00 USD |
| `7D` | `11.97` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 354,730.00 USD | 35,140.00 USD | 223,430.00 USD |
| `1D` | `11.98` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 39,010.00 USD | 23,470.00 USD | 98,270.00 USD |
| `7D` | `11.99` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 242,400.00 USD | 17,110.00 USD | 130,130.00 USD |
| `1D` | `12.00` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 65,840.00 USD | 9,300.00 USD | 30,800.00 USD |
| `7D` | `12.01` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 164,140.00 USD | 5,360.00 USD | 247,680.00 USD |
| `1D` | `12.02` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 42,950.00 USD | 27,660.00 USD | 31,440.00 USD |
| `7D` | `12.03` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 321,170.00 USD | 140,540.00 USD | 192,600.00 USD |
| `1D` | `12.04` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 209,440.00 USD | 65,620.00 USD | 97,900.00 USD |
| `7D` | `12.05` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 333,260.00 USD | 125,990.00 USD | 188,430.00 USD |
| `1D` | `12.06` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 187,660.00 USD | 88,160.00 USD | 147,980.00 USD |
| `7D` | `12.07` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 278,510.00 USD | 90,210.00 USD | 204,280.00 USD |
| `1D` | `12.08` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 123,260.00 USD | 30,500.00 USD | 52,780.00 USD |
| `7D` | `12.09` | 7,900,000.00 USD | 7,900,000.00 USD | 0.00 USD | 167,080.00 USD | 75,220.00 USD | 50,380.00 USD |
| `1D` | `12.10` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 36,180.00 USD | 16,940.00 USD | 22,460.00 USD |
| `7D` | `12.11` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 84,910.00 USD | 74,760.00 USD | 111,260.00 USD |
| `1D` | `12.12` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 138,630.00 USD | 60,020.00 USD | 63,050.00 USD |
| `7D` | `12.13` | 8,440,000.00 USD | 8,440,000.00 USD | 0.00 USD | 148,530.00 USD | 73,120.00 USD | 48,150.00 USD |
| `1D` | `12.14` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 92,340.00 USD | 33,200.00 USD | 55,720.00 USD |
| `7D` | `12.15` | 9,040,000.00 USD | 9,040,000.00 USD | 0.00 USD | 325,540.00 USD | 125,190.00 USD | 145,370.00 USD |
| `1D` | `12.16` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 126,410.00 USD | 37,730.00 USD | 67,630.00 USD |
| `7D` | `12.17` | 9,180,000.00 USD | 9,180,000.00 USD | 0.00 USD | 26,820.00 USD | 61,400.00 USD | 53,310.00 USD |
| `1D` | `12.18` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 112,590.00 USD | 42,390.00 USD | 33,670.00 USD |
| `7D` | `12.19` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 196,200.00 USD | 58,580.00 USD | 79,450.00 USD |
| `1D` | `12.20` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 77,890.00 USD | 43,590.00 USD | 31,800.00 USD |
| `7D` | `12.21` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 200,760.00 USD | 62,900.00 USD | 128,560.00 USD |
| `1D` | `12.22` | 6,250,000.00 USD | 6,250,000.00 USD | 0.00 USD | 12,890.00 USD | 16,780.00 USD | 28,210.00 USD |
| `7D` | `12.23` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 140,270.00 USD | 19,720.00 USD | 57,540.00 USD |
| `1D` | `12.24` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 9,250.00 USD | 14,730.00 USD | 7,780.00 USD |
| `7D` | `12.25` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 136,810.00 USD | 56,100.00 USD | 102,920.00 USD |
| `1D` | `12.26` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 43,220.00 USD | 22,010.00 USD | 21,450.00 USD |
| `7D` | `12.27` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 118,980.00 USD | 49,260.00 USD | 64,060.00 USD |
| `1D` | `12.28` | 6,510,000.00 USD | 6,510,000.00 USD | 0.00 USD | 83,960.00 USD | 17,410.00 USD | 37,620.00 USD |
| `7D` | `12.29` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 235,780.00 USD | 105,510.00 USD | 175,310.00 USD |
| `1D` | `12.30` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 57,170.00 USD | 16,300.00 USD | 36,460.00 USD |
| `7D` | `12.31` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 135,150.00 USD | 53,830.00 USD | 55,040.00 USD |
| `1D` | `12.32` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 1,610.00 USD | 7,100.00 USD | 79.72 USD |
| `7D` | `12.33` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 165,330.00 USD | 96,930.00 USD | 5,470.00 USD |
| `1D` | `12.34` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 20,380.00 USD | 8,560.00 USD | 12,700.00 USD |
| `7D` | `12.35` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 116,830.00 USD | 9,820.00 USD | 19,280.00 USD |
| `1D` | `12.36` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 19,360.00 USD | 16,550.00 USD | 5,460.00 USD |
| `7D` | `12.37` | 11,900,000.00 USD | 11,900,000.00 USD | 0.00 USD | 32,750.00 USD | 24,960.00 USD | 12,900.00 USD |
| `1D` | `12.38` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 20,670.00 USD | 6,420.00 USD | 12,550.00 USD |
| `7D` | `12.39` | 12,440,000.00 USD | 12,440,000.00 USD | 0.00 USD | 160,660.00 USD | 42,040.00 USD | 338,190.00 USD |
| `1D` | `12.40` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 18,820.00 USD | 12,140.00 USD | 22,850.00 USD |
| `7D` | `12.41` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 80,100.00 USD | 25,020.00 USD | 113,860.00 USD |
| `1D` | `12.42` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 57,750.00 USD | 13,980.00 USD | 9,730.00 USD |
| `7D` | `12.43` | 13,250,000.00 USD | 13,250,000.00 USD | 0.00 USD | 237,780.00 USD | 22,230.00 USD | 334,320.00 USD |
| `1D` | `12.44` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 17,720.00 USD | 10,270.00 USD | 6,510.00 USD |
| `7D` | `12.45` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 57,130.00 USD | 99,050.00 USD | 258,810.00 USD |
| `1D` | `12.46` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 269.21 USD | 9,440.00 USD | 4,210.00 USD |
| `7D` | `12.47` | 13,840,000.00 USD | 13,840,000.00 USD | 0.00 USD | 66,870.00 USD | 29,080.00 USD | 75,590.00 USD |
| `1D` | `12.48` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 1,620.00 USD | 2,560.00 USD | 8,350.00 USD |
| `7D` | `12.49` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 91,900.00 USD | 17,730.00 USD | 60,380.00 USD |
| `1D` | `12.50` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 656.89 USD | 4,320.00 USD | 8,270.00 USD |
| `7D` | `12.51` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 133,990.00 USD | 26,650.00 USD | 85,850.00 USD |
| `1D` | `12.52` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 29,950.00 USD | 5,020.00 USD | 26,240.00 USD |
| `7D` | `12.53` | 14,560,000.00 USD | 14,560,000.00 USD | 0.00 USD | 131,510.00 USD | 50,370.00 USD | 128,240.00 USD |
| `1D` | `12.54` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 14,620.00 USD | 2,830.00 USD | 20.72 USD |
| `7D` | `12.55` | 14,810,000.00 USD | 14,810,000.00 USD | 0.00 USD | 115,090.00 USD | 45,060.00 USD | 82,010.00 USD |
| `1D` | `12.56` | 7,080,000.00 USD | 7,080,000.00 USD | 0.00 USD | 26,250.00 USD | 9,320.00 USD | 9,990.00 USD |
| `7D` | `12.57` | 15,000,000.00 USD | 15,000,000.00 USD | 0.00 USD | 118,650.00 USD | 65,650.00 USD | 10,850.00 USD |
| `1D` | `12.58` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 6,910.00 USD | 1,030.00 USD | 10,960.00 USD |
| `7D` | `12.59` | 15,120,000.00 USD | 15,120,000.00 USD | 0.00 USD | 65,910.00 USD | 14,350.00 USD | 36,480.00 USD |
| `1D` | `12.60` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 15,910.00 USD | 3,320.00 USD | 1,090.00 USD |
| `7D` | `12.61` | 15,250,000.00 USD | 15,250,000.00 USD | 0.00 USD | 41,220.00 USD | 29,650.00 USD | 58,880.00 USD |
| `1D` | `12.62` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 13,530.00 USD | 9,530.00 USD | 10,230.00 USD |
| `7D` | `12.63` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 64,120.00 USD | 28,270.00 USD | 81,370.00 USD |
| `1D` | `12.64` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 31,180.00 USD | 4,260.00 USD | 11,530.00 USD |
| `7D` | `12.65` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 76,240.00 USD | 26,110.00 USD | 90,700.00 USD |
| `1D` | `12.66` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 4,470.00 USD | 3,450.00 USD | 17,890.00 USD |
| `7D` | `12.67` | 15,920,000.00 USD | 15,920,000.00 USD | 0.00 USD | 65,670.00 USD | 16,240.00 USD | 223,860.00 USD |
| `1D` | `12.68` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 8,540.00 USD | 4,400.00 USD | 7,150.00 USD |
| `7D` | `12.69` | 16,160,000.00 USD | 16,160,000.00 USD | 0.00 USD | 44,600.00 USD | 30,290.00 USD | 165,350.00 USD |
| `1D` | `12.70` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 0.00 USD | 4,720.00 USD | 2,780.00 USD |
| `7D` | `12.71` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 31,960.00 USD | 43,220.00 USD | 24,430.00 USD |
| `1D` | `12.72` | 7,280,000.00 USD | 7,280,000.00 USD | 0.00 USD | 13,460.00 USD | 3,750.00 USD | 6,470.00 USD |
| `7D` | `12.73` | 16,350,000.00 USD | 16,350,000.00 USD | 0.00 USD | 54,040.00 USD | 11,090.00 USD | 28,320.00 USD |
| `1D` | `12.74` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 20,500.00 USD | 10,800.00 USD | 6,520.00 USD |
| `7D` | `12.75` | 16,420,000.00 USD | 16,420,000.00 USD | 0.00 USD | 33,190.00 USD | 22,700.00 USD | 14,980.00 USD |
| `1D` | `12.76` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 39,130.00 USD | 13,230.00 USD | 16,280.00 USD |
| `7D` | `12.77` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 34,550.00 USD | 11,060.00 USD | 42,330.00 USD |
| `1D` | `12.78` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 9,440.00 USD | 3,120.00 USD | 6,000.00 USD |
| `7D` | `12.79` | 16,600,000.00 USD | 16,600,000.00 USD | 0.00 USD | 55,160.00 USD | 22,760.00 USD | 6,590.00 USD |
| `1D` | `12.80` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 12,430.00 USD | 4,750.00 USD | 12,890.00 USD |
| `7D` | `12.81` | 16,620,000.00 USD | 16,620,000.00 USD | 0.00 USD | 7,760.00 USD | 0.00 USD | 19,920.00 USD |
| `1D` | `12.82` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 2,680.00 USD | 3,450.00 USD | 3,600.00 USD |
| `7D` | `12.83` | 16,650,000.00 USD | 16,650,000.00 USD | 0.00 USD | 15,730.00 USD | 183.20 USD | 5,000.00 USD |
| `1D` | `12.84` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 20,500.00 USD | 5,830.00 USD | 6,190.00 USD |
| `7D` | `12.85` | 16,730,000.00 USD | 16,730,000.00 USD | 0.00 USD | 56,660.00 USD | 18,130.00 USD | 13,710.00 USD |
| `1D` | `12.86` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 27,750.00 USD | 3,790.00 USD | 5,430.00 USD |
| `7D` | `12.87` | 16,770,000.00 USD | 16,770,000.00 USD | 0.00 USD | 9,820.00 USD | 6,560.00 USD | 21,060.00 USD |
| `1D` | `12.88` | 7,520,000.00 USD | 7,520,000.00 USD | 0.00 USD | 116.15 USD | 2,310.00 USD | 4,590.00 USD |
| `7D` | `12.89` | 16,860,000.00 USD | 16,860,000.00 USD | 0.00 USD | 48,720.00 USD | 18,800.00 USD | 20,700.00 USD |
| `1D` | `12.90` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 15,310.00 USD | 5,660.00 USD | 1,810.00 USD |
| `7D` | `12.91` | 16,960,000.00 USD | 16,960,000.00 USD | 0.00 USD | 59,260.00 USD | 15,540.00 USD | 23,330.00 USD |
| `1D` | `12.92` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 57.17 USD | 1,530.00 USD | 8,190.00 USD |
| `7D` | `12.93` | 16,980,000.00 USD | 16,980,000.00 USD | 0.00 USD | 26,330.00 USD | 231.70 USD | 16.88 USD |
| `1D` | `12.94` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 2,650.00 USD | 1,290.00 USD | 0.00 USD |
| `7D` | `12.95` | 17,000,000.00 USD | 17,000,000.00 USD | 0.00 USD | 1,920.00 USD | 9,210.00 USD | 4,200.00 USD |
| `1D` | `12.96` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 227.00 USD | 5,090.00 USD | 3,110.00 USD |
| `7D` | `12.97` | 17,030,000.00 USD | 17,030,000.00 USD | 0.00 USD | 13,890.00 USD | 10,560.00 USD | 10,050.00 USD |
| `1D` | `12.98` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 21,360.00 USD | 5,250.00 USD | 11,950.00 USD |
| `7D` | `12.99` | 17,100,000.00 USD | 17,100,000.00 USD | 0.00 USD | 38,730.00 USD | 9,460.00 USD | 22,600.00 USD |
| `1D` | `13.00` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 11,890.00 USD | 7,680.00 USD | 12,890.00 USD |
| `7D` | `13.01` | 17,110,000.00 USD | 17,110,000.00 USD | 0.00 USD | 1,290.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `13.03` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 267.65 USD | 3,370.00 USD | 5,130.00 USD |
| `7D` | `13.05` | 17,120,000.00 USD | 17,120,000.00 USD | 0.00 USD | 303.50 USD | 3,370.00 USD | 0.00 USD |
| `7D` | `13.07` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 5,250.00 USD |
| `7D` | `13.09` | 17,130,000.00 USD | 17,130,000.00 USD | 0.00 USD | 140.23 USD | 0.00 USD | 7,600.00 USD |
| `7D` | `13.11` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 19,270.00 USD | 5,730.00 USD | 20.43 USD |
| `7D` | `13.13` | 17,160,000.00 USD | 17,160,000.00 USD | 0.00 USD | 321.45 USD | 4,010.00 USD | 0.00 USD |
| `7D` | `13.17` | 17,180,000.00 USD | 17,180,000.00 USD | 0.00 USD | 0.00 USD | 3,960.00 USD | 8,430.00 USD |
| `7D` | `13.19` | 17,190,000.00 USD | 17,190,000.00 USD | 0.00 USD | 972.55 USD | 0.00 USD | 9,710.00 USD |
| `7D` | `13.21` | 17,210,000.00 USD | 17,210,000.00 USD | 0.00 USD | 13,890.00 USD | 213.60 USD | 8,930.00 USD |
| `7D` | `13.23` | 17,220,000.00 USD | 17,220,000.00 USD | 0.00 USD | 10,840.00 USD | 146.97 USD | 22.55 USD |
| `7D` | `13.25` | 17,290,000.00 USD | 17,290,000.00 USD | 0.00 USD | 25,480.00 USD | 14,870.00 USD | 24,510.00 USD |
| `7D` | `13.27` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 10,290.00 USD | 8,420.00 USD | 10,920.00 USD |
| `7D` | `13.29` | 17,320,000.00 USD | 17,320,000.00 USD | 0.00 USD | 6,180.00 USD | 2,560.00 USD | 0.00 USD |
| `7D` | `13.31` | 17,350,000.00 USD | 17,350,000.00 USD | 0.00 USD | 12,560.00 USD | 6,580.00 USD | 6,470.00 USD |
| `7D` | `13.33` | 17,360,000.00 USD | 17,360,000.00 USD | 0.00 USD | 9,030.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `533.53M` | Total OI Tokens: `47,386,277.9 LINK`
  * 1h OI Change: `-2.70%` | 4h OI Change: `-5.45%` | 24h OI Change: `-7.12%`
  * Exchange Breakdown: Binance=`101.24M` | Bybit=`63.03M` | OKX=`26.08M` | Hyperliquid=`51.65M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `3.30K` | Last 24h: `44.37K` | Last 3d: `101.04K` | Last 7d: `164.04K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0021%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0025%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0022%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0033%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0089%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LINK` | `47.39%` | `52.61%` | `0.90` | 23,320,000.00 USD |
| `15M` | `Binance` | `44.29%` | `55.71%` | `0.80` | 7,930,000.00 USD |
| `15M` | `OKX` | `49.99%` | `50.01%` | `1.00` | 2,160,000.00 USD |
| `15M` | `Bybit` | `37.61%` | `62.39%` | `0.60` | 2,100,000.00 USD |
| `15M` | `KuCoin` | `53.37%` | `46.63%` | `1.14` | 112,290.00 USD |
| `15M` | `Gate` | `61.62%` | `38.38%` | `1.61` | 450,810.00 USD |
| `15M` | `Bitget` | `49.71%` | `50.29%` | `0.99` | 500,610.00 USD |
| `15M` | `BingX` | `28.27%` | `71.73%` | `0.39` | 609,740.00 USD |
| `15M` | `MEXC` | `51.31%` | `48.69%` | `1.05` | 4,750,000.00 USD |
| `15M` | `Bitunix` | `41.68%` | `58.32%` | `0.71` | 907,710.00 USD |
| `15M` | `Hyperliquid` | `48.13%` | `51.87%` | `0.93` | 2,160,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.3%` | `48.7%` | `1.05` | 806,740.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `97.8%` | `2.2%` | `44.45` | 523,440.00 USD |
| `15M` | `HTX` | `55.37%` | `44.63%` | `1.24` | 10,780.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.19%` | `73.81%` | `0.35` | 199,900.00 USD |
| `15M` | `Aster` | `71.75%` | `28.25%` | `2.54` | 49,760.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `69.23%` | `30.77%` | `2.25` | 54,880.00 USD |
| `15M` | `Whale Positions` | `44.29%` | `55.71%` | `0.80` | 7,930,000.00 USD |
| `15M` | `Global Accounts` | `47.39%` | `52.61%` | `0.90` | 23,320,000.00 USD |
| `1H` | `LINK` | `46.12%` | `53.88%` | `0.86` | 95,400,000.00 USD |
| `1H` | `Binance` | `44.63%` | `55.37%` | `0.81` | 37,840,000.00 USD |
| `1H` | `OKX` | `49.78%` | `50.22%` | `0.99` | 9,980,000.00 USD |
| `1H` | `Bybit` | `42%` | `58%` | `0.72` | 15,570,000.00 USD |
| `1H` | `KuCoin` | `50.57%` | `49.43%` | `1.02` | 495,810.00 USD |
| `1H` | `Gate` | `48.55%` | `51.45%` | `0.94` | 4,040,000.00 USD |
| `1H` | `Bitget` | `45.52%` | `54.48%` | `0.84` | 2,860,000.00 USD |
| `1H` | `BingX` | `45.04%` | `54.96%` | `0.82` | 3,880,000.00 USD |
| `1H` | `MEXC` | `50.12%` | `49.88%` | `1.00` | 1,250,000.00 USD |
| `1H` | `Bitunix` | `44.53%` | `55.47%` | `0.80` | 1,830,000.00 USD |
| `1H` | `Hyperliquid` | `42.74%` | `57.26%` | `0.75` | 6,160,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `56.2%` | `43.8%` | `1.28` | 3,740,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `39.71%` | `60.29%` | `0.66` | 6,320,000.00 USD |
| `1H` | `HTX` | `42%` | `58%` | `0.72` | 296,070.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `45.47%` | `54.53%` | `0.83` | 838,070.00 USD |
| `1H` | `Aster` | `55.35%` | `44.65%` | `1.24` | 110,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `33.85%` | `66.15%` | `0.51` | 181,110.00 USD |
| `1H` | `Whale Positions` | `44.63%` | `55.37%` | `0.81` | 37,840,000.00 USD |
| `1H` | `Global Accounts` | `46.12%` | `53.88%` | `0.86` | 95,400,000.00 USD |
| `4H` | `LINK` | `50.11%` | `49.89%` | `1.00` | 108,800,000.00 USD |
| `4H` | `Binance` | `49.71%` | `50.29%` | `0.99` | 42,660,000.00 USD |
| `4H` | `OKX` | `53.54%` | `46.46%` | `1.15` | 10,910,000.00 USD |
| `4H` | `Bybit` | `55.4%` | `44.6%` | `1.24` | 16,700,000.00 USD |
| `4H` | `KuCoin` | `59.69%` | `40.31%` | `1.48` | 693,920.00 USD |
| `4H` | `Gate` | `48.69%` | `51.31%` | `0.95` | 5,010,000.00 USD |
| `4H` | `Bitget` | `57.77%` | `42.23%` | `1.37` | 3,080,000.00 USD |
| `4H` | `BingX` | `30.72%` | `69.28%` | `0.44` | 4,560,000.00 USD |
| `4H` | `MEXC` | `41.13%` | `58.87%` | `0.70` | 1,440,000.00 USD |
| `4H` | `Bitunix` | `51%` | `49%` | `1.04` | 1,960,000.00 USD |
| `4H` | `Hyperliquid` | `63.76%` | `36.24%` | `1.76` | 6,410,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.05%` | `50.95%` | `0.96` | 5,520,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `32.87%` | `67.13%` | `0.49` | 8,090,000.00 USD |
| `4H` | `HTX` | `56.84%` | `43.16%` | `1.32` | 453,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `72.79%` | `27.21%` | `2.68` | 912,330.00 USD |
| `4H` | `Aster` | `45.12%` | `54.88%` | `0.82` | 117,510.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `57.35%` | `42.65%` | `1.34` | 260,980.00 USD |
| `4H` | `Whale Positions` | `49.71%` | `50.29%` | `0.99` | 42,660,000.00 USD |
| `4H` | `Global Accounts` | `50.11%` | `49.89%` | `1.00` | 108,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `11.64` | `11.65` | `11.64` | `11.69` | `11.64` | 859,560.77 USD | 300,851.02 USD | 558,709.75 USD | -257,858.72 USD | `-30.00%` | `5B / 13S` |
| `5:00 UTC` | `11.68` | `11.66` | `11.68` | `11.68` | `11.63` | 997,243.09 USD | 360,139.33 USD | 637,103.76 USD | -276,964.43 USD | `-27.77%` | `11B / 15S` |
| `0:00 UTC` | `11.72` | `11.71` | `11.72` | `11.73` | `11.68` | 1,229,457.09 USD | 722,946.86 USD | 506,510.23 USD | 216,436.63 USD | `+17.60%` | `13B / 6S` |
| `5:00 UTC` | `11.70` | `11.70` | `11.70` | `11.72` | `11.68` | 638,959.31 USD | 356,011.33 USD | 282,947.98 USD | 73,063.35 USD | `+11.43%` | `5B / 5S` |
| `0:00 UTC` | `11.53` | `11.52` | `11.53` | `11.69` | `11.42` | 7,042,914.29 USD | 3,385,099.97 USD | 3,657,814.32 USD | -272,714.35 USD | `-3.87%` | `7B / 36S` |
| `5:00 UTC` | `11.53` | `11.53` | `11.53` | `11.57` | `11.50` | 1,919,098.80 USD | 908,695.92 USD | 1,010,402.88 USD | -101,706.95 USD | `-5.30%` | `5B / 9S` |
| `0:00 UTC` | `11.13` | `11.25` | `11.13` | `11.55` | `11.03` | 15,867,227.37 USD | 6,488,166.63 USD | 9,379,060.74 USD | -2,890,894.11 USD | `-18.22%` | `4B / 29S` |
| `5:00 UTC` | `11.00` | `11.03` | `11.00` | `11.19` | `10.87` | 17,839,722.17 USD | 8,415,517.99 USD | 9,424,204.18 USD | -1,008,686.19 USD | `-5.65%` | `9B / 18S` |
| `0:00 UTC` | `11.11` | `11.06` | `11.11` | `11.18` | `10.95` | 10,677,747.31 USD | 5,105,845.59 USD | 5,571,901.72 USD | -466,056.13 USD | `-4.36%` | `1B / 2S` |
| `5:00 UTC` | `11.27` | `11.23` | `11.27` | `11.30` | `11.15` | 3,716,788.65 USD | 1,633,287.55 USD | 2,083,501.10 USD | -450,213.55 USD | `-12.11%` | `9B / 33S` |

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
| `5m` | -137,750.00 USD | -73,400.00 USD | **`DISTRIBUTION`** |
| `15m` | -329,050.00 USD | -1,190,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -2,250,000.00 USD | -1,410,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -4,360,000.00 USD | -8,010,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,690,000.00 USD | -8,370,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -5,330,000.00 USD | -9,650,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,990,000.00 USD | -11,160,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,620,000.00 USD | -9,820,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,510,000.00 USD | -9,460,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -4,910,000.00 USD | -14,700,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,510,000.00 USD | -32,970,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -73,580,000.00 USD | -195,110,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-137.75K` | 15m=`-329.05K` | 1h=`-4.36M` | 24h=`-4.91M`
* Futures Capital Netflows: 5m=`-73.40K` | 15m=`-1.19M` | 1h=`-8.01M` | 24h=`-14.70M`
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
  * `2026-10-30 02:15:01 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:51:01 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:50:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:52:01 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:52:01 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:52:01 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `11.04` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `10.74` (Risk Distance: `0.2972` pts)
  * +2.5R Take Profit: `11.78`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `11.24` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `11.54` (Risk Distance: `0.2972` pts)
  * +2.5R Take Profit: `10.50`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`11.31`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
