# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BCH
**Canonical Key**: `BCH` | **Broker Instrument**: `BCHUSD.p` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `283.86` | **Live Ask Quote**: `284.54` | **Mid Price**: `284.20`
- **Spread Points**: `680.00` | **Spread BPS**: `23.93 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `276.95` | VWAP Z-Score: `+1.21` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `2.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `60.23` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `295.05` | Lower -3.00σ Band: `258.85`
  * Upper +2.51σ Band: `292.10` | Lower -2.51σ Band: `261.80`
  * Upper +2.01σ Band: `289.08` | Lower -2.01σ Band: `264.82`
  * Upper +2.00σ Band: `289.02` | Lower -2.00σ Band: `264.88`
  * Upper +1.28σ Band: `284.67` | Lower -1.28σ Band: `269.23`
  * Upper +1.00σ Band: `282.98` | Lower -1.00σ Band: `270.91`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`281.31` | EMA-20=`281.14` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`280.48` (Slope: `+0.0000`) | EMA-100=`280.88`
  * Institutional Anchors: EMA-144=`281.75` | EMA-200=`283.38` (Slope: `-0.1197`) | EMA-233=`284.20`
- **Range Boundaries**: 24H High=`292.96` | 24H Low=`262.56` | Weekly High=`304.16` | Weekly Low=`262.56`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `284.44` (Distance: `+0.00%`)
  * Point of Control (POC) = `283.81` (Distance: `+0.23%`)
  * Value Area Low (VAL) = `273.07` (Distance: `+4.17%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`288.04` | POC=`278.98` | VAL=`276.48`
  * Prior Day Extremes: PDH=`292.96` | PDL=`269.53` | PDC=`270.09`
  * Monday Range Blueprint: High=`283.95` | Mid=`278.61` | Low=`273.26`
  * Developing Weekly Value Area: Weekly VAH=`289.32` | Weekly POC=`278.51` | Weekly VAL=`274.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`286.26` | Low=`262.56`
  * London Session (08:00-16:00 UTC): High=`284.96` | Low=`278.06`
  * New York Session (13:00-21:00 UTC): High=`284.46` | Low=`279.46`
  * Initial Balance (First Hour): IB High=`284.86` | IB Low=`282.66`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `283.06` - `285.34`
  * Optimal Trade Entry (OTE 0.705): `284.77`
  * Structural Invalidation Anchor (0.786): `286.47`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `284.29` | `284.99` | `284.04` | `284.76` | `827` | 235,478.84 USD | 39,289.22 USD | `+16.68%` | -1,540,329.20 USD | `+0.37` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `284.76` | `284.96` | `283.70` | `283.86` | `973` | 276,491.03 USD | -49,734.94 USD | `-17.99%` | -1,590,064.15 USD | `-0.77` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `283.86` | `284.47` | `283.74` | `284.35` | `276` | 78,392.70 USD | 7,793.39 USD | `+9.94%` | -1,582,270.76 USD | `-0.07` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `280.48` | `282.20` | `280.15` | `281.70` | `2,342` | 658,245.44 USD | 170,536.24 USD | `+25.91%` | -1,539,774.85 USD | `+1.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `281.72` | `284.99` | `281.56` | `284.76` | `4,953` | 1,404,905.07 USD | 153,177.98 USD | `+10.90%` | -1,386,596.87 USD | `+0.89` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `284.76` | `284.96` | `283.70` | `284.44` | `1,251` | 355,569.09 USD | -41,350.60 USD | `-11.63%` | -1,427,947.48 USD | `-0.17` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `281.78` | `283.64` | `278.73` | `279.02` | `16,468` | 4,630,594.81 USD | 275,996.65 USD | `+5.96%` | -1,529,264.29 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `279.03` | `282.29` | `278.54` | `281.15` | `18,009` | 5,054,095.53 USD | -226,117.37 USD | `-4.47%` | -1,755,381.65 USD | `-0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `281.14` | `284.99` | `280.02` | `284.36` | `10,258` | 2,898,891.02 USD | 326,916.59 USD | `+11.28%` | -1,428,465.06 USD | `+0.59` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `284.99` | `278.54` | `284.35` | `44,734` | 12,583,423.82 USD | 376,722.51 USD | `+2.99%` | -1,363,188.14 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `287.97` | `293.41` | `285.90` | `286.78` | `93,832` | 27,140,746.86 USD | -1,471,901.93 USD | `-5.42%` | 272,834.37 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `286.78` | `286.91` | `269.28` | `273.69` | `173,941` | 48,134,933.69 USD | -1,778,544.61 USD | `-3.69%` | -1,505,710.23 USD | `-0.80` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `273.69` | `284.75` | `263.06` | `283.99` | `130,478` | 35,571,721.39 USD | 290,178.37 USD | `+0.82%` | -1,215,531.86 USD | `+0.42` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `283.99` | `287.12` | `280.79` | `281.78` | `53,010` | 15,060,754.66 USD | -524,378.78 USD | `-3.48%` | -1,739,910.64 USD | `-0.14` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `281.78` | `284.99` | `278.54` | `284.35` | `44,734` | 12,583,423.82 USD | 376,722.51 USD | `+2.99%` | -1,363,188.14 USD | `+0.51` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`284.20`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:23:13 IST` |

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
| `7D` | `Long Liquidation` | `240.00` | 10,360,000.00 USD | 10,360,000.00 USD | 887.27 USD | 588.60 USD | 37.38 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.40` | 10,360,000.00 USD | 10,360,000.00 USD | 1,510.00 USD | 0.00 USD | 17.73 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `240.80` | 10,350,000.00 USD | 10,350,000.00 USD | 1,270.00 USD | 0.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `241.20` | 10,350,000.00 USD | 10,350,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `241.50` | 251.88 USD | 40,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `241.60` | 10,350,000.00 USD | 10,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.00` | 10,340,000.00 USD | 10,340,000.00 USD | 27,990.00 USD | 11,260.00 USD | 21,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `242.40` | 10,280,000.00 USD | 10,280,000.00 USD | 27,150.00 USD | 0.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `242.50` | 7,180.00 USD | 40,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `242.80` | 10,240,000.00 USD | 10,240,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `243.20` | 10,240,000.00 USD | 10,240,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `243.50` | 1,850.00 USD | 33,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `243.60` | 10,220,000.00 USD | 10,220,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `244.00` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `244.50` | 5,760.00 USD | 31,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `244.80` | 10,170,000.00 USD | 10,170,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `245.20` | 10,150,000.00 USD | 10,150,000.00 USD | 599.05 USD | 15,350.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `245.50` | 1,030.00 USD | 25,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `245.60` | 10,130,000.00 USD | 10,130,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.00` | 10,110,000.00 USD | 10,110,000.00 USD | 11,860.00 USD | 8,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.40` | 10,090,000.00 USD | 10,090,000.00 USD | 11,440.00 USD | 10,300.00 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `246.80` | 10,060,000.00 USD | 10,060,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `247.20` | 10,050,000.00 USD | 10,050,000.00 USD | 14,580.00 USD | 17,320.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `247.50` | 106.67 USD | 24,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `247.60` | 10,020,000.00 USD | 10,020,000.00 USD | 9,000.00 USD | 4,610.00 USD | 11.75 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.00` | 10,000,000.00 USD | 10,000,000.00 USD | 555.60 USD | 310.87 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `248.40` | 10,000,000.00 USD | 10,000,000.00 USD | 13,830.00 USD | 3,060.00 USD | 28,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `248.50` | 595.16 USD | 24,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `248.80` | 9,960,000.00 USD | 9,960,000.00 USD | 28,270.00 USD | 15,790.00 USD | 28,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.20` | 9,880,000.00 USD | 9,880,000.00 USD | 23,830.00 USD | 30,530.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `249.60` | 9,830,000.00 USD | 9,830,000.00 USD | 46,340.00 USD | 35,710.00 USD | 16,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.00` | 9,730,000.00 USD | 9,730,000.00 USD | 38,050.00 USD | 9,910.00 USD | 22,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `250.40` | 5,070,000.00 USD | 5,070,000.00 USD | 9,190.00 USD | 6,150.00 USD | 12,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.40` | 9,660,000.00 USD | 9,660,000.00 USD | 22,500.00 USD | 35,680.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,330.00 USD | 24,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `250.80` | 5,050,000.00 USD | 5,050,000.00 USD | 9,730.00 USD | 14,160.00 USD | 10,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `250.80` | 9,590,000.00 USD | 9,590,000.00 USD | 32,990.00 USD | 60,940.00 USD | 27,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `251.20` | 5,010,000.00 USD | 5,010,000.00 USD | 25,370.00 USD | 23,980.00 USD | 16,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.20` | 9,460,000.00 USD | 9,460,000.00 USD | 44,420.00 USD | 56,200.00 USD | 18,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `251.50` | 268.35 USD | 22,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `251.60` | 4,950,000.00 USD | 4,950,000.00 USD | 26,820.00 USD | 47,060.00 USD | 19,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `251.60` | 9,340,000.00 USD | 9,340,000.00 USD | 51,190.00 USD | 89,120.00 USD | 44,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.00` | 4,850,000.00 USD | 4,850,000.00 USD | 16,340.00 USD | 11,100.00 USD | 16,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.00` | 9,160,000.00 USD | 9,160,000.00 USD | 63,990.00 USD | 31,270.00 USD | 32,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `252.40` | 4,810,000.00 USD | 4,810,000.00 USD | 6,700.00 USD | 1,540.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.40` | 9,030,000.00 USD | 9,030,000.00 USD | 53,750.00 USD | 29,340.00 USD | 17,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `252.50` | 1,030.00 USD | 22,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `252.80` | 4,800,000.00 USD | 4,800,000.00 USD | 6,800.00 USD | 2,270.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `252.80` | 8,930,000.00 USD | 8,930,000.00 USD | 24,570.00 USD | 10,300.00 USD | 13.01 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.20` | 4,780,000.00 USD | 4,780,000.00 USD | 8,060.00 USD | 3,910.00 USD | 821.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.20` | 8,900,000.00 USD | 8,900,000.00 USD | 12,620.00 USD | 36,470.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `253.60` | 4,770,000.00 USD | 4,770,000.00 USD | 22,180.00 USD | 19,850.00 USD | 21,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `253.60` | 8,830,000.00 USD | 8,830,000.00 USD | 27,790.00 USD | 37,080.00 USD | 34,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.00` | 4,710,000.00 USD | 4,710,000.00 USD | 5,800.00 USD | 8,100.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.00` | 8,730,000.00 USD | 8,730,000.00 USD | 45,450.00 USD | 35,310.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `254.40` | 4,680,000.00 USD | 4,680,000.00 USD | 8,310.00 USD | 13,680.00 USD | 3,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.40` | 8,630,000.00 USD | 8,630,000.00 USD | 19,460.00 USD | 25,910.00 USD | 60,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `254.50` | 548.45 USD | 21,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `254.80` | 4,660,000.00 USD | 4,660,000.00 USD | 2,210.00 USD | 3,080.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `254.80` | 8,530,000.00 USD | 8,530,000.00 USD | 50,650.00 USD | 29,470.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.20` | 4,650,000.00 USD | 4,650,000.00 USD | 16,750.00 USD | 17,380.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.20` | 8,410,000.00 USD | 8,410,000.00 USD | 23,880.00 USD | 13,020.00 USD | 25,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `255.60` | 4,610,000.00 USD | 4,610,000.00 USD | 17,490.00 USD | 30,230.00 USD | 20,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `255.60` | 8,350,000.00 USD | 8,350,000.00 USD | 33,430.00 USD | 16,640.00 USD | 31,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.00` | 4,540,000.00 USD | 4,540,000.00 USD | 10,010.00 USD | 11,660.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.00` | 8,260,000.00 USD | 8,260,000.00 USD | 18,300.00 USD | 10,360.00 USD | 25,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `256.40` | 4,500,000.00 USD | 4,500,000.00 USD | 7,460.00 USD | 31,910.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.40` | 8,210,000.00 USD | 8,210,000.00 USD | 29,190.00 USD | 739.13 USD | 23,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `256.50` | 3,210.00 USD | 20,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `256.80` | 4,440,000.00 USD | 4,440,000.00 USD | 1,760.00 USD | 5,950.00 USD | 14,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `256.80` | 8,160,000.00 USD | 8,160,000.00 USD | 32,310.00 USD | 13,750.00 USD | 56,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.20` | 4,420,000.00 USD | 4,420,000.00 USD | 14,160.00 USD | 1,040.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.20` | 8,050,000.00 USD | 8,050,000.00 USD | 15,600.00 USD | 3,420.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `257.60` | 4,400,000.00 USD | 4,400,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `257.60` | 8,020,000.00 USD | 8,020,000.00 USD | 34,480.00 USD | 4,400.00 USD | 10,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.00` | 4,380,000.00 USD | 4,380,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.00` | 7,980,000.00 USD | 7,980,000.00 USD | 26,960.00 USD | 4,790.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `258.40` | 4,320,000.00 USD | 4,320,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.40` | 7,940,000.00 USD | 7,940,000.00 USD | 128,170.00 USD | 37,820.00 USD | 92,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `258.50` | 645.99 USD | 17,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `258.80` | 4,260,000.00 USD | 4,260,000.00 USD | 8,320.00 USD | 30,390.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `258.80` | 7,680,000.00 USD | 7,680,000.00 USD | 59,230.00 USD | 2,500.00 USD | 34,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.20` | 4,190,000.00 USD | 4,190,000.00 USD | 14,560.00 USD | 12,990.00 USD | 17,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.20` | 7,580,000.00 USD | 7,580,000.00 USD | 5,210.00 USD | 45,200.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `259.60` | 4,140,000.00 USD | 4,140,000.00 USD | 13,590.00 USD | 4,640.00 USD | 22,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `259.60` | 7,520,000.00 USD | 7,520,000.00 USD | 20,030.00 USD | 8,340.00 USD | 16,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.00` | 4,100,000.00 USD | 4,100,000.00 USD | 45,280.00 USD | 32,840.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.00` | 7,480,000.00 USD | 7,480,000.00 USD | 103,390.00 USD | 63,410.00 USD | 106,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `260.40` | 4,000,000.00 USD | 4,000,000.00 USD | 19,610.00 USD | 7,660.00 USD | 16,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.40` | 7,200,000.00 USD | 7,200,000.00 USD | 4,590.00 USD | 3,590.00 USD | 74,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `260.50` | 2,040.00 USD | 16,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `260.80` | 3,960,000.00 USD | 3,960,000.00 USD | 1,360.00 USD | 46,690.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `260.80` | 7,120,000.00 USD | 7,120,000.00 USD | 14,600.00 USD | 56,470.00 USD | 37,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.20` | 3,880,000.00 USD | 3,880,000.00 USD | 8,180.00 USD | 23,140.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.20` | 7,010,000.00 USD | 7,010,000.00 USD | 6,110.00 USD | 90,180.00 USD | 15,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `261.60` | 3,820,000.00 USD | 3,820,000.00 USD | 18,900.00 USD | 55,190.00 USD | 53,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `261.60` | 6,900,000.00 USD | 6,900,000.00 USD | 24,520.00 USD | 84,260.00 USD | 48,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.00` | 3,690,000.00 USD | 3,690,000.00 USD | 17,910.00 USD | 44,250.00 USD | 21,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.00` | 6,740,000.00 USD | 6,740,000.00 USD | 61,230.00 USD | 39,230.00 USD | 81,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `262.40` | 3,610,000.00 USD | 3,610,000.00 USD | 21,110.00 USD | 6,200.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.40` | 6,560,000.00 USD | 6,560,000.00 USD | 28,440.00 USD | 55,580.00 USD | 0.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `262.50` | 1,310.00 USD | 14,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `262.80` | 3,570,000.00 USD | 3,570,000.00 USD | 747.53 USD | 13,310.00 USD | 19,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `262.80` | 6,480,000.00 USD | 6,480,000.00 USD | 73,660.00 USD | 45,060.00 USD | 32,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.20` | 3,540,000.00 USD | 3,540,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.20` | 6,330,000.00 USD | 6,330,000.00 USD | 21,560.00 USD | 13,710.00 USD | 152.95 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `263.60` | 3,460,000.00 USD | 3,460,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `263.60` | 6,290,000.00 USD | 6,290,000.00 USD | 278,330.00 USD | 1,880.00 USD | 83,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.00` | 3,360,000.00 USD | 3,360,000.00 USD | 52,440.00 USD | 15,650.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.00` | 5,930,000.00 USD | 5,930,000.00 USD | 135,390.00 USD | 629.16 USD | 34,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.40` | 3,270,000.00 USD | 3,270,000.00 USD | 6,130.00 USD | 20,120.00 USD | 21.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.40` | 5,760,000.00 USD | 5,760,000.00 USD | 44,740.00 USD | 21,810.00 USD | 44.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `264.80` | 3,250,000.00 USD | 3,250,000.00 USD | 22,660.00 USD | 1,370.00 USD | 20,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `264.80` | 5,690,000.00 USD | 5,690,000.00 USD | 26,950.00 USD | 1,900.00 USD | 198.07 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `265.20` | 3,200,000.00 USD | 3,200,000.00 USD | 75,930.00 USD | 3,410.00 USD | 33,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.20` | 5,660,000.00 USD | 5,660,000.00 USD | 106,380.00 USD | 1,640.00 USD | 33,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `265.50` | 531.00 USD | 13,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `265.60` | 3,090,000.00 USD | 3,090,000.00 USD | 415.98 USD | 788.61 USD | 12.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `265.60` | 5,520,000.00 USD | 5,520,000.00 USD | 199,660.00 USD | 694.90 USD | 151.46 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.00` | 3,090,000.00 USD | 3,090,000.00 USD | 12,120.00 USD | 209.24 USD | 5.24 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.00` | 5,320,000.00 USD | 5,320,000.00 USD | 140,360.00 USD | 645.20 USD | 25.50 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.40` | 3,080,000.00 USD | 3,080,000.00 USD | 4,400.00 USD | 13,530.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.40` | 5,180,000.00 USD | 5,180,000.00 USD | 106,830.00 USD | 804.70 USD | 10.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `266.80` | 3,050,000.00 USD | 3,050,000.00 USD | 22,750.00 USD | 30,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `266.80` | 5,070,000.00 USD | 5,070,000.00 USD | 125,320.00 USD | 63,260.00 USD | 28.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `267.20` | 3,000,000.00 USD | 3,000,000.00 USD | 43,580.00 USD | 34,990.00 USD | 12,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.20` | 4,880,000.00 USD | 4,880,000.00 USD | 101,740.00 USD | 26,850.00 USD | 23.69 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `267.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `267.60` | 2,910,000.00 USD | 2,910,000.00 USD | 10,330.00 USD | 72,630.00 USD | 23,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `267.60` | 4,750,000.00 USD | 4,750,000.00 USD | 75,350.00 USD | 61,270.00 USD | 38,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.00` | 2,800,000.00 USD | 2,800,000.00 USD | 19,060.00 USD | 4,020.00 USD | 51,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.00` | 4,580,000.00 USD | 4,580,000.00 USD | 234,660.00 USD | 25,100.00 USD | 388.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.40` | 2,730,000.00 USD | 2,730,000.00 USD | 18,310.00 USD | 43,230.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.40` | 4,320,000.00 USD | 4,320,000.00 USD | 136,830.00 USD | 124,980.00 USD | 95,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `268.80` | 2,650,000.00 USD | 2,650,000.00 USD | 21,330.00 USD | 11,530.00 USD | 146.66 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `268.80` | 3,960,000.00 USD | 3,960,000.00 USD | 23,340.00 USD | 18,320.00 USD | 105.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.20` | 2,620,000.00 USD | 2,620,000.00 USD | 10,990.00 USD | 2,660.00 USD | 8,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.20` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 2,470.00 USD | 70.45 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `269.60` | 2,600,000.00 USD | 2,600,000.00 USD | 6,520.00 USD | 19,180.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `269.60` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 2,540.00 USD | 200.97 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.00` | 2,560,000.00 USD | 2,560,000.00 USD | 7,960.00 USD | 11,930.00 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.00` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 1,310.00 USD | 146.37 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `270.40` | 2,540,000.00 USD | 2,540,000.00 USD | 54,750.00 USD | 1,930.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.40` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 166.02 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `270.50` | 13,090.00 USD | 13,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `270.80` | 2,480,000.00 USD | 2,480,000.00 USD | 3,100.00 USD | 15,660.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `270.80` | 3,910,000.00 USD | 3,910,000.00 USD | 33,050.00 USD | 0.00 USD | 84.79 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.20` | 2,460,000.00 USD | 2,460,000.00 USD | 12,890.00 USD | 6,410.00 USD | 12,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.20` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `271.60` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 8,940.00 USD | 13,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `271.60` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 7,250.00 USD | 61,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.00` | 2,400,000.00 USD | 2,400,000.00 USD | 28,410.00 USD | 52,240.00 USD | 9,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.00` | 3,790,000.00 USD | 3,790,000.00 USD | 61,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `272.40` | 2,310,000.00 USD | 2,310,000.00 USD | 10,530.00 USD | 33,560.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.40` | 3,730,000.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `272.50` | 214.19 USD | 3,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `272.80` | 2,210,000.00 USD | 2,210,000.00 USD | 62,230.00 USD | 9,400.00 USD | 59,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `272.80` | 3,700,000.00 USD | 3,700,000.00 USD | 25,660.00 USD | 69,990.00 USD | 89,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.20` | 2,080,000.00 USD | 2,080,000.00 USD | 30,300.00 USD | 115,960.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.20` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 79,710.00 USD | 173,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `273.60` | 1,890,000.00 USD | 1,890,000.00 USD | 42,760.00 USD | 18,430.00 USD | 53,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `273.60` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 66,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.00` | 1,770,000.00 USD | 1,770,000.00 USD | 159,390.00 USD | 97,110.00 USD | 39,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.00` | 3,190,000.00 USD | 3,190,000.00 USD | 466,260.00 USD | 0.00 USD | 94,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.40` | 1,480,000.00 USD | 1,480,000.00 USD | 155,650.00 USD | 21,440.00 USD | 41,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.40` | 2,630,000.00 USD | 2,630,000.00 USD | 413,010.00 USD | 34,960.00 USD | 83,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `274.80` | 1,260,000.00 USD | 1,260,000.00 USD | 70,330.00 USD | 22,510.00 USD | 29,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `274.80` | 2,100,000.00 USD | 2,100,000.00 USD | 334,980.00 USD | 0.00 USD | 34,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.20` | 1,140,000.00 USD | 1,140,000.00 USD | 11,720.00 USD | 3,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.20` | 1,730,000.00 USD | 1,730,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `275.60` | 1,120,000.00 USD | 1,120,000.00 USD | 35,420.00 USD | 15,980.00 USD | 26,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `275.60` | 1,650,000.00 USD | 1,650,000.00 USD | 1,350.00 USD | 0.00 USD | 48,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.00` | 1,040,000.00 USD | 1,040,000.00 USD | 143,900.00 USD | 18,930.00 USD | 40,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.00` | 1,600,000.00 USD | 1,600,000.00 USD | 3,140.00 USD | 23,010.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.40` | 839,480.00 USD | 839,480.00 USD | 40,580.00 USD | 16,150.00 USD | 18,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.40` | 1,540,000.00 USD | 1,540,000.00 USD | 217,250.00 USD | 0.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `276.80` | 764,080.00 USD | 764,080.00 USD | 11,880.00 USD | 25,410.00 USD | 25,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `276.80` | 1,220,000.00 USD | 1,220,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.20` | 701,620.00 USD | 701,620.00 USD | 25,720.00 USD | 17,880.00 USD | 26,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.20` | 1,200,000.00 USD | 1,200,000.00 USD | 28,580.00 USD | 42,210.00 USD | 163,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `277.60` | 631,480.00 USD | 631,480.00 USD | 26,620.00 USD | 21,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `277.60` | 968,400.00 USD | 968,400.00 USD | 123,610.00 USD | 193,330.00 USD | 18,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.00` | 583,780.00 USD | 583,780.00 USD | 21,070.00 USD | 54,860.00 USD | 103,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.00` | 633,190.00 USD | 633,190.00 USD | 0.00 USD | 1,830.00 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.40` | 403,890.00 USD | 403,890.00 USD | 57,720.00 USD | 108,840.00 USD | 59,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.40` | 571,510.00 USD | 571,510.00 USD | 76,060.00 USD | 35,270.00 USD | 179,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `278.80` | 177,950.00 USD | 177,950.00 USD | 55,370.00 USD | 10,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `278.80` | 281,150.00 USD | 281,150.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.20` | 111,750.00 USD | 111,750.00 USD | 0.00 USD | 0.00 USD | 23,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `279.20` | 262,090.00 USD | 262,090.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `279.60` | 88,340.00 USD | 88,340.00 USD | 0.00 USD | 0.00 USD | 47,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.00` | 40,890.00 USD | 40,890.00 USD | 0.00 USD | 0.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `280.80` | 9,550.00 USD | 9,550.00 USD | 0.00 USD | 0.00 USD | 12.68 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `280.80` | 259,430.00 USD | 259,430.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.20` | 243,880.00 USD | 243,880.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `281.60` | 150,060.00 USD | 150,060.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.00` | 27,670.00 USD | 27,670.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `282.40` | 9,540.00 USD | 9,540.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `282.40` | 6,970.00 USD | 6,970.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `283.20` | 1,280.00 USD | 1,280.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `283.20` | 3,450.00 USD | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `283.50` | 306.46 USD | 3,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `284.00` | 2,000.00 USD | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.40` | 3,560.00 USD | 3,560.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `284.80` | 36,350.00 USD | 36,350.00 USD | 28,720.00 USD | 7,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `284.80` | 58,950.00 USD | 58,950.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.20` | 130,970.00 USD | 130,970.00 USD | 36,620.00 USD | 16,320.00 USD | 41,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.20` | 458,290.00 USD | 458,290.00 USD | 126,910.00 USD | 206,630.00 USD | 65,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `285.60` | 179,980.00 USD | 179,980.00 USD | 27,570.00 USD | 21,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `285.60` | 660,380.00 USD | 660,380.00 USD | 50,130.00 USD | 151,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.00` | 251,920.00 USD | 251,920.00 USD | 29,220.00 USD | 2,980.00 USD | 39,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.00` | 716,810.00 USD | 716,810.00 USD | 1,200.00 USD | 55,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.40` | 273,880.00 USD | 273,880.00 USD | 17,340.00 USD | 4,610.00 USD | 4.24 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.40` | 854,250.00 USD | 854,250.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `286.80` | 380,790.00 USD | 380,790.00 USD | 18,110.00 USD | 10,660.00 USD | 78,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `286.80` | 1,010,000.00 USD | 1,010,000.00 USD | 30,110.00 USD | 122,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `287.20` | 579,910.00 USD | 579,910.00 USD | 112,240.00 USD | 47,050.00 USD | 39,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.20` | 1,210,000.00 USD | 1,210,000.00 USD | 82,910.00 USD | 116,440.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `287.50` | 112.12 USD | 3,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `287.60` | 735,000.00 USD | 735,000.00 USD | 47,390.00 USD | 41,050.00 USD | 66,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `287.60` | 1,360,000.00 USD | 1,360,000.00 USD | 70,340.00 USD | 33,740.00 USD | 53,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.00` | 834,840.00 USD | 834,840.00 USD | 9,440.00 USD | 26,480.00 USD | 63,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.00` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 272,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.40` | 954,540.00 USD | 954,540.00 USD | 68,380.00 USD | 22,110.00 USD | 29,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.40` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 1,550.00 USD | 41,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `288.80` | 1,040,000.00 USD | 1,040,000.00 USD | 43,690.00 USD | 32,420.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `288.80` | 1,940,000.00 USD | 1,940,000.00 USD | 124,780.00 USD | 15,650.00 USD | 122,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.20` | 1,130,000.00 USD | 1,130,000.00 USD | 6,160.00 USD | 52,920.00 USD | 30,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.20` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `289.60` | 1,340,000.00 USD | 1,340,000.00 USD | 25,200.00 USD | 62,860.00 USD | 121,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `289.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 62,370.00 USD | 95,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.00` | 1,610,000.00 USD | 1,610,000.00 USD | 115,670.00 USD | 54,130.00 USD | 106,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.00` | 2,370,000.00 USD | 2,370,000.00 USD | 53,890.00 USD | 38,660.00 USD | 122,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.40` | 1,810,000.00 USD | 1,810,000.00 USD | 36,130.00 USD | 107,960.00 USD | 49,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.40` | 2,430,000.00 USD | 2,430,000.00 USD | 33,530.00 USD | 19,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `290.80` | 1,990,000.00 USD | 1,990,000.00 USD | 56,480.00 USD | 71,550.00 USD | 54,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `290.80` | 2,550,000.00 USD | 2,550,000.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `291.20` | 2,050,000.00 USD | 2,050,000.00 USD | 28,320.00 USD | 12,060.00 USD | 24,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.20` | 2,590,000.00 USD | 2,590,000.00 USD | 24,680.00 USD | 18,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `291.50` | 954.95 USD | 4,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `291.60` | 2,100,000.00 USD | 2,100,000.00 USD | 12,550.00 USD | 6,560.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `291.60` | 2,700,000.00 USD | 2,700,000.00 USD | 2,710.00 USD | 85,290.00 USD | 19,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.00` | 2,140,000.00 USD | 2,140,000.00 USD | 7,010.00 USD | 30,490.00 USD | 31.89 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.00` | 2,850,000.00 USD | 2,850,000.00 USD | 2,560.00 USD | 149,160.00 USD | 9.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `292.40` | 2,200,000.00 USD | 2,200,000.00 USD | 29,860.00 USD | 14,820.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.40` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 25,520.00 USD | 40.84 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `292.50` | 6,050.00 USD | 10,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `292.80` | 2,260,000.00 USD | 2,260,000.00 USD | 29,430.00 USD | 27,590.00 USD | 3,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `292.80` | 2,980,000.00 USD | 2,980,000.00 USD | 887.27 USD | 101,280.00 USD | 131.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.20` | 2,360,000.00 USD | 2,360,000.00 USD | 50,900.00 USD | 20,980.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.20` | 3,150,000.00 USD | 3,150,000.00 USD | 33,580.00 USD | 132,080.00 USD | 88.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `293.60` | 2,510,000.00 USD | 2,510,000.00 USD | 77,380.00 USD | 48,560.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `293.60` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 1,860.00 USD | 113.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.00` | 2,640,000.00 USD | 2,640,000.00 USD | 30,750.00 USD | 23,790.00 USD | 70,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.00` | 3,330,000.00 USD | 3,330,000.00 USD | 54,350.00 USD | 34,230.00 USD | 95,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.40` | 2,880,000.00 USD | 2,880,000.00 USD | 64,400.00 USD | 64,490.00 USD | 116,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.40` | 3,640,000.00 USD | 3,640,000.00 USD | 201,580.00 USD | 9,460.00 USD | 92,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `294.80` | 3,020,000.00 USD | 3,020,000.00 USD | 59,910.00 USD | 35,750.00 USD | 44,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `294.80` | 3,900,000.00 USD | 3,900,000.00 USD | 63,770.00 USD | 108,720.00 USD | 89,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.20` | 3,160,000.00 USD | 3,160,000.00 USD | 8,650.00 USD | 27,140.00 USD | 99,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.20` | 4,180,000.00 USD | 4,180,000.00 USD | 733.30 USD | 64,810.00 USD | 214,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `295.60` | 3,400,000.00 USD | 3,400,000.00 USD | 73,320.00 USD | 42,660.00 USD | 123,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `295.60` | 4,750,000.00 USD | 4,750,000.00 USD | 176,660.00 USD | 91,360.00 USD | 306,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.00` | 3,610,000.00 USD | 3,610,000.00 USD | 54,390.00 USD | 112,840.00 USD | 43,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.00` | 5,010,000.00 USD | 5,010,000.00 USD | 76,740.00 USD | 99,260.00 USD | 86,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.40` | 3,750,000.00 USD | 3,750,000.00 USD | 80,090.00 USD | 31,130.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.40` | 5,160,000.00 USD | 5,160,000.00 USD | 1,550.00 USD | 78,210.00 USD | 68,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `296.80` | 3,880,000.00 USD | 3,880,000.00 USD | 24,560.00 USD | 32,150.00 USD | 74,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `296.80` | 5,500,000.00 USD | 5,500,000.00 USD | 133,480.00 USD | 4,410.00 USD | 201,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.20` | 3,990,000.00 USD | 3,990,000.00 USD | 56,450.00 USD | 1,160.00 USD | 50,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.20` | 5,630,000.00 USD | 5,630,000.00 USD | 77,480.00 USD | 51,810.00 USD | 72.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `297.60` | 4,030,000.00 USD | 4,030,000.00 USD | 7,640.00 USD | 11,600.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `297.60` | 5,730,000.00 USD | 5,730,000.00 USD | 1,640.00 USD | 62,110.00 USD | 34,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.00` | 4,150,000.00 USD | 4,150,000.00 USD | 63,620.00 USD | 9,490.00 USD | 41,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.00` | 5,900,000.00 USD | 5,900,000.00 USD | 47,790.00 USD | 43,980.00 USD | 75,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.40` | 4,220,000.00 USD | 4,220,000.00 USD | 7,430.00 USD | 2,180.00 USD | 56,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.40` | 6,020,000.00 USD | 6,020,000.00 USD | 32,250.00 USD | 42,940.00 USD | 48,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `298.80` | 4,330,000.00 USD | 4,330,000.00 USD | 23,700.00 USD | 457.80 USD | 94,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `298.80` | 6,100,000.00 USD | 6,100,000.00 USD | 69,820.00 USD | 12,530.00 USD | 83.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.20` | 4,370,000.00 USD | 4,370,000.00 USD | 8,500.00 USD | 15,770.00 USD | 12,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.20` | 6,210,000.00 USD | 6,210,000.00 USD | 2,350.00 USD | 15,140.00 USD | 85,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `299.60` | 4,430,000.00 USD | 4,430,000.00 USD | 35,920.00 USD | 5,850.00 USD | 21,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `299.60` | 6,240,000.00 USD | 6,240,000.00 USD | 4,590.00 USD | 13,830.00 USD | 19,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.00` | 4,480,000.00 USD | 4,480,000.00 USD | 3,760.00 USD | 14,300.00 USD | 27,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.00` | 6,310,000.00 USD | 6,310,000.00 USD | 53,130.00 USD | 10,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `300.40` | 4,600,000.00 USD | 4,600,000.00 USD | 41,880.00 USD | 31,010.00 USD | 42,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.40` | 6,310,000.00 USD | 6,310,000.00 USD | 2,070.00 USD | 645.96 USD | 58.05 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `300.50` | 991.05 USD | 11,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `300.80` | 4,610,000.00 USD | 4,610,000.00 USD | 790.57 USD | 924.19 USD | 17,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `300.80` | 6,450,000.00 USD | 6,450,000.00 USD | 24,730.00 USD | 71,120.00 USD | 48,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.20` | 4,660,000.00 USD | 4,660,000.00 USD | 348.65 USD | 15,610.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.20` | 6,640,000.00 USD | 6,640,000.00 USD | 48,570.00 USD | 42,080.00 USD | 91,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `301.60` | 4,720,000.00 USD | 4,720,000.00 USD | 19,530.00 USD | 8,470.00 USD | 34,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `301.60` | 6,840,000.00 USD | 6,840,000.00 USD | 62,390.00 USD | 79,410.00 USD | 59,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.00` | 4,790,000.00 USD | 4,790,000.00 USD | 25,220.00 USD | 28,210.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.00` | 7,070,000.00 USD | 7,070,000.00 USD | 52,640.00 USD | 150,800.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.40` | 4,820,000.00 USD | 4,820,000.00 USD | 11,420.00 USD | 5,080.00 USD | 17,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.40` | 7,170,000.00 USD | 7,170,000.00 USD | 580.96 USD | 99,780.00 USD | 2.17 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `302.80` | 4,870,000.00 USD | 4,870,000.00 USD | 4,420.00 USD | 12,990.00 USD | 34,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `302.80` | 7,390,000.00 USD | 7,390,000.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.20` | 4,910,000.00 USD | 4,910,000.00 USD | 21,180.00 USD | 1,310.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.20` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 1,780.00 USD | 177.41 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `303.60` | 4,910,000.00 USD | 4,910,000.00 USD | 228.18 USD | 2,000.00 USD | 1.44 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `303.60` | 7,420,000.00 USD | 7,420,000.00 USD | 2,130.00 USD | 693.54 USD | 24,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.00` | 4,950,000.00 USD | 4,950,000.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.00` | 7,480,000.00 USD | 7,480,000.00 USD | 20,680.00 USD | 14,630.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.40` | 5,010,000.00 USD | 5,010,000.00 USD | 9,670.00 USD | 2,470.00 USD | 49,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.40` | 7,490,000.00 USD | 7,490,000.00 USD | 1,340.00 USD | 11,280.00 USD | 82.73 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `304.80` | 5,040,000.00 USD | 5,040,000.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `304.80` | 7,530,000.00 USD | 7,530,000.00 USD | 34,540.00 USD | 682.27 USD | 4,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.20` | 5,050,000.00 USD | 5,050,000.00 USD | 47.98 USD | 5,330.00 USD | 2,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.20` | 7,860,000.00 USD | 7,860,000.00 USD | 113,060.00 USD | 128,470.00 USD | 89,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `305.60` | 5,050,000.00 USD | 5,050,000.00 USD | 3,060.00 USD | 440.72 USD | 12.59 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `305.60` | 8,000,000.00 USD | 8,000,000.00 USD | 76,400.00 USD | 21,950.00 USD | 41,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.00` | 5,080,000.00 USD | 5,080,000.00 USD | 7,500.00 USD | 5,780.00 USD | 12,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.00` | 8,160,000.00 USD | 8,160,000.00 USD | 60,790.00 USD | 50,650.00 USD | 44,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.40` | 5,090,000.00 USD | 5,090,000.00 USD | 7,310.00 USD | 183.24 USD | 5,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.40` | 8,280,000.00 USD | 8,280,000.00 USD | 35,090.00 USD | 65,940.00 USD | 25,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `306.80` | 5,160,000.00 USD | 5,160,000.00 USD | 19,990.00 USD | 35,330.00 USD | 11,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `306.80` | 8,500,000.00 USD | 8,500,000.00 USD | 84,850.00 USD | 66,200.00 USD | 66,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.20` | 5,220,000.00 USD | 5,220,000.00 USD | 11,270.00 USD | 19,960.00 USD | 29,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.20` | 8,710,000.00 USD | 8,710,000.00 USD | 11,730.00 USD | 87,980.00 USD | 106,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `307.60` | 5,270,000.00 USD | 5,270,000.00 USD | 22,580.00 USD | 27,240.00 USD | 5.95 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `307.60` | 8,970,000.00 USD | 8,970,000.00 USD | 78,600.00 USD | 122,070.00 USD | 56,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.00` | 5,310,000.00 USD | 5,310,000.00 USD | 16,340.00 USD | 10,700.00 USD | 16,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.00` | 9,220,000.00 USD | 9,220,000.00 USD | 125,470.00 USD | 70,950.00 USD | 60,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.40` | 5,320,000.00 USD | 5,320,000.00 USD | 3,150.00 USD | 212.94 USD | 2,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.40` | 9,510,000.00 USD | 9,510,000.00 USD | 131,420.00 USD | 45,250.00 USD | 114,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `308.80` | 5,330,000.00 USD | 5,330,000.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `308.80` | 9,630,000.00 USD | 9,630,000.00 USD | 54,880.00 USD | 42,230.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.20` | 5,330,000.00 USD | 5,330,000.00 USD | 2,990.00 USD | 1,190.00 USD | 2,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.20` | 9,720,000.00 USD | 9,720,000.00 USD | 33,440.00 USD | 19,290.00 USD | 32,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `309.60` | 5,350,000.00 USD | 5,350,000.00 USD | 8,250.00 USD | 8,710.00 USD | 1,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `309.60` | 10,000,000.00 USD | 10,000,000.00 USD | 41,230.00 USD | 107,950.00 USD | 131,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.00` | 5,380,000.00 USD | 5,380,000.00 USD | 16,880.00 USD | 3,310.00 USD | 7,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.00` | 10,200,000.00 USD | 10,200,000.00 USD | 20,240.00 USD | 98,540.00 USD | 82,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.40` | 5,400,000.00 USD | 5,400,000.00 USD | 176.40 USD | 5,960.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.40` | 10,390,000.00 USD | 10,390,000.00 USD | 91,290.00 USD | 74,340.00 USD | 21,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `310.80` | 5,410,000.00 USD | 5,410,000.00 USD | 5,080.00 USD | 2,080.00 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `310.80` | 10,460,000.00 USD | 10,460,000.00 USD | 29,950.00 USD | 35,930.00 USD | 12,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.20` | 5,410,000.00 USD | 5,410,000.00 USD | 257.90 USD | 3,180.00 USD | 1,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.20` | 10,680,000.00 USD | 10,680,000.00 USD | 74,340.00 USD | 65,480.00 USD | 72,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `311.60` | 5,430,000.00 USD | 5,430,000.00 USD | 7,100.00 USD | 10,150.00 USD | 14.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `311.60` | 10,730,000.00 USD | 10,730,000.00 USD | 40,900.00 USD | 10,550.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.00` | 5,440,000.00 USD | 5,440,000.00 USD | 1,190.00 USD | 4,490.00 USD | 4,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.00` | 10,800,000.00 USD | 10,800,000.00 USD | 40,590.00 USD | 2,020.00 USD | 28,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.40` | 5,490,000.00 USD | 5,490,000.00 USD | 17,490.00 USD | 14,240.00 USD | 20,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.40` | 10,890,000.00 USD | 10,890,000.00 USD | 28,530.00 USD | 22,960.00 USD | 31,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `312.80` | 5,520,000.00 USD | 5,520,000.00 USD | 9,120.00 USD | 2,880.00 USD | 15,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `312.80` | 10,910,000.00 USD | 10,910,000.00 USD | 15,280.00 USD | 2,460.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.20` | 5,540,000.00 USD | 5,540,000.00 USD | 40.35 USD | 15,380.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.20` | 10,990,000.00 USD | 10,990,000.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `313.60` | 5,560,000.00 USD | 5,560,000.00 USD | 8,130.00 USD | 7,190.00 USD | 8,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `313.60` | 11,030,000.00 USD | 11,030,000.00 USD | 10,400.00 USD | 755.05 USD | 34,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.00` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.00` | 11,080,000.00 USD | 11,080,000.00 USD | 22,920.00 USD | 815.59 USD | 20,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `314.10` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.40` | 11,150,000.00 USD | 11,150,000.00 USD | 51,980.00 USD | 307.60 USD | 24,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `314.80` | 11,180,000.00 USD | 11,180,000.00 USD | 17,720.00 USD | 0.00 USD | 10,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.20` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 258.00 USD | 3.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `315.60` | 11,240,000.00 USD | 11,240,000.00 USD | 1,070.00 USD | 28,580.00 USD | 30,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.00` | 11,290,000.00 USD | 11,290,000.00 USD | 38,990.00 USD | 5,120.00 USD | 75.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.40` | 11,400,000.00 USD | 11,400,000.00 USD | 16,580.00 USD | 40,060.00 USD | 61,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `316.80` | 11,410,000.00 USD | 11,410,000.00 USD | 1,990.00 USD | 667.80 USD | 30.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.20` | 11,420,000.00 USD | 11,420,000.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.60` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 265.17 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `317.80` | 11,440,000.00 USD | 11,440,000.00 USD | 20,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `70.50` | 212,160.00 USD | 0.00 USD | 2,890.00 USD | `-74.82%` | `41,012,000,000.00` |
| `Live` | `Long` | `77.50` | 209,270.00 USD | 0.00 USD | 556.06 USD | `-72.32%` | `7,175,000,000.00` |
| `Live` | `Long` | `89.50` | 208,720.00 USD | 0.00 USD | 1,170.00 USD | `-68.04%` | `13,105,000,000.00` |
| `Live` | `Long` | `95.50` | 207,540.00 USD | 0.00 USD | 920.05 USD | `-65.90%` | `9,634,000,000.00` |
| `Live` | `Long` | `101.50` | 206,620.00 USD | 0.00 USD | 6,240.00 USD | `-63.75%` | `61,439,000,000.00` |
| `Live` | `Long` | `102.50` | 200,390.00 USD | 0.00 USD | 4,080.00 USD | `-63.40%` | `39,797,000,000.00` |
| `Live` | `Long` | `105.50` | 196,310.00 USD | 0.00 USD | 398.79 USD | `-62.33%` | `3,780,000,000.00` |
| `Live` | `Long` | `108.50` | 195,910.00 USD | 0.00 USD | 108.50 USD | `-61.25%` | `1,000,000,000.00` |
| `Live` | `Long` | `109.50` | 195,800.00 USD | 0.00 USD | 212.76 USD | `-60.90%` | `1,943,000,000.00` |
| `Live` | `Long` | `111.50` | 195,590.00 USD | 0.00 USD | 174.94 USD | `-60.18%` | `1,569,000,000.00` |
| `Live` | `Long` | `118.50` | 195,410.00 USD | 0.00 USD | 212.35 USD | `-57.68%` | `1,792,000,000.00` |
| `Live` | `Long` | `122.50` | 195,200.00 USD | 0.00 USD | 124.46 USD | `-56.25%` | `1,016,000,000.00` |
| `Live` | `Long` | `126.50` | 195,080.00 USD | 0.00 USD | 658.18 USD | `-54.83%` | `5,203,000,000.00` |
| `Live` | `Long` | `128.50` | 194,420.00 USD | 0.00 USD | 2,060.00 USD | `-54.11%` | `16,000,000,000.00` |
| `Live` | `Long` | `138.50` | 192,360.00 USD | 0.00 USD | 3,460.00 USD | `-50.54%` | `25,000,000,000.00` |
| `Live` | `Long` | `147.50` | 188,900.00 USD | 0.00 USD | 895.47 USD | `-47.33%` | `6,071,000,000.00` |
| `Live` | `Long` | `148.50` | 188,000.00 USD | 0.00 USD | 1,270.00 USD | `-46.97%` | `8,528,000,000.00` |
| `Live` | `Long` | `149.50` | 186,740.00 USD | 0.00 USD | 2,370.00 USD | `-46.61%` | `15,823,000,000.00` |
| `Live` | `Long` | `152.50` | 184,370.00 USD | 0.00 USD | 303.78 USD | `-45.54%` | `1,992,000,000.00` |
| `Live` | `Long` | `162.50` | 184,070.00 USD | 0.00 USD | 1,880.00 USD | `-41.97%` | `11,599,000,000.00` |
| `Live` | `Long` | `167.50` | 182,180.00 USD | 0.00 USD | 285.75 USD | `-40.18%` | `1,706,000,000.00` |
| `Live` | `Long` | `168.50` | 181,900.00 USD | 0.00 USD | 8,430.00 USD | `-39.83%` | `50,000,000,000.00` |
| `Live` | `Long` | `169.50` | 173,470.00 USD | 0.00 USD | 1,280.00 USD | `-39.47%` | `7,572,000,000.00` |
| `Live` | `Long` | `170.50` | 172,190.00 USD | 0.00 USD | 426.25 USD | `-39.11%` | `2,500,000,000.00` |
| `Live` | `Long` | `174.50` | 171,760.00 USD | 0.00 USD | 169.96 USD | `-37.69%` | `974,000,000.00` |
| `Live` | `Long` | `175.50` | 171,590.00 USD | 0.00 USD | 516.67 USD | `-37.33%` | `2,944,000,000.00` |
| `Live` | `Long` | `176.50` | 171,080.00 USD | 0.00 USD | 373.83 USD | `-36.97%` | `2,118,000,000.00` |
| `Live` | `Long` | `184.50` | 170,700.00 USD | 0.00 USD | 808.66 USD | `-34.11%` | `4,383,000,000.00` |
| `Live` | `Long` | `188.50` | 169,890.00 USD | 0.00 USD | 418.28 USD | `-32.69%` | `2,219,000,000.00` |
| `Live` | `Long` | `190.50` | 169,480.00 USD | 0.00 USD | 694.75 USD | `-31.97%` | `3,647,000,000.00` |
| `Live` | `Long` | `191.50` | 168,780.00 USD | 0.00 USD | 858.49 USD | `-31.61%` | `4,483,000,000.00` |
| `Live` | `Long` | `192.50` | 167,920.00 USD | 0.00 USD | 1,490.00 USD | `-31.26%` | `7,715,000,000.00` |
| `Live` | `Long` | `195.50` | 166,440.00 USD | 0.00 USD | 370.47 USD | `-30.19%` | `1,895,000,000.00` |
| `Live` | `Long` | `196.50` | 166,070.00 USD | 0.00 USD | 210.65 USD | `-29.83%` | `1,072,000,000.00` |
| `Live` | `Long` | `199.50` | 165,860.00 USD | 0.00 USD | 548.03 USD | `-28.76%` | `2,747,000,000.00` |
| `Live` | `Long` | `200.50` | 165,310.00 USD | 0.00 USD | 293.13 USD | `-28.40%` | `1,462,000,000.00` |
| `Live` | `Long` | `202.50` | 165,020.00 USD | 0.00 USD | 420.39 USD | `-27.69%` | `2,076,000,000.00` |
| `Live` | `Long` | `205.50` | 164,600.00 USD | 0.00 USD | 191.53 USD | `-26.62%` | `932,000,000.00` |
| `Live` | `Long` | `206.50` | 164,400.00 USD | 0.00 USD | 41,790.00 USD | `-26.26%` | `202,387,000,000.00` |
| `Live` | `Long` | `210.50` | 122,610.00 USD | 0.00 USD | 108.83 USD | `-24.83%` | `517,000,000.00` |
| `Live` | `Long` | `213.50` | 122,500.00 USD | 0.00 USD | 3,800.00 USD | `-23.76%` | `17,817,000,000.00` |
| `Live` | `Long` | `214.50` | 118,700.00 USD | 0.00 USD | 643.50 USD | `-23.40%` | `3,000,000,000.00` |
| `Live` | `Long` | `215.50` | 118,050.00 USD | 0.00 USD | 239.85 USD | `-23.04%` | `1,113,000,000.00` |
| `Live` | `Long` | `223.50` | 117,810.00 USD | 0.00 USD | 31,290.00 USD | `-20.19%` | `140,000,000,000.00` |
| `Live` | `Long` | `224.50` | 86,520.00 USD | 0.00 USD | 12,900.00 USD | `-19.83%` | `57,451,000,000.00` |
| `Live` | `Long` | `226.50` | 73,630.00 USD | 0.00 USD | 1,240.00 USD | `-19.12%` | `5,455,000,000.00` |
| `Live` | `Long` | `227.50` | 72,390.00 USD | 0.00 USD | 174.49 USD | `-18.76%` | `767,000,000.00` |
| `Live` | `Long` | `228.50` | 72,220.00 USD | 0.00 USD | 642.77 USD | `-18.40%` | `2,813,000,000.00` |
| `Live` | `Long` | `229.50` | 71,570.00 USD | 0.00 USD | 114.75 USD | `-18.04%` | `500,000,000.00` |
| `Live` | `Long` | `230.50` | 71,460.00 USD | 0.00 USD | 1,190.00 USD | `-17.69%` | `5,171,000,000.00` |
| `Live` | `Long` | `231.50` | 70,270.00 USD | 0.00 USD | 295.86 USD | `-17.33%` | `1,278,000,000.00` |
| `Live` | `Long` | `234.50` | 69,970.00 USD | 0.00 USD | 637.61 USD | `-16.26%` | `2,719,000,000.00` |
| `Live` | `Long` | `237.50` | 69,330.00 USD | 0.00 USD | 23,750.00 USD | `-15.19%` | `100,000,000,000.00` |
| `Live` | `Long` | `238.50` | 45,580.00 USD | 0.00 USD | 3,790.00 USD | `-14.83%` | `15,877,000,000.00` |
| `Live` | `Long` | `239.50` | 41,800.00 USD | 0.00 USD | 1,030.00 USD | `-14.47%` | `4,281,000,000.00` |
| `Live` | `Long` | `241.50` | 40,770.00 USD | 0.00 USD | 251.88 USD | `-13.76%` | `1,043,000,000.00` |
| `Live` | `Long` | `242.50` | 40,520.00 USD | 0.00 USD | 7,180.00 USD | `-13.40%` | `29,590,000,000.00` |
| `Live` | `Long` | `243.50` | 33,340.00 USD | 0.00 USD | 1,850.00 USD | `-13.05%` | `7,591,000,000.00` |
| `Live` | `Long` | `244.50` | 31,500.00 USD | 0.00 USD | 5,760.00 USD | `-12.69%` | `23,551,000,000.00` |
| `Live` | `Long` | `245.50` | 25,740.00 USD | 0.00 USD | 1,030.00 USD | `-12.33%` | `4,182,000,000.00` |
| `Live` | `Long` | `247.50` | 24,710.00 USD | 0.00 USD | 106.67 USD | `-11.62%` | `431,000,000.00` |
| `Live` | `Long` | `248.50` | 24,600.00 USD | 0.00 USD | 595.16 USD | `-11.26%` | `2,395,000,000.00` |
| `Live` | `Long` | `250.50` | 24,010.00 USD | 0.00 USD | 1,330.00 USD | `-10.55%` | `5,292,000,000.00` |
| `Live` | `Long` | `251.50` | 22,680.00 USD | 0.00 USD | 268.35 USD | `-10.19%` | `1,067,000,000.00` |
| `Live` | `Long` | `252.50` | 22,420.00 USD | 0.00 USD | 1,030.00 USD | `-9.83%` | `4,088,000,000.00` |
| `Live` | `Long` | `254.50` | 21,380.00 USD | 0.00 USD | 548.45 USD | `-9.12%` | `2,155,000,000.00` |
| `Live` | `Long` | `256.50` | 20,830.00 USD | 0.00 USD | 3,210.00 USD | `-8.40%` | `12,514,000,000.00` |
| `Live` | `Long` | `258.50` | 17,620.00 USD | 0.00 USD | 645.99 USD | `-7.69%` | `2,499,000,000.00` |
| `Live` | `Long` | `260.50` | 16,980.00 USD | 0.00 USD | 2,040.00 USD | `-6.97%` | `7,839,000,000.00` |
| `Live` | `Long` | `262.50` | 14,940.00 USD | 0.00 USD | 1,310.00 USD | `-6.26%` | `5,000,000,000.00` |
| `Live` | `Long` | `265.50` | 13,620.00 USD | 0.00 USD | 531.00 USD | `-5.19%` | `2,000,000,000.00` |
| `Live` | `Short` | `267.50` | 2,920.00 USD | 2,920.00 USD | 0.00 USD | `-4.47%` | `10,931,000,000.00` |
| `Live` | `Long` | `270.50` | 13,090.00 USD | 0.00 USD | 13,090.00 USD | `-3.40%` | `48,404,000,000.00` |
| `Live` | `Short` | `272.50` | 3,140.00 USD | 214.19 USD | 0.00 USD | `-2.69%` | `786,000,000.00` |
| `Live` | `Short` | `283.50` | 3,440.00 USD | 306.46 USD | 0.00 USD | `+1.24%` | `1,081,000,000.00` |
| `Live` | `Short` | `287.50` | 3,560.00 USD | 112.12 USD | 0.00 USD | `+2.67%` | `390,000,000.00` |
| `Live` | `Short` | `291.50` | 4,510.00 USD | 954.95 USD | 0.00 USD | `+4.10%` | `3,276,000,000.00` |
| `Live` | `Short` | `292.50` | 10,560.00 USD | 6,050.00 USD | 0.00 USD | `+4.45%` | `20,668,000,000.00` |
| `Live` | `Short` | `300.50` | 11,550.00 USD | 991.05 USD | 0.00 USD | `+7.31%` | `3,298,000,000.00` |
| `Live` | `Short` | `320.50` | 12,650.00 USD | 1,110.00 USD | 0.00 USD | `+14.45%` | `3,452,000,000.00` |
| `Live` | `Short` | `324.50` | 14,880.00 USD | 2,220.00 USD | 0.00 USD | `+15.88%` | `6,855,000,000.00` |
| `Live` | `Short` | `326.50` | 40,410.00 USD | 25,530.00 USD | 0.00 USD | `+16.59%` | `78,189,000,000.00` |
| `Live` | `Short` | `342.50` | 41,780.00 USD | 1,370.00 USD | 0.00 USD | `+22.31%` | `4,000,000,000.00` |
| `Live` | `Short` | `358.50` | 42,790.00 USD | 1,010.00 USD | 0.00 USD | `+28.02%` | `2,812,000,000.00` |
| `Live` | `Short` | `368.50` | 43,230.00 USD | 445.52 USD | 0.00 USD | `+31.59%` | `1,209,000,000.00` |
| `Live` | `Short` | `373.50` | 84,320.00 USD | 41,090.00 USD | 0.00 USD | `+33.38%` | `110,000,000,000.00` |
| `Live` | `Short` | `406.50` | 94,960.00 USD | 10,640.00 USD | 0.00 USD | `+45.16%` | `26,172,000,000.00` |
| `Live` | `Short` | `459.50` | 141,210.00 USD | 46,250.00 USD | 0.00 USD | `+64.09%` | `100,662,000,000.00` |
| `Live` | `Short` | `498.50` | 141,930.00 USD | 718.34 USD | 0.00 USD | `+78.02%` | `1,441,000,000.00` |
| `Live` | `Short` | `552.50` | 142,120.00 USD | 195.03 USD | 0.00 USD | `+97.30%` | `353,000,000.00` |
| `Live` | `Short` | `560.50` | 142,970.00 USD | 842.43 USD | 0.00 USD | `+100.16%` | `1,503,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `143.50` | 452,640.00 USD | 0.00 USD | 210.94 USD | `-48.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `145.50` | 452,430.00 USD | 0.00 USD | 2,070.00 USD | `-48.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `165.50` | 450,360.00 USD | 0.00 USD | 489.38 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `178.50` | 449,870.00 USD | 0.00 USD | 2,530.00 USD | `-36.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `184.50` | 447,350.00 USD | 0.00 USD | 490.59 USD | `-34.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `196.50` | 446,850.00 USD | 0.00 USD | 482.01 USD | `-29.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `200.50` | 446,370.00 USD | 0.00 USD | 189.07 USD | `-28.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `208.50` | 446,180.00 USD | 0.00 USD | 441.60 USD | `-25.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `210.50` | 445,740.00 USD | 0.00 USD | 299.96 USD | `-24.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `211.50` | 445,440.00 USD | 0.00 USD | 715.29 USD | `-24.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `221.50` | 444,730.00 USD | 0.00 USD | 638.36 USD | `-20.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `224.50` | 444,090.00 USD | 0.00 USD | 740.85 USD | `-19.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `228.50` | 443,350.00 USD | 0.00 USD | 478.48 USD | `-18.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `233.50` | 442,870.00 USD | 0.00 USD | 389.48 USD | `-16.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `236.50` | 442,480.00 USD | 0.00 USD | 812.38 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `237.50` | 441,670.00 USD | 0.00 USD | 220.64 USD | `-15.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `238.50` | 441,450.00 USD | 0.00 USD | 429.30 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `239.50` | 441,020.00 USD | 0.00 USD | 296.50 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `240.50` | 440,720.00 USD | 0.00 USD | 216.45 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `242.50` | 440,500.00 USD | 0.00 USD | 387.76 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `244.50` | 440,120.00 USD | 0.00 USD | 18,080.00 USD | `-12.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `246.50` | 422,030.00 USD | 0.00 USD | 1,630.00 USD | `-11.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `247.50` | 420,410.00 USD | 0.00 USD | 2,700.00 USD | `-11.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `249.50` | 417,710.00 USD | 0.00 USD | 2,940.00 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `250.50` | 414,760.00 USD | 0.00 USD | 4,560.00 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `251.50` | 410,210.00 USD | 0.00 USD | 1,850.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `252.50` | 408,360.00 USD | 0.00 USD | 231.54 USD | `-9.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `253.50` | 408,130.00 USD | 0.00 USD | 109.26 USD | `-9.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `255.50` | 408,020.00 USD | 0.00 USD | 1,780.00 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `256.50` | 406,240.00 USD | 0.00 USD | 51,300.00 USD | `-8.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `257.50` | 354,940.00 USD | 0.00 USD | 250.81 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `260.50` | 354,690.00 USD | 0.00 USD | 2,370.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `261.50` | 352,320.00 USD | 0.00 USD | 269,800.00 USD | `-6.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `263.50` | 82,520.00 USD | 0.00 USD | 3,600.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `264.50` | 78,920.00 USD | 0.00 USD | 199.17 USD | `-5.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `265.50` | 78,720.00 USD | 0.00 USD | 2,180.00 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `266.50` | 76,550.00 USD | 0.00 USD | 241.98 USD | `-4.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `267.50` | 76,310.00 USD | 0.00 USD | 219.35 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `268.50` | 76,090.00 USD | 0.00 USD | 107.40 USD | `-4.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `269.50` | 75,980.00 USD | 0.00 USD | 29,530.00 USD | `-3.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `270.50` | 46,450.00 USD | 0.00 USD | 3,340.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `271.50` | 43,110.00 USD | 0.00 USD | 620.38 USD | `-3.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `272.50` | 42,490.00 USD | 0.00 USD | 13,500.00 USD | `-2.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `273.50` | 28,990.00 USD | 0.00 USD | 136.20 USD | `-2.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `274.50` | 28,850.00 USD | 0.00 USD | 667.86 USD | `-1.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `275.50` | 28,190.00 USD | 0.00 USD | 275.50 USD | `-1.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `276.50` | 27,910.00 USD | 0.00 USD | 553.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `277.50` | 27,360.00 USD | 0.00 USD | 326.34 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `278.50` | 27,030.00 USD | 0.00 USD | 5,040.00 USD | `-0.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `279.50` | 21,990.00 USD | 0.00 USD | 21,990.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `280.50` | 139.69 USD | 139.69 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `281.50` | 3,240.00 USD | 3,100.00 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `282.50` | 6,180.00 USD | 2,940.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `283.50` | 14,220.00 USD | 8,040.00 USD | 0.00 USD | `+1.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `284.50` | 14,360.00 USD | 137.98 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `285.50` | 15,410.00 USD | 1,050.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `286.50` | 15,690.00 USD | 280.77 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `287.50` | 22,600.00 USD | 6,910.00 USD | 0.00 USD | `+2.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `288.50` | 22,860.00 USD | 261.96 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `289.50` | 23,390.00 USD | 530.36 USD | 0.00 USD | `+3.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `290.50` | 23,600.00 USD | 212.36 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `291.50` | 48,880.00 USD | 25,280.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `292.50` | 49,050.00 USD | 167.89 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `293.50` | 50,040.00 USD | 992.62 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `294.50` | 52,060.00 USD | 2,020.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `295.50` | 56,790.00 USD | 4,730.00 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `297.50` | 56,900.00 USD | 110.37 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `298.50` | 57,290.00 USD | 388.95 USD | 0.00 USD | `+6.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `299.50` | 57,440.00 USD | 153.94 USD | 0.00 USD | `+6.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `300.50` | 68,220.00 USD | 10,780.00 USD | 0.00 USD | `+7.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `302.50` | 73,320.00 USD | 5,110.00 USD | 0.00 USD | `+8.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `304.50` | 84,050.00 USD | 10,730.00 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `305.50` | 86,700.00 USD | 2,650.00 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `308.50` | 86,980.00 USD | 282.89 USD | 0.00 USD | `+10.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `309.50` | 101,480.00 USD | 14,500.00 USD | 0.00 USD | `+10.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `310.50` | 102,110.00 USD | 634.04 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `316.50` | 103,150.00 USD | 1,030.00 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `318.50` | 108,800.00 USD | 5,650.00 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `320.50` | 109,330.00 USD | 534.59 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `321.50` | 109,650.00 USD | 321.50 USD | 0.00 USD | `+14.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `325.50` | 176,370.00 USD | 66,720.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `332.50` | 177,460.00 USD | 1,090.00 USD | 0.00 USD | `+18.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `334.50` | 189,450.00 USD | 12,000.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `340.50` | 190,000.00 USD | 547.52 USD | 0.00 USD | `+21.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `345.50` | 190,110.00 USD | 110.91 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `346.50` | 190,370.00 USD | 257.45 USD | 0.00 USD | `+23.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `348.50` | 190,540.00 USD | 174.25 USD | 0.00 USD | `+24.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `351.50` | 190,700.00 USD | 151.50 USD | 0.00 USD | `+25.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `357.50` | 192,150.00 USD | 1,450.00 USD | 0.00 USD | `+27.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `359.50` | 193,920.00 USD | 1,770.00 USD | 0.00 USD | `+28.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `361.50` | 194,250.00 USD | 326.07 USD | 0.00 USD | `+29.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `363.50` | 195,080.00 USD | 826.60 USD | 0.00 USD | `+29.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `365.50` | 202,520.00 USD | 7,440.00 USD | 0.00 USD | `+30.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `369.50` | 203,200.00 USD | 682.84 USD | 0.00 USD | `+31.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `381.50` | 204,300.00 USD | 1,100.00 USD | 0.00 USD | `+36.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `396.50` | 204,990.00 USD | 683.96 USD | 0.00 USD | `+41.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `399.50` | 205,190.00 USD | 199.75 USD | 0.00 USD | `+42.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `400.50` | 206,920.00 USD | 1,730.00 USD | 0.00 USD | `+43.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `404.50` | 207,960.00 USD | 1,040.00 USD | 0.00 USD | `+44.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `405.50` | 208,330.00 USD | 376.71 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `410.50` | 208,490.00 USD | 158.86 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `415.50` | 214,390.00 USD | 5,900.00 USD | 0.00 USD | `+48.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `423.50` | 215,470.00 USD | 1,080.00 USD | 0.00 USD | `+51.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `425.50` | 217,170.00 USD | 1,700.00 USD | 0.00 USD | `+51.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `430.50` | 218,730.00 USD | 1,550.00 USD | 0.00 USD | `+53.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `435.50` | 220,110.00 USD | 1,380.00 USD | 0.00 USD | `+55.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `436.50` | 220,730.00 USD | 621.14 USD | 0.00 USD | `+55.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `440.50` | 223,010.00 USD | 2,280.00 USD | 0.00 USD | `+57.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `445.50` | 223,230.00 USD | 222.75 USD | 0.00 USD | `+59.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `450.50` | 230,150.00 USD | 6,920.00 USD | 0.00 USD | `+60.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `451.50` | 236,070.00 USD | 5,920.00 USD | 0.00 USD | `+61.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `460.50` | 237,200.00 USD | 1,130.00 USD | 0.00 USD | `+64.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `482.50` | 244,830.00 USD | 7,630.00 USD | 0.00 USD | `+72.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `487.50` | 245,810.00 USD | 975.00 USD | 0.00 USD | `+74.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `490.50` | 246,790.00 USD | 981.00 USD | 0.00 USD | `+75.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `499.50` | 247,290.00 USD | 499.50 USD | 0.00 USD | `+78.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `500.50` | 2,130,000.00 USD | 1,890,000.00 USD | 0.00 USD | `+78.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `501.50` | 2,130,000.00 USD | 1,000.00 USD | 0.00 USD | `+79.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `518.50` | 2,140,000.00 USD | 1,040.00 USD | 0.00 USD | `+85.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `522.50` | 2,140,000.00 USD | 340.67 USD | 0.00 USD | `+86.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `556.50` | 2,140,000.00 USD | 638.86 USD | 0.00 USD | `+98.73%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `240.00` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 887.27 USD | 588.60 USD | 37.38 USD |
| `7D` | `240.40` | 10,360,000.00 USD | 0.00 USD | 10,360,000.00 USD | 1,510.00 USD | 0.00 USD | 17.73 USD |
| `7D` | `240.80` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 1,270.00 USD | 0.00 USD | 4,560.00 USD |
| `7D` | `241.20` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 0.00 USD | 1,180.00 USD | 4.90 USD |
| `7D` | `241.60` | 10,350,000.00 USD | 0.00 USD | 10,350,000.00 USD | 7,150.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `242.00` | 10,340,000.00 USD | 0.00 USD | 10,340,000.00 USD | 27,990.00 USD | 11,260.00 USD | 21,510.00 USD |
| `7D` | `242.40` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 27,150.00 USD | 0.00 USD | 8,370.00 USD |
| `7D` | `242.80` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 1,150.00 USD | 5,680.00 USD | 0.66 USD |
| `7D` | `243.20` | 10,240,000.00 USD | 0.00 USD | 10,240,000.00 USD | 0.00 USD | 10,950.00 USD | 5,490.00 USD |
| `7D` | `243.60` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 30,790.00 USD | 762.05 USD | 0.00 USD |
| `7D` | `244.00` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 0.00 USD | 0.00 USD | 20,790.00 USD |
| `7D` | `244.80` | 10,170,000.00 USD | 0.00 USD | 10,170,000.00 USD | 836.88 USD | 18,270.00 USD | 2,640.00 USD |
| `7D` | `245.20` | 10,150,000.00 USD | 0.00 USD | 10,150,000.00 USD | 599.05 USD | 15,350.00 USD | 1,640.00 USD |
| `7D` | `245.60` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 4,550.00 USD | 9,660.00 USD | 6,240.00 USD |
| `7D` | `246.00` | 10,110,000.00 USD | 0.00 USD | 10,110,000.00 USD | 11,860.00 USD | 8,060.00 USD | 0.00 USD |
| `7D` | `246.40` | 10,090,000.00 USD | 0.00 USD | 10,090,000.00 USD | 11,440.00 USD | 10,300.00 USD | 7,710.00 USD |
| `7D` | `246.80` | 10,060,000.00 USD | 0.00 USD | 10,060,000.00 USD | 4,590.00 USD | 472.85 USD | 1,720.00 USD |
| `7D` | `247.20` | 10,050,000.00 USD | 0.00 USD | 10,050,000.00 USD | 14,580.00 USD | 17,320.00 USD | 2,700.00 USD |
| `7D` | `247.60` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 9,000.00 USD | 4,610.00 USD | 11.75 USD |
| `7D` | `248.00` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 555.60 USD | 310.87 USD | 2,800.00 USD |
| `7D` | `248.40` | 10,000,000.00 USD | 0.00 USD | 10,000,000.00 USD | 13,830.00 USD | 3,060.00 USD | 28,090.00 USD |
| `7D` | `248.80` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 28,270.00 USD | 15,790.00 USD | 28,690.00 USD |
| `7D` | `249.20` | 9,880,000.00 USD | 0.00 USD | 9,880,000.00 USD | 23,830.00 USD | 30,530.00 USD | 3,540.00 USD |
| `7D` | `249.60` | 9,830,000.00 USD | 0.00 USD | 9,830,000.00 USD | 46,340.00 USD | 35,710.00 USD | 16,340.00 USD |
| `7D` | `250.00` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 38,050.00 USD | 9,910.00 USD | 22,870.00 USD |
| `1D` | `250.40` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 9,190.00 USD | 6,150.00 USD | 12,280.00 USD |
| `7D` | `250.40` | 9,660,000.00 USD | 0.00 USD | 9,660,000.00 USD | 22,500.00 USD | 35,680.00 USD | 12,500.00 USD |
| `1D` | `250.80` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 9,730.00 USD | 14,160.00 USD | 10,300.00 USD |
| `7D` | `250.80` | 9,590,000.00 USD | 0.00 USD | 9,590,000.00 USD | 32,990.00 USD | 60,940.00 USD | 27,640.00 USD |
| `1D` | `251.20` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 25,370.00 USD | 23,980.00 USD | 16,990.00 USD |
| `7D` | `251.20` | 9,460,000.00 USD | 0.00 USD | 9,460,000.00 USD | 44,420.00 USD | 56,200.00 USD | 18,160.00 USD |
| `1D` | `251.60` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 26,820.00 USD | 47,060.00 USD | 19,210.00 USD |
| `7D` | `251.60` | 9,340,000.00 USD | 0.00 USD | 9,340,000.00 USD | 51,190.00 USD | 89,120.00 USD | 44,770.00 USD |
| `1D` | `252.00` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 16,340.00 USD | 11,100.00 USD | 16,180.00 USD |
| `7D` | `252.00` | 9,160,000.00 USD | 0.00 USD | 9,160,000.00 USD | 63,990.00 USD | 31,270.00 USD | 32,510.00 USD |
| `1D` | `252.40` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 6,700.00 USD | 1,540.00 USD | 2,530.00 USD |
| `7D` | `252.40` | 9,030,000.00 USD | 0.00 USD | 9,030,000.00 USD | 53,750.00 USD | 29,340.00 USD | 17,700.00 USD |
| `1D` | `252.80` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 6,800.00 USD | 2,270.00 USD | 4,830.00 USD |
| `7D` | `252.80` | 8,930,000.00 USD | 0.00 USD | 8,930,000.00 USD | 24,570.00 USD | 10,300.00 USD | 13.01 USD |
| `1D` | `253.20` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 8,060.00 USD | 3,900.00 USD | 821.20 USD |
| `7D` | `253.20` | 8,900,000.00 USD | 0.00 USD | 8,900,000.00 USD | 12,620.00 USD | 36,470.00 USD | 14,210.00 USD |
| `1D` | `253.60` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 20,500.00 USD | 17,790.00 USD | 21,440.00 USD |
| `7D` | `253.60` | 8,830,000.00 USD | 0.00 USD | 8,830,000.00 USD | 27,790.00 USD | 37,080.00 USD | 34,110.00 USD |
| `1D` | `254.00` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 5,800.00 USD | 8,100.00 USD | 9,690.00 USD |
| `7D` | `254.00` | 8,730,000.00 USD | 0.00 USD | 8,730,000.00 USD | 45,450.00 USD | 35,310.00 USD | 21,940.00 USD |
| `1D` | `254.40` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 8,310.00 USD | 13,680.00 USD | 3,970.00 USD |
| `7D` | `254.40` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 19,460.00 USD | 25,910.00 USD | 60,760.00 USD |
| `1D` | `254.80` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 2,210.00 USD | 3,080.00 USD | 1,480.00 USD |
| `7D` | `254.80` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 50,650.00 USD | 29,470.00 USD | 36,980.00 USD |
| `1D` | `255.20` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 16,750.00 USD | 17,660.00 USD | 12,890.00 USD |
| `7D` | `255.20` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 23,880.00 USD | 13,020.00 USD | 25,500.00 USD |
| `1D` | `255.60` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 17,490.00 USD | 32,020.00 USD | 23,780.00 USD |
| `7D` | `255.60` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 33,430.00 USD | 16,640.00 USD | 31,160.00 USD |
| `1D` | `256.00` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 10,010.00 USD | 11,710.00 USD | 15,530.00 USD |
| `7D` | `256.00` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 18,300.00 USD | 10,360.00 USD | 25,390.00 USD |
| `1D` | `256.40` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 7,460.00 USD | 31,910.00 USD | 19,770.00 USD |
| `7D` | `256.40` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 29,190.00 USD | 739.13 USD | 23,250.00 USD |
| `1D` | `256.80` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 1,820.00 USD | 5,950.00 USD | 14,920.00 USD |
| `7D` | `256.80` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 32,310.00 USD | 13,750.00 USD | 56,650.00 USD |
| `1D` | `257.20` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 14,160.00 USD | 3,660.00 USD | 7,340.00 USD |
| `7D` | `257.20` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 15,600.00 USD | 3,420.00 USD | 11,100.00 USD |
| `1D` | `257.60` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 2,420.00 USD | 5,450.00 USD | 9,250.00 USD |
| `7D` | `257.60` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 34,480.00 USD | 4,400.00 USD | 10,260.00 USD |
| `1D` | `258.00` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 19,750.00 USD | 1,980.00 USD | 38,720.00 USD |
| `7D` | `258.00` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 26,960.00 USD | 4,790.00 USD | 7,950.00 USD |
| `1D` | `258.40` | 4,480,000.00 USD | 0.00 USD | 4,480,000.00 USD | 18,320.00 USD | 15,600.00 USD | 19,460.00 USD |
| `7D` | `258.40` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 128,170.00 USD | 37,820.00 USD | 92,480.00 USD |
| `1D` | `258.80` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 8,320.00 USD | 30,390.00 USD | 40,000.00 USD |
| `7D` | `258.80` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 59,230.00 USD | 2,500.00 USD | 34,370.00 USD |
| `1D` | `259.20` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 14,560.00 USD | 12,990.00 USD | 17,630.00 USD |
| `7D` | `259.20` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 5,210.00 USD | 45,200.00 USD | 8,030.00 USD |
| `1D` | `259.60` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 13,590.00 USD | 4,640.00 USD | 22,250.00 USD |
| `7D` | `259.60` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 20,030.00 USD | 8,340.00 USD | 16,980.00 USD |
| `1D` | `260.00` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 45,280.00 USD | 32,840.00 USD | 23,920.00 USD |
| `7D` | `260.00` | 7,480,000.00 USD | 0.00 USD | 7,480,000.00 USD | 103,390.00 USD | 63,410.00 USD | 106,080.00 USD |
| `1D` | `260.40` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 19,610.00 USD | 7,660.00 USD | 16,020.00 USD |
| `7D` | `260.40` | 7,200,000.00 USD | 0.00 USD | 7,200,000.00 USD | 4,590.00 USD | 3,590.00 USD | 74,400.00 USD |
| `1D` | `260.80` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 1,360.00 USD | 46,690.00 USD | 25,130.00 USD |
| `7D` | `260.80` | 7,120,000.00 USD | 0.00 USD | 7,120,000.00 USD | 14,600.00 USD | 56,470.00 USD | 37,920.00 USD |
| `1D` | `261.20` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 8,180.00 USD | 23,140.00 USD | 30,850.00 USD |
| `7D` | `261.20` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 6,110.00 USD | 90,180.00 USD | 15,970.00 USD |
| `1D` | `261.60` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 18,900.00 USD | 55,190.00 USD | 53,770.00 USD |
| `7D` | `261.60` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 24,520.00 USD | 84,260.00 USD | 48,430.00 USD |
| `1D` | `262.00` | 3,850,000.00 USD | 0.00 USD | 3,850,000.00 USD | 17,910.00 USD | 44,250.00 USD | 21,380.00 USD |
| `7D` | `262.00` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 61,230.00 USD | 39,230.00 USD | 81,290.00 USD |
| `1D` | `262.40` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 21,110.00 USD | 6,200.00 USD | 10,850.00 USD |
| `7D` | `262.40` | 6,560,000.00 USD | 0.00 USD | 6,560,000.00 USD | 28,440.00 USD | 55,580.00 USD | 0.80 USD |
| `1D` | `262.80` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 747.53 USD | 13,250.00 USD | 19,480.00 USD |
| `7D` | `262.80` | 6,480,000.00 USD | 0.00 USD | 6,480,000.00 USD | 73,660.00 USD | 45,060.00 USD | 32,790.00 USD |
| `1D` | `263.20` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 10,020.00 USD | 4,350.00 USD | 61,470.00 USD |
| `7D` | `263.20` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 21,560.00 USD | 13,710.00 USD | 152.95 USD |
| `1D` | `263.60` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 30,230.00 USD | 29,870.00 USD | 41,410.00 USD |
| `7D` | `263.60` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 278,330.00 USD | 1,880.00 USD | 83,120.00 USD |
| `1D` | `264.00` | 3,520,000.00 USD | 0.00 USD | 3,520,000.00 USD | 52,440.00 USD | 15,650.00 USD | 17,280.00 USD |
| `7D` | `264.00` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 135,390.00 USD | 629.16 USD | 34,870.00 USD |
| `1D` | `264.40` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 6,130.00 USD | 20,240.00 USD | 21.88 USD |
| `7D` | `264.40` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 44,740.00 USD | 21,810.00 USD | 44.70 USD |
| `1D` | `264.80` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 22,660.00 USD | 1,670.00 USD | 20,040.00 USD |
| `7D` | `264.80` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 26,950.00 USD | 1,900.00 USD | 198.07 USD |
| `1D` | `265.20` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 75,930.00 USD | 3,490.00 USD | 33,270.00 USD |
| `7D` | `265.20` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 106,380.00 USD | 1,640.00 USD | 33,980.00 USD |
| `1D` | `265.60` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 415.98 USD | 788.61 USD | 12.92 USD |
| `7D` | `265.60` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 199,660.00 USD | 694.90 USD | 151.46 USD |
| `1D` | `266.00` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 12,200.00 USD | 209.24 USD | 5.24 USD |
| `7D` | `266.00` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 140,360.00 USD | 645.20 USD | 25.50 USD |
| `1D` | `266.40` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 4,400.00 USD | 13,530.00 USD | 4,800.00 USD |
| `7D` | `266.40` | 5,180,000.00 USD | 0.00 USD | 5,180,000.00 USD | 106,830.00 USD | 804.70 USD | 10.30 USD |
| `1D` | `266.80` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 22,750.00 USD | 30,970.00 USD | 0.00 USD |
| `7D` | `266.80` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 125,320.00 USD | 63,260.00 USD | 28.20 USD |
| `1D` | `267.20` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 43,580.00 USD | 34,990.00 USD | 12,550.00 USD |
| `7D` | `267.20` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 101,740.00 USD | 26,850.00 USD | 23.69 USD |
| `1D` | `267.60` | 3,070,000.00 USD | 0.00 USD | 3,070,000.00 USD | 10,330.00 USD | 72,630.00 USD | 23,000.00 USD |
| `7D` | `267.60` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 75,350.00 USD | 61,270.00 USD | 38,660.00 USD |
| `1D` | `268.00` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 19,060.00 USD | 4,020.00 USD | 51,860.00 USD |
| `7D` | `268.00` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 234,660.00 USD | 25,100.00 USD | 388.83 USD |
| `1D` | `268.40` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 18,310.00 USD | 43,230.00 USD | 13,970.00 USD |
| `7D` | `268.40` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 136,830.00 USD | 124,980.00 USD | 95,630.00 USD |
| `1D` | `268.80` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 21,330.00 USD | 11,530.00 USD | 146.66 USD |
| `7D` | `268.80` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 23,340.00 USD | 18,320.00 USD | 105.78 USD |
| `1D` | `269.20` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 10,990.00 USD | 2,810.00 USD | 8,340.00 USD |
| `7D` | `269.20` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 2,470.00 USD | 70.45 USD |
| `1D` | `269.60` | 2,760,000.00 USD | 0.00 USD | 2,760,000.00 USD | 6,520.00 USD | 19,580.00 USD | 10,340.00 USD |
| `7D` | `269.60` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 0.00 USD | 2,540.00 USD | 200.97 USD |
| `1D` | `270.00` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 7,960.00 USD | 12,030.00 USD | 3,380.00 USD |
| `7D` | `270.00` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 1,310.00 USD | 146.37 USD |
| `1D` | `270.40` | 2,700,000.00 USD | 0.00 USD | 2,700,000.00 USD | 54,750.00 USD | 1,930.00 USD | 3,540.00 USD |
| `7D` | `270.40` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 166.02 USD |
| `1D` | `270.80` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 3,210.00 USD | 15,660.00 USD | 4,930.00 USD |
| `7D` | `270.80` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 33,050.00 USD | 0.00 USD | 84.79 USD |
| `1D` | `271.20` | 2,620,000.00 USD | 0.00 USD | 2,620,000.00 USD | 12,890.00 USD | 6,410.00 USD | 12,590.00 USD |
| `7D` | `271.20` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 20,830.00 USD |
| `1D` | `271.60` | 2,590,000.00 USD | 0.00 USD | 2,590,000.00 USD | 0.00 USD | 8,940.00 USD | 13,270.00 USD |
| `7D` | `271.60` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 0.00 USD | 7,250.00 USD | 61,070.00 USD |
| `1D` | `272.00` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 28,410.00 USD | 52,240.00 USD | 9,610.00 USD |
| `7D` | `272.00` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 61,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `272.40` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 10,530.00 USD | 35,390.00 USD | 57,740.00 USD |
| `7D` | `272.40` | 3,730,000.00 USD | 0.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 29,930.00 USD |
| `1D` | `272.80` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 62,230.00 USD | 15,740.00 USD | 68,920.00 USD |
| `7D` | `272.80` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 25,660.00 USD | 69,990.00 USD | 89,520.00 USD |
| `1D` | `273.20` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 32,520.00 USD | 117,860.00 USD | 43,510.00 USD |
| `7D` | `273.20` | 3,510,000.00 USD | 0.00 USD | 3,510,000.00 USD | 0.00 USD | 79,710.00 USD | 173,630.00 USD |
| `1D` | `273.60` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 42,760.00 USD | 18,430.00 USD | 53,420.00 USD |
| `7D` | `273.60` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 66,850.00 USD |
| `1D` | `274.00` | 1,910,000.00 USD | 0.00 USD | 1,910,000.00 USD | 159,390.00 USD | 97,110.00 USD | 39,870.00 USD |
| `7D` | `274.00` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 466,260.00 USD | 0.00 USD | 94,820.00 USD |
| `1D` | `274.40` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 155,650.00 USD | 27,970.00 USD | 41,320.00 USD |
| `7D` | `274.40` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 413,010.00 USD | 34,960.00 USD | 83,040.00 USD |
| `1D` | `274.80` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 70,330.00 USD | 22,510.00 USD | 29,260.00 USD |
| `7D` | `274.80` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 334,980.00 USD | 0.00 USD | 34,730.00 USD |
| `1D` | `275.20` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 11,720.00 USD | 3,760.00 USD | 0.00 USD |
| `7D` | `275.20` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 59,580.00 USD | 19,960.00 USD | 0.00 USD |
| `1D` | `275.60` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 35,420.00 USD | 15,980.00 USD | 26,710.00 USD |
| `7D` | `275.60` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 1,350.00 USD | 0.00 USD | 48,580.00 USD |
| `1D` | `276.00` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 143,900.00 USD | 18,930.00 USD | 40,360.00 USD |
| `7D` | `276.00` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 3,140.00 USD | 23,010.00 USD | 33,750.00 USD |
| `1D` | `276.40` | 973,410.00 USD | 0.00 USD | 973,410.00 USD | 40,580.00 USD | 16,150.00 USD | 18,670.00 USD |
| `7D` | `276.40` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 217,250.00 USD | 0.00 USD | 103,930.00 USD |
| `1D` | `276.80` | 898,010.00 USD | 0.00 USD | 898,010.00 USD | 11,880.00 USD | 25,410.00 USD | 25,170.00 USD |
| `7D` | `276.80` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 16,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `277.20` | 835,550.00 USD | 0.00 USD | 835,550.00 USD | 25,720.00 USD | 17,880.00 USD | 26,540.00 USD |
| `7D` | `277.20` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 28,580.00 USD | 42,210.00 USD | 163,790.00 USD |
| `1D` | `277.60` | 765,410.00 USD | 0.00 USD | 765,410.00 USD | 26,620.00 USD | 21,090.00 USD | 0.00 USD |
| `7D` | `277.60` | 968,400.00 USD | 0.00 USD | 968,400.00 USD | 123,610.00 USD | 193,330.00 USD | 18,270.00 USD |
| `1D` | `278.00` | 717,700.00 USD | 0.00 USD | 717,700.00 USD | 21,070.00 USD | 54,860.00 USD | 103,960.00 USD |
| `7D` | `278.00` | 633,190.00 USD | 0.00 USD | 633,190.00 USD | 0.00 USD | 1,830.00 USD | 59,850.00 USD |
| `1D` | `278.40` | 537,810.00 USD | 0.00 USD | 537,810.00 USD | 57,720.00 USD | 125,180.00 USD | 77,350.00 USD |
| `7D` | `278.40` | 571,510.00 USD | 0.00 USD | 571,510.00 USD | 76,060.00 USD | 35,270.00 USD | 179,030.00 USD |
| `1D` | `278.80` | 277,570.00 USD | 0.00 USD | 277,570.00 USD | 55,370.00 USD | 10,830.00 USD | 0.00 USD |
| `7D` | `278.80` | 281,150.00 USD | 0.00 USD | 281,150.00 USD | 0.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `279.20` | 211,370.00 USD | 0.00 USD | 211,370.00 USD | 4,440.00 USD | 3,800.00 USD | 23,400.00 USD |
| `7D` | `279.20` | 262,090.00 USD | 0.00 USD | 262,090.00 USD | 2,660.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `279.60` | 179,730.00 USD | 0.00 USD | 179,730.00 USD | 0.00 USD | 0.00 USD | 47,450.00 USD |
| `1D` | `280.00` | 132,270.00 USD | 0.00 USD | 132,270.00 USD | 0.00 USD | 13,070.00 USD | 31,340.00 USD |
| `1D` | `280.80` | 87,860.00 USD | 0.00 USD | 87,860.00 USD | 0.00 USD | 0.00 USD | 12.68 USD |
| `7D` | `280.80` | 259,430.00 USD | 0.00 USD | 259,430.00 USD | 5,560.00 USD | 9,980.00 USD | 0.00 USD |
| `7D` | `281.20` | 243,880.00 USD | 0.00 USD | 243,880.00 USD | 0.00 USD | 14,140.00 USD | 79,690.00 USD |
| `7D` | `281.60` | 150,060.00 USD | 0.00 USD | 150,060.00 USD | 0.00 USD | 0.00 USD | 122,390.00 USD |
| `7D` | `282.00` | 27,670.00 USD | 0.00 USD | 27,670.00 USD | 0.00 USD | 20,710.00 USD | 0.00 USD |
| `1D` | `282.40` | 87,850.00 USD | 0.00 USD | 87,850.00 USD | 8,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `282.40` | 6,970.00 USD | 0.00 USD | 6,970.00 USD | 3,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `283.20` | 79,590.00 USD | 0.00 USD | 79,590.00 USD | 1,280.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.20` | 3,450.00 USD | 0.00 USD | 3,450.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `283.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.00` | 2,000.00 USD | 2,000.00 USD | 0.00 USD | 2,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.40` | 3,560.00 USD | 3,560.00 USD | 0.00 USD | 1,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `284.80` | 58,950.00 USD | 58,950.00 USD | 0.00 USD | 0.00 USD | 55,390.00 USD | 0.00 USD |
| `1D` | `285.20` | 78,310.00 USD | 0.00 USD | 78,310.00 USD | 36,620.00 USD | 0.00 USD | 41,690.00 USD |
| `7D` | `285.20` | 458,290.00 USD | 458,290.00 USD | 0.00 USD | 126,910.00 USD | 206,630.00 USD | 65,810.00 USD |
| `1D` | `285.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `285.60` | 27,570.00 USD | 27,570.00 USD | 0.00 USD | 27,570.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `285.60` | 660,380.00 USD | 660,380.00 USD | 0.00 USD | 50,130.00 USD | 151,960.00 USD | 0.00 USD |
| `1D` | `286.00` | 99,520.00 USD | 99,520.00 USD | 0.00 USD | 29,220.00 USD | 2,980.00 USD | 39,750.00 USD |
| `7D` | `286.00` | 716,810.00 USD | 716,810.00 USD | 0.00 USD | 1,200.00 USD | 55,230.00 USD | 0.00 USD |
| `1D` | `286.40` | 121,480.00 USD | 121,480.00 USD | 0.00 USD | 17,340.00 USD | 4,610.00 USD | 4.24 USD |
| `7D` | `286.40` | 854,250.00 USD | 854,250.00 USD | 0.00 USD | 0.00 USD | 137,440.00 USD | 0.00 USD |
| `1D` | `286.80` | 228,380.00 USD | 228,380.00 USD | 0.00 USD | 18,110.00 USD | 10,660.00 USD | 78,130.00 USD |
| `7D` | `286.80` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 30,110.00 USD | 122,000.00 USD | 0.00 USD |
| `1D` | `287.20` | 427,500.00 USD | 427,500.00 USD | 0.00 USD | 112,240.00 USD | 47,050.00 USD | 39,830.00 USD |
| `7D` | `287.20` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 82,910.00 USD | 116,440.00 USD | 0.00 USD |
| `1D` | `287.60` | 576,390.00 USD | 576,390.00 USD | 0.00 USD | 47,390.00 USD | 34,850.00 USD | 66,650.00 USD |
| `7D` | `287.60` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 70,340.00 USD | 33,740.00 USD | 53,280.00 USD |
| `1D` | `288.00` | 676,230.00 USD | 676,230.00 USD | 0.00 USD | 9,440.00 USD | 26,480.00 USD | 63,920.00 USD |
| `7D` | `288.00` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 272,310.00 USD | 0.00 USD |
| `1D` | `288.40` | 795,940.00 USD | 795,940.00 USD | 0.00 USD | 68,380.00 USD | 22,110.00 USD | 29,220.00 USD |
| `7D` | `288.40` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 1,550.00 USD | 41,660.00 USD |
| `1D` | `288.80` | 879,250.00 USD | 879,250.00 USD | 0.00 USD | 43,690.00 USD | 32,420.00 USD | 7,210.00 USD |
| `7D` | `288.80` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 124,780.00 USD | 15,650.00 USD | 122,130.00 USD |
| `1D` | `289.20` | 968,510.00 USD | 968,510.00 USD | 0.00 USD | 6,160.00 USD | 52,920.00 USD | 30,180.00 USD |
| `7D` | `289.20` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 932.60 USD | 59,850.00 USD |
| `1D` | `289.60` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 25,200.00 USD | 66,520.00 USD | 121,890.00 USD |
| `7D` | `289.60` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 62,370.00 USD | 95,440.00 USD |
| `1D` | `290.00` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 115,670.00 USD | 66,820.00 USD | 124,250.00 USD |
| `7D` | `290.00` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 53,890.00 USD | 38,660.00 USD | 122,160.00 USD |
| `1D` | `290.40` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 40,570.00 USD | 111,760.00 USD | 49,240.00 USD |
| `7D` | `290.40` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 33,530.00 USD | 19,060.00 USD | 0.00 USD |
| `1D` | `290.80` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 56,480.00 USD | 71,550.00 USD | 54,940.00 USD |
| `7D` | `290.80` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 30,940.00 USD | 1,760.00 USD | 90,940.00 USD |
| `1D` | `291.20` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 28,320.00 USD | 25,130.00 USD | 24,320.00 USD |
| `7D` | `291.20` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 24,680.00 USD | 18,390.00 USD | 0.00 USD |
| `1D` | `291.60` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 12,550.00 USD | 6,560.00 USD | 30,420.00 USD |
| `7D` | `291.60` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 2,710.00 USD | 85,290.00 USD | 19,430.00 USD |
| `1D` | `292.00` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 7,010.00 USD | 30,490.00 USD | 31.89 USD |
| `7D` | `292.00` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 2,560.00 USD | 149,160.00 USD | 9.00 USD |
| `1D` | `292.40` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 29,860.00 USD | 14,820.00 USD | 13,730.00 USD |
| `7D` | `292.40` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 25,520.00 USD | 40.84 USD |
| `1D` | `292.80` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 29,430.00 USD | 27,590.00 USD | 3,560.00 USD |
| `7D` | `292.80` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 887.27 USD | 101,280.00 USD | 131.64 USD |
| `1D` | `293.20` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 50,900.00 USD | 12,760.00 USD | 32,300.00 USD |
| `7D` | `293.20` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 33,580.00 USD | 132,080.00 USD | 88.00 USD |
| `1D` | `293.60` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 77,380.00 USD | 48,560.00 USD | 20,970.00 USD |
| `7D` | `293.60` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 1,860.00 USD | 113.10 USD |
| `1D` | `294.00` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 30,750.00 USD | 23,790.00 USD | 70,500.00 USD |
| `7D` | `294.00` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 54,350.00 USD | 34,230.00 USD | 95,120.00 USD |
| `1D` | `294.40` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 64,400.00 USD | 64,490.00 USD | 116,730.00 USD |
| `7D` | `294.40` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 201,580.00 USD | 9,460.00 USD | 92,460.00 USD |
| `1D` | `294.80` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 59,910.00 USD | 35,750.00 USD | 44,460.00 USD |
| `7D` | `294.80` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 63,770.00 USD | 108,720.00 USD | 89,150.00 USD |
| `1D` | `295.20` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 8,650.00 USD | 28,960.00 USD | 99,830.00 USD |
| `7D` | `295.20` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 733.30 USD | 64,810.00 USD | 214,270.00 USD |
| `1D` | `295.60` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 73,320.00 USD | 48,980.00 USD | 132,630.00 USD |
| `7D` | `295.60` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 176,660.00 USD | 91,360.00 USD | 306,320.00 USD |
| `1D` | `296.00` | 3,520,000.00 USD | 3,520,000.00 USD | 0.00 USD | 56,610.00 USD | 114,680.00 USD | 43,670.00 USD |
| `7D` | `296.00` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 76,740.00 USD | 99,260.00 USD | 86,710.00 USD |
| `1D` | `296.40` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 80,090.00 USD | 31,130.00 USD | 27,120.00 USD |
| `7D` | `296.40` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 1,550.00 USD | 78,210.00 USD | 68,400.00 USD |
| `1D` | `296.80` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 24,560.00 USD | 32,150.00 USD | 74,510.00 USD |
| `7D` | `296.80` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 133,480.00 USD | 4,410.00 USD | 201,410.00 USD |
| `1D` | `297.20` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 56,450.00 USD | 7,700.00 USD | 50,330.00 USD |
| `7D` | `297.20` | 5,630,000.00 USD | 5,630,000.00 USD | 0.00 USD | 77,480.00 USD | 51,810.00 USD | 72.03 USD |
| `1D` | `297.60` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 7,640.00 USD | 11,760.00 USD | 29,800.00 USD |
| `7D` | `297.60` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 1,640.00 USD | 62,110.00 USD | 34,710.00 USD |
| `1D` | `298.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 63,620.00 USD | 9,890.00 USD | 41,720.00 USD |
| `7D` | `298.00` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 47,790.00 USD | 43,980.00 USD | 75,730.00 USD |
| `1D` | `298.40` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 7,430.00 USD | 2,280.00 USD | 56,410.00 USD |
| `7D` | `298.40` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 32,250.00 USD | 42,940.00 USD | 48,050.00 USD |
| `1D` | `298.80` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 23,700.00 USD | 457.80 USD | 94,680.00 USD |
| `7D` | `298.80` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 69,820.00 USD | 12,530.00 USD | 83.18 USD |
| `1D` | `299.20` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 8,500.00 USD | 15,770.00 USD | 12,340.00 USD |
| `7D` | `299.20` | 6,210,000.00 USD | 6,210,000.00 USD | 0.00 USD | 2,350.00 USD | 15,140.00 USD | 85,830.00 USD |
| `1D` | `299.60` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 36,030.00 USD | 5,850.00 USD | 21,870.00 USD |
| `7D` | `299.60` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 4,590.00 USD | 13,830.00 USD | 19,830.00 USD |
| `1D` | `300.00` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 3,760.00 USD | 14,300.00 USD | 27,500.00 USD |
| `7D` | `300.00` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 53,130.00 USD | 10,090.00 USD | 0.00 USD |
| `1D` | `300.40` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 41,880.00 USD | 31,000.00 USD | 42,620.00 USD |
| `7D` | `300.40` | 6,310,000.00 USD | 6,310,000.00 USD | 0.00 USD | 2,070.00 USD | 645.96 USD | 58.05 USD |
| `1D` | `300.80` | 4,530,000.00 USD | 4,530,000.00 USD | 0.00 USD | 790.57 USD | 879.82 USD | 17,320.00 USD |
| `7D` | `300.80` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 24,730.00 USD | 71,120.00 USD | 48,360.00 USD |
| `1D` | `301.20` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 348.65 USD | 15,610.00 USD | 30,860.00 USD |
| `7D` | `301.20` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 48,570.00 USD | 42,080.00 USD | 91,020.00 USD |
| `1D` | `301.60` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 19,530.00 USD | 8,470.00 USD | 34,890.00 USD |
| `7D` | `301.60` | 6,840,000.00 USD | 6,840,000.00 USD | 0.00 USD | 62,390.00 USD | 79,410.00 USD | 59,560.00 USD |
| `1D` | `302.00` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 25,220.00 USD | 28,210.00 USD | 10,420.00 USD |
| `7D` | `302.00` | 7,070,000.00 USD | 7,070,000.00 USD | 0.00 USD | 52,640.00 USD | 150,800.00 USD | 26,260.00 USD |
| `1D` | `302.40` | 4,740,000.00 USD | 4,740,000.00 USD | 0.00 USD | 11,420.00 USD | 5,200.00 USD | 17,560.00 USD |
| `7D` | `302.40` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 580.96 USD | 99,780.00 USD | 2.17 USD |
| `1D` | `302.80` | 4,790,000.00 USD | 4,790,000.00 USD | 0.00 USD | 4,420.00 USD | 13,290.00 USD | 34,920.00 USD |
| `7D` | `302.80` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 71,700.00 USD | 111,900.00 USD | 41,810.00 USD |
| `1D` | `303.20` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 21,180.00 USD | 1,390.00 USD | 9,360.00 USD |
| `7D` | `303.20` | 7,390,000.00 USD | 7,390,000.00 USD | 0.00 USD | 0.00 USD | 1,780.00 USD | 177.41 USD |
| `1D` | `303.60` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 228.18 USD | 2,000.00 USD | 1.44 USD |
| `7D` | `303.60` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 2,130.00 USD | 693.54 USD | 24,610.00 USD |
| `1D` | `304.00` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 21,920.00 USD | 1,760.00 USD | 18,760.00 USD |
| `7D` | `304.00` | 7,480,000.00 USD | 7,480,000.00 USD | 0.00 USD | 20,680.00 USD | 14,630.00 USD | 21,410.00 USD |
| `1D` | `304.40` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 9,750.00 USD | 2,470.00 USD | 49,830.00 USD |
| `7D` | `304.40` | 7,490,000.00 USD | 7,490,000.00 USD | 0.00 USD | 1,340.00 USD | 11,280.00 USD | 82.73 USD |
| `1D` | `304.80` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 9,920.00 USD | 3,310.00 USD | 16,360.00 USD |
| `7D` | `304.80` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 34,540.00 USD | 682.27 USD | 4,050.00 USD |
| `1D` | `305.20` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 47.98 USD | 5,330.00 USD | 2,030.00 USD |
| `7D` | `305.20` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 113,060.00 USD | 128,470.00 USD | 89,570.00 USD |
| `1D` | `305.60` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 3,060.00 USD | 440.72 USD | 12.59 USD |
| `7D` | `305.60` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 76,400.00 USD | 21,950.00 USD | 41,130.00 USD |
| `1D` | `306.00` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 7,500.00 USD | 5,780.00 USD | 12,230.00 USD |
| `7D` | `306.00` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 60,790.00 USD | 50,650.00 USD | 44,610.00 USD |
| `1D` | `306.40` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 7,310.00 USD | 183.24 USD | 5,670.00 USD |
| `7D` | `306.40` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 35,090.00 USD | 65,940.00 USD | 25,800.00 USD |
| `1D` | `306.80` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 19,990.00 USD | 35,330.00 USD | 11,000.00 USD |
| `7D` | `306.80` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 84,850.00 USD | 66,200.00 USD | 66,880.00 USD |
| `1D` | `307.20` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 11,270.00 USD | 19,960.00 USD | 29,820.00 USD |
| `7D` | `307.20` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 11,730.00 USD | 87,980.00 USD | 106,420.00 USD |
| `1D` | `307.60` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 22,580.00 USD | 27,240.00 USD | 5.95 USD |
| `7D` | `307.60` | 8,970,000.00 USD | 8,970,000.00 USD | 0.00 USD | 78,600.00 USD | 122,070.00 USD | 56,050.00 USD |
| `1D` | `308.00` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 16,340.00 USD | 10,700.00 USD | 16,150.00 USD |
| `7D` | `308.00` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 125,470.00 USD | 70,950.00 USD | 60,840.00 USD |
| `1D` | `308.40` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 3,150.00 USD | 212.94 USD | 2,510.00 USD |
| `7D` | `308.40` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 131,420.00 USD | 45,250.00 USD | 114,550.00 USD |
| `1D` | `308.80` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 5,260.00 USD | 984.86 USD | 3,480.00 USD |
| `7D` | `308.80` | 9,630,000.00 USD | 9,630,000.00 USD | 0.00 USD | 54,880.00 USD | 42,230.00 USD | 19,730.00 USD |
| `1D` | `309.20` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 2,990.00 USD | 1,190.00 USD | 2,150.00 USD |
| `7D` | `309.20` | 9,720,000.00 USD | 9,720,000.00 USD | 0.00 USD | 33,440.00 USD | 19,290.00 USD | 32,300.00 USD |
| `1D` | `309.60` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 8,250.00 USD | 8,700.00 USD | 1,420.00 USD |
| `7D` | `309.60` | 10,000,000.00 USD | 10,000,000.00 USD | 0.00 USD | 41,230.00 USD | 107,950.00 USD | 131,040.00 USD |
| `1D` | `310.00` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 15,210.00 USD | 1,250.00 USD | 7,300.00 USD |
| `7D` | `310.00` | 10,200,000.00 USD | 10,200,000.00 USD | 0.00 USD | 20,240.00 USD | 98,540.00 USD | 82,930.00 USD |
| `1D` | `310.40` | 5,310,000.00 USD | 5,310,000.00 USD | 0.00 USD | 176.40 USD | 5,960.00 USD | 9,660.00 USD |
| `7D` | `310.40` | 10,390,000.00 USD | 10,390,000.00 USD | 0.00 USD | 91,290.00 USD | 74,340.00 USD | 21,940.00 USD |
| `1D` | `310.80` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 5,080.00 USD | 2,080.00 USD | 3,950.00 USD |
| `7D` | `310.80` | 10,460,000.00 USD | 10,460,000.00 USD | 0.00 USD | 29,950.00 USD | 35,930.00 USD | 12,180.00 USD |
| `1D` | `311.20` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 257.90 USD | 3,180.00 USD | 1,480.00 USD |
| `7D` | `311.20` | 10,680,000.00 USD | 10,680,000.00 USD | 0.00 USD | 74,340.00 USD | 65,480.00 USD | 72,070.00 USD |
| `1D` | `311.60` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 7,100.00 USD | 10,150.00 USD | 14.73 USD |
| `7D` | `311.60` | 10,730,000.00 USD | 10,730,000.00 USD | 0.00 USD | 40,900.00 USD | 10,550.00 USD | 5,680.00 USD |
| `1D` | `312.00` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 1,190.00 USD | 4,770.00 USD | 4,070.00 USD |
| `7D` | `312.00` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 40,590.00 USD | 2,020.00 USD | 28,220.00 USD |
| `1D` | `312.40` | 5,410,000.00 USD | 5,410,000.00 USD | 0.00 USD | 17,490.00 USD | 16,020.00 USD | 23,760.00 USD |
| `7D` | `312.40` | 10,890,000.00 USD | 10,890,000.00 USD | 0.00 USD | 28,530.00 USD | 22,960.00 USD | 31,140.00 USD |
| `1D` | `312.80` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 9,120.00 USD | 2,930.00 USD | 15,530.00 USD |
| `7D` | `312.80` | 10,910,000.00 USD | 10,910,000.00 USD | 0.00 USD | 15,280.00 USD | 2,460.00 USD | 7,350.00 USD |
| `1D` | `313.20` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 40.35 USD | 15,380.00 USD | 3,670.00 USD |
| `7D` | `313.20` | 10,990,000.00 USD | 10,990,000.00 USD | 0.00 USD | 26,740.00 USD | 10,510.00 USD | 38,360.00 USD |
| `1D` | `313.60` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 8,180.00 USD | 7,190.00 USD | 8,220.00 USD |
| `7D` | `313.60` | 11,030,000.00 USD | 11,030,000.00 USD | 0.00 USD | 10,400.00 USD | 755.05 USD | 34,650.00 USD |
| `1D` | `314.00` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 239.05 USD | 4,860.00 USD |
| `7D` | `314.00` | 11,080,000.00 USD | 11,080,000.00 USD | 0.00 USD | 22,920.00 USD | 815.59 USD | 20,600.00 USD |
| `1D` | `314.40` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 4,210.00 USD | 2,610.00 USD | 7,320.00 USD |
| `7D` | `314.40` | 11,150,000.00 USD | 11,150,000.00 USD | 0.00 USD | 51,980.00 USD | 307.60 USD | 24,560.00 USD |
| `1D` | `314.80` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 32.00 USD | 3,660.00 USD | 9,250.00 USD |
| `7D` | `314.80` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 17,720.00 USD | 0.00 USD | 10,250.00 USD |
| `1D` | `315.10` | 5,520,000.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 1,400.00 USD | 1,620.00 USD |
| `7D` | `315.20` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 258.00 USD | 3.94 USD |
| `7D` | `315.60` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 1,070.00 USD | 28,580.00 USD | 30,020.00 USD |
| `7D` | `316.00` | 11,290,000.00 USD | 11,290,000.00 USD | 0.00 USD | 38,990.00 USD | 5,120.00 USD | 75.22 USD |
| `7D` | `316.40` | 11,400,000.00 USD | 11,400,000.00 USD | 0.00 USD | 16,580.00 USD | 40,060.00 USD | 61,780.00 USD |
| `7D` | `316.80` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 1,990.00 USD | 667.80 USD | 30.33 USD |
| `7D` | `317.20` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 15,590.00 USD | 748.91 USD | 44.94 USD |
| `7D` | `317.60` | 11,420,000.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 265.17 USD | 0.00 USD |
| `7D` | `317.80` | 11,440,000.00 USD | 11,440,000.00 USD | 0.00 USD | 20,490.00 USD | 0.00 USD | 0.00 USD |

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
| `5:00 UTC` | `284.50` | `284.31` | `284.50` | `284.97` | `283.70` | 270,008.97 USD | 109,559.67 USD | 160,449.29 USD | -50,889.62 USD | `-18.85%` | `21B / 25S` |

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
| `5m` | 20,210.00 USD | 75,510.00 USD | **`ACCUMULATION`** |
| `15m` | 24,470.00 USD | 165,390.00 USD | **`ACCUMULATION`** |
| `30m` | 135,850.00 USD | 700,900.00 USD | **`ACCUMULATION`** |
| `1h` | 119,040.00 USD | 777,460.00 USD | **`ACCUMULATION`** |
| `2h` | 96,950.00 USD | 867,540.00 USD | **`ACCUMULATION`** |
| `4h` | 256,570.00 USD | 594,890.00 USD | **`ACCUMULATION`** |
| `6h` | 335,490.00 USD | 1,140,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,070,000.00 USD | -481,190.00 USD | **`ACCUMULATION`** |
| `12h` | 657,800.00 USD | -383,020.00 USD | **`ACCUMULATION`** |
| `24h` | 163,180.00 USD | -1,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -138,320.00 USD | -13,050,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -13,800,000.00 USD | -137,000,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+20.21K` | 15m=`+24.47K` | 1h=`+119.04K` | 24h=`+163.18K`
* Futures Capital Netflows: 5m=`+75.51K` | 15m=`+165.39K` | 1h=`+777.46K` | 24h=`-1.61M`
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
  * `2026-10-30 15:50:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:33:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:15 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:18:15 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:17:15 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `273.07` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `269.51` (Risk Distance: `3.56` pts)
  * +2.5R Take Profit: `281.96`
  * Mathematical Lot Sizing: **`2.81 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `284.44` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `288.00` (Risk Distance: `3.56` pts)
  * +2.5R Take Profit: `275.55`
  * Mathematical Lot Sizing: **`2.81 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`286.47`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
