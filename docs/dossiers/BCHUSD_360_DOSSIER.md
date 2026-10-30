# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 11:32:22 IST` (`2026-10-30 06:02:22 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `284.26` | **Live Ask Quote**: `284.84` | **Mid Price**: `284.55`
- **Spread Points**: `580.00` | **Spread BPS**: `20.38 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `274.88` | VWAP Z-Score: `+1.50` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.72` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `62.99` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `293.43` | Lower -3.00σ Band: `256.33`
  * Upper +2.51σ Band: `290.40` | Lower -2.51σ Band: `259.36`
  * Upper +2.01σ Band: `287.31` | Lower -2.01σ Band: `262.45`
  * Upper +2.00σ Band: `287.25` | Lower -2.00σ Band: `262.51`
  * Upper +1.28σ Band: `282.80` | Lower -1.28σ Band: `266.97`
  * Upper +1.00σ Band: `281.07` | Lower -1.00σ Band: `268.70`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`282.58` | EMA-20=`280.11` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`279.22` (Slope: `+0.0000`) | EMA-100=`280.53`
  * Institutional Anchors: EMA-144=`281.54` | EMA-200=`283.02` (Slope: `-0.0474`) | EMA-233=`284.11`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `278.75` (Distance: `+2.08%`)
  * Point of Control (POC) = `276.23` (Distance: `+3.01%`)
  * Value Area Low (VAL) = `268.48` (Distance: `+5.98%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.60` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.86` | Low=`282.66`
  * New York Session (13:00-21:00 UTC): High=`286.26` | Low=`282.84`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `283.41` - `285.69`
  * Optimal Trade Entry (OTE 0.705): `285.12`
  * Structural Invalidation Anchor (0.786): `286.83`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.96` | `285.59` | `284.68` | `284.86` | `681` | 194,140.61 USD | 3,860.67 USD | `+1.99%` | -2,293,161.18 USD | `+0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `284.85` | `285.59` | `284.75` | `284.99` | `393` | 112,094.12 USD | -12,209.81 USD | `-10.89%` | -2,305,370.99 USD | `-0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `284.98` | `284.99` | `284.53` | `284.53` | `349` | 99,274.44 USD | -20,649.33 USD | `-20.80%` | -2,326,020.32 USD | `-0.38` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `283.51` | `285.59` | `283.46` | `283.92` | `3,278` | 932,067.73 USD | 167,554.77 USD | `+17.98%` | -2,343,314.31 USD | `+0.27` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `283.93` | `285.15` | `283.91` | `284.97` | `1,528` | 434,490.61 USD | 46,292.46 USD | `+10.65%` | -2,297,021.85 USD | `-0.04` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `284.96` | `285.59` | `284.43` | `284.49` | `1,438` | 409,760.72 USD | -31,392.32 USD | `-7.66%` | -2,328,414.17 USD | `-0.14` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `276.08` | `284.75` | `276.00` | `283.99` | `21,838` | 6,138,674.85 USD | -75,926.04 USD | `-1.24%` | -2,486,653.51 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `283.99` | `287.12` | `282.33` | `283.51` | `23,256` | 6,620,902.65 USD | -28,395.05 USD | `-0.43%` | -2,515,048.57 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `283.51` | `285.59` | `283.46` | `284.49` | `6,243` | 1,776,319.05 USD | 182,454.91 USD | `+10.27%` | -2,332,593.65 USD | `+0.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.49` | `29,499` | 8,397,221.70 USD | 154,059.86 USD | `+1.83%` | -1,720,323.14 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `279.38` | `288.24` | `277.49` | `287.96` | `74,069` | 20,847,128.37 USD | 1,744,736.30 USD | `+8.37%` | 1,085,885.17 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | -386,016.76 USD | `-0.98` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -2,164,561.37 USD | `-0.90` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,874,383.00 USD | `+0.52` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `282.33` | `284.99` | `30,757` | 8,755,982.56 USD | 134,729.75 USD | `+1.54%` | -1,739,653.25 USD | `+0.36` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`284.55`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1947` | `0x12d2...f97f` | `LONG` | 1,031,769.27 USD | `3,627,243,000,000.00` | `303.26` | `284.38` | `0.000000` | -68,230.07 USD | `-6.61%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
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
| `7D` | `Long Liquidation` | `234.80` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.30` | 10,120,000.00 USD | 10,120,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `235.80` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.30` | 10,100,000.00 USD | 10,100,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `236.80` | 10,090,000.00 USD | 10,090,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `237.30` | 10,060,000.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `237.50` | 30,780.00 USD | 53,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `237.80` | 10,050,000.00 USD | 10,050,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.30` | 10,050,000.00 USD | 10,050,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `238.80` | 10,030,000.00 USD | 10,030,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `239.30` | 10,000,000.00 USD | 10,000,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `239.50` | 1,030.00 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `239.80` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.30` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 9,980,000.00 USD | 9,980,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.30` | 9,980,000.00 USD | 9,980,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 21,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.80` | 9,970,000.00 USD | 9,970,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.30` | 9,950,000.00 USD | 9,950,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 1,520.00 USD | 21,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 9,870,000.00 USD | 9,870,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.30` | 9,860,000.00 USD | 9,860,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 19,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.80` | 9,850,000.00 USD | 9,850,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 4,220.00 USD | 18,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 9,800,000.00 USD | 9,800,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.30` | 9,770,000.00 USD | 9,770,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.80` | 9,740,000.00 USD | 9,740,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.30` | 9,730,000.00 USD | 9,730,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 9,690,000.00 USD | 9,690,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.30` | 9,680,000.00 USD | 9,680,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 12,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.80` | 9,640,000.00 USD | 9,640,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.30` | 9,630,000.00 USD | 9,630,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 12,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,620,000.00 USD | 9,620,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.30` | 9,510,000.00 USD | 9,510,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,590.00 USD | 12,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `249.80` | 9,430,000.00 USD | 9,430,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.30` | 9,320,000.00 USD | 9,320,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 10,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,220,000.00 USD | 9,220,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.30` | 9,090,000.00 USD | 9,090,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 9,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `251.80` | 8,940,000.00 USD | 8,940,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.30` | 8,760,000.00 USD | 8,760,000.00 USD | 69,530.00 USD | 32,580.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,170.00 USD | 8,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,640,000.00 USD | 8,640,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.30` | 8,560,000.00 USD | 8,560,000.00 USD | 37,170.00 USD | 49,360.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.80` | 8,450,000.00 USD | 8,450,000.00 USD | 10,460.00 USD | 32,560.00 USD | 28,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 4,430,000.00 USD | 4,430,000.00 USD | 7,950.00 USD | 17,690.00 USD | 15,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.30` | 8,380,000.00 USD | 8,380,000.00 USD | 44,200.00 USD | 44,160.00 USD | 25,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 4,390,000.00 USD | 4,390,000.00 USD | 8,310.00 USD | 12,740.00 USD | 2.31 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 7,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 4,360,000.00 USD | 4,360,000.00 USD | 2,210.00 USD | 991.04 USD | 17.15 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,260,000.00 USD | 8,260,000.00 USD | 51,240.00 USD | 38,370.00 USD | 77,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 4,360,000.00 USD | 4,360,000.00 USD | 15,800.00 USD | 9,440.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.30` | 8,100,000.00 USD | 8,100,000.00 USD | 44,970.00 USD | 12,850.00 USD | 31,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.60` | 4,320,000.00 USD | 4,320,000.00 USD | 14,430.00 USD | 25,340.00 USD | 12,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.80` | 8,010,000.00 USD | 8,010,000.00 USD | 12,780.00 USD | 16,980.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 4,270,000.00 USD | 4,270,000.00 USD | 6,630.00 USD | 9,130.00 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.30` | 7,950,000.00 USD | 7,950,000.00 USD | 81,660.00 USD | 24,260.00 USD | 48,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 4,240,000.00 USD | 4,240,000.00 USD | 7,420.00 USD | 29,480.00 USD | 18,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 4,490.00 USD | 7,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 4,190,000.00 USD | 4,190,000.00 USD | 791.61 USD | 5,950.00 USD | 14,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 7,800,000.00 USD | 7,800,000.00 USD | 32,750.00 USD | 21,210.00 USD | 64,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 4,160,000.00 USD | 4,160,000.00 USD | 14,160.00 USD | 1,040.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.30` | 7,680,000.00 USD | 7,680,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `257.50` | 467.62 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `257.60` | 4,140,000.00 USD | 4,140,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.80` | 7,650,000.00 USD | 7,650,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 4,120,000.00 USD | 4,120,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.30` | 7,580,000.00 USD | 7,580,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 4,060,000.00 USD | 4,060,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 176.56 USD | 2,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 4,010,000.00 USD | 4,010,000.00 USD | 8,320.00 USD | 30,410.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,350,000.00 USD | 7,350,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 3,930,000.00 USD | 3,930,000.00 USD | 14,560.00 USD | 13,000.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.30` | 7,180,000.00 USD | 7,180,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 3,890,000.00 USD | 3,890,000.00 USD | 13,640.00 USD | 4,640.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.80` | 7,120,000.00 USD | 7,120,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 3,850,000.00 USD | 3,850,000.00 USD | 45,250.00 USD | 32,940.00 USD | 23,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.30` | 6,960,000.00 USD | 6,960,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 3,740,000.00 USD | 3,740,000.00 USD | 19,630.00 USD | 6,890.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 3,700,000.00 USD | 3,700,000.00 USD | 1,450.00 USD | 46,360.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 6,740,000.00 USD | 6,740,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 3,630,000.00 USD | 3,630,000.00 USD | 8,240.00 USD | 22,970.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.30` | 6,610,000.00 USD | 6,610,000.00 USD | 7,150.00 USD | 97,320.00 USD | 52,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 3,570,000.00 USD | 3,570,000.00 USD | 18,640.00 USD | 55,030.00 USD | 53,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.80` | 6,450,000.00 USD | 6,450,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 3,440,000.00 USD | 3,440,000.00 USD | 17,810.00 USD | 43,870.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.30` | 6,260,000.00 USD | 6,260,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 3,360,000.00 USD | 3,360,000.00 USD | 20,850.00 USD | 4,110.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.80` | 3,320,000.00 USD | 3,320,000.00 USD | 366.04 USD | 13,020.00 USD | 19,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,080,000.00 USD | 6,080,000.00 USD | 74,900.00 USD | 49,480.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 3,290,000.00 USD | 3,290,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.30` | 5,930,000.00 USD | 5,930,000.00 USD | 33,590.00 USD | 13,230.00 USD | 101.93 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 3,210,000.00 USD | 3,210,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.80` | 5,880,000.00 USD | 5,880,000.00 USD | 391,670.00 USD | 1,380.00 USD | 117,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 3,110,000.00 USD | 3,110,000.00 USD | 52,440.00 USD | 15,290.00 USD | 17,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.30` | 5,370,000.00 USD | 5,370,000.00 USD | 48,690.00 USD | 0.00 USD | 133.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 3,030,000.00 USD | 3,030,000.00 USD | 6,250.00 USD | 19,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.80` | 3,000,000.00 USD | 3,000,000.00 USD | 22,350.00 USD | 773.98 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,320,000.00 USD | 5,320,000.00 USD | 33,940.00 USD | 21,410.00 USD | 198.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 2,960,000.00 USD | 2,960,000.00 USD | 75,770.00 USD | 1,510.00 USD | 33,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.30` | 5,260,000.00 USD | 5,260,000.00 USD | 256,440.00 USD | 0.00 USD | 33,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.60` | 2,850,000.00 USD | 2,850,000.00 USD | 167.69 USD | 228.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.80` | 4,970,000.00 USD | 4,970,000.00 USD | 69,380.00 USD | 0.00 USD | 109.91 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 2,850,000.00 USD | 2,850,000.00 USD | 12,120.00 USD | 63.94 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.30` | 4,900,000.00 USD | 4,900,000.00 USD | 216,090.00 USD | 0.00 USD | 17.82 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 2,830,000.00 USD | 2,830,000.00 USD | 8,650.00 USD | 13,250.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.80` | 2,810,000.00 USD | 2,810,000.00 USD | 36,150.00 USD | 30,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 4,690,000.00 USD | 4,690,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 2,740,000.00 USD | 2,740,000.00 USD | 43,080.00 USD | 32,200.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.30` | 4,490,000.00 USD | 4,490,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.60` | 2,650,000.00 USD | 2,650,000.00 USD | 4,660.00 USD | 72,250.00 USD | 14,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.80` | 4,300,000.00 USD | 4,300,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 2,560,000.00 USD | 2,560,000.00 USD | 4,570.00 USD | 0.00 USD | 49,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.30` | 4,010,000.00 USD | 4,010,000.00 USD | 169,940.00 USD | 148,780.00 USD | 62,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 35,070.00 USD | 13,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.80` | 2,460,000.00 USD | 2,460,000.00 USD | 8,400.00 USD | 321.80 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,630,000.00 USD | 3,630,000.00 USD | 23,340.00 USD | 0.00 USD | 55.96 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 2,450,000.00 USD | 2,450,000.00 USD | 178.30 USD | 703.50 USD | 20.82 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.30` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 1,930.00 USD | 148.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.60` | 2,450,000.00 USD | 2,450,000.00 USD | 378.60 USD | 16,500.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.80` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 240.42 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 2,420,000.00 USD | 2,420,000.00 USD | 450.60 USD | 793.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.30` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 2,420,000.00 USD | 2,420,000.00 USD | 9,980.00 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.80` | 2,400,000.00 USD | 2,400,000.00 USD | 323.80 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 120.25 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 2,390,000.00 USD | 2,390,000.00 USD | 12,890.00 USD | 478.10 USD | 2,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.60` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.80` | 3,610,000.00 USD | 3,610,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 2,370,000.00 USD | 2,370,000.00 USD | 15,100.00 USD | 41,690.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.30` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 2,310,000.00 USD | 2,310,000.00 USD | 6,060.00 USD | 10,340.00 USD | 38,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.80` | 2,250,000.00 USD | 2,250,000.00 USD | 50,370.00 USD | 5,990.00 USD | 58,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,470,000.00 USD | 3,470,000.00 USD | 25,660.00 USD | 69,990.00 USD | 47,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 2,140,000.00 USD | 2,140,000.00 USD | 14,040.00 USD | 104,070.00 USD | 16,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.30` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 70,180.00 USD | 240,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 2,000,000.00 USD | 2,000,000.00 USD | 11,610.00 USD | 10,810.00 USD | 42,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.80` | 3,020,000.00 USD | 3,020,000.00 USD | 181,410.00 USD | 0.00 USD | 29,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.00` | 1,940,000.00 USD | 1,940,000.00 USD | 164,540.00 USD | 80,800.00 USD | 39,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.30` | 2,810,000.00 USD | 2,810,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 1,650,000.00 USD | 1,650,000.00 USD | 239,320.00 USD | 0.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.80` | 1,370,000.00 USD | 1,370,000.00 USD | 89,480.00 USD | 19,960.00 USD | 12,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 2,250,000.00 USD | 2,250,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.30` | 1,720,000.00 USD | 1,720,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.60` | 1,250,000.00 USD | 1,250,000.00 USD | 20,900.00 USD | 10,450.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.80` | 1,640,000.00 USD | 1,640,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.00` | 1,190,000.00 USD | 1,190,000.00 USD | 83,200.00 USD | 0.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.30` | 1,530,000.00 USD | 1,530,000.00 USD | 153,820.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.40` | 1,070,000.00 USD | 1,070,000.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.80` | 1,050,000.00 USD | 1,050,000.00 USD | 11,880.00 USD | 13,540.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 1,270,000.00 USD | 1,270,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.20` | 1,020,000.00 USD | 1,020,000.00 USD | 25,720.00 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.30` | 1,260,000.00 USD | 1,260,000.00 USD | 152,190.00 USD | 63,290.00 USD | 99,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.80` | 943,170.00 USD | 943,170.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.00` | 985,900.00 USD | 985,900.00 USD | 12,120.00 USD | 21,820.00 USD | 76,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.30` | 725,580.00 USD | 725,580.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.40` | 875,440.00 USD | 875,440.00 USD | 42,620.00 USD | 88,620.00 USD | 45,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.80` | 699,090.00 USD | 699,090.00 USD | 38,650.00 USD | 21,300.00 USD | 34,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 568,300.00 USD | 568,300.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.20` | 604,700.00 USD | 604,700.00 USD | 6,300.00 USD | 64,260.00 USD | 17,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.30` | 516,060.00 USD | 516,060.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.60` | 516,200.00 USD | 516,200.00 USD | 14,720.00 USD | 21,310.00 USD | 47,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.80` | 513,390.00 USD | 513,390.00 USD | 0.00 USD | 1,770.00 USD | 58,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.00` | 432,720.00 USD | 432,720.00 USD | 5,130.00 USD | 14,930.00 USD | 31,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.30` | 453,590.00 USD | 453,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.40` | 381,310.00 USD | 381,310.00 USD | 14,910.00 USD | 60,750.00 USD | 97,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.80` | 208,600.00 USD | 208,600.00 USD | 28,040.00 USD | 23,190.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 436,230.00 USD | 436,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `281.20` | 157,360.00 USD | 157,360.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.30` | 420,690.00 USD | 420,690.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.80` | 323,280.00 USD | 323,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.00` | 137,680.00 USD | 137,680.00 USD | 2,050.00 USD | 21,390.00 USD | 4,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.30` | 125,860.00 USD | 125,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.40` | 110,090.00 USD | 110,090.00 USD | 8,260.00 USD | 12,740.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.80` | 89,090.00 USD | 89,090.00 USD | 0.00 USD | 52,180.00 USD | 19.90 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.20` | 36,890.00 USD | 36,890.00 USD | 16,210.00 USD | 20,630.00 USD | 47.36 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.30` | 101,640.00 USD | 101,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 2,000.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `283.80` | 3,990.00 USD | 3,990.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.30` | 180,540.00 USD | 180,540.00 USD | 1,560.00 USD | 174,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.40` | 397.40 USD | 397.40 USD | 0.00 USD | 397.40 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.80` | 1,350.00 USD | 1,350.00 USD | 0.00 USD | 948.40 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 490,550.00 USD | 490,550.00 USD | 0.00 USD | 310,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.20` | 129,300.00 USD | 129,300.00 USD | 86,260.00 USD | 0.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.30` | 786,620.00 USD | 786,620.00 USD | 68,860.00 USD | 227,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.60` | 131,010.00 USD | 131,010.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.80` | 985,210.00 USD | 985,210.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.00` | 162,240.00 USD | 162,240.00 USD | 7,580.00 USD | 434.90 USD | 23,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.30` | 1,030,000.00 USD | 1,030,000.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.40` | 168,710.00 USD | 168,710.00 USD | 5,620.00 USD | 851.39 USD | 4.24 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.80` | 255,560.00 USD | 255,560.00 USD | 3,590.00 USD | 5,130.00 USD | 78,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,280,000.00 USD | 1,280,000.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.20` | 381,190.00 USD | 381,190.00 USD | 51,540.00 USD | 34,260.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.30` | 1,480,000.00 USD | 1,480,000.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 112.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.60` | 476,060.00 USD | 476,060.00 USD | 13,180.00 USD | 24,900.00 USD | 56,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.80` | 1,810,000.00 USD | 1,810,000.00 USD | 4,240.00 USD | 272,200.00 USD | 53,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.00` | 544,350.00 USD | 544,350.00 USD | 9,440.00 USD | 14,610.00 USD | 44,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.30` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 35,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.40` | 651,530.00 USD | 651,530.00 USD | 68,380.00 USD | 18,330.00 USD | 20,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.80` | 682,770.00 USD | 682,770.00 USD | 17,070.00 USD | 14,160.00 USD | 11.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 2,050,000.00 USD | 2,050,000.00 USD | 124,780.00 USD | 1,140.00 USD | 80,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 729,630.00 USD | 729,630.00 USD | 1,720.00 USD | 14,960.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.60` | 870,720.00 USD | 870,720.00 USD | 20,690.00 USD | 37,460.00 USD | 82,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.80` | 2,400,000.00 USD | 2,400,000.00 USD | 51,310.00 USD | 101,040.00 USD | 134,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.00` | 1,090,000.00 USD | 1,090,000.00 USD | 86,650.00 USD | 47,310.00 USD | 84,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.30` | 2,430,000.00 USD | 2,430,000.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.40` | 1,210,000.00 USD | 1,210,000.00 USD | 10,530.00 USD | 80,370.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.80` | 1,360,000.00 USD | 1,360,000.00 USD | 33,300.00 USD | 63,390.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,490,000.00 USD | 2,490,000.00 USD | 898.13 USD | 1,760.00 USD | 58,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 1,420,000.00 USD | 1,420,000.00 USD | 15,390.00 USD | 11,280.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.30` | 2,530,000.00 USD | 2,530,000.00 USD | 24,680.00 USD | 10,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 1,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.60` | 1,460,000.00 USD | 1,460,000.00 USD | 1,740.00 USD | 20,290.00 USD | 22,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.80` | 2,730,000.00 USD | 2,730,000.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 1,510,000.00 USD | 1,510,000.00 USD | 1,150.00 USD | 45,050.00 USD | 34.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.30` | 2,800,000.00 USD | 2,800,000.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 1,550,000.00 USD | 1,550,000.00 USD | 22,300.00 USD | 12,110.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.80` | 1,590,000.00 USD | 1,590,000.00 USD | 12,680.00 USD | 21,060.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,900,000.00 USD | 2,900,000.00 USD | 887.27 USD | 100,630.00 USD | 138.60 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 1,650,000.00 USD | 1,650,000.00 USD | 20,320.00 USD | 14,450.00 USD | 27,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.30` | 3,040,000.00 USD | 3,040,000.00 USD | 534.50 USD | 132,080.00 USD | 36.33 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 1,790,000.00 USD | 1,790,000.00 USD | 77,480.00 USD | 41,450.00 USD | 16,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.80` | 3,080,000.00 USD | 3,080,000.00 USD | 38,790.00 USD | 1,860.00 USD | 126.44 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 1,900,000.00 USD | 1,900,000.00 USD | 30,820.00 USD | 20,050.00 USD | 60,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.30` | 3,470,000.00 USD | 3,470,000.00 USD | 217,140.00 USD | 33,590.00 USD | 146,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 2,120,000.00 USD | 2,120,000.00 USD | 50,740.00 USD | 55,140.00 USD | 113,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 2,240,000.00 USD | 2,240,000.00 USD | 57,560.00 USD | 16,260.00 USD | 44,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,740,000.00 USD | 3,740,000.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 2,340,000.00 USD | 2,340,000.00 USD | 6,060.00 USD | 11,650.00 USD | 80,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.30` | 4,210,000.00 USD | 4,210,000.00 USD | 46,330.00 USD | 83,210.00 USD | 345,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.60` | 2,560,000.00 USD | 2,560,000.00 USD | 61,310.00 USD | 38,860.00 USD | 122,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.80` | 4,620,000.00 USD | 4,620,000.00 USD | 165,320.00 USD | 72,570.00 USD | 167,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 2,740,000.00 USD | 2,740,000.00 USD | 48,420.00 USD | 100,760.00 USD | 32,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.30` | 4,950,000.00 USD | 4,950,000.00 USD | 43,710.00 USD | 167,290.00 USD | 120,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 2,880,000.00 USD | 2,880,000.00 USD | 77,530.00 USD | 31,150.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `296.50` | 6,130.00 USD | 7,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `296.80` | 3,010,000.00 USD | 3,010,000.00 USD | 24,600.00 USD | 31,800.00 USD | 74,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,290,000.00 USD | 5,290,000.00 USD | 133,820.00 USD | 2,910.00 USD | 201,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 3,110,000.00 USD | 3,110,000.00 USD | 56,360.00 USD | 1,060.00 USD | 50,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.30` | 5,420,000.00 USD | 5,420,000.00 USD | 78,980.00 USD | 53,400.00 USD | 72.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 3,160,000.00 USD | 3,160,000.00 USD | 7,710.00 USD | 10,830.00 USD | 29,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.80` | 5,660,000.00 USD | 5,660,000.00 USD | 47,530.00 USD | 99,320.00 USD | 89,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 3,280,000.00 USD | 3,280,000.00 USD | 63,370.00 USD | 7,750.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.30` | 5,800,000.00 USD | 5,800,000.00 USD | 32,650.00 USD | 42,710.00 USD | 68,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 3,340,000.00 USD | 3,340,000.00 USD | 7,220.00 USD | 1,390.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `298.50` | 442.08 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `298.80` | 3,460,000.00 USD | 3,460,000.00 USD | 23,670.00 USD | 257.02 USD | 94,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 5,880,000.00 USD | 5,880,000.00 USD | 69,820.00 USD | 12,040.00 USD | 112.32 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 3,500,000.00 USD | 3,500,000.00 USD | 8,230.00 USD | 15,610.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.30` | 6,000,000.00 USD | 6,000,000.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.60` | 3,560,000.00 USD | 3,560,000.00 USD | 35,820.00 USD | 5,460.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.80` | 6,050,000.00 USD | 6,050,000.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 3,600,000.00 USD | 3,600,000.00 USD | 3,500.00 USD | 12,210.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.30` | 6,090,000.00 USD | 6,090,000.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 3,720,000.00 USD | 3,720,000.00 USD | 41,760.00 USD | 30,720.00 USD | 42,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 14,550.00 USD | 22,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `300.80` | 3,740,000.00 USD | 3,740,000.00 USD | 526.85 USD | 766.84 USD | 17,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,230,000.00 USD | 6,230,000.00 USD | 25,930.00 USD | 71,120.00 USD | 48,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 3,780,000.00 USD | 3,780,000.00 USD | 252.55 USD | 15,610.00 USD | 30,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.30` | 6,520,000.00 USD | 6,520,000.00 USD | 73,320.00 USD | 57,720.00 USD | 150,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.60` | 3,840,000.00 USD | 3,840,000.00 USD | 19,530.00 USD | 8,210.00 USD | 34,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.80` | 6,760,000.00 USD | 6,760,000.00 USD | 89,300.00 USD | 130,520.00 USD | 26,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 3,910,000.00 USD | 3,910,000.00 USD | 25,220.00 USD | 28,100.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.30` | 6,940,000.00 USD | 6,940,000.00 USD | 1,560.00 USD | 180,380.00 USD | 39.94 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 3,940,000.00 USD | 3,940,000.00 USD | 11,420.00 USD | 4,570.00 USD | 17,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 3,990,000.00 USD | 3,990,000.00 USD | 4,210.00 USD | 12,390.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,170,000.00 USD | 7,170,000.00 USD | 71,700.00 USD | 111,440.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 4,020,000.00 USD | 4,020,000.00 USD | 20,990.00 USD | 884.42 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.30` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 968.59 USD | 183.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 4,030,000.00 USD | 4,030,000.00 USD | 167.69 USD | 1,800.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.80` | 7,220,000.00 USD | 7,220,000.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 4,070,000.00 USD | 4,070,000.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.30` | 7,250,000.00 USD | 7,250,000.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 4,130,000.00 USD | 4,130,000.00 USD | 9,670.00 USD | 2,470.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 4,160,000.00 USD | 4,160,000.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,310,000.00 USD | 7,310,000.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 4,170,000.00 USD | 4,170,000.00 USD | 47.98 USD | 5,340.00 USD | 4,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.30` | 7,740,000.00 USD | 7,740,000.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 4,180,000.00 USD | 4,180,000.00 USD | 7,620.00 USD | 1,650.00 USD | 1,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.80` | 7,880,000.00 USD | 7,880,000.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 4,210,000.00 USD | 4,210,000.00 USD | 9,080.00 USD | 5,780.00 USD | 12,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.30` | 8,040,000.00 USD | 8,040,000.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 4,220,000.00 USD | 4,220,000.00 USD | 7,300.00 USD | 191.14 USD | 5,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 4,290,000.00 USD | 4,290,000.00 USD | 28,750.00 USD | 38,280.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,280,000.00 USD | 8,280,000.00 USD | 94,690.00 USD | 74,180.00 USD | 70,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 4,370,000.00 USD | 4,370,000.00 USD | 11,230.00 USD | 37,090.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.30` | 8,580,000.00 USD | 8,580,000.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.60` | 4,440,000.00 USD | 4,440,000.00 USD | 24,180.00 USD | 38,040.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.80` | 8,870,000.00 USD | 8,870,000.00 USD | 115,070.00 USD | 113,210.00 USD | 60,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 4,510,000.00 USD | 4,510,000.00 USD | 30,230.00 USD | 20,450.00 USD | 21,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.30` | 9,210,000.00 USD | 9,210,000.00 USD | 169,010.00 USD | 59,350.00 USD | 114,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 4,520,000.00 USD | 4,520,000.00 USD | 4,760.00 USD | 3,470.00 USD | 3,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.80` | 4,530,000.00 USD | 4,530,000.00 USD | 9,380.00 USD | 204.90 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,370,000.00 USD | 9,370,000.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.20` | 4,550,000.00 USD | 4,550,000.00 USD | 2,030.00 USD | 6,060.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.30` | 9,480,000.00 USD | 9,480,000.00 USD | 34,260.00 USD | 36,240.00 USD | 36,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.60` | 4,560,000.00 USD | 4,560,000.00 USD | 4,630.00 USD | 5,400.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.80` | 9,830,000.00 USD | 9,830,000.00 USD | 58,760.00 USD | 140,230.00 USD | 150,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.00` | 4,570,000.00 USD | 4,570,000.00 USD | 8,440.00 USD | 2,060.00 USD | 6,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.30` | 10,070,000.00 USD | 10,070,000.00 USD | 49,020.00 USD | 108,410.00 USD | 80,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.40` | 4,590,000.00 USD | 4,590,000.00 USD | 112.30 USD | 2,080.00 USD | 9,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.80` | 4,590,000.00 USD | 4,590,000.00 USD | 5,080.00 USD | 2,080.00 USD | 1.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,180,000.00 USD | 10,180,000.00 USD | 60,910.00 USD | 51,380.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.20` | 4,590,000.00 USD | 4,590,000.00 USD | 257.90 USD | 160.90 USD | 0.82 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.30` | 10,430,000.00 USD | 10,430,000.00 USD | 114,310.00 USD | 65,480.00 USD | 63,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.60` | 4,610,000.00 USD | 4,610,000.00 USD | 7,100.00 USD | 6,520.00 USD | 6.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.80` | 10,480,000.00 USD | 10,480,000.00 USD | 19,880.00 USD | 11,240.00 USD | 25,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.00` | 4,610,000.00 USD | 4,610,000.00 USD | 244.00 USD | 184.55 USD | 4,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.30` | 10,580,000.00 USD | 10,580,000.00 USD | 43,780.00 USD | 11,410.00 USD | 43,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.40` | 4,650,000.00 USD | 4,650,000.00 USD | 14,430.00 USD | 9,350.00 USD | 12,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.80` | 4,670,000.00 USD | 4,670,000.00 USD | 5,750.00 USD | 346.79 USD | 13,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,640,000.00 USD | 10,640,000.00 USD | 29,300.00 USD | 20,380.00 USD | 7,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.20` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 12,950.00 USD | 2,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.30` | 10,760,000.00 USD | 10,760,000.00 USD | 54,040.00 USD | 18,790.00 USD | 45,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.60` | 4,710,000.00 USD | 4,710,000.00 USD | 7,160.00 USD | 7,190.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.80` | 10,850,000.00 USD | 10,850,000.00 USD | 33,220.00 USD | 9,030.00 USD | 44,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.30` | 10,930,000.00 USD | 10,930,000.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.40` | 4,720,000.00 USD | 4,720,000.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.80` | 4,740,000.00 USD | 4,740,000.00 USD | 32.00 USD | 3,720.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 10,970,000.00 USD | 10,970,000.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.20` | 4,740,000.00 USD | 4,740,000.00 USD | 2,020.00 USD | 1,400.00 USD | 1,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.30` | 10,970,000.00 USD | 10,970,000.00 USD | 500.10 USD | 547.95 USD | 9.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `315.60` | 4,750,000.00 USD | 4,750,000.00 USD | 1,730.00 USD | 144.50 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.80` | 11,050,000.00 USD | 11,050,000.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `316.00` | 4,760,000.00 USD | 4,760,000.00 USD | 2,110.00 USD | 0.00 USD | 5,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.30` | 11,150,000.00 USD | 11,150,000.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,210,000.00 USD | 11,210,000.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.30` | 11,230,000.00 USD | 11,230,000.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,260,000.00 USD | 11,260,000.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `318.30` | 11,320,000.00 USD | 11,320,000.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD | `Tier 1 CEX` |
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
| `7D` | `234.80` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 0.00 USD | 182.78 USD | 3,090.00 USD |
| `7D` | `235.30` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 3,770.00 USD | 272.00 USD | 3,650.00 USD |
| `7D` | `235.80` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 0.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `236.30` | 10,100,000.00 USD | 0.00 USD | 10,100,000.00 USD | 5,950.00 USD | 0.00 USD | 7,710.00 USD |
| `7D` | `236.80` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 196.53 USD | 17,300.00 USD | 9,990.00 USD |
| `7D` | `237.30` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 0.00 USD | 0.00 USD | 9,550.00 USD |
| `7D` | `237.80` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 5,120.00 USD | 146.67 USD | 0.00 USD |
| `7D` | `238.30` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 178.62 USD | 6,570.00 USD | 12,600.00 USD |
| `7D` | `238.80` | 10,030,000.00 USD | 0.00 USD | 10,030,000.00 USD | 140.10 USD | 9,360.00 USD | 19,430.00 USD |
| `7D` | `239.30` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 6,300.00 USD | 4,660.00 USD | 4,220.00 USD |
| `7D` | `239.80` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 0.00 USD | 588.60 USD | 0.00 USD |
| `7D` | `240.30` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 0.00 USD | 0.00 USD | 17.73 USD |
| `7D` | `240.80` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 2,780.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.30` | 9,980,000.00 USD | 0.00 USD | 9,980,000.00 USD | 7,150.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.80` | 9,970,000.00 USD | 0.00 USD | 9,970,000.00 USD | 8,740.00 USD | 0.00 USD | 4,900.00 USD |
| `7D` | `242.30` | 9,950,000.00 USD | 0.00 USD | 9,950,000.00 USD | 46,400.00 USD | 11,260.00 USD | 24,970.00 USD |
| `7D` | `242.80` | 9,870,000.00 USD | 0.00 USD | 9,870,000.00 USD | 1,150.00 USD | 5,680.00 USD | 1.62 USD |
| `7D` | `243.30` | 9,860,000.00 USD | 0.00 USD | 9,860,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.80` | 9,850,000.00 USD | 0.00 USD | 9,850,000.00 USD | 30,790.00 USD | 762.05 USD | 20,790.00 USD |
| `7D` | `244.80` | 9,800,000.00 USD | 0.00 USD | 9,800,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.30` | 9,770,000.00 USD | 0.00 USD | 9,770,000.00 USD | 5,050.00 USD | 21,700.00 USD | 4,870.00 USD |
| `7D` | `245.80` | 9,740,000.00 USD | 0.00 USD | 9,740,000.00 USD | 1,310.00 USD | 3,590.00 USD | 3,020.00 USD |
| `7D` | `246.30` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 22,100.00 USD | 18,080.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 9,690,000.00 USD | 0.00 USD | 9,690,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD |
| `7D` | `247.30` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 20,460.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.80` | 9,640,000.00 USD | 0.00 USD | 9,640,000.00 USD | 3,560.00 USD | 4,920.00 USD | 31.56 USD |
| `7D` | `248.30` | 9,630,000.00 USD | 0.00 USD | 9,630,000.00 USD | 5,250.00 USD | 2,370.00 USD | 6,390.00 USD |
| `7D` | `248.80` | 9,620,000.00 USD | 0.00 USD | 9,620,000.00 USD | 36,970.00 USD | 16,480.00 USD | 53,160.00 USD |
| `7D` | `249.30` | 9,510,000.00 USD | 0.00 USD | 9,510,000.00 USD | 27,950.00 USD | 42,050.00 USD | 5,530.00 USD |
| `7D` | `249.80` | 9,430,000.00 USD | 0.00 USD | 9,430,000.00 USD | 56,160.00 USD | 28,590.00 USD | 30,090.00 USD |
| `7D` | `250.30` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 42,450.00 USD | 41,170.00 USD | 10,590.00 USD |
| `7D` | `250.80` | 9,220,000.00 USD | 0.00 USD | 9,220,000.00 USD | 37,150.00 USD | 60,940.00 USD | 36,660.00 USD |
| `7D` | `251.30` | 9,090,000.00 USD | 0.00 USD | 9,090,000.00 USD | 45,790.00 USD | 79,700.00 USD | 21,120.00 USD |
| `7D` | `251.80` | 8,940,000.00 USD | 0.00 USD | 8,940,000.00 USD | 63,310.00 USD | 75,650.00 USD | 46,200.00 USD |
| `7D` | `252.30` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 69,530.00 USD | 32,580.00 USD | 17,360.00 USD |
| `7D` | `252.80` | 8,640,000.00 USD | 0.00 USD | 8,640,000.00 USD | 47,280.00 USD | 19,890.00 USD | 15,320.00 USD |
| `7D` | `253.30` | 8,560,000.00 USD | 0.00 USD | 8,560,000.00 USD | 37,170.00 USD | 49,360.00 USD | 20,250.00 USD |
| `7D` | `253.80` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 10,460.00 USD | 32,560.00 USD | 28,070.00 USD |
| `1D` | `254.00` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 7,950.00 USD | 17,690.00 USD | 15,980.00 USD |
| `7D` | `254.30` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 44,200.00 USD | 44,160.00 USD | 25,760.00 USD |
| `1D` | `254.40` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 8,310.00 USD | 12,740.00 USD | 2.31 USD |
| `1D` | `254.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 2,210.00 USD | 991.04 USD | 17.15 USD |
| `7D` | `254.80` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 51,240.00 USD | 38,370.00 USD | 77,340.00 USD |
| `1D` | `255.20` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 15,800.00 USD | 9,440.00 USD | 12,890.00 USD |
| `7D` | `255.30` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 44,970.00 USD | 12,850.00 USD | 31,400.00 USD |
| `1D` | `255.60` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 14,430.00 USD | 25,340.00 USD | 12,400.00 USD |
| `7D` | `255.80` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 12,780.00 USD | 16,980.00 USD | 29,500.00 USD |
| `1D` | `256.00` | 4,270,000.00 USD | 0.00 USD | 4,270,000.00 USD | 6,630.00 USD | 9,130.00 USD | 13,380.00 USD |
| `7D` | `256.30` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 81,660.00 USD | 24,260.00 USD | 48,030.00 USD |
| `1D` | `256.40` | 4,240,000.00 USD | 0.00 USD | 4,240,000.00 USD | 7,420.00 USD | 29,480.00 USD | 18,680.00 USD |
| `1D` | `256.80` | 4,190,000.00 USD | 0.00 USD | 4,190,000.00 USD | 791.61 USD | 5,950.00 USD | 14,920.00 USD |
| `7D` | `256.80` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 32,750.00 USD | 21,210.00 USD | 64,360.00 USD |
| `1D` | `257.20` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 14,160.00 USD | 1,040.00 USD | 7,340.00 USD |
| `7D` | `257.30` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 16,030.00 USD | 3,420.00 USD | 11,110.00 USD |
| `1D` | `257.60` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD |
| `7D` | `257.80` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 41,630.00 USD | 7,360.00 USD | 18,200.00 USD |
| `1D` | `258.00` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD |
| `7D` | `258.30` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 106,580.00 USD | 46,410.00 USD | 71,560.00 USD |
| `1D` | `258.40` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD |
| `1D` | `258.80` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 8,320.00 USD | 30,410.00 USD | 40,000.00 USD |
| `7D` | `258.80` | 7,350,000.00 USD | 0.00 USD | 7,350,000.00 USD | 115,170.00 USD | 5,390.00 USD | 55,290.00 USD |
| `1D` | `259.20` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 14,560.00 USD | 13,000.00 USD | 17,630.00 USD |
| `7D` | `259.30` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 6,030.00 USD | 45,540.00 USD | 8,060.00 USD |
| `1D` | `259.60` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 13,640.00 USD | 4,640.00 USD | 22,250.00 USD |
| `7D` | `259.80` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 24,560.00 USD | 15,250.00 USD | 114,140.00 USD |
| `1D` | `260.00` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 45,250.00 USD | 32,940.00 USD | 23,930.00 USD |
| `7D` | `260.30` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 100,790.00 USD | 58,310.00 USD | 60,930.00 USD |
| `1D` | `260.40` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 19,630.00 USD | 6,890.00 USD | 16,020.00 USD |
| `1D` | `260.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 1,450.00 USD | 46,360.00 USD | 25,120.00 USD |
| `7D` | `260.80` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 16,450.00 USD | 56,900.00 USD | 60,240.00 USD |
| `1D` | `261.20` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 8,240.00 USD | 22,970.00 USD | 30,850.00 USD |
| `7D` | `261.30` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 7,150.00 USD | 97,320.00 USD | 52,540.00 USD |
| `1D` | `261.60` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 18,640.00 USD | 55,030.00 USD | 53,770.00 USD |
| `7D` | `261.80` | 6,450,000.00 USD | 0.00 USD | 6,450,000.00 USD | 68,120.00 USD | 82,780.00 USD | 45,180.00 USD |
| `1D` | `262.00` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 17,810.00 USD | 43,870.00 USD | 21,380.00 USD |
| `7D` | `262.30` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 43,780.00 USD | 83,350.00 USD | 47,980.00 USD |
| `1D` | `262.40` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 20,850.00 USD | 4,110.00 USD | 10,850.00 USD |
| `1D` | `262.80` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 366.04 USD | 13,020.00 USD | 19,470.00 USD |
| `7D` | `262.80` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 74,900.00 USD | 49,480.00 USD | 32,720.00 USD |
| `1D` | `263.20` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 9,930.00 USD | 4,190.00 USD | 61,430.00 USD |
| `7D` | `263.30` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 33,590.00 USD | 13,230.00 USD | 101.93 USD |
| `1D` | `263.60` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,340.00 USD |
| `7D` | `263.80` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 391,670.00 USD | 1,380.00 USD | 117,860.00 USD |
| `1D` | `264.00` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 52,440.00 USD | 15,290.00 USD | 17,150.00 USD |
| `7D` | `264.30` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 48,690.00 USD | 0.00 USD | 133.80 USD |
| `1D` | `264.40` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 6,250.00 USD | 19,610.00 USD | 0.00 USD |
| `1D` | `264.80` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 22,350.00 USD | 773.98 USD | 20,040.00 USD |
| `7D` | `264.80` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 33,940.00 USD | 21,410.00 USD | 198.07 USD |
| `1D` | `265.20` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 75,770.00 USD | 1,510.00 USD | 33,270.00 USD |
| `7D` | `265.30` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 256,440.00 USD | 0.00 USD | 33,980.00 USD |
| `1D` | `265.60` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 167.69 USD | 228.00 USD | 0.00 USD |
| `7D` | `265.80` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 69,380.00 USD | 0.00 USD | 109.91 USD |
| `1D` | `266.00` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 12,120.00 USD | 63.94 USD | 0.00 USD |
| `7D` | `266.30` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 216,090.00 USD | 0.00 USD | 17.82 USD |
| `1D` | `266.40` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 8,650.00 USD | 13,250.00 USD | 4,800.00 USD |
| `1D` | `266.80` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 36,150.00 USD | 30,370.00 USD | 0.00 USD |
| `7D` | `266.80` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 136,640.00 USD | 63,260.00 USD | 42.10 USD |
| `1D` | `267.20` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 43,080.00 USD | 32,200.00 USD | 12,550.00 USD |
| `7D` | `267.30` | 4,490,000.00 USD | 0.00 USD | 4,490,000.00 USD | 131,280.00 USD | 52,200.00 USD | 23.69 USD |
| `1D` | `267.60` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 4,660.00 USD | 72,250.00 USD | 14,900.00 USD |
| `7D` | `267.80` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 217,320.00 USD | 35,090.00 USD | 38,820.00 USD |
| `1D` | `268.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 4,570.00 USD | 0.00 USD | 49,710.00 USD |
| `7D` | `268.30` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 169,940.00 USD | 148,780.00 USD | 62,780.00 USD |
| `1D` | `268.40` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 0.00 USD | 35,070.00 USD | 13,870.00 USD |
| `1D` | `268.80` | 2,460,000.00 USD | 0.00 USD | 2,460,000.00 USD | 8,400.00 USD | 321.80 USD | 0.00 USD |
| `7D` | `268.80` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 23,340.00 USD | 0.00 USD | 55.96 USD |
| `1D` | `269.20` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 178.30 USD | 703.50 USD | 20.82 USD |
| `7D` | `269.30` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 0.00 USD | 1,930.00 USD | 148.23 USD |
| `1D` | `269.60` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 378.60 USD | 16,500.00 USD | 10,340.00 USD |
| `7D` | `269.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 240.42 USD |
| `1D` | `270.00` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 450.60 USD | 793.00 USD | 3,380.00 USD |
| `7D` | `270.30` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 159.70 USD |
| `1D` | `270.40` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 9,980.00 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `270.80` | 2,400,000.00 USD | 0.00 USD | 2,400,000.00 USD | 323.80 USD | 7,580.00 USD | 0.00 USD |
| `7D` | `270.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 120.25 USD |
| `1D` | `271.20` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 12,890.00 USD | 478.10 USD | 2,750.00 USD |
| `1D` | `271.60` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 5,300.00 USD |
| `7D` | `271.80` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 61,810.00 USD | 0.00 USD | 40,480.00 USD |
| `1D` | `272.00` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 15,100.00 USD | 41,690.00 USD | 9,610.00 USD |
| `7D` | `272.30` | 3,500,000.00 USD | 0.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.40` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 6,060.00 USD | 10,340.00 USD | 38,270.00 USD |
| `1D` | `272.80` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 50,370.00 USD | 5,990.00 USD | 58,560.00 USD |
| `7D` | `272.80` | 3,470,000.00 USD | 0.00 USD | 3,470,000.00 USD | 25,660.00 USD | 69,990.00 USD | 47,720.00 USD |
| `1D` | `273.20` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 14,040.00 USD | 104,070.00 USD | 16,570.00 USD |
| `7D` | `273.30` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 0.00 USD | 70,180.00 USD | 240,480.00 USD |
| `1D` | `273.60` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 11,610.00 USD | 10,810.00 USD | 42,030.00 USD |
| `7D` | `273.80` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 181,410.00 USD | 0.00 USD | 29,020.00 USD |
| `1D` | `274.00` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 164,540.00 USD | 80,800.00 USD | 39,870.00 USD |
| `7D` | `274.30` | 2,810,000.00 USD | 0.00 USD | 2,810,000.00 USD | 476,550.00 USD | 0.00 USD | 83,040.00 USD |
| `1D` | `274.40` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 239,320.00 USD | 0.00 USD | 41,320.00 USD |
| `1D` | `274.80` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 89,480.00 USD | 19,960.00 USD | 12,720.00 USD |
| `7D` | `274.80` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 496,200.00 USD | 0.00 USD | 34,730.00 USD |
| `7D` | `275.30` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.60` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 20,900.00 USD | 10,450.00 USD | 26,710.00 USD |
| `7D` | `275.80` | 1,640,000.00 USD | 0.00 USD | 1,640,000.00 USD | 1,830.00 USD | 23,010.00 USD | 82,330.00 USD |
| `1D` | `276.00` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 83,200.00 USD | 0.00 USD | 40,360.00 USD |
| `7D` | `276.30` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 153,820.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.40` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 6,370.00 USD | 0.00 USD | 8,810.00 USD |
| `1D` | `276.80` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 11,880.00 USD | 13,540.00 USD | 5,500.00 USD |
| `7D` | `276.80` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.20` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 25,720.00 USD | 0.00 USD | 10,600.00 USD |
| `7D` | `277.30` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 152,190.00 USD | 63,290.00 USD | 99,240.00 USD |
| `7D` | `277.80` | 943,170.00 USD | 0.00 USD | 943,170.00 USD | 0.00 USD | 157,740.00 USD | 59,850.00 USD |
| `1D` | `278.00` | 985,900.00 USD | 0.00 USD | 985,900.00 USD | 12,120.00 USD | 21,820.00 USD | 76,520.00 USD |
| `7D` | `278.30` | 725,580.00 USD | 0.00 USD | 725,580.00 USD | 24,750.00 USD | 37,090.00 USD | 95,440.00 USD |
| `1D` | `278.40` | 875,440.00 USD | 0.00 USD | 875,440.00 USD | 42,620.00 USD | 88,620.00 USD | 45,110.00 USD |
| `1D` | `278.80` | 699,090.00 USD | 0.00 USD | 699,090.00 USD | 38,650.00 USD | 21,300.00 USD | 34,450.00 USD |
| `7D` | `278.80` | 568,300.00 USD | 0.00 USD | 568,300.00 USD | 51,310.00 USD | 933.19 USD | 0.00 USD |
| `1D` | `279.20` | 604,700.00 USD | 0.00 USD | 604,700.00 USD | 6,300.00 USD | 64,260.00 USD | 17,940.00 USD |
| `7D` | `279.30` | 516,060.00 USD | 0.00 USD | 516,060.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.60` | 516,200.00 USD | 0.00 USD | 516,200.00 USD | 14,720.00 USD | 21,310.00 USD | 47,450.00 USD |
| `7D` | `279.80` | 513,390.00 USD | 0.00 USD | 513,390.00 USD | 0.00 USD | 1,770.00 USD | 58,030.00 USD |
| `1D` | `280.00` | 432,720.00 USD | 0.00 USD | 432,720.00 USD | 5,130.00 USD | 14,930.00 USD | 31,350.00 USD |
| `7D` | `280.30` | 453,590.00 USD | 0.00 USD | 453,590.00 USD | 0.00 USD | 0.00 USD | 17,360.00 USD |
| `1D` | `280.40` | 381,310.00 USD | 0.00 USD | 381,310.00 USD | 14,910.00 USD | 60,750.00 USD | 97,040.00 USD |
| `1D` | `280.80` | 208,600.00 USD | 0.00 USD | 208,600.00 USD | 28,040.00 USD | 23,190.00 USD | 12.68 USD |
| `7D` | `280.80` | 436,230.00 USD | 0.00 USD | 436,230.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `1D` | `281.20` | 157,360.00 USD | 0.00 USD | 157,360.00 USD | 12,730.00 USD | 6,950.00 USD | 0.00 USD |
| `7D` | `281.30` | 420,690.00 USD | 0.00 USD | 420,690.00 USD | 0.00 USD | 17,720.00 USD | 79,690.00 USD |
| `7D` | `281.80` | 323,280.00 USD | 0.00 USD | 323,280.00 USD | 75,030.00 USD | 0.00 USD | 122,390.00 USD |
| `1D` | `282.00` | 137,680.00 USD | 0.00 USD | 137,680.00 USD | 2,050.00 USD | 21,390.00 USD | 4,140.00 USD |
| `7D` | `282.30` | 125,860.00 USD | 0.00 USD | 125,860.00 USD | 3,520.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.40` | 110,090.00 USD | 0.00 USD | 110,090.00 USD | 8,260.00 USD | 12,740.00 USD | 0.00 USD |
| `1D` | `282.80` | 89,090.00 USD | 0.00 USD | 89,090.00 USD | 0.00 USD | 52,180.00 USD | 19.90 USD |
| `1D` | `283.20` | 36,890.00 USD | 0.00 USD | 36,890.00 USD | 16,210.00 USD | 20,630.00 USD | 47.36 USD |
| `7D` | `283.30` | 101,640.00 USD | 0.00 USD | 101,640.00 USD | 3,450.00 USD | 98,190.00 USD | 0.00 USD |
| `7D` | `283.80` | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.80` | 3,990.00 USD | 3,990.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.30` | 180,540.00 USD | 180,540.00 USD | 0.00 USD | 1,560.00 USD | 174,980.00 USD | 0.00 USD |
| `1D` | `284.40` | 397.40 USD | 397.40 USD | 0.00 USD | 0.00 USD | 397.40 USD | 0.00 USD |
| `1D` | `284.80` | 1,350.00 USD | 1,350.00 USD | 0.00 USD | 0.00 USD | 948.40 USD | 0.00 USD |
| `7D` | `284.80` | 490,550.00 USD | 490,550.00 USD | 0.00 USD | 0.00 USD | 310,010.00 USD | 0.00 USD |
| `1D` | `285.20` | 129,300.00 USD | 129,300.00 USD | 0.00 USD | 86,260.00 USD | 0.00 USD | 41,690.00 USD |
| `7D` | `285.30` | 786,620.00 USD | 786,620.00 USD | 0.00 USD | 68,860.00 USD | 227,210.00 USD | 0.00 USD |
| `1D` | `285.60` | 131,010.00 USD | 131,010.00 USD | 0.00 USD | 1,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `285.80` | 985,210.00 USD | 985,210.00 USD | 0.00 USD | 48,090.00 USD | 150,500.00 USD | 0.00 USD |
| `1D` | `286.00` | 162,240.00 USD | 162,240.00 USD | 0.00 USD | 7,580.00 USD | 434.90 USD | 23,210.00 USD |
| `7D` | `286.30` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 1,200.00 USD | 43,020.00 USD | 0.00 USD |
| `1D` | `286.40` | 168,710.00 USD | 168,710.00 USD | 0.00 USD | 5,620.00 USD | 851.39 USD | 4.24 USD |
| `1D` | `286.80` | 255,560.00 USD | 255,560.00 USD | 0.00 USD | 3,590.00 USD | 5,130.00 USD | 78,130.00 USD |
| `7D` | `286.80` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 30,110.00 USD | 217,580.00 USD | 0.00 USD |
| `1D` | `287.20` | 381,190.00 USD | 381,190.00 USD | 0.00 USD | 51,540.00 USD | 34,260.00 USD | 39,830.00 USD |
| `7D` | `287.30` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 12.00 USD |
| `1D` | `287.60` | 476,060.00 USD | 476,060.00 USD | 0.00 USD | 13,180.00 USD | 24,900.00 USD | 56,790.00 USD |
| `7D` | `287.80` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 4,240.00 USD | 272,200.00 USD | 53,270.00 USD |
| `1D` | `288.00` | 544,350.00 USD | 544,350.00 USD | 0.00 USD | 9,440.00 USD | 14,610.00 USD | 44,250.00 USD |
| `7D` | `288.30` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 35,400.00 USD | 0.00 USD |
| `1D` | `288.40` | 651,530.00 USD | 651,530.00 USD | 0.00 USD | 68,380.00 USD | 18,330.00 USD | 20,470.00 USD |
| `1D` | `288.80` | 682,770.00 USD | 682,770.00 USD | 0.00 USD | 17,070.00 USD | 14,160.00 USD | 11.08 USD |
| `7D` | `288.80` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 124,780.00 USD | 1,140.00 USD | 80,970.00 USD |
| `1D` | `289.20` | 729,630.00 USD | 729,630.00 USD | 0.00 USD | 1,720.00 USD | 14,960.00 USD | 30,180.00 USD |
| `7D` | `289.30` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.60` | 870,720.00 USD | 870,720.00 USD | 0.00 USD | 20,690.00 USD | 37,460.00 USD | 82,950.00 USD |
| `7D` | `289.80` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 51,310.00 USD | 101,040.00 USD | 134,010.00 USD |
| `1D` | `290.00` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 86,650.00 USD | 47,310.00 USD | 84,690.00 USD |
| `7D` | `290.30` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `290.40` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 10,530.00 USD | 80,370.00 USD | 32,790.00 USD |
| `1D` | `290.80` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 33,300.00 USD | 63,390.00 USD | 54,940.00 USD |
| `7D` | `290.80` | 2,490,000.00 USD | 2,490,000.00 USD | 0.00 USD | 898.13 USD | 1,760.00 USD | 58,030.00 USD |
| `1D` | `291.20` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 15,390.00 USD | 11,280.00 USD | 24,320.00 USD |
| `7D` | `291.30` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 24,680.00 USD | 10,160.00 USD | 0.00 USD |
| `1D` | `291.60` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 1,740.00 USD | 20,290.00 USD | 22,150.00 USD |
| `7D` | `291.80` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 4,030.00 USD | 177,200.00 USD | 19,430.00 USD |
| `1D` | `292.00` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 1,150.00 USD | 45,050.00 USD | 34.55 USD |
| `7D` | `292.30` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 1,240.00 USD | 73,530.00 USD | 42.88 USD |
| `1D` | `292.40` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 22,300.00 USD | 12,110.00 USD | 13,730.00 USD |
| `1D` | `292.80` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 12,680.00 USD | 21,060.00 USD | 3,560.00 USD |
| `7D` | `292.80` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 887.27 USD | 100,630.00 USD | 138.60 USD |
| `1D` | `293.20` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 20,320.00 USD | 14,450.00 USD | 27,370.00 USD |
| `7D` | `293.30` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 534.50 USD | 132,080.00 USD | 36.33 USD |
| `1D` | `293.60` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 77,480.00 USD | 41,450.00 USD | 16,340.00 USD |
| `7D` | `293.80` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 38,790.00 USD | 1,860.00 USD | 126.44 USD |
| `1D` | `294.00` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 30,820.00 USD | 20,050.00 USD | 60,900.00 USD |
| `7D` | `294.30` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 217,140.00 USD | 33,590.00 USD | 146,150.00 USD |
| `1D` | `294.40` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 50,740.00 USD | 55,140.00 USD | 113,130.00 USD |
| `1D` | `294.80` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 57,560.00 USD | 16,260.00 USD | 44,460.00 USD |
| `7D` | `294.80` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 63,770.00 USD | 109,430.00 USD | 89,160.00 USD |
| `1D` | `295.20` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 6,060.00 USD | 11,650.00 USD | 80,350.00 USD |
| `7D` | `295.30` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 46,330.00 USD | 83,210.00 USD | 345,510.00 USD |
| `1D` | `295.60` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 61,310.00 USD | 38,860.00 USD | 122,260.00 USD |
| `7D` | `295.80` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 165,320.00 USD | 72,570.00 USD | 167,420.00 USD |
| `1D` | `296.00` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 48,420.00 USD | 100,760.00 USD | 32,880.00 USD |
| `7D` | `296.30` | 4,950,000.00 USD | 4,950,000.00 USD | 0.00 USD | 43,710.00 USD | 167,290.00 USD | 120,790.00 USD |
| `1D` | `296.40` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 77,530.00 USD | 31,150.00 USD | 27,010.00 USD |
| `1D` | `296.80` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 24,600.00 USD | 31,800.00 USD | 74,430.00 USD |
| `7D` | `296.80` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 133,820.00 USD | 2,910.00 USD | 201,380.00 USD |
| `1D` | `297.20` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 56,360.00 USD | 1,060.00 USD | 50,250.00 USD |
| `7D` | `297.30` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 78,980.00 USD | 53,400.00 USD | 72.03 USD |
| `1D` | `297.60` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 7,710.00 USD | 10,830.00 USD | 29,780.00 USD |
| `7D` | `297.80` | 5,660,000.00 USD | 5,660,000.00 USD | 0.00 USD | 47,530.00 USD | 99,320.00 USD | 89,610.00 USD |
| `1D` | `298.00` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 63,370.00 USD | 7,750.00 USD | 41,710.00 USD |
| `7D` | `298.30` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 32,650.00 USD | 42,710.00 USD | 68,810.00 USD |
| `1D` | `298.40` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 7,220.00 USD | 1,390.00 USD | 56,410.00 USD |
| `1D` | `298.80` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 23,670.00 USD | 257.02 USD | 94,680.00 USD |
| `7D` | `298.80` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 69,820.00 USD | 12,040.00 USD | 112.32 USD |
| `1D` | `299.20` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 8,230.00 USD | 15,610.00 USD | 12,340.00 USD |
| `7D` | `299.30` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 3,550.00 USD | 26,470.00 USD | 85,830.00 USD |
| `1D` | `299.60` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 35,820.00 USD | 5,460.00 USD | 21,870.00 USD |
| `7D` | `299.80` | 6,050,000.00 USD | 6,050,000.00 USD | 0.00 USD | 22,950.00 USD | 9,100.00 USD | 19,830.00 USD |
| `1D` | `300.00` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 3,500.00 USD | 12,210.00 USD | 27,500.00 USD |
| `7D` | `300.30` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 35,320.00 USD | 2,910.00 USD | 16.16 USD |
| `1D` | `300.40` | 3,720,000.00 USD | 3,720,000.00 USD | 0.00 USD | 41,760.00 USD | 30,720.00 USD | 42,620.00 USD |
| `1D` | `300.80` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 526.85 USD | 766.84 USD | 17,290.00 USD |
| `7D` | `300.80` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 25,930.00 USD | 71,120.00 USD | 48,300.00 USD |
| `1D` | `301.20` | 3,780,000.00 USD | 3,780,000.00 USD | 0.00 USD | 252.55 USD | 15,610.00 USD | 30,780.00 USD |
| `7D` | `301.30` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 73,320.00 USD | 57,720.00 USD | 150,400.00 USD |
| `1D` | `301.60` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 19,530.00 USD | 8,210.00 USD | 34,830.00 USD |
| `7D` | `301.80` | 6,760,000.00 USD | 6,760,000.00 USD | 0.00 USD | 89,300.00 USD | 130,520.00 USD | 26,330.00 USD |
| `1D` | `302.00` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 25,220.00 USD | 28,100.00 USD | 10,360.00 USD |
| `7D` | `302.30` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 1,560.00 USD | 180,380.00 USD | 39.94 USD |
| `1D` | `302.40` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 11,420.00 USD | 4,570.00 USD | 17,550.00 USD |
| `1D` | `302.80` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 4,210.00 USD | 12,390.00 USD | 34,910.00 USD |
| `7D` | `302.80` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 71,700.00 USD | 111,440.00 USD | 41,810.00 USD |
| `1D` | `303.20` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 20,990.00 USD | 884.42 USD | 9,360.00 USD |
| `7D` | `303.30` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 0.00 USD | 968.59 USD | 183.84 USD |
| `1D` | `303.60` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 167.69 USD | 1,800.00 USD | 1.44 USD |
| `7D` | `303.80` | 7,220,000.00 USD | 7,220,000.00 USD | 0.00 USD | 20,720.00 USD | 10,170.00 USD | 24,710.00 USD |
| `1D` | `304.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD |
| `7D` | `304.30` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 2,500.00 USD | 5,160.00 USD | 21,390.00 USD |
| `1D` | `304.40` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 9,670.00 USD | 2,470.00 USD | 49,830.00 USD |
| `1D` | `304.80` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD |
| `7D` | `304.80` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 36,140.00 USD | 11,790.00 USD | 4,050.00 USD |
| `1D` | `305.20` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 47.98 USD | 5,340.00 USD | 4,030.00 USD |
| `7D` | `305.30` | 7,740,000.00 USD | 7,740,000.00 USD | 0.00 USD | 164,710.00 USD | 143,110.00 USD | 121,430.00 USD |
| `1D` | `305.60` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 7,620.00 USD | 1,650.00 USD | 1,500.00 USD |
| `7D` | `305.80` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 81,430.00 USD | 52,160.00 USD | 12,740.00 USD |
| `1D` | `306.00` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 9,080.00 USD | 5,780.00 USD | 12,240.00 USD |
| `7D` | `306.30` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 30,110.00 USD | 63,880.00 USD | 63,800.00 USD |
| `1D` | `306.40` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 7,300.00 USD | 191.14 USD | 5,670.00 USD |
| `1D` | `306.80` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 28,750.00 USD | 38,280.00 USD | 5,490.00 USD |
| `7D` | `306.80` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 94,690.00 USD | 74,180.00 USD | 70,010.00 USD |
| `1D` | `307.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 11,230.00 USD | 37,090.00 USD | 32,720.00 USD |
| `7D` | `307.30` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 27,410.00 USD | 136,020.00 USD | 134,390.00 USD |
| `1D` | `307.60` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 24,180.00 USD | 38,040.00 USD | 1,620.00 USD |
| `7D` | `307.80` | 8,870,000.00 USD | 8,870,000.00 USD | 0.00 USD | 115,070.00 USD | 113,210.00 USD | 60,720.00 USD |
| `1D` | `308.00` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 30,230.00 USD | 20,450.00 USD | 21,270.00 USD |
| `7D` | `308.30` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 169,010.00 USD | 59,350.00 USD | 114,230.00 USD |
| `1D` | `308.40` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 4,760.00 USD | 3,470.00 USD | 3,000.00 USD |
| `1D` | `308.80` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 9,380.00 USD | 204.90 USD | 3,480.00 USD |
| `7D` | `308.80` | 9,370,000.00 USD | 9,370,000.00 USD | 0.00 USD | 78,590.00 USD | 51,820.00 USD | 35,090.00 USD |
| `1D` | `309.20` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 2,030.00 USD | 6,060.00 USD | 2,800.00 USD |
| `7D` | `309.30` | 9,480,000.00 USD | 9,480,000.00 USD | 0.00 USD | 34,260.00 USD | 36,240.00 USD | 36,580.00 USD |
| `1D` | `309.60` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 4,630.00 USD | 5,400.00 USD | 2,060.00 USD |
| `7D` | `309.80` | 9,830,000.00 USD | 9,830,000.00 USD | 0.00 USD | 58,760.00 USD | 140,230.00 USD | 150,830.00 USD |
| `1D` | `310.00` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 8,440.00 USD | 2,060.00 USD | 6,290.00 USD |
| `7D` | `310.30` | 10,070,000.00 USD | 10,070,000.00 USD | 0.00 USD | 49,020.00 USD | 108,410.00 USD | 80,780.00 USD |
| `1D` | `310.40` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 112.30 USD | 2,080.00 USD | 9,630.00 USD |
| `1D` | `310.80` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 5,080.00 USD | 2,080.00 USD | 1.49 USD |
| `7D` | `310.80` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 60,910.00 USD | 51,380.00 USD | 3,850.00 USD |
| `1D` | `311.20` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 257.90 USD | 160.90 USD | 0.82 USD |
| `7D` | `311.30` | 10,430,000.00 USD | 10,430,000.00 USD | 0.00 USD | 114,310.00 USD | 65,480.00 USD | 63,850.00 USD |
| `1D` | `311.60` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 7,100.00 USD | 6,520.00 USD | 6.94 USD |
| `7D` | `311.80` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 19,880.00 USD | 11,240.00 USD | 25,570.00 USD |
| `1D` | `312.00` | 4,610,000.00 USD | 4,610,000.00 USD | 0.00 USD | 244.00 USD | 184.55 USD | 4,070.00 USD |
| `7D` | `312.30` | 10,580,000.00 USD | 10,580,000.00 USD | 0.00 USD | 43,780.00 USD | 11,410.00 USD | 43,600.00 USD |
| `1D` | `312.40` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 14,430.00 USD | 9,350.00 USD | 12,380.00 USD |
| `1D` | `312.80` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 5,750.00 USD | 346.79 USD | 13,380.00 USD |
| `7D` | `312.80` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 29,300.00 USD | 20,380.00 USD | 7,420.00 USD |
| `1D` | `313.20` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 12,950.00 USD | 2,580.00 USD |
| `7D` | `313.30` | 10,760,000.00 USD | 10,760,000.00 USD | 0.00 USD | 54,040.00 USD | 18,790.00 USD | 45,480.00 USD |
| `1D` | `313.60` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 7,160.00 USD | 7,190.00 USD | 8,220.00 USD |
| `7D` | `313.80` | 10,850,000.00 USD | 10,850,000.00 USD | 0.00 USD | 33,220.00 USD | 9,030.00 USD | 44,160.00 USD |
| `1D` | `314.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD |
| `7D` | `314.30` | 10,930,000.00 USD | 10,930,000.00 USD | 0.00 USD | 52,520.00 USD | 307.60 USD | 35,620.00 USD |
| `1D` | `314.40` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 4,210.00 USD | 0.00 USD | 7,320.00 USD |
| `1D` | `314.80` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 32.00 USD | 3,720.00 USD | 9,250.00 USD |
| `7D` | `314.80` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 24,660.00 USD | 0.00 USD | 10,290.00 USD |
| `1D` | `315.20` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 2,020.00 USD | 1,400.00 USD | 1,620.00 USD |
| `7D` | `315.30` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 500.10 USD | 547.95 USD | 9.16 USD |
| `1D` | `315.60` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 1,730.00 USD | 144.50 USD | 5,230.00 USD |
| `7D` | `315.80` | 11,050,000.00 USD | 11,050,000.00 USD | 0.00 USD | 9,200.00 USD | 43,070.00 USD | 30,060.00 USD |
| `1D` | `316.00` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 2,110.00 USD | 0.00 USD | 5,590.00 USD |
| `7D` | `316.30` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 38,840.00 USD | 19,680.00 USD | 43,430.00 USD |
| `7D` | `316.80` | 11,210,000.00 USD | 11,210,000.00 USD | 0.00 USD | 18,110.00 USD | 21,050.00 USD | 18,400.00 USD |
| `7D` | `317.30` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD |
| `7D` | `317.80` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 21,640.00 USD | 8,380.00 USD | 108.90 USD |
| `7D` | `318.30` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 627.00 USD | 31,660.00 USD | 32,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `308.34M` | Total OI Tokens: `1,084,916.4 BCH`
  * 1h OI Change: `+0.46%` | 4h OI Change: `+4.09%` | 24h OI Change: `-1.57%`
  * Exchange Breakdown: Binance=`90.06M` | Bybit=`38.76M` | OKX=`24.08M` | Hyperliquid=`7.25M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `14.45K` | Last 24h: `11.49K` | Last 3d: `73.35K` | Last 7d: `145.00K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0083%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BCH` | `51.61%` | `48.39%` | `1.07` | 3,110,000.00 USD |
| `15M` | `Binance` | `43.87%` | `56.13%` | `0.78` | 1,140,000.00 USD |
| `15M` | `OKX` | `46.64%` | `53.36%` | `0.87` | 401,420.00 USD |
| `15M` | `Bybit` | `76.03%` | `23.97%` | `3.17` | 337,720.00 USD |
| `15M` | `KuCoin` | `48.6%` | `51.4%` | `0.95` | 42,840.00 USD |
| `15M` | `Gate` | `64.33%` | `35.67%` | `1.80` | 292,980.00 USD |
| `15M` | `Bitget` | `65.31%` | `34.69%` | `1.88` | 180,760.00 USD |
| `15M` | `BingX` | `42.33%` | `57.67%` | `0.73` | 423,890.00 USD |
| `15M` | `MEXC` | `31.65%` | `68.35%` | `0.46` | 39,150.00 USD |
| `15M` | `Bitunix` | `77.02%` | `22.98%` | `3.35` | 38,150.00 USD |
| `15M` | `Hyperliquid` | `35.58%` | `64.42%` | `0.55` | 7,150.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.33%` | `50.67%` | `0.97` | 161,610.00 USD |
| `15M` | `Crypto.com` | `66.63%` | `33.37%` | `2.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 37,310.00 USD |
| `15M` | `HTX` | `20.93%` | `79.07%` | `0.26` | 9,500.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `84.83%` | `15.17%` | `5.59` | 284.59 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 901.00 USD |
| `15M` | `Whale Positions` | `43.87%` | `56.13%` | `0.78` | 1,140,000.00 USD |
| `15M` | `Global Accounts` | `51.61%` | `48.39%` | `1.07` | 3,110,000.00 USD |
| `1H` | `BCH` | `51.13%` | `48.87%` | `1.05` | 10,060,000.00 USD |
| `1H` | `Binance` | `53.01%` | `46.99%` | `1.13` | 3,100,000.00 USD |
| `1H` | `OKX` | `55.33%` | `44.67%` | `1.24` | 1,960,000.00 USD |
| `1H` | `Bybit` | `69.73%` | `30.27%` | `2.30` | 1,350,000.00 USD |
| `1H` | `KuCoin` | `51.13%` | `48.87%` | `1.05` | 565,260.00 USD |
| `1H` | `Gate` | `55.45%` | `44.55%` | `1.24` | 171,060.00 USD |
| `1H` | `Bitget` | `62.92%` | `37.08%` | `1.70` | 129,340.00 USD |
| `1H` | `BingX` | `20.54%` | `79.46%` | `0.26` | 450,710.00 USD |
| `1H` | `MEXC` | `45.88%` | `54.12%` | `0.85` | 280,050.00 USD |
| `1H` | `Bitunix` | `35.56%` | `64.44%` | `0.55` | 310,820.00 USD |
| `1H` | `Hyperliquid` | `69.39%` | `30.61%` | `2.27` | 21,690.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.16%` | `53.84%` | `0.86` | 1,290,000.00 USD |
| `1H` | `Crypto.com` | `78.78%` | `21.22%` | `3.71` | 93.67 USD |
| `1H` | `WhiteBIT` | `11.29%` | `88.71%` | `0.13` | 405,510.00 USD |
| `1H` | `HTX` | `76.62%` | `23.38%` | `3.28` | 5,760.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `99.58%` | `0.42%` | `237.10` | 13,630.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `36.04%` | `63.96%` | `0.56` | 1,050.00 USD |
| `1H` | `Whale Positions` | `53.01%` | `46.99%` | `1.13` | 3,100,000.00 USD |
| `1H` | `Global Accounts` | `51.13%` | `48.87%` | `1.05` | 10,060,000.00 USD |
| `4H` | `BCH` | `47.41%` | `52.59%` | `0.90` | 73,430,000.00 USD |
| `4H` | `Binance` | `47.09%` | `52.91%` | `0.89` | 24,990,000.00 USD |
| `4H` | `OKX` | `51.58%` | `48.42%` | `1.07` | 17,870,000.00 USD |
| `4H` | `Bybit` | `55.05%` | `44.95%` | `1.22` | 5,950,000.00 USD |
| `4H` | `KuCoin` | `50.82%` | `49.18%` | `1.03` | 2,500,000.00 USD |
| `4H` | `Gate` | `46.15%` | `53.85%` | `0.86` | 1,480,000.00 USD |
| `4H` | `Bitget` | `52.23%` | `47.77%` | `1.09` | 1,860,000.00 USD |
| `4H` | `BingX` | `19.78%` | `80.22%` | `0.25` | 2,840,000.00 USD |
| `4H` | `MEXC` | `54.68%` | `45.32%` | `1.21` | 1,040,000.00 USD |
| `4H` | `Bitunix` | `50.26%` | `49.74%` | `1.01` | 2,170,000.00 USD |
| `4H` | `Hyperliquid` | `37.72%` | `62.28%` | `0.61` | 660,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `47.67%` | `52.33%` | `0.91` | 10,450,000.00 USD |
| `4H` | `Crypto.com` | `82.61%` | `17.39%` | `4.75` | 1,360.00 USD |
| `4H` | `WhiteBIT` | `5.7%` | `94.3%` | `0.06` | 1,410,000.00 USD |
| `4H` | `HTX` | `43.08%` | `56.92%` | `0.76` | 59,560.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `10.78%` | `89.22%` | `0.12` | 7,620.00 USD |
| `4H` | `Aster` | `48.91%` | `51.09%` | `0.96` | 85,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `53.32%` | `46.68%` | `1.14` | 37,150.00 USD |
| `4H` | `Whale Positions` | `47.09%` | `52.91%` | `0.89` | 24,990,000.00 USD |
| `4H` | `Global Accounts` | `47.41%` | `52.59%` | `0.90` | 73,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `282.40` | `283.39` | `282.40` | `284.76` | `281.82` | 2,261,635.40 USD | 1,044,285.27 USD | 1,217,350.14 USD | -173,064.87 USD | `-7.65%` | `26B / 23S` |
| `0:00 UTC` | `287.03` | `284.86` | `287.03` | `287.15` | `282.35` | 3,497,591.91 USD | 1,841,198.98 USD | 1,656,392.94 USD | 184,806.04 USD | `+5.28%` | `24B / 10S` |
| `5:00 UTC` | `284.49` | `285.18` | `284.49` | `286.67` | `284.13` | 976,529.89 USD | 414,772.25 USD | 561,757.64 USD | -146,985.38 USD | `-15.05%` | `8B / 33S` |
| `0:00 UTC` | `284.00` | `284.42` | `284.00` | `285.15` | `283.77` | 825,459.63 USD | 394,600.86 USD | 430,858.77 USD | -36,257.91 USD | `-4.39%` | `20B / 24S` |
| `5:00 UTC` | `284.75` | `284.10` | `284.75` | `284.97` | `283.36` | 1,321,321.21 USD | 645,681.70 USD | 675,639.51 USD | -29,957.81 USD | `-2.27%` | `33B / 48S` |
| `0:00 UTC` | `284.87` | `284.37` | `284.87` | `285.61` | `283.47` | 932,067.73 USD | 549,811.25 USD | 382,256.48 USD | 167,554.77 USD | `+17.98%` | `21B / 18S` |
| `5:00 UTC` | `284.45` | `284.39` | `284.45` | `285.15` | `283.92` | 434,490.61 USD | 240,391.53 USD | 194,099.07 USD | 46,292.46 USD | `+10.65%` | `28B / 17S` |
| `0:00 UTC` | `284.90` | `285.00` | `284.90` | `285.60` | `284.43` | 472,346.34 USD | 237,853.29 USD | 234,493.05 USD | 3,360.25 USD | `+0.71%` | `26B / 30S` |
| `5:00 UTC` | `284.95` | `284.76` | `284.95` | `285.69` | `283.69` | 541,584.39 USD | 205,935.09 USD | 335,649.30 USD | -129,714.21 USD | `-23.95%` | `9B / 38S` |
| `0:00 UTC` | `283.83` | `283.92` | `283.83` | `284.03` | `283.83` | 27,260.29 USD | 7,646.28 USD | 19,614.01 USD | -11,967.74 USD | `-43.90%` | `1B / 8S` |

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
| `5m` | -6,510.00 USD | 18,840.00 USD | **`ACCUMULATION`** |
| `15m` | -8,020.00 USD | 353,230.00 USD | **`ACCUMULATION`** |
| `30m` | 1,530.00 USD | 495,500.00 USD | **`ACCUMULATION`** |
| `1h` | 90,690.00 USD | 1,160,000.00 USD | **`ACCUMULATION`** |
| `2h` | 437,680.00 USD | 87,940.00 USD | **`ACCUMULATION`** |
| `4h` | 1,150,000.00 USD | -227,880.00 USD | **`ACCUMULATION`** |
| `6h` | 612,270.00 USD | 2,370,000.00 USD | **`ACCUMULATION`** |
| `8h` | 702,350.00 USD | -906,470.00 USD | **`DISTRIBUTION`** |
| `12h` | -124,050.00 USD | -216,130.00 USD | **`DISTRIBUTION`** |
| `24h` | 59,950.00 USD | -4,100,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -913,770.00 USD | -14,160,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -14,410,000.00 USD | -136,730,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.51K` | 15m=`-8.02K` | 1h=`+90.69K` | 24h=`+59.95K`
* Futures Capital Netflows: 5m=`+18.84K` | 15m=`+353.23K` | 1h=`+1.16M` | 24h=`-4.10M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `268.48` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `264.35` (Risk Distance: `4.13` pts)
  * +2.5R Take Profit: `278.81`
  * Mathematical Lot Sizing: **`2.41 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `278.75` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `282.88` (Risk Distance: `4.13` pts)
  * +2.5R Take Profit: `268.42`
  * Mathematical Lot Sizing: **`2.41 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`286.83`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
