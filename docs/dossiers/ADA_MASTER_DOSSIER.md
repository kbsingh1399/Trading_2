# 🏛️ SOVEREIGN CANDIDATE DOSSIER: ADA
**Canonical Key**: `ADA` | **Broker Instrument**: `ADAUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:01:31 IST` (`2026-10-30 04:31:31 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.1914` | **Live Ask Quote**: `0.1935` | **Mid Price**: `0.1925`
- **Spread Points**: `21.00` | **Spread BPS**: `109.12 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `0.1925` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.1938` | Lower -3.00σ Band: `0.1911`
  * Upper +2.51σ Band: `0.1935` | Lower -2.51σ Band: `0.1914`
  * Upper +2.01σ Band: `0.1933` | Lower -2.01σ Band: `0.1916`
  * Upper +2.00σ Band: `0.1932` | Lower -2.00σ Band: `0.1917`
  * Upper +1.28σ Band: `0.1930` | Lower -1.28σ Band: `0.1919`
  * Upper +1.00σ Band: `0.1928` | Lower -1.00σ Band: `0.1921`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.1925` | EMA-20=`0.1925` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.1925` (Slope: `+0.0000`) | EMA-100=`0.1925`
  * Institutional Anchors: EMA-144=`0.1925` | EMA-200=`0.1925` (Slope: `+0.0000`) | EMA-233=`0.1925`
- **Range Boundaries**: 24H High=`0.1944` | 24H Low=`0.1905` | Weekly High=`0.1963` | Weekly Low=`0.1886`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.1925` (Distance: `-0.05%`)
  * Point of Control (POC) = `0.1907` (Distance: `+0.92%`)
  * Value Area Low (VAL) = `0.1859` (Distance: `+3.50%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.2037` | POC=`0.2010` | VAL=`0.1953`
  * Prior Day Extremes: PDH=`0.2074` | PDL=`0.1862` | PDC=`0.1892`
  * Monday Range Blueprint: High=`0.2068` | Mid=`0.2030` | Low=`0.1991`
  * Developing Weekly Value Area: Weekly VAH=`0.2065` | Weekly POC=`0.2031` | Weekly VAL=`0.1994`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.1940` | Low=`0.1808`
  * London Session (08:00-16:00 UTC): High=`0.1932` | Low=`0.1917`
  * New York Session (13:00-21:00 UTC): High=`0.1936` | Low=`0.1913`
  * Initial Balance (First Hour): IB High=`0.1930` | IB Low=`0.1919`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.1917` - `0.1932`
  * Optimal Trade Entry (OTE 0.705): `0.1928`
  * Structural Invalidation Anchor (0.786): `0.1940`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.1925` | `0.1926` | `0.1921` | `0.1923` | `1,521,570` | 292,687.75 USD | -37,605.60 USD | `-12.85%` | -3,279,425.48 USD | `-0.32` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.1924` | `0.1928` | `0.1922` | `0.1928` | `1,827,731` | 351,875.49 USD | 166,076.68 USD | `+47.20%` | -3,113,348.80 USD | `+1.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.1928` | `0.1929` | `0.1926` | `0.1928` | `309,054` | 59,557.58 USD | -1,760.20 USD | `-2.96%` | -3,115,109.00 USD | `-0.18` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1921` | `0.1924` | `0.1912` | `0.1924` | `8,307,390` | 1,592,969.86 USD | 56,498.59 USD | `+3.55%` | -3,165,051.93 USD | `+0.04` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `0.1923` | `0.1928` | `0.1920` | `0.1928` | `6,565,851` | 1,263,727.12 USD | 75,148.96 USD | `+5.95%` | -3,089,902.97 USD | `+0.08` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.1928` | `0.1929` | `0.1926` | `0.1929` | `309,937` | 59,727.91 USD | -1,589.87 USD | `-2.66%` | -3,091,492.84 USD | `-0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1871` | `0.1899` | `0.1858` | `0.1890` | `34,457,559` | 6,492,300.86 USD | -34,935.20 USD | `-0.54%` | -3,549,912.57 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.1891` | `0.1925` | `0.1890` | `0.1922` | `38,552,834` | 7,355,562.18 USD | 283,539.33 USD | `+3.85%` | -3,266,373.24 USD | `+0.28` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `0.1921` | `0.1929` | `0.1912` | `0.1928` | `15,182,295` | 2,916,254.56 USD | 129,887.35 USD | `+4.45%` | -3,136,485.90 USD | `+0.20` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,580,512.54 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -3,611,263.47 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1929` | `0.1912` | `0.1928` | `15,182,295` | 2,916,254.56 USD | 129,887.35 USD | `+4.45%` | -3,481,376.12 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2009` | `0.2065` | `0.1996` | `0.2063` | `188,101,434` | 38,166,427.66 USD | 1,767,906.72 USD | `+4.63%` | 2,548,855.78 USD | `+1.00` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.2064` | `0.2087` | `0.2012` | `0.2022` | `158,619,640` | 32,404,571.85 USD | 439,532.34 USD | `+1.36%` | 2,988,388.12 USD | `-0.99` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.2022` | `0.2023` | `0.1871` | `0.1902` | `578,181,433` | 111,477,674.40 USD | -6,568,900.66 USD | `-5.89%` | -3,580,512.54 USD | `-1.71` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.1903` | `0.1925` | `0.1821` | `0.1922` | `389,376,322` | 72,711,522.42 USD | -30,750.93 USD | `-0.04%` | -3,611,263.47 USD | `+0.23` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.1921` | `0.1929` | `0.1912` | `0.1928` | `15,182,295` | 2,916,254.56 USD | 129,887.35 USD | `+4.45%` | -3,481,376.12 USD | `+0.26` | **`BULLISH`** | `NEUTRAL CHOP` |

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
| --- | **`0.1925`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:01:04 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `543` | `0x77ee...2902` | `SHORT` | 4,114,138.57 USD | `21,412,192.00` | `0.1911` | `0.1926` | `0.5705` | -22,886.83 USD | `-0.56%` | `10X Cross` |
| `1227` | `0x123d...3bff` | `LONG` | 1,809,536.41 USD | `9,392,870.00` | `0.2912` | `0.1926` | `0.000000` | -926,120.31 USD | `-51.18%` | `10X Cross` |
| `1264` | `0x7737...bf66` | `SHORT` | 1,751,470.92 USD | `9,091,466.00` | `0.2190` | `0.1926` | `2.05` | 239,518.87 USD | `+13.68%` | `10X Cross` |
| `1564` | `0x5f94...4b96` | `SHORT` | 1,379,820.56 USD | `7,162,318.00` | `0.2303` | `0.1926` | `0.7081` | 269,654.63 USD | `+19.54%` | `10X Cross` |
| `1799` | `0x4982...59e6` | `SHORT` | 1,154,471.37 USD | `5,998,812.00` | `0.1891` | `0.1926` | `0.4067` | -19,913.01 USD | `-1.72%` | `10X Cross` |
| `1850` | `0xcac1...26b3` | `LONG` | 1,117,313.99 USD | `5,803,927.00` | `0.2000` | `0.1926` | `0.000000` | -43,501.60 USD | `-3.89%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.2049` | 6,649.01 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2049 USD [API] | `2026-10-29 01:00:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2154` | 112.87 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.11K USD at 0.2154 USD [API] | `2026-09-03 14:48:53` |
| `ANNOUNCEMENT` | `INFO` | `0.2154` | 196.66 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.20K USD at 0.2154 USD [API] | `2026-09-03 14:48:53` |
| `ANNOUNCEMENT` | `INFO` | `0.1961` | 493.51 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Long: 0.49K USD at 0.1961 USD [API] | `2026-08-20 14:01:11` |
| `ANNOUNCEMENT` | `INFO` | `0.2049` | 6,648.65 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale BUY: 6.65K USD at 0.2049 USD [API] | `2026-10-29 01:17:48` |
| `ANNOUNCEMENT` | `INFO` | `0.2041` | 8,718.07 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 8.72K USD at 0.2041 USD [API] | `2026-10-29 01:25:22` |
| `ANNOUNCEMENT` | `INFO` | `0.2029` | 8,300.25 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 8.30K USD at 0.2029 USD [API] | `2026-10-29 01:33:52` |
| `ANNOUNCEMENT` | `INFO` | `0.2029` | 6,153.65 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 6.15K USD at 0.2029 USD [API] | `2026-10-29 01:33:52` |
| `ANNOUNCEMENT` | `INFO` | `0.2030` | 5,005.40 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.2030 USD [API] | `2026-10-29 01:33:52` |
| `ANNOUNCEMENT` | `INFO` | `0.1992` | 29,190.71 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 29.19K USD at 0.1992 USD [API] | `2026-10-29 01:52:39` |
| `ANNOUNCEMENT` | `INFO` | `0.1993` | 7,509.47 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 7.51K USD at 0.1993 USD [API] | `2026-10-29 01:52:39` |
| `ANNOUNCEMENT` | `INFO` | `0.1993` | 5,006.22 USD | `-` | `NEWS_INTEL` | `-` | #ADA Whale SELL: 5.01K USD at 0.1993 USD [API] | `2026-10-29 01:52:39` |
| `ANNOUNCEMENT` | `INFO` | `0.1969` | 236.46 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 0.24K USD at 0.1969 USD [API] | `2026-10-29 02:05:46` |
| `ANNOUNCEMENT` | `INFO` | `0.1969` | 174.44 USD | `-` | `NEWS_INTEL` | `-` | #ADA Liquidated Short: 0.17K USD at 0.1969 USD [API] | `2026-10-29 02:05:46` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.1943` (Vol: 288,800.00 USD, Dist: `+1.21%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.67%`)
  * 48H Horizon: Short MP=`0.1943` (Vol: 288,800.00 USD, Dist: `+1.17%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.69%`)
  * 3D Horizon: Short MP=`0.000000` (Vol: 0.00 USD, Dist: `+0.00%`) | Long MP=`0.1830` (Vol: 577,600.00 USD, Dist: `--4.69%`)
  * 7D Horizon: Short MP=`0.2131` (Vol: 448,200.00 USD, Dist: `+11.00%`) | Long MP=`0.1832` (Vol: 577,600.00 USD, Dist: `--4.60%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.0415` | 823.53 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0455` | 242.88 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0465` | 247.71 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0495` | 105.29 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0535` | 401.25 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0565` | 508.50 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0595` | 167.25 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0645` | 1,540.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0685` | 640.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0695` | 3,370.00 USD | 2,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0715` | 7,510.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0755` | 259.95 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0815` | 284.84 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0845` | 159,650.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0865` | 102.50 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0875` | 344.75 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0885` | 1,150.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0915` | 12,810.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0925` | 165.11 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0935` | 935.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0945` | 327.54 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0975` | 170.04 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.0985` | 87,280.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1015` | 343.58 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1025` | 4,100.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1035` | 1,050.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1055` | 4,310.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1065` | 653.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1075` | 2,630.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1095` | 1,490.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1115` | 114.96 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1145` | 1,230.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1165` | 40,150.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1175` | 8,820.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1185` | 169.34 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1205` | 826.27 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1215` | 1,050.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1235` | 1,180.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1245` | 404.62 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1255` | 1,980.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1265` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1275` | 1,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1295` | 2,540.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1305` | 13,060.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1315` | 687.35 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1325` | 6,960.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1335` | 5,910.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1345` | 491.46 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1355` | 106.64 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1365` | 403.77 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1405` | 314.44 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1415` | 9,540.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1425` | 1,060.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1435` | 15,780.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1445` | 2,220.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1455` | 7,330.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 37,670.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1475` | 292.94 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1485` | 1,360.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1495` | 427.12 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1505` | 3,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1515` | 35,710.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1525` | 981.95 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1535` | 42,360.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 721.05 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1555` | 1,940.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1565` | 10,860.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1575` | 157.50 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1585` | 703,320.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1595` | 2,780.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 57,720.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1615` | 4,200.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1625` | 2,180.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1645` | 10,840.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1665` | 1,950.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1675` | 630.81 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1685` | 12,160.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1695` | 78,180.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 626,600.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1710` | 4,180,000.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1715` | 252,270.00 USD | 388,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1720` | 4,140,000.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1725` | 33,550.00 USD | 136,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1730` | 4,080,000.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1735` | 1,270.00 USD | 102,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1740` | 4,040,000.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1745` | 234.18 USD | 101,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1750` | 4,030,000.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1755` | 18,510.00 USD | 101,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1760` | 4,010,000.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1765` | 42,760.00 USD | 82,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1770` | 3,920,000.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1775` | 1,360.00 USD | 40,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1780` | 3,760,000.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1785` | 4,530.00 USD | 38,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1790` | 3,590,000.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1790` | 13,210,000.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1795` | 3,840.00 USD | 34,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1800` | 3,420,000.00 USD | 3,420,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1800` | 13,120,000.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1805` | 12,610.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1810` | 3,270,000.00 USD | 3,270,000.00 USD | 50,420.00 USD | 27,730.00 USD | 44,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1810` | 13,090,000.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1815` | 11,080.00 USD | 17,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1820` | 3,150,000.00 USD | 3,150,000.00 USD | 159,050.00 USD | 14,270.00 USD | 72,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1820` | 12,920,000.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.1825` | 6,780.00 USD | 6,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.1830` | 2,910,000.00 USD | 2,910,000.00 USD | 72,410.00 USD | 24,810.00 USD | 133,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1830` | 12,620,000.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1840` | 2,670,000.00 USD | 2,670,000.00 USD | 113,190.00 USD | 50,780.00 USD | 145,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1840` | 12,440,000.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1850` | 2,370,000.00 USD | 2,370,000.00 USD | 110,780.00 USD | 66,490.00 USD | 179,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1850` | 11,950,000.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1860` | 2,010,000.00 USD | 2,010,000.00 USD | 228,970.00 USD | 8,970.00 USD | 94,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1860` | 10,940,000.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1870` | 1,680,000.00 USD | 1,680,000.00 USD | 178,050.00 USD | 55,340.00 USD | 277,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1870` | 10,560,000.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1880` | 1,170,000.00 USD | 1,170,000.00 USD | 294,230.00 USD | 92,270.00 USD | 246,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1880` | 10,300,000.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1890` | 532,270.00 USD | 532,270.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1890` | 10,040,000.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1900` | 80,250.00 USD | 80,250.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1900` | 9,600,000.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.1910` | 37,340.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1910` | 9,050,000.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1920` | 8,720,000.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1930` | 8,310,000.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1940` | 615,120.00 USD | 615,120.00 USD | 166,380.00 USD | 5,450.00 USD | 81,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1940` | 7,070,000.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.1950` | 973,990.00 USD | 973,990.00 USD | 96,260.00 USD | 25,730.00 USD | 236,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1950` | 5,210,000.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1955` | 755.22 USD | 755.22 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1960` | 3,870,000.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1965` | 104.93 USD | 860.15 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1970` | 2,990,000.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1975` | 187.03 USD | 1,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1980` | 2,360,000.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1985` | 338.64 USD | 1,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.1990` | 2,080,000.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.1995` | 252.97 USD | 1,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2000` | 800,740.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2005` | 2,570.00 USD | 4,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.2010` | 610,930.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2015` | 2,100.00 USD | 6,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2020` | 3,670,000.00 USD | 3,670,000.00 USD | 94,050.00 USD | 29,200.00 USD | 103,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2025` | 105.50 USD | 6,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2030` | 4,110,000.00 USD | 4,110,000.00 USD | 76,100.00 USD | 86,660.00 USD | 281,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2040` | 4,490,000.00 USD | 4,490,000.00 USD | 43,130.00 USD | 212,450.00 USD | 124,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2050` | 4,620,000.00 USD | 4,620,000.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2060` | 4,990,000.00 USD | 4,990,000.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2070` | 5,800,000.00 USD | 5,800,000.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2075` | 2,220.00 USD | 8,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2080` | 6,500,000.00 USD | 6,500,000.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2090` | 7,470,000.00 USD | 7,470,000.00 USD | 505,530.00 USD | 178,540.00 USD | 285,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2100` | 8,670,000.00 USD | 8,670,000.00 USD | 666,700.00 USD | 153,810.00 USD | 381,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2110` | 8,950,000.00 USD | 8,950,000.00 USD | 142,180.00 USD | 46,780.00 USD | 96,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2120` | 9,380,000.00 USD | 9,380,000.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2145` | 426.21 USD | 9,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2175` | 3,930.00 USD | 12,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2185` | 2,650.00 USD | 15,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2215` | 996.75 USD | 16,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2235` | 200.48 USD | 16,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2265` | 2,230.00 USD | 19,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2285` | 9,240.00 USD | 28,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.2325` | 282.02 USD | 28,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2335` | 7,640.00 USD | 36,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2405` | 1,670.00 USD | 37,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2415` | 1,310.00 USD | 39,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2425` | 1,080.00 USD | 40,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2435` | 1,040.00 USD | 41,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2585` | 380.25 USD | 41,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2635` | 1,390.00 USD | 43,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2675` | 1,970.00 USD | 45,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2715` | 120.00 USD | 45,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2775` | 379.62 USD | 45,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2845` | 2,170.00 USD | 47,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2895` | 411.09 USD | 48,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2915` | 3,260.00 USD | 51,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2935` | 519.79 USD | 51,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2945` | 2,560.00 USD | 54,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.2955` | 7,990.00 USD | 62,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3005` | 1,260.00 USD | 63,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3045` | 4,240.00 USD | 67,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3055` | 408.15 USD | 68,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3075` | 67,840.00 USD | 136,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3115` | 97,190.00 USD | 233,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3145` | 3,600.00 USD | 237,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3225` | 1,130.00 USD | 238,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3235` | 36,880.00 USD | 275,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3275` | 311.12 USD | 275,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3295` | 2,380.00 USD | 277,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3305` | 799.81 USD | 278,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3335` | 2,930.00 USD | 281,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3425` | 78,160.00 USD | 359,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3455` | 198,800.00 USD | 558,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3465` | 248.09 USD | 558,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3505` | 331.22 USD | 559,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3515` | 1,120.00 USD | 560,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3525` | 157.57 USD | 560,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3545` | 142.15 USD | 560,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3565` | 106.95 USD | 560,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3585` | 328.03 USD | 560,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3615` | 2,940.00 USD | 563,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3625` | 261,420.00 USD | 825,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3705` | 942.18 USD | 826,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3715` | 9,170.00 USD | 835,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3745` | 3,140.00 USD | 838,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.3795` | 24,090.00 USD | 862,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.0415` | 2,440,000.00 USD | 0.00 USD | 823.53 USD | `-78.32%` | `19,844.00` |
| `Live` | `Long` | `0.0455` | 2,440,000.00 USD | 0.00 USD | 242.88 USD | `-76.23%` | `5,338.00` |
| `Live` | `Long` | `0.0465` | 2,440,000.00 USD | 0.00 USD | 247.71 USD | `-75.71%` | `5,327.00` |
| `Live` | `Long` | `0.0495` | 2,440,000.00 USD | 0.00 USD | 105.29 USD | `-74.14%` | `2,127.00` |
| `Live` | `Long` | `0.0535` | 2,440,000.00 USD | 0.00 USD | 401.25 USD | `-72.05%` | `7,500.00` |
| `Live` | `Long` | `0.0565` | 2,440,000.00 USD | 0.00 USD | 508.50 USD | `-70.48%` | `9,000.00` |
| `Live` | `Long` | `0.0595` | 2,440,000.00 USD | 0.00 USD | 167.25 USD | `-68.91%` | `2,811.00` |
| `Live` | `Long` | `0.0645` | 2,440,000.00 USD | 0.00 USD | 1,540.00 USD | `-66.30%` | `23,814.00` |
| `Live` | `Long` | `0.0685` | 2,440,000.00 USD | 0.00 USD | 640.00 USD | `-64.21%` | `9,343.00` |
| `Live` | `Long` | `0.0695` | 2,440,000.00 USD | 0.00 USD | 3,370.00 USD | `-63.69%` | `48,444.00` |
| `Live` | `Long` | `0.0715` | 2,430,000.00 USD | 0.00 USD | 7,510.00 USD | `-62.65%` | `105,008.00` |
| `Live` | `Long` | `0.0755` | 2,430,000.00 USD | 0.00 USD | 259.95 USD | `-60.56%` | `3,443.00` |
| `Live` | `Long` | `0.0815` | 2,430,000.00 USD | 0.00 USD | 284.84 USD | `-57.42%` | `3,495.00` |
| `Live` | `Long` | `0.0845` | 2,430,000.00 USD | 0.00 USD | 159,650.00 USD | `-55.85%` | `1,889,331.00` |
| `Live` | `Long` | `0.0865` | 2,270,000.00 USD | 0.00 USD | 102.50 USD | `-54.81%` | `1,185.00` |
| `Live` | `Long` | `0.0875` | 2,270,000.00 USD | 0.00 USD | 344.75 USD | `-54.29%` | `3,940.00` |
| `Live` | `Long` | `0.0885` | 2,270,000.00 USD | 0.00 USD | 1,150.00 USD | `-53.76%` | `13,050.00` |
| `Live` | `Long` | `0.0915` | 2,260,000.00 USD | 0.00 USD | 12,810.00 USD | `-52.20%` | `140,000.00` |
| `Live` | `Long` | `0.0925` | 2,250,000.00 USD | 0.00 USD | 165.11 USD | `-51.67%` | `1,785.00` |
| `Live` | `Long` | `0.0935` | 2,250,000.00 USD | 0.00 USD | 935.00 USD | `-51.15%` | `10,000.00` |
| `Live` | `Long` | `0.0945` | 2,250,000.00 USD | 0.00 USD | 327.54 USD | `-50.63%` | `3,466.00` |
| `Live` | `Long` | `0.0975` | 2,250,000.00 USD | 0.00 USD | 170.04 USD | `-49.06%` | `1,744.00` |
| `Live` | `Long` | `0.0985` | 2,250,000.00 USD | 0.00 USD | 87,280.00 USD | `-48.54%` | `886,128.00` |
| `Live` | `Long` | `0.1015` | 2,160,000.00 USD | 0.00 USD | 343.58 USD | `-46.97%` | `3,385.00` |
| `Live` | `Long` | `0.1025` | 2,160,000.00 USD | 0.00 USD | 4,100.00 USD | `-46.45%` | `40,000.00` |
| `Live` | `Long` | `0.1035` | 2,160,000.00 USD | 0.00 USD | 1,050.00 USD | `-45.93%` | `10,149.00` |
| `Live` | `Long` | `0.1055` | 2,160,000.00 USD | 0.00 USD | 4,310.00 USD | `-44.88%` | `40,836.00` |
| `Live` | `Long` | `0.1065` | 2,150,000.00 USD | 0.00 USD | 653.70 USD | `-44.36%` | `6,138.00` |
| `Live` | `Long` | `0.1075` | 2,150,000.00 USD | 0.00 USD | 2,630.00 USD | `-43.84%` | `24,424.00` |
| `Live` | `Long` | `0.1095` | 2,150,000.00 USD | 0.00 USD | 1,490.00 USD | `-42.79%` | `13,608.00` |
| `Live` | `Long` | `0.1115` | 2,150,000.00 USD | 0.00 USD | 114.96 USD | `-41.75%` | `1,031.00` |
| `Live` | `Long` | `0.1145` | 2,150,000.00 USD | 0.00 USD | 1,230.00 USD | `-40.18%` | `10,702.00` |
| `Live` | `Long` | `0.1165` | 2,150,000.00 USD | 0.00 USD | 40,150.00 USD | `-39.13%` | `344,662.00` |
| `Live` | `Long` | `0.1175` | 2,110,000.00 USD | 0.00 USD | 8,820.00 USD | `-38.61%` | `75,083.00` |
| `Live` | `Long` | `0.1185` | 2,100,000.00 USD | 0.00 USD | 169.34 USD | `-38.09%` | `1,429.00` |
| `Live` | `Long` | `0.1205` | 2,100,000.00 USD | 0.00 USD | 826.27 USD | `-37.05%` | `6,857.00` |
| `Live` | `Long` | `0.1215` | 2,100,000.00 USD | 0.00 USD | 1,050.00 USD | `-36.52%` | `8,652.00` |
| `Live` | `Long` | `0.1235` | 2,100,000.00 USD | 0.00 USD | 1,180.00 USD | `-35.48%` | `9,522.00` |
| `Live` | `Long` | `0.1245` | 2,100,000.00 USD | 0.00 USD | 404.62 USD | `-34.96%` | `3,250.00` |
| `Live` | `Long` | `0.1255` | 2,090,000.00 USD | 0.00 USD | 1,980.00 USD | `-34.43%` | `15,773.00` |
| `Live` | `Long` | `0.1265` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-33.91%` | `2,487.00` |
| `Live` | `Long` | `0.1275` | 2,090,000.00 USD | 0.00 USD | 1,260.00 USD | `-33.39%` | `9,873.00` |
| `Live` | `Long` | `0.1295` | 2,090,000.00 USD | 0.00 USD | 2,540.00 USD | `-32.34%` | `19,609.00` |
| `Live` | `Long` | `0.1305` | 2,090,000.00 USD | 0.00 USD | 13,060.00 USD | `-31.82%` | `100,090.00` |
| `Live` | `Long` | `0.1315` | 2,080,000.00 USD | 0.00 USD | 687.35 USD | `-31.30%` | `5,227.00` |
| `Live` | `Long` | `0.1325` | 2,070,000.00 USD | 0.00 USD | 6,960.00 USD | `-30.78%` | `52,553.00` |
| `Live` | `Long` | `0.1335` | 2,070,000.00 USD | 0.00 USD | 5,910.00 USD | `-30.25%` | `44,280.00` |
| `Live` | `Long` | `0.1345` | 2,060,000.00 USD | 0.00 USD | 491.46 USD | `-29.73%` | `3,654.00` |
| `Live` | `Long` | `0.1355` | 2,060,000.00 USD | 0.00 USD | 106.64 USD | `-29.21%` | `787.00` |
| `Live` | `Long` | `0.1365` | 2,060,000.00 USD | 0.00 USD | 403.77 USD | `-28.69%` | `2,958.00` |
| `Live` | `Long` | `0.1405` | 2,060,000.00 USD | 0.00 USD | 314.44 USD | `-26.60%` | `2,238.00` |
| `Live` | `Long` | `0.1415` | 2,060,000.00 USD | 0.00 USD | 9,540.00 USD | `-26.07%` | `67,399.00` |
| `Live` | `Long` | `0.1425` | 2,050,000.00 USD | 0.00 USD | 1,060.00 USD | `-25.55%` | `7,443.00` |
| `Live` | `Long` | `0.1435` | 2,050,000.00 USD | 0.00 USD | 15,780.00 USD | `-25.03%` | `109,977.00` |
| `Live` | `Long` | `0.1445` | 2,030,000.00 USD | 0.00 USD | 2,220.00 USD | `-24.51%` | `15,394.00` |
| `Live` | `Long` | `0.1455` | 2,030,000.00 USD | 0.00 USD | 7,330.00 USD | `-23.98%` | `50,393.00` |
| `Live` | `Long` | `0.1465` | 2,020,000.00 USD | 0.00 USD | 37,670.00 USD | `-23.46%` | `257,143.00` |
| `Live` | `Long` | `0.1475` | 1,990,000.00 USD | 0.00 USD | 292.94 USD | `-22.94%` | `1,986.00` |
| `Live` | `Long` | `0.1485` | 1,990,000.00 USD | 0.00 USD | 1,360.00 USD | `-22.42%` | `9,140.00` |
| `Live` | `Long` | `0.1495` | 1,990,000.00 USD | 0.00 USD | 427.12 USD | `-21.89%` | `2,857.00` |
| `Live` | `Long` | `0.1505` | 1,990,000.00 USD | 0.00 USD | 3,000.00 USD | `-21.37%` | `19,912.00` |
| `Live` | `Long` | `0.1515` | 1,980,000.00 USD | 0.00 USD | 35,710.00 USD | `-20.85%` | `235,729.00` |
| `Live` | `Long` | `0.1525` | 1,950,000.00 USD | 0.00 USD | 981.95 USD | `-20.33%` | `6,439.00` |
| `Live` | `Long` | `0.1535` | 1,950,000.00 USD | 0.00 USD | 42,360.00 USD | `-19.80%` | `275,955.00` |
| `Live` | `Long` | `0.1545` | 1,900,000.00 USD | 0.00 USD | 721.05 USD | `-19.28%` | `4,667.00` |
| `Live` | `Long` | `0.1555` | 1,900,000.00 USD | 0.00 USD | 1,940.00 USD | `-18.76%` | `12,478.00` |
| `Live` | `Long` | `0.1565` | 1,900,000.00 USD | 0.00 USD | 10,860.00 USD | `-18.24%` | `69,381.00` |
| `Live` | `Long` | `0.1575` | 1,890,000.00 USD | 0.00 USD | 157.50 USD | `-17.71%` | `1,000.00` |
| `Live` | `Long` | `0.1585` | 1,890,000.00 USD | 0.00 USD | 703,320.00 USD | `-17.19%` | `4,437,337.00` |
| `Live` | `Long` | `0.1595` | 1,190,000.00 USD | 0.00 USD | 2,780.00 USD | `-16.67%` | `17,408.00` |
| `Live` | `Long` | `0.1605` | 1,180,000.00 USD | 0.00 USD | 57,720.00 USD | `-16.15%` | `359,655.00` |
| `Live` | `Long` | `0.1615` | 1,130,000.00 USD | 0.00 USD | 4,200.00 USD | `-15.62%` | `26,015.00` |
| `Live` | `Long` | `0.1625` | 1,120,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.10%` | `13,446.00` |
| `Live` | `Long` | `0.1645` | 1,120,000.00 USD | 0.00 USD | 10,840.00 USD | `-14.06%` | `65,896.00` |
| `Live` | `Long` | `0.1665` | 1,110,000.00 USD | 0.00 USD | 1,950.00 USD | `-13.01%` | `11,682.00` |
| `Live` | `Long` | `0.1675` | 1,110,000.00 USD | 0.00 USD | 630.81 USD | `-12.49%` | `3,766.00` |
| `Live` | `Long` | `0.1685` | 1,110,000.00 USD | 0.00 USD | 12,160.00 USD | `-11.97%` | `72,152.00` |
| `Live` | `Long` | `0.1695` | 1,090,000.00 USD | 0.00 USD | 78,180.00 USD | `-11.45%` | `461,249.00` |
| `Live` | `Long` | `0.1705` | 1,020,000.00 USD | 0.00 USD | 626,600.00 USD | `-10.92%` | `3,675,078.00` |
| `Live` | `Long` | `0.1715` | 388,790.00 USD | 0.00 USD | 252,270.00 USD | `-10.40%` | `1,470,975.00` |
| `Live` | `Long` | `0.1725` | 136,510.00 USD | 0.00 USD | 33,550.00 USD | `-9.88%` | `194,482.00` |
| `Live` | `Long` | `0.1735` | 102,970.00 USD | 0.00 USD | 1,270.00 USD | `-9.36%` | `7,296.00` |
| `Live` | `Long` | `0.1745` | 101,700.00 USD | 0.00 USD | 234.18 USD | `-8.83%` | `1,342.00` |
| `Live` | `Long` | `0.1755` | 101,460.00 USD | 0.00 USD | 18,510.00 USD | `-8.31%` | `105,458.00` |
| `Live` | `Long` | `0.1765` | 82,960.00 USD | 0.00 USD | 42,760.00 USD | `-7.79%` | `242,276.00` |
| `Live` | `Long` | `0.1775` | 40,200.00 USD | 0.00 USD | 1,360.00 USD | `-7.27%` | `7,657.00` |
| `Live` | `Long` | `0.1785` | 38,840.00 USD | 0.00 USD | 4,530.00 USD | `-6.74%` | `25,371.00` |
| `Live` | `Long` | `0.1795` | 34,310.00 USD | 0.00 USD | 3,840.00 USD | `-6.22%` | `21,396.00` |
| `Live` | `Long` | `0.1805` | 30,470.00 USD | 0.00 USD | 12,610.00 USD | `-5.70%` | `69,840.00` |
| `Live` | `Long` | `0.1815` | 17,860.00 USD | 0.00 USD | 11,080.00 USD | `-5.18%` | `61,030.00` |
| `Live` | `Long` | `0.1825` | 6,780.00 USD | 0.00 USD | 6,780.00 USD | `-4.65%` | `37,172.00` |
| `Live` | `Short` | `0.1955` | 755.22 USD | 755.22 USD | 0.00 USD | `+2.14%` | `3,863.00` |
| `Live` | `Short` | `0.1965` | 860.15 USD | 104.93 USD | 0.00 USD | `+2.66%` | `534.00` |
| `Live` | `Short` | `0.1975` | 1,050.00 USD | 187.03 USD | 0.00 USD | `+3.18%` | `947.00` |
| `Live` | `Short` | `0.1985` | 1,390.00 USD | 338.64 USD | 0.00 USD | `+3.71%` | `1,706.00` |
| `Live` | `Short` | `0.1995` | 1,640.00 USD | 252.97 USD | 0.00 USD | `+4.23%` | `1,268.00` |
| `Live` | `Short` | `0.2005` | 4,210.00 USD | 2,570.00 USD | 0.00 USD | `+4.75%` | `12,837.00` |
| `Live` | `Short` | `0.2015` | 6,310.00 USD | 2,100.00 USD | 0.00 USD | `+5.27%` | `10,418.00` |
| `Live` | `Short` | `0.2025` | 6,420.00 USD | 105.50 USD | 0.00 USD | `+5.80%` | `521.00` |
| `Live` | `Short` | `0.2075` | 8,630.00 USD | 2,220.00 USD | 0.00 USD | `+8.41%` | `10,683.00` |
| `Live` | `Short` | `0.2145` | 9,060.00 USD | 426.21 USD | 0.00 USD | `+12.06%` | `1,987.00` |
| `Live` | `Short` | `0.2175` | 12,990.00 USD | 3,930.00 USD | 0.00 USD | `+13.63%` | `18,067.00` |
| `Live` | `Short` | `0.2185` | 15,640.00 USD | 2,650.00 USD | 0.00 USD | `+14.15%` | `12,136.00` |
| `Live` | `Short` | `0.2215` | 16,640.00 USD | 996.75 USD | 0.00 USD | `+15.72%` | `4,500.00` |
| `Live` | `Short` | `0.2235` | 16,840.00 USD | 200.48 USD | 0.00 USD | `+16.77%` | `897.00` |
| `Live` | `Short` | `0.2265` | 19,070.00 USD | 2,230.00 USD | 0.00 USD | `+18.33%` | `9,853.00` |
| `Live` | `Short` | `0.2285` | 28,310.00 USD | 9,240.00 USD | 0.00 USD | `+19.38%` | `40,428.00` |
| `Live` | `Short` | `0.2325` | 28,590.00 USD | 282.02 USD | 0.00 USD | `+21.47%` | `1,213.00` |
| `Live` | `Short` | `0.2335` | 36,230.00 USD | 7,640.00 USD | 0.00 USD | `+21.99%` | `32,708.00` |
| `Live` | `Short` | `0.2405` | 37,900.00 USD | 1,670.00 USD | 0.00 USD | `+25.65%` | `6,957.00` |
| `Live` | `Short` | `0.2415` | 39,210.00 USD | 1,310.00 USD | 0.00 USD | `+26.17%` | `5,427.00` |
| `Live` | `Short` | `0.2425` | 40,290.00 USD | 1,080.00 USD | 0.00 USD | `+26.69%` | `4,435.00` |
| `Live` | `Short` | `0.2435` | 41,320.00 USD | 1,040.00 USD | 0.00 USD | `+27.22%` | `4,254.00` |
| `Live` | `Short` | `0.2585` | 41,700.00 USD | 380.25 USD | 0.00 USD | `+35.05%` | `1,471.00` |
| `Live` | `Short` | `0.2635` | 43,100.00 USD | 1,390.00 USD | 0.00 USD | `+37.66%` | `5,287.00` |
| `Live` | `Short` | `0.2675` | 45,070.00 USD | 1,970.00 USD | 0.00 USD | `+39.75%` | `7,372.00` |
| `Live` | `Short` | `0.2715` | 45,190.00 USD | 120.00 USD | 0.00 USD | `+41.84%` | `442.00` |
| `Live` | `Short` | `0.2775` | 45,570.00 USD | 379.62 USD | 0.00 USD | `+44.98%` | `1,368.00` |
| `Live` | `Short` | `0.2845` | 47,740.00 USD | 2,170.00 USD | 0.00 USD | `+48.64%` | `7,640.00` |
| `Live` | `Short` | `0.2895` | 48,150.00 USD | 411.09 USD | 0.00 USD | `+51.25%` | `1,420.00` |
| `Live` | `Short` | `0.2915` | 51,420.00 USD | 3,260.00 USD | 0.00 USD | `+52.29%` | `11,194.00` |
| `Live` | `Short` | `0.2935` | 51,940.00 USD | 519.79 USD | 0.00 USD | `+53.34%` | `1,771.00` |
| `Live` | `Short` | `0.2945` | 54,500.00 USD | 2,560.00 USD | 0.00 USD | `+53.86%` | `8,697.00` |
| `Live` | `Short` | `0.2955` | 62,480.00 USD | 7,990.00 USD | 0.00 USD | `+54.38%` | `27,027.00` |
| `Live` | `Short` | `0.3005` | 63,750.00 USD | 1,260.00 USD | 0.00 USD | `+57.00%` | `4,200.00` |
| `Live` | `Short` | `0.3045` | 67,990.00 USD | 4,240.00 USD | 0.00 USD | `+59.09%` | `13,937.00` |
| `Live` | `Short` | `0.3055` | 68,400.00 USD | 408.15 USD | 0.00 USD | `+59.61%` | `1,336.00` |
| `Live` | `Short` | `0.3075` | 136,240.00 USD | 67,840.00 USD | 0.00 USD | `+60.65%` | `220,630.00` |
| `Live` | `Short` | `0.3115` | 233,440.00 USD | 97,190.00 USD | 0.00 USD | `+62.74%` | `312,021.00` |
| `Live` | `Short` | `0.3145` | 237,040.00 USD | 3,600.00 USD | 0.00 USD | `+64.31%` | `11,458.00` |
| `Live` | `Short` | `0.3225` | 238,170.00 USD | 1,130.00 USD | 0.00 USD | `+68.49%` | `3,500.00` |
| `Live` | `Short` | `0.3235` | 275,050.00 USD | 36,880.00 USD | 0.00 USD | `+69.01%` | `114,011.00` |
| `Live` | `Short` | `0.3275` | 275,360.00 USD | 311.12 USD | 0.00 USD | `+71.10%` | `950.00` |
| `Live` | `Short` | `0.3295` | 277,740.00 USD | 2,380.00 USD | 0.00 USD | `+72.15%` | `7,219.00` |
| `Live` | `Short` | `0.3305` | 278,540.00 USD | 799.81 USD | 0.00 USD | `+72.67%` | `2,420.00` |
| `Live` | `Short` | `0.3335` | 281,470.00 USD | 2,930.00 USD | 0.00 USD | `+74.24%` | `8,785.00` |
| `Live` | `Short` | `0.3425` | 359,630.00 USD | 78,160.00 USD | 0.00 USD | `+78.94%` | `228,215.00` |
| `Live` | `Short` | `0.3455` | 558,440.00 USD | 198,800.00 USD | 0.00 USD | `+80.51%` | `575,408.00` |
| `Live` | `Short` | `0.3465` | 558,680.00 USD | 248.09 USD | 0.00 USD | `+81.03%` | `716.00` |
| `Live` | `Short` | `0.3505` | 559,020.00 USD | 331.22 USD | 0.00 USD | `+83.12%` | `945.00` |
| `Live` | `Short` | `0.3515` | 560,140.00 USD | 1,120.00 USD | 0.00 USD | `+83.64%` | `3,187.00` |
| `Live` | `Short` | `0.3525` | 560,290.00 USD | 157.57 USD | 0.00 USD | `+84.16%` | `447.00` |
| `Live` | `Short` | `0.3545` | 560,440.00 USD | 142.15 USD | 0.00 USD | `+85.21%` | `401.00` |
| `Live` | `Short` | `0.3565` | 560,540.00 USD | 106.95 USD | 0.00 USD | `+86.25%` | `300.00` |
| `Live` | `Short` | `0.3585` | 560,870.00 USD | 328.03 USD | 0.00 USD | `+87.30%` | `915.00` |
| `Live` | `Short` | `0.3615` | 563,810.00 USD | 2,940.00 USD | 0.00 USD | `+88.86%` | `8,134.00` |
| `Live` | `Short` | `0.3625` | 825,230.00 USD | 261,420.00 USD | 0.00 USD | `+89.39%` | `721,150.00` |
| `Live` | `Short` | `0.3705` | 826,170.00 USD | 942.18 USD | 0.00 USD | `+93.57%` | `2,543.00` |
| `Live` | `Short` | `0.3715` | 835,340.00 USD | 9,170.00 USD | 0.00 USD | `+94.09%` | `24,689.00` |
| `Live` | `Short` | `0.3745` | 838,490.00 USD | 3,140.00 USD | 0.00 USD | `+95.66%` | `8,395.00` |
| `Live` | `Short` | `0.3795` | 862,580.00 USD | 24,090.00 USD | 0.00 USD | `+98.27%` | `63,484.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.0595` | 110,710,000.00 USD | 0.00 USD | 415.13 USD | `-68.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.0605` | 110,710,000.00 USD | 0.00 USD | 438.99 USD | `-68.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1105` | 110,700,000.00 USD | 0.00 USD | 1,100.00 USD | `-42.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1115` | 110,700,000.00 USD | 0.00 USD | 541.33 USD | `-41.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1155` | 110,700,000.00 USD | 0.00 USD | 429.20 USD | `-39.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1205` | 110,700,000.00 USD | 0.00 USD | 602,500.00 USD | `-37.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1235` | 110,100,000.00 USD | 0.00 USD | 4,460.00 USD | `-35.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1275` | 110,100,000.00 USD | 0.00 USD | 1,320.00 USD | `-33.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1305` | 110,090,000.00 USD | 0.00 USD | 13,390.00 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1325` | 110,080,000.00 USD | 0.00 USD | 728.88 USD | `-30.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1345` | 110,080,000.00 USD | 0.00 USD | 4,350.00 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1375` | 110,080,000.00 USD | 0.00 USD | 4,730.00 USD | `-28.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1395` | 110,070,000.00 USD | 0.00 USD | 1,820.00 USD | `-27.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1415` | 110,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-26.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1425` | 110,070,000.00 USD | 0.00 USD | 351.26 USD | `-25.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1435` | 110,070,000.00 USD | 0.00 USD | 1,600.00 USD | `-25.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1455` | 110,070,000.00 USD | 0.00 USD | 10,400.00 USD | `-23.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1495` | 110,060,000.00 USD | 0.00 USD | 5,980.00 USD | `-21.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1505` | 110,050,000.00 USD | 0.00 USD | 303.26 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1515` | 110,050,000.00 USD | 0.00 USD | 3,230.00 USD | `-20.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1525` | 110,050,000.00 USD | 0.00 USD | 6,380.00 USD | `-20.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1545` | 110,040,000.00 USD | 0.00 USD | 126.54 USD | `-19.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1555` | 110,040,000.00 USD | 0.00 USD | 1,790.00 USD | `-18.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1565` | 110,040,000.00 USD | 0.00 USD | 6,260.00 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1585` | 110,030,000.00 USD | 0.00 USD | 552.21 USD | `-17.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1595` | 110,030,000.00 USD | 0.00 USD | 166.84 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1605` | 110,030,000.00 USD | 0.00 USD | 9,410.00 USD | `-16.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1615` | 110,020,000.00 USD | 0.00 USD | 769.39 USD | `-15.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1625` | 110,020,000.00 USD | 0.00 USD | 24,760.00 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1635` | 110,000,000.00 USD | 0.00 USD | 6,540.00 USD | `-14.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1645` | 109,990,000.00 USD | 0.00 USD | 1,750.00 USD | `-14.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1655` | 109,990,000.00 USD | 0.00 USD | 452.97 USD | `-13.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1665` | 109,990,000.00 USD | 0.00 USD | 12,640.00 USD | `-13.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1675` | 109,970,000.00 USD | 0.00 USD | 317.92 USD | `-12.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1695` | 109,970,000.00 USD | 0.00 USD | 4,270.00 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1705` | 109,970,000.00 USD | 0.00 USD | 1,300.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1715` | 109,970,000.00 USD | 0.00 USD | 1,220.00 USD | `-10.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1725` | 109,970,000.00 USD | 0.00 USD | 640.67 USD | `-9.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1735` | 109,970,000.00 USD | 0.00 USD | 595.80 USD | `-9.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1745` | 109,970,000.00 USD | 0.00 USD | 885.06 USD | `-8.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1755` | 109,970,000.00 USD | 0.00 USD | 1,760.00 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1765` | 109,960,000.00 USD | 0.00 USD | 847.38 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1775` | 109,960,000.00 USD | 0.00 USD | 5,090.00 USD | `-7.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1785` | 109,960,000.00 USD | 0.00 USD | 5,400.00 USD | `-6.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1795` | 109,950,000.00 USD | 0.00 USD | 15,050.00 USD | `-6.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1805` | 109,940,000.00 USD | 0.00 USD | 1,570.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1815` | 109,940,000.00 USD | 0.00 USD | 2,720.00 USD | `-5.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1825` | 109,930,000.00 USD | 0.00 USD | 36,500,000.00 USD | `-4.65%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1835` | 73,430,000.00 USD | 0.00 USD | 73,400,000.00 USD | `-4.13%` | `HIGH (Cascade Hazard)` |
| `Sell Stop` | `0.1845` | 33,320.00 USD | 0.00 USD | 18,800.00 USD | `-3.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1855` | 14,510.00 USD | 0.00 USD | 3,970.00 USD | `-3.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1865` | 10,550.00 USD | 0.00 USD | 1,420.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1875` | 9,130.00 USD | 0.00 USD | 3,580.00 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1885` | 5,550.00 USD | 0.00 USD | 3,100.00 USD | `-1.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1895` | 2,450.00 USD | 0.00 USD | 2,320.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.1905` | 126.49 USD | 0.00 USD | 126.49 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1915` | 2,090.00 USD | 2,090.00 USD | 0.00 USD | `+0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1925` | 2,450.00 USD | 362.29 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1935` | 3,840.00 USD | 1,390.00 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1945` | 4,230.00 USD | 389.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1955` | 4,480.00 USD | 247.89 USD | 0.00 USD | `+2.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1965` | 8,130.00 USD | 3,660.00 USD | 0.00 USD | `+2.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1975` | 9,140.00 USD | 1,000.00 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1985` | 9,780.00 USD | 646.71 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.1995` | 10,180.00 USD | 399.00 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2005` | 27,040.00 USD | 16,860.00 USD | 0.00 USD | `+4.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2015` | 73,380.00 USD | 46,340.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2025` | 73,980.00 USD | 594.34 USD | 0.00 USD | `+5.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2035` | 81,180.00 USD | 7,210.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2045` | 83,870.00 USD | 2,690.00 USD | 0.00 USD | `+6.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2055` | 86,030.00 USD | 2,160.00 USD | 0.00 USD | `+7.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2065` | 86,230.00 USD | 207.74 USD | 0.00 USD | `+7.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2075` | 86,550.00 USD | 312.70 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2085` | 94,890.00 USD | 8,340.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2095` | 103,040.00 USD | 8,150.00 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2105` | 125,110.00 USD | 22,070.00 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2115` | 144,930.00 USD | 19,820.00 USD | 0.00 USD | `+10.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2125` | 151,640.00 USD | 6,700.00 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2135` | 155,830.00 USD | 4,190.00 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2145` | 156,790.00 USD | 965.25 USD | 0.00 USD | `+12.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2155` | 167,100.00 USD | 10,300.00 USD | 0.00 USD | `+12.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2165` | 167,710.00 USD | 609.66 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2185` | 167,820.00 USD | 109.91 USD | 0.00 USD | `+14.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2195` | 183,280.00 USD | 15,460.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2205` | 186,040.00 USD | 2,760.00 USD | 0.00 USD | `+15.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2215` | 187,690.00 USD | 1,650.00 USD | 0.00 USD | `+15.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2225` | 196,870.00 USD | 9,180.00 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2235` | 200,620.00 USD | 3,750.00 USD | 0.00 USD | `+16.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2245` | 200,730.00 USD | 114.50 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2255` | 201,070.00 USD | 339.60 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2265` | 201,180.00 USD | 109.40 USD | 0.00 USD | `+18.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2275` | 201,330.00 USD | 151.06 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2285` | 210,470.00 USD | 9,140.00 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2305` | 211,140.00 USD | 662.92 USD | 0.00 USD | `+20.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2315` | 211,470.00 USD | 337.06 USD | 0.00 USD | `+20.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2325` | 211,650.00 USD | 171.12 USD | 0.00 USD | `+21.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2335` | 211,750.00 USD | 101.11 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2345` | 212,860.00 USD | 1,110.00 USD | 0.00 USD | `+22.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2355` | 222,280.00 USD | 9,420.00 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2365` | 222,720.00 USD | 443.91 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2375` | 223,500.00 USD | 778.76 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2385` | 223,690.00 USD | 192.71 USD | 0.00 USD | `+24.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2395` | 224,210.00 USD | 514.45 USD | 0.00 USD | `+25.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2405` | 224,420.00 USD | 209.72 USD | 0.00 USD | `+25.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2415` | 224,530.00 USD | 115.92 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2435` | 224,770.00 USD | 236.19 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2445` | 225,920.00 USD | 1,150.00 USD | 0.00 USD | `+27.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2455` | 226,200.00 USD | 288.22 USD | 0.00 USD | `+28.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2465` | 226,700.00 USD | 491.03 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2475` | 228,020.00 USD | 1,320.00 USD | 0.00 USD | `+29.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2485` | 237,960.00 USD | 9,940.00 USD | 0.00 USD | `+29.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2495` | 238,460.00 USD | 499.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2505` | 239,560.00 USD | 1,100.00 USD | 0.00 USD | `+30.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2515` | 239,730.00 USD | 168.76 USD | 0.00 USD | `+31.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2525` | 240,330.00 USD | 603.73 USD | 0.00 USD | `+31.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2535` | 242,500.00 USD | 2,170.00 USD | 0.00 USD | `+32.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2575` | 244,200.00 USD | 1,700.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2595` | 244,470.00 USD | 271.44 USD | 0.00 USD | `+35.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2605` | 665,220.00 USD | 420,750.00 USD | 0.00 USD | `+36.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2645` | 666,410.00 USD | 1,180.00 USD | 0.00 USD | `+38.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2675` | 675,300.00 USD | 8,890.00 USD | 0.00 USD | `+39.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2685` | 690,160.00 USD | 14,860.00 USD | 0.00 USD | `+40.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2695` | 691,500.00 USD | 1,340.00 USD | 0.00 USD | `+40.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2715` | 694,210.00 USD | 2,710.00 USD | 0.00 USD | `+41.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2735` | 708,080.00 USD | 13,870.00 USD | 0.00 USD | `+42.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2745` | 713,290.00 USD | 5,220.00 USD | 0.00 USD | `+43.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2775` | 714,470.00 USD | 1,170.00 USD | 0.00 USD | `+44.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2785` | 718,620.00 USD | 4,150.00 USD | 0.00 USD | `+45.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2795` | 719,570.00 USD | 944.99 USD | 0.00 USD | `+46.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2835` | 719,770.00 USD | 198.73 USD | 0.00 USD | `+48.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2845` | 721,140.00 USD | 1,370.00 USD | 0.00 USD | `+48.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2875` | 722,220.00 USD | 1,080.00 USD | 0.00 USD | `+50.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2905` | 737,200.00 USD | 14,980.00 USD | 0.00 USD | `+51.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2915` | 738,430.00 USD | 1,230.00 USD | 0.00 USD | `+52.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2975` | 739,880.00 USD | 1,440.00 USD | 0.00 USD | `+55.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.2995` | 740,230.00 USD | 355.21 USD | 0.00 USD | `+56.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3005` | 746,880.00 USD | 6,650.00 USD | 0.00 USD | `+57.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3055` | 765,860.00 USD | 18,980.00 USD | 0.00 USD | `+59.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3085` | 770,010.00 USD | 4,150.00 USD | 0.00 USD | `+61.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3145` | 773,260.00 USD | 3,250.00 USD | 0.00 USD | `+64.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3245` | 773,750.00 USD | 493.89 USD | 0.00 USD | `+69.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3255` | 773,930.00 USD | 181.30 USD | 0.00 USD | `+70.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3295` | 775,320.00 USD | 1,380.00 USD | 0.00 USD | `+72.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3325` | 787,610.00 USD | 12,290.00 USD | 0.00 USD | `+73.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3335` | 787,720.00 USD | 111.06 USD | 0.00 USD | `+74.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3415` | 787,940.00 USD | 220.61 USD | 0.00 USD | `+78.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3495` | 791,280.00 USD | 3,340.00 USD | 0.00 USD | `+82.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3775` | 791,470.00 USD | 188.75 USD | 0.00 USD | `+97.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3785` | 792,370.00 USD | 909.54 USD | 0.00 USD | `+97.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.3805` | 792,500.00 USD | 121.76 USD | 0.00 USD | `+98.79%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `0.1710` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 29,110.00 USD | 2,020.00 USD | 16,860.00 USD |
| `1D` | `0.1720` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 10,810.00 USD | 837.36 USD | 45,740.00 USD |
| `1D` | `0.1730` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 5,710.00 USD | 7,590.00 USD | 28,880.00 USD |
| `1D` | `0.1740` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 1,100.00 USD | 8,260.00 USD | 567.36 USD |
| `1D` | `0.1750` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 20,870.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.1760` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 63,220.00 USD | 15,120.00 USD | 11,190.00 USD |
| `1D` | `0.1770` | 3,920,000.00 USD | 0.00 USD | 3,920,000.00 USD | 54,620.00 USD | 20,340.00 USD | 79,670.00 USD |
| `1D` | `0.1780` | 3,760,000.00 USD | 0.00 USD | 3,760,000.00 USD | 69,710.00 USD | 35,540.00 USD | 67,000.00 USD |
| `1D` | `0.1790` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 80,130.00 USD | 38,930.00 USD | 46,170.00 USD |
| `7D` | `0.1790` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 30,000.00 USD | 14,510.00 USD | 39,710.00 USD |
| `1D` | `0.1800` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 77,510.00 USD | 26,100.00 USD | 47,570.00 USD |
| `7D` | `0.1800` | 13,120,000.00 USD | 0.00 USD | 13,120,000.00 USD | 0.00 USD | 7,250.00 USD | 26,080.00 USD |
| `1D` | `0.1810` | 3,270,000.00 USD | 0.00 USD | 3,270,000.00 USD | 50,420.00 USD | 27,730.00 USD | 44,490.00 USD |
| `7D` | `0.1810` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 114,070.00 USD | 28,500.00 USD | 32,110.00 USD |
| `1D` | `0.1820` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 159,050.00 USD | 14,270.00 USD | 72,260.00 USD |
| `7D` | `0.1820` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 123,330.00 USD | 51,580.00 USD | 119,260.00 USD |
| `1D` | `0.1830` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 72,410.00 USD | 24,810.00 USD | 133,410.00 USD |
| `7D` | `0.1830` | 12,620,000.00 USD | 0.00 USD | 12,620,000.00 USD | 87,420.00 USD | 37,700.00 USD | 60,460.00 USD |
| `1D` | `0.1840` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 113,190.00 USD | 50,780.00 USD | 145,530.00 USD |
| `7D` | `0.1840` | 12,440,000.00 USD | 0.00 USD | 12,440,000.00 USD | 240,220.00 USD | 58,820.00 USD | 191,110.00 USD |
| `1D` | `0.1850` | 2,370,000.00 USD | 0.00 USD | 2,370,000.00 USD | 110,780.00 USD | 66,490.00 USD | 179,880.00 USD |
| `7D` | `0.1850` | 11,950,000.00 USD | 0.00 USD | 11,950,000.00 USD | 453,420.00 USD | 130,740.00 USD | 423,420.00 USD |
| `1D` | `0.1860` | 2,010,000.00 USD | 0.00 USD | 2,010,000.00 USD | 228,970.00 USD | 8,970.00 USD | 94,110.00 USD |
| `7D` | `0.1860` | 10,940,000.00 USD | 0.00 USD | 10,940,000.00 USD | 118,460.00 USD | 56,980.00 USD | 208,320.00 USD |
| `1D` | `0.1870` | 1,680,000.00 USD | 0.00 USD | 1,680,000.00 USD | 178,050.00 USD | 55,340.00 USD | 277,370.00 USD |
| `7D` | `0.1870` | 10,560,000.00 USD | 0.00 USD | 10,560,000.00 USD | 125,060.00 USD | 37,510.00 USD | 91,240.00 USD |
| `1D` | `0.1880` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 294,230.00 USD | 92,270.00 USD | 246,440.00 USD |
| `7D` | `0.1880` | 10,300,000.00 USD | 0.00 USD | 10,300,000.00 USD | 172,850.00 USD | 44,760.00 USD | 42,250.00 USD |
| `1D` | `0.1890` | 532,270.00 USD | 0.00 USD | 532,270.00 USD | 162,010.00 USD | 135,840.00 USD | 154,170.00 USD |
| `7D` | `0.1890` | 10,040,000.00 USD | 0.00 USD | 10,040,000.00 USD | 251,030.00 USD | 53,780.00 USD | 139,790.00 USD |
| `1D` | `0.1900` | 80,250.00 USD | 0.00 USD | 80,250.00 USD | 0.00 USD | 0.00 USD | 42,920.00 USD |
| `7D` | `0.1900` | 9,600,000.00 USD | 0.00 USD | 9,600,000.00 USD | 252,200.00 USD | 60,410.00 USD | 230,090.00 USD |
| `1D` | `0.1910` | 37,340.00 USD | 0.00 USD | 37,340.00 USD | 37,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1910` | 9,050,000.00 USD | 0.00 USD | 9,050,000.00 USD | 234,100.00 USD | 90,020.00 USD | 9,730.00 USD |
| `1D` | `0.1920` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1920` | 8,720,000.00 USD | 0.00 USD | 8,720,000.00 USD | 269,330.00 USD | 73,760.00 USD | 71,270.00 USD |
| `1D` | `0.1930` | 361,640.00 USD | 361,640.00 USD | 0.00 USD | 361,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.1930` | 8,310,000.00 USD | 0.00 USD | 8,310,000.00 USD | 747,900.00 USD | 171,040.00 USD | 316,090.00 USD |
| `1D` | `0.1940` | 615,120.00 USD | 615,120.00 USD | 0.00 USD | 166,380.00 USD | 5,450.00 USD | 81,660.00 USD |
| `7D` | `0.1940` | 7,070,000.00 USD | 0.00 USD | 7,070,000.00 USD | 762,550.00 USD | 271,400.00 USD | 827,350.00 USD |
| `1D` | `0.1950` | 973,990.00 USD | 973,990.00 USD | 0.00 USD | 96,260.00 USD | 25,730.00 USD | 236,880.00 USD |
| `7D` | `0.1950` | 5,210,000.00 USD | 0.00 USD | 5,210,000.00 USD | 651,390.00 USD | 297,900.00 USD | 391,170.00 USD |
| `1D` | `0.1960` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 77,200.00 USD | 221,440.00 USD | 253,530.00 USD |
| `7D` | `0.1960` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 134,940.00 USD | 9,990.00 USD | 730,170.00 USD |
| `1D` | `0.1970` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 56,610.00 USD | 170,560.00 USD |
| `7D` | `0.1970` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 242,270.00 USD | 136,410.00 USD | 260,640.00 USD |
| `1D` | `0.1980` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 179,990.00 USD | 3,990.00 USD | 79,050.00 USD |
| `7D` | `0.1980` | 2,360,000.00 USD | 0.00 USD | 2,360,000.00 USD | 201,320.00 USD | 46,410.00 USD | 28,250.00 USD |
| `1D` | `0.1990` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 88,240.00 USD | 40,300.00 USD | 185,390.00 USD |
| `7D` | `0.1990` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 48,580.00 USD | 16,090.00 USD | 1,210,000.00 USD |
| `1D` | `0.2000` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 225,870.00 USD | 37,570.00 USD | 297,800.00 USD |
| `7D` | `0.2000` | 800,740.00 USD | 0.00 USD | 800,740.00 USD | 51,800.00 USD | 25,400.00 USD | 112,610.00 USD |
| `1D` | `0.2010` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 112,020.00 USD | 136,420.00 USD | 302,380.00 USD |
| `7D` | `0.2010` | 610,930.00 USD | 0.00 USD | 610,930.00 USD | 252,260.00 USD | 112,400.00 USD | 246,270.00 USD |
| `1D` | `0.2020` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 94,050.00 USD | 29,200.00 USD | 103,450.00 USD |
| `7D` | `0.2020` | 415,850.00 USD | 415,850.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `7D` | `0.2020` | 831,700.00 USD | 831,700.00 USD | 0.00 USD | 0.00 USD | 16,410.00 USD | 399,440.00 USD |
| `1D` | `0.2030` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 76,100.00 USD | 86,660.00 USD | 281,720.00 USD |
| `7D` | `0.2030` | 897,270.00 USD | 897,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 65,570.00 USD |
| `1D` | `0.2040` | 4,490,000.00 USD | 4,490,000.00 USD | 0.00 USD | 43,130.00 USD | 212,450.00 USD | 124,890.00 USD |
| `7D` | `0.2040` | 950,960.00 USD | 950,960.00 USD | 0.00 USD | 0.00 USD | 53,690.00 USD | 0.00 USD |
| `1D` | `0.2050` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 62,210.00 USD | 26,520.00 USD | 33,330.00 USD |
| `1D` | `0.2060` | 4,990,000.00 USD | 4,990,000.00 USD | 0.00 USD | 243,890.00 USD | 31,850.00 USD | 94,760.00 USD |
| `7D` | `0.2060` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 82,670.00 USD | 1,020.00 USD | 11,950.00 USD |
| `1D` | `0.2070` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 375,200.00 USD | 178,420.00 USD | 258,630.00 USD |
| `7D` | `0.2070` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 390,170.00 USD | 96,630.00 USD | 3,030.00 USD |
| `1D` | `0.2080` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 504,370.00 USD | 162,000.00 USD | 30,700.00 USD |
| `7D` | `0.2080` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 592,060.00 USD | 44,630.00 USD | 4,610.00 USD |
| `1D` | `0.2090` | 7,470,000.00 USD | 7,470,000.00 USD | 0.00 USD | 505,530.00 USD | 178,540.00 USD | 285,710.00 USD |
| `7D` | `0.2090` | 5,070,000.00 USD | 5,070,000.00 USD | 0.00 USD | 2,270,000.00 USD | 211,920.00 USD | 403,720.00 USD |
| `1D` | `0.2100` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 666,700.00 USD | 153,810.00 USD | 381,110.00 USD |
| `7D` | `0.2100` | 9,100,000.00 USD | 9,100,000.00 USD | 0.00 USD | 1,730,000.00 USD | 687,470.00 USD | 1,620,000.00 USD |
| `1D` | `0.2110` | 8,950,000.00 USD | 8,950,000.00 USD | 0.00 USD | 142,180.00 USD | 46,780.00 USD | 96,740.00 USD |
| `7D` | `0.2110` | 12,200,000.00 USD | 12,200,000.00 USD | 0.00 USD | 1,060,000.00 USD | 510,780.00 USD | 1,530,000.00 USD |
| `1D` | `0.2120` | 9,380,000.00 USD | 9,380,000.00 USD | 0.00 USD | 194,250.00 USD | 98,370.00 USD | 139,010.00 USD |
| `7D` | `0.2120` | 15,190,000.00 USD | 15,190,000.00 USD | 0.00 USD | 1,160,000.00 USD | 464,320.00 USD | 1,370,000.00 USD |
| `1D` | `0.2130` | 9,740,000.00 USD | 9,740,000.00 USD | 0.00 USD | 210,380.00 USD | 58,850.00 USD | 87,590.00 USD |
| `7D` | `0.2130` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 1,220,000.00 USD | 346,970.00 USD | 1,220,000.00 USD |
| `1D` | `0.2140` | 10,110,000.00 USD | 10,110,000.00 USD | 0.00 USD | 196,360.00 USD | 58,130.00 USD | 110,450.00 USD |
| `7D` | `0.2140` | 20,100,000.00 USD | 20,100,000.00 USD | 0.00 USD | 878,140.00 USD | 392,290.00 USD | 850,440.00 USD |
| `1D` | `0.2150` | 10,150,000.00 USD | 10,150,000.00 USD | 0.00 USD | 31,260.00 USD | 8,690.00 USD | 5,840.00 USD |
| `7D` | `0.2150` | 22,360,000.00 USD | 22,360,000.00 USD | 0.00 USD | 924,080.00 USD | 318,370.00 USD | 1,010,000.00 USD |
| `7D` | `0.2160` | 23,390,000.00 USD | 23,390,000.00 USD | 0.00 USD | 467,380.00 USD | 165,890.00 USD | 397,620.00 USD |
| `7D` | `0.2170` | 24,030,000.00 USD | 24,030,000.00 USD | 0.00 USD | 309,430.00 USD | 96,120.00 USD | 232,930.00 USD |
| `7D` | `0.2180` | 24,540,000.00 USD | 24,540,000.00 USD | 0.00 USD | 271,760.00 USD | 92,360.00 USD | 153,380.00 USD |
| `7D` | `0.2190` | 25,700,000.00 USD | 25,700,000.00 USD | 0.00 USD | 636,690.00 USD | 143,650.00 USD | 379,400.00 USD |
| `7D` | `0.2200` | 26,860,000.00 USD | 26,860,000.00 USD | 0.00 USD | 468,970.00 USD | 215,710.00 USD | 476,240.00 USD |
| `7D` | `0.2210` | 27,910,000.00 USD | 27,910,000.00 USD | 0.00 USD | 540,140.00 USD | 85,690.00 USD | 417,540.00 USD |
| `7D` | `0.2220` | 28,350,000.00 USD | 28,350,000.00 USD | 0.00 USD | 189,800.00 USD | 84,950.00 USD | 172,410.00 USD |
| `7D` | `0.2230` | 28,590,000.00 USD | 28,590,000.00 USD | 0.00 USD | 133,080.00 USD | 46,290.00 USD | 61,370.00 USD |
| `7D` | `0.2240` | 29,330,000.00 USD | 29,330,000.00 USD | 0.00 USD | 378,190.00 USD | 81,770.00 USD | 277,380.00 USD |
| `7D` | `0.2250` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 186,370.00 USD | 100,540.00 USD | 212,920.00 USD |
| `7D` | `0.2260` | 30,830,000.00 USD | 30,830,000.00 USD | 0.00 USD | 436,540.00 USD | 104,680.00 USD | 452,530.00 USD |
| `7D` | `0.2270` | 31,300,000.00 USD | 31,300,000.00 USD | 0.00 USD | 230,310.00 USD | 64,520.00 USD | 175,420.00 USD |
| `7D` | `0.2280` | 31,670,000.00 USD | 31,670,000.00 USD | 0.00 USD | 105,300.00 USD | 58,730.00 USD | 208,320.00 USD |
| `7D` | `0.2290` | 31,870,000.00 USD | 31,870,000.00 USD | 0.00 USD | 74,100.00 USD | 32,530.00 USD | 91,240.00 USD |
| `7D` | `0.2300` | 31,980,000.00 USD | 31,980,000.00 USD | 0.00 USD | 54,070.00 USD | 16,650.00 USD | 39,410.00 USD |
| `7D` | `0.2310` | 31,990,000.00 USD | 31,990,000.00 USD | 0.00 USD | 11,140.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `413.25M` | Total OI Tokens: `2,137,978,811.4 ADA`
  * 1h OI Change: `+1.27%` | 4h OI Change: `+2.63%` | 24h OI Change: `-6.24%`
  * Exchange Breakdown: Binance=`76.61M` | Bybit=`51.15M` | OKX=`29.18M` | Hyperliquid=`28.35M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-351.87` | Last 24h: `10.54K` | Last 3d: `50.95K` | Last 7d: `82.09K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0082%` |
| **USDT Bybit** | `-0.0189%` | **USDT KuCoin** | `0.0055%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0043%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `ADA` | `48.26%` | `51.74%` | `0.93` | 22,500,000.00 USD |
| `15M` | `Binance` | `44.37%` | `55.63%` | `0.80` | 14,870,000.00 USD |
| `15M` | `OKX` | `50.46%` | `49.54%` | `1.02` | 2,200,000.00 USD |
| `15M` | `Bybit` | `58.83%` | `41.17%` | `1.43` | 1,150,000.00 USD |
| `15M` | `KuCoin` | `46.77%` | `53.23%` | `0.88` | 186,710.00 USD |
| `15M` | `Gate` | `49.14%` | `50.86%` | `0.97` | 930,630.00 USD |
| `15M` | `Bitget` | `60.02%` | `39.98%` | `1.50` | 597,210.00 USD |
| `15M` | `BingX` | `37.62%` | `62.38%` | `0.60` | 387,340.00 USD |
| `15M` | `MEXC` | `91.26%` | `8.74%` | `10.44` | 597,170.00 USD |
| `15M` | `Bitunix` | `48.95%` | `51.05%` | `0.96` | 502,300.00 USD |
| `15M` | `Hyperliquid` | `81.33%` | `18.67%` | `4.36` | 551,580.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.69%` | `50.31%` | `0.99` | 55,350.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `20.51%` | `79.49%` | `0.26` | 48,420.00 USD |
| `15M` | `HTX` | `25.54%` | `74.46%` | `0.34` | 95,350.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `44.18%` | `55.82%` | `0.79` | 259,120.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `18.33%` | `81.67%` | `0.22` | 79,860.00 USD |
| `15M` | `Whale Positions` | `44.37%` | `55.63%` | `0.80` | 14,870,000.00 USD |
| `15M` | `Global Accounts` | `48.26%` | `51.74%` | `0.93` | 22,500,000.00 USD |
| `1H` | `ADA` | `51.97%` | `48.03%` | `1.08` | 109,590,000.00 USD |
| `1H` | `Binance` | `50.49%` | `49.51%` | `1.02` | 67,920,000.00 USD |
| `1H` | `OKX` | `52.6%` | `47.4%` | `1.11` | 11,770,000.00 USD |
| `1H` | `Bybit` | `51.48%` | `48.52%` | `1.06` | 8,160,000.00 USD |
| `1H` | `KuCoin` | `53.77%` | `46.23%` | `1.16` | 681,500.00 USD |
| `1H` | `Gate` | `52.07%` | `47.93%` | `1.09` | 3,360,000.00 USD |
| `1H` | `Bitget` | `47.81%` | `52.19%` | `0.92` | 2,450,000.00 USD |
| `1H` | `BingX` | `44.68%` | `55.32%` | `0.81` | 1,850,000.00 USD |
| `1H` | `MEXC` | `68.18%` | `31.82%` | `2.14` | 1,640,000.00 USD |
| `1H` | `Bitunix` | `53.66%` | `46.34%` | `1.16` | 2,830,000.00 USD |
| `1H` | `Hyperliquid` | `74.01%` | `25.99%` | `2.85` | 5,090,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.7%` | `53.3%` | `0.88` | 266,280.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `23.71%` | `76.29%` | `0.31` | 106,420.00 USD |
| `1H` | `HTX` | `26.14%` | `73.86%` | `0.35` | 693,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `100%` | `0.00` | 3,750.00 USD |
| `1H` | `Aster` | `51.88%` | `48.12%` | `1.08` | 1,900,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.05%` | `49.95%` | `1.00` | 840,990.00 USD |
| `1H` | `Whale Positions` | `50.49%` | `49.51%` | `1.02` | 67,920,000.00 USD |
| `1H` | `Global Accounts` | `51.97%` | `48.03%` | `1.08` | 109,590,000.00 USD |
| `4H` | `ADA` | `50.07%` | `49.93%` | `1.00` | 749,180,000.00 USD |
| `4H` | `Binance` | `49.47%` | `50.53%` | `0.98` | 475,520,000.00 USD |
| `4H` | `OKX` | `47.52%` | `52.48%` | `0.91` | 66,410,000.00 USD |
| `4H` | `Bybit` | `55.58%` | `44.42%` | `1.25` | 52,990,000.00 USD |
| `4H` | `KuCoin` | `56.62%` | `43.38%` | `1.31` | 4,330,000.00 USD |
| `4H` | `Gate` | `48.47%` | `51.53%` | `0.94` | 21,290,000.00 USD |
| `4H` | `Bitget` | `50.92%` | `49.08%` | `1.04` | 14,510,000.00 USD |
| `4H` | `BingX` | `39.91%` | `60.09%` | `0.66` | 12,450,000.00 USD |
| `4H` | `MEXC` | `56.48%` | `43.52%` | `1.30` | 8,410,000.00 USD |
| `4H` | `Bitunix` | `52.89%` | `47.11%` | `1.12` | 18,130,000.00 USD |
| `4H` | `Hyperliquid` | `57.39%` | `42.61%` | `1.35` | 39,060,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50%` | `50%` | `1.00` | 3,940,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `28.83%` | `71.17%` | `0.41` | 531,420.00 USD |
| `4H` | `HTX` | `41.98%` | `58.02%` | `0.72` | 2,640,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `67.11%` | `32.89%` | `2.04` | 2,260,000.00 USD |
| `4H` | `Aster` | `51.91%` | `48.09%` | `1.08` | 18,630,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `31.92%` | `68.08%` | `0.47` | 8,090,000.00 USD |
| `4H` | `Whale Positions` | `49.47%` | `50.53%` | `0.98` | 475,520,000.00 USD |
| `4H` | `Global Accounts` | `50.07%` | `49.93%` | `1.00` | 749,180,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.1874` | `0.1870` | `0.1874` | `0.1881` | `0.1859` | 2,036,163.82 USD | 1,133,163.53 USD | 903,000.29 USD | 230,163.23 USD | `+11.30%` | `3B / 0S` |
| `5:00 UTC` | `0.1888` | `0.1889` | `0.1888` | `0.1898` | `0.1880` | 1,960,271.66 USD | 990,186.27 USD | 970,085.39 USD | 20,100.88 USD | `+1.03%` | `3B / 0S` |
| `0:00 UTC` | `0.1899` | `0.1895` | `0.1899` | `0.1900` | `0.1890` | 1,399,205.02 USD | 619,891.71 USD | 779,313.31 USD | -159,421.60 USD | `-11.39%` | `1B / 1S` |
| `5:00 UTC` | `0.1890` | `0.1890` | `0.1890` | `0.1898` | `0.1885` | 1,096,660.36 USD | 485,441.32 USD | 611,219.04 USD | -125,777.71 USD | `-11.47%` | `0B / 2S` |
| `0:00 UTC` | `0.1900` | `0.1898` | `0.1900` | `0.1901` | `0.1890` | 2,242,807.14 USD | 1,164,175.89 USD | 1,078,631.26 USD | 85,544.63 USD | `+3.81%` | `1B / 2S` |
| `5:00 UTC` | `0.1906` | `0.1904` | `0.1906` | `0.1910` | `0.1895` | 1,602,763.76 USD | 810,182.01 USD | 792,581.75 USD | 17,600.26 USD | `+1.10%` | `0B / 0S` |
| `0:00 UTC` | `0.1918` | `0.1914` | `0.1918` | `0.1921` | `0.1903` | 1,967,841.08 USD | 1,071,704.13 USD | 896,136.95 USD | 175,567.18 USD | `+8.92%` | `5B / 1S` |
| `5:00 UTC` | `0.1923` | `0.1922` | `0.1923` | `0.1925` | `0.1918` | 1,542,150.19 USD | 773,488.73 USD | 768,661.46 USD | 4,827.26 USD | `+0.31%` | `0B / 0S` |
| `0:00 UTC` | `0.1915` | `0.1918` | `0.1915` | `0.1925` | `0.1913` | 1,592,969.86 USD | 824,734.22 USD | 768,235.64 USD | 56,498.59 USD | `+3.55%` | `2B / 0S` |
| `5:00 UTC` | `0.1925` | `0.1925` | `0.1925` | `0.1928` | `0.1920` | 1,140,132.73 USD | 563,524.95 USD | 576,607.78 USD | -13,082.84 USD | `-1.15%` | `1B / 1S` |

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
| `5m` | 24,930.00 USD | 292,880.00 USD | **`ACCUMULATION`** |
| `15m` | -56,930.00 USD | -227,560.00 USD | **`DISTRIBUTION`** |
| `30m` | -170,560.00 USD | -319,070.00 USD | **`DISTRIBUTION`** |
| `1h` | -189,940.00 USD | 140,450.00 USD | **`DISTRIBUTION`** |
| `2h` | 48,440.00 USD | 500,400.00 USD | **`ACCUMULATION`** |
| `4h` | 68,830.00 USD | -1,950,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -3,430,000.00 USD | -694,530.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,700,000.00 USD | -11,350,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -8,930,000.00 USD | -13,330,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -8,280,000.00 USD | -7,500,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -21,780,000.00 USD | -40,480,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -79,000,000.00 USD | -198,770,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+24.93K` | 15m=`-56.93K` | 1h=`-189.94K` | 24h=`-8.28M`
* Futures Capital Netflows: 5m=`+292.88K` | 15m=`-227.56K` | 1h=`+140.45K` | 24h=`-7.50M`
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
  * `2026-10-30 09:50:37 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:09:37 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:56:37 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:55:37 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:57:37 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:57:37 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.1859` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-1.02` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.19`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.1925` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.40` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.82`
  * Mathematical Lot Sizing: **`8.31 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.1940`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
