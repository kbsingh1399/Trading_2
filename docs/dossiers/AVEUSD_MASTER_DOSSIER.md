# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 14:29:40 IST` (`2026-10-30 08:59:40 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `124.61` | **Live Ask Quote**: `124.91` | **Mid Price**: `124.76`
- **Spread Points**: `30.00` | **Spread BPS**: `24.05 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `121.92` | VWAP Z-Score: `+0.85` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.10` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.82` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `131.91` | Lower -3.00σ Band: `111.94`
  * Upper +2.51σ Band: `130.28` | Lower -2.51σ Band: `113.57`
  * Upper +2.01σ Band: `128.61` | Lower -2.01σ Band: `115.23`
  * Upper +2.00σ Band: `128.58` | Lower -2.00σ Band: `115.27`
  * Upper +1.28σ Band: `126.18` | Lower -1.28σ Band: `117.66`
  * Upper +1.00σ Band: `125.25` | Lower -1.00σ Band: `118.60`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`125.14` | EMA-20=`124.80` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`125.04` (Slope: `+0.0000`) | EMA-100=`126.84`
  * Institutional Anchors: EMA-144=`127.96` | EMA-200=`128.98` (Slope: `-0.3327`) | EMA-233=`129.36`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `124.93` (Distance: `-0.13%`)
  * Point of Control (POC) = `119.02` (Distance: `+4.83%`)
  * Value Area Low (VAL) = `117.73` (Distance: `+5.97%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.33` | Weekly POC=`135.06` | Weekly VAL=`130.46`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`127.41` | Low=`123.92`
  * New York Session (13:00-21:00 UTC): High=`125.51` | Low=`124.01`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `124.26` - `125.26`
  * Optimal Trade Entry (OTE 0.705): `125.01`
  * Structural Invalidation Anchor (0.786): `125.76`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `412` | `0x3ee5...4fab` | `LONG` | 5,418,590.93 USD | `43,303.83` | `77.35` | `125.30` | `72.48` | 2,068,900.89 USD | `+38.18%` | `10X Cross` |
| `769` | `0xecb6...2b00` | `SHORT` | 3,011,912.02 USD | `24,077.96` | `133.17` | `125.30` | `1365.20` | 194,612.25 USD | `+6.46%` | `10X Cross` |
| `799` | `0x0514...bdfe` | `SHORT` | 2,879,830.00 USD | `23,000.00` | `87.41` | `125.30` | `155.43` | -869,350.78 USD | `-30.19%` | `10X Cross` |
| `837` | `0x08c1...1135` | `LONG` | 2,728,212.33 USD | `21,836.18` | `80.89` | `125.30` | `87.09` | 961,877.98 USD | `+35.26%` | `10X Cross` |
| `1044` | `0x0996...0ba6` | `SHORT` | 2,124,660.00 USD | `17,000.00` | `107.97` | `125.30` | `196.59` | -289,086.70 USD | `-13.61%` | `3X Cross` |
| `1126` | `0x45d2...4029` | `SHORT` | 1,964,103.14 USD | `15,721.00` | `118.40` | `125.30` | `2745.58` | -102,711.95 USD | `-5.23%` | `10X Cross` |
| `1140` | `0xbfc7...80b4` | `SHORT` | 1,946,741.15 USD | `15,561.48` | `115.30` | `125.30` | `223.21` | -152,441.82 USD | `-7.83%` | `10X Cross` |
| `1177` | `0x6540...f7b7` | `LONG` | 1,893,960.46 USD | `15,158.96` | `144.34` | `125.30` | `76.49` | -294,072.58 USD | `-15.53%` | `5X Isolated` |
| `1247` | `0x07fd...689d` | `LONG` | 1,791,161.27 USD | `14,332.73` | `148.42` | `125.30` | `0.000000` | -336,121.00 USD | `-18.77%` | `10X Cross` |
| `1460` | `0xcac1...26b3` | `SHORT` | 1,501,200.00 USD | `12,000.00` | `125.37` | `125.30` | `829.19` | 3,240.86 USD | `+0.22%` | `10X Cross` |
| `1466` | `0x12d2...f97f` | `LONG` | 1,494,817.41 USD | `11,961.41` | `133.88` | `125.30` | `0.000000` | -106,587.03 USD | `-7.13%` | `10X Cross` |
| `1473` | `0xeadc...9d55` | `LONG` | 1,478,344.72 USD | `11,823.92` | `89.93` | `125.30` | `0.000000` | 414,988.31 USD | `+28.07%` | `10X Cross` |
| `1646` | `0x9df2...c665` | `SHORT` | 1,297,209.84 USD | `10,380.17` | `133.78` | `125.30` | `3049.71` | 91,499.43 USD | `+7.05%` | `10X Cross` |
| `1696` | `0x3dc9...54b0` | `SHORT` | 1,250,005.00 USD | `10,000.00` | `128.60` | `125.30` | `1804.94` | 36,016.83 USD | `+2.88%` | `10X Cross` |
| `1823` | `0x8af7...fa05` | `SHORT` | 1,141,263.89 USD | `9,133.75` | `131.49` | `125.30` | `2201.63` | 59,716.86 USD | `+5.23%` | `10X Cross` |
| `2006` | `0xbc5b...7fdc` | `LONG` | 1,003,651.39 USD | `8,033.71` | `136.30` | `125.30` | `18.26` | -91,377.82 USD | `-9.10%` | `10X Cross` |
| `2014` | `0x72db...8bb6` | `LONG` | 1,001,680.00 USD | `8,000.00` | `180.99` | `125.30` | `0.000000` | -446,277.43 USD | `-44.55%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `128.44` | 10,728.59 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 10.73K USD at 128.4400 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.74` | 370.77 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 0.37K USD at 128.7400 USD [API] | `2026-10-29 02:35:59` |
| `ANNOUNCEMENT` | `INFO` | `128.43` | 8,476.38 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 8.48K USD at 128.4300 USD [API] | `2026-10-29 02:36:30` |
| `ANNOUNCEMENT` | `INFO` | `128.48` | 2,998.72 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 3.00K USD at 128.4800 USD [API] | `2026-10-29 02:36:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+2.97%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.85%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+2.98%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.86%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+2.98%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.86%`)
  * 7D Horizon: Short MP=`139.84` (Vol: 370,900.00 USD, Dist: `+11.79%`) | Long MP=`116.38` (Vol: 253,400.00 USD, Dist: `--6.96%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `26.50` | 5,020.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,740.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 660.06 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 118,450.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 1,500.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 1,090.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 23,360.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.50` | 1,060.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 2,760.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.50` | 209.30 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.50` | 66,420.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.50` | 161.50 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 6,350.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 805.51 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 63,270.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 1,610.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 1,920.00 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 168.51 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 506.87 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 9,120.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `64.50` | 313.47 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 115.94 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 1,060.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 24,470.00 USD | 7,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,110.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 30,980.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 836.84 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 18,010.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,140,000.00 USD | 7,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 11,400.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,890.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,170,000.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 5,210.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 7,090.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 6,060.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 14,100.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `84.50` | 845.00 USD | 3,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 57,430.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 8,960.00 USD | 3,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 1,930,000.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 8,520.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 54,650.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,910.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,990.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 19,120.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 4,190.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,350.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,290.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 50,100.00 USD | 940,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 14,470.00 USD | 890,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 68,140.00 USD | 876,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 26,860.00 USD | 808,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 17,150.00 USD | 781,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 109,670.00 USD | 764,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 11,110.00 USD | 654,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 24,540.00 USD | 643,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,530.00 USD | 618,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 35,590.00 USD | 608,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 7,660.00 USD | 572,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 5,680.00 USD | 565,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 433,620.00 USD | 559,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 16,160.00 USD | 125,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 109,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 52,030.00 USD | 75,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 23,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,770.00 USD | 19,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,270.00 USD | 16,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 195.05 USD | 8,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `118.50` | 1,960.00 USD | 1,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 375.23 USD | 7,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 6,480.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 11,120.00 USD | 13,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 26,830.00 USD | 39,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 34,120.00 USD | 74,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 297.70 USD | 74,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 252.53 USD | 74,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 4,050.00 USD | 78,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 81,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 719.82 USD | 82,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 83,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 108,770.00 USD | 192,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,530.00 USD | 194,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 600,860.00 USD | 795,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 150.28 USD | 795,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 1,990.00 USD | 797,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 457.53 USD | 798,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `154.50` | 3,630,000.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 2,200.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `157.50` | 155.93 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `162.50` | 4,210.00 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 874.72 USD | 4,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 49,950.00 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `169.50` | 198.31 USD | 4,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `170.50` | 1,060.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `173.50` | 1,560.00 USD | 4,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 18,950.00 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 349.68 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `178.50` | 385.56 USD | 4,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `180.50` | 315,500.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 1,280.00 USD | 4,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 33,330.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,230.00 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `188.50` | 748.34 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 538.18 USD | 4,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 16,590.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,500.00 USD | 4,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 15,940.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 124,060.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 1,240.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `214.50` | 8,790.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `224.50` | 3,490,000.00 USD | 11,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 67,650.00 USD | 11,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `227.50` | 1,030,000.00 USD | 12,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 61,900.00 USD | 13,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 2,560.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `234.50` | 379.89 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 2,120.00 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 409.82 USD | 13,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `248.50` | 165,990.00 USD | 14,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `26.50` | 8,190,000.00 USD | 0.00 USD | 5,020.00 USD | `-78.85%` | `189.55` |
| `Live` | `Long` | `27.50` | 8,190,000.00 USD | 0.00 USD | 5,740.00 USD | `-78.06%` | `208.76` |
| `Live` | `Long` | `28.50` | 8,180,000.00 USD | 0.00 USD | 660.06 USD | `-77.26%` | `23.16` |
| `Live` | `Long` | `29.50` | 8,180,000.00 USD | 0.00 USD | 118,450.00 USD | `-76.46%` | `4,015.35` |
| `Live` | `Long` | `30.50` | 8,060,000.00 USD | 0.00 USD | 1,500.00 USD | `-75.66%` | `49.18` |
| `Live` | `Long` | `34.50` | 8,060,000.00 USD | 0.00 USD | 1,090.00 USD | `-72.47%` | `31.69` |
| `Live` | `Long` | `35.50` | 8,060,000.00 USD | 0.00 USD | 23,360.00 USD | `-71.67%` | `657.96` |
| `Live` | `Long` | `38.50` | 8,040,000.00 USD | 0.00 USD | 232.54 USD | `-69.28%` | `6.04` |
| `Live` | `Long` | `42.50` | 8,040,000.00 USD | 0.00 USD | 1,060.00 USD | `-66.09%` | `25.04` |
| `Live` | `Long` | `44.50` | 8,040,000.00 USD | 0.00 USD | 2,760.00 USD | `-64.49%` | `62.13` |
| `Live` | `Long` | `45.50` | 8,030,000.00 USD | 0.00 USD | 209.30 USD | `-63.69%` | `4.60` |
| `Live` | `Long` | `46.50` | 8,030,000.00 USD | 0.00 USD | 66,420.00 USD | `-62.89%` | `1,428.39` |
| `Live` | `Long` | `47.50` | 7,970,000.00 USD | 0.00 USD | 161.50 USD | `-62.10%` | `3.40` |
| `Live` | `Long` | `49.50` | 7,970,000.00 USD | 0.00 USD | 6,350.00 USD | `-60.50%` | `128.20` |
| `Live` | `Long` | `54.50` | 7,960,000.00 USD | 0.00 USD | 805.51 USD | `-56.51%` | `14.78` |
| `Live` | `Long` | `56.50` | 7,960,000.00 USD | 0.00 USD | 63,270.00 USD | `-54.92%` | `1,119.86` |
| `Live` | `Long` | `58.50` | 7,900,000.00 USD | 0.00 USD | 1,610.00 USD | `-53.32%` | `27.49` |
| `Live` | `Long` | `60.50` | 7,900,000.00 USD | 0.00 USD | 1,920.00 USD | `-51.72%` | `31.67` |
| `Live` | `Long` | `61.50` | 7,890,000.00 USD | 0.00 USD | 168.51 USD | `-50.93%` | `2.74` |
| `Live` | `Long` | `62.50` | 7,890,000.00 USD | 0.00 USD | 506.87 USD | `-50.13%` | `8.11` |
| `Live` | `Long` | `63.50` | 7,890,000.00 USD | 0.00 USD | 9,120.00 USD | `-49.33%` | `143.58` |
| `Live` | `Long` | `64.50` | 7,880,000.00 USD | 0.00 USD | 313.47 USD | `-48.53%` | `4.86` |
| `Live` | `Long` | `65.50` | 7,880,000.00 USD | 0.00 USD | 115.94 USD | `-47.73%` | `1.77` |
| `Live` | `Long` | `66.50` | 7,880,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.94%` | `15.99` |
| `Live` | `Long` | `67.50` | 7,880,000.00 USD | 0.00 USD | 24,470.00 USD | `-46.14%` | `362.50` |
| `Live` | `Long` | `68.50` | 7,860,000.00 USD | 0.00 USD | 7,110.00 USD | `-45.34%` | `103.75` |
| `Live` | `Long` | `69.50` | 7,850,000.00 USD | 0.00 USD | 30,980.00 USD | `-44.54%` | `445.79` |
| `Live` | `Long` | `70.50` | 7,820,000.00 USD | 0.00 USD | 836.84 USD | `-43.74%` | `11.87` |
| `Live` | `Long` | `71.50` | 7,820,000.00 USD | 0.00 USD | 18,010.00 USD | `-42.95%` | `251.92` |
| `Live` | `Long` | `72.50` | 7,800,000.00 USD | 0.00 USD | 3,140,000.00 USD | `-42.15%` | `43,311.83` |
| `Live` | `Long` | `73.50` | 4,660,000.00 USD | 0.00 USD | 11,400.00 USD | `-41.35%` | `155.11` |
| `Live` | `Long` | `74.50` | 4,650,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.55%` | `14.20` |
| `Live` | `Long` | `75.50` | 4,650,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.75%` | `25.00` |
| `Live` | `Long` | `76.50` | 4,650,000.00 USD | 0.00 USD | 1,170,000.00 USD | `-38.96%` | `15,287.36` |
| `Live` | `Long` | `77.50` | 3,480,000.00 USD | 0.00 USD | 9,050.00 USD | `-38.16%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,470,000.00 USD | 0.00 USD | 5,210.00 USD | `-37.36%` | `66.36` |
| `Live` | `Long` | `79.50` | 3,460,000.00 USD | 0.00 USD | 7,090.00 USD | `-36.56%` | `89.17` |
| `Live` | `Long` | `82.50` | 3,460,000.00 USD | 0.00 USD | 6,060.00 USD | `-34.17%` | `73.51` |
| `Live` | `Long` | `83.50` | 3,450,000.00 USD | 0.00 USD | 14,100.00 USD | `-33.37%` | `168.92` |
| `Live` | `Long` | `84.50` | 3,440,000.00 USD | 0.00 USD | 845.00 USD | `-32.57%` | `10.00` |
| `Live` | `Long` | `85.50` | 3,430,000.00 USD | 0.00 USD | 57,430.00 USD | `-31.77%` | `671.67` |
| `Live` | `Long` | `86.50` | 3,380,000.00 USD | 0.00 USD | 8,960.00 USD | `-30.98%` | `103.58` |
| `Live` | `Long` | `87.50` | 3,370,000.00 USD | 0.00 USD | 1,930,000.00 USD | `-30.18%` | `22,005.56` |
| `Live` | `Long` | `88.50` | 1,440,000.00 USD | 0.00 USD | 8,520.00 USD | `-29.38%` | `96.23` |
| `Live` | `Long` | `89.50` | 1,430,000.00 USD | 0.00 USD | 54,650.00 USD | `-28.58%` | `610.64` |
| `Live` | `Long` | `90.50` | 1,380,000.00 USD | 0.00 USD | 6,910.00 USD | `-27.78%` | `76.33` |
| `Live` | `Long` | `91.50` | 1,370,000.00 USD | 0.00 USD | 277,420.00 USD | `-26.99%` | `3,031.94` |
| `Live` | `Long` | `92.50` | 1,090,000.00 USD | 0.00 USD | 14,990.00 USD | `-26.19%` | `162.01` |
| `Live` | `Long` | `93.50` | 1,080,000.00 USD | 0.00 USD | 10,990.00 USD | `-25.39%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,070,000.00 USD | 0.00 USD | 19,120.00 USD | `-24.59%` | `202.34` |
| `Live` | `Long` | `95.50` | 1,050,000.00 USD | 0.00 USD | 4,190.00 USD | `-23.80%` | `43.83` |
| `Live` | `Long` | `96.50` | 1,050,000.00 USD | 0.00 USD | 9,350.00 USD | `-23.00%` | `96.87` |
| `Live` | `Long` | `97.50` | 1,040,000.00 USD | 0.00 USD | 95,290.00 USD | `-22.20%` | `977.30` |
| `Live` | `Long` | `98.50` | 940,900.00 USD | 0.00 USD | 50,100.00 USD | `-21.40%` | `508.59` |
| `Live` | `Long` | `99.50` | 890,810.00 USD | 0.00 USD | 14,470.00 USD | `-20.60%` | `145.42` |
| `Live` | `Long` | `100.50` | 876,340.00 USD | 0.00 USD | 68,140.00 USD | `-19.81%` | `678.00` |
| `Live` | `Long` | `101.50` | 808,200.00 USD | 0.00 USD | 26,860.00 USD | `-19.01%` | `264.64` |
| `Live` | `Long` | `102.50` | 781,340.00 USD | 0.00 USD | 17,150.00 USD | `-18.21%` | `167.35` |
| `Live` | `Long` | `103.50` | 764,180.00 USD | 0.00 USD | 109,670.00 USD | `-17.41%` | `1,059.58` |
| `Live` | `Long` | `104.50` | 654,520.00 USD | 0.00 USD | 11,110.00 USD | `-16.61%` | `106.30` |
| `Live` | `Long` | `105.50` | 643,410.00 USD | 0.00 USD | 24,540.00 USD | `-15.82%` | `232.58` |
| `Live` | `Long` | `106.50` | 618,870.00 USD | 0.00 USD | 10,530.00 USD | `-15.02%` | `98.84` |
| `Live` | `Long` | `107.50` | 608,340.00 USD | 0.00 USD | 35,590.00 USD | `-14.22%` | `331.09` |
| `Live` | `Long` | `108.50` | 572,750.00 USD | 0.00 USD | 7,660.00 USD | `-13.42%` | `70.63` |
| `Live` | `Long` | `109.50` | 565,090.00 USD | 0.00 USD | 5,680.00 USD | `-12.62%` | `51.88` |
| `Live` | `Long` | `110.50` | 559,410.00 USD | 0.00 USD | 433,620.00 USD | `-11.83%` | `3,924.17` |
| `Live` | `Long` | `111.50` | 125,790.00 USD | 0.00 USD | 16,160.00 USD | `-11.03%` | `144.95` |
| `Live` | `Long` | `112.50` | 109,630.00 USD | 0.00 USD | 33,900.00 USD | `-10.23%` | `301.33` |
| `Live` | `Long` | `113.50` | 75,730.00 USD | 0.00 USD | 52,030.00 USD | `-9.43%` | `458.42` |
| `Live` | `Long` | `114.50` | 23,690.00 USD | 0.00 USD | 4,560.00 USD | `-8.63%` | `39.82` |
| `Live` | `Long` | `115.50` | 19,140.00 USD | 0.00 USD | 2,770.00 USD | `-7.84%` | `24.00` |
| `Live` | `Long` | `116.50` | 16,360.00 USD | 0.00 USD | 8,270.00 USD | `-7.04%` | `71.00` |
| `Live` | `Long` | `117.50` | 8,090.00 USD | 0.00 USD | 195.05 USD | `-6.24%` | `1.66` |
| `Live` | `Short` | `118.50` | 1,960.00 USD | 1,960.00 USD | 0.00 USD | `-5.44%` | `16.56` |
| `Live` | `Long` | `119.50` | 7,900.00 USD | 0.00 USD | 375.23 USD | `-4.64%` | `3.14` |
| `Live` | `Long` | `120.50` | 7,520.00 USD | 0.00 USD | 6,480.00 USD | `-3.85%` | `53.77` |
| `Live` | `Long` | `121.50` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-3.05%` | `8.58` |
| `Live` | `Short` | `130.50` | 13,080.00 USD | 11,120.00 USD | 0.00 USD | `+4.13%` | `85.21` |
| `Live` | `Short` | `131.50` | 39,910.00 USD | 26,830.00 USD | 0.00 USD | `+4.93%` | `204.05` |
| `Live` | `Short` | `132.50` | 74,030.00 USD | 34,120.00 USD | 0.00 USD | `+5.73%` | `257.50` |
| `Live` | `Short` | `133.50` | 74,330.00 USD | 297.70 USD | 0.00 USD | `+6.53%` | `2.23` |
| `Live` | `Short` | `136.50` | 74,580.00 USD | 252.53 USD | 0.00 USD | `+8.92%` | `1.85` |
| `Live` | `Short` | `137.50` | 78,630.00 USD | 4,050.00 USD | 0.00 USD | `+9.72%` | `29.44` |
| `Live` | `Short` | `138.50` | 81,480.00 USD | 2,850.00 USD | 0.00 USD | `+10.52%` | `20.56` |
| `Live` | `Short` | `139.50` | 82,200.00 USD | 719.82 USD | 0.00 USD | `+11.32%` | `5.16` |
| `Live` | `Short` | `140.50` | 83,350.00 USD | 1,150.00 USD | 0.00 USD | `+12.11%` | `8.19` |
| `Live` | `Short` | `141.50` | 192,120.00 USD | 108,770.00 USD | 0.00 USD | `+12.91%` | `768.71` |
| `Live` | `Short` | `142.50` | 194,650.00 USD | 2,530.00 USD | 0.00 USD | `+13.71%` | `17.73` |
| `Live` | `Short` | `143.50` | 795,510.00 USD | 600,860.00 USD | 0.00 USD | `+14.51%` | `4,187.17` |
| `Live` | `Short` | `144.50` | 795,660.00 USD | 150.28 USD | 0.00 USD | `+15.30%` | `1.04` |
| `Live` | `Short` | `150.50` | 797,650.00 USD | 1,990.00 USD | 0.00 USD | `+20.09%` | `13.23` |
| `Live` | `Short` | `151.50` | 798,110.00 USD | 457.53 USD | 0.00 USD | `+20.89%` | `3.02` |
| `Live` | `Short` | `154.50` | 4,430,000.00 USD | 3,630,000.00 USD | 0.00 USD | `+23.28%` | `23,480.07` |
| `Live` | `Short` | `155.50` | 4,430,000.00 USD | 2,200.00 USD | 0.00 USD | `+24.08%` | `14.13` |
| `Live` | `Short` | `157.50` | 4,430,000.00 USD | 155.93 USD | 0.00 USD | `+25.68%` | `0.99` |
| `Live` | `Short` | `158.50` | 4,430,000.00 USD | 1,480.00 USD | 0.00 USD | `+26.48%` | `9.36` |
| `Live` | `Short` | `162.50` | 4,430,000.00 USD | 4,210.00 USD | 0.00 USD | `+29.67%` | `25.90` |
| `Live` | `Short` | `163.50` | 4,430,000.00 USD | 874.72 USD | 0.00 USD | `+30.47%` | `5.35` |
| `Live` | `Short` | `166.50` | 4,480,000.00 USD | 49,950.00 USD | 0.00 USD | `+32.86%` | `300.00` |
| `Live` | `Short` | `169.50` | 4,480,000.00 USD | 198.31 USD | 0.00 USD | `+35.25%` | `1.17` |
| `Live` | `Short` | `170.50` | 4,490,000.00 USD | 1,060.00 USD | 0.00 USD | `+36.05%` | `6.20` |
| `Live` | `Short` | `173.50` | 4,490,000.00 USD | 1,560.00 USD | 0.00 USD | `+38.45%` | `9.00` |
| `Live` | `Short` | `175.50` | 4,510,000.00 USD | 18,950.00 USD | 0.00 USD | `+40.04%` | `108.00` |
| `Live` | `Short` | `177.50` | 4,510,000.00 USD | 349.68 USD | 0.00 USD | `+41.64%` | `1.97` |
| `Live` | `Short` | `178.50` | 4,510,000.00 USD | 385.56 USD | 0.00 USD | `+42.44%` | `2.16` |
| `Live` | `Short` | `180.50` | 4,820,000.00 USD | 315,500.00 USD | 0.00 USD | `+44.03%` | `1,747.94` |
| `Live` | `Short` | `181.50` | 4,820,000.00 USD | 2,170.00 USD | 0.00 USD | `+44.83%` | `11.93` |
| `Live` | `Short` | `183.50` | 4,830,000.00 USD | 1,280.00 USD | 0.00 USD | `+46.43%` | `6.97` |
| `Live` | `Short` | `186.50` | 4,860,000.00 USD | 33,330.00 USD | 0.00 USD | `+48.82%` | `178.70` |
| `Live` | `Short` | `187.50` | 4,860,000.00 USD | 4,230.00 USD | 0.00 USD | `+49.62%` | `22.56` |
| `Live` | `Short` | `188.50` | 4,860,000.00 USD | 748.34 USD | 0.00 USD | `+50.41%` | `3.97` |
| `Live` | `Short` | `189.50` | 4,860,000.00 USD | 538.18 USD | 0.00 USD | `+51.21%` | `2.84` |
| `Live` | `Short` | `194.50` | 4,880,000.00 USD | 16,590.00 USD | 0.00 USD | `+55.20%` | `85.28` |
| `Live` | `Short` | `195.50` | 4,880,000.00 USD | 1,500.00 USD | 0.00 USD | `+56.00%` | `7.67` |
| `Live` | `Short` | `196.50` | 8,220,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+56.80%` | `17,000.00` |
| `Live` | `Short` | `200.50` | 8,240,000.00 USD | 15,940.00 USD | 0.00 USD | `+59.99%` | `79.49` |
| `Live` | `Short` | `203.50` | 8,240,000.00 USD | 372.41 USD | 0.00 USD | `+62.38%` | `1.83` |
| `Live` | `Short` | `205.50` | 8,360,000.00 USD | 124,060.00 USD | 0.00 USD | `+63.98%` | `603.72` |
| `Live` | `Short` | `210.50` | 8,370,000.00 USD | 1,240.00 USD | 0.00 USD | `+67.97%` | `5.87` |
| `Live` | `Short` | `214.50` | 8,370,000.00 USD | 8,790.00 USD | 0.00 USD | `+71.16%` | `41.00` |
| `Live` | `Short` | `220.50` | 8,380,000.00 USD | 2,000.00 USD | 0.00 USD | `+75.95%` | `9.06` |
| `Live` | `Short` | `224.50` | 11,870,000.00 USD | 3,490,000.00 USD | 0.00 USD | `+79.14%` | `15,561.48` |
| `Live` | `Short` | `225.50` | 11,940,000.00 USD | 67,650.00 USD | 0.00 USD | `+79.94%` | `300.00` |
| `Live` | `Short` | `227.50` | 12,960,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+81.54%` | `4,508.67` |
| `Live` | `Short` | `229.50` | 13,020,000.00 USD | 61,900.00 USD | 0.00 USD | `+83.13%` | `269.73` |
| `Live` | `Short` | `230.50` | 13,030,000.00 USD | 2,560.00 USD | 0.00 USD | `+83.93%` | `11.09` |
| `Live` | `Short` | `232.50` | 13,850,000.00 USD | 818,270.00 USD | 0.00 USD | `+85.53%` | `3,519.45` |
| `Live` | `Short` | `234.50` | 13,850,000.00 USD | 379.89 USD | 0.00 USD | `+87.12%` | `1.62` |
| `Live` | `Short` | `240.50` | 13,850,000.00 USD | 2,120.00 USD | 0.00 USD | `+91.91%` | `8.82` |
| `Live` | `Short` | `242.50` | 13,850,000.00 USD | 409.82 USD | 0.00 USD | `+93.50%` | `1.69` |
| `Live` | `Short` | `248.50` | 14,010,000.00 USD | 165,990.00 USD | 0.00 USD | `+98.29%` | `667.95` |

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
  * Current Rate: `1.60K` | Last 24h: `2.78K` | Last 3d: `40.34K` | Last 7d: `111.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0009%` | **USDT OKX** | `-0.0049%` |
| **USDT Bybit** | `0.0059%` | **USDT KuCoin** | `-0.0043%` |
| **USDT MEXC** | `-0.0009%` | **USDT BingX** | `0.0041%` |
| **USDT Gate** | `-0.0061%` | **USDT Bitget** | `0.0035%` |
| **CoinM Binance** | `0.1149%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `127.50` | `127.35` | `127.50` | `127.84` | `126.94` | 1,022,226.97 USD | 569,223.87 USD | 453,003.10 USD | 116,220.77 USD | `+11.37%` | `20B / 15S` |
| `5:00 UTC` | `127.09` | `127.03` | `127.09` | `127.44` | `126.44` | 1,604,834.75 USD | 705,842.40 USD | 898,992.35 USD | -193,149.95 USD | `-12.04%` | `11B / 25S` |
| `0:00 UTC` | `126.77` | `126.57` | `126.77` | `127.28` | `125.82` | 2,533,134.55 USD | 1,512,642.78 USD | 1,020,491.77 USD | 492,151.02 USD | `+19.43%` | `25B / 32S` |
| `5:00 UTC` | `126.05` | `125.98` | `126.05` | `126.25` | `125.69` | 1,218,204.56 USD | 827,425.56 USD | 390,779.01 USD | 436,646.55 USD | `+35.84%` | `14B / 9S` |
| `0:00 UTC` | `126.06` | `125.45` | `126.06` | `126.25` | `124.81` | 1,613,048.55 USD | 753,514.49 USD | 859,534.06 USD | -106,019.57 USD | `-6.57%` | `16B / 54S` |
| `5:00 UTC` | `125.06` | `125.16` | `125.06` | `125.59` | `124.80` | 1,451,895.08 USD | 700,314.65 USD | 751,580.42 USD | -51,265.77 USD | `-3.53%` | `14B / 12S` |
| `0:00 UTC` | `125.19` | `125.12` | `125.19` | `125.45` | `124.72` | 893,258.87 USD | 412,743.87 USD | 480,515.00 USD | -67,771.12 USD | `-7.59%` | `7B / 17S` |
| `5:00 UTC` | `125.34` | `125.36` | `125.34` | `125.68` | `125.05` | 944,493.33 USD | 470,610.76 USD | 473,882.56 USD | -3,271.80 USD | `-0.35%` | `9B / 6S` |
| `0:00 UTC` | `125.27` | `125.16` | `125.27` | `125.47` | `124.73` | 786,073.81 USD | 420,964.65 USD | 365,109.16 USD | 55,855.49 USD | `+7.11%` | `10B / 9S` |
| `5:00 UTC` | `125.00` | `125.08` | `125.00` | `125.53` | `124.66` | 810,843.52 USD | 375,765.97 USD | 435,077.54 USD | -59,311.57 USD | `-7.31%` | `12B / 21S` |

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
| `5m` | -297,820.00 USD | -191,420.00 USD | **`DISTRIBUTION`** |
| `15m` | -351,380.00 USD | -104,720.00 USD | **`DISTRIBUTION`** |
| `30m` | -415,810.00 USD | 71,790.00 USD | **`DISTRIBUTION`** |
| `1h` | -729,680.00 USD | -522,960.00 USD | **`DISTRIBUTION`** |
| `2h` | -666,720.00 USD | 424,890.00 USD | **`DISTRIBUTION`** |
| `4h` | -234,620.00 USD | 3,640,000.00 USD | **`ACCUMULATION`** |
| `6h` | -121,950.00 USD | 5,570,000.00 USD | **`ACCUMULATION`** |
| `8h` | -1,070,000.00 USD | 4,860,000.00 USD | **`ACCUMULATION`** |
| `12h` | -3,020,000.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,310,000.00 USD | -7,050,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -28,850,000.00 USD | -45,350,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -116,620,000.00 USD | -94,200,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-297.82K` | 15m=`-351.38K` | 1h=`-729.68K` | 24h=`-7.31M`
* Futures Capital Netflows: 5m=`-191.42K` | 15m=`-104.72K` | 1h=`-522.96K` | 24h=`-7.05M`
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
  * Execution Entry: `117.73` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `115.96` (Risk Distance: `1.77` pts)
  * +2.5R Take Profit: `122.16`
  * Mathematical Lot Sizing: **`5.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `124.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `126.70` (Risk Distance: `1.77` pts)
  * +2.5R Take Profit: `120.50`
  * Mathematical Lot Sizing: **`5.64 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`125.76`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
