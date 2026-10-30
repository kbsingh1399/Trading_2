# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 08:09:34 IST` (`2026-10-30 02:39:34 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.53` | **Live Ask Quote**: `6.55` | **Mid Price**: `6.54`
- **Spread Points**: `29.00` | **Spread BPS**: `44.35 bps` (Charter Threshold: `12.00 bps`)
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
  * Session VWAP: `6.44` | VWAP Z-Score: `+1.45` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.1262` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `44.57` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `6.63` | Lower -3.00σ Band: `6.24`
  * Upper +2.51σ Band: `6.60` | Lower -2.51σ Band: `6.27`
  * Upper +2.01σ Band: `6.57` | Lower -2.01σ Band: `6.30`
  * Upper +2.00σ Band: `6.57` | Lower -2.00σ Band: `6.31`
  * Upper +1.28σ Band: `6.52` | Lower -1.28σ Band: `6.35`
  * Upper +1.00σ Band: `6.50` | Lower -1.00σ Band: `6.37`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.49` | EMA-20=`6.55` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.77` (Slope: `+0.0000`) | EMA-100=`6.91`
  * Institutional Anchors: EMA-144=`6.96` | EMA-200=`6.99` (Slope: `-0.9719`) | EMA-233=`7.01`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.53` (Distance: `+0.37%`)
  * Point of Control (POC) = `6.46` (Distance: `+1.48%`)
  * Value Area Low (VAL) = `6.35` (Distance: `+3.27%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.22` | Weekly POC=`7.05` | Weekly VAL=`6.91`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.57` | Low=`6.51`
  * New York Session (13:00-21:00 UTC): High=`6.58` | Low=`6.50`
  * Initial Balance (First Hour): IB High=`6.56` | IB Low=`6.52`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.51` - `6.57`
  * Optimal Trade Entry (OTE 0.705): `6.55`
  * Structural Invalidation Anchor (0.786): `6.59`

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 07:57:16 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `335` | `0x5396...8b79` | `LONG` | 6,677,098.66 USD | `999,999.80` | `6.88` | `6.68` | `5.66` | -203,599.66 USD | `-3.05%` | `5X Cross` |
| `752` | `0x9df2...c665` | `SHORT` | 3,004,155.00 USD | `450,000.00` | `4.49` | `6.68` | `76.31` | -983,154.87 USD | `-32.73%` | `10X Cross` |
| `817` | `0xecb6...2b00` | `SHORT` | 2,746,759.18 USD | `411,690.70` | `6.63` | `6.68` | `74.09` | -16,981.56 USD | `-0.62%` | `10X Cross` |
| `831` | `0xbf6d...ecc0` | `LONG` | 2,697,963.51 USD | `404,134.80` | `7.42` | `6.68` | `5.13` | -301,460.07 USD | `-11.17%` | `10X Cross` |
| `879` | `0xcd21...9826` | `LONG` | 2,554,701.17 USD | `382,990.70` | `7.52` | `6.68` | `5.33` | -324,978.95 USD | `-12.72%` | `10X Cross` |
| `989` | `0xdd53...2b13` | `SHORT` | 2,210,763.67 USD | `331,155.90` | `7.28` | `6.68` | `195.57` | 199,842.63 USD | `+9.04%` | `3X Cross` |
| `1004` | `0x60a8...85f6` | `SHORT` | 2,173,911.85 USD | `325,831.00` | `6.48` | `6.68` | `58.31` | -61,806.51 USD | `-2.84%` | `10X Cross` |
| `1085` | `0xb46b...538e` | `SHORT` | 1,996,290.00 USD | `300,000.00` | `8.20` | `6.68` | `22.00` | 463,494.42 USD | `+23.22%` | `10X Cross` |
| `1236` | `0xf21d...3b2d` | `LONG` | 1,770,824.57 USD | `265,479.00` | `4.32` | `6.68` | `4.10` | 624,565.55 USD | `+35.27%` | `10X Isolated` |
| `1327` | `0xf472...5d8b` | `LONG` | 1,611,244.53 USD | `241,374.10` | `4.44` | `6.68` | `0.000000` | 538,601.25 USD | `+33.43%` | `5X Cross` |
| `1462` | `0xb5b3...7a08` | `LONG` | 1,467,268.00 USD | `220,000.00` | `7.36` | `6.68` | `1.78` | -152,942.15 USD | `-10.42%` | `10X Cross` |
| `1523` | `0x265e...7f70` | `LONG` | 1,406,255.41 USD | `210,665.50` | `7.39` | `6.68` | `0.000000` | -151,077.78 USD | `-10.74%` | `3X Cross` |
| `1578` | `0xcac1...26b3` | `SHORT` | 1,335,405.04 USD | `200,336.80` | `7.76` | `6.68` | `50.63` | 218,442.93 USD | `+16.36%` | `10X Cross` |
| `1611` | `0x9aa5...58af` | `SHORT` | 1,301,352.05 USD | `195,041.80` | `7.34` | `6.68` | `54.02` | 130,356.89 USD | `+10.02%` | `10X Cross` |
| `1710` | `0x12d2...f97f` | `LONG` | 1,205,143.24 USD | `180,697.40` | `8.85` | `6.68` | `0.000000` | -394,776.66 USD | `-32.76%` | `10X Cross` |
| `1714` | `0x7cee...fc93` | `SHORT` | 1,201,293.61 USD | `180,052.70` | `6.84` | `6.68` | `22.03` | 30,227.95 USD | `+2.52%` | `5X Cross` |
| `1756` | `0x645b...87b8` | `SHORT` | 1,158,002.40 USD | `173,519.90` | `8.57` | `6.68` | `132.13` | 329,516.39 USD | `+28.46%` | `10X Cross` |
| `1796` | `0x51f6...2b39` | `SHORT` | 1,130,788.31 USD | `169,485.20` | `7.30` | `6.68` | `14.17` | 105,878.90 USD | `+9.36%` | `10X Cross` |
| `1812` | `0xb83d...6e36` | `SHORT` | 1,122,322.28 USD | `168,971.00` | `7.45` | `6.68` | `813.57` | 135,779.95 USD | `+12.10%` | `3X Cross` |
| `1912` | `0xdf95...7d72` | `SHORT` | 1,032,237.67 USD | `154,714.20` | `6.56` | `6.68` | `253.83` | -16,640.21 USD | `-1.61%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 48H Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 3D Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
  * 7D Horizon: Short MP=`6.67` (Vol: 1,200,000.00 USD, Dist: `+3.30%`) | Long MP=`6.17` (Vol: 812,600.00 USD, Dist: `--4.44%`)
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
  * Current Rate: `26.94K` | Last 24h: `53.94K` | Last 3d: `142.67K` | Last 7d: `259.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0090%` |
| **USDT Bybit** | `0.0063%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `6.46` | `6.46` | `6.46` | `6.50` | `6.43` | 7,714,315.60 USD | 3,882,377.81 USD | 3,831,937.79 USD | 50,440.02 USD | `+0.65%` | `1B / 1S` |
| `5:00 UTC` | `6.33` | `6.37` | `6.33` | `6.51` | `6.25` | 21,731,536.36 USD | 9,271,035.82 USD | 12,460,500.54 USD | -3,189,464.71 USD | `-14.68%` | `3B / 10S` |
| `0:00 UTC` | `6.42` | `6.36` | `6.42` | `6.44` | `6.26` | 10,203,831.59 USD | 4,743,342.97 USD | 5,460,488.62 USD | -717,145.66 USD | `-7.03%` | `6B / 14S` |
| `5:00 UTC` | `6.49` | `6.47` | `6.49` | `6.52` | `6.39` | 10,332,566.01 USD | 6,083,569.00 USD | 4,248,997.01 USD | 1,834,571.99 USD | `+17.76%` | `31B / 4S` |
| `0:00 UTC` | `6.52` | `6.48` | `6.52` | `6.55` | `6.41` | 7,350,422.21 USD | 3,756,137.60 USD | 3,594,284.62 USD | 161,852.98 USD | `+2.20%` | `10B / 21S` |
| `5:00 UTC` | `6.50` | `6.52` | `6.50` | `6.56` | `6.48` | 5,770,145.58 USD | 2,140,624.21 USD | 3,629,521.37 USD | -1,488,897.17 USD | `-25.80%` | `4B / 15S` |
| `0:00 UTC` | `6.55` | `6.52` | `6.55` | `6.58` | `6.44` | 5,592,794.96 USD | 2,688,660.61 USD | 2,904,134.35 USD | -215,473.74 USD | `-3.85%` | `7B / 23S` |
| `5:00 UTC` | `6.51` | `6.51` | `6.51` | `6.56` | `6.45` | 8,801,980.78 USD | 4,357,443.96 USD | 4,444,536.83 USD | -87,092.87 USD | `-0.99%` | `8B / 5S` |
| `0:00 UTC` | `6.53` | `6.54` | `6.53` | `6.61` | `6.48` | 5,801,726.86 USD | 2,983,022.82 USD | 2,818,704.04 USD | 164,318.78 USD | `+2.83%` | `13B / 18S` |
| `5:00 UTC` | `6.64` | `6.63` | `6.64` | `6.65` | `6.60` | 6,121,109.14 USD | 3,441,260.14 USD | 2,679,849.00 USD | 761,411.15 USD | `+12.44%` | `3B / 5S` |

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
| `5m` | -172,630.00 USD | 417,440.00 USD | **`ACCUMULATION`** |
| `15m` | -289,880.00 USD | 662,910.00 USD | **`ACCUMULATION`** |
| `30m` | -778,550.00 USD | 231,740.00 USD | **`DISTRIBUTION`** |
| `1h` | -716,280.00 USD | 299,750.00 USD | **`DISTRIBUTION`** |
| `2h` | -2,090,000.00 USD | 1,320,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,000,000.00 USD | -10,840,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -11,000,000.00 USD | -37,180,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -12,330,000.00 USD | -38,990,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -11,260,000.00 USD | -36,990,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -11,400,000.00 USD | -45,150,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -17,540,000.00 USD | -87,620,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -53,080,000.00 USD | -504,900,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-172.63K` | 15m=`-289.88K` | 1h=`-716.28K` | 24h=`-11.40M`
* Futures Capital Netflows: 5m=`+417.44K` | 15m=`+662.91K` | 1h=`+299.75K` | 24h=`-45.15M`
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
  * `2026-10-30 07:16:25 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:52:25 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 07:51:25 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:53:25 IST`: [economics.td.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [investinglive.com] - (Sentiment: `Neutral`)
  * `2026-10-30 03:53:25 IST`: [msn.com] - (Sentiment: `Neutral`)
  * `2026-10-30 02:53:25 IST`: [morningstar.com] - (Sentiment: `Neutral`)
  * `2026-10-30 01:53:25 IST`: [sec.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.35` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.15` (Risk Distance: `0.1949` pts)
  * +2.5R Take Profit: `6.83`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.73` (Risk Distance: `0.1949` pts)
  * +2.5R Take Profit: `6.04`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.59`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
