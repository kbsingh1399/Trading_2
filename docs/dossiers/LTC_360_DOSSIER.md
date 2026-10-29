# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-29 22:30:50 IST` (`2026-10-29 17:00:50 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `57.84` | **Live Ask Quote**: `58.14` | **Mid Price**: `57.99`
- **Spread Points**: `300.00` | **Spread BPS**: `51.73 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `57.76` | VWAP Z-Score: `-0.04` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.2691` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.89` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `59.84` | Lower -3.00σ Band: `55.69`
  * Upper +2.51σ Band: `59.50` | Lower -2.51σ Band: `56.03`
  * Upper +2.01σ Band: `59.15` | Lower -2.01σ Band: `56.37`
  * Upper +2.00σ Band: `59.14` | Lower -2.00σ Band: `56.38`
  * Upper +1.28σ Band: `58.65` | Lower -1.28σ Band: `56.88`
  * Upper +1.00σ Band: `58.45` | Lower -1.00σ Band: `57.07`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`57.77` | EMA-20=`57.64` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`57.65` (Slope: `+0.0000`) | EMA-100=`57.69`
  * Institutional Anchors: EMA-144=`57.61` | EMA-200=`57.42` (Slope: `+0.0852`) | EMA-233=`57.25`
- **Range Boundaries**: 24H High=`59.62` | 24H Low=`56.67` | Weekly High=`59.62` | Weekly Low=`55.48`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `58.27` (Distance: `-0.49%`)
  * Point of Control (POC) = `57.84` (Distance: `+0.27%`)
  * Value Area Low (VAL) = `56.74` (Distance: `+2.21%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.44` | POC=`57.22` | VAL=`56.70`
  * Prior Day Extremes: PDH=`59.62` | PDL=`56.37` | PDC=`58.69`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`57.62` | Weekly POC=`56.49` | Weekly VAL=`55.97`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`59.52` | Low=`56.73`
  * London Session (08:00-16:00 UTC): High=`58.12` | Low=`56.67`
  * New York Session (13:00-21:00 UTC): High=`58.13` | Low=`57.04`
  * Initial Balance (First Hour): IB High=`58.02` | IB Low=`57.29`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `57.76` - `58.22`
  * Optimal Trade Entry (OTE 0.705): `58.11`
  * Structural Invalidation Anchor (0.786): `58.45`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `57.94` | `58.02` | `57.88` | `58.00` | `3,133` | 181,611.88 USD | -2,359.39 USD | `-1.30%` | 639,250.24 USD | `-0.21` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `57.99` | `58.06` | `57.92` | `57.96` | `2,472` | 143,325.18 USD | 36,255.70 USD | `+25.30%` | 675,505.94 USD | `+0.44` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `57.95` | `58.06` | `57.88` | `58.05` | `1,408` | 81,613.04 USD | 2,800.32 USD | `+3.43%` | 678,306.26 USD | `-0.09` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `58.06` | `58.07` | `57.64` | `57.82` | `11,125` | 643,593.97 USD | -39,482.73 USD | `-6.13%` | 615,215.17 USD | `-0.64` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `57.82` | `58.07` | `57.78` | `57.94` | `10,598` | 613,593.73 USD | 26,394.46 USD | `+4.30%` | 641,609.63 USD | `-0.07` | **`BULLISH`** | `NEUTRAL CHOP` |
| `15m` | `57.94` | `58.06` | `57.88` | `58.05` | `7,014` | 406,550.09 USD | 36,696.63 USD | `+9.03%` | 678,306.26 USD | `+0.01` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `58.00` | `58.34` | `57.82` | `58.14` | `49,234` | 2,859,187.45 USD | 425,183.00 USD | `+14.87%` | -1,081,236.49 USD | `+1.29` | **`BULLISH`** | `DELTA ALIGNED` |
| `1h` | `58.15` | `58.34` | `57.64` | `57.94` | `42,884` | 2,487,851.85 USD | 112,159.36 USD | `+4.51%` | -969,077.13 USD | `+0.41` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `57.94` | `58.06` | `57.88` | `58.05` | `7,014` | 406,550.09 USD | 36,696.63 USD | `+9.03%` | -932,380.50 USD | `+0.18` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -2,272,672.44 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,819,863.27 USD | `+1.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.34` | `57.64` | `58.05` | `99,132` | 5,753,589.40 USD | 574,038.99 USD | `+9.98%` | -1,245,824.28 USD | `+1.26` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `59.52` | `59.83` | `58.53` | `59.20` | `214,225` | 12,692,496.60 USD | -10,637.52 USD | `-0.08%` | -540,169.90 USD | `+1.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `59.19` | `59.70` | `56.95` | `57.21` | `387,394` | 22,568,170.72 USD | -1,232,294.71 USD | `-5.46%` | -1,772,464.61 USD | `-1.28` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `57.20` | `58.23` | `56.92` | `57.04` | `229,127` | 13,178,164.26 USD | -500,207.83 USD | `-3.80%` | -2,272,672.44 USD | `+0.16` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `57.04` | `58.16` | `56.85` | `58.00` | `178,996` | 10,300,529.12 USD | 452,809.17 USD | `+4.40%` | -1,819,863.27 USD | `+1.45` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `58.00` | `58.34` | `57.64` | `58.05` | `99,132` | 5,753,589.40 USD | 574,038.99 USD | `+9.98%` | -1,245,824.28 USD | `+1.26` | **`BULLISH`** | `DELTA ALIGNED` |

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
| --- | **`57.99`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-29 19:44:05 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1072` | `0xeadc...9d55` | `LONG` | 2,114,643.41 USD | `36,463.77` | `52.78` | `57.94` | `0.000000` | 189,967.46 USD | `+8.98%` | `10X Cross` |
| `1083` | `0x9aa5...58af` | `SHORT` | 2,097,363.08 USD | `36,177.65` | `71.22` | `57.94` | `269.29` | 479,123.59 USD | `+22.84%` | `10X Cross` |
| `2032` | `0xcac1...26b3` | `SHORT` | 1,009,974.37 USD | `17,411.55` | `49.01` | `57.94` | `505.21` | -156,569.05 USD | `-15.50%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `56.77` | 5,782.02 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 5.78K USD at 56.7700 USD [API] | `2026-10-27 18:47:25` |
| `ANNOUNCEMENT` | `INFO` | `56.75` | 8,512.80 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 8.51K USD at 56.7520 USD [API] | `2026-10-27 19:07:24` |
| `ANNOUNCEMENT` | `INFO` | `56.70` | 5,103.18 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.10K USD at 56.7020 USD [API] | `2026-10-27 20:03:44` |
| `ANNOUNCEMENT` | `INFO` | `56.65` | 5,700.59 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.70K USD at 56.6490 USD [API] | `2026-10-27 20:41:45` |
| `ANNOUNCEMENT` | `INFO` | `56.60` | 9,999.84 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 10.00K USD at 56.6050 USD [API] | `2026-10-27 21:22:06` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`59.03` (Vol: 206,500.00 USD, Dist: `+1.83%`) | Long MP=`56.68` (Vol: 275,700.00 USD, Dist: `--2.22%`)
  * 48H Horizon: Short MP=`58.99` (Vol: 215,600.00 USD, Dist: `+1.76%`) | Long MP=`56.71` (Vol: 253,400.00 USD, Dist: `--2.17%`)
  * 3D Horizon: Short MP=`60.60` (Vol: 240,800.00 USD, Dist: `+4.54%`) | Long MP=`56.70` (Vol: 233,500.00 USD, Dist: `--2.20%`)
  * 7D Horizon: Short MP=`59.04` (Vol: 206,500.00 USD, Dist: `+1.84%`) | Long MP=`55.27` (Vol: 344,500.00 USD, Dist: `--4.66%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.65` | 226.13 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.65` | 2,540.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.05` | 2,200.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 2,210.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.55` | 465.60 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.75` | 885.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.15` | 3,410.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `15.95` | 620.77 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.35` | 1,960.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.55` | 467.87 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `16.65` | 3,250.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.95` | 5,580.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,470.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.35` | 344.38 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.85` | 213.26 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.55` | 133.27 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 194.75 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.05` | 421.36 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.05` | 694.14 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 23,750.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `26.95` | 6,110.00 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.45` | 546.53 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 453.35 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 8,560.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.85` | 225.90 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 583.00 USD | 2,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.25` | 3,630.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.55` | 108.74 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 298,070.00 USD | 2,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.15` | 1,020.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.35` | 121.40 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.85` | 4,030.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,620.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 5,680.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.05` | 382.04 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 4,000.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.45` | 166.47 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 5,270.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.85` | 32,850.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.85` | 286.03 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.55` | 6,020.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 17,580.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 1,080.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.45` | 265.88 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.85` | 672.19 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 423.18 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 359.76 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.65` | 4,850.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,210.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.05` | 15,940.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 341.70 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 287.61 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 5,150.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 384.57 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 4,840.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.45` | 865.53 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 162.95 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,550.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 133.10 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.35` | 154.94 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,670.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 509.01 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 396.54 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,490.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,580.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 3,090.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.35` | 243.94 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,710.00 USD | 1,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.75` | 26,780.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 8,950.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 120,820.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 1,830.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 6,050.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 2,010.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.95` | 38,450.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 274.79 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 932,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 5,470.00 USD | 931,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 926,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 921,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,620.00 USD | 921,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 329.32 USD | 919,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 135.00 USD | 918,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,580.00 USD | 918,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 1,780.00 USD | 915,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 913,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 7,820.00 USD | 889,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 11,380.00 USD | 881,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.75` | 107.97 USD | 870,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.85` | 458.50 USD | 870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 704.87 USD | 869,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 9,710.00 USD | 868,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.25` | 39,710.00 USD | 859,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 936.73 USD | 819,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 818,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 49,130.00 USD | 818,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 574.09 USD | 769,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 2,600.00 USD | 768,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,180.00 USD | 766,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 1,770.00 USD | 763,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 4,780.00 USD | 762,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.85` | 1,290.00 USD | 757,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 1,440.00 USD | 755,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 1,860.00 USD | 754,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.15` | 2,680.00 USD | 752,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.25` | 5,350.00 USD | 750,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 744,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 742,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.95` | 1,390.00 USD | 742,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 740,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 739,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 733,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.45` | 9,350.00 USD | 728,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 719,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.65` | 17,300.00 USD | 701,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.75` | 20,390.00 USD | 683,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.85` | 3,240.00 USD | 663,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.95` | 28,540.00 USD | 660,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 631,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 629,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,030.00 USD | 629,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 628,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 623,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 539,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `50.95` | 245.07 USD | 530,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.10` | 17,920,000.00 USD | 17,920,000.00 USD | 114,000.00 USD | 41,880.00 USD | 98,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 235,460.00 USD | 530,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.20` | 17,670,000.00 USD | 17,670,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 17,600,000.00 USD | 17,600,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 17,530,000.00 USD | 17,530,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 19,630.00 USD | 295,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.50` | 17,380,000.00 USD | 17,380,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 275,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.60` | 17,290,000.00 USD | 17,290,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 155.47 USD | 274,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.70` | 17,230,000.00 USD | 17,230,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,450.00 USD | 274,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `51.80` | 17,190,000.00 USD | 17,190,000.00 USD | 21,870.00 USD | 12,160.00 USD | 19,510.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 3,580.00 USD | 268,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 6,190,000.00 USD | 6,190,000.00 USD | 13,770.00 USD | 20,230.00 USD | 13,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 17,140,000.00 USD | 17,140,000.00 USD | 4,940.00 USD | 15,240.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 12,070.00 USD | 264,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 6,140,000.00 USD | 6,140,000.00 USD | 18,400.00 USD | 3,660.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 17,110,000.00 USD | 17,110,000.00 USD | 53,250.00 USD | 13,690.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.10` | 6,110,000.00 USD | 6,110,000.00 USD | 37,310.00 USD | 11,010.00 USD | 31,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 17,030,000.00 USD | 17,030,000.00 USD | 22,820.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.20` | 6,030,000.00 USD | 6,030,000.00 USD | 20,300.00 USD | 10,990.00 USD | 12,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 16,970,000.00 USD | 16,970,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 563.25 USD | 252,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 5,990,000.00 USD | 5,990,000.00 USD | 38,980.00 USD | 14,090.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 16,900,000.00 USD | 16,900,000.00 USD | 12,910.00 USD | 12,370.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 27,650.00 USD | 252,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 5,910,000.00 USD | 5,910,000.00 USD | 5,540.00 USD | 10,620.00 USD | 245.94 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 16,870,000.00 USD | 16,870,000.00 USD | 19,330.00 USD | 10,630.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 3,620.00 USD | 224,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 5,890,000.00 USD | 5,890,000.00 USD | 7,160.00 USD | 8,120.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 16,830,000.00 USD | 16,830,000.00 USD | 25,930.00 USD | 667.05 USD | 18,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 220,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 5,870,000.00 USD | 5,870,000.00 USD | 10,900.00 USD | 6,450.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 16,790,000.00 USD | 16,790,000.00 USD | 52,790.00 USD | 6,760.00 USD | 8,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `52.70` | 5,840,000.00 USD | 5,840,000.00 USD | 30,140.00 USD | 9,010.00 USD | 18,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 16,720,000.00 USD | 16,720,000.00 USD | 19,810.00 USD | 27,090.00 USD | 35,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 7,110.00 USD | 212,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 5,780,000.00 USD | 5,780,000.00 USD | 9,200.00 USD | 2,400.00 USD | 8,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 16,640,000.00 USD | 16,640,000.00 USD | 39,270.00 USD | 18,870.00 USD | 108.50 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 205,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 5,760,000.00 USD | 5,760,000.00 USD | 1,560.00 USD | 10,250.00 USD | 12,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 16,580,000.00 USD | 16,580,000.00 USD | 37,910.00 USD | 24,700.00 USD | 3,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 11,500.00 USD | 199,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 5,740,000.00 USD | 5,740,000.00 USD | 4,250.00 USD | 2,200.00 USD | 1,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 16,510,000.00 USD | 16,510,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 1,860.00 USD | 187,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 5,730,000.00 USD | 5,730,000.00 USD | 17,750.00 USD | 2,780.00 USD | 7,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 16,450,000.00 USD | 16,450,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 181.24 USD | 185,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 5,700,000.00 USD | 5,700,000.00 USD | 25,580.00 USD | 11,010.00 USD | 6,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 16,360,000.00 USD | 16,360,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 1,500.00 USD | 185,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 5,660,000.00 USD | 5,660,000.00 USD | 10,170.00 USD | 10,720.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 16,230,000.00 USD | 16,230,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.35` | 1,910.00 USD | 184,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.40` | 5,630,000.00 USD | 5,630,000.00 USD | 42,240.00 USD | 11,460.00 USD | 32,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 16,110,000.00 USD | 16,110,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 4,880.00 USD | 182,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 5,540,000.00 USD | 5,540,000.00 USD | 25,150.00 USD | 5,350.00 USD | 4,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 16,010,000.00 USD | 16,010,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 5,510,000.00 USD | 5,510,000.00 USD | 29,300.00 USD | 5,030.00 USD | 22,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 15,920,000.00 USD | 15,920,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.65` | 533.82 USD | 177,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.70` | 5,450,000.00 USD | 5,450,000.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 15,850,000.00 USD | 15,850,000.00 USD | 62,710.00 USD | 15,090.00 USD | 12,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.75` | 23,570.00 USD | 176,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.80` | 5,440,000.00 USD | 5,440,000.00 USD | 283.21 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 15,760,000.00 USD | 15,760,000.00 USD | 97,770.00 USD | 48,300.00 USD | 86,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.85` | 2,130.00 USD | 153,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.90` | 5,440,000.00 USD | 5,440,000.00 USD | 3,950.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 15,530,000.00 USD | 15,530,000.00 USD | 110,410.00 USD | 25,310.00 USD | 123,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.95` | 28,950.00 USD | 150,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.00` | 5,440,000.00 USD | 5,440,000.00 USD | 2,770.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 15,270,000.00 USD | 15,270,000.00 USD | 340,500.00 USD | 142,130.00 USD | 210,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.05` | 219.44 USD | 122,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.10` | 5,440,000.00 USD | 5,440,000.00 USD | 11,980.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 14,580,000.00 USD | 14,580,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.15` | 13,440.00 USD | 121,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.20` | 5,430,000.00 USD | 5,430,000.00 USD | 15,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 14,160,000.00 USD | 14,160,000.00 USD | 233,240.00 USD | 141,240.00 USD | 133,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.25` | 2,720.00 USD | 108,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.30` | 5,410,000.00 USD | 5,410,000.00 USD | 4,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 13,660,000.00 USD | 13,660,000.00 USD | 243,980.00 USD | 89,080.00 USD | 257,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 5,410,000.00 USD | 5,410,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 13,070,000.00 USD | 13,070,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 5,400,000.00 USD | 5,400,000.00 USD | 5,000.00 USD | 126.10 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 12,530,000.00 USD | 12,530,000.00 USD | 170,480.00 USD | 53,460.00 USD | 142,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.55` | 1,060.00 USD | 105,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.60` | 5,400,000.00 USD | 5,400,000.00 USD | 2,740.00 USD | 601.45 USD | 944.92 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 12,170,000.00 USD | 12,170,000.00 USD | 106,050.00 USD | 43,430.00 USD | 73,330.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.65` | 12,980.00 USD | 104,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.70` | 5,390,000.00 USD | 5,390,000.00 USD | 52,430.00 USD | 15,810.00 USD | 52,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 11,940,000.00 USD | 11,940,000.00 USD | 123,370.00 USD | 50,560.00 USD | 172,060.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.75` | 180.67 USD | 91,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `54.80` | 5,270,000.00 USD | 5,270,000.00 USD | 45,490.00 USD | 18,410.00 USD | 26,940.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 11,600,000.00 USD | 11,600,000.00 USD | 307,360.00 USD | 104,820.00 USD | 156,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 5,180,000.00 USD | 5,180,000.00 USD | 51,230.00 USD | 32,190.00 USD | 10,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 11,030,000.00 USD | 11,030,000.00 USD | 255,130.00 USD | 162,220.00 USD | 276,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `54.95` | 8,190.00 USD | 91,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.00` | 5,090,000.00 USD | 5,090,000.00 USD | 42,020.00 USD | 24,810.00 USD | 30,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 10,330,000.00 USD | 10,330,000.00 USD | 264,000.00 USD | 81,220.00 USD | 310,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.05` | 394.71 USD | 83,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.10` | 4,990,000.00 USD | 4,990,000.00 USD | 44,730.00 USD | 10,460.00 USD | 25,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 9,680,000.00 USD | 9,680,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.15` | 3,010.00 USD | 82,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.20` | 4,910,000.00 USD | 4,910,000.00 USD | 26,190.00 USD | 13,920.00 USD | 10,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 9,000,000.00 USD | 9,000,000.00 USD | 336,630.00 USD | 177,110.00 USD | 279,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.30` | 4,860,000.00 USD | 4,860,000.00 USD | 9,120.00 USD | 4,380.00 USD | 12,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.30` | 8,210,000.00 USD | 8,210,000.00 USD | 365,190.00 USD | 67,310.00 USD | 256,220.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `55.35` | 1,610.00 USD | 79,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `55.40` | 4,830,000.00 USD | 4,830,000.00 USD | 23,020.00 USD | 40,410.00 USD | 14,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.40` | 7,520,000.00 USD | 7,520,000.00 USD | 302,780.00 USD | 182,540.00 USD | 223,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.50` | 4,760,000.00 USD | 4,760,000.00 USD | 63,040.00 USD | 21,070.00 USD | 35,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.50` | 6,810,000.00 USD | 6,810,000.00 USD | 294,630.00 USD | 169,030.00 USD | 513,930.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.60` | 4,640,000.00 USD | 4,640,000.00 USD | 121,460.00 USD | 34,970.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.60` | 5,830,000.00 USD | 5,830,000.00 USD | 423,370.00 USD | 260,600.00 USD | 243,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.70` | 4,400,000.00 USD | 4,400,000.00 USD | 78,100.00 USD | 48,670.00 USD | 39,270.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.70` | 4,900,000.00 USD | 4,900,000.00 USD | 174,240.00 USD | 26,870.00 USD | 273,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.80` | 4,240,000.00 USD | 4,240,000.00 USD | 131,460.00 USD | 56,300.00 USD | 59,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.80` | 4,430,000.00 USD | 4,430,000.00 USD | 60,840.00 USD | 52,890.00 USD | 143,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.90` | 3,990,000.00 USD | 3,990,000.00 USD | 131,660.00 USD | 68,110.00 USD | 127,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.90` | 4,170,000.00 USD | 4,170,000.00 USD | 65,400.00 USD | 92,360.00 USD | 234,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.00` | 3,660,000.00 USD | 3,660,000.00 USD | 124,190.00 USD | 62,180.00 USD | 78,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.00` | 3,780,000.00 USD | 3,780,000.00 USD | 162,940.00 USD | 81,400.00 USD | 107,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.10` | 3,400,000.00 USD | 3,400,000.00 USD | 123,860.00 USD | 89,640.00 USD | 52,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.10` | 3,430,000.00 USD | 3,430,000.00 USD | 111,340.00 USD | 108,750.00 USD | 46,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `56.15` | 78,230.00 USD | 78,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `56.20` | 3,130,000.00 USD | 3,130,000.00 USD | 113,060.00 USD | 68,300.00 USD | 109,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.20` | 3,160,000.00 USD | 3,160,000.00 USD | 93,330.00 USD | 80,130.00 USD | 184,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.30` | 2,840,000.00 USD | 2,840,000.00 USD | 101,530.00 USD | 39,780.00 USD | 79,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.30` | 2,800,000.00 USD | 2,800,000.00 USD | 72,590.00 USD | 125,830.00 USD | 52,430.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.40` | 2,620,000.00 USD | 2,620,000.00 USD | 93,910.00 USD | 72,860.00 USD | 133,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.40` | 2,550,000.00 USD | 2,550,000.00 USD | 142,580.00 USD | 120,740.00 USD | 126,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.50` | 2,320,000.00 USD | 2,320,000.00 USD | 64,730.00 USD | 89,990.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.50` | 2,160,000.00 USD | 2,160,000.00 USD | 26,520.00 USD | 89,320.00 USD | 19,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.60` | 2,130,000.00 USD | 2,130,000.00 USD | 167,360.00 USD | 56,860.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.60` | 2,030,000.00 USD | 2,030,000.00 USD | 294,170.00 USD | 94,520.00 USD | 96,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.70` | 1,820,000.00 USD | 1,820,000.00 USD | 288,830.00 USD | 104,640.00 USD | 195,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.70` | 1,540,000.00 USD | 1,540,000.00 USD | 110,940.00 USD | 104,010.00 USD | 138,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.80` | 1,230,000.00 USD | 1,230,000.00 USD | 170,610.00 USD | 126,170.00 USD | 111,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.80` | 1,190,000.00 USD | 1,190,000.00 USD | 153,580.00 USD | 87,050.00 USD | 262,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `56.90` | 821,450.00 USD | 821,450.00 USD | 394,430.00 USD | 134,120.00 USD | 198,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `56.90` | 683,560.00 USD | 683,560.00 USD | 108,440.00 USD | 62,910.00 USD | 93,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.00` | 94,760.00 USD | 94,760.00 USD | 24,400.00 USD | 18,420.00 USD | 14,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.00` | 418,770.00 USD | 418,770.00 USD | 50,710.00 USD | 107,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.10` | 37,780.00 USD | 37,780.00 USD | 35,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.20` | 260,720.00 USD | 260,720.00 USD | 0.00 USD | 0.00 USD | 3,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.30` | 257,020.00 USD | 257,020.00 USD | 0.00 USD | 27,320.00 USD | 3,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `57.40` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | 0.00 USD | 1,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.40` | 225,990.00 USD | 225,990.00 USD | 0.00 USD | 0.00 USD | 98,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.50` | 127,360.00 USD | 127,360.00 USD | 0.00 USD | 23,070.00 USD | 68,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.60` | 35,410.00 USD | 35,410.00 USD | 0.00 USD | 15,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `57.80` | 20,310.00 USD | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 10,560.00 USD | 10,560.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 638.03 USD | 638.03 USD | 0.00 USD | 0.00 USD | 638.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 171,710.00 USD | 171,710.00 USD | 0.00 USD | 15,050.00 USD | 146,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 151,410.00 USD | 151,410.00 USD | 0.00 USD | 46,180.00 USD | 104,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 330,590.00 USD | 330,590.00 USD | 104,980.00 USD | 50,050.00 USD | 24,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 259,210.00 USD | 259,210.00 USD | 33,380.00 USD | 0.00 USD | 54,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 437,080.00 USD | 437,080.00 USD | 48,820.00 USD | 20,920.00 USD | 36,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 283,740.00 USD | 283,740.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 488,740.00 USD | 488,740.00 USD | 22,190.00 USD | 8,070.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 388,050.00 USD | 388,050.00 USD | 32,230.00 USD | 4,430.00 USD | 67,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 530,990.00 USD | 530,990.00 USD | 8,280.00 USD | 8,760.00 USD | 25,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 639,180.00 USD | 639,180.00 USD | 245,570.00 USD | 0.00 USD | 5,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.90` | 645,370.00 USD | 645,370.00 USD | 21,990.00 USD | 80,820.00 USD | 11,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 677,800.00 USD | 677,800.00 USD | 0.00 USD | 35,850.00 USD | 2,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 868,610.00 USD | 868,610.00 USD | 122,800.00 USD | 30,550.00 USD | 69,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 980,680.00 USD | 980,680.00 USD | 186,160.00 USD | 29,720.00 USD | 87,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 1,230,000.00 USD | 1,230,000.00 USD | 180,920.00 USD | 37,450.00 USD | 138,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 1,210,000.00 USD | 1,210,000.00 USD | 91,060.00 USD | 43,600.00 USD | 90,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 1,480,000.00 USD | 1,480,000.00 USD | 123,350.00 USD | 56,390.00 USD | 78,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 1,530,000.00 USD | 1,530,000.00 USD | 153,580.00 USD | 0.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 1,940,000.00 USD | 1,940,000.00 USD | 266,690.00 USD | 68,620.00 USD | 120,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 1,810,000.00 USD | 1,810,000.00 USD | 88,710.00 USD | 65,110.00 USD | 117,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.40` | 2,110,000.00 USD | 2,110,000.00 USD | 68,520.00 USD | 51,170.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 2,020,000.00 USD | 2,020,000.00 USD | 103,370.00 USD | 69,170.00 USD | 46,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 2,220,000.00 USD | 2,220,000.00 USD | 77,430.00 USD | 26,350.00 USD | 5,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 2,110,000.00 USD | 2,110,000.00 USD | 30,480.00 USD | 45,040.00 USD | 7,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 2,290,000.00 USD | 2,290,000.00 USD | 34,730.00 USD | 26,400.00 USD | 13,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 2,630,000.00 USD | 2,630,000.00 USD | 342,080.00 USD | 95,250.00 USD | 86,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 2,490,000.00 USD | 2,490,000.00 USD | 114,860.00 USD | 47,810.00 USD | 42,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 2,960,000.00 USD | 2,960,000.00 USD | 31,450.00 USD | 181,680.00 USD | 120,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 2,700,000.00 USD | 2,700,000.00 USD | 86,810.00 USD | 51,640.00 USD | 69,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 3,280,000.00 USD | 3,280,000.00 USD | 126,070.00 USD | 66,860.00 USD | 123,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 2,880,000.00 USD | 2,880,000.00 USD | 55,090.00 USD | 23,890.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 3,680,000.00 USD | 3,680,000.00 USD | 251,510.00 USD | 106,200.00 USD | 39,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 3,160,000.00 USD | 3,160,000.00 USD | 81,220.00 USD | 93,410.00 USD | 100,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 4,070,000.00 USD | 4,070,000.00 USD | 161,330.00 USD | 185,420.00 USD | 41,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 3,340,000.00 USD | 3,340,000.00 USD | 104,900.00 USD | 39,410.00 USD | 41,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 4,570,000.00 USD | 4,570,000.00 USD | 229,390.00 USD | 113,130.00 USD | 158,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.20` | 3,730,000.00 USD | 3,730,000.00 USD | 211,970.00 USD | 64,400.00 USD | 115,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 5,030,000.00 USD | 5,030,000.00 USD | 207,990.00 USD | 130,630.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 4,140,000.00 USD | 4,140,000.00 USD | 170,550.00 USD | 117,840.00 USD | 113,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 5,390,000.00 USD | 5,390,000.00 USD | 118,160.00 USD | 90,580.00 USD | 155,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.40` | 4,560,000.00 USD | 4,560,000.00 USD | 189,140.00 USD | 113,750.00 USD | 124,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 5,830,000.00 USD | 5,830,000.00 USD | 89,500.00 USD | 125,690.00 USD | 225,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 5,170,000.00 USD | 5,170,000.00 USD | 304,030.00 USD | 107,800.00 USD | 190,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 6,240,000.00 USD | 6,240,000.00 USD | 158,260.00 USD | 87,030.00 USD | 161,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.55` | 302.14 USD | 302.14 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.60` | 5,450,000.00 USD | 5,450,000.00 USD | 169,220.00 USD | 62,740.00 USD | 52,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 6,810,000.00 USD | 6,810,000.00 USD | 274,700.00 USD | 102,070.00 USD | 186,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 5,770,000.00 USD | 5,770,000.00 USD | 147,130.00 USD | 49,120.00 USD | 126,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 7,100,000.00 USD | 7,100,000.00 USD | 177,510.00 USD | 59,630.00 USD | 62,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.75` | 1,310.00 USD | 1,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.80` | 5,960,000.00 USD | 5,960,000.00 USD | 84,330.00 USD | 21,790.00 USD | 76,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 7,310,000.00 USD | 7,310,000.00 USD | 49,070.00 USD | 79,230.00 USD | 73,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.85` | 3,790.00 USD | 5,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.90` | 6,070,000.00 USD | 6,070,000.00 USD | 63,100.00 USD | 20,750.00 USD | 33,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 7,600,000.00 USD | 7,600,000.00 USD | 143,640.00 USD | 50,770.00 USD | 95,160.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 662.53 USD | 6,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 6,150,000.00 USD | 6,150,000.00 USD | 27,820.00 USD | 9,760.00 USD | 43,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 7,750,000.00 USD | 7,750,000.00 USD | 96,210.00 USD | 48,220.00 USD | 5,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 6,160,000.00 USD | 6,160,000.00 USD | 6,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 7,780,000.00 USD | 7,780,000.00 USD | 29,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.15` | 156.54 USD | 6,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.20` | 6,260,000.00 USD | 6,260,000.00 USD | 30,990.00 USD | 26,500.00 USD | 42,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 7,950,000.00 USD | 7,950,000.00 USD | 81,590.00 USD | 74,350.00 USD | 20,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 6,300,000.00 USD | 6,300,000.00 USD | 22,660.00 USD | 9,170.00 USD | 3,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 8,090,000.00 USD | 8,090,000.00 USD | 51,890.00 USD | 36,170.00 USD | 55,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 6,380,000.00 USD | 6,380,000.00 USD | 47,280.00 USD | 14,720.00 USD | 18,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 8,250,000.00 USD | 8,250,000.00 USD | 84,080.00 USD | 41,800.00 USD | 24,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 6,500,000.00 USD | 6,500,000.00 USD | 55,570.00 USD | 34,710.00 USD | 37,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 8,340,000.00 USD | 8,340,000.00 USD | 22,670.00 USD | 34,770.00 USD | 35,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.60` | 6,600,000.00 USD | 6,600,000.00 USD | 30,310.00 USD | 29,330.00 USD | 33,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.60` | 8,590,000.00 USD | 8,590,000.00 USD | 55,000.00 USD | 63,390.00 USD | 132,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.70` | 6,860,000.00 USD | 6,860,000.00 USD | 143,900.00 USD | 35,660.00 USD | 84,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 8,820,000.00 USD | 8,820,000.00 USD | 98,580.00 USD | 15,950.00 USD | 114,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.80` | 6,960,000.00 USD | 6,960,000.00 USD | 71,680.00 USD | 18,690.00 USD | 13,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 9,160,000.00 USD | 9,160,000.00 USD | 180,840.00 USD | 68,030.00 USD | 92,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.90` | 7,080,000.00 USD | 7,080,000.00 USD | 59,440.00 USD | 11,940.00 USD | 46,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 9,310,000.00 USD | 9,310,000.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.00` | 7,120,000.00 USD | 7,120,000.00 USD | 24,960.00 USD | 1,560.00 USD | 13,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 9,430,000.00 USD | 9,430,000.00 USD | 56,020.00 USD | 13,260.00 USD | 49,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.10` | 7,140,000.00 USD | 7,140,000.00 USD | 13,440.00 USD | 945.47 USD | 2,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 9,490,000.00 USD | 9,490,000.00 USD | 34,630.00 USD | 12,820.00 USD | 13,950.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.20` | 7,140,000.00 USD | 7,140,000.00 USD | 4,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 9,610,000.00 USD | 9,610,000.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.30` | 7,150,000.00 USD | 7,150,000.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 9,760,000.00 USD | 9,760,000.00 USD | 38,690.00 USD | 23,450.00 USD | 85,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.35` | 213,600.00 USD | 219,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `62.40` | 7,150,000.00 USD | 7,150,000.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 9,890,000.00 USD | 9,890,000.00 USD | 78,840.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.50` | 7,150,000.00 USD | 7,150,000.00 USD | 4,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.50` | 9,980,000.00 USD | 9,980,000.00 USD | 47,530.00 USD | 14,320.00 USD | 26,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.60` | 7,160,000.00 USD | 7,160,000.00 USD | 2,090.00 USD | 0.00 USD | 327.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.60` | 10,050,000.00 USD | 10,050,000.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.70` | 7,200,000.00 USD | 7,200,000.00 USD | 20,030.00 USD | 4,920.00 USD | 18,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.70` | 10,130,000.00 USD | 10,130,000.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.80` | 7,240,000.00 USD | 7,240,000.00 USD | 17,470.00 USD | 7,010.00 USD | 10,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.80` | 10,280,000.00 USD | 10,280,000.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `62.90` | 7,260,000.00 USD | 7,260,000.00 USD | 8,780.00 USD | 10,210.00 USD | 1,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.90` | 10,370,000.00 USD | 10,370,000.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.00` | 7,280,000.00 USD | 7,280,000.00 USD | 10,350.00 USD | 7,320.00 USD | 10,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.00` | 10,440,000.00 USD | 10,440,000.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.10` | 7,310,000.00 USD | 7,310,000.00 USD | 12,260.00 USD | 4,070.00 USD | 9,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.10` | 10,480,000.00 USD | 10,480,000.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.20` | 7,310,000.00 USD | 7,310,000.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.30` | 7,330,000.00 USD | 7,330,000.00 USD | 5,160.00 USD | 4,550.00 USD | 2,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.30` | 10,520,000.00 USD | 10,520,000.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.40` | 7,330,000.00 USD | 7,330,000.00 USD | 1,910.00 USD | 931.11 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.40` | 10,540,000.00 USD | 10,540,000.00 USD | 13,660.00 USD | 656.00 USD | 9,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.50` | 7,360,000.00 USD | 7,360,000.00 USD | 8,930.00 USD | 14,750.00 USD | 5,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.50` | 10,570,000.00 USD | 10,570,000.00 USD | 5,690.00 USD | 15,240.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.60` | 7,400,000.00 USD | 7,400,000.00 USD | 18,400.00 USD | 3,660.00 USD | 10,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.60` | 10,650,000.00 USD | 10,650,000.00 USD | 52,430.00 USD | 13,690.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.70` | 7,480,000.00 USD | 7,480,000.00 USD | 38,080.00 USD | 11,010.00 USD | 31,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.70` | 10,710,000.00 USD | 10,710,000.00 USD | 20,540.00 USD | 18,810.00 USD | 21,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.80` | 7,520,000.00 USD | 7,520,000.00 USD | 20,300.00 USD | 10,990.00 USD | 12,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.80` | 10,770,000.00 USD | 10,770,000.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `63.90` | 7,600,000.00 USD | 7,600,000.00 USD | 38,980.00 USD | 14,090.00 USD | 22,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `63.90` | 10,800,000.00 USD | 10,800,000.00 USD | 6,490.00 USD | 12,370.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.00` | 7,610,000.00 USD | 7,610,000.00 USD | 5,540.00 USD | 10,620.00 USD | 245.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.00` | 10,830,000.00 USD | 10,830,000.00 USD | 10,140.00 USD | 10,630.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.10` | 7,640,000.00 USD | 7,640,000.00 USD | 7,160.00 USD | 8,120.00 USD | 9,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.10` | 10,860,000.00 USD | 10,860,000.00 USD | 13,040.00 USD | 667.05 USD | 18,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `64.20` | 7,660,000.00 USD | 7,660,000.00 USD | 10,610.00 USD | 6,450.00 USD | 10,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `64.20` | 10,920,000.00 USD | 10,920,000.00 USD | 44,990.00 USD | 6,760.00 USD | 8,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `64.25` | 735.02 USD | 220,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `65.15` | 267.12 USD | 220,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `65.95` | 1,160.00 USD | 222,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.85` | 33,950.00 USD | 255,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `66.95` | 121.18 USD | 256,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 256,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `68.75` | 191.13 USD | 256,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `70.45` | 6,740.00 USD | 263,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `71.75` | 5,110.00 USD | 268,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `73.15` | 667.86 USD | 269,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `75.15` | 129.26 USD | 269,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 277,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 278,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.95` | 136.41 USD | 278,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 279,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 298,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 298,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.65` | 3,850.00 USD | 302,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 302,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.85` | 2,770.00 USD | 305,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `83.95` | 3,360.00 USD | 308,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `84.65` | 862.58 USD | 309,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `87.35` | 23,310.00 USD | 332,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `89.55` | 163.88 USD | 333,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `93.15` | 990.18 USD | 334,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `93.25` | 1,900.00 USD | 335,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `96.35` | 3,070.00 USD | 338,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `100.35` | 20,070.00 USD | 359,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `103.65` | 20,730.00 USD | 379,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.35` | 352,080.00 USD | 731,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.45` | 131.44 USD | 731,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.55` | 1,120.00 USD | 733,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.65` | 4,830.00 USD | 737,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 738,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.65` | 2,920,000.00 USD | 0.00 USD | 226.13 USD | `-79.90%` | `19.41` |
| `Live` | `Long` | `12.25` | 2,920,000.00 USD | 0.00 USD | 122.50 USD | `-78.87%` | `10.00` |
| `Live` | `Long` | `12.65` | 2,920,000.00 USD | 0.00 USD | 2,540.00 USD | `-78.18%` | `200.43` |
| `Live` | `Long` | `13.05` | 2,910,000.00 USD | 0.00 USD | 2,200.00 USD | `-77.49%` | `168.79` |
| `Live` | `Long` | `13.65` | 2,910,000.00 USD | 0.00 USD | 2,210.00 USD | `-76.45%` | `161.57` |
| `Live` | `Long` | `14.55` | 2,910,000.00 USD | 0.00 USD | 465.60 USD | `-74.90%` | `32.00` |
| `Live` | `Long` | `14.75` | 2,910,000.00 USD | 0.00 USD | 885.00 USD | `-74.56%` | `60.00` |
| `Live` | `Long` | `15.15` | 2,910,000.00 USD | 0.00 USD | 3,410.00 USD | `-73.87%` | `225.00` |
| `Live` | `Long` | `15.95` | 2,900,000.00 USD | 0.00 USD | 620.77 USD | `-72.49%` | `38.92` |
| `Live` | `Long` | `16.35` | 2,900,000.00 USD | 0.00 USD | 1,960.00 USD | `-71.80%` | `120.00` |
| `Live` | `Long` | `16.55` | 2,900,000.00 USD | 0.00 USD | 467.87 USD | `-71.45%` | `28.27` |
| `Live` | `Long` | `16.65` | 2,900,000.00 USD | 0.00 USD | 3,250.00 USD | `-71.28%` | `195.03` |
| `Live` | `Long` | `18.95` | 2,900,000.00 USD | 0.00 USD | 5,580.00 USD | `-67.31%` | `294.67` |
| `Live` | `Long` | `19.05` | 2,890,000.00 USD | 0.00 USD | 3,470.00 USD | `-67.14%` | `182.00` |
| `Live` | `Long` | `19.45` | 2,890,000.00 USD | 0.00 USD | 2,010.00 USD | `-66.45%` | `103.47` |
| `Live` | `Long` | `21.35` | 2,890,000.00 USD | 0.00 USD | 344.38 USD | `-63.17%` | `16.13` |
| `Live` | `Long` | `21.85` | 2,890,000.00 USD | 0.00 USD | 213.26 USD | `-62.31%` | `9.76` |
| `Live` | `Long` | `22.55` | 2,890,000.00 USD | 0.00 USD | 133.27 USD | `-61.10%` | `5.91` |
| `Live` | `Long` | `23.75` | 2,890,000.00 USD | 0.00 USD | 194.75 USD | `-59.03%` | `8.20` |
| `Live` | `Long` | `24.05` | 2,890,000.00 USD | 0.00 USD | 421.36 USD | `-58.52%` | `17.52` |
| `Live` | `Long` | `25.05` | 2,890,000.00 USD | 0.00 USD | 694.14 USD | `-56.79%` | `27.71` |
| `Live` | `Long` | `25.25` | 2,880,000.00 USD | 0.00 USD | 277,980.00 USD | `-56.45%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,610,000.00 USD | 0.00 USD | 23,750.00 USD | `-56.27%` | `936.84` |
| `Live` | `Long` | `25.55` | 2,580,000.00 USD | 0.00 USD | 50,740.00 USD | `-55.93%` | `1,985.99` |
| `Live` | `Long` | `25.95` | 2,530,000.00 USD | 0.00 USD | 374.20 USD | `-55.24%` | `14.42` |
| `Live` | `Long` | `26.95` | 2,530,000.00 USD | 0.00 USD | 6,110.00 USD | `-53.51%` | `226.89` |
| `Live` | `Long` | `27.45` | 2,530,000.00 USD | 0.00 USD | 546.53 USD | `-52.65%` | `19.91` |
| `Live` | `Long` | `27.55` | 2,530,000.00 USD | 0.00 USD | 272.75 USD | `-52.48%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,520,000.00 USD | 0.00 USD | 453.35 USD | `-51.79%` | `16.22` |
| `Live` | `Long` | `28.55` | 2,520,000.00 USD | 0.00 USD | 8,560.00 USD | `-50.75%` | `300.00` |
| `Live` | `Long` | `28.85` | 2,520,000.00 USD | 0.00 USD | 225.90 USD | `-50.24%` | `7.83` |
| `Live` | `Long` | `29.15` | 2,520,000.00 USD | 0.00 USD | 583.00 USD | `-49.72%` | `20.00` |
| `Live` | `Long` | `29.25` | 2,510,000.00 USD | 0.00 USD | 3,630.00 USD | `-49.55%` | `124.01` |
| `Live` | `Long` | `29.55` | 2,510,000.00 USD | 0.00 USD | 108.74 USD | `-49.03%` | `3.68` |
| `Live` | `Long` | `29.75` | 2,510,000.00 USD | 0.00 USD | 298,070.00 USD | `-48.68%` | `10,019.26` |
| `Live` | `Long` | `30.05` | 2,210,000.00 USD | 0.00 USD | 218.46 USD | `-48.17%` | `7.27` |
| `Live` | `Long` | `30.15` | 2,210,000.00 USD | 0.00 USD | 1,020.00 USD | `-47.99%` | `33.94` |
| `Live` | `Long` | `30.35` | 2,210,000.00 USD | 0.00 USD | 121.40 USD | `-47.65%` | `4.00` |
| `Live` | `Long` | `30.85` | 2,210,000.00 USD | 0.00 USD | 4,030.00 USD | `-46.79%` | `130.63` |
| `Live` | `Long` | `30.95` | 2,210,000.00 USD | 0.00 USD | 538.53 USD | `-46.61%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,210,000.00 USD | 0.00 USD | 27,620.00 USD | `-46.27%` | `886.80` |
| `Live` | `Long` | `31.55` | 2,180,000.00 USD | 0.00 USD | 5,680.00 USD | `-45.58%` | `180.02` |
| `Live` | `Long` | `31.85` | 2,170,000.00 USD | 0.00 USD | 2,870.00 USD | `-45.06%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,170,000.00 USD | 0.00 USD | 125.24 USD | `-44.89%` | `3.92` |
| `Live` | `Long` | `32.05` | 2,170,000.00 USD | 0.00 USD | 382.04 USD | `-44.72%` | `11.92` |
| `Live` | `Long` | `32.15` | 2,170,000.00 USD | 0.00 USD | 4,000.00 USD | `-44.54%` | `124.50` |
| `Live` | `Long` | `32.45` | 2,170,000.00 USD | 0.00 USD | 166.47 USD | `-44.03%` | `5.13` |
| `Live` | `Long` | `32.65` | 2,170,000.00 USD | 0.00 USD | 653.00 USD | `-43.68%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,170,000.00 USD | 0.00 USD | 5,270.00 USD | `-43.51%` | `161.06` |
| `Live` | `Long` | `32.85` | 2,160,000.00 USD | 0.00 USD | 32,850.00 USD | `-43.34%` | `1,000.01` |
| `Live` | `Long` | `33.65` | 2,130,000.00 USD | 0.00 USD | 257.76 USD | `-41.96%` | `7.66` |
| `Live` | `Long` | `33.85` | 2,130,000.00 USD | 0.00 USD | 286.03 USD | `-41.61%` | `8.45` |
| `Live` | `Long` | `34.05` | 2,130,000.00 USD | 0.00 USD | 182.85 USD | `-41.27%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,130,000.00 USD | 0.00 USD | 126.70 USD | `-41.09%` | `3.71` |
| `Live` | `Long` | `34.55` | 2,130,000.00 USD | 0.00 USD | 6,020.00 USD | `-40.40%` | `174.22` |
| `Live` | `Long` | `34.65` | 2,120,000.00 USD | 0.00 USD | 3,240.00 USD | `-40.23%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,120,000.00 USD | 0.00 USD | 17,580.00 USD | `-39.71%` | `503.00` |
| `Live` | `Long` | `35.05` | 2,100,000.00 USD | 0.00 USD | 1,080.00 USD | `-39.54%` | `30.75` |
| `Live` | `Long` | `35.45` | 2,100,000.00 USD | 0.00 USD | 265.88 USD | `-38.85%` | `7.50` |
| `Live` | `Long` | `35.85` | 2,100,000.00 USD | 0.00 USD | 672.19 USD | `-38.16%` | `18.75` |
| `Live` | `Long` | `36.35` | 2,100,000.00 USD | 0.00 USD | 3,020.00 USD | `-37.30%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,090,000.00 USD | 0.00 USD | 423.18 USD | `-37.13%` | `11.61` |
| `Live` | `Long` | `36.75` | 2,090,000.00 USD | 0.00 USD | 101.80 USD | `-36.61%` | `2.77` |
| `Live` | `Long` | `37.05` | 2,090,000.00 USD | 0.00 USD | 359.76 USD | `-36.09%` | `9.71` |
| `Live` | `Long` | `37.15` | 2,090,000.00 USD | 0.00 USD | 438.74 USD | `-35.92%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,090,000.00 USD | 0.00 USD | 9,260.00 USD | `-35.57%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,080,000.00 USD | 0.00 USD | 3,530.00 USD | `-35.23%` | `94.04` |
| `Live` | `Long` | `37.65` | 2,080,000.00 USD | 0.00 USD | 4,850.00 USD | `-35.06%` | `128.71` |
| `Live` | `Long` | `37.85` | 2,080,000.00 USD | 0.00 USD | 6,210.00 USD | `-34.71%` | `164.03` |
| `Live` | `Long` | `37.95` | 2,070,000.00 USD | 0.00 USD | 446.67 USD | `-34.54%` | `11.77` |
| `Live` | `Long` | `38.05` | 2,070,000.00 USD | 0.00 USD | 15,940.00 USD | `-34.37%` | `418.87` |
| `Live` | `Long` | `38.35` | 2,050,000.00 USD | 0.00 USD | 341.70 USD | `-33.85%` | `8.91` |
| `Live` | `Long` | `38.45` | 2,050,000.00 USD | 0.00 USD | 287.61 USD | `-33.68%` | `7.48` |
| `Live` | `Long` | `38.55` | 2,050,000.00 USD | 0.00 USD | 5,150.00 USD | `-33.50%` | `133.70` |
| `Live` | `Long` | `38.65` | 2,050,000.00 USD | 0.00 USD | 384.57 USD | `-33.33%` | `9.95` |
| `Live` | `Long` | `38.95` | 2,050,000.00 USD | 0.00 USD | 4,840.00 USD | `-32.81%` | `124.26` |
| `Live` | `Long` | `39.05` | 2,040,000.00 USD | 0.00 USD | 664,760.00 USD | `-32.64%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,380,000.00 USD | 0.00 USD | 570.02 USD | `-32.47%` | `14.56` |
| `Live` | `Long` | `39.45` | 1,380,000.00 USD | 0.00 USD | 865.53 USD | `-31.95%` | `21.94` |
| `Live` | `Long` | `39.55` | 1,380,000.00 USD | 0.00 USD | 162.95 USD | `-31.78%` | `4.12` |
| `Live` | `Long` | `39.65` | 1,380,000.00 USD | 0.00 USD | 5,900.00 USD | `-31.61%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,370,000.00 USD | 0.00 USD | 1,550.00 USD | `-31.43%` | `38.90` |
| `Live` | `Long` | `39.85` | 1,370,000.00 USD | 0.00 USD | 133.10 USD | `-31.26%` | `3.34` |
| `Live` | `Long` | `40.05` | 1,370,000.00 USD | 0.00 USD | 2,160.00 USD | `-30.92%` | `53.97` |
| `Live` | `Long` | `40.35` | 1,370,000.00 USD | 0.00 USD | 154.94 USD | `-30.40%` | `3.84` |
| `Live` | `Long` | `40.45` | 1,370,000.00 USD | 0.00 USD | 1,670.00 USD | `-30.23%` | `41.39` |
| `Live` | `Long` | `40.55` | 1,360,000.00 USD | 0.00 USD | 133.00 USD | `-30.05%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,360,000.00 USD | 0.00 USD | 274.39 USD | `-29.88%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,360,000.00 USD | 0.00 USD | 6,340.00 USD | `-29.54%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,360,000.00 USD | 0.00 USD | 509.01 USD | `-29.36%` | `12.43` |
| `Live` | `Long` | `41.05` | 1,360,000.00 USD | 0.00 USD | 396.54 USD | `-29.19%` | `9.66` |
| `Live` | `Long` | `41.25` | 1,360,000.00 USD | 0.00 USD | 14,490.00 USD | `-28.85%` | `351.26` |
| `Live` | `Long` | `41.45` | 1,340,000.00 USD | 0.00 USD | 644.96 USD | `-28.50%` | `15.56` |
| `Live` | `Long` | `41.85` | 1,340,000.00 USD | 0.00 USD | 3,580.00 USD | `-27.81%` | `85.43` |
| `Live` | `Long` | `42.05` | 1,340,000.00 USD | 0.00 USD | 3,090.00 USD | `-27.47%` | `73.52` |
| `Live` | `Long` | `42.15` | 1,330,000.00 USD | 0.00 USD | 64,190.00 USD | `-27.29%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,270,000.00 USD | 0.00 USD | 35,410.00 USD | `-27.12%` | `838.00` |
| `Live` | `Long` | `42.35` | 1,240,000.00 USD | 0.00 USD | 243.94 USD | `-26.95%` | `5.76` |
| `Live` | `Long` | `42.65` | 1,240,000.00 USD | 0.00 USD | 1,710.00 USD | `-26.43%` | `40.16` |
| `Live` | `Long` | `42.75` | 1,230,000.00 USD | 0.00 USD | 26,780.00 USD | `-26.26%` | `626.50` |
| `Live` | `Long` | `42.85` | 1,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-26.09%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,200,000.00 USD | 0.00 USD | 2,000.00 USD | `-25.91%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,200,000.00 USD | 0.00 USD | 8,950.00 USD | `-25.74%` | `208.00` |
| `Live` | `Long` | `43.15` | 1,190,000.00 USD | 0.00 USD | 120,820.00 USD | `-25.57%` | `2,800.00` |
| `Live` | `Long` | `43.25` | 1,070,000.00 USD | 0.00 USD | 1,830.00 USD | `-25.40%` | `42.22` |
| `Live` | `Long` | `43.35` | 1,070,000.00 USD | 0.00 USD | 6,050.00 USD | `-25.22%` | `139.57` |
| `Live` | `Long` | `43.45` | 1,060,000.00 USD | 0.00 USD | 2,010.00 USD | `-25.05%` | `46.25` |
| `Live` | `Long` | `43.65` | 1,060,000.00 USD | 0.00 USD | 426.02 USD | `-24.71%` | `9.76` |
| `Live` | `Long` | `43.85` | 1,060,000.00 USD | 0.00 USD | 801.14 USD | `-24.36%` | `18.27` |
| `Live` | `Long` | `43.95` | 1,060,000.00 USD | 0.00 USD | 38,450.00 USD | `-24.19%` | `874.89` |
| `Live` | `Long` | `44.15` | 1,020,000.00 USD | 0.00 USD | 2,380.00 USD | `-23.84%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,020,000.00 USD | 0.00 USD | 274.79 USD | `-23.67%` | `6.21` |
| `Live` | `Long` | `44.35` | 1,020,000.00 USD | 0.00 USD | 84,440.00 USD | `-23.50%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 932,350.00 USD | 0.00 USD | 842.44 USD | `-23.15%` | `18.91` |
| `Live` | `Long` | `44.65` | 931,510.00 USD | 0.00 USD | 5,470.00 USD | `-22.98%` | `122.48` |
| `Live` | `Long` | `44.75` | 926,040.00 USD | 0.00 USD | 4,230.00 USD | `-22.81%` | `94.55` |
| `Live` | `Long` | `44.85` | 921,810.00 USD | 0.00 USD | 134.55 USD | `-22.64%` | `3.00` |
| `Live` | `Long` | `44.95` | 921,680.00 USD | 0.00 USD | 2,620.00 USD | `-22.46%` | `58.18` |
| `Live` | `Long` | `45.05` | 919,060.00 USD | 0.00 USD | 329.32 USD | `-22.29%` | `7.31` |
| `Live` | `Long` | `45.15` | 918,730.00 USD | 0.00 USD | 135.00 USD | `-22.12%` | `2.99` |
| `Live` | `Long` | `45.25` | 918,600.00 USD | 0.00 USD | 3,580.00 USD | `-21.95%` | `79.11` |
| `Live` | `Long` | `45.35` | 915,020.00 USD | 0.00 USD | 1,780.00 USD | `-21.77%` | `39.28` |
| `Live` | `Long` | `45.45` | 913,240.00 USD | 0.00 USD | 23,940.00 USD | `-21.60%` | `526.65` |
| `Live` | `Long` | `45.55` | 889,300.00 USD | 0.00 USD | 7,820.00 USD | `-21.43%` | `171.57` |
| `Live` | `Long` | `45.65` | 881,490.00 USD | 0.00 USD | 11,380.00 USD | `-21.26%` | `249.31` |
| `Live` | `Long` | `45.75` | 870,100.00 USD | 0.00 USD | 107.97 USD | `-21.08%` | `2.36` |
| `Live` | `Long` | `45.85` | 870,000.00 USD | 0.00 USD | 458.50 USD | `-20.91%` | `10.00` |
| `Live` | `Long` | `45.95` | 869,540.00 USD | 0.00 USD | 704.87 USD | `-20.74%` | `15.34` |
| `Live` | `Long` | `46.05` | 868,830.00 USD | 0.00 USD | 9,710.00 USD | `-20.57%` | `210.95` |
| `Live` | `Long` | `46.25` | 859,120.00 USD | 0.00 USD | 39,710.00 USD | `-20.22%` | `858.49` |
| `Live` | `Long` | `46.65` | 819,410.00 USD | 0.00 USD | 936.73 USD | `-19.53%` | `20.08` |
| `Live` | `Long` | `46.95` | 818,480.00 USD | 0.00 USD | 158.22 USD | `-19.01%` | `3.37` |
| `Live` | `Long` | `47.15` | 818,320.00 USD | 0.00 USD | 49,130.00 USD | `-18.67%` | `1,042.07` |
| `Live` | `Long` | `47.25` | 769,190.00 USD | 0.00 USD | 574.09 USD | `-18.50%` | `12.15` |
| `Live` | `Long` | `47.35` | 768,610.00 USD | 0.00 USD | 2,600.00 USD | `-18.32%` | `55.00` |
| `Live` | `Long` | `47.45` | 766,010.00 USD | 0.00 USD | 2,180.00 USD | `-18.15%` | `45.94` |
| `Live` | `Long` | `47.55` | 763,830.00 USD | 0.00 USD | 1,770.00 USD | `-17.98%` | `37.28` |
| `Live` | `Long` | `47.75` | 762,050.00 USD | 0.00 USD | 4,780.00 USD | `-17.63%` | `100.00` |
| `Live` | `Long` | `47.85` | 757,280.00 USD | 0.00 USD | 1,290.00 USD | `-17.46%` | `26.89` |
| `Live` | `Long` | `47.95` | 755,990.00 USD | 0.00 USD | 1,440.00 USD | `-17.29%` | `30.00` |
| `Live` | `Long` | `48.05` | 754,550.00 USD | 0.00 USD | 1,860.00 USD | `-17.12%` | `38.61` |
| `Live` | `Long` | `48.15` | 752,700.00 USD | 0.00 USD | 2,680.00 USD | `-16.94%` | `55.56` |
| `Live` | `Long` | `48.25` | 750,020.00 USD | 0.00 USD | 5,350.00 USD | `-16.77%` | `110.96` |
| `Live` | `Long` | `48.55` | 744,670.00 USD | 0.00 USD | 2,030.00 USD | `-16.25%` | `41.85` |
| `Live` | `Long` | `48.65` | 742,640.00 USD | 0.00 USD | 273.90 USD | `-16.08%` | `5.63` |
| `Live` | `Long` | `48.95` | 742,360.00 USD | 0.00 USD | 1,390.00 USD | `-15.56%` | `28.33` |
| `Live` | `Long` | `49.05` | 740,980.00 USD | 0.00 USD | 1,580.00 USD | `-15.39%` | `32.25` |
| `Live` | `Long` | `49.15` | 739,400.00 USD | 0.00 USD | 5,740.00 USD | `-15.22%` | `116.83` |
| `Live` | `Long` | `49.35` | 733,650.00 USD | 0.00 USD | 5,230.00 USD | `-14.87%` | `105.97` |
| `Live` | `Long` | `49.45` | 728,420.00 USD | 0.00 USD | 9,350.00 USD | `-14.70%` | `188.98` |
| `Live` | `Long` | `49.55` | 719,080.00 USD | 0.00 USD | 18,010.00 USD | `-14.53%` | `363.57` |
| `Live` | `Long` | `49.65` | 701,060.00 USD | 0.00 USD | 17,300.00 USD | `-14.36%` | `348.52` |
| `Live` | `Long` | `49.75` | 683,760.00 USD | 0.00 USD | 20,390.00 USD | `-14.18%` | `409.75` |
| `Live` | `Long` | `49.85` | 663,370.00 USD | 0.00 USD | 3,240.00 USD | `-14.01%` | `65.00` |
| `Live` | `Long` | `49.95` | 660,130.00 USD | 0.00 USD | 28,540.00 USD | `-13.84%` | `571.31` |
| `Live` | `Long` | `50.05` | 631,600.00 USD | 0.00 USD | 1,820.00 USD | `-13.67%` | `36.43` |
| `Live` | `Long` | `50.25` | 629,770.00 USD | 0.00 USD | 102.51 USD | `-13.32%` | `2.04` |
| `Live` | `Long` | `50.35` | 629,670.00 USD | 0.00 USD | 1,030.00 USD | `-13.15%` | `20.49` |
| `Live` | `Long` | `50.45` | 628,640.00 USD | 0.00 USD | 4,720.00 USD | `-12.98%` | `93.64` |
| `Live` | `Long` | `50.55` | 623,920.00 USD | 0.00 USD | 84,100.00 USD | `-12.80%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 539,820.00 USD | 0.00 USD | 9,050.00 USD | `-12.46%` | `178.28` |
| `Live` | `Long` | `50.95` | 530,770.00 USD | 0.00 USD | 245.07 USD | `-12.11%` | `4.81` |
| `Live` | `Long` | `51.15` | 530,530.00 USD | 0.00 USD | 235,460.00 USD | `-11.77%` | `4,603.23` |
| `Live` | `Long` | `51.45` | 295,070.00 USD | 0.00 USD | 19,630.00 USD | `-11.25%` | `381.45` |
| `Live` | `Long` | `51.55` | 275,450.00 USD | 0.00 USD | 551.07 USD | `-11.08%` | `10.69` |
| `Live` | `Long` | `51.65` | 274,900.00 USD | 0.00 USD | 155.47 USD | `-10.91%` | `3.01` |
| `Live` | `Long` | `51.75` | 274,740.00 USD | 0.00 USD | 6,450.00 USD | `-10.73%` | `124.64` |
| `Live` | `Long` | `51.85` | 268,290.00 USD | 0.00 USD | 3,580.00 USD | `-10.56%` | `69.10` |
| `Live` | `Long` | `51.95` | 264,710.00 USD | 0.00 USD | 12,070.00 USD | `-10.39%` | `232.41` |
| `Live` | `Long` | `52.25` | 252,630.00 USD | 0.00 USD | 563.25 USD | `-9.87%` | `10.78` |
| `Live` | `Long` | `52.35` | 252,070.00 USD | 0.00 USD | 27,650.00 USD | `-9.70%` | `528.09` |
| `Live` | `Long` | `52.45` | 224,420.00 USD | 0.00 USD | 3,620.00 USD | `-9.53%` | `68.95` |
| `Live` | `Long` | `52.55` | 220,810.00 USD | 0.00 USD | 8,700.00 USD | `-9.35%` | `165.49` |
| `Live` | `Long` | `52.75` | 212,110.00 USD | 0.00 USD | 7,110.00 USD | `-9.01%` | `134.82` |
| `Live` | `Long` | `52.85` | 205,000.00 USD | 0.00 USD | 5,950.00 USD | `-8.84%` | `112.64` |
| `Live` | `Long` | `52.95` | 199,050.00 USD | 0.00 USD | 11,500.00 USD | `-8.66%` | `217.16` |
| `Live` | `Long` | `53.05` | 187,550.00 USD | 0.00 USD | 1,860.00 USD | `-8.49%` | `35.13` |
| `Live` | `Long` | `53.15` | 185,680.00 USD | 0.00 USD | 181.24 USD | `-8.32%` | `3.41` |
| `Live` | `Long` | `53.25` | 185,500.00 USD | 0.00 USD | 1,500.00 USD | `-8.15%` | `28.15` |
| `Live` | `Long` | `53.35` | 184,000.00 USD | 0.00 USD | 1,910.00 USD | `-7.97%` | `35.71` |
| `Live` | `Long` | `53.45` | 182,100.00 USD | 0.00 USD | 4,880.00 USD | `-7.80%` | `91.21` |
| `Live` | `Long` | `53.65` | 177,220.00 USD | 0.00 USD | 533.82 USD | `-7.46%` | `9.95` |
| `Live` | `Long` | `53.75` | 176,690.00 USD | 0.00 USD | 23,570.00 USD | `-7.28%` | `438.47` |
| `Live` | `Long` | `53.85` | 153,120.00 USD | 0.00 USD | 2,130.00 USD | `-7.11%` | `39.58` |
| `Live` | `Long` | `53.95` | 150,990.00 USD | 0.00 USD | 28,950.00 USD | `-6.94%` | `536.62` |
| `Live` | `Long` | `54.05` | 122,040.00 USD | 0.00 USD | 219.44 USD | `-6.77%` | `4.06` |
| `Live` | `Long` | `54.15` | 121,820.00 USD | 0.00 USD | 13,440.00 USD | `-6.59%` | `248.25` |
| `Live` | `Long` | `54.25` | 108,380.00 USD | 0.00 USD | 2,720.00 USD | `-6.42%` | `50.12` |
| `Live` | `Long` | `54.55` | 105,660.00 USD | 0.00 USD | 1,060.00 USD | `-5.90%` | `19.49` |
| `Live` | `Long` | `54.65` | 104,600.00 USD | 0.00 USD | 12,980.00 USD | `-5.73%` | `237.57` |
| `Live` | `Long` | `54.75` | 91,610.00 USD | 0.00 USD | 180.67 USD | `-5.56%` | `3.30` |
| `Live` | `Long` | `54.95` | 91,430.00 USD | 0.00 USD | 8,190.00 USD | `-5.21%` | `149.09` |
| `Live` | `Long` | `55.05` | 83,240.00 USD | 0.00 USD | 394.71 USD | `-5.04%` | `7.17` |
| `Live` | `Long` | `55.15` | 82,850.00 USD | 0.00 USD | 3,010.00 USD | `-4.87%` | `54.52` |
| `Live` | `Long` | `55.35` | 79,840.00 USD | 0.00 USD | 1,610.00 USD | `-4.52%` | `29.05` |
| `Live` | `Long` | `56.15` | 78,230.00 USD | 0.00 USD | 78,230.00 USD | `-3.14%` | `1,393.24` |
| `Live` | `Short` | `60.55` | 302.14 USD | 302.14 USD | 0.00 USD | `+4.45%` | `4.99` |
| `Live` | `Short` | `60.75` | 1,620.00 USD | 1,310.00 USD | 0.00 USD | `+4.79%` | `21.64` |
| `Live` | `Short` | `60.85` | 5,410.00 USD | 3,790.00 USD | 0.00 USD | `+4.96%` | `62.35` |
| `Live` | `Short` | `60.95` | 6,070.00 USD | 662.53 USD | 0.00 USD | `+5.14%` | `10.87` |
| `Live` | `Short` | `61.15` | 6,230.00 USD | 156.54 USD | 0.00 USD | `+5.48%` | `2.56` |
| `Live` | `Short` | `62.35` | 219,830.00 USD | 213,600.00 USD | 0.00 USD | `+7.55%` | `3,425.89` |
| `Live` | `Short` | `64.25` | 220,570.00 USD | 735.02 USD | 0.00 USD | `+10.83%` | `11.44` |
| `Live` | `Short` | `65.15` | 220,840.00 USD | 267.12 USD | 0.00 USD | `+12.38%` | `4.10` |
| `Live` | `Short` | `65.95` | 222,000.00 USD | 1,160.00 USD | 0.00 USD | `+13.76%` | `17.59` |
| `Live` | `Short` | `66.85` | 255,940.00 USD | 33,950.00 USD | 0.00 USD | `+15.31%` | `507.83` |
| `Live` | `Short` | `66.95` | 256,070.00 USD | 121.18 USD | 0.00 USD | `+15.48%` | `1.81` |
| `Live` | `Short` | `67.85` | 256,770.00 USD | 709.03 USD | 0.00 USD | `+17.04%` | `10.45` |
| `Live` | `Short` | `68.75` | 256,970.00 USD | 191.13 USD | 0.00 USD | `+18.59%` | `2.78` |
| `Live` | `Short` | `70.45` | 263,700.00 USD | 6,740.00 USD | 0.00 USD | `+21.52%` | `95.63` |
| `Live` | `Short` | `71.75` | 268,810.00 USD | 5,110.00 USD | 0.00 USD | `+23.76%` | `71.15` |
| `Live` | `Short` | `73.15` | 269,480.00 USD | 667.86 USD | 0.00 USD | `+26.18%` | `9.13` |
| `Live` | `Short` | `75.15` | 269,610.00 USD | 129.26 USD | 0.00 USD | `+29.63%` | `1.72` |
| `Live` | `Short` | `76.35` | 277,990.00 USD | 8,380.00 USD | 0.00 USD | `+31.70%` | `109.80` |
| `Live` | `Short` | `77.85` | 278,590.00 USD | 602.56 USD | 0.00 USD | `+34.29%` | `7.74` |
| `Live` | `Short` | `77.95` | 278,730.00 USD | 136.41 USD | 0.00 USD | `+34.46%` | `1.75` |
| `Live` | `Short` | `80.75` | 279,370.00 USD | 646.00 USD | 0.00 USD | `+39.29%` | `8.00` |
| `Live` | `Short` | `81.05` | 298,370.00 USD | 19,000.00 USD | 0.00 USD | `+39.81%` | `234.42` |
| `Live` | `Short` | `81.55` | 298,500.00 USD | 123.96 USD | 0.00 USD | `+40.67%` | `1.52` |
| `Live` | `Short` | `82.65` | 302,350.00 USD | 3,850.00 USD | 0.00 USD | `+42.57%` | `46.61` |
| `Live` | `Short` | `82.75` | 302,560.00 USD | 214.32 USD | 0.00 USD | `+42.74%` | `2.59` |
| `Live` | `Short` | `83.85` | 305,330.00 USD | 2,770.00 USD | 0.00 USD | `+44.64%` | `33.00` |
| `Live` | `Short` | `83.95` | 308,690.00 USD | 3,360.00 USD | 0.00 USD | `+44.81%` | `40.00` |
| `Live` | `Short` | `84.65` | 309,550.00 USD | 862.58 USD | 0.00 USD | `+46.02%` | `10.19` |
| `Live` | `Short` | `87.35` | 332,860.00 USD | 23,310.00 USD | 0.00 USD | `+50.67%` | `266.81` |
| `Live` | `Short` | `89.55` | 333,020.00 USD | 163.88 USD | 0.00 USD | `+54.47%` | `1.83` |
| `Live` | `Short` | `93.15` | 334,010.00 USD | 990.18 USD | 0.00 USD | `+60.68%` | `10.63` |
| `Live` | `Short` | `93.25` | 335,910.00 USD | 1,900.00 USD | 0.00 USD | `+60.85%` | `20.39` |
| `Live` | `Short` | `96.35` | 338,980.00 USD | 3,070.00 USD | 0.00 USD | `+66.20%` | `31.83` |
| `Live` | `Short` | `100.35` | 359,050.00 USD | 20,070.00 USD | 0.00 USD | `+73.10%` | `200.00` |
| `Live` | `Short` | `103.65` | 379,780.00 USD | 20,730.00 USD | 0.00 USD | `+78.79%` | `200.00` |
| `Live` | `Short` | `104.35` | 731,860.00 USD | 352,080.00 USD | 0.00 USD | `+80.00%` | `3,374.01` |
| `Live` | `Short` | `110.45` | 731,990.00 USD | 131.44 USD | 0.00 USD | `+90.52%` | `1.19` |
| `Live` | `Short` | `110.55` | 733,110.00 USD | 1,120.00 USD | 0.00 USD | `+90.69%` | `10.11` |
| `Live` | `Short` | `110.65` | 737,940.00 USD | 4,830.00 USD | 0.00 USD | `+90.86%` | `43.66` |
| `Live` | `Short` | `110.95` | 738,600.00 USD | 664.59 USD | 0.00 USD | `+91.38%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 483,230.00 USD | 0.00 USD | 392.18 USD | `-65.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 482,840.00 USD | 0.00 USD | 2,310.00 USD | `-61.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 480,530.00 USD | 0.00 USD | 122.24 USD | `-56.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 480,410.00 USD | 0.00 USD | 1,560.00 USD | `-56.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 478,850.00 USD | 0.00 USD | 410.25 USD | `-52.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 478,440.00 USD | 0.00 USD | 281.57 USD | `-48.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 478,160.00 USD | 0.00 USD | 36,050.00 USD | `-37.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.05` | 442,110.00 USD | 0.00 USD | 3,590.00 USD | `-36.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 438,520.00 USD | 0.00 USD | 37,550.00 USD | `-35.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 400,970.00 USD | 0.00 USD | 447.01 USD | `-34.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 400,520.00 USD | 0.00 USD | 40,560.00 USD | `-32.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 359,970.00 USD | 0.00 USD | 489.57 USD | `-31.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 359,480.00 USD | 0.00 USD | 1,550.00 USD | `-31.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 357,920.00 USD | 0.00 USD | 9,500.00 USD | `-30.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 348,420.00 USD | 0.00 USD | 2,060.00 USD | `-29.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 346,370.00 USD | 0.00 USD | 2,960.00 USD | `-28.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 343,410.00 USD | 0.00 USD | 6,050.00 USD | `-27.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 337,360.00 USD | 0.00 USD | 5,680.00 USD | `-25.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 331,680.00 USD | 0.00 USD | 672.22 USD | `-24.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 331,000.00 USD | 0.00 USD | 213.80 USD | `-23.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 330,790.00 USD | 0.00 USD | 223.20 USD | `-23.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 330,570.00 USD | 0.00 USD | 391.13 USD | `-22.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 330,180.00 USD | 0.00 USD | 7,080.00 USD | `-22.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 323,100.00 USD | 0.00 USD | 1,370.00 USD | `-21.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.85` | 321,730.00 USD | 0.00 USD | 158.18 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 321,570.00 USD | 0.00 USD | 553.80 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 321,020.00 USD | 0.00 USD | 14,000.00 USD | `-19.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 307,030.00 USD | 0.00 USD | 158.56 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 306,870.00 USD | 0.00 USD | 373.28 USD | `-18.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 306,490.00 USD | 0.00 USD | 849.46 USD | `-18.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 305,640.00 USD | 0.00 USD | 1,150.00 USD | `-17.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 304,490.00 USD | 0.00 USD | 1,740.00 USD | `-15.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 302,750.00 USD | 0.00 USD | 981.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 301,770.00 USD | 0.00 USD | 1,150.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 300,630.00 USD | 0.00 USD | 298.20 USD | `-13.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 300,330.00 USD | 0.00 USD | 14,650.00 USD | `-13.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 285,670.00 USD | 0.00 USD | 6,410.00 USD | `-13.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 279,260.00 USD | 0.00 USD | 459.70 USD | `-13.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 278,800.00 USD | 0.00 USD | 1,020.00 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 277,780.00 USD | 0.00 USD | 439.89 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 277,340.00 USD | 0.00 USD | 3,700.00 USD | `-10.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.75` | 273,640.00 USD | 0.00 USD | 107.64 USD | `-10.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 273,530.00 USD | 0.00 USD | 26,430.00 USD | `-10.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 247,100.00 USD | 0.00 USD | 51,800.00 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 195,300.00 USD | 0.00 USD | 10,530.00 USD | `-9.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 184,770.00 USD | 0.00 USD | 271.13 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 184,500.00 USD | 0.00 USD | 12,410.00 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 172,090.00 USD | 0.00 USD | 1,060.00 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 171,030.00 USD | 0.00 USD | 460.81 USD | `-8.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.35` | 170,570.00 USD | 0.00 USD | 4,740.00 USD | `-7.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 165,830.00 USD | 0.00 USD | 184.21 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 165,650.00 USD | 0.00 USD | 1,370.00 USD | `-7.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 164,280.00 USD | 0.00 USD | 462.03 USD | `-7.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.95` | 163,820.00 USD | 0.00 USD | 201.23 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 163,620.00 USD | 0.00 USD | 601.58 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 163,010.00 USD | 0.00 USD | 3,090.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 159,930.00 USD | 0.00 USD | 156.53 USD | `-6.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 159,770.00 USD | 0.00 USD | 570.09 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 159,200.00 USD | 0.00 USD | 5,090.00 USD | `-5.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 154,110.00 USD | 0.00 USD | 2,210.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 151,900.00 USD | 0.00 USD | 3,510.00 USD | `-5.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 148,390.00 USD | 0.00 USD | 18,160.00 USD | `-5.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 130,230.00 USD | 0.00 USD | 219.80 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 130,010.00 USD | 0.00 USD | 2,040.00 USD | `-5.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 127,970.00 USD | 0.00 USD | 532.61 USD | `-4.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 127,430.00 USD | 0.00 USD | 2,140.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 125,300.00 USD | 0.00 USD | 3,360.00 USD | `-4.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 121,930.00 USD | 0.00 USD | 4,930.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 117,010.00 USD | 0.00 USD | 309.41 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.85` | 116,700.00 USD | 0.00 USD | 196.59 USD | `-3.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.95` | 116,500.00 USD | 0.00 USD | 193.03 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.05` | 116,310.00 USD | 0.00 USD | 587.96 USD | `-3.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.15` | 115,720.00 USD | 0.00 USD | 1,070.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.35` | 114,650.00 USD | 0.00 USD | 78,570.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.45` | 36,070.00 USD | 0.00 USD | 694.90 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.55` | 35,380.00 USD | 0.00 USD | 2,640.00 USD | `-2.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.65` | 32,740.00 USD | 0.00 USD | 1,230.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.75` | 31,510.00 USD | 0.00 USD | 1,200.00 USD | `-2.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.85` | 30,310.00 USD | 0.00 USD | 17,440.00 USD | `-1.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `56.95` | 12,860.00 USD | 0.00 USD | 474.96 USD | `-1.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.05` | 12,390.00 USD | 0.00 USD | 5,800.00 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.15` | 6,590.00 USD | 0.00 USD | 4,030.00 USD | `-1.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.25` | 2,550.00 USD | 0.00 USD | 150.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.35` | 2,400.00 USD | 0.00 USD | 444.46 USD | `-1.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.45` | 1,960.00 USD | 0.00 USD | 877.26 USD | `-0.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.55` | 1,080.00 USD | 0.00 USD | 202.58 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.65` | 880.38 USD | 0.00 USD | 160.27 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.75` | 720.11 USD | 0.00 USD | 199.24 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.85` | 520.87 USD | 0.00 USD | 392.22 USD | `-0.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `57.95` | 128.65 USD | 0.00 USD | 128.65 USD | `-0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 1,980.00 USD | 1,980.00 USD | 0.00 USD | `+0.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 2,360.00 USD | 385.53 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 2,540.00 USD | 174.75 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 2,660.00 USD | 123.70 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 3,430.00 USD | 766.28 USD | 0.00 USD | `+0.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 3,530.00 USD | 100.71 USD | 0.00 USD | `+1.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.65` | 3,800.00 USD | 274.48 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 3,930.00 USD | 124.55 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 7,220.00 USD | 3,290.00 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 12,320.00 USD | 5,100.00 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 17,120.00 USD | 4,800.00 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 18,400.00 USD | 1,280.00 USD | 0.00 USD | `+2.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 18,860.00 USD | 461.74 USD | 0.00 USD | `+2.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 19,060.00 USD | 200.35 USD | 0.00 USD | `+2.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.55` | 19,560.00 USD | 496.65 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 20,560.00 USD | 1,000.00 USD | 0.00 USD | `+2.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.75` | 20,670.00 USD | 113.53 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 21,170.00 USD | 500.94 USD | 0.00 USD | `+3.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.95` | 36,540.00 USD | 15,360.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 37,160.00 USD | 627.52 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.15` | 38,970.00 USD | 1,800.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 39,520.00 USD | 551.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 323,620.00 USD | 284,100.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 325,620.00 USD | 2,000.00 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 326,030.00 USD | 413.63 USD | 0.00 USD | `+4.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.75` | 326,440.00 USD | 407.63 USD | 0.00 USD | `+4.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 327,640.00 USD | 1,190.00 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 328,520.00 USD | 882.56 USD | 0.00 USD | `+5.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 330,880.00 USD | 2,360.00 USD | 0.00 USD | `+5.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 331,010.00 USD | 125.56 USD | 0.00 USD | `+5.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.35` | 331,240.00 USD | 236.20 USD | 0.00 USD | `+5.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 334,840.00 USD | 3,600.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 335,480.00 USD | 643.20 USD | 0.00 USD | `+6.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.95` | 337,600.00 USD | 2,120.00 USD | 0.00 USD | `+6.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 341,470.00 USD | 3,870.00 USD | 0.00 USD | `+7.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.25` | 341,590.00 USD | 117.03 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 342,070.00 USD | 483.21 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.45` | 342,290.00 USD | 217.95 USD | 0.00 USD | `+7.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 342,640.00 USD | 347.15 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 343,350.00 USD | 716.72 USD | 0.00 USD | `+8.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.75` | 343,490.00 USD | 141.19 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 344,830.00 USD | 1,340.00 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 345,740.00 USD | 900.52 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 346,440.00 USD | 703.97 USD | 0.00 USD | `+9.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.35` | 346,580.00 USD | 140.64 USD | 0.00 USD | `+9.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 347,250.00 USD | 668.13 USD | 0.00 USD | `+9.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 351,800.00 USD | 4,550.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 352,330.00 USD | 531.62 USD | 0.00 USD | `+10.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 352,530.00 USD | 202.69 USD | 0.00 USD | `+11.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 352,830.00 USD | 298.04 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 352,930.00 USD | 102.13 USD | 0.00 USD | `+12.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 353,470.00 USD | 540.09 USD | 0.00 USD | `+12.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 353,570.00 USD | 100.79 USD | 0.00 USD | `+12.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 353,840.00 USD | 262.20 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.65` | 354,150.00 USD | 315.12 USD | 0.00 USD | `+13.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 354,520.00 USD | 371.49 USD | 0.00 USD | `+13.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.85` | 355,400.00 USD | 881.07 USD | 0.00 USD | `+13.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 356,230.00 USD | 825.63 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 356,760.00 USD | 534.00 USD | 0.00 USD | `+15.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 367,840.00 USD | 11,080.00 USD | 0.00 USD | `+15.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 381,250.00 USD | 13,410.00 USD | 0.00 USD | `+15.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 386,120.00 USD | 4,860.00 USD | 0.00 USD | `+17.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 386,320.00 USD | 204.48 USD | 0.00 USD | `+19.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 388,230.00 USD | 1,910.00 USD | 0.00 USD | `+20.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 389,040.00 USD | 810.02 USD | 0.00 USD | `+20.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 708,940.00 USD | 319,890.00 USD | 0.00 USD | `+20.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.75` | 710,200.00 USD | 1,260.00 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 710,370.00 USD | 170.04 USD | 0.00 USD | `+22.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 716,140.00 USD | 5,770.00 USD | 0.00 USD | `+22.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 716,700.00 USD | 555.61 USD | 0.00 USD | `+22.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 717,850.00 USD | 1,150.00 USD | 0.00 USD | `+24.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 720,550.00 USD | 2,700.00 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 720,710.00 USD | 156.78 USD | 0.00 USD | `+24.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 723,930.00 USD | 3,220.00 USD | 0.00 USD | `+25.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 724,340.00 USD | 411.14 USD | 0.00 USD | `+26.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 847,530.00 USD | 123,190.00 USD | 0.00 USD | `+27.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 848,550.00 USD | 1,020.00 USD | 0.00 USD | `+28.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 848,650.00 USD | 104.93 USD | 0.00 USD | `+29.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 849,050.00 USD | 392.51 USD | 0.00 USD | `+29.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 849,450.00 USD | 402.59 USD | 0.00 USD | `+29.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `76.05` | 854,890.00 USD | 5,440.00 USD | 0.00 USD | `+31.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 855,200.00 USD | 315.18 USD | 0.00 USD | `+33.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 914,510.00 USD | 59,310.00 USD | 0.00 USD | `+35.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 917,670.00 USD | 3,160.00 USD | 0.00 USD | `+36.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 923,360.00 USD | 5,690.00 USD | 0.00 USD | `+37.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 960,980.00 USD | 37,620.00 USD | 0.00 USD | `+38.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 961,420.00 USD | 433.89 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,000,000.00 USD | 40,700.00 USD | 0.00 USD | `+39.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,000,000.00 USD | 164.10 USD | 0.00 USD | `+41.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,000,000.00 USD | 546.81 USD | 0.00 USD | `+42.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,010,000.00 USD | 2,300.00 USD | 0.00 USD | `+44.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,020,000.00 USD | 12,070.00 USD | 0.00 USD | `+46.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.75` | 1,030,000.00 USD | 12,330.00 USD | 0.00 USD | `+47.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.25` | 1,030,000.00 USD | 435.38 USD | 0.00 USD | `+50.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,030,000.00 USD | 1,580.00 USD | 0.00 USD | `+51.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,070,000.00 USD | 37,000.00 USD | 0.00 USD | `+51.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,070,000.00 USD | 473.21 USD | 0.00 USD | `+53.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,070,000.00 USD | 845.08 USD | 0.00 USD | `+53.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,070,000.00 USD | 1,630.00 USD | 0.00 USD | `+54.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,090,000.00 USD | 18,740.00 USD | 0.00 USD | `+55.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,090,000.00 USD | 481.55 USD | 0.00 USD | `+57.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,090,000.00 USD | 1,330.00 USD | 0.00 USD | `+58.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,090,000.00 USD | 188.10 USD | 0.00 USD | `+62.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,360,000.00 USD | 266,140.00 USD | 0.00 USD | `+63.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,360,000.00 USD | 3,400.00 USD | 0.00 USD | `+64.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,380,000.00 USD | 21,930.00 USD | 0.00 USD | `+65.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,380,000.00 USD | 294.15 USD | 0.00 USD | `+69.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,390,000.00 USD | 4,010.00 USD | 0.00 USD | `+72.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,390,000.00 USD | 306.15 USD | 0.00 USD | `+76.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,390,000.00 USD | 936.72 USD | 0.00 USD | `+77.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,390,000.00 USD | 2,920.00 USD | 0.00 USD | `+77.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,390,000.00 USD | 324.15 USD | 0.00 USD | `+86.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,390,000.00 USD | 123.23 USD | 0.00 USD | `+88.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,480,000.00 USD | 89,110.00 USD | 0.00 USD | `+91.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `112.35` | 1,490,000.00 USD | 10,880.00 USD | 0.00 USD | `+93.80%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `51.10` | 17,920,000.00 USD | 0.00 USD | 17,920,000.00 USD | 114,000.00 USD | 41,880.00 USD | 98,810.00 USD |
| `7D` | `51.20` | 17,670,000.00 USD | 0.00 USD | 17,670,000.00 USD | 25,820.00 USD | 7,100.00 USD | 27,730.00 USD |
| `7D` | `51.30` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 17,810.00 USD | 12,490.00 USD | 47,090.00 USD |
| `7D` | `51.40` | 17,530,000.00 USD | 0.00 USD | 17,530,000.00 USD | 69,290.00 USD | 28,960.00 USD | 45,150.00 USD |
| `7D` | `51.50` | 17,380,000.00 USD | 0.00 USD | 17,380,000.00 USD | 33,190.00 USD | 23,710.00 USD | 36,170.00 USD |
| `7D` | `51.60` | 17,290,000.00 USD | 0.00 USD | 17,290,000.00 USD | 33,770.00 USD | 12,240.00 USD | 17,650.00 USD |
| `7D` | `51.70` | 17,230,000.00 USD | 0.00 USD | 17,230,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `7D` | `51.80` | 17,190,000.00 USD | 0.00 USD | 17,190,000.00 USD | 21,870.00 USD | 12,160.00 USD | 19,510.00 USD |
| `1D` | `51.90` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 13,770.00 USD | 20,230.00 USD | 13,690.00 USD |
| `7D` | `51.90` | 17,140,000.00 USD | 0.00 USD | 17,140,000.00 USD | 4,940.00 USD | 15,240.00 USD | 4,760.00 USD |
| `1D` | `52.00` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 18,400.00 USD | 3,660.00 USD | 10,020.00 USD |
| `7D` | `52.00` | 17,110,000.00 USD | 0.00 USD | 17,110,000.00 USD | 53,250.00 USD | 13,690.00 USD | 11,640.00 USD |
| `1D` | `52.10` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 37,310.00 USD | 11,010.00 USD | 31,870.00 USD |
| `7D` | `52.10` | 17,030,000.00 USD | 0.00 USD | 17,030,000.00 USD | 22,820.00 USD | 18,810.00 USD | 21,910.00 USD |
| `1D` | `52.20` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 21,730.00 USD | 10,990.00 USD | 11,940.00 USD |
| `7D` | `52.20` | 16,970,000.00 USD | 0.00 USD | 16,970,000.00 USD | 35,740.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 38,980.00 USD | 14,090.00 USD | 23,220.00 USD |
| `7D` | `52.30` | 16,900,000.00 USD | 0.00 USD | 16,900,000.00 USD | 12,910.00 USD | 12,370.00 USD | 8,770.00 USD |
| `1D` | `52.40` | 5,940,000.00 USD | 0.00 USD | 5,940,000.00 USD | 5,540.00 USD | 10,620.00 USD | 158.33 USD |
| `7D` | `52.40` | 16,870,000.00 USD | 0.00 USD | 16,870,000.00 USD | 19,330.00 USD | 10,630.00 USD | 7,650.00 USD |
| `1D` | `52.50` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 7,160.00 USD | 8,120.00 USD | 9,920.00 USD |
| `7D` | `52.50` | 16,830,000.00 USD | 0.00 USD | 16,830,000.00 USD | 25,930.00 USD | 667.05 USD | 18,540.00 USD |
| `1D` | `52.60` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 10,900.00 USD | 6,450.00 USD | 10,560.00 USD |
| `7D` | `52.60` | 16,790,000.00 USD | 0.00 USD | 16,790,000.00 USD | 52,790.00 USD | 6,760.00 USD | 8,940.00 USD |
| `1D` | `52.70` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 30,140.00 USD | 9,010.00 USD | 18,400.00 USD |
| `7D` | `52.70` | 16,720,000.00 USD | 0.00 USD | 16,720,000.00 USD | 19,810.00 USD | 27,090.00 USD | 35,160.00 USD |
| `1D` | `52.80` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 9,200.00 USD | 2,400.00 USD | 8,730.00 USD |
| `7D` | `52.80` | 16,640,000.00 USD | 0.00 USD | 16,640,000.00 USD | 39,270.00 USD | 18,870.00 USD | 108.50 USD |
| `1D` | `52.90` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 1,560.00 USD | 10,250.00 USD | 12,260.00 USD |
| `7D` | `52.90` | 16,580,000.00 USD | 0.00 USD | 16,580,000.00 USD | 37,910.00 USD | 24,700.00 USD | 3,870.00 USD |
| `1D` | `53.00` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 4,250.00 USD | 2,200.00 USD | 842.86 USD |
| `7D` | `53.00` | 16,510,000.00 USD | 0.00 USD | 16,510,000.00 USD | 19,580.00 USD | 8,880.00 USD | 32,670.00 USD |
| `1D` | `53.10` | 5,760,000.00 USD | 0.00 USD | 5,760,000.00 USD | 17,750.00 USD | 2,780.00 USD | 7,520.00 USD |
| `7D` | `53.10` | 16,450,000.00 USD | 0.00 USD | 16,450,000.00 USD | 51,920.00 USD | 29,200.00 USD | 9,860.00 USD |
| `1D` | `53.20` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 25,580.00 USD | 11,010.00 USD | 6,340.00 USD |
| `7D` | `53.20` | 16,360,000.00 USD | 0.00 USD | 16,360,000.00 USD | 90,340.00 USD | 17,580.00 USD | 25,530.00 USD |
| `1D` | `53.30` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 10,170.00 USD | 10,720.00 USD | 10,120.00 USD |
| `7D` | `53.30` | 16,230,000.00 USD | 0.00 USD | 16,230,000.00 USD | 63,050.00 USD | 14,250.00 USD | 37,140.00 USD |
| `1D` | `53.40` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 42,240.00 USD | 11,460.00 USD | 32,610.00 USD |
| `7D` | `53.40` | 16,110,000.00 USD | 0.00 USD | 16,110,000.00 USD | 49,250.00 USD | 4,350.00 USD | 48,070.00 USD |
| `1D` | `53.50` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 25,150.00 USD | 5,350.00 USD | 4,970.00 USD |
| `7D` | `53.50` | 16,010,000.00 USD | 0.00 USD | 16,010,000.00 USD | 50,210.00 USD | 13,810.00 USD | 22,130.00 USD |
| `1D` | `53.60` | 5,540,000.00 USD | 0.00 USD | 5,540,000.00 USD | 29,300.00 USD | 5,030.00 USD | 22,080.00 USD |
| `7D` | `53.60` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 51,280.00 USD | 8,450.00 USD | 10,670.00 USD |
| `1D` | `53.70` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 4,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.70` | 15,850,000.00 USD | 0.00 USD | 15,850,000.00 USD | 62,710.00 USD | 15,090.00 USD | 12,040.00 USD |
| `1D` | `53.80` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 283.21 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.80` | 15,760,000.00 USD | 0.00 USD | 15,760,000.00 USD | 97,770.00 USD | 48,300.00 USD | 86,270.00 USD |
| `1D` | `53.90` | 5,480,000.00 USD | 0.00 USD | 5,480,000.00 USD | 3,950.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `53.90` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 110,410.00 USD | 25,310.00 USD | 123,850.00 USD |
| `1D` | `54.00` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 2,770.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.00` | 15,270,000.00 USD | 0.00 USD | 15,270,000.00 USD | 340,500.00 USD | 142,130.00 USD | 210,440.00 USD |
| `1D` | `54.10` | 5,470,000.00 USD | 0.00 USD | 5,470,000.00 USD | 11,980.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.10` | 14,580,000.00 USD | 0.00 USD | 14,580,000.00 USD | 232,410.00 USD | 45,470.00 USD | 138,110.00 USD |
| `1D` | `54.20` | 5,460,000.00 USD | 0.00 USD | 5,460,000.00 USD | 15,320.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.20` | 14,160,000.00 USD | 0.00 USD | 14,160,000.00 USD | 233,240.00 USD | 141,240.00 USD | 133,320.00 USD |
| `1D` | `54.30` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 4,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.30` | 13,660,000.00 USD | 0.00 USD | 13,660,000.00 USD | 243,980.00 USD | 89,080.00 USD | 257,030.00 USD |
| `1D` | `54.40` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 2,900.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `54.40` | 13,070,000.00 USD | 0.00 USD | 13,070,000.00 USD | 319,640.00 USD | 106,460.00 USD | 105,880.00 USD |
| `1D` | `54.50` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 5,000.00 USD | 126.10 USD | 0.00 USD |
| `7D` | `54.50` | 12,530,000.00 USD | 0.00 USD | 12,530,000.00 USD | 170,480.00 USD | 53,460.00 USD | 142,750.00 USD |
| `1D` | `54.60` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 2,740.00 USD | 601.45 USD | 282.35 USD |
| `7D` | `54.60` | 12,170,000.00 USD | 0.00 USD | 12,170,000.00 USD | 106,050.00 USD | 43,430.00 USD | 73,330.00 USD |
| `1D` | `54.70` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 52,430.00 USD | 15,810.00 USD | 52,580.00 USD |
| `7D` | `54.70` | 11,940,000.00 USD | 0.00 USD | 11,940,000.00 USD | 123,370.00 USD | 50,560.00 USD | 172,060.00 USD |
| `1D` | `54.80` | 5,310,000.00 USD | 0.00 USD | 5,310,000.00 USD | 45,490.00 USD | 18,410.00 USD | 27,940.00 USD |
| `7D` | `54.80` | 11,600,000.00 USD | 0.00 USD | 11,600,000.00 USD | 307,360.00 USD | 104,820.00 USD | 156,690.00 USD |
| `1D` | `54.90` | 5,220,000.00 USD | 0.00 USD | 5,220,000.00 USD | 51,230.00 USD | 32,190.00 USD | 9,950.00 USD |
| `7D` | `54.90` | 11,030,000.00 USD | 0.00 USD | 11,030,000.00 USD | 255,130.00 USD | 162,220.00 USD | 276,830.00 USD |
| `1D` | `55.00` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 42,020.00 USD | 24,810.00 USD | 30,380.00 USD |
| `7D` | `55.00` | 10,330,000.00 USD | 0.00 USD | 10,330,000.00 USD | 264,000.00 USD | 81,220.00 USD | 310,900.00 USD |
| `1D` | `55.10` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 44,730.00 USD | 10,460.00 USD | 25,360.00 USD |
| `7D` | `55.10` | 9,680,000.00 USD | 0.00 USD | 9,680,000.00 USD | 362,320.00 USD | 145,730.00 USD | 171,990.00 USD |
| `1D` | `55.20` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 26,190.00 USD | 13,920.00 USD | 10,450.00 USD |
| `7D` | `55.20` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 336,630.00 USD | 177,110.00 USD | 279,820.00 USD |
| `1D` | `55.30` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 9,120.00 USD | 4,380.00 USD | 13,750.00 USD |
| `7D` | `55.30` | 8,210,000.00 USD | 0.00 USD | 8,210,000.00 USD | 365,190.00 USD | 67,310.00 USD | 256,220.00 USD |
| `1D` | `55.40` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 23,020.00 USD | 40,410.00 USD | 14,200.00 USD |
| `7D` | `55.40` | 7,520,000.00 USD | 0.00 USD | 7,520,000.00 USD | 302,780.00 USD | 182,540.00 USD | 223,080.00 USD |
| `1D` | `55.50` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 63,040.00 USD | 21,070.00 USD | 33,580.00 USD |
| `7D` | `55.50` | 6,810,000.00 USD | 0.00 USD | 6,810,000.00 USD | 294,630.00 USD | 169,030.00 USD | 513,930.00 USD |
| `1D` | `55.60` | 4,670,000.00 USD | 0.00 USD | 4,670,000.00 USD | 121,460.00 USD | 35,220.00 USD | 79,850.00 USD |
| `7D` | `55.60` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 423,370.00 USD | 260,600.00 USD | 243,460.00 USD |
| `1D` | `55.70` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 83,760.00 USD | 49,670.00 USD | 41,770.00 USD |
| `7D` | `55.70` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 174,240.00 USD | 26,870.00 USD | 273,340.00 USD |
| `1D` | `55.80` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 131,460.00 USD | 56,300.00 USD | 58,680.00 USD |
| `7D` | `55.80` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 60,840.00 USD | 52,890.00 USD | 143,760.00 USD |
| `1D` | `55.90` | 4,010,000.00 USD | 0.00 USD | 4,010,000.00 USD | 131,660.00 USD | 68,110.00 USD | 126,940.00 USD |
| `7D` | `55.90` | 4,170,000.00 USD | 0.00 USD | 4,170,000.00 USD | 65,400.00 USD | 92,360.00 USD | 234,440.00 USD |
| `1D` | `56.00` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 124,190.00 USD | 62,180.00 USD | 80,670.00 USD |
| `7D` | `56.00` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 162,940.00 USD | 81,400.00 USD | 107,390.00 USD |
| `1D` | `56.10` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 123,860.00 USD | 89,640.00 USD | 52,470.00 USD |
| `7D` | `56.10` | 3,430,000.00 USD | 0.00 USD | 3,430,000.00 USD | 111,340.00 USD | 108,750.00 USD | 46,880.00 USD |
| `1D` | `56.20` | 3,150,000.00 USD | 0.00 USD | 3,150,000.00 USD | 113,060.00 USD | 68,300.00 USD | 108,600.00 USD |
| `7D` | `56.20` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 93,330.00 USD | 80,130.00 USD | 184,830.00 USD |
| `1D` | `56.30` | 2,860,000.00 USD | 0.00 USD | 2,860,000.00 USD | 101,530.00 USD | 39,780.00 USD | 79,600.00 USD |
| `7D` | `56.30` | 2,800,000.00 USD | 0.00 USD | 2,800,000.00 USD | 72,590.00 USD | 125,830.00 USD | 52,430.00 USD |
| `1D` | `56.40` | 2,640,000.00 USD | 0.00 USD | 2,640,000.00 USD | 93,910.00 USD | 72,860.00 USD | 135,500.00 USD |
| `7D` | `56.40` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 142,580.00 USD | 120,740.00 USD | 126,150.00 USD |
| `1D` | `56.50` | 2,340,000.00 USD | 0.00 USD | 2,340,000.00 USD | 64,730.00 USD | 89,990.00 USD | 30,670.00 USD |
| `7D` | `56.50` | 2,160,000.00 USD | 0.00 USD | 2,160,000.00 USD | 26,520.00 USD | 89,320.00 USD | 19,740.00 USD |
| `1D` | `56.60` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 167,360.00 USD | 56,860.00 USD | 86,110.00 USD |
| `7D` | `56.60` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 294,170.00 USD | 94,520.00 USD | 96,750.00 USD |
| `1D` | `56.70` | 1,840,000.00 USD | 0.00 USD | 1,840,000.00 USD | 288,830.00 USD | 105,150.00 USD | 195,830.00 USD |
| `7D` | `56.70` | 1,540,000.00 USD | 0.00 USD | 1,540,000.00 USD | 110,940.00 USD | 104,010.00 USD | 138,660.00 USD |
| `1D` | `56.80` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 181,920.00 USD | 128,160.00 USD | 117,770.00 USD |
| `7D` | `56.80` | 1,190,000.00 USD | 0.00 USD | 1,190,000.00 USD | 153,580.00 USD | 87,050.00 USD | 262,620.00 USD |
| `1D` | `56.90` | 826,620.00 USD | 0.00 USD | 826,620.00 USD | 394,430.00 USD | 134,120.00 USD | 201,350.00 USD |
| `7D` | `56.90` | 683,560.00 USD | 0.00 USD | 683,560.00 USD | 108,440.00 USD | 62,910.00 USD | 93,440.00 USD |
| `1D` | `57.00` | 96,720.00 USD | 0.00 USD | 96,720.00 USD | 24,400.00 USD | 18,420.00 USD | 14,160.00 USD |
| `7D` | `57.00` | 418,770.00 USD | 0.00 USD | 418,770.00 USD | 50,710.00 USD | 107,330.00 USD | 0.00 USD |
| `1D` | `57.10` | 39,740.00 USD | 0.00 USD | 39,740.00 USD | 35,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `57.20` | 3,940.00 USD | 0.00 USD | 3,940.00 USD | 0.00 USD | 0.00 USD | 2,260.00 USD |
| `7D` | `57.20` | 260,720.00 USD | 0.00 USD | 260,720.00 USD | 0.00 USD | 0.00 USD | 3,700.00 USD |
| `7D` | `57.30` | 257,020.00 USD | 0.00 USD | 257,020.00 USD | 0.00 USD | 27,320.00 USD | 3,710.00 USD |
| `7D` | `57.40` | 225,990.00 USD | 0.00 USD | 225,990.00 USD | 0.00 USD | 0.00 USD | 98,630.00 USD |
| `1D` | `57.50` | 1,680.00 USD | 0.00 USD | 1,680.00 USD | 0.00 USD | 0.00 USD | 806.82 USD |
| `7D` | `57.50` | 127,360.00 USD | 0.00 USD | 127,360.00 USD | 0.00 USD | 23,070.00 USD | 68,890.00 USD |
| `7D` | `57.60` | 35,410.00 USD | 0.00 USD | 35,410.00 USD | 0.00 USD | 15,090.00 USD | 0.00 USD |
| `1D` | `57.70` | 873.62 USD | 0.00 USD | 873.62 USD | 0.00 USD | 0.00 USD | 873.62 USD |
| `7D` | `57.80` | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD | 20,310.00 USD | 0.00 USD |
| `7D` | `57.90` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `58.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `58.00` | 10,560.00 USD | 10,560.00 USD | 0.00 USD | 0.00 USD | 10,560.00 USD | 0.00 USD |
| `1D` | `58.20` | 3,100.00 USD | 3,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,100.00 USD |
| `7D` | `58.20` | 171,710.00 USD | 171,710.00 USD | 0.00 USD | 0.00 USD | 15,050.00 USD | 146,100.00 USD |
| `1D` | `58.30` | 154,180.00 USD | 154,180.00 USD | 0.00 USD | 0.00 USD | 46,180.00 USD | 104,890.00 USD |
| `1D` | `58.40` | 333,630.00 USD | 333,630.00 USD | 0.00 USD | 104,980.00 USD | 50,050.00 USD | 24,420.00 USD |
| `7D` | `58.40` | 259,210.00 USD | 259,210.00 USD | 0.00 USD | 33,380.00 USD | 0.00 USD | 54,120.00 USD |
| `1D` | `58.50` | 440,380.00 USD | 440,380.00 USD | 0.00 USD | 48,820.00 USD | 20,920.00 USD | 37,010.00 USD |
| `7D` | `58.50` | 283,740.00 USD | 283,740.00 USD | 0.00 USD | 0.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.70` | 491,550.00 USD | 491,550.00 USD | 0.00 USD | 22,190.00 USD | 8,070.00 USD | 20,910.00 USD |
| `7D` | `58.70` | 388,050.00 USD | 388,050.00 USD | 0.00 USD | 32,230.00 USD | 4,430.00 USD | 67,650.00 USD |
| `1D` | `58.80` | 536,090.00 USD | 536,090.00 USD | 0.00 USD | 8,280.00 USD | 8,760.00 USD | 27,500.00 USD |
| `7D` | `58.80` | 639,180.00 USD | 639,180.00 USD | 0.00 USD | 245,570.00 USD | 0.00 USD | 5,560.00 USD |
| `1D` | `58.90` | 650,530.00 USD | 650,530.00 USD | 0.00 USD | 21,990.00 USD | 80,820.00 USD | 11,630.00 USD |
| `7D` | `58.90` | 677,800.00 USD | 677,800.00 USD | 0.00 USD | 0.00 USD | 35,850.00 USD | 2,770.00 USD |
| `1D` | `59.00` | 871,040.00 USD | 871,040.00 USD | 0.00 USD | 122,800.00 USD | 30,550.00 USD | 67,160.00 USD |
| `7D` | `59.00` | 980,680.00 USD | 980,680.00 USD | 0.00 USD | 186,160.00 USD | 29,720.00 USD | 87,000.00 USD |
| `1D` | `59.10` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 180,920.00 USD | 37,950.00 USD | 139,720.00 USD |
| `7D` | `59.10` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 91,060.00 USD | 43,600.00 USD | 90,180.00 USD |
| `1D` | `59.20` | 1,510,000.00 USD | 1,510,000.00 USD | 0.00 USD | 134,660.00 USD | 58,390.00 USD | 82,970.00 USD |
| `7D` | `59.20` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 153,580.00 USD | 0.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 1,960,000.00 USD | 1,960,000.00 USD | 0.00 USD | 266,690.00 USD | 68,620.00 USD | 121,820.00 USD |
| `7D` | `59.30` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 88,710.00 USD | 65,110.00 USD | 117,760.00 USD |
| `1D` | `59.40` | 2,130,000.00 USD | 2,130,000.00 USD | 0.00 USD | 68,520.00 USD | 51,170.00 USD | 47,220.00 USD |
| `7D` | `59.40` | 2,020,000.00 USD | 2,020,000.00 USD | 0.00 USD | 103,370.00 USD | 69,170.00 USD | 46,100.00 USD |
| `1D` | `59.50` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 77,430.00 USD | 26,350.00 USD | 5,440.00 USD |
| `7D` | `59.50` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 30,480.00 USD | 45,040.00 USD | 7,180.00 USD |
| `1D` | `59.60` | 2,310,000.00 USD | 2,310,000.00 USD | 0.00 USD | 34,730.00 USD | 26,400.00 USD | 12,080.00 USD |
| `7D` | `59.60` | 2,630,000.00 USD | 2,630,000.00 USD | 0.00 USD | 342,080.00 USD | 95,250.00 USD | 86,840.00 USD |
| `1D` | `59.70` | 2,520,000.00 USD | 2,520,000.00 USD | 0.00 USD | 114,860.00 USD | 47,810.00 USD | 42,970.00 USD |
| `7D` | `59.70` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 31,450.00 USD | 181,680.00 USD | 120,070.00 USD |
| `1D` | `59.80` | 2,720,000.00 USD | 2,720,000.00 USD | 0.00 USD | 86,810.00 USD | 51,640.00 USD | 68,210.00 USD |
| `7D` | `59.80` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 126,070.00 USD | 66,860.00 USD | 123,960.00 USD |
| `1D` | `59.90` | 2,910,000.00 USD | 2,910,000.00 USD | 0.00 USD | 55,090.00 USD | 23,890.00 USD | 102,080.00 USD |
| `7D` | `59.90` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 251,510.00 USD | 106,200.00 USD | 39,700.00 USD |
| `1D` | `60.00` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 81,220.00 USD | 93,410.00 USD | 100,060.00 USD |
| `7D` | `60.00` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 161,330.00 USD | 185,420.00 USD | 41,680.00 USD |
| `1D` | `60.10` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 104,900.00 USD | 39,410.00 USD | 38,110.00 USD |
| `7D` | `60.10` | 4,570,000.00 USD | 4,570,000.00 USD | 0.00 USD | 229,390.00 USD | 113,130.00 USD | 158,360.00 USD |
| `1D` | `60.20` | 3,760,000.00 USD | 3,760,000.00 USD | 0.00 USD | 211,970.00 USD | 64,660.00 USD | 117,740.00 USD |
| `7D` | `60.20` | 5,030,000.00 USD | 5,030,000.00 USD | 0.00 USD | 207,990.00 USD | 130,630.00 USD | 123,230.00 USD |
| `1D` | `60.30` | 4,170,000.00 USD | 4,170,000.00 USD | 0.00 USD | 176,210.00 USD | 118,840.00 USD | 114,040.00 USD |
| `7D` | `60.30` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 118,160.00 USD | 90,580.00 USD | 155,610.00 USD |
| `1D` | `60.40` | 4,600,000.00 USD | 4,600,000.00 USD | 0.00 USD | 189,140.00 USD | 113,750.00 USD | 126,570.00 USD |
| `7D` | `60.40` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 89,500.00 USD | 125,690.00 USD | 225,740.00 USD |
| `1D` | `60.50` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 304,030.00 USD | 107,800.00 USD | 192,020.00 USD |
| `7D` | `60.50` | 6,240,000.00 USD | 6,240,000.00 USD | 0.00 USD | 158,260.00 USD | 87,030.00 USD | 161,660.00 USD |
| `1D` | `60.60` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 169,220.00 USD | 62,740.00 USD | 52,850.00 USD |
| `7D` | `60.60` | 6,810,000.00 USD | 6,810,000.00 USD | 0.00 USD | 274,700.00 USD | 102,070.00 USD | 186,860.00 USD |
| `1D` | `60.70` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 147,130.00 USD | 49,120.00 USD | 126,600.00 USD |
| `7D` | `60.70` | 7,100,000.00 USD | 7,100,000.00 USD | 0.00 USD | 177,510.00 USD | 59,630.00 USD | 62,340.00 USD |
| `1D` | `60.80` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 84,330.00 USD | 21,790.00 USD | 74,390.00 USD |
| `7D` | `60.80` | 7,310,000.00 USD | 7,310,000.00 USD | 0.00 USD | 49,070.00 USD | 79,230.00 USD | 73,940.00 USD |
| `1D` | `60.90` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 63,100.00 USD | 20,750.00 USD | 33,340.00 USD |
| `7D` | `60.90` | 7,600,000.00 USD | 7,600,000.00 USD | 0.00 USD | 143,640.00 USD | 50,770.00 USD | 95,160.00 USD |
| `1D` | `61.00` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 27,820.00 USD | 9,760.00 USD | 44,170.00 USD |
| `7D` | `61.00` | 7,750,000.00 USD | 7,750,000.00 USD | 0.00 USD | 96,210.00 USD | 48,220.00 USD | 5,370.00 USD |
| `1D` | `61.10` | 6,190,000.00 USD | 6,190,000.00 USD | 0.00 USD | 6,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `61.10` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 29,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `61.20` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 30,990.00 USD | 26,500.00 USD | 42,930.00 USD |
| `7D` | `61.20` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 81,590.00 USD | 74,350.00 USD | 20,130.00 USD |
| `1D` | `61.30` | 6,330,000.00 USD | 6,330,000.00 USD | 0.00 USD | 22,660.00 USD | 9,170.00 USD | 2,270.00 USD |
| `7D` | `61.30` | 8,090,000.00 USD | 8,090,000.00 USD | 0.00 USD | 51,890.00 USD | 36,170.00 USD | 55,130.00 USD |
| `1D` | `61.40` | 6,410,000.00 USD | 6,410,000.00 USD | 0.00 USD | 47,280.00 USD | 14,720.00 USD | 18,950.00 USD |
| `7D` | `61.40` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 84,080.00 USD | 41,800.00 USD | 24,650.00 USD |
| `1D` | `61.50` | 6,530,000.00 USD | 6,530,000.00 USD | 0.00 USD | 55,570.00 USD | 34,710.00 USD | 36,130.00 USD |
| `7D` | `61.50` | 8,340,000.00 USD | 8,340,000.00 USD | 0.00 USD | 22,670.00 USD | 34,770.00 USD | 35,770.00 USD |
| `1D` | `61.60` | 6,630,000.00 USD | 6,630,000.00 USD | 0.00 USD | 30,310.00 USD | 29,330.00 USD | 34,230.00 USD |
| `7D` | `61.60` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 55,000.00 USD | 63,390.00 USD | 132,550.00 USD |
| `1D` | `61.70` | 6,890,000.00 USD | 6,890,000.00 USD | 0.00 USD | 143,900.00 USD | 35,660.00 USD | 85,110.00 USD |
| `7D` | `61.70` | 8,820,000.00 USD | 8,820,000.00 USD | 0.00 USD | 98,580.00 USD | 15,950.00 USD | 114,970.00 USD |
| `1D` | `61.80` | 7,000,000.00 USD | 7,000,000.00 USD | 0.00 USD | 71,680.00 USD | 18,690.00 USD | 14,030.00 USD |
| `7D` | `61.80` | 9,160,000.00 USD | 9,160,000.00 USD | 0.00 USD | 180,840.00 USD | 68,030.00 USD | 92,510.00 USD |
| `1D` | `61.90` | 7,120,000.00 USD | 7,120,000.00 USD | 0.00 USD | 59,440.00 USD | 11,940.00 USD | 47,010.00 USD |
| `7D` | `61.90` | 9,310,000.00 USD | 9,310,000.00 USD | 0.00 USD | 79,630.00 USD | 35,500.00 USD | 35,860.00 USD |
| `1D` | `62.00` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 24,960.00 USD | 1,560.00 USD | 13,280.00 USD |
| `7D` | `62.00` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 56,020.00 USD | 13,260.00 USD | 49,920.00 USD |
| `1D` | `62.10` | 7,170,000.00 USD | 7,170,000.00 USD | 0.00 USD | 13,440.00 USD | 945.47 USD | 2,230.00 USD |
| `7D` | `62.10` | 9,490,000.00 USD | 9,490,000.00 USD | 0.00 USD | 34,630.00 USD | 12,820.00 USD | 13,950.00 USD |
| `1D` | `62.20` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 4,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 9,610,000.00 USD | 9,610,000.00 USD | 0.00 USD | 39,180.00 USD | 34,620.00 USD | 41,360.00 USD |
| `1D` | `62.30` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 2,650.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.30` | 9,760,000.00 USD | 9,760,000.00 USD | 0.00 USD | 38,690.00 USD | 23,450.00 USD | 85,980.00 USD |
| `1D` | `62.40` | 7,180,000.00 USD | 7,180,000.00 USD | 0.00 USD | 2,700.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.40` | 9,890,000.00 USD | 9,890,000.00 USD | 0.00 USD | 78,840.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `62.50` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 4,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.50` | 9,980,000.00 USD | 9,980,000.00 USD | 0.00 USD | 47,530.00 USD | 14,320.00 USD | 26,310.00 USD |
| `1D` | `62.60` | 7,190,000.00 USD | 7,190,000.00 USD | 0.00 USD | 2,090.00 USD | 0.00 USD | 112.94 USD |
| `7D` | `62.60` | 10,050,000.00 USD | 10,050,000.00 USD | 0.00 USD | 35,940.00 USD | 7,100.00 USD | 27,730.00 USD |
| `1D` | `62.70` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 20,030.00 USD | 4,920.00 USD | 18,590.00 USD |
| `7D` | `62.70` | 10,130,000.00 USD | 10,130,000.00 USD | 0.00 USD | 22,860.00 USD | 12,490.00 USD | 47,090.00 USD |
| `1D` | `62.80` | 7,270,000.00 USD | 7,270,000.00 USD | 0.00 USD | 17,470.00 USD | 7,010.00 USD | 11,140.00 USD |
| `7D` | `62.80` | 10,280,000.00 USD | 10,280,000.00 USD | 0.00 USD | 74,100.00 USD | 28,960.00 USD | 45,150.00 USD |
| `1D` | `62.90` | 7,290,000.00 USD | 7,290,000.00 USD | 0.00 USD | 8,780.00 USD | 10,210.00 USD | 1,800.00 USD |
| `7D` | `62.90` | 10,370,000.00 USD | 10,370,000.00 USD | 0.00 USD | 31,770.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `63.00` | 7,320,000.00 USD | 7,320,000.00 USD | 0.00 USD | 10,350.00 USD | 7,320.00 USD | 10,070.00 USD |
| `7D` | `63.00` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 35,710.00 USD | 12,240.00 USD | 17,650.00 USD |
| `1D` | `63.10` | 7,340,000.00 USD | 7,340,000.00 USD | 0.00 USD | 12,260.00 USD | 4,070.00 USD | 9,280.00 USD |
| `7D` | `63.10` | 10,480,000.00 USD | 10,480,000.00 USD | 0.00 USD | 11,870.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `63.20` | 7,350,000.00 USD | 7,350,000.00 USD | 0.00 USD | 3,530.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `63.30` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 5,160.00 USD | 4,550.00 USD | 2,630.00 USD |
| `7D` | `63.30` | 10,520,000.00 USD | 10,520,000.00 USD | 0.00 USD | 20,280.00 USD | 11,500.00 USD | 9,730.00 USD |
| `1D` | `63.40` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 1,910.00 USD | 931.11 USD | 5,390.00 USD |
| `7D` | `63.40` | 10,540,000.00 USD | 10,540,000.00 USD | 0.00 USD | 13,660.00 USD | 656.00 USD | 9,790.00 USD |
| `1D` | `63.50` | 7,400,000.00 USD | 7,400,000.00 USD | 0.00 USD | 8,930.00 USD | 14,750.00 USD | 5,670.00 USD |
| `7D` | `63.50` | 10,570,000.00 USD | 10,570,000.00 USD | 0.00 USD | 5,690.00 USD | 15,240.00 USD | 4,760.00 USD |
| `1D` | `63.60` | 7,430,000.00 USD | 7,430,000.00 USD | 0.00 USD | 18,400.00 USD | 3,660.00 USD | 10,020.00 USD |
| `7D` | `63.60` | 10,650,000.00 USD | 10,650,000.00 USD | 0.00 USD | 52,430.00 USD | 13,690.00 USD | 11,640.00 USD |
| `1D` | `63.70` | 7,510,000.00 USD | 7,510,000.00 USD | 0.00 USD | 38,080.00 USD | 11,010.00 USD | 31,870.00 USD |
| `7D` | `63.70` | 10,710,000.00 USD | 10,710,000.00 USD | 0.00 USD | 20,540.00 USD | 18,810.00 USD | 21,910.00 USD |
| `1D` | `63.80` | 7,550,000.00 USD | 7,550,000.00 USD | 0.00 USD | 21,730.00 USD | 10,990.00 USD | 11,940.00 USD |
| `7D` | `63.80` | 10,770,000.00 USD | 10,770,000.00 USD | 0.00 USD | 33,340.00 USD | 4,340.00 USD | 25,270.00 USD |
| `1D` | `63.90` | 7,630,000.00 USD | 7,630,000.00 USD | 0.00 USD | 38,980.00 USD | 14,090.00 USD | 23,220.00 USD |
| `7D` | `63.90` | 10,800,000.00 USD | 10,800,000.00 USD | 0.00 USD | 6,490.00 USD | 12,370.00 USD | 8,770.00 USD |
| `1D` | `64.00` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 5,540.00 USD | 10,620.00 USD | 158.33 USD |
| `7D` | `64.00` | 10,830,000.00 USD | 10,830,000.00 USD | 0.00 USD | 10,140.00 USD | 10,630.00 USD | 7,650.00 USD |
| `1D` | `64.10` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 7,160.00 USD | 8,120.00 USD | 9,920.00 USD |
| `7D` | `64.10` | 10,860,000.00 USD | 10,860,000.00 USD | 0.00 USD | 13,040.00 USD | 667.05 USD | 18,540.00 USD |
| `1D` | `64.20` | 7,700,000.00 USD | 7,700,000.00 USD | 0.00 USD | 10,610.00 USD | 6,450.00 USD | 10,130.00 USD |
| `7D` | `64.20` | 10,920,000.00 USD | 10,920,000.00 USD | 0.00 USD | 44,990.00 USD | 6,760.00 USD | 8,360.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 14:10:00 UTC - 2026-10-29 14:15:00 UTC` |
| `15m` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 14:00:00 UTC - 2026-10-29 14:15:00 UTC` |
| `1h` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 14:00:00 UTC - 2026-10-29 15:00:00 UTC` |
| `4h` | `BALANCED` | 0.00 USD | 1,340.00 USD | 1,340.00 USD | 1,340.00 USD | `1` | `2026-10-29 12:00:00 UTC - 2026-10-29 16:00:00 UTC` |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `455.49M` | Total OI Tokens: `7,866,822.2 LTC`
  * 1h OI Change: `-0.65%` | 4h OI Change: `+1.39%` | 24h OI Change: `+0.22%`
  * Exchange Breakdown: Binance=`81.76M` | Bybit=`69.32M` | OKX=`34.85M` | Hyperliquid=`22.85M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `16.51K` | Last 24h: `6.52K` | Last 3d: `60.13K` | Last 7d: `92.20K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0094%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0100%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `37.54%` | `62.46%` | `0.60` | 8,400,000.00 USD |
| `15M` | `Binance` | `42.31%` | `57.69%` | `0.73` | 2,910,000.00 USD |
| `15M` | `OKX` | `41.09%` | `58.91%` | `0.70` | 725,710.00 USD |
| `15M` | `Bybit` | `43.81%` | `56.19%` | `0.78` | 511,910.00 USD |
| `15M` | `KuCoin` | `45.77%` | `54.23%` | `0.84` | 58,350.00 USD |
| `15M` | `Gate` | `28.56%` | `71.44%` | `0.40` | 2,480,000.00 USD |
| `15M` | `Bitget` | `27.53%` | `72.47%` | `0.38` | 500,640.00 USD |
| `15M` | `BingX` | `13.99%` | `86.01%` | `0.16` | 116,080.00 USD |
| `15M` | `MEXC` | `43.52%` | `56.48%` | `0.77` | 59,330.00 USD |
| `15M` | `Bitunix` | `33.54%` | `66.46%` | `0.50` | 90,090.00 USD |
| `15M` | `Hyperliquid` | `35.04%` | `64.96%` | `0.54` | 120,880.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.87%` | `50.13%` | `0.99` | 428,280.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `49.79%` | `50.21%` | `0.99` | 265,470.00 USD |
| `15M` | `HTX` | `41.12%` | `58.88%` | `0.70` | 18,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `51.61%` | `48.39%` | `1.07` | 78,450.00 USD |
| `15M` | `Aster` | `53.69%` | `46.31%` | `1.16` | 28,500.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `39.26%` | `60.74%` | `0.65` | 11,970.00 USD |
| `15M` | `Whale Positions` | `42.31%` | `57.69%` | `0.73` | 2,910,000.00 USD |
| `15M` | `Global Accounts` | `37.54%` | `62.46%` | `0.60` | 8,400,000.00 USD |
| `1H` | `LTC` | `47.81%` | `52.19%` | `0.92` | 26,330,000.00 USD |
| `1H` | `Binance` | `49.77%` | `50.23%` | `0.99` | 7,010,000.00 USD |
| `1H` | `OKX` | `46.98%` | `53.02%` | `0.89` | 2,090,000.00 USD |
| `1H` | `Bybit` | `55.52%` | `44.48%` | `1.25` | 1,230,000.00 USD |
| `1H` | `KuCoin` | `41.11%` | `58.89%` | `0.70` | 229,790.00 USD |
| `1H` | `Gate` | `41.26%` | `58.74%` | `0.70` | 526,800.00 USD |
| `1H` | `Bitget` | `46.5%` | `53.5%` | `0.87` | 796,030.00 USD |
| `1H` | `BingX` | `33.73%` | `66.27%` | `0.51` | 885,150.00 USD |
| `1H` | `MEXC` | `50.96%` | `49.04%` | `1.04` | 11,020,000.00 USD |
| `1H` | `Bitunix` | `43.9%` | `56.1%` | `0.78` | 872,220.00 USD |
| `1H` | `Hyperliquid` | `23.75%` | `76.25%` | `0.31` | 247,260.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `41.72%` | `58.28%` | `0.72` | 560,160.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `11.86%` | `88.14%` | `0.13` | 702,740.00 USD |
| `1H` | `HTX` | `39.75%` | `60.25%` | `0.66` | 7,060.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `70.41%` | `29.59%` | `2.38` | 90,660.00 USD |
| `1H` | `Aster` | `59.31%` | `40.69%` | `1.46` | 21,600.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `8.54%` | `91.46%` | `0.09` | 49,210.00 USD |
| `1H` | `Whale Positions` | `49.77%` | `50.23%` | `0.99` | 7,010,000.00 USD |
| `1H` | `Global Accounts` | `47.81%` | `52.19%` | `0.92` | 26,330,000.00 USD |
| `4H` | `LTC` | `48.32%` | `51.68%` | `0.93` | 20,430,000.00 USD |
| `4H` | `Binance` | `45.79%` | `54.21%` | `0.84` | 6,550,000.00 USD |
| `4H` | `OKX` | `52.66%` | `47.34%` | `1.11` | 1,750,000.00 USD |
| `4H` | `Bybit` | `41.61%` | `58.39%` | `0.71` | 911,800.00 USD |
| `4H` | `KuCoin` | `49.32%` | `50.68%` | `0.97` | 321,340.00 USD |
| `4H` | `Gate` | `29.57%` | `70.43%` | `0.42` | 2,780,000.00 USD |
| `4H` | `Bitget` | `29.71%` | `70.29%` | `0.42` | 629,940.00 USD |
| `4H` | `BingX` | `24.83%` | `75.17%` | `0.33` | 1,130,000.00 USD |
| `4H` | `MEXC` | `87.68%` | `12.32%` | `7.12` | 883,270.00 USD |
| `4H` | `Bitunix` | `46.73%` | `53.27%` | `0.88` | 208,000.00 USD |
| `4H` | `Hyperliquid` | `53.27%` | `46.73%` | `1.14` | 352,920.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.42%` | `49.58%` | `1.02` | 2,810,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `86.4%` | `13.6%` | `6.35` | 1,500,000.00 USD |
| `4H` | `HTX` | `49.38%` | `50.62%` | `0.98` | 227,880.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `61.24%` | `38.76%` | `1.58` | 226,680.00 USD |
| `4H` | `Aster` | `69.14%` | `30.86%` | `2.24` | 55,450.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `64.83%` | `35.17%` | `1.84` | 92,310.00 USD |
| `4H` | `Whale Positions` | `45.79%` | `54.21%` | `0.84` | 6,550,000.00 USD |
| `4H` | `Global Accounts` | `48.32%` | `51.68%` | `0.93` | 20,430,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `58.11` | `58.06` | `58.11` | `58.16` | `57.91` | 1,017,513.96 USD | 419,303.39 USD | 598,210.57 USD | -178,907.17 USD | `-17.58%` | `4B / 5S` |
| `0:00 UTC` | `57.97` | `57.93` | `57.97` | `58.03` | `57.83` | 727,506.52 USD | 481,658.23 USD | 245,848.29 USD | 235,809.94 USD | `+32.41%` | `5B / 1S` |
| `5:00 UTC` | `58.05` | `58.06` | `58.05` | `58.14` | `57.97` | 604,868.16 USD | 360,734.89 USD | 244,133.27 USD | 116,601.61 USD | `+19.28%` | `2B / 1S` |
| `0:00 UTC` | `58.05` | `58.17` | `58.05` | `58.34` | `58.00` | 1,031,965.27 USD | 611,895.14 USD | 420,070.14 USD | 191,825.00 USD | `+18.59%` | `11B / 2S` |
| `5:00 UTC` | `58.20` | `58.14` | `58.20` | `58.25` | `58.02` | 494,847.50 USD | 187,896.97 USD | 306,950.53 USD | -119,053.55 USD | `-24.06%` | `1B / 4S` |
| `0:00 UTC` | `58.30` | `58.18` | `58.30` | `58.34` | `58.00` | 607,668.52 USD | 285,031.06 USD | 322,637.45 USD | -37,606.39 USD | `-6.19%` | `3B / 6S` |
| `5:00 UTC` | `58.20` | `58.14` | `58.20` | `58.30` | `57.98` | 622,995.64 USD | 392,924.83 USD | 230,070.80 USD | 162,854.03 USD | `+26.14%` | `10B / 4S` |
| `0:00 UTC` | `57.86` | `57.86` | `57.86` | `58.08` | `57.64` | 643,593.97 USD | 302,055.62 USD | 341,538.35 USD | -39,482.73 USD | `-6.13%` | `4B / 6S` |
| `5:00 UTC` | `57.91` | `57.90` | `57.91` | `58.08` | `57.78` | 613,593.73 USD | 319,994.09 USD | 293,599.64 USD | 26,394.46 USD | `+4.30%` | `5B / 4S` |
| `0:00 UTC` | `57.97` | `57.97` | `57.97` | `58.06` | `57.89` | 346,305.83 USD | 187,646.24 USD | 158,659.59 USD | 28,986.64 USD | `+8.37%` | `3B / 2S` |

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
| `5m` | -17,600.00 USD | 57,100.00 USD | **`ACCUMULATION`** |
| `15m` | -58,420.00 USD | 105,850.00 USD | **`ACCUMULATION`** |
| `30m` | -87,080.00 USD | 167,650.00 USD | **`ACCUMULATION`** |
| `1h` | -332,610.00 USD | -62,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -73,240.00 USD | 1,570,000.00 USD | **`ACCUMULATION`** |
| `4h` | 536,040.00 USD | 2,490,000.00 USD | **`ACCUMULATION`** |
| `6h` | 675,860.00 USD | 2,870,000.00 USD | **`ACCUMULATION`** |
| `8h` | 769,680.00 USD | 1,910,000.00 USD | **`ACCUMULATION`** |
| `12h` | 333,120.00 USD | 987,980.00 USD | **`ACCUMULATION`** |
| `24h` | 786,830.00 USD | -681,870.00 USD | **`ACCUMULATION`** |
| `1w` | 2,540,000.00 USD | -23,700,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,380,000.00 USD | -199,160,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-17.60K` | 15m=`-58.42K` | 1h=`-332.61K` | 24h=`+786.83K`
* Futures Capital Netflows: 5m=`+57.10K` | 15m=`+105.85K` | 1h=`-62.00K` | 24h=`-681.87K`
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
  * `2026-10-29 19:41:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:40:49 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-29 19:20:49 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-29 19:09:49 IST`: [youtube.com/ecbeuro] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [zerohedge.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [dol.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:49:49 IST`: [bea.gov] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-29 19:48:49 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-29 16:50:49 IST`: [marctomarket.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [ecb.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-29 15:50:49 IST`: [bankofengland.co.uk] - (Sentiment: `Neutral`)


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
  * Execution Entry: `56.74` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `55.96` (Risk Distance: `0.7729` pts)
  * +2.5R Take Profit: `58.67`
  * Mathematical Lot Sizing: **`12.93 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `58.27` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `59.05` (Risk Distance: `0.7729` pts)
  * +2.5R Take Profit: `56.34`
  * Mathematical Lot Sizing: **`12.93 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`58.45`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
