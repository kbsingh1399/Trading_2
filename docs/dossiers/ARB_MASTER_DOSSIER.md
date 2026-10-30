# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ARB
**Canonical Key**: `ARB` | **Broker Instrument**: `ARBUSD.p` | **Asset Class**: `Crypto Alt L2`
**Timestamp**: `2026-10-30 16:42:50 IST` (`2026-10-30 11:12:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.1640` | `0.1641` | `0.1635` | `0.1636` | `1,661,985` | 272,239.75 USD | 8,363.32 USD | `+3.07%` | -7,357,518.70 USD | `-0.11` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1636` | `0.1640` | `0.1632` | `0.1633` | `1,918,867` | 313,839.47 USD | 87,975.34 USD | `+28.03%` | -7,269,543.36 USD | `+1.02` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.1633` | `0.1636` | `0.1631` | `0.1633` | `446,711` | 72,974.03 USD | 4,553.48 USD | `+6.24%` | -7,264,989.88 USD | `-0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.1622` | `0.1631` | `0.1620` | `0.1627` | `3,416,453` | 555,739.49 USD | -25,758.68 USD | `-4.64%` | -7,708,495.36 USD | `-0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.1627` | `0.1643` | `0.1623` | `0.1640` | `5,875,262` | 958,344.10 USD | 342,613.33 USD | `+35.75%` | -7,365,882.02 USD | `+2.04` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `0.1640` | `0.1641` | `0.1631` | `0.1633` | `4,027,564` | 659,053.25 USD | 100,892.15 USD | `+15.31%` | -7,264,989.88 USD | `+0.52` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.1629` | `0.1632` | `0.1611` | `0.1621` | `15,160,560` | 2,456,828.08 USD | -319,109.65 USD | `-12.99%` | -7,482,204.74 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.1621` | `0.1643` | `0.1613` | `0.1640` | `15,542,725` | 2,526,795.97 USD | 358,867.92 USD | `+14.20%` | -7,123,336.83 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.1640` | `0.1641` | `0.1631` | `0.1633` | `4,028,229` | 659,161.92 USD | 101,000.82 USD | `+15.32%` | -7,022,336.01 USD | `+0.38` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1633` | `64,659,114` | 10,554,636.51 USD | -174,930.05 USD | `-1.66%` | -7,022,444.68 USD | `+0.81` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1745` | `0.1759` | `0.1673` | `0.1683` | `85,850,218` | 14,657,035.37 USD | -1,197,458.00 USD | `-8.17%` | -2,435,586.34 USD | `+1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1683` | `0.1684` | `0.1508` | `0.1542` | `355,450,890` | 55,657,564.18 USD | -3,724,223.97 USD | `-6.69%` | -6,159,810.32 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1542` | `0.1585` | `0.1471` | `0.1580` | `199,849,201` | 30,537,556.03 USD | -620,938.51 USD | `-2.03%` | -6,780,748.83 USD | `+0.90` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1580` | `0.1665` | `0.1577` | `0.1649` | `114,713,582` | 18,773,815.61 USD | -66,765.80 USD | `-0.36%` | -6,847,514.63 USD | `+1.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1650` | `0.1657` | `0.1611` | `0.1633` | `64,659,114` | 10,554,636.51 USD | -174,930.05 USD | `-1.66%` | -7,022,444.68 USD | `+0.81` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:42:20 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.1665` | 9,204.24 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 9.20K USD at 0.1665 USD [API] | `2026-10-29 20:02:44` |
| `ANNOUNCEMENT` | `INFO` | `0.1666` | 7,123.24 USD | `-` | `NEWS_INTEL` | `-` | #ARB Whale SELL: 7.12K USD at 0.1666 USD [API] | `2026-10-29 20:02:44` |
| `ANNOUNCEMENT` | `INFO` | `0.1625` | 9,769.92 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 9.77K USD at 0.1625 USD [API] | `2026-10-29 07:16:16` |
| `ANNOUNCEMENT` | `INFO` | `0.1630` | 4,247.83 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.25K USD at 0.1630 USD [API] | `2026-10-29 07:16:12` |
| `ANNOUNCEMENT` | `INFO` | `0.1640` | 4,556.63 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 4.56K USD at 0.1640 USD [API] | `2026-10-29 20:06:55` |
| `ANNOUNCEMENT` | `INFO` | `0.1616` | 1,667.74 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.67K USD at 0.1616 USD [API] | `2026-10-29 20:34:08` |
| `ANNOUNCEMENT` | `INFO` | `0.1617` | 1,677.74 USD | `-` | `NEWS_INTEL` | `-` | #ARB Liquidated Short: 1.68K USD at 0.1617 USD [API] | `2026-10-29 20:34:08` |


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
| `Live` | `Long Liquidation` | `0.0385` | 1,490.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0415` | 110.22 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0425` | 4,420.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 1,560.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0475` | 121.77 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0485` | 107.79 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 109.52 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0505` | 610.70 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 1,030.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 289.43 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 479.20 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 2,270.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 16,360.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0585` | 1,100.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 186.63 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 219,780.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0635` | 6,470.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 104,180.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 313.22 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 976.14 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0705` | 3,280.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 6,070.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0725` | 61,160.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 2,440.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0745` | 226.17 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0765` | 14,690.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0795` | 4,630.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0825` | 18,860.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 21,410.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 4,830.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 3,030.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0895` | 364.11 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 113.80 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 2,410.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 2,680.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 1,510.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0965` | 10,890.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 589.74 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 3,540.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 7,670.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1005` | 10,640.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 3,570.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 5,700.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 6,500.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 8,930.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 181.20 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 1,060.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 11,210.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1105` | 14,360.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 425.50 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 368.45 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 281.48 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 8,950.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 7,630.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 129,500.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 25,800.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1195` | 3,150.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,730.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1225` | 19,560.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 50,430.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 377.05 USD | 982,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 134.66 USD | 981,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 16,720.00 USD | 981,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 10,250.00 USD | 964,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 645.03 USD | 954,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 3,330.00 USD | 954,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 32,320.00 USD | 950,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 14,350.00 USD | 918,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 4,640.00 USD | 904,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 51,860.00 USD | 899,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 28,900.00 USD | 847,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 8,620.00 USD | 818,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1357` | 8,700,000.00 USD | 8,700,000.00 USD | 21,410.00 USD | 17,110.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1360` | 8,650,000.00 USD | 8,650,000.00 USD | 16,290.00 USD | 3,690.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1363` | 8,630,000.00 USD | 8,630,000.00 USD | 7,890.00 USD | 3,220.00 USD | 4,690.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1365` | 8,320.00 USD | 810,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1366` | 8,610,000.00 USD | 8,610,000.00 USD | 11,610.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1369` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1372` | 8,590,000.00 USD | 8,590,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1375` | 8,580,000.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1375` | 25,370.00 USD | 801,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1378` | 8,550,000.00 USD | 8,550,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1384` | 8,530,000.00 USD | 8,530,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1385` | 4,330.00 USD | 776,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1387` | 8,490,000.00 USD | 8,490,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1390` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1393` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 50,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1395` | 9,210.00 USD | 772,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1396` | 8,410,000.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1399` | 8,380,000.00 USD | 8,380,000.00 USD | 6,210.00 USD | 4,200.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1402` | 8,370,000.00 USD | 8,370,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1405` | 2,640.00 USD | 762,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 493,500.00 USD | 760,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1417` | 8,360,000.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1420` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1423` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1425` | 22,060.00 USD | 266,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1435` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1435` | 18,970.00 USD | 244,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1438` | 8,300,000.00 USD | 8,300,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1441` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1445` | 9,510.00 USD | 225,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1450` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1451` | 4,860,000.00 USD | 4,860,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1453` | 4,840,000.00 USD | 4,840,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1455` | 4,830,000.00 USD | 4,830,000.00 USD | 3,450.00 USD | 689.96 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1455` | 92,080.00 USD | 216,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1457` | 4,830,000.00 USD | 4,830,000.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1459` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1461` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 3,000.00 USD | 2,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1463` | 4,800,000.00 USD | 4,800,000.00 USD | 9,940.00 USD | 3,900.00 USD | 5,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1465` | 4,790,000.00 USD | 4,790,000.00 USD | 11,020.00 USD | 8,490.00 USD | 11,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1465` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 3,700.00 USD | 93,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1465` | 23,540.00 USD | 124,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1467` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1468` | 8,160,000.00 USD | 8,160,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1469` | 4,750,000.00 USD | 4,750,000.00 USD | 5,850.00 USD | 1,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1471` | 4,740,000.00 USD | 4,740,000.00 USD | 10,000.00 USD | 7,170.00 USD | 933.22 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1471` | 8,140,000.00 USD | 8,140,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1473` | 4,730,000.00 USD | 4,730,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1474` | 8,140,000.00 USD | 8,140,000.00 USD | 19,430.00 USD | 12,610.00 USD | 24,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1475` | 4,600,000.00 USD | 4,600,000.00 USD | 20,680.00 USD | 7,230.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1475` | 82,910.00 USD | 100,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1477` | 4,560,000.00 USD | 4,560,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1477` | 8,080,000.00 USD | 8,080,000.00 USD | 85,800.00 USD | 25,460.00 USD | 110,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1479` | 4,280,000.00 USD | 4,280,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1480` | 7,860,000.00 USD | 7,860,000.00 USD | 50,400.00 USD | 29,300.00 USD | 20,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1481` | 4,170,000.00 USD | 4,170,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1483` | 4,120,000.00 USD | 4,120,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1483` | 7,760,000.00 USD | 7,760,000.00 USD | 42,230.00 USD | 16,640.00 USD | 202,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1485` | 3,960,000.00 USD | 3,960,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1485` | 2,290.00 USD | 17,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1486` | 7,500,000.00 USD | 7,500,000.00 USD | 66,760.00 USD | 10,470.00 USD | 35,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1487` | 3,840,000.00 USD | 3,840,000.00 USD | 8,840.00 USD | 3,580.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1489` | 3,820,000.00 USD | 3,820,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1489` | 7,380,000.00 USD | 7,380,000.00 USD | 21,100.00 USD | 3,710.00 USD | 67,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1491` | 3,790,000.00 USD | 3,790,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1492` | 7,290,000.00 USD | 7,290,000.00 USD | 40,320.00 USD | 22,920.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1493` | 3,740,000.00 USD | 3,740,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1495` | 3,700,000.00 USD | 3,700,000.00 USD | 56,660.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1495` | 7,190,000.00 USD | 7,190,000.00 USD | 34,650.00 USD | 18,690.00 USD | 191,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1495` | 937.17 USD | 15,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1497` | 3,620,000.00 USD | 3,620,000.00 USD | 8,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1498` | 6,950,000.00 USD | 6,950,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1499` | 3,610,000.00 USD | 3,610,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1501` | 3,590,000.00 USD | 3,590,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1501` | 6,890,000.00 USD | 6,890,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1503` | 3,560,000.00 USD | 3,560,000.00 USD | 48,710.00 USD | 4,400.00 USD | 153,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1504` | 6,840,000.00 USD | 6,840,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1505` | 3,360,000.00 USD | 3,360,000.00 USD | 35,380.00 USD | 1,940.00 USD | 5,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1507` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1507` | 6,770,000.00 USD | 6,770,000.00 USD | 152,330.00 USD | 12,910.00 USD | 182,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1509` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1510` | 6,420,000.00 USD | 6,420,000.00 USD | 135,010.00 USD | 12,930.00 USD | 112,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1511` | 2,950,000.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1513` | 2,950,000.00 USD | 2,950,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1513` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 17,610.00 USD | 104,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1515` | 2,690,000.00 USD | 2,690,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1516` | 6,040,000.00 USD | 6,040,000.00 USD | 48,970.00 USD | 0.00 USD | 338,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1517` | 2,560,000.00 USD | 2,560,000.00 USD | 12,390.00 USD | 6,150.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1519` | 2,520,000.00 USD | 2,520,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1519` | 5,650,000.00 USD | 5,650,000.00 USD | 47,340.00 USD | 24,320.00 USD | 70,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1521` | 2,440,000.00 USD | 2,440,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1522` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 9,640.00 USD | 130,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1523` | 2,390,000.00 USD | 2,390,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1525` | 2,380,000.00 USD | 2,380,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1525` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1527` | 2,340,000.00 USD | 2,340,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1528` | 5,350,000.00 USD | 5,350,000.00 USD | 0.00 USD | 31,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1529` | 2,320,000.00 USD | 2,320,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1531` | 2,290,000.00 USD | 2,290,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1531` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 8,400.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1533` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1534` | 5,310,000.00 USD | 5,310,000.00 USD | 35,470.00 USD | 17,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1535` | 2,260,000.00 USD | 2,260,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1537` | 2,240,000.00 USD | 2,240,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1537` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 11,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1539` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1540` | 5,250,000.00 USD | 5,250,000.00 USD | 0.00 USD | 6,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1541` | 2,210,000.00 USD | 2,210,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1543` | 5,240,000.00 USD | 5,240,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1545` | 2,170,000.00 USD | 2,170,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1545` | 2,550.00 USD | 14,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1547` | 2,140,000.00 USD | 2,140,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1549` | 2,120,000.00 USD | 2,120,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1549` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 19,500.00 USD | 89,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1551` | 2,070,000.00 USD | 2,070,000.00 USD | 14,290.00 USD | 12,210.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1552` | 5,130,000.00 USD | 5,130,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1553` | 2,040,000.00 USD | 2,040,000.00 USD | 12,260.00 USD | 4,020.00 USD | 5,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1555` | 2,010,000.00 USD | 2,010,000.00 USD | 40,830.00 USD | 1,660.00 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1555` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1555` | 2,170.00 USD | 11,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1557` | 1,960,000.00 USD | 1,960,000.00 USD | 2,800.00 USD | 12,870.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1558` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1559` | 1,940,000.00 USD | 1,940,000.00 USD | 17,010.00 USD | 2,970.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1561` | 1,920,000.00 USD | 1,920,000.00 USD | 12,360.00 USD | 3,020.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1561` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1563` | 1,900,000.00 USD | 1,900,000.00 USD | 11,460.00 USD | 25,680.00 USD | 3,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1564` | 4,900,000.00 USD | 4,900,000.00 USD | 0.00 USD | 43,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1565` | 1,850,000.00 USD | 1,850,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1565` | 9,660.00 USD | 9,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1567` | 1,760,000.00 USD | 1,760,000.00 USD | 25,400.00 USD | 1,850.00 USD | 9,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1567` | 4,850,000.00 USD | 4,850,000.00 USD | 123,230.00 USD | 15,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1569` | 1,730,000.00 USD | 1,730,000.00 USD | 24,170.00 USD | 0.00 USD | 107,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1570` | 4,710,000.00 USD | 4,710,000.00 USD | 134,890.00 USD | 5,100.00 USD | 210,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1571` | 1,600,000.00 USD | 1,600,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1573` | 1,480,000.00 USD | 1,480,000.00 USD | 24,010.00 USD | 3,460.00 USD | 32,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1573` | 4,360,000.00 USD | 4,360,000.00 USD | 191,190.00 USD | 64,570.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1575` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1576` | 4,070,000.00 USD | 4,070,000.00 USD | 26,600.00 USD | 108,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1577` | 1,410,000.00 USD | 1,410,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1579` | 1,340,000.00 USD | 1,340,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1579` | 3,940,000.00 USD | 3,940,000.00 USD | 197,810.00 USD | 80,390.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1581` | 1,310,000.00 USD | 1,310,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1582` | 3,650,000.00 USD | 3,650,000.00 USD | 56,130.00 USD | 17,610.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1583` | 1,280,000.00 USD | 1,280,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1585` | 1,140,000.00 USD | 1,140,000.00 USD | 21,920.00 USD | 20,720.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1585` | 3,540,000.00 USD | 3,540,000.00 USD | 87,110.00 USD | 0.00 USD | 23,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1587` | 1,090,000.00 USD | 1,090,000.00 USD | 50,950.00 USD | 19,830.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1588` | 3,430,000.00 USD | 3,430,000.00 USD | 74,200.00 USD | 0.00 USD | 89,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1589` | 973,550.00 USD | 973,550.00 USD | 20,380.00 USD | 6,150.00 USD | 44,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1591` | 902,160.00 USD | 902,160.00 USD | 20,460.00 USD | 21,570.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1591` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 12,590.00 USD | 16,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1593` | 817,590.00 USD | 817,590.00 USD | 14,950.00 USD | 38,970.00 USD | 45,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1594` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 29,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1595` | 718,200.00 USD | 718,200.00 USD | 10,260.00 USD | 14,420.00 USD | 7,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1597` | 686,170.00 USD | 686,170.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1597` | 3,210,000.00 USD | 3,210,000.00 USD | 0.00 USD | 96,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1599` | 668,360.00 USD | 668,360.00 USD | 7,070.00 USD | 7,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1600` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 38,830.00 USD | 75,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1601` | 653,710.00 USD | 653,710.00 USD | 21,340.00 USD | 2,310.00 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1603` | 625,390.00 USD | 625,390.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1603` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 58,120.00 USD | 116,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1605` | 582,890.00 USD | 582,890.00 USD | 24,530.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1606` | 2,820,000.00 USD | 2,820,000.00 USD | 237,510.00 USD | 0.00 USD | 376,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1607` | 522,230.00 USD | 522,230.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1609` | 499,730.00 USD | 499,730.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1609` | 2,210,000.00 USD | 2,210,000.00 USD | 117,480.00 USD | 11,640.00 USD | 296,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1611` | 351,700.00 USD | 351,700.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1612` | 1,780,000.00 USD | 1,780,000.00 USD | 304,890.00 USD | 10,980.00 USD | 254,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1613` | 176,150.00 USD | 176,150.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1615` | 112,780.00 USD | 112,780.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1615` | 1,210,000.00 USD | 1,210,000.00 USD | 293,210.00 USD | 35,210.00 USD | 243,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1617` | 96,350.00 USD | 96,350.00 USD | 0.00 USD | 3,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1618` | 638,790.00 USD | 638,790.00 USD | 0.00 USD | 0.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1619` | 92,790.00 USD | 92,790.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1621` | 43,910.00 USD | 43,910.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1621` | 591,200.00 USD | 591,200.00 USD | 78,750.00 USD | 57,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1624` | 455,150.00 USD | 455,150.00 USD | 0.00 USD | 170,670.00 USD | 33,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1625` | 38,240.00 USD | 38,240.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1627` | 251,040.00 USD | 251,040.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1630` | 70,940.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1649` | 16,600.00 USD | 16,600.00 USD | 11,310.00 USD | 3,450.00 USD | 1,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1651` | 41,460.00 USD | 41,460.00 USD | 24,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1653` | 64,690.00 USD | 64,690.00 USD | 17,080.00 USD | 0.00 USD | 6,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1655` | 76,710.00 USD | 76,710.00 USD | 5,090.00 USD | 2,360.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1657` | 91,660.00 USD | 91,660.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1659` | 113,040.00 USD | 113,040.00 USD | 0.00 USD | 6,040.00 USD | 15,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1660` | 97,610.00 USD | 97,610.00 USD | 68,280.00 USD | 29,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1661` | 130,100.00 USD | 130,100.00 USD | 0.00 USD | 13,210.00 USD | 3,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1663` | 211,190.00 USD | 211,190.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1663` | 247,680.00 USD | 247,680.00 USD | 121,520.00 USD | 0.00 USD | 28,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1665` | 255,600.00 USD | 255,600.00 USD | 7,070.00 USD | 3,710.00 USD | 33,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1666` | 338,750.00 USD | 338,750.00 USD | 49,590.00 USD | 12,670.00 USD | 28,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1667` | 302,170.00 USD | 302,170.00 USD | 21,340.00 USD | 5,340.00 USD | 19,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1669` | 329,930.00 USD | 329,930.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1669` | 583,020.00 USD | 583,020.00 USD | 76,120.00 USD | 81,000.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1671` | 399,990.00 USD | 399,990.00 USD | 33,930.00 USD | 0.00 USD | 36,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1672` | 786,760.00 USD | 786,760.00 USD | 96,910.00 USD | 38,070.00 USD | 68,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1673` | 484,240.00 USD | 484,240.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1675` | 517,530.00 USD | 517,530.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1675` | 981,350.00 USD | 981,350.00 USD | 64,490.00 USD | 130,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1675` | 4,640.00 USD | 4,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1677` | 707,690.00 USD | 707,690.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1678` | 1,160,000.00 USD | 1,160,000.00 USD | 71,860.00 USD | 90,910.00 USD | 16,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1679` | 765,350.00 USD | 765,350.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1681` | 918,420.00 USD | 918,420.00 USD | 94,350.00 USD | 36,530.00 USD | 22,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1681` | 1,430,000.00 USD | 1,430,000.00 USD | 69,520.00 USD | 71,610.00 USD | 128,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1683` | 1,040,000.00 USD | 1,040,000.00 USD | 61,280.00 USD | 12,810.00 USD | 49,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1684` | 1,550,000.00 USD | 1,550,000.00 USD | 60,960.00 USD | 14,000.00 USD | 47,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1685` | 1,180,000.00 USD | 1,180,000.00 USD | 41,190.00 USD | 48,480.00 USD | 52,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1687` | 1,280,000.00 USD | 1,280,000.00 USD | 6,960.00 USD | 9,500.00 USD | 74,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1687` | 1,650,000.00 USD | 1,650,000.00 USD | 78,750.00 USD | 0.00 USD | 14,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1689` | 1,380,000.00 USD | 1,380,000.00 USD | 54,040.00 USD | 26,970.00 USD | 23,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1690` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 63,850.00 USD | 74,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1691` | 1,630,000.00 USD | 1,630,000.00 USD | 69,010.00 USD | 72,070.00 USD | 108,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1693` | 1,780,000.00 USD | 1,780,000.00 USD | 57,220.00 USD | 35,730.00 USD | 61,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1693` | 1,910,000.00 USD | 1,910,000.00 USD | 33,660.00 USD | 46,740.00 USD | 42,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1695` | 1,840,000.00 USD | 1,840,000.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1695` | 10,590.00 USD | 15,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1696` | 2,040,000.00 USD | 2,040,000.00 USD | 17,360.00 USD | 87,350.00 USD | 28,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1697` | 1,900,000.00 USD | 1,900,000.00 USD | 27,270.00 USD | 37,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1699` | 2,000,000.00 USD | 2,000,000.00 USD | 24,020.00 USD | 22,050.00 USD | 51,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1699` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1701` | 2,040,000.00 USD | 2,040,000.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1702` | 2,280,000.00 USD | 2,280,000.00 USD | 68,360.00 USD | 55,360.00 USD | 72,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1703` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1705` | 2,130,000.00 USD | 2,130,000.00 USD | 35,700.00 USD | 6,390.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1705` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 34,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1705` | 448.16 USD | 15,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1707` | 2,270,000.00 USD | 2,270,000.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1708` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 31,310.00 USD | 87,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1709` | 2,350,000.00 USD | 2,350,000.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1711` | 2,390,000.00 USD | 2,390,000.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1711` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 5,490.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1713` | 2,420,000.00 USD | 2,420,000.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1714` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 59,620.00 USD | 38,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1715` | 2,500,000.00 USD | 2,500,000.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1715` | 3,220.00 USD | 18,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1717` | 2,540,000.00 USD | 2,540,000.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1717` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 38,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1719` | 2,610,000.00 USD | 2,610,000.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1720` | 2,790,000.00 USD | 2,790,000.00 USD | 39,370.00 USD | 0.00 USD | 161,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1721` | 2,730,000.00 USD | 2,730,000.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1723` | 2,820,000.00 USD | 2,820,000.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1723` | 3,140,000.00 USD | 3,140,000.00 USD | 118,060.00 USD | 12,590.00 USD | 225,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1725` | 2,880,000.00 USD | 2,880,000.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1727` | 2,900,000.00 USD | 2,900,000.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1729` | 2,910,000.00 USD | 2,910,000.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1729` | 3,260,000.00 USD | 3,260,000.00 USD | 120,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1732` | 3,600,000.00 USD | 3,600,000.00 USD | 324,890.00 USD | 0.00 USD | 9,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1733` | 2,930,000.00 USD | 2,930,000.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1735` | 2,960,000.00 USD | 2,960,000.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1737` | 2,990,000.00 USD | 2,990,000.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1738` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1739` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 2,270.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1741` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1743` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1744` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1745` | 3,020,000.00 USD | 3,020,000.00 USD | 3,500.00 USD | 2,460.00 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1747` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1749` | 3,140,000.00 USD | 3,140,000.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1750` | 3,900,000.00 USD | 3,900,000.00 USD | 69,520.00 USD | 0.00 USD | 120,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1751` | 3,170,000.00 USD | 3,170,000.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1753` | 3,200,000.00 USD | 3,200,000.00 USD | 17,770.00 USD | 0.00 USD | 11,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1753` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 197,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1755` | 3,250,000.00 USD | 3,250,000.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1755` | 753.16 USD | 19,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1756` | 4,260,000.00 USD | 4,260,000.00 USD | 112,930.00 USD | 0.00 USD | 53,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1757` | 3,320,000.00 USD | 3,320,000.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1759` | 3,370,000.00 USD | 3,370,000.00 USD | 40,430.00 USD | 7,040.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1759` | 4,500,000.00 USD | 4,500,000.00 USD | 200,480.00 USD | 38,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1761` | 3,510,000.00 USD | 3,510,000.00 USD | 33,150.00 USD | 66,160.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1762` | 4,750,000.00 USD | 4,750,000.00 USD | 117,200.00 USD | 94,740.00 USD | 32,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1763` | 3,570,000.00 USD | 3,570,000.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1765` | 3,640,000.00 USD | 3,640,000.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1765` | 5,050,000.00 USD | 5,050,000.00 USD | 154,540.00 USD | 97,630.00 USD | 48,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1767` | 3,740,000.00 USD | 3,740,000.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1768` | 5,330,000.00 USD | 5,330,000.00 USD | 161,560.00 USD | 92,440.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1769` | 3,830,000.00 USD | 3,830,000.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1771` | 3,850,000.00 USD | 3,850,000.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1771` | 5,500,000.00 USD | 5,500,000.00 USD | 69,030.00 USD | 83,790.00 USD | 21,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1773` | 3,900,000.00 USD | 3,900,000.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1774` | 5,730,000.00 USD | 5,730,000.00 USD | 148,780.00 USD | 85,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1775` | 3,930,000.00 USD | 3,930,000.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1777` | 4,050,000.00 USD | 4,050,000.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1777` | 5,900,000.00 USD | 5,900,000.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1779` | 4,070,000.00 USD | 4,070,000.00 USD | 7,310.00 USD | 9,400.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1780` | 6,040,000.00 USD | 6,040,000.00 USD | 52,730.00 USD | 38,910.00 USD | 46,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1781` | 4,080,000.00 USD | 4,080,000.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1783` | 4,140,000.00 USD | 4,140,000.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1783` | 6,240,000.00 USD | 6,240,000.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1785` | 4,190,000.00 USD | 4,190,000.00 USD | 12,390.00 USD | 27,370.00 USD | 5,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1785` | 138.82 USD | 19,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1786` | 6,430,000.00 USD | 6,430,000.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1787` | 4,220,000.00 USD | 4,220,000.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1789` | 4,230,000.00 USD | 4,230,000.00 USD | 9,350.00 USD | 1,210.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1789` | 6,490,000.00 USD | 6,490,000.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1791` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 2,640.00 USD | 5,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1792` | 6,670,000.00 USD | 6,670,000.00 USD | 134,000.00 USD | 43,520.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1793` | 4,260,000.00 USD | 4,260,000.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1795` | 4,320,000.00 USD | 4,320,000.00 USD | 17,710.00 USD | 33,080.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1795` | 6,750,000.00 USD | 6,750,000.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1795` | 131.88 USD | 19,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1797` | 4,350,000.00 USD | 4,350,000.00 USD | 10,870.00 USD | 4,390.00 USD | 9,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1798` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1799` | 4,370,000.00 USD | 4,370,000.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1801` | 4,410,000.00 USD | 4,410,000.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1801` | 6,910,000.00 USD | 6,910,000.00 USD | 19,430.00 USD | 43,480.00 USD | 55,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1803` | 4,430,000.00 USD | 4,430,000.00 USD | 3,990.00 USD | 10,580.00 USD | 14,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1804` | 6,990,000.00 USD | 6,990,000.00 USD | 28,790.00 USD | 27,450.00 USD | 25,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1805` | 4,450,000.00 USD | 4,450,000.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1805` | 3,640.00 USD | 23,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1807` | 4,480,000.00 USD | 4,480,000.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1807` | 7,130,000.00 USD | 7,130,000.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1809` | 4,490,000.00 USD | 4,490,000.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1810` | 4,510,000.00 USD | 4,510,000.00 USD | 9,360.00 USD | 3,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1810` | 7,250,000.00 USD | 7,250,000.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1813` | 7,370,000.00 USD | 7,370,000.00 USD | 32,530.00 USD | 15,780.00 USD | 67,760.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1815` | 23,550.00 USD | 47,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1816` | 7,470,000.00 USD | 7,470,000.00 USD | 46,430.00 USD | 21,200.00 USD | 35,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1819` | 7,590,000.00 USD | 7,590,000.00 USD | 52,150.00 USD | 24,720.00 USD | 43,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1822` | 7,700,000.00 USD | 7,700,000.00 USD | 46,760.00 USD | 29,530.00 USD | 37,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1825` | 7,780,000.00 USD | 7,780,000.00 USD | 38,800.00 USD | 17,120.00 USD | 20,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1828` | 7,840,000.00 USD | 7,840,000.00 USD | 29,430.00 USD | 13,380.00 USD | 17,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1831` | 7,940,000.00 USD | 7,940,000.00 USD | 63,190.00 USD | 9,610.00 USD | 24,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1834` | 7,970,000.00 USD | 7,970,000.00 USD | 18,400.00 USD | 0.00 USD | 15,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1837` | 8,080,000.00 USD | 8,080,000.00 USD | 11,490.00 USD | 13,450.00 USD | 83,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1840` | 8,230,000.00 USD | 8,230,000.00 USD | 70,360.00 USD | 18,020.00 USD | 65,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1843` | 8,280,000.00 USD | 8,280,000.00 USD | 17,340.00 USD | 3,040.00 USD | 28,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1845` | 4,860.00 USD | 51,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.1846` | 8,340,000.00 USD | 8,340,000.00 USD | 8,330.00 USD | 10,850.00 USD | 42,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.1848` | 8,420,000.00 USD | 8,420,000.00 USD | 35,280.00 USD | 35,270.00 USD | 5,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1855` | 616.01 USD | 52,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1875` | 893.89 USD | 53,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1945` | 802.74 USD | 54,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.1975` | 150.10 USD | 54,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2055` | 11,590.00 USD | 66,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2065` | 41,600.00 USD | 107,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2075` | 257.20 USD | 107,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2085` | 474.40 USD | 108,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2095` | 164.23 USD | 108,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2135` | 15,690.00 USD | 124,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2155` | 42,650.00 USD | 166,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2175` | 213.22 USD | 167,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2195` | 88,150.00 USD | 255,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2235` | 114.52 USD | 255,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2255` | 154.78 USD | 255,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 6,980.00 USD | 262,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 15,930.00 USD | 278,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2375` | 102.62 USD | 278,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 21,020.00 USD | 299,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 796.25 USD | 300,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2455` | 231.97 USD | 300,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 1,560.00 USD | 302,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2545` | 546.54 USD | 302,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2565` | 3,870.00 USD | 306,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2575` | 26,570.00 USD | 333,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 54,960.00 USD | 388,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 154.94 USD | 388,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2685` | 226.51 USD | 388,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2705` | 11,880.00 USD | 400,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 13,240.00 USD | 413,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2725` | 214.21 USD | 413,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2745` | 11,600.00 USD | 425,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2795` | 482.84 USD | 425,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,160.00 USD | 428,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2905` | 3,520.00 USD | 431,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 187.26 USD | 431,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2925` | 794.52 USD | 432,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2985` | 1,890.00 USD | 434,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2995` | 288,660.00 USD | 723,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 6,890.00 USD | 729,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3085` | 363.72 USD | 730,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 11,930.00 USD | 742,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 640.88 USD | 742,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 1,530.00 USD | 744,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 473.81 USD | 744,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0385` | 1,820,000.00 USD | 0.00 USD | 1,490.00 USD | `-76.51%` | `38,823,900,000,000.00` |
| `Live` | `Long` | `0.0415` | 1,820,000.00 USD | 0.00 USD | 110.22 USD | `-74.68%` | `2,655,800,000,000.00` |
| `Live` | `Long` | `0.0425` | 1,820,000.00 USD | 0.00 USD | 4,420.00 USD | `-74.07%` | `104,000,000,000,000.00` |
| `Live` | `Long` | `0.0455` | 1,820,000.00 USD | 0.00 USD | 1,560.00 USD | `-72.24%` | `34,249,500,000,000.00` |
| `Live` | `Long` | `0.0475` | 1,820,000.00 USD | 0.00 USD | 121.77 USD | `-71.02%` | `2,563,600,000,000.00` |
| `Live` | `Long` | `0.0485` | 1,820,000.00 USD | 0.00 USD | 107.79 USD | `-70.41%` | `2,222,400,000,000.00` |
| `Live` | `Long` | `0.0495` | 1,820,000.00 USD | 0.00 USD | 109.52 USD | `-69.79%` | `2,212,600,000,000.00` |
| `Live` | `Long` | `0.0505` | 1,820,000.00 USD | 0.00 USD | 610.70 USD | `-69.18%` | `12,093,000,000,000.00` |
| `Live` | `Long` | `0.0515` | 1,820,000.00 USD | 0.00 USD | 1,030.00 USD | `-68.57%` | `20,000,000,000,000.00` |
| `Live` | `Long` | `0.0525` | 1,810,000.00 USD | 0.00 USD | 289.43 USD | `-67.96%` | `5,513,000,000,000.00` |
| `Live` | `Long` | `0.0535` | 1,810,000.00 USD | 0.00 USD | 479.20 USD | `-67.35%` | `8,957,000,000,000.00` |
| `Live` | `Long` | `0.0545` | 1,810,000.00 USD | 0.00 USD | 2,270.00 USD | `-66.74%` | `41,635,000,000,000.00` |
| `Live` | `Long` | `0.0565` | 1,810,000.00 USD | 0.00 USD | 16,360.00 USD | `-65.52%` | `289,477,000,000,000.00` |
| `Live` | `Long` | `0.0585` | 1,800,000.00 USD | 0.00 USD | 1,100.00 USD | `-64.30%` | `18,731,100,000,000.00` |
| `Live` | `Long` | `0.0615` | 1,790,000.00 USD | 0.00 USD | 186.63 USD | `-62.47%` | `3,034,600,000,000.00` |
| `Live` | `Long` | `0.0625` | 1,790,000.00 USD | 0.00 USD | 219,780.00 USD | `-61.86%` | `3,516,409,800,000,000.00` |
| `Live` | `Long` | `0.0635` | 1,570,000.00 USD | 0.00 USD | 6,470.00 USD | `-61.25%` | `101,831,000,000,000.00` |
| `Live` | `Long` | `0.0675` | 1,570,000.00 USD | 0.00 USD | 104,180.00 USD | `-58.81%` | `1,543,385,900,000,000.00` |
| `Live` | `Long` | `0.0685` | 1,460,000.00 USD | 0.00 USD | 313.22 USD | `-58.20%` | `4,572,600,000,000.00` |
| `Live` | `Long` | `0.0695` | 1,460,000.00 USD | 0.00 USD | 976.14 USD | `-57.59%` | `14,045,200,000,000.00` |
| `Live` | `Long` | `0.0705` | 1,460,000.00 USD | 0.00 USD | 3,280.00 USD | `-56.98%` | `46,532,700,000,000.00` |
| `Live` | `Long` | `0.0715` | 1,460,000.00 USD | 0.00 USD | 6,070.00 USD | `-56.37%` | `84,893,500,000,000.00` |
| `Live` | `Long` | `0.0725` | 1,450,000.00 USD | 0.00 USD | 61,160.00 USD | `-55.76%` | `843,610,100,000,000.00` |
| `Live` | `Long` | `0.0735` | 1,390,000.00 USD | 0.00 USD | 2,440.00 USD | `-55.15%` | `33,161,800,000,000.00` |
| `Live` | `Long` | `0.0745` | 1,390,000.00 USD | 0.00 USD | 226.17 USD | `-54.54%` | `3,035,900,000,000.00` |
| `Live` | `Long` | `0.0765` | 1,390,000.00 USD | 0.00 USD | 14,690.00 USD | `-53.32%` | `192,029,300,000,000.00` |
| `Live` | `Long` | `0.0795` | 1,370,000.00 USD | 0.00 USD | 4,630.00 USD | `-51.49%` | `58,261,800,000,000.00` |
| `Live` | `Long` | `0.0825` | 1,370,000.00 USD | 0.00 USD | 18,860.00 USD | `-49.66%` | `228,584,300,000,000.00` |
| `Live` | `Long` | `0.0865` | 1,350,000.00 USD | 0.00 USD | 21,410.00 USD | `-47.22%` | `247,561,200,000,000.00` |
| `Live` | `Long` | `0.0875` | 1,330,000.00 USD | 0.00 USD | 4,830.00 USD | `-46.61%` | `55,220,200,000,000.00` |
| `Live` | `Long` | `0.0885` | 1,320,000.00 USD | 0.00 USD | 3,030.00 USD | `-46.00%` | `34,269,700,000,000.00` |
| `Live` | `Long` | `0.0895` | 1,320,000.00 USD | 0.00 USD | 364.11 USD | `-45.39%` | `4,068,300,000,000.00` |
| `Live` | `Long` | `0.0915` | 1,320,000.00 USD | 0.00 USD | 113.80 USD | `-44.17%` | `1,243,700,000,000.00` |
| `Live` | `Long` | `0.0925` | 1,320,000.00 USD | 0.00 USD | 2,410.00 USD | `-43.56%` | `26,091,400,000,000.00` |
| `Live` | `Long` | `0.0935` | 1,320,000.00 USD | 0.00 USD | 2,680.00 USD | `-42.95%` | `28,708,500,000,000.00` |
| `Live` | `Long` | `0.0945` | 1,320,000.00 USD | 0.00 USD | 1,510.00 USD | `-42.34%` | `16,031,700,000,000.00` |
| `Live` | `Long` | `0.0965` | 1,310,000.00 USD | 0.00 USD | 10,890.00 USD | `-41.12%` | `112,820,000,000,000.00` |
| `Live` | `Long` | `0.0975` | 1,300,000.00 USD | 0.00 USD | 589.74 USD | `-40.51%` | `6,048,600,000,000.00` |
| `Live` | `Long` | `0.0985` | 1,300,000.00 USD | 0.00 USD | 3,540.00 USD | `-39.90%` | `35,986,600,000,000.00` |
| `Live` | `Long` | `0.0995` | 1,300,000.00 USD | 0.00 USD | 7,670.00 USD | `-39.28%` | `77,071,300,000,000.00` |
| `Live` | `Long` | `0.1005` | 1,290,000.00 USD | 0.00 USD | 10,640.00 USD | `-38.67%` | `105,855,400,000,000.00` |
| `Live` | `Long` | `0.1025` | 1,280,000.00 USD | 0.00 USD | 3,570.00 USD | `-37.45%` | `34,875,900,000,000.00` |
| `Live` | `Long` | `0.1035` | 1,280,000.00 USD | 0.00 USD | 5,700.00 USD | `-36.84%` | `55,107,400,000,000.00` |
| `Live` | `Long` | `0.1045` | 1,270,000.00 USD | 0.00 USD | 6,500.00 USD | `-36.23%` | `62,191,700,000,000.00` |
| `Live` | `Long` | `0.1055` | 1,270,000.00 USD | 0.00 USD | 8,930.00 USD | `-35.62%` | `84,682,700,000,000.00` |
| `Live` | `Long` | `0.1065` | 1,260,000.00 USD | 0.00 USD | 181.20 USD | `-35.01%` | `1,701,400,000,000.00` |
| `Live` | `Long` | `0.1075` | 1,260,000.00 USD | 0.00 USD | 1,060.00 USD | `-34.40%` | `9,856,300,000,000.00` |
| `Live` | `Long` | `0.1085` | 1,260,000.00 USD | 0.00 USD | 11,210.00 USD | `-33.79%` | `103,322,500,000,000.00` |
| `Live` | `Long` | `0.1105` | 1,240,000.00 USD | 0.00 USD | 14,360.00 USD | `-32.57%` | `129,913,800,000,000.00` |
| `Live` | `Long` | `0.1115` | 1,230,000.00 USD | 0.00 USD | 425.50 USD | `-31.96%` | `3,816,100,000,000.00` |
| `Live` | `Long` | `0.1125` | 1,230,000.00 USD | 0.00 USD | 368.45 USD | `-31.35%` | `3,275,100,000,000.00` |
| `Live` | `Long` | `0.1135` | 1,230,000.00 USD | 0.00 USD | 281.48 USD | `-30.74%` | `2,480,000,000,000.00` |
| `Live` | `Long` | `0.1145` | 1,230,000.00 USD | 0.00 USD | 8,950.00 USD | `-30.13%` | `78,144,100,000,000.00` |
| `Live` | `Long` | `0.1155` | 1,220,000.00 USD | 0.00 USD | 7,630.00 USD | `-29.52%` | `66,029,500,000,000.00` |
| `Live` | `Long` | `0.1175` | 1,210,000.00 USD | 0.00 USD | 129,500.00 USD | `-28.30%` | `1,102,087,700,000,000.00` |
| `Live` | `Long` | `0.1185` | 1,080,000.00 USD | 0.00 USD | 25,800.00 USD | `-27.69%` | `217,694,900,000,000.00` |
| `Live` | `Long` | `0.1195` | 1,060,000.00 USD | 0.00 USD | 3,150.00 USD | `-27.08%` | `26,345,100,000,000.00` |
| `Live` | `Long` | `0.1215` | 1,050,000.00 USD | 0.00 USD | 1,730.00 USD | `-25.86%` | `14,200,000,000,000.00` |
| `Live` | `Long` | `0.1225` | 1,050,000.00 USD | 0.00 USD | 19,560.00 USD | `-25.25%` | `159,692,100,000,000.00` |
| `Live` | `Long` | `0.1235` | 1,030,000.00 USD | 0.00 USD | 50,430.00 USD | `-24.64%` | `408,338,300,000,000.00` |
| `Live` | `Long` | `0.1245` | 982,210.00 USD | 0.00 USD | 377.05 USD | `-24.03%` | `3,028,500,000,000.00` |
| `Live` | `Long` | `0.1255` | 981,830.00 USD | 0.00 USD | 134.66 USD | `-23.42%` | `1,073,000,000,000.00` |
| `Live` | `Long` | `0.1265` | 981,700.00 USD | 0.00 USD | 16,720.00 USD | `-22.81%` | `132,151,600,000,000.00` |
| `Live` | `Long` | `0.1275` | 964,980.00 USD | 0.00 USD | 10,250.00 USD | `-22.20%` | `80,425,800,000,000.00` |
| `Live` | `Long` | `0.1285` | 954,730.00 USD | 0.00 USD | 645.03 USD | `-21.59%` | `5,019,700,000,000.00` |
| `Live` | `Long` | `0.1295` | 954,080.00 USD | 0.00 USD | 3,330.00 USD | `-20.98%` | `25,720,700,000,000.00` |
| `Live` | `Long` | `0.1305` | 950,750.00 USD | 0.00 USD | 32,320.00 USD | `-20.37%` | `247,690,000,000,000.00` |
| `Live` | `Long` | `0.1315` | 918,430.00 USD | 0.00 USD | 14,350.00 USD | `-19.76%` | `109,117,100,000,000.00` |
| `Live` | `Long` | `0.1325` | 904,080.00 USD | 0.00 USD | 4,640.00 USD | `-19.15%` | `35,013,800,000,000.00` |
| `Live` | `Long` | `0.1335` | 899,440.00 USD | 0.00 USD | 51,860.00 USD | `-18.54%` | `388,489,900,000,000.00` |
| `Live` | `Long` | `0.1345` | 847,570.00 USD | 0.00 USD | 28,900.00 USD | `-17.93%` | `214,903,400,000,000.00` |
| `Live` | `Long` | `0.1355` | 818,670.00 USD | 0.00 USD | 8,620.00 USD | `-17.32%` | `63,632,100,000,000.00` |
| `Live` | `Long` | `0.1365` | 810,050.00 USD | 0.00 USD | 8,320.00 USD | `-16.71%` | `60,965,900,000,000.00` |
| `Live` | `Long` | `0.1375` | 801,730.00 USD | 0.00 USD | 25,370.00 USD | `-16.10%` | `184,514,800,000,000.00` |
| `Live` | `Long` | `0.1385` | 776,350.00 USD | 0.00 USD | 4,330.00 USD | `-15.49%` | `31,259,100,000,000.00` |
| `Live` | `Long` | `0.1395` | 772,030.00 USD | 0.00 USD | 9,210.00 USD | `-14.88%` | `66,000,700,000,000.00` |
| `Live` | `Long` | `0.1405` | 762,820.00 USD | 0.00 USD | 2,640.00 USD | `-14.27%` | `18,781,700,000,000.00` |
| `Live` | `Long` | `0.1415` | 760,180.00 USD | 0.00 USD | 493,500.00 USD | `-13.66%` | `3,487,642,600,000,000.00` |
| `Live` | `Long` | `0.1425` | 266,680.00 USD | 0.00 USD | 22,060.00 USD | `-13.05%` | `154,773,800,000,000.00` |
| `Live` | `Long` | `0.1435` | 244,620.00 USD | 0.00 USD | 18,970.00 USD | `-12.44%` | `132,163,100,000,000.00` |
| `Live` | `Long` | `0.1445` | 225,660.00 USD | 0.00 USD | 9,510.00 USD | `-11.83%` | `65,841,200,000,000.00` |
| `Live` | `Long` | `0.1455` | 216,140.00 USD | 0.00 USD | 92,080.00 USD | `-11.22%` | `632,843,200,000,000.00` |
| `Live` | `Long` | `0.1465` | 124,060.00 USD | 0.00 USD | 23,540.00 USD | `-10.61%` | `160,700,100,000,000.00` |
| `Live` | `Long` | `0.1475` | 100,520.00 USD | 0.00 USD | 82,910.00 USD | `-10.00%` | `562,123,800,000,000.06` |
| `Live` | `Long` | `0.1485` | 17,610.00 USD | 0.00 USD | 2,290.00 USD | `-9.38%` | `15,410,500,000,000.00` |
| `Live` | `Long` | `0.1495` | 15,320.00 USD | 0.00 USD | 937.17 USD | `-8.77%` | `6,268,700,000,000.00` |
| `Live` | `Long` | `0.1545` | 14,380.00 USD | 0.00 USD | 2,550.00 USD | `-5.72%` | `16,500,600,000,000.00` |
| `Live` | `Long` | `0.1555` | 11,830.00 USD | 0.00 USD | 2,170.00 USD | `-5.11%` | `13,965,000,000,000.00` |
| `Live` | `Long` | `0.1565` | 9,660.00 USD | 0.00 USD | 9,660.00 USD | `-4.50%` | `61,740,200,000,000.00` |
| `Live` | `Short` | `0.1675` | 4,640.00 USD | 4,640.00 USD | 0.00 USD | `+2.21%` | `27,726,400,000,000.00` |
| `Live` | `Short` | `0.1695` | 15,230.00 USD | 10,590.00 USD | 0.00 USD | `+3.43%` | `62,475,700,000,000.00` |
| `Live` | `Short` | `0.1705` | 15,680.00 USD | 448.16 USD | 0.00 USD | `+4.04%` | `2,628,500,000,000.00` |
| `Live` | `Short` | `0.1715` | 18,910.00 USD | 3,220.00 USD | 0.00 USD | `+4.65%` | `18,797,800,000,000.00` |
| `Live` | `Short` | `0.1755` | 19,660.00 USD | 753.16 USD | 0.00 USD | `+7.09%` | `4,291,500,000,000.00` |
| `Live` | `Short` | `0.1785` | 19,800.00 USD | 138.82 USD | 0.00 USD | `+8.92%` | `777,700,000,000.00` |
| `Live` | `Short` | `0.1795` | 19,930.00 USD | 131.88 USD | 0.00 USD | `+9.53%` | `734,700,000,000.00` |
| `Live` | `Short` | `0.1805` | 23,570.00 USD | 3,640.00 USD | 0.00 USD | `+10.14%` | `20,150,900,000,000.00` |
| `Live` | `Short` | `0.1815` | 47,120.00 USD | 23,550.00 USD | 0.00 USD | `+10.75%` | `129,749,200,000,000.00` |
| `Live` | `Short` | `0.1845` | 51,980.00 USD | 4,860.00 USD | 0.00 USD | `+12.58%` | `26,350,500,000,000.00` |
| `Live` | `Short` | `0.1855` | 52,590.00 USD | 616.01 USD | 0.00 USD | `+13.19%` | `3,320,800,000,000.00` |
| `Live` | `Short` | `0.1875` | 53,490.00 USD | 893.89 USD | 0.00 USD | `+14.41%` | `4,767,400,000,000.00` |
| `Live` | `Short` | `0.1945` | 54,290.00 USD | 802.74 USD | 0.00 USD | `+18.68%` | `4,127,200,000,000.00` |
| `Live` | `Short` | `0.1975` | 54,440.00 USD | 150.10 USD | 0.00 USD | `+20.52%` | `760,000,000,000.00` |
| `Live` | `Short` | `0.2055` | 66,030.00 USD | 11,590.00 USD | 0.00 USD | `+25.40%` | `56,409,600,000,000.00` |
| `Live` | `Short` | `0.2065` | 107,640.00 USD | 41,600.00 USD | 0.00 USD | `+26.01%` | `201,472,400,000,000.00` |
| `Live` | `Short` | `0.2075` | 107,890.00 USD | 257.20 USD | 0.00 USD | `+26.62%` | `1,239,500,000,000.00` |
| `Live` | `Short` | `0.2085` | 108,370.00 USD | 474.40 USD | 0.00 USD | `+27.23%` | `2,275,300,000,000.00` |
| `Live` | `Short` | `0.2095` | 108,530.00 USD | 164.23 USD | 0.00 USD | `+27.84%` | `783,900,000,000.00` |
| `Live` | `Short` | `0.2135` | 124,230.00 USD | 15,690.00 USD | 0.00 USD | `+30.28%` | `73,505,600,000,000.00` |
| `Live` | `Short` | `0.2155` | 166,870.00 USD | 42,650.00 USD | 0.00 USD | `+31.50%` | `197,895,300,000,000.00` |
| `Live` | `Short` | `0.2175` | 167,090.00 USD | 213.22 USD | 0.00 USD | `+32.72%` | `980,300,000,000.00` |
| `Live` | `Short` | `0.2195` | 255,240.00 USD | 88,150.00 USD | 0.00 USD | `+33.94%` | `401,602,500,000,000.00` |
| `Live` | `Short` | `0.2235` | 255,350.00 USD | 114.52 USD | 0.00 USD | `+36.38%` | `512,400,000,000.00` |
| `Live` | `Short` | `0.2255` | 255,510.00 USD | 154.78 USD | 0.00 USD | `+37.60%` | `686,400,000,000.00` |
| `Live` | `Short` | `0.2295` | 262,490.00 USD | 6,980.00 USD | 0.00 USD | `+40.04%` | `30,426,900,000,000.00` |
| `Live` | `Short` | `0.2355` | 278,420.00 USD | 15,930.00 USD | 0.00 USD | `+43.70%` | `67,638,800,000,000.00` |
| `Live` | `Short` | `0.2375` | 278,520.00 USD | 102.62 USD | 0.00 USD | `+44.92%` | `432,100,000,000.00` |
| `Live` | `Short` | `0.2395` | 299,540.00 USD | 21,020.00 USD | 0.00 USD | `+46.14%` | `87,750,200,000,000.00` |
| `Live` | `Short` | `0.2425` | 300,330.00 USD | 796.25 USD | 0.00 USD | `+47.97%` | `3,283,500,000,000.00` |
| `Live` | `Short` | `0.2455` | 300,570.00 USD | 231.97 USD | 0.00 USD | `+49.80%` | `944,900,000,000.00` |
| `Live` | `Short` | `0.2525` | 302,130.00 USD | 1,560.00 USD | 0.00 USD | `+54.08%` | `6,184,400,000,000.00` |
| `Live` | `Short` | `0.2545` | 302,670.00 USD | 546.54 USD | 0.00 USD | `+55.30%` | `2,147,500,000,000.00` |
| `Live` | `Short` | `0.2565` | 306,540.00 USD | 3,870.00 USD | 0.00 USD | `+56.52%` | `15,070,700,000,000.00` |
| `Live` | `Short` | `0.2575` | 333,110.00 USD | 26,570.00 USD | 0.00 USD | `+57.13%` | `103,191,700,000,000.00` |
| `Live` | `Short` | `0.2585` | 388,080.00 USD | 54,960.00 USD | 0.00 USD | `+57.74%` | `212,629,500,000,000.00` |
| `Live` | `Short` | `0.2615` | 388,230.00 USD | 154.94 USD | 0.00 USD | `+59.57%` | `592,500,000,000.00` |
| `Live` | `Short` | `0.2685` | 388,460.00 USD | 226.51 USD | 0.00 USD | `+63.84%` | `843,600,000,000.00` |
| `Live` | `Short` | `0.2705` | 400,330.00 USD | 11,880.00 USD | 0.00 USD | `+65.06%` | `43,905,000,000,000.00` |
| `Live` | `Short` | `0.2715` | 413,580.00 USD | 13,240.00 USD | 0.00 USD | `+65.67%` | `48,778,100,000,000.00` |
| `Live` | `Short` | `0.2725` | 413,790.00 USD | 214.21 USD | 0.00 USD | `+66.28%` | `786,100,000,000.00` |
| `Live` | `Short` | `0.2745` | 425,390.00 USD | 11,600.00 USD | 0.00 USD | `+67.50%` | `42,249,200,000,000.00` |
| `Live` | `Short` | `0.2795` | 425,870.00 USD | 482.84 USD | 0.00 USD | `+70.55%` | `1,727,500,000,000.00` |
| `Live` | `Short` | `0.2845` | 428,040.00 USD | 2,160.00 USD | 0.00 USD | `+73.60%` | `7,608,100,000,000.00` |
| `Live` | `Short` | `0.2905` | 431,550.00 USD | 3,520.00 USD | 0.00 USD | `+77.26%` | `12,106,500,000,000.00` |
| `Live` | `Short` | `0.2915` | 431,740.00 USD | 187.26 USD | 0.00 USD | `+77.87%` | `642,400,000,000.00` |
| `Live` | `Short` | `0.2925` | 432,530.00 USD | 794.52 USD | 0.00 USD | `+78.48%` | `2,716,300,000,000.00` |
| `Live` | `Short` | `0.2985` | 434,420.00 USD | 1,890.00 USD | 0.00 USD | `+82.15%` | `6,328,900,000,000.00` |
| `Live` | `Short` | `0.2995` | 723,080.00 USD | 288,660.00 USD | 0.00 USD | `+82.76%` | `963,809,300,000,000.00` |
| `Live` | `Short` | `0.3075` | 729,970.00 USD | 6,890.00 USD | 0.00 USD | `+87.64%` | `22,398,000,000,000.00` |
| `Live` | `Short` | `0.3085` | 730,340.00 USD | 363.72 USD | 0.00 USD | `+88.25%` | `1,179,000,000,000.00` |
| `Live` | `Short` | `0.3105` | 742,260.00 USD | 11,930.00 USD | 0.00 USD | `+89.47%` | `38,407,000,000,000.00` |
| `Live` | `Short` | `0.3115` | 742,900.00 USD | 640.88 USD | 0.00 USD | `+90.08%` | `2,057,400,000,000.00` |
| `Live` | `Short` | `0.3125` | 744,430.00 USD | 1,530.00 USD | 0.00 USD | `+90.69%` | `4,897,100,000,000.00` |
| `Live` | `Short` | `0.3175` | 744,910.00 USD | 473.81 USD | 0.00 USD | `+93.74%` | `1,492,300,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0355` | 790,400.00 USD | 0.00 USD | 355.00 USD | `-78.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0425` | 790,050.00 USD | 0.00 USD | 297.50 USD | `-74.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0505` | 789,750.00 USD | 0.00 USD | 353.50 USD | `-69.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0545` | 789,400.00 USD | 0.00 USD | 276.53 USD | `-66.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0555` | 789,120.00 USD | 0.00 USD | 4,310.00 USD | `-66.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0635` | 784,810.00 USD | 0.00 USD | 475.11 USD | `-61.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0655` | 784,330.00 USD | 0.00 USD | 131.16 USD | `-60.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0665` | 784,200.00 USD | 0.00 USD | 881.45 USD | `-59.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0675` | 783,320.00 USD | 0.00 USD | 1,070.00 USD | `-58.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0685` | 782,250.00 USD | 0.00 USD | 1,050.00 USD | `-58.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0695` | 781,200.00 USD | 0.00 USD | 1,010.00 USD | `-57.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0705` | 780,190.00 USD | 0.00 USD | 4,100.00 USD | `-56.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0715` | 776,080.00 USD | 0.00 USD | 529.04 USD | `-56.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0725` | 775,560.00 USD | 0.00 USD | 2,390.00 USD | `-55.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0755` | 773,170.00 USD | 0.00 USD | 757.39 USD | `-53.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0785` | 772,410.00 USD | 0.00 USD | 1,490.00 USD | `-52.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0855` | 770,920.00 USD | 0.00 USD | 255.36 USD | `-47.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0865` | 770,670.00 USD | 0.00 USD | 277.37 USD | `-47.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0875` | 770,390.00 USD | 0.00 USD | 262.50 USD | `-46.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0885` | 770,130.00 USD | 0.00 USD | 795.57 USD | `-46.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0905` | 769,330.00 USD | 0.00 USD | 181.00 USD | `-44.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1005` | 769,150.00 USD | 0.00 USD | 3,810.00 USD | `-38.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1025` | 765,340.00 USD | 0.00 USD | 1,550.00 USD | `-37.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1075` | 763,790.00 USD | 0.00 USD | 116.07 USD | `-34.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1085` | 763,680.00 USD | 0.00 USD | 19,070.00 USD | `-33.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 744,600.00 USD | 0.00 USD | 577.22 USD | `-32.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1145` | 744,030.00 USD | 0.00 USD | 343.50 USD | `-30.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1165` | 743,680.00 USD | 0.00 USD | 26,280.00 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 717,400.00 USD | 0.00 USD | 4,870.00 USD | `-26.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1215` | 712,540.00 USD | 0.00 USD | 83,620.00 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1225` | 628,910.00 USD | 0.00 USD | 487.10 USD | `-25.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1245` | 628,420.00 USD | 0.00 USD | 14,940.00 USD | `-24.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1255` | 613,490.00 USD | 0.00 USD | 129,320.00 USD | `-23.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1265` | 484,160.00 USD | 0.00 USD | 2,670.00 USD | `-22.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 481,500.00 USD | 0.00 USD | 473.27 USD | `-22.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1285` | 481,030.00 USD | 0.00 USD | 203,210.00 USD | `-21.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 277,820.00 USD | 0.00 USD | 1,670.00 USD | `-20.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1315` | 276,140.00 USD | 0.00 USD | 1,590.00 USD | `-19.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 274,550.00 USD | 0.00 USD | 6,000.00 USD | `-19.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1335` | 268,550.00 USD | 0.00 USD | 625.78 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 267,920.00 USD | 0.00 USD | 502.28 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1355` | 267,420.00 USD | 0.00 USD | 162.60 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1365` | 267,260.00 USD | 0.00 USD | 700.86 USD | `-16.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 266,560.00 USD | 0.00 USD | 13,710.00 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1385` | 252,840.00 USD | 0.00 USD | 108.57 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1405` | 252,740.00 USD | 0.00 USD | 4,210.00 USD | `-14.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 248,520.00 USD | 0.00 USD | 127.35 USD | `-13.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 248,400.00 USD | 0.00 USD | 24,850.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 223,550.00 USD | 0.00 USD | 1,300.00 USD | `-12.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1445` | 222,250.00 USD | 0.00 USD | 1,960.00 USD | `-11.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 220,290.00 USD | 0.00 USD | 46,010.00 USD | `-11.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1465` | 174,280.00 USD | 0.00 USD | 18,040.00 USD | `-10.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1475` | 156,240.00 USD | 0.00 USD | 2,400.00 USD | `-10.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1485` | 153,840.00 USD | 0.00 USD | 2,610.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 151,230.00 USD | 0.00 USD | 1,540.00 USD | `-8.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 149,680.00 USD | 0.00 USD | 3,010.00 USD | `-8.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 146,670.00 USD | 0.00 USD | 3,430.00 USD | `-7.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 143,240.00 USD | 0.00 USD | 2,990.00 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1535` | 140,250.00 USD | 0.00 USD | 39,990.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 100,260.00 USD | 0.00 USD | 4,060.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 96,210.00 USD | 0.00 USD | 23,220.00 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 72,990.00 USD | 0.00 USD | 19,560.00 USD | `-4.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1575` | 53,430.00 USD | 0.00 USD | 499.16 USD | `-3.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 52,930.00 USD | 0.00 USD | 9,980.00 USD | `-3.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 42,950.00 USD | 0.00 USD | 21,740.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 21,210.00 USD | 0.00 USD | 19,290.00 USD | `-2.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 1,920.00 USD | 0.00 USD | 126.63 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 1,800.00 USD | 0.00 USD | 107.35 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 1,690.00 USD | 0.00 USD | 1,690.00 USD | `-0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1645` | 151.44 USD | 151.44 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1655` | 378.62 USD | 227.18 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1665` | 7,140.00 USD | 6,760.00 USD | 0.00 USD | `+1.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1675` | 9,300.00 USD | 2,160.00 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1685` | 9,800.00 USD | 509.21 USD | 0.00 USD | `+2.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1695` | 9,930.00 USD | 126.35 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1705` | 10,500.00 USD | 564.90 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1715` | 12,300.00 USD | 1,800.00 USD | 0.00 USD | `+4.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1725` | 13,210.00 USD | 918.29 USD | 0.00 USD | `+5.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1735` | 13,350.00 USD | 137.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1745` | 13,980.00 USD | 630.24 USD | 0.00 USD | `+6.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1755` | 15,080.00 USD | 1,100.00 USD | 0.00 USD | `+7.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1765` | 15,870.00 USD | 790.28 USD | 0.00 USD | `+7.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1775` | 16,200.00 USD | 336.40 USD | 0.00 USD | `+8.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1785` | 17,100.00 USD | 898.02 USD | 0.00 USD | `+8.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1795` | 22,130.00 USD | 5,030.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1805` | 33,790.00 USD | 11,660.00 USD | 0.00 USD | `+10.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1815` | 44,640.00 USD | 10,840.00 USD | 0.00 USD | `+10.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1825` | 45,500.00 USD | 864.12 USD | 0.00 USD | `+11.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1835` | 48,020.00 USD | 2,520.00 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1845` | 48,300.00 USD | 276.75 USD | 0.00 USD | `+12.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1855` | 48,430.00 USD | 128.68 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1865` | 51,800.00 USD | 3,370.00 USD | 0.00 USD | `+13.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1875` | 55,500.00 USD | 3,700.00 USD | 0.00 USD | `+14.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1885` | 55,750.00 USD | 245.50 USD | 0.00 USD | `+15.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1895` | 56,280.00 USD | 531.47 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1905` | 56,980.00 USD | 697.34 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 57,200.00 USD | 222.24 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 86,320.00 USD | 29,130.00 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 93,400.00 USD | 7,070.00 USD | 0.00 USD | `+18.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 93,590.00 USD | 194.50 USD | 0.00 USD | `+18.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 93,730.00 USD | 137.77 USD | 0.00 USD | `+19.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 93,860.00 USD | 133.19 USD | 0.00 USD | `+19.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 97,610.00 USD | 3,750.00 USD | 0.00 USD | `+21.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 98,110.00 USD | 492.19 USD | 0.00 USD | `+21.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 120,860.00 USD | 22,750.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 121,420.00 USD | 560.96 USD | 0.00 USD | `+22.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 142,760.00 USD | 21,340.00 USD | 0.00 USD | `+23.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 143,130.00 USD | 371.35 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 229,030.00 USD | 85,900.00 USD | 0.00 USD | `+24.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 230,490.00 USD | 1,470.00 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 230,670.00 USD | 174.20 USD | 0.00 USD | `+26.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 232,740.00 USD | 2,080.00 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 232,990.00 USD | 252.51 USD | 0.00 USD | `+27.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 235,360.00 USD | 2,370.00 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 235,720.00 USD | 356.72 USD | 0.00 USD | `+29.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 236,080.00 USD | 360.08 USD | 0.00 USD | `+30.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 236,440.00 USD | 361.76 USD | 0.00 USD | `+31.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 236,800.00 USD | 363.44 USD | 0.00 USD | `+32.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2175` | 237,170.00 USD | 365.12 USD | 0.00 USD | `+32.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 243,450.00 USD | 6,280.00 USD | 0.00 USD | `+33.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 243,820.00 USD | 368.47 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 266,310.00 USD | 22,490.00 USD | 0.00 USD | `+34.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 266,640.00 USD | 333.91 USD | 0.00 USD | `+35.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 270,620.00 USD | 3,980.00 USD | 0.00 USD | `+36.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 271,000.00 USD | 378.55 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 271,380.00 USD | 380.23 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 275,210.00 USD | 3,840.00 USD | 0.00 USD | `+39.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 305,550.00 USD | 30,340.00 USD | 0.00 USD | `+40.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 309,810.00 USD | 4,260.00 USD | 0.00 USD | `+41.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 311,330.00 USD | 1,520.00 USD | 0.00 USD | `+42.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 332,550.00 USD | 21,230.00 USD | 0.00 USD | `+44.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 335,080.00 USD | 2,530.00 USD | 0.00 USD | `+45.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 343,700.00 USD | 8,620.00 USD | 0.00 USD | `+46.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 353,010.00 USD | 9,300.00 USD | 0.00 USD | `+47.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 354,920.00 USD | 1,910.00 USD | 0.00 USD | `+49.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 374,740.00 USD | 19,820.00 USD | 0.00 USD | `+50.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 375,300.00 USD | 551.23 USD | 0.00 USD | `+51.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 375,690.00 USD | 397.90 USD | 0.00 USD | `+52.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 380,030.00 USD | 4,330.00 USD | 0.00 USD | `+52.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 380,350.00 USD | 320.66 USD | 0.00 USD | `+53.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 396,230.00 USD | 15,880.00 USD | 0.00 USD | `+54.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2545` | 398,230.00 USD | 2,000.00 USD | 0.00 USD | `+55.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2555` | 400,780.00 USD | 2,550.00 USD | 0.00 USD | `+55.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 412,510.00 USD | 11,730.00 USD | 0.00 USD | `+56.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 417,670.00 USD | 5,160.00 USD | 0.00 USD | `+57.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 434,540.00 USD | 16,870.00 USD | 0.00 USD | `+58.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 461,330.00 USD | 26,790.00 USD | 0.00 USD | `+58.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2705` | 461,600.00 USD | 272.88 USD | 0.00 USD | `+65.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2755` | 461,710.00 USD | 114.99 USD | 0.00 USD | `+68.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2765` | 462,110.00 USD | 394.01 USD | 0.00 USD | `+68.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2805` | 462,480.00 USD | 375.53 USD | 0.00 USD | `+71.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2855` | 464,620.00 USD | 2,130.00 USD | 0.00 USD | `+74.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2865` | 465,200.00 USD | 579.27 USD | 0.00 USD | `+74.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 466,950.00 USD | 1,750.00 USD | 0.00 USD | `+77.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2955` | 467,050.00 USD | 101.21 USD | 0.00 USD | `+80.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2965` | 467,310.00 USD | 262.73 USD | 0.00 USD | `+80.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 468,750.00 USD | 1,440.00 USD | 0.00 USD | `+81.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 474,180.00 USD | 5,430.00 USD | 0.00 USD | `+83.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3015` | 479,610.00 USD | 5,430.00 USD | 0.00 USD | `+83.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 479,900.00 USD | 289.61 USD | 0.00 USD | `+86.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3065` | 480,390.00 USD | 487.09 USD | 0.00 USD | `+87.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3095` | 486,960.00 USD | 6,570.00 USD | 0.00 USD | `+88.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 492,130.00 USD | 5,180.00 USD | 0.00 USD | `+91.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3185` | 509,650.00 USD | 17,520.00 USD | 0.00 USD | `+94.35%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1357` | 8,700,000.00 USD | 0.00 USD | 8,700,000.00 USD | 21,410.00 USD | 17,110.00 USD | 11,830.00 USD |
| `7D` | `0.1360` | 8,650,000.00 USD | 0.00 USD | 8,650,000.00 USD | 16,290.00 USD | 3,690.00 USD | 6,320.00 USD |
| `7D` | `0.1363` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 7,890.00 USD | 3,220.00 USD | 4,690.00 USD |
| `7D` | `0.1366` | 8,610,000.00 USD | 0.00 USD | 8,610,000.00 USD | 11,610.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.1369` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 0.00 USD | 1,760.00 USD | 2,530.00 USD |
| `7D` | `0.1372` | 8,590,000.00 USD | 0.00 USD | 8,590,000.00 USD | 4,620.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1375` | 8,580,000.00 USD | 0.00 USD | 8,580,000.00 USD | 0.00 USD | 0.00 USD | 35,720.00 USD |
| `7D` | `0.1378` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 13,860.00 USD | 2,040.00 USD | 0.00 USD |
| `7D` | `0.1384` | 8,530,000.00 USD | 0.00 USD | 8,530,000.00 USD | 11,880.00 USD | 0.00 USD | 30,320.00 USD |
| `7D` | `0.1387` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 17,360.00 USD | 0.00 USD | 11,770.00 USD |
| `7D` | `0.1390` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 4,690.00 USD | 0.00 USD |
| `7D` | `0.1393` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 50,050.00 USD |
| `7D` | `0.1396` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 28,780.00 USD |
| `7D` | `0.1399` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 6,210.00 USD | 4,200.00 USD | 0.00 USD |
| `7D` | `0.1402` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 5,800.00 USD | 3,680.00 USD | 0.00 USD |
| `7D` | `0.1417` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 9,420.00 USD |
| `7D` | `0.1420` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 5,260.00 USD |
| `7D` | `0.1423` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 17,820.00 USD |
| `7D` | `0.1435` | 8,320,000.00 USD | 0.00 USD | 8,320,000.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD |
| `7D` | `0.1438` | 8,300,000.00 USD | 0.00 USD | 8,300,000.00 USD | 29,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1441` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 0.00 USD | 0.00 USD | 6,160.00 USD |
| `7D` | `0.1450` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 0.00 USD | 8,120.00 USD | 0.00 USD |
| `1D` | `0.1451` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 16,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1453` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 12,460.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.1455` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,450.00 USD | 689.96 USD | 0.00 USD |
| `1D` | `0.1457` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1459` | 4,820,000.00 USD | 0.00 USD | 4,820,000.00 USD | 0.00 USD | 4,870.00 USD | 3,350.00 USD |
| `1D` | `0.1461` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 0.00 USD | 3,000.00 USD | 2,680.00 USD |
| `1D` | `0.1463` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 9,940.00 USD | 3,900.00 USD | 5,440.00 USD |
| `1D` | `0.1465` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 11,020.00 USD | 8,490.00 USD | 11,120.00 USD |
| `7D` | `0.1465` | 8,260,000.00 USD | 0.00 USD | 8,260,000.00 USD | 0.00 USD | 3,700.00 USD | 93,240.00 USD |
| `1D` | `0.1467` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 0.00 USD | 1,110.00 USD | 2,660.00 USD |
| `7D` | `0.1468` | 8,160,000.00 USD | 0.00 USD | 8,160,000.00 USD | 9,720.00 USD | 5,520.00 USD | 3,880.00 USD |
| `1D` | `0.1469` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 5,850.00 USD | 1,420.00 USD | 0.00 USD |
| `1D` | `0.1471` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 10,000.00 USD | 7,170.00 USD | 933.22 USD |
| `7D` | `0.1471` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 6,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1473` | 4,730,000.00 USD | 0.00 USD | 4,730,000.00 USD | 24,360.00 USD | 26,350.00 USD | 78,410.00 USD |
| `7D` | `0.1474` | 8,140,000.00 USD | 0.00 USD | 8,140,000.00 USD | 19,430.00 USD | 12,610.00 USD | 24,530.00 USD |
| `1D` | `0.1475` | 4,600,000.00 USD | 0.00 USD | 4,600,000.00 USD | 20,680.00 USD | 7,230.00 USD | 4,670.00 USD |
| `1D` | `0.1477` | 4,560,000.00 USD | 0.00 USD | 4,560,000.00 USD | 101,700.00 USD | 18,420.00 USD | 158,990.00 USD |
| `7D` | `0.1477` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 85,800.00 USD | 25,460.00 USD | 110,550.00 USD |
| `1D` | `0.1479` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 71,170.00 USD | 13,530.00 USD | 29,040.00 USD |
| `7D` | `0.1480` | 7,860,000.00 USD | 0.00 USD | 7,860,000.00 USD | 50,400.00 USD | 29,300.00 USD | 20,830.00 USD |
| `1D` | `0.1481` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 45,520.00 USD | 1,650.00 USD | 3,880.00 USD |
| `1D` | `0.1483` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 28,260.00 USD | 8,210.00 USD | 125,420.00 USD |
| `7D` | `0.1483` | 7,760,000.00 USD | 0.00 USD | 7,760,000.00 USD | 42,230.00 USD | 16,640.00 USD | 202,650.00 USD |
| `1D` | `0.1485` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 45,800.00 USD | 1,040.00 USD | 66,840.00 USD |
| `7D` | `0.1486` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 66,760.00 USD | 10,470.00 USD | 35,500.00 USD |
| `1D` | `0.1487` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 8,840.00 USD | 3,580.00 USD | 11,560.00 USD |
| `1D` | `0.1489` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 24,850.00 USD | 0.00 USD | 5,520.00 USD |
| `7D` | `0.1489` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 21,100.00 USD | 3,710.00 USD | 67,450.00 USD |
| `1D` | `0.1491` | 3,790,000.00 USD | 0.00 USD | 3,790,000.00 USD | 23,780.00 USD | 15,530.00 USD | 11,460.00 USD |
| `7D` | `0.1492` | 7,290,000.00 USD | 0.00 USD | 7,290,000.00 USD | 40,320.00 USD | 22,920.00 USD | 35,230.00 USD |
| `1D` | `0.1493` | 3,740,000.00 USD | 0.00 USD | 3,740,000.00 USD | 20,150.00 USD | 9,030.00 USD | 8,810.00 USD |
| `1D` | `0.1495` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 56,660.00 USD | 0.00 USD | 28,520.00 USD |
| `7D` | `0.1495` | 7,190,000.00 USD | 0.00 USD | 7,190,000.00 USD | 34,650.00 USD | 18,690.00 USD | 191,550.00 USD |
| `1D` | `0.1497` | 3,620,000.00 USD | 0.00 USD | 3,620,000.00 USD | 8,630.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1498` | 6,950,000.00 USD | 0.00 USD | 6,950,000.00 USD | 42,100.00 USD | 9,610.00 USD | 10,480.00 USD |
| `1D` | `0.1499` | 3,610,000.00 USD | 0.00 USD | 3,610,000.00 USD | 5,920.00 USD | 7,890.00 USD | 2,340.00 USD |
| `1D` | `0.1501` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 11,460.00 USD | 13,130.00 USD | 2,490.00 USD |
| `7D` | `0.1501` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 21,010.00 USD | 7,930.00 USD | 15,630.00 USD |
| `1D` | `0.1503` | 3,560,000.00 USD | 0.00 USD | 3,560,000.00 USD | 48,710.00 USD | 4,400.00 USD | 153,130.00 USD |
| `7D` | `0.1504` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 17,800.00 USD | 11,590.00 USD | 44,850.00 USD |
| `1D` | `0.1505` | 3,360,000.00 USD | 0.00 USD | 3,360,000.00 USD | 35,380.00 USD | 1,940.00 USD | 5,420.00 USD |
| `1D` | `0.1507` | 3,320,000.00 USD | 0.00 USD | 3,320,000.00 USD | 0.00 USD | 1,150.00 USD | 304,230.00 USD |
| `7D` | `0.1507` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 152,330.00 USD | 12,910.00 USD | 182,120.00 USD |
| `1D` | `0.1509` | 3,010,000.00 USD | 0.00 USD | 3,010,000.00 USD | 0.00 USD | 6,130.00 USD | 49,580.00 USD |
| `7D` | `0.1510` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 135,010.00 USD | 12,930.00 USD | 112,100.00 USD |
| `1D` | `0.1511` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 1,300.00 USD |
| `1D` | `0.1513` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 11,750.00 USD | 3,900.00 USD | 249,020.00 USD |
| `7D` | `0.1513` | 6,160,000.00 USD | 0.00 USD | 6,160,000.00 USD | 0.00 USD | 17,610.00 USD | 104,500.00 USD |
| `1D` | `0.1515` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 7,040.00 USD | 0.00 USD | 122,820.00 USD |
| `7D` | `0.1516` | 6,040,000.00 USD | 0.00 USD | 6,040,000.00 USD | 48,970.00 USD | 0.00 USD | 338,620.00 USD |
| `1D` | `0.1517` | 2,560,000.00 USD | 0.00 USD | 2,560,000.00 USD | 12,390.00 USD | 6,150.00 USD | 21,910.00 USD |
| `1D` | `0.1519` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 40,200.00 USD | 7,220.00 USD | 28,700.00 USD |
| `7D` | `0.1519` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 47,340.00 USD | 24,320.00 USD | 70,660.00 USD |
| `1D` | `0.1521` | 2,440,000.00 USD | 0.00 USD | 2,440,000.00 USD | 33,890.00 USD | 4,770.00 USD | 13,640.00 USD |
| `7D` | `0.1522` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 0.00 USD | 9,640.00 USD | 130,510.00 USD |
| `1D` | `0.1523` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 8,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1525` | 2,380,000.00 USD | 0.00 USD | 2,380,000.00 USD | 40,210.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.1525` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 0.00 USD | 18,470.00 USD | 0.00 USD |
| `1D` | `0.1527` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 12,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1528` | 5,350,000.00 USD | 0.00 USD | 5,350,000.00 USD | 0.00 USD | 31,930.00 USD | 0.00 USD |
| `1D` | `0.1529` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 23,440.00 USD | 9,270.00 USD | 0.00 USD |
| `1D` | `0.1531` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 6,490.00 USD | 9,650.00 USD | 4,670.00 USD |
| `7D` | `0.1531` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 0.00 USD | 8,400.00 USD | 0.00 USD |
| `1D` | `0.1533` | 2,270,000.00 USD | 0.00 USD | 2,270,000.00 USD | 0.00 USD | 1,760.00 USD | 11,690.00 USD |
| `7D` | `0.1534` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 35,470.00 USD | 17,430.00 USD | 0.00 USD |
| `1D` | `0.1535` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 10,930.00 USD | 3,970.00 USD | 7,470.00 USD |
| `1D` | `0.1537` | 2,240,000.00 USD | 0.00 USD | 2,240,000.00 USD | 4,040.00 USD | 14,200.00 USD | 3,100.00 USD |
| `7D` | `0.1537` | 5,260,000.00 USD | 0.00 USD | 5,260,000.00 USD | 0.00 USD | 11,700.00 USD | 0.00 USD |
| `1D` | `0.1539` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 0.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.1540` | 5,250,000.00 USD | 0.00 USD | 5,250,000.00 USD | 0.00 USD | 6,530.00 USD | 0.00 USD |
| `1D` | `0.1541` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 32,370.00 USD | 1,730.00 USD | 7,440.00 USD |
| `7D` | `0.1543` | 5,240,000.00 USD | 0.00 USD | 5,240,000.00 USD | 0.00 USD | 3,590.00 USD | 0.00 USD |
| `1D` | `0.1545` | 2,170,000.00 USD | 0.00 USD | 2,170,000.00 USD | 20,110.00 USD | 7,790.00 USD | 5,850.00 USD |
| `1D` | `0.1547` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 14,430.00 USD | 0.00 USD | 4,630.00 USD |
| `1D` | `0.1549` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 5,820.00 USD | 17,930.00 USD | 25,090.00 USD |
| `7D` | `0.1549` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 0.00 USD | 19,500.00 USD | 89,090.00 USD |
| `1D` | `0.1551` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 14,290.00 USD | 12,210.00 USD | 5,970.00 USD |
| `7D` | `0.1552` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 0.00 USD | 17,320.00 USD | 0.00 USD |
| `1D` | `0.1553` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 12,260.00 USD | 4,020.00 USD | 5,190.00 USD |
| `1D` | `0.1555` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 40,830.00 USD | 1,660.00 USD | 8,390.00 USD |
| `7D` | `0.1555` | 5,110,000.00 USD | 0.00 USD | 5,110,000.00 USD | 0.00 USD | 9,540.00 USD | 0.00 USD |
| `1D` | `0.1557` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 2,800.00 USD | 12,870.00 USD | 5,360.00 USD |
| `7D` | `0.1558` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 0.00 USD | 20,630.00 USD | 178,620.00 USD |
| `1D` | `0.1559` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 17,010.00 USD | 2,970.00 USD | 4,410.00 USD |
| `1D` | `0.1561` | 1,920,000.00 USD | 0.00 USD | 1,920,000.00 USD | 12,360.00 USD | 3,020.00 USD | 7,670.00 USD |
| `7D` | `0.1561` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 0.00 USD | 5,070.00 USD | 0.00 USD |
| `1D` | `0.1563` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 11,460.00 USD | 25,680.00 USD | 3,980.00 USD |
| `7D` | `0.1564` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 0.00 USD | 43,350.00 USD | 0.00 USD |
| `1D` | `0.1565` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 54,610.00 USD | 19,210.00 USD | 16,410.00 USD |
| `1D` | `0.1567` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 25,400.00 USD | 1,850.00 USD | 9,250.00 USD |
| `7D` | `0.1567` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 123,230.00 USD | 15,360.00 USD | 0.00 USD |
| `1D` | `0.1569` | 1,730,000.00 USD | 0.00 USD | 1,730,000.00 USD | 24,170.00 USD | 0.00 USD | 107,740.00 USD |
| `7D` | `0.1570` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 134,890.00 USD | 5,100.00 USD | 210,460.00 USD |
| `1D` | `0.1571` | 1,600,000.00 USD | 0.00 USD | 1,600,000.00 USD | 54,580.00 USD | 7,000.00 USD | 49,580.00 USD |
| `1D` | `0.1573` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 24,010.00 USD | 3,460.00 USD | 32,940.00 USD |
| `7D` | `0.1573` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 191,190.00 USD | 64,570.00 USD | 34,380.00 USD |
| `1D` | `0.1575` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 4,810.00 USD | 11,190.00 USD |
| `7D` | `0.1576` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 26,600.00 USD | 108,010.00 USD | 0.00 USD |
| `1D` | `0.1577` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 28,900.00 USD | 29,200.00 USD | 14,400.00 USD |
| `1D` | `0.1579` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 11,910.00 USD | 0.00 USD | 12,500.00 USD |
| `7D` | `0.1579` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 197,810.00 USD | 80,390.00 USD | 8,370.00 USD |
| `1D` | `0.1581` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 19,190.00 USD | 8,040.00 USD | 2,850.00 USD |
| `7D` | `0.1582` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 56,130.00 USD | 17,610.00 USD | 38,720.00 USD |
| `1D` | `0.1583` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 86,410.00 USD | 25,280.00 USD | 29,500.00 USD |
| `1D` | `0.1585` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 21,920.00 USD | 20,720.00 USD | 8,460.00 USD |
| `7D` | `0.1585` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 87,110.00 USD | 0.00 USD | 23,800.00 USD |
| `1D` | `0.1587` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 50,950.00 USD | 19,830.00 USD | 44,380.00 USD |
| `7D` | `0.1588` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 74,200.00 USD | 0.00 USD | 89,310.00 USD |
| `1D` | `0.1589` | 973,550.00 USD | 0.00 USD | 973,550.00 USD | 20,380.00 USD | 6,150.00 USD | 44,860.00 USD |
| `1D` | `0.1591` | 902,160.00 USD | 0.00 USD | 902,160.00 USD | 20,460.00 USD | 21,570.00 USD | 42,540.00 USD |
| `7D` | `0.1591` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 0.00 USD | 12,590.00 USD | 16,720.00 USD |
| `1D` | `0.1593` | 817,590.00 USD | 0.00 USD | 817,590.00 USD | 14,950.00 USD | 38,970.00 USD | 45,470.00 USD |
| `7D` | `0.1594` | 3,240,000.00 USD | 0.00 USD | 3,240,000.00 USD | 0.00 USD | 29,330.00 USD | 0.00 USD |
| `1D` | `0.1595` | 718,200.00 USD | 0.00 USD | 718,200.00 USD | 10,260.00 USD | 14,420.00 USD | 7,350.00 USD |
| `1D` | `0.1597` | 686,170.00 USD | 0.00 USD | 686,170.00 USD | 11,790.00 USD | 0.00 USD | 6,030.00 USD |
| `7D` | `0.1597` | 3,210,000.00 USD | 0.00 USD | 3,210,000.00 USD | 0.00 USD | 96,110.00 USD | 0.00 USD |
| `1D` | `0.1599` | 668,360.00 USD | 0.00 USD | 668,360.00 USD | 7,070.00 USD | 7,580.00 USD | 0.00 USD |
| `7D` | `0.1600` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 0.00 USD | 38,830.00 USD | 75,810.00 USD |
| `1D` | `0.1601` | 653,710.00 USD | 0.00 USD | 653,710.00 USD | 21,340.00 USD | 2,310.00 USD | 4,670.00 USD |
| `1D` | `0.1603` | 625,390.00 USD | 0.00 USD | 625,390.00 USD | 28,500.00 USD | 14,000.00 USD | 0.00 USD |
| `7D` | `0.1603` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 0.00 USD | 58,120.00 USD | 116,120.00 USD |
| `1D` | `0.1605` | 582,890.00 USD | 0.00 USD | 582,890.00 USD | 24,530.00 USD | 0.00 USD | 36,130.00 USD |
| `7D` | `0.1606` | 2,820,000.00 USD | 0.00 USD | 2,820,000.00 USD | 237,510.00 USD | 0.00 USD | 376,580.00 USD |
| `1D` | `0.1607` | 522,230.00 USD | 0.00 USD | 522,230.00 USD | 5,090.00 USD | 17,410.00 USD | 0.00 USD |
| `1D` | `0.1609` | 499,730.00 USD | 0.00 USD | 499,730.00 USD | 57,710.00 USD | 0.00 USD | 90,310.00 USD |
| `7D` | `0.1609` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 117,480.00 USD | 11,640.00 USD | 296,510.00 USD |
| `1D` | `0.1611` | 351,700.00 USD | 0.00 USD | 351,700.00 USD | 61,340.00 USD | 69,930.00 USD | 44,280.00 USD |
| `7D` | `0.1612` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 304,890.00 USD | 10,980.00 USD | 254,850.00 USD |
| `1D` | `0.1613` | 176,150.00 USD | 0.00 USD | 176,150.00 USD | 18,100.00 USD | 30,050.00 USD | 15,220.00 USD |
| `1D` | `0.1615` | 112,780.00 USD | 0.00 USD | 112,780.00 USD | 0.00 USD | 16,430.00 USD | 0.00 USD |
| `7D` | `0.1615` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 293,210.00 USD | 35,210.00 USD | 243,310.00 USD |
| `1D` | `0.1617` | 96,350.00 USD | 0.00 USD | 96,350.00 USD | 0.00 USD | 3,570.00 USD | 0.00 USD |
| `7D` | `0.1618` | 638,790.00 USD | 0.00 USD | 638,790.00 USD | 0.00 USD | 0.00 USD | 47,590.00 USD |
| `1D` | `0.1619` | 92,790.00 USD | 0.00 USD | 92,790.00 USD | 0.00 USD | 17,910.00 USD | 30,970.00 USD |
| `1D` | `0.1621` | 43,910.00 USD | 0.00 USD | 43,910.00 USD | 0.00 USD | 5,660.00 USD | 0.00 USD |
| `7D` | `0.1621` | 591,200.00 USD | 0.00 USD | 591,200.00 USD | 78,750.00 USD | 57,300.00 USD | 0.00 USD |
| `7D` | `0.1624` | 455,150.00 USD | 0.00 USD | 455,150.00 USD | 0.00 USD | 170,670.00 USD | 33,440.00 USD |
| `1D` | `0.1625` | 38,240.00 USD | 0.00 USD | 38,240.00 USD | 38,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1627` | 251,040.00 USD | 0.00 USD | 251,040.00 USD | 76,780.00 USD | 0.00 USD | 103,330.00 USD |
| `7D` | `0.1630` | 70,940.00 USD | 0.00 USD | 70,940.00 USD | 70,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1637` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1639` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1649` | 16,600.00 USD | 16,600.00 USD | 0.00 USD | 11,310.00 USD | 3,450.00 USD | 1,840.00 USD |
| `1D` | `0.1651` | 41,460.00 USD | 41,460.00 USD | 0.00 USD | 24,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1653` | 64,690.00 USD | 64,690.00 USD | 0.00 USD | 17,080.00 USD | 0.00 USD | 6,160.00 USD |
| `1D` | `0.1655` | 76,710.00 USD | 76,710.00 USD | 0.00 USD | 5,090.00 USD | 2,360.00 USD | 4,570.00 USD |
| `1D` | `0.1657` | 91,660.00 USD | 91,660.00 USD | 0.00 USD | 14,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1659` | 113,040.00 USD | 113,040.00 USD | 0.00 USD | 0.00 USD | 6,040.00 USD | 15,340.00 USD |
| `7D` | `0.1660` | 97,610.00 USD | 97,610.00 USD | 0.00 USD | 68,280.00 USD | 29,330.00 USD | 0.00 USD |
| `1D` | `0.1661` | 130,100.00 USD | 130,100.00 USD | 0.00 USD | 0.00 USD | 13,210.00 USD | 3,860.00 USD |
| `1D` | `0.1663` | 211,190.00 USD | 211,190.00 USD | 0.00 USD | 11,790.00 USD | 14,550.00 USD | 54,750.00 USD |
| `7D` | `0.1663` | 247,680.00 USD | 247,680.00 USD | 0.00 USD | 121,520.00 USD | 0.00 USD | 28,550.00 USD |
| `1D` | `0.1665` | 255,600.00 USD | 255,600.00 USD | 0.00 USD | 7,070.00 USD | 3,710.00 USD | 33,630.00 USD |
| `7D` | `0.1666` | 338,750.00 USD | 338,750.00 USD | 0.00 USD | 49,590.00 USD | 12,670.00 USD | 28,810.00 USD |
| `1D` | `0.1667` | 302,170.00 USD | 302,170.00 USD | 0.00 USD | 21,340.00 USD | 5,340.00 USD | 19,890.00 USD |
| `1D` | `0.1669` | 329,930.00 USD | 329,930.00 USD | 0.00 USD | 4,600.00 USD | 15,730.00 USD | 7,440.00 USD |
| `7D` | `0.1669` | 583,020.00 USD | 583,020.00 USD | 0.00 USD | 76,120.00 USD | 81,000.00 USD | 87,160.00 USD |
| `1D` | `0.1671` | 399,990.00 USD | 399,990.00 USD | 0.00 USD | 33,930.00 USD | 0.00 USD | 36,130.00 USD |
| `7D` | `0.1672` | 786,760.00 USD | 786,760.00 USD | 0.00 USD | 96,910.00 USD | 38,070.00 USD | 68,760.00 USD |
| `1D` | `0.1673` | 484,240.00 USD | 484,240.00 USD | 0.00 USD | 51,000.00 USD | 13,590.00 USD | 19,670.00 USD |
| `1D` | `0.1675` | 517,530.00 USD | 517,530.00 USD | 0.00 USD | 8,930.00 USD | 1,990.00 USD | 22,370.00 USD |
| `7D` | `0.1675` | 981,350.00 USD | 981,350.00 USD | 0.00 USD | 64,490.00 USD | 130,100.00 USD | 0.00 USD |
| `1D` | `0.1677` | 707,690.00 USD | 707,690.00 USD | 0.00 USD | 86,210.00 USD | 58,400.00 USD | 45,540.00 USD |
| `7D` | `0.1678` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 71,860.00 USD | 90,910.00 USD | 16,740.00 USD |
| `1D` | `0.1679` | 765,350.00 USD | 765,350.00 USD | 0.00 USD | 20,840.00 USD | 14,460.00 USD | 22,370.00 USD |
| `1D` | `0.1681` | 918,420.00 USD | 918,420.00 USD | 0.00 USD | 94,350.00 USD | 36,530.00 USD | 22,180.00 USD |
| `7D` | `0.1681` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 69,520.00 USD | 71,610.00 USD | 128,480.00 USD |
| `1D` | `0.1683` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 61,280.00 USD | 12,810.00 USD | 49,630.00 USD |
| `7D` | `0.1684` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 60,960.00 USD | 14,000.00 USD | 47,590.00 USD |
| `1D` | `0.1685` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 41,190.00 USD | 48,480.00 USD | 52,800.00 USD |
| `1D` | `0.1687` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 6,960.00 USD | 9,500.00 USD | 74,600.00 USD |
| `7D` | `0.1687` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 78,750.00 USD | 0.00 USD | 14,830.00 USD |
| `1D` | `0.1689` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 54,040.00 USD | 26,970.00 USD | 23,460.00 USD |
| `7D` | `0.1690` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 63,850.00 USD | 74,130.00 USD |
| `1D` | `0.1691` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 69,010.00 USD | 72,070.00 USD | 108,930.00 USD |
| `1D` | `0.1693` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 57,220.00 USD | 35,730.00 USD | 61,640.00 USD |
| `7D` | `0.1693` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 33,660.00 USD | 46,740.00 USD | 42,090.00 USD |
| `1D` | `0.1695` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 18,340.00 USD | 17,530.00 USD | 19,580.00 USD |
| `7D` | `0.1696` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 17,360.00 USD | 87,350.00 USD | 28,010.00 USD |
| `1D` | `0.1697` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 27,270.00 USD | 37,380.00 USD | 0.00 USD |
| `1D` | `0.1699` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 24,020.00 USD | 22,050.00 USD | 51,290.00 USD |
| `7D` | `0.1699` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 25,330.00 USD | 18,830.00 USD |
| `1D` | `0.1701` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 9,960.00 USD | 7,000.00 USD | 24,300.00 USD |
| `7D` | `0.1702` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 68,360.00 USD | 55,360.00 USD | 72,270.00 USD |
| `1D` | `0.1703` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 14,420.00 USD | 16,630.00 USD |
| `1D` | `0.1705` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 35,700.00 USD | 6,390.00 USD | 11,670.00 USD |
| `7D` | `0.1705` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 34,380.00 USD |
| `1D` | `0.1707` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 46,300.00 USD | 71,240.00 USD | 26,650.00 USD |
| `7D` | `0.1708` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 31,310.00 USD | 87,520.00 USD |
| `1D` | `0.1709` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 28,900.00 USD | 29,200.00 USD | 17,110.00 USD |
| `1D` | `0.1711` | 2,390,000.00 USD | 2,390,000.00 USD | 0.00 USD | 17,400.00 USD | 4,910.00 USD | 17,830.00 USD |
| `7D` | `0.1711` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 0.00 USD | 5,490.00 USD | 8,370.00 USD |
| `1D` | `0.1713` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 7,010.00 USD | 20,450.00 USD | 2,850.00 USD |
| `7D` | `0.1714` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 59,620.00 USD | 38,720.00 USD |
| `1D` | `0.1715` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 11,710.00 USD | 40,520.00 USD | 32,850.00 USD |
| `1D` | `0.1717` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 10,610.00 USD | 18,050.00 USD | 10,190.00 USD |
| `7D` | `0.1717` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,960.00 USD |
| `1D` | `0.1719` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 39,720.00 USD | 5,950.00 USD | 20,520.00 USD |
| `7D` | `0.1720` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 39,370.00 USD | 0.00 USD | 161,770.00 USD |
| `1D` | `0.1721` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 53,810.00 USD | 19,690.00 USD | 47,610.00 USD |
| `1D` | `0.1723` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 29,070.00 USD | 9,300.00 USD | 54,900.00 USD |
| `7D` | `0.1723` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 118,060.00 USD | 12,590.00 USD | 225,200.00 USD |
| `1D` | `0.1725` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 8,230.00 USD | 13,360.00 USD | 37,590.00 USD |
| `1D` | `0.1727` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 10,260.00 USD | 0.00 USD | 7,360.00 USD |
| `1D` | `0.1729` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 8,220.00 USD | 0.00 USD | 6,720.00 USD |
| `7D` | `0.1729` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 120,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1732` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 324,890.00 USD | 0.00 USD | 9,420.00 USD |
| `1D` | `0.1733` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 7,950.00 USD | 1,560.00 USD | 10,060.00 USD |
| `1D` | `0.1735` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 16,980.00 USD | 9,510.00 USD | 1,170.00 USD |
| `1D` | `0.1737` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 15,900.00 USD | 2,310.00 USD | 6,410.00 USD |
| `7D` | `0.1738` | 3,700,000.00 USD | 3,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 101,630.00 USD |
| `1D` | `0.1739` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 2,270.00 USD | 2,500.00 USD |
| `1D` | `0.1741` | 2,990,000.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | 0.00 USD |
| `1D` | `0.1743` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,980.00 USD |
| `7D` | `0.1744` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 13,120.00 USD |
| `1D` | `0.1745` | 3,020,000.00 USD | 3,020,000.00 USD | 0.00 USD | 3,500.00 USD | 2,460.00 USD | 3,250.00 USD |
| `1D` | `0.1747` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 25,680.00 USD |
| `1D` | `0.1749` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 80,070.00 USD | 2,280.00 USD | 17,280.00 USD |
| `7D` | `0.1750` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 69,520.00 USD | 0.00 USD | 120,240.00 USD |
| `1D` | `0.1751` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 16,950.00 USD | 0.00 USD | 10,700.00 USD |
| `1D` | `0.1753` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 17,770.00 USD | 0.00 USD | 11,350.00 USD |
| `7D` | `0.1753` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 197,880.00 USD |
| `1D` | `0.1755` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 16,760.00 USD | 8,430.00 USD | 21,420.00 USD |
| `7D` | `0.1756` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 112,930.00 USD | 0.00 USD | 53,560.00 USD |
| `1D` | `0.1757` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 6,850.00 USD | 14,210.00 USD | 49,080.00 USD |
| `1D` | `0.1759` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 40,430.00 USD | 7,040.00 USD | 7,910.00 USD |
| `7D` | `0.1759` | 4,500,000.00 USD | 4,500,000.00 USD | 0.00 USD | 200,480.00 USD | 38,670.00 USD | 0.00 USD |
| `1D` | `0.1761` | 3,510,000.00 USD | 3,510,000.00 USD | 0.00 USD | 33,150.00 USD | 66,160.00 USD | 36,270.00 USD |
| `7D` | `0.1762` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 117,200.00 USD | 94,740.00 USD | 32,350.00 USD |
| `1D` | `0.1763` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 17,320.00 USD | 10,910.00 USD | 33,930.00 USD |
| `1D` | `0.1765` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 15,830.00 USD | 20,220.00 USD | 35,570.00 USD |
| `7D` | `0.1765` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 154,540.00 USD | 97,630.00 USD | 48,870.00 USD |
| `1D` | `0.1767` | 3,740,000.00 USD | 3,740,000.00 USD | 0.00 USD | 19,860.00 USD | 41,430.00 USD | 34,410.00 USD |
| `7D` | `0.1768` | 5,330,000.00 USD | 5,330,000.00 USD | 0.00 USD | 161,560.00 USD | 92,440.00 USD | 23,040.00 USD |
| `1D` | `0.1769` | 3,830,000.00 USD | 3,830,000.00 USD | 0.00 USD | 21,060.00 USD | 35,020.00 USD | 32,820.00 USD |
| `1D` | `0.1771` | 3,850,000.00 USD | 3,850,000.00 USD | 0.00 USD | 16,140.00 USD | 5,670.00 USD | 2,400.00 USD |
| `7D` | `0.1771` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 69,030.00 USD | 83,790.00 USD | 21,360.00 USD |
| `1D` | `0.1773` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 5,720.00 USD | 23,730.00 USD | 18,830.00 USD |
| `7D` | `0.1774` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 148,780.00 USD | 85,710.00 USD | 0.00 USD |
| `1D` | `0.1775` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 20,860.00 USD | 6,390.00 USD | 5,300.00 USD |
| `1D` | `0.1777` | 4,050,000.00 USD | 4,050,000.00 USD | 0.00 USD | 27,230.00 USD | 68,360.00 USD | 20,580.00 USD |
| `7D` | `0.1777` | 5,900,000.00 USD | 5,900,000.00 USD | 0.00 USD | 67,350.00 USD | 40,700.00 USD | 59,520.00 USD |
| `1D` | `0.1779` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 7,310.00 USD | 9,400.00 USD | 7,340.00 USD |
| `7D` | `0.1780` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 52,730.00 USD | 38,910.00 USD | 46,470.00 USD |
| `1D` | `0.1781` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 3,800.00 USD | 1,610.00 USD | 2,080.00 USD |
| `1D` | `0.1783` | 4,140,000.00 USD | 4,140,000.00 USD | 0.00 USD | 27,640.00 USD | 15,680.00 USD | 18,910.00 USD |
| `7D` | `0.1783` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 117,540.00 USD | 56,000.00 USD | 21,910.00 USD |
| `1D` | `0.1785` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 12,390.00 USD | 27,370.00 USD | 5,360.00 USD |
| `7D` | `0.1786` | 6,430,000.00 USD | 6,430,000.00 USD | 0.00 USD | 129,440.00 USD | 55,090.00 USD | 14,040.00 USD |
| `1D` | `0.1787` | 4,220,000.00 USD | 4,220,000.00 USD | 0.00 USD | 7,560.00 USD | 21,410.00 USD | 5,900.00 USD |
| `1D` | `0.1789` | 4,230,000.00 USD | 4,230,000.00 USD | 0.00 USD | 9,350.00 USD | 1,210.00 USD | 2,310.00 USD |
| `7D` | `0.1789` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 48,810.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.1791` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 2,640.00 USD | 5,060.00 USD |
| `7D` | `0.1792` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 134,000.00 USD | 43,520.00 USD | 3,940.00 USD |
| `1D` | `0.1793` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 9,190.00 USD | 4,600.00 USD | 2,660.00 USD |
| `1D` | `0.1795` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 17,710.00 USD | 33,080.00 USD | 12,260.00 USD |
| `7D` | `0.1795` | 6,750,000.00 USD | 6,750,000.00 USD | 0.00 USD | 17,130.00 USD | 19,870.00 USD | 44,450.00 USD |
| `1D` | `0.1797` | 4,350,000.00 USD | 4,350,000.00 USD | 0.00 USD | 10,870.00 USD | 4,390.00 USD | 9,760.00 USD |
| `7D` | `0.1798` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 6,240.00 USD | 27,010.00 USD |
| `1D` | `0.1799` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 3,780.00 USD | 8,790.00 USD | 11,410.00 USD |
| `1D` | `0.1801` | 4,410,000.00 USD | 4,410,000.00 USD | 0.00 USD | 3,730.00 USD | 17,760.00 USD | 13,800.00 USD |
| `7D` | `0.1801` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 19,430.00 USD | 43,480.00 USD | 55,340.00 USD |
| `1D` | `0.1803` | 4,430,000.00 USD | 4,430,000.00 USD | 0.00 USD | 3,990.00 USD | 10,580.00 USD | 14,430.00 USD |
| `7D` | `0.1804` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 28,790.00 USD | 27,450.00 USD | 25,100.00 USD |
| `1D` | `0.1805` | 4,450,000.00 USD | 4,450,000.00 USD | 0.00 USD | 4,010.00 USD | 4,760.00 USD | 6,870.00 USD |
| `1D` | `0.1807` | 4,480,000.00 USD | 4,480,000.00 USD | 0.00 USD | 11,560.00 USD | 11,500.00 USD | 9,360.00 USD |
| `7D` | `0.1807` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 11,410.00 USD | 63,170.00 USD | 67,160.00 USD |
| `1D` | `0.1809` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 2,490.00 USD | 7,210.00 USD | 1,970.00 USD |
| `1D` | `0.1810` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 9,360.00 USD | 3,190.00 USD | 0.00 USD |
| `7D` | `0.1810` | 7,250,000.00 USD | 7,250,000.00 USD | 0.00 USD | 79,380.00 USD | 30,940.00 USD | 12,950.00 USD |
| `7D` | `0.1813` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 32,530.00 USD | 15,780.00 USD | 67,760.00 USD |
| `7D` | `0.1816` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 46,430.00 USD | 21,200.00 USD | 35,500.00 USD |
| `7D` | `0.1819` | 7,590,000.00 USD | 7,590,000.00 USD | 0.00 USD | 52,150.00 USD | 24,720.00 USD | 43,100.00 USD |
| `7D` | `0.1822` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 46,760.00 USD | 29,530.00 USD | 37,430.00 USD |
| `7D` | `0.1825` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 38,800.00 USD | 17,120.00 USD | 20,270.00 USD |
| `7D` | `0.1828` | 7,840,000.00 USD | 7,840,000.00 USD | 0.00 USD | 29,430.00 USD | 13,380.00 USD | 17,090.00 USD |
| `7D` | `0.1831` | 7,940,000.00 USD | 7,940,000.00 USD | 0.00 USD | 63,190.00 USD | 9,610.00 USD | 24,180.00 USD |
| `7D` | `0.1834` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 18,400.00 USD | 0.00 USD | 15,630.00 USD |
| `7D` | `0.1837` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 11,490.00 USD | 13,450.00 USD | 83,480.00 USD |
| `7D` | `0.1840` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 70,360.00 USD | 18,020.00 USD | 65,400.00 USD |
| `7D` | `0.1843` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 17,340.00 USD | 3,040.00 USD | 28,930.00 USD |
| `7D` | `0.1846` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 8,330.00 USD | 10,850.00 USD | 42,240.00 USD |
| `7D` | `0.1848` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 35,280.00 USD | 35,270.00 USD | 5,880.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `185.49M` | Total OI Tokens: `1,133,864,915.1 ARB`
  * 1h OI Change: `+1.54%` | 4h OI Change: `+0.46%` | 24h OI Change: `-13.27%`
  * Exchange Breakdown: Binance=`40.42M` | Bybit=`25.92M` | OKX=`13.98M` | Hyperliquid=`12.95M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.03K` | Last 24h: `11.04K` | Last 3d: `13.14K` | Last 7d: `51.59K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0078%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0079%` | **USDT Bitget** | `0.0017%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ARB` | `66.13%` | `33.87%` | `1.95` | 2,930,000.00 USD |
| `15M` | `Binance` | `65.25%` | `34.75%` | `1.88` | 1,150,000.00 USD |
| `15M` | `OKX` | `60.15%` | `39.85%` | `1.51` | 394,720.00 USD |
| `15M` | `Bybit` | `69.44%` | `30.56%` | `2.27` | 290,500.00 USD |
| `15M` | `KuCoin` | `52.89%` | `47.11%` | `1.12` | 38,720.00 USD |
| `15M` | `Gate` | `57.37%` | `42.63%` | `1.35` | 42,290.00 USD |
| `15M` | `Bitget` | `55.22%` | `44.78%` | `1.23` | 252,940.00 USD |
| `15M` | `BingX` | `57.86%` | `42.14%` | `1.37` | 50,480.00 USD |
| `15M` | `MEXC` | `77.64%` | `22.36%` | `3.47` | 340,190.00 USD |
| `15M` | `Bitunix` | `51.84%` | `48.16%` | `1.08` | 49,770.00 USD |
| `15M` | `Hyperliquid` | `66.58%` | `33.42%` | `1.99` | 55,570.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `52.74%` | `47.26%` | `1.12` | 100,040.00 USD |
| `15M` | `Crypto.com` | `0.25%` | `99.75%` | `0.00` | 1,160.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 154,980.00 USD |
| `15M` | `HTX` | `55.34%` | `44.66%` | `1.24` | 121.30 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `44.7%` | `55.3%` | `0.81` | 2,970.00 USD |
| `15M` | `Aster` | `90.53%` | `9.47%` | `9.56` | 58.24 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.49%` | `85.51%` | `0.17` | 10,180.00 USD |
| `15M` | `Whale Positions` | `65.25%` | `34.75%` | `1.88` | 1,150,000.00 USD |
| `15M` | `Global Accounts` | `66.13%` | `33.87%` | `1.95` | 2,930,000.00 USD |
| `1H` | `ARB` | `59.26%` | `40.74%` | `1.45` | 8,590,000.00 USD |
| `1H` | `Binance` | `57.81%` | `42.19%` | `1.37` | 2,920,000.00 USD |
| `1H` | `OKX` | `50.89%` | `49.11%` | `1.04` | 1,340,000.00 USD |
| `1H` | `Bybit` | `66.7%` | `33.3%` | `2.00` | 646,500.00 USD |
| `1H` | `KuCoin` | `67.04%` | `32.96%` | `2.03` | 213,070.00 USD |
| `1H` | `Gate` | `63.87%` | `36.13%` | `1.77` | 208,140.00 USD |
| `1H` | `Bitget` | `58.81%` | `41.19%` | `1.43` | 679,250.00 USD |
| `1H` | `BingX` | `34.11%` | `65.89%` | `0.52` | 643,030.00 USD |
| `1H` | `MEXC` | `69.86%` | `30.14%` | `2.32` | 835,010.00 USD |
| `1H` | `Bitunix` | `53.11%` | `46.89%` | `1.13` | 168,100.00 USD |
| `1H` | `Hyperliquid` | `57.47%` | `42.53%` | `1.35` | 105,530.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.38%` | `48.62%` | `1.06` | 202,260.00 USD |
| `1H` | `Crypto.com` | `25.07%` | `74.93%` | `0.33` | 2,790.00 USD |
| `1H` | `WhiteBIT` | `100%` | `0%` | `1.00` | 538,410.00 USD |
| `1H` | `HTX` | `57.49%` | `42.51%` | `1.35` | 323.20 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `36.82%` | `63.18%` | `0.58` | 21,700.00 USD |
| `1H` | `Aster` | `91.47%` | `8.53%` | `10.72` | 258.63 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `11.64%` | `88.36%` | `0.13` | 60,220.00 USD |
| `1H` | `Whale Positions` | `57.81%` | `42.19%` | `1.37` | 2,920,000.00 USD |
| `1H` | `Global Accounts` | `59.26%` | `40.74%` | `1.45` | 8,590,000.00 USD |
| `4H` | `ARB` | `50.12%` | `49.88%` | `1.00` | 42,120,000.00 USD |
| `4H` | `Binance` | `50.69%` | `49.31%` | `1.03` | 15,440,000.00 USD |
| `4H` | `OKX` | `47.83%` | `52.17%` | `0.92` | 6,080,000.00 USD |
| `4H` | `Bybit` | `50.1%` | `49.9%` | `1.00` | 4,310,000.00 USD |
| `4H` | `KuCoin` | `49.18%` | `50.82%` | `0.97` | 736,130.00 USD |
| `4H` | `Gate` | `47.42%` | `52.58%` | `0.90` | 1,340,000.00 USD |
| `4H` | `Bitget` | `50.52%` | `49.48%` | `1.02` | 2,870,000.00 USD |
| `4H` | `BingX` | `28.36%` | `71.64%` | `0.40` | 3,280,000.00 USD |
| `4H` | `MEXC` | `52.64%` | `47.36%` | `1.11` | 3,130,000.00 USD |
| `4H` | `Bitunix` | `51.45%` | `48.55%` | `1.06` | 612,080.00 USD |
| `4H` | `Hyperliquid` | `59.19%` | `40.81%` | `1.45` | 635,810.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.82%` | `50.18%` | `0.99` | 1,490,000.00 USD |
| `4H` | `Crypto.com` | `39.04%` | `60.96%` | `0.64` | 21,620.00 USD |
| `4H` | `WhiteBIT` | `86.51%` | `13.49%` | `6.41` | 1,840,000.00 USD |
| `4H` | `HTX` | `66.48%` | `33.52%` | `1.98` | 13,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.06%` | `57.94%` | `0.73` | 105,850.00 USD |
| `4H` | `Aster` | `25.96%` | `74.04%` | `0.35` | 28,920.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.1%` | `47.9%` | `1.09` | 197,100.00 USD |
| `4H` | `Whale Positions` | `50.69%` | `49.31%` | `1.03` | 15,440,000.00 USD |
| `4H` | `Global Accounts` | `50.12%` | `49.88%` | `1.00` | 42,120,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.1625` | `0.1631` | `0.1625` | `0.1640` | `0.1624` | 778,400.97 USD | 315,731.23 USD | 462,669.74 USD | -146,938.51 USD | `-18.88%` | `22B / 62S` |
| `0:00 UTC` | `0.1629` | `0.1625` | `0.1629` | `0.1632` | `0.1619` | 775,902.97 USD | 309,320.91 USD | 466,582.05 USD | -157,261.14 USD | `-20.27%` | `13B / 34S` |
| `5:00 UTC` | `0.1623` | `0.1620` | `0.1623` | `0.1624` | `0.1615` | 562,907.20 USD | 223,683.16 USD | 339,224.04 USD | -115,540.88 USD | `-20.53%` | `7B / 21S` |
| `0:00 UTC` | `0.1620` | `0.1617` | `0.1620` | `0.1623` | `0.1611` | 779,913.00 USD | 372,491.97 USD | 407,421.03 USD | -34,929.06 USD | `-4.48%` | `22B / 23S` |
| `5:00 UTC` | `0.1620` | `0.1619` | `0.1620` | `0.1622` | `0.1615` | 338,104.92 USD | 163,363.17 USD | 174,741.74 USD | -11,378.57 USD | `-3.37%` | `6B / 19S` |
| `0:00 UTC` | `0.1617` | `0.1618` | `0.1617` | `0.1624` | `0.1613` | 561,491.28 USD | 247,384.47 USD | 314,106.81 USD | -66,722.34 USD | `-11.88%` | `26B / 27S` |
| `5:00 UTC` | `0.1628` | `0.1622` | `0.1628` | `0.1629` | `0.1614` | 451,221.10 USD | 279,978.35 USD | 171,242.75 USD | 108,735.60 USD | `+24.10%` | `38B / 17S` |
| `0:00 UTC` | `0.1626` | `0.1627` | `0.1626` | `0.1631` | `0.1620` | 555,739.49 USD | 264,990.40 USD | 290,749.08 USD | -25,758.68 USD | `-4.64%` | `27B / 22S` |
| `5:00 UTC` | `0.1623` | `0.1631` | `0.1623` | `0.1643` | `0.1623` | 958,344.10 USD | 650,478.72 USD | 307,865.38 USD | 342,613.33 USD | `+35.75%` | `38B / 5S` |
| `0:00 UTC` | `0.1635` | `0.1637` | `0.1635` | `0.1641` | `0.1633` | 542,824.03 USD | 324,781.45 USD | 218,042.57 USD | 106,738.88 USD | `+19.66%` | `15B / 12S` |

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
| `5m` | 5,130.00 USD | 278,920.00 USD | **`ACCUMULATION`** |
| `15m` | 30,620.00 USD | 676,600.00 USD | **`ACCUMULATION`** |
| `30m` | 75,190.00 USD | 664,300.00 USD | **`ACCUMULATION`** |
| `1h` | 45,560.00 USD | 739,320.00 USD | **`ACCUMULATION`** |
| `2h` | -98,860.00 USD | 209,130.00 USD | **`ACCUMULATION`** |
| `4h` | -403,260.00 USD | -96,080.00 USD | **`DISTRIBUTION`** |
| `6h` | -559,550.00 USD | -1,920,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -586,540.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -876,070.00 USD | -1,880,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,400,000.00 USD | -10,630,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,460,000.00 USD | -36,780,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -33,590,000.00 USD | -165,500,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+5.13K` | 15m=`+30.62K` | 1h=`+45.56K` | 24h=`-2.40M`
* Futures Capital Netflows: 5m=`+278.92K` | 15m=`+676.60K` | 1h=`+739.32K` | 24h=`-10.63M`
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
  * `2026-10-30 16:35:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:32 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:37:32 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:36:32 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:38:32 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
