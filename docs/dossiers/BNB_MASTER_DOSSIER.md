# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 17:19:12 IST` (`2026-10-30 11:49:12 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `699.90` | **Live Ask Quote**: `703.10` | **Mid Price**: `701.50`
- **Spread Points**: `320.00` | **Spread BPS**: `45.62 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `701.50` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.75` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `706.41` | Lower -3.00σ Band: `696.59`
  * Upper +2.51σ Band: `705.36` | Lower -2.51σ Band: `697.64`
  * Upper +2.01σ Band: `704.45` | Lower -2.01σ Band: `698.55`
  * Upper +2.00σ Band: `704.31` | Lower -2.00σ Band: `698.69`
  * Upper +1.28σ Band: `703.46` | Lower -1.28σ Band: `699.54`
  * Upper +1.00σ Band: `702.90` | Lower -1.00σ Band: `700.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`701.50` | EMA-20=`701.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`701.50` (Slope: `+0.0000`) | EMA-100=`701.50`
  * Institutional Anchors: EMA-144=`701.50` | EMA-200=`701.50` (Slope: `+0.0000`) | EMA-233=`701.50`
- **Range Boundaries**: 24H High=`708.51` | 24H Low=`694.49` | Weekly High=`715.53` | Weekly Low=`687.47`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.93` (Distance: `-1.88%`)
  * Point of Control (POC) = `700.80` (Distance: `+0.10%`)
  * Value Area Low (VAL) = `698.95` (Distance: `+0.36%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`752.25` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`697.90`
  * New York Session (13:00-21:00 UTC): High=`702.45` | Low=`697.90`
  * Initial Balance (First Hour): IB High=`717.90` | IB Low=`712.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `698.69` - `704.31`
  * Optimal Trade Entry (OTE 0.705): `702.90`
  * Structural Invalidation Anchor (0.786): `707.11`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `703.20` | `703.24` | `701.56` | `701.76` | `3,427` | 2,407,610.21 USD | -961,886.44 USD | `-39.95%` | -51,240,945.27 USD | `-1.45` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `5m` | `701.76` | `702.03` | `701.11` | `701.25` | `2,833` | 1,987,125.62 USD | -263,378.79 USD | `-13.25%` | -51,504,324.06 USD | `-0.01` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `701.25` | `701.36` | `700.55` | `700.72` | `1,802` | 1,263,317.43 USD | -800,251.14 USD | `-63.35%` | -52,304,575.20 USD | `-1.08` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `701.40` | `704.90` | `700.98` | `704.55` | `12,523` | 8,808,249.32 USD | -1,105,644.17 USD | `-12.55%` | -49,877,181.81 USD | `+0.34` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `704.55` | `704.60` | `702.24` | `703.20` | `7,481` | 5,260,203.50 USD | -401,877.02 USD | `-7.64%` | -50,279,058.83 USD | `+0.76` | **`BEARISH`** | `DELTA ALIGNED` |
| `15m` | `703.20` | `703.24` | `700.55` | `700.61` | `8,031` | 5,636,249.37 USD | -2,047,320.26 USD | `-36.32%` | -52,326,379.09 USD | `-0.41` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `705.59` | `705.77` | `701.87` | `702.57` | `37,167` | 26,150,375.30 USD | -2,890,562.45 USD | `-11.05%` | -51,182,747.74 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `702.57` | `704.90` | `700.77` | `703.20` | `36,793` | 25,855,185.75 USD | -3,007,688.24 USD | `-11.63%` | -54,190,435.98 USD | `+0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `703.20` | `703.24` | `700.55` | `700.60` | `8,022` | 5,630,294.20 USD | -2,052,154.47 USD | `-36.45%` | -56,242,590.45 USD | `+0.13` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `700.55` | `700.60` | `123,789` | 87,163,096.83 USD | -15,440,649.91 USD | `-17.71%` | -56,242,590.45 USD | `-0.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | 8,277,694.32 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | 775,183.01 USD | `-1.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `700.55` | `700.60` | `123,789` | 87,163,096.83 USD | -15,440,649.91 USD | `-17.71%` | -56,242,590.45 USD | `-0.56` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| --- | **`701.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `701.52` | `1118000000.0000` | 784.30 USD | 121,217.68 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `701.53` | `9502000000.0000` | 6,665.94 USD | 120,433.38 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `701.57` | `13953000000.0000` | 9,789.01 USD | 113,767.45 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `701.58` | `25693000000.0000` | 18,025.69 USD | 103,978.44 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `701.61` | `1492000000.0000` | 1,046.80 USD | 85,952.74 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `701.64` | `10726000000.0000` | 7,525.79 USD | 84,905.94 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `701.67` | `14207000000.0000` | 9,968.63 USD | 77,380.15 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `701.68` | `56480000000.0000` | 39,630.89 USD | 67,411.53 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `701.69` | `19746000000.0000` | 13,855.57 USD | 27,780.64 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `701.70` | `1001000000.0000` | 702.40 USD | 13,925.07 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `701.73` | `2342000000.0000` | 1,643.45 USD | 13,222.67 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `701.76` | `1491000000.0000` | 1,046.32 USD | 11,579.22 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `701.79` | `1475000000.0000` | 1,035.14 USD | 10,532.89 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `701.83` | `2342000000.0000` | 1,643.69 USD | 9,497.75 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `701.84` | `1491000000.0000` | 1,046.44 USD | 7,854.07 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `701.91` | `712000000.0000` | 499.76 USD | 6,807.62 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `701.92` | `1491000000.0000` | 1,046.56 USD | 6,307.86 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `701.95` | `2342000000.0000` | 1,643.97 USD | 5,261.30 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `701.98` | `3662000000.0000` | 2,570.65 USD | 3,617.33 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `702.00` | `1491000000.0000` | 1,046.68 USD | 1,046.68 USD | `1 orders` | `-0.01%` | `-` |
| `MID_SPREAD` | `702.05` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 702.05` | `0.00%` | `-` |
| `ASK` | `702.09` | `5341000000.0000` | 3,749.86 USD | 3,749.86 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.10` | `5341000000.0000` | 3,749.92 USD | 7,499.78 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.11` | `5341000000.0000` | 3,749.97 USD | 11,249.75 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.12` | `9495000000.0000` | 6,666.63 USD | 17,916.38 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.13` | `13408000000.0000` | 9,414.16 USD | 27,330.54 USD | `6 orders` | `+0.01%` | `-` |
| `ASK` | `702.14` | `150000000.0000` | 105.32 USD | 27,435.86 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.15` | `4351000000.0000` | 3,055.05 USD | 30,490.91 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `702.25` | `15822000000.0000` | 11,111.00 USD | 41,601.91 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `702.26` | `150000000.0000` | 105.34 USD | 41,707.25 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `702.28` | `299000000.0000` | 209.98 USD | 41,917.23 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `702.36` | `2340000000.0000` | 1,643.52 USD | 43,560.76 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `702.39` | `18983000000.0000` | 13,333.47 USD | 56,894.22 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `702.42` | `427000000.0000` | 299.93 USD | 57,194.16 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `702.44` | `71000000.0000` | 49.87 USD | 57,244.03 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `702.45` | `2479000000.0000` | 1,741.37 USD | 58,985.40 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `702.46` | `42057000000.0000` | 29,543.36 USD | 88,528.76 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `702.47` | `150000000.0000` | 105.37 USD | 88,634.14 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `702.48` | `2340000000.0000` | 1,643.80 USD | 90,277.94 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `702.49` | `1118000000.0000` | 785.38 USD | 91,063.32 USD | `1 orders` | `+0.06%` | `-` |
| `ASK` | `702.51` | `7196000000.0000` | 5,055.26 USD | 96,118.58 USD | `1 orders` | `+0.07%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:52:59 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `793` | `0xea00...a918` | `LONG` | 2,878,695.55 USD | `4,098,429,000,000.00` | `787.24` | `701.99` | `0.000000` | -347,731.24 USD | `-12.08%` | `5X Cross` |
| `891` | `0x7d0c...1b28` | `LONG` | 2,495,336.85 USD | `3,554,054,000,000.00` | `703.79` | `701.99` | `0.000000` | -5,969.89 USD | `-0.24%` | `10X Cross` |
| `909` | `0xfe7c...b7ae` | `LONG` | 2,451,469.72 USD | `3,491,575,000,000.00` | `686.05` | `701.99` | `0.000000` | 56,058.86 USD | `+2.29%` | `10X Cross` |
| `1121` | `0x27c9...d65d` | `LONG` | 1,952,514.96 USD | `2,779,816,000,000.00` | `700.84` | `701.99` | `160.76` | 4,300.15 USD | `+0.22%` | `10X Cross` |
| `1191` | `0x7737...bf66` | `SHORT` | 1,858,067.51 USD | `2,646,179,000,000.00` | `752.73` | `701.99` | `7053.96` | 133,803.08 USD | `+7.20%` | `10X Cross` |
| `1366` | `0x51f6...2b39` | `LONG` | 1,573,294.50 USD | `2,240,640,000,000.00` | `703.00` | `701.99` | `111.34` | -1,865.23 USD | `-0.12%` | `10X Cross` |
| `1496` | `0xc675...795d` | `LONG` | 1,442,862.99 USD | `2,055,214,000,000.00` | `706.91` | `701.99` | `640.73` | -9,981.68 USD | `-0.69%` | `10X Cross` |
| `1537` | `0x2edd...8179` | `LONG` | 1,403,101.54 USD | `1,998,407,000,000.00` | `714.56` | `701.99` | `0.000000` | -24,882.65 USD | `-1.77%` | `10X Cross` |
| `1581` | `0x325e...9564` | `LONG` | 1,358,029.59 USD | `1,934,212,000,000.00` | `707.43` | `701.99` | `0.000000` | -10,296.18 USD | `-0.76%` | `10X Cross` |
| `1720` | `0x07fd...689d` | `LONG` | 1,224,580.20 USD | `1,744,292,000,000.00` | `714.31` | `701.99` | `0.000000` | -21,383.35 USD | `-1.75%` | `10X Cross` |
| `1731` | `0xecb6...2b00` | `SHORT` | 1,214,614.49 USD | `1,729,949,000,000.00` | `712.79` | `701.99` | `19086.63` | 18,473.31 USD | `+1.52%` | `5X Cross` |
| `1735` | `0x645b...87b8` | `LONG` | 1,209,117.66 USD | `1,721,990,000,000.00` | `747.34` | `701.99` | `0.000000` | -77,789.75 USD | `-6.43%` | `10X Cross` |
| `1794` | `0xa4a6...46cf` | `SHORT` | 1,157,703.46 USD | `1,648,704,000,000.00` | `711.73` | `701.99` | `1614.12` | 15,734.89 USD | `+1.36%` | `10X Cross` |
| `1892` | `0xfc27...9d9d` | `LONG` | 1,075,256.61 USD | `1,531,349,000,000.00` | `701.15` | `701.99` | `0.000000` | 1,548.75 USD | `+0.14%` | `10X Cross` |
| `1913` | `0x14c6...b280` | `SHORT` | 1,053,211.50 USD | `1,500,000,000,000.00` | `712.51` | `701.99` | `1466.72` | 15,550.20 USD | `+1.48%` | `10X Cross` |
| `1959` | `0x4420...4c4b` | `LONG` | 1,027,196.77 USD | `1,462,889,000,000.00` | `704.02` | `701.99` | `181.91` | -2,705.85 USD | `-0.26%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `744.57` | 44,579.64 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale SELL: 44.58K USD at 744.5700 USD [API] | `2026-10-29 18:26:19` |
| `ANNOUNCEMENT` | `INFO` | `709.14` | 8,495.50 USD | `-` | `NEWS_INTEL` | `-` | #BNB Liquidated Short: 8.50K USD at 709.1400 USD [API] | `2026-10-29 20:38:10` |
| `ANNOUNCEMENT` | `INFO` | `709.14` | 2,858.54 USD | `-` | `NEWS_INTEL` | `-` | #BNB Liquidated Short: 2.86K USD at 709.1400 USD [API] | `2026-10-29 20:38:10` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`728.51` (Vol: 1,600,000.00 USD, Dist: `+3.62%`) | Long MP=`677.23` (Vol: 3,200,000.00 USD, Dist: `--3.68%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+9.22%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.67%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+9.22%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.67%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+9.22%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.67%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `140.50` | 850.02 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `141.50` | 5,520.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `145.50` | 2,040.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `154.50` | 4,370.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `166.50` | 99,900.00 USD | 5,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 315.50 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `176.50` | 5,980.00 USD | 5,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `180.50` | 696.73 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `182.50` | 519.58 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `183.50` | 510,100.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `196.50` | 135.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `203.50` | 309,350.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `210.50` | 258.28 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `212.50` | 21,250.00 USD | 4,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `218.50` | 190.31 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `221.50` | 272.22 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `236.50` | 359.72 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `243.50` | 16,910.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 1,370.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `258.50` | 258,500.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `259.50` | 1,370.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `268.50` | 21,280.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `301.50` | 5,360.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `311.50` | 154,780.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `325.50` | 1,020.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 376.06 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `346.50` | 122.31 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `347.50` | 961.53 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `355.50` | 303.60 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 1,980.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `365.50` | 548.25 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 10,630.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 73,190.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `376.50` | 11,540.00 USD | 4,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 950.92 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 17,680.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 1,910.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 10,870.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 2,510.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 341.17 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `390.50` | 3,370.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `392.50` | 103.62 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 1,100.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 1,950.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 158.20 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 522.32 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 1,690.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 8,190.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 619.57 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `403.50` | 102.09 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 3,490.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 11,690.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 2,700.00 USD | 4,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 2,350.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 5,100.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 60,370.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,440.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `424.50` | 4,250.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 616.48 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `432.50` | 3,370.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 133.13 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,980.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `447.50` | 1,680.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `451.50` | 8,890.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 464.50 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 2,400.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `483.50` | 483.50 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 5,240.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 207.25 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 256.91 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 2,300.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `492.50` | 140.36 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 2,270.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 11,260.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 5,150.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 186.69 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 14,130.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 3,500.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 6,630.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `507.50` | 62,650.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 2,750.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 830.99 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 317.45 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 6,470.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 41,970.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 703.92 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 662.60 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 178,590.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 2,090.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `523.50` | 53,820.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 289.03 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,410.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 136,080.00 USD | 3,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 1,350.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 208.88 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 422.81 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,680.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 211,300.00 USD | 3,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 12,560.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,740.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 82,810.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 3,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 791.65 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 984.80 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `562.50` | 1,510.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 143.83 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 750,370.00 USD | 3,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `573.50` | 458.80 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.50` | 1,020.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 2,690.00 USD | 2,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 5,780.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 1,230.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 165,950.00 USD | 2,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,060.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,240.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 16,390.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,420.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `591.50` | 2,180.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 226.93 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 44,960.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 940.89 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 7,680.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,480.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 791.22 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 222.32 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 22,860.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 256.91 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 60,390.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 4,250.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 6,410.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `615.50` | 1,540.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 2,690.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `620.80` | 40,560,000.00 USD | 40,560,000.00 USD | 0.00 USD | 0.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 696.70 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `621.70` | 40,290,000.00 USD | 40,290,000.00 USD | 310,160.00 USD | 55,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `623.50` | 415.25 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 22,260.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `626.20` | 39,920,000.00 USD | 39,920,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `628.50` | 590.79 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `628.90` | 39,880,000.00 USD | 39,880,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `629.80` | 39,620,000.00 USD | 39,620,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `630.70` | 54,730,000.00 USD | 54,730,000.00 USD | 52,660.00 USD | 26,750.00 USD | 382,570.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `630.70` | 39,360,000.00 USD | 39,360,000.00 USD | 0.00 USD | 50,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `631.50` | 54,260,000.00 USD | 54,260,000.00 USD | 73,890.00 USD | 103,360.00 USD | 604,560.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `631.60` | 39,310,000.00 USD | 39,310,000.00 USD | 289,390.00 USD | 113,090.00 USD | 53,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `632.30` | 53,480,000.00 USD | 53,480,000.00 USD | 564,850.00 USD | 86,460.00 USD | 135,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `632.50` | 38,860,000.00 USD | 38,860,000.00 USD | 0.00 USD | 13,560.00 USD | 47,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.10` | 52,700,000.00 USD | 52,700,000.00 USD | 174,370.00 USD | 11,550.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `633.40` | 38,800,000.00 USD | 38,800,000.00 USD | 87,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `633.90` | 52,480,000.00 USD | 52,480,000.00 USD | 217,300.00 USD | 37,950.00 USD | 83,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `634.30` | 38,710,000.00 USD | 38,710,000.00 USD | 0.00 USD | 13,860.00 USD | 65,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 5,900.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.70` | 52,140,000.00 USD | 52,140,000.00 USD | 39,810.00 USD | 16,410.00 USD | 75,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `635.20` | 38,630,000.00 USD | 38,630,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `635.50` | 52,010,000.00 USD | 52,010,000.00 USD | 101,710.00 USD | 9,540.00 USD | 58,120.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `636.10` | 38,580,000.00 USD | 38,580,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `636.30` | 51,840,000.00 USD | 51,840,000.00 USD | 57,730.00 USD | 56,570.00 USD | 236,370.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.10` | 51,490,000.00 USD | 51,490,000.00 USD | 136,880.00 USD | 10,320.00 USD | 3,760.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.90` | 51,340,000.00 USD | 51,340,000.00 USD | 59,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.70` | 51,280,000.00 USD | 51,280,000.00 USD | 4,240.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `639.50` | 51,240,000.00 USD | 51,240,000.00 USD | 242,510.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 1,490.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `640.60` | 38,470,000.00 USD | 38,470,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.10` | 50,810,000.00 USD | 50,810,000.00 USD | 0.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.90` | 50,810,000.00 USD | 50,810,000.00 USD | 230,450.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `642.40` | 38,250,000.00 USD | 38,250,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `642.50` | 334.10 USD | 334.10 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.70` | 50,580,000.00 USD | 50,580,000.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `643.30` | 38,210,000.00 USD | 38,210,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `643.50` | 50,540,000.00 USD | 50,540,000.00 USD | 69,670.00 USD | 6,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 449,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `644.20` | 38,030,000.00 USD | 38,030,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.30` | 50,470,000.00 USD | 50,470,000.00 USD | 393,100.00 USD | 36,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `644.50` | 19,460.00 USD | 448,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `645.10` | 50,040,000.00 USD | 50,040,000.00 USD | 93,740.00 USD | 4,720.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `645.10` | 38,000,000.00 USD | 38,000,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 307.26 USD | 429,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `645.90` | 49,600,000.00 USD | 49,600,000.00 USD | 79,070.00 USD | 11,780.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `646.00` | 37,970,000.00 USD | 37,970,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 428,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.70` | 49,470,000.00 USD | 49,470,000.00 USD | 250,710.00 USD | 2,560.00 USD | 169,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `646.90` | 37,900,000.00 USD | 37,900,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.50` | 49,050,000.00 USD | 49,050,000.00 USD | 140,910.00 USD | 33,700.00 USD | 21,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `647.80` | 37,730,000.00 USD | 37,730,000.00 USD | 76,970.00 USD | 16,830.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `648.30` | 48,850,000.00 USD | 48,850,000.00 USD | 136,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 428,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `648.70` | 37,620,000.00 USD | 37,620,000.00 USD | 45,630.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.10` | 48,720,000.00 USD | 48,720,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 426,890.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `649.60` | 37,560,000.00 USD | 37,560,000.00 USD | 104,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.90` | 48,670,000.00 USD | 48,670,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `650.50` | 37,460,000.00 USD | 37,460,000.00 USD | 81,630.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 335.01 USD | 425,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `650.70` | 48,600,000.00 USD | 48,600,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `651.40` | 37,360,000.00 USD | 37,360,000.00 USD | 0.00 USD | 14,650.00 USD | 154,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `651.50` | 48,590,000.00 USD | 48,590,000.00 USD | 167,330.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 13,790.00 USD | 424,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.30` | 48,420,000.00 USD | 48,420,000.00 USD | 15,190.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `652.30` | 37,190,000.00 USD | 37,190,000.00 USD | 196,170.00 USD | 33,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 411,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.10` | 48,310,000.00 USD | 48,310,000.00 USD | 15,540.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `653.20` | 36,960,000.00 USD | 36,960,000.00 USD | 109,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 98,240.00 USD | 410,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `653.90` | 48,270,000.00 USD | 48,270,000.00 USD | 56,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 312,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.70` | 48,210,000.00 USD | 48,210,000.00 USD | 143,830.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `655.00` | 36,850,000.00 USD | 36,850,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `655.50` | 48,070,000.00 USD | 48,070,000.00 USD | 245,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 122.58 USD | 312,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `655.90` | 36,660,000.00 USD | 36,660,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.30` | 47,820,000.00 USD | 47,820,000.00 USD | 77,320.00 USD | 19,650.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `656.50` | 24,500.00 USD | 312,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `656.80` | 36,590,000.00 USD | 36,590,000.00 USD | 143,550.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.10` | 46,900,000.00 USD | 46,900,000.00 USD | 187,030.00 USD | 21,320.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `657.50` | 13,020.00 USD | 287,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `657.70` | 36,440,000.00 USD | 36,440,000.00 USD | 0.00 USD | 7,610.00 USD | 9,210.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.90` | 46,690,000.00 USD | 46,690,000.00 USD | 935,290.00 USD | 14,920.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 2,050.00 USD | 274,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `658.60` | 36,420,000.00 USD | 36,420,000.00 USD | 0.00 USD | 10,650.00 USD | 23,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.70` | 45,720,000.00 USD | 45,720,000.00 USD | 171,980.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `659.50` | 45,470,000.00 USD | 45,470,000.00 USD | 111,490.00 USD | 7,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `659.50` | 36,390,000.00 USD | 36,390,000.00 USD | 38,970.00 USD | 20,150.00 USD | 87,160.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 45,510.00 USD | 272,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.30` | 45,350,000.00 USD | 45,350,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `660.40` | 36,240,000.00 USD | 36,240,000.00 USD | 21,730.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 226,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.10` | 45,240,000.00 USD | 45,240,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `661.30` | 36,210,000.00 USD | 36,210,000.00 USD | 343,180.00 USD | 17,690.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 223,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `661.90` | 45,160,000.00 USD | 45,160,000.00 USD | 592,290.00 USD | 68,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `662.20` | 35,820,000.00 USD | 35,820,000.00 USD | 113,650.00 USD | 19,070.00 USD | 697,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 203,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.70` | 44,500,000.00 USD | 44,500,000.00 USD | 98,540.00 USD | 87,740.00 USD | 24,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `663.10` | 34,990,000.00 USD | 34,990,000.00 USD | 863,730.00 USD | 138,640.00 USD | 21,580.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `663.50` | 44,290,000.00 USD | 44,290,000.00 USD | 202,030.00 USD | 5,000.00 USD | 19,650.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 13,440.00 USD | 200,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.00` | 33,960,000.00 USD | 33,960,000.00 USD | 167,890.00 USD | 18,740.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.30` | 44,060,000.00 USD | 44,060,000.00 USD | 785,690.00 USD | 64,390.00 USD | 89,900.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 592.73 USD | 187,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.90` | 33,750,000.00 USD | 33,750,000.00 USD | 237,720.00 USD | 22,990.00 USD | 38,120.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.10` | 43,120,000.00 USD | 43,120,000.00 USD | 684,260.00 USD | 0.00 USD | 43,850.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 8,790.00 USD | 186,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.80` | 33,450,000.00 USD | 33,450,000.00 USD | 348,440.00 USD | 54,100.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.90` | 42,390,000.00 USD | 42,390,000.00 USD | 756,330.00 USD | 84,510.00 USD | 746,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 2,200.00 USD | 177,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.70` | 40,800,000.00 USD | 40,800,000.00 USD | 839,260.00 USD | 13,270.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.70` | 32,990,000.00 USD | 32,990,000.00 USD | 398,430.00 USD | 39,830.00 USD | 62,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.50` | 39,920,000.00 USD | 39,920,000.00 USD | 516,430.00 USD | 167,750.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,830.00 USD | 175,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.60` | 32,490,000.00 USD | 32,490,000.00 USD | 601,660.00 USD | 45,130.00 USD | 39,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.30` | 39,230,000.00 USD | 39,230,000.00 USD | 754,630.00 USD | 3,380.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.50` | 31,810,000.00 USD | 31,810,000.00 USD | 846,160.00 USD | 82,630.00 USD | 62,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 8,920.00 USD | 173,700.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.10` | 38,470,000.00 USD | 38,470,000.00 USD | 486,520.00 USD | 70,860.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.40` | 30,810,000.00 USD | 30,810,000.00 USD | 629,370.00 USD | 48,360.00 USD | 98,640.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 5,060.00 USD | 164,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `669.90` | 37,890,000.00 USD | 37,890,000.00 USD | 478,650.00 USD | 43,250.00 USD | 1,510,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.30` | 30,040,000.00 USD | 30,040,000.00 USD | 206,130.00 USD | 92,120.00 USD | 43,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 4,670.00 USD | 159,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.70` | 35,860,000.00 USD | 35,860,000.00 USD | 474,770.00 USD | 10,760.00 USD | 3,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.20` | 29,700,000.00 USD | 29,700,000.00 USD | 780,550.00 USD | 43,140.00 USD | 714,260.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `671.50` | 35,370,000.00 USD | 35,370,000.00 USD | 1,900,000.00 USD | 30,160.00 USD | 46,180.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 830.65 USD | 155,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `672.10` | 28,160,000.00 USD | 28,160,000.00 USD | 108,430.00 USD | 26,430.00 USD | 40,110.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `672.30` | 33,390,000.00 USD | 33,390,000.00 USD | 591,410.00 USD | 3,440.00 USD | 139,170.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 7,860.00 USD | 154,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.00` | 27,980,000.00 USD | 27,980,000.00 USD | 1,010,000.00 USD | 165,010.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.10` | 32,660,000.00 USD | 32,660,000.00 USD | 212,350.00 USD | 280,780.00 USD | 1,050,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 39,130.00 USD | 146,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `673.90` | 31,110,000.00 USD | 31,110,000.00 USD | 280,490.00 USD | 215,360.00 USD | 1,630,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.90` | 26,770,000.00 USD | 26,770,000.00 USD | 335,670.00 USD | 329,650.00 USD | 251,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,100.00 USD | 107,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.70` | 28,980,000.00 USD | 28,980,000.00 USD | 1,310,000.00 USD | 399,040.00 USD | 458,040.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.80` | 25,850,000.00 USD | 25,850,000.00 USD | 312,600.00 USD | 184,460.00 USD | 520,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.50` | 26,810,000.00 USD | 26,810,000.00 USD | 1,420,000.00 USD | 187,180.00 USD | 460,780.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 74,720.00 USD | 103,130.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.70` | 24,840,000.00 USD | 24,840,000.00 USD | 550,560.00 USD | 36,500.00 USD | 2,400,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.30` | 24,750,000.00 USD | 24,750,000.00 USD | 822,970.00 USD | 347,350.00 USD | 445,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,960.00 USD | 28,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.60` | 21,850,000.00 USD | 21,850,000.00 USD | 518,720.00 USD | 455,810.00 USD | 358,560.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.10` | 23,130,000.00 USD | 23,130,000.00 USD | 93,570.00 USD | 87,370.00 USD | 312,780.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `677.50` | 20,520,000.00 USD | 20,520,000.00 USD | 2,260,000.00 USD | 128,230.00 USD | 903,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 250.67 USD | 26,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `677.90` | 22,640,000.00 USD | 22,640,000.00 USD | 438,990.00 USD | 172,180.00 USD | 250,510.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.40` | 17,230,000.00 USD | 17,230,000.00 USD | 465,560.00 USD | 73,000.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 2,390.00 USD | 26,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `678.70` | 21,780,000.00 USD | 21,780,000.00 USD | 1,530,000.00 USD | 164,420.00 USD | 148,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.30` | 16,650,000.00 USD | 16,650,000.00 USD | 82,740.00 USD | 53,030.00 USD | 158,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `679.50` | 19,930,000.00 USD | 19,930,000.00 USD | 1,590,000.00 USD | 80,850.00 USD | 155,260.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 998.19 USD | 23,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `680.20` | 16,350,000.00 USD | 16,350,000.00 USD | 21,320.00 USD | 65,770.00 USD | 163,020.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.30` | 18,100,000.00 USD | 18,100,000.00 USD | 25,960.00 USD | 215,610.00 USD | 261,300.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 21,870.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.10` | 17,600,000.00 USD | 17,600,000.00 USD | 597,000.00 USD | 206,150.00 USD | 87,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.10` | 16,100,000.00 USD | 16,100,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `681.90` | 16,710,000.00 USD | 16,710,000.00 USD | 452,920.00 USD | 334,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.00` | 15,870,000.00 USD | 15,870,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.70` | 15,920,000.00 USD | 15,920,000.00 USD | 336,330.00 USD | 59,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.90` | 14,110,000.00 USD | 14,110,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.50` | 15,530,000.00 USD | 15,530,000.00 USD | 468,720.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.80` | 14,070,000.00 USD | 14,070,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.30` | 15,020,000.00 USD | 15,020,000.00 USD | 429,900.00 USD | 21,510.00 USD | 50,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.70` | 13,990,000.00 USD | 13,990,000.00 USD | 369,590.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.10` | 14,520,000.00 USD | 14,520,000.00 USD | 406,260.00 USD | 37,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.60` | 13,510,000.00 USD | 13,510,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.90` | 14,080,000.00 USD | 14,080,000.00 USD | 1,120,000.00 USD | 48,550.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.50` | 12,310,000.00 USD | 12,310,000.00 USD | 58,940.00 USD | 36,480.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.70` | 12,910,000.00 USD | 12,910,000.00 USD | 135,120.00 USD | 141,180.00 USD | 525,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.40` | 12,220,000.00 USD | 12,220,000.00 USD | 148,480.00 USD | 580,220.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.50` | 12,110,000.00 USD | 12,110,000.00 USD | 1,250,000.00 USD | 292,550.00 USD | 326,890.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.30` | 10,230,000.00 USD | 10,230,000.00 USD | 770,930.00 USD | 133,560.00 USD | 801,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.30` | 11,370,000.00 USD | 11,370,000.00 USD | 234,210.00 USD | 427,630.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.10` | 8,520,000.00 USD | 8,520,000.00 USD | 646,890.00 USD | 111,110.00 USD | 1,480,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.20` | 10,440,000.00 USD | 10,440,000.00 USD | 234,630.00 USD | 57,190.00 USD | 2,350,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.90` | 6,290,000.00 USD | 6,290,000.00 USD | 825,990.00 USD | 106,890.00 USD | 358,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.10` | 7,800,000.00 USD | 7,800,000.00 USD | 543,670.00 USD | 237,760.00 USD | 1,340,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.70` | 5,000,000.00 USD | 5,000,000.00 USD | 329,760.00 USD | 199,550.00 USD | 401,550.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.00` | 5,680,000.00 USD | 5,680,000.00 USD | 281,290.00 USD | 325,740.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.50` | 4,060,000.00 USD | 4,060,000.00 USD | 0.00 USD | 71,280.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.90` | 3,950,000.00 USD | 3,950,000.00 USD | 22,150.00 USD | 0.00 USD | 969,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.30` | 3,940,000.00 USD | 3,940,000.00 USD | 780,530.00 USD | 31,410.00 USD | 102,980.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.80` | 2,960,000.00 USD | 2,960,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.10` | 3,030,000.00 USD | 3,030,000.00 USD | 76,730.00 USD | 159,980.00 USD | 69,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.70` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.90` | 2,720,000.00 USD | 2,720,000.00 USD | 320,330.00 USD | 140,550.00 USD | 382,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.60` | 1,500,000.00 USD | 1,500,000.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.70` | 1,880,000.00 USD | 1,880,000.00 USD | 66,510.00 USD | 118,590.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.50` | 1,510,000.00 USD | 1,510,000.00 USD | 239,550.00 USD | 34,140.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.50` | 1,040,000.00 USD | 1,040,000.00 USD | 0.00 USD | 128,880.00 USD | 335,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.30` | 1,150,000.00 USD | 1,150,000.00 USD | 153,900.00 USD | 32,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `696.50` | 2,350.00 USD | 2,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `697.10` | 966,400.00 USD | 966,400.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `697.90` | 902,690.00 USD | 902,690.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.70` | 699,330.00 USD | 699,330.00 USD | 276,500.00 USD | 0.00 USD | 67,030.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.10` | 575,930.00 USD | 575,930.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.50` | 355,790.00 USD | 355,790.00 USD | 0.00 USD | 31,670.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.30` | 324,120.00 USD | 324,120.00 USD | 324,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `705.90` | 121,180.00 USD | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `709.90` | 677,910.00 USD | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `710.70` | 464,720.00 USD | 464,720.00 USD | 343,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.50` | 850,080.00 USD | 850,080.00 USD | 308,680.00 USD | 0.00 USD | 76,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `712.60` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `714.70` | 1,850,000.00 USD | 1,850,000.00 USD | 135,120.00 USD | 21,500.00 USD | 841,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `715.30` | 947,510.00 USD | 947,510.00 USD | 0.00 USD | 40,990.00 USD | 112,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `715.50` | 3,480,000.00 USD | 3,480,000.00 USD | 227,340.00 USD | 180,660.00 USD | 1,230,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `716.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 231,020.00 USD | 269,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `716.30` | 4,150,000.00 USD | 4,150,000.00 USD | 203,920.00 USD | 44,140.00 USD | 414,830.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.10` | 5,100,000.00 USD | 5,100,000.00 USD | 584,450.00 USD | 24,690.00 USD | 345,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `717.10` | 2,190,000.00 USD | 2,190,000.00 USD | 337,810.00 USD | 0.00 USD | 404,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.90` | 5,870,000.00 USD | 5,870,000.00 USD | 463,930.00 USD | 41,310.00 USD | 260,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `718.00` | 2,690,000.00 USD | 2,690,000.00 USD | 345,570.00 USD | 51,150.00 USD | 107,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.70` | 6,660,000.00 USD | 6,660,000.00 USD | 582,730.00 USD | 71,870.00 USD | 142,630.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `718.90` | 4,020,000.00 USD | 4,020,000.00 USD | 775,390.00 USD | 69,290.00 USD | 481,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.50` | 7,030,000.00 USD | 7,030,000.00 USD | 60,590.00 USD | 82,030.00 USD | 219,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `719.80` | 6,270,000.00 USD | 6,270,000.00 USD | 183,760.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.30` | 8,240,000.00 USD | 8,240,000.00 USD | 988,460.00 USD | 86,780.00 USD | 134,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 376.82 USD | 3,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `720.70` | 7,040,000.00 USD | 7,040,000.00 USD | 622,340.00 USD | 146,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.10` | 8,790,000.00 USD | 8,790,000.00 USD | 177,520.00 USD | 328,830.00 USD | 50,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,040.00 USD | 36,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `721.60` | 7,410,000.00 USD | 7,410,000.00 USD | 181,600.00 USD | 106,060.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.90` | 9,510,000.00 USD | 9,510,000.00 USD | 145,470.00 USD | 207,490.00 USD | 368,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `722.50` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 131,550.00 USD | 643,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 1,950.00 USD | 38,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `722.70` | 10,250,000.00 USD | 10,250,000.00 USD | 393,920.00 USD | 131,240.00 USD | 207,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `723.40` | 9,330,000.00 USD | 9,330,000.00 USD | 806,150.00 USD | 0.00 USD | 335,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.50` | 11,270,000.00 USD | 11,270,000.00 USD | 446,650.00 USD | 403,140.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 2,170.00 USD | 40,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.30` | 11,760,000.00 USD | 11,760,000.00 USD | 300,180.00 USD | 185,360.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `724.30` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 40,760.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.10` | 12,150,000.00 USD | 12,150,000.00 USD | 223,480.00 USD | 152,860.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 993.93 USD | 41,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.90` | 12,490,000.00 USD | 12,490,000.00 USD | 317,710.00 USD | 0.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `726.10` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 58,160.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 3,710.00 USD | 45,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.70` | 12,830,000.00 USD | 12,830,000.00 USD | 226,170.00 USD | 85,880.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `727.00` | 11,830,000.00 USD | 11,830,000.00 USD | 552,080.00 USD | 0.00 USD | 639,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `727.50` | 13,410,000.00 USD | 13,410,000.00 USD | 537,650.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 200.06 USD | 45,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `727.90` | 12,610,000.00 USD | 12,610,000.00 USD | 575,930.00 USD | 201,080.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `728.30` | 13,780,000.00 USD | 13,780,000.00 USD | 235,780.00 USD | 0.00 USD | 133,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,080.00 USD | 86,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `728.80` | 13,530,000.00 USD | 13,530,000.00 USD | 779,040.00 USD | 145,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.10` | 15,010,000.00 USD | 15,010,000.00 USD | 499,870.00 USD | 317,000.00 USD | 414,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 171,010.00 USD | 257,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `729.70` | 14,730,000.00 USD | 14,730,000.00 USD | 576,440.00 USD | 425,860.00 USD | 191,070.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.90` | 16,060,000.00 USD | 16,060,000.00 USD | 226,750.00 USD | 246,250.00 USD | 572,410.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 22,440.00 USD | 280,190.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `730.60` | 15,420,000.00 USD | 15,420,000.00 USD | 296,730.00 USD | 273,740.00 USD | 119,980.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.70` | 22,050,000.00 USD | 22,050,000.00 USD | 3,220,000.00 USD | 484,450.00 USD | 2,280,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.50` | 23,550,000.00 USD | 23,550,000.00 USD | 738,570.00 USD | 139,290.00 USD | 624,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `731.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 114,370.00 USD | 941,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 2,050.00 USD | 282,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.30` | 26,370,000.00 USD | 26,370,000.00 USD | 1,290,000.00 USD | 113,040.00 USD | 1,410,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `732.40` | 18,320,000.00 USD | 18,320,000.00 USD | 172,790.00 USD | 118,880.00 USD | 1,550,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 140,300.00 USD | 422,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.10` | 28,100,000.00 USD | 28,100,000.00 USD | 927,780.00 USD | 249,610.00 USD | 551,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `733.30` | 19,130,000.00 USD | 19,130,000.00 USD | 91,880.00 USD | 162,870.00 USD | 559,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 12,500.00 USD | 435,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `733.90` | 29,040,000.00 USD | 29,040,000.00 USD | 365,220.00 USD | 226,780.00 USD | 347,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `734.20` | 19,740,000.00 USD | 19,740,000.00 USD | 123,040.00 USD | 0.00 USD | 484,840.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 188,860.00 USD | 623,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.70` | 30,110,000.00 USD | 30,110,000.00 USD | 967,050.00 USD | 52,620.00 USD | 51,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `735.10` | 20,400,000.00 USD | 20,400,000.00 USD | 547,660.00 USD | 73,000.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `735.50` | 31,340,000.00 USD | 31,340,000.00 USD | 401,720.00 USD | 207,980.00 USD | 625,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 37,370.00 USD | 661,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `736.00` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 53,030.00 USD | 158,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.30` | 31,990,000.00 USD | 31,990,000.00 USD | 385,990.00 USD | 70,270.00 USD | 191,130.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 44,080.00 USD | 705,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `736.90` | 21,020,000.00 USD | 21,020,000.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.10` | 32,280,000.00 USD | 32,280,000.00 USD | 156,930.00 USD | 43,110.00 USD | 88,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 7,670.00 USD | 713,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `737.80` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.90` | 32,900,000.00 USD | 32,900,000.00 USD | 399,410.00 USD | 178,930.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 53,020.00 USD | 766,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.70` | 34,030,000.00 USD | 34,030,000.00 USD | 624,880.00 USD | 33,100.00 USD | 472,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `738.70` | 22,170,000.00 USD | 22,170,000.00 USD | 50,860.00 USD | 166,070.00 USD | 703,580.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.50` | 34,710,000.00 USD | 34,710,000.00 USD | 186,290.00 USD | 31,860.00 USD | 461,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 108,310.00 USD | 874,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `739.60` | 23,190,000.00 USD | 23,190,000.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.30` | 34,940,000.00 USD | 34,940,000.00 USD | 92,050.00 USD | 134,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `740.50` | 24,940,000.00 USD | 24,940,000.00 USD | 1,090,000.00 USD | 0.00 USD | 659,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 6,760.00 USD | 881,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `741.10` | 35,540,000.00 USD | 35,540,000.00 USD | 554,740.00 USD | 32,240.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `741.40` | 25,400,000.00 USD | 25,400,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 32,760.00 USD | 913,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `741.90` | 35,840,000.00 USD | 35,840,000.00 USD | 291,160.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `742.30` | 25,910,000.00 USD | 25,910,000.00 USD | 383,790.00 USD | 100,540.00 USD | 21,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 66,150.00 USD | 980,010.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.70` | 35,980,000.00 USD | 35,980,000.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `743.20` | 26,520,000.00 USD | 26,520,000.00 USD | 389,520.00 USD | 0.00 USD | 220,040.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `743.50` | 36,670,000.00 USD | 36,670,000.00 USD | 233,380.00 USD | 21,120.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 49,810.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `744.10` | 27,100,000.00 USD | 27,100,000.00 USD | 160,880.00 USD | 282,830.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `744.30` | 37,760,000.00 USD | 37,760,000.00 USD | 891,770.00 USD | 191,870.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 126,390.00 USD | 1,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `745.00` | 27,260,000.00 USD | 27,260,000.00 USD | 0.00 USD | 155,680.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.10` | 39,430,000.00 USD | 39,430,000.00 USD | 710,280.00 USD | 61,600.00 USD | 897,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 20,430.00 USD | 1,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `745.90` | 39,820,000.00 USD | 39,820,000.00 USD | 196,920.00 USD | 120,210.00 USD | 78,280.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `745.90` | 27,710,000.00 USD | 27,710,000.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 185,960.00 USD | 1,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.70` | 41,560,000.00 USD | 41,560,000.00 USD | 674,650.00 USD | 29,460.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.80` | 28,550,000.00 USD | 28,550,000.00 USD | 324,750.00 USD | 0.00 USD | 513,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.50` | 42,020,000.00 USD | 42,020,000.00 USD | 300,360.00 USD | 74,380.00 USD | 80,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `747.70` | 28,990,000.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 435,810.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `748.30` | 42,620,000.00 USD | 42,620,000.00 USD | 407,940.00 USD | 84,260.00 USD | 108,850.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 4,270.00 USD | 1,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `748.60` | 29,320,000.00 USD | 29,320,000.00 USD | 337,680.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.10` | 43,020,000.00 USD | 43,020,000.00 USD | 401,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `749.50` | 29,740,000.00 USD | 29,740,000.00 USD | 356,770.00 USD | 61,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 67,670.00 USD | 1,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `749.90` | 43,270,000.00 USD | 43,270,000.00 USD | 251,210.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `750.40` | 29,830,000.00 USD | 29,830,000.00 USD | 86,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 574,740.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.70` | 43,390,000.00 USD | 43,390,000.00 USD | 121,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `751.30` | 30,000,000.00 USD | 30,000,000.00 USD | 175,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `751.50` | 43,620,000.00 USD | 43,620,000.00 USD | 97,960.00 USD | 25,010.00 USD | 98,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 21,390.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.30` | 44,150,000.00 USD | 44,150,000.00 USD | 93,830.00 USD | 0.00 USD | 441,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 48,630.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.10` | 44,790,000.00 USD | 44,790,000.00 USD | 393,720.00 USD | 0.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `753.10` | 30,450,000.00 USD | 30,450,000.00 USD | 96,700.00 USD | 0.00 USD | 351,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `753.50` | 4,660.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `753.90` | 45,250,000.00 USD | 45,250,000.00 USD | 362,250.00 USD | 54,420.00 USD | 40,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `754.00` | 30,880,000.00 USD | 30,880,000.00 USD | 310,190.00 USD | 83,030.00 USD | 33,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 860,170.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.70` | 45,530,000.00 USD | 45,530,000.00 USD | 159,380.00 USD | 98,410.00 USD | 16,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `754.90` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.50` | 46,040,000.00 USD | 46,040,000.00 USD | 396,840.00 USD | 96,170.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 11,710.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.80` | 31,060,000.00 USD | 31,060,000.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.30` | 46,120,000.00 USD | 46,120,000.00 USD | 13,050.00 USD | 24,970.00 USD | 46,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.70` | 31,110,000.00 USD | 31,110,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.10` | 46,350,000.00 USD | 46,350,000.00 USD | 164,820.00 USD | 33,270.00 USD | 30,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 2,010.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.60` | 31,220,000.00 USD | 31,220,000.00 USD | 0.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.90` | 46,770,000.00 USD | 46,770,000.00 USD | 378,680.00 USD | 26,940.00 USD | 18,080.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.50` | 33,150,000.00 USD | 33,150,000.00 USD | 1,660,000.00 USD | 0.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,980.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `758.70` | 47,330,000.00 USD | 47,330,000.00 USD | 144,220.00 USD | 142,320.00 USD | 273,090.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `759.40` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 55,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.50` | 47,760,000.00 USD | 47,760,000.00 USD | 415,540.00 USD | 2,460.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 704.82 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.30` | 48,070,000.00 USD | 48,070,000.00 USD | 231,490.00 USD | 55,920.00 USD | 20,250.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.30` | 33,700,000.00 USD | 33,700,000.00 USD | 420,720.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 6,020.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.10` | 48,580,000.00 USD | 48,580,000.00 USD | 254,000.00 USD | 15,330.00 USD | 243,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.20` | 33,990,000.00 USD | 33,990,000.00 USD | 164,720.00 USD | 30,310.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 367.04 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `761.90` | 49,230,000.00 USD | 49,230,000.00 USD | 575,650.00 USD | 35,860.00 USD | 40,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.10` | 34,660,000.00 USD | 34,660,000.00 USD | 35,980.00 USD | 322,010.00 USD | 314,310.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 8,050.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.70` | 49,980,000.00 USD | 49,980,000.00 USD | 413,500.00 USD | 19,550.00 USD | 317,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.00` | 37,570,000.00 USD | 37,570,000.00 USD | 2,300,000.00 USD | 271,300.00 USD | 333,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `763.50` | 50,230,000.00 USD | 50,230,000.00 USD | 112,700.00 USD | 90,910.00 USD | 43,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 595,810.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `763.90` | 39,460,000.00 USD | 39,460,000.00 USD | 1,240,000.00 USD | 295,990.00 USD | 353,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.30` | 50,680,000.00 USD | 50,680,000.00 USD | 401,340.00 USD | 9,260.00 USD | 40,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.80` | 41,290,000.00 USD | 41,290,000.00 USD | 1,250,000.00 USD | 260,460.00 USD | 307,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.10` | 50,970,000.00 USD | 50,970,000.00 USD | 123,170.00 USD | 127,420.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `765.50` | 785.40 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `765.70` | 43,880,000.00 USD | 43,880,000.00 USD | 2,000,000.00 USD | 134,320.00 USD | 455,200.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.90` | 51,330,000.00 USD | 51,330,000.00 USD | 322,090.00 USD | 5,340.00 USD | 41,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.60` | 48,720,000.00 USD | 48,720,000.00 USD | 3,720,000.00 USD | 374,820.00 USD | 742,360.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.70` | 51,800,000.00 USD | 51,800,000.00 USD | 325,730.00 USD | 47,980.00 USD | 91,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.50` | 52,410,000.00 USD | 52,410,000.00 USD | 524,440.00 USD | 0.00 USD | 90,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.50` | 51,300,000.00 USD | 51,300,000.00 USD | 1,920,000.00 USD | 171,000.00 USD | 487,470.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 74,200.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.30` | 52,680,000.00 USD | 52,680,000.00 USD | 235,790.00 USD | 15,950.00 USD | 12,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.40` | 54,420,000.00 USD | 54,420,000.00 USD | 2,660,000.00 USD | 95,830.00 USD | 365,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 300.48 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `769.10` | 52,890,000.00 USD | 52,890,000.00 USD | 154,200.00 USD | 35,430.00 USD | 21,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.30` | 55,940,000.00 USD | 55,940,000.00 USD | 718,800.00 USD | 209,770.00 USD | 589,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.90` | 53,050,000.00 USD | 53,050,000.00 USD | 131,210.00 USD | 29,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.20` | 58,490,000.00 USD | 58,490,000.00 USD | 2,030,000.00 USD | 213,870.00 USD | 311,860.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 661.86 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.70` | 53,520,000.00 USD | 53,520,000.00 USD | 85,240.00 USD | 31,140.00 USD | 352,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.10` | 60,150,000.00 USD | 60,150,000.00 USD | 1,230,000.00 USD | 293,960.00 USD | 134,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `771.50` | 54,390,000.00 USD | 54,390,000.00 USD | 58,210.00 USD | 132,690.00 USD | 675,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 395,010.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.00` | 62,710,000.00 USD | 62,710,000.00 USD | 1,640,000.00 USD | 386,400.00 USD | 526,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.30` | 54,700,000.00 USD | 54,700,000.00 USD | 224,770.00 USD | 34,100.00 USD | 54,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 2,450.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.90` | 65,520,000.00 USD | 65,520,000.00 USD | 2,120,000.00 USD | 316,840.00 USD | 375,440.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.10` | 55,500,000.00 USD | 55,500,000.00 USD | 634,740.00 USD | 71,650.00 USD | 97,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 1,480.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.80` | 67,270,000.00 USD | 67,270,000.00 USD | 1,190,000.00 USD | 270,430.00 USD | 282,970.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.90` | 55,730,000.00 USD | 55,730,000.00 USD | 144,620.00 USD | 26,310.00 USD | 53,940.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.70` | 56,180,000.00 USD | 56,180,000.00 USD | 315,250.00 USD | 48,490.00 USD | 91,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.70` | 69,230,000.00 USD | 69,230,000.00 USD | 1,080,000.00 USD | 416,900.00 USD | 470,250.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.50` | 56,360,000.00 USD | 56,360,000.00 USD | 162,620.00 USD | 0.00 USD | 9,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 544.40 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `775.60` | 71,400,000.00 USD | 71,400,000.00 USD | 1,550,000.00 USD | 386,090.00 USD | 231,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `776.50` | 73,200,000.00 USD | 73,200,000.00 USD | 1,410,000.00 USD | 95,320.00 USD | 293,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 89,520.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `777.40` | 73,940,000.00 USD | 73,940,000.00 USD | 571,520.00 USD | 76,980.00 USD | 94,890.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `778.30` | 75,530,000.00 USD | 75,530,000.00 USD | 1,290,000.00 USD | 160,280.00 USD | 135,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 8,100.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `779.20` | 76,740,000.00 USD | 76,740,000.00 USD | 971,150.00 USD | 107,630.00 USD | 122,470.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.10` | 78,140,000.00 USD | 78,140,000.00 USD | 1,060,000.00 USD | 123,080.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 4,150.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.00` | 79,160,000.00 USD | 79,160,000.00 USD | 750,650.00 USD | 90,990.00 USD | 182,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 4,320.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.90` | 81,380,000.00 USD | 81,380,000.00 USD | 1,770,000.00 USD | 87,670.00 USD | 361,100.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.80` | 83,540,000.00 USD | 83,540,000.00 USD | 1,700,000.00 USD | 36,140.00 USD | 427,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.70` | 84,110,000.00 USD | 84,110,000.00 USD | 508,850.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 130.23 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.60` | 84,480,000.00 USD | 84,480,000.00 USD | 243,470.00 USD | 68,480.00 USD | 53,990.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `785.50` | 85,470,000.00 USD | 85,470,000.00 USD | 850,840.00 USD | 54,140.00 USD | 87,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 1,750.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `786.40` | 86,150,000.00 USD | 86,150,000.00 USD | 623,380.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,780.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `787.30` | 86,740,000.00 USD | 86,740,000.00 USD | 483,900.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.20` | 87,040,000.00 USD | 87,040,000.00 USD | 120,880.00 USD | 93,190.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `789.10` | 87,980,000.00 USD | 87,980,000.00 USD | 754,040.00 USD | 74,540.00 USD | 113,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.00` | 88,520,000.00 USD | 88,520,000.00 USD | 280,800.00 USD | 99,920.00 USD | 160,030.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 247.43 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.90` | 89,350,000.00 USD | 89,350,000.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.80` | 90,250,000.00 USD | 90,250,000.00 USD | 780,710.00 USD | 16,830.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.70` | 90,520,000.00 USD | 90,520,000.00 USD | 258,640.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 2,660.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.60` | 90,660,000.00 USD | 90,660,000.00 USD | 143,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.50` | 90,870,000.00 USD | 90,870,000.00 USD | 194,400.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.40` | 91,030,000.00 USD | 91,030,000.00 USD | 131,460.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.30` | 91,210,000.00 USD | 91,210,000.00 USD | 34,010.00 USD | 0.00 USD | 140,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 1,240.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,090.00 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `799.50` | 438.13 USD | 4,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `800.50` | 28,250.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `801.50` | 709,870.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `802.50` | 72,430.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `803.50` | 5,720.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `804.50` | 181.01 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,600.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `807.50` | 738.06 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `808.50` | 13,210.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `811.50` | 434.15 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `815.50` | 8,150.00 USD | 5,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `818.50` | 7,720.00 USD | 5,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `822.50` | 84,720.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `825.50` | 528,640.00 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `826.50` | 426.47 USD | 5,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `828.50` | 5,880.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 239.24 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 3,570.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `840.50` | 679.96 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 4,410.00 USD | 5,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 12,050.00 USD | 5,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `844.50` | 34,100.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `847.50` | 289.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 393.78 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `852.50` | 5,020.00 USD | 5,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 2,110.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `857.50` | 1,480.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `862.50` | 526,120.00 USD | 6,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 289,650.00 USD | 6,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 326.69 USD | 6,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 702,210.00 USD | 7,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 4,540.00 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 7,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `884.50` | 14,140.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,580.00 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 215.42 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `890.50` | 380.24 USD | 7,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 3,950.00 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 7,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 7,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 223,880.00 USD | 7,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 89,750.00 USD | 7,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 153,370.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 5,400.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `903.50` | 5,470.00 USD | 8,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 158,550.00 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `905.50` | 107.75 USD | 8,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 188,080.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 2,420.00 USD | 8,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 37,210.00 USD | 8,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 34,630.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 121.23 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `912.50` | 1,820.00 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `914.50` | 389.58 USD | 8,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `917.50` | 22,940.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `923.50` | 30,360.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `924.50` | 649.00 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `930.50` | 172.14 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 956.93 USD | 8,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 4,760.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `936.50` | 121,750.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `940.50` | 7,750.00 USD | 8,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 207,790.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `949.50` | 2,820.00 USD | 8,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `956.50` | 18,930.00 USD | 8,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `957.50` | 19,600.00 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 204.16 USD | 8,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 3,210.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `965.50` | 35,070.00 USD | 8,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `968.50` | 1,940.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `976.50` | 59,960.00 USD | 8,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `977.50` | 14,210.00 USD | 9,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 1,100.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `987.50` | 69,740.00 USD | 9,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `988.50` | 288,210.00 USD | 9,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `989.50` | 98,950.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,320.00 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 791.82 USD | 9,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 313.58 USD | 9,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 989.52 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 9,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 46,370.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1002.50` | 161.40 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 677.36 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 9,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 29,110.00 USD | 9,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,370.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1011.50` | 14,570.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 238.71 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1030.50` | 718,890.00 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 497.66 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 10,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1059.50` | 66,220.00 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1062.50` | 635.38 USD | 10,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1063.50` | 18,960.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 3,510.00 USD | 10,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1066.50` | 693,230.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 2,940.00 USD | 11,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1074.50` | 120.34 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1077.50` | 766.10 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 11,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 16,230.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1089.50` | 1,570.00 USD | 11,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1090.50` | 74,430.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 120,790.00 USD | 11,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1095.50` | 70,020.00 USD | 11,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1100.50` | 507.33 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1114.50` | 2,230.00 USD | 11,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1116.50` | 116,120.00 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 351.21 USD | 11,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1123.50` | 60,740.00 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1130.50` | 151.49 USD | 11,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,250.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1138.50` | 1,520.00 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1146.50` | 119.24 USD | 12,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1151.50` | 11,690.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1152.50` | 4,940.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1154.50` | 8,180.00 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1162.50` | 155.78 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1175.50` | 20,410.00 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1176.50` | 356.48 USD | 12,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1179.50` | 82,770.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1184.50` | 561.45 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1190.50` | 167.86 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1203.50` | 118,860.00 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1209.50` | 30,220.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1218.50` | 43,870.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1223.50` | 606,150.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 4,750.00 USD | 13,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1233.50` | 59,590.00 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1245.50` | 102.13 USD | 13,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1246.50` | 6,750.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1247.50` | 2,660.00 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 300.36 USD | 13,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1253.50` | 24,340.00 USD | 13,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1259.50` | 113,360.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1266.50` | 901.75 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1272.50` | 5,080.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 25,570.00 USD | 13,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1286.50` | 61,910.00 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1288.50` | 349.18 USD | 13,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1289.50` | 21,380.00 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 13,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1298.50` | 110,770.00 USD | 13,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1301.50` | 4,020.00 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1303.50` | 100.37 USD | 13,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1306.50` | 1,850,000.00 USD | 15,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1309.50` | 166,150.00 USD | 15,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1311.50` | 18,450.00 USD | 15,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1316.50` | 30,280.00 USD | 15,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 15,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1322.50` | 208.96 USD | 15,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1325.50` | 2,650.00 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 242.93 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 184.66 USD | 15,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1329.50` | 13,220.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 25,340.00 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 494.28 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1347.50` | 233.12 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1349.50` | 4,220.00 USD | 15,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1352.50` | 87,910.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1354.50` | 3,850.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1359.50` | 121.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1363.50` | 6,820.00 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1373.50` | 4,120.00 USD | 15,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1384.50` | 69,220.00 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1385.50` | 508.48 USD | 15,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1389.50` | 4,800.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1399.50` | 3,980.00 USD | 15,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1403.50` | 252,630.00 USD | 16,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 16,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `140.50` | 5,640,000.00 USD | 0.00 USD | 850.02 USD | `-80.00%` | `6,050,000,000.00` |
| `Live` | `Long` | `141.50` | 5,640,000.00 USD | 0.00 USD | 5,520.00 USD | `-79.86%` | `38,980,000,000.00` |
| `Live` | `Long` | `143.50` | 5,640,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.58%` | `20,000,000,000.00` |
| `Live` | `Long` | `145.50` | 5,630,000.00 USD | 0.00 USD | 2,040.00 USD | `-79.29%` | `14,000,000,000.00` |
| `Live` | `Long` | `154.50` | 5,630,000.00 USD | 0.00 USD | 4,370.00 USD | `-78.01%` | `28,261,000,000.00` |
| `Live` | `Long` | `166.50` | 5,630,000.00 USD | 0.00 USD | 99,900.00 USD | `-76.30%` | `600,000,000,000.00` |
| `Live` | `Long` | `174.50` | 5,530,000.00 USD | 0.00 USD | 315.50 USD | `-75.16%` | `1,808,000,000.00` |
| `Live` | `Long` | `176.50` | 5,530,000.00 USD | 0.00 USD | 5,980.00 USD | `-74.88%` | `33,907,000,000.00` |
| `Live` | `Long` | `178.50` | 5,520,000.00 USD | 0.00 USD | 239.90 USD | `-74.60%` | `1,344,000,000.00` |
| `Live` | `Long` | `180.50` | 5,520,000.00 USD | 0.00 USD | 696.73 USD | `-74.31%` | `3,860,000,000.00` |
| `Live` | `Long` | `182.50` | 5,520,000.00 USD | 0.00 USD | 519.58 USD | `-74.03%` | `2,847,000,000.00` |
| `Live` | `Long` | `183.50` | 5,520,000.00 USD | 0.00 USD | 510,100.00 USD | `-73.88%` | `2,779,816,000,000.00` |
| `Live` | `Long` | `196.50` | 5,010,000.00 USD | 0.00 USD | 135.00 USD | `-72.03%` | `687,000,000.00` |
| `Live` | `Long` | `203.50` | 5,010,000.00 USD | 0.00 USD | 309,350.00 USD | `-71.04%` | `1,520,143,000,000.00` |
| `Live` | `Long` | `210.50` | 4,700,000.00 USD | 0.00 USD | 258.28 USD | `-70.04%` | `1,227,000,000.00` |
| `Live` | `Long` | `212.50` | 4,700,000.00 USD | 0.00 USD | 21,250.00 USD | `-69.76%` | `100,000,000,000.00` |
| `Live` | `Long` | `218.50` | 4,680,000.00 USD | 0.00 USD | 190.31 USD | `-68.90%` | `871,000,000.00` |
| `Live` | `Long` | `221.50` | 4,680,000.00 USD | 0.00 USD | 272.22 USD | `-68.48%` | `1,229,000,000.00` |
| `Live` | `Long` | `236.50` | 4,680,000.00 USD | 0.00 USD | 359.72 USD | `-66.34%` | `1,521,000,000.00` |
| `Live` | `Long` | `243.50` | 4,680,000.00 USD | 0.00 USD | 16,910.00 USD | `-65.34%` | `69,447,000,000.00` |
| `Live` | `Long` | `249.50` | 4,660,000.00 USD | 0.00 USD | 1,370.00 USD | `-64.49%` | `5,489,000,000.00` |
| `Live` | `Long` | `258.50` | 4,660,000.00 USD | 0.00 USD | 258,500.00 USD | `-63.21%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `259.50` | 4,400,000.00 USD | 0.00 USD | 1,370.00 USD | `-63.07%` | `5,281,000,000.00` |
| `Live` | `Long` | `268.50` | 4,400,000.00 USD | 0.00 USD | 21,280.00 USD | `-61.79%` | `79,269,000,000.00` |
| `Live` | `Long` | `301.50` | 4,380,000.00 USD | 0.00 USD | 5,360.00 USD | `-57.09%` | `17,770,000,000.00` |
| `Live` | `Long` | `311.50` | 4,370,000.00 USD | 0.00 USD | 154,780.00 USD | `-55.67%` | `496,876,000,000.00` |
| `Live` | `Long` | `312.50` | 4,220,000.00 USD | 0.00 USD | 500.00 USD | `-55.52%` | `1,600,000,000.00` |
| `Live` | `Long` | `325.50` | 4,220,000.00 USD | 0.00 USD | 1,020.00 USD | `-53.67%` | `3,147,000,000.00` |
| `Live` | `Long` | `326.50` | 4,220,000.00 USD | 0.00 USD | 500.85 USD | `-53.53%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,220,000.00 USD | 0.00 USD | 314.07 USD | `-53.39%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,220,000.00 USD | 0.00 USD | 376.06 USD | `-52.68%` | `1,131,000,000.00` |
| `Live` | `Long` | `342.50` | 4,220,000.00 USD | 0.00 USD | 650.75 USD | `-51.25%` | `1,900,000,000.00` |
| `Live` | `Long` | `346.50` | 4,210,000.00 USD | 0.00 USD | 122.31 USD | `-50.69%` | `353,000,000.00` |
| `Live` | `Long` | `347.50` | 4,210,000.00 USD | 0.00 USD | 961.53 USD | `-50.54%` | `2,767,000,000.00` |
| `Live` | `Long` | `355.50` | 4,210,000.00 USD | 0.00 USD | 303.60 USD | `-49.40%` | `854,000,000.00` |
| `Live` | `Long` | `359.50` | 4,210,000.00 USD | 0.00 USD | 212.10 USD | `-48.84%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,210,000.00 USD | 0.00 USD | 1,980.00 USD | `-48.27%` | `5,441,000,000.00` |
| `Live` | `Long` | `365.50` | 4,210,000.00 USD | 0.00 USD | 548.25 USD | `-47.98%` | `1,500,000,000.00` |
| `Live` | `Long` | `371.50` | 4,210,000.00 USD | 0.00 USD | 10,630.00 USD | `-47.13%` | `28,611,000,000.00` |
| `Live` | `Long` | `373.50` | 4,200,000.00 USD | 0.00 USD | 73,190.00 USD | `-46.84%` | `195,958,000,000.00` |
| `Live` | `Long` | `376.50` | 4,130,000.00 USD | 0.00 USD | 11,540.00 USD | `-46.42%` | `30,661,000,000.00` |
| `Live` | `Long` | `377.50` | 4,120,000.00 USD | 0.00 USD | 950.92 USD | `-46.27%` | `2,519,000,000.00` |
| `Live` | `Long` | `378.50` | 4,110,000.00 USD | 0.00 USD | 17,680.00 USD | `-46.13%` | `46,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,100,000.00 USD | 0.00 USD | 1,910.00 USD | `-45.70%` | `5,000,000,000.00` |
| `Live` | `Long` | `382.50` | 4,090,000.00 USD | 0.00 USD | 10,870.00 USD | `-45.56%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 4,080,000.00 USD | 0.00 USD | 2,510.00 USD | `-45.28%` | `6,536,000,000.00` |
| `Live` | `Long` | `385.50` | 4,080,000.00 USD | 0.00 USD | 341.17 USD | `-45.13%` | `885,000,000.00` |
| `Live` | `Long` | `386.50` | 4,080,000.00 USD | 0.00 USD | 531.44 USD | `-44.99%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 4,080,000.00 USD | 0.00 USD | 392.54 USD | `-44.85%` | `1,013,000,000.00` |
| `Live` | `Long` | `390.50` | 4,080,000.00 USD | 0.00 USD | 3,370.00 USD | `-44.42%` | `8,638,000,000.00` |
| `Live` | `Long` | `392.50` | 4,080,000.00 USD | 0.00 USD | 103.62 USD | `-44.14%` | `264,000,000.00` |
| `Live` | `Long` | `393.50` | 4,080,000.00 USD | 0.00 USD | 1,100.00 USD | `-44.00%` | `2,792,000,000.00` |
| `Live` | `Long` | `394.50` | 4,080,000.00 USD | 0.00 USD | 1,950.00 USD | `-43.85%` | `4,947,000,000.00` |
| `Live` | `Long` | `395.50` | 4,070,000.00 USD | 0.00 USD | 158.20 USD | `-43.71%` | `400,000,000.00` |
| `Live` | `Long` | `396.50` | 4,070,000.00 USD | 0.00 USD | 317.20 USD | `-43.57%` | `800,000,000.00` |
| `Live` | `Long` | `397.50` | 4,070,000.00 USD | 0.00 USD | 522.32 USD | `-43.43%` | `1,314,000,000.00` |
| `Live` | `Long` | `398.50` | 4,070,000.00 USD | 0.00 USD | 1,690.00 USD | `-43.28%` | `4,250,000,000.00` |
| `Live` | `Long` | `399.50` | 4,070,000.00 USD | 0.00 USD | 8,190.00 USD | `-43.14%` | `20,511,000,000.00` |
| `Live` | `Long` | `400.50` | 4,060,000.00 USD | 0.00 USD | 619.57 USD | `-43.00%` | `1,547,000,000.00` |
| `Live` | `Long` | `403.50` | 4,060,000.00 USD | 0.00 USD | 102.09 USD | `-42.57%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 4,060,000.00 USD | 0.00 USD | 613.02 USD | `-41.72%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 4,060,000.00 USD | 0.00 USD | 105.91 USD | `-41.58%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 4,060,000.00 USD | 0.00 USD | 3,490.00 USD | `-41.29%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 4,060,000.00 USD | 0.00 USD | 11,690.00 USD | `-41.15%` | `28,268,000,000.00` |
| `Live` | `Long` | `414.50` | 4,050,000.00 USD | 0.00 USD | 2,700.00 USD | `-41.01%` | `6,519,000,000.00` |
| `Live` | `Long` | `416.50` | 4,040,000.00 USD | 0.00 USD | 2,350.00 USD | `-40.72%` | `5,644,000,000.00` |
| `Live` | `Long` | `417.50` | 4,040,000.00 USD | 0.00 USD | 5,100.00 USD | `-40.58%` | `12,208,000,000.00` |
| `Live` | `Long` | `418.50` | 4,040,000.00 USD | 0.00 USD | 60,370.00 USD | `-40.44%` | `144,245,000,000.00` |
| `Live` | `Long` | `419.50` | 3,980,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.30%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 3,970,000.00 USD | 0.00 USD | 2,320.00 USD | `-40.01%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 3,970,000.00 USD | 0.00 USD | 1,440.00 USD | `-39.87%` | `3,419,000,000.00` |
| `Live` | `Long` | `424.50` | 3,970,000.00 USD | 0.00 USD | 4,250.00 USD | `-39.58%` | `10,000,000,000.00` |
| `Live` | `Long` | `429.50` | 3,960,000.00 USD | 0.00 USD | 846.12 USD | `-38.87%` | `1,970,000,000.00` |
| `Live` | `Long` | `430.50` | 3,960,000.00 USD | 0.00 USD | 616.48 USD | `-38.73%` | `1,432,000,000.00` |
| `Live` | `Long` | `432.50` | 3,960,000.00 USD | 0.00 USD | 3,370.00 USD | `-38.45%` | `7,799,000,000.00` |
| `Live` | `Long` | `436.50` | 3,960,000.00 USD | 0.00 USD | 133.13 USD | `-37.88%` | `305,000,000.00` |
| `Live` | `Long` | `438.50` | 3,960,000.00 USD | 0.00 USD | 1,980.00 USD | `-37.59%` | `4,517,000,000.00` |
| `Live` | `Long` | `447.50` | 3,960,000.00 USD | 0.00 USD | 1,680.00 USD | `-36.31%` | `3,759,000,000.00` |
| `Live` | `Long` | `448.50` | 3,960,000.00 USD | 0.00 USD | 3,350.00 USD | `-36.17%` | `7,470,000,000.00` |
| `Live` | `Long` | `451.50` | 3,950,000.00 USD | 0.00 USD | 8,890.00 USD | `-35.74%` | `19,691,000,000.00` |
| `Live` | `Long` | `456.50` | 3,940,000.00 USD | 0.00 USD | 4,730.00 USD | `-35.03%` | `10,359,000,000.00` |
| `Live` | `Long` | `464.50` | 3,940,000.00 USD | 0.00 USD | 464.50 USD | `-33.89%` | `1,000,000,000.00` |
| `Live` | `Long` | `469.50` | 3,940,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.18%` | `9,301,000,000.00` |
| `Live` | `Long` | `475.50` | 3,930,000.00 USD | 0.00 USD | 5,320.00 USD | `-32.33%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,930,000.00 USD | 0.00 USD | 2,400.00 USD | `-31.47%` | `4,989,000,000.00` |
| `Live` | `Long` | `483.50` | 3,930,000.00 USD | 0.00 USD | 483.50 USD | `-31.19%` | `1,000,000,000.00` |
| `Live` | `Long` | `484.50` | 3,930,000.00 USD | 0.00 USD | 5,240.00 USD | `-31.04%` | `10,811,000,000.00` |
| `Live` | `Long` | `486.50` | 3,920,000.00 USD | 0.00 USD | 207.25 USD | `-30.76%` | `426,000,000.00` |
| `Live` | `Long` | `487.50` | 3,920,000.00 USD | 0.00 USD | 256.91 USD | `-30.62%` | `527,000,000.00` |
| `Live` | `Long` | `488.50` | 3,920,000.00 USD | 0.00 USD | 2,300.00 USD | `-30.48%` | `4,712,000,000.00` |
| `Live` | `Long` | `492.50` | 3,920,000.00 USD | 0.00 USD | 140.36 USD | `-29.91%` | `285,000,000.00` |
| `Live` | `Long` | `493.50` | 3,920,000.00 USD | 0.00 USD | 2,270.00 USD | `-29.76%` | `4,598,000,000.00` |
| `Live` | `Long` | `498.50` | 3,920,000.00 USD | 0.00 USD | 11,260.00 USD | `-29.05%` | `22,583,000,000.00` |
| `Live` | `Long` | `499.50` | 3,900,000.00 USD | 0.00 USD | 5,150.00 USD | `-28.91%` | `10,306,000,000.00` |
| `Live` | `Long` | `500.50` | 3,900,000.00 USD | 0.00 USD | 186.69 USD | `-28.77%` | `373,000,000.00` |
| `Live` | `Long` | `501.50` | 3,900,000.00 USD | 0.00 USD | 14,130.00 USD | `-28.63%` | `28,185,000,000.00` |
| `Live` | `Long` | `502.50` | 3,890,000.00 USD | 0.00 USD | 109.04 USD | `-28.48%` | `217,000,000.00` |
| `Live` | `Long` | `504.50` | 3,880,000.00 USD | 0.00 USD | 3,500.00 USD | `-28.20%` | `6,944,000,000.00` |
| `Live` | `Long` | `505.50` | 3,880,000.00 USD | 0.00 USD | 6,630.00 USD | `-28.06%` | `13,121,000,000.00` |
| `Live` | `Long` | `507.50` | 3,870,000.00 USD | 0.00 USD | 62,650.00 USD | `-27.77%` | `123,441,000,000.00` |
| `Live` | `Long` | `508.50` | 3,810,000.00 USD | 0.00 USD | 2,750.00 USD | `-27.63%` | `5,411,000,000.00` |
| `Live` | `Long` | `509.50` | 3,810,000.00 USD | 0.00 USD | 830.99 USD | `-27.49%` | `1,631,000,000.00` |
| `Live` | `Long` | `510.50` | 3,810,000.00 USD | 0.00 USD | 4,080.00 USD | `-27.34%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,800,000.00 USD | 0.00 USD | 5,180.00 USD | `-27.20%` | `10,118,000,000.00` |
| `Live` | `Long` | `513.50` | 3,800,000.00 USD | 0.00 USD | 2,520.00 USD | `-26.92%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,800,000.00 USD | 0.00 USD | 317.45 USD | `-26.78%` | `617,000,000.00` |
| `Live` | `Long` | `515.50` | 3,800,000.00 USD | 0.00 USD | 6,470.00 USD | `-26.63%` | `12,554,000,000.00` |
| `Live` | `Long` | `517.50` | 3,790,000.00 USD | 0.00 USD | 22,650.00 USD | `-26.35%` | `43,765,000,000.00` |
| `Live` | `Long` | `518.50` | 3,770,000.00 USD | 0.00 USD | 41,970.00 USD | `-26.21%` | `80,941,000,000.00` |
| `Live` | `Long` | `519.50` | 3,730,000.00 USD | 0.00 USD | 703.92 USD | `-26.06%` | `1,355,000,000.00` |
| `Live` | `Long` | `520.50` | 3,720,000.00 USD | 0.00 USD | 662.60 USD | `-25.92%` | `1,273,000,000.00` |
| `Live` | `Long` | `521.50` | 3,720,000.00 USD | 0.00 USD | 178,590.00 USD | `-25.78%` | `342,446,000,000.00` |
| `Live` | `Long` | `522.50` | 3,550,000.00 USD | 0.00 USD | 2,090.00 USD | `-25.64%` | `3,993,000,000.00` |
| `Live` | `Long` | `523.50` | 3,540,000.00 USD | 0.00 USD | 53,820.00 USD | `-25.49%` | `102,811,000,000.00` |
| `Live` | `Long` | `524.50` | 3,490,000.00 USD | 0.00 USD | 833.43 USD | `-25.35%` | `1,589,000,000.00` |
| `Live` | `Long` | `525.50` | 3,490,000.00 USD | 0.00 USD | 289.03 USD | `-25.21%` | `550,000,000.00` |
| `Live` | `Long` | `526.50` | 3,490,000.00 USD | 0.00 USD | 1,410.00 USD | `-25.07%` | `2,684,000,000.00` |
| `Live` | `Long` | `529.50` | 3,490,000.00 USD | 0.00 USD | 136,080.00 USD | `-24.64%` | `256,989,000,000.00` |
| `Live` | `Long` | `530.50` | 3,350,000.00 USD | 0.00 USD | 1,350.00 USD | `-24.50%` | `2,537,000,000.00` |
| `Live` | `Long` | `531.50` | 3,350,000.00 USD | 0.00 USD | 208.88 USD | `-24.36%` | `393,000,000.00` |
| `Live` | `Long` | `532.50` | 3,350,000.00 USD | 0.00 USD | 422.81 USD | `-24.21%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,350,000.00 USD | 0.00 USD | 555.35 USD | `-23.93%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,350,000.00 USD | 0.00 USD | 100.14 USD | `-23.79%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 3,350,000.00 USD | 0.00 USD | 490.94 USD | `-23.22%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,350,000.00 USD | 0.00 USD | 471.32 USD | `-23.07%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,350,000.00 USD | 0.00 USD | 2,680.00 USD | `-22.65%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,340,000.00 USD | 0.00 USD | 211,300.00 USD | `-22.51%` | `388,057,000,000.00` |
| `Live` | `Long` | `545.50` | 3,130,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.36%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,130,000.00 USD | 0.00 USD | 530.11 USD | `-22.22%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,130,000.00 USD | 0.00 USD | 1,980.00 USD | `-21.94%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 3,130,000.00 USD | 0.00 USD | 1,370.00 USD | `-21.79%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,130,000.00 USD | 0.00 USD | 633.63 USD | `-21.65%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,130,000.00 USD | 0.00 USD | 1,250.00 USD | `-21.51%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 3,130,000.00 USD | 0.00 USD | 12,560.00 USD | `-21.37%` | `22,739,000,000.00` |
| `Live` | `Long` | `553.50` | 3,110,000.00 USD | 0.00 USD | 2,740.00 USD | `-21.22%` | `4,955,000,000.00` |
| `Live` | `Long` | `555.50` | 3,110,000.00 USD | 0.00 USD | 82,810.00 USD | `-20.94%` | `149,080,000,000.00` |
| `Live` | `Long` | `556.50` | 3,030,000.00 USD | 0.00 USD | 5,670.00 USD | `-20.80%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 3,020,000.00 USD | 0.00 USD | 791.65 USD | `-20.66%` | `1,420,000,000.00` |
| `Live` | `Long` | `560.50` | 3,020,000.00 USD | 0.00 USD | 984.80 USD | `-20.23%` | `1,757,000,000.00` |
| `Live` | `Long` | `562.50` | 3,020,000.00 USD | 0.00 USD | 1,510.00 USD | `-19.94%` | `2,682,000,000.00` |
| `Live` | `Long` | `568.50` | 3,020,000.00 USD | 0.00 USD | 143.83 USD | `-19.09%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 3,020,000.00 USD | 0.00 USD | 750,370.00 USD | `-18.66%` | `1,312,975,000,000.00` |
| `Live` | `Long` | `573.50` | 2,270,000.00 USD | 0.00 USD | 458.80 USD | `-18.38%` | `800,000,000.00` |
| `Live` | `Long` | `574.50` | 2,270,000.00 USD | 0.00 USD | 323.44 USD | `-18.24%` | `563,000,000.00` |
| `Live` | `Long` | `575.50` | 2,270,000.00 USD | 0.00 USD | 1,020.00 USD | `-18.09%` | `1,765,000,000.00` |
| `Live` | `Long` | `576.50` | 2,270,000.00 USD | 0.00 USD | 2,690.00 USD | `-17.95%` | `4,674,000,000.00` |
| `Live` | `Long` | `577.50` | 2,260,000.00 USD | 0.00 USD | 5,780.00 USD | `-17.81%` | `10,000,000,000.00` |
| `Live` | `Long` | `578.50` | 2,260,000.00 USD | 0.00 USD | 1,230.00 USD | `-17.67%` | `2,134,000,000.00` |
| `Live` | `Long` | `580.50` | 2,260,000.00 USD | 0.00 USD | 35,850.00 USD | `-17.38%` | `61,765,000,000.00` |
| `Live` | `Long` | `582.50` | 2,220,000.00 USD | 0.00 USD | 165,950.00 USD | `-17.10%` | `284,885,000,000.00` |
| `Live` | `Long` | `583.50` | 2,060,000.00 USD | 0.00 USD | 3,060.00 USD | `-16.95%` | `5,239,000,000.00` |
| `Live` | `Long` | `585.50` | 2,050,000.00 USD | 0.00 USD | 210.19 USD | `-16.67%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,050,000.00 USD | 0.00 USD | 2,360.00 USD | `-16.53%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,050,000.00 USD | 0.00 USD | 5,240.00 USD | `-16.39%` | `8,916,000,000.00` |
| `Live` | `Long` | `588.50` | 2,040,000.00 USD | 0.00 USD | 397.24 USD | `-16.24%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 2,040,000.00 USD | 0.00 USD | 16,390.00 USD | `-16.10%` | `27,799,000,000.00` |
| `Live` | `Long` | `590.50` | 2,030,000.00 USD | 0.00 USD | 2,420.00 USD | `-15.96%` | `4,106,000,000.00` |
| `Live` | `Long` | `591.50` | 2,020,000.00 USD | 0.00 USD | 2,180.00 USD | `-15.82%` | `3,693,000,000.00` |
| `Live` | `Long` | `592.50` | 2,020,000.00 USD | 0.00 USD | 226.93 USD | `-15.67%` | `383,000,000.00` |
| `Live` | `Long` | `593.50` | 2,020,000.00 USD | 0.00 USD | 44,960.00 USD | `-15.53%` | `75,762,000,000.00` |
| `Live` | `Long` | `595.50` | 1,980,000.00 USD | 0.00 USD | 940.89 USD | `-15.25%` | `1,580,000,000.00` |
| `Live` | `Long` | `596.50` | 1,980,000.00 USD | 0.00 USD | 7,680.00 USD | `-15.10%` | `12,878,000,000.00` |
| `Live` | `Long` | `597.50` | 1,970,000.00 USD | 0.00 USD | 2,480.00 USD | `-14.96%` | `4,156,000,000.00` |
| `Live` | `Long` | `598.50` | 1,970,000.00 USD | 0.00 USD | 791.22 USD | `-14.82%` | `1,322,000,000.00` |
| `Live` | `Long` | `600.50` | 1,970,000.00 USD | 0.00 USD | 945.19 USD | `-14.54%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,960,000.00 USD | 0.00 USD | 16,880.00 USD | `-14.39%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,950,000.00 USD | 0.00 USD | 222.32 USD | `-14.25%` | `369,000,000.00` |
| `Live` | `Long` | `603.50` | 1,950,000.00 USD | 0.00 USD | 22,860.00 USD | `-14.11%` | `37,877,000,000.00` |
| `Live` | `Long` | `604.50` | 1,920,000.00 USD | 0.00 USD | 256.91 USD | `-13.97%` | `425,000,000.00` |
| `Live` | `Long` | `606.50` | 1,920,000.00 USD | 0.00 USD | 60,390.00 USD | `-13.68%` | `99,569,000,000.00` |
| `Live` | `Long` | `607.50` | 1,860,000.00 USD | 0.00 USD | 4,250.00 USD | `-13.54%` | `7,002,000,000.00` |
| `Live` | `Long` | `609.50` | 1,860,000.00 USD | 0.00 USD | 6,410.00 USD | `-13.25%` | `10,516,000,000.00` |
| `Live` | `Long` | `611.50` | 1,850,000.00 USD | 0.00 USD | 1,580.00 USD | `-12.97%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,850,000.00 USD | 0.00 USD | 12,250.00 USD | `-12.83%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,840,000.00 USD | 0.00 USD | 120.25 USD | `-12.69%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,840,000.00 USD | 0.00 USD | 4,280.00 USD | `-12.54%` | `6,973,000,000.00` |
| `Live` | `Long` | `615.50` | 1,840,000.00 USD | 0.00 USD | 1,540.00 USD | `-12.40%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,830,000.00 USD | 0.00 USD | 156.23 USD | `-12.12%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,830,000.00 USD | 0.00 USD | 932.70 USD | `-11.97%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,830,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.83%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,830,000.00 USD | 0.00 USD | 2,690.00 USD | `-11.69%` | `4,329,000,000.00` |
| `Live` | `Long` | `621.50` | 1,830,000.00 USD | 0.00 USD | 696.70 USD | `-11.55%` | `1,121,000,000.00` |
| `Live` | `Long` | `623.50` | 1,830,000.00 USD | 0.00 USD | 415.25 USD | `-11.26%` | `666,000,000.00` |
| `Live` | `Long` | `624.50` | 1,830,000.00 USD | 0.00 USD | 22,260.00 USD | `-11.12%` | `35,642,000,000.00` |
| `Live` | `Long` | `625.50` | 1,810,000.00 USD | 0.00 USD | 14,200.00 USD | `-10.98%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,790,000.00 USD | 0.00 USD | 964.81 USD | `-10.84%` | `1,540,000,000.00` |
| `Live` | `Long` | `628.50` | 1,790,000.00 USD | 0.00 USD | 590.79 USD | `-10.55%` | `940,000,000.00` |
| `Live` | `Long` | `630.50` | 1,790,000.00 USD | 0.00 USD | 153.21 USD | `-10.27%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,790,000.00 USD | 0.00 USD | 2,900.00 USD | `-10.12%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,790,000.00 USD | 0.00 USD | 3,560.00 USD | `-9.98%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,780,000.00 USD | 0.00 USD | 5,900.00 USD | `-9.70%` | `9,302,000,000.00` |
| `Live` | `Long` | `635.50` | 1,780,000.00 USD | 0.00 USD | 155.06 USD | `-9.55%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,780,000.00 USD | 0.00 USD | 1,110.00 USD | `-9.41%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,780,000.00 USD | 0.00 USD | 305.36 USD | `-9.27%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,780,000.00 USD | 0.00 USD | 6,710.00 USD | `-9.13%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,770,000.00 USD | 0.00 USD | 1,490.00 USD | `-8.98%` | `2,333,000,000.00` |
| `Live` | `Long` | `640.50` | 1,770,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-8.84%` | `2,057,820,000,000.00` |
| `Live` | `Short` | `642.50` | 334.10 USD | 334.10 USD | 0.00 USD | `-8.56%` | `520,000,000.00` |
| `Live` | `Long` | `643.50` | 449,090.00 USD | 0.00 USD | 339.12 USD | `-8.42%` | `527,000,000.00` |
| `Live` | `Long` | `644.50` | 448,750.00 USD | 0.00 USD | 19,460.00 USD | `-8.27%` | `30,194,000,000.00` |
| `Live` | `Long` | `645.50` | 429,290.00 USD | 0.00 USD | 307.26 USD | `-8.13%` | `476,000,000.00` |
| `Live` | `Long` | `646.50` | 428,990.00 USD | 0.00 USD | 155.81 USD | `-7.99%` | `241,000,000.00` |
| `Live` | `Long` | `648.50` | 428,830.00 USD | 0.00 USD | 1,940.00 USD | `-7.70%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 426,890.00 USD | 0.00 USD | 1,620.00 USD | `-7.56%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 425,270.00 USD | 0.00 USD | 335.01 USD | `-7.42%` | `515,000,000.00` |
| `Live` | `Long` | `651.50` | 424,930.00 USD | 0.00 USD | 13,790.00 USD | `-7.28%` | `21,159,000,000.00` |
| `Live` | `Long` | `652.50` | 411,150.00 USD | 0.00 USD | 652.50 USD | `-7.13%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 410,500.00 USD | 0.00 USD | 98,240.00 USD | `-6.99%` | `150,322,000,000.00` |
| `Live` | `Long` | `654.50` | 312,260.00 USD | 0.00 USD | 100.14 USD | `-6.85%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 312,160.00 USD | 0.00 USD | 122.58 USD | `-6.71%` | `187,000,000.00` |
| `Live` | `Long` | `656.50` | 312,040.00 USD | 0.00 USD | 24,500.00 USD | `-6.57%` | `37,326,000,000.00` |
| `Live` | `Long` | `657.50` | 287,530.00 USD | 0.00 USD | 13,020.00 USD | `-6.42%` | `19,802,000,000.00` |
| `Live` | `Long` | `658.50` | 274,510.00 USD | 0.00 USD | 2,050.00 USD | `-6.28%` | `3,114,000,000.00` |
| `Live` | `Long` | `659.50` | 272,460.00 USD | 0.00 USD | 45,510.00 USD | `-6.14%` | `69,000,000,000.00` |
| `Live` | `Long` | `660.50` | 226,960.00 USD | 0.00 USD | 3,410.00 USD | `-6.00%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 223,540.00 USD | 0.00 USD | 20,140.00 USD | `-5.85%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 203,400.00 USD | 0.00 USD | 2,850.00 USD | `-5.71%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 200,550.00 USD | 0.00 USD | 13,440.00 USD | `-5.57%` | `20,263,000,000.00` |
| `Live` | `Long` | `664.50` | 187,110.00 USD | 0.00 USD | 592.73 USD | `-5.43%` | `892,000,000.00` |
| `Live` | `Long` | `665.50` | 186,520.00 USD | 0.00 USD | 8,790.00 USD | `-5.28%` | `13,205,000,000.00` |
| `Live` | `Long` | `666.50` | 177,730.00 USD | 0.00 USD | 2,200.00 USD | `-5.14%` | `3,298,000,000.00` |
| `Live` | `Long` | `667.50` | 175,530.00 USD | 0.00 USD | 1,830.00 USD | `-5.00%` | `2,749,000,000.00` |
| `Live` | `Long` | `668.50` | 173,700.00 USD | 0.00 USD | 8,920.00 USD | `-4.86%` | `13,339,000,000.00` |
| `Live` | `Long` | `669.50` | 164,780.00 USD | 0.00 USD | 5,060.00 USD | `-4.72%` | `7,565,000,000.00` |
| `Live` | `Long` | `670.50` | 159,710.00 USD | 0.00 USD | 4,670.00 USD | `-4.57%` | `6,963,000,000.00` |
| `Live` | `Long` | `671.50` | 155,050.00 USD | 0.00 USD | 830.65 USD | `-4.43%` | `1,237,000,000.00` |
| `Live` | `Long` | `672.50` | 154,220.00 USD | 0.00 USD | 7,860.00 USD | `-4.29%` | `11,685,000,000.00` |
| `Live` | `Long` | `673.50` | 146,360.00 USD | 0.00 USD | 39,130.00 USD | `-4.15%` | `58,100,000,000.00` |
| `Live` | `Long` | `674.50` | 107,230.00 USD | 0.00 USD | 4,100.00 USD | `-4.00%` | `6,078,000,000.00` |
| `Live` | `Long` | `675.50` | 103,130.00 USD | 0.00 USD | 74,720.00 USD | `-3.86%` | `110,607,000,000.00` |
| `Live` | `Long` | `676.50` | 28,410.00 USD | 0.00 USD | 1,960.00 USD | `-3.72%` | `2,901,000,000.00` |
| `Live` | `Long` | `677.50` | 26,450.00 USD | 0.00 USD | 250.67 USD | `-3.58%` | `370,000,000.00` |
| `Live` | `Long` | `678.50` | 26,200.00 USD | 0.00 USD | 2,390.00 USD | `-3.43%` | `3,518,000,000.00` |
| `Live` | `Long` | `679.50` | 23,810.00 USD | 0.00 USD | 998.19 USD | `-3.29%` | `1,469,000,000.00` |
| `Live` | `Long` | `680.50` | 22,810.00 USD | 0.00 USD | 21,870.00 USD | `-3.15%` | `32,144,000,000.00` |
| `Live` | `Long` | `681.50` | 939.79 USD | 0.00 USD | 939.79 USD | `-3.01%` | `1,379,000,000.00` |
| `Live` | `Short` | `696.50` | 2,690.00 USD | 2,350.00 USD | 0.00 USD | `-0.87%` | `3,381,000,000.00` |
| `Live` | `Short` | `720.50` | 3,070.00 USD | 376.82 USD | 0.00 USD | `+2.54%` | `523,000,000.00` |
| `Live` | `Short` | `721.50` | 36,110.00 USD | 33,040.00 USD | 0.00 USD | `+2.69%` | `45,800,000,000.00` |
| `Live` | `Short` | `722.50` | 38,060.00 USD | 1,950.00 USD | 0.00 USD | `+2.83%` | `2,702,000,000.00` |
| `Live` | `Short` | `723.50` | 40,230.00 USD | 2,170.00 USD | 0.00 USD | `+2.97%` | `2,996,000,000.00` |
| `Live` | `Short` | `724.50` | 40,760.00 USD | 525.26 USD | 0.00 USD | `+3.11%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 41,750.00 USD | 993.93 USD | 0.00 USD | `+3.25%` | `1,370,000,000.00` |
| `Live` | `Short` | `726.50` | 45,460.00 USD | 3,710.00 USD | 0.00 USD | `+3.40%` | `5,105,000,000.00` |
| `Live` | `Short` | `727.50` | 45,660.00 USD | 200.06 USD | 0.00 USD | `+3.54%` | `275,000,000.00` |
| `Live` | `Short` | `728.50` | 86,730.00 USD | 41,080.00 USD | 0.00 USD | `+3.68%` | `56,385,000,000.00` |
| `Live` | `Short` | `729.50` | 257,750.00 USD | 171,010.00 USD | 0.00 USD | `+3.82%` | `234,425,000,000.00` |
| `Live` | `Short` | `730.50` | 280,190.00 USD | 22,440.00 USD | 0.00 USD | `+3.97%` | `30,716,000,000.00` |
| `Live` | `Short` | `731.50` | 282,230.00 USD | 2,050.00 USD | 0.00 USD | `+4.11%` | `2,797,000,000.00` |
| `Live` | `Short` | `732.50` | 422,530.00 USD | 140,300.00 USD | 0.00 USD | `+4.25%` | `191,538,000,000.00` |
| `Live` | `Short` | `733.50` | 435,030.00 USD | 12,500.00 USD | 0.00 USD | `+4.39%` | `17,040,000,000.00` |
| `Live` | `Short` | `734.50` | 623,900.00 USD | 188,860.00 USD | 0.00 USD | `+4.54%` | `257,131,000,000.00` |
| `Live` | `Short` | `735.50` | 661,260.00 USD | 37,370.00 USD | 0.00 USD | `+4.68%` | `50,806,000,000.00` |
| `Live` | `Short` | `736.50` | 705,340.00 USD | 44,080.00 USD | 0.00 USD | `+4.82%` | `59,844,000,000.00` |
| `Live` | `Short` | `737.50` | 713,010.00 USD | 7,670.00 USD | 0.00 USD | `+4.96%` | `10,405,000,000.00` |
| `Live` | `Short` | `738.50` | 766,030.00 USD | 53,020.00 USD | 0.00 USD | `+5.11%` | `71,790,000,000.00` |
| `Live` | `Short` | `739.50` | 874,340.00 USD | 108,310.00 USD | 0.00 USD | `+5.25%` | `146,462,000,000.00` |
| `Live` | `Short` | `740.50` | 881,100.00 USD | 6,760.00 USD | 0.00 USD | `+5.39%` | `9,131,000,000.00` |
| `Live` | `Short` | `741.50` | 913,860.00 USD | 32,760.00 USD | 0.00 USD | `+5.53%` | `44,185,000,000.00` |
| `Live` | `Short` | `742.50` | 980,010.00 USD | 66,150.00 USD | 0.00 USD | `+5.67%` | `89,093,000,000.00` |
| `Live` | `Short` | `743.50` | 1,030,000.00 USD | 49,810.00 USD | 0.00 USD | `+5.82%` | `66,998,000,000.00` |
| `Live` | `Short` | `744.50` | 1,160,000.00 USD | 126,390.00 USD | 0.00 USD | `+5.96%` | `169,769,000,000.00` |
| `Live` | `Short` | `745.50` | 1,180,000.00 USD | 20,430.00 USD | 0.00 USD | `+6.10%` | `27,406,000,000.00` |
| `Live` | `Short` | `746.50` | 1,360,000.00 USD | 185,960.00 USD | 0.00 USD | `+6.24%` | `249,111,000,000.00` |
| `Live` | `Short` | `748.50` | 1,370,000.00 USD | 4,270.00 USD | 0.00 USD | `+6.53%` | `5,702,000,000.00` |
| `Live` | `Short` | `749.50` | 1,430,000.00 USD | 67,670.00 USD | 0.00 USD | `+6.67%` | `90,291,000,000.00` |
| `Live` | `Short` | `750.50` | 2,010,000.00 USD | 574,740.00 USD | 0.00 USD | `+6.81%` | `765,807,000,000.00` |
| `Live` | `Short` | `751.50` | 2,030,000.00 USD | 21,390.00 USD | 0.00 USD | `+6.96%` | `28,467,000,000.00` |
| `Live` | `Short` | `752.50` | 2,080,000.00 USD | 48,630.00 USD | 0.00 USD | `+7.10%` | `64,624,000,000.00` |
| `Live` | `Short` | `753.50` | 2,080,000.00 USD | 4,660.00 USD | 0.00 USD | `+7.24%` | `6,189,000,000.00` |
| `Live` | `Short` | `754.50` | 2,940,000.00 USD | 860,170.00 USD | 0.00 USD | `+7.38%` | `1,140,058,000,000.00` |
| `Live` | `Short` | `755.50` | 2,960,000.00 USD | 11,710.00 USD | 0.00 USD | `+7.52%` | `15,500,000,000.00` |
| `Live` | `Short` | `757.50` | 2,960,000.00 USD | 2,010.00 USD | 0.00 USD | `+7.81%` | `2,652,000,000.00` |
| `Live` | `Short` | `758.50` | 3,140,000.00 USD | 180,980.00 USD | 0.00 USD | `+7.95%` | `238,608,000,000.00` |
| `Live` | `Short` | `759.50` | 3,140,000.00 USD | 704.82 USD | 0.00 USD | `+8.09%` | `928,000,000.00` |
| `Live` | `Short` | `760.50` | 3,150,000.00 USD | 6,020.00 USD | 0.00 USD | `+8.24%` | `7,921,000,000.00` |
| `Live` | `Short` | `761.50` | 3,150,000.00 USD | 367.04 USD | 0.00 USD | `+8.38%` | `482,000,000.00` |
| `Live` | `Short` | `762.50` | 3,150,000.00 USD | 8,050.00 USD | 0.00 USD | `+8.52%` | `10,551,000,000.00` |
| `Live` | `Short` | `763.50` | 3,750,000.00 USD | 595,810.00 USD | 0.00 USD | `+8.66%` | `780,361,000,000.00` |
| `Live` | `Short` | `765.50` | 3,750,000.00 USD | 785.40 USD | 0.00 USD | `+8.95%` | `1,026,000,000.00` |
| `Live` | `Short` | `766.50` | 3,750,000.00 USD | 2,850.00 USD | 0.00 USD | `+9.09%` | `3,719,000,000.00` |
| `Live` | `Short` | `767.50` | 3,830,000.00 USD | 74,200.00 USD | 0.00 USD | `+9.23%` | `96,674,000,000.00` |
| `Live` | `Short` | `768.50` | 3,830,000.00 USD | 300.48 USD | 0.00 USD | `+9.37%` | `391,000,000.00` |
| `Live` | `Short` | `770.50` | 3,830,000.00 USD | 661.86 USD | 0.00 USD | `+9.66%` | `859,000,000.00` |
| `Live` | `Short` | `771.50` | 4,220,000.00 USD | 395,010.00 USD | 0.00 USD | `+9.80%` | `512,000,000,000.00` |
| `Live` | `Short` | `772.50` | 4,230,000.00 USD | 2,450.00 USD | 0.00 USD | `+9.94%` | `3,173,000,000.00` |
| `Live` | `Short` | `773.50` | 4,230,000.00 USD | 1,480.00 USD | 0.00 USD | `+10.09%` | `1,907,000,000.00` |
| `Live` | `Short` | `775.50` | 4,230,000.00 USD | 544.40 USD | 0.00 USD | `+10.37%` | `702,000,000.00` |
| `Live` | `Short` | `776.50` | 4,320,000.00 USD | 89,520.00 USD | 0.00 USD | `+10.51%` | `115,281,000,000.00` |
| `Live` | `Short` | `777.50` | 4,320,000.00 USD | 209.15 USD | 0.00 USD | `+10.66%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 4,330,000.00 USD | 8,100.00 USD | 0.00 USD | `+10.80%` | `10,401,000,000.00` |
| `Live` | `Short` | `780.50` | 4,330,000.00 USD | 4,150.00 USD | 0.00 USD | `+11.08%` | `5,318,000,000.00` |
| `Live` | `Short` | `781.50` | 4,330,000.00 USD | 4,320.00 USD | 0.00 USD | `+11.22%` | `5,527,000,000.00` |
| `Live` | `Short` | `784.50` | 4,330,000.00 USD | 130.23 USD | 0.00 USD | `+11.65%` | `166,000,000.00` |
| `Live` | `Short` | `785.50` | 4,340,000.00 USD | 1,750.00 USD | 0.00 USD | `+11.79%` | `2,227,000,000.00` |
| `Live` | `Short` | `786.50` | 4,340,000.00 USD | 4,780.00 USD | 0.00 USD | `+11.94%` | `6,080,000,000.00` |
| `Live` | `Short` | `788.50` | 4,340,000.00 USD | 1,580.00 USD | 0.00 USD | `+12.22%` | `2,000,000,000.00` |
| `Live` | `Short` | `790.50` | 4,340,000.00 USD | 247.43 USD | 0.00 USD | `+12.51%` | `313,000,000.00` |
| `Live` | `Short` | `793.50` | 4,350,000.00 USD | 2,660.00 USD | 0.00 USD | `+12.93%` | `3,352,000,000.00` |
| `Live` | `Short` | `795.50` | 4,350,000.00 USD | 518.67 USD | 0.00 USD | `+13.22%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 4,350,000.00 USD | 1,240.00 USD | 0.00 USD | `+13.36%` | `1,553,000,000.00` |
| `Live` | `Short` | `797.50` | 4,350,000.00 USD | 1,090.00 USD | 0.00 USD | `+13.50%` | `1,367,000,000.00` |
| `Live` | `Short` | `799.50` | 4,350,000.00 USD | 438.13 USD | 0.00 USD | `+13.79%` | `548,000,000.00` |
| `Live` | `Short` | `800.50` | 4,380,000.00 USD | 28,250.00 USD | 0.00 USD | `+13.93%` | `35,287,000,000.00` |
| `Live` | `Short` | `801.50` | 5,090,000.00 USD | 709,870.00 USD | 0.00 USD | `+14.07%` | `885,682,000,000.00` |
| `Live` | `Short` | `802.50` | 5,160,000.00 USD | 72,430.00 USD | 0.00 USD | `+14.21%` | `90,251,000,000.00` |
| `Live` | `Short` | `803.50` | 5,170,000.00 USD | 5,720.00 USD | 0.00 USD | `+14.36%` | `7,115,000,000.00` |
| `Live` | `Short` | `804.50` | 5,170,000.00 USD | 181.01 USD | 0.00 USD | `+14.50%` | `225,000,000.00` |
| `Live` | `Short` | `805.50` | 5,180,000.00 USD | 15,600.00 USD | 0.00 USD | `+14.64%` | `19,368,000,000.00` |
| `Live` | `Short` | `806.50` | 5,180,000.00 USD | 2,890.00 USD | 0.00 USD | `+14.78%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 5,180,000.00 USD | 738.06 USD | 0.00 USD | `+14.93%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 5,200,000.00 USD | 13,210.00 USD | 0.00 USD | `+15.07%` | `16,339,000,000.00` |
| `Live` | `Short` | `811.50` | 5,200,000.00 USD | 434.15 USD | 0.00 USD | `+15.49%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 5,200,000.00 USD | 692.32 USD | 0.00 USD | `+15.92%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 5,210,000.00 USD | 8,150.00 USD | 0.00 USD | `+16.06%` | `9,992,000,000.00` |
| `Live` | `Short` | `816.50` | 5,220,000.00 USD | 15,410.00 USD | 0.00 USD | `+16.21%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 5,220,000.00 USD | 325.37 USD | 0.00 USD | `+16.35%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 5,230,000.00 USD | 7,720.00 USD | 0.00 USD | `+16.49%` | `9,432,000,000.00` |
| `Live` | `Short` | `822.50` | 5,320,000.00 USD | 84,720.00 USD | 0.00 USD | `+17.06%` | `102,997,000,000.00` |
| `Live` | `Short` | `825.50` | 5,840,000.00 USD | 528,640.00 USD | 0.00 USD | `+17.49%` | `640,389,000,000.00` |
| `Live` | `Short` | `826.50` | 5,840,000.00 USD | 426.47 USD | 0.00 USD | `+17.63%` | `516,000,000.00` |
| `Live` | `Short` | `828.50` | 5,850,000.00 USD | 5,880.00 USD | 0.00 USD | `+17.91%` | `7,102,000,000.00` |
| `Live` | `Short` | `834.50` | 5,850,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.77%` | `1,206,000,000.00` |
| `Live` | `Short` | `836.50` | 5,850,000.00 USD | 239.24 USD | 0.00 USD | `+19.05%` | `286,000,000.00` |
| `Live` | `Short` | `837.50` | 5,850,000.00 USD | 3,570.00 USD | 0.00 USD | `+19.20%` | `4,257,000,000.00` |
| `Live` | `Short` | `838.50` | 5,880,000.00 USD | 21,840.00 USD | 0.00 USD | `+19.34%` | `26,046,000,000.00` |
| `Live` | `Short` | `840.50` | 5,880,000.00 USD | 679.96 USD | 0.00 USD | `+19.62%` | `809,000,000.00` |
| `Live` | `Short` | `841.50` | 5,880,000.00 USD | 4,410.00 USD | 0.00 USD | `+19.76%` | `5,235,000,000.00` |
| `Live` | `Short` | `842.50` | 5,890,000.00 USD | 12,050.00 USD | 0.00 USD | `+19.91%` | `14,297,000,000.00` |
| `Live` | `Short` | `844.50` | 5,930,000.00 USD | 34,100.00 USD | 0.00 USD | `+20.19%` | `40,378,000,000.00` |
| `Live` | `Short` | `847.50` | 5,930,000.00 USD | 289.00 USD | 0.00 USD | `+20.62%` | `341,000,000.00` |
| `Live` | `Short` | `850.50` | 5,930,000.00 USD | 393.78 USD | 0.00 USD | `+21.05%` | `463,000,000.00` |
| `Live` | `Short` | `852.50` | 5,930,000.00 USD | 5,020.00 USD | 0.00 USD | `+21.33%` | `5,884,000,000.00` |
| `Live` | `Short` | `855.50` | 5,940,000.00 USD | 2,110.00 USD | 0.00 USD | `+21.76%` | `2,462,000,000.00` |
| `Live` | `Short` | `857.50` | 5,940,000.00 USD | 1,480.00 USD | 0.00 USD | `+22.04%` | `1,721,000,000.00` |
| `Live` | `Short` | `859.50` | 5,950,000.00 USD | 16,380.00 USD | 0.00 USD | `+22.33%` | `19,059,000,000.00` |
| `Live` | `Short` | `862.50` | 6,480,000.00 USD | 526,120.00 USD | 0.00 USD | `+22.75%` | `610,000,000,000.00` |
| `Live` | `Short` | `864.50` | 6,770,000.00 USD | 289,650.00 USD | 0.00 USD | `+23.04%` | `335,051,000,000.00` |
| `Live` | `Short` | `865.50` | 6,790,000.00 USD | 18,900.00 USD | 0.00 USD | `+23.18%` | `21,832,000,000.00` |
| `Live` | `Short` | `873.50` | 6,790,000.00 USD | 326.69 USD | 0.00 USD | `+24.32%` | `374,000,000.00` |
| `Live` | `Short` | `877.50` | 7,490,000.00 USD | 702,210.00 USD | 0.00 USD | `+24.89%` | `800,238,000,000.00` |
| `Live` | `Short` | `878.50` | 7,500,000.00 USD | 4,540.00 USD | 0.00 USD | `+25.03%` | `5,165,000,000.00` |
| `Live` | `Short` | `880.50` | 7,500,000.00 USD | 663.02 USD | 0.00 USD | `+25.31%` | `753,000,000.00` |
| `Live` | `Short` | `884.50` | 7,510,000.00 USD | 14,140.00 USD | 0.00 USD | `+25.88%` | `15,992,000,000.00` |
| `Live` | `Short` | `885.50` | 7,510,000.00 USD | 2,580.00 USD | 0.00 USD | `+26.03%` | `2,917,000,000.00` |
| `Live` | `Short` | `886.50` | 7,510,000.00 USD | 215.42 USD | 0.00 USD | `+26.17%` | `243,000,000.00` |
| `Live` | `Short` | `887.50` | 7,510,000.00 USD | 385.18 USD | 0.00 USD | `+26.31%` | `434,000,000.00` |
| `Live` | `Short` | `890.50` | 7,510,000.00 USD | 380.24 USD | 0.00 USD | `+26.74%` | `427,000,000.00` |
| `Live` | `Short` | `891.50` | 7,520,000.00 USD | 3,950.00 USD | 0.00 USD | `+26.88%` | `4,429,000,000.00` |
| `Live` | `Short` | `893.50` | 7,520,000.00 USD | 173.34 USD | 0.00 USD | `+27.17%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,540,000.00 USD | 26,840.00 USD | 0.00 USD | `+27.31%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 7,770,000.00 USD | 223,880.00 USD | 0.00 USD | `+27.45%` | `250,000,000,000.00` |
| `Live` | `Short` | `897.50` | 7,860,000.00 USD | 89,750.00 USD | 0.00 USD | `+27.73%` | `100,000,000,000.00` |
| `Live` | `Short` | `898.50` | 8,010,000.00 USD | 153,370.00 USD | 0.00 USD | `+27.88%` | `170,697,000,000.00` |
| `Live` | `Short` | `899.50` | 8,020,000.00 USD | 5,400.00 USD | 0.00 USD | `+28.02%` | `6,000,000,000.00` |
| `Live` | `Short` | `902.50` | 8,020,000.00 USD | 305.05 USD | 0.00 USD | `+28.45%` | `338,000,000.00` |
| `Live` | `Short` | `903.50` | 8,020,000.00 USD | 5,470.00 USD | 0.00 USD | `+28.59%` | `6,050,000,000.00` |
| `Live` | `Short` | `904.50` | 8,180,000.00 USD | 158,550.00 USD | 0.00 USD | `+28.73%` | `175,293,000,000.00` |
| `Live` | `Short` | `905.50` | 8,180,000.00 USD | 107.75 USD | 0.00 USD | `+28.87%` | `119,000,000.00` |
| `Live` | `Short` | `906.50` | 8,370,000.00 USD | 188,080.00 USD | 0.00 USD | `+29.02%` | `207,476,000,000.00` |
| `Live` | `Short` | `908.50` | 8,370,000.00 USD | 2,420.00 USD | 0.00 USD | `+29.30%` | `2,669,000,000.00` |
| `Live` | `Short` | `909.50` | 8,410,000.00 USD | 37,210.00 USD | 0.00 USD | `+29.44%` | `40,909,000,000.00` |
| `Live` | `Short` | `910.50` | 8,440,000.00 USD | 34,630.00 USD | 0.00 USD | `+29.58%` | `38,036,000,000.00` |
| `Live` | `Short` | `911.50` | 8,440,000.00 USD | 121.23 USD | 0.00 USD | `+29.73%` | `133,000,000.00` |
| `Live` | `Short` | `912.50` | 8,450,000.00 USD | 1,820.00 USD | 0.00 USD | `+29.87%` | `2,000,000,000.00` |
| `Live` | `Short` | `914.50` | 8,450,000.00 USD | 389.58 USD | 0.00 USD | `+30.15%` | `426,000,000.00` |
| `Live` | `Short` | `917.50` | 8,470,000.00 USD | 22,940.00 USD | 0.00 USD | `+30.58%` | `25,000,000,000.00` |
| `Live` | `Short` | `923.50` | 8,500,000.00 USD | 30,360.00 USD | 0.00 USD | `+31.43%` | `32,872,000,000.00` |
| `Live` | `Short` | `924.50` | 8,500,000.00 USD | 649.00 USD | 0.00 USD | `+31.58%` | `702,000,000.00` |
| `Live` | `Short` | `930.50` | 8,500,000.00 USD | 172.14 USD | 0.00 USD | `+32.43%` | `185,000,000.00` |
| `Live` | `Short` | `934.50` | 8,500,000.00 USD | 956.93 USD | 0.00 USD | `+33.00%` | `1,024,000,000.00` |
| `Live` | `Short` | `935.50` | 8,510,000.00 USD | 4,760.00 USD | 0.00 USD | `+33.14%` | `5,090,000,000.00` |
| `Live` | `Short` | `936.50` | 8,630,000.00 USD | 121,750.00 USD | 0.00 USD | `+33.28%` | `130,000,000,000.00` |
| `Live` | `Short` | `940.50` | 8,640,000.00 USD | 7,750.00 USD | 0.00 USD | `+33.85%` | `8,244,000,000.00` |
| `Live` | `Short` | `944.50` | 8,840,000.00 USD | 207,790.00 USD | 0.00 USD | `+34.42%` | `220,000,000,000.00` |
| `Live` | `Short` | `949.50` | 8,850,000.00 USD | 2,820.00 USD | 0.00 USD | `+35.14%` | `2,965,000,000.00` |
| `Live` | `Short` | `956.50` | 8,870,000.00 USD | 18,930.00 USD | 0.00 USD | `+36.13%` | `19,788,000,000.00` |
| `Live` | `Short` | `957.50` | 8,880,000.00 USD | 19,600.00 USD | 0.00 USD | `+36.27%` | `20,472,000,000.00` |
| `Live` | `Short` | `958.50` | 8,880,000.00 USD | 204.16 USD | 0.00 USD | `+36.42%` | `213,000,000.00` |
| `Live` | `Short` | `960.50` | 8,890,000.00 USD | 3,210.00 USD | 0.00 USD | `+36.70%` | `3,344,000,000.00` |
| `Live` | `Short` | `965.50` | 8,920,000.00 USD | 35,070.00 USD | 0.00 USD | `+37.41%` | `36,319,000,000.00` |
| `Live` | `Short` | `968.50` | 8,930,000.00 USD | 1,940.00 USD | 0.00 USD | `+37.84%` | `2,000,000,000.00` |
| `Live` | `Short` | `969.50` | 8,930,000.00 USD | 5,780.00 USD | 0.00 USD | `+37.98%` | `5,960,000,000.00` |
| `Live` | `Short` | `976.50` | 8,990,000.00 USD | 59,960.00 USD | 0.00 USD | `+38.98%` | `61,406,000,000.00` |
| `Live` | `Short` | `977.50` | 9,010,000.00 USD | 14,210.00 USD | 0.00 USD | `+39.12%` | `14,541,000,000.00` |
| `Live` | `Short` | `981.50` | 9,020,000.00 USD | 14,480.00 USD | 0.00 USD | `+39.69%` | `14,758,000,000.00` |
| `Live` | `Short` | `985.50` | 9,020,000.00 USD | 1,100.00 USD | 0.00 USD | `+40.26%` | `1,112,000,000.00` |
| `Live` | `Short` | `987.50` | 9,090,000.00 USD | 69,740.00 USD | 0.00 USD | `+40.54%` | `70,621,000,000.00` |
| `Live` | `Short` | `988.50` | 9,380,000.00 USD | 288,210.00 USD | 0.00 USD | `+40.69%` | `291,563,000,000.00` |
| `Live` | `Short` | `989.50` | 9,480,000.00 USD | 98,950.00 USD | 0.00 USD | `+40.83%` | `99,998,000,000.00` |
| `Live` | `Short` | `990.50` | 9,510,000.00 USD | 28,300.00 USD | 0.00 USD | `+40.97%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 9,510,000.00 USD | 2,320.00 USD | 0.00 USD | `+41.25%` | `2,339,000,000.00` |
| `Live` | `Short` | `993.50` | 9,510,000.00 USD | 791.82 USD | 0.00 USD | `+41.40%` | `797,000,000.00` |
| `Live` | `Short` | `994.50` | 9,790,000.00 USD | 285,520.00 USD | 0.00 USD | `+41.54%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 9,790,000.00 USD | 313.58 USD | 0.00 USD | `+41.68%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 9,800,000.00 USD | 989.52 USD | 0.00 USD | `+41.82%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 9,800,000.00 USD | 7,300.00 USD | 0.00 USD | `+41.97%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 9,850,000.00 USD | 46,370.00 USD | 0.00 USD | `+42.11%` | `46,439,000,000.00` |
| `Live` | `Short` | `1002.50` | 9,850,000.00 USD | 161.40 USD | 0.00 USD | `+42.68%` | `161,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,850,000.00 USD | 677.36 USD | 0.00 USD | `+42.82%` | `675,000,000.00` |
| `Live` | `Short` | `1005.50` | 9,850,000.00 USD | 4,050.00 USD | 0.00 USD | `+43.11%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 9,880,000.00 USD | 29,110.00 USD | 0.00 USD | `+43.53%` | `28,860,000,000.00` |
| `Live` | `Short` | `1009.50` | 9,930,000.00 USD | 51,370.00 USD | 0.00 USD | `+43.67%` | `50,889,000,000.00` |
| `Live` | `Short` | `1011.50` | 9,950,000.00 USD | 14,570.00 USD | 0.00 USD | `+43.96%` | `14,403,000,000.00` |
| `Live` | `Short` | `1024.50` | 9,950,000.00 USD | 238.71 USD | 0.00 USD | `+45.81%` | `233,000,000.00` |
| `Live` | `Short` | `1030.50` | 10,670,000.00 USD | 718,890.00 USD | 0.00 USD | `+46.66%` | `697,611,000,000.00` |
| `Live` | `Short` | `1032.50` | 10,670,000.00 USD | 497.66 USD | 0.00 USD | `+46.95%` | `482,000,000.00` |
| `Live` | `Short` | `1050.50` | 10,670,000.00 USD | 500.04 USD | 0.00 USD | `+49.51%` | `476,000,000.00` |
| `Live` | `Short` | `1059.50` | 10,740,000.00 USD | 66,220.00 USD | 0.00 USD | `+50.79%` | `62,500,000,000.00` |
| `Live` | `Short` | `1062.50` | 10,740,000.00 USD | 635.38 USD | 0.00 USD | `+51.22%` | `598,000,000.00` |
| `Live` | `Short` | `1063.50` | 10,760,000.00 USD | 18,960.00 USD | 0.00 USD | `+51.36%` | `17,826,000,000.00` |
| `Live` | `Short` | `1064.50` | 10,760,000.00 USD | 3,510.00 USD | 0.00 USD | `+51.50%` | `3,301,000,000.00` |
| `Live` | `Short` | `1066.50` | 11,450,000.00 USD | 693,230.00 USD | 0.00 USD | `+51.79%` | `650,000,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,450,000.00 USD | 2,940.00 USD | 0.00 USD | `+52.78%` | `2,738,000,000.00` |
| `Live` | `Short` | `1074.50` | 11,460,000.00 USD | 120.34 USD | 0.00 USD | `+52.93%` | `112,000,000.00` |
| `Live` | `Short` | `1077.50` | 11,460,000.00 USD | 766.10 USD | 0.00 USD | `+53.35%` | `711,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,460,000.00 USD | 5,770.00 USD | 0.00 USD | `+54.78%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,480,000.00 USD | 16,230.00 USD | 0.00 USD | `+54.92%` | `14,913,000,000.00` |
| `Live` | `Short` | `1089.50` | 11,480,000.00 USD | 1,570.00 USD | 0.00 USD | `+55.06%` | `1,445,000,000.00` |
| `Live` | `Short` | `1090.50` | 11,550,000.00 USD | 74,430.00 USD | 0.00 USD | `+55.20%` | `68,249,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,670,000.00 USD | 120,790.00 USD | 0.00 USD | `+55.63%` | `110,460,000,000.00` |
| `Live` | `Short` | `1095.50` | 11,740,000.00 USD | 70,020.00 USD | 0.00 USD | `+55.91%` | `63,916,000,000.00` |
| `Live` | `Short` | `1100.50` | 11,750,000.00 USD | 507.33 USD | 0.00 USD | `+56.63%` | `461,000,000.00` |
| `Live` | `Short` | `1114.50` | 11,750,000.00 USD | 2,230.00 USD | 0.00 USD | `+58.62%` | `2,000,000,000.00` |
| `Live` | `Short` | `1116.50` | 11,860,000.00 USD | 116,120.00 USD | 0.00 USD | `+58.90%` | `104,000,000,000.00` |
| `Live` | `Short` | `1118.50` | 11,860,000.00 USD | 351.21 USD | 0.00 USD | `+59.19%` | `314,000,000.00` |
| `Live` | `Short` | `1123.50` | 11,920,000.00 USD | 60,740.00 USD | 0.00 USD | `+59.90%` | `54,065,000,000.00` |
| `Live` | `Short` | `1130.50` | 11,920,000.00 USD | 151.49 USD | 0.00 USD | `+60.90%` | `134,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,270,000.00 USD | 341,250.00 USD | 0.00 USD | `+61.89%` | `300,000,000,000.00` |
| `Live` | `Short` | `1138.50` | 12,270,000.00 USD | 1,520.00 USD | 0.00 USD | `+62.03%` | `1,337,000,000.00` |
| `Live` | `Short` | `1146.50` | 12,270,000.00 USD | 119.24 USD | 0.00 USD | `+63.17%` | `104,000,000.00` |
| `Live` | `Short` | `1151.50` | 12,280,000.00 USD | 11,690.00 USD | 0.00 USD | `+63.88%` | `10,154,000,000.00` |
| `Live` | `Short` | `1152.50` | 12,280,000.00 USD | 4,940.00 USD | 0.00 USD | `+64.03%` | `4,284,000,000.00` |
| `Live` | `Short` | `1154.50` | 12,290,000.00 USD | 8,180.00 USD | 0.00 USD | `+64.31%` | `7,082,000,000.00` |
| `Live` | `Short` | `1162.50` | 12,290,000.00 USD | 155.78 USD | 0.00 USD | `+65.45%` | `134,000,000.00` |
| `Live` | `Short` | `1175.50` | 12,310,000.00 USD | 20,410.00 USD | 0.00 USD | `+67.30%` | `17,363,000,000.00` |
| `Live` | `Short` | `1176.50` | 12,310,000.00 USD | 356.48 USD | 0.00 USD | `+67.44%` | `303,000,000.00` |
| `Live` | `Short` | `1179.50` | 12,400,000.00 USD | 82,770.00 USD | 0.00 USD | `+67.87%` | `70,177,000,000.00` |
| `Live` | `Short` | `1184.50` | 12,400,000.00 USD | 561.45 USD | 0.00 USD | `+68.58%` | `474,000,000.00` |
| `Live` | `Short` | `1190.50` | 12,400,000.00 USD | 167.86 USD | 0.00 USD | `+69.43%` | `141,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,400,000.00 USD | 463.43 USD | 0.00 USD | `+70.43%` | `387,000,000.00` |
| `Live` | `Short` | `1203.50` | 12,520,000.00 USD | 118,860.00 USD | 0.00 USD | `+71.29%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,520,000.00 USD | 385.19 USD | 0.00 USD | `+71.85%` | `319,000,000.00` |
| `Live` | `Short` | `1209.50` | 12,550,000.00 USD | 30,220.00 USD | 0.00 USD | `+72.14%` | `24,982,000,000.00` |
| `Live` | `Short` | `1218.50` | 12,590,000.00 USD | 43,870.00 USD | 0.00 USD | `+73.42%` | `36,000,000,000.00` |
| `Live` | `Short` | `1223.50` | 13,200,000.00 USD | 606,150.00 USD | 0.00 USD | `+74.13%` | `495,423,000,000.00` |
| `Live` | `Short` | `1224.50` | 13,200,000.00 USD | 4,750.00 USD | 0.00 USD | `+74.27%` | `3,876,000,000.00` |
| `Live` | `Short` | `1233.50` | 13,260,000.00 USD | 59,590.00 USD | 0.00 USD | `+75.55%` | `48,311,000,000.00` |
| `Live` | `Short` | `1245.50` | 13,260,000.00 USD | 102.13 USD | 0.00 USD | `+77.26%` | `82,000,000.00` |
| `Live` | `Short` | `1246.50` | 13,270,000.00 USD | 6,750.00 USD | 0.00 USD | `+77.40%` | `5,419,000,000.00` |
| `Live` | `Short` | `1247.50` | 13,270,000.00 USD | 2,660.00 USD | 0.00 USD | `+77.55%` | `2,134,000,000.00` |
| `Live` | `Short` | `1251.50` | 13,270,000.00 USD | 300.36 USD | 0.00 USD | `+78.12%` | `240,000,000.00` |
| `Live` | `Short` | `1253.50` | 13,300,000.00 USD | 24,340.00 USD | 0.00 USD | `+78.40%` | `19,414,000,000.00` |
| `Live` | `Short` | `1259.50` | 13,410,000.00 USD | 113,360.00 USD | 0.00 USD | `+79.26%` | `90,000,000,000.00` |
| `Live` | `Short` | `1266.50` | 13,410,000.00 USD | 901.75 USD | 0.00 USD | `+80.25%` | `712,000,000.00` |
| `Live` | `Short` | `1272.50` | 13,410,000.00 USD | 5,080.00 USD | 0.00 USD | `+81.11%` | `3,994,000,000.00` |
| `Live` | `Short` | `1278.50` | 13,440,000.00 USD | 25,570.00 USD | 0.00 USD | `+81.96%` | `20,000,000,000.00` |
| `Live` | `Short` | `1286.50` | 13,500,000.00 USD | 61,910.00 USD | 0.00 USD | `+83.10%` | `48,123,000,000.00` |
| `Live` | `Short` | `1288.50` | 13,500,000.00 USD | 349.18 USD | 0.00 USD | `+83.38%` | `271,000,000.00` |
| `Live` | `Short` | `1289.50` | 13,520,000.00 USD | 21,380.00 USD | 0.00 USD | `+83.52%` | `16,583,000,000.00` |
| `Live` | `Short` | `1295.50` | 13,520,000.00 USD | 181.37 USD | 0.00 USD | `+84.38%` | `140,000,000.00` |
| `Live` | `Short` | `1298.50` | 13,630,000.00 USD | 110,770.00 USD | 0.00 USD | `+84.81%` | `85,305,000,000.00` |
| `Live` | `Short` | `1301.50` | 13,640,000.00 USD | 4,020.00 USD | 0.00 USD | `+85.23%` | `3,092,000,000.00` |
| `Live` | `Short` | `1303.50` | 13,640,000.00 USD | 100.37 USD | 0.00 USD | `+85.52%` | `77,000,000.00` |
| `Live` | `Short` | `1306.50` | 15,480,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+85.94%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1309.50` | 15,650,000.00 USD | 166,150.00 USD | 0.00 USD | `+86.37%` | `126,881,000,000.00` |
| `Live` | `Short` | `1311.50` | 15,670,000.00 USD | 18,450.00 USD | 0.00 USD | `+86.66%` | `14,070,000,000.00` |
| `Live` | `Short` | `1316.50` | 15,700,000.00 USD | 30,280.00 USD | 0.00 USD | `+87.37%` | `23,000,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,710,000.00 USD | 14,130.00 USD | 0.00 USD | `+87.79%` | `10,710,000,000.00` |
| `Live` | `Short` | `1322.50` | 15,710,000.00 USD | 208.96 USD | 0.00 USD | `+88.22%` | `158,000,000.00` |
| `Live` | `Short` | `1325.50` | 15,720,000.00 USD | 2,650.00 USD | 0.00 USD | `+88.65%` | `2,000,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,720,000.00 USD | 242.93 USD | 0.00 USD | `+88.93%` | `183,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,720,000.00 USD | 184.66 USD | 0.00 USD | `+89.08%` | `139,000,000.00` |
| `Live` | `Short` | `1329.50` | 15,730,000.00 USD | 13,220.00 USD | 0.00 USD | `+89.22%` | `9,946,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,760,000.00 USD | 25,340.00 USD | 0.00 USD | `+89.36%` | `19,049,000,000.00` |
| `Live` | `Short` | `1339.50` | 15,760,000.00 USD | 494.28 USD | 0.00 USD | `+90.64%` | `369,000,000.00` |
| `Live` | `Short` | `1347.50` | 15,760,000.00 USD | 233.12 USD | 0.00 USD | `+91.78%` | `173,000,000.00` |
| `Live` | `Short` | `1349.50` | 15,760,000.00 USD | 4,220.00 USD | 0.00 USD | `+92.06%` | `3,130,000,000.00` |
| `Live` | `Short` | `1352.50` | 15,850,000.00 USD | 87,910.00 USD | 0.00 USD | `+92.49%` | `65,000,000,000.00` |
| `Live` | `Short` | `1354.50` | 15,850,000.00 USD | 3,850.00 USD | 0.00 USD | `+92.78%` | `2,846,000,000.00` |
| `Live` | `Short` | `1359.50` | 15,850,000.00 USD | 121.00 USD | 0.00 USD | `+93.49%` | `89,000,000.00` |
| `Live` | `Short` | `1363.50` | 15,860,000.00 USD | 6,820.00 USD | 0.00 USD | `+94.06%` | `5,000,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,860,000.00 USD | 761.70 USD | 0.00 USD | `+94.63%` | `557,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,910,000.00 USD | 46,880.00 USD | 0.00 USD | `+94.91%` | `34,232,000,000.00` |
| `Live` | `Short` | `1373.50` | 15,910,000.00 USD | 4,120.00 USD | 0.00 USD | `+95.48%` | `3,000,000,000.00` |
| `Live` | `Short` | `1384.50` | 15,980,000.00 USD | 69,220.00 USD | 0.00 USD | `+97.05%` | `50,000,000,000.00` |
| `Live` | `Short` | `1385.50` | 15,980,000.00 USD | 508.48 USD | 0.00 USD | `+97.19%` | `367,000,000.00` |
| `Live` | `Short` | `1389.50` | 15,990,000.00 USD | 4,800.00 USD | 0.00 USD | `+97.76%` | `3,457,000,000.00` |
| `Live` | `Short` | `1399.50` | 15,990,000.00 USD | 3,980.00 USD | 0.00 USD | `+99.18%` | `2,844,000,000.00` |
| `Live` | `Short` | `1403.50` | 16,240,000.00 USD | 252,630.00 USD | 0.00 USD | `+99.75%` | `180,000,000,000.00` |
| `Live` | `Short` | `1405.50` | 16,250,000.00 USD | 4,770.00 USD | 0.00 USD | `+100.03%` | `3,392,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 3,150,000.00 USD | 0.00 USD | 475.73 USD | `-78.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `288.50` | 3,150,000.00 USD | 0.00 USD | 1,310.00 USD | `-58.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 3,150,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 3,150,000.00 USD | 0.00 USD | 333.50 USD | `-52.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 3,150,000.00 USD | 0.00 USD | 8,140.00 USD | `-48.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 3,140,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 3,140,000.00 USD | 0.00 USD | 17,290.00 USD | `-43.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 3,120,000.00 USD | 0.00 USD | 25,210.00 USD | `-41.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 3,090,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 3,090,000.00 USD | 0.00 USD | 8,180.00 USD | `-39.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 3,080,000.00 USD | 0.00 USD | 173.83 USD | `-38.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 3,080,000.00 USD | 0.00 USD | 2,210.00 USD | `-36.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `450.50` | 3,080,000.00 USD | 0.00 USD | 4,660.00 USD | `-35.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 3,070,000.00 USD | 0.00 USD | 698.74 USD | `-35.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 3,070,000.00 USD | 0.00 USD | 2,270.00 USD | `-35.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `457.50` | 3,070,000.00 USD | 0.00 USD | 2,270.00 USD | `-34.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 3,070,000.00 USD | 0.00 USD | 1,750.00 USD | `-34.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 3,070,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `484.50` | 3,060,000.00 USD | 0.00 USD | 100.29 USD | `-31.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `485.50` | 3,060,000.00 USD | 0.00 USD | 100.50 USD | `-30.90%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 3,060,000.00 USD | 0.00 USD | 100.71 USD | `-30.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 3,060,000.00 USD | 0.00 USD | 6,600.00 USD | `-30.62%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 3,060,000.00 USD | 0.00 USD | 125.06 USD | `-30.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `490.50` | 3,060,000.00 USD | 0.00 USD | 101.53 USD | `-30.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 3,060,000.00 USD | 0.00 USD | 2,450.00 USD | `-29.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `495.50` | 3,050,000.00 USD | 0.00 USD | 102.57 USD | `-29.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 3,050,000.00 USD | 0.00 USD | 163.01 USD | `-29.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 3,050,000.00 USD | 0.00 USD | 214.78 USD | `-28.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 3,050,000.00 USD | 0.00 USD | 23,300.00 USD | `-28.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 3,030,000.00 USD | 0.00 USD | 42,390.00 USD | `-28.34%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 2,990,000.00 USD | 0.00 USD | 138.78 USD | `-27.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 2,990,000.00 USD | 0.00 USD | 185.97 USD | `-27.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 2,990,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 2,990,000.00 USD | 0.00 USD | 125.51 USD | `-26.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 2,990,000.00 USD | 0.00 USD | 280.49 USD | `-26.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 2,990,000.00 USD | 0.00 USD | 258.14 USD | `-25.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 2,990,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 2,980,000.00 USD | 0.00 USD | 485.16 USD | `-24.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 2,980,000.00 USD | 0.00 USD | 4,650.00 USD | `-23.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 2,970,000.00 USD | 0.00 USD | 2,270.00 USD | `-23.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 2,970,000.00 USD | 0.00 USD | 864.80 USD | `-23.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `547.50` | 2,970,000.00 USD | 0.00 USD | 248.56 USD | `-22.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 2,970,000.00 USD | 0.00 USD | 125,240.00 USD | `-21.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 2,840,000.00 USD | 0.00 USD | 366,230.00 USD | `-21.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,480,000.00 USD | 0.00 USD | 1,190.00 USD | `-21.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,480,000.00 USD | 0.00 USD | 611.05 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,480,000.00 USD | 0.00 USD | 213.52 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,480,000.00 USD | 0.00 USD | 51,260.00 USD | `-20.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,420,000.00 USD | 0.00 USD | 292.02 USD | `-20.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 2,420,000.00 USD | 0.00 USD | 199.12 USD | `-19.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 2,420,000.00 USD | 0.00 USD | 808.06 USD | `-19.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,420,000.00 USD | 0.00 USD | 566.50 USD | `-19.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,420,000.00 USD | 0.00 USD | 126.55 USD | `-19.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,420,000.00 USD | 0.00 USD | 5,680.00 USD | `-19.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 2,420,000.00 USD | 0.00 USD | 569.50 USD | `-18.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,420,000.00 USD | 0.00 USD | 774.17 USD | `-18.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,420,000.00 USD | 0.00 USD | 1,700.00 USD | `-18.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,410,000.00 USD | 0.00 USD | 291.91 USD | `-18.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,410,000.00 USD | 0.00 USD | 469.61 USD | `-18.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,410,000.00 USD | 0.00 USD | 289.98 USD | `-17.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,410,000.00 USD | 0.00 USD | 285.86 USD | `-17.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,410,000.00 USD | 0.00 USD | 289.17 USD | `-17.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,410,000.00 USD | 0.00 USD | 6,750.00 USD | `-17.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,410,000.00 USD | 0.00 USD | 1,240.00 USD | `-17.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 2,400,000.00 USD | 0.00 USD | 6,980.00 USD | `-17.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,400,000.00 USD | 0.00 USD | 287.67 USD | `-16.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,400,000.00 USD | 0.00 USD | 763.94 USD | `-16.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,400,000.00 USD | 0.00 USD | 542.76 USD | `-16.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,400,000.00 USD | 0.00 USD | 34,020.00 USD | `-16.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,360,000.00 USD | 0.00 USD | 830,190.00 USD | `-16.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,530,000.00 USD | 0.00 USD | 1,220.00 USD | `-16.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,530,000.00 USD | 0.00 USD | 540.31 USD | `-15.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 1,530,000.00 USD | 0.00 USD | 109.43 USD | `-15.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,530,000.00 USD | 0.00 USD | 698.56 USD | `-15.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 1,530,000.00 USD | 0.00 USD | 1,160.00 USD | `-15.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 1,530,000.00 USD | 0.00 USD | 119.30 USD | `-15.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 1,530,000.00 USD | 0.00 USD | 222.87 USD | `-14.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,530,000.00 USD | 0.00 USD | 244.79 USD | `-14.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `599.50` | 1,530,000.00 USD | 0.00 USD | 145.68 USD | `-14.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,530,000.00 USD | 0.00 USD | 41,660.00 USD | `-14.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 1,490,000.00 USD | 0.00 USD | 1,590.00 USD | `-14.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,480,000.00 USD | 0.00 USD | 46,760.00 USD | `-14.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 1,440,000.00 USD | 0.00 USD | 937.84 USD | `-14.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,440,000.00 USD | 0.00 USD | 1,870.00 USD | `-13.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,430,000.00 USD | 0.00 USD | 8,040.00 USD | `-13.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 1,430,000.00 USD | 0.00 USD | 18,380.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 1,410,000.00 USD | 0.00 USD | 30,480.00 USD | `-13.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 1,380,000.00 USD | 0.00 USD | 7,790.00 USD | `-13.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,370,000.00 USD | 0.00 USD | 4,470.00 USD | `-12.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,370,000.00 USD | 0.00 USD | 269.15 USD | `-12.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,360,000.00 USD | 0.00 USD | 2,380.00 USD | `-12.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,360,000.00 USD | 0.00 USD | 120.83 USD | `-12.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,360,000.00 USD | 0.00 USD | 8,670.00 USD | `-11.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 1,350,000.00 USD | 0.00 USD | 1,980.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 1,350,000.00 USD | 0.00 USD | 219.47 USD | `-11.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 1,350,000.00 USD | 0.00 USD | 445.27 USD | `-11.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,350,000.00 USD | 0.00 USD | 445.98 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 1,350,000.00 USD | 0.00 USD | 694.79 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 1,350,000.00 USD | 0.00 USD | 916.15 USD | `-10.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 1,350,000.00 USD | 0.00 USD | 746.03 USD | `-10.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 1,350,000.00 USD | 0.00 USD | 2,740.00 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,350,000.00 USD | 0.00 USD | 861.26 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 1,340,000.00 USD | 0.00 USD | 179.98 USD | `-10.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 1,340,000.00 USD | 0.00 USD | 4,900.00 USD | `-9.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,340,000.00 USD | 0.00 USD | 164.08 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 1,340,000.00 USD | 0.00 USD | 6,760.00 USD | `-9.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 1,330,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,330,000.00 USD | 0.00 USD | 3,640.00 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 1,330,000.00 USD | 0.00 USD | 384.98 USD | `-8.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 1,330,000.00 USD | 0.00 USD | 429.78 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 1,330,000.00 USD | 0.00 USD | 352.18 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 1,330,000.00 USD | 0.00 USD | 357.87 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 1,320,000.00 USD | 0.00 USD | 1,980.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 1,320,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,320,000.00 USD | 0.00 USD | 8,850.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,310,000.00 USD | 0.00 USD | 971.04 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 1,310,000.00 USD | 0.00 USD | 1,800.00 USD | `-7.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,310,000.00 USD | 0.00 USD | 107.17 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,310,000.00 USD | 0.00 USD | 28,620.00 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,280,000.00 USD | 0.00 USD | 5,890.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,270,000.00 USD | 0.00 USD | 2,020.00 USD | `-6.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,270,000.00 USD | 0.00 USD | 308.92 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 1,270,000.00 USD | 0.00 USD | 633.21 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,270,000.00 USD | 0.00 USD | 456.27 USD | `-6.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,270,000.00 USD | 0.00 USD | 110.46 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 1,270,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,270,000.00 USD | 0.00 USD | 13,060.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,250,000.00 USD | 0.00 USD | 567.37 USD | `-6.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 1,250,000.00 USD | 0.00 USD | 11,670.00 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,240,000.00 USD | 0.00 USD | 5,480.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 1,240,000.00 USD | 0.00 USD | 4,040.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 1,230,000.00 USD | 0.00 USD | 818.00 USD | `-5.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 1,230,000.00 USD | 0.00 USD | 576.32 USD | `-5.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,230,000.00 USD | 0.00 USD | 24,530.00 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 1,210,000.00 USD | 0.00 USD | 1,140.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 1,210,000.00 USD | 0.00 USD | 719.97 USD | `-4.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,210,000.00 USD | 0.00 USD | 2,390.00 USD | `-4.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,200,000.00 USD | 0.00 USD | 135,800.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 1,070,000.00 USD | 0.00 USD | 4,020.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,060,000.00 USD | 0.00 USD | 67,140.00 USD | `-4.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 996,070.00 USD | 0.00 USD | 3,460.00 USD | `-4.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 992,610.00 USD | 0.00 USD | 1,470.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 991,130.00 USD | 0.00 USD | 9,450.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 981,680.00 USD | 0.00 USD | 56,170.00 USD | `-3.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 925,510.00 USD | 0.00 USD | 41,960.00 USD | `-3.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 883,550.00 USD | 0.00 USD | 825.73 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 882,730.00 USD | 0.00 USD | 99,720.00 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 783,000.00 USD | 0.00 USD | 9,670.00 USD | `-3.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 773,340.00 USD | 0.00 USD | 3,290.00 USD | `-3.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 770,050.00 USD | 0.00 USD | 5,290.00 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 764,750.00 USD | 0.00 USD | 171,850.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 592,910.00 USD | 0.00 USD | 171,120.00 USD | `-2.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 421,780.00 USD | 0.00 USD | 11,030.00 USD | `-2.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 410,760.00 USD | 0.00 USD | 1,780.00 USD | `-2.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 408,980.00 USD | 0.00 USD | 323.12 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 408,650.00 USD | 0.00 USD | 382.81 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 408,270.00 USD | 0.00 USD | 996.33 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 407,270.00 USD | 0.00 USD | 77,140.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 330,130.00 USD | 0.00 USD | 177,090.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 153,040.00 USD | 0.00 USD | 4,450.00 USD | `-1.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 148,590.00 USD | 0.00 USD | 990.32 USD | `-1.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 147,600.00 USD | 0.00 USD | 1,540.00 USD | `-1.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 146,060.00 USD | 0.00 USD | 718.45 USD | `-1.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 145,350.00 USD | 0.00 USD | 9,290.00 USD | `-0.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 136,060.00 USD | 0.00 USD | 47,550.00 USD | `-0.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 88,510.00 USD | 0.00 USD | 291.97 USD | `-0.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 88,220.00 USD | 0.00 USD | 38,470.00 USD | `-0.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 49,750.00 USD | 0.00 USD | 42,040.00 USD | `-0.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 7,710.00 USD | 0.00 USD | 681.16 USD | `-0.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 7,030.00 USD | 0.00 USD | 7,030.00 USD | `-0.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `703.50` | 1,990.00 USD | 1,990.00 USD | 0.00 USD | `+0.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `704.50` | 7,470.00 USD | 5,480.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `705.50` | 15,850.00 USD | 8,370.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `706.50` | 19,690.00 USD | 3,840.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 37,370.00 USD | 17,690.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 38,190.00 USD | 812.65 USD | 0.00 USD | `+0.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 61,550.00 USD | 23,370.00 USD | 0.00 USD | `+0.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 61,980.00 USD | 422.04 USD | 0.00 USD | `+1.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 94,400.00 USD | 32,430.00 USD | 0.00 USD | `+1.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 106,430.00 USD | 12,030.00 USD | 0.00 USD | `+1.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 107,250.00 USD | 822.67 USD | 0.00 USD | `+1.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 107,730.00 USD | 474.43 USD | 0.00 USD | `+1.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 107,960.00 USD | 228.24 USD | 0.00 USD | `+1.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 109,040.00 USD | 1,090.00 USD | 0.00 USD | `+1.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 116,620.00 USD | 7,580.00 USD | 0.00 USD | `+2.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 177,300.00 USD | 60,670.00 USD | 0.00 USD | `+2.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 181,940.00 USD | 4,650.00 USD | 0.00 USD | `+2.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 182,840.00 USD | 891.98 USD | 0.00 USD | `+2.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 236,520.00 USD | 53,690.00 USD | 0.00 USD | `+2.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 247,180.00 USD | 10,650.00 USD | 0.00 USD | `+2.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 258,470.00 USD | 11,290.00 USD | 0.00 USD | `+2.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 283,960.00 USD | 25,500.00 USD | 0.00 USD | `+3.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 376,720.00 USD | 92,760.00 USD | 0.00 USD | `+3.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 377,000.00 USD | 279.70 USD | 0.00 USD | `+3.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 395,670.00 USD | 18,670.00 USD | 0.00 USD | `+3.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 427,330.00 USD | 31,660.00 USD | 0.00 USD | `+3.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 594,870.00 USD | 167,540.00 USD | 0.00 USD | `+3.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 598,760.00 USD | 3,900.00 USD | 0.00 USD | `+3.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 797,510.00 USD | 198,750.00 USD | 0.00 USD | `+4.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 799,270.00 USD | 1,760.00 USD | 0.00 USD | `+4.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,290,000.00 USD | 487,680.00 USD | 0.00 USD | `+4.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,290,000.00 USD | 5,190.00 USD | 0.00 USD | `+4.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,320,000.00 USD | 23,100.00 USD | 0.00 USD | `+4.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,320,000.00 USD | 5,760.00 USD | 0.00 USD | `+4.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,320,000.00 USD | 685.88 USD | 0.00 USD | `+4.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,340,000.00 USD | 13,480.00 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,340,000.00 USD | 3,420.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,350,000.00 USD | 10,870.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,350,000.00 USD | 3,960.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,370,000.00 USD | 17,990.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,380,000.00 USD | 8,280.00 USD | 0.00 USD | `+5.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,580,000.00 USD | 203,810.00 USD | 0.00 USD | `+5.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,590,000.00 USD | 7,210.00 USD | 0.00 USD | `+6.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,670,000.00 USD | 76,650.00 USD | 0.00 USD | `+6.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,670,000.00 USD | 1,240.00 USD | 0.00 USD | `+6.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,670,000.00 USD | 279.19 USD | 0.00 USD | `+6.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,670,000.00 USD | 601.10 USD | 0.00 USD | `+6.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,670,000.00 USD | 123.83 USD | 0.00 USD | `+6.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,680,000.00 USD | 8,990.00 USD | 0.00 USD | `+6.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,680,000.00 USD | 2,730.00 USD | 0.00 USD | `+7.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,680,000.00 USD | 629.17 USD | 0.00 USD | `+7.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,730,000.00 USD | 47,160.00 USD | 0.00 USD | `+7.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,730,000.00 USD | 4,420.00 USD | 0.00 USD | `+7.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,740,000.00 USD | 10,340.00 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,890,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,890,000.00 USD | 904.13 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 1,890,000.00 USD | 325.07 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,180,000.00 USD | 287,930.00 USD | 0.00 USD | `+8.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,190,000.00 USD | 11,460.00 USD | 0.00 USD | `+8.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,190,000.00 USD | 239.43 USD | 0.00 USD | `+8.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,210,000.00 USD | 26,620.00 USD | 0.00 USD | `+8.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,210,000.00 USD | 240.05 USD | 0.00 USD | `+8.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,280,000.00 USD | 60,710.00 USD | 0.00 USD | `+8.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,280,000.00 USD | 331.13 USD | 0.00 USD | `+9.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,740,000.00 USD | 468,310.00 USD | 0.00 USD | `+9.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,740,000.00 USD | 180.60 USD | 0.00 USD | `+9.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,740,000.00 USD | 171.60 USD | 0.00 USD | `+9.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,750,000.00 USD | 1,540.00 USD | 0.00 USD | `+9.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,750,000.00 USD | 242.25 USD | 0.00 USD | `+9.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,760,000.00 USD | 12,400.00 USD | 0.00 USD | `+9.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,760,000.00 USD | 656.70 USD | 0.00 USD | `+10.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,770,000.00 USD | 9,680.00 USD | 0.00 USD | `+10.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,770,000.00 USD | 4,570.00 USD | 0.00 USD | `+10.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,790,000.00 USD | 14,230.00 USD | 0.00 USD | `+10.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,800,000.00 USD | 15,690.00 USD | 0.00 USD | `+10.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,810,000.00 USD | 9,990.00 USD | 0.00 USD | `+10.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,810,000.00 USD | 132.52 USD | 0.00 USD | `+10.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,840,000.00 USD | 24,280.00 USD | 0.00 USD | `+11.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,840,000.00 USD | 2,050.00 USD | 0.00 USD | `+11.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,840,000.00 USD | 1,900.00 USD | 0.00 USD | `+11.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,840,000.00 USD | 101.07 USD | 0.00 USD | `+11.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,840,000.00 USD | 102.77 USD | 0.00 USD | `+11.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,840,000.00 USD | 559.28 USD | 0.00 USD | `+11.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,850,000.00 USD | 5,610.00 USD | 0.00 USD | `+11.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,850,000.00 USD | 2,260.00 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,850,000.00 USD | 133.26 USD | 0.00 USD | `+12.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,870,000.00 USD | 15,770.00 USD | 0.00 USD | `+12.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,870,000.00 USD | 704.44 USD | 0.00 USD | `+12.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,870,000.00 USD | 4,360.00 USD | 0.00 USD | `+12.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,870,000.00 USD | 1,450.00 USD | 0.00 USD | `+12.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,880,000.00 USD | 3,630.00 USD | 0.00 USD | `+13.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,880,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,880,000.00 USD | 154.52 USD | 0.00 USD | `+13.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `798.50` | 2,890,000.00 USD | 7,140.00 USD | 0.00 USD | `+13.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,890,000.00 USD | 1,260.00 USD | 0.00 USD | `+13.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,910,000.00 USD | 25,190.00 USD | 0.00 USD | `+13.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,910,000.00 USD | 120.22 USD | 0.00 USD | `+14.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,910,000.00 USD | 803.50 USD | 0.00 USD | `+14.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,910,000.00 USD | 120.02 USD | 0.00 USD | `+14.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,920,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,920,000.00 USD | 5,010.00 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,920,000.00 USD | 242.04 USD | 0.00 USD | `+15.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 2,920,000.00 USD | 3,440.00 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 2,920,000.00 USD | 374.10 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 2,930,000.00 USD | 844.19 USD | 0.00 USD | `+15.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 2,930,000.00 USD | 118.77 USD | 0.00 USD | `+15.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 2,930,000.00 USD | 3,390.00 USD | 0.00 USD | `+15.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 2,930,000.00 USD | 984.70 USD | 0.00 USD | `+16.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 2,930,000.00 USD | 162.68 USD | 0.00 USD | `+16.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 2,940,000.00 USD | 5,990.00 USD | 0.00 USD | `+16.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 2,940,000.00 USD | 7,820.00 USD | 0.00 USD | `+16.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 2,940,000.00 USD | 408.13 USD | 0.00 USD | `+17.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 2,950,000.00 USD | 672.77 USD | 0.00 USD | `+17.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 2,950,000.00 USD | 276.38 USD | 0.00 USD | `+17.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 2,950,000.00 USD | 1,800.00 USD | 0.00 USD | `+17.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 2,980,000.00 USD | 35,850.00 USD | 0.00 USD | `+18.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 2,980,000.00 USD | 1,050.00 USD | 0.00 USD | `+18.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 2,980,000.00 USD | 187.15 USD | 0.00 USD | `+18.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 2,980,000.00 USD | 372.24 USD | 0.00 USD | `+19.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 2,990,000.00 USD | 326.62 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 2,990,000.00 USD | 296.34 USD | 0.00 USD | `+19.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 2,990,000.00 USD | 5,040.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 2,990,000.00 USD | 329.87 USD | 0.00 USD | `+19.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 2,990,000.00 USD | 425.97 USD | 0.00 USD | `+20.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 2,990,000.00 USD | 1,770.00 USD | 0.00 USD | `+20.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 3,000,000.00 USD | 2,550.00 USD | 0.00 USD | `+21.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 3,010,000.00 USD | 11,650.00 USD | 0.00 USD | `+21.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 3,010,000.00 USD | 137.57 USD | 0.00 USD | `+21.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 3,010,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 3,010,000.00 USD | 1,160.00 USD | 0.00 USD | `+22.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 3,010,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 3,010,000.00 USD | 874.73 USD | 0.00 USD | `+22.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 3,010,000.00 USD | 2,970.00 USD | 0.00 USD | `+23.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 3,020,000.00 USD | 3,460.00 USD | 0.00 USD | `+23.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 3,020,000.00 USD | 2,610.00 USD | 0.00 USD | `+23.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 3,020,000.00 USD | 228.07 USD | 0.00 USD | `+23.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 3,020,000.00 USD | 1,110.00 USD | 0.00 USD | `+24.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,080,000.00 USD | 54,820.00 USD | 0.00 USD | `+25.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,080,000.00 USD | 266.55 USD | 0.00 USD | `+26.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,080,000.00 USD | 390.93 USD | 0.00 USD | `+26.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,080,000.00 USD | 605.33 USD | 0.00 USD | `+26.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `895.50` | 3,080,000.00 USD | 130.74 USD | 0.00 USD | `+27.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `898.50` | 3,080,000.00 USD | 101.53 USD | 0.00 USD | `+27.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,200,000.00 USD | 126,250.00 USD | 0.00 USD | `+28.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,200,000.00 USD | 167.33 USD | 0.00 USD | `+28.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,210,000.00 USD | 1,640.00 USD | 0.00 USD | `+29.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,210,000.00 USD | 770.99 USD | 0.00 USD | `+30.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,210,000.00 USD | 4,150.00 USD | 0.00 USD | `+30.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,210,000.00 USD | 533.99 USD | 0.00 USD | `+30.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,210,000.00 USD | 463.01 USD | 0.00 USD | `+31.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,210,000.00 USD | 320.57 USD | 0.00 USD | `+31.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,210,000.00 USD | 552.72 USD | 0.00 USD | `+32.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,210,000.00 USD | 196.03 USD | 0.00 USD | `+32.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,210,000.00 USD | 287.20 USD | 0.00 USD | `+33.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,210,000.00 USD | 890.45 USD | 0.00 USD | `+36.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,220,000.00 USD | 498.94 USD | 0.00 USD | `+36.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,220,000.00 USD | 964.50 USD | 0.00 USD | `+37.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,220,000.00 USD | 1,930.00 USD | 0.00 USD | `+37.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,220,000.00 USD | 293.25 USD | 0.00 USD | `+39.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,220,000.00 USD | 1,300.00 USD | 0.00 USD | `+39.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,220,000.00 USD | 109.93 USD | 0.00 USD | `+39.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,220,000.00 USD | 439.09 USD | 0.00 USD | `+40.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,220,000.00 USD | 2,590.00 USD | 0.00 USD | `+40.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,220,000.00 USD | 145.34 USD | 0.00 USD | `+41.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,220,000.00 USD | 1,780.00 USD | 0.00 USD | `+41.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,230,000.00 USD | 3,990.00 USD | 0.00 USD | `+42.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,230,000.00 USD | 938.53 USD | 0.00 USD | `+42.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,240,000.00 USD | 11,810.00 USD | 0.00 USD | `+42.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,240,000.00 USD | 203.50 USD | 0.00 USD | `+44.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,240,000.00 USD | 148.99 USD | 0.00 USD | `+45.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,240,000.00 USD | 149.87 USD | 0.00 USD | `+46.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,240,000.00 USD | 150.45 USD | 0.00 USD | `+46.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,240,000.00 USD | 195.51 USD | 0.00 USD | `+48.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,240,000.00 USD | 149.60 USD | 0.00 USD | `+49.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,240,000.00 USD | 156.58 USD | 0.00 USD | `+52.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,240,000.00 USD | 278.43 USD | 0.00 USD | `+56.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,240,000.00 USD | 555.75 USD | 0.00 USD | `+58.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,240,000.00 USD | 165.93 USD | 0.00 USD | `+61.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,240,000.00 USD | 167.39 USD | 0.00 USD | `+63.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,310,000.00 USD | 62,330.00 USD | 0.00 USD | `+70.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,310,000.00 USD | 1,250.00 USD | 0.00 USD | `+71.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,310,000.00 USD | 235.49 USD | 0.00 USD | `+74.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,310,000.00 USD | 3,580.00 USD | 0.00 USD | `+75.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,310,000.00 USD | 421.42 USD | 0.00 USD | `+77.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,320,000.00 USD | 3,750.00 USD | 0.00 USD | `+82.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,320,000.00 USD | 133.64 USD | 0.00 USD | `+84.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,320,000.00 USD | 685.36 USD | 0.00 USD | `+85.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,370,000.00 USD | 58,230.00 USD | 0.00 USD | `+89.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,460,000.00 USD | 80,850.00 USD | 0.00 USD | `+90.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,460,000.00 USD | 6,210.00 USD | 0.00 USD | `+93.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,460,000.00 USD | 349.06 USD | 0.00 USD | `+94.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,460,000.00 USD | 1,060.00 USD | 0.00 USD | `+95.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,480,000.00 USD | 19,210.00 USD | 0.00 USD | `+95.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,480,000.00 USD | 425.19 USD | 0.00 USD | `+97.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,490,000.00 USD | 3,850.00 USD | 0.00 USD | `+99.32%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `620.80` | 40,560,000.00 USD | 0.00 USD | 40,560,000.00 USD | 0.00 USD | 0.00 USD | 265,620.00 USD |
| `7D` | `621.70` | 40,290,000.00 USD | 0.00 USD | 40,290,000.00 USD | 310,160.00 USD | 55,460.00 USD | 0.00 USD |
| `7D` | `626.20` | 39,920,000.00 USD | 0.00 USD | 39,920,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `628.90` | 39,880,000.00 USD | 0.00 USD | 39,880,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `629.80` | 39,620,000.00 USD | 0.00 USD | 39,620,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD |
| `1D` | `630.70` | 54,730,000.00 USD | 0.00 USD | 54,730,000.00 USD | 52,660.00 USD | 26,750.00 USD | 382,570.00 USD |
| `7D` | `630.70` | 39,360,000.00 USD | 0.00 USD | 39,360,000.00 USD | 0.00 USD | 50,030.00 USD | 0.00 USD |
| `1D` | `631.50` | 54,260,000.00 USD | 0.00 USD | 54,260,000.00 USD | 73,890.00 USD | 103,360.00 USD | 604,560.00 USD |
| `7D` | `631.60` | 39,310,000.00 USD | 0.00 USD | 39,310,000.00 USD | 289,390.00 USD | 113,090.00 USD | 53,970.00 USD |
| `1D` | `632.30` | 53,480,000.00 USD | 0.00 USD | 53,480,000.00 USD | 564,850.00 USD | 86,460.00 USD | 135,460.00 USD |
| `7D` | `632.50` | 38,860,000.00 USD | 0.00 USD | 38,860,000.00 USD | 0.00 USD | 13,560.00 USD | 47,990.00 USD |
| `1D` | `633.10` | 52,700,000.00 USD | 0.00 USD | 52,700,000.00 USD | 174,370.00 USD | 11,550.00 USD | 26,530.00 USD |
| `7D` | `633.40` | 38,800,000.00 USD | 0.00 USD | 38,800,000.00 USD | 87,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `633.90` | 52,480,000.00 USD | 0.00 USD | 52,480,000.00 USD | 217,300.00 USD | 37,950.00 USD | 83,560.00 USD |
| `7D` | `634.30` | 38,710,000.00 USD | 0.00 USD | 38,710,000.00 USD | 0.00 USD | 13,860.00 USD | 65,800.00 USD |
| `1D` | `634.70` | 52,140,000.00 USD | 0.00 USD | 52,140,000.00 USD | 39,810.00 USD | 16,410.00 USD | 75,240.00 USD |
| `7D` | `635.20` | 38,630,000.00 USD | 0.00 USD | 38,630,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD |
| `1D` | `635.50` | 52,010,000.00 USD | 0.00 USD | 52,010,000.00 USD | 101,710.00 USD | 9,540.00 USD | 58,120.00 USD |
| `7D` | `636.10` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD |
| `1D` | `636.30` | 51,840,000.00 USD | 0.00 USD | 51,840,000.00 USD | 57,730.00 USD | 56,570.00 USD | 236,370.00 USD |
| `1D` | `637.10` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 136,880.00 USD | 10,320.00 USD | 3,760.00 USD |
| `1D` | `637.90` | 51,340,000.00 USD | 0.00 USD | 51,340,000.00 USD | 59,460.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `638.70` | 51,280,000.00 USD | 0.00 USD | 51,280,000.00 USD | 4,240.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `639.50` | 51,240,000.00 USD | 0.00 USD | 51,240,000.00 USD | 242,510.00 USD | 0.00 USD | 184,710.00 USD |
| `7D` | `640.60` | 38,470,000.00 USD | 0.00 USD | 38,470,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD |
| `1D` | `641.10` | 50,810,000.00 USD | 0.00 USD | 50,810,000.00 USD | 0.00 USD | 0.00 USD | 4,880.00 USD |
| `1D` | `641.90` | 50,810,000.00 USD | 0.00 USD | 50,810,000.00 USD | 230,450.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `642.40` | 38,250,000.00 USD | 0.00 USD | 38,250,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD |
| `1D` | `642.70` | 50,580,000.00 USD | 0.00 USD | 50,580,000.00 USD | 33,090.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `643.30` | 38,210,000.00 USD | 0.00 USD | 38,210,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `643.50` | 50,540,000.00 USD | 0.00 USD | 50,540,000.00 USD | 69,670.00 USD | 6,260.00 USD | 0.00 USD |
| `7D` | `644.20` | 38,030,000.00 USD | 0.00 USD | 38,030,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.30` | 50,470,000.00 USD | 0.00 USD | 50,470,000.00 USD | 393,100.00 USD | 36,890.00 USD | 0.00 USD |
| `1D` | `645.10` | 50,040,000.00 USD | 0.00 USD | 50,040,000.00 USD | 93,740.00 USD | 4,720.00 USD | 341,610.00 USD |
| `7D` | `645.10` | 38,000,000.00 USD | 0.00 USD | 38,000,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD |
| `1D` | `645.90` | 49,600,000.00 USD | 0.00 USD | 49,600,000.00 USD | 79,070.00 USD | 11,780.00 USD | 34,900.00 USD |
| `7D` | `646.00` | 37,970,000.00 USD | 0.00 USD | 37,970,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD |
| `1D` | `646.70` | 49,470,000.00 USD | 0.00 USD | 49,470,000.00 USD | 250,710.00 USD | 2,560.00 USD | 169,060.00 USD |
| `7D` | `646.90` | 37,900,000.00 USD | 0.00 USD | 37,900,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD |
| `1D` | `647.50` | 49,050,000.00 USD | 0.00 USD | 49,050,000.00 USD | 140,910.00 USD | 33,700.00 USD | 21,540.00 USD |
| `7D` | `647.80` | 37,730,000.00 USD | 0.00 USD | 37,730,000.00 USD | 76,970.00 USD | 16,830.00 USD | 14,870.00 USD |
| `1D` | `648.30` | 48,850,000.00 USD | 0.00 USD | 48,850,000.00 USD | 136,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `648.70` | 37,620,000.00 USD | 0.00 USD | 37,620,000.00 USD | 45,630.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `649.10` | 48,720,000.00 USD | 0.00 USD | 48,720,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `649.60` | 37,560,000.00 USD | 0.00 USD | 37,560,000.00 USD | 104,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `649.90` | 48,670,000.00 USD | 0.00 USD | 48,670,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `650.50` | 37,460,000.00 USD | 0.00 USD | 37,460,000.00 USD | 81,630.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `650.70` | 48,600,000.00 USD | 0.00 USD | 48,600,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `651.40` | 37,360,000.00 USD | 0.00 USD | 37,360,000.00 USD | 0.00 USD | 14,650.00 USD | 154,910.00 USD |
| `1D` | `651.50` | 48,590,000.00 USD | 0.00 USD | 48,590,000.00 USD | 167,330.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `652.30` | 48,420,000.00 USD | 0.00 USD | 48,420,000.00 USD | 15,190.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `652.30` | 37,190,000.00 USD | 0.00 USD | 37,190,000.00 USD | 196,170.00 USD | 33,210.00 USD | 0.00 USD |
| `1D` | `653.10` | 48,310,000.00 USD | 0.00 USD | 48,310,000.00 USD | 15,540.00 USD | 26,830.00 USD | 0.00 USD |
| `7D` | `653.20` | 36,960,000.00 USD | 0.00 USD | 36,960,000.00 USD | 109,210.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.90` | 48,270,000.00 USD | 0.00 USD | 48,270,000.00 USD | 56,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `654.70` | 48,210,000.00 USD | 0.00 USD | 48,210,000.00 USD | 143,830.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `655.00` | 36,850,000.00 USD | 0.00 USD | 36,850,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `655.50` | 48,070,000.00 USD | 0.00 USD | 48,070,000.00 USD | 245,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `655.90` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD |
| `1D` | `656.30` | 47,820,000.00 USD | 0.00 USD | 47,820,000.00 USD | 77,320.00 USD | 19,650.00 USD | 825,700.00 USD |
| `7D` | `656.80` | 36,590,000.00 USD | 0.00 USD | 36,590,000.00 USD | 143,550.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `657.10` | 46,900,000.00 USD | 0.00 USD | 46,900,000.00 USD | 187,030.00 USD | 21,320.00 USD | 0.00 USD |
| `7D` | `657.70` | 36,440,000.00 USD | 0.00 USD | 36,440,000.00 USD | 0.00 USD | 7,610.00 USD | 9,210.00 USD |
| `1D` | `657.90` | 46,690,000.00 USD | 0.00 USD | 46,690,000.00 USD | 935,290.00 USD | 14,920.00 USD | 21,320.00 USD |
| `7D` | `658.60` | 36,420,000.00 USD | 0.00 USD | 36,420,000.00 USD | 0.00 USD | 10,650.00 USD | 23,760.00 USD |
| `1D` | `658.70` | 45,720,000.00 USD | 0.00 USD | 45,720,000.00 USD | 171,980.00 USD | 0.00 USD | 81,440.00 USD |
| `1D` | `659.50` | 45,470,000.00 USD | 0.00 USD | 45,470,000.00 USD | 111,490.00 USD | 7,460.00 USD | 0.00 USD |
| `7D` | `659.50` | 36,390,000.00 USD | 0.00 USD | 36,390,000.00 USD | 38,970.00 USD | 20,150.00 USD | 87,160.00 USD |
| `1D` | `660.30` | 45,350,000.00 USD | 0.00 USD | 45,350,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `660.40` | 36,240,000.00 USD | 0.00 USD | 36,240,000.00 USD | 21,730.00 USD | 0.00 USD | 11,830.00 USD |
| `1D` | `661.10` | 45,240,000.00 USD | 0.00 USD | 45,240,000.00 USD | 0.00 USD | 83,170.00 USD | 0.00 USD |
| `7D` | `661.30` | 36,210,000.00 USD | 0.00 USD | 36,210,000.00 USD | 343,180.00 USD | 17,690.00 USD | 29,800.00 USD |
| `1D` | `661.90` | 45,160,000.00 USD | 0.00 USD | 45,160,000.00 USD | 592,290.00 USD | 68,060.00 USD | 0.00 USD |
| `7D` | `662.20` | 35,820,000.00 USD | 0.00 USD | 35,820,000.00 USD | 113,650.00 USD | 19,070.00 USD | 697,290.00 USD |
| `1D` | `662.70` | 44,500,000.00 USD | 0.00 USD | 44,500,000.00 USD | 98,540.00 USD | 87,740.00 USD | 24,990.00 USD |
| `7D` | `663.10` | 34,990,000.00 USD | 0.00 USD | 34,990,000.00 USD | 863,730.00 USD | 138,640.00 USD | 21,580.00 USD |
| `1D` | `663.50` | 44,290,000.00 USD | 0.00 USD | 44,290,000.00 USD | 202,030.00 USD | 5,000.00 USD | 19,650.00 USD |
| `7D` | `664.00` | 33,960,000.00 USD | 0.00 USD | 33,960,000.00 USD | 167,890.00 USD | 18,740.00 USD | 29,380.00 USD |
| `1D` | `664.30` | 44,060,000.00 USD | 0.00 USD | 44,060,000.00 USD | 785,690.00 USD | 64,390.00 USD | 89,900.00 USD |
| `7D` | `664.90` | 33,750,000.00 USD | 0.00 USD | 33,750,000.00 USD | 237,720.00 USD | 22,990.00 USD | 38,120.00 USD |
| `1D` | `665.10` | 43,120,000.00 USD | 0.00 USD | 43,120,000.00 USD | 684,260.00 USD | 0.00 USD | 43,850.00 USD |
| `7D` | `665.80` | 33,450,000.00 USD | 0.00 USD | 33,450,000.00 USD | 348,440.00 USD | 54,100.00 USD | 54,800.00 USD |
| `1D` | `665.90` | 42,390,000.00 USD | 0.00 USD | 42,390,000.00 USD | 756,330.00 USD | 84,510.00 USD | 746,590.00 USD |
| `1D` | `666.70` | 40,800,000.00 USD | 0.00 USD | 40,800,000.00 USD | 839,260.00 USD | 13,270.00 USD | 31,410.00 USD |
| `7D` | `666.70` | 32,990,000.00 USD | 0.00 USD | 32,990,000.00 USD | 398,430.00 USD | 39,830.00 USD | 62,560.00 USD |
| `1D` | `667.50` | 39,920,000.00 USD | 0.00 USD | 39,920,000.00 USD | 516,430.00 USD | 167,750.00 USD | 9,290.00 USD |
| `7D` | `667.60` | 32,490,000.00 USD | 0.00 USD | 32,490,000.00 USD | 601,660.00 USD | 45,130.00 USD | 39,410.00 USD |
| `1D` | `668.30` | 39,230,000.00 USD | 0.00 USD | 39,230,000.00 USD | 754,630.00 USD | 3,380.00 USD | 3,620.00 USD |
| `7D` | `668.50` | 31,810,000.00 USD | 0.00 USD | 31,810,000.00 USD | 846,160.00 USD | 82,630.00 USD | 62,990.00 USD |
| `1D` | `669.10` | 38,470,000.00 USD | 0.00 USD | 38,470,000.00 USD | 486,520.00 USD | 70,860.00 USD | 18,950.00 USD |
| `7D` | `669.40` | 30,810,000.00 USD | 0.00 USD | 30,810,000.00 USD | 629,370.00 USD | 48,360.00 USD | 98,640.00 USD |
| `1D` | `669.90` | 37,890,000.00 USD | 0.00 USD | 37,890,000.00 USD | 478,650.00 USD | 43,250.00 USD | 1,510,000.00 USD |
| `7D` | `670.30` | 30,040,000.00 USD | 0.00 USD | 30,040,000.00 USD | 206,130.00 USD | 92,120.00 USD | 43,140.00 USD |
| `1D` | `670.70` | 35,860,000.00 USD | 0.00 USD | 35,860,000.00 USD | 474,770.00 USD | 10,760.00 USD | 3,780.00 USD |
| `7D` | `671.20` | 29,700,000.00 USD | 0.00 USD | 29,700,000.00 USD | 780,550.00 USD | 43,140.00 USD | 714,260.00 USD |
| `1D` | `671.50` | 35,370,000.00 USD | 0.00 USD | 35,370,000.00 USD | 1,900,000.00 USD | 30,160.00 USD | 46,180.00 USD |
| `7D` | `672.10` | 28,160,000.00 USD | 0.00 USD | 28,160,000.00 USD | 108,430.00 USD | 26,430.00 USD | 40,110.00 USD |
| `1D` | `672.30` | 33,390,000.00 USD | 0.00 USD | 33,390,000.00 USD | 591,410.00 USD | 3,440.00 USD | 139,170.00 USD |
| `7D` | `673.00` | 27,980,000.00 USD | 0.00 USD | 27,980,000.00 USD | 1,010,000.00 USD | 165,010.00 USD | 31,670.00 USD |
| `1D` | `673.10` | 32,660,000.00 USD | 0.00 USD | 32,660,000.00 USD | 212,350.00 USD | 280,780.00 USD | 1,050,000.00 USD |
| `1D` | `673.90` | 31,110,000.00 USD | 0.00 USD | 31,110,000.00 USD | 280,490.00 USD | 215,360.00 USD | 1,630,000.00 USD |
| `7D` | `673.90` | 26,770,000.00 USD | 0.00 USD | 26,770,000.00 USD | 335,670.00 USD | 329,650.00 USD | 251,710.00 USD |
| `1D` | `674.70` | 28,980,000.00 USD | 0.00 USD | 28,980,000.00 USD | 1,310,000.00 USD | 399,040.00 USD | 458,040.00 USD |
| `7D` | `674.80` | 25,850,000.00 USD | 0.00 USD | 25,850,000.00 USD | 312,600.00 USD | 184,460.00 USD | 520,760.00 USD |
| `1D` | `675.50` | 26,810,000.00 USD | 0.00 USD | 26,810,000.00 USD | 1,420,000.00 USD | 187,180.00 USD | 460,780.00 USD |
| `7D` | `675.70` | 24,840,000.00 USD | 0.00 USD | 24,840,000.00 USD | 550,560.00 USD | 36,500.00 USD | 2,400,000.00 USD |
| `1D` | `676.30` | 24,750,000.00 USD | 0.00 USD | 24,750,000.00 USD | 822,970.00 USD | 347,350.00 USD | 445,630.00 USD |
| `7D` | `676.60` | 21,850,000.00 USD | 0.00 USD | 21,850,000.00 USD | 518,720.00 USD | 455,810.00 USD | 358,560.00 USD |
| `1D` | `677.10` | 23,130,000.00 USD | 0.00 USD | 23,130,000.00 USD | 93,570.00 USD | 87,370.00 USD | 312,780.00 USD |
| `7D` | `677.50` | 20,520,000.00 USD | 0.00 USD | 20,520,000.00 USD | 2,260,000.00 USD | 128,230.00 USD | 903,260.00 USD |
| `1D` | `677.90` | 22,640,000.00 USD | 0.00 USD | 22,640,000.00 USD | 438,990.00 USD | 172,180.00 USD | 250,510.00 USD |
| `7D` | `678.40` | 17,230,000.00 USD | 0.00 USD | 17,230,000.00 USD | 465,560.00 USD | 73,000.00 USD | 43,880.00 USD |
| `1D` | `678.70` | 21,780,000.00 USD | 0.00 USD | 21,780,000.00 USD | 1,530,000.00 USD | 164,420.00 USD | 148,360.00 USD |
| `7D` | `679.30` | 16,650,000.00 USD | 0.00 USD | 16,650,000.00 USD | 82,740.00 USD | 53,030.00 USD | 158,890.00 USD |
| `1D` | `679.50` | 19,930,000.00 USD | 0.00 USD | 19,930,000.00 USD | 1,590,000.00 USD | 80,850.00 USD | 155,260.00 USD |
| `7D` | `680.20` | 16,350,000.00 USD | 0.00 USD | 16,350,000.00 USD | 21,320.00 USD | 65,770.00 USD | 163,020.00 USD |
| `1D` | `680.30` | 18,100,000.00 USD | 0.00 USD | 18,100,000.00 USD | 25,960.00 USD | 215,610.00 USD | 261,300.00 USD |
| `1D` | `681.10` | 17,600,000.00 USD | 0.00 USD | 17,600,000.00 USD | 597,000.00 USD | 206,150.00 USD | 87,500.00 USD |
| `7D` | `681.10` | 16,100,000.00 USD | 0.00 USD | 16,100,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `681.90` | 16,710,000.00 USD | 0.00 USD | 16,710,000.00 USD | 452,920.00 USD | 334,790.00 USD | 0.00 USD |
| `7D` | `682.00` | 15,870,000.00 USD | 0.00 USD | 15,870,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `682.70` | 15,920,000.00 USD | 0.00 USD | 15,920,000.00 USD | 336,330.00 USD | 59,430.00 USD | 0.00 USD |
| `7D` | `682.90` | 14,110,000.00 USD | 0.00 USD | 14,110,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `683.50` | 15,530,000.00 USD | 0.00 USD | 15,530,000.00 USD | 468,720.00 USD | 0.00 USD | 37,900.00 USD |
| `7D` | `683.80` | 14,070,000.00 USD | 0.00 USD | 14,070,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `684.30` | 15,020,000.00 USD | 0.00 USD | 15,020,000.00 USD | 429,900.00 USD | 21,510.00 USD | 50,970.00 USD |
| `7D` | `684.70` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 369,590.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `685.10` | 14,520,000.00 USD | 0.00 USD | 14,520,000.00 USD | 406,260.00 USD | 37,140.00 USD | 0.00 USD |
| `7D` | `685.60` | 13,510,000.00 USD | 0.00 USD | 13,510,000.00 USD | 1,200,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `685.90` | 14,080,000.00 USD | 0.00 USD | 14,080,000.00 USD | 1,120,000.00 USD | 48,550.00 USD | 0.00 USD |
| `7D` | `686.50` | 12,310,000.00 USD | 0.00 USD | 12,310,000.00 USD | 58,940.00 USD | 36,480.00 USD | 0.00 USD |
| `1D` | `686.70` | 12,910,000.00 USD | 0.00 USD | 12,910,000.00 USD | 135,120.00 USD | 141,180.00 USD | 525,120.00 USD |
| `7D` | `687.40` | 12,220,000.00 USD | 0.00 USD | 12,220,000.00 USD | 148,480.00 USD | 580,220.00 USD | 112,300.00 USD |
| `1D` | `687.50` | 12,110,000.00 USD | 0.00 USD | 12,110,000.00 USD | 1,250,000.00 USD | 292,550.00 USD | 326,890.00 USD |
| `1D` | `688.30` | 10,230,000.00 USD | 0.00 USD | 10,230,000.00 USD | 770,930.00 USD | 133,560.00 USD | 801,820.00 USD |
| `7D` | `688.30` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 234,210.00 USD | 427,630.00 USD | 269,830.00 USD |
| `1D` | `689.10` | 8,520,000.00 USD | 0.00 USD | 8,520,000.00 USD | 646,890.00 USD | 111,110.00 USD | 1,480,000.00 USD |
| `7D` | `689.20` | 10,440,000.00 USD | 0.00 USD | 10,440,000.00 USD | 234,630.00 USD | 57,190.00 USD | 2,350,000.00 USD |
| `1D` | `689.90` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 825,990.00 USD | 106,890.00 USD | 358,770.00 USD |
| `7D` | `690.10` | 7,800,000.00 USD | 0.00 USD | 7,800,000.00 USD | 543,670.00 USD | 237,760.00 USD | 1,340,000.00 USD |
| `1D` | `690.70` | 5,000,000.00 USD | 0.00 USD | 5,000,000.00 USD | 329,760.00 USD | 199,550.00 USD | 401,550.00 USD |
| `7D` | `691.00` | 5,680,000.00 USD | 0.00 USD | 5,680,000.00 USD | 281,290.00 USD | 325,740.00 USD | 1,120,000.00 USD |
| `1D` | `691.50` | 4,060,000.00 USD | 0.00 USD | 4,060,000.00 USD | 0.00 USD | 71,280.00 USD | 52,930.00 USD |
| `7D` | `691.90` | 3,950,000.00 USD | 0.00 USD | 3,950,000.00 USD | 22,150.00 USD | 0.00 USD | 969,680.00 USD |
| `1D` | `692.30` | 3,940,000.00 USD | 0.00 USD | 3,940,000.00 USD | 780,530.00 USD | 31,410.00 USD | 102,980.00 USD |
| `7D` | `692.80` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD |
| `1D` | `693.10` | 3,030,000.00 USD | 0.00 USD | 3,030,000.00 USD | 76,730.00 USD | 159,980.00 USD | 69,190.00 USD |
| `7D` | `693.70` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 317,780.00 USD |
| `1D` | `693.90` | 2,720,000.00 USD | 0.00 USD | 2,720,000.00 USD | 320,330.00 USD | 140,550.00 USD | 382,250.00 USD |
| `7D` | `694.60` | 1,500,000.00 USD | 0.00 USD | 1,500,000.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD |
| `1D` | `694.70` | 1,880,000.00 USD | 0.00 USD | 1,880,000.00 USD | 66,510.00 USD | 118,590.00 USD | 176,360.00 USD |
| `1D` | `695.50` | 1,510,000.00 USD | 0.00 USD | 1,510,000.00 USD | 239,550.00 USD | 34,140.00 USD | 88,480.00 USD |
| `7D` | `695.50` | 1,040,000.00 USD | 0.00 USD | 1,040,000.00 USD | 0.00 USD | 128,880.00 USD | 335,740.00 USD |
| `1D` | `696.30` | 1,150,000.00 USD | 0.00 USD | 1,150,000.00 USD | 153,900.00 USD | 32,060.00 USD | 0.00 USD |
| `1D` | `697.10` | 966,400.00 USD | 0.00 USD | 966,400.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD |
| `1D` | `697.90` | 902,690.00 USD | 0.00 USD | 902,690.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `698.70` | 699,330.00 USD | 0.00 USD | 699,330.00 USD | 276,500.00 USD | 0.00 USD | 67,030.00 USD |
| `7D` | `699.10` | 575,930.00 USD | 0.00 USD | 575,930.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.50` | 355,790.00 USD | 0.00 USD | 355,790.00 USD | 0.00 USD | 31,670.00 USD | 0.00 USD |
| `1D` | `700.30` | 324,120.00 USD | 0.00 USD | 324,120.00 USD | 324,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.00` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `703.70` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `705.90` | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.90` | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `710.70` | 464,720.00 USD | 464,720.00 USD | 0.00 USD | 343,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `711.50` | 850,080.00 USD | 850,080.00 USD | 0.00 USD | 308,680.00 USD | 0.00 USD | 76,680.00 USD |
| `7D` | `712.60` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `714.70` | 1,850,000.00 USD | 1,850,000.00 USD | 0.00 USD | 135,120.00 USD | 21,500.00 USD | 841,710.00 USD |
| `7D` | `715.30` | 947,510.00 USD | 947,510.00 USD | 0.00 USD | 0.00 USD | 40,990.00 USD | 112,300.00 USD |
| `1D` | `715.50` | 3,480,000.00 USD | 3,480,000.00 USD | 0.00 USD | 227,340.00 USD | 180,660.00 USD | 1,230,000.00 USD |
| `7D` | `716.20` | 1,450,000.00 USD | 1,450,000.00 USD | 0.00 USD | 0.00 USD | 231,020.00 USD | 269,830.00 USD |
| `1D` | `716.30` | 4,150,000.00 USD | 4,150,000.00 USD | 0.00 USD | 203,920.00 USD | 44,140.00 USD | 414,830.00 USD |
| `1D` | `717.10` | 5,100,000.00 USD | 5,100,000.00 USD | 0.00 USD | 584,450.00 USD | 24,690.00 USD | 345,010.00 USD |
| `7D` | `717.10` | 2,190,000.00 USD | 2,190,000.00 USD | 0.00 USD | 337,810.00 USD | 0.00 USD | 404,380.00 USD |
| `1D` | `717.90` | 5,870,000.00 USD | 5,870,000.00 USD | 0.00 USD | 463,930.00 USD | 41,310.00 USD | 260,930.00 USD |
| `7D` | `718.00` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 345,570.00 USD | 51,150.00 USD | 107,000.00 USD |
| `1D` | `718.70` | 6,660,000.00 USD | 6,660,000.00 USD | 0.00 USD | 582,730.00 USD | 71,870.00 USD | 142,630.00 USD |
| `7D` | `718.90` | 4,020,000.00 USD | 4,020,000.00 USD | 0.00 USD | 775,390.00 USD | 69,290.00 USD | 481,540.00 USD |
| `1D` | `719.50` | 7,030,000.00 USD | 7,030,000.00 USD | 0.00 USD | 60,590.00 USD | 82,030.00 USD | 219,580.00 USD |
| `7D` | `719.80` | 6,270,000.00 USD | 6,270,000.00 USD | 0.00 USD | 183,760.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `720.30` | 8,240,000.00 USD | 8,240,000.00 USD | 0.00 USD | 988,460.00 USD | 86,780.00 USD | 134,970.00 USD |
| `7D` | `720.70` | 7,040,000.00 USD | 7,040,000.00 USD | 0.00 USD | 622,340.00 USD | 146,010.00 USD | 0.00 USD |
| `1D` | `721.10` | 8,790,000.00 USD | 8,790,000.00 USD | 0.00 USD | 177,520.00 USD | 328,830.00 USD | 50,390.00 USD |
| `7D` | `721.60` | 7,410,000.00 USD | 7,410,000.00 USD | 0.00 USD | 181,600.00 USD | 106,060.00 USD | 87,760.00 USD |
| `1D` | `721.90` | 9,510,000.00 USD | 9,510,000.00 USD | 0.00 USD | 145,470.00 USD | 207,490.00 USD | 368,620.00 USD |
| `7D` | `722.50` | 8,190,000.00 USD | 8,190,000.00 USD | 0.00 USD | 0.00 USD | 131,550.00 USD | 643,830.00 USD |
| `1D` | `722.70` | 10,250,000.00 USD | 10,250,000.00 USD | 0.00 USD | 393,920.00 USD | 131,240.00 USD | 207,830.00 USD |
| `7D` | `723.40` | 9,330,000.00 USD | 9,330,000.00 USD | 0.00 USD | 806,150.00 USD | 0.00 USD | 335,740.00 USD |
| `1D` | `723.50` | 11,270,000.00 USD | 11,270,000.00 USD | 0.00 USD | 446,650.00 USD | 403,140.00 USD | 175,000.00 USD |
| `1D` | `724.30` | 11,760,000.00 USD | 11,760,000.00 USD | 0.00 USD | 300,180.00 USD | 185,360.00 USD | 0.00 USD |
| `7D` | `724.30` | 9,460,000.00 USD | 9,460,000.00 USD | 0.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD |
| `1D` | `725.10` | 12,150,000.00 USD | 12,150,000.00 USD | 0.00 USD | 223,480.00 USD | 152,860.00 USD | 18,950.00 USD |
| `1D` | `725.90` | 12,490,000.00 USD | 12,490,000.00 USD | 0.00 USD | 317,710.00 USD | 0.00 USD | 19,390.00 USD |
| `7D` | `726.10` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 0.00 USD | 58,160.00 USD | 1,120,000.00 USD |
| `1D` | `726.70` | 12,830,000.00 USD | 12,830,000.00 USD | 0.00 USD | 226,170.00 USD | 85,880.00 USD | 24,380.00 USD |
| `7D` | `727.00` | 11,830,000.00 USD | 11,830,000.00 USD | 0.00 USD | 552,080.00 USD | 0.00 USD | 639,380.00 USD |
| `1D` | `727.50` | 13,410,000.00 USD | 13,410,000.00 USD | 0.00 USD | 537,650.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `727.90` | 12,610,000.00 USD | 12,610,000.00 USD | 0.00 USD | 575,930.00 USD | 201,080.00 USD | 0.00 USD |
| `1D` | `728.30` | 13,780,000.00 USD | 13,780,000.00 USD | 0.00 USD | 235,780.00 USD | 0.00 USD | 133,900.00 USD |
| `7D` | `728.80` | 13,530,000.00 USD | 13,530,000.00 USD | 0.00 USD | 779,040.00 USD | 145,560.00 USD | 0.00 USD |
| `1D` | `729.10` | 15,010,000.00 USD | 15,010,000.00 USD | 0.00 USD | 499,870.00 USD | 317,000.00 USD | 414,580.00 USD |
| `7D` | `729.70` | 14,730,000.00 USD | 14,730,000.00 USD | 0.00 USD | 576,440.00 USD | 425,860.00 USD | 191,070.00 USD |
| `1D` | `729.90` | 16,060,000.00 USD | 16,060,000.00 USD | 0.00 USD | 226,750.00 USD | 246,250.00 USD | 572,410.00 USD |
| `7D` | `730.60` | 15,420,000.00 USD | 15,420,000.00 USD | 0.00 USD | 296,730.00 USD | 273,740.00 USD | 119,980.00 USD |
| `1D` | `730.70` | 22,050,000.00 USD | 22,050,000.00 USD | 0.00 USD | 3,220,000.00 USD | 484,450.00 USD | 2,280,000.00 USD |
| `1D` | `731.50` | 23,550,000.00 USD | 23,550,000.00 USD | 0.00 USD | 738,570.00 USD | 139,290.00 USD | 624,430.00 USD |
| `7D` | `731.50` | 16,470,000.00 USD | 16,470,000.00 USD | 0.00 USD | 0.00 USD | 114,370.00 USD | 941,540.00 USD |
| `1D` | `732.30` | 26,370,000.00 USD | 26,370,000.00 USD | 0.00 USD | 1,290,000.00 USD | 113,040.00 USD | 1,410,000.00 USD |
| `7D` | `732.40` | 18,320,000.00 USD | 18,320,000.00 USD | 0.00 USD | 172,790.00 USD | 118,880.00 USD | 1,550,000.00 USD |
| `1D` | `733.10` | 28,100,000.00 USD | 28,100,000.00 USD | 0.00 USD | 927,780.00 USD | 249,610.00 USD | 551,370.00 USD |
| `7D` | `733.30` | 19,130,000.00 USD | 19,130,000.00 USD | 0.00 USD | 91,880.00 USD | 162,870.00 USD | 559,810.00 USD |
| `1D` | `733.90` | 29,040,000.00 USD | 29,040,000.00 USD | 0.00 USD | 365,220.00 USD | 226,780.00 USD | 347,700.00 USD |
| `7D` | `734.20` | 19,740,000.00 USD | 19,740,000.00 USD | 0.00 USD | 123,040.00 USD | 0.00 USD | 484,840.00 USD |
| `1D` | `734.70` | 30,110,000.00 USD | 30,110,000.00 USD | 0.00 USD | 967,050.00 USD | 52,620.00 USD | 51,490.00 USD |
| `7D` | `735.10` | 20,400,000.00 USD | 20,400,000.00 USD | 0.00 USD | 547,660.00 USD | 73,000.00 USD | 43,880.00 USD |
| `1D` | `735.50` | 31,340,000.00 USD | 31,340,000.00 USD | 0.00 USD | 401,720.00 USD | 207,980.00 USD | 625,520.00 USD |
| `7D` | `736.00` | 20,620,000.00 USD | 20,620,000.00 USD | 0.00 USD | 0.00 USD | 53,030.00 USD | 158,890.00 USD |
| `1D` | `736.30` | 31,990,000.00 USD | 31,990,000.00 USD | 0.00 USD | 385,990.00 USD | 70,270.00 USD | 191,130.00 USD |
| `7D` | `736.90` | 21,020,000.00 USD | 21,020,000.00 USD | 0.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD |
| `1D` | `737.10` | 32,280,000.00 USD | 32,280,000.00 USD | 0.00 USD | 156,930.00 USD | 43,110.00 USD | 88,180.00 USD |
| `7D` | `737.80` | 21,250,000.00 USD | 21,250,000.00 USD | 0.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `737.90` | 32,900,000.00 USD | 32,900,000.00 USD | 0.00 USD | 399,410.00 USD | 178,930.00 USD | 44,240.00 USD |
| `1D` | `738.70` | 34,030,000.00 USD | 34,030,000.00 USD | 0.00 USD | 624,880.00 USD | 33,100.00 USD | 472,930.00 USD |
| `7D` | `738.70` | 22,170,000.00 USD | 22,170,000.00 USD | 0.00 USD | 50,860.00 USD | 166,070.00 USD | 703,580.00 USD |
| `1D` | `739.50` | 34,710,000.00 USD | 34,710,000.00 USD | 0.00 USD | 186,290.00 USD | 31,860.00 USD | 461,770.00 USD |
| `7D` | `739.60` | 23,190,000.00 USD | 23,190,000.00 USD | 0.00 USD | 1,010,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `740.30` | 34,940,000.00 USD | 34,940,000.00 USD | 0.00 USD | 92,050.00 USD | 134,150.00 USD | 0.00 USD |
| `7D` | `740.50` | 24,940,000.00 USD | 24,940,000.00 USD | 0.00 USD | 1,090,000.00 USD | 0.00 USD | 659,710.00 USD |
| `1D` | `741.10` | 35,540,000.00 USD | 35,540,000.00 USD | 0.00 USD | 554,740.00 USD | 32,240.00 USD | 12,190.00 USD |
| `7D` | `741.40` | 25,400,000.00 USD | 25,400,000.00 USD | 0.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `741.90` | 35,840,000.00 USD | 35,840,000.00 USD | 0.00 USD | 291,160.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `742.30` | 25,910,000.00 USD | 25,910,000.00 USD | 0.00 USD | 383,790.00 USD | 100,540.00 USD | 21,460.00 USD |
| `1D` | `742.70` | 35,980,000.00 USD | 35,980,000.00 USD | 0.00 USD | 140,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.20` | 26,520,000.00 USD | 26,520,000.00 USD | 0.00 USD | 389,520.00 USD | 0.00 USD | 220,040.00 USD |
| `1D` | `743.50` | 36,670,000.00 USD | 36,670,000.00 USD | 0.00 USD | 233,380.00 USD | 21,120.00 USD | 436,560.00 USD |
| `7D` | `744.10` | 27,100,000.00 USD | 27,100,000.00 USD | 0.00 USD | 160,880.00 USD | 282,830.00 USD | 141,790.00 USD |
| `1D` | `744.30` | 37,760,000.00 USD | 37,760,000.00 USD | 0.00 USD | 891,770.00 USD | 191,870.00 USD | 0.00 USD |
| `7D` | `745.00` | 27,260,000.00 USD | 27,260,000.00 USD | 0.00 USD | 0.00 USD | 155,680.00 USD | 0.00 USD |
| `1D` | `745.10` | 39,430,000.00 USD | 39,430,000.00 USD | 0.00 USD | 710,280.00 USD | 61,600.00 USD | 897,830.00 USD |
| `1D` | `745.90` | 39,820,000.00 USD | 39,820,000.00 USD | 0.00 USD | 196,920.00 USD | 120,210.00 USD | 78,280.00 USD |
| `7D` | `745.90` | 27,710,000.00 USD | 27,710,000.00 USD | 0.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD |
| `1D` | `746.70` | 41,560,000.00 USD | 41,560,000.00 USD | 0.00 USD | 674,650.00 USD | 29,460.00 USD | 1,040,000.00 USD |
| `7D` | `746.80` | 28,550,000.00 USD | 28,550,000.00 USD | 0.00 USD | 324,750.00 USD | 0.00 USD | 513,150.00 USD |
| `1D` | `747.50` | 42,020,000.00 USD | 42,020,000.00 USD | 0.00 USD | 300,360.00 USD | 74,380.00 USD | 80,900.00 USD |
| `7D` | `747.70` | 28,990,000.00 USD | 28,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 435,810.00 USD |
| `1D` | `748.30` | 42,620,000.00 USD | 42,620,000.00 USD | 0.00 USD | 407,940.00 USD | 84,260.00 USD | 108,850.00 USD |
| `7D` | `748.60` | 29,320,000.00 USD | 29,320,000.00 USD | 0.00 USD | 337,680.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `749.10` | 43,020,000.00 USD | 43,020,000.00 USD | 0.00 USD | 401,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `749.50` | 29,740,000.00 USD | 29,740,000.00 USD | 0.00 USD | 356,770.00 USD | 61,650.00 USD | 0.00 USD |
| `1D` | `749.90` | 43,270,000.00 USD | 43,270,000.00 USD | 0.00 USD | 251,210.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `750.40` | 29,830,000.00 USD | 29,830,000.00 USD | 0.00 USD | 86,120.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.70` | 43,390,000.00 USD | 43,390,000.00 USD | 0.00 USD | 121,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `751.30` | 30,000,000.00 USD | 30,000,000.00 USD | 0.00 USD | 175,960.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.50` | 43,620,000.00 USD | 43,620,000.00 USD | 0.00 USD | 97,960.00 USD | 25,010.00 USD | 98,240.00 USD |
| `1D` | `752.30` | 44,150,000.00 USD | 44,150,000.00 USD | 0.00 USD | 93,830.00 USD | 0.00 USD | 441,380.00 USD |
| `1D` | `753.10` | 44,790,000.00 USD | 44,790,000.00 USD | 0.00 USD | 393,720.00 USD | 0.00 USD | 248,870.00 USD |
| `7D` | `753.10` | 30,450,000.00 USD | 30,450,000.00 USD | 0.00 USD | 96,700.00 USD | 0.00 USD | 351,790.00 USD |
| `1D` | `753.90` | 45,250,000.00 USD | 45,250,000.00 USD | 0.00 USD | 362,250.00 USD | 54,420.00 USD | 40,370.00 USD |
| `7D` | `754.00` | 30,880,000.00 USD | 30,880,000.00 USD | 0.00 USD | 310,190.00 USD | 83,030.00 USD | 33,430.00 USD |
| `1D` | `754.70` | 45,530,000.00 USD | 45,530,000.00 USD | 0.00 USD | 159,380.00 USD | 98,410.00 USD | 16,910.00 USD |
| `7D` | `754.90` | 30,940,000.00 USD | 30,940,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.50` | 46,040,000.00 USD | 46,040,000.00 USD | 0.00 USD | 396,840.00 USD | 96,170.00 USD | 19,780.00 USD |
| `7D` | `755.80` | 31,060,000.00 USD | 31,060,000.00 USD | 0.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `756.30` | 46,120,000.00 USD | 46,120,000.00 USD | 0.00 USD | 13,050.00 USD | 24,970.00 USD | 46,440.00 USD |
| `7D` | `756.70` | 31,110,000.00 USD | 31,110,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.10` | 46,350,000.00 USD | 46,350,000.00 USD | 0.00 USD | 164,820.00 USD | 33,270.00 USD | 30,030.00 USD |
| `7D` | `757.60` | 31,220,000.00 USD | 31,220,000.00 USD | 0.00 USD | 0.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `757.90` | 46,770,000.00 USD | 46,770,000.00 USD | 0.00 USD | 378,680.00 USD | 26,940.00 USD | 18,080.00 USD |
| `7D` | `758.50` | 33,150,000.00 USD | 33,150,000.00 USD | 0.00 USD | 1,660,000.00 USD | 0.00 USD | 265,620.00 USD |
| `1D` | `758.70` | 47,330,000.00 USD | 47,330,000.00 USD | 0.00 USD | 144,220.00 USD | 142,320.00 USD | 273,090.00 USD |
| `7D` | `759.40` | 33,200,000.00 USD | 33,200,000.00 USD | 0.00 USD | 0.00 USD | 55,460.00 USD | 0.00 USD |
| `1D` | `759.50` | 47,760,000.00 USD | 47,760,000.00 USD | 0.00 USD | 415,540.00 USD | 2,460.00 USD | 8,370.00 USD |
| `1D` | `760.30` | 48,070,000.00 USD | 48,070,000.00 USD | 0.00 USD | 231,490.00 USD | 55,920.00 USD | 20,250.00 USD |
| `7D` | `760.30` | 33,700,000.00 USD | 33,700,000.00 USD | 0.00 USD | 420,720.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `761.10` | 48,580,000.00 USD | 48,580,000.00 USD | 0.00 USD | 254,000.00 USD | 15,330.00 USD | 243,930.00 USD |
| `7D` | `761.20` | 33,990,000.00 USD | 33,990,000.00 USD | 0.00 USD | 164,720.00 USD | 30,310.00 USD | 100,630.00 USD |
| `1D` | `761.90` | 49,230,000.00 USD | 49,230,000.00 USD | 0.00 USD | 575,650.00 USD | 35,860.00 USD | 40,640.00 USD |
| `7D` | `762.10` | 34,660,000.00 USD | 34,660,000.00 USD | 0.00 USD | 35,980.00 USD | 322,010.00 USD | 314,310.00 USD |
| `1D` | `762.70` | 49,980,000.00 USD | 49,980,000.00 USD | 0.00 USD | 413,500.00 USD | 19,550.00 USD | 317,130.00 USD |
| `7D` | `763.00` | 37,570,000.00 USD | 37,570,000.00 USD | 0.00 USD | 2,300,000.00 USD | 271,300.00 USD | 333,320.00 USD |
| `1D` | `763.50` | 50,230,000.00 USD | 50,230,000.00 USD | 0.00 USD | 112,700.00 USD | 90,910.00 USD | 43,820.00 USD |
| `7D` | `763.90` | 39,460,000.00 USD | 39,460,000.00 USD | 0.00 USD | 1,240,000.00 USD | 295,990.00 USD | 353,650.00 USD |
| `1D` | `764.30` | 50,680,000.00 USD | 50,680,000.00 USD | 0.00 USD | 401,340.00 USD | 9,260.00 USD | 40,840.00 USD |
| `7D` | `764.80` | 41,290,000.00 USD | 41,290,000.00 USD | 0.00 USD | 1,250,000.00 USD | 260,460.00 USD | 307,280.00 USD |
| `1D` | `765.10` | 50,970,000.00 USD | 50,970,000.00 USD | 0.00 USD | 123,170.00 USD | 127,420.00 USD | 32,870.00 USD |
| `7D` | `765.70` | 43,880,000.00 USD | 43,880,000.00 USD | 0.00 USD | 2,000,000.00 USD | 134,320.00 USD | 455,200.00 USD |
| `1D` | `765.90` | 51,330,000.00 USD | 51,330,000.00 USD | 0.00 USD | 322,090.00 USD | 5,340.00 USD | 41,230.00 USD |
| `7D` | `766.60` | 48,720,000.00 USD | 48,720,000.00 USD | 0.00 USD | 3,720,000.00 USD | 374,820.00 USD | 742,360.00 USD |
| `1D` | `766.70` | 51,800,000.00 USD | 51,800,000.00 USD | 0.00 USD | 325,730.00 USD | 47,980.00 USD | 91,020.00 USD |
| `1D` | `767.50` | 52,410,000.00 USD | 52,410,000.00 USD | 0.00 USD | 524,440.00 USD | 0.00 USD | 90,830.00 USD |
| `7D` | `767.50` | 51,300,000.00 USD | 51,300,000.00 USD | 0.00 USD | 1,920,000.00 USD | 171,000.00 USD | 487,470.00 USD |
| `1D` | `768.30` | 52,680,000.00 USD | 52,680,000.00 USD | 0.00 USD | 235,790.00 USD | 15,950.00 USD | 12,850.00 USD |
| `7D` | `768.40` | 54,420,000.00 USD | 54,420,000.00 USD | 0.00 USD | 2,660,000.00 USD | 95,830.00 USD | 365,050.00 USD |
| `1D` | `769.10` | 52,890,000.00 USD | 52,890,000.00 USD | 0.00 USD | 154,200.00 USD | 35,430.00 USD | 21,990.00 USD |
| `7D` | `769.30` | 55,940,000.00 USD | 55,940,000.00 USD | 0.00 USD | 718,800.00 USD | 209,770.00 USD | 589,300.00 USD |
| `1D` | `769.90` | 53,050,000.00 USD | 53,050,000.00 USD | 0.00 USD | 131,210.00 USD | 29,070.00 USD | 0.00 USD |
| `7D` | `770.20` | 58,490,000.00 USD | 58,490,000.00 USD | 0.00 USD | 2,030,000.00 USD | 213,870.00 USD | 311,860.00 USD |
| `1D` | `770.70` | 53,520,000.00 USD | 53,520,000.00 USD | 0.00 USD | 85,240.00 USD | 31,140.00 USD | 352,370.00 USD |
| `7D` | `771.10` | 60,150,000.00 USD | 60,150,000.00 USD | 0.00 USD | 1,230,000.00 USD | 293,960.00 USD | 134,800.00 USD |
| `1D` | `771.50` | 54,390,000.00 USD | 54,390,000.00 USD | 0.00 USD | 58,210.00 USD | 132,690.00 USD | 675,580.00 USD |
| `7D` | `772.00` | 62,710,000.00 USD | 62,710,000.00 USD | 0.00 USD | 1,640,000.00 USD | 386,400.00 USD | 526,280.00 USD |
| `1D` | `772.30` | 54,700,000.00 USD | 54,700,000.00 USD | 0.00 USD | 224,770.00 USD | 34,100.00 USD | 54,000.00 USD |
| `7D` | `772.90` | 65,520,000.00 USD | 65,520,000.00 USD | 0.00 USD | 2,120,000.00 USD | 316,840.00 USD | 375,440.00 USD |
| `1D` | `773.10` | 55,500,000.00 USD | 55,500,000.00 USD | 0.00 USD | 634,740.00 USD | 71,650.00 USD | 97,820.00 USD |
| `7D` | `773.80` | 67,270,000.00 USD | 67,270,000.00 USD | 0.00 USD | 1,190,000.00 USD | 270,430.00 USD | 282,970.00 USD |
| `1D` | `773.90` | 55,730,000.00 USD | 55,730,000.00 USD | 0.00 USD | 144,620.00 USD | 26,310.00 USD | 53,940.00 USD |
| `1D` | `774.70` | 56,180,000.00 USD | 56,180,000.00 USD | 0.00 USD | 315,250.00 USD | 48,490.00 USD | 91,240.00 USD |
| `7D` | `774.70` | 69,230,000.00 USD | 69,230,000.00 USD | 0.00 USD | 1,080,000.00 USD | 416,900.00 USD | 470,250.00 USD |
| `1D` | `775.50` | 56,360,000.00 USD | 56,360,000.00 USD | 0.00 USD | 162,620.00 USD | 0.00 USD | 9,990.00 USD |
| `7D` | `775.60` | 71,400,000.00 USD | 71,400,000.00 USD | 0.00 USD | 1,550,000.00 USD | 386,090.00 USD | 231,150.00 USD |
| `7D` | `776.50` | 73,200,000.00 USD | 73,200,000.00 USD | 0.00 USD | 1,410,000.00 USD | 95,320.00 USD | 293,250.00 USD |
| `7D` | `777.40` | 73,940,000.00 USD | 73,940,000.00 USD | 0.00 USD | 571,520.00 USD | 76,980.00 USD | 94,890.00 USD |
| `7D` | `778.30` | 75,530,000.00 USD | 75,530,000.00 USD | 0.00 USD | 1,290,000.00 USD | 160,280.00 USD | 135,080.00 USD |
| `7D` | `779.20` | 76,740,000.00 USD | 76,740,000.00 USD | 0.00 USD | 971,150.00 USD | 107,630.00 USD | 122,470.00 USD |
| `7D` | `780.10` | 78,140,000.00 USD | 78,140,000.00 USD | 0.00 USD | 1,060,000.00 USD | 123,080.00 USD | 218,750.00 USD |
| `7D` | `781.00` | 79,160,000.00 USD | 79,160,000.00 USD | 0.00 USD | 750,650.00 USD | 90,990.00 USD | 182,550.00 USD |
| `7D` | `781.90` | 81,380,000.00 USD | 81,380,000.00 USD | 0.00 USD | 1,770,000.00 USD | 87,670.00 USD | 361,100.00 USD |
| `7D` | `782.80` | 83,540,000.00 USD | 83,540,000.00 USD | 0.00 USD | 1,700,000.00 USD | 36,140.00 USD | 427,460.00 USD |
| `7D` | `783.70` | 84,110,000.00 USD | 84,110,000.00 USD | 0.00 USD | 508,850.00 USD | 10,100.00 USD | 54,380.00 USD |
| `7D` | `784.60` | 84,480,000.00 USD | 84,480,000.00 USD | 0.00 USD | 243,470.00 USD | 68,480.00 USD | 53,990.00 USD |
| `7D` | `785.50` | 85,470,000.00 USD | 85,470,000.00 USD | 0.00 USD | 850,840.00 USD | 54,140.00 USD | 87,490.00 USD |
| `7D` | `786.40` | 86,150,000.00 USD | 86,150,000.00 USD | 0.00 USD | 623,380.00 USD | 30,660.00 USD | 23,970.00 USD |
| `7D` | `787.30` | 86,740,000.00 USD | 86,740,000.00 USD | 0.00 USD | 483,900.00 USD | 17,630.00 USD | 91,050.00 USD |
| `7D` | `788.20` | 87,040,000.00 USD | 87,040,000.00 USD | 0.00 USD | 120,880.00 USD | 93,190.00 USD | 81,230.00 USD |
| `7D` | `789.10` | 87,980,000.00 USD | 87,980,000.00 USD | 0.00 USD | 754,040.00 USD | 74,540.00 USD | 113,410.00 USD |
| `7D` | `790.00` | 88,520,000.00 USD | 88,520,000.00 USD | 0.00 USD | 280,800.00 USD | 99,920.00 USD | 160,030.00 USD |
| `7D` | `790.90` | 89,350,000.00 USD | 89,350,000.00 USD | 0.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD |
| `7D` | `791.80` | 90,250,000.00 USD | 90,250,000.00 USD | 0.00 USD | 780,710.00 USD | 16,830.00 USD | 96,020.00 USD |
| `7D` | `792.70` | 90,520,000.00 USD | 90,520,000.00 USD | 0.00 USD | 258,640.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `793.60` | 90,660,000.00 USD | 90,660,000.00 USD | 0.00 USD | 143,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.50` | 90,870,000.00 USD | 90,870,000.00 USD | 0.00 USD | 194,400.00 USD | 15,690.00 USD | 0.00 USD |
| `7D` | `795.40` | 91,030,000.00 USD | 91,030,000.00 USD | 0.00 USD | 131,460.00 USD | 14,650.00 USD | 14,200.00 USD |
| `7D` | `796.30` | 91,210,000.00 USD | 91,210,000.00 USD | 0.00 USD | 34,010.00 USD | 0.00 USD | 140,720.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.30B` | Total OI Tokens: `1,851,195.9 BNB`
  * 1h OI Change: `+0.78%` | 4h OI Change: `-1.02%` | 24h OI Change: `+4.39%`
  * Exchange Breakdown: Binance=`566.39M` | Bybit=`142.36M` | OKX=`64.91M` | Hyperliquid=`68.84M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-119.42K` | Last 24h: `-160.49K` | Last 3d: `35.49K` | Last 7d: `220.92K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0293%` |
| **USDT Bybit** | `-0.0700%` | **USDT KuCoin** | `-0.0132%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `0.0072%` | **USDT Bitget** | `-0.0126%` |
| **CoinM Binance** | `0.0018%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `40.03%` | `59.97%` | `0.67` | 25,410,000.00 USD |
| `15M` | `Binance` | `50.33%` | `49.67%` | `1.01` | 7,690,000.00 USD |
| `15M` | `OKX` | `32.98%` | `67.02%` | `0.49` | 2,700,000.00 USD |
| `15M` | `Bybit` | `41.19%` | `58.81%` | `0.70` | 2,820,000.00 USD |
| `15M` | `KuCoin` | `14.27%` | `85.73%` | `0.17` | 1,100,000.00 USD |
| `15M` | `Gate` | `54.72%` | `45.28%` | `1.21` | 724,200.00 USD |
| `15M` | `Bitget` | `41.15%` | `58.85%` | `0.70` | 1,240,000.00 USD |
| `15M` | `BingX` | `19.81%` | `80.19%` | `0.25` | 1,520,000.00 USD |
| `15M` | `MEXC` | `53.69%` | `46.31%` | `1.16` | 2,210,000.00 USD |
| `15M` | `Bitunix` | `49.79%` | `50.21%` | `0.99` | 2,870,000.00 USD |
| `15M` | `Hyperliquid` | `17.22%` | `82.78%` | `0.21` | 311,610.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `53.55%` | `46.45%` | `1.15` | 98,020.00 USD |
| `15M` | `Crypto.com` | `42.82%` | `57.18%` | `0.75` | 23,120.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 1,770,000.00 USD |
| `15M` | `HTX` | `14.03%` | `85.97%` | `0.16` | 26,170.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `47.1%` | `52.9%` | `0.89` | 124,190.00 USD |
| `15M` | `Aster` | `46.5%` | `53.5%` | `0.87` | 108,760.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `56.08%` | `43.92%` | `1.28` | 76,930.00 USD |
| `15M` | `Whale Positions` | `50.33%` | `49.67%` | `1.01` | 7,690,000.00 USD |
| `15M` | `Global Accounts` | `40.03%` | `59.97%` | `0.67` | 25,410,000.00 USD |
| `1H` | `BNB` | `53.66%` | `46.34%` | `1.16` | 1,840,000,000.00 USD |
| `1H` | `Binance` | `53.59%` | `46.41%` | `1.15` | 578,840,000.00 USD |
| `1H` | `OKX` | `54.06%` | `45.94%` | `1.18` | 398,660,000.00 USD |
| `1H` | `Bybit` | `55.38%` | `44.62%` | `1.24` | 119,050,000.00 USD |
| `1H` | `KuCoin` | `32.68%` | `67.32%` | `0.49` | 12,010,000.00 USD |
| `1H` | `Gate` | `55.11%` | `44.89%` | `1.23` | 288,920,000.00 USD |
| `1H` | `Bitget` | `55.02%` | `44.98%` | `1.22` | 72,030,000.00 USD |
| `1H` | `BingX` | `52.02%` | `47.98%` | `1.08` | 33,480,000.00 USD |
| `1H` | `MEXC` | `61.4%` | `38.6%` | `1.59` | 83,080,000.00 USD |
| `1H` | `Bitunix` | `52.18%` | `47.82%` | `1.09` | 69,540,000.00 USD |
| `1H` | `Hyperliquid` | `71.27%` | `28.73%` | `2.48` | 81,210,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `50.38%` | `49.62%` | `1.02` | 4,240,000.00 USD |
| `1H` | `Crypto.com` | `50.35%` | `49.65%` | `1.01` | 0.00 USD |
| `1H` | `WhiteBIT` | `6.3%` | `93.7%` | `0.07` | 13,250,000.00 USD |
| `1H` | `HTX` | `80.69%` | `19.31%` | `4.18` | 18,530,000.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 10,450,000.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 480,390.00 USD |
| `1H` | `Kraken` | `65.97%` | `34.03%` | `1.94` | 8,660,000.00 USD |
| `1H` | `Aster` | `42%` | `58%` | `0.72` | 28,570,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `50.76%` | `49.24%` | `1.03` | 22,680,000.00 USD |
| `1H` | `Whale Positions` | `53.59%` | `46.41%` | `1.15` | 578,840,000.00 USD |
| `1H` | `Global Accounts` | `53.66%` | `46.34%` | `1.16` | 1,840,000,000.00 USD |
| `4H` | `BNB` | `44.54%` | `55.46%` | `0.80` | 458,890,000.00 USD |
| `4H` | `Binance` | `48.25%` | `51.75%` | `0.93` | 152,180,000.00 USD |
| `4H` | `OKX` | `44.36%` | `55.64%` | `0.80` | 47,320,000.00 USD |
| `4H` | `Bybit` | `42.72%` | `57.28%` | `0.75` | 72,890,000.00 USD |
| `4H` | `KuCoin` | `43.01%` | `56.99%` | `0.75` | 5,860,000.00 USD |
| `4H` | `Gate` | `53.66%` | `46.34%` | `1.16` | 21,750,000.00 USD |
| `4H` | `Bitget` | `49.67%` | `50.33%` | `0.99` | 33,620,000.00 USD |
| `4H` | `BingX` | `33.01%` | `66.99%` | `0.49` | 8,970,000.00 USD |
| `4H` | `MEXC` | `47.34%` | `52.66%` | `0.90` | 54,000,000.00 USD |
| `4H` | `Bitunix` | `47.83%` | `52.17%` | `0.92` | 18,000,000.00 USD |
| `4H` | `Hyperliquid` | `56.48%` | `43.52%` | `1.30` | 11,100,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `50.28%` | `49.72%` | `1.01` | 1,730,000.00 USD |
| `4H` | `Crypto.com` | `53.1%` | `46.9%` | `1.13` | 816,820.00 USD |
| `4H` | `WhiteBIT` | `1.12%` | `98.88%` | `0.01` | 23,130,000.00 USD |
| `4H` | `HTX` | `41.86%` | `58.14%` | `0.72` | 252,910.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `39.14%` | `60.86%` | `0.64` | 2,990,000.00 USD |
| `4H` | `Aster` | `33.39%` | `66.61%` | `0.50` | 3,270,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `59.79%` | `40.21%` | `1.49` | 981,830.00 USD |
| `4H` | `Whale Positions` | `48.25%` | `51.75%` | `0.93` | 152,180,000.00 USD |
| `4H` | `Global Accounts` | `44.54%` | `55.46%` | `0.80` | 458,890,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `703.95` | `704.38` | `703.95` | `705.75` | `703.65` | 5,175,697.85 USD | 1,950,975.29 USD | 3,224,722.56 USD | -1,273,747.26 USD | `-24.61%` | `0B / 0S` |
| `5:00 UTC` | `703.95` | `703.57` | `703.95` | `704.55` | `702.75` | 8,548,516.20 USD | 3,944,253.54 USD | 4,604,262.66 USD | -660,009.13 USD | `-7.72%` | `0B / 0S` |
| `0:00 UTC` | `703.95` | `703.78` | `703.95` | `704.55` | `702.75` | 6,123,120.93 USD | 2,836,378.38 USD | 3,286,742.56 USD | -450,364.18 USD | `-7.36%` | `1B / 0S` |
| `5:00 UTC` | `702.75` | `702.81` | `702.75` | `703.95` | `701.85` | 6,303,040.32 USD | 2,898,299.22 USD | 3,404,741.10 USD | -506,441.88 USD | `-8.03%` | `1B / 0S` |
| `0:00 UTC` | `702.45` | `702.42` | `702.45` | `703.35` | `701.85` | 6,113,769.16 USD | 3,015,754.20 USD | 3,098,014.96 USD | -82,260.76 USD | `-1.35%` | `0B / 0S` |
| `5:00 UTC` | `701.55` | `701.57` | `701.55` | `702.75` | `700.65` | 5,730,646.91 USD | 2,127,528.75 USD | 3,603,118.16 USD | -1,475,589.41 USD | `-25.75%` | `0B / 3S` |
| `0:00 UTC` | `704.25` | `703.41` | `704.25` | `704.85` | `700.95` | 8,750,566.19 USD | 3,851,302.57 USD | 4,899,263.61 USD | -1,047,961.04 USD | `-11.98%` | `2B / 1S` |
| `5:00 UTC` | `703.05` | `703.18` | `703.05` | `704.55` | `702.15` | 5,260,203.50 USD | 2,429,163.24 USD | 2,831,040.26 USD | -401,877.02 USD | `-7.64%` | `0B / 2S` |
| `0:00 UTC` | `701.55` | `701.66` | `701.55` | `703.35` | `700.65` | 6,676,951.30 USD | 2,353,190.13 USD | 4,323,761.17 USD | -1,970,571.04 USD | `-29.51%` | `0B / 3S` |
| `5:00 UTC` | `700.65` | `700.64` | `700.65` | `700.95` | `700.35` | 2,225,601.95 USD | 609,507.77 USD | 1,616,094.18 USD | -1,006,586.42 USD | `-45.23%` | `1B / 1S` |

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
| `5m` | 1,610,000.00 USD | -562,320.00 USD | **`ACCUMULATION`** |
| `15m` | 714,300.00 USD | -2,500,000.00 USD | **`DISTRIBUTION`** |
| `30m` | 1,220,000.00 USD | -2,870,000.00 USD | **`DISTRIBUTION`** |
| `1h` | 2,710,000.00 USD | -6,960,000.00 USD | **`DISTRIBUTION`** |
| `2h` | 1,440,000.00 USD | -11,570,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -7,490,000.00 USD | -34,310,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -9,740,000.00 USD | -50,600,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -5,980,000.00 USD | -56,020,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -26,890,000.00 USD | -71,490,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -43,840,000.00 USD | -105,830,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -55,220,000.00 USD | -144,820,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -165,500,000.00 USD | -490,090,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+1.61M` | 15m=`+714.30K` | 1h=`+2.71M` | 24h=`-43.84M`
* Futures Capital Netflows: 5m=`-562.32K` | 15m=`-2.50M` | 1h=`-6.96M` | 24h=`-105.83M`
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
  * Execution Entry: `698.95` (Daily VAL sweep / Bullish OTE)
  * Spread-Padded Stop Loss: `692.05` (Risk Distance: `6.90` pts)
  * +2.5R Take Profit: `716.21`
  * Mathematical Lot Sizing: **`1.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `721.83` (Risk Distance: `6.90` pts)
  * +2.5R Take Profit: `697.67`
  * Mathematical Lot Sizing: **`1.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`707.11`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
