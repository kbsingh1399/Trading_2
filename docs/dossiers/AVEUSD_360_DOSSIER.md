# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVEUSD
**Canonical Key**: `AVEUSD` | **Broker Instrument**: `AVEUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 15:54:24 IST` (`2026-10-30 10:24:24 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `124.12` | **Live Ask Quote**: `124.38` | **Mid Price**: `124.25`
- **Spread Points**: `26.00` | **Spread BPS**: `20.93 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `122.19` | VWAP Z-Score: `+0.56` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.9975` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `46.14` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `131.89` | Lower -3.00σ Band: `112.48`
  * Upper +2.51σ Band: `130.31` | Lower -2.51σ Band: `114.07`
  * Upper +2.01σ Band: `128.69` | Lower -2.01σ Band: `115.69`
  * Upper +2.00σ Band: `128.66` | Lower -2.00σ Band: `115.72`
  * Upper +1.28σ Band: `126.33` | Lower -1.28σ Band: `118.05`
  * Upper +1.00σ Band: `125.42` | Lower -1.00σ Band: `118.95`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`124.51` | EMA-20=`124.58` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`124.89` (Slope: `+0.0000`) | EMA-100=`126.55`
  * Institutional Anchors: EMA-144=`127.67` | EMA-200=`128.75` (Slope: `-0.4074`) | EMA-233=`129.09`
- **Range Boundaries**: 24H High=`137.67` | 24H Low=`114.69` | Weekly High=`138.47` | Weekly Low=`114.69`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `127.07` (Distance: `-2.22%`)
  * Point of Control (POC) = `124.41` (Distance: `-0.13%`)
  * Value Area Low (VAL) = `119.79` (Distance: `+3.73%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`134.69` | POC=`132.92` | VAL=`129.68`
  * Prior Day Extremes: PDH=`137.67` | PDL=`122.01` | PDC=`123.50`
  * Monday Range Blueprint: High=`138.35` | Mid=`135.31` | Low=`132.27`
  * Developing Weekly Value Area: Weekly VAH=`136.33` | Weekly POC=`135.06` | Weekly VAL=`130.31`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`127.54` | Low=`114.69`
  * London Session (08:00-16:00 UTC): High=`127.41` | Low=`123.78`
  * New York Session (13:00-21:00 UTC): High=`124.81` | Low=`123.86`
  * Initial Balance (First Hour): IB High=`126.87` | IB Low=`123.92`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `123.75` - `124.75`
  * Optimal Trade Entry (OTE 0.705): `124.50`
  * Structural Invalidation Anchor (0.786): `125.24`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:50:34 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `411` | `0x3ee5...4fab` | `LONG` | 5,379,201.76 USD | `43,303.83` | `77.35` | `124.33` | `71.79` | 2,029,511.72 USD | `+37.73%` | `10X Cross` |
| `759` | `0xecb6...2b00` | `SHORT` | 2,993,562.20 USD | `24,077.96` | `133.17` | `124.33` | `1298.44` | 212,962.06 USD | `+7.11%` | `10X Cross` |
| `788` | `0x0514...bdfe` | `SHORT` | 2,856,411.40 USD | `23,000.00` | `87.41` | `124.33` | `155.53` | -845,932.18 USD | `-29.62%` | `10X Cross` |
| `823` | `0x08c1...1135` | `LONG` | 2,714,839.85 USD | `21,836.18` | `80.89` | `124.33` | `86.63` | 948,505.50 USD | `+34.94%` | `10X Cross` |
| `1013` | `0x0996...0ba6` | `SHORT` | 2,110,890.00 USD | `17,000.00` | `107.97` | `124.33` | `196.59` | -275,316.70 USD | `-13.04%` | `3X Cross` |
| `1105` | `0x45d2...4029` | `SHORT` | 1,954,827.75 USD | `15,721.00` | `118.40` | `124.33` | `2757.01` | -93,436.56 USD | `-4.78%` | `10X Cross` |
| `1123` | `0xbfc7...80b4` | `SHORT` | 1,934,724.57 USD | `15,561.48` | `115.30` | `124.33` | `224.41` | -140,425.25 USD | `-7.26%` | `10X Cross` |
| `1159` | `0x6540...f7b7` | `LONG` | 1,884,181.49 USD | `15,155.90` | `144.34` | `124.33` | `76.49` | -303,409.88 USD | `-16.10%` | `5X Isolated` |
| `1228` | `0x07fd...689d` | `LONG` | 1,780,276.99 USD | `14,332.73` | `148.42` | `124.33` | `0.000000` | -347,005.28 USD | `-19.49%` | `10X Cross` |
| `1447` | `0xcac1...26b3` | `SHORT` | 1,491,840.00 USD | `12,000.00` | `125.37` | `124.33` | `851.79` | 12,600.86 USD | `+0.84%` | `10X Cross` |
| `1454` | `0x12d2...f97f` | `LONG` | 1,485,367.89 USD | `11,961.41` | `133.88` | `124.33` | `0.000000` | -116,036.55 USD | `-7.81%` | `10X Cross` |
| `1460` | `0xeadc...9d55` | `LONG` | 1,469,122.06 USD | `11,823.92` | `89.93` | `124.33` | `0.000000` | 405,765.65 USD | `+27.62%` | `10X Cross` |
| `1626` | `0x9df2...c665` | `SHORT` | 1,289,327.14 USD | `10,380.17` | `133.78` | `124.33` | `3056.97` | 99,382.13 USD | `+7.71%` | `10X Cross` |
| `1681` | `0x3dc9...54b0` | `SHORT` | 1,243,200.00 USD | `10,000.00` | `128.60` | `124.33` | `1824.81` | 42,821.83 USD | `+3.44%` | `10X Cross` |
| `1812` | `0x8af7...fa05` | `SHORT` | 1,134,046.40 USD | `9,133.75` | `131.49` | `124.33` | `2188.33` | 66,934.35 USD | `+5.90%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `128.48` | 2,998.72 USD | `-` | `NEWS_INTEL` | `-` | #AAVE Liquidated Short: 3.00K USD at 128.4800 USD [API] | `2026-10-29 02:36:30` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`128.80` (Vol: 368,100.00 USD, Dist: `+3.60%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.28%`)
  * 48H Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.62%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.28%`)
  * 3D Horizon: Short MP=`128.82` (Vol: 290,600.00 USD, Dist: `+3.62%`) | Long MP=`116.52` (Vol: 253,400.00 USD, Dist: `--6.28%`)
  * 7D Horizon: Short MP=`128.71` (Vol: 394,000.00 USD, Dist: `+3.53%`) | Long MP=`116.45` (Vol: 253,400.00 USD, Dist: `--6.33%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `26.50` | 3,720.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.50` | 5,740.00 USD | 8,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.50` | 114,210.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.50` | 165.20 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.50` | 231.80 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.50` | 1,800.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.50` | 529.57 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.50` | 8,350.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.50` | 24,150.00 USD | 8,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.50` | 232.54 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.50` | 158.94 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.50` | 356.70 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.50` | 2,760.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.50` | 46,500.00 USD | 8,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.50` | 293.03 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `53.50` | 471.87 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `54.50` | 27,320.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `55.50` | 6,940.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `56.50` | 1,510.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `58.50` | 2,470.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `60.50` | 66,930.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `61.50` | 661.74 USD | 7,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `62.50` | 506.87 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `63.50` | 4,270.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `65.50` | 434.27 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `66.50` | 101.08 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `67.50` | 29,330.00 USD | 7,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `68.50` | 7,110.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `69.50` | 23,930.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `70.50` | 8,140.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `71.50` | 1,410.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `72.50` | 3,140,000.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `73.50` | 19,810.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `74.50` | 1,060.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `75.50` | 1,890.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `76.50` | 1,160,000.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `77.50` | 9,050.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `78.50` | 4,310.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `79.50` | 9,510.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `82.50` | 14,400.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `83.50` | 6,780.00 USD | 3,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `85.50` | 44,800.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `86.50` | 1,900,000.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `87.50` | 14,820.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `88.50` | 15,120.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `89.50` | 60,720.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `90.50` | 6,460.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `91.50` | 277,420.00 USD | 1,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `92.50` | 14,750.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `93.50` | 10,990.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `94.50` | 19,350.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `95.50` | 4,300.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `96.50` | 9,050.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `97.50` | 95,290.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `98.50` | 38,060.00 USD | 974,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `99.50` | 10,680.00 USD | 936,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `100.50` | 18,550.00 USD | 926,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `101.50` | 18,880.00 USD | 907,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `102.50` | 24,400.00 USD | 888,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `103.50` | 36,040.00 USD | 864,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `104.50` | 87,240.00 USD | 828,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `105.50` | 100,380.00 USD | 741,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `106.50` | 10,530.00 USD | 640,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `107.50` | 34,850.00 USD | 630,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `108.50` | 7,660.00 USD | 595,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `109.50` | 2,400.00 USD | 587,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `110.50` | 436,940.00 USD | 585,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `111.50` | 16,160.00 USD | 148,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `112.50` | 33,900.00 USD | 132,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `113.50` | 49,760.00 USD | 98,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `114.50` | 4,560.00 USD | 48,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `115.50` | 2,770.00 USD | 43,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `116.50` | 8,970.00 USD | 41,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `117.50` | 14,610.00 USD | 32,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `118.50` | 437.27 USD | 17,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `119.50` | 15,310.00 USD | 17,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `120.50` | 806.14 USD | 1,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `121.50` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `130.50` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `131.50` | 28,270.00 USD | 41,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `132.50` | 35,000.00 USD | 76,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `133.50` | 3,090.00 USD | 80,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `134.50` | 162.75 USD | 80,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `136.50` | 252.53 USD | 80,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `137.50` | 2,850.00 USD | 83,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `138.50` | 2,850.00 USD | 86,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `139.50` | 719.82 USD | 86,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `140.50` | 1,150.00 USD | 88,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `141.50` | 108,770.00 USD | 196,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `142.50` | 2,730.00 USD | 199,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `143.50` | 607,480.00 USD | 807,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `144.50` | 150.28 USD | 807,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `145.50` | 14,550.00 USD | 821,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `148.50` | 2,280.00 USD | 824,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `150.50` | 1,990.00 USD | 826,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `151.50` | 457.53 USD | 826,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `155.50` | 3,580,000.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `158.50` | 1,480.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `163.50` | 874.72 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `164.50` | 162.85 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `166.50` | 4,310.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `167.50` | 50,250.00 USD | 4,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `171.50` | 103,960.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `175.50` | 20,530.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `177.50` | 1,600.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `181.50` | 2,170.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `183.50` | 141.30 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `184.50` | 322,490.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `185.50` | 1,150.00 USD | 4,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `186.50` | 33,690.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `187.50` | 4,630.00 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `189.50` | 538.18 USD | 4,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `194.50` | 16,590.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `195.50` | 1,500.00 USD | 4,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `196.50` | 3,340,000.00 USD | 8,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `200.50` | 15,270.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `203.50` | 372.41 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `205.50` | 124,060.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `206.50` | 689.71 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `210.50` | 151.56 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `214.50` | 8,790.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `220.50` | 2,000.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `225.50` | 3,570,000.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `226.50` | 67,950.00 USD | 12,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `229.50` | 1,030,000.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `230.50` | 251.25 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `231.50` | 2,310.00 USD | 13,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `232.50` | 818,270.00 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `237.50` | 384.75 USD | 13,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `240.50` | 162,760.00 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `242.50` | 409.82 USD | 14,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `246.50` | 50,490.00 USD | 14,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `247.50` | 3,910.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `26.50` | 8,210,000.00 USD | 0.00 USD | 3,720.00 USD | `-78.71%` | `140.23` |
| `Live` | `Long` | `27.50` | 8,210,000.00 USD | 0.00 USD | 5,740.00 USD | `-77.91%` | `208.76` |
| `Live` | `Long` | `28.50` | 8,200,000.00 USD | 0.00 USD | 114,210.00 USD | `-77.10%` | `4,007.41` |
| `Live` | `Long` | `29.50` | 8,090,000.00 USD | 0.00 USD | 165.20 USD | `-76.30%` | `5.60` |
| `Live` | `Long` | `30.50` | 8,090,000.00 USD | 0.00 USD | 231.80 USD | `-75.50%` | `7.60` |
| `Live` | `Long` | `32.50` | 8,090,000.00 USD | 0.00 USD | 1,800.00 USD | `-73.89%` | `55.31` |
| `Live` | `Long` | `34.50` | 8,080,000.00 USD | 0.00 USD | 529.57 USD | `-72.28%` | `15.35` |
| `Live` | `Long` | `35.50` | 8,080,000.00 USD | 0.00 USD | 8,350.00 USD | `-71.48%` | `235.28` |
| `Live` | `Long` | `37.50` | 8,080,000.00 USD | 0.00 USD | 24,150.00 USD | `-69.87%` | `643.92` |
| `Live` | `Long` | `38.50` | 8,050,000.00 USD | 0.00 USD | 232.54 USD | `-69.07%` | `6.04` |
| `Live` | `Long` | `41.50` | 8,050,000.00 USD | 0.00 USD | 158.94 USD | `-66.66%` | `3.83` |
| `Live` | `Long` | `43.50` | 8,050,000.00 USD | 0.00 USD | 356.70 USD | `-65.05%` | `8.20` |
| `Live` | `Long` | `44.50` | 8,050,000.00 USD | 0.00 USD | 2,760.00 USD | `-64.25%` | `62.13` |
| `Live` | `Long` | `49.50` | 8,050,000.00 USD | 0.00 USD | 46,500.00 USD | `-60.23%` | `939.41` |
| `Live` | `Long` | `51.50` | 8,000,000.00 USD | 0.00 USD | 293.03 USD | `-58.63%` | `5.69` |
| `Live` | `Long` | `53.50` | 8,000,000.00 USD | 0.00 USD | 471.87 USD | `-57.02%` | `8.82` |
| `Live` | `Long` | `54.50` | 8,000,000.00 USD | 0.00 USD | 27,320.00 USD | `-56.22%` | `501.34` |
| `Live` | `Long` | `55.50` | 7,970,000.00 USD | 0.00 USD | 6,940.00 USD | `-55.41%` | `125.00` |
| `Live` | `Long` | `56.50` | 7,970,000.00 USD | 0.00 USD | 1,510.00 USD | `-54.61%` | `26.66` |
| `Live` | `Long` | `58.50` | 7,960,000.00 USD | 0.00 USD | 2,470.00 USD | `-53.00%` | `42.24` |
| `Live` | `Long` | `60.50` | 7,960,000.00 USD | 0.00 USD | 66,930.00 USD | `-51.40%` | `1,106.32` |
| `Live` | `Long` | `61.50` | 7,900,000.00 USD | 0.00 USD | 661.74 USD | `-50.59%` | `10.76` |
| `Live` | `Long` | `62.50` | 7,890,000.00 USD | 0.00 USD | 506.87 USD | `-49.79%` | `8.11` |
| `Live` | `Long` | `63.50` | 7,890,000.00 USD | 0.00 USD | 4,270.00 USD | `-48.99%` | `67.25` |
| `Live` | `Long` | `65.50` | 7,890,000.00 USD | 0.00 USD | 434.27 USD | `-47.38%` | `6.63` |
| `Live` | `Long` | `66.50` | 7,890,000.00 USD | 0.00 USD | 101.08 USD | `-46.58%` | `1.52` |
| `Live` | `Long` | `67.50` | 7,890,000.00 USD | 0.00 USD | 29,330.00 USD | `-45.77%` | `434.59` |
| `Live` | `Long` | `68.50` | 7,860,000.00 USD | 0.00 USD | 7,110.00 USD | `-44.97%` | `103.75` |
| `Live` | `Long` | `69.50` | 7,850,000.00 USD | 0.00 USD | 23,930.00 USD | `-44.17%` | `344.37` |
| `Live` | `Long` | `70.50` | 7,830,000.00 USD | 0.00 USD | 8,140.00 USD | `-43.36%` | `115.49` |
| `Live` | `Long` | `71.50` | 7,820,000.00 USD | 0.00 USD | 1,410.00 USD | `-42.56%` | `19.76` |
| `Live` | `Long` | `72.50` | 7,820,000.00 USD | 0.00 USD | 3,140,000.00 USD | `-41.76%` | `43,315.63` |
| `Live` | `Long` | `73.50` | 4,680,000.00 USD | 0.00 USD | 19,810.00 USD | `-40.95%` | `269.58` |
| `Live` | `Long` | `74.50` | 4,660,000.00 USD | 0.00 USD | 1,060.00 USD | `-40.15%` | `14.20` |
| `Live` | `Long` | `75.50` | 4,660,000.00 USD | 0.00 USD | 1,890.00 USD | `-39.35%` | `25.00` |
| `Live` | `Long` | `76.50` | 4,660,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-38.54%` | `15,157.94` |
| `Live` | `Long` | `77.50` | 3,500,000.00 USD | 0.00 USD | 9,050.00 USD | `-37.74%` | `116.79` |
| `Live` | `Long` | `78.50` | 3,490,000.00 USD | 0.00 USD | 4,310.00 USD | `-36.94%` | `54.87` |
| `Live` | `Long` | `79.50` | 3,480,000.00 USD | 0.00 USD | 9,510.00 USD | `-36.13%` | `119.58` |
| `Live` | `Long` | `82.50` | 3,470,000.00 USD | 0.00 USD | 14,400.00 USD | `-33.72%` | `174.53` |
| `Live` | `Long` | `83.50` | 3,460,000.00 USD | 0.00 USD | 6,780.00 USD | `-32.92%` | `81.14` |
| `Live` | `Long` | `85.50` | 3,450,000.00 USD | 0.00 USD | 44,800.00 USD | `-31.31%` | `524.00` |
| `Live` | `Long` | `86.50` | 3,410,000.00 USD | 0.00 USD | 1,900,000.00 USD | `-30.51%` | `22,017.11` |
| `Live` | `Long` | `87.50` | 1,500,000.00 USD | 0.00 USD | 14,820.00 USD | `-29.71%` | `169.38` |
| `Live` | `Long` | `88.50` | 1,490,000.00 USD | 0.00 USD | 15,120.00 USD | `-28.90%` | `170.85` |
| `Live` | `Long` | `89.50` | 1,470,000.00 USD | 0.00 USD | 60,720.00 USD | `-28.10%` | `678.40` |
| `Live` | `Long` | `90.50` | 1,410,000.00 USD | 0.00 USD | 6,460.00 USD | `-27.30%` | `71.37` |
| `Live` | `Long` | `91.50` | 1,410,000.00 USD | 0.00 USD | 277,420.00 USD | `-26.49%` | `3,031.94` |
| `Live` | `Long` | `92.50` | 1,130,000.00 USD | 0.00 USD | 14,750.00 USD | `-25.69%` | `159.47` |
| `Live` | `Long` | `93.50` | 1,110,000.00 USD | 0.00 USD | 10,990.00 USD | `-24.89%` | `117.52` |
| `Live` | `Long` | `94.50` | 1,100,000.00 USD | 0.00 USD | 19,350.00 USD | `-24.08%` | `204.77` |
| `Live` | `Long` | `95.50` | 1,080,000.00 USD | 0.00 USD | 4,300.00 USD | `-23.28%` | `44.98` |
| `Live` | `Long` | `96.50` | 1,080,000.00 USD | 0.00 USD | 9,050.00 USD | `-22.48%` | `93.75` |
| `Live` | `Long` | `97.50` | 1,070,000.00 USD | 0.00 USD | 95,290.00 USD | `-21.67%` | `977.30` |
| `Live` | `Long` | `98.50` | 974,940.00 USD | 0.00 USD | 38,060.00 USD | `-20.87%` | `386.39` |
| `Live` | `Long` | `99.50` | 936,880.00 USD | 0.00 USD | 10,680.00 USD | `-20.07%` | `107.31` |
| `Live` | `Long` | `100.50` | 926,200.00 USD | 0.00 USD | 18,550.00 USD | `-19.26%` | `184.62` |
| `Live` | `Long` | `101.50` | 907,650.00 USD | 0.00 USD | 18,880.00 USD | `-18.46%` | `186.04` |
| `Live` | `Long` | `102.50` | 888,760.00 USD | 0.00 USD | 24,400.00 USD | `-17.66%` | `238.04` |
| `Live` | `Long` | `103.50` | 864,370.00 USD | 0.00 USD | 36,040.00 USD | `-16.85%` | `348.24` |
| `Live` | `Long` | `104.50` | 828,320.00 USD | 0.00 USD | 87,240.00 USD | `-16.05%` | `834.83` |
| `Live` | `Long` | `105.50` | 741,080.00 USD | 0.00 USD | 100,380.00 USD | `-15.25%` | `951.44` |
| `Live` | `Long` | `106.50` | 640,710.00 USD | 0.00 USD | 10,530.00 USD | `-14.44%` | `98.84` |
| `Live` | `Long` | `107.50` | 630,180.00 USD | 0.00 USD | 34,850.00 USD | `-13.64%` | `324.23` |
| `Live` | `Long` | `108.50` | 595,330.00 USD | 0.00 USD | 7,660.00 USD | `-12.84%` | `70.63` |
| `Live` | `Long` | `109.50` | 587,660.00 USD | 0.00 USD | 2,400.00 USD | `-12.03%` | `21.88` |
| `Live` | `Long` | `110.50` | 585,270.00 USD | 0.00 USD | 436,940.00 USD | `-11.23%` | `3,954.17` |
| `Live` | `Long` | `111.50` | 148,330.00 USD | 0.00 USD | 16,160.00 USD | `-10.43%` | `144.95` |
| `Live` | `Long` | `112.50` | 132,170.00 USD | 0.00 USD | 33,900.00 USD | `-9.62%` | `301.33` |
| `Live` | `Long` | `113.50` | 98,270.00 USD | 0.00 USD | 49,760.00 USD | `-8.82%` | `438.42` |
| `Live` | `Long` | `114.50` | 48,510.00 USD | 0.00 USD | 4,560.00 USD | `-8.02%` | `39.82` |
| `Live` | `Long` | `115.50` | 43,950.00 USD | 0.00 USD | 2,770.00 USD | `-7.21%` | `24.00` |
| `Live` | `Long` | `116.50` | 41,180.00 USD | 0.00 USD | 8,970.00 USD | `-6.41%` | `77.00` |
| `Live` | `Long` | `117.50` | 32,210.00 USD | 0.00 USD | 14,610.00 USD | `-5.61%` | `124.38` |
| `Live` | `Long` | `118.50` | 17,590.00 USD | 0.00 USD | 437.27 USD | `-4.80%` | `3.69` |
| `Live` | `Long` | `119.50` | 17,150.00 USD | 0.00 USD | 15,310.00 USD | `-4.00%` | `128.08` |
| `Live` | `Long` | `120.50` | 1,850.00 USD | 0.00 USD | 806.14 USD | `-3.20%` | `6.69` |
| `Live` | `Long` | `121.50` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-2.39%` | `8.58` |
| `Live` | `Short` | `130.50` | 13,720.00 USD | 13,720.00 USD | 0.00 USD | `+4.84%` | `105.16` |
| `Live` | `Short` | `131.50` | 41,990.00 USD | 28,270.00 USD | 0.00 USD | `+5.64%` | `214.96` |
| `Live` | `Short` | `132.50` | 76,990.00 USD | 35,000.00 USD | 0.00 USD | `+6.44%` | `264.17` |
| `Live` | `Short` | `133.50` | 80,080.00 USD | 3,090.00 USD | 0.00 USD | `+7.25%` | `23.11` |
| `Live` | `Short` | `134.50` | 80,240.00 USD | 162.75 USD | 0.00 USD | `+8.05%` | `1.21` |
| `Live` | `Short` | `136.50` | 80,490.00 USD | 252.53 USD | 0.00 USD | `+9.66%` | `1.85` |
| `Live` | `Short` | `137.50` | 83,350.00 USD | 2,850.00 USD | 0.00 USD | `+10.46%` | `20.75` |
| `Live` | `Short` | `138.50` | 86,190.00 USD | 2,850.00 USD | 0.00 USD | `+11.26%` | `20.56` |
| `Live` | `Short` | `139.50` | 86,910.00 USD | 719.82 USD | 0.00 USD | `+12.07%` | `5.16` |
| `Live` | `Short` | `140.50` | 88,060.00 USD | 1,150.00 USD | 0.00 USD | `+12.87%` | `8.19` |
| `Live` | `Short` | `141.50` | 196,840.00 USD | 108,770.00 USD | 0.00 USD | `+13.67%` | `768.71` |
| `Live` | `Short` | `142.50` | 199,570.00 USD | 2,730.00 USD | 0.00 USD | `+14.48%` | `19.19` |
| `Live` | `Short` | `143.50` | 807,050.00 USD | 607,480.00 USD | 0.00 USD | `+15.28%` | `4,233.30` |
| `Live` | `Short` | `144.50` | 807,200.00 USD | 150.28 USD | 0.00 USD | `+16.08%` | `1.04` |
| `Live` | `Short` | `145.50` | 821,750.00 USD | 14,550.00 USD | 0.00 USD | `+16.89%` | `100.00` |
| `Live` | `Short` | `148.50` | 824,030.00 USD | 2,280.00 USD | 0.00 USD | `+19.30%` | `15.36` |
| `Live` | `Short` | `150.50` | 826,020.00 USD | 1,990.00 USD | 0.00 USD | `+20.90%` | `13.23` |
| `Live` | `Short` | `151.50` | 826,480.00 USD | 457.53 USD | 0.00 USD | `+21.71%` | `3.02` |
| `Live` | `Short` | `155.50` | 4,410,000.00 USD | 3,580,000.00 USD | 0.00 USD | `+24.92%` | `23,014.13` |
| `Live` | `Short` | `158.50` | 4,410,000.00 USD | 1,480.00 USD | 0.00 USD | `+27.33%` | `9.36` |
| `Live` | `Short` | `163.50` | 4,410,000.00 USD | 874.72 USD | 0.00 USD | `+31.35%` | `5.35` |
| `Live` | `Short` | `164.50` | 4,410,000.00 USD | 162.85 USD | 0.00 USD | `+32.15%` | `0.99` |
| `Live` | `Short` | `166.50` | 4,410,000.00 USD | 4,310.00 USD | 0.00 USD | `+33.76%` | `25.90` |
| `Live` | `Short` | `167.50` | 4,460,000.00 USD | 50,250.00 USD | 0.00 USD | `+34.56%` | `300.00` |
| `Live` | `Short` | `171.50` | 4,570,000.00 USD | 103,960.00 USD | 0.00 USD | `+37.77%` | `606.20` |
| `Live` | `Short` | `175.50` | 4,590,000.00 USD | 20,530.00 USD | 0.00 USD | `+40.99%` | `117.00` |
| `Live` | `Short` | `177.50` | 4,590,000.00 USD | 1,600.00 USD | 0.00 USD | `+42.59%` | `9.01` |
| `Live` | `Short` | `181.50` | 4,590,000.00 USD | 2,170.00 USD | 0.00 USD | `+45.81%` | `11.93` |
| `Live` | `Short` | `183.50` | 4,590,000.00 USD | 141.30 USD | 0.00 USD | `+47.41%` | `0.77` |
| `Live` | `Short` | `184.50` | 4,910,000.00 USD | 322,490.00 USD | 0.00 USD | `+48.22%` | `1,747.94` |
| `Live` | `Short` | `185.50` | 4,910,000.00 USD | 1,150.00 USD | 0.00 USD | `+49.02%` | `6.20` |
| `Live` | `Short` | `186.50` | 4,950,000.00 USD | 33,690.00 USD | 0.00 USD | `+49.82%` | `180.67` |
| `Live` | `Short` | `187.50` | 4,950,000.00 USD | 4,630.00 USD | 0.00 USD | `+50.63%` | `24.72` |
| `Live` | `Short` | `189.50` | 4,950,000.00 USD | 538.18 USD | 0.00 USD | `+52.23%` | `2.84` |
| `Live` | `Short` | `194.50` | 4,970,000.00 USD | 16,590.00 USD | 0.00 USD | `+56.25%` | `85.28` |
| `Live` | `Short` | `195.50` | 4,970,000.00 USD | 1,500.00 USD | 0.00 USD | `+57.05%` | `7.67` |
| `Live` | `Short` | `196.50` | 8,310,000.00 USD | 3,340,000.00 USD | 0.00 USD | `+57.86%` | `17,000.00` |
| `Live` | `Short` | `200.50` | 8,330,000.00 USD | 15,270.00 USD | 0.00 USD | `+61.07%` | `76.15` |
| `Live` | `Short` | `203.50` | 8,330,000.00 USD | 372.41 USD | 0.00 USD | `+63.48%` | `1.83` |
| `Live` | `Short` | `205.50` | 8,450,000.00 USD | 124,060.00 USD | 0.00 USD | `+65.09%` | `603.72` |
| `Live` | `Short` | `206.50` | 8,450,000.00 USD | 689.71 USD | 0.00 USD | `+65.89%` | `3.34` |
| `Live` | `Short` | `210.50` | 8,450,000.00 USD | 151.56 USD | 0.00 USD | `+69.10%` | `0.72` |
| `Live` | `Short` | `214.50` | 8,460,000.00 USD | 8,790.00 USD | 0.00 USD | `+72.32%` | `41.00` |
| `Live` | `Short` | `220.50` | 8,460,000.00 USD | 2,000.00 USD | 0.00 USD | `+77.14%` | `9.06` |
| `Live` | `Short` | `225.50` | 12,030,000.00 USD | 3,570,000.00 USD | 0.00 USD | `+81.15%` | `15,836.36` |
| `Live` | `Short` | `226.50` | 12,100,000.00 USD | 67,950.00 USD | 0.00 USD | `+81.96%` | `300.00` |
| `Live` | `Short` | `229.50` | 13,140,000.00 USD | 1,030,000.00 USD | 0.00 USD | `+84.37%` | `4,508.67` |
| `Live` | `Short` | `230.50` | 13,140,000.00 USD | 251.25 USD | 0.00 USD | `+85.17%` | `1.09` |
| `Live` | `Short` | `231.50` | 13,140,000.00 USD | 2,310.00 USD | 0.00 USD | `+85.97%` | `10.00` |
| `Live` | `Short` | `232.50` | 13,960,000.00 USD | 818,270.00 USD | 0.00 USD | `+86.78%` | `3,519.45` |
| `Live` | `Short` | `237.50` | 13,960,000.00 USD | 384.75 USD | 0.00 USD | `+90.79%` | `1.62` |
| `Live` | `Short` | `240.50` | 14,120,000.00 USD | 162,760.00 USD | 0.00 USD | `+93.20%` | `676.77` |
| `Live` | `Short` | `242.50` | 14,120,000.00 USD | 409.82 USD | 0.00 USD | `+94.81%` | `1.69` |
| `Live` | `Short` | `246.50` | 14,170,000.00 USD | 50,490.00 USD | 0.00 USD | `+98.02%` | `204.83` |
| `Live` | `Short` | `247.50` | 14,180,000.00 USD | 3,910.00 USD | 0.00 USD | `+98.83%` | `15.81` |

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
  * Current Rate: `1.89K` | Last 24h: `2.78K` | Last 3d: `40.34K` | Last 7d: `111.39K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0001%` | **USDT OKX** | `-0.0010%` |
| **USDT Bybit** | `0.0054%` | **USDT KuCoin** | `0.0033%` |
| **USDT MEXC** | `0.0001%` | **USDT BingX** | `0.0045%` |
| **USDT Gate** | `-0.0009%` | **USDT Bitget** | `0.0013%` |
| **CoinM Binance** | `0.1631%` | **CoinM OKX** | `-` |

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
| `0:00 UTC` | `125.19` | `125.12` | `125.19` | `125.45` | `124.72` | 893,258.87 USD | 412,743.87 USD | 480,515.00 USD | -67,771.12 USD | `-7.59%` | `7B / 17S` |
| `5:00 UTC` | `125.34` | `125.36` | `125.34` | `125.68` | `125.05` | 944,493.33 USD | 470,610.76 USD | 473,882.56 USD | -3,271.80 USD | `-0.35%` | `9B / 6S` |
| `0:00 UTC` | `125.27` | `125.16` | `125.27` | `125.47` | `124.73` | 786,073.81 USD | 420,964.65 USD | 365,109.16 USD | 55,855.49 USD | `+7.11%` | `10B / 9S` |
| `5:00 UTC` | `125.00` | `125.10` | `125.00` | `125.53` | `124.66` | 887,277.31 USD | 387,796.46 USD | 499,480.85 USD | -111,684.39 USD | `-12.59%` | `10B / 23S` |
| `0:00 UTC` | `124.45` | `124.82` | `124.45` | `125.66` | `124.31` | 1,781,424.08 USD | 591,700.01 USD | 1,189,724.07 USD | -598,024.06 USD | `-33.57%` | `13B / 39S` |
| `5:00 UTC` | `124.41` | `124.42` | `124.41` | `124.69` | `124.20` | 1,280,426.88 USD | 695,542.34 USD | 584,884.54 USD | 110,657.80 USD | `+8.64%` | `8B / 5S` |
| `0:00 UTC` | `124.56` | `124.51` | `124.56` | `124.78` | `124.10` | 675,363.07 USD | 319,234.27 USD | 356,128.80 USD | -36,894.54 USD | `-5.46%` | `7B / 14S` |
| `5:00 UTC` | `124.98` | `124.71` | `124.98` | `125.06` | `124.30` | 643,674.29 USD | 263,568.94 USD | 380,105.36 USD | -116,536.42 USD | `-18.10%` | `5B / 12S` |
| `0:00 UTC` | `124.53` | `124.54` | `124.53` | `125.02` | `124.28` | 704,011.73 USD | 281,288.21 USD | 422,723.52 USD | -141,435.31 USD | `-20.09%` | `3B / 19S` |
| `5:00 UTC` | `124.22` | `124.27` | `124.22` | `124.38` | `124.16` | 154,762.53 USD | 37,577.33 USD | 117,185.20 USD | -79,607.87 USD | `-51.44%` | `0B / 6S` |

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
| `5m` | -6,960.00 USD | -107,130.00 USD | **`DISTRIBUTION`** |
| `15m` | -152,650.00 USD | -238,110.00 USD | **`DISTRIBUTION`** |
| `30m` | -119,830.00 USD | -274,790.00 USD | **`DISTRIBUTION`** |
| `1h` | -136,800.00 USD | -215,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -741,740.00 USD | -204,130.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,060,000.00 USD | 609,230.00 USD | **`DISTRIBUTION`** |
| `6h` | -742,890.00 USD | 3,890,000.00 USD | **`ACCUMULATION`** |
| `8h` | -317,070.00 USD | 6,890,000.00 USD | **`ACCUMULATION`** |
| `12h` | -1,870,000.00 USD | -68,560.00 USD | **`DISTRIBUTION`** |
| `24h` | -7,790,000.00 USD | -8,150,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -29,090,000.00 USD | -44,470,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -116,930,000.00 USD | -94,470,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-6.96K` | 15m=`-152.65K` | 1h=`-136.80K` | 24h=`-7.79M`
* Futures Capital Netflows: 5m=`-107.13K` | 15m=`-238.11K` | 1h=`-215.00K` | 24h=`-8.15M`
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
  * `2026-10-30 15:33:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:17 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:17 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:17 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:46:17 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:45:17 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `119.79` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `118.20` (Risk Distance: `1.59` pts)
  * +2.5R Take Profit: `123.76`
  * Mathematical Lot Sizing: **`6.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `127.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `128.66` (Risk Distance: `1.59` pts)
  * +2.5R Take Profit: `123.10`
  * Mathematical Lot Sizing: **`6.30 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`125.24`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
