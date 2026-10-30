# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 16:12:33 IST` (`2026-10-30 10:42:33 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `702.50` | VWAP Z-Score: `+0.00` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `1.76` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `50.00` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `707.42` | Lower -3.00σ Band: `697.58`
  * Upper +2.51σ Band: `706.36` | Lower -2.51σ Band: `698.64`
  * Upper +2.01σ Band: `705.45` | Lower -2.01σ Band: `699.55`
  * Upper +2.00σ Band: `705.31` | Lower -2.00σ Band: `699.69`
  * Upper +1.28σ Band: `704.47` | Lower -1.28σ Band: `700.53`
  * Upper +1.00σ Band: `703.90` | Lower -1.00σ Band: `701.10`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`702.50` | EMA-20=`702.50` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`702.50` (Slope: `+0.0000`) | EMA-100=`702.50`
  * Institutional Anchors: EMA-144=`702.50` | EMA-200=`702.50` (Slope: `+0.0000`) | EMA-233=`702.50`
- **Range Boundaries**: 24H High=`709.52` | 24H Low=`695.48` | Weekly High=`716.55` | Weekly Low=`688.45`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `714.93` (Distance: `-1.67%`)
  * Point of Control (POC) = `700.80` (Distance: `+0.31%`)
  * Value Area Low (VAL) = `698.95` (Distance: `+0.58%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BEARISH (Below Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`697.90`
  * New York Session (13:00-21:00 UTC): High=`702.45` | Low=`697.90`
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
| `5m` | `701.40` | `703.43` | `700.98` | `703.28` | `4,655` | 3,267,717.38 USD | -405,435.17 USD | `-12.41%` | -46,803,984.79 USD | `-0.35` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `703.28` | `704.46` | `703.24` | `704.26` | `4,548` | 3,201,444.43 USD | -459,842.46 USD | `-14.36%` | -47,263,827.25 USD | `-0.41` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `704.27` | `704.90` | `703.99` | `704.28` | `1,932` | 1,360,946.69 USD | -163,004.61 USD | `-11.98%` | -47,426,831.86 USD | `+0.26` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `702.57` | `703.32` | `701.75` | `702.70` | `8,704` | 6,113,769.16 USD | -82,260.76 USD | `-1.35%` | -44,980,643.35 USD | `+1.05` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `702.71` | `702.71` | `700.77` | `701.40` | `8,086` | 5,672,963.77 USD | -1,417,906.28 USD | `-24.99%` | -46,398,549.62 USD | `+0.10` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `701.40` | `704.90` | `700.98` | `704.28` | `11,130` | 7,826,967.37 USD | -1,030,986.71 USD | `-13.17%` | -47,429,536.34 USD | `+0.39` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `707.72` | `708.59` | `703.88` | `705.59` | `41,806` | 29,527,241.58 USD | -7,490,244.75 USD | `-25.37%` | -43,690,984.02 USD | `-0.52` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `705.59` | `705.77` | `701.87` | `702.57` | `37,167` | 26,150,375.30 USD | -2,890,562.45 USD | `-11.05%` | -46,581,546.46 USD | `+0.02` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `702.57` | `704.90` | `700.77` | `704.22` | `27,909` | 19,606,544.96 USD | -2,532,632.54 USD | `-12.92%` | -49,114,179.01 USD | `+0.08` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `700.77` | `704.22` | `106,883` | 75,284,161.84 USD | -12,913,439.74 USD | `-17.15%` | -53,715,380.28 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | 8,277,694.32 USD | `-1.00` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | 775,183.01 USD | `-1.22` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -18,402,356.22 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `705.71` | `707.71` | `169,364` | 121,053,242.86 USD | -22,399,584.33 USD | `-18.50%` | -40,801,940.55 USD | `-1.24` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `4h` | `707.72` | `708.59` | `700.77` | `704.22` | `106,883` | 75,284,161.84 USD | -12,913,439.74 USD | `-17.15%` | -53,715,380.28 USD | `-0.37` | **`BEARISH`** | `AGGRESSIVE SELLING` |

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
| `BID` | `703.19` | `24161000000.0000` | 16,989.77 USD | 147,817.21 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `703.20` | `1276000000.0000` | 897.28 USD | 130,827.44 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `703.21` | `27402000000.0000` | 19,269.36 USD | 129,930.16 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `703.23` | `2326000000.0000` | 1,635.71 USD | 110,660.79 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `703.28` | `25630000000.0000` | 18,025.07 USD | 109,025.08 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.29` | `3331000000.0000` | 2,342.66 USD | 91,000.02 USD | `3 orders` | `-0.04%` | `-` |
| `BID` | `703.30` | `1269000000.0000` | 892.49 USD | 88,657.36 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `703.31` | `18957000000.0000` | 13,332.65 USD | 87,764.87 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.32` | `1269000000.0000` | 892.51 USD | 74,432.22 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.36` | `44232000000.0000` | 31,111.02 USD | 73,539.71 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `703.37` | `15796000000.0000` | 11,110.43 USD | 42,428.69 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `703.41` | `954000000.0000` | 671.05 USD | 31,318.26 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `703.42` | `1269000000.0000` | 892.64 USD | 30,647.20 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `703.44` | `2843000000.0000` | 1,999.88 USD | 29,754.56 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `703.45` | `14058000000.0000` | 9,889.10 USD | 27,754.68 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `703.48` | `3693000000.0000` | 2,597.95 USD | 17,865.58 USD | `4 orders` | `-0.01%` | `-` |
| `BID` | `703.49` | `951000000.0000` | 669.02 USD | 15,267.63 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `703.53` | `1320000000.0000` | 928.66 USD | 14,598.61 USD | `2 orders` | `-0.00%` | `-` |
| `BID` | `703.54` | `2406000000.0000` | 1,692.72 USD | 13,669.95 USD | `4 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `703.55` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 703.55` | `0.00%` | `-` |
| `BID` | `703.55` | `17024000000.0000` | 11,977.24 USD | 11,977.24 USD | `5 orders` | `-0.00%` | `-` |
| `ASK` | `703.56` | `300000000.0000` | 211.07 USD | 211.07 USD | `2 orders` | `+0.00%` | `-` |
| `ASK` | `703.60` | `450000000.0000` | 316.62 USD | 527.69 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `703.61` | `300000000.0000` | 211.08 USD | 738.77 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `703.65` | `210000000.0000` | 147.77 USD | 886.54 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `703.66` | `150000000.0000` | 105.55 USD | 992.09 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `703.67` | `150000000.0000` | 105.55 USD | 1,097.64 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `703.68` | `150000000.0000` | 105.55 USD | 1,203.19 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `703.74` | `951000000.0000` | 669.26 USD | 1,872.45 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `703.78` | `5999000000.0000` | 4,221.98 USD | 6,094.42 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `703.84` | `1274000000.0000` | 896.69 USD | 6,991.11 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.86` | `180000000.0000` | 126.69 USD | 7,117.81 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.87` | `180000000.0000` | 126.70 USD | 7,244.51 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `703.88` | `267000000.0000` | 187.94 USD | 7,432.44 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `703.89` | `790000000.0000` | 556.07 USD | 7,988.51 USD | `4 orders` | `+0.05%` | `-` |
| `ASK` | `703.90` | `1276000000.0000` | 898.18 USD | 8,886.69 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `703.91` | `10381000000.0000` | 7,307.29 USD | 16,193.98 USD | `2 orders` | `+0.05%` | `-` |
| `ASK` | `703.92` | `500000000.0000` | 351.96 USD | 16,545.94 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `703.94` | `2324000000.0000` | 1,635.96 USD | 18,181.90 USD | `1 orders` | `+0.05%` | `-` |
| `ASK` | `703.95` | `44397000000.0000` | 31,253.27 USD | 49,435.17 USD | `2 orders` | `+0.06%` | `-` |
| `ASK` | `703.96` | `4293000000.0000` | 3,022.10 USD | 52,457.27 USD | `2 orders` | `+0.06%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 16:12:11 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `784` | `0xea00...a918` | `LONG` | 2,873,408.57 USD | `4,098,429,000,000.00` | `787.24` | `702.65` | `0.000000` | -353,018.21 USD | `-12.29%` | `5X Cross` |
| `902` | `0x7d0c...1b28` | `LONG` | 2,459,950.51 USD | `3,502,756,000,000.00` | `703.91` | `702.65` | `0.000000` | -5,670.79 USD | `-0.23%` | `10X Cross` |
| `905` | `0xfe7c...b7ae` | `LONG` | 2,452,098.21 USD | `3,491,575,000,000.00` | `686.05` | `702.65` | `0.000000` | 56,687.35 USD | `+2.31%` | `10X Cross` |
| `1116` | `0x27c9...d65d` | `LONG` | 1,947,580.79 USD | `2,779,816,000,000.00` | `700.84` | `702.65` | `158.83` | -634.03 USD | `-0.03%` | `10X Cross` |
| `1178` | `0x7737...bf66` | `SHORT` | 1,855,262.56 USD | `2,646,179,000,000.00` | `752.73` | `702.65` | `7067.19` | 136,608.02 USD | `+7.36%` | `10X Cross` |
| `1362` | `0x51f6...2b39` | `LONG` | 1,573,646.28 USD | `2,240,640,000,000.00` | `703.00` | `702.65` | `114.73` | -1,513.45 USD | `-0.10%` | `10X Cross` |
| `1489` | `0xc675...795d` | `LONG` | 1,440,889.98 USD | `2,055,214,000,000.00` | `706.91` | `702.65` | `640.75` | -11,954.68 USD | `-0.83%` | `10X Cross` |
| `1526` | `0x2edd...8179` | `LONG` | 1,406,011.29 USD | `2,001,696,000,000.00` | `714.56` | `702.65` | `0.000000` | -24,323.09 USD | `-1.73%` | `10X Cross` |
| `1577` | `0x325e...9564` | `LONG` | 1,356,076.03 USD | `1,934,212,000,000.00` | `707.43` | `702.65` | `0.000000` | -12,249.74 USD | `-0.90%` | `10X Cross` |
| `1707` | `0x07fd...689d` | `LONG` | 1,225,208.14 USD | `1,744,292,000,000.00` | `714.31` | `702.65` | `0.000000` | -20,755.40 USD | `-1.69%` | `10X Cross` |
| `1718` | `0x645b...87b8` | `LONG` | 1,209,663.54 USD | `1,721,990,000,000.00` | `747.34` | `702.65` | `0.000000` | -77,243.88 USD | `-6.39%` | `10X Cross` |
| `1774` | `0xecb6...2b00` | `SHORT` | 1,158,004.56 USD | `1,648,452,000,000.00` | `714.11` | `702.65` | `17961.53` | 19,176.93 USD | `+1.66%` | `5X Cross` |
| `1803` | `0xa4a6...46cf` | `SHORT` | 1,139,613.64 USD | `1,625,442,000,000.00` | `711.86` | `702.65` | `1621.47` | 17,478.73 USD | `+1.53%` | `10X Cross` |
| `1880` | `0xfc27...9d9d` | `LONG` | 1,075,497.03 USD | `1,531,349,000,000.00` | `701.15` | `702.65` | `0.000000` | 1,789.17 USD | `+0.17%` | `10X Cross` |
| `1886` | `0x4420...4c4b` | `LONG` | 1,067,474.82 USD | `1,520,143,000,000.00` | `704.02` | `702.65` | `204.16` | -2,735.75 USD | `-0.26%` | `10X Cross` |
| `1902` | `0x14c6...b280` | `SHORT` | 1,053,480.00 USD | `1,500,000,000,000.00` | `712.51` | `702.65` | `1466.17` | 15,281.70 USD | `+1.45%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| `ANNOUNCEMENT` | `INFO` | `745.47` | 34,073.94 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale BUY: 34.07K USD at 745.4700 USD [API] | `2026-10-29 13:56:46` |
| `ANNOUNCEMENT` | `INFO` | `744.57` | 44,579.64 USD | `-` | `NEWS_INTEL` | `-` | #BNB Whale SELL: 44.58K USD at 744.5700 USD [API] | `2026-10-29 18:26:19` |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.49` (Vol: 2,400,000.00 USD, Dist: `+7.71%`) | Long MP=`677.23` (Vol: 3,200,000.00 USD, Dist: `--3.83%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+9.05%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.82%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+9.05%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.82%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+9.05%`) | Long MP=`677.29` (Vol: 3,200,000.00 USD, Dist: `--3.82%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `141.50` | 5,520.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `146.50` | 280.69 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 6,230.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `163.50` | 98,100.00 USD | 5,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 1,030.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 6,290.00 USD | 5,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `194.50` | 351.66 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `202.50` | 20,250.00 USD | 5,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 310,870.00 USD | 5,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `207.50` | 590.75 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `209.50` | 257.06 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `218.50` | 190.31 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `235.50` | 909.03 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `240.50` | 165.22 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 998.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `250.50` | 1,320.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `261.50` | 397.74 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 267,500.00 USD | 4,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `268.50` | 21,280.00 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `280.50` | 11,220.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `294.50` | 361.94 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `305.50` | 21,220.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `310.50` | 154,740.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `315.50` | 5,610.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `329.50` | 8,540.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 376.06 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `348.50` | 1,090.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `352.50` | 1,260.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 340.60 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 2,200.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 15,770.00 USD | 4,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `370.50` | 150.79 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 10,480.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 17,600.00 USD | 4,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,400.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 19,070.00 USD | 4,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 10,870.00 USD | 4,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 2,510.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 341.17 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `388.50` | 601.01 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `390.50` | 3,370.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `392.50` | 7,560.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 600.48 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 1,950.00 USD | 4,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 158.20 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 522.32 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `400.50` | 1,700.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `403.50` | 102.09 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 3,490.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 9,800.00 USD | 4,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 3,700.00 USD | 4,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 526.02 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 2,350.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 5,680.00 USD | 4,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,440.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `424.50` | 29,710.00 USD | 4,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 3,540.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `445.50` | 33,080.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `447.50` | 223.75 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `452.50` | 957.04 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `457.50` | 1,490.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `463.50` | 927.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `470.50` | 202.31 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `473.50` | 8,320.00 USD | 3,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 615.36 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `483.50` | 483.50 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 2,840.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,400.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 207.25 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 2,070.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 3,490.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 2,270.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 11,260.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 4,470.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `500.50` | 186.69 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 14,130.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `504.50` | 3,500.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 5,760.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `507.50` | 1,050.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 2,750.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 1,710.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 73,860.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 3,220.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 6,470.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `518.50` | 263.92 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 703.92 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 43,270.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 838.05 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 2,090.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `525.50` | 289.03 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,410.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `528.50` | 63,390.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 59,770.00 USD | 3,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 3,220.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 208.88 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 751.36 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 55,510.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 182,620.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,680.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 12,560.00 USD | 3,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 2,740.00 USD | 3,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `555.50` | 81,680.00 USD | 3,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 3,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 791.65 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `561.50` | 1,510.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 391.57 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 733,410.00 USD | 3,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `575.50` | 460.40 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 19,800.00 USD | 2,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `577.50` | 5,780.00 USD | 2,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 1,850.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 690.26 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,060.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `584.50` | 165,820.00 USD | 2,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,490.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 16,680.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,420.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 226.93 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 44,960.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 940.89 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 7,680.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,480.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 791.22 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 222.32 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 22,860.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 10,310.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.50` | 58,420.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 1,880.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 213.32 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `609.90` | 39,280,000.00 USD | 39,280,000.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `611.50` | 5,860.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 6,520.00 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `620.90` | 39,250,000.00 USD | 39,250,000.00 USD | 0.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `621.50` | 696.70 USD | 1,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `621.90` | 38,930,000.00 USD | 38,930,000.00 USD | 310,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `623.50` | 415.25 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 25,400.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `626.90` | 38,620,000.00 USD | 38,620,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `628.50` | 148.95 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `628.90` | 38,580,000.00 USD | 38,580,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `629.90` | 38,310,000.00 USD | 38,310,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `630.90` | 51,890,000.00 USD | 51,890,000.00 USD | 18,100.00 USD | 56,930.00 USD | 337,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `630.90` | 38,060,000.00 USD | 38,060,000.00 USD | 230,570.00 USD | 50,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `631.70` | 51,470,000.00 USD | 51,470,000.00 USD | 67,470.00 USD | 84,770.00 USD | 582,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `631.90` | 37,780,000.00 USD | 37,780,000.00 USD | 58,820.00 USD | 88,750.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `632.50` | 50,740,000.00 USD | 50,740,000.00 USD | 545,170.00 USD | 64,140.00 USD | 117,930.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `633.30` | 50,010,000.00 USD | 50,010,000.00 USD | 140,890.00 USD | 11,550.00 USD | 26,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `633.90` | 37,630,000.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `634.10` | 49,830,000.00 USD | 49,830,000.00 USD | 194,950.00 USD | 30,650.00 USD | 93,550.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `634.50` | 5,900.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `634.90` | 49,510,000.00 USD | 49,510,000.00 USD | 0.00 USD | 16,410.00 USD | 65,250.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `634.90` | 37,560,000.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `635.70` | 49,430,000.00 USD | 49,430,000.00 USD | 140,670.00 USD | 9,540.00 USD | 58,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `635.90` | 37,510,000.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `636.50` | 49,220,000.00 USD | 49,220,000.00 USD | 120,680.00 USD | 66,890.00 USD | 240,130.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `637.30` | 48,790,000.00 USD | 48,790,000.00 USD | 69,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.10` | 48,730,000.00 USD | 48,730,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `638.90` | 48,660,000.00 USD | 48,660,000.00 USD | 186,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `639.50` | 1,490.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `639.70` | 48,480,000.00 USD | 48,480,000.00 USD | 59,770.00 USD | 0.00 USD | 184,710.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `640.90` | 37,400,000.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `641.30` | 48,230,000.00 USD | 48,230,000.00 USD | 59,370.00 USD | 0.00 USD | 4,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `641.90` | 37,170,000.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `642.10` | 48,170,000.00 USD | 48,170,000.00 USD | 171,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 462,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `642.90` | 48,000,000.00 USD | 48,000,000.00 USD | 51,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `642.90` | 37,130,000.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 454,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `643.70` | 47,950,000.00 USD | 47,950,000.00 USD | 51,730.00 USD | 10,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `643.90` | 36,960,000.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.50` | 47,880,000.00 USD | 47,880,000.00 USD | 393,100.00 USD | 33,090.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `644.90` | 36,930,000.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.30` | 47,120,000.00 USD | 47,120,000.00 USD | 93,740.00 USD | 4,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `645.50` | 307.26 USD | 454,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `645.90` | 36,900,000.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.10` | 47,020,000.00 USD | 47,020,000.00 USD | 174,120.00 USD | 11,780.00 USD | 180,100.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 155.81 USD | 453,780.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `646.90` | 46,650,000.00 USD | 46,650,000.00 USD | 176,670.00 USD | 2,560.00 USD | 31,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `646.90` | 36,830,000.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.70` | 46,440,000.00 USD | 46,440,000.00 USD | 164,610.00 USD | 33,700.00 USD | 14,210.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `647.90` | 36,660,000.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `648.50` | 46,230,000.00 USD | 46,230,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 453,620.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `648.90` | 36,510,000.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.30` | 46,140,000.00 USD | 46,140,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 451,680.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `649.90` | 36,490,000.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `650.10` | 46,090,000.00 USD | 46,090,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 457.30 USD | 450,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `650.90` | 46,020,000.00 USD | 46,020,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `650.90` | 36,310,000.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 449,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.70` | 46,010,000.00 USD | 46,010,000.00 USD | 167,330.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `651.90` | 36,260,000.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `652.50` | 45,740,000.00 USD | 45,740,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 439,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `652.90` | 35,990,000.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `653.30` | 45,710,000.00 USD | 45,710,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 98,240.00 USD | 439,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.10` | 45,640,000.00 USD | 45,640,000.00 USD | 67,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 341,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.90` | 45,570,000.00 USD | 45,570,000.00 USD | 111,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `654.90` | 35,780,000.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 122.58 USD | 340,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.70` | 45,460,000.00 USD | 45,460,000.00 USD | 202,940.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `655.90` | 35,590,000.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.50` | 45,260,000.00 USD | 45,260,000.00 USD | 136,660.00 USD | 40,970.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `656.50` | 24,500.00 USD | 340,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `656.90` | 35,520,000.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.30` | 44,260,000.00 USD | 44,260,000.00 USD | 211,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `657.50` | 338.61 USD | 316,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `657.90` | 35,410,000.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.10` | 44,040,000.00 USD | 44,040,000.00 USD | 875,210.00 USD | 14,920.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 316,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `658.90` | 43,130,000.00 USD | 43,130,000.00 USD | 119,820.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `658.90` | 35,380,000.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 45,510.00 USD | 300,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.70` | 42,930,000.00 USD | 42,930,000.00 USD | 111,490.00 USD | 7,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `659.90` | 35,350,000.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `660.50` | 42,810,000.00 USD | 42,810,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 255,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `660.90` | 35,200,000.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `661.30` | 42,710,000.00 USD | 42,710,000.00 USD | 462,080.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 251,990.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `661.90` | 34,890,000.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `662.10` | 42,160,000.00 USD | 42,160,000.00 USD | 139,750.00 USD | 155,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 231,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.90` | 41,870,000.00 USD | 41,870,000.00 USD | 274,050.00 USD | 0.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `662.90` | 34,060,000.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 31,360.00 USD | 229,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.70` | 41,550,000.00 USD | 41,550,000.00 USD | 16,980.00 USD | 69,400.00 USD | 64,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `663.90` | 33,710,000.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `664.50` | 41,400,000.00 USD | 41,400,000.00 USD | 1,300,000.00 USD | 0.00 USD | 61,580.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 747.56 USD | 197,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `664.90` | 32,730,000.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.30` | 40,030,000.00 USD | 40,030,000.00 USD | 181,030.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 1,610.00 USD | 196,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 32,420,000.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.10` | 39,840,000.00 USD | 39,840,000.00 USD | 846,450.00 USD | 88,780.00 USD | 750,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 2,140.00 USD | 195,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `666.90` | 38,150,000.00 USD | 38,150,000.00 USD | 845,590.00 USD | 13,270.00 USD | 31,410.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `666.90` | 31,890,000.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,830.00 USD | 193,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `667.70` | 37,260,000.00 USD | 37,260,000.00 USD | 541,360.00 USD | 167,750.00 USD | 9,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `667.90` | 31,380,000.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.50` | 36,540,000.00 USD | 36,540,000.00 USD | 774,260.00 USD | 39,300.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 13,450.00 USD | 191,310.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.90` | 30,200,000.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.30` | 35,730,000.00 USD | 35,730,000.00 USD | 365,600.00 USD | 58,270.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 824.15 USD | 177,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `669.90` | 29,320,000.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `670.10` | 35,270,000.00 USD | 35,270,000.00 USD | 609,810.00 USD | 42,060.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 4,750.00 USD | 177,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.90` | 33,120,000.00 USD | 33,120,000.00 USD | 289,790.00 USD | 21,410.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.90` | 28,970,000.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 17,940.00 USD | 172,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.70` | 32,810,000.00 USD | 32,810,000.00 USD | 2,340,000.00 USD | 21,250.00 USD | 46,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.90` | 27,970,000.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `672.50` | 30,400,000.00 USD | 30,400,000.00 USD | 131,990.00 USD | 8,980.00 USD | 713,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 7,860.00 USD | 154,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `672.90` | 27,000,000.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.30` | 29,540,000.00 USD | 29,540,000.00 USD | 72,040.00 USD | 336,780.00 USD | 1,730,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 39,130.00 USD | 146,490.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `673.90` | 25,800,000.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.10` | 27,400,000.00 USD | 27,400,000.00 USD | 272,200.00 USD | 232,500.00 USD | 225,530.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,100.00 USD | 107,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `674.90` | 26,670,000.00 USD | 26,670,000.00 USD | 1,340,000.00 USD | 290,890.00 USD | 512,050.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `674.90` | 25,130,000.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 74,720.00 USD | 103,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `675.70` | 24,530,000.00 USD | 24,530,000.00 USD | 1,660,000.00 USD | 193,370.00 USD | 271,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.90` | 24,000,000.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `676.50` | 22,400,000.00 USD | 22,400,000.00 USD | 248,760.00 USD | 334,230.00 USD | 439,290.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,960.00 USD | 28,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `676.90` | 21,640,000.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.30` | 21,380,000.00 USD | 21,380,000.00 USD | 198,850.00 USD | 58,150.00 USD | 217,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 250.67 USD | 26,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `677.90` | 18,560,000.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.10` | 20,900,000.00 USD | 20,900,000.00 USD | 609,730.00 USD | 168,340.00 USD | 286,140.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 2,520.00 USD | 26,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `678.90` | 19,840,000.00 USD | 19,840,000.00 USD | 1,250,000.00 USD | 182,260.00 USD | 106,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.90` | 17,300,000.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 998.19 USD | 23,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.70` | 18,300,000.00 USD | 18,300,000.00 USD | 1,610,000.00 USD | 227,550.00 USD | 307,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.90` | 16,910,000.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `680.50` | 16,160,000.00 USD | 16,160,000.00 USD | 60,980.00 USD | 59,290.00 USD | 143,090.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 21,870.00 USD | 22,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `680.90` | 16,430,000.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.30` | 15,890,000.00 USD | 15,890,000.00 USD | 602,640.00 USD | 508,720.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `681.90` | 16,190,000.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.10` | 14,740,000.00 USD | 14,740,000.00 USD | 399,330.00 USD | 16,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.90` | 14,320,000.00 USD | 14,320,000.00 USD | 690,810.00 USD | 59,430.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `682.90` | 14,430,000.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.70` | 13,570,000.00 USD | 13,570,000.00 USD | 392,840.00 USD | 0.00 USD | 88,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 14,390,000.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.50` | 13,090,000.00 USD | 13,090,000.00 USD | 151,300.00 USD | 21,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.90` | 14,320,000.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.30` | 12,920,000.00 USD | 12,920,000.00 USD | 406,260.00 USD | 37,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.90` | 12,710,000.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.10` | 12,480,000.00 USD | 12,480,000.00 USD | 1,120,000.00 USD | 48,550.00 USD | 44,130.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.90` | 11,260,000.00 USD | 11,260,000.00 USD | 186,390.00 USD | 211,140.00 USD | 187,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.90` | 12,590,000.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.70` | 10,680,000.00 USD | 10,680,000.00 USD | 1,190,000.00 USD | 166,060.00 USD | 315,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.90` | 12,460,000.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.50` | 9,000,000.00 USD | 9,000,000.00 USD | 530,770.00 USD | 140,450.00 USD | 829,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.90` | 11,820,000.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.30` | 7,500,000.00 USD | 7,500,000.00 USD | 532,160.00 USD | 87,180.00 USD | 1,140,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.90` | 9,550,000.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.10` | 5,750,000.00 USD | 5,750,000.00 USD | 502,870.00 USD | 29,070.00 USD | 264,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.90` | 4,950,000.00 USD | 4,950,000.00 USD | 115,540.00 USD | 199,550.00 USD | 307,460.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.90` | 8,340,000.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.70` | 4,330,000.00 USD | 4,330,000.00 USD | 184,180.00 USD | 71,280.00 USD | 104,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.90` | 8,050,000.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `692.50` | 3,970,000.00 USD | 3,970,000.00 USD | 673,080.00 USD | 46,300.00 USD | 69,760.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 5,920,000.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.30` | 3,180,000.00 USD | 3,180,000.00 USD | 74,030.00 USD | 162,210.00 USD | 69,370.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.90` | 4,770,000.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.10` | 2,870,000.00 USD | 2,870,000.00 USD | 246,300.00 USD | 177,770.00 USD | 363,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.90` | 2,080,000.00 USD | 2,080,000.00 USD | 306,060.00 USD | 64,240.00 USD | 264,840.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.90` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.70` | 1,450,000.00 USD | 1,450,000.00 USD | 153,900.00 USD | 34,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.90` | 3,660,000.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.50` | 1,260,000.00 USD | 1,260,000.00 USD | 0.00 USD | 32,060.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `697.30` | 1,230,000.00 USD | 1,230,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.10` | 1,170,000.00 USD | 1,170,000.00 USD | 203,360.00 USD | 0.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.90` | 937,420.00 USD | 937,420.00 USD | 276,500.00 USD | 31,670.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.90` | 3,530,000.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.70` | 586,600.00 USD | 586,600.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.50` | 452,600.00 USD | 452,600.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.90` | 2,960,000.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 2,880,000.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.10` | 262,480.00 USD | 262,480.00 USD | 227,540.00 USD | 34,930.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.90` | 2,690,000.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.90` | 2,580,000.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.90` | 1,550,000.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `706.10` | 121,180.00 USD | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `709.90` | 677,910.00 USD | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `710.90` | 502,620.00 USD | 502,620.00 USD | 343,540.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `711.70` | 850,080.00 USD | 850,080.00 USD | 308,680.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `714.10` | 894,210.00 USD | 894,210.00 USD | 0.00 USD | 0.00 USD | 44,130.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `714.90` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 63,380.00 USD | 504,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `715.70` | 2,750,000.00 USD | 2,750,000.00 USD | 181,810.00 USD | 64,780.00 USD | 1,040,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `716.50` | 3,050,000.00 USD | 3,050,000.00 USD | 51,080.00 USD | 24,200.00 USD | 225,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `717.30` | 3,690,000.00 USD | 3,690,000.00 USD | 273,400.00 USD | 24,690.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.10` | 4,510,000.00 USD | 4,510,000.00 USD | 673,150.00 USD | 20,360.00 USD | 124,850.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `718.90` | 5,080,000.00 USD | 5,080,000.00 USD | 115,540.00 USD | 117,390.00 USD | 341,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.70` | 5,270,000.00 USD | 5,270,000.00 USD | 60,590.00 USD | 71,280.00 USD | 52,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `720.50` | 6,390,000.00 USD | 6,390,000.00 USD | 988,460.00 USD | 31,410.00 USD | 102,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 376.82 USD | 376.82 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.30` | 7,140,000.00 USD | 7,140,000.00 USD | 177,520.00 USD | 443,160.00 USD | 127,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,040.00 USD | 33,420.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.10` | 7,910,000.00 USD | 7,910,000.00 USD | 348,340.00 USD | 110,100.00 USD | 319,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 1,950.00 USD | 35,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `722.90` | 8,500,000.00 USD | 8,500,000.00 USD | 191,050.00 USD | 130,270.00 USD | 266,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 2,170.00 USD | 37,540.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.70` | 9,550,000.00 USD | 9,550,000.00 USD | 446,650.00 USD | 508,710.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `724.50` | 9,950,000.00 USD | 9,950,000.00 USD | 327,200.00 USD | 79,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 38,070.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `725.30` | 10,420,000.00 USD | 10,420,000.00 USD | 321,800.00 USD | 120,790.00 USD | 18,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 39,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `726.10` | 10,640,000.00 USD | 10,640,000.00 USD | 192,360.00 USD | 10,760.00 USD | 19,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 3,710.00 USD | 43,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.90` | 11,240,000.00 USD | 11,240,000.00 USD | 502,670.00 USD | 75,120.00 USD | 24,380.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 342.65 USD | 43,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.70` | 11,630,000.00 USD | 11,630,000.00 USD | 339,770.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `728.50` | 11,860,000.00 USD | 11,860,000.00 USD | 157,160.00 USD | 5,290.00 USD | 71,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,080.00 USD | 84,720.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.30` | 13,320,000.00 USD | 13,320,000.00 USD | 359,560.00 USD | 374,970.00 USD | 724,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 171,010.00 USD | 255,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.10` | 15,740,000.00 USD | 15,740,000.00 USD | 2,020,000.00 USD | 333,240.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 28,500.00 USD | 284,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `730.90` | 19,750,000.00 USD | 19,750,000.00 USD | 1,460,000.00 USD | 315,090.00 USD | 2,240,000.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 2,050.00 USD | 286,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `731.70` | 21,290,000.00 USD | 21,290,000.00 USD | 654,700.00 USD | 170,350.00 USD | 714,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `732.50` | 23,980,000.00 USD | 23,980,000.00 USD | 1,100,000.00 USD | 113,600.00 USD | 1,470,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 140,300.00 USD | 426,580.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `733.30` | 25,510,000.00 USD | 25,510,000.00 USD | 866,380.00 USD | 184,030.00 USD | 484,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 12,260.00 USD | 438,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `734.10` | 26,400,000.00 USD | 26,400,000.00 USD | 477,580.00 USD | 204,160.00 USD | 201,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,680.00 USD | 591,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.90` | 27,480,000.00 USD | 27,480,000.00 USD | 893,060.00 USD | 167,830.00 USD | 18,290.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 26,410.00 USD | 617,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.70` | 28,610,000.00 USD | 28,610,000.00 USD | 405,830.00 USD | 101,320.00 USD | 625,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `736.50` | 29,270,000.00 USD | 29,270,000.00 USD | 389,130.00 USD | 88,890.00 USD | 181,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 20,080.00 USD | 638,020.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.30` | 29,530,000.00 USD | 29,530,000.00 USD | 145,170.00 USD | 32,120.00 USD | 88,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 8,670.00 USD | 646,690.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.10` | 30,100,000.00 USD | 30,100,000.00 USD | 338,980.00 USD | 179,820.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 59,210.00 USD | 705,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `738.90` | 31,650,000.00 USD | 31,650,000.00 USD | 603,470.00 USD | 16,030.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 129,150.00 USD | 835,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `739.70` | 31,900,000.00 USD | 31,900,000.00 USD | 222,140.00 USD | 31,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.50` | 32,270,000.00 USD | 32,270,000.00 USD | 228,370.00 USD | 134,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 6,760.00 USD | 841,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.30` | 32,680,000.00 USD | 32,680,000.00 USD | 366,560.00 USD | 32,240.00 USD | 12,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 32,060.00 USD | 873,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `742.10` | 33,010,000.00 USD | 33,010,000.00 USD | 318,870.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 67,300.00 USD | 941,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.90` | 33,250,000.00 USD | 33,250,000.00 USD | 233,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 47,230.00 USD | 988,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.70` | 33,820,000.00 USD | 33,820,000.00 USD | 112,430.00 USD | 21,120.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `744.50` | 34,970,000.00 USD | 34,970,000.00 USD | 913,440.00 USD | 236,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 1,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.30` | 36,620,000.00 USD | 36,620,000.00 USD | 700,970.00 USD | 31,390.00 USD | 923,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 26,890.00 USD | 1,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.10` | 37,470,000.00 USD | 37,470,000.00 USD | 567,430.00 USD | 135,740.00 USD | 149,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 185,960.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `746.90` | 38,740,000.00 USD | 38,740,000.00 USD | 291,780.00 USD | 37,280.00 USD | 939,640.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `747.50` | 2,010.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `747.70` | 39,300,000.00 USD | 39,300,000.00 USD | 419,020.00 USD | 37,100.00 USD | 98,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `748.50` | 39,860,000.00 USD | 39,860,000.00 USD | 390,720.00 USD | 84,260.00 USD | 91,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 4,270.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.30` | 40,160,000.00 USD | 40,160,000.00 USD | 300,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 67,670.00 USD | 1,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `750.10` | 40,430,000.00 USD | 40,430,000.00 USD | 269,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 575,140.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.90` | 40,510,000.00 USD | 40,510,000.00 USD | 79,400.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 21,390.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.70` | 41,040,000.00 USD | 41,040,000.00 USD | 112,060.00 USD | 25,010.00 USD | 393,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `752.50` | 41,530,000.00 USD | 41,530,000.00 USD | 336,940.00 USD | 0.00 USD | 146,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 48,630.00 USD | 2,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.30` | 41,920,000.00 USD | 41,920,000.00 USD | 139,220.00 USD | 3,810.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.10` | 42,390,000.00 USD | 42,390,000.00 USD | 363,270.00 USD | 50,610.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,580.00 USD | 2,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `754.90` | 42,850,000.00 USD | 42,850,000.00 USD | 277,270.00 USD | 142,490.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 3,890.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.70` | 43,210,000.00 USD | 43,210,000.00 USD | 250,440.00 USD | 96,170.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `756.50` | 43,390,000.00 USD | 43,390,000.00 USD | 100,220.00 USD | 24,970.00 USD | 54,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.30` | 43,730,000.00 USD | 43,730,000.00 USD | 155,490.00 USD | 103,180.00 USD | 73,520.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 2,010.00 USD | 2,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.10` | 44,670,000.00 USD | 44,670,000.00 USD | 656,280.00 USD | 72,680.00 USD | 218,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,980.00 USD | 3,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `758.90` | 45,030,000.00 USD | 45,030,000.00 USD | 162,660.00 USD | 137,350.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 8,560.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `759.70` | 45,450,000.00 USD | 45,450,000.00 USD | 397,100.00 USD | 21,070.00 USD | 8,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `760.50` | 45,810,000.00 USD | 45,810,000.00 USD | 274,870.00 USD | 37,300.00 USD | 42,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 6,020.00 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.30` | 46,830,000.00 USD | 46,830,000.00 USD | 756,450.00 USD | 24,020.00 USD | 235,550.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `761.50` | 367.04 USD | 3,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.10` | 46,960,000.00 USD | 46,960,000.00 USD | 65,550.00 USD | 42,210.00 USD | 26,330.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 8,050.00 USD | 3,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `762.90` | 47,760,000.00 USD | 47,760,000.00 USD | 392,000.00 USD | 61,680.00 USD | 351,620.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 595,810.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.70` | 48,190,000.00 USD | 48,190,000.00 USD | 370,320.00 USD | 42,990.00 USD | 9,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `764.50` | 48,380,000.00 USD | 48,380,000.00 USD | 137,070.00 USD | 15,480.00 USD | 40,840.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.30` | 48,650,000.00 USD | 48,650,000.00 USD | 115,580.00 USD | 117,270.00 USD | 32,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `765.50` | 785.40 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.10` | 49,220,000.00 USD | 49,220,000.00 USD | 451,950.00 USD | 35,470.00 USD | 90,350.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `766.90` | 49,540,000.00 USD | 49,540,000.00 USD | 211,510.00 USD | 12,510.00 USD | 94,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `767.50` | 2,450.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `767.70` | 50,340,000.00 USD | 50,340,000.00 USD | 734,810.00 USD | 14,040.00 USD | 44,130.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `768.50` | 50,380,000.00 USD | 50,380,000.00 USD | 9,780.00 USD | 15,850.00 USD | 20,190.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 300.48 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.30` | 50,580,000.00 USD | 50,580,000.00 USD | 164,570.00 USD | 28,060.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.10` | 50,880,000.00 USD | 50,880,000.00 USD | 203,040.00 USD | 70,230.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 661.86 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `770.90` | 51,280,000.00 USD | 51,280,000.00 USD | 4,860.00 USD | 33,850.00 USD | 361,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 395,010.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.70` | 52,070,000.00 USD | 52,070,000.00 USD | 82,150.00 USD | 96,870.00 USD | 607,180.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `772.50` | 52,500,000.00 USD | 52,500,000.00 USD | 243,310.00 USD | 133,890.00 USD | 48,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 2,450.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.30` | 53,380,000.00 USD | 53,380,000.00 USD | 745,520.00 USD | 23,860.00 USD | 111,430.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 2,200.00 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.10` | 53,560,000.00 USD | 53,560,000.00 USD | 130,070.00 USD | 26,310.00 USD | 28,310.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.90` | 53,960,000.00 USD | 53,960,000.00 USD | 249,450.00 USD | 41,190.00 USD | 107,850.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `775.50` | 544.40 USD | 4,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `775.70` | 54,190,000.00 USD | 54,190,000.00 USD | 130,910.00 USD | 24,070.00 USD | 76,830.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.50` | 54,420,000.00 USD | 54,420,000.00 USD | 149,370.00 USD | 13,880.00 USD | 65,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 89,520.00 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.30` | 54,620,000.00 USD | 54,620,000.00 USD | 181,420.00 USD | 11,790.00 USD | 5,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 4,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 8,100.00 USD | 4,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 4,150.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `784.50` | 743.71 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 1,750.00 USD | 4,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 4,780.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `786.90` | 82,500,000.00 USD | 82,500,000.00 USD | 601,980.00 USD | 28,250.00 USD | 104,290.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `787.50` | 7,880.00 USD | 4,230,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `787.90` | 82,910,000.00 USD | 82,910,000.00 USD | 261,000.00 USD | 56,730.00 USD | 91,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `788.90` | 83,800,000.00 USD | 83,800,000.00 USD | 750,800.00 USD | 111,010.00 USD | 28,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `789.50` | 798.18 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `789.90` | 84,470,000.00 USD | 84,470,000.00 USD | 327,320.00 USD | 99,920.00 USD | 244,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `790.50` | 1,230.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `790.90` | 85,300,000.00 USD | 85,300,000.00 USD | 657,830.00 USD | 107,360.00 USD | 68,600.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 86,260,000.00 USD | 86,260,000.00 USD | 841,380.00 USD | 16,830.00 USD | 96,020.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.90` | 86,480,000.00 USD | 86,480,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 1,280.00 USD | 4,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.90` | 86,640,000.00 USD | 86,640,000.00 USD | 166,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.90` | 86,900,000.00 USD | 86,900,000.00 USD | 236,740.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 96,410.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `795.90` | 87,160,000.00 USD | 87,160,000.00 USD | 93,020.00 USD | 14,650.00 USD | 154,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 567.11 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.90` | 87,250,000.00 USD | 87,250,000.00 USD | 62,760.00 USD | 33,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,760.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.90` | 87,360,000.00 USD | 87,360,000.00 USD | 103,930.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 5,310.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `800.50` | 28,250.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,410.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `802.50` | 779,990.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `803.50` | 5,930.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,600.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `807.50` | 738.06 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `809.50` | 574.75 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `811.50` | 434.15 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `815.50` | 8,150.00 USD | 5,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `818.50` | 7,720.00 USD | 5,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,710.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `822.50` | 3,540.00 USD | 5,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `826.50` | 536,790.00 USD | 5,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `827.50` | 81,670.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `828.50` | 5,880.00 USD | 5,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `829.50` | 2,900.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `836.50` | 239.24 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 3,570.00 USD | 5,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 32,510.00 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `840.50` | 679.96 USD | 5,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 4,410.00 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 171.03 USD | 5,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 34,060.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `846.50` | 1,160.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `847.50` | 289.00 USD | 5,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 393.78 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 2,110.00 USD | 5,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `856.50` | 29,740.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `857.50` | 5,050.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 523,680.00 USD | 6,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `862.50` | 1,480.00 USD | 6,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `864.50` | 289,650.00 USD | 6,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `873.50` | 326.69 USD | 6,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `875.50` | 14,000.00 USD | 6,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 702,210.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 4,540.00 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 7,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 2,580.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 3,950.00 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 7,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 7,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 254,270.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 249.23 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `897.50` | 126,180.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 5,400.00 USD | 7,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 90,560.00 USD | 8,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `903.50` | 5,470.00 USD | 8,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 100,930.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `905.50` | 107.75 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 268,530.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 2,420.00 USD | 8,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 29,900.00 USD | 8,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 34,790.00 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `912.50` | 116.80 USD | 8,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 13,930.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `915.50` | 390.00 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 206.66 USD | 8,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,830.00 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `927.50` | 651.10 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 956.93 USD | 8,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 3,810.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `936.50` | 121,750.00 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `942.50` | 963.24 USD | 8,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `948.50` | 66,390.00 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `951.50` | 676.52 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `954.50` | 19,120.00 USD | 8,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `957.50` | 9,620.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `958.50` | 114.06 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `960.50` | 204.59 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 14,110.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `972.50` | 1,950.00 USD | 8,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `978.50` | 63,360.00 USD | 8,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 1,280.00 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `986.50` | 612.62 USD | 8,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,140.00 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 975.62 USD | 8,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 313.58 USD | 9,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 989.52 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 9,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 337,490.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 99,950.00 USD | 9,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 34,290.00 USD | 9,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 9,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 29,110.00 USD | 9,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,370.00 USD | 9,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1012.50` | 13,440.00 USD | 9,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 760,880.00 USD | 10,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1016.50` | 14,880.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 10,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1032.50` | 720,280.00 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1038.50` | 500.56 USD | 11,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1040.50` | 65,030.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 7,000.00 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1062.50` | 635.38 USD | 11,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,760.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1069.50` | 119.78 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 11,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1075.50` | 68,740.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1077.50` | 1,560.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 11,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 15,780.00 USD | 11,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 120,790.00 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1096.50` | 810.31 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1103.50` | 461.26 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1109.50` | 237.43 USD | 11,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1111.50` | 177,260.00 USD | 11,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1120.50` | 76,470.00 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1123.50` | 352.78 USD | 11,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1126.50` | 20,080.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1136.50` | 152.29 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 349,310.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1145.50` | 1,530.00 USD | 12,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1157.50` | 11,750.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1166.50` | 20,250.00 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1168.50` | 156.58 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1175.50` | 122.25 USD | 12,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1180.50` | 5,060.00 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1199.50` | 169.13 USD | 12,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1202.50` | 118,760.00 USD | 12,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1203.50` | 2,370.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1219.50` | 73,150.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 1,400.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1228.50` | 63,080.00 USD | 12,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1244.50` | 2,660.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 2,050.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 1,650.00 USD | 12,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1256.50` | 5,020.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1257.50` | 201.20 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1258.50` | 113,270.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1260.50` | 1,260.00 USD | 12,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1264.50` | 6,850.00 USD | 12,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1266.50` | 25,330.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1268.50` | 24,630.00 USD | 12,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1271.50` | 18,990.00 USD | 12,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1276.50` | 108,890.00 USD | 12,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1279.50` | 617,840.00 USD | 13,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 1,810.00 USD | 13,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1284.50` | 18,070.00 USD | 13,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1287.50` | 61,960.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1290.50` | 349.73 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1297.50` | 224.47 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1305.50` | 100.52 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1308.50` | 4,050.00 USD | 13,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1310.50` | 1,850,000.00 USD | 15,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1314.50` | 166,790.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1315.50` | 2,630.00 USD | 15,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 242.93 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 184.66 USD | 15,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1331.50` | 30,620.00 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1332.50` | 210.53 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1337.50` | 58,170.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 494.28 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1344.50` | 4,210.00 USD | 15,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1347.50` | 94,330.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1359.50` | 121.00 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1371.50` | 4,110.00 USD | 15,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1382.50` | 69,120.00 USD | 15,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `141.50` | 5,140,000.00 USD | 0.00 USD | 5,520.00 USD | `-79.83%` | `38,980,000,000.00` |
| `Live` | `Long` | `143.50` | 5,140,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.55%` | `20,000,000,000.00` |
| `Live` | `Long` | `146.50` | 5,130,000.00 USD | 0.00 USD | 280.69 USD | `-79.12%` | `1,916,000,000.00` |
| `Live` | `Long` | `147.50` | 5,130,000.00 USD | 0.00 USD | 6,230.00 USD | `-78.98%` | `42,261,000,000.00` |
| `Live` | `Long` | `163.50` | 5,130,000.00 USD | 0.00 USD | 98,100.00 USD | `-76.69%` | `600,000,000,000.00` |
| `Live` | `Long` | `170.50` | 5,030,000.00 USD | 0.00 USD | 1,030.00 USD | `-75.70%` | `6,050,000,000.00` |
| `Live` | `Long` | `178.50` | 5,030,000.00 USD | 0.00 USD | 6,290.00 USD | `-74.56%` | `35,251,000,000.00` |
| `Live` | `Long` | `194.50` | 5,020,000.00 USD | 0.00 USD | 351.66 USD | `-72.28%` | `1,808,000,000.00` |
| `Live` | `Long` | `202.50` | 5,020,000.00 USD | 0.00 USD | 20,250.00 USD | `-71.14%` | `100,000,000,000.00` |
| `Live` | `Long` | `204.50` | 5,000,000.00 USD | 0.00 USD | 310,870.00 USD | `-70.85%` | `1,520,143,000,000.00` |
| `Live` | `Long` | `207.50` | 4,690,000.00 USD | 0.00 USD | 590.75 USD | `-70.42%` | `2,847,000,000.00` |
| `Live` | `Long` | `209.50` | 4,690,000.00 USD | 0.00 USD | 257.06 USD | `-70.14%` | `1,227,000,000.00` |
| `Live` | `Long` | `218.50` | 4,690,000.00 USD | 0.00 USD | 190.31 USD | `-68.85%` | `871,000,000.00` |
| `Live` | `Long` | `235.50` | 4,690,000.00 USD | 0.00 USD | 909.03 USD | `-66.43%` | `3,860,000,000.00` |
| `Live` | `Long` | `240.50` | 4,690,000.00 USD | 0.00 USD | 165.22 USD | `-65.72%` | `687,000,000.00` |
| `Live` | `Long` | `249.50` | 4,690,000.00 USD | 0.00 USD | 998.00 USD | `-64.44%` | `4,000,000,000.00` |
| `Live` | `Long` | `250.50` | 4,690,000.00 USD | 0.00 USD | 1,320.00 USD | `-64.29%` | `5,281,000,000.00` |
| `Live` | `Long` | `261.50` | 4,690,000.00 USD | 0.00 USD | 397.74 USD | `-62.73%` | `1,521,000,000.00` |
| `Live` | `Long` | `267.50` | 4,690,000.00 USD | 0.00 USD | 267,500.00 USD | `-61.87%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `268.50` | 4,420,000.00 USD | 0.00 USD | 21,280.00 USD | `-61.73%` | `79,269,000,000.00` |
| `Live` | `Long` | `280.50` | 4,400,000.00 USD | 0.00 USD | 11,220.00 USD | `-60.02%` | `40,000,000,000.00` |
| `Live` | `Long` | `294.50` | 4,390,000.00 USD | 0.00 USD | 361.94 USD | `-58.02%` | `1,229,000,000.00` |
| `Live` | `Long` | `305.50` | 4,390,000.00 USD | 0.00 USD | 21,220.00 USD | `-56.45%` | `69,447,000,000.00` |
| `Live` | `Long` | `310.50` | 4,360,000.00 USD | 0.00 USD | 154,740.00 USD | `-55.74%` | `498,365,000,000.00` |
| `Live` | `Long` | `312.50` | 4,210,000.00 USD | 0.00 USD | 500.00 USD | `-55.46%` | `1,600,000,000.00` |
| `Live` | `Long` | `315.50` | 4,210,000.00 USD | 0.00 USD | 5,610.00 USD | `-55.03%` | `17,770,000,000.00` |
| `Live` | `Long` | `326.50` | 4,200,000.00 USD | 0.00 USD | 500.85 USD | `-53.46%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,200,000.00 USD | 0.00 USD | 314.07 USD | `-53.32%` | `959,000,000.00` |
| `Live` | `Long` | `329.50` | 4,200,000.00 USD | 0.00 USD | 8,540.00 USD | `-53.03%` | `25,914,000,000.00` |
| `Live` | `Long` | `332.50` | 4,190,000.00 USD | 0.00 USD | 376.06 USD | `-52.60%` | `1,131,000,000.00` |
| `Live` | `Long` | `342.50` | 4,190,000.00 USD | 0.00 USD | 650.75 USD | `-51.18%` | `1,900,000,000.00` |
| `Live` | `Long` | `348.50` | 4,190,000.00 USD | 0.00 USD | 1,090.00 USD | `-50.32%` | `3,120,000,000.00` |
| `Live` | `Long` | `352.50` | 4,190,000.00 USD | 0.00 USD | 1,260.00 USD | `-49.75%` | `3,573,000,000.00` |
| `Live` | `Long` | `359.50` | 4,190,000.00 USD | 0.00 USD | 212.10 USD | `-48.76%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,190,000.00 USD | 0.00 USD | 340.60 USD | `-48.19%` | `937,000,000.00` |
| `Live` | `Long` | `366.50` | 4,190,000.00 USD | 0.00 USD | 2,200.00 USD | `-47.76%` | `6,004,000,000.00` |
| `Live` | `Long` | `367.50` | 4,190,000.00 USD | 0.00 USD | 15,770.00 USD | `-47.62%` | `42,904,000,000.00` |
| `Live` | `Long` | `370.50` | 4,170,000.00 USD | 0.00 USD | 150.79 USD | `-47.19%` | `407,000,000.00` |
| `Live` | `Long` | `371.50` | 4,170,000.00 USD | 0.00 USD | 10,480.00 USD | `-47.05%` | `28,204,000,000.00` |
| `Live` | `Long` | `373.50` | 4,160,000.00 USD | 0.00 USD | 17,600.00 USD | `-46.76%` | `47,130,000,000.00` |
| `Live` | `Long` | `377.50` | 4,140,000.00 USD | 0.00 USD | 1,400.00 USD | `-46.19%` | `3,716,000,000.00` |
| `Live` | `Long` | `378.50` | 4,140,000.00 USD | 0.00 USD | 643.45 USD | `-46.05%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 4,140,000.00 USD | 0.00 USD | 19,070.00 USD | `-45.62%` | `50,000,000,000.00` |
| `Live` | `Long` | `382.50` | 4,120,000.00 USD | 0.00 USD | 10,870.00 USD | `-45.48%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 4,110,000.00 USD | 0.00 USD | 2,510.00 USD | `-45.19%` | `6,536,000,000.00` |
| `Live` | `Long` | `385.50` | 4,110,000.00 USD | 0.00 USD | 341.17 USD | `-45.05%` | `885,000,000.00` |
| `Live` | `Long` | `386.50` | 4,110,000.00 USD | 0.00 USD | 531.44 USD | `-44.91%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 4,110,000.00 USD | 0.00 USD | 392.54 USD | `-44.77%` | `1,013,000,000.00` |
| `Live` | `Long` | `388.50` | 4,110,000.00 USD | 0.00 USD | 601.01 USD | `-44.62%` | `1,547,000,000.00` |
| `Live` | `Long` | `390.50` | 4,110,000.00 USD | 0.00 USD | 3,370.00 USD | `-44.34%` | `8,638,000,000.00` |
| `Live` | `Long` | `392.50` | 4,100,000.00 USD | 0.00 USD | 7,560.00 USD | `-44.05%` | `19,264,000,000.00` |
| `Live` | `Long` | `393.50` | 4,100,000.00 USD | 0.00 USD | 600.48 USD | `-43.91%` | `1,526,000,000.00` |
| `Live` | `Long` | `394.50` | 4,100,000.00 USD | 0.00 USD | 1,950.00 USD | `-43.77%` | `4,947,000,000.00` |
| `Live` | `Long` | `395.50` | 4,090,000.00 USD | 0.00 USD | 158.20 USD | `-43.62%` | `400,000,000.00` |
| `Live` | `Long` | `396.50` | 4,090,000.00 USD | 0.00 USD | 317.20 USD | `-43.48%` | `800,000,000.00` |
| `Live` | `Long` | `397.50` | 4,090,000.00 USD | 0.00 USD | 522.32 USD | `-43.34%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 4,090,000.00 USD | 0.00 USD | 603.64 USD | `-43.05%` | `1,511,000,000.00` |
| `Live` | `Long` | `400.50` | 4,090,000.00 USD | 0.00 USD | 1,700.00 USD | `-42.91%` | `4,250,000,000.00` |
| `Live` | `Long` | `403.50` | 4,090,000.00 USD | 0.00 USD | 102.09 USD | `-42.48%` | `253,000,000.00` |
| `Live` | `Long` | `409.50` | 4,090,000.00 USD | 0.00 USD | 613.02 USD | `-41.63%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 4,090,000.00 USD | 0.00 USD | 105.91 USD | `-41.49%` | `258,000,000.00` |
| `Live` | `Long` | `412.50` | 4,090,000.00 USD | 0.00 USD | 3,490.00 USD | `-41.20%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 4,090,000.00 USD | 0.00 USD | 9,800.00 USD | `-41.06%` | `23,702,000,000.00` |
| `Live` | `Long` | `414.50` | 4,080,000.00 USD | 0.00 USD | 3,700.00 USD | `-40.92%` | `8,934,000,000.00` |
| `Live` | `Long` | `415.50` | 4,070,000.00 USD | 0.00 USD | 526.02 USD | `-40.77%` | `1,266,000,000.00` |
| `Live` | `Long` | `416.50` | 4,070,000.00 USD | 0.00 USD | 2,350.00 USD | `-40.63%` | `5,644,000,000.00` |
| `Live` | `Long` | `417.50` | 4,070,000.00 USD | 0.00 USD | 5,680.00 USD | `-40.49%` | `13,599,000,000.00` |
| `Live` | `Long` | `418.50` | 4,060,000.00 USD | 0.00 USD | 318.06 USD | `-40.35%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 4,060,000.00 USD | 0.00 USD | 2,650.00 USD | `-40.20%` | `6,316,000,000.00` |
| `Live` | `Long` | `421.50` | 4,060,000.00 USD | 0.00 USD | 2,320.00 USD | `-39.92%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 4,060,000.00 USD | 0.00 USD | 1,440.00 USD | `-39.78%` | `3,419,000,000.00` |
| `Live` | `Long` | `424.50` | 4,060,000.00 USD | 0.00 USD | 29,710.00 USD | `-39.49%` | `70,000,000,000.00` |
| `Live` | `Long` | `429.50` | 4,030,000.00 USD | 0.00 USD | 846.12 USD | `-38.78%` | `1,970,000,000.00` |
| `Live` | `Long` | `436.50` | 4,030,000.00 USD | 0.00 USD | 3,540.00 USD | `-37.78%` | `8,104,000,000.00` |
| `Live` | `Long` | `438.50` | 4,020,000.00 USD | 0.00 USD | 1,790.00 USD | `-37.50%` | `4,087,000,000.00` |
| `Live` | `Long` | `445.50` | 4,020,000.00 USD | 0.00 USD | 33,080.00 USD | `-36.50%` | `74,245,000,000.00` |
| `Live` | `Long` | `447.50` | 3,990,000.00 USD | 0.00 USD | 223.75 USD | `-36.21%` | `500,000,000.00` |
| `Live` | `Long` | `448.50` | 3,990,000.00 USD | 0.00 USD | 3,350.00 USD | `-36.07%` | `7,470,000,000.00` |
| `Live` | `Long` | `452.50` | 3,990,000.00 USD | 0.00 USD | 957.04 USD | `-35.50%` | `2,115,000,000.00` |
| `Live` | `Long` | `456.50` | 3,980,000.00 USD | 0.00 USD | 4,730.00 USD | `-34.93%` | `10,359,000,000.00` |
| `Live` | `Long` | `457.50` | 3,980,000.00 USD | 0.00 USD | 1,490.00 USD | `-34.79%` | `3,259,000,000.00` |
| `Live` | `Long` | `463.50` | 3,980,000.00 USD | 0.00 USD | 927.00 USD | `-33.93%` | `2,000,000,000.00` |
| `Live` | `Long` | `469.50` | 3,980,000.00 USD | 0.00 USD | 4,370.00 USD | `-33.08%` | `9,301,000,000.00` |
| `Live` | `Long` | `470.50` | 3,970,000.00 USD | 0.00 USD | 202.31 USD | `-32.93%` | `430,000,000.00` |
| `Live` | `Long` | `473.50` | 3,970,000.00 USD | 0.00 USD | 8,320.00 USD | `-32.51%` | `17,576,000,000.00` |
| `Live` | `Long` | `475.50` | 3,960,000.00 USD | 0.00 USD | 5,320.00 USD | `-32.22%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,960,000.00 USD | 0.00 USD | 615.36 USD | `-31.37%` | `1,278,000,000.00` |
| `Live` | `Long` | `483.50` | 3,960,000.00 USD | 0.00 USD | 483.50 USD | `-31.08%` | `1,000,000,000.00` |
| `Live` | `Long` | `484.50` | 3,960,000.00 USD | 0.00 USD | 2,840.00 USD | `-30.94%` | `5,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,960,000.00 USD | 0.00 USD | 2,400.00 USD | `-30.80%` | `4,947,000,000.00` |
| `Live` | `Long` | `486.50` | 3,950,000.00 USD | 0.00 USD | 207.25 USD | `-30.65%` | `426,000,000.00` |
| `Live` | `Long` | `487.50` | 3,950,000.00 USD | 0.00 USD | 2,070.00 USD | `-30.51%` | `4,238,000,000.00` |
| `Live` | `Long` | `488.50` | 3,950,000.00 USD | 0.00 USD | 3,490.00 USD | `-30.37%` | `7,144,000,000.00` |
| `Live` | `Long` | `493.50` | 3,950,000.00 USD | 0.00 USD | 2,270.00 USD | `-29.66%` | `4,598,000,000.00` |
| `Live` | `Long` | `498.50` | 3,940,000.00 USD | 0.00 USD | 11,260.00 USD | `-28.94%` | `22,583,000,000.00` |
| `Live` | `Long` | `499.50` | 3,930,000.00 USD | 0.00 USD | 4,470.00 USD | `-28.80%` | `8,957,000,000.00` |
| `Live` | `Long` | `500.50` | 3,930,000.00 USD | 0.00 USD | 186.69 USD | `-28.66%` | `373,000,000.00` |
| `Live` | `Long` | `501.50` | 3,930,000.00 USD | 0.00 USD | 14,130.00 USD | `-28.52%` | `28,185,000,000.00` |
| `Live` | `Long` | `502.50` | 3,910,000.00 USD | 0.00 USD | 109.04 USD | `-28.37%` | `217,000,000.00` |
| `Live` | `Long` | `504.50` | 3,910,000.00 USD | 0.00 USD | 3,500.00 USD | `-28.09%` | `6,944,000,000.00` |
| `Live` | `Long` | `505.50` | 3,910,000.00 USD | 0.00 USD | 5,760.00 USD | `-27.95%` | `11,387,000,000.00` |
| `Live` | `Long` | `507.50` | 3,910,000.00 USD | 0.00 USD | 1,050.00 USD | `-27.66%` | `2,073,000,000.00` |
| `Live` | `Long` | `508.50` | 3,900,000.00 USD | 0.00 USD | 2,750.00 USD | `-27.52%` | `5,411,000,000.00` |
| `Live` | `Long` | `509.50` | 3,900,000.00 USD | 0.00 USD | 1,710.00 USD | `-27.38%` | `3,365,000,000.00` |
| `Live` | `Long` | `510.50` | 3,900,000.00 USD | 0.00 USD | 4,080.00 USD | `-27.23%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,900,000.00 USD | 0.00 USD | 5,180.00 USD | `-27.09%` | `10,118,000,000.00` |
| `Live` | `Long` | `512.50` | 3,890,000.00 USD | 0.00 USD | 73,860.00 USD | `-26.95%` | `144,110,000,000.00` |
| `Live` | `Long` | `513.50` | 3,820,000.00 USD | 0.00 USD | 3,220.00 USD | `-26.80%` | `6,263,000,000.00` |
| `Live` | `Long` | `515.50` | 3,810,000.00 USD | 0.00 USD | 6,470.00 USD | `-26.52%` | `12,554,000,000.00` |
| `Live` | `Long` | `517.50` | 3,810,000.00 USD | 0.00 USD | 22,650.00 USD | `-26.23%` | `43,765,000,000.00` |
| `Live` | `Long` | `518.50` | 3,780,000.00 USD | 0.00 USD | 263.92 USD | `-26.09%` | `509,000,000.00` |
| `Live` | `Long` | `519.50` | 3,780,000.00 USD | 0.00 USD | 703.92 USD | `-25.95%` | `1,355,000,000.00` |
| `Live` | `Long` | `520.50` | 3,780,000.00 USD | 0.00 USD | 43,270.00 USD | `-25.81%` | `83,133,000,000.00` |
| `Live` | `Long` | `521.50` | 3,740,000.00 USD | 0.00 USD | 838.05 USD | `-25.66%` | `1,607,000,000.00` |
| `Live` | `Long` | `522.50` | 3,740,000.00 USD | 0.00 USD | 2,090.00 USD | `-25.52%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 3,740,000.00 USD | 0.00 USD | 833.43 USD | `-25.24%` | `1,589,000,000.00` |
| `Live` | `Long` | `525.50` | 3,740,000.00 USD | 0.00 USD | 289.03 USD | `-25.09%` | `550,000,000.00` |
| `Live` | `Long` | `526.50` | 3,740,000.00 USD | 0.00 USD | 1,410.00 USD | `-24.95%` | `2,684,000,000.00` |
| `Live` | `Long` | `528.50` | 3,730,000.00 USD | 0.00 USD | 63,390.00 USD | `-24.67%` | `119,940,000,000.00` |
| `Live` | `Long` | `529.50` | 3,670,000.00 USD | 0.00 USD | 59,770.00 USD | `-24.52%` | `112,879,000,000.00` |
| `Live` | `Long` | `530.50` | 3,610,000.00 USD | 0.00 USD | 3,220.00 USD | `-24.38%` | `6,071,000,000.00` |
| `Live` | `Long` | `531.50` | 3,610,000.00 USD | 0.00 USD | 208.88 USD | `-24.24%` | `393,000,000.00` |
| `Live` | `Long` | `532.50` | 3,610,000.00 USD | 0.00 USD | 751.36 USD | `-24.10%` | `1,411,000,000.00` |
| `Live` | `Long` | `534.50` | 3,610,000.00 USD | 0.00 USD | 55,510.00 USD | `-23.81%` | `103,850,000,000.00` |
| `Live` | `Long` | `535.50` | 3,550,000.00 USD | 0.00 USD | 182,620.00 USD | `-23.67%` | `341,026,000,000.00` |
| `Live` | `Long` | `539.50` | 3,370,000.00 USD | 0.00 USD | 490.94 USD | `-23.10%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,370,000.00 USD | 0.00 USD | 471.32 USD | `-22.96%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,370,000.00 USD | 0.00 USD | 2,680.00 USD | `-22.53%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,370,000.00 USD | 0.00 USD | 210,830.00 USD | `-22.39%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 3,150,000.00 USD | 0.00 USD | 1,580.00 USD | `-22.24%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,150,000.00 USD | 0.00 USD | 530.11 USD | `-22.10%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,150,000.00 USD | 0.00 USD | 1,980.00 USD | `-21.82%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 3,150,000.00 USD | 0.00 USD | 1,370.00 USD | `-21.67%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,150,000.00 USD | 0.00 USD | 633.63 USD | `-21.53%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 3,150,000.00 USD | 0.00 USD | 1,250.00 USD | `-21.39%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 3,150,000.00 USD | 0.00 USD | 12,560.00 USD | `-21.25%` | `22,739,000,000.00` |
| `Live` | `Long` | `553.50` | 3,140,000.00 USD | 0.00 USD | 2,740.00 USD | `-21.10%` | `4,955,000,000.00` |
| `Live` | `Long` | `555.50` | 3,130,000.00 USD | 0.00 USD | 81,680.00 USD | `-20.82%` | `147,042,000,000.00` |
| `Live` | `Long` | `556.50` | 3,050,000.00 USD | 0.00 USD | 5,670.00 USD | `-20.68%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 3,040,000.00 USD | 0.00 USD | 791.65 USD | `-20.53%` | `1,420,000,000.00` |
| `Live` | `Long` | `560.50` | 3,040,000.00 USD | 0.00 USD | 582.36 USD | `-20.11%` | `1,039,000,000.00` |
| `Live` | `Long` | `561.50` | 3,040,000.00 USD | 0.00 USD | 1,510.00 USD | `-19.96%` | `2,682,000,000.00` |
| `Live` | `Long` | `567.50` | 3,040,000.00 USD | 0.00 USD | 391.57 USD | `-19.11%` | `690,000,000.00` |
| `Live` | `Long` | `569.50` | 3,040,000.00 USD | 0.00 USD | 144.08 USD | `-18.82%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 3,040,000.00 USD | 0.00 USD | 733,410.00 USD | `-18.54%` | `1,283,300,000,000.00` |
| `Live` | `Long` | `574.50` | 2,310,000.00 USD | 0.00 USD | 323.44 USD | `-18.11%` | `563,000,000.00` |
| `Live` | `Long` | `575.50` | 2,310,000.00 USD | 0.00 USD | 460.40 USD | `-17.97%` | `800,000,000.00` |
| `Live` | `Long` | `576.50` | 2,310,000.00 USD | 0.00 USD | 19,800.00 USD | `-17.82%` | `34,349,000,000.00` |
| `Live` | `Long` | `577.50` | 2,290,000.00 USD | 0.00 USD | 5,780.00 USD | `-17.68%` | `10,000,000,000.00` |
| `Live` | `Long` | `578.50` | 2,280,000.00 USD | 0.00 USD | 1,850.00 USD | `-17.54%` | `3,202,000,000.00` |
| `Live` | `Long` | `580.50` | 2,280,000.00 USD | 0.00 USD | 35,850.00 USD | `-17.25%` | `61,765,000,000.00` |
| `Live` | `Long` | `582.50` | 2,240,000.00 USD | 0.00 USD | 690.26 USD | `-16.97%` | `1,185,000,000.00` |
| `Live` | `Long` | `583.50` | 2,240,000.00 USD | 0.00 USD | 3,060.00 USD | `-16.83%` | `5,239,000,000.00` |
| `Live` | `Long` | `584.50` | 2,240,000.00 USD | 0.00 USD | 165,820.00 USD | `-16.68%` | `283,700,000,000.00` |
| `Live` | `Long` | `585.50` | 2,070,000.00 USD | 0.00 USD | 210.19 USD | `-16.54%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,070,000.00 USD | 0.00 USD | 2,360.00 USD | `-16.40%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,070,000.00 USD | 0.00 USD | 5,490.00 USD | `-16.26%` | `9,339,000,000.00` |
| `Live` | `Long` | `588.50` | 2,070,000.00 USD | 0.00 USD | 397.24 USD | `-16.11%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 2,070,000.00 USD | 0.00 USD | 16,680.00 USD | `-15.97%` | `28,299,000,000.00` |
| `Live` | `Long` | `590.50` | 2,050,000.00 USD | 0.00 USD | 2,420.00 USD | `-15.83%` | `4,106,000,000.00` |
| `Live` | `Long` | `592.50` | 2,050,000.00 USD | 0.00 USD | 226.93 USD | `-15.54%` | `383,000,000.00` |
| `Live` | `Long` | `593.50` | 2,050,000.00 USD | 0.00 USD | 44,960.00 USD | `-15.40%` | `75,762,000,000.00` |
| `Live` | `Long` | `595.50` | 2,000,000.00 USD | 0.00 USD | 940.89 USD | `-15.12%` | `1,580,000,000.00` |
| `Live` | `Long` | `596.50` | 2,000,000.00 USD | 0.00 USD | 7,680.00 USD | `-14.97%` | `12,878,000,000.00` |
| `Live` | `Long` | `597.50` | 1,990,000.00 USD | 0.00 USD | 2,480.00 USD | `-14.83%` | `4,156,000,000.00` |
| `Live` | `Long` | `598.50` | 1,990,000.00 USD | 0.00 USD | 791.22 USD | `-14.69%` | `1,322,000,000.00` |
| `Live` | `Long` | `600.50` | 1,990,000.00 USD | 0.00 USD | 945.19 USD | `-14.40%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,990,000.00 USD | 0.00 USD | 16,880.00 USD | `-14.26%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,970,000.00 USD | 0.00 USD | 222.32 USD | `-14.12%` | `369,000,000.00` |
| `Live` | `Long` | `603.50` | 1,970,000.00 USD | 0.00 USD | 22,860.00 USD | `-13.98%` | `37,877,000,000.00` |
| `Live` | `Long` | `604.50` | 1,950,000.00 USD | 0.00 USD | 10,310.00 USD | `-13.83%` | `17,049,000,000.00` |
| `Live` | `Long` | `605.50` | 1,940,000.00 USD | 0.00 USD | 58,420.00 USD | `-13.69%` | `96,477,000,000.00` |
| `Live` | `Long` | `606.50` | 1,880,000.00 USD | 0.00 USD | 1,880.00 USD | `-13.55%` | `3,092,000,000.00` |
| `Live` | `Long` | `609.50` | 1,880,000.00 USD | 0.00 USD | 213.32 USD | `-13.12%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,880,000.00 USD | 0.00 USD | 5,860.00 USD | `-12.84%` | `9,586,000,000.00` |
| `Live` | `Long` | `612.50` | 1,870,000.00 USD | 0.00 USD | 12,250.00 USD | `-12.69%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,860,000.00 USD | 0.00 USD | 120.25 USD | `-12.55%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,860,000.00 USD | 0.00 USD | 4,280.00 USD | `-12.41%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,860,000.00 USD | 0.00 USD | 1,540.00 USD | `-12.12%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,850,000.00 USD | 0.00 USD | 156.23 USD | `-11.98%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,850,000.00 USD | 0.00 USD | 932.70 USD | `-11.84%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,850,000.00 USD | 0.00 USD | 1,410.00 USD | `-11.70%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,850,000.00 USD | 0.00 USD | 6,520.00 USD | `-11.55%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,850,000.00 USD | 0.00 USD | 696.70 USD | `-11.41%` | `1,121,000,000.00` |
| `Live` | `Long` | `623.50` | 1,840,000.00 USD | 0.00 USD | 415.25 USD | `-11.13%` | `666,000,000.00` |
| `Live` | `Long` | `624.50` | 1,840,000.00 USD | 0.00 USD | 25,400.00 USD | `-10.98%` | `40,673,000,000.00` |
| `Live` | `Long` | `625.50` | 1,820,000.00 USD | 0.00 USD | 14,200.00 USD | `-10.84%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,800,000.00 USD | 0.00 USD | 964.81 USD | `-10.70%` | `1,540,000,000.00` |
| `Live` | `Long` | `628.50` | 1,800,000.00 USD | 0.00 USD | 148.95 USD | `-10.41%` | `237,000,000.00` |
| `Live` | `Long` | `630.50` | 1,800,000.00 USD | 0.00 USD | 153.21 USD | `-10.13%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,800,000.00 USD | 0.00 USD | 2,900.00 USD | `-9.99%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,800,000.00 USD | 0.00 USD | 3,560.00 USD | `-9.84%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,800,000.00 USD | 0.00 USD | 5,900.00 USD | `-9.56%` | `9,302,000,000.00` |
| `Live` | `Long` | `635.50` | 1,790,000.00 USD | 0.00 USD | 155.06 USD | `-9.41%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,790,000.00 USD | 0.00 USD | 1,110.00 USD | `-9.27%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,790,000.00 USD | 0.00 USD | 305.36 USD | `-9.13%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,790,000.00 USD | 0.00 USD | 6,710.00 USD | `-8.99%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,780,000.00 USD | 0.00 USD | 1,490.00 USD | `-8.84%` | `2,333,000,000.00` |
| `Live` | `Long` | `640.50` | 1,780,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-8.70%` | `2,057,820,000,000.00` |
| `Live` | `Long` | `642.50` | 462,900.00 USD | 0.00 USD | 8,480.00 USD | `-8.42%` | `13,199,000,000.00` |
| `Live` | `Long` | `643.50` | 454,420.00 USD | 0.00 USD | 339.12 USD | `-8.27%` | `527,000,000.00` |
| `Live` | `Long` | `645.50` | 454,080.00 USD | 0.00 USD | 307.26 USD | `-7.99%` | `476,000,000.00` |
| `Live` | `Long` | `646.50` | 453,780.00 USD | 0.00 USD | 155.81 USD | `-7.85%` | `241,000,000.00` |
| `Live` | `Long` | `648.50` | 453,620.00 USD | 0.00 USD | 1,940.00 USD | `-7.56%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 451,680.00 USD | 0.00 USD | 1,620.00 USD | `-7.42%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 450,060.00 USD | 0.00 USD | 457.30 USD | `-7.28%` | `703,000,000.00` |
| `Live` | `Long` | `651.50` | 449,600.00 USD | 0.00 USD | 9,650.00 USD | `-7.13%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 439,950.00 USD | 0.00 USD | 652.50 USD | `-6.99%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 439,300.00 USD | 0.00 USD | 98,240.00 USD | `-6.85%` | `150,322,000,000.00` |
| `Live` | `Long` | `654.50` | 341,070.00 USD | 0.00 USD | 100.14 USD | `-6.71%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 340,970.00 USD | 0.00 USD | 122.58 USD | `-6.56%` | `187,000,000.00` |
| `Live` | `Long` | `656.50` | 340,840.00 USD | 0.00 USD | 24,500.00 USD | `-6.42%` | `37,326,000,000.00` |
| `Live` | `Long` | `657.50` | 316,340.00 USD | 0.00 USD | 338.61 USD | `-6.28%` | `515,000,000.00` |
| `Live` | `Long` | `658.50` | 316,000.00 USD | 0.00 USD | 15,090.00 USD | `-6.14%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 300,910.00 USD | 0.00 USD | 45,510.00 USD | `-5.99%` | `69,000,000,000.00` |
| `Live` | `Long` | `660.50` | 255,410.00 USD | 0.00 USD | 3,410.00 USD | `-5.85%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 251,990.00 USD | 0.00 USD | 20,140.00 USD | `-5.71%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 231,850.00 USD | 0.00 USD | 2,850.00 USD | `-5.57%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 229,000.00 USD | 0.00 USD | 31,360.00 USD | `-5.42%` | `47,258,000,000.00` |
| `Live` | `Long` | `664.50` | 197,650.00 USD | 0.00 USD | 747.56 USD | `-5.28%` | `1,125,000,000.00` |
| `Live` | `Long` | `665.50` | 196,900.00 USD | 0.00 USD | 1,610.00 USD | `-5.14%` | `2,419,000,000.00` |
| `Live` | `Long` | `666.50` | 195,290.00 USD | 0.00 USD | 2,140.00 USD | `-5.00%` | `3,212,000,000.00` |
| `Live` | `Long` | `667.50` | 193,150.00 USD | 0.00 USD | 1,830.00 USD | `-4.85%` | `2,749,000,000.00` |
| `Live` | `Long` | `668.50` | 191,310.00 USD | 0.00 USD | 13,450.00 USD | `-4.71%` | `20,115,000,000.00` |
| `Live` | `Long` | `669.50` | 177,870.00 USD | 0.00 USD | 824.15 USD | `-4.57%` | `1,231,000,000.00` |
| `Live` | `Long` | `670.50` | 177,040.00 USD | 0.00 USD | 4,750.00 USD | `-4.43%` | `7,086,000,000.00` |
| `Live` | `Long` | `671.50` | 172,290.00 USD | 0.00 USD | 17,940.00 USD | `-4.28%` | `26,720,000,000.00` |
| `Live` | `Long` | `672.50` | 154,350.00 USD | 0.00 USD | 7,860.00 USD | `-4.14%` | `11,685,000,000.00` |
| `Live` | `Long` | `673.50` | 146,490.00 USD | 0.00 USD | 39,130.00 USD | `-4.00%` | `58,100,000,000.00` |
| `Live` | `Long` | `674.50` | 107,360.00 USD | 0.00 USD | 4,100.00 USD | `-3.86%` | `6,078,000,000.00` |
| `Live` | `Long` | `675.50` | 103,260.00 USD | 0.00 USD | 74,720.00 USD | `-3.71%` | `110,607,000,000.00` |
| `Live` | `Long` | `676.50` | 28,550.00 USD | 0.00 USD | 1,960.00 USD | `-3.57%` | `2,901,000,000.00` |
| `Live` | `Long` | `677.50` | 26,580.00 USD | 0.00 USD | 250.67 USD | `-3.43%` | `370,000,000.00` |
| `Live` | `Long` | `678.50` | 26,330.00 USD | 0.00 USD | 2,520.00 USD | `-3.29%` | `3,716,000,000.00` |
| `Live` | `Long` | `679.50` | 23,810.00 USD | 0.00 USD | 998.19 USD | `-3.14%` | `1,469,000,000.00` |
| `Live` | `Long` | `680.50` | 22,810.00 USD | 0.00 USD | 21,870.00 USD | `-3.00%` | `32,144,000,000.00` |
| `Live` | `Long` | `681.50` | 939.79 USD | 0.00 USD | 939.79 USD | `-2.86%` | `1,379,000,000.00` |
| `Live` | `Short` | `720.50` | 376.82 USD | 376.82 USD | 0.00 USD | `+2.70%` | `523,000,000.00` |
| `Live` | `Short` | `721.50` | 33,420.00 USD | 33,040.00 USD | 0.00 USD | `+2.84%` | `45,800,000,000.00` |
| `Live` | `Short` | `722.50` | 35,370.00 USD | 1,950.00 USD | 0.00 USD | `+2.99%` | `2,702,000,000.00` |
| `Live` | `Short` | `723.50` | 37,540.00 USD | 2,170.00 USD | 0.00 USD | `+3.13%` | `2,996,000,000.00` |
| `Live` | `Short` | `724.50` | 38,070.00 USD | 525.26 USD | 0.00 USD | `+3.27%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 39,600.00 USD | 1,530.00 USD | 0.00 USD | `+3.41%` | `2,108,000,000.00` |
| `Live` | `Short` | `726.50` | 43,300.00 USD | 3,710.00 USD | 0.00 USD | `+3.56%` | `5,105,000,000.00` |
| `Live` | `Short` | `727.50` | 43,650.00 USD | 342.65 USD | 0.00 USD | `+3.70%` | `471,000,000.00` |
| `Live` | `Short` | `728.50` | 84,720.00 USD | 41,080.00 USD | 0.00 USD | `+3.84%` | `56,385,000,000.00` |
| `Live` | `Short` | `729.50` | 255,740.00 USD | 171,010.00 USD | 0.00 USD | `+3.98%` | `234,425,000,000.00` |
| `Live` | `Short` | `730.50` | 284,230.00 USD | 28,500.00 USD | 0.00 USD | `+4.13%` | `39,009,000,000.00` |
| `Live` | `Short` | `731.50` | 286,280.00 USD | 2,050.00 USD | 0.00 USD | `+4.27%` | `2,797,000,000.00` |
| `Live` | `Short` | `732.50` | 426,580.00 USD | 140,300.00 USD | 0.00 USD | `+4.41%` | `191,538,000,000.00` |
| `Live` | `Short` | `733.50` | 438,850.00 USD | 12,260.00 USD | 0.00 USD | `+4.55%` | `16,721,000,000.00` |
| `Live` | `Short` | `734.50` | 591,530.00 USD | 152,680.00 USD | 0.00 USD | `+4.70%` | `207,869,000,000.00` |
| `Live` | `Short` | `735.50` | 617,940.00 USD | 26,410.00 USD | 0.00 USD | `+4.84%` | `35,913,000,000.00` |
| `Live` | `Short` | `736.50` | 638,020.00 USD | 20,080.00 USD | 0.00 USD | `+4.98%` | `27,260,000,000.00` |
| `Live` | `Short` | `737.50` | 646,690.00 USD | 8,670.00 USD | 0.00 USD | `+5.12%` | `11,762,000,000.00` |
| `Live` | `Short` | `738.50` | 705,900.00 USD | 59,210.00 USD | 0.00 USD | `+5.27%` | `80,176,000,000.00` |
| `Live` | `Short` | `739.50` | 835,050.00 USD | 129,150.00 USD | 0.00 USD | `+5.41%` | `174,646,000,000.00` |
| `Live` | `Short` | `740.50` | 841,810.00 USD | 6,760.00 USD | 0.00 USD | `+5.55%` | `9,131,000,000.00` |
| `Live` | `Short` | `741.50` | 873,880.00 USD | 32,060.00 USD | 0.00 USD | `+5.69%` | `43,243,000,000.00` |
| `Live` | `Short` | `742.50` | 941,170.00 USD | 67,300.00 USD | 0.00 USD | `+5.84%` | `90,634,000,000.00` |
| `Live` | `Short` | `743.50` | 988,400.00 USD | 47,230.00 USD | 0.00 USD | `+5.98%` | `63,520,000,000.00` |
| `Live` | `Short` | `744.50` | 1,110,000.00 USD | 117,700.00 USD | 0.00 USD | `+6.12%` | `158,091,000,000.00` |
| `Live` | `Short` | `745.50` | 1,130,000.00 USD | 26,890.00 USD | 0.00 USD | `+6.26%` | `36,068,000,000.00` |
| `Live` | `Short` | `746.50` | 1,320,000.00 USD | 185,960.00 USD | 0.00 USD | `+6.41%` | `249,111,000,000.00` |
| `Live` | `Short` | `747.50` | 1,320,000.00 USD | 2,010.00 USD | 0.00 USD | `+6.55%` | `2,691,000,000.00` |
| `Live` | `Short` | `748.50` | 1,330,000.00 USD | 4,270.00 USD | 0.00 USD | `+6.69%` | `5,702,000,000.00` |
| `Live` | `Short` | `749.50` | 1,390,000.00 USD | 67,670.00 USD | 0.00 USD | `+6.83%` | `90,291,000,000.00` |
| `Live` | `Short` | `750.50` | 1,970,000.00 USD | 575,140.00 USD | 0.00 USD | `+6.98%` | `766,346,000,000.00` |
| `Live` | `Short` | `751.50` | 1,990,000.00 USD | 21,390.00 USD | 0.00 USD | `+7.12%` | `28,467,000,000.00` |
| `Live` | `Short` | `752.50` | 2,040,000.00 USD | 48,630.00 USD | 0.00 USD | `+7.26%` | `64,624,000,000.00` |
| `Live` | `Short` | `754.50` | 2,900,000.00 USD | 863,580.00 USD | 0.00 USD | `+7.55%` | `1,144,577,000,000.00` |
| `Live` | `Short` | `755.50` | 2,910,000.00 USD | 3,890.00 USD | 0.00 USD | `+7.69%` | `5,151,000,000.00` |
| `Live` | `Short` | `757.50` | 2,910,000.00 USD | 2,010.00 USD | 0.00 USD | `+7.98%` | `2,652,000,000.00` |
| `Live` | `Short` | `758.50` | 3,090,000.00 USD | 180,980.00 USD | 0.00 USD | `+8.12%` | `238,608,000,000.00` |
| `Live` | `Short` | `759.50` | 3,100,000.00 USD | 8,560.00 USD | 0.00 USD | `+8.26%` | `11,277,000,000.00` |
| `Live` | `Short` | `760.50` | 3,100,000.00 USD | 6,020.00 USD | 0.00 USD | `+8.40%` | `7,921,000,000.00` |
| `Live` | `Short` | `761.50` | 3,100,000.00 USD | 367.04 USD | 0.00 USD | `+8.55%` | `482,000,000.00` |
| `Live` | `Short` | `762.50` | 3,110,000.00 USD | 8,050.00 USD | 0.00 USD | `+8.69%` | `10,551,000,000.00` |
| `Live` | `Short` | `763.50` | 3,710,000.00 USD | 595,810.00 USD | 0.00 USD | `+8.83%` | `780,361,000,000.00` |
| `Live` | `Short` | `765.50` | 3,710,000.00 USD | 785.40 USD | 0.00 USD | `+9.12%` | `1,026,000,000.00` |
| `Live` | `Short` | `766.50` | 3,710,000.00 USD | 2,850.00 USD | 0.00 USD | `+9.26%` | `3,719,000,000.00` |
| `Live` | `Short` | `767.50` | 3,710,000.00 USD | 2,450.00 USD | 0.00 USD | `+9.40%` | `3,190,000,000.00` |
| `Live` | `Short` | `768.50` | 3,710,000.00 USD | 300.48 USD | 0.00 USD | `+9.54%` | `391,000,000.00` |
| `Live` | `Short` | `770.50` | 3,710,000.00 USD | 661.86 USD | 0.00 USD | `+9.83%` | `859,000,000.00` |
| `Live` | `Short` | `771.50` | 4,110,000.00 USD | 395,010.00 USD | 0.00 USD | `+9.97%` | `512,000,000,000.00` |
| `Live` | `Short` | `772.50` | 4,110,000.00 USD | 2,450.00 USD | 0.00 USD | `+10.11%` | `3,173,000,000.00` |
| `Live` | `Short` | `773.50` | 4,110,000.00 USD | 2,200.00 USD | 0.00 USD | `+10.26%` | `2,842,000,000.00` |
| `Live` | `Short` | `775.50` | 4,110,000.00 USD | 544.40 USD | 0.00 USD | `+10.54%` | `702,000,000.00` |
| `Live` | `Short` | `776.50` | 4,200,000.00 USD | 89,520.00 USD | 0.00 USD | `+10.68%` | `115,281,000,000.00` |
| `Live` | `Short` | `777.50` | 4,200,000.00 USD | 209.15 USD | 0.00 USD | `+10.83%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 4,210,000.00 USD | 8,100.00 USD | 0.00 USD | `+10.97%` | `10,401,000,000.00` |
| `Live` | `Short` | `780.50` | 4,220,000.00 USD | 4,150.00 USD | 0.00 USD | `+11.25%` | `5,318,000,000.00` |
| `Live` | `Short` | `781.50` | 4,220,000.00 USD | 1,830.00 USD | 0.00 USD | `+11.40%` | `2,337,000,000.00` |
| `Live` | `Short` | `784.50` | 4,220,000.00 USD | 743.71 USD | 0.00 USD | `+11.82%` | `948,000,000.00` |
| `Live` | `Short` | `785.50` | 4,220,000.00 USD | 1,750.00 USD | 0.00 USD | `+11.97%` | `2,227,000,000.00` |
| `Live` | `Short` | `786.50` | 4,230,000.00 USD | 4,780.00 USD | 0.00 USD | `+12.11%` | `6,080,000,000.00` |
| `Live` | `Short` | `787.50` | 4,230,000.00 USD | 7,880.00 USD | 0.00 USD | `+12.25%` | `10,000,000,000.00` |
| `Live` | `Short` | `788.50` | 4,240,000.00 USD | 1,580.00 USD | 0.00 USD | `+12.39%` | `2,000,000,000.00` |
| `Live` | `Short` | `789.50` | 4,240,000.00 USD | 798.18 USD | 0.00 USD | `+12.54%` | `1,011,000,000.00` |
| `Live` | `Short` | `790.50` | 4,240,000.00 USD | 1,230.00 USD | 0.00 USD | `+12.68%` | `1,551,000,000.00` |
| `Live` | `Short` | `793.50` | 4,240,000.00 USD | 1,280.00 USD | 0.00 USD | `+13.11%` | `1,616,000,000.00` |
| `Live` | `Short` | `795.50` | 4,330,000.00 USD | 96,410.00 USD | 0.00 USD | `+13.39%` | `121,200,000,000.00` |
| `Live` | `Short` | `796.50` | 4,340,000.00 USD | 567.11 USD | 0.00 USD | `+13.53%` | `712,000,000.00` |
| `Live` | `Short` | `797.50` | 4,340,000.00 USD | 1,760.00 USD | 0.00 USD | `+13.68%` | `2,208,000,000.00` |
| `Live` | `Short` | `799.50` | 4,340,000.00 USD | 5,310.00 USD | 0.00 USD | `+13.96%` | `6,642,000,000.00` |
| `Live` | `Short` | `800.50` | 4,370,000.00 USD | 28,250.00 USD | 0.00 USD | `+14.10%` | `35,287,000,000.00` |
| `Live` | `Short` | `801.50` | 4,370,000.00 USD | 3,410.00 USD | 0.00 USD | `+14.25%` | `4,250,000,000.00` |
| `Live` | `Short` | `802.50` | 5,150,000.00 USD | 779,990.00 USD | 0.00 USD | `+14.39%` | `971,951,000,000.00` |
| `Live` | `Short` | `803.50` | 5,160,000.00 USD | 5,930.00 USD | 0.00 USD | `+14.53%` | `7,379,000,000.00` |
| `Live` | `Short` | `805.50` | 5,180,000.00 USD | 15,600.00 USD | 0.00 USD | `+14.82%` | `19,368,000,000.00` |
| `Live` | `Short` | `806.50` | 5,180,000.00 USD | 2,890.00 USD | 0.00 USD | `+14.96%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 5,180,000.00 USD | 738.06 USD | 0.00 USD | `+15.10%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 5,190,000.00 USD | 11,780.00 USD | 0.00 USD | `+15.24%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 5,190,000.00 USD | 574.75 USD | 0.00 USD | `+15.39%` | `710,000,000.00` |
| `Live` | `Short` | `811.50` | 5,190,000.00 USD | 434.15 USD | 0.00 USD | `+15.67%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 5,190,000.00 USD | 692.32 USD | 0.00 USD | `+16.10%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 5,200,000.00 USD | 8,150.00 USD | 0.00 USD | `+16.24%` | `9,992,000,000.00` |
| `Live` | `Short` | `816.50` | 5,220,000.00 USD | 15,410.00 USD | 0.00 USD | `+16.39%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 5,220,000.00 USD | 325.37 USD | 0.00 USD | `+16.53%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 5,220,000.00 USD | 7,720.00 USD | 0.00 USD | `+16.67%` | `9,432,000,000.00` |
| `Live` | `Short` | `821.50` | 5,240,000.00 USD | 11,710.00 USD | 0.00 USD | `+17.10%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 5,240,000.00 USD | 3,540.00 USD | 0.00 USD | `+17.24%` | `4,302,000,000.00` |
| `Live` | `Short` | `826.50` | 5,780,000.00 USD | 536,790.00 USD | 0.00 USD | `+17.81%` | `649,473,000,000.00` |
| `Live` | `Short` | `827.50` | 5,860,000.00 USD | 81,670.00 USD | 0.00 USD | `+17.95%` | `98,695,000,000.00` |
| `Live` | `Short` | `828.50` | 5,860,000.00 USD | 5,880.00 USD | 0.00 USD | `+18.10%` | `7,102,000,000.00` |
| `Live` | `Short` | `829.50` | 5,870,000.00 USD | 2,900.00 USD | 0.00 USD | `+18.24%` | `3,500,000,000.00` |
| `Live` | `Short` | `834.50` | 5,870,000.00 USD | 1,010.00 USD | 0.00 USD | `+18.95%` | `1,206,000,000.00` |
| `Live` | `Short` | `836.50` | 5,870,000.00 USD | 239.24 USD | 0.00 USD | `+19.24%` | `286,000,000.00` |
| `Live` | `Short` | `837.50` | 5,870,000.00 USD | 3,570.00 USD | 0.00 USD | `+19.38%` | `4,257,000,000.00` |
| `Live` | `Short` | `838.50` | 5,900,000.00 USD | 32,510.00 USD | 0.00 USD | `+19.52%` | `38,769,000,000.00` |
| `Live` | `Short` | `840.50` | 5,900,000.00 USD | 679.96 USD | 0.00 USD | `+19.81%` | `809,000,000.00` |
| `Live` | `Short` | `841.50` | 5,910,000.00 USD | 4,410.00 USD | 0.00 USD | `+19.95%` | `5,235,000,000.00` |
| `Live` | `Short` | `842.50` | 5,910,000.00 USD | 171.03 USD | 0.00 USD | `+20.09%` | `203,000,000.00` |
| `Live` | `Short` | `843.50` | 5,940,000.00 USD | 34,060.00 USD | 0.00 USD | `+20.23%` | `40,378,000,000.00` |
| `Live` | `Short` | `846.50` | 5,940,000.00 USD | 1,160.00 USD | 0.00 USD | `+20.66%` | `1,371,000,000.00` |
| `Live` | `Short` | `847.50` | 5,940,000.00 USD | 289.00 USD | 0.00 USD | `+20.80%` | `341,000,000.00` |
| `Live` | `Short` | `850.50` | 5,950,000.00 USD | 393.78 USD | 0.00 USD | `+21.23%` | `463,000,000.00` |
| `Live` | `Short` | `855.50` | 5,950,000.00 USD | 2,110.00 USD | 0.00 USD | `+21.94%` | `2,462,000,000.00` |
| `Live` | `Short` | `856.50` | 5,980,000.00 USD | 29,740.00 USD | 0.00 USD | `+22.09%` | `34,722,000,000.00` |
| `Live` | `Short` | `857.50` | 5,980,000.00 USD | 5,050.00 USD | 0.00 USD | `+22.23%` | `5,884,000,000.00` |
| `Live` | `Short` | `858.50` | 6,510,000.00 USD | 523,680.00 USD | 0.00 USD | `+22.37%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 6,520,000.00 USD | 16,380.00 USD | 0.00 USD | `+22.51%` | `19,059,000,000.00` |
| `Live` | `Short` | `862.50` | 6,520,000.00 USD | 1,480.00 USD | 0.00 USD | `+22.94%` | `1,721,000,000.00` |
| `Live` | `Short` | `864.50` | 6,810,000.00 USD | 289,650.00 USD | 0.00 USD | `+23.23%` | `335,051,000,000.00` |
| `Live` | `Short` | `865.50` | 6,830,000.00 USD | 18,900.00 USD | 0.00 USD | `+23.37%` | `21,832,000,000.00` |
| `Live` | `Short` | `873.50` | 6,830,000.00 USD | 326.69 USD | 0.00 USD | `+24.51%` | `374,000,000.00` |
| `Live` | `Short` | `875.50` | 6,850,000.00 USD | 14,000.00 USD | 0.00 USD | `+24.80%` | `15,992,000,000.00` |
| `Live` | `Short` | `877.50` | 7,550,000.00 USD | 702,210.00 USD | 0.00 USD | `+25.08%` | `800,238,000,000.00` |
| `Live` | `Short` | `878.50` | 7,550,000.00 USD | 4,540.00 USD | 0.00 USD | `+25.22%` | `5,165,000,000.00` |
| `Live` | `Short` | `880.50` | 7,550,000.00 USD | 663.02 USD | 0.00 USD | `+25.51%` | `753,000,000.00` |
| `Live` | `Short` | `885.50` | 7,560,000.00 USD | 2,580.00 USD | 0.00 USD | `+26.22%` | `2,917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,560,000.00 USD | 385.18 USD | 0.00 USD | `+26.51%` | `434,000,000.00` |
| `Live` | `Short` | `891.50` | 7,560,000.00 USD | 3,950.00 USD | 0.00 USD | `+27.08%` | `4,429,000,000.00` |
| `Live` | `Short` | `893.50` | 7,560,000.00 USD | 173.34 USD | 0.00 USD | `+27.36%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,590,000.00 USD | 26,840.00 USD | 0.00 USD | `+27.50%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 7,840,000.00 USD | 254,270.00 USD | 0.00 USD | `+27.65%` | `283,946,000,000.00` |
| `Live` | `Short` | `896.50` | 7,840,000.00 USD | 249.23 USD | 0.00 USD | `+27.79%` | `278,000,000.00` |
| `Live` | `Short` | `897.50` | 7,970,000.00 USD | 126,180.00 USD | 0.00 USD | `+27.93%` | `140,590,000,000.00` |
| `Live` | `Short` | `898.50` | 7,970,000.00 USD | 127.59 USD | 0.00 USD | `+28.07%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 7,970,000.00 USD | 5,400.00 USD | 0.00 USD | `+28.22%` | `6,000,000,000.00` |
| `Live` | `Short` | `902.50` | 8,060,000.00 USD | 90,560.00 USD | 0.00 USD | `+28.64%` | `100,338,000,000.00` |
| `Live` | `Short` | `903.50` | 8,070,000.00 USD | 5,470.00 USD | 0.00 USD | `+28.79%` | `6,050,000,000.00` |
| `Live` | `Short` | `904.50` | 8,170,000.00 USD | 100,930.00 USD | 0.00 USD | `+28.93%` | `111,587,000,000.00` |
| `Live` | `Short` | `905.50` | 8,170,000.00 USD | 107.75 USD | 0.00 USD | `+29.07%` | `119,000,000.00` |
| `Live` | `Short` | `906.50` | 8,440,000.00 USD | 268,530.00 USD | 0.00 USD | `+29.21%` | `296,225,000,000.00` |
| `Live` | `Short` | `908.50` | 8,440,000.00 USD | 2,420.00 USD | 0.00 USD | `+29.50%` | `2,669,000,000.00` |
| `Live` | `Short` | `909.50` | 8,470,000.00 USD | 29,900.00 USD | 0.00 USD | `+29.64%` | `32,872,000,000.00` |
| `Live` | `Short` | `911.50` | 8,510,000.00 USD | 34,790.00 USD | 0.00 USD | `+29.93%` | `38,169,000,000.00` |
| `Live` | `Short` | `912.50` | 8,510,000.00 USD | 116.80 USD | 0.00 USD | `+30.07%` | `128,000,000.00` |
| `Live` | `Short` | `913.50` | 8,520,000.00 USD | 13,930.00 USD | 0.00 USD | `+30.21%` | `15,247,000,000.00` |
| `Live` | `Short` | `915.50` | 8,520,000.00 USD | 390.00 USD | 0.00 USD | `+30.50%` | `426,000,000.00` |
| `Live` | `Short` | `918.50` | 8,520,000.00 USD | 206.66 USD | 0.00 USD | `+30.92%` | `225,000,000.00` |
| `Live` | `Short` | `925.50` | 8,530,000.00 USD | 9,830.00 USD | 0.00 USD | `+31.92%` | `10,619,000,000.00` |
| `Live` | `Short` | `927.50` | 8,530,000.00 USD | 651.10 USD | 0.00 USD | `+32.21%` | `702,000,000.00` |
| `Live` | `Short` | `934.50` | 8,530,000.00 USD | 956.93 USD | 0.00 USD | `+33.21%` | `1,024,000,000.00` |
| `Live` | `Short` | `935.50` | 8,540,000.00 USD | 3,810.00 USD | 0.00 USD | `+33.35%` | `4,068,000,000.00` |
| `Live` | `Short` | `936.50` | 8,660,000.00 USD | 121,750.00 USD | 0.00 USD | `+33.49%` | `130,000,000,000.00` |
| `Live` | `Short` | `942.50` | 8,660,000.00 USD | 963.24 USD | 0.00 USD | `+34.35%` | `1,022,000,000.00` |
| `Live` | `Short` | `948.50` | 8,730,000.00 USD | 66,390.00 USD | 0.00 USD | `+35.20%` | `70,000,000,000.00` |
| `Live` | `Short` | `951.50` | 8,730,000.00 USD | 676.52 USD | 0.00 USD | `+35.63%` | `711,000,000.00` |
| `Live` | `Short` | `954.50` | 8,750,000.00 USD | 19,120.00 USD | 0.00 USD | `+36.06%` | `20,031,000,000.00` |
| `Live` | `Short` | `957.50` | 8,760,000.00 USD | 9,620.00 USD | 0.00 USD | `+36.48%` | `10,045,000,000.00` |
| `Live` | `Short` | `958.50` | 8,760,000.00 USD | 114.06 USD | 0.00 USD | `+36.63%` | `119,000,000.00` |
| `Live` | `Short` | `960.50` | 8,760,000.00 USD | 204.59 USD | 0.00 USD | `+36.91%` | `213,000,000.00` |
| `Live` | `Short` | `969.50` | 8,760,000.00 USD | 5,780.00 USD | 0.00 USD | `+38.19%` | `5,960,000,000.00` |
| `Live` | `Short` | `970.50` | 8,780,000.00 USD | 14,110.00 USD | 0.00 USD | `+38.34%` | `14,541,000,000.00` |
| `Live` | `Short` | `972.50` | 8,780,000.00 USD | 1,950.00 USD | 0.00 USD | `+38.62%` | `2,000,000,000.00` |
| `Live` | `Short` | `978.50` | 8,840,000.00 USD | 63,360.00 USD | 0.00 USD | `+39.48%` | `64,750,000,000.00` |
| `Live` | `Short` | `981.50` | 8,860,000.00 USD | 14,480.00 USD | 0.00 USD | `+39.90%` | `14,758,000,000.00` |
| `Live` | `Short` | `985.50` | 8,860,000.00 USD | 1,280.00 USD | 0.00 USD | `+40.47%` | `1,297,000,000.00` |
| `Live` | `Short` | `986.50` | 8,860,000.00 USD | 612.62 USD | 0.00 USD | `+40.62%` | `621,000,000.00` |
| `Live` | `Short` | `990.50` | 8,890,000.00 USD | 28,300.00 USD | 0.00 USD | `+41.19%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 8,890,000.00 USD | 2,140.00 USD | 0.00 USD | `+41.47%` | `2,154,000,000.00` |
| `Live` | `Short` | `993.50` | 8,890,000.00 USD | 975.62 USD | 0.00 USD | `+41.61%` | `982,000,000.00` |
| `Live` | `Short` | `994.50` | 9,170,000.00 USD | 285,520.00 USD | 0.00 USD | `+41.76%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 9,170,000.00 USD | 313.58 USD | 0.00 USD | `+41.90%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 9,180,000.00 USD | 989.52 USD | 0.00 USD | `+42.04%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 9,180,000.00 USD | 7,300.00 USD | 0.00 USD | `+42.19%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 9,520,000.00 USD | 337,490.00 USD | 0.00 USD | `+42.33%` | `338,002,000,000.00` |
| `Live` | `Short` | `999.50` | 9,620,000.00 USD | 99,950.00 USD | 0.00 USD | `+42.47%` | `99,998,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,650,000.00 USD | 34,290.00 USD | 0.00 USD | `+43.04%` | `34,169,000,000.00` |
| `Live` | `Short` | `1005.50` | 9,660,000.00 USD | 4,050.00 USD | 0.00 USD | `+43.33%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 9,690,000.00 USD | 29,110.00 USD | 0.00 USD | `+43.75%` | `28,860,000,000.00` |
| `Live` | `Short` | `1009.50` | 9,740,000.00 USD | 51,370.00 USD | 0.00 USD | `+43.90%` | `50,889,000,000.00` |
| `Live` | `Short` | `1012.50` | 9,750,000.00 USD | 13,440.00 USD | 0.00 USD | `+44.32%` | `13,273,000,000.00` |
| `Live` | `Short` | `1014.50` | 10,510,000.00 USD | 760,880.00 USD | 0.00 USD | `+44.61%` | `750,000,000,000.00` |
| `Live` | `Short` | `1016.50` | 10,530,000.00 USD | 14,880.00 USD | 0.00 USD | `+44.89%` | `14,636,000,000.00` |
| `Live` | `Short` | `1024.50` | 10,530,000.00 USD | 2,850.00 USD | 0.00 USD | `+46.03%` | `2,777,000,000.00` |
| `Live` | `Short` | `1032.50` | 11,250,000.00 USD | 720,280.00 USD | 0.00 USD | `+47.17%` | `697,611,000,000.00` |
| `Live` | `Short` | `1038.50` | 11,250,000.00 USD | 500.56 USD | 0.00 USD | `+48.03%` | `482,000,000.00` |
| `Live` | `Short` | `1040.50` | 11,320,000.00 USD | 65,030.00 USD | 0.00 USD | `+48.31%` | `62,500,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,320,000.00 USD | 500.04 USD | 0.00 USD | `+49.74%` | `476,000,000.00` |
| `Live` | `Short` | `1057.50` | 11,320,000.00 USD | 7,000.00 USD | 0.00 USD | `+50.74%` | `6,620,000,000.00` |
| `Live` | `Short` | `1062.50` | 11,320,000.00 USD | 635.38 USD | 0.00 USD | `+51.45%` | `598,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,330,000.00 USD | 1,760.00 USD | 0.00 USD | `+51.74%` | `1,657,000,000.00` |
| `Live` | `Short` | `1069.50` | 11,330,000.00 USD | 119.78 USD | 0.00 USD | `+52.45%` | `112,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,330,000.00 USD | 1,610.00 USD | 0.00 USD | `+53.02%` | `1,500,000,000.00` |
| `Live` | `Short` | `1075.50` | 11,400,000.00 USD | 68,740.00 USD | 0.00 USD | `+53.30%` | `63,916,000,000.00` |
| `Live` | `Short` | `1077.50` | 11,400,000.00 USD | 1,560.00 USD | 0.00 USD | `+53.59%` | `1,445,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,400,000.00 USD | 5,770.00 USD | 0.00 USD | `+55.01%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,420,000.00 USD | 15,780.00 USD | 0.00 USD | `+55.16%` | `14,495,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,540,000.00 USD | 120,790.00 USD | 0.00 USD | `+55.87%` | `110,460,000,000.00` |
| `Live` | `Short` | `1096.50` | 11,540,000.00 USD | 810.31 USD | 0.00 USD | `+56.30%` | `739,000,000.00` |
| `Live` | `Short` | `1103.50` | 11,540,000.00 USD | 461.26 USD | 0.00 USD | `+57.29%` | `418,000,000.00` |
| `Live` | `Short` | `1109.50` | 11,540,000.00 USD | 237.43 USD | 0.00 USD | `+58.15%` | `214,000,000.00` |
| `Live` | `Short` | `1111.50` | 11,720,000.00 USD | 177,260.00 USD | 0.00 USD | `+58.43%` | `159,478,000,000.00` |
| `Live` | `Short` | `1120.50` | 11,800,000.00 USD | 76,470.00 USD | 0.00 USD | `+59.72%` | `68,249,000,000.00` |
| `Live` | `Short` | `1123.50` | 11,800,000.00 USD | 352.78 USD | 0.00 USD | `+60.15%` | `314,000,000.00` |
| `Live` | `Short` | `1126.50` | 11,820,000.00 USD | 20,080.00 USD | 0.00 USD | `+60.57%` | `17,826,000,000.00` |
| `Live` | `Short` | `1136.50` | 11,820,000.00 USD | 152.29 USD | 0.00 USD | `+62.00%` | `134,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,170,000.00 USD | 349,310.00 USD | 0.00 USD | `+62.14%` | `307,082,000,000.00` |
| `Live` | `Short` | `1145.50` | 12,170,000.00 USD | 1,530.00 USD | 0.00 USD | `+63.28%` | `1,337,000,000.00` |
| `Live` | `Short` | `1157.50` | 12,180,000.00 USD | 11,750.00 USD | 0.00 USD | `+64.99%` | `10,154,000,000.00` |
| `Live` | `Short` | `1166.50` | 12,200,000.00 USD | 20,250.00 USD | 0.00 USD | `+66.27%` | `17,363,000,000.00` |
| `Live` | `Short` | `1168.50` | 12,200,000.00 USD | 156.58 USD | 0.00 USD | `+66.56%` | `134,000,000.00` |
| `Live` | `Short` | `1175.50` | 12,200,000.00 USD | 122.25 USD | 0.00 USD | `+67.56%` | `104,000,000.00` |
| `Live` | `Short` | `1180.50` | 12,210,000.00 USD | 5,060.00 USD | 0.00 USD | `+68.27%` | `4,284,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,210,000.00 USD | 463.43 USD | 0.00 USD | `+70.69%` | `387,000,000.00` |
| `Live` | `Short` | `1199.50` | 12,210,000.00 USD | 169.13 USD | 0.00 USD | `+70.98%` | `141,000,000.00` |
| `Live` | `Short` | `1202.50` | 12,320,000.00 USD | 118,760.00 USD | 0.00 USD | `+71.41%` | `98,764,000,000.00` |
| `Live` | `Short` | `1203.50` | 12,330,000.00 USD | 2,370.00 USD | 0.00 USD | `+71.55%` | `1,971,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,330,000.00 USD | 385.19 USD | 0.00 USD | `+72.12%` | `319,000,000.00` |
| `Live` | `Short` | `1219.50` | 12,400,000.00 USD | 73,150.00 USD | 0.00 USD | `+73.83%` | `59,982,000,000.00` |
| `Live` | `Short` | `1224.50` | 12,400,000.00 USD | 1,400.00 USD | 0.00 USD | `+74.54%` | `1,144,000,000.00` |
| `Live` | `Short` | `1228.50` | 12,460,000.00 USD | 63,080.00 USD | 0.00 USD | `+75.11%` | `51,346,000,000.00` |
| `Live` | `Short` | `1244.50` | 12,470,000.00 USD | 2,660.00 USD | 0.00 USD | `+77.39%` | `2,134,000,000.00` |
| `Live` | `Short` | `1249.50` | 12,470,000.00 USD | 2,050.00 USD | 0.00 USD | `+78.11%` | `1,644,000,000.00` |
| `Live` | `Short` | `1251.50` | 12,470,000.00 USD | 1,650.00 USD | 0.00 USD | `+78.39%` | `1,318,000,000.00` |
| `Live` | `Short` | `1256.50` | 12,480,000.00 USD | 5,020.00 USD | 0.00 USD | `+79.10%` | `3,994,000,000.00` |
| `Live` | `Short` | `1257.50` | 12,480,000.00 USD | 201.20 USD | 0.00 USD | `+79.25%` | `160,000,000.00` |
| `Live` | `Short` | `1258.50` | 12,590,000.00 USD | 113,270.00 USD | 0.00 USD | `+79.39%` | `90,000,000,000.00` |
| `Live` | `Short` | `1260.50` | 12,590,000.00 USD | 1,260.00 USD | 0.00 USD | `+79.67%` | `1,000,000,000.00` |
| `Live` | `Short` | `1264.50` | 12,600,000.00 USD | 6,850.00 USD | 0.00 USD | `+80.24%` | `5,419,000,000.00` |
| `Live` | `Short` | `1266.50` | 12,620,000.00 USD | 25,330.00 USD | 0.00 USD | `+80.53%` | `20,000,000,000.00` |
| `Live` | `Short` | `1268.50` | 12,650,000.00 USD | 24,630.00 USD | 0.00 USD | `+80.81%` | `19,414,000,000.00` |
| `Live` | `Short` | `1271.50` | 12,670,000.00 USD | 18,990.00 USD | 0.00 USD | `+81.24%` | `14,939,000,000.00` |
| `Live` | `Short` | `1276.50` | 12,780,000.00 USD | 108,890.00 USD | 0.00 USD | `+81.95%` | `85,305,000,000.00` |
| `Live` | `Short` | `1279.50` | 13,390,000.00 USD | 617,840.00 USD | 0.00 USD | `+82.38%` | `482,880,000,000.00` |
| `Live` | `Short` | `1283.50` | 13,400,000.00 USD | 1,810.00 USD | 0.00 USD | `+82.95%` | `1,409,000,000.00` |
| `Live` | `Short` | `1284.50` | 13,410,000.00 USD | 18,070.00 USD | 0.00 USD | `+83.09%` | `14,070,000,000.00` |
| `Live` | `Short` | `1287.50` | 13,480,000.00 USD | 61,960.00 USD | 0.00 USD | `+83.52%` | `48,123,000,000.00` |
| `Live` | `Short` | `1290.50` | 13,480,000.00 USD | 349.73 USD | 0.00 USD | `+83.95%` | `271,000,000.00` |
| `Live` | `Short` | `1295.50` | 13,480,000.00 USD | 181.37 USD | 0.00 USD | `+84.66%` | `140,000,000.00` |
| `Live` | `Short` | `1297.50` | 13,480,000.00 USD | 224.47 USD | 0.00 USD | `+84.95%` | `173,000,000.00` |
| `Live` | `Short` | `1305.50` | 13,480,000.00 USD | 100.52 USD | 0.00 USD | `+86.09%` | `77,000,000.00` |
| `Live` | `Short` | `1308.50` | 13,480,000.00 USD | 4,050.00 USD | 0.00 USD | `+86.52%` | `3,092,000,000.00` |
| `Live` | `Short` | `1310.50` | 15,330,000.00 USD | 1,850,000.00 USD | 0.00 USD | `+86.80%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1314.50` | 15,500,000.00 USD | 166,790.00 USD | 0.00 USD | `+87.37%` | `126,881,000,000.00` |
| `Live` | `Short` | `1315.50` | 15,500,000.00 USD | 2,630.00 USD | 0.00 USD | `+87.51%` | `2,000,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,520,000.00 USD | 14,130.00 USD | 0.00 USD | `+88.08%` | `10,710,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,520,000.00 USD | 242.93 USD | 0.00 USD | `+89.22%` | `183,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,520,000.00 USD | 184.66 USD | 0.00 USD | `+89.37%` | `139,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,540,000.00 USD | 23,470.00 USD | 0.00 USD | `+89.65%` | `17,640,000,000.00` |
| `Live` | `Short` | `1331.50` | 15,570,000.00 USD | 30,620.00 USD | 0.00 USD | `+89.79%` | `23,000,000,000.00` |
| `Live` | `Short` | `1332.50` | 15,570,000.00 USD | 210.53 USD | 0.00 USD | `+89.94%` | `158,000,000.00` |
| `Live` | `Short` | `1337.50` | 15,630,000.00 USD | 58,170.00 USD | 0.00 USD | `+90.65%` | `43,490,000,000.00` |
| `Live` | `Short` | `1339.50` | 15,630,000.00 USD | 494.28 USD | 0.00 USD | `+90.93%` | `369,000,000.00` |
| `Live` | `Short` | `1344.50` | 15,630,000.00 USD | 4,210.00 USD | 0.00 USD | `+91.65%` | `3,130,000,000.00` |
| `Live` | `Short` | `1347.50` | 15,730,000.00 USD | 94,330.00 USD | 0.00 USD | `+92.07%` | `70,000,000,000.00` |
| `Live` | `Short` | `1359.50` | 15,730,000.00 USD | 121.00 USD | 0.00 USD | `+93.79%` | `89,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,730,000.00 USD | 761.70 USD | 0.00 USD | `+94.93%` | `557,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,780,000.00 USD | 46,880.00 USD | 0.00 USD | `+95.21%` | `34,232,000,000.00` |
| `Live` | `Short` | `1371.50` | 15,780,000.00 USD | 4,110.00 USD | 0.00 USD | `+95.50%` | `3,000,000,000.00` |
| `Live` | `Short` | `1382.50` | 15,850,000.00 USD | 69,120.00 USD | 0.00 USD | `+97.06%` | `50,000,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 3,060,000.00 USD | 0.00 USD | 475.73 USD | `-78.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `288.50` | 3,060,000.00 USD | 0.00 USD | 1,310.00 USD | `-58.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 3,060,000.00 USD | 0.00 USD | 2,400.00 USD | `-57.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 3,060,000.00 USD | 0.00 USD | 333.50 USD | `-52.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 3,060,000.00 USD | 0.00 USD | 8,140.00 USD | `-48.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 3,050,000.00 USD | 0.00 USD | 5,170.00 USD | `-47.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 3,040,000.00 USD | 0.00 USD | 17,290.00 USD | `-42.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 3,020,000.00 USD | 0.00 USD | 25,210.00 USD | `-41.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 3,000,000.00 USD | 0.00 USD | 4,550.00 USD | `-41.20%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 2,990,000.00 USD | 0.00 USD | 8,180.00 USD | `-39.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 2,990,000.00 USD | 0.00 USD | 173.83 USD | `-38.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 2,990,000.00 USD | 0.00 USD | 2,210.00 USD | `-36.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `450.50` | 2,980,000.00 USD | 0.00 USD | 4,660.00 USD | `-35.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 2,980,000.00 USD | 0.00 USD | 698.74 USD | `-35.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 2,980,000.00 USD | 0.00 USD | 2,270.00 USD | `-34.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `457.50` | 2,980,000.00 USD | 0.00 USD | 2,270.00 USD | `-34.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 2,970,000.00 USD | 0.00 USD | 1,750.00 USD | `-34.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 2,970,000.00 USD | 0.00 USD | 3,550.00 USD | `-33.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `485.50` | 2,970,000.00 USD | 0.00 USD | 100.50 USD | `-30.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 2,970,000.00 USD | 0.00 USD | 100.71 USD | `-30.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 2,970,000.00 USD | 0.00 USD | 6,600.00 USD | `-30.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 2,960,000.00 USD | 0.00 USD | 125.06 USD | `-30.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `490.50` | 2,960,000.00 USD | 0.00 USD | 101.53 USD | `-30.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 2,960,000.00 USD | 0.00 USD | 2,450.00 USD | `-29.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `495.50` | 2,960,000.00 USD | 0.00 USD | 102.57 USD | `-29.37%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 2,960,000.00 USD | 0.00 USD | 163.01 USD | `-28.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 2,960,000.00 USD | 0.00 USD | 214.78 USD | `-28.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 2,960,000.00 USD | 0.00 USD | 7,820.00 USD | `-28.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 2,950,000.00 USD | 0.00 USD | 42,390.00 USD | `-28.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 2,910,000.00 USD | 0.00 USD | 138.78 USD | `-27.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 2,910,000.00 USD | 0.00 USD | 185.97 USD | `-27.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 2,910,000.00 USD | 0.00 USD | 1,030.00 USD | `-26.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 2,910,000.00 USD | 0.00 USD | 125.51 USD | `-26.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 2,910,000.00 USD | 0.00 USD | 280.49 USD | `-26.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 2,910,000.00 USD | 0.00 USD | 258.14 USD | `-25.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 2,910,000.00 USD | 0.00 USD | 8,170.00 USD | `-25.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 2,900,000.00 USD | 0.00 USD | 485.16 USD | `-24.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 2,900,000.00 USD | 0.00 USD | 4,650.00 USD | `-23.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 2,890,000.00 USD | 0.00 USD | 1,680.00 USD | `-23.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 2,890,000.00 USD | 0.00 USD | 864.80 USD | `-22.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `547.50` | 2,890,000.00 USD | 0.00 USD | 248.56 USD | `-21.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 2,890,000.00 USD | 0.00 USD | 4,130.00 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 2,890,000.00 USD | 0.00 USD | 366,230.00 USD | `-21.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,520,000.00 USD | 0.00 USD | 1,190.00 USD | `-20.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,520,000.00 USD | 0.00 USD | 611.05 USD | `-20.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,520,000.00 USD | 0.00 USD | 213.52 USD | `-20.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,520,000.00 USD | 0.00 USD | 51,260.00 USD | `-20.39%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,470,000.00 USD | 0.00 USD | 292.02 USD | `-20.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 2,470,000.00 USD | 0.00 USD | 748.48 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 2,470,000.00 USD | 0.00 USD | 199.12 USD | `-19.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 2,470,000.00 USD | 0.00 USD | 808.06 USD | `-19.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,460,000.00 USD | 0.00 USD | 566.50 USD | `-19.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,460,000.00 USD | 0.00 USD | 126.55 USD | `-19.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,460,000.00 USD | 0.00 USD | 5,680.00 USD | `-18.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 2,460,000.00 USD | 0.00 USD | 569.50 USD | `-18.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,460,000.00 USD | 0.00 USD | 774.17 USD | `-18.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,460,000.00 USD | 0.00 USD | 1,700.00 USD | `-18.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,460,000.00 USD | 0.00 USD | 291.91 USD | `-18.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,460,000.00 USD | 0.00 USD | 469.61 USD | `-17.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,450,000.00 USD | 0.00 USD | 289.98 USD | `-17.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,450,000.00 USD | 0.00 USD | 285.86 USD | `-17.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,450,000.00 USD | 0.00 USD | 289.17 USD | `-17.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,450,000.00 USD | 0.00 USD | 6,750.00 USD | `-17.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,450,000.00 USD | 0.00 USD | 1,240.00 USD | `-17.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 2,450,000.00 USD | 0.00 USD | 6,980.00 USD | `-16.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,440,000.00 USD | 0.00 USD | 287.67 USD | `-16.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,440,000.00 USD | 0.00 USD | 763.94 USD | `-16.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,440,000.00 USD | 0.00 USD | 542.76 USD | `-16.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,440,000.00 USD | 0.00 USD | 34,020.00 USD | `-16.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,400,000.00 USD | 0.00 USD | 830,190.00 USD | `-16.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,570,000.00 USD | 0.00 USD | 1,220.00 USD | `-15.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,570,000.00 USD | 0.00 USD | 540.31 USD | `-15.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `591.50` | 1,570,000.00 USD | 0.00 USD | 109.43 USD | `-15.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,570,000.00 USD | 0.00 USD | 698.56 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 1,570,000.00 USD | 0.00 USD | 1,160.00 USD | `-15.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 1,570,000.00 USD | 0.00 USD | 119.30 USD | `-14.97%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 1,570,000.00 USD | 0.00 USD | 222.87 USD | `-14.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,570,000.00 USD | 0.00 USD | 244.79 USD | `-14.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `599.50` | 1,570,000.00 USD | 0.00 USD | 145.68 USD | `-14.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,570,000.00 USD | 0.00 USD | 57,400.00 USD | `-14.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 1,510,000.00 USD | 0.00 USD | 1,590.00 USD | `-14.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,510,000.00 USD | 0.00 USD | 46,760.00 USD | `-14.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 1,460,000.00 USD | 0.00 USD | 937.84 USD | `-13.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,460,000.00 USD | 0.00 USD | 1,870.00 USD | `-13.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,460,000.00 USD | 0.00 USD | 8,040.00 USD | `-13.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 1,450,000.00 USD | 0.00 USD | 18,380.00 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 1,430,000.00 USD | 0.00 USD | 30,480.00 USD | `-13.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 1,400,000.00 USD | 0.00 USD | 12,220.00 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,390,000.00 USD | 0.00 USD | 4,470.00 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,390,000.00 USD | 0.00 USD | 269.15 USD | `-12.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,390,000.00 USD | 0.00 USD | 2,380.00 USD | `-12.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,380,000.00 USD | 0.00 USD | 120.83 USD | `-12.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,380,000.00 USD | 0.00 USD | 13,170.00 USD | `-11.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 1,370,000.00 USD | 0.00 USD | 1,980.00 USD | `-11.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 1,370,000.00 USD | 0.00 USD | 219.47 USD | `-11.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 1,370,000.00 USD | 0.00 USD | 445.27 USD | `-10.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,370,000.00 USD | 0.00 USD | 445.98 USD | `-10.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 1,370,000.00 USD | 0.00 USD | 694.79 USD | `-10.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 1,370,000.00 USD | 0.00 USD | 916.15 USD | `-10.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 1,370,000.00 USD | 0.00 USD | 746.03 USD | `-10.41%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 1,370,000.00 USD | 0.00 USD | 2,740.00 USD | `-10.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,360,000.00 USD | 0.00 USD | 861.26 USD | `-10.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 1,360,000.00 USD | 0.00 USD | 179.98 USD | `-9.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 1,360,000.00 USD | 0.00 USD | 4,900.00 USD | `-9.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,360,000.00 USD | 0.00 USD | 164.08 USD | `-9.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 1,360,000.00 USD | 0.00 USD | 6,760.00 USD | `-9.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 1,350,000.00 USD | 0.00 USD | 2,730.00 USD | `-9.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,350,000.00 USD | 0.00 USD | 3,640.00 USD | `-8.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 1,340,000.00 USD | 0.00 USD | 384.98 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 1,340,000.00 USD | 0.00 USD | 429.78 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 1,340,000.00 USD | 0.00 USD | 352.18 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 1,340,000.00 USD | 0.00 USD | 357.87 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 1,340,000.00 USD | 0.00 USD | 1,980.00 USD | `-8.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 1,340,000.00 USD | 0.00 USD | 3,790.00 USD | `-8.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,340,000.00 USD | 0.00 USD | 10,640.00 USD | `-7.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,330,000.00 USD | 0.00 USD | 971.04 USD | `-7.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 1,320,000.00 USD | 0.00 USD | 1,800.00 USD | `-7.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,320,000.00 USD | 0.00 USD | 107.17 USD | `-7.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,320,000.00 USD | 0.00 USD | 28,620.00 USD | `-7.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,290,000.00 USD | 0.00 USD | 5,890.00 USD | `-7.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,290,000.00 USD | 0.00 USD | 2,020.00 USD | `-6.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,290,000.00 USD | 0.00 USD | 308.92 USD | `-6.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 1,290,000.00 USD | 0.00 USD | 165.84 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,290,000.00 USD | 0.00 USD | 456.27 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,280,000.00 USD | 0.00 USD | 110.46 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 1,280,000.00 USD | 0.00 USD | 1,320.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,280,000.00 USD | 0.00 USD | 13,060.00 USD | `-5.99%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,270,000.00 USD | 0.00 USD | 567.37 USD | `-5.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 1,270,000.00 USD | 0.00 USD | 11,440.00 USD | `-5.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,260,000.00 USD | 0.00 USD | 5,480.00 USD | `-5.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 1,250,000.00 USD | 0.00 USD | 4,040.00 USD | `-5.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 1,250,000.00 USD | 0.00 USD | 713.01 USD | `-5.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 1,250,000.00 USD | 0.00 USD | 576.32 USD | `-5.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,250,000.00 USD | 0.00 USD | 24,530.00 USD | `-5.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 1,220,000.00 USD | 0.00 USD | 586.07 USD | `-4.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 1,220,000.00 USD | 0.00 USD | 719.97 USD | `-4.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,220,000.00 USD | 0.00 USD | 2,390.00 USD | `-4.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,220,000.00 USD | 0.00 USD | 135,800.00 USD | `-4.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 1,080,000.00 USD | 0.00 USD | 4,020.00 USD | `-4.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,080,000.00 USD | 0.00 USD | 68,120.00 USD | `-4.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 1,010,000.00 USD | 0.00 USD | 3,460.00 USD | `-4.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 1,010,000.00 USD | 0.00 USD | 1,470.00 USD | `-3.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 1,010,000.00 USD | 0.00 USD | 8,350.00 USD | `-3.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 998,140.00 USD | 0.00 USD | 56,170.00 USD | `-3.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 941,960.00 USD | 0.00 USD | 39,650.00 USD | `-3.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 902,320.00 USD | 0.00 USD | 825.73 USD | `-3.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 901,490.00 USD | 0.00 USD | 101,080.00 USD | `-3.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 800,410.00 USD | 0.00 USD | 3,200.00 USD | `-3.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 797,200.00 USD | 0.00 USD | 146.52 USD | `-2.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 797,060.00 USD | 0.00 USD | 5,290.00 USD | `-2.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 791,770.00 USD | 0.00 USD | 171,850.00 USD | `-2.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 619,920.00 USD | 0.00 USD | 171,120.00 USD | `-2.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 448,790.00 USD | 0.00 USD | 17,880.00 USD | `-2.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 430,910.00 USD | 0.00 USD | 780.55 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 430,130.00 USD | 0.00 USD | 323.12 USD | `-2.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 429,810.00 USD | 0.00 USD | 382.81 USD | `-1.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 429,430.00 USD | 0.00 USD | 996.33 USD | `-1.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 428,430.00 USD | 0.00 USD | 76,650.00 USD | `-1.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 351,780.00 USD | 0.00 USD | 176,810.00 USD | `-1.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 174,970.00 USD | 0.00 USD | 4,720.00 USD | `-1.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 170,250.00 USD | 0.00 USD | 990.32 USD | `-1.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 169,260.00 USD | 0.00 USD | 1,540.00 USD | `-1.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 167,720.00 USD | 0.00 USD | 11,730.00 USD | `-0.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 155,990.00 USD | 0.00 USD | 9,290.00 USD | `-0.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 146,700.00 USD | 0.00 USD | 47,550.00 USD | `-0.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 99,150.00 USD | 0.00 USD | 291.97 USD | `-0.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 98,860.00 USD | 0.00 USD | 38,470.00 USD | `-0.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 60,390.00 USD | 0.00 USD | 59,710.00 USD | `-0.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 681.16 USD | 0.00 USD | 681.16 USD | `-0.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `702.50` | 7,030.00 USD | 7,030.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `703.50` | 9,020.00 USD | 1,990.00 USD | 0.00 USD | `+0.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `704.50` | 14,500.00 USD | 5,480.00 USD | 0.00 USD | `+0.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `705.50` | 19,330.00 USD | 4,830.00 USD | 0.00 USD | `+0.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `706.50` | 23,170.00 USD | 3,840.00 USD | 0.00 USD | `+0.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `707.50` | 36,440.00 USD | 13,270.00 USD | 0.00 USD | `+0.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `708.50` | 39,380.00 USD | 2,940.00 USD | 0.00 USD | `+0.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `709.50` | 40,740.00 USD | 1,360.00 USD | 0.00 USD | `+1.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `710.50` | 47,960.00 USD | 7,210.00 USD | 0.00 USD | `+1.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `711.50` | 82,300.00 USD | 34,340.00 USD | 0.00 USD | `+1.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `712.50` | 89,420.00 USD | 7,130.00 USD | 0.00 USD | `+1.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `713.50` | 107,420.00 USD | 18,000.00 USD | 0.00 USD | `+1.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `714.50` | 108,000.00 USD | 578.03 USD | 0.00 USD | `+1.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `715.50` | 111,100.00 USD | 3,100.00 USD | 0.00 USD | `+1.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `716.50` | 112,490.00 USD | 1,390.00 USD | 0.00 USD | `+2.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 114,630.00 USD | 2,140.00 USD | 0.00 USD | `+2.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 175,300.00 USD | 60,670.00 USD | 0.00 USD | `+2.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 245,540.00 USD | 70,240.00 USD | 0.00 USD | `+2.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 248,830.00 USD | 3,290.00 USD | 0.00 USD | `+2.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 302,400.00 USD | 53,570.00 USD | 0.00 USD | `+2.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 313,050.00 USD | 10,650.00 USD | 0.00 USD | `+2.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 322,330.00 USD | 9,280.00 USD | 0.00 USD | `+3.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 347,830.00 USD | 25,500.00 USD | 0.00 USD | `+3.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 442,410.00 USD | 94,580.00 USD | 0.00 USD | `+3.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 442,910.00 USD | 501.28 USD | 0.00 USD | `+3.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 461,880.00 USD | 18,970.00 USD | 0.00 USD | `+3.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 515,050.00 USD | 53,170.00 USD | 0.00 USD | `+3.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 650,590.00 USD | 135,540.00 USD | 0.00 USD | `+3.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 655,020.00 USD | 4,430.00 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 854,010.00 USD | 198,990.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 855,420.00 USD | 1,410.00 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,340,000.00 USD | 487,680.00 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,350,000.00 USD | 7,480.00 USD | 0.00 USD | `+4.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,370,000.00 USD | 23,100.00 USD | 0.00 USD | `+4.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,380,000.00 USD | 5,460.00 USD | 0.00 USD | `+4.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,380,000.00 USD | 685.88 USD | 0.00 USD | `+5.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,390,000.00 USD | 13,480.00 USD | 0.00 USD | `+5.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,400,000.00 USD | 3,420.00 USD | 0.00 USD | `+5.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,400,000.00 USD | 2,110.00 USD | 0.00 USD | `+5.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,400,000.00 USD | 3,960.00 USD | 0.00 USD | `+5.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,420,000.00 USD | 17,990.00 USD | 0.00 USD | `+5.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,430,000.00 USD | 8,280.00 USD | 0.00 USD | `+5.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,630,000.00 USD | 203,810.00 USD | 0.00 USD | `+6.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,640,000.00 USD | 3,390.00 USD | 0.00 USD | `+6.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,710,000.00 USD | 76,650.00 USD | 0.00 USD | `+6.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,710,000.00 USD | 1,240.00 USD | 0.00 USD | `+6.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,710,000.00 USD | 279.19 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,720,000.00 USD | 704.53 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,720,000.00 USD | 123.83 USD | 0.00 USD | `+6.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,720,000.00 USD | 8,720.00 USD | 0.00 USD | `+7.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,730,000.00 USD | 2,730.00 USD | 0.00 USD | `+7.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,730,000.00 USD | 629.17 USD | 0.00 USD | `+7.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,770,000.00 USD | 47,160.00 USD | 0.00 USD | `+7.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,780,000.00 USD | 4,420.00 USD | 0.00 USD | `+7.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,790,000.00 USD | 10,340.00 USD | 0.00 USD | `+7.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,930,000.00 USD | 142,940.00 USD | 0.00 USD | `+7.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,930,000.00 USD | 665.96 USD | 0.00 USD | `+8.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 1,930,000.00 USD | 325.07 USD | 0.00 USD | `+8.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,220,000.00 USD | 287,930.00 USD | 0.00 USD | `+8.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,230,000.00 USD | 11,460.00 USD | 0.00 USD | `+8.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,230,000.00 USD | 239.43 USD | 0.00 USD | `+8.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,260,000.00 USD | 29,030.00 USD | 0.00 USD | `+8.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,260,000.00 USD | 240.05 USD | 0.00 USD | `+8.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,320,000.00 USD | 60,710.00 USD | 0.00 USD | `+9.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,320,000.00 USD | 331.13 USD | 0.00 USD | `+9.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,790,000.00 USD | 468,310.00 USD | 0.00 USD | `+9.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,790,000.00 USD | 180.60 USD | 0.00 USD | `+9.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,790,000.00 USD | 171.60 USD | 0.00 USD | `+9.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,790,000.00 USD | 1,540.00 USD | 0.00 USD | `+9.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,790,000.00 USD | 242.25 USD | 0.00 USD | `+9.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,810,000.00 USD | 12,400.00 USD | 0.00 USD | `+10.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,810,000.00 USD | 656.70 USD | 0.00 USD | `+10.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,820,000.00 USD | 9,680.00 USD | 0.00 USD | `+10.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,820,000.00 USD | 4,570.00 USD | 0.00 USD | `+10.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,840,000.00 USD | 14,230.00 USD | 0.00 USD | `+10.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,850,000.00 USD | 15,690.00 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,860,000.00 USD | 9,990.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,860,000.00 USD | 132.52 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,890,000.00 USD | 24,280.00 USD | 0.00 USD | `+11.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,890,000.00 USD | 2,050.00 USD | 0.00 USD | `+11.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,890,000.00 USD | 1,900.00 USD | 0.00 USD | `+11.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,890,000.00 USD | 101.07 USD | 0.00 USD | `+11.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,890,000.00 USD | 102.77 USD | 0.00 USD | `+11.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,890,000.00 USD | 559.28 USD | 0.00 USD | `+11.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,900,000.00 USD | 5,610.00 USD | 0.00 USD | `+12.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,900,000.00 USD | 2,260.00 USD | 0.00 USD | `+12.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,900,000.00 USD | 133.26 USD | 0.00 USD | `+12.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,910,000.00 USD | 15,650.00 USD | 0.00 USD | `+12.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,910,000.00 USD | 704.44 USD | 0.00 USD | `+12.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,920,000.00 USD | 4,360.00 USD | 0.00 USD | `+12.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,920,000.00 USD | 1,450.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,920,000.00 USD | 3,630.00 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,930,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,930,000.00 USD | 154.52 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `798.50` | 2,930,000.00 USD | 7,140.00 USD | 0.00 USD | `+13.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,940,000.00 USD | 1,260.00 USD | 0.00 USD | `+13.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,960,000.00 USD | 25,190.00 USD | 0.00 USD | `+14.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,960,000.00 USD | 120.22 USD | 0.00 USD | `+14.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,960,000.00 USD | 803.50 USD | 0.00 USD | `+14.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,960,000.00 USD | 120.02 USD | 0.00 USD | `+14.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,960,000.00 USD | 1,300.00 USD | 0.00 USD | `+14.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,970,000.00 USD | 5,010.00 USD | 0.00 USD | `+15.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,970,000.00 USD | 242.04 USD | 0.00 USD | `+15.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 2,970,000.00 USD | 2,870.00 USD | 0.00 USD | `+15.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 2,970,000.00 USD | 374.10 USD | 0.00 USD | `+15.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 2,970,000.00 USD | 844.19 USD | 0.00 USD | `+15.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 2,970,000.00 USD | 118.77 USD | 0.00 USD | `+15.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 2,980,000.00 USD | 3,390.00 USD | 0.00 USD | `+16.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 2,980,000.00 USD | 984.70 USD | 0.00 USD | `+16.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 2,980,000.00 USD | 162.68 USD | 0.00 USD | `+16.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 2,980,000.00 USD | 5,990.00 USD | 0.00 USD | `+16.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 2,990,000.00 USD | 7,820.00 USD | 0.00 USD | `+16.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 2,990,000.00 USD | 408.13 USD | 0.00 USD | `+17.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 2,990,000.00 USD | 672.77 USD | 0.00 USD | `+17.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 2,990,000.00 USD | 276.38 USD | 0.00 USD | `+17.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 2,990,000.00 USD | 1,800.00 USD | 0.00 USD | `+18.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 3,030,000.00 USD | 35,850.00 USD | 0.00 USD | `+18.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 3,030,000.00 USD | 1,050.00 USD | 0.00 USD | `+18.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 3,030,000.00 USD | 187.15 USD | 0.00 USD | `+19.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 3,030,000.00 USD | 372.24 USD | 0.00 USD | `+19.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 3,030,000.00 USD | 326.62 USD | 0.00 USD | `+19.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 3,030,000.00 USD | 296.34 USD | 0.00 USD | `+19.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 3,040,000.00 USD | 5,040.00 USD | 0.00 USD | `+19.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 3,040,000.00 USD | 329.87 USD | 0.00 USD | `+19.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 3,040,000.00 USD | 425.97 USD | 0.00 USD | `+20.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 3,040,000.00 USD | 1,770.00 USD | 0.00 USD | `+20.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 3,040,000.00 USD | 2,550.00 USD | 0.00 USD | `+21.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 3,050,000.00 USD | 11,650.00 USD | 0.00 USD | `+21.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 3,050,000.00 USD | 102.30 USD | 0.00 USD | `+21.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 3,050,000.00 USD | 137.57 USD | 0.00 USD | `+21.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 3,060,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 3,060,000.00 USD | 1,160.00 USD | 0.00 USD | `+22.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 3,060,000.00 USD | 1,200.00 USD | 0.00 USD | `+22.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 3,060,000.00 USD | 874.73 USD | 0.00 USD | `+23.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 3,060,000.00 USD | 2,970.00 USD | 0.00 USD | `+23.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 3,070,000.00 USD | 3,460.00 USD | 0.00 USD | `+23.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 3,070,000.00 USD | 2,610.00 USD | 0.00 USD | `+23.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 3,070,000.00 USD | 228.07 USD | 0.00 USD | `+24.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 3,070,000.00 USD | 1,110.00 USD | 0.00 USD | `+24.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,120,000.00 USD | 54,820.00 USD | 0.00 USD | `+26.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,120,000.00 USD | 266.55 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,120,000.00 USD | 690.14 USD | 0.00 USD | `+26.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,130,000.00 USD | 605.33 USD | 0.00 USD | `+27.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `895.50` | 3,130,000.00 USD | 130.74 USD | 0.00 USD | `+27.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `898.50` | 3,130,000.00 USD | 101.53 USD | 0.00 USD | `+28.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,250,000.00 USD | 126,250.00 USD | 0.00 USD | `+28.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,250,000.00 USD | 167.33 USD | 0.00 USD | `+28.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,250,000.00 USD | 1,640.00 USD | 0.00 USD | `+29.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,250,000.00 USD | 908.02 USD | 0.00 USD | `+30.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,260,000.00 USD | 4,150.00 USD | 0.00 USD | `+30.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,260,000.00 USD | 533.99 USD | 0.00 USD | `+30.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,260,000.00 USD | 166.43 USD | 0.00 USD | `+31.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,260,000.00 USD | 463.01 USD | 0.00 USD | `+31.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,260,000.00 USD | 320.57 USD | 0.00 USD | `+32.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,260,000.00 USD | 552.72 USD | 0.00 USD | `+32.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,260,000.00 USD | 196.03 USD | 0.00 USD | `+33.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,260,000.00 USD | 287.20 USD | 0.00 USD | `+33.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,260,000.00 USD | 890.45 USD | 0.00 USD | `+36.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,260,000.00 USD | 498.94 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,260,000.00 USD | 964.50 USD | 0.00 USD | `+37.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,270,000.00 USD | 1,930.00 USD | 0.00 USD | `+37.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,270,000.00 USD | 293.25 USD | 0.00 USD | `+39.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,270,000.00 USD | 1,300.00 USD | 0.00 USD | `+39.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,270,000.00 USD | 109.93 USD | 0.00 USD | `+39.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,270,000.00 USD | 439.09 USD | 0.00 USD | `+40.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,270,000.00 USD | 2,590.00 USD | 0.00 USD | `+40.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,270,000.00 USD | 145.34 USD | 0.00 USD | `+41.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,270,000.00 USD | 1,780.00 USD | 0.00 USD | `+42.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,280,000.00 USD | 3,990.00 USD | 0.00 USD | `+42.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,280,000.00 USD | 938.53 USD | 0.00 USD | `+42.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,290,000.00 USD | 11,810.00 USD | 0.00 USD | `+42.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,290,000.00 USD | 203.50 USD | 0.00 USD | `+45.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,290,000.00 USD | 148.99 USD | 0.00 USD | `+45.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,290,000.00 USD | 149.87 USD | 0.00 USD | `+46.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,290,000.00 USD | 150.45 USD | 0.00 USD | `+46.89%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,290,000.00 USD | 195.51 USD | 0.00 USD | `+49.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,290,000.00 USD | 149.60 USD | 0.00 USD | `+50.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,290,000.00 USD | 156.58 USD | 0.00 USD | `+52.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,290,000.00 USD | 278.43 USD | 0.00 USD | `+56.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,290,000.00 USD | 555.75 USD | 0.00 USD | `+58.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,290,000.00 USD | 165.93 USD | 0.00 USD | `+62.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,290,000.00 USD | 167.39 USD | 0.00 USD | `+63.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,350,000.00 USD | 62,330.00 USD | 0.00 USD | `+71.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,350,000.00 USD | 1,250.00 USD | 0.00 USD | `+71.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,360,000.00 USD | 235.49 USD | 0.00 USD | `+74.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,360,000.00 USD | 3,580.00 USD | 0.00 USD | `+75.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,360,000.00 USD | 421.42 USD | 0.00 USD | `+78.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,360,000.00 USD | 3,750.00 USD | 0.00 USD | `+82.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,360,000.00 USD | 133.64 USD | 0.00 USD | `+84.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,360,000.00 USD | 685.36 USD | 0.00 USD | `+85.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,420,000.00 USD | 58,230.00 USD | 0.00 USD | `+89.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,500,000.00 USD | 80,850.00 USD | 0.00 USD | `+91.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,510,000.00 USD | 6,210.00 USD | 0.00 USD | `+93.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,510,000.00 USD | 349.06 USD | 0.00 USD | `+94.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,510,000.00 USD | 1,060.00 USD | 0.00 USD | `+95.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,530,000.00 USD | 19,210.00 USD | 0.00 USD | `+95.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,530,000.00 USD | 425.19 USD | 0.00 USD | `+98.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,530,000.00 USD | 3,850.00 USD | 0.00 USD | `+99.63%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `7D` | `609.90` | 39,280,000.00 USD | 0.00 USD | 39,280,000.00 USD | 30,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `620.90` | 39,250,000.00 USD | 0.00 USD | 39,250,000.00 USD | 0.00 USD | 55,460.00 USD | 265,620.00 USD |
| `7D` | `621.90` | 38,930,000.00 USD | 0.00 USD | 38,930,000.00 USD | 310,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `626.90` | 38,620,000.00 USD | 0.00 USD | 38,620,000.00 USD | 42,610.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `628.90` | 38,580,000.00 USD | 0.00 USD | 38,580,000.00 USD | 261,840.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `629.90` | 38,310,000.00 USD | 0.00 USD | 38,310,000.00 USD | 0.00 USD | 0.00 USD | 255,750.00 USD |
| `1D` | `630.90` | 51,890,000.00 USD | 0.00 USD | 51,890,000.00 USD | 18,100.00 USD | 56,930.00 USD | 337,840.00 USD |
| `7D` | `630.90` | 38,060,000.00 USD | 0.00 USD | 38,060,000.00 USD | 230,570.00 USD | 50,030.00 USD | 0.00 USD |
| `1D` | `631.70` | 51,470,000.00 USD | 0.00 USD | 51,470,000.00 USD | 67,470.00 USD | 84,770.00 USD | 582,650.00 USD |
| `7D` | `631.90` | 37,780,000.00 USD | 0.00 USD | 37,780,000.00 USD | 58,820.00 USD | 88,750.00 USD | 0.00 USD |
| `1D` | `632.50` | 50,740,000.00 USD | 0.00 USD | 50,740,000.00 USD | 545,170.00 USD | 64,140.00 USD | 117,930.00 USD |
| `1D` | `633.30` | 50,010,000.00 USD | 0.00 USD | 50,010,000.00 USD | 140,890.00 USD | 11,550.00 USD | 26,530.00 USD |
| `7D` | `633.90` | 37,630,000.00 USD | 0.00 USD | 37,630,000.00 USD | 70,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `634.10` | 49,830,000.00 USD | 0.00 USD | 49,830,000.00 USD | 194,950.00 USD | 30,650.00 USD | 93,550.00 USD |
| `1D` | `634.90` | 49,510,000.00 USD | 0.00 USD | 49,510,000.00 USD | 0.00 USD | 16,410.00 USD | 65,250.00 USD |
| `7D` | `634.90` | 37,560,000.00 USD | 0.00 USD | 37,560,000.00 USD | 0.00 USD | 51,290.00 USD | 0.00 USD |
| `1D` | `635.70` | 49,430,000.00 USD | 0.00 USD | 49,430,000.00 USD | 140,670.00 USD | 9,540.00 USD | 58,120.00 USD |
| `7D` | `635.90` | 37,510,000.00 USD | 0.00 USD | 37,510,000.00 USD | 90,060.00 USD | 17,990.00 USD | 0.00 USD |
| `1D` | `636.50` | 49,220,000.00 USD | 0.00 USD | 49,220,000.00 USD | 120,680.00 USD | 66,890.00 USD | 240,130.00 USD |
| `1D` | `637.30` | 48,790,000.00 USD | 0.00 USD | 48,790,000.00 USD | 69,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `638.10` | 48,730,000.00 USD | 0.00 USD | 48,730,000.00 USD | 24,710.00 USD | 37,610.00 USD | 0.00 USD |
| `1D` | `638.90` | 48,660,000.00 USD | 0.00 USD | 48,660,000.00 USD | 186,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `639.70` | 48,480,000.00 USD | 0.00 USD | 48,480,000.00 USD | 59,770.00 USD | 0.00 USD | 184,710.00 USD |
| `7D` | `640.90` | 37,400,000.00 USD | 0.00 USD | 37,400,000.00 USD | 0.00 USD | 0.00 USD | 224,770.00 USD |
| `1D` | `641.30` | 48,230,000.00 USD | 0.00 USD | 48,230,000.00 USD | 59,370.00 USD | 0.00 USD | 4,880.00 USD |
| `7D` | `641.90` | 37,170,000.00 USD | 0.00 USD | 37,170,000.00 USD | 0.00 USD | 40,220.00 USD | 0.00 USD |
| `1D` | `642.10` | 48,170,000.00 USD | 0.00 USD | 48,170,000.00 USD | 171,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `642.90` | 48,000,000.00 USD | 0.00 USD | 48,000,000.00 USD | 51,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `642.90` | 37,130,000.00 USD | 0.00 USD | 37,130,000.00 USD | 171,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `643.70` | 47,950,000.00 USD | 0.00 USD | 47,950,000.00 USD | 51,730.00 USD | 10,060.00 USD | 0.00 USD |
| `7D` | `643.90` | 36,960,000.00 USD | 0.00 USD | 36,960,000.00 USD | 35,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.50` | 47,880,000.00 USD | 0.00 USD | 47,880,000.00 USD | 393,100.00 USD | 33,090.00 USD | 341,610.00 USD |
| `7D` | `644.90` | 36,930,000.00 USD | 0.00 USD | 36,930,000.00 USD | 0.00 USD | 24,160.00 USD | 0.00 USD |
| `1D` | `645.30` | 47,120,000.00 USD | 0.00 USD | 47,120,000.00 USD | 93,740.00 USD | 4,720.00 USD | 0.00 USD |
| `7D` | `645.90` | 36,900,000.00 USD | 0.00 USD | 36,900,000.00 USD | 0.00 USD | 0.00 USD | 73,770.00 USD |
| `1D` | `646.10` | 47,020,000.00 USD | 0.00 USD | 47,020,000.00 USD | 174,120.00 USD | 11,780.00 USD | 180,100.00 USD |
| `1D` | `646.90` | 46,650,000.00 USD | 0.00 USD | 46,650,000.00 USD | 176,670.00 USD | 2,560.00 USD | 31,190.00 USD |
| `7D` | `646.90` | 36,830,000.00 USD | 0.00 USD | 36,830,000.00 USD | 45,640.00 USD | 18,000.00 USD | 105,680.00 USD |
| `1D` | `647.70` | 46,440,000.00 USD | 0.00 USD | 46,440,000.00 USD | 164,610.00 USD | 33,700.00 USD | 14,210.00 USD |
| `7D` | `647.90` | 36,660,000.00 USD | 0.00 USD | 36,660,000.00 USD | 122,600.00 USD | 16,830.00 USD | 14,870.00 USD |
| `1D` | `648.50` | 46,230,000.00 USD | 0.00 USD | 46,230,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `648.90` | 36,510,000.00 USD | 0.00 USD | 36,510,000.00 USD | 0.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `649.30` | 46,140,000.00 USD | 0.00 USD | 46,140,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `649.90` | 36,490,000.00 USD | 0.00 USD | 36,490,000.00 USD | 162,040.00 USD | 15,690.00 USD | 0.00 USD |
| `1D` | `650.10` | 46,090,000.00 USD | 0.00 USD | 46,090,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `650.90` | 46,020,000.00 USD | 0.00 USD | 46,020,000.00 USD | 16,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `650.90` | 36,310,000.00 USD | 0.00 USD | 36,310,000.00 USD | 23,920.00 USD | 14,650.00 USD | 14,200.00 USD |
| `1D` | `651.70` | 46,010,000.00 USD | 0.00 USD | 46,010,000.00 USD | 167,330.00 USD | 0.00 USD | 94,590.00 USD |
| `7D` | `651.90` | 36,260,000.00 USD | 0.00 USD | 36,260,000.00 USD | 92,240.00 USD | 33,210.00 USD | 140,720.00 USD |
| `1D` | `652.50` | 45,740,000.00 USD | 0.00 USD | 45,740,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `652.90` | 35,990,000.00 USD | 0.00 USD | 35,990,000.00 USD | 213,140.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.30` | 45,710,000.00 USD | 0.00 USD | 45,710,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.10` | 45,640,000.00 USD | 0.00 USD | 45,640,000.00 USD | 67,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `654.90` | 45,570,000.00 USD | 0.00 USD | 45,570,000.00 USD | 111,480.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `654.90` | 35,780,000.00 USD | 0.00 USD | 35,780,000.00 USD | 163,670.00 USD | 8,370.00 USD | 21,920.00 USD |
| `1D` | `655.70` | 45,460,000.00 USD | 0.00 USD | 45,460,000.00 USD | 202,940.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `655.90` | 35,590,000.00 USD | 0.00 USD | 35,590,000.00 USD | 47,200.00 USD | 16,330.00 USD | 0.00 USD |
| `1D` | `656.50` | 45,260,000.00 USD | 0.00 USD | 45,260,000.00 USD | 136,660.00 USD | 40,970.00 USD | 825,700.00 USD |
| `7D` | `656.90` | 35,520,000.00 USD | 0.00 USD | 35,520,000.00 USD | 105,420.00 USD | 0.00 USD | 10,970.00 USD |
| `1D` | `657.30` | 44,260,000.00 USD | 0.00 USD | 44,260,000.00 USD | 211,880.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `657.90` | 35,410,000.00 USD | 0.00 USD | 35,410,000.00 USD | 0.00 USD | 7,610.00 USD | 19,000.00 USD |
| `1D` | `658.10` | 44,040,000.00 USD | 0.00 USD | 44,040,000.00 USD | 875,210.00 USD | 14,920.00 USD | 21,320.00 USD |
| `1D` | `658.90` | 43,130,000.00 USD | 0.00 USD | 43,130,000.00 USD | 119,820.00 USD | 0.00 USD | 81,440.00 USD |
| `7D` | `658.90` | 35,380,000.00 USD | 0.00 USD | 35,380,000.00 USD | 0.00 USD | 18,790.00 USD | 13,980.00 USD |
| `1D` | `659.70` | 42,930,000.00 USD | 0.00 USD | 42,930,000.00 USD | 111,490.00 USD | 7,460.00 USD | 0.00 USD |
| `7D` | `659.90` | 35,350,000.00 USD | 0.00 USD | 35,350,000.00 USD | 38,970.00 USD | 12,000.00 USD | 98,990.00 USD |
| `1D` | `660.50` | 42,810,000.00 USD | 0.00 USD | 42,810,000.00 USD | 90,670.00 USD | 0.00 USD | 14,670.00 USD |
| `7D` | `660.90` | 35,200,000.00 USD | 0.00 USD | 35,200,000.00 USD | 277,360.00 USD | 17,690.00 USD | 14,570.00 USD |
| `1D` | `661.30` | 42,710,000.00 USD | 0.00 USD | 42,710,000.00 USD | 462,080.00 USD | 83,170.00 USD | 0.00 USD |
| `7D` | `661.90` | 34,890,000.00 USD | 0.00 USD | 34,890,000.00 USD | 123,210.00 USD | 13,120.00 USD | 692,280.00 USD |
| `1D` | `662.10` | 42,160,000.00 USD | 0.00 USD | 42,160,000.00 USD | 139,750.00 USD | 155,800.00 USD | 0.00 USD |
| `1D` | `662.90` | 41,870,000.00 USD | 0.00 USD | 41,870,000.00 USD | 274,050.00 USD | 0.00 USD | 44,630.00 USD |
| `7D` | `662.90` | 34,060,000.00 USD | 0.00 USD | 34,060,000.00 USD | 166,320.00 USD | 144,590.00 USD | 36,490.00 USD |
| `1D` | `663.70` | 41,550,000.00 USD | 0.00 USD | 41,550,000.00 USD | 16,980.00 USD | 69,400.00 USD | 64,090.00 USD |
| `7D` | `663.90` | 33,710,000.00 USD | 0.00 USD | 33,710,000.00 USD | 943,280.00 USD | 18,740.00 USD | 22,460.00 USD |
| `1D` | `664.50` | 41,400,000.00 USD | 0.00 USD | 41,400,000.00 USD | 1,300,000.00 USD | 0.00 USD | 61,580.00 USD |
| `7D` | `664.90` | 32,730,000.00 USD | 0.00 USD | 32,730,000.00 USD | 237,720.00 USD | 22,990.00 USD | 50,380.00 USD |
| `1D` | `665.30` | 40,030,000.00 USD | 0.00 USD | 40,030,000.00 USD | 181,030.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 32,420,000.00 USD | 0.00 USD | 32,420,000.00 USD | 398,250.00 USD | 60,610.00 USD | 63,410.00 USD |
| `1D` | `666.10` | 39,840,000.00 USD | 0.00 USD | 39,840,000.00 USD | 846,450.00 USD | 88,780.00 USD | 750,630.00 USD |
| `1D` | `666.90` | 38,150,000.00 USD | 0.00 USD | 38,150,000.00 USD | 845,590.00 USD | 13,270.00 USD | 31,410.00 USD |
| `7D` | `666.90` | 31,890,000.00 USD | 0.00 USD | 31,890,000.00 USD | 425,290.00 USD | 33,320.00 USD | 53,950.00 USD |
| `1D` | `667.70` | 37,260,000.00 USD | 0.00 USD | 37,260,000.00 USD | 541,360.00 USD | 167,750.00 USD | 9,290.00 USD |
| `7D` | `667.90` | 31,380,000.00 USD | 0.00 USD | 31,380,000.00 USD | 1,050,000.00 USD | 67,080.00 USD | 67,320.00 USD |
| `1D` | `668.50` | 36,540,000.00 USD | 0.00 USD | 36,540,000.00 USD | 774,260.00 USD | 39,300.00 USD | 3,620.00 USD |
| `7D` | `668.90` | 30,200,000.00 USD | 0.00 USD | 30,200,000.00 USD | 738,400.00 USD | 70,910.00 USD | 72,340.00 USD |
| `1D` | `669.30` | 35,730,000.00 USD | 0.00 USD | 35,730,000.00 USD | 365,600.00 USD | 58,270.00 USD | 29,910.00 USD |
| `7D` | `669.90` | 29,320,000.00 USD | 0.00 USD | 29,320,000.00 USD | 240,000.00 USD | 38,130.00 USD | 71,700.00 USD |
| `1D` | `670.10` | 35,270,000.00 USD | 0.00 USD | 35,270,000.00 USD | 609,810.00 USD | 42,060.00 USD | 1,500,000.00 USD |
| `1D` | `670.90` | 33,120,000.00 USD | 0.00 USD | 33,120,000.00 USD | 289,790.00 USD | 21,410.00 USD | 2,650.00 USD |
| `7D` | `670.90` | 28,970,000.00 USD | 0.00 USD | 28,970,000.00 USD | 760,980.00 USD | 135,260.00 USD | 102,340.00 USD |
| `1D` | `671.70` | 32,810,000.00 USD | 0.00 USD | 32,810,000.00 USD | 2,340,000.00 USD | 21,250.00 USD | 46,180.00 USD |
| `7D` | `671.90` | 27,970,000.00 USD | 0.00 USD | 27,970,000.00 USD | 255,560.00 USD | 26,430.00 USD | 684,860.00 USD |
| `1D` | `672.50` | 30,400,000.00 USD | 0.00 USD | 30,400,000.00 USD | 131,990.00 USD | 8,980.00 USD | 713,630.00 USD |
| `7D` | `672.90` | 27,000,000.00 USD | 0.00 USD | 27,000,000.00 USD | 1,010,000.00 USD | 159,740.00 USD | 31,670.00 USD |
| `1D` | `673.30` | 29,540,000.00 USD | 0.00 USD | 29,540,000.00 USD | 72,040.00 USD | 336,780.00 USD | 1,730,000.00 USD |
| `7D` | `673.90` | 25,800,000.00 USD | 0.00 USD | 25,800,000.00 USD | 335,670.00 USD | 268,790.00 USD | 60,640.00 USD |
| `1D` | `674.10` | 27,400,000.00 USD | 0.00 USD | 27,400,000.00 USD | 272,200.00 USD | 232,500.00 USD | 225,530.00 USD |
| `1D` | `674.90` | 26,670,000.00 USD | 0.00 USD | 26,670,000.00 USD | 1,340,000.00 USD | 290,890.00 USD | 512,050.00 USD |
| `7D` | `674.90` | 25,130,000.00 USD | 0.00 USD | 25,130,000.00 USD | 143,690.00 USD | 129,800.00 USD | 860,540.00 USD |
| `1D` | `675.70` | 24,530,000.00 USD | 0.00 USD | 24,530,000.00 USD | 1,660,000.00 USD | 193,370.00 USD | 271,520.00 USD |
| `7D` | `675.90` | 24,000,000.00 USD | 0.00 USD | 24,000,000.00 USD | 394,120.00 USD | 131,610.00 USD | 1,840,000.00 USD |
| `1D` | `676.50` | 22,400,000.00 USD | 0.00 USD | 22,400,000.00 USD | 248,760.00 USD | 334,230.00 USD | 439,290.00 USD |
| `7D` | `676.90` | 21,640,000.00 USD | 0.00 USD | 21,640,000.00 USD | 2,140,000.00 USD | 428,700.00 USD | 502,410.00 USD |
| `1D` | `677.30` | 21,380,000.00 USD | 0.00 USD | 21,380,000.00 USD | 198,850.00 USD | 58,150.00 USD | 217,990.00 USD |
| `7D` | `677.90` | 18,560,000.00 USD | 0.00 USD | 18,560,000.00 USD | 752,200.00 USD | 28,030.00 USD | 484,840.00 USD |
| `1D` | `678.10` | 20,900,000.00 USD | 0.00 USD | 20,900,000.00 USD | 609,730.00 USD | 168,340.00 USD | 286,140.00 USD |
| `1D` | `678.90` | 19,840,000.00 USD | 0.00 USD | 19,840,000.00 USD | 1,250,000.00 USD | 182,260.00 USD | 106,140.00 USD |
| `7D` | `678.90` | 17,300,000.00 USD | 0.00 USD | 17,300,000.00 USD | 244,010.00 USD | 98,010.00 USD | 43,880.00 USD |
| `1D` | `679.70` | 18,300,000.00 USD | 0.00 USD | 18,300,000.00 USD | 1,610,000.00 USD | 227,550.00 USD | 307,330.00 USD |
| `7D` | `679.90` | 16,910,000.00 USD | 0.00 USD | 16,910,000.00 USD | 89,860.00 USD | 65,770.00 USD | 321,910.00 USD |
| `1D` | `680.50` | 16,160,000.00 USD | 0.00 USD | 16,160,000.00 USD | 60,980.00 USD | 59,290.00 USD | 143,090.00 USD |
| `7D` | `680.90` | 16,430,000.00 USD | 0.00 USD | 16,430,000.00 USD | 10,590.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `681.30` | 15,890,000.00 USD | 0.00 USD | 15,890,000.00 USD | 602,640.00 USD | 508,720.00 USD | 44,240.00 USD |
| `7D` | `681.90` | 16,190,000.00 USD | 0.00 USD | 16,190,000.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `682.10` | 14,740,000.00 USD | 0.00 USD | 14,740,000.00 USD | 399,330.00 USD | 16,030.00 USD | 0.00 USD |
| `1D` | `682.90` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 690,810.00 USD | 59,430.00 USD | 0.00 USD |
| `7D` | `682.90` | 14,430,000.00 USD | 0.00 USD | 14,430,000.00 USD | 39,810.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `683.70` | 13,570,000.00 USD | 0.00 USD | 13,570,000.00 USD | 392,840.00 USD | 0.00 USD | 88,870.00 USD |
| `7D` | `683.90` | 14,390,000.00 USD | 0.00 USD | 14,390,000.00 USD | 77,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `684.50` | 13,090,000.00 USD | 0.00 USD | 13,090,000.00 USD | 151,300.00 USD | 21,510.00 USD | 0.00 USD |
| `7D` | `684.90` | 14,320,000.00 USD | 0.00 USD | 14,320,000.00 USD | 1,490,000.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `685.30` | 12,920,000.00 USD | 0.00 USD | 12,920,000.00 USD | 406,260.00 USD | 37,140.00 USD | 0.00 USD |
| `7D` | `685.90` | 12,710,000.00 USD | 0.00 USD | 12,710,000.00 USD | 122,630.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.10` | 12,480,000.00 USD | 0.00 USD | 12,480,000.00 USD | 1,120,000.00 USD | 48,550.00 USD | 44,130.00 USD |
| `1D` | `686.90` | 11,260,000.00 USD | 0.00 USD | 11,260,000.00 USD | 186,390.00 USD | 211,140.00 USD | 187,960.00 USD |
| `7D` | `686.90` | 12,590,000.00 USD | 0.00 USD | 12,590,000.00 USD | 53,070.00 USD | 71,560.00 USD | 0.00 USD |
| `1D` | `687.70` | 10,680,000.00 USD | 0.00 USD | 10,680,000.00 USD | 1,190,000.00 USD | 166,060.00 USD | 315,530.00 USD |
| `7D` | `687.90` | 12,460,000.00 USD | 0.00 USD | 12,460,000.00 USD | 142,930.00 USD | 504,150.00 USD | 0.00 USD |
| `1D` | `688.50` | 9,000,000.00 USD | 0.00 USD | 9,000,000.00 USD | 530,770.00 USD | 140,450.00 USD | 829,650.00 USD |
| `7D` | `688.90` | 11,820,000.00 USD | 0.00 USD | 11,820,000.00 USD | 70,480.00 USD | 253,790.00 USD | 1,940,000.00 USD |
| `1D` | `689.30` | 7,500,000.00 USD | 0.00 USD | 7,500,000.00 USD | 532,160.00 USD | 87,180.00 USD | 1,140,000.00 USD |
| `7D` | `689.90` | 9,550,000.00 USD | 0.00 USD | 9,550,000.00 USD | 170,280.00 USD | 0.00 USD | 1,040,000.00 USD |
| `1D` | `690.10` | 5,750,000.00 USD | 0.00 USD | 5,750,000.00 USD | 502,870.00 USD | 29,070.00 USD | 264,670.00 USD |
| `1D` | `690.90` | 4,950,000.00 USD | 0.00 USD | 4,950,000.00 USD | 115,540.00 USD | 199,550.00 USD | 307,460.00 USD |
| `7D` | `690.90` | 8,340,000.00 USD | 0.00 USD | 8,340,000.00 USD | 109,680.00 USD | 186,610.00 USD | 0.00 USD |
| `1D` | `691.70` | 4,330,000.00 USD | 0.00 USD | 4,330,000.00 USD | 184,180.00 USD | 71,280.00 USD | 104,480.00 USD |
| `7D` | `691.90` | 8,050,000.00 USD | 0.00 USD | 8,050,000.00 USD | 67,140.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `692.50` | 3,970,000.00 USD | 0.00 USD | 3,970,000.00 USD | 673,080.00 USD | 46,300.00 USD | 69,760.00 USD |
| `7D` | `692.90` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 803,940.00 USD | 252,070.00 USD | 87,760.00 USD |
| `1D` | `693.30` | 3,180,000.00 USD | 0.00 USD | 3,180,000.00 USD | 74,030.00 USD | 162,210.00 USD | 69,370.00 USD |
| `7D` | `693.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 0.00 USD | 131,550.00 USD | 317,780.00 USD |
| `1D` | `694.10` | 2,870,000.00 USD | 0.00 USD | 2,870,000.00 USD | 246,300.00 USD | 177,770.00 USD | 363,740.00 USD |
| `1D` | `694.90` | 2,080,000.00 USD | 0.00 USD | 2,080,000.00 USD | 306,060.00 USD | 64,240.00 USD | 264,840.00 USD |
| `7D` | `694.90` | 4,320,000.00 USD | 0.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 661,790.00 USD |
| `1D` | `695.70` | 1,450,000.00 USD | 0.00 USD | 1,450,000.00 USD | 153,900.00 USD | 34,140.00 USD | 0.00 USD |
| `7D` | `695.90` | 3,660,000.00 USD | 0.00 USD | 3,660,000.00 USD | 0.00 USD | 128,880.00 USD | 0.00 USD |
| `1D` | `696.50` | 1,260,000.00 USD | 0.00 USD | 1,260,000.00 USD | 0.00 USD | 32,060.00 USD | 0.00 USD |
| `1D` | `697.30` | 1,230,000.00 USD | 0.00 USD | 1,230,000.00 USD | 0.00 USD | 63,720.00 USD | 0.00 USD |
| `1D` | `698.10` | 1,170,000.00 USD | 0.00 USD | 1,170,000.00 USD | 203,360.00 USD | 0.00 USD | 24,380.00 USD |
| `1D` | `698.90` | 937,420.00 USD | 0.00 USD | 937,420.00 USD | 276,500.00 USD | 31,670.00 USD | 42,650.00 USD |
| `7D` | `698.90` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 575,930.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `699.70` | 586,600.00 USD | 0.00 USD | 586,600.00 USD | 134,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `700.50` | 452,600.00 USD | 0.00 USD | 452,600.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `700.90` | 2,960,000.00 USD | 0.00 USD | 2,960,000.00 USD | 0.00 USD | 72,960.00 USD | 0.00 USD |
| `7D` | `701.90` | 2,880,000.00 USD | 0.00 USD | 2,880,000.00 USD | 0.00 USD | 190,950.00 USD | 0.00 USD |
| `1D` | `702.10` | 262,480.00 USD | 0.00 USD | 262,480.00 USD | 227,540.00 USD | 34,930.00 USD | 0.00 USD |
| `7D` | `702.90` | 2,690,000.00 USD | 0.00 USD | 2,690,000.00 USD | 0.00 USD | 114,370.00 USD | 0.00 USD |
| `1D` | `703.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `703.90` | 2,580,000.00 USD | 0.00 USD | 2,580,000.00 USD | 0.00 USD | 0.00 USD | 1,030,000.00 USD |
| `7D` | `704.90` | 1,550,000.00 USD | 0.00 USD | 1,550,000.00 USD | 1,550,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `705.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `706.10` | 121,180.00 USD | 121,180.00 USD | 0.00 USD | 121,180.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.90` | 677,910.00 USD | 677,910.00 USD | 0.00 USD | 677,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `710.90` | 502,620.00 USD | 502,620.00 USD | 0.00 USD | 343,540.00 USD | 0.00 USD | 37,900.00 USD |
| `1D` | `711.70` | 850,080.00 USD | 850,080.00 USD | 0.00 USD | 308,680.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `712.90` | 794,220.00 USD | 794,220.00 USD | 0.00 USD | 0.00 USD | 116,310.00 USD | 0.00 USD |
| `1D` | `714.10` | 894,210.00 USD | 894,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 44,130.00 USD |
| `1D` | `714.90` | 1,460,000.00 USD | 1,460,000.00 USD | 0.00 USD | 0.00 USD | 63,380.00 USD | 504,550.00 USD |
| `1D` | `715.70` | 2,750,000.00 USD | 2,750,000.00 USD | 0.00 USD | 181,810.00 USD | 64,780.00 USD | 1,040,000.00 USD |
| `1D` | `716.50` | 3,050,000.00 USD | 3,050,000.00 USD | 0.00 USD | 51,080.00 USD | 24,200.00 USD | 225,540.00 USD |
| `1D` | `717.30` | 3,690,000.00 USD | 3,690,000.00 USD | 0.00 USD | 273,400.00 USD | 24,690.00 USD | 338,540.00 USD |
| `1D` | `718.10` | 4,510,000.00 USD | 4,510,000.00 USD | 0.00 USD | 673,150.00 USD | 20,360.00 USD | 124,850.00 USD |
| `1D` | `718.90` | 5,080,000.00 USD | 5,080,000.00 USD | 0.00 USD | 115,540.00 USD | 117,390.00 USD | 341,270.00 USD |
| `7D` | `718.90` | 1,570,000.00 USD | 1,570,000.00 USD | 0.00 USD | 775,390.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `719.70` | 5,270,000.00 USD | 5,270,000.00 USD | 0.00 USD | 60,590.00 USD | 71,280.00 USD | 52,930.00 USD |
| `7D` | `719.90` | 3,630,000.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 256,450.00 USD | 1,810,000.00 USD |
| `1D` | `720.50` | 6,390,000.00 USD | 6,390,000.00 USD | 0.00 USD | 988,460.00 USD | 31,410.00 USD | 102,980.00 USD |
| `7D` | `720.90` | 4,670,000.00 USD | 4,670,000.00 USD | 0.00 USD | 803,940.00 USD | 146,010.00 USD | 87,760.00 USD |
| `1D` | `721.30` | 7,140,000.00 USD | 7,140,000.00 USD | 0.00 USD | 177,520.00 USD | 443,160.00 USD | 127,300.00 USD |
| `7D` | `721.90` | 5,090,000.00 USD | 5,090,000.00 USD | 0.00 USD | 0.00 USD | 106,060.00 USD | 317,780.00 USD |
| `1D` | `722.10` | 7,910,000.00 USD | 7,910,000.00 USD | 0.00 USD | 348,340.00 USD | 110,100.00 USD | 319,170.00 USD |
| `1D` | `722.90` | 8,500,000.00 USD | 8,500,000.00 USD | 0.00 USD | 191,050.00 USD | 130,270.00 USD | 266,900.00 USD |
| `7D` | `722.90` | 5,550,000.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 131,550.00 USD | 326,040.00 USD |
| `1D` | `723.70` | 9,550,000.00 USD | 9,550,000.00 USD | 0.00 USD | 446,650.00 USD | 508,710.00 USD | 88,480.00 USD |
| `7D` | `723.90` | 6,820,000.00 USD | 6,820,000.00 USD | 0.00 USD | 806,150.00 USD | 128,880.00 USD | 335,740.00 USD |
| `1D` | `724.50` | 9,950,000.00 USD | 9,950,000.00 USD | 0.00 USD | 327,200.00 USD | 79,990.00 USD | 0.00 USD |
| `1D` | `725.30` | 10,420,000.00 USD | 10,420,000.00 USD | 0.00 USD | 321,800.00 USD | 120,790.00 USD | 18,950.00 USD |
| `7D` | `725.90` | 7,950,000.00 USD | 7,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 1,120,000.00 USD |
| `1D` | `726.10` | 10,640,000.00 USD | 10,640,000.00 USD | 0.00 USD | 192,360.00 USD | 10,760.00 USD | 19,390.00 USD |
| `1D` | `726.90` | 11,240,000.00 USD | 11,240,000.00 USD | 0.00 USD | 502,670.00 USD | 75,120.00 USD | 24,380.00 USD |
| `7D` | `726.90` | 8,560,000.00 USD | 8,560,000.00 USD | 0.00 USD | 552,080.00 USD | 58,160.00 USD | 0.00 USD |
| `1D` | `727.70` | 11,630,000.00 USD | 11,630,000.00 USD | 0.00 USD | 339,770.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `727.90` | 9,970,000.00 USD | 9,970,000.00 USD | 0.00 USD | 575,930.00 USD | 201,080.00 USD | 639,380.00 USD |
| `1D` | `728.50` | 11,860,000.00 USD | 11,860,000.00 USD | 0.00 USD | 157,160.00 USD | 5,290.00 USD | 71,460.00 USD |
| `7D` | `728.90` | 11,450,000.00 USD | 11,450,000.00 USD | 0.00 USD | 1,360,000.00 USD | 125,070.00 USD | 0.00 USD |
| `1D` | `729.30` | 13,320,000.00 USD | 13,320,000.00 USD | 0.00 USD | 359,560.00 USD | 374,970.00 USD | 724,100.00 USD |
| `7D` | `729.90` | 11,820,000.00 USD | 11,820,000.00 USD | 0.00 USD | 0.00 USD | 365,010.00 USD | 0.00 USD |
| `1D` | `730.10` | 15,740,000.00 USD | 15,740,000.00 USD | 0.00 USD | 2,020,000.00 USD | 333,240.00 USD | 73,220.00 USD |
| `1D` | `730.90` | 19,750,000.00 USD | 19,750,000.00 USD | 0.00 USD | 1,460,000.00 USD | 315,090.00 USD | 2,240,000.00 USD |
| `7D` | `730.90` | 12,480,000.00 USD | 12,480,000.00 USD | 0.00 USD | 127,820.00 USD | 219,090.00 USD | 313,360.00 USD |
| `1D` | `731.70` | 21,290,000.00 USD | 21,290,000.00 USD | 0.00 USD | 654,700.00 USD | 170,350.00 USD | 714,880.00 USD |
| `7D` | `731.90` | 14,180,000.00 USD | 14,180,000.00 USD | 0.00 USD | 0.00 USD | 114,370.00 USD | 1,580,000.00 USD |
| `1D` | `732.50` | 23,980,000.00 USD | 23,980,000.00 USD | 0.00 USD | 1,100,000.00 USD | 113,600.00 USD | 1,470,000.00 USD |
| `7D` | `732.90` | 14,630,000.00 USD | 14,630,000.00 USD | 0.00 USD | 0.00 USD | 93,300.00 USD | 363,490.00 USD |
| `1D` | `733.30` | 25,510,000.00 USD | 25,510,000.00 USD | 0.00 USD | 866,380.00 USD | 184,030.00 USD | 484,920.00 USD |
| `7D` | `733.90` | 15,790,000.00 USD | 15,790,000.00 USD | 0.00 USD | 123,040.00 USD | 128,230.00 USD | 903,260.00 USD |
| `1D` | `734.10` | 26,400,000.00 USD | 26,400,000.00 USD | 0.00 USD | 477,580.00 USD | 204,160.00 USD | 201,750.00 USD |
| `1D` | `734.90` | 27,480,000.00 USD | 27,480,000.00 USD | 0.00 USD | 893,060.00 USD | 167,830.00 USD | 18,290.00 USD |
| `7D` | `734.90` | 16,320,000.00 USD | 16,320,000.00 USD | 0.00 USD | 456,850.00 USD | 73,000.00 USD | 0.00 USD |
| `1D` | `735.70` | 28,610,000.00 USD | 28,610,000.00 USD | 0.00 USD | 405,830.00 USD | 101,320.00 USD | 625,610.00 USD |
| `7D` | `735.90` | 16,660,000.00 USD | 16,660,000.00 USD | 0.00 USD | 90,800.00 USD | 53,030.00 USD | 202,770.00 USD |
| `1D` | `736.50` | 29,270,000.00 USD | 29,270,000.00 USD | 0.00 USD | 389,130.00 USD | 88,890.00 USD | 181,870.00 USD |
| `7D` | `736.90` | 17,070,000.00 USD | 17,070,000.00 USD | 0.00 USD | 176,450.00 USD | 65,770.00 USD | 163,020.00 USD |
| `1D` | `737.30` | 29,530,000.00 USD | 29,530,000.00 USD | 0.00 USD | 145,170.00 USD | 32,120.00 USD | 88,180.00 USD |
| `7D` | `737.90` | 17,300,000.00 USD | 17,300,000.00 USD | 0.00 USD | 0.00 USD | 64,440.00 USD | 167,870.00 USD |
| `1D` | `738.10` | 30,100,000.00 USD | 30,100,000.00 USD | 0.00 USD | 338,980.00 USD | 179,820.00 USD | 44,240.00 USD |
| `1D` | `738.90` | 31,650,000.00 USD | 31,650,000.00 USD | 0.00 USD | 603,470.00 USD | 16,030.00 USD | 934,700.00 USD |
| `7D` | `738.90` | 18,170,000.00 USD | 18,170,000.00 USD | 0.00 USD | 0.00 USD | 166,070.00 USD | 703,580.00 USD |
| `1D` | `739.70` | 31,900,000.00 USD | 31,900,000.00 USD | 0.00 USD | 222,140.00 USD | 31,860.00 USD | 0.00 USD |
| `7D` | `739.90` | 19,980,000.00 USD | 19,980,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 626,320.00 USD |
| `1D` | `740.50` | 32,270,000.00 USD | 32,270,000.00 USD | 0.00 USD | 228,370.00 USD | 134,150.00 USD | 0.00 USD |
| `7D` | `740.90` | 21,190,000.00 USD | 21,190,000.00 USD | 0.00 USD | 1,180,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.30` | 32,680,000.00 USD | 32,680,000.00 USD | 0.00 USD | 366,560.00 USD | 32,240.00 USD | 12,190.00 USD |
| `7D` | `741.90` | 21,810,000.00 USD | 21,810,000.00 USD | 0.00 USD | 287,970.00 USD | 100,540.00 USD | 230,050.00 USD |
| `1D` | `742.10` | 33,010,000.00 USD | 33,010,000.00 USD | 0.00 USD | 318,870.00 USD | 15,840.00 USD | 0.00 USD |
| `1D` | `742.90` | 33,250,000.00 USD | 33,250,000.00 USD | 0.00 USD | 233,800.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `742.90` | 22,460,000.00 USD | 22,460,000.00 USD | 0.00 USD | 485,340.00 USD | 0.00 USD | 162,460.00 USD |
| `1D` | `743.70` | 33,820,000.00 USD | 33,820,000.00 USD | 0.00 USD | 112,430.00 USD | 21,120.00 USD | 436,560.00 USD |
| `7D` | `743.90` | 23,010,000.00 USD | 23,010,000.00 USD | 0.00 USD | 160,880.00 USD | 194,060.00 USD | 199,370.00 USD |
| `1D` | `744.50` | 34,970,000.00 USD | 34,970,000.00 USD | 0.00 USD | 913,440.00 USD | 236,000.00 USD | 0.00 USD |
| `7D` | `744.90` | 23,260,000.00 USD | 23,260,000.00 USD | 0.00 USD | 0.00 USD | 244,460.00 USD | 0.00 USD |
| `1D` | `745.30` | 36,620,000.00 USD | 36,620,000.00 USD | 0.00 USD | 700,970.00 USD | 31,390.00 USD | 923,500.00 USD |
| `7D` | `745.90` | 23,710,000.00 USD | 23,710,000.00 USD | 0.00 USD | 396,930.00 USD | 57,190.00 USD | 0.00 USD |
| `1D` | `746.10` | 37,470,000.00 USD | 37,470,000.00 USD | 0.00 USD | 567,430.00 USD | 135,740.00 USD | 149,390.00 USD |
| `1D` | `746.90` | 38,740,000.00 USD | 38,740,000.00 USD | 0.00 USD | 291,780.00 USD | 37,280.00 USD | 939,640.00 USD |
| `7D` | `746.90` | 24,980,000.00 USD | 24,980,000.00 USD | 0.00 USD | 324,750.00 USD | 0.00 USD | 948,960.00 USD |
| `1D` | `747.70` | 39,300,000.00 USD | 39,300,000.00 USD | 0.00 USD | 419,020.00 USD | 37,100.00 USD | 98,540.00 USD |
| `1D` | `748.50` | 39,860,000.00 USD | 39,860,000.00 USD | 0.00 USD | 390,720.00 USD | 84,260.00 USD | 91,200.00 USD |
| `7D` | `748.90` | 25,380,000.00 USD | 25,380,000.00 USD | 0.00 USD | 337,680.00 USD | 61,650.00 USD | 0.00 USD |
| `1D` | `749.30` | 40,160,000.00 USD | 40,160,000.00 USD | 0.00 USD | 300,470.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `749.90` | 25,790,000.00 USD | 25,790,000.00 USD | 0.00 USD | 404,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.10` | 40,430,000.00 USD | 40,430,000.00 USD | 0.00 USD | 269,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.90` | 40,510,000.00 USD | 40,510,000.00 USD | 0.00 USD | 79,400.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `750.90` | 25,860,000.00 USD | 25,860,000.00 USD | 0.00 USD | 70,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.70` | 41,040,000.00 USD | 41,040,000.00 USD | 0.00 USD | 112,060.00 USD | 25,010.00 USD | 393,600.00 USD |
| `7D` | `751.90` | 25,960,000.00 USD | 25,960,000.00 USD | 0.00 USD | 105,420.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `752.50` | 41,530,000.00 USD | 41,530,000.00 USD | 0.00 USD | 336,940.00 USD | 0.00 USD | 146,020.00 USD |
| `7D` | `752.90` | 26,320,000.00 USD | 26,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 351,790.00 USD |
| `1D` | `753.30` | 41,920,000.00 USD | 41,920,000.00 USD | 0.00 USD | 139,220.00 USD | 3,810.00 USD | 248,870.00 USD |
| `7D` | `753.90` | 26,840,000.00 USD | 26,840,000.00 USD | 0.00 USD | 406,900.00 USD | 83,030.00 USD | 33,430.00 USD |
| `1D` | `754.10` | 42,390,000.00 USD | 42,390,000.00 USD | 0.00 USD | 363,270.00 USD | 50,610.00 USD | 57,280.00 USD |
| `1D` | `754.90` | 42,850,000.00 USD | 42,850,000.00 USD | 0.00 USD | 277,270.00 USD | 142,490.00 USD | 37,120.00 USD |
| `7D` | `754.90` | 26,900,000.00 USD | 26,900,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.70` | 43,210,000.00 USD | 43,210,000.00 USD | 0.00 USD | 250,440.00 USD | 96,170.00 USD | 19,780.00 USD |
| `7D` | `755.90` | 27,020,000.00 USD | 27,020,000.00 USD | 0.00 USD | 120,600.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `756.50` | 43,390,000.00 USD | 43,390,000.00 USD | 0.00 USD | 100,220.00 USD | 24,970.00 USD | 54,690.00 USD |
| `7D` | `756.90` | 27,180,000.00 USD | 27,180,000.00 USD | 0.00 USD | 0.00 USD | 160,580.00 USD | 0.00 USD |
| `1D` | `757.30` | 43,730,000.00 USD | 43,730,000.00 USD | 0.00 USD | 155,490.00 USD | 103,180.00 USD | 73,520.00 USD |
| `7D` | `757.90` | 27,660,000.00 USD | 27,660,000.00 USD | 0.00 USD | 475,510.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `758.10` | 44,670,000.00 USD | 44,670,000.00 USD | 0.00 USD | 656,280.00 USD | 72,680.00 USD | 218,280.00 USD |
| `1D` | `758.90` | 45,030,000.00 USD | 45,030,000.00 USD | 0.00 USD | 162,660.00 USD | 137,350.00 USD | 54,810.00 USD |
| `7D` | `758.90` | 29,160,000.00 USD | 29,160,000.00 USD | 0.00 USD | 1,190,000.00 USD | 55,460.00 USD | 265,620.00 USD |
| `1D` | `759.70` | 45,450,000.00 USD | 45,450,000.00 USD | 0.00 USD | 397,100.00 USD | 21,070.00 USD | 8,370.00 USD |
| `7D` | `759.90` | 29,520,000.00 USD | 29,520,000.00 USD | 0.00 USD | 310,160.00 USD | 0.00 USD | 42,540.00 USD |
| `1D` | `760.50` | 45,810,000.00 USD | 45,810,000.00 USD | 0.00 USD | 274,870.00 USD | 37,300.00 USD | 42,940.00 USD |
| `7D` | `760.90` | 29,870,000.00 USD | 29,870,000.00 USD | 0.00 USD | 264,540.00 USD | 27,650.00 USD | 61,350.00 USD |
| `1D` | `761.30` | 46,830,000.00 USD | 46,830,000.00 USD | 0.00 USD | 756,450.00 USD | 24,020.00 USD | 235,550.00 USD |
| `7D` | `761.90` | 30,490,000.00 USD | 30,490,000.00 USD | 0.00 USD | 46,720.00 USD | 282,090.00 USD | 288,600.00 USD |
| `1D` | `762.10` | 46,960,000.00 USD | 46,960,000.00 USD | 0.00 USD | 65,550.00 USD | 42,210.00 USD | 26,330.00 USD |
| `1D` | `762.90` | 47,760,000.00 USD | 47,760,000.00 USD | 0.00 USD | 392,000.00 USD | 61,680.00 USD | 351,620.00 USD |
| `7D` | `762.90` | 32,530,000.00 USD | 32,530,000.00 USD | 0.00 USD | 1,290,000.00 USD | 427,600.00 USD | 324,830.00 USD |
| `1D` | `763.70` | 48,190,000.00 USD | 48,190,000.00 USD | 0.00 USD | 370,320.00 USD | 42,990.00 USD | 9,330.00 USD |
| `7D` | `763.90` | 35,570,000.00 USD | 35,570,000.00 USD | 0.00 USD | 2,260,000.00 USD | 329,860.00 USD | 450,710.00 USD |
| `1D` | `764.50` | 48,380,000.00 USD | 48,380,000.00 USD | 0.00 USD | 137,070.00 USD | 15,480.00 USD | 40,840.00 USD |
| `7D` | `764.90` | 37,480,000.00 USD | 37,480,000.00 USD | 0.00 USD | 1,250,000.00 USD | 308,520.00 USD | 346,190.00 USD |
| `1D` | `765.30` | 48,650,000.00 USD | 48,650,000.00 USD | 0.00 USD | 115,580.00 USD | 117,270.00 USD | 32,870.00 USD |
| `7D` | `765.90` | 40,850,000.00 USD | 40,850,000.00 USD | 0.00 USD | 2,560,000.00 USD | 228,800.00 USD | 585,320.00 USD |
| `1D` | `766.10` | 49,220,000.00 USD | 49,220,000.00 USD | 0.00 USD | 451,950.00 USD | 35,470.00 USD | 90,350.00 USD |
| `1D` | `766.90` | 49,540,000.00 USD | 49,540,000.00 USD | 0.00 USD | 211,510.00 USD | 12,510.00 USD | 94,800.00 USD |
| `7D` | `766.90` | 45,470,000.00 USD | 45,470,000.00 USD | 0.00 USD | 3,530,000.00 USD | 285,740.00 USD | 801,480.00 USD |
| `1D` | `767.70` | 50,340,000.00 USD | 50,340,000.00 USD | 0.00 USD | 734,810.00 USD | 14,040.00 USD | 44,130.00 USD |
| `7D` | `767.90` | 49,710,000.00 USD | 49,710,000.00 USD | 0.00 USD | 3,510,000.00 USD | 173,810.00 USD | 557,450.00 USD |
| `1D` | `768.50` | 50,380,000.00 USD | 50,380,000.00 USD | 0.00 USD | 9,780.00 USD | 15,850.00 USD | 20,190.00 USD |
| `7D` | `768.90` | 51,290,000.00 USD | 51,290,000.00 USD | 0.00 USD | 1,050,000.00 USD | 92,840.00 USD | 436,370.00 USD |
| `1D` | `769.30` | 50,580,000.00 USD | 50,580,000.00 USD | 0.00 USD | 164,570.00 USD | 28,060.00 USD | 8,460.00 USD |
| `7D` | `769.90` | 53,330,000.00 USD | 53,330,000.00 USD | 0.00 USD | 1,240,000.00 USD | 322,290.00 USD | 486,170.00 USD |
| `1D` | `770.10` | 50,880,000.00 USD | 50,880,000.00 USD | 0.00 USD | 203,040.00 USD | 70,230.00 USD | 28,450.00 USD |
| `1D` | `770.90` | 51,280,000.00 USD | 51,280,000.00 USD | 0.00 USD | 4,860.00 USD | 33,850.00 USD | 361,060.00 USD |
| `7D` | `770.90` | 55,620,000.00 USD | 55,620,000.00 USD | 0.00 USD | 1,860,000.00 USD | 259,380.00 USD | 170,990.00 USD |
| `1D` | `771.70` | 52,070,000.00 USD | 52,070,000.00 USD | 0.00 USD | 82,150.00 USD | 96,870.00 USD | 607,180.00 USD |
| `7D` | `771.90` | 58,460,000.00 USD | 58,460,000.00 USD | 0.00 USD | 2,000,000.00 USD | 431,660.00 USD | 411,300.00 USD |
| `1D` | `772.50` | 52,500,000.00 USD | 52,500,000.00 USD | 0.00 USD | 243,310.00 USD | 133,890.00 USD | 48,490.00 USD |
| `7D` | `772.90` | 61,480,000.00 USD | 61,480,000.00 USD | 0.00 USD | 2,310,000.00 USD | 316,340.00 USD | 397,820.00 USD |
| `1D` | `773.30` | 53,380,000.00 USD | 53,380,000.00 USD | 0.00 USD | 745,520.00 USD | 23,860.00 USD | 111,430.00 USD |
| `7D` | `773.90` | 63,280,000.00 USD | 63,280,000.00 USD | 0.00 USD | 1,220,000.00 USD | 270,430.00 USD | 304,680.00 USD |
| `1D` | `774.10` | 53,560,000.00 USD | 53,560,000.00 USD | 0.00 USD | 130,070.00 USD | 26,310.00 USD | 28,310.00 USD |
| `1D` | `774.90` | 53,960,000.00 USD | 53,960,000.00 USD | 0.00 USD | 249,450.00 USD | 41,190.00 USD | 107,850.00 USD |
| `7D` | `774.90` | 65,430,000.00 USD | 65,430,000.00 USD | 0.00 USD | 1,140,000.00 USD | 515,010.00 USD | 490,500.00 USD |
| `1D` | `775.70` | 54,190,000.00 USD | 54,190,000.00 USD | 0.00 USD | 130,910.00 USD | 24,070.00 USD | 76,830.00 USD |
| `7D` | `775.90` | 67,690,000.00 USD | 67,690,000.00 USD | 0.00 USD | 1,670,000.00 USD | 274,120.00 USD | 316,370.00 USD |
| `1D` | `776.50` | 54,420,000.00 USD | 54,420,000.00 USD | 0.00 USD | 149,370.00 USD | 13,880.00 USD | 65,600.00 USD |
| `7D` | `776.90` | 69,280,000.00 USD | 69,280,000.00 USD | 0.00 USD | 1,370,000.00 USD | 106,550.00 USD | 115,990.00 USD |
| `1D` | `777.30` | 54,620,000.00 USD | 54,620,000.00 USD | 0.00 USD | 181,420.00 USD | 11,790.00 USD | 5,680.00 USD |
| `7D` | `777.90` | 71,190,000.00 USD | 71,190,000.00 USD | 0.00 USD | 1,470,000.00 USD | 240,260.00 USD | 196,170.00 USD |
| `7D` | `778.90` | 72,450,000.00 USD | 72,450,000.00 USD | 0.00 USD | 994,320.00 USD | 117,290.00 USD | 152,370.00 USD |
| `7D` | `779.90` | 73,470,000.00 USD | 73,470,000.00 USD | 0.00 USD | 758,640.00 USD | 125,670.00 USD | 135,630.00 USD |
| `7D` | `780.90` | 75,020,000.00 USD | 75,020,000.00 USD | 0.00 USD | 1,220,000.00 USD | 93,770.00 USD | 240,340.00 USD |
| `7D` | `781.90` | 77,320,000.00 USD | 77,320,000.00 USD | 0.00 USD | 1,790,000.00 USD | 118,390.00 USD | 386,440.00 USD |
| `7D` | `782.90` | 79,620,000.00 USD | 79,620,000.00 USD | 0.00 USD | 1,840,000.00 USD | 36,140.00 USD | 427,460.00 USD |
| `7D` | `783.90` | 80,120,000.00 USD | 80,120,000.00 USD | 0.00 USD | 437,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `7D` | `784.90` | 80,720,000.00 USD | 80,720,000.00 USD | 0.00 USD | 424,680.00 USD | 81,720.00 USD | 92,590.00 USD |
| `7D` | `785.90` | 81,760,000.00 USD | 81,760,000.00 USD | 0.00 USD | 932,150.00 USD | 60,930.00 USD | 48,900.00 USD |
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
  * Total Open Interest: `1.29B` | Total OI Tokens: `1,838,938.7 BNB`
  * 1h OI Change: `+0.20%` | 4h OI Change: `-2.11%` | 24h OI Change: `+3.16%`
  * Exchange Breakdown: Binance=`563.81M` | Bybit=`139.73M` | OKX=`65.17M` | Hyperliquid=`67.96M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-117.58K` | Last 24h: `-160.49K` | Last 3d: `35.49K` | Last 7d: `220.92K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0327%` |
| **USDT Bybit** | `-0.0690%` | **USDT KuCoin** | `-0.0161%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `0.0070%` | **USDT Bitget** | `-0.0169%` |
| **CoinM Binance** | `0.0060%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `47.37%` | `52.63%` | `0.90` | 32,610,000.00 USD |
| `15M` | `Binance` | `47.71%` | `52.29%` | `0.91` | 10,690,000.00 USD |
| `15M` | `OKX` | `48.81%` | `51.19%` | `0.95` | 3,770,000.00 USD |
| `15M` | `Bybit` | `54.01%` | `45.99%` | `1.17` | 3,870,000.00 USD |
| `15M` | `KuCoin` | `53.9%` | `46.1%` | `1.17` | 872,710.00 USD |
| `15M` | `Gate` | `52.26%` | `47.74%` | `1.09` | 1,490,000.00 USD |
| `15M` | `Bitget` | `65.17%` | `34.83%` | `1.87` | 2,330,000.00 USD |
| `15M` | `BingX` | `45.33%` | `54.67%` | `0.83` | 366,790.00 USD |
| `15M` | `MEXC` | `38.06%` | `61.94%` | `0.61` | 4,100,000.00 USD |
| `15M` | `Bitunix` | `59.76%` | `40.24%` | `1.49` | 1,260,000.00 USD |
| `15M` | `Hyperliquid` | `74.78%` | `25.22%` | `2.97` | 1,020,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `65.82%` | `34.18%` | `1.93` | 130,150.00 USD |
| `15M` | `Crypto.com` | `55.88%` | `44.12%` | `1.27` | 39,540.00 USD |
| `15M` | `WhiteBIT` | `0.13%` | `99.87%` | `0.00` | 2,040,000.00 USD |
| `15M` | `HTX` | `56.09%` | `43.91%` | `1.28` | 12,450.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `45.6%` | `54.4%` | `0.84` | 357,380.00 USD |
| `15M` | `Aster` | `50.18%` | `49.82%` | `1.01` | 171,750.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `47.49%` | `52.51%` | `0.90` | 84,940.00 USD |
| `15M` | `Whale Positions` | `47.71%` | `52.29%` | `0.91` | 10,690,000.00 USD |
| `15M` | `Global Accounts` | `47.37%` | `52.63%` | `0.90` | 32,610,000.00 USD |
| `1H` | `BNB` | `41.01%` | `58.99%` | `0.70` | 108,580,000.00 USD |
| `1H` | `Binance` | `45.77%` | `54.23%` | `0.84` | 31,000,000.00 USD |
| `1H` | `OKX` | `39.93%` | `60.07%` | `0.66` | 9,810,000.00 USD |
| `1H` | `Bybit` | `28.75%` | `71.25%` | `0.40` | 16,150,000.00 USD |
| `1H` | `KuCoin` | `43.62%` | `56.38%` | `0.77` | 2,250,000.00 USD |
| `1H` | `Gate` | `53.85%` | `46.15%` | `1.17` | 5,240,000.00 USD |
| `1H` | `Bitget` | `50.25%` | `49.75%` | `1.01` | 8,220,000.00 USD |
| `1H` | `BingX` | `30.72%` | `69.28%` | `0.44` | 2,350,000.00 USD |
| `1H` | `MEXC` | `48.37%` | `51.63%` | `0.94` | 17,440,000.00 USD |
| `1H` | `Bitunix` | `48.96%` | `51.04%` | `0.96` | 3,510,000.00 USD |
| `1H` | `Hyperliquid` | `50.78%` | `49.22%` | `1.03` | 3,050,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `39.89%` | `60.11%` | `0.66` | 307,570.00 USD |
| `1H` | `Crypto.com` | `64%` | `36%` | `1.78` | 183,060.00 USD |
| `1H` | `WhiteBIT` | `2.49%` | `97.51%` | `0.03` | 7,000,000.00 USD |
| `1H` | `HTX` | `55.65%` | `44.35%` | `1.25` | 44,260.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `49.69%` | `50.31%` | `0.99` | 1,280,000.00 USD |
| `1H` | `Aster` | `44.14%` | `55.86%` | `0.79` | 484,730.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `51.19%` | `48.81%` | `1.05` | 272,070.00 USD |
| `1H` | `Whale Positions` | `45.77%` | `54.23%` | `0.84` | 31,000,000.00 USD |
| `1H` | `Global Accounts` | `41.01%` | `58.99%` | `0.70` | 108,580,000.00 USD |
| `4H` | `BNB` | `47.27%` | `52.73%` | `0.90` | 461,100,000.00 USD |
| `4H` | `Binance` | `47.28%` | `52.72%` | `0.90` | 151,780,000.00 USD |
| `4H` | `OKX` | `44.8%` | `55.2%` | `0.81` | 49,820,000.00 USD |
| `4H` | `Bybit` | `48.73%` | `51.27%` | `0.95` | 73,800,000.00 USD |
| `4H` | `KuCoin` | `47.95%` | `52.05%` | `0.92` | 5,150,000.00 USD |
| `4H` | `Gate` | `51.18%` | `48.82%` | `1.05` | 23,670,000.00 USD |
| `4H` | `Bitget` | `42.94%` | `57.06%` | `0.75` | 34,940,000.00 USD |
| `4H` | `BingX` | `44.09%` | `55.91%` | `0.79` | 9,240,000.00 USD |
| `4H` | `MEXC` | `48.98%` | `51.02%` | `0.96` | 56,890,000.00 USD |
| `4H` | `Bitunix` | `45.78%` | `54.22%` | `0.84` | 16,400,000.00 USD |
| `4H` | `Hyperliquid` | `49.56%` | `50.44%` | `0.98` | 11,280,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `52.34%` | `47.66%` | `1.10` | 1,600,000.00 USD |
| `4H` | `Crypto.com` | `45.9%` | `54.1%` | `0.85` | 864,030.00 USD |
| `4H` | `WhiteBIT` | `73.41%` | `26.59%` | `2.76` | 18,860,000.00 USD |
| `4H` | `HTX` | `52.01%` | `47.99%` | `1.08` | 233,720.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `30.93%` | `69.07%` | `0.45` | 2,600,000.00 USD |
| `4H` | `Aster` | `36.68%` | `63.32%` | `0.58` | 3,160,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `47.7%` | `52.3%` | `0.91` | 823,790.00 USD |
| `4H` | `Whale Positions` | `47.28%` | `52.72%` | `0.90` | 151,780,000.00 USD |
| `4H` | `Global Accounts` | `47.27%` | `52.73%` | `0.90` | 461,100,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `707.85` | `707.46` | `707.85` | `708.45` | `706.05` | 5,397,479.08 USD | 2,137,235.04 USD | 3,260,244.05 USD | -1,123,009.01 USD | `-20.81%` | `0B / 3S` |
| `0:00 UTC` | `706.05` | `706.04` | `706.05` | `706.95` | `705.15` | 8,644,432.66 USD | 3,111,233.15 USD | 5,533,199.52 USD | -2,421,966.37 USD | `-28.02%` | `0B / 2S` |
| `5:00 UTC` | `705.15` | `704.94` | `705.15` | `705.75` | `703.95` | 6,533,203.74 USD | 2,600,747.39 USD | 3,932,456.35 USD | -1,331,708.96 USD | `-20.38%` | `0B / 1S` |
| `0:00 UTC` | `703.95` | `704.38` | `703.95` | `705.75` | `703.65` | 5,175,697.85 USD | 1,950,975.29 USD | 3,224,722.56 USD | -1,273,747.26 USD | `-24.61%` | `0B / 0S` |
| `5:00 UTC` | `703.95` | `703.57` | `703.95` | `704.55` | `702.75` | 8,548,516.20 USD | 3,944,253.54 USD | 4,604,262.66 USD | -660,009.13 USD | `-7.72%` | `0B / 0S` |
| `0:00 UTC` | `703.95` | `703.78` | `703.95` | `704.55` | `702.75` | 6,123,120.93 USD | 2,836,378.38 USD | 3,286,742.56 USD | -450,364.18 USD | `-7.36%` | `1B / 0S` |
| `5:00 UTC` | `702.75` | `702.81` | `702.75` | `703.95` | `701.85` | 6,303,040.32 USD | 2,898,299.22 USD | 3,404,741.10 USD | -506,441.88 USD | `-8.03%` | `1B / 0S` |
| `0:00 UTC` | `702.45` | `702.42` | `702.45` | `703.35` | `701.85` | 6,113,769.16 USD | 3,015,754.20 USD | 3,098,014.96 USD | -82,260.76 USD | `-1.35%` | `0B / 0S` |
| `5:00 UTC` | `701.55` | `701.57` | `701.55` | `702.75` | `700.65` | 5,730,646.91 USD | 2,127,528.75 USD | 3,603,118.16 USD | -1,475,589.41 USD | `-25.75%` | `0B / 3S` |
| `0:00 UTC` | `703.95` | `702.94` | `703.95` | `704.55` | `700.95` | 5,990,231.56 USD | 2,603,137.07 USD | 3,387,094.49 USD | -783,957.42 USD | `-13.09%` | `2B / 3S` |

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
| `5m` | -452,070.00 USD | -1,080,000.00 USD | **`DISTRIBUTION`** |
| `15m` | -802,260.00 USD | -1,980,000.00 USD | **`DISTRIBUTION`** |
| `30m` | -738,820.00 USD | -2,290,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,480,000.00 USD | -6,140,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -4,030,000.00 USD | -14,380,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -12,250,000.00 USD | -41,620,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,310,000.00 USD | -43,780,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -12,610,000.00 USD | -60,050,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -23,280,000.00 USD | -68,180,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -49,540,000.00 USD | -94,780,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -61,110,000.00 USD | -141,560,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -169,300,000.00 USD | -486,740,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-452.07K` | 15m=`-802.26K` | 1h=`-1.48M` | 24h=`-49.54M`
* Futures Capital Netflows: 5m=`-1.08M` | 15m=`-1.98M` | 1h=`-6.14M` | 24h=`-94.78M`
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
  * `2026-10-30 15:49:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:32:45 IST`: [ec.europa.eu] - (Sentiment: `Neutral`)
  * `2026-10-30 15:18:45 IST`: [dailyforex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 15:12:45 IST`: [breakingthenews.net] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@LiveSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [@FirstSquawk] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [destatis.de] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [istat.it] - (Sentiment: `Neutral`)
  * `2026-10-30 16:07:45 IST`: [channelnewsasia.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [ine.es] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [kof.ethz.ch] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [gerlachmacro.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 16:06:45 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `692.04` (Risk Distance: `6.91` pts)
  * +2.5R Take Profit: `716.22`
  * Mathematical Lot Sizing: **`1.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `714.93` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `721.84` (Risk Distance: `6.91` pts)
  * +2.5R Take Profit: `697.66`
  * Mathematical Lot Sizing: **`1.44 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`708.12`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
