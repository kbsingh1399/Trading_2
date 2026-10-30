# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 15:42:19 IST` (`2026-10-30 10:12:19 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1700` | **Live Ask Quote**: `0.1700` | **Mid Price**: `0.1700`
- **Spread Points**: `0.000034` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
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
  * Session VWAP: `0.1700` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1712` | Lower -3.00σ Band: `0.1688`
  * Upper +2.51σ Band: `0.1710` | Lower -2.51σ Band: `0.1691`
  * Upper +2.01σ Band: `0.1707` | Lower -2.01σ Band: `0.1693`
  * Upper +2.00σ Band: `0.1707` | Lower -2.00σ Band: `0.1693`
  * Upper +1.28σ Band: `0.1705` | Lower -1.28σ Band: `0.1695`
  * Upper +1.00σ Band: `0.1704` | Lower -1.00σ Band: `0.1697`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1700` | EMA-20=`0.1700` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1700` (Slope: `+0.0000`) | EMA-100=`0.1700`
  * Institutional Anchors: EMA-144=`0.1700` | EMA-200=`0.1700` (Slope: `+0.0000`) | EMA-233=`0.1700`
- **Range Boundaries**: 24H High=`0.1717` | 24H Low=`0.1683` | Weekly High=`0.1734` | Weekly Low=`0.1666`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1705` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.1700` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.1695` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.1707` | POC=`0.1700` | VAL=`0.1693`
  * Prior Day Extremes: PDH=`0.1710` | PDL=`0.1690` | PDC=`0.1700`
  * Monday Range Blueprint: High=`0.1709` | Mid=`0.1700` | Low=`0.1692`
  * Developing Weekly Value Area: Weekly VAH=`0.1714` | Weekly POC=`0.1700` | Weekly VAL=`0.1687`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1704` | Low=`0.1697`
  * London Session (08:00-16:00 UTC): High=`0.1707` | Low=`0.1693`
  * New York Session (13:00-21:00 UTC): High=`0.1710` | Low=`0.1690`
  * Initial Balance (First Hour): IB High=`0.1705` | IB Low=`0.1695`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1693` - `0.1707`
  * Optimal Trade Entry (OTE 0.705): `0.1704`
  * Structural Invalidation Anchor (0.786): `0.1714`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1620` | `0.1621` | `0.1615` | `0.1620` | `576,482` | 93,233.07 USD | -19,114.48 USD | `-20.50%` | -8,030,543.45 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.1620` | `0.1621` | `0.1617` | `0.1619` | `667,973` | 108,148.01 USD | -9,157.85 USD | `-8.47%` | -8,039,701.30 USD | `+0.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1620` | `0.1622` | `0.1618` | `0.1621` | `834,246` | 135,190.41 USD | 18,237.94 USD | `+13.49%` | -8,021,463.35 USD | `+0.80` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1620` | `0.1623` | `0.1611` | `0.1620` | `4,822,290` | 779,913.00 USD | -34,929.06 USD | `-4.48%` | -7,919,665.34 USD | `+0.07` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1620` | `0.1622` | `0.1615` | `0.1621` | `2,088,160` | 338,104.92 USD | -11,378.57 USD | `-3.37%` | -7,931,043.91 USD | `+0.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1621` | `0.1624` | `0.1613` | `0.1617` | `2,787,002` | 451,192.52 USD | -17,748.83 USD | `-3.93%` | -7,948,792.74 USD | `-0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1650` | `0.1657` | `0.1623` | `0.1629` | `29,928,265` | 4,911,959.21 USD | -315,580.46 USD | `-6.42%` | -7,559,567.01 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1629` | `0.1632` | `0.1611` | `0.1621` | `15,160,560` | 2,456,828.08 USD | -319,109.65 USD | `-12.99%` | -7,878,676.67 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1621` | `0.1624` | `0.1613` | `0.1617` | `2,787,002` | 451,192.52 USD | -17,748.83 USD | `-3.93%` | -7,896,425.50 USD | `+0.29` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1621` | `45,079,800` | 7,367,324.16 USD | -633,275.63 USD | `-8.60%` | -7,480,790.26 USD | `+0.52` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1617` | `47,875,827` | 7,819,979.81 USD | -652,438.95 USD | `-8.34%` | -7,499,953.58 USD | `+0.51` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:40:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1625` | 4,182.60 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.18K USD at 0.1625 USD [API] | `2026-10-29 07:16:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1684` | 5,823.61 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 5.82K USD at 0.1684 USD [API] | `2026-10-29 10:57:33` |
| `ANNOUNCEMENT` | `INFO` | `0.1770` | 709.13 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.71K USD at 0.1770 USD [API] | `2026-10-28 20:01:24` |
| `ANNOUNCEMENT` | `INFO` | `0.1730` | 1,220.98 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 1.22K USD at 0.1730 USD [API] | `2026-10-26 08:46:55` |
| `ANNOUNCEMENT` | `INFO` | `0.2105` | 227.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.23K USD at 0.2105 USD [API] | `2026-09-19 03:39:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1708` | 6,077.79 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 6.08K USD at 0.1708 USD [API] | `2026-10-29 13:59:02` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1629` (Vol: 153,600.00 USD, Dist: `+4.92%`) | Long MP=`0.1511` (Vol: 173,700.00 USD, Dist: `--2.69%`)
  * 48H Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.1784` (Vol: 158,900.00 USD, Dist: `+14.89%`) | Long MP=`0.1510` (Vol: 189,600.00 USD, Dist: `--2.77%`)
  * 7D Horizon: Short MP=`0.1791` (Vol: 196,100.00 USD, Dist: `+15.75%`) | Long MP=`0.1511` (Vol: 221,900.00 USD, Dist: `--2.38%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0345` | 105.57 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0365` | 356.31 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0375` | 242.53 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 4,650.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 100.47 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 156.28 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 924.32 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 16,160.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 205,030.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 1,110.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 1,250.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 11,240.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 99,790.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 3,000.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 79,110.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 14,220.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0835` | 4,980.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 280.45 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 4,780.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 2,180.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0955` | 2,750.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 396.66 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 13,020.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 7,670.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 3,860.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 8,870.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 414.83 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 802.14 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 13,280.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,190.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 1,620.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,230.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 13,820.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 118,120.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,450.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 14,280.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,240.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,220.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,430.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 377.05 USD | 995,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 348.01 USD | 995,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 16,720.00 USD | 994,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 10,250.00 USD | 978,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,010.00 USD | 968,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 17,000.00 USD | 966,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1310` | 8,110,000.00 USD | 8,110,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1313` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1315` | 19,580.00 USD | 949,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1316` | 8,090,000.00 USD | 8,090,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1319` | 8,070,000.00 USD | 8,070,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1322` | 8,050,000.00 USD | 8,050,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1325` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 929,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1328` | 8,010,000.00 USD | 8,010,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1331` | 7,980,000.00 USD | 7,980,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1334` | 7,950,000.00 USD | 7,950,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,860.00 USD | 924,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1337` | 7,940,000.00 USD | 7,940,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1340` | 7,910,000.00 USD | 7,910,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1343` | 7,880,000.00 USD | 7,880,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1345` | 39,090.00 USD | 872,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1346` | 7,860,000.00 USD | 7,860,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1349` | 7,800,000.00 USD | 7,800,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1352` | 7,780,000.00 USD | 7,780,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1355` | 7,750,000.00 USD | 7,750,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1355` | 1,440.00 USD | 833,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1358` | 7,720,000.00 USD | 7,720,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1361` | 7,680,000.00 USD | 7,680,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1364` | 7,670,000.00 USD | 7,670,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 10,320.00 USD | 832,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1367` | 7,640,000.00 USD | 7,640,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1370` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1373` | 7,630,000.00 USD | 7,630,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 18,260.00 USD | 822,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1379` | 7,590,000.00 USD | 7,590,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1385` | 7,570,000.00 USD | 7,570,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,330.00 USD | 803,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1388` | 7,520,000.00 USD | 7,520,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1391` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1394` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 9,210.00 USD | 799,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1397` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1400` | 7,420,000.00 USD | 7,420,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1403` | 7,400,000.00 USD | 7,400,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 14,550.00 USD | 790,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 16,540.00 USD | 775,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1418` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1421` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,030.00 USD | 759,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,140.00 USD | 260,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1436` | 7,370,000.00 USD | 7,370,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1439` | 7,330,000.00 USD | 7,330,000.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1442` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 241,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1447` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1451` | 4,680,000.00 USD | 4,680,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1451` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 4,660,000.00 USD | 4,660,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,650,000.00 USD | 4,650,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 231,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1457` | 4,650,000.00 USD | 4,650,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1459` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,630,000.00 USD | 4,630,000.00 USD | 0.00 USD | 3,000.00 USD | 1,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 4,630,000.00 USD | 4,630,000.00 USD | 9,940.00 USD | 2,690.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 4,610,000.00 USD | 4,610,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 28,360.00 USD | 139,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1466` | 7,300,000.00 USD | 7,300,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 4,580,000.00 USD | 4,580,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1469` | 7,190,000.00 USD | 7,190,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 4,580,000.00 USD | 4,580,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1472` | 7,180,000.00 USD | 7,180,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,560,000.00 USD | 4,560,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,430,000.00 USD | 4,430,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1475` | 7,150,000.00 USD | 7,150,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 83,410.00 USD | 111,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 4,400,000.00 USD | 4,400,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1478` | 7,100,000.00 USD | 7,100,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,120,000.00 USD | 4,120,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 4,010,000.00 USD | 4,010,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1481` | 6,840,000.00 USD | 6,840,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 3,950,000.00 USD | 3,950,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1484` | 6,740,000.00 USD | 6,740,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,790,000.00 USD | 3,790,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 3,340.00 USD | 27,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,680,000.00 USD | 3,680,000.00 USD | 8,840.00 USD | 3,580.00 USD | 11,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1487` | 6,530,000.00 USD | 6,530,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,650,000.00 USD | 3,650,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1490` | 6,430,000.00 USD | 6,430,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,620,000.00 USD | 3,620,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,570,000.00 USD | 3,570,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1493` | 6,290,000.00 USD | 6,290,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,540,000.00 USD | 3,540,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 24,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1496` | 6,230,000.00 USD | 6,230,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,450,000.00 USD | 3,450,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,440,000.00 USD | 3,440,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1499` | 5,990,000.00 USD | 5,990,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,420,000.00 USD | 3,420,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1502` | 5,900,000.00 USD | 5,900,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,400,000.00 USD | 3,400,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,190,000.00 USD | 3,190,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1505` | 5,890,000.00 USD | 5,890,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1508` | 5,740,000.00 USD | 5,740,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1511` | 5,340,000.00 USD | 5,340,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,780,000.00 USD | 2,780,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1514` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,520,000.00 USD | 2,520,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1515` | 945.33 USD | 23,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,390,000.00 USD | 2,390,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1517` | 4,820,000.00 USD | 4,820,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,340,000.00 USD | 2,340,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1520` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,270,000.00 USD | 2,270,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,220,000.00 USD | 2,220,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1523` | 4,420,000.00 USD | 4,420,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,210,000.00 USD | 2,210,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1526` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,160,000.00 USD | 2,160,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,150,000.00 USD | 2,150,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1529` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,120,000.00 USD | 2,120,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1532` | 4,360,000.00 USD | 4,360,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,080,000.00 USD | 2,080,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1535` | 4,350,000.00 USD | 4,350,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,620.00 USD | 22,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,060,000.00 USD | 2,060,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1538` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,040,000.00 USD | 2,040,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1541` | 4,290,000.00 USD | 4,290,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1544` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,000,000.00 USD | 2,000,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 1,960,000.00 USD | 1,960,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1547` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 1,940,000.00 USD | 1,940,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1550` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 1,890,000.00 USD | 1,890,000.00 USD | 11,600.00 USD | 10,490.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 1,870,000.00 USD | 1,870,000.00 USD | 7,900.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1553` | 4,160,000.00 USD | 4,160,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 1,850,000.00 USD | 1,850,000.00 USD | 40,830.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 4,150.00 USD | 13,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1556` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,800,000.00 USD | 1,800,000.00 USD | 2,800.00 USD | 11,690.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 1,780,000.00 USD | 1,780,000.00 USD | 14,470.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1559` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,760,000.00 USD | 1,760,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1562` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,750,000.00 USD | 1,750,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 1,710,000.00 USD | 1,710,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1565` | 3,940,000.00 USD | 3,940,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,660.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,620,000.00 USD | 1,620,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1568` | 3,840,000.00 USD | 3,840,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,590,000.00 USD | 1,590,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,460,000.00 USD | 1,460,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1571` | 3,560,000.00 USD | 3,560,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,350,000.00 USD | 1,350,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1574` | 3,300,000.00 USD | 3,300,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,280,000.00 USD | 1,280,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1577` | 3,100,000.00 USD | 3,100,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 1,210,000.00 USD | 1,210,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1580` | 2,950,000.00 USD | 2,950,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,180,000.00 USD | 1,180,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,150,000.00 USD | 1,150,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1583` | 2,670,000.00 USD | 2,670,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 1,010,000.00 USD | 1,010,000.00 USD | 16,540.00 USD | 17,270.00 USD | 6,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1586` | 2,560,000.00 USD | 2,560,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 969,900.00 USD | 969,900.00 USD | 42,230.00 USD | 24,370.00 USD | 45,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 858,060.00 USD | 858,060.00 USD | 20,380.00 USD | 10,830.00 USD | 44,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1589` | 2,470,000.00 USD | 2,470,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 781,990.00 USD | 781,990.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1592` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 708,920.00 USD | 708,920.00 USD | 14,950.00 USD | 32,920.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 630,900.00 USD | 630,900.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1595` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 615,940.00 USD | 615,940.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1598` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 598,130.00 USD | 598,130.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 590,540.00 USD | 590,540.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1601` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 566,890.00 USD | 566,890.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1604` | 2,050,000.00 USD | 2,050,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 524,390.00 USD | 524,390.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 471,760.00 USD | 471,760.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1607` | 1,650,000.00 USD | 1,650,000.00 USD | 166,880.00 USD | 0.00 USD | 370,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 449,250.00 USD | 449,250.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1610` | 1,120,000.00 USD | 1,120,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 301,230.00 USD | 301,230.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 125,680.00 USD | 125,680.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1613` | 748,360.00 USD | 748,360.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 62,310.00 USD | 62,310.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 271,830.00 USD | 271,830.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1616` | 543,650.00 USD | 543,650.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1617` | 34,490.00 USD | 34,490.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1617` | 68,980.00 USD | 68,980.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1619` | 117,860.00 USD | 117,860.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1619` | 620,320.00 USD | 620,320.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1621` | 123,520.00 USD | 123,520.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1622` | 775,540.00 USD | 775,540.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1623` | 140,550.00 USD | 140,550.00 USD | 0.00 USD | 17,020.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1625` | 226,000.00 USD | 226,000.00 USD | 38,240.00 USD | 0.00 USD | 47,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1625` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1627` | 287,460.00 USD | 287,460.00 USD | 0.00 USD | 20,350.00 USD | 41,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1628` | 1,110,000.00 USD | 1,110,000.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1629` | 392,600.00 USD | 392,600.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1631` | 1,180,000.00 USD | 1,180,000.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1635` | 401,300.00 USD | 401,300.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1637` | 416,170.00 USD | 416,170.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1649` | 422,100.00 USD | 422,100.00 USD | 5,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1651` | 438,230.00 USD | 438,230.00 USD | 16,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 461,470.00 USD | 461,470.00 USD | 17,080.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 476,420.00 USD | 476,420.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1661` | 1,290,000.00 USD | 1,290,000.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 557,500.00 USD | 557,500.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1664` | 1,450,000.00 USD | 1,450,000.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 594,840.00 USD | 594,840.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 636,750.00 USD | 636,750.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1667` | 1,500,000.00 USD | 1,500,000.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 664,520.00 USD | 664,520.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1670` | 1,840,000.00 USD | 1,840,000.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 726,550.00 USD | 726,550.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 810,800.00 USD | 810,800.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1673` | 1,950,000.00 USD | 1,950,000.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 844,090.00 USD | 844,090.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 6,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1676` | 2,190,000.00 USD | 2,190,000.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1677` | 1,030,000.00 USD | 1,030,000.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 1,090,000.00 USD | 1,090,000.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1679` | 2,400,000.00 USD | 2,400,000.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 1,240,000.00 USD | 1,240,000.00 USD | 91,660.00 USD | 34,810.00 USD | 21,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1682` | 2,640,000.00 USD | 2,640,000.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 1,360,000.00 USD | 1,360,000.00 USD | 56,920.00 USD | 12,810.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 1,500,000.00 USD | 1,500,000.00 USD | 41,190.00 USD | 48,480.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1685` | 2,740,000.00 USD | 2,740,000.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,590,000.00 USD | 1,590,000.00 USD | 6,960.00 USD | 8,320.00 USD | 72,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1688` | 2,820,000.00 USD | 2,820,000.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 1,690,000.00 USD | 1,690,000.00 USD | 51,500.00 USD | 26,970.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,930,000.00 USD | 1,930,000.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1691` | 3,000,000.00 USD | 3,000,000.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 2,080,000.00 USD | 2,080,000.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1694` | 3,120,000.00 USD | 3,120,000.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 2,130,000.00 USD | 2,130,000.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 2,190,000.00 USD | 2,190,000.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1697` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 2,290,000.00 USD | 2,290,000.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1700` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 2,330,000.00 USD | 2,330,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1703` | 3,420,000.00 USD | 3,420,000.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,410,000.00 USD | 2,410,000.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 7,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1706` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,550,000.00 USD | 2,550,000.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 2,630,000.00 USD | 2,630,000.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1709` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,670,000.00 USD | 2,670,000.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1712` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,700,000.00 USD | 2,700,000.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 2,780,000.00 USD | 2,780,000.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1715` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 1,150.00 USD | 8,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,820,000.00 USD | 2,820,000.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1718` | 3,740,000.00 USD | 3,740,000.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,890,000.00 USD | 2,890,000.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 3,010,000.00 USD | 3,010,000.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1721` | 4,080,000.00 USD | 4,080,000.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 3,100,000.00 USD | 3,100,000.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1724` | 4,280,000.00 USD | 4,280,000.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 3,160,000.00 USD | 3,160,000.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1725` | 10,550.00 USD | 18,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1727` | 3,180,000.00 USD | 3,180,000.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 3,200,000.00 USD | 3,200,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1730` | 4,590,000.00 USD | 4,590,000.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 3,220,000.00 USD | 3,220,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1733` | 4,730,000.00 USD | 4,730,000.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 3,240,000.00 USD | 3,240,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 1,190.00 USD | 19,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 3,270,000.00 USD | 3,270,000.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1739` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 3,300,000.00 USD | 3,300,000.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1745` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1748` | 4,930,000.00 USD | 4,930,000.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 3,430,000.00 USD | 3,430,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 3,460,000.00 USD | 3,460,000.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1751` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 171,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,500,000.00 USD | 3,500,000.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1754` | 5,320,000.00 USD | 5,320,000.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,540,000.00 USD | 3,540,000.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 3,610,000.00 USD | 3,610,000.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1757` | 5,490,000.00 USD | 5,490,000.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,700,000.00 USD | 3,700,000.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1760` | 5,750,000.00 USD | 5,750,000.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,840,000.00 USD | 3,840,000.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 3,900,000.00 USD | 3,900,000.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1763` | 6,000,000.00 USD | 6,000,000.00 USD | 142,420.00 USD | 101,270.00 USD | 12,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,970,000.00 USD | 3,970,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1766` | 6,340,000.00 USD | 6,340,000.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 4,060,000.00 USD | 4,060,000.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 4,150,000.00 USD | 4,150,000.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1769` | 6,540,000.00 USD | 6,540,000.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 4,180,000.00 USD | 4,180,000.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1772` | 6,750,000.00 USD | 6,750,000.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 4,230,000.00 USD | 4,230,000.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 4,260,000.00 USD | 4,260,000.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1775` | 6,950,000.00 USD | 6,950,000.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,370,000.00 USD | 4,370,000.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1778` | 7,150,000.00 USD | 7,150,000.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 4,400,000.00 USD | 4,400,000.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 4,400,000.00 USD | 4,400,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1781` | 7,200,000.00 USD | 7,200,000.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,470,000.00 USD | 4,470,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1784` | 7,430,000.00 USD | 7,430,000.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,510,000.00 USD | 4,510,000.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 1,980.00 USD | 21,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1787` | 4,550,000.00 USD | 4,550,000.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1787` | 7,600,000.00 USD | 7,600,000.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,550,000.00 USD | 4,550,000.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1790` | 7,720,000.00 USD | 7,720,000.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 4,580,000.00 USD | 4,580,000.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1793` | 7,850,000.00 USD | 7,850,000.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,640,000.00 USD | 4,640,000.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1796` | 7,920,000.00 USD | 7,920,000.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1797` | 4,660,000.00 USD | 4,660,000.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 4,680,000.00 USD | 4,680,000.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1799` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,720,000.00 USD | 4,720,000.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1802` | 8,110,000.00 USD | 8,110,000.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 4,750,000.00 USD | 4,750,000.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 4,760,000.00 USD | 4,760,000.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1805` | 8,170,000.00 USD | 8,170,000.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,800,000.00 USD | 4,800,000.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1808` | 8,320,000.00 USD | 8,320,000.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 4,810,000.00 USD | 4,810,000.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1811` | 4,830,000.00 USD | 4,830,000.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1811` | 8,430,000.00 USD | 8,430,000.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1813` | 4,880,000.00 USD | 4,880,000.00 USD | 7,950.00 USD | 35,640.00 USD | 8,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1814` | 8,550,000.00 USD | 8,550,000.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1815` | 4,900,000.00 USD | 4,900,000.00 USD | 7,040.00 USD | 1,040.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 135.29 USD | 22,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1817` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 9,410.00 USD | 7,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1817` | 8,660,000.00 USD | 8,660,000.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1819` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1820` | 8,790,000.00 USD | 8,790,000.00 USD | 52,150.00 USD | 43,140.00 USD | 38,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1821` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 10,520.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1823` | 4,960,000.00 USD | 4,960,000.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1823` | 8,920,000.00 USD | 8,920,000.00 USD | 62,540.00 USD | 18,340.00 USD | 50,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1825` | 4,980,000.00 USD | 4,980,000.00 USD | 3,290.00 USD | 3,020.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1826` | 8,990,000.00 USD | 8,990,000.00 USD | 45,250.00 USD | 9,890.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1827` | 4,980,000.00 USD | 4,980,000.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1829` | 9,080,000.00 USD | 9,080,000.00 USD | 20,880.00 USD | 17,180.00 USD | 51,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1832` | 9,210,000.00 USD | 9,210,000.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1835` | 9,250,000.00 USD | 9,250,000.00 USD | 13,840.00 USD | 7,930.00 USD | 16,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1838` | 9,420,000.00 USD | 9,420,000.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1841` | 9,500,000.00 USD | 9,500,000.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1844` | 9,580,000.00 USD | 9,580,000.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,390.00 USD | 24,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1847` | 9,620,000.00 USD | 9,620,000.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1850` | 9,800,000.00 USD | 9,800,000.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1853` | 9,900,000.00 USD | 9,900,000.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1854` | 9,910,000.00 USD | 9,910,000.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 25,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 1,450.00 USD | 26,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,010.00 USD | 30,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 30,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 42,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 13,570.00 USD | 55,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 474.40 USD | 56,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 56,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2105` | 190.73 USD | 56,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 72,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2145` | 4,320.00 USD | 76,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 41,330.00 USD | 118,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 118,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 87,800.00 USD | 206,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 206,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2245` | 338.64 USD | 206,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 206,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 213,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 229,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 229,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 22,000.00 USD | 251,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 49,300.00 USD | 300,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 301,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 301,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 305,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 26,570.00 USD | 332,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 54,960.00 USD | 387,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 387,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 387,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2695` | 11,830.00 USD | 399,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 201,290.00 USD | 600,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 600,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 612,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 612,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2835` | 2,160.00 USD | 615,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 615,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 616,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 287,090.00 USD | 903,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3015` | 1,910.00 USD | 905,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 485.90 USD | 905,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 911,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 603.06 USD | 912,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 924,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 1,530.00 USD | 925,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3155` | 649.11 USD | 926,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 926,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0345` | 1,850,000.00 USD | 0.00 USD | 3,350.00 USD | `-78.67%` | `97,221,100,000,000.00` |
| `Live` | `Long` | `0.0385` | 1,850,000.00 USD | 0.00 USD | 1,740.00 USD | `-76.20%` | `45,291,300,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,840,000.00 USD | 0.00 USD | 110.22 USD | `-74.35%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,840,000.00 USD | 0.00 USD | 170.00 USD | `-73.73%` | `4,000,000,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,840,000.00 USD | 0.00 USD | 1,700.00 USD | `-69.40%` | `34,259,200,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,840,000.00 USD | 0.00 USD | 289.43 USD | `-67.55%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,840,000.00 USD | 0.00 USD | 6,000.00 USD | `-66.93%` | `112,093,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,840,000.00 USD | 0.00 USD | 2,270.00 USD | `-66.31%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,830,000.00 USD | 0.00 USD | 15,650.00 USD | `-65.07%` | `276,984,000,000,000.00` |
| `Live` | `Long` | `0.0575` | 1,820,000.00 USD | 0.00 USD | 1,230.00 USD | `-64.46%` | `21,450,000,000,000.00` |
| `Live` | `Long` | `0.0595` | 1,820,000.00 USD | 0.00 USD | 1,110.00 USD | `-63.22%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0605` | 1,810,000.00 USD | 0.00 USD | 3,280.00 USD | `-62.60%` | `54,249,500,000,000.00` |
| `Live` | `Long` | `0.0615` | 1,810,000.00 USD | 0.00 USD | 157.66 USD | `-61.98%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,810,000.00 USD | 0.00 USD | 126.34 USD | `-60.75%` | `1,989,600,000,000.00` |
| `Live` | `Long` | `0.0665` | 1,810,000.00 USD | 0.00 USD | 233,840.00 USD | `-58.89%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,580,000.00 USD | 0.00 USD | 106,660.00 USD | `-58.27%` | `1,580,216,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,470,000.00 USD | 0.00 USD | 4,920.00 USD | `-57.66%` | `71,795,000,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,470,000.00 USD | 0.00 USD | 976.14 USD | `-57.04%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,470,000.00 USD | 0.00 USD | 2,970.00 USD | `-56.42%` | `42,142,800,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,460,000.00 USD | 0.00 USD | 5,840.00 USD | `-55.80%` | `81,674,400,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,460,000.00 USD | 0.00 USD | 111.58 USD | `-55.18%` | `1,539,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,460,000.00 USD | 0.00 USD | 2,760.00 USD | `-54.57%` | `37,551,700,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,450,000.00 USD | 0.00 USD | 226.17 USD | `-53.95%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0755` | 1,450,000.00 USD | 0.00 USD | 472.15 USD | `-53.33%` | `6,253,700,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,450,000.00 USD | 0.00 USD | 14,690.00 USD | `-52.71%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0785` | 1,440,000.00 USD | 0.00 USD | 66,100.00 USD | `-51.47%` | `842,071,000,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,370,000.00 USD | 0.00 USD | 4,630.00 USD | `-50.86%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,370,000.00 USD | 0.00 USD | 19,130.00 USD | `-49.00%` | `231,907,800,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,350,000.00 USD | 0.00 USD | 19,460.00 USD | `-46.53%` | `224,937,400,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,330,000.00 USD | 0.00 USD | 280.45 USD | `-45.91%` | `3,205,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,330,000.00 USD | 0.00 USD | 362.62 USD | `-45.29%` | `4,097,400,000,000.00` |
| `Live` | `Long` | `0.0905` | 1,330,000.00 USD | 0.00 USD | 2,050.00 USD | `-44.06%` | `22,623,800,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,330,000.00 USD | 0.00 USD | 5,000.00 USD | `-43.44%` | `54,609,300,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,320,000.00 USD | 0.00 USD | 2,040.00 USD | `-42.82%` | `22,044,300,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,320,000.00 USD | 0.00 USD | 814.24 USD | `-42.20%` | `8,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,320,000.00 USD | 0.00 USD | 1,510.00 USD | `-41.58%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,320,000.00 USD | 0.00 USD | 1,600.00 USD | `-40.35%` | `16,620,400,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,310,000.00 USD | 0.00 USD | 17,090.00 USD | `-39.11%` | `173,538,000,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,300,000.00 USD | 0.00 USD | 8,070.00 USD | `-38.49%` | `81,139,600,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,290,000.00 USD | 0.00 USD | 2,600.00 USD | `-37.87%` | `25,906,300,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,290,000.00 USD | 0.00 USD | 9,850.00 USD | `-36.02%` | `95,169,100,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,280,000.00 USD | 0.00 USD | 13,700.00 USD | `-35.40%` | `131,115,100,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,260,000.00 USD | 0.00 USD | 8,450.00 USD | `-34.78%` | `80,138,800,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,260,000.00 USD | 0.00 USD | 596.55 USD | `-34.17%` | `5,601,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,250,000.00 USD | 0.00 USD | 1,820.00 USD | `-33.55%` | `16,928,700,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,250,000.00 USD | 0.00 USD | 12,400.00 USD | `-32.93%` | `114,250,900,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,240,000.00 USD | 0.00 USD | 13,820.00 USD | `-31.69%` | `125,027,000,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,230,000.00 USD | 0.00 USD | 425.50 USD | `-31.07%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,230,000.00 USD | 0.00 USD | 281.48 USD | `-29.84%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,230,000.00 USD | 0.00 USD | 8,950.00 USD | `-29.22%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,220,000.00 USD | 0.00 USD | 1,450.00 USD | `-28.60%` | `12,552,800,000,000.00` |
| `Live` | `Long` | `0.1165` | 1,220,000.00 USD | 0.00 USD | 569.31 USD | `-27.98%` | `4,886,800,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,210,000.00 USD | 0.00 USD | 129,500.00 USD | `-27.37%` | `1,102,087,700,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,090,000.00 USD | 0.00 USD | 33,440.00 USD | `-26.75%` | `282,230,500,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,050,000.00 USD | 0.00 USD | 1,830.00 USD | `-26.13%` | `15,286,200,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,050,000.00 USD | 0.00 USD | 303.75 USD | `-24.89%` | `2,500,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,050,000.00 USD | 0.00 USD | 19,420.00 USD | `-24.28%` | `158,503,900,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,030,000.00 USD | 0.00 USD | 50,980.00 USD | `-23.66%` | `412,801,600,000,000.00` |
| `Live` | `Long` | `0.1245` | 979,430.00 USD | 0.00 USD | 377.05 USD | `-23.04%` | `3,028,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 979,050.00 USD | 0.00 USD | 344.89 USD | `-22.42%` | `2,748,100,000,000.00` |
| `Live` | `Long` | `0.1265` | 978,710.00 USD | 0.00 USD | 16,720.00 USD | `-21.80%` | `132,151,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 961,990.00 USD | 0.00 USD | 10,470.00 USD | `-21.18%` | `82,125,800,000,000.00` |
| `Live` | `Long` | `0.1295` | 951,520.00 USD | 0.00 USD | 2,440.00 USD | `-19.95%` | `18,831,200,000,000.00` |
| `Live` | `Long` | `0.1305` | 949,080.00 USD | 0.00 USD | 17,000.00 USD | `-19.33%` | `130,296,400,000,000.00` |
| `Live` | `Long` | `0.1315` | 932,080.00 USD | 0.00 USD | 19,580.00 USD | `-18.71%` | `148,881,700,000,000.00` |
| `Live` | `Long` | `0.1325` | 912,500.00 USD | 0.00 USD | 4,640.00 USD | `-18.09%` | `35,013,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 907,860.00 USD | 0.00 USD | 51,860.00 USD | `-17.48%` | `388,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 856,000.00 USD | 0.00 USD | 38,380.00 USD | `-16.86%` | `285,372,900,000,000.00` |
| `Live` | `Long` | `0.1355` | 817,610.00 USD | 0.00 USD | 3,540.00 USD | `-16.24%` | `26,114,400,000,000.00` |
| `Live` | `Long` | `0.1365` | 814,070.00 USD | 0.00 USD | 13,440.00 USD | `-15.62%` | `98,483,600,000,000.00` |
| `Live` | `Long` | `0.1375` | 800,630.00 USD | 0.00 USD | 13,710.00 USD | `-15.00%` | `99,721,600,000,000.00` |
| `Live` | `Long` | `0.1385` | 786,920.00 USD | 0.00 USD | 4,330.00 USD | `-14.38%` | `31,259,100,000,000.00` |
| `Live` | `Long` | `0.1395` | 782,590.00 USD | 0.00 USD | 21,040.00 USD | `-13.77%` | `150,793,900,000,000.00` |
| `Live` | `Long` | `0.1405` | 761,550.00 USD | 0.00 USD | 2,640.00 USD | `-13.15%` | `18,781,700,000,000.00` |
| `Live` | `Long` | `0.1415` | 758,920.00 USD | 0.00 USD | 8,950.00 USD | `-12.53%` | `63,238,400,000,000.00` |
| `Live` | `Long` | `0.1425` | 749,970.00 USD | 0.00 USD | 499,030.00 USD | `-11.91%` | `3,501,939,200,000,000.00` |
| `Live` | `Long` | `0.1435` | 250,940.00 USD | 0.00 USD | 19,140.00 USD | `-11.29%` | `133,388,500,000,000.00` |
| `Live` | `Long` | `0.1445` | 231,800.00 USD | 0.00 USD | 9,510.00 USD | `-10.68%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 222,290.00 USD | 0.00 USD | 92,080.00 USD | `-10.06%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 130,210.00 USD | 0.00 USD | 23,540.00 USD | `-9.44%` | `160,700,100,000,000.00` |
| `Live` | `Long` | `0.1475` | 106,660.00 USD | 0.00 USD | 82,980.00 USD | `-8.82%` | `562,602,100,000,000.00` |
| `Live` | `Long` | `0.1485` | 23,680.00 USD | 0.00 USD | 2,290.00 USD | `-8.20%` | `15,410,500,000,000.00` |
| `Live` | `Long` | `0.1495` | 21,390.00 USD | 0.00 USD | 937.17 USD | `-7.58%` | `6,268,700,000,000.00` |
| `Live` | `Long` | `0.1535` | 20,460.00 USD | 0.00 USD | 8,620.00 USD | `-5.11%` | `56,165,700,000,000.00` |
| `Live` | `Long` | `0.1555` | 11,830.00 USD | 0.00 USD | 2,170.00 USD | `-3.88%` | `13,965,000,000,000.00` |
| `Live` | `Long` | `0.1565` | 9,660.00 USD | 0.00 USD | 9,660.00 USD | `-3.26%` | `61,740,200,000,000.00` |
| `Live` | `Short` | `0.1635` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | `+1.07%` | `14,355,700,000,000.00` |
| `Live` | `Short` | `0.1675` | 6,990.00 USD | 4,640.00 USD | 0.00 USD | `+3.54%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1695` | 18,310.00 USD | 11,320.00 USD | 0.00 USD | `+4.78%` | `66,784,399,999,999.99` |
| `Live` | `Short` | `0.1705` | 18,760.00 USD | 448.16 USD | 0.00 USD | `+5.40%` | `2,628,500,000,000.00` |
| `Live` | `Short` | `0.1715` | 21,980.00 USD | 3,220.00 USD | 0.00 USD | `+6.01%` | `18,797,800,000,000.00` |
| `Live` | `Short` | `0.1735` | 23,180.00 USD | 1,190.00 USD | 0.00 USD | `+7.25%` | `6,881,100,000,000.00` |
| `Live` | `Short` | `0.1785` | 23,320.00 USD | 138.82 USD | 0.00 USD | `+10.34%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1795` | 25,170.00 USD | 1,850.00 USD | 0.00 USD | `+10.96%` | `10,330,000,000,000.00` |
| `Live` | `Short` | `0.1815` | 25,310.00 USD | 135.29 USD | 0.00 USD | `+12.20%` | `745,400,000,000.00` |
| `Live` | `Short` | `0.1845` | 27,690.00 USD | 2,390.00 USD | 0.00 USD | `+14.05%` | `12,933,500,000,000.00` |
| `Live` | `Short` | `0.1855` | 28,310.00 USD | 616.01 USD | 0.00 USD | `+14.67%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 29,200.00 USD | 893.89 USD | 0.00 USD | `+15.91%` | `4,767,400,000,000.00` |
| `Live` | `Short` | `0.1945` | 33,390.00 USD | 4,190.00 USD | 0.00 USD | `+20.23%` | `21,520,800,000,000.00` |
| `Live` | `Short` | `0.1975` | 33,540.00 USD | 150.10 USD | 0.00 USD | `+22.09%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 45,130.00 USD | 11,590.00 USD | 0.00 USD | `+27.03%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2065` | 45,310.00 USD | 176.60 USD | 0.00 USD | `+27.65%` | `855,200,000,000.00` |
| `Live` | `Short` | `0.2075` | 58,880.00 USD | 13,570.00 USD | 0.00 USD | `+28.27%` | `65,394,900,000,000.00` |
| `Live` | `Short` | `0.2085` | 59,350.00 USD | 474.40 USD | 0.00 USD | `+28.89%` | `2,275,300,000,000.00` |
| `Live` | `Short` | `0.2095` | 59,510.00 USD | 164.23 USD | 0.00 USD | `+29.50%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2105` | 59,710.00 USD | 190.73 USD | 0.00 USD | `+30.12%` | `906,100,000,000.00` |
| `Live` | `Short` | `0.2135` | 75,400.00 USD | 15,690.00 USD | 0.00 USD | `+31.98%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 121,070.00 USD | 45,680.00 USD | 0.00 USD | `+33.21%` | `211,952,600,000,000.00` |
| `Live` | `Short` | `0.2175` | 121,290.00 USD | 213.22 USD | 0.00 USD | `+34.45%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 209,440.00 USD | 88,150.00 USD | 0.00 USD | `+35.69%` | `401,602,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 209,550.00 USD | 114.52 USD | 0.00 USD | `+38.16%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 209,710.00 USD | 154.78 USD | 0.00 USD | `+39.40%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 216,690.00 USD | 6,980.00 USD | 0.00 USD | `+41.87%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 232,620.00 USD | 15,930.00 USD | 0.00 USD | `+45.58%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 232,720.00 USD | 102.62 USD | 0.00 USD | `+46.81%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2395` | 254,660.00 USD | 21,940.00 USD | 0.00 USD | `+48.05%` | `91,595,600,000,000.00` |
| `Live` | `Short` | `0.2425` | 255,460.00 USD | 796.25 USD | 0.00 USD | `+49.90%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2435` | 304,160.00 USD | 48,700.00 USD | 0.00 USD | `+50.52%` | `200,003,000,000,000.00` |
| `Live` | `Short` | `0.2455` | 304,390.00 USD | 231.97 USD | 0.00 USD | `+51.76%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2545` | 304,940.00 USD | 546.54 USD | 0.00 USD | `+57.32%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 310,390.00 USD | 5,450.00 USD | 0.00 USD | `+58.56%` | `21,255,100,000,000.00` |
| `Live` | `Short` | `0.2575` | 336,960.00 USD | 26,570.00 USD | 0.00 USD | `+59.18%` | `103,191,700,000,000.00` |
| `Live` | `Short` | `0.2585` | 391,920.00 USD | 54,960.00 USD | 0.00 USD | `+59.79%` | `212,629,500,000,000.00` |
| `Live` | `Short` | `0.2615` | 392,080.00 USD | 154.94 USD | 0.00 USD | `+61.65%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 392,310.00 USD | 226.51 USD | 0.00 USD | `+65.98%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2695` | 578,970.00 USD | 186,670.00 USD | 0.00 USD | `+66.59%` | `692,636,800,000,000.00` |
| `Live` | `Short` | `0.2715` | 592,210.00 USD | 13,240.00 USD | 0.00 USD | `+67.83%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 592,430.00 USD | 214.21 USD | 0.00 USD | `+68.45%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 604,030.00 USD | 11,600.00 USD | 0.00 USD | `+69.69%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2755` | 616,120.00 USD | 12,100.00 USD | 0.00 USD | `+70.30%` | `43,905,000,000,000.00` |
| `Live` | `Short` | `0.2765` | 618,230.00 USD | 2,100.00 USD | 0.00 USD | `+70.92%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2795` | 618,710.00 USD | 482.84 USD | 0.00 USD | `+72.78%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 618,900.00 USD | 187.26 USD | 0.00 USD | `+80.19%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 619,690.00 USD | 794.52 USD | 0.00 USD | `+80.81%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.3005` | 621,590.00 USD | 1,900.00 USD | 0.00 USD | `+85.76%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.3065` | 899,970.00 USD | 278,380.00 USD | 0.00 USD | `+89.47%` | `908,260,900,000,000.00` |
| `Live` | `Short` | `0.3075` | 906,270.00 USD | 6,290.00 USD | 0.00 USD | `+90.08%` | `20,460,400,000,000.00` |
| `Live` | `Short` | `0.3085` | 906,630.00 USD | 363.72 USD | 0.00 USD | `+90.70%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3095` | 907,120.00 USD | 492.26 USD | 0.00 USD | `+91.32%` | `1,590,500,000,000.00` |
| `Live` | `Short` | `0.3105` | 919,290.00 USD | 12,170.00 USD | 0.00 USD | `+91.94%` | `39,182,800,000,000.00` |
| `Live` | `Short` | `0.3115` | 919,930.00 USD | 640.88 USD | 0.00 USD | `+92.56%` | `2,057,400,000,000.00` |
| `Live` | `Short` | `0.3125` | 921,460.00 USD | 1,530.00 USD | 0.00 USD | `+93.18%` | `4,897,100,000,000.00` |
| `Live` | `Short` | `0.3175` | 921,690.00 USD | 227.49 USD | 0.00 USD | `+96.27%` | `716,500,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 786,190.00 USD | 0.00 USD | 355.00 USD | `-78.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 785,830.00 USD | 0.00 USD | 297.50 USD | `-73.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 785,530.00 USD | 0.00 USD | 353.50 USD | `-68.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 785,180.00 USD | 0.00 USD | 276.53 USD | `-66.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 784,900.00 USD | 0.00 USD | 4,310.00 USD | `-65.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 780,590.00 USD | 0.00 USD | 475.11 USD | `-60.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 780,120.00 USD | 0.00 USD | 131.16 USD | `-59.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 779,980.00 USD | 0.00 USD | 881.45 USD | `-58.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 779,100.00 USD | 0.00 USD | 1,070.00 USD | `-58.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 778,030.00 USD | 0.00 USD | 1,050.00 USD | `-57.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 776,980.00 USD | 0.00 USD | 1,010.00 USD | `-57.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 775,970.00 USD | 0.00 USD | 4,100.00 USD | `-56.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 771,870.00 USD | 0.00 USD | 529.04 USD | `-55.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 771,340.00 USD | 0.00 USD | 2,390.00 USD | `-55.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 768,950.00 USD | 0.00 USD | 757.39 USD | `-53.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 768,190.00 USD | 0.00 USD | 1,490.00 USD | `-51.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 766,710.00 USD | 0.00 USD | 255.36 USD | `-47.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 766,450.00 USD | 0.00 USD | 277.37 USD | `-46.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 766,170.00 USD | 0.00 USD | 262.50 USD | `-45.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 765,910.00 USD | 0.00 USD | 795.57 USD | `-45.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 765,120.00 USD | 0.00 USD | 181.00 USD | `-44.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 764,930.00 USD | 0.00 USD | 3,810.00 USD | `-37.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 761,120.00 USD | 0.00 USD | 1,550.00 USD | `-36.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 759,580.00 USD | 0.00 USD | 116.07 USD | `-33.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 759,460.00 USD | 0.00 USD | 19,070.00 USD | `-32.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 740,390.00 USD | 0.00 USD | 577.22 USD | `-31.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 739,810.00 USD | 0.00 USD | 343.50 USD | `-29.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 739,470.00 USD | 0.00 USD | 26,280.00 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 713,190.00 USD | 0.00 USD | 4,870.00 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 708,320.00 USD | 0.00 USD | 83,620.00 USD | `-24.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 624,690.00 USD | 0.00 USD | 487.10 USD | `-24.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 624,210.00 USD | 0.00 USD | 14,940.00 USD | `-23.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 609,270.00 USD | 0.00 USD | 129,320.00 USD | `-22.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 479,950.00 USD | 0.00 USD | 2,670.00 USD | `-21.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 477,280.00 USD | 0.00 USD | 473.27 USD | `-21.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 476,810.00 USD | 0.00 USD | 203,210.00 USD | `-20.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 273,600.00 USD | 0.00 USD | 1,670.00 USD | `-19.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 271,930.00 USD | 0.00 USD | 1,590.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 270,330.00 USD | 0.00 USD | 6,000.00 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 264,330.00 USD | 0.00 USD | 625.78 USD | `-17.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 263,700.00 USD | 0.00 USD | 502.28 USD | `-16.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 263,200.00 USD | 0.00 USD | 162.60 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 263,040.00 USD | 0.00 USD | 700.86 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 262,340.00 USD | 0.00 USD | 13,710.00 USD | `-15.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 248,630.00 USD | 0.00 USD | 108.57 USD | `-14.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 248,520.00 USD | 0.00 USD | 4,210.00 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 244,310.00 USD | 0.00 USD | 127.35 USD | `-12.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 244,180.00 USD | 0.00 USD | 24,850.00 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 219,330.00 USD | 0.00 USD | 1,300.00 USD | `-11.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 218,030.00 USD | 0.00 USD | 1,960.00 USD | `-10.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 216,070.00 USD | 0.00 USD | 46,010.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 170,070.00 USD | 0.00 USD | 17,490.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 152,580.00 USD | 0.00 USD | 2,400.00 USD | `-8.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 150,170.00 USD | 0.00 USD | 2,610.00 USD | `-8.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 147,560.00 USD | 0.00 USD | 1,540.00 USD | `-7.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 146,020.00 USD | 0.00 USD | 3,010.00 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 143,010.00 USD | 0.00 USD | 3,430.00 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 139,580.00 USD | 0.00 USD | 2,990.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 136,590.00 USD | 0.00 USD | 38,030.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 98,560.00 USD | 0.00 USD | 9,010.00 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 89,550.00 USD | 0.00 USD | 23,370.00 USD | `-3.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 66,180.00 USD | 0.00 USD | 14,540.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 51,630.00 USD | 0.00 USD | 499.16 USD | `-2.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 51,130.00 USD | 0.00 USD | 9,980.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 41,150.00 USD | 0.00 USD | 21,740.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 19,420.00 USD | 0.00 USD | 19,290.00 USD | `-0.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 126.63 USD | 0.00 USD | 126.63 USD | `-0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1625` | 107.35 USD | 107.35 USD | 0.00 USD | `+0.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1635` | 1,800.00 USD | 1,690.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 1,950.00 USD | 151.44 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 7,120.00 USD | 5,170.00 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 13,250.00 USD | 6,130.00 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 15,410.00 USD | 2,160.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 16,560.00 USD | 1,150.00 USD | 0.00 USD | `+4.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 16,840.00 USD | 279.93 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 17,400.00 USD | 564.90 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 19,200.00 USD | 1,800.00 USD | 0.00 USD | `+6.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 19,910.00 USD | 706.39 USD | 0.00 USD | `+6.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 20,570.00 USD | 661.31 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 20,790.00 USD | 219.54 USD | 0.00 USD | `+7.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 21,880.00 USD | 1,100.00 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 22,670.00 USD | 790.28 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 23,010.00 USD | 336.40 USD | 0.00 USD | `+9.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 23,910.00 USD | 898.02 USD | 0.00 USD | `+10.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 28,940.00 USD | 5,030.00 USD | 0.00 USD | `+10.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 40,600.00 USD | 11,660.00 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 51,440.00 USD | 10,840.00 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 52,310.00 USD | 864.12 USD | 0.00 USD | `+12.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 54,830.00 USD | 2,520.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 55,110.00 USD | 276.75 USD | 0.00 USD | `+14.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 55,240.00 USD | 128.68 USD | 0.00 USD | `+14.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 58,610.00 USD | 3,370.00 USD | 0.00 USD | `+15.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 62,310.00 USD | 3,700.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 62,560.00 USD | 245.50 USD | 0.00 USD | `+16.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 63,090.00 USD | 531.47 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 63,780.00 USD | 697.34 USD | 0.00 USD | `+17.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 64,010.00 USD | 222.24 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 93,130.00 USD | 29,130.00 USD | 0.00 USD | `+19.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 100,200.00 USD | 7,070.00 USD | 0.00 USD | `+19.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 100,400.00 USD | 194.50 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 100,540.00 USD | 137.77 USD | 0.00 USD | `+20.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 100,670.00 USD | 133.19 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 104,420.00 USD | 3,750.00 USD | 0.00 USD | `+22.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 104,910.00 USD | 492.19 USD | 0.00 USD | `+23.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 127,670.00 USD | 22,750.00 USD | 0.00 USD | `+23.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 128,230.00 USD | 560.96 USD | 0.00 USD | `+24.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 149,570.00 USD | 21,340.00 USD | 0.00 USD | `+25.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 149,940.00 USD | 371.35 USD | 0.00 USD | `+25.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 235,830.00 USD | 85,900.00 USD | 0.00 USD | `+26.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 237,300.00 USD | 1,470.00 USD | 0.00 USD | `+27.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 237,470.00 USD | 174.20 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 239,550.00 USD | 2,080.00 USD | 0.00 USD | `+28.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 239,800.00 USD | 252.51 USD | 0.00 USD | `+29.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 242,170.00 USD | 2,370.00 USD | 0.00 USD | `+30.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 242,530.00 USD | 356.72 USD | 0.00 USD | `+31.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 242,890.00 USD | 360.08 USD | 0.00 USD | `+32.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 243,250.00 USD | 361.76 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 243,610.00 USD | 363.44 USD | 0.00 USD | `+33.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 243,980.00 USD | 365.12 USD | 0.00 USD | `+34.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 250,260.00 USD | 6,280.00 USD | 0.00 USD | `+35.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 250,620.00 USD | 368.47 USD | 0.00 USD | `+35.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 273,120.00 USD | 22,490.00 USD | 0.00 USD | `+36.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 273,450.00 USD | 333.91 USD | 0.00 USD | `+37.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 277,430.00 USD | 3,980.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 277,800.00 USD | 378.55 USD | 0.00 USD | `+39.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 278,180.00 USD | 380.23 USD | 0.00 USD | `+40.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 282,020.00 USD | 3,840.00 USD | 0.00 USD | `+41.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 312,360.00 USD | 30,340.00 USD | 0.00 USD | `+42.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 316,620.00 USD | 4,260.00 USD | 0.00 USD | `+43.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 318,130.00 USD | 1,520.00 USD | 0.00 USD | `+44.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 339,360.00 USD | 21,230.00 USD | 0.00 USD | `+46.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 341,890.00 USD | 2,530.00 USD | 0.00 USD | `+47.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 348,710.00 USD | 6,820.00 USD | 0.00 USD | `+48.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 358,010.00 USD | 9,300.00 USD | 0.00 USD | `+49.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 359,920.00 USD | 1,910.00 USD | 0.00 USD | `+51.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 379,750.00 USD | 19,820.00 USD | 0.00 USD | `+52.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 380,300.00 USD | 551.23 USD | 0.00 USD | `+52.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 380,700.00 USD | 397.90 USD | 0.00 USD | `+54.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 385,030.00 USD | 4,330.00 USD | 0.00 USD | `+54.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 385,350.00 USD | 320.66 USD | 0.00 USD | `+55.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 401,230.00 USD | 15,880.00 USD | 0.00 USD | `+56.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 403,230.00 USD | 2,000.00 USD | 0.00 USD | `+57.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 405,790.00 USD | 2,550.00 USD | 0.00 USD | `+57.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 417,520.00 USD | 11,730.00 USD | 0.00 USD | `+58.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 422,680.00 USD | 5,160.00 USD | 0.00 USD | `+59.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 439,540.00 USD | 16,870.00 USD | 0.00 USD | `+60.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 466,330.00 USD | 26,790.00 USD | 0.00 USD | `+61.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 466,600.00 USD | 272.88 USD | 0.00 USD | `+67.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 466,720.00 USD | 114.99 USD | 0.00 USD | `+70.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 467,110.00 USD | 394.01 USD | 0.00 USD | `+70.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 467,490.00 USD | 375.53 USD | 0.00 USD | `+73.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 469,620.00 USD | 2,130.00 USD | 0.00 USD | `+76.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 470,200.00 USD | 579.27 USD | 0.00 USD | `+77.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 471,950.00 USD | 1,750.00 USD | 0.00 USD | `+79.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 472,050.00 USD | 101.21 USD | 0.00 USD | `+82.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 472,320.00 USD | 262.73 USD | 0.00 USD | `+83.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 473,750.00 USD | 1,440.00 USD | 0.00 USD | `+83.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 479,190.00 USD | 5,430.00 USD | 0.00 USD | `+85.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 484,610.00 USD | 5,430.00 USD | 0.00 USD | `+86.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 484,900.00 USD | 289.61 USD | 0.00 USD | `+88.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 485,390.00 USD | 487.09 USD | 0.00 USD | `+89.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 491,960.00 USD | 6,570.00 USD | 0.00 USD | `+91.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 497,140.00 USD | 5,180.00 USD | 0.00 USD | `+94.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 514,650.00 USD | 17,520.00 USD | 0.00 USD | `+96.88%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1310` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 6,470.00 USD | 4,610.00 USD | 5,180.00 USD |
| `7D` | `0.1313` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 0.00 USD | 4,010.00 USD | 2,660.00 USD |
| `7D` | `0.1316` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 9,620.00 USD | 4,840.00 USD | 2,140.00 USD |
| `7D` | `0.1319` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 4,630.00 USD | 0.00 USD | 18,380.00 USD |
| `7D` | `0.1322` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 5,580.00 USD | 2,780.00 USD | 17,750.00 USD |
| `7D` | `0.1325` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 0.00 USD | 5,550.00 USD | 4,560.00 USD |
| `7D` | `0.1328` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 19,000.00 USD | 7,370.00 USD | 8,920.00 USD |
| `7D` | `0.1331` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 13,420.00 USD | 4,240.00 USD | 7,210.00 USD |
| `7D` | `0.1334` | 7,950,000.00 USD | 0.00 USD | 7,950,000.00 USD | 3,580.00 USD | 3,230.00 USD | 7,810.00 USD |
| `7D` | `0.1337` | 7,940,000.00 USD | 0.00 USD | 7,940,000.00 USD | 2,830.00 USD | 4,520.00 USD | 19,560.00 USD |
| `7D` | `0.1340` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 6,330.00 USD | 5,970.00 USD | 13,100.00 USD |
| `7D` | `0.1343` | 7,880,000.00 USD | 0.00 USD | 7,880,000.00 USD | 0.00 USD | 5,790.00 USD | 13,540.00 USD |
| `7D` | `0.1346` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 33,130.00 USD | 5,000.00 USD | 21,650.00 USD |
| `7D` | `0.1349` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 4,450.00 USD | 2,140.00 USD | 19,300.00 USD |
| `7D` | `0.1352` | 7,780,000.00 USD | 0.00 USD | 7,780,000.00 USD | 11,390.00 USD | 6,290.00 USD | 13,140.00 USD |
| `7D` | `0.1355` | 7,750,000.00 USD | 0.00 USD | 7,750,000.00 USD | 7,540.00 USD | 9,000.00 USD | 6,460.00 USD |
| `7D` | `0.1358` | 7,720,000.00 USD | 0.00 USD | 7,720,000.00 USD | 25,150.00 USD | 9,870.00 USD | 5,370.00 USD |
| `7D` | `0.1361` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 8,700.00 USD | 1,930.00 USD | 6,320.00 USD |
| `7D` | `0.1364` | 7,670,000.00 USD | 0.00 USD | 7,670,000.00 USD | 15,000.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1367` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 4,500.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1370` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1373` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 4,620.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1379` | 7,590,000.00 USD | 0.00 USD | 7,590,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1385` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 11,880.00 USD | 0.00 USD | 42,090.00 USD |
| `7D` | `0.1388` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 17,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1391` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 0.00 USD | 4,690.00 USD | 50,050.00 USD |
| `7D` | `0.1394` | 7,450,000.00 USD | 0.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 5,950.00 USD |
| `7D` | `0.1397` | 7,440,000.00 USD | 0.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 22,820.00 USD |
| `7D` | `0.1400` | 7,420,000.00 USD | 0.00 USD | 7,420,000.00 USD | 6,210.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `0.1403` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 5,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1418` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 0.00 USD | 0.00 USD | 14,680.00 USD |
| `7D` | `0.1421` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1436` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 15,360.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1439` | 7,330,000.00 USD | 0.00 USD | 7,330,000.00 USD | 14,190.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1442` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1447` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 0.00 USD | 5,160.00 USD | 0.00 USD |
| `1D` | `0.1451` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1451` | 7,310,000.00 USD | 0.00 USD | 7,310,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `1D` | `0.1453` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1455` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 3,450.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1457` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1459` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1461` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 0.00 USD | 3,000.00 USD | 1,760.00 USD |
| `1D` | `0.1463` | 4,630,000.00 USD | 0.00 USD | 4,630,000.00 USD | 9,940.00 USD | 2,690.00 USD | 3,130.00 USD |
| `1D` | `0.1465` | 4,610,000.00 USD | 0.00 USD | 4,610,000.00 USD | 11,020.00 USD | 5,840.00 USD | 10,350.00 USD |
| `7D` | `0.1466` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 9,720.00 USD | 5,520.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD |
| `1D` | `0.1469` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD |
| `7D` | `0.1469` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 6,230.00 USD | 0.00 USD | 3,880.00 USD |
| `1D` | `0.1471` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD |
| `7D` | `0.1472` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 12,940.00 USD | 3,390.00 USD | 14,170.00 USD |
| `1D` | `0.1473` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD |
| `1D` | `0.1475` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD |
| `7D` | `0.1475` | 7,150,000.00 USD | 0.00 USD | 7,150,000.00 USD | 24,840.00 USD | 13,040.00 USD | 10,360.00 USD |
| `1D` | `0.1477` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD |
| `7D` | `0.1478` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 110,850.00 USD | 33,410.00 USD | 125,110.00 USD |
| `1D` | `0.1479` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD |
| `1D` | `0.1481` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD |
| `7D` | `0.1481` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 41,960.00 USD | 31,150.00 USD | 25,160.00 USD |
| `1D` | `0.1483` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD |
| `7D` | `0.1484` | 6,740,000.00 USD | 0.00 USD | 6,740,000.00 USD | 12,060.00 USD | 3,040.00 USD | 194,160.00 USD |
| `1D` | `0.1485` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD |
| `1D` | `0.1487` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 8,840.00 USD | 3,580.00 USD | 11,900.00 USD |
| `7D` | `0.1487` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 61,970.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1489` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD |
| `7D` | `0.1490` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 38,870.00 USD | 14,820.00 USD | 77,920.00 USD |
| `1D` | `0.1491` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD |
| `1D` | `0.1493` | 3,570,000.00 USD | 0.00 USD | 3,570,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD |
| `7D` | `0.1493` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 27,770.00 USD | 17,120.00 USD | 20,270.00 USD |
| `1D` | `0.1495` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 57,850.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1496` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 29,430.00 USD | 13,380.00 USD | 195,710.00 USD |
| `1D` | `0.1497` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 8,630.00 USD | 0.00 USD | 347.81 USD |
| `1D` | `0.1499` | 3,440,000.00 USD | 0.00 USD | 3,440,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD |
| `7D` | `0.1499` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 60,500.00 USD | 9,610.00 USD | 17,350.00 USD |
| `1D` | `0.1501` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD |
| `7D` | `0.1502` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 2,610.00 USD | 9,860.00 USD | 4,600.00 USD |
| `1D` | `0.1503` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 48,710.00 USD | 4,400.00 USD | 154,490.00 USD |
| `1D` | `0.1505` | 3,190,000.00 USD | 0.00 USD | 3,190,000.00 USD | 35,380.00 USD | 1,940.00 USD | 6,750.00 USD |
| `7D` | `0.1505` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 67,080.00 USD | 21,620.00 USD | 52,590.00 USD |
| `1D` | `0.1507` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD |
| `7D` | `0.1508` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 151,240.00 USD | 4,870.00 USD | 248,410.00 USD |
| `1D` | `0.1509` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD |
| `1D` | `0.1511` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD |
| `7D` | `0.1511` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 86,820.00 USD | 11,590.00 USD | 38,070.00 USD |
| `1D` | `0.1513` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD |
| `7D` | `0.1514` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 0.00 USD | 15,050.00 USD | 367,590.00 USD |
| `1D` | `0.1515` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD |
| `1D` | `0.1517` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD |
| `7D` | `0.1517` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 96,310.00 USD | 4,290.00 USD | 119,870.00 USD |
| `1D` | `0.1519` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD |
| `7D` | `0.1520` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 0.00 USD | 22,600.00 USD | 156,830.00 USD |
| `1D` | `0.1521` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `1D` | `0.1523` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1523` | 4,420,000.00 USD | 0.00 USD | 4,420,000.00 USD | 0.00 USD | 15,080.00 USD | 0.00 USD |
| `1D` | `0.1525` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1526` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 0.00 USD | 38,870.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1529` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD |
| `7D` | `0.1529` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 0.00 USD | 6,020.00 USD | 0.00 USD |
| `1D` | `0.1531` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD |
| `7D` | `0.1532` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 0.00 USD | 14,780.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD |
| `1D` | `0.1535` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD |
| `7D` | `0.1535` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 35,470.00 USD | 8,570.00 USD | 0.00 USD |
| `1D` | `0.1537` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD |
| `7D` | `0.1538` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 0.00 USD | 14,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1541` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1541` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD |
| `7D` | `0.1544` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1547` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD |
| `7D` | `0.1547` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 0.00 USD | 12,560.00 USD | 89,090.00 USD |
| `1D` | `0.1549` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD |
| `7D` | `0.1550` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 0.00 USD | 16,530.00 USD | 0.00 USD |
| `1D` | `0.1551` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 11,600.00 USD | 10,490.00 USD | 5,050.00 USD |
| `1D` | `0.1553` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 7,900.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1553` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 0.00 USD | 7,730.00 USD | 0.00 USD |
| `1D` | `0.1555` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 40,830.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1556` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 2,800.00 USD | 11,690.00 USD | 3,080.00 USD |
| `1D` | `0.1559` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 14,470.00 USD | 2,970.00 USD | 4,410.00 USD |
| `7D` | `0.1559` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1561` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 12,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1562` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 0.00 USD | 10,580.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,750,000.00 USD | 0.00 USD | 1,750,000.00 USD | 11,460.00 USD | 19,080.00 USD | 2,050.00 USD |
| `1D` | `0.1565` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD |
| `7D` | `0.1565` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 70,940.00 USD | 28,480.00 USD | 0.00 USD |
| `1D` | `0.1567` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD |
| `7D` | `0.1568` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 111,700.00 USD | 10,060.00 USD | 151,620.00 USD |
| `1D` | `0.1569` | 1,590,000.00 USD | 0.00 USD | 1,590,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD |
| `1D` | `0.1571` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD |
| `7D` | `0.1571` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 194,660.00 USD | 13,570.00 USD | 58,840.00 USD |
| `1D` | `0.1573` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD |
| `7D` | `0.1574` | 3,300,000.00 USD | 0.00 USD | 3,300,000.00 USD | 77,250.00 USD | 79,780.00 USD | 34,380.00 USD |
| `1D` | `0.1575` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD |
| `1D` | `0.1577` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD |
| `7D` | `0.1577` | 3,100,000.00 USD | 0.00 USD | 3,100,000.00 USD | 31,130.00 USD | 118,000.00 USD | 0.00 USD |
| `1D` | `0.1579` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD |
| `7D` | `0.1580` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 216,490.00 USD | 46,710.00 USD | 22,580.00 USD |
| `1D` | `0.1581` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD |
| `1D` | `0.1583` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD |
| `7D` | `0.1583` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 70,150.00 USD | 17,610.00 USD | 24,510.00 USD |
| `1D` | `0.1585` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 16,540.00 USD | 17,270.00 USD | 6,620.00 USD |
| `7D` | `0.1586` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 59,180.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1587` | 969,900.00 USD | 0.00 USD | 969,900.00 USD | 42,230.00 USD | 24,370.00 USD | 45,250.00 USD |
| `1D` | `0.1589` | 858,060.00 USD | 0.00 USD | 858,060.00 USD | 20,380.00 USD | 10,830.00 USD | 44,860.00 USD |
| `7D` | `0.1589` | 2,470,000.00 USD | 0.00 USD | 2,470,000.00 USD | 59,670.00 USD | 12,590.00 USD | 89,310.00 USD |
| `1D` | `0.1591` | 781,990.00 USD | 0.00 USD | 781,990.00 USD | 15,370.00 USD | 19,200.00 USD | 38,490.00 USD |
| `7D` | `0.1592` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 16,720.00 USD |
| `1D` | `0.1593` | 708,920.00 USD | 0.00 USD | 708,920.00 USD | 14,950.00 USD | 32,920.00 USD | 30,140.00 USD |
| `1D` | `0.1595` | 630,900.00 USD | 0.00 USD | 630,900.00 USD | 10,260.00 USD | 1,210.00 USD | 3,490.00 USD |
| `7D` | `0.1595` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 0.00 USD | 37,130.00 USD | 0.00 USD |
| `1D` | `0.1597` | 615,940.00 USD | 0.00 USD | 615,940.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `0.1598` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 0.00 USD | 86,680.00 USD | 75,810.00 USD |
| `1D` | `0.1599` | 598,130.00 USD | 0.00 USD | 598,130.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD |
| `1D` | `0.1601` | 590,540.00 USD | 0.00 USD | 590,540.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1601` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 0.00 USD | 47,500.00 USD | 0.00 USD |
| `1D` | `0.1603` | 566,890.00 USD | 0.00 USD | 566,890.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1604` | 2,050,000.00 USD | 0.00 USD | 2,050,000.00 USD | 98,670.00 USD | 21,760.00 USD | 273,670.00 USD |
| `1D` | `0.1605` | 524,390.00 USD | 0.00 USD | 524,390.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1607` | 471,760.00 USD | 0.00 USD | 471,760.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD |
| `7D` | `0.1607` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 166,880.00 USD | 0.00 USD | 370,770.00 USD |
| `1D` | `0.1609` | 449,250.00 USD | 0.00 USD | 449,250.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD |
| `7D` | `0.1610` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 178,210.00 USD | 11,640.00 USD | 178,270.00 USD |
| `1D` | `0.1611` | 301,230.00 USD | 0.00 USD | 301,230.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD |
| `1D` | `0.1613` | 125,680.00 USD | 0.00 USD | 125,680.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD |
| `7D` | `0.1613` | 748,360.00 USD | 0.00 USD | 748,360.00 USD | 321,740.00 USD | 10,980.00 USD | 415,640.00 USD |
| `1D` | `0.1615` | 62,310.00 USD | 0.00 USD | 62,310.00 USD | 0.00 USD | 41,050.00 USD | 21,260.00 USD |
| `7D` | `0.1616` | 271,830.00 USD | 271,830.00 USD | 0.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD |
| `7D` | `0.1616` | 543,650.00 USD | 543,650.00 USD | 0.00 USD | 187,590.00 USD | 35,210.00 USD | 49,020.00 USD |
| `1D` | `0.1617` | 34,490.00 USD | 34,490.00 USD | 0.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD |
| `1D` | `0.1617` | 68,980.00 USD | 68,980.00 USD | 0.00 USD | 0.00 USD | 8,790.00 USD | 25,700.00 USD |
| `1D` | `0.1619` | 117,860.00 USD | 117,860.00 USD | 0.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD |
| `7D` | `0.1619` | 620,320.00 USD | 620,320.00 USD | 0.00 USD | 29,070.00 USD | 0.00 USD | 47,590.00 USD |
| `1D` | `0.1621` | 123,520.00 USD | 123,520.00 USD | 0.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD |
| `7D` | `0.1622` | 775,540.00 USD | 775,540.00 USD | 0.00 USD | 49,670.00 USD | 105,540.00 USD | 0.00 USD |
| `1D` | `0.1623` | 140,550.00 USD | 140,550.00 USD | 0.00 USD | 0.00 USD | 17,020.00 USD | 0.00 USD |
| `1D` | `0.1625` | 226,000.00 USD | 226,000.00 USD | 0.00 USD | 38,240.00 USD | 0.00 USD | 47,210.00 USD |
| `7D` | `0.1625` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 122,430.00 USD | 136,760.00 USD |
| `1D` | `0.1627` | 287,460.00 USD | 287,460.00 USD | 0.00 USD | 0.00 USD | 20,350.00 USD | 41,120.00 USD |
| `7D` | `0.1628` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1629` | 392,600.00 USD | 392,600.00 USD | 0.00 USD | 0.00 USD | 3,520.00 USD | 101,620.00 USD |
| `7D` | `0.1631` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1635` | 401,300.00 USD | 401,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1637` | 416,170.00 USD | 416,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `1D` | `0.1649` | 422,100.00 USD | 422,100.00 USD | 0.00 USD | 5,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1651` | 438,230.00 USD | 438,230.00 USD | 0.00 USD | 16,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1653` | 461,470.00 USD | 461,470.00 USD | 0.00 USD | 17,080.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1657` | 476,420.00 USD | 476,420.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1661` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 103,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1663` | 557,500.00 USD | 557,500.00 USD | 0.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD |
| `7D` | `0.1664` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 104,470.00 USD | 0.00 USD | 57,360.00 USD |
| `1D` | `0.1665` | 594,840.00 USD | 594,840.00 USD | 0.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD |
| `1D` | `0.1667` | 636,750.00 USD | 636,750.00 USD | 0.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD |
| `7D` | `0.1667` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 42,580.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.1669` | 664,520.00 USD | 664,520.00 USD | 0.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD |
| `7D` | `0.1670` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 141,080.00 USD | 108,010.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 726,550.00 USD | 726,550.00 USD | 0.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD |
| `1D` | `0.1673` | 810,800.00 USD | 810,800.00 USD | 0.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD |
| `7D` | `0.1673` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 20,540.00 USD | 23,800.00 USD | 68,760.00 USD |
| `1D` | `0.1675` | 844,090.00 USD | 844,090.00 USD | 0.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD |
| `7D` | `0.1676` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 84,020.00 USD | 153,400.00 USD | 0.00 USD |
| `1D` | `0.1677` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD |
| `1D` | `0.1679` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD |
| `7D` | `0.1679` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 52,340.00 USD | 72,840.00 USD | 80,890.00 USD |
| `1D` | `0.1681` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 91,660.00 USD | 34,810.00 USD | 21,260.00 USD |
| `7D` | `0.1682` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 130,480.00 USD | 53,630.00 USD | 64,330.00 USD |
| `1D` | `0.1683` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 56,920.00 USD | 12,810.00 USD | 49,630.00 USD |
| `1D` | `0.1685` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 41,190.00 USD | 48,480.00 USD | 52,800.00 USD |
| `7D` | `0.1685` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 29,070.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1687` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 6,960.00 USD | 8,320.00 USD | 72,320.00 USD |
| `7D` | `0.1688` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 49,670.00 USD | 25,190.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 51,500.00 USD | 26,970.00 USD | 23,460.00 USD |
| `1D` | `0.1691` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 69,010.00 USD | 69,050.00 USD | 101,270.00 USD |
| `7D` | `0.1691` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 33,660.00 USD | 38,670.00 USD | 104,450.00 USD |
| `1D` | `0.1693` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 57,220.00 USD | 29,120.00 USD | 59,710.00 USD |
| `7D` | `0.1694` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 17,360.00 USD | 62,560.00 USD | 39,780.00 USD |
| `1D` | `0.1695` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD |
| `1D` | `0.1697` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD |
| `7D` | `0.1697` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 56,860.00 USD | 0.00 USD |
| `1D` | `0.1699` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD |
| `7D` | `0.1700` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 91,090.00 USD |
| `1D` | `0.1701` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `1D` | `0.1703` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD |
| `7D` | `0.1703` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 0.00 USD |
| `1D` | `0.1705` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD |
| `7D` | `0.1706` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 57,200.00 USD |
| `1D` | `0.1707` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD |
| `1D` | `0.1709` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD |
| `7D` | `0.1709` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 64,690.00 USD |
| `1D` | `0.1711` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD |
| `7D` | `0.1712` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 22,580.00 USD |
| `1D` | `0.1713` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD |
| `1D` | `0.1715` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD |
| `7D` | `0.1715` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 24,510.00 USD |
| `1D` | `0.1717` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD |
| `7D` | `0.1718` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 14,540.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1719` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD |
| `1D` | `0.1721` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD |
| `7D` | `0.1721` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 68,850.00 USD | 12,590.00 USD | 266,220.00 USD |
| `1D` | `0.1723` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD |
| `7D` | `0.1724` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 74,040.00 USD | 0.00 USD | 120,740.00 USD |
| `1D` | `0.1725` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD |
| `1D` | `0.1727` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD |
| `1D` | `0.1729` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1730` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 299,490.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD |
| `7D` | `0.1733` | 4,730,000.00 USD | 4,730,000.00 USD | 0.00 USD | 145,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1735` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD |
| `1D` | `0.1737` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD |
| `1D` | `0.1739` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 2,270.00 USD | 5,180.00 USD |
| `7D` | `0.1739` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1741` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `0.1743` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `1D` | `0.1745` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD |
| `7D` | `0.1745` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1747` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD |
| `7D` | `0.1748` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `0.1749` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD |
| `1D` | `0.1751` | 3,460,000.00 USD | 3,460,000.00 USD | 0.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD |
| `7D` | `0.1751` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 171,280.00 USD |
| `1D` | `0.1753` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD |
| `7D` | `0.1754` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 37,610.00 USD | 0.00 USD | 176,480.00 USD |
| `1D` | `0.1755` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD |
| `1D` | `0.1757` | 3,610,000.00 USD | 3,610,000.00 USD | 0.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD |
| `7D` | `0.1757` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 124,250.00 USD | 38,670.00 USD | 8,600.00 USD |
| `1D` | `0.1759` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD |
| `7D` | `0.1760` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 209,280.00 USD | 15,550.00 USD | 32,350.00 USD |
| `1D` | `0.1761` | 3,840,000.00 USD | 3,840,000.00 USD | 0.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD |
| `1D` | `0.1763` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD |
| `7D` | `0.1763` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 142,420.00 USD | 101,270.00 USD | 12,330.00 USD |
| `1D` | `0.1765` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD |
| `7D` | `0.1766` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 163,180.00 USD | 138,030.00 USD | 36,540.00 USD |
| `1D` | `0.1767` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD |
| `1D` | `0.1769` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD |
| `7D` | `0.1769` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 113,280.00 USD | 60,410.00 USD | 23,040.00 USD |
| `1D` | `0.1771` | 4,180,000.00 USD | 4,180,000.00 USD | 0.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD |
| `7D` | `0.1772` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 77,840.00 USD | 112,520.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD |
| `1D` | `0.1775` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD |
| `7D` | `0.1775` | 6,950,000.00 USD | 6,950,000.00 USD | 0.00 USD | 164,290.00 USD | 30,480.00 USD | 0.00 USD |
| `1D` | `0.1777` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD |
| `7D` | `0.1778` | 7,150,000.00 USD | 7,150,000.00 USD | 0.00 USD | 63,990.00 USD | 71,060.00 USD | 72,190.00 USD |
| `1D` | `0.1779` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 7,310.00 USD | 8,710.00 USD | 7,340.00 USD |
| `1D` | `0.1781` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 2,050.00 USD | 1,610.00 USD | 2,080.00 USD |
| `7D` | `0.1781` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 11,220.00 USD | 4,590.00 USD | 33,810.00 USD |
| `1D` | `0.1783` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1784` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 149,100.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 12,390.00 USD | 27,370.00 USD | 4,440.00 USD |
| `1D` | `0.1787` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD |
| `7D` | `0.1787` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 97,870.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1789` | 4,550,000.00 USD | 4,550,000.00 USD | 0.00 USD | 9,350.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1790` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 103,860.00 USD | 17,360.00 USD | 3,940.00 USD |
| `1D` | `0.1791` | 4,560,000.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,290.00 USD |
| `1D` | `0.1793` | 4,580,000.00 USD | 4,580,000.00 USD | 0.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD |
| `7D` | `0.1793` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 78,950.00 USD | 42,780.00 USD | 8,910.00 USD |
| `1D` | `0.1795` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD |
| `7D` | `0.1796` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 17,130.00 USD | 12,930.00 USD | 35,530.00 USD |
| `1D` | `0.1797` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD |
| `1D` | `0.1799` | 4,680,000.00 USD | 4,680,000.00 USD | 0.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD |
| `7D` | `0.1799` | 8,000,000.00 USD | 8,000,000.00 USD | 0.00 USD | 0.00 USD | 11,280.00 USD | 68,230.00 USD |
| `1D` | `0.1801` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD |
| `7D` | `0.1802` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 48,220.00 USD | 36,020.00 USD | 33,890.00 USD |
| `1D` | `0.1803` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD |
| `1D` | `0.1805` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD |
| `7D` | `0.1805` | 8,170,000.00 USD | 8,170,000.00 USD | 0.00 USD | 11,410.00 USD | 38,130.00 USD | 5,320.00 USD |
| `1D` | `0.1807` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD |
| `7D` | `0.1808` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 23,650.00 USD | 52,750.00 USD | 73,440.00 USD |
| `1D` | `0.1809` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD |
| `1D` | `0.1811` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 13,300.00 USD | 4,850.00 USD | 3,980.00 USD |
| `7D` | `0.1811` | 8,430,000.00 USD | 8,430,000.00 USD | 0.00 USD | 64,990.00 USD | 26,860.00 USD | 18,880.00 USD |
| `1D` | `0.1813` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 7,950.00 USD | 35,640.00 USD | 8,750.00 USD |
| `7D` | `0.1814` | 8,550,000.00 USD | 8,550,000.00 USD | 0.00 USD | 28,070.00 USD | 26,510.00 USD | 65,950.00 USD |
| `1D` | `0.1815` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 7,040.00 USD | 1,040.00 USD | 9,760.00 USD |
| `1D` | `0.1817` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 0.00 USD | 9,410.00 USD | 7,940.00 USD |
| `7D` | `0.1817` | 8,660,000.00 USD | 8,660,000.00 USD | 0.00 USD | 64,770.00 USD | 10,470.00 USD | 29,600.00 USD |
| `1D` | `0.1819` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 0.00 USD | 2,620.00 USD | 5,520.00 USD |
| `7D` | `0.1820` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 52,150.00 USD | 43,140.00 USD | 38,610.00 USD |
| `1D` | `0.1821` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 10,520.00 USD | 2,390.00 USD |
| `1D` | `0.1823` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 10,830.00 USD | 7,660.00 USD | 5,380.00 USD |
| `7D` | `0.1823` | 8,920,000.00 USD | 8,920,000.00 USD | 0.00 USD | 62,540.00 USD | 18,340.00 USD | 50,880.00 USD |
| `1D` | `0.1825` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 3,290.00 USD | 3,020.00 USD | 8,810.00 USD |
| `7D` | `0.1826` | 8,990,000.00 USD | 8,990,000.00 USD | 0.00 USD | 45,250.00 USD | 9,890.00 USD | 14,210.00 USD |
| `1D` | `0.1827` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 5,300.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1829` | 9,080,000.00 USD | 9,080,000.00 USD | 0.00 USD | 20,880.00 USD | 17,180.00 USD | 51,250.00 USD |
| `7D` | `0.1832` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 79,470.00 USD | 18,130.00 USD | 35,210.00 USD |
| `7D` | `0.1835` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 13,840.00 USD | 7,930.00 USD | 16,530.00 USD |
| `7D` | `0.1838` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 54,990.00 USD | 11,590.00 USD | 106,440.00 USD |
| `7D` | `0.1841` | 9,500,000.00 USD | 9,500,000.00 USD | 0.00 USD | 28,940.00 USD | 12,910.00 USD | 30,500.00 USD |
| `7D` | `0.1844` | 9,580,000.00 USD | 9,580,000.00 USD | 0.00 USD | 20,990.00 USD | 3,900.00 USD | 56,660.00 USD |
| `7D` | `0.1847` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 5,770.00 USD | 11,590.00 USD | 20,400.00 USD |
| `7D` | `0.1850` | 9,800,000.00 USD | 9,800,000.00 USD | 0.00 USD | 77,110.00 USD | 51,400.00 USD | 51,650.00 USD |
| `7D` | `0.1853` | 9,900,000.00 USD | 9,900,000.00 USD | 0.00 USD | 46,730.00 USD | 0.00 USD | 56,290.00 USD |
| `7D` | `0.1854` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 4,750.00 USD | 4,290.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `183.23M` | Total OI Tokens: `1,129,923,742.7 ARB`
  * 1h OI Change: `-0.07%` | 4h OI Change: `-0.27%` | 24h OI Change: `-14.15%`
  * Exchange Breakdown: Binance=`40.33M` | Bybit=`25.75M` | OKX=`13.88M` | Hyperliquid=`12.82M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `7.97K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0099%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0015%` | **USDT Bitget** | `-0.0021%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `51.70%` | `48.30%` | `1.07` | 846,120.00 USD |
| `15M` | `Binance` | `49.41%` | `50.59%` | `0.98` | 314,720.00 USD |
| `15M` | `OKX` | `53.55%` | `46.45%` | `1.15` | 59,140.00 USD |
| `15M` | `Bybit` | `70.04%` | `29.96%` | `2.34` | 78,420.00 USD |
| `15M` | `KuCoin` | `50.1%` | `49.9%` | `1.00` | 53,390.00 USD |
| `15M` | `Gate` | `6.6%` | `93.4%` | `0.07` | 26,110.00 USD |
| `15M` | `Bitget` | `66.88%` | `33.12%` | `2.02` | 15,710.00 USD |
| `15M` | `BingX` | `40.56%` | `59.44%` | `0.68` | 43,930.00 USD |
| `15M` | `MEXC` | `81.37%` | `18.63%` | `4.37` | 35,790.00 USD |
| `15M` | `Bitunix` | `43.73%` | `56.27%` | `0.78` | 6,690.00 USD |
| `15M` | `Hyperliquid` | `59.8%` | `40.2%` | `1.49` | 5,850.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `54.34%` | `45.66%` | `1.19` | 162,890.00 USD |
| `15M` | `Crypto.com` | `9.68%` | `90.32%` | `0.11` | 2.17 USD |
| `15M` | `WhiteBIT` | `65.67%` | `34.33%` | `1.91` | 21,820.00 USD |
| `15M` | `HTX` | `45.44%` | `54.56%` | `0.83` | 0.57 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `100%` | `0.00` | 8,810.00 USD |
| `15M` | `Aster` | `9.09%` | `90.91%` | `0.10` | 109.61 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0.95%` | `99.05%` | `0.01` | 12,740.00 USD |
| `15M` | `Whale Positions` | `49.41%` | `50.59%` | `0.98` | 314,720.00 USD |
| `15M` | `Global Accounts` | `51.70%` | `48.30%` | `1.07` | 846,120.00 USD |
| `1H` | `ARB` | `45.69%` | `54.31%` | `0.84` | 14,570,000.00 USD |
| `1H` | `Binance` | `48.58%` | `51.42%` | `0.94` | 5,400,000.00 USD |
| `1H` | `OKX` | `56.18%` | `43.82%` | `1.28` | 2,160,000.00 USD |
| `1H` | `Bybit` | `36.14%` | `63.86%` | `0.57` | 1,400,000.00 USD |
| `1H` | `KuCoin` | `51%` | `49%` | `1.04` | 598,800.00 USD |
| `1H` | `Gate` | `53.65%` | `46.35%` | `1.16` | 302,070.00 USD |
| `1H` | `Bitget` | `77.05%` | `22.95%` | `3.36` | 214,200.00 USD |
| `1H` | `BingX` | `50.94%` | `49.06%` | `1.04` | 147,140.00 USD |
| `1H` | `MEXC` | `59.33%` | `40.67%` | `1.46` | 134,570.00 USD |
| `1H` | `Bitunix` | `52.72%` | `47.28%` | `1.12` | 223,880.00 USD |
| `1H` | `Hyperliquid` | `65.28%` | `34.72%` | `1.88` | 80,510.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.88%` | `49.12%` | `1.04` | 2,340,000.00 USD |
| `1H` | `Crypto.com` | `49.98%` | `50.02%` | `1.00` | 22.39 USD |
| `1H` | `WhiteBIT` | `8.09%` | `91.91%` | `0.09` | 1,490,000.00 USD |
| `1H` | `HTX` | `68.78%` | `31.22%` | `2.20` | 4,540.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `42.58%` | `57.42%` | `0.74` | 53,920.00 USD |
| `1H` | `Aster` | `65.56%` | `34.44%` | `1.90` | 3,050.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `96.83%` | `3.17%` | `30.55` | 18,990.00 USD |
| `1H` | `Whale Positions` | `48.58%` | `51.42%` | `0.94` | 5,400,000.00 USD |
| `1H` | `Global Accounts` | `45.69%` | `54.31%` | `0.84` | 14,570,000.00 USD |
| `4H` | `ARB` | `46.24%` | `53.76%` | `0.86` | 30,510,000.00 USD |
| `4H` | `Binance` | `43.21%` | `56.79%` | `0.76` | 7,830,000.00 USD |
| `4H` | `OKX` | `44.31%` | `55.69%` | `0.80` | 2,480,000.00 USD |
| `4H` | `Bybit` | `47.79%` | `52.21%` | `0.92` | 2,130,000.00 USD |
| `4H` | `KuCoin` | `49.24%` | `50.76%` | `0.97` | 1,870,000.00 USD |
| `4H` | `Gate` | `39.97%` | `60.03%` | `0.67` | 1,100,000.00 USD |
| `4H` | `Bitget` | `53.37%` | `46.63%` | `1.14` | 698,120.00 USD |
| `4H` | `BingX` | `20.23%` | `79.77%` | `0.25` | 3,450,000.00 USD |
| `4H` | `MEXC` | `50.26%` | `49.74%` | `1.01` | 1,080,000.00 USD |
| `4H` | `Bitunix` | `48.51%` | `51.49%` | `0.94` | 566,070.00 USD |
| `4H` | `Hyperliquid` | `32.29%` | `67.71%` | `0.48` | 463,050.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.89%` | `50.11%` | `1.00` | 6,470,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `93.65%` | `6.35%` | `14.75` | 2,060,000.00 USD |
| `4H` | `HTX` | `39.16%` | `60.84%` | `0.64` | 18,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `11.45%` | `88.55%` | `0.13` | 276,490.00 USD |
| `4H` | `Aster` | `30.83%` | `69.17%` | `0.45` | 4,060.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `77.45%` | `22.55%` | `3.43` | 28,350.00 USD |
| `4H` | `Whale Positions` | `43.21%` | `56.79%` | `0.76` | 7,830,000.00 USD |
| `4H` | `Global Accounts` | `46.24%` | `53.76%` | `0.86` | 30,510,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1650` | `0.1648` | `0.1650` | `0.1651` | `0.1640` | 1,330,863.86 USD | 714,476.79 USD | 616,387.06 USD | 98,089.73 USD | `+7.37%` | `15B / 7S` |
| `0:00 UTC` | `0.1641` | `0.1647` | `0.1641` | `0.1657` | `0.1639` | 2,406,571.88 USD | 1,201,675.03 USD | 1,204,896.84 USD | -3,221.81 USD | `-0.13%` | `31B / 55S` |
| `5:00 UTC` | `0.1641` | `0.1639` | `0.1641` | `0.1647` | `0.1634` | 780,398.32 USD | 282,316.37 USD | 498,081.96 USD | -215,765.59 USD | `-27.65%` | `7B / 50S` |
| `0:00 UTC` | `0.1639` | `0.1637` | `0.1639` | `0.1646` | `0.1631` | 946,588.03 USD | 498,466.74 USD | 448,121.29 USD | 50,345.45 USD | `+5.32%` | `36B / 23S` |
| `5:00 UTC` | `0.1625` | `0.1631` | `0.1625` | `0.1640` | `0.1624` | 778,400.97 USD | 315,731.23 USD | 462,669.74 USD | -146,938.51 USD | `-18.88%` | `22B / 62S` |
| `0:00 UTC` | `0.1629` | `0.1625` | `0.1629` | `0.1632` | `0.1619` | 775,902.97 USD | 309,320.91 USD | 466,582.05 USD | -157,261.14 USD | `-20.27%` | `13B / 34S` |
| `5:00 UTC` | `0.1623` | `0.1620` | `0.1623` | `0.1624` | `0.1615` | 562,907.20 USD | 223,683.16 USD | 339,224.04 USD | -115,540.88 USD | `-20.53%` | `7B / 21S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1623` | `0.1611` | 779,913.00 USD | 372,491.97 USD | 407,421.03 USD | -34,929.06 USD | `-4.48%` | `22B / 23S` |
| `5:00 UTC` | `0.1620` | `0.1619` | `0.1620` | `0.1622` | `0.1615` | 338,104.92 USD | 163,363.17 USD | 174,741.74 USD | -11,378.57 USD | `-3.37%` | `6B / 19S` |
| `0:00 UTC` | `0.1621` | `0.1620` | `0.1621` | `0.1624` | `0.1615` | 366,960.37 USD | 186,288.11 USD | 180,672.27 USD | 5,615.84 USD | `+1.53%` | `24B / 18S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1671` | 1,100,000.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1677` | 2,200,000.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 20:47` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1667` | 522,000.00 USD | 0.00 USD |
| `10-28 20:42` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1670` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1668` | 0.00 USD | 0.00 USD |
| `10-28 20:36` | `Volume 10M ARB` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1677` | 0.00 USD | 0.00 USD |
| `10-28 20:08` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1637` | 359,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1637` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1642` | 1,100,000.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,300,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1640` | 0.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1634` | 0.00 USD | 0.00 USD |
| `10-28 19:42` | `Volume 10M ARB` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1631` | 2,900,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1649` | 0.00 USD | 0.00 USD |
| `10-28 19:03` | `Volume 10M ARB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1659` | 2,200,000.00 USD | 0.00 USD |
| `10-28 18:55` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1652` | 0.00 USD | 0.00 USD |
| `10-28 18:43` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1646` | 0.00 USD | 0.00 USD |
| `10-28 18:23` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1641` | 0.00 USD | 0.00 USD |
| `10-28 18:08` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1654` | 0.00 USD | 0.00 USD |
| `10-28 17:56` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 2,000,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1658` | 0.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1665` | 504,000.00 USD | 0.00 USD |
| `10-28 17:44` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1659` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1676` | 294,000.00 USD | 0.00 USD |
| `10-28 16:55` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1685` | 413,000.00 USD | 0.00 USD |
| `10-28 16:37` | `Volume 10M ARB` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1675` | 0.00 USD | 0.00 USD |
| `10-28 15:42` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 751,000.00 USD | 0.00 USD |
| `10-28 14:07` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1701` | 750,000.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1705` | 3,300,000.00 USD | 0.00 USD |
| `10-28 13:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1683` | 1,800,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1677` | 434,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1677` | 1,900,000.00 USD | 0.00 USD |
| `10-28 12:29` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1684` | 0.00 USD | 0.00 USD |
| `10-28 11:54` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 11:22` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1688` | 1,200,000.00 USD | 0.00 USD |
| `10-28 10:31` | `Range 0.0005` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1693` | 513,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.0005` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.1704` | 352,000.00 USD | 0.00 USD |
| `10-28 09:49` | `Volume 10M ARB` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.1681` | 1,300,000.00 USD | 0.00 USD |
| `10-28 09:09` | `Range 0.0005` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.1708` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.1688` | 0.00 USD | 0.00 USD |
| `10-28 08:45` | `Range 0.0005` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.1688` | 843,000.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.1694` | 0.00 USD | 0.00 USD |
| `10-28 08:26` | `Range 0.0005` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.1699` | 422,000.00 USD | 0.00 USD |
| `10-28 07:57` | `Range 0.0005` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.1691` | 1,100,000.00 USD | 0.00 USD |
| `10-28 07:35` | `Range 0.0005` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.1698` | 0.00 USD | 0.00 USD |
| `10-28 06:51` | `Range 0.0005` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.1691` | 1,600,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -18,850.00 USD | -104,550.00 USD | **`DISTRIBUTION`** |
| `15m` | -5,020.00 USD | -31,590.00 USD | **`DISTRIBUTION`** |
| `30m` | -61,430.00 USD | 11,020.00 USD | **`DISTRIBUTION`** |
| `1h` | -188,570.00 USD | -491,840.00 USD | **`DISTRIBUTION`** |
| `2h` | -633,420.00 USD | -1,200,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -476,730.00 USD | -847,580.00 USD | **`DISTRIBUTION`** |
| `6h` | -512,900.00 USD | -3,600,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -644,790.00 USD | -1,770,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -539,400.00 USD | -1,420,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,150,000.00 USD | -11,600,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,720,000.00 USD | -37,600,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,530,000.00 USD | -166,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-18.85K` | 15m=`-5.02K` | 1h=`-188.57K` | 24h=`-2.15M`
* Futures Capital Netflows: 5m=`-104.55K` | 15m=`-31.59K` | 1h=`-491.84K` | 24h=`-11.60M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1695` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.03` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.17`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1705` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.37` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.83`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1714`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
