# 🏛️ SOVEREIGN CANDIDATE DOSSIER: AVAX
**Canonical Key**: `AVAX` | **Broker Instrument**: `AVXUSD.p` | **Asset Class**: `Crypto Alt L1`
**Timestamp**: `2026-10-30 15:18:04 IST` (`2026-10-30 09:48:04 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `8.45` | **Live Ask Quote**: `8.49` | **Mid Price**: `8.47`
- **Spread Points**: `4.00` | **Spread BPS**: `47.23 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `8.33` | VWAP Z-Score: `+0.68` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `0.0594` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `47.77` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `8.87` | Lower -3.00σ Band: `7.79`
  * Upper +2.51σ Band: `8.78` | Lower -2.51σ Band: `7.88`
  * Upper +2.01σ Band: `8.69` | Lower -2.01σ Band: `7.97`
  * Upper +2.00σ Band: `8.69` | Lower -2.00σ Band: `7.97`
  * Upper +1.28σ Band: `8.56` | Lower -1.28σ Band: `8.10`
  * Upper +1.00σ Band: `8.51` | Lower -1.00σ Band: `8.15`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`8.47` | EMA-20=`8.47` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`8.48` (Slope: `+0.0000`) | EMA-100=`8.55`
  * Institutional Anchors: EMA-144=`8.60` | EMA-200=`8.66` (Slope: `-0.2424`) | EMA-233=`8.68`
- **Range Boundaries**: 24H High=`9.06` | 24H Low=`7.97` | Weekly High=`9.14` | Weekly Low=`7.97`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `8.52` (Distance: `-0.66%`)
  * Point of Control (POC) = `8.32` (Distance: `+1.74%`)
  * Value Area Low (VAL) = `8.17` (Distance: `+3.63%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`8.90` | POC=`8.74` | VAL=`8.55`
  * Prior Day Extremes: PDH=`9.06` | PDL=`8.24` | PDC=`8.33`
  * Monday Range Blueprint: High=`9.03` | Mid=`8.88` | Low=`8.73`
  * Developing Weekly Value Area: Weekly VAH=`9.02` | Weekly POC=`8.92` | Weekly VAL=`8.69`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`8.58` | Low=`7.97`
  * London Session (08:00-16:00 UTC): High=`8.64` | Low=`8.42`
  * New York Session (13:00-21:00 UTC): High=`8.52` | Low=`8.42`
  * Initial Balance (First Hour): IB High=`8.59` | IB Low=`8.50`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `8.44` - `8.50`
  * Optimal Trade Entry (OTE 0.705): `8.49`
  * Structural Invalidation Anchor (0.786): `8.54`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `8.47` | `8.47` | `8.44` | `8.46` | `63,050` | 532,849.52 USD | -215,829.37 USD | `-40.50%` | -5,817,817.15 USD | `-2.16` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `8.46` | `8.48` | `8.46` | `8.48` | `22,299` | 188,817.33 USD | 47,892.98 USD | `+25.36%` | -5,769,924.17 USD | `+0.65` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `8.48` | `8.48` | `8.48` | `8.48` | `1,153` | 9,777.34 USD | -4,875.22 USD | `-49.86%` | -5,774,799.39 USD | `+0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `8.48` | `8.51` | `8.46` | `8.46` | `82,886` | 702,848.74 USD | -8,982.78 USD | `-1.28%` | -5,715,267.02 USD | `-0.10` | **`BEARISH`** | `NEUTRAL CHOP` |
| `15m` | `8.46` | `8.48` | `8.46` | `8.47` | `94,312` | 798,371.69 USD | 113,279.23 USD | `+14.19%` | -5,601,987.79 USD | `+0.28` | **`BULLISH`** | `DELTA ALIGNED` |
| `15m` | `8.47` | `8.48` | `8.44` | `8.48` | `86,502` | 731,444.19 USD | -172,811.60 USD | `-23.63%` | -5,774,799.39 USD | `-0.37` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `8.63` | `8.63` | `8.48` | `8.50` | `671,897` | 5,750,861.25 USD | -1,429,699.87 USD | `-24.86%` | -5,391,829.51 USD | `-0.68` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `8.50` | `8.52` | `8.45` | `8.48` | `439,030` | 3,723,872.89 USD | -159,958.73 USD | `-4.30%` | -5,551,788.23 USD | `+0.07` | **`BEARISH`** | `NEUTRAL CHOP` |
| `1h` | `8.48` | `8.51` | `8.44` | `8.48` | `263,700` | 2,232,664.62 USD | -68,515.15 USD | `-3.07%` | -5,620,303.39 USD | `+0.12` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.48` | `702,730` | 5,956,537.50 USD | -228,473.88 USD | `-3.84%` | -5,633,313.88 USD | `+0.48` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `9.01` | `9.08` | `8.79` | `8.85` | `2,257,850` | 20,128,793.68 USD | -2,511,995.64 USD | `-12.48%` | -2,565,817.62 USD | `-1.00` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `8.85` | `8.86` | `8.24` | `8.28` | `9,887,211` | 83,385,218.31 USD | -3,335,945.82 USD | `-4.00%` | -5,901,763.44 USD | `-0.98` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `8.28` | `8.48` | `7.99` | `8.45` | `5,044,426` | 41,379,085.88 USD | -289,781.98 USD | `-0.70%` | -6,191,545.43 USD | `+0.89` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `8.45` | `8.68` | `8.40` | `8.50` | `2,701,744` | 23,135,089.54 USD | 786,705.43 USD | `+3.40%` | -5,404,840.00 USD | `+1.19` | **`BULLISH`** | `NEUTRAL CHOP` |
| `4h` | `8.50` | `8.52` | `8.44` | `8.48` | `702,730` | 5,956,537.50 USD | -228,473.88 USD | `-3.84%` | -5,633,313.88 USD | `+0.48` | **`BEARISH`** | `NEUTRAL CHOP` |

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
| --- | **`8.47`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `8.47` | `87.0300` | 737.57 USD | 3,007.39 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.47` | `1652.6700` | 14,005.39 USD | 17,012.77 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `8.47` | `120.0800` | 1,017.58 USD | 18,030.36 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.47` | `5.5200` | 46.78 USD | 18,077.13 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.47` | `340.8000` | 2,887.87 USD | 20,965.00 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.47` | `38.4500` | 325.81 USD | 21,290.82 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `8.47` | `118.0100` | 999.96 USD | 22,290.77 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `8.47` | `87.0300` | 737.38 USD | 23,028.15 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `8.47` | `216.1300` | 1,831.10 USD | 24,859.25 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.47` | `87.0300` | 737.33 USD | 25,596.58 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.47` | `1652.6700` | 14,001.42 USD | 39,598.00 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `8.47` | `159.2800` | 1,349.28 USD | 40,947.27 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `8.47` | `60.3400` | 511.12 USD | 41,458.40 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.47` | `71.0700` | 602.01 USD | 42,060.40 USD | `3 orders` | `-0.07%` | `-` |
| `BID` | `8.47` | `222.8900` | 1,887.99 USD | 43,948.39 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.47` | `87.0300` | 737.16 USD | 44,685.55 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `8.47` | `1186.1000` | 10,046.03 USD | 54,731.58 USD | `1 orders` | `-0.08%` | `-` |
| `BID` | `8.47` | `1652.6700` | 13,997.45 USD | 68,729.04 USD | `1 orders` | `-0.08%` | `-` |
| `ASK` | `8.48` | `87.0300` | 738.18 USD | 33,638.67 USD | `1 orders` | `+0.07%` | `-` |
| `ASK` | `8.48` | `1728.4900` | 14,660.53 USD | 32,900.49 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `4.7200` | 40.03 USD | 18,239.96 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `707.4300` | 6,000.07 USD | 18,199.93 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `84.0400` | 712.78 USD | 12,199.86 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `65.2700` | 553.57 USD | 11,487.08 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `87.0300` | 738.11 USD | 10,933.51 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `8.48` | `8.3700` | 70.99 USD | 10,195.40 USD | `3 orders` | `+0.05%` | `-` |
| `ASK` | `8.48` | `91.7000` | 777.70 USD | 10,124.41 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.48` | `200.0000` | 1,696.14 USD | 9,346.71 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.48` | `208.1100` | 1,764.86 USD | 7,650.57 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `8.48` | `60.3400` | 511.70 USD | 5,885.72 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `8.48` | `65.2700` | 553.46 USD | 5,374.02 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.48` | `137.5600` | 1,166.44 USD | 4,820.55 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `8.48` | `47.8000` | 405.31 USD | 3,654.11 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `8.48` | `65.2700` | 553.43 USD | 3,248.81 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.48` | `1.9200` | 16.28 USD | 2,695.38 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `8.48` | `87.0300` | 737.88 USD | 2,679.10 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.48` | `87.0300` | 737.84 USD | 1,941.22 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `8.48` | `141.9500` | 1,203.38 USD | 1,203.38 USD | `1 orders` | `+0.01%` | `-` |
| `MID_SPREAD` | `8.48` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 8.48` | `0.00%` | `-` |
| `BID` | `8.48` | `150.0100` | 1,271.36 USD | 1,271.36 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `8.48` | `117.8100` | 998.45 USD | 2,269.82 USD | `1 orders` | `-0.01%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 15:10:55 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1475` | `0x7737...bf66` | `SHORT` | 1,452,134.90 USD | `171,568.06` | `7.43` | `8.46` | `111.03` | -176,589.88 USD | `-12.16%` | `10X Cross` |
| `1577` | `0xeadc...9d55` | `LONG` | 1,354,821.21 USD | `160,070.56` | `8.11` | `8.46` | `0.000000` | 57,183.64 USD | `+4.22%` | `10X Cross` |

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
  * 24H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.41%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.94%`)
  * 48H Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.34%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.96%`)
  * 3D Horizon: Short MP=`8.76` (Vol: 389,700.00 USD, Dist: `+3.34%`) | Long MP=`8.05` (Vol: 448,200.00 USD, Dist: `--4.96%`)
  * 7D Horizon: Short MP=`9.23` (Vol: 459,400.00 USD, Dist: `+8.89%`) | Long MP=`8.31` (Vol: 454,800.00 USD, Dist: `--1.92%`)
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
| `7D` | `Long Liquidation` | `7.14` | 6,420,000.00 USD | 6,420,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.14` | 20,270.00 USD | 476,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.16` | 6,310,000.00 USD | 6,310,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.17` | 2,380.00 USD | 455,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.18` | 6,260,000.00 USD | 6,260,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.18` | 1,440.00 USD | 453,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.20` | 2,520.00 USD | 451,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.20` | 6,230,000.00 USD | 6,230,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.21` | 322.94 USD | 449,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.22` | 6,200,000.00 USD | 6,200,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.24` | 1,480.00 USD | 449,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.24` | 6,180,000.00 USD | 6,180,000.00 USD | 39,910.00 USD | 0.00 USD | 10,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.25` | 29,170.00 USD | 447,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.25` | 24,850.00 USD | 418,470.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.26` | 6,130,000.00 USD | 6,130,000.00 USD | 0.00 USD | 1,810.00 USD | 38.95 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.28` | 6,130,000.00 USD | 6,130,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.29` | 36,420.00 USD | 393,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.29` | 1,680.00 USD | 357,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.30` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.32` | 6,110,000.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.34` | 552.42 USD | 355,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.36` | 3,820.00 USD | 354,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.36` | 6,110,000.00 USD | 6,110,000.00 USD | 983.83 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.37` | 3,970.00 USD | 351,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.38` | 1,100.00 USD | 347,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.38` | 6,110,000.00 USD | 6,110,000.00 USD | 46,040.00 USD | 0.00 USD | 503.12 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.38` | 13,430.00 USD | 346,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.40` | 6,060,000.00 USD | 6,060,000.00 USD | 44,790.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.42` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 457.98 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.42` | 147.61 USD | 332,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.43` | 3,290.00 USD | 332,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.45` | 2,410.00 USD | 329,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.46` | 10,390.00 USD | 326,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.46` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.46` | 4,590.00 USD | 316,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.47` | 1,120.00 USD | 311,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.48` | 5,990,000.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 962.81 USD | 310,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.50` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 570.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.50` | 421.78 USD | 309,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.51` | 1,710.00 USD | 309,320.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.52` | 5,970,000.00 USD | 5,970,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.53` | 1,570.00 USD | 307,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.54` | 4,210.00 USD | 306,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.54` | 5,930,000.00 USD | 5,930,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.55` | 2,580.00 USD | 301,820.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.56` | 5,900,000.00 USD | 5,900,000.00 USD | 20,150.00 USD | 4,310.00 USD | 301.55 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.57` | 25,060.00 USD | 299,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `7.58` | 118.25 USD | 274,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `7.58` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.59` | 5,100,000.00 USD | 5,100,000.00 USD | 1,390.00 USD | 0.00 USD | 7,310.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.59` | 1,630.00 USD | 274,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.60` | 5,090,000.00 USD | 5,090,000.00 USD | 706.40 USD | 4,900.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.61` | 5,090,000.00 USD | 5,090,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 754.04 USD | 272,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.62` | 5,070,000.00 USD | 5,070,000.00 USD | 3,270.00 USD | 1,330.00 USD | 286.32 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.62` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 2,130.00 USD | 547.66 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.62` | 787.51 USD | 271,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.63` | 5,070,000.00 USD | 5,070,000.00 USD | 1,040.00 USD | 0.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.63` | 378.93 USD | 270,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.64` | 5,060,000.00 USD | 5,060,000.00 USD | 33,010.00 USD | 812.96 USD | 2,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.64` | 5,870,000.00 USD | 5,870,000.00 USD | 41,300.00 USD | 0.00 USD | 761.26 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.65` | 5,020,000.00 USD | 5,020,000.00 USD | 0.00 USD | 817.75 USD | 9,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.66` | 135.42 USD | 270,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.66` | 5,010,000.00 USD | 5,010,000.00 USD | 3,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.66` | 5,830,000.00 USD | 5,830,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,420.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 256.09 USD | 270,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.67` | 5,010,000.00 USD | 5,010,000.00 USD | 1,140.00 USD | 587.20 USD | 401.01 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.67` | 4,480.00 USD | 270,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.68` | 5,000,000.00 USD | 5,000,000.00 USD | 892.30 USD | 0.00 USD | 3,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.68` | 5,790,000.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.68` | 739.30 USD | 265,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.69` | 5,000,000.00 USD | 5,000,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.70` | 6,690.00 USD | 264,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.70` | 5,000,000.00 USD | 5,000,000.00 USD | 4,140.00 USD | 2,390.00 USD | 17,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.70` | 5,780,000.00 USD | 5,780,000.00 USD | 393.33 USD | 0.00 USD | 686.63 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.71` | 4,970,000.00 USD | 4,970,000.00 USD | 660.12 USD | 5,040.00 USD | 7,650.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.72` | 4,960,000.00 USD | 4,960,000.00 USD | 701.68 USD | 568.00 USD | 2,390.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.72` | 5,780,000.00 USD | 5,780,000.00 USD | 38,970.00 USD | 0.00 USD | 41,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.73` | 4,960,000.00 USD | 4,960,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.74` | 4,950,000.00 USD | 4,950,000.00 USD | 16,520.00 USD | 0.00 USD | 50.97 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.74` | 5,700,000.00 USD | 5,700,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.75` | 4,930,000.00 USD | 4,930,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.75` | 500.12 USD | 258,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.76` | 4,920,000.00 USD | 4,920,000.00 USD | 458.75 USD | 494.12 USD | 15.98 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.76` | 5,670,000.00 USD | 5,670,000.00 USD | 812.95 USD | 13,360.00 USD | 11,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.76` | 455.73 USD | 257,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.77` | 4,910,000.00 USD | 4,910,000.00 USD | 13,020.00 USD | 689.91 USD | 3,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.78` | 6,310.00 USD | 257,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.78` | 4,900,000.00 USD | 4,900,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.78` | 5,650,000.00 USD | 5,650,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 3,750.00 USD | 250,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.79` | 4,890,000.00 USD | 4,890,000.00 USD | 18,960.00 USD | 2,920.00 USD | 6,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.79` | 4,480.00 USD | 247,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.80` | 4,860,000.00 USD | 4,860,000.00 USD | 4,920.00 USD | 7,910.00 USD | 111.29 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.80` | 5,570,000.00 USD | 5,570,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,010.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.80` | 6,380.00 USD | 242,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.81` | 4,850,000.00 USD | 4,850,000.00 USD | 349.70 USD | 0.00 USD | 321.73 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.82` | 4,850,000.00 USD | 4,850,000.00 USD | 248.67 USD | 1,680.00 USD | 137.41 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.82` | 5,510,000.00 USD | 5,510,000.00 USD | 1,450.00 USD | 5,260.00 USD | 5,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.83` | 1,940.00 USD | 236,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.83` | 4,840,000.00 USD | 4,840,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.84` | 4,810,000.00 USD | 4,810,000.00 USD | 1,060.00 USD | 1,800.00 USD | 574.12 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.84` | 5,490,000.00 USD | 5,490,000.00 USD | 32,340.00 USD | 2,380.00 USD | 26,820.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.84` | 22,560.00 USD | 234,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.85` | 4,810,000.00 USD | 4,810,000.00 USD | 5,210.00 USD | 1,250.00 USD | 3,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.86` | 4,800,000.00 USD | 4,800,000.00 USD | 3,110.00 USD | 6,690.00 USD | 17,160.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.86` | 5,430,000.00 USD | 5,430,000.00 USD | 137,360.00 USD | 5,460.00 USD | 17,740.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.87` | 233.83 USD | 211,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.87` | 4,770,000.00 USD | 4,770,000.00 USD | 13,700.00 USD | 10,860.00 USD | 23,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.88` | 555.19 USD | 211,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.88` | 4,720,000.00 USD | 4,720,000.00 USD | 161,670.00 USD | 5,030.00 USD | 33,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.88` | 5,270,000.00 USD | 5,270,000.00 USD | 170,100.00 USD | 12,780.00 USD | 29,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.89` | 4,520,000.00 USD | 4,520,000.00 USD | 59,740.00 USD | 3,720.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.89` | 15,880.00 USD | 211,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.90` | 4,430,000.00 USD | 4,430,000.00 USD | 56,130.00 USD | 6,970.00 USD | 6,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.90` | 5,060,000.00 USD | 5,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,600.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.91` | 2,930.00 USD | 195,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.91` | 4,360,000.00 USD | 4,360,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.92` | 4,310,000.00 USD | 4,310,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.92` | 4,990,000.00 USD | 4,990,000.00 USD | 55,490.00 USD | 23,630.00 USD | 40,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.92` | 4,600.00 USD | 192,250.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.93` | 4,280,000.00 USD | 4,280,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.93` | 16,340.00 USD | 187,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.94` | 4,260,000.00 USD | 4,260,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.94` | 4,870,000.00 USD | 4,870,000.00 USD | 51,390.00 USD | 9,960.00 USD | 33,210.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.95` | 141.74 USD | 171,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.95` | 4,160,000.00 USD | 4,160,000.00 USD | 27,800.00 USD | 9,190.00 USD | 87,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.96` | 127,900.00 USD | 171,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.96` | 4,040,000.00 USD | 4,040,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.96` | 4,780,000.00 USD | 4,780,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `7.97` | 3,960,000.00 USD | 3,960,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.97` | 1,580.00 USD | 43,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.98` | 3,930,000.00 USD | 3,930,000.00 USD | 5,050.00 USD | 2,060.00 USD | 43,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `7.98` | 4,660,000.00 USD | 4,660,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,400.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `7.99` | 1,280.00 USD | 41,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `7.99` | 3,880,000.00 USD | 3,880,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,730.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.00` | 530.79 USD | 40,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.00` | 3,860,000.00 USD | 3,860,000.00 USD | 50,430.00 USD | 8,950.00 USD | 22,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.00` | 4,430,000.00 USD | 4,430,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.01` | 3,780,000.00 USD | 3,780,000.00 USD | 6,540.00 USD | 3,750.00 USD | 3,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.02` | 3,770,000.00 USD | 3,770,000.00 USD | 75,150.00 USD | 0.00 USD | 114.63 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.02` | 4,350,000.00 USD | 4,350,000.00 USD | 15,300.00 USD | 46,670.00 USD | 55,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.03` | 14,210.00 USD | 39,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.03` | 3,690,000.00 USD | 3,690,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.04` | 3,660,000.00 USD | 3,660,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.04` | 4,230,000.00 USD | 4,230,000.00 USD | 460,990.00 USD | 0.00 USD | 85,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.04` | 823.33 USD | 25,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.05` | 3,600,000.00 USD | 3,600,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.06` | 3,220,000.00 USD | 3,220,000.00 USD | 155,360.00 USD | 0.00 USD | 66,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.06` | 3,680,000.00 USD | 3,680,000.00 USD | 336,530.00 USD | 0.00 USD | 85,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.06` | 439.54 USD | 24,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.07` | 3,000,000.00 USD | 3,000,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.07` | 21,710.00 USD | 24,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.08` | 2,850,000.00 USD | 2,850,000.00 USD | 14,440.00 USD | 0.00 USD | 65,350.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.08` | 3,260,000.00 USD | 3,260,000.00 USD | 5,100.00 USD | 0.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.09` | 2,770,000.00 USD | 2,770,000.00 USD | 3,110.00 USD | 0.00 USD | 29,350.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.10` | 2,740,000.00 USD | 2,740,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.10` | 3,180,000.00 USD | 3,180,000.00 USD | 56,590.00 USD | 0.00 USD | 14,030.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.11` | 2,580,000.00 USD | 2,580,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 738.14 USD | 2,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.12` | 2,310,000.00 USD | 2,310,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,430.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.12` | 3,110,000.00 USD | 3,110,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.12` | 521.62 USD | 1,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.13` | 2,150,000.00 USD | 2,150,000.00 USD | 21,470.00 USD | 8,550.00 USD | 1,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.14` | 2,120,000.00 USD | 2,120,000.00 USD | 2,320.00 USD | 8,630.00 USD | 105,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.14` | 2,950,000.00 USD | 2,950,000.00 USD | 160,410.00 USD | 30,700.00 USD | 184,370.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.15` | 2,000,000.00 USD | 2,000,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `8.15` | 1,420.00 USD | 1,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `8.16` | 1,890,000.00 USD | 1,890,000.00 USD | 192.50 USD | 21,000.00 USD | 165,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.16` | 2,570,000.00 USD | 2,570,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.17` | 1,710,000.00 USD | 1,710,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.18` | 1,500,000.00 USD | 1,500,000.00 USD | 7,140.00 USD | 1,470.00 USD | 15.88 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.18` | 2,500,000.00 USD | 2,500,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.19` | 1,490,000.00 USD | 1,490,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.20` | 1,460,000.00 USD | 1,460,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.20` | 2,290,000.00 USD | 2,290,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.21` | 1,420,000.00 USD | 1,420,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.22` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 16,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.22` | 2,060,000.00 USD | 2,060,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.23` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 1,750.00 USD | 2,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.24` | 1,360,000.00 USD | 1,360,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.24` | 2,030,000.00 USD | 2,030,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.25` | 1,350,000.00 USD | 1,350,000.00 USD | 0.00 USD | 5,000.00 USD | 38,150.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.26` | 1,300,000.00 USD | 1,300,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.26` | 1,890,000.00 USD | 1,890,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.27` | 1,220,000.00 USD | 1,220,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.28` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 13,760.00 USD | 4,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.28` | 1,770,000.00 USD | 1,770,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.29` | 1,150,000.00 USD | 1,150,000.00 USD | 39,480.00 USD | 11,800.00 USD | 53.52 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.30` | 1,100,000.00 USD | 1,100,000.00 USD | 42,390.00 USD | 12,550.00 USD | 20,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.30` | 1,650,000.00 USD | 1,650,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.31` | 1,030,000.00 USD | 1,030,000.00 USD | 52,050.00 USD | 11,920.00 USD | 56,400.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.32` | 905,820.00 USD | 905,820.00 USD | 73,050.00 USD | 6,080.00 USD | 14,220.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.32` | 1,390,000.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 1,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.33` | 812,470.00 USD | 812,470.00 USD | 0.00 USD | 6,210.00 USD | 21.18 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.34` | 806,240.00 USD | 806,240.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.34` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 5,080.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.35` | 804,030.00 USD | 804,030.00 USD | 0.00 USD | 19,810.00 USD | 16,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.36` | 767,230.00 USD | 767,230.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.36` | 1,150,000.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 14,290.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.37` | 749,430.00 USD | 749,430.00 USD | 691.75 USD | 14,420.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.38` | 734,320.00 USD | 734,320.00 USD | 17,220.00 USD | 5,940.00 USD | 50,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.38` | 909,640.00 USD | 909,640.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.39` | 660,920.00 USD | 660,920.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.40` | 513,950.00 USD | 513,950.00 USD | 10,500.00 USD | 7,000.00 USD | 56,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.40` | 851,900.00 USD | 851,900.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.41` | 440,080.00 USD | 440,080.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.42` | 421,690.00 USD | 421,690.00 USD | 0.00 USD | 16,260.00 USD | 43,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.42` | 757,360.00 USD | 757,360.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.43` | 362,410.00 USD | 362,410.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.44` | 265,790.00 USD | 265,790.00 USD | 11,130.00 USD | 32,380.00 USD | 160,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.44` | 512,380.00 USD | 512,380.00 USD | 152,190.00 USD | 8,000.00 USD | 76,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.45` | 61,570.00 USD | 61,570.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `8.46` | 275,880.00 USD | 275,880.00 USD | 152,650.00 USD | 0.00 USD | 123,230.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `8.47` | 815.09 USD | 815.09 USD | 663.00 USD | 0.00 USD | 152.09 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 749.80 USD | 749.80 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.48` | 1,500.00 USD | 1,500.00 USD | 749.80 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.48` | 337,360.00 USD | 337,360.00 USD | 144,290.00 USD | 0.00 USD | 193,070.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.50` | 337,590.00 USD | 337,590.00 USD | 0.00 USD | 0.00 USD | 223.58 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.51` | 174,150.00 USD | 174,150.00 USD | 0.00 USD | 0.00 USD | 172,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.52` | 337,770.00 USD | 337,770.00 USD | 158,630.00 USD | 0.00 USD | 4,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.52` | 543,210.00 USD | 543,210.00 USD | 113,820.00 USD | 0.00 USD | 91,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.53` | 361,950.00 USD | 361,950.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.54` | 564,750.00 USD | 564,750.00 USD | 202,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.54` | 902,390.00 USD | 902,390.00 USD | 357,740.00 USD | 0.00 USD | 1,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.55` | 591,520.00 USD | 591,520.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.56` | 630,630.00 USD | 630,630.00 USD | 686.73 USD | 38,320.00 USD | 101.23 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.56` | 1,170,000.00 USD | 1,170,000.00 USD | 144,180.00 USD | 122,650.00 USD | 962.39 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.57` | 800,120.00 USD | 800,120.00 USD | 169,490.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.58` | 859,420.00 USD | 859,420.00 USD | 59,120.00 USD | 0.00 USD | 179.45 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.58` | 1,340,000.00 USD | 1,340,000.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.60` | 861,460.00 USD | 861,460.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.61` | 862,300.00 USD | 862,300.00 USD | 497.00 USD | 0.00 USD | 337.70 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.62` | 1,030,000.00 USD | 1,030,000.00 USD | 41,980.00 USD | 0.00 USD | 124,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.62` | 1,370,000.00 USD | 1,370,000.00 USD | 2,810.00 USD | 0.00 USD | 27,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.63` | 1,160,000.00 USD | 1,160,000.00 USD | 129,280.00 USD | 2,420.00 USD | 197.20 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.64` | 1,210,000.00 USD | 1,210,000.00 USD | 42,390.00 USD | 8,070.00 USD | 3,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.64` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.65` | 1,250,000.00 USD | 1,250,000.00 USD | 4,980.00 USD | 9,010.00 USD | 17,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.66` | 1,270,000.00 USD | 1,270,000.00 USD | 6,230.00 USD | 2,020.00 USD | 14,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.66` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.67` | 1,280,000.00 USD | 1,280,000.00 USD | 880.60 USD | 9,960.00 USD | 395.26 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.68` | 1,320,000.00 USD | 1,320,000.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.68` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 30,000.00 USD | 117,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.69` | 209.31 USD | 475.12 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.69` | 1,380,000.00 USD | 1,380,000.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.70` | 1,470,000.00 USD | 1,470,000.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.70` | 1,730,000.00 USD | 1,730,000.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.71` | 1,490,000.00 USD | 1,490,000.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.72` | 1,580,000.00 USD | 1,580,000.00 USD | 34,050.00 USD | 2,520.00 USD | 50,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.72` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 547.66 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.73` | 1,660,000.00 USD | 1,660,000.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.74` | 1,720,000.00 USD | 1,720,000.00 USD | 38,500.00 USD | 3,500.00 USD | 17,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.74` | 1,820,000.00 USD | 1,820,000.00 USD | 51,030.00 USD | 30,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.75` | 1,770,000.00 USD | 1,770,000.00 USD | 33,520.00 USD | 8,970.00 USD | 16,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.76` | 1,920,000.00 USD | 1,920,000.00 USD | 82,470.00 USD | 10,010.00 USD | 56,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.76` | 2,070,000.00 USD | 2,070,000.00 USD | 196,960.00 USD | 0.00 USD | 58,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.77` | 2,120,000.00 USD | 2,120,000.00 USD | 155,740.00 USD | 2,060.00 USD | 43,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.78` | 2,240,000.00 USD | 2,240,000.00 USD | 41,500.00 USD | 25,510.00 USD | 50,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.78` | 2,360,000.00 USD | 2,360,000.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.79` | 2,320,000.00 USD | 2,320,000.00 USD | 31,710.00 USD | 17,970.00 USD | 31,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.80` | 2,480,000.00 USD | 2,480,000.00 USD | 113,160.00 USD | 19,150.00 USD | 24,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.80` | 2,450,000.00 USD | 2,450,000.00 USD | 27,360.00 USD | 33,750.00 USD | 33,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.81` | 2,530,000.00 USD | 2,530,000.00 USD | 39,870.00 USD | 8,400.00 USD | 2,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.82` | 2,600,000.00 USD | 2,600,000.00 USD | 4,520.00 USD | 4,510.00 USD | 61,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.82` | 2,850,000.00 USD | 2,850,000.00 USD | 345,340.00 USD | 18,440.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.82` | 6,000.00 USD | 6,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.83` | 2,800,000.00 USD | 2,800,000.00 USD | 171,230.00 USD | 19,400.00 USD | 7,220.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.84` | 2,860,000.00 USD | 2,860,000.00 USD | 1,500.00 USD | 3,110.00 USD | 59,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.84` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.85` | 2,890,000.00 USD | 2,890,000.00 USD | 13,040.00 USD | 3,360.00 USD | 10,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.86` | 2,890,000.00 USD | 2,890,000.00 USD | 2,060.00 USD | 1,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.86` | 2,970,000.00 USD | 2,970,000.00 USD | 29,310.00 USD | 0.00 USD | 81,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.87` | 1,160.00 USD | 7,640.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.87` | 2,900,000.00 USD | 2,900,000.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.88` | 2,920,000.00 USD | 2,920,000.00 USD | 803.70 USD | 14,670.00 USD | 82.64 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.88` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.88` | 691.70 USD | 8,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.89` | 2,970,000.00 USD | 2,970,000.00 USD | 12,390.00 USD | 3,410.00 USD | 32,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.89` | 808.47 USD | 9,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.90` | 3,090,000.00 USD | 3,090,000.00 USD | 28,690.00 USD | 5,990.00 USD | 84,510.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.90` | 3,120,000.00 USD | 3,120,000.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.90` | 8,910.00 USD | 18,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.91` | 3,150,000.00 USD | 3,150,000.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.92` | 3,160,000.00 USD | 3,160,000.00 USD | 1,110.00 USD | 3,220.00 USD | 6,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.92` | 3,250,000.00 USD | 3,250,000.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.93` | 3,230,000.00 USD | 3,230,000.00 USD | 31,830.00 USD | 6,810.00 USD | 39,110.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.94` | 3,300,000.00 USD | 3,300,000.00 USD | 50,590.00 USD | 12,260.00 USD | 3,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.94` | 3,390,000.00 USD | 3,390,000.00 USD | 129,180.00 USD | 0.00 USD | 13,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.95` | 3,330,000.00 USD | 3,330,000.00 USD | 2,540.00 USD | 6,630.00 USD | 20,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.96` | 3,340,000.00 USD | 3,340,000.00 USD | 1,260.00 USD | 2,980.00 USD | 481.46 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.96` | 3,430,000.00 USD | 3,430,000.00 USD | 3,320.00 USD | 4,000.00 USD | 26,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.97` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 152.79 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.97` | 10,480.00 USD | 28,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `8.98` | 3,400,000.00 USD | 3,400,000.00 USD | 35,320.00 USD | 9,420.00 USD | 19,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `8.98` | 3,440,000.00 USD | 3,440,000.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `8.99` | 3,470,000.00 USD | 3,470,000.00 USD | 48,380.00 USD | 22,110.00 USD | 3,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `8.99` | 539,710.00 USD | 568,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.00` | 3,540,000.00 USD | 3,540,000.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.00` | 3,870,000.00 USD | 3,870,000.00 USD | 370,780.00 USD | 17,920.00 USD | 40,730.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.01` | 3,620,000.00 USD | 3,620,000.00 USD | 49,510.00 USD | 14,940.00 USD | 15,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.02` | 3,690,000.00 USD | 3,690,000.00 USD | 39,170.00 USD | 29,440.00 USD | 4,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.02` | 4,010,000.00 USD | 4,010,000.00 USD | 82,280.00 USD | 56,120.00 USD | 1,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.03` | 3,860,000.00 USD | 3,860,000.00 USD | 125,760.00 USD | 10,300.00 USD | 34,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.04` | 3,920,000.00 USD | 3,920,000.00 USD | 41,220.00 USD | 5,900.00 USD | 14,790.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.04` | 4,240,000.00 USD | 4,240,000.00 USD | 136,520.00 USD | 74,750.00 USD | 15,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.05` | 3,980,000.00 USD | 3,980,000.00 USD | 21,980.00 USD | 9,980.00 USD | 24,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.05` | 213.70 USD | 568,440.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.06` | 4,020,000.00 USD | 4,020,000.00 USD | 28,180.00 USD | 6,890.00 USD | 10,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.06` | 4,310,000.00 USD | 4,310,000.00 USD | 7,440.00 USD | 14,960.00 USD | 53,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.06` | 6,040.00 USD | 574,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.07` | 4,080,000.00 USD | 4,080,000.00 USD | 13,070.00 USD | 18,070.00 USD | 28,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.08` | 4,130,000.00 USD | 4,130,000.00 USD | 12,960.00 USD | 2,110.00 USD | 34,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.08` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 11,960.00 USD | 65,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.09` | 4,250,000.00 USD | 4,250,000.00 USD | 82,070.00 USD | 9,730.00 USD | 27,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.10` | 3,890.00 USD | 578,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.10` | 4,310,000.00 USD | 4,310,000.00 USD | 16,320.00 USD | 12,520.00 USD | 34,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.10` | 5,590,000.00 USD | 5,590,000.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.11` | 4,470,000.00 USD | 4,470,000.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.12` | 4,620,000.00 USD | 4,620,000.00 USD | 101,900.00 USD | 22,410.00 USD | 26,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.12` | 6,580,000.00 USD | 6,580,000.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.13` | 4,750,000.00 USD | 4,750,000.00 USD | 75,260.00 USD | 15,960.00 USD | 40,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.14` | 4,820,000.00 USD | 4,820,000.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.14` | 7,640,000.00 USD | 7,640,000.00 USD | 536,560.00 USD | 18,540.00 USD | 500,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.14` | 180.80 USD | 578,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.15` | 4,920,000.00 USD | 4,920,000.00 USD | 57,140.00 USD | 23,170.00 USD | 22,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.16` | 5,040,000.00 USD | 5,040,000.00 USD | 63,930.00 USD | 23,900.00 USD | 32,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.16` | 8,230,000.00 USD | 8,230,000.00 USD | 358,370.00 USD | 44,360.00 USD | 196,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.17` | 5,170,000.00 USD | 5,170,000.00 USD | 80,160.00 USD | 3,200.00 USD | 49,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.18` | 5,260,000.00 USD | 5,260,000.00 USD | 28,310.00 USD | 26,430.00 USD | 31,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.18` | 9,260,000.00 USD | 9,260,000.00 USD | 566,340.00 USD | 162,460.00 USD | 292,060.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.19` | 5,370,000.00 USD | 5,370,000.00 USD | 78,040.00 USD | 29,140.00 USD | 7,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.20` | 5,490,000.00 USD | 5,490,000.00 USD | 64,910.00 USD | 11,090.00 USD | 37,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.20` | 10,180,000.00 USD | 10,180,000.00 USD | 550,150.00 USD | 134,550.00 USD | 237,080.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.21` | 5,530,000.00 USD | 5,530,000.00 USD | 30,000.00 USD | 2,950.00 USD | 4,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.22` | 5,600,000.00 USD | 5,600,000.00 USD | 58,470.00 USD | 2,850.00 USD | 11,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.22` | 11,320,000.00 USD | 11,320,000.00 USD | 620,010.00 USD | 144,840.00 USD | 379,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.23` | 5,600,000.00 USD | 5,600,000.00 USD | 471.32 USD | 4,270.00 USD | 34.98 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.24` | 5,650,000.00 USD | 5,650,000.00 USD | 45,890.00 USD | 0.00 USD | 3,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.24` | 11,840,000.00 USD | 11,840,000.00 USD | 336,360.00 USD | 44,660.00 USD | 135,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.25` | 5,680,000.00 USD | 5,680,000.00 USD | 17,240.00 USD | 5,840.00 USD | 9,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.26` | 5,690,000.00 USD | 5,690,000.00 USD | 574.60 USD | 0.00 USD | 3,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.26` | 12,230,000.00 USD | 12,230,000.00 USD | 273,920.00 USD | 96,980.00 USD | 21,230.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.27` | 5,720,000.00 USD | 5,720,000.00 USD | 23,430.00 USD | 1,360.00 USD | 6,470.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.28` | 5,730,000.00 USD | 5,730,000.00 USD | 1,610.00 USD | 8,760.00 USD | 10.22 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.28` | 12,860,000.00 USD | 12,860,000.00 USD | 428,160.00 USD | 69,460.00 USD | 136,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.29` | 5,770,000.00 USD | 5,770,000.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.29` | 3,860.00 USD | 582,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `9.30` | 5,830,000.00 USD | 5,830,000.00 USD | 39,880.00 USD | 7,520.00 USD | 11,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.30` | 13,400,000.00 USD | 13,400,000.00 USD | 199,810.00 USD | 97,780.00 USD | 233,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.31` | 5,880,000.00 USD | 5,880,000.00 USD | 28,930.00 USD | 5,500.00 USD | 12,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.32` | 5,890,000.00 USD | 5,890,000.00 USD | 11,960.00 USD | 1,330.00 USD | 5,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.32` | 14,000,000.00 USD | 14,000,000.00 USD | 241,960.00 USD | 51,970.00 USD | 308,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.33` | 5,920,000.00 USD | 5,920,000.00 USD | 7,820.00 USD | 6,000.00 USD | 9,640.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.34` | 5,970,000.00 USD | 5,970,000.00 USD | 46,210.00 USD | 3,660.00 USD | 5,530.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.34` | 14,200,000.00 USD | 14,200,000.00 USD | 98,640.00 USD | 41,250.00 USD | 59,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.35` | 6,000,000.00 USD | 6,000,000.00 USD | 13,620.00 USD | 817.75 USD | 15,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.36` | 6,020,000.00 USD | 6,020,000.00 USD | 4,730.00 USD | 6,760.00 USD | 7,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.36` | 14,570,000.00 USD | 14,570,000.00 USD | 215,620.00 USD | 64,120.00 USD | 97,570.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.37` | 6,040,000.00 USD | 6,040,000.00 USD | 12,900.00 USD | 6,260.00 USD | 2,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.38` | 6,070,000.00 USD | 6,070,000.00 USD | 15,290.00 USD | 0.00 USD | 13,890.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.38` | 14,910,000.00 USD | 14,910,000.00 USD | 224,850.00 USD | 31,100.00 USD | 77,240.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.39` | 6,080,000.00 USD | 6,080,000.00 USD | 7,470.00 USD | 1,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.40` | 6,100,000.00 USD | 6,100,000.00 USD | 21,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.40` | 15,290,000.00 USD | 15,290,000.00 USD | 234,760.00 USD | 42,520.00 USD | 103,930.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `9.41` | 6,120,000.00 USD | 6,120,000.00 USD | 3,440.00 USD | 0.00 USD | 10,110.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `9.41` | 440.06 USD | 582,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `9.42` | 15,460,000.00 USD | 15,460,000.00 USD | 109,230.00 USD | 13,910.00 USD | 52,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.44` | 15,610,000.00 USD | 15,610,000.00 USD | 80,230.00 USD | 19,420.00 USD | 44,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.46` | 15,700,000.00 USD | 15,700,000.00 USD | 89,160.00 USD | 0.00 USD | 1,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.48` | 15,740,000.00 USD | 15,740,000.00 USD | 10,620.00 USD | 11,060.00 USD | 20,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.50` | 15,870,000.00 USD | 15,870,000.00 USD | 65,230.00 USD | 12,050.00 USD | 53,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.52` | 15,980,000.00 USD | 15,980,000.00 USD | 57,650.00 USD | 18,520.00 USD | 30,220.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.54` | 16,000,000.00 USD | 16,000,000.00 USD | 11,650.00 USD | 13,310.00 USD | 839.03 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.56` | 16,020,000.00 USD | 16,020,000.00 USD | 7,430.00 USD | 5,260.00 USD | 4,660.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.58` | 16,090,000.00 USD | 16,090,000.00 USD | 35,340.00 USD | 2,380.00 USD | 27,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.60` | 16,140,000.00 USD | 16,140,000.00 USD | 31,720.00 USD | 5,460.00 USD | 19,760.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `9.62` | 16,180,000.00 USD | 16,180,000.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD | `Tier 1 CEX` |
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
| `Live` | `Long` | `1.77` | 2,300,000.00 USD | 0.00 USD | 215.89 USD | `-79.04%` | `121.63` |
| `Live` | `Long` | `1.81` | 2,300,000.00 USD | 0.00 USD | 127.05 USD | `-78.57%` | `70.00` |
| `Live` | `Long` | `1.92` | 2,300,000.00 USD | 0.00 USD | 220.22 USD | `-77.39%` | `115.00` |
| `Live` | `Long` | `1.96` | 2,300,000.00 USD | 0.00 USD | 2,520.00 USD | `-76.91%` | `1,288.03` |
| `Live` | `Long` | `1.97` | 2,300,000.00 USD | 0.00 USD | 217.74 USD | `-76.79%` | `110.81` |
| `Live` | `Long` | `2.00` | 2,300,000.00 USD | 0.00 USD | 160.40 USD | `-76.32%` | `80.00` |
| `Live` | `Long` | `2.04` | 2,300,000.00 USD | 0.00 USD | 1,430.00 USD | `-75.97%` | `701.61` |
| `Live` | `Long` | `2.06` | 2,290,000.00 USD | 0.00 USD | 4,920.00 USD | `-75.61%` | `2,382.76` |
| `Live` | `Long` | `2.15` | 2,290,000.00 USD | 0.00 USD | 247.83 USD | `-74.55%` | `115.00` |
| `Live` | `Long` | `2.19` | 2,290,000.00 USD | 0.00 USD | 252.43 USD | `-74.08%` | `115.00` |
| `Live` | `Long` | `2.21` | 2,290,000.00 USD | 0.00 USD | 808.52 USD | `-73.84%` | `365.02` |
| `Live` | `Long` | `2.29` | 2,290,000.00 USD | 0.00 USD | 263.93 USD | `-72.90%` | `115.00` |
| `Live` | `Long` | `2.35` | 2,290,000.00 USD | 0.00 USD | 110.07 USD | `-72.31%` | `46.94` |
| `Live` | `Long` | `2.69` | 2,290,000.00 USD | 0.00 USD | 942.44 USD | `-68.29%` | `351.00` |
| `Live` | `Long` | `2.85` | 2,290,000.00 USD | 0.00 USD | 328.32 USD | `-66.28%` | `115.00` |
| `Live` | `Long` | `2.87` | 2,290,000.00 USD | 0.00 USD | 381.65 USD | `-66.17%` | `133.21` |
| `Live` | `Long` | `2.94` | 2,290,000.00 USD | 0.00 USD | 44,510.00 USD | `-65.34%` | `15,165.76` |
| `Live` | `Long` | `2.96` | 2,240,000.00 USD | 0.00 USD | 11,810.00 USD | `-64.99%` | `3,981.48` |
| `Live` | `Long` | `2.98` | 2,230,000.00 USD | 0.00 USD | 111.12 USD | `-64.87%` | `37.35` |
| `Live` | `Long` | `3.00` | 2,230,000.00 USD | 0.00 USD | 21,010.00 USD | `-64.51%` | `6,990.57` |
| `Live` | `Long` | `3.06` | 2,210,000.00 USD | 0.00 USD | 102.71 USD | `-63.80%` | `33.51` |
| `Live` | `Long` | `3.17` | 2,210,000.00 USD | 0.00 USD | 1,200.00 USD | `-62.62%` | `377.71` |
| `Live` | `Long` | `3.31` | 2,210,000.00 USD | 0.00 USD | 24,670.00 USD | `-60.97%` | `7,465.11` |
| `Live` | `Long` | `3.37` | 2,180,000.00 USD | 0.00 USD | 389.53 USD | `-60.26%` | `115.76` |
| `Live` | `Long` | `3.38` | 2,180,000.00 USD | 0.00 USD | 151.88 USD | `-60.14%` | `45.00` |
| `Live` | `Long` | `3.54` | 2,180,000.00 USD | 0.00 USD | 392.22 USD | `-58.14%` | `110.64` |
| `Live` | `Long` | `3.58` | 2,180,000.00 USD | 0.00 USD | 583.78 USD | `-57.66%` | `162.84` |
| `Live` | `Long` | `3.67` | 2,180,000.00 USD | 0.00 USD | 109.95 USD | `-56.72%` | `30.00` |
| `Live` | `Long` | `3.75` | 2,180,000.00 USD | 0.00 USD | 1,500.00 USD | `-55.66%` | `400.00` |
| `Live` | `Long` | `3.90` | 2,180,000.00 USD | 0.00 USD | 131.73 USD | `-54.00%` | `33.82` |
| `Live` | `Long` | `3.98` | 2,180,000.00 USD | 0.00 USD | 7,970.00 USD | `-52.94%` | `2,000.00` |
| `Live` | `Long` | `4.03` | 2,170,000.00 USD | 0.00 USD | 402.70 USD | `-52.47%` | `100.05` |
| `Live` | `Long` | `4.04` | 2,170,000.00 USD | 0.00 USD | 152.29 USD | `-52.23%` | `37.65` |
| `Live` | `Long` | `4.08` | 2,170,000.00 USD | 0.00 USD | 1,630.00 USD | `-51.76%` | `400.00` |
| `Live` | `Long` | `4.14` | 2,170,000.00 USD | 0.00 USD | 159.29 USD | `-51.05%` | `38.43` |
| `Live` | `Long` | `4.21` | 2,170,000.00 USD | 0.00 USD | 393.34 USD | `-50.22%` | `93.32` |
| `Live` | `Long` | `4.24` | 2,170,000.00 USD | 0.00 USD | 169.40 USD | `-49.99%` | `40.00` |
| `Live` | `Long` | `4.25` | 2,170,000.00 USD | 0.00 USD | 196.42 USD | `-49.87%` | `46.27` |
| `Live` | `Long` | `4.45` | 2,170,000.00 USD | 0.00 USD | 110.77 USD | `-47.51%` | `24.92` |
| `Live` | `Long` | `4.59` | 2,170,000.00 USD | 0.00 USD | 30,970.00 USD | `-45.74%` | `6,740.93` |
| `Live` | `Long` | `4.62` | 2,140,000.00 USD | 0.00 USD | 3,420.00 USD | `-45.38%` | `739.57` |
| `Live` | `Long` | `4.66` | 2,130,000.00 USD | 0.00 USD | 105.11 USD | `-45.03%` | `22.58` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 3,280.00 USD | `-44.91%` | `703.94` |
| `Live` | `Long` | `4.67` | 2,130,000.00 USD | 0.00 USD | 1,490.00 USD | `-44.79%` | `317.75` |
| `Live` | `Long` | `4.68` | 2,130,000.00 USD | 0.00 USD | 8,380.00 USD | `-44.67%` | `1,787.97` |
| `Live` | `Long` | `4.70` | 2,120,000.00 USD | 0.00 USD | 7,040.00 USD | `-44.56%` | `1,500.00` |
| `Live` | `Long` | `4.75` | 2,110,000.00 USD | 0.00 USD | 474.50 USD | `-43.97%` | `100.00` |
| `Live` | `Long` | `4.76` | 2,110,000.00 USD | 0.00 USD | 105.64 USD | `-43.73%` | `22.17` |
| `Live` | `Long` | `4.83` | 2,110,000.00 USD | 0.00 USD | 467.01 USD | `-42.90%` | `96.59` |
| `Live` | `Long` | `4.87` | 2,110,000.00 USD | 0.00 USD | 2,430.00 USD | `-42.55%` | `500.00` |
| `Live` | `Long` | `4.89` | 2,110,000.00 USD | 0.00 USD | 16,080.00 USD | `-42.19%` | `3,286.00` |
| `Live` | `Long` | `4.91` | 2,090,000.00 USD | 0.00 USD | 3,880.00 USD | `-42.08%` | `790.61` |
| `Live` | `Long` | `4.92` | 2,090,000.00 USD | 0.00 USD | 1,230.00 USD | `-41.96%` | `251.00` |
| `Live` | `Long` | `4.93` | 2,090,000.00 USD | 0.00 USD | 314.61 USD | `-41.72%` | `63.75` |
| `Live` | `Long` | `4.95` | 2,090,000.00 USD | 0.00 USD | 565.66 USD | `-41.60%` | `114.39` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 945.36 USD | `-41.49%` | `190.79` |
| `Live` | `Long` | `4.96` | 2,090,000.00 USD | 0.00 USD | 4,090.00 USD | `-41.37%` | `824.62` |
| `Live` | `Long` | `4.97` | 2,080,000.00 USD | 0.00 USD | 282.23 USD | `-41.25%` | `56.73` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 269.53 USD | `-41.01%` | `53.96` |
| `Live` | `Long` | `5.00` | 2,080,000.00 USD | 0.00 USD | 550.55 USD | `-40.90%` | `110.00` |
| `Live` | `Long` | `5.01` | 2,080,000.00 USD | 0.00 USD | 56,390.00 USD | `-40.78%` | `11,243.48` |
| `Live` | `Long` | `5.04` | 2,030,000.00 USD | 0.00 USD | 482.71 USD | `-40.54%` | `95.87` |
| `Live` | `Long` | `5.05` | 2,020,000.00 USD | 0.00 USD | 504.74 USD | `-40.30%` | `99.85` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 213.20 USD | `-40.07%` | `42.01` |
| `Live` | `Long` | `5.08` | 2,020,000.00 USD | 0.00 USD | 105.46 USD | `-39.95%` | `20.74` |
| `Live` | `Long` | `5.09` | 2,020,000.00 USD | 0.00 USD | 1,270.00 USD | `-39.83%` | `249.71` |
| `Live` | `Long` | `5.11` | 2,020,000.00 USD | 0.00 USD | 118.44 USD | `-39.71%` | `23.20` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 1,040.00 USD | `-39.60%` | `202.43` |
| `Live` | `Long` | `5.12` | 2,020,000.00 USD | 0.00 USD | 250.20 USD | `-39.48%` | `48.82` |
| `Live` | `Long` | `5.13` | 2,020,000.00 USD | 0.00 USD | 396.06 USD | `-39.36%` | `77.13` |
| `Live` | `Long` | `5.17` | 2,020,000.00 USD | 0.00 USD | 1,620.00 USD | `-38.89%` | `312.94` |
| `Live` | `Long` | `5.18` | 2,020,000.00 USD | 0.00 USD | 150.57 USD | `-38.77%` | `29.04` |
| `Live` | `Long` | `5.21` | 2,020,000.00 USD | 0.00 USD | 5,790.00 USD | `-38.42%` | `1,110.70` |
| `Live` | `Long` | `5.24` | 2,010,000.00 USD | 0.00 USD | 502.82 USD | `-38.18%` | `96.05` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 213.00 USD | `-38.06%` | `40.61` |
| `Live` | `Long` | `5.25` | 2,010,000.00 USD | 0.00 USD | 1,050.00 USD | `-37.94%` | `200.00` |
| `Live` | `Long` | `5.26` | 2,010,000.00 USD | 0.00 USD | 2,230.00 USD | `-37.82%` | `423.54` |
| `Live` | `Long` | `5.29` | 2,010,000.00 USD | 0.00 USD | 161,490.00 USD | `-37.59%` | `30,556.43` |
| `Live` | `Long` | `5.32` | 1,850,000.00 USD | 0.00 USD | 232.85 USD | `-37.23%` | `43.81` |
| `Live` | `Long` | `5.33` | 1,850,000.00 USD | 0.00 USD | 716.11 USD | `-37.12%` | `134.48` |
| `Live` | `Long` | `5.39` | 1,850,000.00 USD | 0.00 USD | 660.46 USD | `-36.29%` | `122.42` |
| `Live` | `Long` | `5.41` | 1,850,000.00 USD | 0.00 USD | 260.63 USD | `-36.17%` | `48.22` |
| `Live` | `Long` | `5.42` | 1,850,000.00 USD | 0.00 USD | 20,560.00 USD | `-36.05%` | `3,797.34` |
| `Live` | `Long` | `5.42` | 1,830,000.00 USD | 0.00 USD | 160,400.00 USD | `-35.94%` | `29,567.25` |
| `Live` | `Long` | `5.43` | 1,660,000.00 USD | 0.00 USD | 1,360.00 USD | `-35.82%` | `250.00` |
| `Live` | `Long` | `5.45` | 1,660,000.00 USD | 0.00 USD | 299.48 USD | `-35.70%` | `55.00` |
| `Live` | `Long` | `5.46` | 1,660,000.00 USD | 0.00 USD | 264.72 USD | `-35.46%` | `48.44` |
| `Live` | `Long` | `5.47` | 1,660,000.00 USD | 0.00 USD | 1,320.00 USD | `-35.34%` | `240.95` |
| `Live` | `Long` | `5.49` | 1,660,000.00 USD | 0.00 USD | 354.06 USD | `-35.23%` | `64.55` |
| `Live` | `Long` | `5.50` | 1,660,000.00 USD | 0.00 USD | 19,290.00 USD | `-35.11%` | `3,510.41` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 1,490.00 USD | `-34.64%` | `270.00` |
| `Live` | `Long` | `5.54` | 1,640,000.00 USD | 0.00 USD | 2,880.00 USD | `-34.52%` | `519.63` |
| `Live` | `Long` | `5.58` | 1,640,000.00 USD | 0.00 USD | 63,260.00 USD | `-34.16%` | `11,347.58` |
| `Live` | `Long` | `5.61` | 1,570,000.00 USD | 0.00 USD | 34,490.00 USD | `-33.81%` | `6,153.60` |
| `Live` | `Long` | `5.62` | 1,540,000.00 USD | 0.00 USD | 139.36 USD | `-33.69%` | `24.82` |
| `Live` | `Long` | `5.63` | 1,540,000.00 USD | 0.00 USD | 468.55 USD | `-33.46%` | `83.15` |
| `Live` | `Long` | `5.72` | 1,540,000.00 USD | 0.00 USD | 2,390.00 USD | `-32.39%` | `417.17` |
| `Live` | `Long` | `5.74` | 1,540,000.00 USD | 0.00 USD | 661.65 USD | `-32.27%` | `115.37` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 125.70 USD | `-32.16%` | `21.88` |
| `Live` | `Long` | `5.75` | 1,540,000.00 USD | 0.00 USD | 3,190.00 USD | `-32.04%` | `554.18` |
| `Live` | `Long` | `5.76` | 1,530,000.00 USD | 0.00 USD | 10,850.00 USD | `-31.92%` | `1,882.90` |
| `Live` | `Long` | `5.78` | 1,520,000.00 USD | 0.00 USD | 801.40 USD | `-31.80%` | `138.77` |
| `Live` | `Long` | `5.79` | 1,520,000.00 USD | 0.00 USD | 635.31 USD | `-31.57%` | `109.63` |
| `Live` | `Long` | `5.80` | 1,520,000.00 USD | 0.00 USD | 580.50 USD | `-31.45%` | `100.00` |
| `Live` | `Long` | `5.82` | 1,520,000.00 USD | 0.00 USD | 106.65 USD | `-31.33%` | `18.34` |
| `Live` | `Long` | `5.83` | 1,520,000.00 USD | 0.00 USD | 1,360.00 USD | `-31.21%` | `233.60` |
| `Live` | `Long` | `5.84` | 1,520,000.00 USD | 0.00 USD | 146.13 USD | `-30.98%` | `25.00` |
| `Live` | `Long` | `5.86` | 1,520,000.00 USD | 0.00 USD | 2,110.00 USD | `-30.86%` | `360.33` |
| `Live` | `Long` | `5.89` | 1,520,000.00 USD | 0.00 USD | 984.70 USD | `-30.38%` | `167.04` |
| `Live` | `Long` | `5.91` | 1,520,000.00 USD | 0.00 USD | 399.18 USD | `-30.27%` | `67.60` |
| `Live` | `Long` | `5.96` | 1,510,000.00 USD | 0.00 USD | 11,720.00 USD | `-29.68%` | `1,968.19` |
| `Live` | `Long` | `5.96` | 1,500,000.00 USD | 0.00 USD | 6,320.00 USD | `-29.56%` | `1,060.32` |
| `Live` | `Long` | `5.97` | 1,500,000.00 USD | 0.00 USD | 585.97 USD | `-29.44%` | `98.07` |
| `Live` | `Long` | `6.00` | 1,500,000.00 USD | 0.00 USD | 341.56 USD | `-29.09%` | `56.88` |
| `Live` | `Long` | `6.01` | 1,500,000.00 USD | 0.00 USD | 446.85 USD | `-28.97%` | `74.29` |
| `Live` | `Long` | `6.04` | 1,500,000.00 USD | 0.00 USD | 437.84 USD | `-28.61%` | `72.43` |
| `Live` | `Long` | `6.05` | 1,500,000.00 USD | 0.00 USD | 1,310.00 USD | `-28.50%` | `216.39` |
| `Live` | `Long` | `6.07` | 1,490,000.00 USD | 0.00 USD | 265.10 USD | `-28.38%` | `43.71` |
| `Live` | `Long` | `6.08` | 1,490,000.00 USD | 0.00 USD | 1,690.00 USD | `-28.26%` | `278.94` |
| `Live` | `Long` | `6.09` | 1,490,000.00 USD | 0.00 USD | 3,530.00 USD | `-28.02%` | `579.39` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 1,140.00 USD | `-27.79%` | `185.96` |
| `Live` | `Long` | `6.12` | 1,490,000.00 USD | 0.00 USD | 137.02 USD | `-27.67%` | `22.37` |
| `Live` | `Long` | `6.13` | 1,490,000.00 USD | 0.00 USD | 2,030.00 USD | `-27.55%` | `330.65` |
| `Live` | `Long` | `6.14` | 1,480,000.00 USD | 0.00 USD | 238.61 USD | `-27.43%` | `38.83` |
| `Live` | `Long` | `6.16` | 1,480,000.00 USD | 0.00 USD | 7,810.00 USD | `-27.31%` | `1,268.30` |
| `Live` | `Long` | `6.17` | 1,480,000.00 USD | 0.00 USD | 104.36 USD | `-27.08%` | `16.90` |
| `Live` | `Long` | `6.21` | 1,480,000.00 USD | 0.00 USD | 310.25 USD | `-26.72%` | `50.00` |
| `Live` | `Long` | `6.25` | 1,480,000.00 USD | 0.00 USD | 972.65 USD | `-26.13%` | `155.50` |
| `Live` | `Long` | `6.28` | 1,480,000.00 USD | 0.00 USD | 2,510.00 USD | `-25.90%` | `400.00` |
| `Live` | `Long` | `6.29` | 1,470,000.00 USD | 0.00 USD | 2,430.00 USD | `-25.66%` | `386.46` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 277.48 USD | `-25.31%` | `43.87` |
| `Live` | `Long` | `6.33` | 1,470,000.00 USD | 0.00 USD | 1,430.00 USD | `-25.19%` | `225.14` |
| `Live` | `Long` | `6.36` | 1,470,000.00 USD | 0.00 USD | 4,470.00 USD | `-24.95%` | `703.33` |
| `Live` | `Long` | `6.37` | 1,460,000.00 USD | 0.00 USD | 284,770.00 USD | `-24.83%` | `44,740.07` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 1,310.00 USD | `-24.72%` | `204.92` |
| `Live` | `Long` | `6.38` | 1,180,000.00 USD | 0.00 USD | 5,120.00 USD | `-24.60%` | `801.31` |
| `Live` | `Long` | `6.39` | 1,170,000.00 USD | 0.00 USD | 5,940.00 USD | `-24.48%` | `928.10` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 306.32 USD | `-24.24%` | `47.75` |
| `Live` | `Long` | `6.42` | 1,170,000.00 USD | 0.00 USD | 484.64 USD | `-24.13%` | `75.43` |
| `Live` | `Long` | `6.43` | 1,170,000.00 USD | 0.00 USD | 6,780.00 USD | `-24.01%` | `1,052.89` |
| `Live` | `Long` | `6.46` | 1,160,000.00 USD | 0.00 USD | 363,480.00 USD | `-23.65%` | `56,222.15` |
| `Live` | `Long` | `6.50` | 796,220.00 USD | 0.00 USD | 1,520.00 USD | `-23.18%` | `234.11` |
| `Live` | `Long` | `6.54` | 794,700.00 USD | 0.00 USD | 852.03 USD | `-22.83%` | `130.38` |
| `Live` | `Long` | `6.54` | 793,840.00 USD | 0.00 USD | 8,970.00 USD | `-22.71%` | `1,370.89` |
| `Live` | `Long` | `6.59` | 784,870.00 USD | 0.00 USD | 2,870.00 USD | `-22.12%` | `435.69` |
| `Live` | `Long` | `6.62` | 782,000.00 USD | 0.00 USD | 2,110.00 USD | `-21.88%` | `318.57` |
| `Live` | `Long` | `6.62` | 779,890.00 USD | 0.00 USD | 1,880.00 USD | `-21.76%` | `283.49` |
| `Live` | `Long` | `6.63` | 778,010.00 USD | 0.00 USD | 1,780.00 USD | `-21.65%` | `268.08` |
| `Live` | `Long` | `6.67` | 776,230.00 USD | 0.00 USD | 1,320.00 USD | `-21.17%` | `198.12` |
| `Live` | `Long` | `6.68` | 774,910.00 USD | 0.00 USD | 3,160.00 USD | `-21.06%` | `472.28` |
| `Live` | `Long` | `6.71` | 771,750.00 USD | 0.00 USD | 11,000.00 USD | `-20.82%` | `1,641.31` |
| `Live` | `Long` | `6.71` | 760,750.00 USD | 0.00 USD | 6,180.00 USD | `-20.70%` | `920.74` |
| `Live` | `Long` | `6.75` | 754,570.00 USD | 0.00 USD | 1,330.00 USD | `-20.23%` | `196.95` |
| `Live` | `Long` | `6.78` | 753,240.00 USD | 0.00 USD | 7,990.00 USD | `-19.99%` | `1,179.83` |
| `Live` | `Long` | `6.79` | 745,240.00 USD | 0.00 USD | 22,020.00 USD | `-19.87%` | `3,245.57` |
| `Live` | `Long` | `6.79` | 723,220.00 USD | 0.00 USD | 5,170.00 USD | `-19.76%` | `761.18` |
| `Live` | `Long` | `6.80` | 718,050.00 USD | 0.00 USD | 1,500.00 USD | `-19.64%` | `220.95` |
| `Live` | `Long` | `6.82` | 716,550.00 USD | 0.00 USD | 7,230.00 USD | `-19.52%` | `1,061.04` |
| `Live` | `Long` | `6.83` | 709,310.00 USD | 0.00 USD | 271.02 USD | `-19.40%` | `39.71` |
| `Live` | `Long` | `6.87` | 709,040.00 USD | 0.00 USD | 3,340.00 USD | `-18.93%` | `486.46` |
| `Live` | `Long` | `6.88` | 705,700.00 USD | 0.00 USD | 263.66 USD | `-18.81%` | `38.35` |
| `Live` | `Long` | `6.88` | 705,440.00 USD | 0.00 USD | 1,580.00 USD | `-18.69%` | `229.18` |
| `Live` | `Long` | `6.92` | 703,860.00 USD | 0.00 USD | 579.62 USD | `-18.22%` | `83.70` |
| `Live` | `Long` | `6.93` | 703,280.00 USD | 0.00 USD | 3,500.00 USD | `-18.10%` | `504.07` |
| `Live` | `Long` | `6.95` | 699,790.00 USD | 0.00 USD | 215.30 USD | `-17.99%` | `31.00` |
| `Live` | `Long` | `6.96` | 699,570.00 USD | 0.00 USD | 7,240.00 USD | `-17.87%` | `1,041.68` |
| `Live` | `Long` | `6.96` | 692,330.00 USD | 0.00 USD | 636.74 USD | `-17.75%` | `91.42` |
| `Live` | `Long` | `6.97` | 691,690.00 USD | 0.00 USD | 128,810.00 USD | `-17.63%` | `18,466.99` |
| `Live` | `Long` | `7.00` | 562,880.00 USD | 0.00 USD | 1,040.00 USD | `-17.39%` | `149.32` |
| `Live` | `Long` | `7.01` | 561,840.00 USD | 0.00 USD | 20,890.00 USD | `-17.16%` | `2,978.11` |
| `Live` | `Long` | `7.03` | 540,950.00 USD | 0.00 USD | 1,370.00 USD | `-17.04%` | `194.51` |
| `Live` | `Long` | `7.07` | 539,580.00 USD | 0.00 USD | 23,960.00 USD | `-16.57%` | `3,390.75` |
| `Live` | `Long` | `7.08` | 515,620.00 USD | 0.00 USD | 6,700.00 USD | `-16.45%` | `947.44` |
| `Live` | `Long` | `7.08` | 508,920.00 USD | 0.00 USD | 1,050.00 USD | `-16.33%` | `148.63` |
| `Live` | `Long` | `7.09` | 507,870.00 USD | 0.00 USD | 2,130.00 USD | `-16.21%` | `300.00` |
| `Live` | `Long` | `7.11` | 505,740.00 USD | 0.00 USD | 28,530.00 USD | `-16.10%` | `4,015.35` |
| `Live` | `Long` | `7.12` | 477,210.00 USD | 0.00 USD | 379.66 USD | `-15.98%` | `53.36` |
| `Live` | `Long` | `7.13` | 476,830.00 USD | 0.00 USD | 777.50 USD | `-15.74%` | `108.97` |
| `Live` | `Long` | `7.14` | 476,050.00 USD | 0.00 USD | 20,270.00 USD | `-15.62%` | `2,837.00` |
| `Live` | `Long` | `7.17` | 455,780.00 USD | 0.00 USD | 2,380.00 USD | `-15.27%` | `331.12` |
| `Live` | `Long` | `7.18` | 453,410.00 USD | 0.00 USD | 1,440.00 USD | `-15.15%` | `200.95` |
| `Live` | `Long` | `7.20` | 451,960.00 USD | 0.00 USD | 2,520.00 USD | `-15.03%` | `350.58` |
| `Live` | `Long` | `7.21` | 449,440.00 USD | 0.00 USD | 322.94 USD | `-14.80%` | `44.76` |
| `Live` | `Long` | `7.24` | 449,120.00 USD | 0.00 USD | 1,480.00 USD | `-14.56%` | `205.21` |
| `Live` | `Long` | `7.25` | 447,630.00 USD | 0.00 USD | 29,170.00 USD | `-14.44%` | `4,025.65` |
| `Live` | `Long` | `7.25` | 418,470.00 USD | 0.00 USD | 24,850.00 USD | `-14.32%` | `3,424.57` |
| `Live` | `Long` | `7.29` | 393,620.00 USD | 0.00 USD | 36,420.00 USD | `-13.97%` | `5,000.00` |
| `Live` | `Long` | `7.29` | 357,200.00 USD | 0.00 USD | 1,680.00 USD | `-13.85%` | `230.97` |
| `Live` | `Long` | `7.34` | 355,510.00 USD | 0.00 USD | 552.42 USD | `-13.26%` | `75.21` |
| `Live` | `Long` | `7.36` | 354,960.00 USD | 0.00 USD | 3,820.00 USD | `-13.14%` | `519.63` |
| `Live` | `Long` | `7.37` | 351,140.00 USD | 0.00 USD | 3,970.00 USD | `-13.03%` | `539.15` |
| `Live` | `Long` | `7.38` | 347,170.00 USD | 0.00 USD | 1,100.00 USD | `-12.91%` | `148.75` |
| `Live` | `Long` | `7.38` | 346,070.00 USD | 0.00 USD | 13,430.00 USD | `-12.79%` | `1,817.92` |
| `Live` | `Long` | `7.42` | 332,650.00 USD | 0.00 USD | 147.61 USD | `-12.32%` | `19.88` |
| `Live` | `Long` | `7.43` | 332,500.00 USD | 0.00 USD | 3,290.00 USD | `-12.20%` | `442.38` |
| `Live` | `Long` | `7.45` | 329,210.00 USD | 0.00 USD | 2,410.00 USD | `-12.08%` | `324.35` |
| `Live` | `Long` | `7.46` | 326,790.00 USD | 0.00 USD | 10,390.00 USD | `-11.96%` | `1,393.53` |
| `Live` | `Long` | `7.46` | 316,410.00 USD | 0.00 USD | 4,590.00 USD | `-11.84%` | `614.36` |
| `Live` | `Long` | `7.47` | 311,820.00 USD | 0.00 USD | 1,120.00 USD | `-11.73%` | `149.52` |
| `Live` | `Long` | `7.50` | 310,700.00 USD | 0.00 USD | 962.81 USD | `-11.49%` | `128.46` |
| `Live` | `Long` | `7.50` | 309,740.00 USD | 0.00 USD | 421.78 USD | `-11.37%` | `56.20` |
| `Live` | `Long` | `7.51` | 309,320.00 USD | 0.00 USD | 1,710.00 USD | `-11.25%` | `228.21` |
| `Live` | `Long` | `7.53` | 307,600.00 USD | 0.00 USD | 1,570.00 USD | `-11.14%` | `208.52` |
| `Live` | `Long` | `7.54` | 306,030.00 USD | 0.00 USD | 4,210.00 USD | `-11.02%` | `559.01` |
| `Live` | `Long` | `7.55` | 301,820.00 USD | 0.00 USD | 2,580.00 USD | `-10.78%` | `341.09` |
| `Live` | `Long` | `7.57` | 299,240.00 USD | 0.00 USD | 25,060.00 USD | `-10.66%` | `3,312.23` |
| `Live` | `Long` | `7.58` | 274,190.00 USD | 0.00 USD | 118.25 USD | `-10.55%` | `15.61` |
| `Live` | `Long` | `7.59` | 274,070.00 USD | 0.00 USD | 1,630.00 USD | `-10.31%` | `214.22` |
| `Live` | `Long` | `7.62` | 272,440.00 USD | 0.00 USD | 754.04 USD | `-10.07%` | `99.02` |
| `Live` | `Long` | `7.62` | 271,690.00 USD | 0.00 USD | 787.51 USD | `-9.96%` | `103.28` |
| `Live` | `Long` | `7.63` | 270,900.00 USD | 0.00 USD | 378.93 USD | `-9.84%` | `49.63` |
| `Live` | `Long` | `7.66` | 270,520.00 USD | 0.00 USD | 135.42 USD | `-9.60%` | `17.69` |
| `Live` | `Long` | `7.67` | 270,390.00 USD | 0.00 USD | 256.09 USD | `-9.48%` | `33.41` |
| `Live` | `Long` | `7.67` | 270,130.00 USD | 0.00 USD | 4,480.00 USD | `-9.36%` | `583.63` |
| `Live` | `Long` | `7.68` | 265,650.00 USD | 0.00 USD | 739.30 USD | `-9.25%` | `96.20` |
| `Live` | `Long` | `7.70` | 264,910.00 USD | 0.00 USD | 6,690.00 USD | `-9.13%` | `869.22` |
| `Live` | `Long` | `7.75` | 258,220.00 USD | 0.00 USD | 500.12 USD | `-8.42%` | `64.49` |
| `Live` | `Long` | `7.76` | 257,720.00 USD | 0.00 USD | 455.73 USD | `-8.30%` | `58.69` |
| `Live` | `Long` | `7.78` | 257,270.00 USD | 0.00 USD | 6,310.00 USD | `-8.18%` | `812.08` |
| `Live` | `Long` | `7.79` | 250,950.00 USD | 0.00 USD | 3,750.00 USD | `-8.07%` | `481.06` |
| `Live` | `Long` | `7.79` | 247,210.00 USD | 0.00 USD | 4,480.00 USD | `-7.95%` | `574.50` |
| `Live` | `Long` | `7.80` | 242,730.00 USD | 0.00 USD | 6,380.00 USD | `-7.83%` | `817.06` |
| `Live` | `Long` | `7.83` | 236,350.00 USD | 0.00 USD | 1,940.00 USD | `-7.59%` | `247.42` |
| `Live` | `Long` | `7.84` | 234,420.00 USD | 0.00 USD | 22,560.00 USD | `-7.36%` | `2,875.86` |
| `Live` | `Long` | `7.87` | 211,850.00 USD | 0.00 USD | 233.83 USD | `-7.12%` | `29.73` |
| `Live` | `Long` | `7.88` | 211,620.00 USD | 0.00 USD | 555.19 USD | `-7.00%` | `70.50` |
| `Live` | `Long` | `7.89` | 211,070.00 USD | 0.00 USD | 15,880.00 USD | `-6.77%` | `2,011.99` |
| `Live` | `Long` | `7.91` | 195,180.00 USD | 0.00 USD | 2,930.00 USD | `-6.65%` | `370.74` |
| `Live` | `Long` | `7.92` | 192,250.00 USD | 0.00 USD | 4,600.00 USD | `-6.41%` | `580.78` |
| `Live` | `Long` | `7.93` | 187,650.00 USD | 0.00 USD | 16,340.00 USD | `-6.29%` | `2,059.56` |
| `Live` | `Long` | `7.95` | 171,300.00 USD | 0.00 USD | 141.74 USD | `-6.18%` | `17.84` |
| `Live` | `Long` | `7.96` | 171,160.00 USD | 0.00 USD | 127,900.00 USD | `-6.06%` | `16,078.30` |
| `Live` | `Long` | `7.97` | 43,260.00 USD | 0.00 USD | 1,580.00 USD | `-5.82%` | `198.26` |
| `Live` | `Long` | `7.99` | 41,680.00 USD | 0.00 USD | 1,280.00 USD | `-5.70%` | `160.68` |
| `Live` | `Long` | `8.00` | 40,400.00 USD | 0.00 USD | 530.79 USD | `-5.59%` | `66.39` |
| `Live` | `Long` | `8.03` | 39,870.00 USD | 0.00 USD | 14,210.00 USD | `-5.23%` | `1,770.35` |
| `Live` | `Long` | `8.04` | 25,660.00 USD | 0.00 USD | 823.33 USD | `-5.00%` | `102.34` |
| `Live` | `Short` | `8.05` | 265.81 USD | 265.81 USD | 0.00 USD | `-4.88%` | `33.00` |
| `Live` | `Long` | `8.06` | 24,830.00 USD | 0.00 USD | 439.54 USD | `-4.76%` | `54.50` |
| `Live` | `Long` | `8.07` | 24,400.00 USD | 0.00 USD | 21,710.00 USD | `-4.64%` | `2,688.93` |
| `Live` | `Long` | `8.12` | 2,680.00 USD | 0.00 USD | 738.14 USD | `-4.17%` | `90.96` |
| `Live` | `Long` | `8.12` | 1,940.00 USD | 0.00 USD | 521.62 USD | `-4.05%` | `64.20` |
| `Live` | `Long` | `8.15` | 1,420.00 USD | 0.00 USD | 1,420.00 USD | `-3.70%` | `174.44` |
| `Live` | `Short` | `8.69` | 475.12 USD | 209.31 USD | 0.00 USD | `+2.56%` | `24.10` |
| `Live` | `Short` | `8.82` | 6,480.00 USD | 6,000.00 USD | 0.00 USD | `+4.22%` | `680.16` |
| `Live` | `Short` | `8.87` | 7,640.00 USD | 1,160.00 USD | 0.00 USD | `+4.69%` | `130.57` |
| `Live` | `Short` | `8.88` | 8,330.00 USD | 691.70 USD | 0.00 USD | `+4.92%` | `77.85` |
| `Live` | `Short` | `8.89` | 9,140.00 USD | 808.47 USD | 0.00 USD | `+5.04%` | `90.89` |
| `Live` | `Short` | `8.90` | 18,040.00 USD | 8,910.00 USD | 0.00 USD | `+5.16%` | `1,000.45` |
| `Live` | `Short` | `8.97` | 28,520.00 USD | 10,480.00 USD | 0.00 USD | `+5.99%` | `1,167.41` |
| `Live` | `Short` | `8.99` | 568,230.00 USD | 539,710.00 USD | 0.00 USD | `+6.22%` | `60,000.94` |
| `Live` | `Short` | `9.05` | 568,440.00 USD | 213.70 USD | 0.00 USD | `+6.93%` | `23.60` |
| `Live` | `Short` | `9.06` | 574,480.00 USD | 6,040.00 USD | 0.00 USD | `+7.05%` | `666.20` |
| `Live` | `Short` | `9.10` | 578,370.00 USD | 3,890.00 USD | 0.00 USD | `+7.40%` | `427.53` |
| `Live` | `Short` | `9.14` | 578,550.00 USD | 180.80 USD | 0.00 USD | `+7.99%` | `19.77` |
| `Live` | `Short` | `9.29` | 582,410.00 USD | 3,860.00 USD | 0.00 USD | `+9.77%` | `415.00` |
| `Live` | `Short` | `9.41` | 582,850.00 USD | 440.06 USD | 0.00 USD | `+11.18%` | `46.74` |
| `Live` | `Short` | `9.62` | 582,990.00 USD | 138.98 USD | 0.00 USD | `+13.66%` | `14.44` |
| `Live` | `Short` | `9.64` | 584,920.00 USD | 1,930.00 USD | 0.00 USD | `+13.90%` | `200.61` |
| `Live` | `Short` | `9.69` | 585,210.00 USD | 285.51 USD | 0.00 USD | `+14.37%` | `29.48` |
| `Live` | `Short` | `9.73` | 585,400.00 USD | 192.95 USD | 0.00 USD | `+14.96%` | `19.82` |
| `Live` | `Short` | `9.88` | 585,770.00 USD | 371.77 USD | 0.00 USD | `+16.73%` | `37.61` |
| `Live` | `Short` | `10.35` | 588,430.00 USD | 2,650.00 USD | 0.00 USD | `+22.17%` | `256.58` |
| `Live` | `Short` | `10.47` | 609,380.00 USD | 20,950.00 USD | 0.00 USD | `+23.70%` | `2,000.00` |
| `Live` | `Short` | `10.56` | 609,900.00 USD | 523.81 USD | 0.00 USD | `+24.76%` | `49.58` |
| `Live` | `Short` | `10.78` | 610,080.00 USD | 173.91 USD | 0.00 USD | `+27.24%` | `16.14` |
| `Live` | `Short` | `10.81` | 611,220.00 USD | 1,150.00 USD | 0.00 USD | `+27.72%` | `106.17` |
| `Live` | `Short` | `10.98` | 666,150.00 USD | 54,920.00 USD | 0.00 USD | `+29.72%` | `5,000.00` |
| `Live` | `Short` | `11.01` | 673,120.00 USD | 6,970.00 USD | 0.00 USD | `+29.96%` | `633.00` |
| `Live` | `Short` | `11.19` | 677,330.00 USD | 4,210.00 USD | 0.00 USD | `+32.09%` | `376.48` |
| `Live` | `Short` | `11.27` | 801,650.00 USD | 124,320.00 USD | 0.00 USD | `+33.03%` | `11,035.87` |
| `Live` | `Short` | `11.46` | 801,970.00 USD | 322.74 USD | 0.00 USD | `+35.39%` | `28.15` |
| `Live` | `Short` | `11.48` | 802,240.00 USD | 275.18 USD | 0.00 USD | `+35.63%` | `23.96` |
| `Live` | `Short` | `11.62` | 814,380.00 USD | 12,140.00 USD | 0.00 USD | `+37.28%` | `1,043.90` |
| `Live` | `Short` | `11.69` | 1,110,000.00 USD | 296,760.00 USD | 0.00 USD | `+37.99%` | `25,397.02` |
| `Live` | `Short` | `11.93` | 1,110,000.00 USD | 505.74 USD | 0.00 USD | `+40.82%` | `42.41` |
| `Live` | `Short` | `11.95` | 1,110,000.00 USD | 1,050.00 USD | 0.00 USD | `+41.06%` | `87.54` |
| `Live` | `Short` | `12.30` | 1,110,000.00 USD | 1,730.00 USD | 0.00 USD | `+45.31%` | `140.71` |
| `Live` | `Short` | `12.40` | 1,110,000.00 USD | 343.62 USD | 0.00 USD | `+46.49%` | `27.70` |
| `Live` | `Short` | `12.96` | 1,120,000.00 USD | 1,530.00 USD | 0.00 USD | `+52.99%` | `117.87` |
| `Live` | `Short` | `13.20` | 1,200,000.00 USD | 87,940.00 USD | 0.00 USD | `+55.82%` | `6,665.00` |
| `Live` | `Short` | `13.29` | 1,210,000.00 USD | 3,810.00 USD | 0.00 USD | `+57.00%` | `286.56` |
| `Live` | `Short` | `13.46` | 1,210,000.00 USD | 430.34 USD | 0.00 USD | `+59.01%` | `31.96` |
| `Live` | `Short` | `13.49` | 1,270,000.00 USD | 61,470.00 USD | 0.00 USD | `+59.36%` | `4,555.14` |
| `Live` | `Short` | `13.54` | 1,270,000.00 USD | 111.48 USD | 0.00 USD | `+59.96%` | `8.23` |
| `Live` | `Short` | `13.69` | 1,270,000.00 USD | 172.29 USD | 0.00 USD | `+61.61%` | `12.59` |
| `Live` | `Short` | `14.66` | 1,270,000.00 USD | 823.29 USD | 0.00 USD | `+73.18%` | `56.14` |
| `Live` | `Short` | `14.78` | 1,270,000.00 USD | 242.46 USD | 0.00 USD | `+74.48%` | `16.41` |
| `Live` | `Short` | `15.06` | 1,270,000.00 USD | 324.65 USD | 0.00 USD | `+77.91%` | `21.55` |
| `Live` | `Short` | `15.09` | 1,270,000.00 USD | 219.34 USD | 0.00 USD | `+78.14%` | `14.54` |
| `Live` | `Short` | `15.12` | 1,270,000.00 USD | 542.84 USD | 0.00 USD | `+78.61%` | `35.89` |
| `Live` | `Short` | `15.23` | 1,280,000.00 USD | 4,230.00 USD | 0.00 USD | `+79.91%` | `277.54` |
| `Live` | `Short` | `15.29` | 1,280,000.00 USD | 229.43 USD | 0.00 USD | `+80.62%` | `15.00` |
| `Live` | `Short` | `15.35` | 1,280,000.00 USD | 230.17 USD | 0.00 USD | `+81.21%` | `15.00` |
| `Live` | `Short` | `15.38` | 1,300,000.00 USD | 20,000.00 USD | 0.00 USD | `+81.68%` | `1,300.00` |
| `Live` | `Short` | `15.77` | 1,300,000.00 USD | 185.55 USD | 0.00 USD | `+86.17%` | `11.77` |
| `Live` | `Short` | `15.82` | 1,300,000.00 USD | 1,700.00 USD | 0.00 USD | `+86.88%` | `107.48` |
| `Live` | `Short` | `16.38` | 1,560,000.00 USD | 265,410.00 USD | 0.00 USD | `+93.38%` | `16,208.00` |
| `Live` | `Short` | `16.50` | 1,590,000.00 USD | 23,330.00 USD | 0.00 USD | `+94.79%` | `1,414.55` |
| `Live` | `Short` | `16.52` | 1,590,000.00 USD | 190.91 USD | 0.00 USD | `+95.03%` | `11.56` |
| `Live` | `Short` | `16.62` | 1,590,000.00 USD | 118.20 USD | 0.00 USD | `+96.33%` | `7.11` |
| `Live` | `Short` | `16.64` | 1,610,000.00 USD | 24,270.00 USD | 0.00 USD | `+96.45%` | `1,459.25` |
| `Live` | `Short` | `16.91` | 1,610,000.00 USD | 1,960.00 USD | 0.00 USD | `+99.63%` | `115.73` |
| `Live` | `Short` | `16.93` | 1,700,000.00 USD | 85,310.00 USD | 0.00 USD | `+99.99%` | `5,037.66` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `2.33` | 359,270.00 USD | 0.00 USD | 611.73 USD | `-72.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `4.00` | 358,660.00 USD | 0.00 USD | 793.75 USD | `-52.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.00` | 357,870.00 USD | 0.00 USD | 67,970.00 USD | `-40.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.30` | 289,900.00 USD | 0.00 USD | 205.30 USD | `-37.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.46` | 289,690.00 USD | 0.00 USD | 465.42 USD | `-35.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.50` | 289,230.00 USD | 0.00 USD | 349.35 USD | `-34.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.54` | 288,880.00 USD | 0.00 USD | 1,020.00 USD | `-34.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.82` | 287,860.00 USD | 0.00 USD | 1,330.00 USD | `-31.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.93` | 286,530.00 USD | 0.00 USD | 493.50 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `5.97` | 286,040.00 USD | 0.00 USD | 100.98 USD | `-29.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.00` | 285,940.00 USD | 0.00 USD | 500.70 USD | `-29.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.11` | 285,440.00 USD | 0.00 USD | 4,160.00 USD | `-27.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.17` | 281,280.00 USD | 0.00 USD | 6,500.00 USD | `-27.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.21` | 274,780.00 USD | 0.00 USD | 906.18 USD | `-26.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.25` | 273,880.00 USD | 0.00 USD | 127.35 USD | `-26.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.29` | 273,750.00 USD | 0.00 USD | 864.38 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.50` | 272,880.00 USD | 0.00 USD | 130.10 USD | `-23.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.54` | 272,750.00 USD | 0.00 USD | 4,340.00 USD | `-22.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 268,410.00 USD | 0.00 USD | 5,520.00 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.71` | 262,890.00 USD | 0.00 USD | 203.67 USD | `-20.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.75` | 262,690.00 USD | 0.00 USD | 296.34 USD | `-20.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.76` | 262,390.00 USD | 0.00 USD | 921.19 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.89` | 261,470.00 USD | 0.00 USD | 709.98 USD | `-18.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.91` | 260,760.00 USD | 0.00 USD | 4,630.00 USD | `-18.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.92` | 256,130.00 USD | 0.00 USD | 691.50 USD | `-18.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `6.96` | 255,440.00 USD | 0.00 USD | 262.44 USD | `-17.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.00` | 255,180.00 USD | 0.00 USD | 24,350.00 USD | `-17.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.04` | 230,830.00 USD | 0.00 USD | 653.69 USD | `-16.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.11` | 230,170.00 USD | 0.00 USD | 187.79 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 229,990.00 USD | 0.00 USD | 6,790.00 USD | `-15.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.17` | 223,200.00 USD | 0.00 USD | 4,960.00 USD | `-15.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.21` | 218,240.00 USD | 0.00 USD | 7,210.00 USD | `-14.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.24` | 211,030.00 USD | 0.00 USD | 282.74 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 210,750.00 USD | 0.00 USD | 603.44 USD | `-14.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.25` | 210,140.00 USD | 0.00 USD | 464.61 USD | `-14.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.30` | 209,680.00 USD | 0.00 USD | 2,090.00 USD | `-13.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 207,590.00 USD | 0.00 USD | 129.58 USD | `-13.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.33` | 207,460.00 USD | 0.00 USD | 114.65 USD | `-13.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.39` | 207,340.00 USD | 0.00 USD | 702.75 USD | `-12.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.41` | 206,640.00 USD | 0.00 USD | 4,630.00 USD | `-12.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.46` | 202,010.00 USD | 0.00 USD | 199.39 USD | `-11.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.47` | 201,810.00 USD | 0.00 USD | 6,270.00 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.49` | 195,540.00 USD | 0.00 USD | 37,420.00 USD | `-11.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.50` | 158,120.00 USD | 0.00 USD | 2,120.00 USD | `-11.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.53` | 156,000.00 USD | 0.00 USD | 799.83 USD | `-11.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.54` | 155,200.00 USD | 0.00 USD | 820.44 USD | `-10.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,380.00 USD | 0.00 USD | 218.24 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.58` | 154,160.00 USD | 0.00 USD | 113.78 USD | `-10.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.61` | 154,040.00 USD | 0.00 USD | 152.10 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.62` | 153,890.00 USD | 0.00 USD | 297.59 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.68` | 153,590.00 USD | 0.00 USD | 528.88 USD | `-9.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.71` | 153,060.00 USD | 0.00 USD | 360.13 USD | `-9.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.74` | 152,700.00 USD | 0.00 USD | 578.04 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.75` | 152,130.00 USD | 0.00 USD | 106.32 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.79` | 152,020.00 USD | 0.00 USD | 424.05 USD | `-7.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.80` | 151,600.00 USD | 0.00 USD | 1,170.00 USD | `-7.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.82` | 150,430.00 USD | 0.00 USD | 3,940.00 USD | `-7.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.83` | 146,490.00 USD | 0.00 USD | 154.70 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.86` | 146,330.00 USD | 0.00 USD | 115.23 USD | `-7.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.87` | 146,220.00 USD | 0.00 USD | 183.33 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.89` | 146,030.00 USD | 0.00 USD | 1,890.00 USD | `-6.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.91` | 144,140.00 USD | 0.00 USD | 6,840.00 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 137,300.00 USD | 0.00 USD | 5,710.00 USD | `-6.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.92` | 131,590.00 USD | 0.00 USD | 1,590.00 USD | `-6.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.95` | 130,010.00 USD | 0.00 USD | 898.42 USD | `-6.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 129,110.00 USD | 0.00 USD | 7,960.00 USD | `-6.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.96` | 121,150.00 USD | 0.00 USD | 246.52 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.97` | 120,910.00 USD | 0.00 USD | 2,420.00 USD | `-5.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `7.99` | 118,480.00 USD | 0.00 USD | 1,440.00 USD | `-5.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.00` | 117,050.00 USD | 0.00 USD | 435.73 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.01` | 116,610.00 USD | 0.00 USD | 4,320.00 USD | `-5.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 112,290.00 USD | 0.00 USD | 123.58 USD | `-5.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.04` | 112,170.00 USD | 0.00 USD | 796.62 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.05` | 111,370.00 USD | 0.00 USD | 152.56 USD | `-4.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.06` | 111,220.00 USD | 0.00 USD | 2,730.00 USD | `-4.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.07` | 108,490.00 USD | 0.00 USD | 121.69 USD | `-4.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.09` | 108,370.00 USD | 0.00 USD | 5,230.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.10` | 103,140.00 USD | 0.00 USD | 477.36 USD | `-4.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.11` | 102,660.00 USD | 0.00 USD | 924.78 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 101,740.00 USD | 0.00 USD | 744.88 USD | `-4.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.12` | 100,990.00 USD | 0.00 USD | 6,500.00 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.13` | 94,490.00 USD | 0.00 USD | 884.60 USD | `-3.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.14` | 93,600.00 USD | 0.00 USD | 5,550.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.15` | 88,050.00 USD | 0.00 USD | 1,540.00 USD | `-3.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.16` | 86,510.00 USD | 0.00 USD | 3,080.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.18` | 83,430.00 USD | 0.00 USD | 520.75 USD | `-3.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.19` | 82,900.00 USD | 0.00 USD | 3,020.00 USD | `-3.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.20` | 79,880.00 USD | 0.00 USD | 141.04 USD | `-3.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 79,740.00 USD | 0.00 USD | 22,560.00 USD | `-3.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.21` | 57,180.00 USD | 0.00 USD | 515.66 USD | `-2.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.22` | 56,660.00 USD | 0.00 USD | 139.74 USD | `-2.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.23` | 56,520.00 USD | 0.00 USD | 490.15 USD | `-2.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.24` | 56,030.00 USD | 0.00 USD | 197.96 USD | `-2.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.26` | 55,830.00 USD | 0.00 USD | 9,640.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.27` | 46,200.00 USD | 0.00 USD | 535.65 USD | `-2.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.28` | 45,660.00 USD | 0.00 USD | 734.99 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 44,920.00 USD | 0.00 USD | 828.50 USD | `-2.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.29` | 44,100.00 USD | 0.00 USD | 311.97 USD | `-2.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.30` | 43,780.00 USD | 0.00 USD | 5,380.00 USD | `-1.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.31` | 38,410.00 USD | 0.00 USD | 245.13 USD | `-1.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.32` | 38,160.00 USD | 0.00 USD | 1,690.00 USD | `-1.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.34` | 36,470.00 USD | 0.00 USD | 408.58 USD | `-1.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.35` | 36,060.00 USD | 0.00 USD | 808.63 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.36` | 35,250.00 USD | 0.00 USD | 4,070.00 USD | `-1.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.37` | 31,180.00 USD | 0.00 USD | 24,090.00 USD | `-1.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 7,090.00 USD | 0.00 USD | 503.59 USD | `-1.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.38` | 6,590.00 USD | 0.00 USD | 419.25 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.39` | 6,170.00 USD | 0.00 USD | 376.68 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.40` | 5,790.00 USD | 0.00 USD | 4,240.00 USD | `-0.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.41` | 1,560.00 USD | 0.00 USD | 314.81 USD | `-0.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.43` | 1,240.00 USD | 0.00 USD | 198.83 USD | `-0.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.44` | 1,040.00 USD | 0.00 USD | 195.52 USD | `-0.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.45` | 849.06 USD | 0.00 USD | 138.24 USD | `-0.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `8.46` | 710.81 USD | 0.00 USD | 710.81 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.47` | 769.61 USD | 769.61 USD | 0.00 USD | `+0.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.48` | 1,550.00 USD | 777.14 USD | 0.00 USD | `+0.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.49` | 1,960.00 USD | 408.78 USD | 0.00 USD | `+0.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.51` | 18,970.00 USD | 17,010.00 USD | 0.00 USD | `+0.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.52` | 19,370.00 USD | 408.55 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.53` | 21,540.00 USD | 2,160.00 USD | 0.00 USD | `+0.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 23,710.00 USD | 2,170.00 USD | 0.00 USD | `+0.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.54` | 23,830.00 USD | 123.56 USD | 0.00 USD | `+0.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.55` | 33,820.00 USD | 9,990.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.56` | 35,410.00 USD | 1,600.00 USD | 0.00 USD | `+1.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.57` | 35,980.00 USD | 566.55 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.59` | 36,120.00 USD | 143.28 USD | 0.00 USD | `+1.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.60` | 36,250.00 USD | 124.28 USD | 0.00 USD | `+1.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.61` | 36,350.00 USD | 102.14 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 36,480.00 USD | 124.57 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.62` | 36,600.00 USD | 128.51 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.63` | 36,810.00 USD | 201.97 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.64` | 38,690.00 USD | 1,880.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.65` | 39,560.00 USD | 877.88 USD | 0.00 USD | `+2.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.66` | 39,760.00 USD | 200.85 USD | 0.00 USD | `+2.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.68` | 39,940.00 USD | 176.62 USD | 0.00 USD | `+2.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.69` | 40,930.00 USD | 990.09 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.70` | 41,760.00 USD | 830.81 USD | 0.00 USD | `+2.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 42,340.00 USD | 575.14 USD | 0.00 USD | `+2.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.71` | 42,740.00 USD | 399.67 USD | 0.00 USD | `+2.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.72` | 43,160.00 USD | 421.85 USD | 0.00 USD | `+3.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.73` | 43,400.00 USD | 239.51 USD | 0.00 USD | `+3.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.74` | 47,770.00 USD | 4,370.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.76` | 51,510.00 USD | 3,740.00 USD | 0.00 USD | `+3.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.77` | 51,690.00 USD | 173.28 USD | 0.00 USD | `+3.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.78` | 51,900.00 USD | 215.16 USD | 0.00 USD | `+3.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 52,290.00 USD | 388.12 USD | 0.00 USD | `+3.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.79` | 53,000.00 USD | 711.78 USD | 0.00 USD | `+3.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.80` | 71,180.00 USD | 18,170.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.82` | 73,210.00 USD | 2,030.00 USD | 0.00 USD | `+4.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.84` | 73,450.00 USD | 243.40 USD | 0.00 USD | `+4.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.85` | 73,620.00 USD | 168.05 USD | 0.00 USD | `+4.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.86` | 73,960.00 USD | 339.94 USD | 0.00 USD | `+4.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.87` | 74,270.00 USD | 310.98 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 74,380.00 USD | 110.58 USD | 0.00 USD | `+4.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.88` | 75,240.00 USD | 860.96 USD | 0.00 USD | `+4.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.89` | 77,170.00 USD | 1,930.00 USD | 0.00 USD | `+5.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.90` | 77,960.00 USD | 788.72 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.91` | 79,770.00 USD | 1,800.00 USD | 0.00 USD | `+5.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.93` | 79,930.00 USD | 163.33 USD | 0.00 USD | `+5.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.94` | 80,710.00 USD | 782.17 USD | 0.00 USD | `+5.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.95` | 80,940.00 USD | 223.62 USD | 0.00 USD | `+5.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 618,240.00 USD | 537,310.00 USD | 0.00 USD | `+5.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.96` | 618,650.00 USD | 401.63 USD | 0.00 USD | `+5.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.97` | 933,800.00 USD | 315,150.00 USD | 0.00 USD | `+5.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `8.99` | 934,140.00 USD | 338.30 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.01` | 934,400.00 USD | 260.96 USD | 0.00 USD | `+6.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.02` | 935,770.00 USD | 1,380.00 USD | 0.00 USD | `+6.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.03` | 936,860.00 USD | 1,090.00 USD | 0.00 USD | `+6.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 937,480.00 USD | 616.37 USD | 0.00 USD | `+6.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.04` | 937,580.00 USD | 102.03 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.05` | 938,030.00 USD | 453.84 USD | 0.00 USD | `+6.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.06` | 938,200.00 USD | 160.99 USD | 0.00 USD | `+7.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.07` | 938,410.00 USD | 215.98 USD | 0.00 USD | `+7.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.09` | 939,920.00 USD | 1,510.00 USD | 0.00 USD | `+7.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.10` | 940,370.00 USD | 451.48 USD | 0.00 USD | `+7.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.11` | 940,510.00 USD | 139.58 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 941,800.00 USD | 1,290.00 USD | 0.00 USD | `+7.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.12` | 941,970.00 USD | 166.53 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.14` | 943,970.00 USD | 2,000.00 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.15` | 1,340,000.00 USD | 394,210.00 USD | 0.00 USD | `+8.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.16` | 1,340,000.00 USD | 119.24 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,340,000.00 USD | 3,020.00 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.21` | 1,340,000.00 USD | 131.87 USD | 0.00 USD | `+8.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.22` | 1,340,000.00 USD | 149.17 USD | 0.00 USD | `+8.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.23` | 1,340,000.00 USD | 2,220.00 USD | 0.00 USD | `+9.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.26` | 1,580,000.00 USD | 231,380.00 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.28` | 1,580,000.00 USD | 1,960.00 USD | 0.00 USD | `+9.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.29` | 1,580,000.00 USD | 434.45 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.30` | 1,600,000.00 USD | 18,610.00 USD | 0.00 USD | `+9.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.31` | 1,600,000.00 USD | 166.83 USD | 0.00 USD | `+10.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.32` | 1,600,000.00 USD | 674.29 USD | 0.00 USD | `+10.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.35` | 1,600,000.00 USD | 101.58 USD | 0.00 USD | `+10.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.36` | 1,600,000.00 USD | 109.36 USD | 0.00 USD | `+10.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.37` | 1,600,000.00 USD | 116.69 USD | 0.00 USD | `+10.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,600,000.00 USD | 163.41 USD | 0.00 USD | `+10.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.38` | 1,600,000.00 USD | 102.01 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.39` | 1,600,000.00 USD | 102.12 USD | 0.00 USD | `+10.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.40` | 1,600,000.00 USD | 714.59 USD | 0.00 USD | `+11.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.41` | 1,600,000.00 USD | 928.13 USD | 0.00 USD | `+11.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.43` | 1,600,000.00 USD | 102.45 USD | 0.00 USD | `+11.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.44` | 1,600,000.00 USD | 219.84 USD | 0.00 USD | `+11.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.45` | 1,600,000.00 USD | 311.69 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.46` | 1,600,000.00 USD | 1,890.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.48` | 1,600,000.00 USD | 1,130.00 USD | 0.00 USD | `+12.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.49` | 1,600,000.00 USD | 288.46 USD | 0.00 USD | `+12.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.53` | 1,600,000.00 USD | 119.92 USD | 0.00 USD | `+12.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.59` | 1,600,000.00 USD | 231.00 USD | 0.00 USD | `+13.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.60` | 1,600,000.00 USD | 221.07 USD | 0.00 USD | `+13.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.61` | 1,600,000.00 USD | 992.00 USD | 0.00 USD | `+13.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.63` | 1,610,000.00 USD | 148.48 USD | 0.00 USD | `+13.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.65` | 1,610,000.00 USD | 191.36 USD | 0.00 USD | `+14.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.69` | 1,610,000.00 USD | 4,440.00 USD | 0.00 USD | `+14.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.71` | 1,610,000.00 USD | 108.21 USD | 0.00 USD | `+14.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.73` | 1,610,000.00 USD | 169.68 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.74` | 1,610,000.00 USD | 574.66 USD | 0.00 USD | `+15.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.77` | 1,610,000.00 USD | 121.87 USD | 0.00 USD | `+15.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.85` | 1,610,000.00 USD | 115.88 USD | 0.00 USD | `+16.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.87` | 1,610,000.00 USD | 340.05 USD | 0.00 USD | `+16.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.89` | 1,610,000.00 USD | 742.12 USD | 0.00 USD | `+16.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.90` | 1,610,000.00 USD | 899.47 USD | 0.00 USD | `+16.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.91` | 1,680,000.00 USD | 70,020.00 USD | 0.00 USD | `+17.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `9.93` | 1,680,000.00 USD | 373.97 USD | 0.00 USD | `+17.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.01` | 1,690,000.00 USD | 5,050.00 USD | 0.00 USD | `+18.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.06` | 1,690,000.00 USD | 6,370.00 USD | 0.00 USD | `+18.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.11` | 1,690,000.00 USD | 404.20 USD | 0.00 USD | `+19.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 210,980.00 USD | 0.00 USD | `+19.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.12` | 1,910,000.00 USD | 1,150.00 USD | 0.00 USD | `+19.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.21` | 1,910,000.00 USD | 172.16 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.29` | 1,910,000.00 USD | 922.87 USD | 0.00 USD | `+21.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.32` | 1,910,000.00 USD | 489.40 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.37` | 1,910,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.43` | 1,910,000.00 USD | 118.01 USD | 0.00 USD | `+23.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.46` | 1,910,000.00 USD | 971.48 USD | 0.00 USD | `+23.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.47` | 1,910,000.00 USD | 818.31 USD | 0.00 USD | `+23.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.51` | 1,910,000.00 USD | 312.31 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.52` | 1,910,000.00 USD | 2,290.00 USD | 0.00 USD | `+24.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.53` | 1,920,000.00 USD | 1,890.00 USD | 0.00 USD | `+24.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.59` | 1,920,000.00 USD | 178.46 USD | 0.00 USD | `+25.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.72` | 1,920,000.00 USD | 173.42 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.73` | 1,920,000.00 USD | 184.75 USD | 0.00 USD | `+26.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.79` | 1,920,000.00 USD | 135.78 USD | 0.00 USD | `+27.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.84` | 1,920,000.00 USD | 127.96 USD | 0.00 USD | `+27.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.88` | 1,920,000.00 USD | 476.43 USD | 0.00 USD | `+28.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.90` | 1,920,000.00 USD | 869.35 USD | 0.00 USD | `+28.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.91` | 1,950,000.00 USD | 35,110.00 USD | 0.00 USD | `+28.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.93` | 1,950,000.00 USD | 251.06 USD | 0.00 USD | `+29.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `10.94` | 1,950,000.00 USD | 552.44 USD | 0.00 USD | `+29.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.01` | 1,950,000.00 USD | 537.26 USD | 0.00 USD | `+29.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.11` | 1,960,000.00 USD | 1,110.00 USD | 0.00 USD | `+31.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.12` | 1,960,000.00 USD | 320.29 USD | 0.00 USD | `+31.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.18` | 1,960,000.00 USD | 1,100.00 USD | 0.00 USD | `+31.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.21` | 1,960,000.00 USD | 2,270.00 USD | 0.00 USD | `+32.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.26` | 1,960,000.00 USD | 1,270.00 USD | 0.00 USD | `+32.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.36` | 1,960,000.00 USD | 1,380.00 USD | 0.00 USD | `+34.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.40` | 1,960,000.00 USD | 2,410.00 USD | 0.00 USD | `+34.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.46` | 1,980,000.00 USD | 10,640.00 USD | 0.00 USD | `+35.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.48` | 1,980,000.00 USD | 2,050.00 USD | 0.00 USD | `+35.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.51` | 1,980,000.00 USD | 529.11 USD | 0.00 USD | `+35.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.60` | 1,990,000.00 USD | 7,700.00 USD | 0.00 USD | `+36.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.82` | 1,990,000.00 USD | 906.03 USD | 0.00 USD | `+39.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.87` | 1,990,000.00 USD | 434.61 USD | 0.00 USD | `+40.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `11.88` | 1,990,000.00 USD | 163.52 USD | 0.00 USD | `+40.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.01` | 2,000,000.00 USD | 10,370.00 USD | 0.00 USD | `+41.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.19` | 2,000,000.00 USD | 5,270.00 USD | 0.00 USD | `+43.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.28` | 2,000,000.00 USD | 115.02 USD | 0.00 USD | `+44.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.71` | 2,010,000.00 USD | 3,870.00 USD | 0.00 USD | `+50.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.80` | 2,010,000.00 USD | 197.97 USD | 0.00 USD | `+51.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.90` | 2,010,000.00 USD | 3,200.00 USD | 0.00 USD | `+52.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `12.98` | 2,010,000.00 USD | 179.58 USD | 0.00 USD | `+53.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.01` | 2,010,000.00 USD | 568.45 USD | 0.00 USD | `+53.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.13` | 2,010,000.00 USD | 169.57 USD | 0.00 USD | `+55.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.37` | 2,010,000.00 USD | 446.52 USD | 0.00 USD | `+57.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.48` | 2,020,000.00 USD | 5,320.00 USD | 0.00 USD | `+59.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.51` | 2,230,000.00 USD | 210,750.00 USD | 0.00 USD | `+59.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.69` | 2,230,000.00 USD | 407.95 USD | 0.00 USD | `+61.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `13.80` | 2,230,000.00 USD | 174.91 USD | 0.00 USD | `+63.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.01` | 2,230,000.00 USD | 4,680.00 USD | 0.00 USD | `+65.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.21` | 2,230,000.00 USD | 960.26 USD | 0.00 USD | `+67.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.36` | 2,240,000.00 USD | 2,710.00 USD | 0.00 USD | `+69.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.51` | 2,240,000.00 USD | 805.90 USD | 0.00 USD | `+71.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.71` | 2,240,000.00 USD | 655.55 USD | 0.00 USD | `+73.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.79` | 2,240,000.00 USD | 4,890.00 USD | 0.00 USD | `+74.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.88` | 2,240,000.00 USD | 471.09 USD | 0.00 USD | `+75.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `14.96` | 2,240,000.00 USD | 383.85 USD | 0.00 USD | `+76.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.01` | 2,900,000.00 USD | 653,420.00 USD | 0.00 USD | `+77.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.06` | 2,900,000.00 USD | 1,510.00 USD | 0.00 USD | `+77.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `15.85` | 2,900,000.00 USD | 111.87 USD | 0.00 USD | `+87.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `16.00` | 2,900,000.00 USD | 219.91 USD | 0.00 USD | `+89.01%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `7.14` | 6,420,000.00 USD | 0.00 USD | 6,420,000.00 USD | 45,760.00 USD | 20,580.00 USD | 41,370.00 USD |
| `7D` | `7.16` | 6,310,000.00 USD | 0.00 USD | 6,310,000.00 USD | 29,500.00 USD | 4,260.00 USD | 21,790.00 USD |
| `7D` | `7.18` | 6,260,000.00 USD | 0.00 USD | 6,260,000.00 USD | 5,030.00 USD | 3,780.00 USD | 19,770.00 USD |
| `7D` | `7.20` | 6,230,000.00 USD | 0.00 USD | 6,230,000.00 USD | 11,960.00 USD | 7,300.00 USD | 2,250.00 USD |
| `7D` | `7.22` | 6,200,000.00 USD | 0.00 USD | 6,200,000.00 USD | 12,260.00 USD | 6,540.00 USD | 6,900.00 USD |
| `7D` | `7.24` | 6,180,000.00 USD | 0.00 USD | 6,180,000.00 USD | 39,910.00 USD | 0.00 USD | 10,600.00 USD |
| `7D` | `7.26` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 0.00 USD | 1,810.00 USD | 38.95 USD |
| `7D` | `7.28` | 6,130,000.00 USD | 0.00 USD | 6,130,000.00 USD | 7,520.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.30` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 4,770.00 USD |
| `7D` | `7.32` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 0.00 USD | 0.00 USD | 6,150.00 USD |
| `7D` | `7.36` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 983.83 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.38` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 46,040.00 USD | 0.00 USD | 503.12 USD |
| `7D` | `7.40` | 6,060,000.00 USD | 0.00 USD | 6,060,000.00 USD | 44,790.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.42` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 457.98 USD |
| `7D` | `7.46` | 6,020,000.00 USD | 0.00 USD | 6,020,000.00 USD | 0.00 USD | 0.00 USD | 23,950.00 USD |
| `7D` | `7.48` | 5,990,000.00 USD | 0.00 USD | 5,990,000.00 USD | 0.00 USD | 0.00 USD | 20,570.00 USD |
| `7D` | `7.50` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 570.66 USD |
| `7D` | `7.52` | 5,970,000.00 USD | 0.00 USD | 5,970,000.00 USD | 3,220.00 USD | 14,470.00 USD | 18,280.00 USD |
| `7D` | `7.54` | 5,930,000.00 USD | 0.00 USD | 5,930,000.00 USD | 34,840.00 USD | 4,450.00 USD | 0.00 USD |
| `7D` | `7.56` | 5,900,000.00 USD | 0.00 USD | 5,900,000.00 USD | 20,150.00 USD | 4,310.00 USD | 301.55 USD |
| `7D` | `7.58` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 609.73 USD |
| `1D` | `7.59` | 5,100,000.00 USD | 0.00 USD | 5,100,000.00 USD | 1,390.00 USD | 0.00 USD | 7,310.00 USD |
| `1D` | `7.60` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 706.40 USD | 4,900.00 USD | 0.00 USD |
| `1D` | `7.61` | 5,090,000.00 USD | 0.00 USD | 5,090,000.00 USD | 2,750.00 USD | 1,250.00 USD | 11,600.00 USD |
| `1D` | `7.62` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 3,270.00 USD | 1,330.00 USD | 286.32 USD |
| `7D` | `7.62` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 0.00 USD | 2,130.00 USD | 547.66 USD |
| `1D` | `7.63` | 5,070,000.00 USD | 0.00 USD | 5,070,000.00 USD | 1,040.00 USD | 0.00 USD | 9,640.00 USD |
| `1D` | `7.64` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 33,010.00 USD | 812.96 USD | 2,480.00 USD |
| `7D` | `7.64` | 5,870,000.00 USD | 0.00 USD | 5,870,000.00 USD | 41,300.00 USD | 0.00 USD | 761.26 USD |
| `1D` | `7.65` | 5,020,000.00 USD | 0.00 USD | 5,020,000.00 USD | 0.00 USD | 817.75 USD | 9,610.00 USD |
| `1D` | `7.66` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 3,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `7.66` | 5,830,000.00 USD | 0.00 USD | 5,830,000.00 USD | 4,870.00 USD | 2,350.00 USD | 24,420.00 USD |
| `1D` | `7.67` | 5,010,000.00 USD | 0.00 USD | 5,010,000.00 USD | 1,140.00 USD | 587.20 USD | 401.01 USD |
| `1D` | `7.68` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 892.30 USD | 0.00 USD | 3,670.00 USD |
| `7D` | `7.68` | 5,790,000.00 USD | 0.00 USD | 5,790,000.00 USD | 0.00 USD | 0.00 USD | 9,280.00 USD |
| `1D` | `7.69` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 0.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `7.70` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 4,140.00 USD | 2,390.00 USD | 17,390.00 USD |
| `7D` | `7.70` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 393.33 USD | 0.00 USD | 686.63 USD |
| `1D` | `7.71` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 660.12 USD | 5,040.00 USD | 7,650.00 USD |
| `1D` | `7.72` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 701.68 USD | 568.00 USD | 2,390.00 USD |
| `7D` | `7.72` | 5,780,000.00 USD | 0.00 USD | 5,780,000.00 USD | 38,970.00 USD | 0.00 USD | 41,000.00 USD |
| `1D` | `7.73` | 4,960,000.00 USD | 0.00 USD | 4,960,000.00 USD | 4,120.00 USD | 1,240.00 USD | 5,600.00 USD |
| `1D` | `7.74` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 16,520.00 USD | 0.00 USD | 50.97 USD |
| `7D` | `7.74` | 5,700,000.00 USD | 0.00 USD | 5,700,000.00 USD | 30,110.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `7.75` | 4,930,000.00 USD | 0.00 USD | 4,930,000.00 USD | 900.06 USD | 6,210.00 USD | 8,050.00 USD |
| `1D` | `7.76` | 4,920,000.00 USD | 0.00 USD | 4,920,000.00 USD | 458.75 USD | 494.12 USD | 15.98 USD |
| `7D` | `7.76` | 5,670,000.00 USD | 0.00 USD | 5,670,000.00 USD | 812.95 USD | 13,360.00 USD | 11,090.00 USD |
| `1D` | `7.77` | 4,910,000.00 USD | 0.00 USD | 4,910,000.00 USD | 13,020.00 USD | 689.91 USD | 3,400.00 USD |
| `1D` | `7.78` | 4,900,000.00 USD | 0.00 USD | 4,900,000.00 USD | 2,730.00 USD | 6,250.00 USD | 0.00 USD |
| `7D` | `7.78` | 5,650,000.00 USD | 0.00 USD | 5,650,000.00 USD | 46,570.00 USD | 7,520.00 USD | 28,030.00 USD |
| `1D` | `7.79` | 4,890,000.00 USD | 0.00 USD | 4,890,000.00 USD | 18,960.00 USD | 2,920.00 USD | 6,900.00 USD |
| `1D` | `7.80` | 4,860,000.00 USD | 0.00 USD | 4,860,000.00 USD | 4,920.00 USD | 7,910.00 USD | 111.29 USD |
| `7D` | `7.80` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 46,450.00 USD | 12,980.00 USD | 1,010.00 USD |
| `1D` | `7.81` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 349.70 USD | 0.00 USD | 321.73 USD |
| `1D` | `7.82` | 4,850,000.00 USD | 0.00 USD | 4,850,000.00 USD | 248.67 USD | 1,680.00 USD | 137.41 USD |
| `7D` | `7.82` | 5,510,000.00 USD | 0.00 USD | 5,510,000.00 USD | 1,450.00 USD | 5,260.00 USD | 5,140.00 USD |
| `1D` | `7.83` | 4,840,000.00 USD | 0.00 USD | 4,840,000.00 USD | 27,230.00 USD | 6,330.00 USD | 0.00 USD |
| `1D` | `7.84` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 1,060.00 USD | 1,800.00 USD | 574.12 USD |
| `7D` | `7.84` | 5,490,000.00 USD | 0.00 USD | 5,490,000.00 USD | 32,340.00 USD | 2,380.00 USD | 26,820.00 USD |
| `1D` | `7.85` | 4,810,000.00 USD | 0.00 USD | 4,810,000.00 USD | 5,210.00 USD | 1,250.00 USD | 3,170.00 USD |
| `1D` | `7.86` | 4,800,000.00 USD | 0.00 USD | 4,800,000.00 USD | 3,110.00 USD | 6,690.00 USD | 17,160.00 USD |
| `7D` | `7.86` | 5,430,000.00 USD | 0.00 USD | 5,430,000.00 USD | 137,360.00 USD | 5,460.00 USD | 17,740.00 USD |
| `1D` | `7.87` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 13,700.00 USD | 10,860.00 USD | 23,050.00 USD |
| `1D` | `7.88` | 4,720,000.00 USD | 0.00 USD | 4,720,000.00 USD | 161,670.00 USD | 5,030.00 USD | 33,750.00 USD |
| `7D` | `7.88` | 5,270,000.00 USD | 0.00 USD | 5,270,000.00 USD | 170,100.00 USD | 12,780.00 USD | 29,320.00 USD |
| `1D` | `7.89` | 4,520,000.00 USD | 0.00 USD | 4,520,000.00 USD | 59,740.00 USD | 3,720.00 USD | 26,790.00 USD |
| `1D` | `7.90` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 56,130.00 USD | 6,970.00 USD | 6,000.00 USD |
| `7D` | `7.90` | 5,060,000.00 USD | 0.00 USD | 5,060,000.00 USD | 33,680.00 USD | 12,890.00 USD | 18,600.00 USD |
| `1D` | `7.91` | 4,360,000.00 USD | 0.00 USD | 4,360,000.00 USD | 14,180.00 USD | 10,370.00 USD | 28,300.00 USD |
| `1D` | `7.92` | 4,310,000.00 USD | 0.00 USD | 4,310,000.00 USD | 15,980.00 USD | 2,950.00 USD | 8,770.00 USD |
| `7D` | `7.92` | 4,990,000.00 USD | 0.00 USD | 4,990,000.00 USD | 55,490.00 USD | 23,630.00 USD | 40,540.00 USD |
| `1D` | `7.93` | 4,280,000.00 USD | 0.00 USD | 4,280,000.00 USD | 7,960.00 USD | 6,570.00 USD | 4,570.00 USD |
| `1D` | `7.94` | 4,260,000.00 USD | 0.00 USD | 4,260,000.00 USD | 17,720.00 USD | 20,510.00 USD | 61,880.00 USD |
| `7D` | `7.94` | 4,870,000.00 USD | 0.00 USD | 4,870,000.00 USD | 51,390.00 USD | 9,960.00 USD | 33,210.00 USD |
| `1D` | `7.95` | 4,160,000.00 USD | 0.00 USD | 4,160,000.00 USD | 27,800.00 USD | 9,190.00 USD | 87,240.00 USD |
| `1D` | `7.96` | 4,040,000.00 USD | 0.00 USD | 4,040,000.00 USD | 2,970.00 USD | 15,680.00 USD | 62,540.00 USD |
| `7D` | `7.96` | 4,780,000.00 USD | 0.00 USD | 4,780,000.00 USD | 21,840.00 USD | 6,920.00 USD | 87,840.00 USD |
| `1D` | `7.97` | 3,960,000.00 USD | 0.00 USD | 3,960,000.00 USD | 12,860.00 USD | 9,820.00 USD | 4,040.00 USD |
| `1D` | `7.98` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 5,050.00 USD | 2,060.00 USD | 43,440.00 USD |
| `7D` | `7.98` | 4,660,000.00 USD | 0.00 USD | 4,660,000.00 USD | 59,410.00 USD | 26,790.00 USD | 146,400.00 USD |
| `1D` | `7.99` | 3,880,000.00 USD | 0.00 USD | 3,880,000.00 USD | 3,450.00 USD | 10,180.00 USD | 4,730.00 USD |
| `1D` | `8.00` | 3,860,000.00 USD | 0.00 USD | 3,860,000.00 USD | 50,430.00 USD | 8,950.00 USD | 22,080.00 USD |
| `7D` | `8.00` | 4,430,000.00 USD | 0.00 USD | 4,430,000.00 USD | 60,980.00 USD | 16,420.00 USD | 5,080.00 USD |
| `1D` | `8.01` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 6,540.00 USD | 3,750.00 USD | 3,820.00 USD |
| `1D` | `8.02` | 3,770,000.00 USD | 0.00 USD | 3,770,000.00 USD | 75,150.00 USD | 0.00 USD | 114.63 USD |
| `7D` | `8.02` | 4,350,000.00 USD | 0.00 USD | 4,350,000.00 USD | 15,300.00 USD | 46,670.00 USD | 55,530.00 USD |
| `1D` | `8.03` | 3,690,000.00 USD | 0.00 USD | 3,690,000.00 USD | 9,070.00 USD | 12,540.00 USD | 12,890.00 USD |
| `1D` | `8.04` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 49,540.00 USD | 0.00 USD | 10,010.00 USD |
| `7D` | `8.04` | 4,230,000.00 USD | 0.00 USD | 4,230,000.00 USD | 460,990.00 USD | 0.00 USD | 85,870.00 USD |
| `1D` | `8.05` | 3,600,000.00 USD | 0.00 USD | 3,600,000.00 USD | 317,940.00 USD | 6,430.00 USD | 53,840.00 USD |
| `1D` | `8.06` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 155,360.00 USD | 0.00 USD | 66,930.00 USD |
| `7D` | `8.06` | 3,680,000.00 USD | 0.00 USD | 3,680,000.00 USD | 336,530.00 USD | 0.00 USD | 85,640.00 USD |
| `1D` | `8.07` | 3,000,000.00 USD | 0.00 USD | 3,000,000.00 USD | 130,100.00 USD | 9,310.00 USD | 4,540.00 USD |
| `1D` | `8.08` | 2,850,000.00 USD | 0.00 USD | 2,850,000.00 USD | 14,440.00 USD | 0.00 USD | 65,350.00 USD |
| `7D` | `8.08` | 3,260,000.00 USD | 0.00 USD | 3,260,000.00 USD | 5,100.00 USD | 0.00 USD | 74,730.00 USD |
| `1D` | `8.09` | 2,770,000.00 USD | 0.00 USD | 2,770,000.00 USD | 3,110.00 USD | 0.00 USD | 29,350.00 USD |
| `1D` | `8.10` | 2,740,000.00 USD | 0.00 USD | 2,740,000.00 USD | 31,390.00 USD | 6,770.00 USD | 122,470.00 USD |
| `7D` | `8.10` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 56,590.00 USD | 0.00 USD | 14,030.00 USD |
| `1D` | `8.11` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 77,850.00 USD | 0.00 USD | 194,300.00 USD |
| `1D` | `8.12` | 2,310,000.00 USD | 0.00 USD | 2,310,000.00 USD | 19,930.00 USD | 11,230.00 USD | 126,430.00 USD |
| `7D` | `8.12` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 23,240.00 USD | 0.00 USD | 141,990.00 USD |
| `1D` | `8.13` | 2,150,000.00 USD | 0.00 USD | 2,150,000.00 USD | 21,470.00 USD | 8,550.00 USD | 1,810.00 USD |
| `1D` | `8.14` | 2,120,000.00 USD | 0.00 USD | 2,120,000.00 USD | 2,320.00 USD | 8,630.00 USD | 105,300.00 USD |
| `7D` | `8.14` | 2,950,000.00 USD | 0.00 USD | 2,950,000.00 USD | 160,410.00 USD | 30,700.00 USD | 184,370.00 USD |
| `1D` | `8.15` | 2,000,000.00 USD | 0.00 USD | 2,000,000.00 USD | 43,510.00 USD | 12,240.00 USD | 53,620.00 USD |
| `1D` | `8.16` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 192.50 USD | 21,000.00 USD | 165,410.00 USD |
| `7D` | `8.16` | 2,570,000.00 USD | 0.00 USD | 2,570,000.00 USD | 30,670.00 USD | 23,640.00 USD | 14,520.00 USD |
| `1D` | `8.17` | 1,710,000.00 USD | 0.00 USD | 1,710,000.00 USD | 11,100.00 USD | 8,610.00 USD | 183,410.00 USD |
| `1D` | `8.18` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 7,140.00 USD | 1,470.00 USD | 15.88 USD |
| `7D` | `8.18` | 2,500,000.00 USD | 0.00 USD | 2,500,000.00 USD | 1,200.00 USD | 40,090.00 USD | 172,780.00 USD |
| `1D` | `8.19` | 1,490,000.00 USD | 0.00 USD | 1,490,000.00 USD | 18,260.00 USD | 0.00 USD | 15,460.00 USD |
| `1D` | `8.20` | 1,460,000.00 USD | 0.00 USD | 1,460,000.00 USD | 25,900.00 USD | 4,000.00 USD | 11,410.00 USD |
| `7D` | `8.20` | 2,290,000.00 USD | 0.00 USD | 2,290,000.00 USD | 174,220.00 USD | 58,100.00 USD | 0.00 USD |
| `1D` | `8.21` | 1,420,000.00 USD | 0.00 USD | 1,420,000.00 USD | 41,620.00 USD | 1,260.00 USD | 0.00 USD |
| `1D` | `8.22` | 1,380,000.00 USD | 0.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 16,400.00 USD |
| `7D` | `8.22` | 2,060,000.00 USD | 0.00 USD | 2,060,000.00 USD | 0.00 USD | 21,570.00 USD | 0.00 USD |
| `1D` | `8.23` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 0.00 USD | 1,750.00 USD | 2,340.00 USD |
| `1D` | `8.24` | 1,360,000.00 USD | 0.00 USD | 1,360,000.00 USD | 168.44 USD | 3,220.00 USD | 5,970.00 USD |
| `7D` | `8.24` | 2,030,000.00 USD | 0.00 USD | 2,030,000.00 USD | 106,990.00 USD | 18,690.00 USD | 17,610.00 USD |
| `1D` | `8.25` | 1,350,000.00 USD | 0.00 USD | 1,350,000.00 USD | 0.00 USD | 5,000.00 USD | 38,150.00 USD |
| `1D` | `8.26` | 1,300,000.00 USD | 0.00 USD | 1,300,000.00 USD | 50,590.00 USD | 12,510.00 USD | 23,300.00 USD |
| `7D` | `8.26` | 1,890,000.00 USD | 0.00 USD | 1,890,000.00 USD | 100,930.00 USD | 5,750.00 USD | 11,420.00 USD |
| `1D` | `8.27` | 1,220,000.00 USD | 0.00 USD | 1,220,000.00 USD | 13,860.00 USD | 12,270.00 USD | 20,140.00 USD |
| `1D` | `8.28` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 0.00 USD | 13,760.00 USD | 4,290.00 USD |
| `7D` | `8.28` | 1,770,000.00 USD | 0.00 USD | 1,770,000.00 USD | 91,120.00 USD | 4,000.00 USD | 27,120.00 USD |
| `1D` | `8.29` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 39,480.00 USD | 11,800.00 USD | 53.52 USD |
| `1D` | `8.30` | 1,100,000.00 USD | 0.00 USD | 1,100,000.00 USD | 42,390.00 USD | 12,550.00 USD | 20,060.00 USD |
| `7D` | `8.30` | 1,650,000.00 USD | 0.00 USD | 1,650,000.00 USD | 224,520.00 USD | 17,210.00 USD | 21,710.00 USD |
| `1D` | `8.31` | 1,030,000.00 USD | 0.00 USD | 1,030,000.00 USD | 52,050.00 USD | 11,920.00 USD | 56,400.00 USD |
| `1D` | `8.32` | 905,820.00 USD | 0.00 USD | 905,820.00 USD | 73,050.00 USD | 6,080.00 USD | 14,220.00 USD |
| `7D` | `8.32` | 1,390,000.00 USD | 0.00 USD | 1,390,000.00 USD | 220,640.00 USD | 0.00 USD | 1,990.00 USD |
| `1D` | `8.33` | 812,470.00 USD | 0.00 USD | 812,470.00 USD | 0.00 USD | 6,210.00 USD | 21.18 USD |
| `1D` | `8.34` | 806,240.00 USD | 0.00 USD | 806,240.00 USD | 0.00 USD | 2,210.00 USD | 0.00 USD |
| `7D` | `8.34` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 0.00 USD | 11,770.00 USD | 5,080.00 USD |
| `1D` | `8.35` | 804,030.00 USD | 0.00 USD | 804,030.00 USD | 0.00 USD | 19,810.00 USD | 16,990.00 USD |
| `1D` | `8.36` | 767,230.00 USD | 0.00 USD | 767,230.00 USD | 0.00 USD | 0.00 USD | 17,800.00 USD |
| `7D` | `8.36` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 223,170.00 USD | 0.00 USD | 14,290.00 USD |
| `1D` | `8.37` | 749,430.00 USD | 0.00 USD | 749,430.00 USD | 691.75 USD | 14,420.00 USD | 0.00 USD |
| `1D` | `8.38` | 734,320.00 USD | 0.00 USD | 734,320.00 USD | 17,220.00 USD | 5,940.00 USD | 50,240.00 USD |
| `7D` | `8.38` | 909,640.00 USD | 0.00 USD | 909,640.00 USD | 0.00 USD | 0.00 USD | 57,740.00 USD |
| `1D` | `8.39` | 660,920.00 USD | 0.00 USD | 660,920.00 USD | 100,740.00 USD | 13,620.00 USD | 32,610.00 USD |
| `1D` | `8.40` | 513,950.00 USD | 0.00 USD | 513,950.00 USD | 10,500.00 USD | 7,000.00 USD | 56,370.00 USD |
| `7D` | `8.40` | 851,900.00 USD | 0.00 USD | 851,900.00 USD | 0.00 USD | 7,600.00 USD | 86,940.00 USD |
| `1D` | `8.41` | 440,080.00 USD | 0.00 USD | 440,080.00 USD | 0.00 USD | 6,440.00 USD | 11,940.00 USD |
| `1D` | `8.42` | 421,690.00 USD | 0.00 USD | 421,690.00 USD | 0.00 USD | 16,260.00 USD | 43,020.00 USD |
| `7D` | `8.42` | 757,360.00 USD | 0.00 USD | 757,360.00 USD | 209,760.00 USD | 0.00 USD | 35,220.00 USD |
| `1D` | `8.43` | 362,410.00 USD | 0.00 USD | 362,410.00 USD | 81,350.00 USD | 7,730.00 USD | 7,540.00 USD |
| `1D` | `8.44` | 265,790.00 USD | 0.00 USD | 265,790.00 USD | 11,130.00 USD | 32,380.00 USD | 160,690.00 USD |
| `7D` | `8.44` | 512,380.00 USD | 0.00 USD | 512,380.00 USD | 152,190.00 USD | 8,000.00 USD | 76,300.00 USD |
| `1D` | `8.45` | 61,570.00 USD | 0.00 USD | 61,570.00 USD | 54,790.00 USD | 5,970.00 USD | 0.00 USD |
| `7D` | `8.46` | 275,880.00 USD | 0.00 USD | 275,880.00 USD | 152,650.00 USD | 0.00 USD | 123,230.00 USD |
| `1D` | `8.47` | 815.09 USD | 0.00 USD | 815.09 USD | 663.00 USD | 0.00 USD | 152.09 USD |
| `7D` | `8.47` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 749.80 USD | 749.80 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.48` | 1,500.00 USD | 1,500.00 USD | 0.00 USD | 749.80 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.48` | 337,360.00 USD | 337,360.00 USD | 0.00 USD | 144,290.00 USD | 0.00 USD | 193,070.00 USD |
| `7D` | `8.50` | 337,590.00 USD | 337,590.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 223.58 USD |
| `1D` | `8.51` | 174,150.00 USD | 174,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 172,650.00 USD |
| `1D` | `8.52` | 337,770.00 USD | 337,770.00 USD | 0.00 USD | 158,630.00 USD | 0.00 USD | 4,980.00 USD |
| `7D` | `8.52` | 543,210.00 USD | 543,210.00 USD | 0.00 USD | 113,820.00 USD | 0.00 USD | 91,800.00 USD |
| `1D` | `8.53` | 361,950.00 USD | 361,950.00 USD | 0.00 USD | 24,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.54` | 564,750.00 USD | 564,750.00 USD | 0.00 USD | 202,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `8.54` | 902,390.00 USD | 902,390.00 USD | 0.00 USD | 357,740.00 USD | 0.00 USD | 1,440.00 USD |
| `1D` | `8.55` | 591,520.00 USD | 591,520.00 USD | 0.00 USD | 1,650.00 USD | 0.00 USD | 25,120.00 USD |
| `1D` | `8.56` | 630,630.00 USD | 630,630.00 USD | 0.00 USD | 686.73 USD | 38,320.00 USD | 101.23 USD |
| `7D` | `8.56` | 1,170,000.00 USD | 1,170,000.00 USD | 0.00 USD | 144,180.00 USD | 122,650.00 USD | 962.39 USD |
| `1D` | `8.57` | 800,120.00 USD | 800,120.00 USD | 0.00 USD | 169,490.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.58` | 859,420.00 USD | 859,420.00 USD | 0.00 USD | 59,120.00 USD | 0.00 USD | 179.45 USD |
| `7D` | `8.58` | 1,340,000.00 USD | 1,340,000.00 USD | 0.00 USD | 4,370.00 USD | 164,810.00 USD | 0.00 USD |
| `1D` | `8.60` | 861,460.00 USD | 861,460.00 USD | 0.00 USD | 2,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `8.61` | 862,300.00 USD | 862,300.00 USD | 0.00 USD | 497.00 USD | 0.00 USD | 337.70 USD |
| `1D` | `8.62` | 1,030,000.00 USD | 1,030,000.00 USD | 0.00 USD | 41,980.00 USD | 0.00 USD | 124,440.00 USD |
| `7D` | `8.62` | 1,370,000.00 USD | 1,370,000.00 USD | 0.00 USD | 2,810.00 USD | 0.00 USD | 27,760.00 USD |
| `1D` | `8.63` | 1,160,000.00 USD | 1,160,000.00 USD | 0.00 USD | 129,280.00 USD | 2,420.00 USD | 197.20 USD |
| `1D` | `8.64` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 42,390.00 USD | 8,070.00 USD | 3,570.00 USD |
| `7D` | `8.64` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 10,660.00 USD | 0.00 USD |
| `1D` | `8.65` | 1,250,000.00 USD | 1,250,000.00 USD | 0.00 USD | 4,980.00 USD | 9,010.00 USD | 17,300.00 USD |
| `1D` | `8.66` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 6,230.00 USD | 2,020.00 USD | 14,350.00 USD |
| `7D` | `8.66` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,530.00 USD |
| `1D` | `8.67` | 1,280,000.00 USD | 1,280,000.00 USD | 0.00 USD | 880.60 USD | 9,960.00 USD | 395.26 USD |
| `1D` | `8.68` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 588.00 USD | 12,020.00 USD | 25,890.00 USD |
| `7D` | `8.68` | 1,530,000.00 USD | 1,530,000.00 USD | 0.00 USD | 0.00 USD | 30,000.00 USD | 117,630.00 USD |
| `1D` | `8.69` | 1,380,000.00 USD | 1,380,000.00 USD | 0.00 USD | 10,820.00 USD | 19,200.00 USD | 33,840.00 USD |
| `1D` | `8.70` | 1,470,000.00 USD | 1,470,000.00 USD | 0.00 USD | 62,600.00 USD | 0.00 USD | 23,500.00 USD |
| `7D` | `8.70` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 116,370.00 USD | 41,840.00 USD | 46,400.00 USD |
| `1D` | `8.71` | 1,490,000.00 USD | 1,490,000.00 USD | 0.00 USD | 18,700.00 USD | 7,990.00 USD | 0.00 USD |
| `1D` | `8.72` | 1,580,000.00 USD | 1,580,000.00 USD | 0.00 USD | 34,050.00 USD | 2,520.00 USD | 50,540.00 USD |
| `7D` | `8.72` | 1,730,000.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 547.66 USD |
| `1D` | `8.73` | 1,660,000.00 USD | 1,660,000.00 USD | 0.00 USD | 12,580.00 USD | 28,810.00 USD | 32,610.00 USD |
| `1D` | `8.74` | 1,720,000.00 USD | 1,720,000.00 USD | 0.00 USD | 38,500.00 USD | 3,500.00 USD | 17,600.00 USD |
| `7D` | `8.74` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 51,030.00 USD | 30,470.00 USD | 0.00 USD |
| `1D` | `8.75` | 1,770,000.00 USD | 1,770,000.00 USD | 0.00 USD | 33,520.00 USD | 8,970.00 USD | 16,680.00 USD |
| `1D` | `8.76` | 1,920,000.00 USD | 1,920,000.00 USD | 0.00 USD | 82,470.00 USD | 10,010.00 USD | 56,500.00 USD |
| `7D` | `8.76` | 2,070,000.00 USD | 2,070,000.00 USD | 0.00 USD | 196,960.00 USD | 0.00 USD | 58,380.00 USD |
| `1D` | `8.77` | 2,120,000.00 USD | 2,120,000.00 USD | 0.00 USD | 155,740.00 USD | 2,060.00 USD | 43,170.00 USD |
| `1D` | `8.78` | 2,240,000.00 USD | 2,240,000.00 USD | 0.00 USD | 41,500.00 USD | 25,510.00 USD | 50,260.00 USD |
| `7D` | `8.78` | 2,360,000.00 USD | 2,360,000.00 USD | 0.00 USD | 144,010.00 USD | 8,000.00 USD | 133,500.00 USD |
| `1D` | `8.79` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 31,710.00 USD | 17,970.00 USD | 31,300.00 USD |
| `1D` | `8.80` | 2,480,000.00 USD | 2,480,000.00 USD | 0.00 USD | 113,160.00 USD | 19,150.00 USD | 24,260.00 USD |
| `7D` | `8.80` | 2,450,000.00 USD | 2,450,000.00 USD | 0.00 USD | 27,360.00 USD | 33,750.00 USD | 33,400.00 USD |
| `1D` | `8.81` | 2,530,000.00 USD | 2,530,000.00 USD | 0.00 USD | 39,870.00 USD | 8,400.00 USD | 2,000.00 USD |
| `1D` | `8.82` | 2,600,000.00 USD | 2,600,000.00 USD | 0.00 USD | 4,520.00 USD | 4,510.00 USD | 61,900.00 USD |
| `7D` | `8.82` | 2,850,000.00 USD | 2,850,000.00 USD | 0.00 USD | 345,340.00 USD | 18,440.00 USD | 39,340.00 USD |
| `1D` | `8.83` | 2,800,000.00 USD | 2,800,000.00 USD | 0.00 USD | 171,230.00 USD | 19,400.00 USD | 7,220.00 USD |
| `1D` | `8.84` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 1,500.00 USD | 3,110.00 USD | 59,100.00 USD |
| `7D` | `8.84` | 2,860,000.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 5,880.00 USD | 0.00 USD |
| `1D` | `8.85` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 13,040.00 USD | 3,360.00 USD | 10,690.00 USD |
| `1D` | `8.86` | 2,890,000.00 USD | 2,890,000.00 USD | 0.00 USD | 2,060.00 USD | 1,470.00 USD | 0.00 USD |
| `7D` | `8.86` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 29,310.00 USD | 0.00 USD | 81,390.00 USD |
| `1D` | `8.87` | 2,900,000.00 USD | 2,900,000.00 USD | 0.00 USD | 1,410.00 USD | 0.00 USD | 8,900.00 USD |
| `1D` | `8.88` | 2,920,000.00 USD | 2,920,000.00 USD | 0.00 USD | 803.70 USD | 14,670.00 USD | 82.64 USD |
| `7D` | `8.88` | 3,000,000.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 28,570.00 USD |
| `1D` | `8.89` | 2,970,000.00 USD | 2,970,000.00 USD | 0.00 USD | 12,390.00 USD | 3,410.00 USD | 32,960.00 USD |
| `1D` | `8.90` | 3,090,000.00 USD | 3,090,000.00 USD | 0.00 USD | 28,690.00 USD | 5,990.00 USD | 84,510.00 USD |
| `7D` | `8.90` | 3,120,000.00 USD | 3,120,000.00 USD | 0.00 USD | 2,440.00 USD | 0.00 USD | 115,480.00 USD |
| `1D` | `8.91` | 3,150,000.00 USD | 3,150,000.00 USD | 0.00 USD | 32,240.00 USD | 11,620.00 USD | 15,860.00 USD |
| `1D` | `8.92` | 3,160,000.00 USD | 3,160,000.00 USD | 0.00 USD | 1,110.00 USD | 3,220.00 USD | 6,080.00 USD |
| `7D` | `8.92` | 3,250,000.00 USD | 3,250,000.00 USD | 0.00 USD | 99,150.00 USD | 0.00 USD | 35,230.00 USD |
| `1D` | `8.93` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 31,830.00 USD | 6,810.00 USD | 39,110.00 USD |
| `1D` | `8.94` | 3,300,000.00 USD | 3,300,000.00 USD | 0.00 USD | 50,590.00 USD | 12,260.00 USD | 3,910.00 USD |
| `7D` | `8.94` | 3,390,000.00 USD | 3,390,000.00 USD | 0.00 USD | 129,180.00 USD | 0.00 USD | 13,460.00 USD |
| `1D` | `8.95` | 3,330,000.00 USD | 3,330,000.00 USD | 0.00 USD | 2,540.00 USD | 6,630.00 USD | 20,480.00 USD |
| `1D` | `8.96` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 1,260.00 USD | 2,980.00 USD | 481.46 USD |
| `7D` | `8.96` | 3,430,000.00 USD | 3,430,000.00 USD | 0.00 USD | 3,320.00 USD | 4,000.00 USD | 26,790.00 USD |
| `1D` | `8.97` | 3,340,000.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 152.79 USD |
| `1D` | `8.98` | 3,400,000.00 USD | 3,400,000.00 USD | 0.00 USD | 35,320.00 USD | 9,420.00 USD | 19,790.00 USD |
| `7D` | `8.98` | 3,440,000.00 USD | 3,440,000.00 USD | 0.00 USD | 1,180.00 USD | 0.00 USD | 9,090.00 USD |
| `1D` | `8.99` | 3,470,000.00 USD | 3,470,000.00 USD | 0.00 USD | 48,380.00 USD | 22,110.00 USD | 3,120.00 USD |
| `1D` | `9.00` | 3,540,000.00 USD | 3,540,000.00 USD | 0.00 USD | 36,960.00 USD | 0.00 USD | 24,740.00 USD |
| `7D` | `9.00` | 3,870,000.00 USD | 3,870,000.00 USD | 0.00 USD | 370,780.00 USD | 17,920.00 USD | 40,730.00 USD |
| `1D` | `9.01` | 3,620,000.00 USD | 3,620,000.00 USD | 0.00 USD | 49,510.00 USD | 14,940.00 USD | 15,830.00 USD |
| `1D` | `9.02` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 39,170.00 USD | 29,440.00 USD | 4,930.00 USD |
| `7D` | `9.02` | 4,010,000.00 USD | 4,010,000.00 USD | 0.00 USD | 82,280.00 USD | 56,120.00 USD | 1,300.00 USD |
| `1D` | `9.03` | 3,860,000.00 USD | 3,860,000.00 USD | 0.00 USD | 125,760.00 USD | 10,300.00 USD | 34,070.00 USD |
| `1D` | `9.04` | 3,920,000.00 USD | 3,920,000.00 USD | 0.00 USD | 41,220.00 USD | 5,900.00 USD | 14,790.00 USD |
| `7D` | `9.04` | 4,240,000.00 USD | 4,240,000.00 USD | 0.00 USD | 136,520.00 USD | 74,750.00 USD | 15,490.00 USD |
| `1D` | `9.05` | 3,980,000.00 USD | 3,980,000.00 USD | 0.00 USD | 21,980.00 USD | 9,980.00 USD | 24,040.00 USD |
| `1D` | `9.06` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 28,180.00 USD | 6,890.00 USD | 10,340.00 USD |
| `7D` | `9.06` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 7,440.00 USD | 14,960.00 USD | 53,770.00 USD |
| `1D` | `9.07` | 4,080,000.00 USD | 4,080,000.00 USD | 0.00 USD | 13,070.00 USD | 18,070.00 USD | 28,540.00 USD |
| `1D` | `9.08` | 4,130,000.00 USD | 4,130,000.00 USD | 0.00 USD | 12,960.00 USD | 2,110.00 USD | 34,130.00 USD |
| `7D` | `9.08` | 4,390,000.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 11,960.00 USD | 65,690.00 USD |
| `1D` | `9.09` | 4,250,000.00 USD | 4,250,000.00 USD | 0.00 USD | 82,070.00 USD | 9,730.00 USD | 27,800.00 USD |
| `1D` | `9.10` | 4,310,000.00 USD | 4,310,000.00 USD | 0.00 USD | 16,320.00 USD | 12,520.00 USD | 34,200.00 USD |
| `7D` | `9.10` | 5,590,000.00 USD | 5,590,000.00 USD | 0.00 USD | 826,500.00 USD | 35,760.00 USD | 334,340.00 USD |
| `1D` | `9.11` | 4,470,000.00 USD | 4,470,000.00 USD | 0.00 USD | 60,160.00 USD | 14,420.00 USD | 82,390.00 USD |
| `1D` | `9.12` | 4,620,000.00 USD | 4,620,000.00 USD | 0.00 USD | 101,900.00 USD | 22,410.00 USD | 26,490.00 USD |
| `7D` | `9.12` | 6,580,000.00 USD | 6,580,000.00 USD | 0.00 USD | 466,670.00 USD | 24,170.00 USD | 503,360.00 USD |
| `1D` | `9.13` | 4,750,000.00 USD | 4,750,000.00 USD | 0.00 USD | 75,260.00 USD | 15,960.00 USD | 40,170.00 USD |
| `1D` | `9.14` | 4,820,000.00 USD | 4,820,000.00 USD | 0.00 USD | 30,520.00 USD | 3,380.00 USD | 29,600.00 USD |
| `7D` | `9.14` | 7,640,000.00 USD | 7,640,000.00 USD | 0.00 USD | 536,560.00 USD | 18,540.00 USD | 500,720.00 USD |
| `1D` | `9.15` | 4,920,000.00 USD | 4,920,000.00 USD | 0.00 USD | 57,140.00 USD | 23,170.00 USD | 22,990.00 USD |
| `1D` | `9.16` | 5,040,000.00 USD | 5,040,000.00 USD | 0.00 USD | 63,930.00 USD | 23,900.00 USD | 32,520.00 USD |
| `7D` | `9.16` | 8,230,000.00 USD | 8,230,000.00 USD | 0.00 USD | 358,370.00 USD | 44,360.00 USD | 196,390.00 USD |
| `1D` | `9.17` | 5,170,000.00 USD | 5,170,000.00 USD | 0.00 USD | 80,160.00 USD | 3,200.00 USD | 49,590.00 USD |
| `1D` | `9.18` | 5,260,000.00 USD | 5,260,000.00 USD | 0.00 USD | 28,310.00 USD | 26,430.00 USD | 31,180.00 USD |
| `7D` | `9.18` | 9,260,000.00 USD | 9,260,000.00 USD | 0.00 USD | 566,340.00 USD | 162,460.00 USD | 292,060.00 USD |
| `1D` | `9.19` | 5,370,000.00 USD | 5,370,000.00 USD | 0.00 USD | 78,040.00 USD | 29,140.00 USD | 7,620.00 USD |
| `1D` | `9.20` | 5,490,000.00 USD | 5,490,000.00 USD | 0.00 USD | 64,910.00 USD | 11,090.00 USD | 37,680.00 USD |
| `7D` | `9.20` | 10,180,000.00 USD | 10,180,000.00 USD | 0.00 USD | 550,150.00 USD | 134,550.00 USD | 237,080.00 USD |
| `1D` | `9.21` | 5,530,000.00 USD | 5,530,000.00 USD | 0.00 USD | 30,000.00 USD | 2,950.00 USD | 4,620.00 USD |
| `1D` | `9.22` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 58,470.00 USD | 2,850.00 USD | 11,180.00 USD |
| `7D` | `9.22` | 11,320,000.00 USD | 11,320,000.00 USD | 0.00 USD | 620,010.00 USD | 144,840.00 USD | 379,180.00 USD |
| `1D` | `9.23` | 5,600,000.00 USD | 5,600,000.00 USD | 0.00 USD | 471.32 USD | 4,270.00 USD | 34.98 USD |
| `1D` | `9.24` | 5,650,000.00 USD | 5,650,000.00 USD | 0.00 USD | 45,890.00 USD | 0.00 USD | 3,140.00 USD |
| `7D` | `9.24` | 11,840,000.00 USD | 11,840,000.00 USD | 0.00 USD | 336,360.00 USD | 44,660.00 USD | 135,140.00 USD |
| `1D` | `9.25` | 5,680,000.00 USD | 5,680,000.00 USD | 0.00 USD | 17,240.00 USD | 5,840.00 USD | 9,680.00 USD |
| `1D` | `9.26` | 5,690,000.00 USD | 5,690,000.00 USD | 0.00 USD | 574.60 USD | 0.00 USD | 3,410.00 USD |
| `7D` | `9.26` | 12,230,000.00 USD | 12,230,000.00 USD | 0.00 USD | 273,920.00 USD | 96,980.00 USD | 21,230.00 USD |
| `1D` | `9.27` | 5,720,000.00 USD | 5,720,000.00 USD | 0.00 USD | 23,430.00 USD | 1,360.00 USD | 6,470.00 USD |
| `1D` | `9.28` | 5,730,000.00 USD | 5,730,000.00 USD | 0.00 USD | 1,610.00 USD | 8,760.00 USD | 10.22 USD |
| `7D` | `9.28` | 12,860,000.00 USD | 12,860,000.00 USD | 0.00 USD | 428,160.00 USD | 69,460.00 USD | 136,770.00 USD |
| `1D` | `9.29` | 5,770,000.00 USD | 5,770,000.00 USD | 0.00 USD | 16,190.00 USD | 4,140.00 USD | 17,930.00 USD |
| `1D` | `9.30` | 5,830,000.00 USD | 5,830,000.00 USD | 0.00 USD | 39,880.00 USD | 7,520.00 USD | 11,640.00 USD |
| `7D` | `9.30` | 13,400,000.00 USD | 13,400,000.00 USD | 0.00 USD | 199,810.00 USD | 97,780.00 USD | 233,540.00 USD |
| `1D` | `9.31` | 5,880,000.00 USD | 5,880,000.00 USD | 0.00 USD | 28,930.00 USD | 5,500.00 USD | 12,900.00 USD |
| `1D` | `9.32` | 5,890,000.00 USD | 5,890,000.00 USD | 0.00 USD | 11,960.00 USD | 1,330.00 USD | 5,090.00 USD |
| `7D` | `9.32` | 14,000,000.00 USD | 14,000,000.00 USD | 0.00 USD | 241,960.00 USD | 51,970.00 USD | 308,180.00 USD |
| `1D` | `9.33` | 5,920,000.00 USD | 5,920,000.00 USD | 0.00 USD | 7,820.00 USD | 6,000.00 USD | 9,640.00 USD |
| `1D` | `9.34` | 5,970,000.00 USD | 5,970,000.00 USD | 0.00 USD | 46,210.00 USD | 3,660.00 USD | 5,530.00 USD |
| `7D` | `9.34` | 14,200,000.00 USD | 14,200,000.00 USD | 0.00 USD | 98,640.00 USD | 41,250.00 USD | 59,820.00 USD |
| `1D` | `9.35` | 6,000,000.00 USD | 6,000,000.00 USD | 0.00 USD | 13,620.00 USD | 817.75 USD | 15,020.00 USD |
| `1D` | `9.36` | 6,020,000.00 USD | 6,020,000.00 USD | 0.00 USD | 4,730.00 USD | 6,760.00 USD | 7,950.00 USD |
| `7D` | `9.36` | 14,570,000.00 USD | 14,570,000.00 USD | 0.00 USD | 215,620.00 USD | 64,120.00 USD | 97,570.00 USD |
| `1D` | `9.37` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 12,900.00 USD | 6,260.00 USD | 2,740.00 USD |
| `1D` | `9.38` | 6,070,000.00 USD | 6,070,000.00 USD | 0.00 USD | 15,290.00 USD | 0.00 USD | 13,890.00 USD |
| `7D` | `9.38` | 14,910,000.00 USD | 14,910,000.00 USD | 0.00 USD | 224,850.00 USD | 31,100.00 USD | 77,240.00 USD |
| `1D` | `9.39` | 6,080,000.00 USD | 6,080,000.00 USD | 0.00 USD | 7,470.00 USD | 1,600.00 USD | 0.00 USD |
| `1D` | `9.40` | 6,100,000.00 USD | 6,100,000.00 USD | 0.00 USD | 21,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `9.40` | 15,290,000.00 USD | 15,290,000.00 USD | 0.00 USD | 234,760.00 USD | 42,520.00 USD | 103,930.00 USD |
| `1D` | `9.41` | 6,120,000.00 USD | 6,120,000.00 USD | 0.00 USD | 3,440.00 USD | 0.00 USD | 10,110.00 USD |
| `7D` | `9.42` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 109,230.00 USD | 13,910.00 USD | 52,280.00 USD |
| `7D` | `9.44` | 15,610,000.00 USD | 15,610,000.00 USD | 0.00 USD | 80,230.00 USD | 19,420.00 USD | 44,640.00 USD |
| `7D` | `9.46` | 15,700,000.00 USD | 15,700,000.00 USD | 0.00 USD | 89,160.00 USD | 0.00 USD | 1,950.00 USD |
| `7D` | `9.48` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 10,620.00 USD | 11,060.00 USD | 20,710.00 USD |
| `7D` | `9.50` | 15,870,000.00 USD | 15,870,000.00 USD | 0.00 USD | 65,230.00 USD | 12,050.00 USD | 53,180.00 USD |
| `7D` | `9.52` | 15,980,000.00 USD | 15,980,000.00 USD | 0.00 USD | 57,650.00 USD | 18,520.00 USD | 30,220.00 USD |
| `7D` | `9.54` | 16,000,000.00 USD | 16,000,000.00 USD | 0.00 USD | 11,650.00 USD | 13,310.00 USD | 839.03 USD |
| `7D` | `9.56` | 16,020,000.00 USD | 16,020,000.00 USD | 0.00 USD | 7,430.00 USD | 5,260.00 USD | 4,660.00 USD |
| `7D` | `9.58` | 16,090,000.00 USD | 16,090,000.00 USD | 0.00 USD | 35,340.00 USD | 2,380.00 USD | 27,020.00 USD |
| `7D` | `9.60` | 16,140,000.00 USD | 16,140,000.00 USD | 0.00 USD | 31,720.00 USD | 5,460.00 USD | 19,760.00 USD |
| `7D` | `9.62` | 16,180,000.00 USD | 16,180,000.00 USD | 0.00 USD | 26,870.00 USD | 1,540.00 USD | 9,730.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `351.49M` | Total OI Tokens: `41,484,016.2 AVAX`
  * 1h OI Change: `-0.26%` | 4h OI Change: `-1.55%` | 24h OI Change: `-6.99%`
  * Exchange Breakdown: Binance=`79.91M` | Bybit=`57.22M` | OKX=`11.49M` | Hyperliquid=`16.74M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `13.39K` | Last 24h: `16.67K` | Last 3d: `66.43K` | Last 7d: `105.12K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0100%` | **USDT OKX** | `0.0100%` |
| **USDT Bybit** | `0.0090%` | **USDT KuCoin** | `0.0100%` |
| **USDT MEXC** | `0.0100%` | **USDT BingX** | `0.0100%` |
| **USDT Gate** | `0.0062%` | **USDT Bitget** | `0.0058%` |
| **CoinM Binance** | `0.0100%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `AVAX` | `51.25%` | `48.75%` | `1.05` | 6,610,000.00 USD |
| `15M` | `Binance` | `47.46%` | `52.54%` | `0.90` | 1,960,000.00 USD |
| `15M` | `OKX` | `51.87%` | `48.13%` | `1.08` | 456,130.00 USD |
| `15M` | `Bybit` | `57.9%` | `42.1%` | `1.38` | 388,500.00 USD |
| `15M` | `KuCoin` | `46.28%` | `53.72%` | `0.86` | 60,240.00 USD |
| `15M` | `Gate` | `54.73%` | `45.27%` | `1.21` | 472,730.00 USD |
| `15M` | `Bitget` | `75.53%` | `24.47%` | `3.09` | 104,220.00 USD |
| `15M` | `BingX` | `58.96%` | `41.04%` | `1.44` | 1,100,000.00 USD |
| `15M` | `MEXC` | `51.65%` | `48.35%` | `1.07` | 499,090.00 USD |
| `15M` | `Bitunix` | `49.58%` | `50.42%` | `0.98` | 84,720.00 USD |
| `15M` | `Hyperliquid` | `33.63%` | `66.37%` | `0.51` | 109,500.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.06%` | `46.94%` | `1.13` | 1,010,000.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `1.69%` | `98.31%` | `0.02` | 218,730.00 USD |
| `15M` | `HTX` | `48.64%` | `51.36%` | `0.95` | 10,490.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `75.56%` | `24.44%` | `3.09` | 96,230.00 USD |
| `15M` | `Aster` | `96.97%` | `3.03%` | `32.00` | 360.30 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `80.24%` | `19.76%` | `4.06` | 27,340.00 USD |
| `15M` | `Whale Positions` | `47.46%` | `52.54%` | `0.90` | 1,960,000.00 USD |
| `15M` | `Global Accounts` | `51.25%` | `48.75%` | `1.05` | 6,610,000.00 USD |
| `1H` | `AVAX` | `44.44%` | `55.56%` | `0.80` | 50,820,000.00 USD |
| `1H` | `Binance` | `44.44%` | `55.56%` | `0.80` | 32,700,000.00 USD |
| `1H` | `OKX` | `49.38%` | `50.62%` | `0.98` | 3,180,000.00 USD |
| `1H` | `Bybit` | `33.14%` | `66.86%` | `0.50` | 3,800,000.00 USD |
| `1H` | `KuCoin` | `53.81%` | `46.19%` | `1.16` | 769,500.00 USD |
| `1H` | `Gate` | `51.38%` | `48.62%` | `1.06` | 2,370,000.00 USD |
| `1H` | `Bitget` | `34.2%` | `65.8%` | `0.52` | 920,150.00 USD |
| `1H` | `BingX` | `42.84%` | `57.16%` | `0.75` | 1,030,000.00 USD |
| `1H` | `MEXC` | `52.28%` | `47.72%` | `1.10` | 518,250.00 USD |
| `1H` | `Bitunix` | `46.55%` | `53.45%` | `0.87` | 1,290,000.00 USD |
| `1H` | `Hyperliquid` | `53.56%` | `46.44%` | `1.15` | 1,020,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `46.24%` | `53.76%` | `0.86` | 561,300.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.95%` | `99.05%` | `0.01` | 906,050.00 USD |
| `1H` | `HTX` | `65.46%` | `34.54%` | `1.90` | 348,380.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `69.21%` | `30.79%` | `2.25` | 400,080.00 USD |
| `1H` | `Aster` | `62.06%` | `37.94%` | `1.64` | 720,830.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `68.65%` | `31.35%` | `2.19` | 292,610.00 USD |
| `1H` | `Whale Positions` | `44.44%` | `55.56%` | `0.80` | 32,700,000.00 USD |
| `1H` | `Global Accounts` | `44.44%` | `55.56%` | `0.80` | 50,820,000.00 USD |
| `4H` | `AVAX` | `44.39%` | `55.61%` | `0.80` | 160,160,000.00 USD |
| `4H` | `Binance` | `44.83%` | `55.17%` | `0.81` | 59,320,000.00 USD |
| `4H` | `OKX` | `45.74%` | `54.26%` | `0.84` | 33,690,000.00 USD |
| `4H` | `Bybit` | `42.77%` | `57.23%` | `0.75` | 10,630,000.00 USD |
| `4H` | `KuCoin` | `45.63%` | `54.37%` | `0.84` | 1,030,000.00 USD |
| `4H` | `Gate` | `46.53%` | `53.47%` | `0.87` | 27,070,000.00 USD |
| `4H` | `Bitget` | `41.91%` | `58.09%` | `0.72` | 3,010,000.00 USD |
| `4H` | `BingX` | `37.24%` | `62.76%` | `0.59` | 2,880,000.00 USD |
| `4H` | `MEXC` | `42.89%` | `57.11%` | `0.75` | 9,860,000.00 USD |
| `4H` | `Bitunix` | `47.63%` | `52.37%` | `0.91` | 3,860,000.00 USD |
| `4H` | `Hyperliquid` | `56.61%` | `43.39%` | `1.30` | 1,310,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.05%` | `49.95%` | `1.00` | 1,120,000.00 USD |
| `4H` | `Crypto.com` | `33.26%` | `66.74%` | `0.50` | 191,210.00 USD |
| `4H` | `WhiteBIT` | `19.61%` | `80.39%` | `0.24` | 4,030,000.00 USD |
| `4H` | `HTX` | `42.47%` | `57.53%` | `0.74` | 751,030.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `47.93%` | `52.07%` | `0.92` | 481,660.00 USD |
| `4H` | `Aster` | `38.33%` | `61.67%` | `0.62` | 902,930.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.03%` | `40.97%` | `1.44` | 43,350.00 USD |
| `4H` | `Whale Positions` | `44.83%` | `55.17%` | `0.81` | 59,320,000.00 USD |
| `4H` | `Global Accounts` | `44.39%` | `55.61%` | `0.80` | 160,160,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `8.56` | `8.56` | `8.56` | `8.62` | `8.50` | 1,991,917.42 USD | 805,962.82 USD | 1,185,954.60 USD | -379,991.79 USD | `-19.08%` | `9B / 38S` |
| `5:00 UTC` | `8.49` | `8.51` | `8.49` | `8.55` | `8.48` | 1,276,824.26 USD | 505,302.94 USD | 771,521.32 USD | -266,218.38 USD | `-20.85%` | `4B / 18S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.52` | `8.45` | 1,829,814.14 USD | 869,168.19 USD | 960,645.95 USD | -91,477.76 USD | `-5.00%` | `11B / 14S` |
| `5:00 UTC` | `8.51` | `8.50` | `8.51` | `8.52` | `8.48` | 752,301.06 USD | 385,792.91 USD | 366,508.15 USD | 19,284.76 USD | `+2.56%` | `8B / 9S` |
| `0:00 UTC` | `8.46` | `8.47` | `8.46` | `8.49` | `8.46` | 681,089.39 USD | 260,569.06 USD | 420,520.33 USD | -159,951.27 USD | `-23.48%` | `1B / 5S` |
| `5:00 UTC` | `8.49` | `8.48` | `8.49` | `8.50` | `8.45` | 460,668.30 USD | 266,426.92 USD | 194,241.38 USD | 72,185.55 USD | `+15.67%` | `10B / 4S` |
| `0:00 UTC` | `8.48` | `8.48` | `8.48` | `8.51` | `8.46` | 702,848.74 USD | 346,932.98 USD | 355,915.76 USD | -8,982.78 USD | `-1.28%` | `2B / 6S` |
| `5:00 UTC` | `8.46` | `8.47` | `8.46` | `8.48` | `8.46` | 798,371.69 USD | 455,825.46 USD | 342,546.23 USD | 113,279.23 USD | `+14.19%` | `6B / 4S` |
| `0:00 UTC` | `8.47` | `8.46` | `8.47` | `8.48` | `8.44` | 1,028,869.35 USD | 429,609.02 USD | 599,260.32 USD | -169,651.30 USD | `-16.49%` | `4B / 8S` |
| `5:00 UTC` | `8.47` | `8.47` | `8.47` | `8.48` | `8.46` | 241,759.37 USD | 29,431.46 USD | 212,327.91 USD | -182,896.45 USD | `-75.65%` | `2B / 8S` |

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
| `5m` | 892.24 USD | 75,770.00 USD | **`ACCUMULATION`** |
| `15m` | -65,590.00 USD | -206,390.00 USD | **`DISTRIBUTION`** |
| `30m` | -52,890.00 USD | -105,020.00 USD | **`DISTRIBUTION`** |
| `1h` | -48,550.00 USD | -119,260.00 USD | **`DISTRIBUTION`** |
| `2h` | -378,340.00 USD | -1,320,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -469,080.00 USD | -1,870,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -34,100.00 USD | -1,700,000.00 USD | **`DISTRIBUTION`** |
| `8h` | 155,090.00 USD | 381,580.00 USD | **`ACCUMULATION`** |
| `12h` | -706,160.00 USD | -3,130,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -2,850,000.00 USD | -12,600,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -7,990,000.00 USD | -50,990,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -57,680,000.00 USD | -267,230,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+892.24` | 15m=`-65.59K` | 1h=`-48.55K` | 24h=`-2.85M`
* Futures Capital Netflows: 5m=`+75.77K` | 15m=`-206.39K` | 1h=`-119.26K` | 24h=`-12.60M`
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
  * `2026-10-30 15:12:05 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 14:41:05 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:38:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 14:34:05 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 14:33:05 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [@financialjuice] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:16:05 IST`: [insee.fr] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 15:15:05 IST`: [nationwide.co.uk] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `8.04` (Risk Distance: `0.1313` pts)
  * +2.5R Take Profit: `8.50`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `8.52` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `8.65` (Risk Distance: `0.1313` pts)
  * +2.5R Take Profit: `8.19`
  * Mathematical Lot Sizing: **`20.00 lots`** (Nominal Risk = `0.00 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`8.54`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
