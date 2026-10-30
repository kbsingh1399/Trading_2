# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:47:32 IST` (`2026-10-30 06:17:32 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

---

## 1. MT5 Live Broker Telemetry & True Contract Specifications
*(Sources: 00_MT5_Account_Telemetry.parquet, 23_Master_Pipeline_Telemetry.parquet, master_asset_catalog.json)*
- **Live Bid Quote**: `713.90` | **Live Ask Quote**: `717.10` | **Mid Price**: `715.50`
- **Spread Points**: `320.00` | **Spread BPS**: `44.72 bps` (Charter Threshold: `25.00 bps`)
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
  * Session VWAP: `701.21` | VWAP Z-Score: `+1.12` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `5.11` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `53.13` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `732.54` | Lower -3.00σ Band: `669.87`
  * Upper +2.51σ Band: `727.42` | Lower -2.51σ Band: `674.99`
  * Upper +2.01σ Band: `722.20` | Lower -2.01σ Band: `680.21`
  * Upper +2.00σ Band: `722.10` | Lower -2.00σ Band: `680.32`
  * Upper +1.28σ Band: `714.58` | Lower -1.28σ Band: `687.84`
  * Upper +1.00σ Band: `711.65` | Lower -1.00σ Band: `690.76`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`713.26` | EMA-20=`710.66` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`714.83` (Slope: `+0.0000`) | EMA-100=`724.41`
  * Institutional Anchors: EMA-144=`729.31` | EMA-200=`732.73` (Slope: `-0.3398`) | EMA-233=`734.34`
- **Range Boundaries**: 24H High=`755.37` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

---

## 3. Auction Market Structure & Volume Profile Framework
*(Sources: 20_Auction_Market_Structure.parquet, 11_Technical.parquet)*
- **Daily Developing Value Area**:
  * Value Area High (VAH) = `715.55` (Distance: `-0.01%`)
  * Point of Control (POC) = `706.94` (Distance: `+1.21%`)
  * Value Area Low (VAL) = `698.95` (Distance: `+2.37%`)
  * Auction Positioning: `INSIDE_VALUE (Balance)` | Session Bias: **`BULLISH (Above Pivot)`** | Market Regime: `ROTATIONAL_BALANCE`
- **Prior Day & Multi-Session Structural Reference Levels**:
  * Prior Day Value Area: VAH=`754.57` | POC=`744.11` | VAL=`738.60`
  * Prior Day Extremes: PDH=`759.80` | PDL=`677.20` | PDC=`696.20`
  * Monday Range Blueprint: High=`746.00` | Mid=`738.45` | Low=`730.90`
  * Developing Weekly Value Area: Weekly VAH=`751.69` | Weekly POC=`740.53` | Weekly VAL=`734.95`
- **Session High/Low Liquidity Pockets**:
  * Asian Session (00:00-08:00 UTC): High=`724.00` | Low=`677.90`
  * London Session (08:00-16:00 UTC): High=`717.90` | Low=`712.90`
  * New York Session (13:00-21:00 UTC): High=`719.79` | Low=`711.21`
  * Initial Balance (First Hour): IB High=`717.90` | IB Low=`712.90`
- **Fibonacci Institutional Confluence Nodes**:
  * Golden Pocket Zone (0.618 - 0.650): `712.64` - `718.36`
  * Optimal Trade Entry (OTE 0.705): `716.93`
  * Structural Invalidation Anchor (0.786): `721.22`

---

## 4. Multi-Timeframe Cumulative Volume Delta (CVD) & Options Surface
*(Sources: 18_CVD_30D_5m/15m/1h/4h/ALL.parquet, 18_CVD.parquet, 21_Tradfye_Orderflow.parquet)*
- **Multi-Timeframe CVD Execution Table (18_CVD_30D_ALL.parquet, 18_CVD.parquet)**:
| Timeframe | Open | High | Low | Close | Total Volume | Quote Vol (USD) | Candle Delta (USD) | Delta % | Cumulative CVD | CVD Z-Score | Directional Bias | Regime |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5m` | `715.88` | `716.71` | `715.61` | `715.85` | `3,812` | 2,730,025.59 USD | -350,291.49 USD | `-12.83%` | -42,265,043.56 USD | `-0.19` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `715.86` | `717.47` | `715.86` | `716.81` | `1,344` | 963,286.17 USD | -149,209.74 USD | `-15.49%` | -42,414,253.30 USD | `+0.11` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `5m` | `716.81` | `717.19` | `716.35` | `716.99` | `783` | 561,227.72 USD | -227,100.95 USD | `-40.47%` | -42,641,354.25 USD | `-0.03` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `719.49` | `719.66` | `716.84` | `717.61` | `6,829` | 4,905,512.59 USD | -831,410.72 USD | `-16.95%` | -38,643,631.16 USD | `+0.02` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `717.61` | `718.80` | `715.87` | `715.89` | `9,600` | 6,887,306.42 USD | -3,271,120.92 USD | `-47.49%` | -41,914,752.07 USD | `-1.05` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `715.88` | `717.47` | `715.61` | `717.00` | `5,937` | 4,253,026.64 USD | -725,146.69 USD | `-17.05%` | -42,639,898.76 USD | `+0.29` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `1h` | `719.56` | `719.60` | `715.13` | `717.32` | `39,263` | 28,162,402.44 USD | -3,149,012.91 USD | `-11.18%` | -35,501,287.17 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `717.32` | `721.67` | `715.87` | `715.89` | `37,119` | 26,675,746.45 USD | -4,022,750.80 USD | `-15.08%` | -39,524,037.97 USD | `-0.33` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `715.88` | `717.47` | `715.61` | `717.00` | `5,937` | 4,253,026.64 USD | -725,146.69 USD | `-17.05%` | -40,249,184.66 USD | `+0.04` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `716.99` | `82,317` | 59,090,028.32 USD | -7,898,000.24 USD | `-13.37%` | -36,640,648.95 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -2,294,794.05 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -2,062,598.17 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `716.99` | `82,317` | 59,090,028.32 USD | -7,898,000.24 USD | `-13.37%` | -36,640,648.95 USD | `-0.21` | **`BEARISH`** | `DELTA ALIGNED` |

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
| --- | **`715.50`** | **[CURRENT MID]** | --- | --- | --- | --- | --- | --- |

- **Consolidated L2 Orderbook Depth & Liquidity Skew Ladder (17_Orderbook.parquet)**:
| Side | Price (USD) | Size (Coins) | Depth (USD) | Cumulative Depth (USD) | Orders Tier | Distance (%) | Wallet / Explorer |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `BID` | `716.03` | `44407000000.0000` | 31,796.74 USD | 79,937.52 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `716.04` | `921000000.0000` | 659.47 USD | 48,140.77 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `716.06` | `32822000000.0000` | 23,502.52 USD | 47,481.30 USD | `2 orders` | `-0.07%` | `-` |
| `BID` | `716.09` | `921000000.0000` | 659.52 USD | 23,978.78 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `716.10` | `2318000000.0000` | 1,659.92 USD | 23,319.26 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `716.17` | `7387000000.0000` | 5,290.35 USD | 21,659.34 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `716.18` | `2494000000.0000` | 1,786.15 USD | 16,368.99 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `716.19` | `2449000000.0000` | 1,753.95 USD | 14,582.84 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `716.22` | `2797000000.0000` | 2,003.27 USD | 12,828.89 USD | `1 orders` | `-0.05%` | `-` |
| `BID` | `716.23` | `3238000000.0000` | 2,319.15 USD | 10,825.62 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `716.28` | `921000000.0000` | 659.69 USD | 8,506.47 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `716.30` | `921000000.0000` | 659.71 USD | 7,846.77 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `716.32` | `444000000.0000` | 318.05 USD | 7,187.06 USD | `2 orders` | `-0.03%` | `-` |
| `BID` | `716.36` | `2317000000.0000` | 1,659.81 USD | 6,869.02 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `716.37` | `2398000000.0000` | 1,717.86 USD | 5,209.21 USD | `2 orders` | `-0.02%` | `-` |
| `BID` | `716.42` | `921000000.0000` | 659.82 USD | 3,491.36 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `716.44` | `921000000.0000` | 659.84 USD | 2,831.53 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `716.48` | `690000000.0000` | 494.37 USD | 2,171.69 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `716.49` | `1922000000.0000` | 1,377.09 USD | 1,677.32 USD | `2 orders` | `-0.01%` | `-` |
| `BID` | `716.53` | `419000000.0000` | 300.23 USD | 300.23 USD | `1 orders` | `-0.00%` | `-` |
| `MID_SPREAD` | `716.54` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 716.54` | `0.00%` | `-` |
| `ASK` | `716.56` | `921000000.0000` | 659.95 USD | 659.95 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `716.59` | `1945000000.0000` | 1,393.77 USD | 2,053.72 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `716.60` | `2008000000.0000` | 1,438.93 USD | 3,492.65 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `716.63` | `15000000.0000` | 10.75 USD | 3,503.40 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.64` | `9302000000.0000` | 6,666.19 USD | 10,169.59 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.65` | `2319000000.0000` | 1,661.91 USD | 11,831.50 USD | `2 orders` | `+0.01%` | `-` |
| `ASK` | `716.66` | `1000000000.0000` | 716.66 USD | 12,548.16 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.68` | `150000000.0000` | 107.50 USD | 12,655.66 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.69` | `921000000.0000` | 660.07 USD | 13,315.73 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.70` | `12552000000.0000` | 8,996.02 USD | 22,311.75 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `716.71` | `2808000000.0000` | 2,012.52 USD | 24,324.27 USD | `4 orders` | `+0.02%` | `-` |
| `ASK` | `716.72` | `140000000.0000` | 100.34 USD | 24,424.61 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `716.73` | `140000000.0000` | 100.34 USD | 24,524.95 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.74` | `423000000.0000` | 303.18 USD | 24,828.14 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `716.75` | `990000000.0000` | 709.58 USD | 25,537.72 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `716.76` | `2795000000.0000` | 2,003.34 USD | 27,541.06 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.77` | `69000000.0000` | 49.46 USD | 27,590.52 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.78` | `140000000.0000` | 100.35 USD | 27,690.87 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `716.79` | `11135000000.0000` | 7,981.46 USD | 35,672.33 USD | `2 orders` | `+0.03%` | `-` |
| `ASK` | `716.81` | `2633000000.0000` | 1,887.36 USD | 37,559.69 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:43:56 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `781` | `0xea00...a918` | `LONG` | 2,937,671.94 USD | `4,098,429,000,000.00` | `787.24` | `716.16` | `0.000000` | -288,754.84 USD | `-9.83%` | `5X Cross` |
| `897` | `0xfe7c...b7ae` | `LONG` | 2,502,621.30 USD | `3,491,575,000,000.00` | `686.05` | `716.16` | `0.000000` | 107,210.44 USD | `+4.28%` | `10X Cross` |
| `1074` | `0x7d0c...1b28` | `LONG` | 2,027,413.39 USD | `2,828,620,000,000.00` | `703.85` | `716.16` | `0.000000` | 36,486.98 USD | `+1.80%` | `10X Cross` |
| `1087` | `0x27c9...d65d` | `LONG` | 2,000,889.94 USD | `2,791,498,000,000.00` | `700.84` | `716.16` | `171.42` | 44,487.87 USD | `+2.22%` | `10X Cross` |
| `1166` | `0x7737...bf66` | `SHORT` | 1,896,648.80 USD | `2,646,179,000,000.00` | `752.73` | `716.16` | `6900.82` | 95,221.79 USD | `+5.02%` | `10X Cross` |
| `1340` | `0x51f6...2b39` | `LONG` | 1,605,984.79 USD | `2,240,711,000,000.00` | `703.00` | `716.16` | `112.75` | 30,775.15 USD | `+1.92%` | `10X Cross` |
| `1463` | `0xc675...795d` | `LONG` | 1,472,601.94 USD | `2,055,214,000,000.00` | `706.91` | `716.16` | `640.89` | 19,757.27 USD | `+1.34%` | `10X Cross` |
| `1490` | `0x2edd...8179` | `LONG` | 1,447,381.30 USD | `2,019,367,000,000.00` | `714.56` | `716.16` | `0.000000` | 4,419.91 USD | `+0.31%` | `10X Cross` |
| `1552` | `0x325e...9564` | `LONG` | 1,386,346.45 USD | `1,934,212,000,000.00` | `707.43` | `716.16` | `0.000000` | 18,020.68 USD | `+1.30%` | `10X Cross` |
| `1603` | `0xecb6...2b00` | `SHORT` | 1,315,214.63 USD | `1,835,482,000,000.00` | `715.33` | `716.16` | `15289.56` | -2,247.79 USD | `-0.17%` | `5X Cross` |
| `1692` | `0x07fd...689d` | `LONG` | 1,238,835.00 USD | `1,728,406,000,000.00` | `714.40` | `716.16` | `0.000000` | 4,052.02 USD | `+0.33%` | `10X Cross` |
| `1697` | `0x645b...87b8` | `LONG` | 1,234,236.33 USD | `1,721,990,000,000.00` | `747.34` | `716.16` | `0.000000` | -52,671.09 USD | `-4.27%` | `10X Cross` |
| `1769` | `0xa4a6...46cf` | `SHORT` | 1,165,035.55 USD | `1,625,442,000,000.00` | `711.86` | `716.16` | `1624.36` | -7,943.18 USD | `-0.68%` | `10X Cross` |
| `1847` | `0xfc27...9d9d` | `LONG` | 1,101,921.30 USD | `1,537,536,000,000.00` | `701.02` | `716.16` | `0.000000` | 24,073.76 USD | `+2.18%` | `10X Cross` |
| `1861` | `0x4420...4c4b` | `LONG` | 1,089,668.91 USD | `1,520,143,000,000.00` | `704.02` | `716.16` | `213.69` | 19,458.34 USD | `+1.79%` | `10X Cross` |
| `1877` | `0x14c6...b280` | `SHORT` | 1,075,087.50 USD | `1,500,000,000,000.00` | `712.51` | `716.16` | `1467.32` | -6,325.80 USD | `-0.59%` | `10X Cross` |
| `1980` | `0x646b...01dc` | `SHORT` | 1,012,517.72 USD | `1,412,868,000,000.00` | `699.26` | `716.16` | `1250.68` | -24,548.73 USD | `-2.42%` | `10X Cross` |

- **Hyperdash Telegram Institutional Intelligence Alerts (16_Hyperdash_telegram_Intel.parquet)**:
| Event Type | Side | Price (USD) | Notional (USD) | Metric / Distance | Impact | Duration | Intelligence Detail | Time (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|:---:|
| Intel | Baseline | - | - | - | Neutral | - | No anomalous telegram alerts in current window | - |


---

## 6. Liquidation Max Pain, Heatmaps & Retail Stops Cascade Map
*(Sources: 14_Liquidation_Matrix.parquet, 14_Hyperdash_Liq_Map.parquet, 15_Hyperdash_Stops_Map.parquet, 9_Liquidation_Max_Pain_24H/48H/3D/7D.parquet, 8_Exchange_Liquidation_Map_1D/7D.parquet, 7_Liq_Heapmap.parquet, 7_Live_Liq.parquet, 22_Forced_Liquidations_MTF.parquet)*
- **Multi-Horizon Liquidation Max Pain Strikes (9_Liquidation_Max_Pain*.parquet)**:
  * 24H Horizon: Short MP=`758.19` (Vol: 2,900,000.00 USD, Dist: `+5.51%`) | Long MP=`677.28` (Vol: 3,100,000.00 USD, Dist: `--5.75%`)
  * 48H Horizon: Short MP=`767.93` (Vol: 3,000,000.00 USD, Dist: `+6.86%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.75%`)
  * 3D Horizon: Short MP=`767.93` (Vol: 3,400,000.00 USD, Dist: `+6.86%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.75%`)
  * 7D Horizon: Short MP=`767.93` (Vol: 3,500,000.00 USD, Dist: `+6.86%`) | Long MP=`677.29` (Vol: 3,100,000.00 USD, Dist: `--5.75%`)
- **Multi-Venue Complete Liquidation Matrix Ladder Table (14_Liquidation_Matrix.parquet)**:
| Timeframe | Side | Price Level (USD) | Liquidation Vol (USD) | Cumulative Liq (USD) | Binance Vol (USD) | OKX Vol (USD) | Bybit Vol (USD) | Venue Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long Liquidation` | `143.50` | 2,870.00 USD | 5,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `151.50` | 104.08 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `157.50` | 94,500.00 USD | 5,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `170.50` | 476,380.00 USD | 5,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `174.50` | 174,500.00 USD | 4,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 6,470.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `187.50` | 954.19 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `200.50` | 20,050.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 1,480.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 253.38 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `213.50` | 324,550.00 USD | 4,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `224.50` | 341.46 USD | 4,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `245.50` | 17,050.00 USD | 4,410,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 998.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `251.50` | 374.48 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `254.50` | 8,690.00 USD | 4,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `255.50` | 1,350.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `263.50` | 4,680.00 USD | 4,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `266.50` | 21,130.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `273.50` | 18,920.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `277.50` | 11,100.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `305.50` | 151,800.00 USD | 4,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `309.50` | 705.35 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `314.50` | 5,530.00 USD | 4,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `324.50` | 1,020.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `329.50` | 131,800.00 USD | 4,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 150.29 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 226.45 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `337.50` | 119.14 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `340.50` | 942.16 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 650.75 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `343.50` | 9,460.00 USD | 4,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `356.50` | 3,570.00 USD | 4,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 18,340.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 146.63 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `368.50` | 15,810.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 146.37 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `372.50` | 10,510.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 15,900.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 1,650.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 3,530.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `382.50` | 10,870.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 1,060.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 1,800.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `390.50` | 28,990.00 USD | 3,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 1,310.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 1,950.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 158.20 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `397.50` | 522.32 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `405.50` | 580.68 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 7,910.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 3,480.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 11,400.00 USD | 3,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 1,890.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 5,060.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 29,430.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 6,570.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 1,440.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `423.50` | 536.15 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `425.50` | 899.93 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `426.50` | 1,390.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `428.50` | 184.25 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `431.50` | 612.73 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 133.13 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `449.50` | 644.13 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `458.50` | 1,230.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 396.68 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 615.36 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 7,330.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 2,840.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,400.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `486.50` | 58,560.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 256.91 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 3,150.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `489.50` | 279.50 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 2,500.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 1,820.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 13,210.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 62,050.00 USD | 3,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 109.04 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 9,270.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 992.08 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 316.21 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 701.78 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 5,990.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 481.89 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 42,140.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 9,800.00 USD | 3,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 180,170.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 1,700.00 USD | 3,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 119,130.00 USD | 3,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 18,050.00 USD | 3,240,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 484.73 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 422.81 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,680.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 2,250.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 24,120.00 USD | 2,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 3,080.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 10,020.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 212.23 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `567.50` | 107.83 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 454.80 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 161,710.00 USD | 2,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 712,450.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 8,800.00 USD | 2,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `573.50` | 286.75 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 323.44 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 4,810.00 USD | 2,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 7,640.00 USD | 2,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 580.34 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 1,540.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,470.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,240.00 USD | 2,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 10,820.00 USD | 2,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 19,950.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `591.50` | 619.30 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 840.76 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 36,050.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 8,860.00 USD | 1,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 3,000.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 8,910.00 USD | 1,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,390.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,100.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 418.13 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 23,410.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 7,020.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 3,930.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 58,610.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 213.32 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 6,520.00 USD | 1,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 13,930.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,690.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 104.17 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 153.21 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `634.50` | 6,660.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 455.96 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 397,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 388,600.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `643.90` | 46,900,000.00 USD | 46,900,000.00 USD | 40,470.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.70` | 46,860,000.00 USD | 46,860,000.00 USD | 381,780.00 USD | 14,440.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.50` | 46,120,000.00 USD | 46,120,000.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.30` | 46,100,000.00 USD | 46,100,000.00 USD | 156,000.00 USD | 11,780.00 USD | 184,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 463.54 USD | 388,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.10` | 45,740,000.00 USD | 45,740,000.00 USD | 204,530.00 USD | 31,640.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.90` | 45,470,000.00 USD | 45,470,000.00 USD | 136,750.00 USD | 4,630.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 387,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.70` | 45,330,000.00 USD | 45,330,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.50` | 45,230,000.00 USD | 45,230,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,960.00 USD | 385,860.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `650.30` | 45,140,000.00 USD | 45,140,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 1,760.00 USD | 383,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.10` | 45,120,000.00 USD | 45,120,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 382,140.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.90` | 44,940,000.00 USD | 44,940,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 372,500.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.70` | 44,840,000.00 USD | 44,840,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `653.50` | 44,810,000.00 USD | 44,810,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 97,380.00 USD | 371,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.30` | 44,740,000.00 USD | 44,740,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 274,460.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.10` | 44,670,000.00 USD | 44,670,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 437.87 USD | 274,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.90` | 44,580,000.00 USD | 44,580,000.00 USD | 209,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.70` | 44,370,000.00 USD | 44,370,000.00 USD | 113,920.00 USD | 40,970.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.50` | 43,390,000.00 USD | 43,390,000.00 USD | 248,110.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.30` | 43,120,000.00 USD | 43,120,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 273,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.10` | 42,310,000.00 USD | 42,310,000.00 USD | 119,820.00 USD | 7,460.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 46,450.00 USD | 258,840.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.90` | 42,100,000.00 USD | 42,100,000.00 USD | 69,270.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 212,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.70` | 42,020,000.00 USD | 42,020,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `661.50` | 41,840,000.00 USD | 41,840,000.00 USD | 468,220.00 USD | 19,460.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 208,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.30` | 41,350,000.00 USD | 41,350,000.00 USD | 165,160.00 USD | 136,330.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 188,830.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.10` | 41,050,000.00 USD | 41,050,000.00 USD | 259,470.00 USD | 5,000.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 9,230.00 USD | 185,980.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.90` | 40,740,000.00 USD | 40,740,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 24,100.00 USD | 176,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.70` | 40,570,000.00 USD | 40,570,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.50` | 39,180,000.00 USD | 39,180,000.00 USD | 695,850.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 5,400.00 USD | 152,660.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.30` | 38,470,000.00 USD | 38,470,000.00 USD | 294,510.00 USD | 93,680.00 USD | 750,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 3,150.00 USD | 147,260.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.10` | 37,330,000.00 USD | 37,330,000.00 USD | 892,590.00 USD | 25,280.00 USD | 40,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 144,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.90` | 36,370,000.00 USD | 36,370,000.00 USD | 385,370.00 USD | 150,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 1,450.00 USD | 142,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `668.70` | 35,830,000.00 USD | 35,830,000.00 USD | 771,830.00 USD | 39,300.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.50` | 35,020,000.00 USD | 35,020,000.00 USD | 481,670.00 USD | 61,020.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 2,930.00 USD | 141,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.30` | 34,450,000.00 USD | 34,450,000.00 USD | 661,320.00 USD | 50,060.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 5,560.00 USD | 138,350.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.10` | 32,240,000.00 USD | 32,240,000.00 USD | 557,780.00 USD | 13,720.00 USD | 45,290.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 692.99 USD | 132,800.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.90` | 31,620,000.00 USD | 31,620,000.00 USD | 1,970,000.00 USD | 18,180.00 USD | 6,520.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 6,720.00 USD | 132,100.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.70` | 29,630,000.00 USD | 29,630,000.00 USD | 136,910.00 USD | 63,880.00 USD | 857,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.50` | 28,570,000.00 USD | 28,570,000.00 USD | 330,660.00 USD | 300,600.00 USD | 1,560,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 41,240.00 USD | 125,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.30` | 26,370,000.00 USD | 26,370,000.00 USD | 370,460.00 USD | 421,810.00 USD | 104,800.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,100.00 USD | 84,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.10` | 25,470,000.00 USD | 25,470,000.00 USD | 2,080,000.00 USD | 77,990.00 USD | 392,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 9,690.00 USD | 80,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.90` | 22,930,000.00 USD | 22,930,000.00 USD | 647,750.00 USD | 351,990.00 USD | 228,720.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 711.68 USD | 70,360.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `676.70` | 21,700,000.00 USD | 21,700,000.00 USD | 296,630.00 USD | 184,180.00 USD | 276,610.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.50` | 20,940,000.00 USD | 20,940,000.00 USD | 304,270.00 USD | 145,960.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 438.34 USD | 69,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.30` | 20,240,000.00 USD | 20,240,000.00 USD | 1,270,000.00 USD | 140,140.00 USD | 209,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 417.96 USD | 69,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.10` | 18,620,000.00 USD | 18,620,000.00 USD | 167,390.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 7,890.00 USD | 68,790.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.90` | 18,450,000.00 USD | 18,450,000.00 USD | 1,430,000.00 USD | 247,960.00 USD | 298,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 59,960.00 USD | 60,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.70` | 16,480,000.00 USD | 16,480,000.00 USD | 169,080.00 USD | 126,150.00 USD | 187,330.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.50` | 16,000,000.00 USD | 16,000,000.00 USD | 488,760.00 USD | 414,700.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.30` | 15,090,000.00 USD | 15,090,000.00 USD | 323,390.00 USD | 16,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.10` | 14,750,000.00 USD | 14,750,000.00 USD | 662,310.00 USD | 59,430.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.90` | 13,990,000.00 USD | 13,990,000.00 USD | 405,890.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.70` | 13,550,000.00 USD | 13,550,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.50` | 13,350,000.00 USD | 13,350,000.00 USD | 522,300.00 USD | 32,890.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.30` | 12,800,000.00 USD | 12,800,000.00 USD | 937,160.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.10` | 11,860,000.00 USD | 11,860,000.00 USD | 902,200.00 USD | 136,370.00 USD | 98,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.90` | 10,720,000.00 USD | 10,720,000.00 USD | 113,770.00 USD | 45,630.00 USD | 180,340.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.70` | 10,380,000.00 USD | 10,380,000.00 USD | 420,000.00 USD | 107,080.00 USD | 490,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.50` | 9,360,000.00 USD | 9,360,000.00 USD | 77,980.00 USD | 37,360.00 USD | 760,670.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.30` | 8,490,000.00 USD | 8,490,000.00 USD | 31,110.00 USD | 63,780.00 USD | 212,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.10` | 8,180,000.00 USD | 8,180,000.00 USD | 0.00 USD | 129,500.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.90` | 8,030,000.00 USD | 8,030,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.50` | 8,010,000.00 USD | 8,010,000.00 USD | 0.00 USD | 60,140.00 USD | 273,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.30` | 7,680,000.00 USD | 7,680,000.00 USD | 0.00 USD | 117,630.00 USD | 180,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.10` | 7,380,000.00 USD | 7,380,000.00 USD | 239,550.00 USD | 64,240.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.90` | 6,900,000.00 USD | 6,900,000.00 USD | 0.00 USD | 34,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.70` | 6,870,000.00 USD | 6,870,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.30` | 6,770,000.00 USD | 6,770,000.00 USD | 479,860.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.10` | 6,290,000.00 USD | 6,290,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.70` | 6,220,000.00 USD | 6,220,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.50` | 6,030,000.00 USD | 6,030,000.00 USD | 0.00 USD | 131,450.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.30` | 5,890,000.00 USD | 5,890,000.00 USD | 227,540.00 USD | 39,170.00 USD | 67,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.10` | 5,560,000.00 USD | 5,560,000.00 USD | 434,010.00 USD | 58,910.00 USD | 298,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.90` | 4,770,000.00 USD | 4,770,000.00 USD | 155,960.00 USD | 12,800.00 USD | 376,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.70` | 4,220,000.00 USD | 4,220,000.00 USD | 62,230.00 USD | 23,130.00 USD | 231,880.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.50` | 3,900,000.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 121,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `705.50` | 458.57 USD | 458.57 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `706.30` | 3,780,000.00 USD | 3,780,000.00 USD | 237,450.00 USD | 0.00 USD | 123,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `707.90` | 3,420,000.00 USD | 3,420,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `708.70` | 3,220,000.00 USD | 3,220,000.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `710.30` | 2,840,000.00 USD | 2,840,000.00 USD | 292,560.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.10` | 2,550,000.00 USD | 2,550,000.00 USD | 401,530.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.90` | 2,110,000.00 USD | 2,110,000.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.70` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.10` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 317,060.00 USD | 415,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.90` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.10` | 82,030.00 USD | 82,030.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.90` | 166,220.00 USD | 166,220.00 USD | 60,590.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 161.39 USD | 619.97 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.70` | 578,690.00 USD | 578,690.00 USD | 207,940.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.50` | 816,230.00 USD | 816,230.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,260.00 USD | 33,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.30` | 1,360,000.00 USD | 1,360,000.00 USD | 28,010.00 USD | 123,420.00 USD | 391,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 566.44 USD | 34,450.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.10` | 2,010,000.00 USD | 2,010,000.00 USD | 191,050.00 USD | 283,040.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 3,560.00 USD | 38,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.90` | 2,840,000.00 USD | 2,840,000.00 USD | 380,140.00 USD | 359,630.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 38,530.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.70` | 3,230,000.00 USD | 3,230,000.00 USD | 345,070.00 USD | 45,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `725.50` | 3,680,000.00 USD | 3,680,000.00 USD | 289,330.00 USD | 120,790.00 USD | 38,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 40,060.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `726.30` | 3,940,000.00 USD | 3,940,000.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 3,710.00 USD | 43,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.10` | 4,520,000.00 USD | 4,520,000.00 USD | 502,440.00 USD | 75,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 1,230.00 USD | 45,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.90` | 4,710,000.00 USD | 4,710,000.00 USD | 136,640.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,740.00 USD | 86,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.70` | 5,200,000.00 USD | 5,200,000.00 USD | 235,850.00 USD | 48,340.00 USD | 207,690.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.50` | 6,060,000.00 USD | 6,060,000.00 USD | 171,580.00 USD | 233,920.00 USD | 458,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 172,210.00 USD | 258,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.30` | 8,250,000.00 USD | 8,250,000.00 USD | 1,690,000.00 USD | 351,100.00 USD | 141,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 24,090.00 USD | 283,040.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.10` | 11,950,000.00 USD | 11,950,000.00 USD | 1,410,000.00 USD | 132,680.00 USD | 2,160,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 7,340.00 USD | 290,380.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.90` | 12,820,000.00 USD | 12,820,000.00 USD | 206,640.00 USD | 152,280.00 USD | 502,920.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 136,920.00 USD | 427,300.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.70` | 15,800,000.00 USD | 15,800,000.00 USD | 1,610,000.00 USD | 119,840.00 USD | 1,250,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `733.50` | 16,510,000.00 USD | 16,510,000.00 USD | 62,230.00 USD | 317,290.00 USD | 334,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 15,780.00 USD | 443,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.30` | 17,140,000.00 USD | 17,140,000.00 USD | 481,120.00 USD | 11,800.00 USD | 132,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,470.00 USD | 595,560.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.10` | 17,980,000.00 USD | 17,980,000.00 USD | 634,640.00 USD | 210,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 22,600.00 USD | 618,160.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.90` | 19,470,000.00 USD | 19,470,000.00 USD | 702,000.00 USD | 57,600.00 USD | 727,530.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 11,120.00 USD | 629,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.70` | 20,110,000.00 USD | 20,110,000.00 USD | 494,810.00 USD | 58,820.00 USD | 90,190.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.50` | 20,700,000.00 USD | 20,700,000.00 USD | 376,720.00 USD | 126,150.00 USD | 87,500.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 3,010.00 USD | 632,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.30` | 21,400,000.00 USD | 21,400,000.00 USD | 610,590.00 USD | 85,790.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 88,470.00 USD | 720,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.10` | 22,510,000.00 USD | 22,510,000.00 USD | 157,860.00 USD | 16,030.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.90` | 22,940,000.00 USD | 22,940,000.00 USD | 399,360.00 USD | 31,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 3,980.00 USD | 724,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `740.70` | 23,350,000.00 USD | 23,350,000.00 USD | 246,020.00 USD | 166,390.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.50` | 23,970,000.00 USD | 23,970,000.00 USD | 622,710.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 8,530.00 USD | 733,270.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.30` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 11,610.00 USD | 744,880.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.10` | 24,240,000.00 USD | 24,240,000.00 USD | 250,640.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 102,990.00 USD | 847,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.90` | 24,800,000.00 USD | 24,800,000.00 USD | 16,710.00 USD | 106,580.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 965,570.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.70` | 26,630,000.00 USD | 26,630,000.00 USD | 910,100.00 USD | 65,730.00 USD | 854,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.50` | 27,400,000.00 USD | 27,400,000.00 USD | 617,380.00 USD | 94,190.00 USD | 60,660.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 67,820.00 USD | 1,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.30` | 28,130,000.00 USD | 28,130,000.00 USD | 451,300.00 USD | 61,130.00 USD | 219,610.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 182,880.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.10` | 29,610,000.00 USD | 29,610,000.00 USD | 521,800.00 USD | 74,380.00 USD | 881,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.90` | 29,990,000.00 USD | 29,990,000.00 USD | 163,850.00 USD | 84,260.00 USD | 133,250.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 2,970.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.70` | 30,410,000.00 USD | 30,410,000.00 USD | 395,410.00 USD | 0.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.50` | 30,810,000.00 USD | 30,810,000.00 USD | 406,170.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 64,400.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.30` | 30,860,000.00 USD | 30,860,000.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 48,600.00 USD | 1,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.10` | 30,950,000.00 USD | 30,950,000.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 554,840.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.90` | 31,500,000.00 USD | 31,500,000.00 USD | 86,270.00 USD | 25,010.00 USD | 433,820.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 62,350.00 USD | 1,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.70` | 31,950,000.00 USD | 31,950,000.00 USD | 349,490.00 USD | 0.00 USD | 105,800.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.50` | 32,380,000.00 USD | 32,380,000.00 USD | 158,100.00 USD | 3,810.00 USD | 262,160.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.30` | 32,890,000.00 USD | 32,890,000.00 USD | 396,550.00 USD | 70,850.00 USD | 43,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,450.00 USD | 2,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.10` | 33,280,000.00 USD | 33,280,000.00 USD | 157,340.00 USD | 192,190.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `755.90` | 33,980,000.00 USD | 33,980,000.00 USD | 576,050.00 USD | 62,280.00 USD | 66,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.70` | 34,140,000.00 USD | 34,140,000.00 USD | 87,170.00 USD | 24,970.00 USD | 49,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.50` | 34,550,000.00 USD | 34,550,000.00 USD | 198,850.00 USD | 179,910.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 2,010.00 USD | 2,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.30` | 35,560,000.00 USD | 35,560,000.00 USD | 757,140.00 USD | 34,450.00 USD | 218,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,270.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.10` | 36,600,000.00 USD | 36,600,000.00 USD | 861,530.00 USD | 117,910.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 3,830.00 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `759.90` | 36,970,000.00 USD | 36,970,000.00 USD | 335,910.00 USD | 21,070.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 540.72 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.70` | 37,380,000.00 USD | 37,380,000.00 USD | 301,710.00 USD | 52,630.00 USD | 53,580.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.50` | 38,340,000.00 USD | 38,340,000.00 USD | 720,170.00 USD | 8,690.00 USD | 232,870.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.30` | 38,660,000.00 USD | 38,660,000.00 USD | 97,090.00 USD | 124,370.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 367.52 USD | 3,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.10` | 41,280,000.00 USD | 41,280,000.00 USD | 1,940,000.00 USD | 154,730.00 USD | 523,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 445,300.00 USD | 3,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.90` | 42,610,000.00 USD | 42,610,000.00 USD | 996,680.00 USD | 110,320.00 USD | 222,330.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 76,450.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.70` | 44,180,000.00 USD | 44,180,000.00 USD | 1,190,000.00 USD | 210,400.00 USD | 167,240.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.50` | 44,970,000.00 USD | 44,970,000.00 USD | 557,990.00 USD | 81,400.00 USD | 147,690.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.30` | 46,430,000.00 USD | 46,430,000.00 USD | 868,340.00 USD | 233,150.00 USD | 358,440.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.10` | 48,970,000.00 USD | 48,970,000.00 USD | 2,280,000.00 USD | 30,760.00 USD | 230,710.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.90` | 50,460,000.00 USD | 50,460,000.00 USD | 1,110,000.00 USD | 102,730.00 USD | 281,670.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.70` | 51,200,000.00 USD | 51,200,000.00 USD | 650,590.00 USD | 54,840.00 USD | 36,980.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.50` | 51,670,000.00 USD | 51,670,000.00 USD | 411,850.00 USD | 49,670.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.30` | 51,940,000.00 USD | 51,940,000.00 USD | 167,380.00 USD | 75,090.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 881.45 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.10` | 52,520,000.00 USD | 52,520,000.00 USD | 156,280.00 USD | 56,560.00 USD | 361,060.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 9,260.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.90` | 53,310,000.00 USD | 53,310,000.00 USD | 140,150.00 USD | 70,310.00 USD | 582,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 2,450.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.70` | 53,680,000.00 USD | 53,680,000.00 USD | 221,230.00 USD | 134,200.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.50` | 54,380,000.00 USD | 54,380,000.00 USD | 618,270.00 USD | 12,950.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 2,200.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.30` | 54,980,000.00 USD | 54,980,000.00 USD | 583,550.00 USD | 11,780.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.10` | 55,170,000.00 USD | 55,170,000.00 USD | 67,380.00 USD | 34,120.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.90` | 55,340,000.00 USD | 55,340,000.00 USD | 98,960.00 USD | 24,070.00 USD | 49,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 89,180.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `776.70` | 55,570,000.00 USD | 55,570,000.00 USD | 152,260.00 USD | 4,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.50` | 56,180,000.00 USD | 56,180,000.00 USD | 462,430.00 USD | 112,090.00 USD | 36,270.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.30` | 57,250,000.00 USD | 57,250,000.00 USD | 673,890.00 USD | 52,880.00 USD | 347,410.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 3,480.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.10` | 58,140,000.00 USD | 58,140,000.00 USD | 689,070.00 USD | 73,260.00 USD | 123,210.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.90` | 58,550,000.00 USD | 58,550,000.00 USD | 275,710.00 USD | 87,740.00 USD | 46,700.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 6,640.00 USD | 3,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.70` | 59,060,000.00 USD | 59,060,000.00 USD | 373,710.00 USD | 53,100.00 USD | 79,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.50` | 59,720,000.00 USD | 59,720,000.00 USD | 363,950.00 USD | 99,050.00 USD | 197,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 4,530.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.30` | 61,090,000.00 USD | 61,090,000.00 USD | 1,090,000.00 USD | 23,530.00 USD | 259,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `782.50` | 1,360.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.10` | 61,810,000.00 USD | 61,810,000.00 USD | 591,390.00 USD | 38,390.00 USD | 88,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `783.50` | 880.65 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.90` | 62,060,000.00 USD | 62,060,000.00 USD | 225,990.00 USD | 14,770.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.70` | 62,480,000.00 USD | 62,480,000.00 USD | 421,270.00 USD | 2,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.50` | 62,560,000.00 USD | 62,560,000.00 USD | 73,390.00 USD | 4,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 129.61 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.30` | 62,630,000.00 USD | 62,630,000.00 USD | 73,970.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 126,920.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.10` | 62,650,000.00 USD | 62,650,000.00 USD | 17,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `787.90` | 63,380,000.00 USD | 63,380,000.00 USD | 379,320.00 USD | 14,440.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 1,580.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.70` | 63,440,000.00 USD | 63,440,000.00 USD | 55,460.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `789.50` | 63,650,000.00 USD | 63,650,000.00 USD | 158,750.00 USD | 11,780.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.30` | 64,090,000.00 USD | 64,090,000.00 USD | 279,010.00 USD | 2,560.00 USD | 162,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.10` | 64,320,000.00 USD | 64,320,000.00 USD | 172,930.00 USD | 33,700.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `791.50` | 2,400.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `791.90` | 64,400,000.00 USD | 64,400,000.00 USD | 70,860.00 USD | 0.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.70` | 64,520,000.00 USD | 64,520,000.00 USD | 123,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.50` | 64,540,000.00 USD | 64,540,000.00 USD | 25,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 1,280.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 567.11 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,090.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 610.02 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `800.50` | 379.44 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,680.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 778,380.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `803.50` | 3,280.00 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 105.39 USD | 4,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,370.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 28,850.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 173.23 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `810.50` | 1,260.00 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `812.50` | 434.69 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 692.32 USD | 4,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `815.50` | 6,020.00 USD | 4,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 4,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 7,720.00 USD | 4,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,710.00 USD | 4,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 3,540.00 USD | 4,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `824.50` | 81,370.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `826.50` | 536,790.00 USD | 5,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 2,230.00 USD | 5,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `829.50` | 16,590.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `833.50` | 1,140.00 USD | 5,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 5,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 11,450.00 USD | 5,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,830.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 1,970.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 34,060.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 289.34 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 108.86 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 285.25 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `852.50` | 422,500.00 USD | 5,810,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `853.50` | 5,020.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `855.50` | 2,110.00 USD | 5,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `857.50` | 29,770.00 USD | 5,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 523,680.00 USD | 6,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 6,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 40,770.00 USD | 6,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `870.50` | 300,720.00 USD | 6,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 614,250.00 USD | 7,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 92,600.00 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 663.02 USD | 7,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `883.50` | 14,640.00 USD | 7,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 126,550.00 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `890.50` | 79,030.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 3,950.00 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 7,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 223,880.00 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 7,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `899.50` | 179,900.00 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `901.50` | 110.88 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 8,090,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 63,930.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 313.65 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 3,630.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 1,280.00 USD | 8,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 2,630.00 USD | 8,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 34,790.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 3,170.00 USD | 8,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 132,360.00 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `920.50` | 993.22 USD | 8,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `921.50` | 14,050.00 USD | 8,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `924.50` | 30,390.00 USD | 8,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 10,200.00 USD | 8,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 7,650.00 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `929.50` | 652.51 USD | 8,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `932.50` | 15,720.00 USD | 8,420,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `934.50` | 65,420.00 USD | 8,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `938.50` | 57,630.00 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `944.50` | 112.40 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `948.50` | 202.03 USD | 8,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `956.50` | 18,930.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `965.50` | 6,950.00 USD | 8,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `968.50` | 2,350.00 USD | 8,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `980.50` | 228.46 USD | 8,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `985.50` | 1,100.00 USD | 8,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 8,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 101,390.00 USD | 8,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 15,420.00 USD | 8,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 313.58 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 989.52 USD | 9,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 8,780.00 USD | 9,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 9,550.00 USD | 9,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 36,850.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 838.93 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1007.50` | 301.24 USD | 9,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 28,800.00 USD | 9,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,680.00 USD | 9,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1014.50` | 760,880.00 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1017.50` | 490.44 USD | 9,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1023.50` | 298,410.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 2,850.00 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1026.50` | 637.46 USD | 10,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1037.50` | 723,770.00 USD | 10,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 32,060.00 USD | 10,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1046.50` | 15,070.00 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 11,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1057.50` | 66,090.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 11,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 5,770.00 USD | 11,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 35,180.00 USD | 11,110,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1090.50` | 74,430.00 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1092.50` | 122.36 USD | 11,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 190,680.00 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1096.50` | 810.31 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1116.50` | 149.61 USD | 11,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1122.50` | 60,690.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1124.50` | 117,060.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1126.50` | 1,510.00 USD | 11,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,610.00 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1146.50` | 153.63 USD | 11,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1151.50` | 11,690.00 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1176.50` | 817.67 USD | 11,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1178.50` | 66,060.00 USD | 11,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1179.50` | 3,150.00 USD | 11,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1186.50` | 57,320.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1191.50` | 168.00 USD | 12,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 108,240.00 USD | 12,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1204.50` | 118,960.00 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1209.50` | 42,330.00 USD | 12,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1210.50` | 30,240.00 USD | 12,330,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1222.50` | 21,230.00 USD | 12,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 4,750.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1233.50` | 1,230.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1237.50` | 198.00 USD | 12,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1240.50` | 5,310.00 USD | 12,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1241.50` | 26,600.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1245.50` | 2,660.00 USD | 12,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 2,050.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1254.50` | 5,010.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1260.50` | 24,470.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 6,850.00 USD | 12,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1265.50` | 113,890.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1272.50` | 7,330.00 USD | 12,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 61,530.00 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1280.50` | 347.02 USD | 12,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1284.50` | 38,800.00 USD | 12,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1291.50` | 61,740.00 USD | 12,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1293.50` | 1,830,000.00 USD | 14,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 129,730.00 USD | 14,670,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1298.50` | 110,770.00 USD | 14,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1299.50` | 164,880.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1309.50` | 19,560.00 USD | 14,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 138.06 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 289.61 USD | 14,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 54,070.00 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1345.50` | 232.77 USD | 15,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1352.50` | 19,380.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1358.50` | 498.57 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1363.50` | 3,880.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1364.50` | 2,730.00 USD | 15,060,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1365.50` | 193.90 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1366.50` | 4,100.00 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 46,880.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1382.50` | 1,950.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1386.50` | 4,790.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1390.50` | 340,670.00 USD | 15,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 15,470,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1408.50` | 70,420.00 USD | 15,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1421.50` | 31,560.00 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1431.50` | 360.74 USD | 15,570,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `143.50` | 5,520,000.00 USD | 0.00 USD | 2,870.00 USD | `-79.97%` | `20,000,000,000.00` |
| `Live` | `Long` | `151.50` | 5,510,000.00 USD | 0.00 USD | 104.08 USD | `-78.86%` | `687,000,000.00` |
| `Live` | `Long` | `157.50` | 5,510,000.00 USD | 0.00 USD | 94,500.00 USD | `-78.02%` | `600,000,000,000.00` |
| `Live` | `Long` | `170.50` | 5,420,000.00 USD | 0.00 USD | 476,380.00 USD | `-76.20%` | `2,794,004,000,000.00` |
| `Live` | `Long` | `174.50` | 4,940,000.00 USD | 0.00 USD | 174,500.00 USD | `-75.65%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `178.50` | 4,770,000.00 USD | 0.00 USD | 6,470.00 USD | `-75.09%` | `36,251,000,000.00` |
| `Live` | `Long` | `187.50` | 4,760,000.00 USD | 0.00 USD | 954.19 USD | `-73.83%` | `5,089,000,000.00` |
| `Live` | `Long` | `200.50` | 4,760,000.00 USD | 0.00 USD | 20,050.00 USD | `-72.02%` | `100,000,000,000.00` |
| `Live` | `Long` | `205.50` | 4,740,000.00 USD | 0.00 USD | 1,480.00 USD | `-71.32%` | `7,186,000,000.00` |
| `Live` | `Long` | `206.50` | 4,740,000.00 USD | 0.00 USD | 253.38 USD | `-71.18%` | `1,227,000,000.00` |
| `Live` | `Long` | `213.50` | 4,740,000.00 USD | 0.00 USD | 324,550.00 USD | `-70.20%` | `1,520,143,000,000.00` |
| `Live` | `Long` | `219.50` | 4,420,000.00 USD | 0.00 USD | 191.18 USD | `-69.37%` | `871,000,000.00` |
| `Live` | `Long` | `224.50` | 4,420,000.00 USD | 0.00 USD | 341.46 USD | `-68.67%` | `1,521,000,000.00` |
| `Live` | `Long` | `245.50` | 4,410,000.00 USD | 0.00 USD | 17,050.00 USD | `-65.74%` | `69,447,000,000.00` |
| `Live` | `Long` | `249.50` | 4,400,000.00 USD | 0.00 USD | 998.00 USD | `-65.18%` | `4,000,000,000.00` |
| `Live` | `Long` | `251.50` | 4,400,000.00 USD | 0.00 USD | 374.48 USD | `-64.90%` | `1,489,000,000.00` |
| `Live` | `Long` | `254.50` | 4,400,000.00 USD | 0.00 USD | 8,690.00 USD | `-64.48%` | `34,129,000,000.00` |
| `Live` | `Long` | `255.50` | 4,390,000.00 USD | 0.00 USD | 1,350.00 USD | `-64.34%` | `5,281,000,000.00` |
| `Live` | `Long` | `263.50` | 4,390,000.00 USD | 0.00 USD | 4,680.00 USD | `-63.23%` | `17,770,000,000.00` |
| `Live` | `Long` | `266.50` | 4,380,000.00 USD | 0.00 USD | 21,130.00 USD | `-62.81%` | `79,269,000,000.00` |
| `Live` | `Long` | `273.50` | 4,360,000.00 USD | 0.00 USD | 18,920.00 USD | `-61.83%` | `69,189,000,000.00` |
| `Live` | `Long` | `277.50` | 4,340,000.00 USD | 0.00 USD | 11,100.00 USD | `-61.27%` | `40,000,000,000.00` |
| `Live` | `Long` | `305.50` | 4,330,000.00 USD | 0.00 USD | 151,800.00 USD | `-57.36%` | `496,876,000,000.00` |
| `Live` | `Long` | `309.50` | 4,180,000.00 USD | 0.00 USD | 705.35 USD | `-56.81%` | `2,279,000,000.00` |
| `Live` | `Long` | `312.50` | 4,180,000.00 USD | 0.00 USD | 500.00 USD | `-56.39%` | `1,600,000,000.00` |
| `Live` | `Long` | `314.50` | 4,180,000.00 USD | 0.00 USD | 5,530.00 USD | `-56.11%` | `17,576,000,000.00` |
| `Live` | `Long` | `324.50` | 4,170,000.00 USD | 0.00 USD | 1,020.00 USD | `-54.71%` | `3,147,000,000.00` |
| `Live` | `Long` | `326.50` | 4,170,000.00 USD | 0.00 USD | 500.85 USD | `-54.43%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,170,000.00 USD | 0.00 USD | 314.07 USD | `-54.29%` | `959,000,000.00` |
| `Live` | `Long` | `329.50` | 4,170,000.00 USD | 0.00 USD | 131,800.00 USD | `-54.01%` | `400,000,000,000.00` |
| `Live` | `Long` | `332.50` | 4,040,000.00 USD | 0.00 USD | 150.29 USD | `-53.60%` | `452,000,000.00` |
| `Live` | `Long` | `333.50` | 4,040,000.00 USD | 0.00 USD | 226.45 USD | `-53.46%` | `679,000,000.00` |
| `Live` | `Long` | `337.50` | 4,040,000.00 USD | 0.00 USD | 119.14 USD | `-52.90%` | `353,000,000.00` |
| `Live` | `Long` | `340.50` | 4,040,000.00 USD | 0.00 USD | 942.16 USD | `-52.48%` | `2,767,000,000.00` |
| `Live` | `Long` | `342.50` | 4,040,000.00 USD | 0.00 USD | 650.75 USD | `-52.20%` | `1,900,000,000.00` |
| `Live` | `Long` | `343.50` | 4,040,000.00 USD | 0.00 USD | 9,460.00 USD | `-52.06%` | `27,554,000,000.00` |
| `Live` | `Long` | `356.50` | 4,030,000.00 USD | 0.00 USD | 3,570.00 USD | `-50.25%` | `10,019,000,000.00` |
| `Live` | `Long` | `359.50` | 4,020,000.00 USD | 0.00 USD | 212.10 USD | `-49.83%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,020,000.00 USD | 0.00 USD | 18,340.00 USD | `-49.27%` | `50,441,000,000.00` |
| `Live` | `Long` | `366.50` | 4,000,000.00 USD | 0.00 USD | 549.75 USD | `-48.85%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 4,000,000.00 USD | 0.00 USD | 146.63 USD | `-48.71%` | `399,000,000.00` |
| `Live` | `Long` | `368.50` | 4,000,000.00 USD | 0.00 USD | 15,810.00 USD | `-48.57%` | `42,904,000,000.00` |
| `Live` | `Long` | `371.50` | 3,990,000.00 USD | 0.00 USD | 146.37 USD | `-48.15%` | `394,000,000.00` |
| `Live` | `Long` | `372.50` | 3,990,000.00 USD | 0.00 USD | 10,510.00 USD | `-48.01%` | `28,204,000,000.00` |
| `Live` | `Long` | `373.50` | 3,980,000.00 USD | 0.00 USD | 15,900.00 USD | `-47.87%` | `42,578,000,000.00` |
| `Live` | `Long` | `374.50` | 3,960,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.73%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 3,960,000.00 USD | 0.00 USD | 1,650.00 USD | `-47.32%` | `4,381,000,000.00` |
| `Live` | `Long` | `378.50` | 3,960,000.00 USD | 0.00 USD | 643.45 USD | `-47.18%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 3,960,000.00 USD | 0.00 USD | 3,530.00 USD | `-46.76%` | `9,250,000,000.00` |
| `Live` | `Long` | `382.50` | 3,950,000.00 USD | 0.00 USD | 10,870.00 USD | `-46.62%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 3,940,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.34%` | `2,746,000,000.00` |
| `Live` | `Long` | `385.50` | 3,940,000.00 USD | 0.00 USD | 1,800.00 USD | `-46.20%` | `4,675,000,000.00` |
| `Live` | `Long` | `386.50` | 3,940,000.00 USD | 0.00 USD | 531.44 USD | `-46.06%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 3,940,000.00 USD | 0.00 USD | 392.54 USD | `-45.92%` | `1,013,000,000.00` |
| `Live` | `Long` | `390.50` | 3,940,000.00 USD | 0.00 USD | 28,990.00 USD | `-45.50%` | `74,245,000,000.00` |
| `Live` | `Long` | `393.50` | 3,910,000.00 USD | 0.00 USD | 1,310.00 USD | `-45.08%` | `3,337,000,000.00` |
| `Live` | `Long` | `394.50` | 3,910,000.00 USD | 0.00 USD | 1,950.00 USD | `-44.94%` | `4,947,000,000.00` |
| `Live` | `Long` | `395.50` | 3,910,000.00 USD | 0.00 USD | 158.20 USD | `-44.80%` | `400,000,000.00` |
| `Live` | `Long` | `396.50` | 3,910,000.00 USD | 0.00 USD | 317.20 USD | `-44.66%` | `800,000,000.00` |
| `Live` | `Long` | `397.50` | 3,910,000.00 USD | 0.00 USD | 522.32 USD | `-44.52%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 3,910,000.00 USD | 0.00 USD | 603.64 USD | `-44.25%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 3,910,000.00 USD | 0.00 USD | 102.34 USD | `-43.55%` | `253,000,000.00` |
| `Live` | `Long` | `405.50` | 3,910,000.00 USD | 0.00 USD | 580.68 USD | `-43.41%` | `1,432,000,000.00` |
| `Live` | `Long` | `409.50` | 3,900,000.00 USD | 0.00 USD | 613.02 USD | `-42.85%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 3,900,000.00 USD | 0.00 USD | 7,910.00 USD | `-42.71%` | `19,258,000,000.00` |
| `Live` | `Long` | `411.50` | 3,900,000.00 USD | 0.00 USD | 3,480.00 USD | `-42.57%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 3,890,000.00 USD | 0.00 USD | 11,400.00 USD | `-42.29%` | `27,562,000,000.00` |
| `Live` | `Long` | `414.50` | 3,880,000.00 USD | 0.00 USD | 1,890.00 USD | `-42.15%` | `4,566,000,000.00` |
| `Live` | `Long` | `415.50` | 3,880,000.00 USD | 0.00 USD | 5,060.00 USD | `-42.01%` | `12,167,000,000.00` |
| `Live` | `Long` | `417.50` | 3,870,000.00 USD | 0.00 USD | 7,140.00 USD | `-41.73%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 3,870,000.00 USD | 0.00 USD | 318.06 USD | `-41.59%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 3,870,000.00 USD | 0.00 USD | 2,650.00 USD | `-41.45%` | `6,316,000,000.00` |
| `Live` | `Long` | `420.50` | 3,860,000.00 USD | 0.00 USD | 29,430.00 USD | `-41.31%` | `70,000,000,000.00` |
| `Live` | `Long` | `421.50` | 3,840,000.00 USD | 0.00 USD | 6,570.00 USD | `-41.17%` | `15,583,000,000.00` |
| `Live` | `Long` | `422.50` | 3,830,000.00 USD | 0.00 USD | 1,440.00 USD | `-41.04%` | `3,419,000,000.00` |
| `Live` | `Long` | `423.50` | 3,830,000.00 USD | 0.00 USD | 536.15 USD | `-40.90%` | `1,266,000,000.00` |
| `Live` | `Long` | `425.50` | 3,830,000.00 USD | 0.00 USD | 899.93 USD | `-40.62%` | `2,115,000,000.00` |
| `Live` | `Long` | `426.50` | 3,830,000.00 USD | 0.00 USD | 1,390.00 USD | `-40.48%` | `3,259,000,000.00` |
| `Live` | `Long` | `428.50` | 3,820,000.00 USD | 0.00 USD | 184.25 USD | `-40.20%` | `430,000,000.00` |
| `Live` | `Long` | `429.50` | 3,820,000.00 USD | 0.00 USD | 846.12 USD | `-40.06%` | `1,970,000,000.00` |
| `Live` | `Long` | `431.50` | 3,820,000.00 USD | 0.00 USD | 612.73 USD | `-39.78%` | `1,420,000,000.00` |
| `Live` | `Long` | `436.50` | 3,820,000.00 USD | 0.00 USD | 133.13 USD | `-39.08%` | `305,000,000.00` |
| `Live` | `Long` | `438.50` | 3,820,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.80%` | `4,087,000,000.00` |
| `Live` | `Long` | `448.50` | 3,820,000.00 USD | 0.00 USD | 3,350.00 USD | `-37.41%` | `7,470,000,000.00` |
| `Live` | `Long` | `449.50` | 3,820,000.00 USD | 0.00 USD | 644.13 USD | `-37.27%` | `1,433,000,000.00` |
| `Live` | `Long` | `456.50` | 3,820,000.00 USD | 0.00 USD | 4,730.00 USD | `-36.29%` | `10,359,000,000.00` |
| `Live` | `Long` | `458.50` | 3,810,000.00 USD | 0.00 USD | 1,230.00 USD | `-36.01%` | `2,682,000,000.00` |
| `Live` | `Long` | `464.50` | 3,810,000.00 USD | 0.00 USD | 396.68 USD | `-35.17%` | `854,000,000.00` |
| `Live` | `Long` | `469.50` | 3,810,000.00 USD | 0.00 USD | 4,370.00 USD | `-34.48%` | `9,301,000,000.00` |
| `Live` | `Long` | `475.50` | 3,810,000.00 USD | 0.00 USD | 5,320.00 USD | `-33.64%` | `11,182,000,000.00` |
| `Live` | `Long` | `481.50` | 3,800,000.00 USD | 0.00 USD | 615.36 USD | `-32.80%` | `1,278,000,000.00` |
| `Live` | `Long` | `482.50` | 3,800,000.00 USD | 0.00 USD | 7,330.00 USD | `-32.66%` | `15,184,000,000.00` |
| `Live` | `Long` | `484.50` | 3,790,000.00 USD | 0.00 USD | 2,840.00 USD | `-32.38%` | `5,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,790,000.00 USD | 0.00 USD | 2,400.00 USD | `-32.24%` | `4,947,000,000.00` |
| `Live` | `Long` | `486.50` | 3,790,000.00 USD | 0.00 USD | 58,560.00 USD | `-32.10%` | `120,366,000,000.00` |
| `Live` | `Long` | `487.50` | 3,730,000.00 USD | 0.00 USD | 256.91 USD | `-31.96%` | `527,000,000.00` |
| `Live` | `Long` | `488.50` | 3,730,000.00 USD | 0.00 USD | 3,150.00 USD | `-31.82%` | `6,446,000,000.00` |
| `Live` | `Long` | `489.50` | 3,730,000.00 USD | 0.00 USD | 279.50 USD | `-31.68%` | `571,000,000.00` |
| `Live` | `Long` | `493.50` | 3,730,000.00 USD | 0.00 USD | 2,500.00 USD | `-31.13%` | `5,069,000,000.00` |
| `Live` | `Long` | `498.50` | 3,720,000.00 USD | 0.00 USD | 1,820.00 USD | `-30.43%` | `3,656,000,000.00` |
| `Live` | `Long` | `499.50` | 3,720,000.00 USD | 0.00 USD | 13,210.00 USD | `-30.29%` | `26,444,000,000.00` |
| `Live` | `Long` | `501.50` | 3,710,000.00 USD | 0.00 USD | 62,050.00 USD | `-30.01%` | `123,724,000,000.00` |
| `Live` | `Long` | `502.50` | 3,650,000.00 USD | 0.00 USD | 109.04 USD | `-29.87%` | `217,000,000.00` |
| `Live` | `Long` | `505.50` | 3,650,000.00 USD | 0.00 USD | 9,270.00 USD | `-29.45%` | `18,331,000,000.00` |
| `Live` | `Long` | `508.50` | 3,640,000.00 USD | 0.00 USD | 992.08 USD | `-29.03%` | `1,951,000,000.00` |
| `Live` | `Long` | `509.50` | 3,640,000.00 USD | 0.00 USD | 3,100.00 USD | `-28.89%` | `6,091,000,000.00` |
| `Live` | `Long` | `510.50` | 3,630,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.75%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,630,000.00 USD | 0.00 USD | 5,180.00 USD | `-28.61%` | `10,118,000,000.00` |
| `Live` | `Long` | `512.50` | 3,620,000.00 USD | 0.00 USD | 316.21 USD | `-28.47%` | `617,000,000.00` |
| `Live` | `Long` | `513.50` | 3,620,000.00 USD | 0.00 USD | 2,520.00 USD | `-28.34%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,620,000.00 USD | 0.00 USD | 701.78 USD | `-28.20%` | `1,364,000,000.00` |
| `Live` | `Long` | `515.50` | 3,620,000.00 USD | 0.00 USD | 5,990.00 USD | `-28.06%` | `11,621,000,000.00` |
| `Live` | `Long` | `516.50` | 3,610,000.00 USD | 0.00 USD | 481.89 USD | `-27.92%` | `933,000,000.00` |
| `Live` | `Long` | `517.50` | 3,610,000.00 USD | 0.00 USD | 22,650.00 USD | `-27.78%` | `43,765,000,000.00` |
| `Live` | `Long` | `519.50` | 3,590,000.00 USD | 0.00 USD | 968.35 USD | `-27.50%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 3,590,000.00 USD | 0.00 USD | 42,140.00 USD | `-27.36%` | `80,955,000,000.00` |
| `Live` | `Long` | `521.50` | 3,550,000.00 USD | 0.00 USD | 9,800.00 USD | `-27.22%` | `18,796,000,000.00` |
| `Live` | `Long` | `522.50` | 3,540,000.00 USD | 0.00 USD | 180,170.00 USD | `-27.08%` | `344,832,000,000.00` |
| `Live` | `Long` | `524.50` | 3,360,000.00 USD | 0.00 USD | 833.43 USD | `-26.80%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 3,360,000.00 USD | 0.00 USD | 1,700.00 USD | `-26.52%` | `3,234,000,000.00` |
| `Live` | `Long` | `529.50` | 3,350,000.00 USD | 0.00 USD | 119,130.00 USD | `-26.10%` | `224,979,000,000.00` |
| `Live` | `Long` | `530.50` | 3,240,000.00 USD | 0.00 USD | 18,050.00 USD | `-25.96%` | `34,028,000,000.00` |
| `Live` | `Long` | `531.50` | 3,220,000.00 USD | 0.00 USD | 484.73 USD | `-25.82%` | `912,000,000.00` |
| `Live` | `Long` | `532.50` | 3,220,000.00 USD | 0.00 USD | 422.81 USD | `-25.68%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,220,000.00 USD | 0.00 USD | 555.35 USD | `-25.40%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,220,000.00 USD | 0.00 USD | 100.14 USD | `-25.26%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 3,220,000.00 USD | 0.00 USD | 490.94 USD | `-24.71%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,220,000.00 USD | 0.00 USD | 471.32 USD | `-24.57%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,210,000.00 USD | 0.00 USD | 2,680.00 USD | `-24.15%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,210,000.00 USD | 0.00 USD | 210,830.00 USD | `-24.01%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 3,000,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.87%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 3,000,000.00 USD | 0.00 USD | 530.11 USD | `-23.73%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 3,000,000.00 USD | 0.00 USD | 2,250.00 USD | `-23.45%` | `4,111,000,000.00` |
| `Live` | `Long` | `549.50` | 3,000,000.00 USD | 0.00 USD | 1,370.00 USD | `-23.31%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 3,000,000.00 USD | 0.00 USD | 633.63 USD | `-23.17%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 2,990,000.00 USD | 0.00 USD | 1,250.00 USD | `-23.03%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 2,990,000.00 USD | 0.00 USD | 24,120.00 USD | `-22.89%` | `43,665,000,000.00` |
| `Live` | `Long` | `553.50` | 2,970,000.00 USD | 0.00 USD | 3,080.00 USD | `-22.75%` | `5,565,000,000.00` |
| `Live` | `Long` | `556.50` | 2,970,000.00 USD | 0.00 USD | 5,670.00 USD | `-22.33%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 2,960,000.00 USD | 0.00 USD | 10,020.00 USD | `-22.19%` | `17,967,000,000.00` |
| `Live` | `Long` | `558.50` | 2,950,000.00 USD | 0.00 USD | 212.23 USD | `-22.05%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 2,950,000.00 USD | 0.00 USD | 582.36 USD | `-21.78%` | `1,039,000,000.00` |
| `Live` | `Long` | `567.50` | 2,950,000.00 USD | 0.00 USD | 107.83 USD | `-20.80%` | `190,000,000.00` |
| `Live` | `Long` | `568.50` | 2,950,000.00 USD | 0.00 USD | 454.80 USD | `-20.66%` | `800,000,000.00` |
| `Live` | `Long` | `569.50` | 2,950,000.00 USD | 0.00 USD | 161,710.00 USD | `-20.52%` | `283,953,000,000.00` |
| `Live` | `Long` | `571.50` | 2,790,000.00 USD | 0.00 USD | 712,450.00 USD | `-20.24%` | `1,246,635,000,000.00` |
| `Live` | `Long` | `572.50` | 2,080,000.00 USD | 0.00 USD | 8,800.00 USD | `-20.10%` | `15,374,000,000.00` |
| `Live` | `Long` | `573.50` | 2,070,000.00 USD | 0.00 USD | 286.75 USD | `-19.96%` | `500,000,000.00` |
| `Live` | `Long` | `574.50` | 2,070,000.00 USD | 0.00 USD | 323.44 USD | `-19.82%` | `563,000,000.00` |
| `Live` | `Long` | `576.50` | 2,070,000.00 USD | 0.00 USD | 4,810.00 USD | `-19.54%` | `8,349,000,000.00` |
| `Live` | `Long` | `578.50` | 2,060,000.00 USD | 0.00 USD | 7,640.00 USD | `-19.26%` | `13,202,000,000.00` |
| `Live` | `Long` | `580.50` | 2,050,000.00 USD | 0.00 USD | 35,850.00 USD | `-18.98%` | `61,765,000,000.00` |
| `Live` | `Long` | `581.50` | 2,020,000.00 USD | 0.00 USD | 580.34 USD | `-18.84%` | `998,000,000.00` |
| `Live` | `Long` | `582.50` | 2,020,000.00 USD | 0.00 USD | 1,540.00 USD | `-18.71%` | `2,646,000,000.00` |
| `Live` | `Long` | `583.50` | 2,020,000.00 USD | 0.00 USD | 3,470.00 USD | `-18.57%` | `5,952,000,000.00` |
| `Live` | `Long` | `585.50` | 2,010,000.00 USD | 0.00 USD | 210.19 USD | `-18.29%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 2,010,000.00 USD | 0.00 USD | 2,360.00 USD | `-18.15%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 2,010,000.00 USD | 0.00 USD | 5,240.00 USD | `-18.01%` | `8,916,000,000.00` |
| `Live` | `Long` | `588.50` | 2,000,000.00 USD | 0.00 USD | 397.24 USD | `-17.87%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 2,000,000.00 USD | 0.00 USD | 10,820.00 USD | `-17.73%` | `18,352,000,000.00` |
| `Live` | `Long` | `590.50` | 1,990,000.00 USD | 0.00 USD | 19,950.00 USD | `-17.59%` | `33,781,000,000.00` |
| `Live` | `Long` | `591.50` | 1,970,000.00 USD | 0.00 USD | 619.30 USD | `-17.45%` | `1,047,000,000.00` |
| `Live` | `Long` | `592.50` | 1,970,000.00 USD | 0.00 USD | 840.76 USD | `-17.31%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 1,970,000.00 USD | 0.00 USD | 36,050.00 USD | `-17.17%` | `60,735,000,000.00` |
| `Live` | `Long` | `594.50` | 1,940,000.00 USD | 0.00 USD | 8,860.00 USD | `-17.03%` | `14,906,000,000.00` |
| `Live` | `Long` | `595.50` | 1,930,000.00 USD | 0.00 USD | 3,000.00 USD | `-16.89%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,920,000.00 USD | 0.00 USD | 8,910.00 USD | `-16.75%` | `14,934,000,000.00` |
| `Live` | `Long` | `597.50` | 1,910,000.00 USD | 0.00 USD | 2,390.00 USD | `-16.61%` | `3,998,000,000.00` |
| `Live` | `Long` | `598.50` | 1,910,000.00 USD | 0.00 USD | 1,100.00 USD | `-16.47%` | `1,832,000,000.00` |
| `Live` | `Long` | `600.50` | 1,910,000.00 USD | 0.00 USD | 945.19 USD | `-16.19%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,910,000.00 USD | 0.00 USD | 16,880.00 USD | `-16.05%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,890,000.00 USD | 0.00 USD | 418.13 USD | `-15.91%` | `694,000,000.00` |
| `Live` | `Long` | `603.50` | 1,890,000.00 USD | 0.00 USD | 23,410.00 USD | `-15.77%` | `38,785,000,000.00` |
| `Live` | `Long` | `604.50` | 1,870,000.00 USD | 0.00 USD | 7,020.00 USD | `-15.64%` | `11,609,000,000.00` |
| `Live` | `Long` | `606.50` | 1,860,000.00 USD | 0.00 USD | 3,930.00 USD | `-15.36%` | `6,473,000,000.00` |
| `Live` | `Long` | `607.50` | 1,860,000.00 USD | 0.00 USD | 58,610.00 USD | `-15.22%` | `96,477,000,000.00` |
| `Live` | `Long` | `609.50` | 1,800,000.00 USD | 0.00 USD | 213.32 USD | `-14.94%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,800,000.00 USD | 0.00 USD | 1,580.00 USD | `-14.66%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,800,000.00 USD | 0.00 USD | 12,250.00 USD | `-14.52%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,790,000.00 USD | 0.00 USD | 120.25 USD | `-14.38%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,790,000.00 USD | 0.00 USD | 4,280.00 USD | `-14.24%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,780,000.00 USD | 0.00 USD | 1,540.00 USD | `-13.96%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,780,000.00 USD | 0.00 USD | 156.23 USD | `-13.82%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,780,000.00 USD | 0.00 USD | 932.70 USD | `-13.68%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,780,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.54%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,780,000.00 USD | 0.00 USD | 6,520.00 USD | `-13.40%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,770,000.00 USD | 0.00 USD | 13,930.00 USD | `-13.26%` | `22,412,000,000.00` |
| `Live` | `Long` | `624.50` | 1,760,000.00 USD | 0.00 USD | 3,690.00 USD | `-12.84%` | `5,905,000,000.00` |
| `Live` | `Long` | `625.50` | 1,750,000.00 USD | 0.00 USD | 14,200.00 USD | `-12.70%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,740,000.00 USD | 0.00 USD | 964.81 USD | `-12.56%` | `1,540,000,000.00` |
| `Live` | `Long` | `627.50` | 1,740,000.00 USD | 0.00 USD | 104.17 USD | `-12.43%` | `166,000,000.00` |
| `Live` | `Long` | `630.50` | 1,740,000.00 USD | 0.00 USD | 153.21 USD | `-12.01%` | `243,000,000.00` |
| `Live` | `Long` | `631.50` | 1,740,000.00 USD | 0.00 USD | 2,900.00 USD | `-11.87%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,740,000.00 USD | 0.00 USD | 3,560.00 USD | `-11.73%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,730,000.00 USD | 0.00 USD | 6,660.00 USD | `-11.45%` | `10,489,000,000.00` |
| `Live` | `Long` | `635.50` | 1,720,000.00 USD | 0.00 USD | 155.06 USD | `-11.31%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,720,000.00 USD | 0.00 USD | 1,110.00 USD | `-11.17%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,720,000.00 USD | 0.00 USD | 305.36 USD | `-11.03%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,720,000.00 USD | 0.00 USD | 6,710.00 USD | `-10.89%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,720,000.00 USD | 0.00 USD | 455.96 USD | `-10.75%` | `713,000,000.00` |
| `Live` | `Long` | `640.50` | 1,720,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-10.61%` | `2,059,440,000,000.00` |
| `Live` | `Long` | `642.50` | 397,080.00 USD | 0.00 USD | 8,480.00 USD | `-10.33%` | `13,199,000,000.00` |
| `Live` | `Long` | `643.50` | 388,600.00 USD | 0.00 USD | 339.12 USD | `-10.19%` | `527,000,000.00` |
| `Live` | `Long` | `646.50` | 388,260.00 USD | 0.00 USD | 463.54 USD | `-9.77%` | `717,000,000.00` |
| `Live` | `Long` | `648.50` | 387,800.00 USD | 0.00 USD | 1,940.00 USD | `-9.49%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 385,860.00 USD | 0.00 USD | 1,960.00 USD | `-9.35%` | `3,016,000,000.00` |
| `Live` | `Long` | `650.50` | 383,900.00 USD | 0.00 USD | 1,760.00 USD | `-9.22%` | `2,703,000,000.00` |
| `Live` | `Long` | `651.50` | 382,140.00 USD | 0.00 USD | 9,650.00 USD | `-9.08%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 372,500.00 USD | 0.00 USD | 652.50 USD | `-8.94%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 371,840.00 USD | 0.00 USD | 97,380.00 USD | `-8.80%` | `149,014,000,000.00` |
| `Live` | `Long` | `654.50` | 274,460.00 USD | 0.00 USD | 100.14 USD | `-8.66%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 274,360.00 USD | 0.00 USD | 437.87 USD | `-8.52%` | `668,000,000.00` |
| `Live` | `Long` | `658.50` | 273,930.00 USD | 0.00 USD | 15,090.00 USD | `-8.10%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 258,840.00 USD | 0.00 USD | 46,450.00 USD | `-7.96%` | `70,433,000,000.00` |
| `Live` | `Long` | `660.50` | 212,380.00 USD | 0.00 USD | 3,410.00 USD | `-7.82%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 208,970.00 USD | 0.00 USD | 20,140.00 USD | `-7.68%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 188,830.00 USD | 0.00 USD | 2,850.00 USD | `-7.54%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 185,980.00 USD | 0.00 USD | 9,230.00 USD | `-7.40%` | `13,911,000,000.00` |
| `Live` | `Long` | `664.50` | 176,750.00 USD | 0.00 USD | 24,100.00 USD | `-7.26%` | `36,261,000,000.00` |
| `Live` | `Long` | `665.50` | 152,660.00 USD | 0.00 USD | 5,400.00 USD | `-7.12%` | `8,112,000,000.00` |
| `Live` | `Long` | `666.50` | 147,260.00 USD | 0.00 USD | 3,150.00 USD | `-6.98%` | `4,728,000,000.00` |
| `Live` | `Long` | `667.50` | 144,110.00 USD | 0.00 USD | 1,380.00 USD | `-6.84%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 142,730.00 USD | 0.00 USD | 1,450.00 USD | `-6.70%` | `2,164,000,000.00` |
| `Live` | `Long` | `669.50` | 141,280.00 USD | 0.00 USD | 2,930.00 USD | `-6.56%` | `4,371,000,000.00` |
| `Live` | `Long` | `670.50` | 138,350.00 USD | 0.00 USD | 5,560.00 USD | `-6.42%` | `8,289,000,000.00` |
| `Live` | `Long` | `671.50` | 132,800.00 USD | 0.00 USD | 692.99 USD | `-6.28%` | `1,032,000,000.00` |
| `Live` | `Long` | `672.50` | 132,100.00 USD | 0.00 USD | 6,720.00 USD | `-6.14%` | `9,986,000,000.00` |
| `Live` | `Long` | `673.50` | 125,390.00 USD | 0.00 USD | 41,240.00 USD | `-6.01%` | `61,234,000,000.00` |
| `Live` | `Long` | `674.50` | 84,150.00 USD | 0.00 USD | 4,100.00 USD | `-5.87%` | `6,078,000,000.00` |
| `Live` | `Long` | `675.50` | 80,050.00 USD | 0.00 USD | 9,690.00 USD | `-5.73%` | `14,346,000,000.00` |
| `Live` | `Long` | `676.50` | 70,360.00 USD | 0.00 USD | 711.68 USD | `-5.59%` | `1,052,000,000.00` |
| `Live` | `Long` | `677.50` | 69,650.00 USD | 0.00 USD | 438.34 USD | `-5.45%` | `647,000,000.00` |
| `Live` | `Long` | `678.50` | 69,210.00 USD | 0.00 USD | 417.96 USD | `-5.31%` | `616,000,000.00` |
| `Live` | `Long` | `679.50` | 68,790.00 USD | 0.00 USD | 7,890.00 USD | `-5.17%` | `11,616,000,000.00` |
| `Live` | `Long` | `680.50` | 60,900.00 USD | 0.00 USD | 59,960.00 USD | `-5.03%` | `88,106,000,000.00` |
| `Live` | `Long` | `681.50` | 939.79 USD | 0.00 USD | 939.79 USD | `-4.89%` | `1,379,000,000.00` |
| `Live` | `Short` | `705.50` | 458.57 USD | 458.57 USD | 0.00 USD | `-1.54%` | `650,000,000.00` |
| `Live` | `Short` | `720.50` | 619.97 USD | 161.39 USD | 0.00 USD | `+0.55%` | `224,000,000.00` |
| `Live` | `Short` | `721.50` | 33,880.00 USD | 33,260.00 USD | 0.00 USD | `+0.69%` | `46,099,000,000.00` |
| `Live` | `Short` | `722.50` | 34,450.00 USD | 566.44 USD | 0.00 USD | `+0.83%` | `784,000,000.00` |
| `Live` | `Short` | `723.50` | 38,000.00 USD | 3,560.00 USD | 0.00 USD | `+0.97%` | `4,914,000,000.00` |
| `Live` | `Short` | `724.50` | 38,530.00 USD | 525.26 USD | 0.00 USD | `+1.11%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 40,060.00 USD | 1,530.00 USD | 0.00 USD | `+1.25%` | `2,108,000,000.00` |
| `Live` | `Short` | `726.50` | 43,770.00 USD | 3,710.00 USD | 0.00 USD | `+1.39%` | `5,105,000,000.00` |
| `Live` | `Short` | `727.50` | 45,000.00 USD | 1,230.00 USD | 0.00 USD | `+1.53%` | `1,693,000,000.00` |
| `Live` | `Short` | `728.50` | 86,740.00 USD | 41,740.00 USD | 0.00 USD | `+1.67%` | `57,295,000,000.00` |
| `Live` | `Short` | `729.50` | 258,950.00 USD | 172,210.00 USD | 0.00 USD | `+1.81%` | `236,072,000,000.00` |
| `Live` | `Short` | `730.50` | 283,040.00 USD | 24,090.00 USD | 0.00 USD | `+1.95%` | `32,978,000,000.00` |
| `Live` | `Short` | `731.50` | 290,380.00 USD | 7,340.00 USD | 0.00 USD | `+2.09%` | `10,036,000,000.00` |
| `Live` | `Short` | `732.50` | 427,300.00 USD | 136,920.00 USD | 0.00 USD | `+2.23%` | `186,920,000,000.00` |
| `Live` | `Short` | `733.50` | 443,080.00 USD | 15,780.00 USD | 0.00 USD | `+2.37%` | `21,512,000,000.00` |
| `Live` | `Short` | `734.50` | 595,560.00 USD | 152,470.00 USD | 0.00 USD | `+2.51%` | `207,590,000,000.00` |
| `Live` | `Short` | `735.50` | 618,160.00 USD | 22,600.00 USD | 0.00 USD | `+2.65%` | `30,729,000,000.00` |
| `Live` | `Short` | `736.50` | 629,280.00 USD | 11,120.00 USD | 0.00 USD | `+2.79%` | `15,104,000,000.00` |
| `Live` | `Short` | `737.50` | 632,290.00 USD | 3,010.00 USD | 0.00 USD | `+2.93%` | `4,082,000,000.00` |
| `Live` | `Short` | `738.50` | 720,770.00 USD | 88,470.00 USD | 0.00 USD | `+3.07%` | `119,803,000,000.00` |
| `Live` | `Short` | `740.50` | 724,750.00 USD | 3,980.00 USD | 0.00 USD | `+3.35%` | `5,376,000,000.00` |
| `Live` | `Short` | `741.50` | 733,270.00 USD | 8,530.00 USD | 0.00 USD | `+3.48%` | `11,498,000,000.00` |
| `Live` | `Short` | `742.50` | 744,880.00 USD | 11,610.00 USD | 0.00 USD | `+3.62%` | `15,634,000,000.00` |
| `Live` | `Short` | `743.50` | 847,870.00 USD | 102,990.00 USD | 0.00 USD | `+3.76%` | `138,520,000,000.00` |
| `Live` | `Short` | `744.50` | 965,570.00 USD | 117,700.00 USD | 0.00 USD | `+3.90%` | `158,091,000,000.00` |
| `Live` | `Short` | `745.50` | 1,030,000.00 USD | 67,820.00 USD | 0.00 USD | `+4.04%` | `90,974,000,000.00` |
| `Live` | `Short` | `746.50` | 1,220,000.00 USD | 182,880.00 USD | 0.00 USD | `+4.18%` | `244,988,000,000.00` |
| `Live` | `Short` | `748.50` | 1,220,000.00 USD | 2,970.00 USD | 0.00 USD | `+4.46%` | `3,974,000,000.00` |
| `Live` | `Short` | `749.50` | 1,280,000.00 USD | 64,400.00 USD | 0.00 USD | `+4.60%` | `85,920,000,000.00` |
| `Live` | `Short` | `750.50` | 1,330,000.00 USD | 48,600.00 USD | 0.00 USD | `+4.74%` | `64,754,000,000.00` |
| `Live` | `Short` | `751.50` | 1,890,000.00 USD | 554,840.00 USD | 0.00 USD | `+4.88%` | `738,316,000,000.00` |
| `Live` | `Short` | `752.50` | 1,950,000.00 USD | 62,350.00 USD | 0.00 USD | `+5.02%` | `82,863,000,000.00` |
| `Live` | `Short` | `754.50` | 2,810,000.00 USD | 863,450.00 USD | 0.00 USD | `+5.30%` | `1,144,401,000,000.00` |
| `Live` | `Short` | `756.50` | 2,820,000.00 USD | 3,750.00 USD | 0.00 USD | `+5.58%` | `4,960,000,000.00` |
| `Live` | `Short` | `757.50` | 2,820,000.00 USD | 2,010.00 USD | 0.00 USD | `+5.72%` | `2,652,000,000.00` |
| `Live` | `Short` | `758.50` | 3,000,000.00 USD | 180,270.00 USD | 0.00 USD | `+5.86%` | `237,673,000,000.00` |
| `Live` | `Short` | `759.50` | 3,000,000.00 USD | 3,830.00 USD | 0.00 USD | `+6.00%` | `5,039,000,000.00` |
| `Live` | `Short` | `760.50` | 3,000,000.00 USD | 540.72 USD | 0.00 USD | `+6.14%` | `711,000,000.00` |
| `Live` | `Short` | `762.50` | 3,000,000.00 USD | 367.52 USD | 0.00 USD | `+6.42%` | `482,000,000.00` |
| `Live` | `Short` | `763.50` | 3,450,000.00 USD | 445,300.00 USD | 0.00 USD | `+6.56%` | `583,234,000,000.00` |
| `Live` | `Short` | `764.50` | 3,530,000.00 USD | 76,450.00 USD | 0.00 USD | `+6.69%` | `100,000,000,000.00` |
| `Live` | `Short` | `766.50` | 3,530,000.00 USD | 2,850.00 USD | 0.00 USD | `+6.97%` | `3,719,000,000.00` |
| `Live` | `Short` | `768.50` | 3,530,000.00 USD | 156.77 USD | 0.00 USD | `+7.25%` | `204,000,000.00` |
| `Live` | `Short` | `770.50` | 3,530,000.00 USD | 881.45 USD | 0.00 USD | `+7.53%` | `1,144,000,000.00` |
| `Live` | `Short` | `771.50` | 3,540,000.00 USD | 9,260.00 USD | 0.00 USD | `+7.67%` | `12,000,000,000.00` |
| `Live` | `Short` | `772.50` | 3,540,000.00 USD | 2,450.00 USD | 0.00 USD | `+7.81%` | `3,173,000,000.00` |
| `Live` | `Short` | `773.50` | 3,540,000.00 USD | 2,200.00 USD | 0.00 USD | `+7.95%` | `2,842,000,000.00` |
| `Live` | `Short` | `776.50` | 3,630,000.00 USD | 89,180.00 USD | 0.00 USD | `+8.37%` | `114,851,000,000.00` |
| `Live` | `Short` | `777.50` | 3,630,000.00 USD | 209.15 USD | 0.00 USD | `+8.51%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 3,640,000.00 USD | 3,480.00 USD | 0.00 USD | `+8.65%` | `4,472,000,000.00` |
| `Live` | `Short` | `780.50` | 3,640,000.00 USD | 6,640.00 USD | 0.00 USD | `+8.93%` | `8,508,000,000.00` |
| `Live` | `Short` | `781.50` | 3,650,000.00 USD | 4,530.00 USD | 0.00 USD | `+9.07%` | `5,801,000,000.00` |
| `Live` | `Short` | `782.50` | 3,650,000.00 USD | 1,360.00 USD | 0.00 USD | `+9.21%` | `1,736,000,000.00` |
| `Live` | `Short` | `783.50` | 3,650,000.00 USD | 880.65 USD | 0.00 USD | `+9.35%` | `1,124,000,000.00` |
| `Live` | `Short` | `785.50` | 3,650,000.00 USD | 129.61 USD | 0.00 USD | `+9.63%` | `165,000,000.00` |
| `Live` | `Short` | `786.50` | 3,780,000.00 USD | 126,920.00 USD | 0.00 USD | `+9.77%` | `161,372,000,000.00` |
| `Live` | `Short` | `788.50` | 3,780,000.00 USD | 1,580.00 USD | 0.00 USD | `+10.04%` | `2,000,000,000.00` |
| `Live` | `Short` | `791.50` | 3,780,000.00 USD | 2,400.00 USD | 0.00 USD | `+10.46%` | `3,029,000,000.00` |
| `Live` | `Short` | `793.50` | 3,780,000.00 USD | 1,280.00 USD | 0.00 USD | `+10.74%` | `1,616,000,000.00` |
| `Live` | `Short` | `795.50` | 3,780,000.00 USD | 518.67 USD | 0.00 USD | `+11.02%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 3,780,000.00 USD | 567.11 USD | 0.00 USD | `+11.16%` | `712,000,000.00` |
| `Live` | `Short` | `797.50` | 3,780,000.00 USD | 1,090.00 USD | 0.00 USD | `+11.30%` | `1,367,000,000.00` |
| `Live` | `Short` | `799.50` | 3,780,000.00 USD | 610.02 USD | 0.00 USD | `+11.58%` | `763,000,000.00` |
| `Live` | `Short` | `800.50` | 3,780,000.00 USD | 379.44 USD | 0.00 USD | `+11.72%` | `474,000,000.00` |
| `Live` | `Short` | `801.50` | 3,790,000.00 USD | 3,680.00 USD | 0.00 USD | `+11.86%` | `4,594,000,000.00` |
| `Live` | `Short` | `802.50` | 4,570,000.00 USD | 778,380.00 USD | 0.00 USD | `+12.00%` | `969,946,000,000.00` |
| `Live` | `Short` | `803.50` | 4,570,000.00 USD | 3,280.00 USD | 0.00 USD | `+12.14%` | `4,076,000,000.00` |
| `Live` | `Short` | `804.50` | 4,570,000.00 USD | 105.39 USD | 0.00 USD | `+12.28%` | `131,000,000.00` |
| `Live` | `Short` | `805.50` | 4,590,000.00 USD | 15,370.00 USD | 0.00 USD | `+12.42%` | `19,085,000,000.00` |
| `Live` | `Short` | `806.50` | 4,590,000.00 USD | 2,890.00 USD | 0.00 USD | `+12.56%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 4,620,000.00 USD | 28,850.00 USD | 0.00 USD | `+12.70%` | `35,727,000,000.00` |
| `Live` | `Short` | `808.50` | 4,630,000.00 USD | 11,780.00 USD | 0.00 USD | `+12.84%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 4,630,000.00 USD | 173.23 USD | 0.00 USD | `+12.98%` | `214,000,000.00` |
| `Live` | `Short` | `810.50` | 4,630,000.00 USD | 1,260.00 USD | 0.00 USD | `+13.11%` | `1,551,000,000.00` |
| `Live` | `Short` | `812.50` | 4,630,000.00 USD | 434.69 USD | 0.00 USD | `+13.39%` | `535,000,000.00` |
| `Live` | `Short` | `814.50` | 4,630,000.00 USD | 692.32 USD | 0.00 USD | `+13.67%` | `850,000,000.00` |
| `Live` | `Short` | `815.50` | 4,640,000.00 USD | 6,020.00 USD | 0.00 USD | `+13.81%` | `7,383,000,000.00` |
| `Live` | `Short` | `816.50` | 4,650,000.00 USD | 15,410.00 USD | 0.00 USD | `+13.95%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 4,650,000.00 USD | 325.37 USD | 0.00 USD | `+14.09%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 4,660,000.00 USD | 7,720.00 USD | 0.00 USD | `+14.23%` | `9,432,000,000.00` |
| `Live` | `Short` | `821.50` | 4,670,000.00 USD | 11,710.00 USD | 0.00 USD | `+14.65%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 4,680,000.00 USD | 3,540.00 USD | 0.00 USD | `+14.79%` | `4,302,000,000.00` |
| `Live` | `Short` | `824.50` | 4,760,000.00 USD | 81,370.00 USD | 0.00 USD | `+15.07%` | `98,695,000,000.00` |
| `Live` | `Short` | `826.50` | 5,290,000.00 USD | 536,790.00 USD | 0.00 USD | `+15.35%` | `649,473,000,000.00` |
| `Live` | `Short` | `828.50` | 5,300,000.00 USD | 2,230.00 USD | 0.00 USD | `+15.63%` | `2,689,000,000.00` |
| `Live` | `Short` | `829.50` | 5,310,000.00 USD | 16,590.00 USD | 0.00 USD | `+15.77%` | `20,000,000,000.00` |
| `Live` | `Short` | `833.50` | 5,310,000.00 USD | 1,140.00 USD | 0.00 USD | `+16.32%` | `1,371,000,000.00` |
| `Live` | `Short` | `834.50` | 5,320,000.00 USD | 1,010.00 USD | 0.00 USD | `+16.46%` | `1,206,000,000.00` |
| `Live` | `Short` | `837.50` | 5,330,000.00 USD | 11,450.00 USD | 0.00 USD | `+16.88%` | `13,676,000,000.00` |
| `Live` | `Short` | `838.50` | 5,350,000.00 USD | 21,840.00 USD | 0.00 USD | `+17.02%` | `26,046,000,000.00` |
| `Live` | `Short` | `841.50` | 5,350,000.00 USD | 2,830.00 USD | 0.00 USD | `+17.44%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 5,350,000.00 USD | 1,970.00 USD | 0.00 USD | `+17.58%` | `2,344,000,000.00` |
| `Live` | `Short` | `843.50` | 5,390,000.00 USD | 34,060.00 USD | 0.00 USD | `+17.72%` | `40,378,000,000.00` |
| `Live` | `Short` | `848.50` | 5,390,000.00 USD | 289.34 USD | 0.00 USD | `+18.42%` | `341,000,000.00` |
| `Live` | `Short` | `850.50` | 5,390,000.00 USD | 108.86 USD | 0.00 USD | `+18.70%` | `128,000,000.00` |
| `Live` | `Short` | `851.50` | 5,390,000.00 USD | 285.25 USD | 0.00 USD | `+18.84%` | `335,000,000.00` |
| `Live` | `Short` | `852.50` | 5,810,000.00 USD | 422,500.00 USD | 0.00 USD | `+18.98%` | `495,603,000,000.00` |
| `Live` | `Short` | `853.50` | 5,820,000.00 USD | 5,020.00 USD | 0.00 USD | `+19.12%` | `5,884,000,000.00` |
| `Live` | `Short` | `855.50` | 5,820,000.00 USD | 2,110.00 USD | 0.00 USD | `+19.39%` | `2,462,000,000.00` |
| `Live` | `Short` | `857.50` | 5,850,000.00 USD | 29,770.00 USD | 0.00 USD | `+19.67%` | `34,722,000,000.00` |
| `Live` | `Short` | `858.50` | 6,370,000.00 USD | 523,680.00 USD | 0.00 USD | `+19.81%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 6,390,000.00 USD | 16,380.00 USD | 0.00 USD | `+19.95%` | `19,059,000,000.00` |
| `Live` | `Short` | `865.50` | 6,430,000.00 USD | 40,770.00 USD | 0.00 USD | `+20.79%` | `47,107,000,000.00` |
| `Live` | `Short` | `870.50` | 6,730,000.00 USD | 300,720.00 USD | 0.00 USD | `+21.49%` | `345,452,000,000.00` |
| `Live` | `Short` | `877.50` | 7,340,000.00 USD | 614,250.00 USD | 0.00 USD | `+22.47%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 7,440,000.00 USD | 92,600.00 USD | 0.00 USD | `+22.60%` | `105,403,000,000.00` |
| `Live` | `Short` | `880.50` | 7,440,000.00 USD | 663.02 USD | 0.00 USD | `+22.88%` | `753,000,000.00` |
| `Live` | `Short` | `883.50` | 7,450,000.00 USD | 14,640.00 USD | 0.00 USD | `+23.30%` | `16,565,000,000.00` |
| `Live` | `Short` | `885.50` | 7,580,000.00 USD | 126,550.00 USD | 0.00 USD | `+23.58%` | `142,909,000,000.00` |
| `Live` | `Short` | `886.50` | 7,580,000.00 USD | 812.92 USD | 0.00 USD | `+23.72%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,580,000.00 USD | 385.18 USD | 0.00 USD | `+23.86%` | `434,000,000.00` |
| `Live` | `Short` | `890.50` | 7,660,000.00 USD | 79,030.00 USD | 0.00 USD | `+24.28%` | `88,749,000,000.00` |
| `Live` | `Short` | `891.50` | 7,660,000.00 USD | 3,950.00 USD | 0.00 USD | `+24.42%` | `4,429,000,000.00` |
| `Live` | `Short` | `893.50` | 7,660,000.00 USD | 173.34 USD | 0.00 USD | `+24.70%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,690,000.00 USD | 26,840.00 USD | 0.00 USD | `+24.84%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 7,910,000.00 USD | 223,880.00 USD | 0.00 USD | `+24.98%` | `250,000,000,000.00` |
| `Live` | `Short` | `898.50` | 7,910,000.00 USD | 127.59 USD | 0.00 USD | `+25.40%` | `142,000,000.00` |
| `Live` | `Short` | `899.50` | 8,090,000.00 USD | 179,900.00 USD | 0.00 USD | `+25.54%` | `200,000,000,000.00` |
| `Live` | `Short` | `901.50` | 8,090,000.00 USD | 110.88 USD | 0.00 USD | `+25.81%` | `123,000,000.00` |
| `Live` | `Short` | `902.50` | 8,090,000.00 USD | 305.05 USD | 0.00 USD | `+25.95%` | `338,000,000.00` |
| `Live` | `Short` | `904.50` | 8,160,000.00 USD | 63,930.00 USD | 0.00 USD | `+26.23%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 8,160,000.00 USD | 313.65 USD | 0.00 USD | `+26.51%` | `346,000,000.00` |
| `Live` | `Short` | `908.50` | 8,160,000.00 USD | 3,630.00 USD | 0.00 USD | `+26.79%` | `3,992,000,000.00` |
| `Live` | `Short` | `909.50` | 8,160,000.00 USD | 1,280.00 USD | 0.00 USD | `+26.93%` | `1,405,000,000.00` |
| `Live` | `Short` | `910.50` | 8,170,000.00 USD | 2,630.00 USD | 0.00 USD | `+27.07%` | `2,884,000,000.00` |
| `Live` | `Short` | `911.50` | 8,200,000.00 USD | 34,790.00 USD | 0.00 USD | `+27.21%` | `38,169,000,000.00` |
| `Live` | `Short` | `913.50` | 8,200,000.00 USD | 3,170.00 USD | 0.00 USD | `+27.49%` | `3,472,000,000.00` |
| `Live` | `Short` | `918.50` | 8,340,000.00 USD | 132,360.00 USD | 0.00 USD | `+28.19%` | `144,104,000,000.00` |
| `Live` | `Short` | `920.50` | 8,340,000.00 USD | 993.22 USD | 0.00 USD | `+28.47%` | `1,079,000,000.00` |
| `Live` | `Short` | `921.50` | 8,350,000.00 USD | 14,050.00 USD | 0.00 USD | `+28.61%` | `15,247,000,000.00` |
| `Live` | `Short` | `924.50` | 8,380,000.00 USD | 30,390.00 USD | 0.00 USD | `+29.02%` | `32,872,000,000.00` |
| `Live` | `Short` | `925.50` | 8,390,000.00 USD | 10,200.00 USD | 0.00 USD | `+29.16%` | `11,022,000,000.00` |
| `Live` | `Short` | `928.50` | 8,400,000.00 USD | 7,650.00 USD | 0.00 USD | `+29.58%` | `8,244,000,000.00` |
| `Live` | `Short` | `929.50` | 8,400,000.00 USD | 652.51 USD | 0.00 USD | `+29.72%` | `702,000,000.00` |
| `Live` | `Short` | `932.50` | 8,420,000.00 USD | 15,720.00 USD | 0.00 USD | `+30.14%` | `16,854,000,000.00` |
| `Live` | `Short` | `934.50` | 8,480,000.00 USD | 65,420.00 USD | 0.00 USD | `+30.42%` | `70,000,000,000.00` |
| `Live` | `Short` | `938.50` | 8,540,000.00 USD | 57,630.00 USD | 0.00 USD | `+30.98%` | `61,406,000,000.00` |
| `Live` | `Short` | `944.50` | 8,540,000.00 USD | 112.40 USD | 0.00 USD | `+31.82%` | `119,000,000.00` |
| `Live` | `Short` | `948.50` | 8,540,000.00 USD | 202.03 USD | 0.00 USD | `+32.37%` | `213,000,000.00` |
| `Live` | `Short` | `956.50` | 8,560,000.00 USD | 18,930.00 USD | 0.00 USD | `+33.49%` | `19,788,000,000.00` |
| `Live` | `Short` | `965.50` | 8,560,000.00 USD | 6,950.00 USD | 0.00 USD | `+34.75%` | `7,199,000,000.00` |
| `Live` | `Short` | `968.50` | 8,570,000.00 USD | 2,350.00 USD | 0.00 USD | `+35.17%` | `2,428,000,000.00` |
| `Live` | `Short` | `969.50` | 8,570,000.00 USD | 5,780.00 USD | 0.00 USD | `+35.30%` | `5,960,000,000.00` |
| `Live` | `Short` | `980.50` | 8,570,000.00 USD | 228.46 USD | 0.00 USD | `+36.84%` | `233,000,000.00` |
| `Live` | `Short` | `981.50` | 8,590,000.00 USD | 14,480.00 USD | 0.00 USD | `+36.98%` | `14,758,000,000.00` |
| `Live` | `Short` | `985.50` | 8,590,000.00 USD | 1,100.00 USD | 0.00 USD | `+37.54%` | `1,112,000,000.00` |
| `Live` | `Short` | `990.50` | 8,620,000.00 USD | 28,300.00 USD | 0.00 USD | `+38.24%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 8,720,000.00 USD | 101,390.00 USD | 0.00 USD | `+38.51%` | `102,152,000,000.00` |
| `Live` | `Short` | `993.50` | 8,730,000.00 USD | 15,420.00 USD | 0.00 USD | `+38.65%` | `15,523,000,000.00` |
| `Live` | `Short` | `994.50` | 9,020,000.00 USD | 285,520.00 USD | 0.00 USD | `+38.79%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 9,020,000.00 USD | 313.58 USD | 0.00 USD | `+38.93%` | `315,000,000.00` |
| `Live` | `Short` | `996.50` | 9,020,000.00 USD | 989.52 USD | 0.00 USD | `+39.07%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 9,030,000.00 USD | 8,780.00 USD | 0.00 USD | `+39.21%` | `8,798,000,000.00` |
| `Live` | `Short` | `998.50` | 9,040,000.00 USD | 9,550.00 USD | 0.00 USD | `+39.35%` | `9,569,000,000.00` |
| `Live` | `Short` | `999.50` | 9,080,000.00 USD | 36,850.00 USD | 0.00 USD | `+39.49%` | `36,870,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,080,000.00 USD | 838.93 USD | 0.00 USD | `+40.05%` | `836,000,000.00` |
| `Live` | `Short` | `1005.50` | 9,080,000.00 USD | 4,050.00 USD | 0.00 USD | `+40.33%` | `4,024,000,000.00` |
| `Live` | `Short` | `1007.50` | 9,080,000.00 USD | 301.24 USD | 0.00 USD | `+40.61%` | `299,000,000.00` |
| `Live` | `Short` | `1008.50` | 9,110,000.00 USD | 28,800.00 USD | 0.00 USD | `+40.75%` | `28,558,000,000.00` |
| `Live` | `Short` | `1009.50` | 9,160,000.00 USD | 51,680.00 USD | 0.00 USD | `+40.89%` | `51,191,000,000.00` |
| `Live` | `Short` | `1014.50` | 9,920,000.00 USD | 760,880.00 USD | 0.00 USD | `+41.59%` | `750,000,000,000.00` |
| `Live` | `Short` | `1017.50` | 9,920,000.00 USD | 490.44 USD | 0.00 USD | `+42.00%` | `482,000,000.00` |
| `Live` | `Short` | `1023.50` | 10,220,000.00 USD | 298,410.00 USD | 0.00 USD | `+42.84%` | `291,563,000,000.00` |
| `Live` | `Short` | `1024.50` | 10,220,000.00 USD | 2,850.00 USD | 0.00 USD | `+42.98%` | `2,777,000,000.00` |
| `Live` | `Short` | `1026.50` | 10,220,000.00 USD | 637.46 USD | 0.00 USD | `+43.26%` | `621,000,000.00` |
| `Live` | `Short` | `1037.50` | 10,950,000.00 USD | 723,770.00 USD | 0.00 USD | `+44.80%` | `697,611,000,000.00` |
| `Live` | `Short` | `1039.50` | 10,980,000.00 USD | 32,060.00 USD | 0.00 USD | `+45.07%` | `30,841,000,000.00` |
| `Live` | `Short` | `1046.50` | 11,000,000.00 USD | 15,070.00 USD | 0.00 USD | `+46.05%` | `14,403,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,000,000.00 USD | 500.04 USD | 0.00 USD | `+46.61%` | `476,000,000.00` |
| `Live` | `Short` | `1057.50` | 11,060,000.00 USD | 66,090.00 USD | 0.00 USD | `+47.59%` | `62,500,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,060,000.00 USD | 1,600.00 USD | 0.00 USD | `+48.56%` | `1,500,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,070,000.00 USD | 1,610.00 USD | 0.00 USD | `+49.82%` | `1,500,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,070,000.00 USD | 5,770.00 USD | 0.00 USD | `+51.77%` | `5,310,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,110,000.00 USD | 35,180.00 USD | 0.00 USD | `+51.91%` | `32,321,000,000.00` |
| `Live` | `Short` | `1090.50` | 11,180,000.00 USD | 74,430.00 USD | 0.00 USD | `+52.19%` | `68,249,000,000.00` |
| `Live` | `Short` | `1092.50` | 11,180,000.00 USD | 122.36 USD | 0.00 USD | `+52.47%` | `112,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,370,000.00 USD | 190,680.00 USD | 0.00 USD | `+52.61%` | `174,376,000,000.00` |
| `Live` | `Short` | `1096.50` | 11,370,000.00 USD | 810.31 USD | 0.00 USD | `+53.03%` | `739,000,000.00` |
| `Live` | `Short` | `1116.50` | 11,370,000.00 USD | 149.61 USD | 0.00 USD | `+55.82%` | `134,000,000.00` |
| `Live` | `Short` | `1122.50` | 11,430,000.00 USD | 60,690.00 USD | 0.00 USD | `+56.66%` | `54,065,000,000.00` |
| `Live` | `Short` | `1124.50` | 11,550,000.00 USD | 117,060.00 USD | 0.00 USD | `+56.94%` | `104,104,000,000.00` |
| `Live` | `Short` | `1126.50` | 11,550,000.00 USD | 1,510.00 USD | 0.00 USD | `+57.22%` | `1,337,000,000.00` |
| `Live` | `Short` | `1137.50` | 11,890,000.00 USD | 341,610.00 USD | 0.00 USD | `+58.75%` | `300,314,000,000.00` |
| `Live` | `Short` | `1146.50` | 11,890,000.00 USD | 153.63 USD | 0.00 USD | `+60.01%` | `134,000,000.00` |
| `Live` | `Short` | `1151.50` | 11,910,000.00 USD | 11,690.00 USD | 0.00 USD | `+60.71%` | `10,154,000,000.00` |
| `Live` | `Short` | `1176.50` | 11,910,000.00 USD | 817.67 USD | 0.00 USD | `+64.19%` | `695,000,000.00` |
| `Live` | `Short` | `1178.50` | 11,970,000.00 USD | 66,060.00 USD | 0.00 USD | `+64.47%` | `56,055,000,000.00` |
| `Live` | `Short` | `1179.50` | 11,980,000.00 USD | 3,150.00 USD | 0.00 USD | `+64.61%` | `2,672,000,000.00` |
| `Live` | `Short` | `1186.50` | 12,030,000.00 USD | 57,320.00 USD | 0.00 USD | `+65.59%` | `48,311,000,000.00` |
| `Live` | `Short` | `1191.50` | 12,030,000.00 USD | 168.00 USD | 0.00 USD | `+66.29%` | `141,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,140,000.00 USD | 108,240.00 USD | 0.00 USD | `+67.12%` | `90,387,000,000.00` |
| `Live` | `Short` | `1204.50` | 12,260,000.00 USD | 118,960.00 USD | 0.00 USD | `+68.10%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,260,000.00 USD | 385.19 USD | 0.00 USD | `+68.52%` | `319,000,000.00` |
| `Live` | `Short` | `1209.50` | 12,300,000.00 USD | 42,330.00 USD | 0.00 USD | `+68.80%` | `35,000,000,000.00` |
| `Live` | `Short` | `1210.50` | 12,330,000.00 USD | 30,240.00 USD | 0.00 USD | `+68.94%` | `24,982,000,000.00` |
| `Live` | `Short` | `1222.50` | 12,350,000.00 USD | 21,230.00 USD | 0.00 USD | `+70.61%` | `17,363,000,000.00` |
| `Live` | `Short` | `1224.50` | 12,360,000.00 USD | 4,750.00 USD | 0.00 USD | `+70.89%` | `3,876,000,000.00` |
| `Live` | `Short` | `1233.50` | 12,360,000.00 USD | 1,230.00 USD | 0.00 USD | `+72.15%` | `1,000,000,000.00` |
| `Live` | `Short` | `1237.50` | 12,360,000.00 USD | 198.00 USD | 0.00 USD | `+72.71%` | `160,000,000.00` |
| `Live` | `Short` | `1240.50` | 12,370,000.00 USD | 5,310.00 USD | 0.00 USD | `+73.13%` | `4,284,000,000.00` |
| `Live` | `Short` | `1241.50` | 12,390,000.00 USD | 26,600.00 USD | 0.00 USD | `+73.27%` | `21,429,000,000.00` |
| `Live` | `Short` | `1245.50` | 12,390,000.00 USD | 2,660.00 USD | 0.00 USD | `+73.82%` | `2,134,000,000.00` |
| `Live` | `Short` | `1249.50` | 12,400,000.00 USD | 2,050.00 USD | 0.00 USD | `+74.38%` | `1,644,000,000.00` |
| `Live` | `Short` | `1251.50` | 12,400,000.00 USD | 100.12 USD | 0.00 USD | `+74.66%` | `80,000,000.00` |
| `Live` | `Short` | `1254.50` | 12,400,000.00 USD | 5,010.00 USD | 0.00 USD | `+75.08%` | `3,994,000,000.00` |
| `Live` | `Short` | `1260.50` | 12,430,000.00 USD | 24,470.00 USD | 0.00 USD | `+75.92%` | `19,414,000,000.00` |
| `Live` | `Short` | `1263.50` | 12,430,000.00 USD | 6,850.00 USD | 0.00 USD | `+76.34%` | `5,419,000,000.00` |
| `Live` | `Short` | `1265.50` | 12,550,000.00 USD | 113,890.00 USD | 0.00 USD | `+76.62%` | `90,000,000,000.00` |
| `Live` | `Short` | `1272.50` | 12,550,000.00 USD | 7,330.00 USD | 0.00 USD | `+77.59%` | `5,758,000,000.00` |
| `Live` | `Short` | `1278.50` | 12,620,000.00 USD | 61,530.00 USD | 0.00 USD | `+78.43%` | `48,123,000,000.00` |
| `Live` | `Short` | `1280.50` | 12,620,000.00 USD | 347.02 USD | 0.00 USD | `+78.71%` | `271,000,000.00` |
| `Live` | `Short` | `1284.50` | 12,660,000.00 USD | 38,800.00 USD | 0.00 USD | `+79.27%` | `30,209,000,000.00` |
| `Live` | `Short` | `1291.50` | 12,720,000.00 USD | 61,740.00 USD | 0.00 USD | `+80.24%` | `47,804,000,000.00` |
| `Live` | `Short` | `1293.50` | 14,540,000.00 USD | 1,830,000.00 USD | 0.00 USD | `+80.52%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1295.50` | 14,670,000.00 USD | 129,730.00 USD | 0.00 USD | `+80.80%` | `100,140,000,000.00` |
| `Live` | `Short` | `1298.50` | 14,790,000.00 USD | 110,770.00 USD | 0.00 USD | `+81.22%` | `85,305,000,000.00` |
| `Live` | `Short` | `1299.50` | 14,950,000.00 USD | 164,880.00 USD | 0.00 USD | `+81.36%` | `126,881,000,000.00` |
| `Live` | `Short` | `1309.50` | 14,970,000.00 USD | 19,560.00 USD | 0.00 USD | `+82.76%` | `14,939,000,000.00` |
| `Live` | `Short` | `1319.50` | 14,980,000.00 USD | 14,130.00 USD | 0.00 USD | `+84.15%` | `10,710,000,000.00` |
| `Live` | `Short` | `1327.50` | 14,980,000.00 USD | 138.06 USD | 0.00 USD | `+85.27%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 14,980,000.00 USD | 289.61 USD | 0.00 USD | `+85.41%` | `218,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,040,000.00 USD | 54,070.00 USD | 0.00 USD | `+85.69%` | `40,640,000,000.00` |
| `Live` | `Short` | `1345.50` | 15,040,000.00 USD | 232.77 USD | 0.00 USD | `+87.78%` | `173,000,000.00` |
| `Live` | `Short` | `1352.50` | 15,060,000.00 USD | 19,380.00 USD | 0.00 USD | `+88.76%` | `14,327,000,000.00` |
| `Live` | `Short` | `1358.50` | 15,060,000.00 USD | 498.57 USD | 0.00 USD | `+89.59%` | `367,000,000.00` |
| `Live` | `Short` | `1363.50` | 15,060,000.00 USD | 3,880.00 USD | 0.00 USD | `+90.29%` | `2,846,000,000.00` |
| `Live` | `Short` | `1364.50` | 15,060,000.00 USD | 2,730.00 USD | 0.00 USD | `+90.43%` | `2,000,000,000.00` |
| `Live` | `Short` | `1365.50` | 15,070,000.00 USD | 193.90 USD | 0.00 USD | `+90.57%` | `142,000,000.00` |
| `Live` | `Short` | `1366.50` | 15,070,000.00 USD | 4,100.00 USD | 0.00 USD | `+90.71%` | `3,000,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,070,000.00 USD | 761.70 USD | 0.00 USD | `+90.85%` | `557,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,120,000.00 USD | 46,880.00 USD | 0.00 USD | `+91.13%` | `34,232,000,000.00` |
| `Live` | `Short` | `1382.50` | 15,120,000.00 USD | 1,950.00 USD | 0.00 USD | `+92.94%` | `1,409,000,000.00` |
| `Live` | `Short` | `1386.50` | 15,120,000.00 USD | 4,790.00 USD | 0.00 USD | `+93.50%` | `3,457,000,000.00` |
| `Live` | `Short` | `1390.50` | 15,460,000.00 USD | 340,670.00 USD | 0.00 USD | `+94.06%` | `245,000,000,000.00` |
| `Live` | `Short` | `1405.50` | 15,470,000.00 USD | 4,770.00 USD | 0.00 USD | `+96.15%` | `3,392,000,000.00` |
| `Live` | `Short` | `1408.50` | 15,540,000.00 USD | 70,420.00 USD | 0.00 USD | `+96.57%` | `50,000,000,000.00` |
| `Live` | `Short` | `1421.50` | 15,570,000.00 USD | 31,560.00 USD | 0.00 USD | `+98.39%` | `22,200,000,000.00` |
| `Live` | `Short` | `1431.50` | 15,570,000.00 USD | 360.74 USD | 0.00 USD | `+99.78%` | `252,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 3,300,000.00 USD | 0.00 USD | 475.73 USD | `-79.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 3,300,000.00 USD | 0.00 USD | 2,400.00 USD | `-58.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 3,300,000.00 USD | 0.00 USD | 333.50 USD | `-53.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 3,300,000.00 USD | 0.00 USD | 8,140.00 USD | `-49.69%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 3,290,000.00 USD | 0.00 USD | 5,170.00 USD | `-48.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 3,290,000.00 USD | 0.00 USD | 17,290.00 USD | `-44.11%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 3,270,000.00 USD | 0.00 USD | 25,210.00 USD | `-42.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 3,240,000.00 USD | 0.00 USD | 4,550.00 USD | `-42.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 3,240,000.00 USD | 0.00 USD | 8,180.00 USD | `-40.76%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 3,230,000.00 USD | 0.00 USD | 173.83 USD | `-39.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 3,230,000.00 USD | 0.00 USD | 2,210.00 USD | `-37.83%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 3,230,000.00 USD | 0.00 USD | 698.74 USD | `-36.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 3,230,000.00 USD | 0.00 USD | 2,270.00 USD | `-36.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `457.50` | 3,230,000.00 USD | 0.00 USD | 2,270.00 USD | `-36.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 3,220,000.00 USD | 0.00 USD | 1,750.00 USD | `-36.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 3,220,000.00 USD | 0.00 USD | 3,550.00 USD | `-34.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 3,220,000.00 USD | 0.00 USD | 100.71 USD | `-32.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 3,220,000.00 USD | 0.00 USD | 6,600.00 USD | `-31.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 3,210,000.00 USD | 0.00 USD | 125.06 USD | `-31.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `490.50` | 3,210,000.00 USD | 0.00 USD | 101.53 USD | `-31.55%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 3,210,000.00 USD | 0.00 USD | 2,450.00 USD | `-31.27%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 3,210,000.00 USD | 0.00 USD | 163.01 USD | `-30.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 3,210,000.00 USD | 0.00 USD | 214.78 USD | `-30.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 3,210,000.00 USD | 0.00 USD | 12,610.00 USD | `-30.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 3,200,000.00 USD | 0.00 USD | 42,390.00 USD | `-29.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 3,150,000.00 USD | 0.00 USD | 138.78 USD | `-29.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 3,150,000.00 USD | 0.00 USD | 185.97 USD | `-28.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 3,150,000.00 USD | 0.00 USD | 1,030.00 USD | `-28.06%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 3,150,000.00 USD | 0.00 USD | 125.51 USD | `-27.92%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 3,150,000.00 USD | 0.00 USD | 280.49 USD | `-27.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 3,150,000.00 USD | 0.00 USD | 258.14 USD | `-27.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 3,150,000.00 USD | 0.00 USD | 8,170.00 USD | `-26.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 3,140,000.00 USD | 0.00 USD | 485.16 USD | `-26.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 3,140,000.00 USD | 0.00 USD | 4,650.00 USD | `-25.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 3,140,000.00 USD | 0.00 USD | 1,680.00 USD | `-24.85%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 3,140,000.00 USD | 0.00 USD | 864.80 USD | `-24.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 3,140,000.00 USD | 0.00 USD | 4,130.00 USD | `-23.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 3,130,000.00 USD | 0.00 USD | 366,230.00 USD | `-22.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 2,770,000.00 USD | 0.00 USD | 1,190.00 USD | `-22.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 2,760,000.00 USD | 0.00 USD | 611.05 USD | `-22.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 2,760,000.00 USD | 0.00 USD | 213.52 USD | `-22.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 2,760,000.00 USD | 0.00 USD | 51,260.00 USD | `-22.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 2,710,000.00 USD | 0.00 USD | 292.02 USD | `-21.78%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 2,710,000.00 USD | 0.00 USD | 748.48 USD | `-21.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 2,710,000.00 USD | 0.00 USD | 199.12 USD | `-21.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 2,710,000.00 USD | 0.00 USD | 808.06 USD | `-21.36%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 2,710,000.00 USD | 0.00 USD | 566.50 USD | `-20.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 2,710,000.00 USD | 0.00 USD | 330.85 USD | `-20.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 2,710,000.00 USD | 0.00 USD | 5,680.00 USD | `-20.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 2,700,000.00 USD | 0.00 USD | 569.50 USD | `-20.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 2,700,000.00 USD | 0.00 USD | 774.17 USD | `-20.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 2,700,000.00 USD | 0.00 USD | 1,700.00 USD | `-20.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 2,700,000.00 USD | 0.00 USD | 291.91 USD | `-19.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 2,700,000.00 USD | 0.00 USD | 469.61 USD | `-19.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 2,700,000.00 USD | 0.00 USD | 289.98 USD | `-19.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 2,700,000.00 USD | 0.00 USD | 285.86 USD | `-19.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 2,700,000.00 USD | 0.00 USD | 289.17 USD | `-19.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 2,700,000.00 USD | 0.00 USD | 6,750.00 USD | `-18.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 2,690,000.00 USD | 0.00 USD | 1,240.00 USD | `-18.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 2,690,000.00 USD | 0.00 USD | 6,980.00 USD | `-18.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 2,680,000.00 USD | 0.00 USD | 287.67 USD | `-18.57%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 2,680,000.00 USD | 0.00 USD | 763.94 USD | `-18.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 2,680,000.00 USD | 0.00 USD | 542.76 USD | `-18.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 2,680,000.00 USD | 0.00 USD | 34,020.00 USD | `-18.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 2,650,000.00 USD | 0.00 USD | 830,190.00 USD | `-18.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 1,820,000.00 USD | 0.00 USD | 287.78 USD | `-17.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 1,820,000.00 USD | 0.00 USD | 252.31 USD | `-17.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 1,820,000.00 USD | 0.00 USD | 540.31 USD | `-17.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 1,820,000.00 USD | 0.00 USD | 698.56 USD | `-17.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 1,820,000.00 USD | 0.00 USD | 1,160.00 USD | `-17.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 1,820,000.00 USD | 0.00 USD | 119.30 USD | `-16.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 1,820,000.00 USD | 0.00 USD | 222.87 USD | `-16.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 1,820,000.00 USD | 0.00 USD | 244.79 USD | `-16.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 1,810,000.00 USD | 0.00 USD | 41,990.00 USD | `-16.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 1,770,000.00 USD | 0.00 USD | 1,590.00 USD | `-16.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 1,770,000.00 USD | 0.00 USD | 46,760.00 USD | `-15.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 1,720,000.00 USD | 0.00 USD | 123,870.00 USD | `-15.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 1,600,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.64%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 1,600,000.00 USD | 0.00 USD | 2,610.00 USD | `-15.50%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 1,600,000.00 USD | 0.00 USD | 18,380.00 USD | `-15.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 1,580,000.00 USD | 0.00 USD | 30,480.00 USD | `-14.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 1,550,000.00 USD | 0.00 USD | 11,650.00 USD | `-14.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 1,540,000.00 USD | 0.00 USD | 4,470.00 USD | `-14.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 1,530,000.00 USD | 0.00 USD | 1,380.00 USD | `-14.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 1,530,000.00 USD | 0.00 USD | 269.15 USD | `-14.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 1,530,000.00 USD | 0.00 USD | 1,740.00 USD | `-14.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 1,530,000.00 USD | 0.00 USD | 120.83 USD | `-13.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 1,530,000.00 USD | 0.00 USD | 13,170.00 USD | `-13.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 1,510,000.00 USD | 0.00 USD | 2,150.00 USD | `-13.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 1,510,000.00 USD | 0.00 USD | 219.47 USD | `-12.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 1,510,000.00 USD | 0.00 USD | 445.27 USD | `-12.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 1,510,000.00 USD | 0.00 USD | 445.98 USD | `-12.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 1,510,000.00 USD | 0.00 USD | 694.79 USD | `-12.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 1,510,000.00 USD | 0.00 USD | 916.15 USD | `-12.43%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 1,510,000.00 USD | 0.00 USD | 746.03 USD | `-12.29%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 1,510,000.00 USD | 0.00 USD | 2,740.00 USD | `-12.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 1,510,000.00 USD | 0.00 USD | 861.26 USD | `-12.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 1,510,000.00 USD | 0.00 USD | 179.98 USD | `-11.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 1,510,000.00 USD | 0.00 USD | 1,100.00 USD | `-11.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 1,500,000.00 USD | 0.00 USD | 164.08 USD | `-11.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 1,500,000.00 USD | 0.00 USD | 2,550.00 USD | `-11.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 1,500,000.00 USD | 0.00 USD | 6,760.00 USD | `-11.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 1,490,000.00 USD | 0.00 USD | 2,730.00 USD | `-11.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 1,490,000.00 USD | 0.00 USD | 3,640.00 USD | `-10.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 1,490,000.00 USD | 0.00 USD | 384.98 USD | `-10.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 1,490,000.00 USD | 0.00 USD | 429.78 USD | `-10.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 1,490,000.00 USD | 0.00 USD | 352.18 USD | `-10.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 1,490,000.00 USD | 0.00 USD | 357.87 USD | `-10.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 1,490,000.00 USD | 0.00 USD | 1,830.00 USD | `-10.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 1,480,000.00 USD | 0.00 USD | 3,790.00 USD | `-10.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 1,480,000.00 USD | 0.00 USD | 10,640.00 USD | `-9.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 1,470,000.00 USD | 0.00 USD | 971.04 USD | `-9.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 1,470,000.00 USD | 0.00 USD | 1,800.00 USD | `-9.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 1,470,000.00 USD | 0.00 USD | 107.17 USD | `-9.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 1,470,000.00 USD | 0.00 USD | 32,440.00 USD | `-9.22%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 1,440,000.00 USD | 0.00 USD | 5,890.00 USD | `-9.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 1,430,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 1,430,000.00 USD | 0.00 USD | 308.92 USD | `-8.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 1,430,000.00 USD | 0.00 USD | 165.84 USD | `-8.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 1,430,000.00 USD | 0.00 USD | 2,330.00 USD | `-8.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 1,420,000.00 USD | 0.00 USD | 110.46 USD | `-8.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 1,420,000.00 USD | 0.00 USD | 1,320.00 USD | `-8.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 1,420,000.00 USD | 0.00 USD | 13,060.00 USD | `-7.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 1,410,000.00 USD | 0.00 USD | 6,470.00 USD | `-7.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 1,400,000.00 USD | 0.00 USD | 11,310.00 USD | `-7.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 1,390,000.00 USD | 0.00 USD | 7,780.00 USD | `-7.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 1,380,000.00 USD | 0.00 USD | 2,840.00 USD | `-7.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 1,380,000.00 USD | 0.00 USD | 713.01 USD | `-7.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 1,380,000.00 USD | 0.00 USD | 576.32 USD | `-7.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 1,380,000.00 USD | 0.00 USD | 24,530.00 USD | `-6.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 1,360,000.00 USD | 0.00 USD | 10,740.00 USD | `-6.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 1,350,000.00 USD | 0.00 USD | 719.97 USD | `-6.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 1,340,000.00 USD | 0.00 USD | 2,390.00 USD | `-6.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 1,340,000.00 USD | 0.00 USD | 126,240.00 USD | `-6.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 1,220,000.00 USD | 0.00 USD | 2,340.00 USD | `-6.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 1,210,000.00 USD | 0.00 USD | 1,500.00 USD | `-6.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 1,210,000.00 USD | 0.00 USD | 3,460.00 USD | `-6.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 1,210,000.00 USD | 0.00 USD | 1,470.00 USD | `-5.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 1,210,000.00 USD | 0.00 USD | 10,640.00 USD | `-5.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 1,200,000.00 USD | 0.00 USD | 56,170.00 USD | `-5.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 1,140,000.00 USD | 0.00 USD | 39,650.00 USD | `-5.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 1,100,000.00 USD | 0.00 USD | 825.73 USD | `-5.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 1,100,000.00 USD | 0.00 USD | 5,250.00 USD | `-5.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 1,090,000.00 USD | 0.00 USD | 1,950.00 USD | `-5.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 1,090,000.00 USD | 0.00 USD | 146.52 USD | `-4.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 1,090,000.00 USD | 0.00 USD | 4,740.00 USD | `-4.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,090,000.00 USD | 0.00 USD | 171,850.00 USD | `-4.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 915,690.00 USD | 0.00 USD | 171,120.00 USD | `-4.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 744,560.00 USD | 0.00 USD | 11,030.00 USD | `-4.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 733,540.00 USD | 0.00 USD | 530.66 USD | `-4.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 733,010.00 USD | 0.00 USD | 653.81 USD | `-4.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 732,350.00 USD | 0.00 USD | 262.32 USD | `-3.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 732,090.00 USD | 0.00 USD | 532.98 USD | `-3.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 731,560.00 USD | 0.00 USD | 3,860.00 USD | `-3.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 727,700.00 USD | 0.00 USD | 190,350.00 USD | `-3.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 537,340.00 USD | 0.00 USD | 4,450.00 USD | `-3.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 532,890.00 USD | 0.00 USD | 7,180.00 USD | `-3.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 525,720.00 USD | 0.00 USD | 1,540.00 USD | `-3.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 524,180.00 USD | 0.00 USD | 10,080.00 USD | `-2.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 514,100.00 USD | 0.00 USD | 2,200.00 USD | `-2.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 511,890.00 USD | 0.00 USD | 47,550.00 USD | `-2.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 464,340.00 USD | 0.00 USD | 15,500.00 USD | `-2.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 448,850.00 USD | 0.00 USD | 38,470.00 USD | `-2.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 410,380.00 USD | 0.00 USD | 42,040.00 USD | `-2.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 368,340.00 USD | 0.00 USD | 329.71 USD | `-2.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 368,010.00 USD | 0.00 USD | 29,960.00 USD | `-1.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 338,040.00 USD | 0.00 USD | 3,850.00 USD | `-1.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 334,200.00 USD | 0.00 USD | 86,660.00 USD | `-1.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 247,540.00 USD | 0.00 USD | 640.59 USD | `-1.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 246,900.00 USD | 0.00 USD | 11,290.00 USD | `-1.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 235,610.00 USD | 0.00 USD | 13,270.00 USD | `-1.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 222,340.00 USD | 0.00 USD | 2,130.00 USD | `-1.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 220,210.00 USD | 0.00 USD | 247.62 USD | `-0.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 219,960.00 USD | 0.00 USD | 39,230.00 USD | `-0.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 180,740.00 USD | 0.00 USD | 2,460.00 USD | `-0.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 178,270.00 USD | 0.00 USD | 1,640.00 USD | `-0.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 176,630.00 USD | 0.00 USD | 3,180.00 USD | `-0.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 173,450.00 USD | 0.00 USD | 1,660.00 USD | `-0.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 171,790.00 USD | 0.00 USD | 3,100.00 USD | `-0.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 168,690.00 USD | 0.00 USD | 168,690.00 USD | `-0.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | `+0.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 81,910.00 USD | 80,870.00 USD | 0.00 USD | `+0.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 152,150.00 USD | 70,240.00 USD | 0.00 USD | `+0.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 176,190.00 USD | 24,040.00 USD | 0.00 USD | `+0.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 221,450.00 USD | 45,260.00 USD | 0.00 USD | `+0.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 226,420.00 USD | 4,970.00 USD | 0.00 USD | `+0.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 236,670.00 USD | 10,250.00 USD | 0.00 USD | `+0.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 262,020.00 USD | 25,350.00 USD | 0.00 USD | `+1.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 353,870.00 USD | 91,850.00 USD | 0.00 USD | `+1.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 354,370.00 USD | 501.28 USD | 0.00 USD | `+1.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 373,670.00 USD | 19,300.00 USD | 0.00 USD | `+1.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 428,920.00 USD | 55,250.00 USD | 0.00 USD | `+1.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 569,730.00 USD | 140,810.00 USD | 0.00 USD | `+1.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 577,590.00 USD | 7,860.00 USD | 0.00 USD | `+1.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 797,550.00 USD | 219,960.00 USD | 0.00 USD | `+2.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 799,830.00 USD | 2,280.00 USD | 0.00 USD | `+2.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,290,000.00 USD | 487,680.00 USD | 0.00 USD | `+2.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,290,000.00 USD | 7,480.00 USD | 0.00 USD | `+2.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,330,000.00 USD | 33,960.00 USD | 0.00 USD | `+2.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,340,000.00 USD | 6,860.00 USD | 0.00 USD | `+2.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,340,000.00 USD | 3,970.00 USD | 0.00 USD | `+2.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,350,000.00 USD | 13,270.00 USD | 0.00 USD | `+3.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,350,000.00 USD | 790.53 USD | 0.00 USD | `+3.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,360,000.00 USD | 2,440.00 USD | 0.00 USD | `+3.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,360,000.00 USD | 3,840.00 USD | 0.00 USD | `+3.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,370,000.00 USD | 11,030.00 USD | 0.00 USD | `+3.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,370,000.00 USD | 2,460.00 USD | 0.00 USD | `+3.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,580,000.00 USD | 203,810.00 USD | 0.00 USD | `+3.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,580,000.00 USD | 5,390.00 USD | 0.00 USD | `+4.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,590,000.00 USD | 4,790.00 USD | 0.00 USD | `+4.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,590,000.00 USD | 1,070.00 USD | 0.00 USD | `+4.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,590,000.00 USD | 279.19 USD | 0.00 USD | `+4.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,590,000.00 USD | 704.53 USD | 0.00 USD | `+4.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,590,000.00 USD | 123.83 USD | 0.00 USD | `+4.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,600,000.00 USD | 8,720.00 USD | 0.00 USD | `+4.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,600,000.00 USD | 2,730.00 USD | 0.00 USD | `+5.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,600,000.00 USD | 629.17 USD | 0.00 USD | `+5.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,650,000.00 USD | 47,160.00 USD | 0.00 USD | `+5.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,650,000.00 USD | 4,420.00 USD | 0.00 USD | `+5.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,670,000.00 USD | 13,590.00 USD | 0.00 USD | `+5.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,810,000.00 USD | 142,940.00 USD | 0.00 USD | `+5.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,810,000.00 USD | 2,790.00 USD | 0.00 USD | `+5.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 1,810,000.00 USD | 325.07 USD | 0.00 USD | `+6.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,100,000.00 USD | 288,360.00 USD | 0.00 USD | `+6.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,110,000.00 USD | 11,460.00 USD | 0.00 USD | `+6.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,110,000.00 USD | 274.50 USD | 0.00 USD | `+6.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,160,000.00 USD | 46,140.00 USD | 0.00 USD | `+6.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,160,000.00 USD | 323.38 USD | 0.00 USD | `+6.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,220,000.00 USD | 60,710.00 USD | 0.00 USD | `+6.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,220,000.00 USD | 331.13 USD | 0.00 USD | `+6.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,690,000.00 USD | 468,310.00 USD | 0.00 USD | `+7.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,690,000.00 USD | 421.91 USD | 0.00 USD | `+7.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,690,000.00 USD | 171.60 USD | 0.00 USD | `+7.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,690,000.00 USD | 1,540.00 USD | 0.00 USD | `+7.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,690,000.00 USD | 242.25 USD | 0.00 USD | `+7.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,700,000.00 USD | 12,050.00 USD | 0.00 USD | `+7.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,700,000.00 USD | 656.70 USD | 0.00 USD | `+7.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,710,000.00 USD | 9,680.00 USD | 0.00 USD | `+8.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,720,000.00 USD | 4,570.00 USD | 0.00 USD | `+8.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,730,000.00 USD | 14,230.00 USD | 0.00 USD | `+8.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,750,000.00 USD | 15,690.00 USD | 0.00 USD | `+8.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,760,000.00 USD | 9,990.00 USD | 0.00 USD | `+8.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,760,000.00 USD | 132.52 USD | 0.00 USD | `+8.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,780,000.00 USD | 24,280.00 USD | 0.00 USD | `+8.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,780,000.00 USD | 2,050.00 USD | 0.00 USD | `+9.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,790,000.00 USD | 1,900.00 USD | 0.00 USD | `+9.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,790,000.00 USD | 101.07 USD | 0.00 USD | `+9.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,790,000.00 USD | 102.77 USD | 0.00 USD | `+9.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,790,000.00 USD | 559.28 USD | 0.00 USD | `+9.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,800,000.00 USD | 11,990.00 USD | 0.00 USD | `+9.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,800,000.00 USD | 2,260.00 USD | 0.00 USD | `+9.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,800,000.00 USD | 133.26 USD | 0.00 USD | `+10.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,810,000.00 USD | 4,190.00 USD | 0.00 USD | `+10.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,810,000.00 USD | 704.44 USD | 0.00 USD | `+10.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,810,000.00 USD | 4,360.00 USD | 0.00 USD | `+10.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,810,000.00 USD | 1,450.00 USD | 0.00 USD | `+10.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,820,000.00 USD | 3,630.00 USD | 0.00 USD | `+10.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,820,000.00 USD | 3,390.00 USD | 0.00 USD | `+11.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,820,000.00 USD | 154.52 USD | 0.00 USD | `+11.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,820,000.00 USD | 1,260.00 USD | 0.00 USD | `+11.58%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,830,000.00 USD | 12,890.00 USD | 0.00 USD | `+11.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,830,000.00 USD | 120.22 USD | 0.00 USD | `+11.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,830,000.00 USD | 803.50 USD | 0.00 USD | `+12.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,830,000.00 USD | 120.02 USD | 0.00 USD | `+12.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,840,000.00 USD | 1,300.00 USD | 0.00 USD | `+12.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,840,000.00 USD | 5,010.00 USD | 0.00 USD | `+12.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,840,000.00 USD | 242.04 USD | 0.00 USD | `+12.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 2,860,000.00 USD | 15,790.00 USD | 0.00 USD | `+13.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 2,860,000.00 USD | 374.10 USD | 0.00 USD | `+13.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 2,860,000.00 USD | 844.19 USD | 0.00 USD | `+13.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 2,860,000.00 USD | 109.82 USD | 0.00 USD | `+13.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 2,860,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 2,860,000.00 USD | 984.70 USD | 0.00 USD | `+13.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 2,860,000.00 USD | 162.68 USD | 0.00 USD | `+14.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 2,870,000.00 USD | 5,990.00 USD | 0.00 USD | `+14.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 2,880,000.00 USD | 8,230.00 USD | 0.00 USD | `+14.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 2,880,000.00 USD | 408.13 USD | 0.00 USD | `+15.07%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 2,880,000.00 USD | 672.77 USD | 0.00 USD | `+15.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 2,880,000.00 USD | 276.38 USD | 0.00 USD | `+15.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 2,880,000.00 USD | 1,800.00 USD | 0.00 USD | `+15.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 2,920,000.00 USD | 35,850.00 USD | 0.00 USD | `+15.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 2,920,000.00 USD | 1,050.00 USD | 0.00 USD | `+16.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 2,920,000.00 USD | 187.15 USD | 0.00 USD | `+16.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 2,920,000.00 USD | 372.24 USD | 0.00 USD | `+16.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 2,920,000.00 USD | 326.62 USD | 0.00 USD | `+16.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 2,920,000.00 USD | 296.34 USD | 0.00 USD | `+17.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 2,920,000.00 USD | 441.26 USD | 0.00 USD | `+17.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 2,920,000.00 USD | 329.87 USD | 0.00 USD | `+17.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 2,920,000.00 USD | 425.97 USD | 0.00 USD | `+17.72%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 2,920,000.00 USD | 1,770.00 USD | 0.00 USD | `+17.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 2,920,000.00 USD | 2,550.00 USD | 0.00 USD | `+18.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 2,940,000.00 USD | 11,650.00 USD | 0.00 USD | `+18.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 2,940,000.00 USD | 102.30 USD | 0.00 USD | `+18.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 2,940,000.00 USD | 137.57 USD | 0.00 USD | `+19.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 2,940,000.00 USD | 1,200.00 USD | 0.00 USD | `+19.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 2,940,000.00 USD | 1,160.00 USD | 0.00 USD | `+20.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 2,940,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 2,940,000.00 USD | 874.73 USD | 0.00 USD | `+20.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 2,940,000.00 USD | 2,970.00 USD | 0.00 USD | `+20.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 2,950,000.00 USD | 3,460.00 USD | 0.00 USD | `+20.79%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 2,950,000.00 USD | 2,610.00 USD | 0.00 USD | `+21.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 2,950,000.00 USD | 228.07 USD | 0.00 USD | `+21.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 2,950,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 3,010,000.00 USD | 54,820.00 USD | 0.00 USD | `+23.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 3,010,000.00 USD | 266.55 USD | 0.00 USD | `+24.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 3,010,000.00 USD | 690.14 USD | 0.00 USD | `+24.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 3,010,000.00 USD | 605.33 USD | 0.00 USD | `+24.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `895.50` | 3,010,000.00 USD | 130.74 USD | 0.00 USD | `+24.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `898.50` | 3,010,000.00 USD | 101.53 USD | 0.00 USD | `+25.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,140,000.00 USD | 132,720.00 USD | 0.00 USD | `+25.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,140,000.00 USD | 167.33 USD | 0.00 USD | `+26.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,140,000.00 USD | 1,640.00 USD | 0.00 USD | `+26.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,140,000.00 USD | 908.02 USD | 0.00 USD | `+27.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,150,000.00 USD | 4,150.00 USD | 0.00 USD | `+27.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,150,000.00 USD | 533.99 USD | 0.00 USD | `+28.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,150,000.00 USD | 166.43 USD | 0.00 USD | `+28.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,150,000.00 USD | 463.01 USD | 0.00 USD | `+28.47%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,150,000.00 USD | 320.57 USD | 0.00 USD | `+29.30%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,150,000.00 USD | 552.72 USD | 0.00 USD | `+29.86%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,150,000.00 USD | 196.03 USD | 0.00 USD | `+30.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,150,000.00 USD | 287.20 USD | 0.00 USD | `+30.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,150,000.00 USD | 782.14 USD | 0.00 USD | `+33.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,150,000.00 USD | 498.94 USD | 0.00 USD | `+33.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,150,000.00 USD | 964.50 USD | 0.00 USD | `+34.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,150,000.00 USD | 1,930.00 USD | 0.00 USD | `+34.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,150,000.00 USD | 293.25 USD | 0.00 USD | `+36.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,160,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,160,000.00 USD | 109.93 USD | 0.00 USD | `+36.98%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,160,000.00 USD | 439.09 USD | 0.00 USD | `+37.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,160,000.00 USD | 2,590.00 USD | 0.00 USD | `+37.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,160,000.00 USD | 145.34 USD | 0.00 USD | `+38.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,160,000.00 USD | 1,740.00 USD | 0.00 USD | `+39.21%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,160,000.00 USD | 3,990.00 USD | 0.00 USD | `+39.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,170,000.00 USD | 938.53 USD | 0.00 USD | `+39.49%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,180,000.00 USD | 11,810.00 USD | 0.00 USD | `+39.63%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,180,000.00 USD | 203.50 USD | 0.00 USD | `+42.00%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,180,000.00 USD | 148.99 USD | 0.00 USD | `+42.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,180,000.00 USD | 149.87 USD | 0.00 USD | `+43.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,180,000.00 USD | 150.45 USD | 0.00 USD | `+43.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,180,000.00 USD | 195.51 USD | 0.00 USD | `+45.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,180,000.00 USD | 149.60 USD | 0.00 USD | `+47.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,180,000.00 USD | 156.58 USD | 0.00 USD | `+49.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,180,000.00 USD | 278.43 USD | 0.00 USD | `+53.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,180,000.00 USD | 555.75 USD | 0.00 USD | `+55.12%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,180,000.00 USD | 165.93 USD | 0.00 USD | `+58.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,180,000.00 USD | 167.39 USD | 0.00 USD | `+60.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,240,000.00 USD | 62,330.00 USD | 0.00 USD | `+67.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,240,000.00 USD | 1,250.00 USD | 0.00 USD | `+67.82%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,240,000.00 USD | 235.49 USD | 0.00 USD | `+71.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,250,000.00 USD | 3,580.00 USD | 0.00 USD | `+71.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,250,000.00 USD | 421.42 USD | 0.00 USD | `+74.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,250,000.00 USD | 3,750.00 USD | 0.00 USD | `+78.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,250,000.00 USD | 133.64 USD | 0.00 USD | `+81.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,250,000.00 USD | 685.36 USD | 0.00 USD | `+81.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,310,000.00 USD | 58,230.00 USD | 0.00 USD | `+85.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,390,000.00 USD | 80,850.00 USD | 0.00 USD | `+87.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,400,000.00 USD | 6,210.00 USD | 0.00 USD | `+89.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,400,000.00 USD | 349.06 USD | 0.00 USD | `+90.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,400,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,420,000.00 USD | 19,210.00 USD | 0.00 USD | `+91.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,420,000.00 USD | 425.19 USD | 0.00 USD | `+93.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,420,000.00 USD | 3,850.00 USD | 0.00 USD | `+95.46%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `643.90` | 46,900,000.00 USD | 0.00 USD | 46,900,000.00 USD | 40,470.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.70` | 46,860,000.00 USD | 0.00 USD | 46,860,000.00 USD | 381,780.00 USD | 14,440.00 USD | 341,610.00 USD |
| `1D` | `645.50` | 46,120,000.00 USD | 0.00 USD | 46,120,000.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `646.30` | 46,100,000.00 USD | 0.00 USD | 46,100,000.00 USD | 156,000.00 USD | 11,780.00 USD | 184,540.00 USD |
| `1D` | `647.10` | 45,740,000.00 USD | 0.00 USD | 45,740,000.00 USD | 204,530.00 USD | 31,640.00 USD | 33,810.00 USD |
| `1D` | `647.90` | 45,470,000.00 USD | 0.00 USD | 45,470,000.00 USD | 136,750.00 USD | 4,630.00 USD | 7,150.00 USD |
| `1D` | `648.70` | 45,330,000.00 USD | 0.00 USD | 45,330,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `649.50` | 45,230,000.00 USD | 0.00 USD | 45,230,000.00 USD | 96,580.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `650.30` | 45,140,000.00 USD | 0.00 USD | 45,140,000.00 USD | 17,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.10` | 45,120,000.00 USD | 0.00 USD | 45,120,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.90` | 44,940,000.00 USD | 0.00 USD | 44,940,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `652.70` | 44,840,000.00 USD | 0.00 USD | 44,840,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.50` | 44,810,000.00 USD | 0.00 USD | 44,810,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.30` | 44,740,000.00 USD | 0.00 USD | 44,740,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.10` | 44,670,000.00 USD | 0.00 USD | 44,670,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.90` | 44,580,000.00 USD | 0.00 USD | 44,580,000.00 USD | 209,270.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.70` | 44,370,000.00 USD | 0.00 USD | 44,370,000.00 USD | 113,920.00 USD | 40,970.00 USD | 825,700.00 USD |
| `1D` | `657.50` | 43,390,000.00 USD | 0.00 USD | 43,390,000.00 USD | 248,110.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `658.30` | 43,120,000.00 USD | 0.00 USD | 43,120,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.10` | 42,310,000.00 USD | 0.00 USD | 42,310,000.00 USD | 119,820.00 USD | 7,460.00 USD | 81,440.00 USD |
| `1D` | `659.90` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 69,270.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `660.70` | 42,020,000.00 USD | 0.00 USD | 42,020,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `661.50` | 41,840,000.00 USD | 0.00 USD | 41,840,000.00 USD | 468,220.00 USD | 19,460.00 USD | 0.00 USD |
| `1D` | `662.30` | 41,350,000.00 USD | 0.00 USD | 41,350,000.00 USD | 165,160.00 USD | 136,330.00 USD | 0.00 USD |
| `1D` | `663.10` | 41,050,000.00 USD | 0.00 USD | 41,050,000.00 USD | 259,470.00 USD | 5,000.00 USD | 44,630.00 USD |
| `1D` | `663.90` | 40,740,000.00 USD | 0.00 USD | 40,740,000.00 USD | 45,960.00 USD | 64,390.00 USD | 64,090.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.70` | 40,570,000.00 USD | 0.00 USD | 40,570,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.50` | 39,180,000.00 USD | 0.00 USD | 39,180,000.00 USD | 695,850.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.30` | 38,470,000.00 USD | 0.00 USD | 38,470,000.00 USD | 294,510.00 USD | 93,680.00 USD | 750,630.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.10` | 37,330,000.00 USD | 0.00 USD | 37,330,000.00 USD | 892,590.00 USD | 25,280.00 USD | 40,700.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `667.90` | 36,370,000.00 USD | 0.00 USD | 36,370,000.00 USD | 385,370.00 USD | 150,850.00 USD | 0.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `668.70` | 35,830,000.00 USD | 0.00 USD | 35,830,000.00 USD | 771,830.00 USD | 39,300.00 USD | 3,620.00 USD |
| `1D` | `669.50` | 35,020,000.00 USD | 0.00 USD | 35,020,000.00 USD | 481,670.00 USD | 61,020.00 USD | 29,910.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.30` | 34,450,000.00 USD | 0.00 USD | 34,450,000.00 USD | 661,320.00 USD | 50,060.00 USD | 1,500,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.10` | 32,240,000.00 USD | 0.00 USD | 32,240,000.00 USD | 557,780.00 USD | 13,720.00 USD | 45,290.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.90` | 31,620,000.00 USD | 0.00 USD | 31,620,000.00 USD | 1,970,000.00 USD | 18,180.00 USD | 6,520.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.70` | 29,630,000.00 USD | 0.00 USD | 29,630,000.00 USD | 136,910.00 USD | 63,880.00 USD | 857,540.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.50` | 28,570,000.00 USD | 0.00 USD | 28,570,000.00 USD | 330,660.00 USD | 300,600.00 USD | 1,560,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.30` | 26,370,000.00 USD | 0.00 USD | 26,370,000.00 USD | 370,460.00 USD | 421,810.00 USD | 104,800.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.10` | 25,470,000.00 USD | 0.00 USD | 25,470,000.00 USD | 2,080,000.00 USD | 77,990.00 USD | 392,190.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `675.90` | 22,930,000.00 USD | 0.00 USD | 22,930,000.00 USD | 647,750.00 USD | 351,990.00 USD | 228,720.00 USD |
| `1D` | `676.70` | 21,700,000.00 USD | 0.00 USD | 21,700,000.00 USD | 296,630.00 USD | 184,180.00 USD | 276,610.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.50` | 20,940,000.00 USD | 0.00 USD | 20,940,000.00 USD | 304,270.00 USD | 145,960.00 USD | 250,200.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.30` | 20,240,000.00 USD | 0.00 USD | 20,240,000.00 USD | 1,270,000.00 USD | 140,140.00 USD | 209,020.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.10` | 18,620,000.00 USD | 0.00 USD | 18,620,000.00 USD | 167,390.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.90` | 18,450,000.00 USD | 0.00 USD | 18,450,000.00 USD | 1,430,000.00 USD | 247,960.00 USD | 298,080.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.70` | 16,480,000.00 USD | 0.00 USD | 16,480,000.00 USD | 169,080.00 USD | 126,150.00 USD | 187,330.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.50` | 16,000,000.00 USD | 0.00 USD | 16,000,000.00 USD | 488,760.00 USD | 414,700.00 USD | 0.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.30` | 15,090,000.00 USD | 0.00 USD | 15,090,000.00 USD | 323,390.00 USD | 16,030.00 USD | 0.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.10` | 14,750,000.00 USD | 0.00 USD | 14,750,000.00 USD | 662,310.00 USD | 59,430.00 USD | 37,900.00 USD |
| `1D` | `683.90` | 13,990,000.00 USD | 0.00 USD | 13,990,000.00 USD | 405,890.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.70` | 13,550,000.00 USD | 0.00 USD | 13,550,000.00 USD | 138,250.00 USD | 58,650.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.50` | 13,350,000.00 USD | 0.00 USD | 13,350,000.00 USD | 522,300.00 USD | 32,890.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.30` | 12,800,000.00 USD | 0.00 USD | 12,800,000.00 USD | 937,160.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.10` | 11,860,000.00 USD | 0.00 USD | 11,860,000.00 USD | 902,200.00 USD | 136,370.00 USD | 98,790.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.90` | 10,720,000.00 USD | 0.00 USD | 10,720,000.00 USD | 113,770.00 USD | 45,630.00 USD | 180,340.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.70` | 10,380,000.00 USD | 0.00 USD | 10,380,000.00 USD | 420,000.00 USD | 107,080.00 USD | 490,120.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.50` | 9,360,000.00 USD | 0.00 USD | 9,360,000.00 USD | 77,980.00 USD | 37,360.00 USD | 760,670.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `690.30` | 8,490,000.00 USD | 0.00 USD | 8,490,000.00 USD | 31,110.00 USD | 63,780.00 USD | 212,990.00 USD |
| `1D` | `691.10` | 8,180,000.00 USD | 0.00 USD | 8,180,000.00 USD | 0.00 USD | 129,500.00 USD | 17,880.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.90` | 8,030,000.00 USD | 0.00 USD | 8,030,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.50` | 8,010,000.00 USD | 0.00 USD | 8,010,000.00 USD | 0.00 USD | 60,140.00 USD | 273,200.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.30` | 7,680,000.00 USD | 0.00 USD | 7,680,000.00 USD | 0.00 USD | 117,630.00 USD | 180,380.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.10` | 7,380,000.00 USD | 0.00 USD | 7,380,000.00 USD | 239,550.00 USD | 64,240.00 USD | 175,000.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `695.90` | 6,900,000.00 USD | 0.00 USD | 6,900,000.00 USD | 0.00 USD | 34,140.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.70` | 6,870,000.00 USD | 0.00 USD | 6,870,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `698.30` | 6,770,000.00 USD | 0.00 USD | 6,770,000.00 USD | 479,860.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `699.10` | 6,290,000.00 USD | 0.00 USD | 6,290,000.00 USD | 0.00 USD | 31,670.00 USD | 42,650.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.70` | 6,220,000.00 USD | 0.00 USD | 6,220,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.50` | 6,030,000.00 USD | 0.00 USD | 6,030,000.00 USD | 0.00 USD | 131,450.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.30` | 5,890,000.00 USD | 0.00 USD | 5,890,000.00 USD | 227,540.00 USD | 39,170.00 USD | 67,790.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.10` | 5,560,000.00 USD | 0.00 USD | 5,560,000.00 USD | 434,010.00 USD | 58,910.00 USD | 298,770.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `703.90` | 4,770,000.00 USD | 0.00 USD | 4,770,000.00 USD | 155,960.00 USD | 12,800.00 USD | 376,910.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `704.70` | 4,220,000.00 USD | 0.00 USD | 4,220,000.00 USD | 62,230.00 USD | 23,130.00 USD | 231,880.00 USD |
| `1D` | `705.50` | 3,900,000.00 USD | 0.00 USD | 3,900,000.00 USD | 0.00 USD | 0.00 USD | 121,600.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `706.30` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 237,450.00 USD | 0.00 USD | 123,170.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `707.90` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.70` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 382,110.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `1D` | `710.30` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 292,560.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.10` | 2,550,000.00 USD | 0.00 USD | 2,550,000.00 USD | 401,530.00 USD | 0.00 USD | 37,900.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `711.90` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD |
| `1D` | `712.70` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.10` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 317,060.00 USD | 415,380.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.90` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 1,060,000.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `717.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.10` | 82,030.00 USD | 82,030.00 USD | 0.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD |
| `1D` | `719.90` | 166,220.00 USD | 166,220.00 USD | 0.00 USD | 60,590.00 USD | 23,600.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.70` | 578,690.00 USD | 578,690.00 USD | 0.00 USD | 207,940.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.50` | 816,230.00 USD | 816,230.00 USD | 0.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.30` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 28,010.00 USD | 123,420.00 USD | 391,200.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.10` | 2,010,000.00 USD | 2,010,000.00 USD | 0.00 USD | 191,050.00 USD | 283,040.00 USD | 176,360.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.90` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 380,140.00 USD | 359,630.00 USD | 88,480.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.70` | 3,230,000.00 USD | 3,230,000.00 USD | 0.00 USD | 345,070.00 USD | 45,850.00 USD | 0.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.50` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 289,330.00 USD | 120,790.00 USD | 38,340.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `726.30` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD |
| `1D` | `727.10` | 4,520,000.00 USD | 4,520,000.00 USD | 0.00 USD | 502,440.00 USD | 75,120.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.90` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 136,640.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.70` | 5,200,000.00 USD | 5,200,000.00 USD | 0.00 USD | 235,850.00 USD | 48,340.00 USD | 207,690.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.50` | 6,060,000.00 USD | 6,060,000.00 USD | 0.00 USD | 171,580.00 USD | 233,920.00 USD | 458,580.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.30` | 8,250,000.00 USD | 8,250,000.00 USD | 0.00 USD | 1,690,000.00 USD | 351,100.00 USD | 141,300.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.10` | 11,950,000.00 USD | 11,950,000.00 USD | 0.00 USD | 1,410,000.00 USD | 132,680.00 USD | 2,160,000.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `731.90` | 12,820,000.00 USD | 12,820,000.00 USD | 0.00 USD | 206,640.00 USD | 152,280.00 USD | 502,920.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.70` | 15,800,000.00 USD | 15,800,000.00 USD | 0.00 USD | 1,610,000.00 USD | 119,840.00 USD | 1,250,000.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `733.50` | 16,510,000.00 USD | 16,510,000.00 USD | 0.00 USD | 62,230.00 USD | 317,290.00 USD | 334,930.00 USD |
| `1D` | `734.30` | 17,140,000.00 USD | 17,140,000.00 USD | 0.00 USD | 481,120.00 USD | 11,800.00 USD | 132,930.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.10` | 17,980,000.00 USD | 17,980,000.00 USD | 0.00 USD | 634,640.00 USD | 210,260.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.90` | 19,470,000.00 USD | 19,470,000.00 USD | 0.00 USD | 702,000.00 USD | 57,600.00 USD | 727,530.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.70` | 20,110,000.00 USD | 20,110,000.00 USD | 0.00 USD | 494,810.00 USD | 58,820.00 USD | 90,190.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.50` | 20,700,000.00 USD | 20,700,000.00 USD | 0.00 USD | 376,720.00 USD | 126,150.00 USD | 87,500.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.30` | 21,400,000.00 USD | 21,400,000.00 USD | 0.00 USD | 610,590.00 USD | 85,790.00 USD | 0.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.10` | 22,510,000.00 USD | 22,510,000.00 USD | 0.00 USD | 157,860.00 USD | 16,030.00 USD | 934,700.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `739.90` | 22,940,000.00 USD | 22,940,000.00 USD | 0.00 USD | 399,360.00 USD | 31,860.00 USD | 0.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `740.70` | 23,350,000.00 USD | 23,350,000.00 USD | 0.00 USD | 246,020.00 USD | 166,390.00 USD | 0.00 USD |
| `1D` | `741.50` | 23,970,000.00 USD | 23,970,000.00 USD | 0.00 USD | 622,710.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `742.30` | 23,990,000.00 USD | 23,990,000.00 USD | 0.00 USD | 0.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.10` | 24,240,000.00 USD | 24,240,000.00 USD | 0.00 USD | 250,640.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.90` | 24,800,000.00 USD | 24,800,000.00 USD | 0.00 USD | 16,710.00 USD | 106,580.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.70` | 26,630,000.00 USD | 26,630,000.00 USD | 0.00 USD | 910,100.00 USD | 65,730.00 USD | 854,020.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.50` | 27,400,000.00 USD | 27,400,000.00 USD | 0.00 USD | 617,380.00 USD | 94,190.00 USD | 60,660.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.30` | 28,130,000.00 USD | 28,130,000.00 USD | 0.00 USD | 451,300.00 USD | 61,130.00 USD | 219,610.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.10` | 29,610,000.00 USD | 29,610,000.00 USD | 0.00 USD | 521,800.00 USD | 74,380.00 USD | 881,280.00 USD |
| `1D` | `747.90` | 29,990,000.00 USD | 29,990,000.00 USD | 0.00 USD | 163,850.00 USD | 84,260.00 USD | 133,250.00 USD |
| `1D` | `748.70` | 30,410,000.00 USD | 30,410,000.00 USD | 0.00 USD | 395,410.00 USD | 0.00 USD | 17,880.00 USD |
| `1D` | `749.50` | 30,810,000.00 USD | 30,810,000.00 USD | 0.00 USD | 406,170.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.30` | 30,860,000.00 USD | 30,860,000.00 USD | 0.00 USD | 51,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.10` | 30,950,000.00 USD | 30,950,000.00 USD | 0.00 USD | 88,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.90` | 31,500,000.00 USD | 31,500,000.00 USD | 0.00 USD | 86,270.00 USD | 25,010.00 USD | 433,820.00 USD |
| `1D` | `752.70` | 31,950,000.00 USD | 31,950,000.00 USD | 0.00 USD | 349,490.00 USD | 0.00 USD | 105,800.00 USD |
| `1D` | `753.50` | 32,380,000.00 USD | 32,380,000.00 USD | 0.00 USD | 158,100.00 USD | 3,810.00 USD | 262,160.00 USD |
| `1D` | `754.30` | 32,890,000.00 USD | 32,890,000.00 USD | 0.00 USD | 396,550.00 USD | 70,850.00 USD | 43,990.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.10` | 33,280,000.00 USD | 33,280,000.00 USD | 0.00 USD | 157,340.00 USD | 192,190.00 USD | 37,120.00 USD |
| `1D` | `755.90` | 33,980,000.00 USD | 33,980,000.00 USD | 0.00 USD | 576,050.00 USD | 62,280.00 USD | 66,220.00 USD |
| `1D` | `756.70` | 34,140,000.00 USD | 34,140,000.00 USD | 0.00 USD | 87,170.00 USD | 24,970.00 USD | 49,060.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.50` | 34,550,000.00 USD | 34,550,000.00 USD | 0.00 USD | 198,850.00 USD | 179,910.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.30` | 35,560,000.00 USD | 35,560,000.00 USD | 0.00 USD | 757,140.00 USD | 34,450.00 USD | 218,280.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.10` | 36,600,000.00 USD | 36,600,000.00 USD | 0.00 USD | 861,530.00 USD | 117,910.00 USD | 54,810.00 USD |
| `1D` | `759.90` | 36,970,000.00 USD | 36,970,000.00 USD | 0.00 USD | 335,910.00 USD | 21,070.00 USD | 15,370.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.70` | 37,380,000.00 USD | 37,380,000.00 USD | 0.00 USD | 301,710.00 USD | 52,630.00 USD | 53,580.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.50` | 38,340,000.00 USD | 38,340,000.00 USD | 0.00 USD | 720,170.00 USD | 8,690.00 USD | 232,870.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `762.30` | 38,660,000.00 USD | 38,660,000.00 USD | 0.00 USD | 97,090.00 USD | 124,370.00 USD | 98,750.00 USD |
| `1D` | `763.10` | 41,280,000.00 USD | 41,280,000.00 USD | 0.00 USD | 1,940,000.00 USD | 154,730.00 USD | 523,900.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.90` | 42,610,000.00 USD | 42,610,000.00 USD | 0.00 USD | 996,680.00 USD | 110,320.00 USD | 222,330.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.70` | 44,180,000.00 USD | 44,180,000.00 USD | 0.00 USD | 1,190,000.00 USD | 210,400.00 USD | 167,240.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.50` | 44,970,000.00 USD | 44,970,000.00 USD | 0.00 USD | 557,990.00 USD | 81,400.00 USD | 147,690.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.30` | 46,430,000.00 USD | 46,430,000.00 USD | 0.00 USD | 868,340.00 USD | 233,150.00 USD | 358,440.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.10` | 48,970,000.00 USD | 48,970,000.00 USD | 0.00 USD | 2,280,000.00 USD | 30,760.00 USD | 230,710.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `767.90` | 50,460,000.00 USD | 50,460,000.00 USD | 0.00 USD | 1,110,000.00 USD | 102,730.00 USD | 281,670.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.70` | 51,200,000.00 USD | 51,200,000.00 USD | 0.00 USD | 650,590.00 USD | 54,840.00 USD | 36,980.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `769.50` | 51,670,000.00 USD | 51,670,000.00 USD | 0.00 USD | 411,850.00 USD | 49,670.00 USD | 8,460.00 USD |
| `1D` | `770.30` | 51,940,000.00 USD | 51,940,000.00 USD | 0.00 USD | 167,380.00 USD | 75,090.00 USD | 28,450.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.10` | 52,520,000.00 USD | 52,520,000.00 USD | 0.00 USD | 156,280.00 USD | 56,560.00 USD | 361,060.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.90` | 53,310,000.00 USD | 53,310,000.00 USD | 0.00 USD | 140,150.00 USD | 70,310.00 USD | 582,120.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.70` | 53,680,000.00 USD | 53,680,000.00 USD | 0.00 USD | 221,230.00 USD | 134,200.00 USD | 16,360.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.50` | 54,380,000.00 USD | 54,380,000.00 USD | 0.00 USD | 618,270.00 USD | 12,950.00 USD | 68,320.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.30` | 54,980,000.00 USD | 54,980,000.00 USD | 0.00 USD | 583,550.00 USD | 11,780.00 USD | 1,360.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.10` | 55,170,000.00 USD | 55,170,000.00 USD | 0.00 USD | 67,380.00 USD | 34,120.00 USD | 86,160.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `775.90` | 55,340,000.00 USD | 55,340,000.00 USD | 0.00 USD | 98,960.00 USD | 24,070.00 USD | 49,120.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `776.70` | 55,570,000.00 USD | 55,570,000.00 USD | 0.00 USD | 152,260.00 USD | 4,350.00 USD | 73,050.00 USD |
| `1D` | `777.50` | 56,180,000.00 USD | 56,180,000.00 USD | 0.00 USD | 462,430.00 USD | 112,090.00 USD | 36,270.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.30` | 57,250,000.00 USD | 57,250,000.00 USD | 0.00 USD | 673,890.00 USD | 52,880.00 USD | 347,410.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.10` | 58,140,000.00 USD | 58,140,000.00 USD | 0.00 USD | 689,070.00 USD | 73,260.00 USD | 123,210.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.90` | 58,550,000.00 USD | 58,550,000.00 USD | 0.00 USD | 275,710.00 USD | 87,740.00 USD | 46,700.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.70` | 59,060,000.00 USD | 59,060,000.00 USD | 0.00 USD | 373,710.00 USD | 53,100.00 USD | 79,750.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.50` | 59,720,000.00 USD | 59,720,000.00 USD | 0.00 USD | 363,950.00 USD | 99,050.00 USD | 197,320.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.30` | 61,090,000.00 USD | 61,090,000.00 USD | 0.00 USD | 1,090,000.00 USD | 23,530.00 USD | 259,020.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.10` | 61,810,000.00 USD | 61,810,000.00 USD | 0.00 USD | 591,390.00 USD | 38,390.00 USD | 88,920.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `783.90` | 62,060,000.00 USD | 62,060,000.00 USD | 0.00 USD | 225,990.00 USD | 14,770.00 USD | 8,400.00 USD |
| `1D` | `784.70` | 62,480,000.00 USD | 62,480,000.00 USD | 0.00 USD | 421,270.00 USD | 2,690.00 USD | 0.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.50` | 62,560,000.00 USD | 62,560,000.00 USD | 0.00 USD | 73,390.00 USD | 4,490.00 USD | 0.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.30` | 62,630,000.00 USD | 62,630,000.00 USD | 0.00 USD | 73,970.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.10` | 62,650,000.00 USD | 62,650,000.00 USD | 0.00 USD | 17,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.90` | 63,380,000.00 USD | 63,380,000.00 USD | 0.00 USD | 379,320.00 USD | 14,440.00 USD | 341,610.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.70` | 63,440,000.00 USD | 63,440,000.00 USD | 0.00 USD | 55,460.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.50` | 63,650,000.00 USD | 63,650,000.00 USD | 0.00 USD | 158,750.00 USD | 11,780.00 USD | 34,900.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 279,010.00 USD | 2,560.00 USD | 162,050.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.10` | 64,320,000.00 USD | 64,320,000.00 USD | 0.00 USD | 172,930.00 USD | 33,700.00 USD | 21,390.00 USD |
| `1D` | `791.90` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 70,860.00 USD | 0.00 USD | 7,150.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.70` | 64,520,000.00 USD | 64,520,000.00 USD | 0.00 USD | 123,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.50` | 64,540,000.00 USD | 64,540,000.00 USD | 0.00 USD | 25,500.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 0.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 0.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD |
| `7D` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 0.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD |
| `7D` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 0.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 0.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 0.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 0.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 0.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD |
| `7D` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 0.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD |
| `7D` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 0.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 0.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 0.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD |
| `7D` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 0.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD |
| `7D` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 0.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD |
| `7D` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 0.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD |
| `7D` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 0.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD |
| `7D` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 0.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD |
| `7D` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 0.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD |
| `7D` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 0.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD |
| `7D` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 0.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD |
| `7D` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 0.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD |
| `7D` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 0.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD |
| `7D` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 0.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD |
| `7D` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 0.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD |
| `7D` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 0.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD |
| `7D` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 0.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD |
| `7D` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 0.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD |
| `7D` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 0.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD |
| `7D` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 0.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD |
| `7D` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 0.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD |
| `7D` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 0.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD |
| `7D` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 0.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `7D` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 0.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD |
| `7D` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 0.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD |
| `7D` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 0.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD |
| `7D` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 0.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD |
| `7D` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 0.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD |
| `7D` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 0.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD |
| `7D` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 0.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD |
| `7D` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 0.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD |
| `7D` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 0.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD |
| `7D` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 0.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD |

- **Multi-Timeframe Forced Liquidations Summary Table (22_Forced_Liquidations_MTF.parquet)**:
| Timeframe | Dominant Side | Long Liq (USD) | Short Liq (USD) | Total Liq (USD) | Net Liq Delta (USD) | Orders Count | Window (UTC) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| MTF | Balanced | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0 | Current Candle |


---

## 7. Derivatives Sentiment, Long/Short Positioning & 12-Venue Funding Rates
*(Sources: 5_OI.parquet, 5_Funding_Rate.parquet, 6_Funding_Fee_Settlement.parquet, 3_Exchanges_LS_Ratio_15M/1H/4H.parquet)*
- **Open Interest Profile & Capitalization (5_OI.parquet)**:
  * Total Open Interest: `1.32B` | Total OI Tokens: `1,845,388.7 BNB`
  * 1h OI Change: `-0.30%` | 4h OI Change: `-1.38%` | 24h OI Change: `+5.53%`
  * Exchange Breakdown: Binance=`572.03M` | Bybit=`137.76M` | OKX=`65.23M` | Hyperliquid=`70.37M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-138.03K` | Last 24h: `-51.15K` | Last 3d: `142.23K` | Last 7d: `346.08K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0594%` |
| **USDT Bybit** | `-0.0707%` | **USDT KuCoin** | `-0.0086%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `-0.0163%` | **USDT Bitget** | `-0.0094%` |
| **CoinM Binance** | `0.1134%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `49.69%` | `50.31%` | `0.99` | 66,660,000.00 USD |
| `15M` | `Binance` | `50.28%` | `49.72%` | `1.01` | 20,780,000.00 USD |
| `15M` | `OKX` | `52.41%` | `47.59%` | `1.10` | 10,710,000.00 USD |
| `15M` | `Bybit` | `39.22%` | `60.78%` | `0.65` | 7,240,000.00 USD |
| `15M` | `KuCoin` | `46.91%` | `53.09%` | `0.88` | 407,170.00 USD |
| `15M` | `Gate` | `51.55%` | `48.45%` | `1.06` | 5,720,000.00 USD |
| `15M` | `Bitget` | `51.79%` | `48.21%` | `1.07` | 2,340,000.00 USD |
| `15M` | `BingX` | `45.97%` | `54.03%` | `0.85` | 2,630,000.00 USD |
| `15M` | `MEXC` | `66.71%` | `33.29%` | `2.00` | 4,390,000.00 USD |
| `15M` | `Bitunix` | `53.28%` | `46.72%` | `1.14` | 4,400,000.00 USD |
| `15M` | `Hyperliquid` | `44.46%` | `55.54%` | `0.80` | 2,130,000.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `55.61%` | `44.39%` | `1.25` | 455,890.00 USD |
| `15M` | `Crypto.com` | `58.89%` | `41.11%` | `1.43` | 136,880.00 USD |
| `15M` | `WhiteBIT` | `99.94%` | `0.06%` | `1665.67` | 1,050,000.00 USD |
| `15M` | `HTX` | `54.13%` | `45.87%` | `1.18` | 49,730.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `51.53%` | `48.47%` | `1.06` | 673,900.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `19.29%` | `80.71%` | `0.24` | 3,540,000.00 USD |
| `15M` | `Whale Positions` | `50.28%` | `49.72%` | `1.01` | 20,780,000.00 USD |
| `15M` | `Global Accounts` | `49.69%` | `50.31%` | `0.99` | 66,660,000.00 USD |
| `1H` | `BNB` | `46.43%` | `53.57%` | `0.87` | 303,950,000.00 USD |
| `1H` | `Binance` | `45.5%` | `54.5%` | `0.83` | 86,650,000.00 USD |
| `1H` | `OKX` | `46.36%` | `53.64%` | `0.86` | 58,630,000.00 USD |
| `1H` | `Bybit` | `43.13%` | `56.87%` | `0.76` | 37,960,000.00 USD |
| `1H` | `KuCoin` | `45.54%` | `54.46%` | `0.84` | 1,410,000.00 USD |
| `1H` | `Gate` | `52.92%` | `47.08%` | `1.12` | 23,220,000.00 USD |
| `1H` | `Bitget` | `40.24%` | `59.76%` | `0.67` | 13,300,000.00 USD |
| `1H` | `BingX` | `50.19%` | `49.81%` | `1.01` | 13,280,000.00 USD |
| `1H` | `MEXC` | `38.82%` | `61.18%` | `0.63` | 23,650,000.00 USD |
| `1H` | `Bitunix` | `47.39%` | `52.61%` | `0.90` | 19,490,000.00 USD |
| `1H` | `Hyperliquid` | `55.6%` | `44.4%` | `1.25` | 12,210,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `51.04%` | `48.96%` | `1.04` | 1,750,000.00 USD |
| `1H` | `Crypto.com` | `55.36%` | `44.64%` | `1.24` | 448,850.00 USD |
| `1H` | `WhiteBIT` | `99.64%` | `0.36%` | `276.78` | 3,500,000.00 USD |
| `1H` | `HTX` | `58.98%` | `41.02%` | `1.44` | 564,830.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `46.49%` | `53.51%` | `0.87` | 2,150,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `35.08%` | `64.92%` | `0.54` | 5,730,000.00 USD |
| `1H` | `Whale Positions` | `45.5%` | `54.5%` | `0.83` | 86,650,000.00 USD |
| `1H` | `Global Accounts` | `46.43%` | `53.57%` | `0.87` | 303,950,000.00 USD |
| `4H` | `BNB` | `51.05%` | `48.95%` | `1.04` | 1,330,000,000.00 USD |
| `4H` | `Binance` | `51.98%` | `48.02%` | `1.08` | 414,880,000.00 USD |
| `4H` | `OKX` | `53.61%` | `46.39%` | `1.16` | 268,820,000.00 USD |
| `4H` | `Bybit` | `50.44%` | `49.56%` | `1.02` | 140,260,000.00 USD |
| `4H` | `KuCoin` | `54.4%` | `45.6%` | `1.19` | 9,030,000.00 USD |
| `4H` | `Gate` | `53.09%` | `46.91%` | `1.13` | 84,120,000.00 USD |
| `4H` | `Bitget` | `51.91%` | `48.09%` | `1.08` | 52,410,000.00 USD |
| `4H` | `BingX` | `47.94%` | `52.06%` | `0.92` | 51,850,000.00 USD |
| `4H` | `MEXC` | `38.48%` | `61.52%` | `0.63` | 110,590,000.00 USD |
| `4H` | `Bitunix` | `50.63%` | `49.37%` | `1.03` | 75,530,000.00 USD |
| `4H` | `Hyperliquid` | `49.18%` | `50.82%` | `0.97` | 63,580,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `49.86%` | `50.14%` | `0.99` | 9,530,000.00 USD |
| `4H` | `Crypto.com` | `53.79%` | `46.21%` | `1.16` | 1,970,000.00 USD |
| `4H` | `WhiteBIT` | `88.21%` | `11.79%` | `7.48` | 13,730,000.00 USD |
| `4H` | `HTX` | `59.42%` | `40.58%` | `1.46` | 2,490,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `72.49%` | `27.51%` | `2.64` | 99,020.00 USD |
| `4H` | `Aster` | `56.87%` | `43.13%` | `1.32` | 12,430,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `44.06%` | `55.94%` | `0.79` | 18,790,000.00 USD |
| `4H` | `Whale Positions` | `51.98%` | `48.02%` | `1.08` | 414,880,000.00 USD |
| `4H` | `Global Accounts` | `51.05%` | `48.95%` | `1.04` | 1,330,000,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `5:00 UTC` | `718.65` | `718.30` | `718.65` | `719.85` | `716.85` | 14,406,892.83 USD | 6,892,738.14 USD | 7,514,154.69 USD | -621,416.55 USD | `-4.31%` | `1B / 0S` |
| `0:00 UTC` | `716.85` | `716.98` | `716.85` | `719.55` | `715.05` | 10,882,676.97 USD | 3,981,765.95 USD | 6,900,911.02 USD | -2,919,145.07 USD | `-26.82%` | `0B / 0S` |
| `5:00 UTC` | `717.15` | `717.39` | `717.15` | `718.65` | `716.25` | 6,978,599.94 USD | 3,350,532.71 USD | 3,628,067.23 USD | -277,534.53 USD | `-3.98%` | `0B / 0S` |
| `0:00 UTC` | `717.45` | `717.74` | `717.45` | `719.55` | `716.55` | 5,355,538.86 USD | 2,861,377.69 USD | 2,494,161.17 USD | 367,216.51 USD | `+6.86%` | `2B / 1S` |
| `5:00 UTC` | `717.45` | `717.28` | `717.45` | `718.05` | `716.55` | 4,945,586.67 USD | 2,313,018.42 USD | 2,632,568.25 USD | -319,549.83 USD | `-6.46%` | `0B / 2S` |
| `0:00 UTC` | `719.85` | `719.92` | `719.85` | `721.65` | `716.55` | 8,783,632.79 USD | 5,084,805.58 USD | 3,698,827.21 USD | 1,385,978.37 USD | `+15.78%` | `3B / 1S` |
| `5:00 UTC` | `718.65` | `718.49` | `718.65` | `719.55` | `717.45` | 6,099,294.65 USD | 2,396,548.55 USD | 3,702,746.10 USD | -1,306,197.54 USD | `-21.42%` | `0B / 1S` |
| `0:00 UTC` | `718.95` | `718.35` | `718.95` | `719.55` | `716.85` | 4,905,756.58 USD | 2,037,050.94 USD | 2,868,705.64 USD | -831,654.70 USD | `-16.95%` | `0B / 3S` |
| `5:00 UTC` | `718.35` | `717.49` | `718.35` | `718.95` | `715.95` | 6,887,062.43 USD | 1,808,092.75 USD | 5,078,969.68 USD | -3,270,876.93 USD | `-47.49%` | `0B / 3S` |
| `0:00 UTC` | `715.95` | `716.26` | `715.95` | `717.45` | `715.65` | 3,660,193.51 USD | 1,568,611.32 USD | 2,091,582.19 USD | -522,970.88 USD | `-14.29%` | `0B / 1S` |

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
| `5m` | 59,650.00 USD | -264,050.00 USD | **`DISTRIBUTION`** |
| `15m` | -314,330.00 USD | -785,550.00 USD | **`DISTRIBUTION`** |
| `30m` | 66,210.00 USD | -4,000,000.00 USD | **`DISTRIBUTION`** |
| `1h` | -1,450,000.00 USD | -5,840,000.00 USD | **`DISTRIBUTION`** |
| `2h` | -226,830.00 USD | -3,640,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -2,190,000.00 USD | -8,690,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -5,480,000.00 USD | -10,110,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -13,270,000.00 USD | 3,410,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -29,060,000.00 USD | -65,620,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -32,190,000.00 USD | -82,880,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -58,260,000.00 USD | -112,510,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -157,650,000.00 USD | -436,600,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`+59.65K` | 15m=`-314.33K` | 1h=`-1.45M` | 24h=`-32.19M`
* Futures Capital Netflows: 5m=`-264.05K` | 15m=`-785.55K` | 1h=`-5.84M` | 24h=`-82.88M`
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
  * `2026-10-30 11:03:46 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:38:46 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:37:46 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:39:46 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:39:46 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:39:46 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:39:46 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `688.02` (Risk Distance: `10.93` pts)
  * +2.5R Take Profit: `726.28`
  * Mathematical Lot Sizing: **`0.91 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `715.55` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `726.48` (Risk Distance: `10.93` pts)
  * +2.5R Take Profit: `688.22`
  * Mathematical Lot Sizing: **`0.91 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`721.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
