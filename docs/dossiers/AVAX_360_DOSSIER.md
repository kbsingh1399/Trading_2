# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 14:41:48 IST` (`2026-10-30 09:11:48 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.46` | **Live Ask Quote**: `8.49` | **Mid Price**: `8.48`
- **Spread Points**: `3.00` | **Spread BPS**: `35.40 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.32` | VWAP Z-Score: `+0.70` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0625` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.36` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `7.78`
  * Upper +2.51σ Band: `8.78` | Lower -2.51σ Band: `7.87`
  * Upper +2.01σ Band: `8.69` | Lower -2.01σ Band: `7.96`
  * Upper +2.00σ Band: `8.69` | Lower -2.00σ Band: `7.96`
  * Upper +1.28σ Band: `8.56` | Lower -1.28σ Band: `8.09`
  * Upper +1.00σ Band: `8.50` | Lower -1.00σ Band: `8.14`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.48` | EMA-20=`8.48` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.48` (Slope: `+0.0000`) | EMA-100=`8.56`
  * Institutional Anchors: EMA-144=`8.61` | EMA-200=`8.66` (Slope: `-0.2094`) | EMA-233=`8.69`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.53` (Distance: `-0.48%`)
  * Point of Control (POC) = `8.32` (Distance: `+1.98%`)
  * Value Area Low (VAL) = `8.17` (Distance: `+3.87%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.70`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.53` | Low=`8.42`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.44` - `8.51`
  * Optimal Trade Entry (OTE 0.705): `8.49`
  * Structural Invalidation Anchor (0.786): `8.54`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.46` | `8.50` | `8.46` | `8.50` | `21,812` | 184,900.57 USD | 62,408.90 USD | `+33.75%` | -5,821,880.98 USD | `+0.73` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.50` | `8.50` | `8.48` | `8.48` | `16,697` | 141,692.51 USD | 38,143.67 USD | `+26.92%` | -5,783,737.31 USD | `+0.62` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `5m` | `8.48` | `8.49` | `8.48` | `8.49` | `8,664` | 73,502.12 USD | 14,664.43 USD | `+19.95%` | -5,769,072.88 USD | `+0.53` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.48` | `8.49` | `8.46` | `8.46` | `80,389` | 681,089.39 USD | -159,951.27 USD | `-23.48%` | -5,833,344.87 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.46` | `8.50` | `8.45` | `8.48` | `54,359` | 460,668.30 USD | 72,185.55 USD | `+15.67%` | -5,761,159.32 USD | `+0.09` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `8.48` | `8.49` | `8.48` | `8.49` | `8,664` | 73,502.12 USD | 14,664.43 USD | `+19.95%` | -5,746,494.89 USD | `-0.05` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `1h` | `8.63` | `8.63` | `8.48` | `8.50` | `671,897` | 5,750,861.25 USD | -1,429,699.87 USD | `-24.86%` | -5,391,829.51 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.50` | `8.52` | `8.45` | `8.48` | `439,030` | 3,723,872.89 USD | -159,958.73 USD | `-4.30%` | -5,551,788.23 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.48` | `8.49` | `8.48` | `8.49` | `8,648` | 73,366.30 USD | 14,528.62 USD | `+19.80%` | -5,537,259.61 USD | `+0.17` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.45` | `8.49` | `447,694` | 3,797,375.00 USD | -145,294.29 USD | `-3.83%` | -5,550,134.29 USD | `+0.53` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.45` | `8.49` | `447,694` | 3,797,375.00 USD | -145,294.29 USD | `-3.83%` | -5,550,134.29 USD | `+0.53` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.48`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `ASK` | `8.49` | `1.9200` | 16.31 USD | 16.31 USD | `1 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `8.49` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.49` | `0.00%` | `-` |
| `BID` | `8.49` | `181.7600` | 1,543.81 USD | 1,543.81 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `8.49` | `16.0000` | 135.89 USD | 1,679.71 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.49` | `42.2800` | 359.09 USD | 2,038.80 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.49` | `242.2100` | 2,057.09 USD | 4,095.89 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.49` | `181.7200` | 1,543.28 USD | 5,639.16 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.77 USD | 6,410.93 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.71 USD | 7,182.64 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.49` | `119.6800` | 1,016.23 USD | 8,198.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.63 USD | 8,970.49 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `90.8700` | 771.50 USD | 9,741.99 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.49` | `123.2900` | 1,046.72 USD | 10,788.71 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.49` | `1875.0500` | 15,918.42 USD | 26,707.13 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `8.49` | `706.7500` | 5,999.95 USD | 32,707.09 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.49` | `655.1300` | 5,561.40 USD | 38,268.48 USD | `4 orders` | `-0.06%` | `-` |
| `BID` | `8.49` | `120.0800` | 1,019.35 USD | 39,287.83 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.49` | `68.1500` | 578.51 USD | 39,866.34 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.43 USD | 40,637.78 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.37 USD | 41,409.15 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.49` | `1652.6700` | 14,026.21 USD | 55,435.36 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.49` | `90.8800` | 771.29 USD | 56,206.65 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `8.50` | `117.6300` | 999.94 USD | 47,541.87 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.50` | `90.8600` | 772.36 USD | 46,541.93 USD | `1 orders` | `+0.08%` | `-` |
| `ASK` | `8.50` | `5.8000` | 49.30 USD | 45,769.58 USD | `2 orders` | `+0.07%` | `-` |
| `ASK` | `8.50` | `1411.9400` | 12,000.93 USD | 45,720.28 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.50` | `91.7000` | 779.34 USD | 33,719.35 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.50` | `90.8600` | 772.19 USD | 32,940.01 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.50` | `49.2200` | 418.30 USD | 32,167.82 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.50` | `1176.8000` | 10,000.68 USD | 31,749.52 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.50` | `91.7000` | 779.25 USD | 21,748.84 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.50` | `56.6000` | 480.96 USD | 20,969.59 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.50` | `120.0800` | 1,020.38 USD | 20,488.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.50` | `91.7000` | 779.18 USD | 19,468.24 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.50` | `941.5600` | 8,000.44 USD | 18,689.06 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.50` | `200.0000` | 1,699.38 USD | 10,688.62 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.50` | `58.3900` | 496.12 USD | 8,989.24 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.50` | `122.4800` | 1,040.63 USD | 8,493.12 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.50` | `148.2200` | 1,259.28 USD | 7,452.50 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.50` | `20.8000` | 176.71 USD | 6,193.22 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.50` | `706.2800` | 6,000.20 USD | 6,016.51 USD | `1 orders` | `+0.02%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:32:27 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1489` | `0x7737...bf66` | `SHORT` | 1,456,235.38 USD | `171,568.06` | `7.43` | `8.49` | `111.75` | -180,690.36 USD | `-12.41%` | `10X Cross` |
| `1591` | `0xeadc...9d55` | `LONG` | 1,359,863.44 USD | `160,070.56` | `8.11` | `8.49` | `0.000000` | 62,225.86 USD | `+4.58%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `8.78` | 14,595.44 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 14.60K USD at 8.7827 USD [API] | `2026-10-29 10:57:18` |
| `ANNOUNCEMENT` | `INFO` | `8.79` | 5,023.36 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.02K USD at 8.7907 USD [API] | `2026-10-29 11:52:34` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,295.54 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 5.30K USD at 8.8074 USD [API] | `2026-10-29 13:20:34` |
| `ANNOUNCEMENT` | `INFO` | `8.80` | 7,335.21 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 7.34K USD at 8.8043 USD [API] | `2026-10-29 13:27:49` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,999.91 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 6.00K USD at 8.8138 USD [API] | `2026-10-29 14:01:56` |
| `ANNOUNCEMENT` | `INFO` | `8.81` | 5,668.07 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale SELL: 5.67K USD at 8.8149 USD [API] | `2026-10-29 14:01:46` |
| `ANNOUNCEMENT` | `INFO` | `8.82` | 9,104.31 USD | `-` | `NEWS_INTEL` | `-` | #AVAX Whale BUY: 9.10K USD at 8.8185 USD [API] | `2026-10-29 14:07:26` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.60%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.76%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.54%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.78%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.54%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.78%`)
  * 7D Horizon: Short MP=`9.28` (Vol: 462,400.00 USD, Dist: `+9.76%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.81%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `1.77` | 215.89 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.81` | 127.05 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.92` | 220.22 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.96` | 2,520.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `1.97` | 217.74 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.00` | 160.40 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.04` | 1,430.00 USD | 2,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.06` | 4,920.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.15` | 247.83 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.19` | 252.43 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.21` | 808.52 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.29` | 263.93 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.35` | 110.07 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.69` | 942.44 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.85` | 328.32 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.87` | 381.65 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.94` | 44,510.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.96` | 11,810.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `2.98` | 111.12 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.00` | 21,010.00 USD | 2,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.06` | 102.71 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.17` | 1,200.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.31` | 24,670.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.37` | 389.53 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.38` | 151.88 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.54` | 392.22 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.58` | 583.78 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.67` | 109.95 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.75` | 1,500.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.90` | 131.73 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `3.98` | 7,970.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.03` | 402.70 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.04` | 152.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.08` | 1,630.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.14` | 159.29 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.21` | 393.34 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.24` | 169.40 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.25` | 196.42 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.45` | 110.77 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.59` | 30,970.00 USD | 2,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.62` | 3,420.00 USD | 2,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.66` | 105.11 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 3,280.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.67` | 1,490.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.68` | 8,380.00 USD | 2,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.70` | 7,040.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.75` | 474.50 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.76` | 105.64 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.83` | 467.01 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.87` | 2,430.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.89` | 16,080.00 USD | 2,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.91` | 3,880.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.92` | 1,230.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.93` | 314.61 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.95` | 565.66 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 945.36 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.96` | 4,090.00 USD | 2,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `4.97` | 282.23 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 269.53 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.00` | 550.55 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.01` | 56,390.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.04` | 482.71 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.05` | 504.74 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 213.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.08` | 105.46 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.09` | 1,270.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.11` | 118.44 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 1,040.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.12` | 250.20 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.13` | 396.06 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.17` | 1,620.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.18` | 150.57 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.21` | 5,790.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.24` | 502.82 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 213.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.25` | 1,050.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.26` | 2,230.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.29` | 161,490.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.32` | 232.85 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.33` | 716.11 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.39` | 660.46 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.41` | 260.63 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 20,560.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.42` | 160,400.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.43` | 1,360.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.45` | 299.48 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.46` | 264.72 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.47` | 1,320.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.49` | 354.06 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.50` | 19,290.00 USD | 1,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 1,490.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.54` | 2,880.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.58` | 63,260.00 USD | 1,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.61` | 34,490.00 USD | 1,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.62` | 139.36 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.63` | 468.55 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.72` | 2,390.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.74` | 661.65 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 125.70 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.75` | 3,190.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.76` | 10,850.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.78` | 801.40 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.79` | 635.31 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.80` | 580.50 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.82` | 106.65 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.83` | 1,360.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.84` | 146.13 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.86` | 2,110.00 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.89` | 984.70 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.91` | 399.18 USD | 1,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 11,720.00 USD | 1,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.96` | 6,320.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `5.97` | 585.97 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.00` | 341.56 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.01` | 446.85 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.04` | 437.84 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.05` | 1,310.00 USD | 1,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.07` | 265.10 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.08` | 1,690.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.09` | 3,530.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 1,140.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.12` | 137.02 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.13` | 2,030.00 USD | 1,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.14` | 238.61 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.16` | 7,810.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.17` | 104.36 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.21` | 310.25 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.25` | 972.65 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.28` | 2,510.00 USD | 1,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.29` | 2,430.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 277.48 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.33` | 1,430.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.36` | 4,470.00 USD | 1,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.37` | 284,770.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 1,310.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.38` | 5,120.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.39` | 5,940.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 306.32 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.42` | 484.64 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.43` | 6,780.00 USD | 1,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.46` | 363,480.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.50` | 1,520.00 USD | 796,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 852.03 USD | 794,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.54` | 8,970.00 USD | 793,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.59` | 2,870.00 USD | 784,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 2,110.00 USD | 782,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.62` | 1,880.00 USD | 779,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.63` | 1,780.00 USD | 778,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.67` | 1,320.00 USD | 776,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.68` | 3,160.00 USD | 774,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 11,000.00 USD | 771,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.71` | 6,180.00 USD | 760,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.75` | 1,330.00 USD | 754,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.78` | 7,990.00 USD | 753,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 22,020.00 USD | 745,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.79` | 5,170.00 USD | 723,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.80` | 1,500.00 USD | 718,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.82` | 7,230.00 USD | 716,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.83` | 271.02 USD | 709,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.87` | 3,340.00 USD | 709,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 263.66 USD | 705,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.88` | 1,580.00 USD | 705,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.92` | 579.62 USD | 703,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.93` | 3,500.00 USD | 703,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.95` | 215.30 USD | 699,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 7,240.00 USD | 699,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.96` | 636.74 USD | 692,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `6.97` | 128,810.00 USD | 691,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.00` | 1,040.00 USD | 562,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.01` | 20,890.00 USD | 561,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.03` | 1,370.00 USD | 540,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.07` | 23,960.00 USD | 539,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 6,700.00 USD | 515,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.08` | 1,050.00 USD | 508,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.09` | 2,130.00 USD | 507,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.11` | 28,530.00 USD | 505,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.12` | 379.66 USD | 477,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.13` | 777.50 USD | 476,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.14` | 6,430,000.00 USD | 6,430,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 476,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 6,330,000.00 USD | 6,330,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 455,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 6,270,000.00 USD | 6,270,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 453,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.20` | 2,520.00 USD | 451,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 6,240,000.00 USD | 6,240,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 449,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 6,220,000.00 USD | 6,220,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 449,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 6,190,000.00 USD | 6,190,000.00 USD | 39,910.00 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 29,170.00 USD | 447,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 24,850.00 USD | 418,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 1,810.00 USD | 38.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.28` | 6,140,000.00 USD | 6,140,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 393,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 357,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.32` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 355,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 354,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 6,120,000.00 USD | 6,120,000.00 USD | 983.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 3,970.00 USD | 351,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 347,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 6,120,000.00 USD | 6,120,000.00 USD | 46,040.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 13,430.00 USD | 346,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 6,080,000.00 USD | 6,080,000.00 USD | 44,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.42` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 332,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 3,290.00 USD | 332,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 329,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 326,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 316,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 311,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 6,010,000.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 310,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.50` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 570.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 309,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 309,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 5,990,000.00 USD | 5,990,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 306,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 5,950,000.00 USD | 5,950,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 2,580.00 USD | 301,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 5,910,000.00 USD | 5,910,000.00 USD | 20,150.00 USD | 4,310.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 299,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 274,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.58` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 1,630.00 USD | 274,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,040,000.00 USD | 5,040,000.00 USD | 2,440.00 USD | 4,900.00 USD | 7,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,030,000.00 USD | 5,030,000.00 USD | 1,220.00 USD | 761.26 USD | 11,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 272,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,010,000.00 USD | 5,010,000.00 USD | 956.60 USD | 1,330.00 USD | 133.28 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 2,130.00 USD | 547.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 271,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,010,000.00 USD | 5,010,000.00 USD | 1,040.00 USD | 0.00 USD | 8,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 270,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,000,000.00 USD | 5,000,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 5,880,000.00 USD | 5,880,000.00 USD | 41,300.00 USD | 0.00 USD | 761.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 4,960,000.00 USD | 4,960,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 270,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 4,950,000.00 USD | 4,950,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 5,840,000.00 USD | 5,840,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 270,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 4,950,000.00 USD | 4,950,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 270,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 4,950,000.00 USD | 4,950,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 5,810,000.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 265,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 4,940,000.00 USD | 4,940,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 264,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 4,940,000.00 USD | 4,940,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 5,800,000.00 USD | 5,800,000.00 USD | 393.33 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 4,920,000.00 USD | 4,920,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 4,900,000.00 USD | 4,900,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 5,800,000.00 USD | 5,800,000.00 USD | 38,970.00 USD | 0.00 USD | 41,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 4,900,000.00 USD | 4,900,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 4,890,000.00 USD | 4,890,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 5,720,000.00 USD | 5,720,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 4,870,000.00 USD | 4,870,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 258,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 4,860,000.00 USD | 4,860,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 5,690,000.00 USD | 5,690,000.00 USD | 812.95 USD | 13,360.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 257,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 4,860,000.00 USD | 4,860,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 6,310.00 USD | 257,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 4,840,000.00 USD | 4,840,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 5,660,000.00 USD | 5,660,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 250,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,830,000.00 USD | 4,830,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 247,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 4,800,000.00 USD | 4,800,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 5,580,000.00 USD | 5,580,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 242,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,790,000.00 USD | 4,790,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 4,790,000.00 USD | 4,790,000.00 USD | 302.72 USD | 1,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 5,520,000.00 USD | 5,520,000.00 USD | 1,450.00 USD | 5,260.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 236,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,790,000.00 USD | 4,790,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 4,750,000.00 USD | 4,750,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 5,510,000.00 USD | 5,510,000.00 USD | 32,340.00 USD | 2,380.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 234,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,750,000.00 USD | 4,750,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,740,000.00 USD | 4,740,000.00 USD | 5,060.00 USD | 6,690.00 USD | 17,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 5,450,000.00 USD | 5,450,000.00 USD | 137,360.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 211,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,710,000.00 USD | 4,710,000.00 USD | 13,800.00 USD | 10,860.00 USD | 24,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 211,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,660,000.00 USD | 4,660,000.00 USD | 161,670.00 USD | 5,890.00 USD | 34,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 5,290,000.00 USD | 5,290,000.00 USD | 170,100.00 USD | 12,780.00 USD | 29,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,460,000.00 USD | 4,460,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 211,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,370,000.00 USD | 4,370,000.00 USD | 56,130.00 USD | 6,970.00 USD | 5,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 5,070,000.00 USD | 5,070,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 195,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,300,000.00 USD | 4,300,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,250,000.00 USD | 4,250,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 5,010,000.00 USD | 5,010,000.00 USD | 55,490.00 USD | 23,630.00 USD | 40,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 192,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,220,000.00 USD | 4,220,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 187,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,200,000.00 USD | 4,200,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 4,890,000.00 USD | 4,890,000.00 USD | 51,390.00 USD | 9,960.00 USD | 33,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 171,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,100,000.00 USD | 4,100,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 171,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 3,980,000.00 USD | 3,980,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 4,800,000.00 USD | 4,800,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 3,900,000.00 USD | 3,900,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 43,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 3,870,000.00 USD | 3,870,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 4,680,000.00 USD | 4,680,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 41,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,820,000.00 USD | 3,820,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 530.79 USD | 40,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,800,000.00 USD | 3,800,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 4,450,000.00 USD | 4,450,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,720,000.00 USD | 3,720,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,710,000.00 USD | 3,710,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 4,360,000.00 USD | 4,360,000.00 USD | 15,300.00 USD | 46,670.00 USD | 55,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 14,210.00 USD | 39,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,630,000.00 USD | 3,630,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,600,000.00 USD | 3,600,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 4,250,000.00 USD | 4,250,000.00 USD | 460,990.00 USD | 0.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 823.33 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,540,000.00 USD | 3,540,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,160,000.00 USD | 3,160,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 3,700,000.00 USD | 3,700,000.00 USD | 336,530.00 USD | 0.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 24,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 2,940,000.00 USD | 2,940,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 24,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 2,790,000.00 USD | 2,790,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 3,280,000.00 USD | 3,280,000.00 USD | 5,100.00 USD | 0.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 2,710,000.00 USD | 2,710,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 2,680,000.00 USD | 2,680,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 3,200,000.00 USD | 3,200,000.00 USD | 56,590.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 2,520,000.00 USD | 2,520,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 2,250,000.00 USD | 2,250,000.00 USD | 13,810.00 USD | 10,020.00 USD | 126,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 3,130,000.00 USD | 3,130,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,100,000.00 USD | 2,100,000.00 USD | 13,420.00 USD | 7,840.00 USD | 1,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 7,660.00 USD | 103,280.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 2,960,000.00 USD | 2,960,000.00 USD | 160,410.00 USD | 33,950.00 USD | 184,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 1,960,000.00 USD | 1,960,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,660.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.15` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,850,000.00 USD | 1,850,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 2,580,000.00 USD | 2,580,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,670,000.00 USD | 1,670,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 1,460,000.00 USD | 1,460,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 2,510,000.00 USD | 2,510,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,450,000.00 USD | 1,450,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 1,420,000.00 USD | 1,420,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 2,300,000.00 USD | 2,300,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,380,000.00 USD | 1,380,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 1,320,000.00 USD | 1,320,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 2,040,000.00 USD | 2,040,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 1,310,000.00 USD | 1,310,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,260,000.00 USD | 1,260,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 1,900,000.00 USD | 1,900,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,180,000.00 USD | 1,180,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,130,000.00 USD | 1,130,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 1,780,000.00 USD | 1,780,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,110,000.00 USD | 1,110,000.00 USD | 27,240.00 USD | 9,380.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,080,000.00 USD | 1,080,000.00 USD | 26,280.00 USD | 11,130.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 1,660,000.00 USD | 1,660,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,020,000.00 USD | 1,020,000.00 USD | 47,410.00 USD | 9,970.00 USD | 52,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 908,940.00 USD | 908,940.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 1,390,000.00 USD | 1,390,000.00 USD | 220,640.00 USD | 6,490.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 815,750.00 USD | 815,750.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 809,430.00 USD | 809,430.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 807,210.00 USD | 807,210.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 770,430.00 USD | 770,430.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 1,150,000.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 752,630.00 USD | 752,630.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 737,500.00 USD | 737,500.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 909,640.00 USD | 909,640.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 664,050.00 USD | 664,050.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 517,080.00 USD | 517,080.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 851,900.00 USD | 851,900.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 443,000.00 USD | 443,000.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 424,610.00 USD | 424,610.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 757,360.00 USD | 757,360.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 365,470.00 USD | 365,470.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 268,850.00 USD | 268,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 512,380.00 USD | 512,380.00 USD | 152,190.00 USD | 8,000.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 64,870.00 USD | 64,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.46` | 4,110.00 USD | 4,110.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 275,880.00 USD | 275,880.00 USD | 152,650.00 USD | 0.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 663.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 749.80 USD | 749.80 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 1,500.00 USD | 1,500.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 337,360.00 USD | 337,360.00 USD | 144,290.00 USD | 0.00 USD | 193,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.49` | 1,510.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 12.70 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 337,880.00 USD | 337,880.00 USD | 0.00 USD | 0.00 USD | 515.03 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 173,950.00 USD | 173,950.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 337,390.00 USD | 337,390.00 USD | 158,630.00 USD | 0.00 USD | 4,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 543,500.00 USD | 543,500.00 USD | 113,820.00 USD | 0.00 USD | 91,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 370,980.00 USD | 370,980.00 USD | 33,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 573,930.00 USD | 573,930.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 902,680.00 USD | 902,680.00 USD | 357,740.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 600,710.00 USD | 600,710.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 639,720.00 USD | 639,720.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,170,000.00 USD | 1,170,000.00 USD | 144,180.00 USD | 122,650.00 USD | 962.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 814,140.00 USD | 814,140.00 USD | 174,430.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 873,260.00 USD | 873,260.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,340,000.00 USD | 1,340,000.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 875,300.00 USD | 875,300.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 876,500.00 USD | 876,500.00 USD | 497.00 USD | 0.00 USD | 699.64 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,040,000.00 USD | 1,040,000.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,370,000.00 USD | 1,370,000.00 USD | 2,810.00 USD | 0.00 USD | 27,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,160,000.00 USD | 1,160,000.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,200,000.00 USD | 1,200,000.00 USD | 26,280.00 USD | 6,650.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,220,000.00 USD | 1,220,000.00 USD | 342.65 USD | 7,060.00 USD | 13,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,240,000.00 USD | 1,240,000.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 6,490.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,250,000.00 USD | 1,250,000.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,290,000.00 USD | 1,290,000.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 30,000.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 475.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,350,000.00 USD | 1,350,000.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,440,000.00 USD | 1,440,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,740,000.00 USD | 1,740,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,470,000.00 USD | 1,470,000.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,550,000.00 USD | 1,550,000.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 547.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,630,000.00 USD | 1,630,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,690,000.00 USD | 1,690,000.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,820,000.00 USD | 1,820,000.00 USD | 51,030.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,750,000.00 USD | 1,750,000.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,900,000.00 USD | 1,900,000.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 2,080,000.00 USD | 2,080,000.00 USD | 196,960.00 USD | 0.00 USD | 58,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,100,000.00 USD | 2,100,000.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,210,000.00 USD | 2,210,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 2,360,000.00 USD | 2,360,000.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,290,000.00 USD | 2,290,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,440,000.00 USD | 2,440,000.00 USD | 107,040.00 USD | 17,940.00 USD | 23,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 2,460,000.00 USD | 2,460,000.00 USD | 27,360.00 USD | 33,750.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,480,000.00 USD | 2,480,000.00 USD | 31,820.00 USD | 7,690.00 USD | 1,750.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,550,000.00 USD | 2,550,000.00 USD | 2,200.00 USD | 3,530.00 USD | 59,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 2,860,000.00 USD | 2,860,000.00 USD | 345,340.00 USD | 21,680.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,750,000.00 USD | 2,750,000.00 USD | 171,230.00 USD | 19,400.00 USD | 7,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,810,000.00 USD | 2,810,000.00 USD | 1,500.00 USD | 3,110.00 USD | 59,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,840,000.00 USD | 2,840,000.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,840,000.00 USD | 2,840,000.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 2,980,000.00 USD | 2,980,000.00 USD | 29,310.00 USD | 0.00 USD | 81,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,850,000.00 USD | 2,850,000.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,870,000.00 USD | 2,870,000.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,920,000.00 USD | 2,920,000.00 USD | 12,390.00 USD | 3,410.00 USD | 32,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.89` | 808.47 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.90` | 3,040,000.00 USD | 3,040,000.00 USD | 28,690.00 USD | 5,990.00 USD | 84,550.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 3,130,000.00 USD | 3,130,000.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.90` | 8,910.00 USD | 18,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.91` | 3,100,000.00 USD | 3,100,000.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 3,110,000.00 USD | 3,110,000.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 3,260,000.00 USD | 3,260,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 3,180,000.00 USD | 3,180,000.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 3,250,000.00 USD | 3,250,000.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 3,400,000.00 USD | 3,400,000.00 USD | 129,180.00 USD | 0.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 3,280,000.00 USD | 3,280,000.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 3,290,000.00 USD | 3,290,000.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 3,440,000.00 USD | 3,440,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 28,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 3,350,000.00 USD | 3,350,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,420,000.00 USD | 3,420,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 568,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,490,000.00 USD | 3,490,000.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 3,880,000.00 USD | 3,880,000.00 USD | 370,780.00 USD | 17,920.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,570,000.00 USD | 3,570,000.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,640,000.00 USD | 3,640,000.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 4,020,000.00 USD | 4,020,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,810,000.00 USD | 3,810,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,870,000.00 USD | 3,870,000.00 USD | 41,220.00 USD | 5,900.00 USD | 14,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 4,250,000.00 USD | 4,250,000.00 USD | 136,520.00 USD | 74,750.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,930,000.00 USD | 3,930,000.00 USD | 21,980.00 USD | 10,760.00 USD | 24,060.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 568,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 3,970,000.00 USD | 3,970,000.00 USD | 28,180.00 USD | 6,890.00 USD | 10,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 4,320,000.00 USD | 4,320,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.06` | 6,040.00 USD | 574,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.07` | 4,030,000.00 USD | 4,030,000.00 USD | 13,070.00 USD | 18,070.00 USD | 28,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 4,080,000.00 USD | 4,080,000.00 USD | 12,960.00 USD | 2,110.00 USD | 33,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 11,960.00 USD | 65,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 4,210,000.00 USD | 4,210,000.00 USD | 84,540.00 USD | 11,440.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 578,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 4,280,000.00 USD | 4,280,000.00 USD | 16,320.00 USD | 16,280.00 USD | 36,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 5,600,000.00 USD | 5,600,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,440,000.00 USD | 4,440,000.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,590,000.00 USD | 4,590,000.00 USD | 102,010.00 USD | 22,410.00 USD | 26,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 6,590,000.00 USD | 6,590,000.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,720,000.00 USD | 4,720,000.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,780,000.00 USD | 4,780,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 7,650,000.00 USD | 7,650,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 578,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,880,000.00 USD | 4,880,000.00 USD | 57,140.00 USD | 23,170.00 USD | 23,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 5,000,000.00 USD | 5,000,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 8,240,000.00 USD | 8,240,000.00 USD | 358,370.00 USD | 44,360.00 USD | 196,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 5,140,000.00 USD | 5,140,000.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 5,220,000.00 USD | 5,220,000.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 9,270,000.00 USD | 9,270,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,340,000.00 USD | 5,340,000.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,450,000.00 USD | 5,450,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 10,190,000.00 USD | 10,190,000.00 USD | 550,150.00 USD | 134,550.00 USD | 237,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,490,000.00 USD | 5,490,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,560,000.00 USD | 5,560,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 11,330,000.00 USD | 11,330,000.00 USD | 620,010.00 USD | 144,840.00 USD | 379,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,570,000.00 USD | 5,570,000.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,620,000.00 USD | 5,620,000.00 USD | 45,890.00 USD | 0.00 USD | 3,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 11,850,000.00 USD | 11,850,000.00 USD | 336,360.00 USD | 44,660.00 USD | 135,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,650,000.00 USD | 5,650,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,650,000.00 USD | 5,650,000.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 12,240,000.00 USD | 12,240,000.00 USD | 273,920.00 USD | 96,980.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,680,000.00 USD | 5,680,000.00 USD | 23,520.00 USD | 1,360.00 USD | 6,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,690,000.00 USD | 5,690,000.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 12,890,000.00 USD | 12,890,000.00 USD | 428,160.00 USD | 69,460.00 USD | 153,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,730,000.00 USD | 5,730,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 582,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,790,000.00 USD | 5,790,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 13,450,000.00 USD | 13,450,000.00 USD | 199,810.00 USD | 97,780.00 USD | 263,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,840,000.00 USD | 5,840,000.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,850,000.00 USD | 5,850,000.00 USD | 9,650.00 USD | 1,330.00 USD | 5,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 14,050,000.00 USD | 14,050,000.00 USD | 241,960.00 USD | 51,970.00 USD | 308,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,880,000.00 USD | 5,880,000.00 USD | 8,050.00 USD | 6,000.00 USD | 8,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,930,000.00 USD | 5,930,000.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 14,250,000.00 USD | 14,250,000.00 USD | 98,640.00 USD | 41,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 5,960,000.00 USD | 5,960,000.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 5,980,000.00 USD | 5,980,000.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 14,630,000.00 USD | 14,630,000.00 USD | 215,620.00 USD | 64,120.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 6,000,000.00 USD | 6,000,000.00 USD | 12,900.00 USD | 6,260.00 USD | 2,720.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 6,030,000.00 USD | 6,030,000.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 14,960,000.00 USD | 14,960,000.00 USD | 224,850.00 USD | 31,100.00 USD | 77,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 6,040,000.00 USD | 6,040,000.00 USD | 9,080.00 USD | 1,600.00 USD | 12.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 6,070,000.00 USD | 6,070,000.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 15,350,000.00 USD | 15,350,000.00 USD | 234,760.00 USD | 42,520.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 6,080,000.00 USD | 6,080,000.00 USD | 4,410.00 USD | 0.00 USD | 10,140.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 582,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.42` | 6,100,000.00 USD | 6,100,000.00 USD | 9,240.00 USD | 2,390.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.42` | 15,520,000.00 USD | 15,520,000.00 USD | 109,230.00 USD | 13,910.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.43` | 6,100,000.00 USD | 6,100,000.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.44` | 6,110,000.00 USD | 6,110,000.00 USD | 795.69 USD | 568.00 USD | 2,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 15,670,000.00 USD | 15,670,000.00 USD | 80,230.00 USD | 19,420.00 USD | 44,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.45` | 6,110,000.00 USD | 6,110,000.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.46` | 6,130,000.00 USD | 6,130,000.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 15,760,000.00 USD | 15,760,000.00 USD | 89,160.00 USD | 0.00 USD | 10,510.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.47` | 6,140,000.00 USD | 6,140,000.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.48` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 494.12 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 15,820,000.00 USD | 15,820,000.00 USD | 10,620.00 USD | 11,060.00 USD | 35,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.49` | 6,160,000.00 USD | 6,160,000.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 15,950,000.00 USD | 15,950,000.00 USD | 65,230.00 USD | 12,050.00 USD | 53,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 16,060,000.00 USD | 16,060,000.00 USD | 57,650.00 USD | 18,520.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 16,090,000.00 USD | 16,090,000.00 USD | 13,190.00 USD | 13,310.00 USD | 839.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 16,100,000.00 USD | 16,100,000.00 USD | 7,430.00 USD | 5,260.00 USD | 5,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 16,170,000.00 USD | 16,170,000.00 USD | 35,340.00 USD | 2,380.00 USD | 27,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 16,230,000.00 USD | 16,230,000.00 USD | 31,720.00 USD | 5,460.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 16,260,000.00 USD | 16,260,000.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.62` | 138.98 USD | 582,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.64` | 1,930.00 USD | 584,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.69` | 285.51 USD | 585,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.73` | 192.95 USD | 585,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `9.88` | 371.77 USD | 585,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.35` | 2,650.00 USD | 588,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.47` | 20,950.00 USD | 609,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.56` | 523.81 USD | 609,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.78` | 173.91 USD | 610,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.81` | 1,150.00 USD | 611,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `10.98` | 54,920.00 USD | 666,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.01` | 6,970.00 USD | 673,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.19` | 4,210.00 USD | 677,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.27` | 124,320.00 USD | 801,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.46` | 322.74 USD | 801,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.48` | 275.18 USD | 802,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.62` | 12,140.00 USD | 814,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.69` | 296,760.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.93` | 505.74 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `11.95` | 1,050.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.30` | 1,730.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.40` | 343.62 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `12.96` | 1,530.00 USD | 1,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.20` | 87,940.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.29` | 3,810.00 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.46` | 430.34 USD | 1,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.49` | 61,470.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.54` | 111.48 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `13.69` | 172.29 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.66` | 823.29 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `14.78` | 242.46 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.06` | 324.65 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.09` | 219.34 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.12` | 542.84 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.23` | 4,230.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.29` | 229.43 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.35` | 230.17 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.38` | 20,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.77` | 185.55 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `15.82` | 1,700.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.38` | 265,410.00 USD | 1,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.50` | 23,330.00 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.52` | 190.91 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.62` | 118.20 USD | 1,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.64` | 24,270.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.91` | 1,960.00 USD | 1,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `16.93` | 85,310.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `1.77` | 2,300,000.00 USD | 0.00 USD | 215.89 USD | `-79.06%` | `121.63` |
| `Live` | `Long` | `1.81` | 2,300,000.00 USD | 0.00 USD | 127.05 USD | `-78.59%` | `70.00` |
| `Live` | `Long` | `1.92` | 2,300,000.00 USD | 0.00 USD | 220.22 USD | `-77.41%` | `115.00` |
| `Live` | `Long` | `1.96` | 2,300,000.00 USD | 0.00 USD | 2,520.00 USD | `-76.94%` | `1,288.03` |
| `Live` | `Long` | `1.97` | 2,300,000.00 USD | 0.00 USD | 217.74 USD | `-76.82%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,300,000.00 USD | 0.00 USD | 160.40 USD | `-76.35%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,300,000.00 USD | 0.00 USD | 1,430.00 USD | `-75.99%` | `701.61` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.64%` | `2,382.76` |
| `Live` | `Long` | `2.15` | 2,290,000.00 USD | 0.00 USD | 247.83 USD | `-74.58%` | `115.00` |
| `Live` | `Long` | `2.19` | 2,290,000.00 USD | 0.00 USD | 252.43 USD | `-74.11%` | `115.00` |
| `Live` | `Long` | `2.21` | 2,290,000.00 USD | 0.00 USD | 808.52 USD | `-73.87%` | `365.02` |
| `Live` | `Long` | `2.29` | 2,290,000.00 USD | 0.00 USD | 263.93 USD | `-72.93%` | `115.00` |
| `Live` | `Long` | `2.35` | 2,290,000.00 USD | 0.00 USD | 110.07 USD | `-72.34%` | `46.94` |
| `Live` | `Long` | `2.69` | 2,290,000.00 USD | 0.00 USD | 942.44 USD | `-68.33%` | `351.00` |
| `Live` | `Long` | `2.85` | 2,290,000.00 USD | 0.00 USD | 328.32 USD | `-66.32%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 381.65 USD | `-66.20%` | `133.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.38%` | `15,165.76` |
| `Live` | `Long` | `2.96` | 2,240,000.00 USD | 0.00 USD | 11,810.00 USD | `-65.02%` | `3,981.48` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 111.12 USD | `-64.91%` | `37.35` |
| `Live` | `Long` | `3.00` | 2,230,000.00 USD | 0.00 USD | 21,010.00 USD | `-64.55%` | `6,990.57` |
| `Live` | `Long` | `3.06` | 2,210,000.00 USD | 0.00 USD | 102.71 USD | `-63.85%` | `33.51` |
| `Live` | `Long` | `3.17` | 2,210,000.00 USD | 0.00 USD | 1,200.00 USD | `-62.67%` | `377.71` |
| `Live` | `Long` | `3.31` | 2,210,000.00 USD | 0.00 USD | 24,670.00 USD | `-61.01%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.31%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.19%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.18%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 583.78 USD | `-57.71%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,180,000.00 USD | 0.00 USD | 109.95 USD | `-56.77%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,180,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.71%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,180,000.00 USD | 0.00 USD | 131.73 USD | `-54.05%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,180,000.00 USD | 0.00 USD | 7,970.00 USD | `-52.99%` | `2,000.00` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-52.52%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-52.28%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,170,000.00 USD | 0.00 USD | 1,630.00 USD | `-51.81%` | `400.00` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-51.11%` | `38.43` |
| `Live` | `Long` | `4.21` | 2,170,000.00 USD | 0.00 USD | 393.34 USD | `-50.28%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 169.40 USD | `-50.04%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,170,000.00 USD | 0.00 USD | 196.42 USD | `-49.93%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-47.57%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,170,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.80%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,140,000.00 USD | 0.00 USD | 3,420.00 USD | `-45.44%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.09%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.97%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.85%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,130,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.74%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.62%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,110,000.00 USD | 0.00 USD | 474.50 USD | `-44.03%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-43.79%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 467.01 USD | `-42.97%` | `96.59` |
| `Live` | `Long` | `4.87` | 2,110,000.00 USD | 0.00 USD | 2,430.00 USD | `-42.61%` | `500.00` |
| `Live` | `Long` | `4.89` | 2,110,000.00 USD | 0.00 USD | 16,080.00 USD | `-42.26%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.14%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,090,000.00 USD | 0.00 USD | 1,230.00 USD | `-42.02%` | `251.00` |
| `Live` | `Long` | `4.93` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-41.79%` | `63.75` |
| `Live` | `Long` | `4.95` | 2,090,000.00 USD | 0.00 USD | 565.66 USD | `-41.67%` | `114.39` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-41.55%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.43%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-41.31%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.08%` | `53.96` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 550.55 USD | `-40.96%` | `110.00` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.84%` | `11,243.48` |
| `Live` | `Long` | `5.04` | 2,030,000.00 USD | 0.00 USD | 482.71 USD | `-40.61%` | `95.87` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 504.74 USD | `-40.37%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 213.20 USD | `-40.13%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 105.46 USD | `-40.02%` | `20.74` |
| `Live` | `Long` | `5.09` | 2,020,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.90%` | `249.71` |
| `Live` | `Long` | `5.11` | 2,020,000.00 USD | 0.00 USD | 118.44 USD | `-39.78%` | `23.20` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 1,040.00 USD | `-39.66%` | `202.43` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-39.55%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-39.43%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.96%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,020,000.00 USD | 0.00 USD | 150.57 USD | `-38.84%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,020,000.00 USD | 0.00 USD | 5,790.00 USD | `-38.48%` | `1,110.70` |
| `Live` | `Long` | `5.24` | 2,010,000.00 USD | 0.00 USD | 502.82 USD | `-38.25%` | `96.05` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 213.00 USD | `-38.13%` | `40.61` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-38.01%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,010,000.00 USD | 0.00 USD | 2,230.00 USD | `-37.89%` | `423.54` |
| `Live` | `Long` | `5.29` | 2,010,000.00 USD | 0.00 USD | 161,490.00 USD | `-37.66%` | `30,556.43` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-37.30%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-37.19%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-36.36%` | `122.42` |
| `Live` | `Long` | `5.41` | 1,850,000.00 USD | 0.00 USD | 260.63 USD | `-36.24%` | `48.22` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,560.00 USD | `-36.12%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-36.01%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.89%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 299.48 USD | `-35.77%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-35.53%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.42%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-35.30%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.18%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 1,490.00 USD | `-34.71%` | `270.00` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-34.59%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.24%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,570,000.00 USD | 0.00 USD | 34,490.00 USD | `-33.88%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,540,000.00 USD | 0.00 USD | 139.36 USD | `-33.77%` | `24.82` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-33.53%` | `83.15` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.47%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,540,000.00 USD | 0.00 USD | 661.65 USD | `-32.35%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 125.70 USD | `-32.23%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 3,190.00 USD | `-32.11%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-32.00%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-31.88%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-31.64%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,520,000.00 USD | 0.00 USD | 580.50 USD | `-31.52%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 106.65 USD | `-31.41%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,520,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.29%` | `233.60` |
| `Live` | `Long` | `5.84` | 1,520,000.00 USD | 0.00 USD | 146.13 USD | `-31.05%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.93%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,520,000.00 USD | 0.00 USD | 984.70 USD | `-30.46%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,520,000.00 USD | 0.00 USD | 399.18 USD | `-30.34%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.75%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 6,320.00 USD | `-29.64%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,500,000.00 USD | 0.00 USD | 585.97 USD | `-29.52%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,500,000.00 USD | 0.00 USD | 341.56 USD | `-29.16%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,500,000.00 USD | 0.00 USD | 446.85 USD | `-29.05%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,500,000.00 USD | 0.00 USD | 437.84 USD | `-28.69%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,500,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.57%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,490,000.00 USD | 0.00 USD | 265.10 USD | `-28.46%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.34%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,530.00 USD | `-28.10%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.87%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 137.02 USD | `-27.75%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,490,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.63%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-27.51%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,480,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.40%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,480,000.00 USD | 0.00 USD | 104.36 USD | `-27.16%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,480,000.00 USD | 0.00 USD | 310.25 USD | `-26.81%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,480,000.00 USD | 0.00 USD | 972.65 USD | `-26.22%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,480,000.00 USD | 0.00 USD | 2,510.00 USD | `-25.98%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,470,000.00 USD | 0.00 USD | 2,430.00 USD | `-25.74%` | `386.46` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 277.48 USD | `-25.39%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 1,430.00 USD | `-25.27%` | `225.14` |
| `Live` | `Long` | `6.36` | 1,470,000.00 USD | 0.00 USD | 4,470.00 USD | `-25.04%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,460,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.92%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 1,310.00 USD | `-24.80%` | `204.92` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 5,120.00 USD | `-24.68%` | `801.31` |
| `Live` | `Long` | `6.39` | 1,170,000.00 USD | 0.00 USD | 5,940.00 USD | `-24.56%` | `928.10` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 306.32 USD | `-24.33%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 484.64 USD | `-24.21%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,170,000.00 USD | 0.00 USD | 6,780.00 USD | `-24.09%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,160,000.00 USD | 0.00 USD | 363,480.00 USD | `-23.74%` | `56,222.15` |
| `Live` | `Long` | `6.50` | 796,220.00 USD | 0.00 USD | 1,520.00 USD | `-23.27%` | `234.11` |
| `Live` | `Long` | `6.54` | 794,700.00 USD | 0.00 USD | 852.03 USD | `-22.91%` | `130.38` |
| `Live` | `Long` | `6.54` | 793,840.00 USD | 0.00 USD | 8,970.00 USD | `-22.79%` | `1,370.89` |
| `Live` | `Long` | `6.59` | 784,870.00 USD | 0.00 USD | 2,870.00 USD | `-22.20%` | `435.69` |
| `Live` | `Long` | `6.62` | 782,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.97%` | `318.57` |
| `Live` | `Long` | `6.62` | 779,890.00 USD | 0.00 USD | 1,880.00 USD | `-21.85%` | `283.49` |
| `Live` | `Long` | `6.63` | 778,010.00 USD | 0.00 USD | 1,780.00 USD | `-21.73%` | `268.08` |
| `Live` | `Long` | `6.67` | 776,230.00 USD | 0.00 USD | 1,320.00 USD | `-21.26%` | `198.12` |
| `Live` | `Long` | `6.68` | 774,910.00 USD | 0.00 USD | 3,160.00 USD | `-21.14%` | `472.28` |
| `Live` | `Long` | `6.71` | 771,750.00 USD | 0.00 USD | 11,000.00 USD | `-20.91%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 760,750.00 USD | 0.00 USD | 6,180.00 USD | `-20.79%` | `920.74` |
| `Live` | `Long` | `6.75` | 754,570.00 USD | 0.00 USD | 1,330.00 USD | `-20.32%` | `196.95` |
| `Live` | `Long` | `6.78` | 753,240.00 USD | 0.00 USD | 7,990.00 USD | `-20.08%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 745,240.00 USD | 0.00 USD | 22,020.00 USD | `-19.96%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 723,220.00 USD | 0.00 USD | 5,170.00 USD | `-19.85%` | `761.18` |
| `Live` | `Long` | `6.80` | 718,050.00 USD | 0.00 USD | 1,500.00 USD | `-19.73%` | `220.95` |
| `Live` | `Long` | `6.82` | 716,550.00 USD | 0.00 USD | 7,230.00 USD | `-19.61%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 709,310.00 USD | 0.00 USD | 271.02 USD | `-19.49%` | `39.71` |
| `Live` | `Long` | `6.87` | 709,040.00 USD | 0.00 USD | 3,340.00 USD | `-19.02%` | `486.46` |
| `Live` | `Long` | `6.88` | 705,700.00 USD | 0.00 USD | 263.66 USD | `-18.90%` | `38.35` |
| `Live` | `Long` | `6.88` | 705,440.00 USD | 0.00 USD | 1,580.00 USD | `-18.78%` | `229.18` |
| `Live` | `Long` | `6.92` | 703,860.00 USD | 0.00 USD | 579.62 USD | `-18.31%` | `83.70` |
| `Live` | `Long` | `6.93` | 703,280.00 USD | 0.00 USD | 3,500.00 USD | `-18.19%` | `504.07` |
| `Live` | `Long` | `6.95` | 699,790.00 USD | 0.00 USD | 215.30 USD | `-18.08%` | `31.00` |
| `Live` | `Long` | `6.96` | 699,570.00 USD | 0.00 USD | 7,240.00 USD | `-17.96%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 692,330.00 USD | 0.00 USD | 636.74 USD | `-17.84%` | `91.42` |
| `Live` | `Long` | `6.97` | 691,690.00 USD | 0.00 USD | 128,810.00 USD | `-17.72%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 562,880.00 USD | 0.00 USD | 1,040.00 USD | `-17.49%` | `149.32` |
| `Live` | `Long` | `7.01` | 561,840.00 USD | 0.00 USD | 20,890.00 USD | `-17.25%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 540,950.00 USD | 0.00 USD | 1,370.00 USD | `-17.13%` | `194.51` |
| `Live` | `Long` | `7.07` | 539,580.00 USD | 0.00 USD | 23,960.00 USD | `-16.66%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 515,620.00 USD | 0.00 USD | 6,700.00 USD | `-16.54%` | `947.44` |
| `Live` | `Long` | `7.08` | 508,920.00 USD | 0.00 USD | 1,050.00 USD | `-16.42%` | `148.63` |
| `Live` | `Long` | `7.09` | 507,870.00 USD | 0.00 USD | 2,130.00 USD | `-16.31%` | `300.00` |
| `Live` | `Long` | `7.11` | 505,740.00 USD | 0.00 USD | 28,530.00 USD | `-16.19%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 477,210.00 USD | 0.00 USD | 379.66 USD | `-16.07%` | `53.36` |
| `Live` | `Long` | `7.13` | 476,830.00 USD | 0.00 USD | 777.50 USD | `-15.84%` | `108.97` |
| `Live` | `Long` | `7.14` | 476,050.00 USD | 0.00 USD | 20,270.00 USD | `-15.72%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 455,780.00 USD | 0.00 USD | 2,380.00 USD | `-15.36%` | `331.12` |
| `Live` | `Long` | `7.18` | 453,410.00 USD | 0.00 USD | 1,440.00 USD | `-15.25%` | `200.95` |
| `Live` | `Long` | `7.20` | 451,960.00 USD | 0.00 USD | 2,520.00 USD | `-15.13%` | `350.58` |
| `Live` | `Long` | `7.21` | 449,440.00 USD | 0.00 USD | 322.94 USD | `-14.89%` | `44.76` |
| `Live` | `Long` | `7.24` | 449,120.00 USD | 0.00 USD | 1,480.00 USD | `-14.66%` | `205.21` |
| `Live` | `Long` | `7.25` | 447,630.00 USD | 0.00 USD | 29,170.00 USD | `-14.54%` | `4,025.65` |
| `Live` | `Long` | `7.25` | 418,470.00 USD | 0.00 USD | 24,850.00 USD | `-14.42%` | `3,424.57` |
| `Live` | `Long` | `7.29` | 393,620.00 USD | 0.00 USD | 36,420.00 USD | `-14.07%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 357,200.00 USD | 0.00 USD | 1,680.00 USD | `-13.95%` | `230.97` |
| `Live` | `Long` | `7.34` | 355,510.00 USD | 0.00 USD | 552.42 USD | `-13.36%` | `75.21` |
| `Live` | `Long` | `7.36` | 354,960.00 USD | 0.00 USD | 3,820.00 USD | `-13.24%` | `519.63` |
| `Live` | `Long` | `7.37` | 351,140.00 USD | 0.00 USD | 3,970.00 USD | `-13.12%` | `539.15` |
| `Live` | `Long` | `7.38` | 347,170.00 USD | 0.00 USD | 1,100.00 USD | `-13.00%` | `148.75` |
| `Live` | `Long` | `7.38` | 346,070.00 USD | 0.00 USD | 13,430.00 USD | `-12.89%` | `1,817.92` |
| `Live` | `Long` | `7.42` | 332,650.00 USD | 0.00 USD | 147.61 USD | `-12.41%` | `19.88` |
| `Live` | `Long` | `7.43` | 332,500.00 USD | 0.00 USD | 3,290.00 USD | `-12.30%` | `442.38` |
| `Live` | `Long` | `7.45` | 329,210.00 USD | 0.00 USD | 2,410.00 USD | `-12.18%` | `324.35` |
| `Live` | `Long` | `7.46` | 326,790.00 USD | 0.00 USD | 10,390.00 USD | `-12.06%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 316,410.00 USD | 0.00 USD | 4,590.00 USD | `-11.94%` | `614.36` |
| `Live` | `Long` | `7.47` | 311,820.00 USD | 0.00 USD | 1,120.00 USD | `-11.82%` | `149.52` |
| `Live` | `Long` | `7.50` | 310,700.00 USD | 0.00 USD | 962.81 USD | `-11.59%` | `128.46` |
| `Live` | `Long` | `7.50` | 309,740.00 USD | 0.00 USD | 421.78 USD | `-11.47%` | `56.20` |
| `Live` | `Long` | `7.51` | 309,320.00 USD | 0.00 USD | 1,710.00 USD | `-11.35%` | `228.21` |
| `Live` | `Long` | `7.53` | 307,600.00 USD | 0.00 USD | 1,570.00 USD | `-11.23%` | `208.52` |
| `Live` | `Long` | `7.54` | 306,030.00 USD | 0.00 USD | 4,210.00 USD | `-11.12%` | `559.01` |
| `Live` | `Long` | `7.55` | 301,820.00 USD | 0.00 USD | 2,580.00 USD | `-10.88%` | `341.09` |
| `Live` | `Long` | `7.57` | 299,240.00 USD | 0.00 USD | 25,060.00 USD | `-10.76%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 274,190.00 USD | 0.00 USD | 118.25 USD | `-10.64%` | `15.61` |
| `Live` | `Long` | `7.59` | 274,070.00 USD | 0.00 USD | 1,630.00 USD | `-10.41%` | `214.22` |
| `Live` | `Long` | `7.62` | 272,440.00 USD | 0.00 USD | 754.04 USD | `-10.17%` | `99.02` |
| `Live` | `Long` | `7.62` | 271,690.00 USD | 0.00 USD | 787.51 USD | `-10.05%` | `103.28` |
| `Live` | `Long` | `7.63` | 270,900.00 USD | 0.00 USD | 378.93 USD | `-9.94%` | `49.63` |
| `Live` | `Long` | `7.66` | 270,520.00 USD | 0.00 USD | 135.42 USD | `-9.70%` | `17.69` |
| `Live` | `Long` | `7.67` | 270,390.00 USD | 0.00 USD | 256.09 USD | `-9.58%` | `33.41` |
| `Live` | `Long` | `7.67` | 270,130.00 USD | 0.00 USD | 4,480.00 USD | `-9.47%` | `583.63` |
| `Live` | `Long` | `7.68` | 265,650.00 USD | 0.00 USD | 739.30 USD | `-9.35%` | `96.20` |
| `Live` | `Long` | `7.70` | 264,910.00 USD | 0.00 USD | 6,690.00 USD | `-9.23%` | `869.22` |
| `Live` | `Long` | `7.75` | 258,220.00 USD | 0.00 USD | 500.12 USD | `-8.52%` | `64.49` |
| `Live` | `Long` | `7.76` | 257,720.00 USD | 0.00 USD | 455.73 USD | `-8.40%` | `58.69` |
| `Live` | `Long` | `7.78` | 257,270.00 USD | 0.00 USD | 6,310.00 USD | `-8.29%` | `812.08` |
| `Live` | `Long` | `7.79` | 250,950.00 USD | 0.00 USD | 3,750.00 USD | `-8.17%` | `481.06` |
| `Live` | `Long` | `7.79` | 247,210.00 USD | 0.00 USD | 4,480.00 USD | `-8.05%` | `574.50` |
| `Live` | `Long` | `7.80` | 242,730.00 USD | 0.00 USD | 6,380.00 USD | `-7.93%` | `817.06` |
| `Live` | `Long` | `7.83` | 236,350.00 USD | 0.00 USD | 1,940.00 USD | `-7.70%` | `247.42` |
| `Live` | `Long` | `7.84` | 234,420.00 USD | 0.00 USD | 22,560.00 USD | `-7.46%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 211,850.00 USD | 0.00 USD | 233.83 USD | `-7.22%` | `29.73` |
| `Live` | `Long` | `7.88` | 211,620.00 USD | 0.00 USD | 555.19 USD | `-7.11%` | `70.50` |
| `Live` | `Long` | `7.89` | 211,070.00 USD | 0.00 USD | 15,880.00 USD | `-6.87%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 195,180.00 USD | 0.00 USD | 2,930.00 USD | `-6.75%` | `370.74` |
| `Live` | `Long` | `7.92` | 192,250.00 USD | 0.00 USD | 4,600.00 USD | `-6.52%` | `580.78` |
| `Live` | `Long` | `7.93` | 187,650.00 USD | 0.00 USD | 16,340.00 USD | `-6.40%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 171,300.00 USD | 0.00 USD | 141.74 USD | `-6.28%` | `17.84` |
| `Live` | `Long` | `7.96` | 171,160.00 USD | 0.00 USD | 127,900.00 USD | `-6.16%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 43,260.00 USD | 0.00 USD | 1,580.00 USD | `-5.93%` | `198.26` |
| `Live` | `Long` | `7.99` | 41,680.00 USD | 0.00 USD | 1,280.00 USD | `-5.81%` | `160.68` |
| `Live` | `Long` | `8.00` | 40,400.00 USD | 0.00 USD | 530.79 USD | `-5.69%` | `66.39` |
| `Live` | `Long` | `8.03` | 39,870.00 USD | 0.00 USD | 14,210.00 USD | `-5.34%` | `1,770.35` |
| `Live` | `Long` | `8.04` | 25,660.00 USD | 0.00 USD | 823.33 USD | `-5.10%` | `102.34` |
| `Live` | `Short` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | `-4.98%` | `33.00` |
| `Live` | `Long` | `8.06` | 24,830.00 USD | 0.00 USD | 439.54 USD | `-4.86%` | `54.50` |
| `Live` | `Long` | `8.07` | 24,400.00 USD | 0.00 USD | 21,710.00 USD | `-4.75%` | `2,688.93` |
| `Live` | `Long` | `8.12` | 2,680.00 USD | 0.00 USD | 738.14 USD | `-4.27%` | `90.96` |
| `Live` | `Long` | `8.12` | 1,940.00 USD | 0.00 USD | 521.62 USD | `-4.16%` | `64.20` |
| `Live` | `Long` | `8.15` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | `-3.80%` | `174.44` |
| `Live` | `Short` | `8.69` | 475.12 USD | 209.31 USD | 0.00 USD | `+2.45%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,480.00 USD | 6,000.00 USD | 0.00 USD | `+4.10%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,640.00 USD | 1,160.00 USD | 0.00 USD | `+4.57%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,330.00 USD | 691.70 USD | 0.00 USD | `+4.81%` | `77.85` |
| `Live` | `Short` | `8.89` | 9,140.00 USD | 808.47 USD | 0.00 USD | `+4.93%` | `90.89` |
| `Live` | `Short` | `8.90` | 18,040.00 USD | 8,910.00 USD | 0.00 USD | `+5.04%` | `1,000.45` |
| `Live` | `Short` | `8.97` | 28,520.00 USD | 10,480.00 USD | 0.00 USD | `+5.87%` | `1,167.41` |
| `Live` | `Short` | `8.99` | 568,230.00 USD | 539,710.00 USD | 0.00 USD | `+6.11%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 568,440.00 USD | 213.70 USD | 0.00 USD | `+6.81%` | `23.60` |
| `Live` | `Short` | `9.06` | 574,480.00 USD | 6,040.00 USD | 0.00 USD | `+6.93%` | `666.20` |
| `Live` | `Short` | `9.10` | 578,370.00 USD | 3,890.00 USD | 0.00 USD | `+7.29%` | `427.53` |
| `Live` | `Short` | `9.14` | 578,550.00 USD | 180.80 USD | 0.00 USD | `+7.88%` | `19.77` |
| `Live` | `Short` | `9.29` | 582,410.00 USD | 3,860.00 USD | 0.00 USD | `+9.64%` | `415.00` |
| `Live` | `Short` | `9.41` | 582,850.00 USD | 440.06 USD | 0.00 USD | `+11.06%` | `46.74` |
| `Live` | `Short` | `9.62` | 582,990.00 USD | 138.98 USD | 0.00 USD | `+13.54%` | `14.44` |
| `Live` | `Short` | `9.64` | 584,920.00 USD | 1,930.00 USD | 0.00 USD | `+13.77%` | `200.61` |
| `Live` | `Short` | `9.69` | 585,210.00 USD | 285.51 USD | 0.00 USD | `+14.24%` | `29.48` |
| `Live` | `Short` | `9.73` | 585,400.00 USD | 192.95 USD | 0.00 USD | `+14.83%` | `19.82` |
| `Live` | `Short` | `9.88` | 585,770.00 USD | 371.77 USD | 0.00 USD | `+16.60%` | `37.61` |
| `Live` | `Short` | `10.35` | 588,430.00 USD | 2,650.00 USD | 0.00 USD | `+22.03%` | `256.58` |
| `Live` | `Short` | `10.47` | 609,380.00 USD | 20,950.00 USD | 0.00 USD | `+23.56%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 609,900.00 USD | 523.81 USD | 0.00 USD | `+24.63%` | `49.58` |
| `Live` | `Short` | `10.78` | 610,080.00 USD | 173.91 USD | 0.00 USD | `+27.10%` | `16.14` |
| `Live` | `Short` | `10.81` | 611,220.00 USD | 1,150.00 USD | 0.00 USD | `+27.57%` | `106.17` |
| `Live` | `Short` | `10.98` | 666,150.00 USD | 54,920.00 USD | 0.00 USD | `+29.58%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 673,120.00 USD | 6,970.00 USD | 0.00 USD | `+29.82%` | `633.00` |
| `Live` | `Short` | `11.19` | 677,330.00 USD | 4,210.00 USD | 0.00 USD | `+31.94%` | `376.48` |
| `Live` | `Short` | `11.27` | 801,650.00 USD | 124,320.00 USD | 0.00 USD | `+32.88%` | `11,035.87` |
| `Live` | `Short` | `11.46` | 801,970.00 USD | 322.74 USD | 0.00 USD | `+35.24%` | `28.15` |
| `Live` | `Short` | `11.48` | 802,240.00 USD | 275.18 USD | 0.00 USD | `+35.48%` | `23.96` |
| `Live` | `Short` | `11.62` | 814,380.00 USD | 12,140.00 USD | 0.00 USD | `+37.13%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,110,000.00 USD | 296,760.00 USD | 0.00 USD | `+37.84%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,110,000.00 USD | 505.74 USD | 0.00 USD | `+40.67%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,110,000.00 USD | 1,050.00 USD | 0.00 USD | `+40.90%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+45.15%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,110,000.00 USD | 343.62 USD | 0.00 USD | `+46.33%` | `27.70` |
| `Live` | `Short` | `12.96` | 1,120,000.00 USD | 1,530.00 USD | 0.00 USD | `+52.82%` | `117.87` |
| `Live` | `Short` | `13.20` | 1,200,000.00 USD | 87,940.00 USD | 0.00 USD | `+55.65%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,210,000.00 USD | 3,810.00 USD | 0.00 USD | `+56.83%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,210,000.00 USD | 430.34 USD | 0.00 USD | `+58.83%` | `31.96` |
| `Live` | `Short` | `13.49` | 1,270,000.00 USD | 61,470.00 USD | 0.00 USD | `+59.19%` | `4,555.14` |
| `Live` | `Short` | `13.54` | 1,270,000.00 USD | 111.48 USD | 0.00 USD | `+59.78%` | `8.23` |
| `Live` | `Short` | `13.69` | 1,270,000.00 USD | 172.29 USD | 0.00 USD | `+61.43%` | `12.59` |
| `Live` | `Short` | `14.66` | 1,270,000.00 USD | 823.29 USD | 0.00 USD | `+72.99%` | `56.14` |
| `Live` | `Short` | `14.78` | 1,270,000.00 USD | 242.46 USD | 0.00 USD | `+74.29%` | `16.41` |
| `Live` | `Short` | `15.06` | 1,270,000.00 USD | 324.65 USD | 0.00 USD | `+77.71%` | `21.55` |
| `Live` | `Short` | `15.09` | 1,270,000.00 USD | 219.34 USD | 0.00 USD | `+77.94%` | `14.54` |
| `Live` | `Short` | `15.12` | 1,270,000.00 USD | 542.84 USD | 0.00 USD | `+78.42%` | `35.89` |
| `Live` | `Short` | `15.23` | 1,280,000.00 USD | 4,230.00 USD | 0.00 USD | `+79.71%` | `277.54` |
| `Live` | `Short` | `15.29` | 1,280,000.00 USD | 229.43 USD | 0.00 USD | `+80.42%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,280,000.00 USD | 230.17 USD | 0.00 USD | `+81.01%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,300,000.00 USD | 20,000.00 USD | 0.00 USD | `+81.48%` | `1,300.00` |
| `Live` | `Short` | `15.77` | 1,300,000.00 USD | 185.55 USD | 0.00 USD | `+85.97%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,300,000.00 USD | 1,700.00 USD | 0.00 USD | `+86.67%` | `107.48` |
| `Live` | `Short` | `16.38` | 1,560,000.00 USD | 265,410.00 USD | 0.00 USD | `+93.16%` | `16,208.00` |
| `Live` | `Short` | `16.50` | 1,590,000.00 USD | 23,330.00 USD | 0.00 USD | `+94.58%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,590,000.00 USD | 190.91 USD | 0.00 USD | `+94.81%` | `11.56` |
| `Live` | `Short` | `16.62` | 1,590,000.00 USD | 118.20 USD | 0.00 USD | `+96.11%` | `7.11` |
| `Live` | `Short` | `16.64` | 1,610,000.00 USD | 24,270.00 USD | 0.00 USD | `+96.23%` | `1,459.25` |
| `Live` | `Short` | `16.91` | 1,610,000.00 USD | 1,960.00 USD | 0.00 USD | `+99.41%` | `115.73` |
| `Live` | `Short` | `16.93` | 1,700,000.00 USD | 85,310.00 USD | 0.00 USD | `+99.77%` | `5,037.66` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 371,260.00 USD | 0.00 USD | 611.73 USD | `-72.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 370,650.00 USD | 0.00 USD | 793.75 USD | `-52.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 369,860.00 USD | 0.00 USD | 67,970.00 USD | `-40.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 301,890.00 USD | 0.00 USD | 205.30 USD | `-37.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 301,690.00 USD | 0.00 USD | 465.42 USD | `-35.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 301,220.00 USD | 0.00 USD | 349.35 USD | `-35.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 300,870.00 USD | 0.00 USD | 1,020.00 USD | `-34.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 299,860.00 USD | 0.00 USD | 1,330.00 USD | `-31.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 298,530.00 USD | 0.00 USD | 493.50 USD | `-29.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 298,030.00 USD | 0.00 USD | 100.98 USD | `-29.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 297,930.00 USD | 0.00 USD | 500.70 USD | `-29.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 297,430.00 USD | 0.00 USD | 4,160.00 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 293,280.00 USD | 0.00 USD | 6,500.00 USD | `-27.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 286,770.00 USD | 0.00 USD | 906.18 USD | `-26.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 285,870.00 USD | 0.00 USD | 127.35 USD | `-26.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 285,740.00 USD | 0.00 USD | 864.38 USD | `-25.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 284,880.00 USD | 0.00 USD | 130.10 USD | `-23.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 284,750.00 USD | 0.00 USD | 4,340.00 USD | `-22.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 280,410.00 USD | 0.00 USD | 5,520.00 USD | `-20.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 274,880.00 USD | 0.00 USD | 203.67 USD | `-20.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 274,680.00 USD | 0.00 USD | 296.34 USD | `-20.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 274,380.00 USD | 0.00 USD | 921.19 USD | `-20.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 273,460.00 USD | 0.00 USD | 709.98 USD | `-18.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 272,750.00 USD | 0.00 USD | 4,630.00 USD | `-18.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 268,130.00 USD | 0.00 USD | 691.50 USD | `-18.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 267,440.00 USD | 0.00 USD | 262.44 USD | `-17.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 267,170.00 USD | 0.00 USD | 24,350.00 USD | `-17.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 242,820.00 USD | 0.00 USD | 653.69 USD | `-17.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 242,170.00 USD | 0.00 USD | 187.79 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 241,980.00 USD | 0.00 USD | 6,790.00 USD | `-15.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 235,190.00 USD | 0.00 USD | 4,960.00 USD | `-15.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 230,230.00 USD | 0.00 USD | 7,210.00 USD | `-15.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 223,020.00 USD | 0.00 USD | 282.74 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 222,740.00 USD | 0.00 USD | 603.44 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 222,140.00 USD | 0.00 USD | 464.61 USD | `-14.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 221,670.00 USD | 0.00 USD | 2,090.00 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 219,580.00 USD | 0.00 USD | 129.58 USD | `-13.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 219,450.00 USD | 0.00 USD | 114.65 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 219,340.00 USD | 0.00 USD | 702.75 USD | `-12.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 218,630.00 USD | 0.00 USD | 4,630.00 USD | `-12.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 214,000.00 USD | 0.00 USD | 199.39 USD | `-11.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 213,800.00 USD | 0.00 USD | 6,270.00 USD | `-11.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 207,530.00 USD | 0.00 USD | 37,420.00 USD | `-11.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 170,110.00 USD | 0.00 USD | 2,120.00 USD | `-11.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 167,990.00 USD | 0.00 USD | 799.83 USD | `-11.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 167,190.00 USD | 0.00 USD | 820.44 USD | `-11.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 166,370.00 USD | 0.00 USD | 218.24 USD | `-10.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 166,150.00 USD | 0.00 USD | 113.78 USD | `-10.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 166,040.00 USD | 0.00 USD | 152.10 USD | `-10.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 165,880.00 USD | 0.00 USD | 297.59 USD | `-10.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 165,590.00 USD | 0.00 USD | 528.88 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 165,060.00 USD | 0.00 USD | 360.13 USD | `-9.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 164,700.00 USD | 0.00 USD | 578.04 USD | `-8.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 164,120.00 USD | 0.00 USD | 424.05 USD | `-8.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 163,700.00 USD | 0.00 USD | 1,170.00 USD | `-7.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 162,520.00 USD | 0.00 USD | 3,940.00 USD | `-7.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 158,590.00 USD | 0.00 USD | 154.70 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 158,430.00 USD | 0.00 USD | 115.23 USD | `-7.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 158,320.00 USD | 0.00 USD | 183.33 USD | `-7.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 158,130.00 USD | 0.00 USD | 1,890.00 USD | `-6.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 156,240.00 USD | 0.00 USD | 6,840.00 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 149,400.00 USD | 0.00 USD | 5,710.00 USD | `-6.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 143,690.00 USD | 0.00 USD | 1,590.00 USD | `-6.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 142,110.00 USD | 0.00 USD | 898.42 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 141,210.00 USD | 0.00 USD | 7,960.00 USD | `-6.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 133,250.00 USD | 0.00 USD | 246.52 USD | `-6.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 133,010.00 USD | 0.00 USD | 1,440.00 USD | `-5.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 131,570.00 USD | 0.00 USD | 435.73 USD | `-5.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 131,130.00 USD | 0.00 USD | 4,210.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 126,920.00 USD | 0.00 USD | 123.58 USD | `-5.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 126,800.00 USD | 0.00 USD | 796.62 USD | `-5.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 126,000.00 USD | 0.00 USD | 152.56 USD | `-4.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 125,850.00 USD | 0.00 USD | 2,730.00 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 123,120.00 USD | 0.00 USD | 121.69 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 123,000.00 USD | 0.00 USD | 5,230.00 USD | `-4.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 117,770.00 USD | 0.00 USD | 477.36 USD | `-4.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 117,290.00 USD | 0.00 USD | 924.78 USD | `-4.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 116,370.00 USD | 0.00 USD | 744.88 USD | `-4.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 115,620.00 USD | 0.00 USD | 6,500.00 USD | `-4.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 109,120.00 USD | 0.00 USD | 884.60 USD | `-4.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 108,240.00 USD | 0.00 USD | 5,550.00 USD | `-3.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 102,680.00 USD | 0.00 USD | 1,420.00 USD | `-3.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 101,260.00 USD | 0.00 USD | 3,080.00 USD | `-3.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 98,180.00 USD | 0.00 USD | 520.75 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 97,660.00 USD | 0.00 USD | 3,020.00 USD | `-3.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 94,630.00 USD | 0.00 USD | 141.04 USD | `-3.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 94,490.00 USD | 0.00 USD | 22,560.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 71,930.00 USD | 0.00 USD | 515.66 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 71,410.00 USD | 0.00 USD | 139.74 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 71,270.00 USD | 0.00 USD | 490.15 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 70,780.00 USD | 0.00 USD | 197.96 USD | `-2.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 70,580.00 USD | 0.00 USD | 9,110.00 USD | `-2.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 61,470.00 USD | 0.00 USD | 535.65 USD | `-2.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 60,940.00 USD | 0.00 USD | 734.99 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 60,200.00 USD | 0.00 USD | 2,360.00 USD | `-2.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 57,840.00 USD | 0.00 USD | 311.97 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 57,530.00 USD | 0.00 USD | 15,070.00 USD | `-2.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 42,450.00 USD | 0.00 USD | 245.13 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 42,210.00 USD | 0.00 USD | 1,690.00 USD | `-1.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 40,520.00 USD | 0.00 USD | 408.58 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 40,110.00 USD | 0.00 USD | 808.63 USD | `-1.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 39,300.00 USD | 0.00 USD | 4,070.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 35,230.00 USD | 0.00 USD | 24,090.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 11,140.00 USD | 0.00 USD | 503.59 USD | `-1.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 10,640.00 USD | 0.00 USD | 419.25 USD | `-1.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 10,220.00 USD | 0.00 USD | 1,970.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 8,250.00 USD | 0.00 USD | 4,240.00 USD | `-0.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 4,010.00 USD | 0.00 USD | 314.81 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 3,700.00 USD | 0.00 USD | 1,880.00 USD | `-0.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 1,810.00 USD | 0.00 USD | 195.52 USD | `-0.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 1,620.00 USD | 0.00 USD | 138.24 USD | `-0.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 1,480.00 USD | 0.00 USD | 710.81 USD | `-0.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.47` | 769.61 USD | 0.00 USD | 769.61 USD | `-0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 777.14 USD | 777.14 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 1,190.00 USD | 408.78 USD | 0.00 USD | `+0.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 18,200.00 USD | 17,010.00 USD | 0.00 USD | `+0.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 18,600.00 USD | 408.55 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 19,730.00 USD | 1,130.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 20,020.00 USD | 290.10 USD | 0.00 USD | `+0.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 24,430.00 USD | 4,400.00 USD | 0.00 USD | `+0.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 34,410.00 USD | 9,990.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 36,010.00 USD | 1,600.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 36,580.00 USD | 566.55 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 36,720.00 USD | 143.28 USD | 0.00 USD | `+1.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 38,910.00 USD | 2,180.00 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 39,660.00 USD | 751.56 USD | 0.00 USD | `+1.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 43,860.00 USD | 4,200.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 43,960.00 USD | 107.47 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 44,170.00 USD | 201.97 USD | 0.00 USD | `+1.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 46,040.00 USD | 1,880.00 USD | 0.00 USD | `+1.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 46,720.00 USD | 673.62 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 46,920.00 USD | 200.85 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 47,100.00 USD | 176.62 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 48,090.00 USD | 990.09 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 48,510.00 USD | 420.32 USD | 0.00 USD | `+2.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 49,080.00 USD | 575.14 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 49,480.00 USD | 399.67 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 49,900.00 USD | 421.85 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 50,240.00 USD | 333.07 USD | 0.00 USD | `+3.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 54,610.00 USD | 4,370.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 58,350.00 USD | 3,740.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 58,520.00 USD | 173.28 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 58,740.00 USD | 215.16 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 59,130.00 USD | 388.12 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 59,840.00 USD | 711.78 USD | 0.00 USD | `+3.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 79,640.00 USD | 19,810.00 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 81,680.00 USD | 2,030.00 USD | 0.00 USD | `+4.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 81,920.00 USD | 243.40 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 82,090.00 USD | 168.05 USD | 0.00 USD | `+4.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 82,430.00 USD | 339.94 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 82,590.00 USD | 163.91 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 82,700.00 USD | 110.58 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 83,560.00 USD | 860.96 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 85,500.00 USD | 1,930.00 USD | 0.00 USD | `+4.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 86,290.00 USD | 788.72 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 88,090.00 USD | 1,800.00 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 88,250.00 USD | 163.33 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 89,030.00 USD | 782.17 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 89,260.00 USD | 223.62 USD | 0.00 USD | `+5.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 626,570.00 USD | 537,310.00 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 626,970.00 USD | 401.63 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 942,120.00 USD | 315,150.00 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 942,460.00 USD | 338.30 USD | 0.00 USD | `+6.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 942,720.00 USD | 260.96 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 944,100.00 USD | 1,380.00 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 945,180.00 USD | 1,090.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 945,800.00 USD | 616.37 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 945,900.00 USD | 102.03 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 946,360.00 USD | 453.84 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 946,520.00 USD | 160.99 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 946,730.00 USD | 215.98 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 948,240.00 USD | 1,510.00 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 948,690.00 USD | 451.48 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 948,830.00 USD | 139.58 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 950,130.00 USD | 1,290.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 950,290.00 USD | 166.53 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 952,290.00 USD | 2,000.00 USD | 0.00 USD | `+7.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,350,000.00 USD | 394,210.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,350,000.00 USD | 119.24 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,350,000.00 USD | 3,020.00 USD | 0.00 USD | `+8.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,350,000.00 USD | 131.87 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,350,000.00 USD | 149.17 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,350,000.00 USD | 2,220.00 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,580,000.00 USD | 231,380.00 USD | 0.00 USD | `+9.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,590,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,590,000.00 USD | 434.45 USD | 0.00 USD | `+9.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,600,000.00 USD | 18,610.00 USD | 0.00 USD | `+9.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,600,000.00 USD | 166.83 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,610,000.00 USD | 674.29 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,610,000.00 USD | 101.58 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,610,000.00 USD | 109.36 USD | 0.00 USD | `+10.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,610,000.00 USD | 116.69 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,610,000.00 USD | 163.41 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,610,000.00 USD | 102.01 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,610,000.00 USD | 102.12 USD | 0.00 USD | `+10.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,610,000.00 USD | 714.59 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,610,000.00 USD | 928.13 USD | 0.00 USD | `+11.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,610,000.00 USD | 102.45 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,610,000.00 USD | 219.84 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,610,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,610,000.00 USD | 1,130.00 USD | 0.00 USD | `+11.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,610,000.00 USD | 288.46 USD | 0.00 USD | `+12.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,610,000.00 USD | 119.92 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,610,000.00 USD | 231.00 USD | 0.00 USD | `+13.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,610,000.00 USD | 221.07 USD | 0.00 USD | `+13.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,610,000.00 USD | 992.00 USD | 0.00 USD | `+13.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,610,000.00 USD | 148.48 USD | 0.00 USD | `+13.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,610,000.00 USD | 191.36 USD | 0.00 USD | `+13.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,620,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,620,000.00 USD | 108.21 USD | 0.00 USD | `+14.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,620,000.00 USD | 169.68 USD | 0.00 USD | `+14.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,620,000.00 USD | 574.66 USD | 0.00 USD | `+14.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,620,000.00 USD | 121.87 USD | 0.00 USD | `+15.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,620,000.00 USD | 115.88 USD | 0.00 USD | `+16.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,620,000.00 USD | 340.05 USD | 0.00 USD | `+16.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,620,000.00 USD | 742.12 USD | 0.00 USD | `+16.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,620,000.00 USD | 899.47 USD | 0.00 USD | `+16.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,690,000.00 USD | 70,020.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,690,000.00 USD | 373.97 USD | 0.00 USD | `+17.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,700,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,700,000.00 USD | 6,370.00 USD | 0.00 USD | `+18.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,700,000.00 USD | 404.20 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,920,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,920,000.00 USD | 172.16 USD | 0.00 USD | `+20.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,920,000.00 USD | 922.87 USD | 0.00 USD | `+21.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,920,000.00 USD | 489.40 USD | 0.00 USD | `+21.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,920,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,920,000.00 USD | 118.01 USD | 0.00 USD | `+22.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,920,000.00 USD | 971.48 USD | 0.00 USD | `+23.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,920,000.00 USD | 818.31 USD | 0.00 USD | `+23.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,920,000.00 USD | 312.31 USD | 0.00 USD | `+23.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,920,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,920,000.00 USD | 1,890.00 USD | 0.00 USD | `+24.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,920,000.00 USD | 178.46 USD | 0.00 USD | `+24.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,920,000.00 USD | 173.42 USD | 0.00 USD | `+26.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,920,000.00 USD | 184.75 USD | 0.00 USD | `+26.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,920,000.00 USD | 135.78 USD | 0.00 USD | `+27.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,930,000.00 USD | 127.96 USD | 0.00 USD | `+27.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,930,000.00 USD | 476.43 USD | 0.00 USD | `+28.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,930,000.00 USD | 869.35 USD | 0.00 USD | `+28.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,960,000.00 USD | 35,110.00 USD | 0.00 USD | `+28.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,960,000.00 USD | 251.06 USD | 0.00 USD | `+28.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,960,000.00 USD | 552.44 USD | 0.00 USD | `+28.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,960,000.00 USD | 537.26 USD | 0.00 USD | `+29.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,960,000.00 USD | 1,110.00 USD | 0.00 USD | `+31.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,960,000.00 USD | 320.29 USD | 0.00 USD | `+31.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,970,000.00 USD | 1,100.00 USD | 0.00 USD | `+31.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,970,000.00 USD | 2,270.00 USD | 0.00 USD | `+32.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,970,000.00 USD | 1,270.00 USD | 0.00 USD | `+32.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,970,000.00 USD | 1,380.00 USD | 0.00 USD | `+33.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,970,000.00 USD | 2,410.00 USD | 0.00 USD | `+34.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,980,000.00 USD | 9,520.00 USD | 0.00 USD | `+35.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,980,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,980,000.00 USD | 529.11 USD | 0.00 USD | `+35.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,990,000.00 USD | 7,700.00 USD | 0.00 USD | `+36.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,990,000.00 USD | 906.03 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,990,000.00 USD | 434.61 USD | 0.00 USD | `+39.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,990,000.00 USD | 163.52 USD | 0.00 USD | `+40.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,000,000.00 USD | 10,370.00 USD | 0.00 USD | `+41.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 2,010,000.00 USD | 5,270.00 USD | 0.00 USD | `+43.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 2,010,000.00 USD | 115.02 USD | 0.00 USD | `+44.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,010,000.00 USD | 3,870.00 USD | 0.00 USD | `+49.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,010,000.00 USD | 197.97 USD | 0.00 USD | `+51.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,020,000.00 USD | 3,200.00 USD | 0.00 USD | `+52.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,020,000.00 USD | 179.58 USD | 0.00 USD | `+53.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,020,000.00 USD | 568.45 USD | 0.00 USD | `+53.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,020,000.00 USD | 169.57 USD | 0.00 USD | `+54.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,020,000.00 USD | 446.52 USD | 0.00 USD | `+57.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,020,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,230,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,230,000.00 USD | 407.95 USD | 0.00 USD | `+61.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,240,000.00 USD | 174.91 USD | 0.00 USD | `+62.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,240,000.00 USD | 4,680.00 USD | 0.00 USD | `+65.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,240,000.00 USD | 960.26 USD | 0.00 USD | `+67.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,240,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,240,000.00 USD | 805.90 USD | 0.00 USD | `+71.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,240,000.00 USD | 655.55 USD | 0.00 USD | `+73.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,250,000.00 USD | 4,890.00 USD | 0.00 USD | `+74.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,250,000.00 USD | 471.09 USD | 0.00 USD | `+75.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,250,000.00 USD | 383.85 USD | 0.00 USD | `+76.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,910,000.00 USD | 654,840.00 USD | 0.00 USD | `+77.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,910,000.00 USD | 1,510.00 USD | 0.00 USD | `+77.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,910,000.00 USD | 111.87 USD | 0.00 USD | `+86.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,910,000.00 USD | 219.91 USD | 0.00 USD | `+88.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.95` | 2,910,000.00 USD | 121.74 USD | 0.00 USD | `+100.00%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 6,430,000.00 USD | 0.00 USD | 6,430,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,370.00 USD |
| `7D` | `7.16` | 6,330,000.00 USD | 0.00 USD | 6,330,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,790.00 USD |
| `7D` | `7.18` | 6,270,000.00 USD | 0.00 USD | 6,270,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,770.00 USD |
| `7D` | `7.20` | 6,240,000.00 USD | 0.00 USD | 6,240,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,250.00 USD |
| `7D` | `7.22` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,900.00 USD |
| `7D` | `7.24` | 6,190,000.00 USD | 0.00 USD | 6,190,000.00 USD | 39,910.00 USD | 0.00 USD | 10,600.00 USD |
| `7D` | `7.26` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 0.00 USD | 1,810.00 USD | 38.95 USD |
| `7D` | `7.28` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.30` | 6,140,000.00 USD | 0.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD |
| `7D` | `7.36` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 983.83 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.38` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 46,040.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.40` | 6,080,000.00 USD | 0.00 USD | 6,080,000.00 USD | 44,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.46` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 6,010,000.00 USD | 0.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.50` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 570.66 USD |
| `7D` | `7.52` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 5,950,000.00 USD | 0.00 USD | 5,950,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 20,150.00 USD | 4,310.00 USD | 301.55 USD |
| `7D` | `7.58` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `7.60` | 5,040,000.00 USD | 0.00 USD | 5,040,000.00 USD | 2,440.00 USD | 4,900.00 USD | 7,920.00 USD |
| `1D` | `7.61` | 5,030,000.00 USD | 0.00 USD | 5,030,000.00 USD | 1,220.00 USD | 761.26 USD | 11,670.00 USD |
| `1D` | `7.62` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 956.60 USD | 1,330.00 USD | 133.28 USD |
| `7D` | `7.62` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 0.00 USD | 2,130.00 USD | 547.66 USD |
| `1D` | `7.63` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 1,040.00 USD | 0.00 USD | 8,870.00 USD |
| `1D` | `7.64` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 33,010.00 USD | 812.96 USD | 2,390.00 USD |
| `7D` | `7.64` | 5,880,000.00 USD | 0.00 USD | 5,880,000.00 USD | 41,300.00 USD | 0.00 USD | 761.26 USD |
| `1D` | `7.65` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 0.00 USD | 817.75 USD | 9,870.00 USD |
| `1D` | `7.66` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 3,030.00 USD | 0.00 USD | 531.95 USD |
| `7D` | `7.66` | 5,840,000.00 USD | 0.00 USD | 5,840,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,420.00 USD |
| `1D` | `7.67` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 1,140.00 USD | 587.20 USD | 114.38 USD |
| `1D` | `7.68` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 892.30 USD | 0.00 USD | 3,830.00 USD |
| `7D` | `7.68` | 5,810,000.00 USD | 0.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.69` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `7.70` | 4,940,000.00 USD | 0.00 USD | 4,940,000.00 USD | 4,140.00 USD | 2,390.00 USD | 16,770.00 USD |
| `7D` | `7.70` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 393.33 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.71` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 660.12 USD | 5,040.00 USD | 7,390.00 USD |
| `1D` | `7.72` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 701.68 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `7.72` | 5,800,000.00 USD | 0.00 USD | 5,800,000.00 USD | 38,970.00 USD | 0.00 USD | 41,000.00 USD |
| `1D` | `7.73` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 16,520.00 USD | 0.00 USD | 184.39 USD |
| `7D` | `7.74` | 5,720,000.00 USD | 0.00 USD | 5,720,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 458.75 USD | 494.12 USD | 0.00 USD |
| `7D` | `7.76` | 5,690,000.00 USD | 0.00 USD | 5,690,000.00 USD | 812.95 USD | 13,360.00 USD | 11,090.00 USD |
| `1D` | `7.77` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 13,020.00 USD | 689.91 USD | 3,430.00 USD |
| `1D` | `7.78` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `7D` | `7.78` | 5,660,000.00 USD | 0.00 USD | 5,660,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,030.00 USD |
| `1D` | `7.79` | 4,830,000.00 USD | 0.00 USD | 4,830,000.00 USD | 18,960.00 USD | 2,920.00 USD | 7,250.00 USD |
| `1D` | `7.80` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 4,920.00 USD | 7,910.00 USD | 709.61 USD |
| `7D` | `7.80` | 5,580,000.00 USD | 0.00 USD | 5,580,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,010.00 USD |
| `1D` | `7.81` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 349.70 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.82` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 302.72 USD | 1,680.00 USD | 0.00 USD |
| `7D` | `7.82` | 5,520,000.00 USD | 0.00 USD | 5,520,000.00 USD | 1,450.00 USD | 5,260.00 USD | 5,140.00 USD |
| `1D` | `7.83` | 4,790,000.00 USD | 0.00 USD | 4,790,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD |
| `1D` | `7.84` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 1,060.00 USD | 1,800.00 USD | 10.76 USD |
| `7D` | `7.84` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 32,340.00 USD | 2,380.00 USD | 26,820.00 USD |
| `1D` | `7.85` | 4,750,000.00 USD | 0.00 USD | 4,750,000.00 USD | 5,210.00 USD | 1,250.00 USD | 2,650.00 USD |
| `1D` | `7.86` | 4,740,000.00 USD | 0.00 USD | 4,740,000.00 USD | 5,060.00 USD | 6,690.00 USD | 17,220.00 USD |
| `7D` | `7.86` | 5,450,000.00 USD | 0.00 USD | 5,450,000.00 USD | 137,360.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.87` | 4,710,000.00 USD | 0.00 USD | 4,710,000.00 USD | 13,800.00 USD | 10,860.00 USD | 24,540.00 USD |
| `1D` | `7.88` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 161,670.00 USD | 5,890.00 USD | 34,820.00 USD |
| `7D` | `7.88` | 5,290,000.00 USD | 0.00 USD | 5,290,000.00 USD | 170,100.00 USD | 12,780.00 USD | 29,320.00 USD |
| `1D` | `7.89` | 4,460,000.00 USD | 0.00 USD | 4,460,000.00 USD | 59,740.00 USD | 3,720.00 USD | 27,230.00 USD |
| `1D` | `7.90` | 4,370,000.00 USD | 0.00 USD | 4,370,000.00 USD | 56,130.00 USD | 6,970.00 USD | 5,990.00 USD |
| `7D` | `7.90` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,600.00 USD |
| `1D` | `7.91` | 4,300,000.00 USD | 0.00 USD | 4,300,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD |
| `7D` | `7.92` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 55,490.00 USD | 23,630.00 USD | 40,540.00 USD |
| `1D` | `7.93` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,480.00 USD |
| `1D` | `7.94` | 4,200,000.00 USD | 0.00 USD | 4,200,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,750.00 USD |
| `7D` | `7.94` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 51,390.00 USD | 9,960.00 USD | 33,210.00 USD |
| `1D` | `7.95` | 4,100,000.00 USD | 0.00 USD | 4,100,000.00 USD | 27,800.00 USD | 9,190.00 USD | 86,980.00 USD |
| `1D` | `7.96` | 3,980,000.00 USD | 0.00 USD | 3,980,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,330.00 USD |
| `7D` | `7.96` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,840.00 USD |
| `1D` | `7.97` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 3,870,000.00 USD | 0.00 USD | 3,870,000.00 USD | 5,050.00 USD | 2,060.00 USD | 42,970.00 USD |
| `7D` | `7.98` | 4,680,000.00 USD | 0.00 USD | 4,680,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,400.00 USD |
| `1D` | `7.99` | 3,820,000.00 USD | 0.00 USD | 3,820,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,660.00 USD |
| `1D` | `8.00` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 50,430.00 USD | 8,950.00 USD | 21,810.00 USD |
| `7D` | `8.00` | 4,450,000.00 USD | 0.00 USD | 4,450,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,080.00 USD |
| `1D` | `8.01` | 3,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 6,540.00 USD | 3,750.00 USD | 4,040.00 USD |
| `1D` | `8.02` | 3,710,000.00 USD | 0.00 USD | 3,710,000.00 USD | 75,150.00 USD | 0.00 USD | 274.70 USD |
| `7D` | `8.02` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 15,300.00 USD | 46,670.00 USD | 55,530.00 USD |
| `1D` | `8.03` | 3,630,000.00 USD | 0.00 USD | 3,630,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 460,990.00 USD | 0.00 USD | 85,870.00 USD |
| `1D` | `8.05` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,960.00 USD |
| `1D` | `8.06` | 3,160,000.00 USD | 0.00 USD | 3,160,000.00 USD | 155,360.00 USD | 0.00 USD | 66,970.00 USD |
| `7D` | `8.06` | 3,700,000.00 USD | 0.00 USD | 3,700,000.00 USD | 336,530.00 USD | 0.00 USD | 85,640.00 USD |
| `1D` | `8.07` | 2,940,000.00 USD | 0.00 USD | 2,940,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 2,790,000.00 USD | 0.00 USD | 2,790,000.00 USD | 14,440.00 USD | 0.00 USD | 65,310.00 USD |
| `7D` | `8.08` | 3,280,000.00 USD | 0.00 USD | 3,280,000.00 USD | 5,100.00 USD | 0.00 USD | 74,730.00 USD |
| `1D` | `8.09` | 2,710,000.00 USD | 0.00 USD | 2,710,000.00 USD | 3,110.00 USD | 0.00 USD | 29,580.00 USD |
| `1D` | `8.10` | 2,680,000.00 USD | 0.00 USD | 2,680,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,420.00 USD |
| `7D` | `8.10` | 3,200,000.00 USD | 0.00 USD | 3,200,000.00 USD | 56,590.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `8.11` | 2,520,000.00 USD | 0.00 USD | 2,520,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `1D` | `8.12` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 13,810.00 USD | 10,020.00 USD | 126,250.00 USD |
| `7D` | `8.12` | 3,130,000.00 USD | 0.00 USD | 3,130,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 2,100,000.00 USD | 0.00 USD | 2,100,000.00 USD | 13,420.00 USD | 7,840.00 USD | 1,710.00 USD |
| `1D` | `8.14` | 2,070,000.00 USD | 0.00 USD | 2,070,000.00 USD | 0.00 USD | 7,660.00 USD | 103,280.00 USD |
| `7D` | `8.14` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 160,410.00 USD | 33,950.00 USD | 184,370.00 USD |
| `1D` | `8.15` | 1,960,000.00 USD | 0.00 USD | 1,960,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,660.00 USD |
| `1D` | `8.16` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 192.50 USD | 21,000.00 USD | 165,460.00 USD |
| `7D` | `8.16` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,520.00 USD |
| `1D` | `8.17` | 1,670,000.00 USD | 0.00 USD | 1,670,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,140.00 USD |
| `1D` | `8.18` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 7,140.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `8.18` | 2,510,000.00 USD | 0.00 USD | 2,510,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,560.00 USD |
| `7D` | `8.20` | 2,300,000.00 USD | 0.00 USD | 2,300,000.00 USD | 174,220.00 USD | 58,100.00 USD | 5,890.00 USD |
| `1D` | `8.21` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 0.00 USD | 0.00 USD | 16,310.00 USD |
| `7D` | `8.22` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 0.00 USD | 1,750.00 USD | 2,380.00 USD |
| `1D` | `8.24` | 1,320,000.00 USD | 0.00 USD | 1,320,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD |
| `7D` | `8.24` | 2,040,000.00 USD | 0.00 USD | 2,040,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 1,310,000.00 USD | 0.00 USD | 1,310,000.00 USD | 0.00 USD | 5,000.00 USD | 38,170.00 USD |
| `1D` | `8.26` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD |
| `1D` | `8.27` | 1,180,000.00 USD | 0.00 USD | 1,180,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD |
| `1D` | `8.28` | 1,130,000.00 USD | 0.00 USD | 1,130,000.00 USD | 0.00 USD | 13,760.00 USD | 4,240.00 USD |
| `7D` | `8.28` | 1,780,000.00 USD | 0.00 USD | 1,780,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,120.00 USD |
| `1D` | `8.29` | 1,110,000.00 USD | 0.00 USD | 1,110,000.00 USD | 27,240.00 USD | 9,380.00 USD | 0.00 USD |
| `1D` | `8.30` | 1,080,000.00 USD | 0.00 USD | 1,080,000.00 USD | 26,280.00 USD | 11,130.00 USD | 20,060.00 USD |
| `7D` | `8.30` | 1,660,000.00 USD | 0.00 USD | 1,660,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,710.00 USD |
| `1D` | `8.31` | 1,020,000.00 USD | 0.00 USD | 1,020,000.00 USD | 47,410.00 USD | 9,970.00 USD | 52,450.00 USD |
| `1D` | `8.32` | 908,940.00 USD | 0.00 USD | 908,940.00 USD | 73,050.00 USD | 6,080.00 USD | 14,060.00 USD |
| `7D` | `8.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 220,640.00 USD | 6,490.00 USD | 1,990.00 USD |
| `1D` | `8.33` | 815,750.00 USD | 0.00 USD | 815,750.00 USD | 0.00 USD | 6,210.00 USD | 109.14 USD |
| `1D` | `8.34` | 809,430.00 USD | 0.00 USD | 809,430.00 USD | 0.00 USD | 2,210.00 USD | 13.84 USD |
| `7D` | `8.34` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 5,080.00 USD |
| `1D` | `8.35` | 807,210.00 USD | 0.00 USD | 807,210.00 USD | 0.00 USD | 19,810.00 USD | 16,970.00 USD |
| `1D` | `8.36` | 770,430.00 USD | 0.00 USD | 770,430.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `8.37` | 752,630.00 USD | 0.00 USD | 752,630.00 USD | 691.75 USD | 14,420.00 USD | 16.86 USD |
| `1D` | `8.38` | 737,500.00 USD | 0.00 USD | 737,500.00 USD | 17,220.00 USD | 5,940.00 USD | 50,290.00 USD |
| `7D` | `8.38` | 909,640.00 USD | 0.00 USD | 909,640.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 664,050.00 USD | 0.00 USD | 664,050.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 517,080.00 USD | 0.00 USD | 517,080.00 USD | 10,500.00 USD | 7,000.00 USD | 56,580.00 USD |
| `7D` | `8.40` | 851,900.00 USD | 0.00 USD | 851,900.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 443,000.00 USD | 0.00 USD | 443,000.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD |
| `1D` | `8.42` | 424,610.00 USD | 0.00 USD | 424,610.00 USD | 0.00 USD | 16,260.00 USD | 42,890.00 USD |
| `7D` | `8.42` | 757,360.00 USD | 0.00 USD | 757,360.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 365,470.00 USD | 0.00 USD | 365,470.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 268,850.00 USD | 0.00 USD | 268,850.00 USD | 11,130.00 USD | 32,380.00 USD | 160,460.00 USD |
| `7D` | `8.44` | 512,380.00 USD | 0.00 USD | 512,380.00 USD | 152,190.00 USD | 8,000.00 USD | 76,300.00 USD |
| `1D` | `8.45` | 64,870.00 USD | 0.00 USD | 64,870.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `1D` | `8.46` | 4,110.00 USD | 0.00 USD | 4,110.00 USD | 0.00 USD | 3,450.00 USD | 0.00 USD |
| `7D` | `8.46` | 275,880.00 USD | 0.00 USD | 275,880.00 USD | 152,650.00 USD | 0.00 USD | 123,230.00 USD |
| `1D` | `8.47` | 663.00 USD | 0.00 USD | 663.00 USD | 663.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.47` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 749.80 USD | 749.80 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 1,500.00 USD | 1,500.00 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 337,360.00 USD | 337,360.00 USD | 0.00 USD | 144,290.00 USD | 0.00 USD | 193,070.00 USD |
| `1D` | `8.49` | 1,510.00 USD | 1,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 12.70 USD |
| `7D` | `8.50` | 337,880.00 USD | 337,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 515.03 USD |
| `1D` | `8.51` | 173,950.00 USD | 173,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172,440.00 USD |
| `1D` | `8.52` | 337,390.00 USD | 337,390.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 4,800.00 USD |
| `7D` | `8.52` | 543,500.00 USD | 543,500.00 USD | 0.00 USD | 113,820.00 USD | 0.00 USD | 91,800.00 USD |
| `1D` | `8.53` | 370,980.00 USD | 370,980.00 USD | 0.00 USD | 33,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.54` | 573,930.00 USD | 573,930.00 USD | 0.00 USD | 202,800.00 USD | 0.00 USD | 156.94 USD |
| `7D` | `8.54` | 902,680.00 USD | 902,680.00 USD | 0.00 USD | 357,740.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `8.55` | 600,710.00 USD | 600,710.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 639,720.00 USD | 639,720.00 USD | 0.00 USD | 686.73 USD | 38,320.00 USD | 0.00 USD |
| `7D` | `8.56` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 144,180.00 USD | 122,650.00 USD | 962.39 USD |
| `1D` | `8.57` | 814,140.00 USD | 814,140.00 USD | 0.00 USD | 174,430.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 873,260.00 USD | 873,260.00 USD | 0.00 USD | 59,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.58` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 875,300.00 USD | 875,300.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.61` | 876,500.00 USD | 876,500.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 699.64 USD |
| `1D` | `8.62` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 125,290.00 USD |
| `7D` | `8.62` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 27,760.00 USD |
| `1D` | `8.63` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 117,050.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.64` | 1,200,000.00 USD | 1,200,000.00 USD | 0.00 USD | 26,280.00 USD | 6,650.00 USD | 3,410.00 USD |
| `7D` | `8.64` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,220,000.00 USD | 1,220,000.00 USD | 0.00 USD | 342.65 USD | 7,060.00 USD | 13,310.00 USD |
| `1D` | `8.66` | 1,240,000.00 USD | 1,240,000.00 USD | 0.00 USD | 6,230.00 USD | 2,020.00 USD | 14,040.00 USD |
| `7D` | `8.66` | 1,390,000.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 6,490.00 USD | 1,530.00 USD |
| `1D` | `8.67` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 880.60 USD | 9,960.00 USD | 56.72 USD |
| `1D` | `8.68` | 1,290,000.00 USD | 1,290,000.00 USD | 0.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 1,540,000.00 USD | 1,540,000.00 USD | 0.00 USD | 0.00 USD | 30,000.00 USD | 117,630.00 USD |
| `1D` | `8.69` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,440,000.00 USD | 1,440,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 34,050.00 USD | 2,520.00 USD | 50,790.00 USD |
| `7D` | `8.72` | 1,740,000.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 547.66 USD |
| `1D` | `8.73` | 1,630,000.00 USD | 1,630,000.00 USD | 0.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,690,000.00 USD | 1,690,000.00 USD | 0.00 USD | 38,500.00 USD | 3,500.00 USD | 17,580.00 USD |
| `7D` | `8.74` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.75` | 1,750,000.00 USD | 1,750,000.00 USD | 0.00 USD | 33,520.00 USD | 8,970.00 USD | 16,930.00 USD |
| `1D` | `8.76` | 1,900,000.00 USD | 1,900,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 57,030.00 USD |
| `7D` | `8.76` | 2,080,000.00 USD | 2,080,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,380.00 USD |
| `1D` | `8.77` | 2,100,000.00 USD | 2,100,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 43,030.00 USD |
| `1D` | `8.78` | 2,210,000.00 USD | 2,210,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,110.00 USD |
| `7D` | `8.78` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD |
| `1D` | `8.79` | 2,290,000.00 USD | 2,290,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,130.00 USD |
| `1D` | `8.80` | 2,440,000.00 USD | 2,440,000.00 USD | 0.00 USD | 107,040.00 USD | 17,940.00 USD | 23,840.00 USD |
| `7D` | `8.80` | 2,460,000.00 USD | 2,460,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 33,400.00 USD |
| `1D` | `8.81` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 31,820.00 USD | 7,690.00 USD | 1,750.00 USD |
| `1D` | `8.82` | 2,550,000.00 USD | 2,550,000.00 USD | 0.00 USD | 2,200.00 USD | 3,530.00 USD | 59,520.00 USD |
| `7D` | `8.82` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 345,340.00 USD | 21,680.00 USD | 39,340.00 USD |
| `1D` | `8.83` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 171,230.00 USD | 19,400.00 USD | 7,020.00 USD |
| `1D` | `8.84` | 2,810,000.00 USD | 2,810,000.00 USD | 0.00 USD | 1,500.00 USD | 3,110.00 USD | 59,130.00 USD |
| `7D` | `8.84` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD |
| `1D` | `8.85` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 13,040.00 USD | 3,360.00 USD | 11,200.00 USD |
| `1D` | `8.86` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 2,060.00 USD | 1,470.00 USD | 607.55 USD |
| `7D` | `8.86` | 2,980,000.00 USD | 2,980,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 81,390.00 USD |
| `1D` | `8.87` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 2,870,000.00 USD | 2,870,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 186.36 USD |
| `7D` | `8.88` | 3,010,000.00 USD | 3,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 12,390.00 USD | 3,410.00 USD | 32,950.00 USD |
| `1D` | `8.90` | 3,040,000.00 USD | 3,040,000.00 USD | 0.00 USD | 28,690.00 USD | 5,990.00 USD | 84,550.00 USD |
| `7D` | `8.90` | 3,130,000.00 USD | 3,130,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.91` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD |
| `1D` | `8.92` | 3,110,000.00 USD | 3,110,000.00 USD | 0.00 USD | 1,110.00 USD | 3,220.00 USD | 6,040.00 USD |
| `7D` | `8.92` | 3,260,000.00 USD | 3,260,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 3,180,000.00 USD | 3,180,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 38,940.00 USD |
| `1D` | `8.94` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 3,770.00 USD |
| `7D` | `8.94` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 129,180.00 USD | 0.00 USD | 13,460.00 USD |
| `1D` | `8.95` | 3,280,000.00 USD | 3,280,000.00 USD | 0.00 USD | 2,540.00 USD | 6,630.00 USD | 20,340.00 USD |
| `1D` | `8.96` | 3,290,000.00 USD | 3,290,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 175.90 USD |
| `7D` | `8.96` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,790.00 USD |
| `1D` | `8.98` | 3,350,000.00 USD | 3,350,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,670.00 USD |
| `7D` | `8.98` | 3,450,000.00 USD | 3,450,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,420,000.00 USD | 3,420,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,420.00 USD |
| `1D` | `9.00` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD |
| `7D` | `9.00` | 3,880,000.00 USD | 3,880,000.00 USD | 0.00 USD | 370,780.00 USD | 17,920.00 USD | 40,730.00 USD |
| `1D` | `9.01` | 3,570,000.00 USD | 3,570,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 16,240.00 USD |
| `1D` | `9.02` | 3,640,000.00 USD | 3,640,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 5,010.00 USD |
| `7D` | `9.02` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,300.00 USD |
| `1D` | `9.03` | 3,810,000.00 USD | 3,810,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,410.00 USD |
| `1D` | `9.04` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 41,220.00 USD | 5,900.00 USD | 14,800.00 USD |
| `7D` | `9.04` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 136,520.00 USD | 74,750.00 USD | 15,490.00 USD |
| `1D` | `9.05` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 21,980.00 USD | 10,760.00 USD | 24,060.00 USD |
| `1D` | `9.06` | 3,970,000.00 USD | 3,970,000.00 USD | 0.00 USD | 28,180.00 USD | 6,890.00 USD | 10,490.00 USD |
| `7D` | `9.06` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,770.00 USD |
| `1D` | `9.07` | 4,030,000.00 USD | 4,030,000.00 USD | 0.00 USD | 13,070.00 USD | 18,070.00 USD | 28,510.00 USD |
| `1D` | `9.08` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 12,960.00 USD | 2,110.00 USD | 33,970.00 USD |
| `7D` | `9.08` | 4,400,000.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,690.00 USD |
| `1D` | `9.09` | 4,210,000.00 USD | 4,210,000.00 USD | 0.00 USD | 84,540.00 USD | 11,440.00 USD | 29,380.00 USD |
| `1D` | `9.10` | 4,280,000.00 USD | 4,280,000.00 USD | 0.00 USD | 16,320.00 USD | 16,280.00 USD | 36,950.00 USD |
| `7D` | `9.10` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD |
| `1D` | `9.11` | 4,440,000.00 USD | 4,440,000.00 USD | 0.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,590,000.00 USD | 4,590,000.00 USD | 0.00 USD | 102,010.00 USD | 22,410.00 USD | 26,360.00 USD |
| `7D` | `9.12` | 6,590,000.00 USD | 6,590,000.00 USD | 0.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 40,180.00 USD |
| `1D` | `9.14` | 4,780,000.00 USD | 4,780,000.00 USD | 0.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 7,650,000.00 USD | 7,650,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,720.00 USD |
| `1D` | `9.15` | 4,880,000.00 USD | 4,880,000.00 USD | 0.00 USD | 57,140.00 USD | 23,170.00 USD | 23,060.00 USD |
| `1D` | `9.16` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,470.00 USD |
| `7D` | `9.16` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 196,390.00 USD |
| `1D` | `9.17` | 5,140,000.00 USD | 5,140,000.00 USD | 0.00 USD | 80,620.00 USD | 3,200.00 USD | 49,540.00 USD |
| `1D` | `9.18` | 5,220,000.00 USD | 5,220,000.00 USD | 0.00 USD | 28,620.00 USD | 26,430.00 USD | 31,220.00 USD |
| `7D` | `9.18` | 9,270,000.00 USD | 9,270,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,060.00 USD |
| `1D` | `9.19` | 5,340,000.00 USD | 5,340,000.00 USD | 0.00 USD | 78,040.00 USD | 29,140.00 USD | 7,680.00 USD |
| `1D` | `9.20` | 5,450,000.00 USD | 5,450,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,460.00 USD |
| `7D` | `9.20` | 10,190,000.00 USD | 10,190,000.00 USD | 0.00 USD | 550,150.00 USD | 134,550.00 USD | 237,080.00 USD |
| `1D` | `9.21` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,760.00 USD |
| `1D` | `9.22` | 5,560,000.00 USD | 5,560,000.00 USD | 0.00 USD | 58,470.00 USD | 2,850.00 USD | 11,100.00 USD |
| `7D` | `9.22` | 11,330,000.00 USD | 11,330,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 379,180.00 USD |
| `1D` | `9.23` | 5,570,000.00 USD | 5,570,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 17.80 USD |
| `1D` | `9.24` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 45,890.00 USD | 0.00 USD | 3,020.00 USD |
| `7D` | `9.24` | 11,850,000.00 USD | 11,850,000.00 USD | 0.00 USD | 336,360.00 USD | 44,660.00 USD | 135,140.00 USD |
| `1D` | `9.25` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,510.00 USD |
| `1D` | `9.26` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,540.00 USD |
| `7D` | `9.26` | 12,240,000.00 USD | 12,240,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 21,230.00 USD |
| `1D` | `9.27` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 23,520.00 USD | 1,360.00 USD | 6,640.00 USD |
| `1D` | `9.28` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 169.17 USD |
| `7D` | `9.28` | 12,890,000.00 USD | 12,890,000.00 USD | 0.00 USD | 428,160.00 USD | 69,460.00 USD | 153,880.00 USD |
| `1D` | `9.29` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,600.00 USD |
| `7D` | `9.30` | 13,450,000.00 USD | 13,450,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 263,010.00 USD |
| `1D` | `9.31` | 5,840,000.00 USD | 5,840,000.00 USD | 0.00 USD | 27,750.00 USD | 5,020.00 USD | 12,920.00 USD |
| `1D` | `9.32` | 5,850,000.00 USD | 5,850,000.00 USD | 0.00 USD | 9,650.00 USD | 1,330.00 USD | 5,070.00 USD |
| `7D` | `9.32` | 14,050,000.00 USD | 14,050,000.00 USD | 0.00 USD | 241,960.00 USD | 51,970.00 USD | 308,180.00 USD |
| `1D` | `9.33` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 8,050.00 USD | 6,000.00 USD | 8,990.00 USD |
| `1D` | `9.34` | 5,930,000.00 USD | 5,930,000.00 USD | 0.00 USD | 46,210.00 USD | 3,660.00 USD | 5,580.00 USD |
| `7D` | `9.34` | 14,250,000.00 USD | 14,250,000.00 USD | 0.00 USD | 98,640.00 USD | 41,250.00 USD | 59,820.00 USD |
| `1D` | `9.35` | 5,960,000.00 USD | 5,960,000.00 USD | 0.00 USD | 13,620.00 USD | 817.75 USD | 14,910.00 USD |
| `1D` | `9.36` | 5,980,000.00 USD | 5,980,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 8,030.00 USD |
| `7D` | `9.36` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 215,620.00 USD | 64,120.00 USD | 97,570.00 USD |
| `1D` | `9.37` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 12,900.00 USD | 6,260.00 USD | 2,720.00 USD |
| `1D` | `9.38` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 13,850.00 USD |
| `7D` | `9.38` | 14,960,000.00 USD | 14,960,000.00 USD | 0.00 USD | 224,850.00 USD | 31,100.00 USD | 77,240.00 USD |
| `1D` | `9.39` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 9,080.00 USD | 1,600.00 USD | 12.70 USD |
| `1D` | `9.40` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 22,270.00 USD | 0.00 USD | 12.64 USD |
| `7D` | `9.40` | 15,350,000.00 USD | 15,350,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 103,930.00 USD |
| `1D` | `9.41` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 4,410.00 USD | 0.00 USD | 10,140.00 USD |
| `1D` | `9.42` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 9,240.00 USD | 2,390.00 USD | 6,520.00 USD |
| `7D` | `9.42` | 15,520,000.00 USD | 15,520,000.00 USD | 0.00 USD | 109,230.00 USD | 13,910.00 USD | 52,280.00 USD |
| `1D` | `9.43` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 5,380.00 USD | 700.38 USD | 20.54 USD |
| `1D` | `9.44` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 795.69 USD | 568.00 USD | 2,430.00 USD |
| `7D` | `9.44` | 15,670,000.00 USD | 15,670,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 44,640.00 USD |
| `1D` | `9.45` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 96.25 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `9.46` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 16,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.46` | 15,760,000.00 USD | 15,760,000.00 USD | 0.00 USD | 89,160.00 USD | 0.00 USD | 10,510.00 USD |
| `1D` | `9.47` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 1,180.00 USD | 1,900.00 USD | 8,050.00 USD |
| `1D` | `9.48` | 6,140,000.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 494.12 USD | 0.00 USD |
| `7D` | `9.48` | 15,820,000.00 USD | 15,820,000.00 USD | 0.00 USD | 10,620.00 USD | 11,060.00 USD | 35,440.00 USD |
| `1D` | `9.49` | 6,160,000.00 USD | 6,160,000.00 USD | 0.00 USD | 9,740.00 USD | 689.91 USD | 3,380.00 USD |
| `7D` | `9.50` | 15,950,000.00 USD | 15,950,000.00 USD | 0.00 USD | 65,230.00 USD | 12,050.00 USD | 53,180.00 USD |
| `7D` | `9.52` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 57,650.00 USD | 18,520.00 USD | 30,220.00 USD |
| `7D` | `9.54` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 13,190.00 USD | 13,310.00 USD | 839.03 USD |
| `7D` | `9.56` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 7,430.00 USD | 5,260.00 USD | 5,050.00 USD |
| `7D` | `9.58` | 16,170,000.00 USD | 16,170,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 27,020.00 USD |
| `7D` | `9.60` | 16,230,000.00 USD | 16,230,000.00 USD | 0.00 USD | 31,720.00 USD | 5,460.00 USD | 19,760.00 USD |
| `7D` | `9.62` | 16,260,000.00 USD | 16,260,000.00 USD | 0.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `352.89M` | Total OI Tokens: `41,542,058.8 AVAX`
  * 1h OI Change: `-0.15%` | 4h OI Change: `-1.27%` | 24h OI Change: `-6.58%`
  * Exchange Breakdown: Binance=`80.22M` | Bybit=`57.44M` | OKX=`11.52M` | Hyperliquid=`16.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.45K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0100%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0100%` | **USDT Bitget** | `0.0066%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `52.93%` | `47.07%` | `1.12` | 4,970,000.00 USD |
| `15M` | `Binance` | `64.2%` | `35.8%` | `1.79` | 1,930,000.00 USD |
| `15M` | `OKX` | `51.06%` | `48.94%` | `1.04` | 245,020.00 USD |
| `15M` | `Bybit` | `57.58%` | `42.42%` | `1.36` | 286,920.00 USD |
| `15M` | `KuCoin` | `64.67%` | `35.33%` | `1.83` | 57,510.00 USD |
| `15M` | `Gate` | `67.03%` | `32.97%` | `2.03` | 297,430.00 USD |
| `15M` | `Bitget` | `76.77%` | `23.23%` | `3.30` | 94,640.00 USD |
| `15M` | `BingX` | `28.86%` | `71.14%` | `0.41` | 192,870.00 USD |
| `15M` | `MEXC` | `28.38%` | `71.62%` | `0.40` | 445,180.00 USD |
| `15M` | `Bitunix` | `52%` | `48%` | `1.08` | 74,780.00 USD |
| `15M` | `Hyperliquid` | `56.68%` | `43.32%` | `1.31` | 14,340.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.99%` | `49.01%` | `1.04` | 994,220.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 255,740.00 USD |
| `15M` | `HTX` | `59.9%` | `40.1%` | `1.49` | 16,930.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `69.55%` | `30.45%` | `2.28` | 72,090.00 USD |
| `15M` | `Aster` | `67.92%` | `32.08%` | `2.12` | 328.52 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `96.46%` | `3.54%` | `27.25` | 409.81 USD |
| `15M` | `Whale Positions` | `64.2%` | `35.8%` | `1.79` | 1,930,000.00 USD |
| `15M` | `Global Accounts` | `52.93%` | `47.07%` | `1.12` | 4,970,000.00 USD |
| `1H` | `AVAX` | `48.39%` | `51.61%` | `0.94` | 15,040,000.00 USD |
| `1H` | `Binance` | `54.27%` | `45.73%` | `1.19` | 5,340,000.00 USD |
| `1H` | `OKX` | `49.2%` | `50.8%` | `0.97` | 826,090.00 USD |
| `1H` | `Bybit` | `55.24%` | `44.76%` | `1.23` | 1,090,000.00 USD |
| `1H` | `KuCoin` | `65.98%` | `34.02%` | `1.94` | 199,880.00 USD |
| `1H` | `Gate` | `60.1%` | `39.9%` | `1.51` | 398,470.00 USD |
| `1H` | `Bitget` | `55.79%` | `44.21%` | `1.26` | 346,480.00 USD |
| `1H` | `BingX` | `42.71%` | `57.29%` | `0.75` | 487,060.00 USD |
| `1H` | `MEXC` | `45.32%` | `54.68%` | `0.83` | 1,970,000.00 USD |
| `1H` | `Bitunix` | `42.42%` | `57.58%` | `0.74` | 441,000.00 USD |
| `1H` | `Hyperliquid` | `28.91%` | `71.09%` | `0.41` | 157,570.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.23%` | `50.77%` | `0.97` | 2,660,000.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0%` | `100%` | `0.00` | 818,390.00 USD |
| `1H` | `HTX` | `53.9%` | `46.1%` | `1.17` | 89,310.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `52.15%` | `47.85%` | `1.09` | 206,500.00 USD |
| `1H` | `Aster` | `28.66%` | `71.34%` | `0.40` | 2,580.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `79.94%` | `20.06%` | `3.99` | 12,840.00 USD |
| `1H` | `Whale Positions` | `54.27%` | `45.73%` | `1.19` | 5,340,000.00 USD |
| `1H` | `Global Accounts` | `48.39%` | `51.61%` | `0.94` | 15,040,000.00 USD |
| `4H` | `AVAX` | `45.02%` | `54.98%` | `0.82` | 73,210,000.00 USD |
| `4H` | `Binance` | `51.03%` | `48.97%` | `1.04` | 23,830,000.00 USD |
| `4H` | `OKX` | `49.72%` | `50.28%` | `0.99` | 5,790,000.00 USD |
| `4H` | `Bybit` | `44.54%` | `55.46%` | `0.80` | 6,200,000.00 USD |
| `4H` | `KuCoin` | `50.02%` | `49.98%` | `1.00` | 1,060,000.00 USD |
| `4H` | `Gate` | `52.13%` | `47.87%` | `1.09` | 1,860,000.00 USD |
| `4H` | `Bitget` | `41.36%` | `58.64%` | `0.71` | 2,370,000.00 USD |
| `4H` | `BingX` | `29.33%` | `70.67%` | `0.42` | 10,410,000.00 USD |
| `4H` | `MEXC` | `45.67%` | `54.33%` | `0.84` | 5,670,000.00 USD |
| `4H` | `Bitunix` | `46.62%` | `53.38%` | `0.87` | 1,790,000.00 USD |
| `4H` | `Hyperliquid` | `35.25%` | `64.75%` | `0.54` | 648,470.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.78%` | `49.22%` | `1.03` | 11,030,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `2.26%` | `97.74%` | `0.02` | 1,940,000.00 USD |
| `4H` | `HTX` | `56.47%` | `43.53%` | `1.30` | 336,920.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `53.44%` | `46.56%` | `1.15` | 214,370.00 USD |
| `4H` | `Aster` | `25.24%` | `74.76%` | `0.34` | 33,210.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `57.67%` | `42.33%` | `1.36` | 27,830.00 USD |
| `4H` | `Whale Positions` | `51.03%` | `48.97%` | `1.04` | 23,830,000.00 USD |
| `4H` | `Global Accounts` | `45.02%` | `54.98%` | `0.82` | 73,210,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `8.62` | `8.61` | `8.62` | `8.64` | `8.58` | 677,702.04 USD | 366,387.84 USD | 311,314.20 USD | 55,073.64 USD | `+8.13%` | `8B / 8S` |
| `0:00 UTC` | `8.60` | `8.60` | `8.60` | `8.63` | `8.58` | 929,414.14 USD | 426,619.56 USD | 502,794.57 USD | -76,175.01 USD | `-8.20%` | `4B / 10S` |
| `5:00 UTC` | `8.57` | `8.57` | `8.57` | `8.60` | `8.56` | 1,552,705.44 USD | 422,695.37 USD | 1,130,010.07 USD | -707,314.70 USD | `-45.55%` | `6B / 15S` |
| `0:00 UTC` | `8.56` | `8.56` | `8.56` | `8.62` | `8.50` | 1,991,917.42 USD | 805,962.82 USD | 1,185,954.60 USD | -379,991.79 USD | `-19.08%` | `9B / 38S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.55` | `8.48` | 1,276,824.26 USD | 505,302.94 USD | 771,521.32 USD | -266,218.38 USD | `-20.85%` | `4B / 18S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.52` | `8.45` | 1,829,814.14 USD | 869,168.19 USD | 960,645.95 USD | -91,477.76 USD | `-5.00%` | `11B / 14S` |
| `5:00 UTC` | `8.51` | `8.50` | `8.51` | `8.52` | `8.48` | 752,301.06 USD | 385,792.91 USD | 366,508.15 USD | 19,284.76 USD | `+2.56%` | `8B / 9S` |
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 535,990.99 USD | 272,440.57 USD | 263,550.41 USD | 8,890.16 USD | `+1.66%` | `4B / 4S` |

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
| `5m` | -17,180.00 USD | 65,480.00 USD | **`ACCUMULATION`** |
| `15m` | 29,110.00 USD | 163,630.00 USD | **`ACCUMULATION`** |
| `30m` | -41,330.00 USD | -192,730.00 USD | **`DISTRIBUTION`** |
| `1h` | -259,560.00 USD | -345,010.00 USD | **`DISTRIBUTION`** |
| `2h` | -273,570.00 USD | -2,520,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -248,220.00 USD | -1,320,000.00 USD | **`DISTRIBUTION`** |
| `6h` | 24,270.00 USD | -541,170.00 USD | **`DISTRIBUTION`** |
| `8h` | 59,590.00 USD | -2,760,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -838,490.00 USD | -1,110,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,790,000.00 USD | -12,480,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -8,460,000.00 USD | -50,830,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,550,000.00 USD | -267,060,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-17.18K` | 15m=`+29.11K` | 1h=`-259.56K` | 24h=`-2.79M`
* Futures Capital Netflows: 5m=`+65.48K` | 15m=`+163.63K` | 1h=`-345.01K` | 24h=`-12.48M`
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
  * `2026-10-30 14:37:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:32:38 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 14:09:38 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 13:52:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 13:51:38 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:38 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:37:38 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Execution Entry: `8.17` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `8.05` (Risk Distance: `0.1200` pts)
  * +2.5R Take Profit: `8.47`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.53` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.65` (Risk Distance: `0.1200` pts)
  * +2.5R Take Profit: `8.23`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.54`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
