# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 11:14:11 IST` (`2026-10-30 05:44:11 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.80` | **Live Ask Quote**: `6.83` | **Mid Price**: `6.82`
- **Spread Points**: `25.00` | **Spread BPS**: `36.68 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.54` | VWAP Z-Score: `+2.01` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.0836` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `62.81` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `6.95` | Lower -3.00σ Band: `6.14`
  * Upper +2.51σ Band: `6.88` | Lower -2.51σ Band: `6.20`
  * Upper +2.01σ Band: `6.82` | Lower -2.01σ Band: `6.27`
  * Upper +2.00σ Band: `6.82` | Lower -2.00σ Band: `6.27`
  * Upper +1.28σ Band: `6.72` | Lower -1.28σ Band: `6.37`
  * Upper +1.00σ Band: `6.68` | Lower -1.00σ Band: `6.41`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.74` | EMA-20=`6.68` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.74` (Slope: `+0.0000`) | EMA-100=`6.86`
  * Institutional Anchors: EMA-144=`6.92` | EMA-200=`6.96` (Slope: `-0.4489`) | EMA-233=`6.97`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.60` (Distance: `+3.19%`)
  * Point of Control (POC) = `6.46` (Distance: `+5.43%`)
  * Value Area Low (VAL) = `6.25` (Distance: `+9.05%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.25` | Weekly POC=`7.05` | Weekly VAL=`6.91`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.85` | Low=`6.76`
  * New York Session (13:00-21:00 UTC): High=`6.86` | Low=`6.78`
  * Initial Balance (First Hour): IB High=`6.85` | IB Low=`6.76`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.79` - `6.84`
  * Optimal Trade Entry (OTE 0.705): `6.83`
  * Structural Invalidation Anchor (0.786): `6.87`

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
| --- | **`6.82`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:13:49 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `331` | `0x5396...8b79` | `LONG` | 6,831,798.63 USD | `999,999.80` | `6.88` | `6.84` | `5.66` | -48,899.69 USD | `-0.72%` | `5X Cross` |
| `747` | `0x9df2...c665` | `SHORT` | 3,074,715.00 USD | `450,000.00` | `4.49` | `6.84` | `72.60` | -1,053,714.87 USD | `-34.27%` | `10X Cross` |
| `809` | `0xecb6...2b00` | `SHORT` | 2,822,182.03 USD | `412,895.50` | `6.63` | `6.84` | `77.00` | -83,976.65 USD | `-2.98%` | `10X Cross` |
| `814` | `0xbf6d...ecc0` | `LONG` | 2,810,796.27 USD | `411,412.10` | `7.41` | `6.84` | `5.23` | -238,626.73 USD | `-8.49%` | `10X Cross` |
| `854` | `0xcd21...9826` | `LONG` | 2,667,351.64 USD | `390,271.80` | `7.51` | `6.84` | `5.43` | -262,327.79 USD | `-9.83%` | `10X Cross` |
| `985` | `0xdd53...2b13` | `SHORT` | 2,262,480.29 USD | `331,155.90` | `7.28` | `6.84` | `184.16` | 148,126.01 USD | `+6.55%` | `3X Cross` |
| `1070` | `0xb46b...538e` | `SHORT` | 2,049,990.00 USD | `300,000.00` | `8.20` | `6.84` | `20.85` | 409,794.42 USD | `+19.99%` | `10X Cross` |
| `1155` | `0x60a8...85f6` | `SHORT` | 1,927,281.24 USD | `282,067.30` | `6.48` | `6.84` | `65.24` | -98,861.45 USD | `-5.13%` | `10X Cross` |
| `1217` | `0xf21d...3b2d` | `LONG` | 1,814,548.97 USD | `265,479.00` | `4.32` | `6.84` | `4.10` | 668,289.94 USD | `+36.83%` | `10X Isolated` |
| `1319` | `0xf472...5d8b` | `LONG` | 1,649,309.23 USD | `241,374.10` | `4.44` | `6.84` | `0.000000` | 576,665.95 USD | `+34.96%` | `5X Cross` |
| `1451` | `0xb5b3...7a08` | `LONG` | 1,504,712.00 USD | `220,000.00` | `7.36` | `6.84` | `1.75` | -115,498.15 USD | `-7.68%` | `10X Cross` |
| `1510` | `0x265e...7f70` | `LONG` | 1,439,919.76 USD | `210,665.50` | `7.39` | `6.84` | `0.000000` | -117,413.43 USD | `-8.15%` | `3X Cross` |
| `1570` | `0xcac1...26b3` | `SHORT` | 1,368,715.04 USD | `200,336.80` | `7.76` | `6.84` | `48.71` | 185,132.93 USD | `+13.53%` | `10X Cross` |
| `1707` | `0x12d2...f97f` | `LONG` | 1,234,578.85 USD | `180,697.40` | `8.85` | `6.84` | `0.000000` | -365,341.05 USD | `-29.59%` | `10X Cross` |
| `1722` | `0x7cee...fc93` | `SHORT` | 1,215,161.16 USD | `177,785.10` | `6.84` | `6.84` | `21.39` | 736.87 USD | `+0.06%` | `5X Cross` |
| `1744` | `0x645b...87b8` | `SHORT` | 1,184,684.14 USD | `173,323.60` | `8.57` | `6.84` | `125.43` | 301,151.85 USD | `+25.42%` | `10X Cross` |
| `1791` | `0x9aa5...58af` | `SHORT` | 1,158,611.79 USD | `169,591.00` | `7.34` | `6.84` | `59.16` | 86,274.95 USD | `+7.45%` | `10X Cross` |
| `1792` | `0x51f6...2b39` | `SHORT` | 1,158,143.22 USD | `169,485.20` | `7.30` | `6.84` | `14.05` | 78,523.99 USD | `+6.78%` | `10X Cross` |
| `1797` | `0xb83d...6e36` | `SHORT` | 1,154,528.15 USD | `168,971.00` | `7.45` | `6.84` | `748.68` | 103,574.08 USD | `+8.97%` | `3X Cross` |
| `1911` | `0xdf95...7d72` | `SHORT` | 1,057,780.99 USD | `154,714.20` | `6.56` | `6.84` | `242.46` | -42,183.52 USD | `-3.99%` | `10X Cross` |
| `2004` | `0xa23d...bf71` | `LONG` | 1,008,833.35 USD | `147,660.80` | `7.66` | `6.84` | `5.62` | -121,841.99 USD | `-12.08%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `6.97` | 162.41 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Short: 0.16K USD at 6.9705 USD [API] | `2026-10-29 02:30:52` |


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
  * Current Rate: `-25.26` | Last 24h: `53.98K` | Last 3d: `142.71K` | Last 7d: `259.96K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0018%` |
| **USDT Bybit** | `-0.0262%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0006%` | **USDT Bitget** | `0.0100%` |
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
| `5:00 UTC` | `6.66` | `6.65` | `6.66` | `6.68` | `6.62` | 2,098,352.85 USD | 1,088,207.05 USD | 1,010,145.80 USD | 78,061.25 USD | `+3.72%` | `7B / 6S` |
| `0:00 UTC` | `6.70` | `6.70` | `6.70` | `6.74` | `6.67` | 2,696,324.51 USD | 1,506,489.83 USD | 1,189,834.69 USD | 316,655.14 USD | `+11.74%` | `14B / 8S` |
| `5:00 UTC` | `6.73` | `6.73` | `6.73` | `6.77` | `6.70` | 3,192,208.87 USD | 1,465,881.58 USD | 1,726,327.28 USD | -260,445.70 USD | `-8.16%` | `10B / 6S` |
| `0:00 UTC` | `6.70` | `6.70` | `6.70` | `6.74` | `6.67` | 2,713,288.95 USD | 1,145,945.63 USD | 1,567,343.32 USD | -421,397.69 USD | `-15.53%` | `9B / 8S` |
| `5:00 UTC` | `6.74` | `6.74` | `6.74` | `6.77` | `6.71` | 1,866,648.34 USD | 897,232.07 USD | 969,416.26 USD | -72,184.19 USD | `-3.87%` | `6B / 7S` |
| `0:00 UTC` | `6.76` | `6.78` | `6.76` | `6.80` | `6.72` | 4,248,624.28 USD | 2,532,020.86 USD | 1,716,603.42 USD | 815,417.44 USD | `+19.19%` | `23B / 4S` |
| `5:00 UTC` | `6.79` | `6.80` | `6.79` | `6.83` | `6.79` | 5,265,311.00 USD | 2,625,984.82 USD | 2,639,326.18 USD | -13,341.36 USD | `-0.25%` | `7B / 4S` |
| `0:00 UTC` | `6.86` | `6.84` | `6.86` | `6.89` | `6.79` | 3,849,795.58 USD | 2,386,624.38 USD | 1,463,171.20 USD | 923,453.18 USD | `+23.99%` | `22B / 11S` |
| `5:00 UTC` | `6.86` | `6.86` | `6.86` | `6.88` | `6.84` | 2,495,833.60 USD | 958,712.37 USD | 1,537,121.24 USD | -578,408.87 USD | `-23.17%` | `0B / 6S` |
| `0:00 UTC` | `6.83` | `6.83` | `6.83` | `6.86` | `6.81` | 1,552,283.42 USD | 646,830.23 USD | 905,453.19 USD | -258,622.96 USD | `-16.66%` | `7B / 10S` |

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
| `5m` | 0.00 USD | -268,800.00 USD | **`DISTRIBUTION`** |
| `15m` | 0.00 USD | -771,320.00 USD | **`DISTRIBUTION`** |
| `30m` | 0.00 USD | 414,860.00 USD | **`ACCUMULATION`** |
| `1h` | 0.00 USD | 1,290,000.00 USD | **`ACCUMULATION`** |
| `2h` | 0.00 USD | 622,470.00 USD | **`ACCUMULATION`** |
| `4h` | 0.00 USD | 883,810.00 USD | **`ACCUMULATION`** |
| `6h` | 0.00 USD | -5,230,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 0.00 USD | -36,570,000.00 USD | **`DISTRIBUTION`** |
| `12h` | 0.00 USD | -38,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 0.00 USD | -43,090,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 0.00 USD | -86,070,000.00 USD | **`DISTRIBUTION`** |
| `30d` | 0.00 USD | -503,140,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-268.80K` | 15m=`-771.32K` | 1h=`+1.29M` | 24h=`-43.09M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:09:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:10:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:08:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:10:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:10:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:10:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `6.11` (Risk Distance: `0.1379` pts)
  * +2.5R Take Profit: `6.59`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.60` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.74` (Risk Distance: `0.1379` pts)
  * +2.5R Take Profit: `6.26`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.87`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
