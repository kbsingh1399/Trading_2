# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 22:52:02 IST` (`2026-10-29 17:22:02 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `58.05` | **Live Ask Quote**: `58.35` | **Mid Price**: `58.20`
- **Spread Points**: `300.00` | **Spread BPS**: `51.55 bps` (Charter Threshold: `25.00 bps`)
- **Gate 1 Clearance**: **`SPREAD_DISQUALIFIED`** | **Execution Posture**: `DISQUALIFIED` | **Order Type Allowed**: `NONE`
- **True Broker Contract Specifications**:
  * Contract Size: `1.0` | Digits: `2` | Point: `0.01`
  * Point Value (1.0 Lot): `0.01 USD` | Point Value (0.01 Lot): `0.0001 USD`
  * Allowed Lot Sizing: Min Lot=`0.01` | Step Lot=`0.01` | Max Lot=`20.00`
- **Solvency Defense Ladder**:
  * Hard Floor Stop: `4,775.00 USD` (Zero Open Risk) | Operating Defense Buffer: `4,795.00 USD` (Capital Preservation Mode)
  * Kernel Admission Floor: `4,795.00 USD` (`min(balance, equity) - StressedLoss - 2.00 >= 4,795.00 USD`)
- **Pipeline Health (23_Master_Pipeline_Telemetry.parquet)**: Status=`HEALTHY` | Latency=`4.2 ms` | RAM Usage=`385.0 MB`

---

## 2. Technical Profile, VWAP Dispersion Grid & BTC Ribbon
*(Sources: 11_Technical.parquet, 11_Technical_BTC_Ribbon.parquet)*
- **Session Anchor & Volatility**:
  * Session VWAP: `57.84` | VWAP Z-Score: `+0.62` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.3393` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `55.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `59.75` | Lower -3.00σ Band: `55.93`
  * Upper +2.51σ Band: `59.44` | Lower -2.51σ Band: `56.25`
  * Upper +2.01σ Band: `59.12` | Lower -2.01σ Band: `56.56`
  * Upper +2.00σ Band: `59.11` | Lower -2.00σ Band: `56.57`
  * Upper +1.28σ Band: `58.66` | Lower -1.28σ Band: `57.03`
  * Upper +1.00σ Band: `58.48` | Lower -1.00σ Band: `57.21`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`58.23` | EMA-20=`58.03` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.84` (Slope: `+0.0000`) | EMA-100=`57.79`
  * Institutional Anchors: EMA-144=`57.68` | EMA-200=`57.48` (Slope: `+0.1433`) | EMA-233=`57.29`
- **Range Boundaries**: 24H High=`59.62` | 24H Low=`56.67` | Weekly High=`59.62` | Weekly Low=`55.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `59.18` (Distance: `-1.58%`)
  * Point of Control (POC) = `57.84` (Distance: `+0.72%`)
  * Value Area Low (VAL) = `57.46` (Distance: `+1.38%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.44` | POC=`57.22` | VAL=`56.70`
  * Prior Day Extremes: PDH=`59.62` | PDL=`56.37` | PDC=`58.69`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.76` | Weekly POC=`56.49` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`59.52` | Low=`56.73`
  * London Session (08:00-16:00 UTC): High=`58.12` | Low=`56.67`
  * New York Session (13:00-21:00 UTC): High=`58.72` | Low=`57.04`
  * Initial Balance (First Hour): IB High=`58.02` | IB Low=`57.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `57.97` - `58.43`
  * Optimal Trade Entry (OTE 0.705): `58.32`
  * Structural Invalidation Anchor (0.786): `58.67`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `58.44` | `58.44` | `58.27` | `58.31` | `7,205` | 420,470.17 USD | -163,317.81 USD | `-38.84%` | -759,292.39 USD | `-0.80` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `58.31` | `58.31` | `58.17` | `58.25` | `5,486` | 319,467.81 USD | -29,241.70 USD | `-9.15%` | -788,534.09 USD | `-0.10` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `58.25` | `58.30` | `58.20` | `58.28` | `1,331` | 77,550.34 USD | -5,161.35 USD | `-6.66%` | -793,695.43 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `58.62` | `58.68` | `58.37` | `58.46` | `11,556` | 676,217.74 USD | -95,802.70 USD | `-14.17%` | -650,556.54 USD | `-0.54` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `58.47` | `58.52` | `58.31` | `58.43` | `11,892` | 694,681.39 USD | 54,581.96 USD | `+7.86%` | -595,974.58 USD | `+0.16` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `58.44` | `58.44` | `58.17` | `58.28` | `14,022` | 817,488.32 USD | -197,720.85 USD | `-24.19%` | -793,695.43 USD | `-1.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `57.84` | `58.68` | `57.81` | `58.62` | `63,089` | 3,682,096.48 USD | -283,247.54 USD | `-7.69%` | -988,865.32 USD | `-0.65` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `58.63` | `58.93` | `58.31` | `58.43` | `105,448` | 6,183,662.04 USD | 224,464.05 USD | `+3.63%` | -764,401.27 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `58.44` | `58.44` | `58.17` | `58.28` | `14,022` | 817,488.32 USD | -197,720.85 USD | `-24.19%` | -962,122.12 USD | `-0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `58.17` | `58.28` | `119,469` | 7,001,150.36 USD | 26,743.20 USD | `+0.38%` | -1,015,002.13 USD | `+0.35` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `59.19` | `59.70` | `56.95` | `57.21` | `387,394` | 22,568,170.72 USD | -1,232,294.71 USD | `-5.46%` | -1,242,932.23 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -1,743,140.06 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,290,330.89 USD | `+1.24` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.68` | `57.61` | `58.62` | `226,840` | 13,180,757.08 USD | 248,585.56 USD | `+1.89%` | -1,041,745.33 USD | `+0.76` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.63` | `58.93` | `58.17` | `58.28` | `119,469` | 7,001,150.36 USD | 26,743.20 USD | `+0.38%` | -1,015,002.13 USD | `+0.35` | **`BULLISH`** | `BULLISH ABSORPTION` |

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
| --- | **`58.20`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 22:44:58 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1070` | `0xeadc...9d55` | `LONG` | 2,123,103.01 USD | `36,463.77` | `52.78` | `58.19` | `0.000000` | 198,427.06 USD | `+9.35%` | `10X Cross` |
| `1078` | `0x9aa5...58af` | `SHORT` | 2,107,058.69 USD | `36,177.65` | `71.22` | `58.19` | `252.12` | 469,427.98 USD | `+22.28%` | `10X Cross` |
| `2031` | `0xcac1...26b3` | `SHORT` | 1,013,404.44 USD | `17,411.55` | `49.01` | `58.19` | `486.39` | -159,999.12 USD | `-15.79%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `56.75` | 8,512.80 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 8.51K USD at 56.7520 USD [API] | `2026-10-27 19:07:24` |
| `ANNOUNCEMENT` | `INFO` | `56.70` | 5,103.18 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.10K USD at 56.7020 USD [API] | `2026-10-27 20:03:44` |
| `ANNOUNCEMENT` | `INFO` | `56.65` | 5,700.59 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.70K USD at 56.6490 USD [API] | `2026-10-27 20:41:45` |
| `ANNOUNCEMENT` | `INFO` | `56.60` | 9,999.84 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 10.00K USD at 56.6050 USD [API] | `2026-10-27 21:22:06` |
| `ANNOUNCEMENT` | `INFO` | `57.00` | 7,510.28 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 57.0040 USD [API] | `2026-10-27 21:51:50` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 256,600.00 USD, Dist: `+1.44%`) | Long MP=`56.68` (Vol: 327,300.00 USD, Dist: `--2.59%`)
  * 48H Horizon: Short MP=`59.03` (Vol: 286,000.00 USD, Dist: `+1.44%`) | Long MP=`56.69` (Vol: 302,600.00 USD, Dist: `--2.58%`)
  * 3D Horizon: Short MP=`59.01` (Vol: 285,100.00 USD, Dist: `+1.40%`) | Long MP=`56.70` (Vol: 302,600.00 USD, Dist: `--2.57%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 256,600.00 USD, Dist: `+1.45%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--5.02%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.95` | 446.40 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.45` | 4,260.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.15` | 589.64 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.45` | 3,010.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.65` | 1,880.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.35` | 1,040.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.95` | 5,690.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.95` | 4,490.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.45` | 566.67 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.15` | 341.15 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 491.90 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.45` | 19,950.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.55` | 127.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 194.75 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 51,610.00 USD | 2,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.25` | 205.54 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 5,490.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 966.50 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.15` | 3,490.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.45` | 4,100.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 2,270.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.65` | 3,870.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 298,340.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 305.50 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 7,070.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 1,450.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 953.68 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.15` | 5,780.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 249.38 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 658.87 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 4,140.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 462.66 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.15` | 4,650.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.65` | 8,060.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 608.57 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 976.97 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 7,570.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 287.61 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 4,880.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 148.80 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 6,890.00 USD | 1,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.15` | 33,680.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 18,010.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 416.50 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 65,900.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 26,780.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 7,120.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 10,250.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 312.26 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,390.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 706.06 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 1,850.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 12,190.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 11,950.00 USD | 938,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 12,490.00 USD | 926,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 913,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 913,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 910,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 910,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,830.00 USD | 910,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 1,780.00 USD | 906,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 904,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 318.39 USD | 880,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 880,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,710.00 USD | 879,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,320.00 USD | 870,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 383.78 USD | 830,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 830,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 829,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 829,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 49,130.00 USD | 829,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 779,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 779,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 776,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 774,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.65` | 6,850.00 USD | 772,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 765,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 975.66 USD | 761,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 1,440.00 USD | 760,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 758,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 756,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 4,390.00 USD | 754,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 749,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 747,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 231.56 USD | 747,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,390.00 USD | 747,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 745,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 744,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 738,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 1,960.00 USD | 733,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 731,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 4,890.00 USD | 713,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 1,250.00 USD | 708,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 18,920.00 USD | 707,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 688,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 659,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 657,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 657,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 656,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 103,540.00 USD | 652,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.65` | 25,330.00 USD | 548,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 523,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 514,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `51.05` | 550.32 USD | 513,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.10` | 19,170,000.00 USD | 19,170,000.00 USD | 114,000.00 USD | 49,240.00 USD | 98,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 513,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.20` | 18,900,000.00 USD | 18,900,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 18,840,000.00 USD | 18,840,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 18,770,000.00 USD | 18,770,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 22,090.00 USD | 294,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.50` | 18,620,000.00 USD | 18,620,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 271,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.60` | 18,530,000.00 USD | 18,530,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 271,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.70` | 18,470,000.00 USD | 18,470,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 271,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.80` | 18,430,000.00 USD | 18,430,000.00 USD | 22,510.00 USD | 12,820.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 3,580.00 USD | 264,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.90` | 18,370,000.00 USD | 18,370,000.00 USD | 5,870.00 USD | 15,240.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 261,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `52.00` | 18,350,000.00 USD | 18,350,000.00 USD | 64,300.00 USD | 17,390.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 18,250,000.00 USD | 18,250,000.00 USD | 24,220.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 18,190,000.00 USD | 18,190,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.30` | 6,010,000.00 USD | 6,010,000.00 USD | 57,580.00 USD | 23,000.00 USD | 30,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 18,120,000.00 USD | 18,120,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 1,470.00 USD | 249,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 5,900,000.00 USD | 5,900,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 18,090,000.00 USD | 18,090,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,620.00 USD | 247,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 5,880,000.00 USD | 5,880,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 18,040,000.00 USD | 18,040,000.00 USD | 33,240.00 USD | 667.05 USD | 18,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 244,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 5,860,000.00 USD | 5,860,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 17,980,000.00 USD | 17,980,000.00 USD | 52,790.00 USD | 16,820.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 5,830,000.00 USD | 5,830,000.00 USD | 18,580.00 USD | 12,960.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 17,910,000.00 USD | 17,910,000.00 USD | 20,660.00 USD | 30,990.00 USD | 49,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,450.00 USD | 235,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 5,780,000.00 USD | 5,780,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 17,800,000.00 USD | 17,800,000.00 USD | 54,600.00 USD | 18,870.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 227,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 5,750,000.00 USD | 5,750,000.00 USD | 29,080.00 USD | 2,430.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 17,730,000.00 USD | 17,730,000.00 USD | 51,920.00 USD | 24,700.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 11,500.00 USD | 221,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 5,710,000.00 USD | 5,710,000.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 17,650,000.00 USD | 17,650,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 900.26 USD | 210,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 5,700,000.00 USD | 5,700,000.00 USD | 9,600.00 USD | 2,780.00 USD | 882.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 17,590,000.00 USD | 17,590,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 23,340.00 USD | 209,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 5,690,000.00 USD | 5,690,000.00 USD | 11,160.00 USD | 8,090.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 17,500,000.00 USD | 17,500,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,500.00 USD | 186,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 5,660,000.00 USD | 5,660,000.00 USD | 10,170.00 USD | 4,410.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 17,360,000.00 USD | 17,360,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 184,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 5,640,000.00 USD | 5,640,000.00 USD | 24,480.00 USD | 4,490.00 USD | 14,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 17,250,000.00 USD | 17,250,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 182,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 5,600,000.00 USD | 5,600,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 17,150,000.00 USD | 17,150,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 5,580,000.00 USD | 5,580,000.00 USD | 19,360.00 USD | 5,030.00 USD | 10,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 17,060,000.00 USD | 17,060,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 177,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 5,550,000.00 USD | 5,550,000.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 16,990,000.00 USD | 16,990,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 148.35 USD | 177,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 5,540,000.00 USD | 5,540,000.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 16,900,000.00 USD | 16,900,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 177,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 5,540,000.00 USD | 5,540,000.00 USD | 6,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 16,670,000.00 USD | 16,670,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 28,950.00 USD | 175,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 5,540,000.00 USD | 5,540,000.00 USD | 2,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 16,410,000.00 USD | 16,410,000.00 USD | 342,600.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 19,340.00 USD | 146,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 5,530,000.00 USD | 5,530,000.00 USD | 11,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 15,710,000.00 USD | 15,710,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,030.00 USD | 126,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 5,520,000.00 USD | 5,520,000.00 USD | 15,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 15,290,000.00 USD | 15,290,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 3,260.00 USD | 113,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 5,510,000.00 USD | 5,510,000.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 14,790,000.00 USD | 14,790,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 5,500,000.00 USD | 5,500,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 14,190,000.00 USD | 14,190,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.45` | 14,120.00 USD | 110,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,500,000.00 USD | 5,500,000.00 USD | 3,070.00 USD | 126.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 13,660,000.00 USD | 13,660,000.00 USD | 170,480.00 USD | 53,460.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 1,060.00 USD | 96,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 5,500,000.00 USD | 5,500,000.00 USD | 3,300.00 USD | 601.45 USD | 944.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 13,290,000.00 USD | 13,290,000.00 USD | 108,280.00 USD | 43,430.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 488.57 USD | 95,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.70` | 5,490,000.00 USD | 5,490,000.00 USD | 51,940.00 USD | 15,810.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 13,070,000.00 USD | 13,070,000.00 USD | 123,820.00 USD | 50,560.00 USD | 172,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 470.85 USD | 94,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.80` | 5,370,000.00 USD | 5,370,000.00 USD | 47,390.00 USD | 18,410.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 12,720,000.00 USD | 12,720,000.00 USD | 309,200.00 USD | 104,820.00 USD | 156,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 5,280,000.00 USD | 5,280,000.00 USD | 53,720.00 USD | 21,230.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 12,150,000.00 USD | 12,150,000.00 USD | 257,210.00 USD | 162,220.00 USD | 276,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 7,160.00 USD | 94,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.00` | 5,200,000.00 USD | 5,200,000.00 USD | 38,520.00 USD | 24,110.00 USD | 12,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 11,460,000.00 USD | 11,460,000.00 USD | 266,790.00 USD | 81,220.00 USD | 310,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 1,100.00 USD | 87,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.10` | 5,120,000.00 USD | 5,120,000.00 USD | 26,400.00 USD | 10,460.00 USD | 18,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 10,800,000.00 USD | 10,800,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 3,010.00 USD | 86,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.20` | 5,070,000.00 USD | 5,070,000.00 USD | 19,810.00 USD | 4,030.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 10,120,000.00 USD | 10,120,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 5,030,000.00 USD | 5,030,000.00 USD | 11,840.00 USD | 5,120.00 USD | 12,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 9,320,000.00 USD | 9,320,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 83,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.40` | 5,000,000.00 USD | 5,000,000.00 USD | 29,970.00 USD | 51,060.00 USD | 19,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 8,630,000.00 USD | 8,630,000.00 USD | 302,780.00 USD | 187,160.00 USD | 237,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.45` | 1,090.00 USD | 81,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.50` | 4,900,000.00 USD | 4,900,000.00 USD | 71,580.00 USD | 25,990.00 USD | 61,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 7,900,000.00 USD | 7,900,000.00 USD | 329,130.00 USD | 178,270.00 USD | 529,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.55` | 1,390.00 USD | 80,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.60` | 4,740,000.00 USD | 4,740,000.00 USD | 97,100.00 USD | 20,900.00 USD | 82,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 6,860,000.00 USD | 6,860,000.00 USD | 426,340.00 USD | 260,600.00 USD | 243,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.65` | 676.15 USD | 79,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.70` | 4,540,000.00 USD | 4,540,000.00 USD | 90,090.00 USD | 49,390.00 USD | 47,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 5,930,000.00 USD | 5,930,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.75` | 153.87 USD | 78,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.80` | 4,360,000.00 USD | 4,360,000.00 USD | 120,170.00 USD | 47,100.00 USD | 42,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 5,450,000.00 USD | 5,450,000.00 USD | 60,840.00 USD | 54,060.00 USD | 143,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 4,150,000.00 USD | 4,150,000.00 USD | 118,870.00 USD | 60,380.00 USD | 130,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 5,200,000.00 USD | 5,200,000.00 USD | 65,400.00 USD | 94,590.00 USD | 280,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 3,840,000.00 USD | 3,840,000.00 USD | 125,000.00 USD | 60,260.00 USD | 56,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 4,760,000.00 USD | 4,760,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.10` | 3,600,000.00 USD | 3,600,000.00 USD | 98,040.00 USD | 77,880.00 USD | 26,680.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.10` | 4,380,000.00 USD | 4,380,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `56.20` | 3,390,000.00 USD | 3,390,000.00 USD | 73,120.00 USD | 74,660.00 USD | 87,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.20` | 4,080,000.00 USD | 4,080,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.30` | 3,160,000.00 USD | 3,160,000.00 USD | 77,950.00 USD | 44,480.00 USD | 65,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.30` | 3,680,000.00 USD | 3,680,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.40` | 2,970,000.00 USD | 2,970,000.00 USD | 185,180.00 USD | 35,450.00 USD | 111,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.40` | 3,370,000.00 USD | 3,370,000.00 USD | 215,940.00 USD | 124,050.00 USD | 139,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.50` | 2,640,000.00 USD | 2,640,000.00 USD | 69,340.00 USD | 109,070.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.50` | 2,890,000.00 USD | 2,890,000.00 USD | 26,520.00 USD | 98,550.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.60` | 2,420,000.00 USD | 2,420,000.00 USD | 161,590.00 USD | 60,330.00 USD | 124,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.60` | 2,710,000.00 USD | 2,710,000.00 USD | 363,190.00 USD | 113,010.00 USD | 128,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.70` | 2,070,000.00 USD | 2,070,000.00 USD | 204,190.00 USD | 64,830.00 USD | 190,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.70` | 2,110,000.00 USD | 2,110,000.00 USD | 110,940.00 USD | 104,010.00 USD | 138,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.80` | 1,610,000.00 USD | 1,610,000.00 USD | 189,690.00 USD | 111,830.00 USD | 122,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.80` | 1,760,000.00 USD | 1,760,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.90` | 1,190,000.00 USD | 1,190,000.00 USD | 299,280.00 USD | 93,310.00 USD | 119,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.90` | 1,240,000.00 USD | 1,240,000.00 USD | 108,440.00 USD | 65,260.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.00` | 674,640.00 USD | 674,640.00 USD | 34,380.00 USD | 20,790.00 USD | 44,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.00` | 975,190.00 USD | 975,190.00 USD | 50,710.00 USD | 111,790.00 USD | 91,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.10` | 574,760.00 USD | 574,760.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.10` | 721,290.00 USD | 721,290.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.20` | 471,550.00 USD | 471,550.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.20` | 669,330.00 USD | 669,330.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.30` | 403,660.00 USD | 403,660.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.30` | 594,180.00 USD | 594,180.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.40` | 336,230.00 USD | 336,230.00 USD | 19,650.00 USD | 26,470.00 USD | 1,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.40` | 498,970.00 USD | 498,970.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.50` | 288,770.00 USD | 288,770.00 USD | 80,510.00 USD | 12,870.00 USD | 36,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.50` | 300,510.00 USD | 300,510.00 USD | 76,670.00 USD | 23,070.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.60` | 158,550.00 USD | 158,550.00 USD | 138,820.00 USD | 0.00 USD | 19,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.60` | 131,890.00 USD | 131,890.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.80` | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 638.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 94,790.00 USD | 94,790.00 USD | 48,820.00 USD | 20,920.00 USD | 255.20 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 8,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 113,690.00 USD | 113,690.00 USD | 0.00 USD | 10,240.00 USD | 602.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 127,280.00 USD | 127,280.00 USD | 0.00 USD | 3,320.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 255,630.00 USD | 255,630.00 USD | 0.00 USD | 102,110.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 203,260.00 USD | 203,260.00 USD | 0.00 USD | 45,070.00 USD | 30,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 571,890.00 USD | 571,890.00 USD | 141,660.00 USD | 51,970.00 USD | 122,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 625,220.00 USD | 625,220.00 USD | 255,180.00 USD | 48,210.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 966,070.00 USD | 966,070.00 USD | 189,650.00 USD | 40,310.00 USD | 164,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 850,060.00 USD | 850,060.00 USD | 91,060.00 USD | 43,600.00 USD | 90,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 1,280,000.00 USD | 1,280,000.00 USD | 149,140.00 USD | 72,500.00 USD | 95,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 1,190,000.00 USD | 1,190,000.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 1,770,000.00 USD | 1,770,000.00 USD | 283,630.00 USD | 71,450.00 USD | 132,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 1,460,000.00 USD | 1,460,000.00 USD | 88,710.00 USD | 67,460.00 USD | 117,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 1,980,000.00 USD | 1,980,000.00 USD | 78,510.00 USD | 53,540.00 USD | 76,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 1,780,000.00 USD | 1,780,000.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 2,160,000.00 USD | 2,160,000.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 1,910,000.00 USD | 1,910,000.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 2,300,000.00 USD | 2,300,000.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 2,510,000.00 USD | 2,510,000.00 USD | 363,240.00 USD | 145,550.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 2,480,000.00 USD | 2,480,000.00 USD | 20,820.00 USD | 63,340.00 USD | 94,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 2,900,000.00 USD | 2,900,000.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 2,700,000.00 USD | 2,700,000.00 USD | 100,280.00 USD | 51,160.00 USD | 68,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 3,270,000.00 USD | 3,270,000.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 2,920,000.00 USD | 2,920,000.00 USD | 113,050.00 USD | 26,580.00 USD | 78,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 3,710,000.00 USD | 3,710,000.00 USD | 284,130.00 USD | 107,860.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 3,290,000.00 USD | 3,290,000.00 USD | 226,310.00 USD | 63,870.00 USD | 82,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 4,210,000.00 USD | 4,210,000.00 USD | 231,370.00 USD | 190,040.00 USD | 82,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 3,490,000.00 USD | 3,490,000.00 USD | 98,470.00 USD | 39,900.00 USD | 66,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 4,770,000.00 USD | 4,770,000.00 USD | 263,890.00 USD | 122,370.00 USD | 174,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 3,760,000.00 USD | 3,760,000.00 USD | 136,940.00 USD | 37,620.00 USD | 86,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 5,230,000.00 USD | 5,230,000.00 USD | 207,990.00 USD | 130,630.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 4,060,000.00 USD | 4,060,000.00 USD | 113,360.00 USD | 95,210.00 USD | 101,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 5,600,000.00 USD | 5,600,000.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 4,390,000.00 USD | 4,390,000.00 USD | 164,430.00 USD | 72,990.00 USD | 92,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 6,040,000.00 USD | 6,040,000.00 USD | 89,500.00 USD | 126,870.00 USD | 225,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 4,700,000.00 USD | 4,700,000.00 USD | 147,700.00 USD | 55,300.00 USD | 104,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 6,500,000.00 USD | 6,500,000.00 USD | 160,180.00 USD | 89,260.00 USD | 207,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 4,830,000.00 USD | 4,830,000.00 USD | 78,970.00 USD | 40,280.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 7,090,000.00 USD | 7,090,000.00 USD | 294,830.00 USD | 109,510.00 USD | 187,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 5,020,000.00 USD | 5,020,000.00 USD | 84,580.00 USD | 59,300.00 USD | 48,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 7,420,000.00 USD | 7,420,000.00 USD | 190,160.00 USD | 84,780.00 USD | 49,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 5,190,000.00 USD | 5,190,000.00 USD | 45,420.00 USD | 29,560.00 USD | 90,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 7,640,000.00 USD | 7,640,000.00 USD | 52,050.00 USD | 78,710.00 USD | 94,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.85` | 469.76 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.90` | 5,320,000.00 USD | 5,320,000.00 USD | 71,970.00 USD | 25,460.00 USD | 33,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 7,950,000.00 USD | 7,950,000.00 USD | 139,720.00 USD | 61,040.00 USD | 110,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.00` | 5,420,000.00 USD | 5,420,000.00 USD | 55,630.00 USD | 10,730.00 USD | 32,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 8,120,000.00 USD | 8,120,000.00 USD | 114,840.00 USD | 48,220.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 5,420,000.00 USD | 5,420,000.00 USD | 5,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 8,150,000.00 USD | 8,150,000.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 1,180.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 5,560,000.00 USD | 5,560,000.00 USD | 100,130.00 USD | 6,410.00 USD | 31,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 8,380,000.00 USD | 8,380,000.00 USD | 116,610.00 USD | 74,350.00 USD | 33,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 5,580,000.00 USD | 5,580,000.00 USD | 13,840.00 USD | 6,960.00 USD | 2,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 8,520,000.00 USD | 8,520,000.00 USD | 51,890.00 USD | 36,170.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 5,620,000.00 USD | 5,620,000.00 USD | 23,410.00 USD | 8,360.00 USD | 2,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 8,670,000.00 USD | 8,670,000.00 USD | 87,050.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.45` | 267.31 USD | 2,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.50` | 5,690,000.00 USD | 5,690,000.00 USD | 20,390.00 USD | 23,040.00 USD | 26,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 8,770,000.00 USD | 8,770,000.00 USD | 22,140.00 USD | 34,770.00 USD | 35,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 5,750,000.00 USD | 5,750,000.00 USD | 25,020.00 USD | 13,550.00 USD | 26,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 9,020,000.00 USD | 9,020,000.00 USD | 56,380.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 5,880,000.00 USD | 5,880,000.00 USD | 72,570.00 USD | 13,270.00 USD | 39,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 9,250,000.00 USD | 9,250,000.00 USD | 100,140.00 USD | 15,950.00 USD | 114,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 5,910,000.00 USD | 5,910,000.00 USD | 22,930.00 USD | 8,420.00 USD | 1,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 9,590,000.00 USD | 9,590,000.00 USD | 182,940.00 USD | 68,030.00 USD | 92,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 5,980,000.00 USD | 5,980,000.00 USD | 36,240.00 USD | 11,940.00 USD | 16,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 9,750,000.00 USD | 9,750,000.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 6,010,000.00 USD | 6,010,000.00 USD | 22,240.00 USD | 1,560.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 9,870,000.00 USD | 9,870,000.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 6,030,000.00 USD | 6,030,000.00 USD | 11,870.00 USD | 945.47 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 9,930,000.00 USD | 9,930,000.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 6,030,000.00 USD | 6,030,000.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 10,040,000.00 USD | 10,040,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 6,030,000.00 USD | 6,030,000.00 USD | 1,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 10,190,000.00 USD | 10,190,000.00 USD | 38,690.00 USD | 23,450.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.35` | 213,600.00 USD | 216,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `62.40` | 6,040,000.00 USD | 6,040,000.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 10,330,000.00 USD | 10,330,000.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 6,040,000.00 USD | 6,040,000.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 10,420,000.00 USD | 10,420,000.00 USD | 46,040.00 USD | 14,320.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 6,040,000.00 USD | 6,040,000.00 USD | 2,090.00 USD | 0.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 10,490,000.00 USD | 10,490,000.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 6,090,000.00 USD | 6,090,000.00 USD | 18,970.00 USD | 4,920.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 10,570,000.00 USD | 10,570,000.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 6,120,000.00 USD | 6,120,000.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 10,720,000.00 USD | 10,720,000.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 6,140,000.00 USD | 6,140,000.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 10,810,000.00 USD | 10,810,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 6,150,000.00 USD | 6,150,000.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 10,880,000.00 USD | 10,880,000.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 6,170,000.00 USD | 6,170,000.00 USD | 3,990.00 USD | 4,070.00 USD | 6,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 10,920,000.00 USD | 10,920,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 6,170,000.00 USD | 6,170,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 6,180,000.00 USD | 6,180,000.00 USD | 4,440.00 USD | 594.25 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 10,960,000.00 USD | 10,960,000.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 6,190,000.00 USD | 6,190,000.00 USD | 3,520.00 USD | 1,230.00 USD | 5,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 10,980,000.00 USD | 10,980,000.00 USD | 14,300.00 USD | 1,320.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 6,230,000.00 USD | 6,230,000.00 USD | 10,280.00 USD | 18,600.00 USD | 7,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 11,010,000.00 USD | 11,010,000.00 USD | 6,620.00 USD | 15,240.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 6,280,000.00 USD | 6,280,000.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 11,100,000.00 USD | 11,100,000.00 USD | 63,480.00 USD | 17,390.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 6,340,000.00 USD | 6,340,000.00 USD | 28,040.00 USD | 5,870.00 USD | 30,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 11,170,000.00 USD | 11,170,000.00 USD | 21,940.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 6,390,000.00 USD | 6,390,000.00 USD | 23,560.00 USD | 10,410.00 USD | 14,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 11,230,000.00 USD | 11,230,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 6,450,000.00 USD | 6,450,000.00 USD | 34,020.00 USD | 12,600.00 USD | 16,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 11,260,000.00 USD | 11,260,000.00 USD | 7,650.00 USD | 12,840.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.00` | 6,480,000.00 USD | 6,480,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 11,300,000.00 USD | 11,300,000.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.10` | 6,500,000.00 USD | 6,500,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 11,340,000.00 USD | 11,340,000.00 USD | 20,350.00 USD | 667.05 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.20` | 6,520,000.00 USD | 6,520,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 11,410,000.00 USD | 11,410,000.00 USD | 44,990.00 USD | 16,820.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `64.25` | 735.02 USD | 217,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `64.40` | 6,540,000.00 USD | 6,540,000.00 USD | 1,140.00 USD | 6,300.00 USD | 13,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.40` | 11,460,000.00 USD | 11,460,000.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.50` | 6,580,000.00 USD | 6,580,000.00 USD | 17,440.00 USD | 6,670.00 USD | 9,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.50` | 11,500,000.00 USD | 11,500,000.00 USD | 8,110.00 USD | 10,390.00 USD | 20,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.60` | 6,610,000.00 USD | 6,610,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.60` | 11,560,000.00 USD | 11,560,000.00 USD | 40,220.00 USD | 18,870.00 USD | 108.50 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.70` | 6,650,000.00 USD | 6,650,000.00 USD | 29,080.00 USD | 2,430.00 USD | 6,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.70` | 11,630,000.00 USD | 11,630,000.00 USD | 39,430.00 USD | 24,700.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.80` | 6,650,000.00 USD | 6,650,000.00 USD | 3,880.00 USD | 2,200.00 USD | 731.81 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.80` | 11,670,000.00 USD | 11,670,000.00 USD | 8,140.00 USD | 8,210.00 USD | 20,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.90` | 6,660,000.00 USD | 6,660,000.00 USD | 6,320.00 USD | 1,370.00 USD | 669.73 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.90` | 11,710,000.00 USD | 11,710,000.00 USD | 25,750.00 USD | 8,010.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `65.00` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 9,480.00 USD | 13,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 218,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 252,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 252,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 253,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `69.45` | 414.62 USD | 253,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 6,740.00 USD | 260,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.75` | 5,110.00 USD | 265,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `72.35` | 660.56 USD | 266,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 274,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 275,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 275,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 275,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 294,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 295,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 298,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 299,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 299,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.55` | 2,890.00 USD | 302,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `88.05` | 3,520.00 USD | 306,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.15` | 23,790.00 USD | 330,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.65` | 1,830.00 USD | 332,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `95.05` | 649.19 USD | 332,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `95.55` | 2,390.00 USD | 335,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.55` | 1,040.00 USD | 336,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.15` | 20,630.00 USD | 356,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 20,870.00 USD | 377,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.55` | 352,750.00 USD | 730,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 730,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 731,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 4,830.00 USD | 736,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 333,510.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `113.65` | 817.14 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `114.65` | 420.77 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `115.35` | 763,270.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `12.25` | 2,930,000.00 USD | 0.00 USD | 122.50 USD | `-79.03%` | `10.00` |
| `Live` | `Long` | `12.75` | 2,930,000.00 USD | 0.00 USD | 2,560.00 USD | `-78.18%` | `200.43` |
| `Live` | `Long` | `13.05` | 2,930,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.67%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,920,000.00 USD | 0.00 USD | 150.15 USD | `-76.64%` | `11.00` |
| `Live` | `Long` | `13.95` | 2,920,000.00 USD | 0.00 USD | 446.40 USD | `-76.12%` | `32.00` |
| `Live` | `Long` | `14.45` | 2,920,000.00 USD | 0.00 USD | 4,260.00 USD | `-75.27%` | `294.67` |
| `Live` | `Long` | `15.15` | 2,920,000.00 USD | 0.00 USD | 589.64 USD | `-74.07%` | `38.92` |
| `Live` | `Long` | `15.45` | 2,920,000.00 USD | 0.00 USD | 3,010.00 USD | `-73.56%` | `195.03` |
| `Live` | `Long` | `15.65` | 2,920,000.00 USD | 0.00 USD | 1,880.00 USD | `-73.22%` | `120.00` |
| `Live` | `Long` | `17.35` | 2,910,000.00 USD | 0.00 USD | 1,040.00 USD | `-70.31%` | `60.00` |
| `Live` | `Long` | `18.95` | 2,910,000.00 USD | 0.00 USD | 5,690.00 USD | `-67.57%` | `300.00` |
| `Live` | `Long` | `19.05` | 2,910,000.00 USD | 0.00 USD | 3,470.00 USD | `-67.40%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,900,000.00 USD | 0.00 USD | 2,010.00 USD | `-66.71%` | `103.47` |
| `Live` | `Long` | `19.95` | 2,900,000.00 USD | 0.00 USD | 4,490.00 USD | `-65.86%` | `225.00` |
| `Live` | `Long` | `20.45` | 2,900,000.00 USD | 0.00 USD | 566.67 USD | `-65.00%` | `27.71` |
| `Live` | `Long` | `21.15` | 2,900,000.00 USD | 0.00 USD | 341.15 USD | `-63.80%` | `16.13` |
| `Live` | `Long` | `21.35` | 2,900,000.00 USD | 0.00 USD | 491.90 USD | `-63.46%` | `23.04` |
| `Live` | `Long` | `21.45` | 2,900,000.00 USD | 0.00 USD | 19,950.00 USD | `-63.29%` | `930.00` |
| `Live` | `Long` | `21.55` | 2,880,000.00 USD | 0.00 USD | 127.36 USD | `-63.12%` | `5.91` |
| `Live` | `Long` | `23.75` | 2,880,000.00 USD | 0.00 USD | 194.75 USD | `-59.35%` | `8.20` |
| `Live` | `Long` | `24.05` | 2,880,000.00 USD | 0.00 USD | 421.36 USD | `-58.84%` | `17.52` |
| `Live` | `Long` | `25.25` | 2,880,000.00 USD | 0.00 USD | 277,980.00 USD | `-56.79%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,600,000.00 USD | 0.00 USD | 173.39 USD | `-56.61%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,600,000.00 USD | 0.00 USD | 51,610.00 USD | `-56.27%` | `2,019.93` |
| `Live` | `Long` | `25.95` | 2,550,000.00 USD | 0.00 USD | 374.20 USD | `-55.59%` | `14.42` |
| `Live` | `Long` | `26.25` | 2,550,000.00 USD | 0.00 USD | 205.54 USD | `-55.07%` | `7.83` |
| `Live` | `Long` | `26.95` | 2,540,000.00 USD | 0.00 USD | 5,490.00 USD | `-53.88%` | `203.85` |
| `Live` | `Long` | `27.05` | 2,540,000.00 USD | 0.00 USD | 966.50 USD | `-53.70%` | `35.73` |
| `Live` | `Long` | `27.55` | 2,540,000.00 USD | 0.00 USD | 272.75 USD | `-52.85%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,540,000.00 USD | 0.00 USD | 173.85 USD | `-52.16%` | `6.22` |
| `Live` | `Long` | `28.15` | 2,540,000.00 USD | 0.00 USD | 3,490.00 USD | `-51.82%` | `124.01` |
| `Live` | `Long` | `28.45` | 2,530,000.00 USD | 0.00 USD | 4,100.00 USD | `-51.31%` | `144.17` |
| `Live` | `Long` | `28.55` | 2,530,000.00 USD | 0.00 USD | 2,270.00 USD | `-51.14%` | `79.49` |
| `Live` | `Long` | `29.15` | 2,530,000.00 USD | 0.00 USD | 583.00 USD | `-50.11%` | `20.00` |
| `Live` | `Long` | `29.55` | 2,530,000.00 USD | 0.00 USD | 108.74 USD | `-49.43%` | `3.68` |
| `Live` | `Long` | `29.65` | 2,530,000.00 USD | 0.00 USD | 3,870.00 USD | `-49.25%` | `130.63` |
| `Live` | `Long` | `29.75` | 2,520,000.00 USD | 0.00 USD | 298,340.00 USD | `-49.08%` | `10,028.37` |
| `Live` | `Long` | `30.05` | 2,230,000.00 USD | 0.00 USD | 218.46 USD | `-48.57%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,230,000.00 USD | 0.00 USD | 305.50 USD | `-47.71%` | `10.00` |
| `Live` | `Long` | `30.95` | 2,220,000.00 USD | 0.00 USD | 538.53 USD | `-47.03%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,220,000.00 USD | 0.00 USD | 27,620.00 USD | `-46.69%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,200,000.00 USD | 0.00 USD | 5,680.00 USD | `-46.00%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,190,000.00 USD | 0.00 USD | 7,070.00 USD | `-45.49%` | `221.94` |
| `Live` | `Long` | `31.95` | 2,180,000.00 USD | 0.00 USD | 125.24 USD | `-45.32%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,180,000.00 USD | 0.00 USD | 1,450.00 USD | `-44.98%` | `45.01` |
| `Live` | `Long` | `32.45` | 2,180,000.00 USD | 0.00 USD | 166.47 USD | `-44.46%` | `5.13` |
| `Live` | `Long` | `32.65` | 2,180,000.00 USD | 0.00 USD | 653.00 USD | `-44.12%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,180,000.00 USD | 0.00 USD | 953.68 USD | `-43.95%` | `29.12` |
| `Live` | `Long` | `32.85` | 2,180,000.00 USD | 0.00 USD | 32,850.00 USD | `-43.78%` | `1,000.01` |
| `Live` | `Long` | `33.15` | 2,150,000.00 USD | 0.00 USD | 5,780.00 USD | `-43.26%` | `174.22` |
| `Live` | `Long` | `33.25` | 2,140,000.00 USD | 0.00 USD | 249.38 USD | `-43.09%` | `7.50` |
| `Live` | `Long` | `33.65` | 2,140,000.00 USD | 0.00 USD | 658.87 USD | `-42.41%` | `19.58` |
| `Live` | `Long` | `34.05` | 2,140,000.00 USD | 0.00 USD | 182.85 USD | `-41.72%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,140,000.00 USD | 0.00 USD | 126.70 USD | `-41.55%` | `3.71` |
| `Live` | `Long` | `34.65` | 2,140,000.00 USD | 0.00 USD | 4,140.00 USD | `-40.70%` | `119.56` |
| `Live` | `Long` | `34.95` | 2,140,000.00 USD | 0.00 USD | 17,580.00 USD | `-40.18%` | `503.00` |
| `Live` | `Long` | `35.05` | 2,120,000.00 USD | 0.00 USD | 462.66 USD | `-40.01%` | `13.20` |
| `Live` | `Long` | `36.15` | 2,120,000.00 USD | 0.00 USD | 4,650.00 USD | `-38.13%` | `128.71` |
| `Live` | `Long` | `36.35` | 2,110,000.00 USD | 0.00 USD | 3,020.00 USD | `-37.79%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,110,000.00 USD | 0.00 USD | 423.18 USD | `-37.62%` | `11.61` |
| `Live` | `Long` | `36.65` | 2,110,000.00 USD | 0.00 USD | 8,060.00 USD | `-37.27%` | `220.00` |
| `Live` | `Long` | `36.75` | 2,100,000.00 USD | 0.00 USD | 101.80 USD | `-37.10%` | `2.77` |
| `Live` | `Long` | `36.95` | 2,100,000.00 USD | 0.00 USD | 608.57 USD | `-36.76%` | `16.47` |
| `Live` | `Long` | `37.05` | 2,100,000.00 USD | 0.00 USD | 359.76 USD | `-36.59%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,100,000.00 USD | 0.00 USD | 438.74 USD | `-36.42%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,100,000.00 USD | 0.00 USD | 9,260.00 USD | `-36.08%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,090,000.00 USD | 0.00 USD | 3,530.00 USD | `-35.73%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,090,000.00 USD | 0.00 USD | 976.97 USD | `-35.39%` | `25.88` |
| `Live` | `Long` | `37.85` | 2,090,000.00 USD | 0.00 USD | 6,210.00 USD | `-35.22%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,080,000.00 USD | 0.00 USD | 446.67 USD | `-35.05%` | `11.77` |
| `Live` | `Long` | `38.05` | 2,080,000.00 USD | 0.00 USD | 7,570.00 USD | `-34.88%` | `198.87` |
| `Live` | `Long` | `38.35` | 2,070,000.00 USD | 0.00 USD | 341.70 USD | `-34.36%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,070,000.00 USD | 0.00 USD | 287.61 USD | `-34.19%` | `7.48` |
| `Live` | `Long` | `38.55` | 2,070,000.00 USD | 0.00 USD | 4,880.00 USD | `-34.02%` | `126.57` |
| `Live` | `Long` | `38.65` | 2,070,000.00 USD | 0.00 USD | 384.57 USD | `-33.85%` | `9.95` |
| `Live` | `Long` | `38.75` | 2,070,000.00 USD | 0.00 USD | 148.80 USD | `-33.68%` | `3.84` |
| `Live` | `Long` | `38.95` | 2,070,000.00 USD | 0.00 USD | 4,840.00 USD | `-33.34%` | `124.26` |
| `Live` | `Long` | `39.05` | 2,060,000.00 USD | 0.00 USD | 664,760.00 USD | `-33.17%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,400,000.00 USD | 0.00 USD | 570.02 USD | `-33.00%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,400,000.00 USD | 0.00 USD | 865.53 USD | `-32.48%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,400,000.00 USD | 0.00 USD | 162.95 USD | `-32.31%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,400,000.00 USD | 0.00 USD | 6,890.00 USD | `-32.14%` | `173.66` |
| `Live` | `Long` | `39.75` | 1,390,000.00 USD | 0.00 USD | 1,550.00 USD | `-31.97%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,390,000.00 USD | 0.00 USD | 133.10 USD | `-31.80%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,390,000.00 USD | 0.00 USD | 2,160.00 USD | `-31.46%` | `53.97` |
| `Live` | `Long` | `40.15` | 1,380,000.00 USD | 0.00 USD | 33,680.00 USD | `-31.28%` | `838.92` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-30.77%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-30.60%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 274.39 USD | `-30.43%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,350,000.00 USD | 0.00 USD | 6,340.00 USD | `-30.09%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,340,000.00 USD | 0.00 USD | 509.01 USD | `-29.91%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,340,000.00 USD | 0.00 USD | 396.54 USD | `-29.74%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,340,000.00 USD | 0.00 USD | 18,010.00 USD | `-29.40%` | `436.69` |
| `Live` | `Long` | `41.45` | 1,320,000.00 USD | 0.00 USD | 644.96 USD | `-29.06%` | `15.56` |
| `Live` | `Long` | `41.65` | 1,320,000.00 USD | 0.00 USD | 416.50 USD | `-28.72%` | `10.00` |
| `Live` | `Long` | `42.05` | 1,320,000.00 USD | 0.00 USD | 3,090.00 USD | `-28.03%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,320,000.00 USD | 0.00 USD | 65,900.00 USD | `-27.86%` | `1,563.54` |
| `Live` | `Long` | `42.25` | 1,250,000.00 USD | 0.00 USD | 35,410.00 USD | `-27.69%` | `838.00` |
| `Live` | `Long` | `42.65` | 1,220,000.00 USD | 0.00 USD | 1,570.00 USD | `-27.01%` | `36.70` |
| `Live` | `Long` | `42.75` | 1,220,000.00 USD | 0.00 USD | 26,780.00 USD | `-26.83%` | `626.50` |
| `Live` | `Long` | `42.85` | 1,190,000.00 USD | 0.00 USD | 5,800.00 USD | `-26.66%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,180,000.00 USD | 0.00 USD | 7,120.00 USD | `-26.49%` | `165.73` |
| `Live` | `Long` | `43.05` | 1,180,000.00 USD | 0.00 USD | 10,250.00 USD | `-26.32%` | `238.00` |
| `Live` | `Long` | `43.15` | 1,170,000.00 USD | 0.00 USD | 120,820.00 USD | `-26.15%` | `2,800.00` |
| `Live` | `Long` | `43.25` | 1,050,000.00 USD | 0.00 USD | 312.26 USD | `-25.98%` | `7.22` |
| `Live` | `Long` | `43.35` | 1,050,000.00 USD | 0.00 USD | 5,390.00 USD | `-25.81%` | `124.24` |
| `Live` | `Long` | `43.45` | 1,040,000.00 USD | 0.00 USD | 706.06 USD | `-25.64%` | `16.25` |
| `Live` | `Long` | `43.65` | 1,040,000.00 USD | 0.00 USD | 426.02 USD | `-25.29%` | `9.76` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-24.95%` | `18.27` |
| `Live` | `Long` | `43.95` | 1,040,000.00 USD | 0.00 USD | 1,850.00 USD | `-24.78%` | `42.18` |
| `Live` | `Long` | `44.15` | 1,040,000.00 USD | 0.00 USD | 2,380.00 USD | `-24.44%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,030,000.00 USD | 0.00 USD | 12,190.00 USD | `-24.27%` | `275.59` |
| `Live` | `Long` | `44.35` | 1,020,000.00 USD | 0.00 USD | 84,440.00 USD | `-24.10%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 938,180.00 USD | 0.00 USD | 11,950.00 USD | `-23.75%` | `268.22` |
| `Live` | `Long` | `44.75` | 926,230.00 USD | 0.00 USD | 12,490.00 USD | `-23.41%` | `279.20` |
| `Live` | `Long` | `44.85` | 913,740.00 USD | 0.00 USD | 134.55 USD | `-23.24%` | `3.00` |
| `Live` | `Long` | `44.95` | 913,600.00 USD | 0.00 USD | 2,620.00 USD | `-23.07%` | `58.18` |
| `Live` | `Long` | `45.05` | 910,990.00 USD | 0.00 USD | 329.32 USD | `-22.90%` | `7.31` |
| `Live` | `Long` | `45.15` | 910,660.00 USD | 0.00 USD | 135.00 USD | `-22.73%` | `2.99` |
| `Live` | `Long` | `45.25` | 910,520.00 USD | 0.00 USD | 3,830.00 USD | `-22.56%` | `84.55` |
| `Live` | `Long` | `45.35` | 906,700.00 USD | 0.00 USD | 1,780.00 USD | `-22.38%` | `39.28` |
| `Live` | `Long` | `45.45` | 904,920.00 USD | 0.00 USD | 23,940.00 USD | `-22.21%` | `526.65` |
| `Live` | `Long` | `45.55` | 880,980.00 USD | 0.00 USD | 318.39 USD | `-22.04%` | `6.99` |
| `Live` | `Long` | `45.95` | 880,660.00 USD | 0.00 USD | 704.87 USD | `-21.36%` | `15.34` |
| `Live` | `Long` | `46.05` | 879,960.00 USD | 0.00 USD | 9,710.00 USD | `-21.19%` | `210.95` |
| `Live` | `Long` | `46.25` | 870,240.00 USD | 0.00 USD | 39,320.00 USD | `-20.84%` | `850.21` |
| `Live` | `Long` | `46.35` | 830,920.00 USD | 0.00 USD | 383.78 USD | `-20.67%` | `8.28` |
| `Live` | `Long` | `46.65` | 830,540.00 USD | 0.00 USD | 936.73 USD | `-20.16%` | `20.08` |
| `Live` | `Long` | `46.85` | 829,600.00 USD | 0.00 USD | 358.40 USD | `-19.82%` | `7.65` |
| `Live` | `Long` | `46.95` | 829,240.00 USD | 0.00 USD | 158.22 USD | `-19.65%` | `3.37` |
| `Live` | `Long` | `47.15` | 829,080.00 USD | 0.00 USD | 49,130.00 USD | `-19.30%` | `1,042.07` |
| `Live` | `Long` | `47.25` | 779,950.00 USD | 0.00 USD | 574.09 USD | `-19.13%` | `12.15` |
| `Live` | `Long` | `47.35` | 779,380.00 USD | 0.00 USD | 2,600.00 USD | `-18.96%` | `55.00` |
| `Live` | `Long` | `47.45` | 776,770.00 USD | 0.00 USD | 2,180.00 USD | `-18.79%` | `45.94` |
| `Live` | `Long` | `47.55` | 774,590.00 USD | 0.00 USD | 1,770.00 USD | `-18.62%` | `37.28` |
| `Live` | `Long` | `47.65` | 772,820.00 USD | 0.00 USD | 6,850.00 USD | `-18.45%` | `143.81` |
| `Live` | `Long` | `47.75` | 765,970.00 USD | 0.00 USD | 4,780.00 USD | `-18.28%` | `100.00` |
| `Live` | `Long` | `47.85` | 761,190.00 USD | 0.00 USD | 975.66 USD | `-18.11%` | `20.39` |
| `Live` | `Long` | `47.95` | 760,220.00 USD | 0.00 USD | 1,440.00 USD | `-17.93%` | `30.00` |
| `Live` | `Long` | `48.05` | 758,780.00 USD | 0.00 USD | 1,860.00 USD | `-17.76%` | `38.61` |
| `Live` | `Long` | `48.15` | 756,920.00 USD | 0.00 USD | 2,680.00 USD | `-17.59%` | `55.56` |
| `Live` | `Long` | `48.25` | 754,250.00 USD | 0.00 USD | 4,390.00 USD | `-17.42%` | `90.89` |
| `Live` | `Long` | `48.55` | 749,860.00 USD | 0.00 USD | 2,030.00 USD | `-16.91%` | `41.85` |
| `Live` | `Long` | `48.65` | 747,830.00 USD | 0.00 USD | 273.90 USD | `-16.74%` | `5.63` |
| `Live` | `Long` | `48.75` | 747,560.00 USD | 0.00 USD | 231.56 USD | `-16.57%` | `4.75` |
| `Live` | `Long` | `48.95` | 747,320.00 USD | 0.00 USD | 1,390.00 USD | `-16.22%` | `28.33` |
| `Live` | `Long` | `49.05` | 745,940.00 USD | 0.00 USD | 1,580.00 USD | `-16.05%` | `32.25` |
| `Live` | `Long` | `49.15` | 744,360.00 USD | 0.00 USD | 5,740.00 USD | `-15.88%` | `116.83` |
| `Live` | `Long` | `49.35` | 738,610.00 USD | 0.00 USD | 5,230.00 USD | `-15.54%` | `105.97` |
| `Live` | `Long` | `49.45` | 733,380.00 USD | 0.00 USD | 1,960.00 USD | `-15.37%` | `39.73` |
| `Live` | `Long` | `49.55` | 731,420.00 USD | 0.00 USD | 18,010.00 USD | `-15.20%` | `363.57` |
| `Live` | `Long` | `49.65` | 713,400.00 USD | 0.00 USD | 4,890.00 USD | `-15.03%` | `98.52` |
| `Live` | `Long` | `49.75` | 708,510.00 USD | 0.00 USD | 1,250.00 USD | `-14.85%` | `25.06` |
| `Live` | `Long` | `49.85` | 707,270.00 USD | 0.00 USD | 18,920.00 USD | `-14.68%` | `379.44` |
| `Live` | `Long` | `49.95` | 688,350.00 USD | 0.00 USD | 28,540.00 USD | `-14.51%` | `571.31` |
| `Live` | `Long` | `50.05` | 659,810.00 USD | 0.00 USD | 1,820.00 USD | `-14.34%` | `36.43` |
| `Live` | `Long` | `50.25` | 657,990.00 USD | 0.00 USD | 102.51 USD | `-14.00%` | `2.04` |
| `Live` | `Long` | `50.35` | 657,890.00 USD | 0.00 USD | 1,030.00 USD | `-13.83%` | `20.49` |
| `Live` | `Long` | `50.45` | 656,860.00 USD | 0.00 USD | 4,720.00 USD | `-13.66%` | `93.64` |
| `Live` | `Long` | `50.55` | 652,130.00 USD | 0.00 USD | 103,540.00 USD | `-13.48%` | `2,048.30` |
| `Live` | `Long` | `50.65` | 548,590.00 USD | 0.00 USD | 25,330.00 USD | `-13.31%` | `500.00` |
| `Live` | `Long` | `50.75` | 523,270.00 USD | 0.00 USD | 9,050.00 USD | `-13.14%` | `178.28` |
| `Live` | `Long` | `50.95` | 514,220.00 USD | 0.00 USD | 245.07 USD | `-12.80%` | `4.81` |
| `Live` | `Long` | `51.05` | 513,970.00 USD | 0.00 USD | 550.32 USD | `-12.63%` | `10.78` |
| `Live` | `Long` | `51.15` | 513,420.00 USD | 0.00 USD | 219,370.00 USD | `-12.46%` | `4,288.79` |
| `Live` | `Long` | `51.45` | 294,050.00 USD | 0.00 USD | 22,090.00 USD | `-11.94%` | `429.37` |
| `Live` | `Long` | `51.55` | 271,960.00 USD | 0.00 USD | 551.07 USD | `-11.77%` | `10.69` |
| `Live` | `Long` | `51.65` | 271,410.00 USD | 0.00 USD | 155.47 USD | `-11.60%` | `3.01` |
| `Live` | `Long` | `51.75` | 271,250.00 USD | 0.00 USD | 6,450.00 USD | `-11.43%` | `124.64` |
| `Live` | `Long` | `51.85` | 264,800.00 USD | 0.00 USD | 3,580.00 USD | `-11.26%` | `69.10` |
| `Live` | `Long` | `51.95` | 261,220.00 USD | 0.00 USD | 12,070.00 USD | `-11.09%` | `232.41` |
| `Live` | `Long` | `52.35` | 249,150.00 USD | 0.00 USD | 1,470.00 USD | `-10.40%` | `28.09` |
| `Live` | `Long` | `52.45` | 247,680.00 USD | 0.00 USD | 3,620.00 USD | `-10.23%` | `68.95` |
| `Live` | `Long` | `52.55` | 244,060.00 USD | 0.00 USD | 8,700.00 USD | `-10.06%` | `165.49` |
| `Live` | `Long` | `52.75` | 235,360.00 USD | 0.00 USD | 7,450.00 USD | `-9.72%` | `141.16` |
| `Live` | `Long` | `52.85` | 227,920.00 USD | 0.00 USD | 5,950.00 USD | `-9.55%` | `112.64` |
| `Live` | `Long` | `52.95` | 221,960.00 USD | 0.00 USD | 11,500.00 USD | `-9.38%` | `217.16` |
| `Live` | `Long` | `53.05` | 210,470.00 USD | 0.00 USD | 900.26 USD | `-9.21%` | `16.97` |
| `Live` | `Long` | `53.15` | 209,570.00 USD | 0.00 USD | 23,340.00 USD | `-9.03%` | `439.12` |
| `Live` | `Long` | `53.25` | 186,230.00 USD | 0.00 USD | 1,500.00 USD | `-8.86%` | `28.15` |
| `Live` | `Long` | `53.35` | 184,730.00 USD | 0.00 USD | 1,910.00 USD | `-8.69%` | `35.71` |
| `Live` | `Long` | `53.45` | 182,820.00 USD | 0.00 USD | 4,880.00 USD | `-8.52%` | `91.21` |
| `Live` | `Long` | `53.65` | 177,950.00 USD | 0.00 USD | 533.82 USD | `-8.18%` | `9.95` |
| `Live` | `Long` | `53.75` | 177,410.00 USD | 0.00 USD | 148.35 USD | `-8.01%` | `2.76` |
| `Live` | `Long` | `53.85` | 177,270.00 USD | 0.00 USD | 2,130.00 USD | `-7.84%` | `39.58` |
| `Live` | `Long` | `53.95` | 175,130.00 USD | 0.00 USD | 28,950.00 USD | `-7.67%` | `536.62` |
| `Live` | `Long` | `54.05` | 146,180.00 USD | 0.00 USD | 19,340.00 USD | `-7.49%` | `357.82` |
| `Live` | `Long` | `54.15` | 126,840.00 USD | 0.00 USD | 13,030.00 USD | `-7.32%` | `240.54` |
| `Live` | `Long` | `54.25` | 113,820.00 USD | 0.00 USD | 3,260.00 USD | `-7.15%` | `60.01` |
| `Live` | `Long` | `54.45` | 110,560.00 USD | 0.00 USD | 14,120.00 USD | `-6.81%` | `259.32` |
| `Live` | `Long` | `54.55` | 96,440.00 USD | 0.00 USD | 1,060.00 USD | `-6.64%` | `19.49` |
| `Live` | `Long` | `54.65` | 95,380.00 USD | 0.00 USD | 488.57 USD | `-6.47%` | `8.94` |
| `Live` | `Long` | `54.75` | 94,890.00 USD | 0.00 USD | 470.85 USD | `-6.30%` | `8.60` |
| `Live` | `Long` | `54.95` | 94,420.00 USD | 0.00 USD | 7,160.00 USD | `-5.95%` | `130.33` |
| `Live` | `Long` | `55.05` | 87,260.00 USD | 0.00 USD | 1,100.00 USD | `-5.78%` | `19.96` |
| `Live` | `Long` | `55.15` | 86,160.00 USD | 0.00 USD | 3,010.00 USD | `-5.61%` | `54.52` |
| `Live` | `Long` | `55.35` | 83,150.00 USD | 0.00 USD | 1,610.00 USD | `-5.27%` | `29.05` |
| `Live` | `Long` | `55.45` | 81,540.00 USD | 0.00 USD | 1,090.00 USD | `-5.10%` | `19.70` |
| `Live` | `Long` | `55.55` | 80,450.00 USD | 0.00 USD | 1,390.00 USD | `-4.93%` | `25.05` |
| `Live` | `Long` | `55.65` | 79,060.00 USD | 0.00 USD | 676.15 USD | `-4.76%` | `12.15` |
| `Live` | `Long` | `55.75` | 78,380.00 USD | 0.00 USD | 153.87 USD | `-4.59%` | `2.76` |
| `Live` | `Long` | `56.15` | 78,230.00 USD | 0.00 USD | 78,230.00 USD | `-3.90%` | `1,393.24` |
| `Live` | `Short` | `60.75` | 1,040.00 USD | 1,040.00 USD | 0.00 USD | `+3.97%` | `17.16` |
| `Live` | `Short` | `60.85` | 1,510.00 USD | 469.76 USD | 0.00 USD | `+4.14%` | `7.72` |
| `Live` | `Short` | `61.15` | 2,690.00 USD | 1,180.00 USD | 0.00 USD | `+4.66%` | `19.27` |
| `Live` | `Short` | `61.45` | 2,960.00 USD | 267.31 USD | 0.00 USD | `+5.17%` | `4.35` |
| `Live` | `Short` | `62.35` | 216,560.00 USD | 213,600.00 USD | 0.00 USD | `+6.71%` | `3,425.89` |
| `Live` | `Short` | `64.25` | 217,300.00 USD | 735.02 USD | 0.00 USD | `+9.96%` | `11.44` |
| `Live` | `Short` | `65.95` | 218,460.00 USD | 1,160.00 USD | 0.00 USD | `+12.87%` | `17.59` |
| `Live` | `Short` | `66.85` | 252,410.00 USD | 33,950.00 USD | 0.00 USD | `+14.41%` | `507.83` |
| `Live` | `Short` | `66.95` | 252,530.00 USD | 121.18 USD | 0.00 USD | `+14.58%` | `1.81` |
| `Live` | `Short` | `67.85` | 253,240.00 USD | 709.03 USD | 0.00 USD | `+16.12%` | `10.45` |
| `Live` | `Short` | `69.45` | 253,650.00 USD | 414.62 USD | 0.00 USD | `+18.86%` | `5.97` |
| `Live` | `Short` | `70.45` | 260,390.00 USD | 6,740.00 USD | 0.00 USD | `+20.57%` | `95.63` |
| `Live` | `Short` | `71.75` | 265,490.00 USD | 5,110.00 USD | 0.00 USD | `+22.80%` | `71.15` |
| `Live` | `Short` | `72.35` | 266,150.00 USD | 660.56 USD | 0.00 USD | `+23.83%` | `9.13` |
| `Live` | `Short` | `76.35` | 274,540.00 USD | 8,380.00 USD | 0.00 USD | `+30.67%` | `109.80` |
| `Live` | `Short` | `77.85` | 275,140.00 USD | 602.56 USD | 0.00 USD | `+33.24%` | `7.74` |
| `Live` | `Short` | `77.95` | 275,280.00 USD | 136.41 USD | 0.00 USD | `+33.41%` | `1.75` |
| `Live` | `Short` | `80.75` | 275,920.00 USD | 646.00 USD | 0.00 USD | `+38.20%` | `8.00` |
| `Live` | `Short` | `81.05` | 294,920.00 USD | 19,000.00 USD | 0.00 USD | `+38.72%` | `234.42` |
| `Live` | `Short` | `81.55` | 295,050.00 USD | 123.96 USD | 0.00 USD | `+39.57%` | `1.52` |
| `Live` | `Short` | `82.65` | 298,900.00 USD | 3,850.00 USD | 0.00 USD | `+41.45%` | `46.61` |
| `Live` | `Short` | `82.75` | 299,110.00 USD | 214.32 USD | 0.00 USD | `+41.62%` | `2.59` |
| `Live` | `Short` | `84.65` | 299,970.00 USD | 862.58 USD | 0.00 USD | `+44.88%` | `10.19` |
| `Live` | `Short` | `87.55` | 302,860.00 USD | 2,890.00 USD | 0.00 USD | `+49.84%` | `33.00` |
| `Live` | `Short` | `88.05` | 306,390.00 USD | 3,520.00 USD | 0.00 USD | `+50.70%` | `40.00` |
| `Live` | `Short` | `89.15` | 330,170.00 USD | 23,790.00 USD | 0.00 USD | `+52.58%` | `266.81` |
| `Live` | `Short` | `89.65` | 332,000.00 USD | 1,830.00 USD | 0.00 USD | `+53.43%` | `20.39` |
| `Live` | `Short` | `95.05` | 332,650.00 USD | 649.19 USD | 0.00 USD | `+62.68%` | `6.83` |
| `Live` | `Short` | `95.55` | 335,040.00 USD | 2,390.00 USD | 0.00 USD | `+63.53%` | `25.00` |
| `Live` | `Short` | `97.55` | 336,070.00 USD | 1,040.00 USD | 0.00 USD | `+66.95%` | `10.63` |
| `Live` | `Short` | `103.15` | 356,700.00 USD | 20,630.00 USD | 0.00 USD | `+76.54%` | `200.00` |
| `Live` | `Short` | `104.35` | 377,570.00 USD | 20,870.00 USD | 0.00 USD | `+78.59%` | `200.00` |
| `Live` | `Short` | `104.55` | 730,330.00 USD | 352,750.00 USD | 0.00 USD | `+78.94%` | `3,374.01` |
| `Live` | `Short` | `110.45` | 730,460.00 USD | 131.44 USD | 0.00 USD | `+89.03%` | `1.19` |
| `Live` | `Short` | `110.55` | 731,580.00 USD | 1,120.00 USD | 0.00 USD | `+89.20%` | `10.11` |
| `Live` | `Short` | `110.65` | 736,410.00 USD | 4,830.00 USD | 0.00 USD | `+89.38%` | `43.66` |
| `Live` | `Short` | `110.95` | 1,070,000.00 USD | 333,510.00 USD | 0.00 USD | `+89.89%` | `3,005.99` |
| `Live` | `Short` | `113.65` | 1,070,000.00 USD | 817.14 USD | 0.00 USD | `+94.51%` | `7.19` |
| `Live` | `Short` | `114.65` | 1,070,000.00 USD | 420.77 USD | 0.00 USD | `+96.22%` | `3.67` |
| `Live` | `Short` | `115.35` | 1,830,000.00 USD | 763,270.00 USD | 0.00 USD | `+97.42%` | `6,617.03` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 525,300.00 USD | 0.00 USD | 392.18 USD | `-65.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 524,900.00 USD | 0.00 USD | 2,310.00 USD | `-62.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 522,600.00 USD | 0.00 USD | 122.24 USD | `-57.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 522,470.00 USD | 0.00 USD | 1,560.00 USD | `-56.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 520,920.00 USD | 0.00 USD | 410.25 USD | `-53.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 520,510.00 USD | 0.00 USD | 281.57 USD | `-48.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 520,230.00 USD | 0.00 USD | 36,050.00 USD | `-38.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 484,180.00 USD | 0.00 USD | 37,550.00 USD | `-35.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 446,630.00 USD | 0.00 USD | 447.01 USD | `-35.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 446,180.00 USD | 0.00 USD | 40,560.00 USD | `-33.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 405,620.00 USD | 0.00 USD | 489.57 USD | `-32.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 405,130.00 USD | 0.00 USD | 1,550.00 USD | `-31.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 403,580.00 USD | 0.00 USD | 9,500.00 USD | `-31.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 394,080.00 USD | 0.00 USD | 2,060.00 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 392,020.00 USD | 0.00 USD | 2,960.00 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 389,060.00 USD | 0.00 USD | 6,050.00 USD | `-28.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 383,010.00 USD | 0.00 USD | 5,680.00 USD | `-26.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 377,330.00 USD | 0.00 USD | 672.22 USD | `-24.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 376,660.00 USD | 0.00 USD | 213.80 USD | `-23.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 376,450.00 USD | 0.00 USD | 223.20 USD | `-23.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 376,220.00 USD | 0.00 USD | 391.13 USD | `-23.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 375,830.00 USD | 0.00 USD | 7,080.00 USD | `-22.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 368,750.00 USD | 0.00 USD | 1,370.00 USD | `-22.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 367,390.00 USD | 0.00 USD | 553.80 USD | `-21.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 366,830.00 USD | 0.00 USD | 14,000.00 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 352,840.00 USD | 0.00 USD | 158.56 USD | `-19.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 352,680.00 USD | 0.00 USD | 373.28 USD | `-19.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 352,310.00 USD | 0.00 USD | 849.46 USD | `-18.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 351,460.00 USD | 0.00 USD | 1,150.00 USD | `-17.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 350,310.00 USD | 0.00 USD | 1,740.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 348,570.00 USD | 0.00 USD | 981.00 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 347,590.00 USD | 0.00 USD | 1,150.00 USD | `-15.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 346,440.00 USD | 0.00 USD | 298.20 USD | `-14.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 346,140.00 USD | 0.00 USD | 14,650.00 USD | `-14.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 331,490.00 USD | 0.00 USD | 6,410.00 USD | `-14.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 325,070.00 USD | 0.00 USD | 459.70 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 324,610.00 USD | 0.00 USD | 1,020.00 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 323,590.00 USD | 0.00 USD | 439.89 USD | `-12.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 323,150.00 USD | 0.00 USD | 3,700.00 USD | `-11.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.75` | 319,450.00 USD | 0.00 USD | 107.64 USD | `-11.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 319,350.00 USD | 0.00 USD | 27,730.00 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 291,620.00 USD | 0.00 USD | 51,800.00 USD | `-10.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 239,810.00 USD | 0.00 USD | 10,530.00 USD | `-9.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 229,280.00 USD | 0.00 USD | 271.13 USD | `-9.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 229,010.00 USD | 0.00 USD | 12,410.00 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 216,610.00 USD | 0.00 USD | 1,060.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 215,550.00 USD | 0.00 USD | 460.81 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 215,080.00 USD | 0.00 USD | 184.21 USD | `-8.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 214,900.00 USD | 0.00 USD | 1,370.00 USD | `-8.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 213,530.00 USD | 0.00 USD | 462.03 USD | `-7.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 213,070.00 USD | 0.00 USD | 601.58 USD | `-7.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 212,470.00 USD | 0.00 USD | 3,090.00 USD | `-7.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 209,380.00 USD | 0.00 USD | 156.53 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 209,220.00 USD | 0.00 USD | 570.09 USD | `-6.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 208,650.00 USD | 0.00 USD | 1,690.00 USD | `-6.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 206,960.00 USD | 0.00 USD | 2,210.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 204,750.00 USD | 0.00 USD | 33,280.00 USD | `-6.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 171,470.00 USD | 0.00 USD | 219.80 USD | `-5.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 171,250.00 USD | 0.00 USD | 21,090.00 USD | `-5.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 150,170.00 USD | 0.00 USD | 429.85 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 149,740.00 USD | 0.00 USD | 2,140.00 USD | `-5.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 147,600.00 USD | 0.00 USD | 113.88 USD | `-4.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 147,490.00 USD | 0.00 USD | 4,930.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 142,560.00 USD | 0.00 USD | 1,820.00 USD | `-4.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 140,740.00 USD | 0.00 USD | 196.59 USD | `-4.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 140,550.00 USD | 0.00 USD | 193.03 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 140,350.00 USD | 0.00 USD | 587.96 USD | `-4.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 139,770.00 USD | 0.00 USD | 1,070.00 USD | `-3.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.35` | 138,690.00 USD | 0.00 USD | 78,570.00 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.45` | 60,120.00 USD | 0.00 USD | 694.90 USD | `-3.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.55` | 59,430.00 USD | 0.00 USD | 2,640.00 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.65` | 56,790.00 USD | 0.00 USD | 1,230.00 USD | `-3.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.75` | 55,560.00 USD | 0.00 USD | 1,200.00 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.85` | 54,350.00 USD | 0.00 USD | 17,440.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.95` | 36,910.00 USD | 0.00 USD | 474.96 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 36,440.00 USD | 0.00 USD | 5,800.00 USD | `-2.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.15` | 30,630.00 USD | 0.00 USD | 4,030.00 USD | `-2.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.25` | 26,600.00 USD | 0.00 USD | 150.00 USD | `-2.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 26,450.00 USD | 0.00 USD | 444.46 USD | `-1.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.45` | 26,010.00 USD | 0.00 USD | 877.26 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.55` | 25,130.00 USD | 0.00 USD | 20,360.00 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.65` | 4,770.00 USD | 0.00 USD | 160.27 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.75` | 4,610.00 USD | 0.00 USD | 199.24 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.85` | 4,410.00 USD | 0.00 USD | 392.22 USD | `-0.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 4,020.00 USD | 0.00 USD | 128.65 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.05` | 3,890.00 USD | 0.00 USD | 1,980.00 USD | `-0.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.15` | 1,910.00 USD | 0.00 USD | 706.52 USD | `-0.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.25` | 1,210.00 USD | 0.00 USD | 1,080.00 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `58.35` | 123.70 USD | 0.00 USD | 123.70 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 101.12 USD | 101.12 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 201.82 USD | 100.71 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 476.31 USD | 274.48 USD | 0.00 USD | `+0.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 600.86 USD | 124.55 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 3,540.00 USD | 2,940.00 USD | 0.00 USD | `+0.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 8,640.00 USD | 5,100.00 USD | 0.00 USD | `+0.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 13,440.00 USD | 4,800.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 14,720.00 USD | 1,280.00 USD | 0.00 USD | `+1.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 15,180.00 USD | 461.74 USD | 0.00 USD | `+1.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 15,380.00 USD | 200.35 USD | 0.00 USD | `+1.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 15,880.00 USD | 496.65 USD | 0.00 USD | `+1.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 16,600.00 USD | 724.75 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 16,720.00 USD | 113.53 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 17,140.00 USD | 418.35 USD | 0.00 USD | `+2.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 32,500.00 USD | 15,360.00 USD | 0.00 USD | `+2.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 33,130.00 USD | 627.52 USD | 0.00 USD | `+2.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.15` | 34,930.00 USD | 1,800.00 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 35,480.00 USD | 551.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 319,590.00 USD | 284,100.00 USD | 0.00 USD | `+3.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 320,050.00 USD | 463.21 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 320,850.00 USD | 795.12 USD | 0.00 USD | `+3.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 321,250.00 USD | 407.63 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 322,450.00 USD | 1,190.00 USD | 0.00 USD | `+4.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 323,330.00 USD | 882.56 USD | 0.00 USD | `+4.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 325,690.00 USD | 2,360.00 USD | 0.00 USD | `+4.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 325,820.00 USD | 125.56 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 326,050.00 USD | 236.20 USD | 0.00 USD | `+5.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 329,650.00 USD | 3,600.00 USD | 0.00 USD | `+5.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 330,290.00 USD | 643.20 USD | 0.00 USD | `+5.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 332,410.00 USD | 2,120.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 332,520.00 USD | 106.11 USD | 0.00 USD | `+6.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 332,640.00 USD | 117.03 USD | 0.00 USD | `+6.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 333,120.00 USD | 483.21 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 333,340.00 USD | 217.95 USD | 0.00 USD | `+6.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 333,680.00 USD | 347.15 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 334,400.00 USD | 716.72 USD | 0.00 USD | `+7.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 334,540.00 USD | 141.19 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 335,880.00 USD | 1,340.00 USD | 0.00 USD | `+7.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 336,780.00 USD | 900.52 USD | 0.00 USD | `+8.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 337,490.00 USD | 703.97 USD | 0.00 USD | `+8.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 337,630.00 USD | 140.64 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 338,300.00 USD | 668.13 USD | 0.00 USD | `+8.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 342,850.00 USD | 4,550.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 343,400.00 USD | 555.03 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 343,930.00 USD | 531.62 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 344,140.00 USD | 202.69 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 344,430.00 USD | 298.04 USD | 0.00 USD | `+10.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 344,540.00 USD | 102.13 USD | 0.00 USD | `+11.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 345,080.00 USD | 540.09 USD | 0.00 USD | `+11.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 345,180.00 USD | 100.79 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 345,440.00 USD | 262.20 USD | 0.00 USD | `+12.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 345,760.00 USD | 315.12 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 346,130.00 USD | 371.49 USD | 0.00 USD | `+12.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 347,010.00 USD | 881.07 USD | 0.00 USD | `+12.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 347,830.00 USD | 825.63 USD | 0.00 USD | `+13.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 348,370.00 USD | 534.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 359,450.00 USD | 11,080.00 USD | 0.00 USD | `+14.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 372,860.00 USD | 13,410.00 USD | 0.00 USD | `+14.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 377,720.00 USD | 4,860.00 USD | 0.00 USD | `+16.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 377,920.00 USD | 204.48 USD | 0.00 USD | `+19.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 378,850.00 USD | 929.64 USD | 0.00 USD | `+19.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 698,750.00 USD | 319,890.00 USD | 0.00 USD | `+19.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 698,920.00 USD | 170.04 USD | 0.00 USD | `+21.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 704,680.00 USD | 5,770.00 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 705,240.00 USD | 555.61 USD | 0.00 USD | `+21.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 706,390.00 USD | 1,150.00 USD | 0.00 USD | `+23.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 709,100.00 USD | 2,700.00 USD | 0.00 USD | `+23.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 709,250.00 USD | 156.78 USD | 0.00 USD | `+23.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 712,480.00 USD | 3,220.00 USD | 0.00 USD | `+24.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 712,890.00 USD | 411.14 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 836,080.00 USD | 123,190.00 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 837,090.00 USD | 1,020.00 USD | 0.00 USD | `+27.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 837,200.00 USD | 104.93 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 837,590.00 USD | 392.51 USD | 0.00 USD | `+28.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 837,990.00 USD | 402.59 USD | 0.00 USD | `+28.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 838,310.00 USD | 315.18 USD | 0.00 USD | `+32.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 897,620.00 USD | 59,310.00 USD | 0.00 USD | `+34.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 900,780.00 USD | 3,160.00 USD | 0.00 USD | `+35.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 906,470.00 USD | 5,690.00 USD | 0.00 USD | `+36.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 944,090.00 USD | 37,620.00 USD | 0.00 USD | `+37.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 944,520.00 USD | 433.89 USD | 0.00 USD | `+38.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 985,220.00 USD | 40,700.00 USD | 0.00 USD | `+38.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 985,380.00 USD | 164.10 USD | 0.00 USD | `+40.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 985,930.00 USD | 546.81 USD | 0.00 USD | `+41.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 988,230.00 USD | 2,300.00 USD | 0.00 USD | `+43.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,000,000.00 USD | 12,070.00 USD | 0.00 USD | `+45.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,010,000.00 USD | 12,330.00 USD | 0.00 USD | `+46.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,010,000.00 USD | 435.38 USD | 0.00 USD | `+49.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,010,000.00 USD | 1,580.00 USD | 0.00 USD | `+50.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,050,000.00 USD | 37,000.00 USD | 0.00 USD | `+50.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,050,000.00 USD | 473.21 USD | 0.00 USD | `+52.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,050,000.00 USD | 1,270.00 USD | 0.00 USD | `+52.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,060,000.00 USD | 1,630.00 USD | 0.00 USD | `+53.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,070,000.00 USD | 18,740.00 USD | 0.00 USD | `+54.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,070,000.00 USD | 481.55 USD | 0.00 USD | `+56.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,080,000.00 USD | 1,330.00 USD | 0.00 USD | `+57.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,080,000.00 USD | 188.10 USD | 0.00 USD | `+60.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,340,000.00 USD | 266,140.00 USD | 0.00 USD | `+62.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,350,000.00 USD | 3,400.00 USD | 0.00 USD | `+63.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,370,000.00 USD | 21,930.00 USD | 0.00 USD | `+64.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,370,000.00 USD | 294.15 USD | 0.00 USD | `+67.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,370,000.00 USD | 4,010.00 USD | 0.00 USD | `+71.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,370,000.00 USD | 306.15 USD | 0.00 USD | `+74.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,370,000.00 USD | 936.72 USD | 0.00 USD | `+76.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,380,000.00 USD | 2,920.00 USD | 0.00 USD | `+76.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,380,000.00 USD | 324.15 USD | 0.00 USD | `+84.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,380,000.00 USD | 123.23 USD | 0.00 USD | `+86.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,470,000.00 USD | 89,110.00 USD | 0.00 USD | `+90.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `116.35` | 1,470,000.00 USD | 696.94 USD | 0.00 USD | `+99.13%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `51.10` | 19,170,000.00 USD | 0.00 USD | 19,170,000.00 USD | 114,000.00 USD | 49,240.00 USD | 98,810.00 USD |
| `7D` | `51.20` | 18,900,000.00 USD | 0.00 USD | 18,900,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD |
| `7D` | `51.30` | 18,840,000.00 USD | 0.00 USD | 18,840,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `51.40` | 18,770,000.00 USD | 0.00 USD | 18,770,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `51.50` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `51.60` | 18,530,000.00 USD | 0.00 USD | 18,530,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `51.70` | 18,470,000.00 USD | 0.00 USD | 18,470,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `51.80` | 18,430,000.00 USD | 0.00 USD | 18,430,000.00 USD | 22,510.00 USD | 12,820.00 USD | 19,510.00 USD |
| `7D` | `51.90` | 18,370,000.00 USD | 0.00 USD | 18,370,000.00 USD | 5,870.00 USD | 15,240.00 USD | 4,760.00 USD |
| `7D` | `52.00` | 18,350,000.00 USD | 0.00 USD | 18,350,000.00 USD | 64,300.00 USD | 17,390.00 USD | 11,880.00 USD |
| `7D` | `52.10` | 18,250,000.00 USD | 0.00 USD | 18,250,000.00 USD | 24,220.00 USD | 18,810.00 USD | 21,910.00 USD |
| `7D` | `52.20` | 18,190,000.00 USD | 0.00 USD | 18,190,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 57,580.00 USD | 23,000.00 USD | 30,490.00 USD |
| `7D` | `52.30` | 18,120,000.00 USD | 0.00 USD | 18,120,000.00 USD | 14,070.00 USD | 12,840.00 USD | 8,770.00 USD |
| `1D` | `52.40` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD |
| `7D` | `52.40` | 18,090,000.00 USD | 0.00 USD | 18,090,000.00 USD | 20,580.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `52.50` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD |
| `7D` | `52.50` | 18,040,000.00 USD | 0.00 USD | 18,040,000.00 USD | 33,240.00 USD | 667.05 USD | 18,540.00 USD |
| `1D` | `52.60` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD |
| `7D` | `52.60` | 17,980,000.00 USD | 0.00 USD | 17,980,000.00 USD | 52,790.00 USD | 16,820.00 USD | 8,940.00 USD |
| `1D` | `52.70` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 18,580.00 USD | 12,960.00 USD | 23,040.00 USD |
| `7D` | `52.70` | 17,910,000.00 USD | 0.00 USD | 17,910,000.00 USD | 20,660.00 USD | 30,990.00 USD | 49,780.00 USD |
| `1D` | `52.80` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD |
| `7D` | `52.80` | 17,800,000.00 USD | 0.00 USD | 17,800,000.00 USD | 54,600.00 USD | 18,870.00 USD | 108.50 USD |
| `1D` | `52.90` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 29,080.00 USD | 2,430.00 USD | 6,120.00 USD |
| `7D` | `52.90` | 17,730,000.00 USD | 0.00 USD | 17,730,000.00 USD | 51,920.00 USD | 24,700.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 3,880.00 USD | 2,200.00 USD | 1,010.00 USD |
| `7D` | `53.00` | 17,650,000.00 USD | 0.00 USD | 17,650,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 9,600.00 USD | 2,780.00 USD | 882.41 USD |
| `7D` | `53.10` | 17,590,000.00 USD | 0.00 USD | 17,590,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 11,160.00 USD | 8,090.00 USD | 6,480.00 USD |
| `7D` | `53.20` | 17,500,000.00 USD | 0.00 USD | 17,500,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 10,170.00 USD | 4,410.00 USD | 9,870.00 USD |
| `7D` | `53.30` | 17,360,000.00 USD | 0.00 USD | 17,360,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 24,480.00 USD | 4,490.00 USD | 14,390.00 USD |
| `7D` | `53.40` | 17,250,000.00 USD | 0.00 USD | 17,250,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD |
| `1D` | `53.50` | 5,600,000.00 USD | 0.00 USD | 5,600,000.00 USD | 9,130.00 USD | 2,350.00 USD | 83.29 USD |
| `7D` | `53.50` | 17,150,000.00 USD | 0.00 USD | 17,150,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 19,360.00 USD | 5,030.00 USD | 10,180.00 USD |
| `7D` | `53.60` | 17,060,000.00 USD | 0.00 USD | 17,060,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 5,550,000.00 USD | 0.00 USD | 5,550,000.00 USD | 4,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.70` | 16,990,000.00 USD | 0.00 USD | 16,990,000.00 USD | 64,150.00 USD | 15,090.00 USD | 12,040.00 USD |
| `1D` | `53.80` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 1,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.80` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 99,150.00 USD | 48,300.00 USD | 86,270.00 USD |
| `1D` | `53.90` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 6,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.90` | 16,670,000.00 USD | 0.00 USD | 16,670,000.00 USD | 111,970.00 USD | 25,310.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 2,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.00` | 16,410,000.00 USD | 0.00 USD | 16,410,000.00 USD | 342,600.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 5,530,000.00 USD | 0.00 USD | 5,530,000.00 USD | 11,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 15,710,000.00 USD | 0.00 USD | 15,710,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 15,760.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 15,290,000.00 USD | 0.00 USD | 15,290,000.00 USD | 234,980.00 USD | 141,240.00 USD | 133,320.00 USD |
| `1D` | `54.30` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 4,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.30` | 14,790,000.00 USD | 0.00 USD | 14,790,000.00 USD | 245,850.00 USD | 89,080.00 USD | 257,030.00 USD |
| `1D` | `54.40` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.40` | 14,190,000.00 USD | 0.00 USD | 14,190,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD |
| `1D` | `54.50` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 3,070.00 USD | 126.10 USD | 0.00 USD |
| `7D` | `54.50` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 170,480.00 USD | 53,460.00 USD | 142,750.00 USD |
| `1D` | `54.60` | 5,500,000.00 USD | 0.00 USD | 5,500,000.00 USD | 3,300.00 USD | 601.45 USD | 944.92 USD |
| `7D` | `54.60` | 13,290,000.00 USD | 0.00 USD | 13,290,000.00 USD | 108,280.00 USD | 43,430.00 USD | 73,330.00 USD |
| `1D` | `54.70` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 51,940.00 USD | 15,810.00 USD | 52,670.00 USD |
| `7D` | `54.70` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 123,820.00 USD | 50,560.00 USD | 172,060.00 USD |
| `1D` | `54.80` | 5,370,000.00 USD | 0.00 USD | 5,370,000.00 USD | 47,390.00 USD | 18,410.00 USD | 26,940.00 USD |
| `7D` | `54.80` | 12,720,000.00 USD | 0.00 USD | 12,720,000.00 USD | 309,200.00 USD | 104,820.00 USD | 156,690.00 USD |
| `1D` | `54.90` | 5,280,000.00 USD | 0.00 USD | 5,280,000.00 USD | 53,720.00 USD | 21,230.00 USD | 5,570.00 USD |
| `7D` | `54.90` | 12,150,000.00 USD | 0.00 USD | 12,150,000.00 USD | 257,210.00 USD | 162,220.00 USD | 276,830.00 USD |
| `1D` | `55.00` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 38,520.00 USD | 24,110.00 USD | 12,080.00 USD |
| `7D` | `55.00` | 11,460,000.00 USD | 0.00 USD | 11,460,000.00 USD | 266,790.00 USD | 81,220.00 USD | 310,900.00 USD |
| `1D` | `55.10` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 26,400.00 USD | 10,460.00 USD | 18,380.00 USD |
| `7D` | `55.10` | 10,800,000.00 USD | 0.00 USD | 10,800,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD |
| `1D` | `55.20` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 19,810.00 USD | 4,030.00 USD | 10,700.00 USD |
| `7D` | `55.20` | 10,120,000.00 USD | 0.00 USD | 10,120,000.00 USD | 338,950.00 USD | 177,110.00 USD | 279,820.00 USD |
| `1D` | `55.30` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 11,840.00 USD | 5,120.00 USD | 12,690.00 USD |
| `7D` | `55.30` | 9,320,000.00 USD | 0.00 USD | 9,320,000.00 USD | 367,680.00 USD | 68,970.00 USD | 256,220.00 USD |
| `1D` | `55.40` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 29,970.00 USD | 51,060.00 USD | 19,910.00 USD |
| `7D` | `55.40` | 8,630,000.00 USD | 0.00 USD | 8,630,000.00 USD | 302,780.00 USD | 187,160.00 USD | 237,150.00 USD |
| `1D` | `55.50` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 71,580.00 USD | 25,990.00 USD | 61,320.00 USD |
| `7D` | `55.50` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 329,130.00 USD | 178,270.00 USD | 529,720.00 USD |
| `1D` | `55.60` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 97,100.00 USD | 20,900.00 USD | 82,110.00 USD |
| `7D` | `55.60` | 6,860,000.00 USD | 0.00 USD | 6,860,000.00 USD | 426,340.00 USD | 260,600.00 USD | 243,460.00 USD |
| `1D` | `55.70` | 4,540,000.00 USD | 0.00 USD | 4,540,000.00 USD | 90,090.00 USD | 49,390.00 USD | 47,910.00 USD |
| `7D` | `55.70` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 174,240.00 USD | 32,180.00 USD | 273,340.00 USD |
| `1D` | `55.80` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 120,170.00 USD | 47,100.00 USD | 42,010.00 USD |
| `7D` | `55.80` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 60,840.00 USD | 54,060.00 USD | 143,760.00 USD |
| `1D` | `55.90` | 4,150,000.00 USD | 0.00 USD | 4,150,000.00 USD | 118,870.00 USD | 60,380.00 USD | 130,300.00 USD |
| `7D` | `55.90` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 65,400.00 USD | 94,590.00 USD | 280,140.00 USD |
| `1D` | `56.00` | 3,840,000.00 USD | 0.00 USD | 3,840,000.00 USD | 125,000.00 USD | 60,260.00 USD | 56,270.00 USD |
| `7D` | `56.00` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 181,230.00 USD | 88,840.00 USD | 107,640.00 USD |
| `1D` | `56.10` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 98,040.00 USD | 77,880.00 USD | 26,680.00 USD |
| `7D` | `56.10` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 121,920.00 USD | 133,900.00 USD | 46,880.00 USD |
| `1D` | `56.20` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 73,120.00 USD | 74,660.00 USD | 87,150.00 USD |
| `7D` | `56.20` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 104,510.00 USD | 80,130.00 USD | 205,740.00 USD |
| `1D` | `56.30` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 77,950.00 USD | 44,480.00 USD | 65,840.00 USD |
| `7D` | `56.30` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 91,850.00 USD | 140,830.00 USD | 85,420.00 USD |
| `1D` | `56.40` | 2,970,000.00 USD | 0.00 USD | 2,970,000.00 USD | 185,180.00 USD | 35,450.00 USD | 111,090.00 USD |
| `7D` | `56.40` | 3,370,000.00 USD | 0.00 USD | 3,370,000.00 USD | 215,940.00 USD | 124,050.00 USD | 139,370.00 USD |
| `1D` | `56.50` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 69,340.00 USD | 109,070.00 USD | 42,530.00 USD |
| `7D` | `56.50` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 26,520.00 USD | 98,550.00 USD | 47,880.00 USD |
| `1D` | `56.60` | 2,420,000.00 USD | 0.00 USD | 2,420,000.00 USD | 161,590.00 USD | 60,330.00 USD | 124,840.00 USD |
| `7D` | `56.60` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 363,190.00 USD | 113,010.00 USD | 128,320.00 USD |
| `1D` | `56.70` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 204,190.00 USD | 64,830.00 USD | 190,800.00 USD |
| `7D` | `56.70` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 110,940.00 USD | 104,010.00 USD | 138,660.00 USD |
| `1D` | `56.80` | 1,610,000.00 USD | 0.00 USD | 1,610,000.00 USD | 189,690.00 USD | 111,830.00 USD | 122,070.00 USD |
| `7D` | `56.80` | 1,760,000.00 USD | 0.00 USD | 1,760,000.00 USD | 153,580.00 USD | 97,670.00 USD | 262,620.00 USD |
| `1D` | `56.90` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 299,280.00 USD | 93,310.00 USD | 119,420.00 USD |
| `7D` | `56.90` | 1,240,000.00 USD | 0.00 USD | 1,240,000.00 USD | 108,440.00 USD | 65,260.00 USD | 93,440.00 USD |
| `1D` | `57.00` | 674,640.00 USD | 0.00 USD | 674,640.00 USD | 34,380.00 USD | 20,790.00 USD | 44,710.00 USD |
| `7D` | `57.00` | 975,190.00 USD | 0.00 USD | 975,190.00 USD | 50,710.00 USD | 111,790.00 USD | 91,400.00 USD |
| `1D` | `57.10` | 574,760.00 USD | 0.00 USD | 574,760.00 USD | 73,260.00 USD | 25,570.00 USD | 4,390.00 USD |
| `7D` | `57.10` | 721,290.00 USD | 0.00 USD | 721,290.00 USD | 36,580.00 USD | 14,880.00 USD | 500.18 USD |
| `1D` | `57.20` | 471,550.00 USD | 0.00 USD | 471,550.00 USD | 27,530.00 USD | 40,100.00 USD | 256.90 USD |
| `7D` | `57.20` | 669,330.00 USD | 0.00 USD | 669,330.00 USD | 21,160.00 USD | 50,300.00 USD | 3,700.00 USD |
| `1D` | `57.30` | 403,660.00 USD | 0.00 USD | 403,660.00 USD | 0.00 USD | 15,520.00 USD | 51,900.00 USD |
| `7D` | `57.30` | 594,180.00 USD | 0.00 USD | 594,180.00 USD | 22,360.00 USD | 27,320.00 USD | 45,530.00 USD |
| `1D` | `57.40` | 336,230.00 USD | 0.00 USD | 336,230.00 USD | 19,650.00 USD | 26,470.00 USD | 1,340.00 USD |
| `7D` | `57.40` | 498,970.00 USD | 0.00 USD | 498,970.00 USD | 38,520.00 USD | 30,000.00 USD | 129,940.00 USD |
| `1D` | `57.50` | 288,770.00 USD | 0.00 USD | 288,770.00 USD | 80,510.00 USD | 12,870.00 USD | 36,850.00 USD |
| `7D` | `57.50` | 300,510.00 USD | 0.00 USD | 300,510.00 USD | 76,670.00 USD | 23,070.00 USD | 68,890.00 USD |
| `1D` | `57.60` | 158,550.00 USD | 0.00 USD | 158,550.00 USD | 138,820.00 USD | 0.00 USD | 19,730.00 USD |
| `7D` | `57.60` | 131,890.00 USD | 0.00 USD | 131,890.00 USD | 70,040.00 USD | 15,090.00 USD | 26,440.00 USD |
| `7D` | `57.80` | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD |
| `1D` | `58.10` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 0.00 USD | 638.03 USD |
| `7D` | `58.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.40` | 24,790.00 USD | 24,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,150.00 USD |
| `7D` | `58.40` | 54,120.00 USD | 54,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 94,790.00 USD | 94,790.00 USD | 0.00 USD | 48,820.00 USD | 20,920.00 USD | 255.20 USD |
| `7D` | `58.50` | 78,650.00 USD | 78,650.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.70` | 102,850.00 USD | 102,850.00 USD | 0.00 USD | 0.00 USD | 8,070.00 USD | 0.00 USD |
| `7D` | `58.70` | 118,400.00 USD | 118,400.00 USD | 0.00 USD | 0.00 USD | 4,430.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 113,690.00 USD | 113,690.00 USD | 0.00 USD | 0.00 USD | 10,240.00 USD | 602.87 USD |
| `7D` | `58.80` | 127,280.00 USD | 127,280.00 USD | 0.00 USD | 0.00 USD | 3,320.00 USD | 5,560.00 USD |
| `1D` | `58.90` | 255,630.00 USD | 255,630.00 USD | 0.00 USD | 0.00 USD | 102,110.00 USD | 39,820.00 USD |
| `7D` | `58.90` | 203,260.00 USD | 203,260.00 USD | 0.00 USD | 0.00 USD | 45,070.00 USD | 30,910.00 USD |
| `1D` | `59.00` | 571,890.00 USD | 571,890.00 USD | 0.00 USD | 141,660.00 USD | 51,970.00 USD | 122,640.00 USD |
| `7D` | `59.00` | 625,220.00 USD | 625,220.00 USD | 0.00 USD | 255,180.00 USD | 48,210.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 966,070.00 USD | 966,070.00 USD | 0.00 USD | 189,650.00 USD | 40,310.00 USD | 164,220.00 USD |
| `7D` | `59.10` | 850,060.00 USD | 850,060.00 USD | 0.00 USD | 91,060.00 USD | 43,600.00 USD | 90,180.00 USD |
| `1D` | `59.20` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 149,140.00 USD | 72,500.00 USD | 95,850.00 USD |
| `7D` | `59.20` | 1,190,000.00 USD | 1,190,000.00 USD | 0.00 USD | 153,580.00 USD | 10,620.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 283,630.00 USD | 71,450.00 USD | 132,920.00 USD |
| `7D` | `59.30` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 117,760.00 USD |
| `1D` | `59.40` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 78,510.00 USD | 53,540.00 USD | 76,850.00 USD |
| `7D` | `59.40` | 1,780,000.00 USD | 1,780,000.00 USD | 0.00 USD | 103,370.00 USD | 73,620.00 USD | 137,500.00 USD |
| `1D` | `59.50` | 2,160,000.00 USD | 2,160,000.00 USD | 0.00 USD | 114,880.00 USD | 51,920.00 USD | 9,950.00 USD |
| `7D` | `59.50` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 67,060.00 USD | 59,920.00 USD | 7,680.00 USD |
| `1D` | `59.60` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 62,260.00 USD | 66,510.00 USD | 13,440.00 USD |
| `7D` | `59.60` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 363,240.00 USD | 145,550.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 20,820.00 USD | 63,340.00 USD | 94,060.00 USD |
| `7D` | `59.70` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 53,810.00 USD | 180,620.00 USD | 161,880.00 USD |
| `1D` | `59.80` | 2,700,000.00 USD | 2,700,000.00 USD | 0.00 USD | 100,280.00 USD | 51,160.00 USD | 68,860.00 USD |
| `7D` | `59.80` | 3,270,000.00 USD | 3,270,000.00 USD | 0.00 USD | 118,240.00 USD | 96,860.00 USD | 155,270.00 USD |
| `1D` | `59.90` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 113,050.00 USD | 26,580.00 USD | 78,540.00 USD |
| `7D` | `59.90` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 284,130.00 USD | 107,860.00 USD | 39,700.00 USD |
| `1D` | `60.00` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 226,310.00 USD | 63,870.00 USD | 82,690.00 USD |
| `7D` | `60.00` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 231,370.00 USD | 190,040.00 USD | 82,190.00 USD |
| `1D` | `60.10` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 98,470.00 USD | 39,900.00 USD | 66,730.00 USD |
| `7D` | `60.10` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 263,890.00 USD | 122,370.00 USD | 174,140.00 USD |
| `1D` | `60.20` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 136,940.00 USD | 37,620.00 USD | 86,520.00 USD |
| `7D` | `60.20` | 5,230,000.00 USD | 5,230,000.00 USD | 0.00 USD | 207,990.00 USD | 130,630.00 USD | 123,230.00 USD |
| `1D` | `60.30` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 113,360.00 USD | 95,210.00 USD | 101,070.00 USD |
| `7D` | `60.30` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 118,160.00 USD | 95,890.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 164,430.00 USD | 72,990.00 USD | 92,650.00 USD |
| `7D` | `60.40` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 89,500.00 USD | 126,870.00 USD | 225,740.00 USD |
| `1D` | `60.50` | 4,700,000.00 USD | 4,700,000.00 USD | 0.00 USD | 147,700.00 USD | 55,300.00 USD | 104,230.00 USD |
| `7D` | `60.50` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 160,180.00 USD | 89,260.00 USD | 207,360.00 USD |
| `1D` | `60.60` | 4,830,000.00 USD | 4,830,000.00 USD | 0.00 USD | 78,970.00 USD | 40,280.00 USD | 6,040.00 USD |
| `7D` | `60.60` | 7,090,000.00 USD | 7,090,000.00 USD | 0.00 USD | 294,830.00 USD | 109,510.00 USD | 187,110.00 USD |
| `1D` | `60.70` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 84,580.00 USD | 59,300.00 USD | 48,530.00 USD |
| `7D` | `60.70` | 7,420,000.00 USD | 7,420,000.00 USD | 0.00 USD | 190,160.00 USD | 84,780.00 USD | 49,880.00 USD |
| `1D` | `60.80` | 5,190,000.00 USD | 5,190,000.00 USD | 0.00 USD | 45,420.00 USD | 29,560.00 USD | 90,940.00 USD |
| `7D` | `60.80` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 52,050.00 USD | 78,710.00 USD | 94,850.00 USD |
| `1D` | `60.90` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 71,970.00 USD | 25,460.00 USD | 33,550.00 USD |
| `7D` | `60.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 139,720.00 USD | 61,040.00 USD | 110,810.00 USD |
| `1D` | `61.00` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 55,630.00 USD | 10,730.00 USD | 32,920.00 USD |
| `7D` | `61.00` | 8,120,000.00 USD | 8,120,000.00 USD | 0.00 USD | 114,840.00 USD | 48,220.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.10` | 8,150,000.00 USD | 8,150,000.00 USD | 0.00 USD | 31,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 100,130.00 USD | 6,410.00 USD | 31,390.00 USD |
| `7D` | `61.20` | 8,380,000.00 USD | 8,380,000.00 USD | 0.00 USD | 116,610.00 USD | 74,350.00 USD | 33,350.00 USD |
| `1D` | `61.30` | 5,580,000.00 USD | 5,580,000.00 USD | 0.00 USD | 13,840.00 USD | 6,960.00 USD | 2,700.00 USD |
| `7D` | `61.30` | 8,520,000.00 USD | 8,520,000.00 USD | 0.00 USD | 51,890.00 USD | 36,170.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 23,410.00 USD | 8,360.00 USD | 2,210.00 USD |
| `7D` | `61.40` | 8,670,000.00 USD | 8,670,000.00 USD | 0.00 USD | 87,050.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 20,390.00 USD | 23,040.00 USD | 26,580.00 USD |
| `7D` | `61.50` | 8,770,000.00 USD | 8,770,000.00 USD | 0.00 USD | 22,140.00 USD | 34,770.00 USD | 35,770.00 USD |
| `1D` | `61.60` | 5,750,000.00 USD | 5,750,000.00 USD | 0.00 USD | 25,020.00 USD | 13,550.00 USD | 26,260.00 USD |
| `7D` | `61.60` | 9,020,000.00 USD | 9,020,000.00 USD | 0.00 USD | 56,380.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 72,570.00 USD | 13,270.00 USD | 39,640.00 USD |
| `7D` | `61.70` | 9,250,000.00 USD | 9,250,000.00 USD | 0.00 USD | 100,140.00 USD | 15,950.00 USD | 114,970.00 USD |
| `1D` | `61.80` | 5,910,000.00 USD | 5,910,000.00 USD | 0.00 USD | 22,930.00 USD | 8,420.00 USD | 1,830.00 USD |
| `7D` | `61.80` | 9,590,000.00 USD | 9,590,000.00 USD | 0.00 USD | 182,940.00 USD | 68,030.00 USD | 92,510.00 USD |
| `1D` | `61.90` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 36,240.00 USD | 11,940.00 USD | 16,490.00 USD |
| `7D` | `61.90` | 9,750,000.00 USD | 9,750,000.00 USD | 0.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 22,240.00 USD | 1,560.00 USD | 13,970.00 USD |
| `7D` | `62.00` | 9,870,000.00 USD | 9,870,000.00 USD | 0.00 USD | 57,760.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 11,870.00 USD | 945.47 USD | 2,230.00 USD |
| `7D` | `62.10` | 9,930,000.00 USD | 9,930,000.00 USD | 0.00 USD | 36,500.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 4,170.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 10,040,000.00 USD | 10,040,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 1,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.30` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 38,690.00 USD | 23,450.00 USD | 85,980.00 USD |
| `1D` | `62.40` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 3,260.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.40` | 10,330,000.00 USD | 10,330,000.00 USD | 0.00 USD | 81,060.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 4,100.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.50` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 46,040.00 USD | 14,320.00 USD | 26,310.00 USD |
| `1D` | `62.60` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 2,090.00 USD | 0.00 USD | 327.72 USD |
| `7D` | `62.60` | 10,490,000.00 USD | 10,490,000.00 USD | 0.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 6,090,000.00 USD | 6,090,000.00 USD | 0.00 USD | 18,970.00 USD | 4,920.00 USD | 18,640.00 USD |
| `7D` | `62.70` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 16,330.00 USD | 7,010.00 USD | 10,780.00 USD |
| `7D` | `62.80` | 10,720,000.00 USD | 10,720,000.00 USD | 0.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 8,780.00 USD | 6,670.00 USD | 63.10 USD |
| `7D` | `62.90` | 10,810,000.00 USD | 10,810,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 6,150,000.00 USD | 6,150,000.00 USD | 0.00 USD | 7,650.00 USD | 7,040.00 USD | 4,820.00 USD |
| `7D` | `63.00` | 10,880,000.00 USD | 10,880,000.00 USD | 0.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 3,990.00 USD | 4,070.00 USD | 6,480.00 USD |
| `7D` | `63.10` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 6,170,000.00 USD | 6,170,000.00 USD | 0.00 USD | 2,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 6,180,000.00 USD | 6,180,000.00 USD | 0.00 USD | 4,440.00 USD | 594.25 USD | 2,730.00 USD |
| `7D` | `63.30` | 10,960,000.00 USD | 10,960,000.00 USD | 0.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 3,520.00 USD | 1,230.00 USD | 5,020.00 USD |
| `7D` | `63.40` | 10,980,000.00 USD | 10,980,000.00 USD | 0.00 USD | 14,300.00 USD | 1,320.00 USD | 9,790.00 USD |
| `1D` | `63.50` | 6,230,000.00 USD | 6,230,000.00 USD | 0.00 USD | 10,280.00 USD | 18,600.00 USD | 7,000.00 USD |
| `7D` | `63.50` | 11,010,000.00 USD | 11,010,000.00 USD | 0.00 USD | 6,620.00 USD | 15,240.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 6,280,000.00 USD | 6,280,000.00 USD | 0.00 USD | 23,100.00 USD | 7,230.00 USD | 21,130.00 USD |
| `7D` | `63.60` | 11,100,000.00 USD | 11,100,000.00 USD | 0.00 USD | 63,480.00 USD | 17,390.00 USD | 11,880.00 USD |
| `1D` | `63.70` | 6,340,000.00 USD | 6,340,000.00 USD | 0.00 USD | 28,040.00 USD | 5,870.00 USD | 30,810.00 USD |
| `7D` | `63.70` | 11,170,000.00 USD | 11,170,000.00 USD | 0.00 USD | 21,940.00 USD | 18,810.00 USD | 21,910.00 USD |
| `1D` | `63.80` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 23,560.00 USD | 10,410.00 USD | 14,460.00 USD |
| `7D` | `63.80` | 11,230,000.00 USD | 11,230,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 6,450,000.00 USD | 6,450,000.00 USD | 0.00 USD | 34,020.00 USD | 12,600.00 USD | 16,030.00 USD |
| `7D` | `63.90` | 11,260,000.00 USD | 11,260,000.00 USD | 0.00 USD | 7,650.00 USD | 12,840.00 USD | 8,770.00 USD |
| `1D` | `64.00` | 6,480,000.00 USD | 6,480,000.00 USD | 0.00 USD | 7,880.00 USD | 10,970.00 USD | 6,280.00 USD |
| `7D` | `64.00` | 11,300,000.00 USD | 11,300,000.00 USD | 0.00 USD | 11,390.00 USD | 11,230.00 USD | 20,050.00 USD |
| `1D` | `64.10` | 6,500,000.00 USD | 6,500,000.00 USD | 0.00 USD | 13,740.00 USD | 7,370.00 USD | 158.87 USD |
| `7D` | `64.10` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 20,350.00 USD | 667.05 USD | 18,540.00 USD |
| `1D` | `64.20` | 6,520,000.00 USD | 6,520,000.00 USD | 0.00 USD | 2,760.00 USD | 13,230.00 USD | 6,220.00 USD |
| `7D` | `64.20` | 11,410,000.00 USD | 11,410,000.00 USD | 0.00 USD | 44,990.00 USD | 16,820.00 USD | 8,940.00 USD |
| `1D` | `64.40` | 6,540,000.00 USD | 6,540,000.00 USD | 0.00 USD | 1,140.00 USD | 6,300.00 USD | 13,680.00 USD |
| `7D` | `64.40` | 11,460,000.00 USD | 11,460,000.00 USD | 0.00 USD | 2,540.00 USD | 20,590.00 USD | 29,110.00 USD |
| `1D` | `64.50` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 17,440.00 USD | 6,670.00 USD | 9,360.00 USD |
| `7D` | `64.50` | 11,500,000.00 USD | 11,500,000.00 USD | 0.00 USD | 8,110.00 USD | 10,390.00 USD | 20,670.00 USD |
| `1D` | `64.60` | 6,610,000.00 USD | 6,610,000.00 USD | 0.00 USD | 18,390.00 USD | 2,680.00 USD | 11,200.00 USD |
| `7D` | `64.60` | 11,560,000.00 USD | 11,560,000.00 USD | 0.00 USD | 40,220.00 USD | 18,870.00 USD | 108.50 USD |
| `1D` | `64.70` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 29,080.00 USD | 2,430.00 USD | 6,120.00 USD |
| `7D` | `64.70` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 39,430.00 USD | 24,700.00 USD | 3,870.00 USD |
| `1D` | `64.80` | 6,650,000.00 USD | 6,650,000.00 USD | 0.00 USD | 3,880.00 USD | 2,200.00 USD | 731.81 USD |
| `7D` | `64.80` | 11,670,000.00 USD | 11,670,000.00 USD | 0.00 USD | 8,140.00 USD | 8,210.00 USD | 20,430.00 USD |
| `1D` | `64.90` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 6,320.00 USD | 1,370.00 USD | 669.73 USD |
| `7D` | `64.90` | 11,710,000.00 USD | 11,710,000.00 USD | 0.00 USD | 25,750.00 USD | 8,010.00 USD | 9,860.00 USD |
| `7D` | `65.00` | 11,730,000.00 USD | 11,730,000.00 USD | 0.00 USD | 0.00 USD | 9,480.00 USD | 13,480.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 17:10:00 UTC - 2026-10-29 17:15:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 17:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 17:00:00 UTC - 2026-10-29 18:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 16:00:00 UTC - 2026-10-29 20:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `455.06M` | Total OI Tokens: `7,823,365.9 LTC`
  * 1h OI Change: `-1.50%` | 4h OI Change: `-0.88%` | 24h OI Change: `-3.66%`
  * Exchange Breakdown: Binance=`82.81M` | Bybit=`70.10M` | OKX=`35.14M` | Hyperliquid=`22.99M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `17.05K` | Last 24h: `36.85K` | Last 3d: `60.07K` | Last 7d: `106.71K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `43.94%` | `56.06%` | `0.78` | 3,640,000.00 USD |
| `15M` | `Binance` | `40.77%` | `59.23%` | `0.69` | 1,020,000.00 USD |
| `15M` | `OKX` | `28.01%` | `71.99%` | `0.39` | 463,170.00 USD |
| `15M` | `Bybit` | `27.88%` | `72.12%` | `0.39` | 362,090.00 USD |
| `15M` | `KuCoin` | `34.39%` | `65.61%` | `0.52` | 35,920.00 USD |
| `15M` | `Gate` | `50.84%` | `49.16%` | `1.03` | 529,610.00 USD |
| `15M` | `Bitget` | `39.2%` | `60.8%` | `0.64` | 54,190.00 USD |
| `15M` | `BingX` | `48.49%` | `51.51%` | `0.94` | 590,420.00 USD |
| `15M` | `MEXC` | `29.7%` | `70.3%` | `0.42` | 69,690.00 USD |
| `15M` | `Bitunix` | `33.23%` | `66.77%` | `0.50` | 57,520.00 USD |
| `15M` | `Hyperliquid` | `12.33%` | `87.67%` | `0.14` | 38,890.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.76%` | `50.24%` | `0.99` | 104,710.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `90.24%` | `9.76%` | `9.25` | 294,160.00 USD |
| `15M` | `HTX` | `8.5%` | `91.5%` | `0.09` | 5,080.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `2.58%` | `97.42%` | `0.03` | 11,120.00 USD |
| `15M` | `Aster` | `0.69%` | `99.31%` | `0.01` | 1,590.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `0%` | `100%` | `0.00` | 228.39 USD |
| `15M` | `Whale Positions` | `40.77%` | `59.23%` | `0.69` | 1,020,000.00 USD |
| `15M` | `Global Accounts` | `43.94%` | `56.06%` | `0.78` | 3,640,000.00 USD |
| `1H` | `LTC` | `41.73%` | `58.27%` | `0.72` | 7,620,000.00 USD |
| `1H` | `Binance` | `44.35%` | `55.65%` | `0.80` | 2,530,000.00 USD |
| `1H` | `OKX` | `31.7%` | `68.3%` | `0.46` | 859,640.00 USD |
| `1H` | `Bybit` | `50.23%` | `49.77%` | `1.01` | 556,650.00 USD |
| `1H` | `KuCoin` | `48.88%` | `51.12%` | `0.96` | 551,200.00 USD |
| `1H` | `Gate` | `42.45%` | `57.55%` | `0.74` | 205,120.00 USD |
| `1H` | `Bitget` | `43.31%` | `56.69%` | `0.76` | 277,600.00 USD |
| `1H` | `BingX` | `31.91%` | `68.09%` | `0.47` | 586,960.00 USD |
| `1H` | `MEXC` | `49.03%` | `50.97%` | `0.96` | 522,730.00 USD |
| `1H` | `Bitunix` | `37.21%` | `62.79%` | `0.59` | 197,460.00 USD |
| `1H` | `Hyperliquid` | `17.34%` | `82.66%` | `0.21` | 206,090.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.97%` | `50.03%` | `1.00` | 841,560.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `5.86%` | `94.14%` | `0.06` | 186,270.00 USD |
| `1H` | `HTX` | `73.55%` | `26.45%` | `2.78` | 21,060.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `67.79%` | `32.21%` | `2.10` | 40,850.00 USD |
| `1H` | `Aster` | `0.17%` | `99.83%` | `0.00` | 34,090.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Whale Positions` | `44.35%` | `55.65%` | `0.80` | 2,530,000.00 USD |
| `1H` | `Global Accounts` | `41.73%` | `58.27%` | `0.72` | 7,620,000.00 USD |
| `4H` | `LTC` | `46.71%` | `53.29%` | `0.88` | 36,610,000.00 USD |
| `4H` | `Binance` | `46.88%` | `53.12%` | `0.88` | 13,160,000.00 USD |
| `4H` | `OKX` | `44.65%` | `55.35%` | `0.81` | 4,190,000.00 USD |
| `4H` | `Bybit` | `49.39%` | `50.61%` | `0.98` | 2,230,000.00 USD |
| `4H` | `KuCoin` | `50.25%` | `49.75%` | `1.01` | 2,170,000.00 USD |
| `4H` | `Gate` | `54.02%` | `45.98%` | `1.17` | 1,510,000.00 USD |
| `4H` | `Bitget` | `49.59%` | `50.41%` | `0.98` | 1,270,000.00 USD |
| `4H` | `BingX` | `37.51%` | `62.49%` | `0.60` | 2,640,000.00 USD |
| `4H` | `MEXC` | `50.74%` | `49.26%` | `1.03` | 2,190,000.00 USD |
| `4H` | `Bitunix` | `52.91%` | `47.09%` | `1.12` | 1,270,000.00 USD |
| `4H` | `Hyperliquid` | `45.78%` | `54.22%` | `0.84` | 999,230.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.1%` | `49.9%` | `1.00` | 3,630,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `21.03%` | `78.97%` | `0.27` | 979,300.00 USD |
| `4H` | `HTX` | `46.82%` | `53.18%` | `0.88` | 55,470.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.49%` | `46.51%` | `1.15` | 173,490.00 USD |
| `4H` | `Aster` | `32.83%` | `67.17%` | `0.49` | 130,800.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Whale Positions` | `46.88%` | `53.12%` | `0.88` | 13,160,000.00 USD |
| `4H` | `Global Accounts` | `46.71%` | `53.29%` | `0.88` | 36,610,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `58.44` | `58.23` | `58.44` | `58.50` | `57.81` | 1,176,112.95 USD | 551,465.94 USD | 624,647.01 USD | -73,181.06 USD | `-6.22%` | `14B / 7S` |
| `5:00 UTC` | `58.28` | `58.30` | `58.28` | `58.50` | `58.16` | 781,088.89 USD | 394,741.16 USD | 386,347.73 USD | 8,393.43 USD | `+1.07%` | `2B / 7S` |
| `0:00 UTC` | `58.48` | `58.45` | `58.48` | `58.59` | `58.19` | 938,333.48 USD | 401,248.45 USD | 537,085.04 USD | -135,836.59 USD | `-14.48%` | `6B / 6S` |
| `5:00 UTC` | `58.56` | `58.55` | `58.56` | `58.69` | `58.45` | 786,561.16 USD | 351,968.92 USD | 434,592.24 USD | -82,623.32 USD | `-10.50%` | `1B / 7S` |
| `0:00 UTC` | `58.75` | `58.71` | `58.75` | `58.94` | `58.39` | 3,012,388.15 USD | 1,829,068.33 USD | 1,183,319.82 USD | 645,748.50 USD | `+21.44%` | `9B / 5S` |
| `5:00 UTC` | `58.62` | `58.67` | `58.62` | `58.89` | `58.47` | 1,800,374.76 USD | 710,155.53 USD | 1,090,219.24 USD | -380,063.71 USD | `-21.11%` | `7B / 10S` |
| `0:00 UTC` | `58.62` | `58.52` | `58.62` | `58.69` | `58.38` | 676,217.74 USD | 290,207.52 USD | 386,010.22 USD | -95,802.70 USD | `-14.17%` | `4B / 7S` |
| `5:00 UTC` | `58.47` | `58.42` | `58.47` | `58.53` | `58.31` | 694,681.39 USD | 374,631.67 USD | 320,049.71 USD | 54,581.96 USD | `+7.86%` | `5B / 5S` |
| `0:00 UTC` | `58.41` | `58.31` | `58.41` | `58.45` | `58.17` | 879,667.69 USD | 349,324.06 USD | 530,343.63 USD | -181,019.57 USD | `-20.58%` | `0B / 5S` |
| `5:00 UTC` | `58.17` | `58.18` | `58.17` | `58.25` | `58.12` | 267,923.30 USD | 146,214.06 USD | 121,709.23 USD | 24,504.83 USD | `+9.15%` | `2B / 3S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 21:10` | `Volume 50K LTC` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.75` | 0.00 USD | 0.00 USD |
| `10-28 20:58` | `Volume 50K LTC` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `58.09` | 8,700.00 USD | 0.00 USD |
| `10-28 20:51` | `Range 0.2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.55` | 0.00 USD | 0.00 USD |
| `10-28 20:34` | `Volume 50K LTC` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.96` | 0.00 USD | 0.00 USD |
| `10-28 20:31` | `Range 0.2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `58.43` | 0.00 USD | 0.00 USD |
| `10-28 20:22` | `Range 0.2` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.80` | 0.00 USD | 0.00 USD |
| `10-28 19:58` | `Range 0.2` | `Trapped longs` | **`BEARISH`** | Failed breakout | `57.47` | 6,700.00 USD | 0.00 USD |
| `10-28 19:07` | `Range 0.2` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `57.43` | 3,500.00 USD | 0.00 USD |
| `10-28 17:09` | `Range 0.2` | `Divergence` | **`BULLISH`** | Drop without taker selling | `57.66` | 0.00 USD | 0.00 USD |
| `10-28 16:32` | `Range 0.2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `57.49` | 0.00 USD | 0.00 USD |
| `10-28 14:20` | `Volume 50K LTC` | `Divergence` | **`BEARISH`** | Rally without taker buying | `57.96` | 0.00 USD | 0.00 USD |
| `10-28 11:09` | `Range 0.2` | `Divergence` | **`BEARISH`** | Rally without taker buying | `57.49` | 0.00 USD | 0.00 USD |
| `10-28 08:20` | `Range 0.2` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `57.39` | 4,900.00 USD | 0.00 USD |
| `10-28 07:52` | `Range 0.2` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `57.28` | 2,800.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -34,360.00 USD | -101,940.00 USD | **`DISTRIBUTION`** |
| `15m` | -143,860.00 USD | -514,400.00 USD | **`DISTRIBUTION`** |
| `30m` | -44,560.00 USD | -526,840.00 USD | **`DISTRIBUTION`** |
| `1h` | -34,640.00 USD | -1,440,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 447,680.00 USD | -232,890.00 USD | **`ACCUMULATION`** |
| `4h` | 1,140,000.00 USD | -248,080.00 USD | **`ACCUMULATION`** |
| `6h` | 1,610,000.00 USD | 1,860,000.00 USD | **`ACCUMULATION`** |
| `8h` | 1,980,000.00 USD | 3,420,000.00 USD | **`ACCUMULATION`** |
| `12h` | 2,240,000.00 USD | 2,190,000.00 USD | **`ACCUMULATION`** |
| `24h` | 798,560.00 USD | -3,780,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 5,340,000.00 USD | -19,840,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -21,000,000.00 USD | -188,120,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-34.36K` | 15m=`-143.86K` | 1h=`-34.64K` | 24h=`+798.56K`
* Futures Capital Netflows: 5m=`-101.94K` | 15m=`-514.40K` | 1h=`-1.44M` | 24h=`-3.78M`
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
  * `2026-10-29 22:45:14 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:06:14 IST`: [fxstreet.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [ForexFactory] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 22:50:14 IST`: [youtube.com/bankofcanadaofficial] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [notayesmanseconomics.wordpress.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-29 22:49:14 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:51:14 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 18:51:14 IST`: [dol.gov] - (Sentiment: `Neutral`)


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
  * Execution Entry: `57.46` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `56.60` (Risk Distance: `0.8571` pts)
  * +2.5R Take Profit: `59.60`
  * Mathematical Lot Sizing: **`11.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `59.18` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `60.04` (Risk Distance: `0.8571` pts)
  * +2.5R Take Profit: `57.04`
  * Mathematical Lot Sizing: **`11.66 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`58.67`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
