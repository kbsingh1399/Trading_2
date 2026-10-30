# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 11:11:08 IST` (`2026-10-30 05:41:08 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `284.56` | **Live Ask Quote**: `285.14` | **Mid Price**: `284.85`
- **Spread Points**: `585.00` | **Spread BPS**: `20.54 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `274.75` | VWAP Z-Score: `+1.54` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.84` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `62.98` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `293.12` | Lower -3.00σ Band: `256.37`
  * Upper +2.51σ Band: `290.12` | Lower -2.51σ Band: `259.38`
  * Upper +2.01σ Band: `287.06` | Lower -2.01σ Band: `262.44`
  * Upper +2.00σ Band: `287.00` | Lower -2.00σ Band: `262.50`
  * Upper +1.28σ Band: `282.59` | Lower -1.28σ Band: `266.91`
  * Upper +1.00σ Band: `280.87` | Lower -1.00σ Band: `268.62`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`282.18` | EMA-20=`279.68` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`279.02` (Slope: `+0.0000`) | EMA-100=`280.45`
  * Institutional Anchors: EMA-144=`281.49` | EMA-200=`282.97` (Slope: `-0.0726`) | EMA-233=`284.07`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.75` (Distance: `+2.15%`)
  * Point of Control (POC) = `276.23` (Distance: `+3.09%`)
  * Value Area Low (VAL) = `268.64` (Distance: `+6.00%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.86` | Low=`282.66`
  * New York Session (13:00-21:00 UTC): High=`286.56` | Low=`283.14`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `283.71` - `285.99`
  * Optimal Trade Entry (OTE 0.705): `285.42`
  * Structural Invalidation Anchor (0.786): `287.13`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.40` | `284.71` | `283.93` | `284.40` | `484` | 137,687.19 USD | -4,739.02 USD | `-3.44%` | -2,233,439.53 USD | `-0.03` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `284.40` | `285.15` | `284.37` | `284.97` | `406` | 115,593.72 USD | 17,510.22 USD | `+15.15%` | -2,215,929.31 USD | `+0.26` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `284.96` | `285.59` | `284.88` | `285.22` | `449` | 128,091.87 USD | 8,544.13 USD | `+6.67%` | -2,207,385.18 USD | `+0.13` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `283.51` | `285.59` | `283.46` | `283.92` | `3,278` | 932,067.73 USD | 167,554.77 USD | `+17.98%` | -2,343,314.31 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `283.93` | `285.15` | `283.91` | `284.97` | `1,528` | 434,490.61 USD | 46,292.46 USD | `+10.65%` | -2,297,021.85 USD | `-0.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `284.96` | `285.59` | `284.88` | `285.22` | `449` | 128,091.87 USD | 8,544.13 USD | `+6.67%` | -2,288,477.72 USD | `-0.06` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `276.08` | `284.75` | `276.00` | `283.99` | `21,838` | 6,138,674.85 USD | -75,926.04 USD | `-1.24%` | -2,486,653.51 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `283.99` | `287.12` | `282.33` | `283.51` | `23,256` | 6,620,902.65 USD | -28,395.05 USD | `-0.43%` | -2,515,048.57 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `283.51` | `285.59` | `283.46` | `285.26` | `5,262` | 1,496,696.06 USD | 223,501.00 USD | `+14.93%` | -2,291,547.57 USD | `+0.34` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `285.26` | `28,518` | 8,117,598.70 USD | 195,105.95 USD | `+2.40%` | -1,679,277.05 USD | `+0.40` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | 1,085,885.17 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -386,016.76 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `285.26` | `28,518` | 8,117,598.70 USD | 195,105.95 USD | `+2.40%` | -1,679,277.05 USD | `+0.40` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`284.85`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:04:06 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1955` | `0x12d2...f97f` | `LONG` | 1,032,784.90 USD | `3,627,243,000,000.00` | `303.26` | `284.80` | `0.000000` | -67,214.44 USD | `-6.51%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `282.54` | 6,657.21 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.66K USD at 282.5400 USD [API] | `2026-10-29 02:19:03` |
| `ANNOUNCEMENT` | `INFO` | `278.13` | 9,771.82 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 9.77K USD at 278.1300 USD [API] | `2026-10-29 04:05:44` |
| `ANNOUNCEMENT` | `INFO` | `278.10` | 6,043.39 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.04K USD at 278.1000 USD [API] | `2026-10-29 04:05:44` |
| `ANNOUNCEMENT` | `INFO` | `280.17` | 14,501.60 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 14.50K USD at 280.1700 USD [API] | `2026-10-29 05:08:53` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+1.20%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--7.00%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.18%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.98%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.18%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.98%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.18%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.98%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `66.50` | 2,730.00 USD | 201,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 277.83 USD | 198,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 541.71 USD | 198,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 1,110.00 USD | 198,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 146.70 USD | 196,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 196,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 195,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 189,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 185,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 185,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 3,190.00 USD | 185,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 125.50 USD | 181,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 181,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `133.50` | 2,000.00 USD | 181,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 179,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 178,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 177,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 174,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 174,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 8,280.00 USD | 174,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 165,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 165,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 165,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 164,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 164,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 2,310.00 USD | 163,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 161,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 160,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 160,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 159,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 158,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `193.50` | 1,050.00 USD | 157,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 156,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 2,290.00 USD | 155,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 153,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 153,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 152,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 152,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 42,410.00 USD | 152,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 109,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `211.50` | 6,660.00 USD | 109,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 103,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 2,610.00 USD | 99,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 96,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 5,340.00 USD | 63,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 58,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 57,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 1,320.00 USD | 57,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 1,300.00 USD | 55,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 54,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `232.50` | 632.17 USD | 54,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `234.80` | 10,900,000.00 USD | 10,900,000.00 USD | 172.38 USD | 182.78 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 10,900,000.00 USD | 10,900,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 10,880,000.00 USD | 10,880,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 10,860,000.00 USD | 10,860,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 30,780.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 10,830,000.00 USD | 10,830,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 10,820,000.00 USD | 10,820,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.80` | 10,800,000.00 USD | 10,800,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 10,770,000.00 USD | 10,770,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.30` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,760,000.00 USD | 10,760,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 10,750,000.00 USD | 10,750,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 10,740,000.00 USD | 10,740,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 10,730,000.00 USD | 10,730,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 21,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 10,640,000.00 USD | 10,640,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 19,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 10,620,000.00 USD | 10,620,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 18,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 10,570,000.00 USD | 10,570,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 10,550,000.00 USD | 10,550,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 10,520,000.00 USD | 10,520,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 10,510,000.00 USD | 10,510,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 10,460,000.00 USD | 10,460,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 10,450,000.00 USD | 10,450,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 12,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 10,410,000.00 USD | 10,410,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 10,400,000.00 USD | 10,400,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 12,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 10,390,000.00 USD | 10,390,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 10,280,000.00 USD | 10,280,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 12,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.80` | 10,210,000.00 USD | 10,210,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 10,090,000.00 USD | 10,090,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 10,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.80` | 10,000,000.00 USD | 10,000,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 9,860,000.00 USD | 9,860,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 9,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.80` | 9,720,000.00 USD | 9,720,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 9,530,000.00 USD | 9,530,000.00 USD | 69,530.00 USD | 32,580.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,590,000.00 USD | 4,590,000.00 USD | 14,310.00 USD | 5,700.00 USD | 7,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,170.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.80` | 9,410,000.00 USD | 9,410,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,560,000.00 USD | 4,560,000.00 USD | 6,910.00 USD | 6,870.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,550,000.00 USD | 4,550,000.00 USD | 6,040.00 USD | 5,400.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 9,330,000.00 USD | 9,330,000.00 USD | 37,170.00 USD | 49,360.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,520,000.00 USD | 4,520,000.00 USD | 17,280.00 USD | 17,660.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 9,220,000.00 USD | 9,220,000.00 USD | 10,460.00 USD | 32,560.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,470,000.00 USD | 4,470,000.00 USD | 1,590.00 USD | 4,460.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 9,150,000.00 USD | 9,150,000.00 USD | 44,200.00 USD | 44,160.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,460,000.00 USD | 4,460,000.00 USD | 8,310.00 USD | 10,660.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.80` | 9,040,000.00 USD | 9,040,000.00 USD | 56,440.00 USD | 38,370.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,440,000.00 USD | 4,440,000.00 USD | 9,050.00 USD | 8,770.00 USD | 17.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,430,000.00 USD | 4,430,000.00 USD | 8,970.00 USD | 7,060.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 8,870,000.00 USD | 8,870,000.00 USD | 44,970.00 USD | 12,850.00 USD | 31,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,390,000.00 USD | 4,390,000.00 USD | 14,340.00 USD | 20,270.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 8,780,000.00 USD | 8,780,000.00 USD | 12,780.00 USD | 16,980.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,340,000.00 USD | 4,340,000.00 USD | 6,390.00 USD | 17,760.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 8,720,000.00 USD | 8,720,000.00 USD | 81,660.00 USD | 24,260.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,300,000.00 USD | 4,300,000.00 USD | 7,420.00 USD | 21,020.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 4,490.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.80` | 8,560,000.00 USD | 8,560,000.00 USD | 32,750.00 USD | 21,210.00 USD | 52,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 4,270,000.00 USD | 4,270,000.00 USD | 6,970.00 USD | 5,880.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 4,250,000.00 USD | 4,250,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 8,460,000.00 USD | 8,460,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 467.62 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 4,230,000.00 USD | 4,230,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 8,430,000.00 USD | 8,430,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 4,210,000.00 USD | 4,210,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 8,360,000.00 USD | 8,360,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 4,150,000.00 USD | 4,150,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.80` | 8,140,000.00 USD | 8,140,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 4,090,000.00 USD | 4,090,000.00 USD | 6,660.00 USD | 38,650.00 USD | 31,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 4,010,000.00 USD | 4,010,000.00 USD | 15,070.00 USD | 5,740.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,960,000.00 USD | 7,960,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 3,980,000.00 USD | 3,980,000.00 USD | 19,030.00 USD | 34,280.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 7,900,000.00 USD | 7,900,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 3,880,000.00 USD | 3,880,000.00 USD | 39,480.00 USD | 8,550.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 7,750,000.00 USD | 7,750,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,830,000.00 USD | 3,830,000.00 USD | 19,180.00 USD | 1,100.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,530,000.00 USD | 7,530,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,780,000.00 USD | 3,780,000.00 USD | 9,160.00 USD | 50,690.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,710,000.00 USD | 3,710,000.00 USD | 8,130.00 USD | 29,290.00 USD | 33,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 7,390,000.00 USD | 7,390,000.00 USD | 7,150.00 USD | 97,320.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,640,000.00 USD | 3,640,000.00 USD | 15,200.00 USD | 60,480.00 USD | 51,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 7,240,000.00 USD | 7,240,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,510,000.00 USD | 3,510,000.00 USD | 13,620.00 USD | 27,330.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 7,040,000.00 USD | 7,040,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,450,000.00 USD | 3,450,000.00 USD | 20,850.00 USD | 4,730.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,860,000.00 USD | 6,860,000.00 USD | 74,900.00 USD | 49,480.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,410,000.00 USD | 3,410,000.00 USD | 366.04 USD | 12,480.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,380,000.00 USD | 3,380,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 6,710,000.00 USD | 6,710,000.00 USD | 33,590.00 USD | 13,230.00 USD | 101.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,300,000.00 USD | 3,300,000.00 USD | 41,850.00 USD | 29,870.00 USD | 41,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 6,660,000.00 USD | 6,660,000.00 USD | 391,670.00 USD | 1,380.00 USD | 117,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 3,190,000.00 USD | 3,190,000.00 USD | 46,180.00 USD | 15,290.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 6,150,000.00 USD | 6,150,000.00 USD | 48,690.00 USD | 0.00 USD | 133.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 3,110,000.00 USD | 3,110,000.00 USD | 1,020.00 USD | 19,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 6,100,000.00 USD | 6,100,000.00 USD | 33,940.00 USD | 21,410.00 USD | 165.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 3,090,000.00 USD | 3,090,000.00 USD | 33,130.00 USD | 1,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 3,000,000.00 USD | 3,000,000.00 USD | 64,510.00 USD | 1,030.00 USD | 3.40 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 6,040,000.00 USD | 6,040,000.00 USD | 256,440.00 USD | 0.00 USD | 33,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.70` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 228.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 5,750,000.00 USD | 5,750,000.00 USD | 69,380.00 USD | 0.00 USD | 109.91 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 2,940,000.00 USD | 2,940,000.00 USD | 16,000.00 USD | 13,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 5,680,000.00 USD | 5,680,000.00 USD | 216,090.00 USD | 0.00 USD | 17.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 2,910,000.00 USD | 2,910,000.00 USD | 18,860.00 USD | 8,190.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 5,470,000.00 USD | 5,470,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 2,880,000.00 USD | 2,880,000.00 USD | 31,870.00 USD | 22,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 2,820,000.00 USD | 2,820,000.00 USD | 33,120.00 USD | 68,390.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 5,270,000.00 USD | 5,270,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.70` | 2,710,000.00 USD | 2,710,000.00 USD | 4,660.00 USD | 36,050.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 5,090,000.00 USD | 5,090,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,650,000.00 USD | 2,650,000.00 USD | 4,570.00 USD | 24,460.00 USD | 63,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,790,000.00 USD | 4,790,000.00 USD | 169,940.00 USD | 148,780.00 USD | 62,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 10,610.00 USD | 6.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 4,410,000.00 USD | 4,410,000.00 USD | 23,340.00 USD | 0.00 USD | 55.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,550,000.00 USD | 2,550,000.00 USD | 8,400.00 USD | 321.80 USD | 20.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,540,000.00 USD | 2,540,000.00 USD | 178.30 USD | 703.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 1,930.00 USD | 148.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,540,000.00 USD | 2,540,000.00 USD | 378.60 USD | 16,420.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 196.31 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,500,000.00 USD | 2,500,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 120.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,490,000.00 USD | 2,490,000.00 USD | 323.80 USD | 7,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,490,000.00 USD | 2,490,000.00 USD | 12,710.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 25,790.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 4,390,000.00 USD | 4,390,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,440,000.00 USD | 2,440,000.00 USD | 15,100.00 USD | 15,900.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,390,000.00 USD | 2,390,000.00 USD | 6,060.00 USD | 16,330.00 USD | 28,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 4,250,000.00 USD | 4,250,000.00 USD | 25,660.00 USD | 69,990.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,340,000.00 USD | 2,340,000.00 USD | 55,090.00 USD | 5,420.00 USD | 64,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 2,210,000.00 USD | 2,210,000.00 USD | 9,330.00 USD | 109,460.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 70,180.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 2,080,000.00 USD | 2,080,000.00 USD | 37,900.00 USD | 59,570.00 USD | 58,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 3,800,000.00 USD | 3,800,000.00 USD | 181,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,930,000.00 USD | 1,930,000.00 USD | 161,460.00 USD | 21,230.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 3,620,000.00 USD | 3,620,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,750,000.00 USD | 1,750,000.00 USD | 235,460.00 USD | 0.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 3,060,000.00 USD | 3,060,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,460,000.00 USD | 1,460,000.00 USD | 64,430.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 2,530,000.00 USD | 2,530,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,360,000.00 USD | 1,360,000.00 USD | 20,900.00 USD | 10,450.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 2,450,000.00 USD | 2,450,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 1,280,000.00 USD | 1,280,000.00 USD | 83,200.00 USD | 0.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 2,340,000.00 USD | 2,340,000.00 USD | 153,820.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 1,190,000.00 USD | 1,190,000.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 2,080,000.00 USD | 2,080,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 1,170,000.00 USD | 1,170,000.00 USD | 37,290.00 USD | 13,540.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 1,120,000.00 USD | 1,120,000.00 USD | 301.20 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 2,070,000.00 USD | 2,070,000.00 USD | 152,190.00 USD | 63,290.00 USD | 99,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 1,090,000.00 USD | 1,090,000.00 USD | 12,120.00 USD | 53,570.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 1,540,000.00 USD | 1,540,000.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 965,430.00 USD | 965,430.00 USD | 70,120.00 USD | 56,870.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 1,380,000.00 USD | 1,380,000.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 771,540.00 USD | 771,540.00 USD | 11,140.00 USD | 63,940.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.30` | 683,790.00 USD | 683,790.00 USD | 0.00 USD | 21,610.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 1,330,000.00 USD | 1,330,000.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 644,240.00 USD | 644,240.00 USD | 14,720.00 USD | 21,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 608,210.00 USD | 608,210.00 USD | 0.00 USD | 26,770.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.30` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 521,600.00 USD | 521,600.00 USD | 34,230.00 USD | 53,570.00 USD | 68,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 1,300,000.00 USD | 1,300,000.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 365,250.00 USD | 365,250.00 USD | 8,730.00 USD | 18,530.00 USD | 12.68 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 337,970.00 USD | 337,970.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.70` | 318,300.00 USD | 318,300.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.80` | 1,190,000.00 USD | 1,190,000.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 312,890.00 USD | 312,890.00 USD | 10,310.00 USD | 15,980.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 993,730.00 USD | 993,730.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.50` | 282,450.00 USD | 282,450.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.90` | 269,700.00 USD | 269,700.00 USD | 14,930.00 USD | 52,180.00 USD | 35.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 202,560.00 USD | 202,560.00 USD | 1,280.00 USD | 20,630.00 USD | 31.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 969,510.00 USD | 969,510.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.80` | 867,870.00 USD | 867,870.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 180,620.00 USD | 180,620.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.30` | 865,870.00 USD | 865,870.00 USD | 1,560.00 USD | 174,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.50` | 176,820.00 USD | 176,820.00 USD | 0.00 USD | 397.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.80` | 689,330.00 USD | 689,330.00 USD | 0.00 USD | 310,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.90` | 176,420.00 USD | 176,420.00 USD | 8,460.00 USD | 948.40 USD | 9.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.30` | 167,000.00 USD | 167,000.00 USD | 86,260.00 USD | 0.00 USD | 80,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.30` | 379,310.00 USD | 379,310.00 USD | 68,860.00 USD | 227,210.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 93,130.00 USD | 93,130.00 USD | 93,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 198,590.00 USD | 198,590.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 129,010.00 USD | 129,010.00 USD | 11,950.00 USD | 719.80 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 242,800.00 USD | 242,800.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 164,350.00 USD | 164,350.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 490,490.00 USD | 490,490.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 283,550.00 USD | 283,550.00 USD | 32,920.00 USD | 5,570.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 387,790.00 USD | 387,790.00 USD | 19,920.00 USD | 50,650.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 689,850.00 USD | 689,850.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 472,230.00 USD | 472,230.00 USD | 17,310.00 USD | 17,270.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,020,000.00 USD | 1,020,000.00 USD | 4,240.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 533,060.00 USD | 533,060.00 USD | 21,420.00 USD | 14,780.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 35,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 627,980.00 USD | 627,980.00 USD | 52,260.00 USD | 22,180.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 1,260,000.00 USD | 1,260,000.00 USD | 124,780.00 USD | 1,140.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 656,360.00 USD | 656,360.00 USD | 18,130.00 USD | 10,240.00 USD | 17.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 735,480.00 USD | 735,480.00 USD | 12,780.00 USD | 15,140.00 USD | 51,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 894,460.00 USD | 894,460.00 USD | 52,150.00 USD | 44,920.00 USD | 61,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 1,610,000.00 USD | 1,610,000.00 USD | 51,310.00 USD | 101,040.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,060,000.00 USD | 1,060,000.00 USD | 43,080.00 USD | 39,910.00 USD | 84,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 1,650,000.00 USD | 1,650,000.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,220,000.00 USD | 1,220,000.00 USD | 4,230.00 USD | 104,380.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 1,650,000.00 USD | 1,650,000.00 USD | 898.13 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,310,000.00 USD | 1,310,000.00 USD | 34,600.00 USD | 39,180.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 1,330,000.00 USD | 1,330,000.00 USD | 8,960.00 USD | 11,300.00 USD | 2.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 1,680,000.00 USD | 1,680,000.00 USD | 24,680.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 1,390,000.00 USD | 1,390,000.00 USD | 2,040.00 USD | 38,580.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 1,880,000.00 USD | 1,880,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 1,440,000.00 USD | 1,440,000.00 USD | 854.05 USD | 37,580.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 1,960,000.00 USD | 1,960,000.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 1,470,000.00 USD | 1,470,000.00 USD | 22,320.00 USD | 994.05 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,060,000.00 USD | 2,060,000.00 USD | 887.27 USD | 100,630.00 USD | 138.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 1,530,000.00 USD | 1,530,000.00 USD | 32,260.00 USD | 23,980.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 1,590,000.00 USD | 1,590,000.00 USD | 10,900.00 USD | 23,080.00 USD | 27,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 2,190,000.00 USD | 2,190,000.00 USD | 534.50 USD | 132,080.00 USD | 36.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 1,770,000.00 USD | 1,770,000.00 USD | 76,770.00 USD | 41,410.00 USD | 60,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 2,230,000.00 USD | 2,230,000.00 USD | 38,790.00 USD | 1,860.00 USD | 126.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 1,860,000.00 USD | 1,860,000.00 USD | 21,360.00 USD | 21,910.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 2,630,000.00 USD | 2,630,000.00 USD | 217,140.00 USD | 33,590.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,090,000.00 USD | 2,090,000.00 USD | 83,190.00 USD | 69,460.00 USD | 85,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 2,890,000.00 USD | 2,890,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 2,170,000.00 USD | 2,170,000.00 USD | 31,140.00 USD | 86.80 USD | 48,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 2,320,000.00 USD | 2,320,000.00 USD | 15,420.00 USD | 49,460.00 USD | 83,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 3,370,000.00 USD | 3,370,000.00 USD | 46,330.00 USD | 83,210.00 USD | 345,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 2,540,000.00 USD | 2,540,000.00 USD | 94,310.00 USD | 6,630.00 USD | 121,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 3,770,000.00 USD | 3,770,000.00 USD | 165,320.00 USD | 72,570.00 USD | 167,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 2,740,000.00 USD | 2,740,000.00 USD | 44,070.00 USD | 114,650.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 4,100,000.00 USD | 4,100,000.00 USD | 43,710.00 USD | 167,290.00 USD | 120,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 2,820,000.00 USD | 2,820,000.00 USD | 30,870.00 USD | 22,430.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `296.80` | 4,410,000.00 USD | 4,410,000.00 USD | 133,820.00 USD | 2,910.00 USD | 172,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 2,940,000.00 USD | 2,940,000.00 USD | 21,800.00 USD | 21,450.00 USD | 78,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 3,030,000.00 USD | 3,030,000.00 USD | 61,250.00 USD | 805.28 USD | 31,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 4,550,000.00 USD | 4,550,000.00 USD | 78,980.00 USD | 53,400.00 USD | 72.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 3,070,000.00 USD | 3,070,000.00 USD | 15,870.00 USD | 10,830.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 4,780,000.00 USD | 4,780,000.00 USD | 47,530.00 USD | 99,320.00 USD | 89,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 3,170,000.00 USD | 3,170,000.00 USD | 51,630.00 USD | 8,080.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 4,930,000.00 USD | 4,930,000.00 USD | 32,650.00 USD | 42,710.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 3,240,000.00 USD | 3,240,000.00 USD | 5,160.00 USD | 929.37 USD | 56,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `298.50` | 442.08 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `298.80` | 5,010,000.00 USD | 5,010,000.00 USD | 69,820.00 USD | 12,040.00 USD | 112.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 3,360,000.00 USD | 3,360,000.00 USD | 28,150.00 USD | 5,530.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 3,420,000.00 USD | 3,420,000.00 USD | 33,970.00 USD | 10,510.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 5,120,000.00 USD | 5,120,000.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 3,470,000.00 USD | 3,470,000.00 USD | 8,070.00 USD | 10,660.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 5,180,000.00 USD | 5,180,000.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 3,590,000.00 USD | 3,590,000.00 USD | 19,640.00 USD | 36,540.00 USD | 64,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 5,210,000.00 USD | 5,210,000.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 3,630,000.00 USD | 3,630,000.00 USD | 23,000.00 USD | 1,410.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 14,550.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `300.80` | 5,360,000.00 USD | 5,360,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 3,660,000.00 USD | 3,660,000.00 USD | 269.05 USD | 866.42 USD | 29,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 3,700,000.00 USD | 3,700,000.00 USD | 597.00 USD | 15,110.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 5,640,000.00 USD | 5,640,000.00 USD | 73,320.00 USD | 57,720.00 USD | 150,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 3,740,000.00 USD | 3,740,000.00 USD | 19,840.00 USD | 8,210.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 5,890,000.00 USD | 5,890,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 3,810,000.00 USD | 3,810,000.00 USD | 25,190.00 USD | 30,470.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 6,070,000.00 USD | 6,070,000.00 USD | 1,560.00 USD | 180,380.00 USD | 39.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 3,870,000.00 USD | 3,870,000.00 USD | 13,820.00 USD | 12,980.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 6,290,000.00 USD | 6,290,000.00 USD | 71,700.00 USD | 111,440.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 3,890,000.00 USD | 3,890,000.00 USD | 1,180.00 USD | 1,560.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 3,920,000.00 USD | 3,920,000.00 USD | 20,650.00 USD | 2,520.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 968.59 USD | 183.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 302.70 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 6,350,000.00 USD | 6,350,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 3,990,000.00 USD | 3,990,000.00 USD | 21,920.00 USD | 1,930.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 6,380,000.00 USD | 6,380,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 4,040,000.00 USD | 4,040,000.00 USD | 9,530.00 USD | 2,100.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 6,430,000.00 USD | 6,430,000.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 4,060,000.00 USD | 4,060,000.00 USD | 9,920.00 USD | 8,480.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 4,070,000.00 USD | 4,070,000.00 USD | 1,930.00 USD | 172.52 USD | 2,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 6,860,000.00 USD | 6,860,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 4,090,000.00 USD | 4,090,000.00 USD | 10,640.00 USD | 4,710.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 7,010,000.00 USD | 7,010,000.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 4,110,000.00 USD | 4,110,000.00 USD | 7,390.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 7,170,000.00 USD | 7,170,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 4,120,000.00 USD | 4,120,000.00 USD | 4,290.00 USD | 40.30 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 7,400,000.00 USD | 7,400,000.00 USD | 94,690.00 USD | 74,180.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 4,200,000.00 USD | 4,200,000.00 USD | 31,880.00 USD | 43,430.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 4,290,000.00 USD | 4,290,000.00 USD | 7,900.00 USD | 48,680.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 7,700,000.00 USD | 7,700,000.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 4,350,000.00 USD | 4,350,000.00 USD | 28,880.00 USD | 30,430.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 7,990,000.00 USD | 7,990,000.00 USD | 115,070.00 USD | 113,210.00 USD | 60,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 4,400,000.00 USD | 4,400,000.00 USD | 25,640.00 USD | 11,300.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 8,330,000.00 USD | 8,330,000.00 USD | 169,010.00 USD | 59,350.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 4,420,000.00 USD | 4,420,000.00 USD | 4,640.00 USD | 3,470.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 8,500,000.00 USD | 8,500,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 4,430,000.00 USD | 4,430,000.00 USD | 9,380.00 USD | 5,860.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 4,440,000.00 USD | 4,440,000.00 USD | 2,280.00 USD | 436.11 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 8,610,000.00 USD | 8,610,000.00 USD | 34,260.00 USD | 36,240.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 4,460,000.00 USD | 4,460,000.00 USD | 8,420.00 USD | 5,400.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 8,960,000.00 USD | 8,960,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 4,480,000.00 USD | 4,480,000.00 USD | 8,290.00 USD | 6,510.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 9,190,000.00 USD | 9,190,000.00 USD | 49,020.00 USD | 108,410.00 USD | 80,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 4,490,000.00 USD | 4,490,000.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 9,310,000.00 USD | 9,310,000.00 USD | 60,910.00 USD | 51,380.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 4,490,000.00 USD | 4,490,000.00 USD | 5,080.00 USD | 0.00 USD | 2.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 4,490,000.00 USD | 4,490,000.00 USD | 257.90 USD | 160.90 USD | 6.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 9,550,000.00 USD | 9,550,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 4,510,000.00 USD | 4,510,000.00 USD | 7,100.00 USD | 6,700.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 9,620,000.00 USD | 9,620,000.00 USD | 25,080.00 USD | 11,240.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 4,530,000.00 USD | 4,530,000.00 USD | 244.00 USD | 4,180.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 9,710,000.00 USD | 9,710,000.00 USD | 43,780.00 USD | 11,410.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 4,560,000.00 USD | 4,560,000.00 USD | 14,340.00 USD | 5,500.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 9,770,000.00 USD | 9,770,000.00 USD | 29,300.00 USD | 20,380.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 4,570,000.00 USD | 4,570,000.00 USD | 5,500.00 USD | 23.27 USD | 4,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 4,590,000.00 USD | 4,590,000.00 USD | 3,580.00 USD | 15,840.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 9,890,000.00 USD | 9,890,000.00 USD | 54,040.00 USD | 18,790.00 USD | 45,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 4,600,000.00 USD | 4,600,000.00 USD | 3,580.00 USD | 4,500.00 USD | 3,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 9,970,000.00 USD | 9,970,000.00 USD | 33,220.00 USD | 9,030.00 USD | 32,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 10,050,000.00 USD | 10,050,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 4,620,000.00 USD | 4,620,000.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 10,090,000.00 USD | 10,090,000.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 3,660.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 4,630,000.00 USD | 4,630,000.00 USD | 2,020.00 USD | 1,550.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 10,090,000.00 USD | 10,090,000.00 USD | 500.10 USD | 547.95 USD | 9.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 4,640,000.00 USD | 4,640,000.00 USD | 1,850.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 10,170,000.00 USD | 10,170,000.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 4,650,000.00 USD | 4,650,000.00 USD | 2,080.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 10,270,000.00 USD | 10,270,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 10,330,000.00 USD | 10,330,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 10,350,000.00 USD | 10,350,000.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 10,380,000.00 USD | 10,380,000.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 10,450,000.00 USD | 10,450,000.00 USD | 3,320.00 USD | 32,080.00 USD | 32,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.80` | 10,510,000.00 USD | 10,510,000.00 USD | 10,810.00 USD | 18,090.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.30` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 17,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 23,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `323.50` | 2,220.00 USD | 25,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 51,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `339.50` | 1,360.00 USD | 52,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 53,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 53,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `374.50` | 41,200.00 USD | 95,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 141,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `477.50` | 8,200.00 USD | 149,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 150,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 151,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `66.50` | 201,600.00 USD | 0.00 USD | 2,730.00 USD | `-76.56%` | `41,012,000,000.00` |
| `Live` | `Long` | `73.50` | 198,870.00 USD | 0.00 USD | 277.83 USD | `-74.09%` | `3,780,000,000.00` |
| `Live` | `Long` | `75.50` | 198,590.00 USD | 0.00 USD | 541.71 USD | `-73.38%` | `7,175,000,000.00` |
| `Live` | `Long` | `84.50` | 198,050.00 USD | 0.00 USD | 1,110.00 USD | `-70.21%` | `13,105,000,000.00` |
| `Live` | `Long` | `93.50` | 196,950.00 USD | 0.00 USD | 146.70 USD | `-67.04%` | `1,569,000,000.00` |
| `Live` | `Long` | `95.50` | 196,800.00 USD | 0.00 USD | 920.05 USD | `-66.33%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 195,880.00 USD | 0.00 USD | 6,240.00 USD | `-64.22%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 189,640.00 USD | 0.00 USD | 4,080.00 USD | `-63.87%` | `39,797,000,000.00` |
| `Live` | `Long` | `109.50` | 185,560.00 USD | 0.00 USD | 212.76 USD | `-61.40%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 185,350.00 USD | 0.00 USD | 212.35 USD | `-58.23%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 185,140.00 USD | 0.00 USD | 3,190.00 USD | `-56.82%` | `26,016,000,000.00` |
| `Live` | `Long` | `125.50` | 181,950.00 USD | 0.00 USD | 125.50 USD | `-55.76%` | `1,000,000,000.00` |
| `Live` | `Long` | `126.50` | 181,830.00 USD | 0.00 USD | 658.18 USD | `-55.41%` | `5,203,000,000.00` |
| `Live` | `Long` | `133.50` | 181,170.00 USD | 0.00 USD | 2,000.00 USD | `-52.94%` | `15,000,000,000.00` |
| `Live` | `Long` | `147.50` | 179,170.00 USD | 0.00 USD | 895.47 USD | `-48.00%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 178,270.00 USD | 0.00 USD | 1,270.00 USD | `-47.65%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 177,000.00 USD | 0.00 USD | 2,370.00 USD | `-47.30%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 174,640.00 USD | 0.00 USD | 303.78 USD | `-46.24%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 174,330.00 USD | 0.00 USD | 325.00 USD | `-42.72%` | `2,000,000,000.00` |
| `Live` | `Long` | `165.50` | 174,010.00 USD | 0.00 USD | 8,280.00 USD | `-41.66%` | `50,000,000,000.00` |
| `Live` | `Long` | `167.50` | 165,730.00 USD | 0.00 USD | 285.75 USD | `-40.95%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 165,450.00 USD | 0.00 USD | 426.25 USD | `-39.89%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 165,020.00 USD | 0.00 USD | 169.96 USD | `-38.48%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 164,850.00 USD | 0.00 USD | 516.67 USD | `-38.13%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 164,340.00 USD | 0.00 USD | 373.83 USD | `-37.78%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 163,960.00 USD | 0.00 USD | 2,310.00 USD | `-35.31%` | `12,599,000,000.00` |
| `Live` | `Long` | `184.50` | 161,650.00 USD | 0.00 USD | 808.66 USD | `-34.96%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 160,840.00 USD | 0.00 USD | 418.28 USD | `-33.55%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 160,420.00 USD | 0.00 USD | 694.75 USD | `-32.84%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 159,730.00 USD | 0.00 USD | 858.49 USD | `-32.49%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 158,870.00 USD | 0.00 USD | 1,490.00 USD | `-32.14%` | `7,715,000,000.00` |
| `Live` | `Long` | `193.50` | 157,380.00 USD | 0.00 USD | 1,050.00 USD | `-31.79%` | `5,434,000,000.00` |
| `Live` | `Long` | `195.50` | 156,330.00 USD | 0.00 USD | 370.47 USD | `-31.08%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 155,960.00 USD | 0.00 USD | 2,290.00 USD | `-30.73%` | `11,644,000,000.00` |
| `Live` | `Long` | `199.50` | 153,670.00 USD | 0.00 USD | 548.03 USD | `-29.67%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 153,130.00 USD | 0.00 USD | 293.13 USD | `-29.32%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 152,830.00 USD | 0.00 USD | 420.39 USD | `-28.61%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 152,410.00 USD | 0.00 USD | 191.53 USD | `-27.56%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 152,220.00 USD | 0.00 USD | 42,410.00 USD | `-27.20%` | `205,387,000,000.00` |
| `Live` | `Long` | `210.50` | 109,810.00 USD | 0.00 USD | 108.83 USD | `-25.79%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 109,700.00 USD | 0.00 USD | 6,660.00 USD | `-25.44%` | `31,500,000,000.00` |
| `Live` | `Long` | `213.50` | 103,040.00 USD | 0.00 USD | 3,800.00 USD | `-24.74%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 99,230.00 USD | 0.00 USD | 2,610.00 USD | `-24.03%` | `12,132,000,000.00` |
| `Live` | `Long` | `223.50` | 96,620.00 USD | 0.00 USD | 32,860.00 USD | `-21.21%` | `147,023,000,000.00` |
| `Live` | `Long` | `224.50` | 63,760.00 USD | 0.00 USD | 5,340.00 USD | `-20.86%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 58,420.00 USD | 0.00 USD | 1,240.00 USD | `-20.15%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 57,180.00 USD | 0.00 USD | 174.49 USD | `-19.80%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 57,010.00 USD | 0.00 USD | 1,320.00 USD | `-19.45%` | `5,783,000,000.00` |
| `Live` | `Long` | `229.50` | 55,680.00 USD | 0.00 USD | 1,300.00 USD | `-19.10%` | `5,671,000,000.00` |
| `Live` | `Long` | `231.50` | 54,380.00 USD | 0.00 USD | 295.86 USD | `-18.39%` | `1,278,000,000.00` |
| `Live` | `Long` | `232.50` | 54,090.00 USD | 0.00 USD | 632.17 USD | `-18.04%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 53,460.00 USD | 0.00 USD | 30,780.00 USD | `-16.28%` | `129,590,000,000.00` |
| `Live` | `Long` | `239.50` | 22,680.00 USD | 0.00 USD | 1,030.00 USD | `-15.57%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 21,650.00 USD | 0.00 USD | 251.88 USD | `-14.87%` | `1,043,000,000.00` |
| `Live` | `Long` | `242.50` | 21,400.00 USD | 0.00 USD | 1,520.00 USD | `-14.51%` | `6,274,000,000.00` |
| `Live` | `Long` | `243.50` | 19,880.00 USD | 0.00 USD | 1,850.00 USD | `-14.16%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 18,030.00 USD | 0.00 USD | 4,220.00 USD | `-13.81%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 13,810.00 USD | 0.00 USD | 1,030.00 USD | `-13.46%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 12,780.00 USD | 0.00 USD | 106.67 USD | `-12.75%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 12,670.00 USD | 0.00 USD | 595.16 USD | `-12.40%` | `2,395,000,000.00` |
| `Live` | `Long` | `249.50` | 12,080.00 USD | 0.00 USD | 1,590.00 USD | `-12.05%` | `6,354,000,000.00` |
| `Live` | `Long` | `250.50` | 10,490.00 USD | 0.00 USD | 1,330.00 USD | `-11.69%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 9,170.00 USD | 0.00 USD | 268.35 USD | `-11.34%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 8,900.00 USD | 0.00 USD | 1,170.00 USD | `-10.99%` | `4,639,000,000.00` |
| `Live` | `Long` | `254.50` | 7,730.00 USD | 0.00 USD | 548.45 USD | `-10.28%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 7,180.00 USD | 0.00 USD | 4,490.00 USD | `-9.58%` | `17,514,000,000.00` |
| `Live` | `Long` | `257.50` | 2,690.00 USD | 0.00 USD | 467.62 USD | `-9.23%` | `1,816,000,000.00` |
| `Live` | `Long` | `258.50` | 2,220.00 USD | 0.00 USD | 176.56 USD | `-8.87%` | `683,000,000.00` |
| `Live` | `Long` | `260.50` | 2,040.00 USD | 0.00 USD | 2,040.00 USD | `-8.17%` | `7,839,000,000.00` |
| `Live` | `Short` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | `+1.35%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 1,070.00 USD | 954.95 USD | 0.00 USD | `+2.76%` | `3,276,000,000.00` |
| `Live` | `Short` | `296.50` | 7,200.00 USD | 6,130.00 USD | 0.00 USD | `+4.52%` | `20,668,000,000.00` |
| `Live` | `Short` | `298.50` | 7,640.00 USD | 442.08 USD | 0.00 USD | `+5.23%` | `1,481,000,000.00` |
| `Live` | `Short` | `300.50` | 22,180.00 USD | 14,550.00 USD | 0.00 USD | `+5.93%` | `48,404,000,000.00` |
| `Live` | `Short` | `320.50` | 23,290.00 USD | 1,110.00 USD | 0.00 USD | `+12.98%` | `3,452,000,000.00` |
| `Live` | `Short` | `323.50` | 25,510.00 USD | 2,220.00 USD | 0.00 USD | `+14.04%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 51,040.00 USD | 25,530.00 USD | 0.00 USD | `+15.10%` | `78,189,000,000.00` |
| `Live` | `Short` | `339.50` | 52,390.00 USD | 1,360.00 USD | 0.00 USD | `+19.68%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 53,400.00 USD | 1,010.00 USD | 0.00 USD | `+26.38%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 53,850.00 USD | 445.52 USD | 0.00 USD | `+29.90%` | `1,209,000,000.00` |
| `Live` | `Short` | `374.50` | 95,040.00 USD | 41,200.00 USD | 0.00 USD | `+32.02%` | `110,000,000,000.00` |
| `Live` | `Short` | `459.50` | 141,300.00 USD | 46,250.00 USD | 0.00 USD | `+61.98%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 149,500.00 USD | 8,200.00 USD | 0.00 USD | `+68.33%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 150,210.00 USD | 718.34 USD | 0.00 USD | `+75.73%` | `1,441,000,000.00` |
| `Live` | `Short` | `560.50` | 151,060.00 USD | 842.43 USD | 0.00 USD | `+97.59%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 449,470.00 USD | 0.00 USD | 210.94 USD | `-49.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 449,260.00 USD | 0.00 USD | 2,070.00 USD | `-48.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 447,190.00 USD | 0.00 USD | 489.38 USD | `-41.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 446,700.00 USD | 0.00 USD | 2,530.00 USD | `-37.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 444,170.00 USD | 0.00 USD | 490.59 USD | `-34.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 443,680.00 USD | 0.00 USD | 482.01 USD | `-30.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 443,200.00 USD | 0.00 USD | 189.07 USD | `-29.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 443,010.00 USD | 0.00 USD | 441.60 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 442,570.00 USD | 0.00 USD | 299.96 USD | `-25.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 442,270.00 USD | 0.00 USD | 715.29 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 441,550.00 USD | 0.00 USD | 638.36 USD | `-21.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 440,920.00 USD | 0.00 USD | 740.85 USD | `-20.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 440,170.00 USD | 0.00 USD | 478.48 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 439,700.00 USD | 0.00 USD | 389.48 USD | `-17.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 439,310.00 USD | 0.00 USD | 812.38 USD | `-16.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 438,490.00 USD | 0.00 USD | 220.64 USD | `-16.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 438,270.00 USD | 0.00 USD | 429.30 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 437,840.00 USD | 0.00 USD | 296.50 USD | `-15.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 437,550.00 USD | 0.00 USD | 216.45 USD | `-15.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 437,330.00 USD | 0.00 USD | 387.76 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 436,940.00 USD | 0.00 USD | 9,420.00 USD | `-13.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 427,530.00 USD | 0.00 USD | 1,630.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 425,900.00 USD | 0.00 USD | 2,700.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 423,200.00 USD | 0.00 USD | 2,940.00 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 420,260.00 USD | 0.00 USD | 4,560.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 415,700.00 USD | 0.00 USD | 1,850.00 USD | `-11.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 413,850.00 USD | 0.00 USD | 231.54 USD | `-10.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 413,620.00 USD | 0.00 USD | 109.26 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 413,510.00 USD | 0.00 USD | 1,780.00 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 411,730.00 USD | 0.00 USD | 51,300.00 USD | `-9.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 360,430.00 USD | 0.00 USD | 250.81 USD | `-9.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 360,180.00 USD | 0.00 USD | 2,370.00 USD | `-8.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 357,810.00 USD | 0.00 USD | 269,800.00 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 88,020.00 USD | 0.00 USD | 857.85 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 87,160.00 USD | 0.00 USD | 320.15 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 86,840.00 USD | 0.00 USD | 199.17 USD | `-6.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 86,640.00 USD | 0.00 USD | 2,180.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 84,460.00 USD | 0.00 USD | 241.98 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 84,220.00 USD | 0.00 USD | 219.35 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 84,000.00 USD | 0.00 USD | 107.40 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 83,890.00 USD | 0.00 USD | 29,530.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 54,370.00 USD | 0.00 USD | 3,340.00 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 51,020.00 USD | 0.00 USD | 620.38 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 50,400.00 USD | 0.00 USD | 13,500.00 USD | `-3.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 36,910.00 USD | 0.00 USD | 1,010.00 USD | `-3.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 35,890.00 USD | 0.00 USD | 667.86 USD | `-3.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 35,220.00 USD | 0.00 USD | 299.74 USD | `-2.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 34,920.00 USD | 0.00 USD | 903.60 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 34,020.00 USD | 0.00 USD | 326.34 USD | `-2.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 33,690.00 USD | 0.00 USD | 125.88 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 33,570.00 USD | 0.00 USD | 21,990.00 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 11,580.00 USD | 0.00 USD | 3,080.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 8,500.00 USD | 0.00 USD | 104.72 USD | `-0.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 8,400.00 USD | 0.00 USD | 355.67 USD | `-0.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 8,040.00 USD | 0.00 USD | 8,040.00 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 2,010.00 USD | 2,010.00 USD | 0.00 USD | `+0.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 3,060.00 USD | 1,050.00 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 3,340.00 USD | 280.77 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 8,500.00 USD | 5,160.00 USD | 0.00 USD | `+1.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 8,760.00 USD | 261.96 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 9,290.00 USD | 530.36 USD | 0.00 USD | `+2.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 11,440.00 USD | 2,150.00 USD | 0.00 USD | `+2.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 36,720.00 USD | 25,280.00 USD | 0.00 USD | `+2.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 36,820.00 USD | 107.05 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 37,820.00 USD | 992.62 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 39,840.00 USD | 2,020.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 44,560.00 USD | 4,730.00 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 44,670.00 USD | 110.37 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 45,060.00 USD | 388.95 USD | 0.00 USD | `+5.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 45,220.00 USD | 153.94 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 55,990.00 USD | 10,780.00 USD | 0.00 USD | `+5.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 66,720.00 USD | 10,730.00 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 69,370.00 USD | 2,650.00 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 69,470.00 USD | 102.73 USD | 0.00 USD | `+8.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 83,970.00 USD | 14,500.00 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 84,600.00 USD | 634.04 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 85,640.00 USD | 1,030.00 USD | 0.00 USD | `+11.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 91,290.00 USD | 5,650.00 USD | 0.00 USD | `+12.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 91,820.00 USD | 534.59 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 92,140.00 USD | 321.50 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 158,860.00 USD | 66,720.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 159,950.00 USD | 1,090.00 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 171,940.00 USD | 12,000.00 USD | 0.00 USD | `+17.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 172,490.00 USD | 547.52 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 172,600.00 USD | 110.91 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 172,860.00 USD | 257.45 USD | 0.00 USD | `+22.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 173,030.00 USD | 174.25 USD | 0.00 USD | `+22.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 173,190.00 USD | 151.50 USD | 0.00 USD | `+23.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 174,640.00 USD | 1,450.00 USD | 0.00 USD | `+26.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 176,410.00 USD | 1,770.00 USD | 0.00 USD | `+26.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 176,740.00 USD | 326.07 USD | 0.00 USD | `+27.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 177,570.00 USD | 826.60 USD | 0.00 USD | `+28.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 185,010.00 USD | 7,440.00 USD | 0.00 USD | `+28.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 185,690.00 USD | 682.84 USD | 0.00 USD | `+30.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 186,790.00 USD | 1,100.00 USD | 0.00 USD | `+34.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 187,480.00 USD | 683.96 USD | 0.00 USD | `+39.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 187,680.00 USD | 199.75 USD | 0.00 USD | `+40.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 188,970.00 USD | 1,290.00 USD | 0.00 USD | `+41.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 190,010.00 USD | 1,040.00 USD | 0.00 USD | `+42.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 190,380.00 USD | 376.71 USD | 0.00 USD | `+42.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 190,540.00 USD | 158.86 USD | 0.00 USD | `+44.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 196,440.00 USD | 5,900.00 USD | 0.00 USD | `+46.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 197,520.00 USD | 1,080.00 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 199,220.00 USD | 1,700.00 USD | 0.00 USD | `+50.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 200,770.00 USD | 1,550.00 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 202,160.00 USD | 1,380.00 USD | 0.00 USD | `+53.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 202,780.00 USD | 621.14 USD | 0.00 USD | `+53.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 205,060.00 USD | 2,280.00 USD | 0.00 USD | `+55.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 205,280.00 USD | 222.75 USD | 0.00 USD | `+57.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 212,200.00 USD | 6,920.00 USD | 0.00 USD | `+58.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 218,120.00 USD | 5,920.00 USD | 0.00 USD | `+59.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 219,250.00 USD | 1,130.00 USD | 0.00 USD | `+62.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 226,880.00 USD | 7,630.00 USD | 0.00 USD | `+70.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 227,860.00 USD | 975.00 USD | 0.00 USD | `+71.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 228,840.00 USD | 981.00 USD | 0.00 USD | `+72.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 229,340.00 USD | 499.50 USD | 0.00 USD | `+76.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,120,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+76.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,120,000.00 USD | 1,000.00 USD | 0.00 USD | `+76.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,120,000.00 USD | 1,040.00 USD | 0.00 USD | `+82.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,120,000.00 USD | 340.67 USD | 0.00 USD | `+84.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,120,000.00 USD | 638.86 USD | 0.00 USD | `+96.18%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.80` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 172.38 USD | 182.78 USD | 3,090.00 USD |
| `7D` | `235.30` | 10,900,000.00 USD | 0.00 USD | 10,900,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 10,890,000.00 USD | 0.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `236.30` | 10,880,000.00 USD | 0.00 USD | 10,880,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `236.80` | 10,860,000.00 USD | 0.00 USD | 10,860,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD |
| `7D` | `237.30` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 10,830,000.00 USD | 0.00 USD | 10,830,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD |
| `7D` | `238.30` | 10,820,000.00 USD | 0.00 USD | 10,820,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD |
| `7D` | `238.80` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 10,770,000.00 USD | 0.00 USD | 10,770,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.30` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD |
| `7D` | `240.80` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 10,740,000.00 USD | 0.00 USD | 10,740,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.30` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD |
| `7D` | `243.30` | 10,640,000.00 USD | 0.00 USD | 10,640,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.30` | 10,550,000.00 USD | 0.00 USD | 10,550,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 10,460,000.00 USD | 0.00 USD | 10,460,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD |
| `7D` | `247.30` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.80` | 10,410,000.00 USD | 0.00 USD | 10,410,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD |
| `7D` | `248.30` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD |
| `7D` | `248.80` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD |
| `7D` | `249.30` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD |
| `7D` | `249.80` | 10,210,000.00 USD | 0.00 USD | 10,210,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD |
| `7D` | `250.30` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD |
| `7D` | `250.80` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD |
| `7D` | `251.30` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,120.00 USD |
| `7D` | `251.80` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD |
| `7D` | `252.30` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 69,530.00 USD | 32,580.00 USD | 17,360.00 USD |
| `1D` | `252.50` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 14,310.00 USD | 5,700.00 USD | 7,960.00 USD |
| `7D` | `252.80` | 9,410,000.00 USD | 0.00 USD | 9,410,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD |
| `1D` | `252.90` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 6,910.00 USD | 6,870.00 USD | 2,830.00 USD |
| `1D` | `253.30` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 6,040.00 USD | 5,400.00 USD | 14,780.00 USD |
| `7D` | `253.30` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 37,170.00 USD | 49,360.00 USD | 20,250.00 USD |
| `1D` | `253.70` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 17,280.00 USD | 17,660.00 USD | 12,010.00 USD |
| `7D` | `253.80` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 10,460.00 USD | 32,560.00 USD | 28,070.00 USD |
| `1D` | `254.10` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 1,590.00 USD | 4,460.00 USD | 3,940.00 USD |
| `7D` | `254.30` | 9,150,000.00 USD | 0.00 USD | 9,150,000.00 USD | 44,200.00 USD | 44,160.00 USD | 25,760.00 USD |
| `1D` | `254.50` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 8,310.00 USD | 10,660.00 USD | 2.31 USD |
| `7D` | `254.80` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 56,440.00 USD | 38,370.00 USD | 77,340.00 USD |
| `1D` | `254.90` | 4,440,000.00 USD | 0.00 USD | 4,440,000.00 USD | 9,050.00 USD | 8,770.00 USD | 17.15 USD |
| `1D` | `255.30` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 8,970.00 USD | 7,060.00 USD | 22,440.00 USD |
| `7D` | `255.30` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 44,970.00 USD | 12,850.00 USD | 31,380.00 USD |
| `1D` | `255.70` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 14,340.00 USD | 20,270.00 USD | 11,800.00 USD |
| `7D` | `255.80` | 8,780,000.00 USD | 0.00 USD | 8,780,000.00 USD | 12,780.00 USD | 16,980.00 USD | 29,500.00 USD |
| `1D` | `256.10` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 6,390.00 USD | 17,760.00 USD | 13,780.00 USD |
| `7D` | `256.30` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 81,660.00 USD | 24,260.00 USD | 48,030.00 USD |
| `1D` | `256.50` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 7,420.00 USD | 21,020.00 USD | 9,270.00 USD |
| `7D` | `256.80` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 32,750.00 USD | 21,210.00 USD | 52,750.00 USD |
| `1D` | `256.90` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 6,970.00 USD | 5,880.00 USD | 5,430.00 USD |
| `1D` | `257.30` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD |
| `7D` | `257.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD |
| `1D` | `257.70` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD |
| `7D` | `257.80` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD |
| `7D` | `258.30` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD |
| `1D` | `258.50` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.80` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD |
| `1D` | `258.90` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 6,660.00 USD | 38,650.00 USD | 31,030.00 USD |
| `1D` | `259.30` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 15,070.00 USD | 5,740.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 7,960,000.00 USD | 0.00 USD | 7,960,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD |
| `1D` | `259.70` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 19,030.00 USD | 34,280.00 USD | 39,300.00 USD |
| `7D` | `259.80` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD |
| `1D` | `260.10` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 39,480.00 USD | 8,550.00 USD | 6,870.00 USD |
| `7D` | `260.30` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD |
| `1D` | `260.50` | 3,830,000.00 USD | 0.00 USD | 3,830,000.00 USD | 19,180.00 USD | 1,100.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 7,530,000.00 USD | 0.00 USD | 7,530,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,240.00 USD |
| `1D` | `260.90` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 9,160.00 USD | 50,690.00 USD | 13,930.00 USD |
| `1D` | `261.30` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 8,130.00 USD | 29,290.00 USD | 33,410.00 USD |
| `7D` | `261.30` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 7,150.00 USD | 97,320.00 USD | 52,540.00 USD |
| `1D` | `261.70` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 15,200.00 USD | 60,480.00 USD | 51,230.00 USD |
| `7D` | `261.80` | 7,240,000.00 USD | 0.00 USD | 7,240,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD |
| `1D` | `262.10` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 13,620.00 USD | 27,330.00 USD | 21,370.00 USD |
| `7D` | `262.30` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD |
| `1D` | `262.50` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 20,850.00 USD | 4,730.00 USD | 10,850.00 USD |
| `7D` | `262.80` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 74,900.00 USD | 49,480.00 USD | 32,720.00 USD |
| `1D` | `262.90` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 366.04 USD | 12,480.00 USD | 19,480.00 USD |
| `1D` | `263.30` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,440.00 USD |
| `7D` | `263.30` | 6,710,000.00 USD | 0.00 USD | 6,710,000.00 USD | 33,590.00 USD | 13,230.00 USD | 101.93 USD |
| `1D` | `263.70` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 41,850.00 USD | 29,870.00 USD | 41,330.00 USD |
| `7D` | `263.80` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 391,670.00 USD | 1,380.00 USD | 117,860.00 USD |
| `1D` | `264.10` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 46,180.00 USD | 15,290.00 USD | 17,150.00 USD |
| `7D` | `264.30` | 6,150,000.00 USD | 0.00 USD | 6,150,000.00 USD | 48,690.00 USD | 0.00 USD | 133.80 USD |
| `1D` | `264.50` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 1,020.00 USD | 19,610.00 USD | 0.00 USD |
| `7D` | `264.80` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 33,940.00 USD | 21,410.00 USD | 165.00 USD |
| `1D` | `264.90` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 33,130.00 USD | 1,190.00 USD | 53,200.00 USD |
| `1D` | `265.30` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 64,510.00 USD | 1,030.00 USD | 3.40 USD |
| `7D` | `265.30` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 256,440.00 USD | 0.00 USD | 33,980.00 USD |
| `1D` | `265.70` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 0.00 USD | 228.00 USD | 0.00 USD |
| `7D` | `265.80` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 69,380.00 USD | 0.00 USD | 109.91 USD |
| `1D` | `266.10` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 16,000.00 USD | 13,250.00 USD | 0.00 USD |
| `7D` | `266.30` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 216,090.00 USD | 0.00 USD | 17.82 USD |
| `1D` | `266.50` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 18,860.00 USD | 8,190.00 USD | 4,800.00 USD |
| `7D` | `266.80` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD |
| `1D` | `266.90` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 31,870.00 USD | 22,170.00 USD | 0.00 USD |
| `1D` | `267.30` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 33,120.00 USD | 68,390.00 USD | 12,550.00 USD |
| `7D` | `267.30` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD |
| `1D` | `267.70` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 4,660.00 USD | 36,050.00 USD | 14,900.00 USD |
| `7D` | `267.80` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,820.00 USD |
| `1D` | `268.10` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 4,570.00 USD | 24,460.00 USD | 63,570.00 USD |
| `7D` | `268.30` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 169,940.00 USD | 148,780.00 USD | 62,780.00 USD |
| `1D` | `268.50` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 0.00 USD | 10,610.00 USD | 6.84 USD |
| `7D` | `268.80` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 23,340.00 USD | 0.00 USD | 55.96 USD |
| `1D` | `268.90` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 8,400.00 USD | 321.80 USD | 20.82 USD |
| `1D` | `269.30` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 178.30 USD | 703.50 USD | 0.00 USD |
| `7D` | `269.30` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 1,930.00 USD | 148.23 USD |
| `1D` | `269.70` | 2,540,000.00 USD | 0.00 USD | 2,540,000.00 USD | 378.60 USD | 16,420.00 USD | 13,580.00 USD |
| `7D` | `269.80` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 196.31 USD |
| `1D` | `270.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD |
| `7D` | `270.30` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD |
| `1D` | `270.50` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `270.80` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 120.25 USD |
| `1D` | `270.90` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 323.80 USD | 7,970.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 12,710.00 USD | 0.00 USD | 2,750.00 USD |
| `1D` | `271.70` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 0.00 USD | 25,790.00 USD | 5,300.00 USD |
| `7D` | `271.80` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD |
| `1D` | `272.10` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 15,100.00 USD | 15,900.00 USD | 19,770.00 USD |
| `7D` | `272.30` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 6,060.00 USD | 16,330.00 USD | 28,120.00 USD |
| `7D` | `272.80` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 25,660.00 USD | 69,990.00 USD | 47,720.00 USD |
| `1D` | `272.90` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 55,090.00 USD | 5,420.00 USD | 64,890.00 USD |
| `1D` | `273.30` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 9,330.00 USD | 109,460.00 USD | 10,240.00 USD |
| `7D` | `273.30` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 0.00 USD | 70,180.00 USD | 240,480.00 USD |
| `1D` | `273.70` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 37,900.00 USD | 59,570.00 USD | 58,180.00 USD |
| `7D` | `273.80` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 181,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.10` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 161,460.00 USD | 21,230.00 USD | 6.00 USD |
| `7D` | `274.30` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 235,460.00 USD | 0.00 USD | 54,030.00 USD |
| `7D` | `274.80` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `274.90` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 64,430.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.30` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `275.30` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.70` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 20,900.00 USD | 10,450.00 USD | 53,200.00 USD |
| `7D` | `275.80` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD |
| `1D` | `276.10` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 83,200.00 USD | 0.00 USD | 7,090.00 USD |
| `7D` | `276.30` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 153,820.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD |
| `7D` | `276.80` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 37,290.00 USD | 13,540.00 USD | 5,500.00 USD |
| `1D` | `277.30` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 301.20 USD | 0.00 USD | 10,600.00 USD |
| `7D` | `277.30` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 152,190.00 USD | 63,290.00 USD | 99,240.00 USD |
| `1D` | `277.70` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD |
| `7D` | `277.80` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD |
| `1D` | `278.10` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 12,120.00 USD | 53,570.00 USD | 56,220.00 USD |
| `7D` | `278.30` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD |
| `1D` | `278.50` | 965,430.00 USD | 0.00 USD | 965,430.00 USD | 70,120.00 USD | 56,870.00 USD | 66,900.00 USD |
| `7D` | `278.80` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD |
| `1D` | `278.90` | 771,540.00 USD | 0.00 USD | 771,540.00 USD | 11,140.00 USD | 63,940.00 USD | 12,660.00 USD |
| `1D` | `279.30` | 683,790.00 USD | 0.00 USD | 683,790.00 USD | 0.00 USD | 21,610.00 USD | 17,940.00 USD |
| `7D` | `279.30` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 644,240.00 USD | 0.00 USD | 644,240.00 USD | 14,720.00 USD | 21,310.00 USD | 0.00 USD |
| `7D` | `279.80` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `280.10` | 608,210.00 USD | 0.00 USD | 608,210.00 USD | 0.00 USD | 26,770.00 USD | 59,840.00 USD |
| `7D` | `280.30` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD |
| `1D` | `280.50` | 521,600.00 USD | 0.00 USD | 521,600.00 USD | 34,230.00 USD | 53,570.00 USD | 68,550.00 USD |
| `7D` | `280.80` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `280.90` | 365,250.00 USD | 0.00 USD | 365,250.00 USD | 8,730.00 USD | 18,530.00 USD | 12.68 USD |
| `1D` | `281.30` | 337,970.00 USD | 0.00 USD | 337,970.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD |
| `7D` | `281.30` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `1D` | `281.70` | 318,300.00 USD | 0.00 USD | 318,300.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 312,890.00 USD | 0.00 USD | 312,890.00 USD | 10,310.00 USD | 15,980.00 USD | 4,140.00 USD |
| `7D` | `282.30` | 993,730.00 USD | 0.00 USD | 993,730.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.50` | 282,450.00 USD | 0.00 USD | 282,450.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD |
| `1D` | `282.90` | 269,700.00 USD | 0.00 USD | 269,700.00 USD | 14,930.00 USD | 52,180.00 USD | 35.51 USD |
| `1D` | `283.30` | 202,560.00 USD | 0.00 USD | 202,560.00 USD | 1,280.00 USD | 20,630.00 USD | 31.75 USD |
| `7D` | `283.30` | 969,510.00 USD | 0.00 USD | 969,510.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD |
| `7D` | `283.80` | 867,870.00 USD | 0.00 USD | 867,870.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 180,620.00 USD | 0.00 USD | 180,620.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD |
| `7D` | `284.30` | 865,870.00 USD | 0.00 USD | 865,870.00 USD | 1,560.00 USD | 174,980.00 USD | 0.00 USD |
| `1D` | `284.50` | 176,820.00 USD | 0.00 USD | 176,820.00 USD | 0.00 USD | 397.40 USD | 0.00 USD |
| `7D` | `284.80` | 689,330.00 USD | 0.00 USD | 689,330.00 USD | 0.00 USD | 310,010.00 USD | 0.00 USD |
| `1D` | `284.90` | 176,420.00 USD | 0.00 USD | 176,420.00 USD | 8,460.00 USD | 948.40 USD | 9.04 USD |
| `1D` | `285.30` | 167,000.00 USD | 0.00 USD | 167,000.00 USD | 86,260.00 USD | 0.00 USD | 80,730.00 USD |
| `7D` | `285.30` | 379,310.00 USD | 0.00 USD | 379,310.00 USD | 68,860.00 USD | 227,210.00 USD | 83,240.00 USD |
| `7D` | `285.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `285.60` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `285.70` | 93,130.00 USD | 93,130.00 USD | 0.00 USD | 93,130.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `285.80` | 198,590.00 USD | 198,590.00 USD | 0.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD |
| `1D` | `286.10` | 129,010.00 USD | 129,010.00 USD | 0.00 USD | 11,950.00 USD | 719.80 USD | 23,210.00 USD |
| `7D` | `286.30` | 242,800.00 USD | 242,800.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD |
| `1D` | `286.50` | 164,350.00 USD | 164,350.00 USD | 0.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD |
| `7D` | `286.80` | 490,490.00 USD | 490,490.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 283,550.00 USD | 283,550.00 USD | 0.00 USD | 32,920.00 USD | 5,570.00 USD | 80,710.00 USD |
| `1D` | `287.30` | 387,790.00 USD | 387,790.00 USD | 0.00 USD | 19,920.00 USD | 50,650.00 USD | 33,670.00 USD |
| `7D` | `287.30` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD |
| `1D` | `287.70` | 472,230.00 USD | 472,230.00 USD | 0.00 USD | 17,310.00 USD | 17,270.00 USD | 49,860.00 USD |
| `7D` | `287.80` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 4,240.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.10` | 533,060.00 USD | 533,060.00 USD | 0.00 USD | 21,420.00 USD | 14,780.00 USD | 24,620.00 USD |
| `7D` | `288.30` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 0.00 USD |
| `1D` | `288.50` | 627,980.00 USD | 627,980.00 USD | 0.00 USD | 52,260.00 USD | 22,180.00 USD | 20,480.00 USD |
| `7D` | `288.80` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 124,780.00 USD | 1,140.00 USD | 80,970.00 USD |
| `1D` | `288.90` | 656,360.00 USD | 656,360.00 USD | 0.00 USD | 18,130.00 USD | 10,240.00 USD | 17.54 USD |
| `1D` | `289.30` | 735,480.00 USD | 735,480.00 USD | 0.00 USD | 12,780.00 USD | 15,140.00 USD | 51,210.00 USD |
| `7D` | `289.30` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.70` | 894,460.00 USD | 894,460.00 USD | 0.00 USD | 52,150.00 USD | 44,920.00 USD | 61,910.00 USD |
| `7D` | `289.80` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 134,010.00 USD |
| `1D` | `290.10` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 43,080.00 USD | 39,910.00 USD | 84,680.00 USD |
| `7D` | `290.30` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 4,230.00 USD | 104,380.00 USD | 46,650.00 USD |
| `7D` | `290.80` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 898.13 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `290.90` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 34,600.00 USD | 39,180.00 USD | 17,940.00 USD |
| `1D` | `291.30` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 8,960.00 USD | 11,300.00 USD | 2.42 USD |
| `7D` | `291.30` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 24,680.00 USD | 10,160.00 USD | 0.00 USD |
| `1D` | `291.70` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 2,040.00 USD | 38,580.00 USD | 22,170.00 USD |
| `7D` | `291.80` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 854.05 USD | 37,580.00 USD | 11,510.00 USD |
| `7D` | `292.30` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD |
| `1D` | `292.50` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 22,320.00 USD | 994.05 USD | 2,240.00 USD |
| `7D` | `292.80` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 887.27 USD | 100,630.00 USD | 138.60 USD |
| `1D` | `292.90` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 32,260.00 USD | 23,980.00 USD | 3,560.00 USD |
| `1D` | `293.30` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 10,900.00 USD | 23,080.00 USD | 27,370.00 USD |
| `7D` | `293.30` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 534.50 USD | 132,080.00 USD | 36.33 USD |
| `1D` | `293.70` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 76,770.00 USD | 41,410.00 USD | 60,310.00 USD |
| `7D` | `293.80` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 126.44 USD |
| `1D` | `294.10` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 21,360.00 USD | 21,910.00 USD | 44,840.00 USD |
| `7D` | `294.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 217,140.00 USD | 33,590.00 USD | 146,150.00 USD |
| `1D` | `294.50` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 83,190.00 USD | 69,460.00 USD | 85,220.00 USD |
| `7D` | `294.80` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD |
| `1D` | `294.90` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 31,140.00 USD | 86.80 USD | 48,700.00 USD |
| `1D` | `295.30` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 15,420.00 USD | 49,460.00 USD | 83,010.00 USD |
| `7D` | `295.30` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 46,330.00 USD | 83,210.00 USD | 345,510.00 USD |
| `1D` | `295.70` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 94,310.00 USD | 6,630.00 USD | 121,700.00 USD |
| `7D` | `295.80` | 3,770,000.00 USD | 3,770,000.00 USD | 0.00 USD | 165,320.00 USD | 72,570.00 USD | 167,420.00 USD |
| `1D` | `296.10` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 44,070.00 USD | 114,650.00 USD | 33,000.00 USD |
| `7D` | `296.30` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 43,710.00 USD | 167,290.00 USD | 120,790.00 USD |
| `1D` | `296.50` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 30,870.00 USD | 22,430.00 USD | 29,580.00 USD |
| `7D` | `296.80` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 133,820.00 USD | 2,910.00 USD | 172,360.00 USD |
| `1D` | `296.90` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 21,800.00 USD | 21,450.00 USD | 78,160.00 USD |
| `1D` | `297.30` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 61,250.00 USD | 805.28 USD | 31,480.00 USD |
| `7D` | `297.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 78,980.00 USD | 53,400.00 USD | 72.03 USD |
| `1D` | `297.70` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 15,870.00 USD | 10,830.00 USD | 12,070.00 USD |
| `7D` | `297.80` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 47,530.00 USD | 99,320.00 USD | 89,560.00 USD |
| `1D` | `298.10` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 51,630.00 USD | 8,080.00 USD | 41,570.00 USD |
| `7D` | `298.30` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 32,650.00 USD | 42,710.00 USD | 68,810.00 USD |
| `1D` | `298.50` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 5,160.00 USD | 929.37 USD | 56,410.00 USD |
| `7D` | `298.80` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 69,820.00 USD | 12,040.00 USD | 112.32 USD |
| `1D` | `298.90` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 28,150.00 USD | 5,530.00 USD | 94,670.00 USD |
| `1D` | `299.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 33,970.00 USD | 10,510.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD |
| `1D` | `299.70` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 8,070.00 USD | 10,660.00 USD | 27,680.00 USD |
| `7D` | `299.80` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD |
| `1D` | `300.10` | 3,590,000.00 USD | 3,590,000.00 USD | 0.00 USD | 19,640.00 USD | 36,540.00 USD | 64,300.00 USD |
| `7D` | `300.30` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD |
| `1D` | `300.50` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 23,000.00 USD | 1,410.00 USD | 17,180.00 USD |
| `7D` | `300.80` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,300.00 USD |
| `1D` | `300.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 269.05 USD | 866.42 USD | 29,440.00 USD |
| `1D` | `301.30` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 597.00 USD | 15,110.00 USD | 20,870.00 USD |
| `7D` | `301.30` | 5,640,000.00 USD | 5,640,000.00 USD | 0.00 USD | 73,320.00 USD | 57,720.00 USD | 150,400.00 USD |
| `1D` | `301.70` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 19,840.00 USD | 8,210.00 USD | 15,430.00 USD |
| `7D` | `301.80` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,330.00 USD |
| `1D` | `302.10` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 25,190.00 USD | 30,470.00 USD | 10,360.00 USD |
| `7D` | `302.30` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 1,560.00 USD | 180,380.00 USD | 39.94 USD |
| `1D` | `302.50` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 13,820.00 USD | 12,980.00 USD | 38,380.00 USD |
| `7D` | `302.80` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 71,700.00 USD | 111,440.00 USD | 41,780.00 USD |
| `1D` | `302.90` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 1,180.00 USD | 1,560.00 USD | 13,980.00 USD |
| `1D` | `303.30` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 20,650.00 USD | 2,520.00 USD | 9,360.00 USD |
| `7D` | `303.30` | 6,300,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 968.59 USD | 183.84 USD |
| `1D` | `303.70` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 302.70 USD | 1.44 USD |
| `7D` | `303.80` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD |
| `1D` | `304.10` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 21,920.00 USD | 1,930.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD |
| `1D` | `304.50` | 4,040,000.00 USD | 4,040,000.00 USD | 0.00 USD | 9,530.00 USD | 2,100.00 USD | 44,520.00 USD |
| `7D` | `304.80` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD |
| `1D` | `304.90` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 9,920.00 USD | 8,480.00 USD | 2,030.00 USD |
| `1D` | `305.30` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 1,930.00 USD | 172.52 USD | 2,010.00 USD |
| `7D` | `305.30` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD |
| `1D` | `305.70` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 10,640.00 USD | 4,710.00 USD | 7,360.00 USD |
| `7D` | `305.80` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD |
| `1D` | `306.10` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 7,390.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD |
| `1D` | `306.50` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 4,290.00 USD | 40.30 USD | 5,670.00 USD |
| `7D` | `306.80` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 94,690.00 USD | 74,180.00 USD | 70,010.00 USD |
| `1D` | `306.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 31,880.00 USD | 43,430.00 USD | 13,060.00 USD |
| `1D` | `307.30` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 7,900.00 USD | 48,680.00 USD | 25,510.00 USD |
| `7D` | `307.30` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD |
| `1D` | `307.70` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 28,880.00 USD | 30,430.00 USD | 6,160.00 USD |
| `7D` | `307.80` | 7,990,000.00 USD | 7,990,000.00 USD | 0.00 USD | 115,070.00 USD | 113,210.00 USD | 60,720.00 USD |
| `1D` | `308.10` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 25,640.00 USD | 11,300.00 USD | 16,370.00 USD |
| `7D` | `308.30` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 169,010.00 USD | 59,350.00 USD | 114,230.00 USD |
| `1D` | `308.50` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 4,640.00 USD | 3,470.00 USD | 3,000.00 USD |
| `7D` | `308.80` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD |
| `1D` | `308.90` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 9,380.00 USD | 5,860.00 USD | 4,140.00 USD |
| `1D` | `309.30` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 2,280.00 USD | 436.11 USD | 2,150.00 USD |
| `7D` | `309.30` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 34,260.00 USD | 36,240.00 USD | 36,580.00 USD |
| `1D` | `309.70` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 8,420.00 USD | 5,400.00 USD | 3,030.00 USD |
| `7D` | `309.80` | 8,960,000.00 USD | 8,960,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,830.00 USD |
| `1D` | `310.10` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 8,290.00 USD | 6,510.00 USD | 11,020.00 USD |
| `7D` | `310.30` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 49,020.00 USD | 108,410.00 USD | 80,780.00 USD |
| `1D` | `310.50` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD |
| `7D` | `310.80` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 3,850.00 USD |
| `1D` | `310.90` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 2.31 USD |
| `1D` | `311.30` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 257.90 USD | 160.90 USD | 6.94 USD |
| `7D` | `311.30` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,850.00 USD |
| `1D` | `311.70` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 7,100.00 USD | 6,700.00 USD | 4,060.00 USD |
| `7D` | `311.80` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 25,080.00 USD | 11,240.00 USD | 25,570.00 USD |
| `1D` | `312.10` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 244.00 USD | 4,180.00 USD | 9,550.00 USD |
| `7D` | `312.30` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 43,580.00 USD |
| `1D` | `312.50` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 14,340.00 USD | 5,500.00 USD | 11,780.00 USD |
| `7D` | `312.80` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 29,300.00 USD | 20,380.00 USD | 7,420.00 USD |
| `1D` | `312.90` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 5,500.00 USD | 23.27 USD | 4,360.00 USD |
| `1D` | `313.30` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 3,580.00 USD | 15,840.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 54,040.00 USD | 18,790.00 USD | 45,480.00 USD |
| `1D` | `313.70` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 3,580.00 USD | 4,500.00 USD | 3,590.00 USD |
| `7D` | `313.80` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 33,220.00 USD | 9,030.00 USD | 32,550.00 USD |
| `1D` | `314.10` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.30` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `1D` | `314.50` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `314.80` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `314.90` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 3,660.00 USD | 4,830.00 USD |
| `1D` | `315.30` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 2,020.00 USD | 1,550.00 USD | 1,620.00 USD |
| `7D` | `315.30` | 10,090,000.00 USD | 10,090,000.00 USD | 0.00 USD | 500.10 USD | 547.95 USD | 9.16 USD |
| `1D` | `315.70` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 1,850.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `315.80` | 10,170,000.00 USD | 10,170,000.00 USD | 0.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD |
| `1D` | `316.10` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 2,080.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `316.30` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD |
| `7D` | `316.80` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD |
| `7D` | `317.30` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD |
| `7D` | `317.80` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD |
| `7D` | `318.30` | 10,450,000.00 USD | 10,450,000.00 USD | 0.00 USD | 3,320.00 USD | 32,080.00 USD | 32,130.00 USD |
| `7D` | `318.80` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 10,810.00 USD | 18,090.00 USD | 37,810.00 USD |
| `7D` | `319.30` | 10,530,000.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 17,950.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `308.45M` | Total OI Tokens: `1,082,696.0 BCH`
  * 1h OI Change: `+0.22%` | 4h OI Change: `+3.32%` | 24h OI Change: `-1.33%`
  * Exchange Breakdown: Binance=`90.18M` | Bybit=`38.76M` | OKX=`24.14M` | Hyperliquid=`7.27M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.43K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0071%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `53.97%` | `46.03%` | `1.17` | 2,940,000.00 USD |
| `15M` | `Binance` | `50.74%` | `49.26%` | `1.03` | 780,580.00 USD |
| `15M` | `OKX` | `45.23%` | `54.77%` | `0.83` | 261,350.00 USD |
| `15M` | `Bybit` | `67.91%` | `32.09%` | `2.12` | 308,460.00 USD |
| `15M` | `KuCoin` | `46%` | `54%` | `0.85` | 20,510.00 USD |
| `15M` | `Gate` | `28.05%` | `71.95%` | `0.39` | 418,570.00 USD |
| `15M` | `Bitget` | `82.74%` | `17.26%` | `4.79` | 63,430.00 USD |
| `15M` | `BingX` | `51.79%` | `48.21%` | `1.07` | 456,340.00 USD |
| `15M` | `MEXC` | `26.81%` | `73.19%` | `0.37` | 127,070.00 USD |
| `15M` | `Bitunix` | `36.06%` | `63.94%` | `0.56` | 41,500.00 USD |
| `15M` | `Hyperliquid` | `82.81%` | `17.19%` | `4.82` | 30,070.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `39.04%` | `60.96%` | `0.64` | 86,410.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.68%` | `1.32%` | `74.76` | 335,970.00 USD |
| `15M` | `HTX` | `93.11%` | `6.89%` | `13.51` | 3,190.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `100%` | `0%` | `1.00` | 128.15 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `97.18%` | `2.82%` | `34.46` | 3,420.00 USD |
| `15M` | `Whale Positions` | `50.74%` | `49.26%` | `1.03` | 780,580.00 USD |
| `15M` | `Global Accounts` | `53.97%` | `46.03%` | `1.17` | 2,940,000.00 USD |
| `1H` | `BCH` | `50.53%` | `49.47%` | `1.02` | 10,020,000.00 USD |
| `1H` | `Binance` | `48.71%` | `51.29%` | `0.95` | 2,950,000.00 USD |
| `1H` | `OKX` | `53.11%` | `46.89%` | `1.13` | 1,240,000.00 USD |
| `1H` | `Bybit` | `58.47%` | `41.53%` | `1.41` | 956,450.00 USD |
| `1H` | `KuCoin` | `47.39%` | `52.61%` | `0.90` | 124,910.00 USD |
| `1H` | `Gate` | `42.2%` | `57.8%` | `0.73` | 1,030,000.00 USD |
| `1H` | `Bitget` | `76.56%` | `23.44%` | `3.27` | 282,250.00 USD |
| `1H` | `BingX` | `42.66%` | `57.34%` | `0.74` | 2,110,000.00 USD |
| `1H` | `MEXC` | `21.17%` | `78.83%` | `0.27` | 302,740.00 USD |
| `1H` | `Bitunix` | `57.82%` | `42.18%` | `1.37` | 169,180.00 USD |
| `1H` | `Hyperliquid` | `37.66%` | `62.34%` | `0.60` | 119,670.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.4%` | `49.6%` | `1.02` | 262,900.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `98.71%` | `1.29%` | `76.52` | 439,760.00 USD |
| `1H` | `HTX` | `75.9%` | `24.1%` | `3.15` | 19,710.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `98.11%` | `1.89%` | `51.91` | 989.22 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `97.56%` | `2.44%` | `39.98` | 7,920.00 USD |
| `1H` | `Whale Positions` | `48.71%` | `51.29%` | `0.95` | 2,950,000.00 USD |
| `1H` | `Global Accounts` | `50.53%` | `49.47%` | `1.02` | 10,020,000.00 USD |
| `4H` | `BCH` | `48.58%` | `51.42%` | `0.94` | 52,800,000.00 USD |
| `4H` | `Binance` | `45.6%` | `54.4%` | `0.84` | 16,690,000.00 USD |
| `4H` | `OKX` | `49.68%` | `50.32%` | `0.99` | 6,750,000.00 USD |
| `4H` | `Bybit` | `53.91%` | `46.09%` | `1.17` | 4,170,000.00 USD |
| `4H` | `KuCoin` | `47.79%` | `52.21%` | `0.92` | 462,480.00 USD |
| `4H` | `Gate` | `46.92%` | `53.08%` | `0.88` | 4,740,000.00 USD |
| `4H` | `Bitget` | `53.64%` | `46.36%` | `1.16` | 1,960,000.00 USD |
| `4H` | `BingX` | `40.81%` | `59.19%` | `0.69` | 9,730,000.00 USD |
| `4H` | `MEXC` | `51.13%` | `48.87%` | `1.05` | 2,600,000.00 USD |
| `4H` | `Bitunix` | `50.08%` | `49.92%` | `1.00` | 1,520,000.00 USD |
| `4H` | `Hyperliquid` | `56.02%` | `43.98%` | `1.27` | 919,490.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.1%` | `48.9%` | `1.04` | 1,600,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `98.82%` | `1.18%` | `83.75` | 1,420,000.00 USD |
| `4H` | `HTX` | `54.18%` | `45.82%` | `1.18` | 110,830.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `45.71%` | `54.29%` | `0.84` | 17,190.00 USD |
| `4H` | `Aster` | `69.58%` | `30.42%` | `2.29` | 96,500.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `84.44%` | `15.56%` | `5.43` | 22,820.00 USD |
| `4H` | `Whale Positions` | `45.6%` | `54.4%` | `0.84` | 16,690,000.00 USD |
| `4H` | `Global Accounts` | `48.58%` | `51.42%` | `0.94` | 52,800,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `278.75` | `278.95` | `278.75` | `279.99` | `277.87` | 899,043.00 USD | 507,720.36 USD | 391,322.65 USD | 116,397.71 USD | `+12.95%` | `23B / 14S` |
| `0:00 UTC` | `281.80` | `281.23` | `281.80` | `282.56` | `279.38` | 1,860,973.61 USD | 1,019,031.48 USD | 841,942.13 USD | 177,089.35 USD | `+9.52%` | `29B / 17S` |
| `5:00 UTC` | `282.40` | `283.39` | `282.40` | `284.76` | `281.82` | 2,261,635.40 USD | 1,044,285.27 USD | 1,217,350.14 USD | -173,064.87 USD | `-7.65%` | `26B / 23S` |
| `0:00 UTC` | `287.03` | `284.86` | `287.03` | `287.15` | `282.35` | 3,497,591.91 USD | 1,841,198.98 USD | 1,656,392.94 USD | 184,806.04 USD | `+5.28%` | `24B / 10S` |
| `5:00 UTC` | `284.49` | `285.18` | `284.49` | `286.67` | `284.13` | 976,529.89 USD | 414,772.25 USD | 561,757.64 USD | -146,985.38 USD | `-15.05%` | `8B / 33S` |
| `0:00 UTC` | `284.00` | `284.42` | `284.00` | `285.15` | `283.77` | 825,459.63 USD | 394,600.86 USD | 430,858.77 USD | -36,257.91 USD | `-4.39%` | `20B / 24S` |
| `5:00 UTC` | `284.75` | `284.10` | `284.75` | `284.97` | `283.36` | 1,321,321.21 USD | 645,681.70 USD | 675,639.51 USD | -29,957.81 USD | `-2.27%` | `33B / 48S` |
| `0:00 UTC` | `284.87` | `284.37` | `284.87` | `285.61` | `283.47` | 932,067.73 USD | 549,811.25 USD | 382,256.48 USD | 167,554.77 USD | `+17.98%` | `21B / 18S` |
| `5:00 UTC` | `284.45` | `284.39` | `284.45` | `285.15` | `283.92` | 434,490.61 USD | 240,391.53 USD | 194,099.07 USD | 46,292.46 USD | `+10.65%` | `28B / 17S` |
| `0:00 UTC` | `285.50` | `285.11` | `285.50` | `285.60` | `284.69` | 329,436.68 USD | 161,636.87 USD | 167,799.81 USD | -6,162.94 USD | `-1.87%` | `18B / 31S` |

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
| `5m` | -1,240.00 USD | 22,010.00 USD | **`ACCUMULATION`** |
| `15m` | 22,560.00 USD | 160,870.00 USD | **`ACCUMULATION`** |
| `30m` | 69,940.00 USD | 281,240.00 USD | **`ACCUMULATION`** |
| `1h` | 75,050.00 USD | 727,490.00 USD | **`ACCUMULATION`** |
| `2h` | 601,680.00 USD | 612,730.00 USD | **`ACCUMULATION`** |
| `4h` | 1,020,000.00 USD | -605,200.00 USD | **`ACCUMULATION`** |
| `6h` | 511,660.00 USD | 1,640,000.00 USD | **`ACCUMULATION`** |
| `8h` | 693,110.00 USD | -595,150.00 USD | **`ACCUMULATION`** |
| `12h` | -253,960.00 USD | -1,380,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 69,300.00 USD | -4,180,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -917,890.00 USD | -14,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,300,000.00 USD | -137,080,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-1.24K` | 15m=`+22.56K` | 1h=`+75.05K` | 24h=`+69.30K`
* Futures Capital Netflows: 5m=`+22.01K` | 15m=`+160.87K` | 1h=`+727.49K` | 24h=`-4.18M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `268.64` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `264.35` (Risk Distance: `4.29` pts)
  * +2.5R Take Profit: `279.36`
  * Mathematical Lot Sizing: **`2.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `283.04` (Risk Distance: `4.29` pts)
  * +2.5R Take Profit: `268.03`
  * Mathematical Lot Sizing: **`2.33 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`287.13`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
