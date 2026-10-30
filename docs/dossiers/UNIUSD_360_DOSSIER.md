# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.87` | **Live Ask Quote**: `6.89` | **Mid Price**: `6.88`
- **Spread Points**: `23.00` | **Spread BPS**: `33.44 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.63` | VWAP Z-Score: `+1.35` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0678` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `58.69` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `7.09` | Lower -3.00σ Band: `6.17`
  * Upper +2.51σ Band: `7.01` | Lower -2.51σ Band: `6.24`
  * Upper +2.01σ Band: `6.94` | Lower -2.01σ Band: `6.32`
  * Upper +2.00σ Band: `6.93` | Lower -2.00σ Band: `6.32`
  * Upper +1.28σ Band: `6.82` | Lower -1.28σ Band: `6.43`
  * Upper +1.00σ Band: `6.78` | Lower -1.00σ Band: `6.47`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.80` | EMA-20=`6.76` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.75` (Slope: `+0.0000`) | EMA-100=`6.82`
  * Institutional Anchors: EMA-144=`6.87` | EMA-200=`6.92` (Slope: `-0.2651`) | EMA-233=`6.92`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.70` (Distance: `+2.67%`)
  * Point of Control (POC) = `6.46` (Distance: `+6.40%`)
  * Value Area Low (VAL) = `6.25` (Distance: `+10.08%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.25` | Weekly POC=`7.05` | Weekly VAL=`6.84`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.94` | Low=`6.64`
  * New York Session (13:00-21:00 UTC): High=`6.94` | Low=`6.72`
  * Initial Balance (First Hour): IB High=`6.85` | IB Low=`6.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.85` - `6.91`
  * Optimal Trade Entry (OTE 0.705): `6.89`
  * Structural Invalidation Anchor (0.786): `6.93`

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
| --- | **`6.88`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `335` | `0x5396...8b79` | `LONG` | 6,871,498.63 USD | `999,999.80` | `6.88` | `6.87` | `5.66` | -9,199.70 USD | `-0.13%` | `5X Cross` |
| `738` | `0x9df2...c665` | `SHORT` | 3,091,545.00 USD | `450,000.00` | `4.49` | `6.87` | `54.04` | -1,070,544.87 USD | `-34.63%` | `10X Cross` |
| `784` | `0xecb6...2b00` | `SHORT` | 2,915,602.84 USD | `424,353.10` | `6.64` | `6.87` | `81.00` | -97,025.62 USD | `-3.33%` | `10X Cross` |
| `805` | `0xbf6d...ecc0` | `LONG` | 2,826,977.10 USD | `411,412.10` | `7.41` | `6.87` | `5.17` | -222,445.90 USD | `-7.87%` | `10X Cross` |
| `838` | `0xcd21...9826` | `LONG` | 2,689,753.25 USD | `390,271.80` | `7.51` | `6.87` | `5.36` | -239,926.19 USD | `-8.92%` | `10X Cross` |
| `972` | `0xdd53...2b13` | `SHORT` | 2,274,075.24 USD | `331,010.50` | `7.28` | `6.87` | `186.20` | 135,472.64 USD | `+5.96%` | `3X Cross` |
| `1042` | `0xb46b...538e` | `SHORT` | 2,061,000.00 USD | `300,000.00` | `8.20` | `6.87` | `20.66` | 398,784.42 USD | `+19.35%` | `10X Cross` |
| `1126` | `0x60a8...85f6` | `SHORT` | 1,937,830.56 USD | `282,067.30` | `6.48` | `6.87` | `80.31` | -109,410.76 USD | `-5.65%` | `10X Cross` |
| `1209` | `0xf21d...3b2d` | `LONG` | 1,824,584.07 USD | `265,479.00` | `4.32` | `6.87` | `4.10` | 678,325.05 USD | `+37.18%` | `10X Isolated` |
| `1298` | `0xf472...5d8b` | `LONG` | 1,662,922.72 USD | `241,374.10` | `4.44` | `6.87` | `0.000000` | 590,279.45 USD | `+35.50%` | `5X Cross` |
| `1426` | `0xb5b3...7a08` | `LONG` | 1,512,038.00 USD | `220,000.00` | `7.36` | `6.87` | `1.81` | -108,172.15 USD | `-7.15%` | `10X Cross` |
| `1478` | `0x265e...7f70` | `LONG` | 1,447,377.32 USD | `210,665.50` | `7.39` | `6.87` | `0.000000` | -109,955.87 USD | `-7.60%` | `3X Cross` |
| `1694` | `0x12d2...f97f` | `LONG` | 1,241,680.25 USD | `180,697.40` | `8.85` | `6.87` | `0.000000` | -358,239.64 USD | `-28.85%` | `10X Cross` |
| `1730` | `0x7cee...fc93` | `SHORT` | 1,206,397.02 USD | `175,532.10` | `6.84` | `6.87` | `22.18` | -5,907.59 USD | `-0.49%` | `5X Cross` |
| `1759` | `0x645b...87b8` | `SHORT` | 1,174,471.96 USD | `170,939.20` | `8.57` | `6.87` | `131.06` | 290,923.49 USD | `+24.77%` | `10X Cross` |
| `1773` | `0x51f6...2b39` | `SHORT` | 1,164,380.27 USD | `169,485.20` | `7.30` | `6.87` | `14.05` | 72,286.94 USD | `+6.21%` | `10X Cross` |
| `1774` | `0xb83d...6e36` | `SHORT` | 1,161,134.92 USD | `168,971.00` | `7.45` | `6.87` | `623.88` | 96,967.31 USD | `+8.35%` | `3X Cross` |
| `1896` | `0xdf95...7d72` | `SHORT` | 1,061,818.96 USD | `154,558.80` | `6.56` | `6.87` | `249.27` | -47,241.59 USD | `-4.45%` | `10X Cross` |
| `1971` | `0xa23d...bf71` | `LONG` | 1,014,444.46 USD | `147,660.80` | `7.66` | `6.87` | `5.62` | -116,230.88 USD | `-11.46%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `6.85` | 1,773.88 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.77K USD at 6.8516 USD [API] | `2026-10-29 20:33:43` |
| `ANNOUNCEMENT` | `INFO` | `6.92` | 1,918.14 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.92K USD at 6.9172 USD [API] | `2026-10-29 20:33:15` |
| `ANNOUNCEMENT` | `INFO` | `6.83` | 1,000.29 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.00K USD at 6.8326 USD [API] | `2026-10-29 20:34:11` |
| `ANNOUNCEMENT` | `INFO` | `6.83` | 11.62 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.01K USD at 6.8326 USD [API] | `2026-10-29 20:34:11` |
| `ANNOUNCEMENT` | `INFO` | `6.83` | 283.55 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.28K USD at 6.8326 USD [API] | `2026-10-29 20:34:11` |
| `ANNOUNCEMENT` | `INFO` | `6.83` | 102.49 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.10K USD at 6.8326 USD [API] | `2026-10-29 20:34:11` |
| `ANNOUNCEMENT` | `INFO` | `6.67` | 1,273.91 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.27K USD at 6.6662 USD [API] | `2026-10-29 20:42:27` |
| `ANNOUNCEMENT` | `INFO` | `6.81` | 1,293.88 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 1.29K USD at 6.8099 USD [API] | `2026-10-29 20:40:55` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+11.78%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.71%`)
  * 48H Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+4.70%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.71%`)
  * 3D Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+4.70%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.71%`)
  * 7D Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+4.70%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.71%`)
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
  * Current Rate: `-694.63` | Last 24h: `48.59K` | Last 3d: `131.97K` | Last 7d: `247.30K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `-0.0331%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0002%` | **USDT Bitget** | `0.0015%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

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
| `0:00 UTC` | `6.73` | `6.73` | `6.73` | `6.76` | `6.69` | 1,774,118.48 USD | 1,147,816.84 USD | 626,301.63 USD | 521,515.21 USD | `+29.40%` | `14B / 3S` |
| `5:00 UTC` | `6.69` | `6.69` | `6.69` | `6.72` | `6.67` | 1,632,526.20 USD | 922,793.61 USD | 709,732.59 USD | 213,061.02 USD | `+13.05%` | `6B / 4S` |
| `0:00 UTC` | `6.73` | `6.72` | `6.73` | `6.75` | `6.69` | 1,221,759.35 USD | 699,787.06 USD | 521,972.29 USD | 177,814.77 USD | `+14.55%` | `18B / 10S` |
| `5:00 UTC` | `6.78` | `6.77` | `6.78` | `6.79` | `6.73` | 2,885,343.54 USD | 1,820,635.09 USD | 1,064,708.45 USD | 755,926.64 USD | `+26.20%` | `19B / 1S` |
| `0:00 UTC` | `6.76` | `6.76` | `6.76` | `6.79` | `6.75` | 1,616,287.97 USD | 938,464.99 USD | 677,822.99 USD | 260,642.00 USD | `+16.13%` | `6B / 0S` |
| `5:00 UTC` | `6.80` | `6.78` | `6.80` | `6.82` | `6.74` | 1,612,258.22 USD | 945,334.77 USD | 666,923.45 USD | 278,411.31 USD | `+17.27%` | `16B / 4S` |
| `0:00 UTC` | `6.80` | `6.80` | `6.80` | `6.81` | `6.78` | 2,508,343.11 USD | 1,546,359.13 USD | 961,983.98 USD | 584,375.15 USD | `+23.30%` | `5B / 1S` |
| `5:00 UTC` | `6.85` | `6.82` | `6.85` | `6.86` | `6.77` | 3,289,721.75 USD | 1,873,877.09 USD | 1,415,844.66 USD | 458,032.42 USD | `+13.92%` | `25B / 6S` |
| `0:00 UTC` | `6.89` | `6.89` | `6.89` | `6.93` | `6.85` | 3,892,782.18 USD | 2,304,895.69 USD | 1,587,886.49 USD | 717,009.20 USD | `+18.42%` | `20B / 2S` |
| `5:00 UTC` | `6.88` | `6.89` | `6.88` | `6.92` | `6.87` | 747,629.34 USD | 269,508.78 USD | 478,120.56 USD | -208,611.78 USD | `-27.90%` | `4B / 17S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:55` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.08` | 0.00 USD | 0.00 USD |
| `10-28 20:19` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.05` | 0.00 USD | 0.00 USD |
| `10-28 19:51` | `Range 0.02` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `6.97` | 22,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Range 0.02` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `6.98` | 41,000.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.01` | 0.00 USD | 0.00 USD |
| `10-28 19:23` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `6.98` | 0.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.02` | 0.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `6.99` | 0.00 USD | 0.00 USD |
| `10-28 19:08` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.04` | 16,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.03` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.00` | 0.00 USD | 0.00 USD |
| `10-28 17:56` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.09` | 36,000.00 USD | 0.00 USD |
| `10-28 17:26` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.12` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.18` | 0.00 USD | 0.00 USD |
| `10-28 16:07` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.15` | 21,000.00 USD | 0.00 USD |
| `10-28 14:32` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.15` | 0.00 USD | 0.00 USD |
| `10-28 13:31` | `Range 0.02` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `7.20` | 0.00 USD | 0.00 USD |
| `10-28 11:45` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `7.18` | 0.00 USD | 0.00 USD |
| `10-28 10:40` | `Range 0.02` | `Divergence` | **`BULLISH`** | Drop without taker selling | `7.17` | 0.00 USD | 0.00 USD |
| `10-28 09:38` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.10` | 0.00 USD | 0.00 USD |
| `10-28 09:19` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.15` | 20,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.16` | 14,000.00 USD | 0.00 USD |
| `10-28 08:57` | `Range 0.02` | `Divergence` | **`BEARISH`** | Rally without taker buying | `7.15` | 0.00 USD | 0.00 USD |
| `10-28 06:23` | `Range 0.02` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `7.10` | 48,000.00 USD | 0.00 USD |
| `10-28 06:23` | `Range 0.02` | `Trapped longs` | **`BEARISH`** | Failed breakout | `7.10` | 48,000.00 USD | 0.00 USD |
| `10-28 06:03` | `Range 0.02` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `7.06` | 21,000.00 USD | 0.00 USD |
| `10-28 05:38` | `Range 0.02` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `7.04` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 154,360.00 USD | -106,690.00 USD | **`ACCUMULATION`** |
| `15m` | 52,870.00 USD | -705,930.00 USD | **`DISTRIBUTION`** |
| `30m` | 408,120.00 USD | -1,120,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 1,240,000.00 USD | 304,050.00 USD | **`ACCUMULATION`** |
| `2h` | 1,310,000.00 USD | 978,690.00 USD | **`ACCUMULATION`** |
| `4h` | 1,920,000.00 USD | 4,440,000.00 USD | **`ACCUMULATION`** |
| `6h` | 2,650,000.00 USD | 3,480,000.00 USD | **`ACCUMULATION`** |
| `8h` | 3,020,000.00 USD | 2,970,000.00 USD | **`ACCUMULATION`** |
| `12h` | -1,900,000.00 USD | 104,200.00 USD | **`DISTRIBUTION`** |
| `24h` | -10,380,000.00 USD | -39,490,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -16,650,000.00 USD | -77,010,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -51,770,000.00 USD | -497,260,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+154.36K` | 15m=`+52.87K` | 1h=`+1.24M` | 24h=`-10.38M`
* Futures Capital Netflows: 5m=`-106.69K` | 15m=`-705.93K` | 1h=`+304.05K` | 24h=`-39.49M`
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
  * `2026-10-30 16:36:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:26:03 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:50:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:48:03 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:47:03 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:49:03 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.25` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.13` (Risk Distance: `0.1159` pts)
  * +2.5R Take Profit: `6.53`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.70` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.81` (Risk Distance: `0.1159` pts)
  * +2.5R Take Profit: `6.41`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.93`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
