# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-29 22:33:52 IST` (`2026-10-29 17:03:52 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.2038` | **Live Ask Quote**: `0.2060` | **Mid Price**: `0.2049`
- **Spread Points**: `22.00` | **Spread BPS**: `107.37 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1987` | VWAP Z-Score: `+1.86` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0013` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `71.77` (State: `OVERBOUGHT`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.2060` | Lower -3.00σ Band: `0.1913`
  * Upper +2.51σ Band: `0.2048` | Lower -2.51σ Band: `0.1925`
  * Upper +2.01σ Band: `0.2036` | Lower -2.01σ Band: `0.1938`
  * Upper +2.00σ Band: `0.2035` | Lower -2.00σ Band: `0.1938`
  * Upper +1.28σ Band: `0.2018` | Lower -1.28σ Band: `0.1955`
  * Upper +1.00σ Band: `0.2011` | Lower -1.00σ Band: `0.1962`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.2008` | EMA-20=`0.1999` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1995` (Slope: `+0.0000`) | EMA-100=`0.2004`
  * Institutional Anchors: EMA-144=`0.2010` | EMA-200=`0.2015` (Slope: `-0.0769`) | EMA-233=`0.2018`
- **Range Boundaries**: 24H High=`0.2086` | 24H Low=`0.1944` | Weekly High=`0.2086` | Weekly Low=`0.1944`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.2064` (Distance: `-0.73%`)
  * Point of Control (POC) = `0.2047` (Distance: `+0.11%`)
  * Value Area Low (VAL) = `0.1976` (Distance: `+3.67%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2067` | POC=`0.2054` | VAL=`0.2018`
  * Prior Day Extremes: PDH=`0.2086` | PDL=`0.1994` | PDC=`0.2054`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2058` | Weekly POC=`0.2030` | Weekly VAL=`0.2011`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.2065` | Low=`0.1944`
  * London Session (08:00-16:00 UTC): High=`0.2009` | Low=`0.1957`
  * New York Session (13:00-21:00 UTC): High=`0.2074` | Low=`0.1979`
  * Initial Balance (First Hour): IB High=`0.2000` | IB Low=`0.1977`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.2041` - `0.2057`
  * Optimal Trade Entry (OTE 0.705): `0.2053`
  * Structural Invalidation Anchor (0.786): `0.2065`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.2054` | `0.2055` | `0.2051` | `0.2052` | `1,678,744` | 344,700.07 USD | -111,020.60 USD | `-32.21%` | 2,641,645.03 USD | `-0.74` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.2051` | `0.2055` | `0.2051` | `0.2054` | `1,031,916` | 211,820.89 USD | 12,740.39 USD | `+6.01%` | 2,654,385.42 USD | `-0.20` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.2055` | `0.2055` | `0.2050` | `0.2051` | `1,651,191` | 338,932.46 USD | -9,033.55 USD | `-2.67%` | 2,645,351.87 USD | `-0.28` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.2057` | `0.2061` | `0.2047` | `0.2055` | `13,059,178` | 2,681,797.52 USD | 328,128.82 USD | `+12.24%` | 2,483,080.35 USD | `+0.65` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2055` | `0.2059` | `0.2051` | `0.2054` | `5,372,201` | 1,103,361.90 USD | 61,188.16 USD | `+5.55%` | 2,544,268.51 USD | `-0.24` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.2055` | `0.2055` | `0.2050` | `0.2050` | `1,650,694` | 338,830.53 USD | -9,119.49 USD | `-2.69%` | 2,535,149.02 USD | `-0.58` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2037` | `0.2065` | `0.2035` | `0.2063` | `50,555,533` | 10,368,970.33 USD | 269,833.71 USD | `+2.60%` | 1,061,283.01 USD | `+0.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.2064` | `0.2087` | `0.2047` | `0.2054` | `58,420,928` | 12,055,112.15 USD | 949,842.55 USD | `+7.88%` | 2,011,125.56 USD | `+0.81` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.2055` | `0.2055` | `0.2050` | `0.2051` | `1,651,191` | 338,932.46 USD | -9,033.55 USD | `-2.67%` | 2,002,092.01 USD | `+0.05` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2047` | `0.2051` | `60,072,119` | 12,394,044.61 USD | 940,809.00 USD | `+7.59%` | 981,343.57 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2058` | `0.2065` | `0.1954` | `0.1973` | `282,726,861` | 56,231,891.33 USD | -5,955,308.28 USD | `-10.59%` | -3,049,296.45 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1973` | `0.2013` | `0.1966` | `0.1973` | `110,015,025` | 21,864,887.33 USD | 540,975.25 USD | `+2.47%` | -2,508,321.21 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.1974` | `0.2022` | `0.1974` | `0.2010` | `107,888,826` | 21,566,372.97 USD | 780,949.06 USD | `+3.62%` | -1,727,372.15 USD | `+0.37` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 40,534.57 USD | `+0.57` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2047` | `0.2051` | `60,072,119` | 12,394,044.61 USD | 940,809.00 USD | `+7.59%` | 981,343.57 USD | `+0.27` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`0.2049`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:31:36 IST` |

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
| `1D` | `Long Liquidation` | `0.1810` | 8,510,000.00 USD | 8,510,000.00 USD | 118,290.00 USD | 70,090.00 USD | 113,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 11,150,000.00 USD | 11,150,000.00 USD | 112,560.00 USD | 27,510.00 USD | 31,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 7,670.00 USD | 457,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 8,210,000.00 USD | 8,210,000.00 USD | 53,260.00 USD | 21,110.00 USD | 75,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 10,980,000.00 USD | 10,980,000.00 USD | 95,280.00 USD | 47,480.00 USD | 117,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 18,250.00 USD | 450,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 8,060,000.00 USD | 8,060,000.00 USD | 48,990.00 USD | 11,640.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 10,720,000.00 USD | 10,720,000.00 USD | 84,560.00 USD | 36,880.00 USD | 59,960.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1835` | 367.00 USD | 431,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1840` | 7,980,000.00 USD | 7,980,000.00 USD | 80,720.00 USD | 17,960.00 USD | 17,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 10,540,000.00 USD | 10,540,000.00 USD | 226,530.00 USD | 58,050.00 USD | 174,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1845` | 956.45 USD | 431,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1850` | 7,870,000.00 USD | 7,870,000.00 USD | 103,680.00 USD | 35,330.00 USD | 67,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 10,080,000.00 USD | 10,080,000.00 USD | 404,170.00 USD | 111,470.00 USD | 387,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1855` | 6,190.00 USD | 430,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1860` | 7,660,000.00 USD | 7,660,000.00 USD | 34,240.00 USD | 8,700.00 USD | 12,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 9,170,000.00 USD | 9,170,000.00 USD | 114,090.00 USD | 56,980.00 USD | 194,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1865` | 2,900.00 USD | 424,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1870` | 7,610,000.00 USD | 7,610,000.00 USD | 77,280.00 USD | 5,970.00 USD | 664.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 8,810,000.00 USD | 8,810,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1875` | 4,120.00 USD | 421,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1880` | 7,520,000.00 USD | 7,520,000.00 USD | 231,610.00 USD | 34,960.00 USD | 33,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 8,550,000.00 USD | 8,550,000.00 USD | 158,590.00 USD | 41,220.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1885` | 9,670.00 USD | 417,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1890` | 7,220,000.00 USD | 7,220,000.00 USD | 99,480.00 USD | 72,180.00 USD | 183,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 8,310,000.00 USD | 8,310,000.00 USD | 246,750.00 USD | 52,560.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1895` | 10,260.00 USD | 407,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1900` | 6,870,000.00 USD | 6,870,000.00 USD | 239,840.00 USD | 104,970.00 USD | 203,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 7,870,000.00 USD | 7,870,000.00 USD | 247,920.00 USD | 72,080.00 USD | 235,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1905` | 13,110.00 USD | 397,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1910` | 6,320,000.00 USD | 6,320,000.00 USD | 226,440.00 USD | 80,880.00 USD | 91,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 7,320,000.00 USD | 7,320,000.00 USD | 258,450.00 USD | 86,060.00 USD | 16,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1915` | 27,820.00 USD | 384,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1920` | 5,920,000.00 USD | 5,920,000.00 USD | 489,900.00 USD | 116,840.00 USD | 182,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 6,960,000.00 USD | 6,960,000.00 USD | 257,730.00 USD | 74,890.00 USD | 77,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1925` | 50,480.00 USD | 356,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1930` | 5,130,000.00 USD | 5,130,000.00 USD | 328,820.00 USD | 223,980.00 USD | 497,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 6,550,000.00 USD | 6,550,000.00 USD | 722,350.00 USD | 159,940.00 USD | 323,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1935` | 290,550.00 USD | 306,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1940` | 4,080,000.00 USD | 4,080,000.00 USD | 644,680.00 USD | 280,880.00 USD | 639,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 5,340,000.00 USD | 5,340,000.00 USD | 678,880.00 USD | 259,610.00 USD | 823,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1945` | 6,000.00 USD | 15,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1950` | 2,510,000.00 USD | 2,510,000.00 USD | 519,790.00 USD | 188,170.00 USD | 232,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 3,580,000.00 USD | 3,580,000.00 USD | 619,180.00 USD | 288,290.00 USD | 388,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1955` | 8,500.00 USD | 9,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1960` | 1,570,000.00 USD | 1,570,000.00 USD | 390,140.00 USD | 123,250.00 USD | 274,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 2,280,000.00 USD | 2,280,000.00 USD | 99,630.00 USD | 9,990.00 USD | 676,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1965` | 982.50 USD | 982.50 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1970` | 785,850.00 USD | 785,850.00 USD | 182,100.00 USD | 109,630.00 USD | 191,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 1,500,000.00 USD | 1,500,000.00 USD | 80,840.00 USD | 56,210.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1980` | 302,770.00 USD | 302,770.00 USD | 126,240.00 USD | 57,150.00 USD | 80,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 20,720.00 USD | 1,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 1,170,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2000` | 38,910.00 USD | 38,910.00 USD | 0.00 USD | 0.00 USD | 13,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 31,080.00 USD | 31,080.00 USD | 0.00 USD | 25,400.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.2010` | 25,270.00 USD | 25,270.00 USD | 0.00 USD | 0.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 602,690.00 USD | 602,690.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2010` | 1,210,000.00 USD | 1,210,000.00 USD | 588,030.00 USD | 0.00 USD | 14,660.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 19,440.00 USD | 19,440.00 USD | 0.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2020` | 38,870.00 USD | 38,870.00 USD | 0.00 USD | 0.00 USD | 19,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 1,720,000.00 USD | 1,720,000.00 USD | 154,520.00 USD | 0.00 USD | 360,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2030` | 945,220.00 USD | 945,220.00 USD | 462,960.00 USD | 151,590.00 USD | 291,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 2,000,000.00 USD | 2,000,000.00 USD | 173,570.00 USD | 109,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 1,970,000.00 USD | 1,970,000.00 USD | 541,580.00 USD | 159,880.00 USD | 324,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 2,400,000.00 USD | 2,400,000.00 USD | 125,120.00 USD | 53,690.00 USD | 215,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 2,930,000.00 USD | 2,930,000.00 USD | 303,360.00 USD | 179,100.00 USD | 474,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2050` | 3,000,000.00 USD | 3,000,000.00 USD | 276,760.00 USD | 82,430.00 USD | 242,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 3,870,000.00 USD | 3,870,000.00 USD | 450,430.00 USD | 164,720.00 USD | 325,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 3,380,000.00 USD | 3,380,000.00 USD | 144,470.00 USD | 31,310.00 USD | 206,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 4,670,000.00 USD | 4,670,000.00 USD | 509,340.00 USD | 106,370.00 USD | 189,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 3,910,000.00 USD | 3,910,000.00 USD | 385,560.00 USD | 80,540.00 USD | 58,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2080` | 5,300,000.00 USD | 5,300,000.00 USD | 341,010.00 USD | 104,430.00 USD | 179,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 4,570,000.00 USD | 4,570,000.00 USD | 552,200.00 USD | 44,630.00 USD | 65,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 5,810,000.00 USD | 5,810,000.00 USD | 263,990.00 USD | 110,830.00 USD | 134,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 6,820,000.00 USD | 6,820,000.00 USD | 2,010,000.00 USD | 87,520.00 USD | 155,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 6,990,000.00 USD | 6,990,000.00 USD | 393,310.00 USD | 224,090.00 USD | 563,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 10,610,000.00 USD | 10,610,000.00 USD | 1,560,000.00 USD | 660,820.00 USD | 1,570,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 7,510,000.00 USD | 7,510,000.00 USD | 291,750.00 USD | 72,130.00 USD | 158,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 13,600,000.00 USD | 13,600,000.00 USD | 1,030,000.00 USD | 499,260.00 USD | 1,460,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 7,860,000.00 USD | 7,860,000.00 USD | 235,580.00 USD | 47,910.00 USD | 64,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 16,490,000.00 USD | 16,490,000.00 USD | 1,120,000.00 USD | 463,080.00 USD | 1,320,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 8,270,000.00 USD | 8,270,000.00 USD | 198,160.00 USD | 63,370.00 USD | 144,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 18,970,000.00 USD | 18,970,000.00 USD | 1,090,000.00 USD | 289,130.00 USD | 1,100,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2135` | 715.44 USD | 715.44 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2140` | 8,710,000.00 USD | 8,710,000.00 USD | 205,450.00 USD | 76,000.00 USD | 165,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 21,000,000.00 USD | 21,000,000.00 USD | 820,780.00 USD | 379,940.00 USD | 830,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2150` | 8,840,000.00 USD | 8,840,000.00 USD | 58,150.00 USD | 16,520.00 USD | 54,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 23,230,000.00 USD | 23,230,000.00 USD | 916,150.00 USD | 316,800.00 USD | 1,000,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2155` | 4,300.00 USD | 5,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2160` | 8,980,000.00 USD | 8,980,000.00 USD | 117,290.00 USD | 15,090.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 24,240,000.00 USD | 24,240,000.00 USD | 447,110.00 USD | 164,960.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2170` | 9,190,000.00 USD | 9,190,000.00 USD | 70,840.00 USD | 28,410.00 USD | 115,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,870,000.00 USD | 24,870,000.00 USD | 296,410.00 USD | 94,900.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 104.40 USD | 5,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2180` | 9,360,000.00 USD | 9,360,000.00 USD | 75,700.00 USD | 29,740.00 USD | 63,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2180` | 25,390,000.00 USD | 25,390,000.00 USD | 266,770.00 USD | 102,870.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 18,910.00 USD | 24,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2190` | 9,490,000.00 USD | 9,490,000.00 USD | 70,150.00 USD | 26,400.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2190` | 26,600,000.00 USD | 26,600,000.00 USD | 630,760.00 USD | 188,070.00 USD | 391,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2200` | 9,640,000.00 USD | 9,640,000.00 USD | 80,740.00 USD | 24,090.00 USD | 41,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 27,920,000.00 USD | 27,920,000.00 USD | 558,280.00 USD | 232,970.00 USD | 526,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2210` | 9,750,000.00 USD | 9,750,000.00 USD | 55,260.00 USD | 23,800.00 USD | 37,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 28,950,000.00 USD | 28,950,000.00 USD | 532,080.00 USD | 84,700.00 USD | 416,740.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 1,640.00 USD | 25,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2220` | 9,910,000.00 USD | 9,910,000.00 USD | 57,240.00 USD | 21,110.00 USD | 75,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2220` | 29,420,000.00 USD | 29,420,000.00 USD | 188,710.00 USD | 86,520.00 USD | 195,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2230` | 9,980,000.00 USD | 9,980,000.00 USD | 46,100.00 USD | 11,060.00 USD | 15,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 29,710,000.00 USD | 29,710,000.00 USD | 149,810.00 USD | 47,320.00 USD | 85,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 25,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2275` | 2,160.00 USD | 28,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 37,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
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
| `Sell Stop` | `0.0595` | 803,260,000.00 USD | 0.00 USD | 415.13 USD | `-71.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 803,260,000.00 USD | 0.00 USD | 1,100.00 USD | `-46.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 803,260,000.00 USD | 0.00 USD | 541.33 USD | `-45.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 803,260,000.00 USD | 0.00 USD | 602,500.00 USD | `-41.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 802,650,000.00 USD | 0.00 USD | 1,320.00 USD | `-37.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 802,650,000.00 USD | 0.00 USD | 13,390.00 USD | `-36.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 802,640,000.00 USD | 0.00 USD | 728.88 USD | `-35.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 802,640,000.00 USD | 0.00 USD | 4,350.00 USD | `-34.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 802,630,000.00 USD | 0.00 USD | 542.99 USD | `-33.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 802,630,000.00 USD | 0.00 USD | 1,820.00 USD | `-32.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 802,630,000.00 USD | 0.00 USD | 1,050.00 USD | `-31.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 802,630,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 802,630,000.00 USD | 0.00 USD | 1,600.00 USD | `-30.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 802,630,000.00 USD | 0.00 USD | 4,580.00 USD | `-29.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 802,620,000.00 USD | 0.00 USD | 303.26 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 802,620,000.00 USD | 0.00 USD | 1,290.00 USD | `-26.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 802,620,000.00 USD | 0.00 USD | 279.53 USD | `-25.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 802,620,000.00 USD | 0.00 USD | 324.30 USD | `-24.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 802,620,000.00 USD | 0.00 USD | 1,010.00 USD | `-24.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 802,620,000.00 USD | 0.00 USD | 552.21 USD | `-22.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 802,620,000.00 USD | 0.00 USD | 166.84 USD | `-22.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 802,620,000.00 USD | 0.00 USD | 2,990.00 USD | `-21.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 802,610,000.00 USD | 0.00 USD | 562.67 USD | `-21.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 802,610,000.00 USD | 0.00 USD | 24,760.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 802,590,000.00 USD | 0.00 USD | 6,540.00 USD | `-20.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 802,580,000.00 USD | 0.00 USD | 2,870.00 USD | `-19.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 802,580,000.00 USD | 0.00 USD | 452.97 USD | `-19.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 802,580,000.00 USD | 0.00 USD | 6,660.00 USD | `-18.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 802,570,000.00 USD | 0.00 USD | 317.92 USD | `-18.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1685` | 802,570,000.00 USD | 0.00 USD | 6,740.00 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 802,570,000.00 USD | 0.00 USD | 4,270.00 USD | `-17.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 802,560,000.00 USD | 0.00 USD | 7,630.00 USD | `-16.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 802,550,000.00 USD | 0.00 USD | 6,860.00 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 802,550,000.00 USD | 0.00 USD | 6,900.00 USD | `-15.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 802,540,000.00 USD | 0.00 USD | 103.58 USD | `-15.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 802,540,000.00 USD | 0.00 USD | 8,220.00 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 802,530,000.00 USD | 0.00 USD | 1,760.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 802,530,000.00 USD | 0.00 USD | 623.57 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 802,530,000.00 USD | 0.00 USD | 4,440.00 USD | `-13.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 802,520,000.00 USD | 0.00 USD | 12,390.00 USD | `-13.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 802,510,000.00 USD | 0.00 USD | 5,760.00 USD | `-12.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 802,510,000.00 USD | 0.00 USD | 26,930.00 USD | `-12.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 802,480,000.00 USD | 0.00 USD | 2,400.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 802,480,000.00 USD | 0.00 USD | 2,190.00 USD | `-11.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1835` | 802,480,000.00 USD | 0.00 USD | 3,160.00 USD | `-10.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1845` | 802,470,000.00 USD | 0.00 USD | 18,650.00 USD | `-10.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 802,450,000.00 USD | 0.00 USD | 282.33 USD | `-9.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 802,450,000.00 USD | 0.00 USD | 218.76 USD | `-9.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 802,450,000.00 USD | 0.00 USD | 109.69 USD | `-8.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 802,450,000.00 USD | 0.00 USD | 7,190.00 USD | `-8.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 802,450,000.00 USD | 0.00 USD | 837.40 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 802,440,000.00 USD | 0.00 USD | 16,100.00 USD | `-7.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1915` | 802,430,000.00 USD | 0.00 USD | 1,050.00 USD | `-6.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1925` | 802,430,000.00 USD | 0.00 USD | 211.37 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1935` | 802,430,000.00 USD | 0.00 USD | 2,100.00 USD | `-5.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1945` | 802,430,000.00 USD | 0.00 USD | 2,620.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1955` | 802,420,000.00 USD | 0.00 USD | 2,050.00 USD | `-4.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1965` | 802,420,000.00 USD | 0.00 USD | 2,380.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1975` | 802,420,000.00 USD | 0.00 USD | 79,000,000.00 USD | `-3.80%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1985` | 723,410,000.00 USD | 0.00 USD | 79,400,000.00 USD | `-3.32%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1995` | 644,010,000.00 USD | 0.00 USD | 319,210,000.00 USD | `-2.83%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2005` | 324,810,000.00 USD | 0.00 USD | 80,200,000.00 USD | `-2.34%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2015` | 244,600,000.00 USD | 0.00 USD | 40,300,000.00 USD | `-1.86%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2025` | 204,300,000.00 USD | 0.00 USD | 763.83 USD | `-1.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.2035` | 204,300,000.00 USD | 0.00 USD | 40,700,000.00 USD | `-0.88%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.2045` | 163,600,000.00 USD | 0.00 USD | 163,600,000.00 USD | `-0.39%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2055` | 82,200,000.00 USD | 82,200,000.00 USD | 0.00 USD | `+0.09%` | `HIGH (Cascade Hazard)` |
| `Buy Stop` | `0.2065` | 82,200,000.00 USD | 1,260.00 USD | 0.00 USD | `+0.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 82,210,000.00 USD | 8,020.00 USD | 0.00 USD | `+1.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 82,210,000.00 USD | 3,540.00 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 82,220,000.00 USD | 8,720.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 82,260,000.00 USD | 34,050.00 USD | 0.00 USD | `+2.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 82,260,000.00 USD | 2,690.00 USD | 0.00 USD | `+3.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 82,260,000.00 USD | 1,120.00 USD | 0.00 USD | `+3.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 82,270,000.00 USD | 10,740.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 82,270,000.00 USD | 2,460.00 USD | 0.00 USD | `+4.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 82,280,000.00 USD | 2,600.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 82,280,000.00 USD | 109.77 USD | 0.00 USD | `+5.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 82,280,000.00 USD | 109.91 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 82,280,000.00 USD | 584.97 USD | 0.00 USD | `+6.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 82,390,000.00 USD | 117,180.00 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 82,390,000.00 USD | 1,650.00 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 82,400,000.00 USD | 1,690.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 82,400,000.00 USD | 501.31 USD | 0.00 USD | `+8.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 82,400,000.00 USD | 6,860.00 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 82,400,000.00 USD | 341.18 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 82,400,000.00 USD | 109.40 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 82,410,000.00 USD | 10,110.00 USD | 0.00 USD | `+10.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 82,420,000.00 USD | 9,140.00 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2295` | 82,430,000.00 USD | 9,180.00 USD | 0.00 USD | `+11.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 82,430,000.00 USD | 662.92 USD | 0.00 USD | `+12.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 82,440,000.00 USD | 9,600.00 USD | 0.00 USD | `+12.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 82,440,000.00 USD | 171.12 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 82,450,000.00 USD | 9,340.00 USD | 0.00 USD | `+13.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 82,450,000.00 USD | 1,010.00 USD | 0.00 USD | `+14.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 82,460,000.00 USD | 9,420.00 USD | 0.00 USD | `+14.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 82,460,000.00 USD | 557.19 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 82,460,000.00 USD | 650.04 USD | 0.00 USD | `+15.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 82,460,000.00 USD | 192.71 USD | 0.00 USD | `+16.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 82,480,000.00 USD | 12,620.00 USD | 0.00 USD | `+16.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 82,480,000.00 USD | 209.72 USD | 0.00 USD | `+17.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 82,480,000.00 USD | 115.92 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 82,490,000.00 USD | 10,930.00 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 82,490,000.00 USD | 288.22 USD | 0.00 USD | `+19.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 82,490,000.00 USD | 491.03 USD | 0.00 USD | `+20.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 82,490,000.00 USD | 1,320.00 USD | 0.00 USD | `+20.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 82,500,000.00 USD | 10,630.00 USD | 0.00 USD | `+21.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 82,500,000.00 USD | 499.00 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 82,500,000.00 USD | 1,100.00 USD | 0.00 USD | `+22.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 82,500,000.00 USD | 168.76 USD | 0.00 USD | `+22.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 82,500,000.00 USD | 603.73 USD | 0.00 USD | `+22.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 82,510,000.00 USD | 2,170.00 USD | 0.00 USD | `+23.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2565` | 82,510,000.00 USD | 1,570.00 USD | 0.00 USD | `+24.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 82,510,000.00 USD | 1,470.00 USD | 0.00 USD | `+25.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 82,510,000.00 USD | 271.44 USD | 0.00 USD | `+26.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 82,930,000.00 USD | 421,430.00 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2655` | 82,930,000.00 USD | 945.98 USD | 0.00 USD | `+29.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 82,940,000.00 USD | 8,890.00 USD | 0.00 USD | `+30.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 82,950,000.00 USD | 14,860.00 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 82,960,000.00 USD | 4,620.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 82,960,000.00 USD | 1,310.00 USD | 0.00 USD | `+32.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 82,970,000.00 USD | 13,870.00 USD | 0.00 USD | `+33.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 82,980,000.00 USD | 4,670.00 USD | 0.00 USD | `+33.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 82,980,000.00 USD | 944.99 USD | 0.00 USD | `+36.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2825` | 82,980,000.00 USD | 161.87 USD | 0.00 USD | `+37.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 82,980,000.00 USD | 542.34 USD | 0.00 USD | `+38.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 82,980,000.00 USD | 1,370.00 USD | 0.00 USD | `+38.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 82,980,000.00 USD | 1,080.00 USD | 0.00 USD | `+40.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 83,000,000.00 USD | 15,160.00 USD | 0.00 USD | `+41.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 83,000,000.00 USD | 796.09 USD | 0.00 USD | `+41.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 83,000,000.00 USD | 1,440.00 USD | 0.00 USD | `+44.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 83,000,000.00 USD | 355.21 USD | 0.00 USD | `+45.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 83,010,000.00 USD | 6,950.00 USD | 0.00 USD | `+46.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 83,030,000.00 USD | 18,980.00 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 83,030,000.00 USD | 4,150.00 USD | 0.00 USD | `+50.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 83,030,000.00 USD | 3,250.00 USD | 0.00 USD | `+53.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3205` | 83,040,000.00 USD | 5,090.00 USD | 0.00 USD | `+56.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 83,040,000.00 USD | 1,450.00 USD | 0.00 USD | `+58.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 83,040,000.00 USD | 181.30 USD | 0.00 USD | `+58.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 83,050,000.00 USD | 12,290.00 USD | 0.00 USD | `+61.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 83,050,000.00 USD | 111.06 USD | 0.00 USD | `+62.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 83,050,000.00 USD | 220.61 USD | 0.00 USD | `+66.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 83,060,000.00 USD | 3,850.00 USD | 0.00 USD | `+70.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 83,060,000.00 USD | 188.75 USD | 0.00 USD | `+83.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 83,060,000.00 USD | 121.76 USD | 0.00 USD | `+85.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3895` | 83,060,000.00 USD | 141.78 USD | 0.00 USD | `+89.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3935` | 83,060,000.00 USD | 393.50 USD | 0.00 USD | `+91.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3945` | 83,060,000.00 USD | 1,260.00 USD | 0.00 USD | `+92.15%` | `TACTICAL (Retail Cluster)` |

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
  * Execution Entry: `0.1976` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `0.1928` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.2097`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.2064` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `0.2112` (Risk Distance: `0.0048` pts)
  * +2.5R Take Profit: `0.1943`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.2065`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
