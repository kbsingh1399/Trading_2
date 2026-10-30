# 🏛️ SOVEREIGN CANDIDATE DOSSIER: UNIUSD
**Canonical Key**: `UNIUSD` | **Broker Instrument**: `UNIUSD.p` | **Asset Class**: `Crypto Altcoin`
**Timestamp**: `2026-10-30 09:28:14 IST` (`2026-10-30 03:58:14 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `6.74` | **Live Ask Quote**: `6.76` | **Mid Price**: `6.75`
- **Spread Points**: `25.00` | **Spread BPS**: `37.04 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `6.50` | VWAP Z-Score: `+2.11` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1013` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `56.54` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `6.80` | Lower -3.00σ Band: `6.19`
  * Upper +2.51σ Band: `6.75` | Lower -2.51σ Band: `6.24`
  * Upper +2.01σ Band: `6.70` | Lower -2.01σ Band: `6.29`
  * Upper +2.00σ Band: `6.70` | Lower -2.00σ Band: `6.29`
  * Upper +1.28σ Band: `6.63` | Lower -1.28σ Band: `6.37`
  * Upper +1.00σ Band: `6.60` | Lower -1.00σ Band: `6.39`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`6.61` | EMA-20=`6.60` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`6.74` (Slope: `+0.0000`) | EMA-100=`6.88`
  * Institutional Anchors: EMA-144=`6.93` | EMA-200=`6.97` (Slope: `-0.7013`) | EMA-233=`6.99`
- **Range Boundaries**: 24H High=`7.50` | 24H Low=`6.23` | Weekly High=`7.50` | Weekly Low=`6.23`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `6.56` (Distance: `+2.84%`)
  * Point of Control (POC) = `6.46` (Distance: `+4.45%`)
  * Value Area Low (VAL) = `6.28` (Distance: `+7.38%`)
  * Auction Positioning: `ABOVE_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `RANGE_EXPANSION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`7.32` | POC=`7.16` | VAL=`6.99`
  * Prior Day Extremes: PDH=`7.50` | PDL=`6.48` | PDC=`6.58`
  * Monday Range Blueprint: High=`7.17` | Mid=`6.97` | Low=`6.76`
  * Developing Weekly Value Area: Weekly VAH=`7.23` | Weekly POC=`7.05` | Weekly VAL=`6.91`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`6.79` | Low=`6.23`
  * London Session (08:00-16:00 UTC): High=`6.78` | Low=`6.72`
  * New York Session (13:00-21:00 UTC): High=`6.79` | Low=`6.71`
  * Initial Balance (First Hour): IB High=`6.77` | IB Low=`6.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `6.72` - `6.78`
  * Optimal Trade Entry (OTE 0.705): `6.76`
  * Structural Invalidation Anchor (0.786): `6.80`

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
| --- | **`6.75`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 09:20:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `333` | `0x5396...8b79` | `LONG` | 6,765,748.65 USD | `999,999.80` | `6.88` | `6.74` | `5.66` | -114,949.68 USD | `-1.70%` | `5X Cross` |
| `752` | `0x9df2...c665` | `SHORT` | 3,033,652.50 USD | `450,000.00` | `4.49` | `6.74` | `73.85` | -1,012,652.37 USD | `-33.38%` | `10X Cross` |
| `820` | `0xecb6...2b00` | `SHORT` | 2,776,509.32 USD | `412,009.80` | `6.63` | `6.74` | `71.40` | -44,560.06 USD | `-1.60%` | `10X Cross` |
| `832` | `0xbf6d...ecc0` | `LONG` | 2,724,842.52 USD | `404,134.80` | `7.42` | `6.74` | `5.17` | -274,581.07 USD | `-10.08%` | `10X Cross` |
| `881` | `0xcd21...9826` | `LONG` | 2,580,782.83 USD | `382,990.70` | `7.52` | `6.74` | `5.38` | -298,897.29 USD | `-11.58%` | `10X Cross` |
| `1000` | `0xdd53...2b13` | `SHORT` | 2,232,292.12 USD | `331,155.90` | `7.28` | `6.74` | `189.83` | 178,314.18 USD | `+7.99%` | `3X Cross` |
| `1052` | `0x60a8...85f6` | `SHORT` | 2,068,307.84 USD | `306,870.60` | `6.48` | `6.74` | `60.69` | -79,107.82 USD | `-3.82%` | `10X Cross` |
| `1083` | `0xb46b...538e` | `SHORT` | 2,022,660.00 USD | `300,000.00` | `8.20` | `6.74` | `21.45` | 437,124.42 USD | `+21.61%` | `10X Cross` |
| `1239` | `0xf21d...3b2d` | `LONG` | 1,788,478.93 USD | `265,479.00` | `4.32` | `6.74` | `4.10` | 642,219.90 USD | `+35.91%` | `10X Isolated` |
| `1333` | `0xf472...5d8b` | `LONG` | 1,626,844.54 USD | `241,374.10` | `4.44` | `6.74` | `0.000000` | 554,201.26 USD | `+34.07%` | `5X Cross` |
| `1460` | `0xb5b3...7a08` | `LONG` | 1,482,470.00 USD | `220,000.00` | `7.36` | `6.74` | `1.77` | -137,740.15 USD | `-9.29%` | `10X Cross` |
| `1517` | `0x265e...7f70` | `LONG` | 1,419,662.16 USD | `210,665.50` | `7.39` | `6.74` | `0.000000` | -137,671.03 USD | `-9.70%` | `3X Cross` |
| `1580` | `0xcac1...26b3` | `SHORT` | 1,350,752.84 USD | `200,336.80` | `7.76` | `6.74` | `49.60` | 203,095.13 USD | `+15.04%` | `10X Cross` |
| `1645` | `0x9aa5...58af` | `SHORT` | 1,285,797.89 USD | `190,771.20` | `7.34` | `6.74` | `53.75` | 114,562.61 USD | `+8.91%` | `10X Cross` |
| `1717` | `0x12d2...f97f` | `LONG` | 1,221,008.47 USD | `180,697.40` | `8.85` | `6.74` | `0.000000` | -378,911.42 USD | `-31.03%` | `10X Cross` |
| `1721` | `0x7cee...fc93` | `SHORT` | 1,216,094.54 USD | `180,405.10` | `6.84` | `6.74` | `21.64` | 17,722.04 USD | `+1.46%` | `5X Cross` |
| `1775` | `0x645b...87b8` | `SHORT` | 1,169,334.99 USD | `173,519.90` | `8.57` | `6.74` | `127.52` | 318,183.80 USD | `+27.21%` | `10X Cross` |
| `1806` | `0x51f6...2b39` | `SHORT` | 1,142,448.89 USD | `169,485.20` | `7.30` | `6.74` | `13.93` | 94,218.32 USD | `+8.25%` | `10X Cross` |
| `1811` | `0xb83d...6e36` | `SHORT` | 1,138,852.71 USD | `168,971.00` | `7.45` | `6.74` | `769.08` | 119,249.52 USD | `+10.47%` | `3X Cross` |
| `1929` | `0xdf95...7d72` | `SHORT` | 1,042,605.07 USD | `154,714.20` | `6.56` | `6.74` | `247.28` | -27,007.61 USD | `-2.59%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `6.82` | 168.47 USD | `-` | `NEWS_INTEL` | `-` | #UNI Liquidated Long: 0.17K USD at 6.8205 USD [API] | `2026-09-07 15:43:29` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`6.76` (Vol: 718,000.00 USD, Dist: `+0.27%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.12%`)
  * 48H Horizon: Short MP=`6.76` (Vol: 718,000.00 USD, Dist: `+0.27%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.12%`)
  * 3D Horizon: Short MP=`6.76` (Vol: 718,000.00 USD, Dist: `+0.27%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.12%`)
  * 7D Horizon: Short MP=`6.76` (Vol: 718,000.00 USD, Dist: `+0.27%`) | Long MP=`6.33` (Vol: 1,000,000.00 USD, Dist: `--6.12%`)
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
  * Current Rate: `4.42K` | Last 24h: `53.94K` | Last 3d: `142.67K` | Last 7d: `259.87K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0006%` |
| **USDT Bybit** | `-0.0206%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0074%` | **USDT Bitget** | `0.0100%` |
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
| `0:00 UTC` | `6.55` | `6.52` | `6.55` | `6.58` | `6.44` | 5,592,794.96 USD | 2,688,660.61 USD | 2,904,134.35 USD | -215,473.74 USD | `-3.85%` | `7B / 23S` |
| `5:00 UTC` | `6.51` | `6.51` | `6.51` | `6.56` | `6.45` | 8,801,980.78 USD | 4,357,443.96 USD | 4,444,536.83 USD | -87,092.87 USD | `-0.99%` | `8B / 5S` |
| `0:00 UTC` | `6.53` | `6.54` | `6.53` | `6.61` | `6.48` | 5,801,726.86 USD | 2,983,022.82 USD | 2,818,704.04 USD | 164,318.78 USD | `+2.83%` | `13B / 18S` |
| `5:00 UTC` | `6.64` | `6.64` | `6.64` | `6.67` | `6.60` | 11,236,075.28 USD | 6,492,166.43 USD | 4,743,908.85 USD | 1,748,257.58 USD | `+15.56%` | `6B / 7S` |
| `0:00 UTC` | `6.67` | `6.67` | `6.67` | `6.68` | `6.64` | 4,772,123.07 USD | 1,778,438.22 USD | 2,993,684.86 USD | -1,215,246.64 USD | `-25.47%` | `0B / 6S` |
| `5:00 UTC` | `6.62` | `6.63` | `6.62` | `6.67` | `6.61` | 2,405,930.78 USD | 1,117,414.85 USD | 1,288,515.94 USD | -171,101.09 USD | `-7.11%` | `5B / 14S` |
| `0:00 UTC` | `6.63` | `6.63` | `6.63` | `6.65` | `6.60` | 2,714,211.79 USD | 1,270,573.80 USD | 1,443,637.99 USD | -173,064.19 USD | `-6.38%` | `1B / 5S` |
| `5:00 UTC` | `6.66` | `6.65` | `6.66` | `6.68` | `6.62` | 2,098,352.85 USD | 1,088,207.05 USD | 1,010,145.80 USD | 78,061.25 USD | `+3.72%` | `7B / 6S` |
| `0:00 UTC` | `6.70` | `6.70` | `6.70` | `6.74` | `6.67` | 2,696,324.51 USD | 1,506,489.83 USD | 1,189,834.69 USD | 316,655.14 USD | `+11.74%` | `14B / 8S` |
| `5:00 UTC` | `6.73` | `6.74` | `6.73` | `6.75` | `6.73` | 655,693.76 USD | 276,079.70 USD | 379,614.06 USD | -103,534.36 USD | `-15.79%` | `3B / 4S` |

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
| `5m` | 16,640.00 USD | 130,580.00 USD | **`ACCUMULATION`** |
| `15m` | 285,360.00 USD | 492,680.00 USD | **`ACCUMULATION`** |
| `30m` | 239,110.00 USD | 929,780.00 USD | **`ACCUMULATION`** |
| `1h` | -507,410.00 USD | 635,630.00 USD | **`ACCUMULATION`** |
| `2h` | -2,480,000.00 USD | 385,670.00 USD | **`DISTRIBUTION`** |
| `4h` | -4,990,000.00 USD | -3,440,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -9,610,000.00 USD | -28,820,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,200,000.00 USD | -37,590,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -13,420,000.00 USD | -40,020,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -12,840,000.00 USD | -42,930,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -19,390,000.00 USD | -86,770,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -53,680,000.00 USD | -500,830,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+16.64K` | 15m=`+285.36K` | 1h=`-507.41K` | 24h=`-12.84M`
* Futures Capital Netflows: 5m=`+130.58K` | 15m=`+492.68K` | 1h=`+635.63K` | 24h=`-42.93M`
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
  * `2026-10-30 09:09:58 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:33:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:32:58 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 09:15:58 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 09:14:58 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:16:58 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:16:58 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)
  * `2026-10-30 04:16:58 IST`: [economics.td.com] - (Sentiment: `Neutral`)


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
  * Execution Entry: `6.28` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `6.12` (Risk Distance: `0.1591` pts)
  * +2.5R Take Profit: `6.68`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `6.56` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `6.72` (Risk Distance: `0.1591` pts)
  * +2.5R Take Profit: `6.16`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`6.80`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
