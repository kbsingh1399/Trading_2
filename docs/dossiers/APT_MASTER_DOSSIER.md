# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:23:36 IST` (`2026-10-30 08:53:36 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `0.6900` | **Live Ask Quote**: `0.6901` | **Mid Price**: `0.6901`
- **Spread Points**: `0.000138` | **Spread BPS**: `2.00 bps` (Charter Threshold: `12.00 bps`)
- **Gate 1 Clearance**: **`PASS`** | **Execution Posture**: `PASSIVE_MAKER_LIMIT_ONLY` | **Order Type Allowed**: `LIMIT_ONLY`
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
  * Session VWAP: `0.6901` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `0.6949` | Lower -3.00σ Band: `0.6852`
  * Upper +2.51σ Band: `0.6939` | Lower -2.51σ Band: `0.6863`
  * Upper +2.01σ Band: `0.6930` | Lower -2.01σ Band: `0.6872`
  * Upper +2.00σ Band: `0.6928` | Lower -2.00σ Band: `0.6873`
  * Upper +1.28σ Band: `0.6920` | Lower -1.28σ Band: `0.6881`
  * Upper +1.00σ Band: `0.6914` | Lower -1.00σ Band: `0.6887`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`0.6901` | EMA-20=`0.6901` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`0.6901` (Slope: `+0.0000`) | EMA-100=`0.6901`
  * Institutional Anchors: EMA-144=`0.6901` | EMA-200=`0.6901` (Slope: `+0.0000`) | EMA-233=`0.6901`
- **Range Boundaries**: 24H High=`0.6970` | 24H Low=`0.6832` | Weekly High=`0.7039` | Weekly Low=`0.6763`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `0.6921` (Distance: `+0.00%`)
  * Point of Control (POC) = `0.6901` (Distance: `+0.00%`)
  * Value Area Low (VAL) = `0.6880` (Distance: `+0.00%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`NEUTRAL`** | Market Regime: `BALANCED_AUCTION`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`0.6928` | POC=`0.6901` | VAL=`0.6873`
  * Prior Day Extremes: PDH=`0.6942` | PDL=`0.6859` | PDC=`0.6901`
  * Monday Range Blueprint: High=`0.6935` | Mid=`0.6901` | Low=`0.6866`
  * Developing Weekly Value Area: Weekly VAH=`0.6956` | Weekly POC=`0.6901` | Weekly VAL=`0.6845`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`0.6914` | Low=`0.6887`
  * London Session (08:00-16:00 UTC): High=`0.6928` | Low=`0.6873`
  * New York Session (13:00-21:00 UTC): High=`0.6942` | Low=`0.6859`
  * Initial Balance (First Hour): IB High=`0.6921` | IB Low=`0.6880`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `0.6873` - `0.6928`
  * Optimal Trade Entry (OTE 0.705): `0.6914`
  * Structural Invalidation Anchor (0.786): `0.6956`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `0.6203` | `0.6207` | `0.6185` | `0.6186` | `172,601` | 107,040.01 USD | 30,943.80 USD | `+28.91%` | -6,134,987.80 USD | `+0.78` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `0.6186` | `0.6197` | `0.6169` | `0.6186` | `162,563` | 100,458.88 USD | -31,153.63 USD | `-31.01%` | -6,166,141.43 USD | `-1.05` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `0.6186` | `0.6186` | `0.6168` | `0.6168` | `27,913` | 17,233.45 USD | -7,558.40 USD | `-43.86%` | -6,173,699.83 USD | `-0.30` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `0.6189` | `0.6221` | `0.6169` | `0.6218` | `454,874` | 281,500.66 USD | 40,847.84 USD | `+14.51%` | -6,152,833.36 USD | `+0.64` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `0.6219` | `0.6227` | `0.6190` | `0.6202` | `418,432` | 259,699.58 USD | -13,098.24 USD | `-5.04%` | -6,165,931.60 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6203` | `0.6207` | `0.6169` | `0.6169` | `362,350` | 224,284.35 USD | -7,320.25 USD | `-3.26%` | -6,173,251.84 USD | `+0.15` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `0.6194` | `0.6301` | `0.6174` | `0.6243` | `2,525,871` | 1,575,584.41 USD | -193,264.45 USD | `-12.27%` | -6,308,896.38 USD | `+0.15` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6243` | `0.6267` | `0.6164` | `0.6189` | `2,727,046` | 1,694,829.37 USD | 60,855.45 USD | `+3.59%` | -6,248,040.93 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6189` | `0.6227` | `0.6168` | `0.6174` | `1,243,290` | 770,194.78 USD | 24,243.58 USD | `+3.15%` | -6,223,797.36 USD | `+0.43` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6227` | `0.6169` | `0.6169` | `1,235,656` | 765,484.59 USD | 20,429.35 USD | `+2.67%` | -6,048,007.39 USD | `+0.80` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -1,617,014.88 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,283,281.24 USD | `-1.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6227` | `0.6169` | `0.6169` | `1,235,656` | 765,484.59 USD | 20,429.35 USD | `+2.67%` | -6,048,007.39 USD | `+0.80` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:22:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`0.7060` (Vol: 90,823.17 USD, Dist: `+2.43%`) | Long MP=`0.6718` (Vol: 39,956.88 USD, Dist: `--2.53%`)
  * 48H Horizon: Short MP=`0.7055` (Vol: 81,903.46 USD, Dist: `+2.36%`) | Long MP=`0.6702` (Vol: 45,046.52 USD, Dist: `--2.77%`)
  * 3D Horizon: Short MP=`0.7210` (Vol: 125,191.03 USD, Dist: `+4.60%`) | Long MP=`0.6703` (Vol: 75,398.81 USD, Dist: `--2.76%`)
  * 7D Horizon: Short MP=`0.8539` (Vol: 187,280.71 USD, Dist: `+24.46%`) | Long MP=`0.6700` (Vol: 92,436.78 USD, Dist: `--2.35%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `0.1415` | 283.00 USD | 250,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1545` | 19,930.00 USD | 249,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 229,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1885` | 837.82 USD | 229,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2205` | 228.91 USD | 228,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2315` | 232.95 USD | 228,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2325` | 2,620.00 USD | 228,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 225,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 224,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 9,950.00 USD | 222,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 212,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 212,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3725` | 558.75 USD | 212,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 211,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 211,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 208,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4055` | 283.85 USD | 208,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4095` | 414.59 USD | 208,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 207,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 6,740.00 USD | 206,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 200,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 199,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4375` | 31,060.00 USD | 199,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4385` | 824.98 USD | 168,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 167,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 27,150.00 USD | 167,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 5,530.00 USD | 139,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 134,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 901.90 USD | 134,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 5,730.00 USD | 133,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 127,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 126,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 188.60 USD | 126,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 126,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 125,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 125,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4895` | 165.94 USD | 122,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 122,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 111,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 110,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 107,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 667.49 USD | 107,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 106,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 303.42 USD | 105,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 105,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 519.77 USD | 105,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 105,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 104,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 104,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 95,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5220` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5260` | 1,440,000.00 USD | 1,440,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5270` | 1,430,000.00 USD | 1,430,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5290` | 1,420,000.00 USD | 1,420,000.00 USD | 2,560.00 USD | 0.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 94,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5300` | 1,420,000.00 USD | 1,420,000.00 USD | 2,560.00 USD | 0.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5310` | 1,410,000.00 USD | 1,410,000.00 USD | 8,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 92,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,400,000.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 81,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5330` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 79,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5350` | 1,390,000.00 USD | 1,390,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 44.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5370` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 1,550.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5390` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 80.65 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5410` | 1,380,000.00 USD | 1,380,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,370,000.00 USD | 1,370,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5430` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 627.61 USD | 4,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 523.59 USD | 8,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 78,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5450` | 1,340,000.00 USD | 1,340,000.00 USD | 2,250.00 USD | 0.00 USD | 2,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 3,030.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5470` | 1,330,000.00 USD | 1,330,000.00 USD | 0.00 USD | 795.70 USD | 17.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 78,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,330,000.00 USD | 1,330,000.00 USD | 2,000.00 USD | 0.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5490` | 1,330,000.00 USD | 1,330,000.00 USD | 2,100.00 USD | 474.54 USD | 2,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,320,000.00 USD | 1,320,000.00 USD | 3,890.00 USD | 967.07 USD | 4,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5510` | 1,310,000.00 USD | 1,310,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,310,000.00 USD | 1,310,000.00 USD | 2,380.00 USD | 0.00 USD | 24.91 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5530` | 1,300,000.00 USD | 1,300,000.00 USD | 1,650.00 USD | 1,150.00 USD | 12,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 1,420,000.00 USD | 1,420,000.00 USD | 6,650.00 USD | 7,160.00 USD | 4,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,290,000.00 USD | 1,290,000.00 USD | 11,190.00 USD | 6,110.00 USD | 5,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 76,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 1,400,000.00 USD | 1,400,000.00 USD | 2,940.00 USD | 0.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5550` | 1,260,000.00 USD | 1,260,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 1,400,000.00 USD | 1,400,000.00 USD | 4,540.00 USD | 686.25 USD | 1,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,250,000.00 USD | 1,250,000.00 USD | 12,540.00 USD | 0.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 1,390,000.00 USD | 1,390,000.00 USD | 4,670.00 USD | 2,460.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5570` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 812.74 USD | 3,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 1,380,000.00 USD | 1,380,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 1,230,000.00 USD | 1,230,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 1,370,000.00 USD | 1,370,000.00 USD | 1,670.00 USD | 2,150.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5590` | 1,200,000.00 USD | 1,200,000.00 USD | 2,660.00 USD | 7,220.00 USD | 2,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 1,190,000.00 USD | 1,190,000.00 USD | 1,410.00 USD | 938.63 USD | 15.87 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 1,360,000.00 USD | 1,360,000.00 USD | 2,240.00 USD | 500.33 USD | 823.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5610` | 1,180,000.00 USD | 1,180,000.00 USD | 13,590.00 USD | 1,960.00 USD | 7,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 18,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 1,350,000.00 USD | 1,350,000.00 USD | 1,800.00 USD | 995.72 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 1,160,000.00 USD | 1,160,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 1,350,000.00 USD | 1,350,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5630` | 1,140,000.00 USD | 1,140,000.00 USD | 14,240.00 USD | 2,380.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 1,330,000.00 USD | 1,330,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 24.47 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5650` | 1,310,000.00 USD | 1,310,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5650` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 18,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 1,120,000.00 USD | 1,120,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5670` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 1,100,000.00 USD | 1,100,000.00 USD | 5,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5690` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 107.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 1,090,000.00 USD | 1,090,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5710` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 2,850.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 1,520.00 USD | 10,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5730` | 1,070,000.00 USD | 1,070,000.00 USD | 2,690.00 USD | 528.82 USD | 185.80 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 1,070,000.00 USD | 1,070,000.00 USD | 18,940.00 USD | 574.82 USD | 1,470.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 218.30 USD | 14,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 1,280,000.00 USD | 1,280,000.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 1,250,000.00 USD | 1,250,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 1,050,000.00 USD | 1,050,000.00 USD | 2,150.00 USD | 7,300.00 USD | 28.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 1,230,000.00 USD | 1,230,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5770` | 1,040,000.00 USD | 1,040,000.00 USD | 21,510.00 USD | 0.00 USD | 146.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 1,210,000.00 USD | 1,210,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 1,020,000.00 USD | 1,020,000.00 USD | 19,410.00 USD | 0.00 USD | 1,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 1,200,000.00 USD | 1,200,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5790` | 996,470.00 USD | 996,470.00 USD | 1,610.00 USD | 0.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 1,170,000.00 USD | 1,170,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 983,750.00 USD | 983,750.00 USD | 0.00 USD | 3,900.00 USD | 16,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5810` | 963,060.00 USD | 963,060.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 1,150,000.00 USD | 1,150,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 959,700.00 USD | 959,700.00 USD | 0.00 USD | 0.00 USD | 3,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 1,140,000.00 USD | 1,140,000.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 2,190.00 USD | 4,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 956,160.00 USD | 956,160.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 1,120,000.00 USD | 1,120,000.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 1,090,000.00 USD | 1,090,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 1,080,000.00 USD | 1,080,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5870` | 935,010.00 USD | 935,010.00 USD | 0.00 USD | 1,400.00 USD | 195.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 1,060,000.00 USD | 1,060,000.00 USD | 33,380.00 USD | 8,680.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 933,410.00 USD | 933,410.00 USD | 3,110.00 USD | 14,610.00 USD | 211.49 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 8,900.00 USD | 14,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 1,010,000.00 USD | 1,010,000.00 USD | 34,810.00 USD | 11,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5890` | 915,480.00 USD | 915,480.00 USD | 43,020.00 USD | 0.00 USD | 163.05 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 966,260.00 USD | 966,260.00 USD | 24,340.00 USD | 12,640.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 872,290.00 USD | 872,290.00 USD | 61,220.00 USD | 1,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 919,130.00 USD | 919,130.00 USD | 26,100.00 USD | 12,590.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5910` | 809,520.00 USD | 809,520.00 USD | 0.00 USD | 9,340.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5915` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5920` | 861,150.00 USD | 861,150.00 USD | 25,360.00 USD | 6,570.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 783,660.00 USD | 783,660.00 USD | 11,690.00 USD | 10,620.00 USD | 58,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 819,240.00 USD | 819,240.00 USD | 11,360.00 USD | 6,380.00 USD | 18,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5930` | 702,530.00 USD | 702,530.00 USD | 25,390.00 USD | 0.00 USD | 10,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 783,410.00 USD | 783,410.00 USD | 24,760.00 USD | 2,040.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 666,640.00 USD | 666,640.00 USD | 5,780.00 USD | 0.00 USD | 46.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 740,180.00 USD | 740,180.00 USD | 37,990.00 USD | 4,980.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5950` | 660,820.00 USD | 660,820.00 USD | 13,060.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 695,580.00 USD | 695,580.00 USD | 12,270.00 USD | 2,560.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 647,760.00 USD | 647,760.00 USD | 5,120.00 USD | 18,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 672,170.00 USD | 672,170.00 USD | 12,870.00 USD | 532.93 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 653,590.00 USD | 653,590.00 USD | 15,950.00 USD | 4,300.00 USD | 54.42 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 624,230.00 USD | 624,230.00 USD | 37,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 633,290.00 USD | 633,290.00 USD | 6,880.00 USD | 1,700.00 USD | 1,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 586,410.00 USD | 586,410.00 USD | 3,320.00 USD | 0.00 USD | 247.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 623,610.00 USD | 623,610.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 582,840.00 USD | 582,840.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 586,470.00 USD | 586,470.00 USD | 2,960.00 USD | 6,370.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6010` | 554,780.00 USD | 554,780.00 USD | 12,110.00 USD | 4,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 572,110.00 USD | 572,110.00 USD | 2,680.00 USD | 8,040.00 USD | 1,720.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 538,580.00 USD | 538,580.00 USD | 0.00 USD | 7,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 559,670.00 USD | 559,670.00 USD | 40,580.00 USD | 14,050.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 531,430.00 USD | 531,430.00 USD | 38,530.00 USD | 0.00 USD | 139.74 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 501,400.00 USD | 501,400.00 USD | 6,530.00 USD | 9,900.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 492,760.00 USD | 492,760.00 USD | 0.00 USD | 18,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 477,400.00 USD | 477,400.00 USD | 20,690.00 USD | 2,140.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6050` | 474,080.00 USD | 474,080.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 440,870.00 USD | 440,870.00 USD | 22,710.00 USD | 0.00 USD | 10,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 453,270.00 USD | 453,270.00 USD | 30,590.00 USD | 0.00 USD | 20,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 407,870.00 USD | 407,870.00 USD | 27,430.00 USD | 4,080.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 401,920.00 USD | 401,920.00 USD | 11,560.00 USD | 0.00 USD | 161.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 360,280.00 USD | 360,280.00 USD | 26,190.00 USD | 6,680.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 390,200.00 USD | 390,200.00 USD | 2,860.00 USD | 0.00 USD | 30,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 324,330.00 USD | 324,330.00 USD | 11,540.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 356,940.00 USD | 356,940.00 USD | 13,920.00 USD | 44,860.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 309,760.00 USD | 309,760.00 USD | 3,470.00 USD | 1,070.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 273,040.00 USD | 273,040.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 263,680.00 USD | 263,680.00 USD | 27,240.00 USD | 7,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 262,990.00 USD | 262,990.00 USD | 34,870.00 USD | 2,210.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 229,250.00 USD | 229,250.00 USD | 43,790.00 USD | 3,410.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 213,040.00 USD | 213,040.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 179,880.00 USD | 179,880.00 USD | 85,200.00 USD | 6,720.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 156,500.00 USD | 156,500.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 47,840.00 USD | 47,840.00 USD | 6,130.00 USD | 9,520.00 USD | 19,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 22,770.00 USD | 22,770.00 USD | 0.00 USD | 6,170.00 USD | 45.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6150` | 12,990.00 USD | 12,990.00 USD | 12,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6150` | 16,560.00 USD | 16,560.00 USD | 0.00 USD | 0.00 USD | 16,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6160` | 147.01 USD | 147.01 USD | 0.00 USD | 0.00 USD | 147.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6160` | 294.02 USD | 294.02 USD | 0.00 USD | 0.00 USD | 147.01 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6170` | 424.25 USD | 424.25 USD | 0.00 USD | 0.00 USD | 130.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6180` | 1,760.00 USD | 1,760.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6200` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 50.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 43,430.00 USD | 43,430.00 USD | 13,870.00 USD | 0.00 USD | 29,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6210` | 66,240.00 USD | 66,240.00 USD | 0.00 USD | 22,640.00 USD | 168.33 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 66,360.00 USD | 66,360.00 USD | 0.00 USD | 0.00 USD | 118.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6230` | 66,430.00 USD | 66,430.00 USD | 0.00 USD | 0.00 USD | 66.51 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 73,930.00 USD | 73,930.00 USD | 0.00 USD | 7,300.00 USD | 199.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6250` | 74,230.00 USD | 74,230.00 USD | 0.00 USD | 0.00 USD | 303.07 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6260` | 10,180.00 USD | 10,180.00 USD | 0.00 USD | 8,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 74,460.00 USD | 74,460.00 USD | 0.00 USD | 0.00 USD | 229.50 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6270` | 82,720.00 USD | 82,720.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 52,000.00 USD | 52,000.00 USD | 0.00 USD | 16,420.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 121,950.00 USD | 121,950.00 USD | 0.00 USD | 22,580.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6290` | 100,200.00 USD | 100,200.00 USD | 20,690.00 USD | 7,350.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6290` | 170,760.00 USD | 170,760.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 148,420.00 USD | 148,420.00 USD | 25,290.00 USD | 3,430.00 USD | 19,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 222,050.00 USD | 222,050.00 USD | 30,590.00 USD | 0.00 USD | 20,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 234,840.00 USD | 234,840.00 USD | 39,760.00 USD | 8,860.00 USD | 37,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6310` | 233,600.00 USD | 233,600.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 310,080.00 USD | 310,080.00 USD | 51,560.00 USD | 9,600.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 352,150.00 USD | 352,150.00 USD | 14,490.00 USD | 12,370.00 USD | 15,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6330` | 291,880.00 USD | 291,880.00 USD | 57,940.00 USD | 0.00 USD | 336.25 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 428,640.00 USD | 428,640.00 USD | 31,480.00 USD | 4,250.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 302,700.00 USD | 302,700.00 USD | 10,730.00 USD | 0.00 USD | 95.88 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 492,290.00 USD | 492,290.00 USD | 54,290.00 USD | 5,510.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6350` | 372,120.00 USD | 372,120.00 USD | 69,190.00 USD | 0.00 USD | 230.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 593,170.00 USD | 593,170.00 USD | 54,290.00 USD | 5,880.00 USD | 40,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 428,970.00 USD | 428,970.00 USD | 0.00 USD | 0.00 USD | 56,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 612,180.00 USD | 612,180.00 USD | 0.00 USD | 3,950.00 USD | 15,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6370` | 438,460.00 USD | 438,460.00 USD | 0.00 USD | 0.00 USD | 9,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 701,690.00 USD | 701,690.00 USD | 45,820.00 USD | 25,640.00 USD | 18,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 515,540.00 USD | 515,540.00 USD | 32,220.00 USD | 0.00 USD | 44,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 767,650.00 USD | 767,650.00 USD | 8,220.00 USD | 7,210.00 USD | 50,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6390` | 568,600.00 USD | 568,600.00 USD | 24,230.00 USD | 15,680.00 USD | 13,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 884,810.00 USD | 884,810.00 USD | 66,560.00 USD | 37,130.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 588,440.00 USD | 588,440.00 USD | 19,270.00 USD | 0.00 USD | 569.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 944,800.00 USD | 944,800.00 USD | 29,560.00 USD | 14,660.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6410` | 612,990.00 USD | 612,990.00 USD | 0.00 USD | 18,210.00 USD | 6,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,030,000.00 USD | 1,030,000.00 USD | 55,880.00 USD | 9,980.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 724,470.00 USD | 724,470.00 USD | 55,350.00 USD | 26,560.00 USD | 29,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,090,000.00 USD | 1,090,000.00 USD | 24,220.00 USD | 12,130.00 USD | 28,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6430` | 776,560.00 USD | 776,560.00 USD | 31,500.00 USD | 7,140.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,200,000.00 USD | 1,200,000.00 USD | 36,460.00 USD | 14,890.00 USD | 56,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 843,750.00 USD | 843,750.00 USD | 34,270.00 USD | 17,680.00 USD | 15,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,300,000.00 USD | 1,300,000.00 USD | 62,440.00 USD | 14,460.00 USD | 21,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6450` | 976,210.00 USD | 976,210.00 USD | 81,220.00 USD | 15,560.00 USD | 35,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,340,000.00 USD | 1,340,000.00 USD | 25,640.00 USD | 12,810.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,200,000.00 USD | 1,200,000.00 USD | 91,390.00 USD | 31,070.00 USD | 102,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,430,000.00 USD | 1,430,000.00 USD | 57,900.00 USD | 17,750.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6470` | 1,250,000.00 USD | 1,250,000.00 USD | 9,660.00 USD | 26,520.00 USD | 9,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 209.47 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,520,000.00 USD | 1,520,000.00 USD | 78,190.00 USD | 9,530.00 USD | 373.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,360,000.00 USD | 1,360,000.00 USD | 94,210.00 USD | 0.00 USD | 23,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,590,000.00 USD | 1,590,000.00 USD | 52,900.00 USD | 2,940.00 USD | 12,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6490` | 1,420,000.00 USD | 1,420,000.00 USD | 36,340.00 USD | 0.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,660,000.00 USD | 1,660,000.00 USD | 55,160.00 USD | 9,280.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,590,000.00 USD | 1,590,000.00 USD | 53,330.00 USD | 0.00 USD | 121,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,730,000.00 USD | 1,730,000.00 USD | 58,460.00 USD | 0.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6510` | 1,870,000.00 USD | 1,870,000.00 USD | 244,480.00 USD | 8,270.00 USD | 18,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,840,000.00 USD | 1,840,000.00 USD | 93,550.00 USD | 13,800.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 2,020,000.00 USD | 2,020,000.00 USD | 65,690.00 USD | 6,720.00 USD | 86,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,870,000.00 USD | 1,870,000.00 USD | 18,010.00 USD | 3,910.00 USD | 11.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6530` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 4,440.00 USD | 47,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,900,000.00 USD | 1,900,000.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,110,000.00 USD | 2,110,000.00 USD | 15,730.00 USD | 0.00 USD | 14,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6550` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 458.49 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 5,380.00 USD | 562.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 4,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6570` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 6,350.00 USD | 198.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 21,920.00 USD | 9,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6590` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 11,320.00 USD | 339.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,950,000.00 USD | 1,950,000.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 7,100.00 USD | 127.46 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,950,000.00 USD | 1,950,000.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 2,180,000.00 USD | 2,180,000.00 USD | 8,600.00 USD | 0.00 USD | 540.47 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 507.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 1,970,000.00 USD | 1,970,000.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6630` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 502.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 1,980,000.00 USD | 1,980,000.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,220,000.00 USD | 2,220,000.00 USD | 33,660.00 USD | 0.00 USD | 6,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6650` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 6,770.00 USD | 133.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 395.59 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,030,000.00 USD | 2,030,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6670` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 238.68 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 158.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 666.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,070,000.00 USD | 2,070,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,120,000.00 USD | 2,120,000.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 2,320,000.00 USD | 2,320,000.00 USD | 58,470.00 USD | 0.00 USD | 30,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,120,000.00 USD | 2,120,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,160,000.00 USD | 2,160,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6730` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 132.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,240,000.00 USD | 2,240,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,360,000.00 USD | 2,360,000.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,280,000.00 USD | 2,280,000.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 75,730.00 USD | 68.35 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,300,000.00 USD | 2,300,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,340,000.00 USD | 2,340,000.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 2,550,000.00 USD | 2,550,000.00 USD | 63,600.00 USD | 4,190.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,400,000.00 USD | 2,400,000.00 USD | 33,610.00 USD | 11,780.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 12,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,440,000.00 USD | 2,440,000.00 USD | 2,940.00 USD | 18,610.00 USD | 13,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6795` | 62,650.00 USD | 62,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,450,000.00 USD | 2,450,000.00 USD | 4,540.00 USD | 686.25 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,600,000.00 USD | 2,600,000.00 USD | 6,120.00 USD | 0.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,470,000.00 USD | 2,470,000.00 USD | 4,670.00 USD | 2,460.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,520,000.00 USD | 2,520,000.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,680,000.00 USD | 2,680,000.00 USD | 32,570.00 USD | 37,730.00 USD | 73.84 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,600,000.00 USD | 2,600,000.00 USD | 26,250.00 USD | 15,380.00 USD | 36,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 17,730.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,670,000.00 USD | 2,670,000.00 USD | 45,780.00 USD | 13,660.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,900,000.00 USD | 2,900,000.00 USD | 57,890.00 USD | 36,580.00 USD | 54,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,730,000.00 USD | 2,730,000.00 USD | 29,890.00 USD | 6,280.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 2,940,000.00 USD | 2,940,000.00 USD | 24,240.00 USD | 4,710.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,790,000.00 USD | 2,790,000.00 USD | 42,050.00 USD | 4,600.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,980,000.00 USD | 2,980,000.00 USD | 32,660.00 USD | 9,830.00 USD | 209.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6870` | 2,860,000.00 USD | 2,860,000.00 USD | 63,220.00 USD | 1,160.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 3,000,000.00 USD | 3,000,000.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6880` | 2,910,000.00 USD | 2,910,000.00 USD | 20,970.00 USD | 11,390.00 USD | 14,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 3,040,000.00 USD | 3,040,000.00 USD | 24,610.00 USD | 17,300.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6890` | 2,920,000.00 USD | 2,920,000.00 USD | 1,180.00 USD | 0.00 USD | 8,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 3,060,000.00 USD | 3,060,000.00 USD | 4,850.00 USD | 12,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6900` | 2,960,000.00 USD | 2,960,000.00 USD | 18,600.00 USD | 4,990.00 USD | 21,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6910` | 3,000,000.00 USD | 3,000,000.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 3,190,000.00 USD | 3,190,000.00 USD | 69,620.00 USD | 2,090.00 USD | 37,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 3,270,000.00 USD | 3,270,000.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 3,320,000.00 USD | 3,320,000.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,350,000.00 USD | 3,350,000.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 3,370,000.00 USD | 3,370,000.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,400,000.00 USD | 3,400,000.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 3,440,000.00 USD | 3,440,000.00 USD | 13,410.00 USD | 0.00 USD | 30,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 63,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 63,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7945` | 365.88 USD | 63,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 82,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 83,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9145` | 21,920.00 USD | 105,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9155` | 3,070.00 USD | 108,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9735` | 17,180.00 USD | 125,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 125,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 151,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,200.00 USD | 156,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 82,060.00 USD | 238,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 239,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 242,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 242,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 242,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 243,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 796.83 USD | 243,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1415` | 250,160.00 USD | 0.00 USD | 283.00 USD | `-77.14%` | `2,000.00` |
| `Live` | `Long` | `0.1545` | 249,870.00 USD | 0.00 USD | 19,930.00 USD | `-75.04%` | `129,000.00` |
| `Live` | `Long` | `0.1875` | 229,940.00 USD | 0.00 USD | 269.27 USD | `-69.71%` | `1,436.09` |
| `Live` | `Long` | `0.1885` | 229,670.00 USD | 0.00 USD | 837.82 USD | `-69.55%` | `4,444.65` |
| `Live` | `Long` | `0.2205` | 228,830.00 USD | 0.00 USD | 228.91 USD | `-64.38%` | `1,038.12` |
| `Live` | `Long` | `0.2315` | 228,610.00 USD | 0.00 USD | 232.95 USD | `-62.60%` | `1,006.27` |
| `Live` | `Long` | `0.2325` | 228,370.00 USD | 0.00 USD | 2,620.00 USD | `-62.44%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 225,750.00 USD | 0.00 USD | 1,460.00 USD | `-60.82%` | `6,000.00` |
| `Live` | `Long` | `0.3175` | 224,290.00 USD | 0.00 USD | 1,590.00 USD | `-48.71%` | `5,000.00` |
| `Live` | `Long` | `0.3305` | 222,710.00 USD | 0.00 USD | 9,950.00 USD | `-46.61%` | `30,091.58` |
| `Live` | `Long` | `0.3545` | 212,760.00 USD | 0.00 USD | 177.25 USD | `-42.73%` | `500.00` |
| `Live` | `Long` | `0.3675` | 212,580.00 USD | 0.00 USD | 189.99 USD | `-40.63%` | `516.98` |
| `Live` | `Long` | `0.3725` | 212,390.00 USD | 0.00 USD | 558.75 USD | `-39.82%` | `1,500.00` |
| `Live` | `Long` | `0.3905` | 211,840.00 USD | 0.00 USD | 359.26 USD | `-36.91%` | `919.99` |
| `Live` | `Long` | `0.3955` | 211,480.00 USD | 0.00 USD | 2,640.00 USD | `-36.11%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 208,830.00 USD | 0.00 USD | 271.06 USD | `-35.46%` | `678.49` |
| `Live` | `Long` | `0.4055` | 208,560.00 USD | 0.00 USD | 283.85 USD | `-34.49%` | `700.00` |
| `Live` | `Long` | `0.4095` | 208,280.00 USD | 0.00 USD | 414.59 USD | `-33.84%` | `1,012.44` |
| `Live` | `Long` | `0.4125` | 207,860.00 USD | 0.00 USD | 1,070.00 USD | `-33.36%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 206,790.00 USD | 0.00 USD | 6,740.00 USD | `-33.20%` | `16,295.12` |
| `Live` | `Long` | `0.4185` | 200,050.00 USD | 0.00 USD | 630.86 USD | `-32.39%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 199,420.00 USD | 0.00 USD | 224.96 USD | `-31.26%` | `528.69` |
| `Live` | `Long` | `0.4375` | 199,200.00 USD | 0.00 USD | 31,060.00 USD | `-29.32%` | `71,004.49` |
| `Live` | `Long` | `0.4385` | 168,130.00 USD | 0.00 USD | 824.98 USD | `-29.16%` | `1,881.36` |
| `Live` | `Long` | `0.4475` | 167,310.00 USD | 0.00 USD | 226.63 USD | `-27.71%` | `506.43` |
| `Live` | `Long` | `0.4525` | 167,080.00 USD | 0.00 USD | 27,150.00 USD | `-26.90%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 139,930.00 USD | 0.00 USD | 5,530.00 USD | `-26.74%` | `12,191.83` |
| `Live` | `Long` | `0.4605` | 134,400.00 USD | 0.00 USD | 125.38 USD | `-25.61%` | `272.27` |
| `Live` | `Long` | `0.4615` | 134,280.00 USD | 0.00 USD | 901.90 USD | `-25.44%` | `1,954.27` |
| `Live` | `Long` | `0.4625` | 133,370.00 USD | 0.00 USD | 5,730.00 USD | `-25.28%` | `12,399.59` |
| `Live` | `Long` | `0.4645` | 127,640.00 USD | 0.00 USD | 876.05 USD | `-24.96%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 126,760.00 USD | 0.00 USD | 468.50 USD | `-24.31%` | `1,000.00` |
| `Live` | `Long` | `0.4715` | 126,290.00 USD | 0.00 USD | 188.60 USD | `-23.83%` | `400.00` |
| `Live` | `Long` | `0.4835` | 126,110.00 USD | 0.00 USD | 135.33 USD | `-21.89%` | `279.90` |
| `Live` | `Long` | `0.4855` | 125,970.00 USD | 0.00 USD | 181.88 USD | `-21.57%` | `374.62` |
| `Live` | `Long` | `0.4865` | 125,790.00 USD | 0.00 USD | 3,170.00 USD | `-21.41%` | `6,508.47` |
| `Live` | `Long` | `0.4895` | 122,620.00 USD | 0.00 USD | 165.94 USD | `-20.92%` | `339.00` |
| `Live` | `Long` | `0.4925` | 122,460.00 USD | 0.00 USD | 10,520.00 USD | `-20.44%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 111,930.00 USD | 0.00 USD | 1,580.00 USD | `-20.27%` | `3,199.85` |
| `Live` | `Long` | `0.4955` | 110,350.00 USD | 0.00 USD | 3,180.00 USD | `-19.95%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 107,170.00 USD | 0.00 USD | 143.19 USD | `-19.79%` | `288.40` |
| `Live` | `Long` | `0.4975` | 107,030.00 USD | 0.00 USD | 667.49 USD | `-19.63%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 106,360.00 USD | 0.00 USD | 429.90 USD | `-19.47%` | `862.38` |
| `Live` | `Long` | `0.5075` | 105,930.00 USD | 0.00 USD | 303.42 USD | `-18.01%` | `597.87` |
| `Live` | `Long` | `0.5085` | 105,630.00 USD | 0.00 USD | 102.82 USD | `-17.85%` | `202.20` |
| `Live` | `Long` | `0.5105` | 105,530.00 USD | 0.00 USD | 519.77 USD | `-17.53%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 105,010.00 USD | 0.00 USD | 248.05 USD | `-17.21%` | `484.00` |
| `Live` | `Long` | `0.5135` | 104,760.00 USD | 0.00 USD | 298.60 USD | `-17.04%` | `581.49` |
| `Live` | `Long` | `0.5175` | 104,460.00 USD | 0.00 USD | 9,440.00 USD | `-16.40%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 95,010.00 USD | 0.00 USD | 281.56 USD | `-16.24%` | `543.02` |
| `Live` | `Long` | `0.5295` | 94,730.00 USD | 0.00 USD | 1,840.00 USD | `-14.46%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 92,900.00 USD | 0.00 USD | 11,510.00 USD | `-14.14%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 81,380.00 USD | 0.00 USD | 2,260.00 USD | `-13.97%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 79,120.00 USD | 0.00 USD | 163.22 USD | `-13.81%` | `305.95` |
| `Live` | `Long` | `0.5445` | 78,960.00 USD | 0.00 USD | 855.28 USD | `-12.04%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 78,110.00 USD | 0.00 USD | 1,630.00 USD | `-11.55%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 76,480.00 USD | 0.00 USD | 47,450.00 USD | `-10.42%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 29,030.00 USD | 0.00 USD | 10,520.00 USD | `-9.77%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 18,510.00 USD | 0.00 USD | 258.48 USD | `-9.29%` | `460.33` |
| `Live` | `Long` | `0.5635` | 18,250.00 USD | 0.00 USD | 244.90 USD | `-8.97%` | `434.61` |
| `Live` | `Long` | `0.5655` | 18,000.00 USD | 0.00 USD | 1,920.00 USD | `-8.64%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 16,080.00 USD | 0.00 USD | 1,370.00 USD | `-8.48%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 14,710.00 USD | 0.00 USD | 289.08 USD | `-7.67%` | `505.82` |
| `Live` | `Long` | `0.5745` | 14,420.00 USD | 0.00 USD | 218.30 USD | `-7.19%` | `379.98` |
| `Live` | `Long` | `0.5885` | 14,210.00 USD | 0.00 USD | 8,900.00 USD | `-4.93%` | `15,117.28` |
| `Live` | `Long` | `0.5915` | 5,310.00 USD | 0.00 USD | 5,310.00 USD | `-4.44%` | `8,975.06` |
| `Live` | `Short` | `0.6475` | 209.47 USD | 209.47 USD | 0.00 USD | `+4.60%` | `323.51` |
| `Live` | `Short` | `0.6795` | 62,860.00 USD | 62,650.00 USD | 0.00 USD | `+9.77%` | `92,204.70` |
| `Live` | `Short` | `0.7245` | 63,230.00 USD | 364.39 USD | 0.00 USD | `+17.04%` | `502.96` |
| `Live` | `Short` | `0.7725` | 63,390.00 USD | 165.62 USD | 0.00 USD | `+24.80%` | `214.40` |
| `Live` | `Short` | `0.7945` | 63,760.00 USD | 365.88 USD | 0.00 USD | `+28.35%` | `460.51` |
| `Live` | `Short` | `0.8005` | 82,880.00 USD | 19,120.00 USD | 0.00 USD | `+29.32%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 83,260.00 USD | 378.95 USD | 0.00 USD | `+39.98%` | `437.33` |
| `Live` | `Short` | `0.9145` | 105,170.00 USD | 21,920.00 USD | 0.00 USD | `+47.74%` | `23,964.69` |
| `Live` | `Short` | `0.9155` | 108,240.00 USD | 3,070.00 USD | 0.00 USD | `+47.90%` | `3,354.34` |
| `Live` | `Short` | `0.9735` | 125,420.00 USD | 17,180.00 USD | 0.00 USD | `+57.27%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 125,590.00 USD | 166.01 USD | 0.00 USD | `+60.50%` | `167.10` |
| `Live` | `Short` | `1.02` | 151,560.00 USD | 25,970.00 USD | 0.00 USD | `+65.02%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 156,760.00 USD | 5,200.00 USD | 0.00 USD | `+67.93%` | `5,000.00` |
| `Live` | `Short` | `1.08` | 238,820.00 USD | 82,060.00 USD | 0.00 USD | `+73.75%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 239,300.00 USD | 479.74 USD | 0.00 USD | `+76.33%` | `439.52` |
| `Live` | `Short` | `1.12` | 242,100.00 USD | 2,800.00 USD | 0.00 USD | `+80.86%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 242,600.00 USD | 501.44 USD | 0.00 USD | `+89.58%` | `427.30` |
| `Live` | `Short` | `1.19` | 242,820.00 USD | 227.46 USD | 0.00 USD | `+91.68%` | `191.71` |
| `Live` | `Short` | `1.19` | 243,020.00 USD | 199.98 USD | 0.00 USD | `+92.00%` | `168.26` |
| `Live` | `Short` | `1.22` | 243,820.00 USD | 796.83 USD | 0.00 USD | `+97.33%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 199,490.00 USD | 0.00 USD | 340.19 USD | `-43.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 199,150.00 USD | 0.00 USD | 104.57 USD | `-25.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 199,040.00 USD | 0.00 USD | 111.62 USD | `-19.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 198,930.00 USD | 0.00 USD | 111.85 USD | `-19.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 198,820.00 USD | 0.00 USD | 67,850.00 USD | `-19.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 130,970.00 USD | 0.00 USD | 112.97 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 130,860.00 USD | 0.00 USD | 225.65 USD | `-18.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 130,640.00 USD | 0.00 USD | 101.97 USD | `-17.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 130,530.00 USD | 0.00 USD | 111.69 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 130,420.00 USD | 0.00 USD | 5,380.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 125,040.00 USD | 0.00 USD | 115.47 USD | `-16.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 124,930.00 USD | 0.00 USD | 116.58 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 124,810.00 USD | 0.00 USD | 116.96 USD | `-16.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 124,690.00 USD | 0.00 USD | 539.96 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 124,150.00 USD | 0.00 USD | 117.70 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 124,030.00 USD | 0.00 USD | 117.93 USD | `-15.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 123,920.00 USD | 0.00 USD | 770.19 USD | `-14.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 123,150.00 USD | 0.00 USD | 8,750.00 USD | `-12.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 114,390.00 USD | 0.00 USD | 8,150.00 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 106,240.00 USD | 0.00 USD | 4,500.00 USD | `-11.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 101,740.00 USD | 0.00 USD | 126.71 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 101,620.00 USD | 0.00 USD | 126.90 USD | `-10.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 101,490.00 USD | 0.00 USD | 57,800.00 USD | `-10.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 43,690.00 USD | 0.00 USD | 173.58 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 43,520.00 USD | 0.00 USD | 10,540.00 USD | `-9.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 32,980.00 USD | 0.00 USD | 339.84 USD | `-9.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 32,640.00 USD | 0.00 USD | 930.52 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 31,710.00 USD | 0.00 USD | 127.62 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 31,580.00 USD | 0.00 USD | 127.30 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 31,450.00 USD | 0.00 USD | 9,410.00 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 22,040.00 USD | 0.00 USD | 127.63 USD | `-7.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 21,910.00 USD | 0.00 USD | 151.62 USD | `-7.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 21,760.00 USD | 0.00 USD | 999.82 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 20,760.00 USD | 0.00 USD | 1,710.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 19,050.00 USD | 0.00 USD | 127.36 USD | `-6.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 18,920.00 USD | 0.00 USD | 780.04 USD | `-6.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 18,140.00 USD | 0.00 USD | 127.27 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 18,010.00 USD | 0.00 USD | 999.65 USD | `-5.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 17,010.00 USD | 0.00 USD | 533.37 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 16,480.00 USD | 0.00 USD | 8,930.00 USD | `-4.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 7,550.00 USD | 0.00 USD | 265.69 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 7,290.00 USD | 0.00 USD | 597.80 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 6,690.00 USD | 0.00 USD | 509.04 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 6,180.00 USD | 0.00 USD | 953.02 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 5,230.00 USD | 0.00 USD | 999.99 USD | `-2.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 4,230.00 USD | 0.00 USD | 1,910.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6075` | 2,320.00 USD | 0.00 USD | 389.92 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 1,930.00 USD | 0.00 USD | 301.32 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 1,630.00 USD | 0.00 USD | 629.83 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 998.49 USD | 0.00 USD | 410.30 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6175` | 588.19 USD | 0.00 USD | 588.19 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 1,120.00 USD | 1,120.00 USD | 0.00 USD | `+0.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 2,120.00 USD | 1,000.00 USD | 0.00 USD | `+0.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 2,560.00 USD | 433.11 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 3,030.00 USD | 469.94 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 7,450.00 USD | 4,430.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 7,720.00 USD | 269.44 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 16,120.00 USD | 8,390.00 USD | 0.00 USD | `+2.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 17,320.00 USD | 1,200.00 USD | 0.00 USD | `+3.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 27,000.00 USD | 9,680.00 USD | 0.00 USD | `+3.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6415` | 34,600.00 USD | 7,600.00 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6425` | 40,480.00 USD | 5,880.00 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 45,770.00 USD | 5,300.00 USD | 0.00 USD | `+4.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 55,750.00 USD | 9,980.00 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 56,320.00 USD | 567.58 USD | 0.00 USD | `+5.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 56,490.00 USD | 172.51 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 60,570.00 USD | 4,080.00 USD | 0.00 USD | `+5.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 62,010.00 USD | 1,440.00 USD | 0.00 USD | `+6.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 62,590.00 USD | 580.23 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 62,880.00 USD | 289.66 USD | 0.00 USD | `+7.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 63,140.00 USD | 262.60 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 63,430.00 USD | 283.50 USD | 0.00 USD | `+7.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 63,590.00 USD | 162.91 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6735` | 63,900.00 USD | 310.15 USD | 0.00 USD | `+8.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 64,500.00 USD | 598.31 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 64,650.00 USD | 154.30 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 64,870.00 USD | 214.20 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 75,430.00 USD | 10,560.00 USD | 0.00 USD | `+10.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 76,560.00 USD | 1,130.00 USD | 0.00 USD | `+10.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 76,700.00 USD | 140.41 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 77,210.00 USD | 514.80 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 77,320.00 USD | 101.96 USD | 0.00 USD | `+11.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 78,340.00 USD | 1,020.00 USD | 0.00 USD | `+11.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 78,950.00 USD | 610.10 USD | 0.00 USD | `+12.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 79,050.00 USD | 101.38 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 79,840.00 USD | 789.18 USD | 0.00 USD | `+12.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 79,940.00 USD | 102.99 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 80,050.00 USD | 111.08 USD | 0.00 USD | `+13.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 80,750.00 USD | 694.49 USD | 0.00 USD | `+13.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 80,880.00 USD | 132.99 USD | 0.00 USD | `+14.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 81,000.00 USD | 122.04 USD | 0.00 USD | `+14.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 82,840.00 USD | 1,830.00 USD | 0.00 USD | `+15.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 83,020.00 USD | 183.26 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 83,170.00 USD | 147.15 USD | 0.00 USD | `+16.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 89,460.00 USD | 6,290.00 USD | 0.00 USD | `+17.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 89,770.00 USD | 309.91 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 89,930.00 USD | 165.17 USD | 0.00 USD | `+18.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 90,960.00 USD | 1,030.00 USD | 0.00 USD | `+18.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 91,690.00 USD | 733.09 USD | 0.00 USD | `+19.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 91,880.00 USD | 185.43 USD | 0.00 USD | `+20.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 94,050.00 USD | 2,170.00 USD | 0.00 USD | `+20.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 94,360.00 USD | 318.43 USD | 0.00 USD | `+20.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 94,510.00 USD | 141.39 USD | 0.00 USD | `+21.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 98,620.00 USD | 4,120.00 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 99,130.00 USD | 511.82 USD | 0.00 USD | `+22.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 100,010.00 USD | 875.23 USD | 0.00 USD | `+23.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 100,110.00 USD | 103.35 USD | 0.00 USD | `+23.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 100,240.00 USD | 127.48 USD | 0.00 USD | `+23.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 100,340.00 USD | 101.61 USD | 0.00 USD | `+23.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 100,530.00 USD | 186.97 USD | 0.00 USD | `+24.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 100,640.00 USD | 109.43 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 100,800.00 USD | 166.70 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 101,940.00 USD | 1,140.00 USD | 0.00 USD | `+26.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 108,250.00 USD | 6,310.00 USD | 0.00 USD | `+27.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 120,330.00 USD | 12,070.00 USD | 0.00 USD | `+31.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 121,980.00 USD | 1,650.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 122,910.00 USD | 929.08 USD | 0.00 USD | `+34.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 163,500.00 USD | 40,590.00 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 180,240.00 USD | 16,740.00 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 192,960.00 USD | 12,720.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 204,740.00 USD | 11,780.00 USD | 0.00 USD | `+37.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8555` | 204,850.00 USD | 108.85 USD | 0.00 USD | `+38.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 205,010.00 USD | 159.86 USD | 0.00 USD | `+40.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 205,710.00 USD | 702.20 USD | 0.00 USD | `+45.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 205,900.00 USD | 193.62 USD | 0.00 USD | `+46.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 206,330.00 USD | 424.63 USD | 0.00 USD | `+51.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 209,120.00 USD | 2,790.00 USD | 0.00 USD | `+51.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 209,460.00 USD | 340.54 USD | 0.00 USD | `+53.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 209,570.00 USD | 108.83 USD | 0.00 USD | `+55.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 209,710.00 USD | 145.72 USD | 0.00 USD | `+56.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 211,750.00 USD | 2,030.00 USD | 0.00 USD | `+59.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 211,880.00 USD | 136.10 USD | 0.00 USD | `+61.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 212,430.00 USD | 550.48 USD | 0.00 USD | `+61.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 212,750.00 USD | 314.99 USD | 0.00 USD | `+65.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 213,350.00 USD | 602.17 USD | 0.00 USD | `+69.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 213,710.00 USD | 360.61 USD | 0.00 USD | `+71.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 214,650.00 USD | 942.77 USD | 0.00 USD | `+74.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 215,050.00 USD | 397.19 USD | 0.00 USD | `+77.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.23` | 215,580.00 USD | 525.37 USD | 0.00 USD | `+98.63%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5220` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `0.5260` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.5270` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `0.5290` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,560.00 USD | 0.00 USD | 2,270.00 USD |
| `7D` | `0.5300` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,560.00 USD | 0.00 USD | 6,810.00 USD |
| `7D` | `0.5310` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 8,680.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5320` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5330` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5350` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `7D` | `0.5360` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 44.79 USD |
| `7D` | `0.5370` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 0.00 USD | 1,550.00 USD | 2,900.00 USD |
| `7D` | `0.5390` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 80.65 USD |
| `7D` | `0.5400` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `0.5410` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD |
| `7D` | `0.5420` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,860.00 USD |
| `7D` | `0.5430` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 627.61 USD | 4,910.00 USD |
| `7D` | `0.5440` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 523.59 USD | 8,750.00 USD |
| `7D` | `0.5450` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 2,250.00 USD | 0.00 USD | 2,020.00 USD |
| `7D` | `0.5460` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 3,030.00 USD | 3,140.00 USD |
| `7D` | `0.5470` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 0.00 USD | 795.70 USD | 17.38 USD |
| `7D` | `0.5480` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,000.00 USD | 0.00 USD | 4,460.00 USD |
| `7D` | `0.5490` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 2,100.00 USD | 474.54 USD | 2,140.00 USD |
| `7D` | `0.5500` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 3,890.00 USD | 967.07 USD | 4,650.00 USD |
| `7D` | `0.5510` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,960.00 USD |
| `7D` | `0.5520` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,380.00 USD | 0.00 USD | 24.91 USD |
| `7D` | `0.5530` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 1,650.00 USD | 1,150.00 USD | 12,780.00 USD |
| `1D` | `0.5540` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 6,650.00 USD | 7,160.00 USD | 4,250.00 USD |
| `7D` | `0.5540` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 11,190.00 USD | 6,110.00 USD | 5,760.00 USD |
| `1D` | `0.5550` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,940.00 USD | 0.00 USD | 2,790.00 USD |
| `7D` | `0.5550` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,270.00 USD |
| `1D` | `0.5560` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 4,540.00 USD | 686.25 USD | 1,730.00 USD |
| `7D` | `0.5560` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 12,540.00 USD | 0.00 USD | 7,690.00 USD |
| `1D` | `0.5570` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 4,670.00 USD | 2,460.00 USD | 7,630.00 USD |
| `7D` | `0.5570` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 812.74 USD | 3,260.00 USD |
| `1D` | `0.5580` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD |
| `7D` | `0.5580` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,110.00 USD |
| `1D` | `0.5590` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,670.00 USD | 2,150.00 USD | 1,370.00 USD |
| `7D` | `0.5590` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 2,660.00 USD | 7,220.00 USD | 2,460.00 USD |
| `1D` | `0.5600` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD |
| `7D` | `0.5600` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 1,410.00 USD | 938.63 USD | 15.87 USD |
| `1D` | `0.5610` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 2,240.00 USD | 500.33 USD | 823.46 USD |
| `7D` | `0.5610` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 13,590.00 USD | 1,960.00 USD | 7,910.00 USD |
| `1D` | `0.5620` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 1,800.00 USD | 995.72 USD | 2,180.00 USD |
| `7D` | `0.5620` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,740.00 USD |
| `1D` | `0.5630` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,090.00 USD |
| `7D` | `0.5630` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 14,240.00 USD | 2,380.00 USD | 2,900.00 USD |
| `1D` | `0.5640` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD |
| `7D` | `0.5640` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 24.47 USD |
| `1D` | `0.5650` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5650` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD |
| `1D` | `0.5660` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `0.5660` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,170.00 USD |
| `7D` | `0.5670` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 0.00 USD | 2,900.00 USD |
| `7D` | `0.5680` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 5,100.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5690` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `7D` | `0.5690` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 0.00 USD | 107.84 USD |
| `1D` | `0.5700` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.5700` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5710` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 2,850.00 USD | 1,560.00 USD |
| `1D` | `0.5720` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `7D` | `0.5720` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 1,520.00 USD | 10,590.00 USD |
| `1D` | `0.5730` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.5730` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 2,690.00 USD | 528.82 USD | 185.80 USD |
| `1D` | `0.5740` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD |
| `7D` | `0.5740` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 18,940.00 USD | 574.82 USD | 1,470.00 USD |
| `1D` | `0.5750` | 1,280,000.00 USD | 0.00 USD | 1,280,000.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD |
| `1D` | `0.5760` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD |
| `7D` | `0.5760` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,150.00 USD | 7,300.00 USD | 28.00 USD |
| `1D` | `0.5770` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD |
| `7D` | `0.5770` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 21,510.00 USD | 0.00 USD | 146.30 USD |
| `1D` | `0.5780` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD |
| `7D` | `0.5780` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 19,410.00 USD | 0.00 USD | 1,630.00 USD |
| `1D` | `0.5790` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `7D` | `0.5790` | 996,470.00 USD | 0.00 USD | 996,470.00 USD | 1,610.00 USD | 0.00 USD | 11,110.00 USD |
| `1D` | `0.5800` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD |
| `7D` | `0.5800` | 983,750.00 USD | 0.00 USD | 983,750.00 USD | 0.00 USD | 3,900.00 USD | 16,790.00 USD |
| `1D` | `0.5810` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD |
| `7D` | `0.5810` | 963,060.00 USD | 0.00 USD | 963,060.00 USD | 0.00 USD | 0.00 USD | 3,360.00 USD |
| `1D` | `0.5820` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD |
| `7D` | `0.5820` | 959,700.00 USD | 0.00 USD | 959,700.00 USD | 0.00 USD | 0.00 USD | 3,530.00 USD |
| `1D` | `0.5830` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD |
| `1D` | `0.5840` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 2,190.00 USD | 4,300.00 USD |
| `7D` | `0.5840` | 956,160.00 USD | 0.00 USD | 956,160.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD |
| `1D` | `0.5850` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD |
| `1D` | `0.5860` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,880.00 USD |
| `1D` | `0.5870` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.5870` | 935,010.00 USD | 0.00 USD | 935,010.00 USD | 0.00 USD | 1,400.00 USD | 195.16 USD |
| `1D` | `0.5880` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 33,380.00 USD | 8,680.00 USD | 7,790.00 USD |
| `7D` | `0.5880` | 933,410.00 USD | 0.00 USD | 933,410.00 USD | 3,110.00 USD | 14,610.00 USD | 211.49 USD |
| `1D` | `0.5890` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 34,810.00 USD | 11,450.00 USD | 0.00 USD |
| `7D` | `0.5890` | 915,480.00 USD | 0.00 USD | 915,480.00 USD | 43,020.00 USD | 0.00 USD | 163.05 USD |
| `1D` | `0.5900` | 966,260.00 USD | 0.00 USD | 966,260.00 USD | 24,340.00 USD | 12,640.00 USD | 10,140.00 USD |
| `7D` | `0.5900` | 872,290.00 USD | 0.00 USD | 872,290.00 USD | 61,220.00 USD | 1,560.00 USD | 0.00 USD |
| `1D` | `0.5910` | 919,130.00 USD | 0.00 USD | 919,130.00 USD | 26,100.00 USD | 12,590.00 USD | 19,290.00 USD |
| `7D` | `0.5910` | 809,520.00 USD | 0.00 USD | 809,520.00 USD | 0.00 USD | 9,340.00 USD | 16,520.00 USD |
| `1D` | `0.5920` | 861,150.00 USD | 0.00 USD | 861,150.00 USD | 25,360.00 USD | 6,570.00 USD | 9,970.00 USD |
| `7D` | `0.5920` | 783,660.00 USD | 0.00 USD | 783,660.00 USD | 11,690.00 USD | 10,620.00 USD | 58,810.00 USD |
| `1D` | `0.5930` | 819,240.00 USD | 0.00 USD | 819,240.00 USD | 11,360.00 USD | 6,380.00 USD | 18,090.00 USD |
| `7D` | `0.5930` | 702,530.00 USD | 0.00 USD | 702,530.00 USD | 25,390.00 USD | 0.00 USD | 10,500.00 USD |
| `1D` | `0.5940` | 783,410.00 USD | 0.00 USD | 783,410.00 USD | 24,760.00 USD | 2,040.00 USD | 16,430.00 USD |
| `7D` | `0.5940` | 666,640.00 USD | 0.00 USD | 666,640.00 USD | 5,780.00 USD | 0.00 USD | 46.83 USD |
| `1D` | `0.5950` | 740,180.00 USD | 0.00 USD | 740,180.00 USD | 37,990.00 USD | 4,980.00 USD | 1,640.00 USD |
| `7D` | `0.5950` | 660,820.00 USD | 0.00 USD | 660,820.00 USD | 13,060.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5960` | 695,580.00 USD | 0.00 USD | 695,580.00 USD | 12,270.00 USD | 2,560.00 USD | 8,580.00 USD |
| `7D` | `0.5960` | 647,760.00 USD | 0.00 USD | 647,760.00 USD | 5,120.00 USD | 18,410.00 USD | 0.00 USD |
| `1D` | `0.5970` | 672,170.00 USD | 0.00 USD | 672,170.00 USD | 12,870.00 USD | 532.93 USD | 5,180.00 USD |
| `1D` | `0.5980` | 653,590.00 USD | 0.00 USD | 653,590.00 USD | 15,950.00 USD | 4,300.00 USD | 54.42 USD |
| `7D` | `0.5980` | 624,230.00 USD | 0.00 USD | 624,230.00 USD | 37,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5990` | 633,290.00 USD | 0.00 USD | 633,290.00 USD | 6,880.00 USD | 1,700.00 USD | 1,100.00 USD |
| `7D` | `0.5990` | 586,410.00 USD | 0.00 USD | 586,410.00 USD | 3,320.00 USD | 0.00 USD | 247.18 USD |
| `1D` | `0.6000` | 623,610.00 USD | 0.00 USD | 623,610.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD |
| `7D` | `0.6000` | 582,840.00 USD | 0.00 USD | 582,840.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD |
| `1D` | `0.6010` | 586,470.00 USD | 0.00 USD | 586,470.00 USD | 2,960.00 USD | 6,370.00 USD | 5,020.00 USD |
| `7D` | `0.6010` | 554,780.00 USD | 0.00 USD | 554,780.00 USD | 12,110.00 USD | 4,090.00 USD | 0.00 USD |
| `1D` | `0.6020` | 572,110.00 USD | 0.00 USD | 572,110.00 USD | 2,680.00 USD | 8,040.00 USD | 1,720.00 USD |
| `7D` | `0.6020` | 538,580.00 USD | 0.00 USD | 538,580.00 USD | 0.00 USD | 7,150.00 USD | 0.00 USD |
| `1D` | `0.6030` | 559,670.00 USD | 0.00 USD | 559,670.00 USD | 40,580.00 USD | 14,050.00 USD | 3,630.00 USD |
| `7D` | `0.6030` | 531,430.00 USD | 0.00 USD | 531,430.00 USD | 38,530.00 USD | 0.00 USD | 139.74 USD |
| `1D` | `0.6040` | 501,400.00 USD | 0.00 USD | 501,400.00 USD | 6,530.00 USD | 9,900.00 USD | 7,580.00 USD |
| `7D` | `0.6040` | 492,760.00 USD | 0.00 USD | 492,760.00 USD | 0.00 USD | 18,680.00 USD | 0.00 USD |
| `1D` | `0.6050` | 477,400.00 USD | 0.00 USD | 477,400.00 USD | 20,690.00 USD | 2,140.00 USD | 13,690.00 USD |
| `7D` | `0.6050` | 474,080.00 USD | 0.00 USD | 474,080.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD |
| `1D` | `0.6060` | 440,870.00 USD | 0.00 USD | 440,870.00 USD | 22,710.00 USD | 0.00 USD | 10,290.00 USD |
| `7D` | `0.6060` | 453,270.00 USD | 0.00 USD | 453,270.00 USD | 30,590.00 USD | 0.00 USD | 20,760.00 USD |
| `1D` | `0.6070` | 407,870.00 USD | 0.00 USD | 407,870.00 USD | 27,430.00 USD | 4,080.00 USD | 16,080.00 USD |
| `7D` | `0.6070` | 401,920.00 USD | 0.00 USD | 401,920.00 USD | 11,560.00 USD | 0.00 USD | 161.30 USD |
| `1D` | `0.6080` | 360,280.00 USD | 0.00 USD | 360,280.00 USD | 26,190.00 USD | 6,680.00 USD | 3,080.00 USD |
| `7D` | `0.6080` | 390,200.00 USD | 0.00 USD | 390,200.00 USD | 2,860.00 USD | 0.00 USD | 30,400.00 USD |
| `1D` | `0.6090` | 324,330.00 USD | 0.00 USD | 324,330.00 USD | 11,540.00 USD | 3,030.00 USD | 0.00 USD |
| `7D` | `0.6090` | 356,940.00 USD | 0.00 USD | 356,940.00 USD | 13,920.00 USD | 44,860.00 USD | 25,120.00 USD |
| `1D` | `0.6100` | 309,760.00 USD | 0.00 USD | 309,760.00 USD | 3,470.00 USD | 1,070.00 USD | 41,540.00 USD |
| `7D` | `0.6100` | 273,040.00 USD | 0.00 USD | 273,040.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD |
| `1D` | `0.6110` | 263,680.00 USD | 0.00 USD | 263,680.00 USD | 27,240.00 USD | 7,190.00 USD | 0.00 USD |
| `7D` | `0.6110` | 262,990.00 USD | 0.00 USD | 262,990.00 USD | 34,870.00 USD | 2,210.00 USD | 12,860.00 USD |
| `1D` | `0.6120` | 229,250.00 USD | 0.00 USD | 229,250.00 USD | 43,790.00 USD | 3,410.00 USD | 2,170.00 USD |
| `7D` | `0.6120` | 213,040.00 USD | 0.00 USD | 213,040.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD |
| `1D` | `0.6130` | 179,880.00 USD | 0.00 USD | 179,880.00 USD | 85,200.00 USD | 6,720.00 USD | 40,120.00 USD |
| `7D` | `0.6130` | 156,500.00 USD | 0.00 USD | 156,500.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD |
| `1D` | `0.6140` | 47,840.00 USD | 0.00 USD | 47,840.00 USD | 6,130.00 USD | 9,520.00 USD | 19,180.00 USD |
| `7D` | `0.6140` | 22,770.00 USD | 0.00 USD | 22,770.00 USD | 0.00 USD | 6,170.00 USD | 45.18 USD |
| `1D` | `0.6150` | 12,990.00 USD | 0.00 USD | 12,990.00 USD | 12,990.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6150` | 16,560.00 USD | 0.00 USD | 16,560.00 USD | 0.00 USD | 0.00 USD | 16,560.00 USD |
| `1D` | `0.6160` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6160` | 147.01 USD | 147.01 USD | 0.00 USD | 0.00 USD | 0.00 USD | 147.01 USD |
| `7D` | `0.6160` | 294.02 USD | 294.02 USD | 0.00 USD | 0.00 USD | 0.00 USD | 147.01 USD |
| `7D` | `0.6170` | 424.25 USD | 424.25 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.23 USD |
| `1D` | `0.6180` | 1,760.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `1D` | `0.6200` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.92 USD |
| `7D` | `0.6200` | 43,430.00 USD | 43,430.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 29,140.00 USD |
| `7D` | `0.6210` | 66,240.00 USD | 66,240.00 USD | 0.00 USD | 0.00 USD | 22,640.00 USD | 168.33 USD |
| `7D` | `0.6220` | 66,360.00 USD | 66,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 118.28 USD |
| `7D` | `0.6230` | 66,430.00 USD | 66,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 66.51 USD |
| `7D` | `0.6240` | 73,930.00 USD | 73,930.00 USD | 0.00 USD | 0.00 USD | 7,300.00 USD | 199.73 USD |
| `7D` | `0.6250` | 74,230.00 USD | 74,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 303.07 USD |
| `1D` | `0.6260` | 10,180.00 USD | 10,180.00 USD | 0.00 USD | 0.00 USD | 8,370.00 USD | 0.00 USD |
| `7D` | `0.6260` | 74,460.00 USD | 74,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 229.50 USD |
| `7D` | `0.6270` | 82,720.00 USD | 82,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,260.00 USD |
| `1D` | `0.6280` | 52,000.00 USD | 52,000.00 USD | 0.00 USD | 0.00 USD | 16,420.00 USD | 25,400.00 USD |
| `7D` | `0.6280` | 121,950.00 USD | 121,950.00 USD | 0.00 USD | 0.00 USD | 22,580.00 USD | 16,650.00 USD |
| `1D` | `0.6290` | 100,200.00 USD | 100,200.00 USD | 0.00 USD | 20,690.00 USD | 7,350.00 USD | 20,170.00 USD |
| `7D` | `0.6290` | 170,760.00 USD | 170,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD |
| `1D` | `0.6300` | 148,420.00 USD | 148,420.00 USD | 0.00 USD | 25,290.00 USD | 3,430.00 USD | 19,500.00 USD |
| `7D` | `0.6300` | 222,050.00 USD | 222,050.00 USD | 0.00 USD | 30,590.00 USD | 0.00 USD | 20,700.00 USD |
| `1D` | `0.6310` | 234,840.00 USD | 234,840.00 USD | 0.00 USD | 39,760.00 USD | 8,860.00 USD | 37,790.00 USD |
| `7D` | `0.6310` | 233,600.00 USD | 233,600.00 USD | 0.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6320` | 310,080.00 USD | 310,080.00 USD | 0.00 USD | 51,560.00 USD | 9,600.00 USD | 14,080.00 USD |
| `1D` | `0.6330` | 352,150.00 USD | 352,150.00 USD | 0.00 USD | 14,490.00 USD | 12,370.00 USD | 15,210.00 USD |
| `7D` | `0.6330` | 291,880.00 USD | 291,880.00 USD | 0.00 USD | 57,940.00 USD | 0.00 USD | 336.25 USD |
| `1D` | `0.6340` | 428,640.00 USD | 428,640.00 USD | 0.00 USD | 31,480.00 USD | 4,250.00 USD | 40,770.00 USD |
| `7D` | `0.6340` | 302,700.00 USD | 302,700.00 USD | 0.00 USD | 10,730.00 USD | 0.00 USD | 95.88 USD |
| `1D` | `0.6350` | 492,290.00 USD | 492,290.00 USD | 0.00 USD | 54,290.00 USD | 5,510.00 USD | 3,850.00 USD |
| `7D` | `0.6350` | 372,120.00 USD | 372,120.00 USD | 0.00 USD | 69,190.00 USD | 0.00 USD | 230.59 USD |
| `1D` | `0.6360` | 593,170.00 USD | 593,170.00 USD | 0.00 USD | 54,290.00 USD | 5,880.00 USD | 40,710.00 USD |
| `7D` | `0.6360` | 428,970.00 USD | 428,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,850.00 USD |
| `1D` | `0.6370` | 612,180.00 USD | 612,180.00 USD | 0.00 USD | 0.00 USD | 3,950.00 USD | 15,060.00 USD |
| `7D` | `0.6370` | 438,460.00 USD | 438,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,480.00 USD |
| `1D` | `0.6380` | 701,690.00 USD | 701,690.00 USD | 0.00 USD | 45,820.00 USD | 25,640.00 USD | 18,040.00 USD |
| `7D` | `0.6380` | 515,540.00 USD | 515,540.00 USD | 0.00 USD | 32,220.00 USD | 0.00 USD | 44,870.00 USD |
| `1D` | `0.6390` | 767,650.00 USD | 767,650.00 USD | 0.00 USD | 8,220.00 USD | 7,210.00 USD | 50,540.00 USD |
| `7D` | `0.6390` | 568,600.00 USD | 568,600.00 USD | 0.00 USD | 24,230.00 USD | 15,680.00 USD | 13,150.00 USD |
| `1D` | `0.6400` | 884,810.00 USD | 884,810.00 USD | 0.00 USD | 66,560.00 USD | 37,130.00 USD | 13,480.00 USD |
| `7D` | `0.6400` | 588,440.00 USD | 588,440.00 USD | 0.00 USD | 19,270.00 USD | 0.00 USD | 569.80 USD |
| `1D` | `0.6410` | 944,800.00 USD | 944,800.00 USD | 0.00 USD | 29,560.00 USD | 14,660.00 USD | 15,770.00 USD |
| `7D` | `0.6410` | 612,990.00 USD | 612,990.00 USD | 0.00 USD | 0.00 USD | 18,210.00 USD | 6,340.00 USD |
| `1D` | `0.6420` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 55,880.00 USD | 9,980.00 USD | 15,000.00 USD |
| `7D` | `0.6420` | 724,470.00 USD | 724,470.00 USD | 0.00 USD | 55,350.00 USD | 26,560.00 USD | 29,570.00 USD |
| `1D` | `0.6430` | 1,090,000.00 USD | 1,090,000.00 USD | 0.00 USD | 24,220.00 USD | 12,130.00 USD | 28,900.00 USD |
| `7D` | `0.6430` | 776,560.00 USD | 776,560.00 USD | 0.00 USD | 31,500.00 USD | 7,140.00 USD | 13,460.00 USD |
| `1D` | `0.6440` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 36,460.00 USD | 14,890.00 USD | 56,530.00 USD |
| `7D` | `0.6440` | 843,750.00 USD | 843,750.00 USD | 0.00 USD | 34,270.00 USD | 17,680.00 USD | 15,240.00 USD |
| `1D` | `0.6450` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 62,440.00 USD | 14,460.00 USD | 21,050.00 USD |
| `7D` | `0.6450` | 976,210.00 USD | 976,210.00 USD | 0.00 USD | 81,220.00 USD | 15,560.00 USD | 35,680.00 USD |
| `1D` | `0.6460` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 25,640.00 USD | 12,810.00 USD | 9,690.00 USD |
| `7D` | `0.6460` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 91,390.00 USD | 31,070.00 USD | 102,440.00 USD |
| `1D` | `0.6470` | 1,430,000.00 USD | 1,430,000.00 USD | 0.00 USD | 57,900.00 USD | 17,750.00 USD | 11,970.00 USD |
| `7D` | `0.6470` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 9,660.00 USD | 26,520.00 USD | 9,370.00 USD |
| `1D` | `0.6480` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 78,190.00 USD | 9,530.00 USD | 373.19 USD |
| `7D` | `0.6480` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 94,210.00 USD | 0.00 USD | 23,550.00 USD |
| `1D` | `0.6490` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 52,900.00 USD | 2,940.00 USD | 12,200.00 USD |
| `7D` | `0.6490` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 36,340.00 USD | 0.00 USD | 18,280.00 USD |
| `1D` | `0.6500` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 55,160.00 USD | 9,280.00 USD | 5,990.00 USD |
| `7D` | `0.6500` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 53,330.00 USD | 0.00 USD | 121,810.00 USD |
| `1D` | `0.6510` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 58,460.00 USD | 0.00 USD | 14,330.00 USD |
| `7D` | `0.6510` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 244,480.00 USD | 8,270.00 USD | 18,620.00 USD |
| `1D` | `0.6520` | 1,840,000.00 USD | 1,840,000.00 USD | 0.00 USD | 93,550.00 USD | 13,800.00 USD | 5,780.00 USD |
| `7D` | `0.6520` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 65,690.00 USD | 6,720.00 USD | 86,910.00 USD |
| `1D` | `0.6530` | 1,870,000.00 USD | 1,870,000.00 USD | 0.00 USD | 18,010.00 USD | 3,910.00 USD | 11.74 USD |
| `7D` | `0.6530` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD | 47,010.00 USD |
| `1D` | `0.6540` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 14,530.00 USD |
| `1D` | `0.6550` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `7D` | `0.6550` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 458.49 USD |
| `1D` | `0.6560` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `0.6560` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 562.81 USD |
| `1D` | `0.6570` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,450.00 USD |
| `7D` | `0.6570` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD | 198.80 USD |
| `1D` | `0.6580` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD |
| `7D` | `0.6580` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 21,920.00 USD | 9,600.00 USD |
| `1D` | `0.6590` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `7D` | `0.6590` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD | 339.59 USD |
| `1D` | `0.6600` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD |
| `7D` | `0.6600` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 7,100.00 USD | 127.46 USD |
| `1D` | `0.6610` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD |
| `7D` | `0.6610` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 540.47 USD |
| `1D` | `0.6620` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD |
| `7D` | `0.6620` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 507.28 USD |
| `1D` | `0.6630` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `0.6630` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 502.00 USD |
| `1D` | `0.6640` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD |
| `7D` | `0.6640` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 6,830.00 USD |
| `1D` | `0.6650` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `7D` | `0.6650` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 133.80 USD |
| `1D` | `0.6660` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD |
| `7D` | `0.6660` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 395.59 USD |
| `1D` | `0.6670` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `7D` | `0.6670` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 238.68 USD |
| `1D` | `0.6680` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 158.16 USD |
| `7D` | `0.6680` | 2,230,000.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 666.83 USD |
| `1D` | `0.6690` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `1D` | `0.6700` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `1D` | `0.6710` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `0.6710` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,210.00 USD |
| `1D` | `0.6720` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6720` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 145.79 USD |
| `1D` | `0.6730` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD |
| `7D` | `0.6730` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 132.72 USD |
| `1D` | `0.6740` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6750` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD |
| `7D` | `0.6750` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 75,730.00 USD | 68.35 USD |
| `1D` | `0.6760` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 2,340,000.00 USD | 2,340,000.00 USD | 0.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD |
| `7D` | `0.6770` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 63,600.00 USD | 4,190.00 USD | 17,930.00 USD |
| `1D` | `0.6780` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 33,610.00 USD | 11,780.00 USD | 12,140.00 USD |
| `7D` | `0.6780` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 0.00 USD | 12,620.00 USD | 0.00 USD |
| `1D` | `0.6790` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 13,670.00 USD |
| `7D` | `0.6790` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD |
| `1D` | `0.6800` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 4,540.00 USD | 686.25 USD | 4,180.00 USD |
| `7D` | `0.6800` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 6,120.00 USD | 0.00 USD | 2,610.00 USD |
| `1D` | `0.6810` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 4,670.00 USD | 2,460.00 USD | 15,190.00 USD |
| `7D` | `0.6810` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 0.00 USD |
| `1D` | `0.6820` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD |
| `7D` | `0.6820` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 32,570.00 USD | 37,730.00 USD | 73.84 USD |
| `1D` | `0.6830` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 26,250.00 USD | 15,380.00 USD | 36,820.00 USD |
| `7D` | `0.6830` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 0.00 USD | 17,730.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 2,670,000.00 USD | 2,670,000.00 USD | 0.00 USD | 45,780.00 USD | 13,660.00 USD | 15,180.00 USD |
| `7D` | `0.6840` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 57,890.00 USD | 36,580.00 USD | 54,170.00 USD |
| `1D` | `0.6850` | 2,730,000.00 USD | 2,730,000.00 USD | 0.00 USD | 29,890.00 USD | 6,280.00 USD | 24,100.00 USD |
| `7D` | `0.6850` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 24,240.00 USD | 4,710.00 USD | 10,480.00 USD |
| `1D` | `0.6860` | 2,790,000.00 USD | 2,790,000.00 USD | 0.00 USD | 42,050.00 USD | 4,600.00 USD | 14,780.00 USD |
| `7D` | `0.6860` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 32,660.00 USD | 9,830.00 USD | 209.15 USD |
| `1D` | `0.6870` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 63,220.00 USD | 1,160.00 USD | 3,820.00 USD |
| `7D` | `0.6870` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6880` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 20,970.00 USD | 11,390.00 USD | 14,740.00 USD |
| `7D` | `0.6880` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 24,610.00 USD | 17,300.00 USD | 2,900.00 USD |
| `1D` | `0.6890` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 8,480.00 USD |
| `7D` | `0.6890` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 4,850.00 USD | 12,670.00 USD | 0.00 USD |
| `1D` | `0.6900` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 18,600.00 USD | 4,990.00 USD | 21,690.00 USD |
| `7D` | `0.6900` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD |
| `1D` | `0.6910` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 31,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6910` | 3,190,000.00 USD | 3,190,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 37,520.00 USD |
| `7D` | `0.6920` | 3,220,000.00 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `7D` | `0.6930` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `7D` | `0.6950` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `7D` | `0.6960` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6970` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD |
| `7D` | `0.6980` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD |
| `7D` | `0.6990` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 13,410.00 USD | 0.00 USD | 30,360.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `86.55M` | Total OI Tokens: `140,447,626.5 APT`
  * 1h OI Change: `+0.06%` | 4h OI Change: `-0.53%` | 24h OI Change: `-10.02%`
  * Exchange Breakdown: Binance=`15.64M` | Bybit=`16.96M` | OKX=`4.03M` | Hyperliquid=`3.44M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `1.29K` | Last 24h: `836.23` | Last 3d: `10.58K` | Last 7d: `3.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0002%` | **USDT OKX** | `-0.0101%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0128%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0094%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `35.14%` | `64.86%` | `0.54` | 2,930,000.00 USD |
| `15M` | `Binance` | `42.33%` | `57.67%` | `0.73` | 902,310.00 USD |
| `15M` | `OKX` | `28.5%` | `71.5%` | `0.40` | 219,560.00 USD |
| `15M` | `Bybit` | `28.61%` | `71.39%` | `0.40` | 187,670.00 USD |
| `15M` | `KuCoin` | `49.21%` | `50.79%` | `0.97` | 12,430.00 USD |
| `15M` | `Gate` | `47.94%` | `52.06%` | `0.92` | 249,210.00 USD |
| `15M` | `Bitget` | `26.11%` | `73.89%` | `0.35` | 69,430.00 USD |
| `15M` | `BingX` | `35.32%` | `64.68%` | `0.55` | 462,540.00 USD |
| `15M` | `MEXC` | `48.73%` | `51.27%` | `0.95` | 47,530.00 USD |
| `15M` | `Bitunix` | `76.7%` | `23.3%` | `3.29` | 42,650.00 USD |
| `15M` | `Hyperliquid` | `13.66%` | `86.34%` | `0.16` | 15,310.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `36.38%` | `63.62%` | `0.57` | 173,840.00 USD |
| `15M` | `Crypto.com` | `74.52%` | `25.48%` | `2.92` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.87%` | `98.13%` | `0.02` | 532,930.00 USD |
| `15M` | `HTX` | `53.11%` | `46.89%` | `1.13` | 5,300.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `9.06%` | `90.94%` | `0.10` | 6,900.00 USD |
| `15M` | `Aster` | `11.12%` | `88.88%` | `0.13` | 5,570.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `17.48%` | `82.52%` | `0.21` | 82.42 USD |
| `15M` | `Whale Positions` | `42.33%` | `57.67%` | `0.73` | 902,310.00 USD |
| `15M` | `Global Accounts` | `35.14%` | `64.86%` | `0.54` | 2,930,000.00 USD |
| `1H` | `APT` | `41.48%` | `58.52%` | `0.71` | 12,030,000.00 USD |
| `1H` | `Binance` | `48.06%` | `51.94%` | `0.93` | 3,570,000.00 USD |
| `1H` | `OKX` | `56.31%` | `43.69%` | `1.29` | 925,340.00 USD |
| `1H` | `Bybit` | `51.01%` | `48.99%` | `1.04` | 1,070,000.00 USD |
| `1H` | `KuCoin` | `51.7%` | `48.3%` | `1.07` | 47,830.00 USD |
| `1H` | `Gate` | `50.68%` | `49.32%` | `1.03` | 1,040,000.00 USD |
| `1H` | `Bitget` | `35.78%` | `64.22%` | `0.56` | 776,650.00 USD |
| `1H` | `BingX` | `4.61%` | `95.39%` | `0.05` | 2,360,000.00 USD |
| `1H` | `MEXC` | `37.46%` | `62.54%` | `0.60` | 472,150.00 USD |
| `1H` | `Bitunix` | `36.02%` | `63.98%` | `0.56` | 258,640.00 USD |
| `1H` | `Hyperliquid` | `6.82%` | `93.18%` | `0.07` | 212,450.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.58%` | `46.42%` | `1.15` | 410,720.00 USD |
| `1H` | `Crypto.com` | `39.97%` | `60.03%` | `0.67` | 0.00 USD |
| `1H` | `WhiteBIT` | `3.3%` | `96.7%` | `0.03` | 855,670.00 USD |
| `1H` | `HTX` | `25.7%` | `74.3%` | `0.35` | 14,560.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `5.25%` | `94.75%` | `0.06` | 11,770.00 USD |
| `1H` | `Aster` | `29.41%` | `70.59%` | `0.42` | 6,920.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `42.31%` | `57.69%` | `0.73` | 2,800.00 USD |
| `1H` | `Whale Positions` | `48.06%` | `51.94%` | `0.93` | 3,570,000.00 USD |
| `1H` | `Global Accounts` | `41.48%` | `58.52%` | `0.71` | 12,030,000.00 USD |
| `4H` | `APT` | `49.10%` | `50.90%` | `0.96` | 41,920,000.00 USD |
| `4H` | `Binance` | `49.62%` | `50.38%` | `0.98` | 12,790,000.00 USD |
| `4H` | `OKX` | `42.72%` | `57.28%` | `0.75` | 4,850,000.00 USD |
| `4H` | `Bybit` | `54.4%` | `45.6%` | `1.19` | 3,950,000.00 USD |
| `4H` | `KuCoin` | `50.78%` | `49.22%` | `1.03` | 396,650.00 USD |
| `4H` | `Gate` | `48.57%` | `51.43%` | `0.94` | 4,270,000.00 USD |
| `4H` | `Bitget` | `51.69%` | `48.31%` | `1.07` | 1,510,000.00 USD |
| `4H` | `BingX` | `41.6%` | `58.4%` | `0.71` | 8,580,000.00 USD |
| `4H` | `MEXC` | `47.42%` | `52.58%` | `0.90` | 1,050,000.00 USD |
| `4H` | `Bitunix` | `42.66%` | `57.34%` | `0.74` | 904,830.00 USD |
| `4H` | `Hyperliquid` | `45.17%` | `54.83%` | `0.82` | 428,700.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.94%` | `50.06%` | `1.00` | 1,240,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `88.6%` | `11.4%` | `7.77` | 1,840,000.00 USD |
| `4H` | `HTX` | `56.38%` | `43.62%` | `1.29` | 55,670.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `38.35%` | `61.65%` | `0.62` | 12,920.00 USD |
| `4H` | `Aster` | `41.03%` | `58.97%` | `0.70` | 17,280.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `76.91%` | `23.09%` | `3.33` | 14,820.00 USD |
| `4H` | `Whale Positions` | `49.62%` | `50.38%` | `0.98` | 12,790,000.00 USD |
| `4H` | `Global Accounts` | `49.10%` | `50.90%` | `0.96` | 41,920,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.6261` | `0.6265` | `0.6261` | `0.6301` | `0.6249` | 279,939.09 USD | 130,926.11 USD | 149,012.98 USD | -18,086.87 USD | `-6.46%` | `11B / 13S` |
| `5:00 UTC` | `0.6226` | `0.6238` | `0.6226` | `0.6261` | `0.6220` | 343,830.82 USD | 133,537.78 USD | 210,293.05 USD | -76,755.27 USD | `-22.32%` | `2B / 11S` |
| `0:00 UTC` | `0.6250` | `0.6245` | `0.6250` | `0.6268` | `0.6220` | 446,891.02 USD | 183,356.85 USD | 263,534.17 USD | -80,177.31 USD | `-17.94%` | `11B / 7S` |
| `5:00 UTC` | `0.6240` | `0.6240` | `0.6240` | `0.6250` | `0.6229` | 210,447.16 USD | 134,415.81 USD | 76,031.35 USD | 58,384.47 USD | `+27.74%` | `5B / 0S` |
| `0:00 UTC` | `0.6183` | `0.6207` | `0.6183` | `0.6265` | `0.6164` | 583,858.34 USD | 265,708.57 USD | 318,149.78 USD | -52,441.21 USD | `-8.98%` | `15B / 19S` |
| `5:00 UTC` | `0.6193` | `0.6186` | `0.6193` | `0.6199` | `0.6168` | 453,632.84 USD | 294,361.17 USD | 159,271.67 USD | 135,089.51 USD | `+29.78%` | `6B / 1S` |
| `0:00 UTC` | `0.6190` | `0.6189` | `0.6190` | `0.6221` | `0.6169` | 281,500.66 USD | 161,174.25 USD | 120,326.41 USD | 40,847.84 USD | `+14.51%` | `12B / 4S` |
| `5:00 UTC` | `0.6206` | `0.6207` | `0.6206` | `0.6228` | `0.6190` | 259,699.58 USD | 123,300.67 USD | 136,398.91 USD | -13,098.24 USD | `-5.04%` | `4B / 8S` |
| `0:00 UTC` | `0.6208` | `0.6182` | `0.6208` | `0.6208` | `0.6153` | 335,089.06 USD | 145,222.32 USD | 189,866.74 USD | -44,644.43 USD | `-13.32%` | `3B / 19S` |
| `5:00 UTC` | `0.6161` | `0.6162` | `0.6161` | `0.6167` | `0.6158` | 86,889.70 USD | 62,412.67 USD | 24,477.04 USD | 37,935.63 USD | `+43.66%` | `3B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:06` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6898` | 0.00 USD | 0.00 USD |
| `10-28 21:06` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6871` | 68,000.00 USD | 0.00 USD |
| `10-28 21:02` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6867` | 0.00 USD | 0.00 USD |
| `10-28 20:37` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6858` | 33,000.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6782` | 0.00 USD | 0.00 USD |
| `10-28 20:01` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6808` | 79,000.00 USD | 0.00 USD |
| `10-28 19:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6764` | 22,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:46` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 44,000.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6771` | 0.00 USD | 0.00 USD |
| `10-28 19:43` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6793` | 39,000.00 USD | 0.00 USD |
| `10-28 19:41` | `Volume 1.0M APT` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6752` | 361,000.00 USD | 0.00 USD |
| `10-28 19:35` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6807` | 0.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6762` | 79,000.00 USD | 0.00 USD |
| `10-28 19:31` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6762` | 106,000.00 USD | 0.00 USD |
| `10-28 19:21` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6771` | 75,000.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6859` | 121,000.00 USD | 0.00 USD |
| `10-28 18:48` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6796` | 47,000.00 USD | 0.00 USD |
| `10-28 18:44` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6793` | 107,000.00 USD | 0.00 USD |
| `10-28 18:37` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6818` | 0.00 USD | 0.00 USD |
| `10-28 17:54` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6887` | 177,000.00 USD | 0.00 USD |
| `10-28 17:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6884` | 112,000.00 USD | 0.00 USD |
| `10-28 17:43` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6842` | 275,000.00 USD | 0.00 USD |
| `10-28 17:36` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6934` | 22,000.00 USD | 0.00 USD |
| `10-28 17:03` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6995` | 234,000.00 USD | 0.00 USD |
| `10-28 16:15` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 140,000.00 USD | 0.00 USD |
| `10-28 16:02` | `Volume 1.0M APT` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6994` | 223,000.00 USD | 0.00 USD |
| `10-28 14:46` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6950` | 67,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6922` | 0.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:31` | `Range 0.002` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `0.6896` | 58,000.00 USD | 0.00 USD |
| `10-28 14:09` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6972` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6976` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.002` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `0.7006` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6962` | 0.00 USD | 0.00 USD |
| `10-28 13:33` | `Volume 1.0M APT` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6929` | 351,000.00 USD | 0.00 USD |
| `10-28 12:44` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6912` | 0.00 USD | 0.00 USD |
| `10-28 12:22` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6924` | 0.00 USD | 0.00 USD |
| `10-28 10:16` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6976` | 25,000.00 USD | 0.00 USD |
| `10-28 09:48` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6958` | 18,000.00 USD | 0.00 USD |
| `10-28 09:29` | `Range 0.002` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `0.6985` | 55,000.00 USD | 0.00 USD |
| `10-28 09:11` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.7008` | 0.00 USD | 0.00 USD |
| `10-28 09:04` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7021` | 0.00 USD | 0.00 USD |
| `10-28 09:00` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.7001` | 27,000.00 USD | 0.00 USD |
| `10-28 08:49` | `Range 0.002` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `0.6966` | 73,000.00 USD | 0.00 USD |
| `10-28 08:31` | `Range 0.002` | `Divergence` | **`BULLISH`** | Drop without taker selling | `0.6974` | 0.00 USD | 0.00 USD |
| `10-28 07:29` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.7003` | 0.00 USD | 0.00 USD |
| `10-28 07:23` | `Range 0.002` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `0.6977` | 10,000.00 USD | 0.00 USD |
| `10-28 06:12` | `Range 0.002` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `0.6982` | 122,000.00 USD | 0.00 USD |
| `10-28 05:31` | `Range 0.002` | `Divergence` | **`BEARISH`** | Rally without taker buying | `0.6963` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -12,910.00 USD | -20,500.00 USD | **`DISTRIBUTION`** |
| `15m` | -24,170.00 USD | -57,730.00 USD | **`DISTRIBUTION`** |
| `30m` | -6,580.00 USD | 2,370.00 USD | **`DISTRIBUTION`** |
| `1h` | 12,280.00 USD | 157,070.00 USD | **`ACCUMULATION`** |
| `2h` | -46,100.00 USD | 117,000.00 USD | **`ACCUMULATION`** |
| `4h` | -292,520.00 USD | -438,100.00 USD | **`DISTRIBUTION`** |
| `6h` | -190,780.00 USD | 1,460.00 USD | **`DISTRIBUTION`** |
| `8h` | -295,110.00 USD | -1,230,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -898,760.00 USD | -985,810.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,170,000.00 USD | -8,460,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,000,000.00 USD | -26,190,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,440,000.00 USD | -106,310,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-12.91K` | 15m=`-24.17K` | 1h=`+12.28K` | 24h=`-1.17M`
* Futures Capital Netflows: 5m=`-20.50K` | 15m=`-57.73K` | 1h=`+157.07K` | 24h=`-8.46M`
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
  * `2026-10-30 14:10:12 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:12 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:32:12 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:24:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 13:22:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 13:21:12 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:17:12 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:16:12 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
  * Execution Entry: `0.6880` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `-0.5122` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `3.69`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `0.6921` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `1.89` (Risk Distance: `1.20` pts)
  * +2.5R Take Profit: `-2.31`
  * Mathematical Lot Sizing: **`8.33 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`PASSIVE_MAKER_LIMIT_ARMED`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`0.6956`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
