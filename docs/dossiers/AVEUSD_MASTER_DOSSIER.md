# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 02:39:45 IST` (`2026-10-29 21:09:45 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `123.56` | **Live Ask Quote**: `127.46` | **Mid Price**: `125.51`
- **Spread Points**: `390.00` | **Spread BPS**: `310.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `131.92` | VWAP Z-Score: `-3.12` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `1.66` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `16.75` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `140.03` | Lower -3.00σ Band: `123.81`
  * Upper +2.51σ Band: `138.70` | Lower -2.51σ Band: `125.14`
  * Upper +2.01σ Band: `137.35` | Lower -2.01σ Band: `126.49`
  * Upper +2.00σ Band: `137.33` | Lower -2.00σ Band: `126.52`
  * Upper +1.28σ Band: `135.38` | Lower -1.28σ Band: `128.46`
  * Upper +1.00σ Band: `134.62` | Lower -1.00σ Band: `129.22`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`129.81` | EMA-20=`131.74` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`132.46` (Slope: `+0.0000`) | EMA-100=`132.51`
  * Institutional Anchors: EMA-144=`132.54` | EMA-200=`132.57` (Slope: `-0.1128`) | EMA-233=`132.65`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`122.01` | Weekly High=`138.47` | Weekly Low=`122.01`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `123.91` (Distance: `+1.79%`)
  * Point of Control (POC) = `123.50` (Distance: `+2.12%`)
  * Value Area Low (VAL) = `123.50` (Distance: `+2.12%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.89` | Weekly POC=`135.12` | Weekly VAL=`131.61`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`124.09` | Low=`123.50`
  * London Session (08:00-16:00 UTC): High=`126.01` | Low=`125.01`
  * New York Session (13:00-21:00 UTC): High=`126.26` | Low=`124.76`
  * Initial Balance (First Hour): IB High=`125.89` | IB Low=`125.13`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `125.01` - `126.01`
  * Optimal Trade Entry (OTE 0.705): `125.76`
  * Structural Invalidation Anchor (0.786): `126.51`

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
| `BID/ASK` | None | `0.0000` | 0.00 USD | `0.00%` | Unarmored | `0.0%` | Interbank L2 | NONE |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 02:35:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `416` | `0x3ee5...4fab` | `LONG` | 5,475,336.27 USD | `43,303.83` | `77.35` | `126.89` | `98.52` | 2,125,646.22 USD | `+38.82%` | `10X Cross` |
| `783` | `0x0514...bdfe` | `SHORT` | 2,908,120.00 USD | `23,000.00` | `87.41` | `126.89` | `190.22` | -897,640.78 USD | `-30.87%` | `10X Cross` |
| `791` | `0x08c1...1135` | `LONG` | 2,873,859.65 USD | `21,836.18` | `80.89` | `126.89` | `93.12` | 1,107,525.30 USD | `+38.54%` | `10X Cross` |
| `1026` | `0x0996...0ba6` | `SHORT` | 2,139,960.00 USD | `17,000.00` | `107.97` | `126.89` | `196.59` | -304,386.70 USD | `-14.22%` | `3X Cross` |
| `1113` | `0x45d2...4029` | `SHORT` | 1,974,714.81 USD | `15,721.00` | `118.40` | `126.89` | `2703.25` | -113,323.63 USD | `-5.74%` | `10X Cross` |
| `1129` | `0xbfc7...80b4` | `SHORT` | 1,964,948.08 USD | `15,561.48` | `115.30` | `126.89` | `471.75` | -170,648.76 USD | `-8.68%` | `10X Cross` |
| `1179` | `0x6540...f7b7` | `LONG` | 1,884,071.07 USD | `14,994.00` | `145.17` | `126.89` | `89.04` | -292,643.58 USD | `-15.53%` | `5X Isolated` |
| `1249` | `0x07fd...689d` | `LONG` | 1,790,014.22 USD | `14,150.31` | `149.67` | `126.89` | `0.000000` | -327,911.52 USD | `-18.32%` | `10X Cross` |
| `1452` | `0xcac1...26b3` | `SHORT` | 1,516,680.00 USD | `12,000.00` | `125.37` | `126.89` | `819.93` | -12,239.14 USD | `-0.81%` | `10X Cross` |
| `1471` | `0xeadc...9d55` | `LONG` | 1,490,878.07 USD | `11,823.92` | `89.93` | `126.89` | `0.000000` | 427,521.66 USD | `+28.68%` | `10X Cross` |
| `1611` | `0x9df2...c665` | `SHORT` | 1,321,257.98 USD | `10,450.51` | `133.81` | `126.89` | `3065.10` | 77,177.34 USD | `+5.84%` | `10X Cross` |
| `1666` | `0x3dc9...54b0` | `SHORT` | 1,263,100.00 USD | `10,000.00` | `128.60` | `126.89` | `1774.80` | 22,921.83 USD | `+1.81%` | `10X Cross` |
| `1778` | `0x8af7...fa05` | `SHORT` | 1,146,924.99 USD | `9,133.75` | `131.49` | `126.89` | `2221.90` | 54,055.76 USD | `+4.71%` | `10X Cross` |
| `1947` | `0x72db...8bb6` | `LONG` | 1,011,520.00 USD | `8,000.00` | `180.99` | `126.89` | `0.000000` | -436,437.43 USD | `-43.15%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`138.79` (Vol: 138,600.00 USD, Dist: `+5.34%`) | Long MP=`128.68` (Vol: 206,000.00 USD, Dist: `--2.34%`)
  * 48H Horizon: Short MP=`140.15` (Vol: 183,800.00 USD, Dist: `+6.37%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--2.31%`)
  * 3D Horizon: Short MP=`140.15` (Vol: 159,300.00 USD, Dist: `+6.37%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--2.31%`)
  * 7D Horizon: Short MP=`140.55` (Vol: 267,100.00 USD, Dist: `+6.67%`) | Long MP=`127.34` (Vol: 265,000.00 USD, Dist: `--3.36%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `29.50` | 118.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 346.78 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.50` | 641.66 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 3,570.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.50` | 5,410.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 862.78 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 4,400.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 5,180.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 854.03 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 1,200.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 4,570.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,880.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 134,680.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 493.23 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 2,270.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 3,860.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 741.11 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 2,600.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 2,050.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,510.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 202.34 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 36,910.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 12,100.00 USD | 10,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,800.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,050.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,610.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 134.47 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 543.59 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 51,060.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 2,430.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 23,110.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 65,710.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 4,420.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 1,530.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 1,610,000.00 USD | 10,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 68,600.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 9,260.00 USD | 8,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,070,000.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 13,290.00 USD | 6,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 15,660.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 101,730.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 37,160.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 1,850.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 966.81 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,850.00 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 4,940.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 7,890.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 30,560.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 14,600.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 40,630.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 11,720.00 USD | 6,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 259,520.00 USD | 6,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 607,360.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 2,470.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 12,940.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 106,790.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,970,000.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 12,940.00 USD | 462,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 62,050.00 USD | 450,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 146,940.00 USD | 387,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 11,320.00 USD | 241,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 781.53 USD | 229,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 14,670.00 USD | 228,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 7,060.00 USD | 214,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 27,400.00 USD | 207,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 16,050.00 USD | 179,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 29,590.00 USD | 163,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 31,640.00 USD | 134,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 70,160.00 USD | 102,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `127.50` | 4,730.00 USD | 32,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 24,290.00 USD | 27,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `129.50` | 1,500.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 1,860.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 100.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 388,080.00 USD | 388,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 4,050.00 USD | 392,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 869.25 USD | 393,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 21,680.00 USD | 414,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 1,210.00 USD | 415,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 416,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 88,250.00 USD | 504,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 237.85 USD | 505,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 595,110.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 1,900.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `156.50` | 1,050.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,820.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 138.99 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 252.34 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 31,880.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 54,750.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 4,230,000.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 22,260.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 671,480.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 867.91 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 2,640.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 9,720.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,350,000.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 70,190.00 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 9,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `219.50` | 921.90 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 46,190.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 262.74 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 2,290.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 525.54 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 225.53 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 3,330.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `235.50` | 23,700.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 1,250.00 USD | 9,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 4,770.00 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 647.48 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `250.50` | 553.61 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `253.50` | 139.43 USD | 9,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `254.50` | 6,970.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `255.50` | 1,400.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `257.50` | 2,480.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `262.50` | 763.88 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `263.50` | 24,790.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `25.50` | 10,430,000.00 USD | 0.00 USD | 397.04 USD | `-79.72%` | `15.57` |
| `Live` | `Long` | `26.50` | 10,430,000.00 USD | 0.00 USD | 828.66 USD | `-78.92%` | `31.27` |
| `Live` | `Long` | `27.50` | 10,430,000.00 USD | 0.00 USD | 17,400.00 USD | `-78.12%` | `632.60` |
| `Live` | `Long` | `29.50` | 10,410,000.00 USD | 0.00 USD | 7,070.00 USD | `-76.53%` | `239.58` |
| `Live` | `Long` | `30.50` | 10,400,000.00 USD | 0.00 USD | 345.26 USD | `-75.74%` | `11.32` |
| `Live` | `Long` | `31.50` | 10,400,000.00 USD | 0.00 USD | 101.11 USD | `-74.94%` | `3.21` |
| `Live` | `Long` | `33.50` | 10,400,000.00 USD | 0.00 USD | 1,520.00 USD | `-73.35%` | `45.35` |
| `Live` | `Long` | `34.50` | 10,400,000.00 USD | 0.00 USD | 304.29 USD | `-72.56%` | `8.82` |
| `Live` | `Long` | `36.50` | 10,400,000.00 USD | 0.00 USD | 743.50 USD | `-70.96%` | `20.37` |
| `Live` | `Long` | `38.50` | 10,400,000.00 USD | 0.00 USD | 384.23 USD | `-69.37%` | `9.98` |
| `Live` | `Long` | `39.50` | 10,400,000.00 USD | 0.00 USD | 5,140.00 USD | `-68.58%` | `130.23` |
| `Live` | `Long` | `43.50` | 10,400,000.00 USD | 0.00 USD | 1,130.00 USD | `-65.40%` | `26.04` |
| `Live` | `Long` | `44.50` | 10,400,000.00 USD | 0.00 USD | 364.90 USD | `-64.60%` | `8.20` |
| `Live` | `Long` | `45.50` | 10,390,000.00 USD | 0.00 USD | 158.34 USD | `-63.81%` | `3.48` |
| `Live` | `Long` | `46.50` | 10,390,000.00 USD | 0.00 USD | 8,370.00 USD | `-63.01%` | `180.00` |
| `Live` | `Long` | `51.50` | 10,390,000.00 USD | 0.00 USD | 175.10 USD | `-59.03%` | `3.40` |
| `Live` | `Long` | `52.50` | 10,390,000.00 USD | 0.00 USD | 4,800.00 USD | `-58.24%` | `91.49` |
| `Live` | `Long` | `54.50` | 10,380,000.00 USD | 0.00 USD | 5,010.00 USD | `-56.65%` | `91.99` |
| `Live` | `Long` | `55.50` | 10,380,000.00 USD | 0.00 USD | 1,410.00 USD | `-55.85%` | `25.36` |
| `Live` | `Long` | `56.50` | 10,370,000.00 USD | 0.00 USD | 6,710.00 USD | `-55.06%` | `118.73` |
| `Live` | `Long` | `57.50` | 10,370,000.00 USD | 0.00 USD | 3,700.00 USD | `-54.26%` | `64.38` |
| `Live` | `Long` | `58.50` | 10,360,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.46%` | `27.49` |
| `Live` | `Long` | `60.50` | 10,360,000.00 USD | 0.00 USD | 4,270.00 USD | `-51.87%` | `70.50` |
| `Live` | `Long` | `61.50` | 10,360,000.00 USD | 0.00 USD | 168.51 USD | `-51.08%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,360,000.00 USD | 0.00 USD | 323.75 USD | `-50.28%` | `5.18` |
| `Live` | `Long` | `63.50` | 10,360,000.00 USD | 0.00 USD | 488.95 USD | `-49.49%` | `7.70` |
| `Live` | `Long` | `64.50` | 10,360,000.00 USD | 0.00 USD | 423.77 USD | `-48.69%` | `6.57` |
| `Live` | `Long` | `65.50` | 10,360,000.00 USD | 0.00 USD | 782.72 USD | `-47.90%` | `11.95` |
| `Live` | `Long` | `66.50` | 10,360,000.00 USD | 0.00 USD | 2,350.00 USD | `-47.10%` | `35.29` |
| `Live` | `Long` | `67.50` | 10,350,000.00 USD | 0.00 USD | 31,310.00 USD | `-46.30%` | `463.92` |
| `Live` | `Long` | `69.50` | 10,320,000.00 USD | 0.00 USD | 18,620.00 USD | `-44.71%` | `267.94` |
| `Live` | `Long` | `70.50` | 10,300,000.00 USD | 0.00 USD | 4,850.00 USD | `-43.92%` | `68.80` |
| `Live` | `Long` | `71.50` | 10,300,000.00 USD | 0.00 USD | 13,210.00 USD | `-43.12%` | `184.76` |
| `Live` | `Long` | `73.50` | 10,290,000.00 USD | 0.00 USD | 15,580.00 USD | `-41.53%` | `211.93` |
| `Live` | `Long` | `74.50` | 10,270,000.00 USD | 0.00 USD | 2,080.00 USD | `-40.74%` | `27.90` |
| `Live` | `Long` | `75.50` | 10,270,000.00 USD | 0.00 USD | 1,050.00 USD | `-39.94%` | `13.87` |
| `Live` | `Long` | `77.50` | 10,270,000.00 USD | 0.00 USD | 10,600.00 USD | `-38.35%` | `136.79` |
| `Live` | `Long` | `78.50` | 10,260,000.00 USD | 0.00 USD | 4,460.00 USD | `-37.55%` | `56.78` |
| `Live` | `Long` | `79.50` | 10,250,000.00 USD | 0.00 USD | 6,790.00 USD | `-36.76%` | `85.43` |
| `Live` | `Long` | `80.50` | 10,250,000.00 USD | 0.00 USD | 4,180.00 USD | `-35.96%` | `51.93` |
| `Live` | `Long` | `81.50` | 10,240,000.00 USD | 0.00 USD | 539.53 USD | `-35.17%` | `6.62` |
| `Live` | `Long` | `82.50` | 10,240,000.00 USD | 0.00 USD | 134.47 USD | `-34.37%` | `1.63` |
| `Live` | `Long` | `83.50` | 10,240,000.00 USD | 0.00 USD | 50,440.00 USD | `-33.58%` | `604.06` |
| `Live` | `Long` | `84.50` | 10,190,000.00 USD | 0.00 USD | 21,120.00 USD | `-32.78%` | `250.00` |
| `Live` | `Long` | `85.50` | 10,170,000.00 USD | 0.00 USD | 53,710.00 USD | `-31.99%` | `628.17` |
| `Live` | `Long` | `86.50` | 10,120,000.00 USD | 0.00 USD | 14,020.00 USD | `-31.19%` | `162.03` |
| `Live` | `Long` | `87.50` | 10,100,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-30.40%` | `22,008.53` |
| `Live` | `Long` | `88.50` | 8,180,000.00 USD | 0.00 USD | 2,050.00 USD | `-29.60%` | `23.18` |
| `Live` | `Long` | `89.50` | 8,170,000.00 USD | 0.00 USD | 4,300.00 USD | `-28.80%` | `48.05` |
| `Live` | `Long` | `90.50` | 8,170,000.00 USD | 0.00 USD | 878.76 USD | `-28.01%` | `9.71` |
| `Live` | `Long` | `91.50` | 8,170,000.00 USD | 0.00 USD | 276,890.00 USD | `-27.21%` | `3,026.15` |
| `Live` | `Long` | `92.50` | 7,890,000.00 USD | 0.00 USD | 1,400,000.00 USD | `-26.42%` | `15,144.51` |
| `Live` | `Long` | `93.50` | 6,490,000.00 USD | 0.00 USD | 9,020.00 USD | `-25.62%` | `96.51` |
| `Live` | `Long` | `94.50` | 6,480,000.00 USD | 0.00 USD | 72,480.00 USD | `-24.83%` | `766.96` |
| `Live` | `Long` | `95.50` | 6,410,000.00 USD | 0.00 USD | 7,130.00 USD | `-24.03%` | `74.65` |
| `Live` | `Long` | `96.50` | 6,400,000.00 USD | 0.00 USD | 16,960.00 USD | `-23.24%` | `175.75` |
| `Live` | `Long` | `97.50` | 6,380,000.00 USD | 0.00 USD | 90,730.00 USD | `-22.44%` | `930.53` |
| `Live` | `Long` | `98.50` | 6,290,000.00 USD | 0.00 USD | 39,660.00 USD | `-21.65%` | `402.60` |
| `Live` | `Long` | `99.50` | 6,250,000.00 USD | 0.00 USD | 7,820.00 USD | `-20.85%` | `78.57` |
| `Live` | `Long` | `100.50` | 6,250,000.00 USD | 0.00 USD | 966.81 USD | `-20.05%` | `9.62` |
| `Live` | `Long` | `101.50` | 6,250,000.00 USD | 0.00 USD | 73,000.00 USD | `-19.26%` | `719.25` |
| `Live` | `Long` | `102.50` | 6,170,000.00 USD | 0.00 USD | 10,270.00 USD | `-18.46%` | `100.24` |
| `Live` | `Long` | `103.50` | 6,160,000.00 USD | 0.00 USD | 7,000.00 USD | `-17.67%` | `67.62` |
| `Live` | `Long` | `104.50` | 6,160,000.00 USD | 0.00 USD | 2,030.00 USD | `-16.87%` | `19.38` |
| `Live` | `Long` | `105.50` | 6,150,000.00 USD | 0.00 USD | 44,090.00 USD | `-16.08%` | `417.90` |
| `Live` | `Long` | `106.50` | 6,110,000.00 USD | 0.00 USD | 17,750.00 USD | `-15.28%` | `166.66` |
| `Live` | `Long` | `107.50` | 6,090,000.00 USD | 0.00 USD | 48,540.00 USD | `-14.49%` | `451.54` |
| `Live` | `Long` | `108.50` | 6,040,000.00 USD | 0.00 USD | 12,130.00 USD | `-13.69%` | `111.76` |
| `Live` | `Long` | `109.50` | 6,030,000.00 USD | 0.00 USD | 82,400.00 USD | `-12.89%` | `752.53` |
| `Live` | `Long` | `110.50` | 5,950,000.00 USD | 0.00 USD | 605,490.00 USD | `-12.10%` | `5,479.53` |
| `Live` | `Long` | `111.50` | 5,340,000.00 USD | 0.00 USD | 6,680.00 USD | `-11.30%` | `59.90` |
| `Live` | `Long` | `112.50` | 5,340,000.00 USD | 0.00 USD | 39,300.00 USD | `-10.51%` | `349.30` |
| `Live` | `Long` | `113.50` | 5,300,000.00 USD | 0.00 USD | 120,550.00 USD | `-9.71%` | `1,062.09` |
| `Live` | `Long` | `114.50` | 5,180,000.00 USD | 0.00 USD | 4,880.00 USD | `-8.92%` | `42.66` |
| `Live` | `Long` | `115.50` | 5,170,000.00 USD | 0.00 USD | 5,020,000.00 USD | `-8.12%` | `43,444.08` |
| `Live` | `Long` | `116.50` | 153,900.00 USD | 0.00 USD | 60,120.00 USD | `-7.33%` | `516.07` |
| `Live` | `Long` | `117.50` | 93,770.00 USD | 0.00 USD | 7,750.00 USD | `-6.53%` | `66.00` |
| `Live` | `Long` | `118.50` | 86,020.00 USD | 0.00 USD | 11,320.00 USD | `-5.74%` | `95.51` |
| `Live` | `Long` | `119.50` | 74,700.00 USD | 0.00 USD | 2,170.00 USD | `-4.94%` | `18.14` |
| `Live` | `Long` | `120.50` | 72,530.00 USD | 0.00 USD | 12,510.00 USD | `-4.14%` | `103.83` |
| `Live` | `Long` | `121.50` | 60,020.00 USD | 0.00 USD | 7,900.00 USD | `-3.35%` | `65.03` |
| `Live` | `Long` | `122.50` | 52,120.00 USD | 0.00 USD | 22,090.00 USD | `-2.55%` | `180.33` |
| `Live` | `Long` | `123.50` | 30,030.00 USD | 0.00 USD | 17,970.00 USD | `-1.76%` | `145.51` |
| `Live` | `Long` | `124.50` | 12,060.00 USD | 0.00 USD | 12,060.00 USD | `-0.96%` | `96.87` |
| `Live` | `Short` | `127.50` | 3,480.00 USD | 3,480.00 USD | 0.00 USD | `+1.42%` | `27.30` |
| `Live` | `Short` | `130.50` | 5,240.00 USD | 1,760.00 USD | 0.00 USD | `+3.81%` | `13.49` |
| `Live` | `Short` | `131.50` | 26,590.00 USD | 21,350.00 USD | 0.00 USD | `+4.61%` | `162.33` |
| `Live` | `Short` | `132.50` | 32,420.00 USD | 5,830.00 USD | 0.00 USD | `+5.40%` | `44.01` |
| `Live` | `Short` | `133.50` | 44,310.00 USD | 11,890.00 USD | 0.00 USD | `+6.20%` | `89.06` |
| `Live` | `Short` | `134.50` | 46,080.00 USD | 1,780.00 USD | 0.00 USD | `+6.99%` | `13.20` |
| `Live` | `Short` | `139.50` | 48,120.00 USD | 2,040.00 USD | 0.00 USD | `+10.97%` | `14.61` |
| `Live` | `Short` | `140.50` | 416,440.00 USD | 368,320.00 USD | 0.00 USD | `+11.77%` | `2,621.46` |
| `Live` | `Short` | `141.50` | 417,440.00 USD | 998.99 USD | 0.00 USD | `+12.56%` | `7.06` |
| `Live` | `Short` | `143.50` | 417,590.00 USD | 156.42 USD | 0.00 USD | `+14.15%` | `1.09` |
| `Live` | `Short` | `145.50` | 418,320.00 USD | 731.87 USD | 0.00 USD | `+15.74%` | `5.03` |
| `Live` | `Short` | `146.50` | 422,620.00 USD | 4,290.00 USD | 0.00 USD | `+16.54%` | `29.30` |
| `Live` | `Short` | `147.50` | 509,330.00 USD | 86,710.00 USD | 0.00 USD | `+17.33%` | `587.87` |
| `Live` | `Short` | `149.50` | 518,490.00 USD | 9,160.00 USD | 0.00 USD | `+18.92%` | `61.27` |
| `Live` | `Short` | `150.50` | 518,650.00 USD | 167.06 USD | 0.00 USD | `+19.72%` | `1.11` |
| `Live` | `Short` | `151.50` | 518,890.00 USD | 237.85 USD | 0.00 USD | `+20.52%` | `1.57` |
| `Live` | `Short` | `152.50` | 1,110,000.00 USD | 594,660.00 USD | 0.00 USD | `+21.31%` | `3,899.39` |
| `Live` | `Short` | `155.50` | 1,120,000.00 USD | 1,900.00 USD | 0.00 USD | `+23.70%` | `12.22` |
| `Live` | `Short` | `158.50` | 1,120,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.08%` | `9.36` |
| `Live` | `Short` | `167.50` | 1,120,000.00 USD | 1,580.00 USD | 0.00 USD | `+33.24%` | `9.42` |
| `Live` | `Short` | `168.50` | 1,120,000.00 USD | 995.84 USD | 0.00 USD | `+34.04%` | `5.91` |
| `Live` | `Short` | `172.50` | 1,120,000.00 USD | 1,810.00 USD | 0.00 USD | `+37.22%` | `10.47` |
| `Live` | `Short` | `175.50` | 1,130,000.00 USD | 5,620.00 USD | 0.00 USD | `+39.61%` | `32.04` |
| `Live` | `Short` | `178.50` | 1,180,000.00 USD | 53,550.00 USD | 0.00 USD | `+41.99%` | `300.00` |
| `Live` | `Short` | `179.50` | 1,180,000.00 USD | 1,420.00 USD | 0.00 USD | `+42.79%` | `7.91` |
| `Live` | `Short` | `181.50` | 1,180,000.00 USD | 2,170.00 USD | 0.00 USD | `+44.38%` | `11.93` |
| `Live` | `Short` | `183.50` | 1,190,000.00 USD | 954.20 USD | 0.00 USD | `+45.97%` | `5.20` |
| `Live` | `Short` | `186.50` | 1,840,000.00 USD | 656,380.00 USD | 0.00 USD | `+48.36%` | `3,519.45` |
| `Live` | `Short` | `187.50` | 1,880,000.00 USD | 37,740.00 USD | 0.00 USD | `+49.15%` | `201.26` |
| `Live` | `Short` | `189.50` | 1,880,000.00 USD | 867.91 USD | 0.00 USD | `+50.74%` | `4.58` |
| `Live` | `Short` | `190.50` | 6,260,000.00 USD | 4,380,000.00 USD | 0.00 USD | `+51.54%` | `23,000.00` |
| `Live` | `Short` | `191.50` | 6,260,000.00 USD | 1,500.00 USD | 0.00 USD | `+52.33%` | `7.83` |
| `Live` | `Short` | `192.50` | 6,260,000.00 USD | 358.05 USD | 0.00 USD | `+53.13%` | `1.86` |
| `Live` | `Short` | `193.50` | 6,260,000.00 USD | 286.38 USD | 0.00 USD | `+53.93%` | `1.48` |
| `Live` | `Short` | `194.50` | 6,270,000.00 USD | 1,510.00 USD | 0.00 USD | `+54.72%` | `7.76` |
| `Live` | `Short` | `195.50` | 6,310,000.00 USD | 40,040.00 USD | 0.00 USD | `+55.52%` | `204.83` |
| `Live` | `Short` | `196.50` | 9,650,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+56.31%` | `17,000.00` |
| `Live` | `Short` | `200.50` | 9,660,000.00 USD | 9,850.00 USD | 0.00 USD | `+59.49%` | `49.15` |
| `Live` | `Short` | `203.50` | 9,660,000.00 USD | 5,870.00 USD | 0.00 USD | `+61.88%` | `28.83` |
| `Live` | `Short` | `204.50` | 9,660,000.00 USD | 1,060.00 USD | 0.00 USD | `+62.68%` | `5.20` |
| `Live` | `Short` | `205.50` | 9,750,000.00 USD | 84,610.00 USD | 0.00 USD | `+63.47%` | `411.72` |
| `Live` | `Short` | `207.50` | 9,760,000.00 USD | 14,940.00 USD | 0.00 USD | `+65.06%` | `72.00` |
| `Live` | `Short` | `208.50` | 9,790,000.00 USD | 25,020.00 USD | 0.00 USD | `+65.86%` | `120.00` |
| `Live` | `Short` | `210.50` | 9,790,000.00 USD | 151.56 USD | 0.00 USD | `+67.45%` | `0.72` |
| `Live` | `Short` | `216.50` | 9,800,000.00 USD | 8,880.00 USD | 0.00 USD | `+72.22%` | `41.00` |
| `Live` | `Short` | `220.50` | 9,800,000.00 USD | 2,000.00 USD | 0.00 USD | `+75.40%` | `9.06` |
| `Live` | `Short` | `223.50` | 9,850,000.00 USD | 47,810.00 USD | 0.00 USD | `+77.79%` | `213.92` |
| `Live` | `Short` | `225.50` | 9,910,000.00 USD | 67,650.00 USD | 0.00 USD | `+79.38%` | `300.00` |
| `Live` | `Short` | `234.50` | 9,920,000.00 USD | 2,540.00 USD | 0.00 USD | `+86.54%` | `10.82` |
| `Live` | `Short` | `239.50` | 9,920,000.00 USD | 4,790.00 USD | 0.00 USD | `+90.52%` | `20.00` |
| `Live` | `Short` | `240.50` | 9,920,000.00 USD | 666.19 USD | 0.00 USD | `+91.31%` | `2.77` |
| `Live` | `Short` | `241.50` | 9,920,000.00 USD | 263.24 USD | 0.00 USD | `+92.11%` | `1.09` |
| `Live` | `Short` | `242.50` | 9,920,000.00 USD | 928.77 USD | 0.00 USD | `+92.90%` | `3.83` |
| `Live` | `Short` | `247.50` | 9,920,000.00 USD | 240.07 USD | 0.00 USD | `+96.88%` | `0.97` |
| `Live` | `Short` | `248.50` | 9,920,000.00 USD | 278.32 USD | 0.00 USD | `+97.68%` | `1.12` |
| `Live` | `Short` | `251.50` | 9,940,000.00 USD | 15,090.00 USD | 0.00 USD | `+100.06%` | `60.00` |

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
  * Current Rate: `-2.00K` | Last 24h: `22.55K` | Last 3d: `65.35K` | Last 7d: `109.24K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0007%` | **USDT OKX** | `-0.0047%` |
| **USDT Bybit** | `-0.0036%` | **USDT KuCoin** | `0.0003%` |
| **USDT MEXC** | `-0.0005%` | **USDT BingX** | `0.0045%` |
| **USDT Gate** | `-0.0055%` | **USDT Bitget** | `0.0050%` |
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
| `5:00 UTC` | `133.31` | `133.18` | `133.31` | `133.78` | `132.50` | 863,735.20 USD | 576,212.05 USD | 287,523.15 USD | 288,688.91 USD | `+33.42%` | `50B / 11S` |
| `0:00 UTC` | `133.14` | `133.20` | `133.14` | `133.66` | `132.88` | 686,449.89 USD | 420,178.59 USD | 266,271.31 USD | 153,907.28 USD | `+22.42%` | `14B / 10S` |
| `5:00 UTC` | `133.47` | `133.44` | `133.47` | `133.81` | `133.05` | 660,168.83 USD | 435,970.69 USD | 224,198.14 USD | 211,772.54 USD | `+32.08%` | `21B / 10S` |
| `0:00 UTC` | `134.05` | `133.79` | `134.05` | `134.09` | `133.39` | 579,547.95 USD | 318,932.27 USD | 260,615.68 USD | 58,316.59 USD | `+10.06%` | `9B / 8S` |
| `5:00 UTC` | `133.55` | `133.56` | `133.55` | `133.86` | `133.31` | 433,946.57 USD | 185,142.03 USD | 248,804.53 USD | -63,662.50 USD | `-14.67%` | `3B / 10S` |
| `0:00 UTC` | `131.00` | `131.60` | `131.00` | `133.52` | `130.52` | 3,297,985.22 USD | 1,608,197.36 USD | 1,689,787.86 USD | -81,590.50 USD | `-2.47%` | `14B / 29S` |
| `5:00 UTC` | `131.94` | `131.88` | `131.94` | `132.34` | `131.47` | 1,452,091.89 USD | 903,261.06 USD | 548,830.83 USD | 354,430.23 USD | `+24.41%` | `32B / 12S` |
| `0:00 UTC` | `127.08` | `128.36` | `127.08` | `132.12` | `125.96` | 9,241,707.96 USD | 3,635,148.90 USD | 5,606,559.06 USD | -1,971,410.16 USD | `-21.33%` | `6B / 35S` |
| `5:00 UTC` | `125.01` | `125.79` | `125.01` | `127.83` | `123.85` | 10,015,523.95 USD | 4,623,982.97 USD | 5,391,540.98 USD | -767,558.02 USD | `-7.66%` | `13B / 27S` |
| `0:00 UTC` | `125.93` | `125.95` | `125.93` | `126.63` | `125.19` | 1,501,499.24 USD | 985,645.28 USD | 515,853.96 USD | 469,791.33 USD | `+31.29%` | `34B / 14S` |

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
| `5m` | 13,720.00 USD | 489,430.00 USD | **`ACCUMULATION`** |
| `15m` | 154,090.00 USD | -117,200.00 USD | **`ACCUMULATION`** |
| `30m` | -2,120,000.00 USD | -5,020,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -2,580,000.00 USD | -4,590,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -3,010,000.00 USD | -4,420,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,310,000.00 USD | -4,940,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,330,000.00 USD | -5,980,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -4,710,000.00 USD | -5,610,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -4,330,000.00 USD | -5,600,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -5,970,000.00 USD | -6,550,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -27,020,000.00 USD | -43,800,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -114,850,000.00 USD | -106,240,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+13.72K` | 15m=`+154.09K` | 1h=`-2.58M` | 24h=`-5.97M`
* Futures Capital Netflows: 5m=`+489.43K` | 15m=`-117.20K` | 1h=`-4.59M` | 24h=`-6.55M`
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
  * `2026-10-30 02:15:26 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:35:26 IST`: [sec.gov] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:31:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 02:30:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 23:32:26 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:32:26 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:32:26 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)


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
  * Execution Entry: `123.50` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `115.65` (Risk Distance: `7.85` pts)
  * +2.5R Take Profit: `143.12`
  * Mathematical Lot Sizing: **`1.27 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `123.91` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `131.76` (Risk Distance: `7.85` pts)
  * +2.5R Take Profit: `104.29`
  * Mathematical Lot Sizing: **`1.27 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`126.51`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
