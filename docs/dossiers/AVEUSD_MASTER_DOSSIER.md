# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 04:50:10 IST` (`2026-10-29 23:20:10 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `119.10` | **Live Ask Quote**: `119.40` | **Mid Price**: `119.25`
- **Spread Points**: `30.00` | **Spread BPS**: `25.16 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `4` | Point: `0.0001`
  * Point Value (1.0 Lot): `0.00 USD` | Point Value (0.01 Lot): `0.0000 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `130.27` | VWAP Z-Score: `-2.56` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `2.17` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `23.87` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `143.28` | Lower -3.00σ Band: `117.26`
  * Upper +2.51σ Band: `141.15` | Lower -2.51σ Band: `119.39`
  * Upper +2.01σ Band: `138.99` | Lower -2.01σ Band: `121.55`
  * Upper +2.00σ Band: `138.94` | Lower -2.00σ Band: `121.60`
  * Upper +1.28σ Band: `135.82` | Lower -1.28σ Band: `124.72`
  * Upper +1.00σ Band: `134.61` | Lower -1.00σ Band: `125.93`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`122.81` | EMA-20=`126.14` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`129.48` (Slope: `+0.0000`) | EMA-100=`130.89`
  * Institutional Anchors: EMA-144=`131.36` | EMA-200=`131.67` (Slope: `-0.7592`) | EMA-233=`131.91`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`118.05` | Weekly High=`138.47` | Weekly Low=`118.05`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `125.93` (Distance: `-5.07%`)
  * Point of Control (POC) = `123.65` (Distance: `-3.32%`)
  * Value Area Low (VAL) = `121.62` (Distance: `-1.71%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.95` | Weekly POC=`135.13` | Weekly VAL=`131.32`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`118.05`
  * London Session (08:00-16:00 UTC): High=`119.73` | Low=`118.77`
  * New York Session (13:00-21:00 UTC): High=`119.97` | Low=`118.53`
  * Initial Balance (First Hour): IB High=`119.61` | IB Low=`118.89`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `118.77` - `119.73`
  * Optimal Trade Entry (OTE 0.705): `119.49`
  * Structural Invalidation Anchor (0.786): `120.20`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `15m` | - | - | - | - | - | 0.00 USD | 0.00 USD | `+0.00%` | 0.00 USD | `0.00` | **`BALANCED`** | Interbank Volume |

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
| --- | **`119.25`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 04:46:31 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `423` | `0x3ee5...4fab` | `LONG` | 5,187,365.80 USD | `43,303.83` | `77.35` | `119.64` | `99.19` | 1,837,675.75 USD | `+35.43%` | `10X Cross` |
| `831` | `0x0514...bdfe` | `SHORT` | 2,740,916.90 USD | `23,000.00` | `87.41` | `119.64` | `189.68` | -730,437.68 USD | `-26.65%` | `10X Cross` |
| `844` | `0xecb6...2b00` | `SHORT` | 2,706,541.88 USD | `22,547.00` | `134.87` | `119.64` | `1359.37` | 334,484.52 USD | `+12.36%` | `10X Cross` |
| `867` | `0x08c1...1135` | `LONG` | 2,615,756.00 USD | `21,836.18` | `80.89` | `119.64` | `81.76` | 849,421.65 USD | `+32.47%` | `10X Cross` |
| `1080` | `0x0996...0ba6` | `SHORT` | 2,040,170.00 USD | `17,000.00` | `107.97` | `119.64` | `196.59` | -204,596.70 USD | `-10.03%` | `3X Cross` |
| `1193` | `0x45d2...4029` | `SHORT` | 1,876,458.56 USD | `15,721.00` | `118.40` | `119.64` | `2739.56` | -15,067.38 USD | `-0.80%` | `10X Cross` |
| `1201` | `0xbfc7...80b4` | `SHORT` | 1,861,775.47 USD | `15,561.48` | `115.30` | `119.64` | `357.70` | -67,476.14 USD | `-3.62%` | `10X Cross` |
| `1206` | `0x6540...f7b7` | `LONG` | 1,845,811.50 USD | `15,450.00` | `144.44` | `119.64` | `81.24` | -385,735.75 USD | `-20.90%` | `5X Isolated` |
| `1275` | `0x07fd...689d` | `LONG` | 1,750,987.90 USD | `14,590.35` | `148.82` | `119.64` | `0.000000` | -420,405.99 USD | `-24.01%` | `10X Cross` |
| `1517` | `0xcac1...26b3` | `SHORT` | 1,432,080.00 USD | `12,000.00` | `125.37` | `119.64` | `848.98` | 72,360.86 USD | `+5.05%` | `10X Cross` |
| `1529` | `0xeadc...9d55` | `LONG` | 1,419,698.07 USD | `11,823.92` | `89.93` | `119.64` | `0.000000` | 356,341.66 USD | `+25.10%` | `10X Cross` |
| `1688` | `0x9df2...c665` | `SHORT` | 1,250,826.76 USD | `10,430.51` | `133.81` | `119.64` | `3146.51` | 144,932.26 USD | `+11.59%` | `10X Cross` |
| `1745` | `0x3dc9...54b0` | `SHORT` | 1,196,200.00 USD | `10,000.00` | `128.60` | `119.64` | `1811.69` | 89,821.83 USD | `+7.51%` | `10X Cross` |
| `1868` | `0x8af7...fa05` | `SHORT` | 1,091,209.11 USD | `9,133.75` | `131.49` | `119.64` | `2228.23` | 109,771.63 USD | `+10.06%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`126.67` (Vol: 411,400.00 USD, Dist: `+4.24%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
  * 48H Horizon: Short MP=`128.76` (Vol: 368,100.00 USD, Dist: `+5.97%`) | Long MP=`121.36` (Vol: 266,900.00 USD, Dist: `--0.12%`)
  * 3D Horizon: Short MP=`128.76` (Vol: 368,100.00 USD, Dist: `+5.97%`) | Long MP=`121.36` (Vol: 266,900.00 USD, Dist: `--0.12%`)
  * 7D Horizon: Short MP=`139.75` (Vol: 348,700.00 USD, Dist: `+15.01%`) | Long MP=`0.000000` (Vol: 0.00 USD, Dist: `-0.00%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `24.50` | 10,840.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.50` | 5,220.00 USD | 10,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.50` | 1,340.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 28,240.00 USD | 10,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 283.86 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 2,170.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 15,250.00 USD | 9,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 639.13 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 901.48 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 1,560.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 723.13 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 24,590.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.50` | 307.80 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 611.71 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 528.96 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 5,800.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 158.34 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 1,220.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 181.90 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 62,440.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,830.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,690.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 7,860.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 323.75 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 797.56 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 4,790.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 314.40 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 1,380.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,530.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 1,010.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,620.00 USD | 9,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 836.84 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 20,690.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 471.25 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 13,560.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,330.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 156.06 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 10,890.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 7,710.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `80.50` | 48,060.00 USD | 9,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 1,810,000.00 USD | 9,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 2,920.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 16,900.00 USD | 7,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 45,290.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 4,860.00 USD | 7,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,370,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 3,750.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 4,470.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 12,350.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 12,070.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 77,160.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 66,790.00 USD | 6,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 93,240.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 4,320,000.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 2,640.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 77,440.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 2,180.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,220.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 22,970.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 1,380.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 28,420.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 5,440.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 113,190.00 USD | 1,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 5,570.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 14,330.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 653,580.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 15,530.00 USD | 630,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 2,560.00 USD | 614,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 40,710.00 USD | 612,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 20,180.00 USD | 571,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 27,900.00 USD | 551,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 61,640.00 USD | 523,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 414,710.00 USD | 461,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 19,120.00 USD | 47,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 27,960.00 USD | 27,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `120.50` | 12,490.00 USD | 12,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `121.50` | 190.75 USD | 12,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `122.50` | 2,610.00 USD | 15,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `123.50` | 5,330.00 USD | 20,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `124.50` | 2,770.00 USD | 23,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `126.50` | 6,490.00 USD | 29,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `127.50` | 7,130.00 USD | 37,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `128.50` | 185.04 USD | 37,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `129.50` | 62,340.00 USD | 99,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 92,320.00 USD | 191,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 43,880.00 USD | 235,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 4,140.00 USD | 239,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 31,160.00 USD | 271,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 26,350.00 USD | 297,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `135.50` | 613.82 USD | 298,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 1,180.00 USD | 299,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 998.59 USD | 300,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 300,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 60,070.00 USD | 360,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 19,640.00 USD | 379,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 142.50 USD | 380,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 380,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `147.50` | 84,040.00 USD | 464,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `149.50` | 2,540.00 USD | 467,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 167.06 USD | 467,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 373,730.00 USD | 841,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 594,420.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 41,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 6,920.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 1,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 674.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 256.51 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 54,150.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 242,130.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 964.60 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 4,340,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 34,580.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 11,800.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 16,810.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 407,370.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `204.50` | 41,890.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 1,070.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 5,840.00 USD | 10,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `213.50` | 57,590.00 USD | 10,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `215.50` | 15,520.00 USD | 10,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 26,220.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,250.00 USD | 10,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 10,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 9,200.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 1,130.00 USD | 10,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 820,600.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 70,540.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 4,770.00 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 261.06 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 11,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `24.50` | 10,020,000.00 USD | 0.00 USD | 10,840.00 USD | `-79.60%` | `442.25` |
| `Live` | `Long` | `25.50` | 10,010,000.00 USD | 0.00 USD | 5,220.00 USD | `-78.76%` | `204.74` |
| `Live` | `Long` | `26.50` | 10,000,000.00 USD | 0.00 USD | 1,340.00 USD | `-77.93%` | `50.41` |
| `Live` | `Long` | `27.50` | 10,000,000.00 USD | 0.00 USD | 28,240.00 USD | `-77.10%` | `1,026.75` |
| `Live` | `Long` | `28.50` | 9,970,000.00 USD | 0.00 USD | 283.86 USD | `-76.27%` | `9.96` |
| `Live` | `Long` | `29.50` | 9,970,000.00 USD | 0.00 USD | 2,170.00 USD | `-75.43%` | `73.67` |
| `Live` | `Long` | `30.50` | 9,970,000.00 USD | 0.00 USD | 15,250.00 USD | `-74.60%` | `500.00` |
| `Live` | `Long` | `31.50` | 9,960,000.00 USD | 0.00 USD | 639.13 USD | `-73.77%` | `20.29` |
| `Live` | `Long` | `33.50` | 9,960,000.00 USD | 0.00 USD | 901.48 USD | `-72.10%` | `26.91` |
| `Live` | `Long` | `34.50` | 9,950,000.00 USD | 0.00 USD | 1,560.00 USD | `-71.27%` | `45.35` |
| `Live` | `Long` | `35.50` | 9,950,000.00 USD | 0.00 USD | 723.13 USD | `-70.44%` | `20.37` |
| `Live` | `Long` | `38.50` | 9,950,000.00 USD | 0.00 USD | 24,590.00 USD | `-67.94%` | `638.64` |
| `Live` | `Long` | `40.50` | 9,930,000.00 USD | 0.00 USD | 307.80 USD | `-66.27%` | `7.60` |
| `Live` | `Long` | `41.50` | 9,930,000.00 USD | 0.00 USD | 611.71 USD | `-65.44%` | `14.74` |
| `Live` | `Long` | `43.50` | 9,930,000.00 USD | 0.00 USD | 528.96 USD | `-63.77%` | `12.16` |
| `Live` | `Long` | `44.50` | 9,930,000.00 USD | 0.00 USD | 5,800.00 USD | `-62.94%` | `130.23` |
| `Live` | `Long` | `45.50` | 9,920,000.00 USD | 0.00 USD | 158.34 USD | `-62.11%` | `3.48` |
| `Live` | `Long` | `51.50` | 9,920,000.00 USD | 0.00 USD | 1,220.00 USD | `-57.11%` | `23.75` |
| `Live` | `Long` | `53.50` | 9,920,000.00 USD | 0.00 USD | 181.90 USD | `-55.45%` | `3.40` |
| `Live` | `Long` | `54.50` | 9,920,000.00 USD | 0.00 USD | 805.51 USD | `-54.61%` | `14.78` |
| `Live` | `Long` | `55.50` | 9,920,000.00 USD | 0.00 USD | 1,410.00 USD | `-53.78%` | `25.36` |
| `Live` | `Long` | `56.50` | 9,920,000.00 USD | 0.00 USD | 62,440.00 USD | `-52.95%` | `1,105.11` |
| `Live` | `Long` | `57.50` | 9,850,000.00 USD | 0.00 USD | 2,010.00 USD | `-52.12%` | `35.00` |
| `Live` | `Long` | `58.50` | 9,850,000.00 USD | 0.00 USD | 1,830.00 USD | `-51.28%` | `31.29` |
| `Live` | `Long` | `60.50` | 9,850,000.00 USD | 0.00 USD | 1,690.00 USD | `-49.62%` | `27.87` |
| `Live` | `Long` | `61.50` | 9,850,000.00 USD | 0.00 USD | 7,860.00 USD | `-48.78%` | `127.81` |
| `Live` | `Long` | `62.50` | 9,840,000.00 USD | 0.00 USD | 323.75 USD | `-47.95%` | `5.18` |
| `Live` | `Long` | `63.50` | 9,840,000.00 USD | 0.00 USD | 797.56 USD | `-47.12%` | `12.56` |
| `Live` | `Long` | `64.50` | 9,840,000.00 USD | 0.00 USD | 4,790.00 USD | `-46.29%` | `74.29` |
| `Live` | `Long` | `65.50` | 9,830,000.00 USD | 0.00 USD | 314.40 USD | `-45.45%` | `4.80` |
| `Live` | `Long` | `66.50` | 9,830,000.00 USD | 0.00 USD | 1,380.00 USD | `-44.62%` | `20.79` |
| `Live` | `Long` | `67.50` | 9,830,000.00 USD | 0.00 USD | 24,530.00 USD | `-43.79%` | `363.36` |
| `Live` | `Long` | `68.50` | 9,810,000.00 USD | 0.00 USD | 1,010.00 USD | `-42.95%` | `14.75` |
| `Live` | `Long` | `69.50` | 9,810,000.00 USD | 0.00 USD | 18,620.00 USD | `-42.12%` | `267.94` |
| `Live` | `Long` | `70.50` | 9,790,000.00 USD | 0.00 USD | 836.84 USD | `-41.29%` | `11.87` |
| `Live` | `Long` | `71.50` | 9,790,000.00 USD | 0.00 USD | 20,690.00 USD | `-40.46%` | `289.31` |
| `Live` | `Long` | `72.50` | 9,770,000.00 USD | 0.00 USD | 471.25 USD | `-39.62%` | `6.50` |
| `Live` | `Long` | `73.50` | 9,770,000.00 USD | 0.00 USD | 13,560.00 USD | `-38.79%` | `184.49` |
| `Live` | `Long` | `74.50` | 9,750,000.00 USD | 0.00 USD | 1,060.00 USD | `-37.96%` | `14.20` |
| `Live` | `Long` | `75.50` | 9,750,000.00 USD | 0.00 USD | 1,330.00 USD | `-37.13%` | `17.64` |
| `Live` | `Long` | `76.50` | 9,750,000.00 USD | 0.00 USD | 156.06 USD | `-36.29%` | `2.04` |
| `Live` | `Long` | `77.50` | 9,750,000.00 USD | 0.00 USD | 10,890.00 USD | `-35.46%` | `140.53` |
| `Live` | `Long` | `78.50` | 9,740,000.00 USD | 0.00 USD | 4,310.00 USD | `-34.63%` | `54.87` |
| `Live` | `Long` | `79.50` | 9,740,000.00 USD | 0.00 USD | 7,710.00 USD | `-33.79%` | `96.92` |
| `Live` | `Long` | `80.50` | 9,730,000.00 USD | 0.00 USD | 48,060.00 USD | `-32.96%` | `597.07` |
| `Live` | `Long` | `82.50` | 9,680,000.00 USD | 0.00 USD | 1,810,000.00 USD | `-31.30%` | `21,905.25` |
| `Live` | `Long` | `83.50` | 7,870,000.00 USD | 0.00 USD | 2,920.00 USD | `-30.46%` | `34.99` |
| `Live` | `Long` | `84.50` | 7,870,000.00 USD | 0.00 USD | 16,900.00 USD | `-29.63%` | `200.00` |
| `Live` | `Long` | `85.50` | 7,850,000.00 USD | 0.00 USD | 45,290.00 USD | `-28.80%` | `529.67` |
| `Live` | `Long` | `86.50` | 7,810,000.00 USD | 0.00 USD | 4,860.00 USD | `-27.96%` | `56.19` |
| `Live` | `Long` | `87.50` | 7,800,000.00 USD | 0.00 USD | 1,370,000.00 USD | `-27.13%` | `15,613.22` |
| `Live` | `Long` | `88.50` | 6,440,000.00 USD | 0.00 USD | 2,050.00 USD | `-26.30%` | `23.18` |
| `Live` | `Long` | `89.50` | 6,430,000.00 USD | 0.00 USD | 3,750.00 USD | `-25.47%` | `41.86` |
| `Live` | `Long` | `90.50` | 6,430,000.00 USD | 0.00 USD | 4,470.00 USD | `-24.63%` | `49.35` |
| `Live` | `Long` | `91.50` | 6,430,000.00 USD | 0.00 USD | 277,420.00 USD | `-23.80%` | `3,031.94` |
| `Live` | `Long` | `92.50` | 6,150,000.00 USD | 0.00 USD | 12,350.00 USD | `-22.97%` | `133.49` |
| `Live` | `Long` | `93.50` | 6,140,000.00 USD | 0.00 USD | 12,070.00 USD | `-22.14%` | `129.13` |
| `Live` | `Long` | `95.50` | 6,120,000.00 USD | 0.00 USD | 77,160.00 USD | `-20.47%` | `807.98` |
| `Live` | `Long` | `96.50` | 6,050,000.00 USD | 0.00 USD | 66,790.00 USD | `-19.64%` | `692.10` |
| `Live` | `Long` | `97.50` | 5,980,000.00 USD | 0.00 USD | 93,240.00 USD | `-18.80%` | `956.29` |
| `Live` | `Long` | `98.50` | 5,890,000.00 USD | 0.00 USD | 4,320,000.00 USD | `-17.97%` | `43,841.99` |
| `Live` | `Long` | `99.50` | 1,570,000.00 USD | 0.00 USD | 2,640.00 USD | `-17.14%` | `26.50` |
| `Live` | `Long` | `100.50` | 1,570,000.00 USD | 0.00 USD | 77,440.00 USD | `-16.31%` | `770.50` |
| `Live` | `Long` | `101.50` | 1,490,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.47%` | `21.47` |
| `Live` | `Long` | `102.50` | 1,490,000.00 USD | 0.00 USD | 11,220.00 USD | `-14.64%` | `109.44` |
| `Live` | `Long` | `103.50` | 1,480,000.00 USD | 0.00 USD | 22,970.00 USD | `-13.81%` | `221.93` |
| `Live` | `Long` | `104.50` | 1,450,000.00 USD | 0.00 USD | 1,380.00 USD | `-12.97%` | `13.20` |
| `Live` | `Long` | `105.50` | 1,450,000.00 USD | 0.00 USD | 28,420.00 USD | `-12.14%` | `269.35` |
| `Live` | `Long` | `106.50` | 1,420,000.00 USD | 0.00 USD | 5,440.00 USD | `-11.31%` | `51.05` |
| `Live` | `Long` | `107.50` | 1,420,000.00 USD | 0.00 USD | 113,190.00 USD | `-10.48%` | `1,052.89` |
| `Live` | `Long` | `108.50` | 1,300,000.00 USD | 0.00 USD | 5,570.00 USD | `-9.64%` | `51.33` |
| `Live` | `Long` | `109.50` | 1,300,000.00 USD | 0.00 USD | 14,330.00 USD | `-8.81%` | `130.89` |
| `Live` | `Long` | `110.50` | 1,280,000.00 USD | 0.00 USD | 653,580.00 USD | `-7.98%` | `5,914.72` |
| `Live` | `Long` | `111.50` | 630,300.00 USD | 0.00 USD | 15,530.00 USD | `-7.15%` | `139.30` |
| `Live` | `Long` | `112.50` | 614,770.00 USD | 0.00 USD | 2,560.00 USD | `-6.31%` | `22.73` |
| `Live` | `Long` | `113.50` | 612,210.00 USD | 0.00 USD | 40,710.00 USD | `-5.48%` | `358.67` |
| `Live` | `Long` | `114.50` | 571,500.00 USD | 0.00 USD | 20,180.00 USD | `-4.65%` | `176.21` |
| `Live` | `Long` | `115.50` | 551,330.00 USD | 0.00 USD | 27,900.00 USD | `-3.81%` | `241.55` |
| `Live` | `Long` | `116.50` | 523,430.00 USD | 0.00 USD | 61,640.00 USD | `-2.98%` | `529.10` |
| `Live` | `Long` | `117.50` | 461,790.00 USD | 0.00 USD | 414,710.00 USD | `-2.15%` | `3,529.41` |
| `Live` | `Long` | `118.50` | 47,080.00 USD | 0.00 USD | 19,120.00 USD | `-1.32%` | `161.32` |
| `Live` | `Long` | `119.50` | 27,960.00 USD | 0.00 USD | 27,960.00 USD | `-0.48%` | `234.01` |
| `Live` | `Short` | `120.50` | 12,490.00 USD | 12,490.00 USD | 0.00 USD | `+0.35%` | `103.64` |
| `Live` | `Short` | `121.50` | 12,680.00 USD | 190.75 USD | 0.00 USD | `+1.18%` | `1.57` |
| `Live` | `Short` | `122.50` | 15,280.00 USD | 2,610.00 USD | 0.00 USD | `+2.02%` | `21.27` |
| `Live` | `Short` | `123.50` | 20,620.00 USD | 5,330.00 USD | 0.00 USD | `+2.85%` | `43.19` |
| `Live` | `Short` | `124.50` | 23,390.00 USD | 2,770.00 USD | 0.00 USD | `+3.68%` | `22.25` |
| `Live` | `Short` | `126.50` | 29,880.00 USD | 6,490.00 USD | 0.00 USD | `+5.35%` | `51.33` |
| `Live` | `Short` | `127.50` | 37,010.00 USD | 7,130.00 USD | 0.00 USD | `+6.18%` | `55.93` |
| `Live` | `Short` | `128.50` | 37,200.00 USD | 185.04 USD | 0.00 USD | `+7.01%` | `1.44` |
| `Live` | `Short` | `129.50` | 99,540.00 USD | 62,340.00 USD | 0.00 USD | `+7.84%` | `481.41` |
| `Live` | `Short` | `130.50` | 191,860.00 USD | 92,320.00 USD | 0.00 USD | `+8.68%` | `707.40` |
| `Live` | `Short` | `131.50` | 235,730.00 USD | 43,880.00 USD | 0.00 USD | `+9.51%` | `333.67` |
| `Live` | `Short` | `132.50` | 239,880.00 USD | 4,140.00 USD | 0.00 USD | `+10.34%` | `31.26` |
| `Live` | `Short` | `133.50` | 271,030.00 USD | 31,160.00 USD | 0.00 USD | `+11.18%` | `233.38` |
| `Live` | `Short` | `134.50` | 297,390.00 USD | 26,350.00 USD | 0.00 USD | `+12.01%` | `195.93` |
| `Live` | `Short` | `135.50` | 298,000.00 USD | 613.82 USD | 0.00 USD | `+12.84%` | `4.53` |
| `Live` | `Short` | `137.50` | 299,170.00 USD | 1,180.00 USD | 0.00 USD | `+14.51%` | `8.55` |
| `Live` | `Short` | `138.50` | 300,170.00 USD | 998.59 USD | 0.00 USD | `+15.34%` | `7.21` |
| `Live` | `Short` | `139.50` | 300,270.00 USD | 100.44 USD | 0.00 USD | `+16.17%` | `0.72` |
| `Live` | `Short` | `140.50` | 360,350.00 USD | 60,070.00 USD | 0.00 USD | `+17.01%` | `427.56` |
| `Live` | `Short` | `141.50` | 379,990.00 USD | 19,640.00 USD | 0.00 USD | `+17.84%` | `138.82` |
| `Live` | `Short` | `142.50` | 380,130.00 USD | 142.50 USD | 0.00 USD | `+18.67%` | `1.00` |
| `Live` | `Short` | `145.50` | 380,860.00 USD | 731.87 USD | 0.00 USD | `+21.17%` | `5.03` |
| `Live` | `Short` | `147.50` | 464,900.00 USD | 84,040.00 USD | 0.00 USD | `+22.83%` | `569.76` |
| `Live` | `Short` | `149.50` | 467,440.00 USD | 2,540.00 USD | 0.00 USD | `+24.50%` | `16.98` |
| `Live` | `Short` | `150.50` | 467,610.00 USD | 167.06 USD | 0.00 USD | `+25.33%` | `1.11` |
| `Live` | `Short` | `151.50` | 841,340.00 USD | 373,730.00 USD | 0.00 USD | `+26.17%` | `2,466.87` |
| `Live` | `Short` | `152.50` | 1,440,000.00 USD | 594,420.00 USD | 0.00 USD | `+27.00%` | `3,897.82` |
| `Live` | `Short` | `155.50` | 1,480,000.00 USD | 41,280.00 USD | 0.00 USD | `+29.50%` | `265.46` |
| `Live` | `Short` | `158.50` | 1,480,000.00 USD | 1,480.00 USD | 0.00 USD | `+32.00%` | `9.36` |
| `Live` | `Short` | `166.50` | 1,490,000.00 USD | 6,920.00 USD | 0.00 USD | `+38.66%` | `41.58` |
| `Live` | `Short` | `167.50` | 1,490,000.00 USD | 1,580.00 USD | 0.00 USD | `+39.49%` | `9.42` |
| `Live` | `Short` | `168.50` | 1,490,000.00 USD | 995.84 USD | 0.00 USD | `+40.32%` | `5.91` |
| `Live` | `Short` | `169.50` | 1,490,000.00 USD | 1,530.00 USD | 0.00 USD | `+41.16%` | `9.00` |
| `Live` | `Short` | `171.50` | 1,490,000.00 USD | 674.00 USD | 0.00 USD | `+42.82%` | `3.93` |
| `Live` | `Short` | `174.50` | 1,490,000.00 USD | 256.51 USD | 0.00 USD | `+45.32%` | `1.47` |
| `Live` | `Short` | `175.50` | 1,500,000.00 USD | 5,620.00 USD | 0.00 USD | `+46.15%` | `32.04` |
| `Live` | `Short` | `180.50` | 1,550,000.00 USD | 54,150.00 USD | 0.00 USD | `+50.32%` | `300.00` |
| `Live` | `Short` | `181.50` | 1,790,000.00 USD | 242,130.00 USD | 0.00 USD | `+51.15%` | `1,334.03` |
| `Live` | `Short` | `183.50` | 1,790,000.00 USD | 141.30 USD | 0.00 USD | `+52.81%` | `0.77` |
| `Live` | `Short` | `185.50` | 1,790,000.00 USD | 964.60 USD | 0.00 USD | `+54.48%` | `5.20` |
| `Live` | `Short` | `187.50` | 1,800,000.00 USD | 4,230.00 USD | 0.00 USD | `+56.15%` | `22.56` |
| `Live` | `Short` | `188.50` | 6,130,000.00 USD | 4,340,000.00 USD | 0.00 USD | `+56.98%` | `23,000.00` |
| `Live` | `Short` | `189.50` | 6,130,000.00 USD | 867.91 USD | 0.00 USD | `+57.81%` | `4.58` |
| `Live` | `Short` | `191.50` | 6,140,000.00 USD | 1,500.00 USD | 0.00 USD | `+59.48%` | `7.83` |
| `Live` | `Short` | `192.50` | 6,140,000.00 USD | 358.05 USD | 0.00 USD | `+60.31%` | `1.86` |
| `Live` | `Short` | `193.50` | 6,170,000.00 USD | 34,580.00 USD | 0.00 USD | `+61.14%` | `178.70` |
| `Live` | `Short` | `196.50` | 9,510,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+63.64%` | `17,007.57` |
| `Live` | `Short` | `200.50` | 9,520,000.00 USD | 11,800.00 USD | 0.00 USD | `+66.97%` | `58.86` |
| `Live` | `Short` | `201.50` | 9,540,000.00 USD | 16,810.00 USD | 0.00 USD | `+67.80%` | `83.42` |
| `Live` | `Short` | `203.50` | 9,950,000.00 USD | 407,370.00 USD | 0.00 USD | `+69.47%` | `2,001.83` |
| `Live` | `Short` | `204.50` | 9,990,000.00 USD | 41,890.00 USD | 0.00 USD | `+70.30%` | `204.83` |
| `Live` | `Short` | `205.50` | 10,070,000.00 USD | 84,610.00 USD | 0.00 USD | `+71.14%` | `411.72` |
| `Live` | `Short` | `206.50` | 10,080,000.00 USD | 1,070.00 USD | 0.00 USD | `+71.97%` | `5.20` |
| `Live` | `Short` | `210.50` | 10,080,000.00 USD | 5,840.00 USD | 0.00 USD | `+75.30%` | `27.72` |
| `Live` | `Short` | `213.50` | 10,140,000.00 USD | 57,590.00 USD | 0.00 USD | `+77.80%` | `269.73` |
| `Live` | `Short` | `215.50` | 10,150,000.00 USD | 15,520.00 USD | 0.00 USD | `+79.46%` | `72.00` |
| `Live` | `Short` | `218.50` | 10,180,000.00 USD | 26,220.00 USD | 0.00 USD | `+81.96%` | `120.00` |
| `Live` | `Short` | `220.50` | 10,180,000.00 USD | 2,250.00 USD | 0.00 USD | `+83.63%` | `10.22` |
| `Live` | `Short` | `223.50` | 10,230,000.00 USD | 47,810.00 USD | 0.00 USD | `+86.13%` | `213.92` |
| `Live` | `Short` | `224.50` | 10,240,000.00 USD | 9,200.00 USD | 0.00 USD | `+86.96%` | `41.00` |
| `Live` | `Short` | `226.50` | 10,240,000.00 USD | 1,130.00 USD | 0.00 USD | `+88.62%` | `5.01` |
| `Live` | `Short` | `232.50` | 11,060,000.00 USD | 820,600.00 USD | 0.00 USD | `+93.62%` | `3,529.45` |
| `Live` | `Short` | `234.50` | 11,130,000.00 USD | 70,540.00 USD | 0.00 USD | `+95.29%` | `300.82` |
| `Live` | `Short` | `238.50` | 11,140,000.00 USD | 4,770.00 USD | 0.00 USD | `+98.62%` | `20.00` |
| `Live` | `Short` | `239.50` | 11,140,000.00 USD | 261.06 USD | 0.00 USD | `+99.45%` | `1.09` |
| `Live` | `Short` | `240.50` | 11,140,000.00 USD | 103.41 USD | 0.00 USD | `+100.28%` | `0.43` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Stops | Clear | - | - | - | 0.00% | SAFE (No Un-Swept Clusters) |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Exchange | Baseline | - | - | - | - | - | - |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `0 USD` | Total OI Tokens: `-`
  * 1h OI Change: `0.00%` | 4h OI Change: `0.00%` | 24h OI Change: `0.00%`
  * Exchange Breakdown: Binance=`-` | Bybit=`-` | OKX=`-` | Hyperliquid=`-`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `675.51` | Last 24h: `22.55K` | Last 3d: `65.35K` | Last 7d: `109.24K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0014%` | **USDT OKX** | `0.0001%` |
| **USDT Bybit** | `-0.0005%` | **USDT KuCoin** | `0.0053%` |
| **USDT MEXC** | `0.0014%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0002%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| Multi-TF | Interbank Desk | 50.0% | 50.0% | 1.00 | Normal Balanced Liquidity |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `125.01` | `125.79` | `125.01` | `127.83` | `123.85` | 10,015,523.95 USD | 4,623,982.97 USD | 5,391,540.98 USD | -767,558.02 USD | `-7.66%` | `13B / 27S` |
| `0:00 UTC` | `125.93` | `126.72` | `125.93` | `128.21` | `125.19` | 5,502,618.32 USD | 2,933,878.59 USD | 2,568,739.72 USD | 365,138.87 USD | `+6.64%` | `24B / 11S` |
| `5:00 UTC` | `127.23` | `128.35` | `127.23` | `129.75` | `127.07` | 4,963,273.74 USD | 2,487,328.38 USD | 2,475,945.37 USD | 11,383.01 USD | `+0.23%` | `22B / 14S` |
| `0:00 UTC` | `126.01` | `127.30` | `126.01` | `128.37` | `125.73` | 4,752,146.34 USD | 1,764,767.19 USD | 2,987,379.15 USD | -1,222,611.96 USD | `-25.73%` | `19B / 40S` |
| `5:00 UTC` | `125.60` | `125.78` | `125.60` | `127.08` | `124.86` | 6,899,831.48 USD | 3,656,346.75 USD | 3,243,484.73 USD | 412,862.03 USD | `+5.98%` | `12B / 8S` |
| `0:00 UTC` | `124.36` | `124.46` | `124.36` | `125.78` | `123.48` | 7,451,122.63 USD | 3,127,709.63 USD | 4,323,413.00 USD | -1,195,703.37 USD | `-16.05%` | `4B / 21S` |
| `5:00 UTC` | `123.61` | `123.98` | `123.61` | `125.07` | `123.01` | 4,418,811.12 USD | 2,143,156.99 USD | 2,275,654.12 USD | -132,497.13 USD | `-3.00%` | `7B / 11S` |
| `0:00 UTC` | `123.51` | `123.74` | `123.51` | `125.27` | `122.59` | 9,249,156.63 USD | 3,934,205.15 USD | 5,314,951.48 USD | -1,380,746.33 USD | `-14.93%` | `1B / 29S` |
| `5:00 UTC` | `120.00` | `120.90` | `120.00` | `123.64` | `119.36` | 18,379,971.25 USD | 8,810,374.99 USD | 9,569,596.27 USD | -759,221.28 USD | `-4.13%` | `4B / 12S` |
| `0:00 UTC` | `118.99` | `119.37` | `118.99` | `120.59` | `118.33` | 10,744,775.18 USD | 4,690,281.52 USD | 6,054,493.66 USD | -1,364,212.14 USD | `-12.70%` | `4B / 18S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:02` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `132.86` | 0.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.95` | 1,200.00 USD | 0.00 USD |
| `10-28 19:52` | `Volume 20K AAVE` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `130.77` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.5` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `130.77` | 3,200.00 USD | 0.00 USD |
| `10-28 19:42` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `131.45` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.5` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `131.08` | 3,500.00 USD | 0.00 USD |
| `10-28 19:06` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.72` | 3,400.00 USD | 0.00 USD |
| `10-28 18:47` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `131.61` | 4,500.00 USD | 0.00 USD |
| `10-28 18:36` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.46` | 1,300.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `132.24` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 20K AAVE` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `133.63` | 5,700.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `133.04` | 0.00 USD | 0.00 USD |
| `10-28 16:41` | `Range 0.5` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `134.42` | 0.00 USD | 0.00 USD |
| `10-28 15:53` | `Range 0.5` | `Divergence` | **`BULLISH`** | Drop without taker selling | `135.39` | 0.00 USD | 0.00 USD |
| `10-28 13:58` | `Volume 20K AAVE` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `136.84` | 0.00 USD | 0.00 USD |
| `10-28 13:36` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `135.33` | 3,200.00 USD | 0.00 USD |
| `10-28 11:03` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.16` | 3,800.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `134.87` | 0.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.5` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.37` | 1,400.00 USD | 0.00 USD |
| `10-28 09:16` | `Range 0.5` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `136.00` | 1,200.00 USD | 0.00 USD |
| `10-28 09:02` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `136.00` | 3,700.00 USD | 0.00 USD |
| `10-28 08:34` | `Volume 20K AAVE` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `134.67` | 3,800.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.22` | 0.00 USD | 0.00 USD |
| `10-28 08:15` | `Volume 20K AAVE` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.66` | 0.00 USD | 0.00 USD |
| `10-28 08:09` | `Range 0.5` | `Divergence` | **`BEARISH`** | Rally without taker buying | `135.15` | 0.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.5` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `135.87` | 3,900.00 USD | 0.00 USD |
| `10-28 07:26` | `Range 0.5` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `135.17` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 339,530.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | -3,900,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 0.00 USD | -6,570,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 0.00 USD | -9,210,000.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -13,170,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -13,620,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -14,060,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -14,790,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -13,800,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -53,060,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -113,880,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+339.53K` | 15m=`-1.27M` | 1h=`-6.57M` | 24h=`-13.80M`
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
  * `2026-10-30 04:15:34 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:41:34 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:40:34 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:42:34 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:42:34 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:42:34 IST`: [fxstreet.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `121.62` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `118.56` (Risk Distance: `3.06` pts)
  * +2.5R Take Profit: `129.26`
  * Mathematical Lot Sizing: **`3.27 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `125.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `128.99` (Risk Distance: `3.06` pts)
  * +2.5R Take Profit: `118.29`
  * Mathematical Lot Sizing: **`3.27 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`120.20`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
