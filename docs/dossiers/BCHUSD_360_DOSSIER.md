# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 10:31:46 IST` (`2026-10-30 05:01:46 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `282.96` | **Live Ask Quote**: `283.54` | **Mid Price**: `283.25`
- **Spread Points**: `580.00` | **Spread BPS**: `20.48 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `283.25` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `285.23` | Lower -3.00σ Band: `281.27`
  * Upper +2.51σ Band: `284.81` | Lower -2.51σ Band: `281.69`
  * Upper +2.01σ Band: `284.44` | Lower -2.01σ Band: `282.06`
  * Upper +2.00σ Band: `284.38` | Lower -2.00σ Band: `282.12`
  * Upper +1.28σ Band: `284.04` | Lower -1.28σ Band: `282.46`
  * Upper +1.00σ Band: `283.82` | Lower -1.00σ Band: `282.68`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`283.25` | EMA-20=`283.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`283.25` (Slope: `+0.0000`) | EMA-100=`283.25`
  * Institutional Anchors: EMA-144=`283.25` | EMA-200=`283.25` (Slope: `+0.0000`) | EMA-233=`283.25`
- **Range Boundaries**: 24H High=`286.08` | 24H Low=`280.42` | Weekly High=`288.92` | Weekly Low=`277.58`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.60` (Distance: `+1.63%`)
  * Point of Control (POC) = `276.23` (Distance: `+2.51%`)
  * Value Area Low (VAL) = `269.27` (Distance: `+5.15%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.38` | Low=`282.12`
  * New York Session (13:00-21:00 UTC): High=`284.95` | Low=`281.55`
  * Initial Balance (First Hour): IB High=`284.10` | IB Low=`282.40`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `282.12` - `284.38`
  * Optimal Trade Entry (OTE 0.705): `283.82`
  * Structural Invalidation Anchor (0.786): `285.52`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.79` | `284.99` | `283.77` | `284.08` | `1,101` | 312,983.82 USD | -100,924.82 USD | `-32.25%` | -2,071,323.97 USD | `-0.59` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `284.09` | `284.65` | `284.09` | `284.26` | `793` | 225,595.39 USD | 25,356.71 USD | `+11.24%` | -2,045,967.26 USD | `+0.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `284.27` | `285.15` | `284.18` | `284.47` | `620` | 176,520.29 USD | 46,505.18 USD | `+26.35%` | -1,999,462.08 USD | `+0.32` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `285.86` | `286.67` | `284.12` | `284.79` | `3,424` | 976,529.89 USD | -146,985.38 USD | `-15.05%` | -2,268,120.78 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `284.79` | `285.15` | `283.77` | `284.59` | `2,902` | 825,459.63 USD | -36,257.91 USD | `-4.39%` | -2,304,378.69 USD | `-0.08` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `284.59` | `284.96` | `283.66` | `283.67` | `2,875` | 817,720.58 USD | -89,292.11 USD | `-10.92%` | -2,393,670.80 USD | `-0.20` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `271.56` | `279.99` | `269.63` | `276.08` | `23,457` | 6,482,271.13 USD | -1,215,804.23 USD | `-18.76%` | -2,230,015.40 USD | `-1.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `276.08` | `284.75` | `276.00` | `283.99` | `21,838` | 6,138,674.85 USD | -75,926.04 USD | `-1.24%` | -2,305,941.44 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `283.99` | `287.12` | `282.33` | `283.72` | `21,476` | 6,116,155.84 USD | -86,871.43 USD | `-1.42%` | -2,392,812.87 USD | `-0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.47` | `18,217` | 5,189,159.00 USD | 8,820.03 USD | `+0.17%` | -1,865,562.97 USD | `+0.27` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | 1,085,885.17 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -386,016.76 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `283.72` | `21,476` | 6,116,155.84 USD | -86,871.43 USD | `-1.42%` | -1,961,254.43 USD | `+0.20` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1971` | `0x12d2...f97f` | `LONG` | 1,028,686.11 USD | `3,627,243,000,000.00` | `303.26` | `283.52` | `0.000000` | -71,313.22 USD | `-6.93%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `282.54` | 6,657.21 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale BUY: 6.66K USD at 282.5400 USD [API] | `2026-10-29 02:19:03` |


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
| `Live` | `Long Liquidation` | `63.50` | 2,600.00 USD | 196,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 255.15 USD | 194,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `81.50` | 584.76 USD | 193,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 1,170.00 USD | 193,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 920.05 USD | 192,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 6,240.00 USD | 191,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 4,080.00 USD | 185,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 168.67 USD | 180,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 212.76 USD | 180,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 156.21 USD | 180,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 859.42 USD | 180,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 1,100.00 USD | 179,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 212.35 USD | 178,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 124.46 USD | 178,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 3,110.00 USD | 178,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 658.18 USD | 175,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `133.50` | 2,000.00 USD | 174,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 895.47 USD | 172,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `148.50` | 1,270.00 USD | 171,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `149.50` | 2,370.00 USD | 170,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `152.50` | 303.78 USD | 167,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `162.50` | 325.00 USD | 167,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 8,280.00 USD | 167,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `167.50` | 285.75 USD | 158,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 426.25 USD | 158,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 169.96 USD | 158,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `175.50` | 516.67 USD | 158,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 373.83 USD | 157,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 191.57 USD | 157,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 616.05 USD | 156,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `188.50` | 418.28 USD | 156,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `190.50` | 694.75 USD | 155,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 858.49 USD | 155,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `192.50` | 1,490.00 USD | 154,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `193.50` | 1,050.00 USD | 152,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `195.50` | 370.47 USD | 151,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 210.65 USD | 151,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 548.03 USD | 151,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 293.13 USD | 150,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 420.39 USD | 150,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 191.53 USD | 150,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 42,410.00 USD | 149,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `208.50` | 6,570.00 USD | 107,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 108.83 USD | 100,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 3,800.00 USD | 100,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `215.50` | 2,610.00 USD | 96,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `223.50` | 32,860.00 USD | 94,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `225.50` | 5,370.00 USD | 61,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 1,240.00 USD | 56,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `227.50` | 174.49 USD | 54,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `228.50` | 642.77 USD | 54,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 7,980.00 USD | 54,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `231.50` | 411.61 USD | 46,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 637.61 USD | 45,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `234.70` | 9,910,000.00 USD | 9,910,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.20` | 9,900,000.00 USD | 9,900,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.70` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.20` | 9,890,000.00 USD | 9,890,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.70` | 9,860,000.00 USD | 9,860,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.20` | 9,850,000.00 USD | 9,850,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.70` | 9,830,000.00 USD | 9,830,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.20` | 9,820,000.00 USD | 9,820,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.70` | 9,800,000.00 USD | 9,800,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.20` | 9,770,000.00 USD | 9,770,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 21,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.70` | 9,760,000.00 USD | 9,760,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.70` | 9,760,000.00 USD | 9,760,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.20` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 20,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.70` | 9,750,000.00 USD | 9,750,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.20` | 9,740,000.00 USD | 9,740,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.70` | 9,670,000.00 USD | 9,670,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.20` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 3,380.00 USD | 19,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.70` | 9,620,000.00 USD | 9,620,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.20` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 16,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.70` | 9,570,000.00 USD | 9,570,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.20` | 9,560,000.00 USD | 9,560,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 12,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.70` | 9,530,000.00 USD | 9,530,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.20` | 9,510,000.00 USD | 9,510,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.70` | 9,470,000.00 USD | 9,470,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 9,460,000.00 USD | 9,460,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.50` | 4,640,000.00 USD | 4,640,000.00 USD | 3,600.00 USD | 2,380.00 USD | 7,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.70` | 9,420,000.00 USD | 9,420,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.90` | 4,630,000.00 USD | 4,630,000.00 USD | 1,810.00 USD | 1,070.00 USD | 17.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.20` | 9,400,000.00 USD | 9,400,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.30` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,880.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 1,550.00 USD | 18.71 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.70` | 9,390,000.00 USD | 9,390,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.10` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 1,740.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 9,290,000.00 USD | 9,290,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.50` | 4,600,000.00 USD | 4,600,000.00 USD | 13,440.00 USD | 10,020.00 USD | 2,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 10,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.70` | 9,230,000.00 USD | 9,230,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.90` | 4,580,000.00 USD | 4,580,000.00 USD | 9,330.00 USD | 1,330.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.20` | 9,120,000.00 USD | 9,120,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.30` | 4,560,000.00 USD | 4,560,000.00 USD | 8,970.00 USD | 5,940.00 USD | 5,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.70` | 4,540,000.00 USD | 4,540,000.00 USD | 8,410.00 USD | 1,930.00 USD | 12,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.70` | 9,010,000.00 USD | 9,010,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.10` | 4,520,000.00 USD | 4,520,000.00 USD | 31,820.00 USD | 43,790.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 8,870,000.00 USD | 8,870,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.50` | 4,430,000.00 USD | 4,430,000.00 USD | 7,900.00 USD | 49,670.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 7,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.70` | 8,750,000.00 USD | 8,750,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.90` | 4,350,000.00 USD | 4,350,000.00 USD | 42,420.00 USD | 37,240.00 USD | 21,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.20` | 8,560,000.00 USD | 8,560,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.30` | 4,250,000.00 USD | 4,250,000.00 USD | 18,430.00 USD | 8,120.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 7,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.70` | 4,220,000.00 USD | 4,220,000.00 USD | 16,100.00 USD | 7,120.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.70` | 8,440,000.00 USD | 8,440,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.10` | 4,190,000.00 USD | 4,190,000.00 USD | 7,380.00 USD | 8,330.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 8,330,000.00 USD | 8,330,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.50` | 4,170,000.00 USD | 4,170,000.00 USD | 17,140.00 USD | 16,560.00 USD | 21,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.70` | 8,270,000.00 USD | 8,270,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.90` | 4,120,000.00 USD | 4,120,000.00 USD | 6,840.00 USD | 8,550.00 USD | 9,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.20` | 8,150,000.00 USD | 8,150,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.30` | 4,090,000.00 USD | 4,090,000.00 USD | 8,310.00 USD | 2,620.00 USD | 3.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.70` | 4,080,000.00 USD | 4,080,000.00 USD | 820.64 USD | 11,440.00 USD | 6.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.70` | 8,050,000.00 USD | 8,050,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.10` | 4,070,000.00 USD | 4,070,000.00 USD | 16,950.00 USD | 8,770.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 7,880,000.00 USD | 7,880,000.00 USD | 32,100.00 USD | 13,440.00 USD | 35,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.50` | 4,030,000.00 USD | 4,030,000.00 USD | 6,410.00 USD | 25,790.00 USD | 17,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.70` | 7,790,000.00 USD | 7,790,000.00 USD | 33,430.00 USD | 16,550.00 USD | 34,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.90` | 3,980,000.00 USD | 3,980,000.00 USD | 14,560.00 USD | 790.27 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.20` | 7,710,000.00 USD | 7,710,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.30` | 3,960,000.00 USD | 3,960,000.00 USD | 3,840.00 USD | 33,520.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.70` | 3,910,000.00 USD | 3,910,000.00 USD | 4,370.00 USD | 1,360.00 USD | 13.09 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.70` | 7,570,000.00 USD | 7,570,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.10` | 3,910,000.00 USD | 3,910,000.00 USD | 14,160.00 USD | 1,230.00 USD | 8,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 7,460,000.00 USD | 7,460,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 3,880,000.00 USD | 3,880,000.00 USD | 1,190.00 USD | 5,680.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.70` | 7,420,000.00 USD | 7,420,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 3,870,000.00 USD | 3,870,000.00 USD | 4,520.00 USD | 1,550.00 USD | 37,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.20` | 7,350,000.00 USD | 7,350,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 3,820,000.00 USD | 3,820,000.00 USD | 24,350.00 USD | 15,770.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 3,760,000.00 USD | 3,760,000.00 USD | 18,720.00 USD | 30,560.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.70` | 7,150,000.00 USD | 7,150,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 3,670,000.00 USD | 3,670,000.00 USD | 14,580.00 USD | 13,100.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 6,990,000.00 USD | 6,990,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 3,630,000.00 USD | 3,630,000.00 USD | 13,390.00 USD | 4,340.00 USD | 32,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.70` | 6,890,000.00 USD | 6,890,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 3,580,000.00 USD | 3,580,000.00 USD | 45,110.00 USD | 33,000.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.20` | 6,740,000.00 USD | 6,740,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 3,490,000.00 USD | 3,490,000.00 USD | 13,810.00 USD | 6,720.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 3,450,000.00 USD | 3,450,000.00 USD | 7,460.00 USD | 24,480.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.70` | 6,520,000.00 USD | 6,520,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 3,390,000.00 USD | 3,390,000.00 USD | 8,370.00 USD | 30,470.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 6,390,000.00 USD | 6,390,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 3,320,000.00 USD | 3,320,000.00 USD | 18,870.00 USD | 43,450.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.70` | 6,270,000.00 USD | 6,270,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 3,230,000.00 USD | 3,230,000.00 USD | 4,750.00 USD | 69,840.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.20` | 6,100,000.00 USD | 6,100,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 3,120,000.00 USD | 3,120,000.00 USD | 34,230.00 USD | 4,590.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 3,060,000.00 USD | 3,060,000.00 USD | 366.04 USD | 13,020.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.70` | 5,900,000.00 USD | 5,900,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 3,030,000.00 USD | 3,030,000.00 USD | 9,320.00 USD | 3,840.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 5,720,000.00 USD | 5,720,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 3,010,000.00 USD | 3,010,000.00 USD | 30,390.00 USD | 343.40 USD | 74,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.70` | 5,660,000.00 USD | 5,660,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 2,910,000.00 USD | 2,910,000.00 USD | 32,780.00 USD | 38,010.00 USD | 45,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.20` | 5,260,000.00 USD | 5,260,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 2,790,000.00 USD | 2,790,000.00 USD | 25,930.00 USD | 16,940.00 USD | 17.51 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.70` | 2,750,000.00 USD | 2,750,000.00 USD | 1,070.00 USD | 9,820.00 USD | 19,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.70` | 5,090,000.00 USD | 5,090,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 2,720,000.00 USD | 2,720,000.00 USD | 33,450.00 USD | 1,600.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 5,040,000.00 USD | 5,040,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 2,650,000.00 USD | 2,650,000.00 USD | 63,680.00 USD | 666.50 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.70` | 4,900,000.00 USD | 4,900,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.90` | 2,580,000.00 USD | 2,580,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.20` | 4,700,000.00 USD | 4,700,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 2,570,000.00 USD | 2,570,000.00 USD | 3,880.00 USD | 13,250.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.70` | 2,550,000.00 USD | 2,550,000.00 USD | 28,750.00 USD | 8,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.70` | 4,510,000.00 USD | 4,510,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 2,510,000.00 USD | 2,510,000.00 USD | 47,450.00 USD | 54,160.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 4,310,000.00 USD | 4,310,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 2,400,000.00 USD | 2,400,000.00 USD | 7,660.00 USD | 44,340.00 USD | 9,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.70` | 4,130,000.00 USD | 4,130,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.90` | 2,340,000.00 USD | 2,340,000.00 USD | 4,660.00 USD | 28,110.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.20` | 3,800,000.00 USD | 3,800,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 2,280,000.00 USD | 2,280,000.00 USD | 4,570.00 USD | 35,070.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.70` | 3,470,000.00 USD | 3,470,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 2,190,000.00 USD | 2,190,000.00 USD | 8,580.00 USD | 656.20 USD | 20.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 3,400,000.00 USD | 3,400,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 16,170.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.70` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 2,160,000.00 USD | 2,160,000.00 USD | 378.60 USD | 1,170.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.20` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 2,150,000.00 USD | 2,150,000.00 USD | 9,760.00 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.70` | 2,140,000.00 USD | 2,140,000.00 USD | 323.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.70` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 7,970.00 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 2,130,000.00 USD | 2,130,000.00 USD | 12,710.00 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.70` | 3,380,000.00 USD | 3,380,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 25,790.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.20` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 2,080,000.00 USD | 2,080,000.00 USD | 21,160.00 USD | 15,900.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 2,020,000.00 USD | 2,020,000.00 USD | 36,620.00 USD | 16,330.00 USD | 48,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.70` | 3,250,000.00 USD | 3,250,000.00 USD | 25,660.00 USD | 17,630.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 1,920,000.00 USD | 1,920,000.00 USD | 23,080.00 USD | 66,980.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 37,090.00 USD | 20,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.70` | 2,910,000.00 USD | 2,910,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 1,760,000.00 USD | 1,760,000.00 USD | 129,000.00 USD | 70,140.00 USD | 38,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.20` | 2,780,000.00 USD | 2,780,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 1,520,000.00 USD | 1,520,000.00 USD | 199,980.00 USD | 0.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.70` | 1,310,000.00 USD | 1,310,000.00 USD | 149,350.00 USD | 19,960.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.70` | 2,270,000.00 USD | 2,270,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 1,100,000.00 USD | 1,100,000.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 1,650,000.00 USD | 1,650,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.70` | 1,490,000.00 USD | 1,490,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 1,050,000.00 USD | 1,050,000.00 USD | 20,900.00 USD | 10,450.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.20` | 1,400,000.00 USD | 1,400,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 977,220.00 USD | 977,220.00 USD | 89,570.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.70` | 884,430.00 USD | 884,430.00 USD | 11,880.00 USD | 13,540.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.70` | 1,230,000.00 USD | 1,230,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 847,930.00 USD | 847,930.00 USD | 25,410.00 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 1,120,000.00 USD | 1,120,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 811,910.00 USD | 811,910.00 USD | 301.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.70` | 969,160.00 USD | 969,160.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 811,610.00 USD | 811,610.00 USD | 12,120.00 USD | 1,140.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.20` | 574,100.00 USD | 574,100.00 USD | 24,750.00 USD | 37,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 769,580.00 USD | 769,580.00 USD | 42,620.00 USD | 109,300.00 USD | 47,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 569,920.00 USD | 569,920.00 USD | 29,210.00 USD | 10,830.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.70` | 512,260.00 USD | 512,260.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.10` | 495,420.00 USD | 495,420.00 USD | 0.00 USD | 53,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 460,020.00 USD | 460,020.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.70` | 457,350.00 USD | 457,350.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.90` | 442,310.00 USD | 442,310.00 USD | 14,720.00 USD | 14,930.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.20` | 455,590.00 USD | 455,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.30` | 381,310.00 USD | 381,310.00 USD | 14,910.00 USD | 44,960.00 USD | 86,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.70` | 234,620.00 USD | 234,620.00 USD | 28,040.00 USD | 38,990.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.70` | 438,230.00 USD | 438,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.10` | 157,360.00 USD | 157,360.00 USD | 12,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 422,680.00 USD | 422,680.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.50` | 144,620.00 USD | 144,620.00 USD | 0.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.70` | 325,280.00 USD | 325,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.90` | 137,680.00 USD | 137,680.00 USD | 2,050.00 USD | 13,250.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.20` | 127,860.00 USD | 127,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.30` | 118,230.00 USD | 118,230.00 USD | 8,260.00 USD | 9,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.70` | 100,890.00 USD | 100,890.00 USD | 0.00 USD | 63,980.00 USD | 19.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.10` | 36,890.00 USD | 36,890.00 USD | 14,930.00 USD | 20,630.00 USD | 35.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 103,640.00 USD | 103,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.50` | 1,290.00 USD | 1,290.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.70` | 2,000.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.20` | 74,590.00 USD | 74,590.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.30` | 4,200.00 USD | 4,200.00 USD | 3,780.00 USD | 397.40 USD | 26.15 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `284.50` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `284.70` | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 948.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.70` | 431,170.00 USD | 431,170.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.10` | 200,620.00 USD | 200,620.00 USD | 94,730.00 USD | 59,060.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.20` | 843,250.00 USD | 843,250.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.50` | 409,590.00 USD | 409,590.00 USD | 74,630.00 USD | 95,280.00 USD | 39,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.70` | 1,030,000.00 USD | 1,030,000.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.90` | 451,740.00 USD | 451,740.00 USD | 18,510.00 USD | 434.90 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.20` | 1,110,000.00 USD | 1,110,000.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.30` | 465,800.00 USD | 465,800.00 USD | 13,210.00 USD | 851.39 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.70` | 503,350.00 USD | 503,350.00 USD | 2,290.00 USD | 5,130.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.70` | 1,290,000.00 USD | 1,290,000.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.10` | 663,660.00 USD | 663,660.00 USD | 33,320.00 USD | 39,160.00 USD | 87,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 1,560,000.00 USD | 1,560,000.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.50` | 770,330.00 USD | 770,330.00 USD | 23,660.00 USD | 26,220.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 1,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `287.70` | 1,780,000.00 USD | 1,780,000.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.90` | 842,230.00 USD | 842,230.00 USD | 13,160.00 USD | 14,490.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.20` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.30` | 942,950.00 USD | 942,950.00 USD | 73,330.00 USD | 22,330.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 721.25 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.70` | 989,950.00 USD | 989,950.00 USD | 17,420.00 USD | 14,160.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.70` | 2,130,000.00 USD | 2,130,000.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 1,040,000.00 USD | 1,040,000.00 USD | 1,720.00 USD | 14,250.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 2,190,000.00 USD | 2,190,000.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.50` | 1,150,000.00 USD | 1,150,000.00 USD | 20,690.00 USD | 25,800.00 USD | 68,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.70` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 99,990.00 USD | 38,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.90` | 1,300,000.00 USD | 1,300,000.00 USD | 76,110.00 USD | 40,970.00 USD | 35,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.20` | 2,420,000.00 USD | 2,420,000.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.30` | 1,410,000.00 USD | 1,410,000.00 USD | 1,110.00 USD | 72,370.00 USD | 27,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.70` | 1,530,000.00 USD | 1,530,000.00 USD | 37,540.00 USD | 46,970.00 USD | 36,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.70` | 2,420,000.00 USD | 2,420,000.00 USD | 898.13 USD | 861.99 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 1,530,000.00 USD | 1,530,000.00 USD | 1,300.00 USD | 556.97 USD | 2.42 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 2,440,000.00 USD | 2,440,000.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 1,570,000.00 USD | 1,570,000.00 USD | 10,700.00 USD | 27,620.00 USD | 16.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.70` | 2,580,000.00 USD | 2,580,000.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 1,620,000.00 USD | 1,620,000.00 USD | 1,150.00 USD | 26,050.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.20` | 2,720,000.00 USD | 2,720,000.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 1,690,000.00 USD | 1,690,000.00 USD | 13,630.00 USD | 45,940.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 1,740,000.00 USD | 1,740,000.00 USD | 21,130.00 USD | 28,380.00 USD | 5,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.70` | 2,820,000.00 USD | 2,820,000.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 1,790,000.00 USD | 1,790,000.00 USD | 20,520.00 USD | 14,170.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 2,960,000.00 USD | 2,960,000.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 1,880,000.00 USD | 1,880,000.00 USD | 16,630.00 USD | 44,050.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.70` | 3,000,000.00 USD | 3,000,000.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 2,020,000.00 USD | 2,020,000.00 USD | 85,250.00 USD | 9,280.00 USD | 46,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.20` | 3,340,000.00 USD | 3,340,000.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 2,090,000.00 USD | 2,090,000.00 USD | 6,700.00 USD | 22,460.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `294.50` | 6,090.00 USD | 7,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `294.70` | 2,400,000.00 USD | 2,400,000.00 USD | 102,370.00 USD | 68,960.00 USD | 129,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.70` | 3,600,000.00 USD | 3,600,000.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 2,500,000.00 USD | 2,500,000.00 USD | 12,380.00 USD | 11,680.00 USD | 76,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 3,940,000.00 USD | 3,940,000.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 2,640,000.00 USD | 2,640,000.00 USD | 43,650.00 USD | 38,680.00 USD | 62,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.70` | 4,430,000.00 USD | 4,430,000.00 USD | 176,660.00 USD | 91,790.00 USD | 216,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 2,790,000.00 USD | 2,790,000.00 USD | 61,360.00 USD | 33,480.00 USD | 53,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.20` | 4,730,000.00 USD | 4,730,000.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 2,980,000.00 USD | 2,980,000.00 USD | 74,380.00 USD | 87,860.00 USD | 27,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.70` | 3,080,000.00 USD | 3,080,000.00 USD | 21,800.00 USD | 20,740.00 USD | 62,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.70` | 5,090,000.00 USD | 5,090,000.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 3,180,000.00 USD | 3,180,000.00 USD | 52,330.00 USD | 1,470.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,270,000.00 USD | 5,270,000.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 3,230,000.00 USD | 3,230,000.00 USD | 10,510.00 USD | 10,470.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.70` | 5,360,000.00 USD | 5,360,000.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 3,260,000.00 USD | 3,260,000.00 USD | 15,610.00 USD | 7,250.00 USD | 16,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.20` | 5,620,000.00 USD | 5,620,000.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 3,420,000.00 USD | 3,420,000.00 USD | 56,090.00 USD | 1,860.00 USD | 93,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 3,520,000.00 USD | 3,520,000.00 USD | 23,390.00 USD | 96.56 USD | 80,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.70` | 5,730,000.00 USD | 5,730,000.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 3,560,000.00 USD | 3,560,000.00 USD | 8,370.00 USD | 7,580.00 USD | 26,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 5,830,000.00 USD | 5,830,000.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 3,630,000.00 USD | 3,630,000.00 USD | 35,730.00 USD | 13,630.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.70` | 5,880,000.00 USD | 5,880,000.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 3,680,000.00 USD | 3,680,000.00 USD | 3,720.00 USD | 12,290.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.20` | 5,940,000.00 USD | 5,940,000.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 3,780,000.00 USD | 3,780,000.00 USD | 31,890.00 USD | 30,720.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 3,810,000.00 USD | 3,810,000.00 USD | 10,320.00 USD | 669.99 USD | 17,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.70` | 6,050,000.00 USD | 6,050,000.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 3,860,000.00 USD | 3,860,000.00 USD | 322.75 USD | 15,710.00 USD | 29,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 6,260,000.00 USD | 6,260,000.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 3,910,000.00 USD | 3,910,000.00 USD | 19,490.00 USD | 99.63 USD | 36,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.70` | 6,530,000.00 USD | 6,530,000.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 3,980,000.00 USD | 3,980,000.00 USD | 21,000.00 USD | 35,690.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.20` | 6,770,000.00 USD | 6,770,000.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 4,010,000.00 USD | 4,010,000.00 USD | 5,200.00 USD | 4,820.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.70` | 4,070,000.00 USD | 4,070,000.00 USD | 14,410.00 USD | 11,570.00 USD | 34,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.70` | 6,980,000.00 USD | 6,980,000.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 4,100,000.00 USD | 4,100,000.00 USD | 20,780.00 USD | 1,680.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 4,100,000.00 USD | 4,100,000.00 USD | 151.00 USD | 1,800.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.70` | 7,070,000.00 USD | 7,070,000.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 4,140,000.00 USD | 4,140,000.00 USD | 21,670.00 USD | 1,810.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.20` | 7,100,000.00 USD | 7,100,000.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 4,170,000.00 USD | 4,170,000.00 USD | 355.83 USD | 2,370.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 4,220,000.00 USD | 4,220,000.00 USD | 9,880.00 USD | 1,650.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.70` | 7,120,000.00 USD | 7,120,000.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 4,240,000.00 USD | 4,240,000.00 USD | 9,500.00 USD | 7,040.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 7,490,000.00 USD | 7,490,000.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 4,260,000.00 USD | 4,260,000.00 USD | 7,620.00 USD | 1,640.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.70` | 7,700,000.00 USD | 7,700,000.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 4,280,000.00 USD | 4,280,000.00 USD | 9,020.00 USD | 5,650.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.20` | 7,870,000.00 USD | 7,870,000.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 4,290,000.00 USD | 4,290,000.00 USD | 6,970.00 USD | 317.96 USD | 6,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `306.50` | 300.37 USD | 8,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `306.70` | 4,330,000.00 USD | 4,330,000.00 USD | 4,670.00 USD | 23,710.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.70` | 8,030,000.00 USD | 8,030,000.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 4,420,000.00 USD | 4,420,000.00 USD | 32,650.00 USD | 36,950.00 USD | 22,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 8,330,000.00 USD | 8,330,000.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 4,490,000.00 USD | 4,490,000.00 USD | 18,940.00 USD | 38,970.00 USD | 12,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.70` | 8,610,000.00 USD | 8,610,000.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 4,570,000.00 USD | 4,570,000.00 USD | 26,540.00 USD | 30,230.00 USD | 20,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.20` | 9,030,000.00 USD | 9,030,000.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 4,600,000.00 USD | 4,600,000.00 USD | 16,840.00 USD | 7,470.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 4,610,000.00 USD | 4,610,000.00 USD | 5,270.00 USD | 204.90 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.70` | 9,170,000.00 USD | 9,170,000.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 4,630,000.00 USD | 4,630,000.00 USD | 11,490.00 USD | 6,090.00 USD | 4,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 9,310,000.00 USD | 9,310,000.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 4,650,000.00 USD | 4,650,000.00 USD | 6,810.00 USD | 12,820.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.70` | 9,650,000.00 USD | 9,650,000.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 4,670,000.00 USD | 4,670,000.00 USD | 12,550.00 USD | 14.55 USD | 6,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.20` | 9,810,000.00 USD | 9,810,000.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 4,680,000.00 USD | 4,680,000.00 USD | 112.30 USD | 6,500.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.70` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 2,320.00 USD | 2.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.70` | 10,030,000.00 USD | 10,030,000.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 4,690,000.00 USD | 4,690,000.00 USD | 5,080.00 USD | 0.00 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,240,000.00 USD | 10,240,000.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 4,710,000.00 USD | 4,710,000.00 USD | 7,350.00 USD | 6,560.00 USD | 6.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.70` | 10,340,000.00 USD | 10,340,000.00 USD | 65,050.00 USD | 11,430.00 USD | 25,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 296.02 USD | 4,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.20` | 10,420,000.00 USD | 10,420,000.00 USD | 43,780.00 USD | 11,410.00 USD | 24,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 4,740,000.00 USD | 4,740,000.00 USD | 6,410.00 USD | 9,270.00 USD | 12,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 4,760,000.00 USD | 4,760,000.00 USD | 13,680.00 USD | 346.79 USD | 4,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.70` | 10,470,000.00 USD | 10,470,000.00 USD | 8,290.00 USD | 19,350.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 8,630.00 USD | 0.96 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 10,610,000.00 USD | 10,610,000.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 4,780,000.00 USD | 4,780,000.00 USD | 7,160.00 USD | 2,890.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.70` | 10,690,000.00 USD | 10,690,000.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 239.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.20` | 10,750,000.00 USD | 10,750,000.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.30` | 4,790,000.00 USD | 4,790,000.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.70` | 4,800,000.00 USD | 4,800,000.00 USD | 32.00 USD | 3,720.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.70` | 10,800,000.00 USD | 10,800,000.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.10` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 1,400.00 USD | 6,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 10,820,000.00 USD | 10,820,000.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.50` | 4,810,000.00 USD | 4,810,000.00 USD | 3,750.00 USD | 144.50 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.70` | 10,900,000.00 USD | 10,900,000.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.90` | 4,820,000.00 USD | 4,820,000.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.20` | 11,010,000.00 USD | 11,010,000.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.30` | 4,820,000.00 USD | 4,820,000.00 USD | 128.70 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.70` | 4,850,000.00 USD | 4,850,000.00 USD | 12,960.00 USD | 3,610.00 USD | 10,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.70` | 11,060,000.00 USD | 11,060,000.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `317.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 2,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 11,080,000.00 USD | 11,080,000.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.70` | 11,080,000.00 USD | 11,080,000.00 USD | 620.15 USD | 721.55 USD | 67.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.20` | 11,150,000.00 USD | 11,150,000.00 USD | 23,930.00 USD | 13,700.00 USD | 32,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.70` | 11,240,000.00 USD | 11,240,000.00 USD | 11,230.00 USD | 44,600.00 USD | 37,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.20` | 11,260,000.00 USD | 11,260,000.00 USD | 366.90 USD | 18,060.00 USD | 49.12 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.70` | 11,280,000.00 USD | 11,280,000.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.20` | 11,380,000.00 USD | 11,380,000.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `323.50` | 2,220.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `326.50` | 8,460.00 USD | 20,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `338.50` | 1,350.00 USD | 21,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `358.50` | 1,010.00 USD | 22,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `368.50` | 445.52 USD | 22,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `375.50` | 41,300.00 USD | 64,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `459.50` | 46,250.00 USD | 110,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `477.50` | 8,200.00 USD | 118,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `498.50` | 718.34 USD | 119,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `532.50` | 1,900.00 USD | 121,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `560.50` | 842.43 USD | 122,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `63.50` | 196,840.00 USD | 0.00 USD | 2,600.00 USD | `-77.58%` | `41,012,000,000.00` |
| `Live` | `Long` | `67.50` | 194,230.00 USD | 0.00 USD | 255.15 USD | `-76.17%` | `3,780,000,000.00` |
| `Live` | `Long` | `81.50` | 193,980.00 USD | 0.00 USD | 584.76 USD | `-71.22%` | `7,175,000,000.00` |
| `Live` | `Long` | `89.50` | 193,390.00 USD | 0.00 USD | 1,170.00 USD | `-68.40%` | `13,105,000,000.00` |
| `Live` | `Long` | `95.50` | 192,220.00 USD | 0.00 USD | 920.05 USD | `-66.28%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 191,300.00 USD | 0.00 USD | 6,240.00 USD | `-64.16%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 185,070.00 USD | 0.00 USD | 4,080.00 USD | `-63.81%` | `39,797,000,000.00` |
| `Live` | `Long` | `107.50` | 180,990.00 USD | 0.00 USD | 168.67 USD | `-62.04%` | `1,569,000,000.00` |
| `Live` | `Long` | `109.50` | 180,820.00 USD | 0.00 USD | 212.76 USD | `-61.33%` | `1,943,000,000.00` |
| `Live` | `Long` | `111.50` | 180,610.00 USD | 0.00 USD | 156.21 USD | `-60.63%` | `1,401,000,000.00` |
| `Live` | `Long` | `113.50` | 180,450.00 USD | 0.00 USD | 859.42 USD | `-59.92%` | `7,572,000,000.00` |
| `Live` | `Long` | `114.50` | 179,590.00 USD | 0.00 USD | 1,100.00 USD | `-59.57%` | `9,599,000,000.00` |
| `Live` | `Long` | `118.50` | 178,490.00 USD | 0.00 USD | 212.35 USD | `-58.16%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 178,280.00 USD | 0.00 USD | 124.46 USD | `-56.74%` | `1,016,000,000.00` |
| `Live` | `Long` | `124.50` | 178,150.00 USD | 0.00 USD | 3,110.00 USD | `-56.04%` | `25,000,000,000.00` |
| `Live` | `Long` | `126.50` | 175,040.00 USD | 0.00 USD | 658.18 USD | `-55.33%` | `5,203,000,000.00` |
| `Live` | `Long` | `133.50` | 174,380.00 USD | 0.00 USD | 2,000.00 USD | `-52.86%` | `15,000,000,000.00` |
| `Live` | `Long` | `147.50` | 172,380.00 USD | 0.00 USD | 895.47 USD | `-47.92%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 171,490.00 USD | 0.00 USD | 1,270.00 USD | `-47.56%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 170,220.00 USD | 0.00 USD | 2,370.00 USD | `-47.21%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 167,850.00 USD | 0.00 USD | 303.78 USD | `-46.15%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 167,550.00 USD | 0.00 USD | 325.00 USD | `-42.62%` | `2,000,000,000.00` |
| `Live` | `Long` | `165.50` | 167,220.00 USD | 0.00 USD | 8,280.00 USD | `-41.56%` | `50,000,000,000.00` |
| `Live` | `Long` | `167.50` | 158,950.00 USD | 0.00 USD | 285.75 USD | `-40.85%` | `1,706,000,000.00` |
| `Live` | `Long` | `170.50` | 158,660.00 USD | 0.00 USD | 426.25 USD | `-39.80%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 158,240.00 USD | 0.00 USD | 169.96 USD | `-38.38%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 158,070.00 USD | 0.00 USD | 516.67 USD | `-38.03%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 157,550.00 USD | 0.00 USD | 373.83 USD | `-37.68%` | `2,118,000,000.00` |
| `Live` | `Long` | `183.50` | 157,180.00 USD | 0.00 USD | 191.57 USD | `-35.20%` | `1,044,000,000.00` |
| `Live` | `Long` | `184.50` | 156,990.00 USD | 0.00 USD | 616.05 USD | `-34.85%` | `3,339,000,000.00` |
| `Live` | `Long` | `188.50` | 156,370.00 USD | 0.00 USD | 418.28 USD | `-33.44%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 155,950.00 USD | 0.00 USD | 694.75 USD | `-32.73%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 155,260.00 USD | 0.00 USD | 858.49 USD | `-32.38%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 154,400.00 USD | 0.00 USD | 1,490.00 USD | `-32.03%` | `7,715,000,000.00` |
| `Live` | `Long` | `193.50` | 152,910.00 USD | 0.00 USD | 1,050.00 USD | `-31.67%` | `5,434,000,000.00` |
| `Live` | `Long` | `195.50` | 151,860.00 USD | 0.00 USD | 370.47 USD | `-30.97%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 151,490.00 USD | 0.00 USD | 210.65 USD | `-30.61%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 151,280.00 USD | 0.00 USD | 548.03 USD | `-29.56%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 150,730.00 USD | 0.00 USD | 293.13 USD | `-29.20%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 150,440.00 USD | 0.00 USD | 420.39 USD | `-28.50%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 150,020.00 USD | 0.00 USD | 191.53 USD | `-27.44%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 149,830.00 USD | 0.00 USD | 42,410.00 USD | `-27.08%` | `205,387,000,000.00` |
| `Live` | `Long` | `208.50` | 107,410.00 USD | 0.00 USD | 6,570.00 USD | `-26.38%` | `31,500,000,000.00` |
| `Live` | `Long` | `210.50` | 100,850.00 USD | 0.00 USD | 108.83 USD | `-25.67%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 100,740.00 USD | 0.00 USD | 3,800.00 USD | `-24.61%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 96,930.00 USD | 0.00 USD | 2,610.00 USD | `-23.91%` | `12,132,000,000.00` |
| `Live` | `Long` | `223.50` | 94,320.00 USD | 0.00 USD | 32,860.00 USD | `-21.08%` | `147,023,000,000.00` |
| `Live` | `Long` | `225.50` | 61,460.00 USD | 0.00 USD | 5,370.00 USD | `-20.37%` | `23,803,000,000.00` |
| `Live` | `Long` | `226.50` | 56,090.00 USD | 0.00 USD | 1,240.00 USD | `-20.02%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 54,860.00 USD | 0.00 USD | 174.49 USD | `-19.67%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 54,680.00 USD | 0.00 USD | 642.77 USD | `-19.31%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 54,040.00 USD | 0.00 USD | 7,980.00 USD | `-18.96%` | `34,761,000,000.00` |
| `Live` | `Long` | `231.50` | 46,060.00 USD | 0.00 USD | 411.61 USD | `-18.26%` | `1,778,000,000.00` |
| `Live` | `Long` | `234.50` | 45,650.00 USD | 0.00 USD | 637.61 USD | `-17.20%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 45,010.00 USD | 0.00 USD | 23,750.00 USD | `-16.14%` | `100,000,000,000.00` |
| `Live` | `Long` | `239.50` | 21,260.00 USD | 0.00 USD | 1,030.00 USD | `-15.43%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 20,240.00 USD | 0.00 USD | 251.88 USD | `-14.72%` | `1,043,000,000.00` |
| `Live` | `Long` | `243.50` | 19,990.00 USD | 0.00 USD | 3,380.00 USD | `-14.02%` | `13,865,000,000.00` |
| `Live` | `Long` | `244.50` | 16,610.00 USD | 0.00 USD | 4,220.00 USD | `-13.67%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 12,390.00 USD | 0.00 USD | 1,030.00 USD | `-13.31%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 11,360.00 USD | 0.00 USD | 699.44 USD | `-12.61%` | `2,826,000,000.00` |
| `Live` | `Long` | `249.50` | 10,660.00 USD | 0.00 USD | 1,590.00 USD | `-11.90%` | `6,364,000,000.00` |
| `Live` | `Long` | `250.50` | 9,070.00 USD | 0.00 USD | 1,330.00 USD | `-11.55%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 7,750.00 USD | 0.00 USD | 268.35 USD | `-11.19%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 7,480.00 USD | 0.00 USD | 1,030.00 USD | `-10.84%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 6,440.00 USD | 0.00 USD | 548.45 USD | `-10.13%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 5,900.00 USD | 0.00 USD | 3,210.00 USD | `-9.43%` | `12,514,000,000.00` |
| `Live` | `Long` | `257.50` | 2,690.00 USD | 0.00 USD | 366.42 USD | `-9.07%` | `1,423,000,000.00` |
| `Live` | `Long` | `258.50` | 2,320.00 USD | 0.00 USD | 278.15 USD | `-8.72%` | `1,076,000,000.00` |
| `Live` | `Long` | `260.50` | 2,040.00 USD | 0.00 USD | 2,040.00 USD | `-8.02%` | `7,839,000,000.00` |
| `Live` | `Short` | `284.50` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | `+0.46%` | `3,674,000,000.00` |
| `Live` | `Short` | `287.50` | 1,160.00 USD | 112.12 USD | 0.00 USD | `+1.52%` | `390,000,000.00` |
| `Live` | `Short` | `288.50` | 1,880.00 USD | 721.25 USD | 0.00 USD | `+1.87%` | `2,500,000,000.00` |
| `Live` | `Short` | `294.50` | 7,970.00 USD | 6,090.00 USD | 0.00 USD | `+3.99%` | `20,668,000,000.00` |
| `Live` | `Short` | `306.50` | 8,270.00 USD | 300.37 USD | 0.00 USD | `+8.23%` | `980,000,000.00` |
| `Live` | `Short` | `320.50` | 9,370.00 USD | 1,110.00 USD | 0.00 USD | `+13.17%` | `3,452,000,000.00` |
| `Live` | `Short` | `323.50` | 11,590.00 USD | 2,220.00 USD | 0.00 USD | `+14.23%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 20,050.00 USD | 8,460.00 USD | 0.00 USD | `+15.29%` | `25,926,000,000.00` |
| `Live` | `Short` | `338.50` | 21,410.00 USD | 1,350.00 USD | 0.00 USD | `+19.53%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 22,420.00 USD | 1,010.00 USD | 0.00 USD | `+26.59%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 22,860.00 USD | 445.52 USD | 0.00 USD | `+30.12%` | `1,209,000,000.00` |
| `Live` | `Short` | `375.50` | 64,170.00 USD | 41,300.00 USD | 0.00 USD | `+32.59%` | `110,000,000,000.00` |
| `Live` | `Short` | `459.50` | 110,420.00 USD | 46,250.00 USD | 0.00 USD | `+62.25%` | `100,662,000,000.00` |
| `Live` | `Short` | `477.50` | 118,620.00 USD | 8,200.00 USD | 0.00 USD | `+68.61%` | `17,172,000,000.00` |
| `Live` | `Short` | `498.50` | 119,340.00 USD | 718.34 USD | 0.00 USD | `+76.02%` | `1,441,000,000.00` |
| `Live` | `Short` | `532.50` | 121,240.00 USD | 1,900.00 USD | 0.00 USD | `+88.03%` | `3,573,000,000.00` |
| `Live` | `Short` | `560.50` | 122,080.00 USD | 842.43 USD | 0.00 USD | `+97.92%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 441,430.00 USD | 0.00 USD | 210.94 USD | `-49.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 441,220.00 USD | 0.00 USD | 2,070.00 USD | `-48.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 439,150.00 USD | 0.00 USD | 489.38 USD | `-41.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 438,660.00 USD | 0.00 USD | 2,530.00 USD | `-36.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 436,130.00 USD | 0.00 USD | 490.59 USD | `-34.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 435,640.00 USD | 0.00 USD | 482.01 USD | `-30.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 435,160.00 USD | 0.00 USD | 189.07 USD | `-29.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 434,970.00 USD | 0.00 USD | 441.60 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 434,530.00 USD | 0.00 USD | 299.96 USD | `-25.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 434,230.00 USD | 0.00 USD | 715.29 USD | `-25.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 433,510.00 USD | 0.00 USD | 638.36 USD | `-21.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 432,880.00 USD | 0.00 USD | 740.85 USD | `-20.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 432,140.00 USD | 0.00 USD | 478.48 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 431,660.00 USD | 0.00 USD | 389.48 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 431,270.00 USD | 0.00 USD | 812.38 USD | `-16.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 430,460.00 USD | 0.00 USD | 220.64 USD | `-16.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 430,230.00 USD | 0.00 USD | 429.30 USD | `-15.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 429,810.00 USD | 0.00 USD | 296.50 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 429,510.00 USD | 0.00 USD | 216.45 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 429,290.00 USD | 0.00 USD | 387.76 USD | `-14.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 428,900.00 USD | 0.00 USD | 9,420.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 419,490.00 USD | 0.00 USD | 1,630.00 USD | `-12.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 417,860.00 USD | 0.00 USD | 2,700.00 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 415,160.00 USD | 0.00 USD | 2,940.00 USD | `-11.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 412,220.00 USD | 0.00 USD | 4,560.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 407,660.00 USD | 0.00 USD | 1,850.00 USD | `-11.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 405,810.00 USD | 0.00 USD | 231.54 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 405,580.00 USD | 0.00 USD | 109.26 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 405,470.00 USD | 0.00 USD | 1,780.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 403,690.00 USD | 0.00 USD | 51,300.00 USD | `-9.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 352,390.00 USD | 0.00 USD | 250.81 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 352,140.00 USD | 0.00 USD | 2,370.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 349,770.00 USD | 0.00 USD | 269,800.00 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `262.50` | 79,980.00 USD | 0.00 USD | 857.85 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 79,120.00 USD | 0.00 USD | 320.15 USD | `-6.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 78,800.00 USD | 0.00 USD | 199.17 USD | `-6.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 78,600.00 USD | 0.00 USD | 2,180.00 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 76,420.00 USD | 0.00 USD | 241.98 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 76,180.00 USD | 0.00 USD | 219.35 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 75,960.00 USD | 0.00 USD | 107.40 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 75,850.00 USD | 0.00 USD | 29,530.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 46,330.00 USD | 0.00 USD | 3,340.00 USD | `-4.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 42,980.00 USD | 0.00 USD | 620.38 USD | `-4.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 42,360.00 USD | 0.00 USD | 13,500.00 USD | `-3.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 28,870.00 USD | 0.00 USD | 1,010.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 27,850.00 USD | 0.00 USD | 667.86 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 27,180.00 USD | 0.00 USD | 299.74 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 26,880.00 USD | 0.00 USD | 903.60 USD | `-2.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 25,980.00 USD | 0.00 USD | 326.34 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 25,650.00 USD | 0.00 USD | 125.88 USD | `-1.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 25,530.00 USD | 0.00 USD | 21,990.00 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `280.50` | 3,540.00 USD | 0.00 USD | 3,080.00 USD | `-0.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `281.50` | 460.39 USD | 0.00 USD | 104.72 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `282.50` | 355.67 USD | 0.00 USD | 355.67 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 8,040.00 USD | 8,040.00 USD | 0.00 USD | `+0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 10,050.00 USD | 2,010.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 11,100.00 USD | 1,050.00 USD | 0.00 USD | `+0.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 11,380.00 USD | 280.77 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 16,540.00 USD | 5,160.00 USD | 0.00 USD | `+1.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 16,800.00 USD | 261.96 USD | 0.00 USD | `+1.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 17,330.00 USD | 530.36 USD | 0.00 USD | `+2.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 19,480.00 USD | 2,150.00 USD | 0.00 USD | `+2.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 44,760.00 USD | 25,280.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 44,860.00 USD | 107.05 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 45,860.00 USD | 992.62 USD | 0.00 USD | `+3.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 47,870.00 USD | 2,020.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 52,600.00 USD | 4,730.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `296.50` | 53,180.00 USD | 581.14 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 53,290.00 USD | 110.37 USD | 0.00 USD | `+5.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 53,680.00 USD | 388.95 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 53,840.00 USD | 153.94 USD | 0.00 USD | `+5.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 64,610.00 USD | 10,780.00 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 75,340.00 USD | 10,730.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 77,990.00 USD | 2,650.00 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 78,090.00 USD | 102.73 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 92,590.00 USD | 14,500.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 93,220.00 USD | 634.04 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 94,260.00 USD | 1,030.00 USD | 0.00 USD | `+11.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 99,910.00 USD | 5,650.00 USD | 0.00 USD | `+12.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 100,440.00 USD | 534.59 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 100,760.00 USD | 321.50 USD | 0.00 USD | `+13.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 167,480.00 USD | 66,720.00 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 168,570.00 USD | 1,090.00 USD | 0.00 USD | `+17.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 180,560.00 USD | 12,000.00 USD | 0.00 USD | `+18.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 181,110.00 USD | 547.52 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 181,220.00 USD | 110.91 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 181,480.00 USD | 257.45 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 181,650.00 USD | 174.25 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 181,810.00 USD | 151.50 USD | 0.00 USD | `+24.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 183,260.00 USD | 1,450.00 USD | 0.00 USD | `+26.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 185,030.00 USD | 1,770.00 USD | 0.00 USD | `+26.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 185,360.00 USD | 326.07 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 186,190.00 USD | 826.60 USD | 0.00 USD | `+28.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 193,630.00 USD | 7,440.00 USD | 0.00 USD | `+29.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 194,310.00 USD | 682.84 USD | 0.00 USD | `+30.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 195,410.00 USD | 1,100.00 USD | 0.00 USD | `+34.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 196,100.00 USD | 683.96 USD | 0.00 USD | `+40.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 196,300.00 USD | 199.75 USD | 0.00 USD | `+41.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 197,590.00 USD | 1,290.00 USD | 0.00 USD | `+41.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 198,630.00 USD | 1,040.00 USD | 0.00 USD | `+42.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 199,000.00 USD | 376.71 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 199,160.00 USD | 158.86 USD | 0.00 USD | `+44.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 205,060.00 USD | 5,900.00 USD | 0.00 USD | `+46.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 206,140.00 USD | 1,080.00 USD | 0.00 USD | `+49.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 207,840.00 USD | 1,700.00 USD | 0.00 USD | `+50.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 209,400.00 USD | 1,550.00 USD | 0.00 USD | `+52.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 210,780.00 USD | 1,380.00 USD | 0.00 USD | `+53.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 211,400.00 USD | 621.14 USD | 0.00 USD | `+54.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 213,680.00 USD | 2,280.00 USD | 0.00 USD | `+55.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 213,900.00 USD | 222.75 USD | 0.00 USD | `+57.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 220,820.00 USD | 6,920.00 USD | 0.00 USD | `+59.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 226,740.00 USD | 5,920.00 USD | 0.00 USD | `+59.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 227,870.00 USD | 1,130.00 USD | 0.00 USD | `+62.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 235,500.00 USD | 7,630.00 USD | 0.00 USD | `+70.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 236,480.00 USD | 975.00 USD | 0.00 USD | `+72.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 237,460.00 USD | 981.00 USD | 0.00 USD | `+73.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 237,960.00 USD | 499.50 USD | 0.00 USD | `+76.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,120,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+76.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,130,000.00 USD | 1,000.00 USD | 0.00 USD | `+77.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,130,000.00 USD | 1,040.00 USD | 0.00 USD | `+83.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,130,000.00 USD | 340.67 USD | 0.00 USD | `+84.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,130,000.00 USD | 638.86 USD | 0.00 USD | `+96.50%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.70` | 9,910,000.00 USD | 0.00 USD | 9,910,000.00 USD | 3,590.00 USD | 4,080.00 USD | 3,090.00 USD |
| `7D` | `235.20` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 3,770.00 USD | 151.15 USD | 3,650.00 USD |
| `7D` | `235.70` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 0.00 USD | 120.85 USD | 3,540.00 USD |
| `7D` | `236.20` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 5,950.00 USD | 0.00 USD | 15,850.00 USD |
| `7D` | `236.70` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 196.53 USD | 11,870.00 USD | 4,340.00 USD |
| `7D` | `237.20` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 0.00 USD | 5,440.00 USD | 15,200.00 USD |
| `7D` | `237.70` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 5,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `238.20` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 178.62 USD | 6,720.00 USD | 12,580.00 USD |
| `7D` | `238.70` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 140.10 USD | 9,360.00 USD | 19,460.00 USD |
| `7D` | `239.20` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 5,410.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.70` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 887.27 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.70` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 2,780.00 USD | 0.00 USD | 4,580.00 USD |
| `7D` | `241.20` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.70` | 9,750,000.00 USD | 0.00 USD | 9,750,000.00 USD | 8,260.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.20` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 40,810.00 USD | 11,260.00 USD | 16,610.00 USD |
| `7D` | `242.70` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 14,370.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `243.20` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 0.00 USD | 16,620.00 USD | 5,490.00 USD |
| `7D` | `243.70` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `244.20` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.70` | 9,570,000.00 USD | 0.00 USD | 9,570,000.00 USD | 836.88 USD | 4,470.00 USD | 2,640.00 USD |
| `7D` | `245.20` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 599.05 USD | 29,150.00 USD | 1,640.00 USD |
| `7D` | `245.70` | 9,530,000.00 USD | 0.00 USD | 9,530,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD |
| `7D` | `246.20` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 15,600.00 USD | 17,450.00 USD | 7,710.00 USD |
| `7D` | `246.70` | 9,470,000.00 USD | 0.00 USD | 9,470,000.00 USD | 12,290.00 USD | 910.23 USD | 3.03 USD |
| `7D` | `247.20` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 14,580.00 USD | 17,800.00 USD | 4,420.00 USD |
| `1D` | `247.50` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 3,600.00 USD | 2,380.00 USD | 7,280.00 USD |
| `7D` | `247.70` | 9,420,000.00 USD | 0.00 USD | 9,420,000.00 USD | 9,440.00 USD | 4,610.00 USD | 27.59 USD |
| `1D` | `247.90` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 1,810.00 USD | 1,070.00 USD | 17.39 USD |
| `7D` | `248.20` | 9,400,000.00 USD | 0.00 USD | 9,400,000.00 USD | 5,250.00 USD | 2,680.00 USD | 6,400.00 USD |
| `1D` | `248.30` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 0.00 USD | 1,880.00 USD | 9,360.00 USD |
| `1D` | `248.70` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 0.00 USD | 1,550.00 USD | 18.71 USD |
| `7D` | `248.70` | 9,390,000.00 USD | 0.00 USD | 9,390,000.00 USD | 36,860.00 USD | 12,340.00 USD | 49,660.00 USD |
| `1D` | `249.10` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 0.00 USD | 1,740.00 USD | 4,200.00 USD |
| `7D` | `249.20` | 9,290,000.00 USD | 0.00 USD | 9,290,000.00 USD | 23,940.00 USD | 34,670.00 USD | 7,050.00 USD |
| `1D` | `249.50` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 13,440.00 USD | 10,020.00 USD | 2,040.00 USD |
| `7D` | `249.70` | 9,230,000.00 USD | 0.00 USD | 9,230,000.00 USD | 57,160.00 USD | 35,710.00 USD | 16,350.00 USD |
| `1D` | `249.90` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 9,330.00 USD | 1,330.00 USD | 3,490.00 USD |
| `7D` | `250.20` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 45,440.00 USD | 39,620.00 USD | 26,320.00 USD |
| `1D` | `250.30` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 8,970.00 USD | 5,940.00 USD | 5,870.00 USD |
| `1D` | `250.70` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 8,410.00 USD | 1,930.00 USD | 12,030.00 USD |
| `7D` | `250.70` | 9,010,000.00 USD | 0.00 USD | 9,010,000.00 USD | 34,320.00 USD | 66,900.00 USD | 36,630.00 USD |
| `1D` | `251.10` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 31,820.00 USD | 43,790.00 USD | 13,070.00 USD |
| `7D` | `251.20` | 8,870,000.00 USD | 0.00 USD | 8,870,000.00 USD | 47,380.00 USD | 55,870.00 USD | 18,200.00 USD |
| `1D` | `251.50` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 7,900.00 USD | 49,670.00 USD | 25,500.00 USD |
| `7D` | `251.70` | 8,750,000.00 USD | 0.00 USD | 8,750,000.00 USD | 54,630.00 USD | 88,770.00 USD | 40,630.00 USD |
| `1D` | `251.90` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 42,420.00 USD | 37,240.00 USD | 21,170.00 USD |
| `7D` | `252.20` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 62,800.00 USD | 34,890.00 USD | 25,880.00 USD |
| `1D` | `252.30` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 18,430.00 USD | 8,120.00 USD | 4,410.00 USD |
| `1D` | `252.70` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 16,100.00 USD | 7,120.00 USD | 4,140.00 USD |
| `7D` | `252.70` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 63,690.00 USD | 28,310.00 USD | 15,320.00 USD |
| `1D` | `253.10` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 7,380.00 USD | 8,330.00 USD | 3,700.00 USD |
| `7D` | `253.20` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 12,990.00 USD | 36,680.00 USD | 14,210.00 USD |
| `1D` | `253.50` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 17,140.00 USD | 16,560.00 USD | 21,070.00 USD |
| `7D` | `253.70` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 35,000.00 USD | 43,350.00 USD | 34,100.00 USD |
| `1D` | `253.90` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 6,840.00 USD | 8,550.00 USD | 9,590.00 USD |
| `7D` | `254.20` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 37,910.00 USD | 42,030.00 USD | 25,760.00 USD |
| `1D` | `254.30` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 8,310.00 USD | 2,620.00 USD | 3.80 USD |
| `1D` | `254.70` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 820.64 USD | 11,440.00 USD | 6.94 USD |
| `7D` | `254.70` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 54,510.00 USD | 41,710.00 USD | 77,340.00 USD |
| `1D` | `255.10` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 16,950.00 USD | 8,770.00 USD | 7,310.00 USD |
| `7D` | `255.20` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 32,100.00 USD | 13,440.00 USD | 35,520.00 USD |
| `1D` | `255.50` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 6,410.00 USD | 25,790.00 USD | 17,900.00 USD |
| `7D` | `255.70` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 33,430.00 USD | 16,550.00 USD | 34,000.00 USD |
| `1D` | `255.90` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 14,560.00 USD | 790.27 USD | 4,380.00 USD |
| `7D` | `256.20` | 7,710,000.00 USD | 0.00 USD | 7,710,000.00 USD | 71,430.00 USD | 24,580.00 USD | 48,040.00 USD |
| `1D` | `256.30` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 3,840.00 USD | 33,520.00 USD | 15,090.00 USD |
| `1D` | `256.70` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 4,370.00 USD | 1,360.00 USD | 13.09 USD |
| `7D` | `256.70` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 42,150.00 USD | 19,480.00 USD | 43,290.00 USD |
| `1D` | `257.10` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 14,160.00 USD | 1,230.00 USD | 8,860.00 USD |
| `7D` | `257.20` | 7,460,000.00 USD | 0.00 USD | 7,460,000.00 USD | 16,870.00 USD | 5,540.00 USD | 20,570.00 USD |
| `1D` | `257.50` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 1,190.00 USD | 5,680.00 USD | 8,330.00 USD |
| `7D` | `257.70` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 42,060.00 USD | 6,820.00 USD | 18,200.00 USD |
| `1D` | `257.90` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 4,520.00 USD | 1,550.00 USD | 37,110.00 USD |
| `7D` | `258.20` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 105,450.00 USD | 42,340.00 USD | 54,140.00 USD |
| `1D` | `258.30` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 24,350.00 USD | 15,770.00 USD | 25,890.00 USD |
| `1D` | `258.70` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 18,720.00 USD | 30,560.00 USD | 40,000.00 USD |
| `7D` | `258.70` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 101,480.00 USD | 8,800.00 USD | 54,330.00 USD |
| `1D` | `259.10` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 14,580.00 USD | 13,100.00 USD | 7,670.00 USD |
| `7D` | `259.20` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 20,040.00 USD | 46,410.00 USD | 26,420.00 USD |
| `1D` | `259.50` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 13,390.00 USD | 4,340.00 USD | 32,200.00 USD |
| `7D` | `259.70` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 21,510.00 USD | 15,590.00 USD | 114,150.00 USD |
| `1D` | `259.90` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 45,110.00 USD | 33,000.00 USD | 17,070.00 USD |
| `7D` | `260.20` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 103,470.00 USD | 58,310.00 USD | 60,890.00 USD |
| `1D` | `260.30` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 13,810.00 USD | 6,720.00 USD | 13,310.00 USD |
| `1D` | `260.70` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 7,460.00 USD | 24,480.00 USD | 28,530.00 USD |
| `7D` | `260.70` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 16,810.00 USD | 46,420.00 USD | 60,260.00 USD |
| `1D` | `261.10` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 8,370.00 USD | 30,470.00 USD | 37,020.00 USD |
| `7D` | `261.20` | 6,390,000.00 USD | 0.00 USD | 6,390,000.00 USD | 6,940.00 USD | 100,180.00 USD | 16,010.00 USD |
| `1D` | `261.50` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 18,870.00 USD | 43,450.00 USD | 28,230.00 USD |
| `7D` | `261.70` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 25,970.00 USD | 89,470.00 USD | 56,500.00 USD |
| `1D` | `261.90` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 4,750.00 USD | 69,840.00 USD | 36,450.00 USD |
| `7D` | `262.20` | 6,100,000.00 USD | 0.00 USD | 6,100,000.00 USD | 60,650.00 USD | 63,760.00 USD | 73,230.00 USD |
| `1D` | `262.30` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 34,230.00 USD | 4,590.00 USD | 21,320.00 USD |
| `1D` | `262.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 366.04 USD | 13,020.00 USD | 15,830.00 USD |
| `7D` | `262.70` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 81,840.00 USD | 70,010.00 USD | 26,770.00 USD |
| `1D` | `263.10` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 9,320.00 USD | 3,840.00 USD | 3,650.00 USD |
| `7D` | `263.20` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 40,950.00 USD | 13,230.00 USD | 6,040.00 USD |
| `1D` | `263.50` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 30,390.00 USD | 343.40 USD | 74,200.00 USD |
| `7D` | `263.70` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 279,310.00 USD | 1,380.00 USD | 117,870.00 USD |
| `1D` | `263.90` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 32,780.00 USD | 38,010.00 USD | 45,590.00 USD |
| `7D` | `264.20` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 172,460.00 USD | 0.00 USD | 108.55 USD |
| `1D` | `264.30` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 25,930.00 USD | 16,940.00 USD | 17.51 USD |
| `1D` | `264.70` | 2,750,000.00 USD | 0.00 USD | 2,750,000.00 USD | 1,070.00 USD | 9,820.00 USD | 19,930.00 USD |
| `7D` | `264.70` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 34,240.00 USD | 21,410.00 USD | 112.55 USD |
| `1D` | `265.10` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 33,450.00 USD | 1,600.00 USD | 33,280.00 USD |
| `7D` | `265.20` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 107,040.00 USD | 0.00 USD | 34,010.00 USD |
| `1D` | `265.50` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 63,680.00 USD | 666.50 USD | 0.00 USD |
| `7D` | `265.70` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 199,660.00 USD | 0.00 USD | 159.14 USD |
| `1D` | `265.90` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 12,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `266.20` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 186,110.00 USD | 0.00 USD | 24.03 USD |
| `1D` | `266.30` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 3,880.00 USD | 13,250.00 USD | 4,800.00 USD |
| `1D` | `266.70` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 28,750.00 USD | 8,190.00 USD | 0.00 USD |
| `7D` | `266.70` | 4,510,000.00 USD | 0.00 USD | 4,510,000.00 USD | 136,380.00 USD | 63,260.00 USD | 36.67 USD |
| `1D` | `267.10` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 47,450.00 USD | 54,160.00 USD | 12,550.00 USD |
| `7D` | `267.20` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 151,750.00 USD | 26,020.00 USD | 29.12 USD |
| `1D` | `267.50` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 7,660.00 USD | 44,340.00 USD | 9,770.00 USD |
| `7D` | `267.70` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 231,410.00 USD | 61,270.00 USD | 38,730.00 USD |
| `1D` | `267.90` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 4,660.00 USD | 28,110.00 USD | 22,270.00 USD |
| `7D` | `268.20` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 137,230.00 USD | 146,930.00 USD | 47,910.00 USD |
| `1D` | `268.30` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 4,570.00 USD | 35,070.00 USD | 46,300.00 USD |
| `7D` | `268.70` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 48,170.00 USD | 1,850.00 USD | 14,970.00 USD |
| `1D` | `269.10` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 8,580.00 USD | 656.20 USD | 20.82 USD |
| `7D` | `269.20` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 23,340.00 USD | 0.00 USD | 117.25 USD |
| `1D` | `269.50` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 0.00 USD | 16,170.00 USD | 10,200.00 USD |
| `7D` | `269.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 0.00 USD | 1,930.00 USD | 156.86 USD |
| `1D` | `269.90` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 378.60 USD | 1,170.00 USD | 3,380.00 USD |
| `7D` | `270.20` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 216.19 USD |
| `1D` | `270.30` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 9,760.00 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `270.70` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 323.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `270.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 180.99 USD |
| `1D` | `271.10` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 0.00 USD | 7,970.00 USD | 2,750.00 USD |
| `1D` | `271.50` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 12,710.00 USD | 0.00 USD | 5,300.00 USD |
| `7D` | `271.70` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD |
| `1D` | `271.90` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 25,790.00 USD | 9,610.00 USD |
| `7D` | `272.20` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.30` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 21,160.00 USD | 15,900.00 USD | 14,390.00 USD |
| `1D` | `272.70` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 36,620.00 USD | 16,330.00 USD | 48,990.00 USD |
| `7D` | `272.70` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 25,660.00 USD | 17,630.00 USD | 0.00 USD |
| `1D` | `273.10` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 23,080.00 USD | 66,980.00 USD | 17,220.00 USD |
| `7D` | `273.20` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 0.00 USD | 122,540.00 USD | 173,630.00 USD |
| `1D` | `273.50` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 37,090.00 USD | 20,500.00 USD |
| `7D` | `273.70` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 63,170.00 USD | 0.00 USD | 66,850.00 USD |
| `1D` | `273.90` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 129,000.00 USD | 70,140.00 USD | 38,950.00 USD |
| `7D` | `274.20` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 503,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.30` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 199,980.00 USD | 0.00 USD | 12,870.00 USD |
| `1D` | `274.70` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 149,350.00 USD | 19,960.00 USD | 41,170.00 USD |
| `7D` | `274.70` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 506,420.00 USD | 0.00 USD | 117,760.00 USD |
| `1D` | `275.10` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.20` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 140,680.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.50` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 26,710.00 USD |
| `7D` | `275.70` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 1,350.00 USD | 0.00 USD | 82,330.00 USD |
| `1D` | `275.90` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 20,900.00 USD | 10,450.00 USD | 40,360.00 USD |
| `7D` | `276.20` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 153,810.00 USD | 23,010.00 USD | 0.00 USD |
| `1D` | `276.30` | 977,220.00 USD | 0.00 USD | 977,220.00 USD | 89,570.00 USD | 0.00 USD | 3,220.00 USD |
| `1D` | `276.70` | 884,430.00 USD | 0.00 USD | 884,430.00 USD | 11,880.00 USD | 13,540.00 USD | 11,090.00 USD |
| `7D` | `276.70` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 485.90 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `277.10` | 847,930.00 USD | 0.00 USD | 847,930.00 USD | 25,410.00 USD | 0.00 USD | 10,600.00 USD |
| `7D` | `277.20` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 44,670.00 USD | 27,710.00 USD | 80,970.00 USD |
| `1D` | `277.50` | 811,910.00 USD | 0.00 USD | 811,910.00 USD | 301.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.70` | 969,160.00 USD | 0.00 USD | 969,160.00 USD | 123,610.00 USD | 193,330.00 USD | 78,120.00 USD |
| `1D` | `277.90` | 811,610.00 USD | 0.00 USD | 811,610.00 USD | 12,120.00 USD | 1,140.00 USD | 28,780.00 USD |
| `7D` | `278.20` | 574,100.00 USD | 0.00 USD | 574,100.00 USD | 24,750.00 USD | 37,090.00 USD | 0.00 USD |
| `1D` | `278.30` | 769,580.00 USD | 0.00 USD | 769,580.00 USD | 42,620.00 USD | 109,300.00 USD | 47,740.00 USD |
| `1D` | `278.70` | 569,920.00 USD | 0.00 USD | 569,920.00 USD | 29,210.00 USD | 10,830.00 USD | 34,450.00 USD |
| `7D` | `278.70` | 512,260.00 USD | 0.00 USD | 512,260.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD |
| `1D` | `279.10` | 495,420.00 USD | 0.00 USD | 495,420.00 USD | 0.00 USD | 53,110.00 USD | 0.00 USD |
| `7D` | `279.20` | 460,020.00 USD | 0.00 USD | 460,020.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `279.70` | 457,350.00 USD | 0.00 USD | 457,350.00 USD | 0.00 USD | 1,770.00 USD | 0.00 USD |
| `1D` | `279.90` | 442,310.00 USD | 0.00 USD | 442,310.00 USD | 14,720.00 USD | 14,930.00 USD | 31,350.00 USD |
| `7D` | `280.20` | 455,590.00 USD | 0.00 USD | 455,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD |
| `1D` | `280.30` | 381,310.00 USD | 0.00 USD | 381,310.00 USD | 14,910.00 USD | 44,960.00 USD | 86,830.00 USD |
| `1D` | `280.70` | 234,620.00 USD | 0.00 USD | 234,620.00 USD | 28,040.00 USD | 38,990.00 USD | 10,230.00 USD |
| `7D` | `280.70` | 438,230.00 USD | 0.00 USD | 438,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `281.10` | 157,360.00 USD | 0.00 USD | 157,360.00 USD | 12,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `281.20` | 422,680.00 USD | 0.00 USD | 422,680.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `1D` | `281.50` | 144,620.00 USD | 0.00 USD | 144,620.00 USD | 0.00 USD | 6,950.00 USD | 0.00 USD |
| `7D` | `281.70` | 325,280.00 USD | 0.00 USD | 325,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `281.90` | 137,680.00 USD | 0.00 USD | 137,680.00 USD | 2,050.00 USD | 13,250.00 USD | 4,140.00 USD |
| `7D` | `282.20` | 127,860.00 USD | 0.00 USD | 127,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.30` | 118,230.00 USD | 0.00 USD | 118,230.00 USD | 8,260.00 USD | 9,080.00 USD | 0.00 USD |
| `1D` | `282.70` | 100,890.00 USD | 0.00 USD | 100,890.00 USD | 0.00 USD | 63,980.00 USD | 19.90 USD |
| `1D` | `283.10` | 36,890.00 USD | 0.00 USD | 36,890.00 USD | 14,930.00 USD | 20,630.00 USD | 35.95 USD |
| `7D` | `283.20` | 103,640.00 USD | 0.00 USD | 103,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD |
| `1D` | `283.50` | 1,290.00 USD | 0.00 USD | 1,290.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD |
| `1D` | `283.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.70` | 2,000.00 USD | 0.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.20` | 74,590.00 USD | 74,590.00 USD | 0.00 USD | 1,560.00 USD | 73,030.00 USD | 0.00 USD |
| `1D` | `284.30` | 4,200.00 USD | 4,200.00 USD | 0.00 USD | 3,780.00 USD | 397.40 USD | 26.15 USD |
| `1D` | `284.70` | 5,150.00 USD | 5,150.00 USD | 0.00 USD | 0.00 USD | 948.40 USD | 0.00 USD |
| `7D` | `284.70` | 431,170.00 USD | 431,170.00 USD | 0.00 USD | 0.00 USD | 356,580.00 USD | 0.00 USD |
| `1D` | `285.10` | 200,620.00 USD | 200,620.00 USD | 0.00 USD | 94,730.00 USD | 59,060.00 USD | 41,680.00 USD |
| `7D` | `285.20` | 843,250.00 USD | 843,250.00 USD | 0.00 USD | 66,830.00 USD | 262,020.00 USD | 83,240.00 USD |
| `1D` | `285.50` | 409,590.00 USD | 409,590.00 USD | 0.00 USD | 74,630.00 USD | 95,280.00 USD | 39,060.00 USD |
| `7D` | `285.70` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 50,130.00 USD | 136,910.00 USD | 0.00 USD |
| `1D` | `285.90` | 451,740.00 USD | 451,740.00 USD | 0.00 USD | 18,510.00 USD | 434.90 USD | 23,210.00 USD |
| `7D` | `286.20` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 1,200.00 USD | 77,190.00 USD | 0.00 USD |
| `1D` | `286.30` | 465,800.00 USD | 465,800.00 USD | 0.00 USD | 13,210.00 USD | 851.39 USD | 0.00 USD |
| `1D` | `286.70` | 503,350.00 USD | 503,350.00 USD | 0.00 USD | 2,290.00 USD | 5,130.00 USD | 30,140.00 USD |
| `7D` | `286.70` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 26,500.00 USD | 153,700.00 USD | 0.00 USD |
| `1D` | `287.10` | 663,660.00 USD | 663,660.00 USD | 0.00 USD | 33,320.00 USD | 39,160.00 USD | 87,820.00 USD |
| `7D` | `287.20` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 86,520.00 USD | 180,320.00 USD | 0.00 USD |
| `1D` | `287.50` | 770,330.00 USD | 770,330.00 USD | 0.00 USD | 23,660.00 USD | 26,220.00 USD | 56,790.00 USD |
| `7D` | `287.70` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 4,240.00 USD | 166,760.00 USD | 53,280.00 USD |
| `1D` | `287.90` | 842,230.00 USD | 842,230.00 USD | 0.00 USD | 13,160.00 USD | 14,490.00 USD | 44,250.00 USD |
| `7D` | `288.20` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 140,840.00 USD | 0.00 USD |
| `1D` | `288.30` | 942,950.00 USD | 942,950.00 USD | 0.00 USD | 73,330.00 USD | 22,330.00 USD | 5,060.00 USD |
| `1D` | `288.70` | 989,950.00 USD | 989,950.00 USD | 0.00 USD | 17,420.00 USD | 14,160.00 USD | 15,420.00 USD |
| `7D` | `288.70` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 123,610.00 USD | 1,140.00 USD | 80,970.00 USD |
| `1D` | `289.10` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 1,720.00 USD | 14,250.00 USD | 30,180.00 USD |
| `7D` | `289.20` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 1,170.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.50` | 1,150,000.00 USD | 1,150,000.00 USD | 0.00 USD | 20,690.00 USD | 25,800.00 USD | 68,790.00 USD |
| `7D` | `289.70` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 99,990.00 USD | 38,570.00 USD |
| `1D` | `289.90` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 76,110.00 USD | 40,970.00 USD | 35,950.00 USD |
| `7D` | `290.20` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 87,420.00 USD | 1,040.00 USD | 0.00 USD |
| `1D` | `290.30` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,110.00 USD | 72,370.00 USD | 27,990.00 USD |
| `1D` | `290.70` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 37,540.00 USD | 46,970.00 USD | 36,440.00 USD |
| `7D` | `290.70` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 0.00 USD |
| `1D` | `291.10` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 1,300.00 USD | 556.97 USD | 2.42 USD |
| `7D` | `291.20` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 24,680.00 USD | 1,810.00 USD | 0.00 USD |
| `1D` | `291.50` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 10,700.00 USD | 27,620.00 USD | 16.83 USD |
| `7D` | `291.70` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 2,710.00 USD | 114,180.00 USD | 19,430.00 USD |
| `1D` | `291.90` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 1,150.00 USD | 26,050.00 USD | 22,170.00 USD |
| `7D` | `292.20` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 2,560.00 USD | 133,170.00 USD | 36.98 USD |
| `1D` | `292.30` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 13,630.00 USD | 45,940.00 USD | 11,490.00 USD |
| `1D` | `292.70` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 21,130.00 USD | 28,380.00 USD | 5,790.00 USD |
| `7D` | `292.70` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 887.27 USD | 99,790.00 USD | 100.06 USD |
| `1D` | `293.10` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 20,520.00 USD | 14,170.00 USD | 13,290.00 USD |
| `7D` | `293.20` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 534.50 USD | 145,540.00 USD | 77.52 USD |
| `1D` | `293.50` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 16,630.00 USD | 44,050.00 USD | 27,680.00 USD |
| `7D` | `293.70` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 37,280.00 USD | 1,860.00 USD | 126.73 USD |
| `1D` | `293.90` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 85,250.00 USD | 9,280.00 USD | 46,730.00 USD |
| `7D` | `294.20` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 156,840.00 USD | 33,590.00 USD | 146,150.00 USD |
| `1D` | `294.30` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 6,700.00 USD | 22,460.00 USD | 44,850.00 USD |
| `1D` | `294.70` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 102,370.00 USD | 68,960.00 USD | 129,670.00 USD |
| `7D` | `294.70` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 77,920.00 USD | 93,810.00 USD | 89,160.00 USD |
| `1D` | `295.10` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 12,380.00 USD | 11,680.00 USD | 76,000.00 USD |
| `7D` | `295.20` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 48,390.00 USD | 79,610.00 USD | 214,270.00 USD |
| `1D` | `295.50` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 43,650.00 USD | 38,680.00 USD | 62,300.00 USD |
| `7D` | `295.70` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 176,660.00 USD | 91,790.00 USD | 216,750.00 USD |
| `1D` | `295.90` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 61,360.00 USD | 33,480.00 USD | 53,790.00 USD |
| `7D` | `296.20` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 77,740.00 USD | 90,470.00 USD | 135,690.00 USD |
| `1D` | `296.30` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 74,380.00 USD | 87,860.00 USD | 27,160.00 USD |
| `1D` | `296.70` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 21,800.00 USD | 20,740.00 USD | 62,270.00 USD |
| `7D` | `296.70` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 119,500.00 USD | 79,730.00 USD | 163,890.00 USD |
| `1D` | `297.10` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 52,330.00 USD | 1,470.00 USD | 40,480.00 USD |
| `7D` | `297.20` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 92,010.00 USD | 51,810.00 USD | 27,830.00 USD |
| `1D` | `297.50` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 10,510.00 USD | 10,470.00 USD | 27,500.00 USD |
| `7D` | `297.70` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 1,640.00 USD | 61,080.00 USD | 34,710.00 USD |
| `1D` | `297.90` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 15,610.00 USD | 7,250.00 USD | 16,120.00 USD |
| `7D` | `298.20` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 80,030.00 USD | 81,680.00 USD | 92,240.00 USD |
| `1D` | `298.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 56,090.00 USD | 1,860.00 USD | 93,920.00 USD |
| `1D` | `298.70` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 23,390.00 USD | 96.56 USD | 80,700.00 USD |
| `7D` | `298.70` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 69,820.00 USD | 12,660.00 USD | 31,540.00 USD |
| `1D` | `299.10` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 8,370.00 USD | 7,580.00 USD | 26,320.00 USD |
| `7D` | `299.20` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 2,350.00 USD | 14,800.00 USD | 85,830.00 USD |
| `1D` | `299.50` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 35,730.00 USD | 13,630.00 USD | 19,140.00 USD |
| `7D` | `299.70` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 7,110.00 USD | 20,230.00 USD | 19,830.00 USD |
| `1D` | `299.90` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 3,720.00 USD | 12,290.00 USD | 30,240.00 USD |
| `7D` | `300.20` | 5,940,000.00 USD | 5,940,000.00 USD | 0.00 USD | 52,360.00 USD | 3,070.00 USD | 16.16 USD |
| `1D` | `300.30` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 31,890.00 USD | 30,720.00 USD | 42,600.00 USD |
| `1D` | `300.70` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 10,320.00 USD | 669.99 USD | 17,200.00 USD |
| `7D` | `300.70` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 25,350.00 USD | 71,770.00 USD | 19,750.00 USD |
| `1D` | `301.10` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 322.75 USD | 15,710.00 USD | 29,320.00 USD |
| `7D` | `301.20` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 49,160.00 USD | 41,600.00 USD | 119,540.00 USD |
| `1D` | `301.50` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 19,490.00 USD | 99.63 USD | 36,290.00 USD |
| `7D` | `301.70` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 62,390.00 USD | 146,640.00 USD | 59,520.00 USD |
| `1D` | `301.90` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 21,000.00 USD | 35,690.00 USD | 10,340.00 USD |
| `7D` | `302.20` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 53,220.00 USD | 156,580.00 USD | 26,260.00 USD |
| `1D` | `302.30` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 5,200.00 USD | 4,820.00 USD | 17,560.00 USD |
| `1D` | `302.70` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 14,410.00 USD | 11,570.00 USD | 34,800.00 USD |
| `7D` | `302.70` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 71,700.00 USD | 95,350.00 USD | 41,780.00 USD |
| `1D` | `303.10` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 20,780.00 USD | 1,680.00 USD | 9,370.00 USD |
| `7D` | `303.20` | 7,020,000.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 40,690.00 USD | 184.71 USD |
| `1D` | `303.50` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 151.00 USD | 1,800.00 USD | 1.44 USD |
| `7D` | `303.70` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 17,370.00 USD | 9,400.00 USD | 24,690.00 USD |
| `1D` | `303.90` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 21,670.00 USD | 1,810.00 USD | 18,760.00 USD |
| `7D` | `304.20` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 5,440.00 USD | 6,090.00 USD | 21,420.00 USD |
| `1D` | `304.30` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 355.83 USD | 2,370.00 USD | 21,660.00 USD |
| `1D` | `304.70` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 9,880.00 USD | 1,650.00 USD | 44,520.00 USD |
| `7D` | `304.70` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 4,020.00 USD | 11,790.00 USD | 2,060.00 USD |
| `1D` | `305.10` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 9,500.00 USD | 7,040.00 USD | 4,030.00 USD |
| `7D` | `305.20` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 145,590.00 USD | 128,470.00 USD | 91,560.00 USD |
| `1D` | `305.50` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 7,620.00 USD | 1,640.00 USD | 1,490.00 USD |
| `7D` | `305.70` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 133,080.00 USD | 32,810.00 USD | 44,590.00 USD |
| `1D` | `305.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 9,020.00 USD | 5,650.00 USD | 5,880.00 USD |
| `7D` | `306.20` | 7,870,000.00 USD | 7,870,000.00 USD | 0.00 USD | 30,110.00 USD | 96,840.00 USD | 46,060.00 USD |
| `1D` | `306.30` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 6,970.00 USD | 317.96 USD | 6,360.00 USD |
| `1D` | `306.70` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 4,670.00 USD | 23,710.00 USD | 9,500.00 USD |
| `7D` | `306.70` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 27,190.00 USD | 44,920.00 USD | 87,760.00 USD |
| `1D` | `307.10` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 32,650.00 USD | 36,950.00 USD | 22,740.00 USD |
| `7D` | `307.20` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 79,230.00 USD | 117,920.00 USD | 106,420.00 USD |
| `1D` | `307.50` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 18,940.00 USD | 38,970.00 USD | 12,910.00 USD |
| `7D` | `307.70` | 8,610,000.00 USD | 8,610,000.00 USD | 0.00 USD | 100,620.00 USD | 122,760.00 USD | 51,910.00 USD |
| `1D` | `307.90` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 26,540.00 USD | 30,230.00 USD | 20,230.00 USD |
| `7D` | `308.20` | 9,030,000.00 USD | 9,030,000.00 USD | 0.00 USD | 181,990.00 USD | 90,920.00 USD | 151,000.00 USD |
| `1D` | `308.30` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 16,840.00 USD | 7,470.00 USD | 4,380.00 USD |
| `1D` | `308.70` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 5,270.00 USD | 204.90 USD | 3,480.00 USD |
| `7D` | `308.70` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 84,590.00 USD | 38,760.00 USD | 15,430.00 USD |
| `1D` | `309.10` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 11,490.00 USD | 6,090.00 USD | 4,330.00 USD |
| `7D` | `309.20` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 44,600.00 USD | 39,620.00 USD | 51,960.00 USD |
| `1D` | `309.50` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 6,810.00 USD | 12,820.00 USD | 2,060.00 USD |
| `7D` | `309.70` | 9,650,000.00 USD | 9,650,000.00 USD | 0.00 USD | 41,230.00 USD | 149,610.00 USD | 151,150.00 USD |
| `1D` | `309.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 12,550.00 USD | 14.55 USD | 6,290.00 USD |
| `7D` | `310.20` | 9,810,000.00 USD | 9,810,000.00 USD | 0.00 USD | 34,250.00 USD | 63,520.00 USD | 62,810.00 USD |
| `1D` | `310.30` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 112.30 USD | 6,500.00 USD | 9,560.00 USD |
| `1D` | `310.70` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 2,320.00 USD | 2.98 USD |
| `7D` | `310.70` | 10,030,000.00 USD | 10,030,000.00 USD | 0.00 USD | 93,490.00 USD | 103,280.00 USD | 25,780.00 USD |
| `1D` | `311.10` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 0.82 USD |
| `7D` | `311.20` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 74,870.00 USD | 66,040.00 USD | 63,830.00 USD |
| `1D` | `311.50` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 7,350.00 USD | 6,560.00 USD | 6.94 USD |
| `7D` | `311.70` | 10,340,000.00 USD | 10,340,000.00 USD | 0.00 USD | 65,050.00 USD | 11,430.00 USD | 25,590.00 USD |
| `1D` | `311.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 296.02 USD | 4,070.00 USD |
| `7D` | `312.20` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 24,190.00 USD |
| `1D` | `312.30` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 6,410.00 USD | 9,270.00 USD | 12,310.00 USD |
| `1D` | `312.70` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 13,680.00 USD | 346.79 USD | 4,360.00 USD |
| `7D` | `312.70` | 10,470,000.00 USD | 10,470,000.00 USD | 0.00 USD | 8,290.00 USD | 19,350.00 USD | 28,260.00 USD |
| `1D` | `313.10` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 8,630.00 USD | 0.96 USD |
| `7D` | `313.20` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 64,510.00 USD | 19,820.00 USD | 52,710.00 USD |
| `1D` | `313.50` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 7,160.00 USD | 2,890.00 USD | 2,580.00 USD |
| `7D` | `313.70` | 10,690,000.00 USD | 10,690,000.00 USD | 0.00 USD | 42,720.00 USD | 8,670.00 USD | 23,110.00 USD |
| `1D` | `313.90` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 0.00 USD | 239.05 USD | 0.00 USD |
| `7D` | `314.20` | 10,750,000.00 USD | 10,750,000.00 USD | 0.00 USD | 15,430.00 USD | 669.97 USD | 45,060.00 USD |
| `1D` | `314.30` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 3,420.00 USD |
| `1D` | `314.70` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 32.00 USD | 3,720.00 USD | 8,330.00 USD |
| `7D` | `314.70` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 38,580.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `315.10` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 6,440.00 USD |
| `7D` | `315.20` | 10,820,000.00 USD | 10,820,000.00 USD | 0.00 USD | 24,720.00 USD | 547.95 USD | 3.94 USD |
| `1D` | `315.50` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 3,750.00 USD | 144.50 USD | 5,230.00 USD |
| `7D` | `315.70` | 10,900,000.00 USD | 10,900,000.00 USD | 0.00 USD | 9,200.00 USD | 42,570.00 USD | 30,070.00 USD |
| `1D` | `315.90` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `316.20` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 38,840.00 USD | 20,190.00 USD | 43,420.00 USD |
| `1D` | `316.30` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 128.70 USD | 0.00 USD | 5,590.00 USD |
| `1D` | `316.70` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 12,960.00 USD | 3,610.00 USD | 10,200.00 USD |
| `7D` | `316.70` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 18,110.00 USD | 20,380.00 USD | 18,380.00 USD |
| `1D` | `317.00` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 2,160.00 USD | 0.00 USD |
| `7D` | `317.20` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 15,590.00 USD | 1,420.00 USD | 69.80 USD |
| `7D` | `317.70` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 620.15 USD | 721.55 USD | 67.28 USD |
| `7D` | `318.20` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 23,930.00 USD | 13,700.00 USD | 32,210.00 USD |
| `7D` | `318.70` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 11,230.00 USD | 44,600.00 USD | 37,840.00 USD |
| `7D` | `319.20` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 366.90 USD | 18,060.00 USD | 49.12 USD |
| `7D` | `319.70` | 11,280,000.00 USD | 11,280,000.00 USD | 0.00 USD | 936.82 USD | 12,700.00 USD | 0.00 USD |
| `7D` | `320.20` | 11,380,000.00 USD | 11,380,000.00 USD | 0.00 USD | 49,670.00 USD | 19,480.00 USD | 30,570.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `306.92M` | Total OI Tokens: `1,082,896.6 BCH`
  * 1h OI Change: `-0.14%` | 4h OI Change: `+5.37%` | 24h OI Change: `-1.57%`
  * Exchange Breakdown: Binance=`89.92M` | Bybit=`38.14M` | OKX=`24.09M` | Hyperliquid=`7.24M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `12.63K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0053%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0070%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `44.94%` | `55.06%` | `0.82` | 2,720,000.00 USD |
| `15M` | `Binance` | `51.29%` | `48.71%` | `1.05` | 880,700.00 USD |
| `15M` | `OKX` | `52.46%` | `47.54%` | `1.10` | 417,020.00 USD |
| `15M` | `Bybit` | `42.87%` | `57.13%` | `0.75` | 219,980.00 USD |
| `15M` | `KuCoin` | `52.98%` | `47.02%` | `1.13` | 46,300.00 USD |
| `15M` | `Gate` | `35.92%` | `64.08%` | `0.56` | 288,540.00 USD |
| `15M` | `Bitget` | `45.51%` | `54.49%` | `0.84` | 59,850.00 USD |
| `15M` | `BingX` | `48.57%` | `51.43%` | `0.94` | 516,870.00 USD |
| `15M` | `MEXC` | `5.65%` | `94.35%` | `0.06` | 120,730.00 USD |
| `15M` | `Bitunix` | `45.81%` | `54.19%` | `0.85` | 37,930.00 USD |
| `15M` | `Hyperliquid` | `4.88%` | `95.12%` | `0.05` | 59,370.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `19.05%` | `80.95%` | `0.24` | 62,420.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `92.94%` | `7.06%` | `13.16` | 8,590.00 USD |
| `15M` | `HTX` | `96.3%` | `3.7%` | `26.03` | 6,390.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `95.42%` | `4.58%` | `20.83` | 243.81 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `63.57%` | `36.43%` | `1.74` | 31.56 USD |
| `15M` | `Whale Positions` | `51.29%` | `48.71%` | `1.05` | 880,700.00 USD |
| `15M` | `Global Accounts` | `44.94%` | `55.06%` | `0.82` | 2,720,000.00 USD |
| `1H` | `BCH` | `44.23%` | `55.77%` | `0.79` | 11,140,000.00 USD |
| `1H` | `Binance` | `44.34%` | `55.66%` | `0.80` | 3,750,000.00 USD |
| `1H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 1,570,000.00 USD |
| `1H` | `Bybit` | `47.34%` | `52.66%` | `0.90` | 875,150.00 USD |
| `1H` | `KuCoin` | `50.53%` | `49.47%` | `1.02` | 118,700.00 USD |
| `1H` | `Gate` | `46.02%` | `53.98%` | `0.85` | 1,260,000.00 USD |
| `1H` | `Bitget` | `35.92%` | `64.08%` | `0.56` | 356,020.00 USD |
| `1H` | `BingX` | `43.21%` | `56.79%` | `0.76` | 1,890,000.00 USD |
| `1H` | `MEXC` | `30.08%` | `69.92%` | `0.43` | 282,740.00 USD |
| `1H` | `Bitunix` | `39.94%` | `60.06%` | `0.67` | 384,990.00 USD |
| `1H` | `Hyperliquid` | `13.27%` | `86.73%` | `0.15` | 122,460.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.68%` | `57.32%` | `0.74` | 403,100.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.49%` | `2.51%` | `38.84` | 66,020.00 USD |
| `1H` | `HTX` | `69.62%` | `30.38%` | `2.29` | 18,300.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `57.08%` | `42.92%` | `1.33` | 34,460.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `78%` | `22%` | `3.55` | 1,270.00 USD |
| `1H` | `Whale Positions` | `44.34%` | `55.66%` | `0.80` | 3,750,000.00 USD |
| `1H` | `Global Accounts` | `44.23%` | `55.77%` | `0.79` | 11,140,000.00 USD |
| `4H` | `BCH` | `48.29%` | `51.71%` | `0.93` | 59,000,000.00 USD |
| `4H` | `Binance` | `45.72%` | `54.28%` | `0.84` | 19,550,000.00 USD |
| `4H` | `OKX` | `47.72%` | `52.28%` | `0.91` | 7,840,000.00 USD |
| `4H` | `Bybit` | `53.05%` | `46.95%` | `1.13` | 4,780,000.00 USD |
| `4H` | `KuCoin` | `45.84%` | `54.16%` | `0.85` | 496,250.00 USD |
| `4H` | `Gate` | `46.87%` | `53.13%` | `0.88` | 4,870,000.00 USD |
| `4H` | `Bitget` | `53.73%` | `46.27%` | `1.16` | 1,920,000.00 USD |
| `4H` | `BingX` | `41.37%` | `58.63%` | `0.71` | 9,820,000.00 USD |
| `4H` | `MEXC` | `52.07%` | `47.93%` | `1.09` | 2,650,000.00 USD |
| `4H` | `Bitunix` | `55.85%` | `44.15%` | `1.27` | 1,810,000.00 USD |
| `4H` | `Hyperliquid` | `42.73%` | `57.27%` | `0.75` | 1,500,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.82%` | `50.18%` | `0.99` | 1,810,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `96.07%` | `3.93%` | `24.45` | 1,590,000.00 USD |
| `4H` | `HTX` | `50.46%` | `49.54%` | `1.02` | 115,410.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `54.04%` | `45.96%` | `1.18` | 60,530.00 USD |
| `4H` | `Aster` | `64.21%` | `35.79%` | `1.79` | 145,730.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `70.33%` | `29.67%` | `2.37` | 23,500.00 USD |
| `4H` | `Whale Positions` | `45.72%` | `54.28%` | `0.84` | 19,550,000.00 USD |
| `4H` | `Global Accounts` | `48.29%` | `51.71%` | `0.93` | 59,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `277.43` | `276.49` | `277.43` | `277.51` | `275.76` | 760,717.24 USD | 265,897.12 USD | 494,820.12 USD | -228,923.01 USD | `-30.09%` | `19B / 60S` |
| `0:00 UTC` | `278.95` | `278.11` | `278.95` | `279.11` | `276.01` | 1,117,022.83 USD | 460,337.30 USD | 656,685.53 USD | -196,348.23 USD | `-17.58%` | `14B / 26S` |
| `5:00 UTC` | `278.75` | `278.95` | `278.75` | `279.99` | `277.87` | 899,043.00 USD | 507,720.36 USD | 391,322.65 USD | 116,397.71 USD | `+12.95%` | `23B / 14S` |
| `0:00 UTC` | `281.80` | `281.23` | `281.80` | `282.56` | `279.38` | 1,860,973.61 USD | 1,019,031.48 USD | 841,942.13 USD | 177,089.35 USD | `+9.52%` | `29B / 17S` |
| `5:00 UTC` | `282.40` | `283.39` | `282.40` | `284.76` | `281.82` | 2,261,635.40 USD | 1,044,285.27 USD | 1,217,350.14 USD | -173,064.87 USD | `-7.65%` | `26B / 23S` |
| `0:00 UTC` | `287.03` | `284.86` | `287.03` | `287.15` | `282.35` | 3,497,591.91 USD | 1,841,198.98 USD | 1,656,392.94 USD | 184,806.04 USD | `+5.28%` | `24B / 10S` |
| `5:00 UTC` | `284.49` | `285.18` | `284.49` | `286.67` | `284.13` | 976,529.89 USD | 414,772.25 USD | 561,757.64 USD | -146,985.38 USD | `-15.05%` | `8B / 33S` |
| `0:00 UTC` | `284.00` | `284.42` | `284.00` | `285.15` | `283.77` | 825,459.63 USD | 394,600.86 USD | 430,858.77 USD | -36,257.91 USD | `-4.39%` | `20B / 24S` |
| `5:00 UTC` | `284.75` | `284.10` | `284.75` | `284.97` | `283.36` | 1,321,321.21 USD | 645,681.70 USD | 675,639.51 USD | -29,957.81 USD | `-2.27%` | `33B / 48S` |
| `0:00 UTC` | `283.69` | `283.62` | `283.69` | `283.75` | `283.49` | 42,298.05 USD | 21,185.73 USD | 21,112.33 USD | 73.40 USD | `+0.17%` | `4B / 6S` |

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
| `5m` | -5,970.00 USD | 102,120.00 USD | **`ACCUMULATION`** |
| `15m` | -6,540.00 USD | 37,570.00 USD | **`ACCUMULATION`** |
| `30m` | 56,290.00 USD | -101,090.00 USD | **`DISTRIBUTION`** |
| `1h` | 340,090.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 721,810.00 USD | -369,180.00 USD | **`ACCUMULATION`** |
| `4h` | 1,030,000.00 USD | 1,100,000.00 USD | **`ACCUMULATION`** |
| `6h` | 312,840.00 USD | -1,480,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 735,040.00 USD | -2,560,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -201,430.00 USD | -901,500.00 USD | **`DISTRIBUTION`** |
| `24h` | -34,720.00 USD | -4,920,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -990,170.00 USD | -16,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,460,000.00 USD | -138,170,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-5.97K` | 15m=`-6.54K` | 1h=`+340.09K` | 24h=`-34.72K`
* Futures Capital Netflows: 5m=`+102.12K` | 15m=`+37.57K` | 1h=`-1.08M` | 24h=`-4.92M`
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
  * `2026-10-30 09:51:10 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:30:10 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:29:10 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:31:10 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:31:10 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:31:10 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `269.27` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `267.20` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `274.45`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `280.67` (Risk Distance: `2.07` pts)
  * +2.5R Take Profit: `273.42`
  * Mathematical Lot Sizing: **`4.83 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`285.52`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
