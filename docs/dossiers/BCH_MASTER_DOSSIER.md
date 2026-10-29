# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 02:24:37 IST` (`2026-10-29 20:54:37 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `273.51` | **Live Ask Quote**: `275.14` | **Mid Price**: `274.32`
- **Spread Points**: `1631.00` | **Spread BPS**: `59.46 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
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
  * Session VWAP: `282.87` | VWAP Z-Score: `-0.39` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.31` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `37.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.13` | Lower -3.00σ Band: `270.60`
  * Upper +2.51σ Band: `293.13` | Lower -2.51σ Band: `272.61`
  * Upper +2.01σ Band: `291.08` | Lower -2.01σ Band: `274.65`
  * Upper +2.00σ Band: `291.04` | Lower -2.00σ Band: `274.69`
  * Upper +1.28σ Band: `288.10` | Lower -1.28σ Band: `277.63`
  * Upper +1.00σ Band: `286.95` | Lower -1.00σ Band: `278.78`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`285.28` | EMA-20=`285.60` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`284.18` (Slope: `+0.0000`) | EMA-100=`284.42`
  * Institutional Anchors: EMA-144=`284.76` | EMA-200=`284.83` (Slope: `+0.0760`) | EMA-233=`285.19`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`274.76` | Weekly High=`304.16` | Weekly Low=`274.76`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `287.43` (Distance: `-4.23%`)
  * Point of Control (POC) = `278.71` (Distance: `-1.24%`)
  * Value Area Low (VAL) = `276.50` (Distance: `-0.45%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`299.16` | POC=`296.76` | VAL=`289.44`
  * Prior Day Extremes: PDH=`304.16` | PDL=`281.75` | PDC=`288.90`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.02` | Weekly POC=`278.72` | Weekly VAL=`275.22`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`290.60` | Low=`274.76`
  * London Session (08:00-16:00 UTC): High=`281.86` | Low=`276.86`
  * New York Session (13:00-21:00 UTC): High=`292.96` | Low=`277.16`
  * Initial Balance (First Hour): IB High=`281.86` | IB Low=`279.31`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `273.23` - `275.42`
  * Optimal Trade Entry (OTE 0.705): `274.87`
  * Structural Invalidation Anchor (0.786): `276.52`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `281.76` | `282.40` | `278.94` | `279.88` | `4,230` | 1,184,906.04 USD | -5,397.45 USD | `-0.46%` | -4,476,764.13 USD | `-0.01` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `279.90` | `280.49` | `278.60` | `279.22` | `4,826` | 1,348,271.25 USD | 216,496.68 USD | `+16.06%` | -4,260,267.45 USD | `+0.72` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `279.22` | `279.24` | `273.56` | `274.94` | `11,736` | 3,242,876.95 USD | -569,600.21 USD | `-17.56%` | -4,829,867.66 USD | `-1.75` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `286.78` | `286.91` | `280.46` | `283.00` | `19,685` | 5,571,416.97 USD | -599,113.61 USD | `-10.75%` | -4,754,145.24 USD | `-1.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `282.99` | `282.99` | `281.48` | `281.76` | `5,633` | 1,589,754.90 USD | 282,778.55 USD | `+17.79%` | -4,471,366.69 USD | `+0.80` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `281.76` | `282.40` | `273.56` | `274.59` | `20,898` | 5,805,136.95 USD | -367,333.40 USD | `-6.33%` | -4,838,700.09 USD | `-0.61` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `288.88` | `289.93` | `285.90` | `288.17` | `14,933` | 4,302,316.36 USD | 354,117.88 USD | `+8.23%` | -4,479,466.60 USD | `+0.75` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `288.16` | `289.02` | `286.45` | `286.78` | `7,901` | 2,272,698.56 USD | 287,500.01 USD | `+12.65%` | -4,191,966.59 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `286.78` | `286.91` | `273.56` | `274.59` | `46,216` | 12,966,308.82 USD | -683,668.45 USD | `-5.27%` | -4,875,635.05 USD | `-0.66` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `273.56` | `274.94` | `46,110` | 12,937,226.11 USD | -674,836.03 USD | `-5.22%` | -4,085,093.83 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `277.35` | `282.39` | `276.59` | `278.88` | `47,861` | 13,383,109.09 USD | -153,847.38 USD | `-1.15%` | -3,024,241.04 USD | `+1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `278.88` | `282.00` | `277.22` | `279.37` | `40,922` | 11,454,296.89 USD | -658,851.13 USD | `-5.75%` | -3,683,092.17 USD | `+0.48` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | -1,938,355.87 USD | `+1.36` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -3,410,257.80 USD | `-0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `273.56` | `274.94` | `46,110` | 12,937,226.11 USD | -674,836.03 USD | `-5.22%` | -4,085,093.83 USD | `+0.00` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:14:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1990` | `0x12d2...f97f` | `LONG` | 1,013,088.97 USD | `3,627,243,000,000.00` | `303.26` | `270.63` | `0.000000` | -86,910.37 USD | `-8.58%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `259.00` | 56,657.29 USD | `-` | `NEWS_INTEL` | `-` | #BCH Liquidated Long: 56.66K USD at 259.0000 USD [API] | `2026-10-15 02:24:27` |
| `ANNOUNCEMENT` | `INFO` | `298.14` | 7,602.87 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 7.60K USD at 298.1400 USD [API] | `2026-10-28 03:49:50` |


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
| `1D` | `Long Liquidation` | `244.00` | 3,900,000.00 USD | 3,900,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.00` | 3,890,000.00 USD | 3,890,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 12,750.00 USD | 254,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 241,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `246.40` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `246.50` | 5,730.00 USD | 240,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `246.80` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.20` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 235,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.60` | 3,890,000.00 USD | 3,890,000.00 USD | 330.05 USD | 0.00 USD | 5.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.60` | 3,890,000.00 USD | 3,890,000.00 USD | 330.05 USD | 0.00 USD | 5.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.00` | 3,890,000.00 USD | 3,890,000.00 USD | 10,640.00 USD | 619.60 USD | 23,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.00` | 3,890,000.00 USD | 3,890,000.00 USD | 10,640.00 USD | 619.60 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.40` | 3,860,000.00 USD | 3,860,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 3,860,000.00 USD | 3,860,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.80` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 251.70 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.80` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 251.70 USD | 13,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.20` | 3,830,000.00 USD | 3,830,000.00 USD | 3,780.00 USD | 9,370.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 3,830,000.00 USD | 3,830,000.00 USD | 3,780.00 USD | 9,370.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.60` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 6.43 USD | 1,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.60` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 6.43 USD | 1,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.00` | 3,800,000.00 USD | 3,800,000.00 USD | 13,540.00 USD | 1,270.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.00` | 3,800,000.00 USD | 3,800,000.00 USD | 13,540.00 USD | 1,270.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.40` | 3,780,000.00 USD | 3,780,000.00 USD | 9,230.00 USD | 5,500.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 3,780,000.00 USD | 3,780,000.00 USD | 9,230.00 USD | 5,500.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 234,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.80` | 3,770,000.00 USD | 3,770,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.80` | 3,760,000.00 USD | 3,760,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.20` | 3,740,000.00 USD | 3,740,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 3,730,000.00 USD | 3,730,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 233,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.60` | 3,650,000.00 USD | 3,650,000.00 USD | 18,740.00 USD | 51,410.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.60` | 3,650,000.00 USD | 3,650,000.00 USD | 18,740.00 USD | 51,410.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.00` | 3,570,000.00 USD | 3,570,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.00` | 3,570,000.00 USD | 3,570,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.40` | 3,500,000.00 USD | 3,500,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 3,490,000.00 USD | 3,490,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 26,370.00 USD | 232,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.80` | 3,480,000.00 USD | 3,480,000.00 USD | 17,180.00 USD | 6,420.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.80` | 3,480,000.00 USD | 3,480,000.00 USD | 17,180.00 USD | 6,420.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.20` | 3,460,000.00 USD | 3,460,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 3,450,000.00 USD | 3,450,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.60` | 3,430,000.00 USD | 3,430,000.00 USD | 14,860.00 USD | 13,480.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.60` | 3,420,000.00 USD | 3,420,000.00 USD | 14,860.00 USD | 13,480.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 3,390,000.00 USD | 3,390,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.00` | 3,380,000.00 USD | 3,380,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 3,370,000.00 USD | 3,370,000.00 USD | 134.35 USD | 2,130.00 USD | 2.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 3,370,000.00 USD | 3,370,000.00 USD | 134.35 USD | 2,130.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 362.92 USD | 206,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 3,370,000.00 USD | 3,370,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 3,370,000.00 USD | 3,370,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 3,360,000.00 USD | 3,360,000.00 USD | 9,500.00 USD | 6,590.00 USD | 11.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 3,360,000.00 USD | 3,360,000.00 USD | 9,500.00 USD | 6,590.00 USD | 11.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.60` | 3,350,000.00 USD | 3,350,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.60` | 3,340,000.00 USD | 3,340,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 3,330,000.00 USD | 3,330,000.00 USD | 11,080.00 USD | 321.10 USD | 4.57 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.00` | 3,330,000.00 USD | 3,330,000.00 USD | 11,080.00 USD | 321.10 USD | 4.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 3,320,000.00 USD | 3,320,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 3,310,000.00 USD | 3,310,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 2,480.00 USD | 205,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 3,300,000.00 USD | 3,300,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 3,290,000.00 USD | 3,290,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 3,290,000.00 USD | 3,290,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 3,290,000.00 USD | 3,290,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 14,580.00 USD | 203,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.60` | 3,280,000.00 USD | 3,280,000.00 USD | 918.80 USD | 600.15 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.60` | 3,270,000.00 USD | 3,270,000.00 USD | 918.80 USD | 600.15 USD | 9,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 3,270,000.00 USD | 3,270,000.00 USD | 3,780.00 USD | 2,390.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.00` | 3,260,000.00 USD | 3,260,000.00 USD | 3,780.00 USD | 2,390.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 3,260,000.00 USD | 3,260,000.00 USD | 1,370.00 USD | 3,270.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 3,260,000.00 USD | 3,260,000.00 USD | 1,370.00 USD | 3,270.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 188,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 3,250,000.00 USD | 3,250,000.00 USD | 2,120.00 USD | 3,640.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 3,250,000.00 USD | 3,250,000.00 USD | 2,120.00 USD | 3,640.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 3,240,000.00 USD | 3,240,000.00 USD | 13,040.00 USD | 7,320.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 3,230,000.00 USD | 3,230,000.00 USD | 13,040.00 USD | 3,850.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 3,210,000.00 USD | 3,210,000.00 USD | 5,330.00 USD | 6,640.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.60` | 3,210,000.00 USD | 3,210,000.00 USD | 5,330.00 USD | 6,640.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 3,190,000.00 USD | 3,190,000.00 USD | 19,940.00 USD | 13,760.00 USD | 33,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.00` | 3,190,000.00 USD | 3,190,000.00 USD | 19,940.00 USD | 13,760.00 USD | 33,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 3,120,000.00 USD | 3,120,000.00 USD | 3,100.00 USD | 10,630.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 3,120,000.00 USD | 3,120,000.00 USD | 3,100.00 USD | 10,630.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 3,860.00 USD | 188,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 3,100,000.00 USD | 3,100,000.00 USD | 9,670.00 USD | 14,940.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 3,100,000.00 USD | 3,100,000.00 USD | 9,670.00 USD | 14,940.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 3,060,000.00 USD | 3,060,000.00 USD | 7,970.00 USD | 14,630.00 USD | 507.10 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 3,060,000.00 USD | 3,060,000.00 USD | 7,970.00 USD | 14,630.00 USD | 507.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 3,040,000.00 USD | 3,040,000.00 USD | 9,470.00 USD | 5,410.00 USD | 18.60 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.60` | 3,040,000.00 USD | 3,040,000.00 USD | 9,470.00 USD | 5,410.00 USD | 18.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 3,020,000.00 USD | 3,020,000.00 USD | 4,560.00 USD | 4,240.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.00` | 3,020,000.00 USD | 3,020,000.00 USD | 4,560.00 USD | 4,240.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 3,000,000.00 USD | 3,000,000.00 USD | 8,640.00 USD | 4,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 3,000,000.00 USD | 3,000,000.00 USD | 8,640.00 USD | 4,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.80` | 2,990,000.00 USD | 2,990,000.00 USD | 366.04 USD | 1,650.00 USD | 12.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 2,990,000.00 USD | 2,990,000.00 USD | 366.04 USD | 1,650.00 USD | 12.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 2,990,000.00 USD | 2,990,000.00 USD | 8,670.00 USD | 571.81 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 2,990,000.00 USD | 2,990,000.00 USD | 8,670.00 USD | 571.81 USD | 16,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 2,960,000.00 USD | 2,960,000.00 USD | 630.84 USD | 6,860.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.60` | 2,960,000.00 USD | 2,960,000.00 USD | 630.84 USD | 6,860.00 USD | 16,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 2,940,000.00 USD | 2,940,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.00` | 2,940,000.00 USD | 2,940,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 2,930,000.00 USD | 2,930,000.00 USD | 1,660.00 USD | 724.53 USD | 16.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 2,930,000.00 USD | 2,930,000.00 USD | 1,660.00 USD | 724.53 USD | 16.24 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `264.50` | 280.37 USD | 184,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `264.80` | 2,930,000.00 USD | 2,930,000.00 USD | 28,700.00 USD | 957.20 USD | 75,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 2,930,000.00 USD | 2,930,000.00 USD | 28,700.00 USD | 957.20 USD | 75,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 2,830,000.00 USD | 2,830,000.00 USD | 20,380.00 USD | 9,330.00 USD | 0.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 2,830,000.00 USD | 2,830,000.00 USD | 20,380.00 USD | 9,330.00 USD | 0.42 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 121,910.00 USD | 184,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.60` | 2,800,000.00 USD | 2,800,000.00 USD | 15,620.00 USD | 23,430.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.60` | 2,800,000.00 USD | 2,800,000.00 USD | 15,620.00 USD | 23,430.00 USD | 67,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 2,690,000.00 USD | 2,690,000.00 USD | 8,300.00 USD | 87.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.00` | 2,690,000.00 USD | 2,690,000.00 USD | 8,300.00 USD | 87.00 USD | 8,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 2,670,000.00 USD | 2,670,000.00 USD | 37,680.00 USD | 63.70 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 2,670,000.00 USD | 2,670,000.00 USD | 37,680.00 USD | 63.70 USD | 5,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `266.50` | 15,210.00 USD | 62,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `266.80` | 2,630,000.00 USD | 2,630,000.00 USD | 22,200.00 USD | 10,910.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 2,630,000.00 USD | 2,630,000.00 USD | 22,200.00 USD | 10,910.00 USD | 8,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 2,590,000.00 USD | 2,590,000.00 USD | 16,540.00 USD | 6,850.00 USD | 5,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 2,590,000.00 USD | 2,590,000.00 USD | 16,540.00 USD | 6,850.00 USD | 5,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `267.50` | 684.00 USD | 47,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.60` | 2,560,000.00 USD | 2,560,000.00 USD | 30,750.00 USD | 78,350.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.60` | 2,560,000.00 USD | 2,560,000.00 USD | 30,750.00 USD | 78,350.00 USD | 23,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 2,430,000.00 USD | 2,430,000.00 USD | 104,590.00 USD | 112,690.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.00` | 2,430,000.00 USD | 2,430,000.00 USD | 104,590.00 USD | 112,690.00 USD | 35,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 2,170,000.00 USD | 2,170,000.00 USD | 57,670.00 USD | 105,790.00 USD | 32,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 2,170,000.00 USD | 2,170,000.00 USD | 57,670.00 USD | 105,790.00 USD | 32,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `268.50` | 7,020.00 USD | 46,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 100,660.00 USD | 58,260.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 1,980,000.00 USD | 1,980,000.00 USD | 100,660.00 USD | 58,260.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 1,760,000.00 USD | 1,760,000.00 USD | 21,310.00 USD | 27,860.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 1,760,000.00 USD | 1,760,000.00 USD | 21,310.00 USD | 27,860.00 USD | 12,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `269.50` | 37,920.00 USD | 39,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `269.60` | 1,700,000.00 USD | 1,700,000.00 USD | 34,010.00 USD | 20,280.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.60` | 1,700,000.00 USD | 1,700,000.00 USD | 34,010.00 USD | 20,280.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 1,640,000.00 USD | 1,640,000.00 USD | 45,580.00 USD | 48,040.00 USD | 141,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.00` | 1,640,000.00 USD | 1,640,000.00 USD | 45,580.00 USD | 48,040.00 USD | 141,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 1,400,000.00 USD | 1,400,000.00 USD | 108,590.00 USD | 46,920.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 1,400,000.00 USD | 1,400,000.00 USD | 108,590.00 USD | 46,920.00 USD | 59,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 106.31 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.80` | 1,190,000.00 USD | 1,190,000.00 USD | 47,740.00 USD | 41,670.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 1,190,000.00 USD | 1,190,000.00 USD | 47,740.00 USD | 41,670.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 1,070,000.00 USD | 1,070,000.00 USD | 47,970.00 USD | 59,220.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.20` | 1,070,000.00 USD | 1,070,000.00 USD | 47,970.00 USD | 59,220.00 USD | 139,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `271.50` | 1,000.00 USD | 1,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `271.60` | 825,130.00 USD | 825,130.00 USD | 16,460.00 USD | 15,290.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.60` | 825,130.00 USD | 825,130.00 USD | 16,460.00 USD | 15,290.00 USD | 24,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 769,090.00 USD | 769,090.00 USD | 110,040.00 USD | 33,030.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.00` | 769,090.00 USD | 769,090.00 USD | 110,040.00 USD | 33,030.00 USD | 17,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 608,590.00 USD | 608,590.00 USD | 69,420.00 USD | 368.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 608,590.00 USD | 608,590.00 USD | 69,420.00 USD | 368.00 USD | 17,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `272.50` | 132.16 USD | 132.16 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `272.80` | 520,910.00 USD | 520,910.00 USD | 85,930.00 USD | 79.70 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 520,910.00 USD | 520,910.00 USD | 85,930.00 USD | 79.70 USD | 13,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 421,330.00 USD | 421,330.00 USD | 65,470.00 USD | 446.50 USD | 47,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 421,330.00 USD | 421,330.00 USD | 65,470.00 USD | 446.50 USD | 47,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 307,980.00 USD | 307,980.00 USD | 229,980.00 USD | 0.00 USD | 78,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.60` | 307,980.00 USD | 307,980.00 USD | 229,980.00 USD | 0.00 USD | 78,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `274.00` | 125,240.00 USD | 125,240.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.00` | 125,240.00 USD | 125,240.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.00` | 250,480.00 USD | 250,480.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `274.40` | 335,210.00 USD | 335,210.00 USD | 209,960.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.40` | 460,460.00 USD | 460,460.00 USD | 209,960.00 USD | 0.00 USD | 6.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `274.50` | 567.94 USD | 773.38 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `274.80` | 380,350.00 USD | 380,350.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.80` | 505,590.00 USD | 505,590.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `275.20` | 459,340.00 USD | 459,340.00 USD | 78,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `275.20` | 584,580.00 USD | 584,580.00 USD | 78,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `275.60` | 503,230.00 USD | 503,230.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `275.60` | 628,480.00 USD | 628,480.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `276.00` | 627,930.00 USD | 627,930.00 USD | 87,530.00 USD | 37,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.00` | 753,170.00 USD | 753,170.00 USD | 87,530.00 USD | 37,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `276.40` | 748,760.00 USD | 748,760.00 USD | 67,030.00 USD | 53,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.40` | 874,000.00 USD | 874,000.00 USD | 67,030.00 USD | 53,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `276.50` | 205.44 USD | 205.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `276.80` | 794,130.00 USD | 794,130.00 USD | 13,620.00 USD | 31,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.80` | 919,370.00 USD | 919,370.00 USD | 13,620.00 USD | 31,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `277.20` | 889,720.00 USD | 889,720.00 USD | 36,000.00 USD | 59,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.20` | 1,010,000.00 USD | 1,010,000.00 USD | 36,000.00 USD | 59,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `277.60` | 947,350.00 USD | 947,350.00 USD | 57,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.60` | 1,070,000.00 USD | 1,070,000.00 USD | 57,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.00` | 960,010.00 USD | 960,010.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.00` | 1,090,000.00 USD | 1,090,000.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.40` | 1,020,000.00 USD | 1,020,000.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.40` | 1,150,000.00 USD | 1,150,000.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.80` | 1,090,000.00 USD | 1,090,000.00 USD | 30,810.00 USD | 34,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.80` | 1,210,000.00 USD | 1,210,000.00 USD | 30,810.00 USD | 34,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.20` | 1,150,000.00 USD | 1,150,000.00 USD | 53,390.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.20` | 1,280,000.00 USD | 1,280,000.00 USD | 53,390.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.60` | 1,210,000.00 USD | 1,210,000.00 USD | 20,320.00 USD | 0.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.60` | 1,330,000.00 USD | 1,330,000.00 USD | 20,320.00 USD | 0.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.00` | 1,240,000.00 USD | 1,240,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.00` | 1,370,000.00 USD | 1,370,000.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.40` | 1,310,000.00 USD | 1,310,000.00 USD | 8,720.00 USD | 11,840.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.40` | 1,430,000.00 USD | 1,430,000.00 USD | 8,720.00 USD | 11,840.00 USD | 41,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.80` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.80` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.40` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.80` | 1,580,000.00 USD | 1,580,000.00 USD | 38,030.00 USD | 0.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.80` | 1,710,000.00 USD | 1,710,000.00 USD | 38,030.00 USD | 0.00 USD | 91,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.20` | 1,730,000.00 USD | 1,730,000.00 USD | 33,360.00 USD | 0.00 USD | 116,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.20` | 1,860,000.00 USD | 1,860,000.00 USD | 33,360.00 USD | 0.00 USD | 116,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.60` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 26,800.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.60` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 26,800.00 USD | 51,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.00` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 22,590.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 22,590.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.40` | 2,090,000.00 USD | 2,090,000.00 USD | 38,700.00 USD | 92,800.00 USD | 49,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 2,210,000.00 USD | 2,210,000.00 USD | 38,700.00 USD | 92,800.00 USD | 49,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.80` | 2,140,000.00 USD | 2,140,000.00 USD | 48,190.00 USD | 9,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 2,270,000.00 USD | 2,270,000.00 USD | 48,190.00 USD | 9,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.20` | 2,270,000.00 USD | 2,270,000.00 USD | 20,960.00 USD | 33,990.00 USD | 73,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.20` | 2,400,000.00 USD | 2,400,000.00 USD | 20,960.00 USD | 33,990.00 USD | 73,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.60` | 2,510,000.00 USD | 2,510,000.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.60` | 2,640,000.00 USD | 2,640,000.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.80` | 2,580,000.00 USD | 2,580,000.00 USD | 750.70 USD | 0.00 USD | 71,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 2,710,000.00 USD | 2,710,000.00 USD | 750.70 USD | 0.00 USD | 71,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.20` | 2,750,000.00 USD | 2,750,000.00 USD | 20,810.00 USD | 117,540.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 2,880,000.00 USD | 2,880,000.00 USD | 20,810.00 USD | 117,540.00 USD | 32,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.60` | 2,840,000.00 USD | 2,840,000.00 USD | 9,030.00 USD | 20,250.00 USD | 54,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.60` | 2,960,000.00 USD | 2,960,000.00 USD | 9,030.00 USD | 20,250.00 USD | 54,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.00` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 10,810.00 USD | 28,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.00` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 10,810.00 USD | 28,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.80` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 2,900,000.00 USD | 2,900,000.00 USD | 1,320.00 USD | 20,430.00 USD | 11.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 3,030,000.00 USD | 3,030,000.00 USD | 1,320.00 USD | 20,430.00 USD | 11.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.60` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.60` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.40` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 305.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 305.70 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.80` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 6,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 6,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 2,930,000.00 USD | 2,930,000.00 USD | 562.74 USD | 9,950.00 USD | 5.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 3,060,000.00 USD | 3,060,000.00 USD | 562.74 USD | 9,950.00 USD | 5.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.60` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 15,630.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 15,630.00 USD | 22,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 31,240.00 USD | 16.77 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 31,240.00 USD | 16.77 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 3,080,000.00 USD | 3,080,000.00 USD | 21,930.00 USD | 41,860.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 3,200,000.00 USD | 3,200,000.00 USD | 21,930.00 USD | 41,860.00 USD | 8,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.80` | 3,160,000.00 USD | 3,160,000.00 USD | 12,000.00 USD | 71,120.00 USD | 6.65 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 3,280,000.00 USD | 3,280,000.00 USD | 12,000.00 USD | 71,120.00 USD | 6.65 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 3,230,000.00 USD | 3,230,000.00 USD | 10,290.00 USD | 37,810.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 3,360,000.00 USD | 3,360,000.00 USD | 10,290.00 USD | 37,810.00 USD | 27,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 3,390,000.00 USD | 3,390,000.00 USD | 89,460.00 USD | 56,780.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.60` | 3,520,000.00 USD | 3,520,000.00 USD | 89,460.00 USD | 56,780.00 USD | 9,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 3,530,000.00 USD | 3,530,000.00 USD | 23,660.00 USD | 52,640.00 USD | 64,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.00` | 3,640,000.00 USD | 3,640,000.00 USD | 23,660.00 USD | 35,280.00 USD | 64,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 3,860,000.00 USD | 3,860,000.00 USD | 116,580.00 USD | 86,500.00 USD | 120,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 3,960,000.00 USD | 3,960,000.00 USD | 116,580.00 USD | 86,500.00 USD | 120,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 4,110,000.00 USD | 4,110,000.00 USD | 79,510.00 USD | 72,940.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 4,220,000.00 USD | 4,220,000.00 USD | 79,510.00 USD | 72,940.00 USD | 105,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 4,240,000.00 USD | 4,240,000.00 USD | 17,510.00 USD | 49,710.00 USD | 56,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 4,340,000.00 USD | 4,340,000.00 USD | 17,510.00 USD | 49,710.00 USD | 56,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.60` | 4,520,000.00 USD | 4,520,000.00 USD | 97,130.00 USD | 95,820.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.60` | 4,630,000.00 USD | 4,630,000.00 USD | 97,130.00 USD | 95,820.00 USD | 94,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 4,690,000.00 USD | 4,690,000.00 USD | 65,850.00 USD | 81,300.00 USD | 23,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.00` | 4,800,000.00 USD | 4,800,000.00 USD | 65,850.00 USD | 81,300.00 USD | 23,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 4,850,000.00 USD | 4,850,000.00 USD | 88,010.00 USD | 59,400.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 4,960,000.00 USD | 4,960,000.00 USD | 88,010.00 USD | 59,400.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.80` | 4,970,000.00 USD | 4,970,000.00 USD | 34,520.00 USD | 24,260.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,080,000.00 USD | 5,080,000.00 USD | 34,520.00 USD | 24,260.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 5,070,000.00 USD | 5,070,000.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,180,000.00 USD | 5,180,000.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 5,100,000.00 USD | 5,100,000.00 USD | 6,390.00 USD | 1,190.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.60` | 5,210,000.00 USD | 5,210,000.00 USD | 6,390.00 USD | 1,190.00 USD | 23,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 5,200,000.00 USD | 5,200,000.00 USD | 49,980.00 USD | 10,150.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.00` | 5,310,000.00 USD | 5,310,000.00 USD | 49,980.00 USD | 10,150.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 5,280,000.00 USD | 5,280,000.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 5,380,000.00 USD | 5,380,000.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.80` | 5,400,000.00 USD | 5,400,000.00 USD | 25,760.00 USD | 257.02 USD | 94,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 5,500,000.00 USD | 5,500,000.00 USD | 25,760.00 USD | 257.02 USD | 94,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 5,430,000.00 USD | 5,430,000.00 USD | 7,810.00 USD | 21,020.00 USD | 6.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 5,530,000.00 USD | 5,530,000.00 USD | 7,810.00 USD | 21,020.00 USD | 6.64 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `299.50` | 295.91 USD | 428.07 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `299.60` | 5,500,000.00 USD | 5,500,000.00 USD | 39,940.00 USD | 15,430.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.60` | 5,600,000.00 USD | 5,600,000.00 USD | 39,940.00 USD | 6,750.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 5,570,000.00 USD | 5,570,000.00 USD | 25,270.00 USD | 22,550.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.00` | 5,670,000.00 USD | 5,670,000.00 USD | 25,270.00 USD | 22,550.00 USD | 24,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 5,720,000.00 USD | 5,720,000.00 USD | 48,790.00 USD | 31,850.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 5,820,000.00 USD | 5,820,000.00 USD | 48,790.00 USD | 31,850.00 USD | 67,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.80` | 5,790,000.00 USD | 5,790,000.00 USD | 10,980.00 USD | 30,600.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 5,890,000.00 USD | 5,890,000.00 USD | 10,980.00 USD | 30,600.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 5,880,000.00 USD | 5,880,000.00 USD | 15,290.00 USD | 49,050.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 5,980,000.00 USD | 5,980,000.00 USD | 15,290.00 USD | 49,050.00 USD | 23,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `301.50` | 1,700.00 USD | 2,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `301.60` | 5,970,000.00 USD | 5,970,000.00 USD | 31,630.00 USD | 17,030.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.60` | 6,070,000.00 USD | 6,070,000.00 USD | 31,630.00 USD | 17,030.00 USD | 43,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 6,060,000.00 USD | 6,060,000.00 USD | 33,930.00 USD | 37,150.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.00` | 6,150,000.00 USD | 6,150,000.00 USD | 33,930.00 USD | 37,150.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 6,090,000.00 USD | 6,090,000.00 USD | 11,150.00 USD | 12,110.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 6,190,000.00 USD | 6,190,000.00 USD | 11,150.00 USD | 12,110.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 6,140,000.00 USD | 6,140,000.00 USD | 1,030.00 USD | 12,530.00 USD | 34,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 6,240,000.00 USD | 6,240,000.00 USD | 1,030.00 USD | 12,530.00 USD | 34,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 6,190,000.00 USD | 6,190,000.00 USD | 31,330.00 USD | 234.82 USD | 24,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 6,290,000.00 USD | 6,290,000.00 USD | 31,330.00 USD | 234.82 USD | 24,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 6,210,000.00 USD | 6,210,000.00 USD | 8,460.00 USD | 3,400.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.60` | 6,310,000.00 USD | 6,310,000.00 USD | 8,460.00 USD | 3,400.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 6,270,000.00 USD | 6,270,000.00 USD | 22,140.00 USD | 807.77 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.00` | 6,370,000.00 USD | 6,370,000.00 USD | 22,140.00 USD | 807.77 USD | 32,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 6,350,000.00 USD | 6,350,000.00 USD | 13,730.00 USD | 9,860.00 USD | 59,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 6,450,000.00 USD | 6,450,000.00 USD | 13,730.00 USD | 9,860.00 USD | 59,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 6,370,000.00 USD | 6,370,000.00 USD | 697.80 USD | 130.30 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 6,470,000.00 USD | 6,470,000.00 USD | 697.80 USD | 130.30 USD | 16,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 6,380,000.00 USD | 6,380,000.00 USD | 9,070.00 USD | 249.40 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 6,480,000.00 USD | 6,480,000.00 USD | 9,070.00 USD | 249.40 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 6,390,000.00 USD | 6,390,000.00 USD | 4,670.00 USD | 1,650.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.60` | 6,480,000.00 USD | 6,480,000.00 USD | 4,670.00 USD | 1,650.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 6,400,000.00 USD | 6,400,000.00 USD | 9,360.00 USD | 5,830.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.00` | 6,500,000.00 USD | 6,500,000.00 USD | 9,360.00 USD | 5,830.00 USD | 3,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 6,420,000.00 USD | 6,420,000.00 USD | 4,230.00 USD | 9,300.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 6,520,000.00 USD | 6,520,000.00 USD | 4,230.00 USD | 9,300.00 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 6,490,000.00 USD | 6,490,000.00 USD | 28,860.00 USD | 35,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 6,590,000.00 USD | 6,590,000.00 USD | 28,860.00 USD | 35,370.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 6,550,000.00 USD | 6,550,000.00 USD | 11,230.00 USD | 27,230.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 6,650,000.00 USD | 6,650,000.00 USD | 11,230.00 USD | 27,230.00 USD | 18,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `307.50` | 411.74 USD | 2,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `307.60` | 6,600,000.00 USD | 6,600,000.00 USD | 14,610.00 USD | 33,780.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.60` | 6,700,000.00 USD | 6,700,000.00 USD | 14,610.00 USD | 33,780.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 6,670,000.00 USD | 6,670,000.00 USD | 30,270.00 USD | 20,570.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.00` | 6,770,000.00 USD | 6,770,000.00 USD | 30,270.00 USD | 20,570.00 USD | 22,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 6,690,000.00 USD | 6,690,000.00 USD | 5,470.00 USD | 3,530.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 6,790,000.00 USD | 6,790,000.00 USD | 5,470.00 USD | 3,530.00 USD | 4,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.80` | 6,700,000.00 USD | 6,700,000.00 USD | 9,910.00 USD | 369.62 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 6,800,000.00 USD | 6,800,000.00 USD | 9,910.00 USD | 369.62 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.20` | 6,730,000.00 USD | 6,730,000.00 USD | 10,010.00 USD | 15,050.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 6,830,000.00 USD | 6,830,000.00 USD | 10,010.00 USD | 15,050.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.60` | 6,770,000.00 USD | 6,770,000.00 USD | 14,370.00 USD | 14,290.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.60` | 6,870,000.00 USD | 6,870,000.00 USD | 14,370.00 USD | 14,290.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.00` | 6,790,000.00 USD | 6,790,000.00 USD | 8,430.00 USD | 4,640.00 USD | 6,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.00` | 6,890,000.00 USD | 6,890,000.00 USD | 8,430.00 USD | 4,640.00 USD | 6,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.40` | 6,800,000.00 USD | 6,800,000.00 USD | 144.00 USD | 7,080.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 6,900,000.00 USD | 6,900,000.00 USD | 144.00 USD | 7,080.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `310.50` | 517.91 USD | 3,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `310.80` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 2,130.00 USD | 1.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 2,130.00 USD | 1.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.20` | 6,810,000.00 USD | 6,810,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 6,910,000.00 USD | 6,910,000.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.60` | 6,830,000.00 USD | 6,830,000.00 USD | 9,900.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.60` | 6,930,000.00 USD | 6,930,000.00 USD | 9,900.00 USD | 6,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.00` | 6,830,000.00 USD | 6,830,000.00 USD | 244.00 USD | 0.00 USD | 5.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.00` | 6,930,000.00 USD | 6,930,000.00 USD | 244.00 USD | 0.00 USD | 5.74 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.40` | 6,850,000.00 USD | 6,850,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 6,940,000.00 USD | 6,940,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.80` | 6,860,000.00 USD | 6,860,000.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 6,960,000.00 USD | 6,960,000.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.20` | 6,870,000.00 USD | 6,870,000.00 USD | 5,080.00 USD | 3,820.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 6,970,000.00 USD | 6,970,000.00 USD | 5,080.00 USD | 3,820.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.60` | 6,880,000.00 USD | 6,880,000.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.60` | 6,980,000.00 USD | 6,980,000.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.40` | 6,890,000.00 USD | 6,890,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 6,990,000.00 USD | 6,990,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.80` | 6,900,000.00 USD | 6,900,000.00 USD | 32.00 USD | 68.55 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 7,000,000.00 USD | 7,000,000.00 USD | 32.00 USD | 68.55 USD | 9,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.20` | 6,910,000.00 USD | 6,910,000.00 USD | 2,050.00 USD | 1,400.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 7,010,000.00 USD | 7,010,000.00 USD | 2,050.00 USD | 1,400.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `315.50` | 6,520.00 USD | 9,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `315.60` | 6,920,000.00 USD | 6,920,000.00 USD | 1,730.00 USD | 3,180.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.60` | 7,020,000.00 USD | 7,020,000.00 USD | 1,730.00 USD | 3,180.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.00` | 6,930,000.00 USD | 6,930,000.00 USD | 3,450.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.00` | 7,030,000.00 USD | 7,030,000.00 USD | 3,450.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.40` | 6,930,000.00 USD | 6,930,000.00 USD | 41.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 7,030,000.00 USD | 7,030,000.00 USD | 41.00 USD | 3,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.80` | 6,960,000.00 USD | 6,960,000.00 USD | 12,980.00 USD | 6,830.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 7,050,000.00 USD | 7,050,000.00 USD | 12,980.00 USD | 3,360.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.20` | 6,980,000.00 USD | 6,980,000.00 USD | 3,660.00 USD | 6,430.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 7,070,000.00 USD | 7,070,000.00 USD | 3,660.00 USD | 6,430.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.60` | 7,020,000.00 USD | 7,020,000.00 USD | 14,560.00 USD | 8,990.00 USD | 17,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.60` | 7,110,000.00 USD | 7,110,000.00 USD | 14,560.00 USD | 8,990.00 USD | 17,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.00` | 7,050,000.00 USD | 7,050,000.00 USD | 5,970.00 USD | 12,250.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.00` | 7,150,000.00 USD | 7,150,000.00 USD | 5,970.00 USD | 12,250.00 USD | 16,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `318.40` | 7,070,000.00 USD | 7,070,000.00 USD | 234.70 USD | 5,410.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 7,160,000.00 USD | 7,160,000.00 USD | 234.70 USD | 5,410.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `318.50` | 114.34 USD | 9,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `318.80` | 7,100,000.00 USD | 7,100,000.00 USD | 9,210.00 USD | 10,850.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.80` | 7,200,000.00 USD | 7,200,000.00 USD | 9,210.00 USD | 10,850.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.20` | 7,120,000.00 USD | 7,120,000.00 USD | 7,830.00 USD | 14,510.00 USD | 488.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.20` | 7,220,000.00 USD | 7,220,000.00 USD | 7,830.00 USD | 14,510.00 USD | 488.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `319.60` | 7,130,000.00 USD | 7,130,000.00 USD | 8,500.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.60` | 7,230,000.00 USD | 7,230,000.00 USD | 8,500.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `320.00` | 7,150,000.00 USD | 7,150,000.00 USD | 4,190.00 USD | 6,480.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.00` | 7,250,000.00 USD | 7,250,000.00 USD | 4,190.00 USD | 6,480.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 10,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `244.00` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD |
| `7D` | `244.00` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 443.40 USD | 265.80 USD | 0.00 USD |
| `1D` | `246.40` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD |
| `7D` | `246.40` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 6.30 USD |
| `1D` | `246.80` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `7D` | `246.80` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 2.41 USD |
| `1D` | `247.20` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD |
| `7D` | `247.20` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 0.00 USD | 2,370.00 USD | 0.00 USD |
| `1D` | `247.60` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 330.05 USD | 0.00 USD | 5.98 USD |
| `7D` | `247.60` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 330.05 USD | 0.00 USD | 5.98 USD |
| `1D` | `248.00` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 10,640.00 USD | 619.60 USD | 23,990.00 USD |
| `7D` | `248.00` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 10,640.00 USD | 619.60 USD | 23,990.00 USD |
| `1D` | `248.40` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD |
| `7D` | `248.40` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 7,480.00 USD | 3,250.00 USD | 6,250.00 USD |
| `1D` | `248.80` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 0.00 USD | 251.70 USD | 13,380.00 USD |
| `7D` | `248.80` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 0.00 USD | 251.70 USD | 13,380.00 USD |
| `1D` | `249.20` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 3,780.00 USD | 9,370.00 USD | 13,460.00 USD |
| `7D` | `249.20` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 3,780.00 USD | 9,370.00 USD | 13,460.00 USD |
| `1D` | `249.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 6.43 USD | 1,280.00 USD |
| `7D` | `249.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 6.43 USD | 1,280.00 USD |
| `1D` | `250.00` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 13,540.00 USD | 1,270.00 USD | 2,210.00 USD |
| `7D` | `250.00` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 13,540.00 USD | 1,270.00 USD | 2,210.00 USD |
| `1D` | `250.40` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 9,230.00 USD | 5,500.00 USD | 3,270.00 USD |
| `7D` | `250.40` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 9,230.00 USD | 5,500.00 USD | 3,270.00 USD |
| `1D` | `250.80` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD |
| `7D` | `250.80` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD |
| `1D` | `251.20` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD |
| `7D` | `251.20` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD |
| `1D` | `251.60` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 18,740.00 USD | 51,410.00 USD | 9,760.00 USD |
| `7D` | `251.60` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 18,740.00 USD | 51,410.00 USD | 9,760.00 USD |
| `1D` | `252.00` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,670.00 USD |
| `7D` | `252.00` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,670.00 USD |
| `1D` | `252.40` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,270.00 USD |
| `7D` | `252.40` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,270.00 USD |
| `1D` | `252.80` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 17,180.00 USD | 6,420.00 USD | 5,660.00 USD |
| `7D` | `252.80` | 3,480,000.00 USD | 0.00 USD | 3,480,000.00 USD | 17,180.00 USD | 6,420.00 USD | 5,660.00 USD |
| `1D` | `253.20` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,720.00 USD |
| `7D` | `253.20` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,720.00 USD |
| `1D` | `253.60` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 14,860.00 USD | 13,480.00 USD | 10,600.00 USD |
| `7D` | `253.60` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 14,860.00 USD | 13,480.00 USD | 10,600.00 USD |
| `1D` | `254.00` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD |
| `7D` | `254.00` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD |
| `1D` | `254.40` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 134.35 USD | 2,130.00 USD | 2.31 USD |
| `7D` | `254.40` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 134.35 USD | 2,130.00 USD | 2.31 USD |
| `1D` | `254.80` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `254.80` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD |
| `1D` | `255.20` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 9,500.00 USD | 6,590.00 USD | 11.05 USD |
| `7D` | `255.20` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 9,500.00 USD | 6,590.00 USD | 11.05 USD |
| `1D` | `255.60` | 3,350,000.00 USD | 0.00 USD | 3,350,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD |
| `7D` | `255.60` | 3,340,000.00 USD | 0.00 USD | 3,340,000.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD |
| `1D` | `256.00` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 11,080.00 USD | 321.10 USD | 4.57 USD |
| `7D` | `256.00` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 11,080.00 USD | 321.10 USD | 4.57 USD |
| `1D` | `256.40` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `256.40` | 3,310,000.00 USD | 0.00 USD | 3,310,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD |
| `1D` | `256.80` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD |
| `7D` | `256.80` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 5,260.00 USD | 928.93 USD | 8.97 USD |
| `1D` | `257.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD |
| `7D` | `257.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD |
| `1D` | `257.60` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 918.80 USD | 600.15 USD | 9,250.00 USD |
| `7D` | `257.60` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 918.80 USD | 600.15 USD | 9,250.00 USD |
| `1D` | `258.00` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 3,780.00 USD | 2,390.00 USD | 1,620.00 USD |
| `7D` | `258.00` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 3,780.00 USD | 2,390.00 USD | 1,620.00 USD |
| `1D` | `258.40` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,370.00 USD | 3,270.00 USD | 5,230.00 USD |
| `7D` | `258.40` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 1,370.00 USD | 3,270.00 USD | 5,230.00 USD |
| `1D` | `258.80` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 2,120.00 USD | 3,640.00 USD | 5,600.00 USD |
| `7D` | `258.80` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 2,120.00 USD | 3,640.00 USD | 5,600.00 USD |
| `1D` | `259.20` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 13,040.00 USD | 7,320.00 USD | 7,670.00 USD |
| `7D` | `259.20` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 13,040.00 USD | 3,850.00 USD | 7,670.00 USD |
| `1D` | `259.60` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 5,330.00 USD | 6,640.00 USD | 7,180.00 USD |
| `7D` | `259.60` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 5,330.00 USD | 6,640.00 USD | 7,180.00 USD |
| `1D` | `260.00` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 19,940.00 USD | 13,760.00 USD | 33,820.00 USD |
| `7D` | `260.00` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 19,940.00 USD | 13,760.00 USD | 33,820.00 USD |
| `1D` | `260.40` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 3,100.00 USD | 10,630.00 USD | 10,400.00 USD |
| `7D` | `260.40` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 3,100.00 USD | 10,630.00 USD | 10,400.00 USD |
| `1D` | `260.80` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 9,670.00 USD | 14,940.00 USD | 13,930.00 USD |
| `7D` | `260.80` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 9,670.00 USD | 14,940.00 USD | 13,930.00 USD |
| `1D` | `261.20` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 7,970.00 USD | 14,630.00 USD | 507.10 USD |
| `7D` | `261.20` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 7,970.00 USD | 14,630.00 USD | 507.10 USD |
| `1D` | `261.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 9,470.00 USD | 5,410.00 USD | 18.60 USD |
| `7D` | `261.60` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 9,470.00 USD | 5,410.00 USD | 18.60 USD |
| `1D` | `262.00` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 4,560.00 USD | 4,240.00 USD | 13,920.00 USD |
| `7D` | `262.00` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 4,560.00 USD | 4,240.00 USD | 13,920.00 USD |
| `1D` | `262.40` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 8,640.00 USD | 4,380.00 USD | 0.00 USD |
| `7D` | `262.40` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 8,640.00 USD | 4,380.00 USD | 0.00 USD |
| `1D` | `262.80` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 366.04 USD | 1,650.00 USD | 12.23 USD |
| `7D` | `262.80` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 366.04 USD | 1,650.00 USD | 12.23 USD |
| `1D` | `263.20` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 8,670.00 USD | 571.81 USD | 16,180.00 USD |
| `7D` | `263.20` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 8,670.00 USD | 571.81 USD | 16,180.00 USD |
| `1D` | `263.60` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 630.84 USD | 6,860.00 USD | 16,160.00 USD |
| `7D` | `263.60` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 630.84 USD | 6,860.00 USD | 16,160.00 USD |
| `1D` | `264.00` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD |
| `7D` | `264.00` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 1,210.00 USD | 726.29 USD | 6.19 USD |
| `1D` | `264.40` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 1,660.00 USD | 724.53 USD | 16.24 USD |
| `7D` | `264.40` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 1,660.00 USD | 724.53 USD | 16.24 USD |
| `1D` | `264.80` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 28,700.00 USD | 957.20 USD | 75,610.00 USD |
| `7D` | `264.80` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 28,700.00 USD | 957.20 USD | 75,610.00 USD |
| `1D` | `265.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 20,380.00 USD | 9,330.00 USD | 0.42 USD |
| `7D` | `265.20` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 20,380.00 USD | 9,330.00 USD | 0.42 USD |
| `1D` | `265.60` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 15,620.00 USD | 23,430.00 USD | 67,100.00 USD |
| `7D` | `265.60` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 15,620.00 USD | 23,430.00 USD | 67,100.00 USD |
| `1D` | `266.00` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 8,300.00 USD | 87.00 USD | 8,710.00 USD |
| `7D` | `266.00` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 8,300.00 USD | 87.00 USD | 8,710.00 USD |
| `1D` | `266.40` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 37,680.00 USD | 63.70 USD | 5,010.00 USD |
| `7D` | `266.40` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 37,680.00 USD | 63.70 USD | 5,010.00 USD |
| `1D` | `266.80` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 22,200.00 USD | 10,910.00 USD | 8,520.00 USD |
| `7D` | `266.80` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 22,200.00 USD | 10,910.00 USD | 8,520.00 USD |
| `1D` | `267.20` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 16,540.00 USD | 6,850.00 USD | 5,310.00 USD |
| `7D` | `267.20` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 16,540.00 USD | 6,850.00 USD | 5,310.00 USD |
| `1D` | `267.60` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 30,750.00 USD | 78,350.00 USD | 23,730.00 USD |
| `7D` | `267.60` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 30,750.00 USD | 78,350.00 USD | 23,730.00 USD |
| `1D` | `268.00` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 104,590.00 USD | 112,690.00 USD | 35,780.00 USD |
| `7D` | `268.00` | 2,430,000.00 USD | 0.00 USD | 2,430,000.00 USD | 104,590.00 USD | 112,690.00 USD | 35,780.00 USD |
| `1D` | `268.40` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 57,670.00 USD | 105,790.00 USD | 32,080.00 USD |
| `7D` | `268.40` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 57,670.00 USD | 105,790.00 USD | 32,080.00 USD |
| `1D` | `268.80` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 100,660.00 USD | 58,260.00 USD | 56,650.00 USD |
| `7D` | `268.80` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 100,660.00 USD | 58,260.00 USD | 56,650.00 USD |
| `1D` | `269.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 21,310.00 USD | 27,860.00 USD | 12,930.00 USD |
| `7D` | `269.20` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 21,310.00 USD | 27,860.00 USD | 12,930.00 USD |
| `1D` | `269.60` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 34,010.00 USD | 20,280.00 USD | 10,340.00 USD |
| `7D` | `269.60` | 1,700,000.00 USD | 0.00 USD | 1,700,000.00 USD | 34,010.00 USD | 20,280.00 USD | 10,340.00 USD |
| `1D` | `270.00` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 45,580.00 USD | 48,040.00 USD | 141,110.00 USD |
| `7D` | `270.00` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 45,580.00 USD | 48,040.00 USD | 141,110.00 USD |
| `1D` | `270.40` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 108,590.00 USD | 46,920.00 USD | 59,180.00 USD |
| `7D` | `270.40` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 108,590.00 USD | 46,920.00 USD | 59,180.00 USD |
| `1D` | `270.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 47,740.00 USD | 41,670.00 USD | 25,510.00 USD |
| `7D` | `270.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 47,740.00 USD | 41,670.00 USD | 25,510.00 USD |
| `1D` | `271.20` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 47,970.00 USD | 59,220.00 USD | 139,870.00 USD |
| `7D` | `271.20` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 47,970.00 USD | 59,220.00 USD | 139,870.00 USD |
| `1D` | `271.60` | 825,130.00 USD | 0.00 USD | 825,130.00 USD | 16,460.00 USD | 15,290.00 USD | 24,290.00 USD |
| `7D` | `271.60` | 825,130.00 USD | 0.00 USD | 825,130.00 USD | 16,460.00 USD | 15,290.00 USD | 24,290.00 USD |
| `1D` | `272.00` | 769,090.00 USD | 0.00 USD | 769,090.00 USD | 110,040.00 USD | 33,030.00 USD | 17,440.00 USD |
| `7D` | `272.00` | 769,090.00 USD | 0.00 USD | 769,090.00 USD | 110,040.00 USD | 33,030.00 USD | 17,440.00 USD |
| `1D` | `272.40` | 608,590.00 USD | 0.00 USD | 608,590.00 USD | 69,420.00 USD | 368.00 USD | 17,890.00 USD |
| `7D` | `272.40` | 608,590.00 USD | 0.00 USD | 608,590.00 USD | 69,420.00 USD | 368.00 USD | 17,890.00 USD |
| `1D` | `272.80` | 520,910.00 USD | 0.00 USD | 520,910.00 USD | 85,930.00 USD | 79.70 USD | 13,580.00 USD |
| `7D` | `272.80` | 520,910.00 USD | 0.00 USD | 520,910.00 USD | 85,930.00 USD | 79.70 USD | 13,580.00 USD |
| `1D` | `273.20` | 421,330.00 USD | 0.00 USD | 421,330.00 USD | 65,470.00 USD | 446.50 USD | 47,440.00 USD |
| `7D` | `273.20` | 421,330.00 USD | 0.00 USD | 421,330.00 USD | 65,470.00 USD | 446.50 USD | 47,440.00 USD |
| `1D` | `273.60` | 307,980.00 USD | 0.00 USD | 307,980.00 USD | 229,980.00 USD | 0.00 USD | 78,000.00 USD |
| `7D` | `273.60` | 307,980.00 USD | 0.00 USD | 307,980.00 USD | 229,980.00 USD | 0.00 USD | 78,000.00 USD |
| `1D` | `273.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.00` | 125,240.00 USD | 125,240.00 USD | 0.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.00` | 125,240.00 USD | 125,240.00 USD | 0.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.00` | 250,480.00 USD | 250,480.00 USD | 0.00 USD | 125,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.40` | 335,210.00 USD | 335,210.00 USD | 0.00 USD | 209,960.00 USD | 0.00 USD | 6.00 USD |
| `7D` | `274.40` | 460,460.00 USD | 460,460.00 USD | 0.00 USD | 209,960.00 USD | 0.00 USD | 6.00 USD |
| `1D` | `274.80` | 380,350.00 USD | 380,350.00 USD | 0.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.80` | 505,590.00 USD | 505,590.00 USD | 0.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `275.20` | 459,340.00 USD | 459,340.00 USD | 0.00 USD | 78,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.20` | 584,580.00 USD | 584,580.00 USD | 0.00 USD | 78,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `275.60` | 503,230.00 USD | 503,230.00 USD | 0.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.60` | 628,480.00 USD | 628,480.00 USD | 0.00 USD | 43,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.00` | 627,930.00 USD | 627,930.00 USD | 0.00 USD | 87,530.00 USD | 37,170.00 USD | 0.00 USD |
| `7D` | `276.00` | 753,170.00 USD | 753,170.00 USD | 0.00 USD | 87,530.00 USD | 37,170.00 USD | 0.00 USD |
| `1D` | `276.40` | 748,760.00 USD | 748,760.00 USD | 0.00 USD | 67,030.00 USD | 53,790.00 USD | 0.00 USD |
| `7D` | `276.40` | 874,000.00 USD | 874,000.00 USD | 0.00 USD | 67,030.00 USD | 53,790.00 USD | 0.00 USD |
| `1D` | `276.80` | 794,130.00 USD | 794,130.00 USD | 0.00 USD | 13,620.00 USD | 31,750.00 USD | 0.00 USD |
| `7D` | `276.80` | 919,370.00 USD | 919,370.00 USD | 0.00 USD | 13,620.00 USD | 31,750.00 USD | 0.00 USD |
| `1D` | `277.20` | 889,720.00 USD | 889,720.00 USD | 0.00 USD | 36,000.00 USD | 59,590.00 USD | 0.00 USD |
| `7D` | `277.20` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 36,000.00 USD | 59,590.00 USD | 0.00 USD |
| `1D` | `277.60` | 947,350.00 USD | 947,350.00 USD | 0.00 USD | 57,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.60` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 57,640.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `278.00` | 960,010.00 USD | 960,010.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `278.00` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `278.40` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `278.40` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 61,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `278.80` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 30,810.00 USD | 34,490.00 USD | 0.00 USD |
| `7D` | `278.80` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 30,810.00 USD | 34,490.00 USD | 0.00 USD |
| `1D` | `279.20` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 53,390.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `279.20` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 53,390.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `279.60` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 20,320.00 USD | 0.00 USD | 34,800.00 USD |
| `7D` | `279.60` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 20,320.00 USD | 0.00 USD | 34,800.00 USD |
| `1D` | `280.00` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD |
| `7D` | `280.00` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD |
| `1D` | `280.40` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 8,720.00 USD | 11,840.00 USD | 41,630.00 USD |
| `7D` | `280.40` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 8,720.00 USD | 11,840.00 USD | 41,630.00 USD |
| `1D` | `280.80` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD |
| `7D` | `280.80` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD |
| `1D` | `281.20` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD |
| `7D` | `281.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 46,760.00 USD |
| `1D` | `282.40` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD |
| `7D` | `282.40` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,380.00 USD |
| `1D` | `282.80` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 38,030.00 USD | 0.00 USD | 91,610.00 USD |
| `7D` | `282.80` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 38,030.00 USD | 0.00 USD | 91,610.00 USD |
| `1D` | `283.20` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 33,360.00 USD | 0.00 USD | 116,190.00 USD |
| `7D` | `283.20` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 33,360.00 USD | 0.00 USD | 116,190.00 USD |
| `1D` | `283.60` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 26,800.00 USD | 51,990.00 USD |
| `7D` | `283.60` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 26,800.00 USD | 51,990.00 USD |
| `1D` | `284.00` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 22,590.00 USD | 69,640.00 USD |
| `7D` | `284.00` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 22,590.00 USD | 69,640.00 USD |
| `1D` | `284.40` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 38,700.00 USD | 92,800.00 USD | 49,010.00 USD |
| `7D` | `284.40` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 38,700.00 USD | 92,800.00 USD | 49,010.00 USD |
| `1D` | `284.80` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 48,190.00 USD | 9,090.00 USD | 0.00 USD |
| `7D` | `284.80` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 48,190.00 USD | 9,090.00 USD | 0.00 USD |
| `1D` | `285.20` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 20,960.00 USD | 33,990.00 USD | 73,380.00 USD |
| `7D` | `285.20` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 20,960.00 USD | 33,990.00 USD | 73,380.00 USD |
| `1D` | `285.60` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD |
| `7D` | `285.60` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD |
| `1D` | `286.80` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 750.70 USD | 0.00 USD | 71,360.00 USD |
| `7D` | `286.80` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 750.70 USD | 0.00 USD | 71,360.00 USD |
| `1D` | `287.20` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 20,810.00 USD | 117,540.00 USD | 32,730.00 USD |
| `7D` | `287.20` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 20,810.00 USD | 117,540.00 USD | 32,730.00 USD |
| `1D` | `287.60` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 9,030.00 USD | 20,250.00 USD | 54,720.00 USD |
| `7D` | `287.60` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 9,030.00 USD | 20,250.00 USD | 54,720.00 USD |
| `1D` | `288.00` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 10,810.00 USD | 28,310.00 USD |
| `7D` | `288.00` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 10,810.00 USD | 28,310.00 USD |
| `1D` | `288.80` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD |
| `7D` | `288.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 0.00 USD |
| `1D` | `289.20` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 1,320.00 USD | 20,430.00 USD | 11.96 USD |
| `7D` | `289.20` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 1,320.00 USD | 20,430.00 USD | 11.96 USD |
| `1D` | `289.60` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,160.00 USD |
| `7D` | `289.60` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,160.00 USD |
| `1D` | `290.40` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 305.70 USD | 0.00 USD |
| `7D` | `290.40` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 305.70 USD | 0.00 USD |
| `1D` | `290.80` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 6,700.00 USD | 0.00 USD |
| `7D` | `290.80` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 6,700.00 USD | 0.00 USD |
| `1D` | `291.20` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 562.74 USD | 9,950.00 USD | 5.82 USD |
| `7D` | `291.20` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 562.74 USD | 9,950.00 USD | 5.82 USD |
| `1D` | `291.60` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 15,630.00 USD | 22,140.00 USD |
| `7D` | `291.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 15,630.00 USD | 22,140.00 USD |
| `1D` | `292.00` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 31,240.00 USD | 16.77 USD |
| `7D` | `292.00` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 31,240.00 USD | 16.77 USD |
| `1D` | `292.40` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 21,930.00 USD | 41,860.00 USD | 8,120.00 USD |
| `7D` | `292.40` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 21,930.00 USD | 41,860.00 USD | 8,120.00 USD |
| `1D` | `292.80` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 12,000.00 USD | 71,120.00 USD | 6.65 USD |
| `7D` | `292.80` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 12,000.00 USD | 71,120.00 USD | 6.65 USD |
| `1D` | `293.20` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 10,290.00 USD | 37,810.00 USD | 27,360.00 USD |
| `7D` | `293.20` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 10,290.00 USD | 37,810.00 USD | 27,360.00 USD |
| `1D` | `293.60` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 89,460.00 USD | 56,780.00 USD | 9,830.00 USD |
| `7D` | `293.60` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 89,460.00 USD | 56,780.00 USD | 9,830.00 USD |
| `1D` | `294.00` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 23,660.00 USD | 52,640.00 USD | 64,900.00 USD |
| `7D` | `294.00` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 23,660.00 USD | 35,280.00 USD | 64,900.00 USD |
| `1D` | `294.40` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 116,580.00 USD | 86,500.00 USD | 120,920.00 USD |
| `7D` | `294.40` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 116,580.00 USD | 86,500.00 USD | 120,920.00 USD |
| `1D` | `294.80` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 79,510.00 USD | 72,940.00 USD | 105,170.00 USD |
| `7D` | `294.80` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 79,510.00 USD | 72,940.00 USD | 105,170.00 USD |
| `1D` | `295.20` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 17,510.00 USD | 49,710.00 USD | 56,340.00 USD |
| `7D` | `295.20` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 17,510.00 USD | 49,710.00 USD | 56,340.00 USD |
| `1D` | `295.60` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 97,130.00 USD | 95,820.00 USD | 94,830.00 USD |
| `7D` | `295.60` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 97,130.00 USD | 95,820.00 USD | 94,830.00 USD |
| `1D` | `296.00` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 65,850.00 USD | 81,300.00 USD | 23,140.00 USD |
| `7D` | `296.00` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 65,850.00 USD | 81,300.00 USD | 23,140.00 USD |
| `1D` | `296.40` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 88,010.00 USD | 59,400.00 USD | 6,460.00 USD |
| `7D` | `296.40` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 88,010.00 USD | 59,400.00 USD | 6,460.00 USD |
| `1D` | `296.80` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 34,520.00 USD | 24,260.00 USD | 62,270.00 USD |
| `7D` | `296.80` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 34,520.00 USD | 24,260.00 USD | 62,270.00 USD |
| `1D` | `297.20` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD |
| `7D` | `297.20` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD |
| `1D` | `297.60` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 6,390.00 USD | 1,190.00 USD | 23,120.00 USD |
| `7D` | `297.60` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 6,390.00 USD | 1,190.00 USD | 23,120.00 USD |
| `1D` | `298.00` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 49,980.00 USD | 10,150.00 USD | 41,570.00 USD |
| `7D` | `298.00` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 49,980.00 USD | 10,150.00 USD | 41,570.00 USD |
| `1D` | `298.40` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD |
| `7D` | `298.40` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD |
| `1D` | `298.80` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 25,760.00 USD | 257.02 USD | 94,680.00 USD |
| `7D` | `298.80` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 25,760.00 USD | 257.02 USD | 94,680.00 USD |
| `1D` | `299.20` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 7,810.00 USD | 21,020.00 USD | 6.64 USD |
| `7D` | `299.20` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 7,810.00 USD | 21,020.00 USD | 6.64 USD |
| `1D` | `299.60` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 39,940.00 USD | 15,430.00 USD | 19,140.00 USD |
| `7D` | `299.60` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 39,940.00 USD | 6,750.00 USD | 19,140.00 USD |
| `1D` | `300.00` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 25,270.00 USD | 22,550.00 USD | 24,860.00 USD |
| `7D` | `300.00` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 25,270.00 USD | 22,550.00 USD | 24,860.00 USD |
| `1D` | `300.40` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 48,790.00 USD | 31,850.00 USD | 67,330.00 USD |
| `7D` | `300.40` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 48,790.00 USD | 31,850.00 USD | 67,330.00 USD |
| `1D` | `300.80` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 10,980.00 USD | 30,600.00 USD | 29,940.00 USD |
| `7D` | `300.80` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 10,980.00 USD | 30,600.00 USD | 29,940.00 USD |
| `1D` | `301.20` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 15,290.00 USD | 49,050.00 USD | 23,960.00 USD |
| `7D` | `301.20` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 15,290.00 USD | 49,050.00 USD | 23,960.00 USD |
| `1D` | `301.60` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 31,630.00 USD | 17,030.00 USD | 43,960.00 USD |
| `7D` | `301.60` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 31,630.00 USD | 17,030.00 USD | 43,960.00 USD |
| `1D` | `302.00` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 33,930.00 USD | 37,150.00 USD | 11,570.00 USD |
| `7D` | `302.00` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 33,930.00 USD | 37,150.00 USD | 11,570.00 USD |
| `1D` | `302.40` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 11,150.00 USD | 12,110.00 USD | 10,300.00 USD |
| `7D` | `302.40` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 11,150.00 USD | 12,110.00 USD | 10,300.00 USD |
| `1D` | `302.80` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 1,030.00 USD | 12,530.00 USD | 34,810.00 USD |
| `7D` | `302.80` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 1,030.00 USD | 12,530.00 USD | 34,810.00 USD |
| `1D` | `303.20` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 31,330.00 USD | 234.82 USD | 24,020.00 USD |
| `7D` | `303.20` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 31,330.00 USD | 234.82 USD | 24,020.00 USD |
| `1D` | `303.60` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 8,460.00 USD | 3,400.00 USD | 6,250.00 USD |
| `7D` | `303.60` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 8,460.00 USD | 3,400.00 USD | 6,250.00 USD |
| `1D` | `304.00` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 22,140.00 USD | 807.77 USD | 32,130.00 USD |
| `7D` | `304.00` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 22,140.00 USD | 807.77 USD | 32,130.00 USD |
| `1D` | `304.40` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 13,730.00 USD | 9,860.00 USD | 59,110.00 USD |
| `7D` | `304.40` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 13,730.00 USD | 9,860.00 USD | 59,110.00 USD |
| `1D` | `304.80` | 6,370,000.00 USD | 6,370,000.00 USD | 0.00 USD | 697.80 USD | 130.30 USD | 16,360.00 USD |
| `7D` | `304.80` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 697.80 USD | 130.30 USD | 16,360.00 USD |
| `1D` | `305.20` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 9,070.00 USD | 249.40 USD | 2,010.00 USD |
| `7D` | `305.20` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 9,070.00 USD | 249.40 USD | 2,010.00 USD |
| `1D` | `305.60` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 4,670.00 USD | 1,650.00 USD | 1,500.00 USD |
| `7D` | `305.60` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 4,670.00 USD | 1,650.00 USD | 1,500.00 USD |
| `1D` | `306.00` | 6,400,000.00 USD | 6,400,000.00 USD | 0.00 USD | 9,360.00 USD | 5,830.00 USD | 3,270.00 USD |
| `7D` | `306.00` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 9,360.00 USD | 5,830.00 USD | 3,270.00 USD |
| `1D` | `306.40` | 6,420,000.00 USD | 6,420,000.00 USD | 0.00 USD | 4,230.00 USD | 9,300.00 USD | 5,670.00 USD |
| `7D` | `306.40` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 4,230.00 USD | 9,300.00 USD | 5,670.00 USD |
| `1D` | `306.80` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 28,860.00 USD | 35,370.00 USD | 5,490.00 USD |
| `7D` | `306.80` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 28,860.00 USD | 35,370.00 USD | 5,490.00 USD |
| `1D` | `307.20` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 11,230.00 USD | 27,230.00 USD | 18,140.00 USD |
| `7D` | `307.20` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 11,230.00 USD | 27,230.00 USD | 18,140.00 USD |
| `1D` | `307.60` | 6,600,000.00 USD | 6,600,000.00 USD | 0.00 USD | 14,610.00 USD | 33,780.00 USD | 3,670.00 USD |
| `7D` | `307.60` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 14,610.00 USD | 33,780.00 USD | 3,670.00 USD |
| `1D` | `308.00` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 30,270.00 USD | 20,570.00 USD | 22,690.00 USD |
| `7D` | `308.00` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 30,270.00 USD | 20,570.00 USD | 22,690.00 USD |
| `1D` | `308.40` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 5,470.00 USD | 3,530.00 USD | 4,270.00 USD |
| `7D` | `308.40` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 5,470.00 USD | 3,530.00 USD | 4,270.00 USD |
| `1D` | `308.80` | 6,700,000.00 USD | 6,700,000.00 USD | 0.00 USD | 9,910.00 USD | 369.62 USD | 3,480.00 USD |
| `7D` | `308.80` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 9,910.00 USD | 369.62 USD | 3,480.00 USD |
| `1D` | `309.20` | 6,730,000.00 USD | 6,730,000.00 USD | 0.00 USD | 10,010.00 USD | 15,050.00 USD | 2,980.00 USD |
| `7D` | `309.20` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 10,010.00 USD | 15,050.00 USD | 2,980.00 USD |
| `1D` | `309.60` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 14,370.00 USD | 14,290.00 USD | 8,230.00 USD |
| `7D` | `309.60` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 14,370.00 USD | 14,290.00 USD | 8,230.00 USD |
| `1D` | `310.00` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 8,430.00 USD | 4,640.00 USD | 6,290.00 USD |
| `7D` | `310.00` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 8,430.00 USD | 4,640.00 USD | 6,290.00 USD |
| `1D` | `310.40` | 6,800,000.00 USD | 6,800,000.00 USD | 0.00 USD | 144.00 USD | 7,080.00 USD | 9,560.00 USD |
| `7D` | `310.40` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 144.00 USD | 7,080.00 USD | 9,560.00 USD |
| `1D` | `310.80` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD | 1.49 USD |
| `7D` | `310.80` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 0.00 USD | 2,130.00 USD | 1.49 USD |
| `1D` | `311.20` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `311.20` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 431.32 USD | 2,050.00 USD | 2,760.00 USD |
| `1D` | `311.60` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 9,900.00 USD | 6,590.00 USD | 0.00 USD |
| `7D` | `311.60` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 9,900.00 USD | 6,590.00 USD | 0.00 USD |
| `1D` | `312.00` | 6,830,000.00 USD | 6,830,000.00 USD | 0.00 USD | 244.00 USD | 0.00 USD | 5.74 USD |
| `7D` | `312.00` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 244.00 USD | 0.00 USD | 5.74 USD |
| `1D` | `312.40` | 6,850,000.00 USD | 6,850,000.00 USD | 0.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD |
| `7D` | `312.40` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 8,470.00 USD | 7,480.00 USD | 2,760.00 USD |
| `1D` | `312.80` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD |
| `7D` | `312.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 11,080.00 USD | 23.27 USD | 0.96 USD |
| `1D` | `313.20` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 5,080.00 USD | 3,820.00 USD | 2,580.00 USD |
| `7D` | `313.20` | 6,970,000.00 USD | 6,970,000.00 USD | 0.00 USD | 5,080.00 USD | 3,820.00 USD | 2,580.00 USD |
| `1D` | `313.60` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD |
| `7D` | `313.60` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 11,920.00 USD | 2,890.00 USD | 0.00 USD |
| `1D` | `314.40` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD |
| `7D` | `314.40` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD |
| `1D` | `314.80` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 32.00 USD | 68.55 USD | 9,250.00 USD |
| `7D` | `314.80` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 32.00 USD | 68.55 USD | 9,250.00 USD |
| `1D` | `315.20` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 2,050.00 USD | 1,400.00 USD | 1,620.00 USD |
| `7D` | `315.20` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 2,050.00 USD | 1,400.00 USD | 1,620.00 USD |
| `1D` | `315.60` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 1,730.00 USD | 3,180.00 USD | 5,230.00 USD |
| `7D` | `315.60` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 1,730.00 USD | 3,180.00 USD | 5,230.00 USD |
| `1D` | `316.00` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `316.00` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 5,590.00 USD |
| `1D` | `316.40` | 6,930,000.00 USD | 6,930,000.00 USD | 0.00 USD | 41.00 USD | 3,070.00 USD | 0.00 USD |
| `7D` | `316.40` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 41.00 USD | 3,070.00 USD | 0.00 USD |
| `1D` | `316.80` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 12,980.00 USD | 6,830.00 USD | 7,660.00 USD |
| `7D` | `316.80` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 12,980.00 USD | 3,360.00 USD | 7,660.00 USD |
| `1D` | `317.20` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 3,660.00 USD | 6,430.00 USD | 7,170.00 USD |
| `7D` | `317.20` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 3,660.00 USD | 6,430.00 USD | 7,170.00 USD |
| `1D` | `317.60` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 14,560.00 USD | 8,990.00 USD | 17,050.00 USD |
| `7D` | `317.60` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 14,560.00 USD | 8,990.00 USD | 17,050.00 USD |
| `1D` | `318.00` | 7,050,000.00 USD | 7,050,000.00 USD | 0.00 USD | 5,970.00 USD | 12,250.00 USD | 16,750.00 USD |
| `7D` | `318.00` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 5,970.00 USD | 12,250.00 USD | 16,750.00 USD |
| `1D` | `318.40` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 234.70 USD | 5,410.00 USD | 10,400.00 USD |
| `7D` | `318.40` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 234.70 USD | 5,410.00 USD | 10,400.00 USD |
| `1D` | `318.80` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 9,210.00 USD | 10,850.00 USD | 13,930.00 USD |
| `7D` | `318.80` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 9,210.00 USD | 10,850.00 USD | 13,930.00 USD |
| `1D` | `319.20` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 7,830.00 USD | 14,510.00 USD | 488.47 USD |
| `7D` | `319.20` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 7,830.00 USD | 14,510.00 USD | 488.47 USD |
| `1D` | `319.60` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 8,500.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `319.60` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 8,500.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `320.00` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 4,190.00 USD | 6,480.00 USD | 8,330.00 USD |
| `7D` | `320.00` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 4,190.00 USD | 6,480.00 USD | 8,330.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `295.50M` | Total OI Tokens: `1,089,799.7 BCH`
  * 1h OI Change: `-6.09%` | 4h OI Change: `-7.12%` | 24h OI Change: `-9.00%`
  * Exchange Breakdown: Binance=`87.69M` | Bybit=`36.82M` | OKX=`23.16M` | Hyperliquid=`7.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `4.61K` | Last 24h: `4.21K` | Last 3d: `81.66K` | Last 7d: `135.31K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0028%` | **USDT OKX** | `-0.0068%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0018%` |
| **USDT MEXC** | `0.0027%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0050%` | **USDT Bitget** | `0.0081%` |
| **CoinM Binance** | `-0.0053%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `43.78%` | `56.22%` | `0.78` | 21,810,000.00 USD |
| `15M` | `Binance` | `47.12%` | `52.88%` | `0.89` | 9,110,000.00 USD |
| `15M` | `OKX` | `42.67%` | `57.33%` | `0.74` | 3,330,000.00 USD |
| `15M` | `Bybit` | `36.91%` | `63.09%` | `0.59` | 2,190,000.00 USD |
| `15M` | `KuCoin` | `41.2%` | `58.8%` | `0.70` | 291,380.00 USD |
| `15M` | `Gate` | `41.6%` | `58.4%` | `0.71` | 616,420.00 USD |
| `15M` | `Bitget` | `31.83%` | `68.17%` | `0.47` | 607,240.00 USD |
| `15M` | `BingX` | `47.96%` | `52.04%` | `0.92` | 207,650.00 USD |
| `15M` | `MEXC` | `34.49%` | `65.51%` | `0.53` | 553,710.00 USD |
| `15M` | `Bitunix` | `45.16%` | `54.84%` | `0.82` | 577,970.00 USD |
| `15M` | `Hyperliquid` | `22.04%` | `77.96%` | `0.28` | 365,010.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.51%` | `50.49%` | `0.98` | 3,530,000.00 USD |
| `15M` | `Crypto.com` | `4.53%` | `95.47%` | `0.05` | 424.87 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 198,820.00 USD |
| `15M` | `HTX` | `40.67%` | `59.33%` | `0.69` | 56,130.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `11.47%` | `88.53%` | `0.13` | 53,470.00 USD |
| `15M` | `Aster` | `42.7%` | `57.3%` | `0.75` | 69,830.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `35.38%` | `64.62%` | `0.55` | 52,890.00 USD |
| `15M` | `Whale Positions` | `47.12%` | `52.88%` | `0.89` | 9,110,000.00 USD |
| `15M` | `Global Accounts` | `43.78%` | `56.22%` | `0.78` | 21,810,000.00 USD |
| `1H` | `BCH` | `44.55%` | `55.45%` | `0.80` | 42,560,000.00 USD |
| `1H` | `Binance` | `47.25%` | `52.75%` | `0.90` | 16,610,000.00 USD |
| `1H` | `OKX` | `45.95%` | `54.05%` | `0.85` | 6,510,000.00 USD |
| `1H` | `Bybit` | `41.01%` | `58.99%` | `0.70` | 4,880,000.00 USD |
| `1H` | `KuCoin` | `46.57%` | `53.43%` | `0.87` | 740,290.00 USD |
| `1H` | `Gate` | `45.69%` | `54.31%` | `0.84` | 1,110,000.00 USD |
| `1H` | `Bitget` | `42.52%` | `57.48%` | `0.74` | 1,500,000.00 USD |
| `1H` | `BingX` | `36.37%` | `63.63%` | `0.57` | 676,090.00 USD |
| `1H` | `MEXC` | `38.88%` | `61.12%` | `0.64` | 787,960.00 USD |
| `1H` | `Bitunix` | `44.45%` | `55.55%` | `0.80` | 1,300,000.00 USD |
| `1H` | `Hyperliquid` | `27.3%` | `72.7%` | `0.38` | 812,460.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `47.72%` | `52.28%` | `0.91` | 6,560,000.00 USD |
| `1H` | `Crypto.com` | `38.68%` | `61.32%` | `0.63` | 604.20 USD |
| `1H` | `WhiteBIT` | `3.72%` | `96.28%` | `0.04` | 754,590.00 USD |
| `1H` | `HTX` | `42.31%` | `57.69%` | `0.73` | 61,070.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `34.83%` | `65.17%` | `0.53` | 115,670.00 USD |
| `1H` | `Aster` | `37.93%` | `62.07%` | `0.61` | 89,290.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.46%` | `63.54%` | `0.57` | 58,750.00 USD |
| `1H` | `Whale Positions` | `47.25%` | `52.75%` | `0.90` | 16,610,000.00 USD |
| `1H` | `Global Accounts` | `44.55%` | `55.45%` | `0.80` | 42,560,000.00 USD |
| `4H` | `BCH` | `45.85%` | `54.15%` | `0.85` | 83,400,000.00 USD |
| `4H` | `Binance` | `49.07%` | `50.93%` | `0.96` | 27,260,000.00 USD |
| `4H` | `OKX` | `48.09%` | `51.91%` | `0.93` | 9,970,000.00 USD |
| `4H` | `Bybit` | `45.86%` | `54.14%` | `0.85` | 9,290,000.00 USD |
| `4H` | `KuCoin` | `47.48%` | `52.52%` | `0.90` | 630,280.00 USD |
| `4H` | `Gate` | `43.96%` | `56.04%` | `0.78` | 7,900,000.00 USD |
| `4H` | `Bitget` | `37.17%` | `62.83%` | `0.59` | 2,660,000.00 USD |
| `4H` | `BingX` | `43.94%` | `56.06%` | `0.78` | 9,320,000.00 USD |
| `4H` | `MEXC` | `40.44%` | `59.56%` | `0.68` | 4,390,000.00 USD |
| `4H` | `Bitunix` | `49.35%` | `50.65%` | `0.97` | 1,370,000.00 USD |
| `4H` | `Hyperliquid` | `27.9%` | `72.1%` | `0.39` | 868,440.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.64%` | `50.36%` | `0.99` | 2,030,000.00 USD |
| `4H` | `Crypto.com` | `38.3%` | `61.7%` | `0.62` | 0.00 USD |
| `4H` | `WhiteBIT` | `1.31%` | `98.69%` | `0.01` | 6,750,000.00 USD |
| `4H` | `HTX` | `39.56%` | `60.44%` | `0.65` | 416,620.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `33.42%` | `66.58%` | `0.50` | 189,600.00 USD |
| `4H` | `Aster` | `27.39%` | `72.61%` | `0.38` | 204,450.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `36.75%` | `63.25%` | `0.58` | 129,090.00 USD |
| `4H` | `Whale Positions` | `49.07%` | `50.93%` | `0.96` | 27,260,000.00 USD |
| `4H` | `Global Accounts` | `45.85%` | `54.15%` | `0.85` | 83,400,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `286.33` | `286.94` | `286.33` | `287.87` | `285.90` | 1,269,041.85 USD | 639,367.56 USD | 629,674.29 USD | 9,693.27 USD | `+0.76%` | `32B / 48S` |
| `5:00 UTC` | `288.00` | `288.25` | `288.00` | `289.13` | `287.22` | 1,082,751.51 USD | 592,384.75 USD | 490,366.75 USD | 102,018.00 USD | `+9.42%` | `41B / 33S` |
| `0:00 UTC` | `288.00` | `287.59` | `288.00` | `288.53` | `286.82` | 774,817.75 USD | 442,366.10 USD | 332,451.65 USD | 109,914.46 USD | `+14.19%` | `38B / 28S` |
| `5:00 UTC` | `289.00` | `288.21` | `289.00` | `289.02` | `287.22` | 505,722.48 USD | 323,366.92 USD | 182,355.56 USD | 141,011.36 USD | `+27.88%` | `60B / 31S` |
| `0:00 UTC` | `288.00` | `287.86` | `288.00` | `288.89` | `287.26` | 500,104.64 USD | 252,267.65 USD | 247,836.98 USD | 4,430.67 USD | `+0.89%` | `39B / 37S` |
| `5:00 UTC` | `287.00` | `286.98` | `287.00` | `287.64` | `286.45` | 492,053.69 USD | 262,098.60 USD | 229,955.08 USD | 32,143.52 USD | `+6.53%` | `24B / 25S` |
| `0:00 UTC` | `282.00` | `283.04` | `282.00` | `286.92` | `280.48` | 5,571,232.46 USD | 2,485,967.17 USD | 3,085,265.29 USD | -599,298.12 USD | `-10.76%` | `4B / 29S` |
| `5:00 UTC` | `282.43` | `282.21` | `282.43` | `283.00` | `281.49` | 1,589,754.90 USD | 936,266.72 USD | 653,488.17 USD | 282,778.55 USD | `+17.79%` | `31B / 14S` |
| `0:00 UTC` | `275.52` | `277.16` | `275.52` | `282.40` | `273.60` | 7,176,408.30 USD | 3,429,549.36 USD | 3,746,858.94 USD | -317,309.59 USD | `-4.42%` | `7B / 13S` |
| `5:00 UTC` | `273.02` | `272.88` | `273.02` | `275.70` | `269.30` | 5,229,833.88 USD | 2,635,845.62 USD | 2,593,988.26 USD | 41,857.36 USD | `+0.80%` | `22B / 10S` |

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
| `5m` | -415,150.00 USD | -783,610.00 USD | **`DISTRIBUTION`** |
| `15m` | -366,760.00 USD | -877,190.00 USD | **`DISTRIBUTION`** |
| `30m` | -186,340.00 USD | 53,050.00 USD | **`DISTRIBUTION`** |
| `1h` | -464,940.00 USD | -1,410,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -785,060.00 USD | -514,710.00 USD | **`DISTRIBUTION`** |
| `4h` | -815,990.00 USD | 93,720.00 USD | **`DISTRIBUTION`** |
| `6h` | -867,540.00 USD | -3,680,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -354,630.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -409,780.00 USD | -1,360,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,730,000.00 USD | -10,210,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -597,890.00 USD | -13,080,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,060,000.00 USD | -137,210,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-415.15K` | 15m=`-366.76K` | 1h=`-464.94K` | 24h=`-1.73M`
* Futures Capital Netflows: 5m=`-783.61K` | 15m=`-877.19K` | 1h=`-1.41M` | 24h=`-10.21M`
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
  * `2026-10-30 02:14:39 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:39 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:21:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:20:39 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:22:39 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:22:39 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:22:39 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `276.50` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `271.28` (Risk Distance: `5.22` pts)
  * +2.5R Take Profit: `289.54`
  * Mathematical Lot Sizing: **`1.91 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `287.43` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `292.65` (Risk Distance: `5.22` pts)
  * +2.5R Take Profit: `274.39`
  * Mathematical Lot Sizing: **`1.91 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`276.52`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
