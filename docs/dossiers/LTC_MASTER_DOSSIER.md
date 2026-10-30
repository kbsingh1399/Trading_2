# 🏛️ SOVEREIGN CANDIDATE DOSSIER: LTC
**Canonical Key**: `LTC` | **Broker Instrument**: `LTCUSD.pi` | **Asset Class**: `Crypto PoW`
**Timestamp**: `2026-10-30 16:55:01 IST` (`2026-10-30 11:25:01 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `55.16` | **Live Ask Quote**: `55.45` | **Mid Price**: `55.30`
- **Spread Points**: `300.00` | **Spread BPS**: `54.24 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `55.30` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.00` (Volatility Regime: `HIGH_EXPANSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `55.69` | Lower -3.00σ Band: `54.92`
  * Upper +2.51σ Band: `55.61` | Lower -2.51σ Band: `55.00`
  * Upper +2.01σ Band: `55.54` | Lower -2.01σ Band: `55.07`
  * Upper +2.00σ Band: `55.53` | Lower -2.00σ Band: `55.08`
  * Upper +1.28σ Band: `55.46` | Lower -1.28σ Band: `55.15`
  * Upper +1.00σ Band: `55.42` | Lower -1.00σ Band: `55.19`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`55.30` | EMA-20=`55.30` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`55.30` (Slope: `+0.0000`) | EMA-100=`55.30`
  * Institutional Anchors: EMA-144=`55.30` | EMA-200=`55.30` (Slope: `+0.0000`) | EMA-233=`55.30`
- **Range Boundaries**: 24H High=`55.86` | 24H Low=`54.75` | Weekly High=`56.41` | Weekly Low=`54.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `56.07` (Distance: `-1.38%`)
  * Point of Control (POC) = `55.30` (Distance: `-0.02%`)
  * Value Area Low (VAL) = `54.64` (Distance: `+1.21%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`58.40` | POC=`57.72` | VAL=`56.83`
  * Prior Day Extremes: PDH=`59.52` | PDL=`54.18` | PDC=`54.46`
  * Monday Range Blueprint: High=`57.03` | Mid=`56.40` | Low=`55.77`
  * Developing Weekly Value Area: Weekly VAH=`58.39` | Weekly POC=`56.43` | Weekly VAL=`55.83`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`56.03` | Low=`52.64`
  * London Session (08:00-16:00 UTC): High=`56.23` | Low=`54.91`
  * New York Session (13:00-21:00 UTC): High=`55.68` | Low=`54.91`
  * Initial Balance (First Hour): IB High=`56.22` | IB Low=`55.73`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `55.08` - `55.53`
  * Optimal Trade Entry (OTE 0.705): `55.42`
  * Structural Invalidation Anchor (0.786): `55.75`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `55.79` | `55.88` | `55.65` | `55.69` | `4,930` | 275,051.10 USD | 59,264.04 USD | `+21.55%` | -6,686,558.96 USD | `+0.63` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `55.69` | `55.69` | `55.51` | `55.54` | `2,861` | 159,026.70 USD | -8,119.76 USD | `-5.11%` | -6,694,678.72 USD | `+0.27` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `55.54` | `55.56` | `55.52` | `55.53` | `834` | 46,308.79 USD | 3,512.68 USD | `+7.59%` | -6,691,166.04 USD | `+0.32` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `15m` | `55.50` | `55.76` | `55.46` | `55.69` | `12,473` | 693,956.44 USD | 210,975.35 USD | `+30.40%` | -6,140,870.98 USD | `+1.42` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `55.70` | `55.79` | `55.41` | `55.79` | `22,951` | 1,274,778.93 USD | -604,952.03 USD | `-47.46%` | -6,745,823.00 USD | `-2.47` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `55.79` | `55.88` | `55.51` | `55.53` | `8,625` | 480,386.59 USD | 54,656.96 USD | `+11.38%` | -6,691,166.04 USD | `+0.58` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `55.54` | `55.70` | `55.26` | `55.41` | `38,786` | 2,150,474.73 USD | -475,444.38 USD | `-22.11%` | -6,079,275.42 USD | `-0.18` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `55.41` | `55.79` | `55.11` | `55.79` | `78,766` | 4,368,598.06 USD | -793,797.55 USD | `-18.17%` | -6,873,072.97 USD | `-0.53` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `55.79` | `55.88` | `55.51` | `55.53` | `8,625` | 480,386.59 USD | 54,656.96 USD | `+11.38%` | -6,818,416.00 USD | `+0.51` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.11` | `55.53` | `174,400` | 9,686,325.59 USD | -1,244,090.44 USD | `-12.84%` | -6,818,416.00 USD | `-0.09` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `58.63` | `58.93` | `57.43` | `57.98` | `235,291` | 13,693,566.61 USD | 139,286.56 USD | `+1.02%` | 387,872.12 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `57.98` | `58.01` | `54.17` | `54.92` | `766,928` | 42,616,057.42 USD | -3,264,040.91 USD | `-7.66%` | -2,876,168.80 USD | `-1.41` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `54.92` | `56.26` | `52.77` | `56.25` | `545,405` | 29,622,433.22 USD | -2,178,516.18 USD | `-7.35%` | -5,054,684.98 USD | `-0.61` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `56.25` | `56.47` | `55.72` | `55.97` | `202,255` | 11,356,305.33 USD | -519,640.59 USD | `-4.58%` | -5,574,325.57 USD | `+0.43` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `55.96` | `55.99` | `55.11` | `55.53` | `174,400` | 9,686,325.59 USD | -1,244,090.44 USD | `-12.84%` | -6,818,416.00 USD | `-0.09` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`55.30`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `MID` | Regular L2 Book | - | - | - | Interbank L2 | 0.00% | Interbank |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1073` | `0xeadc...9d55` | `LONG` | 2,024,650.83 USD | `36,463.77` | `52.78` | `55.49` | `0.000000` | 99,974.88 USD | `+4.94%` | `10X Cross` |
| `1083` | `0x9aa5...58af` | `SHORT` | 2,008,438.42 USD | `36,177.65` | `71.22` | `55.49` | `299.39` | 568,048.25 USD | `+28.28%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `57.58` | 5,362.91 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 5.36K USD at 57.5790 USD [API] | `2026-10-29 18:28:11` |
| `ANNOUNCEMENT` | `INFO` | `57.58` | 7,508.12 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.5820 USD [API] | `2026-10-29 18:28:11` |
| `ANNOUNCEMENT` | `INFO` | `57.48` | 7,508.30 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 57.4820 USD [API] | `2026-10-29 18:31:51` |
| `ANNOUNCEMENT` | `INFO` | `58.07` | 7,508.58 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale BUY: 7.51K USD at 58.0710 USD [API] | `2026-10-29 19:33:24` |
| `ANNOUNCEMENT` | `INFO` | `56.72` | 6,072.76 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 6.07K USD at 56.7230 USD [API] | `2026-10-29 20:33:49` |
| `ANNOUNCEMENT` | `INFO` | `56.72` | 7,508.42 USD | `-` | `NEWS_INTEL` | `-` | #LTC Whale SELL: 7.51K USD at 56.7230 USD [API] | `2026-10-29 20:33:49` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`56.49` (Vol: 204,200.00 USD, Dist: `+1.88%`) | Long MP=`54.13` (Vol: 153,300.00 USD, Dist: `--2.37%`)
  * 48H Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 3D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
  * 7D Horizon: Short MP=`59.00` (Vol: 327,300.00 USD, Dist: `+6.40%`) | Long MP=`54.12` (Vol: 153,300.00 USD, Dist: `--2.41%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `11.35` | 136.20 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.25` | 122.50 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `12.75` | 2,560.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.15` | 2,220.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `13.65` | 150.15 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `14.95` | 2,250.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `17.45` | 16,230.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.15` | 403.66 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `18.25` | 2,190.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.05` | 3,590.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `19.45` | 2,010.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `20.75` | 4,480.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `21.05` | 1,260.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.25` | 358.89 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `22.65` | 961.04 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.35` | 647.03 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.75` | 375.73 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `23.85` | 7,220.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `24.65` | 113,020.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.25` | 277,980.00 USD | 2,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.35` | 173.39 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.55` | 50,740.00 USD | 2,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.75` | 189.52 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `25.95` | 374.20 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.05` | 5,510.00 USD | 2,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.15` | 3,210.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.55` | 272.75 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `27.95` | 173.85 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `28.55` | 8,560.00 USD | 2,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.15` | 755.28 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `29.75` | 297,500.00 USD | 2,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.05` | 218.46 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.55` | 152.75 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.65` | 1,540.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `30.95` | 538.53 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.15` | 27,840.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.55` | 1,060.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.65` | 4,640.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.85` | 2,870.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `31.95` | 125.24 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.15` | 450.10 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.25` | 5,610.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.35` | 172.10 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.65` | 653.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.75` | 3,750.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `32.95` | 32,950.00 USD | 2,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.25` | 6,210.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `33.65` | 257.76 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.05` | 182.85 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.15` | 126.70 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.45` | 65,890.00 USD | 2,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.65` | 3,240.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `34.95` | 4,670.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.05` | 166.49 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `35.55` | 423.76 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.05` | 314.72 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.35` | 3,020.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.45` | 708.59 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.55` | 2,990.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.75` | 101.80 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.85` | 147.03 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `36.95` | 960.70 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.05` | 1,050.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.15` | 438.74 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.35` | 9,260.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.55` | 3,530.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.75` | 377.50 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.85` | 6,540.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `37.95` | 446.67 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.25` | 695.38 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.35` | 847.54 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.45` | 2,400.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.55` | 993.82 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.65` | 4,280.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.75` | 1,040.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `38.95` | 3,700.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.05` | 664,760.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.15` | 570.02 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.35` | 264.83 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.55` | 1,030.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.65` | 5,900.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.75` | 1,180.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `39.85` | 5,390.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.05` | 2,160.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.25` | 1,000.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.45` | 1,010.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.55` | 133.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.65` | 274.39 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.85` | 6,340.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `40.95` | 816.13 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.05` | 727.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.25` | 14,850.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.45` | 644.96 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.65` | 9,160.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.85` | 3,720.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `41.95` | 299.10 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.05` | 201.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.15` | 64,190.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.25` | 35,410.00 USD | 1,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.55` | 339.97 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.65` | 1,570.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.85` | 5,800.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `42.95` | 2,000.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.05` | 9,080.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.15` | 1,580.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.25` | 121,210.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.35` | 5,700.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.45` | 710.84 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.55` | 5,610.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.65` | 426.02 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.75` | 24,460.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `43.85` | 801.14 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.15` | 2,380.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.25` | 1,330.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.35` | 84,440.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.55` | 842.44 USD | 948,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.65` | 1,340.00 USD | 947,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.75` | 4,230.00 USD | 946,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.85` | 134.55 USD | 942,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `44.95` | 2,790.00 USD | 942,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.05` | 4,830.00 USD | 939,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.15` | 8,710.00 USD | 934,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.25` | 3,180.00 USD | 925,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.35` | 2,180.00 USD | 922,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.45` | 23,940.00 USD | 920,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.55` | 12,060.00 USD | 896,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.65` | 42,180.00 USD | 884,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `45.95` | 30,970.00 USD | 842,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.05` | 706.41 USD | 811,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.15` | 265.82 USD | 810,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.35` | 22,820.00 USD | 810,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.55` | 52,170.00 USD | 787,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.65` | 2,390.00 USD | 735,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.75` | 1,590.00 USD | 732,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.85` | 358.40 USD | 731,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `46.95` | 158.22 USD | 730,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.05` | 2,140.00 USD | 730,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.15` | 1,980.00 USD | 728,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.25` | 9,030.00 USD | 726,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.35` | 43,920.00 USD | 717,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.45` | 2,590.00 USD | 673,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.55` | 4,450.00 USD | 671,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.75` | 47,750.00 USD | 666,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `47.95` | 7,890.00 USD | 618,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.05` | 381.04 USD | 611,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.10` | 8,490,000.00 USD | 8,490,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.15` | 1,690.00 USD | 610,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.20` | 8,480,000.00 USD | 8,480,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.25` | 110.49 USD | 608,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.40` | 8,470,000.00 USD | 8,470,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.55` | 2,030.00 USD | 608,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.60` | 8,470,000.00 USD | 8,470,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.65` | 273.90 USD | 606,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `48.75` | 333.94 USD | 606,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.80` | 8,470,000.00 USD | 8,470,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.85` | 1,890.00 USD | 606,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `48.90` | 8,460,000.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `48.95` | 252.58 USD | 604,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.05` | 1,580.00 USD | 604,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `49.15` | 5,740.00 USD | 602,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.30` | 8,460,000.00 USD | 8,460,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.35` | 5,230.00 USD | 596,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.40` | 8,430,000.00 USD | 8,430,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.45` | 419.34 USD | 591,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `49.50` | 8,420,000.00 USD | 8,420,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.55` | 18,010.00 USD | 591,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.60` | 4,570,000.00 USD | 4,570,000.00 USD | 5,570.00 USD | 14,890.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.60` | 8,410,000.00 USD | 8,410,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.65` | 73,260.00 USD | 573,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.70` | 4,530,000.00 USD | 4,530,000.00 USD | 12,650.00 USD | 3,970.00 USD | 8,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.70` | 8,390,000.00 USD | 8,390,000.00 USD | 12,090.00 USD | 0.00 USD | 13,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.75` | 20,390.00 USD | 499,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `49.80` | 4,500,000.00 USD | 4,500,000.00 USD | 6,420.00 USD | 11,200.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.80` | 8,370,000.00 USD | 8,370,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `49.90` | 4,460,000.00 USD | 4,460,000.00 USD | 24,520.00 USD | 20,290.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `49.90` | 8,350,000.00 USD | 8,350,000.00 USD | 45,030.00 USD | 19,560.00 USD | 10,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `49.95` | 19,920.00 USD | 479,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.00` | 4,390,000.00 USD | 4,390,000.00 USD | 21,740.00 USD | 32,170.00 USD | 47,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.00` | 8,270,000.00 USD | 8,270,000.00 USD | 29,070.00 USD | 39,440.00 USD | 25,110.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.05` | 1,820.00 USD | 459,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.10` | 4,290,000.00 USD | 4,290,000.00 USD | 7,310.00 USD | 11,600.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.10` | 8,180,000.00 USD | 8,180,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.20` | 4,260,000.00 USD | 4,260,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.20` | 8,170,000.00 USD | 8,170,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.25` | 102.51 USD | 457,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.30` | 4,260,000.00 USD | 4,260,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.30` | 8,120,000.00 USD | 8,120,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.35` | 1,140.00 USD | 457,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.40` | 4,250,000.00 USD | 4,250,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.40` | 8,090,000.00 USD | 8,090,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.45` | 4,720.00 USD | 456,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.50` | 4,230,000.00 USD | 4,230,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.50` | 8,000,000.00 USD | 8,000,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.55` | 84,100.00 USD | 451,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.60` | 4,200,000.00 USD | 4,200,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.60` | 7,920,000.00 USD | 7,920,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.70` | 4,180,000.00 USD | 4,180,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.70` | 7,790,000.00 USD | 7,790,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.75` | 9,050.00 USD | 367,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `50.80` | 4,160,000.00 USD | 4,160,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.80` | 7,650,000.00 USD | 7,650,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `50.90` | 4,130,000.00 USD | 4,130,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `50.90` | 7,560,000.00 USD | 7,560,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `50.95` | 431.55 USD | 358,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.00` | 4,120,000.00 USD | 4,120,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.00` | 7,300,000.00 USD | 7,300,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `51.10` | 4,120,000.00 USD | 4,120,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.10` | 7,180,000.00 USD | 7,180,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.15` | 219,370.00 USD | 358,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.20` | 4,100,000.00 USD | 4,100,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.20` | 7,100,000.00 USD | 7,100,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.25` | 202.44 USD | 138,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.30` | 4,080,000.00 USD | 4,080,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.30` | 7,030,000.00 USD | 7,030,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.35` | 453.93 USD | 138,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.40` | 4,060,000.00 USD | 4,060,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.40` | 6,930,000.00 USD | 6,930,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.45` | 27,210.00 USD | 138,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.50` | 4,050,000.00 USD | 4,050,000.00 USD | 7,580.00 USD | 10,010.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.50` | 6,770,000.00 USD | 6,770,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.55` | 551.07 USD | 110,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.60` | 3,990,000.00 USD | 3,990,000.00 USD | 5,990.00 USD | 17,860.00 USD | 709.44 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.60` | 6,670,000.00 USD | 6,670,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.65` | 9,100.00 USD | 110,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.70` | 3,970,000.00 USD | 3,970,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.70` | 6,550,000.00 USD | 6,550,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.75` | 6,480.00 USD | 101,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.80` | 3,950,000.00 USD | 3,950,000.00 USD | 10,010.00 USD | 18,760.00 USD | 12,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.80` | 6,520,000.00 USD | 6,520,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.85` | 14,770.00 USD | 94,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `51.90` | 3,910,000.00 USD | 3,910,000.00 USD | 10,800.00 USD | 19,550.00 USD | 21,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `51.90` | 6,460,000.00 USD | 6,460,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `51.95` | 13,950.00 USD | 80,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.00` | 3,860,000.00 USD | 3,860,000.00 USD | 15,280.00 USD | 24,580.00 USD | 16,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.00` | 6,400,000.00 USD | 6,400,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.05` | 305.01 USD | 66,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.10` | 3,800,000.00 USD | 3,800,000.00 USD | 30,730.00 USD | 17,300.00 USD | 40,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.10` | 6,300,000.00 USD | 6,300,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.15` | 1,900.00 USD | 65,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.20` | 3,710,000.00 USD | 3,710,000.00 USD | 13,190.00 USD | 5,050.00 USD | 49,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.20` | 6,210,000.00 USD | 6,210,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.25` | 4,820.00 USD | 63,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.30` | 3,650,000.00 USD | 3,650,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.30` | 6,130,000.00 USD | 6,130,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.35` | 245.52 USD | 59,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.40` | 3,590,000.00 USD | 3,590,000.00 USD | 15,630.00 USD | 15,400.00 USD | 7,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.40` | 6,050,000.00 USD | 6,050,000.00 USD | 20,580.00 USD | 38,950.00 USD | 19,520.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.45` | 5,820.00 USD | 58,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.50` | 3,550,000.00 USD | 3,550,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.50` | 5,970,000.00 USD | 5,970,000.00 USD | 38,650.00 USD | 0.00 USD | 11,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.55` | 8,700.00 USD | 53,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.60` | 3,380,000.00 USD | 3,380,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.60` | 5,920,000.00 USD | 5,920,000.00 USD | 60,960.00 USD | 31,860.00 USD | 59,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.65` | 1,050.00 USD | 44,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.70` | 3,330,000.00 USD | 3,330,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.70` | 5,770,000.00 USD | 5,770,000.00 USD | 18,590.00 USD | 75,910.00 USD | 108,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.75` | 30,280.00 USD | 43,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.80` | 3,250,000.00 USD | 3,250,000.00 USD | 28,880.00 USD | 50,850.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.80` | 5,570,000.00 USD | 5,570,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.85` | 5,950.00 USD | 12,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `52.90` | 3,090,000.00 USD | 3,090,000.00 USD | 44,710.00 USD | 55,550.00 USD | 30,100.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `52.90` | 5,510,000.00 USD | 5,510,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `52.95` | 2,680.00 USD | 7,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.00` | 2,960,000.00 USD | 2,960,000.00 USD | 31,870.00 USD | 34,720.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.00` | 5,440,000.00 USD | 5,440,000.00 USD | 39,690.00 USD | 25,380.00 USD | 97,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.05` | 769.76 USD | 4,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.10` | 2,850,000.00 USD | 2,850,000.00 USD | 12,590.00 USD | 66,450.00 USD | 88,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.10` | 5,270,000.00 USD | 5,270,000.00 USD | 45,320.00 USD | 25,300.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.15` | 2,030.00 USD | 3,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.20` | 2,680,000.00 USD | 2,680,000.00 USD | 36,030.00 USD | 39,410.00 USD | 55,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.20` | 5,200,000.00 USD | 5,200,000.00 USD | 162,460.00 USD | 68,940.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.25` | 619.30 USD | 1,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.30` | 2,550,000.00 USD | 2,550,000.00 USD | 28,400.00 USD | 56,180.00 USD | 16,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.30` | 4,930,000.00 USD | 4,930,000.00 USD | 59,390.00 USD | 77,520.00 USD | 35,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.40` | 2,450,000.00 USD | 2,450,000.00 USD | 12,600.00 USD | 31,610.00 USD | 15,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.40` | 4,760,000.00 USD | 4,760,000.00 USD | 61,460.00 USD | 42,640.00 USD | 107,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `53.45` | 942.86 USD | 942.86 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `53.50` | 2,390,000.00 USD | 2,390,000.00 USD | 21,250.00 USD | 27,740.00 USD | 22,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.50` | 4,550,000.00 USD | 4,550,000.00 USD | 60,260.00 USD | 7,990.00 USD | 28,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.60` | 2,320,000.00 USD | 2,320,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.60` | 4,450,000.00 USD | 4,450,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.70` | 2,210,000.00 USD | 2,210,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.70` | 4,380,000.00 USD | 4,380,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.80` | 2,190,000.00 USD | 2,190,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.80` | 4,210,000.00 USD | 4,210,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `53.90` | 2,100,000.00 USD | 2,100,000.00 USD | 49,810.00 USD | 39,560.00 USD | 27,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `53.90` | 4,070,000.00 USD | 4,070,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.00` | 1,980,000.00 USD | 1,980,000.00 USD | 76,010.00 USD | 30,780.00 USD | 86,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.00` | 3,870,000.00 USD | 3,870,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.10` | 1,790,000.00 USD | 1,790,000.00 USD | 105,010.00 USD | 27,610.00 USD | 74,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.10` | 3,120,000.00 USD | 3,120,000.00 USD | 302,190.00 USD | 5,360.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.20` | 1,580,000.00 USD | 1,580,000.00 USD | 72,600.00 USD | 62,320.00 USD | 47,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.20` | 2,770,000.00 USD | 2,770,000.00 USD | 205,060.00 USD | 14,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.30` | 1,400,000.00 USD | 1,400,000.00 USD | 46,340.00 USD | 65,810.00 USD | 32,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.30` | 2,550,000.00 USD | 2,550,000.00 USD | 381,380.00 USD | 81,250.00 USD | 208,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.40` | 1,250,000.00 USD | 1,250,000.00 USD | 102,880.00 USD | 147,860.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.40` | 1,870,000.00 USD | 1,870,000.00 USD | 304,270.00 USD | 119,790.00 USD | 93,590.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.50` | 978,370.00 USD | 978,370.00 USD | 24,100.00 USD | 106,190.00 USD | 30,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.50` | 1,360,000.00 USD | 1,360,000.00 USD | 194,580.00 USD | 86,030.00 USD | 273,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.60` | 817,270.00 USD | 817,270.00 USD | 25,070.00 USD | 69,570.00 USD | 43,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.60` | 803,330.00 USD | 803,330.00 USD | 18,530.00 USD | 11,010.00 USD | 131,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.70` | 679,040.00 USD | 679,040.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.70` | 642,400.00 USD | 642,400.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.80` | 543,580.00 USD | 543,580.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.80` | 597,490.00 USD | 597,490.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `54.90` | 471,240.00 USD | 471,240.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `54.90` | 535,350.00 USD | 535,350.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.00` | 328,060.00 USD | 328,060.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.00` | 374,780.00 USD | 374,780.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.10` | 178,000.00 USD | 178,000.00 USD | 50,530.00 USD | 0.00 USD | 80,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.10` | 254,900.00 USD | 254,900.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `55.20` | 47,280.00 USD | 47,280.00 USD | 39,390.00 USD | 7,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `55.20` | 117,110.00 USD | 117,110.00 USD | 57,400.00 USD | 59,710.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.30` | 52,860.00 USD | 52,860.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.30` | 105,720.00 USD | 105,720.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 23,140.00 USD | 23,140.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.30` | 46,280.00 USD | 46,280.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.40` | 51,080.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.70` | 106,330.00 USD | 106,330.00 USD | 0.00 USD | 0.00 USD | 613.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.70` | 225,330.00 USD | 225,330.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.80` | 109,510.00 USD | 109,510.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.80` | 316,300.00 USD | 316,300.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `55.90` | 162,570.00 USD | 162,570.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `55.90` | 457,620.00 USD | 457,620.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.00` | 166,950.00 USD | 166,950.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.00` | 628,740.00 USD | 628,740.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.20` | 176,290.00 USD | 176,290.00 USD | 0.00 USD | 9,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.20` | 708,680.00 USD | 708,680.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.30` | 224,180.00 USD | 224,180.00 USD | 10,140.00 USD | 8,440.00 USD | 29,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.30` | 756,750.00 USD | 756,750.00 USD | 0.00 USD | 5,360.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.40` | 302,290.00 USD | 302,290.00 USD | 5,040.00 USD | 63,500.00 USD | 9,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.40` | 785,120.00 USD | 785,120.00 USD | 2,650.00 USD | 25,730.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.50` | 809,870.00 USD | 809,870.00 USD | 169,280.00 USD | 166,360.00 USD | 171,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.50` | 1,210,000.00 USD | 1,210,000.00 USD | 170,750.00 USD | 224,670.00 USD | 33,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.60` | 1,220,000.00 USD | 1,220,000.00 USD | 101,920.00 USD | 203,090.00 USD | 102,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.60` | 1,820,000.00 USD | 1,820,000.00 USD | 363,190.00 USD | 242,530.00 USD | 1,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.70` | 1,670,000.00 USD | 1,670,000.00 USD | 79,170.00 USD | 87,240.00 USD | 287,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.70` | 2,300,000.00 USD | 2,300,000.00 USD | 152,150.00 USD | 192,280.00 USD | 132,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.80` | 1,970,000.00 USD | 1,970,000.00 USD | 128,400.00 USD | 64,860.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.80` | 2,890,000.00 USD | 2,890,000.00 USD | 172,110.00 USD | 101,860.00 USD | 318,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `56.90` | 2,070,000.00 USD | 2,070,000.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `56.90` | 3,360,000.00 USD | 3,360,000.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.00` | 2,150,000.00 USD | 2,150,000.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.00` | 3,690,000.00 USD | 3,690,000.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.10` | 2,350,000.00 USD | 2,350,000.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.10` | 3,820,000.00 USD | 3,820,000.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.20` | 2,600,000.00 USD | 2,600,000.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.20` | 3,990,000.00 USD | 3,990,000.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.30` | 2,810,000.00 USD | 2,810,000.00 USD | 70,930.00 USD | 49,300.00 USD | 87,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.30` | 4,190,000.00 USD | 4,190,000.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.40` | 3,040,000.00 USD | 3,040,000.00 USD | 90,030.00 USD | 53,690.00 USD | 91,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.40` | 4,670,000.00 USD | 4,670,000.00 USD | 124,180.00 USD | 74,860.00 USD | 277,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.50` | 3,490,000.00 USD | 3,490,000.00 USD | 197,830.00 USD | 71,750.00 USD | 178,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.50` | 4,810,000.00 USD | 4,810,000.00 USD | 99,810.00 USD | 39,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.60` | 3,710,000.00 USD | 3,710,000.00 USD | 85,090.00 USD | 56,950.00 USD | 76,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.60` | 5,080,000.00 USD | 5,080,000.00 USD | 149,560.00 USD | 81,050.00 USD | 41,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.70` | 3,960,000.00 USD | 3,960,000.00 USD | 62,800.00 USD | 82,250.00 USD | 106,960.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 58,380.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `57.80` | 4,110,000.00 USD | 4,110,000.00 USD | 18,150.00 USD | 43,620.00 USD | 88,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.80` | 5,340,000.00 USD | 5,340,000.00 USD | 27,080.00 USD | 49,750.00 USD | 66,100.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `57.90` | 4,200,000.00 USD | 4,200,000.00 USD | 25,080.00 USD | 37,910.00 USD | 28,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `57.90` | 5,390,000.00 USD | 5,390,000.00 USD | 14,390.00 USD | 5,510.00 USD | 30,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `57.95` | 125.75 USD | 281.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.00` | 4,240,000.00 USD | 4,240,000.00 USD | 10,450.00 USD | 9,480.00 USD | 15,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.00` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.10` | 4,310,000.00 USD | 4,310,000.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.10` | 5,540,000.00 USD | 5,540,000.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.20` | 4,390,000.00 USD | 4,390,000.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.30` | 4,520,000.00 USD | 4,520,000.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.30` | 5,670,000.00 USD | 5,670,000.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.40` | 4,620,000.00 USD | 4,620,000.00 USD | 27,360.00 USD | 18,940.00 USD | 49,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.40` | 5,790,000.00 USD | 5,790,000.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.50` | 4,620,000.00 USD | 4,620,000.00 USD | 1,420.00 USD | 1,200.00 USD | 124.02 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.50` | 5,820,000.00 USD | 5,820,000.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.60` | 4,690,000.00 USD | 4,690,000.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.60` | 5,920,000.00 USD | 5,920,000.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.70` | 4,780,000.00 USD | 4,780,000.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.70` | 5,990,000.00 USD | 5,990,000.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `58.80` | 4,840,000.00 USD | 4,840,000.00 USD | 36,630.00 USD | 5,970.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.80` | 6,000,000.00 USD | 6,000,000.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `58.85` | 1,480.00 USD | 1,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `58.90` | 5,000,000.00 USD | 5,000,000.00 USD | 24,050.00 USD | 57,780.00 USD | 80,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `58.90` | 6,140,000.00 USD | 6,140,000.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.00` | 5,220,000.00 USD | 5,220,000.00 USD | 93,920.00 USD | 45,360.00 USD | 79,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.00` | 6,580,000.00 USD | 6,580,000.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.10` | 5,430,000.00 USD | 5,430,000.00 USD | 57,720.00 USD | 33,680.00 USD | 113,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.10` | 6,880,000.00 USD | 6,880,000.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.20` | 5,610,000.00 USD | 5,610,000.00 USD | 89,410.00 USD | 46,380.00 USD | 49,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.20` | 7,230,000.00 USD | 7,230,000.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.30` | 5,860,000.00 USD | 5,860,000.00 USD | 146,880.00 USD | 30,070.00 USD | 66,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.30` | 7,500,000.00 USD | 7,500,000.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `59.35` | 9,440.00 USD | 11,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `59.40` | 5,970,000.00 USD | 5,970,000.00 USD | 35,830.00 USD | 30,410.00 USD | 49,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.40` | 7,800,000.00 USD | 7,800,000.00 USD | 107,040.00 USD | 73,620.00 USD | 124,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.50` | 6,110,000.00 USD | 6,110,000.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.50` | 7,950,000.00 USD | 7,950,000.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.60` | 6,200,000.00 USD | 6,200,000.00 USD | 29,830.00 USD | 49,290.00 USD | 5,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.60` | 8,320,000.00 USD | 8,320,000.00 USD | 184,700.00 USD | 106,840.00 USD | 72,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.70` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 15,700.00 USD | 59,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.70` | 8,640,000.00 USD | 8,640,000.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.80` | 6,320,000.00 USD | 6,320,000.00 USD | 21,030.00 USD | 26,470.00 USD | 177.92 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.80` | 9,000,000.00 USD | 9,000,000.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `59.90` | 6,490,000.00 USD | 6,490,000.00 USD | 102,020.00 USD | 15,860.00 USD | 48,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `59.90` | 9,210,000.00 USD | 9,210,000.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.00` | 6,720,000.00 USD | 6,720,000.00 USD | 162,340.00 USD | 27,490.00 USD | 45,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.00` | 9,460,000.00 USD | 9,460,000.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.10` | 6,820,000.00 USD | 6,820,000.00 USD | 46,510.00 USD | 21,380.00 USD | 32,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.10` | 9,840,000.00 USD | 9,840,000.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.15` | 208,880.00 USD | 220,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.20` | 6,940,000.00 USD | 6,940,000.00 USD | 40,980.00 USD | 16,710.00 USD | 57,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.20` | 10,210,000.00 USD | 10,210,000.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.30` | 7,030,000.00 USD | 7,030,000.00 USD | 44,650.00 USD | 25,170.00 USD | 26,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.30` | 10,610,000.00 USD | 10,610,000.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.35` | 431.50 USD | 220,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `60.40` | 7,160,000.00 USD | 7,160,000.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.40` | 10,970,000.00 USD | 10,970,000.00 USD | 55,050.00 USD | 100,560.00 USD | 202,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.50` | 7,230,000.00 USD | 7,230,000.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.50` | 11,340,000.00 USD | 11,340,000.00 USD | 115,390.00 USD | 80,510.00 USD | 169,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.60` | 7,300,000.00 USD | 7,300,000.00 USD | 40,710.00 USD | 20,390.00 USD | 3,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.60` | 11,720,000.00 USD | 11,720,000.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.70` | 7,360,000.00 USD | 7,360,000.00 USD | 32,700.00 USD | 24,020.00 USD | 8,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.70` | 11,860,000.00 USD | 11,860,000.00 USD | 76,200.00 USD | 37,000.00 USD | 23,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.80` | 7,440,000.00 USD | 7,440,000.00 USD | 10,230.00 USD | 18,960.00 USD | 49,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.80` | 12,010,000.00 USD | 12,010,000.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `60.90` | 7,540,000.00 USD | 7,540,000.00 USD | 37,840.00 USD | 33,530.00 USD | 28,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `60.90` | 12,230,000.00 USD | 12,230,000.00 USD | 105,970.00 USD | 43,970.00 USD | 70,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `60.95` | 397.39 USD | 220,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `61.00` | 7,610,000.00 USD | 7,610,000.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.00` | 12,290,000.00 USD | 12,290,000.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.10` | 7,670,000.00 USD | 7,670,000.00 USD | 21,130.00 USD | 22,590.00 USD | 15,730.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.10` | 12,340,000.00 USD | 12,340,000.00 USD | 31,540.00 USD | 21,750.00 USD | 189.67 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.20` | 7,800,000.00 USD | 7,800,000.00 USD | 74,800.00 USD | 9,580.00 USD | 41,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.20` | 12,470,000.00 USD | 12,470,000.00 USD | 51,570.00 USD | 29,220.00 USD | 47,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.30` | 7,820,000.00 USD | 7,820,000.00 USD | 3,530.00 USD | 11,600.00 USD | 7,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.30` | 12,520,000.00 USD | 12,520,000.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.40` | 7,830,000.00 USD | 7,830,000.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.40` | 12,650,000.00 USD | 12,650,000.00 USD | 60,410.00 USD | 25,720.00 USD | 43,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `61.50` | 7,830,000.00 USD | 7,830,000.00 USD | 1,060.00 USD | 2,590.00 USD | 2,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.50` | 12,750,000.00 USD | 12,750,000.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `61.55` | 222.20 USD | 221,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `61.60` | 12,970,000.00 USD | 12,970,000.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.70` | 13,160,000.00 USD | 13,160,000.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.80` | 13,430,000.00 USD | 13,430,000.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `61.90` | 13,570,000.00 USD | 13,570,000.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.00` | 13,670,000.00 USD | 13,670,000.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.10` | 13,680,000.00 USD | 13,680,000.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.20` | 13,790,000.00 USD | 13,790,000.00 USD | 34,230.00 USD | 34,620.00 USD | 41,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.30` | 13,900,000.00 USD | 13,900,000.00 USD | 25,910.00 USD | 23,450.00 USD | 57,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `62.40` | 14,010,000.00 USD | 14,010,000.00 USD | 62,940.00 USD | 25,250.00 USD | 25,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `62.95` | 138.49 USD | 221,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.45` | 3,350.00 USD | 224,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `63.55` | 8,180.00 USD | 232,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.05` | 121.36 USD | 232,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `67.85` | 709.03 USD | 233,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `68.35` | 619.93 USD | 234,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `68.95` | 39,860.00 USD | 274,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `76.35` | 8,380.00 USD | 282,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.75` | 578,460.00 USD | 860,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `77.85` | 602.56 USD | 861,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `80.75` | 646.00 USD | 862,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.05` | 19,000.00 USD | 881,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.45` | 3,260.00 USD | 884,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `81.55` | 123.96 USD | 884,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.05` | 2,710.00 USD | 887,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `82.75` | 214.32 USD | 887,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `85.35` | 23,680.00 USD | 911,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `90.65` | 119.66 USD | 911,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.25` | 164.35 USD | 911,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `97.85` | 2,450.00 USD | 913,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `98.05` | 19,610.00 USD | 933,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `102.75` | 30,820.00 USD | 964,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.25` | 213.71 USD | 964,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.65` | 353,090.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `104.85` | 2,320.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.75` | 1,620.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `106.85` | 1,860.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `107.25` | 199.48 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `108.05` | 6,470.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.35` | 753.69 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `110.95` | 664.59 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `11.35` | 3,050,000.00 USD | 0.00 USD | 136.20 USD | `-79.65%` | `12.00` |
| `Live` | `Long` | `12.25` | 3,050,000.00 USD | 0.00 USD | 122.50 USD | `-78.04%` | `10.00` |
| `Live` | `Long` | `12.75` | 3,050,000.00 USD | 0.00 USD | 2,560.00 USD | `-77.14%` | `200.43` |
| `Live` | `Long` | `13.15` | 3,050,000.00 USD | 0.00 USD | 2,220.00 USD | `-76.43%` | `168.79` |
| `Live` | `Long` | `13.65` | 3,040,000.00 USD | 0.00 USD | 150.15 USD | `-75.53%` | `11.00` |
| `Live` | `Long` | `14.95` | 3,040,000.00 USD | 0.00 USD | 2,250.00 USD | `-73.20%` | `150.57` |
| `Live` | `Long` | `17.45` | 3,040,000.00 USD | 0.00 USD | 16,230.00 USD | `-68.72%` | `930.00` |
| `Live` | `Long` | `18.15` | 3,030,000.00 USD | 0.00 USD | 403.66 USD | `-67.46%` | `22.24` |
| `Live` | `Long` | `18.25` | 3,030,000.00 USD | 0.00 USD | 2,190.00 USD | `-67.29%` | `120.00` |
| `Live` | `Long` | `19.05` | 3,020,000.00 USD | 0.00 USD | 3,590.00 USD | `-65.85%` | `188.60` |
| `Live` | `Long` | `19.45` | 3,020,000.00 USD | 0.00 USD | 2,010.00 USD | `-65.13%` | `103.47` |
| `Live` | `Long` | `20.75` | 3,020,000.00 USD | 0.00 USD | 4,480.00 USD | `-62.80%` | `215.72` |
| `Live` | `Long` | `21.05` | 3,010,000.00 USD | 0.00 USD | 1,260.00 USD | `-62.27%` | `60.00` |
| `Live` | `Long` | `22.25` | 3,010,000.00 USD | 0.00 USD | 358.89 USD | `-60.11%` | `16.13` |
| `Live` | `Long` | `22.65` | 3,010,000.00 USD | 0.00 USD | 961.04 USD | `-59.40%` | `42.43` |
| `Live` | `Long` | `23.35` | 3,010,000.00 USD | 0.00 USD | 647.03 USD | `-58.14%` | `27.71` |
| `Live` | `Long` | `23.75` | 3,010,000.00 USD | 0.00 USD | 375.73 USD | `-57.43%` | `15.82` |
| `Live` | `Long` | `23.85` | 3,010,000.00 USD | 0.00 USD | 7,220.00 USD | `-57.25%` | `302.87` |
| `Live` | `Long` | `24.65` | 3,000,000.00 USD | 0.00 USD | 113,020.00 USD | `-55.81%` | `4,584.81` |
| `Live` | `Long` | `25.25` | 2,890,000.00 USD | 0.00 USD | 277,980.00 USD | `-54.74%` | `11,009.19` |
| `Live` | `Long` | `25.35` | 2,610,000.00 USD | 0.00 USD | 173.39 USD | `-54.56%` | `6.84` |
| `Live` | `Long` | `25.55` | 2,610,000.00 USD | 0.00 USD | 50,740.00 USD | `-54.20%` | `1,985.99` |
| `Live` | `Long` | `25.75` | 2,560,000.00 USD | 0.00 USD | 189.52 USD | `-53.84%` | `7.36` |
| `Live` | `Long` | `25.95` | 2,560,000.00 USD | 0.00 USD | 374.20 USD | `-53.48%` | `14.42` |
| `Live` | `Long` | `27.05` | 2,560,000.00 USD | 0.00 USD | 5,510.00 USD | `-51.51%` | `203.85` |
| `Live` | `Long` | `27.15` | 2,550,000.00 USD | 0.00 USD | 3,210.00 USD | `-51.33%` | `118.41` |
| `Live` | `Long` | `27.55` | 2,550,000.00 USD | 0.00 USD | 272.75 USD | `-50.61%` | `9.90` |
| `Live` | `Long` | `27.95` | 2,550,000.00 USD | 0.00 USD | 173.85 USD | `-49.90%` | `6.22` |
| `Live` | `Long` | `28.55` | 2,550,000.00 USD | 0.00 USD | 8,560.00 USD | `-48.82%` | `300.00` |
| `Live` | `Long` | `29.15` | 2,540,000.00 USD | 0.00 USD | 755.28 USD | `-47.75%` | `25.91` |
| `Live` | `Long` | `29.75` | 2,540,000.00 USD | 0.00 USD | 297,500.00 USD | `-46.67%` | `10,000.00` |
| `Live` | `Long` | `30.05` | 2,240,000.00 USD | 0.00 USD | 218.46 USD | `-46.13%` | `7.27` |
| `Live` | `Long` | `30.55` | 2,240,000.00 USD | 0.00 USD | 152.75 USD | `-45.24%` | `5.00` |
| `Live` | `Long` | `30.65` | 2,240,000.00 USD | 0.00 USD | 1,540.00 USD | `-45.06%` | `50.19` |
| `Live` | `Long` | `30.95` | 2,240,000.00 USD | 0.00 USD | 538.53 USD | `-44.52%` | `17.40` |
| `Live` | `Long` | `31.15` | 2,240,000.00 USD | 0.00 USD | 27,840.00 USD | `-44.16%` | `893.80` |
| `Live` | `Long` | `31.55` | 2,210,000.00 USD | 0.00 USD | 1,060.00 USD | `-43.44%` | `33.49` |
| `Live` | `Long` | `31.65` | 2,210,000.00 USD | 0.00 USD | 4,640.00 USD | `-43.26%` | `146.53` |
| `Live` | `Long` | `31.85` | 2,210,000.00 USD | 0.00 USD | 2,870.00 USD | `-42.91%` | `90.00` |
| `Live` | `Long` | `31.95` | 2,200,000.00 USD | 0.00 USD | 125.24 USD | `-42.73%` | `3.92` |
| `Live` | `Long` | `32.15` | 2,200,000.00 USD | 0.00 USD | 450.10 USD | `-42.37%` | `14.00` |
| `Live` | `Long` | `32.25` | 2,200,000.00 USD | 0.00 USD | 5,610.00 USD | `-42.19%` | `174.01` |
| `Live` | `Long` | `32.35` | 2,200,000.00 USD | 0.00 USD | 172.10 USD | `-42.01%` | `5.32` |
| `Live` | `Long` | `32.65` | 2,200,000.00 USD | 0.00 USD | 653.00 USD | `-41.47%` | `20.00` |
| `Live` | `Long` | `32.75` | 2,200,000.00 USD | 0.00 USD | 3,750.00 USD | `-41.29%` | `114.55` |
| `Live` | `Long` | `32.95` | 2,190,000.00 USD | 0.00 USD | 32,950.00 USD | `-40.93%` | `1,000.01` |
| `Live` | `Long` | `33.25` | 2,160,000.00 USD | 0.00 USD | 6,210.00 USD | `-40.40%` | `186.71` |
| `Live` | `Long` | `33.65` | 2,150,000.00 USD | 0.00 USD | 257.76 USD | `-39.68%` | `7.66` |
| `Live` | `Long` | `34.05` | 2,150,000.00 USD | 0.00 USD | 182.85 USD | `-38.96%` | `5.37` |
| `Live` | `Long` | `34.15` | 2,150,000.00 USD | 0.00 USD | 126.70 USD | `-38.78%` | `3.71` |
| `Live` | `Long` | `34.45` | 2,150,000.00 USD | 0.00 USD | 65,890.00 USD | `-38.25%` | `1,912.61` |
| `Live` | `Long` | `34.65` | 2,090,000.00 USD | 0.00 USD | 3,240.00 USD | `-37.89%` | `93.56` |
| `Live` | `Long` | `34.95` | 2,090,000.00 USD | 0.00 USD | 4,670.00 USD | `-37.35%` | `133.63` |
| `Live` | `Long` | `35.05` | 2,080,000.00 USD | 0.00 USD | 166.49 USD | `-37.17%` | `4.75` |
| `Live` | `Long` | `35.55` | 2,080,000.00 USD | 0.00 USD | 423.76 USD | `-36.27%` | `11.92` |
| `Live` | `Long` | `36.05` | 2,080,000.00 USD | 0.00 USD | 314.72 USD | `-35.38%` | `8.73` |
| `Live` | `Long` | `36.35` | 2,080,000.00 USD | 0.00 USD | 3,020.00 USD | `-34.84%` | `83.03` |
| `Live` | `Long` | `36.45` | 2,080,000.00 USD | 0.00 USD | 708.59 USD | `-34.66%` | `19.44` |
| `Live` | `Long` | `36.55` | 2,080,000.00 USD | 0.00 USD | 2,990.00 USD | `-34.48%` | `81.91` |
| `Live` | `Long` | `36.75` | 2,070,000.00 USD | 0.00 USD | 101.80 USD | `-34.12%` | `2.77` |
| `Live` | `Long` | `36.85` | 2,070,000.00 USD | 0.00 USD | 147.03 USD | `-33.94%` | `3.99` |
| `Live` | `Long` | `36.95` | 2,070,000.00 USD | 0.00 USD | 960.70 USD | `-33.76%` | `26.00` |
| `Live` | `Long` | `37.05` | 2,070,000.00 USD | 0.00 USD | 1,050.00 USD | `-33.58%` | `28.27` |
| `Live` | `Long` | `37.15` | 2,070,000.00 USD | 0.00 USD | 438.74 USD | `-33.41%` | `11.81` |
| `Live` | `Long` | `37.35` | 2,070,000.00 USD | 0.00 USD | 9,260.00 USD | `-33.05%` | `247.91` |
| `Live` | `Long` | `37.55` | 2,060,000.00 USD | 0.00 USD | 3,530.00 USD | `-32.69%` | `94.04` |
| `Live` | `Long` | `37.75` | 2,060,000.00 USD | 0.00 USD | 377.50 USD | `-32.33%` | `10.00` |
| `Live` | `Long` | `37.85` | 2,060,000.00 USD | 0.00 USD | 6,540.00 USD | `-32.15%` | `172.70` |
| `Live` | `Long` | `37.95` | 2,050,000.00 USD | 0.00 USD | 446.67 USD | `-31.97%` | `11.77` |
| `Live` | `Long` | `38.25` | 2,050,000.00 USD | 0.00 USD | 695.38 USD | `-31.43%` | `18.18` |
| `Live` | `Long` | `38.35` | 2,050,000.00 USD | 0.00 USD | 847.54 USD | `-31.25%` | `22.10` |
| `Live` | `Long` | `38.45` | 2,050,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.07%` | `62.34` |
| `Live` | `Long` | `38.55` | 2,050,000.00 USD | 0.00 USD | 993.82 USD | `-30.90%` | `25.78` |
| `Live` | `Long` | `38.65` | 2,050,000.00 USD | 0.00 USD | 4,280.00 USD | `-30.72%` | `110.74` |
| `Live` | `Long` | `38.75` | 2,040,000.00 USD | 0.00 USD | 1,040.00 USD | `-30.54%` | `26.84` |
| `Live` | `Long` | `38.95` | 2,040,000.00 USD | 0.00 USD | 3,700.00 USD | `-30.18%` | `95.00` |
| `Live` | `Long` | `39.05` | 2,040,000.00 USD | 0.00 USD | 664,760.00 USD | `-30.00%` | `17,023.28` |
| `Live` | `Long` | `39.15` | 1,370,000.00 USD | 0.00 USD | 570.02 USD | `-29.82%` | `14.56` |
| `Live` | `Long` | `39.35` | 1,370,000.00 USD | 0.00 USD | 264.83 USD | `-29.46%` | `6.73` |
| `Live` | `Long` | `39.55` | 1,370,000.00 USD | 0.00 USD | 1,030.00 USD | `-29.10%` | `26.06` |
| `Live` | `Long` | `39.65` | 1,370,000.00 USD | 0.00 USD | 5,900.00 USD | `-28.92%` | `148.78` |
| `Live` | `Long` | `39.75` | 1,360,000.00 USD | 0.00 USD | 1,180.00 USD | `-28.74%` | `29.57` |
| `Live` | `Long` | `39.85` | 1,360,000.00 USD | 0.00 USD | 5,390.00 USD | `-28.57%` | `135.28` |
| `Live` | `Long` | `40.05` | 1,360,000.00 USD | 0.00 USD | 2,160.00 USD | `-28.21%` | `53.97` |
| `Live` | `Long` | `40.25` | 1,350,000.00 USD | 0.00 USD | 1,000.00 USD | `-27.85%` | `24.93` |
| `Live` | `Long` | `40.45` | 1,350,000.00 USD | 0.00 USD | 1,010.00 USD | `-27.49%` | `24.92` |
| `Live` | `Long` | `40.55` | 1,350,000.00 USD | 0.00 USD | 133.00 USD | `-27.31%` | `3.28` |
| `Live` | `Long` | `40.65` | 1,350,000.00 USD | 0.00 USD | 274.39 USD | `-27.13%` | `6.75` |
| `Live` | `Long` | `40.85` | 1,350,000.00 USD | 0.00 USD | 6,340.00 USD | `-26.77%` | `155.23` |
| `Live` | `Long` | `40.95` | 1,350,000.00 USD | 0.00 USD | 816.13 USD | `-26.59%` | `19.93` |
| `Live` | `Long` | `41.05` | 1,350,000.00 USD | 0.00 USD | 727.00 USD | `-26.41%` | `17.71` |
| `Live` | `Long` | `41.25` | 1,340,000.00 USD | 0.00 USD | 14,850.00 USD | `-26.06%` | `359.91` |
| `Live` | `Long` | `41.45` | 1,330,000.00 USD | 0.00 USD | 644.96 USD | `-25.70%` | `15.56` |
| `Live` | `Long` | `41.65` | 1,330,000.00 USD | 0.00 USD | 9,160.00 USD | `-25.34%` | `220.00` |
| `Live` | `Long` | `41.85` | 1,320,000.00 USD | 0.00 USD | 3,720.00 USD | `-24.98%` | `88.83` |
| `Live` | `Long` | `41.95` | 1,320,000.00 USD | 0.00 USD | 299.10 USD | `-24.80%` | `7.13` |
| `Live` | `Long` | `42.05` | 1,320,000.00 USD | 0.00 USD | 201.00 USD | `-24.62%` | `4.78` |
| `Live` | `Long` | `42.15` | 1,320,000.00 USD | 0.00 USD | 64,190.00 USD | `-24.44%` | `1,522.78` |
| `Live` | `Long` | `42.25` | 1,250,000.00 USD | 0.00 USD | 35,410.00 USD | `-24.26%` | `838.00` |
| `Live` | `Long` | `42.55` | 1,220,000.00 USD | 0.00 USD | 339.97 USD | `-23.73%` | `7.99` |
| `Live` | `Long` | `42.65` | 1,220,000.00 USD | 0.00 USD | 1,570.00 USD | `-23.55%` | `36.70` |
| `Live` | `Long` | `42.85` | 1,210,000.00 USD | 0.00 USD | 5,800.00 USD | `-23.19%` | `135.38` |
| `Live` | `Long` | `42.95` | 1,210,000.00 USD | 0.00 USD | 2,000.00 USD | `-23.01%` | `46.65` |
| `Live` | `Long` | `43.05` | 1,210,000.00 USD | 0.00 USD | 9,080.00 USD | `-22.83%` | `211.00` |
| `Live` | `Long` | `43.15` | 1,200,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.65%` | `36.59` |
| `Live` | `Long` | `43.25` | 1,200,000.00 USD | 0.00 USD | 121,210.00 USD | `-22.47%` | `2,802.44` |
| `Live` | `Long` | `43.35` | 1,070,000.00 USD | 0.00 USD | 5,700.00 USD | `-22.29%` | `131.46` |
| `Live` | `Long` | `43.45` | 1,070,000.00 USD | 0.00 USD | 710.84 USD | `-22.11%` | `16.36` |
| `Live` | `Long` | `43.55` | 1,070,000.00 USD | 0.00 USD | 5,610.00 USD | `-21.93%` | `128.71` |
| `Live` | `Long` | `43.65` | 1,060,000.00 USD | 0.00 USD | 426.02 USD | `-21.75%` | `9.76` |
| `Live` | `Long` | `43.75` | 1,060,000.00 USD | 0.00 USD | 24,460.00 USD | `-21.57%` | `559.15` |
| `Live` | `Long` | `43.85` | 1,040,000.00 USD | 0.00 USD | 801.14 USD | `-21.39%` | `18.27` |
| `Live` | `Long` | `44.15` | 1,040,000.00 USD | 0.00 USD | 2,380.00 USD | `-20.86%` | `53.99` |
| `Live` | `Long` | `44.25` | 1,030,000.00 USD | 0.00 USD | 1,330.00 USD | `-20.68%` | `30.00` |
| `Live` | `Long` | `44.35` | 1,030,000.00 USD | 0.00 USD | 84,440.00 USD | `-20.50%` | `1,903.87` |
| `Live` | `Long` | `44.55` | 948,680.00 USD | 0.00 USD | 842.44 USD | `-20.14%` | `18.91` |
| `Live` | `Long` | `44.65` | 947,830.00 USD | 0.00 USD | 1,340.00 USD | `-19.96%` | `30.00` |
| `Live` | `Long` | `44.75` | 946,490.00 USD | 0.00 USD | 4,230.00 USD | `-19.78%` | `94.55` |
| `Live` | `Long` | `44.85` | 942,260.00 USD | 0.00 USD | 134.55 USD | `-19.60%` | `3.00` |
| `Live` | `Long` | `44.95` | 942,130.00 USD | 0.00 USD | 2,790.00 USD | `-19.42%` | `62.02` |
| `Live` | `Long` | `45.05` | 939,340.00 USD | 0.00 USD | 4,830.00 USD | `-19.24%` | `107.31` |
| `Live` | `Long` | `45.15` | 934,510.00 USD | 0.00 USD | 8,710.00 USD | `-19.06%` | `193.00` |
| `Live` | `Long` | `45.25` | 925,790.00 USD | 0.00 USD | 3,180.00 USD | `-18.89%` | `70.37` |
| `Live` | `Long` | `45.35` | 922,610.00 USD | 0.00 USD | 2,180.00 USD | `-18.71%` | `48.02` |
| `Live` | `Long` | `45.45` | 920,430.00 USD | 0.00 USD | 23,940.00 USD | `-18.53%` | `526.65` |
| `Live` | `Long` | `45.55` | 896,490.00 USD | 0.00 USD | 12,060.00 USD | `-18.35%` | `264.81` |
| `Live` | `Long` | `45.65` | 884,430.00 USD | 0.00 USD | 42,180.00 USD | `-18.17%` | `924.03` |
| `Live` | `Long` | `45.95` | 842,250.00 USD | 0.00 USD | 30,970.00 USD | `-17.63%` | `673.93` |
| `Live` | `Long` | `46.05` | 811,280.00 USD | 0.00 USD | 706.41 USD | `-17.45%` | `15.34` |
| `Live` | `Long` | `46.15` | 810,580.00 USD | 0.00 USD | 265.82 USD | `-17.27%` | `5.76` |
| `Live` | `Long` | `46.35` | 810,310.00 USD | 0.00 USD | 22,820.00 USD | `-16.91%` | `492.25` |
| `Live` | `Long` | `46.55` | 787,500.00 USD | 0.00 USD | 52,170.00 USD | `-16.55%` | `1,120.69` |
| `Live` | `Long` | `46.65` | 735,330.00 USD | 0.00 USD | 2,390.00 USD | `-16.38%` | `51.33` |
| `Live` | `Long` | `46.75` | 732,930.00 USD | 0.00 USD | 1,590.00 USD | `-16.20%` | `34.08` |
| `Live` | `Long` | `46.85` | 731,340.00 USD | 0.00 USD | 358.40 USD | `-16.02%` | `7.65` |
| `Live` | `Long` | `46.95` | 730,980.00 USD | 0.00 USD | 158.22 USD | `-15.84%` | `3.37` |
| `Live` | `Long` | `47.05` | 730,820.00 USD | 0.00 USD | 2,140.00 USD | `-15.66%` | `45.57` |
| `Live` | `Long` | `47.15` | 728,680.00 USD | 0.00 USD | 1,980.00 USD | `-15.48%` | `42.07` |
| `Live` | `Long` | `47.25` | 726,690.00 USD | 0.00 USD | 9,030.00 USD | `-15.30%` | `191.21` |
| `Live` | `Long` | `47.35` | 717,660.00 USD | 0.00 USD | 43,920.00 USD | `-15.12%` | `927.56` |
| `Live` | `Long` | `47.45` | 673,740.00 USD | 0.00 USD | 2,590.00 USD | `-14.94%` | `54.54` |
| `Live` | `Long` | `47.55` | 671,150.00 USD | 0.00 USD | 4,450.00 USD | `-14.76%` | `93.69` |
| `Live` | `Long` | `47.75` | 666,700.00 USD | 0.00 USD | 47,750.00 USD | `-14.40%` | `1,000.00` |
| `Live` | `Long` | `47.95` | 618,950.00 USD | 0.00 USD | 7,890.00 USD | `-14.04%` | `164.58` |
| `Live` | `Long` | `48.05` | 611,060.00 USD | 0.00 USD | 381.04 USD | `-13.87%` | `7.93` |
| `Live` | `Long` | `48.15` | 610,670.00 USD | 0.00 USD | 1,690.00 USD | `-13.69%` | `35.03` |
| `Live` | `Long` | `48.25` | 608,990.00 USD | 0.00 USD | 110.49 USD | `-13.51%` | `2.29` |
| `Live` | `Long` | `48.55` | 608,880.00 USD | 0.00 USD | 2,030.00 USD | `-12.97%` | `41.85` |
| `Live` | `Long` | `48.65` | 606,850.00 USD | 0.00 USD | 273.90 USD | `-12.79%` | `5.63` |
| `Live` | `Long` | `48.75` | 606,570.00 USD | 0.00 USD | 333.94 USD | `-12.61%` | `6.85` |
| `Live` | `Long` | `48.85` | 606,240.00 USD | 0.00 USD | 1,890.00 USD | `-12.43%` | `38.79` |
| `Live` | `Long` | `48.95` | 604,340.00 USD | 0.00 USD | 252.58 USD | `-12.25%` | `5.16` |
| `Live` | `Long` | `49.05` | 604,090.00 USD | 0.00 USD | 1,580.00 USD | `-12.07%` | `32.25` |
| `Live` | `Long` | `49.15` | 602,510.00 USD | 0.00 USD | 5,740.00 USD | `-11.89%` | `116.83` |
| `Live` | `Long` | `49.35` | 596,770.00 USD | 0.00 USD | 5,230.00 USD | `-11.54%` | `105.97` |
| `Live` | `Long` | `49.45` | 591,540.00 USD | 0.00 USD | 419.34 USD | `-11.36%` | `8.48` |
| `Live` | `Long` | `49.55` | 591,120.00 USD | 0.00 USD | 18,010.00 USD | `-11.18%` | `363.57` |
| `Live` | `Long` | `49.65` | 573,100.00 USD | 0.00 USD | 73,260.00 USD | `-11.00%` | `1,475.52` |
| `Live` | `Long` | `49.75` | 499,840.00 USD | 0.00 USD | 20,390.00 USD | `-10.82%` | `409.75` |
| `Live` | `Long` | `49.95` | 479,460.00 USD | 0.00 USD | 19,920.00 USD | `-10.46%` | `398.70` |
| `Live` | `Long` | `50.05` | 459,540.00 USD | 0.00 USD | 1,820.00 USD | `-10.28%` | `36.43` |
| `Live` | `Long` | `50.25` | 457,720.00 USD | 0.00 USD | 102.51 USD | `-9.92%` | `2.04` |
| `Live` | `Long` | `50.35` | 457,620.00 USD | 0.00 USD | 1,140.00 USD | `-9.74%` | `22.67` |
| `Live` | `Long` | `50.45` | 456,480.00 USD | 0.00 USD | 4,720.00 USD | `-9.56%` | `93.64` |
| `Live` | `Long` | `50.55` | 451,750.00 USD | 0.00 USD | 84,100.00 USD | `-9.38%` | `1,663.61` |
| `Live` | `Long` | `50.75` | 367,660.00 USD | 0.00 USD | 9,050.00 USD | `-9.03%` | `178.28` |
| `Live` | `Long` | `50.95` | 358,610.00 USD | 0.00 USD | 431.55 USD | `-8.67%` | `8.47` |
| `Live` | `Long` | `51.15` | 358,180.00 USD | 0.00 USD | 219,370.00 USD | `-8.31%` | `4,288.79` |
| `Live` | `Long` | `51.25` | 138,810.00 USD | 0.00 USD | 202.44 USD | `-8.13%` | `3.95` |
| `Live` | `Long` | `51.35` | 138,600.00 USD | 0.00 USD | 453.93 USD | `-7.95%` | `8.84` |
| `Live` | `Long` | `51.45` | 138,150.00 USD | 0.00 USD | 27,210.00 USD | `-7.77%` | `528.81` |
| `Live` | `Long` | `51.55` | 110,940.00 USD | 0.00 USD | 551.07 USD | `-7.59%` | `10.69` |
| `Live` | `Long` | `51.65` | 110,390.00 USD | 0.00 USD | 9,100.00 USD | `-7.41%` | `176.09` |
| `Live` | `Long` | `51.75` | 101,300.00 USD | 0.00 USD | 6,480.00 USD | `-7.23%` | `125.17` |
| `Live` | `Long` | `51.85` | 94,820.00 USD | 0.00 USD | 14,770.00 USD | `-7.05%` | `284.87` |
| `Live` | `Long` | `51.95` | 80,050.00 USD | 0.00 USD | 13,950.00 USD | `-6.87%` | `268.48` |
| `Live` | `Long` | `52.05` | 66,100.00 USD | 0.00 USD | 305.01 USD | `-6.70%` | `5.86` |
| `Live` | `Long` | `52.15` | 65,790.00 USD | 0.00 USD | 1,900.00 USD | `-6.52%` | `36.36` |
| `Live` | `Long` | `52.25` | 63,900.00 USD | 0.00 USD | 4,820.00 USD | `-6.34%` | `92.20` |
| `Live` | `Long` | `52.35` | 59,080.00 USD | 0.00 USD | 245.52 USD | `-6.16%` | `4.69` |
| `Live` | `Long` | `52.45` | 58,840.00 USD | 0.00 USD | 5,820.00 USD | `-5.98%` | `110.91` |
| `Live` | `Long` | `52.55` | 53,020.00 USD | 0.00 USD | 8,700.00 USD | `-5.80%` | `165.49` |
| `Live` | `Long` | `52.65` | 44,320.00 USD | 0.00 USD | 1,050.00 USD | `-5.62%` | `20.00` |
| `Live` | `Long` | `52.75` | 43,270.00 USD | 0.00 USD | 30,280.00 USD | `-5.44%` | `574.00` |
| `Live` | `Long` | `52.85` | 12,990.00 USD | 0.00 USD | 5,950.00 USD | `-5.26%` | `112.64` |
| `Live` | `Long` | `52.95` | 7,040.00 USD | 0.00 USD | 2,680.00 USD | `-5.08%` | `50.57` |
| `Live` | `Long` | `53.05` | 4,360.00 USD | 0.00 USD | 769.76 USD | `-4.90%` | `14.51` |
| `Live` | `Long` | `53.15` | 3,590.00 USD | 0.00 USD | 2,030.00 USD | `-4.72%` | `38.15` |
| `Live` | `Long` | `53.25` | 1,560.00 USD | 0.00 USD | 619.30 USD | `-4.54%` | `11.63` |
| `Live` | `Long` | `53.45` | 942.86 USD | 0.00 USD | 942.86 USD | `-4.19%` | `17.64` |
| `Live` | `Short` | `57.75` | 155.35 USD | 155.35 USD | 0.00 USD | `+3.52%` | `2.69` |
| `Live` | `Short` | `57.95` | 281.10 USD | 125.75 USD | 0.00 USD | `+3.88%` | `2.17` |
| `Live` | `Short` | `58.85` | 1,760.00 USD | 1,480.00 USD | 0.00 USD | `+5.49%` | `25.13` |
| `Live` | `Short` | `59.35` | 11,200.00 USD | 9,440.00 USD | 0.00 USD | `+6.39%` | `159.09` |
| `Live` | `Short` | `60.15` | 220,080.00 USD | 208,880.00 USD | 0.00 USD | `+7.82%` | `3,472.67` |
| `Live` | `Short` | `60.35` | 220,510.00 USD | 431.50 USD | 0.00 USD | `+8.18%` | `7.15` |
| `Live` | `Short` | `60.95` | 220,910.00 USD | 397.39 USD | 0.00 USD | `+9.26%` | `6.52` |
| `Live` | `Short` | `61.55` | 221,130.00 USD | 222.20 USD | 0.00 USD | `+10.33%` | `3.61` |
| `Live` | `Short` | `62.95` | 221,270.00 USD | 138.49 USD | 0.00 USD | `+12.84%` | `2.20` |
| `Live` | `Short` | `63.45` | 224,620.00 USD | 3,350.00 USD | 0.00 USD | `+13.74%` | `52.83` |
| `Live` | `Short` | `63.55` | 232,800.00 USD | 8,180.00 USD | 0.00 USD | `+13.92%` | `128.67` |
| `Live` | `Short` | `67.05` | 232,920.00 USD | 121.36 USD | 0.00 USD | `+20.19%` | `1.81` |
| `Live` | `Short` | `67.85` | 233,630.00 USD | 709.03 USD | 0.00 USD | `+21.63%` | `10.45` |
| `Live` | `Short` | `68.35` | 234,250.00 USD | 619.93 USD | 0.00 USD | `+22.52%` | `9.07` |
| `Live` | `Short` | `68.95` | 274,110.00 USD | 39,860.00 USD | 0.00 USD | `+23.60%` | `578.10` |
| `Live` | `Short` | `76.35` | 282,500.00 USD | 8,380.00 USD | 0.00 USD | `+36.86%` | `109.80` |
| `Live` | `Short` | `77.75` | 860,960.00 USD | 578,460.00 USD | 0.00 USD | `+39.37%` | `7,440.05` |
| `Live` | `Short` | `77.85` | 861,560.00 USD | 602.56 USD | 0.00 USD | `+39.55%` | `7.74` |
| `Live` | `Short` | `80.75` | 862,210.00 USD | 646.00 USD | 0.00 USD | `+44.75%` | `8.00` |
| `Live` | `Short` | `81.05` | 881,210.00 USD | 19,000.00 USD | 0.00 USD | `+45.29%` | `234.42` |
| `Live` | `Short` | `81.45` | 884,470.00 USD | 3,260.00 USD | 0.00 USD | `+46.01%` | `40.00` |
| `Live` | `Short` | `81.55` | 884,590.00 USD | 123.96 USD | 0.00 USD | `+46.19%` | `1.52` |
| `Live` | `Short` | `82.05` | 887,300.00 USD | 2,710.00 USD | 0.00 USD | `+47.08%` | `33.00` |
| `Live` | `Short` | `82.75` | 887,510.00 USD | 214.32 USD | 0.00 USD | `+48.34%` | `2.59` |
| `Live` | `Short` | `85.35` | 911,190.00 USD | 23,680.00 USD | 0.00 USD | `+53.00%` | `277.44` |
| `Live` | `Short` | `90.65` | 911,310.00 USD | 119.66 USD | 0.00 USD | `+62.50%` | `1.32` |
| `Live` | `Short` | `97.25` | 911,470.00 USD | 164.35 USD | 0.00 USD | `+74.33%` | `1.69` |
| `Live` | `Short` | `97.85` | 913,920.00 USD | 2,450.00 USD | 0.00 USD | `+75.41%` | `25.00` |
| `Live` | `Short` | `98.05` | 933,530.00 USD | 19,610.00 USD | 0.00 USD | `+75.76%` | `200.00` |
| `Live` | `Short` | `102.75` | 964,360.00 USD | 30,820.00 USD | 0.00 USD | `+84.19%` | `300.00` |
| `Live` | `Short` | `104.25` | 964,570.00 USD | 213.71 USD | 0.00 USD | `+86.88%` | `2.05` |
| `Live` | `Short` | `104.65` | 1,320,000.00 USD | 353,090.00 USD | 0.00 USD | `+87.60%` | `3,374.01` |
| `Live` | `Short` | `104.85` | 1,320,000.00 USD | 2,320.00 USD | 0.00 USD | `+87.95%` | `22.13` |
| `Live` | `Short` | `106.75` | 1,320,000.00 USD | 1,620.00 USD | 0.00 USD | `+91.36%` | `15.16` |
| `Live` | `Short` | `106.85` | 1,320,000.00 USD | 1,860.00 USD | 0.00 USD | `+91.54%` | `17.43` |
| `Live` | `Short` | `107.25` | 1,320,000.00 USD | 199.48 USD | 0.00 USD | `+92.26%` | `1.86` |
| `Live` | `Short` | `108.05` | 1,330,000.00 USD | 6,470.00 USD | 0.00 USD | `+93.69%` | `59.91` |
| `Live` | `Short` | `110.35` | 1,330,000.00 USD | 753.69 USD | 0.00 USD | `+97.81%` | `6.83` |
| `Live` | `Short` | `110.95` | 1,330,000.00 USD | 664.59 USD | 0.00 USD | `+98.89%` | `5.99` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `20.05` | 879,820.00 USD | 0.00 USD | 392.18 USD | `-64.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `22.05` | 879,430.00 USD | 0.00 USD | 2,310.00 USD | `-60.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.05` | 877,120.00 USD | 0.00 USD | 806.86 USD | `-55.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `25.35` | 876,320.00 USD | 0.00 USD | 1,560.00 USD | `-54.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `27.35` | 874,760.00 USD | 0.00 USD | 410.25 USD | `-50.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `30.05` | 874,350.00 USD | 0.00 USD | 281.57 USD | `-46.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `36.05` | 874,070.00 USD | 0.00 USD | 36,050.00 USD | `-35.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.55` | 838,020.00 USD | 0.00 USD | 37,550.00 USD | `-32.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `37.85` | 800,470.00 USD | 0.00 USD | 447.01 USD | `-32.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `38.35` | 800,020.00 USD | 0.00 USD | 73,350.00 USD | `-31.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.05` | 726,670.00 USD | 0.00 USD | 40,560.00 USD | `-30.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.45` | 686,120.00 USD | 0.00 USD | 489.57 USD | `-29.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `39.95` | 685,630.00 USD | 0.00 USD | 1,180.00 USD | `-28.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.05` | 684,440.00 USD | 0.00 USD | 9,840.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `40.95` | 674,610.00 USD | 0.00 USD | 2,060.00 USD | `-26.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.05` | 672,550.00 USD | 0.00 USD | 2,060.00 USD | `-26.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `41.55` | 670,490.00 USD | 0.00 USD | 2,960.00 USD | `-25.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.05` | 667,540.00 USD | 0.00 USD | 4,020.00 USD | `-24.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `42.65` | 663,520.00 USD | 0.00 USD | 3,000.00 USD | `-23.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.05` | 660,520.00 USD | 0.00 USD | 5,680.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `43.85` | 654,840.00 USD | 0.00 USD | 672.22 USD | `-21.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.35` | 654,170.00 USD | 0.00 USD | 329,970.00 USD | `-20.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.45` | 324,200.00 USD | 0.00 USD | 569.85 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.55` | 323,630.00 USD | 0.00 USD | 223.20 USD | `-20.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `44.65` | 323,410.00 USD | 0.00 USD | 391.13 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.05` | 323,010.00 USD | 0.00 USD | 7,080.00 USD | `-19.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `45.55` | 315,940.00 USD | 0.00 USD | 1,370.00 USD | `-18.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.15` | 314,570.00 USD | 0.00 USD | 553.80 USD | `-17.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.35` | 314,020.00 USD | 0.00 USD | 2,970.00 USD | `-16.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.45` | 311,050.00 USD | 0.00 USD | 3,080.00 USD | `-16.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `46.65` | 307,970.00 USD | 0.00 USD | 14,000.00 USD | `-16.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.05` | 293,970.00 USD | 0.00 USD | 158.56 USD | `-15.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.25` | 293,820.00 USD | 0.00 USD | 373.28 USD | `-15.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.35` | 293,440.00 USD | 0.00 USD | 849.46 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `47.95` | 292,590.00 USD | 0.00 USD | 1,150.00 USD | `-14.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.05` | 291,440.00 USD | 0.00 USD | 129.25 USD | `-13.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.15` | 291,310.00 USD | 0.00 USD | 303.35 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `48.85` | 291,010.00 USD | 0.00 USD | 1,740.00 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.05` | 289,270.00 USD | 0.00 USD | 981.00 USD | `-12.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.35` | 288,290.00 USD | 0.00 USD | 817.24 USD | `-11.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.45` | 287,470.00 USD | 0.00 USD | 237.85 USD | `-11.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.55` | 287,230.00 USD | 0.00 USD | 879.51 USD | `-11.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.85` | 286,350.00 USD | 0.00 USD | 108.17 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `49.95` | 286,250.00 USD | 0.00 USD | 298.20 USD | `-10.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.05` | 285,950.00 USD | 0.00 USD | 34,670.00 USD | `-10.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.15` | 251,270.00 USD | 0.00 USD | 6,410.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.35` | 244,860.00 USD | 0.00 USD | 459.70 USD | `-9.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `50.55` | 244,400.00 USD | 0.00 USD | 236.57 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.05` | 244,160.00 USD | 0.00 USD | 1,020.00 USD | `-8.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.15` | 243,140.00 USD | 0.00 USD | 439.89 USD | `-8.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.45` | 242,700.00 USD | 0.00 USD | 204.26 USD | `-7.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.65` | 242,500.00 USD | 0.00 USD | 11,560.00 USD | `-7.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.85` | 230,940.00 USD | 0.00 USD | 106.29 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `51.95` | 230,830.00 USD | 0.00 USD | 8,700.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.05` | 222,130.00 USD | 0.00 USD | 27,140.00 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.25` | 194,990.00 USD | 0.00 USD | 140.03 USD | `-6.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.55` | 194,850.00 USD | 0.00 USD | 18,390.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.65` | 176,460.00 USD | 0.00 USD | 5,460.00 USD | `-5.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.75` | 171,000.00 USD | 0.00 USD | 271.13 USD | `-5.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.85` | 170,730.00 USD | 0.00 USD | 2,840.00 USD | `-5.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `52.95` | 167,890.00 USD | 0.00 USD | 115.43 USD | `-5.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.05` | 167,770.00 USD | 0.00 USD | 9,240.00 USD | `-4.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.15` | 158,530.00 USD | 0.00 USD | 2,660.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.25` | 155,870.00 USD | 0.00 USD | 881.82 USD | `-4.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.35` | 154,990.00 USD | 0.00 USD | 25,130.00 USD | `-4.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.45` | 129,860.00 USD | 0.00 USD | 566.57 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.55` | 129,300.00 USD | 0.00 USD | 5,950.00 USD | `-4.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.65` | 123,350.00 USD | 0.00 USD | 1,370.00 USD | `-3.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.75` | 121,980.00 USD | 0.00 USD | 52,980.00 USD | `-3.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `53.85` | 68,990.00 USD | 0.00 USD | 462.03 USD | `-3.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.05` | 68,530.00 USD | 0.00 USD | 6,010.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.15` | 62,520.00 USD | 0.00 USD | 398.54 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.25` | 62,120.00 USD | 0.00 USD | 3,090.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.35` | 59,040.00 USD | 0.00 USD | 958.73 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.45` | 58,080.00 USD | 0.00 USD | 144.29 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.55` | 57,930.00 USD | 0.00 USD | 788.25 USD | `-2.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.65` | 57,150.00 USD | 0.00 USD | 13,660.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.75` | 43,480.00 USD | 0.00 USD | 198.74 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.85` | 43,280.00 USD | 0.00 USD | 398.21 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `54.95` | 42,890.00 USD | 0.00 USD | 909.97 USD | `-1.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.05` | 41,980.00 USD | 0.00 USD | 550.50 USD | `-1.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.15` | 41,430.00 USD | 0.00 USD | 199.09 USD | `-1.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.25` | 41,230.00 USD | 0.00 USD | 38,720.00 USD | `-0.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.35` | 2,500.00 USD | 0.00 USD | 198.71 USD | `-0.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.45` | 2,310.00 USD | 0.00 USD | 1,190.00 USD | `-0.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.55` | 1,110.00 USD | 0.00 USD | 156.65 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.65` | 954.56 USD | 0.00 USD | 556.50 USD | `-0.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `55.75` | 398.06 USD | 0.00 USD | 398.06 USD | `-0.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.85` | 797.54 USD | 797.54 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `55.95` | 990.57 USD | 193.03 USD | 0.00 USD | `+0.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.05` | 1,620.00 USD | 632.24 USD | 0.00 USD | `+0.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.15` | 1,820.00 USD | 197.65 USD | 0.00 USD | `+0.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.25` | 2,020.00 USD | 204.19 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.35` | 2,430.00 USD | 406.85 USD | 0.00 USD | `+1.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.45` | 2,840.00 USD | 407.57 USD | 0.00 USD | `+1.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.55` | 3,040.00 USD | 204.15 USD | 0.00 USD | `+1.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.65` | 3,160.00 USD | 121.23 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.75` | 3,370.00 USD | 203.73 USD | 0.00 USD | `+1.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.85` | 3,570.00 USD | 204.09 USD | 0.00 USD | `+1.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `56.95` | 4,340.00 USD | 765.41 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.05` | 4,930.00 USD | 596.17 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.15` | 5,140.00 USD | 204.03 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.25` | 6,580.00 USD | 1,440.00 USD | 0.00 USD | `+2.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.35` | 6,780.00 USD | 207.03 USD | 0.00 USD | `+2.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.45` | 7,130.00 USD | 344.70 USD | 0.00 USD | `+2.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.55` | 7,350.00 USD | 218.69 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.65` | 7,470.00 USD | 118.18 USD | 0.00 USD | `+3.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `57.75` | 7,580.00 USD | 119.54 USD | 0.00 USD | `+3.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.05` | 8,330.00 USD | 747.68 USD | 0.00 USD | `+4.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.15` | 8,530.00 USD | 200.04 USD | 0.00 USD | `+4.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.25` | 8,730.00 USD | 200.96 USD | 0.00 USD | `+4.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.35` | 8,930.00 USD | 194.31 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.45` | 9,530.00 USD | 601.45 USD | 0.00 USD | `+4.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.55` | 9,750.00 USD | 223.66 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.75` | 10,240.00 USD | 491.15 USD | 0.00 USD | `+5.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.85` | 13,190.00 USD | 2,940.00 USD | 0.00 USD | `+5.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `58.95` | 13,320.00 USD | 129.69 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.05` | 18,120.00 USD | 4,800.00 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.15` | 19,400.00 USD | 1,280.00 USD | 0.00 USD | `+6.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.25` | 19,610.00 USD | 210.34 USD | 0.00 USD | `+6.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.35` | 20,070.00 USD | 461.74 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.45` | 20,230.00 USD | 159.92 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.65` | 20,950.00 USD | 724.75 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `59.85` | 21,110.00 USD | 158.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.05` | 21,280.00 USD | 171.14 USD | 0.00 USD | `+7.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.35` | 21,830.00 USD | 551.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.45` | 21,990.00 USD | 155.36 USD | 0.00 USD | `+8.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.55` | 22,870.00 USD | 878.58 USD | 0.00 USD | `+8.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.65` | 24,250.00 USD | 1,390.00 USD | 0.00 USD | `+8.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.85` | 25,240.00 USD | 986.99 USD | 0.00 USD | `+9.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `60.95` | 25,910.00 USD | 674.72 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.15` | 28,280.00 USD | 2,360.00 USD | 0.00 USD | `+9.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.25` | 28,400.00 USD | 125.56 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.45` | 32,000.00 USD | 3,600.00 USD | 0.00 USD | `+10.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `61.55` | 32,640.00 USD | 643.20 USD | 0.00 USD | `+10.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.05` | 32,770.00 USD | 130.31 USD | 0.00 USD | `+11.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.35` | 33,870.00 USD | 1,100.00 USD | 0.00 USD | `+11.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.55` | 35,120.00 USD | 1,250.00 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `62.65` | 35,840.00 USD | 716.72 USD | 0.00 USD | `+12.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.05` | 36,070.00 USD | 231.39 USD | 0.00 USD | `+13.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.15` | 36,700.00 USD | 630.87 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.25` | 37,410.00 USD | 703.97 USD | 0.00 USD | `+13.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.45` | 38,070.00 USD | 668.13 USD | 0.00 USD | `+13.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.55` | 48,490.00 USD | 10,420.00 USD | 0.00 USD | `+13.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `63.65` | 49,050.00 USD | 555.03 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.05` | 49,580.00 USD | 531.62 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.35` | 50,250.00 USD | 664.09 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.45` | 50,910.00 USD | 665.12 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.55` | 51,110.00 USD | 202.69 USD | 0.00 USD | `+15.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `64.65` | 51,410.00 USD | 298.04 USD | 0.00 USD | `+15.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.05` | 51,510.00 USD | 102.13 USD | 0.00 USD | `+16.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.15` | 52,050.00 USD | 540.09 USD | 0.00 USD | `+16.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.45` | 52,150.00 USD | 100.79 USD | 0.00 USD | `+17.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.55` | 52,420.00 USD | 262.20 USD | 0.00 USD | `+17.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `65.75` | 52,790.00 USD | 371.49 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.05` | 53,480.00 USD | 696.17 USD | 0.00 USD | `+18.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.75` | 54,020.00 USD | 534.00 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `66.95` | 65,100.00 USD | 11,080.00 USD | 0.00 USD | `+20.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `67.05` | 71,800.00 USD | 6,710.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.05` | 74,160.00 USD | 2,360.00 USD | 0.00 USD | `+21.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `68.35` | 79,030.00 USD | 4,860.00 USD | 0.00 USD | `+22.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.55` | 79,230.00 USD | 204.48 USD | 0.00 USD | `+24.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.65` | 597,430.00 USD | 518,200.00 USD | 0.00 USD | `+24.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `69.95` | 598,240.00 USD | 810.02 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.05` | 918,140.00 USD | 319,890.00 USD | 0.00 USD | `+25.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.85` | 918,310.00 USD | 170.04 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `70.95` | 924,070.00 USD | 5,770.00 USD | 0.00 USD | `+27.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.05` | 924,340.00 USD | 269.28 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `71.95` | 924,630.00 USD | 291.40 USD | 0.00 USD | `+28.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.05` | 931,850.00 USD | 7,220.00 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.25` | 932,000.00 USD | 156.78 USD | 0.00 USD | `+29.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `72.65` | 935,230.00 USD | 3,220.00 USD | 0.00 USD | `+30.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `73.55` | 935,640.00 USD | 411.14 USD | 0.00 USD | `+31.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.05` | 1,060,000.00 USD | 123,190.00 USD | 0.00 USD | `+32.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.55` | 1,060,000.00 USD | 1,020.00 USD | 0.00 USD | `+33.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.75` | 1,060,000.00 USD | 811.04 USD | 0.00 USD | `+34.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `74.95` | 1,060,000.00 USD | 104.93 USD | 0.00 USD | `+34.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.05` | 1,060,000.00 USD | 133.59 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.25` | 1,060,000.00 USD | 402.59 USD | 0.00 USD | `+34.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `75.85` | 1,060,000.00 USD | 308.71 USD | 0.00 USD | `+35.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `77.25` | 1,060,000.00 USD | 315.18 USD | 0.00 USD | `+38.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `78.65` | 1,120,000.00 USD | 59,310.00 USD | 0.00 USD | `+40.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.05` | 1,120,000.00 USD | 3,160.00 USD | 0.00 USD | `+41.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.35` | 1,130,000.00 USD | 5,260.00 USD | 0.00 USD | `+42.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `79.75` | 1,140,000.00 USD | 5,690.00 USD | 0.00 USD | `+42.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.05` | 1,170,000.00 USD | 36,590.00 USD | 0.00 USD | `+43.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `80.95` | 1,170,000.00 USD | 433.89 USD | 0.00 USD | `+45.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `81.05` | 1,170,000.00 USD | 172.64 USD | 0.00 USD | `+45.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.05` | 1,170,000.00 USD | 164.10 USD | 0.00 USD | `+47.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `82.85` | 1,170,000.00 USD | 546.81 USD | 0.00 USD | `+48.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `84.05` | 1,180,000.00 USD | 2,300.00 USD | 0.00 USD | `+50.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `85.05` | 1,190,000.00 USD | 12,070.00 USD | 0.00 USD | `+52.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.05` | 1,210,000.00 USD | 20,230.00 USD | 0.00 USD | `+56.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `87.95` | 1,210,000.00 USD | 1,580.00 USD | 0.00 USD | `+57.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.05` | 1,250,000.00 USD | 37,000.00 USD | 0.00 USD | `+57.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `88.95` | 1,250,000.00 USD | 473.21 USD | 0.00 USD | `+59.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.05` | 1,250,000.00 USD | 422.99 USD | 0.00 USD | `+59.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `89.45` | 1,250,000.00 USD | 1,630.00 USD | 0.00 USD | `+60.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `90.05` | 1,250,000.00 USD | 4,880.00 USD | 0.00 USD | `+61.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `91.55` | 1,250,000.00 USD | 481.55 USD | 0.00 USD | `+64.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `92.05` | 1,260,000.00 USD | 1,330.00 USD | 0.00 USD | `+65.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `94.05` | 1,260,000.00 USD | 375.26 USD | 0.00 USD | `+68.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.05` | 1,520,000.00 USD | 266,140.00 USD | 0.00 USD | `+70.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `95.35` | 1,530,000.00 USD | 3,400.00 USD | 0.00 USD | `+70.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `96.05` | 1,550,000.00 USD | 21,930.00 USD | 0.00 USD | `+72.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `98.05` | 1,550,000.00 USD | 294.15 USD | 0.00 USD | `+75.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `99.05` | 1,560,000.00 USD | 15,380.00 USD | 0.00 USD | `+77.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `100.05` | 1,570,000.00 USD | 3,660.00 USD | 0.00 USD | `+79.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `102.05` | 1,570,000.00 USD | 306.15 USD | 0.00 USD | `+82.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.05` | 1,570,000.00 USD | 936.72 USD | 0.00 USD | `+84.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `103.15` | 1,570,000.00 USD | 2,920.00 USD | 0.00 USD | `+84.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `108.05` | 1,570,000.00 USD | 324.15 USD | 0.00 USD | `+93.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `109.05` | 1,570,000.00 USD | 123.23 USD | 0.00 USD | `+95.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `111.05` | 1,660,000.00 USD | 89,110.00 USD | 0.00 USD | `+99.07%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `48.10` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 0.00 USD | 5,690.00 USD | 0.00 USD |
| `7D` | `48.20` | 8,480,000.00 USD | 0.00 USD | 8,480,000.00 USD | 0.00 USD | 5,540.00 USD | 0.00 USD |
| `7D` | `48.40` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 0.00 USD | 6,080.00 USD | 0.00 USD |
| `7D` | `48.60` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 2,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `48.80` | 8,470,000.00 USD | 0.00 USD | 8,470,000.00 USD | 1,780.00 USD | 2,250.00 USD | 0.00 USD |
| `7D` | `48.90` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 0.00 USD | 0.00 USD | 960.40 USD |
| `7D` | `49.30` | 8,460,000.00 USD | 0.00 USD | 8,460,000.00 USD | 15,190.00 USD | 4,490.00 USD | 14,870.00 USD |
| `7D` | `49.40` | 8,430,000.00 USD | 0.00 USD | 8,430,000.00 USD | 1,320.00 USD | 6,440.00 USD | 516.91 USD |
| `7D` | `49.50` | 8,420,000.00 USD | 0.00 USD | 8,420,000.00 USD | 2,830.00 USD | 7,770.00 USD | 0.00 USD |
| `1D` | `49.60` | 4,570,000.00 USD | 0.00 USD | 4,570,000.00 USD | 5,570.00 USD | 14,890.00 USD | 16,210.00 USD |
| `7D` | `49.60` | 8,410,000.00 USD | 0.00 USD | 8,410,000.00 USD | 1,200.00 USD | 1,260.00 USD | 12,210.00 USD |
| `1D` | `49.70` | 4,530,000.00 USD | 0.00 USD | 4,530,000.00 USD | 12,650.00 USD | 3,970.00 USD | 8,070.00 USD |
| `7D` | `49.70` | 8,390,000.00 USD | 0.00 USD | 8,390,000.00 USD | 12,090.00 USD | 0.00 USD | 13,440.00 USD |
| `1D` | `49.80` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 6,420.00 USD | 11,200.00 USD | 23,300.00 USD |
| `7D` | `49.80` | 8,370,000.00 USD | 0.00 USD | 8,370,000.00 USD | 9,930.00 USD | 8,220.00 USD | 0.00 USD |
| `1D` | `49.90` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 24,520.00 USD | 20,290.00 USD | 28,260.00 USD |
| `7D` | `49.90` | 8,350,000.00 USD | 0.00 USD | 8,350,000.00 USD | 45,030.00 USD | 19,560.00 USD | 10,160.00 USD |
| `1D` | `50.00` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 21,740.00 USD | 32,170.00 USD | 47,790.00 USD |
| `7D` | `50.00` | 8,270,000.00 USD | 0.00 USD | 8,270,000.00 USD | 29,070.00 USD | 39,440.00 USD | 25,110.00 USD |
| `1D` | `50.10` | 4,290,000.00 USD | 0.00 USD | 4,290,000.00 USD | 7,310.00 USD | 11,600.00 USD | 7,600.00 USD |
| `7D` | `50.10` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 363.50 USD | 682.90 USD | 8,340.00 USD |
| `1D` | `50.20` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 177.10 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `50.20` | 8,170,000.00 USD | 0.00 USD | 8,170,000.00 USD | 6,960.00 USD | 500.40 USD | 42,940.00 USD |
| `1D` | `50.30` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 171.03 USD | 3,880.00 USD | 2,500.00 USD |
| `7D` | `50.30` | 8,120,000.00 USD | 0.00 USD | 8,120,000.00 USD | 16,270.00 USD | 10,780.00 USD | 7,240.00 USD |
| `1D` | `50.40` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 8,260.00 USD | 11,890.00 USD | 1,150.00 USD |
| `7D` | `50.40` | 8,090,000.00 USD | 0.00 USD | 8,090,000.00 USD | 28,280.00 USD | 26,580.00 USD | 33,450.00 USD |
| `1D` | `50.50` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 8,910.00 USD | 8,790.00 USD | 10,530.00 USD |
| `7D` | `50.50` | 8,000,000.00 USD | 0.00 USD | 8,000,000.00 USD | 32,490.00 USD | 6,790.00 USD | 44,380.00 USD |
| `1D` | `50.60` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 7,330.00 USD | 3,440.00 USD | 10,850.00 USD |
| `7D` | `50.60` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 67,580.00 USD | 21,530.00 USD | 31,730.00 USD |
| `1D` | `50.70` | 4,180,000.00 USD | 0.00 USD | 4,180,000.00 USD | 8,170.00 USD | 2,300.00 USD | 11,770.00 USD |
| `7D` | `50.70` | 7,790,000.00 USD | 0.00 USD | 7,790,000.00 USD | 65,920.00 USD | 32,820.00 USD | 41,580.00 USD |
| `1D` | `50.80` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 12,550.00 USD | 3,100.00 USD | 8,280.00 USD |
| `7D` | `50.80` | 7,650,000.00 USD | 0.00 USD | 7,650,000.00 USD | 48,340.00 USD | 8,550.00 USD | 39,820.00 USD |
| `1D` | `50.90` | 4,130,000.00 USD | 0.00 USD | 4,130,000.00 USD | 826.24 USD | 260.05 USD | 8,390.00 USD |
| `7D` | `50.90` | 7,560,000.00 USD | 0.00 USD | 7,560,000.00 USD | 57,110.00 USD | 58,070.00 USD | 138,810.00 USD |
| `1D` | `51.00` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 5,040.00 USD | 0.00 USD | 430.77 USD |
| `7D` | `51.00` | 7,300,000.00 USD | 0.00 USD | 7,300,000.00 USD | 66,570.00 USD | 27,560.00 USD | 30,890.00 USD |
| `1D` | `51.10` | 4,120,000.00 USD | 0.00 USD | 4,120,000.00 USD | 9,210.00 USD | 6,650.00 USD | 0.00 USD |
| `7D` | `51.10` | 7,180,000.00 USD | 0.00 USD | 7,180,000.00 USD | 41,150.00 USD | 14,320.00 USD | 26,610.00 USD |
| `1D` | `51.20` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 1,770.00 USD | 1,130.00 USD | 19,220.00 USD |
| `7D` | `51.20` | 7,100,000.00 USD | 0.00 USD | 7,100,000.00 USD | 28,370.00 USD | 7,830.00 USD | 27,730.00 USD |
| `1D` | `51.30` | 4,080,000.00 USD | 0.00 USD | 4,080,000.00 USD | 8,650.00 USD | 9,710.00 USD | 0.00 USD |
| `7D` | `51.30` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 28,400.00 USD | 26,720.00 USD | 47,090.00 USD |
| `1D` | `51.40` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 3,250.00 USD | 5,460.00 USD | 416.23 USD |
| `7D` | `51.40` | 6,930,000.00 USD | 0.00 USD | 6,930,000.00 USD | 73,130.00 USD | 42,820.00 USD | 46,140.00 USD |
| `1D` | `51.50` | 4,050,000.00 USD | 0.00 USD | 4,050,000.00 USD | 7,580.00 USD | 10,010.00 USD | 41,580.00 USD |
| `7D` | `51.50` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 38,520.00 USD | 23,710.00 USD | 36,170.00 USD |
| `1D` | `51.60` | 3,990,000.00 USD | 0.00 USD | 3,990,000.00 USD | 5,990.00 USD | 17,860.00 USD | 709.44 USD |
| `7D` | `51.60` | 6,670,000.00 USD | 0.00 USD | 6,670,000.00 USD | 37,880.00 USD | 36,790.00 USD | 41,490.00 USD |
| `1D` | `51.70` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 2,660.00 USD | 12,840.00 USD | 44.86 USD |
| `7D` | `51.70` | 6,550,000.00 USD | 0.00 USD | 6,550,000.00 USD | 9,540.00 USD | 22,540.00 USD | 5,040.00 USD |
| `1D` | `51.80` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 10,010.00 USD | 18,760.00 USD | 12,840.00 USD |
| `7D` | `51.80` | 6,520,000.00 USD | 0.00 USD | 6,520,000.00 USD | 24,050.00 USD | 12,820.00 USD | 19,680.00 USD |
| `1D` | `51.90` | 3,910,000.00 USD | 0.00 USD | 3,910,000.00 USD | 10,800.00 USD | 19,550.00 USD | 21,410.00 USD |
| `7D` | `51.90` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 5,870.00 USD | 25,410.00 USD | 28,190.00 USD |
| `1D` | `52.00` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 15,280.00 USD | 24,580.00 USD | 16,810.00 USD |
| `7D` | `52.00` | 6,400,000.00 USD | 0.00 USD | 6,400,000.00 USD | 65,840.00 USD | 26,440.00 USD | 11,880.00 USD |
| `1D` | `52.10` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 30,730.00 USD | 17,300.00 USD | 40,580.00 USD |
| `7D` | `52.10` | 6,300,000.00 USD | 0.00 USD | 6,300,000.00 USD | 24,220.00 USD | 28,090.00 USD | 37,880.00 USD |
| `1D` | `52.20` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 13,190.00 USD | 5,050.00 USD | 49,960.00 USD |
| `7D` | `52.20` | 6,210,000.00 USD | 0.00 USD | 6,210,000.00 USD | 38,380.00 USD | 13,960.00 USD | 25,270.00 USD |
| `1D` | `52.30` | 3,650,000.00 USD | 0.00 USD | 3,650,000.00 USD | 26,510.00 USD | 22,090.00 USD | 11,210.00 USD |
| `7D` | `52.30` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 26,450.00 USD | 40,700.00 USD | 7,980.00 USD |
| `1D` | `52.40` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 15,630.00 USD | 15,400.00 USD | 7,040.00 USD |
| `7D` | `52.40` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 20,580.00 USD | 38,950.00 USD | 19,520.00 USD |
| `1D` | `52.50` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 53,990.00 USD | 30,000.00 USD | 79,400.00 USD |
| `7D` | `52.50` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 38,650.00 USD | 0.00 USD | 11,240.00 USD |
| `1D` | `52.60` | 3,380,000.00 USD | 0.00 USD | 3,380,000.00 USD | 9,060.00 USD | 43,700.00 USD | 5,450.00 USD |
| `7D` | `52.60` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 60,960.00 USD | 31,860.00 USD | 59,410.00 USD |
| `1D` | `52.70` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 18,270.00 USD | 19,780.00 USD | 40,000.00 USD |
| `7D` | `52.70` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 18,590.00 USD | 75,910.00 USD | 108,640.00 USD |
| `1D` | `52.80` | 3,250,000.00 USD | 0.00 USD | 3,250,000.00 USD | 28,880.00 USD | 50,850.00 USD | 72,920.00 USD |
| `7D` | `52.80` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 30,590.00 USD | 25,700.00 USD | 0.00 USD |
| `1D` | `52.90` | 3,090,000.00 USD | 0.00 USD | 3,090,000.00 USD | 44,710.00 USD | 55,550.00 USD | 30,100.00 USD |
| `7D` | `52.90` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 30,900.00 USD | 11,650.00 USD | 34,400.00 USD |
| `1D` | `53.00` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 31,870.00 USD | 34,720.00 USD | 52,280.00 USD |
| `7D` | `53.00` | 5,440,000.00 USD | 0.00 USD | 5,440,000.00 USD | 39,690.00 USD | 25,380.00 USD | 97,750.00 USD |
| `1D` | `53.10` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 12,590.00 USD | 66,450.00 USD | 88,790.00 USD |
| `7D` | `53.10` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 45,320.00 USD | 25,300.00 USD | 0.00 USD |
| `1D` | `53.20` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 36,030.00 USD | 39,410.00 USD | 55,630.00 USD |
| `7D` | `53.20` | 5,200,000.00 USD | 0.00 USD | 5,200,000.00 USD | 162,460.00 USD | 68,940.00 USD | 37,000.00 USD |
| `1D` | `53.30` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 28,400.00 USD | 56,180.00 USD | 16,210.00 USD |
| `7D` | `53.30` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 59,390.00 USD | 77,520.00 USD | 35,550.00 USD |
| `1D` | `53.40` | 2,450,000.00 USD | 0.00 USD | 2,450,000.00 USD | 12,600.00 USD | 31,610.00 USD | 15,400.00 USD |
| `7D` | `53.40` | 4,760,000.00 USD | 0.00 USD | 4,760,000.00 USD | 61,460.00 USD | 42,640.00 USD | 107,840.00 USD |
| `1D` | `53.50` | 2,390,000.00 USD | 0.00 USD | 2,390,000.00 USD | 21,250.00 USD | 27,740.00 USD | 22,000.00 USD |
| `7D` | `53.50` | 4,550,000.00 USD | 0.00 USD | 4,550,000.00 USD | 60,260.00 USD | 7,990.00 USD | 28,500.00 USD |
| `1D` | `53.60` | 2,320,000.00 USD | 0.00 USD | 2,320,000.00 USD | 75,950.00 USD | 3,830.00 USD | 20,970.00 USD |
| `7D` | `53.60` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 52,800.00 USD | 3,780.00 USD | 20,660.00 USD |
| `1D` | `53.70` | 2,210,000.00 USD | 0.00 USD | 2,210,000.00 USD | 6,210.00 USD | 11,100.00 USD | 11,960.00 USD |
| `7D` | `53.70` | 4,380,000.00 USD | 0.00 USD | 4,380,000.00 USD | 131,400.00 USD | 21,330.00 USD | 13,220.00 USD |
| `1D` | `53.80` | 2,190,000.00 USD | 0.00 USD | 2,190,000.00 USD | 53,640.00 USD | 28,920.00 USD | 4,830.00 USD |
| `7D` | `53.80` | 4,210,000.00 USD | 0.00 USD | 4,210,000.00 USD | 99,150.00 USD | 43,900.00 USD | 302.55 USD |
| `1D` | `53.90` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 49,810.00 USD | 39,560.00 USD | 27,830.00 USD |
| `7D` | `53.90` | 4,070,000.00 USD | 0.00 USD | 4,070,000.00 USD | 160,820.00 USD | 22,780.00 USD | 9,680.00 USD |
| `1D` | `54.00` | 1,980,000.00 USD | 0.00 USD | 1,980,000.00 USD | 76,010.00 USD | 30,780.00 USD | 86,580.00 USD |
| `7D` | `54.00` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 380,340.00 USD | 71,820.00 USD | 304,530.00 USD |
| `1D` | `54.10` | 1,790,000.00 USD | 0.00 USD | 1,790,000.00 USD | 105,010.00 USD | 27,610.00 USD | 74,530.00 USD |
| `7D` | `54.10` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 302,190.00 USD | 5,360.00 USD | 42,710.00 USD |
| `1D` | `54.20` | 1,580,000.00 USD | 0.00 USD | 1,580,000.00 USD | 72,600.00 USD | 62,320.00 USD | 47,360.00 USD |
| `7D` | `54.20` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 205,060.00 USD | 14,690.00 USD | 0.00 USD |
| `1D` | `54.30` | 1,400,000.00 USD | 0.00 USD | 1,400,000.00 USD | 46,340.00 USD | 65,810.00 USD | 32,500.00 USD |
| `7D` | `54.30` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 381,380.00 USD | 81,250.00 USD | 208,720.00 USD |
| `1D` | `54.40` | 1,250,000.00 USD | 0.00 USD | 1,250,000.00 USD | 102,880.00 USD | 147,860.00 USD | 24,330.00 USD |
| `7D` | `54.40` | 1,870,000.00 USD | 0.00 USD | 1,870,000.00 USD | 304,270.00 USD | 119,790.00 USD | 93,590.00 USD |
| `1D` | `54.50` | 978,370.00 USD | 0.00 USD | 978,370.00 USD | 24,100.00 USD | 106,190.00 USD | 30,800.00 USD |
| `7D` | `54.50` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 194,580.00 USD | 86,030.00 USD | 273,130.00 USD |
| `1D` | `54.60` | 817,270.00 USD | 0.00 USD | 817,270.00 USD | 25,070.00 USD | 69,570.00 USD | 43,580.00 USD |
| `7D` | `54.60` | 803,330.00 USD | 0.00 USD | 803,330.00 USD | 18,530.00 USD | 11,010.00 USD | 131,380.00 USD |
| `1D` | `54.70` | 679,040.00 USD | 0.00 USD | 679,040.00 USD | 6,600.00 USD | 23,060.00 USD | 105,800.00 USD |
| `7D` | `54.70` | 642,400.00 USD | 0.00 USD | 642,400.00 USD | 0.00 USD | 3,600.00 USD | 41,310.00 USD |
| `1D` | `54.80` | 543,580.00 USD | 0.00 USD | 543,580.00 USD | 0.00 USD | 48,420.00 USD | 23,920.00 USD |
| `7D` | `54.80` | 597,490.00 USD | 0.00 USD | 597,490.00 USD | 0.00 USD | 35,700.00 USD | 26,440.00 USD |
| `1D` | `54.90` | 471,240.00 USD | 0.00 USD | 471,240.00 USD | 66,900.00 USD | 65,440.00 USD | 10,850.00 USD |
| `7D` | `54.90` | 535,350.00 USD | 0.00 USD | 535,350.00 USD | 0.00 USD | 112,280.00 USD | 48,290.00 USD |
| `1D` | `55.00` | 328,060.00 USD | 0.00 USD | 328,060.00 USD | 40,710.00 USD | 54,150.00 USD | 55,190.00 USD |
| `7D` | `55.00` | 374,780.00 USD | 0.00 USD | 374,780.00 USD | 97,700.00 USD | 2,830.00 USD | 19,360.00 USD |
| `1D` | `55.10` | 178,000.00 USD | 0.00 USD | 178,000.00 USD | 50,530.00 USD | 0.00 USD | 80,200.00 USD |
| `7D` | `55.10` | 254,900.00 USD | 0.00 USD | 254,900.00 USD | 54,590.00 USD | 18,510.00 USD | 64,690.00 USD |
| `1D` | `55.20` | 47,280.00 USD | 0.00 USD | 47,280.00 USD | 39,390.00 USD | 7,890.00 USD | 0.00 USD |
| `7D` | `55.20` | 117,110.00 USD | 0.00 USD | 117,110.00 USD | 57,400.00 USD | 59,710.00 USD | 0.00 USD |
| `1D` | `55.30` | 52,860.00 USD | 52,860.00 USD | 0.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.30` | 105,720.00 USD | 105,720.00 USD | 0.00 USD | 52,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.30` | 23,140.00 USD | 23,140.00 USD | 0.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.30` | 46,280.00 USD | 46,280.00 USD | 0.00 USD | 23,140.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `55.40` | 51,080.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,800.00 USD |
| `1D` | `55.70` | 106,330.00 USD | 106,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 613.46 USD |
| `7D` | `55.70` | 225,330.00 USD | 225,330.00 USD | 0.00 USD | 174,240.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `55.80` | 109,510.00 USD | 109,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 3,170.00 USD |
| `7D` | `55.80` | 316,300.00 USD | 316,300.00 USD | 0.00 USD | 60,840.00 USD | 28,930.00 USD | 1,200.00 USD |
| `1D` | `55.90` | 162,570.00 USD | 162,570.00 USD | 0.00 USD | 51,520.00 USD | 0.00 USD | 1,550.00 USD |
| `7D` | `55.90` | 457,620.00 USD | 457,620.00 USD | 0.00 USD | 141,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `56.00` | 166,950.00 USD | 166,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 4,380.00 USD |
| `7D` | `56.00` | 628,740.00 USD | 628,740.00 USD | 0.00 USD | 2,590.00 USD | 0.00 USD | 168,520.00 USD |
| `1D` | `56.20` | 176,290.00 USD | 176,290.00 USD | 0.00 USD | 0.00 USD | 9,340.00 USD | 0.00 USD |
| `7D` | `56.20` | 708,680.00 USD | 708,680.00 USD | 0.00 USD | 0.00 USD | 79,940.00 USD | 0.00 USD |
| `1D` | `56.30` | 224,180.00 USD | 224,180.00 USD | 0.00 USD | 10,140.00 USD | 8,440.00 USD | 29,310.00 USD |
| `7D` | `56.30` | 756,750.00 USD | 756,750.00 USD | 0.00 USD | 0.00 USD | 5,360.00 USD | 42,710.00 USD |
| `1D` | `56.40` | 302,290.00 USD | 302,290.00 USD | 0.00 USD | 5,040.00 USD | 63,500.00 USD | 9,570.00 USD |
| `7D` | `56.40` | 785,120.00 USD | 785,120.00 USD | 0.00 USD | 2,650.00 USD | 25,730.00 USD | 0.00 USD |
| `1D` | `56.50` | 809,870.00 USD | 809,870.00 USD | 0.00 USD | 169,280.00 USD | 166,360.00 USD | 171,950.00 USD |
| `7D` | `56.50` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 170,750.00 USD | 224,670.00 USD | 33,450.00 USD |
| `1D` | `56.60` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 101,920.00 USD | 203,090.00 USD | 102,110.00 USD |
| `7D` | `56.60` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 363,190.00 USD | 242,530.00 USD | 1,460.00 USD |
| `1D` | `56.70` | 1,670,000.00 USD | 1,670,000.00 USD | 0.00 USD | 79,170.00 USD | 87,240.00 USD | 287,880.00 USD |
| `7D` | `56.70` | 2,300,000.00 USD | 2,300,000.00 USD | 0.00 USD | 152,150.00 USD | 192,280.00 USD | 132,200.00 USD |
| `1D` | `56.80` | 1,970,000.00 USD | 1,970,000.00 USD | 0.00 USD | 128,400.00 USD | 64,860.00 USD | 106,140.00 USD |
| `7D` | `56.80` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 172,110.00 USD | 101,860.00 USD | 318,330.00 USD |
| `1D` | `56.90` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 45,140.00 USD | 17,930.00 USD | 35,720.00 USD |
| `7D` | `56.90` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 113,780.00 USD | 52,200.00 USD | 307,930.00 USD |
| `1D` | `57.00` | 2,150,000.00 USD | 2,150,000.00 USD | 0.00 USD | 6,480.00 USD | 43,030.00 USD | 29,740.00 USD |
| `7D` | `57.00` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 88,680.00 USD | 56,390.00 USD | 178,370.00 USD |
| `1D` | `57.10` | 2,350,000.00 USD | 2,350,000.00 USD | 0.00 USD | 77,000.00 USD | 77,400.00 USD | 46,610.00 USD |
| `7D` | `57.10` | 3,820,000.00 USD | 3,820,000.00 USD | 0.00 USD | 36,580.00 USD | 79,290.00 USD | 21,040.00 USD |
| `1D` | `57.20` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 53,080.00 USD | 78,490.00 USD | 120,900.00 USD |
| `7D` | `57.20` | 3,990,000.00 USD | 3,990,000.00 USD | 0.00 USD | 118,850.00 USD | 23,920.00 USD | 23,060.00 USD |
| `1D` | `57.30` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 70,930.00 USD | 49,300.00 USD | 87,180.00 USD |
| `7D` | `57.30` | 4,190,000.00 USD | 4,190,000.00 USD | 0.00 USD | 76,940.00 USD | 28,570.00 USD | 98,930.00 USD |
| `1D` | `57.40` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 90,030.00 USD | 53,690.00 USD | 91,080.00 USD |
| `7D` | `57.40` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 124,180.00 USD | 74,860.00 USD | 277,080.00 USD |
| `1D` | `57.50` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 197,830.00 USD | 71,750.00 USD | 178,360.00 USD |
| `7D` | `57.50` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 99,810.00 USD | 39,170.00 USD | 0.00 USD |
| `1D` | `57.60` | 3,710,000.00 USD | 3,710,000.00 USD | 0.00 USD | 85,090.00 USD | 56,950.00 USD | 76,080.00 USD |
| `7D` | `57.60` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 149,560.00 USD | 81,050.00 USD | 41,970.00 USD |
| `1D` | `57.70` | 3,960,000.00 USD | 3,960,000.00 USD | 0.00 USD | 62,800.00 USD | 82,250.00 USD | 106,960.00 USD |
| `7D` | `57.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 58,380.00 USD | 58,050.00 USD |
| `1D` | `57.80` | 4,110,000.00 USD | 4,110,000.00 USD | 0.00 USD | 18,150.00 USD | 43,620.00 USD | 88,080.00 USD |
| `7D` | `57.80` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 27,080.00 USD | 49,750.00 USD | 66,100.00 USD |
| `1D` | `57.90` | 4,200,000.00 USD | 4,200,000.00 USD | 0.00 USD | 25,080.00 USD | 37,910.00 USD | 28,950.00 USD |
| `7D` | `57.90` | 5,390,000.00 USD | 5,390,000.00 USD | 0.00 USD | 14,390.00 USD | 5,510.00 USD | 30,010.00 USD |
| `1D` | `58.00` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 10,450.00 USD | 9,480.00 USD | 15,330.00 USD |
| `7D` | `58.00` | 5,500,000.00 USD | 5,500,000.00 USD | 0.00 USD | 0.00 USD | 5,470.00 USD | 107,350.00 USD |
| `1D` | `58.10` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 31,400.00 USD | 17,830.00 USD | 21,300.00 USD |
| `7D` | `58.10` | 5,540,000.00 USD | 5,540,000.00 USD | 0.00 USD | 5,470.00 USD | 19,160.00 USD | 14,070.00 USD |
| `1D` | `58.20` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 36,640.00 USD | 34,800.00 USD | 4,940.00 USD |
| `7D` | `58.20` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 0.00 USD | 31,590.00 USD | 302.55 USD |
| `1D` | `58.30` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 33,360.00 USD | 38,620.00 USD | 64,380.00 USD |
| `7D` | `58.30` | 5,670,000.00 USD | 5,670,000.00 USD | 0.00 USD | 48,850.00 USD | 11,000.00 USD | 36,500.00 USD |
| `1D` | `58.40` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 27,360.00 USD | 18,940.00 USD | 49,870.00 USD |
| `7D` | `58.40` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 27,290.00 USD | 9,260.00 USD | 86,460.00 USD |
| `1D` | `58.50` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 1,420.00 USD | 1,200.00 USD | 124.02 USD |
| `7D` | `58.50` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 2,060.00 USD | 24,530.00 USD | 0.00 USD |
| `1D` | `58.60` | 4,690,000.00 USD | 4,690,000.00 USD | 0.00 USD | 21,940.00 USD | 5,920.00 USD | 40,890.00 USD |
| `7D` | `58.60` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 30,680.00 USD | 20,260.00 USD | 51,650.00 USD |
| `1D` | `58.70` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 44,920.00 USD | 10,120.00 USD | 29,940.00 USD |
| `7D` | `58.70` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 15,810.00 USD | 11,600.00 USD | 35,320.00 USD |
| `1D` | `58.80` | 4,840,000.00 USD | 4,840,000.00 USD | 0.00 USD | 36,630.00 USD | 5,970.00 USD | 23,200.00 USD |
| `7D` | `58.80` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 3,840.00 USD | 3,320.00 USD | 6,410.00 USD |
| `1D` | `58.90` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 24,050.00 USD | 57,780.00 USD | 80,070.00 USD |
| `7D` | `58.90` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 2,140.00 USD | 54,240.00 USD | 83,500.00 USD |
| `1D` | `59.00` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 93,920.00 USD | 45,360.00 USD | 79,660.00 USD |
| `7D` | `59.00` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 259,280.00 USD | 65,270.00 USD | 118,570.00 USD |
| `1D` | `59.10` | 5,430,000.00 USD | 5,430,000.00 USD | 0.00 USD | 57,720.00 USD | 33,680.00 USD | 113,980.00 USD |
| `7D` | `59.10` | 6,880,000.00 USD | 6,880,000.00 USD | 0.00 USD | 93,390.00 USD | 45,400.00 USD | 158,780.00 USD |
| `1D` | `59.20` | 5,610,000.00 USD | 5,610,000.00 USD | 0.00 USD | 89,410.00 USD | 46,380.00 USD | 49,210.00 USD |
| `7D` | `59.20` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 153,580.00 USD | 18,540.00 USD | 174,600.00 USD |
| `1D` | `59.30` | 5,860,000.00 USD | 5,860,000.00 USD | 0.00 USD | 146,880.00 USD | 30,070.00 USD | 66,050.00 USD |
| `7D` | `59.30` | 7,500,000.00 USD | 7,500,000.00 USD | 0.00 USD | 88,710.00 USD | 67,460.00 USD | 114,310.00 USD |
| `1D` | `59.40` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 35,830.00 USD | 30,410.00 USD | 49,030.00 USD |
| `7D` | `59.40` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 107,040.00 USD | 73,620.00 USD | 124,910.00 USD |
| `1D` | `59.50` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 78,730.00 USD | 34,150.00 USD | 28,530.00 USD |
| `7D` | `59.50` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 67,060.00 USD | 61,370.00 USD | 21,090.00 USD |
| `1D` | `59.60` | 6,200,000.00 USD | 6,200,000.00 USD | 0.00 USD | 29,830.00 USD | 49,290.00 USD | 5,160.00 USD |
| `7D` | `59.60` | 8,320,000.00 USD | 8,320,000.00 USD | 0.00 USD | 184,700.00 USD | 106,840.00 USD | 72,920.00 USD |
| `1D` | `59.70` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 0.00 USD | 15,700.00 USD | 59,880.00 USD |
| `7D` | `59.70` | 8,640,000.00 USD | 8,640,000.00 USD | 0.00 USD | 55,510.00 USD | 99,970.00 USD | 162,850.00 USD |
| `1D` | `59.80` | 6,320,000.00 USD | 6,320,000.00 USD | 0.00 USD | 21,030.00 USD | 26,470.00 USD | 177.92 USD |
| `7D` | `59.80` | 9,000,000.00 USD | 9,000,000.00 USD | 0.00 USD | 118,240.00 USD | 91,980.00 USD | 154,560.00 USD |
| `1D` | `59.90` | 6,490,000.00 USD | 6,490,000.00 USD | 0.00 USD | 102,020.00 USD | 15,860.00 USD | 48,450.00 USD |
| `7D` | `59.90` | 9,210,000.00 USD | 9,210,000.00 USD | 0.00 USD | 142,290.00 USD | 34,490.00 USD | 29,380.00 USD |
| `1D` | `60.00` | 6,720,000.00 USD | 6,720,000.00 USD | 0.00 USD | 162,340.00 USD | 27,490.00 USD | 45,370.00 USD |
| `7D` | `60.00` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 100,570.00 USD | 67,520.00 USD | 83,920.00 USD |
| `1D` | `60.10` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 46,510.00 USD | 21,380.00 USD | 32,190.00 USD |
| `7D` | `60.10` | 9,840,000.00 USD | 9,840,000.00 USD | 0.00 USD | 200,540.00 USD | 84,980.00 USD | 95,670.00 USD |
| `1D` | `60.20` | 6,940,000.00 USD | 6,940,000.00 USD | 0.00 USD | 40,980.00 USD | 16,710.00 USD | 57,470.00 USD |
| `7D` | `60.20` | 10,210,000.00 USD | 10,210,000.00 USD | 0.00 USD | 162,230.00 USD | 99,360.00 USD | 108,990.00 USD |
| `1D` | `60.30` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 44,650.00 USD | 25,170.00 USD | 26,470.00 USD |
| `7D` | `60.30` | 10,610,000.00 USD | 10,610,000.00 USD | 0.00 USD | 133,350.00 USD | 100,380.00 USD | 170,480.00 USD |
| `1D` | `60.40` | 7,160,000.00 USD | 7,160,000.00 USD | 0.00 USD | 66,740.00 USD | 13,730.00 USD | 42,520.00 USD |
| `7D` | `60.40` | 10,970,000.00 USD | 10,970,000.00 USD | 0.00 USD | 55,050.00 USD | 100,560.00 USD | 202,370.00 USD |
| `1D` | `60.50` | 7,230,000.00 USD | 7,230,000.00 USD | 0.00 USD | 22,700.00 USD | 19,320.00 USD | 36,200.00 USD |
| `7D` | `60.50` | 11,340,000.00 USD | 11,340,000.00 USD | 0.00 USD | 115,390.00 USD | 80,510.00 USD | 169,260.00 USD |
| `1D` | `60.60` | 7,300,000.00 USD | 7,300,000.00 USD | 0.00 USD | 40,710.00 USD | 20,390.00 USD | 3,930.00 USD |
| `7D` | `60.60` | 11,720,000.00 USD | 11,720,000.00 USD | 0.00 USD | 251,100.00 USD | 16,970.00 USD | 118,680.00 USD |
| `1D` | `60.70` | 7,360,000.00 USD | 7,360,000.00 USD | 0.00 USD | 32,700.00 USD | 24,020.00 USD | 8,190.00 USD |
| `7D` | `60.70` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 76,200.00 USD | 37,000.00 USD | 23,900.00 USD |
| `1D` | `60.80` | 7,440,000.00 USD | 7,440,000.00 USD | 0.00 USD | 10,230.00 USD | 18,960.00 USD | 49,250.00 USD |
| `7D` | `60.80` | 12,010,000.00 USD | 12,010,000.00 USD | 0.00 USD | 46,960.00 USD | 28,960.00 USD | 76,200.00 USD |
| `1D` | `60.90` | 7,540,000.00 USD | 7,540,000.00 USD | 0.00 USD | 37,840.00 USD | 33,530.00 USD | 28,260.00 USD |
| `7D` | `60.90` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 105,970.00 USD | 43,970.00 USD | 70,380.00 USD |
| `1D` | `61.00` | 7,610,000.00 USD | 7,610,000.00 USD | 0.00 USD | 43,930.00 USD | 6,430.00 USD | 18,420.00 USD |
| `7D` | `61.00` | 12,290,000.00 USD | 12,290,000.00 USD | 0.00 USD | 43,120.00 USD | 11,530.00 USD | 0.00 USD |
| `1D` | `61.10` | 7,670,000.00 USD | 7,670,000.00 USD | 0.00 USD | 21,130.00 USD | 22,590.00 USD | 15,730.00 USD |
| `7D` | `61.10` | 12,340,000.00 USD | 12,340,000.00 USD | 0.00 USD | 31,540.00 USD | 21,750.00 USD | 189.67 USD |
| `1D` | `61.20` | 7,800,000.00 USD | 7,800,000.00 USD | 0.00 USD | 74,800.00 USD | 9,580.00 USD | 41,920.00 USD |
| `7D` | `61.20` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 51,570.00 USD | 29,220.00 USD | 47,810.00 USD |
| `1D` | `61.30` | 7,820,000.00 USD | 7,820,000.00 USD | 0.00 USD | 3,530.00 USD | 11,600.00 USD | 7,600.00 USD |
| `7D` | `61.30` | 12,520,000.00 USD | 12,520,000.00 USD | 0.00 USD | 14,390.00 USD | 13,210.00 USD | 24,230.00 USD |
| `1D` | `61.40` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 1,190.00 USD | 709.61 USD | 5,230.00 USD |
| `7D` | `61.40` | 12,650,000.00 USD | 12,650,000.00 USD | 0.00 USD | 60,410.00 USD | 25,720.00 USD | 43,510.00 USD |
| `1D` | `61.50` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 1,060.00 USD | 2,590.00 USD | 2,290.00 USD |
| `7D` | `61.50` | 12,750,000.00 USD | 12,750,000.00 USD | 0.00 USD | 17,710.00 USD | 42,440.00 USD | 41,390.00 USD |
| `7D` | `61.60` | 12,970,000.00 USD | 12,970,000.00 USD | 0.00 USD | 32,920.00 USD | 58,350.00 USD | 121,470.00 USD |
| `7D` | `61.70` | 13,160,000.00 USD | 13,160,000.00 USD | 0.00 USD | 82,860.00 USD | 10,880.00 USD | 99,740.00 USD |
| `7D` | `61.80` | 13,430,000.00 USD | 13,430,000.00 USD | 0.00 USD | 169,680.00 USD | 25,670.00 USD | 71,530.00 USD |
| `7D` | `61.90` | 13,570,000.00 USD | 13,570,000.00 USD | 0.00 USD | 73,690.00 USD | 32,820.00 USD | 41,580.00 USD |
| `7D` | `62.00` | 13,670,000.00 USD | 13,670,000.00 USD | 0.00 USD | 50,080.00 USD | 8,550.00 USD | 40,590.00 USD |
| `7D` | `62.10` | 13,680,000.00 USD | 13,680,000.00 USD | 0.00 USD | 9,410.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `62.20` | 13,790,000.00 USD | 13,790,000.00 USD | 0.00 USD | 34,230.00 USD | 34,620.00 USD | 41,360.00 USD |
| `7D` | `62.30` | 13,900,000.00 USD | 13,900,000.00 USD | 0.00 USD | 25,910.00 USD | 23,450.00 USD | 57,530.00 USD |
| `7D` | `62.40` | 14,010,000.00 USD | 14,010,000.00 USD | 0.00 USD | 62,940.00 USD | 25,250.00 USD | 25,440.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `408.63M` | Total OI Tokens: `7,362,015.7 LTC`
  * 1h OI Change: `+0.23%` | 4h OI Change: `-1.61%` | 24h OI Change: `-9.95%`
  * Exchange Breakdown: Binance=`71.90M` | Bybit=`66.36M` | OKX=`34.94M` | Hyperliquid=`22.19M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `10.21K` | Last 24h: `29.34K` | Last 3d: `56.60K` | Last 7d: `113.64K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0018%` |
| **USDT Bybit** | `0.0052%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0002%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `0.0100%` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `LTC` | `37.64%` | `62.36%` | `0.60` | 11,710,000.00 USD |
| `15M` | `Binance` | `43.24%` | `56.76%` | `0.76` | 3,470,000.00 USD |
| `15M` | `OKX` | `26.21%` | `73.79%` | `0.36` | 1,180,000.00 USD |
| `15M` | `Bybit` | `33.24%` | `66.76%` | `0.50` | 1,540,000.00 USD |
| `15M` | `KuCoin` | `34.49%` | `65.51%` | `0.53` | 67,350.00 USD |
| `15M` | `Gate` | `20.73%` | `79.27%` | `0.26` | 289,010.00 USD |
| `15M` | `Bitget` | `41.69%` | `58.31%` | `0.71` | 556,150.00 USD |
| `15M` | `BingX` | `63.83%` | `36.17%` | `1.76` | 565,740.00 USD |
| `15M` | `MEXC` | `20.21%` | `79.79%` | `0.25` | 986,090.00 USD |
| `15M` | `Bitunix` | `63.68%` | `36.32%` | `1.75` | 217,630.00 USD |
| `15M` | `Hyperliquid` | `36.43%` | `63.57%` | `0.57` | 1,040,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.14%` | `46.86%` | `1.13` | 133,750.00 USD |
| `15M` | `Crypto.com` | `5.02%` | `94.98%` | `0.05` | 1,810.00 USD |
| `15M` | `WhiteBIT` | `36.97%` | `63.03%` | `0.59` | 1,600,000.00 USD |
| `15M` | `HTX` | `90.95%` | `9.05%` | `10.05` | 1,820.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `48.45%` | `51.55%` | `0.94` | 34,880.00 USD |
| `15M` | `Aster` | `61.4%` | `38.6%` | `1.59` | 3,030.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `43.1%` | `56.9%` | `0.76` | 29,650.00 USD |
| `15M` | `Whale Positions` | `43.24%` | `56.76%` | `0.76` | 3,470,000.00 USD |
| `15M` | `Global Accounts` | `37.64%` | `62.36%` | `0.60` | 11,710,000.00 USD |
| `1H` | `LTC` | `48.59%` | `51.41%` | `0.95` | 59,950,000.00 USD |
| `1H` | `Binance` | `53.53%` | `46.47%` | `1.15` | 24,530,000.00 USD |
| `1H` | `OKX` | `46.37%` | `53.63%` | `0.86` | 5,540,000.00 USD |
| `1H` | `Bybit` | `48.76%` | `51.24%` | `0.95` | 7,160,000.00 USD |
| `1H` | `KuCoin` | `49.75%` | `50.25%` | `0.99` | 477,270.00 USD |
| `1H` | `Gate` | `41.24%` | `58.76%` | `0.70` | 1,210,000.00 USD |
| `1H` | `Bitget` | `43.38%` | `56.62%` | `0.77` | 3,300,000.00 USD |
| `1H` | `BingX` | `45.06%` | `54.94%` | `0.82` | 3,060,000.00 USD |
| `1H` | `MEXC` | `40.19%` | `59.81%` | `0.67` | 2,310,000.00 USD |
| `1H` | `Bitunix` | `50.52%` | `49.48%` | `1.02` | 1,000,000.00 USD |
| `1H` | `Hyperliquid` | `52.31%` | `47.69%` | `1.10` | 3,140,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `53.82%` | `46.18%` | `1.17` | 601,830.00 USD |
| `1H` | `Crypto.com` | `48.8%` | `51.2%` | `0.95` | 8,410.00 USD |
| `1H` | `WhiteBIT` | `38.27%` | `61.73%` | `0.62` | 6,430,000.00 USD |
| `1H` | `HTX` | `62.19%` | `37.81%` | `1.64` | 20,150.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `48.39%` | `51.61%` | `0.94` | 560,480.00 USD |
| `1H` | `Aster` | `36.07%` | `63.93%` | `0.56` | 439,480.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `52.89%` | `47.11%` | `1.12` | 163,810.00 USD |
| `1H` | `Whale Positions` | `53.53%` | `46.47%` | `1.15` | 24,530,000.00 USD |
| `1H` | `Global Accounts` | `48.59%` | `51.41%` | `0.95` | 59,950,000.00 USD |
| `4H` | `LTC` | `49.59%` | `50.41%` | `0.98` | 395,940,000.00 USD |
| `4H` | `Binance` | `53.17%` | `46.83%` | `1.14` | 168,160,000.00 USD |
| `4H` | `OKX` | `48.22%` | `51.78%` | `0.93` | 41,790,000.00 USD |
| `4H` | `Bybit` | `45.78%` | `54.22%` | `0.84` | 52,320,000.00 USD |
| `4H` | `KuCoin` | `54.24%` | `45.76%` | `1.19` | 4,070,000.00 USD |
| `4H` | `Gate` | `50.54%` | `49.46%` | `1.02` | 8,250,000.00 USD |
| `4H` | `Bitget` | `47.79%` | `52.21%` | `0.92` | 18,060,000.00 USD |
| `4H` | `BingX` | `43.84%` | `56.16%` | `0.78` | 18,980,000.00 USD |
| `4H` | `MEXC` | `48.06%` | `51.94%` | `0.93` | 13,520,000.00 USD |
| `4H` | `Bitunix` | `46.57%` | `53.43%` | `0.87` | 6,760,000.00 USD |
| `4H` | `Hyperliquid` | `51.25%` | `48.75%` | `1.05` | 37,460,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.29%` | `48.71%` | `1.05` | 1,770,000.00 USD |
| `4H` | `Crypto.com` | `57.36%` | `42.64%` | `1.35` | 67,510.00 USD |
| `4H` | `WhiteBIT` | `36.4%` | `63.6%` | `0.57` | 18,460,000.00 USD |
| `4H` | `HTX` | `59.28%` | `40.72%` | `1.46` | 432,060.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `44.92%` | `55.08%` | `0.82` | 2,700,000.00 USD |
| `4H` | `Aster` | `42.92%` | `57.08%` | `0.75` | 1,330,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `52.62%` | `47.38%` | `1.11` | 1,800,000.00 USD |
| `4H` | `Whale Positions` | `53.17%` | `46.83%` | `1.14` | 168,160,000.00 USD |
| `4H` | `Global Accounts` | `49.59%` | `50.41%` | `0.98` | 395,940,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `55.50` | `55.53` | `55.50` | `55.70` | `55.44` | 464,437.63 USD | 192,555.45 USD | 271,882.18 USD | -79,326.74 USD | `-17.08%` | `3B / 5S` |
| `5:00 UTC` | `55.42` | `55.46` | `55.42` | `55.59` | `55.39` | 371,902.17 USD | 185,679.40 USD | 186,222.77 USD | -543.37 USD | `-0.15%` | `2B / 4S` |
| `0:00 UTC` | `55.39` | `55.44` | `55.39` | `55.55` | `55.34` | 379,922.90 USD | 203,005.18 USD | 176,917.72 USD | 26,087.46 USD | `+6.87%` | `4B / 0S` |
| `5:00 UTC` | `55.42` | `55.40` | `55.42` | `55.52` | `55.27` | 934,212.03 USD | 256,275.15 USD | 677,936.88 USD | -421,661.72 USD | `-45.14%` | `0B / 6S` |
| `0:00 UTC` | `55.25` | `55.25` | `55.25` | `55.41` | `55.16` | 429,058.08 USD | 168,966.41 USD | 260,091.67 USD | -91,125.26 USD | `-21.24%` | `0B / 7S` |
| `5:00 UTC` | `55.55` | `55.41` | `55.55` | `55.62` | `55.11` | 1,970,804.61 USD | 831,054.50 USD | 1,139,750.11 USD | -308,695.61 USD | `-15.66%` | `11B / 5S` |
| `0:00 UTC` | `55.59` | `55.64` | `55.59` | `55.77` | `55.47` | 693,956.44 USD | 452,465.90 USD | 241,490.54 USD | 210,975.35 USD | `+30.40%` | `12B / 0S` |
| `5:00 UTC` | `55.45` | `55.55` | `55.45` | `55.80` | `55.41` | 1,274,778.93 USD | 334,913.45 USD | 939,865.48 USD | -604,952.03 USD | `-47.46%` | `4B / 16S` |
| `0:00 UTC` | `55.53` | `55.67` | `55.53` | `55.89` | `55.48` | 569,486.92 USD | 313,315.90 USD | 256,171.02 USD | 57,144.89 USD | `+10.03%` | `6B / 4S` |
| `5:00 UTC` | `55.28` | `55.32` | `55.28` | `55.50` | `55.22` | 406,148.95 USD | 193,109.55 USD | 213,039.40 USD | -19,929.85 USD | `-4.91%` | `3B / 8S` |

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
| `5m` | 3,710.00 USD | -193,880.00 USD | **`DISTRIBUTION`** |
| `15m` | -93,560.00 USD | -326,030.00 USD | **`DISTRIBUTION`** |
| `30m` | 28,850.00 USD | -79,910.00 USD | **`DISTRIBUTION`** |
| `1h` | 158,300.00 USD | -999,180.00 USD | **`DISTRIBUTION`** |
| `2h` | -19,760.00 USD | -1,750,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -100,290.00 USD | -2,560,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 198,460.00 USD | -2,340,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 393,670.00 USD | -3,780,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -522,770.00 USD | -6,050,000.00 USD | **`DISTRIBUTION`** |
| `24h` | 402,190.00 USD | -7,270,000.00 USD | **`DISTRIBUTION`** |
| `1w` | 4,730,000.00 USD | -24,890,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -23,940,000.00 USD | -200,760,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+3.71K` | 15m=`-93.56K` | 1h=`+158.30K` | 24h=`+402.19K`
* Futures Capital Netflows: 5m=`-193.88K` | 15m=`-326.03K` | 1h=`-999.18K` | 24h=`-7.27M`
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
  * Execution Entry: `54.64` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `52.99` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `58.76`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `56.07` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `57.72` (Risk Distance: `1.65` pts)
  * +2.5R Take Profit: `51.95`
  * Mathematical Lot Sizing: **`6.06 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`55.75`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
