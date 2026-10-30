# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 17:28:17 IST` (`2026-10-30 11:58:17 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.48` | **Live Ask Quote**: `8.51` | **Mid Price**: `8.50`
- **Spread Points**: `3.00` | **Spread BPS**: `35.31 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.35` | VWAP Z-Score: `+0.83` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0568` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `51.52` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.89` | Lower -3.00σ Band: `7.82`
  * Upper +2.51σ Band: `8.80` | Lower -2.51σ Band: `7.91`
  * Upper +2.01σ Band: `8.71` | Lower -2.01σ Band: `8.00`
  * Upper +2.00σ Band: `8.71` | Lower -2.00σ Band: `8.00`
  * Upper +1.28σ Band: `8.58` | Lower -1.28σ Band: `8.13`
  * Upper +1.00σ Band: `8.53` | Lower -1.00σ Band: `8.18`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.51` | EMA-20=`8.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.49` (Slope: `+0.0000`) | EMA-100=`8.54`
  * Institutional Anchors: EMA-144=`8.59` | EMA-200=`8.65` (Slope: `-0.2323`) | EMA-233=`8.67`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.59` (Distance: `-1.14%`)
  * Point of Control (POC) = `8.46` (Distance: `+0.42%`)
  * Value Area Low (VAL) = `8.26` (Distance: `+2.81%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.03` | Weekly POC=`8.92` | Weekly VAL=`8.68`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.59` | Low=`8.43`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.46` - `8.53`
  * Optimal Trade Entry (OTE 0.705): `8.51`
  * Structural Invalidation Anchor (0.786): `8.56`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.57` | `8.57` | `8.53` | `8.53` | `99,867` | 853,537.48 USD | -384,805.51 USD | `-45.08%` | -5,630,860.66 USD | `-2.86` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.53` | `8.56` | `8.53` | `8.55` | `35,183` | 300,605.99 USD | 114,644.89 USD | `+38.14%` | -5,516,215.77 USD | `+0.68` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.55` | `8.55` | `8.49` | `8.51` | `72,585` | 618,320.88 USD | -14,475.62 USD | `-2.34%` | -5,530,691.39 USD | `-0.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.59` | `8.59` | `8.55` | `8.57` | `82,707` | 708,615.56 USD | -9,982.60 USD | `-1.41%` | -5,098,155.94 USD | `+0.02` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.57` | `8.60` | `8.53` | `8.53` | `140,155` | 1,199,241.44 USD | -477,130.86 USD | `-39.79%` | -5,575,286.80 USD | `-1.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.53` | `8.56` | `8.49` | `8.51` | `107,768` | 918,926.88 USD | 100,169.27 USD | `+10.90%` | -5,475,117.53 USD | `+0.70` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.49` | `406,103` | 3,439,281.91 USD | -233,726.45 USD | `-6.80%` | -5,798,525.18 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.49` | `8.60` | `8.46` | `8.60` | `451,182` | 3,846,932.02 USD | 844,817.04 USD | `+21.96%` | -4,953,708.14 USD | `+0.63` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.60` | `8.62` | `8.49` | `8.51` | `439,240` | 3,759,648.36 USD | -521,409.39 USD | `-13.87%` | -5,475,117.53 USD | `-0.15` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.62` | `8.44` | `8.51` | `1,735,522` | 14,769,454.47 USD | -70,320.07 USD | `-0.48%` | -5,475,160.07 USD | `+0.57` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.62` | `8.44` | `8.51` | `1,735,522` | 14,769,454.47 USD | -70,320.07 USD | `-0.48%` | -5,475,160.07 USD | `+0.57` | **`BEARISH`** | `BEARISH ABSORPTION` |

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
| --- | **`8.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `8.50` | `85.8100` | 729.79 USD | 3,395.25 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.50` | `85.8300` | 729.90 USD | 2,665.46 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.50` | `85.8300` | 729.84 USD | 1,935.56 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.50` | `141.8000` | 1,205.73 USD | 1,205.73 USD | `1 orders` | `+0.02%` | `-` |
| `MID_SPREAD` | `8.50` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.50` | `0.00%` | `-` |
| `BID` | `8.50` | `135.2800` | 1,149.91 USD | 1,149.91 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `8.50` | `0.0100` | 0.09 USD | 1,149.99 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.50` | `85.8100` | 729.34 USD | 1,879.33 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.50` | `1940.3300` | 16,491.06 USD | 18,370.39 USD | `4 orders` | `-0.03%` | `-` |
| `BID` | `8.50` | `85.8300` | 729.47 USD | 19,099.86 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.50` | `85.8300` | 729.41 USD | 19,829.27 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.50` | `222.1600` | 1,887.96 USD | 21,717.23 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.50` | `38.2600` | 325.14 USD | 22,042.37 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `8.50` | `85.8300` | 729.35 USD | 22,771.72 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.50` | `11.8300` | 100.52 USD | 22,872.24 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.50` | `120.0800` | 1,020.36 USD | 23,892.60 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.50` | `39.8300` | 338.44 USD | 24,231.04 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.50` | `455.5400` | 3,870.72 USD | 28,101.76 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.50` | `85.8300` | 729.29 USD | 28,831.05 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.50` | `85.8300` | 729.28 USD | 29,560.33 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.50` | `1756.8400` | 14,927.34 USD | 44,487.67 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.50` | `5.8000` | 49.28 USD | 44,536.95 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.50` | `85.8100` | 729.04 USD | 45,265.99 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.50` | `588.5200` | 4,999.95 USD | 50,265.94 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.50` | `85.8600` | 729.44 USD | 50,995.38 USD | `1 orders` | `-0.07%` | `-` |
| `ASK` | `8.51` | `63.5200` | 540.57 USD | 53,112.11 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `8.51` | `940.1000` | 8,000.35 USD | 52,571.54 USD | `1 orders` | `+0.10%` | `-` |
| `ASK` | `8.51` | `1320.9600` | 11,240.71 USD | 44,571.20 USD | `3 orders` | `+0.09%` | `-` |
| `ASK` | `8.51` | `90.7100` | 771.89 USD | 33,330.49 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `8.51` | `85.8100` | 730.17 USD | 32,558.60 USD | `1 orders` | `+0.09%` | `-` |
| `ASK` | `8.51` | `5.8000` | 49.35 USD | 31,828.43 USD | `2 orders` | `+0.09%` | `-` |
| `ASK` | `8.51` | `25.2600` | 214.93 USD | 31,779.07 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.51` | `293.8100` | 2,499.94 USD | 31,564.14 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.51` | `85.8100` | 730.11 USD | 29,064.20 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.51` | `5.8700` | 49.94 USD | 28,334.10 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.51` | `1876.9200` | 15,969.02 USD | 28,284.15 USD | `2 orders` | `+0.08%` | `-` |
| `ASK` | `8.51` | `85.8100` | 730.05 USD | 12,315.13 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.51` | `705.2800` | 6,000.10 USD | 11,585.07 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.51` | `85.8100` | 729.99 USD | 5,584.98 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.51` | `85.8100` | 729.88 USD | 4,854.98 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.51` | `85.8100` | 729.85 USD | 4,125.10 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 17:23:48 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1475` | `0x7737...bf66` | `SHORT` | 1,455,188.81 USD | `171,568.06` | `7.43` | `8.48` | `110.82` | -179,643.80 USD | `-12.35%` | `10X Cross` |
| `1582` | `0xeadc...9d55` | `LONG` | 1,357,670.47 USD | `160,070.56` | `8.11` | `8.48` | `0.000000` | 60,032.89 USD | `+4.42%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.59` | 1,396.99 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 1.40K USD at 8.5921 USD [API] | `2026-10-29 20:40:49` |
| `ANNOUNCEMENT` | `INFO` | `8.56` | 849.01 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Liquidated Short: 0.85K USD at 8.5612 USD [API] | `2026-10-29 20:41:19` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.58%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.69%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.52%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.72%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+2.52%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--5.72%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 426,900.00 USD, Dist: `+8.70%`) | Long MP=`8.31` (Vol: 495,000.00 USD, Dist: `--2.68%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.98` | 1,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.02` | 223.28 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 110.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.12` | 565.80 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 252.43 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.23` | 257.03 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.33` | 267.38 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.73` | 10,990.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 232.67 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.90` | 332.93 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 1,150.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 21,430.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.15` | 23,480.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.35` | 905.85 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 8,600.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.62` | 590.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.16` | 159.68 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.18` | 390.54 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.42 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.58` | 107.56 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.78` | 525.25 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 3,320.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.87` | 310.14 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.88` | 505.68 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 4,110.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 352.68 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.03` | 216.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 710.03 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 954.05 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 915.43 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.14` | 3,070.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 421.89 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 159,630.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 640.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 4,530.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 688.15 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.95` | 147.55 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.22` | 795.06 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 354,280.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 1,420.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 287,230.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 829,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 827,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 822,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 822,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 822,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 1,050.00 USD | 815,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.49` | 1,480.00 USD | 814,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 6,030.00 USD | 812,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 806,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 805,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.55` | 1,510.00 USD | 796,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 795,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 792,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 364.90 USD | 790,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 245.89 USD | 790,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.66` | 1,740.00 USD | 789,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 788,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 786,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.70` | 15,800.00 USD | 783,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 767,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 756,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.72` | 2,200.00 USD | 750,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 748,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 747,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 739,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 717,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 219.12 USD | 711,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 8,520.00 USD | 711,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 158.14 USD | 703,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 702,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 699,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 3,990.00 USD | 699,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 695,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 694,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 691,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 691,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 683,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 683,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 554,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 553,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 532,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 531,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 507,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 500,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 499,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 497,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 468,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 13,410.00 USD | 468,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 454,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.17` | 4,470.00 USD | 434,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 430,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 428,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.24` | 2,500.00 USD | 428,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 185.83 USD | 425,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 21,280.00 USD | 425,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.27` | 7,140,000.00 USD | 7,140,000.00 USD | 360.23 USD | 1,810.00 USD | 5,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 404,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 368,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.30` | 29,220.00 USD | 366,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.31` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 104.04 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.33` | 13,110.00 USD | 337,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.34` | 1,400.00 USD | 324,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.35` | 7,130,000.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 406.69 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.36` | 5,290.00 USD | 322,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.37` | 2,940.00 USD | 317,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.37` | 7,130,000.00 USD | 7,130,000.00 USD | 45,620.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 314,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 227.97 USD | 313,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.39` | 7,080,000.00 USD | 7,080,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 313,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 2,430.00 USD | 312,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 310,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.45` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 308,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 297,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 293,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.49` | 7,010,000.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 291,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 290,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.51` | 6,990,000.00 USD | 6,990,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 290,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 288,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.53` | 6,970,000.00 USD | 6,970,000.00 USD | 35,990.00 USD | 18,910.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 287,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 1,510.00 USD | 283,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.55` | 6,910,000.00 USD | 6,910,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 1,070.00 USD | 281,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 280,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 255,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.59` | 5,910,000.00 USD | 5,910,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,900,000.00 USD | 5,900,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,900,000.00 USD | 5,900,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.61` | 6,890,000.00 USD | 6,890,000.00 USD | 626.55 USD | 0.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 255,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,880,000.00 USD | 5,880,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 254,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,870,000.00 USD | 5,870,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.63` | 6,890,000.00 USD | 6,890,000.00 USD | 41,300.00 USD | 2,130.00 USD | 1,680.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 253,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,860,000.00 USD | 5,860,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,820,000.00 USD | 5,820,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.65` | 6,840,000.00 USD | 6,840,000.00 USD | 4,870.00 USD | 2,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 253,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,810,000.00 USD | 5,810,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 253,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,800,000.00 USD | 5,800,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.67` | 6,840,000.00 USD | 6,840,000.00 USD | 1,110.00 USD | 0.00 USD | 34,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 140.45 USD | 253,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,800,000.00 USD | 5,800,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 252,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 252,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,790,000.00 USD | 5,790,000.00 USD | 4,490.00 USD | 4,000.00 USD | 19,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 5,770,000.00 USD | 5,770,000.00 USD | 660.12 USD | 5,720.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.71` | 6,800,000.00 USD | 6,800,000.00 USD | 393.33 USD | 1,650.00 USD | 33,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 5,750,000.00 USD | 5,750,000.00 USD | 2,920.00 USD | 1,840.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 5,740,000.00 USD | 5,740,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.73` | 6,770,000.00 USD | 6,770,000.00 USD | 39,770.00 USD | 2,520.00 USD | 7,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 5,730,000.00 USD | 5,730,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 5,710,000.00 USD | 5,710,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.75` | 6,720,000.00 USD | 6,720,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,360.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 245,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 5,700,000.00 USD | 5,700,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 244,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 5,700,000.00 USD | 5,700,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.77` | 6,660,000.00 USD | 6,660,000.00 USD | 20,120.00 USD | 4,900.00 USD | 6,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 12,100.00 USD | 244,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 5,680,000.00 USD | 5,680,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 232,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 5,670,000.00 USD | 5,670,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.79` | 6,630,000.00 USD | 6,630,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 228,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 5,640,000.00 USD | 5,640,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 224,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 5,630,000.00 USD | 5,630,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.81` | 6,530,000.00 USD | 6,530,000.00 USD | 3,970.00 USD | 11,570.00 USD | 1,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 5,630,000.00 USD | 5,630,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 217,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 5,630,000.00 USD | 5,630,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.83` | 6,510,000.00 USD | 6,510,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 5,590,000.00 USD | 5,590,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 215,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 5,590,000.00 USD | 5,590,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.85` | 6,460,000.00 USD | 6,460,000.00 USD | 17,330.00 USD | 7,840.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 5,580,000.00 USD | 5,580,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 193,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 5,560,000.00 USD | 5,560,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.87` | 6,420,000.00 USD | 6,420,000.00 USD | 150,960.00 USD | 1,540.00 USD | 22,350.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 193,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 5,520,000.00 USD | 5,520,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 5,320,000.00 USD | 5,320,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.89` | 6,240,000.00 USD | 6,240,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,270.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 13,270.00 USD | 192,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 5,230,000.00 USD | 5,230,000.00 USD | 56,410.00 USD | 6,970.00 USD | 4,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 179,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 5,160,000.00 USD | 5,160,000.00 USD | 11,200.00 USD | 10,370.00 USD | 26,070.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.91` | 6,050,000.00 USD | 6,050,000.00 USD | 31,740.00 USD | 26,330.00 USD | 45,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 5,120,000.00 USD | 5,120,000.00 USD | 15,830.00 USD | 2,040.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 176,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 5,090,000.00 USD | 5,090,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.93` | 5,950,000.00 USD | 5,950,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 171,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 5,070,000.00 USD | 5,070,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 155,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,980,000.00 USD | 4,980,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.95` | 5,850,000.00 USD | 5,850,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 155,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,850,000.00 USD | 4,850,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 4,770,000.00 USD | 4,770,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.97` | 5,690,000.00 USD | 5,690,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 27,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 4,740,000.00 USD | 4,740,000.00 USD | 5,610.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 25,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 4,690,000.00 USD | 4,690,000.00 USD | 3,980.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.99` | 5,590,000.00 USD | 5,590,000.00 USD | 53,780.00 USD | 20,640.00 USD | 122,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 889.52 USD | 24,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 4,680,000.00 USD | 4,680,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 4,590,000.00 USD | 4,590,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.01` | 5,400,000.00 USD | 5,400,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 4,580,000.00 USD | 4,580,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.03` | 4,500,000.00 USD | 4,500,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.03` | 5,290,000.00 USD | 5,290,000.00 USD | 353,080.00 USD | 35,720.00 USD | 49,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 4,470,000.00 USD | 4,470,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.05` | 4,410,000.00 USD | 4,410,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.05` | 4,850,000.00 USD | 4,850,000.00 USD | 390,130.00 USD | 0.00 USD | 63,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.06` | 4,030,000.00 USD | 4,030,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 23,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,810,000.00 USD | 3,810,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.07` | 4,390,000.00 USD | 4,390,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 23,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 3,670,000.00 USD | 3,670,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.09` | 887.25 USD | 1,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.09` | 3,590,000.00 USD | 3,590,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.09` | 4,260,000.00 USD | 4,260,000.00 USD | 32,760.00 USD | 0.00 USD | 81,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 3,550,000.00 USD | 3,550,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 3,390,000.00 USD | 3,390,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.11` | 4,140,000.00 USD | 4,140,000.00 USD | 33,000.00 USD | 0.00 USD | 140,250.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.12` | 3,120,000.00 USD | 3,120,000.00 USD | 20,660.00 USD | 11,230.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 521.62 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,960,000.00 USD | 2,960,000.00 USD | 35,600.00 USD | 9,180.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.13` | 3,970,000.00 USD | 3,970,000.00 USD | 48,900.00 USD | 12,740.00 USD | 20,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,910,000.00 USD | 2,910,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,780,000.00 USD | 2,780,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.15` | 3,890,000.00 USD | 3,890,000.00 USD | 179,060.00 USD | 31,560.00 USD | 183,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.16` | 2,670,000.00 USD | 2,670,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 2,480,000.00 USD | 2,480,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.17` | 3,490,000.00 USD | 3,490,000.00 USD | 1,590.00 USD | 13,650.00 USD | 149,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 2,280,000.00 USD | 2,280,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 2,260,000.00 USD | 2,260,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.19` | 3,330,000.00 USD | 3,330,000.00 USD | 1,200.00 USD | 72,340.00 USD | 23,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 2,230,000.00 USD | 2,230,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 2,180,000.00 USD | 2,180,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.21` | 3,230,000.00 USD | 3,230,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 2,140,000.00 USD | 2,140,000.00 USD | 6,810.00 USD | 3,080.00 USD | 21,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 2,110,000.00 USD | 2,110,000.00 USD | 0.00 USD | 3,450.00 USD | 10,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.23` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 40,910.00 USD | 5,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 2,100,000.00 USD | 2,100,000.00 USD | 5,700.00 USD | 6,390.00 USD | 9,270.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.25` | 2,990,000.00 USD | 2,990,000.00 USD | 129,050.00 USD | 12,050.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 2,030,000.00 USD | 2,030,000.00 USD | 50,590.00 USD | 12,510.00 USD | 25,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,940,000.00 USD | 1,940,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.27` | 2,830,000.00 USD | 2,830,000.00 USD | 103,730.00 USD | 4,000.00 USD | 37,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,880,000.00 USD | 1,880,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.29` | 2,680,000.00 USD | 2,680,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,830,000.00 USD | 1,830,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,720,000.00 USD | 1,720,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.31` | 2,490,000.00 USD | 2,490,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 1,570,000.00 USD | 1,570,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.33` | 2,110,000.00 USD | 2,110,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.35` | 2,070,000.00 USD | 2,070,000.00 USD | 223,170.00 USD | 0.00 USD | 5,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 1,410,000.00 USD | 1,410,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 1,390,000.00 USD | 1,390,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.37` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 1,370,000.00 USD | 1,370,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 1,300,000.00 USD | 1,300,000.00 USD | 114,370.00 USD | 19,770.00 USD | 43,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.39` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 15,860.00 USD | 68,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 1,120,000.00 USD | 1,120,000.00 USD | 10,500.00 USD | 10,400.00 USD | 72,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 1,020,000.00 USD | 1,020,000.00 USD | 11,070.00 USD | 12,780.00 USD | 18,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.41` | 1,720,000.00 USD | 1,720,000.00 USD | 194,850.00 USD | 0.00 USD | 100,330.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 981,740.00 USD | 981,740.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 922,590.00 USD | 922,590.00 USD | 81,350.00 USD | 7,730.00 USD | 11,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.43` | 1,430,000.00 USD | 1,430,000.00 USD | 163,340.00 USD | 12,610.00 USD | 22,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 821,850.00 USD | 821,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 617,870.00 USD | 617,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.45` | 1,230,000.00 USD | 1,230,000.00 USD | 156,410.00 USD | 8,000.00 USD | 171,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 557,120.00 USD | 557,120.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.47` | 894,220.00 USD | 894,220.00 USD | 0.00 USD | 0.00 USD | 38,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.48` | 556,450.00 USD | 556,450.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.49` | 555,700.00 USD | 555,700.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.49` | 855,480.00 USD | 855,480.00 USD | 0.00 USD | 0.00 USD | 153,260.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.51` | 702,220.00 USD | 702,220.00 USD | 0.00 USD | 0.00 USD | 92,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.52` | 555,690.00 USD | 555,690.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.53` | 397,060.00 USD | 397,060.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.53` | 609,830.00 USD | 609,830.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.54` | 372,880.00 USD | 372,880.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.55` | 174,470.00 USD | 174,470.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.55` | 435,070.00 USD | 435,070.00 USD | 434,770.00 USD | 0.00 USD | 300.56 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.56` | 147,690.00 USD | 147,690.00 USD | 686.73 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.57` | 147,010.00 USD | 147,010.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.57` | 4,370.00 USD | 4,370.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.57` | 8,740.00 USD | 8,740.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 842.65 USD | 842.65 USD | 842.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 1,690.00 USD | 1,690.00 USD | 842.65 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.59` | 9,770.00 USD | 9,770.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 3,720.00 USD | 3,720.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 4,920.00 USD | 4,920.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.61` | 12,860.00 USD | 12,860.00 USD | 2,810.00 USD | 0.00 USD | 271.28 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 172,190.00 USD | 172,190.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 303,890.00 USD | 303,890.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.63` | 41,370.00 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 385,870.00 USD | 385,870.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 447,970.00 USD | 447,970.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.65` | 92,290.00 USD | 92,290.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 477,280.00 USD | 477,280.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 490,680.00 USD | 490,680.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.67` | 105,620.00 USD | 105,620.00 USD | 0.00 USD | 11,770.00 USD | 1,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 530,190.00 USD | 530,190.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 606,050.00 USD | 606,050.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.69` | 346,630.00 USD | 346,630.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 700,570.00 USD | 700,570.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 727,270.00 USD | 727,270.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.71` | 444,860.00 USD | 444,860.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 816,520.00 USD | 816,520.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 921,660.00 USD | 921,660.00 USD | 26,200.00 USD | 34,960.00 USD | 43,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.73` | 516,230.00 USD | 516,230.00 USD | 51,030.00 USD | 19,040.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,000,000.00 USD | 1,000,000.00 USD | 38,500.00 USD | 6,910.00 USD | 33,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,080,000.00 USD | 1,080,000.00 USD | 44,580.00 USD | 15,310.00 USD | 23,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.75` | 779,400.00 USD | 779,400.00 USD | 196,960.00 USD | 19,690.00 USD | 46,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,230,000.00 USD | 1,230,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 1,440,000.00 USD | 1,440,000.00 USD | 155,740.00 USD | 2,060.00 USD | 47,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.77` | 1,040,000.00 USD | 1,040,000.00 USD | 141,710.00 USD | 12,610.00 USD | 105,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 1,560,000.00 USD | 1,560,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 1,640,000.00 USD | 1,640,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.79` | 1,170,000.00 USD | 1,170,000.00 USD | 29,660.00 USD | 33,300.00 USD | 65,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 1,790,000.00 USD | 1,790,000.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 1,860,000.00 USD | 1,860,000.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.81` | 1,380,000.00 USD | 1,380,000.00 USD | 122,920.00 USD | 26,890.00 USD | 58,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 1,940,000.00 USD | 1,940,000.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,140,000.00 USD | 2,140,000.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.83` | 1,620,000.00 USD | 1,620,000.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,210,000.00 USD | 2,210,000.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,240,000.00 USD | 2,240,000.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.85` | 1,710,000.00 USD | 1,710,000.00 USD | 29,310.00 USD | 5,880.00 USD | 58,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,250,000.00 USD | 2,250,000.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,260,000.00 USD | 2,260,000.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.87` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,280,000.00 USD | 2,280,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,330,000.00 USD | 2,330,000.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.89` | 1,810,000.00 USD | 1,810,000.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.90` | 2,440,000.00 USD | 2,440,000.00 USD | 35,510.00 USD | 9,060.00 USD | 70,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.91` | 2,510,000.00 USD | 2,510,000.00 USD | 32,240.00 USD | 13,320.00 USD | 23,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.91` | 1,910,000.00 USD | 1,910,000.00 USD | 2,440.00 USD | 4,130.00 USD | 94,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 2,530,000.00 USD | 2,530,000.00 USD | 6,640.00 USD | 6,390.00 USD | 9,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 2,610,000.00 USD | 2,610,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.93` | 2,090,000.00 USD | 2,090,000.00 USD | 157,480.00 USD | 6,300.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 2,680,000.00 USD | 2,680,000.00 USD | 50,590.00 USD | 12,260.00 USD | 5,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.95` | 3,140.00 USD | 11,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.95` | 2,710,000.00 USD | 2,710,000.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.95` | 2,210,000.00 USD | 2,210,000.00 USD | 74,920.00 USD | 4,000.00 USD | 38,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.96` | 227.82 USD | 11,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.96` | 2,710,000.00 USD | 2,710,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.97` | 2,210,000.00 USD | 2,210,000.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.98` | 2,780,000.00 USD | 2,780,000.00 USD | 36,060.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 2,850,000.00 USD | 2,850,000.00 USD | 49,090.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.99` | 2,400,000.00 USD | 2,400,000.00 USD | 147,500.00 USD | 6,550.00 USD | 29,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 551,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 2,920,000.00 USD | 2,920,000.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,000,000.00 USD | 3,000,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.01` | 2,760,000.00 USD | 2,760,000.00 USD | 303,030.00 USD | 36,180.00 USD | 23,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,070,000.00 USD | 3,070,000.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,240,000.00 USD | 3,240,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.03` | 2,980,000.00 USD | 2,980,000.00 USD | 107,490.00 USD | 101,140.00 USD | 15,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,300,000.00 USD | 3,300,000.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,360,000.00 USD | 3,360,000.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.05` | 3,080,000.00 USD | 3,080,000.00 USD | 38,740.00 USD | 17,700.00 USD | 39,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 551,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,400,000.00 USD | 3,400,000.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.07` | 3,450,000.00 USD | 3,450,000.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.07` | 3,130,000.00 USD | 3,130,000.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 3,490,000.00 USD | 3,490,000.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 3,600,000.00 USD | 3,600,000.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.09` | 3,440,000.00 USD | 3,440,000.00 USD | 152,640.00 USD | 8,680.00 USD | 144,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 555,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 3,660,000.00 USD | 3,660,000.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 3,800,000.00 USD | 3,800,000.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.11` | 4,920,000.00 USD | 4,920,000.00 USD | 877,120.00 USD | 37,620.00 USD | 570,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 3,950,000.00 USD | 3,950,000.00 USD | 94,950.00 USD | 21,650.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,070,000.00 USD | 4,070,000.00 USD | 75,800.00 USD | 15,960.00 USD | 35,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.13` | 6,100,000.00 USD | 6,100,000.00 USD | 668,090.00 USD | 26,540.00 USD | 484,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,120,000.00 USD | 4,120,000.00 USD | 20,200.00 USD | 0.00 USD | 24,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 555,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,210,000.00 USD | 4,210,000.00 USD | 56,980.00 USD | 20,890.00 USD | 13,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.15` | 6,770,000.00 USD | 6,770,000.00 USD | 357,020.00 USD | 38,700.00 USD | 270,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 4,330,000.00 USD | 4,330,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 4,460,000.00 USD | 4,460,000.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.17` | 7,620,000.00 USD | 7,620,000.00 USD | 409,650.00 USD | 133,490.00 USD | 303,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 4,540,000.00 USD | 4,540,000.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 4,660,000.00 USD | 4,660,000.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.19` | 8,420,000.00 USD | 8,420,000.00 USD | 504,150.00 USD | 108,440.00 USD | 193,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 4,770,000.00 USD | 4,770,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 4,810,000.00 USD | 4,810,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.21` | 9,430,000.00 USD | 9,430,000.00 USD | 590,780.00 USD | 144,470.00 USD | 277,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 4,880,000.00 USD | 4,880,000.00 USD | 58,060.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.22` | 416.69 USD | 555,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.23` | 4,890,000.00 USD | 4,890,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.23` | 10,440,000.00 USD | 10,440,000.00 USD | 582,450.00 USD | 92,780.00 USD | 331,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 4,930,000.00 USD | 4,930,000.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 4,970,000.00 USD | 4,970,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.25` | 10,840,000.00 USD | 10,840,000.00 USD | 277,290.00 USD | 61,940.00 USD | 61,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 4,970,000.00 USD | 4,970,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,000,000.00 USD | 5,000,000.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.27` | 11,140,000.00 USD | 11,140,000.00 USD | 156,190.00 USD | 102,670.00 USD | 37,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,010,000.00 USD | 5,010,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 326.09 USD | 556,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,050,000.00 USD | 5,050,000.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.29` | 11,860,000.00 USD | 11,860,000.00 USD | 392,980.00 USD | 82,050.00 USD | 244,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 560,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,110,000.00 USD | 5,110,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,160,000.00 USD | 5,160,000.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.31` | 12,420,000.00 USD | 12,420,000.00 USD | 308,150.00 USD | 44,500.00 USD | 209,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,180,000.00 USD | 5,180,000.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,210,000.00 USD | 5,210,000.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.33` | 12,670,000.00 USD | 12,670,000.00 USD | 134,040.00 USD | 29,420.00 USD | 82,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,270,000.00 USD | 5,270,000.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,300,000.00 USD | 5,300,000.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.35` | 12,940,000.00 USD | 12,940,000.00 USD | 114,090.00 USD | 67,130.00 USD | 96,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,320,000.00 USD | 5,320,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 5,340,000.00 USD | 5,340,000.00 USD | 12,860.00 USD | 6,780.00 USD | 4,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.37` | 13,280,000.00 USD | 13,280,000.00 USD | 211,790.00 USD | 34,660.00 USD | 85,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 5,370,000.00 USD | 5,370,000.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 5,380,000.00 USD | 5,380,000.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.39` | 13,600,000.00 USD | 13,600,000.00 USD | 206,980.00 USD | 32,960.00 USD | 87,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 5,400,000.00 USD | 5,400,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 5,420,000.00 USD | 5,420,000.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.41` | 14,000,000.00 USD | 14,000,000.00 USD | 265,720.00 USD | 30,790.00 USD | 99,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 1,450.00 USD | 561,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 5,440,000.00 USD | 5,440,000.00 USD | 9,600.00 USD | 3,630.00 USD | 8,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 5,450,000.00 USD | 5,450,000.00 USD | 5,380.00 USD | 1,380.00 USD | 3,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.43` | 14,090,000.00 USD | 14,090,000.00 USD | 33,890.00 USD | 15,080.00 USD | 42,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 5,460,000.00 USD | 5,460,000.00 USD | 3,010.00 USD | 1,840.00 USD | 3,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 5,460,000.00 USD | 5,460,000.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.45` | 14,180,000.00 USD | 14,180,000.00 USD | 68,680.00 USD | 11,560.00 USD | 8,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 5,480,000.00 USD | 5,480,000.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 5,490,000.00 USD | 5,490,000.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.47` | 14,240,000.00 USD | 14,240,000.00 USD | 44,170.00 USD | 5,760.00 USD | 12,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 5,510,000.00 USD | 5,510,000.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.49` | 14,280,000.00 USD | 14,280,000.00 USD | 25,360.00 USD | 4,900.00 USD | 6,210.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.51` | 3,580.00 USD | 565,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.51` | 14,370,000.00 USD | 14,370,000.00 USD | 57,130.00 USD | 7,150.00 USD | 25,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.53` | 14,430,000.00 USD | 14,430,000.00 USD | 50,200.00 USD | 9,410.00 USD | 1,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.55` | 14,450,000.00 USD | 14,450,000.00 USD | 11,560.00 USD | 11,570.00 USD | 880.26 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.57` | 14,510,000.00 USD | 14,510,000.00 USD | 31,530.00 USD | 2,130.00 USD | 24,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.59` | 14,550,000.00 USD | 14,550,000.00 USD | 14,070.00 USD | 7,840.00 USD | 14,300.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.61` | 14,600,000.00 USD | 14,600,000.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 565,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 567,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.68` | 319.28 USD | 567,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 285.51 USD | 567,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 567,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 568,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.10` | 119.83 USD | 568,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 571,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 571,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 572,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 117,020.00 USD | 689,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.11` | 55,520.00 USD | 745,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 11,670.00 USD | 756,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.30` | 960.92 USD | 757,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.44` | 1,620.00 USD | 759,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.61` | 326.68 USD | 759,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,410.00 USD | 772,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.46` | 63,360.00 USD | 1,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.90` | 75,090.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.02` | 4,170.00 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.04` | 246.89 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.24` | 875.67 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.39` | 20,010.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.72` | 234.30 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.36` | 265,080.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.43` | 1,900.00 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.50` | 117.28 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 23,530.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.98` | 1,690.00 USD | 1,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.00` | 1,940.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.02` | 191.87 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 207.78 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.05` | 575.27 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.07` | 6,740.00 USD | 1,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.14` | 1,270.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `17.20` | 263.60 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.98` | 2,290,000.00 USD | 0.00 USD | 1,510.00 USD | `-77.04%` | `762.30` |
| `Live` | `Long` | `2.00` | 2,290,000.00 USD | 0.00 USD | 160.40 USD | `-76.69%` | `80.00` |
| `Live` | `Long` | `2.02` | 2,290,000.00 USD | 0.00 USD | 223.28 USD | `-76.57%` | `110.81` |
| `Live` | `Long` | `2.04` | 2,290,000.00 USD | 0.00 USD | 110.52 USD | `-76.34%` | `54.31` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.99%` | `2,382.76` |
| `Live` | `Long` | `2.12` | 2,280,000.00 USD | 0.00 USD | 565.80 USD | `-75.29%` | `266.26` |
| `Live` | `Long` | `2.19` | 2,280,000.00 USD | 0.00 USD | 252.43 USD | `-74.48%` | `115.00` |
| `Live` | `Long` | `2.23` | 2,280,000.00 USD | 0.00 USD | 257.03 USD | `-74.02%` | `115.00` |
| `Live` | `Long` | `2.33` | 2,280,000.00 USD | 0.00 USD | 267.38 USD | `-72.97%` | `115.00` |
| `Live` | `Long` | `2.69` | 2,280,000.00 USD | 0.00 USD | 942.44 USD | `-68.78%` | `351.00` |
| `Live` | `Long` | `2.73` | 2,280,000.00 USD | 0.00 USD | 10,990.00 USD | `-68.32%` | `4,033.48` |
| `Live` | `Long` | `2.87` | 2,270,000.00 USD | 0.00 USD | 232.67 USD | `-66.69%` | `81.21` |
| `Live` | `Long` | `2.90` | 2,270,000.00 USD | 0.00 USD | 332.93 USD | `-66.34%` | `115.00` |
| `Live` | `Long` | `2.94` | 2,270,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.88%` | `15,165.76` |
| `Live` | `Long` | `2.98` | 2,220,000.00 USD | 0.00 USD | 111.12 USD | `-65.41%` | `37.35` |
| `Live` | `Long` | `3.06` | 2,220,000.00 USD | 0.00 USD | 1,150.00 USD | `-64.48%` | `377.71` |
| `Live` | `Long` | `3.06` | 2,220,000.00 USD | 0.00 USD | 21,430.00 USD | `-64.37%` | `6,990.57` |
| `Live` | `Long` | `3.15` | 2,200,000.00 USD | 0.00 USD | 23,480.00 USD | `-63.44%` | `7,465.11` |
| `Live` | `Long` | `3.35` | 2,180,000.00 USD | 0.00 USD | 905.85 USD | `-60.99%` | `270.00` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.88%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.76%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.79%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 8,600.00 USD | `-58.32%` | `2,400.00` |
| `Live` | `Long` | `3.62` | 2,170,000.00 USD | 0.00 USD | 590.29 USD | `-57.86%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,170,000.00 USD | 0.00 USD | 109.95 USD | `-57.39%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,170,000.00 USD | 0.00 USD | 1,500.00 USD | `-56.34%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,170,000.00 USD | 0.00 USD | 131.73 USD | `-54.72%` | `33.82` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-53.21%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,160,000.00 USD | 0.00 USD | 152.29 USD | `-52.97%` | `37.65` |
| `Live` | `Long` | `4.16` | 2,160,000.00 USD | 0.00 USD | 159.68 USD | `-51.69%` | `38.43` |
| `Live` | `Long` | `4.18` | 2,160,000.00 USD | 0.00 USD | 390.54 USD | `-51.35%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,160,000.00 USD | 0.00 USD | 169.40 USD | `-50.76%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,160,000.00 USD | 0.00 USD | 196.42 USD | `-50.65%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,160,000.00 USD | 0.00 USD | 110.77 USD | `-48.32%` | `24.92` |
| `Live` | `Long` | `4.58` | 2,160,000.00 USD | 0.00 USD | 107.56 USD | `-46.69%` | `23.46` |
| `Live` | `Long` | `4.59` | 2,160,000.00 USD | 0.00 USD | 30,970.00 USD | `-46.58%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,130,000.00 USD | 0.00 USD | 3,420.00 USD | `-46.23%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.88%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-45.76%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-45.65%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,120,000.00 USD | 0.00 USD | 8,380.00 USD | `-45.53%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-45.42%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,110,000.00 USD | 0.00 USD | 474.50 USD | `-44.83%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-44.60%` | `22.17` |
| `Live` | `Long` | `4.78` | 2,110,000.00 USD | 0.00 USD | 525.25 USD | `-44.49%` | `110.00` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 3,320.00 USD | `-43.79%` | `685.94` |
| `Live` | `Long` | `4.87` | 2,100,000.00 USD | 0.00 USD | 310.14 USD | `-43.44%` | `63.75` |
| `Live` | `Long` | `4.88` | 2,100,000.00 USD | 0.00 USD | 505.68 USD | `-43.32%` | `103.73` |
| `Live` | `Long` | `4.89` | 2,100,000.00 USD | 0.00 USD | 16,080.00 USD | `-43.09%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 4,110.00 USD | `-42.97%` | `838.83` |
| `Live` | `Long` | `4.92` | 2,080,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.86%` | `251.00` |
| `Live` | `Long` | `4.95` | 2,080,000.00 USD | 0.00 USD | 352.68 USD | `-42.51%` | `71.32` |
| `Live` | `Long` | `4.96` | 2,080,000.00 USD | 0.00 USD | 945.36 USD | `-42.39%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,080,000.00 USD | 0.00 USD | 4,090.00 USD | `-42.28%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-42.16%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.93%` | `53.96` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-41.70%` | `11,243.48` |
| `Live` | `Long` | `5.03` | 2,020,000.00 USD | 0.00 USD | 216.43 USD | `-41.58%` | `43.07` |
| `Live` | `Long` | `5.04` | 2,020,000.00 USD | 0.00 USD | 482.71 USD | `-41.46%` | `95.87` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 710.03 USD | `-41.23%` | `140.46` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 954.05 USD | `-41.00%` | `187.99` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 105.46 USD | `-40.88%` | `20.74` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 915.43 USD | `-40.53%` | `178.97` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-40.42%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-40.30%` | `77.13` |
| `Live` | `Long` | `5.14` | 2,020,000.00 USD | 0.00 USD | 3,070.00 USD | `-40.18%` | `596.05` |
| `Live` | `Long` | `5.17` | 2,010,000.00 USD | 0.00 USD | 1,620.00 USD | `-39.84%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,010,000.00 USD | 0.00 USD | 150.57 USD | `-39.72%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,010,000.00 USD | 0.00 USD | 421.89 USD | `-39.37%` | `80.90` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 159,630.00 USD | `-39.02%` | `30,435.20` |
| `Live` | `Long` | `5.26` | 1,850,000.00 USD | 0.00 USD | 2,230.00 USD | `-38.79%` | `423.54` |
| `Live` | `Long` | `5.29` | 1,850,000.00 USD | 0.00 USD | 640.70 USD | `-38.56%` | `121.23` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-38.21%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-38.09%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-37.28%` | `122.42` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,560.00 USD | `-37.05%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.93%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,670,000.00 USD | 0.00 USD | 1,360.00 USD | `-36.81%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 299.48 USD | `-36.70%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-36.46%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-36.35%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-36.23%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-36.12%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-35.53%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-35.18%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,580,000.00 USD | 0.00 USD | 34,490.00 USD | `-34.84%` | `6,153.60` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-34.49%` | `83.15` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-33.44%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,540,000.00 USD | 0.00 USD | 661.65 USD | `-33.32%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 125.70 USD | `-33.21%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 4,530.00 USD | `-33.09%` | `787.78` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.98%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-32.86%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-32.63%` | `109.63` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 688.15 USD | `-32.39%` | `118.34` |
| `Live` | `Long` | `5.84` | 1,520,000.00 USD | 0.00 USD | 146.13 USD | `-32.05%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-31.93%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,520,000.00 USD | 0.00 USD | 984.70 USD | `-31.46%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,520,000.00 USD | 0.00 USD | 399.18 USD | `-31.35%` | `67.60` |
| `Live` | `Long` | `5.95` | 1,520,000.00 USD | 0.00 USD | 147.55 USD | `-30.88%` | `24.82` |
| `Live` | `Long` | `5.96` | 1,520,000.00 USD | 0.00 USD | 11,720.00 USD | `-30.77%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 6,320.00 USD | `-30.65%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,500,000.00 USD | 0.00 USD | 585.97 USD | `-30.53%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,500,000.00 USD | 0.00 USD | 341.56 USD | `-30.19%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,500,000.00 USD | 0.00 USD | 446.85 USD | `-30.07%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,500,000.00 USD | 0.00 USD | 437.84 USD | `-29.72%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,500,000.00 USD | 0.00 USD | 1,310.00 USD | `-29.60%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,500,000.00 USD | 0.00 USD | 265.10 USD | `-29.49%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,500,000.00 USD | 0.00 USD | 1,690.00 USD | `-29.37%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,530.00 USD | `-29.14%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-28.91%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 137.02 USD | `-28.79%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,490,000.00 USD | 0.00 USD | 2,030.00 USD | `-28.67%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,490,000.00 USD | 0.00 USD | 238.61 USD | `-28.56%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,490,000.00 USD | 0.00 USD | 7,810.00 USD | `-28.44%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,480,000.00 USD | 0.00 USD | 104.36 USD | `-28.21%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,480,000.00 USD | 0.00 USD | 310.25 USD | `-27.86%` | `50.00` |
| `Live` | `Long` | `6.22` | 1,480,000.00 USD | 0.00 USD | 795.06 USD | `-27.63%` | `127.72` |
| `Live` | `Long` | `6.25` | 1,480,000.00 USD | 0.00 USD | 972.65 USD | `-27.28%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,480,000.00 USD | 0.00 USD | 354,280.00 USD | `-27.05%` | `56,459.40` |
| `Live` | `Long` | `6.29` | 1,120,000.00 USD | 0.00 USD | 1,420.00 USD | `-26.93%` | `225.14` |
| `Live` | `Long` | `6.33` | 1,120,000.00 USD | 0.00 USD | 277.48 USD | `-26.47%` | `43.87` |
| `Live` | `Long` | `6.36` | 1,120,000.00 USD | 0.00 USD | 4,470.00 USD | `-26.12%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,120,000.00 USD | 0.00 USD | 287,230.00 USD | `-26.00%` | `45,126.53` |
| `Live` | `Long` | `6.38` | 829,240.00 USD | 0.00 USD | 1,310.00 USD | `-25.88%` | `204.92` |
| `Live` | `Long` | `6.38` | 827,940.00 USD | 0.00 USD | 5,120.00 USD | `-25.77%` | `801.31` |
| `Live` | `Long` | `6.42` | 822,820.00 USD | 0.00 USD | 306.32 USD | `-25.42%` | `47.75` |
| `Live` | `Long` | `6.42` | 822,510.00 USD | 0.00 USD | 484.64 USD | `-25.30%` | `75.43` |
| `Live` | `Long` | `6.43` | 822,030.00 USD | 0.00 USD | 6,780.00 USD | `-25.19%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 815,250.00 USD | 0.00 USD | 1,050.00 USD | `-24.84%` | `162.75` |
| `Live` | `Long` | `6.49` | 814,200.00 USD | 0.00 USD | 1,480.00 USD | `-24.61%` | `228.41` |
| `Live` | `Long` | `6.50` | 812,720.00 USD | 0.00 USD | 6,030.00 USD | `-24.49%` | `928.10` |
| `Live` | `Long` | `6.54` | 806,690.00 USD | 0.00 USD | 852.03 USD | `-24.02%` | `130.38` |
| `Live` | `Long` | `6.54` | 805,840.00 USD | 0.00 USD | 8,970.00 USD | `-23.91%` | `1,370.89` |
| `Live` | `Long` | `6.55` | 796,870.00 USD | 0.00 USD | 1,510.00 USD | `-23.79%` | `231.02` |
| `Live` | `Long` | `6.59` | 795,350.00 USD | 0.00 USD | 2,870.00 USD | `-23.33%` | `435.69` |
| `Live` | `Long` | `6.62` | 792,480.00 USD | 0.00 USD | 2,110.00 USD | `-23.09%` | `318.57` |
| `Live` | `Long` | `6.62` | 790,370.00 USD | 0.00 USD | 364.90 USD | `-22.98%` | `55.08` |
| `Live` | `Long` | `6.63` | 790,010.00 USD | 0.00 USD | 245.89 USD | `-22.86%` | `37.06` |
| `Live` | `Long` | `6.66` | 789,760.00 USD | 0.00 USD | 1,740.00 USD | `-22.63%` | `261.71` |
| `Live` | `Long` | `6.67` | 788,020.00 USD | 0.00 USD | 1,320.00 USD | `-22.40%` | `198.12` |
| `Live` | `Long` | `6.68` | 786,700.00 USD | 0.00 USD | 3,160.00 USD | `-22.28%` | `472.28` |
| `Live` | `Long` | `6.70` | 783,540.00 USD | 0.00 USD | 15,800.00 USD | `-22.16%` | `2,360.46` |
| `Live` | `Long` | `6.71` | 767,740.00 USD | 0.00 USD | 11,000.00 USD | `-22.05%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 756,730.00 USD | 0.00 USD | 6,180.00 USD | `-21.93%` | `920.74` |
| `Live` | `Long` | `6.72` | 750,550.00 USD | 0.00 USD | 2,200.00 USD | `-21.82%` | `326.90` |
| `Live` | `Long` | `6.75` | 748,350.00 USD | 0.00 USD | 1,330.00 USD | `-21.47%` | `196.95` |
| `Live` | `Long` | `6.78` | 747,020.00 USD | 0.00 USD | 7,990.00 USD | `-21.23%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 739,030.00 USD | 0.00 USD | 22,020.00 USD | `-21.12%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 717,010.00 USD | 0.00 USD | 5,170.00 USD | `-21.00%` | `761.18` |
| `Live` | `Long` | `6.80` | 711,830.00 USD | 0.00 USD | 219.12 USD | `-20.88%` | `32.20` |
| `Live` | `Long` | `6.82` | 711,620.00 USD | 0.00 USD | 8,520.00 USD | `-20.77%` | `1,249.79` |
| `Live` | `Long` | `6.83` | 703,100.00 USD | 0.00 USD | 158.14 USD | `-20.65%` | `23.17` |
| `Live` | `Long` | `6.87` | 702,940.00 USD | 0.00 USD | 3,340.00 USD | `-20.19%` | `486.46` |
| `Live` | `Long` | `6.88` | 699,600.00 USD | 0.00 USD | 263.66 USD | `-20.07%` | `38.35` |
| `Live` | `Long` | `6.88` | 699,340.00 USD | 0.00 USD | 3,990.00 USD | `-19.95%` | `579.76` |
| `Live` | `Long` | `6.92` | 695,350.00 USD | 0.00 USD | 579.62 USD | `-19.49%` | `83.70` |
| `Live` | `Long` | `6.93` | 694,770.00 USD | 0.00 USD | 3,500.00 USD | `-19.37%` | `504.07` |
| `Live` | `Long` | `6.95` | 691,270.00 USD | 0.00 USD | 215.30 USD | `-19.26%` | `31.00` |
| `Live` | `Long` | `6.96` | 691,050.00 USD | 0.00 USD | 7,240.00 USD | `-19.14%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 683,810.00 USD | 0.00 USD | 636.74 USD | `-19.02%` | `91.42` |
| `Live` | `Long` | `6.97` | 683,170.00 USD | 0.00 USD | 128,810.00 USD | `-18.91%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 554,370.00 USD | 0.00 USD | 1,040.00 USD | `-18.68%` | `149.32` |
| `Live` | `Long` | `7.01` | 553,320.00 USD | 0.00 USD | 20,890.00 USD | `-18.44%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 532,430.00 USD | 0.00 USD | 1,370.00 USD | `-18.33%` | `194.51` |
| `Live` | `Long` | `7.07` | 531,060.00 USD | 0.00 USD | 23,960.00 USD | `-17.86%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 507,110.00 USD | 0.00 USD | 6,700.00 USD | `-17.75%` | `947.44` |
| `Live` | `Long` | `7.08` | 500,400.00 USD | 0.00 USD | 1,050.00 USD | `-17.63%` | `148.63` |
| `Live` | `Long` | `7.09` | 499,350.00 USD | 0.00 USD | 2,130.00 USD | `-17.51%` | `300.00` |
| `Live` | `Long` | `7.11` | 497,220.00 USD | 0.00 USD | 28,530.00 USD | `-17.40%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 468,690.00 USD | 0.00 USD | 379.66 USD | `-17.28%` | `53.36` |
| `Live` | `Long` | `7.13` | 468,310.00 USD | 0.00 USD | 13,410.00 USD | `-17.05%` | `1,879.32` |
| `Live` | `Long` | `7.14` | 454,910.00 USD | 0.00 USD | 20,270.00 USD | `-16.93%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 434,640.00 USD | 0.00 USD | 4,470.00 USD | `-16.58%` | `622.52` |
| `Live` | `Long` | `7.18` | 430,170.00 USD | 0.00 USD | 1,440.00 USD | `-16.47%` | `200.95` |
| `Live` | `Long` | `7.21` | 428,720.00 USD | 0.00 USD | 322.94 USD | `-16.12%` | `44.76` |
| `Live` | `Long` | `7.24` | 428,400.00 USD | 0.00 USD | 2,500.00 USD | `-15.89%` | `345.21` |
| `Live` | `Long` | `7.25` | 425,900.00 USD | 0.00 USD | 185.83 USD | `-15.77%` | `25.65` |
| `Live` | `Long` | `7.25` | 425,720.00 USD | 0.00 USD | 21,280.00 USD | `-15.65%` | `2,933.17` |
| `Live` | `Long` | `7.29` | 404,440.00 USD | 0.00 USD | 36,420.00 USD | `-15.30%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 368,010.00 USD | 0.00 USD | 1,680.00 USD | `-15.19%` | `230.97` |
| `Live` | `Long` | `7.30` | 366,330.00 USD | 0.00 USD | 29,220.00 USD | `-15.07%` | `4,000.00` |
| `Live` | `Long` | `7.33` | 337,110.00 USD | 0.00 USD | 13,110.00 USD | `-14.72%` | `1,787.05` |
| `Live` | `Long` | `7.34` | 324,000.00 USD | 0.00 USD | 1,400.00 USD | `-14.61%` | `190.54` |
| `Live` | `Long` | `7.36` | 322,600.00 USD | 0.00 USD | 5,290.00 USD | `-14.49%` | `719.63` |
| `Live` | `Long` | `7.37` | 317,310.00 USD | 0.00 USD | 2,940.00 USD | `-14.37%` | `399.15` |
| `Live` | `Long` | `7.38` | 314,370.00 USD | 0.00 USD | 1,100.00 USD | `-14.26%` | `148.75` |
| `Live` | `Long` | `7.38` | 313,270.00 USD | 0.00 USD | 227.97 USD | `-14.14%` | `30.87` |
| `Live` | `Long` | `7.42` | 313,040.00 USD | 0.00 USD | 147.61 USD | `-13.68%` | `19.88` |
| `Live` | `Long` | `7.43` | 312,900.00 USD | 0.00 USD | 2,430.00 USD | `-13.56%` | `327.05` |
| `Live` | `Long` | `7.45` | 310,460.00 USD | 0.00 USD | 2,410.00 USD | `-13.44%` | `324.35` |
| `Live` | `Long` | `7.46` | 308,050.00 USD | 0.00 USD | 10,390.00 USD | `-13.33%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 297,660.00 USD | 0.00 USD | 4,590.00 USD | `-13.21%` | `614.36` |
| `Live` | `Long` | `7.47` | 293,070.00 USD | 0.00 USD | 1,120.00 USD | `-13.10%` | `149.52` |
| `Live` | `Long` | `7.50` | 291,960.00 USD | 0.00 USD | 962.81 USD | `-12.86%` | `128.46` |
| `Live` | `Long` | `7.50` | 290,990.00 USD | 0.00 USD | 421.78 USD | `-12.75%` | `56.20` |
| `Live` | `Long` | `7.51` | 290,570.00 USD | 0.00 USD | 1,710.00 USD | `-12.63%` | `228.21` |
| `Live` | `Long` | `7.53` | 288,860.00 USD | 0.00 USD | 1,570.00 USD | `-12.51%` | `208.52` |
| `Live` | `Long` | `7.54` | 287,290.00 USD | 0.00 USD | 4,210.00 USD | `-12.40%` | `559.01` |
| `Live` | `Long` | `7.54` | 283,080.00 USD | 0.00 USD | 1,510.00 USD | `-12.28%` | `200.00` |
| `Live` | `Long` | `7.55` | 281,570.00 USD | 0.00 USD | 1,070.00 USD | `-12.17%` | `141.09` |
| `Live` | `Long` | `7.57` | 280,500.00 USD | 0.00 USD | 25,060.00 USD | `-12.05%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 255,440.00 USD | 0.00 USD | 118.25 USD | `-11.93%` | `15.61` |
| `Live` | `Long` | `7.62` | 255,330.00 USD | 0.00 USD | 754.04 USD | `-11.47%` | `99.02` |
| `Live` | `Long` | `7.62` | 254,570.00 USD | 0.00 USD | 787.51 USD | `-11.35%` | `103.28` |
| `Live` | `Long` | `7.63` | 253,780.00 USD | 0.00 USD | 378.93 USD | `-11.24%` | `49.63` |
| `Live` | `Long` | `7.66` | 253,400.00 USD | 0.00 USD | 135.42 USD | `-11.00%` | `17.69` |
| `Live` | `Long` | `7.67` | 253,270.00 USD | 0.00 USD | 256.09 USD | `-10.89%` | `33.41` |
| `Live` | `Long` | `7.67` | 253,010.00 USD | 0.00 USD | 140.45 USD | `-10.77%` | `18.30` |
| `Live` | `Long` | `7.68` | 252,870.00 USD | 0.00 USD | 739.30 USD | `-10.65%` | `96.20` |
| `Live` | `Long` | `7.70` | 252,130.00 USD | 0.00 USD | 6,690.00 USD | `-10.54%` | `869.22` |
| `Live` | `Long` | `7.75` | 245,440.00 USD | 0.00 USD | 500.12 USD | `-9.84%` | `64.49` |
| `Live` | `Long` | `7.76` | 244,940.00 USD | 0.00 USD | 455.73 USD | `-9.72%` | `58.69` |
| `Live` | `Long` | `7.78` | 244,490.00 USD | 0.00 USD | 12,100.00 USD | `-9.61%` | `1,555.99` |
| `Live` | `Long` | `7.79` | 232,390.00 USD | 0.00 USD | 3,750.00 USD | `-9.49%` | `481.06` |
| `Live` | `Long` | `7.79` | 228,650.00 USD | 0.00 USD | 4,480.00 USD | `-9.38%` | `574.50` |
| `Live` | `Long` | `7.80` | 224,170.00 USD | 0.00 USD | 6,380.00 USD | `-9.26%` | `817.06` |
| `Live` | `Long` | `7.83` | 217,790.00 USD | 0.00 USD | 1,940.00 USD | `-9.03%` | `247.42` |
| `Live` | `Long` | `7.84` | 215,850.00 USD | 0.00 USD | 22,560.00 USD | `-8.79%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 193,290.00 USD | 0.00 USD | 233.83 USD | `-8.56%` | `29.73` |
| `Live` | `Long` | `7.88` | 193,060.00 USD | 0.00 USD | 555.19 USD | `-8.45%` | `70.50` |
| `Live` | `Long` | `7.89` | 192,500.00 USD | 0.00 USD | 13,270.00 USD | `-8.21%` | `1,680.67` |
| `Live` | `Long` | `7.91` | 179,240.00 USD | 0.00 USD | 2,930.00 USD | `-8.10%` | `370.74` |
| `Live` | `Long` | `7.92` | 176,310.00 USD | 0.00 USD | 4,600.00 USD | `-7.86%` | `580.78` |
| `Live` | `Long` | `7.93` | 171,700.00 USD | 0.00 USD | 16,340.00 USD | `-7.75%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 155,360.00 USD | 0.00 USD | 141.74 USD | `-7.63%` | `17.84` |
| `Live` | `Long` | `7.96` | 155,220.00 USD | 0.00 USD | 127,900.00 USD | `-7.52%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 27,320.00 USD | 0.00 USD | 1,580.00 USD | `-7.28%` | `198.26` |
| `Live` | `Long` | `7.99` | 25,730.00 USD | 0.00 USD | 1,280.00 USD | `-7.17%` | `160.68` |
| `Live` | `Long` | `8.00` | 24,450.00 USD | 0.00 USD | 889.52 USD | `-7.05%` | `111.26` |
| `Live` | `Long` | `8.06` | 23,560.00 USD | 0.00 USD | 439.54 USD | `-6.24%` | `54.50` |
| `Live` | `Long` | `8.07` | 23,120.00 USD | 0.00 USD | 21,710.00 USD | `-6.12%` | `2,688.93` |
| `Live` | `Long` | `8.09` | 1,410.00 USD | 0.00 USD | 887.25 USD | `-6.00%` | `109.74` |
| `Live` | `Long` | `8.12` | 521.62 USD | 0.00 USD | 521.62 USD | `-5.54%` | `64.20` |
| `Live` | `Short` | `8.69` | 209.31 USD | 209.31 USD | 0.00 USD | `+0.97%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,210.00 USD | 6,000.00 USD | 0.00 USD | `+2.60%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,370.00 USD | 1,160.00 USD | 0.00 USD | `+3.06%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,060.00 USD | 691.70 USD | 0.00 USD | `+3.30%` | `77.85` |
| `Live` | `Short` | `8.95` | 11,200.00 USD | 3,140.00 USD | 0.00 USD | `+3.99%` | `350.65` |
| `Live` | `Short` | `8.96` | 11,430.00 USD | 227.82 USD | 0.00 USD | `+4.11%` | `25.44` |
| `Live` | `Short` | `8.99` | 551,130.00 USD | 539,710.00 USD | 0.00 USD | `+4.58%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 551,350.00 USD | 213.70 USD | 0.00 USD | `+5.27%` | `23.60` |
| `Live` | `Short` | `9.10` | 555,240.00 USD | 3,890.00 USD | 0.00 USD | `+5.74%` | `427.53` |
| `Live` | `Short` | `9.14` | 555,420.00 USD | 180.80 USD | 0.00 USD | `+6.32%` | `19.77` |
| `Live` | `Short` | `9.22` | 555,830.00 USD | 416.69 USD | 0.00 USD | `+7.25%` | `45.17` |
| `Live` | `Short` | `9.29` | 556,160.00 USD | 326.09 USD | 0.00 USD | `+7.95%` | `35.12` |
| `Live` | `Short` | `9.29` | 560,020.00 USD | 3,860.00 USD | 0.00 USD | `+8.06%` | `415.00` |
| `Live` | `Short` | `9.41` | 561,460.00 USD | 1,450.00 USD | 0.00 USD | `+9.46%` | `153.50` |
| `Live` | `Short` | `9.51` | 565,040.00 USD | 3,580.00 USD | 0.00 USD | `+10.51%` | `376.48` |
| `Live` | `Short` | `9.62` | 565,180.00 USD | 138.98 USD | 0.00 USD | `+11.90%` | `14.44` |
| `Live` | `Short` | `9.64` | 567,110.00 USD | 1,930.00 USD | 0.00 USD | `+12.13%` | `200.61` |
| `Live` | `Short` | `9.68` | 567,430.00 USD | 319.28 USD | 0.00 USD | `+12.48%` | `33.00` |
| `Live` | `Short` | `9.69` | 567,720.00 USD | 285.51 USD | 0.00 USD | `+12.60%` | `29.48` |
| `Live` | `Short` | `9.73` | 567,910.00 USD | 192.95 USD | 0.00 USD | `+13.18%` | `19.82` |
| `Live` | `Short` | `9.88` | 568,280.00 USD | 371.77 USD | 0.00 USD | `+14.92%` | `37.61` |
| `Live` | `Short` | `10.10` | 568,400.00 USD | 119.83 USD | 0.00 USD | `+17.36%` | `11.87` |
| `Live` | `Short` | `10.35` | 571,060.00 USD | 2,650.00 USD | 0.00 USD | `+20.27%` | `256.58` |
| `Live` | `Short` | `10.56` | 571,580.00 USD | 523.81 USD | 0.00 USD | `+22.83%` | `49.58` |
| `Live` | `Short` | `10.81` | 572,730.00 USD | 1,150.00 USD | 0.00 USD | `+25.74%` | `106.17` |
| `Live` | `Short` | `11.01` | 689,750.00 USD | 117,020.00 USD | 0.00 USD | `+27.94%` | `10,633.00` |
| `Live` | `Short` | `11.11` | 745,270.00 USD | 55,520.00 USD | 0.00 USD | `+29.11%` | `5,000.00` |
| `Live` | `Short` | `11.27` | 756,940.00 USD | 11,670.00 USD | 0.00 USD | `+30.97%` | `1,035.87` |
| `Live` | `Short` | `11.30` | 757,900.00 USD | 960.92 USD | 0.00 USD | `+31.43%` | `85.00` |
| `Live` | `Short` | `11.44` | 759,520.00 USD | 1,620.00 USD | 0.00 USD | `+32.94%` | `141.51` |
| `Live` | `Short` | `11.61` | 759,850.00 USD | 326.68 USD | 0.00 USD | `+34.92%` | `28.15` |
| `Live` | `Short` | `11.62` | 772,260.00 USD | 12,410.00 USD | 0.00 USD | `+35.15%` | `1,067.86` |
| `Live` | `Short` | `11.69` | 1,070,000.00 USD | 296,760.00 USD | 0.00 USD | `+35.85%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,070,000.00 USD | 505.74 USD | 0.00 USD | `+38.64%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,070,000.00 USD | 1,050.00 USD | 0.00 USD | `+38.87%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,070,000.00 USD | 1,730.00 USD | 0.00 USD | `+43.06%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,070,000.00 USD | 343.62 USD | 0.00 USD | `+44.22%` | `27.70` |
| `Live` | `Short` | `12.46` | 1,140,000.00 USD | 63,360.00 USD | 0.00 USD | `+44.80%` | `5,087.03` |
| `Live` | `Short` | `13.20` | 1,220,000.00 USD | 87,940.00 USD | 0.00 USD | `+53.41%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,230,000.00 USD | 3,810.00 USD | 0.00 USD | `+54.57%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,230,000.00 USD | 430.34 USD | 0.00 USD | `+56.54%` | `31.96` |
| `Live` | `Short` | `13.69` | 1,230,000.00 USD | 172.29 USD | 0.00 USD | `+59.10%` | `12.59` |
| `Live` | `Short` | `14.66` | 1,230,000.00 USD | 823.29 USD | 0.00 USD | `+70.50%` | `56.14` |
| `Live` | `Short` | `14.90` | 1,300,000.00 USD | 75,090.00 USD | 0.00 USD | `+73.29%` | `5,037.66` |
| `Live` | `Short` | `15.02` | 1,310,000.00 USD | 4,170.00 USD | 0.00 USD | `+74.56%` | `277.54` |
| `Live` | `Short` | `15.04` | 1,310,000.00 USD | 246.89 USD | 0.00 USD | `+74.91%` | `16.41` |
| `Live` | `Short` | `15.09` | 1,310,000.00 USD | 219.34 USD | 0.00 USD | `+75.38%` | `14.54` |
| `Live` | `Short` | `15.24` | 1,310,000.00 USD | 875.67 USD | 0.00 USD | `+77.24%` | `57.44` |
| `Live` | `Short` | `15.29` | 1,310,000.00 USD | 229.43 USD | 0.00 USD | `+77.82%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,310,000.00 USD | 230.17 USD | 0.00 USD | `+78.40%` | `15.00` |
| `Live` | `Short` | `15.39` | 1,330,000.00 USD | 20,010.00 USD | 0.00 USD | `+78.98%` | `1,300.00` |
| `Live` | `Short` | `15.72` | 1,330,000.00 USD | 234.30 USD | 0.00 USD | `+82.82%` | `14.90` |
| `Live` | `Short` | `15.77` | 1,330,000.00 USD | 185.55 USD | 0.00 USD | `+83.28%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,330,000.00 USD | 1,700.00 USD | 0.00 USD | `+83.98%` | `107.48` |
| `Live` | `Short` | `16.36` | 1,600,000.00 USD | 265,080.00 USD | 0.00 USD | `+90.14%` | `16,208.00` |
| `Live` | `Short` | `16.43` | 1,600,000.00 USD | 1,900.00 USD | 0.00 USD | `+91.07%` | `115.73` |
| `Live` | `Short` | `16.50` | 1,600,000.00 USD | 117.28 USD | 0.00 USD | `+91.77%` | `7.11` |
| `Live` | `Short` | `16.52` | 1,600,000.00 USD | 190.91 USD | 0.00 USD | `+92.00%` | `11.56` |
| `Live` | `Short` | `16.64` | 1,620,000.00 USD | 23,530.00 USD | 0.00 USD | `+93.40%` | `1,414.55` |
| `Live` | `Short` | `16.98` | 1,620,000.00 USD | 1,690.00 USD | 0.00 USD | `+97.47%` | `99.50` |
| `Live` | `Short` | `17.00` | 1,630,000.00 USD | 1,940.00 USD | 0.00 USD | `+97.70%` | `113.93` |
| `Live` | `Short` | `17.02` | 1,630,000.00 USD | 191.87 USD | 0.00 USD | `+97.93%` | `11.27` |
| `Live` | `Short` | `17.05` | 1,630,000.00 USD | 207.78 USD | 0.00 USD | `+98.17%` | `12.19` |
| `Live` | `Short` | `17.05` | 1,630,000.00 USD | 575.27 USD | 0.00 USD | `+98.28%` | `33.73` |
| `Live` | `Short` | `17.07` | 1,630,000.00 USD | 6,740.00 USD | 0.00 USD | `+98.51%` | `395.02` |
| `Live` | `Short` | `17.14` | 1,640,000.00 USD | 1,270.00 USD | 0.00 USD | `+99.21%` | `74.09` |
| `Live` | `Short` | `17.20` | 1,640,000.00 USD | 263.60 USD | 0.00 USD | `+99.91%` | `15.33` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 404,570.00 USD | 0.00 USD | 611.73 USD | `-72.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 403,960.00 USD | 0.00 USD | 793.75 USD | `-53.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 403,170.00 USD | 0.00 USD | 67,970.00 USD | `-41.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 335,200.00 USD | 0.00 USD | 205.30 USD | `-38.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 335,000.00 USD | 0.00 USD | 465.42 USD | `-36.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 334,530.00 USD | 0.00 USD | 349.35 USD | `-36.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 334,180.00 USD | 0.00 USD | 1,020.00 USD | `-35.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 333,160.00 USD | 0.00 USD | 1,330.00 USD | `-32.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 331,840.00 USD | 0.00 USD | 493.50 USD | `-31.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 331,340.00 USD | 0.00 USD | 100.98 USD | `-30.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 331,240.00 USD | 0.00 USD | 500.70 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 330,740.00 USD | 0.00 USD | 4,160.00 USD | `-29.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 326,590.00 USD | 0.00 USD | 6,500.00 USD | `-28.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 320,080.00 USD | 0.00 USD | 906.18 USD | `-27.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 319,180.00 USD | 0.00 USD | 127.35 USD | `-27.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 319,050.00 USD | 0.00 USD | 864.38 USD | `-26.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 318,190.00 USD | 0.00 USD | 130.10 USD | `-24.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 318,060.00 USD | 0.00 USD | 4,340.00 USD | `-24.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 313,720.00 USD | 0.00 USD | 5,520.00 USD | `-22.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 308,190.00 USD | 0.00 USD | 203.67 USD | `-21.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 307,990.00 USD | 0.00 USD | 296.34 USD | `-21.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 307,690.00 USD | 0.00 USD | 921.19 USD | `-21.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 306,770.00 USD | 0.00 USD | 709.98 USD | `-19.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 306,060.00 USD | 0.00 USD | 4,630.00 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 301,440.00 USD | 0.00 USD | 691.50 USD | `-19.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 300,740.00 USD | 0.00 USD | 262.44 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 300,480.00 USD | 0.00 USD | 24,350.00 USD | `-18.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 276,130.00 USD | 0.00 USD | 653.69 USD | `-18.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 275,480.00 USD | 0.00 USD | 187.79 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 275,290.00 USD | 0.00 USD | 6,790.00 USD | `-16.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 268,500.00 USD | 0.00 USD | 4,960.00 USD | `-16.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 263,540.00 USD | 0.00 USD | 7,210.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 256,330.00 USD | 0.00 USD | 282.74 USD | `-15.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 256,050.00 USD | 0.00 USD | 603.44 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 255,450.00 USD | 0.00 USD | 464.61 USD | `-15.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 254,980.00 USD | 0.00 USD | 2,090.00 USD | `-15.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 252,890.00 USD | 0.00 USD | 129.58 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 252,760.00 USD | 0.00 USD | 114.65 USD | `-14.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 252,640.00 USD | 0.00 USD | 702.75 USD | `-14.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 251,940.00 USD | 0.00 USD | 4,630.00 USD | `-13.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 247,310.00 USD | 0.00 USD | 199.39 USD | `-13.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 247,110.00 USD | 0.00 USD | 6,270.00 USD | `-13.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 240,840.00 USD | 0.00 USD | 37,420.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 203,420.00 USD | 0.00 USD | 2,120.00 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 201,300.00 USD | 0.00 USD | 799.83 USD | `-12.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 200,500.00 USD | 0.00 USD | 820.44 USD | `-12.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 199,680.00 USD | 0.00 USD | 218.24 USD | `-11.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 199,460.00 USD | 0.00 USD | 113.78 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 199,340.00 USD | 0.00 USD | 152.10 USD | `-11.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 199,190.00 USD | 0.00 USD | 297.59 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 198,900.00 USD | 0.00 USD | 528.88 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 198,370.00 USD | 0.00 USD | 360.13 USD | `-10.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 198,010.00 USD | 0.00 USD | 578.04 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 197,430.00 USD | 0.00 USD | 106.32 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 197,320.00 USD | 0.00 USD | 424.05 USD | `-9.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 196,900.00 USD | 0.00 USD | 1,170.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 195,730.00 USD | 0.00 USD | 3,940.00 USD | `-9.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 191,790.00 USD | 0.00 USD | 154.70 USD | `-9.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 191,630.00 USD | 0.00 USD | 115.23 USD | `-8.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 191,520.00 USD | 0.00 USD | 183.33 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 191,330.00 USD | 0.00 USD | 1,890.00 USD | `-8.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 189,440.00 USD | 0.00 USD | 8,250.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 181,190.00 USD | 0.00 USD | 5,710.00 USD | `-7.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 175,480.00 USD | 0.00 USD | 1,590.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 173,900.00 USD | 0.00 USD | 898.42 USD | `-7.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 173,000.00 USD | 0.00 USD | 7,960.00 USD | `-7.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 165,040.00 USD | 0.00 USD | 246.52 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 164,800.00 USD | 0.00 USD | 2,420.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 162,370.00 USD | 0.00 USD | 1,440.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 160,940.00 USD | 0.00 USD | 435.73 USD | `-7.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 160,500.00 USD | 0.00 USD | 4,320.00 USD | `-6.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 156,180.00 USD | 0.00 USD | 123.58 USD | `-6.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 156,060.00 USD | 0.00 USD | 796.62 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 155,260.00 USD | 0.00 USD | 152.56 USD | `-6.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 155,110.00 USD | 0.00 USD | 2,730.00 USD | `-6.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 152,380.00 USD | 0.00 USD | 121.69 USD | `-6.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 152,260.00 USD | 0.00 USD | 5,230.00 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 147,030.00 USD | 0.00 USD | 477.36 USD | `-5.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 146,550.00 USD | 0.00 USD | 16,210.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 130,340.00 USD | 0.00 USD | 744.88 USD | `-5.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 129,590.00 USD | 0.00 USD | 6,500.00 USD | `-5.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 123,090.00 USD | 0.00 USD | 884.60 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 122,210.00 USD | 0.00 USD | 5,550.00 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 116,660.00 USD | 0.00 USD | 121.51 USD | `-5.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 116,530.00 USD | 0.00 USD | 3,080.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 113,450.00 USD | 0.00 USD | 520.75 USD | `-4.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 112,930.00 USD | 0.00 USD | 3,020.00 USD | `-4.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 109,910.00 USD | 0.00 USD | 141.04 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 109,770.00 USD | 0.00 USD | 22,560.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 87,200.00 USD | 0.00 USD | 515.66 USD | `-4.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 86,690.00 USD | 0.00 USD | 3,020.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 83,660.00 USD | 0.00 USD | 490.15 USD | `-4.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 83,170.00 USD | 0.00 USD | 197.96 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 82,980.00 USD | 0.00 USD | 9,640.00 USD | `-4.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 73,340.00 USD | 0.00 USD | 535.65 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 72,800.00 USD | 0.00 USD | 734.99 USD | `-3.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 72,070.00 USD | 0.00 USD | 828.50 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 71,240.00 USD | 0.00 USD | 311.97 USD | `-3.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 70,930.00 USD | 0.00 USD | 5,380.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 65,550.00 USD | 0.00 USD | 245.13 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 65,310.00 USD | 0.00 USD | 1,690.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 63,610.00 USD | 0.00 USD | 5,400.00 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 58,220.00 USD | 0.00 USD | 808.63 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 57,410.00 USD | 0.00 USD | 4,070.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 53,340.00 USD | 0.00 USD | 24,090.00 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 29,250.00 USD | 0.00 USD | 1,140.00 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 28,110.00 USD | 0.00 USD | 419.25 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 27,690.00 USD | 0.00 USD | 376.68 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 27,310.00 USD | 0.00 USD | 6,230.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 21,080.00 USD | 0.00 USD | 314.81 USD | `-2.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 20,770.00 USD | 0.00 USD | 198.83 USD | `-2.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 20,570.00 USD | 0.00 USD | 195.52 USD | `-1.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 20,370.00 USD | 0.00 USD | 138.24 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 20,230.00 USD | 0.00 USD | 710.81 USD | `-1.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 19,520.00 USD | 0.00 USD | 769.61 USD | `-1.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.48` | 18,750.00 USD | 0.00 USD | 777.14 USD | `-1.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.49` | 17,970.00 USD | 0.00 USD | 408.78 USD | `-1.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.51` | 17,570.00 USD | 0.00 USD | 122.47 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.52` | 17,440.00 USD | 0.00 USD | 1,720.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.53` | 15,720.00 USD | 0.00 USD | 123.27 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 15,600.00 USD | 0.00 USD | 2,170.00 USD | `-0.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.54` | 13,430.00 USD | 0.00 USD | 123.56 USD | `-0.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.55` | 13,310.00 USD | 0.00 USD | 9,990.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.56` | 3,320.00 USD | 0.00 USD | 2,490.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.57` | 834.12 USD | 0.00 USD | 566.55 USD | `-0.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.59` | 267.57 USD | 0.00 USD | 143.28 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.60` | 124.28 USD | 0.00 USD | 124.28 USD | `-0.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 102.14 USD | 102.14 USD | 0.00 USD | `+0.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 226.71 USD | 124.57 USD | 0.00 USD | `+0.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 355.23 USD | 128.51 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 1,090.00 USD | 733.98 USD | 0.00 USD | `+0.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 3,380.00 USD | 2,290.00 USD | 0.00 USD | `+0.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 3,840.00 USD | 459.41 USD | 0.00 USD | `+0.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 4,040.00 USD | 200.85 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 4,210.00 USD | 176.62 USD | 0.00 USD | `+0.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 7,260.00 USD | 3,050.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 7,670.00 USD | 410.49 USD | 0.00 USD | `+1.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 9,210.00 USD | 1,540.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 9,610.00 USD | 399.67 USD | 0.00 USD | `+1.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 10,040.00 USD | 421.85 USD | 0.00 USD | `+1.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 10,280.00 USD | 239.51 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 14,650.00 USD | 4,370.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 18,390.00 USD | 3,740.00 USD | 0.00 USD | `+1.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 18,560.00 USD | 173.28 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 18,780.00 USD | 215.16 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 19,170.00 USD | 388.12 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 19,880.00 USD | 711.78 USD | 0.00 USD | `+2.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 20,440.00 USD | 563.87 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 20,690.00 USD | 243.40 USD | 0.00 USD | `+2.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 20,850.00 USD | 168.05 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 21,190.00 USD | 339.94 USD | 0.00 USD | `+2.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 21,510.00 USD | 310.98 USD | 0.00 USD | `+3.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 21,620.00 USD | 110.58 USD | 0.00 USD | `+3.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 22,480.00 USD | 860.96 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 24,410.00 USD | 1,930.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 25,200.00 USD | 788.72 USD | 0.00 USD | `+3.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 27,000.00 USD | 1,800.00 USD | 0.00 USD | `+3.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 27,170.00 USD | 163.33 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 27,950.00 USD | 782.17 USD | 0.00 USD | `+3.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 28,170.00 USD | 223.62 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 565,480.00 USD | 537,310.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 565,880.00 USD | 401.63 USD | 0.00 USD | `+4.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 881,030.00 USD | 315,150.00 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.98` | 881,220.00 USD | 186.53 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 881,560.00 USD | 338.30 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 881,820.00 USD | 260.96 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 882,040.00 USD | 220.06 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 883,130.00 USD | 1,090.00 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 883,740.00 USD | 616.37 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 883,850.00 USD | 102.03 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 884,300.00 USD | 453.84 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 884,460.00 USD | 160.99 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 884,680.00 USD | 215.98 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 886,190.00 USD | 1,510.00 USD | 0.00 USD | `+5.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 886,640.00 USD | 451.48 USD | 0.00 USD | `+5.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 886,780.00 USD | 139.58 USD | 0.00 USD | `+5.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 888,070.00 USD | 1,290.00 USD | 0.00 USD | `+5.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 888,230.00 USD | 166.53 USD | 0.00 USD | `+6.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 890,230.00 USD | 2,000.00 USD | 0.00 USD | `+6.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,280,000.00 USD | 394,210.00 USD | 0.00 USD | `+6.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,280,000.00 USD | 119.24 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,290,000.00 USD | 3,020.00 USD | 0.00 USD | `+7.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,290,000.00 USD | 131.87 USD | 0.00 USD | `+7.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,290,000.00 USD | 149.17 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,290,000.00 USD | 2,220.00 USD | 0.00 USD | `+7.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,520,000.00 USD | 231,380.00 USD | 0.00 USD | `+7.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,520,000.00 USD | 1,960.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,520,000.00 USD | 434.45 USD | 0.00 USD | `+8.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,540,000.00 USD | 18,610.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,540,000.00 USD | 166.83 USD | 0.00 USD | `+8.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,540,000.00 USD | 674.29 USD | 0.00 USD | `+8.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,540,000.00 USD | 101.58 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,540,000.00 USD | 109.36 USD | 0.00 USD | `+8.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,540,000.00 USD | 116.69 USD | 0.00 USD | `+8.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,540,000.00 USD | 163.41 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,540,000.00 USD | 102.01 USD | 0.00 USD | `+9.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,540,000.00 USD | 102.12 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,540,000.00 USD | 714.59 USD | 0.00 USD | `+9.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,550,000.00 USD | 928.13 USD | 0.00 USD | `+9.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,550,000.00 USD | 102.45 USD | 0.00 USD | `+9.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,550,000.00 USD | 219.84 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,550,000.00 USD | 311.69 USD | 0.00 USD | `+9.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,550,000.00 USD | 1,890.00 USD | 0.00 USD | `+9.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,550,000.00 USD | 1,130.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,550,000.00 USD | 288.46 USD | 0.00 USD | `+10.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,550,000.00 USD | 119.92 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,550,000.00 USD | 231.00 USD | 0.00 USD | `+11.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,550,000.00 USD | 221.07 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,550,000.00 USD | 992.00 USD | 0.00 USD | `+11.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,550,000.00 USD | 148.48 USD | 0.00 USD | `+12.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,550,000.00 USD | 191.36 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,560,000.00 USD | 4,440.00 USD | 0.00 USD | `+12.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,560,000.00 USD | 108.21 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,560,000.00 USD | 169.68 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,560,000.00 USD | 574.66 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,560,000.00 USD | 121.87 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,560,000.00 USD | 115.88 USD | 0.00 USD | `+14.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,560,000.00 USD | 340.05 USD | 0.00 USD | `+14.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,560,000.00 USD | 742.12 USD | 0.00 USD | `+15.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,560,000.00 USD | 899.47 USD | 0.00 USD | `+15.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,630,000.00 USD | 70,020.00 USD | 0.00 USD | `+15.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,630,000.00 USD | 373.97 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,640,000.00 USD | 6,320.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,640,000.00 USD | 6,370.00 USD | 0.00 USD | `+17.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,640,000.00 USD | 404.20 USD | 0.00 USD | `+17.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,850,000.00 USD | 210,980.00 USD | 0.00 USD | `+17.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,850,000.00 USD | 1,150.00 USD | 0.00 USD | `+17.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,850,000.00 USD | 172.16 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,860,000.00 USD | 922.87 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,860,000.00 USD | 489.40 USD | 0.00 USD | `+20.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,860,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,860,000.00 USD | 118.01 USD | 0.00 USD | `+21.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,860,000.00 USD | 971.48 USD | 0.00 USD | `+21.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,860,000.00 USD | 818.31 USD | 0.00 USD | `+21.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,860,000.00 USD | 312.31 USD | 0.00 USD | `+22.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,860,000.00 USD | 2,290.00 USD | 0.00 USD | `+22.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,860,000.00 USD | 1,890.00 USD | 0.00 USD | `+22.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,860,000.00 USD | 178.46 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,860,000.00 USD | 173.42 USD | 0.00 USD | `+24.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,860,000.00 USD | 184.75 USD | 0.00 USD | `+24.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,860,000.00 USD | 135.78 USD | 0.00 USD | `+25.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,860,000.00 USD | 127.96 USD | 0.00 USD | `+25.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,870,000.00 USD | 476.43 USD | 0.00 USD | `+26.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,870,000.00 USD | 1,080.00 USD | 0.00 USD | `+26.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,900,000.00 USD | 35,110.00 USD | 0.00 USD | `+26.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,900,000.00 USD | 251.06 USD | 0.00 USD | `+27.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,900,000.00 USD | 552.44 USD | 0.00 USD | `+27.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,900,000.00 USD | 537.26 USD | 0.00 USD | `+27.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,900,000.00 USD | 1,110.00 USD | 0.00 USD | `+29.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,900,000.00 USD | 320.29 USD | 0.00 USD | `+29.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,910,000.00 USD | 1,100.00 USD | 0.00 USD | `+29.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,910,000.00 USD | 2,270.00 USD | 0.00 USD | `+30.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,910,000.00 USD | 1,270.00 USD | 0.00 USD | `+30.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,910,000.00 USD | 1,380.00 USD | 0.00 USD | `+32.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,910,000.00 USD | 2,410.00 USD | 0.00 USD | `+32.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,920,000.00 USD | 10,640.00 USD | 0.00 USD | `+33.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,930,000.00 USD | 2,050.00 USD | 0.00 USD | `+33.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,930,000.00 USD | 746.79 USD | 0.00 USD | `+33.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,930,000.00 USD | 7,700.00 USD | 0.00 USD | `+34.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,930,000.00 USD | 906.03 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,930,000.00 USD | 434.61 USD | 0.00 USD | `+37.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,940,000.00 USD | 163.52 USD | 0.00 USD | `+38.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 1,950,000.00 USD | 10,370.00 USD | 0.00 USD | `+39.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 1,950,000.00 USD | 5,270.00 USD | 0.00 USD | `+41.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 1,950,000.00 USD | 115.02 USD | 0.00 USD | `+42.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 1,950,000.00 USD | 3,870.00 USD | 0.00 USD | `+47.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 1,950,000.00 USD | 197.97 USD | 0.00 USD | `+48.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 1,960,000.00 USD | 3,200.00 USD | 0.00 USD | `+50.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 1,960,000.00 USD | 179.58 USD | 0.00 USD | `+50.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 1,960,000.00 USD | 568.45 USD | 0.00 USD | `+51.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 1,960,000.00 USD | 169.57 USD | 0.00 USD | `+52.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 1,960,000.00 USD | 446.52 USD | 0.00 USD | `+55.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 1,960,000.00 USD | 5,320.00 USD | 0.00 USD | `+56.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,180,000.00 USD | 210,750.00 USD | 0.00 USD | `+57.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,180,000.00 USD | 407.95 USD | 0.00 USD | `+59.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,180,000.00 USD | 174.91 USD | 0.00 USD | `+60.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,180,000.00 USD | 5,070.00 USD | 0.00 USD | `+62.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,180,000.00 USD | 960.26 USD | 0.00 USD | `+65.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,180,000.00 USD | 2,710.00 USD | 0.00 USD | `+66.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,190,000.00 USD | 805.90 USD | 0.00 USD | `+68.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,190,000.00 USD | 655.55 USD | 0.00 USD | `+70.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,190,000.00 USD | 4,890.00 USD | 0.00 USD | `+71.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,190,000.00 USD | 471.09 USD | 0.00 USD | `+72.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,190,000.00 USD | 383.85 USD | 0.00 USD | `+73.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,850,000.00 USD | 653,420.00 USD | 0.00 USD | `+74.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,850,000.00 USD | 1,510.00 USD | 0.00 USD | `+75.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,850,000.00 USD | 111.87 USD | 0.00 USD | `+84.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,850,000.00 USD | 219.91 USD | 0.00 USD | `+86.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,850,000.00 USD | 121.74 USD | 0.00 USD | `+97.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.00` | 2,850,000.00 USD | 297.59 USD | 0.00 USD | `+97.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `17.20` | 2,970,000.00 USD | 120,270.00 USD | 0.00 USD | `+100.03%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.27` | 7,140,000.00 USD | 0.00 USD | 7,140,000.00 USD | 360.23 USD | 1,810.00 USD | 5,550.00 USD |
| `7D` | `7.31` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 104.04 USD |
| `7D` | `7.35` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 0.00 USD | 0.00 USD | 406.69 USD |
| `7D` | `7.37` | 7,130,000.00 USD | 0.00 USD | 7,130,000.00 USD | 45,620.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.39` | 7,080,000.00 USD | 0.00 USD | 7,080,000.00 USD | 46,200.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.45` | 7,030,000.00 USD | 0.00 USD | 7,030,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.49` | 7,010,000.00 USD | 0.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.51` | 6,990,000.00 USD | 0.00 USD | 6,990,000.00 USD | 2,070.00 USD | 0.00 USD | 18,280.00 USD |
| `7D` | `7.53` | 6,970,000.00 USD | 0.00 USD | 6,970,000.00 USD | 35,990.00 USD | 18,910.00 USD | 0.00 USD |
| `7D` | `7.55` | 6,910,000.00 USD | 0.00 USD | 6,910,000.00 USD | 20,150.00 USD | 4,310.00 USD | 0.00 USD |
| `1D` | `7.59` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 1,740.00 USD | 0.00 USD | 7,670.00 USD |
| `1D` | `7.60` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 706.40 USD | 4,900.00 USD | 351.13 USD |
| `1D` | `7.61` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,670.00 USD |
| `7D` | `7.61` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 626.55 USD | 0.00 USD | 301.55 USD |
| `1D` | `7.62` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 8,960.00 USD | 1,330.00 USD | 133.28 USD |
| `1D` | `7.63` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 5,940.00 USD | 0.00 USD | 9,660.00 USD |
| `7D` | `7.63` | 6,890,000.00 USD | 0.00 USD | 6,890,000.00 USD | 41,300.00 USD | 2,130.00 USD | 1,680.00 USD |
| `1D` | `7.64` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `1D` | `7.65` | 5,820,000.00 USD | 0.00 USD | 5,820,000.00 USD | 0.00 USD | 1,320.00 USD | 9,870.00 USD |
| `7D` | `7.65` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 4,870.00 USD | 2,350.00 USD | 0.00 USD |
| `1D` | `7.66` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `1D` | `7.67` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 1,410.00 USD | 1,110.00 USD | 1,790.00 USD |
| `7D` | `7.67` | 6,840,000.00 USD | 0.00 USD | 6,840,000.00 USD | 1,110.00 USD | 0.00 USD | 34,150.00 USD |
| `1D` | `7.68` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 892.30 USD | 0.00 USD | 5,300.00 USD |
| `1D` | `7.69` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 1,600.00 USD | 0.13 USD |
| `1D` | `7.70` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 4,490.00 USD | 4,000.00 USD | 19,040.00 USD |
| `1D` | `7.71` | 5,770,000.00 USD | 0.00 USD | 5,770,000.00 USD | 660.12 USD | 5,720.00 USD | 10,490.00 USD |
| `7D` | `7.71` | 6,800,000.00 USD | 0.00 USD | 6,800,000.00 USD | 393.33 USD | 1,650.00 USD | 33,200.00 USD |
| `1D` | `7.72` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 2,920.00 USD | 1,840.00 USD | 3,750.00 USD |
| `1D` | `7.73` | 5,740,000.00 USD | 0.00 USD | 5,740,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `7.73` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 39,770.00 USD | 2,520.00 USD | 7,340.00 USD |
| `1D` | `7.74` | 5,730,000.00 USD | 0.00 USD | 5,730,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `1D` | `7.75` | 5,710,000.00 USD | 0.00 USD | 5,710,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `7D` | `7.75` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 29,320.00 USD | 13,360.00 USD | 10,360.00 USD |
| `1D` | `7.76` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `1D` | `7.77` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `7D` | `7.77` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 20,120.00 USD | 4,900.00 USD | 6,580.00 USD |
| `1D` | `7.78` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `1D` | `7.79` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD |
| `7D` | `7.79` | 6,630,000.00 USD | 0.00 USD | 6,630,000.00 USD | 70,950.00 USD | 7,170.00 USD | 23,040.00 USD |
| `1D` | `7.80` | 5,640,000.00 USD | 0.00 USD | 5,640,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD |
| `1D` | `7.81` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.81` | 6,530,000.00 USD | 0.00 USD | 6,530,000.00 USD | 3,970.00 USD | 11,570.00 USD | 1,770.00 USD |
| `1D` | `7.82` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 248.67 USD | 1,680.00 USD | 0.00 USD |
| `1D` | `7.83` | 5,630,000.00 USD | 0.00 USD | 5,630,000.00 USD | 27,230.00 USD | 5,360.00 USD | 0.00 USD |
| `7D` | `7.83` | 6,510,000.00 USD | 0.00 USD | 6,510,000.00 USD | 29,530.00 USD | 2,130.00 USD | 24,330.00 USD |
| `1D` | `7.84` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 978.04 USD | 1,240.00 USD | 0.00 USD |
| `1D` | `7.85` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 3,320.00 USD | 639.88 USD | 2,650.00 USD |
| `7D` | `7.85` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 17,330.00 USD | 7,840.00 USD | 13,000.00 USD |
| `1D` | `7.86` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 1,290.00 USD | 6,270.00 USD | 13,940.00 USD |
| `1D` | `7.87` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 10,980.00 USD | 10,860.00 USD | 22,910.00 USD |
| `7D` | `7.87` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 150,960.00 USD | 1,540.00 USD | 22,350.00 USD |
| `1D` | `7.88` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 158,960.00 USD | 4,280.00 USD | 33,710.00 USD |
| `1D` | `7.89` | 5,320,000.00 USD | 0.00 USD | 5,320,000.00 USD | 57,720.00 USD | 3,720.00 USD | 27,230.00 USD |
| `7D` | `7.89` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 150,040.00 USD | 18,320.00 USD | 24,270.00 USD |
| `1D` | `7.90` | 5,230,000.00 USD | 0.00 USD | 5,230,000.00 USD | 56,410.00 USD | 6,970.00 USD | 4,310.00 USD |
| `1D` | `7.91` | 5,160,000.00 USD | 0.00 USD | 5,160,000.00 USD | 11,200.00 USD | 10,370.00 USD | 26,070.00 USD |
| `7D` | `7.91` | 6,050,000.00 USD | 0.00 USD | 6,050,000.00 USD | 31,740.00 USD | 26,330.00 USD | 45,390.00 USD |
| `1D` | `7.92` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 15,830.00 USD | 2,040.00 USD | 4,800.00 USD |
| `1D` | `7.93` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `7D` | `7.93` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 78,470.00 USD | 7,330.00 USD | 14,550.00 USD |
| `1D` | `7.94` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 15,580.00 USD | 20,510.00 USD | 61,750.00 USD |
| `1D` | `7.95` | 4,980,000.00 USD | 0.00 USD | 4,980,000.00 USD | 28,200.00 USD | 9,190.00 USD | 86,980.00 USD |
| `7D` | `7.95` | 5,850,000.00 USD | 0.00 USD | 5,850,000.00 USD | 45,890.00 USD | 9,500.00 USD | 102,940.00 USD |
| `1D` | `7.96` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `1D` | `7.97` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `7D` | `7.97` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 37,150.00 USD | 18,700.00 USD | 40,570.00 USD |
| `1D` | `7.98` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 5,610.00 USD | 2,060.00 USD | 42,970.00 USD |
| `1D` | `7.99` | 4,690,000.00 USD | 0.00 USD | 4,690,000.00 USD | 3,980.00 USD | 10,180.00 USD | 4,660.00 USD |
| `7D` | `7.99` | 5,590,000.00 USD | 0.00 USD | 5,590,000.00 USD | 53,780.00 USD | 20,640.00 USD | 122,290.00 USD |
| `1D` | `8.00` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `1D` | `8.01` | 4,590,000.00 USD | 0.00 USD | 4,590,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `7D` | `8.01` | 5,400,000.00 USD | 0.00 USD | 5,400,000.00 USD | 47,380.00 USD | 17,990.00 USD | 46,600.00 USD |
| `1D` | `8.02` | 4,580,000.00 USD | 0.00 USD | 4,580,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `1D` | `8.03` | 4,500,000.00 USD | 0.00 USD | 4,500,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `7D` | `8.03` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 353,080.00 USD | 35,720.00 USD | 49,900.00 USD |
| `1D` | `8.04` | 4,470,000.00 USD | 0.00 USD | 4,470,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `1D` | `8.05` | 4,410,000.00 USD | 0.00 USD | 4,410,000.00 USD | 318,600.00 USD | 6,430.00 USD | 53,960.00 USD |
| `7D` | `8.05` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 390,130.00 USD | 0.00 USD | 63,560.00 USD |
| `1D` | `8.06` | 4,030,000.00 USD | 0.00 USD | 4,030,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `1D` | `8.07` | 3,810,000.00 USD | 0.00 USD | 3,810,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `7D` | `8.07` | 4,390,000.00 USD | 0.00 USD | 4,390,000.00 USD | 60,670.00 USD | 0.00 USD | 75,410.00 USD |
| `1D` | `8.08` | 3,670,000.00 USD | 0.00 USD | 3,670,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `1D` | `8.09` | 3,590,000.00 USD | 0.00 USD | 3,590,000.00 USD | 3,650.00 USD | 0.00 USD | 29,580.00 USD |
| `7D` | `8.09` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 32,760.00 USD | 0.00 USD | 81,280.00 USD |
| `1D` | `8.10` | 3,550,000.00 USD | 0.00 USD | 3,550,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `1D` | `8.11` | 3,390,000.00 USD | 0.00 USD | 3,390,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `7D` | `8.11` | 4,140,000.00 USD | 0.00 USD | 4,140,000.00 USD | 33,000.00 USD | 0.00 USD | 140,250.00 USD |
| `1D` | `8.12` | 3,120,000.00 USD | 0.00 USD | 3,120,000.00 USD | 20,660.00 USD | 11,230.00 USD | 126,250.00 USD |
| `1D` | `8.13` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 35,600.00 USD | 9,180.00 USD | 1,710.00 USD |
| `7D` | `8.13` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 48,900.00 USD | 12,740.00 USD | 20,490.00 USD |
| `1D` | `8.14` | 2,910,000.00 USD | 0.00 USD | 2,910,000.00 USD | 17,740.00 USD | 8,630.00 USD | 105,270.00 USD |
| `1D` | `8.15` | 2,780,000.00 USD | 0.00 USD | 2,780,000.00 USD | 47,020.00 USD | 12,240.00 USD | 53,660.00 USD |
| `7D` | `8.15` | 3,890,000.00 USD | 0.00 USD | 3,890,000.00 USD | 179,060.00 USD | 31,560.00 USD | 183,290.00 USD |
| `1D` | `8.16` | 2,670,000.00 USD | 0.00 USD | 2,670,000.00 USD | 192.50 USD | 22,250.00 USD | 165,460.00 USD |
| `1D` | `8.17` | 2,480,000.00 USD | 0.00 USD | 2,480,000.00 USD | 11,100.00 USD | 9,120.00 USD | 183,140.00 USD |
| `7D` | `8.17` | 3,490,000.00 USD | 0.00 USD | 3,490,000.00 USD | 1,590.00 USD | 13,650.00 USD | 149,580.00 USD |
| `1D` | `8.18` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 7,140.00 USD | 3,280.00 USD | 4,190.00 USD |
| `1D` | `8.19` | 2,260,000.00 USD | 0.00 USD | 2,260,000.00 USD | 18,260.00 USD | 545.08 USD | 19,120.00 USD |
| `7D` | `8.19` | 3,330,000.00 USD | 0.00 USD | 3,330,000.00 USD | 1,200.00 USD | 72,340.00 USD | 23,200.00 USD |
| `1D` | `8.20` | 2,230,000.00 USD | 0.00 USD | 2,230,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `1D` | `8.21` | 2,180,000.00 USD | 0.00 USD | 2,180,000.00 USD | 41,620.00 USD | 2,210.00 USD | 0.00 USD |
| `7D` | `8.21` | 3,230,000.00 USD | 0.00 USD | 3,230,000.00 USD | 174,220.00 USD | 22,240.00 USD | 0.00 USD |
| `1D` | `8.22` | 2,140,000.00 USD | 0.00 USD | 2,140,000.00 USD | 6,810.00 USD | 3,080.00 USD | 21,990.00 USD |
| `1D` | `8.23` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 0.00 USD | 3,450.00 USD | 10,090.00 USD |
| `7D` | `8.23` | 3,040,000.00 USD | 0.00 USD | 3,040,000.00 USD | 0.00 USD | 40,910.00 USD | 5,650.00 USD |
| `1D` | `8.24` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 5,700.00 USD | 6,390.00 USD | 9,270.00 USD |
| `1D` | `8.25` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `7D` | `8.25` | 2,990,000.00 USD | 0.00 USD | 2,990,000.00 USD | 129,050.00 USD | 12,050.00 USD | 17,610.00 USD |
| `1D` | `8.26` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 50,590.00 USD | 12,510.00 USD | 25,360.00 USD |
| `1D` | `8.27` | 1,940,000.00 USD | 0.00 USD | 1,940,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,120.00 USD |
| `7D` | `8.27` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 103,730.00 USD | 4,000.00 USD | 37,940.00 USD |
| `1D` | `8.28` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `1D` | `8.29` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 39,480.00 USD | 11,800.00 USD | 0.00 USD |
| `7D` | `8.29` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 166,800.00 USD | 6,550.00 USD | 21,950.00 USD |
| `1D` | `8.30` | 1,830,000.00 USD | 0.00 USD | 1,830,000.00 USD | 69,220.00 USD | 13,810.00 USD | 20,060.00 USD |
| `1D` | `8.31` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 82,900.00 USD | 11,920.00 USD | 56,400.00 USD |
| `7D` | `8.31` | 2,490,000.00 USD | 0.00 USD | 2,490,000.00 USD | 370,260.00 USD | 10,660.00 USD | 2,790.00 USD |
| `1D` | `8.32` | 1,570,000.00 USD | 0.00 USD | 1,570,000.00 USD | 80,060.00 USD | 6,080.00 USD | 14,060.00 USD |
| `1D` | `8.33` | 1,470,000.00 USD | 0.00 USD | 1,470,000.00 USD | 0.00 USD | 8,710.00 USD | 109.14 USD |
| `7D` | `8.33` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 14,600.00 USD | 11,770.00 USD | 4,900.00 USD |
| `1D` | `8.34` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 3,230.00 USD | 13.84 USD |
| `1D` | `8.35` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 0.00 USD | 23,440.00 USD | 25,350.00 USD |
| `7D` | `8.35` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 223,170.00 USD | 0.00 USD | 5,720.00 USD |
| `1D` | `8.36` | 1,410,000.00 USD | 0.00 USD | 1,410,000.00 USD | 0.00 USD | 1,090.00 USD | 25,130.00 USD |
| `1D` | `8.37` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `7D` | `8.37` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 36,530.00 USD |
| `1D` | `8.38` | 1,370,000.00 USD | 0.00 USD | 1,370,000.00 USD | 17,220.00 USD | 7,830.00 USD | 50,290.00 USD |
| `1D` | `8.39` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 114,370.00 USD | 19,770.00 USD | 43,980.00 USD |
| `7D` | `8.39` | 1,810,000.00 USD | 0.00 USD | 1,810,000.00 USD | 0.00 USD | 15,860.00 USD | 68,640.00 USD |
| `1D` | `8.40` | 1,120,000.00 USD | 0.00 USD | 1,120,000.00 USD | 10,500.00 USD | 10,400.00 USD | 72,020.00 USD |
| `1D` | `8.41` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 11,070.00 USD | 12,780.00 USD | 18,540.00 USD |
| `7D` | `8.41` | 1,720,000.00 USD | 0.00 USD | 1,720,000.00 USD | 194,850.00 USD | 0.00 USD | 100,330.00 USD |
| `1D` | `8.42` | 981,740.00 USD | 0.00 USD | 981,740.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `1D` | `8.43` | 922,590.00 USD | 0.00 USD | 922,590.00 USD | 81,350.00 USD | 7,730.00 USD | 11,670.00 USD |
| `7D` | `8.43` | 1,430,000.00 USD | 0.00 USD | 1,430,000.00 USD | 163,340.00 USD | 12,610.00 USD | 22,840.00 USD |
| `1D` | `8.44` | 821,850.00 USD | 0.00 USD | 821,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `1D` | `8.45` | 617,870.00 USD | 0.00 USD | 617,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `8.45` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 156,410.00 USD | 8,000.00 USD | 171,560.00 USD |
| `1D` | `8.47` | 557,120.00 USD | 0.00 USD | 557,120.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 894,220.00 USD | 0.00 USD | 894,220.00 USD | 0.00 USD | 0.00 USD | 38,730.00 USD |
| `1D` | `8.48` | 556,450.00 USD | 0.00 USD | 556,450.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.49` | 555,700.00 USD | 0.00 USD | 555,700.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.49` | 855,480.00 USD | 0.00 USD | 855,480.00 USD | 0.00 USD | 0.00 USD | 153,260.00 USD |
| `7D` | `8.51` | 702,220.00 USD | 0.00 USD | 702,220.00 USD | 0.00 USD | 0.00 USD | 92,390.00 USD |
| `1D` | `8.52` | 555,690.00 USD | 0.00 USD | 555,690.00 USD | 158,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.53` | 397,060.00 USD | 0.00 USD | 397,060.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.53` | 609,830.00 USD | 0.00 USD | 609,830.00 USD | 173,370.00 USD | 0.00 USD | 1,390.00 USD |
| `1D` | `8.54` | 372,880.00 USD | 0.00 USD | 372,880.00 USD | 198,250.00 USD | 0.00 USD | 156.94 USD |
| `1D` | `8.55` | 174,470.00 USD | 0.00 USD | 174,470.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `7D` | `8.55` | 435,070.00 USD | 0.00 USD | 435,070.00 USD | 434,770.00 USD | 0.00 USD | 300.56 USD |
| `1D` | `8.56` | 147,690.00 USD | 0.00 USD | 147,690.00 USD | 686.73 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.57` | 147,010.00 USD | 0.00 USD | 147,010.00 USD | 147,010.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.57` | 4,370.00 USD | 4,370.00 USD | 0.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.57` | 8,740.00 USD | 8,740.00 USD | 0.00 USD | 4,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 842.65 USD | 842.65 USD | 0.00 USD | 842.65 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 1,690.00 USD | 1,690.00 USD | 0.00 USD | 842.65 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.59` | 9,770.00 USD | 9,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,040.00 USD |
| `1D` | `8.60` | 3,720.00 USD | 3,720.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.61` | 4,920.00 USD | 4,920.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `7D` | `8.61` | 12,860.00 USD | 12,860.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 271.28 USD |
| `1D` | `8.62` | 172,190.00 USD | 172,190.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `1D` | `8.63` | 303,890.00 USD | 303,890.00 USD | 0.00 USD | 129,280.00 USD | 2,420.00 USD | 0.00 USD |
| `7D` | `8.63` | 41,370.00 USD | 41,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,520.00 USD |
| `1D` | `8.64` | 385,870.00 USD | 385,870.00 USD | 0.00 USD | 69,220.00 USD | 9,340.00 USD | 3,410.00 USD |
| `1D` | `8.65` | 447,970.00 USD | 447,970.00 USD | 0.00 USD | 35,830.00 USD | 9,010.00 USD | 17,260.00 USD |
| `7D` | `8.65` | 92,290.00 USD | 92,290.00 USD | 0.00 USD | 40,260.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.66` | 477,280.00 USD | 477,280.00 USD | 0.00 USD | 13,240.00 USD | 2,020.00 USD | 14,040.00 USD |
| `1D` | `8.67` | 490,680.00 USD | 490,680.00 USD | 0.00 USD | 880.60 USD | 12,460.00 USD | 56.72 USD |
| `7D` | `8.67` | 105,620.00 USD | 105,620.00 USD | 0.00 USD | 0.00 USD | 11,770.00 USD | 1,570.00 USD |
| `1D` | `8.68` | 530,190.00 USD | 530,190.00 USD | 0.00 USD | 588.00 USD | 13,040.00 USD | 25,890.00 USD |
| `1D` | `8.69` | 606,050.00 USD | 606,050.00 USD | 0.00 USD | 10,820.00 USD | 22,830.00 USD | 42,210.00 USD |
| `7D` | `8.69` | 346,630.00 USD | 346,630.00 USD | 0.00 USD | 29,260.00 USD | 48,960.00 USD | 162,790.00 USD |
| `1D` | `8.70` | 700,570.00 USD | 700,570.00 USD | 0.00 USD | 62,600.00 USD | 1,090.00 USD | 30,830.00 USD |
| `1D` | `8.71` | 727,270.00 USD | 727,270.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `7D` | `8.71` | 444,860.00 USD | 444,860.00 USD | 0.00 USD | 87,110.00 USD | 11,120.00 USD | 0.00 USD |
| `1D` | `8.72` | 816,520.00 USD | 816,520.00 USD | 0.00 USD | 34,050.00 USD | 4,410.00 USD | 50,790.00 USD |
| `1D` | `8.73` | 921,660.00 USD | 921,660.00 USD | 0.00 USD | 26,200.00 USD | 34,960.00 USD | 43,980.00 USD |
| `7D` | `8.73` | 516,230.00 USD | 516,230.00 USD | 0.00 USD | 51,030.00 USD | 19,040.00 USD | 1,300.00 USD |
| `1D` | `8.74` | 1,000,000.00 USD | 1,000,000.00 USD | 0.00 USD | 38,500.00 USD | 6,910.00 USD | 33,010.00 USD |
| `1D` | `8.75` | 1,080,000.00 USD | 1,080,000.00 USD | 0.00 USD | 44,580.00 USD | 15,310.00 USD | 23,520.00 USD |
| `7D` | `8.75` | 779,400.00 USD | 779,400.00 USD | 0.00 USD | 196,960.00 USD | 19,690.00 USD | 46,530.00 USD |
| `1D` | `8.76` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `1D` | `8.77` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 47,150.00 USD |
| `7D` | `8.77` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 141,710.00 USD | 12,610.00 USD | 105,410.00 USD |
| `1D` | `8.78` | 1,560,000.00 USD | 1,560,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `1D` | `8.79` | 1,640,000.00 USD | 1,640,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `7D` | `8.79` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 29,660.00 USD | 33,300.00 USD | 65,190.00 USD |
| `1D` | `8.80` | 1,790,000.00 USD | 1,790,000.00 USD | 0.00 USD | 113,160.00 USD | 19,150.00 USD | 23,840.00 USD |
| `1D` | `8.81` | 1,860,000.00 USD | 1,860,000.00 USD | 0.00 USD | 53,290.00 USD | 9,030.00 USD | 1,750.00 USD |
| `7D` | `8.81` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 122,920.00 USD | 26,890.00 USD | 58,050.00 USD |
| `1D` | `8.82` | 1,940,000.00 USD | 1,940,000.00 USD | 0.00 USD | 19,950.00 USD | 4,510.00 USD | 61,490.00 USD |
| `1D` | `8.83` | 2,140,000.00 USD | 2,140,000.00 USD | 0.00 USD | 174,730.00 USD | 19,400.00 USD | 7,020.00 USD |
| `7D` | `8.83` | 1,620,000.00 USD | 1,620,000.00 USD | 0.00 USD | 242,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.84` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 1,500.00 USD | 4,360.00 USD | 59,130.00 USD |
| `1D` | `8.85` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 13,040.00 USD | 3,870.00 USD | 11,200.00 USD |
| `7D` | `8.85` | 1,710,000.00 USD | 1,710,000.00 USD | 0.00 USD | 29,310.00 USD | 5,880.00 USD | 58,190.00 USD |
| `1D` | `8.86` | 2,250,000.00 USD | 2,250,000.00 USD | 0.00 USD | 2,060.00 USD | 3,280.00 USD | 4,790.00 USD |
| `1D` | `8.87` | 2,260,000.00 USD | 2,260,000.00 USD | 0.00 USD | 1,410.00 USD | 545.08 USD | 12,570.00 USD |
| `7D` | `8.87` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 24,800.00 USD |
| `1D` | `8.88` | 2,280,000.00 USD | 2,280,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `1D` | `8.89` | 2,330,000.00 USD | 2,330,000.00 USD | 0.00 USD | 13,040.00 USD | 4,360.00 USD | 32,950.00 USD |
| `7D` | `8.89` | 1,810,000.00 USD | 1,810,000.00 USD | 0.00 USD | 1,250.00 USD | 0.00 USD | 73,830.00 USD |
| `1D` | `8.90` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 35,510.00 USD | 9,060.00 USD | 70,850.00 USD |
| `1D` | `8.91` | 2,510,000.00 USD | 2,510,000.00 USD | 0.00 USD | 32,240.00 USD | 13,320.00 USD | 23,580.00 USD |
| `7D` | `8.91` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 2,440.00 USD | 4,130.00 USD | 94,270.00 USD |
| `1D` | `8.92` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 6,640.00 USD | 6,390.00 USD | 9,340.00 USD |
| `1D` | `8.93` | 2,610,000.00 USD | 2,610,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `7D` | `8.93` | 2,090,000.00 USD | 2,090,000.00 USD | 0.00 USD | 157,480.00 USD | 6,300.00 USD | 17,610.00 USD |
| `1D` | `8.94` | 2,680,000.00 USD | 2,680,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 5,830.00 USD |
| `1D` | `8.95` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 3,080.00 USD | 6,630.00 USD | 20,340.00 USD |
| `7D` | `8.95` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 74,920.00 USD | 4,000.00 USD | 38,550.00 USD |
| `1D` | `8.96` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `1D` | `8.97` | 2,710,000.00 USD | 2,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.26 USD |
| `7D` | `8.97` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 1,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.98` | 2,780,000.00 USD | 2,780,000.00 USD | 0.00 USD | 36,060.00 USD | 9,420.00 USD | 19,670.00 USD |
| `1D` | `8.99` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 49,090.00 USD | 22,110.00 USD | 3,420.00 USD |
| `7D` | `8.99` | 2,400,000.00 USD | 2,400,000.00 USD | 0.00 USD | 147,500.00 USD | 6,550.00 USD | 29,050.00 USD |
| `1D` | `9.00` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,750.00 USD |
| `1D` | `9.01` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `7D` | `9.01` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 303,030.00 USD | 36,180.00 USD | 23,020.00 USD |
| `1D` | `9.02` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD |
| `1D` | `9.03` | 3,240,000.00 USD | 3,240,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD |
| `7D` | `9.03` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 107,490.00 USD | 101,140.00 USD | 15,640.00 USD |
| `1D` | `9.04` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 41,710.00 USD | 5,900.00 USD | 14,800.00 USD |
| `1D` | `9.05` | 3,360,000.00 USD | 3,360,000.00 USD | 0.00 USD | 21,980.00 USD | 7,560.00 USD | 22,410.00 USD |
| `7D` | `9.05` | 3,080,000.00 USD | 3,080,000.00 USD | 0.00 USD | 38,740.00 USD | 17,700.00 USD | 39,710.00 USD |
| `1D` | `9.06` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 28,180.00 USD | 5,480.00 USD | 10,490.00 USD |
| `1D` | `9.07` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 13,070.00 USD | 15,350.00 USD | 25,460.00 USD |
| `7D` | `9.07` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 3,990.00 USD | 14,140.00 USD | 36,530.00 USD |
| `1D` | `9.08` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 12,960.00 USD | 1,040.00 USD | 24,280.00 USD |
| `1D` | `9.09` | 3,600,000.00 USD | 3,600,000.00 USD | 0.00 USD | 71,230.00 USD | 9,730.00 USD | 25,300.00 USD |
| `7D` | `9.09` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 152,640.00 USD | 8,680.00 USD | 144,360.00 USD |
| `1D` | `9.10` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 16,320.00 USD | 10,640.00 USD | 30,930.00 USD |
| `1D` | `9.11` | 3,800,000.00 USD | 3,800,000.00 USD | 0.00 USD | 51,080.00 USD | 14,420.00 USD | 82,390.00 USD |
| `7D` | `9.11` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 877,120.00 USD | 37,620.00 USD | 570,050.00 USD |
| `1D` | `9.12` | 3,950,000.00 USD | 3,950,000.00 USD | 0.00 USD | 94,950.00 USD | 21,650.00 USD | 26,360.00 USD |
| `1D` | `9.13` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 75,800.00 USD | 15,960.00 USD | 35,980.00 USD |
| `7D` | `9.13` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 668,090.00 USD | 26,540.00 USD | 484,710.00 USD |
| `1D` | `9.14` | 4,120,000.00 USD | 4,120,000.00 USD | 0.00 USD | 20,200.00 USD | 0.00 USD | 24,040.00 USD |
| `1D` | `9.15` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 56,980.00 USD | 20,890.00 USD | 13,120.00 USD |
| `7D` | `9.15` | 6,770,000.00 USD | 6,770,000.00 USD | 0.00 USD | 357,020.00 USD | 38,700.00 USD | 270,200.00 USD |
| `1D` | `9.16` | 4,330,000.00 USD | 4,330,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `1D` | `9.17` | 4,460,000.00 USD | 4,460,000.00 USD | 0.00 USD | 74,820.00 USD | 3,200.00 USD | 49,540.00 USD |
| `7D` | `9.17` | 7,620,000.00 USD | 7,620,000.00 USD | 0.00 USD | 409,650.00 USD | 133,490.00 USD | 303,370.00 USD |
| `1D` | `9.18` | 4,540,000.00 USD | 4,540,000.00 USD | 0.00 USD | 28,310.00 USD | 26,430.00 USD | 31,220.00 USD |
| `1D` | `9.19` | 4,660,000.00 USD | 4,660,000.00 USD | 0.00 USD | 77,890.00 USD | 29,140.00 USD | 7,680.00 USD |
| `7D` | `9.19` | 8,420,000.00 USD | 8,420,000.00 USD | 0.00 USD | 504,150.00 USD | 108,440.00 USD | 193,800.00 USD |
| `1D` | `9.20` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `1D` | `9.21` | 4,810,000.00 USD | 4,810,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `7D` | `9.21` | 9,430,000.00 USD | 9,430,000.00 USD | 0.00 USD | 590,780.00 USD | 144,470.00 USD | 277,570.00 USD |
| `1D` | `9.22` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 58,060.00 USD | 2,850.00 USD | 11,100.00 USD |
| `1D` | `9.23` | 4,890,000.00 USD | 4,890,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `7D` | `9.23` | 10,440,000.00 USD | 10,440,000.00 USD | 0.00 USD | 582,450.00 USD | 92,780.00 USD | 331,960.00 USD |
| `1D` | `9.24` | 4,930,000.00 USD | 4,930,000.00 USD | 0.00 USD | 45,580.00 USD | 0.00 USD | 3,020.00 USD |
| `1D` | `9.25` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD |
| `7D` | `9.25` | 10,840,000.00 USD | 10,840,000.00 USD | 0.00 USD | 277,290.00 USD | 61,940.00 USD | 61,110.00 USD |
| `1D` | `9.26` | 4,970,000.00 USD | 4,970,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `1D` | `9.27` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 23,430.00 USD | 1,360.00 USD | 6,640.00 USD |
| `7D` | `9.27` | 11,140,000.00 USD | 11,140,000.00 USD | 0.00 USD | 156,190.00 USD | 102,670.00 USD | 37,770.00 USD |
| `1D` | `9.28` | 5,010,000.00 USD | 5,010,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `1D` | `9.29` | 5,050,000.00 USD | 5,050,000.00 USD | 0.00 USD | 16,070.00 USD | 4,140.00 USD | 17,910.00 USD |
| `7D` | `9.29` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 392,980.00 USD | 82,050.00 USD | 244,470.00 USD |
| `1D` | `9.30` | 5,110,000.00 USD | 5,110,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD |
| `1D` | `9.31` | 5,160,000.00 USD | 5,160,000.00 USD | 0.00 USD | 28,930.00 USD | 5,500.00 USD | 12,920.00 USD |
| `7D` | `9.31` | 12,420,000.00 USD | 12,420,000.00 USD | 0.00 USD | 308,150.00 USD | 44,500.00 USD | 209,900.00 USD |
| `1D` | `9.32` | 5,180,000.00 USD | 5,180,000.00 USD | 0.00 USD | 17,660.00 USD | 1,330.00 USD | 5,070.00 USD |
| `1D` | `9.33` | 5,210,000.00 USD | 5,210,000.00 USD | 0.00 USD | 12,710.00 USD | 6,000.00 USD | 9,780.00 USD |
| `7D` | `9.33` | 12,670,000.00 USD | 12,670,000.00 USD | 0.00 USD | 134,040.00 USD | 29,420.00 USD | 82,320.00 USD |
| `1D` | `9.34` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 46,100.00 USD | 3,660.00 USD | 5,580.00 USD |
| `1D` | `9.35` | 5,300,000.00 USD | 5,300,000.00 USD | 0.00 USD | 13,620.00 USD | 1,320.00 USD | 14,910.00 USD |
| `7D` | `9.35` | 12,940,000.00 USD | 12,940,000.00 USD | 0.00 USD | 114,090.00 USD | 67,130.00 USD | 96,310.00 USD |
| `1D` | `9.36` | 5,320,000.00 USD | 5,320,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `1D` | `9.37` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 12,860.00 USD | 6,780.00 USD | 4,400.00 USD |
| `7D` | `9.37` | 13,280,000.00 USD | 13,280,000.00 USD | 0.00 USD | 211,790.00 USD | 34,660.00 USD | 85,580.00 USD |
| `1D` | `9.38` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 15,310.00 USD |
| `1D` | `9.39` | 5,380,000.00 USD | 5,380,000.00 USD | 0.00 USD | 8,850.00 USD | 1,600.00 USD | 12.83 USD |
| `7D` | `9.39` | 13,600,000.00 USD | 13,600,000.00 USD | 0.00 USD | 206,980.00 USD | 32,960.00 USD | 87,830.00 USD |
| `1D` | `9.40` | 5,400,000.00 USD | 5,400,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `1D` | `9.41` | 5,420,000.00 USD | 5,420,000.00 USD | 0.00 USD | 4,410.00 USD | 378.69 USD | 10,140.00 USD |
| `7D` | `9.41` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 265,720.00 USD | 30,790.00 USD | 99,880.00 USD |
| `1D` | `9.42` | 5,440,000.00 USD | 5,440,000.00 USD | 0.00 USD | 9,600.00 USD | 3,630.00 USD | 8,800.00 USD |
| `1D` | `9.43` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 5,380.00 USD | 1,380.00 USD | 3,110.00 USD |
| `7D` | `9.43` | 14,090,000.00 USD | 14,090,000.00 USD | 0.00 USD | 33,890.00 USD | 15,080.00 USD | 42,490.00 USD |
| `1D` | `9.44` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 3,010.00 USD | 1,840.00 USD | 3,750.00 USD |
| `1D` | `9.45` | 5,460,000.00 USD | 5,460,000.00 USD | 0.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD |
| `7D` | `9.45` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 68,680.00 USD | 11,560.00 USD | 8,600.00 USD |
| `1D` | `9.46` | 5,480,000.00 USD | 5,480,000.00 USD | 0.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `9.47` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD |
| `7D` | `9.47` | 14,240,000.00 USD | 14,240,000.00 USD | 0.00 USD | 44,170.00 USD | 5,760.00 USD | 12,750.00 USD |
| `1D` | `9.48` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 0.00 USD | 494.12 USD | 0.00 USD |
| `1D` | `9.49` | 5,510,000.00 USD | 5,510,000.00 USD | 0.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD |
| `7D` | `9.49` | 14,280,000.00 USD | 14,280,000.00 USD | 0.00 USD | 25,360.00 USD | 4,900.00 USD | 6,210.00 USD |
| `7D` | `9.51` | 14,370,000.00 USD | 14,370,000.00 USD | 0.00 USD | 57,130.00 USD | 7,150.00 USD | 25,660.00 USD |
| `7D` | `9.53` | 14,430,000.00 USD | 14,430,000.00 USD | 0.00 USD | 50,200.00 USD | 9,410.00 USD | 1,270.00 USD |
| `7D` | `9.55` | 14,450,000.00 USD | 14,450,000.00 USD | 0.00 USD | 11,560.00 USD | 11,570.00 USD | 880.26 USD |
| `7D` | `9.57` | 14,510,000.00 USD | 14,510,000.00 USD | 0.00 USD | 31,530.00 USD | 2,130.00 USD | 24,130.00 USD |
| `7D` | `9.59` | 14,550,000.00 USD | 14,550,000.00 USD | 0.00 USD | 14,070.00 USD | 7,840.00 USD | 14,300.00 USD |
| `7D` | `9.61` | 14,600,000.00 USD | 14,600,000.00 USD | 0.00 USD | 37,000.00 USD | 0.00 USD | 11,290.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `412.12M` | Total OI Tokens: `2,129,191,146.8 AVAX`
  * 1h OI Change: `-0.82%` | 4h OI Change: `+0.69%` | 24h OI Change: `-8.31%`
  * Exchange Breakdown: Binance=`75.16M` | Bybit=`50.31M` | OKX=`29.55M` | Hyperliquid=`28.06M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `9.11K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0079%` |
| **USDT Bybit** | `0.0018%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0059%` | **USDT Bitget** | `0.0018%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `43.58%` | `56.42%` | `0.77` | 5,210,000.00 USD |
| `15M` | `Binance` | `45.12%` | `54.88%` | `0.82` | 1,540,000.00 USD |
| `15M` | `OKX` | `36.97%` | `63.03%` | `0.59` | 476,170.00 USD |
| `15M` | `Bybit` | `45.74%` | `54.26%` | `0.84` | 834,670.00 USD |
| `15M` | `KuCoin` | `52.29%` | `47.71%` | `1.10` | 19,030.00 USD |
| `15M` | `Gate` | `48.81%` | `51.19%` | `0.95` | 99,000.00 USD |
| `15M` | `Bitget` | `26.32%` | `73.68%` | `0.36` | 213,510.00 USD |
| `15M` | `BingX` | `36.83%` | `63.17%` | `0.58` | 133,160.00 USD |
| `15M` | `MEXC` | `46.22%` | `53.78%` | `0.86` | 1,360,000.00 USD |
| `15M` | `Bitunix` | `44.84%` | `55.16%` | `0.81` | 219,950.00 USD |
| `15M` | `Hyperliquid` | `30.92%` | `69.08%` | `0.45` | 68,840.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.03%` | `49.97%` | `1.00` | 167,240.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `8.32%` | `91.68%` | `0.09` | 4,340.00 USD |
| `15M` | `HTX` | `55.42%` | `44.58%` | `1.24` | 519.93 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `74.26%` | `25.74%` | `2.89` | 19,630.00 USD |
| `15M` | `Aster` | `0.02%` | `99.98%` | `0.00` | 35,990.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `26.03%` | `73.97%` | `0.35` | 5,540.00 USD |
| `15M` | `Whale Positions` | `45.12%` | `54.88%` | `0.82` | 1,540,000.00 USD |
| `15M` | `Global Accounts` | `43.58%` | `56.42%` | `0.77` | 5,210,000.00 USD |
| `1H` | `AVAX` | `45.98%` | `54.02%` | `0.85` | 17,510,000.00 USD |
| `1H` | `Binance` | `48.34%` | `51.66%` | `0.94` | 5,300,000.00 USD |
| `1H` | `OKX` | `36.45%` | `63.55%` | `0.57` | 1,890,000.00 USD |
| `1H` | `Bybit` | `45.97%` | `54.03%` | `0.85` | 1,460,000.00 USD |
| `1H` | `KuCoin` | `26.47%` | `73.53%` | `0.36` | 107,990.00 USD |
| `1H` | `Gate` | `50.09%` | `49.91%` | `1.00` | 199,010.00 USD |
| `1H` | `Bitget` | `39.93%` | `60.07%` | `0.66` | 753,100.00 USD |
| `1H` | `BingX` | `58.3%` | `41.7%` | `1.40` | 499,250.00 USD |
| `1H` | `MEXC` | `47.95%` | `52.05%` | `0.92` | 5,090,000.00 USD |
| `1H` | `Bitunix` | `39.65%` | `60.35%` | `0.66` | 682,270.00 USD |
| `1H` | `Hyperliquid` | `48.68%` | `51.32%` | `0.95` | 233,250.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `48.72%` | `51.28%` | `0.95` | 994,120.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.44%` | `99.56%` | `0.00` | 81,220.00 USD |
| `1H` | `HTX` | `91.49%` | `8.51%` | `10.75` | 8,880.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `47.24%` | `52.76%` | `0.90` | 109,920.00 USD |
| `1H` | `Aster` | `29.39%` | `70.61%` | `0.42` | 63,930.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `60.83%` | `39.17%` | `1.55` | 29,050.00 USD |
| `1H` | `Whale Positions` | `48.34%` | `51.66%` | `0.94` | 5,300,000.00 USD |
| `1H` | `Global Accounts` | `45.98%` | `54.02%` | `0.85` | 17,510,000.00 USD |
| `4H` | `AVAX` | `45.90%` | `54.10%` | `0.85` | 60,860,000.00 USD |
| `4H` | `Binance` | `50.23%` | `49.77%` | `1.01` | 17,100,000.00 USD |
| `4H` | `OKX` | `52.05%` | `47.95%` | `1.09` | 3,210,000.00 USD |
| `4H` | `Bybit` | `44.04%` | `55.96%` | `0.79` | 3,200,000.00 USD |
| `4H` | `KuCoin` | `45.08%` | `54.92%` | `0.82` | 415,380.00 USD |
| `4H` | `Gate` | `46.77%` | `53.23%` | `0.88` | 713,030.00 USD |
| `4H` | `Bitget` | `40.88%` | `59.12%` | `0.69` | 1,010,000.00 USD |
| `4H` | `BingX` | `46.51%` | `53.49%` | `0.87` | 16,600,000.00 USD |
| `4H` | `MEXC` | `56.81%` | `43.19%` | `1.32` | 3,750,000.00 USD |
| `4H` | `Bitunix` | `66.78%` | `33.22%` | `2.01` | 1,260,000.00 USD |
| `4H` | `Hyperliquid` | `45.41%` | `54.59%` | `0.83` | 625,190.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.39%` | `49.61%` | `1.02` | 7,860,000.00 USD |
| `4H` | `Crypto.com` | `47.73%` | `52.27%` | `0.91` | 11,840.00 USD |
| `4H` | `WhiteBIT` | `3.77%` | `96.23%` | `0.04` | 4,340,000.00 USD |
| `4H` | `HTX` | `34.69%` | `65.31%` | `0.53` | 70,350.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `21.3%` | `78.7%` | `0.27` | 479,670.00 USD |
| `4H` | `Aster` | `38.09%` | `61.91%` | `0.62` | 33,940.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `49.04%` | `50.96%` | `0.96` | 153,500.00 USD |
| `4H` | `Whale Positions` | `50.23%` | `49.77%` | `1.01` | 17,100,000.00 USD |
| `4H` | `Global Accounts` | `45.90%` | `54.10%` | `0.85` | 60,860,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.49` | `8.46` | 909,192.14 USD | 370,410.27 USD | 538,781.87 USD | -168,371.60 USD | `-18.52%` | `3B / 9S` |
| `0:00 UTC` | `8.47` | `8.48` | `8.47` | `8.49` | `8.46` | 824,624.01 USD | 408,080.13 USD | 416,543.88 USD | -8,463.75 USD | `-1.03%` | `2B / 3S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.54` | `8.47` | 897,869.95 USD | 576,315.84 USD | 321,554.11 USD | 254,761.73 USD | `+28.37%` | `17B / 7S` |
| `0:00 UTC` | `8.56` | `8.54` | `8.56` | `8.56` | `8.50` | 1,085,360.20 USD | 616,505.04 USD | 468,855.16 USD | 147,649.89 USD | `+13.60%` | `20B / 10S` |
| `5:00 UTC` | `8.58` | `8.57` | `8.58` | `8.60` | `8.53` | 1,039,077.87 USD | 744,973.52 USD | 294,104.35 USD | 450,869.18 USD | `+43.39%` | `24B / 5S` |
| `0:00 UTC` | `8.58` | `8.59` | `8.58` | `8.62` | `8.57` | 932,864.48 USD | 399,199.64 USD | 533,664.84 USD | -134,465.20 USD | `-14.41%` | `5B / 11S` |
| `5:00 UTC` | `8.56` | `8.56` | `8.56` | `8.59` | `8.55` | 162,836.10 USD | 67,515.98 USD | 95,320.13 USD | -27,804.15 USD | `-17.07%` | `2B / 15S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:30` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 20:17` | `Volume 200K AVAX` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.88` | 0.00 USD | 0.00 USD |
| `10-28 19:50` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.79` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Volume 200K AVAX` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.81` | 35,000.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 0.025` | `Bull div` | **`BULLISH`** | Lower low, higher Cumulative Delta | `8.81` | 28,000.00 USD | 0.00 USD |
| `10-28 19:05` | `Volume 200K AVAX` | `Divergence` | **`BULLISH`** | Drop without taker selling | `8.86` | 0.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 18:17` | `Range 0.025` | `Trapped shorts` | **`BULLISH`** | Failed breakdown | `8.85` | 15,000.00 USD | 0.00 USD |
| `10-28 17:45` | `Volume 200K AVAX` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.90` | 0.00 USD | 0.00 USD |
| `10-28 17:35` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `8.96` | 41,000.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `9.02` | 0.00 USD | 0.00 USD |
| `10-28 15:02` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.99` | 0.00 USD | 0.00 USD |
| `10-28 14:06` | `Range 0.025` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 114,000.00 USD | 0.00 USD |
| `10-28 14:01` | `Volume 200K AVAX` | `Bear div` | **`BEARISH`** | Higher high, lower Cumulative Delta | `9.08` | 125,000.00 USD | 0.00 USD |
| `10-28 13:57` | `Range 0.025` | `Divergence` | **`BULLISH`** | Drop without taker selling | `9.03` | 0.00 USD | 0.00 USD |
| `10-28 13:44` | `Range 0.025` | `Absorption` | **`BULLISH`** | Selling absorbed at the low | `9.00` | 16,000.00 USD | 0.00 USD |
| `10-28 12:46` | `Range 0.025` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `8.95` | 0.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 200K AVAX` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `9.08` | 38,000.00 USD | 0.00 USD |
| `10-28 07:47` | `Range 0.025` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `9.07` | 0.00 USD | 0.00 USD |
| `10-28 06:13` | `Range 0.025` | `Divergence` | **`BEARISH`** | Rally without taker buying | `8.98` | 0.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -411,160.00 USD | -1,570.00 USD | **`DISTRIBUTION`** |
| `15m` | -587,760.00 USD | -592,340.00 USD | **`DISTRIBUTION`** |
| `30m` | -601,950.00 USD | -640,420.00 USD | **`DISTRIBUTION`** |
| `1h` | -699,000.00 USD | -361,130.00 USD | **`DISTRIBUTION`** |
| `2h` | -855,760.00 USD | 509,710.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,220,000.00 USD | -522,640.00 USD | **`DISTRIBUTION`** |
| `6h` | -1,320,000.00 USD | -1,350,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -955,110.00 USD | -159,440.00 USD | **`DISTRIBUTION`** |
| `12h` | -2,330,000.00 USD | -1,980,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -3,590,000.00 USD | -11,580,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,720,000.00 USD | -50,200,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,950,000.00 USD | -266,010,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-411.16K` | 15m=`-587.76K` | 1h=`-699.00K` | 24h=`-3.59M`
* Futures Capital Netflows: 5m=`-1.57K` | 15m=`-592.34K` | 1h=`-361.13K` | 24h=`-11.58M`
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
  * Execution Entry: `8.26` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.15` (Risk Distance: `0.1131` pts)
  * +2.5R Take Profit: `8.54`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.59` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.70` (Risk Distance: `0.1131` pts)
  * +2.5R Take Profit: `8.31`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.56`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
