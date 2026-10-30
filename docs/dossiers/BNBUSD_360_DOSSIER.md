# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 14:47:51 IST` (`2026-10-30 09:17:51 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `700.90` | **Live Ask Quote**: `704.10` | **Mid Price**: `702.50`
- **Spread Points**: `320.00` | **Spread BPS**: `45.55 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `702.19` | VWAP Z-Score: `+0.07` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `3.53` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `38.01` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `732.02` | Lower -3.00σ Band: `672.36`
  * Upper +2.51σ Band: `727.15` | Lower -2.51σ Band: `677.23`
  * Upper +2.01σ Band: `722.18` | Lower -2.01σ Band: `682.21`
  * Upper +2.00σ Band: `722.08` | Lower -2.00σ Band: `682.31`
  * Upper +1.28σ Band: `714.92` | Lower -1.28σ Band: `689.47`
  * Upper +1.00σ Band: `712.14` | Lower -1.00σ Band: `692.25`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`705.79` | EMA-20=`707.83` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`712.00` (Slope: `+0.0000`) | EMA-100=`720.85`
  * Institutional Anchors: EMA-144=`726.04` | EMA-200=`730.01` (Slope: `-0.3857`) | EMA-233=`732.00`
- **Range Boundaries**: 24H High=`753.20` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `715.24` (Distance: `-1.78%`)
  * Point of Control (POC) = `704.18` (Distance: `-0.24%`)
  * Value Area Low (VAL) = `699.26` (Distance: `+0.46%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`700.90`
  * New York Session (13:00-21:00 UTC): High=`706.72` | Low=`698.28`
  * Initial Balance (First Hour): IB High=`717.90` | IB Low=`712.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `699.69` - `705.31`
  * Optimal Trade Entry (OTE 0.705): `703.90`
  * Structural Invalidation Anchor (0.786): `708.12`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `705.59` | `705.77` | `705.10` | `705.61` | `1,824` | 1,286,350.95 USD | 299,481.02 USD | `+23.28%` | -54,700,346.50 USD | `+1.19` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `5m` | `705.60` | `705.61` | `703.62` | `704.09` | `3,703` | 2,606,992.10 USD | -1,217,577.90 USD | `-46.70%` | -55,917,924.40 USD | `-0.91` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `704.08` | `704.21` | `703.70` | `704.21` | `1,029` | 724,051.01 USD | -73,675.32 USD | `-10.18%` | -55,991,599.71 USD | `+0.65` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `706.19` | `706.93` | `705.06` | `705.54` | `12,244` | 8,644,432.66 USD | -2,421,966.37 USD | `-28.02%` | -53,668,118.56 USD | `-0.60` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `705.53` | `705.87` | `703.88` | `705.59` | `9,268` | 6,533,203.74 USD | -1,331,708.96 USD | `-20.38%` | -54,999,827.52 USD | `+0.10` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `705.59` | `705.77` | `703.62` | `704.21` | `6,555` | 4,617,394.06 USD | -991,772.20 USD | `-21.48%` | -55,991,599.71 USD | `+0.26` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `715.79` | `715.89` | `705.71` | `707.71` | `63,287` | 44,957,687.37 USD | -10,972,666.83 USD | `-24.41%` | -35,081,859.96 USD | `-0.95` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `707.72` | `708.59` | `703.88` | `705.59` | `41,806` | 29,527,241.58 USD | -7,490,244.75 USD | `-25.37%` | -42,572,104.71 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `705.59` | `705.77` | `703.62` | `704.20` | `6,561` | 4,622,147.47 USD | -995,511.56 USD | `-21.54%` | -43,567,616.28 USD | `+0.22` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `703.62` | `704.21` | `48,361` | 34,144,635.64 USD | -8,482,016.94 USD | `-24.84%` | -49,283,957.49 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | 8,277,694.32 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | 775,183.01 USD | `-1.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `703.62` | `704.21` | `48,361` | 34,144,635.64 USD | -8,482,016.94 USD | `-24.84%` | -49,283,957.49 USD | `-0.03` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`702.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `703.30` | `9008000000.0000` | 6,335.33 USD | 99,673.10 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.31` | `3652000000.0000` | 2,568.49 USD | 93,337.77 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `703.32` | `426000000.0000` | 299.61 USD | 90,769.28 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.33` | `15797000000.0000` | 11,110.50 USD | 90,469.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.34` | `7439000000.0000` | 5,232.15 USD | 79,359.17 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.36` | `44407000000.0000` | 31,234.11 USD | 74,127.02 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `703.37` | `12637000000.0000` | 8,888.49 USD | 42,892.91 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.38` | `1293000000.0000` | 909.47 USD | 34,004.42 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.39` | `2843000000.0000` | 1,999.74 USD | 33,094.95 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.40` | `11105000000.0000` | 7,811.26 USD | 31,095.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.41` | `2279000000.0000` | 1,603.07 USD | 23,283.96 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.43` | `3652000000.0000` | 2,568.93 USD | 21,680.89 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `703.46` | `334000000.0000` | 234.96 USD | 19,111.96 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `703.47` | `2847000000.0000` | 2,002.78 USD | 18,877.01 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `703.50` | `2293000000.0000` | 1,613.13 USD | 16,874.23 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `703.51` | `1293000000.0000` | 909.64 USD | 15,261.10 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `703.53` | `9476000000.0000` | 6,666.65 USD | 14,351.46 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `703.54` | `9074000000.0000` | 6,383.92 USD | 7,684.81 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `703.56` | `1423000000.0000` | 1,001.17 USD | 1,300.89 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `703.58` | `426000000.0000` | 299.73 USD | 299.73 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `703.61` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 703.61` | `0.00%` | `-` |
| `ASK` | `703.64` | `1006000000.0000` | 707.86 USD | 707.86 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `703.66` | `1291000000.0000` | 908.43 USD | 1,616.29 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `703.69` | `3880000000.0000` | 2,730.32 USD | 4,346.60 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `703.73` | `1282000000.0000` | 902.18 USD | 5,248.79 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `703.79` | `1294000000.0000` | 910.70 USD | 6,159.49 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `703.85` | `8965000000.0000` | 6,310.02 USD | 12,469.51 USD | `4 orders` | `+0.03%` | `-` |
| `ASK` | `703.87` | `6307000000.0000` | 4,439.31 USD | 16,908.81 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.88` | `1741000000.0000` | 1,225.46 USD | 18,134.27 USD | `4 orders` | `+0.04%` | `-` |
| `ASK` | `703.89` | `3401000000.0000` | 2,393.93 USD | 20,528.20 USD | `5 orders` | `+0.04%` | `-` |
| `ASK` | `703.90` | `11101000000.0000` | 7,813.99 USD | 28,342.19 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.92` | `8911000000.0000` | 6,272.63 USD | 34,614.82 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.94` | `8384000000.0000` | 5,901.83 USD | 40,516.66 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `703.97` | `8414000000.0000` | 5,923.20 USD | 46,439.86 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `703.98` | `41907000000.0000` | 29,501.69 USD | 75,941.55 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `703.99` | `2500000000.0000` | 1,759.97 USD | 77,701.52 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `704.00` | `190000000.0000` | 133.76 USD | 77,835.28 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `704.01` | `2507000000.0000` | 1,764.95 USD | 79,600.24 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `704.02` | `1119000000.0000` | 787.80 USD | 80,388.04 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `704.03` | `4122000000.0000` | 2,902.01 USD | 83,290.05 USD | `3 orders` | `+0.06%` | `-` |
| `ASK` | `704.04` | `3934000000.0000` | 2,769.69 USD | 86,059.74 USD | `3 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 14:43:12 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `790` | `0xea00...a918` | `LONG` | 2,882,220.19 USD | `4,098,429,000,000.00` | `787.24` | `703.21` | `0.000000` | -344,206.59 USD | `-11.94%` | `5X Cross` |
| `915` | `0xfe7c...b7ae` | `LONG` | 2,455,450.12 USD | `3,491,575,000,000.00` | `686.05` | `703.21` | `0.000000` | 60,039.26 USD | `+2.45%` | `10X Cross` |
| `1030` | `0x7d0c...1b28` | `LONG` | 2,151,839.51 USD | `3,059,850,000,000.00` | `704.22` | `703.21` | `0.000000` | -2,953.15 USD | `-0.14%` | `10X Cross` |
| `1128` | `0x27c9...d65d` | `LONG` | 1,954,905.60 USD | `2,779,816,000,000.00` | `700.84` | `703.21` | `140.63` | 6,690.79 USD | `+0.34%` | `10X Cross` |
| `1188` | `0x7737...bf66` | `SHORT` | 1,861,242.92 USD | `2,646,179,000,000.00` | `752.73` | `703.21` | `7088.28` | 130,627.66 USD | `+7.02%` | `10X Cross` |
| `1373` | `0x51f6...2b39` | `LONG` | 1,575,623.16 USD | `2,240,711,000,000.00` | `703.00` | `703.21` | `101.76` | 413.52 USD | `+0.03%` | `10X Cross` |
| `1496` | `0xc675...795d` | `LONG` | 1,445,216.21 USD | `2,055,214,000,000.00` | `706.91` | `703.21` | `640.79` | -7,628.46 USD | `-0.53%` | `10X Cross` |
| `1532` | `0x2edd...8179` | `LONG` | 1,407,572.61 USD | `2,001,696,000,000.00` | `714.56` | `703.21` | `0.000000` | -22,761.77 USD | `-1.62%` | `10X Cross` |
| `1583` | `0x325e...9564` | `LONG` | 1,360,118.54 USD | `1,934,212,000,000.00` | `707.43` | `703.21` | `0.000000` | -8,207.23 USD | `-0.60%` | `10X Cross` |
| `1717` | `0x07fd...689d` | `LONG` | 1,226,568.69 USD | `1,744,292,000,000.00` | `714.31` | `703.21` | `0.000000` | -19,394.85 USD | `-1.58%` | `10X Cross` |
| `1732` | `0x645b...87b8` | `LONG` | 1,210,886.15 USD | `1,721,990,000,000.00` | `747.34` | `703.21` | `0.000000` | -76,021.27 USD | `-6.28%` | `10X Cross` |
| `1796` | `0xecb6...2b00` | `SHORT` | 1,153,769.77 USD | `1,640,812,000,000.00` | `715.02` | `703.21` | `19549.92` | 19,452.80 USD | `+1.69%` | `5X Cross` |
| `1812` | `0xa4a6...46cf` | `SHORT` | 1,143,092.09 USD | `1,625,442,000,000.00` | `711.86` | `703.21` | `1619.76` | 14,000.29 USD | `+1.22%` | `10X Cross` |
| `1882` | `0xfc27...9d9d` | `LONG` | 1,088,652.86 USD | `1,548,205,000,000.00` | `701.14` | `703.21` | `0.000000` | 3,135.41 USD | `+0.29%` | `10X Cross` |
| `1899` | `0x4420...4c4b` | `LONG` | 1,069,298.99 USD | `1,520,143,000,000.00` | `704.02` | `703.21` | `205.11` | -911.58 USD | `-0.09%` | `10X Cross` |
| `1917` | `0x14c6...b280` | `SHORT` | 1,054,785.00 USD | `1,500,000,000,000.00` | `712.51` | `703.21` | `1464.73` | 13,976.70 USD | `+1.33%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.47` | 34,073.94 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 34.07K USD at 745.4700 USD [API] | `2026-10-29 13:56:46` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.49` (Vol: 2,400,000.00 USD, Dist: `+7.56%`) | Long MP=`677.23` (Vol: 3,100,000.00 USD, Dist: `--3.97%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+8.89%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.96%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+8.89%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.96%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+8.89%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--3.96%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `141.50` | 19,800.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `142.50` | 273.03 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 6,150.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `156.50` | 435,260.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `158.50` | 95,100.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `165.50` | 1,000.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 101.79 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `173.50` | 6,200.00 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `189.50` | 539.51 USD | 4,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 20,250.00 USD | 4,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 310,870.00 USD | 4,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `209.50` | 257.06 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `226.50` | 874.29 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `229.50` | 229,500.00 USD | 4,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `234.50` | 161.10 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 8,310.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 998.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,320.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `262.50` | 399.26 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `268.50` | 21,280.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `274.50` | 10,980.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `277.50` | 341.05 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `297.50` | 20,660.00 USD | 4,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `303.50` | 451.91 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `310.50` | 159,800.00 USD | 4,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `313.50` | 127.59 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 6,500.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 376.06 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `344.50` | 121.61 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `345.50` | 2,040.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `347.50` | 9,580.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 340.60 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 17,420.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 10,480.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 15,780.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `375.50` | 16,900.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,400.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 1,910.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 10,870.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 2,620.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 341.17 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `390.50` | 3,370.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `392.50` | 103.62 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 600.48 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 4,240.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 7,670.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 522.32 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `403.50` | 102.09 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 3,490.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 9,800.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 4,590.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 2,350.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 4,780.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,440.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 29,640.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `425.50` | 7,480.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `426.50` | 31,670.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 4,200.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 545.01 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 133.13 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `442.50` | 935.89 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `447.50` | 223.75 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `451.50` | 1,470.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `463.50` | 927.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `472.50` | 203.17 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 1,300.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 2,840.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,890.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 693.75 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 2,070.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 2,300.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 1,840.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 11,260.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 4,370.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 186.69 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 14,130.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 4,380.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 5,760.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `506.50` | 683.27 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `507.50` | 2,760.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 483.58 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 73,860.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 42,080.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 6,470.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 263.92 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 703.92 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 272.22 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 64,750.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 2,160.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 97,260.00 USD | 3,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 21,140.00 USD | 3,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 536.82 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 181,920.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 10,350.00 USD | 3,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 12,560.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,740.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `563.50` | 281.75 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 107.83 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 721,240.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 5,270.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 5,780.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 1,850.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `579.50` | 164,400.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 53,080.00 USD | 2,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 690.26 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,060.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,530.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 10,820.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,420.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 44,720.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 3,000.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 423.52 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,480.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 791.22 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 222.32 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 22,860.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 2,780.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.50` | 58,420.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 1,880.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 213.32 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `609.90` | 39,280,000.00 USD | 39,280,000.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `610.50` | 4,270.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 6,520.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `620.90` | 39,250,000.00 USD | 39,250,000.00 USD | 0.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 13,930.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `621.90` | 38,930,000.00 USD | 38,930,000.00 USD | 310,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `623.50` | 415.25 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,270.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `626.90` | 38,620,000.00 USD | 38,620,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `628.50` | 381.50 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `628.90` | 38,580,000.00 USD | 38,580,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `629.90` | 38,310,000.00 USD | 38,310,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `630.90` | 38,060,000.00 USD | 38,060,000.00 USD | 230,570.00 USD | 50,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `631.90` | 37,780,000.00 USD | 37,780,000.00 USD | 58,820.00 USD | 88,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.10` | 49,690,000.00 USD | 49,690,000.00 USD | 527,000.00 USD | 61,830.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `633.90` | 49,060,000.00 USD | 49,060,000.00 USD | 89,960.00 USD | 30,650.00 USD | 83,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `633.90` | 37,630,000.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 5,900.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.70` | 48,860,000.00 USD | 48,860,000.00 USD | 39,810.00 USD | 16,410.00 USD | 75,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `634.90` | 37,560,000.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `635.50` | 48,730,000.00 USD | 48,730,000.00 USD | 101,710.00 USD | 9,540.00 USD | 58,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `635.90` | 37,510,000.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `636.30` | 48,560,000.00 USD | 48,560,000.00 USD | 57,730.00 USD | 56,570.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.10` | 48,210,000.00 USD | 48,210,000.00 USD | 136,880.00 USD | 10,320.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.90` | 48,050,000.00 USD | 48,050,000.00 USD | 59,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.70` | 47,990,000.00 USD | 47,990,000.00 USD | 4,240.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `639.50` | 47,950,000.00 USD | 47,950,000.00 USD | 242,510.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 1,490.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `640.90` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.10` | 47,530,000.00 USD | 47,530,000.00 USD | 0.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.90` | 47,520,000.00 USD | 47,520,000.00 USD | 230,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `641.90` | 37,170,000.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 476,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.70` | 47,290,000.00 USD | 47,290,000.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `642.90` | 37,130,000.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `643.50` | 47,260,000.00 USD | 47,260,000.00 USD | 69,670.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 468,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `643.90` | 36,960,000.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.30` | 47,180,000.00 USD | 47,180,000.00 USD | 393,100.00 USD | 36,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `644.90` | 36,930,000.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.10` | 46,750,000.00 USD | 46,750,000.00 USD | 93,740.00 USD | 4,720.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 307.26 USD | 467,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `645.90` | 46,310,000.00 USD | 46,310,000.00 USD | 79,070.00 USD | 11,780.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `645.90` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 467,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.70` | 46,190,000.00 USD | 46,190,000.00 USD | 250,710.00 USD | 2,560.00 USD | 169,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `646.90` | 36,830,000.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.50` | 45,760,000.00 USD | 45,760,000.00 USD | 140,910.00 USD | 33,700.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `647.90` | 36,660,000.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `648.30` | 45,570,000.00 USD | 45,570,000.00 USD | 136,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 467,240.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `648.90` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.10` | 45,430,000.00 USD | 45,430,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 465,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `649.90` | 45,380,000.00 USD | 45,380,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `649.90` | 36,490,000.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 587.40 USD | 463,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `650.70` | 45,320,000.00 USD | 45,320,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `650.90` | 36,310,000.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `651.50` | 45,300,000.00 USD | 45,300,000.00 USD | 167,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 463,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `651.90` | 36,260,000.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `652.30` | 45,130,000.00 USD | 45,130,000.00 USD | 15,190.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 453,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `652.90` | 35,990,000.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `653.10` | 45,020,000.00 USD | 45,020,000.00 USD | 15,540.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 98,240.00 USD | 452,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.90` | 44,980,000.00 USD | 44,980,000.00 USD | 43,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 354,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.70` | 44,940,000.00 USD | 44,940,000.00 USD | 143,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `654.90` | 35,780,000.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `655.50` | 44,790,000.00 USD | 44,790,000.00 USD | 202,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 122.58 USD | 354,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `655.90` | 35,590,000.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.30` | 44,590,000.00 USD | 44,590,000.00 USD | 41,280.00 USD | 19,650.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `656.90` | 35,520,000.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.10` | 43,700,000.00 USD | 43,700,000.00 USD | 175,030.00 USD | 21,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.90` | 43,510,000.00 USD | 43,510,000.00 USD | 935,290.00 USD | 14,920.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `657.90` | 35,410,000.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,430.00 USD | 354,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.70` | 42,540,000.00 USD | 42,540,000.00 USD | 171,980.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `658.90` | 35,380,000.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `659.50` | 42,280,000.00 USD | 42,280,000.00 USD | 111,490.00 USD | 7,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 45,510.00 USD | 338,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `659.90` | 35,350,000.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `660.30` | 42,160,000.00 USD | 42,160,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 293,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `660.90` | 35,200,000.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `661.10` | 42,060,000.00 USD | 42,060,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 289,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.90` | 41,970,000.00 USD | 41,970,000.00 USD | 592,290.00 USD | 68,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `661.90` | 34,890,000.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 269,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.70` | 41,310,000.00 USD | 41,310,000.00 USD | 98,540.00 USD | 87,740.00 USD | 24,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `662.90` | 34,060,000.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `663.50` | 41,100,000.00 USD | 41,100,000.00 USD | 202,030.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 21,880.00 USD | 267,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `663.90` | 33,710,000.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.30` | 40,880,000.00 USD | 40,880,000.00 USD | 785,690.00 USD | 64,390.00 USD | 89,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 10,080.00 USD | 245,120.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.90` | 32,730,000.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.10` | 39,940,000.00 USD | 39,940,000.00 USD | 684,260.00 USD | 0.00 USD | 43,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 6,330.00 USD | 235,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `665.90` | 39,210,000.00 USD | 39,210,000.00 USD | 743,370.00 USD | 93,330.00 USD | 746,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.90` | 32,420,000.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 1,930.00 USD | 228,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.70` | 37,620,000.00 USD | 37,620,000.00 USD | 836,620.00 USD | 13,270.00 USD | 38,830.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.90` | 31,890,000.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.50` | 36,740,000.00 USD | 36,740,000.00 USD | 474,720.00 USD | 167,750.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 226,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.90` | 31,380,000.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.30` | 36,080,000.00 USD | 36,080,000.00 USD | 727,960.00 USD | 25,520.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 41,770.00 USD | 225,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.90` | 30,200,000.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.10` | 35,330,000.00 USD | 35,330,000.00 USD | 477,700.00 USD | 70,860.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 5,280.00 USD | 183,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.90` | 34,760,000.00 USD | 34,760,000.00 USD | 631,610.00 USD | 43,250.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.90` | 29,320,000.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 3,310.00 USD | 178,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.70` | 32,580,000.00 USD | 32,580,000.00 USD | 474,770.00 USD | 10,760.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.90` | 28,970,000.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `671.50` | 32,090,000.00 USD | 32,090,000.00 USD | 1,900,000.00 USD | 30,160.00 USD | 46,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 19,470.00 USD | 175,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `671.90` | 27,970,000.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `672.30` | 30,110,000.00 USD | 30,110,000.00 USD | 595,540.00 USD | 3,440.00 USD | 15,940.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 6,520.00 USD | 155,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `672.90` | 27,000,000.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.10` | 29,490,000.00 USD | 29,490,000.00 USD | 333,580.00 USD | 272,060.00 USD | 869,570.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 40,750.00 USD | 149,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.90` | 28,020,000.00 USD | 28,020,000.00 USD | 254,340.00 USD | 151,100.00 USD | 1,540,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.90` | 25,800,000.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,100.00 USD | 108,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.70` | 26,070,000.00 USD | 26,070,000.00 USD | 1,110,000.00 USD | 372,740.00 USD | 192,750.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.90` | 25,130,000.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.50` | 24,390,000.00 USD | 24,390,000.00 USD | 1,250,000.00 USD | 184,430.00 USD | 307,030.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 74,720.00 USD | 104,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.90` | 24,000,000.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.30` | 22,650,000.00 USD | 22,650,000.00 USD | 458,110.00 USD | 333,250.00 USD | 470,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,960.00 USD | 29,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.90` | 21,640,000.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.10` | 21,390,000.00 USD | 21,390,000.00 USD | 125,560.00 USD | 90,100.00 USD | 312,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.90` | 20,860,000.00 USD | 20,860,000.00 USD | 438,990.00 USD | 174,250.00 USD | 250,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.90` | 18,560,000.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 2,520.00 USD | 27,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `678.70` | 20,000,000.00 USD | 20,000,000.00 USD | 1,530,000.00 USD | 164,420.00 USD | 148,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.90` | 17,300,000.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.50` | 18,150,000.00 USD | 18,150,000.00 USD | 1,590,000.00 USD | 80,850.00 USD | 155,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 1,470.00 USD | 25,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `679.90` | 16,910,000.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.30` | 16,320,000.00 USD | 16,320,000.00 USD | 25,960.00 USD | 215,610.00 USD | 261,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 22,380.00 USD | 23,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `680.90` | 16,430,000.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.10` | 15,820,000.00 USD | 15,820,000.00 USD | 597,000.00 USD | 206,150.00 USD | 87,500.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 1,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.90` | 14,930,000.00 USD | 14,930,000.00 USD | 452,920.00 USD | 334,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.90` | 16,190,000.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.70` | 14,140,000.00 USD | 14,140,000.00 USD | 336,330.00 USD | 59,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.90` | 14,430,000.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.50` | 13,750,000.00 USD | 13,750,000.00 USD | 468,720.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 14,390,000.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.30` | 13,240,000.00 USD | 13,240,000.00 USD | 429,900.00 USD | 21,510.00 USD | 50,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.90` | 14,320,000.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.10` | 12,740,000.00 USD | 12,740,000.00 USD | 406,260.00 USD | 37,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.90` | 12,300,000.00 USD | 12,300,000.00 USD | 1,120,000.00 USD | 48,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.90` | 12,710,000.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.70` | 11,130,000.00 USD | 11,130,000.00 USD | 0.00 USD | 119,680.00 USD | 98,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.90` | 12,590,000.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.50` | 10,910,000.00 USD | 10,910,000.00 USD | 1,030,000.00 USD | 111,890.00 USD | 17,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.90` | 12,460,000.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.30` | 9,750,000.00 USD | 9,750,000.00 USD | 567,010.00 USD | 89,420.00 USD | 386,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.90` | 11,820,000.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.10` | 8,710,000.00 USD | 8,710,000.00 USD | 62,440.00 USD | 86,420.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.90` | 7,510,000.00 USD | 7,510,000.00 USD | 109,090.00 USD | 29,070.00 USD | 188,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.90` | 9,550,000.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.70` | 7,190,000.00 USD | 7,190,000.00 USD | 115,540.00 USD | 199,550.00 USD | 401,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.90` | 8,340,000.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.50` | 6,470,000.00 USD | 6,470,000.00 USD | 0.00 USD | 71,280.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.90` | 8,050,000.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.30` | 6,350,000.00 USD | 6,350,000.00 USD | 780,530.00 USD | 31,410.00 USD | 102,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 5,920,000.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.10` | 5,430,000.00 USD | 5,430,000.00 USD | 76,730.00 USD | 159,980.00 USD | 69,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.90` | 5,130,000.00 USD | 5,130,000.00 USD | 320,330.00 USD | 140,550.00 USD | 382,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.90` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.70` | 4,280,000.00 USD | 4,280,000.00 USD | 66,510.00 USD | 118,590.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.50` | 3,920,000.00 USD | 3,920,000.00 USD | 239,550.00 USD | 34,140.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.30` | 3,560,000.00 USD | 3,560,000.00 USD | 153,900.00 USD | 32,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `697.10` | 3,370,000.00 USD | 3,370,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `697.90` | 3,310,000.00 USD | 3,310,000.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.70` | 3,110,000.00 USD | 3,110,000.00 USD | 276,500.00 USD | 0.00 USD | 67,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.90` | 3,530,000.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.50` | 2,760,000.00 USD | 2,760,000.00 USD | 0.00 USD | 31,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.30` | 2,730,000.00 USD | 2,730,000.00 USD | 324,120.00 USD | 31,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `700.50` | 200.34 USD | 200.34 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `700.90` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.10` | 2,380,000.00 USD | 2,380,000.00 USD | 0.00 USD | 86,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.90` | 2,290,000.00 USD | 2,290,000.00 USD | 478,240.00 USD | 182,900.00 USD | 87,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.70` | 1,540,000.00 USD | 1,540,000.00 USD | 298,700.00 USD | 62,790.00 USD | 156,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.50` | 1,020,000.00 USD | 1,020,000.00 USD | 443,680.00 USD | 58,910.00 USD | 519,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.90` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `704.30` | 38,940.00 USD | 38,940.00 USD | 38,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.90` | 1,550,000.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `705.50` | 10,730.00 USD | 10,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `705.90` | 160,120.00 USD | 160,120.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `709.90` | 677,910.00 USD | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `710.70` | 503,660.00 USD | 503,660.00 USD | 343,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.50` | 889,020.00 USD | 889,020.00 USD | 308,680.00 USD | 0.00 USD | 76,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `712.50` | 2,440.00 USD | 13,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `714.70` | 1,300,000.00 USD | 1,300,000.00 USD | 0.00 USD | 0.00 USD | 415,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `715.50` | 2,220,000.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 917,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.70` | 2,520,000.00 USD | 2,520,000.00 USD | 115,540.00 USD | 35,360.00 USD | 142,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.50` | 2,880,000.00 USD | 2,880,000.00 USD | 60,590.00 USD | 82,030.00 USD | 219,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.30` | 4,090,000.00 USD | 4,090,000.00 USD | 988,460.00 USD | 86,780.00 USD | 134,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 376.82 USD | 13,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.10` | 4,640,000.00 USD | 4,640,000.00 USD | 177,520.00 USD | 328,830.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 28,020.00 USD | 41,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `721.90` | 5,370,000.00 USD | 5,370,000.00 USD | 145,470.00 USD | 207,490.00 USD | 368,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 1,950.00 USD | 43,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `722.70` | 6,100,000.00 USD | 6,100,000.00 USD | 393,920.00 USD | 131,240.00 USD | 207,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.50` | 7,120,000.00 USD | 7,120,000.00 USD | 446,650.00 USD | 403,140.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 2,170.00 USD | 45,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `724.30` | 7,610,000.00 USD | 7,610,000.00 USD | 300,180.00 USD | 185,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 46,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.10` | 8,000,000.00 USD | 8,000,000.00 USD | 223,480.00 USD | 152,860.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 47,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.90` | 8,340,000.00 USD | 8,340,000.00 USD | 317,710.00 USD | 0.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 4,600.00 USD | 52,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.70` | 8,680,000.00 USD | 8,680,000.00 USD | 226,170.00 USD | 85,880.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `727.50` | 9,260,000.00 USD | 9,260,000.00 USD | 537,650.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 342.65 USD | 52,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `728.30` | 9,500,000.00 USD | 9,500,000.00 USD | 235,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,080.00 USD | 93,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.10` | 10,350,000.00 USD | 10,350,000.00 USD | 359,560.00 USD | 285,300.00 USD | 207,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 171,010.00 USD | 264,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `729.90` | 11,200,000.00 USD | 11,200,000.00 USD | 135,850.00 USD | 176,860.00 USD | 531,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 28,500.00 USD | 293,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `730.70` | 16,740,000.00 USD | 16,740,000.00 USD | 3,130,000.00 USD | 450,040.00 USD | 1,970,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.50` | 17,700,000.00 USD | 17,700,000.00 USD | 387,170.00 USD | 129,110.00 USD | 446,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 2,050.00 USD | 295,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `732.30` | 20,150,000.00 USD | 20,150,000.00 USD | 950,550.00 USD | 84,320.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 140,300.00 USD | 435,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `733.10` | 21,850,000.00 USD | 21,850,000.00 USD | 905,320.00 USD | 249,610.00 USD | 551,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 12,260.00 USD | 447,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.90` | 22,790,000.00 USD | 22,790,000.00 USD | 365,220.00 USD | 226,780.00 USD | 347,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,680.00 USD | 600,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.70` | 23,860,000.00 USD | 23,860,000.00 USD | 967,050.00 USD | 52,620.00 USD | 51,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `735.50` | 25,130,000.00 USD | 25,130,000.00 USD | 395,650.00 USD | 245,130.00 USD | 625,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 22,600.00 USD | 623,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.30` | 25,770,000.00 USD | 25,770,000.00 USD | 374,870.00 USD | 70,270.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 8,670.00 USD | 631,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.10` | 26,030,000.00 USD | 26,030,000.00 USD | 136,080.00 USD | 43,110.00 USD | 88,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 9,300.00 USD | 641,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `737.90` | 26,620,000.00 USD | 26,620,000.00 USD | 363,220.00 USD | 178,930.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 14,120.00 USD | 655,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.70` | 27,700,000.00 USD | 27,700,000.00 USD | 576,800.00 USD | 33,100.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.50` | 28,370,000.00 USD | 28,370,000.00 USD | 170,280.00 USD | 31,860.00 USD | 461,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 119,490.00 USD | 774,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.30` | 28,590,000.00 USD | 28,590,000.00 USD | 92,050.00 USD | 134,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 6,760.00 USD | 781,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.10` | 29,190,000.00 USD | 29,190,000.00 USD | 554,740.00 USD | 32,240.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 35,200.00 USD | 816,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `741.90` | 29,500,000.00 USD | 29,500,000.00 USD | 291,160.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 66,550.00 USD | 883,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.70` | 29,640,000.00 USD | 29,640,000.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `743.50` | 30,330,000.00 USD | 30,330,000.00 USD | 233,380.00 USD | 21,120.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 47,230.00 USD | 930,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `744.30` | 31,420,000.00 USD | 31,420,000.00 USD | 891,770.00 USD | 191,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.10` | 33,090,000.00 USD | 33,090,000.00 USD | 710,280.00 USD | 61,600.00 USD | 897,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 30,150.00 USD | 1,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.90` | 33,480,000.00 USD | 33,480,000.00 USD | 196,920.00 USD | 120,210.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 185,960.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.70` | 35,220,000.00 USD | 35,220,000.00 USD | 674,650.00 USD | 29,460.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.50` | 35,670,000.00 USD | 35,670,000.00 USD | 295,810.00 USD | 74,380.00 USD | 80,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 2,010.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.30` | 36,260,000.00 USD | 36,260,000.00 USD | 399,610.00 USD | 84,260.00 USD | 108,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 12,010.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.10` | 36,650,000.00 USD | 36,650,000.00 USD | 385,820.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 67,670.00 USD | 1,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.90` | 36,870,000.00 USD | 36,870,000.00 USD | 224,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 575,140.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.70` | 36,950,000.00 USD | 36,950,000.00 USD | 79,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `751.50` | 37,170,000.00 USD | 37,170,000.00 USD | 92,160.00 USD | 25,010.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 11,270.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `752.30` | 37,700,000.00 USD | 37,700,000.00 USD | 93,830.00 USD | 0.00 USD | 441,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 58,760.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.10` | 38,350,000.00 USD | 38,350,000.00 USD | 393,720.00 USD | 0.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `753.50` | 132.62 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.90` | 38,800,000.00 USD | 38,800,000.00 USD | 362,250.00 USD | 54,420.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,450.00 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.70` | 39,120,000.00 USD | 39,120,000.00 USD | 159,380.00 USD | 142,490.00 USD | 16,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.50` | 39,710,000.00 USD | 39,710,000.00 USD | 396,840.00 USD | 132,220.00 USD | 56,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 144.30 USD | 2,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.30` | 40,180,000.00 USD | 40,180,000.00 USD | 403,440.00 USD | 24,970.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 2,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.10` | 40,530,000.00 USD | 40,530,000.00 USD | 164,820.00 USD | 122,240.00 USD | 63,690.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 367,790.00 USD | 3,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `757.90` | 41,000,000.00 USD | 41,000,000.00 USD | 378,680.00 USD | 67,700.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,430.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `758.70` | 41,840,000.00 USD | 41,840,000.00 USD | 421,820.00 USD | 142,320.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.50` | 43,030,000.00 USD | 43,030,000.00 USD | 1,180,000.00 USD | 2,460.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 704.82 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.30` | 43,330,000.00 USD | 43,330,000.00 USD | 231,490.00 USD | 55,920.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 3,670.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.10` | 43,850,000.00 USD | 43,850,000.00 USD | 254,000.00 USD | 15,330.00 USD | 243,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 2,360.00 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.90` | 44,550,000.00 USD | 44,550,000.00 USD | 575,650.00 USD | 35,860.00 USD | 94,030.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 367.52 USD | 3,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.70` | 46,350,000.00 USD | 46,350,000.00 USD | 1,210,000.00 USD | 133,840.00 USD | 444,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.50` | 47,870,000.00 USD | 47,870,000.00 USD | 1,220,000.00 USD | 125,250.00 USD | 171,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 603,420.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.30` | 49,310,000.00 USD | 49,310,000.00 USD | 1,190,000.00 USD | 66,030.00 USD | 184,950.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.10` | 49,650,000.00 USD | 49,650,000.00 USD | 123,170.00 USD | 166,390.00 USD | 56,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.90` | 50,170,000.00 USD | 50,170,000.00 USD | 322,090.00 USD | 52,730.00 USD | 139,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `766.70` | 51,140,000.00 USD | 51,140,000.00 USD | 585,340.00 USD | 134,040.00 USD | 256,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.50` | 51,890,000.00 USD | 51,890,000.00 USD | 618,250.00 USD | 0.00 USD | 131,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.30` | 52,430,000.00 USD | 52,430,000.00 USD | 433,190.00 USD | 39,510.00 USD | 65,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 300.48 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.10` | 52,640,000.00 USD | 52,640,000.00 USD | 154,200.00 USD | 35,430.00 USD | 21,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.90` | 52,860,000.00 USD | 52,860,000.00 USD | 131,210.00 USD | 69,130.00 USD | 18,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 3,340.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.70` | 53,440,000.00 USD | 53,440,000.00 USD | 238,480.00 USD | 31,140.00 USD | 307,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.50` | 54,240,000.00 USD | 54,240,000.00 USD | 46,740.00 USD | 106,050.00 USD | 645,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 9,260.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.30` | 54,530,000.00 USD | 54,530,000.00 USD | 183,380.00 USD | 95,640.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 2,450.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.10` | 55,330,000.00 USD | 55,330,000.00 USD | 695,920.00 USD | 61,870.00 USD | 40,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 2,200.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `773.90` | 55,840,000.00 USD | 55,840,000.00 USD | 458,230.00 USD | 22,230.00 USD | 27,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.70` | 56,160,000.00 USD | 56,160,000.00 USD | 187,910.00 USD | 41,190.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.50` | 56,440,000.00 USD | 56,440,000.00 USD | 173,850.00 USD | 24,070.00 USD | 84,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 544.40 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.30` | 56,610,000.00 USD | 56,610,000.00 USD | 95,800.00 USD | 13,880.00 USD | 54,090.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 89,520.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.10` | 56,940,000.00 USD | 56,940,000.00 USD | 234,980.00 USD | 26,170.00 USD | 69,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `777.90` | 58,400,000.00 USD | 58,400,000.00 USD | 979,430.00 USD | 146,900.00 USD | 335,110.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 8,100.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.70` | 58,800,000.00 USD | 58,800,000.00 USD | 348,100.00 USD | 23,830.00 USD | 29,200.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.50` | 59,420,000.00 USD | 59,420,000.00 USD | 486,990.00 USD | 40,830.00 USD | 92,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `780.30` | 59,570,000.00 USD | 59,570,000.00 USD | 24,240.00 USD | 73,560.00 USD | 56,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 4,150.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.10` | 60,030,000.00 USD | 60,030,000.00 USD | 327,000.00 USD | 61,630.00 USD | 68,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `781.90` | 60,480,000.00 USD | 60,480,000.00 USD | 176,980.00 USD | 22,830.00 USD | 251,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.70` | 60,850,000.00 USD | 60,850,000.00 USD | 287,580.00 USD | 18,800.00 USD | 58,590.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.50` | 60,970,000.00 USD | 60,970,000.00 USD | 113,880.00 USD | 0.00 USD | 12,350.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.30` | 61,250,000.00 USD | 61,250,000.00 USD | 279,290.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 743.71 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.10` | 61,390,000.00 USD | 61,390,000.00 USD | 138,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 1,750.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `785.90` | 61,510,000.00 USD | 61,510,000.00 USD | 113,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,780.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `786.70` | 61,550,000.00 USD | 61,550,000.00 USD | 34,710.00 USD | 10,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.90` | 82,500,000.00 USD | 82,500,000.00 USD | 601,980.00 USD | 28,250.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `787.50` | 61,930,000.00 USD | 61,930,000.00 USD | 350,030.00 USD | 33,090.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.90` | 82,910,000.00 USD | 82,910,000.00 USD | 261,000.00 USD | 56,730.00 USD | 91,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `788.30` | 62,340,000.00 USD | 62,340,000.00 USD | 68,150.00 USD | 0.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `788.90` | 83,800,000.00 USD | 83,800,000.00 USD | 750,800.00 USD | 111,010.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 798.18 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `789.90` | 84,470,000.00 USD | 84,470,000.00 USD | 327,320.00 USD | 99,920.00 USD | 244,650.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.90` | 85,300,000.00 USD | 85,300,000.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 86,260,000.00 USD | 86,260,000.00 USD | 841,380.00 USD | 16,830.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `792.50` | 1,870.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `792.90` | 86,480,000.00 USD | 86,480,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 1,280.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.90` | 86,640,000.00 USD | 86,640,000.00 USD | 166,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.90` | 86,900,000.00 USD | 86,900,000.00 USD | 236,740.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 97,360.00 USD | 4,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `795.90` | 87,160,000.00 USD | 87,160,000.00 USD | 93,020.00 USD | 14,650.00 USD | 154,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 321,580.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.90` | 87,250,000.00 USD | 87,250,000.00 USD | 62,760.00 USD | 33,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,760.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.90` | 87,360,000.00 USD | 87,360,000.00 USD | 103,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 901.84 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `800.50` | 28,250.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,410.00 USD | 4,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `802.50` | 778,990.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `803.50` | 1,350.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,770.00 USD | 5,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `807.50` | 738.06 USD | 5,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `809.50` | 173.23 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `812.50` | 434.69 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `815.50` | 8,150.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `818.50` | 7,720.00 USD | 5,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,710.00 USD | 5,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `822.50` | 3,540.00 USD | 5,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `826.50` | 536,790.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `828.50` | 87,650.00 USD | 6,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `832.50` | 2,910.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 3,570.00 USD | 6,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 6,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `840.50` | 11,370.00 USD | 6,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,830.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 1,750.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 1,160.00 USD | 6,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `846.50` | 34,180.00 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 393.78 USD | 6,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 2,110.00 USD | 6,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `856.50` | 34,780.00 USD | 6,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 523,680.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 6,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `863.50` | 289,320.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 326.69 USD | 7,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 716,240.00 USD | 7,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 180,240.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,580.00 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `889.50` | 22,480.00 USD | 7,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 3,950.00 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 554.86 USD | 7,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 223,880.00 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 249.23 USD | 8,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 126,180.00 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 8,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 12,810.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `901.50` | 170,160.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `903.50` | 6,030.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 63,930.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `905.50` | 37,150.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 313.65 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `907.50` | 6,470.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 2,420.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 34,790.00 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `912.50` | 116.80 USD | 8,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 44,350.00 USD | 8,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 651.81 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 956.93 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 69,290.00 USD | 8,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `936.50` | 121,750.00 USD | 8,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `938.50` | 959.15 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `946.50` | 2,690.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `952.50` | 6,860.00 USD | 8,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `954.50` | 18,890.00 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `956.50` | 203.73 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `957.50` | 340.87 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `959.50` | 114.18 USD | 8,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 3,210.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `971.50` | 1,940.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `974.50` | 180.28 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `978.50` | 60,090.00 USD | 9,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 1,100.00 USD | 9,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `988.50` | 14,370.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 9,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,140.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 975.62 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 313.58 USD | 9,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 22,340.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 9,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 437,340.00 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 620.69 USD | 9,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1001.50` | 13,290.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 1,070.00 USD | 9,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 29,110.00 USD | 9,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,370.00 USD | 9,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 760,880.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 10,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 720,280.00 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1033.50` | 498.15 USD | 11,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1044.50` | 80,330.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1059.50` | 7,010.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1062.50` | 635.38 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,760.00 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1068.50` | 131.43 USD | 11,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1075.50` | 120.46 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1079.50` | 69,000.00 USD | 11,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 11,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 16,230.00 USD | 11,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 121,730.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1096.50` | 810.31 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1107.50` | 75,590.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1111.50` | 1,570.00 USD | 11,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1114.50` | 60,260.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1115.50` | 116,010.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1119.50` | 1,970.00 USD | 12,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1120.50` | 19,970.00 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1131.50` | 151.62 USD | 12,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1138.50` | 243.64 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1141.50` | 1,530.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1157.50` | 11,750.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1162.50` | 155.78 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1165.50` | 121.21 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1177.50` | 5,040.00 USD | 12,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1199.50` | 169.13 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1200.50` | 58,000.00 USD | 12,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1202.50` | 118,760.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1215.50` | 42,540.00 USD | 12,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1217.50` | 30,420.00 USD | 12,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1222.50` | 21,230.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 1,030.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1228.50` | 3,730.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1246.50` | 2,660.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 2,050.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1253.50` | 200.56 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1256.50` | 5,020.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1261.50` | 113,530.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 6,850.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1265.50` | 1,270.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1266.50` | 24,590.00 USD | 12,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1280.50` | 19,130.00 USD | 12,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1281.50` | 109,320.00 USD | 12,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1284.50` | 61,810.00 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1287.50` | 348.91 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 13,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1296.50` | 25,930.00 USD | 13,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1300.50` | 1,830.00 USD | 13,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1302.50` | 1,840,000.00 USD | 14,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1303.50` | 18,340.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1306.50` | 4,040.00 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1307.50` | 226.20 USD | 14,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1309.50` | 91,670.00 USD | 14,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1311.50` | 166,610.00 USD | 15,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1323.50` | 2,650.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 138.06 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 289.61 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 54,070.00 USD | 15,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1342.50` | 58,390.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1347.50` | 6,740.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1359.50` | 121.00 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1368.50` | 4,110.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1399.50` | 4,840.00 USD | 15,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 15,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1406.50` | 253,170.00 USD | 15,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1407.50` | 516.55 USD | 15,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `141.50` | 5,460,000.00 USD | 0.00 USD | 19,800.00 USD | `-79.88%` | `139,945,000,000.00` |
| `Live` | `Long` | `142.50` | 5,440,000.00 USD | 0.00 USD | 273.03 USD | `-79.74%` | `1,916,000,000.00` |
| `Live` | `Long` | `143.50` | 5,440,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.60%` | `20,000,000,000.00` |
| `Live` | `Long` | `145.50` | 5,440,000.00 USD | 0.00 USD | 6,150.00 USD | `-79.31%` | `42,261,000,000.00` |
| `Live` | `Long` | `156.50` | 5,430,000.00 USD | 0.00 USD | 435,260.00 USD | `-77.75%` | `2,781,237,000,000.00` |
| `Live` | `Long` | `158.50` | 5,000,000.00 USD | 0.00 USD | 95,100.00 USD | `-77.46%` | `600,000,000,000.00` |
| `Live` | `Long` | `165.50` | 4,900,000.00 USD | 0.00 USD | 1,000.00 USD | `-76.47%` | `6,050,000,000.00` |
| `Live` | `Long` | `170.50` | 4,900,000.00 USD | 0.00 USD | 101.79 USD | `-75.76%` | `597,000,000.00` |
| `Live` | `Long` | `173.50` | 4,900,000.00 USD | 0.00 USD | 6,200.00 USD | `-75.33%` | `35,715,000,000.00` |
| `Live` | `Long` | `178.50` | 4,900,000.00 USD | 0.00 USD | 239.90 USD | `-74.62%` | `1,344,000,000.00` |
| `Live` | `Long` | `189.50` | 4,900,000.00 USD | 0.00 USD | 539.51 USD | `-73.06%` | `2,847,000,000.00` |
| `Live` | `Long` | `202.50` | 4,890,000.00 USD | 0.00 USD | 20,250.00 USD | `-71.21%` | `100,000,000,000.00` |
| `Live` | `Long` | `204.50` | 4,870,000.00 USD | 0.00 USD | 310,870.00 USD | `-70.92%` | `1,520,143,000,000.00` |
| `Live` | `Long` | `209.50` | 4,560,000.00 USD | 0.00 USD | 257.06 USD | `-70.21%` | `1,227,000,000.00` |
| `Live` | `Long` | `219.50` | 4,560,000.00 USD | 0.00 USD | 191.18 USD | `-68.79%` | `871,000,000.00` |
| `Live` | `Long` | `226.50` | 4,560,000.00 USD | 0.00 USD | 874.29 USD | `-67.79%` | `3,860,000,000.00` |
| `Live` | `Long` | `229.50` | 4,560,000.00 USD | 0.00 USD | 229,500.00 USD | `-67.37%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `234.50` | 4,330,000.00 USD | 0.00 USD | 161.10 USD | `-66.66%` | `687,000,000.00` |
| `Live` | `Long` | `243.50` | 4,330,000.00 USD | 0.00 USD | 8,310.00 USD | `-65.38%` | `34,129,000,000.00` |
| `Live` | `Long` | `249.50` | 4,320,000.00 USD | 0.00 USD | 998.00 USD | `-64.52%` | `4,000,000,000.00` |
| `Live` | `Long` | `250.50` | 4,320,000.00 USD | 0.00 USD | 1,320.00 USD | `-64.38%` | `5,281,000,000.00` |
| `Live` | `Long` | `262.50` | 4,320,000.00 USD | 0.00 USD | 399.26 USD | `-62.68%` | `1,521,000,000.00` |
| `Live` | `Long` | `268.50` | 4,320,000.00 USD | 0.00 USD | 21,280.00 USD | `-61.82%` | `79,269,000,000.00` |
| `Live` | `Long` | `274.50` | 4,300,000.00 USD | 0.00 USD | 10,980.00 USD | `-60.97%` | `40,000,000,000.00` |
| `Live` | `Long` | `277.50` | 4,290,000.00 USD | 0.00 USD | 341.05 USD | `-60.54%` | `1,229,000,000.00` |
| `Live` | `Long` | `297.50` | 4,290,000.00 USD | 0.00 USD | 20,660.00 USD | `-57.70%` | `69,447,000,000.00` |
| `Live` | `Long` | `303.50` | 4,270,000.00 USD | 0.00 USD | 451.91 USD | `-56.85%` | `1,489,000,000.00` |
| `Live` | `Long` | `310.50` | 4,270,000.00 USD | 0.00 USD | 159,800.00 USD | `-55.85%` | `514,646,000,000.00` |
| `Live` | `Long` | `312.50` | 4,110,000.00 USD | 0.00 USD | 500.00 USD | `-55.57%` | `1,600,000,000.00` |
| `Live` | `Long` | `313.50` | 4,110,000.00 USD | 0.00 USD | 127.59 USD | `-55.42%` | `407,000,000.00` |
| `Live` | `Long` | `326.50` | 4,110,000.00 USD | 0.00 USD | 500.85 USD | `-53.58%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,110,000.00 USD | 0.00 USD | 6,500.00 USD | `-53.43%` | `19,844,000,000.00` |
| `Live` | `Long` | `332.50` | 4,100,000.00 USD | 0.00 USD | 376.06 USD | `-52.72%` | `1,131,000,000.00` |
| `Live` | `Long` | `342.50` | 4,100,000.00 USD | 0.00 USD | 650.75 USD | `-51.30%` | `1,900,000,000.00` |
| `Live` | `Long` | `344.50` | 4,100,000.00 USD | 0.00 USD | 121.61 USD | `-51.02%` | `353,000,000.00` |
| `Live` | `Long` | `345.50` | 4,100,000.00 USD | 0.00 USD | 2,040.00 USD | `-50.87%` | `5,914,000,000.00` |
| `Live` | `Long` | `347.50` | 4,100,000.00 USD | 0.00 USD | 9,580.00 USD | `-50.59%` | `27,554,000,000.00` |
| `Live` | `Long` | `359.50` | 4,090,000.00 USD | 0.00 USD | 212.10 USD | `-48.88%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,090,000.00 USD | 0.00 USD | 340.60 USD | `-48.31%` | `937,000,000.00` |
| `Live` | `Long` | `366.50` | 4,090,000.00 USD | 0.00 USD | 549.75 USD | `-47.89%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 4,090,000.00 USD | 0.00 USD | 17,420.00 USD | `-47.75%` | `47,408,000,000.00` |
| `Live` | `Long` | `371.50` | 4,070,000.00 USD | 0.00 USD | 10,480.00 USD | `-47.18%` | `28,204,000,000.00` |
| `Live` | `Long` | `373.50` | 4,060,000.00 USD | 0.00 USD | 15,780.00 USD | `-46.89%` | `42,262,000,000.00` |
| `Live` | `Long` | `374.50` | 4,040,000.00 USD | 0.00 USD | 1,820.00 USD | `-46.75%` | `4,868,000,000.00` |
| `Live` | `Long` | `375.50` | 4,040,000.00 USD | 0.00 USD | 16,900.00 USD | `-46.61%` | `45,000,000,000.00` |
| `Live` | `Long` | `377.50` | 4,020,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.32%` | `3,716,000,000.00` |
| `Live` | `Long` | `378.50` | 4,020,000.00 USD | 0.00 USD | 643.45 USD | `-46.18%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,020,000.00 USD | 0.00 USD | 1,910.00 USD | `-45.76%` | `5,000,000,000.00` |
| `Live` | `Long` | `382.50` | 4,020,000.00 USD | 0.00 USD | 10,870.00 USD | `-45.61%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 4,010,000.00 USD | 0.00 USD | 2,620.00 USD | `-45.33%` | `6,809,000,000.00` |
| `Live` | `Long` | `385.50` | 4,010,000.00 USD | 0.00 USD | 341.17 USD | `-45.19%` | `885,000,000.00` |
| `Live` | `Long` | `386.50` | 4,010,000.00 USD | 0.00 USD | 531.44 USD | `-45.04%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 4,010,000.00 USD | 0.00 USD | 392.54 USD | `-44.90%` | `1,013,000,000.00` |
| `Live` | `Long` | `390.50` | 4,010,000.00 USD | 0.00 USD | 3,370.00 USD | `-44.48%` | `8,638,000,000.00` |
| `Live` | `Long` | `392.50` | 4,000,000.00 USD | 0.00 USD | 103.62 USD | `-44.19%` | `264,000,000.00` |
| `Live` | `Long` | `393.50` | 4,000,000.00 USD | 0.00 USD | 600.48 USD | `-44.05%` | `1,526,000,000.00` |
| `Live` | `Long` | `394.50` | 4,000,000.00 USD | 0.00 USD | 4,240.00 USD | `-43.91%` | `10,744,000,000.00` |
| `Live` | `Long` | `395.50` | 4,000,000.00 USD | 0.00 USD | 7,670.00 USD | `-43.76%` | `19,400,000,000.00` |
| `Live` | `Long` | `396.50` | 3,990,000.00 USD | 0.00 USD | 317.20 USD | `-43.62%` | `800,000,000.00` |
| `Live` | `Long` | `397.50` | 3,990,000.00 USD | 0.00 USD | 522.32 USD | `-43.48%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 3,990,000.00 USD | 0.00 USD | 603.64 USD | `-43.20%` | `1,511,000,000.00` |
| `Live` | `Long` | `403.50` | 3,990,000.00 USD | 0.00 USD | 102.09 USD | `-42.63%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 3,990,000.00 USD | 0.00 USD | 613.02 USD | `-41.77%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 3,990,000.00 USD | 0.00 USD | 105.91 USD | `-41.63%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 3,990,000.00 USD | 0.00 USD | 3,490.00 USD | `-41.35%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 3,980,000.00 USD | 0.00 USD | 9,800.00 USD | `-41.20%` | `23,702,000,000.00` |
| `Live` | `Long` | `414.50` | 3,970,000.00 USD | 0.00 USD | 4,590.00 USD | `-41.06%` | `11,085,000,000.00` |
| `Live` | `Long` | `416.50` | 3,970,000.00 USD | 0.00 USD | 2,350.00 USD | `-40.78%` | `5,644,000,000.00` |
| `Live` | `Long` | `417.50` | 3,970,000.00 USD | 0.00 USD | 4,780.00 USD | `-40.64%` | `11,448,000,000.00` |
| `Live` | `Long` | `418.50` | 3,960,000.00 USD | 0.00 USD | 318.06 USD | `-40.49%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 3,960,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.35%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 3,960,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.07%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 3,960,000.00 USD | 0.00 USD | 1,440.00 USD | `-39.93%` | `3,419,000,000.00` |
| `Live` | `Long` | `423.50` | 3,960,000.00 USD | 0.00 USD | 29,640.00 USD | `-39.78%` | `70,000,000,000.00` |
| `Live` | `Long` | `425.50` | 3,930,000.00 USD | 0.00 USD | 7,480.00 USD | `-39.50%` | `17,576,000,000.00` |
| `Live` | `Long` | `426.50` | 3,920,000.00 USD | 0.00 USD | 31,670.00 USD | `-39.36%` | `74,245,000,000.00` |
| `Live` | `Long` | `429.50` | 3,890,000.00 USD | 0.00 USD | 4,200.00 USD | `-38.93%` | `9,769,000,000.00` |
| `Live` | `Long` | `430.50` | 3,880,000.00 USD | 0.00 USD | 545.01 USD | `-38.79%` | `1,266,000,000.00` |
| `Live` | `Long` | `436.50` | 3,880,000.00 USD | 0.00 USD | 133.13 USD | `-37.93%` | `305,000,000.00` |
| `Live` | `Long` | `438.50` | 3,880,000.00 USD | 0.00 USD | 1,790.00 USD | `-37.65%` | `4,087,000,000.00` |
| `Live` | `Long` | `442.50` | 3,880,000.00 USD | 0.00 USD | 935.89 USD | `-37.08%` | `2,115,000,000.00` |
| `Live` | `Long` | `447.50` | 3,880,000.00 USD | 0.00 USD | 223.75 USD | `-36.37%` | `500,000,000.00` |
| `Live` | `Long` | `448.50` | 3,880,000.00 USD | 0.00 USD | 3,350.00 USD | `-36.23%` | `7,470,000,000.00` |
| `Live` | `Long` | `451.50` | 3,880,000.00 USD | 0.00 USD | 1,470.00 USD | `-35.80%` | `3,259,000,000.00` |
| `Live` | `Long` | `456.50` | 3,870,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.09%` | `10,359,000,000.00` |
| `Live` | `Long` | `463.50` | 3,870,000.00 USD | 0.00 USD | 927.00 USD | `-34.10%` | `2,000,000,000.00` |
| `Live` | `Long` | `469.50` | 3,870,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.24%` | `9,301,000,000.00` |
| `Live` | `Long` | `472.50` | 3,860,000.00 USD | 0.00 USD | 203.17 USD | `-32.82%` | `430,000,000.00` |
| `Live` | `Long` | `475.50` | 3,860,000.00 USD | 0.00 USD | 5,320.00 USD | `-32.39%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,860,000.00 USD | 0.00 USD | 1,300.00 USD | `-31.54%` | `2,710,000,000.00` |
| `Live` | `Long` | `484.50` | 3,860,000.00 USD | 0.00 USD | 2,840.00 USD | `-31.11%` | `5,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,850,000.00 USD | 0.00 USD | 2,890.00 USD | `-30.97%` | `5,947,000,000.00` |
| `Live` | `Long` | `486.50` | 3,850,000.00 USD | 0.00 USD | 693.75 USD | `-30.83%` | `1,426,000,000.00` |
| `Live` | `Long` | `487.50` | 3,850,000.00 USD | 0.00 USD | 2,070.00 USD | `-30.68%` | `4,238,000,000.00` |
| `Live` | `Long` | `488.50` | 3,850,000.00 USD | 0.00 USD | 2,300.00 USD | `-30.54%` | `4,712,000,000.00` |
| `Live` | `Long` | `493.50` | 3,850,000.00 USD | 0.00 USD | 1,840.00 USD | `-29.83%` | `3,720,000,000.00` |
| `Live` | `Long` | `498.50` | 3,840,000.00 USD | 0.00 USD | 11,260.00 USD | `-29.12%` | `22,583,000,000.00` |
| `Live` | `Long` | `499.50` | 3,830,000.00 USD | 0.00 USD | 4,370.00 USD | `-28.98%` | `8,757,000,000.00` |
| `Live` | `Long` | `500.50` | 3,830,000.00 USD | 0.00 USD | 186.69 USD | `-28.83%` | `373,000,000.00` |
| `Live` | `Long` | `501.50` | 3,830,000.00 USD | 0.00 USD | 14,130.00 USD | `-28.69%` | `28,185,000,000.00` |
| `Live` | `Long` | `502.50` | 3,810,000.00 USD | 0.00 USD | 109.04 USD | `-28.55%` | `217,000,000.00` |
| `Live` | `Long` | `504.50` | 3,810,000.00 USD | 0.00 USD | 4,380.00 USD | `-28.27%` | `8,678,000,000.00` |
| `Live` | `Long` | `505.50` | 3,810,000.00 USD | 0.00 USD | 5,760.00 USD | `-28.12%` | `11,387,000,000.00` |
| `Live` | `Long` | `506.50` | 3,800,000.00 USD | 0.00 USD | 683.27 USD | `-27.98%` | `1,349,000,000.00` |
| `Live` | `Long` | `507.50` | 3,800,000.00 USD | 0.00 USD | 2,760.00 USD | `-27.84%` | `5,431,000,000.00` |
| `Live` | `Long` | `508.50` | 3,800,000.00 USD | 0.00 USD | 483.58 USD | `-27.70%` | `951,000,000.00` |
| `Live` | `Long` | `509.50` | 3,800,000.00 USD | 0.00 USD | 3,100.00 USD | `-27.55%` | `6,091,000,000.00` |
| `Live` | `Long` | `510.50` | 3,800,000.00 USD | 0.00 USD | 4,080.00 USD | `-27.41%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,790,000.00 USD | 0.00 USD | 5,180.00 USD | `-27.27%` | `10,118,000,000.00` |
| `Live` | `Long` | `512.50` | 3,790,000.00 USD | 0.00 USD | 73,860.00 USD | `-27.13%` | `144,110,000,000.00` |
| `Live` | `Long` | `513.50` | 3,710,000.00 USD | 0.00 USD | 2,520.00 USD | `-26.99%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,710,000.00 USD | 0.00 USD | 42,080.00 USD | `-26.84%` | `81,796,000,000.00` |
| `Live` | `Long` | `515.50` | 3,670,000.00 USD | 0.00 USD | 6,470.00 USD | `-26.70%` | `12,554,000,000.00` |
| `Live` | `Long` | `517.50` | 3,660,000.00 USD | 0.00 USD | 22,650.00 USD | `-26.42%` | `43,765,000,000.00` |
| `Live` | `Long` | `518.50` | 3,640,000.00 USD | 0.00 USD | 263.92 USD | `-26.28%` | `509,000,000.00` |
| `Live` | `Long` | `519.50` | 3,640,000.00 USD | 0.00 USD | 703.92 USD | `-26.13%` | `1,355,000,000.00` |
| `Live` | `Long` | `520.50` | 3,640,000.00 USD | 0.00 USD | 272.22 USD | `-25.99%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 3,640,000.00 USD | 0.00 USD | 838.05 USD | `-25.85%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 3,640,000.00 USD | 0.00 USD | 64,750.00 USD | `-25.71%` | `123,933,000,000.00` |
| `Live` | `Long` | `524.50` | 3,570,000.00 USD | 0.00 USD | 833.43 USD | `-25.42%` | `1,589,000,000.00` |
| `Live` | `Long` | `525.50` | 3,570,000.00 USD | 0.00 USD | 2,160.00 USD | `-25.28%` | `4,110,000,000.00` |
| `Live` | `Long` | `526.50` | 3,570,000.00 USD | 0.00 USD | 1,700.00 USD | `-25.14%` | `3,234,000,000.00` |
| `Live` | `Long` | `529.50` | 3,570,000.00 USD | 0.00 USD | 97,260.00 USD | `-24.71%` | `183,680,000,000.00` |
| `Live` | `Long` | `530.50` | 3,470,000.00 USD | 0.00 USD | 21,140.00 USD | `-24.57%` | `39,850,000,000.00` |
| `Live` | `Long` | `531.50` | 3,450,000.00 USD | 0.00 USD | 536.82 USD | `-24.43%` | `1,010,000,000.00` |
| `Live` | `Long` | `532.50` | 3,450,000.00 USD | 0.00 USD | 181,920.00 USD | `-24.28%` | `341,633,000,000.00` |
| `Live` | `Long` | `534.50` | 3,270,000.00 USD | 0.00 USD | 555.35 USD | `-24.00%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,270,000.00 USD | 0.00 USD | 100.14 USD | `-23.86%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 3,270,000.00 USD | 0.00 USD | 490.94 USD | `-23.29%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,270,000.00 USD | 0.00 USD | 471.32 USD | `-23.15%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,270,000.00 USD | 0.00 USD | 10,350.00 USD | `-22.72%` | `19,044,000,000.00` |
| `Live` | `Long` | `544.50` | 3,260,000.00 USD | 0.00 USD | 210,830.00 USD | `-22.58%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 3,050,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.44%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,040,000.00 USD | 0.00 USD | 530.11 USD | `-22.29%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,040,000.00 USD | 0.00 USD | 1,980.00 USD | `-22.01%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 3,040,000.00 USD | 0.00 USD | 1,370.00 USD | `-21.87%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,040,000.00 USD | 0.00 USD | 633.63 USD | `-21.73%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,040,000.00 USD | 0.00 USD | 1,250.00 USD | `-21.58%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 3,040,000.00 USD | 0.00 USD | 12,560.00 USD | `-21.44%` | `22,739,000,000.00` |
| `Live` | `Long` | `553.50` | 3,030,000.00 USD | 0.00 USD | 2,740.00 USD | `-21.30%` | `4,955,000,000.00` |
| `Live` | `Long` | `556.50` | 3,020,000.00 USD | 0.00 USD | 5,670.00 USD | `-20.87%` | `10,193,000,000.00` |
| `Live` | `Long` | `560.50` | 3,020,000.00 USD | 0.00 USD | 582.36 USD | `-20.30%` | `1,039,000,000.00` |
| `Live` | `Long` | `563.50` | 3,020,000.00 USD | 0.00 USD | 281.75 USD | `-19.88%` | `500,000,000.00` |
| `Live` | `Long` | `567.50` | 3,020,000.00 USD | 0.00 USD | 107.83 USD | `-19.31%` | `190,000,000.00` |
| `Live` | `Long` | `569.50` | 3,020,000.00 USD | 0.00 USD | 144.08 USD | `-19.02%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 3,020,000.00 USD | 0.00 USD | 721,240.00 USD | `-18.74%` | `1,262,009,000,000.00` |
| `Live` | `Long` | `574.50` | 2,290,000.00 USD | 0.00 USD | 323.44 USD | `-18.31%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 2,290,000.00 USD | 0.00 USD | 5,270.00 USD | `-18.03%` | `9,149,000,000.00` |
| `Live` | `Long` | `577.50` | 2,290,000.00 USD | 0.00 USD | 5,780.00 USD | `-17.89%` | `10,000,000,000.00` |
| `Live` | `Long` | `578.50` | 2,280,000.00 USD | 0.00 USD | 1,850.00 USD | `-17.74%` | `3,202,000,000.00` |
| `Live` | `Long` | `579.50` | 2,280,000.00 USD | 0.00 USD | 164,400.00 USD | `-17.60%` | `283,700,000,000.00` |
| `Live` | `Long` | `580.50` | 2,120,000.00 USD | 0.00 USD | 53,080.00 USD | `-17.46%` | `91,440,000,000.00` |
| `Live` | `Long` | `582.50` | 2,060,000.00 USD | 0.00 USD | 690.26 USD | `-17.18%` | `1,185,000,000.00` |
| `Live` | `Long` | `583.50` | 2,060,000.00 USD | 0.00 USD | 3,060.00 USD | `-17.03%` | `5,239,000,000.00` |
| `Live` | `Long` | `585.50` | 2,060,000.00 USD | 0.00 USD | 210.19 USD | `-16.75%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,060,000.00 USD | 0.00 USD | 2,360.00 USD | `-16.61%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,060,000.00 USD | 0.00 USD | 5,530.00 USD | `-16.46%` | `9,416,000,000.00` |
| `Live` | `Long` | `588.50` | 2,050,000.00 USD | 0.00 USD | 397.24 USD | `-16.32%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 2,050,000.00 USD | 0.00 USD | 10,820.00 USD | `-16.18%` | `18,352,000,000.00` |
| `Live` | `Long` | `590.50` | 2,040,000.00 USD | 0.00 USD | 2,420.00 USD | `-16.04%` | `4,106,000,000.00` |
| `Live` | `Long` | `593.50` | 2,040,000.00 USD | 0.00 USD | 44,720.00 USD | `-15.61%` | `75,354,000,000.00` |
| `Live` | `Long` | `595.50` | 1,990,000.00 USD | 0.00 USD | 3,000.00 USD | `-15.33%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,990,000.00 USD | 0.00 USD | 423.52 USD | `-15.18%` | `710,000,000.00` |
| `Live` | `Long` | `597.50` | 1,990,000.00 USD | 0.00 USD | 2,480.00 USD | `-15.04%` | `4,156,000,000.00` |
| `Live` | `Long` | `598.50` | 1,990,000.00 USD | 0.00 USD | 791.22 USD | `-14.90%` | `1,322,000,000.00` |
| `Live` | `Long` | `600.50` | 1,990,000.00 USD | 0.00 USD | 945.19 USD | `-14.62%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,990,000.00 USD | 0.00 USD | 16,880.00 USD | `-14.47%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,970,000.00 USD | 0.00 USD | 222.32 USD | `-14.33%` | `369,000,000.00` |
| `Live` | `Long` | `603.50` | 1,970,000.00 USD | 0.00 USD | 22,860.00 USD | `-14.19%` | `37,877,000,000.00` |
| `Live` | `Long` | `604.50` | 1,950,000.00 USD | 0.00 USD | 2,780.00 USD | `-14.05%` | `4,607,000,000.00` |
| `Live` | `Long` | `605.50` | 1,940,000.00 USD | 0.00 USD | 58,420.00 USD | `-13.90%` | `96,477,000,000.00` |
| `Live` | `Long` | `606.50` | 1,890,000.00 USD | 0.00 USD | 1,880.00 USD | `-13.76%` | `3,092,000,000.00` |
| `Live` | `Long` | `609.50` | 1,880,000.00 USD | 0.00 USD | 213.32 USD | `-13.34%` | `350,000,000.00` |
| `Live` | `Long` | `610.50` | 1,880,000.00 USD | 0.00 USD | 4,270.00 USD | `-13.19%` | `7,002,000,000.00` |
| `Live` | `Long` | `611.50` | 1,880,000.00 USD | 0.00 USD | 1,580.00 USD | `-13.05%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,880,000.00 USD | 0.00 USD | 12,250.00 USD | `-12.91%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,860,000.00 USD | 0.00 USD | 120.25 USD | `-12.77%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,860,000.00 USD | 0.00 USD | 4,280.00 USD | `-12.63%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,860,000.00 USD | 0.00 USD | 1,540.00 USD | `-12.34%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,860,000.00 USD | 0.00 USD | 156.23 USD | `-12.20%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,860,000.00 USD | 0.00 USD | 932.70 USD | `-12.06%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,860,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.91%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,860,000.00 USD | 0.00 USD | 6,520.00 USD | `-11.77%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,850,000.00 USD | 0.00 USD | 13,930.00 USD | `-11.63%` | `22,412,000,000.00` |
| `Live` | `Long` | `623.50` | 1,840,000.00 USD | 0.00 USD | 415.25 USD | `-11.35%` | `666,000,000.00` |
| `Live` | `Long` | `624.50` | 1,840,000.00 USD | 0.00 USD | 3,270.00 USD | `-11.20%` | `5,239,000,000.00` |
| `Live` | `Long` | `625.50` | 1,830,000.00 USD | 0.00 USD | 14,200.00 USD | `-11.06%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,820,000.00 USD | 0.00 USD | 964.81 USD | `-10.92%` | `1,540,000,000.00` |
| `Live` | `Long` | `628.50` | 1,820,000.00 USD | 0.00 USD | 381.50 USD | `-10.63%` | `607,000,000.00` |
| `Live` | `Long` | `630.50` | 1,820,000.00 USD | 0.00 USD | 153.21 USD | `-10.35%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,820,000.00 USD | 0.00 USD | 2,900.00 USD | `-10.21%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,810,000.00 USD | 0.00 USD | 3,560.00 USD | `-10.07%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,810,000.00 USD | 0.00 USD | 5,900.00 USD | `-9.78%` | `9,302,000,000.00` |
| `Live` | `Long` | `635.50` | 1,800,000.00 USD | 0.00 USD | 155.06 USD | `-9.64%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,800,000.00 USD | 0.00 USD | 1,110.00 USD | `-9.50%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,800,000.00 USD | 0.00 USD | 305.36 USD | `-9.35%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,800,000.00 USD | 0.00 USD | 6,710.00 USD | `-9.21%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,800,000.00 USD | 0.00 USD | 1,490.00 USD | `-9.07%` | `2,333,000,000.00` |
| `Live` | `Long` | `640.50` | 1,790,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-8.93%` | `2,057,820,000,000.00` |
| `Live` | `Long` | `642.50` | 476,530.00 USD | 0.00 USD | 8,480.00 USD | `-8.64%` | `13,199,000,000.00` |
| `Live` | `Long` | `643.50` | 468,050.00 USD | 0.00 USD | 339.12 USD | `-8.50%` | `527,000,000.00` |
| `Live` | `Long` | `645.50` | 467,710.00 USD | 0.00 USD | 307.26 USD | `-8.22%` | `476,000,000.00` |
| `Live` | `Long` | `646.50` | 467,400.00 USD | 0.00 USD | 155.81 USD | `-8.08%` | `241,000,000.00` |
| `Live` | `Long` | `648.50` | 467,240.00 USD | 0.00 USD | 1,940.00 USD | `-7.79%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 465,310.00 USD | 0.00 USD | 1,620.00 USD | `-7.65%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 463,680.00 USD | 0.00 USD | 587.40 USD | `-7.51%` | `903,000,000.00` |
| `Live` | `Long` | `651.50` | 463,090.00 USD | 0.00 USD | 9,650.00 USD | `-7.36%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 453,450.00 USD | 0.00 USD | 652.50 USD | `-7.22%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 452,800.00 USD | 0.00 USD | 98,240.00 USD | `-7.08%` | `150,322,000,000.00` |
| `Live` | `Long` | `654.50` | 354,560.00 USD | 0.00 USD | 100.14 USD | `-6.94%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 354,460.00 USD | 0.00 USD | 122.58 USD | `-6.80%` | `187,000,000.00` |
| `Live` | `Long` | `658.50` | 354,340.00 USD | 0.00 USD | 15,430.00 USD | `-6.37%` | `23,431,000,000.00` |
| `Live` | `Long` | `659.50` | 338,910.00 USD | 0.00 USD | 45,510.00 USD | `-6.23%` | `69,000,000,000.00` |
| `Live` | `Long` | `660.50` | 293,400.00 USD | 0.00 USD | 3,410.00 USD | `-6.08%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 289,990.00 USD | 0.00 USD | 20,140.00 USD | `-5.94%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 269,850.00 USD | 0.00 USD | 2,850.00 USD | `-5.80%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 267,000.00 USD | 0.00 USD | 21,880.00 USD | `-5.66%` | `32,975,000,000.00` |
| `Live` | `Long` | `664.50` | 245,120.00 USD | 0.00 USD | 10,080.00 USD | `-5.52%` | `15,175,000,000.00` |
| `Live` | `Long` | `665.50` | 235,040.00 USD | 0.00 USD | 6,330.00 USD | `-5.37%` | `9,517,000,000.00` |
| `Live` | `Long` | `666.50` | 228,700.00 USD | 0.00 USD | 1,930.00 USD | `-5.23%` | `2,894,000,000.00` |
| `Live` | `Long` | `667.50` | 226,780.00 USD | 0.00 USD | 1,380.00 USD | `-5.09%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 225,400.00 USD | 0.00 USD | 41,770.00 USD | `-4.95%` | `62,483,000,000.00` |
| `Live` | `Long` | `669.50` | 183,630.00 USD | 0.00 USD | 5,280.00 USD | `-4.80%` | `7,888,000,000.00` |
| `Live` | `Long` | `670.50` | 178,350.00 USD | 0.00 USD | 3,310.00 USD | `-4.66%` | `4,937,000,000.00` |
| `Live` | `Long` | `671.50` | 175,030.00 USD | 0.00 USD | 19,470.00 USD | `-4.52%` | `28,989,000,000.00` |
| `Live` | `Long` | `672.50` | 155,570.00 USD | 0.00 USD | 6,520.00 USD | `-4.38%` | `9,695,000,000.00` |
| `Live` | `Long` | `673.50` | 149,050.00 USD | 0.00 USD | 40,750.00 USD | `-4.24%` | `60,511,000,000.00` |
| `Live` | `Long` | `674.50` | 108,290.00 USD | 0.00 USD | 4,100.00 USD | `-4.09%` | `6,078,000,000.00` |
| `Live` | `Long` | `675.50` | 104,200.00 USD | 0.00 USD | 74,720.00 USD | `-3.95%` | `110,607,000,000.00` |
| `Live` | `Long` | `676.50` | 29,480.00 USD | 0.00 USD | 1,960.00 USD | `-3.81%` | `2,901,000,000.00` |
| `Live` | `Long` | `678.50` | 27,520.00 USD | 0.00 USD | 2,520.00 USD | `-3.52%` | `3,716,000,000.00` |
| `Live` | `Long` | `679.50` | 25,000.00 USD | 0.00 USD | 1,470.00 USD | `-3.38%` | `2,166,000,000.00` |
| `Live` | `Long` | `680.50` | 23,520.00 USD | 0.00 USD | 22,380.00 USD | `-3.24%` | `32,894,000,000.00` |
| `Live` | `Long` | `681.50` | 1,140.00 USD | 0.00 USD | 939.79 USD | `-3.10%` | `1,379,000,000.00` |
| `Live` | `Long` | `700.50` | 200.34 USD | 0.00 USD | 200.34 USD | `-0.40%` | `286,000,000.00` |
| `Live` | `Short` | `705.50` | 10,730.00 USD | 10,730.00 USD | 0.00 USD | `+0.31%` | `15,214,000,000.00` |
| `Live` | `Short` | `712.50` | 13,170.00 USD | 2,440.00 USD | 0.00 USD | `+1.31%` | `3,422,000,000.00` |
| `Live` | `Short` | `720.50` | 13,550.00 USD | 376.82 USD | 0.00 USD | `+2.45%` | `523,000,000.00` |
| `Live` | `Short` | `721.50` | 41,570.00 USD | 28,020.00 USD | 0.00 USD | `+2.59%` | `38,835,000,000.00` |
| `Live` | `Short` | `722.50` | 43,520.00 USD | 1,950.00 USD | 0.00 USD | `+2.73%` | `2,702,000,000.00` |
| `Live` | `Short` | `723.50` | 45,690.00 USD | 2,170.00 USD | 0.00 USD | `+2.87%` | `2,996,000,000.00` |
| `Live` | `Short` | `724.50` | 46,210.00 USD | 525.26 USD | 0.00 USD | `+3.02%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 47,740.00 USD | 1,530.00 USD | 0.00 USD | `+3.16%` | `2,108,000,000.00` |
| `Live` | `Short` | `726.50` | 52,340.00 USD | 4,600.00 USD | 0.00 USD | `+3.30%` | `6,327,000,000.00` |
| `Live` | `Short` | `727.50` | 52,680.00 USD | 342.65 USD | 0.00 USD | `+3.44%` | `471,000,000.00` |
| `Live` | `Short` | `728.50` | 93,760.00 USD | 41,080.00 USD | 0.00 USD | `+3.58%` | `56,385,000,000.00` |
| `Live` | `Short` | `729.50` | 264,770.00 USD | 171,010.00 USD | 0.00 USD | `+3.73%` | `234,425,000,000.00` |
| `Live` | `Short` | `730.50` | 293,270.00 USD | 28,500.00 USD | 0.00 USD | `+3.87%` | `39,009,000,000.00` |
| `Live` | `Short` | `731.50` | 295,310.00 USD | 2,050.00 USD | 0.00 USD | `+4.01%` | `2,797,000,000.00` |
| `Live` | `Short` | `732.50` | 435,610.00 USD | 140,300.00 USD | 0.00 USD | `+4.15%` | `191,538,000,000.00` |
| `Live` | `Short` | `733.50` | 447,880.00 USD | 12,260.00 USD | 0.00 USD | `+4.30%` | `16,721,000,000.00` |
| `Live` | `Short` | `734.50` | 600,560.00 USD | 152,680.00 USD | 0.00 USD | `+4.44%` | `207,869,000,000.00` |
| `Live` | `Short` | `735.50` | 623,160.00 USD | 22,600.00 USD | 0.00 USD | `+4.58%` | `30,729,000,000.00` |
| `Live` | `Short` | `736.50` | 631,830.00 USD | 8,670.00 USD | 0.00 USD | `+4.72%` | `11,775,000,000.00` |
| `Live` | `Short` | `737.50` | 641,140.00 USD | 9,300.00 USD | 0.00 USD | `+4.86%` | `12,615,000,000.00` |
| `Live` | `Short` | `738.50` | 655,260.00 USD | 14,120.00 USD | 0.00 USD | `+5.01%` | `19,120,000,000.00` |
| `Live` | `Short` | `739.50` | 774,740.00 USD | 119,490.00 USD | 0.00 USD | `+5.15%` | `161,580,000,000.00` |
| `Live` | `Short` | `740.50` | 781,510.00 USD | 6,760.00 USD | 0.00 USD | `+5.29%` | `9,131,000,000.00` |
| `Live` | `Short` | `741.50` | 816,710.00 USD | 35,200.00 USD | 0.00 USD | `+5.43%` | `47,470,000,000.00` |
| `Live` | `Short` | `742.50` | 883,260.00 USD | 66,550.00 USD | 0.00 USD | `+5.58%` | `89,634,000,000.00` |
| `Live` | `Short` | `743.50` | 930,490.00 USD | 47,230.00 USD | 0.00 USD | `+5.72%` | `63,520,000,000.00` |
| `Live` | `Short` | `744.50` | 1,050,000.00 USD | 117,700.00 USD | 0.00 USD | `+5.86%` | `158,091,000,000.00` |
| `Live` | `Short` | `745.50` | 1,080,000.00 USD | 30,150.00 USD | 0.00 USD | `+6.00%` | `40,446,000,000.00` |
| `Live` | `Short` | `746.50` | 1,260,000.00 USD | 185,960.00 USD | 0.00 USD | `+6.14%` | `249,111,000,000.00` |
| `Live` | `Short` | `747.50` | 1,270,000.00 USD | 2,010.00 USD | 0.00 USD | `+6.29%` | `2,691,000,000.00` |
| `Live` | `Short` | `748.50` | 1,280,000.00 USD | 12,010.00 USD | 0.00 USD | `+6.43%` | `16,051,000,000.00` |
| `Live` | `Short` | `749.50` | 1,350,000.00 USD | 67,670.00 USD | 0.00 USD | `+6.57%` | `90,291,000,000.00` |
| `Live` | `Short` | `750.50` | 1,920,000.00 USD | 575,140.00 USD | 0.00 USD | `+6.71%` | `766,346,000,000.00` |
| `Live` | `Short` | `751.50` | 1,930,000.00 USD | 11,270.00 USD | 0.00 USD | `+6.85%` | `15,000,000,000.00` |
| `Live` | `Short` | `752.50` | 1,990,000.00 USD | 58,760.00 USD | 0.00 USD | `+7.00%` | `78,091,000,000.00` |
| `Live` | `Short` | `753.50` | 1,990,000.00 USD | 132.62 USD | 0.00 USD | `+7.14%` | `176,000,000.00` |
| `Live` | `Short` | `754.50` | 2,850,000.00 USD | 863,450.00 USD | 0.00 USD | `+7.28%` | `1,144,401,000,000.00` |
| `Live` | `Short` | `755.50` | 2,850,000.00 USD | 144.30 USD | 0.00 USD | `+7.42%` | `191,000,000.00` |
| `Live` | `Short` | `756.50` | 2,860,000.00 USD | 3,750.00 USD | 0.00 USD | `+7.57%` | `4,960,000,000.00` |
| `Live` | `Short` | `757.50` | 3,230,000.00 USD | 367,790.00 USD | 0.00 USD | `+7.71%` | `485,532,000,000.00` |
| `Live` | `Short` | `758.50` | 3,410,000.00 USD | 180,430.00 USD | 0.00 USD | `+7.85%` | `237,882,000,000.00` |
| `Live` | `Short` | `759.50` | 3,410,000.00 USD | 704.82 USD | 0.00 USD | `+7.99%` | `928,000,000.00` |
| `Live` | `Short` | `760.50` | 3,410,000.00 USD | 3,670.00 USD | 0.00 USD | `+8.13%` | `4,822,000,000.00` |
| `Live` | `Short` | `761.50` | 3,410,000.00 USD | 2,360.00 USD | 0.00 USD | `+8.28%` | `3,099,000,000.00` |
| `Live` | `Short` | `762.50` | 3,410,000.00 USD | 367.52 USD | 0.00 USD | `+8.42%` | `482,000,000.00` |
| `Live` | `Short` | `763.50` | 4,020,000.00 USD | 603,420.00 USD | 0.00 USD | `+8.56%` | `790,332,000,000.00` |
| `Live` | `Short` | `766.50` | 4,020,000.00 USD | 2,850.00 USD | 0.00 USD | `+8.99%` | `3,719,000,000.00` |
| `Live` | `Short` | `768.50` | 4,020,000.00 USD | 300.48 USD | 0.00 USD | `+9.27%` | `391,000,000.00` |
| `Live` | `Short` | `770.50` | 4,020,000.00 USD | 3,340.00 USD | 0.00 USD | `+9.56%` | `4,334,000,000.00` |
| `Live` | `Short` | `771.50` | 4,030,000.00 USD | 9,260.00 USD | 0.00 USD | `+9.70%` | `12,000,000,000.00` |
| `Live` | `Short` | `772.50` | 4,040,000.00 USD | 2,450.00 USD | 0.00 USD | `+9.84%` | `3,173,000,000.00` |
| `Live` | `Short` | `773.50` | 4,040,000.00 USD | 2,200.00 USD | 0.00 USD | `+9.98%` | `2,842,000,000.00` |
| `Live` | `Short` | `775.50` | 4,040,000.00 USD | 544.40 USD | 0.00 USD | `+10.27%` | `702,000,000.00` |
| `Live` | `Short` | `776.50` | 4,130,000.00 USD | 89,520.00 USD | 0.00 USD | `+10.41%` | `115,281,000,000.00` |
| `Live` | `Short` | `777.50` | 4,130,000.00 USD | 209.15 USD | 0.00 USD | `+10.55%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 4,140,000.00 USD | 8,100.00 USD | 0.00 USD | `+10.69%` | `10,401,000,000.00` |
| `Live` | `Short` | `780.50` | 4,140,000.00 USD | 4,150.00 USD | 0.00 USD | `+10.98%` | `5,318,000,000.00` |
| `Live` | `Short` | `781.50` | 4,140,000.00 USD | 1,830.00 USD | 0.00 USD | `+11.12%` | `2,337,000,000.00` |
| `Live` | `Short` | `784.50` | 4,140,000.00 USD | 743.71 USD | 0.00 USD | `+11.55%` | `948,000,000.00` |
| `Live` | `Short` | `785.50` | 4,140,000.00 USD | 1,750.00 USD | 0.00 USD | `+11.69%` | `2,227,000,000.00` |
| `Live` | `Short` | `786.50` | 4,150,000.00 USD | 4,780.00 USD | 0.00 USD | `+11.83%` | `6,080,000,000.00` |
| `Live` | `Short` | `788.50` | 4,150,000.00 USD | 1,580.00 USD | 0.00 USD | `+12.12%` | `2,000,000,000.00` |
| `Live` | `Short` | `789.50` | 4,150,000.00 USD | 798.18 USD | 0.00 USD | `+12.26%` | `1,011,000,000.00` |
| `Live` | `Short` | `792.50` | 4,150,000.00 USD | 1,870.00 USD | 0.00 USD | `+12.68%` | `2,355,000,000.00` |
| `Live` | `Short` | `793.50` | 4,150,000.00 USD | 1,280.00 USD | 0.00 USD | `+12.83%` | `1,616,000,000.00` |
| `Live` | `Short` | `795.50` | 4,250,000.00 USD | 97,360.00 USD | 0.00 USD | `+13.11%` | `122,388,000,000.00` |
| `Live` | `Short` | `796.50` | 4,570,000.00 USD | 321,580.00 USD | 0.00 USD | `+13.25%` | `403,741,000,000.00` |
| `Live` | `Short` | `797.50` | 4,580,000.00 USD | 1,760.00 USD | 0.00 USD | `+13.40%` | `2,208,000,000.00` |
| `Live` | `Short` | `799.50` | 4,580,000.00 USD | 901.84 USD | 0.00 USD | `+13.68%` | `1,128,000,000.00` |
| `Live` | `Short` | `800.50` | 4,600,000.00 USD | 28,250.00 USD | 0.00 USD | `+13.82%` | `35,287,000,000.00` |
| `Live` | `Short` | `801.50` | 4,610,000.00 USD | 3,410.00 USD | 0.00 USD | `+13.96%` | `4,250,000,000.00` |
| `Live` | `Short` | `802.50` | 5,390,000.00 USD | 778,990.00 USD | 0.00 USD | `+14.11%` | `970,710,000,000.00` |
| `Live` | `Short` | `803.50` | 5,390,000.00 USD | 1,350.00 USD | 0.00 USD | `+14.25%` | `1,681,000,000.00` |
| `Live` | `Short` | `805.50` | 5,400,000.00 USD | 15,770.00 USD | 0.00 USD | `+14.53%` | `19,581,000,000.00` |
| `Live` | `Short` | `806.50` | 5,410,000.00 USD | 2,890.00 USD | 0.00 USD | `+14.68%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 5,410,000.00 USD | 738.06 USD | 0.00 USD | `+14.82%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 5,420,000.00 USD | 11,780.00 USD | 0.00 USD | `+14.96%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 5,420,000.00 USD | 173.23 USD | 0.00 USD | `+15.10%` | `214,000,000.00` |
| `Live` | `Short` | `812.50` | 5,420,000.00 USD | 434.69 USD | 0.00 USD | `+15.53%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 5,420,000.00 USD | 692.32 USD | 0.00 USD | `+15.81%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 5,430,000.00 USD | 8,150.00 USD | 0.00 USD | `+15.95%` | `9,992,000,000.00` |
| `Live` | `Short` | `816.50` | 5,440,000.00 USD | 15,410.00 USD | 0.00 USD | `+16.10%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 5,440,000.00 USD | 325.37 USD | 0.00 USD | `+16.24%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 5,450,000.00 USD | 7,720.00 USD | 0.00 USD | `+16.38%` | `9,432,000,000.00` |
| `Live` | `Short` | `821.50` | 5,460,000.00 USD | 11,710.00 USD | 0.00 USD | `+16.81%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 5,470,000.00 USD | 3,540.00 USD | 0.00 USD | `+16.95%` | `4,302,000,000.00` |
| `Live` | `Short` | `826.50` | 6,000,000.00 USD | 536,790.00 USD | 0.00 USD | `+17.52%` | `649,473,000,000.00` |
| `Live` | `Short` | `828.50` | 6,090,000.00 USD | 87,650.00 USD | 0.00 USD | `+17.80%` | `105,797,000,000.00` |
| `Live` | `Short` | `832.50` | 6,100,000.00 USD | 2,910.00 USD | 0.00 USD | `+18.37%` | `3,500,000,000.00` |
| `Live` | `Short` | `834.50` | 6,100,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.66%` | `1,206,000,000.00` |
| `Live` | `Short` | `837.50` | 6,100,000.00 USD | 3,570.00 USD | 0.00 USD | `+19.08%` | `4,257,000,000.00` |
| `Live` | `Short` | `838.50` | 6,120,000.00 USD | 21,840.00 USD | 0.00 USD | `+19.23%` | `26,046,000,000.00` |
| `Live` | `Short` | `840.50` | 6,130,000.00 USD | 11,370.00 USD | 0.00 USD | `+19.51%` | `13,532,000,000.00` |
| `Live` | `Short` | `841.50` | 6,140,000.00 USD | 2,830.00 USD | 0.00 USD | `+19.65%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 6,140,000.00 USD | 1,750.00 USD | 0.00 USD | `+19.79%` | `2,074,000,000.00` |
| `Live` | `Short` | `843.50` | 6,140,000.00 USD | 1,160.00 USD | 0.00 USD | `+19.94%` | `1,371,000,000.00` |
| `Live` | `Short` | `846.50` | 6,170,000.00 USD | 34,180.00 USD | 0.00 USD | `+20.36%` | `40,378,000,000.00` |
| `Live` | `Short` | `848.50` | 6,170,000.00 USD | 289.34 USD | 0.00 USD | `+20.65%` | `341,000,000.00` |
| `Live` | `Short` | `850.50` | 6,170,000.00 USD | 393.78 USD | 0.00 USD | `+20.93%` | `463,000,000.00` |
| `Live` | `Short` | `855.50` | 6,180,000.00 USD | 2,110.00 USD | 0.00 USD | `+21.64%` | `2,462,000,000.00` |
| `Live` | `Short` | `856.50` | 6,210,000.00 USD | 34,780.00 USD | 0.00 USD | `+21.78%` | `40,606,000,000.00` |
| `Live` | `Short` | `858.50` | 6,730,000.00 USD | 523,680.00 USD | 0.00 USD | `+22.07%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 6,750,000.00 USD | 16,380.00 USD | 0.00 USD | `+22.21%` | `19,059,000,000.00` |
| `Live` | `Short` | `863.50` | 7,040,000.00 USD | 289,320.00 USD | 0.00 USD | `+22.78%` | `335,051,000,000.00` |
| `Live` | `Short` | `865.50` | 7,060,000.00 USD | 18,900.00 USD | 0.00 USD | `+23.06%` | `21,832,000,000.00` |
| `Live` | `Short` | `873.50` | 7,060,000.00 USD | 326.69 USD | 0.00 USD | `+24.20%` | `374,000,000.00` |
| `Live` | `Short` | `877.50` | 7,780,000.00 USD | 716,240.00 USD | 0.00 USD | `+24.77%` | `816,230,000,000.00` |
| `Live` | `Short` | `878.50` | 7,960,000.00 USD | 180,240.00 USD | 0.00 USD | `+24.91%` | `205,165,000,000.00` |
| `Live` | `Short` | `880.50` | 7,960,000.00 USD | 663.02 USD | 0.00 USD | `+25.20%` | `753,000,000.00` |
| `Live` | `Short` | `885.50` | 7,960,000.00 USD | 2,580.00 USD | 0.00 USD | `+25.91%` | `2,917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,960,000.00 USD | 385.18 USD | 0.00 USD | `+26.19%` | `434,000,000.00` |
| `Live` | `Short` | `889.50` | 7,980,000.00 USD | 22,480.00 USD | 0.00 USD | `+26.48%` | `25,275,000,000.00` |
| `Live` | `Short` | `891.50` | 7,990,000.00 USD | 3,950.00 USD | 0.00 USD | `+26.76%` | `4,429,000,000.00` |
| `Live` | `Short` | `893.50` | 7,990,000.00 USD | 554.86 USD | 0.00 USD | `+27.05%` | `621,000,000.00` |
| `Live` | `Short` | `894.50` | 8,010,000.00 USD | 26,840.00 USD | 0.00 USD | `+27.19%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 8,240,000.00 USD | 223,880.00 USD | 0.00 USD | `+27.33%` | `250,000,000,000.00` |
| `Live` | `Short` | `896.50` | 8,240,000.00 USD | 249.23 USD | 0.00 USD | `+27.47%` | `278,000,000.00` |
| `Live` | `Short` | `897.50` | 8,360,000.00 USD | 126,180.00 USD | 0.00 USD | `+27.61%` | `140,590,000,000.00` |
| `Live` | `Short` | `898.50` | 8,360,000.00 USD | 127.59 USD | 0.00 USD | `+27.76%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 8,380,000.00 USD | 12,810.00 USD | 0.00 USD | `+27.90%` | `14,244,000,000.00` |
| `Live` | `Short` | `901.50` | 8,550,000.00 USD | 170,160.00 USD | 0.00 USD | `+28.18%` | `188,749,000,000.00` |
| `Live` | `Short` | `902.50` | 8,550,000.00 USD | 305.05 USD | 0.00 USD | `+28.33%` | `338,000,000.00` |
| `Live` | `Short` | `903.50` | 8,550,000.00 USD | 6,030.00 USD | 0.00 USD | `+28.47%` | `6,669,000,000.00` |
| `Live` | `Short` | `904.50` | 8,620,000.00 USD | 63,930.00 USD | 0.00 USD | `+28.61%` | `70,678,000,000.00` |
| `Live` | `Short` | `905.50` | 8,650,000.00 USD | 37,150.00 USD | 0.00 USD | `+28.75%` | `41,028,000,000.00` |
| `Live` | `Short` | `906.50` | 8,650,000.00 USD | 313.65 USD | 0.00 USD | `+28.89%` | `346,000,000.00` |
| `Live` | `Short` | `907.50` | 8,660,000.00 USD | 6,470.00 USD | 0.00 USD | `+29.04%` | `7,130,000,000.00` |
| `Live` | `Short` | `908.50` | 8,660,000.00 USD | 2,420.00 USD | 0.00 USD | `+29.18%` | `2,669,000,000.00` |
| `Live` | `Short` | `911.50` | 8,700,000.00 USD | 34,790.00 USD | 0.00 USD | `+29.60%` | `38,169,000,000.00` |
| `Live` | `Short` | `912.50` | 8,700,000.00 USD | 116.80 USD | 0.00 USD | `+29.75%` | `128,000,000.00` |
| `Live` | `Short` | `913.50` | 8,740,000.00 USD | 44,350.00 USD | 0.00 USD | `+29.89%` | `48,545,000,000.00` |
| `Live` | `Short` | `925.50` | 8,750,000.00 USD | 9,260.00 USD | 0.00 USD | `+31.60%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 8,750,000.00 USD | 651.81 USD | 0.00 USD | `+32.02%` | `702,000,000.00` |
| `Live` | `Short` | `934.50` | 8,750,000.00 USD | 956.93 USD | 0.00 USD | `+32.88%` | `1,024,000,000.00` |
| `Live` | `Short` | `935.50` | 8,820,000.00 USD | 69,290.00 USD | 0.00 USD | `+33.02%` | `74,068,000,000.00` |
| `Live` | `Short` | `936.50` | 8,940,000.00 USD | 121,750.00 USD | 0.00 USD | `+33.16%` | `130,000,000,000.00` |
| `Live` | `Short` | `938.50` | 8,950,000.00 USD | 959.15 USD | 0.00 USD | `+33.44%` | `1,022,000,000.00` |
| `Live` | `Short` | `946.50` | 8,950,000.00 USD | 2,690.00 USD | 0.00 USD | `+34.58%` | `2,846,000,000.00` |
| `Live` | `Short` | `952.50` | 8,950,000.00 USD | 6,860.00 USD | 0.00 USD | `+35.43%` | `7,199,000,000.00` |
| `Live` | `Short` | `954.50` | 8,970,000.00 USD | 18,890.00 USD | 0.00 USD | `+35.72%` | `19,788,000,000.00` |
| `Live` | `Short` | `956.50` | 8,970,000.00 USD | 203.73 USD | 0.00 USD | `+36.00%` | `213,000,000.00` |
| `Live` | `Short` | `957.50` | 8,970,000.00 USD | 340.87 USD | 0.00 USD | `+36.15%` | `356,000,000.00` |
| `Live` | `Short` | `959.50` | 8,970,000.00 USD | 114.18 USD | 0.00 USD | `+36.43%` | `119,000,000.00` |
| `Live` | `Short` | `960.50` | 8,980,000.00 USD | 3,210.00 USD | 0.00 USD | `+36.57%` | `3,344,000,000.00` |
| `Live` | `Short` | `969.50` | 8,980,000.00 USD | 5,780.00 USD | 0.00 USD | `+37.85%` | `5,960,000,000.00` |
| `Live` | `Short` | `971.50` | 8,990,000.00 USD | 1,940.00 USD | 0.00 USD | `+38.14%` | `2,000,000,000.00` |
| `Live` | `Short` | `974.50` | 8,990,000.00 USD | 180.28 USD | 0.00 USD | `+38.56%` | `185,000,000.00` |
| `Live` | `Short` | `978.50` | 9,050,000.00 USD | 60,090.00 USD | 0.00 USD | `+39.13%` | `61,406,000,000.00` |
| `Live` | `Short` | `981.50` | 9,060,000.00 USD | 14,480.00 USD | 0.00 USD | `+39.56%` | `14,758,000,000.00` |
| `Live` | `Short` | `985.50` | 9,060,000.00 USD | 1,100.00 USD | 0.00 USD | `+40.13%` | `1,112,000,000.00` |
| `Live` | `Short` | `988.50` | 9,080,000.00 USD | 14,370.00 USD | 0.00 USD | `+40.55%` | `14,541,000,000.00` |
| `Live` | `Short` | `990.50` | 9,100,000.00 USD | 28,300.00 USD | 0.00 USD | `+40.84%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 9,110,000.00 USD | 2,140.00 USD | 0.00 USD | `+41.12%` | `2,154,000,000.00` |
| `Live` | `Short` | `993.50` | 9,110,000.00 USD | 975.62 USD | 0.00 USD | `+41.26%` | `982,000,000.00` |
| `Live` | `Short` | `994.50` | 9,390,000.00 USD | 285,520.00 USD | 0.00 USD | `+41.41%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 9,390,000.00 USD | 313.58 USD | 0.00 USD | `+41.55%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 9,420,000.00 USD | 22,340.00 USD | 0.00 USD | `+41.69%` | `22,422,000,000.00` |
| `Live` | `Short` | `997.50` | 9,420,000.00 USD | 7,300.00 USD | 0.00 USD | `+41.83%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 9,860,000.00 USD | 437,340.00 USD | 0.00 USD | `+41.98%` | `438,000,000,000.00` |
| `Live` | `Short` | `999.50` | 9,860,000.00 USD | 620.69 USD | 0.00 USD | `+42.12%` | `621,000,000.00` |
| `Live` | `Short` | `1001.50` | 9,870,000.00 USD | 13,290.00 USD | 0.00 USD | `+42.40%` | `13,273,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,870,000.00 USD | 1,070.00 USD | 0.00 USD | `+42.69%` | `1,069,000,000.00` |
| `Live` | `Short` | `1005.50` | 9,880,000.00 USD | 4,050.00 USD | 0.00 USD | `+42.97%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 9,910,000.00 USD | 29,110.00 USD | 0.00 USD | `+43.40%` | `28,860,000,000.00` |
| `Live` | `Short` | `1009.50` | 9,960,000.00 USD | 51,370.00 USD | 0.00 USD | `+43.54%` | `50,889,000,000.00` |
| `Live` | `Short` | `1014.50` | 10,720,000.00 USD | 760,880.00 USD | 0.00 USD | `+44.25%` | `750,000,000,000.00` |
| `Live` | `Short` | `1024.50` | 10,720,000.00 USD | 2,850.00 USD | 0.00 USD | `+45.67%` | `2,777,000,000.00` |
| `Live` | `Short` | `1032.50` | 11,440,000.00 USD | 720,280.00 USD | 0.00 USD | `+46.81%` | `697,611,000,000.00` |
| `Live` | `Short` | `1033.50` | 11,440,000.00 USD | 498.15 USD | 0.00 USD | `+46.95%` | `482,000,000.00` |
| `Live` | `Short` | `1044.50` | 11,520,000.00 USD | 80,330.00 USD | 0.00 USD | `+48.52%` | `76,903,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,520,000.00 USD | 500.04 USD | 0.00 USD | `+49.37%` | `476,000,000.00` |
| `Live` | `Short` | `1059.50` | 11,530,000.00 USD | 7,010.00 USD | 0.00 USD | `+50.65%` | `6,620,000,000.00` |
| `Live` | `Short` | `1062.50` | 11,530,000.00 USD | 635.38 USD | 0.00 USD | `+51.08%` | `598,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,530,000.00 USD | 1,760.00 USD | 0.00 USD | `+51.36%` | `1,657,000,000.00` |
| `Live` | `Short` | `1068.50` | 11,530,000.00 USD | 131.43 USD | 0.00 USD | `+51.93%` | `123,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,540,000.00 USD | 1,610.00 USD | 0.00 USD | `+52.64%` | `1,500,000,000.00` |
| `Live` | `Short` | `1075.50` | 11,540,000.00 USD | 120.46 USD | 0.00 USD | `+52.92%` | `112,000,000.00` |
| `Live` | `Short` | `1079.50` | 11,600,000.00 USD | 69,000.00 USD | 0.00 USD | `+53.49%` | `63,916,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,610,000.00 USD | 5,770.00 USD | 0.00 USD | `+54.63%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,630,000.00 USD | 16,230.00 USD | 0.00 USD | `+54.77%` | `14,913,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,750,000.00 USD | 121,730.00 USD | 0.00 USD | `+55.48%` | `111,318,000,000.00` |
| `Live` | `Short` | `1096.50` | 11,750,000.00 USD | 810.31 USD | 0.00 USD | `+55.91%` | `739,000,000.00` |
| `Live` | `Short` | `1107.50` | 11,820,000.00 USD | 75,590.00 USD | 0.00 USD | `+57.47%` | `68,249,000,000.00` |
| `Live` | `Short` | `1111.50` | 11,830,000.00 USD | 1,570.00 USD | 0.00 USD | `+58.04%` | `1,413,000,000.00` |
| `Live` | `Short` | `1114.50` | 11,890,000.00 USD | 60,260.00 USD | 0.00 USD | `+58.47%` | `54,065,000,000.00` |
| `Live` | `Short` | `1115.50` | 12,000,000.00 USD | 116,010.00 USD | 0.00 USD | `+58.61%` | `104,000,000,000.00` |
| `Live` | `Short` | `1119.50` | 12,000,000.00 USD | 1,970.00 USD | 0.00 USD | `+59.18%` | `1,759,000,000.00` |
| `Live` | `Short` | `1120.50` | 12,020,000.00 USD | 19,970.00 USD | 0.00 USD | `+59.32%` | `17,826,000,000.00` |
| `Live` | `Short` | `1131.50` | 12,020,000.00 USD | 151.62 USD | 0.00 USD | `+60.89%` | `134,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,370,000.00 USD | 341,250.00 USD | 0.00 USD | `+61.74%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 12,370,000.00 USD | 243.64 USD | 0.00 USD | `+61.88%` | `214,000,000.00` |
| `Live` | `Short` | `1141.50` | 12,370,000.00 USD | 1,530.00 USD | 0.00 USD | `+62.31%` | `1,337,000,000.00` |
| `Live` | `Short` | `1157.50` | 12,380,000.00 USD | 11,750.00 USD | 0.00 USD | `+64.58%` | `10,154,000,000.00` |
| `Live` | `Short` | `1162.50` | 12,380,000.00 USD | 155.78 USD | 0.00 USD | `+65.29%` | `134,000,000.00` |
| `Live` | `Short` | `1165.50` | 12,380,000.00 USD | 121.21 USD | 0.00 USD | `+65.72%` | `104,000,000.00` |
| `Live` | `Short` | `1177.50` | 12,380,000.00 USD | 5,040.00 USD | 0.00 USD | `+67.43%` | `4,284,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,390,000.00 USD | 463.43 USD | 0.00 USD | `+70.27%` | `387,000,000.00` |
| `Live` | `Short` | `1199.50` | 12,390,000.00 USD | 169.13 USD | 0.00 USD | `+70.56%` | `141,000,000.00` |
| `Live` | `Short` | `1200.50` | 12,440,000.00 USD | 58,000.00 USD | 0.00 USD | `+70.70%` | `48,311,000,000.00` |
| `Live` | `Short` | `1202.50` | 12,560,000.00 USD | 118,760.00 USD | 0.00 USD | `+70.98%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,560,000.00 USD | 385.19 USD | 0.00 USD | `+71.69%` | `319,000,000.00` |
| `Live` | `Short` | `1215.50` | 12,610,000.00 USD | 42,540.00 USD | 0.00 USD | `+72.83%` | `35,000,000,000.00` |
| `Live` | `Short` | `1217.50` | 12,640,000.00 USD | 30,420.00 USD | 0.00 USD | `+73.11%` | `24,982,000,000.00` |
| `Live` | `Short` | `1222.50` | 12,660,000.00 USD | 21,230.00 USD | 0.00 USD | `+73.83%` | `17,363,000,000.00` |
| `Live` | `Short` | `1224.50` | 12,660,000.00 USD | 1,030.00 USD | 0.00 USD | `+74.11%` | `841,000,000.00` |
| `Live` | `Short` | `1228.50` | 12,660,000.00 USD | 3,730.00 USD | 0.00 USD | `+74.68%` | `3,035,000,000.00` |
| `Live` | `Short` | `1246.50` | 12,660,000.00 USD | 2,660.00 USD | 0.00 USD | `+77.24%` | `2,134,000,000.00` |
| `Live` | `Short` | `1249.50` | 12,670,000.00 USD | 2,050.00 USD | 0.00 USD | `+77.66%` | `1,644,000,000.00` |
| `Live` | `Short` | `1251.50` | 12,670,000.00 USD | 100.12 USD | 0.00 USD | `+77.95%` | `80,000,000.00` |
| `Live` | `Short` | `1253.50` | 12,670,000.00 USD | 200.56 USD | 0.00 USD | `+78.23%` | `160,000,000.00` |
| `Live` | `Short` | `1256.50` | 12,670,000.00 USD | 5,020.00 USD | 0.00 USD | `+78.66%` | `3,994,000,000.00` |
| `Live` | `Short` | `1261.50` | 12,790,000.00 USD | 113,530.00 USD | 0.00 USD | `+79.37%` | `90,000,000,000.00` |
| `Live` | `Short` | `1263.50` | 12,790,000.00 USD | 6,850.00 USD | 0.00 USD | `+79.66%` | `5,419,000,000.00` |
| `Live` | `Short` | `1265.50` | 12,790,000.00 USD | 1,270.00 USD | 0.00 USD | `+79.94%` | `1,000,000,000.00` |
| `Live` | `Short` | `1266.50` | 12,820,000.00 USD | 24,590.00 USD | 0.00 USD | `+80.08%` | `19,414,000,000.00` |
| `Live` | `Short` | `1280.50` | 12,840,000.00 USD | 19,130.00 USD | 0.00 USD | `+82.07%` | `14,939,000,000.00` |
| `Live` | `Short` | `1281.50` | 12,950,000.00 USD | 109,320.00 USD | 0.00 USD | `+82.21%` | `85,305,000,000.00` |
| `Live` | `Short` | `1284.50` | 13,010,000.00 USD | 61,810.00 USD | 0.00 USD | `+82.64%` | `48,123,000,000.00` |
| `Live` | `Short` | `1287.50` | 13,010,000.00 USD | 348.91 USD | 0.00 USD | `+83.07%` | `271,000,000.00` |
| `Live` | `Short` | `1295.50` | 13,010,000.00 USD | 181.37 USD | 0.00 USD | `+84.21%` | `140,000,000.00` |
| `Live` | `Short` | `1296.50` | 13,030,000.00 USD | 25,930.00 USD | 0.00 USD | `+84.35%` | `20,000,000,000.00` |
| `Live` | `Short` | `1300.50` | 13,040,000.00 USD | 1,830.00 USD | 0.00 USD | `+84.92%` | `1,409,000,000.00` |
| `Live` | `Short` | `1302.50` | 14,880,000.00 USD | 1,840,000.00 USD | 0.00 USD | `+85.20%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1303.50` | 14,900,000.00 USD | 18,340.00 USD | 0.00 USD | `+85.34%` | `14,070,000,000.00` |
| `Live` | `Short` | `1306.50` | 14,900,000.00 USD | 4,040.00 USD | 0.00 USD | `+85.77%` | `3,092,000,000.00` |
| `Live` | `Short` | `1307.50` | 14,900,000.00 USD | 226.20 USD | 0.00 USD | `+85.91%` | `173,000,000.00` |
| `Live` | `Short` | `1309.50` | 14,990,000.00 USD | 91,670.00 USD | 0.00 USD | `+86.20%` | `70,000,000,000.00` |
| `Live` | `Short` | `1311.50` | 15,160,000.00 USD | 166,610.00 USD | 0.00 USD | `+86.48%` | `127,039,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,170,000.00 USD | 14,130.00 USD | 0.00 USD | `+87.62%` | `10,710,000,000.00` |
| `Live` | `Short` | `1323.50` | 15,170,000.00 USD | 2,650.00 USD | 0.00 USD | `+88.19%` | `2,000,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,170,000.00 USD | 138.06 USD | 0.00 USD | `+88.76%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,170,000.00 USD | 289.61 USD | 0.00 USD | `+88.90%` | `218,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,230,000.00 USD | 54,070.00 USD | 0.00 USD | `+89.18%` | `40,640,000,000.00` |
| `Live` | `Short` | `1342.50` | 15,290,000.00 USD | 58,390.00 USD | 0.00 USD | `+90.89%` | `43,490,000,000.00` |
| `Live` | `Short` | `1347.50` | 15,290,000.00 USD | 6,740.00 USD | 0.00 USD | `+91.60%` | `5,000,000,000.00` |
| `Live` | `Short` | `1359.50` | 15,290,000.00 USD | 121.00 USD | 0.00 USD | `+93.31%` | `89,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,290,000.00 USD | 761.70 USD | 0.00 USD | `+94.44%` | `557,000,000.00` |
| `Live` | `Short` | `1368.50` | 15,300,000.00 USD | 4,110.00 USD | 0.00 USD | `+94.59%` | `3,000,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,350,000.00 USD | 46,880.00 USD | 0.00 USD | `+94.73%` | `34,232,000,000.00` |
| `Live` | `Short` | `1399.50` | 15,350,000.00 USD | 4,840.00 USD | 0.00 USD | `+98.99%` | `3,457,000,000.00` |
| `Live` | `Short` | `1405.50` | 15,360,000.00 USD | 4,770.00 USD | 0.00 USD | `+99.85%` | `3,392,000,000.00` |
| `Live` | `Short` | `1406.50` | 15,610,000.00 USD | 253,170.00 USD | 0.00 USD | `+99.99%` | `180,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 2,960,000.00 USD | 0.00 USD | 475.73 USD | `-78.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 2,960,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 2,960,000.00 USD | 0.00 USD | 333.50 USD | `-52.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 2,950,000.00 USD | 0.00 USD | 8,140.00 USD | `-48.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 2,950,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 2,940,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 2,920,000.00 USD | 0.00 USD | 25,210.00 USD | `-41.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 2,900,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 2,890,000.00 USD | 0.00 USD | 8,180.00 USD | `-39.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 2,890,000.00 USD | 0.00 USD | 173.83 USD | `-38.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 2,890,000.00 USD | 0.00 USD | 2,210.00 USD | `-36.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 2,880,000.00 USD | 0.00 USD | 698.74 USD | `-35.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 2,880,000.00 USD | 0.00 USD | 2,270.00 USD | `-35.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `457.50` | 2,880,000.00 USD | 0.00 USD | 2,270.00 USD | `-34.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 2,880,000.00 USD | 0.00 USD | 1,750.00 USD | `-34.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 2,880,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `485.50` | 2,870,000.00 USD | 0.00 USD | 100.50 USD | `-30.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 2,870,000.00 USD | 0.00 USD | 100.71 USD | `-30.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 2,870,000.00 USD | 0.00 USD | 6,600.00 USD | `-30.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 2,870,000.00 USD | 0.00 USD | 125.06 USD | `-30.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `490.50` | 2,870,000.00 USD | 0.00 USD | 101.53 USD | `-30.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 2,870,000.00 USD | 0.00 USD | 2,450.00 USD | `-29.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `495.50` | 2,860,000.00 USD | 0.00 USD | 102.57 USD | `-29.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 2,860,000.00 USD | 0.00 USD | 163.01 USD | `-29.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 2,860,000.00 USD | 0.00 USD | 214.78 USD | `-28.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 2,860,000.00 USD | 0.00 USD | 12,610.00 USD | `-28.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 2,850,000.00 USD | 0.00 USD | 42,390.00 USD | `-28.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 2,810,000.00 USD | 0.00 USD | 138.78 USD | `-27.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 2,810,000.00 USD | 0.00 USD | 185.97 USD | `-27.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 2,810,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 2,810,000.00 USD | 0.00 USD | 125.51 USD | `-26.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 2,810,000.00 USD | 0.00 USD | 280.49 USD | `-26.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 2,810,000.00 USD | 0.00 USD | 258.14 USD | `-25.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 2,810,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 2,800,000.00 USD | 0.00 USD | 485.16 USD | `-24.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 2,800,000.00 USD | 0.00 USD | 4,650.00 USD | `-24.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 2,790,000.00 USD | 0.00 USD | 1,680.00 USD | `-23.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 2,790,000.00 USD | 0.00 USD | 864.80 USD | `-23.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `547.50` | 2,790,000.00 USD | 0.00 USD | 248.56 USD | `-22.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 2,790,000.00 USD | 0.00 USD | 4,130.00 USD | `-21.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 2,790,000.00 USD | 0.00 USD | 366,230.00 USD | `-21.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,420,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,420,000.00 USD | 0.00 USD | 611.05 USD | `-21.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,420,000.00 USD | 0.00 USD | 213.52 USD | `-20.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,420,000.00 USD | 0.00 USD | 51,260.00 USD | `-20.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,370,000.00 USD | 0.00 USD | 292.02 USD | `-20.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 2,370,000.00 USD | 0.00 USD | 748.48 USD | `-20.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 2,370,000.00 USD | 0.00 USD | 199.12 USD | `-20.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 2,370,000.00 USD | 0.00 USD | 808.06 USD | `-19.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,360,000.00 USD | 0.00 USD | 566.50 USD | `-19.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,360,000.00 USD | 0.00 USD | 330.85 USD | `-19.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,360,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 2,360,000.00 USD | 0.00 USD | 569.50 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,360,000.00 USD | 0.00 USD | 774.17 USD | `-18.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,360,000.00 USD | 0.00 USD | 1,700.00 USD | `-18.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,360,000.00 USD | 0.00 USD | 291.91 USD | `-18.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,350,000.00 USD | 0.00 USD | 469.61 USD | `-18.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,350,000.00 USD | 0.00 USD | 289.98 USD | `-18.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,350,000.00 USD | 0.00 USD | 285.86 USD | `-17.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,350,000.00 USD | 0.00 USD | 289.17 USD | `-17.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,350,000.00 USD | 0.00 USD | 6,750.00 USD | `-17.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,350,000.00 USD | 0.00 USD | 1,240.00 USD | `-17.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 2,350,000.00 USD | 0.00 USD | 6,980.00 USD | `-17.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,340,000.00 USD | 0.00 USD | 287.67 USD | `-17.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,340,000.00 USD | 0.00 USD | 763.94 USD | `-16.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,340,000.00 USD | 0.00 USD | 542.76 USD | `-16.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,340,000.00 USD | 0.00 USD | 34,020.00 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,300,000.00 USD | 0.00 USD | 830,190.00 USD | `-16.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,470,000.00 USD | 0.00 USD | 252.31 USD | `-16.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,470,000.00 USD | 0.00 USD | 540.31 USD | `-16.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,470,000.00 USD | 0.00 USD | 698.56 USD | `-15.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 1,470,000.00 USD | 0.00 USD | 1,160.00 USD | `-15.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 1,470,000.00 USD | 0.00 USD | 119.30 USD | `-15.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 1,470,000.00 USD | 0.00 USD | 222.87 USD | `-15.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,470,000.00 USD | 0.00 USD | 244.79 USD | `-14.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `599.50` | 1,470,000.00 USD | 0.00 USD | 145.68 USD | `-14.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,470,000.00 USD | 0.00 USD | 57,230.00 USD | `-14.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 1,410,000.00 USD | 0.00 USD | 1,590.00 USD | `-14.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,410,000.00 USD | 0.00 USD | 46,760.00 USD | `-14.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 1,360,000.00 USD | 0.00 USD | 937.84 USD | `-14.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,360,000.00 USD | 0.00 USD | 1,870.00 USD | `-14.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,360,000.00 USD | 0.00 USD | 8,040.00 USD | `-13.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 1,350,000.00 USD | 0.00 USD | 18,380.00 USD | `-13.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 1,330,000.00 USD | 0.00 USD | 30,480.00 USD | `-13.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 1,300,000.00 USD | 0.00 USD | 12,220.00 USD | `-13.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,290,000.00 USD | 0.00 USD | 4,470.00 USD | `-13.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,290,000.00 USD | 0.00 USD | 269.15 USD | `-12.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,290,000.00 USD | 0.00 USD | 1,740.00 USD | `-12.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,290,000.00 USD | 0.00 USD | 120.83 USD | `-12.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,290,000.00 USD | 0.00 USD | 13,170.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 1,270,000.00 USD | 0.00 USD | 2,150.00 USD | `-11.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 1,270,000.00 USD | 0.00 USD | 219.47 USD | `-11.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 1,270,000.00 USD | 0.00 USD | 445.27 USD | `-11.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,270,000.00 USD | 0.00 USD | 445.98 USD | `-11.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 1,270,000.00 USD | 0.00 USD | 694.79 USD | `-10.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 1,270,000.00 USD | 0.00 USD | 916.15 USD | `-10.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 1,270,000.00 USD | 0.00 USD | 746.03 USD | `-10.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 1,270,000.00 USD | 0.00 USD | 2,740.00 USD | `-10.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,260,000.00 USD | 0.00 USD | 861.26 USD | `-10.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 1,260,000.00 USD | 0.00 USD | 179.98 USD | `-10.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 1,260,000.00 USD | 0.00 USD | 4,900.00 USD | `-10.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,260,000.00 USD | 0.00 USD | 164.08 USD | `-9.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,260,000.00 USD | 0.00 USD | 2,550.00 USD | `-9.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 1,260,000.00 USD | 0.00 USD | 7,140.00 USD | `-9.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 1,250,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,250,000.00 USD | 0.00 USD | 3,640.00 USD | `-9.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 1,240,000.00 USD | 0.00 USD | 384.98 USD | `-9.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 1,240,000.00 USD | 0.00 USD | 429.78 USD | `-8.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 1,240,000.00 USD | 0.00 USD | 352.18 USD | `-8.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 1,240,000.00 USD | 0.00 USD | 357.87 USD | `-8.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 1,240,000.00 USD | 0.00 USD | 1,980.00 USD | `-8.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 1,240,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,230,000.00 USD | 0.00 USD | 10,640.00 USD | `-8.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,220,000.00 USD | 0.00 USD | 971.04 USD | `-8.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 1,220,000.00 USD | 0.00 USD | 1,800.00 USD | `-7.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,220,000.00 USD | 0.00 USD | 107.17 USD | `-7.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,220,000.00 USD | 0.00 USD | 28,620.00 USD | `-7.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,190,000.00 USD | 0.00 USD | 5,890.00 USD | `-7.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,190,000.00 USD | 0.00 USD | 2,020.00 USD | `-7.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,180,000.00 USD | 0.00 USD | 308.92 USD | `-6.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 1,180,000.00 USD | 0.00 USD | 165.84 USD | `-6.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,180,000.00 USD | 0.00 USD | 456.27 USD | `-6.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,180,000.00 USD | 0.00 USD | 110.46 USD | `-6.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 1,180,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,180,000.00 USD | 0.00 USD | 13,060.00 USD | `-6.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,170,000.00 USD | 0.00 USD | 567.37 USD | `-6.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 1,170,000.00 USD | 0.00 USD | 11,440.00 USD | `-5.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,160,000.00 USD | 0.00 USD | 7,780.00 USD | `-5.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 1,150,000.00 USD | 0.00 USD | 4,040.00 USD | `-5.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 1,140,000.00 USD | 0.00 USD | 713.01 USD | `-5.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 1,140,000.00 USD | 0.00 USD | 576.32 USD | `-5.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,140,000.00 USD | 0.00 USD | 24,530.00 USD | `-5.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 1,120,000.00 USD | 0.00 USD | 10,740.00 USD | `-5.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 1,110,000.00 USD | 0.00 USD | 719.97 USD | `-4.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,110,000.00 USD | 0.00 USD | 2,390.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,110,000.00 USD | 0.00 USD | 135,800.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 969,490.00 USD | 0.00 USD | 6,960.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 962,530.00 USD | 0.00 USD | 71,230.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 891,300.00 USD | 0.00 USD | 3,460.00 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 887,840.00 USD | 0.00 USD | 1,470.00 USD | `-4.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 886,370.00 USD | 0.00 USD | 8,350.00 USD | `-3.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 878,020.00 USD | 0.00 USD | 56,170.00 USD | `-3.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 821,850.00 USD | 0.00 USD | 39,650.00 USD | `-3.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 782,200.00 USD | 0.00 USD | 825.73 USD | `-3.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 781,370.00 USD | 0.00 USD | 254.13 USD | `-3.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 781,120.00 USD | 0.00 USD | 3,200.00 USD | `-3.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 777,920.00 USD | 0.00 USD | 146.52 USD | `-3.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 777,770.00 USD | 0.00 USD | 7,230.00 USD | `-2.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 770,540.00 USD | 0.00 USD | 171,850.00 USD | `-2.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 598,690.00 USD | 0.00 USD | 171,120.00 USD | `-2.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 427,560.00 USD | 0.00 USD | 11,030.00 USD | `-2.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 416,540.00 USD | 0.00 USD | 292.45 USD | `-2.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 416,240.00 USD | 0.00 USD | 323.12 USD | `-2.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 415,920.00 USD | 0.00 USD | 382.81 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 415,540.00 USD | 0.00 USD | 532.98 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 415,010.00 USD | 0.00 USD | 76,650.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 338,360.00 USD | 0.00 USD | 174,840.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 163,510.00 USD | 0.00 USD | 4,450.00 USD | `-1.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 159,060.00 USD | 0.00 USD | 990.32 USD | `-1.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 158,070.00 USD | 0.00 USD | 1,540.00 USD | `-1.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 156,540.00 USD | 0.00 USD | 166.92 USD | `-1.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 156,370.00 USD | 0.00 USD | 9,290.00 USD | `-0.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 147,080.00 USD | 0.00 USD | 47,550.00 USD | `-0.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 99,530.00 USD | 0.00 USD | 291.97 USD | `-0.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 99,240.00 USD | 0.00 USD | 38,470.00 USD | `-0.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 60,770.00 USD | 0.00 USD | 59,710.00 USD | `-0.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 1,060.00 USD | 0.00 USD | 681.16 USD | `-0.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 380.05 USD | 0.00 USD | 380.05 USD | `-0.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `703.50` | 3,850.00 USD | 3,850.00 USD | 0.00 USD | `+0.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `704.50` | 90,500.00 USD | 86,660.00 USD | 0.00 USD | `+0.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `705.50` | 91,150.00 USD | 640.59 USD | 0.00 USD | `+0.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `706.50` | 94,130.00 USD | 2,990.00 USD | 0.00 USD | `+0.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 107,400.00 USD | 13,270.00 USD | 0.00 USD | `+0.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 112,090.00 USD | 4,690.00 USD | 0.00 USD | `+0.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 113,620.00 USD | 1,520.00 USD | 0.00 USD | `+0.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 124,850.00 USD | 11,230.00 USD | 0.00 USD | `+1.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 158,680.00 USD | 33,840.00 USD | 0.00 USD | `+1.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 166,460.00 USD | 7,770.00 USD | 0.00 USD | `+1.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 184,450.00 USD | 18,000.00 USD | 0.00 USD | `+1.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 186,120.00 USD | 1,660.00 USD | 0.00 USD | `+1.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 189,210.00 USD | 3,100.00 USD | 0.00 USD | `+1.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 190,390.00 USD | 1,170.00 USD | 0.00 USD | `+1.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 192,980.00 USD | 2,590.00 USD | 0.00 USD | `+2.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 251,600.00 USD | 58,630.00 USD | 0.00 USD | `+2.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 321,840.00 USD | 70,240.00 USD | 0.00 USD | `+2.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 324,240.00 USD | 2,400.00 USD | 0.00 USD | `+2.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 377,810.00 USD | 53,570.00 USD | 0.00 USD | `+2.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 387,290.00 USD | 9,480.00 USD | 0.00 USD | `+2.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 395,540.00 USD | 8,250.00 USD | 0.00 USD | `+2.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 420,970.00 USD | 25,430.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 515,550.00 USD | 94,580.00 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 516,050.00 USD | 501.28 USD | 0.00 USD | `+3.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 535,020.00 USD | 18,970.00 USD | 0.00 USD | `+3.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 588,190.00 USD | 53,170.00 USD | 0.00 USD | `+3.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 729,000.00 USD | 140,810.00 USD | 0.00 USD | `+3.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 733,430.00 USD | 4,430.00 USD | 0.00 USD | `+3.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 932,420.00 USD | 198,990.00 USD | 0.00 USD | `+4.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 933,830.00 USD | 1,410.00 USD | 0.00 USD | `+4.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,420,000.00 USD | 487,680.00 USD | 0.00 USD | `+4.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,430,000.00 USD | 7,480.00 USD | 0.00 USD | `+4.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,450,000.00 USD | 23,100.00 USD | 0.00 USD | `+4.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,460,000.00 USD | 5,460.00 USD | 0.00 USD | `+4.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,460,000.00 USD | 3,970.00 USD | 0.00 USD | `+4.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,470,000.00 USD | 13,270.00 USD | 0.00 USD | `+5.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,480,000.00 USD | 3,420.00 USD | 0.00 USD | `+5.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,480,000.00 USD | 5,360.00 USD | 0.00 USD | `+5.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,490,000.00 USD | 3,960.00 USD | 0.00 USD | `+5.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,510,000.00 USD | 17,990.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,510,000.00 USD | 8,280.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,720,000.00 USD | 203,810.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,720,000.00 USD | 4,750.00 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,800,000.00 USD | 76,650.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,800,000.00 USD | 824.49 USD | 0.00 USD | `+6.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,800,000.00 USD | 279.19 USD | 0.00 USD | `+6.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,800,000.00 USD | 704.53 USD | 0.00 USD | `+6.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,800,000.00 USD | 123.83 USD | 0.00 USD | `+6.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,810,000.00 USD | 8,720.00 USD | 0.00 USD | `+6.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,810,000.00 USD | 2,730.00 USD | 0.00 USD | `+7.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,810,000.00 USD | 629.17 USD | 0.00 USD | `+7.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,860,000.00 USD | 47,160.00 USD | 0.00 USD | `+7.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,860,000.00 USD | 4,420.00 USD | 0.00 USD | `+7.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,870,000.00 USD | 10,340.00 USD | 0.00 USD | `+7.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 2,020,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 2,020,000.00 USD | 2,790.00 USD | 0.00 USD | `+7.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 2,020,000.00 USD | 325.07 USD | 0.00 USD | `+7.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,310,000.00 USD | 287,930.00 USD | 0.00 USD | `+8.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,320,000.00 USD | 11,460.00 USD | 0.00 USD | `+8.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,320,000.00 USD | 274.50 USD | 0.00 USD | `+8.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,360,000.00 USD | 44,150.00 USD | 0.00 USD | `+8.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,370,000.00 USD | 240.05 USD | 0.00 USD | `+8.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,430,000.00 USD | 60,710.00 USD | 0.00 USD | `+8.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,430,000.00 USD | 331.13 USD | 0.00 USD | `+8.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,890,000.00 USD | 468,310.00 USD | 0.00 USD | `+9.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,890,000.00 USD | 180.60 USD | 0.00 USD | `+9.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,890,000.00 USD | 171.60 USD | 0.00 USD | `+9.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,900,000.00 USD | 1,540.00 USD | 0.00 USD | `+9.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,900,000.00 USD | 242.25 USD | 0.00 USD | `+9.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,910,000.00 USD | 12,400.00 USD | 0.00 USD | `+9.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,910,000.00 USD | 656.70 USD | 0.00 USD | `+9.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,920,000.00 USD | 9,680.00 USD | 0.00 USD | `+10.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,920,000.00 USD | 4,570.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,940,000.00 USD | 14,230.00 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,950,000.00 USD | 15,690.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,960,000.00 USD | 9,990.00 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,960,000.00 USD | 132.52 USD | 0.00 USD | `+10.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,990,000.00 USD | 24,280.00 USD | 0.00 USD | `+10.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,990,000.00 USD | 2,050.00 USD | 0.00 USD | `+11.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,990,000.00 USD | 1,900.00 USD | 0.00 USD | `+11.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,990,000.00 USD | 101.07 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,990,000.00 USD | 102.77 USD | 0.00 USD | `+11.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,990,000.00 USD | 559.28 USD | 0.00 USD | `+11.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 3,000,000.00 USD | 5,610.00 USD | 0.00 USD | `+11.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 3,000,000.00 USD | 2,260.00 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 3,000,000.00 USD | 133.26 USD | 0.00 USD | `+12.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 3,010,000.00 USD | 4,190.00 USD | 0.00 USD | `+12.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 3,010,000.00 USD | 704.44 USD | 0.00 USD | `+12.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 3,010,000.00 USD | 4,360.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 3,010,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 3,020,000.00 USD | 3,630.00 USD | 0.00 USD | `+12.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 3,020,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 3,020,000.00 USD | 154.52 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `798.50` | 3,030,000.00 USD | 7,140.00 USD | 0.00 USD | `+13.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 3,030,000.00 USD | 1,260.00 USD | 0.00 USD | `+13.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 3,050,000.00 USD | 25,190.00 USD | 0.00 USD | `+13.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 3,050,000.00 USD | 120.22 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 3,050,000.00 USD | 803.50 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 3,050,000.00 USD | 120.02 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 3,050,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 3,060,000.00 USD | 5,010.00 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 3,060,000.00 USD | 242.04 USD | 0.00 USD | `+15.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 3,060,000.00 USD | 2,870.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 3,060,000.00 USD | 374.10 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 3,060,000.00 USD | 844.19 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 3,060,000.00 USD | 109.82 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 3,070,000.00 USD | 3,390.00 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 3,070,000.00 USD | 984.70 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 3,070,000.00 USD | 162.68 USD | 0.00 USD | `+16.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 3,070,000.00 USD | 5,990.00 USD | 0.00 USD | `+16.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 3,080,000.00 USD | 7,820.00 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 3,080,000.00 USD | 408.13 USD | 0.00 USD | `+17.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 3,080,000.00 USD | 672.77 USD | 0.00 USD | `+17.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 3,080,000.00 USD | 276.38 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 3,090,000.00 USD | 1,800.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 3,120,000.00 USD | 35,850.00 USD | 0.00 USD | `+18.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 3,120,000.00 USD | 1,170.00 USD | 0.00 USD | `+18.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 3,120,000.00 USD | 187.15 USD | 0.00 USD | `+18.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 3,120,000.00 USD | 372.24 USD | 0.00 USD | `+18.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 3,120,000.00 USD | 326.62 USD | 0.00 USD | `+19.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 3,120,000.00 USD | 296.34 USD | 0.00 USD | `+19.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 3,130,000.00 USD | 5,040.00 USD | 0.00 USD | `+19.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 3,130,000.00 USD | 329.87 USD | 0.00 USD | `+19.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 3,130,000.00 USD | 425.97 USD | 0.00 USD | `+19.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 3,130,000.00 USD | 1,770.00 USD | 0.00 USD | `+20.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 3,130,000.00 USD | 2,550.00 USD | 0.00 USD | `+20.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 3,150,000.00 USD | 11,650.00 USD | 0.00 USD | `+21.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 3,150,000.00 USD | 102.30 USD | 0.00 USD | `+21.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 3,150,000.00 USD | 137.57 USD | 0.00 USD | `+21.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 3,150,000.00 USD | 1,200.00 USD | 0.00 USD | `+21.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 3,150,000.00 USD | 1,160.00 USD | 0.00 USD | `+22.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 3,150,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 3,150,000.00 USD | 874.73 USD | 0.00 USD | `+22.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 3,150,000.00 USD | 2,970.00 USD | 0.00 USD | `+22.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 3,160,000.00 USD | 3,460.00 USD | 0.00 USD | `+23.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 3,160,000.00 USD | 2,610.00 USD | 0.00 USD | `+23.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 3,160,000.00 USD | 228.07 USD | 0.00 USD | `+23.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 3,160,000.00 USD | 1,110.00 USD | 0.00 USD | `+24.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,220,000.00 USD | 54,820.00 USD | 0.00 USD | `+25.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,220,000.00 USD | 266.55 USD | 0.00 USD | `+26.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,220,000.00 USD | 690.14 USD | 0.00 USD | `+26.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,220,000.00 USD | 605.33 USD | 0.00 USD | `+26.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `895.50` | 3,220,000.00 USD | 130.74 USD | 0.00 USD | `+27.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `898.50` | 3,220,000.00 USD | 101.53 USD | 0.00 USD | `+27.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,340,000.00 USD | 126,250.00 USD | 0.00 USD | `+28.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,340,000.00 USD | 167.33 USD | 0.00 USD | `+28.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,350,000.00 USD | 1,640.00 USD | 0.00 USD | `+29.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,350,000.00 USD | 908.02 USD | 0.00 USD | `+29.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,350,000.00 USD | 4,150.00 USD | 0.00 USD | `+30.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,350,000.00 USD | 533.99 USD | 0.00 USD | `+30.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,350,000.00 USD | 166.43 USD | 0.00 USD | `+30.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,350,000.00 USD | 463.01 USD | 0.00 USD | `+30.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,350,000.00 USD | 320.57 USD | 0.00 USD | `+31.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,350,000.00 USD | 552.72 USD | 0.00 USD | `+32.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,350,000.00 USD | 196.03 USD | 0.00 USD | `+32.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,350,000.00 USD | 287.20 USD | 0.00 USD | `+33.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,350,000.00 USD | 890.45 USD | 0.00 USD | `+36.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,350,000.00 USD | 498.94 USD | 0.00 USD | `+36.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,360,000.00 USD | 964.50 USD | 0.00 USD | `+37.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,360,000.00 USD | 1,930.00 USD | 0.00 USD | `+37.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,360,000.00 USD | 293.25 USD | 0.00 USD | `+38.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,360,000.00 USD | 1,300.00 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,360,000.00 USD | 109.93 USD | 0.00 USD | `+39.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,360,000.00 USD | 439.09 USD | 0.00 USD | `+39.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,360,000.00 USD | 2,590.00 USD | 0.00 USD | `+40.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,360,000.00 USD | 145.34 USD | 0.00 USD | `+41.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,360,000.00 USD | 1,780.00 USD | 0.00 USD | `+41.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,370,000.00 USD | 3,990.00 USD | 0.00 USD | `+41.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,370,000.00 USD | 938.53 USD | 0.00 USD | `+42.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,380,000.00 USD | 11,810.00 USD | 0.00 USD | `+42.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,380,000.00 USD | 203.50 USD | 0.00 USD | `+44.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,380,000.00 USD | 148.99 USD | 0.00 USD | `+45.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,380,000.00 USD | 149.87 USD | 0.00 USD | `+45.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,380,000.00 USD | 150.45 USD | 0.00 USD | `+46.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,380,000.00 USD | 195.51 USD | 0.00 USD | `+48.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,380,000.00 USD | 149.60 USD | 0.00 USD | `+49.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,380,000.00 USD | 156.58 USD | 0.00 USD | `+52.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,380,000.00 USD | 278.43 USD | 0.00 USD | `+56.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,380,000.00 USD | 555.75 USD | 0.00 USD | `+58.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,380,000.00 USD | 165.93 USD | 0.00 USD | `+61.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,380,000.00 USD | 167.39 USD | 0.00 USD | `+63.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,450,000.00 USD | 62,330.00 USD | 0.00 USD | `+70.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,450,000.00 USD | 1,250.00 USD | 0.00 USD | `+70.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,450,000.00 USD | 235.49 USD | 0.00 USD | `+74.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,450,000.00 USD | 3,580.00 USD | 0.00 USD | `+74.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,450,000.00 USD | 421.42 USD | 0.00 USD | `+77.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,450,000.00 USD | 3,750.00 USD | 0.00 USD | `+82.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,450,000.00 USD | 133.64 USD | 0.00 USD | `+84.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,460,000.00 USD | 685.36 USD | 0.00 USD | `+84.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,510,000.00 USD | 58,230.00 USD | 0.00 USD | `+89.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,590,000.00 USD | 80,850.00 USD | 0.00 USD | `+90.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,600,000.00 USD | 6,210.00 USD | 0.00 USD | `+93.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,600,000.00 USD | 349.06 USD | 0.00 USD | `+93.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,600,000.00 USD | 1,060.00 USD | 0.00 USD | `+94.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,620,000.00 USD | 19,210.00 USD | 0.00 USD | `+95.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,620,000.00 USD | 425.19 USD | 0.00 USD | `+97.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,630,000.00 USD | 3,850.00 USD | 0.00 USD | `+99.14%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `609.90` | 39,280,000.00 USD | 0.00 USD | 39,280,000.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `620.90` | 39,250,000.00 USD | 0.00 USD | 39,250,000.00 USD | 0.00 USD | 55,460.00 USD | 265,620.00 USD |
| `7D` | `621.90` | 38,930,000.00 USD | 0.00 USD | 38,930,000.00 USD | 310,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `626.90` | 38,620,000.00 USD | 0.00 USD | 38,620,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `628.90` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `629.90` | 38,310,000.00 USD | 0.00 USD | 38,310,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD |
| `7D` | `630.90` | 38,060,000.00 USD | 0.00 USD | 38,060,000.00 USD | 230,570.00 USD | 50,030.00 USD | 0.00 USD |
| `7D` | `631.90` | 37,780,000.00 USD | 0.00 USD | 37,780,000.00 USD | 58,820.00 USD | 88,750.00 USD | 0.00 USD |
| `1D` | `633.00` | 49,710,000.00 USD | 0.00 USD | 49,710,000.00 USD | 542,970.00 USD | 84,150.00 USD | 48,300.00 USD |
| `1D` | `633.80` | 49,030,000.00 USD | 0.00 USD | 49,030,000.00 USD | 121,020.00 USD | 0.00 USD | 94,050.00 USD |
| `7D` | `633.90` | 37,630,000.00 USD | 0.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.60` | 48,820,000.00 USD | 0.00 USD | 48,820,000.00 USD | 39,810.00 USD | 47,060.00 USD | 75,240.00 USD |
| `7D` | `634.90` | 37,560,000.00 USD | 0.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD |
| `1D` | `635.40` | 48,650,000.00 USD | 0.00 USD | 48,650,000.00 USD | 36,840.00 USD | 9,540.00 USD | 58,120.00 USD |
| `7D` | `635.90` | 37,510,000.00 USD | 0.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD |
| `1D` | `636.20` | 48,550,000.00 USD | 0.00 USD | 48,550,000.00 USD | 122,600.00 USD | 40,910.00 USD | 0.00 USD |
| `1D` | `637.00` | 48,390,000.00 USD | 0.00 USD | 48,390,000.00 USD | 136,880.00 USD | 25,980.00 USD | 240,130.00 USD |
| `1D` | `637.80` | 47,980,000.00 USD | 0.00 USD | 47,980,000.00 USD | 34,750.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `638.60` | 47,950,000.00 USD | 0.00 USD | 47,950,000.00 USD | 28,950.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.40` | 47,880,000.00 USD | 0.00 USD | 47,880,000.00 USD | 242,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `640.20` | 47,640,000.00 USD | 0.00 USD | 47,640,000.00 USD | 0.00 USD | 0.00 USD | 184,710.00 USD |
| `7D` | `640.90` | 37,400,000.00 USD | 0.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD |
| `1D` | `641.00` | 47,450,000.00 USD | 0.00 USD | 47,450,000.00 USD | 0.00 USD | 0.00 USD | 4,880.00 USD |
| `1D` | `641.80` | 47,450,000.00 USD | 0.00 USD | 47,450,000.00 USD | 230,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `641.90` | 37,170,000.00 USD | 0.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD |
| `1D` | `642.60` | 47,220,000.00 USD | 0.00 USD | 47,220,000.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `642.90` | 37,130,000.00 USD | 0.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `643.40` | 47,190,000.00 USD | 0.00 USD | 47,190,000.00 USD | 60,180.00 USD | 6,260.00 USD | 0.00 USD |
| `7D` | `643.90` | 36,960,000.00 USD | 0.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.20` | 47,120,000.00 USD | 0.00 USD | 47,120,000.00 USD | 402,590.00 USD | 31,380.00 USD | 0.00 USD |
| `7D` | `644.90` | 36,930,000.00 USD | 0.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD |
| `1D` | `645.00` | 46,690,000.00 USD | 0.00 USD | 46,690,000.00 USD | 93,740.00 USD | 10,240.00 USD | 341,610.00 USD |
| `1D` | `645.80` | 46,240,000.00 USD | 0.00 USD | 46,240,000.00 USD | 79,070.00 USD | 11,780.00 USD | 34,900.00 USD |
| `7D` | `645.90` | 36,900,000.00 USD | 0.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD |
| `1D` | `646.60` | 46,110,000.00 USD | 0.00 USD | 46,110,000.00 USD | 238,270.00 USD | 2,560.00 USD | 162,050.00 USD |
| `7D` | `646.90` | 36,830,000.00 USD | 0.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD |
| `1D` | `647.40` | 45,710,000.00 USD | 0.00 USD | 45,710,000.00 USD | 136,440.00 USD | 33,700.00 USD | 21,390.00 USD |
| `7D` | `647.90` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD |
| `1D` | `648.20` | 45,520,000.00 USD | 0.00 USD | 45,520,000.00 USD | 153,800.00 USD | 0.00 USD | 7,150.00 USD |
| `7D` | `648.90` | 36,510,000.00 USD | 0.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `649.00` | 45,360,000.00 USD | 0.00 USD | 45,360,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `649.80` | 45,310,000.00 USD | 0.00 USD | 45,310,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `649.90` | 36,490,000.00 USD | 0.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `650.60` | 45,250,000.00 USD | 0.00 USD | 45,250,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `650.90` | 36,310,000.00 USD | 0.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `651.40` | 45,230,000.00 USD | 0.00 USD | 45,230,000.00 USD | 167,330.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `651.90` | 36,260,000.00 USD | 0.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD |
| `1D` | `652.20` | 45,060,000.00 USD | 0.00 USD | 45,060,000.00 USD | 15,190.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `652.90` | 35,990,000.00 USD | 0.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.00` | 44,950,000.00 USD | 0.00 USD | 44,950,000.00 USD | 15,540.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `653.80` | 44,910,000.00 USD | 0.00 USD | 44,910,000.00 USD | 43,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `654.60` | 44,870,000.00 USD | 0.00 USD | 44,870,000.00 USD | 108,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `654.90` | 35,780,000.00 USD | 0.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `655.40` | 44,760,000.00 USD | 0.00 USD | 44,760,000.00 USD | 192,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `655.90` | 35,590,000.00 USD | 0.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD |
| `1D` | `656.20` | 44,560,000.00 USD | 0.00 USD | 44,560,000.00 USD | 78,340.00 USD | 19,650.00 USD | 825,700.00 USD |
| `7D` | `656.90` | 35,520,000.00 USD | 0.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `657.00` | 43,640,000.00 USD | 0.00 USD | 43,640,000.00 USD | 191,620.00 USD | 21,320.00 USD | 0.00 USD |
| `1D` | `657.80` | 43,430,000.00 USD | 0.00 USD | 43,430,000.00 USD | 935,290.00 USD | 14,920.00 USD | 21,320.00 USD |
| `7D` | `657.90` | 35,410,000.00 USD | 0.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD |
| `1D` | `658.60` | 42,460,000.00 USD | 0.00 USD | 42,460,000.00 USD | 171,980.00 USD | 0.00 USD | 81,440.00 USD |
| `7D` | `658.90` | 35,380,000.00 USD | 0.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD |
| `1D` | `659.40` | 42,200,000.00 USD | 0.00 USD | 42,200,000.00 USD | 43,350.00 USD | 7,460.00 USD | 0.00 USD |
| `7D` | `659.90` | 35,350,000.00 USD | 0.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD |
| `1D` | `660.20` | 42,150,000.00 USD | 0.00 USD | 42,150,000.00 USD | 158,810.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `660.90` | 35,200,000.00 USD | 0.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD |
| `1D` | `661.00` | 41,980,000.00 USD | 0.00 USD | 41,980,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `661.80` | 41,900,000.00 USD | 0.00 USD | 41,900,000.00 USD | 592,290.00 USD | 68,060.00 USD | 0.00 USD |
| `7D` | `661.90` | 34,890,000.00 USD | 0.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD |
| `1D` | `662.60` | 41,240,000.00 USD | 0.00 USD | 41,240,000.00 USD | 98,540.00 USD | 87,740.00 USD | 24,990.00 USD |
| `7D` | `662.90` | 34,060,000.00 USD | 0.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD |
| `1D` | `663.40` | 41,020,000.00 USD | 0.00 USD | 41,020,000.00 USD | 202,030.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `663.90` | 33,710,000.00 USD | 0.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD |
| `1D` | `664.20` | 40,800,000.00 USD | 0.00 USD | 40,800,000.00 USD | 126,820.00 USD | 64,390.00 USD | 89,900.00 USD |
| `7D` | `664.90` | 32,730,000.00 USD | 0.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD |
| `1D` | `665.00` | 40,520,000.00 USD | 0.00 USD | 40,520,000.00 USD | 1,270,000.00 USD | 0.00 USD | 43,850.00 USD |
| `1D` | `665.80` | 39,200,000.00 USD | 0.00 USD | 39,200,000.00 USD | 799,990.00 USD | 84,510.00 USD | 746,590.00 USD |
| `7D` | `665.90` | 32,420,000.00 USD | 0.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD |
| `1D` | `666.60` | 37,570,000.00 USD | 0.00 USD | 37,570,000.00 USD | 854,990.00 USD | 22,080.00 USD | 38,830.00 USD |
| `7D` | `666.90` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD |
| `1D` | `667.40` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 449,510.00 USD | 167,750.00 USD | 9,290.00 USD |
| `7D` | `667.90` | 31,380,000.00 USD | 0.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD |
| `1D` | `668.20` | 36,030,000.00 USD | 0.00 USD | 36,030,000.00 USD | 740,290.00 USD | 13,980.00 USD | 3,620.00 USD |
| `7D` | `668.90` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD |
| `1D` | `669.00` | 35,270,000.00 USD | 0.00 USD | 35,270,000.00 USD | 459,030.00 USD | 25,320.00 USD | 18,950.00 USD |
| `1D` | `669.80` | 34,770,000.00 USD | 0.00 USD | 34,770,000.00 USD | 595,120.00 USD | 100,330.00 USD | 1,510,000.00 USD |
| `7D` | `669.90` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD |
| `1D` | `670.60` | 32,570,000.00 USD | 0.00 USD | 32,570,000.00 USD | 509,600.00 USD | 10,760.00 USD | 3,780.00 USD |
| `7D` | `670.90` | 28,970,000.00 USD | 0.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD |
| `1D` | `671.40` | 32,040,000.00 USD | 0.00 USD | 32,040,000.00 USD | 1,860,000.00 USD | 30,160.00 USD | 46,180.00 USD |
| `7D` | `671.90` | 27,970,000.00 USD | 0.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD |
| `1D` | `672.20` | 30,110,000.00 USD | 0.00 USD | 30,110,000.00 USD | 681,270.00 USD | 1,740.00 USD | 15,940.00 USD |
| `7D` | `672.90` | 27,000,000.00 USD | 0.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD |
| `1D` | `673.00` | 29,410,000.00 USD | 0.00 USD | 29,410,000.00 USD | 294,420.00 USD | 178,320.00 USD | 867,320.00 USD |
| `1D` | `673.80` | 28,070,000.00 USD | 0.00 USD | 28,070,000.00 USD | 93,710.00 USD | 241,420.00 USD | 1,540,000.00 USD |
| `7D` | `673.90` | 25,800,000.00 USD | 0.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD |
| `1D` | `674.60` | 26,190,000.00 USD | 0.00 USD | 26,190,000.00 USD | 1,310,000.00 USD | 373,230.00 USD | 196,660.00 USD |
| `7D` | `674.90` | 25,130,000.00 USD | 0.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD |
| `1D` | `675.40` | 24,310,000.00 USD | 0.00 USD | 24,310,000.00 USD | 1,050,000.00 USD | 87,430.00 USD | 368,350.00 USD |
| `7D` | `675.90` | 24,000,000.00 USD | 0.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD |
| `1D` | `676.20` | 22,800,000.00 USD | 0.00 USD | 22,800,000.00 USD | 674,370.00 USD | 434,880.00 USD | 447,680.00 USD |
| `7D` | `676.90` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD |
| `1D` | `677.00` | 21,250,000.00 USD | 0.00 USD | 21,250,000.00 USD | 156,750.00 USD | 90,100.00 USD | 332,880.00 USD |
| `1D` | `677.80` | 20,670,000.00 USD | 0.00 USD | 20,670,000.00 USD | 276,800.00 USD | 172,180.00 USD | 241,380.00 USD |
| `7D` | `677.90` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD |
| `1D` | `678.60` | 19,980,000.00 USD | 0.00 USD | 19,980,000.00 USD | 1,680,000.00 USD | 125,250.00 USD | 157,490.00 USD |
| `7D` | `678.90` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD |
| `1D` | `679.40` | 18,010,000.00 USD | 0.00 USD | 18,010,000.00 USD | 1,320,000.00 USD | 103,590.00 USD | 155,260.00 USD |
| `7D` | `679.90` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD |
| `1D` | `680.20` | 16,440,000.00 USD | 0.00 USD | 16,440,000.00 USD | 314,980.00 USD | 216,090.00 USD | 206,400.00 USD |
| `7D` | `680.90` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `681.00` | 15,700,000.00 USD | 0.00 USD | 15,700,000.00 USD | 597,000.00 USD | 153,360.00 USD | 142,410.00 USD |
| `1D` | `681.80` | 14,810,000.00 USD | 0.00 USD | 14,810,000.00 USD | 452,920.00 USD | 403,510.00 USD | 0.00 USD |
| `7D` | `681.90` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `682.60` | 13,950,000.00 USD | 0.00 USD | 13,950,000.00 USD | 336,330.00 USD | 59,430.00 USD | 0.00 USD |
| `7D` | `682.90` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `683.40` | 13,560,000.00 USD | 0.00 USD | 13,560,000.00 USD | 367,040.00 USD | 0.00 USD | 37,900.00 USD |
| `7D` | `683.90` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `684.20` | 13,150,000.00 USD | 0.00 USD | 13,150,000.00 USD | 531,580.00 USD | 21,510.00 USD | 50,970.00 USD |
| `7D` | `684.90` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `685.00` | 12,550,000.00 USD | 0.00 USD | 12,550,000.00 USD | 0.00 USD | 37,140.00 USD | 0.00 USD |
| `1D` | `685.80` | 12,510,000.00 USD | 0.00 USD | 12,510,000.00 USD | 1,530,000.00 USD | 32,890.00 USD | 0.00 USD |
| `7D` | `685.90` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.60` | 10,950,000.00 USD | 0.00 USD | 10,950,000.00 USD | 0.00 USD | 76,670.00 USD | 98,790.00 USD |
| `7D` | `686.90` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD |
| `1D` | `687.40` | 10,780,000.00 USD | 0.00 USD | 10,780,000.00 USD | 1,030,000.00 USD | 170,560.00 USD | 17,690.00 USD |
| `7D` | `687.90` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD |
| `1D` | `688.20` | 9,560,000.00 USD | 0.00 USD | 9,560,000.00 USD | 548,440.00 USD | 51,480.00 USD | 361,150.00 USD |
| `7D` | `688.90` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD |
| `1D` | `689.00` | 8,600,000.00 USD | 0.00 USD | 8,600,000.00 USD | 81,010.00 USD | 87,000.00 USD | 1,060,000.00 USD |
| `1D` | `689.80` | 7,370,000.00 USD | 0.00 USD | 7,370,000.00 USD | 264,400.00 USD | 66,440.00 USD | 312,860.00 USD |
| `7D` | `689.90` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `690.60` | 6,720,000.00 USD | 0.00 USD | 6,720,000.00 USD | 115,540.00 USD | 152,090.00 USD | 342,060.00 USD |
| `7D` | `690.90` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD |
| `1D` | `691.40` | 6,120,000.00 USD | 0.00 USD | 6,120,000.00 USD | 0.00 USD | 71,060.00 USD | 129,930.00 USD |
| `7D` | `691.90` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `692.20` | 5,910,000.00 USD | 0.00 USD | 5,910,000.00 USD | 780,530.00 USD | 63,190.00 USD | 102,980.00 USD |
| `7D` | `692.90` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD |
| `1D` | `693.00` | 4,970,000.00 USD | 0.00 USD | 4,970,000.00 USD | 76,730.00 USD | 124,290.00 USD | 69,190.00 USD |
| `1D` | `693.80` | 4,700,000.00 USD | 0.00 USD | 4,700,000.00 USD | 320,330.00 USD | 192,140.00 USD | 382,250.00 USD |
| `7D` | `693.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD |
| `1D` | `694.60` | 3,800,000.00 USD | 0.00 USD | 3,800,000.00 USD | 0.00 USD | 86,210.00 USD | 176,360.00 USD |
| `7D` | `694.90` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD |
| `1D` | `695.40` | 3,540,000.00 USD | 0.00 USD | 3,540,000.00 USD | 306,060.00 USD | 66,520.00 USD | 88,480.00 USD |
| `7D` | `695.90` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD |
| `1D` | `696.20` | 3,080,000.00 USD | 0.00 USD | 3,080,000.00 USD | 153,900.00 USD | 32,060.00 USD | 0.00 USD |
| `1D` | `697.00` | 2,890,000.00 USD | 0.00 USD | 2,890,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD |
| `1D` | `697.80` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `698.60` | 2,630,000.00 USD | 0.00 USD | 2,630,000.00 USD | 276,500.00 USD | 0.00 USD | 67,030.00 USD |
| `7D` | `698.90` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.40` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 0.00 USD | 31,670.00 USD | 0.00 USD |
| `1D` | `700.20` | 2,250,000.00 USD | 0.00 USD | 2,250,000.00 USD | 324,120.00 USD | 31,320.00 USD | 0.00 USD |
| `7D` | `700.90` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD |
| `1D` | `701.00` | 1,900,000.00 USD | 0.00 USD | 1,900,000.00 USD | 0.00 USD | 45,990.00 USD | 0.00 USD |
| `1D` | `701.80` | 1,850,000.00 USD | 0.00 USD | 1,850,000.00 USD | 250,700.00 USD | 223,780.00 USD | 35,390.00 USD |
| `7D` | `701.90` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD |
| `1D` | `702.60` | 1,340,000.00 USD | 0.00 USD | 1,340,000.00 USD | 489,100.00 USD | 62,790.00 USD | 157,110.00 USD |
| `7D` | `702.90` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD |
| `1D` | `703.40` | 630,350.00 USD | 0.00 USD | 630,350.00 USD | 363,810.00 USD | 58,910.00 USD | 51,680.00 USD |
| `7D` | `703.90` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD |
| `1D` | `704.20` | 155,960.00 USD | 0.00 USD | 155,960.00 USD | 155,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `704.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `704.90` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `705.80` | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.90` | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `711.40` | 811,300.00 USD | 811,300.00 USD | 0.00 USD | 652,220.00 USD | 0.00 USD | 37,900.00 USD |
| `1D` | `712.20` | 850,080.00 USD | 850,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `714.60` | 948,870.00 USD | 948,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 98,790.00 USD |
| `1D` | `715.40` | 2,180,000.00 USD | 2,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,230,000.00 USD |
| `1D` | `717.80` | 2,320,000.00 USD | 2,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 134,350.00 USD |
| `1D` | `718.60` | 2,770,000.00 USD | 2,770,000.00 USD | 0.00 USD | 270,850.00 USD | 35,360.00 USD | 142,630.00 USD |
| `7D` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `719.40` | 3,070,000.00 USD | 3,070,000.00 USD | 0.00 USD | 0.00 USD | 82,030.00 USD | 219,580.00 USD |
| `7D` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `720.20` | 4,070,000.00 USD | 4,070,000.00 USD | 0.00 USD | 777,080.00 USD | 86,780.00 USD | 134,970.00 USD |
| `7D` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD |
| `1D` | `721.00` | 4,720,000.00 USD | 4,720,000.00 USD | 0.00 USD | 348,700.00 USD | 250,500.00 USD | 50,390.00 USD |
| `1D` | `721.80` | 5,620,000.00 USD | 5,620,000.00 USD | 0.00 USD | 246,260.00 USD | 285,820.00 USD | 368,620.00 USD |
| `7D` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD |
| `1D` | `722.60` | 6,350,000.00 USD | 6,350,000.00 USD | 0.00 USD | 393,920.00 USD | 131,240.00 USD | 207,830.00 USD |
| `7D` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD |
| `1D` | `723.40` | 7,370,000.00 USD | 7,370,000.00 USD | 0.00 USD | 446,650.00 USD | 403,140.00 USD | 175,000.00 USD |
| `7D` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD |
| `1D` | `724.20` | 7,710,000.00 USD | 7,710,000.00 USD | 0.00 USD | 153,900.00 USD | 185,360.00 USD | 0.00 USD |
| `1D` | `725.00` | 8,260,000.00 USD | 8,260,000.00 USD | 0.00 USD | 369,750.00 USD | 152,860.00 USD | 18,950.00 USD |
| `1D` | `725.80` | 8,590,000.00 USD | 8,590,000.00 USD | 0.00 USD | 317,710.00 USD | 0.00 USD | 19,390.00 USD |
| `7D` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD |
| `1D` | `726.60` | 8,930,000.00 USD | 8,930,000.00 USD | 0.00 USD | 226,170.00 USD | 85,880.00 USD | 24,380.00 USD |
| `7D` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD |
| `1D` | `727.40` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 479,630.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD |
| `1D` | `728.20` | 9,620,000.00 USD | 9,620,000.00 USD | 0.00 USD | 159,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD |
| `1D` | `729.00` | 10,510,000.00 USD | 10,510,000.00 USD | 0.00 USD | 493,560.00 USD | 189,850.00 USD | 207,690.00 USD |
| `1D` | `729.80` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 135,850.00 USD | 272,320.00 USD | 531,810.00 USD |
| `7D` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD |
| `1D` | `730.60` | 16,880,000.00 USD | 16,880,000.00 USD | 0.00 USD | 3,010,000.00 USD | 450,040.00 USD | 1,970,000.00 USD |
| `7D` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD |
| `1D` | `731.40` | 17,930,000.00 USD | 17,930,000.00 USD | 0.00 USD | 500,380.00 USD | 65,750.00 USD | 487,410.00 USD |
| `7D` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD |
| `1D` | `732.20` | 20,280,000.00 USD | 20,280,000.00 USD | 0.00 USD | 838,660.00 USD | 147,670.00 USD | 1,370,000.00 USD |
| `7D` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD |
| `1D` | `733.00` | 22,200,000.00 USD | 22,200,000.00 USD | 0.00 USD | 1,090,000.00 USD | 249,610.00 USD | 571,630.00 USD |
| `1D` | `733.80` | 23,190,000.00 USD | 23,190,000.00 USD | 0.00 USD | 365,220.00 USD | 226,780.00 USD | 397,220.00 USD |
| `7D` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD |
| `1D` | `734.60` | 24,220,000.00 USD | 24,220,000.00 USD | 0.00 USD | 967,050.00 USD | 13,440.00 USD | 51,490.00 USD |
| `7D` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD |
| `1D` | `735.40` | 25,220,000.00 USD | 25,220,000.00 USD | 0.00 USD | 140,870.00 USD | 236,320.00 USD | 625,520.00 USD |
| `7D` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD |
| `1D` | `736.20` | 26,030,000.00 USD | 26,030,000.00 USD | 0.00 USD | 556,940.00 USD | 103,040.00 USD | 145,860.00 USD |
| `7D` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD |
| `1D` | `737.00` | 26,430,000.00 USD | 26,430,000.00 USD | 0.00 USD | 208,780.00 USD | 58,330.00 USD | 133,450.00 USD |
| `1D` | `737.80` | 26,950,000.00 USD | 26,950,000.00 USD | 0.00 USD | 363,220.00 USD | 110,210.00 USD | 44,240.00 USD |
| `7D` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `738.60` | 28,010,000.00 USD | 28,010,000.00 USD | 0.00 USD | 490,970.00 USD | 101,820.00 USD | 472,930.00 USD |
| `7D` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD |
| `1D` | `739.40` | 28,770,000.00 USD | 28,770,000.00 USD | 0.00 USD | 266,430.00 USD | 31,860.00 USD | 461,770.00 USD |
| `7D` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD |
| `1D` | `740.20` | 28,980,000.00 USD | 28,980,000.00 USD | 0.00 USD | 69,220.00 USD | 134,150.00 USD | 0.00 USD |
| `7D` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.00` | 29,420,000.00 USD | 29,420,000.00 USD | 0.00 USD | 395,870.00 USD | 32,240.00 USD | 12,190.00 USD |
| `1D` | `741.80` | 29,910,000.00 USD | 29,910,000.00 USD | 0.00 USD | 472,860.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD |
| `1D` | `742.60` | 30,030,000.00 USD | 30,030,000.00 USD | 0.00 USD | 123,310.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD |
| `1D` | `743.40` | 30,300,000.00 USD | 30,300,000.00 USD | 0.00 USD | 250,640.00 USD | 21,120.00 USD | 0.00 USD |
| `7D` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD |
| `1D` | `744.20` | 30,960,000.00 USD | 30,960,000.00 USD | 0.00 USD | 72,280.00 USD | 152,190.00 USD | 436,560.00 USD |
| `7D` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD |
| `1D` | `745.00` | 33,430,000.00 USD | 33,430,000.00 USD | 0.00 USD | 1,470,000.00 USD | 101,280.00 USD | 897,830.00 USD |
| `1D` | `745.80` | 33,850,000.00 USD | 33,850,000.00 USD | 0.00 USD | 253,530.00 USD | 88,530.00 USD | 78,280.00 USD |
| `7D` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 0.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD |
| `1D` | `746.60` | 35,590,000.00 USD | 35,590,000.00 USD | 0.00 USD | 655,180.00 USD | 61,130.00 USD | 1,020,000.00 USD |
| `7D` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 0.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD |
| `1D` | `747.40` | 36,080,000.00 USD | 36,080,000.00 USD | 0.00 USD | 315,280.00 USD | 74,380.00 USD | 98,840.00 USD |
| `1D` | `748.20` | 36,670,000.00 USD | 36,670,000.00 USD | 0.00 USD | 399,610.00 USD | 84,260.00 USD | 108,850.00 USD |
| `7D` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 0.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD |
| `1D` | `749.00` | 37,060,000.00 USD | 37,060,000.00 USD | 0.00 USD | 385,820.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `749.80` | 37,230,000.00 USD | 37,230,000.00 USD | 0.00 USD | 176,420.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 0.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.60` | 37,370,000.00 USD | 37,370,000.00 USD | 0.00 USD | 134,510.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.40` | 37,560,000.00 USD | 37,560,000.00 USD | 0.00 USD | 92,160.00 USD | 0.00 USD | 98,240.00 USD |
| `7D` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `752.20` | 38,110,000.00 USD | 38,110,000.00 USD | 0.00 USD | 83,710.00 USD | 25,010.00 USD | 441,380.00 USD |
| `7D` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD |
| `1D` | `753.00` | 38,730,000.00 USD | 38,730,000.00 USD | 0.00 USD | 371,270.00 USD | 0.00 USD | 248,870.00 USD |
| `1D` | `753.80` | 39,200,000.00 USD | 39,200,000.00 USD | 0.00 USD | 394,820.00 USD | 31,700.00 USD | 40,370.00 USD |
| `7D` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 0.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD |
| `1D` | `754.60` | 39,490,000.00 USD | 39,490,000.00 USD | 0.00 USD | 159,380.00 USD | 121,120.00 USD | 16,910.00 USD |
| `7D` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.40` | 40,030,000.00 USD | 40,030,000.00 USD | 0.00 USD | 302,520.00 USD | 176,290.00 USD | 56,900.00 USD |
| `7D` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 0.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `756.20` | 40,520,000.00 USD | 40,520,000.00 USD | 0.00 USD | 419,920.00 USD | 24,970.00 USD | 46,440.00 USD |
| `7D` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD |
| `1D` | `757.00` | 40,890,000.00 USD | 40,890,000.00 USD | 0.00 USD | 242,660.00 USD | 74,900.00 USD | 49,060.00 USD |
| `1D` | `757.80` | 41,400,000.00 USD | 41,400,000.00 USD | 0.00 USD | 378,680.00 USD | 105,010.00 USD | 32,720.00 USD |
| `7D` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 0.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `758.60` | 42,190,000.00 USD | 42,190,000.00 USD | 0.00 USD | 421,820.00 USD | 93,710.00 USD | 273,090.00 USD |
| `7D` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 0.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD |
| `1D` | `759.40` | 43,250,000.00 USD | 43,250,000.00 USD | 0.00 USD | 996,950.00 USD | 58,640.00 USD | 2,720.00 USD |
| `7D` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 0.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD |
| `1D` | `760.20` | 43,640,000.00 USD | 43,640,000.00 USD | 0.00 USD | 306,860.00 USD | 58,380.00 USD | 25,890.00 USD |
| `7D` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD |
| `1D` | `761.00` | 44,060,000.00 USD | 44,060,000.00 USD | 0.00 USD | 362,020.00 USD | 15,330.00 USD | 40,340.00 USD |
| `1D` | `761.80` | 44,940,000.00 USD | 44,940,000.00 USD | 0.00 USD | 559,960.00 USD | 27,330.00 USD | 297,620.00 USD |
| `7D` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 0.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD |
| `1D` | `762.60` | 46,360,000.00 USD | 46,360,000.00 USD | 0.00 USD | 1,170,000.00 USD | 142,370.00 USD | 97,850.00 USD |
| `7D` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 0.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD |
| `1D` | `763.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 125,250.00 USD | 509,120.00 USD |
| `7D` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 0.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD |
| `1D` | `764.20` | 49,670,000.00 USD | 49,670,000.00 USD | 0.00 USD | 1,240,000.00 USD | 66,030.00 USD | 194,280.00 USD |
| `7D` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 0.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD |
| `1D` | `765.00` | 49,950,000.00 USD | 49,950,000.00 USD | 0.00 USD | 81,300.00 USD | 151,430.00 USD | 46,990.00 USD |
| `1D` | `765.80` | 50,540,000.00 USD | 50,540,000.00 USD | 0.00 USD | 418,510.00 USD | 50,860.00 USD | 127,970.00 USD |
| `7D` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 0.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD |
| `1D` | `766.60` | 51,320,000.00 USD | 51,320,000.00 USD | 0.00 USD | 425,410.00 USD | 137,230.00 USD | 212,120.00 USD |
| `7D` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 0.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD |
| `1D` | `767.40` | 51,970,000.00 USD | 51,970,000.00 USD | 0.00 USD | 524,440.00 USD | 13,640.00 USD | 110,940.00 USD |
| `7D` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 0.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD |
| `1D` | `768.20` | 52,230,000.00 USD | 52,230,000.00 USD | 0.00 USD | 235,790.00 USD | 15,950.00 USD | 12,850.00 USD |
| `7D` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 0.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD |
| `1D` | `769.00` | 52,430,000.00 USD | 52,430,000.00 USD | 0.00 USD | 154,200.00 USD | 25,300.00 USD | 21,990.00 USD |
| `1D` | `769.80` | 52,650,000.00 USD | 52,650,000.00 USD | 0.00 USD | 131,210.00 USD | 62,310.00 USD | 18,560.00 USD |
| `7D` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 0.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD |
| `1D` | `770.60` | 53,060,000.00 USD | 53,060,000.00 USD | 0.00 USD | 82,200.00 USD | 48,080.00 USD | 284,410.00 USD |
| `7D` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 0.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD |
| `1D` | `771.40` | 54,010,000.00 USD | 54,010,000.00 USD | 0.00 USD | 195,200.00 USD | 106,050.00 USD | 648,250.00 USD |
| `7D` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 0.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD |
| `1D` | `772.20` | 54,300,000.00 USD | 54,300,000.00 USD | 0.00 USD | 174,150.00 USD | 75,260.00 USD | 36,760.00 USD |
| `7D` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 0.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD |
| `1D` | `773.00` | 55,120,000.00 USD | 55,120,000.00 USD | 0.00 USD | 702,510.00 USD | 82,250.00 USD | 40,920.00 USD |
| `1D` | `773.80` | 55,650,000.00 USD | 55,650,000.00 USD | 0.00 USD | 460,960.00 USD | 22,230.00 USD | 45,280.00 USD |
| `7D` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 0.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD |
| `1D` | `774.60` | 55,970,000.00 USD | 55,970,000.00 USD | 0.00 USD | 226,710.00 USD | 10,540.00 USD | 87,740.00 USD |
| `7D` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 0.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD |
| `1D` | `775.40` | 56,240,000.00 USD | 56,240,000.00 USD | 0.00 USD | 169,940.00 USD | 47,060.00 USD | 50,590.00 USD |
| `7D` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD |
| `1D` | `776.20` | 56,390,000.00 USD | 56,390,000.00 USD | 0.00 USD | 39,010.00 USD | 21,550.00 USD | 91,630.00 USD |
| `7D` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 0.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD |
| `1D` | `777.00` | 56,770,000.00 USD | 56,770,000.00 USD | 0.00 USD | 295,680.00 USD | 11,790.00 USD | 69,710.00 USD |
| `1D` | `777.80` | 58,120,000.00 USD | 58,120,000.00 USD | 0.00 USD | 869,980.00 USD | 146,000.00 USD | 335,110.00 USD |
| `7D` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 0.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD |
| `1D` | `778.60` | 58,630,000.00 USD | 58,630,000.00 USD | 0.00 USD | 442,360.00 USD | 39,120.00 USD | 29,200.00 USD |
| `7D` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 0.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD |
| `1D` | `779.40` | 59,260,000.00 USD | 59,260,000.00 USD | 0.00 USD | 494,110.00 USD | 37,980.00 USD | 92,470.00 USD |
| `7D` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 0.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD |
| `1D` | `780.20` | 59,390,000.00 USD | 59,390,000.00 USD | 0.00 USD | 25,930.00 USD | 76,410.00 USD | 28,010.00 USD |
| `7D` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 0.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD |
| `1D` | `781.00` | 59,820,000.00 USD | 59,820,000.00 USD | 0.00 USD | 309,210.00 USD | 34,030.00 USD | 86,610.00 USD |
| `1D` | `781.80` | 60,230,000.00 USD | 60,230,000.00 USD | 0.00 USD | 121,170.00 USD | 50,430.00 USD | 239,070.00 USD |
| `7D` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 0.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD |
| `1D` | `782.60` | 60,390,000.00 USD | 60,390,000.00 USD | 0.00 USD | 145,580.00 USD | 0.00 USD | 18,970.00 USD |
| `7D` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 0.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD |
| `1D` | `783.40` | 60,520,000.00 USD | 60,520,000.00 USD | 0.00 USD | 110,270.00 USD | 7,020.00 USD | 4,880.00 USD |
| `7D` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 0.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.20` | 60,680,000.00 USD | 60,680,000.00 USD | 0.00 USD | 162,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 0.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD |
| `1D` | `785.00` | 60,920,000.00 USD | 60,920,000.00 USD | 0.00 USD | 239,950.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `785.80` | 61,040,000.00 USD | 61,040,000.00 USD | 0.00 USD | 117,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 0.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD |
| `1D` | `786.60` | 61,040,000.00 USD | 61,040,000.00 USD | 0.00 USD | 0.00 USD | 6,260.00 USD | 0.00 USD |
| `7D` | `786.90` | 82,500,000.00 USD | 82,500,000.00 USD | 0.00 USD | 601,980.00 USD | 28,250.00 USD | 104,290.00 USD |
| `7D` | `787.90` | 82,910,000.00 USD | 82,910,000.00 USD | 0.00 USD | 261,000.00 USD | 56,730.00 USD | 91,960.00 USD |
| `7D` | `788.90` | 83,800,000.00 USD | 83,800,000.00 USD | 0.00 USD | 750,800.00 USD | 111,010.00 USD | 28,790.00 USD |
| `7D` | `789.90` | 84,470,000.00 USD | 84,470,000.00 USD | 0.00 USD | 327,320.00 USD | 99,920.00 USD | 244,650.00 USD |
| `7D` | `790.90` | 85,300,000.00 USD | 85,300,000.00 USD | 0.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD |
| `7D` | `791.90` | 86,260,000.00 USD | 86,260,000.00 USD | 0.00 USD | 841,380.00 USD | 16,830.00 USD | 96,020.00 USD |
| `7D` | `792.90` | 86,480,000.00 USD | 86,480,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `793.90` | 86,640,000.00 USD | 86,640,000.00 USD | 0.00 USD | 166,240.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.90` | 86,900,000.00 USD | 86,900,000.00 USD | 0.00 USD | 236,740.00 USD | 15,690.00 USD | 0.00 USD |
| `7D` | `795.90` | 87,160,000.00 USD | 87,160,000.00 USD | 0.00 USD | 93,020.00 USD | 14,650.00 USD | 154,910.00 USD |
| `7D` | `796.90` | 87,250,000.00 USD | 87,250,000.00 USD | 0.00 USD | 62,760.00 USD | 33,210.00 USD | 0.00 USD |
| `7D` | `797.90` | 87,360,000.00 USD | 87,360,000.00 USD | 0.00 USD | 103,930.00 USD | 0.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.29B` | Total OI Tokens: `1,832,116.3 BNB`
  * 1h OI Change: `+0.04%` | 4h OI Change: `-2.74%` | 24h OI Change: `+1.10%`
  * Exchange Breakdown: Binance=`562.16M` | Bybit=`135.85M` | OKX=`64.47M` | Hyperliquid=`68.39M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-110.30K` | Last 24h: `-160.49K` | Last 3d: `35.49K` | Last 7d: `220.92K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0394%` |
| **USDT Bybit** | `-0.0632%` | **USDT KuCoin** | `-0.0122%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `-0.0581%` |
| **USDT Gate** | `-0.0022%` | **USDT Bitget** | `-0.0222%` |
| **CoinM Binance** | `0.0339%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `42.86%` | `57.14%` | `0.75` | 54,480,000.00 USD |
| `15M` | `Binance` | `41.53%` | `58.47%` | `0.71` | 19,630,000.00 USD |
| `15M` | `OKX` | `33.7%` | `66.3%` | `0.51` | 10,500,000.00 USD |
| `15M` | `Bybit` | `36.16%` | `63.84%` | `0.57` | 4,180,000.00 USD |
| `15M` | `KuCoin` | `32.3%` | `67.7%` | `0.48` | 337,190.00 USD |
| `15M` | `Gate` | `50.74%` | `49.26%` | `1.03` | 4,750,000.00 USD |
| `15M` | `Bitget` | `53.38%` | `46.62%` | `1.15` | 2,960,000.00 USD |
| `15M` | `BingX` | `44.03%` | `55.97%` | `0.79` | 2,470,000.00 USD |
| `15M` | `MEXC` | `57.36%` | `42.64%` | `1.35` | 3,260,000.00 USD |
| `15M` | `Bitunix` | `57.99%` | `42.01%` | `1.38` | 1,880,000.00 USD |
| `15M` | `Hyperliquid` | `42.85%` | `57.15%` | `0.75` | 1,750,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `50.37%` | `49.63%` | `1.01` | 631,680.00 USD |
| `15M` | `Crypto.com` | `22.7%` | `77.3%` | `0.29` | 303,860.00 USD |
| `15M` | `WhiteBIT` | `66.89%` | `33.11%` | `2.02` | 493,800.00 USD |
| `15M` | `HTX` | `33.11%` | `66.89%` | `0.49` | 58,120.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `35.46%` | `64.54%` | `0.55` | 534,340.00 USD |
| `15M` | `Aster` | `34.51%` | `65.49%` | `0.53` | 341,770.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `51.52%` | `48.48%` | `1.06` | 384,240.00 USD |
| `15M` | `Whale Positions` | `41.53%` | `58.47%` | `0.71` | 19,630,000.00 USD |
| `15M` | `Global Accounts` | `42.86%` | `57.14%` | `0.75` | 54,480,000.00 USD |
| `1H` | `BNB` | `40.48%` | `59.52%` | `0.68` | 52,200,000.00 USD |
| `1H` | `Binance` | `39.14%` | `60.86%` | `0.64` | 33,370,000.00 USD |
| `1H` | `OKX` | `41.73%` | `58.27%` | `0.72` | 3,610,000.00 USD |
| `1H` | `Bybit` | `30.56%` | `69.44%` | `0.44` | 3,570,000.00 USD |
| `1H` | `KuCoin` | `52.79%` | `47.21%` | `1.12` | 692,920.00 USD |
| `1H` | `Gate` | `52.56%` | `47.44%` | `1.11` | 2,440,000.00 USD |
| `1H` | `Bitget` | `29.31%` | `70.69%` | `0.41` | 982,970.00 USD |
| `1H` | `BingX` | `46.77%` | `53.23%` | `0.88` | 1,130,000.00 USD |
| `1H` | `MEXC` | `49.18%` | `50.82%` | `0.97` | 529,730.00 USD |
| `1H` | `Bitunix` | `42.92%` | `57.08%` | `0.75` | 1,280,000.00 USD |
| `1H` | `Hyperliquid` | `53%` | `47%` | `1.13` | 1,470,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `49.58%` | `50.42%` | `0.98` | 536,800.00 USD |
| `1H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `WhiteBIT` | `0.27%` | `99.73%` | `0.00` | 898,160.00 USD |
| `1H` | `HTX` | `49.49%` | `50.51%` | `0.98` | 270,110.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `81.39%` | `18.61%` | `4.37` | 685,710.00 USD |
| `1H` | `Aster` | `64.46%` | `35.54%` | `1.81` | 471,210.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `59.27%` | `40.73%` | `1.46` | 253,820.00 USD |
| `1H` | `Whale Positions` | `39.14%` | `60.86%` | `0.64` | 33,370,000.00 USD |
| `1H` | `Global Accounts` | `40.48%` | `59.52%` | `0.68` | 52,200,000.00 USD |
| `4H` | `BNB` | `47.49%` | `52.51%` | `0.90` | 1,050,000,000.00 USD |
| `4H` | `Binance` | `46.09%` | `53.91%` | `0.85` | 316,060,000.00 USD |
| `4H` | `OKX` | `46.53%` | `53.47%` | `0.87` | 205,640,000.00 USD |
| `4H` | `Bybit` | `50.54%` | `49.46%` | `1.02` | 110,270,000.00 USD |
| `4H` | `KuCoin` | `47.65%` | `52.35%` | `0.91` | 4,680,000.00 USD |
| `4H` | `Gate` | `52.37%` | `47.63%` | `1.10` | 78,270,000.00 USD |
| `4H` | `Bitget` | `42.67%` | `57.33%` | `0.74` | 49,420,000.00 USD |
| `4H` | `BingX` | `45.76%` | `54.24%` | `0.84` | 44,650,000.00 USD |
| `4H` | `MEXC` | `44.48%` | `55.52%` | `0.80` | 94,220,000.00 USD |
| `4H` | `Bitunix` | `47.45%` | `52.55%` | `0.90` | 53,480,000.00 USD |
| `4H` | `Hyperliquid` | `50.17%` | `49.83%` | `1.01` | 39,360,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `51.49%` | `48.51%` | `1.06` | 13,520,000.00 USD |
| `4H` | `Crypto.com` | `46.06%` | `53.94%` | `0.85` | 2,500,000.00 USD |
| `4H` | `WhiteBIT` | `85.67%` | `14.33%` | `5.98` | 13,080,000.00 USD |
| `4H` | `HTX` | `50.18%` | `49.82%` | `1.01` | 1,450,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `29.47%` | `70.53%` | `0.42` | 1,800,000.00 USD |
| `4H` | `Aster` | `44.07%` | `55.93%` | `0.79` | 6,760,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `41.09%` | `58.91%` | `0.70` | 12,310,000.00 USD |
| `4H` | `Whale Positions` | `46.09%` | `53.91%` | `0.85` | 316,060,000.00 USD |
| `4H` | `Global Accounts` | `47.49%` | `52.51%` | `0.90` | 1,050,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `714.45` | `714.97` | `714.45` | `715.95` | `714.15` | 4,744,759.02 USD | 1,432,065.49 USD | 3,312,693.53 USD | -1,880,628.03 USD | `-39.64%` | `0B / 3S` |
| `0:00 UTC` | `715.65` | `715.06` | `715.65` | `715.95` | `714.15` | 8,426,556.65 USD | 1,415,418.26 USD | 7,011,138.39 USD | -5,595,720.13 USD | `-66.41%` | `0B / 4S` |
| `5:00 UTC` | `714.15` | `713.37` | `714.15` | `714.45` | `711.75` | 6,200,853.08 USD | 1,812,683.15 USD | 4,388,169.93 USD | -2,575,486.78 USD | `-41.53%` | `0B / 5S` |
| `0:00 UTC` | `707.55` | `709.41` | `707.55` | `712.65` | `707.25` | 17,460,360.59 USD | 7,319,853.16 USD | 10,140,507.43 USD | -2,820,654.27 USD | `-16.15%` | `0B / 5S` |
| `5:00 UTC` | `706.65` | `707.24` | `706.65` | `708.75` | `705.75` | 12,869,917.05 USD | 6,444,555.70 USD | 6,425,361.36 USD | 19,194.34 USD | `+0.15%` | `1B / 1S` |
| `0:00 UTC` | `706.95` | `706.86` | `706.95` | `708.45` | `705.75` | 8,952,126.09 USD | 3,169,282.84 USD | 5,782,843.25 USD | -2,613,560.41 USD | `-29.19%` | `0B / 2S` |
| `5:00 UTC` | `707.85` | `707.46` | `707.85` | `708.45` | `706.05` | 5,397,479.08 USD | 2,137,235.04 USD | 3,260,244.05 USD | -1,123,009.01 USD | `-20.81%` | `0B / 3S` |
| `0:00 UTC` | `706.05` | `706.04` | `706.05` | `706.95` | `705.15` | 8,644,432.66 USD | 3,111,233.15 USD | 5,533,199.52 USD | -2,421,966.37 USD | `-28.02%` | `0B / 2S` |
| `5:00 UTC` | `705.15` | `704.94` | `705.15` | `705.75` | `703.95` | 6,533,203.74 USD | 2,600,747.39 USD | 3,932,456.35 USD | -1,331,708.96 USD | `-20.38%` | `0B / 1S` |
| `0:00 UTC` | `703.95` | `704.55` | `703.95` | `705.75` | `703.65` | 3,887,315.80 USD | 1,487,524.51 USD | 2,399,791.28 USD | -912,266.77 USD | `-23.47%` | `0B / 1S` |

- **CoinGlass Algorithmic Footprint Signals Table (25_CoinGlass_Footprint_Signals.parquet)**:
| Time | Timeframe | Signal Type | Bias | Headline | Price Level | Absorbed Vol (USD) | Bar Delta (USD) |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| `10-28 20:31` | `Volume 10K BNB` | `Divergence` | **`BULLISH`** | Drop without taker selling | `749.22` | 0.00 USD | 0.00 USD |
| `10-28 19:52` | `Range 2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `747.35` | 0.00 USD | 0.00 USD |
| `10-28 19:17` | `Range 2` | `Exhaustion` | **`BULLISH`** | Seller exhaustion | `748.41` | 0.00 USD | 0.00 USD |
| `10-28 17:33` | `Range 2` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `760.29` | 1,300.00 USD | 0.00 USD |
| `10-28 16:24` | `Volume 10K BNB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `761.59` | 1,600.00 USD | 0.00 USD |
| `10-28 16:22` | `Range 2` | `Exhaustion` | **`BEARISH`** | Buyer exhaustion | `761.59` | 0.00 USD | 0.00 USD |
| `10-28 16:00` | `Range 2` | `Divergence` | **`BEARISH`** | Rally without taker buying | `757.65` | 0.00 USD | 0.00 USD |
| `10-28 13:57` | `Volume 10K BNB` | `Trapped longs` | **`BEARISH`** | Failed breakout | `753.22` | 2,100.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 10K BNB` | `Absorption` | **`BEARISH`** | Buying absorbed at the high | `749.29` | 1,800.00 USD | 0.00 USD |
| `10-28 09:02` | `Volume 10K BNB` | `Trapped longs` | **`BEARISH`** | Failed breakout | `749.29` | 1,800.00 USD | 0.00 USD |

- **12-Horizon Macro Capital Netflows Table (2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet)**:
| Horizon | Spot Netflow (USD) | Futures Netflow (USD) | Institutional Bias |
|:---:|:---:|:---:|:---:|
| `5m` | -54,010.00 USD | -1,860,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -629,390.00 USD | -1,670,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -1,210,000.00 USD | -4,460,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,950,000.00 USD | -8,960,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -8,420,000.00 USD | -25,990,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -11,300,000.00 USD | -39,310,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -7,620,000.00 USD | -38,370,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -15,040,000.00 USD | -53,340,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -22,070,000.00 USD | -52,920,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -52,640,000.00 USD | -109,850,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -65,880,000.00 USD | -136,910,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -164,730,000.00 USD | -473,800,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-54.01K` | 15m=`-629.39K` | 1h=`-1.95M` | 24h=`-52.64M`
* Futures Capital Netflows: 5m=`-1.86M` | 15m=`-1.67M` | 1h=`-8.96M` | 24h=`-109.85M`
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
  * Execution Entry: `699.26` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `690.22` (Risk Distance: `9.04` pts)
  * +2.5R Take Profit: `721.86`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `715.24` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `724.28` (Risk Distance: `9.04` pts)
  * +2.5R Take Profit: `692.64`
  * Mathematical Lot Sizing: **`1.10 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`708.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
