# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:38:27 IST` (`2026-10-30 06:08:27 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.72` | **Live Ask Quote**: `6.75` | **Mid Price**: `6.74`
- **Spread Points**: `28.00` | **Spread BPS**: `41.56 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.55` | VWAP Z-Score: `+1.19` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0808` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `52.78` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `6.98` | Lower -3.00σ Band: `6.13`
  * Upper +2.51σ Band: `6.91` | Lower -2.51σ Band: `6.20`
  * Upper +2.01σ Band: `6.84` | Lower -2.01σ Band: `6.27`
  * Upper +2.00σ Band: `6.83` | Lower -2.00σ Band: `6.27`
  * Upper +1.28σ Band: `6.73` | Lower -1.28σ Band: `6.37`
  * Upper +1.00σ Band: `6.69` | Lower -1.00σ Band: `6.41`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.75` | EMA-20=`6.69` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.74` (Slope: `+0.0000`) | EMA-100=`6.86`
  * Institutional Anchors: EMA-144=`6.91` | EMA-200=`6.95` (Slope: `-0.4012`) | EMA-233=`6.97`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.61` (Distance: `+1.95%`)
  * Point of Control (POC) = `6.46` (Distance: `+4.29%`)
  * Value Area Low (VAL) = `6.25` (Distance: `+7.88%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.25` | Weekly POC=`7.05` | Weekly VAL=`6.91`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.85` | Low=`6.70`
  * New York Session (13:00-21:00 UTC): High=`6.78` | Low=`6.70`
  * Initial Balance (First Hour): IB High=`6.85` | IB Low=`6.72`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.71` - `6.76`
  * Optimal Trade Entry (OTE 0.705): `6.75`
  * Structural Invalidation Anchor (0.786): `6.79`

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
| --- | **`6.74`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:33:47 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `333` | `0x5396...8b79` | `LONG` | 6,766,198.65 USD | `999,999.80` | `6.88` | `6.77` | `5.66` | -114,499.68 USD | `-1.69%` | `5X Cross` |
| `757` | `0x9df2...c665` | `SHORT` | 3,045,150.00 USD | `450,000.00` | `4.49` | `6.77` | `73.58` | -1,024,149.87 USD | `-33.63%` | `10X Cross` |
| `800` | `0xecb6...2b00` | `SHORT` | 2,841,760.67 USD | `419,609.10` | `6.63` | `6.77` | `72.93` | -57,778.21 USD | `-2.03%` | `10X Cross` |
| `818` | `0xbf6d...ecc0` | `LONG` | 2,783,038.29 USD | `411,412.10` | `7.41` | `6.77` | `5.22` | -266,384.71 USD | `-9.57%` | `10X Cross` |
| `853` | `0xcd21...9826` | `LONG` | 2,641,671.76 USD | `390,271.80` | `7.51` | `6.77` | `5.43` | -288,007.67 USD | `-10.90%` | `10X Cross` |
| `985` | `0xdd53...2b13` | `SHORT` | 2,240,766.40 USD | `331,155.90` | `7.28` | `6.77` | `185.59` | 169,839.90 USD | `+7.58%` | `3X Cross` |
| `1075` | `0xb46b...538e` | `SHORT` | 2,029,950.00 USD | `300,000.00` | `8.20` | `6.77` | `21.20` | 429,834.42 USD | `+21.17%` | `10X Cross` |
| `1162` | `0x60a8...85f6` | `SHORT` | 1,908,749.42 USD | `282,067.30` | `6.48` | `6.77` | `65.55` | -80,329.62 USD | `-4.21%` | `10X Cross` |
| `1231` | `0xf21d...3b2d` | `LONG` | 1,796,177.82 USD | `265,479.00` | `4.32` | `6.77` | `4.10` | 649,918.79 USD | `+36.18%` | `10X Isolated` |
| `1332` | `0xf472...5d8b` | `LONG` | 1,633,402.67 USD | `241,374.10` | `4.44` | `6.77` | `0.000000` | 560,759.40 USD | `+34.33%` | `5X Cross` |
| `1452` | `0xb5b3...7a08` | `LONG` | 1,489,532.00 USD | `220,000.00` | `7.36` | `6.77` | `1.78` | -130,678.15 USD | `-8.77%` | `10X Cross` |
| `1507` | `0x265e...7f70` | `LONG` | 1,425,910.50 USD | `210,665.50` | `7.39` | `6.77` | `0.000000` | -131,422.69 USD | `-9.22%` | `3X Cross` |
| `1573` | `0xcac1...26b3` | `SHORT` | 1,355,198.32 USD | `200,336.80` | `7.76` | `6.77` | `49.22` | 198,649.66 USD | `+14.66%` | `10X Cross` |
| `1710` | `0x12d2...f97f` | `LONG` | 1,222,598.61 USD | `180,697.40` | `8.85` | `6.77` | `0.000000` | -377,321.29 USD | `-30.86%` | `10X Cross` |
| `1731` | `0x7cee...fc93` | `SHORT` | 1,188,118.86 USD | `175,532.10` | `6.84` | `6.77` | `21.89` | 12,370.57 USD | `+1.04%` | `5X Cross` |
| `1761` | `0x645b...87b8` | `SHORT` | 1,171,867.84 USD | `173,175.70` | `8.57` | `6.77` | `127.22` | 312,700.26 USD | `+26.68%` | `10X Cross` |
| `1789` | `0x51f6...2b39` | `SHORT` | 1,147,189.39 USD | `169,485.20` | `7.30` | `6.77` | `14.09` | 89,477.82 USD | `+7.80%` | `10X Cross` |
| `1797` | `0xb83d...6e36` | `SHORT` | 1,143,426.76 USD | `168,971.00` | `7.45` | `6.77` | `761.02` | 114,675.47 USD | `+10.03%` | `3X Cross` |
| `1902` | `0x9aa5...58af` | `SHORT` | 1,051,114.39 USD | `155,357.00` | `7.34` | `6.77` | `64.38` | 89,287.34 USD | `+8.49%` | `10X Cross` |
| `1907` | `0xdf95...7d72` | `SHORT` | 1,046,856.62 USD | `154,714.20` | `6.56` | `6.77` | `244.81` | -31,259.15 USD | `-2.99%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`7.58` (Vol: 435,300.00 USD, Dist: `+10.96%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--7.39%`)
  * 48H Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+3.94%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--7.39%`)
  * 3D Horizon: Short MP=`7.10` (Vol: 377,300.00 USD, Dist: `+3.94%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--7.39%`)
  * 7D Horizon: Short MP=`6.89` (Vol: 508,800.00 USD, Dist: `+0.78%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--7.39%`)
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
  * Current Rate: `1.07K` | Last 24h: `53.98K` | Last 3d: `142.71K` | Last 7d: `259.96K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0023%` |
| **USDT Bybit** | `-0.0246%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0023%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `6.73` | `6.73` | `6.73` | `6.77` | `6.70` | 3,192,208.87 USD | 1,465,881.58 USD | 1,726,327.28 USD | -260,445.70 USD | `-8.16%` | `10B / 6S` |
| `0:00 UTC` | `6.70` | `6.70` | `6.70` | `6.74` | `6.67` | 2,713,288.95 USD | 1,145,945.63 USD | 1,567,343.32 USD | -421,397.69 USD | `-15.53%` | `9B / 8S` |
| `5:00 UTC` | `6.74` | `6.74` | `6.74` | `6.77` | `6.71` | 1,866,648.34 USD | 897,232.07 USD | 969,416.26 USD | -72,184.19 USD | `-3.87%` | `6B / 7S` |
| `0:00 UTC` | `6.76` | `6.78` | `6.76` | `6.80` | `6.72` | 4,248,624.28 USD | 2,532,020.86 USD | 1,716,603.42 USD | 815,417.44 USD | `+19.19%` | `23B / 4S` |
| `5:00 UTC` | `6.79` | `6.80` | `6.79` | `6.83` | `6.79` | 5,265,311.00 USD | 2,625,984.82 USD | 2,639,326.18 USD | -13,341.36 USD | `-0.25%` | `7B / 4S` |
| `0:00 UTC` | `6.86` | `6.84` | `6.86` | `6.89` | `6.79` | 3,849,795.58 USD | 2,386,624.38 USD | 1,463,171.20 USD | 923,453.18 USD | `+23.99%` | `22B / 11S` |
| `5:00 UTC` | `6.86` | `6.86` | `6.86` | `6.88` | `6.84` | 2,495,833.60 USD | 958,712.37 USD | 1,537,121.24 USD | -578,408.87 USD | `-23.17%` | `0B / 6S` |
| `0:00 UTC` | `6.83` | `6.83` | `6.83` | `6.86` | `6.81` | 2,040,748.31 USD | 908,116.94 USD | 1,132,631.37 USD | -224,514.43 USD | `-11.00%` | `8B / 6S` |
| `5:00 UTC` | `6.79` | `6.79` | `6.79` | `6.84` | `6.75` | 3,139,376.25 USD | 1,306,141.86 USD | 1,833,234.39 USD | -527,092.53 USD | `-16.79%` | `7B / 28S` |
| `0:00 UTC` | `6.76` | `6.76` | `6.76` | `6.76` | `6.75` | 36,994.80 USD | 23,975.02 USD | 13,019.78 USD | 10,955.24 USD | `+29.61%` | `2B / 1S` |

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
| `5m` | 238,680.00 USD | 36,730.00 USD | **`ACCUMULATION`** |
| `15m` | 106,140.00 USD | -1,010,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 183,770.00 USD | -1,070,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -335,580.00 USD | -663,730.00 USD | **`DISTRIBUTION`** |
| `2h` | 658,740.00 USD | 123,320.00 USD | **`ACCUMULATION`** |
| `4h` | -1,950,000.00 USD | -716,630.00 USD | **`DISTRIBUTION`** |
| `6h` | -4,220,000.00 USD | -4,000,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -6,560,000.00 USD | -30,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -13,970,000.00 USD | -38,800,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -12,570,000.00 USD | -42,990,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -18,870,000.00 USD | -86,320,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -53,440,000.00 USD | -502,950,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+238.68K` | 15m=`+106.14K` | 1h=`-335.58K` | 24h=`-12.57M`
* Futures Capital Netflows: 5m=`+36.73K` | 15m=`-1.01M` | 1h=`-663.73K` | 24h=`-42.99M`
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
  * `2026-10-30 11:03:56 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:28:56 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:27:56 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:29:56 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:29:56 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:29:56 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:29:56 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `6.11` (Risk Distance: `0.1390` pts)
  * +2.5R Take Profit: `6.59`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.61` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.75` (Risk Distance: `0.1390` pts)
  * +2.5R Take Profit: `6.26`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.79`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
