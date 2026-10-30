# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:39:17 IST` (`2026-10-30 10:09:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6155` | `0.6162` | `0.6128` | `0.6162` | `172,626` | 106,010.27 USD | 18,377.17 USD | `+17.34%` | -6,402,936.87 USD | `+0.74` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6161` | `0.6185` | `0.6154` | `0.6183` | `136,470` | 84,203.53 USD | 11,763.02 USD | `+13.97%` | -6,391,173.85 USD | `+0.58` | **`BULLISH`** | `DELTA ALIGNED` |
| `5m` | `0.6183` | `0.6190` | `0.6163` | `0.6185` | `263,440` | 162,679.85 USD | -72,242.58 USD | `-44.41%` | -6,463,416.43 USD | `-2.16` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6149` | `0.6165` | `0.6135` | `0.6149` | `357,576` | 219,959.16 USD | -21,453.91 USD | `-9.75%` | -6,394,523.84 USD | `+0.03` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `0.6149` | `0.6167` | `0.6117` | `0.6155` | `758,654` | 465,814.11 USD | -26,790.20 USD | `-5.75%` | -6,421,314.04 USD | `-0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6155` | `0.6190` | `0.6128` | `0.6185` | `572,537` | 352,893.65 USD | -42,102.39 USD | `-11.93%` | -6,463,416.43 USD | `-0.43` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6243` | `0.6267` | `0.6164` | `0.6189` | `2,727,046` | 1,694,829.37 USD | 60,855.45 USD | `+3.59%` | -6,363,218.09 USD | `+0.48` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6189` | `0.6227` | `0.6148` | `0.6154` | `1,973,639` | 1,220,429.53 USD | 16,303.25 USD | `+1.34%` | -6,346,914.84 USD | `+0.42` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `0.6155` | `0.6190` | `0.6117` | `0.6185` | `2,385,969` | 1,467,626.07 USD | -116,501.59 USD | `-7.94%` | -6,463,416.43 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6227` | `0.6117` | `0.6185` | `4,359,608` | 2,688,055.59 USD | -100,198.34 USD | `-3.73%` | -6,168,635.08 USD | `+0.73` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -1,617,014.88 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,283,281.24 USD | `-1.31` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,661,106.76 USD | `+0.75` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6301` | `0.6117` | `0.6189` | `10,604,379` | 6,589,336.18 USD | -407,329.97 USD | `-6.18%` | -6,068,436.74 USD | `+0.62` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6189` | `0.6227` | `0.6117` | `0.6185` | `4,359,608` | 2,688,055.59 USD | -100,198.34 USD | `-3.73%` | -6,168,635.08 USD | `+0.73` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:30:10 IST` |

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
| `Live` | `Long Liquidation` | `0.1415` | 283.00 USD | 252,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1705` | 21,990.00 USD | 252,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 230,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1935` | 860.04 USD | 229,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2215` | 229.94 USD | 229,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2345` | 235.97 USD | 228,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2375` | 2,680.00 USD | 228,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 225,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 224,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 543.58 USD | 222,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3325` | 9,460.00 USD | 222,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 212,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3615` | 362.58 USD | 212,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 212,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3735` | 560.25 USD | 212,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3785` | 301.05 USD | 211,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 211,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 208,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4085` | 413.58 USD | 208,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4095` | 5,380.00 USD | 207,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 202,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 201,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 199,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 199,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4375` | 31,060.00 USD | 199,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4445` | 836.26 USD | 167,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 167,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4525` | 27,150.00 USD | 166,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 5,530.00 USD | 139,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 125.38 USD | 134,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 901.90 USD | 134,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,100.00 USD | 133,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4635` | 4,280.00 USD | 132,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 127,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 468.50 USD | 126,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4715` | 188.60 USD | 126,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 126,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 126,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,170.00 USD | 125,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,690.00 USD | 122,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 112,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 110,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 107,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 667.49 USD | 107,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 106,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 303.42 USD | 106,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 105,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 519.77 USD | 105,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 105,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 104,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 104,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 95,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5215` | 183.17 USD | 94,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5220` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5260` | 1,520,000.00 USD | 1,520,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5270` | 1,510,000.00 USD | 1,510,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5290` | 1,510,000.00 USD | 1,510,000.00 USD | 2,560.00 USD | 0.00 USD | 2,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 94,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5300` | 1,500,000.00 USD | 1,500,000.00 USD | 2,560.00 USD | 0.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5310` | 1,490,000.00 USD | 1,490,000.00 USD | 8,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 92,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 81,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5330` | 1,480,000.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 79,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5350` | 1,480,000.00 USD | 1,480,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5370` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5410` | 1,460,000.00 USD | 1,460,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,460,000.00 USD | 1,460,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5430` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 627.61 USD | 4,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 523.59 USD | 8,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 78,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5450` | 1,430,000.00 USD | 1,430,000.00 USD | 2,250.00 USD | 0.00 USD | 2,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 3,030.00 USD | 3,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5470` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 795.70 USD | 29.80 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 78,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,420,000.00 USD | 1,420,000.00 USD | 2,000.00 USD | 0.00 USD | 4,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5490` | 1,410,000.00 USD | 1,410,000.00 USD | 2,100.00 USD | 474.54 USD | 2,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 1,430,000.00 USD | 1,430,000.00 USD | 1,410.00 USD | 0.00 USD | 38.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,410,000.00 USD | 1,410,000.00 USD | 3,890.00 USD | 967.07 USD | 4,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 1,430,000.00 USD | 1,430,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5510` | 1,400,000.00 USD | 1,400,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,390,000.00 USD | 1,390,000.00 USD | 2,380.00 USD | 0.00 USD | 20.49 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 1,420,000.00 USD | 1,420,000.00 USD | 2,560.00 USD | 1,410.00 USD | 2,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5530` | 1,390,000.00 USD | 1,390,000.00 USD | 1,650.00 USD | 1,150.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 1,420,000.00 USD | 1,420,000.00 USD | 5,390.00 USD | 8,430.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,370,000.00 USD | 1,370,000.00 USD | 11,190.00 USD | 8,450.00 USD | 9,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 76,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 1,400,000.00 USD | 1,400,000.00 USD | 2,940.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5550` | 1,340,000.00 USD | 1,340,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 1,390,000.00 USD | 1,390,000.00 USD | 4,540.00 USD | 686.25 USD | 2,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,330,000.00 USD | 1,330,000.00 USD | 12,540.00 USD | 1,150.00 USD | 7,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 1,380,000.00 USD | 1,380,000.00 USD | 4,670.00 USD | 2,460.00 USD | 7,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5570` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 812.74 USD | 3,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 1,370,000.00 USD | 1,370,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 1,300,000.00 USD | 1,300,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 29,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 1,360,000.00 USD | 1,360,000.00 USD | 1,670.00 USD | 2,150.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5590` | 1,270,000.00 USD | 1,270,000.00 USD | 2,660.00 USD | 7,220.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 1,260,000.00 USD | 1,260,000.00 USD | 1,410.00 USD | 938.63 USD | 104.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 1,350,000.00 USD | 1,350,000.00 USD | 2,240.00 USD | 500.33 USD | 823.46 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5610` | 1,260,000.00 USD | 1,260,000.00 USD | 13,590.00 USD | 1,960.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 18,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 1,340,000.00 USD | 1,340,000.00 USD | 1,800.00 USD | 995.72 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 1,240,000.00 USD | 1,240,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 1,340,000.00 USD | 1,340,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5630` | 1,210,000.00 USD | 1,210,000.00 USD | 14,240.00 USD | 2,380.00 USD | 2,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 18,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 1,320,000.00 USD | 1,320,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 25.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5650` | 1,300,000.00 USD | 1,300,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5650` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 18,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 1,190,000.00 USD | 1,190,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 16,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5670` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5680` | 1,170,000.00 USD | 1,170,000.00 USD | 5,100.00 USD | 0.00 USD | 41.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5690` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 6.78 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 1,170,000.00 USD | 1,170,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5710` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 2,850.00 USD | 1,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 14,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 1,520.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5730` | 1,150,000.00 USD | 1,150,000.00 USD | 2,690.00 USD | 528.82 USD | 5.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 839.21 USD | 3,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 1,140,000.00 USD | 1,140,000.00 USD | 18,940.00 USD | 574.82 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 218.30 USD | 14,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 1,270,000.00 USD | 1,270,000.00 USD | 4,330.00 USD | 840.09 USD | 20,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5750` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 187.30 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 1,240,000.00 USD | 1,240,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 1,120,000.00 USD | 1,120,000.00 USD | 2,150.00 USD | 7,300.00 USD | 19.23 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 1,220,000.00 USD | 1,220,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5770` | 1,110,000.00 USD | 1,110,000.00 USD | 21,510.00 USD | 0.00 USD | 222.98 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 1,200,000.00 USD | 1,200,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 1,090,000.00 USD | 1,090,000.00 USD | 19,410.00 USD | 0.00 USD | 1,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 1,190,000.00 USD | 1,190,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5790` | 1,070,000.00 USD | 1,070,000.00 USD | 1,610.00 USD | 0.00 USD | 11,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 1,160,000.00 USD | 1,160,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 3,900.00 USD | 16,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5810` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 1,140,000.00 USD | 1,140,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 1,130,000.00 USD | 1,130,000.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 2,190.00 USD | 4,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 1,110,000.00 USD | 1,110,000.00 USD | 2,950.00 USD | 0.00 USD | 30,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5850` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 396.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 1,080,000.00 USD | 1,080,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 1,070,000.00 USD | 1,070,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5870` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 1,050,000.00 USD | 1,050,000.00 USD | 34,650.00 USD | 8,680.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 1,010,000.00 USD | 1,010,000.00 USD | 3,110.00 USD | 14,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5885` | 8,900.00 USD | 14,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5890` | 1,000,000.00 USD | 1,000,000.00 USD | 39,360.00 USD | 11,450.00 USD | 6,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5890` | 989,960.00 USD | 989,960.00 USD | 43,020.00 USD | 0.00 USD | 8,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 943,490.00 USD | 943,490.00 USD | 24,340.00 USD | 14,260.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 938,210.00 USD | 938,210.00 USD | 61,220.00 USD | 1,560.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 886,510.00 USD | 886,510.00 USD | 31,110.00 USD | 17,770.00 USD | 19,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5910` | 866,300.00 USD | 866,300.00 USD | 0.00 USD | 15,190.00 USD | 16,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5915` | 5,310.00 USD | 5,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5920` | 818,330.00 USD | 818,330.00 USD | 26,620.00 USD | 6,570.00 USD | 9,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 834,450.00 USD | 834,450.00 USD | 11,690.00 USD | 10,620.00 USD | 58,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 775,170.00 USD | 775,170.00 USD | 11,360.00 USD | 6,380.00 USD | 22,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5930` | 753,320.00 USD | 753,320.00 USD | 25,390.00 USD | 2,880.00 USD | 14,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 735,050.00 USD | 735,050.00 USD | 23,730.00 USD | 2,040.00 USD | 16,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 710,930.00 USD | 710,930.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 692,840.00 USD | 692,840.00 USD | 37,990.00 USD | 4,980.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5950` | 705,150.00 USD | 705,150.00 USD | 13,060.00 USD | 0.00 USD | 301.29 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 648,240.00 USD | 648,240.00 USD | 11,510.00 USD | 2,560.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 691,790.00 USD | 691,790.00 USD | 5,120.00 USD | 18,410.00 USD | 241.99 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 625,590.00 USD | 625,590.00 USD | 12,870.00 USD | 532.93 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 607,010.00 USD | 607,010.00 USD | 15,950.00 USD | 4,300.00 USD | 52.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 668,020.00 USD | 668,020.00 USD | 37,820.00 USD | 0.00 USD | 3.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 586,710.00 USD | 586,710.00 USD | 6,880.00 USD | 1,700.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5990` | 630,200.00 USD | 630,200.00 USD | 3,320.00 USD | 0.00 USD | 52.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 577,040.00 USD | 577,040.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 626,820.00 USD | 626,820.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 539,900.00 USD | 539,900.00 USD | 5,480.00 USD | 6,370.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6010` | 598,770.00 USD | 598,770.00 USD | 12,110.00 USD | 4,090.00 USD | 50.15 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 523,020.00 USD | 523,020.00 USD | 11,780.00 USD | 8,040.00 USD | 15,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 582,520.00 USD | 582,520.00 USD | 0.00 USD | 7,150.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 487,900.00 USD | 487,900.00 USD | 40,580.00 USD | 17,840.00 USD | 20,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6030` | 557,950.00 USD | 557,950.00 USD | 38,530.00 USD | 0.00 USD | 18,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 409,370.00 USD | 409,370.00 USD | 16,550.00 USD | 20,270.00 USD | 7,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 501,160.00 USD | 501,160.00 USD | 0.00 USD | 30,380.00 USD | 89.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 364,980.00 USD | 364,980.00 USD | 23,200.00 USD | 2,140.00 USD | 13,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6050` | 470,680.00 USD | 470,680.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 325,940.00 USD | 325,940.00 USD | 22,710.00 USD | 0.00 USD | 18,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 449,870.00 USD | 449,870.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6070` | 284,350.00 USD | 284,350.00 USD | 27,430.00 USD | 4,080.00 USD | 16,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6070` | 385,290.00 USD | 385,290.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6080` | 236,760.00 USD | 236,760.00 USD | 26,190.00 USD | 6,680.00 USD | 3,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 373,730.00 USD | 373,730.00 USD | 2,860.00 USD | 0.00 USD | 30,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6090` | 200,820.00 USD | 200,820.00 USD | 11,540.00 USD | 3,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6090` | 340,500.00 USD | 340,500.00 USD | 13,920.00 USD | 44,860.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 186,250.00 USD | 186,250.00 USD | 3,470.00 USD | 1,070.00 USD | 41,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 256,600.00 USD | 256,600.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 140,160.00 USD | 140,160.00 USD | 27,240.00 USD | 7,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6110` | 246,540.00 USD | 246,540.00 USD | 34,870.00 USD | 2,210.00 USD | 12,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 105,730.00 USD | 105,730.00 USD | 43,790.00 USD | 3,410.00 USD | 2,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 196,600.00 USD | 196,600.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 56,360.00 USD | 56,360.00 USD | 0.00 USD | 6,720.00 USD | 40,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6130` | 140,060.00 USD | 140,060.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 9,520.00 USD | 9,520.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 6,330.00 USD | 6,330.00 USD | 0.00 USD | 6,170.00 USD | 159.06 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6180` | 1,760.00 USD | 1,760.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6180` | 173.29 USD | 173.29 USD | 0.00 USD | 0.00 USD | 173.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6180` | 346.58 USD | 346.58 USD | 0.00 USD | 0.00 USD | 173.29 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6190` | 528.69 USD | 528.69 USD | 0.00 USD | 0.00 USD | 182.11 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6200` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 50.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 43,470.00 USD | 43,470.00 USD | 13,870.00 USD | 0.00 USD | 29,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6210` | 66,110.00 USD | 66,110.00 USD | 0.00 USD | 22,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6230` | 66,240.00 USD | 66,240.00 USD | 0.00 USD | 0.00 USD | 122.98 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 73,590.00 USD | 73,590.00 USD | 0.00 USD | 7,300.00 USD | 48.83 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6250` | 4,330.00 USD | 4,330.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6260` | 35,380.00 USD | 35,380.00 USD | 9,100.00 USD | 8,370.00 USD | 13,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 91,010.00 USD | 91,010.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 55,640.00 USD | 55,640.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6270` | 117,530.00 USD | 117,530.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 117,850.00 USD | 117,850.00 USD | 10,020.00 USD | 26,790.00 USD | 25,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 168,460.00 USD | 168,460.00 USD | 0.00 USD | 34,280.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6290` | 168,570.00 USD | 168,570.00 USD | 23,200.00 USD | 7,350.00 USD | 20,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6290` | 217,270.00 USD | 217,270.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 225,370.00 USD | 225,370.00 USD | 25,290.00 USD | 3,430.00 USD | 28,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 281,860.00 USD | 281,860.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 310,870.00 USD | 310,870.00 USD | 38,850.00 USD | 8,860.00 USD | 37,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6310` | 293,520.00 USD | 293,520.00 USD | 11,560.00 USD | 0.00 USD | 103.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 386,110.00 USD | 386,110.00 USD | 51,560.00 USD | 9,600.00 USD | 14,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6320` | 293,780.00 USD | 293,780.00 USD | 0.00 USD | 0.00 USD | 265.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 428,160.00 USD | 428,160.00 USD | 14,490.00 USD | 12,370.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6330` | 351,980.00 USD | 351,980.00 USD | 57,940.00 USD | 0.00 USD | 259.82 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 502,090.00 USD | 502,090.00 USD | 28,910.00 USD | 4,250.00 USD | 40,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 362,830.00 USD | 362,830.00 USD | 10,730.00 USD | 0.00 USD | 121.40 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 565,740.00 USD | 565,740.00 USD | 54,290.00 USD | 5,510.00 USD | 3,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6350` | 432,410.00 USD | 432,410.00 USD | 69,190.00 USD | 0.00 USD | 386.01 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 657,060.00 USD | 657,060.00 USD | 49,770.00 USD | 5,880.00 USD | 35,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 489,000.00 USD | 489,000.00 USD | 0.00 USD | 0.00 USD | 56,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 667,470.00 USD | 667,470.00 USD | 0.00 USD | 2,880.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6370` | 498,180.00 USD | 498,180.00 USD | 0.00 USD | 0.00 USD | 9,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 754,950.00 USD | 754,950.00 USD | 47,080.00 USD | 23,740.00 USD | 16,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 575,020.00 USD | 575,020.00 USD | 32,220.00 USD | 0.00 USD | 44,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 827,200.00 USD | 827,200.00 USD | 12,760.00 USD | 6,680.00 USD | 52,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6390` | 636,700.00 USD | 636,700.00 USD | 24,230.00 USD | 15,680.00 USD | 21,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 951,150.00 USD | 951,150.00 USD | 66,560.00 USD | 38,500.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 665,100.00 USD | 665,100.00 USD | 19,270.00 USD | 0.00 USD | 9,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 1,020,000.00 USD | 1,020,000.00 USD | 34,570.00 USD | 19,840.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6410` | 695,470.00 USD | 695,470.00 USD | 0.00 USD | 24,060.00 USD | 6,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,100,000.00 USD | 1,100,000.00 USD | 57,140.00 USD | 9,980.00 USD | 15,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 807,080.00 USD | 807,080.00 USD | 55,350.00 USD | 26,560.00 USD | 29,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,170,000.00 USD | 1,170,000.00 USD | 24,220.00 USD | 10,750.00 USD | 33,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6430` | 865,900.00 USD | 865,900.00 USD | 31,500.00 USD | 10,020.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,280,000.00 USD | 1,280,000.00 USD | 34,630.00 USD | 14,890.00 USD | 56,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 932,540.00 USD | 932,540.00 USD | 34,270.00 USD | 17,680.00 USD | 14,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,370,000.00 USD | 1,370,000.00 USD | 62,440.00 USD | 14,460.00 USD | 15,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6450` | 1,070,000.00 USD | 1,070,000.00 USD | 81,220.00 USD | 15,560.00 USD | 35,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,420,000.00 USD | 1,420,000.00 USD | 25,640.00 USD | 12,810.00 USD | 9,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,290,000.00 USD | 1,290,000.00 USD | 91,390.00 USD | 31,070.00 USD | 102,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,500,000.00 USD | 1,500,000.00 USD | 52,770.00 USD | 17,750.00 USD | 11,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6470` | 1,340,000.00 USD | 1,340,000.00 USD | 9,660.00 USD | 26,520.00 USD | 9,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 209.47 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,590,000.00 USD | 1,590,000.00 USD | 78,190.00 USD | 9,530.00 USD | 392.53 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,450,000.00 USD | 1,450,000.00 USD | 94,210.00 USD | 0.00 USD | 23,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6485` | 210.58 USD | 420.05 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,650,000.00 USD | 1,650,000.00 USD | 46,110.00 USD | 2,940.00 USD | 12,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6490` | 1,510,000.00 USD | 1,510,000.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,720,000.00 USD | 1,720,000.00 USD | 52,920.00 USD | 9,280.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,680,000.00 USD | 1,680,000.00 USD | 53,330.00 USD | 0.00 USD | 122,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,790,000.00 USD | 1,790,000.00 USD | 56,160.00 USD | 0.00 USD | 14,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6510` | 1,950,000.00 USD | 1,950,000.00 USD | 244,480.00 USD | 8,270.00 USD | 18,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,880,000.00 USD | 1,880,000.00 USD | 70,440.00 USD | 13,800.00 USD | 5,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 2,110,000.00 USD | 2,110,000.00 USD | 65,690.00 USD | 6,720.00 USD | 86,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 1,900,000.00 USD | 1,900,000.00 USD | 18,010.00 USD | 3,910.00 USD | 11.74 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6530` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 4,440.00 USD | 47,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 1,930,000.00 USD | 1,930,000.00 USD | 24,280.00 USD | 0.00 USD | 4,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,200,000.00 USD | 2,200,000.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6550` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 414.15 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 8,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 5,380.00 USD | 507.31 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6570` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 6,350.00 USD | 447.57 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 3,310.00 USD | 48.99 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 21,920.00 USD | 9,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6590` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 11,320.00 USD | 331.05 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 1,970,000.00 USD | 1,970,000.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 7,100.00 USD | 249.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 1,980,000.00 USD | 1,980,000.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6610` | 2,270,000.00 USD | 2,270,000.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 128.16 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 2,000,000.00 USD | 2,000,000.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6630` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 254.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 2,010,000.00 USD | 2,010,000.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,310,000.00 USD | 2,310,000.00 USD | 33,660.00 USD | 0.00 USD | 7,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6650` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 6,770.00 USD | 288.69 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 148.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,060,000.00 USD | 2,060,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6670` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 308.18 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 158.16 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6680` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 224.19 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6690` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 448.05 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6695` | 69,660.00 USD | 70,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,100,000.00 USD | 2,100,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 546.45 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,150,000.00 USD | 2,150,000.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6710` | 2,410,000.00 USD | 2,410,000.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,150,000.00 USD | 2,150,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,180,000.00 USD | 2,180,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6730` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 99.42 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,270,000.00 USD | 2,270,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,450,000.00 USD | 2,450,000.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,310,000.00 USD | 2,310,000.00 USD | 30,000.00 USD | 1,410.00 USD | 14,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6750` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 75,730.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,330,000.00 USD | 2,330,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,380,000.00 USD | 2,380,000.00 USD | 19,930.00 USD | 9,080.00 USD | 17,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6770` | 2,650,000.00 USD | 2,650,000.00 USD | 63,600.00 USD | 4,190.00 USD | 21,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,430,000.00 USD | 2,430,000.00 USD | 33,610.00 USD | 9,900.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 14,960.00 USD | 124.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,470,000.00 USD | 2,470,000.00 USD | 2,940.00 USD | 18,610.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6790` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,480,000.00 USD | 2,480,000.00 USD | 4,540.00 USD | 686.25 USD | 5,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,700,000.00 USD | 2,700,000.00 USD | 6,120.00 USD | 1,150.00 USD | 2,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,500,000.00 USD | 2,500,000.00 USD | 4,670.00 USD | 2,460.00 USD | 15,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6810` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 15,720.00 USD | 145.79 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,550,000.00 USD | 2,550,000.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,780,000.00 USD | 2,780,000.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,630,000.00 USD | 2,630,000.00 USD | 26,250.00 USD | 15,380.00 USD | 36,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6830` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 17,730.00 USD | 48,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,700,000.00 USD | 2,700,000.00 USD | 45,780.00 USD | 12,210.00 USD | 15,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 3,000,000.00 USD | 3,000,000.00 USD | 57,890.00 USD | 36,580.00 USD | 54,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6850` | 2,760,000.00 USD | 2,760,000.00 USD | 29,890.00 USD | 6,280.00 USD | 24,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6850` | 3,040,000.00 USD | 3,040,000.00 USD | 24,240.00 USD | 4,710.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6860` | 2,820,000.00 USD | 2,820,000.00 USD | 42,050.00 USD | 4,600.00 USD | 14,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 3,080,000.00 USD | 3,080,000.00 USD | 32,660.00 USD | 9,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6870` | 3,100,000.00 USD | 3,100,000.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 3,140,000.00 USD | 3,140,000.00 USD | 24,610.00 USD | 17,300.00 USD | 2,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6890` | 3,160,000.00 USD | 3,160,000.00 USD | 4,850.00 USD | 12,670.00 USD | 77.75 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6910` | 3,290,000.00 USD | 3,290,000.00 USD | 69,620.00 USD | 2,090.00 USD | 37,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6930` | 3,370,000.00 USD | 3,370,000.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6950` | 3,420,000.00 USD | 3,420,000.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,440,000.00 USD | 3,440,000.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6970` | 3,470,000.00 USD | 3,470,000.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,500,000.00 USD | 3,500,000.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6990` | 3,540,000.00 USD | 3,540,000.00 USD | 13,410.00 USD | 0.00 USD | 30,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 70,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 70,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.7945` | 365.88 USD | 70,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 90,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 90,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9095` | 21,920.00 USD | 112,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9635` | 17,000.00 USD | 129,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 129,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 155,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,200.00 USD | 160,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.08` | 82,670.00 USD | 243,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 243,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.10` | 623.65 USD | 244,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 247,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 247,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 248,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 248,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 796.83 USD | 249,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1415` | 252,460.00 USD | 0.00 USD | 283.00 USD | `-76.97%` | `2,000.00` |
| `Live` | `Long` | `0.1705` | 252,170.00 USD | 0.00 USD | 21,990.00 USD | `-72.24%` | `129,000.00` |
| `Live` | `Long` | `0.1875` | 230,180.00 USD | 0.00 USD | 269.27 USD | `-69.48%` | `1,436.09` |
| `Live` | `Long` | `0.1935` | 229,910.00 USD | 0.00 USD | 860.04 USD | `-68.50%` | `4,444.65` |
| `Live` | `Long` | `0.2215` | 229,050.00 USD | 0.00 USD | 229.94 USD | `-63.94%` | `1,038.12` |
| `Live` | `Long` | `0.2345` | 228,820.00 USD | 0.00 USD | 235.97 USD | `-61.83%` | `1,006.27` |
| `Live` | `Long` | `0.2375` | 228,580.00 USD | 0.00 USD | 2,680.00 USD | `-61.34%` | `11,284.25` |
| `Live` | `Long` | `0.2425` | 225,900.00 USD | 0.00 USD | 1,460.00 USD | `-60.52%` | `6,000.00` |
| `Live` | `Long` | `0.3175` | 224,450.00 USD | 0.00 USD | 1,590.00 USD | `-48.32%` | `5,000.00` |
| `Live` | `Long` | `0.3305` | 222,860.00 USD | 0.00 USD | 543.58 USD | `-46.20%` | `1,644.73` |
| `Live` | `Long` | `0.3325` | 222,320.00 USD | 0.00 USD | 9,460.00 USD | `-45.87%` | `28,446.85` |
| `Live` | `Long` | `0.3545` | 212,860.00 USD | 0.00 USD | 177.25 USD | `-42.29%` | `500.00` |
| `Live` | `Long` | `0.3615` | 212,680.00 USD | 0.00 USD | 362.58 USD | `-41.15%` | `1,002.99` |
| `Live` | `Long` | `0.3675` | 212,320.00 USD | 0.00 USD | 189.99 USD | `-40.18%` | `516.98` |
| `Live` | `Long` | `0.3735` | 212,130.00 USD | 0.00 USD | 560.25 USD | `-39.20%` | `1,500.00` |
| `Live` | `Long` | `0.3785` | 211,570.00 USD | 0.00 USD | 301.05 USD | `-38.39%` | `795.38` |
| `Live` | `Long` | `0.3955` | 211,270.00 USD | 0.00 USD | 2,640.00 USD | `-35.62%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 208,620.00 USD | 0.00 USD | 271.06 USD | `-34.97%` | `678.49` |
| `Live` | `Long` | `0.4085` | 208,350.00 USD | 0.00 USD | 413.58 USD | `-33.50%` | `1,012.44` |
| `Live` | `Long` | `0.4095` | 207,940.00 USD | 0.00 USD | 5,380.00 USD | `-33.34%` | `13,126.15` |
| `Live` | `Long` | `0.4125` | 202,560.00 USD | 0.00 USD | 1,070.00 USD | `-32.85%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 201,490.00 USD | 0.00 USD | 1,600.00 USD | `-32.69%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 199,890.00 USD | 0.00 USD | 630.86 USD | `-31.87%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 199,260.00 USD | 0.00 USD | 224.96 USD | `-30.73%` | `528.69` |
| `Live` | `Long` | `0.4375` | 199,040.00 USD | 0.00 USD | 31,060.00 USD | `-28.78%` | `71,004.49` |
| `Live` | `Long` | `0.4445` | 167,970.00 USD | 0.00 USD | 836.26 USD | `-27.64%` | `1,881.36` |
| `Live` | `Long` | `0.4475` | 167,140.00 USD | 0.00 USD | 226.63 USD | `-27.15%` | `506.43` |
| `Live` | `Long` | `0.4525` | 166,910.00 USD | 0.00 USD | 27,150.00 USD | `-26.34%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 139,760.00 USD | 0.00 USD | 5,530.00 USD | `-26.18%` | `12,191.83` |
| `Live` | `Long` | `0.4605` | 134,230.00 USD | 0.00 USD | 125.38 USD | `-25.04%` | `272.27` |
| `Live` | `Long` | `0.4615` | 134,100.00 USD | 0.00 USD | 901.90 USD | `-24.87%` | `1,954.27` |
| `Live` | `Long` | `0.4625` | 133,200.00 USD | 0.00 USD | 1,100.00 USD | `-24.71%` | `2,368.95` |
| `Live` | `Long` | `0.4635` | 132,110.00 USD | 0.00 USD | 4,280.00 USD | `-24.55%` | `9,243.24` |
| `Live` | `Long` | `0.4645` | 127,820.00 USD | 0.00 USD | 876.05 USD | `-24.39%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 126,950.00 USD | 0.00 USD | 468.50 USD | `-23.73%` | `1,000.00` |
| `Live` | `Long` | `0.4715` | 126,480.00 USD | 0.00 USD | 188.60 USD | `-23.25%` | `400.00` |
| `Live` | `Long` | `0.4835` | 126,290.00 USD | 0.00 USD | 135.33 USD | `-21.29%` | `279.90` |
| `Live` | `Long` | `0.4855` | 126,150.00 USD | 0.00 USD | 181.88 USD | `-20.97%` | `374.62` |
| `Live` | `Long` | `0.4865` | 125,970.00 USD | 0.00 USD | 3,170.00 USD | `-20.80%` | `6,508.47` |
| `Live` | `Long` | `0.4925` | 122,810.00 USD | 0.00 USD | 10,690.00 USD | `-19.83%` | `21,703.96` |
| `Live` | `Long` | `0.4935` | 112,120.00 USD | 0.00 USD | 1,580.00 USD | `-19.66%` | `3,199.85` |
| `Live` | `Long` | `0.4955` | 110,540.00 USD | 0.00 USD | 3,180.00 USD | `-19.34%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 107,360.00 USD | 0.00 USD | 143.19 USD | `-19.18%` | `288.40` |
| `Live` | `Long` | `0.4975` | 107,210.00 USD | 0.00 USD | 667.49 USD | `-19.01%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 106,540.00 USD | 0.00 USD | 429.90 USD | `-18.85%` | `862.38` |
| `Live` | `Long` | `0.5075` | 106,120.00 USD | 0.00 USD | 303.42 USD | `-17.39%` | `597.87` |
| `Live` | `Long` | `0.5085` | 105,810.00 USD | 0.00 USD | 102.82 USD | `-17.22%` | `202.20` |
| `Live` | `Long` | `0.5105` | 105,710.00 USD | 0.00 USD | 519.77 USD | `-16.90%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 105,190.00 USD | 0.00 USD | 248.05 USD | `-16.57%` | `484.00` |
| `Live` | `Long` | `0.5135` | 104,940.00 USD | 0.00 USD | 298.60 USD | `-16.41%` | `581.49` |
| `Live` | `Long` | `0.5175` | 104,640.00 USD | 0.00 USD | 9,440.00 USD | `-15.76%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 95,200.00 USD | 0.00 USD | 281.56 USD | `-15.59%` | `543.02` |
| `Live` | `Long` | `0.5215` | 94,920.00 USD | 0.00 USD | 183.17 USD | `-15.11%` | `351.24` |
| `Live` | `Long` | `0.5295` | 94,730.00 USD | 0.00 USD | 1,840.00 USD | `-13.80%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 92,900.00 USD | 0.00 USD | 11,510.00 USD | `-13.48%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 81,380.00 USD | 0.00 USD | 2,260.00 USD | `-13.32%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 79,120.00 USD | 0.00 USD | 163.22 USD | `-13.15%` | `305.95` |
| `Live` | `Long` | `0.5445` | 78,960.00 USD | 0.00 USD | 855.28 USD | `-11.36%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 78,110.00 USD | 0.00 USD | 1,630.00 USD | `-10.87%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 76,480.00 USD | 0.00 USD | 47,450.00 USD | `-9.73%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 29,030.00 USD | 0.00 USD | 10,520.00 USD | `-9.08%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 18,510.00 USD | 0.00 USD | 258.48 USD | `-8.60%` | `460.33` |
| `Live` | `Long` | `0.5635` | 18,250.00 USD | 0.00 USD | 244.90 USD | `-8.27%` | `434.61` |
| `Live` | `Long` | `0.5655` | 18,000.00 USD | 0.00 USD | 1,920.00 USD | `-7.94%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 16,080.00 USD | 0.00 USD | 1,370.00 USD | `-7.78%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 14,710.00 USD | 0.00 USD | 289.08 USD | `-6.97%` | `505.82` |
| `Live` | `Long` | `0.5745` | 14,420.00 USD | 0.00 USD | 218.30 USD | `-6.48%` | `379.98` |
| `Live` | `Long` | `0.5885` | 14,210.00 USD | 0.00 USD | 8,900.00 USD | `-4.20%` | `15,117.28` |
| `Live` | `Long` | `0.5915` | 5,310.00 USD | 0.00 USD | 5,310.00 USD | `-3.71%` | `8,975.06` |
| `Live` | `Short` | `0.6475` | 209.47 USD | 209.47 USD | 0.00 USD | `+5.40%` | `323.51` |
| `Live` | `Short` | `0.6485` | 420.05 USD | 210.58 USD | 0.00 USD | `+5.57%` | `324.72` |
| `Live` | `Short` | `0.6695` | 70,080.00 USD | 69,660.00 USD | 0.00 USD | `+8.99%` | `104,052.51` |
| `Live` | `Short` | `0.7245` | 70,450.00 USD | 364.39 USD | 0.00 USD | `+17.94%` | `502.96` |
| `Live` | `Short` | `0.7725` | 70,610.00 USD | 165.62 USD | 0.00 USD | `+25.75%` | `214.40` |
| `Live` | `Short` | `0.7945` | 70,980.00 USD | 365.88 USD | 0.00 USD | `+29.33%` | `460.51` |
| `Live` | `Short` | `0.8005` | 90,100.00 USD | 19,120.00 USD | 0.00 USD | `+30.31%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 90,480.00 USD | 378.95 USD | 0.00 USD | `+41.05%` | `437.33` |
| `Live` | `Short` | `0.9095` | 112,390.00 USD | 21,920.00 USD | 0.00 USD | `+48.05%` | `24,095.91` |
| `Live` | `Short` | `0.9635` | 129,400.00 USD | 17,000.00 USD | 0.00 USD | `+56.85%` | `17,648.14` |
| `Live` | `Short` | `0.9935` | 129,560.00 USD | 166.01 USD | 0.00 USD | `+61.73%` | `167.10` |
| `Live` | `Short` | `1.02` | 155,530.00 USD | 25,970.00 USD | 0.00 USD | `+66.29%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 160,730.00 USD | 5,200.00 USD | 0.00 USD | `+69.38%` | `5,000.00` |
| `Live` | `Short` | `1.08` | 243,410.00 USD | 82,670.00 USD | 0.00 USD | `+76.38%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 243,890.00 USD | 479.74 USD | 0.00 USD | `+77.68%` | `439.52` |
| `Live` | `Short` | `1.10` | 244,510.00 USD | 623.65 USD | 0.00 USD | `+79.15%` | `566.70` |
| `Live` | `Short` | `1.12` | 247,310.00 USD | 2,800.00 USD | 0.00 USD | `+82.24%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 247,810.00 USD | 501.44 USD | 0.00 USD | `+91.03%` | `427.30` |
| `Live` | `Short` | `1.19` | 248,040.00 USD | 227.46 USD | 0.00 USD | `+93.15%` | `191.71` |
| `Live` | `Short` | `1.19` | 248,240.00 USD | 199.98 USD | 0.00 USD | `+93.47%` | `168.26` |
| `Live` | `Short` | `1.22` | 249,030.00 USD | 796.83 USD | 0.00 USD | `+98.84%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 205,720.00 USD | 0.00 USD | 340.19 USD | `-42.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 205,380.00 USD | 0.00 USD | 104.57 USD | `-24.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 205,270.00 USD | 0.00 USD | 111.62 USD | `-19.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 205,160.00 USD | 0.00 USD | 111.85 USD | `-19.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 205,050.00 USD | 0.00 USD | 67,850.00 USD | `-18.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 137,200.00 USD | 0.00 USD | 112.97 USD | `-18.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 137,090.00 USD | 0.00 USD | 225.65 USD | `-17.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 136,860.00 USD | 0.00 USD | 101.97 USD | `-17.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 136,760.00 USD | 0.00 USD | 111.69 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 136,650.00 USD | 0.00 USD | 5,380.00 USD | `-16.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 131,270.00 USD | 0.00 USD | 115.47 USD | `-15.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 131,150.00 USD | 0.00 USD | 116.58 USD | `-15.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 131,040.00 USD | 0.00 USD | 116.96 USD | `-15.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 130,920.00 USD | 0.00 USD | 539.96 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 130,380.00 USD | 0.00 USD | 117.70 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 130,260.00 USD | 0.00 USD | 117.93 USD | `-14.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 130,140.00 USD | 0.00 USD | 770.19 USD | `-13.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 129,370.00 USD | 0.00 USD | 8,750.00 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 120,620.00 USD | 0.00 USD | 8,150.00 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 112,470.00 USD | 0.00 USD | 4,500.00 USD | `-10.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5505` | 107,970.00 USD | 0.00 USD | 7,230.00 USD | `-10.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 100,740.00 USD | 0.00 USD | 126.71 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 100,620.00 USD | 0.00 USD | 126.90 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 100,490.00 USD | 0.00 USD | 57,800.00 USD | `-9.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 42,690.00 USD | 0.00 USD | 173.58 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 42,510.00 USD | 0.00 USD | 10,540.00 USD | `-8.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 31,980.00 USD | 0.00 USD | 339.84 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 31,640.00 USD | 0.00 USD | 930.52 USD | `-8.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 30,710.00 USD | 0.00 USD | 127.62 USD | `-7.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 30,580.00 USD | 0.00 USD | 127.30 USD | `-7.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 30,450.00 USD | 0.00 USD | 9,410.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 21,040.00 USD | 0.00 USD | 127.63 USD | `-6.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 20,910.00 USD | 0.00 USD | 151.62 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 20,760.00 USD | 0.00 USD | 999.82 USD | `-6.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 19,760.00 USD | 0.00 USD | 1,710.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 18,040.00 USD | 0.00 USD | 127.36 USD | `-5.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 17,920.00 USD | 0.00 USD | 780.04 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 17,140.00 USD | 0.00 USD | 127.27 USD | `-5.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 17,010.00 USD | 0.00 USD | 999.65 USD | `-5.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 16,010.00 USD | 0.00 USD | 533.37 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 15,480.00 USD | 0.00 USD | 8,930.00 USD | `-3.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 6,550.00 USD | 0.00 USD | 265.69 USD | `-3.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 6,280.00 USD | 0.00 USD | 597.80 USD | `-2.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 5,690.00 USD | 0.00 USD | 509.04 USD | `-2.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 5,180.00 USD | 0.00 USD | 953.02 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 4,220.00 USD | 0.00 USD | 999.99 USD | `-1.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 3,220.00 USD | 0.00 USD | 1,910.00 USD | `-1.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6075` | 1,320.00 USD | 0.00 USD | 389.92 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 926.40 USD | 0.00 USD | 301.32 USD | `-0.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 625.08 USD | 0.00 USD | 214.78 USD | `-0.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6135` | 410.30 USD | 0.00 USD | 410.30 USD | `-0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6175` | 588.19 USD | 588.19 USD | 0.00 USD | `+0.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 1,710.00 USD | 1,120.00 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 2,710.00 USD | 1,000.00 USD | 0.00 USD | `+1.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 3,150.00 USD | 433.11 USD | 0.00 USD | `+2.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 3,620.00 USD | 469.94 USD | 0.00 USD | `+2.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 8,040.00 USD | 4,430.00 USD | 0.00 USD | `+2.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 8,310.00 USD | 269.44 USD | 0.00 USD | `+2.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 16,710.00 USD | 8,390.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 17,910.00 USD | 1,200.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 27,590.00 USD | 9,680.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6415` | 35,190.00 USD | 7,600.00 USD | 0.00 USD | `+4.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6425` | 41,070.00 USD | 5,880.00 USD | 0.00 USD | `+4.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 46,360.00 USD | 5,300.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 56,340.00 USD | 9,980.00 USD | 0.00 USD | `+5.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 56,910.00 USD | 567.58 USD | 0.00 USD | `+5.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 57,080.00 USD | 172.51 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 61,160.00 USD | 4,080.00 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 62,600.00 USD | 1,440.00 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 63,180.00 USD | 580.23 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 63,470.00 USD | 289.66 USD | 0.00 USD | `+8.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 63,730.00 USD | 262.60 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 64,020.00 USD | 283.50 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 64,180.00 USD | 162.91 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6735` | 64,490.00 USD | 310.15 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 65,090.00 USD | 598.31 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 65,240.00 USD | 154.30 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 65,460.00 USD | 214.20 USD | 0.00 USD | `+10.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 76,020.00 USD | 10,560.00 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 77,150.00 USD | 1,130.00 USD | 0.00 USD | `+11.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 77,290.00 USD | 140.41 USD | 0.00 USD | `+11.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 77,800.00 USD | 514.80 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 77,910.00 USD | 101.96 USD | 0.00 USD | `+12.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 78,930.00 USD | 1,020.00 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 79,540.00 USD | 610.10 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 79,640.00 USD | 101.38 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 80,430.00 USD | 789.18 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 80,530.00 USD | 102.99 USD | 0.00 USD | `+13.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 80,640.00 USD | 111.08 USD | 0.00 USD | `+14.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 81,340.00 USD | 694.49 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 81,470.00 USD | 132.99 USD | 0.00 USD | `+15.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 81,590.00 USD | 122.04 USD | 0.00 USD | `+15.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 83,430.00 USD | 1,830.00 USD | 0.00 USD | `+16.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 83,610.00 USD | 183.26 USD | 0.00 USD | `+17.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 83,760.00 USD | 147.15 USD | 0.00 USD | `+17.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 90,050.00 USD | 6,290.00 USD | 0.00 USD | `+18.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 90,360.00 USD | 309.91 USD | 0.00 USD | `+18.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 90,520.00 USD | 165.17 USD | 0.00 USD | `+19.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 91,550.00 USD | 1,030.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 101,280.00 USD | 9,730.00 USD | 0.00 USD | `+20.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 101,460.00 USD | 185.43 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 103,630.00 USD | 2,170.00 USD | 0.00 USD | `+21.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 103,950.00 USD | 318.43 USD | 0.00 USD | `+21.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 104,090.00 USD | 141.39 USD | 0.00 USD | `+22.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 108,200.00 USD | 4,120.00 USD | 0.00 USD | `+23.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 108,720.00 USD | 511.82 USD | 0.00 USD | `+23.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 109,590.00 USD | 875.23 USD | 0.00 USD | `+23.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 109,690.00 USD | 103.35 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 109,820.00 USD | 127.48 USD | 0.00 USD | `+24.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 109,920.00 USD | 101.61 USD | 0.00 USD | `+24.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 110,110.00 USD | 186.97 USD | 0.00 USD | `+25.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 110,220.00 USD | 109.43 USD | 0.00 USD | `+25.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 110,390.00 USD | 166.70 USD | 0.00 USD | `+26.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 111,520.00 USD | 1,140.00 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 117,840.00 USD | 6,310.00 USD | 0.00 USD | `+28.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 129,910.00 USD | 12,070.00 USD | 0.00 USD | `+32.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 131,560.00 USD | 1,650.00 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 132,490.00 USD | 929.08 USD | 0.00 USD | `+35.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 173,080.00 USD | 40,590.00 USD | 0.00 USD | `+37.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 189,820.00 USD | 16,740.00 USD | 0.00 USD | `+38.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 202,540.00 USD | 12,720.00 USD | 0.00 USD | `+38.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 214,320.00 USD | 11,780.00 USD | 0.00 USD | `+38.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8555` | 214,430.00 USD | 108.85 USD | 0.00 USD | `+39.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 214,590.00 USD | 159.86 USD | 0.00 USD | `+42.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 215,290.00 USD | 702.20 USD | 0.00 USD | `+46.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 215,490.00 USD | 193.62 USD | 0.00 USD | `+47.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 215,910.00 USD | 424.63 USD | 0.00 USD | `+52.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 218,700.00 USD | 2,790.00 USD | 0.00 USD | `+53.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 219,040.00 USD | 340.54 USD | 0.00 USD | `+54.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 219,150.00 USD | 108.83 USD | 0.00 USD | `+57.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 219,300.00 USD | 145.72 USD | 0.00 USD | `+58.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 221,330.00 USD | 2,030.00 USD | 0.00 USD | `+60.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 221,470.00 USD | 136.10 USD | 0.00 USD | `+62.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 222,020.00 USD | 550.48 USD | 0.00 USD | `+63.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 222,330.00 USD | 314.99 USD | 0.00 USD | `+67.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 222,930.00 USD | 602.17 USD | 0.00 USD | `+71.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 223,290.00 USD | 360.61 USD | 0.00 USD | `+72.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 224,240.00 USD | 942.77 USD | 0.00 USD | `+75.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 224,630.00 USD | 397.19 USD | 0.00 USD | `+79.15%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5220` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `0.5260` | 1,520,000.00 USD | 0.00 USD | 1,520,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.5270` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `0.5290` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 2,560.00 USD | 0.00 USD | 2,270.00 USD |
| `7D` | `0.5300` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 2,560.00 USD | 0.00 USD | 6,810.00 USD |
| `7D` | `0.5310` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 8,680.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5320` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5330` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5350` | 1,480,000.00 USD | 0.00 USD | 1,480,000.00 USD | 2,440.00 USD | 3,040.00 USD | 0.00 USD |
| `7D` | `0.5370` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 1,550.00 USD | 2,940.00 USD |
| `7D` | `0.5400` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 2,920.00 USD | 0.00 USD |
| `7D` | `0.5410` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 8,600.00 USD | 0.00 USD | 13.19 USD |
| `7D` | `0.5420` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,660.00 USD | 1,290.00 USD | 2,940.00 USD |
| `7D` | `0.5430` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 627.61 USD | 4,900.00 USD |
| `7D` | `0.5440` | 1,440,000.00 USD | 0.00 USD | 1,440,000.00 USD | 0.00 USD | 523.59 USD | 8,730.00 USD |
| `7D` | `0.5450` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 2,250.00 USD | 0.00 USD | 2,060.00 USD |
| `7D` | `0.5460` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 3,030.00 USD | 3,240.00 USD |
| `7D` | `0.5470` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 795.70 USD | 29.80 USD |
| `7D` | `0.5480` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,000.00 USD | 0.00 USD | 4,470.00 USD |
| `7D` | `0.5490` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 2,100.00 USD | 474.54 USD | 2,040.00 USD |
| `1D` | `0.5500` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,410.00 USD | 0.00 USD | 38.17 USD |
| `7D` | `0.5500` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 3,890.00 USD | 967.07 USD | 4,670.00 USD |
| `1D` | `0.5510` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD |
| `7D` | `0.5510` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 1,730.00 USD | 1,920.00 USD | 1,860.00 USD |
| `1D` | `0.5520` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD |
| `7D` | `0.5520` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 2,380.00 USD | 0.00 USD | 20.49 USD |
| `1D` | `0.5530` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 2,560.00 USD | 1,410.00 USD | 2,300.00 USD |
| `7D` | `0.5530` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 1,650.00 USD | 1,150.00 USD | 16,240.00 USD |
| `1D` | `0.5540` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 5,390.00 USD | 8,430.00 USD | 7,110.00 USD |
| `7D` | `0.5540` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 11,190.00 USD | 8,450.00 USD | 9,490.00 USD |
| `1D` | `0.5550` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 2,940.00 USD | 0.00 USD | 2,800.00 USD |
| `7D` | `0.5550` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 7,070.00 USD | 1,920.00 USD | 5,330.00 USD |
| `1D` | `0.5560` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 4,540.00 USD | 686.25 USD | 2,960.00 USD |
| `7D` | `0.5560` | 1,330,000.00 USD | 0.00 USD | 1,330,000.00 USD | 12,540.00 USD | 1,150.00 USD | 7,690.00 USD |
| `1D` | `0.5570` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 4,670.00 USD | 2,460.00 USD | 7,630.00 USD |
| `7D` | `0.5570` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 812.74 USD | 3,250.00 USD |
| `1D` | `0.5580` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 1,750.00 USD | 3,180.00 USD | 3,140.00 USD |
| `7D` | `0.5580` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 6,000.00 USD | 6,010.00 USD | 15,050.00 USD |
| `1D` | `0.5590` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 1,670.00 USD | 2,150.00 USD | 1,370.00 USD |
| `7D` | `0.5590` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 2,660.00 USD | 7,220.00 USD | 2,470.00 USD |
| `1D` | `0.5600` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 1,910.00 USD | 3,830.00 USD |
| `7D` | `0.5600` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 1,410.00 USD | 938.63 USD | 104.99 USD |
| `1D` | `0.5610` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 2,240.00 USD | 500.33 USD | 823.46 USD |
| `7D` | `0.5610` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 13,590.00 USD | 1,960.00 USD | 7,880.00 USD |
| `1D` | `0.5620` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 1,800.00 USD | 995.72 USD | 2,180.00 USD |
| `7D` | `0.5620` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 12,860.00 USD | 5,460.00 USD | 3,660.00 USD |
| `1D` | `0.5630` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 7,800.00 USD | 1,780.00 USD | 8,090.00 USD |
| `7D` | `0.5630` | 1,210,000.00 USD | 0.00 USD | 1,210,000.00 USD | 14,240.00 USD | 2,380.00 USD | 2,980.00 USD |
| `1D` | `0.5640` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 4,020.00 USD | 3,380.00 USD | 10,730.00 USD |
| `7D` | `0.5640` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 25.29 USD |
| `1D` | `0.5650` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 2,600.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.5650` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 1,210.00 USD | 2,250.00 USD |
| `1D` | `0.5660` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `0.5660` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 11,490.00 USD | 1,780.00 USD | 2,330.00 USD |
| `7D` | `0.5670` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 2,890.00 USD |
| `7D` | `0.5680` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 5,100.00 USD | 0.00 USD | 41.99 USD |
| `1D` | `0.5690` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `7D` | `0.5690` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 6.78 USD |
| `1D` | `0.5700` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.5700` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 1,030.00 USD | 452.37 USD | 1,090.00 USD |
| `1D` | `0.5710` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `7D` | `0.5710` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 2,850.00 USD | 1,350.00 USD |
| `1D` | `0.5720` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `7D` | `0.5720` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 1,520.00 USD | 10,600.00 USD |
| `1D` | `0.5730` | 1,290,000.00 USD | 0.00 USD | 1,290,000.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `7D` | `0.5730` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 2,690.00 USD | 528.82 USD | 5.20 USD |
| `1D` | `0.5740` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 0.00 USD | 839.21 USD | 3,950.00 USD |
| `7D` | `0.5740` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 18,940.00 USD | 574.82 USD | 1,680.00 USD |
| `1D` | `0.5750` | 1,270,000.00 USD | 0.00 USD | 1,270,000.00 USD | 4,330.00 USD | 840.09 USD | 20,160.00 USD |
| `7D` | `0.5750` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 187.30 USD |
| `1D` | `0.5760` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 15,020.00 USD | 2,220.00 USD | 2,120.00 USD |
| `7D` | `0.5760` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 2,150.00 USD | 7,300.00 USD | 19.23 USD |
| `1D` | `0.5770` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD |
| `7D` | `0.5770` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 21,510.00 USD | 0.00 USD | 222.98 USD |
| `1D` | `0.5780` | 1,200,000.00 USD | 0.00 USD | 1,200,000.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD |
| `7D` | `0.5780` | 1,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 19,410.00 USD | 0.00 USD | 1,560.00 USD |
| `1D` | `0.5790` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `7D` | `0.5790` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 1,610.00 USD | 0.00 USD | 11,160.00 USD |
| `1D` | `0.5800` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD |
| `7D` | `0.5800` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 3,900.00 USD | 16,760.00 USD |
| `1D` | `0.5810` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD |
| `7D` | `0.5810` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `1D` | `0.5820` | 1,140,000.00 USD | 0.00 USD | 1,140,000.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD |
| `7D` | `0.5820` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 3,420.00 USD |
| `1D` | `0.5830` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD |
| `1D` | `0.5840` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 2,190.00 USD | 4,320.00 USD |
| `7D` | `0.5840` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 21,370.00 USD |
| `1D` | `0.5850` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 2,950.00 USD | 0.00 USD | 30,870.00 USD |
| `7D` | `0.5850` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | 396.16 USD |
| `1D` | `0.5860` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 2,810.00 USD | 2,450.00 USD | 7,900.00 USD |
| `1D` | `0.5870` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 12,190.00 USD | 2,310.00 USD | 0.00 USD |
| `7D` | `0.5870` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 1,400.00 USD | 65.70 USD |
| `1D` | `0.5880` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 34,650.00 USD | 8,680.00 USD | 7,790.00 USD |
| `7D` | `0.5880` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 3,110.00 USD | 14,610.00 USD | 0.00 USD |
| `1D` | `0.5890` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 39,360.00 USD | 11,450.00 USD | 6,790.00 USD |
| `7D` | `0.5890` | 989,960.00 USD | 0.00 USD | 989,960.00 USD | 43,020.00 USD | 0.00 USD | 8,730.00 USD |
| `1D` | `0.5900` | 943,490.00 USD | 0.00 USD | 943,490.00 USD | 24,340.00 USD | 14,260.00 USD | 18,380.00 USD |
| `7D` | `0.5900` | 938,210.00 USD | 0.00 USD | 938,210.00 USD | 61,220.00 USD | 1,560.00 USD | 9,130.00 USD |
| `1D` | `0.5910` | 886,510.00 USD | 0.00 USD | 886,510.00 USD | 31,110.00 USD | 17,770.00 USD | 19,290.00 USD |
| `7D` | `0.5910` | 866,300.00 USD | 0.00 USD | 866,300.00 USD | 0.00 USD | 15,190.00 USD | 16,670.00 USD |
| `1D` | `0.5920` | 818,330.00 USD | 0.00 USD | 818,330.00 USD | 26,620.00 USD | 6,570.00 USD | 9,970.00 USD |
| `7D` | `0.5920` | 834,450.00 USD | 0.00 USD | 834,450.00 USD | 11,690.00 USD | 10,620.00 USD | 58,810.00 USD |
| `1D` | `0.5930` | 775,170.00 USD | 0.00 USD | 775,170.00 USD | 11,360.00 USD | 6,380.00 USD | 22,390.00 USD |
| `7D` | `0.5930` | 753,320.00 USD | 0.00 USD | 753,320.00 USD | 25,390.00 USD | 2,880.00 USD | 14,120.00 USD |
| `1D` | `0.5940` | 735,050.00 USD | 0.00 USD | 735,050.00 USD | 23,730.00 USD | 2,040.00 USD | 16,430.00 USD |
| `7D` | `0.5940` | 710,930.00 USD | 0.00 USD | 710,930.00 USD | 5,780.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5950` | 692,840.00 USD | 0.00 USD | 692,840.00 USD | 37,990.00 USD | 4,980.00 USD | 1,640.00 USD |
| `7D` | `0.5950` | 705,150.00 USD | 0.00 USD | 705,150.00 USD | 13,060.00 USD | 0.00 USD | 301.29 USD |
| `1D` | `0.5960` | 648,240.00 USD | 0.00 USD | 648,240.00 USD | 11,510.00 USD | 2,560.00 USD | 8,580.00 USD |
| `7D` | `0.5960` | 691,790.00 USD | 0.00 USD | 691,790.00 USD | 5,120.00 USD | 18,410.00 USD | 241.99 USD |
| `1D` | `0.5970` | 625,590.00 USD | 0.00 USD | 625,590.00 USD | 12,870.00 USD | 532.93 USD | 5,180.00 USD |
| `1D` | `0.5980` | 607,010.00 USD | 0.00 USD | 607,010.00 USD | 15,950.00 USD | 4,300.00 USD | 52.44 USD |
| `7D` | `0.5980` | 668,020.00 USD | 0.00 USD | 668,020.00 USD | 37,820.00 USD | 0.00 USD | 3.00 USD |
| `1D` | `0.5990` | 586,710.00 USD | 0.00 USD | 586,710.00 USD | 6,880.00 USD | 1,700.00 USD | 1,090.00 USD |
| `7D` | `0.5990` | 630,200.00 USD | 0.00 USD | 630,200.00 USD | 3,320.00 USD | 0.00 USD | 52.70 USD |
| `1D` | `0.6000` | 577,040.00 USD | 0.00 USD | 577,040.00 USD | 22,910.00 USD | 3,360.00 USD | 10,870.00 USD |
| `7D` | `0.6000` | 626,820.00 USD | 0.00 USD | 626,820.00 USD | 16,110.00 USD | 0.00 USD | 11,950.00 USD |
| `1D` | `0.6010` | 539,900.00 USD | 0.00 USD | 539,900.00 USD | 5,480.00 USD | 6,370.00 USD | 5,020.00 USD |
| `7D` | `0.6010` | 598,770.00 USD | 0.00 USD | 598,770.00 USD | 12,110.00 USD | 4,090.00 USD | 50.15 USD |
| `1D` | `0.6020` | 523,020.00 USD | 0.00 USD | 523,020.00 USD | 11,780.00 USD | 8,040.00 USD | 15,300.00 USD |
| `7D` | `0.6020` | 582,520.00 USD | 0.00 USD | 582,520.00 USD | 0.00 USD | 7,150.00 USD | 17,420.00 USD |
| `1D` | `0.6030` | 487,900.00 USD | 0.00 USD | 487,900.00 USD | 40,580.00 USD | 17,840.00 USD | 20,110.00 USD |
| `7D` | `0.6030` | 557,950.00 USD | 0.00 USD | 557,950.00 USD | 38,530.00 USD | 0.00 USD | 18,260.00 USD |
| `1D` | `0.6040` | 409,370.00 USD | 0.00 USD | 409,370.00 USD | 16,550.00 USD | 20,270.00 USD | 7,580.00 USD |
| `7D` | `0.6040` | 501,160.00 USD | 0.00 USD | 501,160.00 USD | 0.00 USD | 30,380.00 USD | 89.59 USD |
| `1D` | `0.6050` | 364,980.00 USD | 0.00 USD | 364,980.00 USD | 23,200.00 USD | 2,140.00 USD | 13,690.00 USD |
| `7D` | `0.6050` | 470,680.00 USD | 0.00 USD | 470,680.00 USD | 0.00 USD | 0.00 USD | 20,810.00 USD |
| `1D` | `0.6060` | 325,940.00 USD | 0.00 USD | 325,940.00 USD | 22,710.00 USD | 0.00 USD | 18,880.00 USD |
| `7D` | `0.6060` | 449,870.00 USD | 0.00 USD | 449,870.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD |
| `1D` | `0.6070` | 284,350.00 USD | 0.00 USD | 284,350.00 USD | 27,430.00 USD | 4,080.00 USD | 16,080.00 USD |
| `7D` | `0.6070` | 385,290.00 USD | 0.00 USD | 385,290.00 USD | 11,560.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6080` | 236,760.00 USD | 0.00 USD | 236,760.00 USD | 26,190.00 USD | 6,680.00 USD | 3,080.00 USD |
| `7D` | `0.6080` | 373,730.00 USD | 0.00 USD | 373,730.00 USD | 2,860.00 USD | 0.00 USD | 30,370.00 USD |
| `1D` | `0.6090` | 200,820.00 USD | 0.00 USD | 200,820.00 USD | 11,540.00 USD | 3,030.00 USD | 0.00 USD |
| `7D` | `0.6090` | 340,500.00 USD | 0.00 USD | 340,500.00 USD | 13,920.00 USD | 44,860.00 USD | 25,120.00 USD |
| `1D` | `0.6100` | 186,250.00 USD | 0.00 USD | 186,250.00 USD | 3,470.00 USD | 1,070.00 USD | 41,540.00 USD |
| `7D` | `0.6100` | 256,600.00 USD | 0.00 USD | 256,600.00 USD | 7,480.00 USD | 2,570.00 USD | 0.00 USD |
| `1D` | `0.6110` | 140,160.00 USD | 0.00 USD | 140,160.00 USD | 27,240.00 USD | 7,190.00 USD | 0.00 USD |
| `7D` | `0.6110` | 246,540.00 USD | 0.00 USD | 246,540.00 USD | 34,870.00 USD | 2,210.00 USD | 12,860.00 USD |
| `1D` | `0.6120` | 105,730.00 USD | 0.00 USD | 105,730.00 USD | 43,790.00 USD | 3,410.00 USD | 2,170.00 USD |
| `7D` | `0.6120` | 196,600.00 USD | 0.00 USD | 196,600.00 USD | 35,760.00 USD | 16,650.00 USD | 4,130.00 USD |
| `1D` | `0.6130` | 56,360.00 USD | 0.00 USD | 56,360.00 USD | 0.00 USD | 6,720.00 USD | 40,120.00 USD |
| `7D` | `0.6130` | 140,060.00 USD | 0.00 USD | 140,060.00 USD | 105,970.00 USD | 9,220.00 USD | 18,530.00 USD |
| `1D` | `0.6140` | 9,520.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD | 9,520.00 USD | 0.00 USD |
| `7D` | `0.6140` | 6,330.00 USD | 0.00 USD | 6,330.00 USD | 0.00 USD | 6,170.00 USD | 159.06 USD |
| `1D` | `0.6170` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6180` | 1,760.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.6180` | 173.29 USD | 173.29 USD | 0.00 USD | 0.00 USD | 0.00 USD | 173.29 USD |
| `7D` | `0.6180` | 346.58 USD | 346.58 USD | 0.00 USD | 0.00 USD | 0.00 USD | 173.29 USD |
| `7D` | `0.6190` | 528.69 USD | 528.69 USD | 0.00 USD | 0.00 USD | 0.00 USD | 182.11 USD |
| `1D` | `0.6200` | 1,810.00 USD | 1,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 50.92 USD |
| `7D` | `0.6200` | 43,470.00 USD | 43,470.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 29,070.00 USD |
| `7D` | `0.6210` | 66,110.00 USD | 66,110.00 USD | 0.00 USD | 0.00 USD | 22,640.00 USD | 0.00 USD |
| `7D` | `0.6230` | 66,240.00 USD | 66,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 122.98 USD |
| `7D` | `0.6240` | 73,590.00 USD | 73,590.00 USD | 0.00 USD | 0.00 USD | 7,300.00 USD | 48.83 USD |
| `1D` | `0.6250` | 4,330.00 USD | 4,330.00 USD | 0.00 USD | 2,520.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6260` | 35,380.00 USD | 35,380.00 USD | 0.00 USD | 9,100.00 USD | 8,370.00 USD | 13,580.00 USD |
| `7D` | `0.6260` | 91,010.00 USD | 91,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 17,420.00 USD |
| `1D` | `0.6270` | 55,640.00 USD | 55,640.00 USD | 0.00 USD | 0.00 USD | 3,780.00 USD | 16,480.00 USD |
| `7D` | `0.6270` | 117,530.00 USD | 117,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 26,520.00 USD |
| `1D` | `0.6280` | 117,850.00 USD | 117,850.00 USD | 0.00 USD | 10,020.00 USD | 26,790.00 USD | 25,400.00 USD |
| `7D` | `0.6280` | 168,460.00 USD | 168,460.00 USD | 0.00 USD | 0.00 USD | 34,280.00 USD | 16,650.00 USD |
| `1D` | `0.6290` | 168,570.00 USD | 168,570.00 USD | 0.00 USD | 23,200.00 USD | 7,350.00 USD | 20,170.00 USD |
| `7D` | `0.6290` | 217,270.00 USD | 217,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 48,810.00 USD |
| `1D` | `0.6300` | 225,370.00 USD | 225,370.00 USD | 0.00 USD | 25,290.00 USD | 3,430.00 USD | 28,080.00 USD |
| `7D` | `0.6300` | 281,860.00 USD | 281,860.00 USD | 0.00 USD | 30,590.00 USD | 5,760.00 USD | 28,240.00 USD |
| `1D` | `0.6310` | 310,870.00 USD | 310,870.00 USD | 0.00 USD | 38,850.00 USD | 8,860.00 USD | 37,790.00 USD |
| `7D` | `0.6310` | 293,520.00 USD | 293,520.00 USD | 0.00 USD | 11,560.00 USD | 0.00 USD | 103.98 USD |
| `1D` | `0.6320` | 386,110.00 USD | 386,110.00 USD | 0.00 USD | 51,560.00 USD | 9,600.00 USD | 14,080.00 USD |
| `7D` | `0.6320` | 293,780.00 USD | 293,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 265.37 USD |
| `1D` | `0.6330` | 428,160.00 USD | 428,160.00 USD | 0.00 USD | 14,490.00 USD | 12,370.00 USD | 15,190.00 USD |
| `7D` | `0.6330` | 351,980.00 USD | 351,980.00 USD | 0.00 USD | 57,940.00 USD | 0.00 USD | 259.82 USD |
| `1D` | `0.6340` | 502,090.00 USD | 502,090.00 USD | 0.00 USD | 28,910.00 USD | 4,250.00 USD | 40,770.00 USD |
| `7D` | `0.6340` | 362,830.00 USD | 362,830.00 USD | 0.00 USD | 10,730.00 USD | 0.00 USD | 121.40 USD |
| `1D` | `0.6350` | 565,740.00 USD | 565,740.00 USD | 0.00 USD | 54,290.00 USD | 5,510.00 USD | 3,850.00 USD |
| `7D` | `0.6350` | 432,410.00 USD | 432,410.00 USD | 0.00 USD | 69,190.00 USD | 0.00 USD | 386.01 USD |
| `1D` | `0.6360` | 657,060.00 USD | 657,060.00 USD | 0.00 USD | 49,770.00 USD | 5,880.00 USD | 35,670.00 USD |
| `7D` | `0.6360` | 489,000.00 USD | 489,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 56,590.00 USD |
| `1D` | `0.6370` | 667,470.00 USD | 667,470.00 USD | 0.00 USD | 0.00 USD | 2,880.00 USD | 7,540.00 USD |
| `7D` | `0.6370` | 498,180.00 USD | 498,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 9,180.00 USD |
| `1D` | `0.6380` | 754,950.00 USD | 754,950.00 USD | 0.00 USD | 47,080.00 USD | 23,740.00 USD | 16,660.00 USD |
| `7D` | `0.6380` | 575,020.00 USD | 575,020.00 USD | 0.00 USD | 32,220.00 USD | 0.00 USD | 44,610.00 USD |
| `1D` | `0.6390` | 827,200.00 USD | 827,200.00 USD | 0.00 USD | 12,760.00 USD | 6,680.00 USD | 52,810.00 USD |
| `7D` | `0.6390` | 636,700.00 USD | 636,700.00 USD | 0.00 USD | 24,230.00 USD | 15,680.00 USD | 21,780.00 USD |
| `1D` | `0.6400` | 951,150.00 USD | 951,150.00 USD | 0.00 USD | 66,560.00 USD | 38,500.00 USD | 18,890.00 USD |
| `7D` | `0.6400` | 665,100.00 USD | 665,100.00 USD | 0.00 USD | 19,270.00 USD | 0.00 USD | 9,130.00 USD |
| `1D` | `0.6410` | 1,020,000.00 USD | 1,020,000.00 USD | 0.00 USD | 34,570.00 USD | 19,840.00 USD | 15,770.00 USD |
| `7D` | `0.6410` | 695,470.00 USD | 695,470.00 USD | 0.00 USD | 0.00 USD | 24,060.00 USD | 6,310.00 USD |
| `1D` | `0.6420` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 57,140.00 USD | 9,980.00 USD | 15,000.00 USD |
| `7D` | `0.6420` | 807,080.00 USD | 807,080.00 USD | 0.00 USD | 55,350.00 USD | 26,560.00 USD | 29,700.00 USD |
| `1D` | `0.6430` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 24,220.00 USD | 10,750.00 USD | 33,200.00 USD |
| `7D` | `0.6430` | 865,900.00 USD | 865,900.00 USD | 0.00 USD | 31,500.00 USD | 10,020.00 USD | 17,300.00 USD |
| `1D` | `0.6440` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 34,630.00 USD | 14,890.00 USD | 56,530.00 USD |
| `7D` | `0.6440` | 932,540.00 USD | 932,540.00 USD | 0.00 USD | 34,270.00 USD | 17,680.00 USD | 14,690.00 USD |
| `1D` | `0.6450` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 62,440.00 USD | 14,460.00 USD | 15,770.00 USD |
| `7D` | `0.6450` | 1,070,000.00 USD | 1,070,000.00 USD | 0.00 USD | 81,220.00 USD | 15,560.00 USD | 35,760.00 USD |
| `1D` | `0.6460` | 1,420,000.00 USD | 1,420,000.00 USD | 0.00 USD | 25,640.00 USD | 12,810.00 USD | 9,710.00 USD |
| `7D` | `0.6460` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 91,390.00 USD | 31,070.00 USD | 102,630.00 USD |
| `1D` | `0.6470` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 52,770.00 USD | 17,750.00 USD | 11,980.00 USD |
| `7D` | `0.6470` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 9,660.00 USD | 26,520.00 USD | 9,470.00 USD |
| `1D` | `0.6480` | 1,590,000.00 USD | 1,590,000.00 USD | 0.00 USD | 78,190.00 USD | 9,530.00 USD | 392.53 USD |
| `7D` | `0.6480` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 94,210.00 USD | 0.00 USD | 23,940.00 USD |
| `1D` | `0.6490` | 1,650,000.00 USD | 1,650,000.00 USD | 0.00 USD | 46,110.00 USD | 2,940.00 USD | 12,200.00 USD |
| `7D` | `0.6490` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 36,340.00 USD | 0.00 USD | 17,650.00 USD |
| `1D` | `0.6500` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 52,920.00 USD | 9,280.00 USD | 5,990.00 USD |
| `7D` | `0.6500` | 1,680,000.00 USD | 1,680,000.00 USD | 0.00 USD | 53,330.00 USD | 0.00 USD | 122,040.00 USD |
| `1D` | `0.6510` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 56,160.00 USD | 0.00 USD | 14,330.00 USD |
| `7D` | `0.6510` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 244,480.00 USD | 8,270.00 USD | 18,220.00 USD |
| `1D` | `0.6520` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 70,440.00 USD | 13,800.00 USD | 5,780.00 USD |
| `7D` | `0.6520` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 65,690.00 USD | 6,720.00 USD | 86,550.00 USD |
| `1D` | `0.6530` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 18,010.00 USD | 3,910.00 USD | 11.74 USD |
| `7D` | `0.6530` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 4,440.00 USD | 47,250.00 USD |
| `1D` | `0.6540` | 1,930,000.00 USD | 1,930,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 4,910.00 USD |
| `7D` | `0.6540` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 15,730.00 USD | 0.00 USD | 14,640.00 USD |
| `1D` | `0.6550` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `7D` | `0.6550` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 414.15 USD |
| `1D` | `0.6560` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,020.00 USD |
| `7D` | `0.6560` | 2,200,000.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 507.31 USD |
| `1D` | `0.6570` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,460.00 USD |
| `7D` | `0.6570` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 6,350.00 USD | 447.57 USD |
| `1D` | `0.6580` | 1,950,000.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 48.99 USD |
| `7D` | `0.6580` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 21,920.00 USD | 9,580.00 USD |
| `1D` | `0.6590` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `7D` | `0.6590` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 0.00 USD | 11,320.00 USD | 331.05 USD |
| `1D` | `0.6600` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD |
| `7D` | `0.6600` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 7,100.00 USD | 249.08 USD |
| `1D` | `0.6610` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD |
| `7D` | `0.6610` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6620` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD |
| `7D` | `0.6620` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 128.16 USD |
| `1D` | `0.6630` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD |
| `7D` | `0.6630` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 254.70 USD |
| `1D` | `0.6640` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD |
| `7D` | `0.6640` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 7,050.00 USD |
| `1D` | `0.6650` | 2,030,000.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `7D` | `0.6650` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 288.69 USD |
| `1D` | `0.6660` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD |
| `7D` | `0.6660` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 148.18 USD |
| `1D` | `0.6670` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `7D` | `0.6670` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 308.18 USD |
| `1D` | `0.6680` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 158.16 USD |
| `7D` | `0.6680` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 224.19 USD |
| `1D` | `0.6690` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `7D` | `0.6690` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 448.05 USD |
| `1D` | `0.6700` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 546.45 USD |
| `1D` | `0.6710` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD |
| `7D` | `0.6710` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,140.00 USD |
| `1D` | `0.6720` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6730` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD |
| `7D` | `0.6730` | 2,410,000.00 USD | 2,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 99.42 USD |
| `1D` | `0.6740` | 2,270,000.00 USD | 2,270,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6750` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 30,000.00 USD | 1,410.00 USD | 14,370.00 USD |
| `7D` | `0.6750` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 75,730.00 USD | 3,480.00 USD |
| `1D` | `0.6760` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,560,000.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 2,240.00 USD | 33,090.00 USD |
| `1D` | `0.6770` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 19,930.00 USD | 9,080.00 USD | 17,950.00 USD |
| `7D` | `0.6770` | 2,650,000.00 USD | 2,650,000.00 USD | 0.00 USD | 63,600.00 USD | 4,190.00 USD | 21,590.00 USD |
| `1D` | `0.6780` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 33,610.00 USD | 9,900.00 USD | 12,150.00 USD |
| `7D` | `0.6780` | 2,660,000.00 USD | 2,660,000.00 USD | 0.00 USD | 0.00 USD | 14,960.00 USD | 124.93 USD |
| `1D` | `0.6790` | 2,470,000.00 USD | 2,470,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 13,680.00 USD |
| `7D` | `0.6790` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,160.00 USD |
| `1D` | `0.6800` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 4,540.00 USD | 686.25 USD | 5,410.00 USD |
| `7D` | `0.6800` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 6,120.00 USD | 1,150.00 USD | 2,610.00 USD |
| `1D` | `0.6810` | 2,500,000.00 USD | 2,500,000.00 USD | 0.00 USD | 4,670.00 USD | 2,460.00 USD | 15,190.00 USD |
| `7D` | `0.6810` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 15,720.00 USD | 145.79 USD |
| `1D` | `0.6820` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 24,350.00 USD | 16,950.00 USD | 9,650.00 USD |
| `7D` | `0.6820` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 32,570.00 USD | 37,730.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 26,250.00 USD | 15,380.00 USD | 36,820.00 USD |
| `7D` | `0.6830` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 17,730.00 USD | 48,260.00 USD |
| `1D` | `0.6840` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 45,780.00 USD | 12,210.00 USD | 15,180.00 USD |
| `7D` | `0.6840` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 57,890.00 USD | 36,580.00 USD | 54,240.00 USD |
| `1D` | `0.6850` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 29,890.00 USD | 6,280.00 USD | 24,100.00 USD |
| `7D` | `0.6850` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 24,240.00 USD | 4,710.00 USD | 10,480.00 USD |
| `1D` | `0.6860` | 2,820,000.00 USD | 2,820,000.00 USD | 0.00 USD | 42,050.00 USD | 4,600.00 USD | 14,780.00 USD |
| `7D` | `0.6860` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 32,660.00 USD | 9,830.00 USD | 0.00 USD |
| `7D` | `0.6870` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 19,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6880` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 24,610.00 USD | 17,300.00 USD | 2,900.00 USD |
| `7D` | `0.6890` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 4,850.00 USD | 12,670.00 USD | 77.75 USD |
| `7D` | `0.6900` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 4,480.00 USD | 16,550.00 USD |
| `7D` | `0.6910` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 37,650.00 USD |
| `7D` | `0.6920` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,370.00 USD |
| `7D` | `0.6930` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,600.00 USD |
| `7D` | `0.6950` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 31,450.00 USD | 0.00 USD | 12,390.00 USD |
| `7D` | `0.6960` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 28,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6970` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 21,650.00 USD | 6,030.00 USD | 0.00 USD |
| `7D` | `0.6980` | 3,500,000.00 USD | 3,500,000.00 USD | 0.00 USD | 14,330.00 USD | 10,960.00 USD | 0.00 USD |
| `7D` | `0.6990` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 13,410.00 USD | 0.00 USD | 30,200.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `86.78M` | Total OI Tokens: `140,379,933.4 APT`
  * 1h OI Change: `+0.13%` | 4h OI Change: `+0.17%` | 24h OI Change: `-10.47%`
  * Exchange Breakdown: Binance=`15.62M` | Bybit=`17.09M` | OKX=`4.16M` | Hyperliquid=`3.48M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `2.33K` | Last 24h: `836.23` | Last 3d: `10.58K` | Last 7d: `3.38K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0059%` | **USDT OKX** | `-0.0040%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `-0.0007%` |
| **USDT MEXC** | `0.0059%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0086%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `37.56%` | `62.44%` | `0.60` | 3,390,000.00 USD |
| `15M` | `Binance` | `32.12%` | `67.88%` | `0.47` | 939,500.00 USD |
| `15M` | `OKX` | `29.47%` | `70.53%` | `0.42` | 218,950.00 USD |
| `15M` | `Bybit` | `41.8%` | `58.2%` | `0.72` | 167,280.00 USD |
| `15M` | `KuCoin` | `49.1%` | `50.9%` | `0.96` | 24,070.00 USD |
| `15M` | `Gate` | `44.51%` | `55.49%` | `0.80` | 307,810.00 USD |
| `15M` | `Bitget` | `68.07%` | `31.93%` | `2.13` | 53,700.00 USD |
| `15M` | `BingX` | `18.37%` | `81.63%` | `0.23` | 1,140,000.00 USD |
| `15M` | `MEXC` | `58.54%` | `41.46%` | `1.41` | 16,140.00 USD |
| `15M` | `Bitunix` | `30.34%` | `69.66%` | `0.44` | 39,200.00 USD |
| `15M` | `Hyperliquid` | `66.9%` | `33.1%` | `2.02` | 4,350.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.34%` | `50.66%` | `0.97` | 79,040.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `96.73%` | `3.27%` | `29.58` | 233,410.00 USD |
| `15M` | `HTX` | `80.57%` | `19.43%` | `4.15` | 5,160.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `72.31%` | `27.69%` | `2.61` | 17,880.00 USD |
| `15M` | `Aster` | `0%` | `100%` | `0.00` | 249.02 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `93.39%` | `6.61%` | `14.13` | 146,610.00 USD |
| `15M` | `Whale Positions` | `32.12%` | `67.88%` | `0.47` | 939,500.00 USD |
| `15M` | `Global Accounts` | `37.56%` | `62.44%` | `0.60` | 3,390,000.00 USD |
| `1H` | `APT` | `50.52%` | `49.48%` | `1.02` | 8,080,000.00 USD |
| `1H` | `Binance` | `35.35%` | `64.65%` | `0.55` | 1,500,000.00 USD |
| `1H` | `OKX` | `45.03%` | `54.97%` | `0.82` | 574,340.00 USD |
| `1H` | `Bybit` | `38.7%` | `61.3%` | `0.63` | 414,750.00 USD |
| `1H` | `KuCoin` | `49.71%` | `50.29%` | `0.99` | 335,710.00 USD |
| `1H` | `Gate` | `60.68%` | `39.32%` | `1.54` | 111,870.00 USD |
| `1H` | `Bitget` | `67.05%` | `32.95%` | `2.03` | 155,230.00 USD |
| `1H` | `BingX` | `51.05%` | `48.95%` | `1.04` | 395,640.00 USD |
| `1H` | `MEXC` | `41.2%` | `58.8%` | `0.70` | 228,980.00 USD |
| `1H` | `Bitunix` | `48.56%` | `51.44%` | `0.94` | 121,370.00 USD |
| `1H` | `Hyperliquid` | `22.27%` | `77.73%` | `0.29` | 104,140.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.98%` | `50.02%` | `1.00` | 3,200,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `88.23%` | `11.77%` | `7.50` | 880,820.00 USD |
| `1H` | `HTX` | `29.93%` | `70.07%` | `0.43` | 4,480.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `62.52%` | `37.48%` | `1.67` | 30,210.00 USD |
| `1H` | `Aster` | `45.34%` | `54.66%` | `0.83` | 991.42 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `89.29%` | `10.71%` | `8.34` | 19,230.00 USD |
| `1H` | `Whale Positions` | `35.35%` | `64.65%` | `0.55` | 1,500,000.00 USD |
| `1H` | `Global Accounts` | `50.52%` | `49.48%` | `1.02` | 8,080,000.00 USD |
| `4H` | `APT` | `47.16%` | `52.84%` | `0.89` | 42,680,000.00 USD |
| `4H` | `Binance` | `49.2%` | `50.8%` | `0.97` | 11,890,000.00 USD |
| `4H` | `OKX` | `40.61%` | `59.39%` | `0.68` | 4,410,000.00 USD |
| `4H` | `Bybit` | `51.48%` | `48.52%` | `1.06` | 3,230,000.00 USD |
| `4H` | `KuCoin` | `44.69%` | `55.31%` | `0.81` | 341,720.00 USD |
| `4H` | `Gate` | `50.8%` | `49.2%` | `1.03` | 4,020,000.00 USD |
| `4H` | `Bitget` | `42.55%` | `57.45%` | `0.74` | 1,290,000.00 USD |
| `4H` | `BingX` | `33.49%` | `66.51%` | `0.50` | 10,450,000.00 USD |
| `4H` | `MEXC` | `56.96%` | `43.04%` | `1.32` | 1,060,000.00 USD |
| `4H` | `Bitunix` | `45.69%` | `54.31%` | `0.84` | 971,090.00 USD |
| `4H` | `Hyperliquid` | `45.78%` | `54.22%` | `0.84` | 363,880.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.8%` | `49.2%` | `1.03` | 1,010,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `91.29%` | `8.71%` | `10.48` | 2,850,000.00 USD |
| `4H` | `HTX` | `49.82%` | `50.18%` | `0.99` | 53,370.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `42.28%` | `57.72%` | `0.73` | 80,460.00 USD |
| `4H` | `Aster` | `40.94%` | `59.06%` | `0.69` | 19,410.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `28.33%` | `71.67%` | `0.40` | 629,100.00 USD |
| `4H` | `Whale Positions` | `49.2%` | `50.8%` | `0.97` | 11,890,000.00 USD |
| `4H` | `Global Accounts` | `47.16%` | `52.84%` | `0.89` | 42,680,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `0.6193` | `0.6186` | `0.6193` | `0.6199` | `0.6168` | 453,632.84 USD | 294,361.17 USD | 159,271.67 USD | 135,089.51 USD | `+29.78%` | `6B / 1S` |
| `0:00 UTC` | `0.6190` | `0.6189` | `0.6190` | `0.6221` | `0.6169` | 281,500.66 USD | 161,174.25 USD | 120,326.41 USD | 40,847.84 USD | `+14.51%` | `12B / 4S` |
| `5:00 UTC` | `0.6206` | `0.6207` | `0.6206` | `0.6228` | `0.6190` | 259,699.58 USD | 123,300.67 USD | 136,398.91 USD | -13,098.24 USD | `-5.04%` | `4B / 8S` |
| `0:00 UTC` | `0.6208` | `0.6182` | `0.6208` | `0.6208` | `0.6153` | 335,089.06 USD | 145,222.32 USD | 189,866.74 USD | -44,644.43 USD | `-13.32%` | `3B / 19S` |
| `5:00 UTC` | `0.6160` | `0.6165` | `0.6160` | `0.6201` | `0.6149` | 344,140.22 USD | 188,669.15 USD | 155,471.07 USD | 33,198.09 USD | `+9.65%` | `14B / 12S` |
| `0:00 UTC` | `0.6158` | `0.6153` | `0.6158` | `0.6177` | `0.6136` | 428,959.14 USD | 201,402.03 USD | 227,557.12 USD | -26,155.09 USD | `-6.10%` | `3B / 7S` |
| `5:00 UTC` | `0.6158` | `0.6152` | `0.6158` | `0.6166` | `0.6136` | 219,959.16 USD | 99,252.63 USD | 120,706.54 USD | -21,453.91 USD | `-9.75%` | `3B / 6S` |
| `0:00 UTC` | `0.6141` | `0.6141` | `0.6141` | `0.6168` | `0.6118` | 465,814.11 USD | 219,511.96 USD | 246,302.16 USD | -26,790.20 USD | `-5.75%` | `11B / 9S` |
| `5:00 UTC` | `0.6133` | `0.6164` | `0.6133` | `0.6190` | `0.6129` | 353,127.32 USD | 155,401.13 USD | 197,726.18 USD | -42,325.05 USD | `-11.99%` | `13B / 7S` |
| `0:00 UTC` | `0.6183` | `0.6182` | `0.6183` | `0.6190` | `0.6173` | 128,017.23 USD | 84,609.35 USD | 43,407.87 USD | 41,201.48 USD | `+32.18%` | `5B / 2S` |

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
| `5m` | -3,730.00 USD | -84,680.00 USD | **`DISTRIBUTION`** |
| `15m` | 75,190.00 USD | -44,360.00 USD | **`ACCUMULATION`** |
| `30m` | 77,500.00 USD | -12,440.00 USD | **`ACCUMULATION`** |
| `1h` | 41,480.00 USD | -100,190.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,170.00 USD | 139,890.00 USD | **`ACCUMULATION`** |
| `4h` | -54,300.00 USD | -59,610.00 USD | **`DISTRIBUTION`** |
| `6h` | -392,800.00 USD | -485,960.00 USD | **`DISTRIBUTION`** |
| `8h` | -172,020.00 USD | 582,210.00 USD | **`ACCUMULATION`** |
| `12h` | -1,410,000.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,130,000.00 USD | -8,620,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -6,030,000.00 USD | -26,020,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,280,000.00 USD | -105,700,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-3.73K` | 15m=`+75.19K` | 1h=`+41.48K` | 24h=`-1.13M`
* Futures Capital Netflows: 5m=`-84.68K` | 15m=`-44.36K` | 1h=`-100.19K` | 24h=`-8.62M`
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
  * `2026-10-30 15:33:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:00 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:19:00 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:00 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:00 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:00 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:36:00 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:35:00 IST`: [insee.fr] - (Sentiment: `Neutral`)


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
