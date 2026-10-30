# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:27:43 IST` (`2026-10-30 10:57:43 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1628` | `0.1629` | `0.1625` | `0.1627` | `963,843` | 156,812.04 USD | -5,581.71 USD | `-3.56%` | -8,007,075.00 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `0.1627` | `0.1629` | `0.1625` | `0.1626` | `1,525,736` | 248,225.55 USD | 55,327.70 USD | `+22.29%` | -7,951,747.30 USD | `+1.22` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1626` | `0.1629` | `0.1623` | `0.1629` | `1,050,640` | 170,619.56 USD | 74,291.60 USD | `+43.54%` | -7,877,455.70 USD | `+1.43` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1616` | `0.1629` | `0.1614` | `0.1622` | `2,781,541` | 451,221.10 USD | 108,735.60 USD | `+24.10%` | -7,836,663.41 USD | `+0.61` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1622` | `0.1631` | `0.1620` | `0.1627` | `3,416,453` | 555,739.49 USD | -25,758.68 USD | `-4.64%` | -7,862,422.08 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1627` | `0.1629` | `0.1623` | `0.1629` | `2,577,367` | 419,006.61 USD | 129,768.36 USD | `+30.97%` | -7,732,653.73 USD | `+0.84` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.1650` | `0.1657` | `0.1623` | `0.1629` | `29,928,265` | 4,911,959.21 USD | -315,580.46 USD | `-6.42%` | -7,559,567.01 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1629` | `0.1632` | `0.1611` | `0.1621` | `15,160,560` | 2,456,828.08 USD | -319,109.65 USD | `-12.99%` | -7,878,676.67 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1621` | `0.1631` | `0.1613` | `0.1629` | `12,243,838` | 1,987,296.97 USD | 145,873.88 USD | `+7.34%` | -7,732,802.79 USD | `+0.44` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1629` | `57,332,664` | 9,356,084.27 USD | -488,816.24 USD | `-5.22%` | -7,336,330.87 USD | `+0.62` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1629` | `57,332,664` | 9,356,084.27 USD | -488,816.24 USD | `-5.22%` | -7,336,330.87 USD | `+0.62` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`0.1700`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

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
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2105` | 227.00 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Long: 0.23K USD at 0.2105 USD [API] | `2026-09-19 03:39:36` |
| `ANNOUNCEMENT` | `INFO` | `0.1708` | 6,077.79 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale BUY: 6.08K USD at 0.1708 USD [API] | `2026-10-29 13:59:02` |
| `ANNOUNCEMENT` | `INFO` | `0.1665` | 9,204.24 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 9.20K USD at 0.1665 USD [API] | `2026-10-29 20:02:44` |
| `ANNOUNCEMENT` | `INFO` | `0.1666` | 7,123.24 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 7.12K USD at 0.1666 USD [API] | `2026-10-29 20:02:44` |


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
| `Live` | `Long Liquidation` | `0.0345` | 3,350.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0385` | 1,740.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 170.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 1,700.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 6,000.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 15,650.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 1,230.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 1,110.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 3,280.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 157.66 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 126.34 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 233,840.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 106,660.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 4,920.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 2,970.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 5,840.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 111.58 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,760.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 472.15 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0785` | 66,100.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 19,130.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 19,460.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 280.45 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 362.62 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 2,050.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 5,000.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,040.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 814.24 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 1,600.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 17,090.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 8,070.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 2,600.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 9,850.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 13,700.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,450.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 596.55 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,820.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 12,400.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 13,820.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 1,450.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 569.31 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 129,500.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 33,440.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 1,830.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 303.75 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,420.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,980.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 377.05 USD | 979,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 344.89 USD | 979,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 16,720.00 USD | 978,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 10,470.00 USD | 961,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,440.00 USD | 951,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 17,000.00 USD | 949,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 19,580.00 USD | 932,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 912,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,860.00 USD | 907,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 38,380.00 USD | 856,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 3,540.00 USD | 817,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1357` | 8,450,000.00 USD | 8,450,000.00 USD | 21,410.00 USD | 17,110.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 8,400,000.00 USD | 8,400,000.00 USD | 16,290.00 USD | 3,690.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1363` | 8,370,000.00 USD | 8,370,000.00 USD | 7,890.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 13,440.00 USD | 814,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1366` | 8,360,000.00 USD | 8,360,000.00 USD | 11,610.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1369` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 8,340,000.00 USD | 8,340,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1375` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 13,710.00 USD | 800,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1378` | 8,300,000.00 USD | 8,300,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 8,280,000.00 USD | 8,280,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,330.00 USD | 786,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1387` | 8,240,000.00 USD | 8,240,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1390` | 8,210,000.00 USD | 8,210,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1393` | 8,200,000.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 21,040.00 USD | 782,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1399` | 8,130,000.00 USD | 8,130,000.00 USD | 6,210.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1402` | 8,120,000.00 USD | 8,120,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,640.00 USD | 761,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 8,950.00 USD | 758,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1417` | 8,110,000.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 8,100,000.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1423` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 499,030.00 USD | 749,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1435` | 8,070,000.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 19,140.00 USD | 250,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1438` | 8,050,000.00 USD | 8,050,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1441` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 231,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1450` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1451` | 4,820,000.00 USD | 4,820,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 4,800,000.00 USD | 4,800,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,790,000.00 USD | 4,790,000.00 USD | 3,450.00 USD | 689.96 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 222,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1457` | 4,790,000.00 USD | 4,790,000.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1459` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 3,000.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 4,760,000.00 USD | 4,760,000.00 USD | 9,940.00 USD | 3,900.00 USD | 4,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 4,750,000.00 USD | 4,750,000.00 USD | 11,020.00 USD | 8,490.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1465` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 3,700.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 23,540.00 USD | 130,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 7,910,000.00 USD | 7,910,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 4,710,000.00 USD | 4,710,000.00 USD | 4,430.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 4,710,000.00 USD | 4,710,000.00 USD | 10,000.00 USD | 7,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 7,890,000.00 USD | 7,890,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,690,000.00 USD | 4,690,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 7,890,000.00 USD | 7,890,000.00 USD | 19,430.00 USD | 12,610.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,560,000.00 USD | 4,560,000.00 USD | 19,070.00 USD | 7,230.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 82,980.00 USD | 106,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 4,530,000.00 USD | 4,530,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1477` | 7,830,000.00 USD | 7,830,000.00 USD | 85,800.00 USD | 25,460.00 USD | 110,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,250,000.00 USD | 4,250,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 7,610,000.00 USD | 7,610,000.00 USD | 50,400.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 4,140,000.00 USD | 4,140,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 4,090,000.00 USD | 4,090,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 7,510,000.00 USD | 7,510,000.00 USD | 42,230.00 USD | 16,640.00 USD | 202,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,920,000.00 USD | 3,920,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 23,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 7,250,000.00 USD | 7,250,000.00 USD | 66,760.00 USD | 10,470.00 USD | 35,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,810,000.00 USD | 3,810,000.00 USD | 8,840.00 USD | 3,580.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,790,000.00 USD | 3,790,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 7,130,000.00 USD | 7,130,000.00 USD | 21,100.00 USD | 3,710.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,760,000.00 USD | 3,760,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 7,040,000.00 USD | 7,040,000.00 USD | 40,320.00 USD | 22,920.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,700,000.00 USD | 3,700,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,670,000.00 USD | 3,670,000.00 USD | 56,660.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 6,940,000.00 USD | 6,940,000.00 USD | 34,650.00 USD | 18,690.00 USD | 191,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 21,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,580,000.00 USD | 3,580,000.00 USD | 8,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1498` | 6,700,000.00 USD | 6,700,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,570,000.00 USD | 3,570,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,560,000.00 USD | 3,560,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 6,640,000.00 USD | 6,640,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,530,000.00 USD | 3,530,000.00 USD | 48,710.00 USD | 4,400.00 USD | 153,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 6,590,000.00 USD | 6,590,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,320,000.00 USD | 3,320,000.00 USD | 35,380.00 USD | 1,940.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1507` | 6,520,000.00 USD | 6,520,000.00 USD | 152,330.00 USD | 12,910.00 USD | 182,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 6,170,000.00 USD | 6,170,000.00 USD | 135,010.00 USD | 12,930.00 USD | 112,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,920,000.00 USD | 2,920,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 17,610.00 USD | 104,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,650,000.00 USD | 2,650,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 5,790,000.00 USD | 5,790,000.00 USD | 48,970.00 USD | 0.00 USD | 338,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,520,000.00 USD | 2,520,000.00 USD | 12,390.00 USD | 6,150.00 USD | 24,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,480,000.00 USD | 2,480,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 5,400,000.00 USD | 5,400,000.00 USD | 47,340.00 USD | 24,320.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,400,000.00 USD | 2,400,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 9,640.00 USD | 130,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,350,000.00 USD | 2,350,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,340,000.00 USD | 2,340,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 5,120,000.00 USD | 5,120,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,300,000.00 USD | 2,300,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 31,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,290,000.00 USD | 2,290,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,250,000.00 USD | 2,250,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 5,060,000.00 USD | 5,060,000.00 USD | 35,470.00 USD | 17,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,220,000.00 USD | 2,220,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1535` | 8,620.00 USD | 20,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,200,000.00 USD | 2,200,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 11,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 6,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,170,000.00 USD | 2,170,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,130,000.00 USD | 2,130,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1547` | 2,100,000.00 USD | 2,100,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 2,080,000.00 USD | 2,080,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 4,980,000.00 USD | 4,980,000.00 USD | 0.00 USD | 19,500.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,030,000.00 USD | 2,030,000.00 USD | 14,290.00 USD | 12,210.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 2,000,000.00 USD | 2,000,000.00 USD | 12,260.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 1,980,000.00 USD | 1,980,000.00 USD | 40,830.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 4,860,000.00 USD | 4,860,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 2,170.00 USD | 11,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,920,000.00 USD | 1,920,000.00 USD | 2,800.00 USD | 12,870.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 4,850,000.00 USD | 4,850,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 1,900,000.00 USD | 1,900,000.00 USD | 17,010.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,880,000.00 USD | 1,880,000.00 USD | 12,360.00 USD | 3,020.00 USD | 4,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 4,650,000.00 USD | 4,650,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,860,000.00 USD | 1,860,000.00 USD | 11,460.00 USD | 25,680.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 4,640,000.00 USD | 4,640,000.00 USD | 0.00 USD | 43,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 1,820,000.00 USD | 1,820,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,660.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,730,000.00 USD | 1,730,000.00 USD | 21,860.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 4,600,000.00 USD | 4,600,000.00 USD | 123,230.00 USD | 15,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,700,000.00 USD | 1,700,000.00 USD | 24,170.00 USD | 0.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 4,460,000.00 USD | 4,460,000.00 USD | 134,890.00 USD | 5,100.00 USD | 210,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,570,000.00 USD | 1,570,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,450,000.00 USD | 1,450,000.00 USD | 20,000.00 USD | 3,460.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 4,110,000.00 USD | 4,110,000.00 USD | 191,190.00 USD | 64,570.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1576` | 3,820,000.00 USD | 3,820,000.00 USD | 26,600.00 USD | 108,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,380,000.00 USD | 1,380,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 1,310,000.00 USD | 1,310,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 3,690,000.00 USD | 3,690,000.00 USD | 197,810.00 USD | 80,390.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,290,000.00 USD | 1,290,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 3,400,000.00 USD | 3,400,000.00 USD | 56,130.00 USD | 17,610.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,260,000.00 USD | 1,260,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 1,110,000.00 USD | 1,110,000.00 USD | 21,920.00 USD | 20,720.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 3,290,000.00 USD | 3,290,000.00 USD | 87,110.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,060,000.00 USD | 1,060,000.00 USD | 50,950.00 USD | 19,830.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 3,180,000.00 USD | 3,180,000.00 USD | 74,200.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 947,580.00 USD | 947,580.00 USD | 20,380.00 USD | 6,150.00 USD | 44,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 876,190.00 USD | 876,190.00 USD | 20,460.00 USD | 21,570.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 12,590.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 791,620.00 USD | 791,620.00 USD | 14,950.00 USD | 38,970.00 USD | 39,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 29,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 698,440.00 USD | 698,440.00 USD | 10,260.00 USD | 14,420.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 666,410.00 USD | 666,410.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 96,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 648,600.00 USD | 648,600.00 USD | 0.00 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 38,830.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 641,020.00 USD | 641,020.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 617,370.00 USD | 617,370.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 58,120.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 574,870.00 USD | 574,870.00 USD | 16,510.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1606` | 2,570,000.00 USD | 2,570,000.00 USD | 237,510.00 USD | 0.00 USD | 376,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 522,230.00 USD | 522,230.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 499,730.00 USD | 499,730.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 1,960,000.00 USD | 1,960,000.00 USD | 117,480.00 USD | 11,640.00 USD | 296,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 351,700.00 USD | 351,700.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 1,530,000.00 USD | 1,530,000.00 USD | 304,890.00 USD | 10,980.00 USD | 254,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 176,150.00 USD | 176,150.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 112,780.00 USD | 112,780.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 959,480.00 USD | 959,480.00 USD | 293,210.00 USD | 35,210.00 USD | 243,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1617` | 96,350.00 USD | 96,350.00 USD | 0.00 USD | 3,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 387,750.00 USD | 387,750.00 USD | 0.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 92,790.00 USD | 92,790.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 43,910.00 USD | 43,910.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 340,160.00 USD | 340,160.00 USD | 78,750.00 USD | 57,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 204,110.00 USD | 204,110.00 USD | 0.00 USD | 170,670.00 USD | 33,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 38,240.00 USD | 38,240.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1627` | 180,100.00 USD | 180,100.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1630` | 251,040.00 USD | 251,040.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1635` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1635` | 2,350.00 USD | 2,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1637` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1649` | 40,160.00 USD | 40,160.00 USD | 11,310.00 USD | 3,450.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1651` | 65,020.00 USD | 65,020.00 USD | 24,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 88,260.00 USD | 88,260.00 USD | 17,080.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 100,270.00 USD | 100,270.00 USD | 5,090.00 USD | 2,360.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 115,230.00 USD | 115,230.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 130,390.00 USD | 130,390.00 USD | 0.00 USD | 6,040.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 348,650.00 USD | 348,650.00 USD | 68,280.00 USD | 29,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 147,460.00 USD | 147,460.00 USD | 0.00 USD | 13,210.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 228,540.00 USD | 228,540.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1663` | 498,720.00 USD | 498,720.00 USD | 121,520.00 USD | 0.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 265,880.00 USD | 265,880.00 USD | 0.00 USD | 3,710.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1666` | 589,790.00 USD | 589,790.00 USD | 49,590.00 USD | 12,670.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 307,790.00 USD | 307,790.00 USD | 21,340.00 USD | 5,340.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 335,560.00 USD | 335,560.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1669` | 834,070.00 USD | 834,070.00 USD | 76,120.00 USD | 81,000.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 397,590.00 USD | 397,590.00 USD | 25,900.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 1,040,000.00 USD | 1,040,000.00 USD | 96,910.00 USD | 38,070.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 481,840.00 USD | 481,840.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 515,130.00 USD | 515,130.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1675` | 1,230,000.00 USD | 1,230,000.00 USD | 64,490.00 USD | 130,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 6,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1677` | 705,280.00 USD | 705,280.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1678` | 1,410,000.00 USD | 1,410,000.00 USD | 71,860.00 USD | 90,910.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 762,950.00 USD | 762,950.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 916,010.00 USD | 916,010.00 USD | 94,350.00 USD | 36,530.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1681` | 1,680,000.00 USD | 1,680,000.00 USD | 69,520.00 USD | 71,610.00 USD | 128,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 1,040,000.00 USD | 1,040,000.00 USD | 61,280.00 USD | 12,810.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 1,800,000.00 USD | 1,800,000.00 USD | 60,960.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 1,180,000.00 USD | 1,180,000.00 USD | 41,190.00 USD | 48,480.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,270,000.00 USD | 1,270,000.00 USD | 6,960.00 USD | 9,500.00 USD | 74,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1687` | 1,900,000.00 USD | 1,900,000.00 USD | 78,750.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 1,380,000.00 USD | 1,380,000.00 USD | 54,040.00 USD | 26,970.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1690` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 63,850.00 USD | 74,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,620,000.00 USD | 1,620,000.00 USD | 69,010.00 USD | 72,070.00 USD | 105,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,780,000.00 USD | 1,780,000.00 USD | 57,220.00 USD | 35,730.00 USD | 61,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1693` | 2,160,000.00 USD | 2,160,000.00 USD | 33,660.00 USD | 46,740.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,830,000.00 USD | 1,830,000.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1695` | 11,320.00 USD | 18,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1696` | 2,290,000.00 USD | 2,290,000.00 USD | 17,360.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 1,900,000.00 USD | 1,900,000.00 USD | 23,730.00 USD | 37,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 1,990,000.00 USD | 1,990,000.00 USD | 24,020.00 USD | 22,050.00 USD | 48,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 2,030,000.00 USD | 2,030,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 2,530,000.00 USD | 2,530,000.00 USD | 68,360.00 USD | 55,360.00 USD | 72,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,110,000.00 USD | 2,110,000.00 USD | 31,680.00 USD | 6,390.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1705` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 18,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,260,000.00 USD | 2,260,000.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 31,310.00 USD | 87,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 2,330,000.00 USD | 2,330,000.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,370,000.00 USD | 2,370,000.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1711` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 5,490.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,400,000.00 USD | 2,400,000.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 59,620.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 2,490,000.00 USD | 2,490,000.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 3,220.00 USD | 21,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,530,000.00 USD | 2,530,000.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1717` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,590,000.00 USD | 2,590,000.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 3,040,000.00 USD | 3,040,000.00 USD | 39,370.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 2,710,000.00 USD | 2,710,000.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,810,000.00 USD | 2,810,000.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 3,390,000.00 USD | 3,390,000.00 USD | 118,060.00 USD | 12,590.00 USD | 225,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 2,870,000.00 USD | 2,870,000.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 2,880,000.00 USD | 2,880,000.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,900,000.00 USD | 2,900,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 3,510,000.00 USD | 3,510,000.00 USD | 120,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 3,850,000.00 USD | 3,850,000.00 USD | 324,890.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 2,920,000.00 USD | 2,920,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,950,000.00 USD | 2,950,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1735` | 1,190.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,970,000.00 USD | 2,970,000.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 2,270.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 3,010,000.00 USD | 3,010,000.00 USD | 3,500.00 USD | 2,460.00 USD | 6,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 3,030,000.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 3,130,000.00 USD | 3,130,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 4,150,000.00 USD | 4,150,000.00 USD | 69,520.00 USD | 0.00 USD | 120,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 3,160,000.00 USD | 3,160,000.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,200,000.00 USD | 3,200,000.00 USD | 17,770.00 USD | 0.00 USD | 21,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 197,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,240,000.00 USD | 3,240,000.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1756` | 4,520,000.00 USD | 4,520,000.00 USD | 112,930.00 USD | 0.00 USD | 53,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 3,310,000.00 USD | 3,310,000.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,400,000.00 USD | 3,400,000.00 USD | 58,360.00 USD | 11,020.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 4,760,000.00 USD | 4,760,000.00 USD | 200,480.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,540,000.00 USD | 3,540,000.00 USD | 33,150.00 USD | 66,160.00 USD | 40,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 5,000,000.00 USD | 5,000,000.00 USD | 117,200.00 USD | 94,740.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 3,600,000.00 USD | 3,600,000.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,670,000.00 USD | 3,670,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 5,300,000.00 USD | 5,300,000.00 USD | 154,540.00 USD | 97,630.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 3,760,000.00 USD | 3,760,000.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 5,580,000.00 USD | 5,580,000.00 USD | 161,560.00 USD | 92,440.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 3,850,000.00 USD | 3,850,000.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,880,000.00 USD | 3,880,000.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 5,750,000.00 USD | 5,750,000.00 USD | 69,030.00 USD | 83,790.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,930,000.00 USD | 3,930,000.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 5,990,000.00 USD | 5,990,000.00 USD | 148,780.00 USD | 85,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 3,960,000.00 USD | 3,960,000.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,070,000.00 USD | 4,070,000.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 6,150,000.00 USD | 6,150,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 4,100,000.00 USD | 4,100,000.00 USD | 7,310.00 USD | 9,400.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 6,290,000.00 USD | 6,290,000.00 USD | 52,730.00 USD | 38,910.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 4,110,000.00 USD | 4,110,000.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,170,000.00 USD | 4,170,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 6,490,000.00 USD | 6,490,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,210,000.00 USD | 4,210,000.00 USD | 12,390.00 USD | 27,370.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 23,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1786` | 6,690,000.00 USD | 6,690,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1787` | 4,250,000.00 USD | 4,250,000.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,260,000.00 USD | 4,260,000.00 USD | 9,350.00 USD | 1,210.00 USD | 1,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 6,740,000.00 USD | 6,740,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,270,000.00 USD | 4,270,000.00 USD | 0.00 USD | 2,640.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 6,920,000.00 USD | 6,920,000.00 USD | 134,000.00 USD | 43,520.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 4,280,000.00 USD | 4,280,000.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,350,000.00 USD | 4,350,000.00 USD | 16,300.00 USD | 33,080.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 7,000,000.00 USD | 7,000,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 1,850.00 USD | 25,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 4,370,000.00 USD | 4,370,000.00 USD | 10,870.00 USD | 4,390.00 USD | 8,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 4,390,000.00 USD | 4,390,000.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,430,000.00 USD | 4,430,000.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 7,160,000.00 USD | 7,160,000.00 USD | 19,430.00 USD | 43,480.00 USD | 55,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 4,460,000.00 USD | 4,460,000.00 USD | 2,390.00 USD | 10,580.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 7,240,000.00 USD | 7,240,000.00 USD | 28,790.00 USD | 27,450.00 USD | 25,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 4,470,000.00 USD | 4,470,000.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,500,000.00 USD | 4,500,000.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 7,380,000.00 USD | 7,380,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 7,500,000.00 USD | 7,500,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 7,620,000.00 USD | 7,620,000.00 USD | 32,530.00 USD | 15,780.00 USD | 67,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 135.29 USD | 25,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1816` | 7,720,000.00 USD | 7,720,000.00 USD | 46,430.00 USD | 21,200.00 USD | 35,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 7,840,000.00 USD | 7,840,000.00 USD | 52,150.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 7,960,000.00 USD | 7,960,000.00 USD | 46,760.00 USD | 29,530.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 8,030,000.00 USD | 8,030,000.00 USD | 38,800.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 8,090,000.00 USD | 8,090,000.00 USD | 29,430.00 USD | 13,380.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 8,190,000.00 USD | 8,190,000.00 USD | 63,190.00 USD | 9,610.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 8,220,000.00 USD | 8,220,000.00 USD | 18,400.00 USD | 0.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 8,330,000.00 USD | 8,330,000.00 USD | 11,490.00 USD | 13,450.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 8,480,000.00 USD | 8,480,000.00 USD | 70,360.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 8,530,000.00 USD | 8,530,000.00 USD | 17,340.00 USD | 3,040.00 USD | 28,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 2,390.00 USD | 27,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1846` | 8,600,000.00 USD | 8,600,000.00 USD | 8,330.00 USD | 10,850.00 USD | 42,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 8,670,000.00 USD | 8,670,000.00 USD | 35,280.00 USD | 35,270.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 893.89 USD | 29,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 4,190.00 USD | 33,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 33,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 45,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 176.60 USD | 45,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 13,570.00 USD | 58,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 474.40 USD | 59,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 59,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2105` | 190.73 USD | 59,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 75,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 45,680.00 USD | 121,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 121,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 88,150.00 USD | 209,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 209,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 209,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 216,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 232,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 232,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 21,940.00 USD | 254,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 255,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2435` | 48,700.00 USD | 304,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 304,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 304,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 5,450.00 USD | 310,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 26,570.00 USD | 336,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 54,960.00 USD | 391,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 392,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 392,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2695` | 186,670.00 USD | 578,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 592,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 592,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 604,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2755` | 12,100.00 USD | 616,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2765` | 2,100.00 USD | 618,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 618,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 618,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 619,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 1,900.00 USD | 621,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3065` | 278,380.00 USD | 899,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,290.00 USD | 906,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 906,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3095` | 492.26 USD | 907,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 12,170.00 USD | 919,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 640.88 USD | 919,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 1,530.00 USD | 921,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 227.49 USD | 921,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

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
| `7D` | `0.1357` | 8,450,000.00 USD | 0.00 USD | 8,450,000.00 USD | 21,410.00 USD | 17,110.00 USD | 11,830.00 USD |
| `7D` | `0.1360` | 8,400,000.00 USD | 0.00 USD | 8,400,000.00 USD | 16,290.00 USD | 3,690.00 USD | 6,320.00 USD |
| `7D` | `0.1363` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 7,890.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1366` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 11,610.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1369` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1372` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1375` | 8,330,000.00 USD | 0.00 USD | 8,330,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1378` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1384` | 8,280,000.00 USD | 0.00 USD | 8,280,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `7D` | `0.1387` | 8,240,000.00 USD | 0.00 USD | 8,240,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `0.1390` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD |
| `7D` | `0.1393` | 8,200,000.00 USD | 0.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 50,050.00 USD |
| `7D` | `0.1396` | 8,150,000.00 USD | 0.00 USD | 8,150,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD |
| `7D` | `0.1399` | 8,130,000.00 USD | 0.00 USD | 8,130,000.00 USD | 6,210.00 USD | 4,200.00 USD | 0.00 USD |
| `7D` | `0.1402` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD |
| `7D` | `0.1417` | 8,110,000.00 USD | 0.00 USD | 8,110,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 8,100,000.00 USD | 0.00 USD | 8,100,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `7D` | `0.1423` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1435` | 8,070,000.00 USD | 0.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1438` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1441` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1450` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 13,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1450` | 8,020,000.00 USD | 0.00 USD | 8,020,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `1D` | `0.1452` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 15,450.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1454` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 3,450.00 USD | 689.96 USD | 0.00 USD |
| `1D` | `0.1456` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 1,740.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1458` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 2,050.00 USD | 0.00 USD | 3,350.00 USD |
| `1D` | `0.1460` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 0.00 USD | 4,870.00 USD | 913.50 USD |
| `1D` | `0.1462` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 2,990.00 USD | 5,690.00 USD | 1,760.00 USD |
| `1D` | `0.1464` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 13,790.00 USD | 2,490.00 USD | 16,560.00 USD |
| `7D` | `0.1465` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 0.00 USD | 3,700.00 USD | 93,240.00 USD |
| `1D` | `0.1466` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 4,180.00 USD | 7,200.00 USD | 0.00 USD |
| `1D` | `0.1468` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 4,430.00 USD | 1,110.00 USD | 2,660.00 USD |
| `7D` | `0.1468` | 7,910,000.00 USD | 0.00 USD | 7,910,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD |
| `1D` | `0.1470` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 4,270.00 USD | 2,810.00 USD | 0.00 USD |
| `7D` | `0.1471` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1472` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 5,730.00 USD | 15,660.00 USD | 64,650.00 USD |
| `1D` | `0.1474` | 4,620,000.00 USD | 0.00 USD | 4,620,000.00 USD | 43,430.00 USD | 16,470.00 USD | 18,430.00 USD |
| `7D` | `0.1474` | 7,890,000.00 USD | 0.00 USD | 7,890,000.00 USD | 19,430.00 USD | 12,610.00 USD | 24,530.00 USD |
| `1D` | `0.1476` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 49,710.00 USD | 22,570.00 USD | 156,050.00 USD |
| `7D` | `0.1477` | 7,830,000.00 USD | 0.00 USD | 7,830,000.00 USD | 85,800.00 USD | 25,460.00 USD | 110,550.00 USD |
| `1D` | `0.1478` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 82,270.00 USD | 6,140.00 USD | 27,730.00 USD |
| `1D` | `0.1480` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 71,150.00 USD | 10,470.00 USD | 6,220.00 USD |
| `7D` | `0.1480` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 50,400.00 USD | 29,300.00 USD | 20,830.00 USD |
| `1D` | `0.1482` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 18,610.00 USD | 6,260.00 USD | 124,300.00 USD |
| `7D` | `0.1483` | 7,510,000.00 USD | 0.00 USD | 7,510,000.00 USD | 42,230.00 USD | 16,640.00 USD | 202,650.00 USD |
| `1D` | `0.1484` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 63,600.00 USD | 4,640.00 USD | 69,860.00 USD |
| `1D` | `0.1486` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 7,110.00 USD | 1,840.00 USD | 1,400.00 USD |
| `7D` | `0.1486` | 7,250,000.00 USD | 0.00 USD | 7,250,000.00 USD | 66,760.00 USD | 10,470.00 USD | 35,500.00 USD |
| `1D` | `0.1488` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 16,750.00 USD | 1,740.00 USD | 12,170.00 USD |
| `7D` | `0.1489` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 21,100.00 USD | 3,710.00 USD | 67,450.00 USD |
| `1D` | `0.1490` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 40,720.00 USD | 15,530.00 USD | 9,590.00 USD |
| `1D` | `0.1492` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 6,410.00 USD | 6,010.00 USD | 9,240.00 USD |
| `7D` | `0.1492` | 7,040,000.00 USD | 0.00 USD | 7,040,000.00 USD | 40,320.00 USD | 22,920.00 USD | 35,230.00 USD |
| `1D` | `0.1494` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 43,870.00 USD | 3,020.00 USD | 12,770.00 USD |
| `7D` | `0.1495` | 6,940,000.00 USD | 0.00 USD | 6,940,000.00 USD | 34,650.00 USD | 18,690.00 USD | 191,550.00 USD |
| `1D` | `0.1496` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 26,530.00 USD | 0.00 USD | 20,690.00 USD |
| `1D` | `0.1498` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 8,630.00 USD | 4,640.00 USD | 0.00 USD |
| `7D` | `0.1498` | 6,700,000.00 USD | 0.00 USD | 6,700,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD |
| `1D` | `0.1500` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 5,920.00 USD | 4,820.00 USD | 2,340.00 USD |
| `7D` | `0.1501` | 6,640,000.00 USD | 0.00 USD | 6,640,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD |
| `1D` | `0.1502` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 11,460.00 USD | 13,970.00 USD | 131,800.00 USD |
| `1D` | `0.1504` | 3,410,000.00 USD | 0.00 USD | 3,410,000.00 USD | 84,100.00 USD | 3,920.00 USD | 29,250.00 USD |
| `7D` | `0.1504` | 6,590,000.00 USD | 0.00 USD | 6,590,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD |
| `1D` | `0.1506` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 0.00 USD | 1,150.00 USD | 198,820.00 USD |
| `7D` | `0.1507` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 152,330.00 USD | 12,910.00 USD | 182,120.00 USD |
| `1D` | `0.1508` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 105,410.00 USD |
| `1D` | `0.1510` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD |
| `7D` | `0.1510` | 6,170,000.00 USD | 0.00 USD | 6,170,000.00 USD | 135,010.00 USD | 12,930.00 USD | 112,100.00 USD |
| `1D` | `0.1512` | 2,930,000.00 USD | 0.00 USD | 2,930,000.00 USD | 5,040.00 USD | 3,900.00 USD | 1,300.00 USD |
| `7D` | `0.1513` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 0.00 USD | 17,610.00 USD | 104,500.00 USD |
| `1D` | `0.1514` | 2,920,000.00 USD | 0.00 USD | 2,920,000.00 USD | 11,720.00 USD | 0.00 USD | 250,360.00 USD |
| `1D` | `0.1516` | 2,660,000.00 USD | 0.00 USD | 2,660,000.00 USD | 7,210.00 USD | 0.00 USD | 139,820.00 USD |
| `7D` | `0.1516` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 48,970.00 USD | 0.00 USD | 338,620.00 USD |
| `1D` | `0.1518` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 31,590.00 USD | 8,960.00 USD | 27,670.00 USD |
| `7D` | `0.1519` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 47,340.00 USD | 24,320.00 USD | 70,660.00 USD |
| `1D` | `0.1520` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 49,700.00 USD | 4,400.00 USD | 12,370.00 USD |
| `1D` | `0.1522` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 0.00 USD | 4,770.00 USD | 8,880.00 USD |
| `7D` | `0.1522` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 0.00 USD | 9,640.00 USD | 130,510.00 USD |
| `1D` | `0.1524` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 39,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1525` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD |
| `1D` | `0.1526` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 21,650.00 USD | 0.00 USD | 3,130.00 USD |
| `1D` | `0.1528` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 17,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1528` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 31,930.00 USD | 0.00 USD |
| `1D` | `0.1530` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 12,670.00 USD | 15,770.00 USD | 4,670.00 USD |
| `7D` | `0.1531` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 0.00 USD | 8,400.00 USD | 0.00 USD |
| `1D` | `0.1532` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 0.00 USD | 4,910.00 USD | 0.00 USD |
| `1D` | `0.1534` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 10,930.00 USD | 0.00 USD | 11,690.00 USD |
| `7D` | `0.1534` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 35,470.00 USD | 17,430.00 USD | 0.00 USD |
| `1D` | `0.1536` | 2,220,000.00 USD | 0.00 USD | 2,220,000.00 USD | 4,040.00 USD | 18,160.00 USD | 10,570.00 USD |
| `7D` | `0.1537` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 0.00 USD | 11,700.00 USD | 0.00 USD |
| `1D` | `0.1538` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1540` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 27,770.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1540` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 6,530.00 USD | 0.00 USD |
| `1D` | `0.1542` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 4,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1543` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1544` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 10,090.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1546` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 14,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1548` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 16,200.00 USD | 12,300.00 USD | 9,340.00 USD |
| `7D` | `0.1549` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 0.00 USD | 19,500.00 USD | 89,090.00 USD |
| `1D` | `0.1550` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 8,630.00 USD | 14,430.00 USD | 20,380.00 USD |
| `1D` | `0.1552` | 2,020,000.00 USD | 0.00 USD | 2,020,000.00 USD | 5,650.00 USD | 3,400.00 USD | 5,970.00 USD |
| `7D` | `0.1552` | 4,880,000.00 USD | 0.00 USD | 4,880,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `1D` | `0.1554` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 40,240.00 USD | 4,020.00 USD | 5,190.00 USD |
| `7D` | `0.1555` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1556` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 15,660.00 USD | 1,660.00 USD | 11,470.00 USD |
| `1D` | `0.1558` | 1,930,000.00 USD | 0.00 USD | 1,930,000.00 USD | 9,540.00 USD | 12,870.00 USD | 6,690.00 USD |
| `7D` | `0.1558` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1560` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 7,480.00 USD | 2,970.00 USD | 784.65 USD |
| `7D` | `0.1561` | 4,650,000.00 USD | 0.00 USD | 4,650,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.1562` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 12,360.00 USD | 6,230.00 USD | 8,810.00 USD |
| `1D` | `0.1564` | 1,860,000.00 USD | 0.00 USD | 1,860,000.00 USD | 17,350.00 USD | 41,690.00 USD | 2,050.00 USD |
| `7D` | `0.1564` | 4,640,000.00 USD | 0.00 USD | 4,640,000.00 USD | 0.00 USD | 43,350.00 USD | 0.00 USD |
| `1D` | `0.1566` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 70,570.00 USD | 1,850.00 USD | 16,410.00 USD |
| `7D` | `0.1567` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 123,230.00 USD | 15,360.00 USD | 0.00 USD |
| `1D` | `0.1568` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 10,670.00 USD | 0.00 USD | 9,250.00 USD |
| `1D` | `0.1570` | 1,690,000.00 USD | 0.00 USD | 1,690,000.00 USD | 27,380.00 USD | 5,080.00 USD | 105,410.00 USD |
| `7D` | `0.1570` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 134,890.00 USD | 5,100.00 USD | 210,460.00 USD |
| `1D` | `0.1572` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 48,950.00 USD | 5,380.00 USD | 82,520.00 USD |
| `7D` | `0.1573` | 4,110,000.00 USD | 0.00 USD | 4,110,000.00 USD | 191,190.00 USD | 64,570.00 USD | 34,380.00 USD |
| `1D` | `0.1574` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 11,750.00 USD | 4,810.00 USD | 0.00 USD |
| `1D` | `0.1576` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,460.00 USD | 0.00 USD | 11,190.00 USD |
| `7D` | `0.1576` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 26,600.00 USD | 108,010.00 USD | 0.00 USD |
| `1D` | `0.1578` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 30,670.00 USD | 29,200.00 USD | 22,140.00 USD |
| `7D` | `0.1579` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 197,810.00 USD | 80,390.00 USD | 8,370.00 USD |
| `1D` | `0.1580` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 9,050.00 USD | 6,060.00 USD | 7,610.00 USD |
| `1D` | `0.1582` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 49,700.00 USD | 14,280.00 USD | 16,650.00 USD |
| `7D` | `0.1582` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 56,130.00 USD | 17,610.00 USD | 38,720.00 USD |
| `1D` | `0.1584` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 71,860.00 USD | 23,060.00 USD | 14,690.00 USD |
| `7D` | `0.1585` | 3,290,000.00 USD | 0.00 USD | 3,290,000.00 USD | 87,110.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1586` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 32,600.00 USD | 24,610.00 USD | 42,840.00 USD |
| `1D` | `0.1588` | 988,730.00 USD | 0.00 USD | 988,730.00 USD | 32,410.00 USD | 12,000.00 USD | 37,340.00 USD |
| `7D` | `0.1588` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 74,200.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1590` | 906,980.00 USD | 0.00 USD | 906,980.00 USD | 24,280.00 USD | 10,870.00 USD | 28,290.00 USD |
| `7D` | `0.1591` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 12,590.00 USD | 16,720.00 USD |
| `1D` | `0.1592` | 843,540.00 USD | 0.00 USD | 843,540.00 USD | 20,040.00 USD | 24,520.00 USD | 44,240.00 USD |
| `1D` | `0.1594` | 754,740.00 USD | 0.00 USD | 754,740.00 USD | 10,260.00 USD | 32,760.00 USD | 38,510.00 USD |
| `7D` | `0.1594` | 2,980,000.00 USD | 0.00 USD | 2,980,000.00 USD | 0.00 USD | 29,330.00 USD | 0.00 USD |
| `1D` | `0.1596` | 673,210.00 USD | 0.00 USD | 673,210.00 USD | 11,790.00 USD | 6,800.00 USD | 0.00 USD |
| `7D` | `0.1597` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 96,110.00 USD | 0.00 USD |
| `1D` | `0.1598` | 654,630.00 USD | 0.00 USD | 654,630.00 USD | 0.00 USD | 7,580.00 USD | 6,030.00 USD |
| `1D` | `0.1600` | 641,020.00 USD | 0.00 USD | 641,020.00 USD | 21,340.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1600` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 0.00 USD | 38,830.00 USD | 75,810.00 USD |
| `1D` | `0.1602` | 617,370.00 USD | 0.00 USD | 617,370.00 USD | 28,500.00 USD | 10,160.00 USD | 0.00 USD |
| `7D` | `0.1603` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 0.00 USD | 58,120.00 USD | 116,120.00 USD |
| `1D` | `0.1604` | 578,710.00 USD | 0.00 USD | 578,710.00 USD | 0.00 USD | 3,850.00 USD | 12,790.00 USD |
| `1D` | `0.1606` | 562,080.00 USD | 0.00 USD | 562,080.00 USD | 21,600.00 USD | 0.00 USD | 23,340.00 USD |
| `7D` | `0.1606` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 237,510.00 USD | 0.00 USD | 376,580.00 USD |
| `1D` | `0.1608` | 517,140.00 USD | 0.00 USD | 517,140.00 USD | 34,860.00 USD | 17,410.00 USD | 90,310.00 USD |
| `7D` | `0.1609` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 117,480.00 USD | 11,640.00 USD | 296,510.00 USD |
| `1D` | `0.1610` | 374,550.00 USD | 0.00 USD | 374,550.00 USD | 71,710.00 USD | 58,400.00 USD | 28,810.00 USD |
| `1D` | `0.1612` | 215,630.00 USD | 0.00 USD | 215,630.00 USD | 23,810.00 USD | 23,830.00 USD | 25,000.00 USD |
| `7D` | `0.1612` | 1,530,000.00 USD | 0.00 USD | 1,530,000.00 USD | 304,890.00 USD | 10,980.00 USD | 254,850.00 USD |
| `1D` | `0.1614` | 142,990.00 USD | 0.00 USD | 142,990.00 USD | 6,760.00 USD | 34,180.00 USD | 5,700.00 USD |
| `7D` | `0.1615` | 959,480.00 USD | 0.00 USD | 959,480.00 USD | 293,210.00 USD | 35,210.00 USD | 243,310.00 USD |
| `1D` | `0.1618` | 96,350.00 USD | 0.00 USD | 96,350.00 USD | 0.00 USD | 12,770.00 USD | 0.00 USD |
| `7D` | `0.1618` | 387,750.00 USD | 0.00 USD | 387,750.00 USD | 0.00 USD | 0.00 USD | 47,590.00 USD |
| `1D` | `0.1620` | 83,580.00 USD | 0.00 USD | 83,580.00 USD | 0.00 USD | 8,710.00 USD | 30,970.00 USD |
| `7D` | `0.1621` | 340,160.00 USD | 0.00 USD | 340,160.00 USD | 78,750.00 USD | 57,300.00 USD | 0.00 USD |
| `1D` | `0.1622` | 43,910.00 USD | 0.00 USD | 43,910.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD |
| `7D` | `0.1624` | 204,110.00 USD | 0.00 USD | 204,110.00 USD | 0.00 USD | 170,670.00 USD | 33,440.00 USD |
| `1D` | `0.1626` | 38,240.00 USD | 0.00 USD | 38,240.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1626` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1627` | 180,100.00 USD | 180,100.00 USD | 0.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `7D` | `0.1630` | 251,040.00 USD | 251,040.00 USD | 0.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1632` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1634` | 8,690.00 USD | 8,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,690.00 USD |
| `1D` | `0.1636` | 23,560.00 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `1D` | `0.1648` | 40,160.00 USD | 40,160.00 USD | 0.00 USD | 11,310.00 USD | 3,450.00 USD | 1,840.00 USD |
| `1D` | `0.1650` | 54,760.00 USD | 54,760.00 USD | 0.00 USD | 14,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1652` | 76,500.00 USD | 76,500.00 USD | 0.00 USD | 21,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1654` | 95,190.00 USD | 95,190.00 USD | 0.00 USD | 5,600.00 USD | 2,360.00 USD | 10,730.00 USD |
| `1D` | `0.1656` | 115,230.00 USD | 115,230.00 USD | 0.00 USD | 20,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1658` | 116,790.00 USD | 116,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,570.00 USD |
| `1D` | `0.1660` | 146,870.00 USD | 146,870.00 USD | 0.00 USD | 0.00 USD | 12,450.00 USD | 17,620.00 USD |
| `7D` | `0.1660` | 348,650.00 USD | 348,650.00 USD | 0.00 USD | 68,280.00 USD | 29,330.00 USD | 0.00 USD |
| `1D` | `0.1662` | 195,150.00 USD | 195,150.00 USD | 0.00 USD | 11,790.00 USD | 15,780.00 USD | 20,710.00 USD |
| `7D` | `0.1663` | 498,720.00 USD | 498,720.00 USD | 0.00 USD | 121,520.00 USD | 0.00 USD | 28,550.00 USD |
| `1D` | `0.1664` | 254,960.00 USD | 254,960.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | 50,530.00 USD |
| `1D` | `0.1666` | 314,000.00 USD | 314,000.00 USD | 0.00 USD | 21,340.00 USD | 5,340.00 USD | 32,360.00 USD |
| `7D` | `0.1666` | 589,790.00 USD | 589,790.00 USD | 0.00 USD | 49,590.00 USD | 12,670.00 USD | 28,810.00 USD |
| `1D` | `0.1668` | 333,320.00 USD | 333,320.00 USD | 0.00 USD | 0.00 USD | 11,890.00 USD | 7,440.00 USD |
| `7D` | `0.1669` | 834,070.00 USD | 834,070.00 USD | 0.00 USD | 76,120.00 USD | 81,000.00 USD | 87,160.00 USD |
| `1D` | `0.1670` | 354,560.00 USD | 354,560.00 USD | 0.00 USD | 4,600.00 USD | 3,850.00 USD | 12,790.00 USD |
| `1D` | `0.1672` | 438,720.00 USD | 438,720.00 USD | 0.00 USD | 56,860.00 USD | 3,960.00 USD | 23,340.00 USD |
| `7D` | `0.1672` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 96,910.00 USD | 38,070.00 USD | 68,760.00 USD |
| `1D` | `0.1674` | 510,420.00 USD | 510,420.00 USD | 0.00 USD | 20,040.00 USD | 9,620.00 USD | 42,040.00 USD |
| `7D` | `0.1675` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 64,490.00 USD | 130,100.00 USD | 0.00 USD |
| `1D` | `0.1676` | 683,540.00 USD | 683,540.00 USD | 0.00 USD | 82,670.00 USD | 60,390.00 USD | 30,060.00 USD |
| `1D` | `0.1678` | 739,230.00 USD | 739,230.00 USD | 0.00 USD | 26,550.00 USD | 0.00 USD | 29,140.00 USD |
| `7D` | `0.1678` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 71,860.00 USD | 90,910.00 USD | 16,740.00 USD |
| `1D` | `0.1680` | 841,580.00 USD | 841,580.00 USD | 0.00 USD | 70,670.00 USD | 22,970.00 USD | 8,710.00 USD |
| `7D` | `0.1681` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 69,520.00 USD | 71,610.00 USD | 128,480.00 USD |
| `1D` | `0.1682` | 991,020.00 USD | 991,020.00 USD | 0.00 USD | 49,580.00 USD | 33,250.00 USD | 66,620.00 USD |
| `1D` | `0.1684` | 1,110,000.00 USD | 1,110,000.00 USD | 0.00 USD | 57,770.00 USD | 40,190.00 USD | 18,640.00 USD |
| `7D` | `0.1684` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1686` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 28,370.00 USD | 18,520.00 USD | 78,360.00 USD |
| `7D` | `0.1687` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 78,750.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1688` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 13,300.00 USD | 6,850.00 USD | 59,050.00 USD |
| `1D` | `0.1690` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 63,270.00 USD | 29,860.00 USD | 42,990.00 USD |
| `7D` | `0.1690` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 63,850.00 USD | 74,130.00 USD |
| `1D` | `0.1692` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 66,540.00 USD | 92,730.00 USD | 120,590.00 USD |
| `7D` | `0.1693` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 33,660.00 USD | 46,740.00 USD | 42,090.00 USD |
| `1D` | `0.1694` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 47,210.00 USD | 26,920.00 USD | 16,900.00 USD |
| `1D` | `0.1696` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 23,530.00 USD | 4,640.00 USD | 9,670.00 USD |
| `7D` | `0.1696` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 28,010.00 USD |
| `1D` | `0.1698` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 36,670.00 USD | 57,580.00 USD | 48,960.00 USD |
| `7D` | `0.1699` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD |
| `1D` | `0.1700` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 5,080.00 USD | 0.00 USD |
| `1D` | `0.1702` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 9,960.00 USD | 1,920.00 USD | 40,930.00 USD |
| `7D` | `0.1702` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 72,270.00 USD |
| `1D` | `0.1704` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 11,790.00 USD | 14,420.00 USD | 11,670.00 USD |
| `7D` | `0.1705` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 34,380.00 USD |
| `1D` | `0.1706` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 44,560.00 USD | 14,400.00 USD | 13,990.00 USD |
| `1D` | `0.1708` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 26,090.00 USD | 63,220.00 USD | 12,660.00 USD |
| `7D` | `0.1708` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 87,520.00 USD |
| `1D` | `0.1710` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 30,670.00 USD | 29,200.00 USD | 30,180.00 USD |
| `7D` | `0.1711` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 8,370.00 USD |
| `1D` | `0.1712` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 16,380.00 USD | 21,110.00 USD | 7,610.00 USD |
| `1D` | `0.1714` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 1,800.00 USD | 16,560.00 USD | 10,630.00 USD |
| `7D` | `0.1714` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 38,720.00 USD |
| `1D` | `0.1716` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 19,740.00 USD | 31,850.00 USD | 28,920.00 USD |
| `7D` | `0.1717` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1718` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 20,700.00 USD | 20,360.00 USD | 18,970.00 USD |
| `1D` | `0.1720` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 34,970.00 USD | 2,830.00 USD | 17,440.00 USD |
| `7D` | `0.1720` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1722` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 69,510.00 USD | 25,370.00 USD | 54,870.00 USD |
| `7D` | `0.1723` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 118,060.00 USD | 12,590.00 USD | 225,200.00 USD |
| `1D` | `0.1724` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 8,230.00 USD | 1,570.00 USD | 52,310.00 USD |
| `1D` | `0.1726` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 10,260.00 USD | 12,580.00 USD | 24,010.00 USD |
| `1D` | `0.1728` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 10,590.00 USD |
| `7D` | `0.1729` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 120,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1732` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 6,670.00 USD | 0.00 USD | 10,060.00 USD |
| `7D` | `0.1732` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 324,890.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1734` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 1,280.00 USD | 1,560.00 USD | 1,170.00 USD |
| `1D` | `0.1736` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 0.00 USD |
| `1D` | `0.1738` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 15,900.00 USD | 3,450.00 USD | 6,410.00 USD |
| `7D` | `0.1738` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1740` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 4,490.00 USD | 2,500.00 USD |
| `1D` | `0.1742` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD |
| `1D` | `0.1744` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 2,460.00 USD | 2,660.00 USD |
| `7D` | `0.1744` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1746` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 3,500.00 USD | 0.00 USD | 6,510.00 USD |
| `1D` | `0.1748` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 55,280.00 USD | 2,280.00 USD | 36,350.00 USD |
| `1D` | `0.1750` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 24,790.00 USD | 0.00 USD | 8,710.00 USD |
| `7D` | `0.1750` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 120,240.00 USD |
| `1D` | `0.1752` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 30,220.00 USD | 0.00 USD | 25,110.00 USD |
| `7D` | `0.1753` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 197,880.00 USD |
| `1D` | `0.1754` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 21,260.00 USD | 8,430.00 USD | 14,700.00 USD |
| `1D` | `0.1756` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 6,850.00 USD | 3,540.00 USD | 47,910.00 USD |
| `7D` | `0.1756` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 53,560.00 USD |
| `1D` | `0.1758` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 28,730.00 USD | 14,260.00 USD | 13,460.00 USD |
| `7D` | `0.1759` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 200,480.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1760` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 17,680.00 USD | 69,600.00 USD | 5,890.00 USD |
| `1D` | `0.1762` | 3,560,000.00 USD | 3,560,000.00 USD | 0.00 USD | 50,470.00 USD | 2,140.00 USD | 60,400.00 USD |
| `7D` | `0.1762` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 117,200.00 USD | 94,740.00 USD | 32,350.00 USD |
| `1D` | `0.1764` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 8,260.00 USD | 25,840.00 USD | 38,630.00 USD |
| `7D` | `0.1765` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 154,540.00 USD | 97,630.00 USD | 48,870.00 USD |
| `1D` | `0.1766` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 7,570.00 USD | 3,150.00 USD | 32,550.00 USD |
| `1D` | `0.1768` | 3,790,000.00 USD | 3,790,000.00 USD | 0.00 USD | 19,860.00 USD | 70,050.00 USD | 25,200.00 USD |
| `7D` | `0.1768` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 161,560.00 USD | 92,440.00 USD | 23,040.00 USD |
| `1D` | `0.1770` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 32,300.00 USD | 12,060.00 USD | 14,520.00 USD |
| `7D` | `0.1771` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 69,030.00 USD | 83,790.00 USD | 21,360.00 USD |
| `1D` | `0.1772` | 3,890,000.00 USD | 3,890,000.00 USD | 0.00 USD | 4,900.00 USD | 9,310.00 USD | 21,240.00 USD |
| `1D` | `0.1774` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 12,400.00 USD | 14,420.00 USD | 5,300.00 USD |
| `7D` | `0.1774` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 148,780.00 USD | 85,710.00 USD | 0.00 USD |
| `1D` | `0.1776` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 22,060.00 USD | 12,480.00 USD | 9,130.00 USD |
| `7D` | `0.1777` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD |
| `1D` | `0.1778` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 26,670.00 USD | 71,670.00 USD | 11,450.00 USD |
| `1D` | `0.1780` | 4,090,000.00 USD | 4,090,000.00 USD | 0.00 USD | 1,740.00 USD | 1,610.00 USD | 9,410.00 USD |
| `7D` | `0.1780` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 52,730.00 USD | 38,910.00 USD | 46,470.00 USD |
| `1D` | `0.1782` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 2,050.00 USD | 10,130.00 USD | 14,570.00 USD |
| `7D` | `0.1783` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1784` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 40,030.00 USD | 8,820.00 USD | 5,250.00 USD |
| `1D` | `0.1786` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 7,560.00 USD | 25,290.00 USD | 7,120.00 USD |
| `7D` | `0.1786` | 6,690,000.00 USD | 6,690,000.00 USD | 0.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1788` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 9,350.00 USD | 20,220.00 USD | 3,230.00 USD |
| `7D` | `0.1789` | 6,740,000.00 USD | 6,740,000.00 USD | 0.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.1790` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 2,490.00 USD | 7,370.00 USD |
| `1D` | `0.1792` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 4,850.00 USD | 0.00 USD |
| `7D` | `0.1792` | 6,920,000.00 USD | 6,920,000.00 USD | 0.00 USD | 134,000.00 USD | 43,520.00 USD | 3,940.00 USD |
| `1D` | `0.1794` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 13,620.00 USD | 34,190.00 USD | 2,660.00 USD |
| `7D` | `0.1795` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD |
| `1D` | `0.1796` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 22,740.00 USD | 0.00 USD | 21,080.00 USD |
| `1D` | `0.1798` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 11,150.00 USD | 11,410.00 USD |
| `7D` | `0.1798` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD |
| `1D` | `0.1800` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 3,780.00 USD | 2,030.00 USD | 11,240.00 USD |
| `7D` | `0.1801` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 19,430.00 USD | 43,480.00 USD | 55,340.00 USD |
| `1D` | `0.1802` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 6,120.00 USD | 28,340.00 USD | 13,660.00 USD |
| `7D` | `0.1804` | 7,240,000.00 USD | 7,240,000.00 USD | 0.00 USD | 28,790.00 USD | 27,450.00 USD | 25,100.00 USD |
| `7D` | `0.1807` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD |
| `7D` | `0.1810` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD |
| `7D` | `0.1813` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 32,530.00 USD | 15,780.00 USD | 67,760.00 USD |
| `7D` | `0.1816` | 7,720,000.00 USD | 7,720,000.00 USD | 0.00 USD | 46,430.00 USD | 21,200.00 USD | 35,500.00 USD |
| `7D` | `0.1819` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 52,150.00 USD | 24,720.00 USD | 43,100.00 USD |
| `7D` | `0.1822` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 46,760.00 USD | 29,530.00 USD | 37,430.00 USD |
| `7D` | `0.1825` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 38,800.00 USD | 17,120.00 USD | 20,270.00 USD |
| `7D` | `0.1828` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 29,430.00 USD | 13,380.00 USD | 17,090.00 USD |
| `7D` | `0.1831` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 63,190.00 USD | 9,610.00 USD | 24,180.00 USD |
| `7D` | `0.1834` | 8,220,000.00 USD | 8,220,000.00 USD | 0.00 USD | 18,400.00 USD | 0.00 USD | 15,630.00 USD |
| `7D` | `0.1837` | 8,330,000.00 USD | 8,330,000.00 USD | 0.00 USD | 11,490.00 USD | 13,450.00 USD | 83,480.00 USD |
| `7D` | `0.1840` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 70,360.00 USD | 18,020.00 USD | 65,400.00 USD |
| `7D` | `0.1843` | 8,530,000.00 USD | 8,530,000.00 USD | 0.00 USD | 17,340.00 USD | 3,040.00 USD | 28,930.00 USD |
| `7D` | `0.1846` | 8,600,000.00 USD | 8,600,000.00 USD | 0.00 USD | 8,330.00 USD | 10,850.00 USD | 42,240.00 USD |
| `7D` | `0.1848` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 35,280.00 USD | 35,270.00 USD | 5,880.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `184.29M` | Total OI Tokens: `1,127,944,082.6 ARB`
  * 1h OI Change: `+0.66%` | 4h OI Change: `-0.45%` | 24h OI Change: `-14.35%`
  * Exchange Breakdown: Binance=`40.39M` | Bybit=`25.88M` | OKX=`13.98M` | Hyperliquid=`12.92M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.01K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0075%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0049%` | **USDT Bitget** | `0.0010%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `55.41%` | `44.59%` | `1.24` | 640,470.00 USD |
| `15M` | `Binance` | `52.6%` | `47.4%` | `1.11` | 199,980.00 USD |
| `15M` | `OKX` | `58.13%` | `41.87%` | `1.39` | 53,470.00 USD |
| `15M` | `Bybit` | `48.26%` | `51.74%` | `0.93` | 46,600.00 USD |
| `15M` | `KuCoin` | `55.14%` | `44.86%` | `1.23` | 35,980.00 USD |
| `15M` | `Gate` | `52.05%` | `47.95%` | `1.09` | 14,490.00 USD |
| `15M` | `Bitget` | `41.12%` | `58.88%` | `0.70` | 7,340.00 USD |
| `15M` | `BingX` | `55.19%` | `44.81%` | `1.23` | 37,780.00 USD |
| `15M` | `MEXC` | `70.11%` | `29.89%` | `2.35` | 77,510.00 USD |
| `15M` | `Bitunix` | `57.04%` | `42.96%` | `1.33` | 5,860.00 USD |
| `15M` | `Hyperliquid` | `58.05%` | `41.95%` | `1.38` | 11,490.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.23%` | `44.77%` | `1.23` | 118,380.00 USD |
| `15M` | `Crypto.com` | `100%` | `0%` | `1.00` | 0.21 USD |
| `15M` | `WhiteBIT` | `60.47%` | `39.53%` | `1.53` | 24,720.00 USD |
| `15M` | `HTX` | `70.43%` | `29.57%` | `2.38` | 1.30 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `100%` | `0%` | `1.00` | 54.28 USD |
| `15M` | `Aster` | `8.81%` | `91.19%` | `0.10` | 113.46 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `2.19%` | `97.81%` | `0.02` | 6,690.00 USD |
| `15M` | `Whale Positions` | `52.6%` | `47.4%` | `1.11` | 199,980.00 USD |
| `15M` | `Global Accounts` | `55.41%` | `44.59%` | `1.24` | 640,470.00 USD |
| `1H` | `ARB` | `52.72%` | `47.28%` | `1.12` | 3,420,000.00 USD |
| `1H` | `Binance` | `50.3%` | `49.7%` | `1.01` | 1,110,000.00 USD |
| `1H` | `OKX` | `63.85%` | `36.15%` | `1.77` | 449,980.00 USD |
| `1H` | `Bybit` | `58.6%` | `41.4%` | `1.42` | 295,390.00 USD |
| `1H` | `KuCoin` | `49.75%` | `50.25%` | `0.99` | 192,570.00 USD |
| `1H` | `Gate` | `34.46%` | `65.54%` | `0.53` | 71,200.00 USD |
| `1H` | `Bitget` | `39.85%` | `60.15%` | `0.66` | 69,870.00 USD |
| `1H` | `BingX` | `41.99%` | `58.01%` | `0.72` | 171,570.00 USD |
| `1H` | `MEXC` | `58.62%` | `41.38%` | `1.42` | 237,800.00 USD |
| `1H` | `Bitunix` | `52.21%` | `47.79%` | `1.09` | 29,260.00 USD |
| `1H` | `Hyperliquid` | `44.28%` | `55.72%` | `0.79` | 53,830.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `54.14%` | `45.86%` | `1.18` | 580,900.00 USD |
| `1H` | `Crypto.com` | `18.46%` | `81.54%` | `0.23` | 4.55 USD |
| `1H` | `WhiteBIT` | `64.62%` | `35.38%` | `1.83` | 104,590.00 USD |
| `1H` | `HTX` | `87.27%` | `12.73%` | `6.86` | 15.50 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0.82%` | `99.18%` | `0.01` | 8,900.00 USD |
| `1H` | `Aster` | `17.69%` | `82.31%` | `0.21` | 990.85 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `1.34%` | `98.66%` | `0.01` | 37,790.00 USD |
| `1H` | `Whale Positions` | `50.3%` | `49.7%` | `1.01` | 1,110,000.00 USD |
| `1H` | `Global Accounts` | `52.72%` | `47.28%` | `1.12` | 3,420,000.00 USD |
| `4H` | `ARB` | `49.45%` | `50.55%` | `0.98` | 41,170,000.00 USD |
| `4H` | `Binance` | `50.08%` | `49.92%` | `1.00` | 15,020,000.00 USD |
| `4H` | `OKX` | `47.28%` | `52.72%` | `0.90` | 6,000,000.00 USD |
| `4H` | `Bybit` | `49.42%` | `50.58%` | `0.98` | 4,250,000.00 USD |
| `4H` | `KuCoin` | `48.89%` | `51.11%` | `0.96` | 720,720.00 USD |
| `4H` | `Gate` | `47.42%` | `52.58%` | `0.90` | 1,340,000.00 USD |
| `4H` | `Bitget` | `50.15%` | `49.85%` | `1.01` | 2,750,000.00 USD |
| `4H` | `BingX` | `28.52%` | `71.48%` | `0.40` | 3,300,000.00 USD |
| `4H` | `MEXC` | `50.23%` | `49.77%` | `1.01` | 2,970,000.00 USD |
| `4H` | `Bitunix` | `50.24%` | `49.76%` | `1.01` | 608,710.00 USD |
| `4H` | `Hyperliquid` | `60.32%` | `39.68%` | `1.52` | 613,040.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.59%` | `50.41%` | `0.98` | 1,470,000.00 USD |
| `4H` | `Crypto.com` | `37.02%` | `62.98%` | `0.59` | 22,800.00 USD |
| `4H` | `WhiteBIT` | `86.06%` | `13.94%` | `6.17` | 1,780,000.00 USD |
| `4H` | `HTX` | `66.69%` | `33.31%` | `2.00` | 13,810.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `41.98%` | `58.02%` | `0.72` | 102,890.00 USD |
| `4H` | `Aster` | `27.85%` | `72.15%` | `0.39` | 30,700.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.78%` | `47.22%` | `1.12` | 192,000.00 USD |
| `4H` | `Whale Positions` | `50.08%` | `49.92%` | `1.00` | 15,020,000.00 USD |
| `4H` | `Global Accounts` | `49.45%` | `50.55%` | `0.98` | 41,170,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1639` | `0.1637` | `0.1639` | `0.1646` | `0.1631` | 946,588.03 USD | 498,466.74 USD | 448,121.29 USD | 50,345.45 USD | `+5.32%` | `36B / 23S` |
| `5:00 UTC` | `0.1625` | `0.1631` | `0.1625` | `0.1640` | `0.1624` | 778,400.97 USD | 315,731.23 USD | 462,669.74 USD | -146,938.51 USD | `-18.88%` | `22B / 62S` |
| `0:00 UTC` | `0.1629` | `0.1625` | `0.1629` | `0.1632` | `0.1619` | 775,902.97 USD | 309,320.91 USD | 466,582.05 USD | -157,261.14 USD | `-20.27%` | `13B / 34S` |
| `5:00 UTC` | `0.1623` | `0.1620` | `0.1623` | `0.1624` | `0.1615` | 562,907.20 USD | 223,683.16 USD | 339,224.04 USD | -115,540.88 USD | `-20.53%` | `7B / 21S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1623` | `0.1611` | 779,913.00 USD | 372,491.97 USD | 407,421.03 USD | -34,929.06 USD | `-4.48%` | `22B / 23S` |
| `5:00 UTC` | `0.1620` | `0.1619` | `0.1620` | `0.1622` | `0.1615` | 338,104.92 USD | 163,363.17 USD | 174,741.74 USD | -11,378.57 USD | `-3.37%` | `6B / 19S` |
| `0:00 UTC` | `0.1617` | `0.1618` | `0.1617` | `0.1624` | `0.1613` | 561,491.28 USD | 247,384.47 USD | 314,106.81 USD | -66,722.34 USD | `-11.88%` | `26B / 27S` |
| `5:00 UTC` | `0.1628` | `0.1622` | `0.1628` | `0.1629` | `0.1614` | 451,221.10 USD | 279,978.35 USD | 171,242.75 USD | 108,735.60 USD | `+24.10%` | `38B / 17S` |
| `0:00 UTC` | `0.1626` | `0.1627` | `0.1626` | `0.1631` | `0.1620` | 555,739.49 USD | 264,990.40 USD | 290,749.08 USD | -25,758.68 USD | `-4.64%` | `27B / 22S` |
| `5:00 UTC` | `0.1626` | `0.1627` | `0.1626` | `0.1629` | `0.1625` | 238,726.08 USD | 149,731.42 USD | 88,994.66 USD | 60,736.75 USD | `+25.44%` | `14B / 2S` |

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
| `5m` | 19,920.00 USD | 90,640.00 USD | **`ACCUMULATION`** |
| `15m` | 55,340.00 USD | -10,330.00 USD | **`ACCUMULATION`** |
| `30m` | 73,370.00 USD | 271,120.00 USD | **`ACCUMULATION`** |
| `1h` | 37,490.00 USD | 216,360.00 USD | **`ACCUMULATION`** |
| `2h` | -383,920.00 USD | -427,980.00 USD | **`DISTRIBUTION`** |
| `4h` | -347,360.00 USD | -67,820.00 USD | **`DISTRIBUTION`** |
| `6h` | -562,570.00 USD | -3,360,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -543,300.00 USD | -1,660,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -896,150.00 USD | -2,300,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,440,000.00 USD | -11,060,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,530,000.00 USD | -37,340,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,630,000.00 USD | -166,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+19.92K` | 15m=`+55.34K` | 1h=`+37.49K` | 24h=`-2.44M`
* Futures Capital Netflows: 5m=`+90.64K` | 15m=`-10.33K` | 1h=`+216.36K` | 24h=`-11.06M`
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
