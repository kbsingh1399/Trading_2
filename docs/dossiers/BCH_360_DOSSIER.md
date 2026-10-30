# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:33:46 IST` (`2026-10-30 11:03:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `285.66` | **Live Ask Quote**: `286.24` | **Mid Price**: `285.95`
- **Spread Points**: `580.00` | **Spread BPS**: `20.28 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `285.95` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `287.95` | Lower -3.00σ Band: `283.95`
  * Upper +2.51σ Band: `287.52` | Lower -2.51σ Band: `284.38`
  * Upper +2.01σ Band: `287.15` | Lower -2.01σ Band: `284.75`
  * Upper +2.00σ Band: `287.09` | Lower -2.00σ Band: `284.81`
  * Upper +1.28σ Band: `286.75` | Lower -1.28σ Band: `285.15`
  * Upper +1.00σ Band: `286.52` | Lower -1.00σ Band: `285.38`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`285.95` | EMA-20=`285.95` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`285.95` (Slope: `+0.0000`) | EMA-100=`285.95`
  * Institutional Anchors: EMA-144=`285.95` | EMA-200=`285.95` (Slope: `+0.0000`) | EMA-233=`285.95`
- **Range Boundaries**: 24H High=`288.81` | 24H Low=`283.09` | Weekly High=`291.67` | Weekly Low=`280.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `284.54` (Distance: `+0.49%`)
  * Point of Control (POC) = `283.72` (Distance: `+0.79%`)
  * Value Area Low (VAL) = `273.18` (Distance: `+4.67%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`275.18`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`287.26` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`287.26` | Low=`279.46`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `284.81` - `287.09`
  * Optimal Trade Entry (OTE 0.705): `286.52`
  * Structural Invalidation Anchor (0.786): `288.24`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.29` | `284.99` | `284.04` | `284.76` | `827` | 235,478.84 USD | 39,289.22 USD | `+16.68%` | -1,540,329.20 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `284.76` | `284.96` | `283.70` | `283.86` | `973` | 276,491.03 USD | -49,734.94 USD | `-17.99%` | -1,590,064.15 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `283.86` | `284.47` | `283.74` | `284.35` | `276` | 78,392.70 USD | 7,793.39 USD | `+9.94%` | -1,582,270.76 USD | `-0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `281.72` | `284.99` | `281.56` | `284.76` | `4,953` | 1,404,905.07 USD | 153,177.98 USD | `+10.90%` | -1,448,967.42 USD | `+0.89` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `284.76` | `286.25` | `283.70` | `286.01` | `3,154` | 898,820.13 USD | 165,203.63 USD | `+18.38%` | -1,283,763.79 USD | `+0.86` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `286.00` | `287.88` | `285.94` | `286.23` | `2,180` | 625,829.37 USD | 263,182.06 USD | `+42.05%` | -1,020,581.73 USD | `+1.23` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `279.03` | `282.29` | `278.54` | `281.15` | `18,009` | 5,054,095.53 USD | -226,117.37 USD | `-4.47%` | -1,690,031.36 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `281.14` | `286.25` | `280.02` | `286.01` | `12,163` | 3,442,669.89 USD | 533,988.41 USD | `+15.51%` | -1,156,042.95 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `286.00` | `287.88` | `285.94` | `286.26` | `2,171` | 623,222.35 USD | 264,614.39 USD | `+42.46%` | -891,428.56 USD | `+0.49` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `284.99` | `278.54` | `284.35` | `44,734` | 12,583,423.82 USD | 376,722.51 USD | `+2.99%` | -1,363,188.14 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `287.88` | `278.54` | `286.26` | `48,811` | 13,750,582.57 USD | 848,482.08 USD | `+6.17%` | -891,428.56 USD | `+0.80` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`285.95`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:32:44 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1939` | `0x12d2...f97f` | `LONG` | 1,034,272.07 USD | `3,627,243,000,000.00` | `303.26` | `285.38` | `0.000000` | -65,727.27 USD | `-6.35%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `70.50` | 2,890.00 USD | 212,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 556.06 USD | 209,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,170.00 USD | 208,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 207,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 206,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 200,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 398.79 USD | 196,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 108.50 USD | 195,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 195,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 174.94 USD | 195,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 195,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 195,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 195,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 2,060.00 USD | 194,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `138.50` | 3,460.00 USD | 192,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 188,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 188,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 186,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 184,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 1,880.00 USD | 184,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 182,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `168.50` | 8,430.00 USD | 181,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `169.50` | 1,280.00 USD | 173,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 172,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 171,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 171,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 171,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 808.66 USD | 170,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 169,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 169,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 168,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 167,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 166,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 210.65 USD | 166,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 165,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 165,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 165,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 164,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 41,790.00 USD | 164,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 122,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 122,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `214.50` | 643.50 USD | 118,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 239.85 USD | 118,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 31,290.00 USD | 117,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 12,900.00 USD | 86,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 73,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 72,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 72,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 114.75 USD | 71,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `230.50` | 1,190.00 USD | 71,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 295.86 USD | 70,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 637.61 USD | 69,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 69,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `238.50` | 3,790.00 USD | 45,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 41,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.00` | 10,920,000.00 USD | 10,920,000.00 USD | 887.27 USD | 588.60 USD | 43.05 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.40` | 10,920,000.00 USD | 10,920,000.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,920,000.00 USD | 10,920,000.00 USD | 1,270.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.20` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 40,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.60` | 10,910,000.00 USD | 10,910,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.00` | 10,910,000.00 USD | 10,910,000.00 USD | 27,990.00 USD | 11,260.00 USD | 21,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 10,840,000.00 USD | 10,840,000.00 USD | 27,150.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 7,180.00 USD | 40,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 10,810,000.00 USD | 10,810,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.20` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 33,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.60` | 10,790,000.00 USD | 10,790,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.00` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.40` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 6.53 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 5,760.00 USD | 31,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 10,730,000.00 USD | 10,730,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.20` | 10,710,000.00 USD | 10,710,000.00 USD | 599.05 USD | 15,350.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.60` | 10,690,000.00 USD | 10,690,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.00` | 10,670,000.00 USD | 10,670,000.00 USD | 11,860.00 USD | 8,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 10,650,000.00 USD | 10,650,000.00 USD | 11,440.00 USD | 10,300.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 10,620,000.00 USD | 10,620,000.00 USD | 4,590.00 USD | 472.85 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 10,620,000.00 USD | 10,620,000.00 USD | 14,580.00 USD | 17,320.00 USD | 2,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.60` | 10,580,000.00 USD | 10,580,000.00 USD | 9,000.00 USD | 4,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.00` | 10,570,000.00 USD | 10,570,000.00 USD | 555.60 USD | 310.87 USD | 2,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 10,570,000.00 USD | 10,570,000.00 USD | 13,830.00 USD | 3,060.00 USD | 28,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 10,520,000.00 USD | 10,520,000.00 USD | 28,270.00 USD | 15,790.00 USD | 28,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 10,450,000.00 USD | 10,450,000.00 USD | 23,830.00 USD | 30,530.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.60` | 10,390,000.00 USD | 10,390,000.00 USD | 46,340.00 USD | 35,710.00 USD | 16,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.00` | 10,290,000.00 USD | 10,290,000.00 USD | 38,050.00 USD | 9,910.00 USD | 22,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.40` | 5,240,000.00 USD | 5,240,000.00 USD | 9,190.00 USD | 6,150.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 10,220,000.00 USD | 10,220,000.00 USD | 22,500.00 USD | 35,680.00 USD | 12,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 24,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.80` | 5,210,000.00 USD | 5,210,000.00 USD | 9,730.00 USD | 14,160.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.80` | 10,150,000.00 USD | 10,150,000.00 USD | 32,990.00 USD | 60,940.00 USD | 27,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.20` | 5,180,000.00 USD | 5,180,000.00 USD | 25,370.00 USD | 23,980.00 USD | 16,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 10,030,000.00 USD | 10,030,000.00 USD | 44,420.00 USD | 56,200.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.60` | 5,110,000.00 USD | 5,110,000.00 USD | 26,820.00 USD | 47,060.00 USD | 19,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.60` | 9,910,000.00 USD | 9,910,000.00 USD | 51,190.00 USD | 89,120.00 USD | 44,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.00` | 5,020,000.00 USD | 5,020,000.00 USD | 16,340.00 USD | 11,100.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.00` | 9,720,000.00 USD | 9,720,000.00 USD | 63,990.00 USD | 31,270.00 USD | 32,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.40` | 4,980,000.00 USD | 4,980,000.00 USD | 6,700.00 USD | 1,540.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 9,600,000.00 USD | 9,600,000.00 USD | 53,750.00 USD | 29,340.00 USD | 17,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.80` | 4,970,000.00 USD | 4,970,000.00 USD | 6,800.00 USD | 2,270.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.80` | 9,500,000.00 USD | 9,500,000.00 USD | 24,570.00 USD | 10,300.00 USD | 16.17 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.20` | 4,950,000.00 USD | 4,950,000.00 USD | 8,060.00 USD | 3,900.00 USD | 821.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 9,460,000.00 USD | 9,460,000.00 USD | 12,620.00 USD | 36,470.00 USD | 14,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.60` | 4,940,000.00 USD | 4,940,000.00 USD | 20,500.00 USD | 17,790.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.60` | 9,400,000.00 USD | 9,400,000.00 USD | 27,790.00 USD | 37,080.00 USD | 34,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 4,880,000.00 USD | 4,880,000.00 USD | 5,800.00 USD | 8,100.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.00` | 9,300,000.00 USD | 9,300,000.00 USD | 45,450.00 USD | 35,310.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 4,860,000.00 USD | 4,860,000.00 USD | 8,310.00 USD | 13,680.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 9,200,000.00 USD | 9,200,000.00 USD | 19,460.00 USD | 25,910.00 USD | 60,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 4,830,000.00 USD | 4,830,000.00 USD | 2,210.00 USD | 3,080.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 9,090,000.00 USD | 9,090,000.00 USD | 50,650.00 USD | 29,470.00 USD | 37,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 4,820,000.00 USD | 4,820,000.00 USD | 16,750.00 USD | 17,660.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 8,970,000.00 USD | 8,970,000.00 USD | 23,880.00 USD | 12,570.00 USD | 25,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.60` | 4,780,000.00 USD | 4,780,000.00 USD | 17,490.00 USD | 32,020.00 USD | 23,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.60` | 8,910,000.00 USD | 8,910,000.00 USD | 33,430.00 USD | 17,110.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 4,700,000.00 USD | 4,700,000.00 USD | 10,010.00 USD | 11,710.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.00` | 8,830,000.00 USD | 8,830,000.00 USD | 18,300.00 USD | 16,500.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 4,670,000.00 USD | 4,670,000.00 USD | 7,460.00 USD | 31,910.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 8,770,000.00 USD | 8,770,000.00 USD | 29,190.00 USD | 739.13 USD | 23,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 4,610,000.00 USD | 4,610,000.00 USD | 1,820.00 USD | 5,950.00 USD | 14,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 8,720,000.00 USD | 8,720,000.00 USD | 32,310.00 USD | 13,750.00 USD | 56,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 4,580,000.00 USD | 4,580,000.00 USD | 14,160.00 USD | 3,660.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 8,610,000.00 USD | 8,610,000.00 USD | 15,600.00 USD | 10,170.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.60` | 4,560,000.00 USD | 4,560,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.60` | 8,580,000.00 USD | 8,580,000.00 USD | 34,480.00 USD | 4,400.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 4,540,000.00 USD | 4,540,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.00` | 8,530,000.00 USD | 8,530,000.00 USD | 26,960.00 USD | 4,790.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 4,480,000.00 USD | 4,480,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 8,490,000.00 USD | 8,490,000.00 USD | 128,170.00 USD | 37,820.00 USD | 92,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 645.99 USD | 17,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 4,430,000.00 USD | 4,430,000.00 USD | 8,320.00 USD | 30,390.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 8,230,000.00 USD | 8,230,000.00 USD | 59,230.00 USD | 2,500.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 4,350,000.00 USD | 4,350,000.00 USD | 14,560.00 USD | 12,990.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 8,130,000.00 USD | 8,130,000.00 USD | 5,210.00 USD | 45,200.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 4,300,000.00 USD | 4,300,000.00 USD | 13,590.00 USD | 4,640.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.60` | 8,070,000.00 USD | 8,070,000.00 USD | 20,030.00 USD | 8,340.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 4,260,000.00 USD | 4,260,000.00 USD | 45,280.00 USD | 32,840.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.00` | 8,030,000.00 USD | 8,030,000.00 USD | 103,390.00 USD | 63,410.00 USD | 106,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 4,160,000.00 USD | 4,160,000.00 USD | 19,610.00 USD | 7,660.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 7,760,000.00 USD | 7,760,000.00 USD | 4,590.00 USD | 3,590.00 USD | 74,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 16,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 4,120,000.00 USD | 4,120,000.00 USD | 1,360.00 USD | 46,690.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,670,000.00 USD | 7,670,000.00 USD | 14,600.00 USD | 56,470.00 USD | 37,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 4,040,000.00 USD | 4,040,000.00 USD | 8,180.00 USD | 23,140.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 7,560,000.00 USD | 7,560,000.00 USD | 6,110.00 USD | 90,180.00 USD | 16,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 3,980,000.00 USD | 3,980,000.00 USD | 18,900.00 USD | 55,190.00 USD | 53,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.60` | 7,450,000.00 USD | 7,450,000.00 USD | 24,520.00 USD | 84,260.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 3,850,000.00 USD | 3,850,000.00 USD | 17,910.00 USD | 44,250.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.00` | 7,300,000.00 USD | 7,300,000.00 USD | 61,230.00 USD | 39,230.00 USD | 81,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 3,770,000.00 USD | 3,770,000.00 USD | 21,110.00 USD | 6,200.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 7,110,000.00 USD | 7,110,000.00 USD | 28,440.00 USD | 55,580.00 USD | 40.11 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,310.00 USD | 14,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.80` | 3,730,000.00 USD | 3,730,000.00 USD | 747.53 USD | 13,250.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 7,030,000.00 USD | 7,030,000.00 USD | 73,660.00 USD | 45,060.00 USD | 32,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 3,700,000.00 USD | 3,700,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 6,880,000.00 USD | 6,880,000.00 USD | 21,560.00 USD | 13,710.00 USD | 104.44 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 3,620,000.00 USD | 3,620,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.60` | 6,840,000.00 USD | 6,840,000.00 USD | 278,330.00 USD | 1,880.00 USD | 83,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 3,520,000.00 USD | 3,520,000.00 USD | 52,440.00 USD | 15,650.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.00` | 6,480,000.00 USD | 6,480,000.00 USD | 135,390.00 USD | 629.16 USD | 34,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 3,440,000.00 USD | 3,440,000.00 USD | 6,130.00 USD | 20,240.00 USD | 21.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 6,310,000.00 USD | 6,310,000.00 USD | 44,740.00 USD | 21,130.00 USD | 97.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.80` | 3,410,000.00 USD | 3,410,000.00 USD | 22,660.00 USD | 1,670.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 6,240,000.00 USD | 6,240,000.00 USD | 26,950.00 USD | 2,610.00 USD | 157.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 3,370,000.00 USD | 3,370,000.00 USD | 75,930.00 USD | 3,490.00 USD | 33,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 6,210,000.00 USD | 6,210,000.00 USD | 106,380.00 USD | 1,640.00 USD | 33,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 531.00 USD | 13,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.60` | 3,250,000.00 USD | 3,250,000.00 USD | 415.98 USD | 788.61 USD | 12.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.60` | 6,070,000.00 USD | 6,070,000.00 USD | 199,660.00 USD | 694.90 USD | 8.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 3,250,000.00 USD | 3,250,000.00 USD | 12,200.00 USD | 209.24 USD | 5.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.00` | 5,870,000.00 USD | 5,870,000.00 USD | 140,360.00 USD | 645.20 USD | 72.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 3,240,000.00 USD | 3,240,000.00 USD | 4,400.00 USD | 13,530.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 5,730,000.00 USD | 5,730,000.00 USD | 106,830.00 USD | 804.70 USD | 226.57 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.80` | 3,220,000.00 USD | 3,220,000.00 USD | 22,750.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 5,620,000.00 USD | 5,620,000.00 USD | 125,320.00 USD | 63,260.00 USD | 7.04 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 3,160,000.00 USD | 3,160,000.00 USD | 43,580.00 USD | 34,990.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 5,430,000.00 USD | 5,430,000.00 USD | 101,740.00 USD | 26,850.00 USD | 201.76 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `267.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.60` | 3,070,000.00 USD | 3,070,000.00 USD | 10,330.00 USD | 72,630.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.60` | 5,300,000.00 USD | 5,300,000.00 USD | 75,350.00 USD | 61,270.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 2,970,000.00 USD | 2,970,000.00 USD | 19,060.00 USD | 4,020.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.00` | 5,130,000.00 USD | 5,130,000.00 USD | 234,660.00 USD | 25,100.00 USD | 184.22 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 2,890,000.00 USD | 2,890,000.00 USD | 18,310.00 USD | 43,230.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 4,870,000.00 USD | 4,870,000.00 USD | 136,830.00 USD | 124,980.00 USD | 95,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.80` | 2,820,000.00 USD | 2,820,000.00 USD | 21,330.00 USD | 11,530.00 USD | 146.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 4,510,000.00 USD | 4,510,000.00 USD | 23,340.00 USD | 18,320.00 USD | 241.40 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 2,780,000.00 USD | 2,780,000.00 USD | 10,990.00 USD | 2,810.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 1,560.00 USD | 260.32 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.60` | 2,760,000.00 USD | 2,760,000.00 USD | 6,520.00 USD | 19,580.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.60` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 3,480.00 USD | 153.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 2,720,000.00 USD | 2,720,000.00 USD | 7,960.00 USD | 12,030.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.00` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 1,310.00 USD | 64.60 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 2,700,000.00 USD | 2,700,000.00 USD | 54,750.00 USD | 1,930.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 27.41 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.80` | 2,640,000.00 USD | 2,640,000.00 USD | 3,210.00 USD | 15,660.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 4,460,000.00 USD | 4,460,000.00 USD | 33,050.00 USD | 0.00 USD | 6.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 2,620,000.00 USD | 2,620,000.00 USD | 12,890.00 USD | 6,410.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.20` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.60` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 8,940.00 USD | 13,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.60` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 7,250.00 USD | 61,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 2,560,000.00 USD | 2,560,000.00 USD | 28,410.00 USD | 52,240.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.00` | 4,340,000.00 USD | 4,340,000.00 USD | 61,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 2,470,000.00 USD | 2,470,000.00 USD | 10,530.00 USD | 35,390.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `272.50` | 214.19 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `272.80` | 2,370,000.00 USD | 2,370,000.00 USD | 62,230.00 USD | 15,740.00 USD | 68,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 4,250,000.00 USD | 4,250,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 2,220,000.00 USD | 2,220,000.00 USD | 32,520.00 USD | 117,860.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 95,060.00 USD | 185,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 2,030,000.00 USD | 2,030,000.00 USD | 42,760.00 USD | 18,430.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.60` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.00` | 1,910,000.00 USD | 1,910,000.00 USD | 159,390.00 USD | 97,110.00 USD | 39,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.00` | 3,730,000.00 USD | 3,730,000.00 USD | 466,260.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 1,620,000.00 USD | 1,620,000.00 USD | 155,650.00 USD | 27,970.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 3,170,000.00 USD | 3,170,000.00 USD | 413,010.00 USD | 51,840.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.80` | 1,390,000.00 USD | 1,390,000.00 USD | 70,330.00 USD | 22,510.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 2,620,000.00 USD | 2,620,000.00 USD | 334,980.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.20` | 1,270,000.00 USD | 1,270,000.00 USD | 11,720.00 USD | 3,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 2,250,000.00 USD | 2,250,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.60` | 1,250,000.00 USD | 1,250,000.00 USD | 35,420.00 USD | 15,980.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.60` | 2,170,000.00 USD | 2,170,000.00 USD | 1,350.00 USD | 0.00 USD | 48,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.00` | 1,180,000.00 USD | 1,180,000.00 USD | 143,900.00 USD | 18,930.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.00` | 2,120,000.00 USD | 2,120,000.00 USD | 3,140.00 USD | 23,010.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.40` | 973,410.00 USD | 973,410.00 USD | 40,580.00 USD | 16,150.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 2,060,000.00 USD | 2,060,000.00 USD | 217,250.00 USD | 0.00 USD | 103,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.80` | 898,010.00 USD | 898,010.00 USD | 11,880.00 USD | 25,410.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 1,740,000.00 USD | 1,740,000.00 USD | 16,100.00 USD | 0.00 USD | 79.76 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.20` | 835,550.00 USD | 835,550.00 USD | 25,720.00 USD | 17,880.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 1,720,000.00 USD | 1,720,000.00 USD | 28,580.00 USD | 42,210.00 USD | 163,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.60` | 765,410.00 USD | 765,410.00 USD | 26,620.00 USD | 21,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.60` | 1,490,000.00 USD | 1,490,000.00 USD | 123,610.00 USD | 193,330.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.00` | 717,700.00 USD | 717,700.00 USD | 21,070.00 USD | 54,860.00 USD | 103,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.00` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 1,830.00 USD | 59,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.40` | 537,810.00 USD | 537,810.00 USD | 57,720.00 USD | 125,180.00 USD | 77,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.40` | 1,090,000.00 USD | 1,090,000.00 USD | 76,060.00 USD | 35,270.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.80` | 277,570.00 USD | 277,570.00 USD | 55,370.00 USD | 10,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 824,280.00 USD | 824,280.00 USD | 0.00 USD | 49,750.00 USD | 23,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.20` | 211,370.00 USD | 211,370.00 USD | 4,440.00 USD | 3,800.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 750,540.00 USD | 750,540.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.60` | 179,730.00 USD | 179,730.00 USD | 0.00 USD | 0.00 USD | 47,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.60` | 747,880.00 USD | 747,880.00 USD | 0.00 USD | 0.00 USD | 154.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.00` | 132,270.00 USD | 132,270.00 USD | 0.00 USD | 13,070.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.00` | 747,720.00 USD | 747,720.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.80` | 87,860.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 713,980.00 USD | 713,980.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 698,440.00 USD | 698,440.00 USD | 0.00 USD | 14,140.00 USD | 79,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.60` | 604,590.00 USD | 604,590.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.00` | 482,210.00 USD | 482,210.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.40` | 87,850.00 USD | 87,850.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.40` | 461,500.00 USD | 461,500.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.20` | 79,590.00 USD | 79,590.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 457,980.00 USD | 457,980.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `283.50` | 306.46 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `283.60` | 454,530.00 USD | 454,530.00 USD | 0.00 USD | 0.00 USD | 1.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.00` | 454,530.00 USD | 454,530.00 USD | 2,000.00 USD | 0.00 USD | 55.52 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.40` | 452,480.00 USD | 452,480.00 USD | 1,560.00 USD | 0.00 USD | 16.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `284.80` | 450,900.00 USD | 450,900.00 USD | 0.00 USD | 0.00 USD | 132.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `285.20` | 78,310.00 USD | 78,310.00 USD | 36,620.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.20` | 450,770.00 USD | 450,770.00 USD | 126,910.00 USD | 206,630.00 USD | 65,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.60` | 27,570.00 USD | 27,570.00 USD | 27,570.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `285.60` | 51,410.00 USD | 51,410.00 USD | 50,130.00 USD | 1,280.00 USD | 7.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.00` | 99,520.00 USD | 99,520.00 USD | 29,220.00 USD | 2,980.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.00` | 3,770.00 USD | 3,770.00 USD | 1,200.00 USD | 2,560.00 USD | 14.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.40` | 121,480.00 USD | 121,480.00 USD | 17,340.00 USD | 4,610.00 USD | 4.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 141,230.00 USD | 141,230.00 USD | 0.00 USD | 137,440.00 USD | 11.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.80` | 228,380.00 USD | 228,380.00 USD | 18,110.00 USD | 10,660.00 USD | 78,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 293,370.00 USD | 293,370.00 USD | 30,110.00 USD | 122,000.00 USD | 31.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.20` | 427,500.00 USD | 427,500.00 USD | 112,240.00 USD | 47,050.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 492,710.00 USD | 492,710.00 USD | 82,910.00 USD | 116,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.60` | 576,390.00 USD | 576,390.00 USD | 47,390.00 USD | 34,850.00 USD | 66,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.60` | 650,070.00 USD | 650,070.00 USD | 70,340.00 USD | 33,740.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.00` | 676,230.00 USD | 676,230.00 USD | 9,440.00 USD | 26,480.00 USD | 63,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.00` | 922,380.00 USD | 922,380.00 USD | 0.00 USD | 272,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.40` | 795,940.00 USD | 795,940.00 USD | 68,380.00 USD | 22,110.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.40` | 965,620.00 USD | 965,620.00 USD | 0.00 USD | 1,550.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.80` | 879,250.00 USD | 879,250.00 USD | 43,690.00 USD | 32,420.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 1,230,000.00 USD | 1,230,000.00 USD | 124,780.00 USD | 15,650.00 USD | 122,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 968,510.00 USD | 968,510.00 USD | 6,160.00 USD | 52,920.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.60` | 1,180,000.00 USD | 1,180,000.00 USD | 25,200.00 USD | 66,520.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.60` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 62,370.00 USD | 95,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.00` | 1,490,000.00 USD | 1,490,000.00 USD | 115,670.00 USD | 66,820.00 USD | 124,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.00` | 1,690,000.00 USD | 1,690,000.00 USD | 53,890.00 USD | 69,350.00 USD | 122,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.40` | 1,690,000.00 USD | 1,690,000.00 USD | 40,570.00 USD | 111,760.00 USD | 49,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 1,750,000.00 USD | 1,750,000.00 USD | 33,530.00 USD | 19,060.00 USD | 25.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.80` | 1,870,000.00 USD | 1,870,000.00 USD | 56,480.00 USD | 71,550.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 1,870,000.00 USD | 1,870,000.00 USD | 30,940.00 USD | 1,760.00 USD | 90,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 1,950,000.00 USD | 1,950,000.00 USD | 28,320.00 USD | 25,130.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 1,950,000.00 USD | 1,950,000.00 USD | 24,680.00 USD | 52,140.00 USD | 49.23 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.60` | 2,000,000.00 USD | 2,000,000.00 USD | 12,550.00 USD | 6,560.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.60` | 2,050,000.00 USD | 2,050,000.00 USD | 2,710.00 USD | 85,290.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 2,040,000.00 USD | 2,040,000.00 USD | 7,010.00 USD | 30,490.00 USD | 31.89 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.00` | 2,200,000.00 USD | 2,200,000.00 USD | 2,560.00 USD | 149,160.00 USD | 113.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 2,100,000.00 USD | 2,100,000.00 USD | 29,860.00 USD | 14,820.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 25,520.00 USD | 121.87 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 6,050.00 USD | 10,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `292.80` | 2,160,000.00 USD | 2,160,000.00 USD | 29,430.00 USD | 27,590.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,330,000.00 USD | 2,330,000.00 USD | 887.27 USD | 101,280.00 USD | 43.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 2,250,000.00 USD | 2,250,000.00 USD | 50,900.00 USD | 12,760.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 2,500,000.00 USD | 2,500,000.00 USD | 33,580.00 USD | 132,080.00 USD | 8.63 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 2,400,000.00 USD | 2,400,000.00 USD | 77,380.00 USD | 48,560.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.60` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 1,860.00 USD | 12.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 2,530,000.00 USD | 2,530,000.00 USD | 30,750.00 USD | 23,790.00 USD | 70,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.00` | 2,680,000.00 USD | 2,680,000.00 USD | 54,350.00 USD | 34,230.00 USD | 95,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 2,770,000.00 USD | 2,770,000.00 USD | 64,400.00 USD | 64,490.00 USD | 116,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 2,990,000.00 USD | 2,990,000.00 USD | 201,580.00 USD | 9,460.00 USD | 92,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 2,910,000.00 USD | 2,910,000.00 USD | 59,910.00 USD | 35,750.00 USD | 44,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,250,000.00 USD | 3,250,000.00 USD | 63,770.00 USD | 108,720.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 3,050,000.00 USD | 3,050,000.00 USD | 8,650.00 USD | 28,960.00 USD | 99,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 3,530,000.00 USD | 3,530,000.00 USD | 733.30 USD | 64,810.00 USD | 214,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.60` | 3,300,000.00 USD | 3,300,000.00 USD | 73,320.00 USD | 48,980.00 USD | 132,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.60` | 4,090,000.00 USD | 4,090,000.00 USD | 176,660.00 USD | 91,360.00 USD | 294,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 3,520,000.00 USD | 3,520,000.00 USD | 56,610.00 USD | 114,680.00 USD | 43,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.00` | 4,380,000.00 USD | 4,380,000.00 USD | 76,740.00 USD | 114,600.00 USD | 98,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 3,660,000.00 USD | 3,660,000.00 USD | 80,090.00 USD | 31,130.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 4,530,000.00 USD | 4,530,000.00 USD | 1,550.00 USD | 78,210.00 USD | 68,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.80` | 3,790,000.00 USD | 3,790,000.00 USD | 24,560.00 USD | 32,150.00 USD | 74,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 4,870,000.00 USD | 4,870,000.00 USD | 133,480.00 USD | 4,410.00 USD | 201,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 3,900,000.00 USD | 3,900,000.00 USD | 56,450.00 USD | 7,700.00 USD | 50,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,020,000.00 USD | 5,020,000.00 USD | 77,480.00 USD | 68,680.00 USD | 85.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 3,950,000.00 USD | 3,950,000.00 USD | 7,640.00 USD | 11,760.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.60` | 5,110,000.00 USD | 5,110,000.00 USD | 1,640.00 USD | 61,200.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 4,070,000.00 USD | 4,070,000.00 USD | 63,620.00 USD | 9,890.00 USD | 41,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.00` | 5,280,000.00 USD | 5,280,000.00 USD | 47,790.00 USD | 44,920.00 USD | 75,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 4,130,000.00 USD | 4,130,000.00 USD | 7,430.00 USD | 2,280.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 5,400,000.00 USD | 5,400,000.00 USD | 32,250.00 USD | 42,940.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.80` | 4,250,000.00 USD | 4,250,000.00 USD | 23,700.00 USD | 457.80 USD | 94,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 5,490,000.00 USD | 5,490,000.00 USD | 69,820.00 USD | 12,530.00 USD | 48.95 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 4,290,000.00 USD | 4,290,000.00 USD | 8,500.00 USD | 15,770.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 5,590,000.00 USD | 5,590,000.00 USD | 2,350.00 USD | 15,140.00 USD | 85,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.60` | 4,350,000.00 USD | 4,350,000.00 USD | 36,030.00 USD | 5,850.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.60` | 5,630,000.00 USD | 5,630,000.00 USD | 4,590.00 USD | 13,830.00 USD | 19,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 4,400,000.00 USD | 4,400,000.00 USD | 3,760.00 USD | 14,300.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.00` | 5,690,000.00 USD | 5,690,000.00 USD | 53,130.00 USD | 10,090.00 USD | 13.78 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 4,510,000.00 USD | 4,510,000.00 USD | 41,880.00 USD | 31,000.00 USD | 42,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 5,690,000.00 USD | 5,690,000.00 USD | 2,070.00 USD | 645.96 USD | 6.37 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 991.05 USD | 11,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `300.80` | 4,530,000.00 USD | 4,530,000.00 USD | 790.57 USD | 879.82 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 5,840,000.00 USD | 5,840,000.00 USD | 24,730.00 USD | 71,120.00 USD | 48,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 4,580,000.00 USD | 4,580,000.00 USD | 348.65 USD | 15,610.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 6,020,000.00 USD | 6,020,000.00 USD | 48,570.00 USD | 42,080.00 USD | 91,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.60` | 4,640,000.00 USD | 4,640,000.00 USD | 19,530.00 USD | 8,470.00 USD | 34,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.60` | 6,220,000.00 USD | 6,220,000.00 USD | 62,390.00 USD | 79,410.00 USD | 59,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 4,710,000.00 USD | 4,710,000.00 USD | 25,220.00 USD | 28,210.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.00` | 6,450,000.00 USD | 6,450,000.00 USD | 52,640.00 USD | 150,800.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 4,740,000.00 USD | 4,740,000.00 USD | 11,420.00 USD | 5,200.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 6,550,000.00 USD | 6,550,000.00 USD | 580.96 USD | 99,100.00 USD | 115.12 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 4,790,000.00 USD | 4,790,000.00 USD | 4,420.00 USD | 13,290.00 USD | 34,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 6,780,000.00 USD | 6,780,000.00 USD | 71,700.00 USD | 112,610.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 4,820,000.00 USD | 4,820,000.00 USD | 21,180.00 USD | 1,390.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 1,780.00 USD | 21.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 4,830,000.00 USD | 4,830,000.00 USD | 228.18 USD | 2,000.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.60` | 6,810,000.00 USD | 6,810,000.00 USD | 2,130.00 USD | 693.54 USD | 24,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 4,870,000.00 USD | 4,870,000.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.00` | 6,860,000.00 USD | 6,860,000.00 USD | 20,680.00 USD | 14,630.00 USD | 21,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 4,930,000.00 USD | 4,930,000.00 USD | 9,750.00 USD | 2,470.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 6,880,000.00 USD | 6,880,000.00 USD | 1,340.00 USD | 11,280.00 USD | 58.87 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 4,960,000.00 USD | 4,960,000.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 6,920,000.00 USD | 6,920,000.00 USD | 34,540.00 USD | 682.27 USD | 3,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 4,970,000.00 USD | 4,970,000.00 USD | 47.98 USD | 5,330.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 7,250,000.00 USD | 7,250,000.00 USD | 113,060.00 USD | 128,470.00 USD | 89,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 4,970,000.00 USD | 4,970,000.00 USD | 3,060.00 USD | 440.72 USD | 12.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.60` | 7,390,000.00 USD | 7,390,000.00 USD | 76,400.00 USD | 21,950.00 USD | 41,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 5,000,000.00 USD | 5,000,000.00 USD | 7,500.00 USD | 5,780.00 USD | 12,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.00` | 7,540,000.00 USD | 7,540,000.00 USD | 60,790.00 USD | 50,650.00 USD | 44,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 5,010,000.00 USD | 5,010,000.00 USD | 7,310.00 USD | 183.24 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 7,670,000.00 USD | 7,670,000.00 USD | 35,090.00 USD | 65,940.00 USD | 25,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 5,080,000.00 USD | 5,080,000.00 USD | 19,990.00 USD | 35,330.00 USD | 11,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 7,890,000.00 USD | 7,890,000.00 USD | 84,850.00 USD | 66,200.00 USD | 66,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 5,140,000.00 USD | 5,140,000.00 USD | 11,270.00 USD | 19,960.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 8,090,000.00 USD | 8,090,000.00 USD | 11,730.00 USD | 87,980.00 USD | 106,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.60` | 5,190,000.00 USD | 5,190,000.00 USD | 22,580.00 USD | 27,240.00 USD | 5.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.60` | 8,350,000.00 USD | 8,350,000.00 USD | 78,600.00 USD | 122,070.00 USD | 56,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 5,230,000.00 USD | 5,230,000.00 USD | 16,340.00 USD | 10,700.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.00` | 8,610,000.00 USD | 8,610,000.00 USD | 125,470.00 USD | 70,950.00 USD | 60,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 5,240,000.00 USD | 5,240,000.00 USD | 3,150.00 USD | 212.94 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 8,900,000.00 USD | 8,900,000.00 USD | 131,420.00 USD | 45,250.00 USD | 114,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.80` | 5,250,000.00 USD | 5,250,000.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,010,000.00 USD | 9,010,000.00 USD | 54,880.00 USD | 42,230.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.20` | 5,250,000.00 USD | 5,250,000.00 USD | 2,990.00 USD | 1,190.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 9,100,000.00 USD | 9,100,000.00 USD | 33,440.00 USD | 19,290.00 USD | 32,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.60` | 5,270,000.00 USD | 5,270,000.00 USD | 8,250.00 USD | 8,700.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.60` | 9,380,000.00 USD | 9,380,000.00 USD | 41,230.00 USD | 107,950.00 USD | 130,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.00` | 5,290,000.00 USD | 5,290,000.00 USD | 15,210.00 USD | 1,250.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.00` | 9,580,000.00 USD | 9,580,000.00 USD | 20,240.00 USD | 98,540.00 USD | 82,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.40` | 5,310,000.00 USD | 5,310,000.00 USD | 176.40 USD | 5,960.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 9,770,000.00 USD | 9,770,000.00 USD | 91,290.00 USD | 74,340.00 USD | 21,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.80` | 5,320,000.00 USD | 5,320,000.00 USD | 5,080.00 USD | 2,080.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 9,850,000.00 USD | 9,850,000.00 USD | 29,950.00 USD | 35,930.00 USD | 12,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.20` | 5,330,000.00 USD | 5,330,000.00 USD | 257.90 USD | 3,180.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,060,000.00 USD | 10,060,000.00 USD | 74,340.00 USD | 65,480.00 USD | 72,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.60` | 5,340,000.00 USD | 5,340,000.00 USD | 7,100.00 USD | 10,150.00 USD | 14.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.60` | 10,120,000.00 USD | 10,120,000.00 USD | 40,900.00 USD | 10,550.00 USD | 5,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.00` | 5,350,000.00 USD | 5,350,000.00 USD | 1,190.00 USD | 4,770.00 USD | 4,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.00` | 10,190,000.00 USD | 10,190,000.00 USD | 40,590.00 USD | 1,560.00 USD | 28,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.40` | 5,410,000.00 USD | 5,410,000.00 USD | 17,490.00 USD | 16,020.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 10,270,000.00 USD | 10,270,000.00 USD | 28,530.00 USD | 23,430.00 USD | 31,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.80` | 5,440,000.00 USD | 5,440,000.00 USD | 9,120.00 USD | 2,930.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,300,000.00 USD | 10,300,000.00 USD | 15,280.00 USD | 8,600.00 USD | 7,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.20` | 5,460,000.00 USD | 5,460,000.00 USD | 40.35 USD | 15,380.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 10,380,000.00 USD | 10,380,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.60` | 5,480,000.00 USD | 5,480,000.00 USD | 8,180.00 USD | 7,190.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.60` | 10,420,000.00 USD | 10,420,000.00 USD | 10,400.00 USD | 755.05 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.00` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.00` | 10,470,000.00 USD | 10,470,000.00 USD | 22,920.00 USD | 815.59 USD | 20,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.40` | 5,500,000.00 USD | 5,500,000.00 USD | 4,210.00 USD | 2,610.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 10,550,000.00 USD | 10,550,000.00 USD | 51,980.00 USD | 7,060.00 USD | 24,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.80` | 5,510,000.00 USD | 5,510,000.00 USD | 32.00 USD | 3,660.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 10,580,000.00 USD | 10,580,000.00 USD | 17,720.00 USD | 0.00 USD | 10,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 1,400.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 258.00 USD | 42.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.60` | 10,640,000.00 USD | 10,640,000.00 USD | 1,070.00 USD | 28,580.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.00` | 10,680,000.00 USD | 10,680,000.00 USD | 38,990.00 USD | 5,120.00 USD | 46.30 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 10,800,000.00 USD | 10,800,000.00 USD | 16,580.00 USD | 40,060.00 USD | 61,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 10,800,000.00 USD | 10,800,000.00 USD | 1,990.00 USD | 667.80 USD | 110.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 10,820,000.00 USD | 10,820,000.00 USD | 15,590.00 USD | 748.91 USD | 114.13 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.60` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 265.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 10,840,000.00 USD | 10,840,000.00 USD | 20,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 12,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `324.50` | 2,220.00 USD | 14,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 25,530.00 USD | 40,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `342.50` | 1,370.00 USD | 41,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 42,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 43,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `373.50` | 41,090.00 USD | 84,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `406.50` | 10,640.00 USD | 94,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 141,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 141,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `552.50` | 195.03 USD | 142,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 142,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `Sell Stop` | `143.50` | 468,050.00 USD | 0.00 USD | 210.94 USD | `-49.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 467,840.00 USD | 0.00 USD | 2,070.00 USD | `-49.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 465,770.00 USD | 0.00 USD | 489.38 USD | `-42.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 465,280.00 USD | 0.00 USD | 2,530.00 USD | `-37.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 462,750.00 USD | 0.00 USD | 490.59 USD | `-35.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 462,260.00 USD | 0.00 USD | 482.01 USD | `-31.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 461,780.00 USD | 0.00 USD | 189.07 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 461,590.00 USD | 0.00 USD | 441.60 USD | `-27.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 461,150.00 USD | 0.00 USD | 299.96 USD | `-26.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 460,850.00 USD | 0.00 USD | 715.29 USD | `-26.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 460,140.00 USD | 0.00 USD | 638.36 USD | `-22.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 459,500.00 USD | 0.00 USD | 740.85 USD | `-21.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 458,760.00 USD | 0.00 USD | 478.48 USD | `-20.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 458,280.00 USD | 0.00 USD | 389.48 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 457,890.00 USD | 0.00 USD | 812.38 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 457,080.00 USD | 0.00 USD | 220.64 USD | `-17.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 456,860.00 USD | 0.00 USD | 429.30 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 456,430.00 USD | 0.00 USD | 296.50 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 456,130.00 USD | 0.00 USD | 216.45 USD | `-16.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 455,910.00 USD | 0.00 USD | 387.76 USD | `-15.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 455,530.00 USD | 0.00 USD | 18,080.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 437,440.00 USD | 0.00 USD | 1,630.00 USD | `-13.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 435,820.00 USD | 0.00 USD | 2,700.00 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 433,120.00 USD | 0.00 USD | 2,940.00 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 430,170.00 USD | 0.00 USD | 4,560.00 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 425,610.00 USD | 0.00 USD | 1,850.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 423,770.00 USD | 0.00 USD | 231.54 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 423,540.00 USD | 0.00 USD | 109.26 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 423,430.00 USD | 0.00 USD | 1,780.00 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 421,650.00 USD | 0.00 USD | 51,300.00 USD | `-10.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 370,350.00 USD | 0.00 USD | 250.81 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 370,100.00 USD | 0.00 USD | 2,370.00 USD | `-9.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 367,730.00 USD | 0.00 USD | 269,800.00 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 97,930.00 USD | 0.00 USD | 3,600.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 94,330.00 USD | 0.00 USD | 199.17 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 94,130.00 USD | 0.00 USD | 2,180.00 USD | `-7.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 91,960.00 USD | 0.00 USD | 241.98 USD | `-6.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 91,710.00 USD | 0.00 USD | 219.35 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 91,500.00 USD | 0.00 USD | 107.40 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 91,390.00 USD | 0.00 USD | 29,530.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 61,860.00 USD | 0.00 USD | 3,340.00 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 58,520.00 USD | 0.00 USD | 620.38 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 57,900.00 USD | 0.00 USD | 13,500.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 44,400.00 USD | 0.00 USD | 136.20 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 44,260.00 USD | 0.00 USD | 667.86 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 43,600.00 USD | 0.00 USD | 275.50 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 43,320.00 USD | 0.00 USD | 553.00 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 42,770.00 USD | 0.00 USD | 326.34 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 42,440.00 USD | 0.00 USD | 5,040.00 USD | `-2.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 37,400.00 USD | 0.00 USD | 21,990.00 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 15,410.00 USD | 0.00 USD | 139.69 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 15,270.00 USD | 0.00 USD | 3,100.00 USD | `-1.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 12,170.00 USD | 0.00 USD | 2,940.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `283.50` | 9,230.00 USD | 0.00 USD | 8,040.00 USD | `-1.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `284.50` | 1,190.00 USD | 0.00 USD | 137.98 USD | `-0.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `285.50` | 1,050.00 USD | 0.00 USD | 1,050.00 USD | `-0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 280.77 USD | 280.77 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 7,190.00 USD | 6,910.00 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 7,450.00 USD | 261.96 USD | 0.00 USD | `+0.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 7,980.00 USD | 530.36 USD | 0.00 USD | `+1.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 8,190.00 USD | 212.36 USD | 0.00 USD | `+1.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 33,470.00 USD | 25,280.00 USD | 0.00 USD | `+1.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 33,640.00 USD | 167.89 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 34,630.00 USD | 992.62 USD | 0.00 USD | `+2.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 36,650.00 USD | 2,020.00 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 41,380.00 USD | 4,730.00 USD | 0.00 USD | `+3.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 41,490.00 USD | 110.37 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 41,880.00 USD | 388.95 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 42,030.00 USD | 153.94 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 52,810.00 USD | 10,780.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 57,910.00 USD | 5,110.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 68,640.00 USD | 10,730.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 71,290.00 USD | 2,650.00 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 71,570.00 USD | 282.89 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 86,070.00 USD | 14,500.00 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 86,700.00 USD | 634.04 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 87,740.00 USD | 1,030.00 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 93,390.00 USD | 5,650.00 USD | 0.00 USD | `+11.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 93,920.00 USD | 534.59 USD | 0.00 USD | `+11.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 94,240.00 USD | 321.50 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 160,960.00 USD | 66,720.00 USD | 0.00 USD | `+13.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 162,050.00 USD | 1,090.00 USD | 0.00 USD | `+16.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 174,050.00 USD | 12,000.00 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 174,590.00 USD | 547.52 USD | 0.00 USD | `+18.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 174,700.00 USD | 110.91 USD | 0.00 USD | `+20.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 174,960.00 USD | 257.45 USD | 0.00 USD | `+20.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 175,140.00 USD | 174.25 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 175,290.00 USD | 151.50 USD | 0.00 USD | `+22.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 176,740.00 USD | 1,450.00 USD | 0.00 USD | `+24.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 178,510.00 USD | 1,770.00 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 178,840.00 USD | 326.07 USD | 0.00 USD | `+26.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 179,670.00 USD | 826.60 USD | 0.00 USD | `+26.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 187,110.00 USD | 7,440.00 USD | 0.00 USD | `+27.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 187,790.00 USD | 682.84 USD | 0.00 USD | `+29.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 188,890.00 USD | 1,100.00 USD | 0.00 USD | `+33.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 189,580.00 USD | 683.96 USD | 0.00 USD | `+38.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 189,780.00 USD | 199.75 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 191,510.00 USD | 1,730.00 USD | 0.00 USD | `+39.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 192,550.00 USD | 1,040.00 USD | 0.00 USD | `+41.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 192,920.00 USD | 376.71 USD | 0.00 USD | `+41.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 193,080.00 USD | 158.86 USD | 0.00 USD | `+43.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 198,980.00 USD | 5,900.00 USD | 0.00 USD | `+45.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 200,060.00 USD | 1,080.00 USD | 0.00 USD | `+47.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 201,760.00 USD | 1,700.00 USD | 0.00 USD | `+48.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 203,320.00 USD | 1,550.00 USD | 0.00 USD | `+50.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 204,700.00 USD | 1,380.00 USD | 0.00 USD | `+52.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 205,320.00 USD | 621.14 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 207,600.00 USD | 2,280.00 USD | 0.00 USD | `+53.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 207,820.00 USD | 222.75 USD | 0.00 USD | `+55.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 214,740.00 USD | 6,920.00 USD | 0.00 USD | `+57.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 220,660.00 USD | 5,920.00 USD | 0.00 USD | `+57.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 221,790.00 USD | 1,130.00 USD | 0.00 USD | `+60.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 229,420.00 USD | 7,630.00 USD | 0.00 USD | `+68.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 230,400.00 USD | 975.00 USD | 0.00 USD | `+70.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 231,380.00 USD | 981.00 USD | 0.00 USD | `+71.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 231,880.00 USD | 499.50 USD | 0.00 USD | `+74.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,120,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+74.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,120,000.00 USD | 1,000.00 USD | 0.00 USD | `+75.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,120,000.00 USD | 1,040.00 USD | 0.00 USD | `+81.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,120,000.00 USD | 340.67 USD | 0.00 USD | `+82.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,120,000.00 USD | 638.86 USD | 0.00 USD | `+94.30%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `240.00` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 887.27 USD | 588.60 USD | 43.05 USD |
| `7D` | `240.40` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `240.80` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 1,270.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.20` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.60` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `242.00` | 10,910,000.00 USD | 0.00 USD | 10,910,000.00 USD | 27,990.00 USD | 11,260.00 USD | 21,510.00 USD |
| `7D` | `242.40` | 10,840,000.00 USD | 0.00 USD | 10,840,000.00 USD | 27,150.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `242.80` | 10,810,000.00 USD | 0.00 USD | 10,810,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.00 USD |
| `7D` | `243.20` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.60` | 10,790,000.00 USD | 0.00 USD | 10,790,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `244.00` | 10,750,000.00 USD | 0.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.40` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 0.00 USD | 0.00 USD | 6.53 USD |
| `7D` | `244.80` | 10,730,000.00 USD | 0.00 USD | 10,730,000.00 USD | 836.88 USD | 18,270.00 USD | 2,630.00 USD |
| `7D` | `245.20` | 10,710,000.00 USD | 0.00 USD | 10,710,000.00 USD | 599.05 USD | 15,350.00 USD | 1,640.00 USD |
| `7D` | `245.60` | 10,690,000.00 USD | 0.00 USD | 10,690,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,250.00 USD |
| `7D` | `246.00` | 10,670,000.00 USD | 0.00 USD | 10,670,000.00 USD | 11,860.00 USD | 8,060.00 USD | 0.00 USD |
| `7D` | `246.40` | 10,650,000.00 USD | 0.00 USD | 10,650,000.00 USD | 11,440.00 USD | 10,300.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 4,590.00 USD | 472.85 USD | 1,730.00 USD |
| `7D` | `247.20` | 10,620,000.00 USD | 0.00 USD | 10,620,000.00 USD | 14,580.00 USD | 17,320.00 USD | 2,690.00 USD |
| `7D` | `247.60` | 10,580,000.00 USD | 0.00 USD | 10,580,000.00 USD | 9,000.00 USD | 4,610.00 USD | 0.00 USD |
| `7D` | `248.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 555.60 USD | 310.87 USD | 2,780.00 USD |
| `7D` | `248.40` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 13,830.00 USD | 3,060.00 USD | 28,110.00 USD |
| `7D` | `248.80` | 10,520,000.00 USD | 0.00 USD | 10,520,000.00 USD | 28,270.00 USD | 15,790.00 USD | 28,710.00 USD |
| `7D` | `249.20` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 23,830.00 USD | 30,530.00 USD | 3,560.00 USD |
| `7D` | `249.60` | 10,390,000.00 USD | 0.00 USD | 10,390,000.00 USD | 46,340.00 USD | 35,710.00 USD | 16,330.00 USD |
| `7D` | `250.00` | 10,290,000.00 USD | 0.00 USD | 10,290,000.00 USD | 38,050.00 USD | 9,910.00 USD | 22,850.00 USD |
| `1D` | `250.40` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 9,190.00 USD | 6,150.00 USD | 12,280.00 USD |
| `7D` | `250.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 22,500.00 USD | 35,680.00 USD | 12,470.00 USD |
| `1D` | `250.80` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 9,730.00 USD | 14,160.00 USD | 10,300.00 USD |
| `7D` | `250.80` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 32,990.00 USD | 60,940.00 USD | 27,600.00 USD |
| `1D` | `251.20` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 25,370.00 USD | 23,980.00 USD | 16,990.00 USD |
| `7D` | `251.20` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 44,420.00 USD | 56,200.00 USD | 18,160.00 USD |
| `1D` | `251.60` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 26,820.00 USD | 47,060.00 USD | 19,210.00 USD |
| `7D` | `251.60` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 51,190.00 USD | 89,120.00 USD | 44,750.00 USD |
| `1D` | `252.00` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 16,340.00 USD | 11,100.00 USD | 16,180.00 USD |
| `7D` | `252.00` | 9,720,000.00 USD | 0.00 USD | 9,720,000.00 USD | 63,990.00 USD | 31,270.00 USD | 32,530.00 USD |
| `1D` | `252.40` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 6,700.00 USD | 1,540.00 USD | 2,530.00 USD |
| `7D` | `252.40` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 53,750.00 USD | 29,340.00 USD | 17,770.00 USD |
| `1D` | `252.80` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 6,800.00 USD | 2,270.00 USD | 4,830.00 USD |
| `7D` | `252.80` | 9,500,000.00 USD | 0.00 USD | 9,500,000.00 USD | 24,570.00 USD | 10,300.00 USD | 16.17 USD |
| `1D` | `253.20` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 8,060.00 USD | 3,900.00 USD | 821.20 USD |
| `7D` | `253.20` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 12,620.00 USD | 36,470.00 USD | 14,240.00 USD |
| `1D` | `253.60` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 20,500.00 USD | 17,790.00 USD | 21,440.00 USD |
| `7D` | `253.60` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 27,790.00 USD | 37,080.00 USD | 34,040.00 USD |
| `1D` | `254.00` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 5,800.00 USD | 8,100.00 USD | 9,690.00 USD |
| `7D` | `254.00` | 9,300,000.00 USD | 0.00 USD | 9,300,000.00 USD | 45,450.00 USD | 35,310.00 USD | 21,980.00 USD |
| `1D` | `254.40` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 8,310.00 USD | 13,680.00 USD | 3,970.00 USD |
| `7D` | `254.40` | 9,200,000.00 USD | 0.00 USD | 9,200,000.00 USD | 19,460.00 USD | 25,910.00 USD | 60,760.00 USD |
| `1D` | `254.80` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,210.00 USD | 3,080.00 USD | 1,480.00 USD |
| `7D` | `254.80` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 50,650.00 USD | 29,470.00 USD | 37,010.00 USD |
| `1D` | `255.20` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 16,750.00 USD | 17,660.00 USD | 12,890.00 USD |
| `7D` | `255.20` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 23,880.00 USD | 12,570.00 USD | 25,480.00 USD |
| `1D` | `255.60` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 17,490.00 USD | 32,020.00 USD | 23,780.00 USD |
| `7D` | `255.60` | 8,910,000.00 USD | 0.00 USD | 8,910,000.00 USD | 33,430.00 USD | 17,110.00 USD | 31,090.00 USD |
| `1D` | `256.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 10,010.00 USD | 11,710.00 USD | 15,530.00 USD |
| `7D` | `256.00` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 18,300.00 USD | 16,500.00 USD | 25,350.00 USD |
| `1D` | `256.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,460.00 USD | 31,910.00 USD | 19,770.00 USD |
| `7D` | `256.40` | 8,770,000.00 USD | 0.00 USD | 8,770,000.00 USD | 29,190.00 USD | 739.13 USD | 23,240.00 USD |
| `1D` | `256.80` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 1,820.00 USD | 5,950.00 USD | 14,920.00 USD |
| `7D` | `256.80` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 32,310.00 USD | 13,750.00 USD | 56,600.00 USD |
| `1D` | `257.20` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 14,160.00 USD | 3,660.00 USD | 7,340.00 USD |
| `7D` | `257.20` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 15,600.00 USD | 10,170.00 USD | 11,110.00 USD |
| `1D` | `257.60` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD |
| `7D` | `257.60` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 34,480.00 USD | 4,400.00 USD | 10,340.00 USD |
| `1D` | `258.00` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD |
| `7D` | `258.00` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 26,960.00 USD | 4,790.00 USD | 8,030.00 USD |
| `1D` | `258.40` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD |
| `7D` | `258.40` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 128,170.00 USD | 37,820.00 USD | 92,400.00 USD |
| `1D` | `258.80` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 8,320.00 USD | 30,390.00 USD | 40,000.00 USD |
| `7D` | `258.80` | 8,230,000.00 USD | 0.00 USD | 8,230,000.00 USD | 59,230.00 USD | 2,500.00 USD | 34,380.00 USD |
| `1D` | `259.20` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 14,560.00 USD | 12,990.00 USD | 17,630.00 USD |
| `7D` | `259.20` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 5,210.00 USD | 45,200.00 USD | 8,030.00 USD |
| `1D` | `259.60` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 13,590.00 USD | 4,640.00 USD | 22,250.00 USD |
| `7D` | `259.60` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 20,030.00 USD | 8,340.00 USD | 17,090.00 USD |
| `1D` | `260.00` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 45,280.00 USD | 32,840.00 USD | 23,920.00 USD |
| `7D` | `260.00` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 103,390.00 USD | 63,410.00 USD | 106,070.00 USD |
| `1D` | `260.40` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 19,610.00 USD | 7,660.00 USD | 16,020.00 USD |
| `7D` | `260.40` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 4,590.00 USD | 3,590.00 USD | 74,360.00 USD |
| `1D` | `260.80` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 1,360.00 USD | 46,690.00 USD | 25,130.00 USD |
| `7D` | `260.80` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 14,600.00 USD | 56,470.00 USD | 37,850.00 USD |
| `1D` | `261.20` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 8,180.00 USD | 23,140.00 USD | 30,850.00 USD |
| `7D` | `261.20` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 6,110.00 USD | 90,180.00 USD | 16,000.00 USD |
| `1D` | `261.60` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 18,900.00 USD | 55,190.00 USD | 53,770.00 USD |
| `7D` | `261.60` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 24,520.00 USD | 84,260.00 USD | 48,530.00 USD |
| `1D` | `262.00` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 17,910.00 USD | 44,250.00 USD | 21,380.00 USD |
| `7D` | `262.00` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 61,230.00 USD | 39,230.00 USD | 81,290.00 USD |
| `1D` | `262.40` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 21,110.00 USD | 6,200.00 USD | 10,850.00 USD |
| `7D` | `262.40` | 7,110,000.00 USD | 0.00 USD | 7,110,000.00 USD | 28,440.00 USD | 55,580.00 USD | 40.11 USD |
| `1D` | `262.80` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 747.53 USD | 13,250.00 USD | 19,480.00 USD |
| `7D` | `262.80` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 73,660.00 USD | 45,060.00 USD | 32,750.00 USD |
| `1D` | `263.20` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,470.00 USD |
| `7D` | `263.20` | 6,880,000.00 USD | 0.00 USD | 6,880,000.00 USD | 21,560.00 USD | 13,710.00 USD | 104.44 USD |
| `1D` | `263.60` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,410.00 USD |
| `7D` | `263.60` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 278,330.00 USD | 1,880.00 USD | 83,060.00 USD |
| `1D` | `264.00` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 52,440.00 USD | 15,650.00 USD | 17,280.00 USD |
| `7D` | `264.00` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 135,390.00 USD | 629.16 USD | 34,890.00 USD |
| `1D` | `264.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 6,130.00 USD | 20,240.00 USD | 21.88 USD |
| `7D` | `264.40` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 44,740.00 USD | 21,130.00 USD | 97.64 USD |
| `1D` | `264.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 22,660.00 USD | 1,670.00 USD | 20,040.00 USD |
| `7D` | `264.80` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 26,950.00 USD | 2,610.00 USD | 157.56 USD |
| `1D` | `265.20` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 75,930.00 USD | 3,490.00 USD | 33,270.00 USD |
| `7D` | `265.20` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 106,380.00 USD | 1,640.00 USD | 33,790.00 USD |
| `1D` | `265.60` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 415.98 USD | 788.61 USD | 12.92 USD |
| `7D` | `265.60` | 6,070,000.00 USD | 0.00 USD | 6,070,000.00 USD | 199,660.00 USD | 694.90 USD | 8.70 USD |
| `1D` | `266.00` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 12,200.00 USD | 209.24 USD | 5.24 USD |
| `7D` | `266.00` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 140,360.00 USD | 645.20 USD | 72.90 USD |
| `1D` | `266.40` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 4,400.00 USD | 13,530.00 USD | 4,800.00 USD |
| `7D` | `266.40` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 106,830.00 USD | 804.70 USD | 226.57 USD |
| `1D` | `266.80` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 22,750.00 USD | 30,970.00 USD | 0.00 USD |
| `7D` | `266.80` | 5,620,000.00 USD | 0.00 USD | 5,620,000.00 USD | 125,320.00 USD | 63,260.00 USD | 7.04 USD |
| `1D` | `267.20` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 43,580.00 USD | 34,990.00 USD | 12,550.00 USD |
| `7D` | `267.20` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 101,740.00 USD | 26,850.00 USD | 201.76 USD |
| `1D` | `267.60` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 10,330.00 USD | 72,630.00 USD | 23,000.00 USD |
| `7D` | `267.60` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 75,350.00 USD | 61,270.00 USD | 38,610.00 USD |
| `1D` | `268.00` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 19,060.00 USD | 4,020.00 USD | 51,860.00 USD |
| `7D` | `268.00` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 234,660.00 USD | 25,100.00 USD | 184.22 USD |
| `1D` | `268.40` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 18,310.00 USD | 43,230.00 USD | 13,970.00 USD |
| `7D` | `268.40` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 136,830.00 USD | 124,980.00 USD | 95,640.00 USD |
| `1D` | `268.80` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 21,330.00 USD | 11,530.00 USD | 146.66 USD |
| `7D` | `268.80` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 23,340.00 USD | 18,320.00 USD | 241.40 USD |
| `1D` | `269.20` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 10,990.00 USD | 2,810.00 USD | 8,340.00 USD |
| `7D` | `269.20` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 1,560.00 USD | 260.32 USD |
| `1D` | `269.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,520.00 USD | 19,580.00 USD | 10,340.00 USD |
| `7D` | `269.60` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 0.00 USD | 3,480.00 USD | 153.87 USD |
| `1D` | `270.00` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 7,960.00 USD | 12,030.00 USD | 3,380.00 USD |
| `7D` | `270.00` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 1,310.00 USD | 64.60 USD |
| `1D` | `270.40` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 54,750.00 USD | 1,930.00 USD | 3,540.00 USD |
| `7D` | `270.40` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 27.41 USD |
| `1D` | `270.80` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 3,210.00 USD | 15,660.00 USD | 4,930.00 USD |
| `7D` | `270.80` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 33,050.00 USD | 0.00 USD | 6.87 USD |
| `1D` | `271.20` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 12,890.00 USD | 6,410.00 USD | 12,590.00 USD |
| `7D` | `271.20` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.60` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 8,940.00 USD | 13,270.00 USD |
| `7D` | `271.60` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 0.00 USD | 7,250.00 USD | 61,070.00 USD |
| `1D` | `272.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 28,410.00 USD | 52,240.00 USD | 9,610.00 USD |
| `7D` | `272.00` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 61,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.40` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 10,530.00 USD | 35,390.00 USD | 57,740.00 USD |
| `7D` | `272.40` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.80` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 62,230.00 USD | 15,740.00 USD | 68,920.00 USD |
| `7D` | `272.80` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `273.20` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 32,520.00 USD | 117,860.00 USD | 43,510.00 USD |
| `7D` | `273.20` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 0.00 USD | 95,060.00 USD | 185,600.00 USD |
| `1D` | `273.60` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 42,760.00 USD | 18,430.00 USD | 53,420.00 USD |
| `7D` | `273.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 66,850.00 USD |
| `1D` | `274.00` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 159,390.00 USD | 97,110.00 USD | 39,870.00 USD |
| `7D` | `274.00` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 466,260.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.40` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 155,650.00 USD | 27,970.00 USD | 41,320.00 USD |
| `7D` | `274.40` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 413,010.00 USD | 51,840.00 USD | 83,040.00 USD |
| `1D` | `274.80` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 70,330.00 USD | 22,510.00 USD | 29,260.00 USD |
| `7D` | `274.80` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 334,980.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `275.20` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 11,720.00 USD | 3,760.00 USD | 0.00 USD |
| `7D` | `275.20` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.60` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 35,420.00 USD | 15,980.00 USD | 26,710.00 USD |
| `7D` | `275.60` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 1,350.00 USD | 0.00 USD | 48,580.00 USD |
| `1D` | `276.00` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 143,900.00 USD | 18,930.00 USD | 40,360.00 USD |
| `7D` | `276.00` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 3,140.00 USD | 23,010.00 USD | 33,750.00 USD |
| `1D` | `276.40` | 973,410.00 USD | 0.00 USD | 973,410.00 USD | 40,580.00 USD | 16,150.00 USD | 18,670.00 USD |
| `7D` | `276.40` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 217,250.00 USD | 0.00 USD | 103,940.00 USD |
| `1D` | `276.80` | 898,010.00 USD | 0.00 USD | 898,010.00 USD | 11,880.00 USD | 25,410.00 USD | 25,170.00 USD |
| `7D` | `276.80` | 1,740,000.00 USD | 0.00 USD | 1,740,000.00 USD | 16,100.00 USD | 0.00 USD | 79.76 USD |
| `1D` | `277.20` | 835,550.00 USD | 0.00 USD | 835,550.00 USD | 25,720.00 USD | 17,880.00 USD | 26,540.00 USD |
| `7D` | `277.20` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 28,580.00 USD | 42,210.00 USD | 163,820.00 USD |
| `1D` | `277.60` | 765,410.00 USD | 0.00 USD | 765,410.00 USD | 26,620.00 USD | 21,090.00 USD | 0.00 USD |
| `7D` | `277.60` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 123,610.00 USD | 193,330.00 USD | 18,280.00 USD |
| `1D` | `278.00` | 717,700.00 USD | 0.00 USD | 717,700.00 USD | 21,070.00 USD | 54,860.00 USD | 103,960.00 USD |
| `7D` | `278.00` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 1,830.00 USD | 59,930.00 USD |
| `1D` | `278.40` | 537,810.00 USD | 0.00 USD | 537,810.00 USD | 57,720.00 USD | 125,180.00 USD | 77,350.00 USD |
| `7D` | `278.40` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 76,060.00 USD | 35,270.00 USD | 155,310.00 USD |
| `1D` | `278.80` | 277,570.00 USD | 0.00 USD | 277,570.00 USD | 55,370.00 USD | 10,830.00 USD | 0.00 USD |
| `7D` | `278.80` | 824,280.00 USD | 0.00 USD | 824,280.00 USD | 0.00 USD | 49,750.00 USD | 23,990.00 USD |
| `1D` | `279.20` | 211,370.00 USD | 0.00 USD | 211,370.00 USD | 4,440.00 USD | 3,800.00 USD | 23,400.00 USD |
| `7D` | `279.20` | 750,540.00 USD | 0.00 USD | 750,540.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.60` | 179,730.00 USD | 0.00 USD | 179,730.00 USD | 0.00 USD | 0.00 USD | 47,450.00 USD |
| `7D` | `279.60` | 747,880.00 USD | 0.00 USD | 747,880.00 USD | 0.00 USD | 0.00 USD | 154.63 USD |
| `1D` | `280.00` | 132,270.00 USD | 0.00 USD | 132,270.00 USD | 0.00 USD | 13,070.00 USD | 31,340.00 USD |
| `7D` | `280.00` | 747,720.00 USD | 0.00 USD | 747,720.00 USD | 0.00 USD | 33,750.00 USD | 0.00 USD |
| `1D` | `280.80` | 87,860.00 USD | 0.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 12.68 USD |
| `7D` | `280.80` | 713,980.00 USD | 0.00 USD | 713,980.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `7D` | `281.20` | 698,440.00 USD | 0.00 USD | 698,440.00 USD | 0.00 USD | 14,140.00 USD | 79,700.00 USD |
| `7D` | `281.60` | 604,590.00 USD | 0.00 USD | 604,590.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `7D` | `282.00` | 482,210.00 USD | 0.00 USD | 482,210.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.40` | 87,850.00 USD | 0.00 USD | 87,850.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.40` | 461,500.00 USD | 0.00 USD | 461,500.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.20` | 79,590.00 USD | 0.00 USD | 79,590.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.20` | 457,980.00 USD | 0.00 USD | 457,980.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.60` | 454,530.00 USD | 0.00 USD | 454,530.00 USD | 0.00 USD | 0.00 USD | 1.92 USD |
| `7D` | `284.00` | 454,530.00 USD | 0.00 USD | 454,530.00 USD | 2,000.00 USD | 0.00 USD | 55.52 USD |
| `7D` | `284.40` | 452,480.00 USD | 0.00 USD | 452,480.00 USD | 1,560.00 USD | 0.00 USD | 16.87 USD |
| `7D` | `284.80` | 450,900.00 USD | 0.00 USD | 450,900.00 USD | 0.00 USD | 0.00 USD | 132.86 USD |
| `1D` | `285.20` | 78,310.00 USD | 0.00 USD | 78,310.00 USD | 36,620.00 USD | 0.00 USD | 41,690.00 USD |
| `7D` | `285.20` | 450,770.00 USD | 0.00 USD | 450,770.00 USD | 126,910.00 USD | 206,630.00 USD | 65,820.00 USD |
| `1D` | `285.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `285.60` | 27,570.00 USD | 27,570.00 USD | 0.00 USD | 27,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `285.60` | 51,410.00 USD | 0.00 USD | 51,410.00 USD | 50,130.00 USD | 1,280.00 USD | 7.35 USD |
| `7D` | `285.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `286.00` | 99,520.00 USD | 99,520.00 USD | 0.00 USD | 29,220.00 USD | 2,980.00 USD | 39,750.00 USD |
| `7D` | `286.00` | 3,770.00 USD | 3,770.00 USD | 0.00 USD | 1,200.00 USD | 2,560.00 USD | 14.26 USD |
| `1D` | `286.40` | 121,480.00 USD | 121,480.00 USD | 0.00 USD | 17,340.00 USD | 4,610.00 USD | 4.24 USD |
| `7D` | `286.40` | 141,230.00 USD | 141,230.00 USD | 0.00 USD | 0.00 USD | 137,440.00 USD | 11.42 USD |
| `1D` | `286.80` | 228,380.00 USD | 228,380.00 USD | 0.00 USD | 18,110.00 USD | 10,660.00 USD | 78,130.00 USD |
| `7D` | `286.80` | 293,370.00 USD | 293,370.00 USD | 0.00 USD | 30,110.00 USD | 122,000.00 USD | 31.50 USD |
| `1D` | `287.20` | 427,500.00 USD | 427,500.00 USD | 0.00 USD | 112,240.00 USD | 47,050.00 USD | 39,830.00 USD |
| `7D` | `287.20` | 492,710.00 USD | 492,710.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 0.00 USD |
| `1D` | `287.60` | 576,390.00 USD | 576,390.00 USD | 0.00 USD | 47,390.00 USD | 34,850.00 USD | 66,650.00 USD |
| `7D` | `287.60` | 650,070.00 USD | 650,070.00 USD | 0.00 USD | 70,340.00 USD | 33,740.00 USD | 53,280.00 USD |
| `1D` | `288.00` | 676,230.00 USD | 676,230.00 USD | 0.00 USD | 9,440.00 USD | 26,480.00 USD | 63,920.00 USD |
| `7D` | `288.00` | 922,380.00 USD | 922,380.00 USD | 0.00 USD | 0.00 USD | 272,310.00 USD | 0.00 USD |
| `1D` | `288.40` | 795,940.00 USD | 795,940.00 USD | 0.00 USD | 68,380.00 USD | 22,110.00 USD | 29,220.00 USD |
| `7D` | `288.40` | 965,620.00 USD | 965,620.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD | 41,690.00 USD |
| `1D` | `288.80` | 879,250.00 USD | 879,250.00 USD | 0.00 USD | 43,690.00 USD | 32,420.00 USD | 7,210.00 USD |
| `7D` | `288.80` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 122,130.00 USD |
| `1D` | `289.20` | 968,510.00 USD | 968,510.00 USD | 0.00 USD | 6,160.00 USD | 52,920.00 USD | 30,180.00 USD |
| `7D` | `289.20` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.60` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 25,200.00 USD | 66,520.00 USD | 121,890.00 USD |
| `7D` | `289.60` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 62,370.00 USD | 95,470.00 USD |
| `1D` | `290.00` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 115,670.00 USD | 66,820.00 USD | 124,250.00 USD |
| `7D` | `290.00` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 53,890.00 USD | 69,350.00 USD | 122,380.00 USD |
| `1D` | `290.40` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 40,570.00 USD | 111,760.00 USD | 49,240.00 USD |
| `7D` | `290.40` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 33,530.00 USD | 19,060.00 USD | 25.60 USD |
| `1D` | `290.80` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 56,480.00 USD | 71,550.00 USD | 54,940.00 USD |
| `7D` | `290.80` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,960.00 USD |
| `1D` | `291.20` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 28,320.00 USD | 25,130.00 USD | 24,320.00 USD |
| `7D` | `291.20` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 24,680.00 USD | 52,140.00 USD | 49.23 USD |
| `1D` | `291.60` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 12,550.00 USD | 6,560.00 USD | 30,420.00 USD |
| `7D` | `291.60` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 2,710.00 USD | 85,290.00 USD | 19,470.00 USD |
| `1D` | `292.00` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 7,010.00 USD | 30,490.00 USD | 31.89 USD |
| `7D` | `292.00` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 2,560.00 USD | 149,160.00 USD | 113.70 USD |
| `1D` | `292.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 29,860.00 USD | 14,820.00 USD | 13,730.00 USD |
| `7D` | `292.40` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 25,520.00 USD | 121.87 USD |
| `1D` | `292.80` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 29,430.00 USD | 27,590.00 USD | 3,560.00 USD |
| `7D` | `292.80` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 43.08 USD |
| `1D` | `293.20` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 50,900.00 USD | 12,760.00 USD | 32,300.00 USD |
| `7D` | `293.20` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 33,580.00 USD | 132,080.00 USD | 8.63 USD |
| `1D` | `293.60` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 77,380.00 USD | 48,560.00 USD | 20,970.00 USD |
| `7D` | `293.60` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 0.00 USD | 1,860.00 USD | 12.54 USD |
| `1D` | `294.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 30,750.00 USD | 23,790.00 USD | 70,500.00 USD |
| `7D` | `294.00` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 54,350.00 USD | 34,230.00 USD | 95,150.00 USD |
| `1D` | `294.40` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 64,400.00 USD | 64,490.00 USD | 116,730.00 USD |
| `7D` | `294.40` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 201,580.00 USD | 9,460.00 USD | 92,520.00 USD |
| `1D` | `294.80` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 59,910.00 USD | 35,750.00 USD | 44,460.00 USD |
| `7D` | `294.80` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 63,770.00 USD | 108,720.00 USD | 89,160.00 USD |
| `1D` | `295.20` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 8,650.00 USD | 28,960.00 USD | 99,830.00 USD |
| `7D` | `295.20` | 3,530,000.00 USD | 3,530,000.00 USD | 0.00 USD | 733.30 USD | 64,810.00 USD | 214,280.00 USD |
| `1D` | `295.60` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 73,320.00 USD | 48,980.00 USD | 132,630.00 USD |
| `7D` | `295.60` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 176,660.00 USD | 91,360.00 USD | 294,410.00 USD |
| `1D` | `296.00` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 56,610.00 USD | 114,680.00 USD | 43,670.00 USD |
| `7D` | `296.00` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 76,740.00 USD | 114,600.00 USD | 98,690.00 USD |
| `1D` | `296.40` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 80,090.00 USD | 31,130.00 USD | 27,120.00 USD |
| `7D` | `296.40` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 1,550.00 USD | 78,210.00 USD | 68,330.00 USD |
| `1D` | `296.80` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 24,560.00 USD | 32,150.00 USD | 74,510.00 USD |
| `7D` | `296.80` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 133,480.00 USD | 4,410.00 USD | 201,550.00 USD |
| `1D` | `297.20` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 56,450.00 USD | 7,700.00 USD | 50,330.00 USD |
| `7D` | `297.20` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 77,480.00 USD | 68,680.00 USD | 85.47 USD |
| `1D` | `297.60` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 7,640.00 USD | 11,760.00 USD | 29,800.00 USD |
| `7D` | `297.60` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 1,640.00 USD | 61,200.00 USD | 34,690.00 USD |
| `1D` | `298.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 63,620.00 USD | 9,890.00 USD | 41,720.00 USD |
| `7D` | `298.00` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 47,790.00 USD | 44,920.00 USD | 75,650.00 USD |
| `1D` | `298.40` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 7,430.00 USD | 2,280.00 USD | 56,410.00 USD |
| `7D` | `298.40` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 32,250.00 USD | 42,940.00 USD | 47,980.00 USD |
| `1D` | `298.80` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 23,700.00 USD | 457.80 USD | 94,680.00 USD |
| `7D` | `298.80` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 48.95 USD |
| `1D` | `299.20` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 8,500.00 USD | 15,770.00 USD | 12,340.00 USD |
| `7D` | `299.20` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 2,350.00 USD | 15,140.00 USD | 85,860.00 USD |
| `1D` | `299.60` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 36,030.00 USD | 5,850.00 USD | 21,870.00 USD |
| `7D` | `299.60` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 4,590.00 USD | 13,830.00 USD | 19,840.00 USD |
| `1D` | `300.00` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 3,760.00 USD | 14,300.00 USD | 27,500.00 USD |
| `7D` | `300.00` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 53,130.00 USD | 10,090.00 USD | 13.78 USD |
| `1D` | `300.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 41,880.00 USD | 31,000.00 USD | 42,620.00 USD |
| `7D` | `300.40` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 2,070.00 USD | 645.96 USD | 6.37 USD |
| `1D` | `300.80` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 790.57 USD | 879.82 USD | 17,320.00 USD |
| `7D` | `300.80` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 24,730.00 USD | 71,120.00 USD | 48,510.00 USD |
| `1D` | `301.20` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 348.65 USD | 15,610.00 USD | 30,860.00 USD |
| `7D` | `301.20` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 48,570.00 USD | 42,080.00 USD | 91,040.00 USD |
| `1D` | `301.60` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 19,530.00 USD | 8,470.00 USD | 34,890.00 USD |
| `7D` | `301.60` | 6,220,000.00 USD | 6,220,000.00 USD | 0.00 USD | 62,390.00 USD | 79,410.00 USD | 59,530.00 USD |
| `1D` | `302.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 25,220.00 USD | 28,210.00 USD | 10,420.00 USD |
| `7D` | `302.00` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 52,640.00 USD | 150,800.00 USD | 26,310.00 USD |
| `1D` | `302.40` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,420.00 USD | 5,200.00 USD | 17,560.00 USD |
| `7D` | `302.40` | 6,550,000.00 USD | 6,550,000.00 USD | 0.00 USD | 580.96 USD | 99,100.00 USD | 115.12 USD |
| `1D` | `302.80` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 4,420.00 USD | 13,290.00 USD | 34,920.00 USD |
| `7D` | `302.80` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 71,700.00 USD | 112,610.00 USD | 41,710.00 USD |
| `1D` | `303.20` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 21,180.00 USD | 1,390.00 USD | 9,360.00 USD |
| `7D` | `303.20` | 6,780,000.00 USD | 6,780,000.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD | 21.84 USD |
| `1D` | `303.60` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 228.18 USD | 2,000.00 USD | 1.44 USD |
| `7D` | `303.60` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 2,130.00 USD | 693.54 USD | 24,660.00 USD |
| `1D` | `304.00` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD |
| `7D` | `304.00` | 6,860,000.00 USD | 6,860,000.00 USD | 0.00 USD | 20,680.00 USD | 14,630.00 USD | 21,330.00 USD |
| `1D` | `304.40` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 9,750.00 USD | 2,470.00 USD | 49,830.00 USD |
| `7D` | `304.40` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 1,340.00 USD | 11,280.00 USD | 58.87 USD |
| `1D` | `304.80` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD |
| `7D` | `304.80` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 34,540.00 USD | 682.27 USD | 3,990.00 USD |
| `1D` | `305.20` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 47.98 USD | 5,330.00 USD | 2,030.00 USD |
| `7D` | `305.20` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 113,060.00 USD | 128,470.00 USD | 89,540.00 USD |
| `1D` | `305.60` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 3,060.00 USD | 440.72 USD | 12.59 USD |
| `7D` | `305.60` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 76,400.00 USD | 21,950.00 USD | 41,200.00 USD |
| `1D` | `306.00` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 7,500.00 USD | 5,780.00 USD | 12,230.00 USD |
| `7D` | `306.00` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 60,790.00 USD | 50,650.00 USD | 44,620.00 USD |
| `1D` | `306.40` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 7,310.00 USD | 183.24 USD | 5,670.00 USD |
| `7D` | `306.40` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 35,090.00 USD | 65,940.00 USD | 25,640.00 USD |
| `1D` | `306.80` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 19,990.00 USD | 35,330.00 USD | 11,000.00 USD |
| `7D` | `306.80` | 7,890,000.00 USD | 7,890,000.00 USD | 0.00 USD | 84,850.00 USD | 66,200.00 USD | 66,910.00 USD |
| `1D` | `307.20` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 11,270.00 USD | 19,960.00 USD | 29,820.00 USD |
| `7D` | `307.20` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 11,730.00 USD | 87,980.00 USD | 106,510.00 USD |
| `1D` | `307.60` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 22,580.00 USD | 27,240.00 USD | 5.95 USD |
| `7D` | `307.60` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 78,600.00 USD | 122,070.00 USD | 56,180.00 USD |
| `1D` | `308.00` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 16,340.00 USD | 10,700.00 USD | 16,150.00 USD |
| `7D` | `308.00` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 125,470.00 USD | 70,950.00 USD | 60,800.00 USD |
| `1D` | `308.40` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 3,150.00 USD | 212.94 USD | 2,510.00 USD |
| `7D` | `308.40` | 8,900,000.00 USD | 8,900,000.00 USD | 0.00 USD | 131,420.00 USD | 45,250.00 USD | 114,690.00 USD |
| `1D` | `308.80` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD |
| `7D` | `308.80` | 9,010,000.00 USD | 9,010,000.00 USD | 0.00 USD | 54,880.00 USD | 42,230.00 USD | 19,720.00 USD |
| `1D` | `309.20` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 2,990.00 USD | 1,190.00 USD | 2,150.00 USD |
| `7D` | `309.20` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 33,440.00 USD | 19,290.00 USD | 32,260.00 USD |
| `1D` | `309.60` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 8,250.00 USD | 8,700.00 USD | 1,420.00 USD |
| `7D` | `309.60` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 41,230.00 USD | 107,950.00 USD | 130,960.00 USD |
| `1D` | `310.00` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 15,210.00 USD | 1,250.00 USD | 7,300.00 USD |
| `7D` | `310.00` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 20,240.00 USD | 98,540.00 USD | 82,900.00 USD |
| `1D` | `310.40` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 176.40 USD | 5,960.00 USD | 9,660.00 USD |
| `7D` | `310.40` | 9,770,000.00 USD | 9,770,000.00 USD | 0.00 USD | 91,290.00 USD | 74,340.00 USD | 21,980.00 USD |
| `1D` | `310.80` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 5,080.00 USD | 2,080.00 USD | 3,950.00 USD |
| `7D` | `310.80` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 29,950.00 USD | 35,930.00 USD | 12,160.00 USD |
| `1D` | `311.20` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 257.90 USD | 3,180.00 USD | 1,480.00 USD |
| `7D` | `311.20` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 74,340.00 USD | 65,480.00 USD | 72,020.00 USD |
| `1D` | `311.60` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 7,100.00 USD | 10,150.00 USD | 14.73 USD |
| `7D` | `311.60` | 10,120,000.00 USD | 10,120,000.00 USD | 0.00 USD | 40,900.00 USD | 10,550.00 USD | 5,710.00 USD |
| `1D` | `312.00` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 1,190.00 USD | 4,770.00 USD | 4,070.00 USD |
| `7D` | `312.00` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 40,590.00 USD | 1,560.00 USD | 28,210.00 USD |
| `1D` | `312.40` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 17,490.00 USD | 16,020.00 USD | 23,760.00 USD |
| `7D` | `312.40` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 28,530.00 USD | 23,430.00 USD | 31,090.00 USD |
| `1D` | `312.80` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 9,120.00 USD | 2,930.00 USD | 15,530.00 USD |
| `7D` | `312.80` | 10,300,000.00 USD | 10,300,000.00 USD | 0.00 USD | 15,280.00 USD | 8,600.00 USD | 7,070.00 USD |
| `1D` | `313.20` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 40.35 USD | 15,380.00 USD | 3,670.00 USD |
| `7D` | `313.20` | 10,380,000.00 USD | 10,380,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,380.00 USD |
| `1D` | `313.60` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 8,180.00 USD | 7,190.00 USD | 8,220.00 USD |
| `7D` | `313.60` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 10,400.00 USD | 755.05 USD | 34,710.00 USD |
| `1D` | `314.00` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD |
| `7D` | `314.00` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 22,920.00 USD | 815.59 USD | 20,580.00 USD |
| `1D` | `314.40` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 4,210.00 USD | 2,610.00 USD | 7,320.00 USD |
| `7D` | `314.40` | 10,550,000.00 USD | 10,550,000.00 USD | 0.00 USD | 51,980.00 USD | 7,060.00 USD | 24,520.00 USD |
| `1D` | `314.80` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 32.00 USD | 3,660.00 USD | 9,250.00 USD |
| `7D` | `314.80` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 17,720.00 USD | 0.00 USD | 10,450.00 USD |
| `1D` | `315.10` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 1,620.00 USD |
| `7D` | `315.20` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 0.00 USD | 258.00 USD | 42.63 USD |
| `7D` | `315.60` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 1,070.00 USD | 28,580.00 USD | 29,930.00 USD |
| `7D` | `316.00` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 38,990.00 USD | 5,120.00 USD | 46.30 USD |
| `7D` | `316.40` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 16,580.00 USD | 40,060.00 USD | 61,760.00 USD |
| `7D` | `316.80` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 1,990.00 USD | 667.80 USD | 110.33 USD |
| `7D` | `317.20` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 114.13 USD |
| `7D` | `317.60` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 0.00 USD | 265.17 USD | 0.00 USD |
| `7D` | `317.80` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 20,490.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.74M` | Total OI Tokens: `1,077,832.8 BCH`
  * 1h OI Change: `+1.50%` | 4h OI Change: `+0.40%` | 24h OI Change: `-0.24%`
  * Exchange Breakdown: Binance=`89.23M` | Bybit=`38.32M` | OKX=`24.13M` | Hyperliquid=`7.32M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.96K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0093%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `51.14%` | `48.86%` | `1.05` | 4,400,000.00 USD |
| `15M` | `Binance` | `38.46%` | `61.54%` | `0.62` | 1,720,000.00 USD |
| `15M` | `OKX` | `29.27%` | `70.73%` | `0.41` | 533,090.00 USD |
| `15M` | `Bybit` | `42.42%` | `57.58%` | `0.74` | 187,570.00 USD |
| `15M` | `KuCoin` | `54.95%` | `45.05%` | `1.22` | 14,060.00 USD |
| `15M` | `Gate` | `69.52%` | `30.48%` | `2.28` | 298,990.00 USD |
| `15M` | `Bitget` | `82.23%` | `17.77%` | `4.63` | 280,060.00 USD |
| `15M` | `BingX` | `54.09%` | `45.91%` | `1.18` | 461,960.00 USD |
| `15M` | `MEXC` | `16.9%` | `83.1%` | `0.20` | 77,570.00 USD |
| `15M` | `Bitunix` | `48.42%` | `51.58%` | `0.94` | 62,890.00 USD |
| `15M` | `Hyperliquid` | `81.11%` | `18.89%` | `4.29` | 4,570.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.22%` | `49.78%` | `1.01` | 198,660.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `95.09%` | `4.91%` | `19.37` | 526,490.00 USD |
| `15M` | `HTX` | `88.65%` | `11.35%` | `7.81` | 9,860.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `26.5%` | `73.5%` | `0.36` | 17,200.00 USD |
| `15M` | `Aster` | `1.14%` | `98.86%` | `0.01` | 8,460.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `6.9%` | `93.1%` | `0.07` | 7,830.00 USD |
| `15M` | `Whale Positions` | `38.46%` | `61.54%` | `0.62` | 1,720,000.00 USD |
| `15M` | `Global Accounts` | `51.14%` | `48.86%` | `1.05` | 4,400,000.00 USD |
| `1H` | `BCH` | `49.47%` | `50.53%` | `0.98` | 16,460,000.00 USD |
| `1H` | `Binance` | `42.28%` | `57.72%` | `0.73` | 5,480,000.00 USD |
| `1H` | `OKX` | `40.31%` | `59.69%` | `0.68` | 1,710,000.00 USD |
| `1H` | `Bybit` | `41.34%` | `58.66%` | `0.70` | 1,430,000.00 USD |
| `1H` | `KuCoin` | `53.51%` | `46.49%` | `1.15` | 82,710.00 USD |
| `1H` | `Gate` | `54.45%` | `45.55%` | `1.20` | 1,170,000.00 USD |
| `1H` | `Bitget` | `65.05%` | `34.95%` | `1.86` | 602,560.00 USD |
| `1H` | `BingX` | `35.57%` | `64.43%` | `0.55` | 2,780,000.00 USD |
| `1H` | `MEXC` | `30.43%` | `69.57%` | `0.44` | 355,140.00 USD |
| `1H` | `Bitunix` | `66.28%` | `33.72%` | `1.97` | 299,370.00 USD |
| `1H` | `Hyperliquid` | `55.7%` | `44.3%` | `1.26` | 39,800.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.15%` | `49.85%` | `1.01` | 371,340.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.52%` | `2.48%` | `39.32` | 1,850,000.00 USD |
| `1H` | `HTX` | `54.72%` | `45.28%` | `1.21` | 52,610.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `68.23%` | `31.77%` | `2.15` | 191,160.00 USD |
| `1H` | `Aster` | `36.61%` | `63.39%` | `0.58` | 20,240.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `10.51%` | `89.49%` | `0.12` | 33,200.00 USD |
| `1H` | `Whale Positions` | `42.28%` | `57.72%` | `0.73` | 5,480,000.00 USD |
| `1H` | `Global Accounts` | `49.47%` | `50.53%` | `0.98` | 16,460,000.00 USD |
| `4H` | `BCH` | `44.51%` | `55.49%` | `0.80` | 54,290,000.00 USD |
| `4H` | `Binance` | `51%` | `49%` | `1.04` | 18,470,000.00 USD |
| `4H` | `OKX` | `54.1%` | `45.9%` | `1.18` | 9,050,000.00 USD |
| `4H` | `Bybit` | `47.32%` | `52.68%` | `0.90` | 4,100,000.00 USD |
| `4H` | `KuCoin` | `49.58%` | `50.42%` | `0.98` | 2,280,000.00 USD |
| `4H` | `Gate` | `54.33%` | `45.67%` | `1.19` | 1,100,000.00 USD |
| `4H` | `Bitget` | `46.14%` | `53.86%` | `0.86` | 1,200,000.00 USD |
| `4H` | `BingX` | `8.99%` | `91.01%` | `0.10` | 3,630,000.00 USD |
| `4H` | `MEXC` | `52.54%` | `47.46%` | `1.11` | 705,860.00 USD |
| `4H` | `Bitunix` | `48.79%` | `51.21%` | `0.95` | 791,860.00 USD |
| `4H` | `Hyperliquid` | `56.06%` | `43.94%` | `1.28` | 470,830.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.62%` | `49.38%` | `1.03` | 7,920,000.00 USD |
| `4H` | `Crypto.com` | `1.81%` | `98.19%` | `0.02` | 3,580.00 USD |
| `4H` | `WhiteBIT` | `3.41%` | `96.59%` | `0.04` | 4,350,000.00 USD |
| `4H` | `HTX` | `52.23%` | `47.77%` | `1.09` | 50,430.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `35.1%` | `64.9%` | `0.54` | 105,690.00 USD |
| `4H` | `Aster` | `34.29%` | `65.71%` | `0.52` | 23,570.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `85.87%` | `14.13%` | `6.08` | 65,510.00 USD |
| `4H` | `Whale Positions` | `51%` | `49%` | `1.04` | 18,470,000.00 USD |
| `4H` | `Global Accounts` | `44.51%` | `55.49%` | `0.80` | 54,290,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `280.81` | `281.09` | `280.81` | `281.94` | `280.02` | 959,751.07 USD | 348,775.30 USD | 610,975.78 USD | -262,200.48 USD | `-27.32%` | `10B / 71S` |
| `5:00 UTC` | `278.88` | `279.51` | `278.88` | `280.56` | `278.74` | 1,525,848.29 USD | 843,855.80 USD | 681,992.49 USD | 161,863.30 USD | `+10.61%` | `26B / 51S` |
| `0:00 UTC` | `281.21` | `280.32` | `281.21` | `281.29` | `278.55` | 1,960,555.94 USD | 896,979.92 USD | 1,063,576.02 USD | -166,596.10 USD | `-8.50%` | `26B / 22S` |
| `5:00 UTC` | `279.18` | `279.58` | `279.18` | `280.70` | `279.06` | 617,038.04 USD | 332,886.00 USD | 284,152.04 USD | 48,733.95 USD | `+7.90%` | `32B / 38S` |
| `0:00 UTC` | `279.30` | `281.19` | `279.30` | `282.30` | `278.88` | 2,044,095.31 USD | 958,971.19 USD | 1,085,124.12 USD | -126,152.93 USD | `-6.17%` | `39B / 29S` |
| `5:00 UTC` | `281.23` | `281.19` | `281.23` | `281.62` | `280.50` | 432,406.23 USD | 225,151.97 USD | 207,254.26 USD | 17,897.70 USD | `+4.14%` | `20B / 20S` |
| `0:00 UTC` | `281.00` | `280.46` | `281.00` | `281.14` | `280.02` | 480,699.25 USD | 262,884.90 USD | 217,814.34 USD | 45,070.56 USD | `+9.38%` | `19B / 14S` |
| `5:00 UTC` | `282.00` | `281.11` | `282.00` | `282.22` | `280.16` | 658,245.44 USD | 414,390.84 USD | 243,854.60 USD | 170,536.24 USD | `+25.91%` | `33B / 5S` |
| `0:00 UTC` | `283.69` | `283.66` | `283.69` | `284.99` | `281.57` | 1,404,905.07 USD | 779,041.52 USD | 625,863.54 USD | 153,177.98 USD | `+10.90%` | `46B / 26S` |
| `5:00 UTC` | `284.51` | `284.94` | `284.51` | `286.25` | `283.71` | 892,829.84 USD | 529,460.66 USD | 363,369.18 USD | 166,091.48 USD | `+18.60%` | `37B / 18S` |

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
| `5m` | 85,460.00 USD | 151,470.00 USD | **`ACCUMULATION`** |
| `15m` | 157,140.00 USD | 462,800.00 USD | **`ACCUMULATION`** |
| `30m` | 175,630.00 USD | 997,210.00 USD | **`ACCUMULATION`** |
| `1h` | 189,670.00 USD | 1,280,000.00 USD | **`ACCUMULATION`** |
| `2h` | 302,100.00 USD | 939,420.00 USD | **`ACCUMULATION`** |
| `4h` | 402,400.00 USD | 1,020,000.00 USD | **`ACCUMULATION`** |
| `6h` | 441,750.00 USD | 1,420,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,110,000.00 USD | -458,760.00 USD | **`ACCUMULATION`** |
| `12h` | 755,100.00 USD | 124,250.00 USD | **`ACCUMULATION`** |
| `24h` | 367,890.00 USD | -913,540.00 USD | **`DISTRIBUTION`** |
| `1w` | 13,620.00 USD | -12,580,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,600,000.00 USD | -136,530,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+85.46K` | 15m=`+157.14K` | 1h=`+189.67K` | 24h=`+367.89K`
* Futures Capital Netflows: 5m=`+151.47K` | 15m=`+462.80K` | 1h=`+1.28M` | 24h=`-913.54K`
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
  * `2026-10-30 16:26:21 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:21 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:28:21 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:27:21 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:29:21 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `273.18` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `271.11` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `278.36`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `284.54` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `286.61` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `279.37`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`288.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
