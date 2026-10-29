# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 23:10:16 IST` (`2026-10-29 17:40:16 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2031` | **Live Ask Quote**: `0.2052` | **Mid Price**: `0.2041`
- **Spread Points**: `21.00` | **Spread BPS**: `102.87 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.2041` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2056` | Lower -3.00σ Band: `0.2027`
  * Upper +2.51σ Band: `0.2053` | Lower -2.51σ Band: `0.2030`
  * Upper +2.01σ Band: `0.2050` | Lower -2.01σ Band: `0.2033`
  * Upper +2.00σ Band: `0.2050` | Lower -2.00σ Band: `0.2033`
  * Upper +1.28σ Band: `0.2047` | Lower -1.28σ Band: `0.2036`
  * Upper +1.00σ Band: `0.2046` | Lower -1.00σ Band: `0.2037`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2041` | EMA-20=`0.2041` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.2041` (Slope: `+0.0000`) | EMA-100=`0.2041`
  * Institutional Anchors: EMA-144=`0.2041` | EMA-200=`0.2041` (Slope: `+0.0000`) | EMA-233=`0.2041`
- **Range Boundaries**: 24H High=`0.2062` | 24H Low=`0.2021` | Weekly High=`0.2082` | Weekly Low=`0.2001`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2064` (Distance: `-0.99%`)
  * Point of Control (POC) = `0.2047` (Distance: `-0.16%`)
  * Value Area Low (VAL) = `0.1977` (Distance: `+3.34%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2058` | Weekly POC=`0.2031` | Weekly VAL=`0.2012`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2074` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2033` - `0.2050`
  * Optimal Trade Entry (OTE 0.705): `0.2046`
  * Structural Invalidation Anchor (0.786): `0.2058`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `539` | `0x77ee...2902` | `SHORT` | 4,378,150.90 USD | `21,412,192.00` | `0.1911` | `0.2044` | `0.5607` | -286,899.16 USD | `-6.55%` | `10X Cross` |
| `1200` | `0x123d...3bff` | `LONG` | 1,920,427.88 USD | `9,393,142.00` | `0.2912` | `0.2044` | `0.000000` | -815,308.06 USD | `-42.45%` | `10X Cross` |
| `1254` | `0x7737...bf66` | `SHORT` | 1,858,477.48 USD | `9,091,466.00` | `0.2190` | `0.2044` | `2.19` | 132,512.32 USD | `+7.13%` | `10X Cross` |
| `1554` | `0x5f94...4b96` | `SHORT` | 1,464,192.67 USD | `7,162,318.00` | `0.2303` | `0.2044` | `0.7729` | 185,282.53 USD | `+12.65%` | `10X Cross` |
| `1774` | `0x4982...59e6` | `SHORT` | 1,226,577.09 USD | `5,998,812.00` | `0.1891` | `0.2044` | `0.3857` | -92,018.73 USD | `-7.50%` | `10X Cross` |
| `1819` | `0xcac1...26b3` | `LONG` | 1,186,612.88 USD | `5,803,927.00` | `0.2000` | `0.2044` | `0.000000` | 25,797.29 USD | `+2.17%` | `10X Cross` |
| `2001` | `0x51f6...2b39` | `LONG` | 1,035,610.81 USD | `5,065,350.00` | `0.2294` | `0.2044` | `0.000000` | -126,538.78 USD | `-12.22%` | `10X Cross` |
| `2009` | `0xeadc...9d55` | `LONG` | 1,029,949.73 USD | `5,038,400.00` | `0.2195` | `0.2044` | `0.000000` | -75,763.02 USD | `-7.36%` | `10X Cross` |
| `2016` | `0x0748...d4b2` | `SHORT` | 1,022,250.00 USD | `5,000,000.00` | `0.2036` | `0.2044` | `0.6134` | -4,392.76 USD | `-0.43%` | `10X Cross` |
| `2047` | `0xfbe2...c8ea` | `LONG` | 1,006,525.34 USD | `4,923,088.00` | `0.2667` | `0.2044` | `0.0180` | -306,420.29 USD | `-30.44%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2067` | 6,278.84 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.28K USD at 0.2067 USD [API] | `2026-10-27 21:36:56` |
| `ANNOUNCEMENT` | `INFO` | `0.2063` | 6,645.63 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2063 USD [API] | `2026-10-27 21:39:43` |
| `ANNOUNCEMENT` | `INFO` | `0.2061` | 6,655.44 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.66K USD at 0.2061 USD [API] | `2026-10-27 21:46:03` |
| `ANNOUNCEMENT` | `INFO` | `0.2057` | 6,350.68 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.35K USD at 0.2057 USD [API] | `2026-10-27 21:53:01` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 6,153.52 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2051` | 9,856.01 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 9.86K USD at 0.2051 USD [API] | `2026-10-27 22:26:18` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,533.03 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.53K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2050` | 6,645.28 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.65K USD at 0.2050 USD [API] | `2026-10-27 22:28:45` |
| `ANNOUNCEMENT` | `INFO` | `0.2052` | 6,153.74 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2052 USD [API] | `2026-10-27 22:32:51` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+2.45%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.68%`)
  * 48H Horizon: Short MP=`0.2093` (Vol: 207,000.00 USD, Dist: `+2.45%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.68%`)
  * 3D Horizon: Short MP=`0.2137` (Vol: 261,100.00 USD, Dist: `+4.60%`) | Long MP=`0.1927` (Vol: 248,000.00 USD, Dist: `--5.68%`)
  * 7D Horizon: Short MP=`0.2124` (Vol: 359,800.00 USD, Dist: `+3.95%`) | Long MP=`0.1926` (Vol: 321,900.00 USD, Dist: `--5.73%`)
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
| `7D` | `Long Liquidation` | `0.1770` | 13,890,000.00 USD | 13,890,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 15,750.00 USD | 636,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1780` | 13,810,000.00 USD | 13,810,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 15,790.00 USD | 620,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,750,000.00 USD | 13,750,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 12,760.00 USD | 605,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,730,000.00 USD | 13,730,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 134,610.00 USD | 592,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,700,000.00 USD | 13,700,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 457,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1820` | 13,520,000.00 USD | 13,520,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,250.00 USD | 450,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.1830` | 13,240,000.00 USD | 13,240,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 431,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 10,720,000.00 USD | 10,720,000.00 USD | 147,760.00 USD | 32,900.00 USD | 35,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 13,060,000.00 USD | 13,060,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 431,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 10,510,000.00 USD | 10,510,000.00 USD | 163,720.00 USD | 57,850.00 USD | 98,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 12,570,000.00 USD | 12,570,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 6,190.00 USD | 430,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 10,190,000.00 USD | 10,190,000.00 USD | 35,280.00 USD | 9,470.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 11,560,000.00 USD | 11,560,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 2,900.00 USD | 424,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 10,130,000.00 USD | 10,130,000.00 USD | 78,720.00 USD | 13,620.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 11,180,000.00 USD | 11,180,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,120.00 USD | 421,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 10,020,000.00 USD | 10,020,000.00 USD | 219,090.00 USD | 32,770.00 USD | 34,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,920,000.00 USD | 10,920,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 9,670.00 USD | 417,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 9,730,000.00 USD | 9,730,000.00 USD | 101,860.00 USD | 72,520.00 USD | 183,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,660,000.00 USD | 10,660,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 10,260.00 USD | 407,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 9,380,000.00 USD | 9,380,000.00 USD | 248,740.00 USD | 105,170.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 10,220,000.00 USD | 10,220,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 13,110.00 USD | 397,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 8,820,000.00 USD | 8,820,000.00 USD | 230,970.00 USD | 83,930.00 USD | 90,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,680,000.00 USD | 9,680,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 27,820.00 USD | 384,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 8,410,000.00 USD | 8,410,000.00 USD | 486,530.00 USD | 112,840.00 USD | 185,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 9,320,000.00 USD | 9,320,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 50,480.00 USD | 356,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 7,630,000.00 USD | 7,630,000.00 USD | 283,810.00 USD | 196,480.00 USD | 462,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,890,000.00 USD | 8,890,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,550.00 USD | 306,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 6,690,000.00 USD | 6,690,000.00 USD | 627,770.00 USD | 252,610.00 USD | 512,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,640,000.00 USD | 7,640,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 6,000.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 5,290,000.00 USD | 5,290,000.00 USD | 514,200.00 USD | 174,610.00 USD | 209,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,820,000.00 USD | 5,820,000.00 USD | 627,100.00 USD | 289,850.00 USD | 389,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 8,500.00 USD | 9,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 4,400,000.00 USD | 4,400,000.00 USD | 472,120.00 USD | 147,670.00 USD | 324,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 4,520,000.00 USD | 4,520,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1965` | 982.50 USD | 982.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1970` | 3,450,000.00 USD | 3,450,000.00 USD | 324,400.00 USD | 149,540.00 USD | 270,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 3,640,000.00 USD | 3,640,000.00 USD | 220,950.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 2,710,000.00 USD | 2,710,000.00 USD | 299,150.00 USD | 92,270.00 USD | 133,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 3,020,000.00 USD | 3,020,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1990` | 2,180,000.00 USD | 2,180,000.00 USD | 26,640.00 USD | 0.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,830,000.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 2,150,000.00 USD | 2,150,000.00 USD | 151,770.00 USD | 70,030.00 USD | 146,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 1,620,000.00 USD | 1,620,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 1,780,000.00 USD | 1,780,000.00 USD | 278,340.00 USD | 79,030.00 USD | 167,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 1,430,000.00 USD | 1,430,000.00 USD | 209,620.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2020` | 1,250,000.00 USD | 1,250,000.00 USD | 211,750.00 USD | 53,220.00 USD | 77,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2020` | 864,540.00 USD | 864,540.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2030` | 910,790.00 USD | 910,790.00 USD | 462,960.00 USD | 151,590.00 USD | 296,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2030` | 354,090.00 USD | 354,090.00 USD | 173,570.00 USD | 109,540.00 USD | 70,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 287,440.00 USD | 287,440.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 574,880.00 USD | 574,880.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 53,690.00 USD | 53,690.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 107,380.00 USD | 107,380.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 587,390.00 USD | 587,390.00 USD | 0.00 USD | 1,760.00 USD | 10,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 115,990.00 USD | 115,990.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 1,250,000.00 USD | 1,250,000.00 USD | 409,780.00 USD | 102,110.00 USD | 145,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 538,120.00 USD | 538,120.00 USD | 341,590.00 USD | 80,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 1,910,000.00 USD | 1,910,000.00 USD | 492,770.00 USD | 153,120.00 USD | 16,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 1,180,000.00 USD | 1,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 2,930,000.00 USD | 2,930,000.00 USD | 542,330.00 USD | 190,640.00 USD | 285,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 4,030,000.00 USD | 4,030,000.00 USD | 2,230,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 4,300,000.00 USD | 4,300,000.00 USD | 637,140.00 USD | 246,150.00 USD | 495,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 8,020,000.00 USD | 8,020,000.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 4,760,000.00 USD | 4,760,000.00 USD | 259,670.00 USD | 55,140.00 USD | 142,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 11,090,000.00 USD | 11,090,000.00 USD | 1,040,000.00 USD | 502,740.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 5,360,000.00 USD | 5,360,000.00 USD | 303,520.00 USD | 112,430.00 USD | 185,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 14,070,000.00 USD | 14,070,000.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 6,020,000.00 USD | 6,020,000.00 USD | 340,500.00 USD | 102,200.00 USD | 216,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 16,840,000.00 USD | 16,840,000.00 USD | 1,200,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 6,640,000.00 USD | 6,640,000.00 USD | 316,620.00 USD | 103,810.00 USD | 194,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 18,960,000.00 USD | 18,960,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 6,790,000.00 USD | 6,790,000.00 USD | 75,880.00 USD | 20,540.00 USD | 57,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 21,210,000.00 USD | 21,210,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 4,300.00 USD | 5,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 6,980,000.00 USD | 6,980,000.00 USD | 117,430.00 USD | 33,940.00 USD | 39,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 22,240,000.00 USD | 22,240,000.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 7,200,000.00 USD | 7,200,000.00 USD | 76,340.00 USD | 28,150.00 USD | 114,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 22,880,000.00 USD | 22,880,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 104.40 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2180` | 7,380,000.00 USD | 7,380,000.00 USD | 87,460.00 USD | 31,290.00 USD | 62,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 23,410,000.00 USD | 23,410,000.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 24,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 7,530,000.00 USD | 7,530,000.00 USD | 83,440.00 USD | 29,430.00 USD | 33,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 24,570,000.00 USD | 24,570,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 7,680,000.00 USD | 7,680,000.00 USD | 85,310.00 USD | 23,540.00 USD | 41,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 25,830,000.00 USD | 25,830,000.00 USD | 532,120.00 USD | 219,450.00 USD | 501,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 7,770,000.00 USD | 7,770,000.00 USD | 41,250.00 USD | 17,390.00 USD | 28,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 26,870,000.00 USD | 26,870,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 25,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 7,860,000.00 USD | 7,860,000.00 USD | 51,150.00 USD | 11,520.00 USD | 32,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 27,350,000.00 USD | 27,350,000.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 7,920,000.00 USD | 7,920,000.00 USD | 46,180.00 USD | 5,700.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 27,630,000.00 USD | 27,630,000.00 USD | 141,730.00 USD | 53,210.00 USD | 85,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2240` | 8,030,000.00 USD | 8,030,000.00 USD | 59,000.00 USD | 23,560.00 USD | 30,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2240` | 28,370,000.00 USD | 28,370,000.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 28,870,000.00 USD | 28,870,000.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2260` | 8,160,000.00 USD | 8,160,000.00 USD | 71,130.00 USD | 26,650.00 USD | 27,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 29,870,000.00 USD | 29,870,000.00 USD | 443,030.00 USD | 105,500.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2270` | 8,320,000.00 USD | 8,320,000.00 USD | 61,490.00 USD | 28,850.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2270` | 30,340,000.00 USD | 30,340,000.00 USD | 230,310.00 USD | 64,760.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 28,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2280` | 8,350,000.00 USD | 8,350,000.00 USD | 12,350.00 USD | 5,480.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2280` | 30,720,000.00 USD | 30,720,000.00 USD | 105,300.00 USD | 59,020.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 37,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2290` | 8,380,000.00 USD | 8,380,000.00 USD | 8,350.00 USD | 8,950.00 USD | 15,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2290` | 30,910,000.00 USD | 30,910,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2300` | 8,420,000.00 USD | 8,420,000.00 USD | 12,650.00 USD | 5,500.00 USD | 19,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,020,000.00 USD | 31,020,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,080,000.00 USD | 31,080,000.00 USD | 11,140.00 USD | 13,670.00 USD | 29,340.00 USD | `Tier 1 CEX` |
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
| `7D` | `0.1770` | 13,890,000.00 USD | 0.00 USD | 13,890,000.00 USD | 44,290.00 USD | 11,160.00 USD | 23,130.00 USD |
| `7D` | `0.1780` | 13,810,000.00 USD | 0.00 USD | 13,810,000.00 USD | 25,340.00 USD | 402.10 USD | 39,710.00 USD |
| `7D` | `0.1790` | 13,750,000.00 USD | 0.00 USD | 13,750,000.00 USD | 4,660.00 USD | 14,110.00 USD | 0.00 USD |
| `7D` | `0.1800` | 13,730,000.00 USD | 0.00 USD | 13,730,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `7D` | `0.1810` | 13,700,000.00 USD | 0.00 USD | 13,700,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `7D` | `0.1820` | 13,520,000.00 USD | 0.00 USD | 13,520,000.00 USD | 106,790.00 USD | 51,580.00 USD | 118,390.00 USD |
| `7D` | `0.1830` | 13,240,000.00 USD | 0.00 USD | 13,240,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 147,760.00 USD | 32,900.00 USD | 35,620.00 USD |
| `7D` | `0.1840` | 13,060,000.00 USD | 0.00 USD | 13,060,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 10,510,000.00 USD | 0.00 USD | 10,510,000.00 USD | 163,720.00 USD | 57,850.00 USD | 98,700.00 USD |
| `7D` | `0.1850` | 12,570,000.00 USD | 0.00 USD | 12,570,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 10,190,000.00 USD | 0.00 USD | 10,190,000.00 USD | 35,280.00 USD | 9,470.00 USD | 14,030.00 USD |
| `7D` | `0.1860` | 11,560,000.00 USD | 0.00 USD | 11,560,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 10,130,000.00 USD | 0.00 USD | 10,130,000.00 USD | 78,720.00 USD | 13,620.00 USD | 15,170.00 USD |
| `7D` | `0.1870` | 11,180,000.00 USD | 0.00 USD | 11,180,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 10,020,000.00 USD | 0.00 USD | 10,020,000.00 USD | 219,090.00 USD | 32,770.00 USD | 34,840.00 USD |
| `7D` | `0.1880` | 10,920,000.00 USD | 0.00 USD | 10,920,000.00 USD | 172,850.00 USD | 43,830.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 9,730,000.00 USD | 0.00 USD | 9,730,000.00 USD | 101,860.00 USD | 72,520.00 USD | 183,110.00 USD |
| `7D` | `0.1890` | 10,660,000.00 USD | 0.00 USD | 10,660,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 9,380,000.00 USD | 0.00 USD | 9,380,000.00 USD | 248,740.00 USD | 105,170.00 USD | 202,770.00 USD |
| `7D` | `0.1900` | 10,220,000.00 USD | 0.00 USD | 10,220,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 8,820,000.00 USD | 0.00 USD | 8,820,000.00 USD | 230,970.00 USD | 83,930.00 USD | 90,970.00 USD |
| `7D` | `0.1910` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 250,530.00 USD | 90,380.00 USD | 16,510.00 USD |
| `1D` | `0.1920` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 486,530.00 USD | 112,840.00 USD | 185,370.00 USD |
| `7D` | `0.1920` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 279,260.00 USD | 74,890.00 USD | 77,590.00 USD |
| `1D` | `0.1930` | 7,630,000.00 USD | 0.00 USD | 7,630,000.00 USD | 283,810.00 USD | 196,480.00 USD | 462,380.00 USD |
| `7D` | `0.1930` | 8,890,000.00 USD | 0.00 USD | 8,890,000.00 USD | 747,900.00 USD | 173,570.00 USD | 325,790.00 USD |
| `1D` | `0.1940` | 6,690,000.00 USD | 0.00 USD | 6,690,000.00 USD | 627,770.00 USD | 252,610.00 USD | 512,190.00 USD |
| `7D` | `0.1940` | 7,640,000.00 USD | 0.00 USD | 7,640,000.00 USD | 721,210.00 USD | 271,400.00 USD | 825,170.00 USD |
| `1D` | `0.1950` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 514,200.00 USD | 174,610.00 USD | 209,740.00 USD |
| `7D` | `0.1950` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 627,100.00 USD | 289,850.00 USD | 389,660.00 USD |
| `1D` | `0.1960` | 4,400,000.00 USD | 0.00 USD | 4,400,000.00 USD | 472,120.00 USD | 147,670.00 USD | 324,410.00 USD |
| `7D` | `0.1960` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 3,450,000.00 USD | 0.00 USD | 3,450,000.00 USD | 324,400.00 USD | 149,540.00 USD | 270,470.00 USD |
| `7D` | `0.1970` | 3,640,000.00 USD | 0.00 USD | 3,640,000.00 USD | 220,950.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 299,150.00 USD | 92,270.00 USD | 133,140.00 USD |
| `7D` | `0.1980` | 3,020,000.00 USD | 0.00 USD | 3,020,000.00 USD | 118,660.00 USD | 47,220.00 USD | 23,890.00 USD |
| `1D` | `0.1990` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 26,640.00 USD | 0.00 USD | 10,340.00 USD |
| `7D` | `0.1990` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 0.00 USD | 0.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 151,770.00 USD | 70,030.00 USD | 146,420.00 USD |
| `7D` | `0.2000` | 1,620,000.00 USD | 0.00 USD | 1,620,000.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 278,340.00 USD | 79,030.00 USD | 167,110.00 USD |
| `7D` | `0.2010` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 209,620.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 211,750.00 USD | 53,220.00 USD | 77,190.00 USD |
| `7D` | `0.2020` | 864,540.00 USD | 0.00 USD | 864,540.00 USD | 94,610.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 910,790.00 USD | 0.00 USD | 910,790.00 USD | 462,960.00 USD | 151,590.00 USD | 296,240.00 USD |
| `7D` | `0.2030` | 354,090.00 USD | 0.00 USD | 354,090.00 USD | 173,570.00 USD | 109,540.00 USD | 70,990.00 USD |
| `1D` | `0.2040` | 287,440.00 USD | 287,440.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD |
| `1D` | `0.2040` | 574,880.00 USD | 574,880.00 USD | 0.00 USD | 0.00 USD | 203,670.00 USD | 83,780.00 USD |
| `7D` | `0.2040` | 53,690.00 USD | 53,690.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `7D` | `0.2040` | 107,380.00 USD | 107,380.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2060` | 587,390.00 USD | 587,390.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD | 10,750.00 USD |
| `7D` | `0.2060` | 115,990.00 USD | 115,990.00 USD | 0.00 USD | 0.00 USD | 1,020.00 USD | 7,590.00 USD |
| `1D` | `0.2070` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 409,780.00 USD | 102,110.00 USD | 145,830.00 USD |
| `7D` | `0.2070` | 538,120.00 USD | 538,120.00 USD | 0.00 USD | 341,590.00 USD | 80,540.00 USD | 0.00 USD |
| `1D` | `0.2080` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 492,770.00 USD | 153,120.00 USD | 16,220.00 USD |
| `7D` | `0.2080` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 2,930,000.00 USD | 2,930,000.00 USD | 0.00 USD | 542,330.00 USD | 190,640.00 USD | 285,280.00 USD |
| `7D` | `0.2090` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 2,230,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 4,300,000.00 USD | 4,300,000.00 USD | 0.00 USD | 637,140.00 USD | 246,150.00 USD | 495,340.00 USD |
| `7D` | `0.2100` | 8,020,000.00 USD | 8,020,000.00 USD | 0.00 USD | 1,690,000.00 USD | 687,470.00 USD | 1,610,000.00 USD |
| `1D` | `0.2110` | 4,760,000.00 USD | 4,760,000.00 USD | 0.00 USD | 259,670.00 USD | 55,140.00 USD | 142,090.00 USD |
| `7D` | `0.2110` | 11,090,000.00 USD | 11,090,000.00 USD | 0.00 USD | 1,040,000.00 USD | 502,740.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 5,360,000.00 USD | 5,360,000.00 USD | 0.00 USD | 303,520.00 USD | 112,430.00 USD | 185,600.00 USD |
| `7D` | `0.2120` | 14,070,000.00 USD | 14,070,000.00 USD | 0.00 USD | 1,160,000.00 USD | 463,080.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 340,500.00 USD | 102,200.00 USD | 216,660.00 USD |
| `7D` | `0.2130` | 16,840,000.00 USD | 16,840,000.00 USD | 0.00 USD | 1,200,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 316,620.00 USD | 103,810.00 USD | 194,350.00 USD |
| `7D` | `0.2140` | 18,960,000.00 USD | 18,960,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 6,790,000.00 USD | 6,790,000.00 USD | 0.00 USD | 75,880.00 USD | 20,540.00 USD | 57,150.00 USD |
| `7D` | `0.2150` | 21,210,000.00 USD | 21,210,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `1D` | `0.2160` | 6,980,000.00 USD | 6,980,000.00 USD | 0.00 USD | 117,430.00 USD | 33,940.00 USD | 39,560.00 USD |
| `7D` | `0.2160` | 22,240,000.00 USD | 22,240,000.00 USD | 0.00 USD | 467,380.00 USD | 164,960.00 USD | 397,620.00 USD |
| `1D` | `0.2170` | 7,200,000.00 USD | 7,200,000.00 USD | 0.00 USD | 76,340.00 USD | 28,150.00 USD | 114,780.00 USD |
| `7D` | `0.2170` | 22,880,000.00 USD | 22,880,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `1D` | `0.2180` | 7,380,000.00 USD | 7,380,000.00 USD | 0.00 USD | 87,460.00 USD | 31,290.00 USD | 62,940.00 USD |
| `7D` | `0.2180` | 23,410,000.00 USD | 23,410,000.00 USD | 0.00 USD | 271,760.00 USD | 104,030.00 USD | 153,380.00 USD |
| `1D` | `0.2190` | 7,530,000.00 USD | 7,530,000.00 USD | 0.00 USD | 83,440.00 USD | 29,430.00 USD | 33,670.00 USD |
| `7D` | `0.2190` | 24,570,000.00 USD | 24,570,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `1D` | `0.2200` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 85,310.00 USD | 23,540.00 USD | 41,810.00 USD |
| `7D` | `0.2200` | 25,830,000.00 USD | 25,830,000.00 USD | 0.00 USD | 532,120.00 USD | 219,450.00 USD | 501,530.00 USD |
| `1D` | `0.2210` | 7,770,000.00 USD | 7,770,000.00 USD | 0.00 USD | 41,250.00 USD | 17,390.00 USD | 28,100.00 USD |
| `7D` | `0.2210` | 26,870,000.00 USD | 26,870,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `1D` | `0.2220` | 7,860,000.00 USD | 7,860,000.00 USD | 0.00 USD | 51,150.00 USD | 11,520.00 USD | 32,990.00 USD |
| `7D` | `0.2220` | 27,350,000.00 USD | 27,350,000.00 USD | 0.00 USD | 198,110.00 USD | 90,610.00 USD | 196,280.00 USD |
| `1D` | `0.2230` | 7,920,000.00 USD | 7,920,000.00 USD | 0.00 USD | 46,180.00 USD | 5,700.00 USD | 4,760.00 USD |
| `7D` | `0.2230` | 27,630,000.00 USD | 27,630,000.00 USD | 0.00 USD | 141,730.00 USD | 53,210.00 USD | 85,630.00 USD |
| `1D` | `0.2240` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 59,000.00 USD | 23,560.00 USD | 30,850.00 USD |
| `7D` | `0.2240` | 28,370,000.00 USD | 28,370,000.00 USD | 0.00 USD | 378,190.00 USD | 82,090.00 USD | 277,380.00 USD |
| `7D` | `0.2250` | 28,870,000.00 USD | 28,870,000.00 USD | 0.00 USD | 186,370.00 USD | 100,930.00 USD | 212,920.00 USD |
| `1D` | `0.2260` | 8,160,000.00 USD | 8,160,000.00 USD | 0.00 USD | 71,130.00 USD | 26,650.00 USD | 27,850.00 USD |
| `7D` | `0.2260` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 443,030.00 USD | 105,500.00 USD | 452,530.00 USD |
| `1D` | `0.2270` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 61,490.00 USD | 28,850.00 USD | 70,850.00 USD |
| `7D` | `0.2270` | 30,340,000.00 USD | 30,340,000.00 USD | 0.00 USD | 230,310.00 USD | 64,760.00 USD | 175,420.00 USD |
| `1D` | `0.2280` | 8,350,000.00 USD | 8,350,000.00 USD | 0.00 USD | 12,350.00 USD | 5,480.00 USD | 14,030.00 USD |
| `7D` | `0.2280` | 30,720,000.00 USD | 30,720,000.00 USD | 0.00 USD | 105,300.00 USD | 59,020.00 USD | 208,320.00 USD |
| `1D` | `0.2290` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 8,350.00 USD | 8,950.00 USD | 15,170.00 USD |
| `7D` | `0.2290` | 30,910,000.00 USD | 30,910,000.00 USD | 0.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD |
| `1D` | `0.2300` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 12,650.00 USD | 5,500.00 USD | 19,370.00 USD |
| `7D` | `0.2300` | 31,020,000.00 USD | 31,020,000.00 USD | 0.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD |
| `7D` | `0.2310` | 31,080,000.00 USD | 31,080,000.00 USD | 0.00 USD | 11,140.00 USD | 13,670.00 USD | 29,340.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `454.83M` | Total OI Tokens: `2,226,955,643.2 ADA`
  * 1h OI Change: `-0.63%` | 4h OI Change: `+0.72%` | 24h OI Change: `-2.30%`
  * Exchange Breakdown: Binance=`85.44M` | Bybit=`54.21M` | OKX=`32.02M` | Hyperliquid=`30.29M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `15.32K` | Last 24h: `14.21K` | Last 3d: `57.26K` | Last 7d: `58.11K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0032%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `49.32%` | `50.68%` | `0.97` | 9,080,000.00 USD |
| `15M` | `Binance` | `45.54%` | `54.46%` | `0.84` | 2,770,000.00 USD |
| `15M` | `OKX` | `62.32%` | `37.68%` | `1.65` | 1,760,000.00 USD |
| `15M` | `Bybit` | `58.67%` | `41.33%` | `1.42` | 471,850.00 USD |
| `15M` | `KuCoin` | `53.12%` | `46.88%` | `1.13` | 26,740.00 USD |
| `15M` | `Gate` | `51.16%` | `48.84%` | `1.05` | 1,690,000.00 USD |
| `15M` | `Bitget` | `82.87%` | `17.13%` | `4.84` | 83,200.00 USD |
| `15M` | `BingX` | `22.58%` | `77.42%` | `0.29` | 475,690.00 USD |
| `15M` | `MEXC` | `56.95%` | `43.05%` | `1.32` | 796,670.00 USD |
| `15M` | `Bitunix` | `48.09%` | `51.91%` | `0.93` | 377,160.00 USD |
| `15M` | `Hyperliquid` | `73.69%` | `26.31%` | `2.80` | 46,260.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.59%` | `56.41%` | `0.77` | 54,450.00 USD |
| `15M` | `Crypto.com` | `47.95%` | `52.05%` | `0.92` | 9,740.00 USD |
| `15M` | `WhiteBIT` | `14.1%` | `85.9%` | `0.16` | 319,440.00 USD |
| `15M` | `HTX` | `86.38%` | `13.62%` | `6.34` | 10,150.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `49.49%` | `50.51%` | `0.98` | 43,770.00 USD |
| `15M` | `Aster` | `7.25%` | `92.75%` | `0.08` | 133,470.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `41.34%` | `58.66%` | `0.70` | 1,740.00 USD |
| `15M` | `Whale Positions` | `45.54%` | `54.46%` | `0.84` | 2,770,000.00 USD |
| `15M` | `Global Accounts` | `49.32%` | `50.68%` | `0.97` | 9,080,000.00 USD |
| `1H` | `ADA` | `46.02%` | `53.98%` | `0.85` | 53,450,000.00 USD |
| `1H` | `Binance` | `46.05%` | `53.95%` | `0.85` | 17,410,000.00 USD |
| `1H` | `OKX` | `48.7%` | `51.3%` | `0.95` | 10,720,000.00 USD |
| `1H` | `Bybit` | `50.69%` | `49.31%` | `1.03` | 3,790,000.00 USD |
| `1H` | `KuCoin` | `39.01%` | `60.99%` | `0.64` | 325,370.00 USD |
| `1H` | `Gate` | `49.4%` | `50.6%` | `0.98` | 7,870,000.00 USD |
| `1H` | `Bitget` | `37.88%` | `62.12%` | `0.61` | 893,580.00 USD |
| `1H` | `BingX` | `27.65%` | `72.35%` | `0.38` | 2,720,000.00 USD |
| `1H` | `MEXC` | `46.23%` | `53.77%` | `0.86` | 4,170,000.00 USD |
| `1H` | `Bitunix` | `48.2%` | `51.8%` | `0.93` | 1,390,000.00 USD |
| `1H` | `Hyperliquid` | `48.67%` | `51.33%` | `0.95` | 1,750,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.09%` | `51.91%` | `0.93` | 248,060.00 USD |
| `1H` | `Crypto.com` | `49.34%` | `50.66%` | `0.97` | 70,170.00 USD |
| `1H` | `WhiteBIT` | `31.32%` | `68.68%` | `0.46` | 1,230,000.00 USD |
| `1H` | `HTX` | `39.25%` | `60.75%` | `0.65` | 148,330.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `34.22%` | `65.78%` | `0.52` | 248,060.00 USD |
| `1H` | `Aster` | `45.72%` | `54.28%` | `0.84` | 388,030.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `23.4%` | `76.6%` | `0.31` | 59,750.00 USD |
| `1H` | `Whale Positions` | `46.05%` | `53.95%` | `0.85` | 17,410,000.00 USD |
| `1H` | `Global Accounts` | `46.02%` | `53.98%` | `0.85` | 53,450,000.00 USD |
| `4H` | `ADA` | `50.04%` | `49.96%` | `1.00` | 337,480,000.00 USD |
| `4H` | `Binance` | `52.7%` | `47.3%` | `1.11` | 119,140,000.00 USD |
| `4H` | `OKX` | `47.96%` | `52.04%` | `0.92` | 73,160,000.00 USD |
| `4H` | `Bybit` | `51.73%` | `48.27%` | `1.07` | 23,380,000.00 USD |
| `4H` | `KuCoin` | `44.56%` | `55.44%` | `0.80` | 2,380,000.00 USD |
| `4H` | `Gate` | `45.2%` | `54.8%` | `0.82` | 45,300,000.00 USD |
| `4H` | `Bitget` | `45.72%` | `54.28%` | `0.84` | 8,720,000.00 USD |
| `4H` | `BingX` | `39.6%` | `60.4%` | `0.66` | 9,320,000.00 USD |
| `4H` | `MEXC` | `51.81%` | `48.19%` | `1.08` | 27,790,000.00 USD |
| `4H` | `Bitunix` | `57.51%` | `42.49%` | `1.35` | 10,550,000.00 USD |
| `4H` | `Hyperliquid` | `62.18%` | `37.82%` | `1.64` | 3,190,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.94%` | `48.06%` | `1.08` | 1,390,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 337,250.00 USD |
| `4H` | `WhiteBIT` | `3.25%` | `96.75%` | `0.03` | 6,340,000.00 USD |
| `4H` | `HTX` | `46.76%` | `53.24%` | `0.88` | 1,570,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `51.51%` | `48.49%` | `1.06` | 1,470,000.00 USD |
| `4H` | `Aster` | `62.79%` | `37.21%` | `1.69` | 3,330,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `40.6%` | `59.4%` | `0.68` | 113,220.00 USD |
| `4H` | `Whale Positions` | `52.7%` | `47.3%` | `1.11` | 119,140,000.00 USD |
| `4H` | `Global Accounts` | `50.04%` | `49.96%` | `1.00` | 337,480,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.2049` | `0.2048` | `0.2049` | `0.2057` | `0.2041` | 2,372,003.28 USD | 1,123,364.70 USD | 1,248,638.58 USD | -125,273.88 USD | `-5.28%` | `1B / 1S` |
| `0:00 UTC` | `0.2051` | `0.2051` | `0.2051` | `0.2056` | `0.2042` | 2,366,919.63 USD | 1,383,725.71 USD | 983,193.92 USD | 400,531.79 USD | `+16.92%` | `1B / 0S` |
| `5:00 UTC` | `0.2054` | `0.2059` | `0.2054` | `0.2066` | `0.2049` | 3,269,747.09 USD | 1,525,563.65 USD | 1,744,183.44 USD | -218,619.79 USD | `-6.69%` | `1B / 1S` |
| `0:00 UTC` | `0.2064` | `0.2072` | `0.2064` | `0.2087` | `0.2056` | 5,724,356.79 USD | 3,224,697.96 USD | 2,499,658.83 USD | 725,039.12 USD | `+12.67%` | `4B / 0S` |
| `5:00 UTC` | `0.2061` | `0.2060` | `0.2061` | `0.2072` | `0.2054` | 2,545,595.94 USD | 1,190,541.20 USD | 1,355,054.75 USD | -164,513.55 USD | `-6.46%` | `0B / 1S` |
| `0:00 UTC` | `0.2052` | `0.2054` | `0.2052` | `0.2061` | `0.2047` | 2,681,797.52 USD | 1,504,963.17 USD | 1,176,834.35 USD | 328,128.82 USD | `+12.24%` | `2B / 1S` |
| `5:00 UTC` | `0.2054` | `0.2054` | `0.2054` | `0.2059` | `0.2051` | 1,103,361.90 USD | 582,275.03 USD | 521,086.87 USD | 61,188.16 USD | `+5.55%` | `1B / 1S` |
| `0:00 UTC` | `0.2047` | `0.2049` | `0.2047` | `0.2056` | `0.2042` | 2,508,493.59 USD | 1,331,643.13 USD | 1,176,850.47 USD | 154,792.66 USD | `+6.17%` | `1B / 1S` |
| `5:00 UTC` | `0.2044` | `0.2044` | `0.2044` | `0.2047` | `0.2041` | 1,406,635.22 USD | 616,800.46 USD | 789,834.77 USD | -173,034.31 USD | `-12.30%` | `0B / 0S` |
| `0:00 UTC` | `0.2049` | `0.2046` | `0.2049` | `0.2051` | `0.2042` | 431,021.24 USD | 261,908.24 USD | 169,113.00 USD | 92,795.24 USD | `+21.53%` | `4B / 0S` |

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
| `5m` | 9,200.00 USD | 69,820.00 USD | **`ACCUMULATION`** |
| `15m` | -6,450.00 USD | -82,260.00 USD | **`DISTRIBUTION`** |
| `30m` | -284,720.00 USD | -575,520.00 USD | **`DISTRIBUTION`** |
| `1h` | -462,760.00 USD | -208,780.00 USD | **`DISTRIBUTION`** |
| `2h` | -309,790.00 USD | -683,710.00 USD | **`DISTRIBUTION`** |
| `4h` | -208,770.00 USD | 2,470,000.00 USD | **`ACCUMULATION`** |
| `6h` | -349,590.00 USD | 2,960,000.00 USD | **`ACCUMULATION`** |
| `8h` | -67,770.00 USD | 4,290,000.00 USD | **`ACCUMULATION`** |
| `12h` | -229,910.00 USD | 4,690,000.00 USD | **`ACCUMULATION`** |
| `24h` | -3,030,000.00 USD | -1,220,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -13,290,000.00 USD | -24,220,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -70,510,000.00 USD | -186,050,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+9.20K` | 15m=`-6.45K` | 1h=`-462.76K` | 24h=`-3.03M`
* Futures Capital Netflows: 5m=`+69.82K` | 15m=`-82.26K` | 1h=`-208.78K` | 24h=`-1.22M`
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
  * `2026-10-29 23:01:06 IST`: [snb.ch] - (Sentiment: `Neutral`)
  * `2026-10-29 22:55:06 IST`: [@Tenz_News] - (Sentiment: `Neutral`)
  * `2026-10-29 22:45:06 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:06 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 23:01:06 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 23:00:06 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 20:02:06 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:02:06 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1977` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.01` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.21`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2064` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.41` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.80`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2058`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
