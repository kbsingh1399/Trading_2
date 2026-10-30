# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 11:05:06 IST` (`2026-10-30 05:35:06 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `1962` | `0x12d2...f97f` | `LONG` | 1,031,733.00 USD | `3,627,243,000,000.00` | `303.26` | `284.35` | `0.000000` | -68,266.34 USD | `-6.62%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`288.85` (Vol: 247,200.00 USD, Dist: `+1.80%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.45%`)
  * 48H Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
  * 3D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.78%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.42%`)
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
| `7D` | `Long Liquidation` | `234.70` | 10,120,000.00 USD | 10,120,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.20` | 10,110,000.00 USD | 10,110,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.70` | 10,100,000.00 USD | 10,100,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.20` | 10,090,000.00 USD | 10,090,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.70` | 10,070,000.00 USD | 10,070,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.20` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 30,780.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.70` | 10,040,000.00 USD | 10,040,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.20` | 10,030,000.00 USD | 10,030,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.70` | 10,010,000.00 USD | 10,010,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.20` | 9,980,000.00 USD | 9,980,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.70` | 9,970,000.00 USD | 9,970,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.70` | 9,970,000.00 USD | 9,970,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.20` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.70` | 9,960,000.00 USD | 9,960,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.20` | 9,940,000.00 USD | 9,940,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 21,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.70` | 9,880,000.00 USD | 9,880,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.20` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 19,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.70` | 9,830,000.00 USD | 9,830,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.20` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 18,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.70` | 9,780,000.00 USD | 9,780,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.20` | 9,770,000.00 USD | 9,770,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.70` | 9,740,000.00 USD | 9,740,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.20` | 9,720,000.00 USD | 9,720,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.70` | 9,680,000.00 USD | 9,680,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 9,660,000.00 USD | 9,660,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 12,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.70` | 9,630,000.00 USD | 9,630,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.20` | 9,610,000.00 USD | 9,610,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 12,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.70` | 9,600,000.00 USD | 9,600,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 9,500,000.00 USD | 9,500,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 12,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.70` | 9,430,000.00 USD | 9,430,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.20` | 9,330,000.00 USD | 9,330,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 10,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.70` | 9,210,000.00 USD | 9,210,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.90` | 4,620,000.00 USD | 4,620,000.00 USD | 12,620.00 USD | 26,890.00 USD | 15,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 9,080,000.00 USD | 9,080,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.30` | 4,570,000.00 USD | 4,570,000.00 USD | 32,620.00 USD | 36,610.00 USD | 22,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 9,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.70` | 4,480,000.00 USD | 4,480,000.00 USD | 31,940.00 USD | 62,050.00 USD | 18,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.70` | 8,960,000.00 USD | 8,960,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.10` | 4,370,000.00 USD | 4,370,000.00 USD | 27,230.00 USD | 12,040.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.20` | 8,770,000.00 USD | 8,770,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.50` | 4,310,000.00 USD | 4,310,000.00 USD | 12,550.00 USD | 4,910.00 USD | 6,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,170.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.70` | 8,650,000.00 USD | 8,650,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.90` | 4,290,000.00 USD | 4,290,000.00 USD | 6,910.00 USD | 6,870.00 USD | 2,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 8,540,000.00 USD | 8,540,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.30` | 4,270,000.00 USD | 4,270,000.00 USD | 8,350.00 USD | 5,400.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.70` | 4,240,000.00 USD | 4,240,000.00 USD | 17,280.00 USD | 17,660.00 USD | 12,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 8,480,000.00 USD | 8,480,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.10` | 4,190,000.00 USD | 4,190,000.00 USD | 1,590.00 USD | 4,460.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.20` | 8,360,000.00 USD | 8,360,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.50` | 4,180,000.00 USD | 4,180,000.00 USD | 8,310.00 USD | 10,660.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `254.70` | 8,260,000.00 USD | 8,260,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.90` | 4,160,000.00 USD | 4,160,000.00 USD | 9,050.00 USD | 8,770.00 USD | 17.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 8,080,000.00 USD | 8,080,000.00 USD | 32,100.00 USD | 13,260.00 USD | 25,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.30` | 4,150,000.00 USD | 4,150,000.00 USD | 8,970.00 USD | 7,060.00 USD | 22,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.70` | 4,110,000.00 USD | 4,110,000.00 USD | 14,340.00 USD | 20,270.00 USD | 11,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 8,010,000.00 USD | 8,010,000.00 USD | 33,430.00 USD | 16,550.00 USD | 35,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.10` | 4,060,000.00 USD | 4,060,000.00 USD | 6,390.00 USD | 17,760.00 USD | 13,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.20` | 7,930,000.00 USD | 7,930,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.50` | 4,020,000.00 USD | 4,020,000.00 USD | 7,420.00 USD | 16,700.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 4,490.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `256.70` | 7,780,000.00 USD | 7,780,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.90` | 3,990,000.00 USD | 3,990,000.00 USD | 6,970.00 USD | 1,620.00 USD | 5,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 7,680,000.00 USD | 7,680,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.30` | 3,980,000.00 USD | 3,980,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 467.62 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.70` | 3,960,000.00 USD | 3,960,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.70` | 7,640,000.00 USD | 7,640,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.10` | 3,950,000.00 USD | 3,950,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.20` | 7,570,000.00 USD | 7,570,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.50` | 3,880,000.00 USD | 3,880,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `258.70` | 7,370,000.00 USD | 7,370,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.90` | 3,820,000.00 USD | 3,820,000.00 USD | 6,660.00 USD | 38,650.00 USD | 31,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 7,200,000.00 USD | 7,200,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.30` | 3,750,000.00 USD | 3,750,000.00 USD | 15,070.00 USD | 5,740.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.70` | 3,710,000.00 USD | 3,710,000.00 USD | 19,030.00 USD | 34,280.00 USD | 39,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 7,110,000.00 USD | 7,110,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.10` | 3,610,000.00 USD | 3,610,000.00 USD | 39,480.00 USD | 8,550.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.20` | 6,960,000.00 USD | 6,960,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.50` | 3,560,000.00 USD | 3,560,000.00 USD | 19,180.00 USD | 1,100.00 USD | 27,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `260.70` | 6,740,000.00 USD | 6,740,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.90` | 3,510,000.00 USD | 3,510,000.00 USD | 9,160.00 USD | 50,690.00 USD | 13,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 6,610,000.00 USD | 6,610,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.30` | 3,440,000.00 USD | 3,440,000.00 USD | 8,130.00 USD | 29,290.00 USD | 33,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.70` | 3,370,000.00 USD | 3,370,000.00 USD | 15,200.00 USD | 60,480.00 USD | 51,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 6,490,000.00 USD | 6,490,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.10` | 3,240,000.00 USD | 3,240,000.00 USD | 13,620.00 USD | 27,330.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.20` | 6,320,000.00 USD | 6,320,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.50` | 3,180,000.00 USD | 3,180,000.00 USD | 20,850.00 USD | 4,730.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.70` | 6,120,000.00 USD | 6,120,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.90` | 3,140,000.00 USD | 3,140,000.00 USD | 366.04 USD | 12,480.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 5,940,000.00 USD | 5,940,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.30` | 3,110,000.00 USD | 3,110,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.70` | 3,030,000.00 USD | 3,030,000.00 USD | 41,850.00 USD | 29,870.00 USD | 41,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 5,880,000.00 USD | 5,880,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.10` | 2,920,000.00 USD | 2,920,000.00 USD | 46,180.00 USD | 15,290.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.20` | 5,480,000.00 USD | 5,480,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.50` | 2,840,000.00 USD | 2,840,000.00 USD | 1,020.00 USD | 19,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.70` | 5,310,000.00 USD | 5,310,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.90` | 2,820,000.00 USD | 2,820,000.00 USD | 33,130.00 USD | 1,190.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 5,250,000.00 USD | 5,250,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.30` | 2,730,000.00 USD | 2,730,000.00 USD | 64,510.00 USD | 1,030.00 USD | 3.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.70` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 228.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.70` | 5,110,000.00 USD | 5,110,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.10` | 2,670,000.00 USD | 2,670,000.00 USD | 16,000.00 USD | 13,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.20` | 4,910,000.00 USD | 4,910,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.50` | 2,640,000.00 USD | 2,640,000.00 USD | 18,860.00 USD | 8,190.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 4,730,000.00 USD | 4,730,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.90` | 2,610,000.00 USD | 2,610,000.00 USD | 31,870.00 USD | 22,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 4,530,000.00 USD | 4,530,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.30` | 2,550,000.00 USD | 2,550,000.00 USD | 33,120.00 USD | 68,390.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.70` | 2,440,000.00 USD | 2,440,000.00 USD | 4,660.00 USD | 36,050.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.70` | 4,350,000.00 USD | 4,350,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.10` | 2,380,000.00 USD | 2,380,000.00 USD | 4,570.00 USD | 24,460.00 USD | 63,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.20` | 4,020,000.00 USD | 4,020,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.50` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 10,610.00 USD | 6.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.70` | 3,690,000.00 USD | 3,690,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.90` | 2,280,000.00 USD | 2,280,000.00 USD | 8,400.00 USD | 321.80 USD | 20.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 3,620,000.00 USD | 3,620,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.30` | 2,270,000.00 USD | 2,270,000.00 USD | 178.30 USD | 703.50 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.70` | 2,270,000.00 USD | 2,270,000.00 USD | 378.60 USD | 16,420.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.10` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.20` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.50` | 2,240,000.00 USD | 2,240,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.90` | 2,230,000.00 USD | 2,230,000.00 USD | 323.80 USD | 7,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.30` | 2,220,000.00 USD | 2,220,000.00 USD | 12,710.00 USD | 0.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.70` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 25,790.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.70` | 3,600,000.00 USD | 3,600,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.10` | 2,170,000.00 USD | 2,170,000.00 USD | 15,100.00 USD | 15,900.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.20` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.50` | 2,120,000.00 USD | 2,120,000.00 USD | 6,060.00 USD | 16,330.00 USD | 28,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 3,460,000.00 USD | 3,460,000.00 USD | 25,660.00 USD | 17,630.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.90` | 2,070,000.00 USD | 2,070,000.00 USD | 55,090.00 USD | 5,420.00 USD | 64,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.30` | 1,950,000.00 USD | 1,950,000.00 USD | 9,330.00 USD | 98,660.00 USD | 10,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.70` | 1,830,000.00 USD | 1,830,000.00 USD | 37,900.00 USD | 48,910.00 USD | 49,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 3,080,000.00 USD | 3,080,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.10` | 1,690,000.00 USD | 1,690,000.00 USD | 161,460.00 USD | 21,230.00 USD | 6.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.20` | 2,950,000.00 USD | 2,950,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.50` | 1,510,000.00 USD | 1,510,000.00 USD | 235,460.00 USD | 0.00 USD | 54,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.70` | 2,440,000.00 USD | 2,440,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.90` | 1,220,000.00 USD | 1,220,000.00 USD | 64,430.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 1,820,000.00 USD | 1,820,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.30` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.70` | 1,130,000.00 USD | 1,130,000.00 USD | 20,900.00 USD | 10,450.00 USD | 53,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 1,660,000.00 USD | 1,660,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.10` | 1,040,000.00 USD | 1,040,000.00 USD | 83,200.00 USD | 0.00 USD | 7,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.20` | 1,570,000.00 USD | 1,570,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.50` | 952,770.00 USD | 952,770.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.70` | 1,400,000.00 USD | 1,400,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.90` | 937,580.00 USD | 937,580.00 USD | 37,290.00 USD | 13,540.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 1,290,000.00 USD | 1,290,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.30` | 881,260.00 USD | 881,260.00 USD | 301.20 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.70` | 870,360.00 USD | 870,360.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 1,140,000.00 USD | 1,140,000.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.10` | 850,050.00 USD | 850,050.00 USD | 12,120.00 USD | 53,570.00 USD | 56,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.20` | 744,130.00 USD | 744,130.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.50` | 728,150.00 USD | 728,150.00 USD | 70,120.00 USD | 56,870.00 USD | 66,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 586,850.00 USD | 586,850.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.90` | 534,260.00 USD | 534,260.00 USD | 11,140.00 USD | 63,940.00 USD | 12,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 534,610.00 USD | 534,610.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.70` | 446,510.00 USD | 446,510.00 USD | 14,720.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 531,950.00 USD | 531,950.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.10` | 431,790.00 USD | 431,790.00 USD | 0.00 USD | 26,770.00 USD | 59,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.20` | 530,180.00 USD | 530,180.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.50` | 345,180.00 USD | 345,180.00 USD | 34,230.00 USD | 53,570.00 USD | 68,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.70` | 512,820.00 USD | 512,820.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.90` | 188,830.00 USD | 188,830.00 USD | 8,730.00 USD | 18,530.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 497,280.00 USD | 497,280.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.30` | 161,560.00 USD | 161,560.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.70` | 141,880.00 USD | 141,880.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 399,870.00 USD | 399,870.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.10` | 136,470.00 USD | 136,470.00 USD | 10,310.00 USD | 15,980.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.20` | 202,450.00 USD | 202,450.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.50` | 106,030.00 USD | 106,030.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.90` | 93,290.00 USD | 93,290.00 USD | 14,930.00 USD | 52,180.00 USD | 35.51 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 178,230.00 USD | 178,230.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.30` | 26,140.00 USD | 26,140.00 USD | 1,280.00 USD | 20,630.00 USD | 31.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 76,590.00 USD | 76,590.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.10` | 4,200.00 USD | 4,200.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.20` | 74,590.00 USD | 74,590.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `284.50` | 397.40 USD | 397.40 USD | 0.00 USD | 397.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.70` | 356,580.00 USD | 356,580.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.70` | 713,150.00 USD | 713,150.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.90` | 9,420.00 USD | 9,420.00 USD | 8,460.00 USD | 948.40 USD | 9.04 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.20` | 1,130,000.00 USD | 1,130,000.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.30` | 279,540.00 USD | 279,540.00 USD | 86,260.00 USD | 103,120.00 USD | 80,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.70` | 423,900.00 USD | 423,900.00 USD | 93,130.00 USD | 51,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.70` | 1,310,000.00 USD | 1,310,000.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.10` | 459,770.00 USD | 459,770.00 USD | 11,950.00 USD | 719.80 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.20` | 1,390,000.00 USD | 1,390,000.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.50` | 495,110.00 USD | 495,110.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.70` | 1,570,000.00 USD | 1,570,000.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.90` | 614,310.00 USD | 614,310.00 USD | 32,920.00 USD | 5,570.00 USD | 80,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 1,840,000.00 USD | 1,840,000.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.30` | 718,560.00 USD | 718,560.00 USD | 19,920.00 USD | 50,650.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.70` | 802,990.00 USD | 802,990.00 USD | 17,310.00 USD | 17,270.00 USD | 49,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.70` | 2,060,000.00 USD | 2,060,000.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.10` | 863,820.00 USD | 863,820.00 USD | 21,420.00 USD | 14,780.00 USD | 24,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.20` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.50` | 958,740.00 USD | 958,740.00 USD | 52,260.00 USD | 22,180.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.70` | 2,410,000.00 USD | 2,410,000.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.90` | 987,120.00 USD | 987,120.00 USD | 18,130.00 USD | 10,240.00 USD | 17.54 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 2,470,000.00 USD | 2,470,000.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.30` | 1,070,000.00 USD | 1,070,000.00 USD | 12,780.00 USD | 15,140.00 USD | 51,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.70` | 1,230,000.00 USD | 1,230,000.00 USD | 52,150.00 USD | 44,920.00 USD | 61,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 99,990.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.10` | 1,390,000.00 USD | 1,390,000.00 USD | 43,080.00 USD | 39,910.00 USD | 84,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.20` | 2,790,000.00 USD | 2,790,000.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.50` | 1,530,000.00 USD | 1,530,000.00 USD | 4,230.00 USD | 82,770.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.70` | 2,790,000.00 USD | 2,790,000.00 USD | 898.13 USD | 861.99 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.90` | 1,580,000.00 USD | 1,580,000.00 USD | 34,600.00 USD | 17,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 2,820,000.00 USD | 2,820,000.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.30` | 1,600,000.00 USD | 1,600,000.00 USD | 8,960.00 USD | 11,300.00 USD | 2.42 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.70` | 1,660,000.00 USD | 1,660,000.00 USD | 2,040.00 USD | 38,580.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 2,960,000.00 USD | 2,960,000.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.10` | 1,710,000.00 USD | 1,710,000.00 USD | 854.05 USD | 37,580.00 USD | 11,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.20` | 3,090,000.00 USD | 3,090,000.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.50` | 1,740,000.00 USD | 1,740,000.00 USD | 22,320.00 USD | 994.05 USD | 2,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 3,190,000.00 USD | 3,190,000.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.90` | 1,800,000.00 USD | 1,800,000.00 USD | 32,260.00 USD | 23,980.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 3,340,000.00 USD | 3,340,000.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.30` | 1,860,000.00 USD | 1,860,000.00 USD | 10,900.00 USD | 23,080.00 USD | 27,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.70` | 2,040,000.00 USD | 2,040,000.00 USD | 76,770.00 USD | 41,410.00 USD | 60,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 3,380,000.00 USD | 3,380,000.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.10` | 2,130,000.00 USD | 2,130,000.00 USD | 21,360.00 USD | 21,910.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.20` | 3,720,000.00 USD | 3,720,000.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.50` | 2,360,000.00 USD | 2,360,000.00 USD | 83,190.00 USD | 69,460.00 USD | 85,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 3,980,000.00 USD | 3,980,000.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.90` | 2,440,000.00 USD | 2,440,000.00 USD | 31,140.00 USD | 86.80 USD | 48,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 4,320,000.00 USD | 4,320,000.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.30` | 2,590,000.00 USD | 2,590,000.00 USD | 15,420.00 USD | 49,460.00 USD | 83,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.70` | 2,810,000.00 USD | 2,810,000.00 USD | 94,310.00 USD | 6,630.00 USD | 121,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 4,850,000.00 USD | 4,850,000.00 USD | 176,660.00 USD | 91,790.00 USD | 264,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.10` | 2,990,000.00 USD | 2,990,000.00 USD | 44,070.00 USD | 103,850.00 USD | 33,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.20` | 5,160,000.00 USD | 5,160,000.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.50` | 3,060,000.00 USD | 3,060,000.00 USD | 30,870.00 USD | 11,780.00 USD | 20,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `296.70` | 5,520,000.00 USD | 5,520,000.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.90` | 3,180,000.00 USD | 3,180,000.00 USD | 21,800.00 USD | 21,450.00 USD | 78,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,690,000.00 USD | 5,690,000.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.30` | 3,270,000.00 USD | 3,270,000.00 USD | 61,250.00 USD | 805.28 USD | 31,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.70` | 3,310,000.00 USD | 3,310,000.00 USD | 15,870.00 USD | 10,830.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 5,790,000.00 USD | 5,790,000.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.10` | 3,410,000.00 USD | 3,410,000.00 USD | 51,630.00 USD | 8,080.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.20` | 6,040,000.00 USD | 6,040,000.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.50` | 3,480,000.00 USD | 3,480,000.00 USD | 5,160.00 USD | 929.37 USD | 56,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `298.50` | 442.08 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `298.70` | 6,160,000.00 USD | 6,160,000.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.90` | 3,600,000.00 USD | 3,600,000.00 USD | 28,150.00 USD | 5,530.00 USD | 94,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 6,260,000.00 USD | 6,260,000.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.30` | 3,660,000.00 USD | 3,660,000.00 USD | 33,970.00 USD | 10,510.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.70` | 3,710,000.00 USD | 3,710,000.00 USD | 8,070.00 USD | 10,660.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 6,310,000.00 USD | 6,310,000.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.10` | 3,830,000.00 USD | 3,830,000.00 USD | 19,640.00 USD | 36,540.00 USD | 64,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.20` | 6,360,000.00 USD | 6,360,000.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.50` | 3,870,000.00 USD | 3,870,000.00 USD | 23,000.00 USD | 1,410.00 USD | 17,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 14,550.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `300.70` | 6,480,000.00 USD | 6,480,000.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.90` | 3,900,000.00 USD | 3,900,000.00 USD | 269.05 USD | 866.42 USD | 29,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 6,690,000.00 USD | 6,690,000.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.30` | 3,940,000.00 USD | 3,940,000.00 USD | 597.00 USD | 15,110.00 USD | 20,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.70` | 3,980,000.00 USD | 3,980,000.00 USD | 19,840.00 USD | 8,210.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.70` | 6,960,000.00 USD | 6,960,000.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.10` | 4,050,000.00 USD | 4,050,000.00 USD | 25,190.00 USD | 30,470.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.20` | 7,190,000.00 USD | 7,190,000.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.50` | 4,110,000.00 USD | 4,110,000.00 USD | 13,820.00 USD | 12,980.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 7,400,000.00 USD | 7,400,000.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.90` | 4,130,000.00 USD | 4,130,000.00 USD | 1,180.00 USD | 1,560.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.30` | 4,160,000.00 USD | 4,160,000.00 USD | 20,650.00 USD | 2,520.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.70` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 302.70 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 7,490,000.00 USD | 7,490,000.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.10` | 4,220,000.00 USD | 4,220,000.00 USD | 21,920.00 USD | 1,930.00 USD | 40,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.20` | 7,530,000.00 USD | 7,530,000.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.50` | 4,280,000.00 USD | 4,280,000.00 USD | 9,530.00 USD | 2,100.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 7,550,000.00 USD | 7,550,000.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.90` | 4,300,000.00 USD | 4,300,000.00 USD | 9,920.00 USD | 8,480.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 7,910,000.00 USD | 7,910,000.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.30` | 4,310,000.00 USD | 4,310,000.00 USD | 1,930.00 USD | 172.52 USD | 2,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.70` | 4,330,000.00 USD | 4,330,000.00 USD | 10,640.00 USD | 4,710.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 8,120,000.00 USD | 8,120,000.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.10` | 4,340,000.00 USD | 4,340,000.00 USD | 7,390.00 USD | 2,900.00 USD | 6,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.20` | 8,290,000.00 USD | 8,290,000.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.50` | 4,350,000.00 USD | 4,350,000.00 USD | 4,290.00 USD | 40.30 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 8,450,000.00 USD | 8,450,000.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.90` | 4,440,000.00 USD | 4,440,000.00 USD | 31,880.00 USD | 43,430.00 USD | 13,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 8,760,000.00 USD | 8,760,000.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.30` | 4,530,000.00 USD | 4,530,000.00 USD | 7,900.00 USD | 48,680.00 USD | 25,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.70` | 4,590,000.00 USD | 4,590,000.00 USD | 28,880.00 USD | 30,430.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 9,030,000.00 USD | 9,030,000.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.10` | 4,640,000.00 USD | 4,640,000.00 USD | 25,640.00 USD | 11,300.00 USD | 16,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.20` | 9,460,000.00 USD | 9,460,000.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.50` | 4,660,000.00 USD | 4,660,000.00 USD | 4,640.00 USD | 3,470.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 9,600,000.00 USD | 9,600,000.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.90` | 4,670,000.00 USD | 4,670,000.00 USD | 9,380.00 USD | 5,860.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 9,730,000.00 USD | 9,730,000.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.30` | 4,680,000.00 USD | 4,680,000.00 USD | 4,590.00 USD | 436.11 USD | 2,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.70` | 4,700,000.00 USD | 4,700,000.00 USD | 8,420.00 USD | 5,400.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 10,070,000.00 USD | 10,070,000.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.10` | 4,720,000.00 USD | 4,720,000.00 USD | 8,290.00 USD | 6,510.00 USD | 11,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.20` | 10,230,000.00 USD | 10,230,000.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.50` | 4,730,000.00 USD | 4,730,000.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.70` | 10,460,000.00 USD | 10,460,000.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.90` | 4,740,000.00 USD | 4,740,000.00 USD | 5,080.00 USD | 0.00 USD | 2.31 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,660,000.00 USD | 10,660,000.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.30` | 4,740,000.00 USD | 4,740,000.00 USD | 257.90 USD | 160.90 USD | 6.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.70` | 4,750,000.00 USD | 4,750,000.00 USD | 7,100.00 USD | 6,700.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 10,760,000.00 USD | 10,760,000.00 USD | 65,050.00 USD | 11,240.00 USD | 25,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.10` | 4,770,000.00 USD | 4,770,000.00 USD | 244.00 USD | 4,180.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.20` | 10,830,000.00 USD | 10,830,000.00 USD | 43,780.00 USD | 11,410.00 USD | 14,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.50` | 4,800,000.00 USD | 4,800,000.00 USD | 14,340.00 USD | 5,500.00 USD | 11,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 10,890,000.00 USD | 10,890,000.00 USD | 8,290.00 USD | 19,350.00 USD | 29,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.90` | 4,810,000.00 USD | 4,810,000.00 USD | 5,500.00 USD | 23.27 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 11,030,000.00 USD | 11,030,000.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.30` | 4,830,000.00 USD | 4,830,000.00 USD | 3,580.00 USD | 11,520.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.70` | 4,830,000.00 USD | 4,830,000.00 USD | 3,580.00 USD | 239.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 11,100,000.00 USD | 11,100,000.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.20` | 11,160,000.00 USD | 11,160,000.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.50` | 4,850,000.00 USD | 4,850,000.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 11,210,000.00 USD | 11,210,000.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.90` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 3,660.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 11,240,000.00 USD | 11,240,000.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.30` | 4,860,000.00 USD | 4,860,000.00 USD | 2,020.00 USD | 1,550.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.70` | 4,870,000.00 USD | 4,870,000.00 USD | 1,850.00 USD | 0.00 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 11,320,000.00 USD | 11,320,000.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.10` | 4,880,000.00 USD | 4,880,000.00 USD | 2,100.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.20` | 11,420,000.00 USD | 11,420,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.50` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.60` | 4,890,000.00 USD | 4,890,000.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 11,480,000.00 USD | 11,480,000.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 11,500,000.00 USD | 11,500,000.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 11,500,000.00 USD | 11,500,000.00 USD | 620.15 USD | 721.55 USD | 67.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.20` | 11,570,000.00 USD | 11,570,000.00 USD | 23,930.00 USD | 13,700.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.70` | 11,660,000.00 USD | 11,660,000.00 USD | 11,230.00 USD | 44,600.00 USD | 37,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.20` | 11,680,000.00 USD | 11,680,000.00 USD | 366.90 USD | 18,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 11,690,000.00 USD | 11,690,000.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.20` | 11,790,000.00 USD | 11,790,000.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD | `Tier 1 CEX` |
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
| `7D` | `234.70` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD |
| `7D` | `235.20` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD |
| `7D` | `235.70` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD |
| `7D` | `236.20` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD |
| `7D` | `236.70` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD |
| `7D` | `237.20` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD |
| `7D` | `237.70` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `238.20` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD |
| `7D` | `238.70` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD |
| `7D` | `239.20` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.70` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.70` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `241.20` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.70` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.20` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD |
| `7D` | `242.70` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `243.20` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD |
| `7D` | `243.70` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `244.20` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.70` | 9,780,000.00 USD | 0.00 USD | 9,780,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD |
| `7D` | `245.20` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD |
| `7D` | `245.70` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD |
| `7D` | `246.20` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD |
| `7D` | `246.70` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD |
| `7D` | `247.20` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD |
| `7D` | `247.70` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD |
| `7D` | `248.20` | 9,610,000.00 USD | 0.00 USD | 9,610,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD |
| `7D` | `248.70` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD |
| `7D` | `249.20` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD |
| `7D` | `249.70` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD |
| `7D` | `250.20` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD |
| `7D` | `250.70` | 9,210,000.00 USD | 0.00 USD | 9,210,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD |
| `1D` | `250.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 12,620.00 USD | 26,890.00 USD | 15,900.00 USD |
| `7D` | `251.20` | 9,080,000.00 USD | 0.00 USD | 9,080,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD |
| `1D` | `251.30` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 32,620.00 USD | 36,610.00 USD | 22,750.00 USD |
| `1D` | `251.70` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 31,940.00 USD | 62,050.00 USD | 18,150.00 USD |
| `7D` | `251.70` | 8,960,000.00 USD | 0.00 USD | 8,960,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD |
| `1D` | `252.10` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 27,230.00 USD | 12,040.00 USD | 16,430.00 USD |
| `7D` | `252.20` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD |
| `1D` | `252.50` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 12,550.00 USD | 4,910.00 USD | 6,490.00 USD |
| `7D` | `252.70` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD |
| `1D` | `252.90` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 6,910.00 USD | 6,870.00 USD | 2,830.00 USD |
| `7D` | `253.20` | 8,540,000.00 USD | 0.00 USD | 8,540,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD |
| `1D` | `253.30` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 8,350.00 USD | 5,400.00 USD | 14,780.00 USD |
| `1D` | `253.70` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 17,280.00 USD | 17,660.00 USD | 12,010.00 USD |
| `7D` | `253.70` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD |
| `1D` | `254.10` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 1,590.00 USD | 4,460.00 USD | 3,940.00 USD |
| `7D` | `254.20` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD |
| `1D` | `254.50` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 8,310.00 USD | 10,660.00 USD | 2.31 USD |
| `7D` | `254.70` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD |
| `1D` | `254.90` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 9,050.00 USD | 8,770.00 USD | 17.15 USD |
| `7D` | `255.20` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 32,100.00 USD | 13,260.00 USD | 25,480.00 USD |
| `1D` | `255.30` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 8,970.00 USD | 7,060.00 USD | 22,440.00 USD |
| `1D` | `255.70` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 14,340.00 USD | 20,270.00 USD | 11,800.00 USD |
| `7D` | `255.70` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 33,430.00 USD | 16,550.00 USD | 35,380.00 USD |
| `1D` | `256.10` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 6,390.00 USD | 17,760.00 USD | 13,780.00 USD |
| `7D` | `256.20` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD |
| `1D` | `256.50` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 7,420.00 USD | 16,700.00 USD | 5,680.00 USD |
| `7D` | `256.70` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD |
| `1D` | `256.90` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 6,970.00 USD | 1,620.00 USD | 5,430.00 USD |
| `7D` | `257.20` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD |
| `1D` | `257.30` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD |
| `1D` | `257.70` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD |
| `7D` | `257.70` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD |
| `7D` | `258.20` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD |
| `1D` | `258.50` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.70` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD |
| `1D` | `258.90` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 6,660.00 USD | 38,650.00 USD | 31,030.00 USD |
| `7D` | `259.20` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD |
| `1D` | `259.30` | 3,750,000.00 USD | 0.00 USD | 3,750,000.00 USD | 15,070.00 USD | 5,740.00 USD | 17,630.00 USD |
| `1D` | `259.70` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 19,030.00 USD | 34,280.00 USD | 39,300.00 USD |
| `7D` | `259.70` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD |
| `1D` | `260.10` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 39,480.00 USD | 8,550.00 USD | 6,870.00 USD |
| `7D` | `260.20` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD |
| `1D` | `260.50` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 19,180.00 USD | 1,100.00 USD | 27,210.00 USD |
| `7D` | `260.70` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD |
| `1D` | `260.90` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 9,160.00 USD | 50,690.00 USD | 13,930.00 USD |
| `7D` | `261.20` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD |
| `1D` | `261.30` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 8,130.00 USD | 29,290.00 USD | 33,410.00 USD |
| `1D` | `261.70` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 15,200.00 USD | 60,480.00 USD | 51,230.00 USD |
| `7D` | `261.70` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD |
| `1D` | `262.10` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 13,620.00 USD | 27,330.00 USD | 21,370.00 USD |
| `7D` | `262.20` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD |
| `1D` | `262.50` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 20,850.00 USD | 4,730.00 USD | 10,850.00 USD |
| `7D` | `262.70` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD |
| `1D` | `262.90` | 3,140,000.00 USD | 0.00 USD | 3,140,000.00 USD | 366.04 USD | 12,480.00 USD | 19,480.00 USD |
| `7D` | `263.20` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD |
| `1D` | `263.30` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,440.00 USD |
| `1D` | `263.70` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 41,850.00 USD | 29,870.00 USD | 41,330.00 USD |
| `7D` | `263.70` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD |
| `1D` | `264.10` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 46,180.00 USD | 15,290.00 USD | 17,150.00 USD |
| `7D` | `264.20` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD |
| `1D` | `264.50` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 1,020.00 USD | 19,610.00 USD | 0.00 USD |
| `7D` | `264.70` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD |
| `1D` | `264.90` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 33,130.00 USD | 1,190.00 USD | 53,200.00 USD |
| `7D` | `265.20` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD |
| `1D` | `265.30` | 2,730,000.00 USD | 0.00 USD | 2,730,000.00 USD | 64,510.00 USD | 1,030.00 USD | 3.40 USD |
| `1D` | `265.70` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 0.00 USD | 228.00 USD | 0.00 USD |
| `7D` | `265.70` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD |
| `1D` | `266.10` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 16,000.00 USD | 13,250.00 USD | 0.00 USD |
| `7D` | `266.20` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD |
| `1D` | `266.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 18,860.00 USD | 8,190.00 USD | 4,800.00 USD |
| `7D` | `266.70` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD |
| `1D` | `266.90` | 2,610,000.00 USD | 0.00 USD | 2,610,000.00 USD | 31,870.00 USD | 22,170.00 USD | 0.00 USD |
| `7D` | `267.20` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD |
| `1D` | `267.30` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 33,120.00 USD | 68,390.00 USD | 12,550.00 USD |
| `1D` | `267.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 4,660.00 USD | 36,050.00 USD | 14,900.00 USD |
| `7D` | `267.70` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD |
| `1D` | `268.10` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 4,570.00 USD | 24,460.00 USD | 63,570.00 USD |
| `7D` | `268.20` | 4,020,000.00 USD | 0.00 USD | 4,020,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD |
| `1D` | `268.50` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 0.00 USD | 10,610.00 USD | 6.84 USD |
| `7D` | `268.70` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD |
| `1D` | `268.90` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 8,400.00 USD | 321.80 USD | 20.82 USD |
| `7D` | `269.20` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD |
| `1D` | `269.30` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 178.30 USD | 703.50 USD | 0.00 USD |
| `1D` | `269.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 378.60 USD | 16,420.00 USD | 13,580.00 USD |
| `7D` | `269.70` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD |
| `1D` | `270.10` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 793.00 USD | 3,540.00 USD |
| `7D` | `270.20` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD |
| `1D` | `270.50` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 9,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `270.70` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD |
| `1D` | `270.90` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 323.80 USD | 7,970.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 12,710.00 USD | 0.00 USD | 2,750.00 USD |
| `1D` | `271.70` | 2,200,000.00 USD | 0.00 USD | 2,200,000.00 USD | 0.00 USD | 25,790.00 USD | 5,300.00 USD |
| `7D` | `271.70` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD |
| `1D` | `272.10` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 15,100.00 USD | 15,900.00 USD | 19,770.00 USD |
| `7D` | `272.20` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 6,060.00 USD | 16,330.00 USD | 28,120.00 USD |
| `7D` | `272.70` | 3,460,000.00 USD | 0.00 USD | 3,460,000.00 USD | 25,660.00 USD | 17,630.00 USD | 47,720.00 USD |
| `1D` | `272.90` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 55,090.00 USD | 5,420.00 USD | 64,890.00 USD |
| `7D` | `273.20` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD |
| `1D` | `273.30` | 1,950,000.00 USD | 0.00 USD | 1,950,000.00 USD | 9,330.00 USD | 98,660.00 USD | 10,240.00 USD |
| `1D` | `273.70` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 37,900.00 USD | 48,910.00 USD | 49,200.00 USD |
| `7D` | `273.70` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD |
| `1D` | `274.10` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 161,460.00 USD | 21,230.00 USD | 6.00 USD |
| `7D` | `274.20` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.50` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 235,460.00 USD | 0.00 USD | 54,030.00 USD |
| `7D` | `274.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD |
| `1D` | `274.90` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 64,430.00 USD | 19,960.00 USD | 0.00 USD |
| `7D` | `275.20` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.30` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD |
| `1D` | `275.70` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 20,900.00 USD | 10,450.00 USD | 53,200.00 USD |
| `7D` | `275.70` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD |
| `1D` | `276.10` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 83,200.00 USD | 0.00 USD | 7,090.00 USD |
| `7D` | `276.20` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD |
| `1D` | `276.50` | 952,770.00 USD | 0.00 USD | 952,770.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD |
| `7D` | `276.70` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.90` | 937,580.00 USD | 0.00 USD | 937,580.00 USD | 37,290.00 USD | 13,540.00 USD | 5,500.00 USD |
| `7D` | `277.20` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD |
| `1D` | `277.30` | 881,260.00 USD | 0.00 USD | 881,260.00 USD | 301.20 USD | 0.00 USD | 10,600.00 USD |
| `1D` | `277.70` | 870,360.00 USD | 0.00 USD | 870,360.00 USD | 0.00 USD | 0.00 USD | 20,300.00 USD |
| `7D` | `277.70` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD |
| `1D` | `278.10` | 850,050.00 USD | 0.00 USD | 850,050.00 USD | 12,120.00 USD | 53,570.00 USD | 56,220.00 USD |
| `7D` | `278.20` | 744,130.00 USD | 0.00 USD | 744,130.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD |
| `1D` | `278.50` | 728,150.00 USD | 0.00 USD | 728,150.00 USD | 70,120.00 USD | 56,870.00 USD | 66,900.00 USD |
| `7D` | `278.70` | 586,850.00 USD | 0.00 USD | 586,850.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD |
| `1D` | `278.90` | 534,260.00 USD | 0.00 USD | 534,260.00 USD | 11,140.00 USD | 63,940.00 USD | 12,660.00 USD |
| `7D` | `279.20` | 534,610.00 USD | 0.00 USD | 534,610.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 446,510.00 USD | 0.00 USD | 446,510.00 USD | 14,720.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.70` | 531,950.00 USD | 0.00 USD | 531,950.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `280.10` | 431,790.00 USD | 0.00 USD | 431,790.00 USD | 0.00 USD | 26,770.00 USD | 59,840.00 USD |
| `7D` | `280.20` | 530,180.00 USD | 0.00 USD | 530,180.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD |
| `1D` | `280.50` | 345,180.00 USD | 0.00 USD | 345,180.00 USD | 34,230.00 USD | 53,570.00 USD | 68,550.00 USD |
| `7D` | `280.70` | 512,820.00 USD | 0.00 USD | 512,820.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `280.90` | 188,830.00 USD | 0.00 USD | 188,830.00 USD | 8,730.00 USD | 18,530.00 USD | 12.68 USD |
| `7D` | `281.20` | 497,280.00 USD | 0.00 USD | 497,280.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `1D` | `281.30` | 161,560.00 USD | 0.00 USD | 161,560.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD |
| `1D` | `281.70` | 141,880.00 USD | 0.00 USD | 141,880.00 USD | 0.00 USD | 5,410.00 USD | 0.00 USD |
| `7D` | `281.70` | 399,870.00 USD | 0.00 USD | 399,870.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 136,470.00 USD | 0.00 USD | 136,470.00 USD | 10,310.00 USD | 15,980.00 USD | 4,140.00 USD |
| `7D` | `282.20` | 202,450.00 USD | 0.00 USD | 202,450.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.50` | 106,030.00 USD | 0.00 USD | 106,030.00 USD | 0.00 USD | 12,740.00 USD | 0.00 USD |
| `1D` | `282.90` | 93,290.00 USD | 0.00 USD | 93,290.00 USD | 14,930.00 USD | 52,180.00 USD | 35.51 USD |
| `7D` | `283.20` | 178,230.00 USD | 0.00 USD | 178,230.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD |
| `1D` | `283.30` | 26,140.00 USD | 0.00 USD | 26,140.00 USD | 1,280.00 USD | 20,630.00 USD | 31.75 USD |
| `7D` | `283.70` | 76,590.00 USD | 0.00 USD | 76,590.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.10` | 4,200.00 USD | 0.00 USD | 4,200.00 USD | 3,780.00 USD | 0.00 USD | 26.15 USD |
| `7D` | `284.20` | 74,590.00 USD | 0.00 USD | 74,590.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD |
| `1D` | `284.50` | 397.40 USD | 0.00 USD | 397.40 USD | 0.00 USD | 397.40 USD | 0.00 USD |
| `7D` | `284.70` | 356,580.00 USD | 356,580.00 USD | 0.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD |
| `7D` | `284.70` | 713,150.00 USD | 713,150.00 USD | 0.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD |
| `1D` | `284.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.90` | 9,420.00 USD | 9,420.00 USD | 0.00 USD | 8,460.00 USD | 948.40 USD | 9.04 USD |
| `7D` | `285.20` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD |
| `1D` | `285.30` | 279,540.00 USD | 279,540.00 USD | 0.00 USD | 86,260.00 USD | 103,120.00 USD | 80,730.00 USD |
| `1D` | `285.70` | 423,900.00 USD | 423,900.00 USD | 0.00 USD | 93,130.00 USD | 51,230.00 USD | 0.00 USD |
| `7D` | `285.70` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD |
| `1D` | `286.10` | 459,770.00 USD | 459,770.00 USD | 0.00 USD | 11,950.00 USD | 719.80 USD | 23,210.00 USD |
| `7D` | `286.20` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD |
| `1D` | `286.50` | 495,110.00 USD | 495,110.00 USD | 0.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD |
| `7D` | `286.70` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD |
| `1D` | `286.90` | 614,310.00 USD | 614,310.00 USD | 0.00 USD | 32,920.00 USD | 5,570.00 USD | 80,710.00 USD |
| `7D` | `287.20` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD |
| `1D` | `287.30` | 718,560.00 USD | 718,560.00 USD | 0.00 USD | 19,920.00 USD | 50,650.00 USD | 33,670.00 USD |
| `1D` | `287.70` | 802,990.00 USD | 802,990.00 USD | 0.00 USD | 17,310.00 USD | 17,270.00 USD | 49,860.00 USD |
| `7D` | `287.70` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD |
| `1D` | `288.10` | 863,820.00 USD | 863,820.00 USD | 0.00 USD | 21,420.00 USD | 14,780.00 USD | 24,620.00 USD |
| `7D` | `288.20` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD |
| `1D` | `288.50` | 958,740.00 USD | 958,740.00 USD | 0.00 USD | 52,260.00 USD | 22,180.00 USD | 20,480.00 USD |
| `7D` | `288.70` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD |
| `1D` | `288.90` | 987,120.00 USD | 987,120.00 USD | 0.00 USD | 18,130.00 USD | 10,240.00 USD | 17.54 USD |
| `7D` | `289.20` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.30` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 12,780.00 USD | 15,140.00 USD | 51,210.00 USD |
| `1D` | `289.70` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 52,150.00 USD | 44,920.00 USD | 61,910.00 USD |
| `7D` | `289.70` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 99,990.00 USD | 134,010.00 USD |
| `1D` | `290.10` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 43,080.00 USD | 39,910.00 USD | 84,680.00 USD |
| `7D` | `290.20` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 4,230.00 USD | 82,770.00 USD | 46,650.00 USD |
| `7D` | `290.70` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 0.00 USD |
| `1D` | `290.90` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 34,600.00 USD | 17,870.00 USD | 0.00 USD |
| `7D` | `291.20` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD |
| `1D` | `291.30` | 1,600,000.00 USD | 1,600,000.00 USD | 0.00 USD | 8,960.00 USD | 11,300.00 USD | 2.42 USD |
| `1D` | `291.70` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 2,040.00 USD | 38,580.00 USD | 22,170.00 USD |
| `7D` | `291.70` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 854.05 USD | 37,580.00 USD | 11,510.00 USD |
| `7D` | `292.20` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD |
| `1D` | `292.50` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 22,320.00 USD | 994.05 USD | 2,240.00 USD |
| `7D` | `292.70` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD |
| `1D` | `292.90` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 32,260.00 USD | 23,980.00 USD | 3,560.00 USD |
| `7D` | `293.20` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD |
| `1D` | `293.30` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 10,900.00 USD | 23,080.00 USD | 27,370.00 USD |
| `1D` | `293.70` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 76,770.00 USD | 41,410.00 USD | 60,310.00 USD |
| `7D` | `293.70` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD |
| `1D` | `294.10` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 21,360.00 USD | 21,910.00 USD | 44,840.00 USD |
| `7D` | `294.20` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD |
| `1D` | `294.50` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 83,190.00 USD | 69,460.00 USD | 85,220.00 USD |
| `7D` | `294.70` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD |
| `1D` | `294.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 31,140.00 USD | 86.80 USD | 48,700.00 USD |
| `7D` | `295.20` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD |
| `1D` | `295.30` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 15,420.00 USD | 49,460.00 USD | 83,010.00 USD |
| `1D` | `295.70` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 94,310.00 USD | 6,630.00 USD | 121,700.00 USD |
| `7D` | `295.70` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 176,660.00 USD | 91,790.00 USD | 264,470.00 USD |
| `1D` | `296.10` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 44,070.00 USD | 103,850.00 USD | 33,000.00 USD |
| `7D` | `296.20` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD |
| `1D` | `296.50` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 30,870.00 USD | 11,780.00 USD | 20,610.00 USD |
| `7D` | `296.70` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD |
| `1D` | `296.90` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 21,800.00 USD | 21,450.00 USD | 78,160.00 USD |
| `7D` | `297.20` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD |
| `1D` | `297.30` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 61,250.00 USD | 805.28 USD | 31,480.00 USD |
| `1D` | `297.70` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 15,870.00 USD | 10,830.00 USD | 12,070.00 USD |
| `7D` | `297.70` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD |
| `1D` | `298.10` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 51,630.00 USD | 8,080.00 USD | 41,570.00 USD |
| `7D` | `298.20` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD |
| `1D` | `298.50` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 5,160.00 USD | 929.37 USD | 56,410.00 USD |
| `7D` | `298.70` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD |
| `1D` | `298.90` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 28,150.00 USD | 5,530.00 USD | 94,670.00 USD |
| `7D` | `299.20` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD |
| `1D` | `299.30` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 33,970.00 USD | 10,510.00 USD | 12,340.00 USD |
| `1D` | `299.70` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 8,070.00 USD | 10,660.00 USD | 27,680.00 USD |
| `7D` | `299.70` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD |
| `1D` | `300.10` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 19,640.00 USD | 36,540.00 USD | 64,300.00 USD |
| `7D` | `300.20` | 6,360,000.00 USD | 6,360,000.00 USD | 0.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD |
| `1D` | `300.50` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 23,000.00 USD | 1,410.00 USD | 17,180.00 USD |
| `7D` | `300.70` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD |
| `1D` | `300.90` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 269.05 USD | 866.42 USD | 29,440.00 USD |
| `7D` | `301.20` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD |
| `1D` | `301.30` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 597.00 USD | 15,110.00 USD | 20,870.00 USD |
| `1D` | `301.70` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 19,840.00 USD | 8,210.00 USD | 15,430.00 USD |
| `7D` | `301.70` | 6,960,000.00 USD | 6,960,000.00 USD | 0.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD |
| `1D` | `302.10` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 25,190.00 USD | 30,470.00 USD | 10,360.00 USD |
| `7D` | `302.20` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD |
| `1D` | `302.50` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 13,820.00 USD | 12,980.00 USD | 38,380.00 USD |
| `7D` | `302.70` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD |
| `1D` | `302.90` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 1,180.00 USD | 1,560.00 USD | 13,980.00 USD |
| `7D` | `303.20` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD |
| `1D` | `303.30` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 20,650.00 USD | 2,520.00 USD | 9,360.00 USD |
| `1D` | `303.70` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 302.70 USD | 1.44 USD |
| `7D` | `303.70` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD |
| `1D` | `304.10` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 21,920.00 USD | 1,930.00 USD | 40,420.00 USD |
| `7D` | `304.20` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD |
| `1D` | `304.50` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 9,530.00 USD | 2,100.00 USD | 44,520.00 USD |
| `7D` | `304.70` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD |
| `1D` | `304.90` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 9,920.00 USD | 8,480.00 USD | 2,030.00 USD |
| `7D` | `305.20` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD |
| `1D` | `305.30` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 1,930.00 USD | 172.52 USD | 2,010.00 USD |
| `1D` | `305.70` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 10,640.00 USD | 4,710.00 USD | 7,360.00 USD |
| `7D` | `305.70` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD |
| `1D` | `306.10` | 4,340,000.00 USD | 4,340,000.00 USD | 0.00 USD | 7,390.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.20` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD |
| `1D` | `306.50` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 4,290.00 USD | 40.30 USD | 5,670.00 USD |
| `7D` | `306.70` | 8,450,000.00 USD | 8,450,000.00 USD | 0.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD |
| `1D` | `306.90` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 31,880.00 USD | 43,430.00 USD | 13,060.00 USD |
| `7D` | `307.20` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD |
| `1D` | `307.30` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 7,900.00 USD | 48,680.00 USD | 25,510.00 USD |
| `1D` | `307.70` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 28,880.00 USD | 30,430.00 USD | 6,160.00 USD |
| `7D` | `307.70` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD |
| `1D` | `308.10` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 25,640.00 USD | 11,300.00 USD | 16,370.00 USD |
| `7D` | `308.20` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD |
| `1D` | `308.50` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 4,640.00 USD | 3,470.00 USD | 3,000.00 USD |
| `7D` | `308.70` | 9,600,000.00 USD | 9,600,000.00 USD | 0.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD |
| `1D` | `308.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 9,380.00 USD | 5,860.00 USD | 4,140.00 USD |
| `7D` | `309.20` | 9,730,000.00 USD | 9,730,000.00 USD | 0.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD |
| `1D` | `309.30` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 4,590.00 USD | 436.11 USD | 2,150.00 USD |
| `1D` | `309.70` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 8,420.00 USD | 5,400.00 USD | 3,030.00 USD |
| `7D` | `309.70` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD |
| `1D` | `310.10` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 8,290.00 USD | 6,510.00 USD | 11,020.00 USD |
| `7D` | `310.20` | 10,230,000.00 USD | 10,230,000.00 USD | 0.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD |
| `1D` | `310.50` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 112.30 USD | 2,320.00 USD | 3,930.00 USD |
| `7D` | `310.70` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD |
| `1D` | `310.90` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 2.31 USD |
| `7D` | `311.20` | 10,660,000.00 USD | 10,660,000.00 USD | 0.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD |
| `1D` | `311.30` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 257.90 USD | 160.90 USD | 6.94 USD |
| `1D` | `311.70` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 7,100.00 USD | 6,700.00 USD | 4,060.00 USD |
| `7D` | `311.70` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 65,050.00 USD | 11,240.00 USD | 25,590.00 USD |
| `1D` | `312.10` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 244.00 USD | 4,180.00 USD | 9,550.00 USD |
| `7D` | `312.20` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 14,140.00 USD |
| `1D` | `312.50` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 14,340.00 USD | 5,500.00 USD | 11,780.00 USD |
| `7D` | `312.70` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 8,290.00 USD | 19,350.00 USD | 29,640.00 USD |
| `1D` | `312.90` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 5,500.00 USD | 23.27 USD | 4,360.00 USD |
| `7D` | `313.20` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD |
| `1D` | `313.30` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 3,580.00 USD | 11,520.00 USD | 2,580.00 USD |
| `1D` | `313.70` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 3,580.00 USD | 239.05 USD | 0.00 USD |
| `7D` | `313.70` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD |
| `1D` | `314.10` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `7D` | `314.20` | 11,160,000.00 USD | 11,160,000.00 USD | 0.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD |
| `1D` | `314.50` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 4,240.00 USD | 68.55 USD | 8,330.00 USD |
| `7D` | `314.70` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `314.90` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 3,660.00 USD | 4,830.00 USD |
| `7D` | `315.20` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD |
| `1D` | `315.30` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 2,020.00 USD | 1,550.00 USD | 1,620.00 USD |
| `1D` | `315.70` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 1,850.00 USD | 0.00 USD | 5,230.00 USD |
| `7D` | `315.70` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD |
| `1D` | `316.10` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 2,100.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `316.20` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD |
| `1D` | `316.50` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 3,300.00 USD | 0.00 USD |
| `1D` | `316.60` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 11,070.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `316.70` | 11,480,000.00 USD | 11,480,000.00 USD | 0.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD |
| `7D` | `317.20` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD |
| `7D` | `317.70` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 620.15 USD | 721.55 USD | 67.28 USD |
| `7D` | `318.20` | 11,570,000.00 USD | 11,570,000.00 USD | 0.00 USD | 23,930.00 USD | 13,700.00 USD | 32,180.00 USD |
| `7D` | `318.70` | 11,660,000.00 USD | 11,660,000.00 USD | 0.00 USD | 11,230.00 USD | 44,600.00 USD | 37,810.00 USD |
| `7D` | `319.20` | 11,680,000.00 USD | 11,680,000.00 USD | 0.00 USD | 366.90 USD | 18,060.00 USD | 0.00 USD |
| `7D` | `319.70` | 11,690,000.00 USD | 11,690,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `7D` | `320.20` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.93M` | Total OI Tokens: `1,082,144.3 BCH`
  * 1h OI Change: `-0.06%` | 4h OI Change: `+5.78%` | 24h OI Change: `-1.36%`
  * Exchange Breakdown: Binance=`90.11M` | Bybit=`38.63M` | OKX=`24.01M` | Hyperliquid=`7.26M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.04K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0090%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0065%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `55.85%` | `44.15%` | `1.27` | 2,400,000.00 USD |
| `15M` | `Binance` | `44.1%` | `55.9%` | `0.79` | 651,730.00 USD |
| `15M` | `OKX` | `56.52%` | `43.48%` | `1.30` | 318,360.00 USD |
| `15M` | `Bybit` | `56.98%` | `43.02%` | `1.32` | 250,820.00 USD |
| `15M` | `KuCoin` | `49.2%` | `50.8%` | `0.97` | 31,520.00 USD |
| `15M` | `Gate` | `46.57%` | `53.43%` | `0.87` | 227,520.00 USD |
| `15M` | `Bitget` | `32.18%` | `67.82%` | `0.47` | 33,600.00 USD |
| `15M` | `BingX` | `49.66%` | `50.34%` | `0.99` | 441,630.00 USD |
| `15M` | `MEXC` | `58.95%` | `41.05%` | `1.44` | 28,920.00 USD |
| `15M` | `Bitunix` | `70.92%` | `29.08%` | `2.44` | 76,290.00 USD |
| `15M` | `Hyperliquid` | `57.06%` | `42.94%` | `1.33` | 22,770.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.12%` | `49.88%` | `1.00` | 40,890.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `98.78%` | `1.22%` | `80.97` | 272,370.00 USD |
| `15M` | `HTX` | `79.16%` | `20.84%` | `3.80` | 3,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 0.28 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `98.34%` | `1.66%` | `59.24` | 4,970.00 USD |
| `15M` | `Whale Positions` | `44.1%` | `55.9%` | `0.79` | 651,730.00 USD |
| `15M` | `Global Accounts` | `55.85%` | `44.15%` | `1.27` | 2,400,000.00 USD |
| `1H` | `BCH` | `46.52%` | `53.48%` | `0.87` | 9,290,000.00 USD |
| `1H` | `Binance` | `46.1%` | `53.9%` | `0.86` | 3,600,000.00 USD |
| `1H` | `OKX` | `37.78%` | `62.22%` | `0.61` | 1,340,000.00 USD |
| `1H` | `Bybit` | `54.48%` | `45.52%` | `1.20` | 633,430.00 USD |
| `1H` | `KuCoin` | `49.45%` | `50.55%` | `0.98` | 621,380.00 USD |
| `1H` | `Gate` | `56.42%` | `43.58%` | `1.29` | 582,580.00 USD |
| `1H` | `Bitget` | `55.98%` | `44.02%` | `1.27` | 176,700.00 USD |
| `1H` | `BingX` | `25.05%` | `74.95%` | `0.33` | 648,510.00 USD |
| `1H` | `MEXC` | `49.86%` | `50.14%` | `0.99` | 288,670.00 USD |
| `1H` | `Bitunix` | `47.98%` | `52.02%` | `0.92` | 188,290.00 USD |
| `1H` | `Hyperliquid` | `41.8%` | `58.2%` | `0.72` | 246,800.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.24%` | `49.76%` | `1.01` | 694,200.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `84.85%` | `15.15%` | `5.60` | 265,100.00 USD |
| `1H` | `HTX` | `35.96%` | `64.04%` | `0.56` | 3,290.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `48.7%` | `51.3%` | `0.95` | 6,740.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `46.1%` | `53.9%` | `0.86` | 3,600,000.00 USD |
| `1H` | `Global Accounts` | `46.52%` | `53.48%` | `0.87` | 9,290,000.00 USD |
| `4H` | `BCH` | `49.28%` | `50.72%` | `0.97` | 56,130,000.00 USD |
| `4H` | `Binance` | `46.75%` | `53.25%` | `0.88` | 18,010,000.00 USD |
| `4H` | `OKX` | `48.27%` | `51.73%` | `0.93` | 7,520,000.00 USD |
| `4H` | `Bybit` | `54.09%` | `45.91%` | `1.18` | 4,620,000.00 USD |
| `4H` | `KuCoin` | `47.03%` | `52.97%` | `0.89` | 497,760.00 USD |
| `4H` | `Gate` | `47.56%` | `52.44%` | `0.91` | 4,880,000.00 USD |
| `4H` | `Bitget` | `56.12%` | `43.88%` | `1.28` | 1,910,000.00 USD |
| `4H` | `BingX` | `40.98%` | `59.02%` | `0.69` | 9,790,000.00 USD |
| `4H` | `MEXC` | `52.86%` | `47.14%` | `1.12` | 2,610,000.00 USD |
| `4H` | `Bitunix` | `50.32%` | `49.68%` | `1.01` | 1,560,000.00 USD |
| `4H` | `Hyperliquid` | `58.23%` | `41.77%` | `1.39` | 974,590.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.95%` | `49.05%` | `1.04` | 1,710,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.4%` | `3.6%` | `26.78` | 1,770,000.00 USD |
| `4H` | `HTX` | `53.81%` | `46.19%` | `1.16` | 112,320.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `43.06%` | `56.94%` | `0.76` | 34,320.00 USD |
| `4H` | `Aster` | `63.16%` | `36.84%` | `1.71` | 112,620.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.81%` | `23.19%` | `3.31` | 26,010.00 USD |
| `4H` | `Whale Positions` | `46.75%` | `53.25%` | `0.88` | 18,010,000.00 USD |
| `4H` | `Global Accounts` | `49.28%` | `50.72%` | `0.97` | 56,130,000.00 USD |


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
| `0:00 UTC` | `285.00` | `284.99` | `285.00` | `285.01` | `284.93` | 6,936.85 USD | 6,573.54 USD | 363.31 USD | 6,210.24 USD | `+89.53%` | `2B / 0S` |

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
  * `2026-10-30 10:58:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:58:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:57:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:59:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:59:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:59:46 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
