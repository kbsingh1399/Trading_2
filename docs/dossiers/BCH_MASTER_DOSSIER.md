# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 01:51:14 IST` (`2026-10-29 20:21:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `282.26` | **Live Ask Quote**: `282.94` | **Mid Price**: `282.60`
- **Spread Points**: `680.00` | **Spread BPS**: `24.06 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `282.88` | VWAP Z-Score: `+0.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.07` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `52.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.46` | Lower -3.00σ Band: `270.31`
  * Upper +2.51σ Band: `293.41` | Lower -2.51σ Band: `272.36`
  * Upper +2.01σ Band: `291.31` | Lower -2.01σ Band: `274.46`
  * Upper +2.00σ Band: `291.27` | Lower -2.00σ Band: `274.50`
  * Upper +1.28σ Band: `288.25` | Lower -1.28σ Band: `277.52`
  * Upper +1.00σ Band: `287.08` | Lower -1.00σ Band: `278.69`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`287.22` | EMA-20=`286.42` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`284.37` (Slope: `+0.0000`) | EMA-100=`284.52`
  * Institutional Anchors: EMA-144=`284.86` | EMA-200=`284.85` (Slope: `+0.1335`) | EMA-233=`285.16`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.56` (Distance: `-1.73%`)
  * Point of Control (POC) = `278.70` (Distance: `+1.40%`)
  * Value Area Low (VAL) = `276.88` (Distance: `+2.06%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`299.16` | POC=`296.76` | VAL=`289.44`
  * Prior Day Extremes: PDH=`304.16` | PDL=`281.75` | PDC=`288.90`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.22` | Weekly POC=`278.72` | Weekly VAL=`275.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`290.60` | Low=`274.76`
  * London Session (08:00-16:00 UTC): High=`281.86` | Low=`276.86`
  * New York Session (13:00-21:00 UTC): High=`292.96` | Low=`277.16`
  * Initial Balance (First Hour): IB High=`281.86` | IB Low=`279.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `281.47` - `283.73`
  * Optimal Trade Entry (OTE 0.705): `283.17`
  * Structural Invalidation Anchor (0.786): `284.86`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `286.78` | `286.91` | `281.22` | `282.04` | `10,384` | 2,948,806.86 USD | -1,167,982.63 USD | `-39.61%` | -5,369,429.05 USD | `-4.29` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `282.03` | `283.41` | `280.46` | `282.64` | `5,471` | 1,541,859.43 USD | 302,512.20 USD | `+19.62%` | -5,066,916.85 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `282.69` | `283.37` | `281.09` | `282.78` | `3,616` | 1,020,364.43 USD | 271,052.96 USD | `+26.56%` | -4,795,863.89 USD | `+0.98` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `288.16` | `288.89` | `287.26` | `287.42` | `1,737` | 500,104.64 USD | 4,430.67 USD | `+0.89%` | -4,233,589.94 USD | `+0.18` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `287.41` | `287.64` | `286.45` | `286.78` | `1,715` | 492,053.69 USD | 32,143.52 USD | `+6.53%` | -4,201,446.42 USD | `+0.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `286.78` | `286.91` | `280.46` | `282.83` | `19,492` | 5,516,881.49 USD | -588,654.38 USD | `-10.67%` | -4,790,100.80 USD | `-1.16` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `288.88` | `289.93` | `285.90` | `288.17` | `14,933` | 4,302,316.36 USD | 354,117.88 USD | `+8.23%` | -4,479,466.60 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.16` | `289.02` | `286.45` | `286.78` | `7,901` | 2,272,698.56 USD | 287,500.01 USD | `+12.65%` | -4,191,966.59 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `286.78` | `286.91` | `280.46` | `282.69` | `19,500` | 5,519,324.73 USD | -591,073.30 USD | `-10.71%` | -4,783,039.90 USD | `-0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `280.46` | `282.78` | `19,471` | 5,511,030.72 USD | -594,417.47 USD | `-10.79%` | -4,004,675.26 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `280.46` | `282.78` | `19,471` | 5,511,030.72 USD | -594,417.47 USD | `-10.79%` | -4,004,675.26 USD | `+0.05` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 01:44:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1977` | `0x12d2...f97f` | `LONG` | 1,025,203.96 USD | `3,627,243,000,000.00` | `303.26` | `282.38` | `0.000000` | -74,795.38 USD | `-7.30%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `291.49` | 12,466.74 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 12.47K USD at 291.4900 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `291.47` | 5,973.09 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 5.97K USD at 291.4700 USD [API] | `2026-10-27 22:29:58` |
| `ANNOUNCEMENT` | `INFO` | `259.00` | 56,657.29 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Long: 56.66K USD at 259.0000 USD [API] | `2026-10-15 02:24:27` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`295.47` (Vol: 187,900.00 USD, Dist: `+4.78%`) | Long MP=`271.80` (Vol: 166,000.00 USD, Dist: `--3.62%`)
  * 48H Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`271.85` (Vol: 166,000.00 USD, Dist: `--3.60%`)
  * 3D Horizon: Short MP=`294.39` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`274.98` (Vol: 169,100.00 USD, Dist: `--2.49%`)
  * 7D Horizon: Short MP=`294.37` (Vol: 208,300.00 USD, Dist: `+4.39%`) | Long MP=`263.68` (Vol: 277,800.00 USD, Dist: `--6.50%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 497,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 496,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 490,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 486,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 50,900.00 USD | 486,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 171.25 USD | 435,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 435,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 434,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 434,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `140.50` | 2,110.00 USD | 434,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `144.50` | 7,220.00 USD | 431,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 424,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 423,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 422,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 420,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 419,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 419,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 1,090.00 USD | 419,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 418,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 418,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 417,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 742.07 USD | 417,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 416,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 6,360.00 USD | 415,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `189.50` | 365.74 USD | 409,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 409,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 408,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 406,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 1,260.00 USD | 406,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 405,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 1,410.00 USD | 404,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 40,470.00 USD | 403,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 362,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 362,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 362,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 347.60 USD | 358,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `216.50` | 1,140.00 USD | 358,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 5,220.00 USD | 357,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `220.50` | 1,010.00 USD | 352,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 33,940.00 USD | 351,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 317,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 315,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 315,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,190.00 USD | 315,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 313,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 429.66 USD | 313,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 217.85 USD | 313,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `236.50` | 1,480.00 USD | 312,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 311,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `241.50` | 48,670.00 USD | 310,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 7,280.00 USD | 261,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `244.50` | 12,750.00 USD | 254,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 241,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `246.50` | 5,730.00 USD | 240,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 235,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.50` | 16,310,000.00 USD | 16,310,000.00 USD | 34,780.00 USD | 11,250.00 USD | 31,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 16,230,000.00 USD | 16,230,000.00 USD | 14,600.00 USD | 15,640.00 USD | 7,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 16,190,000.00 USD | 16,190,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.70` | 16,150,000.00 USD | 16,150,000.00 USD | 50,470.00 USD | 24,180.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.10` | 16,060,000.00 USD | 16,060,000.00 USD | 45,440.00 USD | 17,650.00 USD | 26,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.50` | 15,970,000.00 USD | 15,970,000.00 USD | 9,050.00 USD | 52,840.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 234,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.90` | 15,890,000.00 USD | 15,890,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 15,840,000.00 USD | 15,840,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 233,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 15,720,000.00 USD | 15,720,000.00 USD | 50,680.00 USD | 63,110.00 USD | 37,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.90` | 6,760,000.00 USD | 6,760,000.00 USD | 36,290.00 USD | 46,740.00 USD | 31,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.10` | 15,570,000.00 USD | 15,570,000.00 USD | 62,800.00 USD | 22,650.00 USD | 23,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.30` | 6,640,000.00 USD | 6,640,000.00 USD | 13,370.00 USD | 7,400.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.50` | 15,460,000.00 USD | 15,460,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 26,370.00 USD | 232,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.70` | 6,620,000.00 USD | 6,620,000.00 USD | 12,500.00 USD | 5,720.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 15,360,000.00 USD | 15,360,000.00 USD | 13,480.00 USD | 19,580.00 USD | 34.62 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.10` | 6,600,000.00 USD | 6,600,000.00 USD | 9,570.00 USD | 11,880.00 USD | 2,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 15,330,000.00 USD | 15,330,000.00 USD | 29,860.00 USD | 36,720.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.50` | 6,570,000.00 USD | 6,570,000.00 USD | 18,880.00 USD | 13,720.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 15,240,000.00 USD | 15,240,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.90` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 7,040.00 USD | 2.37 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.10` | 15,180,000.00 USD | 15,180,000.00 USD | 28,730.00 USD | 35,210.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.30` | 6,520,000.00 USD | 6,520,000.00 USD | 144.00 USD | 48.50 USD | 3.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.50` | 15,090,000.00 USD | 15,090,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 206,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.70` | 6,520,000.00 USD | 6,520,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 15,030,000.00 USD | 15,030,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.10` | 6,520,000.00 USD | 6,520,000.00 USD | 9,680.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 15,000,000.00 USD | 15,000,000.00 USD | 55,960.00 USD | 10,560.00 USD | 42,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.50` | 6,500,000.00 USD | 6,500,000.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 14,890,000.00 USD | 14,890,000.00 USD | 19,690.00 USD | 13,320.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.90` | 6,490,000.00 USD | 6,490,000.00 USD | 13,380.00 USD | 2,180.00 USD | 3.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.10` | 14,810,000.00 USD | 14,810,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.30` | 6,470,000.00 USD | 6,470,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.50` | 14,720,000.00 USD | 14,720,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.70` | 6,450,000.00 USD | 6,450,000.00 USD | 8,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 14,640,000.00 USD | 14,640,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.10` | 6,440,000.00 USD | 6,440,000.00 USD | 4,210.00 USD | 638.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 14,550,000.00 USD | 14,550,000.00 USD | 23,000.00 USD | 1,200.00 USD | 27,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 6,440,000.00 USD | 6,440,000.00 USD | 32.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.70` | 14,500,000.00 USD | 14,500,000.00 USD | 46,990.00 USD | 6,040.00 USD | 18,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 6,430,000.00 USD | 6,430,000.00 USD | 2,050.00 USD | 2,390.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.10` | 14,420,000.00 USD | 14,420,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 6,410,000.00 USD | 6,410,000.00 USD | 3,110.00 USD | 8,380.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.50` | 14,280,000.00 USD | 14,280,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 6,390,000.00 USD | 6,390,000.00 USD | 2,100.00 USD | 3,080.00 USD | 10,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 14,140,000.00 USD | 14,140,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 6,370,000.00 USD | 6,370,000.00 USD | 13,250.00 USD | 7,870.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 14,080,000.00 USD | 14,080,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 6,330,000.00 USD | 6,330,000.00 USD | 4,620.00 USD | 4,690.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 14,020,000.00 USD | 14,020,000.00 USD | 17,070.00 USD | 13,060.00 USD | 139.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 6,310,000.00 USD | 6,310,000.00 USD | 19,490.00 USD | 17,870.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.10` | 13,990,000.00 USD | 13,990,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 6,250,000.00 USD | 6,250,000.00 USD | 3,100.00 USD | 9,490.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.50` | 13,950,000.00 USD | 13,950,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 6,230,000.00 USD | 6,230,000.00 USD | 5,040.00 USD | 15,080.00 USD | 17,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 13,890,000.00 USD | 13,890,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 6,190,000.00 USD | 6,190,000.00 USD | 12,720.00 USD | 6,860.00 USD | 6,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 13,810,000.00 USD | 13,810,000.00 USD | 1,980.00 USD | 33,470.00 USD | 16,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 6,170,000.00 USD | 6,170,000.00 USD | 8,750.00 USD | 14,260.00 USD | 2.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 13,750,000.00 USD | 13,750,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 6,140,000.00 USD | 6,140,000.00 USD | 4,770.00 USD | 4,240.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.10` | 13,660,000.00 USD | 13,660,000.00 USD | 60,340.00 USD | 34,480.00 USD | 32,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 6,130,000.00 USD | 6,130,000.00 USD | 8,640.00 USD | 765.45 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.50` | 13,530,000.00 USD | 13,530,000.00 USD | 35,770.00 USD | 26,590.00 USD | 41.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 6,110,000.00 USD | 6,110,000.00 USD | 150.60 USD | 1,190.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 13,470,000.00 USD | 13,470,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 6,110,000.00 USD | 6,110,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 13,340,000.00 USD | 13,340,000.00 USD | 31,720.00 USD | 22,930.00 USD | 39,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 6,090,000.00 USD | 6,090,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 13,240,000.00 USD | 13,240,000.00 USD | 265,940.00 USD | 96,750.00 USD | 26,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 6,070,000.00 USD | 6,070,000.00 USD | 746.44 USD | 825.92 USD | 3.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.10` | 12,850,000.00 USD | 12,850,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 6,070,000.00 USD | 6,070,000.00 USD | 1,860.00 USD | 647.93 USD | 9.06 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.50` | 12,680,000.00 USD | 12,680,000.00 USD | 49,620.00 USD | 15,600.00 USD | 37,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.70` | 6,060,000.00 USD | 6,060,000.00 USD | 28,300.00 USD | 615.20 USD | 36,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 12,580,000.00 USD | 12,580,000.00 USD | 22,920.00 USD | 75,900.00 USD | 16,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 6,000,000.00 USD | 6,000,000.00 USD | 20,540.00 USD | 8,870.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 12,460,000.00 USD | 12,460,000.00 USD | 111,680.00 USD | 43,610.00 USD | 103,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 5,950,000.00 USD | 5,950,000.00 USD | 9,760.00 USD | 11,810.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `265.70` | 12,210,000.00 USD | 12,210,000.00 USD | 54,220.00 USD | 77,170.00 USD | 46,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.90` | 5,860,000.00 USD | 5,860,000.00 USD | 14,110.00 USD | 11,850.00 USD | 24.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.10` | 12,030,000.00 USD | 12,030,000.00 USD | 156,170.00 USD | 142,000.00 USD | 57,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 5,840,000.00 USD | 5,840,000.00 USD | 32,850.00 USD | 115.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.50` | 11,670,000.00 USD | 11,670,000.00 USD | 112,390.00 USD | 71,170.00 USD | 105,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.70` | 5,800,000.00 USD | 5,800,000.00 USD | 15,000.00 USD | 3,260.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 11,380,000.00 USD | 11,380,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 5,780,000.00 USD | 5,780,000.00 USD | 28,570.00 USD | 6,830.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 11,020,000.00 USD | 11,020,000.00 USD | 112,040.00 USD | 158,320.00 USD | 88,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 5,730,000.00 USD | 5,730,000.00 USD | 11,820.00 USD | 26,560.00 USD | 23.03 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `267.70` | 10,660,000.00 USD | 10,660,000.00 USD | 171,250.00 USD | 208,600.00 USD | 62,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.90` | 5,690,000.00 USD | 5,690,000.00 USD | 113,020.00 USD | 120,830.00 USD | 45,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.10` | 10,220,000.00 USD | 10,220,000.00 USD | 108,270.00 USD | 282,670.00 USD | 99,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 5,410,000.00 USD | 5,410,000.00 USD | 39,220.00 USD | 98,210.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.50` | 9,730,000.00 USD | 9,730,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.70` | 5,250,000.00 USD | 5,250,000.00 USD | 97,080.00 USD | 85,050.00 USD | 58,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 9,310,000.00 USD | 9,310,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 5,010,000.00 USD | 5,010,000.00 USD | 50,070.00 USD | 22,990.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 8,910,000.00 USD | 8,910,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 4,920,000.00 USD | 4,920,000.00 USD | 31,770.00 USD | 6,100.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `269.70` | 8,370,000.00 USD | 8,370,000.00 USD | 55,620.00 USD | 87,030.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 4,870,000.00 USD | 4,870,000.00 USD | 33,260.00 USD | 43,730.00 USD | 12,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.10` | 8,220,000.00 USD | 8,220,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 4,780,000.00 USD | 4,780,000.00 USD | 118,580.00 USD | 64,760.00 USD | 128,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.50` | 7,810,000.00 USD | 7,810,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 106.31 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.70` | 4,470,000.00 USD | 4,470,000.00 USD | 52,010.00 USD | 39,660.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 7,410,000.00 USD | 7,410,000.00 USD | 275,900.00 USD | 144,560.00 USD | 90,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 4,380,000.00 USD | 4,380,000.00 USD | 40,150.00 USD | 33,840.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 6,900,000.00 USD | 6,900,000.00 USD | 128,290.00 USD | 124,290.00 USD | 39,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 4,160,000.00 USD | 4,160,000.00 USD | 27,990.00 USD | 37,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `271.70` | 6,610,000.00 USD | 6,610,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 4,100,000.00 USD | 4,100,000.00 USD | 93,920.00 USD | 23,970.00 USD | 16,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.10` | 6,110,000.00 USD | 6,110,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 3,960,000.00 USD | 3,960,000.00 USD | 66,270.00 USD | 9,560.00 USD | 17,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.50` | 5,620,000.00 USD | 5,620,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `272.50` | 132.16 USD | 132.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `272.70` | 3,870,000.00 USD | 3,870,000.00 USD | 67,250.00 USD | 29,700.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 5,270,000.00 USD | 5,270,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 3,750,000.00 USD | 3,750,000.00 USD | 89,600.00 USD | 81,790.00 USD | 6,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 4,830,000.00 USD | 4,830,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 3,570,000.00 USD | 3,570,000.00 USD | 225,140.00 USD | 235,090.00 USD | 90,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 4,140,000.00 USD | 4,140,000.00 USD | 195,450.00 USD | 467,590.00 USD | 206,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 3,020,000.00 USD | 3,020,000.00 USD | 88,320.00 USD | 196,260.00 USD | 53,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.10` | 3,270,000.00 USD | 3,270,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 2,690,000.00 USD | 2,690,000.00 USD | 204,120.00 USD | 170,140.00 USD | 126,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.50` | 2,420,000.00 USD | 2,420,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `274.70` | 2,190,000.00 USD | 2,190,000.00 USD | 101,740.00 USD | 43,050.00 USD | 53,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.90` | 1,810,000.00 USD | 1,810,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 1,990,000.00 USD | 1,990,000.00 USD | 68,880.00 USD | 21,290.00 USD | 48,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,300,000.00 USD | 1,300,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 1,850,000.00 USD | 1,850,000.00 USD | 63,860.00 USD | 65,590.00 USD | 39,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 1,150,000.00 USD | 1,150,000.00 USD | 1,350.00 USD | 51,050.00 USD | 117.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 1,680,000.00 USD | 1,680,000.00 USD | 73,380.00 USD | 51,470.00 USD | 22,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.10` | 1,100,000.00 USD | 1,100,000.00 USD | 3,750.00 USD | 0.00 USD | 5.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 1,530,000.00 USD | 1,530,000.00 USD | 68,110.00 USD | 44,550.00 USD | 3,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.50` | 1,100,000.00 USD | 1,100,000.00 USD | 485.90 USD | 0.00 USD | 42.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `276.70` | 1,420,000.00 USD | 1,420,000.00 USD | 18,360.00 USD | 21,650.00 USD | 24,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.90` | 1,100,000.00 USD | 1,100,000.00 USD | 45,560.00 USD | 23,180.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 1,350,000.00 USD | 1,350,000.00 USD | 19,010.00 USD | 64,370.00 USD | 67,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 63,290.00 USD | 88.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 1,200,000.00 USD | 1,200,000.00 USD | 74,620.00 USD | 55,090.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 943,140.00 USD | 943,140.00 USD | 0.00 USD | 27,190.00 USD | 84,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 1,050,000.00 USD | 1,050,000.00 USD | 12,650.00 USD | 9,490.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.10` | 831,580.00 USD | 831,580.00 USD | 24,750.00 USD | 0.00 USD | 59,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 1,010,000.00 USD | 1,010,000.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.50` | 747,350.00 USD | 747,350.00 USD | 17,440.00 USD | 71,230.00 USD | 33.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 864,050.00 USD | 864,050.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.90` | 658,640.00 USD | 658,640.00 USD | 42,950.00 USD | 32,690.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.10` | 791,860.00 USD | 791,860.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 565,850.00 USD | 565,850.00 USD | 31,330.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.50` | 716,080.00 USD | 716,080.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 492,830.00 USD | 492,830.00 USD | 46,800.00 USD | 0.00 USD | 54,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.90` | 642,610.00 USD | 642,610.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.30` | 605,180.00 USD | 605,180.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.50` | 391,630.00 USD | 391,630.00 USD | 0.00 USD | 0.00 USD | 65.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.70` | 533,800.00 USD | 533,800.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.10` | 449,290.00 USD | 449,290.00 USD | 0.00 USD | 0.00 USD | 66,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 391,560.00 USD | 391,560.00 USD | 0.00 USD | 0.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 328,750.00 USD | 328,750.00 USD | 565.82 USD | 0.00 USD | 122,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.90` | 382,790.00 USD | 382,790.00 USD | 0.00 USD | 20,570.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.10` | 205,730.00 USD | 205,730.00 USD | 0.00 USD | 0.00 USD | 133,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.30` | 267,380.00 USD | 267,380.00 USD | 9,480.00 USD | 22,600.00 USD | 154,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.50` | 71,960.00 USD | 71,960.00 USD | 32,190.00 USD | 0.00 USD | 39,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.70` | 80,330.00 USD | 80,330.00 USD | 5,740.00 USD | 34,190.00 USD | 40,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.90` | 42.40 USD | 42.40 USD | 0.00 USD | 0.00 USD | 42.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.10` | 295,060.00 USD | 295,060.00 USD | 71,390.00 USD | 44,720.00 USD | 178,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.30` | 126,570.00 USD | 126,570.00 USD | 0.00 USD | 37,310.00 USD | 89,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.50` | 375,900.00 USD | 375,900.00 USD | 0.00 USD | 0.00 USD | 80,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.70` | 365,430.00 USD | 365,430.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.90` | 445,170.00 USD | 445,170.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.10` | 550,880.00 USD | 550,880.00 USD | 49,500.00 USD | 0.00 USD | 135,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.30` | 560,660.00 USD | 560,660.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.50` | 809,960.00 USD | 809,960.00 USD | 26,130.00 USD | 198,780.00 USD | 34,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.70` | 684,080.00 USD | 684,080.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.10` | 787,880.00 USD | 787,880.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 1,380,000.00 USD | 1,380,000.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.50` | 1,010,000.00 USD | 1,010,000.00 USD | 91,500.00 USD | 95,280.00 USD | 39,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.70` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.90` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 19,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.10` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.50` | 1,690,000.00 USD | 1,690,000.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 1,860,000.00 USD | 1,860,000.00 USD | 27,530.00 USD | 141,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.10` | 1,250,000.00 USD | 1,250,000.00 USD | 20,810.00 USD | 117,540.00 USD | 80,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 2,000,000.00 USD | 2,000,000.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.50` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 11,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.70` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.10` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 43.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 19.71 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 1,870.00 USD | 4.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.50` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 5.58 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 33.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 5.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 9,250.00 USD | 28.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 21,970.00 USD | 5.34 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 94,090.00 USD | 4.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.10` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 118,660.00 USD | 41.53 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 1,410,000.00 USD | 1,410,000.00 USD | 13,260.00 USD | 61,180.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.50` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 26,610.00 USD | 66.48 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 1,530,000.00 USD | 1,530,000.00 USD | 19,680.00 USD | 98,000.00 USD | 9.69 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 118,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 1,580,000.00 USD | 1,580,000.00 USD | 10,710.00 USD | 41,110.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 2,770,000.00 USD | 2,770,000.00 USD | 534.50 USD | 112,560.00 USD | 40.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 1,640,000.00 USD | 1,640,000.00 USD | 14,220.00 USD | 50,540.00 USD | 1.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 2,810,000.00 USD | 2,810,000.00 USD | 37,280.00 USD | 1,170.00 USD | 20.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 1,860,000.00 USD | 1,860,000.00 USD | 88,090.00 USD | 31,360.00 USD | 93,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.10` | 3,040,000.00 USD | 3,040,000.00 USD | 85,150.00 USD | 33,590.00 USD | 105,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 2,040,000.00 USD | 2,040,000.00 USD | 49,730.00 USD | 74,090.00 USD | 56,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.50` | 3,120,000.00 USD | 3,120,000.00 USD | 69,950.00 USD | 15,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 2,430,000.00 USD | 2,430,000.00 USD | 133,430.00 USD | 96,720.00 USD | 168,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 3,380,000.00 USD | 3,380,000.00 USD | 63,470.00 USD | 92,770.00 USD | 104,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 2,610,000.00 USD | 2,610,000.00 USD | 32,330.00 USD | 64,690.00 USD | 73,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 3,750,000.00 USD | 3,750,000.00 USD | 45,590.00 USD | 65,580.00 USD | 252,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 2,840,000.00 USD | 2,840,000.00 USD | 61,560.00 USD | 105,660.00 USD | 68,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 4,060,000.00 USD | 4,060,000.00 USD | 105,410.00 USD | 72,570.00 USD | 133,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 3,020,000.00 USD | 3,020,000.00 USD | 105,070.00 USD | 37,180.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.10` | 4,340,000.00 USD | 4,340,000.00 USD | 75,740.00 USD | 90,470.00 USD | 119,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 3,230,000.00 USD | 3,230,000.00 USD | 88,010.00 USD | 95,560.00 USD | 27,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.50` | 4,480,000.00 USD | 4,480,000.00 USD | 1,060.00 USD | 77,140.00 USD | 57,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.70` | 3,360,000.00 USD | 3,360,000.00 USD | 34,010.00 USD | 39,270.00 USD | 62,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 4,870,000.00 USD | 4,870,000.00 USD | 206,840.00 USD | 50,620.00 USD | 134,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 3,450,000.00 USD | 3,450,000.00 USD | 52,650.00 USD | 177.11 USD | 36,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 4,880,000.00 USD | 4,880,000.00 USD | 3,960.00 USD | 2,500.00 USD | 49.85 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 3,480,000.00 USD | 3,480,000.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 4,970,000.00 USD | 4,970,000.00 USD | 144.38 USD | 56,790.00 USD | 34,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 3,510,000.00 USD | 3,510,000.00 USD | 1,150.00 USD | 9,340.00 USD | 16,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.10` | 5,150,000.00 USD | 5,150,000.00 USD | 49,240.00 USD | 81,680.00 USD | 54,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 3,710,000.00 USD | 3,710,000.00 USD | 55,160.00 USD | 8,520.00 USD | 137,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.50` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 12,660.00 USD | 47,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 3,830,000.00 USD | 3,830,000.00 USD | 29,410.00 USD | 13,250.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 5,330,000.00 USD | 5,330,000.00 USD | 70,090.00 USD | 993.25 USD | 39,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 3,890,000.00 USD | 3,890,000.00 USD | 7,660.00 USD | 16,030.00 USD | 35,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 5,380,000.00 USD | 5,380,000.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 3,990,000.00 USD | 3,990,000.00 USD | 35,750.00 USD | 23,680.00 USD | 43,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 295.91 USD | 428.07 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `299.70` | 5,410,000.00 USD | 5,410,000.00 USD | 5,310.00 USD | 7,720.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 4,060,000.00 USD | 4,060,000.00 USD | 20,860.00 USD | 22,550.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.10` | 5,460,000.00 USD | 5,460,000.00 USD | 51,500.00 USD | 2,470.00 USD | 29.14 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 4,190,000.00 USD | 4,190,000.00 USD | 48,160.00 USD | 32,750.00 USD | 42,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.50` | 5,520,000.00 USD | 5,520,000.00 USD | 866.20 USD | 36,230.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 4,300,000.00 USD | 4,300,000.00 USD | 20,040.00 USD | 37,920.00 USD | 52,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 5,660,000.00 USD | 5,660,000.00 USD | 24,730.00 USD | 34,630.00 USD | 84,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 4,370,000.00 USD | 4,370,000.00 USD | 15,450.00 USD | 28,660.00 USD | 26,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 5,880,000.00 USD | 5,880,000.00 USD | 71,140.00 USD | 55,420.00 USD | 94,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 4,470,000.00 USD | 4,470,000.00 USD | 31,390.00 USD | 24,180.00 USD | 44,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 1,700.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `301.70` | 6,050,000.00 USD | 6,050,000.00 USD | 37,640.00 USD | 130,520.00 USD | 69.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 4,560,000.00 USD | 4,560,000.00 USD | 29,910.00 USD | 47,960.00 USD | 11,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.10` | 6,260,000.00 USD | 6,260,000.00 USD | 53,220.00 USD | 123,390.00 USD | 26,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 4,580,000.00 USD | 4,580,000.00 USD | 5,320.00 USD | 12,280.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.50` | 6,430,000.00 USD | 6,430,000.00 USD | 31,330.00 USD | 102,200.00 USD | 41,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 4,640,000.00 USD | 4,640,000.00 USD | 11,520.00 USD | 11,480.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 6,540,000.00 USD | 6,540,000.00 USD | 40,380.00 USD | 65,280.00 USD | 21.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 4,680,000.00 USD | 4,680,000.00 USD | 20,770.00 USD | 1,270.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 173.09 USD | 322.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 4,700,000.00 USD | 4,700,000.00 USD | 11,460.00 USD | 232.42 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 6,590,000.00 USD | 6,590,000.00 USD | 17,370.00 USD | 8,710.00 USD | 24,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 4,750,000.00 USD | 4,750,000.00 USD | 29,930.00 USD | 3,900.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.10` | 6,600,000.00 USD | 6,600,000.00 USD | 5,440.00 USD | 1,950.00 USD | 67.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 4,810,000.00 USD | 4,810,000.00 USD | 4,310.00 USD | 5,170.00 USD | 48,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.50` | 6,610,000.00 USD | 6,610,000.00 USD | 3,480.00 USD | 11,110.00 USD | 155.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 4,860,000.00 USD | 4,860,000.00 USD | 9,700.00 USD | 4,830.00 USD | 40,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 6,670,000.00 USD | 6,670,000.00 USD | 34,680.00 USD | 18,990.00 USD | 8,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 4,870,000.00 USD | 4,870,000.00 USD | 9,410.00 USD | 249.40 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 7,080,000.00 USD | 7,080,000.00 USD | 162,420.00 USD | 124,800.00 USD | 117,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 4,880,000.00 USD | 4,880,000.00 USD | 4,670.00 USD | 1,640.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 7,190,000.00 USD | 7,190,000.00 USD | 82,270.00 USD | 18,170.00 USD | 12,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 4,890,000.00 USD | 4,890,000.00 USD | 9,360.00 USD | 2,720.00 USD | 1,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.10` | 7,330,000.00 USD | 7,330,000.00 USD | 22,930.00 USD | 67,820.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 4,900,000.00 USD | 4,900,000.00 USD | 3,900.00 USD | 3,200.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.50` | 7,460,000.00 USD | 7,460,000.00 USD | 30,150.00 USD | 41,830.00 USD | 65,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 4,930,000.00 USD | 4,930,000.00 USD | 4,480.00 USD | 21,600.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 7,630,000.00 USD | 7,630,000.00 USD | 58,810.00 USD | 50,570.00 USD | 57,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 5,020,000.00 USD | 5,020,000.00 USD | 33,080.00 USD | 42,120.00 USD | 13,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 7,870,000.00 USD | 7,870,000.00 USD | 27,410.00 USD | 123,720.00 USD | 83,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 5,060,000.00 USD | 5,060,000.00 USD | 6,340.00 USD | 22,280.00 USD | 9,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 411.74 USD | 2,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `307.70` | 8,050,000.00 USD | 8,050,000.00 USD | 84,930.00 USD | 74,370.00 USD | 23,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 5,150,000.00 USD | 5,150,000.00 USD | 33,320.00 USD | 30,540.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.10` | 8,320,000.00 USD | 8,320,000.00 USD | 105,700.00 USD | 63,640.00 USD | 101,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 5,170,000.00 USD | 5,170,000.00 USD | 13,940.00 USD | 7,490.00 USD | 5,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.50` | 8,570,000.00 USD | 8,570,000.00 USD | 118,090.00 USD | 64,440.00 USD | 65,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 5,180,000.00 USD | 5,180,000.00 USD | 5,550.00 USD | 387.08 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 8,680,000.00 USD | 8,680,000.00 USD | 60,660.00 USD | 31,940.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 5,200,000.00 USD | 5,200,000.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 8,770,000.00 USD | 8,770,000.00 USD | 27,540.00 USD | 26,240.00 USD | 36,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 5,250,000.00 USD | 5,250,000.00 USD | 16,550.00 USD | 22,830.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 9,090,000.00 USD | 9,090,000.00 USD | 40,410.00 USD | 132,660.00 USD | 146,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 5,260,000.00 USD | 5,260,000.00 USD | 8,500.00 USD | 2,590.00 USD | 978.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.10` | 9,250,000.00 USD | 9,250,000.00 USD | 34,250.00 USD | 63,360.00 USD | 62,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 7,040.00 USD | 2.37 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.50` | 9,410,000.00 USD | 9,410,000.00 USD | 68,560.00 USD | 73,280.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 3,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.70` | 5,270,000.00 USD | 5,270,000.00 USD | 144.00 USD | 284.03 USD | 2.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 9,480,000.00 USD | 9,480,000.00 USD | 35,670.00 USD | 30,720.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 5,270,000.00 USD | 5,270,000.00 USD | 134.35 USD | 2,050.00 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 9,680,000.00 USD | 9,680,000.00 USD | 84,180.00 USD | 65,480.00 USD | 47,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 5,290,000.00 USD | 5,290,000.00 USD | 7,390.00 USD | 6,590.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 9,760,000.00 USD | 9,760,000.00 USD | 34,040.00 USD | 11,430.00 USD | 31,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 5,290,000.00 USD | 5,290,000.00 USD | 2,810.00 USD | 0.00 USD | 5.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.10` | 9,830,000.00 USD | 9,830,000.00 USD | 46,850.00 USD | 1,100.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 5,310,000.00 USD | 5,310,000.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.50` | 9,920,000.00 USD | 9,920,000.00 USD | 19,540.00 USD | 22,460.00 USD | 49,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 5,320,000.00 USD | 5,320,000.00 USD | 13,380.00 USD | 2,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 10,000,000.00 USD | 10,000,000.00 USD | 22,600.00 USD | 20,090.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 5,330,000.00 USD | 5,330,000.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 10,110,000.00 USD | 10,110,000.00 USD | 64,910.00 USD | 30,120.00 USD | 22,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 5,340,000.00 USD | 5,340,000.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 10,180,000.00 USD | 10,180,000.00 USD | 32,170.00 USD | 15,010.00 USD | 23,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 5,350,000.00 USD | 5,350,000.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.10` | 10,260,000.00 USD | 10,260,000.00 USD | 26,810.00 USD | 362.37 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.30` | 5,360,000.00 USD | 5,360,000.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.50` | 10,330,000.00 USD | 10,330,000.00 USD | 48,630.00 USD | 307.60 USD | 24,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.70` | 5,360,000.00 USD | 5,360,000.00 USD | 32.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 10,370,000.00 USD | 10,370,000.00 USD | 29,590.00 USD | 0.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 5,370,000.00 USD | 5,370,000.00 USD | 32.50 USD | 1,400.00 USD | 6,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 10,380,000.00 USD | 10,380,000.00 USD | 5,690.00 USD | 547.95 USD | 56.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.50` | 5,400,000.00 USD | 5,400,000.00 USD | 3,750.00 USD | 3,270.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `315.50` | 6,520.00 USD | 9,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `315.70` | 10,490,000.00 USD | 10,490,000.00 USD | 9,200.00 USD | 50,270.00 USD | 48,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.90` | 5,410,000.00 USD | 5,410,000.00 USD | 3,360.00 USD | 5,260.00 USD | 43.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.10` | 10,590,000.00 USD | 10,590,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.30` | 5,420,000.00 USD | 5,420,000.00 USD | 128.70 USD | 3,070.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.50` | 10,640,000.00 USD | 10,640,000.00 USD | 16,120.00 USD | 20,630.00 USD | 18,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.70` | 5,460,000.00 USD | 5,460,000.00 USD | 13,180.00 USD | 6,830.00 USD | 17,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 10,660,000.00 USD | 10,660,000.00 USD | 3,030.00 USD | 10,840.00 USD | 121.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.10` | 5,470,000.00 USD | 5,470,000.00 USD | 3,940.00 USD | 4,470.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 10,670,000.00 USD | 10,670,000.00 USD | 14,540.00 USD | 748.91 USD | 46.43 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.50` | 5,520,000.00 USD | 5,520,000.00 USD | 11,570.00 USD | 14,470.00 USD | 17,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 10,670,000.00 USD | 10,670,000.00 USD | 620.15 USD | 265.17 USD | 97.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.90` | 5,550,000.00 USD | 5,550,000.00 USD | 7,000.00 USD | 9,190.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.10` | 10,710,000.00 USD | 10,710,000.00 USD | 22,250.00 USD | 9,100.00 USD | 43.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.30` | 5,570,000.00 USD | 5,570,000.00 USD | 2,200.00 USD | 8,470.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.50` | 10,770,000.00 USD | 10,770,000.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.70` | 5,590,000.00 USD | 5,590,000.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 10,820,000.00 USD | 10,820,000.00 USD | 10,270.00 USD | 17,970.00 USD | 23,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.10` | 5,620,000.00 USD | 5,620,000.00 USD | 12,470.00 USD | 6,760.00 USD | 6,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 18,060.00 USD | 40.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.50` | 5,640,000.00 USD | 5,640,000.00 USD | 8,400.00 USD | 10,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 10,860,000.00 USD | 10,860,000.00 USD | 936.82 USD | 12,700.00 USD | 37.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.80` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.10` | 10,930,000.00 USD | 10,930,000.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.50` | 10,960,000.00 USD | 10,960,000.00 USD | 15,190.00 USD | 10,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 10,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.30` | 10,980,000.00 USD | 10,980,000.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.70` | 11,010,000.00 USD | 11,010,000.00 USD | 4,780.00 USD | 9,110.00 USD | 15,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.10` | 11,050,000.00 USD | 11,050,000.00 USD | 22,940.00 USD | 8,290.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.50` | 11,050,000.00 USD | 11,050,000.00 USD | 555.20 USD | 365.55 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 11,070,000.00 USD | 11,070,000.00 USD | 16,590.00 USD | 5,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.30` | 11,100,000.00 USD | 11,100,000.00 USD | 14,160.00 USD | 5,860.00 USD | 11,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.70` | 11,110,000.00 USD | 11,110,000.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.10` | 11,120,000.00 USD | 11,120,000.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `330.50` | 276.63 USD | 11,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `339.50` | 1,360.00 USD | 12,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `357.50` | 39,330.00 USD | 51,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 52,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 53,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `395.50` | 3,430.00 USD | 56,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `427.50` | 9,480.00 USD | 66,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `432.50` | 8,810.00 USD | 74,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 121,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `466.50` | 135.75 USD | 121,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 1,040.00 USD | 122,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 123,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `565.50` | 1,450.00 USD | 124,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `95.50` | 497,610.00 USD | 0.00 USD | 920.05 USD | `-66.71%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 496,690.00 USD | 0.00 USD | 6,240.00 USD | `-64.61%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 490,460.00 USD | 0.00 USD | 4,080.00 USD | `-64.26%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 486,380.00 USD | 0.00 USD | 212.76 USD | `-61.82%` | `1,943,000,000.00` |
| `Live` | `Long` | `115.50` | 486,170.00 USD | 0.00 USD | 50,900.00 USD | `-59.73%` | `440,704,000,000.00` |
| `Live` | `Long` | `116.50` | 435,260.00 USD | 0.00 USD | 171.25 USD | `-59.38%` | `1,470,000,000.00` |
| `Live` | `Long` | `118.50` | 435,090.00 USD | 0.00 USD | 212.35 USD | `-58.69%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 434,880.00 USD | 0.00 USD | 124.46 USD | `-57.29%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 434,760.00 USD | 0.00 USD | 658.18 USD | `-55.90%` | `5,203,000,000.00` |
| `Live` | `Long` | `140.50` | 434,100.00 USD | 0.00 USD | 2,110.00 USD | `-51.02%` | `15,000,000,000.00` |
| `Live` | `Long` | `144.50` | 431,990.00 USD | 0.00 USD | 7,220.00 USD | `-49.62%` | `50,000,000,000.00` |
| `Live` | `Long` | `147.50` | 424,770.00 USD | 0.00 USD | 895.47 USD | `-48.58%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 423,870.00 USD | 0.00 USD | 1,270.00 USD | `-48.23%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 422,600.00 USD | 0.00 USD | 2,370.00 USD | `-47.88%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 420,240.00 USD | 0.00 USD | 303.78 USD | `-46.83%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 419,930.00 USD | 0.00 USD | 325.00 USD | `-43.35%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 419,610.00 USD | 0.00 USD | 285.75 USD | `-41.60%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 419,320.00 USD | 0.00 USD | 1,090.00 USD | `-40.56%` | `6,397,000,000.00` |
| `Live` | `Long` | `174.50` | 418,230.00 USD | 0.00 USD | 169.96 USD | `-39.16%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 418,060.00 USD | 0.00 USD | 516.67 USD | `-38.81%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 417,550.00 USD | 0.00 USD | 373.83 USD | `-38.47%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 417,170.00 USD | 0.00 USD | 742.07 USD | `-36.02%` | `4,044,000,000.00` |
| `Live` | `Long` | `184.50` | 416,430.00 USD | 0.00 USD | 616.05 USD | `-35.68%` | `3,339,000,000.00` |
| `Live` | `Long` | `188.50` | 415,810.00 USD | 0.00 USD | 6,360.00 USD | `-34.28%` | `33,719,000,000.00` |
| `Live` | `Long` | `189.50` | 409,460.00 USD | 0.00 USD | 365.74 USD | `-33.93%` | `1,930,000,000.00` |
| `Live` | `Long` | `191.50` | 409,090.00 USD | 0.00 USD | 858.49 USD | `-33.24%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 408,230.00 USD | 0.00 USD | 1,490.00 USD | `-32.89%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 406,750.00 USD | 0.00 USD | 370.47 USD | `-31.84%` | `1,895,000,000.00` |
| `Live` | `Long` | `199.50` | 406,380.00 USD | 0.00 USD | 1,260.00 USD | `-30.45%` | `6,335,000,000.00` |
| `Live` | `Long` | `200.50` | 405,110.00 USD | 0.00 USD | 293.13 USD | `-30.10%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 404,820.00 USD | 0.00 USD | 1,410.00 USD | `-29.40%` | `6,949,000,000.00` |
| `Live` | `Long` | `204.50` | 403,410.00 USD | 0.00 USD | 40,470.00 USD | `-28.70%` | `197,897,000,000.00` |
| `Live` | `Long` | `205.50` | 362,940.00 USD | 0.00 USD | 191.53 USD | `-28.35%` | `932,000,000.00` |
| `Live` | `Long` | `210.50` | 362,750.00 USD | 0.00 USD | 108.83 USD | `-26.61%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 362,640.00 USD | 0.00 USD | 3,800.00 USD | `-25.57%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 358,840.00 USD | 0.00 USD | 347.60 USD | `-24.87%` | `1,613,000,000.00` |
| `Live` | `Long` | `216.50` | 358,490.00 USD | 0.00 USD | 1,140.00 USD | `-24.52%` | `5,260,000,000.00` |
| `Live` | `Long` | `219.50` | 357,350.00 USD | 0.00 USD | 5,220.00 USD | `-23.47%` | `23,803,000,000.00` |
| `Live` | `Long` | `220.50` | 352,130.00 USD | 0.00 USD | 1,010.00 USD | `-23.13%` | `4,592,000,000.00` |
| `Live` | `Long` | `223.50` | 351,120.00 USD | 0.00 USD | 33,940.00 USD | `-22.08%` | `151,870,000,000.00` |
| `Live` | `Long` | `226.50` | 317,170.00 USD | 0.00 USD | 1,240.00 USD | `-21.03%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 315,940.00 USD | 0.00 USD | 174.49 USD | `-20.68%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 315,760.00 USD | 0.00 USD | 642.77 USD | `-20.34%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 315,120.00 USD | 0.00 USD | 1,190.00 USD | `-19.99%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 313,930.00 USD | 0.00 USD | 295.86 USD | `-19.29%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 313,640.00 USD | 0.00 USD | 429.66 USD | `-18.94%` | `1,848,000,000.00` |
| `Live` | `Long` | `234.50` | 313,210.00 USD | 0.00 USD | 217.85 USD | `-18.24%` | `929,000,000.00` |
| `Live` | `Long` | `236.50` | 312,990.00 USD | 0.00 USD | 1,480.00 USD | `-17.55%` | `6,274,000,000.00` |
| `Live` | `Long` | `239.50` | 311,510.00 USD | 0.00 USD | 1,030.00 USD | `-16.50%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 310,480.00 USD | 0.00 USD | 48,670.00 USD | `-15.80%` | `201,521,000,000.00` |
| `Live` | `Long` | `243.50` | 261,810.00 USD | 0.00 USD | 7,280.00 USD | `-15.11%` | `29,890,000,000.00` |
| `Live` | `Long` | `244.50` | 254,540.00 USD | 0.00 USD | 12,750.00 USD | `-14.76%` | `52,161,000,000.00` |
| `Live` | `Long` | `245.50` | 241,780.00 USD | 0.00 USD | 1,030.00 USD | `-14.41%` | `4,182,000,000.00` |
| `Live` | `Long` | `246.50` | 240,760.00 USD | 0.00 USD | 5,730.00 USD | `-14.06%` | `23,253,000,000.00` |
| `Live` | `Long` | `247.50` | 235,020.00 USD | 0.00 USD | 699.44 USD | `-13.71%` | `2,826,000,000.00` |
| `Live` | `Long` | `250.50` | 234,320.00 USD | 0.00 USD | 1,330.00 USD | `-12.67%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 233,000.00 USD | 0.00 USD | 268.35 USD | `-12.32%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 232,730.00 USD | 0.00 USD | 26,370.00 USD | `-11.97%` | `104,453,000,000.00` |
| `Live` | `Long` | `254.50` | 206,360.00 USD | 0.00 USD | 362.92 USD | `-11.27%` | `1,426,000,000.00` |
| `Live` | `Long` | `256.50` | 205,990.00 USD | 0.00 USD | 2,480.00 USD | `-10.57%` | `9,686,000,000.00` |
| `Live` | `Long` | `257.50` | 203,510.00 USD | 0.00 USD | 14,580.00 USD | `-10.23%` | `56,622,000,000.00` |
| `Live` | `Long` | `258.50` | 188,930.00 USD | 0.00 USD | 176.56 USD | `-9.88%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 188,750.00 USD | 0.00 USD | 3,860.00 USD | `-9.18%` | `14,816,000,000.00` |
| `Live` | `Long` | `264.50` | 184,890.00 USD | 0.00 USD | 280.37 USD | `-7.79%` | `1,060,000,000.00` |
| `Live` | `Long` | `265.50` | 184,610.00 USD | 0.00 USD | 121,910.00 USD | `-7.44%` | `459,161,000,000.00` |
| `Live` | `Long` | `266.50` | 62,700.00 USD | 0.00 USD | 15,210.00 USD | `-7.09%` | `57,069,000,000.00` |
| `Live` | `Long` | `267.50` | 47,500.00 USD | 0.00 USD | 684.00 USD | `-6.74%` | `2,557,000,000.00` |
| `Live` | `Long` | `268.50` | 46,810.00 USD | 0.00 USD | 7,020.00 USD | `-6.39%` | `26,129,000,000.00` |
| `Live` | `Long` | `269.50` | 39,800.00 USD | 0.00 USD | 37,920.00 USD | `-6.04%` | `140,689,000,000.00` |
| `Live` | `Long` | `270.50` | 1,880.00 USD | 0.00 USD | 106.31 USD | `-5.69%` | `393,000,000.00` |
| `Live` | `Long` | `271.50` | 1,770.00 USD | 0.00 USD | 1,000.00 USD | `-5.34%` | `3,685,000,000.00` |
| `Live` | `Short` | `272.50` | 132.16 USD | 132.16 USD | 0.00 USD | `-5.00%` | `485,000,000.00` |
| `Live` | `Long` | `274.50` | 773.38 USD | 0.00 USD | 567.94 USD | `-4.30%` | `2,069,000,000.00` |
| `Live` | `Long` | `276.50` | 205.44 USD | 0.00 USD | 205.44 USD | `-3.60%` | `743,000,000.00` |
| `Live` | `Short` | `299.50` | 428.07 USD | 295.91 USD | 0.00 USD | `+4.42%` | `988,000,000.00` |
| `Live` | `Short` | `301.50` | 2,130.00 USD | 1,700.00 USD | 0.00 USD | `+5.11%` | `5,643,000,000.00` |
| `Live` | `Short` | `307.50` | 2,540.00 USD | 411.74 USD | 0.00 USD | `+7.21%` | `1,339,000,000.00` |
| `Live` | `Short` | `310.50` | 3,060.00 USD | 517.91 USD | 0.00 USD | `+8.25%` | `1,668,000,000.00` |
| `Live` | `Short` | `315.50` | 9,580.00 USD | 6,520.00 USD | 0.00 USD | `+10.00%` | `20,668,000,000.00` |
| `Live` | `Short` | `318.50` | 9,690.00 USD | 114.34 USD | 0.00 USD | `+11.04%` | `359,000,000.00` |
| `Live` | `Short` | `320.50` | 10,800.00 USD | 1,110.00 USD | 0.00 USD | `+11.74%` | `3,452,000,000.00` |
| `Live` | `Short` | `330.50` | 11,080.00 USD | 276.63 USD | 0.00 USD | `+15.23%` | `837,000,000.00` |
| `Live` | `Short` | `339.50` | 12,440.00 USD | 1,360.00 USD | 0.00 USD | `+18.36%` | `4,000,000,000.00` |
| `Live` | `Short` | `357.50` | 51,760.00 USD | 39,330.00 USD | 0.00 USD | `+24.64%` | `110,000,000,000.00` |
| `Live` | `Short` | `358.50` | 52,770.00 USD | 1,010.00 USD | 0.00 USD | `+24.99%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 53,210.00 USD | 445.52 USD | 0.00 USD | `+28.47%` | `1,209,000,000.00` |
| `Live` | `Short` | `395.50` | 56,650.00 USD | 3,430.00 USD | 0.00 USD | `+37.89%` | `8,681,000,000.00` |
| `Live` | `Short` | `427.50` | 66,130.00 USD | 9,480.00 USD | 0.00 USD | `+49.04%` | `22,172,000,000.00` |
| `Live` | `Short` | `432.50` | 74,930.00 USD | 8,810.00 USD | 0.00 USD | `+50.79%` | `20,366,000,000.00` |
| `Live` | `Short` | `459.50` | 121,190.00 USD | 46,250.00 USD | 0.00 USD | `+60.20%` | `100,662,000,000.00` |
| `Live` | `Short` | `466.50` | 121,320.00 USD | 135.75 USD | 0.00 USD | `+62.64%` | `291,000,000.00` |
| `Live` | `Short` | `498.50` | 122,370.00 USD | 1,040.00 USD | 0.00 USD | `+73.80%` | `2,093,000,000.00` |
| `Live` | `Short` | `560.50` | 123,210.00 USD | 842.43 USD | 0.00 USD | `+95.41%` | `1,503,000,000.00` |
| `Live` | `Short` | `565.50` | 124,660.00 USD | 1,450.00 USD | 0.00 USD | `+97.16%` | `2,572,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 333,000.00 USD | 0.00 USD | 210.94 USD | `-49.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 332,790.00 USD | 0.00 USD | 2,070.00 USD | `-49.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 330,720.00 USD | 0.00 USD | 2,530.00 USD | `-37.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 328,190.00 USD | 0.00 USD | 490.59 USD | `-35.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 327,700.00 USD | 0.00 USD | 482.01 USD | `-31.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 327,220.00 USD | 0.00 USD | 189.07 USD | `-30.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 327,030.00 USD | 0.00 USD | 441.60 USD | `-27.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 326,590.00 USD | 0.00 USD | 703.49 USD | `-26.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 325,890.00 USD | 0.00 USD | 638.36 USD | `-22.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 325,250.00 USD | 0.00 USD | 740.85 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 324,510.00 USD | 0.00 USD | 1,050.00 USD | `-20.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 323,460.00 USD | 0.00 USD | 389.48 USD | `-18.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 323,070.00 USD | 0.00 USD | 220.64 USD | `-17.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 322,850.00 USD | 0.00 USD | 429.30 USD | `-16.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 322,420.00 USD | 0.00 USD | 296.50 USD | `-16.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 322,120.00 USD | 0.00 USD | 216.45 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 321,910.00 USD | 0.00 USD | 101.61 USD | `-15.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 321,800.00 USD | 0.00 USD | 366.75 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 321,440.00 USD | 0.00 USD | 1,630.00 USD | `-14.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 319,810.00 USD | 0.00 USD | 2,940.00 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 316,870.00 USD | 0.00 USD | 4,560.00 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 312,310.00 USD | 0.00 USD | 7,080.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 305,230.00 USD | 0.00 USD | 231.54 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 305,000.00 USD | 0.00 USD | 109.26 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 304,890.00 USD | 0.00 USD | 1,780.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 303,110.00 USD | 0.00 USD | 51,300.00 USD | `-10.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 251,810.00 USD | 0.00 USD | 250.81 USD | `-10.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 251,560.00 USD | 0.00 USD | 707.78 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 250,850.00 USD | 0.00 USD | 857.85 USD | `-8.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 250,000.00 USD | 0.00 USD | 7,790.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 242,200.00 USD | 0.00 USD | 122.99 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 242,080.00 USD | 0.00 USD | 455.86 USD | `-7.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 241,620.00 USD | 0.00 USD | 10,490.00 USD | `-7.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 231,140.00 USD | 0.00 USD | 1,140.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 229,990.00 USD | 0.00 USD | 877.46 USD | `-6.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 229,110.00 USD | 0.00 USD | 498.04 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 228,620.00 USD | 0.00 USD | 24,640.00 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 203,980.00 USD | 0.00 USD | 269.60 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 203,710.00 USD | 0.00 USD | 13,500.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 190,210.00 USD | 0.00 USD | 1,470.00 USD | `-4.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 188,750.00 USD | 0.00 USD | 336.54 USD | `-4.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 188,410.00 USD | 0.00 USD | 299.74 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 188,110.00 USD | 0.00 USD | 903.60 USD | `-3.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 187,210.00 USD | 0.00 USD | 384.34 USD | `-3.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 186,820.00 USD | 0.00 USD | 125.88 USD | `-2.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 186,690.00 USD | 0.00 USD | 21,990.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 164,700.00 USD | 0.00 USD | 3,370.00 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 161,340.00 USD | 0.00 USD | 2,880.00 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 158,460.00 USD | 0.00 USD | 135,630.00 USD | `-1.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 22,820.00 USD | 0.00 USD | 8,040.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 14,780.00 USD | 0.00 USD | 2,010.00 USD | `-0.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 12,770.00 USD | 0.00 USD | 7,690.00 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `286.50` | 5,080.00 USD | 0.00 USD | 5,080.00 USD | `-0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 175.09 USD | 175.09 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 315.01 USD | 139.92 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 468.44 USD | 153.44 USD | 0.00 USD | `+0.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 1,790.00 USD | 1,320.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 27,070.00 USD | 25,280.00 USD | 0.00 USD | `+1.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 27,480.00 USD | 409.21 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 45,730.00 USD | 18,250.00 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 46,140.00 USD | 407.88 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 118,580.00 USD | 72,450.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 119,160.00 USD | 581.14 USD | 0.00 USD | `+3.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 119,550.00 USD | 388.95 USD | 0.00 USD | `+4.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 129,240.00 USD | 9,690.00 USD | 0.00 USD | `+4.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 140,300.00 USD | 11,060.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 142,950.00 USD | 2,650.00 USD | 0.00 USD | `+6.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `306.50` | 144,010.00 USD | 1,060.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 144,110.00 USD | 102.73 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 158,610.00 USD | 14,500.00 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 159,240.00 USD | 634.04 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 160,270.00 USD | 1,030.00 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 165,920.00 USD | 5,650.00 USD | 0.00 USD | `+11.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `319.50` | 166,040.00 USD | 118.85 USD | 0.00 USD | `+11.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 166,580.00 USD | 534.59 USD | 0.00 USD | `+11.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 166,900.00 USD | 321.50 USD | 0.00 USD | `+12.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 231,820.00 USD | 64,920.00 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 232,910.00 USD | 1,090.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 233,460.00 USD | 547.52 USD | 0.00 USD | `+18.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 233,600.00 USD | 138.20 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 233,850.00 USD | 257.45 USD | 0.00 USD | `+20.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 234,030.00 USD | 174.25 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 234,180.00 USD | 151.50 USD | 0.00 USD | `+22.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 235,630.00 USD | 1,450.00 USD | 0.00 USD | `+24.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 237,410.00 USD | 1,770.00 USD | 0.00 USD | `+25.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 237,730.00 USD | 326.07 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 238,560.00 USD | 826.60 USD | 0.00 USD | `+26.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 246,000.00 USD | 7,440.00 USD | 0.00 USD | `+27.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 246,690.00 USD | 682.84 USD | 0.00 USD | `+28.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 247,780.00 USD | 1,100.00 USD | 0.00 USD | `+33.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 248,470.00 USD | 683.96 USD | 0.00 USD | `+38.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 248,670.00 USD | 199.75 USD | 0.00 USD | `+39.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 252,170.00 USD | 3,500.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 253,210.00 USD | 1,040.00 USD | 0.00 USD | `+41.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 253,580.00 USD | 376.71 USD | 0.00 USD | `+41.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 442,230.00 USD | 188,640.00 USD | 0.00 USD | `+43.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 448,130.00 USD | 5,900.00 USD | 0.00 USD | `+44.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 449,090.00 USD | 960.07 USD | 0.00 USD | `+47.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 450,790.00 USD | 1,700.00 USD | 0.00 USD | `+48.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 452,340.00 USD | 1,550.00 USD | 0.00 USD | `+50.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 453,730.00 USD | 1,380.00 USD | 0.00 USD | `+51.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 454,350.00 USD | 621.14 USD | 0.00 USD | `+52.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 457,720.00 USD | 3,380.00 USD | 0.00 USD | `+53.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 457,950.00 USD | 222.75 USD | 0.00 USD | `+55.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 463,540.00 USD | 5,590.00 USD | 0.00 USD | `+57.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 469,460.00 USD | 5,920.00 USD | 0.00 USD | `+57.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 470,590.00 USD | 1,130.00 USD | 0.00 USD | `+60.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 478,220.00 USD | 7,630.00 USD | 0.00 USD | `+68.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 576,700.00 USD | 98,470.00 USD | 0.00 USD | `+69.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 577,680.00 USD | 981.00 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 578,180.00 USD | 499.50 USD | 0.00 USD | `+74.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,460,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+74.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,470,000.00 USD | 1,000.00 USD | 0.00 USD | `+74.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,470,000.00 USD | 1,040.00 USD | 0.00 USD | `+80.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,470,000.00 USD | 340.67 USD | 0.00 USD | `+82.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,470,000.00 USD | 638.86 USD | 0.00 USD | `+94.02%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `248.50` | 16,070,000.00 USD | 0.00 USD | 16,070,000.00 USD | 34,780.00 USD | 11,250.00 USD | 31,960.00 USD |
| `7D` | `248.90` | 15,990,000.00 USD | 0.00 USD | 15,990,000.00 USD | 14,600.00 USD | 15,640.00 USD | 7,090.00 USD |
| `7D` | `249.30` | 15,960,000.00 USD | 0.00 USD | 15,960,000.00 USD | 16,540.00 USD | 28,020.00 USD | 1,990.00 USD |
| `7D` | `249.70` | 15,910,000.00 USD | 0.00 USD | 15,910,000.00 USD | 50,470.00 USD | 24,180.00 USD | 14,350.00 USD |
| `7D` | `250.10` | 15,820,000.00 USD | 0.00 USD | 15,820,000.00 USD | 45,440.00 USD | 17,650.00 USD | 26,290.00 USD |
| `7D` | `250.50` | 15,730,000.00 USD | 0.00 USD | 15,730,000.00 USD | 9,050.00 USD | 52,840.00 USD | 13,790.00 USD |
| `7D` | `250.90` | 15,660,000.00 USD | 0.00 USD | 15,660,000.00 USD | 25,590.00 USD | 15,530.00 USD | 13,850.00 USD |
| `7D` | `251.30` | 15,600,000.00 USD | 0.00 USD | 15,600,000.00 USD | 32,380.00 USD | 71,570.00 USD | 14,650.00 USD |
| `7D` | `251.70` | 15,480,000.00 USD | 0.00 USD | 15,480,000.00 USD | 50,680.00 USD | 63,110.00 USD | 37,660.00 USD |
| `1D` | `251.90` | 6,440,000.00 USD | 0.00 USD | 6,440,000.00 USD | 36,290.00 USD | 46,740.00 USD | 31,050.00 USD |
| `7D` | `252.10` | 15,330,000.00 USD | 0.00 USD | 15,330,000.00 USD | 62,800.00 USD | 22,650.00 USD | 23,560.00 USD |
| `1D` | `252.30` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 13,370.00 USD | 7,400.00 USD | 5,650.00 USD |
| `7D` | `252.50` | 15,220,000.00 USD | 0.00 USD | 15,220,000.00 USD | 54,060.00 USD | 27,550.00 USD | 17,690.00 USD |
| `1D` | `252.70` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 12,500.00 USD | 5,720.00 USD | 4,140.00 USD |
| `7D` | `252.90` | 15,120,000.00 USD | 0.00 USD | 15,120,000.00 USD | 13,480.00 USD | 19,580.00 USD | 56.67 USD |
| `1D` | `253.10` | 6,280,000.00 USD | 0.00 USD | 6,280,000.00 USD | 9,570.00 USD | 11,880.00 USD | 2,320.00 USD |
| `7D` | `253.30` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 29,860.00 USD | 36,720.00 USD | 20,250.00 USD |
| `1D` | `253.50` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 19,030.00 USD | 13,820.00 USD | 9,210.00 USD |
| `7D` | `253.70` | 15,000,000.00 USD | 0.00 USD | 15,000,000.00 USD | 4,870.00 USD | 30,670.00 USD | 28,010.00 USD |
| `1D` | `253.90` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 0.00 USD | 8,890.00 USD | 9,560.00 USD |
| `7D` | `254.10` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 24,240.00 USD | 35,210.00 USD | 21,950.00 USD |
| `1D` | `254.30` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 144.00 USD | 2,130.00 USD | 4.60 USD |
| `7D` | `254.50` | 14,860,000.00 USD | 0.00 USD | 14,860,000.00 USD | 32,120.00 USD | 14,400.00 USD | 16,400.00 USD |
| `1D` | `254.70` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 431.32 USD | 2,050.00 USD | 2,770.00 USD |
| `7D` | `254.90` | 14,800,000.00 USD | 0.00 USD | 14,800,000.00 USD | 14,160.00 USD | 6,640.00 USD | 5,610.00 USD |
| `1D` | `255.10` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 9,680.00 USD | 6,590.00 USD | 0.00 USD |
| `7D` | `255.30` | 14,770,000.00 USD | 0.00 USD | 14,770,000.00 USD | 47,460.00 USD | 10,560.00 USD | 34,510.00 USD |
| `1D` | `255.50` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD |
| `7D` | `255.70` | 14,680,000.00 USD | 0.00 USD | 14,680,000.00 USD | 19,690.00 USD | 13,320.00 USD | 49,670.00 USD |
| `1D` | `255.90` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 13,380.00 USD | 2,180.00 USD | 0.00 USD |
| `7D` | `256.10` | 14,590,000.00 USD | 0.00 USD | 14,590,000.00 USD | 53,510.00 USD | 24,190.00 USD | 14,170.00 USD |
| `1D` | `256.30` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 8,660.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `256.50` | 14,500,000.00 USD | 0.00 USD | 14,500,000.00 USD | 36,010.00 USD | 15,360.00 USD | 27,700.00 USD |
| `1D` | `256.70` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 8,340.00 USD | 0.00 USD | 3.61 USD |
| `7D` | `256.90` | 14,420,000.00 USD | 0.00 USD | 14,420,000.00 USD | 45,670.00 USD | 15,920.00 USD | 31,430.00 USD |
| `1D` | `257.10` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 4,210.00 USD | 638.00 USD | 3,420.00 USD |
| `7D` | `257.30` | 14,330,000.00 USD | 0.00 USD | 14,330,000.00 USD | 23,000.00 USD | 1,200.00 USD | 27,270.00 USD |
| `1D` | `257.50` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 32.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `257.70` | 14,280,000.00 USD | 0.00 USD | 14,280,000.00 USD | 46,990.00 USD | 6,040.00 USD | 18,260.00 USD |
| `1D` | `257.90` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 2,050.00 USD | 2,390.00 USD | 12,620.00 USD |
| `7D` | `258.10` | 14,210,000.00 USD | 0.00 USD | 14,210,000.00 USD | 72,040.00 USD | 39,870.00 USD | 30,880.00 USD |
| `1D` | `258.30` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 3,110.00 USD | 8,380.00 USD | 13,220.00 USD |
| `7D` | `258.50` | 14,060,000.00 USD | 0.00 USD | 14,060,000.00 USD | 109,750.00 USD | 15,580.00 USD | 20,950.00 USD |
| `1D` | `258.70` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 2,100.00 USD | 3,080.00 USD | 10,750.00 USD |
| `7D` | `258.90` | 13,920,000.00 USD | 0.00 USD | 13,920,000.00 USD | 20,250.00 USD | 2,350.00 USD | 34,410.00 USD |
| `1D` | `259.10` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 13,250.00 USD | 7,870.00 USD | 17,540.00 USD |
| `7D` | `259.30` | 13,860,000.00 USD | 0.00 USD | 13,860,000.00 USD | 3,650.00 USD | 43,790.00 USD | 8,080.00 USD |
| `1D` | `259.50` | 6,000,000.00 USD | 0.00 USD | 6,000,000.00 USD | 4,620.00 USD | 4,690.00 USD | 7,180.00 USD |
| `7D` | `259.70` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 17,070.00 USD | 13,060.00 USD | 157.61 USD |
| `1D` | `259.90` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 19,490.00 USD | 17,870.00 USD | 26,940.00 USD |
| `7D` | `260.10` | 13,780,000.00 USD | 0.00 USD | 13,780,000.00 USD | 23,940.00 USD | 8,310.00 USD | 8,870.00 USD |
| `1D` | `260.30` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 3,100.00 USD | 9,490.00 USD | 7,690.00 USD |
| `7D` | `260.50` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 6,310.00 USD | 29,760.00 USD | 22,300.00 USD |
| `1D` | `260.70` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 5,040.00 USD | 15,080.00 USD | 17,340.00 USD |
| `7D` | `260.90` | 13,680,000.00 USD | 0.00 USD | 13,680,000.00 USD | 17,580.00 USD | 31,940.00 USD | 37,850.00 USD |
| `1D` | `261.10` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 12,720.00 USD | 6,860.00 USD | 6,680.00 USD |
| `7D` | `261.30` | 13,590,000.00 USD | 0.00 USD | 13,590,000.00 USD | 1,980.00 USD | 33,470.00 USD | 16,080.00 USD |
| `1D` | `261.50` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 8,750.00 USD | 14,260.00 USD | 9.26 USD |
| `7D` | `261.70` | 13,540,000.00 USD | 0.00 USD | 13,540,000.00 USD | 24,930.00 USD | 50,340.00 USD | 19,890.00 USD |
| `1D` | `261.90` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 4,770.00 USD | 4,240.00 USD | 8,340.00 USD |
| `7D` | `262.10` | 13,440,000.00 USD | 0.00 USD | 13,440,000.00 USD | 60,340.00 USD | 34,480.00 USD | 32,810.00 USD |
| `1D` | `262.30` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 8,640.00 USD | 765.45 USD | 5,590.00 USD |
| `7D` | `262.50` | 13,310,000.00 USD | 0.00 USD | 13,310,000.00 USD | 35,770.00 USD | 26,590.00 USD | 79.25 USD |
| `1D` | `262.70` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 366.04 USD | 1,340.00 USD | 7.87 USD |
| `7D` | `262.90` | 13,250,000.00 USD | 0.00 USD | 13,250,000.00 USD | 66,900.00 USD | 33,480.00 USD | 32,750.00 USD |
| `1D` | `263.10` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 8,670.00 USD | 571.81 USD | 7,500.00 USD |
| `7D` | `263.30` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 32,470.00 USD | 22,930.00 USD | 39,120.00 USD |
| `1D` | `263.50` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 560.34 USD | 839.81 USD | 24,820.00 USD |
| `7D` | `263.70` | 13,020,000.00 USD | 0.00 USD | 13,020,000.00 USD | 265,940.00 USD | 96,750.00 USD | 26,970.00 USD |
| `1D` | `263.90` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 746.44 USD | 825.92 USD | 6.64 USD |
| `7D` | `264.10` | 12,630,000.00 USD | 0.00 USD | 12,630,000.00 USD | 93,540.00 USD | 34,830.00 USD | 41,900.00 USD |
| `1D` | `264.30` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 1,860.00 USD | 647.93 USD | 12.10 USD |
| `7D` | `264.50` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 49,620.00 USD | 15,600.00 USD | 37,300.00 USD |
| `1D` | `264.70` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 28,300.00 USD | 615.20 USD | 36,610.00 USD |
| `7D` | `264.90` | 12,360,000.00 USD | 0.00 USD | 12,360,000.00 USD | 22,920.00 USD | 75,900.00 USD | 16,010.00 USD |
| `1D` | `265.10` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 20,540.00 USD | 8,870.00 USD | 15,620.00 USD |
| `7D` | `265.30` | 12,250,000.00 USD | 0.00 USD | 12,250,000.00 USD | 111,680.00 USD | 43,610.00 USD | 103,040.00 USD |
| `1D` | `265.50` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 9,760.00 USD | 11,810.00 USD | 67,100.00 USD |
| `7D` | `265.70` | 11,990,000.00 USD | 0.00 USD | 11,990,000.00 USD | 54,220.00 USD | 77,170.00 USD | 46,110.00 USD |
| `1D` | `265.90` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 14,110.00 USD | 11,850.00 USD | 23.68 USD |
| `7D` | `266.10` | 11,810,000.00 USD | 0.00 USD | 11,810,000.00 USD | 156,170.00 USD | 142,000.00 USD | 57,620.00 USD |
| `1D` | `266.30` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 32,850.00 USD | 115.00 USD | 5,010.00 USD |
| `7D` | `266.50` | 11,460,000.00 USD | 0.00 USD | 11,460,000.00 USD | 112,390.00 USD | 71,170.00 USD | 105,340.00 USD |
| `1D` | `266.70` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 15,000.00 USD | 3,260.00 USD | 3,710.00 USD |
| `7D` | `266.90` | 11,170,000.00 USD | 0.00 USD | 11,170,000.00 USD | 138,720.00 USD | 162,640.00 USD | 59,260.00 USD |
| `1D` | `267.10` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 28,570.00 USD | 6,830.00 USD | 10,110.00 USD |
| `7D` | `267.30` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 112,040.00 USD | 158,320.00 USD | 88,930.00 USD |
| `1D` | `267.50` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 12,110.00 USD | 26,770.00 USD | 14.03 USD |
| `7D` | `267.70` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 171,250.00 USD | 208,600.00 USD | 62,640.00 USD |
| `1D` | `267.90` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 113,020.00 USD | 120,830.00 USD | 45,390.00 USD |
| `7D` | `268.10` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 109,270.00 USD | 282,670.00 USD | 99,390.00 USD |
| `1D` | `268.30` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 39,220.00 USD | 98,210.00 USD | 26,530.00 USD |
| `7D` | `268.50` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 200,320.00 USD | 140,090.00 USD | 76,180.00 USD |
| `1D` | `268.70` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 97,080.00 USD | 85,050.00 USD | 58,770.00 USD |
| `7D` | `268.90` | 9,100,000.00 USD | 0.00 USD | 9,100,000.00 USD | 199,940.00 USD | 108,260.00 USD | 92,260.00 USD |
| `1D` | `269.10` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 50,070.00 USD | 22,990.00 USD | 16,370.00 USD |
| `7D` | `269.30` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 280,160.00 USD | 180,180.00 USD | 85,230.00 USD |
| `1D` | `269.50` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 31,770.00 USD | 6,100.00 USD | 8,710.00 USD |
| `7D` | `269.70` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 55,620.00 USD | 87,030.00 USD | 10,350.00 USD |
| `1D` | `269.90` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 33,260.00 USD | 43,730.00 USD | 12,980.00 USD |
| `7D` | `270.10` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 143,830.00 USD | 168,260.00 USD | 98,490.00 USD |
| `1D` | `270.30` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 118,580.00 USD | 64,760.00 USD | 128,910.00 USD |
| `7D` | `270.50` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 79,840.00 USD | 98,970.00 USD | 214,580.00 USD |
| `1D` | `270.70` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 56,530.00 USD | 44,280.00 USD | 15,700.00 USD |
| `7D` | `270.90` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 275,900.00 USD | 144,560.00 USD | 90,040.00 USD |
| `1D` | `271.10` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 40,150.00 USD | 39,050.00 USD | 149,680.00 USD |
| `7D` | `271.30` | 6,680,000.00 USD | 0.00 USD | 6,680,000.00 USD | 115,810.00 USD | 124,290.00 USD | 39,340.00 USD |
| `1D` | `271.50` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 27,990.00 USD | 39,010.00 USD | 0.00 USD |
| `7D` | `271.70` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 379,860.00 USD | 47,170.00 USD | 77,220.00 USD |
| `1D` | `271.90` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 93,920.00 USD | 23,970.00 USD | 16,940.00 USD |
| `7D` | `272.10` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 257,880.00 USD | 75,080.00 USD | 148,690.00 USD |
| `1D` | `272.30` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 66,270.00 USD | 9,560.00 USD | 17,040.00 USD |
| `7D` | `272.50` | 5,420,000.00 USD | 0.00 USD | 5,420,000.00 USD | 157,320.00 USD | 168,270.00 USD | 31,360.00 USD |
| `1D` | `272.70` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 67,250.00 USD | 29,700.00 USD | 21,920.00 USD |
| `7D` | `272.90` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 151,480.00 USD | 204,910.00 USD | 83,450.00 USD |
| `1D` | `273.10` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 89,600.00 USD | 81,790.00 USD | 6,980.00 USD |
| `7D` | `273.30` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 282,200.00 USD | 241,130.00 USD | 163,370.00 USD |
| `1D` | `273.50` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 225,140.00 USD | 235,090.00 USD | 90,150.00 USD |
| `7D` | `273.70` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 195,450.00 USD | 467,590.00 USD | 206,110.00 USD |
| `1D` | `273.90` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 88,320.00 USD | 196,260.00 USD | 53,030.00 USD |
| `7D` | `274.10` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 455,510.00 USD | 217,100.00 USD | 178,110.00 USD |
| `1D` | `274.30` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 204,120.00 USD | 170,140.00 USD | 126,070.00 USD |
| `7D` | `274.50` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 345,450.00 USD | 165,040.00 USD | 94,750.00 USD |
| `1D` | `274.70` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 101,740.00 USD | 43,050.00 USD | 53,530.00 USD |
| `7D` | `274.90` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 260,340.00 USD | 167,590.00 USD | 90,760.00 USD |
| `1D` | `275.10` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 68,880.00 USD | 21,290.00 USD | 48,930.00 USD |
| `7D` | `275.30` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 2,800.00 USD | 101,100.00 USD | 40,450.00 USD |
| `1D` | `275.50` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 63,860.00 USD | 65,590.00 USD | 39,040.00 USD |
| `7D` | `275.70` | 945,540.00 USD | 0.00 USD | 945,540.00 USD | 1,350.00 USD | 51,050.00 USD | 60.63 USD |
| `1D` | `275.90` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 73,380.00 USD | 51,470.00 USD | 22,040.00 USD |
| `7D` | `276.10` | 893,080.00 USD | 0.00 USD | 893,080.00 USD | 3,750.00 USD | 0.00 USD | 29.51 USD |
| `1D` | `276.30` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 68,110.00 USD | 53,790.00 USD | 31,400.00 USD |
| `7D` | `276.50` | 889,300.00 USD | 0.00 USD | 889,300.00 USD | 485.90 USD | 0.00 USD | 17.12 USD |
| `1D` | `276.70` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 27,390.00 USD | 32,060.00 USD | 44,570.00 USD |
| `7D` | `276.90` | 888,790.00 USD | 0.00 USD | 888,790.00 USD | 45,560.00 USD | 23,180.00 USD | 19,960.00 USD |
| `1D` | `277.10` | 906,780.00 USD | 0.00 USD | 906,780.00 USD | 19,010.00 USD | 68,080.00 USD | 67,920.00 USD |
| `7D` | `277.30` | 800,100.00 USD | 0.00 USD | 800,100.00 USD | 0.00 USD | 63,290.00 USD | 88.05 USD |
| `1D` | `277.50` | 751,760.00 USD | 0.00 USD | 751,760.00 USD | 74,620.00 USD | 55,090.00 USD | 17,160.00 USD |
| `7D` | `277.70` | 736,720.00 USD | 0.00 USD | 736,720.00 USD | 0.00 USD | 27,190.00 USD | 84,310.00 USD |
| `1D` | `277.90` | 604,890.00 USD | 0.00 USD | 604,890.00 USD | 12,650.00 USD | 9,490.00 USD | 23,940.00 USD |
| `7D` | `278.10` | 625,220.00 USD | 0.00 USD | 625,220.00 USD | 24,750.00 USD | 0.00 USD | 59,450.00 USD |
| `1D` | `278.30` | 558,800.00 USD | 0.00 USD | 558,800.00 USD | 61,240.00 USD | 25,470.00 USD | 57,330.00 USD |
| `7D` | `278.50` | 541,020.00 USD | 0.00 USD | 541,020.00 USD | 17,440.00 USD | 71,230.00 USD | 33.20 USD |
| `1D` | `278.70` | 414,760.00 USD | 0.00 USD | 414,760.00 USD | 26,540.00 USD | 35,300.00 USD | 10,340.00 USD |
| `7D` | `278.90` | 452,310.00 USD | 0.00 USD | 452,310.00 USD | 42,950.00 USD | 32,690.00 USD | 17,150.00 USD |
| `1D` | `279.10` | 342,580.00 USD | 0.00 USD | 342,580.00 USD | 29,260.00 USD | 23,330.00 USD | 23,180.00 USD |
| `7D` | `279.30` | 359,520.00 USD | 0.00 USD | 359,520.00 USD | 31,330.00 USD | 0.00 USD | 41,620.00 USD |
| `1D` | `279.50` | 266,790.00 USD | 0.00 USD | 266,790.00 USD | 28,380.00 USD | 10,290.00 USD | 34,800.00 USD |
| `7D` | `279.70` | 286,570.00 USD | 0.00 USD | 286,570.00 USD | 46,800.00 USD | 0.00 USD | 54,370.00 USD |
| `1D` | `279.90` | 193,320.00 USD | 0.00 USD | 193,320.00 USD | 20,320.00 USD | 0.00 USD | 17,110.00 USD |
| `7D` | `280.10` | 185,400.00 USD | 0.00 USD | 185,400.00 USD | 0.00 USD | 0.00 USD | 65.52 USD |
| `1D` | `280.30` | 155,900.00 USD | 0.00 USD | 155,900.00 USD | 29,750.00 USD | 0.00 USD | 41,630.00 USD |
| `1D` | `280.70` | 84,510.00 USD | 0.00 USD | 84,510.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD |
| `7D` | `280.90` | 185,340.00 USD | 0.00 USD | 185,340.00 USD | 0.00 USD | 0.00 USD | 80.88 USD |
| `7D` | `281.30` | 185,260.00 USD | 0.00 USD | 185,260.00 USD | 0.00 USD | 0.00 USD | 62,860.00 USD |
| `7D` | `281.70` | 122,390.00 USD | 0.00 USD | 122,390.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `7D` | `282.10` | 133,780.00 USD | 133,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 133,780.00 USD |
| `7D` | `282.10` | 267,570.00 USD | 267,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 133,780.00 USD |
| `7D` | `282.50` | 339,480.00 USD | 339,480.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 39,720.00 USD |
| `1D` | `282.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.90` | 339,520.00 USD | 339,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 42.40 USD |
| `1D` | `283.10` | 250,340.00 USD | 250,340.00 USD | 0.00 USD | 71,390.00 USD | 0.00 USD | 178,950.00 USD |
| `7D` | `283.30` | 466,100.00 USD | 466,100.00 USD | 0.00 USD | 0.00 USD | 37,310.00 USD | 89,270.00 USD |
| `1D` | `283.50` | 331,190.00 USD | 331,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 80,840.00 USD |
| `7D` | `283.70` | 704,960.00 USD | 704,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238,860.00 USD |
| `1D` | `283.90` | 400,450.00 USD | 400,450.00 USD | 0.00 USD | 0.00 USD | 30,480.00 USD | 38,790.00 USD |
| `7D` | `284.10` | 890,350.00 USD | 890,350.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 135,900.00 USD |
| `1D` | `284.30` | 515,950.00 USD | 515,950.00 USD | 0.00 USD | 37,810.00 USD | 46,830.00 USD | 30,860.00 USD |
| `7D` | `284.50` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 26,130.00 USD | 198,780.00 USD | 34,150.00 USD |
| `1D` | `284.70` | 639,360.00 USD | 639,360.00 USD | 0.00 USD | 48,190.00 USD | 54,540.00 USD | 20,690.00 USD |
| `7D` | `284.90` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 282,130.00 USD | 0.00 USD |
| `1D` | `285.10` | 743,160.00 USD | 743,160.00 USD | 0.00 USD | 20,960.00 USD | 20,580.00 USD | 62,250.00 USD |
| `7D` | `285.30` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 62,660.00 USD | 143,940.00 USD | 83,240.00 USD |
| `1D` | `285.50` | 969,000.00 USD | 969,000.00 USD | 0.00 USD | 91,500.00 USD | 95,280.00 USD | 39,050.00 USD |
| `7D` | `285.70` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 113,640.00 USD | 0.00 USD |
| `1D` | `285.90` | 988,890.00 USD | 988,890.00 USD | 0.00 USD | 0.00 USD | 19,890.00 USD | 0.00 USD |
| `7D` | `286.10` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 74,850.00 USD | 0.00 USD |
| `7D` | `286.50` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 23,860.00 USD | 95,580.00 USD | 0.00 USD |
| `7D` | `286.90` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 27,530.00 USD | 141,160.00 USD | 3.84 USD |
| `1D` | `287.10` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 20,810.00 USD | 117,540.00 USD | 80,690.00 USD |
| `7D` | `287.30` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 53,620.00 USD | 86,570.00 USD | 0.00 USD |
| `1D` | `287.50` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 20,250.00 USD | 28,170.00 USD |
| `7D` | `287.70` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 0.00 USD | 154,260.00 USD | 0.00 USD |
| `1D` | `287.90` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 9,030.00 USD | 10,410.00 USD | 19,620.00 USD |
| `7D` | `288.10` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 139,290.00 USD | 0.00 USD |
| `1D` | `288.70` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 4.82 USD |
| `1D` | `289.10` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 11,990.00 USD | 0.00 USD |
| `1D` | `289.50` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 2.04 USD |
| `7D` | `289.70` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 0.00 USD | 1,870.00 USD | 0.00 USD |
| `1D` | `291.10` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3.78 USD |
| `7D` | `291.30` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 0.00 USD | 9,250.00 USD | 0.00 USD |
| `1D` | `291.50` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 21,970.00 USD | 5.34 USD |
| `7D` | `291.70` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 0.00 USD | 94,090.00 USD | 0.00 USD |
| `1D` | `291.90` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 5,920.00 USD | 22,130.00 USD |
| `7D` | `292.10` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 118,660.00 USD | 0.00 USD |
| `1D` | `292.30` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 13,260.00 USD | 61,180.00 USD | 8,110.00 USD |
| `7D` | `292.50` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 26,610.00 USD | 68.66 USD |
| `1D` | `292.70` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 19,680.00 USD | 98,000.00 USD | 5.74 USD |
| `7D` | `292.90` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 118,480.00 USD | 1.54 USD |
| `1D` | `293.10` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 10,710.00 USD | 41,110.00 USD | 0.42 USD |
| `7D` | `293.30` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 1.34 USD |
| `1D` | `293.50` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 18,740.00 USD | 55,160.00 USD | 23,910.00 USD |
| `7D` | `293.70` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 37,280.00 USD | 1,170.00 USD | 63.74 USD |
| `1D` | `293.90` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 88,090.00 USD | 36,570.00 USD | 93,370.00 USD |
| `7D` | `294.10` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 85,150.00 USD | 33,590.00 USD | 105,650.00 USD |
| `1D` | `294.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 49,730.00 USD | 75,940.00 USD | 56,630.00 USD |
| `7D` | `294.50` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 69,950.00 USD | 15,030.00 USD | 0.00 USD |
| `1D` | `294.70` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 133,430.00 USD | 96,720.00 USD | 168,940.00 USD |
| `7D` | `294.90` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 63,470.00 USD | 92,770.00 USD | 104,870.00 USD |
| `1D` | `295.10` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 32,330.00 USD | 64,690.00 USD | 73,420.00 USD |
| `7D` | `295.30` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 45,590.00 USD | 65,580.00 USD | 252,150.00 USD |
| `1D` | `295.50` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 61,560.00 USD | 105,870.00 USD | 68,320.00 USD |
| `7D` | `295.70` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 105,410.00 USD | 72,570.00 USD | 133,230.00 USD |
| `1D` | `295.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 105,350.00 USD | 37,180.00 USD | 33,300.00 USD |
| `7D` | `296.10` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 75,740.00 USD | 90,470.00 USD | 119,070.00 USD |
| `1D` | `296.30` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 88,010.00 USD | 95,560.00 USD | 27,140.00 USD |
| `7D` | `296.50` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 2,060.00 USD | 77,140.00 USD | 57,010.00 USD |
| `1D` | `296.70` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 34,010.00 USD | 39,270.00 USD | 62,270.00 USD |
| `7D` | `296.90` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 206,840.00 USD | 50,620.00 USD | 134,620.00 USD |
| `1D` | `297.10` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 52,650.00 USD | 177.11 USD | 36,490.00 USD |
| `7D` | `297.30` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 3,960.00 USD | 2,500.00 USD | 51.49 USD |
| `1D` | `297.50` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 6,280.00 USD | 939.55 USD | 20,820.00 USD |
| `7D` | `297.70` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 144.38 USD | 56,790.00 USD | 34,690.00 USD |
| `1D` | `297.90` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 1,150.00 USD | 9,340.00 USD | 16,110.00 USD |
| `7D` | `298.10` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 49,240.00 USD | 81,680.00 USD | 54,880.00 USD |
| `1D` | `298.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 55,160.00 USD | 8,520.00 USD | 137,670.00 USD |
| `7D` | `298.50` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 12,660.00 USD | 47,990.00 USD |
| `1D` | `298.70` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 29,410.00 USD | 13,250.00 USD | 80,710.00 USD |
| `7D` | `298.90` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 70,090.00 USD | 993.25 USD | 39,930.00 USD |
| `1D` | `299.10` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 7,660.00 USD | 16,030.00 USD | 35,250.00 USD |
| `7D` | `299.30` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 2,570.00 USD | 1,380.00 USD | 45,900.00 USD |
| `1D` | `299.50` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 35,750.00 USD | 23,680.00 USD | 43,830.00 USD |
| `7D` | `299.70` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 5,310.00 USD | 7,720.00 USD | 19,890.00 USD |
| `1D` | `299.90` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 20,860.00 USD | 22,550.00 USD | 24,860.00 USD |
| `7D` | `300.10` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 51,500.00 USD | 2,470.00 USD | 13.40 USD |
| `1D` | `300.30` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 48,160.00 USD | 32,910.00 USD | 42,620.00 USD |
| `7D` | `300.50` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 866.20 USD | 36,230.00 USD | 19,780.00 USD |
| `1D` | `300.70` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 20,250.00 USD | 37,920.00 USD | 52,590.00 USD |
| `7D` | `300.90` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 24,730.00 USD | 34,630.00 USD | 84,540.00 USD |
| `1D` | `301.10` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 15,450.00 USD | 28,660.00 USD | 26,000.00 USD |
| `7D` | `301.30` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 71,890.00 USD | 55,420.00 USD | 94,650.00 USD |
| `1D` | `301.50` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 31,390.00 USD | 24,180.00 USD | 44,040.00 USD |
| `7D` | `301.70` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 37,640.00 USD | 130,520.00 USD | 68.18 USD |
| `1D` | `301.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 29,910.00 USD | 47,960.00 USD | 11,580.00 USD |
| `7D` | `302.10` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 53,220.00 USD | 123,390.00 USD | 26,220.00 USD |
| `1D` | `302.30` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 5,320.00 USD | 12,280.00 USD | 10,300.00 USD |
| `7D` | `302.50` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 31,330.00 USD | 102,200.00 USD | 41,840.00 USD |
| `1D` | `302.70` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 11,520.00 USD | 11,480.00 USD | 34,810.00 USD |
| `7D` | `302.90` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 40,380.00 USD | 65,280.00 USD | 57.15 USD |
| `1D` | `303.10` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 20,770.00 USD | 1,270.00 USD | 14,650.00 USD |
| `7D` | `303.30` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 385.62 USD |
| `1D` | `303.50` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 11,460.00 USD | 232.42 USD | 6,260.00 USD |
| `7D` | `303.70` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 17,370.00 USD | 8,710.00 USD | 24,480.00 USD |
| `1D` | `303.90` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 29,930.00 USD | 3,900.00 USD | 18,760.00 USD |
| `7D` | `304.10` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 5,440.00 USD | 1,950.00 USD | 43.01 USD |
| `1D` | `304.30` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 4,310.00 USD | 5,170.00 USD | 48,500.00 USD |
| `7D` | `304.50` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 3,480.00 USD | 11,110.00 USD | 55.84 USD |
| `1D` | `304.70` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 9,700.00 USD | 4,830.00 USD | 40,350.00 USD |
| `7D` | `304.90` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 34,680.00 USD | 18,990.00 USD | 8,360.00 USD |
| `1D` | `305.10` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 9,410.00 USD | 249.40 USD | 2,010.00 USD |
| `7D` | `305.30` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 162,420.00 USD | 124,800.00 USD | 117,060.00 USD |
| `1D` | `305.50` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 4,670.00 USD | 1,640.00 USD | 1,500.00 USD |
| `7D` | `305.70` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 82,270.00 USD | 18,170.00 USD | 12,830.00 USD |
| `1D` | `305.90` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 9,360.00 USD | 2,720.00 USD | 1,940.00 USD |
| `7D` | `306.10` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 22,930.00 USD | 67,820.00 USD | 46,110.00 USD |
| `1D` | `306.30` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 3,900.00 USD | 3,200.00 USD | 1,400.00 USD |
| `7D` | `306.50` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 30,150.00 USD | 41,830.00 USD | 65,800.00 USD |
| `1D` | `306.70` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 4,480.00 USD | 21,600.00 USD | 3,840.00 USD |
| `7D` | `306.90` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 58,810.00 USD | 50,570.00 USD | 57,630.00 USD |
| `1D` | `307.10` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 33,080.00 USD | 42,120.00 USD | 13,710.00 USD |
| `7D` | `307.30` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 27,410.00 USD | 123,720.00 USD | 83,360.00 USD |
| `1D` | `307.50` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 6,340.00 USD | 22,280.00 USD | 9,450.00 USD |
| `7D` | `307.70` | 8,390,000.00 USD | 8,390,000.00 USD | 0.00 USD | 84,930.00 USD | 74,370.00 USD | 23,930.00 USD |
| `1D` | `307.90` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 33,320.00 USD | 30,540.00 USD | 21,620.00 USD |
| `7D` | `308.10` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 105,700.00 USD | 63,640.00 USD | 101,100.00 USD |
| `1D` | `308.30` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 13,940.00 USD | 7,490.00 USD | 5,650.00 USD |
| `7D` | `308.50` | 8,910,000.00 USD | 8,910,000.00 USD | 0.00 USD | 118,090.00 USD | 64,440.00 USD | 65,480.00 USD |
| `1D` | `308.70` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 5,550.00 USD | 387.08 USD | 3,480.00 USD |
| `7D` | `308.90` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 60,660.00 USD | 31,940.00 USD | 19,680.00 USD |
| `1D` | `309.10` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 12,160.00 USD | 6,430.00 USD | 2,980.00 USD |
| `7D` | `309.30` | 9,110,000.00 USD | 9,110,000.00 USD | 0.00 USD | 27,540.00 USD | 26,240.00 USD | 36,540.00 USD |
| `1D` | `309.50` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 16,550.00 USD | 22,930.00 USD | 8,230.00 USD |
| `7D` | `309.70` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 40,410.00 USD | 132,660.00 USD | 146,820.00 USD |
| `1D` | `309.90` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 8,640.00 USD | 2,590.00 USD | 974.67 USD |
| `7D` | `310.10` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 34,250.00 USD | 63,360.00 USD | 62,760.00 USD |
| `1D` | `310.30` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 8,890.00 USD | 9,560.00 USD |
| `7D` | `310.50` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 64,060.00 USD | 73,280.00 USD | 22,030.00 USD |
| `1D` | `310.70` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 144.00 USD | 2,370.00 USD | 8.56 USD |
| `7D` | `310.90` | 9,820,000.00 USD | 9,820,000.00 USD | 0.00 USD | 35,670.00 USD | 30,720.00 USD | 3,940.00 USD |
| `1D` | `311.10` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 134.35 USD | 2,050.00 USD | 3.19 USD |
| `7D` | `311.30` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 84,180.00 USD | 65,480.00 USD | 47,620.00 USD |
| `1D` | `311.50` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 7,390.00 USD | 6,590.00 USD | 2,760.00 USD |
| `7D` | `311.70` | 10,080,000.00 USD | 10,080,000.00 USD | 0.00 USD | 25,530.00 USD | 11,430.00 USD | 24,310.00 USD |
| `1D` | `311.90` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 4.14 USD |
| `7D` | `312.10` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 46,850.00 USD | 1,100.00 USD | 24,240.00 USD |
| `1D` | `312.30` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 6,410.00 USD | 5,330.00 USD | 2,760.00 USD |
| `7D` | `312.50` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 19,540.00 USD | 22,460.00 USD | 49,690.00 USD |
| `1D` | `312.70` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 13,380.00 USD | 2,180.00 USD | 0.00 USD |
| `7D` | `312.90` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 22,600.00 USD | 20,090.00 USD | 29,930.00 USD |
| `1D` | `313.10` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 5,080.00 USD | 1,940.00 USD | 0.96 USD |
| `7D` | `313.30` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 64,910.00 USD | 30,120.00 USD | 22,640.00 USD |
| `1D` | `313.50` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 7,160.00 USD | 4,770.00 USD | 2,580.00 USD |
| `7D` | `313.70` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 32,170.00 USD | 15,010.00 USD | 23,160.00 USD |
| `1D` | `313.90` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 4,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `314.10` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 26,810.00 USD | 362.37 USD | 47,790.00 USD |
| `1D` | `314.30` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.50` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 48,630.00 USD | 307.60 USD | 24,570.00 USD |
| `1D` | `314.70` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 32.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `314.90` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 29,590.00 USD | 0.00 USD | 10,270.00 USD |
| `1D` | `315.10` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 32.50 USD | 1,400.00 USD | 6,450.00 USD |
| `7D` | `315.30` | 10,700,000.00 USD | 10,700,000.00 USD | 0.00 USD | 5,690.00 USD | 547.95 USD | 156.75 USD |
| `1D` | `315.50` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 3,750.00 USD | 3,270.00 USD | 19,390.00 USD |
| `7D` | `315.70` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 9,200.00 USD | 50,270.00 USD | 48,090.00 USD |
| `1D` | `315.90` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 3,360.00 USD | 5,260.00 USD | 43.60 USD |
| `7D` | `316.10` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,430.00 USD |
| `1D` | `316.30` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 128.70 USD | 3,070.00 USD | 10,700.00 USD |
| `7D` | `316.50` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 16,120.00 USD | 20,630.00 USD | 18,360.00 USD |
| `1D` | `316.70` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 13,180.00 USD | 6,830.00 USD | 17,540.00 USD |
| `7D` | `316.90` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 123.95 USD |
| `1D` | `317.10` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 3,940.00 USD | 4,470.00 USD | 7,170.00 USD |
| `7D` | `317.30` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 14,540.00 USD | 748.91 USD | 41.62 USD |
| `1D` | `317.50` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 11,570.00 USD | 14,470.00 USD | 17,050.00 USD |
| `7D` | `317.70` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 620.15 USD | 265.17 USD | 129.73 USD |
| `1D` | `317.90` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 7,000.00 USD | 9,190.00 USD | 16,750.00 USD |
| `7D` | `318.10` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 22,250.00 USD | 9,100.00 USD | 29.19 USD |
| `1D` | `318.30` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 2,200.00 USD | 8,470.00 USD | 10,400.00 USD |
| `7D` | `318.50` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 3,010.00 USD | 26,630.00 USD | 36,350.00 USD |
| `1D` | `318.70` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 4,470.00 USD | 9,400.00 USD | 7,760.00 USD |
| `7D` | `318.90` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 10,270.00 USD | 17,970.00 USD | 23,850.00 USD |
| `1D` | `319.10` | 5,710,000.00 USD | 5,710,000.00 USD | 0.00 USD | 12,470.00 USD | 6,750.00 USD | 6,660.00 USD |
| `7D` | `319.30` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 0.00 USD | 18,060.00 USD | 0.00 USD |
| `1D` | `319.50` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 8,400.00 USD | 10,930.00 USD | 0.00 USD |
| `7D` | `319.70` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `1D` | `319.80` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD |
| `7D` | `320.10` | 11,250,000.00 USD | 11,250,000.00 USD | 0.00 USD | 34,670.00 USD | 9,520.00 USD | 30,570.00 USD |
| `7D` | `320.50` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 15,190.00 USD | 10,080.00 USD | 40.83 USD |
| `7D` | `320.90` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.30` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 9,210.00 USD | 8,760.00 USD | 5,950.00 USD |
| `7D` | `321.70` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 4,780.00 USD | 9,110.00 USD | 15,090.00 USD |
| `7D` | `322.10` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 22,940.00 USD | 8,290.00 USD | 6,200.00 USD |
| `7D` | `322.50` | 11,370,000.00 USD | 11,370,000.00 USD | 0.00 USD | 555.20 USD | 365.55 USD | 0.00 USD |
| `7D` | `322.90` | 11,390,000.00 USD | 11,390,000.00 USD | 0.00 USD | 16,590.00 USD | 5,630.00 USD | 0.00 USD |
| `7D` | `323.30` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 14,160.00 USD | 5,860.00 USD | 11,480.00 USD |
| `7D` | `323.70` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 269.10 USD | 6,780.00 USD | 0.00 USD |
| `7D` | `324.10` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 7,090.00 USD |
| `7D` | `324.40` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 16,260.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.30M` | Total OI Tokens: `1,089,167.4 BCH`
  * 1h OI Change: `-2.39%` | 4h OI Change: `-3.79%` | 24h OI Change: `-5.28%`
  * Exchange Breakdown: Binance=`91.69M` | Bybit=`38.33M` | OKX=`24.11M` | Hyperliquid=`7.67M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `6.27K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0048%` | **USDT OKX** | `-0.0057%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0003%` |
| **USDT MEXC** | `0.0047%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0028%` | **USDT Bitget** | `0.0098%` |
| **CoinM Binance** | `-0.0026%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `45.55%` | `54.45%` | `0.84` | 10,690,000.00 USD |
| `15M` | `Binance` | `41.91%` | `58.09%` | `0.72` | 3,690,000.00 USD |
| `15M` | `OKX` | `44.77%` | `55.23%` | `0.81` | 1,590,000.00 USD |
| `15M` | `Bybit` | `46.85%` | `53.15%` | `0.88` | 1,130,000.00 USD |
| `15M` | `KuCoin` | `41.16%` | `58.84%` | `0.70` | 76,090.00 USD |
| `15M` | `Gate` | `45.84%` | `54.16%` | `0.85` | 1,050,000.00 USD |
| `15M` | `Bitget` | `41.33%` | `58.67%` | `0.70` | 328,720.00 USD |
| `15M` | `BingX` | `41.3%` | `58.7%` | `0.70` | 808,180.00 USD |
| `15M` | `MEXC` | `35.13%` | `64.87%` | `0.54` | 420,090.00 USD |
| `15M` | `Bitunix` | `52.36%` | `47.64%` | `1.10` | 256,190.00 USD |
| `15M` | `Hyperliquid` | `23.39%` | `76.61%` | `0.31` | 57,670.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.09%` | `49.91%` | `1.00` | 458,920.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `71.8%` | `28.2%` | `2.55` | 719,300.00 USD |
| `15M` | `HTX` | `66.81%` | `33.19%` | `2.01` | 64,030.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `33.97%` | `66.03%` | `0.51` | 19,100.00 USD |
| `15M` | `Aster` | `10.93%` | `89.07%` | `0.12` | 5,510.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `58.97%` | `41.03%` | `1.44` | 4,750.00 USD |
| `15M` | `Whale Positions` | `41.91%` | `58.09%` | `0.72` | 3,690,000.00 USD |
| `15M` | `Global Accounts` | `45.55%` | `54.45%` | `0.84` | 10,690,000.00 USD |
| `1H` | `BCH` | `50.83%` | `49.17%` | `1.03` | 16,640,000.00 USD |
| `1H` | `Binance` | `45.54%` | `54.46%` | `0.84` | 5,030,000.00 USD |
| `1H` | `OKX` | `50.59%` | `49.41%` | `1.02` | 2,040,000.00 USD |
| `1H` | `Bybit` | `56.52%` | `43.48%` | `1.30` | 1,680,000.00 USD |
| `1H` | `KuCoin` | `41.94%` | `58.06%` | `0.72` | 99,880.00 USD |
| `1H` | `Gate` | `45.47%` | `54.53%` | `0.83` | 2,070,000.00 USD |
| `1H` | `Bitget` | `49.33%` | `50.67%` | `0.97` | 464,110.00 USD |
| `1H` | `BingX` | `47.49%` | `52.51%` | `0.90` | 2,270,000.00 USD |
| `1H` | `MEXC` | `40.93%` | `59.07%` | `0.69` | 586,440.00 USD |
| `1H` | `Bitunix` | `53.77%` | `46.23%` | `1.16` | 334,380.00 USD |
| `1H` | `Hyperliquid` | `49.28%` | `50.72%` | `0.97` | 96,460.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.03%` | `49.97%` | `1.00` | 522,870.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `82.92%` | `17.08%` | `4.85` | 1,280,000.00 USD |
| `1H` | `HTX` | `69.46%` | `30.54%` | `2.27` | 71,920.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.35%` | `57.65%` | `0.73` | 30,960.00 USD |
| `1H` | `Aster` | `70.14%` | `29.86%` | `2.35` | 52,710.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `54.71%` | `45.29%` | `1.21` | 5,220.00 USD |
| `1H` | `Whale Positions` | `45.54%` | `54.46%` | `0.84` | 5,030,000.00 USD |
| `1H` | `Global Accounts` | `50.83%` | `49.17%` | `1.03` | 16,640,000.00 USD |
| `4H` | `BCH` | `51.09%` | `48.91%` | `1.04` | 54,060,000.00 USD |
| `4H` | `Binance` | `46.01%` | `53.99%` | `0.85` | 15,410,000.00 USD |
| `4H` | `OKX` | `48.44%` | `51.56%` | `0.94` | 5,650,000.00 USD |
| `4H` | `Bybit` | `49.61%` | `50.39%` | `0.98` | 4,840,000.00 USD |
| `4H` | `KuCoin` | `45.86%` | `54.14%` | `0.85` | 466,460.00 USD |
| `4H` | `Gate` | `49.12%` | `50.88%` | `0.97` | 7,310,000.00 USD |
| `4H` | `Bitget` | `49.76%` | `50.24%` | `0.99` | 1,100,000.00 USD |
| `4H` | `BingX` | `45.2%` | `54.8%` | `0.82` | 9,170,000.00 USD |
| `4H` | `MEXC` | `43.16%` | `56.84%` | `0.76` | 1,740,000.00 USD |
| `4H` | `Bitunix` | `46.61%` | `53.39%` | `0.87` | 850,030.00 USD |
| `4H` | `Hyperliquid` | `36.69%` | `63.31%` | `0.58` | 377,560.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.72%` | `50.28%` | `0.99` | 1,760,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `92.74%` | `7.26%` | `12.77` | 4,870,000.00 USD |
| `4H` | `HTX` | `52.79%` | `47.21%` | `1.12` | 140,090.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `22.01%` | `77.99%` | `0.28` | 203,510.00 USD |
| `4H` | `Aster` | `70.19%` | `29.81%` | `2.35` | 117,960.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `11.23%` | `88.77%` | `0.13` | 36,980.00 USD |
| `4H` | `Whale Positions` | `46.01%` | `53.99%` | `0.85` | 15,410,000.00 USD |
| `4H` | `Global Accounts` | `51.09%` | `48.91%` | `1.04` | 54,060,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `288.09` | `287.57` | `288.09` | `289.31` | `286.49` | 1,912,559.47 USD | 931,105.86 USD | 981,453.62 USD | -50,347.76 USD | `-2.63%` | `25B / 19S` |
| `0:00 UTC` | `289.00` | `288.94` | `289.00` | `289.94` | `288.00` | 1,099,157.40 USD | 660,933.72 USD | 438,223.69 USD | 222,710.03 USD | `+20.26%` | `43B / 33S` |
| `5:00 UTC` | `287.91` | `288.60` | `287.91` | `289.87` | `287.51` | 851,365.60 USD | 435,531.09 USD | 415,834.51 USD | 19,696.57 USD | `+2.31%` | `18B / 22S` |
| `0:00 UTC` | `286.33` | `286.94` | `286.33` | `287.87` | `285.90` | 1,269,041.85 USD | 639,367.56 USD | 629,674.29 USD | 9,693.27 USD | `+0.76%` | `32B / 48S` |
| `5:00 UTC` | `288.00` | `288.25` | `288.00` | `289.13` | `287.22` | 1,082,751.51 USD | 592,384.75 USD | 490,366.75 USD | 102,018.00 USD | `+9.42%` | `41B / 33S` |
| `0:00 UTC` | `288.00` | `287.59` | `288.00` | `288.53` | `286.82` | 774,817.75 USD | 442,366.10 USD | 332,451.65 USD | 109,914.46 USD | `+14.19%` | `38B / 28S` |
| `5:00 UTC` | `289.00` | `288.21` | `289.00` | `289.02` | `287.22` | 505,722.48 USD | 323,366.92 USD | 182,355.56 USD | 141,011.36 USD | `+27.88%` | `60B / 31S` |
| `0:00 UTC` | `288.00` | `287.86` | `288.00` | `288.89` | `287.26` | 500,104.64 USD | 252,267.65 USD | 247,836.98 USD | 4,430.67 USD | `+0.89%` | `39B / 37S` |
| `5:00 UTC` | `287.00` | `286.98` | `287.00` | `287.64` | `286.45` | 492,053.69 USD | 262,098.60 USD | 229,955.08 USD | 32,143.52 USD | `+6.53%` | `24B / 25S` |
| `0:00 UTC` | `282.00` | `283.05` | `282.00` | `286.92` | `280.48` | 5,120,049.98 USD | 2,215,386.82 USD | 2,904,663.16 USD | -689,276.34 USD | `-13.46%` | `4B / 31S` |

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
| `5m` | 6,980.00 USD | 679,570.00 USD | **`ACCUMULATION`** |
| `15m` | -396,570.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -408,100.00 USD | -1,460,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -486,870.00 USD | -1,120,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -579,190.00 USD | -641,030.00 USD | **`DISTRIBUTION`** |
| `4h` | -592,020.00 USD | -2,500,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -250,490.00 USD | -3,010,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -209,820.00 USD | -1,620,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -278,100.00 USD | -1,910,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,500,000.00 USD | -10,110,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -407,110.00 USD | -12,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,840,000.00 USD | -137,120,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+6.98K` | 15m=`-396.57K` | 1h=`-486.87K` | 24h=`-1.50M`
* Futures Capital Netflows: 5m=`+679.57K` | 15m=`-1.44M` | 1h=`-1.12M` | 24h=`-10.11M`
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
  * `2026-10-30 01:36:09 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 00:58:09 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 01:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 01:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:51:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:51:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:51:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `276.88` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `273.38` (Risk Distance: `3.50` pts)
  * +2.5R Take Profit: `285.63`
  * Mathematical Lot Sizing: **`2.85 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `291.06` (Risk Distance: `3.50` pts)
  * +2.5R Take Profit: `278.81`
  * Mathematical Lot Sizing: **`2.85 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`284.86`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
