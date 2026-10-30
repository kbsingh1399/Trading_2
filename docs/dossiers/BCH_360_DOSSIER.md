# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 10:07:34 IST` (`2026-10-30 04:37:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `283.86` | **Live Ask Quote**: `284.44` | **Mid Price**: `284.15`
- **Spread Points**: `580.00` | **Spread BPS**: `20.41 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `273.71` | VWAP Z-Score: `+1.81` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.31` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `63.58` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `290.57` | Lower -3.00σ Band: `256.84`
  * Upper +2.51σ Band: `287.82` | Lower -2.51σ Band: `259.60`
  * Upper +2.01σ Band: `285.01` | Lower -2.01σ Band: `262.41`
  * Upper +2.00σ Band: `284.95` | Lower -2.00σ Band: `262.46`
  * Upper +1.28σ Band: `280.90` | Lower -1.28σ Band: `266.51`
  * Upper +1.00σ Band: `279.33` | Lower -1.00σ Band: `268.09`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`280.26` | EMA-20=`277.82` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`278.25` (Slope: `+0.0000`) | EMA-100=`280.21`
  * Institutional Anchors: EMA-144=`281.37` | EMA-200=`282.81` (Slope: `-0.2094`) | EMA-233=`283.94`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.60` (Distance: `+1.99%`)
  * Point of Control (POC) = `276.23` (Distance: `+2.87%`)
  * Value Area Low (VAL) = `269.75` (Distance: `+5.34%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`285.29` | Low=`283.01`
  * New York Session (13:00-21:00 UTC): High=`285.85` | Low=`282.45`
  * Initial Balance (First Hour): IB High=`285.00` | IB Low=`283.30`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `283.01` - `285.29`
  * Optimal Trade Entry (OTE 0.705): `284.72`
  * Structural Invalidation Anchor (0.786): `286.42`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `285.79` | `285.87` | `284.35` | `284.47` | `1,141` | 325,290.27 USD | -100,379.08 USD | `-30.86%` | -1,922,938.05 USD | `-0.55` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `284.48` | `284.94` | `284.12` | `284.79` | `919` | 261,441.33 USD | 6,709.63 USD | `+2.57%` | -1,916,228.42 USD | `+0.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `284.79` | `284.80` | `284.57` | `284.79` | `99` | 28,156.74 USD | 782.34 USD | `+2.78%` | -1,915,446.08 USD | `+0.03` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `283.99` | `287.12` | `282.33` | `285.86` | `12,279` | 3,497,591.91 USD | 184,806.04 USD | `+5.28%` | -1,823,413.77 USD | `+0.42` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `285.86` | `286.67` | `284.12` | `284.79` | `3,424` | 976,529.89 USD | -146,985.38 USD | `-15.05%` | -1,970,399.15 USD | `-0.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `284.79` | `284.80` | `284.57` | `284.79` | `99` | 28,156.74 USD | 782.34 USD | `+2.78%` | -1,969,616.81 USD | `-0.01` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `271.56` | `279.99` | `269.63` | `276.08` | `23,457` | 6,482,271.13 USD | -1,215,804.23 USD | `-18.76%` | -2,230,015.40 USD | `-1.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `276.08` | `284.75` | `276.00` | `283.99` | `21,838` | 6,138,674.85 USD | -75,926.04 USD | `-1.24%` | -2,305,941.44 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `283.99` | `287.12` | `282.33` | `284.77` | `15,801` | 4,502,135.01 USD | 38,508.45 USD | `+0.86%` | -2,267,432.99 USD | `+0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.77` | `15,801` | 4,502,135.01 USD | 38,508.45 USD | `+0.86%` | -1,835,874.55 USD | `+0.29` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | 1,085,885.17 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -386,016.76 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.77` | `15,801` | 4,502,135.01 USD | 38,508.45 USD | `+0.86%` | -1,835,874.55 USD | `+0.29` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`284.15`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1966` | `0x12d2...f97f` | `LONG` | 1,032,530.99 USD | `3,627,243,000,000.00` | `303.26` | `284.29` | `0.000000` | -67,468.35 USD | `-6.53%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `286.43` | 7,351.23 USD | `-` | `NEWS_INTEL` | `-` | #BCH Whale SELL: 7.35K USD at 286.4300 USD [API] | `2026-10-29 01:10:20` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`265.44` (Vol: 300,100.00 USD, Dist: `--6.82%`)
  * 48H Horizon: Short MP=`297.02` (Vol: 227,200.00 USD, Dist: `+4.27%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.79%`)
  * 3D Horizon: Short MP=`297.02` (Vol: 227,200.00 USD, Dist: `+4.27%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.79%`)
  * 7D Horizon: Short MP=`288.79` (Vol: 247,200.00 USD, Dist: `+1.38%`) | Long MP=`265.52` (Vol: 300,100.00 USD, Dist: `--6.79%`)
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
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 45,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 21,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `240.90` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 330.05 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.40` | 11,710,000.00 USD | 11,710,000.00 USD | 7,150.00 USD | 0.00 USD | 22.63 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 20,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.90` | 11,700,000.00 USD | 11,700,000.00 USD | 19,010.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 11,670,000.00 USD | 11,670,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.90` | 11,620,000.00 USD | 11,620,000.00 USD | 0.00 USD | 5,680.00 USD | 0.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.40` | 11,610,000.00 USD | 11,610,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 3,380.00 USD | 19,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.90` | 11,600,000.00 USD | 11,600,000.00 USD | 781.30 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 16,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.90` | 11,580,000.00 USD | 11,580,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.40` | 11,560,000.00 USD | 11,560,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 12,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.90` | 11,540,000.00 USD | 11,540,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.40` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 11,510,000.00 USD | 11,510,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `246.80` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 6.81 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.90` | 11,480,000.00 USD | 11,480,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `247.20` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 3,690.00 USD | 7.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.40` | 11,470,000.00 USD | 11,470,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 699.44 USD | 11,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `247.60` | 4,830,000.00 USD | 4,830,000.00 USD | 528.00 USD | 0.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.90` | 11,440,000.00 USD | 11,440,000.00 USD | 789.37 USD | 4,610.00 USD | 8.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.00` | 4,820,000.00 USD | 4,820,000.00 USD | 10,640.00 USD | 619.60 USD | 24,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.40` | 4,790,000.00 USD | 4,790,000.00 USD | 7,480.00 USD | 4,690.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 11,430,000.00 USD | 11,430,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `248.80` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 1,750.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.90` | 11,380,000.00 USD | 11,380,000.00 USD | 37,420.00 USD | 28,490.00 USD | 32,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `249.20` | 4,750,000.00 USD | 4,750,000.00 USD | 3,960.00 USD | 12,400.00 USD | 17,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.40` | 11,290,000.00 USD | 11,290,000.00 USD | 49,060.00 USD | 28,020.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 10,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `249.60` | 4,720,000.00 USD | 4,720,000.00 USD | 9,040.00 USD | 1,710.00 USD | 3,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.90` | 11,210,000.00 USD | 11,210,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.00` | 4,700,000.00 USD | 4,700,000.00 USD | 13,540.00 USD | 1,340.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.40` | 4,690,000.00 USD | 4,690,000.00 USD | 9,230.00 USD | 5,500.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 11,100,000.00 USD | 11,100,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 9,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.80` | 4,670,000.00 USD | 4,670,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.90` | 11,020,000.00 USD | 11,020,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.20` | 4,640,000.00 USD | 4,640,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.40` | 10,930,000.00 USD | 10,930,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 7,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.60` | 4,550,000.00 USD | 4,550,000.00 USD | 31,800.00 USD | 51,410.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.90` | 10,760,000.00 USD | 10,760,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.00` | 4,450,000.00 USD | 4,450,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.40` | 4,380,000.00 USD | 4,380,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 10,590,000.00 USD | 10,590,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 7,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.80` | 4,360,000.00 USD | 4,360,000.00 USD | 18,060.00 USD | 6,420.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.90` | 10,450,000.00 USD | 10,450,000.00 USD | 29,220.00 USD | 19,580.00 USD | 12.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.20` | 4,330,000.00 USD | 4,330,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.40` | 10,400,000.00 USD | 10,400,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.60` | 4,310,000.00 USD | 4,310,000.00 USD | 15,820.00 USD | 13,480.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.90` | 10,280,000.00 USD | 10,280,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 4,270,000.00 USD | 4,270,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 4,250,000.00 USD | 4,250,000.00 USD | 134.35 USD | 2,130.00 USD | 10.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 10,220,000.00 USD | 10,220,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 6,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 4,250,000.00 USD | 4,250,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.90` | 10,130,000.00 USD | 10,130,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 4,240,000.00 USD | 4,240,000.00 USD | 9,500.00 USD | 6,590.00 USD | 3.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.40` | 10,080,000.00 USD | 10,080,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.60` | 4,220,000.00 USD | 4,220,000.00 USD | 8,470.00 USD | 8,330.00 USD | 2,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.90` | 10,000,000.00 USD | 10,000,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 4,210,000.00 USD | 4,210,000.00 USD | 11,080.00 USD | 321.10 USD | 22.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 4,190,000.00 USD | 4,190,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 9,940,000.00 USD | 9,940,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 5,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 4,170,000.00 USD | 4,170,000.00 USD | 5,560.00 USD | 928.93 USD | 0.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.90` | 9,810,000.00 USD | 9,810,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 4,170,000.00 USD | 4,170,000.00 USD | 5,380.00 USD | 0.00 USD | 7,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.40` | 9,710,000.00 USD | 9,710,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 366.42 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.60` | 4,150,000.00 USD | 4,150,000.00 USD | 1,190.00 USD | 741.83 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.90` | 9,640,000.00 USD | 9,640,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 4,140,000.00 USD | 4,140,000.00 USD | 5,060.00 USD | 2,390.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 4,130,000.00 USD | 4,130,000.00 USD | 2,130.00 USD | 3,450.00 USD | 5,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 9,580,000.00 USD | 9,580,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 278.15 USD | 2,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 4,120,000.00 USD | 4,120,000.00 USD | 2,120.00 USD | 3,750.00 USD | 5,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.90` | 9,350,000.00 USD | 9,350,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 4,110,000.00 USD | 4,110,000.00 USD | 13,320.00 USD | 3,850.00 USD | 7,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.40` | 9,250,000.00 USD | 9,250,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 4,090,000.00 USD | 4,090,000.00 USD | 5,330.00 USD | 4,700.00 USD | 7,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.90` | 9,190,000.00 USD | 9,190,000.00 USD | 19,140.00 USD | 12,520.00 USD | 109.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 4,070,000.00 USD | 4,070,000.00 USD | 15,300.00 USD | 14,890.00 USD | 23,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 4,010,000.00 USD | 4,010,000.00 USD | 2,940.00 USD | 9,390.00 USD | 10,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 9,160,000.00 USD | 9,160,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 3,990,000.00 USD | 3,990,000.00 USD | 266.79 USD | 18,270.00 USD | 13,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.90` | 9,040,000.00 USD | 9,040,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 3,960,000.00 USD | 3,960,000.00 USD | 7,970.00 USD | 18,100.00 USD | 30,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.40` | 8,920,000.00 USD | 8,920,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 3,900,000.00 USD | 3,900,000.00 USD | 7,930.00 USD | 1,290.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.90` | 8,820,000.00 USD | 8,820,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 3,870,000.00 USD | 3,870,000.00 USD | 4,560.00 USD | 4,320.00 USD | 13,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 3,850,000.00 USD | 3,850,000.00 USD | 9,000.00 USD | 4,480.00 USD | 20.31 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 8,660,000.00 USD | 8,660,000.00 USD | 44,640.00 USD | 52,560.00 USD | 75.21 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.80` | 3,840,000.00 USD | 3,840,000.00 USD | 366.04 USD | 14,220.00 USD | 21.99 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.90` | 8,570,000.00 USD | 8,570,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 3,820,000.00 USD | 3,820,000.00 USD | 9,680.00 USD | 4,510.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.40` | 8,420,000.00 USD | 8,420,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 3,790,000.00 USD | 3,790,000.00 USD | 1,010.00 USD | 7,000.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.90` | 8,240,000.00 USD | 8,240,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 3,770,000.00 USD | 3,770,000.00 USD | 1,210.00 USD | 4,040.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 3,740,000.00 USD | 3,740,000.00 USD | 1,660.00 USD | 920.03 USD | 13.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 7,800,000.00 USD | 7,800,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.80` | 3,740,000.00 USD | 3,740,000.00 USD | 28,700.00 USD | 4,430.00 USD | 75,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.90` | 7,680,000.00 USD | 7,680,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 3,630,000.00 USD | 3,630,000.00 USD | 34,820.00 USD | 13,080.00 USD | 2,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.40` | 7,550,000.00 USD | 7,550,000.00 USD | 134,720.00 USD | 59,500.00 USD | 182,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.60` | 3,580,000.00 USD | 3,580,000.00 USD | 19,750.00 USD | 38,130.00 USD | 77,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.90` | 7,170,000.00 USD | 7,170,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 3,450,000.00 USD | 3,450,000.00 USD | 51,150.00 USD | 7,940.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 3,380,000.00 USD | 3,380,000.00 USD | 41,560.00 USD | 28,430.00 USD | 10,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 6,840,000.00 USD | 6,840,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.80` | 3,300,000.00 USD | 3,300,000.00 USD | 28,890.00 USD | 22,040.00 USD | 80,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.90` | 6,360,000.00 USD | 6,360,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 3,170,000.00 USD | 3,170,000.00 USD | 16,540.00 USD | 8,620.00 USD | 44,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.40` | 5,880,000.00 USD | 5,880,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.60` | 3,100,000.00 USD | 3,100,000.00 USD | 30,750.00 USD | 80,200.00 USD | 23,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.90` | 5,460,000.00 USD | 5,460,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 2,970,000.00 USD | 2,970,000.00 USD | 104,590.00 USD | 112,690.00 USD | 52,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 2,700,000.00 USD | 2,700,000.00 USD | 90,320.00 USD | 130,660.00 USD | 32,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 4,840,000.00 USD | 4,840,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.80` | 2,440,000.00 USD | 2,440,000.00 USD | 100,660.00 USD | 65,950.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.90` | 4,240,000.00 USD | 4,240,000.00 USD | 261,830.00 USD | 135,480.00 USD | 103,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 2,220,000.00 USD | 2,220,000.00 USD | 21,310.00 USD | 34,490.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.40` | 3,740,000.00 USD | 3,740,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.60` | 2,150,000.00 USD | 2,150,000.00 USD | 34,010.00 USD | 20,280.00 USD | 46,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.90` | 3,170,000.00 USD | 3,170,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 2,050,000.00 USD | 2,050,000.00 USD | 45,580.00 USD | 25,140.00 USD | 141,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 1,840,000.00 USD | 1,840,000.00 USD | 129,180.00 USD | 6,950.00 USD | 59,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 2,960,000.00 USD | 2,960,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.80` | 1,640,000.00 USD | 1,640,000.00 USD | 56,030.00 USD | 7,500.00 USD | 29,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.90` | 2,820,000.00 USD | 2,820,000.00 USD | 328,250.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 1,550,000.00 USD | 1,550,000.00 USD | 56,240.00 USD | 7,760.00 USD | 160,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.40` | 2,470,000.00 USD | 2,470,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.60` | 1,320,000.00 USD | 1,320,000.00 USD | 102,160.00 USD | 15,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.90` | 2,320,000.00 USD | 2,320,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 1,210,000.00 USD | 1,210,000.00 USD | 131,180.00 USD | 4,060.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 1,060,000.00 USD | 1,060,000.00 USD | 69,420.00 USD | 368.00 USD | 19,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 1,860,000.00 USD | 1,860,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.80` | 971,800.00 USD | 971,800.00 USD | 85,930.00 USD | 7,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.90` | 1,580,000.00 USD | 1,580,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 878,540.00 USD | 878,540.00 USD | 65,470.00 USD | 73.70 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.40` | 1,410,000.00 USD | 1,410,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 813,000.00 USD | 813,000.00 USD | 229,980.00 USD | 0.00 USD | 111,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.90` | 872,180.00 USD | 872,180.00 USD | 375,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.00` | 471,100.00 USD | 471,100.00 USD | 190,550.00 USD | 0.00 USD | 12.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 280,540.00 USD | 280,540.00 USD | 209,960.00 USD | 0.00 USD | 10.80 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 496,740.00 USD | 496,740.00 USD | 496,740.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.80` | 70,560.00 USD | 70,560.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.90` | 348,470.00 USD | 348,470.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `274.90` | 696,940.00 USD | 696,940.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.20` | 25,430.00 USD | 25,430.00 USD | 25,410.00 USD | 0.00 USD | 13.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `275.40` | 700,470.00 USD | 700,470.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `275.90` | 703,030.00 USD | 703,030.00 USD | 2,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.40` | 809,250.00 USD | 809,250.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `276.90` | 853,930.00 USD | 853,930.00 USD | 44,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `277.20` | 301.20 USD | 301.20 USD | 301.20 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.40` | 917,220.00 USD | 917,220.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `277.60` | 305.64 USD | 305.64 USD | 0.00 USD | 0.00 USD | 4.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `277.90` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 85,690.00 USD | 120.11 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.40` | 1,050,000.00 USD | 1,050,000.00 USD | 24,750.00 USD | 26,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `278.80` | 28,680.00 USD | 28,680.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.90` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 77,560.00 USD | 59.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.20` | 106,940.00 USD | 106,940.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.40` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.60` | 114,630.00 USD | 114,630.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.00` | 152,780.00 USD | 152,780.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.40` | 257,810.00 USD | 257,810.00 USD | 8,720.00 USD | 18,470.00 USD | 77,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.80` | 342,320.00 USD | 342,320.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.20` | 396,020.00 USD | 396,020.00 USD | 0.00 USD | 6,950.00 USD | 46,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.60` | 416,610.00 USD | 416,610.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.90` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 20,710.00 USD | 398,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.00` | 449,700.00 USD | 449,700.00 USD | 8,290.00 USD | 20,660.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.40` | 511,680.00 USD | 511,680.00 USD | 16,510.00 USD | 7,210.00 USD | 38,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.40` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.80` | 789,180.00 USD | 789,180.00 USD | 123,240.00 USD | 21,680.00 USD | 132,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.90` | 1,810,000.00 USD | 1,810,000.00 USD | 32,190.00 USD | 0.00 USD | 160.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.20` | 892,100.00 USD | 892,100.00 USD | 46,740.00 USD | 9,540.00 USD | 46,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.40` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 66,560.00 USD | 146,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.60` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 26,800.00 USD | 91,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.90` | 2,380,000.00 USD | 2,380,000.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.00` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 29,850.00 USD | 69,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.40` | 1,290,000.00 USD | 1,290,000.00 USD | 39,870.00 USD | 92,800.00 USD | 49,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 2,540,000.00 USD | 2,540,000.00 USD | 27,700.00 USD | 89,730.00 USD | 42,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `284.50` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `284.80` | 1,390,000.00 USD | 1,390,000.00 USD | 48,190.00 USD | 21,530.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.90` | 3,000,000.00 USD | 3,000,000.00 USD | 67,050.00 USD | 391,180.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.20` | 1,590,000.00 USD | 1,590,000.00 USD | 87,540.00 USD | 37,830.00 USD | 73,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.40` | 3,340,000.00 USD | 3,340,000.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.60` | 1,830,000.00 USD | 1,830,000.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.90` | 3,440,000.00 USD | 3,440,000.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.00` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 3,310.00 USD | 18,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 137,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.80` | 1,930,000.00 USD | 1,930,000.00 USD | 750.70 USD | 3,470.00 USD | 71,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.90` | 3,780,000.00 USD | 3,780,000.00 USD | 51,390.00 USD | 148,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.20` | 2,110,000.00 USD | 2,110,000.00 USD | 31,110.00 USD | 117,540.00 USD | 32,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.40` | 3,990,000.00 USD | 3,990,000.00 USD | 53,620.00 USD | 103,430.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 1,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.60` | 2,210,000.00 USD | 2,210,000.00 USD | 13,180.00 USD | 29,010.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 288,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.00` | 2,270,000.00 USD | 2,270,000.00 USD | 8,260.00 USD | 14,410.00 USD | 38,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.40` | 2,320,000.00 USD | 2,320,000.00 USD | 42,610.00 USD | 4,250.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `288.50` | 721.25 USD | 1,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `288.80` | 2,340,000.00 USD | 2,340,000.00 USD | 7,560.00 USD | 5,700.00 USD | 6.06 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.90` | 4,280,000.00 USD | 4,280,000.00 USD | 1,170.00 USD | 0.00 USD | 9.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 2,370,000.00 USD | 2,370,000.00 USD | 1,720.00 USD | 20,430.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.40` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 927.80 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 3,710.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.00` | 2,390,000.00 USD | 2,390,000.00 USD | 1,320.00 USD | 106.00 USD | 0.97 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.40` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 445.10 USD | 16,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 4,320,000.00 USD | 4,320,000.00 USD | 34,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.80` | 2,450,000.00 USD | 2,450,000.00 USD | 33,300.00 USD | 6,800.00 USD | 14.35 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.90` | 4,320,000.00 USD | 4,320,000.00 USD | 898.13 USD | 861.99 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 2,460,000.00 USD | 2,460,000.00 USD | 915.64 USD | 9,950.00 USD | 6.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.40` | 4,380,000.00 USD | 4,380,000.00 USD | 1,340.00 USD | 55,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.60` | 2,500,000.00 USD | 2,500,000.00 USD | 375.70 USD | 15,770.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.90` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 120,730.00 USD | 8.56 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 32,090.00 USD | 7.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 2,600,000.00 USD | 2,600,000.00 USD | 21,930.00 USD | 42,060.00 USD | 8,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 71,940.00 USD | 87.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.80` | 2,680,000.00 USD | 2,680,000.00 USD | 12,000.00 USD | 71,120.00 USD | 20.88 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 119,560.00 USD | 103.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 2,760,000.00 USD | 2,760,000.00 USD | 10,290.00 USD | 37,810.00 USD | 27,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.40` | 4,800,000.00 USD | 4,800,000.00 USD | 534.50 USD | 112,560.00 USD | 24.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 2,920,000.00 USD | 2,920,000.00 USD | 89,760.00 USD | 56,780.00 USD | 9,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.90` | 4,920,000.00 USD | 4,920,000.00 USD | 51,570.00 USD | 20,910.00 USD | 45,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 3,040,000.00 USD | 3,040,000.00 USD | 23,660.00 USD | 35,280.00 USD | 64,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 3,310,000.00 USD | 3,310,000.00 USD | 73,590.00 USD | 76,140.00 USD | 120,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 5,130,000.00 USD | 5,130,000.00 USD | 139,780.00 USD | 14,550.00 USD | 60,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `294.50` | 6,090.00 USD | 7,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `294.80` | 3,480,000.00 USD | 3,480,000.00 USD | 71,230.00 USD | 64,650.00 USD | 35,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.90` | 5,410,000.00 USD | 5,410,000.00 USD | 64,510.00 USD | 107,870.00 USD | 104,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 3,570,000.00 USD | 3,570,000.00 USD | 17,510.00 USD | 18,500.00 USD | 56,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.40` | 5,850,000.00 USD | 5,850,000.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.60` | 3,760,000.00 USD | 3,760,000.00 USD | 52,050.00 USD | 53,190.00 USD | 76,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.90` | 6,240,000.00 USD | 6,240,000.00 USD | 108,830.00 USD | 133,090.00 USD | 150,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 3,910,000.00 USD | 3,910,000.00 USD | 65,850.00 USD | 70,930.00 USD | 20,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 4,020,000.00 USD | 4,020,000.00 USD | 70,270.00 USD | 25,510.00 USD | 6,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 6,470,000.00 USD | 6,470,000.00 USD | 27,680.00 USD | 77,570.00 USD | 120,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.80` | 4,130,000.00 USD | 4,130,000.00 USD | 34,520.00 USD | 21,170.00 USD | 62,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.90` | 6,900,000.00 USD | 6,900,000.00 USD | 207,350.00 USD | 50,930.00 USD | 172,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 4,230,000.00 USD | 4,230,000.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.40` | 7,000,000.00 USD | 7,000,000.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 4,260,000.00 USD | 4,260,000.00 USD | 6,390.00 USD | 1,190.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.90` | 7,110,000.00 USD | 7,110,000.00 USD | 17,770.00 USD | 39,840.00 USD | 54,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 4,370,000.00 USD | 4,370,000.00 USD | 50,560.00 USD | 10,150.00 USD | 41,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 4,440,000.00 USD | 4,440,000.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 7,250,000.00 USD | 7,250,000.00 USD | 32,250.00 USD | 42,710.00 USD | 68,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.80` | 4,560,000.00 USD | 4,560,000.00 USD | 26,400.00 USD | 257.02 USD | 94,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.90` | 7,380,000.00 USD | 7,380,000.00 USD | 70,090.00 USD | 12,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 4,610,000.00 USD | 4,610,000.00 USD | 7,810.00 USD | 26,290.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.40` | 7,440,000.00 USD | 7,440,000.00 USD | 4,470.00 USD | 13,080.00 USD | 45,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.60` | 4,670,000.00 USD | 4,670,000.00 USD | 39,940.00 USD | 6,750.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.90` | 7,530,000.00 USD | 7,530,000.00 USD | 56,210.00 USD | 10,220.00 USD | 19,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 4,740,000.00 USD | 4,740,000.00 USD | 14,610.00 USD | 17,340.00 USD | 32,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 4,850,000.00 USD | 4,850,000.00 USD | 37,950.00 USD | 31,850.00 USD | 42,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 7,530,000.00 USD | 7,530,000.00 USD | 866.20 USD | 1,190.00 USD | 71.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.80` | 4,900,000.00 USD | 4,900,000.00 USD | 6,710.00 USD | 18,750.00 USD | 19,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.90` | 7,730,000.00 USD | 7,730,000.00 USD | 24,730.00 USD | 70,210.00 USD | 104,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 4,950,000.00 USD | 4,950,000.00 USD | 4,120.00 USD | 28,830.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.40` | 7,950,000.00 USD | 7,950,000.00 USD | 71,890.00 USD | 56,010.00 USD | 94,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.60` | 5,020,000.00 USD | 5,020,000.00 USD | 19,880.00 USD | 8,210.00 USD | 34,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.90` | 8,250,000.00 USD | 8,250,000.00 USD | 89,300.00 USD | 185,430.00 USD | 26,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 5,080,000.00 USD | 5,080,000.00 USD | 24,910.00 USD | 27,720.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 5,110,000.00 USD | 5,110,000.00 USD | 11,150.00 USD | 4,310.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 8,380,000.00 USD | 8,380,000.00 USD | 1,560.00 USD | 125,480.00 USD | 36.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 5,160,000.00 USD | 5,160,000.00 USD | 1,230.00 USD | 12,530.00 USD | 34,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.90` | 8,600,000.00 USD | 8,600,000.00 USD | 71,700.00 USD | 110,480.00 USD | 41,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 5,220,000.00 USD | 5,220,000.00 USD | 31,330.00 USD | 234.82 USD | 24,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.40` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 173.09 USD | 97.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 5,230,000.00 USD | 5,230,000.00 USD | 7,540.00 USD | 4,840.00 USD | 6,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.90` | 8,680,000.00 USD | 8,680,000.00 USD | 21,140.00 USD | 11,010.00 USD | 46,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 5,290,000.00 USD | 5,290,000.00 USD | 21,670.00 USD | 2,070.00 USD | 32,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 5,380,000.00 USD | 5,380,000.00 USD | 13,310.00 USD | 11,260.00 USD | 63,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 8,700,000.00 USD | 8,700,000.00 USD | 3,670.00 USD | 15,430.00 USD | 197.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 5,410,000.00 USD | 5,410,000.00 USD | 9,920.00 USD | 3,140.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.90` | 8,760,000.00 USD | 8,760,000.00 USD | 36,160.00 USD | 18,990.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 5,420,000.00 USD | 5,420,000.00 USD | 9,070.00 USD | 178.95 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.40` | 9,170,000.00 USD | 9,170,000.00 USD | 163,730.00 USD | 127,450.00 USD | 119,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 5,430,000.00 USD | 5,430,000.00 USD | 4,670.00 USD | 1,650.00 USD | 1,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.90` | 9,320,000.00 USD | 9,320,000.00 USD | 82,000.00 USD | 55,480.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 5,450,000.00 USD | 5,450,000.00 USD | 9,360.00 USD | 5,830.00 USD | 7,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 5,470,000.00 USD | 5,470,000.00 USD | 4,230.00 USD | 9,300.00 USD | 5,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 9,480,000.00 USD | 9,480,000.00 USD | 39,250.00 USD | 55,740.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `306.50` | 300.37 USD | 8,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `306.80` | 5,540,000.00 USD | 5,540,000.00 USD | 28,860.00 USD | 35,370.00 USD | 5,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.90` | 9,740,000.00 USD | 9,740,000.00 USD | 84,850.00 USD | 64,520.00 USD | 102,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 5,600,000.00 USD | 5,600,000.00 USD | 11,230.00 USD | 27,230.00 USD | 24,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.40` | 10,020,000.00 USD | 10,020,000.00 USD | 46,230.00 USD | 154,680.00 USD | 83,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.60` | 5,670,000.00 USD | 5,670,000.00 USD | 27,670.00 USD | 33,780.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.90` | 10,320,000.00 USD | 10,320,000.00 USD | 136,380.00 USD | 101,120.00 USD | 65,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 5,740,000.00 USD | 5,740,000.00 USD | 30,270.00 USD | 20,550.00 USD | 22,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 5,750,000.00 USD | 5,750,000.00 USD | 4,760.00 USD | 3,360.00 USD | 4,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 10,650,000.00 USD | 10,650,000.00 USD | 152,590.00 USD | 50,070.00 USD | 124,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.60` | 5,760,000.00 USD | 5,760,000.00 USD | 5,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.90` | 10,780,000.00 USD | 10,780,000.00 USD | 61,600.00 USD | 52,230.00 USD | 19,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.40` | 10,890,000.00 USD | 10,890,000.00 USD | 28,000.00 USD | 35,530.00 USD | 46,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.90` | 11,230,000.00 USD | 11,230,000.00 USD | 59,490.00 USD | 131,460.00 USD | 144,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 11,510,000.00 USD | 11,510,000.00 USD | 78,770.00 USD | 123,340.00 USD | 76,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.90` | 11,590,000.00 USD | 11,590,000.00 USD | 35,670.00 USD | 35,930.00 USD | 3,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.40` | 11,790,000.00 USD | 11,790,000.00 USD | 89,390.00 USD | 65,750.00 USD | 47,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.90` | 11,850,000.00 USD | 11,850,000.00 USD | 40,320.00 USD | 11,160.00 USD | 13,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 11,960,000.00 USD | 11,960,000.00 USD | 38,320.00 USD | 22,970.00 USD | 43,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.90` | 12,030,000.00 USD | 12,030,000.00 USD | 22,600.00 USD | 8,800.00 USD | 38,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.40` | 12,140,000.00 USD | 12,140,000.00 USD | 55,570.00 USD | 24,730.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.90` | 12,230,000.00 USD | 12,230,000.00 USD | 44,540.00 USD | 15,370.00 USD | 35,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 12,340,000.00 USD | 12,340,000.00 USD | 51,980.00 USD | 307.60 USD | 51,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.90` | 12,390,000.00 USD | 12,390,000.00 USD | 39,410.00 USD | 0.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.40` | 12,400,000.00 USD | 12,400,000.00 USD | 6,160.00 USD | 9,920.00 USD | 52.52 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.90` | 12,520,000.00 USD | 12,520,000.00 USD | 47,110.00 USD | 41,400.00 USD | 29,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 12,640,000.00 USD | 12,640,000.00 USD | 16,580.00 USD | 40,320.00 USD | 61,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.90` | 12,660,000.00 USD | 12,660,000.00 USD | 3,030.00 USD | 10,840.00 USD | 106.47 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.40` | 12,670,000.00 USD | 12,670,000.00 USD | 14,540.00 USD | 1,010.00 USD | 107.86 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.90` | 12,700,000.00 USD | 12,700,000.00 USD | 21,640.00 USD | 8,200.00 USD | 201.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.40` | 12,750,000.00 USD | 12,750,000.00 USD | 3,320.00 USD | 27,530.00 USD | 22,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.90` | 12,820,000.00 USD | 12,820,000.00 USD | 11,180.00 USD | 17,970.00 USD | 37,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.40` | 12,840,000.00 USD | 12,840,000.00 USD | 733.55 USD | 18,060.00 USD | 5.68 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `319.90` | 12,870,000.00 USD | 12,870,000.00 USD | 446.22 USD | 22,230.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `320.40` | 12,950,000.00 USD | 12,950,000.00 USD | 49,620.00 USD | 10,080.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `320.50` | 1,110.00 USD | 9,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `320.90` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 166.45 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.40` | 13,000,000.00 USD | 13,000,000.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `321.90` | 13,010,000.00 USD | 13,010,000.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.40` | 13,040,000.00 USD | 13,040,000.00 USD | 22,930.00 USD | 7,950.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `322.90` | 13,070,000.00 USD | 13,070,000.00 USD | 16,590.00 USD | 5,830.00 USD | 0.48 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `323.40` | 13,100,000.00 USD | 13,100,000.00 USD | 14,160.00 USD | 11,950.00 USD | 11,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `323.50` | 2,220.00 USD | 11,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `323.90` | 13,110,000.00 USD | 13,110,000.00 USD | 269.10 USD | 692.00 USD | 0.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.40` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `324.90` | 13,160,000.00 USD | 13,160,000.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `325.40` | 13,210,000.00 USD | 13,210,000.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD | `Tier 1 CEX` |
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
| `7D` | `240.90` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 0.00 USD | 330.05 USD | 4,560.00 USD |
| `7D` | `241.40` | 11,710,000.00 USD | 0.00 USD | 11,710,000.00 USD | 7,150.00 USD | 0.00 USD | 22.63 USD |
| `7D` | `241.90` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 19,010.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.40` | 11,670,000.00 USD | 0.00 USD | 11,670,000.00 USD | 36,130.00 USD | 11,260.00 USD | 8,370.00 USD |
| `7D` | `242.90` | 11,620,000.00 USD | 0.00 USD | 11,620,000.00 USD | 0.00 USD | 5,680.00 USD | 0.66 USD |
| `7D` | `243.40` | 11,610,000.00 USD | 0.00 USD | 11,610,000.00 USD | 0.00 USD | 9,910.00 USD | 5,490.00 USD |
| `7D` | `243.90` | 11,600,000.00 USD | 0.00 USD | 11,600,000.00 USD | 781.30 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.90` | 11,580,000.00 USD | 0.00 USD | 11,580,000.00 USD | 836.88 USD | 17,320.00 USD | 2,630.00 USD |
| `7D` | `245.40` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 5,050.00 USD | 9,400.00 USD | 4,870.00 USD |
| `7D` | `245.90` | 11,540,000.00 USD | 0.00 USD | 11,540,000.00 USD | 10,560.00 USD | 10,460.00 USD | 3,010.00 USD |
| `1D` | `246.40` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `246.40` | 11,510,000.00 USD | 0.00 USD | 11,510,000.00 USD | 10,200.00 USD | 9,970.00 USD | 7,710.00 USD |
| `1D` | `246.80` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 6.81 USD |
| `7D` | `246.90` | 11,480,000.00 USD | 0.00 USD | 11,480,000.00 USD | 4,670.00 USD | 3,990.00 USD | 1,730.00 USD |
| `1D` | `247.20` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 0.00 USD | 3,690.00 USD | 7.12 USD |
| `7D` | `247.40` | 11,470,000.00 USD | 0.00 USD | 11,470,000.00 USD | 23,270.00 USD | 12,440.00 USD | 2,710.00 USD |
| `1D` | `247.60` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 528.00 USD | 0.00 USD | 7,250.00 USD |
| `7D` | `247.90` | 11,440,000.00 USD | 0.00 USD | 11,440,000.00 USD | 789.37 USD | 4,610.00 USD | 8.00 USD |
| `1D` | `248.00` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 10,640.00 USD | 619.60 USD | 24,000.00 USD |
| `1D` | `248.40` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 7,480.00 USD | 4,690.00 USD | 6,250.00 USD |
| `7D` | `248.40` | 11,430,000.00 USD | 0.00 USD | 11,430,000.00 USD | 11,840.00 USD | 3,060.00 USD | 30,880.00 USD |
| `1D` | `248.80` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 1,750.00 USD | 13,380.00 USD |
| `7D` | `248.90` | 11,380,000.00 USD | 0.00 USD | 11,380,000.00 USD | 37,420.00 USD | 28,490.00 USD | 32,240.00 USD |
| `1D` | `249.20` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 3,960.00 USD | 12,400.00 USD | 17,640.00 USD |
| `7D` | `249.40` | 11,290,000.00 USD | 0.00 USD | 11,290,000.00 USD | 49,060.00 USD | 28,020.00 USD | 3,980.00 USD |
| `1D` | `249.60` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 9,040.00 USD | 1,710.00 USD | 3,310.00 USD |
| `7D` | `249.90` | 11,210,000.00 USD | 0.00 USD | 11,210,000.00 USD | 45,660.00 USD | 28,830.00 USD | 35,200.00 USD |
| `1D` | `250.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 13,540.00 USD | 1,340.00 USD | 2,210.00 USD |
| `1D` | `250.40` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 9,230.00 USD | 5,500.00 USD | 7,210.00 USD |
| `7D` | `250.40` | 11,100,000.00 USD | 0.00 USD | 11,100,000.00 USD | 22,680.00 USD | 38,250.00 USD | 12,500.00 USD |
| `1D` | `250.80` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,430.00 USD | 14,820.00 USD | 7,060.00 USD |
| `7D` | `250.90` | 11,020,000.00 USD | 0.00 USD | 11,020,000.00 USD | 30,350.00 USD | 43,110.00 USD | 18,630.00 USD |
| `1D` | `251.20` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 31,750.00 USD | 38,410.00 USD | 16,130.00 USD |
| `7D` | `251.40` | 10,930,000.00 USD | 0.00 USD | 10,930,000.00 USD | 50,070.00 USD | 99,670.00 USD | 22,230.00 USD |
| `1D` | `251.60` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 31,800.00 USD | 51,410.00 USD | 16,550.00 USD |
| `7D` | `251.90` | 10,760,000.00 USD | 0.00 USD | 10,760,000.00 USD | 74,710.00 USD | 52,190.00 USD | 43,230.00 USD |
| `1D` | `252.00` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 30,240.00 USD | 20,110.00 USD | 22,660.00 USD |
| `1D` | `252.40` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 4,850.00 USD | 3,390.00 USD | 4,260.00 USD |
| `7D` | `252.40` | 10,590,000.00 USD | 0.00 USD | 10,590,000.00 USD | 73,970.00 USD | 33,030.00 USD | 28,080.00 USD |
| `1D` | `252.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 18,060.00 USD | 6,420.00 USD | 5,660.00 USD |
| `7D` | `252.90` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 29,220.00 USD | 19,580.00 USD | 12.98 USD |
| `1D` | `253.20` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 9,580.00 USD | 13,960.00 USD | 4,730.00 USD |
| `7D` | `253.40` | 10,400,000.00 USD | 0.00 USD | 10,400,000.00 USD | 30,180.00 USD | 49,680.00 USD | 44,330.00 USD |
| `1D` | `253.60` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 15,820.00 USD | 13,480.00 USD | 10,590.00 USD |
| `7D` | `253.90` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 6,580.00 USD | 31,310.00 USD | 25,950.00 USD |
| `1D` | `254.00` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 144.00 USD | 6,840.00 USD | 9,560.00 USD |
| `1D` | `254.40` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 134.35 USD | 2,130.00 USD | 10.44 USD |
| `7D` | `254.40` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 40,960.00 USD | 36,880.00 USD | 3,850.00 USD |
| `1D` | `254.80` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 1,280.00 USD | 2,050.00 USD | 2,760.00 USD |
| `7D` | `254.90` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 28,730.00 USD | 6,640.00 USD | 18,160.00 USD |
| `1D` | `255.20` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 9,500.00 USD | 6,590.00 USD | 3.11 USD |
| `7D` | `255.40` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 44,380.00 USD | 11,830.00 USD | 23,790.00 USD |
| `1D` | `255.60` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 8,470.00 USD | 8,330.00 USD | 2,760.00 USD |
| `7D` | `255.90` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 16,050.00 USD | 19,500.00 USD | 28,160.00 USD |
| `1D` | `256.00` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 11,080.00 USD | 321.10 USD | 22.37 USD |
| `1D` | `256.40` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 12,240.00 USD | 6,710.00 USD | 2,580.00 USD |
| `7D` | `256.40` | 9,940,000.00 USD | 0.00 USD | 9,940,000.00 USD | 78,300.00 USD | 15,590.00 USD | 37,460.00 USD |
| `1D` | `256.80` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 5,560.00 USD | 928.93 USD | 0.73 USD |
| `7D` | `256.90` | 9,810,000.00 USD | 0.00 USD | 9,810,000.00 USD | 45,670.00 USD | 16,040.00 USD | 35,900.00 USD |
| `1D` | `257.20` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 5,380.00 USD | 0.00 USD | 7,330.00 USD |
| `7D` | `257.40` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 42,430.00 USD | 1,910.00 USD | 27,330.00 USD |
| `1D` | `257.60` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 1,190.00 USD | 741.83 USD | 9,250.00 USD |
| `7D` | `257.90` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 35,320.00 USD | 6,650.00 USD | 18,200.00 USD |
| `1D` | `258.00` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 5,060.00 USD | 2,390.00 USD | 1,640.00 USD |
| `1D` | `258.40` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 2,130.00 USD | 3,450.00 USD | 5,240.00 USD |
| `7D` | `258.40` | 9,580,000.00 USD | 0.00 USD | 9,580,000.00 USD | 137,820.00 USD | 54,900.00 USD | 33,600.00 USD |
| `1D` | `258.80` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 2,120.00 USD | 3,750.00 USD | 5,610.00 USD |
| `7D` | `258.90` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 61,620.00 USD | 3,500.00 USD | 34,360.00 USD |
| `1D` | `259.20` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 13,320.00 USD | 3,850.00 USD | 7,660.00 USD |
| `7D` | `259.40` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 4,410.00 USD | 45,330.00 USD | 8,090.00 USD |
| `1D` | `259.60` | 4,090,000.00 USD | 0.00 USD | 4,090,000.00 USD | 5,330.00 USD | 4,700.00 USD | 7,170.00 USD |
| `7D` | `259.90` | 9,190,000.00 USD | 0.00 USD | 9,190,000.00 USD | 19,140.00 USD | 12,520.00 USD | 109.79 USD |
| `1D` | `260.00` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 15,300.00 USD | 14,890.00 USD | 23,910.00 USD |
| `1D` | `260.40` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 2,940.00 USD | 9,390.00 USD | 10,400.00 USD |
| `7D` | `260.40` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 25,230.00 USD | 11,260.00 USD | 83,180.00 USD |
| `1D` | `260.80` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 266.79 USD | 18,270.00 USD | 13,960.00 USD |
| `7D` | `260.90` | 9,040,000.00 USD | 0.00 USD | 9,040,000.00 USD | 19,770.00 USD | 58,910.00 USD | 37,890.00 USD |
| `1D` | `261.20` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 7,970.00 USD | 18,100.00 USD | 30,840.00 USD |
| `7D` | `261.40` | 8,920,000.00 USD | 0.00 USD | 8,920,000.00 USD | 15,900.00 USD | 71,870.00 USD | 18,370.00 USD |
| `1D` | `261.60` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 7,930.00 USD | 1,290.00 USD | 19,360.00 USD |
| `7D` | `261.90` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 54,590.00 USD | 49,830.00 USD | 50,320.00 USD |
| `1D` | `262.00` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 4,560.00 USD | 4,320.00 USD | 13,920.00 USD |
| `1D` | `262.40` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 9,000.00 USD | 4,480.00 USD | 20.31 USD |
| `7D` | `262.40` | 8,660,000.00 USD | 0.00 USD | 8,660,000.00 USD | 44,640.00 USD | 52,560.00 USD | 75.21 USD |
| `1D` | `262.80` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 366.04 USD | 14,220.00 USD | 21.99 USD |
| `7D` | `262.90` | 8,570,000.00 USD | 0.00 USD | 8,570,000.00 USD | 74,780.00 USD | 34,390.00 USD | 32,760.00 USD |
| `1D` | `263.20` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 9,680.00 USD | 4,510.00 USD | 16,180.00 USD |
| `7D` | `263.40` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 102,110.00 USD | 30,720.00 USD | 50,100.00 USD |
| `1D` | `263.60` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 1,010.00 USD | 7,000.00 USD | 16,150.00 USD |
| `7D` | `263.90` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 287,090.00 USD | 97,270.00 USD | 57,890.00 USD |
| `1D` | `264.00` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 1,210.00 USD | 4,040.00 USD | 18,120.00 USD |
| `1D` | `264.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 1,660.00 USD | 920.03 USD | 13.24 USD |
| `7D` | `264.40` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 47,200.00 USD | 41,160.00 USD | 26,220.00 USD |
| `1D` | `264.80` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 28,700.00 USD | 4,430.00 USD | 75,610.00 USD |
| `7D` | `264.90` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 28,050.00 USD | 82,080.00 USD | 27,180.00 USD |
| `1D` | `265.20` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 34,820.00 USD | 13,080.00 USD | 2,070.00 USD |
| `7D` | `265.40` | 7,550,000.00 USD | 0.00 USD | 7,550,000.00 USD | 134,720.00 USD | 59,500.00 USD | 182,900.00 USD |
| `1D` | `265.60` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 19,750.00 USD | 38,130.00 USD | 77,540.00 USD |
| `7D` | `265.90` | 7,170,000.00 USD | 0.00 USD | 7,170,000.00 USD | 72,980.00 USD | 117,570.00 USD | 137,710.00 USD |
| `1D` | `266.00` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 51,150.00 USD | 7,940.00 USD | 8,690.00 USD |
| `1D` | `266.40` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 41,560.00 USD | 28,430.00 USD | 10,070.00 USD |
| `7D` | `266.40` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 209,320.00 USD | 160,160.00 USD | 111,530.00 USD |
| `1D` | `266.80` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 28,890.00 USD | 22,040.00 USD | 80,050.00 USD |
| `7D` | `266.90` | 6,360,000.00 USD | 0.00 USD | 6,360,000.00 USD | 156,170.00 USD | 228,210.00 USD | 96,340.00 USD |
| `1D` | `267.20` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 16,540.00 USD | 8,620.00 USD | 44,030.00 USD |
| `7D` | `267.40` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 118,190.00 USD | 209,120.00 USD | 96,470.00 USD |
| `1D` | `267.60` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 30,750.00 USD | 80,200.00 USD | 23,720.00 USD |
| `7D` | `267.90` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 268,540.00 USD | 228,190.00 USD | 119,500.00 USD |
| `1D` | `268.00` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 104,590.00 USD | 112,690.00 USD | 52,740.00 USD |
| `1D` | `268.40` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 90,320.00 USD | 130,660.00 USD | 32,080.00 USD |
| `7D` | `268.40` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 176,940.00 USD | 323,870.00 USD | 99,470.00 USD |
| `1D` | `268.80` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 100,660.00 USD | 65,950.00 USD | 56,660.00 USD |
| `7D` | `268.90` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 261,830.00 USD | 135,480.00 USD | 103,850.00 USD |
| `1D` | `269.20` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 21,310.00 USD | 34,490.00 USD | 12,920.00 USD |
| `7D` | `269.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 299,510.00 USD | 180,180.00 USD | 88,050.00 USD |
| `1D` | `269.60` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 34,010.00 USD | 20,280.00 USD | 46,560.00 USD |
| `7D` | `269.90` | 3,170,000.00 USD | 0.00 USD | 3,170,000.00 USD | 74,250.00 USD | 141,330.00 USD | 0.00 USD |
| `1D` | `270.00` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 45,580.00 USD | 25,140.00 USD | 141,110.00 USD |
| `1D` | `270.40` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 129,180.00 USD | 6,950.00 USD | 59,190.00 USD |
| `7D` | `270.40` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 118,110.00 USD | 14,140.00 USD | 0.00 USD |
| `1D` | `270.80` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 56,030.00 USD | 7,500.00 USD | 29,660.00 USD |
| `7D` | `270.90` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 328,250.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `271.20` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 56,240.00 USD | 7,760.00 USD | 160,750.00 USD |
| `7D` | `271.40` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 152,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `271.60` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 102,160.00 USD | 15,710.00 USD | 0.00 USD |
| `7D` | `271.90` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 463,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.00` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 131,180.00 USD | 4,060.00 USD | 10,130.00 USD |
| `1D` | `272.40` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 69,420.00 USD | 368.00 USD | 19,720.00 USD |
| `7D` | `272.40` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 277,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.80` | 971,800.00 USD | 0.00 USD | 971,800.00 USD | 85,930.00 USD | 7,340.00 USD | 0.00 USD |
| `7D` | `272.90` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 150,960.00 USD | 0.00 USD | 15,300.00 USD |
| `1D` | `273.20` | 878,540.00 USD | 0.00 USD | 878,540.00 USD | 65,470.00 USD | 73.70 USD | 0.00 USD |
| `7D` | `273.40` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 379,280.00 USD | 0.00 USD | 163,350.00 USD |
| `1D` | `273.60` | 813,000.00 USD | 0.00 USD | 813,000.00 USD | 229,980.00 USD | 0.00 USD | 111,930.00 USD |
| `7D` | `273.90` | 872,180.00 USD | 0.00 USD | 872,180.00 USD | 375,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.00` | 471,100.00 USD | 0.00 USD | 471,100.00 USD | 190,550.00 USD | 0.00 USD | 12.78 USD |
| `1D` | `274.40` | 280,540.00 USD | 0.00 USD | 280,540.00 USD | 209,960.00 USD | 0.00 USD | 10.80 USD |
| `7D` | `274.40` | 496,740.00 USD | 0.00 USD | 496,740.00 USD | 496,740.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `274.80` | 70,560.00 USD | 0.00 USD | 70,560.00 USD | 45,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 348,470.00 USD | 348,470.00 USD | 0.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `274.90` | 696,940.00 USD | 696,940.00 USD | 0.00 USD | 348,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `275.20` | 25,430.00 USD | 0.00 USD | 25,430.00 USD | 25,410.00 USD | 0.00 USD | 13.00 USD |
| `7D` | `275.40` | 700,470.00 USD | 700,470.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `275.90` | 703,030.00 USD | 703,030.00 USD | 0.00 USD | 2,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `276.40` | 809,250.00 USD | 809,250.00 USD | 0.00 USD | 2,290.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.80` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `276.90` | 853,930.00 USD | 853,930.00 USD | 0.00 USD | 44,670.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.20` | 301.20 USD | 301.20 USD | 0.00 USD | 301.20 USD | 0.00 USD | 0.00 USD |
| `7D` | `277.40` | 917,220.00 USD | 917,220.00 USD | 0.00 USD | 0.00 USD | 63,290.00 USD | 0.00 USD |
| `1D` | `277.60` | 305.64 USD | 305.64 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4.44 USD |
| `7D` | `277.90` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 85,690.00 USD | 120.11 USD |
| `7D` | `278.40` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 24,750.00 USD | 26,370.00 USD | 0.00 USD |
| `1D` | `278.80` | 28,680.00 USD | 28,680.00 USD | 0.00 USD | 24,100.00 USD | 4,280.00 USD | 0.00 USD |
| `7D` | `278.90` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 77,560.00 USD | 59.08 USD |
| `1D` | `279.20` | 106,940.00 USD | 106,940.00 USD | 0.00 USD | 53,390.00 USD | 24,870.00 USD | 0.00 USD |
| `7D` | `279.40` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 95,990.00 USD |
| `1D` | `279.60` | 114,630.00 USD | 114,630.00 USD | 0.00 USD | 0.00 USD | 7,690.00 USD | 0.00 USD |
| `1D` | `280.00` | 152,780.00 USD | 152,780.00 USD | 0.00 USD | 21,040.00 USD | 0.00 USD | 17,110.00 USD |
| `1D` | `280.40` | 257,810.00 USD | 257,810.00 USD | 0.00 USD | 8,720.00 USD | 18,470.00 USD | 77,850.00 USD |
| `1D` | `280.80` | 342,320.00 USD | 342,320.00 USD | 0.00 USD | 0.00 USD | 11,870.00 USD | 72,640.00 USD |
| `1D` | `281.20` | 396,020.00 USD | 396,020.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | 46,760.00 USD |
| `7D` | `281.40` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 14,140.00 USD | 62,810.00 USD |
| `1D` | `281.60` | 416,610.00 USD | 416,610.00 USD | 0.00 USD | 20,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `281.90` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 20,710.00 USD | 398,050.00 USD |
| `1D` | `282.00` | 449,700.00 USD | 449,700.00 USD | 0.00 USD | 8,290.00 USD | 20,660.00 USD | 4,140.00 USD |
| `1D` | `282.40` | 511,680.00 USD | 511,680.00 USD | 0.00 USD | 16,510.00 USD | 7,210.00 USD | 38,250.00 USD |
| `7D` | `282.40` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,290.00 USD |
| `1D` | `282.80` | 789,180.00 USD | 789,180.00 USD | 0.00 USD | 123,240.00 USD | 21,680.00 USD | 132,580.00 USD |
| `7D` | `282.90` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 32,190.00 USD | 0.00 USD | 160.24 USD |
| `1D` | `283.20` | 892,100.00 USD | 892,100.00 USD | 0.00 USD | 46,740.00 USD | 9,540.00 USD | 46,650.00 USD |
| `7D` | `283.40` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 66,560.00 USD | 146,480.00 USD |
| `1D` | `283.60` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 26,800.00 USD | 91,060.00 USD |
| `7D` | `283.90` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 49,500.00 USD | 0.00 USD | 309,040.00 USD |
| `1D` | `284.00` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 29,850.00 USD | 69,640.00 USD |
| `1D` | `284.40` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 39,870.00 USD | 92,800.00 USD | 49,010.00 USD |
| `7D` | `284.40` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 27,700.00 USD | 89,730.00 USD | 42,780.00 USD |
| `1D` | `284.80` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 48,190.00 USD | 21,530.00 USD | 33,930.00 USD |
| `7D` | `284.90` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 67,050.00 USD | 391,180.00 USD | 0.00 USD |
| `1D` | `285.20` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 87,540.00 USD | 37,830.00 USD | 73,380.00 USD |
| `7D` | `285.40` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 64,060.00 USD | 193,790.00 USD | 83,240.00 USD |
| `1D` | `285.60` | 1,830,000.00 USD | 1,830,000.00 USD | 0.00 USD | 91,500.00 USD | 121,100.00 USD | 27,930.00 USD |
| `7D` | `285.90` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 1,200.00 USD | 97,960.00 USD | 0.00 USD |
| `1D` | `286.00` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 18,120.00 USD |
| `7D` | `286.40` | 3,580,000.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 137,400.00 USD | 0.00 USD |
| `1D` | `286.80` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 750.70 USD | 3,470.00 USD | 71,360.00 USD |
| `7D` | `286.90` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 51,390.00 USD | 148,230.00 USD | 0.00 USD |
| `1D` | `287.20` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 31,110.00 USD | 117,540.00 USD | 32,710.00 USD |
| `7D` | `287.40` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 53,620.00 USD | 103,430.00 USD | 53,280.00 USD |
| `1D` | `287.60` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 13,180.00 USD | 29,010.00 USD | 56,790.00 USD |
| `7D` | `287.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 288,200.00 USD | 0.00 USD |
| `1D` | `288.00` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 8,260.00 USD | 14,410.00 USD | 38,780.00 USD |
| `1D` | `288.40` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 42,610.00 USD | 4,250.00 USD | 5,060.00 USD |
| `1D` | `288.80` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 7,560.00 USD | 5,700.00 USD | 6.06 USD |
| `7D` | `288.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 1,170.00 USD | 0.00 USD | 9.00 USD |
| `1D` | `289.20` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 1,720.00 USD | 20,430.00 USD | 9,870.00 USD |
| `7D` | `289.40` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 927.80 USD | 0.00 USD |
| `1D` | `289.60` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 14,160.00 USD |
| `7D` | `289.90` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 0.00 USD | 1,990.00 USD | 0.00 USD |
| `1D` | `290.00` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 1,320.00 USD | 106.00 USD | 0.97 USD |
| `1D` | `290.40` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 445.10 USD | 16,980.00 USD |
| `7D` | `290.40` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 34,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.80` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 33,300.00 USD | 6,800.00 USD | 14.35 USD |
| `7D` | `290.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 898.13 USD | 861.99 USD | 0.00 USD |
| `1D` | `291.20` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 915.64 USD | 9,950.00 USD | 6.80 USD |
| `7D` | `291.40` | 4,380,000.00 USD | 4,380,000.00 USD | 0.00 USD | 1,340.00 USD | 55,720.00 USD | 0.00 USD |
| `1D` | `291.60` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 375.70 USD | 15,770.00 USD | 22,130.00 USD |
| `7D` | `291.90` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 0.00 USD | 120,730.00 USD | 8.56 USD |
| `1D` | `292.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 32,090.00 USD | 7.16 USD |
| `1D` | `292.40` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 21,930.00 USD | 42,060.00 USD | 8,110.00 USD |
| `7D` | `292.40` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 71,940.00 USD | 87.88 USD |
| `1D` | `292.80` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 12,000.00 USD | 71,120.00 USD | 20.88 USD |
| `7D` | `292.90` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 119,560.00 USD | 103.50 USD |
| `1D` | `293.20` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 10,290.00 USD | 37,810.00 USD | 27,370.00 USD |
| `7D` | `293.40` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 534.50 USD | 112,560.00 USD | 24.81 USD |
| `1D` | `293.60` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 89,760.00 USD | 56,780.00 USD | 9,820.00 USD |
| `7D` | `293.90` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 51,570.00 USD | 20,910.00 USD | 45,040.00 USD |
| `1D` | `294.00` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 23,660.00 USD | 35,280.00 USD | 64,890.00 USD |
| `1D` | `294.40` | 3,310,000.00 USD | 3,310,000.00 USD | 0.00 USD | 73,590.00 USD | 76,140.00 USD | 120,910.00 USD |
| `7D` | `294.40` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 139,780.00 USD | 14,550.00 USD | 60,710.00 USD |
| `1D` | `294.80` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 71,230.00 USD | 64,650.00 USD | 35,630.00 USD |
| `7D` | `294.90` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 64,510.00 USD | 107,870.00 USD | 104,890.00 USD |
| `1D` | `295.20` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 17,510.00 USD | 18,500.00 USD | 56,350.00 USD |
| `7D` | `295.40` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 92,780.00 USD | 94,780.00 USD | 252,180.00 USD |
| `1D` | `295.60` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 52,050.00 USD | 53,190.00 USD | 76,570.00 USD |
| `7D` | `295.90` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 108,830.00 USD | 133,090.00 USD | 150,870.00 USD |
| `1D` | `296.00` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 65,850.00 USD | 70,930.00 USD | 20,690.00 USD |
| `1D` | `296.40` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 70,270.00 USD | 25,510.00 USD | 6,450.00 USD |
| `7D` | `296.40` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 27,680.00 USD | 77,570.00 USD | 120,870.00 USD |
| `1D` | `296.80` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 34,520.00 USD | 21,170.00 USD | 62,260.00 USD |
| `7D` | `296.90` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 207,350.00 USD | 50,930.00 USD | 172,370.00 USD |
| `1D` | `297.20` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 52,770.00 USD | 83.05 USD | 46,240.00 USD |
| `7D` | `297.40` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 4,100.00 USD | 59,290.00 USD | 34,690.00 USD |
| `1D` | `297.60` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 6,390.00 USD | 1,190.00 USD | 23,130.00 USD |
| `7D` | `297.90` | 7,110,000.00 USD | 7,110,000.00 USD | 0.00 USD | 17,770.00 USD | 39,840.00 USD | 54,860.00 USD |
| `1D` | `298.00` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 50,560.00 USD | 10,150.00 USD | 41,570.00 USD |
| `1D` | `298.40` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 10,150.00 USD | 8,080.00 USD | 56,410.00 USD |
| `7D` | `298.40` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 32,250.00 USD | 42,710.00 USD | 68,850.00 USD |
| `1D` | `298.80` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 26,400.00 USD | 257.02 USD | 94,670.00 USD |
| `7D` | `298.90` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 70,090.00 USD | 12,780.00 USD | 40,000.00 USD |
| `1D` | `299.20` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 7,810.00 USD | 26,290.00 USD | 12,330.00 USD |
| `7D` | `299.40` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 4,470.00 USD | 13,080.00 USD | 45,910.00 USD |
| `1D` | `299.60` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 39,940.00 USD | 6,750.00 USD | 19,140.00 USD |
| `7D` | `299.90` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 56,210.00 USD | 10,220.00 USD | 19,850.00 USD |
| `1D` | `300.00` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 14,610.00 USD | 17,340.00 USD | 32,620.00 USD |
| `1D` | `300.40` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 37,950.00 USD | 31,850.00 USD | 42,610.00 USD |
| `7D` | `300.40` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 866.20 USD | 1,190.00 USD | 71.68 USD |
| `1D` | `300.80` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 6,710.00 USD | 18,750.00 USD | 19,860.00 USD |
| `7D` | `300.90` | 7,730,000.00 USD | 7,730,000.00 USD | 0.00 USD | 24,730.00 USD | 70,210.00 USD | 104,190.00 USD |
| `1D` | `301.20` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 4,120.00 USD | 28,830.00 USD | 23,940.00 USD |
| `7D` | `301.40` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 71,890.00 USD | 56,010.00 USD | 94,770.00 USD |
| `1D` | `301.60` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 19,880.00 USD | 8,210.00 USD | 34,830.00 USD |
| `7D` | `301.90` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 89,300.00 USD | 185,430.00 USD | 26,240.00 USD |
| `1D` | `302.00` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 24,910.00 USD | 27,720.00 USD | 10,360.00 USD |
| `1D` | `302.40` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 11,150.00 USD | 4,310.00 USD | 17,550.00 USD |
| `7D` | `302.40` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 1,560.00 USD | 125,480.00 USD | 36.49 USD |
| `1D` | `302.80` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 1,230.00 USD | 12,530.00 USD | 34,810.00 USD |
| `7D` | `302.90` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 71,700.00 USD | 110,480.00 USD | 41,780.00 USD |
| `1D` | `303.20` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 31,330.00 USD | 234.82 USD | 24,010.00 USD |
| `7D` | `303.40` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 0.00 USD | 173.09 USD | 97.76 USD |
| `1D` | `303.60` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 7,540.00 USD | 4,840.00 USD | 6,250.00 USD |
| `7D` | `303.90` | 8,680,000.00 USD | 8,680,000.00 USD | 0.00 USD | 21,140.00 USD | 11,010.00 USD | 46,000.00 USD |
| `1D` | `304.00` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 21,670.00 USD | 2,070.00 USD | 32,140.00 USD |
| `1D` | `304.40` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 13,310.00 USD | 11,260.00 USD | 63,310.00 USD |
| `7D` | `304.40` | 8,700,000.00 USD | 8,700,000.00 USD | 0.00 USD | 3,670.00 USD | 15,430.00 USD | 197.32 USD |
| `1D` | `304.80` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 9,920.00 USD | 3,140.00 USD | 16,360.00 USD |
| `7D` | `304.90` | 8,760,000.00 USD | 8,760,000.00 USD | 0.00 USD | 36,160.00 USD | 18,990.00 USD | 8,390.00 USD |
| `1D` | `305.20` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 9,070.00 USD | 178.95 USD | 4,030.00 USD |
| `7D` | `305.40` | 9,170,000.00 USD | 9,170,000.00 USD | 0.00 USD | 163,730.00 USD | 127,450.00 USD | 119,160.00 USD |
| `1D` | `305.60` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 4,670.00 USD | 1,650.00 USD | 1,490.00 USD |
| `7D` | `305.90` | 9,320,000.00 USD | 9,320,000.00 USD | 0.00 USD | 82,000.00 USD | 55,480.00 USD | 10,750.00 USD |
| `1D` | `306.00` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 9,360.00 USD | 5,830.00 USD | 7,200.00 USD |
| `1D` | `306.40` | 5,470,000.00 USD | 5,470,000.00 USD | 0.00 USD | 4,230.00 USD | 9,300.00 USD | 5,660.00 USD |
| `7D` | `306.40` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 39,250.00 USD | 55,740.00 USD | 66,840.00 USD |
| `1D` | `306.80` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 28,860.00 USD | 35,370.00 USD | 5,480.00 USD |
| `7D` | `306.90` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 84,850.00 USD | 64,520.00 USD | 102,600.00 USD |
| `1D` | `307.20` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 11,230.00 USD | 27,230.00 USD | 24,920.00 USD |
| `7D` | `307.40` | 10,020,000.00 USD | 10,020,000.00 USD | 0.00 USD | 46,230.00 USD | 154,680.00 USD | 83,260.00 USD |
| `1D` | `307.60` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 27,670.00 USD | 33,780.00 USD | 3,670.00 USD |
| `7D` | `307.90` | 10,320,000.00 USD | 10,320,000.00 USD | 0.00 USD | 136,380.00 USD | 101,120.00 USD | 65,290.00 USD |
| `1D` | `308.00` | 5,740,000.00 USD | 5,740,000.00 USD | 0.00 USD | 30,270.00 USD | 20,550.00 USD | 22,660.00 USD |
| `1D` | `308.40` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 4,760.00 USD | 3,360.00 USD | 4,260.00 USD |
| `7D` | `308.40` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 152,590.00 USD | 50,070.00 USD | 124,930.00 USD |
| `1D` | `308.60` | 5,760,000.00 USD | 5,760,000.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `308.90` | 10,780,000.00 USD | 10,780,000.00 USD | 0.00 USD | 61,600.00 USD | 52,230.00 USD | 19,800.00 USD |
| `7D` | `309.40` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 28,000.00 USD | 35,530.00 USD | 46,520.00 USD |
| `7D` | `309.90` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 59,490.00 USD | 131,460.00 USD | 144,750.00 USD |
| `7D` | `310.40` | 11,510,000.00 USD | 11,510,000.00 USD | 0.00 USD | 78,770.00 USD | 123,340.00 USD | 76,910.00 USD |
| `7D` | `310.90` | 11,590,000.00 USD | 11,590,000.00 USD | 0.00 USD | 35,670.00 USD | 35,930.00 USD | 3,900.00 USD |
| `7D` | `311.40` | 11,790,000.00 USD | 11,790,000.00 USD | 0.00 USD | 89,390.00 USD | 65,750.00 USD | 47,650.00 USD |
| `7D` | `311.90` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 40,320.00 USD | 11,160.00 USD | 13,550.00 USD |
| `7D` | `312.40` | 11,960,000.00 USD | 11,960,000.00 USD | 0.00 USD | 38,320.00 USD | 22,970.00 USD | 43,720.00 USD |
| `7D` | `312.90` | 12,030,000.00 USD | 12,030,000.00 USD | 0.00 USD | 22,600.00 USD | 8,800.00 USD | 38,760.00 USD |
| `7D` | `313.40` | 12,140,000.00 USD | 12,140,000.00 USD | 0.00 USD | 55,570.00 USD | 24,730.00 USD | 30,370.00 USD |
| `7D` | `313.90` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 44,540.00 USD | 15,370.00 USD | 35,940.00 USD |
| `7D` | `314.40` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 51,800.00 USD |
| `7D` | `314.90` | 12,390,000.00 USD | 12,390,000.00 USD | 0.00 USD | 39,410.00 USD | 0.00 USD | 10,250.00 USD |
| `7D` | `315.40` | 12,400,000.00 USD | 12,400,000.00 USD | 0.00 USD | 6,160.00 USD | 9,920.00 USD | 52.52 USD |
| `7D` | `315.90` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 47,110.00 USD | 41,400.00 USD | 29,990.00 USD |
| `7D` | `316.40` | 12,640,000.00 USD | 12,640,000.00 USD | 0.00 USD | 16,580.00 USD | 40,320.00 USD | 61,790.00 USD |
| `7D` | `316.90` | 12,660,000.00 USD | 12,660,000.00 USD | 0.00 USD | 3,030.00 USD | 10,840.00 USD | 106.47 USD |
| `7D` | `317.40` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 14,540.00 USD | 1,010.00 USD | 107.86 USD |
| `7D` | `317.90` | 12,700,000.00 USD | 12,700,000.00 USD | 0.00 USD | 21,640.00 USD | 8,200.00 USD | 201.55 USD |
| `7D` | `318.40` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 3,320.00 USD | 27,530.00 USD | 22,330.00 USD |
| `7D` | `318.90` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 11,180.00 USD | 17,970.00 USD | 37,870.00 USD |
| `7D` | `319.40` | 12,840,000.00 USD | 12,840,000.00 USD | 0.00 USD | 733.55 USD | 18,060.00 USD | 5.68 USD |
| `7D` | `319.90` | 12,870,000.00 USD | 12,870,000.00 USD | 0.00 USD | 446.22 USD | 22,230.00 USD | 5,330.00 USD |
| `7D` | `320.40` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 49,620.00 USD | 10,080.00 USD | 25,300.00 USD |
| `7D` | `320.90` | 12,950,000.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 166.45 USD | 0.00 USD |
| `7D` | `321.40` | 13,000,000.00 USD | 13,000,000.00 USD | 0.00 USD | 13,640.00 USD | 17,870.00 USD | 15,790.00 USD |
| `7D` | `321.90` | 13,010,000.00 USD | 13,010,000.00 USD | 0.00 USD | 910.57 USD | 500.60 USD | 5,250.00 USD |
| `7D` | `322.40` | 13,040,000.00 USD | 13,040,000.00 USD | 0.00 USD | 22,930.00 USD | 7,950.00 USD | 6,210.00 USD |
| `7D` | `322.90` | 13,070,000.00 USD | 13,070,000.00 USD | 0.00 USD | 16,590.00 USD | 5,830.00 USD | 0.48 USD |
| `7D` | `323.40` | 13,100,000.00 USD | 13,100,000.00 USD | 0.00 USD | 14,160.00 USD | 11,950.00 USD | 11,480.00 USD |
| `7D` | `323.90` | 13,110,000.00 USD | 13,110,000.00 USD | 0.00 USD | 269.10 USD | 692.00 USD | 0.33 USD |
| `7D` | `324.40` | 13,130,000.00 USD | 13,130,000.00 USD | 0.00 USD | 0.00 USD | 4,960.00 USD | 23,350.00 USD |
| `7D` | `324.90` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 12,280.00 USD | 0.00 USD | 15,410.00 USD |
| `7D` | `325.40` | 13,210,000.00 USD | 13,210,000.00 USD | 0.00 USD | 6,270.00 USD | 30,130.00 USD | 8,690.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `307.57M` | Total OI Tokens: `1,082,837.4 BCH`
  * 1h OI Change: `+1.36%` | 4h OI Change: `+7.94%` | 24h OI Change: `-0.97%`
  * Exchange Breakdown: Binance=`90.47M` | Bybit=`38.31M` | OKX=`24.18M` | Hyperliquid=`7.26M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `11.79K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0027%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0097%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `49.28%` | `50.72%` | `0.97` | 1,970,000.00 USD |
| `15M` | `Binance` | `42.13%` | `57.87%` | `0.73` | 572,230.00 USD |
| `15M` | `OKX` | `60.98%` | `39.02%` | `1.56` | 382,470.00 USD |
| `15M` | `Bybit` | `44.47%` | `55.53%` | `0.80` | 134,410.00 USD |
| `15M` | `KuCoin` | `52.77%` | `47.23%` | `1.12` | 18,250.00 USD |
| `15M` | `Gate` | `56.71%` | `43.29%` | `1.31` | 146,970.00 USD |
| `15M` | `Bitget` | `61.87%` | `38.13%` | `1.62` | 32,770.00 USD |
| `15M` | `BingX` | `48.41%` | `51.59%` | `0.94` | 394,700.00 USD |
| `15M` | `MEXC` | `44.43%` | `55.57%` | `0.80` | 70,160.00 USD |
| `15M` | `Bitunix` | `38.17%` | `61.83%` | `0.62` | 86,200.00 USD |
| `15M` | `Hyperliquid` | `22.68%` | `77.32%` | `0.29` | 5,020.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `38.36%` | `61.64%` | `0.62` | 100,600.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 17,270.00 USD |
| `15M` | `HTX` | `48.17%` | `51.83%` | `0.93` | 1,380.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `99.76%` | `0.24%` | `415.67` | 14,070.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 251.77 USD |
| `15M` | `Whale Positions` | `42.13%` | `57.87%` | `0.73` | 572,230.00 USD |
| `15M` | `Global Accounts` | `49.28%` | `50.72%` | `0.97` | 1,970,000.00 USD |
| `1H` | `BCH` | `45.89%` | `54.11%` | `0.85` | 13,660,000.00 USD |
| `1H` | `Binance` | `44.04%` | `55.96%` | `0.79` | 4,660,000.00 USD |
| `1H` | `OKX` | `48.58%` | `51.42%` | `0.94` | 2,450,000.00 USD |
| `1H` | `Bybit` | `45.81%` | `54.19%` | `0.85` | 969,640.00 USD |
| `1H` | `KuCoin` | `60.71%` | `39.29%` | `1.55` | 115,010.00 USD |
| `1H` | `Gate` | `44.28%` | `55.72%` | `0.79` | 1,610,000.00 USD |
| `1H` | `Bitget` | `36.23%` | `63.77%` | `0.57` | 395,990.00 USD |
| `1H` | `BingX` | `49.48%` | `50.52%` | `0.98` | 1,550,000.00 USD |
| `1H` | `MEXC` | `22.63%` | `77.37%` | `0.29` | 415,540.00 USD |
| `1H` | `Bitunix` | `46.59%` | `53.41%` | `0.87` | 701,650.00 USD |
| `1H` | `Hyperliquid` | `30.42%` | `69.58%` | `0.44` | 87,350.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.52%` | `49.48%` | `1.02` | 437,670.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.28%` | `2.72%` | `35.76` | 194,190.00 USD |
| `1H` | `HTX` | `25.09%` | `74.91%` | `0.33` | 23,850.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `53.27%` | `46.73%` | `1.14` | 33,170.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `70.47%` | `29.53%` | `2.39` | 1,360.00 USD |
| `1H` | `Whale Positions` | `44.04%` | `55.96%` | `0.79` | 4,660,000.00 USD |
| `1H` | `Global Accounts` | `45.89%` | `54.11%` | `0.85` | 13,660,000.00 USD |
| `4H` | `BCH` | `55.11%` | `44.89%` | `1.23` | 45,040,000.00 USD |
| `4H` | `Binance` | `56.64%` | `43.36%` | `1.31` | 18,260,000.00 USD |
| `4H` | `OKX` | `58.77%` | `41.23%` | `1.43` | 4,880,000.00 USD |
| `4H` | `Bybit` | `54.14%` | `45.86%` | `1.18` | 4,600,000.00 USD |
| `4H` | `KuCoin` | `47.44%` | `52.56%` | `0.90` | 2,400,000.00 USD |
| `4H` | `Gate` | `60%` | `40%` | `1.50` | 2,370,000.00 USD |
| `4H` | `Bitget` | `50.17%` | `49.83%` | `1.01` | 1,270,000.00 USD |
| `4H` | `BingX` | `36.21%` | `63.79%` | `0.57` | 2,460,000.00 USD |
| `4H` | `MEXC` | `54%` | `46%` | `1.17` | 2,200,000.00 USD |
| `4H` | `Bitunix` | `52.14%` | `47.86%` | `1.09` | 1,020,000.00 USD |
| `4H` | `Hyperliquid` | `67.08%` | `32.92%` | `2.04` | 636,510.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.26%` | `50.74%` | `0.97` | 3,660,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `99.85%` | `0.15%` | `665.67` | 942,740.00 USD |
| `4H` | `HTX` | `50.7%` | `49.3%` | `1.03` | 30,300.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.19%` | `57.81%` | `0.73` | 234,610.00 USD |
| `4H` | `Aster` | `37.89%` | `62.11%` | `0.61` | 76,040.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `56.64%` | `43.36%` | `1.31` | 18,260,000.00 USD |
| `4H` | `Global Accounts` | `55.11%` | `44.89%` | `1.23` | 45,040,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `269.85` | `271.90` | `269.85` | `274.77` | `269.65` | 1,156,441.43 USD | 590,842.24 USD | 565,599.19 USD | 25,243.06 USD | `+2.18%` | `25B / 11S` |
| `5:00 UTC` | `276.07` | `277.34` | `276.07` | `279.99` | `274.27` | 2,478,226.90 USD | 1,049,714.12 USD | 1,428,512.78 USD | -378,798.66 USD | `-15.29%` | `20B / 19S` |
| `0:00 UTC` | `277.53` | `277.66` | `277.53` | `278.97` | `276.87` | 2,086,885.56 USD | 726,779.97 USD | 1,360,105.59 USD | -633,325.62 USD | `-30.35%` | `5B / 32S` |
| `5:00 UTC` | `277.43` | `276.49` | `277.43` | `277.51` | `275.76` | 760,717.24 USD | 265,897.12 USD | 494,820.12 USD | -228,923.01 USD | `-30.09%` | `19B / 60S` |
| `0:00 UTC` | `278.95` | `278.11` | `278.95` | `279.11` | `276.01` | 1,117,022.83 USD | 460,337.30 USD | 656,685.53 USD | -196,348.23 USD | `-17.58%` | `14B / 26S` |
| `5:00 UTC` | `278.75` | `278.95` | `278.75` | `279.99` | `277.87` | 899,043.00 USD | 507,720.36 USD | 391,322.65 USD | 116,397.71 USD | `+12.95%` | `23B / 14S` |
| `0:00 UTC` | `281.80` | `281.23` | `281.80` | `282.56` | `279.38` | 1,860,973.61 USD | 1,019,031.48 USD | 841,942.13 USD | 177,089.35 USD | `+9.52%` | `29B / 17S` |
| `5:00 UTC` | `282.40` | `283.39` | `282.40` | `284.76` | `281.82` | 2,261,635.40 USD | 1,044,285.27 USD | 1,217,350.14 USD | -173,064.87 USD | `-7.65%` | `26B / 23S` |
| `0:00 UTC` | `287.03` | `284.86` | `287.03` | `287.15` | `282.35` | 3,497,591.91 USD | 1,841,198.98 USD | 1,656,392.94 USD | 184,806.04 USD | `+5.28%` | `24B / 10S` |
| `5:00 UTC` | `285.03` | `285.28` | `285.03` | `286.67` | `284.13` | 839,435.71 USD | 343,904.64 USD | 495,531.07 USD | -151,626.43 USD | `-18.06%` | `10B / 35S` |

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
| `5m` | 134,260.00 USD | 7,090.00 USD | **`ACCUMULATION`** |
| `15m` | 154,460.00 USD | -642,770.00 USD | **`DISTRIBUTION`** |
| `30m` | 380,070.00 USD | -350,060.00 USD | **`ACCUMULATION`** |
| `1h` | 585,010.00 USD | -94,740.00 USD | **`ACCUMULATION`** |
| `2h` | 503,250.00 USD | -1,630,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 1,030,000.00 USD | 2,810,000.00 USD | **`ACCUMULATION`** |
| `6h` | 216,790.00 USD | -1,760,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 150,550.00 USD | -2,060,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -174,120.00 USD | -1,300,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 131,600.00 USD | -4,070,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -805,630.00 USD | -15,940,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,330,000.00 USD | -138,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+134.26K` | 15m=`+154.46K` | 1h=`+585.01K` | 24h=`+131.60K`
* Futures Capital Netflows: 5m=`+7.09K` | 15m=`-642.77K` | 1h=`-94.74K` | 24h=`-4.07M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `269.75` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `264.90` (Risk Distance: `4.85` pts)
  * +2.5R Take Profit: `281.87`
  * Mathematical Lot Sizing: **`2.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `283.45` (Risk Distance: `4.85` pts)
  * +2.5R Take Profit: `266.48`
  * Mathematical Lot Sizing: **`2.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`286.42`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
