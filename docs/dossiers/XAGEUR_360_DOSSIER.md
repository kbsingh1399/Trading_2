# 🏛️ SOVEREIGN CANDIDATE DOSSIER: XAGEUR
**Canonical Key**: `XAGEUR` | **Broker Instrument**: `XAGEUR.pi` | **Asset Class**: `Forex Cross`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `50.19` | **Live Ask Quote**: `50.24` | **Mid Price**: `50.21`
- **Spread Points**: `51.00` | **Spread BPS**: `10.16 bps` (Charter Threshold: `5.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `5,000.0` | Digits: `3` | Point: `0.001`
  * Point Value (1.0 Lot): `5.00 USD` | Point Value (0.01 Lot): `0.0500 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `51.14` | VWAP Z-Score: `-2.06` (Regime: `STRETCH_EXTREME`)
  * 14-Period ATR: `0.1776` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `28.04` (State: `OVERSOLD`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `52.36` | Lower -3.00σ Band: `49.92`
  * Upper +2.51σ Band: `52.16` | Lower -2.51σ Band: `50.12`
  * Upper +2.01σ Band: `51.96` | Lower -2.01σ Band: `50.32`
  * Upper +2.00σ Band: `51.95` | Lower -2.00σ Band: `50.33`
  * Upper +1.28σ Band: `51.66` | Lower -1.28σ Band: `50.62`
  * Upper +1.00σ Band: `51.55` | Lower -1.00σ Band: `50.73`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`50.51` | EMA-20=`50.68` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`51.09` (Slope: `+0.0000`) | EMA-100=`51.63`
  * Institutional Anchors: EMA-144=`51.98` | EMA-200=`52.34` (Slope: `-0.4236`) | EMA-233=`52.56`
- **Range Boundaries**: 24H High=`53.07` | 24H Low=`50.29` | Weekly High=`54.61` | Weekly Low=`50.29`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `52.08` (Distance: `-3.58%`)
  * Point of Control (POC) = `51.44` (Distance: `-2.38%`)
  * Value Area Low (VAL) = `50.84` (Distance: `-1.23%`)
  * Auction Positioning: `BELOW_VALUE (Imbalance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `TREND_DOWN_ACCEPTANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`52.92` | POC=`52.45` | VAL=`51.99`
  * Prior Day Extremes: PDH=`54.37` | PDL=`51.95` | PDC=`52.13`
  * Monday Range Blueprint: High=`54.39` | Mid=`53.69` | Low=`52.99`
  * Developing Weekly Value Area: Weekly VAH=`54.54` | Weekly POC=`53.89` | Weekly VAL=`52.62`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`52.22` | Low=`51.08`
  * London Session (08:00-16:00 UTC): High=`51.79` | Low=`50.18`
  * New York Session (13:00-21:00 UTC): High=`50.77` | Low=`50.18`
  * Initial Balance (First Hour): IB High=`51.79` | IB Low=`50.87`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `50.01` - `50.41`
  * Optimal Trade Entry (OTE 0.705): `50.31`
  * Structural Invalidation Anchor (0.786): `50.61`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `50.71` | `50.81` | `50.68` | `50.80` | `886` | 45,009.69 USD | 34,449.72 USD | `+76.54%` | -1,202,322.90 USD | `+1.22` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `50.80` | `50.91` | `50.79` | `50.86` | `1,199` | 60,981.14 USD | 18,448.08 USD | `+30.25%` | -1,183,874.82 USD | `+0.72` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `50.86` | `50.92` | `50.83` | `50.88` | `1,073` | 54,599.60 USD | 15,689.54 USD | `+28.74%` | -1,168,185.28 USD | `+0.62` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.64` | `50.87` | `50.64` | `50.73` | `3,293` | 167,044.01 USD | 11,017.80 USD | `+6.60%` | -1,869,109.40 USD | `+0.38` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `50.73` | `50.81` | `50.68` | `50.80` | `3,334` | 169,370.53 USD | 115,953.67 USD | `+68.46%` | -1,753,155.73 USD | `+1.41` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `50.80` | `50.93` | `50.79` | `50.89` | `3,349` | 170,437.31 USD | 97,301.90 USD | `+57.09%` | -1,655,853.83 USD | `+1.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `51.08` | `51.12` | `50.66` | `50.78` | `20,835` | 1,057,959.63 USD | -603,060.14 USD | `-57.00%` | -2,722,809.76 USD | `-1.27` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.78` | `50.87` | `50.40` | `50.61` | `11,199` | 566,736.59 USD | -139,241.32 USD | `-24.57%` | -2,862,051.08 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `50.61` | `50.93` | `50.56` | `50.89` | `14,682` | 747,196.34 USD | 590,853.63 USD | `+79.08%` | -2,271,197.45 USD | `+1.75` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.37` | `52.76` | `51.98` | `52.42` | `110,375` | 5,785,526.38 USD | 546,780.27 USD | `+9.45%` | -1,493,267.57 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `52.42` | `52.51` | `51.95` | `52.13` | `45,007` | 2,346,304.92 USD | -993,310.91 USD | `-42.34%` | -2,486,578.48 USD | `-0.15` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `52.14` | `52.22` | `51.73` | `51.78` | `24,880` | 1,288,261.52 USD | -1,001,103.02 USD | `-77.71%` | -3,487,681.50 USD | `-0.14` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.78` | `51.80` | `51.08` | `51.36` | `77,852` | 3,998,478.72 USD | -1,594,400.32 USD | `-39.88%` | -5,082,081.83 USD | `-0.66` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `51.36` | `51.79` | `50.40` | `50.89` | `62,135` | 3,162,174.42 USD | -1,002,113.55 USD | `-31.69%` | -6,084,195.37 USD | `+0.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `116` | `0x5b5d...c060` | `SHORT` | 17,386,684.11 USD | `346,127.65` | `58.90` | `50.19` | `500.92` | 2,999,675.98 USD | `+17.25%` | `5X Cross` |
| `128` | `0x4692...164f` | `SHORT` | 15,438,421.86 USD | `307,470.91` | `52.03` | `50.19` | `262.54` | 558,536.91 USD | `+3.62%` | `5X Cross` |
| `212` | `0xacb6...efbd` | `SHORT` | 10,105,139.63 USD | `201,133.33` | `59.63` | `50.19` | `77.28` | 1,887,517.48 USD | `+18.68%` | `6X Cross` |
| `250` | `0xc26c...b8f4` | `LONG` | 9,115,270.01 USD | `181,463.41` | `55.43` | `50.19` | `0.000000` | -943,485.07 USD | `-10.35%` | `2X Cross` |
| `283` | `0x49e9...e1d0` | `SHORT` | 8,329,586.01 USD | `165,789.30` | `55.17` | `50.19` | `100.16` | 817,849.01 USD | `+9.82%` | `4X Cross` |
| `359` | `0x645b...87b8` | `LONG` | 6,458,675.34 USD | `128,576.91` | `56.54` | `50.19` | `0.000000` | -811,393.90 USD | `-12.56%` | `3X Cross` |
| `363` | `0xd8c5...99b0` | `SHORT` | 6,345,055.61 USD | `126,320.04` | `61.98` | `50.19` | `198.56` | 1,484,282.24 USD | `+23.39%` | `3X Cross` |
| `398` | `0xe9ff...5903` | `SHORT` | 5,673,759.17 USD | `112,996.08` | `60.07` | `50.19` | `171.37` | 1,114,191.64 USD | `+19.64%` | `5X Cross` |
| `652` | `0xfc66...ca06` | `SHORT` | 3,452,654.47 USD | `68,762.91` | `50.60` | `50.19` | `409.26` | 26,622.88 USD | `+0.77%` | `8X Cross` |
| `758` | `0x2056...8396` | `LONG` | 3,014,580.00 USD | `60,000.00` | `66.92` | `50.19` | `21.36` | -1,000,747.14 USD | `-33.20%` | `10X Cross` |
| `827` | `0x9aa5...58af` | `LONG` | 2,737,186.39 USD | `54,513.68` | `61.59` | `50.19` | `0.000000` | -620,521.34 USD | `-22.67%` | `20X Cross` |
| `882` | `0x0242...ffa1` | `SHORT` | 2,507,364.25 USD | `49,916.67` | `56.48` | `50.19` | `334.69` | 311,767.61 USD | `+12.43%` | `10X Cross` |
| `890` | `0x960b...f0fc` | `LONG` | 2,484,866.83 USD | `49,457.96` | `55.82` | `50.19` | `0.000000` | -276,070.20 USD | `-11.11%` | `25X Cross` |
| `955` | `0xb078...de15` | `SHORT` | 2,312,013.88 USD | `46,027.63` | `52.23` | `50.19` | `182.09` | 91,790.55 USD | `+3.97%` | `8X Cross` |
| `980` | `0x8b9d...7b28` | `LONG` | 2,251,527.72 USD | `44,823.47` | `58.35` | `50.19` | `0.000000` | -363,920.82 USD | `-16.16%` | `10X Cross` |
| `1069` | `0x5647...e7de` | `LONG` | 2,022,444.30 USD | `40,262.07` | `57.38` | `50.19` | `0.000000` | -287,793.30 USD | `-14.23%` | `20X Cross` |
| `1080` | `0xa2ce...3126` | `LONG` | 2,008,480.00 USD | `40,000.00` | `74.30` | `50.19` | `0.000000` | -963,575.49 USD | `-47.98%` | `20X Cross` |
| `1217` | `0x4e23...20c3` | `LONG` | 1,802,206.16 USD | `35,870.51` | `50.29` | `50.19` | `0.000000` | -1,851.49 USD | `-0.10%` | `16X Cross` |
| `1440` | `0x3678...b209` | `LONG` | 1,506,960.00 USD | `30,000.00` | `57.15` | `50.19` | `0.000000` | -207,540.00 USD | `-13.77%` | `20X Cross` |
| `1442` | `0x5a88...d997` | `LONG` | 1,506,900.00 USD | `30,000.00` | `59.50` | `50.19` | `38.49` | -277,987.59 USD | `-18.45%` | `25X Cross` |
| `1591` | `0x24fb...ed0f` | `LONG` | 1,336,646.91 USD | `26,610.00` | `51.24` | `50.19` | `0.000000` | -26,752.77 USD | `-2.00%` | `20X Cross` |
| `1612` | `0x354b...6425` | `SHORT` | 1,312,719.90 USD | `26,144.07` | `50.52` | `50.19` | `473.58` | 8,066.22 USD | `+0.61%` | `10X Cross` |
| `1642` | `0xed62...e004` | `SHORT` | 1,288,975.72 USD | `25,660.45` | `50.81` | `50.19` | `54.73` | 14,831.74 USD | `+1.15%` | `25X Cross` |
| `1674` | `0x7ea9...fc7f` | `LONG` | 1,255,300.00 USD | `25,000.00` | `53.60` | `50.19` | `35.35` | -84,704.05 USD | `-6.75%` | `25X Cross` |
| `1815` | `0xf517...c032` | `LONG` | 1,136,873.48 USD | `22,627.50` | `66.29` | `50.19` | `0.000000` | -363,121.62 USD | `-31.94%` | `20X Cross` |
| `1861` | `0x9e11...22a3` | `LONG` | 1,102,390.97 USD | `21,945.99` | `50.67` | `50.19` | `34.46` | -9,531.43 USD | `-0.86%` | `3X Isolated` |
| `1940` | `0xcc9f...d218` | `LONG` | 1,030,975.46 USD | `20,520.60` | `52.63` | `50.19` | `26.87` | -48,932.59 USD | `-4.75%` | `2X Isolated` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`52.71` (Vol: 3,600,000.00 USD, Dist: `+4.03%`) | Long MP=`50.23` (Vol: 3,100,000.00 USD, Dist: `--0.86%`)
  * 48H Horizon: Short MP=`54.87` (Vol: 4,200,000.00 USD, Dist: `+8.28%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 3D Horizon: Short MP=`54.97` (Vol: 5,200,000.00 USD, Dist: `+8.49%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
  * 7D Horizon: Short MP=`55.07` (Vol: 7,100,000.00 USD, Dist: `+8.69%`) | Long MP=`50.60` (Vol: 2,100,000.00 USD, Dist: `--0.13%`)
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
  * Current Rate: `49.41K` | Last 24h: `158.28K` | Last 3d: `386.46K` | Last 7d: `548.84K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-` | **USDT OKX** | `-` |
| **USDT Bybit** | `-` | **USDT KuCoin** | `-` |
| **USDT MEXC** | `0.0101%` | **USDT BingX** | `-` |
| **USDT Gate** | `-` | **USDT Bitget** | `-` |
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
| `2026-10-28 21:11:32 IST` | `Auction` | `AUCTION_ROTATIONAL_BALANCE` | **`BEARISH (BELOW PIVOT)`** | SILVER (XAGUSD.pi) Metal Auction: ROTATI | `53.72` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `15m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30m` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `2h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `4h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `6h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `8h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `12h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `24h` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `1w` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |
| `30d` | 0.00 USD | 0.00 USD | **`NEUTRAL`** |

* Spot Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
* Futures Capital Netflows: 5m=`-` | 15m=`-` | 1h=`-` | 24h=`-`
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
  * Execution Entry: `50.84` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `50.55` (Risk Distance: `0.2896` pts)
  * +2.5R Take Profit: `51.56`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `52.08` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `52.37` (Risk Distance: `0.2896` pts)
  * +2.5R Take Profit: `51.35`
  * Mathematical Lot Sizing: **`0.01 lots`** (Nominal Risk = `0.01 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`50.61`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
