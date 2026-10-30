# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 14:38:47 IST` (`2026-10-30 09:08:47 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `278.36` | **Live Ask Quote**: `278.94` | **Mid Price**: `278.65`
- **Spread Points**: `580.00` | **Spread BPS**: `20.81 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `276.48` | VWAP Z-Score: `+0.30` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.09` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `41.75` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.20` | Lower -3.00σ Band: `257.77`
  * Upper +2.51σ Band: `292.14` | Lower -2.51σ Band: `260.82`
  * Upper +2.01σ Band: `289.02` | Lower -2.01σ Band: `263.94`
  * Upper +2.00σ Band: `288.96` | Lower -2.00σ Band: `264.00`
  * Upper +1.28σ Band: `284.47` | Lower -1.28σ Band: `268.50`
  * Upper +1.00σ Band: `282.72` | Lower -1.00σ Band: `270.24`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`281.11` | EMA-20=`281.25` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.35` (Slope: `+0.0000`) | EMA-100=`280.88`
  * Institutional Anchors: EMA-144=`281.74` | EMA-200=`283.32` (Slope: `-0.0558`) | EMA-233=`284.29`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `281.44` (Distance: `-0.87%`)
  * Point of Control (POC) = `276.23` (Distance: `+1.00%`)
  * Value Area Low (VAL) = `268.01` (Distance: `+4.10%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`280.32` | Low=`276.98`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `277.54` - `279.76`
  * Optimal Trade Entry (OTE 0.705): `279.21`
  * Structural Invalidation Anchor (0.786): `280.88`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `279.96` | `280.56` | `279.31` | `280.20` | `1,310` | 366,659.34 USD | 15,459.92 USD | `+4.22%` | -1,920,387.21 USD | `+0.32` | **`BULLISH`** | `NEUTRAL CHOP` |
| `5m` | `280.19` | `280.19` | `278.73` | `279.02` | `2,447` | 682,704.78 USD | 155,842.05 USD | `+22.83%` | -1,764,545.16 USD | `+1.37` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `279.03` | `279.09` | `278.54` | `279.09` | `810` | 225,728.10 USD | 93,667.36 USD | `+41.50%` | -1,670,877.80 USD | `+0.83` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `281.87` | `281.93` | `280.02` | `280.23` | `3,415` | 959,751.07 USD | -262,200.48 USD | `-27.32%` | -1,784,981.05 USD | `-1.25` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `280.24` | `280.56` | `278.73` | `279.02` | `5,459` | 1,525,848.29 USD | 161,863.30 USD | `+10.61%` | -1,623,117.75 USD | `+0.93` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `279.03` | `279.09` | `278.54` | `279.09` | `810` | 225,728.10 USD | 93,667.36 USD | `+41.50%` | -1,529,450.39 USD | `+0.60` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `283.68` | `284.86` | `280.79` | `281.78` | `11,868` | 3,357,238.13 USD | -360,522.64 USD | `-10.74%` | -1,826,347.97 USD | `-0.33` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `278.73` | `279.02` | `16,468` | 4,630,594.81 USD | 275,996.65 USD | `+5.96%` | -1,550,351.32 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `279.03` | `279.09` | `278.54` | `279.09` | `810` | 225,728.10 USD | 93,667.36 USD | `+41.50%` | -1,456,683.96 USD | `+0.28` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `279.09` | `17,277` | 4,856,322.92 USD | 369,664.01 USD | `+7.61%` | -1,370,246.64 USD | `+0.50` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `283.64` | `278.54` | `279.09` | `17,277` | 4,856,322.92 USD | 369,664.01 USD | `+7.61%` | -1,370,246.64 USD | `+0.50` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`278.65`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1985` | `0x12d2...f97f` | `LONG` | 1,014,793.77 USD | `3,627,243,000,000.00` | `303.26` | `279.78` | `0.000000` | -85,205.56 USD | `-8.40%` | `10X Cross` |

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
| `7D` | `Long Liquidation` | `234.80` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 9,970,000.00 USD | 9,970,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 9,960,000.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 9,950,000.00 USD | 9,950,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 9,940,000.00 USD | 9,940,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 23,750.00 USD | 68,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 9,900,000.00 USD | 9,900,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 9,890,000.00 USD | 9,890,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `238.50` | 3,790.00 USD | 44,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `238.80` | 9,870,000.00 USD | 9,870,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 9,850,000.00 USD | 9,850,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 41,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.30` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 9,830,000.00 USD | 9,830,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 9,820,000.00 USD | 9,820,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 7,400.00 USD | 40,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 9,810,000.00 USD | 9,810,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 9,800,000.00 USD | 9,800,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 32,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 9,720,000.00 USD | 9,720,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 9,710,000.00 USD | 9,710,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 31,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 9,690,000.00 USD | 9,690,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 29,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 9,640,000.00 USD | 9,640,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 9,620,000.00 USD | 9,620,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 9,590,000.00 USD | 9,590,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 9,580,000.00 USD | 9,580,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 9,530,000.00 USD | 9,530,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 9,530,000.00 USD | 9,530,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,490,000.00 USD | 9,490,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,480,000.00 USD | 9,480,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,460,000.00 USD | 9,460,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,360,000.00 USD | 9,360,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,280,000.00 USD | 9,280,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,170,000.00 USD | 9,170,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 23,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.70` | 4,780,000.00 USD | 4,780,000.00 USD | 8,490.00 USD | 4,800.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,070,000.00 USD | 9,070,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.10` | 4,750,000.00 USD | 4,750,000.00 USD | 19,750.00 USD | 35,980.00 USD | 13,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 8,940,000.00 USD | 8,940,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.50` | 4,680,000.00 USD | 4,680,000.00 USD | 5,500.00 USD | 41,320.00 USD | 22,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.80` | 8,790,000.00 USD | 8,790,000.00 USD | 75,110.00 USD | 76,000.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.90` | 4,620,000.00 USD | 4,620,000.00 USD | 38,740.00 USD | 32,460.00 USD | 15,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.30` | 4,530,000.00 USD | 4,530,000.00 USD | 21,350.00 USD | 8,160.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 8,590,000.00 USD | 8,590,000.00 USD | 69,530.00 USD | 39,900.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 21,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.70` | 4,500,000.00 USD | 4,500,000.00 USD | 10,940.00 USD | 7,260.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,470,000.00 USD | 8,470,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.10` | 4,470,000.00 USD | 4,470,000.00 USD | 5,760.00 USD | 2,060.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,380,000.00 USD | 8,380,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.50` | 4,460,000.00 USD | 4,460,000.00 USD | 25,230.00 USD | 18,830.00 USD | 20,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,280,000.00 USD | 8,280,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.90` | 4,400,000.00 USD | 4,400,000.00 USD | 6,840.00 USD | 7,060.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.30` | 4,380,000.00 USD | 4,380,000.00 USD | 8,310.00 USD | 4,360.00 USD | 1,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,190,000.00 USD | 8,190,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.70` | 4,360,000.00 USD | 4,360,000.00 USD | 820.64 USD | 13,630.00 USD | 29.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,070,000.00 USD | 8,070,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.10` | 4,350,000.00 USD | 4,350,000.00 USD | 17,840.00 USD | 11,140.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 7,900,000.00 USD | 7,900,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.50` | 4,310,000.00 USD | 4,310,000.00 USD | 6,510.00 USD | 34,960.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 7,820,000.00 USD | 7,820,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.90` | 4,250,000.00 USD | 4,250,000.00 USD | 16,650.00 USD | 862.50 USD | 15,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.30` | 4,210,000.00 USD | 4,210,000.00 USD | 5,470.00 USD | 41,870.00 USD | 15,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 7,760,000.00 USD | 7,760,000.00 USD | 54,130.00 USD | 10,260.00 USD | 40,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.70` | 4,150,000.00 USD | 4,150,000.00 USD | 5,340.00 USD | 5,660.00 USD | 8,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 7,650,000.00 USD | 7,650,000.00 USD | 32,750.00 USD | 13,750.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.10` | 4,130,000.00 USD | 4,130,000.00 USD | 14,160.00 USD | 1,230.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 7,540,000.00 USD | 7,540,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.50` | 4,100,000.00 USD | 4,100,000.00 USD | 1,190.00 USD | 5,680.00 USD | 8,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 101.20 USD | 17,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,510,000.00 USD | 7,510,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.90` | 4,090,000.00 USD | 4,090,000.00 USD | 4,520.00 USD | 1,550.00 USD | 37,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.30` | 4,040,000.00 USD | 4,040,000.00 USD | 24,350.00 USD | 15,770.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,450,000.00 USD | 7,450,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 1,840.00 USD | 16,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.70` | 3,980,000.00 USD | 3,980,000.00 USD | 18,720.00 USD | 30,550.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,220,000.00 USD | 7,220,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.10` | 3,890,000.00 USD | 3,890,000.00 USD | 14,580.00 USD | 13,100.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,040,000.00 USD | 7,040,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.50` | 3,850,000.00 USD | 3,850,000.00 USD | 13,390.00 USD | 4,330.00 USD | 32,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 6,990,000.00 USD | 6,990,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.90` | 3,800,000.00 USD | 3,800,000.00 USD | 44,930.00 USD | 32,920.00 USD | 17,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.30` | 3,710,000.00 USD | 3,710,000.00 USD | 13,640.00 USD | 6,820.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 6,830,000.00 USD | 6,830,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 15,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.70` | 3,680,000.00 USD | 3,680,000.00 USD | 7,410.00 USD | 25,460.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 6,610,000.00 USD | 6,610,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.10` | 3,610,000.00 USD | 3,610,000.00 USD | 8,190.00 USD | 30,680.00 USD | 37,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,480,000.00 USD | 6,480,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.50` | 3,540,000.00 USD | 3,540,000.00 USD | 18,780.00 USD | 43,520.00 USD | 28,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,320,000.00 USD | 6,320,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.90` | 3,450,000.00 USD | 3,450,000.00 USD | 4,430.00 USD | 70,050.00 USD | 36,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.30` | 3,340,000.00 USD | 3,340,000.00 USD | 34,480.00 USD | 4,710.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,120,000.00 USD | 6,120,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.70` | 3,280,000.00 USD | 3,280,000.00 USD | 629.76 USD | 13,170.00 USD | 15,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 5,950,000.00 USD | 5,950,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.10` | 3,250,000.00 USD | 3,250,000.00 USD | 9,320.00 USD | 4,000.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 5,790,000.00 USD | 5,790,000.00 USD | 33,590.00 USD | 13,710.00 USD | 169.66 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.50` | 3,230,000.00 USD | 3,230,000.00 USD | 30,390.00 USD | 343.40 USD | 74,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 5,740,000.00 USD | 5,740,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.90` | 3,120,000.00 USD | 3,120,000.00 USD | 32,780.00 USD | 38,370.00 USD | 45,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.30` | 3,010,000.00 USD | 3,010,000.00 USD | 25,870.00 USD | 17,340.00 USD | 56.02 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,230,000.00 USD | 5,230,000.00 USD | 48,230.00 USD | 1,170.00 USD | 128.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.70` | 2,960,000.00 USD | 2,960,000.00 USD | 975.50 USD | 10,060.00 USD | 20,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,180,000.00 USD | 5,180,000.00 USD | 33,470.00 USD | 21,870.00 USD | 198.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.10` | 2,930,000.00 USD | 2,930,000.00 USD | 33,730.00 USD | 3,530.00 USD | 33,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,130,000.00 USD | 5,130,000.00 USD | 256,440.00 USD | 2,330.00 USD | 33,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.50` | 2,860,000.00 USD | 2,860,000.00 USD | 63,850.00 USD | 1,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 4,830,000.00 USD | 4,830,000.00 USD | 69,380.00 USD | 0.00 USD | 106.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.90` | 2,800,000.00 USD | 2,800,000.00 USD | 12,120.00 USD | 377.24 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.30` | 2,780,000.00 USD | 2,780,000.00 USD | 4,020.00 USD | 13,390.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 4,760,000.00 USD | 4,760,000.00 USD | 216,090.00 USD | 645.20 USD | 17.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.70` | 2,760,000.00 USD | 2,760,000.00 USD | 14,560.00 USD | 8,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 4,550,000.00 USD | 4,550,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.10` | 2,740,000.00 USD | 2,740,000.00 USD | 43,820.00 USD | 54,430.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,350,000.00 USD | 4,350,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.50` | 2,630,000.00 USD | 2,630,000.00 USD | 8,010.00 USD | 44,550.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,160,000.00 USD | 4,160,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.90` | 2,570,000.00 USD | 2,570,000.00 USD | 4,660.00 USD | 28,320.00 USD | 18,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.30` | 2,510,000.00 USD | 2,510,000.00 USD | 17,480.00 USD | 35,070.00 USD | 46,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 3,870,000.00 USD | 3,870,000.00 USD | 199,420.00 USD | 150,080.00 USD | 62,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.70` | 2,420,000.00 USD | 2,420,000.00 USD | 12,930.00 USD | 15,520.00 USD | 131.67 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,460,000.00 USD | 3,460,000.00 USD | 23,340.00 USD | 17,480.00 USD | 105.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.10` | 2,390,000.00 USD | 2,390,000.00 USD | 16,010.00 USD | 1,330.00 USD | 78.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 3,490.00 USD | 148.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.50` | 2,370,000.00 USD | 2,370,000.00 USD | 110.70 USD | 16,480.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 1,920.00 USD | 240.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.90` | 2,340,000.00 USD | 2,340,000.00 USD | 8,300.00 USD | 2,120.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.30` | 2,330,000.00 USD | 2,330,000.00 USD | 40,330.00 USD | 12,570.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.70` | 2,270,000.00 USD | 2,270,000.00 USD | 11,770.00 USD | 2,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,410,000.00 USD | 3,410,000.00 USD | 33,050.00 USD | 0.00 USD | 120.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.10` | 2,260,000.00 USD | 2,260,000.00 USD | 181.20 USD | 13,990.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.30` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.50` | 2,240,000.00 USD | 2,240,000.00 USD | 12,710.00 USD | 1,940.00 USD | 9,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,360,000.00 USD | 3,360,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.90` | 2,210,000.00 USD | 2,210,000.00 USD | 13,310.00 USD | 32,980.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.30` | 2,160,000.00 USD | 2,160,000.00 USD | 23,380.00 USD | 31,900.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.70` | 2,090,000.00 USD | 2,090,000.00 USD | 36,620.00 USD | 27,760.00 USD | 86,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,220,000.00 USD | 3,220,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.10` | 1,940,000.00 USD | 1,940,000.00 USD | 36,160.00 USD | 75,560.00 USD | 25,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.50` | 1,800,000.00 USD | 1,800,000.00 USD | 4,710.00 USD | 51,210.00 USD | 29,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 2,730,000.00 USD | 2,730,000.00 USD | 181,410.00 USD | 0.00 USD | 29,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.90` | 1,710,000.00 USD | 1,710,000.00 USD | 157,240.00 USD | 80,800.00 USD | 62,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.30` | 1,410,000.00 USD | 1,410,000.00 USD | 159,370.00 USD | 30,340.00 USD | 12,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,520,000.00 USD | 2,520,000.00 USD | 535,520.00 USD | 34,960.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.70` | 1,210,000.00 USD | 1,210,000.00 USD | 156,370.00 USD | 19,960.00 USD | 41,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 1,860,000.00 USD | 1,860,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.10` | 992,290.00 USD | 992,290.00 USD | 20,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,330,000.00 USD | 1,330,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.50` | 971,380.00 USD | 971,380.00 USD | 14,520.00 USD | 0.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,250,000.00 USD | 1,250,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.90` | 930,150.00 USD | 930,150.00 USD | 54,620.00 USD | 34,910.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.30` | 800,270.00 USD | 800,270.00 USD | 139,460.00 USD | 0.00 USD | 3,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,150,000.00 USD | 1,150,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.70` | 657,590.00 USD | 657,590.00 USD | 11,880.00 USD | 27,070.00 USD | 20,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 821,720.00 USD | 821,720.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.10` | 598,330.00 USD | 598,330.00 USD | 25,410.00 USD | 7,450.00 USD | 19,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 805,630.00 USD | 805,630.00 USD | 152,190.00 USD | 77,800.00 USD | 140,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.50` | 546,120.00 USD | 546,120.00 USD | 26,920.00 USD | 14,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 434,740.00 USD | 434,740.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.90` | 504,820.00 USD | 504,820.00 USD | 16,560.00 USD | 33,120.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.30` | 426,360.00 USD | 426,360.00 USD | 42,620.00 USD | 132,160.00 USD | 77,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 217,150.00 USD | 217,150.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.70` | 173,640.00 USD | 173,640.00 USD | 55,370.00 USD | 22,670.00 USD | 95,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.80` | 70,380.00 USD | 70,380.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `278.80` | 140,750.00 USD | 140,750.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.10` | 86,660.00 USD | 86,660.00 USD | 0.00 USD | 86,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.30` | 143,410.00 USD | 143,410.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.50` | 127,750.00 USD | 127,750.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `279.80` | 201,450.00 USD | 201,450.00 USD | 0.00 USD | 0.00 USD | 58,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `279.90` | 183,410.00 USD | 183,410.00 USD | 0.00 USD | 0.00 USD | 55,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.30` | 288,520.00 USD | 288,520.00 USD | 0.00 USD | 18,280.00 USD | 86,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.30` | 218,810.00 USD | 218,810.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `280.70` | 340,800.00 USD | 340,800.00 USD | 4,150.00 USD | 37,910.00 USD | 10,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `280.80` | 234,350.00 USD | 234,350.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.30` | 331,760.00 USD | 331,760.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `281.80` | 454,150.00 USD | 454,150.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `281.90` | 344,940.00 USD | 344,940.00 USD | 0.00 USD | 0.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `282.30` | 353,210.00 USD | 353,210.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `282.30` | 478,370.00 USD | 478,370.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.30` | 481,820.00 USD | 481,820.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `283.50` | 354,500.00 USD | 354,500.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 483,810.00 USD | 483,810.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 485,380.00 USD | 485,380.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 540,760.00 USD | 540,760.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.10` | 421,990.00 USD | 421,990.00 USD | 25,820.00 USD | 0.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 895,810.00 USD | 895,810.00 USD | 127,830.00 USD | 227,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.50` | 478,210.00 USD | 478,210.00 USD | 25,860.00 USD | 30,340.00 USD | 9.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 1,130,000.00 USD | 1,130,000.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.90` | 518,420.00 USD | 518,420.00 USD | 16,570.00 USD | 434.90 USD | 23,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.30` | 532,480.00 USD | 532,480.00 USD | 13,210.00 USD | 851.39 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 1,170,000.00 USD | 1,170,000.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.70` | 584,550.00 USD | 584,550.00 USD | 16,810.00 USD | 5,130.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,420,000.00 USD | 1,420,000.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.10` | 797,750.00 USD | 797,750.00 USD | 67,040.00 USD | 58,340.00 USD | 87,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,620,000.00 USD | 1,620,000.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.50` | 949,510.00 USD | 949,510.00 USD | 73,550.00 USD | 21,410.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `287.80` | 2,020,000.00 USD | 2,020,000.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.90` | 1,040,000.00 USD | 1,040,000.00 USD | 13,160.00 USD | 28,020.00 USD | 53,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.30` | 1,160,000.00 USD | 1,160,000.00 USD | 73,330.00 USD | 25,900.00 USD | 13,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.70` | 1,240,000.00 USD | 1,240,000.00 USD | 34,730.00 USD | 32,420.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 2,310,000.00 USD | 2,310,000.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.10` | 1,310,000.00 USD | 1,310,000.00 USD | 15,470.00 USD | 25,200.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.50` | 1,500,000.00 USD | 1,500,000.00 USD | 20,690.00 USD | 69,700.00 USD | 96,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,720,000.00 USD | 2,720,000.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.90` | 1,710,000.00 USD | 1,710,000.00 USD | 84,710.00 USD | 40,970.00 USD | 83,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.30` | 1,870,000.00 USD | 1,870,000.00 USD | 21,790.00 USD | 96,150.00 USD | 44,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,780,000.00 USD | 2,780,000.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.70` | 2,080,000.00 USD | 2,080,000.00 USD | 61,600.00 USD | 68,580.00 USD | 77,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,870,000.00 USD | 2,870,000.00 USD | 30,380.00 USD | 1,760.00 USD | 58,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.10` | 2,160,000.00 USD | 2,160,000.00 USD | 19,350.00 USD | 37,030.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,920,000.00 USD | 2,920,000.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.50` | 2,200,000.00 USD | 2,200,000.00 USD | 18,130.00 USD | 27,620.00 USD | 16.83 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `291.80` | 3,120,000.00 USD | 3,120,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.90` | 2,250,000.00 USD | 2,250,000.00 USD | 1,150.00 USD | 26,030.00 USD | 22,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.30` | 2,320,000.00 USD | 2,320,000.00 USD | 20,890.00 USD | 34,520.00 USD | 11,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 3,200,000.00 USD | 3,200,000.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.70` | 2,390,000.00 USD | 2,390,000.00 USD | 29,970.00 USD | 33,570.00 USD | 5,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 3,300,000.00 USD | 3,300,000.00 USD | 887.27 USD | 101,280.00 USD | 138.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.10` | 2,460,000.00 USD | 2,460,000.00 USD | 53,250.00 USD | 9,930.00 USD | 13,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,460,000.00 USD | 3,460,000.00 USD | 33,580.00 USD | 132,770.00 USD | 36.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.50` | 2,550,000.00 USD | 2,550,000.00 USD | 16,430.00 USD | 44,740.00 USD | 27,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,530,000.00 USD | 3,530,000.00 USD | 38,790.00 USD | 1,860.00 USD | 20,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.90` | 2,710,000.00 USD | 2,710,000.00 USD | 85,140.00 USD | 11,340.00 USD | 55,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.30` | 2,800,000.00 USD | 2,800,000.00 USD | 15,230.00 USD | 31,680.00 USD | 44,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,930,000.00 USD | 3,930,000.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.70` | 3,110,000.00 USD | 3,110,000.00 USD | 108,820.00 USD | 74,700.00 USD | 129,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 4,190,000.00 USD | 4,190,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.10` | 3,240,000.00 USD | 3,240,000.00 USD | 12,380.00 USD | 27,090.00 USD | 89,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,670,000.00 USD | 4,670,000.00 USD | 46,330.00 USD | 82,780.00 USD | 345,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.50` | 3,420,000.00 USD | 3,420,000.00 USD | 43,990.00 USD | 45,370.00 USD | 86,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 5,110,000.00 USD | 5,110,000.00 USD | 165,320.00 USD | 82,100.00 USD | 197,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.90` | 3,590,000.00 USD | 3,590,000.00 USD | 74,790.00 USD | 42,250.00 USD | 61,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.30` | 3,810,000.00 USD | 3,810,000.00 USD | 79,090.00 USD | 102,190.00 USD | 36,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 5,440,000.00 USD | 5,440,000.00 USD | 43,710.00 USD | 167,940.00 USD | 120,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `296.70` | 3,950,000.00 USD | 3,950,000.00 USD | 24,230.00 USD | 31,530.00 USD | 86,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,780,000.00 USD | 5,780,000.00 USD | 133,820.00 USD | 3,570.00 USD | 201,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.10` | 4,050,000.00 USD | 4,050,000.00 USD | 54,810.00 USD | 1,780.00 USD | 40,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,920,000.00 USD | 5,920,000.00 USD | 78,980.00 USD | 54,960.00 USD | 72.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.50` | 4,100,000.00 USD | 4,100,000.00 USD | 10,420.00 USD | 11,090.00 USD | 27,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 6,150,000.00 USD | 6,150,000.00 USD | 47,530.00 USD | 99,810.00 USD | 89,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.90` | 4,140,000.00 USD | 4,140,000.00 USD | 15,560.00 USD | 8,370.00 USD | 16,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.30` | 4,290,000.00 USD | 4,290,000.00 USD | 56,520.00 USD | 3,080.00 USD | 93,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 6,300,000.00 USD | 6,300,000.00 USD | 32,650.00 USD | 45,150.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.70` | 4,400,000.00 USD | 4,400,000.00 USD | 23,620.00 USD | 514.82 USD | 80,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,380,000.00 USD | 6,380,000.00 USD | 69,820.00 USD | 12,530.00 USD | 112.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.10` | 4,440,000.00 USD | 4,440,000.00 USD | 8,280.00 USD | 7,650.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,500,000.00 USD | 6,500,000.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.50` | 4,510,000.00 USD | 4,510,000.00 USD | 35,600.00 USD | 13,920.00 USD | 19,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,550,000.00 USD | 6,550,000.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.90` | 4,560,000.00 USD | 4,560,000.00 USD | 3,970.00 USD | 12,410.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.30` | 4,660,000.00 USD | 4,660,000.00 USD | 31,890.00 USD | 30,720.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,590,000.00 USD | 6,590,000.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.70` | 4,690,000.00 USD | 4,690,000.00 USD | 10,590.00 USD | 823.51 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,730,000.00 USD | 6,730,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.10` | 4,740,000.00 USD | 4,740,000.00 USD | 322.75 USD | 15,860.00 USD | 29,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 7,020,000.00 USD | 7,020,000.00 USD | 73,320.00 USD | 58,690.00 USD | 150,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.50` | 4,790,000.00 USD | 4,790,000.00 USD | 19,490.00 USD | 210.12 USD | 36,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 7,260,000.00 USD | 7,260,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.90` | 4,860,000.00 USD | 4,860,000.00 USD | 21,000.00 USD | 35,950.00 USD | 10,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.30` | 4,890,000.00 USD | 4,890,000.00 USD | 5,200.00 USD | 5,210.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 7,450,000.00 USD | 7,450,000.00 USD | 1,560.00 USD | 181,550.00 USD | 35.08 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `302.50` | 3,640.00 USD | 10,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `302.70` | 4,950,000.00 USD | 4,950,000.00 USD | 14,490.00 USD | 11,810.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,670,000.00 USD | 7,670,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.10` | 4,980,000.00 USD | 4,980,000.00 USD | 21,280.00 USD | 2,400.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 1,950.00 USD | 183.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.50` | 4,980,000.00 USD | 4,980,000.00 USD | 318.69 USD | 1,960.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,730,000.00 USD | 7,730,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.90` | 5,030,000.00 USD | 5,030,000.00 USD | 21,670.00 USD | 1,900.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.30` | 5,050,000.00 USD | 5,050,000.00 USD | 491.66 USD | 2,430.00 USD | 21,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,760,000.00 USD | 7,760,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.70` | 5,110,000.00 USD | 5,110,000.00 USD | 9,880.00 USD | 1,650.00 USD | 44,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,810,000.00 USD | 7,810,000.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.10` | 5,130,000.00 USD | 5,130,000.00 USD | 9,500.00 USD | 7,030.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 8,240,000.00 USD | 8,240,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.50` | 5,130,000.00 USD | 5,130,000.00 USD | 3,060.00 USD | 440.72 USD | 10.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 8,390,000.00 USD | 8,390,000.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.90` | 5,150,000.00 USD | 5,150,000.00 USD | 7,430.00 USD | 5,640.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.30` | 5,160,000.00 USD | 5,160,000.00 USD | 6,940.00 USD | 317.96 USD | 6,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,540,000.00 USD | 8,540,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.70` | 5,200,000.00 USD | 5,200,000.00 USD | 2,170.00 USD | 22,610.00 USD | 9,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,780,000.00 USD | 8,780,000.00 USD | 94,690.00 USD | 74,510.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.10` | 5,260,000.00 USD | 5,260,000.00 USD | 20,640.00 USD | 25,250.00 USD | 21,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 9,080,000.00 USD | 9,080,000.00 USD | 27,410.00 USD | 136,370.00 USD | 134,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.50` | 5,330,000.00 USD | 5,330,000.00 USD | 24,040.00 USD | 34,310.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 9,380,000.00 USD | 9,380,000.00 USD | 126,860.00 USD | 113,210.00 USD | 60,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.90` | 5,390,000.00 USD | 5,390,000.00 USD | 17,750.00 USD | 26,730.00 USD | 15,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.30` | 5,420,000.00 USD | 5,420,000.00 USD | 19,750.00 USD | 7,520.00 USD | 2,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,730,000.00 USD | 9,730,000.00 USD | 169,010.00 USD | 66,670.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.70` | 5,430,000.00 USD | 5,430,000.00 USD | 5,080.00 USD | 275.30 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,900,000.00 USD | 9,900,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.10` | 5,440,000.00 USD | 5,440,000.00 USD | 4,310.00 USD | 6,190.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 10,000,000.00 USD | 10,000,000.00 USD | 34,260.00 USD | 36,030.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.50` | 5,470,000.00 USD | 5,470,000.00 USD | 10,940.00 USD | 8,710.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 10,350,000.00 USD | 10,350,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.90` | 5,490,000.00 USD | 5,490,000.00 USD | 17,100.00 USD | 82.82 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.30` | 5,500,000.00 USD | 5,500,000.00 USD | 112.30 USD | 5,010.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,610,000.00 USD | 10,610,000.00 USD | 62,230.00 USD | 108,410.00 USD | 80,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.70` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 3,980.00 USD | 1,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,730,000.00 USD | 10,730,000.00 USD | 60,910.00 USD | 51,380.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.10` | 5,510,000.00 USD | 5,510,000.00 USD | 5,080.00 USD | 174.00 USD | 34.32 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,970,000.00 USD | 10,970,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.50` | 5,530,000.00 USD | 5,530,000.00 USD | 7,350.00 USD | 8,680.00 USD | 14.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 11,030,000.00 USD | 11,030,000.00 USD | 19,570.00 USD | 11,240.00 USD | 25,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.90` | 5,540,000.00 USD | 5,540,000.00 USD | 888.84 USD | 6,840.00 USD | 4,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.30` | 5,580,000.00 USD | 5,580,000.00 USD | 6,510.00 USD | 14,240.00 USD | 17,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 11,110,000.00 USD | 11,110,000.00 USD | 43,780.00 USD | 11,410.00 USD | 27,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.70` | 5,610,000.00 USD | 5,610,000.00 USD | 15,760.00 USD | 419.02 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 11,180,000.00 USD | 11,180,000.00 USD | 29,070.00 USD | 14,880.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.10` | 5,630,000.00 USD | 5,630,000.00 USD | 1,620.00 USD | 12,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 11,250,000.00 USD | 11,250,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.50` | 5,650,000.00 USD | 5,650,000.00 USD | 8,130.00 USD | 7,210.00 USD | 10,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 11,330,000.00 USD | 11,330,000.00 USD | 33,220.00 USD | 1,570.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.90` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 4,260.00 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 11,420,000.00 USD | 11,420,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,450,000.00 USD | 11,450,000.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 11,460,000.00 USD | 11,460,000.00 USD | 500.10 USD | 547.95 USD | 9.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,540,000.00 USD | 11,540,000.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,640,000.00 USD | 11,640,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,700,000.00 USD | 11,700,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,710,000.00 USD | 11,710,000.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,740,000.00 USD | 11,740,000.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 11,810,000.00 USD | 11,810,000.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `65.50` | 211,350.00 USD | 0.00 USD | 2,690.00 USD | `-76.51%` | `41,012,000,000.00` |
| `Live` | `Long` | `77.50` | 208,670.00 USD | 0.00 USD | 556.06 USD | `-72.21%` | `7,175,000,000.00` |
| `Live` | `Long` | `85.50` | 208,110.00 USD | 0.00 USD | 1,120.00 USD | `-69.34%` | `13,105,000,000.00` |
| `Live` | `Long` | `92.50` | 206,990.00 USD | 0.00 USD | 349.65 USD | `-66.83%` | `3,780,000,000.00` |
| `Live` | `Long` | `95.50` | 206,640.00 USD | 0.00 USD | 920.05 USD | `-65.75%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 205,720.00 USD | 0.00 USD | 6,400.00 USD | `-63.60%` | `63,008,000,000.00` |
| `Live` | `Long` | `102.50` | 199,330.00 USD | 0.00 USD | 4,080.00 USD | `-63.24%` | `39,797,000,000.00` |
| `Live` | `Long` | `107.50` | 195,250.00 USD | 0.00 USD | 107.50 USD | `-61.45%` | `1,000,000,000.00` |
| `Live` | `Long` | `109.50` | 195,140.00 USD | 0.00 USD | 212.76 USD | `-60.73%` | `1,943,000,000.00` |
| `Live` | `Long` | `118.50` | 194,930.00 USD | 0.00 USD | 212.35 USD | `-57.51%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 194,710.00 USD | 0.00 USD | 124.46 USD | `-56.07%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 194,590.00 USD | 0.00 USD | 658.18 USD | `-54.64%` | `5,203,000,000.00` |
| `Live` | `Long` | `128.50` | 193,930.00 USD | 0.00 USD | 1,930.00 USD | `-53.92%` | `15,000,000,000.00` |
| `Live` | `Long` | `130.50` | 192,000.00 USD | 0.00 USD | 130.50 USD | `-53.20%` | `1,000,000,000.00` |
| `Live` | `Long` | `132.50` | 191,870.00 USD | 0.00 USD | 3,310.00 USD | `-52.49%` | `25,000,000,000.00` |
| `Live` | `Long` | `147.50` | 188,560.00 USD | 0.00 USD | 895.47 USD | `-47.11%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 187,660.00 USD | 0.00 USD | 1,270.00 USD | `-46.75%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 186,400.00 USD | 0.00 USD | 2,370.00 USD | `-46.39%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 184,030.00 USD | 0.00 USD | 303.78 USD | `-45.32%` | `1,992,000,000.00` |
| `Live` | `Long` | `161.50` | 183,730.00 USD | 0.00 USD | 1,550.00 USD | `-42.09%` | `9,599,000,000.00` |
| `Live` | `Long` | `162.50` | 182,180.00 USD | 0.00 USD | 325.00 USD | `-41.73%` | `2,000,000,000.00` |
| `Live` | `Long` | `167.50` | 181,850.00 USD | 0.00 USD | 8,660.00 USD | `-39.94%` | `51,706,000,000.00` |
| `Live` | `Long` | `168.50` | 173,190.00 USD | 0.00 USD | 1,280.00 USD | `-39.58%` | `7,572,000,000.00` |
| `Live` | `Long` | `170.50` | 171,920.00 USD | 0.00 USD | 426.25 USD | `-38.86%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 171,490.00 USD | 0.00 USD | 169.96 USD | `-37.43%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 171,320.00 USD | 0.00 USD | 516.67 USD | `-37.07%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 170,800.00 USD | 0.00 USD | 373.83 USD | `-36.71%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 170,430.00 USD | 0.00 USD | 808.66 USD | `-33.84%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 169,620.00 USD | 0.00 USD | 418.28 USD | `-32.41%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 169,200.00 USD | 0.00 USD | 694.75 USD | `-31.69%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 168,510.00 USD | 0.00 USD | 858.49 USD | `-31.33%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 167,650.00 USD | 0.00 USD | 1,490.00 USD | `-30.97%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 166,160.00 USD | 0.00 USD | 370.47 USD | `-29.90%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 165,790.00 USD | 0.00 USD | 210.65 USD | `-29.54%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 165,580.00 USD | 0.00 USD | 548.03 USD | `-28.46%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 165,040.00 USD | 0.00 USD | 293.13 USD | `-28.10%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 164,740.00 USD | 0.00 USD | 420.39 USD | `-27.39%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 164,320.00 USD | 0.00 USD | 191.53 USD | `-26.31%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 164,130.00 USD | 0.00 USD | 41,790.00 USD | `-25.95%` | `202,387,000,000.00` |
| `Live` | `Long` | `210.50` | 122,340.00 USD | 0.00 USD | 108.83 USD | `-24.52%` | `517,000,000.00` |
| `Live` | `Long` | `211.50` | 122,230.00 USD | 0.00 USD | 634.50 USD | `-24.16%` | `3,000,000,000.00` |
| `Live` | `Long` | `213.50` | 121,590.00 USD | 0.00 USD | 3,800.00 USD | `-23.44%` | `17,817,000,000.00` |
| `Live` | `Long` | `215.50` | 117,790.00 USD | 0.00 USD | 239.85 USD | `-22.72%` | `1,113,000,000.00` |
| `Live` | `Long` | `222.50` | 117,550.00 USD | 0.00 USD | 7,010.00 USD | `-20.21%` | `31,500,000,000.00` |
| `Live` | `Long` | `223.50` | 110,540.00 USD | 0.00 USD | 31,290.00 USD | `-19.86%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 79,250.00 USD | 0.00 USD | 5,830.00 USD | `-19.50%` | `25,951,000,000.00` |
| `Live` | `Long` | `226.50` | 73,430.00 USD | 0.00 USD | 1,240.00 USD | `-18.78%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 72,190.00 USD | 0.00 USD | 174.49 USD | `-18.42%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 72,020.00 USD | 0.00 USD | 642.77 USD | `-18.06%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 71,370.00 USD | 0.00 USD | 114.75 USD | `-17.70%` | `500,000,000.00` |
| `Live` | `Long` | `230.50` | 71,260.00 USD | 0.00 USD | 1,190.00 USD | `-17.34%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 70,070.00 USD | 0.00 USD | 295.86 USD | `-16.99%` | `1,278,000,000.00` |
| `Live` | `Long` | `234.50` | 69,770.00 USD | 0.00 USD | 637.61 USD | `-15.91%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 69,130.00 USD | 0.00 USD | 23,750.00 USD | `-14.83%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 45,380.00 USD | 0.00 USD | 10,840.00 USD | `-14.48%` | `45,467,000,000.00` |
| `Live` | `Long` | `239.50` | 34,540.00 USD | 0.00 USD | 1,030.00 USD | `-14.12%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 33,510.00 USD | 0.00 USD | 251.88 USD | `-13.40%` | `1,043,000,000.00` |
| `Live` | `Long` | `243.50` | 33,260.00 USD | 0.00 USD | 3,380.00 USD | `-12.68%` | `13,865,000,000.00` |
| `Live` | `Long` | `244.50` | 29,890.00 USD | 0.00 USD | 4,220.00 USD | `-12.32%` | `17,277,000,000.00` |
| `Live` | `Long` | `245.50` | 25,660.00 USD | 0.00 USD | 1,030.00 USD | `-11.97%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,630.00 USD | 0.00 USD | 106.67 USD | `-11.25%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,530.00 USD | 0.00 USD | 595.16 USD | `-10.89%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 23,930.00 USD | 0.00 USD | 1,330.00 USD | `-10.17%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,610.00 USD | 0.00 USD | 268.35 USD | `-9.81%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 22,340.00 USD | 0.00 USD | 1,030.00 USD | `-9.46%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 21,310.00 USD | 0.00 USD | 548.45 USD | `-8.74%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 20,760.00 USD | 0.00 USD | 3,210.00 USD | `-8.02%` | `12,514,000,000.00` |
| `Live` | `Long` | `258.50` | 17,550.00 USD | 0.00 USD | 645.99 USD | `-7.30%` | `2,499,000,000.00` |
| `Live` | `Long` | `260.50` | 16,900.00 USD | 0.00 USD | 3,340.00 USD | `-6.59%` | `12,839,000,000.00` |
| `Live` | `Long` | `263.50` | 13,560.00 USD | 0.00 USD | 464.81 USD | `-5.51%` | `1,764,000,000.00` |
| `Live` | `Long` | `270.50` | 13,090.00 USD | 0.00 USD | 13,090.00 USD | `-3.00%` | `48,404,000,000.00` |
| `Live` | `Short` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | `+3.09%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 1,070.00 USD | 954.95 USD | 0.00 USD | `+4.53%` | `3,276,000,000.00` |
| `Live` | `Short` | `292.50` | 7,110.00 USD | 6,050.00 USD | 0.00 USD | `+4.89%` | `20,668,000,000.00` |
| `Live` | `Short` | `302.50` | 10,760.00 USD | 3,640.00 USD | 0.00 USD | `+8.47%` | `12,043,000,000.00` |
| `Live` | `Short` | `320.50` | 11,860.00 USD | 1,110.00 USD | 0.00 USD | `+14.93%` | `3,452,000,000.00` |
| `Live` | `Short` | `324.50` | 14,090.00 USD | 2,220.00 USD | 0.00 USD | `+16.36%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 39,610.00 USD | 25,530.00 USD | 0.00 USD | `+17.08%` | `78,189,000,000.00` |
| `Live` | `Short` | `338.50` | 40,970.00 USD | 1,350.00 USD | 0.00 USD | `+21.38%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 41,980.00 USD | 1,010.00 USD | 0.00 USD | `+28.55%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 42,420.00 USD | 445.52 USD | 0.00 USD | `+32.14%` | `1,209,000,000.00` |
| `Live` | `Short` | `373.50` | 83,510.00 USD | 41,090.00 USD | 0.00 USD | `+33.93%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 94,150.00 USD | 10,640.00 USD | 0.00 USD | `+45.77%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 140,400.00 USD | 46,250.00 USD | 0.00 USD | `+64.77%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 141,120.00 USD | 718.34 USD | 0.00 USD | `+78.76%` | `1,441,000,000.00` |
| `Live` | `Short` | `535.50` | 141,470.00 USD | 348.61 USD | 0.00 USD | `+92.02%` | `651,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 434,340.00 USD | 0.00 USD | 210.94 USD | `-48.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 434,130.00 USD | 0.00 USD | 2,070.00 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 432,060.00 USD | 0.00 USD | 489.38 USD | `-40.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 431,570.00 USD | 0.00 USD | 2,530.00 USD | `-35.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 429,040.00 USD | 0.00 USD | 490.59 USD | `-33.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 428,550.00 USD | 0.00 USD | 482.01 USD | `-29.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 428,070.00 USD | 0.00 USD | 189.07 USD | `-28.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 427,880.00 USD | 0.00 USD | 441.60 USD | `-25.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 427,440.00 USD | 0.00 USD | 299.96 USD | `-24.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 427,140.00 USD | 0.00 USD | 715.29 USD | `-24.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 426,420.00 USD | 0.00 USD | 638.36 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 425,790.00 USD | 0.00 USD | 740.85 USD | `-19.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 425,040.00 USD | 0.00 USD | 478.48 USD | `-18.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 424,570.00 USD | 0.00 USD | 389.48 USD | `-16.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 424,180.00 USD | 0.00 USD | 812.38 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 423,360.00 USD | 0.00 USD | 220.64 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 423,140.00 USD | 0.00 USD | 429.30 USD | `-14.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 422,710.00 USD | 0.00 USD | 296.50 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 422,420.00 USD | 0.00 USD | 216.45 USD | `-13.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 422,200.00 USD | 0.00 USD | 387.76 USD | `-13.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 421,810.00 USD | 0.00 USD | 18,080.00 USD | `-12.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 403,730.00 USD | 0.00 USD | 1,630.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 402,110.00 USD | 0.00 USD | 2,700.00 USD | `-11.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 399,400.00 USD | 0.00 USD | 2,940.00 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 396,460.00 USD | 0.00 USD | 4,560.00 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 391,900.00 USD | 0.00 USD | 1,850.00 USD | `-9.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 390,060.00 USD | 0.00 USD | 231.54 USD | `-9.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 389,820.00 USD | 0.00 USD | 109.26 USD | `-9.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 389,720.00 USD | 0.00 USD | 1,780.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 387,940.00 USD | 0.00 USD | 51,300.00 USD | `-8.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 336,640.00 USD | 0.00 USD | 250.81 USD | `-7.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 336,390.00 USD | 0.00 USD | 2,370.00 USD | `-6.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 334,020.00 USD | 0.00 USD | 269,800.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 64,220.00 USD | 0.00 USD | 320.15 USD | `-5.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 63,900.00 USD | 0.00 USD | 199.17 USD | `-5.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 63,700.00 USD | 0.00 USD | 2,180.00 USD | `-4.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 61,520.00 USD | 0.00 USD | 241.98 USD | `-4.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 61,280.00 USD | 0.00 USD | 219.35 USD | `-4.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 61,060.00 USD | 0.00 USD | 107.40 USD | `-3.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 60,960.00 USD | 0.00 USD | 29,530.00 USD | `-3.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 31,430.00 USD | 0.00 USD | 3,340.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 28,090.00 USD | 0.00 USD | 620.38 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 27,470.00 USD | 0.00 USD | 13,500.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 13,970.00 USD | 0.00 USD | 1,010.00 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 12,950.00 USD | 0.00 USD | 667.86 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 12,280.00 USD | 0.00 USD | 275.50 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 12,010.00 USD | 0.00 USD | 6,640.00 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 5,370.00 USD | 0.00 USD | 326.34 USD | `-0.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 5,040.00 USD | 0.00 USD | 5,040.00 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `279.50` | 21,990.00 USD | 21,990.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 23,380.00 USD | 1,390.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 26,490.00 USD | 3,100.00 USD | 0.00 USD | `+0.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 29,430.00 USD | 2,940.00 USD | 0.00 USD | `+1.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 37,470.00 USD | 8,040.00 USD | 0.00 USD | `+1.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 39,480.00 USD | 2,010.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 40,530.00 USD | 1,050.00 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 40,810.00 USD | 280.77 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 47,710.00 USD | 6,910.00 USD | 0.00 USD | `+3.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 47,970.00 USD | 261.96 USD | 0.00 USD | `+3.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 48,500.00 USD | 530.36 USD | 0.00 USD | `+3.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 48,720.00 USD | 212.36 USD | 0.00 USD | `+4.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 74,000.00 USD | 25,280.00 USD | 0.00 USD | `+4.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 74,170.00 USD | 167.89 USD | 0.00 USD | `+4.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 75,160.00 USD | 992.62 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 77,280.00 USD | 2,130.00 USD | 0.00 USD | `+5.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 82,010.00 USD | 4,730.00 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 82,120.00 USD | 110.37 USD | 0.00 USD | `+6.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 82,510.00 USD | 388.95 USD | 0.00 USD | `+7.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 82,660.00 USD | 153.94 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 93,440.00 USD | 10,780.00 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 98,550.00 USD | 5,110.00 USD | 0.00 USD | `+8.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 109,270.00 USD | 10,730.00 USD | 0.00 USD | `+9.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 111,920.00 USD | 2,650.00 USD | 0.00 USD | `+9.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 112,210.00 USD | 282.89 USD | 0.00 USD | `+10.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 126,700.00 USD | 14,500.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 127,340.00 USD | 634.04 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 128,370.00 USD | 1,030.00 USD | 0.00 USD | `+13.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 134,020.00 USD | 5,650.00 USD | 0.00 USD | `+14.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 134,550.00 USD | 534.59 USD | 0.00 USD | `+14.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 134,880.00 USD | 321.50 USD | 0.00 USD | `+15.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 201,590.00 USD | 66,720.00 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 202,680.00 USD | 1,090.00 USD | 0.00 USD | `+19.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 214,680.00 USD | 12,000.00 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 215,220.00 USD | 547.52 USD | 0.00 USD | `+22.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 215,340.00 USD | 110.91 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 215,590.00 USD | 257.45 USD | 0.00 USD | `+24.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 215,770.00 USD | 174.25 USD | 0.00 USD | `+24.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 215,920.00 USD | 151.50 USD | 0.00 USD | `+26.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 217,370.00 USD | 1,450.00 USD | 0.00 USD | `+28.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 219,150.00 USD | 1,770.00 USD | 0.00 USD | `+28.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 219,470.00 USD | 326.07 USD | 0.00 USD | `+29.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 220,300.00 USD | 826.60 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 227,740.00 USD | 7,440.00 USD | 0.00 USD | `+31.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 228,430.00 USD | 682.84 USD | 0.00 USD | `+32.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 229,530.00 USD | 1,100.00 USD | 0.00 USD | `+36.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 230,210.00 USD | 683.96 USD | 0.00 USD | `+42.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 230,410.00 USD | 199.75 USD | 0.00 USD | `+43.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 231,700.00 USD | 1,290.00 USD | 0.00 USD | `+43.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 232,740.00 USD | 1,040.00 USD | 0.00 USD | `+45.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 233,120.00 USD | 376.71 USD | 0.00 USD | `+45.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 233,270.00 USD | 158.86 USD | 0.00 USD | `+47.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 239,170.00 USD | 5,900.00 USD | 0.00 USD | `+48.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 240,250.00 USD | 1,080.00 USD | 0.00 USD | `+51.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 241,960.00 USD | 1,700.00 USD | 0.00 USD | `+52.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 243,510.00 USD | 1,550.00 USD | 0.00 USD | `+54.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 244,890.00 USD | 1,380.00 USD | 0.00 USD | `+56.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 245,510.00 USD | 621.14 USD | 0.00 USD | `+56.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 247,790.00 USD | 2,280.00 USD | 0.00 USD | `+57.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 248,010.00 USD | 222.75 USD | 0.00 USD | `+59.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 254,930.00 USD | 6,920.00 USD | 0.00 USD | `+61.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 260,850.00 USD | 5,920.00 USD | 0.00 USD | `+61.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 261,980.00 USD | 1,130.00 USD | 0.00 USD | `+65.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 269,610.00 USD | 7,630.00 USD | 0.00 USD | `+73.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 270,590.00 USD | 975.00 USD | 0.00 USD | `+74.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 271,570.00 USD | 981.00 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 272,070.00 USD | 499.50 USD | 0.00 USD | `+79.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,160,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+79.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,160,000.00 USD | 1,000.00 USD | 0.00 USD | `+79.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,160,000.00 USD | 1,040.00 USD | 0.00 USD | `+85.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,160,000.00 USD | 340.67 USD | 0.00 USD | `+87.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,160,000.00 USD | 638.86 USD | 0.00 USD | `+99.56%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `234.80` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD |
| `7D` | `235.30` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 10,140,000.00 USD | 0.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `236.30` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `236.80` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD |
| `7D` | `237.30` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD |
| `7D` | `238.30` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD |
| `7D` | `238.80` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.30` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD |
| `7D` | `240.80` | 10,010,000.00 USD | 0.00 USD | 10,010,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 9,990,000.00 USD | 0.00 USD | 9,990,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.30` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 9,900,000.00 USD | 0.00 USD | 9,900,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD |
| `7D` | `243.30` | 9,890,000.00 USD | 0.00 USD | 9,890,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 9,820,000.00 USD | 0.00 USD | 9,820,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.30` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 9,760,000.00 USD | 0.00 USD | 9,760,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD |
| `7D` | `247.30` | 9,710,000.00 USD | 0.00 USD | 9,710,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.80` | 9,670,000.00 USD | 0.00 USD | 9,670,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD |
| `7D` | `248.30` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD |
| `7D` | `248.80` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD |
| `7D` | `249.30` | 9,540,000.00 USD | 0.00 USD | 9,540,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD |
| `7D` | `249.80` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD |
| `7D` | `250.30` | 9,350,000.00 USD | 0.00 USD | 9,350,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD |
| `1D` | `250.50` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 13,910.00 USD | 7,600.00 USD | 12,280.00 USD |
| `7D` | `250.80` | 9,250,000.00 USD | 0.00 USD | 9,250,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD |
| `1D` | `250.90` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 5,220.00 USD | 23,600.00 USD | 12,730.00 USD |
| `1D` | `251.30` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 26,350.00 USD | 24,910.00 USD | 23,590.00 USD |
| `7D` | `251.30` | 9,120,000.00 USD | 0.00 USD | 9,120,000.00 USD | 45,790.00 USD | 80,030.00 USD | 21,120.00 USD |
| `1D` | `251.70` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 30,050.00 USD | 53,570.00 USD | 14,590.00 USD |
| `7D` | `251.80` | 8,970,000.00 USD | 0.00 USD | 8,970,000.00 USD | 75,330.00 USD | 76,000.00 USD | 59,360.00 USD |
| `1D` | `252.10` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 20,770.00 USD | 8,350.00 USD | 12,960.00 USD |
| `7D` | `252.30` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 69,530.00 USD | 39,900.00 USD | 17,360.00 USD |
| `1D` | `252.50` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 15,520.00 USD | 5,050.00 USD | 5,070.00 USD |
| `7D` | `252.80` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD |
| `1D` | `252.90` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 4,970.00 USD | 6,970.00 USD | 2,170.00 USD |
| `1D` | `253.30` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 12,480.00 USD | 8,710.00 USD | 14,780.00 USD |
| `7D` | `253.30` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 37,170.00 USD | 49,140.00 USD | 20,250.00 USD |
| `1D` | `253.70` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 21,830.00 USD | 15,190.00 USD | 11,050.00 USD |
| `7D` | `253.80` | 8,440,000.00 USD | 0.00 USD | 8,440,000.00 USD | 23,680.00 USD | 32,560.00 USD | 28,070.00 USD |
| `1D` | `254.10` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 1,590.00 USD | 7,170.00 USD | 5,820.00 USD |
| `7D` | `254.30` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 44,200.00 USD | 44,160.00 USD | 34,090.00 USD |
| `1D` | `254.50` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 8,310.00 USD | 10,840.00 USD | 35.81 USD |
| `7D` | `254.80` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 50,920.00 USD | 38,370.00 USD | 77,360.00 USD |
| `1D` | `254.90` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 9,050.00 USD | 10,890.00 USD | 24.94 USD |
| `1D` | `255.30` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 9,910.00 USD | 15,540.00 USD | 28,000.00 USD |
| `7D` | `255.30` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 44,970.00 USD | 12,850.00 USD | 25,560.00 USD |
| `1D` | `255.70` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 14,640.00 USD | 23,250.00 USD | 11,800.00 USD |
| `7D` | `255.80` | 7,990,000.00 USD | 0.00 USD | 7,990,000.00 USD | 12,780.00 USD | 17,200.00 USD | 31,120.00 USD |
| `1D` | `256.10` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 9,840.00 USD | 21,830.00 USD | 15,930.00 USD |
| `7D` | `256.30` | 7,930,000.00 USD | 0.00 USD | 7,930,000.00 USD | 47,040.00 USD | 10,260.00 USD | 40,910.00 USD |
| `1D` | `256.50` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 8,400.00 USD | 21,060.00 USD | 13,890.00 USD |
| `7D` | `256.80` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 32,750.00 USD | 13,750.00 USD | 64,360.00 USD |
| `1D` | `256.90` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 6,970.00 USD | 5,880.00 USD | 10,300.00 USD |
| `1D` | `257.30` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 8,020.00 USD | 1,350.00 USD | 11,770.00 USD |
| `7D` | `257.30` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD |
| `1D` | `257.70` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 2,380.00 USD | 4,680.00 USD | 4,830.00 USD |
| `7D` | `257.80` | 7,690,000.00 USD | 0.00 USD | 7,690,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD |
| `1D` | `258.10` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 19,750.00 USD | 2,310.00 USD | 43,950.00 USD |
| `7D` | `258.30` | 7,620,000.00 USD | 0.00 USD | 7,620,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD |
| `1D` | `258.50` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 20,310.00 USD | 15,260.00 USD | 23,200.00 USD |
| `7D` | `258.80` | 7,390,000.00 USD | 0.00 USD | 7,390,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD |
| `1D` | `258.90` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 6,660.00 USD | 38,640.00 USD | 31,030.00 USD |
| `1D` | `259.30` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 15,070.00 USD | 5,730.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD |
| `1D` | `259.70` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 19,170.00 USD | 34,250.00 USD | 39,300.00 USD |
| `7D` | `259.80` | 7,160,000.00 USD | 0.00 USD | 7,160,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD |
| `1D` | `260.10` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 39,390.00 USD | 8,640.00 USD | 6,870.00 USD |
| `7D` | `260.30` | 7,000,000.00 USD | 0.00 USD | 7,000,000.00 USD | 100,790.00 USD | 58,800.00 USD | 60,930.00 USD |
| `1D` | `260.50` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 19,010.00 USD | 1,900.00 USD | 27,210.00 USD |
| `7D` | `260.80` | 6,780,000.00 USD | 0.00 USD | 6,780,000.00 USD | 16,450.00 USD | 57,420.00 USD | 60,280.00 USD |
| `1D` | `260.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 8,950.00 USD | 50,950.00 USD | 13,940.00 USD |
| `1D` | `261.30` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,130.00 USD | 29,340.00 USD | 33,400.00 USD |
| `7D` | `261.30` | 6,650,000.00 USD | 0.00 USD | 6,650,000.00 USD | 7,150.00 USD | 97,800.00 USD | 52,540.00 USD |
| `1D` | `261.70` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 15,200.00 USD | 60,690.00 USD | 51,230.00 USD |
| `7D` | `261.80` | 6,490,000.00 USD | 0.00 USD | 6,490,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD |
| `1D` | `262.10` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 13,620.00 USD | 27,520.00 USD | 21,370.00 USD |
| `7D` | `262.30` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD |
| `1D` | `262.50` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 21,110.00 USD | 4,750.00 USD | 10,850.00 USD |
| `7D` | `262.80` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 74,900.00 USD | 49,160.00 USD | 32,760.00 USD |
| `1D` | `262.90` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 629.76 USD | 12,630.00 USD | 19,500.00 USD |
| `1D` | `263.30` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 9,930.00 USD | 4,350.00 USD | 61,500.00 USD |
| `7D` | `263.30` | 5,960,000.00 USD | 0.00 USD | 5,960,000.00 USD | 33,590.00 USD | 13,710.00 USD | 169.66 USD |
| `1D` | `263.70` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 41,850.00 USD | 29,980.00 USD | 41,370.00 USD |
| `7D` | `263.80` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 391,670.00 USD | 1,880.00 USD | 117,890.00 USD |
| `1D` | `264.10` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 46,180.00 USD | 15,630.00 USD | 17,270.00 USD |
| `7D` | `264.30` | 5,410,000.00 USD | 0.00 USD | 5,410,000.00 USD | 48,230.00 USD | 1,170.00 USD | 128.94 USD |
| `1D` | `264.50` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 1,200.00 USD | 19,920.00 USD | 4.35 USD |
| `7D` | `264.80` | 5,360,000.00 USD | 0.00 USD | 5,360,000.00 USD | 33,470.00 USD | 21,870.00 USD | 198.07 USD |
| `1D` | `264.90` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 33,200.00 USD | 2,170.00 USD | 53,310.00 USD |
| `1D` | `265.30` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 64,840.00 USD | 2,650.00 USD | 3.40 USD |
| `7D` | `265.30` | 5,300,000.00 USD | 0.00 USD | 5,300,000.00 USD | 256,440.00 USD | 2,330.00 USD | 34,040.00 USD |
| `1D` | `265.70` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 0.00 USD | 629.76 USD | 6.46 USD |
| `7D` | `265.80` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 69,380.00 USD | 0.00 USD | 106.95 USD |
| `1D` | `266.10` | 3,060,000.00 USD | 0.00 USD | 3,060,000.00 USD | 16,140.00 USD | 13,320.00 USD | 0.00 USD |
| `7D` | `266.30` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 216,090.00 USD | 645.20 USD | 17.82 USD |
| `1D` | `266.50` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 14,240.00 USD | 8,470.00 USD | 4,800.00 USD |
| `7D` | `266.80` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD |
| `1D` | `266.90` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 18,330.00 USD | 22,420.00 USD | 0.00 USD |
| `1D` | `267.30` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 33,460.00 USD | 68,530.00 USD | 12,550.00 USD |
| `7D` | `267.30` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD |
| `1D` | `267.70` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 10,330.00 USD | 36,260.00 USD | 28,720.00 USD |
| `7D` | `267.80` | 4,340,000.00 USD | 0.00 USD | 4,340,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,920.00 USD |
| `1D` | `268.10` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 18,930.00 USD | 28,480.00 USD | 60,070.00 USD |
| `7D` | `268.30` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 199,980.00 USD | 150,080.00 USD | 95,720.00 USD |
| `1D` | `268.50` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 12,910.00 USD | 18,920.00 USD | 67.34 USD |
| `7D` | `268.80` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 23,340.00 USD | 17,480.00 USD | 105.78 USD |
| `1D` | `268.90` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 21,330.00 USD | 11,500.00 USD | 182.87 USD |
| `1D` | `269.30` | 2,600,000.00 USD | 0.00 USD | 2,600,000.00 USD | 7,610.00 USD | 1,120.00 USD | 0.00 USD |
| `7D` | `269.30` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 0.00 USD | 3,490.00 USD | 148.23 USD |
| `1D` | `269.70` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 638.90 USD | 17,350.00 USD | 13,710.00 USD |
| `7D` | `269.80` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 0.00 USD | 1,920.00 USD | 240.42 USD |
| `1D` | `270.10` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 16,840.00 USD | 13,340.00 USD | 3,540.00 USD |
| `7D` | `270.30` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD |
| `1D` | `270.50` | 2,530,000.00 USD | 0.00 USD | 2,530,000.00 USD | 42,710.00 USD | 118.00 USD | 0.00 USD |
| `7D` | `270.80` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 33,050.00 USD | 0.00 USD | 120.25 USD |
| `1D` | `270.90` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 505.00 USD | 14,830.00 USD | 0.00 USD |
| `1D` | `271.30` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 12,710.00 USD | 1,780.00 USD | 11,730.00 USD |
| `7D` | `271.30` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.70` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 8,650.00 USD | 34,920.00 USD | 5,300.00 USD |
| `7D` | `271.80` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 61,810.00 USD | 7,250.00 USD | 40,480.00 USD |
| `1D` | `272.10` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 21,980.00 USD | 21,380.00 USD | 19,770.00 USD |
| `7D` | `272.30` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.50` | 2,330,000.00 USD | 0.00 USD | 2,330,000.00 USD | 6,060.00 USD | 38,280.00 USD | 41,840.00 USD |
| `7D` | `272.80` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 25,660.00 USD | 69,990.00 USD | 77,650.00 USD |
| `1D` | `272.90` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 59,390.00 USD | 5,420.00 USD | 71,640.00 USD |
| `1D` | `273.30` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 28,730.00 USD | 121,350.00 USD | 40,460.00 USD |
| `7D` | `273.30` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 0.00 USD | 79,710.00 USD | 240,480.00 USD |
| `1D` | `273.70` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 69,050.00 USD | 67,190.00 USD | 69,750.00 USD |
| `7D` | `273.80` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 181,410.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.10` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 155,110.00 USD | 37,550.00 USD | 12,160.00 USD |
| `7D` | `274.30` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 536,630.00 USD | 34,960.00 USD | 83,040.00 USD |
| `1D` | `274.50` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 186,780.00 USD | 21,440.00 USD | 54,030.00 USD |
| `7D` | `274.80` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `274.90` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 79,290.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.30` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD |
| `7D` | `275.30` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.70` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 35,420.00 USD | 31,580.00 USD | 53,200.00 USD |
| `7D` | `275.80` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD |
| `1D` | `276.10` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 161,250.00 USD | 3,340.00 USD | 7,090.00 USD |
| `7D` | `276.30` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 219,920.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.50` | 847,060.00 USD | 0.00 USD | 847,060.00 USD | 11,920.00 USD | 5,230.00 USD | 8,810.00 USD |
| `7D` | `276.80` | 894,760.00 USD | 0.00 USD | 894,760.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `276.90` | 821,090.00 USD | 0.00 USD | 821,090.00 USD | 37,290.00 USD | 25,410.00 USD | 23,460.00 USD |
| `1D` | `277.30` | 734,930.00 USD | 0.00 USD | 734,930.00 USD | 17,610.00 USD | 18,260.00 USD | 10,600.00 USD |
| `7D` | `277.30` | 878,660.00 USD | 0.00 USD | 878,660.00 USD | 152,190.00 USD | 77,800.00 USD | 140,900.00 USD |
| `1D` | `277.70` | 688,460.00 USD | 0.00 USD | 688,460.00 USD | 13,750.00 USD | 10,950.00 USD | 20,300.00 USD |
| `7D` | `277.80` | 507,780.00 USD | 0.00 USD | 507,780.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD |
| `1D` | `278.10` | 643,450.00 USD | 0.00 USD | 643,450.00 USD | 12,120.00 USD | 97,470.00 USD | 83,650.00 USD |
| `7D` | `278.30` | 290,190.00 USD | 0.00 USD | 290,190.00 USD | 24,750.00 USD | 37,090.00 USD | 155,310.00 USD |
| `1D` | `278.50` | 450,210.00 USD | 0.00 USD | 450,210.00 USD | 78,720.00 USD | 56,870.00 USD | 47,870.00 USD |
| `7D` | `278.80` | 73,040.00 USD | 0.00 USD | 73,040.00 USD | 51,310.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `278.90` | 266,750.00 USD | 0.00 USD | 266,750.00 USD | 19,260.00 USD | 10,830.00 USD | 0.00 USD |
| `1D` | `279.30` | 236,660.00 USD | 0.00 USD | 236,660.00 USD | 0.00 USD | 0.00 USD | 41,080.00 USD |
| `7D` | `279.30` | 2,660.00 USD | 0.00 USD | 2,660.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.70` | 195,580.00 USD | 0.00 USD | 195,580.00 USD | 0.00 USD | 0.00 USD | 24,310.00 USD |
| `1D` | `280.10` | 171,260.00 USD | 0.00 USD | 171,260.00 USD | 0.00 USD | 0.00 USD | 59,820.00 USD |
| `1D` | `280.50` | 111,440.00 USD | 0.00 USD | 111,440.00 USD | 4,150.00 USD | 38,740.00 USD | 68,550.00 USD |
| `7D` | `280.50` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `280.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `280.80` | 15,540.00 USD | 15,540.00 USD | 0.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `280.90` | 17,460.00 USD | 17,460.00 USD | 0.00 USD | 0.00 USD | 17,450.00 USD | 12.68 USD |
| `7D` | `281.30` | 112,950.00 USD | 112,950.00 USD | 0.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `7D` | `281.80` | 235,340.00 USD | 235,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.10` | 29,870.00 USD | 29,870.00 USD | 0.00 USD | 8,260.00 USD | 0.00 USD | 4,140.00 USD |
| `7D` | `282.30` | 259,560.00 USD | 259,560.00 USD | 0.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `283.30` | 31,160.00 USD | 31,160.00 USD | 0.00 USD | 1,280.00 USD | 0.00 USD | 11.41 USD |
| `7D` | `283.30` | 263,010.00 USD | 263,010.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.80` | 265,000.00 USD | 265,000.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.30` | 266,570.00 USD | 266,570.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `284.50` | 69,360.00 USD | 69,360.00 USD | 0.00 USD | 10,630.00 USD | 0.00 USD | 27,570.00 USD |
| `7D` | `284.80` | 321,960.00 USD | 321,960.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD |
| `1D` | `284.90` | 105,720.00 USD | 105,720.00 USD | 0.00 USD | 28,720.00 USD | 7,620.00 USD | 9.04 USD |
| `1D` | `285.30` | 189,530.00 USD | 189,530.00 USD | 0.00 USD | 25,820.00 USD | 16,320.00 USD | 41,680.00 USD |
| `7D` | `285.30` | 743,920.00 USD | 743,920.00 USD | 0.00 USD | 128,940.00 USD | 227,210.00 USD | 65,810.00 USD |
| `1D` | `285.70` | 238,540.00 USD | 238,540.00 USD | 0.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD |
| `7D` | `285.80` | 977,470.00 USD | 977,470.00 USD | 0.00 USD | 48,090.00 USD | 185,460.00 USD | 0.00 USD |
| `1D` | `286.10` | 289,270.00 USD | 289,270.00 USD | 0.00 USD | 26,810.00 USD | 719.80 USD | 23,210.00 USD |
| `7D` | `286.30` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD |
| `1D` | `286.50` | 324,610.00 USD | 324,610.00 USD | 0.00 USD | 3,550.00 USD | 1,650.00 USD | 30,140.00 USD |
| `7D` | `286.80` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD |
| `1D` | `286.90` | 479,460.00 USD | 479,460.00 USD | 0.00 USD | 47,440.00 USD | 26,700.00 USD | 80,710.00 USD |
| `1D` | `287.30` | 655,000.00 USD | 655,000.00 USD | 0.00 USD | 97,970.00 USD | 43,890.00 USD | 33,670.00 USD |
| `7D` | `287.30` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD |
| `1D` | `287.70` | 750,220.00 USD | 750,220.00 USD | 0.00 USD | 22,860.00 USD | 22,500.00 USD | 49,860.00 USD |
| `7D` | `287.80` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 70,340.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.10` | 832,140.00 USD | 832,140.00 USD | 0.00 USD | 21,420.00 USD | 26,660.00 USD | 33,850.00 USD |
| `7D` | `288.30` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 41,660.00 USD |
| `1D` | `288.50` | 939,680.00 USD | 939,680.00 USD | 0.00 USD | 52,260.00 USD | 26,060.00 USD | 29,220.00 USD |
| `7D` | `288.80` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 80,970.00 USD |
| `1D` | `288.90` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 44,740.00 USD | 24,620.00 USD | 17.54 USD |
| `1D` | `289.30` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 17,220.00 USD | 47,120.00 USD | 51,210.00 USD |
| `7D` | `289.30` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.70` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 52,150.00 USD | 67,790.00 USD | 92,100.00 USD |
| `7D` | `289.80` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 193,880.00 USD |
| `1D` | `290.10` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 65,110.00 USD | 51,750.00 USD | 114,510.00 USD |
| `7D` | `290.30` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 36,110.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.50` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 28,010.00 USD | 120,130.00 USD | 46,650.00 USD |
| `7D` | `290.80` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD |
| `1D` | `290.90` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 52,370.00 USD | 47,340.00 USD | 41,080.00 USD |
| `1D` | `291.30` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 27,020.00 USD | 12,070.00 USD | 24,320.00 USD |
| `7D` | `291.30` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 24,680.00 USD | 27,640.00 USD | 0.00 USD |
| `1D` | `291.70` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 9,470.00 USD | 38,560.00 USD | 22,170.00 USD |
| `7D` | `291.80` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.10` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 854.05 USD | 37,580.00 USD | 11,510.00 USD |
| `7D` | `292.30` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD |
| `1D` | `292.50` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 29,880.00 USD | 3,650.00 USD | 2,240.00 USD |
| `7D` | `292.80` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 138.60 USD |
| `1D` | `292.90` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 62,390.00 USD | 30,990.00 USD | 3,560.00 USD |
| `1D` | `293.30` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 22,320.00 USD | 18,040.00 USD | 27,370.00 USD |
| `7D` | `293.30` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 33,580.00 USD | 132,770.00 USD | 91.25 USD |
| `1D` | `293.70` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 76,520.00 USD | 47,640.00 USD | 64,930.00 USD |
| `7D` | `293.80` | 3,410,000.00 USD | 3,410,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 20,950.00 USD |
| `1D` | `294.10` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 21,360.00 USD | 23,760.00 USD | 49,210.00 USD |
| `7D` | `294.30` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 217,140.00 USD | 41,480.00 USD | 146,150.00 USD |
| `1D` | `294.50` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 96,500.00 USD | 76,930.00 USD | 85,210.00 USD |
| `7D` | `294.80` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD |
| `1D` | `294.90` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 33,360.00 USD | 16,330.00 USD | 48,700.00 USD |
| `1D` | `295.30` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 15,750.00 USD | 60,930.00 USD | 96,730.00 USD |
| `7D` | `295.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 46,330.00 USD | 82,780.00 USD | 345,510.00 USD |
| `1D` | `295.70` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 98,960.00 USD | 6,830.00 USD | 128,460.00 USD |
| `7D` | `295.80` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 165,320.00 USD | 82,100.00 USD | 197,410.00 USD |
| `1D` | `296.10` | 3,550,000.00 USD | 3,550,000.00 USD | 0.00 USD | 52,840.00 USD | 126,740.00 USD | 35,670.00 USD |
| `7D` | `296.30` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 43,710.00 USD | 167,940.00 USD | 120,880.00 USD |
| `1D` | `296.50` | 3,650,000.00 USD | 3,650,000.00 USD | 0.00 USD | 33,300.00 USD | 22,420.00 USD | 41,260.00 USD |
| `7D` | `296.80` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 133,820.00 USD | 3,570.00 USD | 201,420.00 USD |
| `1D` | `296.90` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 24,280.00 USD | 21,780.00 USD | 90,450.00 USD |
| `1D` | `297.30` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 61,380.00 USD | 1,000.00 USD | 31,540.00 USD |
| `7D` | `297.30` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 78,980.00 USD | 54,960.00 USD | 72.03 USD |
| `1D` | `297.70` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 15,700.00 USD | 11,340.00 USD | 12,070.00 USD |
| `7D` | `297.80` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 47,530.00 USD | 99,810.00 USD | 89,610.00 USD |
| `1D` | `298.10` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 51,840.00 USD | 10,000.00 USD | 41,710.00 USD |
| `7D` | `298.30` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 32,650.00 USD | 45,150.00 USD | 68,850.00 USD |
| `1D` | `298.50` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 5,730.00 USD | 1,480.00 USD | 56,410.00 USD |
| `7D` | `298.80` | 6,260,000.00 USD | 6,260,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 112.32 USD |
| `1D` | `298.90` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 28,150.00 USD | 5,580.00 USD | 94,670.00 USD |
| `1D` | `299.30` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 33,970.00 USD | 10,810.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 6,380,000.00 USD | 6,380,000.00 USD | 0.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD |
| `1D` | `299.70` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 8,250.00 USD | 10,850.00 USD | 27,680.00 USD |
| `7D` | `299.80` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD |
| `1D` | `300.10` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 19,900.00 USD | 36,560.00 USD | 64,300.00 USD |
| `7D` | `300.30` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD |
| `1D` | `300.50` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 23,270.00 USD | 1,560.00 USD | 17,190.00 USD |
| `7D` | `300.80` | 6,620,000.00 USD | 6,620,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,380.00 USD |
| `1D` | `300.90` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 269.05 USD | 1,020.00 USD | 29,460.00 USD |
| `1D` | `301.30` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 597.00 USD | 15,110.00 USD | 20,950.00 USD |
| `7D` | `301.30` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 73,320.00 USD | 58,690.00 USD | 150,430.00 USD |
| `1D` | `301.70` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 19,840.00 USD | 8,470.00 USD | 15,530.00 USD |
| `7D` | `301.80` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,370.00 USD |
| `1D` | `302.10` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 25,190.00 USD | 30,660.00 USD | 10,400.00 USD |
| `7D` | `302.30` | 7,330,000.00 USD | 7,330,000.00 USD | 0.00 USD | 1,560.00 USD | 181,550.00 USD | 35.08 USD |
| `1D` | `302.50` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 13,820.00 USD | 13,290.00 USD | 38,380.00 USD |
| `7D` | `302.80` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD |
| `1D` | `302.90` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 1,370.00 USD | 2,260.00 USD | 14,080.00 USD |
| `1D` | `303.30` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 21,200.00 USD | 2,760.00 USD | 9,360.00 USD |
| `7D` | `303.30` | 7,560,000.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 1,950.00 USD | 183.84 USD |
| `1D` | `303.70` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 391.16 USD | 1.44 USD |
| `7D` | `303.80` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD |
| `1D` | `304.10` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 21,920.00 USD | 1,990.00 USD | 40,420.00 USD |
| `7D` | `304.30` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD |
| `1D` | `304.50` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 9,670.00 USD | 2,100.00 USD | 44,520.00 USD |
| `7D` | `304.80` | 7,690,000.00 USD | 7,690,000.00 USD | 0.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD |
| `1D` | `304.90` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 9,920.00 USD | 8,470.00 USD | 2,030.00 USD |
| `1D` | `305.30` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 83.23 USD | 172.52 USD | 7.48 USD |
| `7D` | `305.30` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD |
| `1D` | `305.70` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 6,340.00 USD | 3,500.00 USD | 5,870.00 USD |
| `7D` | `305.80` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD |
| `1D` | `306.10` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 7,360.00 USD | 2,900.00 USD | 6,370.00 USD |
| `7D` | `306.30` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD |
| `1D` | `306.50` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 4,330.00 USD | 6.13 USD | 5,670.00 USD |
| `7D` | `306.80` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 94,690.00 USD | 74,510.00 USD | 70,010.00 USD |
| `1D` | `306.90` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 19,810.00 USD | 35,610.00 USD | 18,580.00 USD |
| `1D` | `307.30` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 11,250.00 USD | 40,340.00 USD | 22,610.00 USD |
| `7D` | `307.30` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 27,410.00 USD | 136,370.00 USD | 147,550.00 USD |
| `1D` | `307.70` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 27,000.00 USD | 25,340.00 USD | 4,060.00 USD |
| `7D` | `307.80` | 9,280,000.00 USD | 9,280,000.00 USD | 0.00 USD | 127,080.00 USD | 113,210.00 USD | 60,720.00 USD |
| `1D` | `308.10` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 19,170.00 USD | 7,600.00 USD | 12,900.00 USD |
| `7D` | `308.30` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 169,010.00 USD | 66,670.00 USD | 114,230.00 USD |
| `1D` | `308.50` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 7,610.00 USD | 3,610.00 USD | 1,590.00 USD |
| `7D` | `308.80` | 9,790,000.00 USD | 9,790,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD |
| `1D` | `308.90` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 7,450.00 USD | 5,920.00 USD | 3,480.00 USD |
| `1D` | `309.30` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 5,190.00 USD | 1,580.00 USD | 2,150.00 USD |
| `7D` | `309.30` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 34,260.00 USD | 36,030.00 USD | 36,580.00 USD |
| `1D` | `309.70` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 10,040.00 USD | 7,670.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,820.00 USD |
| `1D` | `310.10` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 14,750.00 USD | 3,980.00 USD | 11,040.00 USD |
| `7D` | `310.30` | 10,500,000.00 USD | 10,500,000.00 USD | 0.00 USD | 62,230.00 USD | 108,410.00 USD | 80,780.00 USD |
| `1D` | `310.50` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 112.30 USD | 5,020.00 USD | 5,800.00 USD |
| `7D` | `310.80` | 10,630,000.00 USD | 10,630,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 12,180.00 USD |
| `1D` | `310.90` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 5,080.00 USD | 73.70 USD | 13.75 USD |
| `1D` | `311.30` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 257.90 USD | 2,350.00 USD | 29.00 USD |
| `7D` | `311.30` | 10,870,000.00 USD | 10,870,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,860.00 USD |
| `1D` | `311.70` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 7,980.00 USD | 9,070.00 USD | 4,070.00 USD |
| `7D` | `311.80` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 19,570.00 USD | 11,240.00 USD | 25,560.00 USD |
| `1D` | `312.10` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 299.35 USD | 10,320.00 USD | 15,100.00 USD |
| `7D` | `312.30` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 27,420.00 USD |
| `1D` | `312.50` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 14,640.00 USD | 8,480.00 USD | 11,780.00 USD |
| `7D` | `312.80` | 11,060,000.00 USD | 11,060,000.00 USD | 0.00 USD | 21,990.00 USD | 14,880.00 USD | 19,390.00 USD |
| `1D` | `312.90` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 8,960.00 USD | 1,670.00 USD | 6,510.00 USD |
| `1D` | `313.30` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 3,580.00 USD | 18,270.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD |
| `1D` | `313.70` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 4,550.00 USD | 4,260.00 USD | 8,220.00 USD |
| `7D` | `313.80` | 11,220,000.00 USD | 11,220,000.00 USD | 0.00 USD | 33,220.00 USD | 1,570.00 USD | 44,160.00 USD |
| `1D` | `314.00` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,860.00 USD |
| `7D` | `314.30` | 11,310,000.00 USD | 11,310,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `7D` | `314.80` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `315.30` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 500.10 USD | 547.95 USD | 9.16 USD |
| `7D` | `315.80` | 11,430,000.00 USD | 11,430,000.00 USD | 0.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD |
| `7D` | `316.30` | 11,530,000.00 USD | 11,530,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD |
| `7D` | `316.80` | 11,580,000.00 USD | 11,580,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD |
| `7D` | `317.30` | 11,600,000.00 USD | 11,600,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD |
| `7D` | `317.80` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD |
| `7D` | `318.30` | 11,700,000.00 USD | 11,700,000.00 USD | 0.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `304.73M` | Total OI Tokens: `1,085,350.5 BCH`
  * 1h OI Change: `+0.37%` | 4h OI Change: `-1.04%` | 24h OI Change: `-0.17%`
  * Exchange Breakdown: Binance=`88.55M` | Bybit=`38.07M` | OKX=`23.76M` | Hyperliquid=`7.18M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.95K` | Last 24h: `24.98K` | Last 3d: `73.64K` | Last 7d: `144.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0081%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0074%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `43.33%` | `56.67%` | `0.76` | 2,240,000.00 USD |
| `15M` | `Binance` | `41.3%` | `58.7%` | `0.70` | 423,620.00 USD |
| `15M` | `OKX` | `43.02%` | `56.98%` | `0.76` | 147,520.00 USD |
| `15M` | `Bybit` | `52.55%` | `47.45%` | `1.11` | 86,710.00 USD |
| `15M` | `KuCoin` | `45.98%` | `54.02%` | `0.85` | 96,340.00 USD |
| `15M` | `Gate` | `67.65%` | `32.35%` | `2.09` | 25,720.00 USD |
| `15M` | `Bitget` | `43.4%` | `56.6%` | `0.77` | 12,700.00 USD |
| `15M` | `BingX` | `9.42%` | `90.58%` | `0.10` | 448,840.00 USD |
| `15M` | `MEXC` | `65.31%` | `34.69%` | `1.88` | 27,440.00 USD |
| `15M` | `Bitunix` | `55.24%` | `44.76%` | `1.23` | 30,030.00 USD |
| `15M` | `Hyperliquid` | `68.24%` | `31.76%` | `2.15` | 10,800.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.39%` | `48.61%` | `1.06` | 692,370.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 166,780.00 USD |
| `15M` | `HTX` | `86.2%` | `13.8%` | `6.25` | 3,420.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `17.28%` | `82.72%` | `0.21` | 71,110.00 USD |
| `15M` | `Aster` | `45.19%` | `54.81%` | `0.82` | 994.75 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `19.11%` | `80.89%` | `0.24` | 5,140.00 USD |
| `15M` | `Whale Positions` | `41.3%` | `58.7%` | `0.70` | 423,620.00 USD |
| `15M` | `Global Accounts` | `43.33%` | `56.67%` | `0.76` | 2,240,000.00 USD |
| `1H` | `BCH` | `47.22%` | `52.78%` | `0.89` | 23,250,000.00 USD |
| `1H` | `Binance` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `OKX` | `47.35%` | `52.65%` | `0.90` | 1,990,000.00 USD |
| `1H` | `Bybit` | `47.29%` | `52.71%` | `0.90` | 2,030,000.00 USD |
| `1H` | `KuCoin` | `59.08%` | `40.92%` | `1.44` | 372,410.00 USD |
| `1H` | `Gate` | `54.44%` | `45.56%` | `1.19` | 847,720.00 USD |
| `1H` | `Bitget` | `43.77%` | `56.23%` | `0.78` | 935,490.00 USD |
| `1H` | `BingX` | `11.83%` | `88.17%` | `0.13` | 2,440,000.00 USD |
| `1H` | `MEXC` | `49.56%` | `50.44%` | `0.98` | 3,490,000.00 USD |
| `1H` | `Bitunix` | `53.54%` | `46.46%` | `1.15` | 917,180.00 USD |
| `1H` | `Hyperliquid` | `43.53%` | `56.47%` | `0.77` | 271,920.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.43%` | `51.57%` | `0.94` | 266,530.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `99.89%` | `0.11%` | `908.09` | 929,840.00 USD |
| `1H` | `HTX` | `47.4%` | `52.6%` | `0.90` | 47,650.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `44.34%` | `55.66%` | `0.80` | 159,240.00 USD |
| `1H` | `Aster` | `48.1%` | `51.9%` | `0.93` | 25,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.17%` | `63.83%` | `0.57` | 6,640.00 USD |
| `1H` | `Whale Positions` | `49.17%` | `50.83%` | `0.97` | 8,540,000.00 USD |
| `1H` | `Global Accounts` | `47.22%` | `52.78%` | `0.89` | 23,250,000.00 USD |
| `4H` | `BCH` | `49.46%` | `50.54%` | `0.98` | 432,690,000.00 USD |
| `4H` | `Binance` | `51.88%` | `48.12%` | `1.08` | 191,400,000.00 USD |
| `4H` | `OKX` | `46.88%` | `53.12%` | `0.88` | 50,920,000.00 USD |
| `4H` | `Bybit` | `48.71%` | `51.29%` | `0.95` | 55,050,000.00 USD |
| `4H` | `KuCoin` | `55.95%` | `44.05%` | `1.27` | 5,250,000.00 USD |
| `4H` | `Gate` | `52.61%` | `47.39%` | `1.11` | 11,340,000.00 USD |
| `4H` | `Bitget` | `51.16%` | `48.84%` | `1.05` | 26,930,000.00 USD |
| `4H` | `BingX` | `38.47%` | `61.53%` | `0.63` | 15,280,000.00 USD |
| `4H` | `MEXC` | `45.58%` | `54.42%` | `0.84` | 16,280,000.00 USD |
| `4H` | `Bitunix` | `47.05%` | `52.95%` | `0.89` | 8,800,000.00 USD |
| `4H` | `Hyperliquid` | `45.86%` | `54.14%` | `0.85` | 32,370,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.7%` | `51.3%` | `0.95` | 1,930,000.00 USD |
| `4H` | `Crypto.com` | `59.46%` | `40.54%` | `1.47` | 72,320.00 USD |
| `4H` | `WhiteBIT` | `46.91%` | `53.09%` | `0.88` | 11,880,000.00 USD |
| `4H` | `HTX` | `53.84%` | `46.16%` | `1.17` | 544,660.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.49%` | `48.51%` | `1.06` | 650,970.00 USD |
| `4H` | `Aster` | `48.56%` | `51.44%` | `0.94` | 1,420,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `46.59%` | `53.41%` | `0.87` | 2,560,000.00 USD |
| `4H` | `Whale Positions` | `51.88%` | `48.12%` | `1.08` | 191,400,000.00 USD |
| `4H` | `Global Accounts` | `49.46%` | `50.54%` | `0.98` | 432,690,000.00 USD |


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
| `5:00 UTC` | `278.88` | `279.52` | `278.88` | `280.56` | `278.74` | 1,483,095.28 USD | 812,226.33 USD | 670,868.95 USD | 141,357.38 USD | `+9.53%` | `26B / 53S` |

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
| `5m` | 9,940.00 USD | 272,860.00 USD | **`ACCUMULATION`** |
| `15m` | -100,660.00 USD | 424,990.00 USD | **`ACCUMULATION`** |
| `30m` | -191,390.00 USD | -152,840.00 USD | **`DISTRIBUTION`** |
| `1h` | -92,110.00 USD | 463,780.00 USD | **`ACCUMULATION`** |
| `2h` | 98,960.00 USD | -13,860.00 USD | **`ACCUMULATION`** |
| `4h` | 144,860.00 USD | 342,040.00 USD | **`ACCUMULATION`** |
| `6h` | 808,570.00 USD | 63,320.00 USD | **`ACCUMULATION`** |
| `8h` | 1,180,000.00 USD | 1,490,000.00 USD | **`ACCUMULATION`** |
| `12h` | 901,350.00 USD | -40,390.00 USD | **`ACCUMULATION`** |
| `24h` | 156,130.00 USD | -2,210,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -665,960.00 USD | -13,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,070,000.00 USD | -136,890,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+9.94K` | 15m=`-100.66K` | 1h=`-92.11K` | 24h=`+156.13K`
* Futures Capital Netflows: 5m=`+272.86K` | 15m=`+424.99K` | 1h=`+463.78K` | 24h=`-2.21M`
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
  * `2026-10-30 14:09:50 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:50:50 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:31:50 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:27:50 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:26:50 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `268.01` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `264.63` (Risk Distance: `3.38` pts)
  * +2.5R Take Profit: `276.45`
  * Mathematical Lot Sizing: **`2.96 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `281.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `284.82` (Risk Distance: `3.38` pts)
  * +2.5R Take Profit: `273.00`
  * Mathematical Lot Sizing: **`2.96 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`280.88`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
