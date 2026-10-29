# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:55:03 IST` (`2026-10-29 17:25:03 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2030` | **Live Ask Quote**: `0.2052` | **Mid Price**: `0.2041`
- **Spread Points**: `22.00` | **Spread BPS**: `107.79 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1997` | VWAP Z-Score: `+1.11` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0014` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.39` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2089` | Lower -3.00σ Band: `0.1904`
  * Upper +2.51σ Band: `0.2074` | Lower -2.51σ Band: `0.1919`
  * Upper +2.01σ Band: `0.2059` | Lower -2.01σ Band: `0.1935`
  * Upper +2.00σ Band: `0.2059` | Lower -2.00σ Band: `0.1935`
  * Upper +1.28σ Band: `0.2036` | Lower -1.28σ Band: `0.1957`
  * Upper +1.00σ Band: `0.2028` | Lower -1.00σ Band: `0.1966`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2038` | EMA-20=`0.2026` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2011` (Slope: `+0.0000`) | EMA-100=`0.2011`
  * Institutional Anchors: EMA-144=`0.2014` | EMA-200=`0.2018` (Slope: `+0.1247`) | EMA-233=`0.2020`
- **Range Boundaries**: 24H High=`0.2086` | 24H Low=`0.1944` | Weekly High=`0.2086` | Weekly Low=`0.1944`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2064` (Distance: `-1.12%`)
  * Point of Control (POC) = `0.2047` (Distance: `-0.28%`)
  * Value Area Low (VAL) = `0.1976` (Distance: `+3.26%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2058` | Weekly POC=`0.2031` | Weekly VAL=`0.2011`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2074` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2033` - `0.2049`
  * Optimal Trade Entry (OTE 0.705): `0.2045`
  * Structural Invalidation Anchor (0.786): `0.2057`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.2047` | `0.2050` | `0.2042` | `0.2043` | `3,296,012` | 674,915.83 USD | -60,266.34 USD | `-8.93%` | 2,513,181.29 USD | `-0.53` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.2043` | `0.2046` | `0.2041` | `0.2043` | `2,921,835` | 597,240.74 USD | -56,952.04 USD | `-9.54%` | 2,456,229.24 USD | `-0.47` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.2043` | `0.2047` | `0.2041` | `0.2043` | `2,425,857` | 495,790.31 USD | -39,746.88 USD | `-8.02%` | 2,416,482.36 USD | `-0.36` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.2055` | `0.2059` | `0.2051` | `0.2054` | `5,372,201` | 1,103,361.90 USD | 61,188.16 USD | `+5.55%` | 2,363,170.61 USD | `-0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2055` | `0.2055` | `0.2042` | `0.2043` | `12,246,608` | 2,508,493.59 USD | 154,792.66 USD | `+6.17%` | 2,517,963.27 USD | `-0.03` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2043` | `0.2047` | `0.2041` | `0.2043` | `5,347,692` | 1,093,031.06 USD | -96,698.93 USD | `-8.85%` | 2,421,264.34 USD | `-0.90` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `0.2037` | `0.2065` | `0.2035` | `0.2063` | `50,555,533` | 10,368,970.33 USD | 269,833.71 USD | `+2.60%` | 1,061,283.01 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2064` | `0.2087` | `0.2047` | `0.2054` | `58,420,928` | 12,055,112.15 USD | 949,842.55 USD | `+7.88%` | 2,011,125.56 USD | `+0.81` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2055` | `0.2055` | `0.2041` | `0.2043` | `17,594,300` | 3,601,524.65 USD | 58,093.73 USD | `+1.61%` | 2,069,219.29 USD | `+0.10` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2041` | `0.2043` | `76,015,228` | 15,656,636.79 USD | 1,007,936.29 USD | `+6.44%` | 1,048,470.86 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2058` | `0.2065` | `0.1954` | `0.1973` | `282,726,861` | 56,231,891.33 USD | -5,955,308.28 USD | `-10.59%` | -3,049,296.45 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -2,508,321.21 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2041` | `0.2043` | `76,015,228` | 15,656,636.79 USD | 1,007,936.29 USD | `+6.44%` | 1,048,470.86 USD | `+0.29` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.2041`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:54:46 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `542` | `0x77ee...2902` | `SHORT` | 4,373,440.22 USD | `21,412,192.00` | `0.1911` | `0.2045` | `0.5635` | -282,188.48 USD | `-6.45%` | `10X Cross` |
| `1200` | `0x123d...3bff` | `LONG` | 1,920,521.81 USD | `9,393,142.00` | `0.2912` | `0.2045` | `0.000000` | -815,214.12 USD | `-42.45%` | `10X Cross` |
| `1253` | `0x7737...bf66` | `SHORT` | 1,857,750.16 USD | `9,091,466.00` | `0.2190` | `0.2045` | `2.20` | 133,239.64 USD | `+7.17%` | `10X Cross` |
| `1557` | `0x5f94...4b96` | `SHORT` | 1,463,476.44 USD | `7,162,318.00` | `0.2303` | `0.2045` | `0.7763` | 185,998.76 USD | `+12.71%` | `10X Cross` |
| `1778` | `0x4982...59e6` | `SHORT` | 1,225,257.35 USD | `5,998,812.00` | `0.1891` | `0.2045` | `0.3857` | -90,698.99 USD | `-7.40%` | `10X Cross` |
| `1821` | `0xcac1...26b3` | `LONG` | 1,185,742.29 USD | `5,803,927.00` | `0.2000` | `0.2045` | `0.000000` | 24,926.70 USD | `+2.10%` | `10X Cross` |
| `2002` | `0x51f6...2b39` | `LONG` | 1,035,661.46 USD | `5,065,350.00` | `0.2294` | `0.2045` | `0.000000` | -126,488.12 USD | `-12.21%` | `10X Cross` |
| `2011` | `0xeadc...9d55` | `LONG` | 1,029,546.66 USD | `5,038,400.00` | `0.2195` | `0.2045` | `0.000000` | -76,166.09 USD | `-7.40%` | `10X Cross` |
| `2018` | `0x0748...d4b2` | `SHORT` | 1,021,300.00 USD | `5,000,000.00` | `0.2036` | `0.2045` | `0.6157` | -3,442.76 USD | `-0.34%` | `10X Cross` |
| `2050` | `0xfbe2...c8ea` | `LONG` | 1,005,589.95 USD | `4,923,088.00` | `0.2667` | `0.2045` | `0.0131` | -307,355.68 USD | `-30.56%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2046` | 6,153.89 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2046 USD [API] | `2026-10-27 20:33:02` |
| `ANNOUNCEMENT` | `INFO` | `0.2046` | 6,648.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2046 USD [API] | `2026-10-27 20:39:19` |
| `ANNOUNCEMENT` | `INFO` | `0.2044` | 6,587.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.59K USD at 0.2044 USD [API] | `2026-10-27 21:21:42` |
| `ANNOUNCEMENT` | `INFO` | `0.2067` | 6,278.84 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.28K USD at 0.2067 USD [API] | `2026-10-27 21:36:56` |
| `ANNOUNCEMENT` | `INFO` | `0.2063` | 6,645.63 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2063 USD [API] | `2026-10-27 21:39:43` |
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 6,655.44 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.66K USD at 0.2061 USD [API] | `2026-10-27 21:46:03` |
| `ANNOUNCEMENT` | `INFO` | `0.2057` | 6,350.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.35K USD at 0.2057 USD [API] | `2026-10-27 21:53:01` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+2.35%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.77%`)
  * 48H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+2.35%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.77%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 261,100.00 USD, Dist: `+4.50%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.77%`)
  * 7D Horizon: Short MP=`0.2124` (Vol: 359,800.00 USD, Dist: `+3.85%`) | Long MP=`0.1926` (Vol: 321,900.00 USD, Dist: `--5.82%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0475` | 427.50 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0515` | 5,410.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0525` | 2,070.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0575` | 898.61 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0615` | 647.35 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0625` | 532.25 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0665` | 124,600.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0675` | 172.87 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0805` | 140.39 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0855` | 855.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 96,080.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0905` | 12,670.00 USD | 2,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0995` | 102.58 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 781.18 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1085` | 942.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 2,550.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1125` | 356.40 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1135` | 691.56 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 862.64 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1155` | 2,830.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 13,360.00 USD | 2,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 931.42 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 3,610.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 125.97 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1285` | 300.95 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 290.36 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 3,600.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 710.03 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 784.14 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1385` | 3,200.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1395` | 2,120.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 565.51 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,870.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 13,970.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,500.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 6,890.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 4,580.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 1,180.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 163.65 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 599.05 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 508,550.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 38,550.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 1,100.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,640.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 11,090.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 1,580.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 6,690.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 1,430.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 60,810.00 USD | 1,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 5,740.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,470.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1635` | 1,040.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,540.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1655` | 587.19 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,820.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 35,510.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 1,750.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 1,280.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 619,740.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,110.00 USD | 907,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1725` | 2,720.00 USD | 655,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,830.00 USD | 652,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1745` | 1,320.00 USD | 650,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1755` | 4,720.00 USD | 649,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1765` | 7,730.00 USD | 644,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1770` | 11,340,000.00 USD | 11,340,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 636,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1780` | 11,270,000.00 USD | 11,270,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 15,790.00 USD | 620,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1790` | 11,200,000.00 USD | 11,200,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 12,760.00 USD | 605,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1800` | 11,180,000.00 USD | 11,180,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 134,610.00 USD | 592,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1810` | 11,150,000.00 USD | 11,150,000.00 USD | 112,560.00 USD | 27,510.00 USD | 31,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 457,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1820` | 10,980,000.00 USD | 10,980,000.00 USD | 95,280.00 USD | 47,480.00 USD | 117,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,250.00 USD | 450,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1830` | 10,720,000.00 USD | 10,720,000.00 USD | 84,560.00 USD | 36,880.00 USD | 59,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 431,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 10,660,000.00 USD | 10,660,000.00 USD | 141,830.00 USD | 33,300.00 USD | 35,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 10,540,000.00 USD | 10,540,000.00 USD | 226,530.00 USD | 58,050.00 USD | 174,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 431,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 10,450,000.00 USD | 10,450,000.00 USD | 163,720.00 USD | 57,260.00 USD | 98,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 10,080,000.00 USD | 10,080,000.00 USD | 404,170.00 USD | 111,470.00 USD | 387,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 6,190.00 USD | 430,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 10,130,000.00 USD | 10,130,000.00 USD | 35,280.00 USD | 8,700.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 9,170,000.00 USD | 9,170,000.00 USD | 114,090.00 USD | 56,980.00 USD | 194,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 2,900.00 USD | 424,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 10,070,000.00 USD | 10,070,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 8,810,000.00 USD | 8,810,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,120.00 USD | 421,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 9,960,000.00 USD | 9,960,000.00 USD | 219,090.00 USD | 32,270.00 USD | 34,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 8,550,000.00 USD | 8,550,000.00 USD | 158,590.00 USD | 41,220.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 9,670.00 USD | 417,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 9,680,000.00 USD | 9,680,000.00 USD | 101,860.00 USD | 72,430.00 USD | 184,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 8,310,000.00 USD | 8,310,000.00 USD | 246,750.00 USD | 52,560.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 10,260.00 USD | 407,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 9,320,000.00 USD | 9,320,000.00 USD | 247,200.00 USD | 105,640.00 USD | 203,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 7,870,000.00 USD | 7,870,000.00 USD | 247,920.00 USD | 72,080.00 USD | 235,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 13,110.00 USD | 397,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 8,760,000.00 USD | 8,760,000.00 USD | 230,970.00 USD | 82,400.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 7,320,000.00 USD | 7,320,000.00 USD | 258,450.00 USD | 86,060.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 27,820.00 USD | 384,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 8,360,000.00 USD | 8,360,000.00 USD | 486,530.00 USD | 114,180.00 USD | 182,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 6,960,000.00 USD | 6,960,000.00 USD | 257,730.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 50,480.00 USD | 356,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 7,580,000.00 USD | 7,580,000.00 USD | 300,360.00 USD | 196,980.00 USD | 468,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 6,550,000.00 USD | 6,550,000.00 USD | 722,350.00 USD | 159,940.00 USD | 323,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,550.00 USD | 306,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 6,610,000.00 USD | 6,610,000.00 USD | 625,710.00 USD | 252,190.00 USD | 513,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 5,340,000.00 USD | 5,340,000.00 USD | 678,880.00 USD | 259,610.00 USD | 823,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 6,000.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 5,220,000.00 USD | 5,220,000.00 USD | 514,200.00 USD | 173,220.00 USD | 212,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 3,580,000.00 USD | 3,580,000.00 USD | 619,180.00 USD | 288,290.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 8,500.00 USD | 9,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 4,320,000.00 USD | 4,320,000.00 USD | 451,150.00 USD | 148,090.00 USD | 319,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 2,280,000.00 USD | 2,280,000.00 USD | 99,630.00 USD | 9,990.00 USD | 676,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1965` | 982.50 USD | 982.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1970` | 3,400,000.00 USD | 3,400,000.00 USD | 324,400.00 USD | 149,150.00 USD | 272,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 1,500,000.00 USD | 1,500,000.00 USD | 80,840.00 USD | 56,210.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 2,650,000.00 USD | 2,650,000.00 USD | 299,150.00 USD | 92,080.00 USD | 129,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 20,720.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1990` | 2,130,000.00 USD | 2,130,000.00 USD | 26,640.00 USD | 0.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 2,100,000.00 USD | 2,100,000.00 USD | 109,830.00 USD | 70,030.00 USD | 137,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 31,080.00 USD | 31,080.00 USD | 0.00 USD | 25,400.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 1,780,000.00 USD | 1,780,000.00 USD | 278,340.00 USD | 79,030.00 USD | 177,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 602,690.00 USD | 602,690.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 1,210,000.00 USD | 1,210,000.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2020` | 1,240,000.00 USD | 1,240,000.00 USD | 211,750.00 USD | 53,220.00 USD | 71,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 1,720,000.00 USD | 1,720,000.00 USD | 154,520.00 USD | 0.00 USD | 360,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2030` | 906,000.00 USD | 906,000.00 USD | 462,960.00 USD | 151,590.00 USD | 291,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 2,000,000.00 USD | 2,000,000.00 USD | 173,570.00 USD | 109,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 286,440.00 USD | 286,440.00 USD | 0.00 USD | 203,670.00 USD | 82,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 572,890.00 USD | 572,890.00 USD | 0.00 USD | 203,670.00 USD | 82,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 2,400,000.00 USD | 2,400,000.00 USD | 125,120.00 USD | 53,690.00 USD | 215,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 584,830.00 USD | 584,830.00 USD | 0.00 USD | 0.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 3,000,000.00 USD | 3,000,000.00 USD | 276,760.00 USD | 82,430.00 USD | 242,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 597,230.00 USD | 597,230.00 USD | 0.00 USD | 1,350.00 USD | 11,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 3,380,000.00 USD | 3,380,000.00 USD | 144,470.00 USD | 31,310.00 USD | 206,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 1,260,000.00 USD | 1,260,000.00 USD | 409,780.00 USD | 106,370.00 USD | 150,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 3,910,000.00 USD | 3,910,000.00 USD | 385,560.00 USD | 80,540.00 USD | 58,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 1,870,000.00 USD | 1,870,000.00 USD | 450,830.00 USD | 152,560.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 4,570,000.00 USD | 4,570,000.00 USD | 552,200.00 USD | 44,630.00 USD | 65,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 2,890,000.00 USD | 2,890,000.00 USD | 542,330.00 USD | 189,870.00 USD | 282,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 6,820,000.00 USD | 6,820,000.00 USD | 2,010,000.00 USD | 87,520.00 USD | 155,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 4,260,000.00 USD | 4,260,000.00 USD | 637,140.00 USD | 247,430.00 USD | 488,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 10,610,000.00 USD | 10,610,000.00 USD | 1,560,000.00 USD | 660,820.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 4,710,000.00 USD | 4,710,000.00 USD | 259,670.00 USD | 54,340.00 USD | 138,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 13,600,000.00 USD | 13,600,000.00 USD | 1,030,000.00 USD | 499,260.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 5,290,000.00 USD | 5,290,000.00 USD | 282,550.00 USD | 112,530.00 USD | 182,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 16,490,000.00 USD | 16,490,000.00 USD | 1,120,000.00 USD | 463,080.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 5,960,000.00 USD | 5,960,000.00 USD | 340,500.00 USD | 103,220.00 USD | 223,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 18,970,000.00 USD | 18,970,000.00 USD | 1,090,000.00 USD | 289,130.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 6,570,000.00 USD | 6,570,000.00 USD | 314,560.00 USD | 103,250.00 USD | 191,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 21,000,000.00 USD | 21,000,000.00 USD | 820,780.00 USD | 379,940.00 USD | 830,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 6,720,000.00 USD | 6,720,000.00 USD | 75,880.00 USD | 19,010.00 USD | 54,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 23,230,000.00 USD | 23,230,000.00 USD | 916,150.00 USD | 316,800.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 4,300.00 USD | 5,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 6,910,000.00 USD | 6,910,000.00 USD | 117,430.00 USD | 35,330.00 USD | 40,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 24,240,000.00 USD | 24,240,000.00 USD | 447,110.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 7,130,000.00 USD | 7,130,000.00 USD | 76,340.00 USD | 28,650.00 USD | 116,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,870,000.00 USD | 24,870,000.00 USD | 296,410.00 USD | 94,900.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 104.40 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2180` | 7,310,000.00 USD | 7,310,000.00 USD | 85,920.00 USD | 30,810.00 USD | 63,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 25,390,000.00 USD | 25,390,000.00 USD | 266,770.00 USD | 102,870.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 24,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 7,460,000.00 USD | 7,460,000.00 USD | 83,440.00 USD | 28,270.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 26,600,000.00 USD | 26,600,000.00 USD | 630,760.00 USD | 188,070.00 USD | 391,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 7,610,000.00 USD | 7,610,000.00 USD | 85,310.00 USD | 24,670.00 USD | 41,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 27,920,000.00 USD | 27,920,000.00 USD | 558,280.00 USD | 232,970.00 USD | 526,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 7,700,000.00 USD | 7,700,000.00 USD | 45,350.00 USD | 17,440.00 USD | 27,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 28,950,000.00 USD | 28,950,000.00 USD | 532,080.00 USD | 84,700.00 USD | 416,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 25,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 7,790,000.00 USD | 7,790,000.00 USD | 51,150.00 USD | 11,430.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 29,420,000.00 USD | 29,420,000.00 USD | 188,710.00 USD | 86,520.00 USD | 195,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 7,850,000.00 USD | 7,850,000.00 USD | 46,180.00 USD | 6,100.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 29,710,000.00 USD | 29,710,000.00 USD | 149,810.00 USD | 47,320.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 7,960,000.00 USD | 7,960,000.00 USD | 53,080.00 USD | 23,430.00 USD | 30,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2260` | 8,080,000.00 USD | 8,080,000.00 USD | 71,130.00 USD | 26,160.00 USD | 28,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2270` | 8,250,000.00 USD | 8,250,000.00 USD | 61,490.00 USD | 29,170.00 USD | 69,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 28,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2280` | 8,280,000.00 USD | 8,280,000.00 USD | 12,350.00 USD | 5,470.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 37,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2290` | 8,310,000.00 USD | 8,310,000.00 USD | 8,350.00 USD | 8,950.00 USD | 15,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2300` | 8,350,000.00 USD | 8,350,000.00 USD | 12,650.00 USD | 5,500.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 1,980.00 USD | 39,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 46,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2355` | 10,470.00 USD | 57,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2395` | 511.57 USD | 57,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,470.00 USD | 59,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 743.58 USD | 60,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2525` | 28,370.00 USD | 88,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 88,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2615` | 1,400.00 USD | 90,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2765` | 14,060.00 USD | 104,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 520.31 USD | 104,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 106,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 107,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 110,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 111,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 119,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 146.34 USD | 119,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 119,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3105` | 96,880.00 USD | 216,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 114.32 USD | 216,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3175` | 301.62 USD | 217,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 219,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3345` | 239.50 USD | 219,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3385` | 1,060.00 USD | 220,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3395` | 2,550.00 USD | 223,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3415` | 4,610.00 USD | 227,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 6,020.00 USD | 233,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3495` | 90,120.00 USD | 323,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 1,490.00 USD | 325,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3575` | 26,440.00 USD | 351,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 575.03 USD | 352,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,320.00 USD | 361,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 364,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3845` | 2,310,000.00 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3915` | 788.87 USD | 2,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3925` | 26,120.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3935` | 280.17 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3995` | 1,030.00 USD | 2,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4045` | 6,820.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4075` | 293,710.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4085` | 2,060.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.4095` | 1,040.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0475` | 2,610,000.00 USD | 0.00 USD | 427.50 USD | `-76.86%` | `9,000.00` |
| `Live` | `Long` | `0.0515` | 2,610,000.00 USD | 0.00 USD | 5,410.00 USD | `-74.92%` | `105,008.00` |
| `Live` | `Long` | `0.0525` | 2,600,000.00 USD | 0.00 USD | 2,070.00 USD | `-74.43%` | `39,410.00` |
| `Live` | `Long` | `0.0575` | 2,600,000.00 USD | 0.00 USD | 898.61 USD | `-71.99%` | `15,628.00` |
| `Live` | `Long` | `0.0615` | 2,600,000.00 USD | 0.00 USD | 647.35 USD | `-70.05%` | `10,526.00` |
| `Live` | `Long` | `0.0625` | 2,600,000.00 USD | 0.00 USD | 532.25 USD | `-69.56%` | `8,516.00` |
| `Live` | `Long` | `0.0665` | 2,600,000.00 USD | 0.00 USD | 124,600.00 USD | `-67.61%` | `1,873,703.00` |
| `Live` | `Long` | `0.0675` | 2,470,000.00 USD | 0.00 USD | 172.87 USD | `-67.12%` | `2,561.00` |
| `Live` | `Long` | `0.0805` | 2,470,000.00 USD | 0.00 USD | 140.39 USD | `-60.79%` | `1,744.00` |
| `Live` | `Long` | `0.0815` | 2,470,000.00 USD | 0.00 USD | 284.84 USD | `-60.30%` | `3,495.00` |
| `Live` | `Long` | `0.0855` | 2,470,000.00 USD | 0.00 USD | 855.00 USD | `-58.36%` | `10,000.00` |
| `Live` | `Long` | `0.0865` | 2,470,000.00 USD | 0.00 USD | 96,080.00 USD | `-57.87%` | `1,110,766.00` |
| `Live` | `Long` | `0.0875` | 2,370,000.00 USD | 0.00 USD | 344.75 USD | `-57.38%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,370,000.00 USD | 0.00 USD | 1,150.00 USD | `-56.89%` | `13,050.00` |
| `Live` | `Long` | `0.0905` | 2,370,000.00 USD | 0.00 USD | 12,670.00 USD | `-55.92%` | `140,000.00` |
| `Live` | `Long` | `0.0925` | 2,360,000.00 USD | 0.00 USD | 165.11 USD | `-54.95%` | `1,785.00` |
| `Live` | `Long` | `0.0945` | 2,360,000.00 USD | 0.00 USD | 327.54 USD | `-53.97%` | `3,466.00` |
| `Live` | `Long` | `0.0995` | 2,360,000.00 USD | 0.00 USD | 102.58 USD | `-51.54%` | `1,031.00` |
| `Live` | `Long` | `0.1025` | 2,360,000.00 USD | 0.00 USD | 4,100.00 USD | `-50.08%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,360,000.00 USD | 0.00 USD | 1,050.00 USD | `-49.59%` | `10,149.00` |
| `Live` | `Long` | `0.1065` | 2,350,000.00 USD | 0.00 USD | 781.18 USD | `-48.13%` | `7,335.00` |
| `Live` | `Long` | `0.1085` | 2,350,000.00 USD | 0.00 USD | 942.00 USD | `-47.15%` | `8,682.00` |
| `Live` | `Long` | `0.1095` | 2,350,000.00 USD | 0.00 USD | 2,550.00 USD | `-46.67%` | `23,247.00` |
| `Live` | `Long` | `0.1125` | 2,350,000.00 USD | 0.00 USD | 356.40 USD | `-45.20%` | `3,168.00` |
| `Live` | `Long` | `0.1135` | 2,350,000.00 USD | 0.00 USD | 691.56 USD | `-44.72%` | `6,093.00` |
| `Live` | `Long` | `0.1145` | 2,350,000.00 USD | 0.00 USD | 862.64 USD | `-44.23%` | `7,534.00` |
| `Live` | `Long` | `0.1155` | 2,350,000.00 USD | 0.00 USD | 2,830.00 USD | `-43.74%` | `24,507.00` |
| `Live` | `Long` | `0.1165` | 2,350,000.00 USD | 0.00 USD | 13,360.00 USD | `-43.26%` | `114,690.00` |
| `Live` | `Long` | `0.1175` | 2,330,000.00 USD | 0.00 USD | 931.42 USD | `-42.77%` | `7,927.00` |
| `Live` | `Long` | `0.1205` | 2,330,000.00 USD | 0.00 USD | 3,610.00 USD | `-41.31%` | `29,974.00` |
| `Live` | `Long` | `0.1215` | 2,330,000.00 USD | 0.00 USD | 1,050.00 USD | `-40.82%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,330,000.00 USD | 0.00 USD | 125.97 USD | `-39.85%` | `1,020.00` |
| `Live` | `Long` | `0.1245` | 2,330,000.00 USD | 0.00 USD | 404.62 USD | `-39.36%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,330,000.00 USD | 0.00 USD | 1,980.00 USD | `-38.87%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,320,000.00 USD | 0.00 USD | 314.61 USD | `-38.39%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,320,000.00 USD | 0.00 USD | 1,260.00 USD | `-37.90%` | `9,873.00` |
| `Live` | `Long` | `0.1285` | 2,320,000.00 USD | 0.00 USD | 300.95 USD | `-37.41%` | `2,342.00` |
| `Live` | `Long` | `0.1295` | 2,320,000.00 USD | 0.00 USD | 2,540.00 USD | `-36.92%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,320,000.00 USD | 0.00 USD | 290.36 USD | `-36.44%` | `2,225.00` |
| `Live` | `Long` | `0.1315` | 2,320,000.00 USD | 0.00 USD | 687.35 USD | `-35.95%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,320,000.00 USD | 0.00 USD | 6,960.00 USD | `-35.46%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,310,000.00 USD | 0.00 USD | 3,600.00 USD | `-34.98%` | `26,965.00` |
| `Live` | `Long` | `0.1345` | 2,310,000.00 USD | 0.00 USD | 710.03 USD | `-34.49%` | `5,279.00` |
| `Live` | `Long` | `0.1355` | 2,310,000.00 USD | 0.00 USD | 784.14 USD | `-34.00%` | `5,787.00` |
| `Live` | `Long` | `0.1385` | 2,310,000.00 USD | 0.00 USD | 3,200.00 USD | `-32.54%` | `23,123.00` |
| `Live` | `Long` | `0.1395` | 2,300,000.00 USD | 0.00 USD | 2,120.00 USD | `-32.05%` | `15,162.00` |
| `Live` | `Long` | `0.1405` | 2,300,000.00 USD | 0.00 USD | 565.51 USD | `-31.57%` | `4,025.00` |
| `Live` | `Long` | `0.1415` | 2,300,000.00 USD | 0.00 USD | 9,870.00 USD | `-31.08%` | `69,722.00` |
| `Live` | `Long` | `0.1435` | 2,290,000.00 USD | 0.00 USD | 13,970.00 USD | `-30.11%` | `97,369.00` |
| `Live` | `Long` | `0.1445` | 2,280,000.00 USD | 0.00 USD | 2,500.00 USD | `-29.62%` | `17,302.00` |
| `Live` | `Long` | `0.1455` | 2,270,000.00 USD | 0.00 USD | 6,890.00 USD | `-29.13%` | `47,381.00` |
| `Live` | `Long` | `0.1465` | 2,270,000.00 USD | 0.00 USD | 4,580.00 USD | `-28.64%` | `31,277.00` |
| `Live` | `Long` | `0.1475` | 2,260,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.16%` | `8,000.00` |
| `Live` | `Long` | `0.1485` | 2,260,000.00 USD | 0.00 USD | 163.65 USD | `-27.67%` | `1,102.00` |
| `Live` | `Long` | `0.1495` | 2,260,000.00 USD | 0.00 USD | 599.05 USD | `-27.18%` | `4,007.00` |
| `Live` | `Long` | `0.1505` | 2,260,000.00 USD | 0.00 USD | 508,550.00 USD | `-26.70%` | `3,379,041.00` |
| `Live` | `Long` | `0.1515` | 1,750,000.00 USD | 0.00 USD | 38,550.00 USD | `-26.21%` | `254,423.00` |
| `Live` | `Long` | `0.1525` | 1,710,000.00 USD | 0.00 USD | 1,100.00 USD | `-25.72%` | `7,199.00` |
| `Live` | `Long` | `0.1535` | 1,710,000.00 USD | 0.00 USD | 42,640.00 USD | `-25.24%` | `277,811.00` |
| `Live` | `Long` | `0.1545` | 1,670,000.00 USD | 0.00 USD | 721.05 USD | `-24.75%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,670,000.00 USD | 0.00 USD | 11,090.00 USD | `-24.26%` | `71,295.00` |
| `Live` | `Long` | `0.1565` | 1,660,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.77%` | `10,116.00` |
| `Live` | `Long` | `0.1585` | 1,660,000.00 USD | 0.00 USD | 6,690.00 USD | `-22.80%` | `42,237.00` |
| `Live` | `Long` | `0.1595` | 1,650,000.00 USD | 0.00 USD | 1,430.00 USD | `-22.31%` | `8,980.00` |
| `Live` | `Long` | `0.1605` | 1,650,000.00 USD | 0.00 USD | 60,810.00 USD | `-21.83%` | `378,894.00` |
| `Live` | `Long` | `0.1615` | 1,590,000.00 USD | 0.00 USD | 5,740.00 USD | `-21.34%` | `35,537.00` |
| `Live` | `Long` | `0.1625` | 1,580,000.00 USD | 0.00 USD | 2,470.00 USD | `-20.85%` | `15,182.00` |
| `Live` | `Long` | `0.1635` | 1,580,000.00 USD | 0.00 USD | 1,040.00 USD | `-20.36%` | `6,337.00` |
| `Live` | `Long` | `0.1645` | 1,580,000.00 USD | 0.00 USD | 10,540.00 USD | `-19.88%` | `64,095.00` |
| `Live` | `Long` | `0.1655` | 1,570,000.00 USD | 0.00 USD | 587.19 USD | `-19.39%` | `3,548.00` |
| `Live` | `Long` | `0.1665` | 1,570,000.00 USD | 0.00 USD | 1,820.00 USD | `-18.90%` | `10,911.00` |
| `Live` | `Long` | `0.1675` | 1,570,000.00 USD | 0.00 USD | 35,510.00 USD | `-18.42%` | `212,026.00` |
| `Live` | `Long` | `0.1685` | 1,530,000.00 USD | 0.00 USD | 1,750.00 USD | `-17.93%` | `10,397.00` |
| `Live` | `Long` | `0.1695` | 1,530,000.00 USD | 0.00 USD | 1,280.00 USD | `-17.44%` | `7,557.00` |
| `Live` | `Long` | `0.1705` | 1,530,000.00 USD | 0.00 USD | 619,740.00 USD | `-16.95%` | `3,634,856.00` |
| `Live` | `Long` | `0.1715` | 907,160.00 USD | 0.00 USD | 252,110.00 USD | `-16.47%` | `1,470,005.00` |
| `Live` | `Long` | `0.1725` | 655,060.00 USD | 0.00 USD | 2,720.00 USD | `-15.98%` | `15,753.00` |
| `Live` | `Long` | `0.1735` | 652,340.00 USD | 0.00 USD | 1,830.00 USD | `-15.49%` | `10,522.00` |
| `Live` | `Long` | `0.1745` | 650,510.00 USD | 0.00 USD | 1,320.00 USD | `-15.01%` | `7,554.00` |
| `Live` | `Long` | `0.1755` | 649,200.00 USD | 0.00 USD | 4,720.00 USD | `-14.52%` | `26,871.00` |
| `Live` | `Long` | `0.1765` | 644,480.00 USD | 0.00 USD | 7,730.00 USD | `-14.03%` | `43,812.00` |
| `Live` | `Long` | `0.1775` | 636,750.00 USD | 0.00 USD | 15,750.00 USD | `-13.55%` | `88,754.00` |
| `Live` | `Long` | `0.1785` | 620,990.00 USD | 0.00 USD | 15,790.00 USD | `-13.06%` | `88,484.00` |
| `Live` | `Long` | `0.1795` | 605,200.00 USD | 0.00 USD | 12,760.00 USD | `-12.57%` | `71,107.00` |
| `Live` | `Long` | `0.1805` | 592,440.00 USD | 0.00 USD | 134,610.00 USD | `-12.08%` | `745,776.00` |
| `Live` | `Long` | `0.1815` | 457,820.00 USD | 0.00 USD | 7,670.00 USD | `-11.60%` | `42,240.00` |
| `Live` | `Long` | `0.1825` | 450,160.00 USD | 0.00 USD | 18,250.00 USD | `-11.11%` | `100,000.00` |
| `Live` | `Long` | `0.1835` | 431,910.00 USD | 0.00 USD | 367.00 USD | `-10.62%` | `2,000.00` |
| `Live` | `Long` | `0.1845` | 431,540.00 USD | 0.00 USD | 956.45 USD | `-10.14%` | `5,184.00` |
| `Live` | `Long` | `0.1855` | 430,580.00 USD | 0.00 USD | 6,190.00 USD | `-9.65%` | `33,366.00` |
| `Live` | `Long` | `0.1865` | 424,390.00 USD | 0.00 USD | 2,900.00 USD | `-9.16%` | `15,565.00` |
| `Live` | `Long` | `0.1875` | 421,490.00 USD | 0.00 USD | 4,120.00 USD | `-8.67%` | `21,979.00` |
| `Live` | `Long` | `0.1885` | 417,370.00 USD | 0.00 USD | 9,670.00 USD | `-8.19%` | `51,278.00` |
| `Live` | `Long` | `0.1895` | 407,700.00 USD | 0.00 USD | 10,260.00 USD | `-7.70%` | `54,132.00` |
| `Live` | `Long` | `0.1905` | 397,450.00 USD | 0.00 USD | 13,110.00 USD | `-7.21%` | `68,819.00` |
| `Live` | `Long` | `0.1915` | 384,340.00 USD | 0.00 USD | 27,820.00 USD | `-6.73%` | `145,262.00` |
| `Live` | `Long` | `0.1925` | 356,520.00 USD | 0.00 USD | 50,480.00 USD | `-6.24%` | `262,243.00` |
| `Live` | `Long` | `0.1935` | 306,040.00 USD | 0.00 USD | 290,550.00 USD | `-5.75%` | `1,501,558.00` |
| `Live` | `Long` | `0.1945` | 15,480.00 USD | 0.00 USD | 6,000.00 USD | `-5.27%` | `30,842.00` |
| `Live` | `Long` | `0.1955` | 9,490.00 USD | 0.00 USD | 8,500.00 USD | `-4.78%` | `43,495.00` |
| `Live` | `Long` | `0.1965` | 982.50 USD | 0.00 USD | 982.50 USD | `-4.29%` | `5,000.00` |
| `Live` | `Short` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | `+3.99%` | `3,351.00` |
| `Live` | `Short` | `0.2155` | 5,010.00 USD | 4,300.00 USD | 0.00 USD | `+4.96%` | `19,938.00` |
| `Live` | `Short` | `0.2175` | 5,120.00 USD | 104.40 USD | 0.00 USD | `+5.94%` | `480.00` |
| `Live` | `Short` | `0.2185` | 24,020.00 USD | 18,910.00 USD | 0.00 USD | `+6.42%` | `86,525.00` |
| `Live` | `Short` | `0.2215` | 25,670.00 USD | 1,640.00 USD | 0.00 USD | `+7.89%` | `7,424.00` |
| `Live` | `Short` | `0.2235` | 25,870.00 USD | 200.48 USD | 0.00 USD | `+8.86%` | `897.00` |
| `Live` | `Short` | `0.2275` | 28,030.00 USD | 2,160.00 USD | 0.00 USD | `+10.81%` | `9,500.00` |
| `Live` | `Short` | `0.2285` | 37,270.00 USD | 9,240.00 USD | 0.00 USD | `+11.30%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 39,250.00 USD | 1,980.00 USD | 0.00 USD | `+13.24%` | `8,516.00` |
| `Live` | `Short` | `0.2335` | 46,880.00 USD | 7,640.00 USD | 0.00 USD | `+13.73%` | `32,708.00` |
| `Live` | `Short` | `0.2355` | 57,350.00 USD | 10,470.00 USD | 0.00 USD | `+14.70%` | `44,446.00` |
| `Live` | `Short` | `0.2395` | 57,860.00 USD | 511.57 USD | 0.00 USD | `+16.65%` | `2,136.00` |
| `Live` | `Short` | `0.2405` | 59,330.00 USD | 1,470.00 USD | 0.00 USD | `+17.14%` | `6,110.00` |
| `Live` | `Short` | `0.2415` | 60,080.00 USD | 743.58 USD | 0.00 USD | `+17.63%` | `3,079.00` |
| `Live` | `Short` | `0.2525` | 88,440.00 USD | 28,370.00 USD | 0.00 USD | `+22.98%` | `112,352.00` |
| `Live` | `Short` | `0.2585` | 88,820.00 USD | 380.25 USD | 0.00 USD | `+25.91%` | `1,471.00` |
| `Live` | `Short` | `0.2615` | 90,220.00 USD | 1,400.00 USD | 0.00 USD | `+27.37%` | `5,346.00` |
| `Live` | `Short` | `0.2765` | 104,280.00 USD | 14,060.00 USD | 0.00 USD | `+34.67%` | `50,841.00` |
| `Live` | `Short` | `0.2775` | 104,800.00 USD | 520.31 USD | 0.00 USD | `+35.16%` | `1,875.00` |
| `Live` | `Short` | `0.2845` | 106,970.00 USD | 2,170.00 USD | 0.00 USD | `+38.57%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 107,380.00 USD | 411.09 USD | 0.00 USD | `+41.01%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 110,650.00 USD | 3,260.00 USD | 0.00 USD | `+41.98%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 111,170.00 USD | 519.79 USD | 0.00 USD | `+42.95%` | `1,771.00` |
| `Live` | `Short` | `0.2955` | 119,150.00 USD | 7,990.00 USD | 0.00 USD | `+43.93%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 119,300.00 USD | 146.34 USD | 0.00 USD | `+46.36%` | `487.00` |
| `Live` | `Short` | `0.3055` | 119,710.00 USD | 408.15 USD | 0.00 USD | `+48.80%` | `1,336.00` |
| `Live` | `Short` | `0.3105` | 216,590.00 USD | 96,880.00 USD | 0.00 USD | `+51.23%` | `312,021.00` |
| `Live` | `Short` | `0.3115` | 216,710.00 USD | 114.32 USD | 0.00 USD | `+51.72%` | `367.00` |
| `Live` | `Short` | `0.3175` | 217,010.00 USD | 301.62 USD | 0.00 USD | `+54.64%` | `950.00` |
| `Live` | `Short` | `0.3295` | 219,390.00 USD | 2,380.00 USD | 0.00 USD | `+60.49%` | `7,219.00` |
| `Live` | `Short` | `0.3345` | 219,630.00 USD | 239.50 USD | 0.00 USD | `+62.92%` | `716.00` |
| `Live` | `Short` | `0.3385` | 220,690.00 USD | 1,060.00 USD | 0.00 USD | `+64.87%` | `3,140.00` |
| `Live` | `Short` | `0.3395` | 223,240.00 USD | 2,550.00 USD | 0.00 USD | `+65.36%` | `7,515.00` |
| `Live` | `Short` | `0.3415` | 227,850.00 USD | 4,610.00 USD | 0.00 USD | `+66.33%` | `13,504.00` |
| `Live` | `Short` | `0.3465` | 233,870.00 USD | 6,020.00 USD | 0.00 USD | `+68.77%` | `17,368.00` |
| `Live` | `Short` | `0.3495` | 323,990.00 USD | 90,120.00 USD | 0.00 USD | `+70.23%` | `257,847.00` |
| `Live` | `Short` | `0.3505` | 325,480.00 USD | 1,490.00 USD | 0.00 USD | `+70.72%` | `4,254.00` |
| `Live` | `Short` | `0.3575` | 351,920.00 USD | 26,440.00 USD | 0.00 USD | `+74.13%` | `73,959.00` |
| `Live` | `Short` | `0.3585` | 352,490.00 USD | 575.03 USD | 0.00 USD | `+74.61%` | `1,604.00` |
| `Live` | `Short` | `0.3715` | 361,810.00 USD | 9,320.00 USD | 0.00 USD | `+80.95%` | `25,090.00` |
| `Live` | `Short` | `0.3745` | 364,960.00 USD | 3,140.00 USD | 0.00 USD | `+82.41%` | `8,395.00` |
| `Live` | `Short` | `0.3845` | 2,670,000.00 USD | 2,310,000.00 USD | 0.00 USD | `+87.28%` | `5,998,812.00` |
| `Live` | `Short` | `0.3915` | 2,670,000.00 USD | 788.87 USD | 0.00 USD | `+90.69%` | `2,015.00` |
| `Live` | `Short` | `0.3925` | 2,700,000.00 USD | 26,120.00 USD | 0.00 USD | `+91.17%` | `66,555.00` |
| `Live` | `Short` | `0.3935` | 2,700,000.00 USD | 280.17 USD | 0.00 USD | `+91.66%` | `712.00` |
| `Live` | `Short` | `0.3995` | 2,700,000.00 USD | 1,030.00 USD | 0.00 USD | `+94.58%` | `2,588.00` |
| `Live` | `Short` | `0.4045` | 2,710,000.00 USD | 6,820.00 USD | 0.00 USD | `+97.02%` | `16,862.00` |
| `Live` | `Short` | `0.4075` | 3,000,000.00 USD | 293,710.00 USD | 0.00 USD | `+98.48%` | `720,753.00` |
| `Live` | `Short` | `0.4085` | 3,000,000.00 USD | 2,060.00 USD | 0.00 USD | `+98.97%` | `5,039.00` |
| `Live` | `Short` | `0.4095` | 3,000,000.00 USD | 1,040.00 USD | 0.00 USD | `+99.45%` | `2,543.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 762,380,000.00 USD | 0.00 USD | 415.13 USD | `-71.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 762,380,000.00 USD | 0.00 USD | 1,100.00 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 762,380,000.00 USD | 0.00 USD | 541.33 USD | `-45.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 762,380,000.00 USD | 0.00 USD | 602,500.00 USD | `-41.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 761,780,000.00 USD | 0.00 USD | 1,320.00 USD | `-37.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 761,780,000.00 USD | 0.00 USD | 13,390.00 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 761,760,000.00 USD | 0.00 USD | 728.88 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 761,760,000.00 USD | 0.00 USD | 4,350.00 USD | `-34.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 761,760,000.00 USD | 0.00 USD | 542.99 USD | `-33.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 761,760,000.00 USD | 0.00 USD | 1,820.00 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 761,760,000.00 USD | 0.00 USD | 1,050.00 USD | `-31.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 761,760,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 761,750,000.00 USD | 0.00 USD | 1,600.00 USD | `-30.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 761,750,000.00 USD | 0.00 USD | 4,580.00 USD | `-29.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 761,750,000.00 USD | 0.00 USD | 303.26 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 761,750,000.00 USD | 0.00 USD | 1,290.00 USD | `-26.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 761,750,000.00 USD | 0.00 USD | 279.53 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 761,750,000.00 USD | 0.00 USD | 324.30 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 761,740,000.00 USD | 0.00 USD | 1,480.00 USD | `-24.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 761,740,000.00 USD | 0.00 USD | 552.21 USD | `-22.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 761,740,000.00 USD | 0.00 USD | 166.84 USD | `-22.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 761,740,000.00 USD | 0.00 USD | 2,990.00 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 761,740,000.00 USD | 0.00 USD | 562.67 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 761,740,000.00 USD | 0.00 USD | 24,760.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 761,710,000.00 USD | 0.00 USD | 6,540.00 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 761,710,000.00 USD | 0.00 USD | 2,870.00 USD | `-19.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 761,710,000.00 USD | 0.00 USD | 452.97 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 761,700,000.00 USD | 0.00 USD | 13,930.00 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 761,690,000.00 USD | 0.00 USD | 317.92 USD | `-18.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 761,690,000.00 USD | 0.00 USD | 6,740.00 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 761,680,000.00 USD | 0.00 USD | 4,270.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 761,680,000.00 USD | 0.00 USD | 7,630.00 USD | `-16.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 761,670,000.00 USD | 0.00 USD | 6,860.00 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 761,660,000.00 USD | 0.00 USD | 6,900.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 761,660,000.00 USD | 0.00 USD | 103.58 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 761,660,000.00 USD | 0.00 USD | 8,220.00 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 761,650,000.00 USD | 0.00 USD | 1,760.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 761,650,000.00 USD | 0.00 USD | 623.57 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 761,650,000.00 USD | 0.00 USD | 4,440.00 USD | `-13.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 761,640,000.00 USD | 0.00 USD | 12,390.00 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 761,630,000.00 USD | 0.00 USD | 5,760.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 761,620,000.00 USD | 0.00 USD | 26,470.00 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 761,600,000.00 USD | 0.00 USD | 2,400.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 761,600,000.00 USD | 0.00 USD | 2,190.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 761,590,000.00 USD | 0.00 USD | 3,160.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 761,590,000.00 USD | 0.00 USD | 18,650.00 USD | `-10.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 761,570,000.00 USD | 0.00 USD | 282.33 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 761,570,000.00 USD | 0.00 USD | 218.76 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 761,570,000.00 USD | 0.00 USD | 109.69 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 761,570,000.00 USD | 0.00 USD | 7,390.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 761,560,000.00 USD | 0.00 USD | 837.40 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 761,560,000.00 USD | 0.00 USD | 16,100.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 761,550,000.00 USD | 0.00 USD | 123.71 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 761,550,000.00 USD | 0.00 USD | 211.37 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 761,550,000.00 USD | 0.00 USD | 2,480.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 761,540,000.00 USD | 0.00 USD | 2,620.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 761,540,000.00 USD | 0.00 USD | 2,050.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 761,540,000.00 USD | 0.00 USD | 2,380.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 761,540,000.00 USD | 0.00 USD | 79,010,000.00 USD | `-3.80%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 682,530,000.00 USD | 0.00 USD | 79,400,000.00 USD | `-3.32%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 603,130,000.00 USD | 0.00 USD | 319,210,000.00 USD | `-2.83%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 283,920,000.00 USD | 0.00 USD | 80,200,000.00 USD | `-2.34%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 203,720,000.00 USD | 0.00 USD | 40,300,000.00 USD | `-1.86%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2025` | 163,420,000.00 USD | 0.00 USD | 10,120.00 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 163,400,000.00 USD | 0.00 USD | 40,700,000.00 USD | `-0.88%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2045` | 122,700,000.00 USD | 0.00 USD | 122,700,000.00 USD | `-0.39%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2055` | 82,200,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+0.09%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 82,200,000.00 USD | 1,260.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 82,210,000.00 USD | 8,020.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 82,210,000.00 USD | 2,120.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 82,220,000.00 USD | 8,720.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 82,250,000.00 USD | 34,460.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 82,270,000.00 USD | 12,990.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 82,270,000.00 USD | 1,700.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 82,280,000.00 USD | 10,740.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 82,280,000.00 USD | 2,460.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 82,290,000.00 USD | 2,720.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 82,290,000.00 USD | 109.77 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 82,290,000.00 USD | 109.91 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 82,290,000.00 USD | 584.97 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 82,410,000.00 USD | 125,830.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 82,410,000.00 USD | 1,650.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 82,420,000.00 USD | 1,690.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 82,420,000.00 USD | 501.31 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 82,420,000.00 USD | 6,860.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 82,420,000.00 USD | 341.18 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 82,420,000.00 USD | 109.40 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 82,440,000.00 USD | 21,490.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 82,450,000.00 USD | 9,140.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 82,460,000.00 USD | 9,180.00 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 82,460,000.00 USD | 662.92 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 82,470,000.00 USD | 9,600.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 82,470,000.00 USD | 171.12 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 82,480,000.00 USD | 9,340.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 82,480,000.00 USD | 1,010.00 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 82,490,000.00 USD | 9,420.00 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 82,490,000.00 USD | 315.96 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 82,490,000.00 USD | 650.04 USD | 0.00 USD | `+15.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 82,490,000.00 USD | 192.71 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 82,510,000.00 USD | 12,620.00 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 82,510,000.00 USD | 209.72 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 82,510,000.00 USD | 115.92 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 82,520,000.00 USD | 10,930.00 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 82,520,000.00 USD | 288.22 USD | 0.00 USD | `+19.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 82,520,000.00 USD | 491.03 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 82,520,000.00 USD | 1,320.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 82,530,000.00 USD | 10,630.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 82,530,000.00 USD | 499.00 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 82,530,000.00 USD | 1,100.00 USD | 0.00 USD | `+22.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 82,530,000.00 USD | 168.76 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 82,530,000.00 USD | 603.73 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 82,540,000.00 USD | 2,170.00 USD | 0.00 USD | `+23.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 82,540,000.00 USD | 1,570.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 82,540,000.00 USD | 1,470.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 82,540,000.00 USD | 271.44 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 82,960,000.00 USD | 421,430.00 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 82,960,000.00 USD | 945.98 USD | 0.00 USD | `+29.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 82,970,000.00 USD | 8,890.00 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 82,980,000.00 USD | 14,860.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 82,990,000.00 USD | 3,920.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 82,990,000.00 USD | 1,310.00 USD | 0.00 USD | `+32.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 83,000,000.00 USD | 13,870.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 83,010,000.00 USD | 4,960.00 USD | 0.00 USD | `+33.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 83,010,000.00 USD | 944.99 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 83,010,000.00 USD | 161.87 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 83,010,000.00 USD | 542.34 USD | 0.00 USD | `+38.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 83,010,000.00 USD | 1,370.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 83,010,000.00 USD | 1,080.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 83,030,000.00 USD | 15,160.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 83,030,000.00 USD | 796.09 USD | 0.00 USD | `+41.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 83,030,000.00 USD | 1,440.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 83,030,000.00 USD | 355.21 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 83,040,000.00 USD | 6,950.00 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 83,060,000.00 USD | 18,980.00 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 83,060,000.00 USD | 4,150.00 USD | 0.00 USD | `+50.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 83,060,000.00 USD | 3,250.00 USD | 0.00 USD | `+53.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 83,070,000.00 USD | 5,090.00 USD | 0.00 USD | `+56.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 83,070,000.00 USD | 1,450.00 USD | 0.00 USD | `+58.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 83,070,000.00 USD | 181.30 USD | 0.00 USD | `+58.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 83,070,000.00 USD | 1,380.00 USD | 0.00 USD | `+60.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 83,080,000.00 USD | 12,290.00 USD | 0.00 USD | `+61.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 83,080,000.00 USD | 111.06 USD | 0.00 USD | `+62.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 83,080,000.00 USD | 220.61 USD | 0.00 USD | `+66.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 83,090,000.00 USD | 3,850.00 USD | 0.00 USD | `+70.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 83,090,000.00 USD | 188.75 USD | 0.00 USD | `+83.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 83,090,000.00 USD | 121.76 USD | 0.00 USD | `+85.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 83,090,000.00 USD | 141.78 USD | 0.00 USD | `+89.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 83,090,000.00 USD | 393.50 USD | 0.00 USD | `+91.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 83,090,000.00 USD | 1,260.00 USD | 0.00 USD | `+92.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.1770` | 11,340,000.00 USD | 0.00 USD | 11,340,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD |
| `7D` | `0.1780` | 11,270,000.00 USD | 0.00 USD | 11,270,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD |
| `7D` | `0.1790` | 11,200,000.00 USD | 0.00 USD | 11,200,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD |
| `7D` | `0.1800` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `7D` | `0.1810` | 11,150,000.00 USD | 0.00 USD | 11,150,000.00 USD | 112,560.00 USD | 27,510.00 USD | 31,310.00 USD |
| `7D` | `0.1820` | 10,980,000.00 USD | 0.00 USD | 10,980,000.00 USD | 95,280.00 USD | 47,480.00 USD | 117,770.00 USD |
| `7D` | `0.1830` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 84,560.00 USD | 36,880.00 USD | 59,960.00 USD |
| `1D` | `0.1840` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 141,830.00 USD | 33,300.00 USD | 35,850.00 USD |
| `7D` | `0.1840` | 10,540,000.00 USD | 0.00 USD | 10,540,000.00 USD | 226,530.00 USD | 58,050.00 USD | 174,570.00 USD |
| `1D` | `0.1850` | 10,450,000.00 USD | 0.00 USD | 10,450,000.00 USD | 163,720.00 USD | 57,260.00 USD | 98,630.00 USD |
| `7D` | `0.1850` | 10,080,000.00 USD | 0.00 USD | 10,080,000.00 USD | 404,170.00 USD | 111,470.00 USD | 387,400.00 USD |
| `1D` | `0.1860` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 35,280.00 USD | 8,700.00 USD | 12,970.00 USD |
| `7D` | `0.1860` | 9,170,000.00 USD | 0.00 USD | 9,170,000.00 USD | 114,090.00 USD | 56,980.00 USD | 194,130.00 USD |
| `1D` | `0.1870` | 10,070,000.00 USD | 0.00 USD | 10,070,000.00 USD | 78,720.00 USD | 14,920.00 USD | 15,560.00 USD |
| `7D` | `0.1870` | 8,810,000.00 USD | 0.00 USD | 8,810,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 9,960,000.00 USD | 0.00 USD | 9,960,000.00 USD | 219,090.00 USD | 32,270.00 USD | 34,270.00 USD |
| `7D` | `0.1880` | 8,550,000.00 USD | 0.00 USD | 8,550,000.00 USD | 158,590.00 USD | 41,220.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 101,860.00 USD | 72,430.00 USD | 184,140.00 USD |
| `7D` | `0.1890` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 246,750.00 USD | 52,560.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 247,200.00 USD | 105,640.00 USD | 203,280.00 USD |
| `7D` | `0.1900` | 7,870,000.00 USD | 0.00 USD | 7,870,000.00 USD | 247,920.00 USD | 72,080.00 USD | 235,020.00 USD |
| `1D` | `0.1910` | 8,760,000.00 USD | 0.00 USD | 8,760,000.00 USD | 230,970.00 USD | 82,400.00 USD | 91,380.00 USD |
| `7D` | `0.1910` | 7,320,000.00 USD | 0.00 USD | 7,320,000.00 USD | 258,450.00 USD | 86,060.00 USD | 16,510.00 USD |
| `1D` | `0.1920` | 8,360,000.00 USD | 0.00 USD | 8,360,000.00 USD | 486,530.00 USD | 114,180.00 USD | 182,050.00 USD |
| `7D` | `0.1920` | 6,960,000.00 USD | 0.00 USD | 6,960,000.00 USD | 257,730.00 USD | 74,890.00 USD | 77,590.00 USD |
| `1D` | `0.1930` | 7,580,000.00 USD | 0.00 USD | 7,580,000.00 USD | 300,360.00 USD | 196,980.00 USD | 468,610.00 USD |
| `7D` | `0.1930` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 722,350.00 USD | 159,940.00 USD | 323,790.00 USD |
| `1D` | `0.1940` | 6,610,000.00 USD | 0.00 USD | 6,610,000.00 USD | 625,710.00 USD | 252,190.00 USD | 513,100.00 USD |
| `7D` | `0.1940` | 5,340,000.00 USD | 0.00 USD | 5,340,000.00 USD | 678,880.00 USD | 259,610.00 USD | 823,650.00 USD |
| `1D` | `0.1950` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 514,200.00 USD | 173,220.00 USD | 212,250.00 USD |
| `7D` | `0.1950` | 3,580,000.00 USD | 0.00 USD | 3,580,000.00 USD | 619,180.00 USD | 288,290.00 USD | 388,420.00 USD |
| `1D` | `0.1960` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 451,150.00 USD | 148,090.00 USD | 319,220.00 USD |
| `7D` | `0.1960` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 99,630.00 USD | 9,990.00 USD | 676,700.00 USD |
| `1D` | `0.1970` | 3,400,000.00 USD | 0.00 USD | 3,400,000.00 USD | 324,400.00 USD | 149,150.00 USD | 272,570.00 USD |
| `7D` | `0.1970` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 80,840.00 USD | 56,210.00 USD | 133,500.00 USD |
| `1D` | `0.1980` | 2,650,000.00 USD | 0.00 USD | 2,650,000.00 USD | 299,150.00 USD | 92,080.00 USD | 129,720.00 USD |
| `7D` | `0.1980` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 20,720.00 USD | 1,190.00 USD |
| `1D` | `0.1990` | 2,130,000.00 USD | 0.00 USD | 2,130,000.00 USD | 26,640.00 USD | 0.00 USD | 11,160.00 USD |
| `7D` | `0.1990` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD |
| `1D` | `0.2000` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 109,830.00 USD | 70,030.00 USD | 137,880.00 USD |
| `7D` | `0.2000` | 31,080.00 USD | 0.00 USD | 31,080.00 USD | 0.00 USD | 25,400.00 USD | 5,680.00 USD |
| `1D` | `0.2010` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 278,340.00 USD | 79,030.00 USD | 177,290.00 USD |
| `7D` | `0.2010` | 602,690.00 USD | 602,690.00 USD | 0.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD |
| `7D` | `0.2010` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD |
| `1D` | `0.2020` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 211,750.00 USD | 53,220.00 USD | 71,740.00 USD |
| `7D` | `0.2020` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 154,520.00 USD | 0.00 USD | 360,160.00 USD |
| `1D` | `0.2030` | 906,000.00 USD | 0.00 USD | 906,000.00 USD | 462,960.00 USD | 151,590.00 USD | 291,450.00 USD |
| `7D` | `0.2030` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 173,570.00 USD | 109,540.00 USD | 0.00 USD |
| `1D` | `0.2040` | 286,440.00 USD | 286,440.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 82,780.00 USD |
| `1D` | `0.2040` | 572,890.00 USD | 572,890.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 82,780.00 USD |
| `7D` | `0.2040` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 125,120.00 USD | 53,690.00 USD | 215,230.00 USD |
| `1D` | `0.2050` | 584,830.00 USD | 584,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 11,940.00 USD |
| `7D` | `0.2050` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 276,760.00 USD | 82,430.00 USD | 242,780.00 USD |
| `1D` | `0.2060` | 597,230.00 USD | 597,230.00 USD | 0.00 USD | 0.00 USD | 1,350.00 USD | 11,060.00 USD |
| `7D` | `0.2060` | 3,380,000.00 USD | 3,380,000.00 USD | 0.00 USD | 144,470.00 USD | 31,310.00 USD | 206,030.00 USD |
| `1D` | `0.2070` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 409,780.00 USD | 106,370.00 USD | 150,360.00 USD |
| `7D` | `0.2070` | 3,910,000.00 USD | 3,910,000.00 USD | 0.00 USD | 385,560.00 USD | 80,540.00 USD | 58,420.00 USD |
| `1D` | `0.2080` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 450,830.00 USD | 152,560.00 USD | 5,890.00 USD |
| `7D` | `0.2080` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 552,200.00 USD | 44,630.00 USD | 65,200.00 USD |
| `1D` | `0.2090` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 542,330.00 USD | 189,870.00 USD | 282,450.00 USD |
| `7D` | `0.2090` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 2,010,000.00 USD | 87,520.00 USD | 155,450.00 USD |
| `1D` | `0.2100` | 4,260,000.00 USD | 4,260,000.00 USD | 0.00 USD | 637,140.00 USD | 247,430.00 USD | 488,790.00 USD |
| `7D` | `0.2100` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 1,560,000.00 USD | 660,820.00 USD | 1,570,000.00 USD |
| `1D` | `0.2110` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 259,670.00 USD | 54,340.00 USD | 138,190.00 USD |
| `7D` | `0.2110` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 1,030,000.00 USD | 499,260.00 USD | 1,460,000.00 USD |
| `1D` | `0.2120` | 5,290,000.00 USD | 5,290,000.00 USD | 0.00 USD | 282,550.00 USD | 112,530.00 USD | 182,810.00 USD |
| `7D` | `0.2120` | 16,490,000.00 USD | 16,490,000.00 USD | 0.00 USD | 1,120,000.00 USD | 463,080.00 USD | 1,320,000.00 USD |
| `1D` | `0.2130` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 340,500.00 USD | 103,220.00 USD | 223,210.00 USD |
| `7D` | `0.2130` | 18,970,000.00 USD | 18,970,000.00 USD | 0.00 USD | 1,090,000.00 USD | 289,130.00 USD | 1,100,000.00 USD |
| `1D` | `0.2140` | 6,570,000.00 USD | 6,570,000.00 USD | 0.00 USD | 314,560.00 USD | 103,250.00 USD | 191,120.00 USD |
| `7D` | `0.2140` | 21,000,000.00 USD | 21,000,000.00 USD | 0.00 USD | 820,780.00 USD | 379,940.00 USD | 830,800.00 USD |
| `1D` | `0.2150` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 75,880.00 USD | 19,010.00 USD | 54,350.00 USD |
| `7D` | `0.2150` | 23,230,000.00 USD | 23,230,000.00 USD | 0.00 USD | 916,150.00 USD | 316,800.00 USD | 1,000,000.00 USD |
| `1D` | `0.2160` | 6,910,000.00 USD | 6,910,000.00 USD | 0.00 USD | 117,430.00 USD | 35,330.00 USD | 40,150.00 USD |
| `7D` | `0.2160` | 24,240,000.00 USD | 24,240,000.00 USD | 0.00 USD | 447,110.00 USD | 164,960.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 76,340.00 USD | 28,650.00 USD | 116,750.00 USD |
| `7D` | `0.2170` | 24,870,000.00 USD | 24,870,000.00 USD | 0.00 USD | 296,410.00 USD | 94,900.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 85,920.00 USD | 30,810.00 USD | 63,140.00 USD |
| `7D` | `0.2180` | 25,390,000.00 USD | 25,390,000.00 USD | 0.00 USD | 266,770.00 USD | 102,870.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 7,460,000.00 USD | 7,460,000.00 USD | 0.00 USD | 83,440.00 USD | 28,270.00 USD | 33,840.00 USD |
| `7D` | `0.2190` | 26,600,000.00 USD | 26,600,000.00 USD | 0.00 USD | 630,760.00 USD | 188,070.00 USD | 391,710.00 USD |
| `1D` | `0.2200` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 85,310.00 USD | 24,670.00 USD | 41,470.00 USD |
| `7D` | `0.2200` | 27,920,000.00 USD | 27,920,000.00 USD | 0.00 USD | 558,280.00 USD | 232,970.00 USD | 526,970.00 USD |
| `1D` | `0.2210` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 45,350.00 USD | 17,440.00 USD | 27,870.00 USD |
| `7D` | `0.2210` | 28,950,000.00 USD | 28,950,000.00 USD | 0.00 USD | 532,080.00 USD | 84,700.00 USD | 416,740.00 USD |
| `1D` | `0.2220` | 7,790,000.00 USD | 7,790,000.00 USD | 0.00 USD | 51,150.00 USD | 11,430.00 USD | 32,950.00 USD |
| `7D` | `0.2220` | 29,420,000.00 USD | 29,420,000.00 USD | 0.00 USD | 188,710.00 USD | 86,520.00 USD | 195,670.00 USD |
| `1D` | `0.2230` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 46,180.00 USD | 6,100.00 USD | 5,080.00 USD |
| `7D` | `0.2230` | 29,710,000.00 USD | 29,710,000.00 USD | 0.00 USD | 149,810.00 USD | 47,320.00 USD | 85,130.00 USD |
| `1D` | `0.2240` | 7,960,000.00 USD | 7,960,000.00 USD | 0.00 USD | 53,080.00 USD | 23,430.00 USD | 30,770.00 USD |
| `1D` | `0.2260` | 8,080,000.00 USD | 8,080,000.00 USD | 0.00 USD | 71,130.00 USD | 26,160.00 USD | 28,910.00 USD |
| `1D` | `0.2270` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 61,490.00 USD | 29,170.00 USD | 69,720.00 USD |
| `1D` | `0.2280` | 8,280,000.00 USD | 8,280,000.00 USD | 0.00 USD | 12,350.00 USD | 5,470.00 USD | 12,970.00 USD |
| `1D` | `0.2290` | 8,310,000.00 USD | 8,310,000.00 USD | 0.00 USD | 8,350.00 USD | 8,950.00 USD | 15,560.00 USD |
| `1D` | `0.2300` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 12,650.00 USD | 5,500.00 USD | 19,370.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `455.13M` | Total OI Tokens: `2,225,427,948.3 ADA`
  * 1h OI Change: `-1.24%` | 4h OI Change: `+0.85%` | 24h OI Change: `-1.83%`
  * Exchange Breakdown: Binance=`85.67M` | Bybit=`54.28M` | OKX=`32.11M` | Hyperliquid=`30.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.35K` | Last 24h: `14.21K` | Last 3d: `57.26K` | Last 7d: `58.11K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0023%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `46.18%` | `53.82%` | `0.86` | 16,170,000.00 USD |
| `15M` | `Binance` | `46.53%` | `53.47%` | `0.87` | 5,310,000.00 USD |
| `15M` | `OKX` | `45.4%` | `54.6%` | `0.83` | 3,670,000.00 USD |
| `15M` | `Bybit` | `51.24%` | `48.76%` | `1.05` | 1,640,000.00 USD |
| `15M` | `KuCoin` | `45.72%` | `54.28%` | `0.84` | 101,360.00 USD |
| `15M` | `Gate` | `48.55%` | `51.45%` | `0.94` | 2,230,000.00 USD |
| `15M` | `Bitget` | `37.1%` | `62.9%` | `0.59` | 290,740.00 USD |
| `15M` | `BingX` | `41.52%` | `58.48%` | `0.71` | 774,860.00 USD |
| `15M` | `MEXC` | `39.8%` | `60.2%` | `0.66` | 1,050,000.00 USD |
| `15M` | `Bitunix` | `45.6%` | `54.4%` | `0.84` | 368,640.00 USD |
| `15M` | `Hyperliquid` | `52.44%` | `47.56%` | `1.10` | 72,080.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `51.81%` | `48.19%` | `1.08` | 55,170.00 USD |
| `15M` | `Crypto.com` | `43.03%` | `56.97%` | `0.76` | 29,170.00 USD |
| `15M` | `WhiteBIT` | `38.49%` | `61.51%` | `0.63` | 307,340.00 USD |
| `15M` | `HTX` | `28.74%` | `71.26%` | `0.40` | 25,680.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `22.11%` | `77.89%` | `0.28` | 100,270.00 USD |
| `15M` | `Aster` | `86.7%` | `13.3%` | `6.52` | 131,840.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `24.49%` | `75.51%` | `0.32` | 4,660.00 USD |
| `15M` | `Whale Positions` | `46.53%` | `53.47%` | `0.87` | 5,310,000.00 USD |
| `15M` | `Global Accounts` | `46.18%` | `53.82%` | `0.86` | 16,170,000.00 USD |
| `1H` | `ADA` | `44.45%` | `55.55%` | `0.80` | 79,690,000.00 USD |
| `1H` | `Binance` | `45.25%` | `54.75%` | `0.83` | 28,040,000.00 USD |
| `1H` | `OKX` | `43.7%` | `56.3%` | `0.78` | 15,990,000.00 USD |
| `1H` | `Bybit` | `48.38%` | `51.62%` | `0.94` | 5,850,000.00 USD |
| `1H` | `KuCoin` | `41.43%` | `58.57%` | `0.71` | 439,830.00 USD |
| `1H` | `Gate` | `50.59%` | `49.41%` | `1.02` | 10,930,000.00 USD |
| `1H` | `Bitget` | `28.9%` | `71.1%` | `0.41` | 2,150,000.00 USD |
| `1H` | `BingX` | `18.89%` | `81.11%` | `0.23` | 4,130,000.00 USD |
| `1H` | `MEXC` | `45.28%` | `54.72%` | `0.83` | 5,230,000.00 USD |
| `1H` | `Bitunix` | `46.81%` | `53.19%` | `0.88` | 2,050,000.00 USD |
| `1H` | `Hyperliquid` | `50.23%` | `49.77%` | `1.01` | 1,910,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.14%` | `48.86%` | `1.05` | 251,860.00 USD |
| `1H` | `Crypto.com` | `50.3%` | `49.7%` | `1.01` | 104,670.00 USD |
| `1H` | `WhiteBIT` | `47.42%` | `52.58%` | `0.90` | 1,310,000.00 USD |
| `1H` | `HTX` | `49%` | `51%` | `0.96` | 337,490.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `46.86%` | `53.14%` | `0.88` | 341,800.00 USD |
| `1H` | `Aster` | `67.67%` | `32.33%` | `2.09` | 546,130.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `22.25%` | `77.75%` | `0.29` | 78,940.00 USD |
| `1H` | `Whale Positions` | `45.25%` | `54.75%` | `0.83` | 28,040,000.00 USD |
| `1H` | `Global Accounts` | `44.45%` | `55.55%` | `0.80` | 79,690,000.00 USD |
| `4H` | `ADA` | `50.05%` | `49.95%` | `1.00` | 344,410,000.00 USD |
| `4H` | `Binance` | `50.88%` | `49.12%` | `1.04` | 123,220,000.00 USD |
| `4H` | `OKX` | `49.35%` | `50.65%` | `0.97` | 73,290,000.00 USD |
| `4H` | `Bybit` | `51.47%` | `48.53%` | `1.06` | 23,510,000.00 USD |
| `4H` | `KuCoin` | `44.37%` | `55.63%` | `0.80` | 2,520,000.00 USD |
| `4H` | `Gate` | `51.01%` | `48.99%` | `1.04` | 46,460,000.00 USD |
| `4H` | `Bitget` | `47.49%` | `52.51%` | `0.90` | 9,430,000.00 USD |
| `4H` | `BingX` | `33.27%` | `66.73%` | `0.50` | 8,960,000.00 USD |
| `4H` | `MEXC` | `49.3%` | `50.7%` | `0.97` | 28,130,000.00 USD |
| `4H` | `Bitunix` | `51.32%` | `48.68%` | `1.05` | 10,580,000.00 USD |
| `4H` | `Hyperliquid` | `52.1%` | `47.9%` | `1.09` | 3,460,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `53.14%` | `46.86%` | `1.13` | 1,410,000.00 USD |
| `4H` | `Crypto.com` | `51.11%` | `48.89%` | `1.05` | 338,480.00 USD |
| `4H` | `WhiteBIT` | `59.9%` | `40.1%` | `1.49` | 6,410,000.00 USD |
| `4H` | `HTX` | `47.98%` | `52.02%` | `0.92` | 1,700,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `46%` | `54%` | `0.85` | 1,490,000.00 USD |
| `4H` | `Aster` | `52.07%` | `47.93%` | `1.09` | 3,400,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `24.88%` | `75.12%` | `0.33` | 114,950.00 USD |
| `4H` | `Whale Positions` | `50.88%` | `49.12%` | `1.04` | 123,220,000.00 USD |
| `4H` | `Global Accounts` | `50.05%` | `49.95%` | `1.00` | 344,410,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.2037` | `0.2046` | `0.2037` | `0.2056` | `0.2036` | 2,360,300.33 USD | 1,286,747.96 USD | 1,073,552.36 USD | 213,195.60 USD | `+9.03%` | `4B / 1S` |
| `5:00 UTC` | `0.2049` | `0.2048` | `0.2049` | `0.2057` | `0.2041` | 2,372,003.28 USD | 1,123,364.70 USD | 1,248,638.58 USD | -125,273.88 USD | `-5.28%` | `1B / 1S` |
| `0:00 UTC` | `0.2051` | `0.2051` | `0.2051` | `0.2056` | `0.2042` | 2,366,919.63 USD | 1,383,725.71 USD | 983,193.92 USD | 400,531.79 USD | `+16.92%` | `1B / 0S` |
| `5:00 UTC` | `0.2054` | `0.2059` | `0.2054` | `0.2066` | `0.2049` | 3,269,747.09 USD | 1,525,563.65 USD | 1,744,183.44 USD | -218,619.79 USD | `-6.69%` | `1B / 1S` |
| `0:00 UTC` | `0.2064` | `0.2072` | `0.2064` | `0.2087` | `0.2056` | 5,724,356.79 USD | 3,224,697.96 USD | 2,499,658.83 USD | 725,039.12 USD | `+12.67%` | `4B / 0S` |
| `5:00 UTC` | `0.2061` | `0.2060` | `0.2061` | `0.2072` | `0.2054` | 2,545,595.94 USD | 1,190,541.20 USD | 1,355,054.75 USD | -164,513.55 USD | `-6.46%` | `0B / 1S` |
| `0:00 UTC` | `0.2052` | `0.2054` | `0.2052` | `0.2061` | `0.2047` | 2,681,797.52 USD | 1,504,963.17 USD | 1,176,834.35 USD | 328,128.82 USD | `+12.24%` | `2B / 1S` |
| `5:00 UTC` | `0.2054` | `0.2054` | `0.2054` | `0.2059` | `0.2051` | 1,103,361.90 USD | 582,275.03 USD | 521,086.87 USD | 61,188.16 USD | `+5.55%` | `1B / 1S` |
| `0:00 UTC` | `0.2047` | `0.2049` | `0.2047` | `0.2056` | `0.2042` | 2,508,493.59 USD | 1,331,643.13 USD | 1,176,850.47 USD | 154,792.66 USD | `+6.17%` | `1B / 1S` |
| `5:00 UTC` | `0.2044` | `0.2044` | `0.2044` | `0.2046` | `0.2041` | 773,898.09 USD | 341,421.72 USD | 432,476.38 USD | -91,054.66 USD | `-11.77%` | `0B / 0S` |

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
| `5m` | -92,600.00 USD | -118,060.00 USD | **`DISTRIBUTION`** |
| `15m` | -266,350.00 USD | -353,360.00 USD | **`DISTRIBUTION`** |
| `30m` | -317,870.00 USD | -264,690.00 USD | **`DISTRIBUTION`** |
| `1h` | -131,320.00 USD | -671,670.00 USD | **`DISTRIBUTION`** |
| `2h` | -239,240.00 USD | -792,570.00 USD | **`DISTRIBUTION`** |
| `4h` | -262,240.00 USD | 2,880,000.00 USD | **`ACCUMULATION`** |
| `6h` | -217,890.00 USD | 2,750,000.00 USD | **`ACCUMULATION`** |
| `8h` | -6,740.00 USD | 4,950,000.00 USD | **`ACCUMULATION`** |
| `12h` | -98,910.00 USD | 4,350,000.00 USD | **`ACCUMULATION`** |
| `24h` | -2,990,000.00 USD | -411,600.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,160,000.00 USD | -23,930,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -70,240,000.00 USD | -185,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-92.60K` | 15m=`-266.35K` | 1h=`-131.32K` | 24h=`-2.99M`
* Futures Capital Netflows: 5m=`-118.06K` | 15m=`-353.36K` | 1h=`-671.67K` | 24h=`-411.60K`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1976` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1926` (Risk Distance: `0.0050` pts)
  * +2.5R Take Profit: `0.2101`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2064` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2114` (Risk Distance: `0.0050` pts)
  * +2.5R Take Profit: `0.1939`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2057`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
