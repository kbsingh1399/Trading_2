# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 00:59:36 IST` (`2026-10-29 19:29:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `133.38` | **Live Ask Quote**: `133.63` | **Mid Price**: `133.50`
- **Spread Points**: `25.00` | **Spread BPS**: `18.73 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE LIMIT ONLY` | **Order Type Allowed**: `BUY_LIMIT / SELL_LIMIT`
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
  * Session VWAP: `132.40` | VWAP Z-Score: `+0.27` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.08` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `44.79` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `138.98` | Lower -3.00σ Band: `125.81`
  * Upper +2.51σ Band: `137.90` | Lower -2.51σ Band: `126.89`
  * Upper +2.01σ Band: `136.81` | Lower -2.01σ Band: `127.99`
  * Upper +2.00σ Band: `136.79` | Lower -2.00σ Band: `128.01`
  * Upper +1.28σ Band: `135.21` | Lower -1.28σ Band: `129.59`
  * Upper +1.00σ Band: `134.59` | Lower -1.00σ Band: `130.20`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`133.56` | EMA-20=`133.86` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`133.24` (Slope: `+0.0000`) | EMA-100=`132.87`
  * Institutional Anchors: EMA-144=`132.81` | EMA-200=`132.80` (Slope: `+0.1198`) | EMA-233=`132.77`
- **Range Boundaries**: 24H High=`138.47` | 24H Low=`128.25` | Weekly High=`138.47` | Weekly Low=`128.25`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `136.70` (Distance: `-2.34%`)
  * Point of Control (POC) = `132.93` (Distance: `+0.43%`)
  * Value Area Low (VAL) = `130.92` (Distance: `+1.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`135.85` | POC=`134.70` | VAL=`132.04`
  * Prior Day Extremes: PDH=`138.47` | PDL=`129.42` | PDC=`134.07`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`135.91` | Weekly POC=`134.76` | Weekly VAL=`131.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`135.37` | Low=`128.25`
  * London Session (08:00-16:00 UTC): High=`133.60` | Low=`129.16`
  * New York Session (13:00-21:00 UTC): High=`137.67` | Low=`130.09`
  * Initial Balance (First Hour): IB High=`131.85` | IB Low=`129.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `132.97` - `134.04`
  * Optimal Trade Entry (OTE 0.705): `133.77`
  * Structural Invalidation Anchor (0.786): `134.57`

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
| --- | **`133.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 00:53:52 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `406` | `0x3ee5...4fab` | `LONG` | 5,794,052.45 USD | `43,303.83` | `77.35` | `133.78` | `114.65` | 2,444,362.41 USD | `+42.19%` | `10X Cross` |
| `766` | `0x0514...bdfe` | `SHORT` | 3,076,020.00 USD | `23,000.00` | `87.41` | `133.78` | `183.89` | -1,065,540.78 USD | `-34.64%` | `10X Cross` |
| `805` | `0x08c1...1135` | `LONG` | 2,921,680.88 USD | `21,836.18` | `80.89` | `133.78` | `94.23` | 1,155,346.53 USD | `+39.54%` | `10X Cross` |
| `1004` | `0x0996...0ba6` | `SHORT` | 2,273,658.20 USD | `17,000.00` | `107.97` | `133.78` | `196.59` | -438,084.90 USD | `-19.27%` | `3X Cross` |
| `1071` | `0x45d2...4029` | `SHORT` | 2,102,641.30 USD | `15,721.00` | `118.40` | `133.78` | `2374.55` | -241,250.12 USD | `-11.47%` | `10X Cross` |
| `1085` | `0xbfc7...80b4` | `SHORT` | 2,080,725.49 USD | `15,561.48` | `115.30` | `133.78` | `416.26` | -286,426.17 USD | `-13.77%` | `10X Cross` |
| `1179` | `0x6540...f7b7` | `LONG` | 1,950,976.49 USD | `14,587.34` | `145.70` | `133.78` | `91.04` | -174,467.86 USD | `-8.94%` | `5X Isolated` |
| `1265` | `0x07fd...689d` | `LONG` | 1,818,961.33 USD | `13,600.26` | `150.55` | `133.78` | `0.000000` | -228,610.80 USD | `-12.57%` | `10X Cross` |
| `1427` | `0xcac1...26b3` | `SHORT` | 1,604,935.20 USD | `12,000.00` | `125.37` | `133.78` | `777.28` | -100,494.34 USD | `-6.26%` | `10X Cross` |
| `1441` | `0xeadc...9d55` | `LONG` | 1,579,912.19 USD | `11,823.92` | `89.93` | `133.78` | `0.000000` | 516,555.78 USD | `+32.70%` | `10X Cross` |
| `1584` | `0x9df2...c665` | `SHORT` | 1,408,764.68 USD | `10,532.82` | `133.81` | `133.78` | `2832.07` | 684.96 USD | `+0.05%` | `10X Cross` |
| `1642` | `0x3dc9...54b0` | `SHORT` | 1,337,500.00 USD | `10,000.00` | `128.60` | `133.78` | `1530.85` | -51,478.17 USD | `-3.85%` | `10X Cross` |
| `1754` | `0x8af7...fa05` | `SHORT` | 1,221,588.83 USD | `9,133.75` | `131.49` | `133.78` | `2210.70` | -20,608.08 USD | `-1.69%` | `10X Cross` |
| `1916` | `0x72db...8bb6` | `LONG` | 1,069,920.00 USD | `8,000.00` | `180.99` | `133.78` | `0.000000` | -378,037.43 USD | `-35.33%` | `10X Cross` |
| `1986` | `0x12d2...f97f` | `LONG` | 1,026,599.48 USD | `7,675.82` | `143.31` | `133.78` | `0.000000` | -73,393.25 USD | `-7.15%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`138.85` (Vol: 128,600.00 USD, Dist: `+4.10%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.50%`)
  * 48H Horizon: Short MP=`140.15` (Vol: 183,800.00 USD, Dist: `+5.08%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.50%`)
  * 3D Horizon: Short MP=`140.15` (Vol: 159,300.00 USD, Dist: `+5.08%`) | Long MP=`128.71` (Vol: 206,000.00 USD, Dist: `--3.50%`)
  * 7D Horizon: Short MP=`140.55` (Vol: 267,100.00 USD, Dist: `+5.38%`) | Long MP=`127.34` (Vol: 265,000.00 USD, Dist: `--4.53%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `29.50` | 118.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 621.29 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 5,520.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.50` | 380.89 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 3,630.00 USD | 10,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 519.82 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 5,180.00 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 726.27 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.50` | 716.83 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 10,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 1,410.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `57.50` | 2,010.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 5,850.00 USD | 10,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `59.50` | 390.92 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 134,480.00 USD | 10,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 653.75 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 13,150.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 2,350.00 USD | 10,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,320.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 2,310.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 18,510.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 202.34 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 13,210.00 USD | 10,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,820.00 USD | 10,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 26,490.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,340.00 USD | 10,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 6,790.00 USD | 10,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 134.47 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 543.59 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 8,530.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 45,160.00 USD | 10,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,610.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 20,650.00 USD | 10,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 2,050.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 4,300.00 USD | 10,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 68,770.00 USD | 10,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 1,610,000.00 USD | 10,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 68,600.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 9,260.00 USD | 8,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 2,070,000.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 13,290.00 USD | 6,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 12,030.00 USD | 6,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 97,940.00 USD | 6,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 45,460.00 USD | 6,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 946.25 USD | 6,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 966.81 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 11,850.00 USD | 6,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 4,750.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 1,060.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 37,780.00 USD | 6,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 14,600.00 USD | 6,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 40,630.00 USD | 6,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 253,200.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 15,810.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 606,920.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 3,720.00 USD | 5,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 12,520.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 105,940.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,970,000.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 12,940.00 USD | 461,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 60,290.00 USD | 448,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 148,710.00 USD | 388,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 11,320.00 USD | 239,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 781.53 USD | 228,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 14,670.00 USD | 227,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 8,410.00 USD | 212,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `122.50` | 21,960.00 USD | 204,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `123.50` | 19,920.00 USD | 182,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `124.50` | 28,580.00 USD | 162,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `125.50` | 33,530.00 USD | 134,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `126.50` | 68,130.00 USD | 100,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `127.50` | 4,730.00 USD | 32,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `128.50` | 24,290.00 USD | 27,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `129.50` | 1,500.00 USD | 3,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `130.50` | 1,860.00 USD | 1,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 2,580.00 USD | 2,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 100.44 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 387,950.00 USD | 390,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 4,710.00 USD | 395,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 869.25 USD | 396,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 21,680.00 USD | 417,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 1,210.00 USD | 419,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 731.87 USD | 419,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 88,250.00 USD | 508,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 237.85 USD | 508,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `152.50` | 595,110.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 1,900.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,820.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 1,580.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `168.50` | 995.84 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 138.99 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 252.34 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 870.97 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `174.50` | 31,180.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 5,620.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 1,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `182.50` | 54,750.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 269.75 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 4,250,000.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 678,760.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 17,730.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 2,570.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `191.50` | 1,500.00 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `192.50` | 358.05 USD | 6,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `193.50` | 1,820.00 USD | 6,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 10,540.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `197.50` | 8,100.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 9,850.00 USD | 9,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `201.50` | 60,450.00 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 9,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 84,610.00 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `209.50` | 190.65 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 9,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `217.50` | 21,580.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `218.50` | 44,760.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `221.50` | 930.30 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `223.50` | 47,810.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 261.58 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,310.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `233.50` | 226.50 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 192.29 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `238.50` | 4,770.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `239.50` | 24,110.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 103.41 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `241.50` | 550.62 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 3,890.00 USD | 9,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `249.50` | 1,310.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `250.50` | 273.05 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `251.50` | 281.68 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `253.50` | 139.43 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `254.50` | 6,970.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `255.50` | 424.13 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `257.50` | 2,480.00 USD | 9,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `260.50` | 15,630.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `262.50` | 763.88 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `263.50` | 532.27 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `265.50` | 8,510.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `29.50` | 10,920,000.00 USD | 0.00 USD | 118.00 USD | `-77.88%` | `4.00` |
| `Live` | `Long` | `30.50` | 10,920,000.00 USD | 0.00 USD | 621.29 USD | `-77.13%` | `20.37` |
| `Live` | `Long` | `32.50` | 10,920,000.00 USD | 0.00 USD | 5,520.00 USD | `-75.63%` | `169.83` |
| `Live` | `Long` | `33.50` | 10,920,000.00 USD | 0.00 USD | 380.89 USD | `-74.88%` | `11.37` |
| `Live` | `Long` | `38.50` | 10,920,000.00 USD | 0.00 USD | 3,630.00 USD | `-71.14%` | `94.31` |
| `Live` | `Long` | `43.50` | 10,910,000.00 USD | 0.00 USD | 519.82 USD | `-67.39%` | `11.95` |
| `Live` | `Long` | `45.50` | 10,910,000.00 USD | 0.00 USD | 5,180.00 USD | `-65.89%` | `113.84` |
| `Live` | `Long` | `47.50` | 10,910,000.00 USD | 0.00 USD | 726.27 USD | `-64.39%` | `15.29` |
| `Live` | `Long` | `48.50` | 10,910,000.00 USD | 0.00 USD | 716.83 USD | `-63.64%` | `14.78` |
| `Live` | `Long` | `54.50` | 10,910,000.00 USD | 0.00 USD | 805.51 USD | `-59.14%` | `14.78` |
| `Live` | `Long` | `55.50` | 10,900,000.00 USD | 0.00 USD | 1,410.00 USD | `-58.39%` | `25.36` |
| `Live` | `Long` | `56.50` | 10,900,000.00 USD | 0.00 USD | 1,510.00 USD | `-57.64%` | `26.66` |
| `Live` | `Long` | `57.50` | 10,900,000.00 USD | 0.00 USD | 2,010.00 USD | `-56.89%` | `35.00` |
| `Live` | `Long` | `58.50` | 10,900,000.00 USD | 0.00 USD | 5,850.00 USD | `-56.14%` | `99.96` |
| `Live` | `Long` | `59.50` | 10,890,000.00 USD | 0.00 USD | 390.92 USD | `-55.39%` | `6.57` |
| `Live` | `Long` | `60.50` | 10,890,000.00 USD | 0.00 USD | 134,480.00 USD | `-54.64%` | `2,222.78` |
| `Live` | `Long` | `61.50` | 10,760,000.00 USD | 0.00 USD | 168.51 USD | `-53.89%` | `2.74` |
| `Live` | `Long` | `62.50` | 10,760,000.00 USD | 0.00 USD | 653.75 USD | `-53.14%` | `10.46` |
| `Live` | `Long` | `63.50` | 10,760,000.00 USD | 0.00 USD | 13,150.00 USD | `-52.39%` | `207.10` |
| `Live` | `Long` | `66.50` | 10,750,000.00 USD | 0.00 USD | 2,350.00 USD | `-50.14%` | `35.29` |
| `Live` | `Long` | `67.50` | 10,740,000.00 USD | 0.00 USD | 24,320.00 USD | `-49.39%` | `360.30` |
| `Live` | `Long` | `68.50` | 10,720,000.00 USD | 0.00 USD | 2,310.00 USD | `-48.64%` | `33.73` |
| `Live` | `Long` | `69.50` | 10,720,000.00 USD | 0.00 USD | 18,510.00 USD | `-47.89%` | `266.40` |
| `Live` | `Long` | `70.50` | 10,700,000.00 USD | 0.00 USD | 202.34 USD | `-47.14%` | `2.87` |
| `Live` | `Long` | `71.50` | 10,700,000.00 USD | 0.00 USD | 13,210.00 USD | `-46.39%` | `184.76` |
| `Live` | `Long` | `73.50` | 10,680,000.00 USD | 0.00 USD | 11,820.00 USD | `-44.89%` | `160.80` |
| `Live` | `Long` | `74.50` | 10,670,000.00 USD | 0.00 USD | 26,490.00 USD | `-44.14%` | `355.59` |
| `Live` | `Long` | `75.50` | 10,650,000.00 USD | 0.00 USD | 1,340.00 USD | `-43.39%` | `17.72` |
| `Live` | `Long` | `77.50` | 10,640,000.00 USD | 0.00 USD | 9,050.00 USD | `-41.90%` | `116.79` |
| `Live` | `Long` | `78.50` | 10,640,000.00 USD | 0.00 USD | 4,310.00 USD | `-41.15%` | `54.87` |
| `Live` | `Long` | `79.50` | 10,630,000.00 USD | 0.00 USD | 6,790.00 USD | `-40.40%` | `85.43` |
| `Live` | `Long` | `82.50` | 10,620,000.00 USD | 0.00 USD | 134.47 USD | `-38.15%` | `1.63` |
| `Live` | `Long` | `83.50` | 10,620,000.00 USD | 0.00 USD | 543.59 USD | `-37.40%` | `6.51` |
| `Live` | `Long` | `84.50` | 10,620,000.00 USD | 0.00 USD | 8,530.00 USD | `-36.65%` | `100.91` |
| `Live` | `Long` | `85.50` | 10,620,000.00 USD | 0.00 USD | 45,160.00 USD | `-35.90%` | `528.17` |
| `Live` | `Long` | `86.50` | 10,570,000.00 USD | 0.00 USD | 1,610.00 USD | `-35.15%` | `18.61` |
| `Live` | `Long` | `87.50` | 10,570,000.00 USD | 0.00 USD | 20,650.00 USD | `-34.40%` | `236.02` |
| `Live` | `Long` | `88.50` | 10,550,000.00 USD | 0.00 USD | 2,050.00 USD | `-33.65%` | `23.18` |
| `Live` | `Long` | `89.50` | 10,550,000.00 USD | 0.00 USD | 4,300.00 USD | `-32.90%` | `48.05` |
| `Live` | `Long` | `90.50` | 10,540,000.00 USD | 0.00 USD | 68,770.00 USD | `-32.15%` | `759.87` |
| `Live` | `Long` | `91.50` | 10,470,000.00 USD | 0.00 USD | 1,610,000.00 USD | `-31.40%` | `17,645.86` |
| `Live` | `Long` | `92.50` | 8,860,000.00 USD | 0.00 USD | 68,600.00 USD | `-30.65%` | `741.63` |
| `Live` | `Long` | `93.50` | 8,790,000.00 USD | 0.00 USD | 9,260.00 USD | `-29.90%` | `99.05` |
| `Live` | `Long` | `94.50` | 8,780,000.00 USD | 0.00 USD | 2,070,000.00 USD | `-29.15%` | `21,863.27` |
| `Live` | `Long` | `95.50` | 6,710,000.00 USD | 0.00 USD | 13,290.00 USD | `-28.40%` | `139.19` |
| `Live` | `Long` | `96.50` | 6,700,000.00 USD | 0.00 USD | 12,030.00 USD | `-27.65%` | `124.67` |
| `Live` | `Long` | `97.50` | 6,690,000.00 USD | 0.00 USD | 97,940.00 USD | `-26.90%` | `1,004.56` |
| `Live` | `Long` | `98.50` | 6,590,000.00 USD | 0.00 USD | 45,460.00 USD | `-26.15%` | `461.55` |
| `Live` | `Long` | `99.50` | 6,550,000.00 USD | 0.00 USD | 946.25 USD | `-25.40%` | `9.51` |
| `Live` | `Long` | `100.50` | 6,540,000.00 USD | 0.00 USD | 966.81 USD | `-24.65%` | `9.62` |
| `Live` | `Long` | `102.50` | 6,540,000.00 USD | 0.00 USD | 11,850.00 USD | `-23.15%` | `115.59` |
| `Live` | `Long` | `103.50` | 6,530,000.00 USD | 0.00 USD | 4,750.00 USD | `-22.40%` | `45.85` |
| `Live` | `Long` | `104.50` | 6,530,000.00 USD | 0.00 USD | 1,060.00 USD | `-21.65%` | `10.11` |
| `Live` | `Long` | `105.50` | 6,530,000.00 USD | 0.00 USD | 37,780.00 USD | `-20.90%` | `358.10` |
| `Live` | `Long` | `106.50` | 6,490,000.00 USD | 0.00 USD | 14,600.00 USD | `-20.15%` | `137.12` |
| `Live` | `Long` | `107.50` | 6,470,000.00 USD | 0.00 USD | 40,630.00 USD | `-19.40%` | `377.94` |
| `Live` | `Long` | `108.50` | 6,430,000.00 USD | 0.00 USD | 253,200.00 USD | `-18.65%` | `2,333.64` |
| `Live` | `Long` | `109.50` | 6,180,000.00 USD | 0.00 USD | 15,810.00 USD | `-17.90%` | `144.39` |
| `Live` | `Long` | `110.50` | 6,160,000.00 USD | 0.00 USD | 606,920.00 USD | `-17.15%` | `5,492.51` |
| `Live` | `Long` | `111.50` | 5,560,000.00 USD | 0.00 USD | 3,720.00 USD | `-16.40%` | `33.36` |
| `Live` | `Long` | `112.50` | 5,550,000.00 USD | 0.00 USD | 12,520.00 USD | `-15.65%` | `111.32` |
| `Live` | `Long` | `113.50` | 5,540,000.00 USD | 0.00 USD | 105,940.00 USD | `-14.90%` | `933.39` |
| `Live` | `Long` | `114.50` | 5,430,000.00 USD | 0.00 USD | 4,970,000.00 USD | `-14.16%` | `43,433.27` |
| `Live` | `Long` | `115.50` | 461,610.00 USD | 0.00 USD | 12,940.00 USD | `-13.41%` | `112.00` |
| `Live` | `Long` | `116.50` | 448,680.00 USD | 0.00 USD | 60,290.00 USD | `-12.66%` | `517.51` |
| `Live` | `Long` | `117.50` | 388,390.00 USD | 0.00 USD | 148,710.00 USD | `-11.91%` | `1,265.65` |
| `Live` | `Long` | `118.50` | 239,670.00 USD | 0.00 USD | 11,320.00 USD | `-11.16%` | `95.51` |
| `Live` | `Long` | `119.50` | 228,360.00 USD | 0.00 USD | 781.53 USD | `-10.41%` | `6.54` |
| `Live` | `Long` | `120.50` | 227,570.00 USD | 0.00 USD | 14,670.00 USD | `-9.66%` | `121.77` |
| `Live` | `Long` | `121.50` | 212,900.00 USD | 0.00 USD | 8,410.00 USD | `-8.91%` | `69.21` |
| `Live` | `Long` | `122.50` | 204,490.00 USD | 0.00 USD | 21,960.00 USD | `-8.16%` | `179.23` |
| `Live` | `Long` | `123.50` | 182,540.00 USD | 0.00 USD | 19,920.00 USD | `-7.41%` | `161.28` |
| `Live` | `Long` | `124.50` | 162,620.00 USD | 0.00 USD | 28,580.00 USD | `-6.66%` | `229.56` |
| `Live` | `Long` | `125.50` | 134,040.00 USD | 0.00 USD | 33,530.00 USD | `-5.91%` | `267.20` |
| `Live` | `Long` | `126.50` | 100,510.00 USD | 0.00 USD | 68,130.00 USD | `-5.16%` | `538.54` |
| `Live` | `Long` | `127.50` | 32,380.00 USD | 0.00 USD | 4,730.00 USD | `-4.41%` | `37.12` |
| `Live` | `Long` | `128.50` | 27,650.00 USD | 0.00 USD | 24,290.00 USD | `-3.66%` | `189.02` |
| `Live` | `Long` | `129.50` | 3,360.00 USD | 0.00 USD | 1,500.00 USD | `-2.91%` | `11.60` |
| `Live` | `Long` | `130.50` | 1,860.00 USD | 0.00 USD | 1,860.00 USD | `-2.16%` | `14.22` |
| `Live` | `Short` | `133.50` | 2,580.00 USD | 2,580.00 USD | 0.00 USD | `+0.09%` | `19.34` |
| `Live` | `Short` | `139.50` | 2,680.00 USD | 100.44 USD | 0.00 USD | `+4.59%` | `0.72` |
| `Live` | `Short` | `140.50` | 390,630.00 USD | 387,950.00 USD | 0.00 USD | `+5.34%` | `2,761.19` |
| `Live` | `Short` | `141.50` | 395,340.00 USD | 4,710.00 USD | 0.00 USD | `+6.09%` | `33.30` |
| `Live` | `Short` | `142.50` | 396,210.00 USD | 869.25 USD | 0.00 USD | `+6.84%` | `6.10` |
| `Live` | `Short` | `143.50` | 417,890.00 USD | 21,680.00 USD | 0.00 USD | `+7.59%` | `151.09` |
| `Live` | `Short` | `144.50` | 419,100.00 USD | 1,210.00 USD | 0.00 USD | `+8.34%` | `8.37` |
| `Live` | `Short` | `145.50` | 419,830.00 USD | 731.87 USD | 0.00 USD | `+9.09%` | `5.03` |
| `Live` | `Short` | `150.50` | 508,080.00 USD | 88,250.00 USD | 0.00 USD | `+12.84%` | `586.35` |
| `Live` | `Short` | `151.50` | 508,320.00 USD | 237.85 USD | 0.00 USD | `+13.59%` | `1.57` |
| `Live` | `Short` | `152.50` | 1,100,000.00 USD | 595,110.00 USD | 0.00 USD | `+14.33%` | `3,902.35` |
| `Live` | `Short` | `155.50` | 1,110,000.00 USD | 1,900.00 USD | 0.00 USD | `+16.58%` | `12.22` |
| `Live` | `Short` | `158.50` | 1,110,000.00 USD | 1,820.00 USD | 0.00 USD | `+18.83%` | `11.47` |
| `Live` | `Short` | `167.50` | 1,110,000.00 USD | 1,580.00 USD | 0.00 USD | `+25.58%` | `9.42` |
| `Live` | `Short` | `168.50` | 1,110,000.00 USD | 995.84 USD | 0.00 USD | `+26.33%` | `5.91` |
| `Live` | `Short` | `169.50` | 1,110,000.00 USD | 138.99 USD | 0.00 USD | `+27.08%` | `0.82` |
| `Live` | `Short` | `170.50` | 1,110,000.00 USD | 252.34 USD | 0.00 USD | `+27.83%` | `1.48` |
| `Live` | `Short` | `173.50` | 1,110,000.00 USD | 870.97 USD | 0.00 USD | `+30.08%` | `5.02` |
| `Live` | `Short` | `174.50` | 1,140,000.00 USD | 31,180.00 USD | 0.00 USD | `+30.83%` | `178.70` |
| `Live` | `Short` | `175.50` | 1,150,000.00 USD | 5,620.00 USD | 0.00 USD | `+31.58%` | `32.04` |
| `Live` | `Short` | `181.50` | 1,150,000.00 USD | 2,170.00 USD | 0.00 USD | `+36.08%` | `11.93` |
| `Live` | `Short` | `182.50` | 1,200,000.00 USD | 54,750.00 USD | 0.00 USD | `+36.83%` | `300.00` |
| `Live` | `Short` | `183.50` | 1,200,000.00 USD | 269.75 USD | 0.00 USD | `+37.58%` | `1.47` |
| `Live` | `Short` | `184.50` | 5,450,000.00 USD | 4,250,000.00 USD | 0.00 USD | `+38.33%` | `23,029.73` |
| `Live` | `Short` | `186.50` | 6,130,000.00 USD | 678,760.00 USD | 0.00 USD | `+39.83%` | `3,639.45` |
| `Live` | `Short` | `187.50` | 6,150,000.00 USD | 17,730.00 USD | 0.00 USD | `+40.58%` | `94.56` |
| `Live` | `Short` | `189.50` | 6,150,000.00 USD | 2,570.00 USD | 0.00 USD | `+42.08%` | `13.58` |
| `Live` | `Short` | `191.50` | 6,150,000.00 USD | 1,500.00 USD | 0.00 USD | `+43.57%` | `7.83` |
| `Live` | `Short` | `192.50` | 6,150,000.00 USD | 358.05 USD | 0.00 USD | `+44.32%` | `1.86` |
| `Live` | `Short` | `193.50` | 6,160,000.00 USD | 1,820.00 USD | 0.00 USD | `+45.07%` | `9.42` |
| `Live` | `Short` | `194.50` | 6,170,000.00 USD | 10,540.00 USD | 0.00 USD | `+45.82%` | `54.20` |
| `Live` | `Short` | `196.50` | 9,510,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+47.32%` | `17,000.00` |
| `Live` | `Short` | `197.50` | 9,520,000.00 USD | 8,100.00 USD | 0.00 USD | `+48.07%` | `41.00` |
| `Live` | `Short` | `200.50` | 9,530,000.00 USD | 9,850.00 USD | 0.00 USD | `+50.32%` | `49.15` |
| `Live` | `Short` | `201.50` | 9,590,000.00 USD | 60,450.00 USD | 0.00 USD | `+51.07%` | `300.00` |
| `Live` | `Short` | `203.50` | 9,590,000.00 USD | 372.41 USD | 0.00 USD | `+52.57%` | `1.83` |
| `Live` | `Short` | `205.50` | 9,670,000.00 USD | 84,610.00 USD | 0.00 USD | `+54.07%` | `411.72` |
| `Live` | `Short` | `209.50` | 9,670,000.00 USD | 190.65 USD | 0.00 USD | `+57.07%` | `0.91` |
| `Live` | `Short` | `210.50` | 9,670,000.00 USD | 151.56 USD | 0.00 USD | `+57.82%` | `0.72` |
| `Live` | `Short` | `217.50` | 9,690,000.00 USD | 21,580.00 USD | 0.00 USD | `+63.07%` | `99.20` |
| `Live` | `Short` | `218.50` | 9,740,000.00 USD | 44,760.00 USD | 0.00 USD | `+63.82%` | `204.83` |
| `Live` | `Short` | `220.50` | 9,740,000.00 USD | 2,000.00 USD | 0.00 USD | `+65.32%` | `9.06` |
| `Live` | `Short` | `221.50` | 9,740,000.00 USD | 930.30 USD | 0.00 USD | `+66.07%` | `4.20` |
| `Live` | `Short` | `223.50` | 9,790,000.00 USD | 47,810.00 USD | 0.00 USD | `+67.57%` | `213.92` |
| `Live` | `Short` | `225.50` | 9,790,000.00 USD | 261.58 USD | 0.00 USD | `+69.07%` | `1.16` |
| `Live` | `Short` | `230.50` | 9,790,000.00 USD | 2,310.00 USD | 0.00 USD | `+72.81%` | `10.00` |
| `Live` | `Short` | `233.50` | 9,790,000.00 USD | 226.50 USD | 0.00 USD | `+75.06%` | `0.97` |
| `Live` | `Short` | `234.50` | 9,790,000.00 USD | 192.29 USD | 0.00 USD | `+75.81%` | `0.82` |
| `Live` | `Short` | `238.50` | 9,800,000.00 USD | 4,770.00 USD | 0.00 USD | `+78.81%` | `20.00` |
| `Live` | `Short` | `239.50` | 9,820,000.00 USD | 24,110.00 USD | 0.00 USD | `+79.56%` | `100.65` |
| `Live` | `Short` | `240.50` | 9,820,000.00 USD | 103.41 USD | 0.00 USD | `+80.31%` | `0.43` |
| `Live` | `Short` | `241.50` | 9,820,000.00 USD | 550.62 USD | 0.00 USD | `+81.06%` | `2.28` |
| `Live` | `Short` | `242.50` | 9,820,000.00 USD | 3,890.00 USD | 0.00 USD | `+81.81%` | `16.05` |
| `Live` | `Short` | `249.50` | 9,830,000.00 USD | 1,310.00 USD | 0.00 USD | `+87.06%` | `5.26` |
| `Live` | `Short` | `250.50` | 9,830,000.00 USD | 273.05 USD | 0.00 USD | `+87.81%` | `1.09` |
| `Live` | `Short` | `251.50` | 9,830,000.00 USD | 281.68 USD | 0.00 USD | `+88.56%` | `1.12` |
| `Live` | `Short` | `253.50` | 9,830,000.00 USD | 139.43 USD | 0.00 USD | `+90.06%` | `0.55` |
| `Live` | `Short` | `254.50` | 9,830,000.00 USD | 6,970.00 USD | 0.00 USD | `+90.81%` | `27.37` |
| `Live` | `Short` | `255.50` | 9,830,000.00 USD | 424.13 USD | 0.00 USD | `+91.56%` | `1.66` |
| `Live` | `Short` | `257.50` | 9,840,000.00 USD | 2,480.00 USD | 0.00 USD | `+93.06%` | `9.62` |
| `Live` | `Short` | `260.50` | 9,850,000.00 USD | 15,630.00 USD | 0.00 USD | `+95.31%` | `60.00` |
| `Live` | `Short` | `262.50` | 9,850,000.00 USD | 763.88 USD | 0.00 USD | `+96.81%` | `2.91` |
| `Live` | `Short` | `263.50` | 9,850,000.00 USD | 532.27 USD | 0.00 USD | `+97.56%` | `2.02` |
| `Live` | `Short` | `265.50` | 9,860,000.00 USD | 8,510.00 USD | 0.00 USD | `+99.06%` | `32.05` |

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
  * Current Rate: `960.88` | Last 24h: `22.61K` | Last 3d: `65.36K` | Last 7d: `109.21K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0036%` | **USDT OKX** | `0.0005%` |
| **USDT Bybit** | `-0.0040%` | **USDT KuCoin** | `0.0099%` |
| **USDT MEXC** | `0.0036%` | **USDT BingX** | `0.0036%` |
| **USDT Gate** | `-0.0029%` | **USDT Bitget** | `0.0032%` |
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
| `0:00 UTC` | `135.20` | `135.14` | `135.20` | `135.91` | `134.62` | 2,622,608.21 USD | 1,514,994.17 USD | 1,107,614.04 USD | 407,380.13 USD | `+15.53%` | `12B / 29S` |
| `5:00 UTC` | `134.62` | `134.76` | `134.62` | `135.20` | `134.44` | 878,992.69 USD | 464,259.89 USD | 414,732.80 USD | 49,527.10 USD | `+5.63%` | `10B / 8S` |
| `0:00 UTC` | `134.09` | `134.61` | `134.09` | `135.59` | `133.75` | 1,172,719.65 USD | 442,820.23 USD | 729,899.42 USD | -287,079.19 USD | `-24.48%` | `18B / 51S` |
| `5:00 UTC` | `133.19` | `133.34` | `133.19` | `134.06` | `132.89` | 1,323,282.70 USD | 549,454.30 USD | 773,828.40 USD | -224,374.10 USD | `-16.96%` | `12B / 26S` |
| `0:00 UTC` | `133.56` | `133.83` | `133.56` | `134.20` | `133.47` | 796,111.43 USD | 359,258.65 USD | 436,852.78 USD | -77,594.12 USD | `-9.75%` | `11B / 15S` |
| `5:00 UTC` | `133.20` | `133.55` | `133.20` | `134.30` | `133.09` | 867,640.21 USD | 417,158.29 USD | 450,481.92 USD | -33,323.63 USD | `-3.84%` | `18B / 33S` |
| `0:00 UTC` | `132.41` | `132.56` | `132.41` | `133.26` | `132.25` | 1,157,375.29 USD | 569,704.83 USD | 587,670.46 USD | -17,965.63 USD | `-1.55%` | `10B / 20S` |
| `5:00 UTC` | `133.31` | `133.18` | `133.31` | `133.78` | `132.50` | 863,735.20 USD | 576,212.05 USD | 287,523.15 USD | 288,688.91 USD | `+33.42%` | `50B / 11S` |
| `0:00 UTC` | `133.14` | `133.20` | `133.14` | `133.66` | `132.88` | 686,449.89 USD | 420,178.59 USD | 266,271.31 USD | 153,907.28 USD | `+22.42%` | `14B / 10S` |
| `5:00 UTC` | `133.47` | `133.32` | `133.47` | `133.47` | `133.05` | 370,465.04 USD | 282,762.89 USD | 87,702.15 USD | 195,060.74 USD | `+52.65%` | `12B / 5S` |

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
| `5m` | 0.00 USD | 280,490.00 USD | **`ACCUMULATION`** |
| `15m` | 0.00 USD | 450,300.00 USD | **`ACCUMULATION`** |
| `30m` | 0.00 USD | 583,130.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 621,260.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | -270,590.00 USD | **`DISTRIBUTION`** |
| `4h` | 0.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 0.00 USD | -1,020,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -1,270,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -154,230.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -2,610,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -39,430,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -99,520,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`+280.49K` | 15m=`+450.30K` | 1h=`+621.26K` | 24h=`-2.61M`
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
  * `2026-10-30 00:48:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 00:17:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@DeItaone] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@mb_ghalibaf] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 00:49:09 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 00:48:09 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 21:50:09 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 20:50:09 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)


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
  * Execution Entry: `130.92` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `129.25` (Risk Distance: `1.67` pts)
  * +2.5R Take Profit: `135.10`
  * Mathematical Lot Sizing: **`5.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `136.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `138.37` (Risk Distance: `1.67` pts)
  * +2.5R Take Profit: `132.52`
  * Mathematical Lot Sizing: **`5.98 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`134.57`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
