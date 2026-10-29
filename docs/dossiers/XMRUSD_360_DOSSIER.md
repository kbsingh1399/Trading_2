# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XMRUSD
**Canonical Key**: `XMRUSD` | **Broker Instrument**: `XMRUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-29 23:07:13 IST` (`2026-10-29 17:37:13 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `603.97` | **Live Ask Quote**: `604.15` | **Mid Price**: `604.06`
- **Spread Points**: `18.00` | **Spread BPS**: `2.98 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `604.06` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.51` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `608.29` | Lower -3.00σ Band: `599.83`
  * Upper +2.51σ Band: `607.38` | Lower -2.51σ Band: `600.74`
  * Upper +2.01σ Band: `606.60` | Lower -2.01σ Band: `601.52`
  * Upper +2.00σ Band: `606.48` | Lower -2.00σ Band: `601.64`
  * Upper +1.28σ Band: `605.75` | Lower -1.28σ Band: `602.37`
  * Upper +1.00σ Band: `605.27` | Lower -1.00σ Band: `602.85`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`604.06` | EMA-20=`604.06` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`604.06` (Slope: `+0.0000`) | EMA-100=`604.06`
  * Institutional Anchors: EMA-144=`604.06` | EMA-200=`604.06` (Slope: `+0.0000`) | EMA-233=`604.06`
- **Range Boundaries**: 24H High=`610.10` | 24H Low=`598.02` | Weekly High=`616.14` | Weekly Low=`591.98`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `606.82` (Distance: `-0.46%`)
  * Point of Control (POC) = `599.28` (Distance: `+0.79%`)
  * Value Area Low (VAL) = `592.19` (Distance: `+2.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`609.02` | POC=`603.23` | VAL=`598.35`
  * Prior Day Extremes: PDH=`619.59` | PDL=`592.48` | PDC=`598.93`
  * Monday Range Blueprint: High=`602.04` | Mid=`592.51` | Low=`582.99`
  * Developing Weekly Value Area: Weekly VAH=`604.10` | Weekly POC=`594.58` | Weekly VAL=`589.70`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`609.29` | Low=`583.39`
  * London Session (08:00-16:00 UTC): High=`603.20` | Low=`588.63`
  * New York Session (13:00-21:00 UTC): High=`617.68` | Low=`596.96`
  * Initial Balance (First Hour): IB High=`592.17` | IB Low=`588.63`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `601.64` - `606.48`
  * Optimal Trade Entry (OTE 0.705): `605.27`
  * Structural Invalidation Anchor (0.786): `608.89`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 23:06:38 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `73` | `0xc179...e0c8` | `LONG` | 23,414,804.11 USD | `38,637,398,000.00` | `602.06` | `607.77` | `433.49` | 152,905.36 USD | `+0.65%` | `5X Cross` |
| `135` | `0xefe4...194b` | `LONG` | 15,227,446.38 USD | `25,045,554,000.00` | `598.97` | `607.77` | `0.000000` | 225,823.21 USD | `+1.48%` | `5X Cross` |
| `224` | `0x7fda...17d1` | `SHORT` | 10,224,503.99 USD | `16,816,895,000.00` | `602.92` | `607.77` | `2748.09` | -85,188.10 USD | `-0.83%` | `5X Cross` |
| `395` | `0x880a...311c` | `SHORT` | 6,093,490.83 USD | `10,023,178,000.00` | `596.67` | `607.77` | `1306.04` | -112,944.87 USD | `-1.85%` | `5X Cross` |
| `671` | `0x645b...87b8` | `SHORT` | 3,544,104.31 USD | `5,851,157,000.00` | `603.14` | `607.77` | `3615.79` | -15,033.25 USD | `-0.42%` | `5X Cross` |
| `745` | `0x07fd...689d` | `LONG` | 3,189,810.34 USD | `5,247,089,000.00` | `568.41` | `607.77` | `0.000000` | 207,288.89 USD | `+6.50%` | `5X Cross` |
| `807` | `0x5f2e...9e2d` | `SHORT` | 2,957,062.70 USD | `4,864,230,000.00` | `604.34` | `607.77` | `1298.69` | -17,425.11 USD | `-0.59%` | `5X Cross` |
| `856` | `0x5ad9...f5ef` | `SHORT` | 2,764,611.26 USD | `4,564,249,000.00` | `601.70` | `607.77` | `996.38` | -18,280.33 USD | `-0.66%` | `2X Cross` |
| `1128` | `0x26b6...9a13` | `LONG` | 2,023,110.62 USD | `3,332,143,000.00` | `604.79` | `607.77` | `0.000000` | 7,870.46 USD | `+0.39%` | `5X Cross` |
| `1211` | `0xe4a6...bd55` | `LONG` | 1,900,756.85 USD | `3,136,490,000.00` | `579.90` | `607.77` | `541.65` | 81,895.85 USD | `+4.31%` | `5X Cross` |
| `1263` | `0x8b1d...ae3c` | `LONG` | 1,825,404.16 USD | `3,002,507,000.00` | `609.91` | `607.77` | `497.42` | -5,858.65 USD | `-0.32%` | `4X Isolated` |
| `1296` | `0x4c6d...5ee9` | `SHORT` | 1,780,563.64 USD | `2,928,944,000.00` | `608.78` | `607.77` | `843.63` | 2,522.72 USD | `+0.14%` | `3X Cross` |
| `1340` | `0x27c9...d65d` | `SHORT` | 1,710,619.31 USD | `2,813,750,000.00` | `603.43` | `607.77` | `1066.21` | -12,716.46 USD | `-0.74%` | `5X Cross` |
| `1390` | `0x5b5d...c060` | `SHORT` | 1,644,565.53 USD | `2,704,922,000.00` | `599.40` | `607.77` | `53861.23` | -23,220.97 USD | `-1.41%` | `3X Cross` |
| `1392` | `0xf946...aebd` | `SHORT` | 1,641,438.00 USD | `2,700,000,000.00` | `510.68` | `607.77` | `705.20` | -262,600.03 USD | `-16.00%` | `5X Cross` |
| `1514` | `0xac48...3201` | `LONG` | 1,513,639.86 USD | `2,489,744,000.00` | `607.33` | `607.77` | `0.000000` | 1,551.91 USD | `+0.10%` | `5X Cross` |
| `1554` | `0x0274...a7f7` | `SHORT` | 1,461,872.59 USD | `2,404,633,000.00` | `528.54` | `607.77` | `831.69` | -190,928.89 USD | `-13.06%` | `2X Cross` |
| `1698` | `0x258a...ff03` | `SHORT` | 1,312,481.67 USD | `2,158,900,000.00` | `601.17` | `607.77` | `2381.38` | -14,604.91 USD | `-1.11%` | `5X Cross` |
| `1791` | `0x3dc9...54b0` | `SHORT` | 1,215,900.00 USD | `2,000,000,000.00` | `505.19` | `607.77` | `6961.35` | -205,521.55 USD | `-16.90%` | `5X Cross` |
| `1828` | `0xd2b2...11ed` | `SHORT` | 1,181,893.76 USD | `1,951,898,000.00` | `554.70` | `607.77` | `3417.74` | -99,166.55 USD | `-8.39%` | `5X Cross` |
| `1851` | `0x1bf6...5bfa` | `SHORT` | 1,162,886.40 USD | `1,920,000,000.00` | `566.73` | `607.77` | `1550.66` | -74,771.57 USD | `-6.43%` | `5X Cross` |
| `1866` | `0xdc51...6ef7` | `LONG` | 1,150,934.19 USD | `1,893,015,000.00` | `600.22` | `607.77` | `0.000000` | 14,700.37 USD | `+1.28%` | `5X Cross` |
| `1982` | `0x833b...db06` | `SHORT` | 1,052,876.53 USD | `1,738,826,000.00` | `551.44` | `607.77` | `1194.36` | -94,024.01 USD | `-8.93%` | `5X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`621.86` (Vol: 130,800.00 USD, Dist: `+2.32%`) | Long MP=`600.84` (Vol: 149,600.00 USD, Dist: `--1.14%`)
  * 48H Horizon: Short MP=`628.09` (Vol: 159,900.00 USD, Dist: `+3.34%`) | Long MP=`600.74` (Vol: 149,600.00 USD, Dist: `--1.16%`)
  * 3D Horizon: Short MP=`622.07` (Vol: 180,600.00 USD, Dist: `+2.35%`) | Long MP=`582.68` (Vol: 236,900.00 USD, Dist: `--4.13%`)
  * 7D Horizon: Short MP=`622.81` (Vol: 400,200.00 USD, Dist: `+2.47%`) | Long MP=`582.51` (Vol: 341,500.00 USD, Dist: `--4.16%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Matrix | Interbank Flow | - | - | - | - | - | - | Interbank Tier |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Map | Near Money | - | - | - | - | 0.00% | - |

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
  * Current Rate: `25.38K` | Last 24h: `45.46K` | Last 3d: `120.00K` | Last 7d: `265.01K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0133%` | **USDT OKX** | `-` |
| **USDT Bybit** | `0.0405%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0130%` | **USDT BingX** | `0.0422%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0189%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

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
| 15m Bar | Interbank Tick Flow | - | - | - | - | - | - | - | - | 0.00% | Balanced Interbank Imbalance |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Live | 15m | Tape Flow | NEUTRAL | Orderflow balanced at current level | - | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 62,740.00 USD | 850,860.00 USD | **`ACCUMULATION`** |
| `15m` | -16,320.00 USD | -238,200.00 USD | **`DISTRIBUTION`** |
| `30m` | 31,410.00 USD | -1,280,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 181,460.00 USD | -975,070.00 USD | **`DISTRIBUTION`** |
| `2h` | 528,180.00 USD | -852,160.00 USD | **`DISTRIBUTION`** |
| `4h` | 884,150.00 USD | -490,360.00 USD | **`ACCUMULATION`** |
| `6h` | 1,350,000.00 USD | 228,060.00 USD | **`ACCUMULATION`** |
| `8h` | 1,890,000.00 USD | 35,650.00 USD | **`ACCUMULATION`** |
| `12h` | 2,580,000.00 USD | -462,700.00 USD | **`ACCUMULATION`** |
| `24h` | 4,540,000.00 USD | -2,610,000.00 USD | **`ACCUMULATION`** |
| `1w` | 13,850,000.00 USD | -635,960.00 USD | **`ACCUMULATION`** |
| `30d` | 31,450,000.00 USD | -14,090,000.00 USD | **`ACCUMULATION`** |

* Spot Capital Netflows: 5m=`+62.74K` | 15m=`-16.32K` | 1h=`+181.46K` | 24h=`+4.54M`
* Futures Capital Netflows: 5m=`+850.86K` | 15m=`-238.20K` | 1h=`-975.07K` | 24h=`-2.61M`
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
  * Execution Entry: `592.19` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `590.11` (Risk Distance: `2.08` pts)
  * +2.5R Take Profit: `597.40`
  * Mathematical Lot Sizing: **`4.80 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `606.82` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `608.90` (Risk Distance: `2.08` pts)
  * +2.5R Take Profit: `601.61`
  * Mathematical Lot Sizing: **`4.80 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`608.89`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
