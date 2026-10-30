# 🏛️ SOVEREIGN CANDIDATE DOSSIER: APT
**Canonical Key**: `APT` | **Broker Instrument**: `APTUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 10:28:44 IST` (`2026-10-30 04:58:44 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
| `5m` | `0.6167` | `0.6184` | `0.6158` | `0.6175` | `158,923` | 98,118.40 USD | 31,627.85 USD | `+32.23%` | -6,087,847.64 USD | `+0.45` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `0.6176` | `0.6181` | `0.6162` | `0.6171` | `206,234` | 127,247.29 USD | -37,747.19 USD | `-29.66%` | -6,125,594.82 USD | `-1.54` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `0.6171` | `0.6173` | `0.6164` | `0.6172` | `107,543` | 66,335.62 USD | -25,066.15 USD | `-37.79%` | -6,150,660.97 USD | `-1.09` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6183` | `0.6184` | `0.6149` | `0.6168` | `506,840` | 312,659.38 USD | 27,478.79 USD | `+8.79%` | -6,181,148.93 USD | `+0.21` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `0.6167` | `0.6184` | `0.6158` | `0.6174` | `539,281` | 332,795.97 USD | -14,158.04 USD | `-4.25%` | -6,195,306.97 USD | `+0.02` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `0.6173` | `0.6222` | `0.6170` | `0.6211` | `788,101` | 488,289.98 USD | -113,087.82 USD | `-23.16%` | -6,308,394.79 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6024` | `0.6109` | `0.5966` | `0.6032` | `3,667,839` | 2,218,815.27 USD | -7,363.46 USD | `-0.33%` | -6,472,195.00 USD | `+0.40` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `0.6032` | `0.6175` | `0.6026` | `0.6161` | `2,079,930` | 1,271,652.33 USD | 258,052.55 USD | `+20.29%` | -6,214,142.45 USD | `+0.71` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `0.6161` | `0.6222` | `0.6117` | `0.6211` | `2,596,114` | 1,602,257.79 USD | -94,252.34 USD | `-5.88%` | -6,308,394.79 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,343,422.64 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,721,248.17 USD | `+0.56` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6186` | `0.6117` | `0.6172` | `1,741,775` | 1,073,084.88 USD | 1,964.09 USD | `+0.18%` | -5,719,284.08 USD | `+0.73` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6713` | `0.7047` | `0.6676` | `0.7036` | `13,569,736` | 9,297,285.20 USD | -148,086.76 USD | `-1.59%` | -208,228.16 USD | `-1.00` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `0.7037` | `0.7077` | `0.6665` | `0.6721` | `16,607,110` | 11,368,753.45 USD | -1,468,928.13 USD | `-12.92%` | -1,677,156.29 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6721` | `0.6728` | `0.6003` | `0.6161` | `56,944,695` | 35,933,598.81 USD | -3,666,266.35 USD | `-10.20%` | -5,343,422.64 USD | `-1.60` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `0.6162` | `0.6185` | `0.5736` | `0.6161` | `24,927,742` | 14,934,999.44 USD | -377,825.53 USD | `-2.53%` | -5,721,248.17 USD | `+0.56` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `0.6161` | `0.6222` | `0.6117` | `0.6214` | `2,598,532` | 1,603,760.10 USD | -92,822.94 USD | `-5.79%` | -5,814,071.11 USD | `+0.67` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`0.6901`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 10:24:51 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| - | Interbank Institutional Desk | - | - | - | - | - | - | - | - | - |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `0.6667` | 375.48 USD | `-` | `NEWS_INTEL` | `-` | #APT Liquidated Short: 0.38K USD at 0.6667 USD [API] | `2026-10-29 02:05:24` |


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
| `Live` | `Long Liquidation` | `0.1395` | 419.65 USD | 207,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1465` | 1,070.00 USD | 207,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1605` | 222.83 USD | 206,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.1875` | 269.27 USD | 206,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2185` | 226.83 USD | 205,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2355` | 2,660.00 USD | 205,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2415` | 243.01 USD | 202,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.2425` | 1,460.00 USD | 202,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3105` | 105.38 USD | 201,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3175` | 1,590.00 USD | 201,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3305` | 9,950.00 USD | 199,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3395` | 679.34 USD | 189,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3545` | 177.25 USD | 188,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3585` | 12,850.00 USD | 188,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3675` | 189.99 USD | 175,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3785` | 567.75 USD | 175,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3905` | 359.26 USD | 175,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3955` | 2,640.00 USD | 174,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.3995` | 271.06 USD | 172,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4035` | 282.45 USD | 171,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4125` | 1,070.00 USD | 171,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4135` | 1,600.00 USD | 170,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4185` | 630.86 USD | 168,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4255` | 224.96 USD | 168,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4395` | 444.97 USD | 167,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4435` | 5,510.00 USD | 167,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4475` | 226.63 USD | 162,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4515` | 27,090.00 USD | 161,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4535` | 5,970.00 USD | 134,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4605` | 430.79 USD | 128,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4615` | 595.82 USD | 128,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4625` | 1,460.00 USD | 127,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4645` | 876.05 USD | 126,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4685` | 1,350.00 USD | 125,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4765` | 4,400.00 USD | 124,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4835` | 135.33 USD | 119,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4855` | 181.88 USD | 119,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4865` | 3,330.00 USD | 119,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4925` | 10,520.00 USD | 115,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4935` | 1,580.00 USD | 105,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4945` | 7,030.00 USD | 103,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4955` | 3,180.00 USD | 96,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4965` | 143.19 USD | 93,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4975` | 667.49 USD | 93,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.4985` | 429.90 USD | 92,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5075` | 303.42 USD | 92,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5085` | 102.82 USD | 92,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5105` | 519.77 USD | 92,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5125` | 248.05 USD | 91,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5135` | 298.60 USD | 91,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5175` | 9,440.00 USD | 90,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5185` | 281.56 USD | 81,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5240` | 1,180,000.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5245` | 209.80 USD | 81,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5260` | 1,180,000.00 USD | 1,180,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5280` | 1,170,000.00 USD | 1,170,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5295` | 1,840.00 USD | 81,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5300` | 1,160,000.00 USD | 1,160,000.00 USD | 5,120.00 USD | 0.00 USD | 9,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5315` | 11,510.00 USD | 79,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5320` | 1,150,000.00 USD | 1,150,000.00 USD | 8,680.00 USD | 0.00 USD | 3,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5325` | 2,260.00 USD | 67,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `0.5335` | 163.22 USD | 65,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5340` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5360` | 1,130,000.00 USD | 1,130,000.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5380` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 1,550.00 USD | 2,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5400` | 1,120,000.00 USD | 1,120,000.00 USD | 0.00 USD | 2,920.00 USD | 80.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5410` | 1,040,000.00 USD | 1,040,000.00 USD | 13,320.00 USD | 1,980.00 USD | 3,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5420` | 1,020,000.00 USD | 1,020,000.00 USD | 2,590.00 USD | 530.84 USD | 2,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5420` | 1,120,000.00 USD | 1,120,000.00 USD | 16,260.00 USD | 1,290.00 USD | 2,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5430` | 1,020,000.00 USD | 1,020,000.00 USD | 3,300.00 USD | 0.00 USD | 2,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5440` | 1,010,000.00 USD | 1,010,000.00 USD | 0.00 USD | 837.01 USD | 552.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5440` | 1,100,000.00 USD | 1,100,000.00 USD | 0.00 USD | 1,150.00 USD | 13,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5445` | 855.28 USD | 65,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5450` | 1,010,000.00 USD | 1,010,000.00 USD | 1,070.00 USD | 1,140.00 USD | 2,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5460` | 1,010,000.00 USD | 1,010,000.00 USD | 3,980.00 USD | 0.00 USD | 585.11 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5460` | 1,080,000.00 USD | 1,080,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,180.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5470` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5475` | 1,630.00 USD | 64,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5480` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 14.03 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5480` | 1,070,000.00 USD | 1,070,000.00 USD | 2,000.00 USD | 795.70 USD | 4,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5490` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5500` | 994,140.00 USD | 994,140.00 USD | 1,410.00 USD | 0.00 USD | 38.17 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5500` | 1,060,000.00 USD | 1,060,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5510` | 992,690.00 USD | 992,690.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5520` | 989,500.00 USD | 989,500.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5520` | 1,050,000.00 USD | 1,050,000.00 USD | 4,110.00 USD | 1,920.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5530` | 988,450.00 USD | 988,450.00 USD | 1,260.00 USD | 1,410.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5540` | 985,780.00 USD | 985,780.00 USD | 5,390.00 USD | 5,750.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5540` | 1,040,000.00 USD | 1,040,000.00 USD | 12,840.00 USD | 7,260.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5545` | 47,450.00 USD | 62,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5550` | 970,470.00 USD | 970,470.00 USD | 2,940.00 USD | 0.00 USD | 1,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5560` | 965,900.00 USD | 965,900.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5560` | 1,000,000.00 USD | 1,000,000.00 USD | 13,490.00 USD | 1,920.00 USD | 10,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5570` | 963,530.00 USD | 963,530.00 USD | 0.00 USD | 1,940.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5580` | 957,180.00 USD | 957,180.00 USD | 0.00 USD | 2,820.00 USD | 2,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5580` | 977,660.00 USD | 977,660.00 USD | 6,000.00 USD | 6,820.00 USD | 18,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5585` | 10,520.00 USD | 15,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5590` | 951,830.00 USD | 951,830.00 USD | 0.00 USD | 1,870.00 USD | 1,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5600` | 948,600.00 USD | 948,600.00 USD | 0.00 USD | 1,690.00 USD | 2,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5600` | 946,550.00 USD | 946,550.00 USD | 4,070.00 USD | 8,160.00 USD | 2,470.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5610` | 944,360.00 USD | 944,360.00 USD | 0.00 USD | 0.00 USD | 823.46 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5615` | 258.48 USD | 4,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5620` | 943,530.00 USD | 943,530.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5620` | 931,850.00 USD | 931,850.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5630` | 940,570.00 USD | 940,570.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5635` | 244.90 USD | 4,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5640` | 934,410.00 USD | 934,410.00 USD | 4,020.00 USD | 2,420.00 USD | 10,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5640` | 893,400.00 USD | 893,400.00 USD | 2,950.00 USD | 741.21 USD | 53.84 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5655` | 1,920.00 USD | 4,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5660` | 917,930.00 USD | 917,930.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5660` | 889,660.00 USD | 889,660.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5665` | 1,370.00 USD | 2,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `0.5680` | 870,760.00 USD | 870,760.00 USD | 5,100.00 USD | 0.00 USD | 2,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5690` | 914,350.00 USD | 914,350.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5700` | 909,250.00 USD | 909,250.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5700` | 862,740.00 USD | 862,740.00 USD | 1,030.00 USD | 452.37 USD | 1,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5710` | 907,500.00 USD | 907,500.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5715` | 289.08 USD | 995.18 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5720` | 905,140.00 USD | 905,140.00 USD | 0.00 USD | 832.92 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5720` | 860,070.00 USD | 860,070.00 USD | 0.00 USD | 4,370.00 USD | 12,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5730` | 904,310.00 USD | 904,310.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5740` | 889,440.00 USD | 889,440.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5740` | 843,550.00 USD | 843,550.00 USD | 21,620.00 USD | 1,100.00 USD | 1,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `0.5745` | 706.11 USD | 706.11 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `0.5750` | 884,670.00 USD | 884,670.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5760` | 859,350.00 USD | 859,350.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5760` | 819,220.00 USD | 819,220.00 USD | 2,150.00 USD | 7,300.00 USD | 173.64 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5770` | 840,010.00 USD | 840,010.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5780` | 819,030.00 USD | 819,030.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5780` | 809,590.00 USD | 809,590.00 USD | 40,930.00 USD | 0.00 USD | 1,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5790` | 803,730.00 USD | 803,730.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5800` | 781,880.00 USD | 781,880.00 USD | 3,310.00 USD | 2,750.00 USD | 1,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5800` | 767,150.00 USD | 767,150.00 USD | 1,610.00 USD | 3,900.00 USD | 27,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5810` | 774,240.00 USD | 774,240.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5820` | 754,400.00 USD | 754,400.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5820` | 733,690.00 USD | 733,690.00 USD | 0.00 USD | 0.00 USD | 6,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5830` | 743,130.00 USD | 743,130.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5840` | 737,390.00 USD | 737,390.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5840` | 726,950.00 USD | 726,950.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5850` | 730,930.00 USD | 730,930.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5860` | 697,120.00 USD | 697,120.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5860` | 705,790.00 USD | 705,790.00 USD | 0.00 USD | 0.00 USD | 195.16 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5870` | 683,330.00 USD | 683,330.00 USD | 15,080.00 USD | 2,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5880` | 665,940.00 USD | 665,940.00 USD | 34,650.00 USD | 10,250.00 USD | 7,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5880` | 705,600.00 USD | 705,600.00 USD | 3,110.00 USD | 16,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5890` | 613,240.00 USD | 613,240.00 USD | 38,270.00 USD | 11,450.00 USD | 7.65 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5900` | 563,510.00 USD | 563,510.00 USD | 29,060.00 USD | 13,050.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5900` | 686,480.00 USD | 686,480.00 USD | 104,240.00 USD | 1,560.00 USD | 226.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5910` | 511,260.00 USD | 511,260.00 USD | 26,100.00 USD | 13,220.00 USD | 18,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5920` | 453,920.00 USD | 453,920.00 USD | 25,960.00 USD | 6,190.00 USD | 7,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5920` | 580,450.00 USD | 580,450.00 USD | 11,690.00 USD | 19,960.00 USD | 75,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5930` | 414,660.00 USD | 414,660.00 USD | 6,060.00 USD | 6,380.00 USD | 12,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5940` | 389,270.00 USD | 389,270.00 USD | 11,050.00 USD | 0.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5940` | 473,470.00 USD | 473,470.00 USD | 19,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5950` | 369,820.00 USD | 369,820.00 USD | 24,900.00 USD | 1,640.00 USD | 59.54 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5960` | 343,230.00 USD | 343,230.00 USD | 7,830.00 USD | 1,040.00 USD | 8,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5960` | 453,560.00 USD | 453,560.00 USD | 18,180.00 USD | 18,410.00 USD | 46.83 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5970` | 325,780.00 USD | 325,780.00 USD | 13,620.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5980` | 310,170.00 USD | 310,170.00 USD | 10,460.00 USD | 1,540.00 USD | 62.20 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.5980` | 416,920.00 USD | 416,920.00 USD | 20,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.5990` | 298,100.00 USD | 298,100.00 USD | 0.00 USD | 0.00 USD | 19.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6000` | 298,080.00 USD | 298,080.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6000` | 396,540.00 USD | 396,540.00 USD | 3,320.00 USD | 0.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6010` | 293,080.00 USD | 293,080.00 USD | 0.00 USD | 6,370.00 USD | 2,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6020` | 284,490.00 USD | 284,490.00 USD | 2,680.00 USD | 3,280.00 USD | 2.58 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6020` | 388,320.00 USD | 388,320.00 USD | 0.00 USD | 8,040.00 USD | 102.85 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6030` | 278,520.00 USD | 278,520.00 USD | 34,080.00 USD | 14,050.00 USD | 3,630.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6040` | 226,750.00 USD | 226,750.00 USD | 6,530.00 USD | 9,900.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6040` | 380,170.00 USD | 380,170.00 USD | 38,530.00 USD | 18,680.00 USD | 89.59 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6050` | 205,320.00 USD | 205,320.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6060` | 175,320.00 USD | 175,320.00 USD | 8,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6060` | 322,870.00 USD | 322,870.00 USD | 19,640.00 USD | 0.00 USD | 20,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6080` | 282,330.00 USD | 282,330.00 USD | 2,860.00 USD | 0.00 USD | 30,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6100` | 166,910.00 USD | 166,910.00 USD | 0.00 USD | 0.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6100` | 249,050.00 USD | 249,050.00 USD | 21,400.00 USD | 47,430.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6110` | 131,740.00 USD | 131,740.00 USD | 8,660.00 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6120` | 121,400.00 USD | 121,400.00 USD | 30,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6120` | 155,100.00 USD | 155,100.00 USD | 35,760.00 USD | 20,330.00 USD | 18,510.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6130` | 91,370.00 USD | 91,370.00 USD | 33,470.00 USD | 0.00 USD | 22,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6140` | 35,120.00 USD | 35,120.00 USD | 6,130.00 USD | 0.00 USD | 15,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6140` | 80,500.00 USD | 80,500.00 USD | 51,900.00 USD | 8,040.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6160` | 13,240.00 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `0.6160` | 16,520.00 USD | 16,520.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `0.6180` | 10,120.00 USD | 10,120.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6190` | 11,470.00 USD | 11,470.00 USD | 9,830.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6190` | 22,930.00 USD | 22,930.00 USD | 9,830.00 USD | 1,640.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6200` | 33,410.00 USD | 33,410.00 USD | 0.00 USD | 1,880.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 42,870.00 USD | 42,870.00 USD | 13,870.00 USD | 0.00 USD | 29,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6200` | 85,740.00 USD | 85,740.00 USD | 13,870.00 USD | 0.00 USD | 29,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6210` | 56,180.00 USD | 56,180.00 USD | 5,900.00 USD | 0.00 USD | 16,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6220` | 68,130.00 USD | 68,130.00 USD | 5,630.00 USD | 2,380.00 USD | 3,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6220` | 113,460.00 USD | 113,460.00 USD | 4,760.00 USD | 22,640.00 USD | 312.38 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6230` | 80,350.00 USD | 80,350.00 USD | 11,380.00 USD | 840.09 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6240` | 111,380.00 USD | 111,380.00 USD | 21,710.00 USD | 2,220.00 USD | 7,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6240` | 121,280.00 USD | 121,280.00 USD | 0.00 USD | 7,300.00 USD | 514.08 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6250` | 142,770.00 USD | 142,770.00 USD | 16,730.00 USD | 12,460.00 USD | 2,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6260` | 161,060.00 USD | 161,060.00 USD | 5,750.00 USD | 8,370.00 USD | 4,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6260` | 230,060.00 USD | 230,060.00 USD | 108,240.00 USD | 0.00 USD | 536.81 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6270` | 240,940.00 USD | 240,940.00 USD | 47,830.00 USD | 20,700.00 USD | 11,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6280` | 290,020.00 USD | 290,020.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6280` | 316,490.00 USD | 316,490.00 USD | 38,530.00 USD | 22,580.00 USD | 25,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6290` | 331,710.00 USD | 331,710.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6300` | 355,360.00 USD | 355,360.00 USD | 10,980.00 USD | 3,430.00 USD | 9,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6300` | 384,940.00 USD | 384,940.00 USD | 19,640.00 USD | 0.00 USD | 48,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6310` | 396,310.00 USD | 396,310.00 USD | 14,450.00 USD | 4,790.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6320` | 440,690.00 USD | 440,690.00 USD | 30,470.00 USD | 2,910.00 USD | 11,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6330` | 482,840.00 USD | 482,840.00 USD | 14,500.00 USD | 9,340.00 USD | 18,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6340` | 550,060.00 USD | 550,060.00 USD | 29,640.00 USD | 3,190.00 USD | 34,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6340` | 453,880.00 USD | 453,880.00 USD | 68,660.00 USD | 0.00 USD | 283.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6350` | 591,980.00 USD | 591,980.00 USD | 35,710.00 USD | 0.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6360` | 709,780.00 USD | 709,780.00 USD | 56,590.00 USD | 2,470.00 USD | 58,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6360` | 545,620.00 USD | 545,620.00 USD | 34,320.00 USD | 0.00 USD | 57,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6370` | 745,940.00 USD | 745,940.00 USD | 0.00 USD | 5,770.00 USD | 30,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6380` | 775,520.00 USD | 775,520.00 USD | 0.00 USD | 23,260.00 USD | 6,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6380` | 585,210.00 USD | 585,210.00 USD | 0.00 USD | 0.00 USD | 39,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6390` | 849,850.00 USD | 849,850.00 USD | 20,130.00 USD | 7,210.00 USD | 47,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6400` | 990,800.00 USD | 990,800.00 USD | 72,890.00 USD | 35,480.00 USD | 32,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6400` | 625,710.00 USD | 625,710.00 USD | 19,270.00 USD | 7,510.00 USD | 13,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6410` | 1,060,000.00 USD | 1,060,000.00 USD | 35,660.00 USD | 16,130.00 USD | 14,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6420` | 1,170,000.00 USD | 1,170,000.00 USD | 77,930.00 USD | 15,540.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6420` | 761,980.00 USD | 761,980.00 USD | 55,350.00 USD | 44,770.00 USD | 36,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6430` | 1,260,000.00 USD | 1,260,000.00 USD | 38,040.00 USD | 14,630.00 USD | 30,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6440` | 1,350,000.00 USD | 1,350,000.00 USD | 26,980.00 USD | 17,270.00 USD | 49,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6440` | 859,120.00 USD | 859,120.00 USD | 54,510.00 USD | 24,820.00 USD | 17,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6450` | 1,460,000.00 USD | 1,460,000.00 USD | 60,850.00 USD | 11,120.00 USD | 35,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6460` | 1,530,000.00 USD | 1,530,000.00 USD | 45,900.00 USD | 11,290.00 USD | 9,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6460` | 1,220,000.00 USD | 1,220,000.00 USD | 172,610.00 USD | 46,630.00 USD | 138,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6470` | 1,610,000.00 USD | 1,610,000.00 USD | 63,150.00 USD | 17,210.00 USD | 8,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6475` | 209.47 USD | 10,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6480` | 1,690,000.00 USD | 1,690,000.00 USD | 70,490.00 USD | 6,780.00 USD | 373.19 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6480` | 1,360,000.00 USD | 1,360,000.00 USD | 86,440.00 USD | 26,520.00 USD | 33,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6490` | 1,770,000.00 USD | 1,770,000.00 USD | 63,670.00 USD | 1,230.00 USD | 11,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.6495` | 157.93 USD | 10,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `0.6500` | 1,820,000.00 USD | 1,820,000.00 USD | 46,720.00 USD | 5,920.00 USD | 128.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6500` | 1,570,000.00 USD | 1,570,000.00 USD | 73,560.00 USD | 0.00 USD | 132,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6510` | 1,890,000.00 USD | 1,890,000.00 USD | 55,500.00 USD | 0.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6520` | 1,990,000.00 USD | 1,990,000.00 USD | 93,550.00 USD | 9,040.00 USD | 4,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6520` | 1,980,000.00 USD | 1,980,000.00 USD | 298,050.00 USD | 10,910.00 USD | 105,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6530` | 2,010,000.00 USD | 2,010,000.00 USD | 11,510.00 USD | 3,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6540` | 2,040,000.00 USD | 2,040,000.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6540` | 2,070,000.00 USD | 2,070,000.00 USD | 15,730.00 USD | 4,440.00 USD | 61,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6550` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6560` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6560` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,380.00 USD | 817.52 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6570` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6580` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6580` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 28,280.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6590` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6600` | 2,090,000.00 USD | 2,090,000.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6600` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 18,420.00 USD | 814.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6610` | 2,100,000.00 USD | 2,100,000.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6620` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6620` | 2,140,000.00 USD | 2,140,000.00 USD | 8,600.00 USD | 0.00 USD | 588.76 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6630` | 2,110,000.00 USD | 2,110,000.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6640` | 2,120,000.00 USD | 2,120,000.00 USD | 11,190.00 USD | 837.01 USD | 126.28 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6640` | 2,180,000.00 USD | 2,180,000.00 USD | 33,660.00 USD | 0.00 USD | 7,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6650` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6660` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6660` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 6,770.00 USD | 396.96 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6670` | 2,170,000.00 USD | 2,170,000.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6680` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 130.23 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6690` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6700` | 2,210,000.00 USD | 2,210,000.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6700` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 243.37 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6710` | 2,260,000.00 USD | 2,260,000.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6720` | 2,260,000.00 USD | 2,260,000.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6720` | 2,280,000.00 USD | 2,280,000.00 USD | 58,470.00 USD | 0.00 USD | 30,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6730` | 2,300,000.00 USD | 2,300,000.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6740` | 2,380,000.00 USD | 2,380,000.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6740` | 2,320,000.00 USD | 2,320,000.00 USD | 39,730.00 USD | 0.00 USD | 364.93 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6750` | 2,430,000.00 USD | 2,430,000.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6760` | 2,440,000.00 USD | 2,440,000.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6760` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 77,970.00 USD | 33,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6770` | 2,490,000.00 USD | 2,490,000.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6780` | 2,550,000.00 USD | 2,550,000.00 USD | 33,610.00 USD | 13,860.00 USD | 12,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6780` | 2,530,000.00 USD | 2,530,000.00 USD | 63,600.00 USD | 16,810.00 USD | 17,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6790` | 2,580,000.00 USD | 2,580,000.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6800` | 2,590,000.00 USD | 2,590,000.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6800` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 16,590.00 USD | 4,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6810` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 1,940.00 USD | 11,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6820` | 2,650,000.00 USD | 2,650,000.00 USD | 22,600.00 USD | 16,590.00 USD | 9,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6820` | 2,630,000.00 USD | 2,630,000.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6830` | 2,740,000.00 USD | 2,740,000.00 USD | 24,570.00 USD | 20,000.00 USD | 49,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `0.6840` | 2,790,000.00 USD | 2,790,000.00 USD | 45,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6840` | 2,850,000.00 USD | 2,850,000.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6860` | 2,920,000.00 USD | 2,920,000.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6880` | 2,980,000.00 USD | 2,980,000.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6900` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6920` | 3,140,000.00 USD | 3,140,000.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6940` | 3,200,000.00 USD | 3,200,000.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6960` | 3,270,000.00 USD | 3,270,000.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.6980` | 3,320,000.00 USD | 3,320,000.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7000` | 3,390,000.00 USD | 3,390,000.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7020` | 3,480,000.00 USD | 3,480,000.00 USD | 29,810.00 USD | 0.00 USD | 53,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7040` | 3,670,000.00 USD | 3,670,000.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7060` | 3,930,000.00 USD | 3,930,000.00 USD | 47,840.00 USD | 33,490.00 USD | 177,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7080` | 4,100,000.00 USD | 4,100,000.00 USD | 24,440.00 USD | 64,870.00 USD | 82,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7100` | 4,460,000.00 USD | 4,460,000.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7120` | 4,870,000.00 USD | 4,870,000.00 USD | 101,040.00 USD | 78,760.00 USD | 227,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7140` | 5,280,000.00 USD | 5,280,000.00 USD | 202,560.00 USD | 67,260.00 USD | 133,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7160` | 5,620,000.00 USD | 5,620,000.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7180` | 5,910,000.00 USD | 5,910,000.00 USD | 165,860.00 USD | 56,910.00 USD | 66,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7200` | 6,230,000.00 USD | 6,230,000.00 USD | 93,750.00 USD | 45,160.00 USD | 178,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7220` | 6,710,000.00 USD | 6,710,000.00 USD | 318,420.00 USD | 67,130.00 USD | 98,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7240` | 7,010,000.00 USD | 7,010,000.00 USD | 146,110.00 USD | 24,910.00 USD | 129,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7245` | 364.39 USD | 11,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7260` | 7,340,000.00 USD | 7,340,000.00 USD | 106,410.00 USD | 52,120.00 USD | 176,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7280` | 7,570,000.00 USD | 7,570,000.00 USD | 99,750.00 USD | 40,180.00 USD | 84,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7295` | 43,330.00 USD | 54,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `0.7300` | 7,850,000.00 USD | 7,850,000.00 USD | 115,310.00 USD | 60,310.00 USD | 109,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7320` | 8,190,000.00 USD | 8,190,000.00 USD | 189,840.00 USD | 65,640.00 USD | 80,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7340` | 8,290,000.00 USD | 8,290,000.00 USD | 31,260.00 USD | 8,620.00 USD | 62,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7360` | 8,480,000.00 USD | 8,480,000.00 USD | 103,600.00 USD | 46,790.00 USD | 35,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7380` | 8,630,000.00 USD | 8,630,000.00 USD | 73,710.00 USD | 19,000.00 USD | 60,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7400` | 8,650,000.00 USD | 8,650,000.00 USD | 1,730.00 USD | 4,760.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7420` | 8,750,000.00 USD | 8,750,000.00 USD | 35,810.00 USD | 35,860.00 USD | 31,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7440` | 8,930,000.00 USD | 8,930,000.00 USD | 74,450.00 USD | 33,900.00 USD | 70,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7460` | 9,090,000.00 USD | 9,090,000.00 USD | 88,800.00 USD | 17,230.00 USD | 51,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7480` | 9,220,000.00 USD | 9,220,000.00 USD | 60,580.00 USD | 28,900.00 USD | 38,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7500` | 9,310,000.00 USD | 9,310,000.00 USD | 52,320.00 USD | 12,610.00 USD | 25,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7520` | 9,420,000.00 USD | 9,420,000.00 USD | 53,470.00 USD | 13,000.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `0.7530` | 9,460,000.00 USD | 9,460,000.00 USD | 21,290.00 USD | 1,890.00 USD | 14,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `0.7725` | 165.62 USD | 54,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8005` | 19,120.00 USD | 73,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.8665` | 378.95 USD | 74,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9065` | 24,440.00 USD | 98,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9935` | 166.01 USD | 98,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `0.9995` | 17,640.00 USD | 116,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.02` | 25,970.00 USD | 142,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.04` | 5,210.00 USD | 147,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 83,050.00 USD | 230,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.09` | 479.74 USD | 231,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.12` | 2,800.00 USD | 233,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.17` | 501.44 USD | 234,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 227.46 USD | 234,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.19` | 199.98 USD | 234,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.20` | 100.76 USD | 234,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1.22` | 796.83 USD | 235,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `0.1395` | 207,740.00 USD | 0.00 USD | 419.65 USD | `-77.26%` | `3,008.22` |
| `Live` | `Long` | `0.1465` | 207,320.00 USD | 0.00 USD | 1,070.00 USD | `-76.12%` | `7,272.07` |
| `Live` | `Long` | `0.1605` | 206,260.00 USD | 0.00 USD | 222.83 USD | `-73.83%` | `1,388.32` |
| `Live` | `Long` | `0.1875` | 206,040.00 USD | 0.00 USD | 269.27 USD | `-69.43%` | `1,436.09` |
| `Live` | `Long` | `0.2185` | 205,770.00 USD | 0.00 USD | 226.83 USD | `-64.38%` | `1,038.12` |
| `Live` | `Long` | `0.2355` | 205,540.00 USD | 0.00 USD | 2,660.00 USD | `-61.61%` | `11,284.25` |
| `Live` | `Long` | `0.2415` | 202,880.00 USD | 0.00 USD | 243.01 USD | `-60.63%` | `1,006.27` |
| `Live` | `Long` | `0.2425` | 202,640.00 USD | 0.00 USD | 1,460.00 USD | `-60.47%` | `6,000.00` |
| `Live` | `Long` | `0.3105` | 201,180.00 USD | 0.00 USD | 105.38 USD | `-49.38%` | `339.38` |
| `Live` | `Long` | `0.3175` | 201,080.00 USD | 0.00 USD | 1,590.00 USD | `-48.24%` | `5,000.00` |
| `Live` | `Long` | `0.3305` | 199,490.00 USD | 0.00 USD | 9,950.00 USD | `-46.12%` | `30,091.58` |
| `Live` | `Long` | `0.3395` | 189,550.00 USD | 0.00 USD | 679.34 USD | `-44.65%` | `2,001.00` |
| `Live` | `Long` | `0.3545` | 188,870.00 USD | 0.00 USD | 177.25 USD | `-42.21%` | `500.00` |
| `Live` | `Long` | `0.3585` | 188,690.00 USD | 0.00 USD | 12,850.00 USD | `-41.56%` | `35,856.81` |
| `Live` | `Long` | `0.3675` | 175,830.00 USD | 0.00 USD | 189.99 USD | `-40.09%` | `516.98` |
| `Live` | `Long` | `0.3785` | 175,640.00 USD | 0.00 USD | 567.75 USD | `-38.29%` | `1,500.00` |
| `Live` | `Long` | `0.3905` | 175,080.00 USD | 0.00 USD | 359.26 USD | `-36.34%` | `919.99` |
| `Live` | `Long` | `0.3955` | 174,720.00 USD | 0.00 USD | 2,640.00 USD | `-35.52%` | `6,686.27` |
| `Live` | `Long` | `0.3995` | 172,070.00 USD | 0.00 USD | 271.06 USD | `-34.87%` | `678.49` |
| `Live` | `Long` | `0.4035` | 171,800.00 USD | 0.00 USD | 282.45 USD | `-34.22%` | `700.00` |
| `Live` | `Long` | `0.4125` | 171,520.00 USD | 0.00 USD | 1,070.00 USD | `-32.75%` | `2,600.00` |
| `Live` | `Long` | `0.4135` | 170,450.00 USD | 0.00 USD | 1,600.00 USD | `-32.59%` | `3,868.97` |
| `Live` | `Long` | `0.4185` | 168,850.00 USD | 0.00 USD | 630.86 USD | `-31.77%` | `1,507.44` |
| `Live` | `Long` | `0.4255` | 168,220.00 USD | 0.00 USD | 224.96 USD | `-30.63%` | `528.69` |
| `Live` | `Long` | `0.4395` | 167,990.00 USD | 0.00 USD | 444.97 USD | `-28.35%` | `1,012.44` |
| `Live` | `Long` | `0.4435` | 167,550.00 USD | 0.00 USD | 5,510.00 USD | `-27.70%` | `12,426.15` |
| `Live` | `Long` | `0.4475` | 162,040.00 USD | 0.00 USD | 226.63 USD | `-27.05%` | `506.43` |
| `Live` | `Long` | `0.4515` | 161,810.00 USD | 0.00 USD | 27,090.00 USD | `-26.39%` | `60,000.00` |
| `Live` | `Long` | `0.4535` | 134,720.00 USD | 0.00 USD | 5,970.00 USD | `-26.07%` | `13,168.58` |
| `Live` | `Long` | `0.4605` | 128,750.00 USD | 0.00 USD | 430.79 USD | `-24.93%` | `935.49` |
| `Live` | `Long` | `0.4615` | 128,320.00 USD | 0.00 USD | 595.82 USD | `-24.76%` | `1,291.05` |
| `Live` | `Long` | `0.4625` | 127,720.00 USD | 0.00 USD | 1,460.00 USD | `-24.60%` | `3,156.35` |
| `Live` | `Long` | `0.4645` | 126,260.00 USD | 0.00 USD | 876.05 USD | `-24.27%` | `1,886.00` |
| `Live` | `Long` | `0.4685` | 125,380.00 USD | 0.00 USD | 1,350.00 USD | `-23.62%` | `2,881.36` |
| `Live` | `Long` | `0.4765` | 124,030.00 USD | 0.00 USD | 4,400.00 USD | `-22.32%` | `9,243.24` |
| `Live` | `Long` | `0.4835` | 119,630.00 USD | 0.00 USD | 135.33 USD | `-21.18%` | `279.90` |
| `Live` | `Long` | `0.4855` | 119,500.00 USD | 0.00 USD | 181.88 USD | `-20.85%` | `374.62` |
| `Live` | `Long` | `0.4865` | 119,310.00 USD | 0.00 USD | 3,330.00 USD | `-20.69%` | `6,847.47` |
| `Live` | `Long` | `0.4925` | 115,980.00 USD | 0.00 USD | 10,520.00 USD | `-19.71%` | `21,364.96` |
| `Live` | `Long` | `0.4935` | 105,460.00 USD | 0.00 USD | 1,580.00 USD | `-19.55%` | `3,199.85` |
| `Live` | `Long` | `0.4945` | 103,880.00 USD | 0.00 USD | 7,030.00 USD | `-19.38%` | `14,223.31` |
| `Live` | `Long` | `0.4955` | 96,850.00 USD | 0.00 USD | 3,180.00 USD | `-19.22%` | `6,422.59` |
| `Live` | `Long` | `0.4965` | 93,660.00 USD | 0.00 USD | 143.19 USD | `-19.06%` | `288.40` |
| `Live` | `Long` | `0.4975` | 93,520.00 USD | 0.00 USD | 667.49 USD | `-18.89%` | `1,341.68` |
| `Live` | `Long` | `0.4985` | 92,850.00 USD | 0.00 USD | 429.90 USD | `-18.73%` | `862.38` |
| `Live` | `Long` | `0.5075` | 92,420.00 USD | 0.00 USD | 303.42 USD | `-17.26%` | `597.87` |
| `Live` | `Long` | `0.5085` | 92,120.00 USD | 0.00 USD | 102.82 USD | `-17.10%` | `202.20` |
| `Live` | `Long` | `0.5105` | 92,020.00 USD | 0.00 USD | 519.77 USD | `-16.78%` | `1,018.15` |
| `Live` | `Long` | `0.5125` | 91,500.00 USD | 0.00 USD | 248.05 USD | `-16.45%` | `484.00` |
| `Live` | `Long` | `0.5135` | 91,250.00 USD | 0.00 USD | 298.60 USD | `-16.29%` | `581.49` |
| `Live` | `Long` | `0.5175` | 90,950.00 USD | 0.00 USD | 9,440.00 USD | `-15.63%` | `18,249.92` |
| `Live` | `Long` | `0.5185` | 81,510.00 USD | 0.00 USD | 281.56 USD | `-15.47%` | `543.02` |
| `Live` | `Long` | `0.5245` | 81,230.00 USD | 0.00 USD | 209.80 USD | `-14.49%` | `400.00` |
| `Live` | `Long` | `0.5295` | 81,020.00 USD | 0.00 USD | 1,840.00 USD | `-13.68%` | `3,467.51` |
| `Live` | `Long` | `0.5315` | 79,180.00 USD | 0.00 USD | 11,510.00 USD | `-13.35%` | `21,664.95` |
| `Live` | `Long` | `0.5325` | 67,660.00 USD | 0.00 USD | 2,260.00 USD | `-13.19%` | `4,240.81` |
| `Live` | `Long` | `0.5335` | 65,410.00 USD | 0.00 USD | 163.22 USD | `-13.03%` | `305.95` |
| `Live` | `Long` | `0.5445` | 65,240.00 USD | 0.00 USD | 855.28 USD | `-11.23%` | `1,570.77` |
| `Live` | `Long` | `0.5475` | 64,390.00 USD | 0.00 USD | 1,630.00 USD | `-10.74%` | `2,968.46` |
| `Live` | `Long` | `0.5545` | 62,760.00 USD | 0.00 USD | 47,450.00 USD | `-9.60%` | `85,578.81` |
| `Live` | `Long` | `0.5585` | 15,310.00 USD | 0.00 USD | 10,520.00 USD | `-8.95%` | `18,834.52` |
| `Live` | `Long` | `0.5615` | 4,790.00 USD | 0.00 USD | 258.48 USD | `-8.46%` | `460.33` |
| `Live` | `Long` | `0.5635` | 4,530.00 USD | 0.00 USD | 244.90 USD | `-8.13%` | `434.61` |
| `Live` | `Long` | `0.5655` | 4,290.00 USD | 0.00 USD | 1,920.00 USD | `-7.81%` | `3,394.98` |
| `Live` | `Long` | `0.5665` | 2,370.00 USD | 0.00 USD | 1,370.00 USD | `-7.65%` | `2,421.90` |
| `Live` | `Long` | `0.5715` | 995.18 USD | 0.00 USD | 289.08 USD | `-6.83%` | `505.82` |
| `Live` | `Long` | `0.5745` | 706.11 USD | 0.00 USD | 706.11 USD | `-6.34%` | `1,229.08` |
| `Live` | `Short` | `0.6285` | 10,370.00 USD | 10,370.00 USD | 0.00 USD | `+2.46%` | `16,500.00` |
| `Live` | `Short` | `0.6475` | 10,580.00 USD | 209.47 USD | 0.00 USD | `+5.56%` | `323.51` |
| `Live` | `Short` | `0.6495` | 10,740.00 USD | 157.93 USD | 0.00 USD | `+5.89%` | `243.15` |
| `Live` | `Short` | `0.7245` | 11,100.00 USD | 364.39 USD | 0.00 USD | `+18.11%` | `502.96` |
| `Live` | `Short` | `0.7295` | 54,440.00 USD | 43,330.00 USD | 0.00 USD | `+18.93%` | `59,401.36` |
| `Live` | `Short` | `0.7725` | 54,600.00 USD | 165.62 USD | 0.00 USD | `+25.94%` | `214.40` |
| `Live` | `Short` | `0.8005` | 73,720.00 USD | 19,120.00 USD | 0.00 USD | `+30.50%` | `23,882.80` |
| `Live` | `Short` | `0.8665` | 74,100.00 USD | 378.95 USD | 0.00 USD | `+41.26%` | `437.33` |
| `Live` | `Short` | `0.9065` | 98,530.00 USD | 24,440.00 USD | 0.00 USD | `+47.78%` | `26,955.72` |
| `Live` | `Short` | `0.9935` | 98,700.00 USD | 166.01 USD | 0.00 USD | `+61.97%` | `167.10` |
| `Live` | `Short` | `0.9995` | 116,340.00 USD | 17,640.00 USD | 0.00 USD | `+62.94%` | `17,648.14` |
| `Live` | `Short` | `1.02` | 142,310.00 USD | 25,970.00 USD | 0.00 USD | `+66.53%` | `25,423.72` |
| `Live` | `Short` | `1.04` | 147,520.00 USD | 5,210.00 USD | 0.00 USD | `+69.95%` | `5,000.00` |
| `Live` | `Short` | `1.09` | 230,570.00 USD | 83,050.00 USD | 0.00 USD | `+77.45%` | `76,300.00` |
| `Live` | `Short` | `1.09` | 231,050.00 USD | 479.74 USD | 0.00 USD | `+77.94%` | `439.52` |
| `Live` | `Short` | `1.12` | 233,850.00 USD | 2,800.00 USD | 0.00 USD | `+82.51%` | `2,500.00` |
| `Live` | `Short` | `1.17` | 234,350.00 USD | 501.44 USD | 0.00 USD | `+91.31%` | `427.30` |
| `Live` | `Short` | `1.19` | 234,580.00 USD | 227.46 USD | 0.00 USD | `+93.43%` | `191.71` |
| `Live` | `Short` | `1.19` | 234,780.00 USD | 199.98 USD | 0.00 USD | `+93.76%` | `168.26` |
| `Live` | `Short` | `1.20` | 234,880.00 USD | 100.76 USD | 0.00 USD | `+95.71%` | `83.93` |
| `Live` | `Short` | `1.22` | 235,680.00 USD | 796.83 USD | 0.00 USD | `+99.14%` | `652.34` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `0.3505` | 166,390.00 USD | 0.00 USD | 340.19 USD | `-42.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4635` | 166,050.00 USD | 0.00 USD | 104.57 USD | `-24.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4955` | 165,950.00 USD | 0.00 USD | 111.62 USD | `-19.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.4965` | 165,830.00 USD | 0.00 USD | 111.85 USD | `-19.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5005` | 165,720.00 USD | 0.00 USD | 67,850.00 USD | `-18.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5015` | 97,880.00 USD | 0.00 USD | 112.97 USD | `-18.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5065` | 97,760.00 USD | 0.00 USD | 225.65 USD | `-17.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5085` | 97,540.00 USD | 0.00 USD | 101.97 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5115` | 97,440.00 USD | 0.00 USD | 111.69 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5125` | 97,320.00 USD | 0.00 USD | 5,380.00 USD | `-16.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5165` | 91,940.00 USD | 0.00 USD | 115.47 USD | `-15.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5175` | 91,830.00 USD | 0.00 USD | 116.58 USD | `-15.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5185` | 91,710.00 USD | 0.00 USD | 116.96 USD | `-15.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5205` | 91,590.00 USD | 0.00 USD | 539.96 USD | `-15.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5225` | 91,050.00 USD | 0.00 USD | 117.70 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5235` | 90,940.00 USD | 0.00 USD | 117.93 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5305` | 90,820.00 USD | 0.00 USD | 770.19 USD | `-13.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5445` | 90,050.00 USD | 0.00 USD | 8,750.00 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5455` | 81,290.00 USD | 0.00 USD | 8,150.00 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5485` | 73,140.00 USD | 0.00 USD | 4,500.00 USD | `-10.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5515` | 68,650.00 USD | 0.00 USD | 126.71 USD | `-10.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5525` | 68,520.00 USD | 0.00 USD | 126.90 USD | `-9.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5555` | 68,390.00 USD | 0.00 USD | 33,000.00 USD | `-9.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5565` | 35,400.00 USD | 0.00 USD | 173.58 USD | `-9.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5595` | 35,220.00 USD | 0.00 USD | 10,540.00 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5605` | 24,680.00 USD | 0.00 USD | 339.84 USD | `-8.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5625` | 24,340.00 USD | 0.00 USD | 930.52 USD | `-8.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5655` | 23,410.00 USD | 0.00 USD | 127.62 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5695` | 23,290.00 USD | 0.00 USD | 127.30 USD | `-7.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5705` | 23,160.00 USD | 0.00 USD | 9,410.00 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5715` | 13,750.00 USD | 0.00 USD | 127.63 USD | `-6.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5735` | 13,620.00 USD | 0.00 USD | 151.62 USD | `-6.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5755` | 13,470.00 USD | 0.00 USD | 999.82 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5775` | 12,470.00 USD | 0.00 USD | 1,710.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5785` | 10,750.00 USD | 0.00 USD | 127.36 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5795` | 10,620.00 USD | 0.00 USD | 780.04 USD | `-5.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5815` | 9,840.00 USD | 0.00 USD | 127.27 USD | `-5.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5835` | 9,720.00 USD | 0.00 USD | 999.65 USD | `-4.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5845` | 8,720.00 USD | 0.00 USD | 533.37 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5865` | 8,180.00 USD | 0.00 USD | 128.36 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5875` | 8,060.00 USD | 0.00 USD | 128.34 USD | `-4.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5895` | 7,930.00 USD | 0.00 USD | 128.45 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5905` | 7,800.00 USD | 0.00 USD | 127.30 USD | `-3.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5925` | 7,670.00 USD | 0.00 USD | 265.69 USD | `-3.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5975` | 7,410.00 USD | 0.00 USD | 597.80 USD | `-2.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.5995` | 6,810.00 USD | 0.00 USD | 509.04 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6005` | 6,300.00 USD | 0.00 USD | 953.02 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6045` | 5,350.00 USD | 0.00 USD | 999.99 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6055` | 4,350.00 USD | 0.00 USD | 1,510.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6065` | 2,840.00 USD | 0.00 USD | 1,910.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6085` | 931.14 USD | 0.00 USD | 301.32 USD | `-0.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `0.6115` | 629.83 USD | 0.00 USD | 629.83 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6135` | 410.30 USD | 410.30 USD | 0.00 USD | `+0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6175` | 929.43 USD | 519.13 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6185` | 1,110.00 USD | 177.58 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6205` | 2,230.00 USD | 1,120.00 USD | 0.00 USD | `+1.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6225` | 3,230.00 USD | 1,000.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6275` | 3,660.00 USD | 433.11 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6285` | 4,130.00 USD | 469.94 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6305` | 8,560.00 USD | 4,430.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6325` | 8,830.00 USD | 269.44 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6335` | 17,230.00 USD | 8,390.00 USD | 0.00 USD | `+3.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6345` | 17,500.00 USD | 276.40 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6395` | 18,700.00 USD | 1,200.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6405` | 18,850.00 USD | 145.91 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6445` | 18,970.00 USD | 121.42 USD | 0.00 USD | `+5.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6465` | 19,380.00 USD | 410.21 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6485` | 19,820.00 USD | 447.03 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6505` | 20,390.00 USD | 567.58 USD | 0.00 USD | `+6.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6525` | 20,560.00 USD | 172.51 USD | 0.00 USD | `+6.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6535` | 20,910.00 USD | 349.76 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6555` | 24,990.00 USD | 4,080.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6585` | 26,430.00 USD | 1,440.00 USD | 0.00 USD | `+7.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6595` | 27,180.00 USD | 746.46 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6605` | 27,760.00 USD | 580.23 USD | 0.00 USD | `+7.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6635` | 28,050.00 USD | 289.66 USD | 0.00 USD | `+8.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6645` | 28,310.00 USD | 262.60 USD | 0.00 USD | `+8.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6655` | 28,590.00 USD | 283.50 USD | 0.00 USD | `+8.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6675` | 28,890.00 USD | 290.78 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6685` | 29,060.00 USD | 170.95 USD | 0.00 USD | `+8.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6695` | 30,720.00 USD | 1,670.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6705` | 30,890.00 USD | 162.91 USD | 0.00 USD | `+9.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6715` | 31,090.00 USD | 202.63 USD | 0.00 USD | `+9.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6725` | 32,760.00 USD | 1,670.00 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6745` | 33,360.00 USD | 598.31 USD | 0.00 USD | `+9.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6755` | 33,720.00 USD | 361.53 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6765` | 33,880.00 USD | 154.30 USD | 0.00 USD | `+10.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6805` | 34,090.00 USD | 214.20 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6815` | 44,650.00 USD | 10,560.00 USD | 0.00 USD | `+11.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6825` | 44,760.00 USD | 112.49 USD | 0.00 USD | `+11.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6845` | 45,900.00 USD | 1,130.00 USD | 0.00 USD | `+11.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6875` | 46,040.00 USD | 140.41 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6885` | 46,550.00 USD | 514.80 USD | 0.00 USD | `+12.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6915` | 46,650.00 USD | 101.96 USD | 0.00 USD | `+12.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6925` | 47,680.00 USD | 1,020.00 USD | 0.00 USD | `+12.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6945` | 48,290.00 USD | 610.10 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6955` | 48,390.00 USD | 101.38 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6965` | 49,180.00 USD | 789.18 USD | 0.00 USD | `+13.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.6985` | 49,280.00 USD | 102.99 USD | 0.00 USD | `+13.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7005` | 49,390.00 USD | 111.08 USD | 0.00 USD | `+14.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7015` | 50,090.00 USD | 694.49 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7095` | 50,220.00 USD | 132.99 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7115` | 50,340.00 USD | 122.04 USD | 0.00 USD | `+15.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7165` | 52,180.00 USD | 1,830.00 USD | 0.00 USD | `+16.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7195` | 52,360.00 USD | 183.26 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7205` | 52,510.00 USD | 147.15 USD | 0.00 USD | `+17.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7265` | 58,800.00 USD | 6,290.00 USD | 0.00 USD | `+18.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7275` | 59,110.00 USD | 309.91 USD | 0.00 USD | `+18.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7325` | 59,270.00 USD | 165.17 USD | 0.00 USD | `+19.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7345` | 60,300.00 USD | 1,030.00 USD | 0.00 USD | `+19.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7405` | 61,030.00 USD | 733.09 USD | 0.00 USD | `+20.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7415` | 61,190.00 USD | 156.98 USD | 0.00 USD | `+20.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7445` | 61,370.00 USD | 185.43 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7455` | 63,540.00 USD | 2,170.00 USD | 0.00 USD | `+21.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7475` | 63,860.00 USD | 318.43 USD | 0.00 USD | `+21.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7505` | 64,000.00 USD | 141.39 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7565` | 68,120.00 USD | 4,120.00 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7575` | 68,630.00 USD | 511.82 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7615` | 69,500.00 USD | 875.23 USD | 0.00 USD | `+24.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7635` | 69,610.00 USD | 103.35 USD | 0.00 USD | `+24.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7665` | 69,730.00 USD | 127.48 USD | 0.00 USD | `+24.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7675` | 69,830.00 USD | 101.61 USD | 0.00 USD | `+25.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7695` | 70,020.00 USD | 186.97 USD | 0.00 USD | `+25.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7705` | 70,130.00 USD | 109.43 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7775` | 70,300.00 USD | 166.70 USD | 0.00 USD | `+26.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7815` | 71,430.00 USD | 1,140.00 USD | 0.00 USD | `+27.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.7865` | 77,750.00 USD | 6,310.00 USD | 0.00 USD | `+28.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8125` | 89,820.00 USD | 12,070.00 USD | 0.00 USD | `+32.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8265` | 91,470.00 USD | 1,650.00 USD | 0.00 USD | `+34.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8335` | 92,400.00 USD | 929.08 USD | 0.00 USD | `+35.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8475` | 132,990.00 USD | 40,590.00 USD | 0.00 USD | `+38.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8505` | 149,730.00 USD | 16,740.00 USD | 0.00 USD | `+38.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8515` | 162,450.00 USD | 12,720.00 USD | 0.00 USD | `+38.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8525` | 174,230.00 USD | 11,780.00 USD | 0.00 USD | `+38.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.8725` | 174,390.00 USD | 159.86 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9005` | 175,090.00 USD | 702.20 USD | 0.00 USD | `+46.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9085` | 175,290.00 USD | 193.62 USD | 0.00 USD | `+48.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9365` | 175,710.00 USD | 424.63 USD | 0.00 USD | `+52.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9405` | 178,510.00 USD | 2,790.00 USD | 0.00 USD | `+53.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9505` | 178,850.00 USD | 340.54 USD | 0.00 USD | `+54.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9655` | 178,950.00 USD | 108.83 USD | 0.00 USD | `+57.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9715` | 179,100.00 USD | 145.72 USD | 0.00 USD | `+58.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `0.9875` | 181,130.00 USD | 2,030.00 USD | 0.00 USD | `+60.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 181,270.00 USD | 136.10 USD | 0.00 USD | `+63.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.00` | 181,820.00 USD | 550.48 USD | 0.00 USD | `+63.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.03` | 182,130.00 USD | 314.99 USD | 0.00 USD | `+67.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.05` | 182,740.00 USD | 602.17 USD | 0.00 USD | `+71.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.06` | 183,100.00 USD | 360.61 USD | 0.00 USD | `+72.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.08` | 184,040.00 USD | 942.77 USD | 0.00 USD | `+76.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1.10` | 184,440.00 USD | 397.19 USD | 0.00 USD | `+79.41%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `0.5240` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 32.85 USD |
| `7D` | `0.5260` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 5,850.00 USD | 0.00 USD | 3,010.00 USD |
| `7D` | `0.5280` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 5,050.00 USD | 0.00 USD | 2,560.00 USD |
| `7D` | `0.5300` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 5,120.00 USD | 0.00 USD | 9,070.00 USD |
| `7D` | `0.5320` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 8,680.00 USD | 0.00 USD | 3,480.00 USD |
| `7D` | `0.5340` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 2,600.00 USD |
| `7D` | `0.5360` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 2,440.00 USD | 3,040.00 USD | 44.79 USD |
| `7D` | `0.5380` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 1,550.00 USD | 2,910.00 USD |
| `7D` | `0.5400` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 0.00 USD | 2,920.00 USD | 80.65 USD |
| `1D` | `0.5410` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 13,320.00 USD | 1,720.00 USD | 2,000.00 USD |
| `1D` | `0.5420` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 2,590.00 USD | 530.84 USD | 2,890.00 USD |
| `7D` | `0.5420` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 16,260.00 USD | 1,290.00 USD | 2,860.00 USD |
| `1D` | `0.5430` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 3,300.00 USD | 0.00 USD | 2,800.00 USD |
| `1D` | `0.5440` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 837.01 USD | 552.11 USD |
| `7D` | `0.5440` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 0.00 USD | 1,150.00 USD | 13,630.00 USD |
| `1D` | `0.5450` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 1,070.00 USD | 1,140.00 USD | 2,670.00 USD |
| `1D` | `0.5460` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 3,980.00 USD | 0.00 USD | 585.11 USD |
| `7D` | `0.5460` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 2,250.00 USD | 3,030.00 USD | 5,180.00 USD |
| `1D` | `0.5470` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 1,090.00 USD |
| `1D` | `0.5480` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 14.03 USD |
| `7D` | `0.5480` | 1,070,000.00 USD | 0.00 USD | 1,070,000.00 USD | 2,000.00 USD | 795.70 USD | 4,510.00 USD |
| `1D` | `0.5490` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 6,610.00 USD |
| `1D` | `0.5500` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 1,410.00 USD | 0.00 USD | 38.17 USD |
| `7D` | `0.5500` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 5,990.00 USD | 1,440.00 USD | 6,810.00 USD |
| `1D` | `0.5510` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 1,340.00 USD | 0.00 USD | 1,850.00 USD |
| `1D` | `0.5520` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 1,050.00 USD | 0.00 USD |
| `7D` | `0.5520` | 1,050,000.00 USD | 0.00 USD | 1,050,000.00 USD | 4,110.00 USD | 1,920.00 USD | 1,950.00 USD |
| `1D` | `0.5530` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 1,260.00 USD | 1,410.00 USD | 0.00 USD |
| `1D` | `0.5540` | 1,010,000.00 USD | 0.00 USD | 1,010,000.00 USD | 5,390.00 USD | 5,750.00 USD | 4,170.00 USD |
| `7D` | `0.5540` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 12,840.00 USD | 7,260.00 USD | 18,510.00 USD |
| `1D` | `0.5550` | 994,470.00 USD | 0.00 USD | 994,470.00 USD | 2,940.00 USD | 0.00 USD | 1,640.00 USD |
| `1D` | `0.5560` | 989,890.00 USD | 0.00 USD | 989,890.00 USD | 1,680.00 USD | 686.25 USD | 0.00 USD |
| `7D` | `0.5560` | 1,000,000.00 USD | 0.00 USD | 1,000,000.00 USD | 13,490.00 USD | 1,920.00 USD | 10,420.00 USD |
| `1D` | `0.5570` | 987,530.00 USD | 0.00 USD | 987,530.00 USD | 1,690.00 USD | 2,460.00 USD | 4,420.00 USD |
| `1D` | `0.5580` | 978,970.00 USD | 0.00 USD | 978,970.00 USD | 0.00 USD | 2,820.00 USD | 2,530.00 USD |
| `7D` | `0.5580` | 977,660.00 USD | 0.00 USD | 977,660.00 USD | 6,000.00 USD | 6,820.00 USD | 18,290.00 USD |
| `1D` | `0.5590` | 973,620.00 USD | 0.00 USD | 973,620.00 USD | 0.00 USD | 1,870.00 USD | 1,370.00 USD |
| `1D` | `0.5600` | 970,390.00 USD | 0.00 USD | 970,390.00 USD | 0.00 USD | 1,690.00 USD | 2,550.00 USD |
| `7D` | `0.5600` | 946,550.00 USD | 0.00 USD | 946,550.00 USD | 4,070.00 USD | 8,160.00 USD | 2,470.00 USD |
| `1D` | `0.5610` | 966,140.00 USD | 0.00 USD | 966,140.00 USD | 0.00 USD | 0.00 USD | 823.46 USD |
| `1D` | `0.5620` | 965,320.00 USD | 0.00 USD | 965,320.00 USD | 0.00 USD | 776.64 USD | 2,180.00 USD |
| `7D` | `0.5620` | 931,850.00 USD | 0.00 USD | 931,850.00 USD | 19,480.00 USD | 7,420.00 USD | 11,550.00 USD |
| `1D` | `0.5630` | 962,360.00 USD | 0.00 USD | 962,360.00 USD | 0.00 USD | 1,560.00 USD | 4,600.00 USD |
| `1D` | `0.5640` | 956,200.00 USD | 0.00 USD | 956,200.00 USD | 4,020.00 USD | 2,420.00 USD | 10,040.00 USD |
| `7D` | `0.5640` | 893,400.00 USD | 0.00 USD | 893,400.00 USD | 2,950.00 USD | 741.21 USD | 53.84 USD |
| `1D` | `0.5660` | 939,710.00 USD | 0.00 USD | 939,710.00 USD | 0.00 USD | 0.00 USD | 3,580.00 USD |
| `7D` | `0.5660` | 889,660.00 USD | 0.00 USD | 889,660.00 USD | 11,490.00 USD | 2,990.00 USD | 4,420.00 USD |
| `7D` | `0.5680` | 870,760.00 USD | 0.00 USD | 870,760.00 USD | 5,100.00 USD | 0.00 USD | 2,920.00 USD |
| `1D` | `0.5690` | 936,130.00 USD | 0.00 USD | 936,130.00 USD | 0.00 USD | 0.00 USD | 5,100.00 USD |
| `1D` | `0.5700` | 931,030.00 USD | 0.00 USD | 931,030.00 USD | 0.00 USD | 1,760.00 USD | 0.00 USD |
| `7D` | `0.5700` | 862,740.00 USD | 0.00 USD | 862,740.00 USD | 1,030.00 USD | 452.37 USD | 1,190.00 USD |
| `1D` | `0.5710` | 929,280.00 USD | 0.00 USD | 929,280.00 USD | 0.00 USD | 2,350.00 USD | 0.00 USD |
| `1D` | `0.5720` | 926,920.00 USD | 0.00 USD | 926,920.00 USD | 0.00 USD | 832.92 USD | 0.00 USD |
| `7D` | `0.5720` | 860,070.00 USD | 0.00 USD | 860,070.00 USD | 0.00 USD | 4,370.00 USD | 12,150.00 USD |
| `1D` | `0.5730` | 926,090.00 USD | 0.00 USD | 926,090.00 USD | 0.00 USD | 0.00 USD | 14,870.00 USD |
| `1D` | `0.5740` | 911,220.00 USD | 0.00 USD | 911,220.00 USD | 0.00 USD | 839.21 USD | 3,930.00 USD |
| `7D` | `0.5740` | 843,550.00 USD | 0.00 USD | 843,550.00 USD | 21,620.00 USD | 1,100.00 USD | 1,600.00 USD |
| `1D` | `0.5750` | 906,450.00 USD | 0.00 USD | 906,450.00 USD | 4,330.00 USD | 840.09 USD | 20,140.00 USD |
| `1D` | `0.5760` | 881,130.00 USD | 0.00 USD | 881,130.00 USD | 15,020.00 USD | 2,220.00 USD | 2,100.00 USD |
| `7D` | `0.5760` | 819,220.00 USD | 0.00 USD | 819,220.00 USD | 2,150.00 USD | 7,300.00 USD | 173.64 USD |
| `1D` | `0.5770` | 861,800.00 USD | 0.00 USD | 861,800.00 USD | 16,730.00 USD | 3,970.00 USD | 279.20 USD |
| `1D` | `0.5780` | 840,820.00 USD | 0.00 USD | 840,820.00 USD | 3,070.00 USD | 1,330.00 USD | 10,910.00 USD |
| `7D` | `0.5780` | 809,590.00 USD | 0.00 USD | 809,590.00 USD | 40,930.00 USD | 0.00 USD | 1,520.00 USD |
| `1D` | `0.5790` | 825,520.00 USD | 0.00 USD | 825,520.00 USD | 11,420.00 USD | 2,690.00 USD | 7,750.00 USD |
| `1D` | `0.5800` | 803,660.00 USD | 0.00 USD | 803,660.00 USD | 3,310.00 USD | 2,750.00 USD | 1,590.00 USD |
| `7D` | `0.5800` | 767,150.00 USD | 0.00 USD | 767,150.00 USD | 1,610.00 USD | 3,900.00 USD | 27,950.00 USD |
| `1D` | `0.5810` | 796,010.00 USD | 0.00 USD | 796,010.00 USD | 0.00 USD | 3,190.00 USD | 16,650.00 USD |
| `1D` | `0.5820` | 776,170.00 USD | 0.00 USD | 776,170.00 USD | 2,580.00 USD | 4,510.00 USD | 4,180.00 USD |
| `7D` | `0.5820` | 733,690.00 USD | 0.00 USD | 733,690.00 USD | 0.00 USD | 0.00 USD | 6,740.00 USD |
| `1D` | `0.5830` | 764,900.00 USD | 0.00 USD | 764,900.00 USD | 4,910.00 USD | 819.33 USD | 0.00 USD |
| `1D` | `0.5840` | 759,170.00 USD | 0.00 USD | 759,170.00 USD | 0.00 USD | 2,190.00 USD | 4,280.00 USD |
| `7D` | `0.5840` | 726,950.00 USD | 0.00 USD | 726,950.00 USD | 0.00 USD | 0.00 USD | 21,160.00 USD |
| `1D` | `0.5850` | 752,710.00 USD | 0.00 USD | 752,710.00 USD | 2,950.00 USD | 0.00 USD | 30,860.00 USD |
| `1D` | `0.5860` | 718,900.00 USD | 0.00 USD | 718,900.00 USD | 2,810.00 USD | 3,110.00 USD | 7,880.00 USD |
| `7D` | `0.5860` | 705,790.00 USD | 0.00 USD | 705,790.00 USD | 0.00 USD | 0.00 USD | 195.16 USD |
| `1D` | `0.5870` | 705,100.00 USD | 0.00 USD | 705,100.00 USD | 15,080.00 USD | 2,310.00 USD | 0.00 USD |
| `1D` | `0.5880` | 687,710.00 USD | 0.00 USD | 687,710.00 USD | 34,650.00 USD | 10,250.00 USD | 7,790.00 USD |
| `7D` | `0.5880` | 705,600.00 USD | 0.00 USD | 705,600.00 USD | 3,110.00 USD | 16,010.00 USD | 0.00 USD |
| `1D` | `0.5890` | 635,020.00 USD | 0.00 USD | 635,020.00 USD | 38,270.00 USD | 11,450.00 USD | 7.65 USD |
| `1D` | `0.5900` | 585,290.00 USD | 0.00 USD | 585,290.00 USD | 29,060.00 USD | 13,050.00 USD | 10,140.00 USD |
| `7D` | `0.5900` | 686,480.00 USD | 0.00 USD | 686,480.00 USD | 104,240.00 USD | 1,560.00 USD | 226.86 USD |
| `1D` | `0.5910` | 533,030.00 USD | 0.00 USD | 533,030.00 USD | 26,100.00 USD | 13,220.00 USD | 18,030.00 USD |
| `1D` | `0.5920` | 475,690.00 USD | 0.00 USD | 475,690.00 USD | 25,960.00 USD | 6,190.00 USD | 7,110.00 USD |
| `7D` | `0.5920` | 580,450.00 USD | 0.00 USD | 580,450.00 USD | 11,690.00 USD | 19,960.00 USD | 75,330.00 USD |
| `1D` | `0.5930` | 436,420.00 USD | 0.00 USD | 436,420.00 USD | 6,060.00 USD | 6,380.00 USD | 12,950.00 USD |
| `1D` | `0.5940` | 411,040.00 USD | 0.00 USD | 411,040.00 USD | 15,260.00 USD | 1,300.00 USD | 8,400.00 USD |
| `7D` | `0.5940` | 473,470.00 USD | 0.00 USD | 473,470.00 USD | 19,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5950` | 386,070.00 USD | 0.00 USD | 386,070.00 USD | 26,720.00 USD | 2,390.00 USD | 59.54 USD |
| `1D` | `0.5960` | 356,900.00 USD | 0.00 USD | 356,900.00 USD | 7,830.00 USD | 1,040.00 USD | 8,580.00 USD |
| `7D` | `0.5960` | 453,560.00 USD | 0.00 USD | 453,560.00 USD | 18,180.00 USD | 18,410.00 USD | 46.83 USD |
| `1D` | `0.5970` | 339,450.00 USD | 0.00 USD | 339,450.00 USD | 13,040.00 USD | 0.00 USD | 1,990.00 USD |
| `1D` | `0.5980` | 324,410.00 USD | 0.00 USD | 324,410.00 USD | 8,520.00 USD | 1,540.00 USD | 62.20 USD |
| `7D` | `0.5980` | 416,920.00 USD | 0.00 USD | 416,920.00 USD | 20,380.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.5990` | 314,290.00 USD | 0.00 USD | 314,290.00 USD | 0.00 USD | 0.00 USD | 13.12 USD |
| `1D` | `0.6000` | 314,280.00 USD | 0.00 USD | 314,280.00 USD | 0.00 USD | 0.00 USD | 5,010.00 USD |
| `7D` | `0.6000` | 396,540.00 USD | 0.00 USD | 396,540.00 USD | 3,320.00 USD | 0.00 USD | 4,900.00 USD |
| `1D` | `0.6010` | 309,270.00 USD | 0.00 USD | 309,270.00 USD | 0.00 USD | 6,370.00 USD | 2,220.00 USD |
| `1D` | `0.6020` | 300,680.00 USD | 0.00 USD | 300,680.00 USD | 2,680.00 USD | 3,280.00 USD | 2.58 USD |
| `7D` | `0.6020` | 388,320.00 USD | 0.00 USD | 388,320.00 USD | 0.00 USD | 8,040.00 USD | 102.85 USD |
| `1D` | `0.6030` | 294,710.00 USD | 0.00 USD | 294,710.00 USD | 34,080.00 USD | 14,050.00 USD | 3,630.00 USD |
| `1D` | `0.6040` | 242,940.00 USD | 0.00 USD | 242,940.00 USD | 6,530.00 USD | 9,900.00 USD | 5,010.00 USD |
| `7D` | `0.6040` | 380,170.00 USD | 0.00 USD | 380,170.00 USD | 38,530.00 USD | 18,680.00 USD | 89.59 USD |
| `1D` | `0.6050` | 221,510.00 USD | 0.00 USD | 221,510.00 USD | 20,690.00 USD | 1,370.00 USD | 7,950.00 USD |
| `1D` | `0.6060` | 191,510.00 USD | 0.00 USD | 191,510.00 USD | 8,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6060` | 322,870.00 USD | 0.00 USD | 322,870.00 USD | 19,640.00 USD | 0.00 USD | 20,900.00 USD |
| `1D` | `0.6070` | 183,100.00 USD | 0.00 USD | 183,100.00 USD | 8,430.00 USD | 2,600.00 USD | 0.00 USD |
| `1D` | `0.6080` | 172,080.00 USD | 0.00 USD | 172,080.00 USD | 3,650.00 USD | 1,510.00 USD | 0.00 USD |
| `7D` | `0.6080` | 282,330.00 USD | 0.00 USD | 282,330.00 USD | 2,860.00 USD | 0.00 USD | 30,420.00 USD |
| `1D` | `0.6100` | 166,910.00 USD | 0.00 USD | 166,910.00 USD | 0.00 USD | 0.00 USD | 35,170.00 USD |
| `7D` | `0.6100` | 249,050.00 USD | 0.00 USD | 249,050.00 USD | 21,400.00 USD | 47,430.00 USD | 25,120.00 USD |
| `1D` | `0.6110` | 131,740.00 USD | 0.00 USD | 131,740.00 USD | 8,660.00 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `0.6120` | 121,400.00 USD | 0.00 USD | 121,400.00 USD | 30,040.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6120` | 155,100.00 USD | 0.00 USD | 155,100.00 USD | 35,760.00 USD | 20,330.00 USD | 18,510.00 USD |
| `1D` | `0.6130` | 91,370.00 USD | 0.00 USD | 91,370.00 USD | 33,470.00 USD | 0.00 USD | 22,770.00 USD |
| `1D` | `0.6140` | 35,120.00 USD | 0.00 USD | 35,120.00 USD | 6,130.00 USD | 0.00 USD | 15,740.00 USD |
| `7D` | `0.6140` | 80,500.00 USD | 0.00 USD | 80,500.00 USD | 51,900.00 USD | 8,040.00 USD | 4,040.00 USD |
| `1D` | `0.6160` | 13,240.00 USD | 0.00 USD | 13,240.00 USD | 0.00 USD | 0.00 USD | 3,130.00 USD |
| `7D` | `0.6160` | 16,520.00 USD | 0.00 USD | 16,520.00 USD | 0.00 USD | 0.00 USD | 16,520.00 USD |
| `1D` | `0.6180` | 10,120.00 USD | 0.00 USD | 10,120.00 USD | 0.00 USD | 1,760.00 USD | 8,360.00 USD |
| `1D` | `0.6190` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `0.6200` | 8,600.00 USD | 8,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,600.00 USD |
| `7D` | `0.6200` | 42,870.00 USD | 42,870.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 29,000.00 USD |
| `7D` | `0.6200` | 85,740.00 USD | 85,740.00 USD | 0.00 USD | 13,870.00 USD | 0.00 USD | 29,000.00 USD |
| `1D` | `0.6210` | 31,370.00 USD | 31,370.00 USD | 0.00 USD | 5,900.00 USD | 0.00 USD | 16,860.00 USD |
| `1D` | `0.6220` | 43,310.00 USD | 43,310.00 USD | 0.00 USD | 5,630.00 USD | 2,380.00 USD | 3,930.00 USD |
| `7D` | `0.6220` | 113,460.00 USD | 113,460.00 USD | 0.00 USD | 4,760.00 USD | 22,640.00 USD | 312.38 USD |
| `1D` | `0.6230` | 55,530.00 USD | 55,530.00 USD | 0.00 USD | 11,380.00 USD | 840.09 USD | 0.00 USD |
| `1D` | `0.6240` | 86,560.00 USD | 86,560.00 USD | 0.00 USD | 21,710.00 USD | 2,220.00 USD | 7,100.00 USD |
| `7D` | `0.6240` | 121,280.00 USD | 121,280.00 USD | 0.00 USD | 0.00 USD | 7,300.00 USD | 514.08 USD |
| `1D` | `0.6250` | 117,950.00 USD | 117,950.00 USD | 0.00 USD | 16,730.00 USD | 12,460.00 USD | 2,200.00 USD |
| `1D` | `0.6260` | 136,240.00 USD | 136,240.00 USD | 0.00 USD | 5,750.00 USD | 8,370.00 USD | 4,170.00 USD |
| `7D` | `0.6260` | 230,060.00 USD | 230,060.00 USD | 0.00 USD | 108,240.00 USD | 0.00 USD | 536.81 USD |
| `1D` | `0.6270` | 216,120.00 USD | 216,120.00 USD | 0.00 USD | 47,830.00 USD | 20,700.00 USD | 11,360.00 USD |
| `1D` | `0.6280` | 265,200.00 USD | 265,200.00 USD | 0.00 USD | 9,840.00 USD | 16,420.00 USD | 22,820.00 USD |
| `7D` | `0.6280` | 316,490.00 USD | 316,490.00 USD | 0.00 USD | 38,530.00 USD | 22,580.00 USD | 25,320.00 USD |
| `1D` | `0.6290` | 306,890.00 USD | 306,890.00 USD | 0.00 USD | 20,690.00 USD | 6,580.00 USD | 14,420.00 USD |
| `1D` | `0.6300` | 330,540.00 USD | 330,540.00 USD | 0.00 USD | 10,980.00 USD | 3,430.00 USD | 9,240.00 USD |
| `7D` | `0.6300` | 384,940.00 USD | 384,940.00 USD | 0.00 USD | 19,640.00 USD | 0.00 USD | 48,810.00 USD |
| `1D` | `0.6310` | 382,510.00 USD | 382,510.00 USD | 0.00 USD | 22,880.00 USD | 7,390.00 USD | 21,710.00 USD |
| `1D` | `0.6320` | 432,070.00 USD | 432,070.00 USD | 0.00 USD | 34,120.00 USD | 4,420.00 USD | 11,010.00 USD |
| `1D` | `0.6330` | 474,200.00 USD | 474,200.00 USD | 0.00 USD | 14,500.00 USD | 9,340.00 USD | 18,300.00 USD |
| `1D` | `0.6340` | 541,420.00 USD | 541,420.00 USD | 0.00 USD | 29,640.00 USD | 3,190.00 USD | 34,390.00 USD |
| `7D` | `0.6340` | 453,880.00 USD | 453,880.00 USD | 0.00 USD | 68,660.00 USD | 0.00 USD | 283.09 USD |
| `1D` | `0.6350` | 583,340.00 USD | 583,340.00 USD | 0.00 USD | 35,710.00 USD | 0.00 USD | 6,210.00 USD |
| `1D` | `0.6360` | 699,170.00 USD | 699,170.00 USD | 0.00 USD | 55,140.00 USD | 2,470.00 USD | 58,220.00 USD |
| `7D` | `0.6360` | 545,620.00 USD | 545,620.00 USD | 0.00 USD | 34,320.00 USD | 0.00 USD | 57,420.00 USD |
| `1D` | `0.6370` | 733,890.00 USD | 733,890.00 USD | 0.00 USD | 0.00 USD | 5,770.00 USD | 28,950.00 USD |
| `1D` | `0.6380` | 763,470.00 USD | 763,470.00 USD | 0.00 USD | 0.00 USD | 23,260.00 USD | 6,320.00 USD |
| `7D` | `0.6380` | 585,210.00 USD | 585,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 39,590.00 USD |
| `1D` | `0.6390` | 837,800.00 USD | 837,800.00 USD | 0.00 USD | 20,130.00 USD | 7,210.00 USD | 47,000.00 USD |
| `1D` | `0.6400` | 978,750.00 USD | 978,750.00 USD | 0.00 USD | 72,890.00 USD | 35,480.00 USD | 32,570.00 USD |
| `7D` | `0.6400` | 625,710.00 USD | 625,710.00 USD | 0.00 USD | 19,270.00 USD | 7,510.00 USD | 13,730.00 USD |
| `1D` | `0.6410` | 1,050,000.00 USD | 1,050,000.00 USD | 0.00 USD | 35,660.00 USD | 16,130.00 USD | 14,480.00 USD |
| `1D` | `0.6420` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 77,930.00 USD | 15,540.00 USD | 23,200.00 USD |
| `7D` | `0.6420` | 761,980.00 USD | 761,980.00 USD | 0.00 USD | 55,350.00 USD | 44,770.00 USD | 36,140.00 USD |
| `1D` | `0.6430` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 38,040.00 USD | 14,630.00 USD | 30,150.00 USD |
| `1D` | `0.6440` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 31,190.00 USD | 18,570.00 USD | 49,870.00 USD |
| `7D` | `0.6440` | 859,120.00 USD | 859,120.00 USD | 0.00 USD | 54,510.00 USD | 24,820.00 USD | 17,810.00 USD |
| `1D` | `0.6450` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 62,680.00 USD | 11,870.00 USD | 35,590.00 USD |
| `1D` | `0.6460` | 1,520,000.00 USD | 1,520,000.00 USD | 0.00 USD | 45,900.00 USD | 11,290.00 USD | 9,690.00 USD |
| `7D` | `0.6460` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 172,610.00 USD | 46,630.00 USD | 138,390.00 USD |
| `1D` | `0.6470` | 1,610,000.00 USD | 1,610,000.00 USD | 0.00 USD | 63,150.00 USD | 17,210.00 USD | 8,780.00 USD |
| `1D` | `0.6480` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 70,490.00 USD | 6,780.00 USD | 373.19 USD |
| `7D` | `0.6480` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 86,440.00 USD | 26,520.00 USD | 33,240.00 USD |
| `1D` | `0.6490` | 1,760,000.00 USD | 1,760,000.00 USD | 0.00 USD | 63,670.00 USD | 1,230.00 USD | 11,110.00 USD |
| `1D` | `0.6500` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 43,840.00 USD | 5,920.00 USD | 128.64 USD |
| `7D` | `0.6500` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 73,560.00 USD | 0.00 USD | 132,640.00 USD |
| `1D` | `0.6510` | 1,880,000.00 USD | 1,880,000.00 USD | 0.00 USD | 55,500.00 USD | 0.00 USD | 11,520.00 USD |
| `1D` | `0.6520` | 1,990,000.00 USD | 1,990,000.00 USD | 0.00 USD | 93,550.00 USD | 9,040.00 USD | 4,060.00 USD |
| `7D` | `0.6520` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 298,050.00 USD | 10,910.00 USD | 105,450.00 USD |
| `1D` | `0.6530` | 2,000,000.00 USD | 2,000,000.00 USD | 0.00 USD | 11,510.00 USD | 3,910.00 USD | 11.74 USD |
| `1D` | `0.6540` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 24,280.00 USD | 0.00 USD | 10,560.00 USD |
| `7D` | `0.6540` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 15,730.00 USD | 4,440.00 USD | 61,470.00 USD |
| `1D` | `0.6550` | 2,040,000.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 6,950.00 USD |
| `1D` | `0.6560` | 2,050,000.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 8,010.00 USD |
| `7D` | `0.6560` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 5,380.00 USD | 817.52 USD |
| `1D` | `0.6570` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,410.00 USD |
| `1D` | `0.6580` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 3,310.00 USD | 34.49 USD |
| `7D` | `0.6580` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 28,280.00 USD | 9,990.00 USD |
| `1D` | `0.6590` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 5,890.00 USD | 164.02 USD |
| `1D` | `0.6600` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 6,010.00 USD | 9,280.00 USD | 59.63 USD |
| `7D` | `0.6600` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 18,420.00 USD | 814.64 USD |
| `1D` | `0.6610` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 6,690.00 USD | 835.70 USD | 142.10 USD |
| `1D` | `0.6620` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 530.84 USD | 7,710.00 USD |
| `7D` | `0.6620` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 8,600.00 USD | 0.00 USD | 588.76 USD |
| `1D` | `0.6630` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 2,310.00 USD |
| `1D` | `0.6640` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 11,190.00 USD | 837.01 USD | 135.08 USD |
| `7D` | `0.6640` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 33,660.00 USD | 0.00 USD | 7,550.00 USD |
| `1D` | `0.6650` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 3,160.00 USD | 17,420.00 USD |
| `1D` | `0.6660` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 839.67 USD | 7,590.00 USD |
| `7D` | `0.6660` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 6,770.00 USD | 396.96 USD |
| `1D` | `0.6670` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 18,850.00 USD | 0.00 USD | 24.36 USD |
| `1D` | `0.6680` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 130.23 USD |
| `1D` | `0.6690` | 2,170,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 3,550.00 USD | 5,500.00 USD |
| `1D` | `0.6700` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 8,830.00 USD | 1,920.00 USD | 24,760.00 USD |
| `7D` | `0.6700` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 243.37 USD |
| `1D` | `0.6710` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 41,970.00 USD | 0.00 USD | 5,960.00 USD |
| `1D` | `0.6720` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `0.6720` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 58,470.00 USD | 0.00 USD | 30,240.00 USD |
| `1D` | `0.6730` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 25,660.00 USD | 3,670.00 USD | 5,560.00 USD |
| `1D` | `0.6740` | 2,370,000.00 USD | 2,370,000.00 USD | 0.00 USD | 64,370.00 USD | 8,170.00 USD | 9,210.00 USD |
| `7D` | `0.6740` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 39,730.00 USD | 0.00 USD | 364.93 USD |
| `1D` | `0.6750` | 2,420,000.00 USD | 2,420,000.00 USD | 0.00 USD | 28,700.00 USD | 4,630.00 USD | 12,070.00 USD |
| `1D` | `0.6760` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 11,840.00 USD | 5,850.00 USD | 0.00 USD |
| `7D` | `0.6760` | 2,430,000.00 USD | 2,430,000.00 USD | 0.00 USD | 0.00 USD | 77,970.00 USD | 33,160.00 USD |
| `1D` | `0.6770` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 19,930.00 USD | 8,320.00 USD | 15,020.00 USD |
| `1D` | `0.6780` | 2,540,000.00 USD | 2,540,000.00 USD | 0.00 USD | 33,610.00 USD | 13,860.00 USD | 12,140.00 USD |
| `7D` | `0.6780` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 63,600.00 USD | 16,810.00 USD | 17,960.00 USD |
| `1D` | `0.6790` | 2,570,000.00 USD | 2,570,000.00 USD | 0.00 USD | 2,940.00 USD | 18,610.00 USD | 12,520.00 USD |
| `1D` | `0.6800` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 1,680.00 USD | 686.25 USD | 2,450.00 USD |
| `7D` | `0.6800` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 16,590.00 USD | 4,460.00 USD |
| `1D` | `0.6810` | 2,590,000.00 USD | 2,590,000.00 USD | 0.00 USD | 1,690.00 USD | 2,460.00 USD | 11,970.00 USD |
| `1D` | `0.6820` | 2,640,000.00 USD | 2,640,000.00 USD | 0.00 USD | 22,600.00 USD | 16,590.00 USD | 9,030.00 USD |
| `7D` | `0.6820` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 32,570.00 USD | 53,450.00 USD | 0.00 USD |
| `1D` | `0.6830` | 2,740,000.00 USD | 2,740,000.00 USD | 0.00 USD | 24,570.00 USD | 20,000.00 USD | 49,600.00 USD |
| `1D` | `0.6840` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 45,780.00 USD | 17,210.00 USD | 13,900.00 USD |
| `7D` | `0.6840` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 57,890.00 USD | 54,300.00 USD | 102,430.00 USD |
| `1D` | `0.6850` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 41,830.00 USD | 5,780.00 USD | 24,130.00 USD |
| `1D` | `0.6860` | 2,940,000.00 USD | 2,940,000.00 USD | 0.00 USD | 40,250.00 USD | 4,380.00 USD | 14,780.00 USD |
| `7D` | `0.6860` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 49,930.00 USD | 14,540.00 USD | 10,480.00 USD |
| `7D` | `0.6880` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 38,030.00 USD | 17,300.00 USD | 131.40 USD |
| `7D` | `0.6900` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 15,510.00 USD | 16,550.00 USD |
| `7D` | `0.6920` | 3,140,000.00 USD | 3,140,000.00 USD | 0.00 USD | 69,620.00 USD | 2,090.00 USD | 61,890.00 USD |
| `7D` | `0.6940` | 3,200,000.00 USD | 3,200,000.00 USD | 0.00 USD | 14,220.00 USD | 0.00 USD | 42,460.00 USD |
| `7D` | `0.6960` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 59,960.00 USD | 0.00 USD | 12,390.00 USD |
| `7D` | `0.6980` | 3,320,000.00 USD | 3,320,000.00 USD | 0.00 USD | 35,980.00 USD | 16,990.00 USD | 0.00 USD |
| `7D` | `0.7000` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 29,740.00 USD | 0.00 USD | 40,190.00 USD |
| `7D` | `0.7020` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 29,810.00 USD | 0.00 USD | 53,380.00 USD |
| `7D` | `0.7040` | 3,670,000.00 USD | 3,670,000.00 USD | 0.00 USD | 95,520.00 USD | 0.00 USD | 96,320.00 USD |
| `7D` | `0.7060` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 47,840.00 USD | 33,490.00 USD | 177,930.00 USD |
| `7D` | `0.7080` | 4,100,000.00 USD | 4,100,000.00 USD | 0.00 USD | 24,440.00 USD | 64,870.00 USD | 82,800.00 USD |
| `7D` | `0.7100` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 150,830.00 USD | 63,530.00 USD | 149,060.00 USD |
| `7D` | `0.7120` | 4,870,000.00 USD | 4,870,000.00 USD | 0.00 USD | 101,040.00 USD | 78,760.00 USD | 227,910.00 USD |
| `7D` | `0.7140` | 5,280,000.00 USD | 5,280,000.00 USD | 0.00 USD | 202,560.00 USD | 67,260.00 USD | 133,720.00 USD |
| `7D` | `0.7160` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 113,040.00 USD | 65,260.00 USD | 164,620.00 USD |
| `7D` | `0.7180` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 165,860.00 USD | 56,910.00 USD | 66,960.00 USD |
| `7D` | `0.7200` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 93,750.00 USD | 45,160.00 USD | 178,460.00 USD |
| `7D` | `0.7220` | 6,710,000.00 USD | 6,710,000.00 USD | 0.00 USD | 318,420.00 USD | 67,130.00 USD | 98,110.00 USD |
| `7D` | `0.7240` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 146,110.00 USD | 24,910.00 USD | 129,240.00 USD |
| `7D` | `0.7260` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 106,410.00 USD | 52,120.00 USD | 176,180.00 USD |
| `7D` | `0.7280` | 7,570,000.00 USD | 7,570,000.00 USD | 0.00 USD | 99,750.00 USD | 40,180.00 USD | 84,240.00 USD |
| `7D` | `0.7300` | 7,850,000.00 USD | 7,850,000.00 USD | 0.00 USD | 115,310.00 USD | 60,310.00 USD | 109,550.00 USD |
| `7D` | `0.7320` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 189,840.00 USD | 65,640.00 USD | 80,630.00 USD |
| `7D` | `0.7340` | 8,290,000.00 USD | 8,290,000.00 USD | 0.00 USD | 31,260.00 USD | 8,620.00 USD | 62,910.00 USD |
| `7D` | `0.7360` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 103,600.00 USD | 46,790.00 USD | 35,010.00 USD |
| `7D` | `0.7380` | 8,630,000.00 USD | 8,630,000.00 USD | 0.00 USD | 73,710.00 USD | 19,000.00 USD | 60,680.00 USD |
| `7D` | `0.7400` | 8,650,000.00 USD | 8,650,000.00 USD | 0.00 USD | 1,730.00 USD | 4,760.00 USD | 12,210.00 USD |
| `7D` | `0.7420` | 8,750,000.00 USD | 8,750,000.00 USD | 0.00 USD | 35,810.00 USD | 35,860.00 USD | 31,340.00 USD |
| `7D` | `0.7440` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 74,450.00 USD | 33,900.00 USD | 70,670.00 USD |
| `7D` | `0.7460` | 9,090,000.00 USD | 9,090,000.00 USD | 0.00 USD | 88,800.00 USD | 17,230.00 USD | 51,570.00 USD |
| `7D` | `0.7480` | 9,220,000.00 USD | 9,220,000.00 USD | 0.00 USD | 60,580.00 USD | 28,900.00 USD | 38,210.00 USD |
| `7D` | `0.7500` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 52,320.00 USD | 12,610.00 USD | 25,050.00 USD |
| `7D` | `0.7520` | 9,420,000.00 USD | 9,420,000.00 USD | 0.00 USD | 53,470.00 USD | 13,000.00 USD | 51,060.00 USD |
| `7D` | `0.7530` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 21,290.00 USD | 1,890.00 USD | 14,770.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `87.54M` | Total OI Tokens: `141,166,855.8 APT`
  * 1h OI Change: `+0.70%` | 4h OI Change: `+4.23%` | 24h OI Change: `-8.68%`
  * Exchange Breakdown: Binance=`15.66M` | Bybit=`17.31M` | OKX=`4.12M` | Hyperliquid=`3.42M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-7.84K` | Last 24h: `2.90K` | Last 3d: `7.60K` | Last 7d: `2.85K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `-0.0189%` | **USDT OKX** | `-0.0200%` |
| **USDT Bybit** | `-0.0237%` | **USDT KuCoin** | `-0.0217%` |
| **USDT MEXC** | `-0.0187%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `-0.0105%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `-` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `APT` | `47.51%` | `52.49%` | `0.91` | 4,020,000.00 USD |
| `15M` | `Binance` | `49.36%` | `50.64%` | `0.97` | 1,440,000.00 USD |
| `15M` | `OKX` | `53.36%` | `46.64%` | `1.14` | 1,100,000.00 USD |
| `15M` | `Bybit` | `47.48%` | `52.52%` | `0.90` | 239,770.00 USD |
| `15M` | `KuCoin` | `48.56%` | `51.44%` | `0.94` | 173,160.00 USD |
| `15M` | `Gate` | `43.67%` | `56.33%` | `0.78` | 70,180.00 USD |
| `15M` | `Bitget` | `49.6%` | `50.4%` | `0.98` | 29,900.00 USD |
| `15M` | `BingX` | `44.43%` | `55.57%` | `0.80` | 52,330.00 USD |
| `15M` | `MEXC` | `40.01%` | `59.99%` | `0.67` | 20,460.00 USD |
| `15M` | `Bitunix` | `28.48%` | `71.52%` | `0.40` | 123,990.00 USD |
| `15M` | `Hyperliquid` | `90.28%` | `9.72%` | `9.29` | 24,350.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `43.36%` | `56.64%` | `0.77` | 662,000.00 USD |
| `15M` | `Crypto.com` | `40.01%` | `59.99%` | `0.67` | 14.21 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 77,310.00 USD |
| `15M` | `HTX` | `0.18%` | `99.82%` | `0.00` | 20,370.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `20.05%` | `79.95%` | `0.25` | 600.13 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `100%` | `0%` | `1.00` | 13.34 USD |
| `15M` | `Whale Positions` | `49.36%` | `50.64%` | `0.97` | 1,440,000.00 USD |
| `15M` | `Global Accounts` | `47.51%` | `52.49%` | `0.91` | 4,020,000.00 USD |
| `1H` | `APT` | `44.23%` | `55.77%` | `0.79` | 11,140,000.00 USD |
| `1H` | `Binance` | `44.34%` | `55.66%` | `0.80` | 3,750,000.00 USD |
| `1H` | `OKX` | `47.02%` | `52.98%` | `0.89` | 1,570,000.00 USD |
| `1H` | `Bybit` | `47.34%` | `52.66%` | `0.90` | 875,150.00 USD |
| `1H` | `KuCoin` | `50.53%` | `49.47%` | `1.02` | 118,700.00 USD |
| `1H` | `Gate` | `46.02%` | `53.98%` | `0.85` | 1,260,000.00 USD |
| `1H` | `Bitget` | `35.92%` | `64.08%` | `0.56` | 356,020.00 USD |
| `1H` | `BingX` | `43.21%` | `56.79%` | `0.76` | 1,890,000.00 USD |
| `1H` | `MEXC` | `30.08%` | `69.92%` | `0.43` | 282,740.00 USD |
| `1H` | `Bitunix` | `39.94%` | `60.06%` | `0.67` | 384,990.00 USD |
| `1H` | `Hyperliquid` | `13.27%` | `86.73%` | `0.15` | 122,460.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `42.68%` | `57.32%` | `0.74` | 403,100.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `97.49%` | `2.51%` | `38.84` | 66,020.00 USD |
| `1H` | `HTX` | `69.62%` | `30.38%` | `2.29` | 18,300.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `57.08%` | `42.92%` | `1.33` | 34,460.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `78%` | `22%` | `3.55` | 1,270.00 USD |
| `1H` | `Whale Positions` | `44.34%` | `55.66%` | `0.80` | 3,750,000.00 USD |
| `1H` | `Global Accounts` | `44.23%` | `55.77%` | `0.79` | 11,140,000.00 USD |
| `4H` | `APT` | `49.02%` | `50.98%` | `0.96` | 90,830,000.00 USD |
| `4H` | `Binance` | `50.33%` | `49.67%` | `1.01` | 33,380,000.00 USD |
| `4H` | `OKX` | `51.66%` | `48.34%` | `1.07` | 21,140,000.00 USD |
| `4H` | `Bybit` | `51.34%` | `48.66%` | `1.06` | 7,110,000.00 USD |
| `4H` | `KuCoin` | `51.39%` | `48.61%` | `1.06` | 2,700,000.00 USD |
| `4H` | `Gate` | `47.96%` | `52.04%` | `0.92` | 2,020,000.00 USD |
| `4H` | `Bitget` | `55.08%` | `44.92%` | `1.23` | 2,580,000.00 USD |
| `4H` | `BingX` | `20.89%` | `79.11%` | `0.26` | 2,960,000.00 USD |
| `4H` | `MEXC` | `56.28%` | `43.72%` | `1.29` | 1,230,000.00 USD |
| `4H` | `Bitunix` | `49%` | `51%` | `0.96` | 2,860,000.00 USD |
| `4H` | `Hyperliquid` | `40.66%` | `59.34%` | `0.69` | 743,130.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.01%` | `50.99%` | `0.96` | 12,330,000.00 USD |
| `4H` | `Crypto.com` | `79.93%` | `20.07%` | `3.98` | 1,390.00 USD |
| `4H` | `WhiteBIT` | `6.3%` | `93.7%` | `0.07` | 1,370,000.00 USD |
| `4H` | `HTX` | `41.29%` | `58.71%` | `0.70` | 73,100.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `73.74%` | `26.26%` | `2.81` | 148,290.00 USD |
| `4H` | `Aster` | `50.54%` | `49.46%` | `1.02` | 130,130.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `51.26%` | `48.74%` | `1.05` | 56,500.00 USD |
| `4H` | `Whale Positions` | `50.33%` | `49.67%` | `1.01` | 33,380,000.00 USD |
| `4H` | `Global Accounts` | `49.02%` | `50.98%` | `0.96` | 90,830,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `0.6099` | `0.6090` | `0.6099` | `0.6109` | `0.6063` | 539,317.21 USD | 218,354.05 USD | 320,963.16 USD | -102,609.12 USD | `-19.03%` | `3B / 5S` |
| `5:00 UTC` | `0.6071` | `0.6045` | `0.6071` | `0.6092` | `0.6016` | 771,529.71 USD | 428,044.31 USD | 343,485.41 USD | 84,558.90 USD | `+10.96%` | `12B / 18S` |
| `0:00 UTC` | `0.6067` | `0.6054` | `0.6067` | `0.6069` | `0.6027` | 290,014.01 USD | 171,806.26 USD | 118,207.75 USD | 53,598.51 USD | `+18.48%` | `8B / 3S` |
| `5:00 UTC` | `0.6083` | `0.6072` | `0.6083` | `0.6096` | `0.6042` | 191,671.81 USD | 128,624.28 USD | 63,047.54 USD | 65,576.74 USD | `+34.21%` | `17B / 3S` |
| `0:00 UTC` | `0.6152` | `0.6139` | `0.6152` | `0.6175` | `0.6090` | 470,291.39 USD | 289,898.53 USD | 180,392.87 USD | 109,505.66 USD | `+23.28%` | `29B / 6S` |
| `5:00 UTC` | `0.6161` | `0.6160` | `0.6161` | `0.6176` | `0.6147` | 319,675.12 USD | 174,523.38 USD | 145,151.74 USD | 29,371.64 USD | `+9.19%` | `4B / 6S` |
| `0:00 UTC` | `0.6151` | `0.6150` | `0.6151` | `0.6187` | `0.6118` | 468,512.46 USD | 237,013.59 USD | 231,498.87 USD | 5,514.73 USD | `+1.18%` | `14B / 9S` |
| `5:00 UTC` | `0.6179` | `0.6169` | `0.6179` | `0.6184` | `0.6149` | 312,659.38 USD | 170,069.09 USD | 142,590.29 USD | 27,478.79 USD | `+8.79%` | `4B / 2S` |
| `0:00 UTC` | `0.6169` | `0.6172` | `0.6169` | `0.6184` | `0.6159` | 332,795.97 USD | 159,318.96 USD | 173,477.01 USD | -14,158.04 USD | `-4.25%` | `4B / 4S` |
| `5:00 UTC` | `0.6199` | `0.6192` | `0.6199` | `0.6207` | `0.6170` | 366,443.96 USD | 116,462.20 USD | 249,981.76 USD | -133,519.56 USD | `-36.44%` | `5B / 5S` |

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
| `5m` | 8,010.00 USD | -107,130.00 USD | **`DISTRIBUTION`** |
| `15m` | 25,090.00 USD | -218,140.00 USD | **`DISTRIBUTION`** |
| `30m` | 42,080.00 USD | -131,030.00 USD | **`DISTRIBUTION`** |
| `1h` | -69,300.00 USD | -234,100.00 USD | **`DISTRIBUTION`** |
| `2h` | 98,650.00 USD | 317,470.00 USD | **`ACCUMULATION`** |
| `4h` | 12,870.00 USD | 831,150.00 USD | **`ACCUMULATION`** |
| `6h` | -477,700.00 USD | -996,480.00 USD | **`DISTRIBUTION`** |
| `8h` | -608,640.00 USD | -5,290,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -1,300,000.00 USD | -6,730,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -1,210,000.00 USD | -8,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -5,730,000.00 USD | -25,560,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -28,530,000.00 USD | -106,320,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+8.01K` | 15m=`+25.09K` | 1h=`-69.30K` | 24h=`-1.21M`
* Futures Capital Netflows: 5m=`-107.13K` | 15m=`-218.14K` | 1h=`-234.10K` | 24h=`-8.88M`
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
  * `2026-10-30 09:51:07 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:20:07 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 10:19:07 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:21:07 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:21:07 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 05:21:07 IST`: [media.rabobank.com] - (Sentiment: `Neutral`)


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
