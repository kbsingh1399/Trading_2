# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 21:43:07 IST` (`2026-10-29 16:13:07 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2007` | **Live Ask Quote**: `0.2028` | **Mid Price**: `0.2017`
- **Spread Points**: `21.00` | **Spread BPS**: `104.09 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1984` | VWAP Z-Score: `+0.94` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0011` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `59.89` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2055` | Lower -3.00σ Band: `0.1913`
  * Upper +2.51σ Band: `0.2043` | Lower -2.51σ Band: `0.1925`
  * Upper +2.01σ Band: `0.2031` | Lower -2.01σ Band: `0.1937`
  * Upper +2.00σ Band: `0.2031` | Lower -2.00σ Band: `0.1937`
  * Upper +1.28σ Band: `0.2014` | Lower -1.28σ Band: `0.1954`
  * Upper +1.00σ Band: `0.2008` | Lower -1.00σ Band: `0.1960`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1999` | EMA-20=`0.1994` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1993` (Slope: `+0.0000`) | EMA-100=`0.2003`
  * Institutional Anchors: EMA-144=`0.2010` | EMA-200=`0.2015` (Slope: `-0.1069`) | EMA-233=`0.2018`
- **Range Boundaries**: 24H High=`0.2086` | 24H Low=`0.1944` | Weekly High=`0.2086` | Weekly Low=`0.1944`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2005` (Distance: `+0.65%`)
  * Point of Control (POC) = `0.1969` (Distance: `+2.51%`)
  * Value Area Low (VAL) = `0.1953` (Distance: `+3.31%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2058` | Weekly POC=`0.2030` | Weekly VAL=`0.2011`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2014` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2009` - `0.2026`
  * Optimal Trade Entry (OTE 0.705): `0.2022`
  * Structural Invalidation Anchor (0.786): `0.2034`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.2019` | `0.2023` | `0.2017` | `0.2021` | `2,939,702` | 593,695.11 USD | -19,549.86 USD | `-3.29%` | 358,934.88 USD | `-0.81` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `0.2020` | `0.2023` | `0.2015` | `0.2015` | `1,890,459` | 381,539.39 USD | 2,529.26 USD | `+0.66%` | 361,464.14 USD | `-0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.2015` | `0.2020` | `0.2012` | `0.2020` | `2,005,051` | 404,192.04 USD | 57,606.07 USD | `+14.25%` | 419,070.21 USD | `+0.02` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.2019` | `0.2020` | `0.2003` | `0.2009` | `11,891,810` | 2,391,609.70 USD | 33,663.94 USD | `+1.41%` | 125,320.55 USD | `-0.09` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2008` | `0.2026` | `0.2007` | `0.2018` | `9,846,458` | 1,983,992.92 USD | 253,164.20 USD | `+12.76%` | 378,484.74 USD | `+0.93` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.2019` | `0.2023` | `0.2012` | `0.2020` | `6,835,212` | 1,379,426.54 USD | 40,585.47 USD | `+2.94%` | 419,070.21 USD | `-0.04` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2009` | `0.2014` | `0.1996` | `0.2012` | `39,609,825` | 7,938,983.02 USD | 184,682.64 USD | `+2.33%` | -587,100.45 USD | `+0.13` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2012` | `0.2026` | `0.2003` | `0.2018` | `39,918,736` | 8,040,677.08 USD | 662,896.98 USD | `+8.24%` | 75,796.52 USD | `+0.47` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `0.2019` | `0.2023` | `0.2012` | `0.2020` | `6,835,212` | 1,379,426.54 USD | 40,585.47 USD | `+2.94%` | 116,381.99 USD | `+0.04` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -1,613,244.20 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -832,295.15 USD | `+0.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2026` | `0.1996` | `0.2020` | `86,363,773` | 17,359,086.64 USD | 888,165.08 USD | `+5.12%` | 55,869.93 USD | `+0.32` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `0.2070` | `0.2106` | `0.2046` | `0.2059` | `145,047,947` | 30,041,034.19 USD | 2,906,011.83 USD | `+9.67%` | 3,801,088.83 USD | `+1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2058` | `0.2065` | `0.1954` | `0.1973` | `282,726,861` | 56,231,891.33 USD | -5,955,308.28 USD | `-10.59%` | -2,154,219.45 USD | `-1.38` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -1,613,244.20 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -832,295.15 USD | `+0.31` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2026` | `0.1996` | `0.2020` | `86,363,773` | 17,359,086.64 USD | 888,165.08 USD | `+5.12%` | 55,869.93 USD | `+0.32` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`0.2017`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `536` | `0x77ee...2902` | `SHORT` | 4,324,192.17 USD | `21,412,192.00` | `0.1911` | `0.2018` | `0.5668` | -232,940.43 USD | `-5.39%` | `10X Cross` |
| `1219` | `0x123d...3bff` | `LONG` | 1,896,381.44 USD | `9,393,142.00` | `0.2912` | `0.2018` | `0.000000` | -839,354.50 USD | `-44.26%` | `10X Cross` |
| `1253` | `0x7737...bf66` | `SHORT` | 1,834,203.27 USD | `9,091,466.00` | `0.2190` | `0.2018` | `2.14` | 156,786.53 USD | `+8.55%` | `10X Cross` |
| `1554` | `0x5f94...4b96` | `SHORT` | 1,446,430.12 USD | `7,162,318.00` | `0.2303` | `0.2018` | `0.7495` | 203,045.08 USD | `+14.04%` | `10X Cross` |
| `1772` | `0x4982...59e6` | `SHORT` | 1,211,460.08 USD | `5,998,812.00` | `0.1891` | `0.2018` | `0.3926` | -76,901.72 USD | `-6.35%` | `10X Cross` |
| `1821` | `0xcac1...26b3` | `LONG` | 1,172,625.41 USD | `5,803,927.00` | `0.2000` | `0.2018` | `0.000000` | 11,809.83 USD | `+1.01%` | `10X Cross` |
| `2009` | `0x51f6...2b39` | `LONG` | 1,022,947.43 USD | `5,065,350.00` | `0.2294` | `0.2018` | `0.000000` | -139,202.15 USD | `-13.61%` | `10X Cross` |
| `2017` | `0xeadc...9d55` | `LONG` | 1,016,698.74 USD | `5,038,400.00` | `0.2195` | `0.2018` | `0.000000` | -89,014.01 USD | `-8.76%` | `10X Cross` |
| `2033` | `0x0748...d4b2` | `SHORT` | 1,009,750.00 USD | `5,000,000.00` | `0.2036` | `0.2018` | `0.5737` | 8,107.24 USD | `+0.80%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2046` | 6,153.89 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2046 USD [API] | `2026-10-27 20:33:02` |
| `ANNOUNCEMENT` | `INFO` | `0.2046` | 6,648.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2046 USD [API] | `2026-10-27 20:39:19` |
| `ANNOUNCEMENT` | `INFO` | `0.2044` | 6,587.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.59K USD at 0.2044 USD [API] | `2026-10-27 21:21:42` |
| `ANNOUNCEMENT` | `INFO` | `0.2067` | 6,278.84 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.28K USD at 0.2067 USD [API] | `2026-10-27 21:36:56` |
| `ANNOUNCEMENT` | `INFO` | `0.2063` | 6,645.63 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2063 USD [API] | `2026-10-27 21:39:43` |
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 6,655.44 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.66K USD at 0.2061 USD [API] | `2026-10-27 21:46:03` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2047` (Vol: 214,800.00 USD, Dist: `+1.24%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.70%`)
  * 48H Horizon: Short MP=`0.2137` (Vol: 235,900.00 USD, Dist: `+5.69%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.70%`)
  * 3D Horizon: Short MP=`0.2111` (Vol: 241,100.00 USD, Dist: `+4.40%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--4.70%`)
  * 7D Horizon: Short MP=`0.2124` (Vol: 359,800.00 USD, Dist: `+5.03%`) | Long MP=`0.1926` (Vol: 321,900.00 USD, Dist: `--4.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0475` | 235.98 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 5,510.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 481.50 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0545` | 139.57 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 2,270.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0605` | 945.49 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 128,350.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 752.61 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0735` | 1,470.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0775` | 659.99 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 11,840.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 967.50 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 110,400.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1045` | 331.06 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 890.98 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 942.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 2,900.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 125.97 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 1,160.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,890.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 7,300.00 USD | 2,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 659.30 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 2,810.00 USD | 2,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 806.33 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 10,000.00 USD | 2,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 14,650.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,500.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 7,310.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 1,800.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 163.65 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 599.05 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 144.33 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 33,400.00 USD | 2,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,640.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 838.47 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 16,490.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 1,580.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 532,050.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,000.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 4,070.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,310.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 5,850.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 3,500.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 12,040.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 356.65 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 35,330.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 1,750.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 511.21 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 619,830.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 254,680.00 USD | 965,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 3,340.00 USD | 710,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 707,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,720.00 USD | 706,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 4,580.00 USD | 701,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1770` | 11,340,000.00 USD | 11,340,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 696,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1780` | 11,270,000.00 USD | 11,270,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 38,210.00 USD | 681,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1790` | 11,200,000.00 USD | 11,200,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 11,150.00 USD | 642,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 8,500,000.00 USD | 8,500,000.00 USD | 126,680.00 USD | 46,860.00 USD | 75,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 135,130.00 USD | 631,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 8,250,000.00 USD | 8,250,000.00 USD | 50,220.00 USD | 23,230.00 USD | 37,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 11,150,000.00 USD | 11,150,000.00 USD | 112,560.00 USD | 27,510.00 USD | 31,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 496,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 8,140,000.00 USD | 8,140,000.00 USD | 48,460.00 USD | 19,700.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 10,980,000.00 USD | 10,980,000.00 USD | 95,280.00 USD | 47,480.00 USD | 117,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,250.00 USD | 488,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 7,990,000.00 USD | 7,990,000.00 USD | 48,990.00 USD | 11,640.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 10,720,000.00 USD | 10,720,000.00 USD | 84,560.00 USD | 36,880.00 USD | 59,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 470,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 7,910,000.00 USD | 7,910,000.00 USD | 80,720.00 USD | 17,960.00 USD | 17,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 10,540,000.00 USD | 10,540,000.00 USD | 226,530.00 USD | 58,050.00 USD | 174,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 470,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 7,800,000.00 USD | 7,800,000.00 USD | 103,680.00 USD | 35,330.00 USD | 67,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 10,080,000.00 USD | 10,080,000.00 USD | 404,170.00 USD | 111,470.00 USD | 387,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 4,100.00 USD | 469,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 7,590,000.00 USD | 7,590,000.00 USD | 34,240.00 USD | 8,700.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 9,170,000.00 USD | 9,170,000.00 USD | 114,090.00 USD | 56,980.00 USD | 194,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 2,900.00 USD | 465,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 7,540,000.00 USD | 7,540,000.00 USD | 77,280.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 8,810,000.00 USD | 8,810,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,540.00 USD | 462,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 7,450,000.00 USD | 7,450,000.00 USD | 229,580.00 USD | 35,540.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 8,550,000.00 USD | 8,550,000.00 USD | 158,590.00 USD | 41,220.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 9,670.00 USD | 457,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 7,150,000.00 USD | 7,150,000.00 USD | 99,480.00 USD | 72,180.00 USD | 183,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 8,310,000.00 USD | 8,310,000.00 USD | 246,750.00 USD | 52,560.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 53,600.00 USD | 448,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 6,800,000.00 USD | 6,800,000.00 USD | 239,840.00 USD | 104,970.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 7,870,000.00 USD | 7,870,000.00 USD | 247,920.00 USD | 72,080.00 USD | 235,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 15,860.00 USD | 394,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 6,250,000.00 USD | 6,250,000.00 USD | 226,440.00 USD | 80,880.00 USD | 90,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 7,320,000.00 USD | 7,320,000.00 USD | 258,450.00 USD | 86,060.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 28,620.00 USD | 378,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 5,850,000.00 USD | 5,850,000.00 USD | 487,190.00 USD | 117,630.00 USD | 185,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 6,960,000.00 USD | 6,960,000.00 USD | 257,730.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 49,940.00 USD | 350,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 5,060,000.00 USD | 5,060,000.00 USD | 323,520.00 USD | 223,980.00 USD | 496,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 6,550,000.00 USD | 6,550,000.00 USD | 722,350.00 USD | 159,940.00 USD | 323,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 289,840.00 USD | 300,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 4,020,000.00 USD | 4,020,000.00 USD | 625,020.00 USD | 279,520.00 USD | 656,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 5,340,000.00 USD | 5,340,000.00 USD | 678,880.00 USD | 259,610.00 USD | 823,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 9,260.00 USD | 10,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 2,460,000.00 USD | 2,460,000.00 USD | 519,790.00 USD | 188,170.00 USD | 231,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 3,580,000.00 USD | 3,580,000.00 USD | 619,180.00 USD | 288,290.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 1,520,000.00 USD | 1,520,000.00 USD | 390,140.00 USD | 123,250.00 USD | 274,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 2,280,000.00 USD | 2,280,000.00 USD | 99,630.00 USD | 9,990.00 USD | 676,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1970` | 728,720.00 USD | 728,720.00 USD | 171,480.00 USD | 109,630.00 USD | 199,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 1,500,000.00 USD | 1,500,000.00 USD | 80,840.00 USD | 56,210.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 248,160.00 USD | 248,160.00 USD | 86,930.00 USD | 48,680.00 USD | 83,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 20,720.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 29,390.00 USD | 29,390.00 USD | 0.00 USD | 0.00 USD | 8,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 31,080.00 USD | 31,080.00 USD | 0.00 USD | 25,400.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 20,670.00 USD | 20,670.00 USD | 0.00 USD | 0.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 602,690.00 USD | 602,690.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 1,210,000.00 USD | 1,210,000.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 24,260.00 USD | 24,260.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 48,510.00 USD | 48,510.00 USD | 0.00 USD | 0.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 1,720,000.00 USD | 1,720,000.00 USD | 154,520.00 USD | 0.00 USD | 360,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 957,360.00 USD | 957,360.00 USD | 462,960.00 USD | 151,590.00 USD | 294,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 2,000,000.00 USD | 2,000,000.00 USD | 173,570.00 USD | 109,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 1,980,000.00 USD | 1,980,000.00 USD | 541,580.00 USD | 159,880.00 USD | 324,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 2,400,000.00 USD | 2,400,000.00 USD | 125,120.00 USD | 53,690.00 USD | 215,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 2,930,000.00 USD | 2,930,000.00 USD | 292,740.00 USD | 179,100.00 USD | 474,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 3,000,000.00 USD | 3,000,000.00 USD | 276,760.00 USD | 82,430.00 USD | 242,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2055` | 411.41 USD | 411.41 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2060` | 3,830,000.00 USD | 3,830,000.00 USD | 411,120.00 USD | 156,250.00 USD | 334,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 3,380,000.00 USD | 3,380,000.00 USD | 144,470.00 USD | 31,310.00 USD | 206,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2065` | 4,260.00 USD | 4,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2070` | 4,640,000.00 USD | 4,640,000.00 USD | 509,340.00 USD | 106,370.00 USD | 188,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 3,910,000.00 USD | 3,910,000.00 USD | 385,560.00 USD | 80,540.00 USD | 58,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 5,260,000.00 USD | 5,260,000.00 USD | 341,010.00 USD | 104,430.00 USD | 182,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 4,570,000.00 USD | 4,570,000.00 USD | 552,200.00 USD | 44,630.00 USD | 65,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2085` | 2,210.00 USD | 6,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2090` | 5,770,000.00 USD | 5,770,000.00 USD | 258,680.00 USD | 110,830.00 USD | 139,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 6,820,000.00 USD | 6,820,000.00 USD | 2,010,000.00 USD | 87,520.00 USD | 155,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2095` | 6,720.00 USD | 13,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2100` | 6,960,000.00 USD | 6,960,000.00 USD | 373,660.00 USD | 222,720.00 USD | 587,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 10,610,000.00 USD | 10,610,000.00 USD | 1,560,000.00 USD | 660,820.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2105` | 1,330.00 USD | 14,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2110` | 7,480,000.00 USD | 7,480,000.00 USD | 291,750.00 USD | 72,130.00 USD | 161,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 13,600,000.00 USD | 13,600,000.00 USD | 1,030,000.00 USD | 499,260.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 7,820,000.00 USD | 7,820,000.00 USD | 232,870.00 USD | 48,690.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 16,490,000.00 USD | 16,490,000.00 USD | 1,120,000.00 USD | 463,080.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 8,230,000.00 USD | 8,230,000.00 USD | 198,160.00 USD | 63,370.00 USD | 143,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 18,970,000.00 USD | 18,970,000.00 USD | 1,090,000.00 USD | 289,130.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 8,680,000.00 USD | 8,680,000.00 USD | 205,450.00 USD | 76,000.00 USD | 167,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 21,000,000.00 USD | 21,000,000.00 USD | 820,780.00 USD | 379,940.00 USD | 830,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 8,810,000.00 USD | 8,810,000.00 USD | 58,150.00 USD | 16,520.00 USD | 56,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 23,230,000.00 USD | 23,230,000.00 USD | 916,150.00 USD | 316,800.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 322.82 USD | 15,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 8,940,000.00 USD | 8,940,000.00 USD | 115,260.00 USD | 15,680.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 24,240,000.00 USD | 24,240,000.00 USD | 447,110.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 9,160,000.00 USD | 9,160,000.00 USD | 70,840.00 USD | 28,410.00 USD | 114,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,870,000.00 USD | 24,870,000.00 USD | 296,410.00 USD | 94,900.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2180` | 9,320,000.00 USD | 9,320,000.00 USD | 75,700.00 USD | 29,740.00 USD | 62,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 25,390,000.00 USD | 25,390,000.00 USD | 266,770.00 USD | 102,870.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 34,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 9,450,000.00 USD | 9,450,000.00 USD | 70,150.00 USD | 26,400.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 26,600,000.00 USD | 26,600,000.00 USD | 630,760.00 USD | 188,070.00 USD | 391,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 9,600,000.00 USD | 9,600,000.00 USD | 80,740.00 USD | 24,090.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 27,920,000.00 USD | 27,920,000.00 USD | 558,280.00 USD | 232,970.00 USD | 526,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 9,720,000.00 USD | 9,720,000.00 USD | 55,260.00 USD | 23,800.00 USD | 37,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 28,950,000.00 USD | 28,950,000.00 USD | 532,080.00 USD | 84,700.00 USD | 416,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 35,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 9,870,000.00 USD | 9,870,000.00 USD | 52,440.00 USD | 19,700.00 USD | 82,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 29,420,000.00 USD | 29,420,000.00 USD | 188,710.00 USD | 86,520.00 USD | 195,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2225` | 124.82 USD | 35,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2230` | 9,940,000.00 USD | 9,940,000.00 USD | 46,100.00 USD | 11,060.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 29,710,000.00 USD | 29,710,000.00 USD | 149,810.00 USD | 47,320.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 36,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2265` | 759.91 USD | 36,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 46,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2295` | 634.57 USD | 46,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 47,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 54,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 56,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 2,310.00 USD | 58,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2495` | 128.74 USD | 58,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,730.00 USD | 87,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2555` | 122.64 USD | 87,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 87,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 89,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2705` | 120.64 USD | 89,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 89,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2815` | 177.91 USD | 89,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2825` | 2,610.00 USD | 92,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 94,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 112,420.00 USD | 207,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 210,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 210,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 8,560.00 USD | 219,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2975` | 135,850.00 USD | 355,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 355,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 2,410.00 USD | 357,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 898.17 USD | 358,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 96,880.00 USD | 455,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 114.32 USD | 455,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3125` | 285.94 USD | 456,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 3,160.00 USD | 459,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3165` | 4,270.00 USD | 463,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 190.54 USD | 463,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 162.77 USD | 463,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 466,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3315` | 3,500.00 USD | 469,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3355` | 2,520.00 USD | 472,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3365` | 748.71 USD | 472,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3375` | 87,120.00 USD | 560,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3485` | 2,370.00 USD | 562,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3635` | 26,880.00 USD | 589,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3675` | 147.37 USD | 589,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 18,170.00 USD | 607,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3725` | 353.88 USD | 608,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 4,740.00 USD | 612,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3755` | 144.94 USD | 612,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 277,130.00 USD | 890,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 2,350,000.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3925` | 26,120.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3935` | 280.17 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3945` | 8,580.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3995` | 534.53 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4045` | 1,030.00 USD | 3,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0475` | 2,700,000.00 USD | 0.00 USD | 235.98 USD | `-76.49%` | `4,968.00` |
| `Live` | `Long` | `0.0525` | 2,700,000.00 USD | 0.00 USD | 5,510.00 USD | `-74.02%` | `105,008.00` |
| `Live` | `Long` | `0.0535` | 2,700,000.00 USD | 0.00 USD | 481.50 USD | `-73.52%` | `9,000.00` |
| `Live` | `Long` | `0.0545` | 2,700,000.00 USD | 0.00 USD | 139.57 USD | `-73.03%` | `2,561.00` |
| `Live` | `Long` | `0.0575` | 2,700,000.00 USD | 0.00 USD | 2,270.00 USD | `-71.54%` | `39,410.00` |
| `Live` | `Long` | `0.0605` | 2,690,000.00 USD | 0.00 USD | 945.49 USD | `-70.06%` | `15,628.00` |
| `Live` | `Long` | `0.0685` | 2,690,000.00 USD | 0.00 USD | 128,350.00 USD | `-66.10%` | `1,873,703.00` |
| `Live` | `Long` | `0.0715` | 2,560,000.00 USD | 0.00 USD | 752.61 USD | `-64.61%` | `10,526.00` |
| `Live` | `Long` | `0.0735` | 2,560,000.00 USD | 0.00 USD | 1,470.00 USD | `-63.62%` | `20,000.00` |
| `Live` | `Long` | `0.0775` | 2,560,000.00 USD | 0.00 USD | 659.99 USD | `-61.64%` | `8,516.00` |
| `Live` | `Long` | `0.0815` | 2,560,000.00 USD | 0.00 USD | 11,840.00 USD | `-59.66%` | `145,239.00` |
| `Live` | `Long` | `0.0865` | 2,550,000.00 USD | 0.00 USD | 967.50 USD | `-57.19%` | `11,185.00` |
| `Live` | `Long` | `0.0875` | 2,550,000.00 USD | 0.00 USD | 344.75 USD | `-56.69%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,550,000.00 USD | 0.00 USD | 1,150.00 USD | `-56.20%` | `13,050.00` |
| `Live` | `Long` | `0.0925` | 2,550,000.00 USD | 0.00 USD | 165.11 USD | `-54.22%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,550,000.00 USD | 0.00 USD | 327.54 USD | `-53.23%` | `3,466.00` |
| `Live` | `Long` | `0.0995` | 2,550,000.00 USD | 0.00 USD | 110,400.00 USD | `-50.75%` | `1,109,581.00` |
| `Live` | `Long` | `0.1025` | 2,440,000.00 USD | 0.00 USD | 4,100.00 USD | `-49.27%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-48.78%` | `10,149.00` |
| `Live` | `Long` | `0.1045` | 2,430,000.00 USD | 0.00 USD | 331.06 USD | `-48.28%` | `3,168.00` |
| `Live` | `Long` | `0.1065` | 2,430,000.00 USD | 0.00 USD | 890.98 USD | `-47.29%` | `8,366.00` |
| `Live` | `Long` | `0.1085` | 2,430,000.00 USD | 0.00 USD | 942.00 USD | `-46.30%` | `8,682.00` |
| `Live` | `Long` | `0.1095` | 2,430,000.00 USD | 0.00 USD | 1,490.00 USD | `-45.81%` | `13,608.00` |
| `Live` | `Long` | `0.1145` | 2,430,000.00 USD | 0.00 USD | 862.64 USD | `-43.33%` | `7,534.00` |
| `Live` | `Long` | `0.1165` | 2,430,000.00 USD | 0.00 USD | 13,360.00 USD | `-42.34%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,410,000.00 USD | 0.00 USD | 931.42 USD | `-41.85%` | `7,927.00` |
| `Live` | `Long` | `0.1185` | 2,410,000.00 USD | 0.00 USD | 2,900.00 USD | `-41.35%` | `24,507.00` |
| `Live` | `Long` | `0.1205` | 2,410,000.00 USD | 0.00 USD | 826.27 USD | `-40.36%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,410,000.00 USD | 0.00 USD | 1,050.00 USD | `-39.87%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,410,000.00 USD | 0.00 USD | 125.97 USD | `-38.88%` | `1,020.00` |
| `Live` | `Long` | `0.1245` | 2,410,000.00 USD | 0.00 USD | 1,160.00 USD | `-38.38%` | `9,343.00` |
| `Live` | `Long` | `0.1255` | 2,410,000.00 USD | 0.00 USD | 1,980.00 USD | `-37.89%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,400,000.00 USD | 0.00 USD | 314.61 USD | `-37.39%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,400,000.00 USD | 0.00 USD | 1,890.00 USD | `-36.90%` | `14,843.00` |
| `Live` | `Long` | `0.1295` | 2,400,000.00 USD | 0.00 USD | 2,540.00 USD | `-35.91%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,400,000.00 USD | 0.00 USD | 290.36 USD | `-35.41%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,400,000.00 USD | 0.00 USD | 687.35 USD | `-34.92%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,400,000.00 USD | 0.00 USD | 7,300.00 USD | `-34.42%` | `55,083.00` |
| `Live` | `Long` | `0.1335` | 2,390,000.00 USD | 0.00 USD | 3,600.00 USD | `-33.93%` | `26,965.00` |
| `Live` | `Long` | `0.1355` | 2,390,000.00 USD | 0.00 USD | 106.64 USD | `-32.94%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,390,000.00 USD | 0.00 USD | 659.30 USD | `-32.44%` | `4,830.00` |
| `Live` | `Long` | `0.1395` | 2,390,000.00 USD | 0.00 USD | 2,810.00 USD | `-30.96%` | `20,162.00` |
| `Live` | `Long` | `0.1405` | 2,380,000.00 USD | 0.00 USD | 806.33 USD | `-30.46%` | `5,739.00` |
| `Live` | `Long` | `0.1415` | 2,380,000.00 USD | 0.00 USD | 10,000.00 USD | `-29.97%` | `70,670.00` |
| `Live` | `Long` | `0.1435` | 2,370,000.00 USD | 0.00 USD | 14,650.00 USD | `-28.98%` | `102,110.00` |
| `Live` | `Long` | `0.1445` | 2,360,000.00 USD | 0.00 USD | 2,500.00 USD | `-28.48%` | `17,302.00` |
| `Live` | `Long` | `0.1455` | 2,360,000.00 USD | 0.00 USD | 7,310.00 USD | `-27.99%` | `50,230.00` |
| `Live` | `Long` | `0.1465` | 2,350,000.00 USD | 0.00 USD | 4,580.00 USD | `-27.49%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,340,000.00 USD | 0.00 USD | 1,800.00 USD | `-27.00%` | `12,201.00` |
| `Live` | `Long` | `0.1485` | 2,340,000.00 USD | 0.00 USD | 163.65 USD | `-26.50%` | `1,102.00` |
| `Live` | `Long` | `0.1495` | 2,340,000.00 USD | 0.00 USD | 599.05 USD | `-26.01%` | `4,007.00` |
| `Live` | `Long` | `0.1505` | 2,340,000.00 USD | 0.00 USD | 144.33 USD | `-25.51%` | `959.00` |
| `Live` | `Long` | `0.1515` | 2,340,000.00 USD | 0.00 USD | 33,400.00 USD | `-25.02%` | `220,430.00` |
| `Live` | `Long` | `0.1525` | 2,310,000.00 USD | 0.00 USD | 981.95 USD | `-24.52%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 2,310,000.00 USD | 0.00 USD | 42,640.00 USD | `-24.03%` | `277,811.00` |
| `Live` | `Long` | `0.1545` | 2,260,000.00 USD | 0.00 USD | 838.47 USD | `-23.53%` | `5,427.00` |
| `Live` | `Long` | `0.1555` | 2,260,000.00 USD | 0.00 USD | 16,490.00 USD | `-23.04%` | `106,025.00` |
| `Live` | `Long` | `0.1565` | 2,250,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.54%` | `10,116.00` |
| `Live` | `Long` | `0.1575` | 2,240,000.00 USD | 0.00 USD | 532,050.00 USD | `-22.05%` | `3,378,082.00` |
| `Live` | `Long` | `0.1585` | 1,710,000.00 USD | 0.00 USD | 6,000.00 USD | `-21.55%` | `37,842.00` |
| `Live` | `Long` | `0.1595` | 1,710,000.00 USD | 0.00 USD | 4,070.00 USD | `-21.06%` | `25,519.00` |
| `Live` | `Long` | `0.1605` | 1,700,000.00 USD | 0.00 USD | 57,310.00 USD | `-20.56%` | `357,091.00` |
| `Live` | `Long` | `0.1615` | 1,650,000.00 USD | 0.00 USD | 5,850.00 USD | `-20.07%` | `36,207.00` |
| `Live` | `Long` | `0.1625` | 1,640,000.00 USD | 0.00 USD | 3,500.00 USD | `-19.57%` | `21,519.00` |
| `Live` | `Long` | `0.1645` | 1,640,000.00 USD | 0.00 USD | 12,040.00 USD | `-18.58%` | `73,221.00` |
| `Live` | `Long` | `0.1655` | 1,620,000.00 USD | 0.00 USD | 356.65 USD | `-18.09%` | `2,155.00` |
| `Live` | `Long` | `0.1665` | 1,620,000.00 USD | 0.00 USD | 35,330.00 USD | `-17.59%` | `212,180.00` |
| `Live` | `Long` | `0.1675` | 1,590,000.00 USD | 0.00 USD | 630.81 USD | `-17.10%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,590,000.00 USD | 0.00 USD | 1,750.00 USD | `-16.60%` | `10,397.00` |
| `Live` | `Long` | `0.1695` | 1,590,000.00 USD | 0.00 USD | 511.21 USD | `-16.11%` | `3,016.00` |
| `Live` | `Long` | `0.1705` | 1,590,000.00 USD | 0.00 USD | 619,830.00 USD | `-15.61%` | `3,635,347.00` |
| `Live` | `Long` | `0.1715` | 965,490.00 USD | 0.00 USD | 254,680.00 USD | `-15.12%` | `1,485,005.00` |
| `Live` | `Long` | `0.1735` | 710,810.00 USD | 0.00 USD | 3,340.00 USD | `-14.13%` | `19,230.00` |
| `Live` | `Long` | `0.1745` | 707,470.00 USD | 0.00 USD | 1,320.00 USD | `-13.64%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 706,150.00 USD | 0.00 USD | 4,720.00 USD | `-13.14%` | `26,871.00` |
| `Live` | `Long` | `0.1765` | 701,440.00 USD | 0.00 USD | 4,580.00 USD | `-12.65%` | `25,953.00` |
| `Live` | `Long` | `0.1775` | 696,860.00 USD | 0.00 USD | 15,750.00 USD | `-12.15%` | `88,754.00` |
| `Live` | `Long` | `0.1785` | 681,100.00 USD | 0.00 USD | 38,210.00 USD | `-11.66%` | `214,064.00` |
| `Live` | `Long` | `0.1795` | 642,890.00 USD | 0.00 USD | 11,150.00 USD | `-11.16%` | `62,104.00` |
| `Live` | `Long` | `0.1805` | 631,750.00 USD | 0.00 USD | 135,130.00 USD | `-10.67%` | `748,623.00` |
| `Live` | `Long` | `0.1815` | 496,620.00 USD | 0.00 USD | 7,670.00 USD | `-10.17%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 488,950.00 USD | 0.00 USD | 18,250.00 USD | `-9.68%` | `100,000.00` |
| `Live` | `Long` | `0.1835` | 470,700.00 USD | 0.00 USD | 367.00 USD | `-9.18%` | `2,000.00` |
| `Live` | `Long` | `0.1845` | 470,340.00 USD | 0.00 USD | 956.45 USD | `-8.69%` | `5,184.00` |
| `Live` | `Long` | `0.1855` | 469,380.00 USD | 0.00 USD | 4,100.00 USD | `-8.19%` | `22,111.00` |
| `Live` | `Long` | `0.1865` | 465,280.00 USD | 0.00 USD | 2,900.00 USD | `-7.70%` | `15,565.00` |
| `Live` | `Long` | `0.1875` | 462,380.00 USD | 0.00 USD | 4,540.00 USD | `-7.20%` | `24,200.00` |
| `Live` | `Long` | `0.1885` | 457,840.00 USD | 0.00 USD | 9,670.00 USD | `-6.71%` | `51,278.00` |
| `Live` | `Long` | `0.1895` | 448,170.00 USD | 0.00 USD | 53,600.00 USD | `-6.21%` | `282,867.00` |
| `Live` | `Long` | `0.1905` | 394,570.00 USD | 0.00 USD | 15,860.00 USD | `-5.72%` | `83,262.00` |
| `Live` | `Long` | `0.1915` | 378,710.00 USD | 0.00 USD | 28,620.00 USD | `-5.22%` | `149,454.00` |
| `Live` | `Long` | `0.1925` | 350,090.00 USD | 0.00 USD | 49,940.00 USD | `-4.73%` | `259,448.00` |
| `Live` | `Long` | `0.1935` | 300,140.00 USD | 0.00 USD | 289,840.00 USD | `-4.23%` | `1,497,885.00` |
| `Live` | `Long` | `0.1945` | 10,300.00 USD | 0.00 USD | 9,260.00 USD | `-3.74%` | `47,614.00` |
| `Live` | `Long` | `0.1955` | 1,040.00 USD | 0.00 USD | 1,040.00 USD | `-3.24%` | `5,327.00` |
| `Live` | `Short` | `0.2055` | 411.41 USD | 411.41 USD | 0.00 USD | `+1.71%` | `2,002.00` |
| `Live` | `Short` | `0.2065` | 4,670.00 USD | 4,260.00 USD | 0.00 USD | `+2.20%` | `20,616.00` |
| `Live` | `Short` | `0.2085` | 6,880.00 USD | 2,210.00 USD | 0.00 USD | `+3.19%` | `10,601.00` |
| `Live` | `Short` | `0.2095` | 13,600.00 USD | 6,720.00 USD | 0.00 USD | `+3.69%` | `32,100.00` |
| `Live` | `Short` | `0.2105` | 14,940.00 USD | 1,330.00 USD | 0.00 USD | `+4.18%` | `6,324.00` |
| `Live` | `Short` | `0.2155` | 15,260.00 USD | 322.82 USD | 0.00 USD | `+6.66%` | `1,498.00` |
| `Live` | `Short` | `0.2185` | 34,160.00 USD | 18,910.00 USD | 0.00 USD | `+8.14%` | `86,525.00` |
| `Live` | `Short` | `0.2215` | 35,810.00 USD | 1,640.00 USD | 0.00 USD | `+9.63%` | `7,424.00` |
| `Live` | `Short` | `0.2225` | 35,930.00 USD | 124.82 USD | 0.00 USD | `+10.12%` | `561.00` |
| `Live` | `Short` | `0.2235` | 36,130.00 USD | 200.48 USD | 0.00 USD | `+10.62%` | `897.00` |
| `Live` | `Short` | `0.2265` | 36,890.00 USD | 759.91 USD | 0.00 USD | `+12.10%` | `3,355.00` |
| `Live` | `Short` | `0.2285` | 46,130.00 USD | 9,240.00 USD | 0.00 USD | `+13.09%` | `40,428.00` |
| `Live` | `Short` | `0.2295` | 46,770.00 USD | 634.57 USD | 0.00 USD | `+13.59%` | `2,765.00` |
| `Live` | `Short` | `0.2325` | 47,050.00 USD | 282.02 USD | 0.00 USD | `+15.07%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 54,680.00 USD | 7,640.00 USD | 0.00 USD | `+15.57%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 56,150.00 USD | 1,470.00 USD | 0.00 USD | `+19.03%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 58,470.00 USD | 2,310.00 USD | 0.00 USD | `+19.52%` | `9,579.00` |
| `Live` | `Short` | `0.2495` | 58,600.00 USD | 128.74 USD | 0.00 USD | `+23.48%` | `516.00` |
| `Live` | `Short` | `0.2525` | 87,330.00 USD | 28,730.00 USD | 0.00 USD | `+24.97%` | `113,787.00` |
| `Live` | `Short` | `0.2555` | 87,450.00 USD | 122.64 USD | 0.00 USD | `+26.45%` | `480.00` |
| `Live` | `Short` | `0.2585` | 87,830.00 USD | 380.25 USD | 0.00 USD | `+27.94%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 89,230.00 USD | 1,400.00 USD | 0.00 USD | `+29.42%` | `5,346.00` |
| `Live` | `Short` | `0.2705` | 89,350.00 USD | 120.64 USD | 0.00 USD | `+33.88%` | `446.00` |
| `Live` | `Short` | `0.2775` | 89,730.00 USD | 379.62 USD | 0.00 USD | `+37.34%` | `1,368.00` |
| `Live` | `Short` | `0.2815` | 89,910.00 USD | 177.91 USD | 0.00 USD | `+39.32%` | `632.00` |
| `Live` | `Short` | `0.2825` | 92,510.00 USD | 2,610.00 USD | 0.00 USD | `+39.82%` | `9,222.00` |
| `Live` | `Short` | `0.2845` | 94,690.00 USD | 2,170.00 USD | 0.00 USD | `+40.81%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 207,100.00 USD | 112,420.00 USD | 0.00 USD | `+43.28%` | `388,319.00` |
| `Live` | `Short` | `0.2915` | 210,370.00 USD | 3,260.00 USD | 0.00 USD | `+44.27%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 210,890.00 USD | 519.79 USD | 0.00 USD | `+45.26%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 219,440.00 USD | 8,560.00 USD | 0.00 USD | `+46.25%` | `28,961.00` |
| `Live` | `Short` | `0.2975` | 355,290.00 USD | 135,850.00 USD | 0.00 USD | `+47.24%` | `456,623.00` |
| `Live` | `Short` | `0.3005` | 355,440.00 USD | 146.34 USD | 0.00 USD | `+48.73%` | `487.00` |
| `Live` | `Short` | `0.3045` | 357,840.00 USD | 2,410.00 USD | 0.00 USD | `+50.71%` | `7,906.00` |
| `Live` | `Short` | `0.3055` | 358,740.00 USD | 898.17 USD | 0.00 USD | `+51.20%` | `2,940.00` |
| `Live` | `Short` | `0.3105` | 455,620.00 USD | 96,880.00 USD | 0.00 USD | `+53.67%` | `312,021.00` |
| `Live` | `Short` | `0.3115` | 455,740.00 USD | 114.32 USD | 0.00 USD | `+54.17%` | `367.00` |
| `Live` | `Short` | `0.3125` | 456,020.00 USD | 285.94 USD | 0.00 USD | `+54.66%` | `915.00` |
| `Live` | `Short` | `0.3145` | 459,180.00 USD | 3,160.00 USD | 0.00 USD | `+55.65%` | `10,035.00` |
| `Live` | `Short` | `0.3165` | 463,450.00 USD | 4,270.00 USD | 0.00 USD | `+56.64%` | `13,504.00` |
| `Live` | `Short` | `0.3235` | 463,650.00 USD | 190.54 USD | 0.00 USD | `+60.11%` | `589.00` |
| `Live` | `Short` | `0.3275` | 463,810.00 USD | 162.77 USD | 0.00 USD | `+62.09%` | `497.00` |
| `Live` | `Short` | `0.3295` | 466,190.00 USD | 2,380.00 USD | 0.00 USD | `+63.08%` | `7,219.00` |
| `Live` | `Short` | `0.3315` | 469,690.00 USD | 3,500.00 USD | 0.00 USD | `+64.07%` | `10,571.00` |
| `Live` | `Short` | `0.3355` | 472,210.00 USD | 2,520.00 USD | 0.00 USD | `+66.05%` | `7,515.00` |
| `Live` | `Short` | `0.3365` | 472,960.00 USD | 748.71 USD | 0.00 USD | `+66.54%` | `2,225.00` |
| `Live` | `Short` | `0.3375` | 560,080.00 USD | 87,120.00 USD | 0.00 USD | `+67.04%` | `258,141.00` |
| `Live` | `Short` | `0.3485` | 562,450.00 USD | 2,370.00 USD | 0.00 USD | `+72.48%` | `6,797.00` |
| `Live` | `Short` | `0.3635` | 589,340.00 USD | 26,880.00 USD | 0.00 USD | `+79.91%` | `73,959.00` |
| `Live` | `Short` | `0.3675` | 589,480.00 USD | 147.37 USD | 0.00 USD | `+81.89%` | `401.00` |
| `Live` | `Short` | `0.3715` | 607,650.00 USD | 18,170.00 USD | 0.00 USD | `+83.87%` | `48,905.00` |
| `Live` | `Short` | `0.3725` | 608,010.00 USD | 353.88 USD | 0.00 USD | `+84.36%` | `950.00` |
| `Live` | `Short` | `0.3745` | 612,740.00 USD | 4,740.00 USD | 0.00 USD | `+85.35%` | `12,649.00` |
| `Live` | `Short` | `0.3755` | 612,890.00 USD | 144.94 USD | 0.00 USD | `+85.85%` | `386.00` |
| `Live` | `Short` | `0.3845` | 890,020.00 USD | 277,130.00 USD | 0.00 USD | `+90.30%` | `720,753.00` |
| `Live` | `Short` | `0.3915` | 3,240,000.00 USD | 2,350,000.00 USD | 0.00 USD | `+93.76%` | `6,000,827.00` |
| `Live` | `Short` | `0.3925` | 3,270,000.00 USD | 26,120.00 USD | 0.00 USD | `+94.26%` | `66,555.00` |
| `Live` | `Short` | `0.3935` | 3,270,000.00 USD | 280.17 USD | 0.00 USD | `+94.75%` | `712.00` |
| `Live` | `Short` | `0.3945` | 3,270,000.00 USD | 8,580.00 USD | 0.00 USD | `+95.25%` | `21,752.00` |
| `Live` | `Short` | `0.3995` | 3,270,000.00 USD | 534.53 USD | 0.00 USD | `+97.72%` | `1,338.00` |
| `Live` | `Short` | `0.4045` | 3,280,000.00 USD | 1,030.00 USD | 0.00 USD | `+100.20%` | `2,543.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 639,290,000.00 USD | 0.00 USD | 415.13 USD | `-70.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0615` | 639,290,000.00 USD | 0.00 USD | 463.46 USD | `-69.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 639,290,000.00 USD | 0.00 USD | 1,100.00 USD | `-45.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 639,290,000.00 USD | 0.00 USD | 541.33 USD | `-44.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 639,290,000.00 USD | 0.00 USD | 602,500.00 USD | `-40.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 638,690,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 638,680,000.00 USD | 0.00 USD | 13,390.00 USD | `-35.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 638,670,000.00 USD | 0.00 USD | 728.88 USD | `-34.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 638,670,000.00 USD | 0.00 USD | 4,350.00 USD | `-33.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 638,670,000.00 USD | 0.00 USD | 542.99 USD | `-31.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 638,670,000.00 USD | 0.00 USD | 1,820.00 USD | `-30.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 638,660,000.00 USD | 0.00 USD | 1,050.00 USD | `-29.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 638,660,000.00 USD | 0.00 USD | 2,110.00 USD | `-29.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 638,660,000.00 USD | 0.00 USD | 1,600.00 USD | `-28.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 638,660,000.00 USD | 0.00 USD | 4,580.00 USD | `-27.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 638,650,000.00 USD | 0.00 USD | 303.26 USD | `-25.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 638,650,000.00 USD | 0.00 USD | 1,290.00 USD | `-25.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 638,650,000.00 USD | 0.00 USD | 279.53 USD | `-24.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 638,650,000.00 USD | 0.00 USD | 324.30 USD | `-23.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 638,650,000.00 USD | 0.00 USD | 818.86 USD | `-23.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 638,650,000.00 USD | 0.00 USD | 552.21 USD | `-21.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 638,650,000.00 USD | 0.00 USD | 13,660.00 USD | `-21.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 638,640,000.00 USD | 0.00 USD | 2,990.00 USD | `-20.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 638,630,000.00 USD | 0.00 USD | 562.67 USD | `-20.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 638,630,000.00 USD | 0.00 USD | 18,260.00 USD | `-19.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 638,620,000.00 USD | 0.00 USD | 6,540.00 USD | `-19.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 638,610,000.00 USD | 0.00 USD | 2,870.00 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 638,610,000.00 USD | 0.00 USD | 452.97 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 638,610,000.00 USD | 0.00 USD | 6,660.00 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 638,600,000.00 USD | 0.00 USD | 7,020.00 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 638,590,000.00 USD | 0.00 USD | 6,740.00 USD | `-16.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 638,590,000.00 USD | 0.00 USD | 4,270.00 USD | `-16.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 638,580,000.00 USD | 0.00 USD | 813.97 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 638,580,000.00 USD | 0.00 USD | 6,860.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 638,570,000.00 USD | 0.00 USD | 6,900.00 USD | `-14.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 638,570,000.00 USD | 0.00 USD | 103.58 USD | `-14.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 638,570,000.00 USD | 0.00 USD | 1,240.00 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 638,570,000.00 USD | 0.00 USD | 8,780.00 USD | `-13.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 638,560,000.00 USD | 0.00 USD | 623.57 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 638,560,000.00 USD | 0.00 USD | 4,440.00 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 638,550,000.00 USD | 0.00 USD | 5,250.00 USD | `-11.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 638,550,000.00 USD | 0.00 USD | 5,760.00 USD | `-11.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 638,540,000.00 USD | 0.00 USD | 26,930.00 USD | `-10.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 638,510,000.00 USD | 0.00 USD | 2,400.00 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 638,510,000.00 USD | 0.00 USD | 2,190.00 USD | `-9.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 638,510,000.00 USD | 0.00 USD | 3,160.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 638,510,000.00 USD | 0.00 USD | 18,650.00 USD | `-8.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 638,490,000.00 USD | 0.00 USD | 282.33 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 638,490,000.00 USD | 0.00 USD | 486.39 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 638,490,000.00 USD | 0.00 USD | 109.69 USD | `-7.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 638,490,000.00 USD | 0.00 USD | 7,190.00 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 638,480,000.00 USD | 0.00 USD | 837.40 USD | `-6.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 638,480,000.00 USD | 0.00 USD | 16,820.00 USD | `-5.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 638,460,000.00 USD | 0.00 USD | 1,290.00 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 638,460,000.00 USD | 0.00 USD | 211.37 USD | `-4.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 638,460,000.00 USD | 0.00 USD | 2,100.00 USD | `-4.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 638,460,000.00 USD | 0.00 USD | 3,010.00 USD | `-3.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 638,450,000.00 USD | 0.00 USD | 2,050.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 638,450,000.00 USD | 0.00 USD | 1,490.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 638,450,000.00 USD | 0.00 USD | 79,000,000.00 USD | `-2.25%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 559,450,000.00 USD | 0.00 USD | 79,450,000.00 USD | `-1.76%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 480,000,000.00 USD | 0.00 USD | 319,200,000.00 USD | `-1.26%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 160,800,000.00 USD | 0.00 USD | 80,200,000.00 USD | `-0.77%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 80,600,000.00 USD | 0.00 USD | 80,600,000.00 USD | `-0.27%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2025` | 763.83 USD | 763.83 USD | 0.00 USD | `+0.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 3,720.00 USD | 2,960.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 13,250.00 USD | 9,520.00 USD | 0.00 USD | `+1.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 18,230.00 USD | 4,980.00 USD | 0.00 USD | `+1.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 19,280.00 USD | 1,050.00 USD | 0.00 USD | `+2.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 26,280.00 USD | 7,010.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 29,830.00 USD | 3,540.00 USD | 0.00 USD | `+3.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 89,550.00 USD | 59,730.00 USD | 0.00 USD | `+3.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 120,300.00 USD | 30,750.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 123,840.00 USD | 3,540.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 127,150.00 USD | 3,310.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 137,590.00 USD | 10,450.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 140,050.00 USD | 2,460.00 USD | 0.00 USD | `+6.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 142,650.00 USD | 2,600.00 USD | 0.00 USD | `+6.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 142,760.00 USD | 109.77 USD | 0.00 USD | `+7.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 142,870.00 USD | 109.91 USD | 0.00 USD | `+8.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 144,340.00 USD | 1,470.00 USD | 0.00 USD | `+8.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 403,760.00 USD | 259,420.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 405,400.00 USD | 1,650.00 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 407,100.00 USD | 1,690.00 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 407,600.00 USD | 501.31 USD | 0.00 USD | `+10.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 415,400.00 USD | 7,810.00 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 415,610.00 USD | 202.27 USD | 0.00 USD | `+11.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 415,720.00 USD | 109.40 USD | 0.00 USD | `+12.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 424,860.00 USD | 9,140.00 USD | 0.00 USD | `+13.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 434,040.00 USD | 9,180.00 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 434,700.00 USD | 662.92 USD | 0.00 USD | `+14.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 435,040.00 USD | 337.06 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 444,510.00 USD | 9,470.00 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 453,850.00 USD | 9,340.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 454,850.00 USD | 1,010.00 USD | 0.00 USD | `+16.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 464,870.00 USD | 10,020.00 USD | 0.00 USD | `+17.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 465,520.00 USD | 650.04 USD | 0.00 USD | `+17.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 465,710.00 USD | 192.71 USD | 0.00 USD | `+18.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 468,750.00 USD | 3,040.00 USD | 0.00 USD | `+18.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 478,580.00 USD | 9,830.00 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 478,690.00 USD | 115.92 USD | 0.00 USD | `+19.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 489,620.00 USD | 10,930.00 USD | 0.00 USD | `+21.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 489,910.00 USD | 288.22 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 490,400.00 USD | 491.03 USD | 0.00 USD | `+22.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 491,720.00 USD | 1,320.00 USD | 0.00 USD | `+22.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 492,420.00 USD | 693.07 USD | 0.00 USD | `+22.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 492,910.00 USD | 499.00 USD | 0.00 USD | `+23.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 494,010.00 USD | 1,100.00 USD | 0.00 USD | `+23.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 494,180.00 USD | 168.76 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 494,790.00 USD | 603.73 USD | 0.00 USD | `+24.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 496,960.00 USD | 2,170.00 USD | 0.00 USD | `+25.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 498,530.00 USD | 1,570.00 USD | 0.00 USD | `+26.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 500,000.00 USD | 1,470.00 USD | 0.00 USD | `+27.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 500,270.00 USD | 271.44 USD | 0.00 USD | `+28.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 921,700.00 USD | 421,430.00 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 922,650.00 USD | 945.98 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 931,540.00 USD | 8,890.00 USD | 0.00 USD | `+32.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 946,410.00 USD | 14,860.00 USD | 0.00 USD | `+32.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 951,030.00 USD | 4,620.00 USD | 0.00 USD | `+33.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 952,340.00 USD | 1,310.00 USD | 0.00 USD | `+34.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 966,210.00 USD | 13,870.00 USD | 0.00 USD | `+35.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 970,870.00 USD | 4,670.00 USD | 0.00 USD | `+35.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 971,820.00 USD | 944.99 USD | 0.00 USD | `+38.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 971,980.00 USD | 161.87 USD | 0.00 USD | `+39.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 972,520.00 USD | 542.34 USD | 0.00 USD | `+40.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 973,890.00 USD | 1,370.00 USD | 0.00 USD | `+40.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 974,970.00 USD | 1,080.00 USD | 0.00 USD | `+42.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 990,130.00 USD | 15,160.00 USD | 0.00 USD | `+43.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 990,930.00 USD | 796.09 USD | 0.00 USD | `+44.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 992,370.00 USD | 1,440.00 USD | 0.00 USD | `+47.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 992,730.00 USD | 355.21 USD | 0.00 USD | `+48.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 999,670.00 USD | 6,950.00 USD | 0.00 USD | `+48.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 1,020,000.00 USD | 18,980.00 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 1,020,000.00 USD | 4,150.00 USD | 0.00 USD | `+52.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 1,030,000.00 USD | 3,250.00 USD | 0.00 USD | `+55.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 1,030,000.00 USD | 5,090.00 USD | 0.00 USD | `+58.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 1,030,000.00 USD | 1,450.00 USD | 0.00 USD | `+60.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 1,030,000.00 USD | 181.30 USD | 0.00 USD | `+61.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 1,050,000.00 USD | 12,290.00 USD | 0.00 USD | `+64.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 1,050,000.00 USD | 111.06 USD | 0.00 USD | `+65.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 1,050,000.00 USD | 220.61 USD | 0.00 USD | `+69.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 1,050,000.00 USD | 3,850.00 USD | 0.00 USD | `+72.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 1,050,000.00 USD | 188.75 USD | 0.00 USD | `+86.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 1,050,000.00 USD | 121.76 USD | 0.00 USD | `+88.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 1,050,000.00 USD | 141.78 USD | 0.00 USD | `+92.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 1,050,000.00 USD | 393.50 USD | 0.00 USD | `+94.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 1,050,000.00 USD | 1,260.00 USD | 0.00 USD | `+95.25%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1770` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD |
| `7D` | `0.1780` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD |
| `7D` | `0.1790` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD |
| `7D` | `0.1800` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 8,510,000.00 USD | 0.00 USD | 8,510,000.00 USD | 118,290.00 USD | 70,090.00 USD | 113,060.00 USD |
| `7D` | `0.1810` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 112,560.00 USD | 27,510.00 USD | 31,310.00 USD |
| `1D` | `0.1820` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 53,260.00 USD | 21,110.00 USD | 75,700.00 USD |
| `7D` | `0.1820` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 95,280.00 USD | 47,480.00 USD | 117,770.00 USD |
| `1D` | `0.1830` | 8,060,000.00 USD | 0.00 USD | 8,060,000.00 USD | 48,990.00 USD | 11,640.00 USD | 15,420.00 USD |
| `7D` | `0.1830` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 84,560.00 USD | 36,880.00 USD | 59,960.00 USD |
| `1D` | `0.1840` | 7,980,000.00 USD | 0.00 USD | 7,980,000.00 USD | 80,720.00 USD | 17,960.00 USD | 17,730.00 USD |
| `7D` | `0.1840` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 226,530.00 USD | 58,050.00 USD | 174,570.00 USD |
| `1D` | `0.1850` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 103,680.00 USD | 35,330.00 USD | 67,220.00 USD |
| `7D` | `0.1850` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 404,170.00 USD | 111,470.00 USD | 387,400.00 USD |
| `1D` | `0.1860` | 7,660,000.00 USD | 0.00 USD | 7,660,000.00 USD | 34,240.00 USD | 8,700.00 USD | 12,970.00 USD |
| `7D` | `0.1860` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 114,090.00 USD | 56,980.00 USD | 194,130.00 USD |
| `1D` | `0.1870` | 7,610,000.00 USD | 0.00 USD | 7,610,000.00 USD | 77,280.00 USD | 5,970.00 USD | 664.17 USD |
| `7D` | `0.1870` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 231,610.00 USD | 34,960.00 USD | 33,870.00 USD |
| `7D` | `0.1880` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 158,590.00 USD | 41,220.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 7,220,000.00 USD | 0.00 USD | 7,220,000.00 USD | 99,480.00 USD | 72,180.00 USD | 183,960.00 USD |
| `7D` | `0.1890` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 246,750.00 USD | 52,560.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 239,840.00 USD | 104,970.00 USD | 203,200.00 USD |
| `7D` | `0.1900` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 247,920.00 USD | 72,080.00 USD | 235,020.00 USD |
| `1D` | `0.1910` | 6,320,000.00 USD | 0.00 USD | 6,320,000.00 USD | 226,440.00 USD | 80,880.00 USD | 91,380.00 USD |
| `7D` | `0.1910` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 258,450.00 USD | 86,060.00 USD | 16,510.00 USD |
| `1D` | `0.1920` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 489,900.00 USD | 116,840.00 USD | 182,570.00 USD |
| `7D` | `0.1920` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 257,730.00 USD | 74,890.00 USD | 77,590.00 USD |
| `1D` | `0.1930` | 5,130,000.00 USD | 0.00 USD | 5,130,000.00 USD | 328,820.00 USD | 223,980.00 USD | 497,620.00 USD |
| `7D` | `0.1930` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 722,350.00 USD | 159,940.00 USD | 323,790.00 USD |
| `1D` | `0.1940` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 644,680.00 USD | 280,880.00 USD | 639,490.00 USD |
| `7D` | `0.1940` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 678,880.00 USD | 259,610.00 USD | 823,650.00 USD |
| `1D` | `0.1950` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 519,790.00 USD | 188,170.00 USD | 232,610.00 USD |
| `7D` | `0.1950` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 619,180.00 USD | 288,290.00 USD | 388,420.00 USD |
| `1D` | `0.1960` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 390,140.00 USD | 123,250.00 USD | 274,240.00 USD |
| `7D` | `0.1960` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 99,630.00 USD | 9,990.00 USD | 676,700.00 USD |
| `1D` | `0.1970` | 785,850.00 USD | 0.00 USD | 785,850.00 USD | 182,100.00 USD | 109,630.00 USD | 191,350.00 USD |
| `7D` | `0.1970` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 80,840.00 USD | 56,210.00 USD | 133,500.00 USD |
| `1D` | `0.1980` | 302,770.00 USD | 0.00 USD | 302,770.00 USD | 126,240.00 USD | 57,150.00 USD | 80,470.00 USD |
| `7D` | `0.1980` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 20,720.00 USD | 1,190.00 USD |
| `7D` | `0.1990` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD |
| `1D` | `0.2000` | 38,910.00 USD | 0.00 USD | 38,910.00 USD | 0.00 USD | 0.00 USD | 13,640.00 USD |
| `7D` | `0.2000` | 31,080.00 USD | 0.00 USD | 31,080.00 USD | 0.00 USD | 25,400.00 USD | 5,680.00 USD |
| `1D` | `0.2010` | 25,270.00 USD | 0.00 USD | 25,270.00 USD | 0.00 USD | 0.00 USD | 25,270.00 USD |
| `7D` | `0.2010` | 602,690.00 USD | 602,690.00 USD | 0.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD |
| `7D` | `0.2010` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD |
| `1D` | `0.2020` | 19,440.00 USD | 19,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,440.00 USD |
| `1D` | `0.2020` | 38,870.00 USD | 38,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 19,440.00 USD |
| `7D` | `0.2020` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 154,520.00 USD | 0.00 USD | 360,160.00 USD |
| `1D` | `0.2030` | 945,220.00 USD | 945,220.00 USD | 0.00 USD | 462,960.00 USD | 151,590.00 USD | 291,790.00 USD |
| `7D` | `0.2030` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 173,570.00 USD | 109,540.00 USD | 0.00 USD |
| `1D` | `0.2040` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 541,580.00 USD | 159,880.00 USD | 324,990.00 USD |
| `7D` | `0.2040` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 125,120.00 USD | 53,690.00 USD | 215,230.00 USD |
| `1D` | `0.2050` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 303,360.00 USD | 179,100.00 USD | 474,370.00 USD |
| `7D` | `0.2050` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 276,760.00 USD | 82,430.00 USD | 242,780.00 USD |
| `1D` | `0.2060` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 450,430.00 USD | 164,720.00 USD | 325,340.00 USD |
| `7D` | `0.2060` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 144,470.00 USD | 31,310.00 USD | 206,030.00 USD |
| `1D` | `0.2070` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 509,340.00 USD | 106,370.00 USD | 189,010.00 USD |
| `7D` | `0.2070` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 385,560.00 USD | 80,540.00 USD | 58,420.00 USD |
| `1D` | `0.2080` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 341,010.00 USD | 104,430.00 USD | 179,000.00 USD |
| `7D` | `0.2080` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 552,200.00 USD | 44,630.00 USD | 65,200.00 USD |
| `1D` | `0.2090` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 263,990.00 USD | 110,830.00 USD | 134,950.00 USD |
| `7D` | `0.2090` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 2,010,000.00 USD | 87,520.00 USD | 155,450.00 USD |
| `1D` | `0.2100` | 6,990,000.00 USD | 6,990,000.00 USD | 0.00 USD | 393,310.00 USD | 224,090.00 USD | 563,200.00 USD |
| `7D` | `0.2100` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 1,560,000.00 USD | 660,820.00 USD | 1,570,000.00 USD |
| `1D` | `0.2110` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 291,750.00 USD | 72,130.00 USD | 158,880.00 USD |
| `7D` | `0.2110` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 1,030,000.00 USD | 499,260.00 USD | 1,460,000.00 USD |
| `1D` | `0.2120` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 235,580.00 USD | 47,910.00 USD | 64,580.00 USD |
| `7D` | `0.2120` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 1,120,000.00 USD | 463,080.00 USD | 1,320,000.00 USD |
| `1D` | `0.2130` | 8,270,000.00 USD | 8,270,000.00 USD | 0.00 USD | 198,160.00 USD | 63,370.00 USD | 144,890.00 USD |
| `7D` | `0.2130` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 1,090,000.00 USD | 289,130.00 USD | 1,100,000.00 USD |
| `1D` | `0.2140` | 8,710,000.00 USD | 8,710,000.00 USD | 0.00 USD | 205,450.00 USD | 76,000.00 USD | 165,050.00 USD |
| `7D` | `0.2140` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 820,780.00 USD | 379,940.00 USD | 830,800.00 USD |
| `1D` | `0.2150` | 8,840,000.00 USD | 8,840,000.00 USD | 0.00 USD | 58,150.00 USD | 16,520.00 USD | 54,520.00 USD |
| `7D` | `0.2150` | 23,230,000.00 USD | 23,230,000.00 USD | 0.00 USD | 916,150.00 USD | 316,800.00 USD | 1,000,000.00 USD |
| `1D` | `0.2160` | 8,980,000.00 USD | 8,980,000.00 USD | 0.00 USD | 117,290.00 USD | 15,090.00 USD | 2,910.00 USD |
| `7D` | `0.2160` | 24,240,000.00 USD | 24,240,000.00 USD | 0.00 USD | 447,110.00 USD | 164,960.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 9,190,000.00 USD | 9,190,000.00 USD | 0.00 USD | 70,840.00 USD | 28,410.00 USD | 115,120.00 USD |
| `7D` | `0.2170` | 24,870,000.00 USD | 24,870,000.00 USD | 0.00 USD | 296,410.00 USD | 94,900.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 9,360,000.00 USD | 9,360,000.00 USD | 0.00 USD | 75,700.00 USD | 29,740.00 USD | 63,110.00 USD |
| `7D` | `0.2180` | 25,390,000.00 USD | 25,390,000.00 USD | 0.00 USD | 266,770.00 USD | 102,870.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 70,150.00 USD | 26,400.00 USD | 33,840.00 USD |
| `7D` | `0.2190` | 26,600,000.00 USD | 26,600,000.00 USD | 0.00 USD | 630,760.00 USD | 188,070.00 USD | 391,710.00 USD |
| `1D` | `0.2200` | 9,640,000.00 USD | 9,640,000.00 USD | 0.00 USD | 80,740.00 USD | 24,090.00 USD | 41,470.00 USD |
| `7D` | `0.2200` | 27,920,000.00 USD | 27,920,000.00 USD | 0.00 USD | 558,280.00 USD | 232,970.00 USD | 526,970.00 USD |
| `1D` | `0.2210` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 55,260.00 USD | 23,800.00 USD | 37,750.00 USD |
| `7D` | `0.2210` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 532,080.00 USD | 84,700.00 USD | 416,740.00 USD |
| `1D` | `0.2220` | 9,910,000.00 USD | 9,910,000.00 USD | 0.00 USD | 57,240.00 USD | 21,110.00 USD | 75,700.00 USD |
| `7D` | `0.2220` | 29,420,000.00 USD | 29,420,000.00 USD | 0.00 USD | 188,710.00 USD | 86,520.00 USD | 195,670.00 USD |
| `1D` | `0.2230` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 46,100.00 USD | 11,060.00 USD | 15,420.00 USD |
| `7D` | `0.2230` | 29,710,000.00 USD | 29,710,000.00 USD | 0.00 USD | 149,810.00 USD | 47,320.00 USD | 85,130.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `455.02M` | Total OI Tokens: `2,253,135,026.1 ADA`
  * 1h OI Change: `+0.83%` | 4h OI Change: `+2.21%` | 24h OI Change: `-2.05%`
  * Exchange Breakdown: Binance=`85.26M` | Bybit=`53.28M` | OKX=`31.90M` | Hyperliquid=`30.41M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `8.72K` | Last 24h: `-492.56` | Last 3d: `57.99K` | Last 7d: `35.83K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `-0.0038%` |
| **USDT Bybit** | `0.0050%` | **USDT KuCoin** | `0.0042%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0005%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `44.70%` | `55.30%` | `0.81` | 10,640,000.00 USD |
| `15M` | `Binance` | `40.36%` | `59.64%` | `0.68` | 6,720,000.00 USD |
| `15M` | `OKX` | `43.13%` | `56.87%` | `0.76` | 683,970.00 USD |
| `15M` | `Bybit` | `37.42%` | `62.58%` | `0.60` | 205,670.00 USD |
| `15M` | `KuCoin` | `24.56%` | `75.44%` | `0.33` | 102,150.00 USD |
| `15M` | `Gate` | `66.2%` | `33.8%` | `1.96` | 1,210,000.00 USD |
| `15M` | `Bitget` | `57.17%` | `42.83%` | `1.33` | 153,910.00 USD |
| `15M` | `BingX` | `48.71%` | `51.29%` | `0.95` | 353,560.00 USD |
| `15M` | `MEXC` | `74.54%` | `25.46%` | `2.93` | 93,230.00 USD |
| `15M` | `Bitunix` | `42.11%` | `57.89%` | `0.73` | 252,960.00 USD |
| `15M` | `Hyperliquid` | `32.08%` | `67.92%` | `0.47` | 135,230.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `37.01%` | `62.99%` | `0.59` | 462,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `100%` | `0%` | `1.00` | 46,520.00 USD |
| `15M` | `HTX` | `82.4%` | `17.6%` | `4.68` | 24,100.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `71.01%` | `28.99%` | `2.45` | 43,800.00 USD |
| `15M` | `Aster` | `65.76%` | `34.24%` | `1.92` | 131,150.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `57.91%` | `42.09%` | `1.38` | 16,160.00 USD |
| `15M` | `Whale Positions` | `40.36%` | `59.64%` | `0.68` | 6,720,000.00 USD |
| `15M` | `Global Accounts` | `44.70%` | `55.30%` | `0.81` | 10,640,000.00 USD |
| `1H` | `ADA` | `51.39%` | `48.61%` | `1.06` | 106,420,000.00 USD |
| `1H` | `Binance` | `49.72%` | `50.28%` | `0.99` | 33,850,000.00 USD |
| `1H` | `OKX` | `50.56%` | `49.44%` | `1.02` | 10,880,000.00 USD |
| `1H` | `Bybit` | `50.22%` | `49.78%` | `1.01` | 10,610,000.00 USD |
| `1H` | `KuCoin` | `51.32%` | `48.68%` | `1.05` | 1,310,000.00 USD |
| `1H` | `Gate` | `50.7%` | `49.3%` | `1.03` | 5,200,000.00 USD |
| `1H` | `Bitget` | `53.61%` | `46.39%` | `1.16` | 12,010,000.00 USD |
| `1H` | `BingX` | `50.32%` | `49.68%` | `1.01` | 1,990,000.00 USD |
| `1H` | `MEXC` | `56.36%` | `43.64%` | `1.29` | 15,760,000.00 USD |
| `1H` | `Bitunix` | `50.89%` | `49.11%` | `1.04` | 4,910,000.00 USD |
| `1H` | `Hyperliquid` | `73.47%` | `26.53%` | `2.77` | 2,800,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `44.66%` | `55.34%` | `0.81` | 895,810.00 USD |
| `1H` | `Crypto.com` | `48%` | `52%` | `0.92` | 181,540.00 USD |
| `1H` | `WhiteBIT` | `22.14%` | `77.86%` | `0.28` | 3,750,000.00 USD |
| `1H` | `HTX` | `64.04%` | `35.96%` | `1.78` | 87,400.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `60.93%` | `39.07%` | `1.56` | 822,930.00 USD |
| `1H` | `Aster` | `72.36%` | `27.64%` | `2.62` | 1,200,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.83%` | `39.17%` | `1.55` | 164,610.00 USD |
| `1H` | `Whale Positions` | `49.72%` | `50.28%` | `0.99` | 33,850,000.00 USD |
| `1H` | `Global Accounts` | `51.39%` | `48.61%` | `1.06` | 106,420,000.00 USD |
| `4H` | `ADA` | `52.00%` | `48.00%` | `1.08` | 317,190,000.00 USD |
| `4H` | `Binance` | `51.73%` | `48.27%` | `1.07` | 214,720,000.00 USD |
| `4H` | `OKX` | `47.29%` | `52.71%` | `0.90` | 18,840,000.00 USD |
| `4H` | `Bybit` | `59.26%` | `40.74%` | `1.45` | 12,150,000.00 USD |
| `4H` | `KuCoin` | `47.07%` | `52.93%` | `0.89` | 1,020,000.00 USD |
| `4H` | `Gate` | `54.17%` | `45.83%` | `1.18` | 26,090,000.00 USD |
| `4H` | `Bitget` | `50.47%` | `49.53%` | `1.02` | 5,750,000.00 USD |
| `4H` | `BingX` | `49.28%` | `50.72%` | `0.97` | 7,530,000.00 USD |
| `4H` | `MEXC` | `48.56%` | `51.44%` | `0.94` | 3,890,000.00 USD |
| `4H` | `Bitunix` | `49.93%` | `50.07%` | `1.00` | 9,050,000.00 USD |
| `4H` | `Hyperliquid` | `61.09%` | `38.91%` | `1.57` | 2,520,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.84%` | `49.16%` | `1.03` | 8,190,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `90.87%` | `9.13%` | `9.95` | 1,100,000.00 USD |
| `4H` | `HTX` | `69.46%` | `30.54%` | `2.27` | 674,990.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.63%` | `61.37%` | `0.63` | 603,080.00 USD |
| `4H` | `Aster` | `55.41%` | `44.59%` | `1.24` | 3,160,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `50.44%` | `49.56%` | `1.02` | 1,890,000.00 USD |
| `4H` | `Whale Positions` | `51.73%` | `48.27%` | `1.07` | 214,720,000.00 USD |
| `4H` | `Global Accounts` | `52.00%` | `48.00%` | `1.08` | 317,190,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.2011` | `0.2011` | `0.2011` | `0.2014` | `0.2007` | 834,548.46 USD | 335,703.57 USD | 498,844.89 USD | -163,141.32 USD | `-19.55%` | `0B / 1S` |
| `0:00 UTC` | `0.2002` | `0.2003` | `0.2002` | `0.2011` | `0.1996` | 2,376,476.73 USD | 990,553.61 USD | 1,385,923.12 USD | -395,369.52 USD | `-16.64%` | `0B / 5S` |
| `5:00 UTC` | `0.2001` | `0.2002` | `0.2001` | `0.2007` | `0.1998` | 1,923,836.73 USD | 956,937.62 USD | 966,899.10 USD | -9,961.48 USD | `-0.52%` | `1B / 1S` |
| `0:00 UTC` | `0.2005` | `0.2007` | `0.2005` | `0.2015` | `0.2001` | 2,740,117.43 USD | 1,667,449.06 USD | 1,072,668.37 USD | 594,780.69 USD | `+21.71%` | `0B / 1S` |
| `5:00 UTC` | `0.2011` | `0.2010` | `0.2011` | `0.2015` | `0.2006` | 898,552.12 USD | 446,892.53 USD | 451,659.59 USD | -4,767.06 USD | `-0.53%` | `1B / 0S` |
| `0:00 UTC` | `0.2016` | `0.2016` | `0.2016` | `0.2021` | `0.2011` | 2,066,743.77 USD | 1,072,594.11 USD | 994,149.66 USD | 78,444.45 USD | `+3.80%` | `2B / 0S` |
| `5:00 UTC` | `0.2017` | `0.2017` | `0.2017` | `0.2022` | `0.2012` | 1,598,330.69 USD | 947,977.54 USD | 650,353.15 USD | 297,624.39 USD | `+18.62%` | `2B / 0S` |
| `0:00 UTC` | `0.2011` | `0.2012` | `0.2011` | `0.2021` | `0.2004` | 2,391,609.70 USD | 1,212,636.82 USD | 1,178,972.88 USD | 33,663.94 USD | `+1.41%` | `0B / 0S` |
| `5:00 UTC` | `0.2015` | `0.2015` | `0.2015` | `0.2026` | `0.2007` | 1,983,992.92 USD | 1,118,578.56 USD | 865,414.36 USD | 253,164.20 USD | `+12.76%` | `3B / 0S` |
| `0:00 UTC` | `0.2020` | `0.2019` | `0.2020` | `0.2024` | `0.2014` | 1,055,965.92 USD | 522,223.33 USD | 533,742.59 USD | -11,519.25 USD | `-1.09%` | `2B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 19:57` | `Range 0.001` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.2010` | 3,900,000.00 USD | 0.00 USD |
| `10-28 17:44` | `Volume 20M ADA` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2042` | 0.00 USD | 0.00 USD |
| `10-28 17:43` | `Range 0.001` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2042` | 0.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.001` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.2058` | 1,300,000.00 USD | 0.00 USD |
| `10-28 16:11` | `Range 0.001` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.2077` | 1,600,000.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.001` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.2066` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.001` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `0.2055` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Range 0.001` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.2075` | 0.00 USD | 0.00 USD |
| `10-28 09:01` | `Range 0.001` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.2085` | 0.00 USD | 0.00 USD |
| `10-28 08:39` | `Volume 20M ADA` | `Trapped longs` | **`BEARISH`** | Failed breakout | `0.2085` | 4,700,000.00 USD | 0.00 USD |
| `10-28 07:53` | `Range 0.001` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.2063` | 3,600,000.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -844.79 USD | 31,910.00 USD | **`ACCUMULATION`** |
| `15m` | 145,330.00 USD | 329,990.00 USD | **`ACCUMULATION`** |
| `30m` | 164,780.00 USD | 554,170.00 USD | **`ACCUMULATION`** |
| `1h` | -54,160.00 USD | 920,060.00 USD | **`ACCUMULATION`** |
| `2h` | 90,480.00 USD | 1,560,000.00 USD | **`ACCUMULATION`** |
| `4h` | 280,780.00 USD | 1,120,000.00 USD | **`ACCUMULATION`** |
| `6h` | 445,960.00 USD | 2,610,000.00 USD | **`ACCUMULATION`** |
| `8h` | 313,640.00 USD | 2,610,000.00 USD | **`ACCUMULATION`** |
| `12h` | -169,420.00 USD | 1,980,000.00 USD | **`ACCUMULATION`** |
| `24h` | -2,630,000.00 USD | -2,730,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -14,870,000.00 USD | -36,590,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -70,320,000.00 USD | -190,050,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-844.79` | 15m=`+145.33K` | 1h=`-54.16K` | 24h=`-2.63M`
* Futures Capital Netflows: 5m=`+31.91K` | 15m=`+329.99K` | 1h=`+920.06K` | 24h=`-2.73M`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1953` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1909` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.2064`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2005` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2049` (Risk Distance: `0.0044` pts)
  * +2.5R Take Profit: `0.1894`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2034`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
