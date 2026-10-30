# 🏛️ SOVEREIGN CANDIDATE DOSSIER: BNB
**Canonical Key**: `BNB` | **Broker Instrument**: `BNBUSD.p` | **Asset Class**: `Crypto Major`
**Timestamp**: `2026-10-30 11:29:21 IST` (`2026-10-30 05:59:21 UTC`) | **Execution Engine**: `Antigravity Sovereign Dossier Engine v3.3 (100% 43-Feed Parquet Lake)`

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
  * Session VWAP: `701.00` | VWAP Z-Score: `+1.24` (Regime: `BALANCED_FAIR_VALUE`)
  * 14-Period ATR: `5.27` (Volatility Regime: `NORMAL_COMPRESSION`)
  * 14-Period RSI: `54.53` (State: `NEUTRAL`)
- **Multi-Sigma VWAP Dispersion Grid (Mean Reversion & Volatility Boundaries)**:
  * Upper +3.00σ Band: `732.21` | Lower -3.00σ Band: `669.80`
  * Upper +2.51σ Band: `727.12` | Lower -2.51σ Band: `674.89`
  * Upper +2.01σ Band: `721.91` | Lower -2.01σ Band: `680.09`
  * Upper +2.00σ Band: `721.81` | Lower -2.00σ Band: `680.20`
  * Upper +1.28σ Band: `714.32` | Lower -1.28σ Band: `687.69`
  * Upper +1.00σ Band: `711.41` | Lower -1.00σ Band: `690.60`
- **Moving Average Ribbon & Trend Slopes**:
  * Fast EMA Array: EMA-9=`713.35` | EMA-20=`710.42` (Slope: `+0.0000`)
  * Core Structural Array: EMA-50=`714.91` (Slope: `+0.0000`) | EMA-100=`724.64`
  * Institutional Anchors: EMA-144=`729.53` | EMA-200=`732.93` (Slope: `-0.3513`) | EMA-233=`734.49`
- **Range Boundaries**: 24H High=`756.00` | 24H Low=`677.20` | Weekly High=`760.90` | Weekly Low=`677.20`

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
| `5m` | `719.49` | `719.66` | `718.66` | `718.78` | `1,894` | 1,362,235.38 USD | -146,378.52 USD | `-10.75%` | -41,960,376.78 USD | `+0.04` | **`BEARISH`** | `DELTA ALIGNED` |
| `5m` | `718.77` | `719.24` | `718.00` | `718.00` | `1,845` | 1,326,420.19 USD | -4,371.74 USD | `-0.33%` | -41,964,748.52 USD | `+0.26` | **`BEARISH`** | `NEUTRAL CHOP` |
| `5m` | `718.00` | `718.31` | `716.84` | `717.51` | `2,507` | 1,798,840.33 USD | -713,606.65 USD | `-39.67%` | -42,678,355.17 USD | `-1.01` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `15m` | `717.32` | `721.67` | `716.64` | `719.01` | `12,201` | 8,783,632.79 USD | 1,385,978.37 USD | `+15.78%` | -40,507,800.71 USD | `+0.92` | **`BULLISH`** | `AGGRESSIVE BUYING` |
| `15m` | `719.01` | `719.50` | `717.47` | `719.49` | `8,489` | 6,099,294.65 USD | -1,306,197.54 USD | `-21.42%` | -41,813,998.25 USD | `-0.28` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `15m` | `719.49` | `719.66` | `716.84` | `717.48` | `6,254` | 4,493,121.11 USD | -868,346.25 USD | `-19.33%` | -42,682,344.51 USD | `+0.00` | **`BEARISH`** | `AGGRESSIVE SELLING` |
| `1h` | `710.57` | `719.84` | `708.09` | `719.55` | `75,178` | 53,681,760.72 USD | 2,189,785.10 USD | `+4.08%` | -37,453,136.79 USD | `+0.38` | **`BULLISH`** | `NEUTRAL CHOP` |
| `1h` | `719.56` | `719.60` | `715.13` | `717.32` | `39,263` | 28,162,402.44 USD | -3,149,012.91 USD | `-11.18%` | -40,602,149.70 USD | `-0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `1h` | `717.32` | `721.67` | `716.64` | `717.25` | `26,960` | 19,387,734.01 USD | -800,222.19 USD | `-4.13%` | -41,402,371.88 USD | `+0.00` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `717.25` | `66,223` | 47,550,136.45 USD | -3,949,235.09 USD | `-8.31%` | -32,691,883.81 USD | `+0.18` | **`BEARISH`** | `DELTA ALIGNED` |
| `4h` | `740.45` | `753.64` | `739.55` | `750.62` | `148,938` | 111,099,080.67 USD | 8,045,498.44 USD | `+7.24%` | -2,294,794.05 USD | `+1.00` | **`BULLISH`** | `DELTA ALIGNED` |
| `4h` | `750.62` | `754.90` | `743.07` | `745.33` | `88,414` | 66,199,547.89 USD | 232,195.88 USD | `+0.35%` | -2,062,598.17 USD | `+0.12` | **`BULLISH`** | `BULLISH ABSORPTION` |
| `4h` | `745.34` | `745.53` | `677.76` | `697.96` | `1,556,116` | 1,101,338,590.19 USD | -7,502,511.31 USD | `-0.68%` | -9,565,109.48 USD | `-0.71` | **`BEARISH`** | `NEUTRAL CHOP` |
| `4h` | `697.96` | `719.84` | `681.03` | `719.55` | `524,764` | 367,784,698.06 USD | -19,177,539.23 USD | `-5.21%` | -28,742,648.71 USD | `-1.45` | **`BEARISH`** | `BEARISH ABSORPTION` |
| `4h` | `719.56` | `721.67` | `715.13` | `717.26` | `72,352` | 51,950,600.91 USD | -5,790,498.45 USD | `-11.15%` | -34,533,147.17 USD | `-0.00` | **`BEARISH`** | `DELTA ALIGNED` |

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
| `BID` | `716.34` | `2449000000.0000` | 1,754.32 USD | 65,561.03 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `716.35` | `910000000.0000` | 651.88 USD | 63,806.72 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `716.37` | `2797000000.0000` | 2,003.69 USD | 63,154.84 USD | `1 orders` | `-0.07%` | `-` |
| `BID` | `716.38` | `2515000000.0000` | 1,801.70 USD | 61,151.15 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `716.39` | `17447000000.0000` | 12,498.86 USD | 59,349.46 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `716.40` | `676000000.0000` | 484.29 USD | 46,850.60 USD | `1 orders` | `-0.06%` | `-` |
| `BID` | `716.43` | `455000000.0000` | 325.98 USD | 46,366.31 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `716.45` | `40769000000.0000` | 29,208.95 USD | 46,040.34 USD | `2 orders` | `-0.06%` | `-` |
| `BID` | `716.46` | `9647000000.0000` | 6,911.69 USD | 16,831.39 USD | `3 orders` | `-0.05%` | `-` |
| `BID` | `716.49` | `469000000.0000` | 336.03 USD | 9,919.70 USD | `2 orders` | `-0.05%` | `-` |
| `BID` | `716.53` | `902000000.0000` | 646.31 USD | 9,583.66 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `716.54` | `1000000000.0000` | 716.54 USD | 8,937.35 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `716.57` | `2327000000.0000` | 1,667.46 USD | 8,220.81 USD | `1 orders` | `-0.04%` | `-` |
| `BID` | `716.59` | `2514000000.0000` | 1,801.51 USD | 6,553.36 USD | `2 orders` | `-0.04%` | `-` |
| `BID` | `716.61` | `902000000.0000` | 646.38 USD | 4,751.85 USD | `1 orders` | `-0.03%` | `-` |
| `BID` | `716.67` | `902000000.0000` | 646.44 USD | 4,105.47 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `716.68` | `1738000000.0000` | 1,245.59 USD | 3,459.03 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `716.72` | `895000000.0000` | 641.46 USD | 2,213.44 USD | `1 orders` | `-0.02%` | `-` |
| `BID` | `716.78` | `895000000.0000` | 641.52 USD | 1,571.98 USD | `1 orders` | `-0.01%` | `-` |
| `BID` | `716.84` | `1298000000.0000` | 930.46 USD | 930.46 USD | `2 orders` | `-0.00%` | `-` |
| `ASK` | `716.85` | `1797000000.0000` | 1,288.18 USD | 1,288.18 USD | `2 orders` | `+0.00%` | `-` |
| `MID_SPREAD` | `716.85` | `0.0000` | 0.00 USD | 0.00 USD | `Mid: USD 716.85` | `0.00%` | `-` |
| `ASK` | `716.87` | `1397000000.0000` | 1,001.47 USD | 2,289.65 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `716.88` | `9299000000.0000` | 6,666.27 USD | 8,955.91 USD | `1 orders` | `+0.00%` | `-` |
| `ASK` | `716.89` | `1000000000.0000` | 716.89 USD | 9,672.80 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.91` | `902000000.0000` | 646.65 USD | 10,319.46 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.94` | `12678000000.0000` | 9,089.37 USD | 19,408.82 USD | `3 orders` | `+0.01%` | `-` |
| `ASK` | `716.95` | `140000000.0000` | 100.37 USD | 19,509.20 USD | `1 orders` | `+0.01%` | `-` |
| `ASK` | `716.96` | `4117000000.0000` | 2,951.72 USD | 22,460.92 USD | `5 orders` | `+0.02%` | `-` |
| `ASK` | `716.98` | `420000000.0000` | 301.13 USD | 22,762.05 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `717.00` | `420000000.0000` | 301.14 USD | 23,063.19 USD | `3 orders` | `+0.02%` | `-` |
| `ASK` | `717.01` | `7113000000.0000` | 5,100.09 USD | 28,163.28 USD | `2 orders` | `+0.02%` | `-` |
| `ASK` | `717.02` | `902000000.0000` | 646.75 USD | 28,810.04 USD | `1 orders` | `+0.02%` | `-` |
| `ASK` | `717.03` | `15495000000.0000` | 11,110.38 USD | 39,920.42 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `717.04` | `2963000000.0000` | 2,124.59 USD | 42,045.00 USD | `3 orders` | `+0.03%` | `-` |
| `ASK` | `717.05` | `180000000.0000` | 129.07 USD | 42,174.07 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `717.07` | `2632000000.0000` | 1,887.33 USD | 44,061.40 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `717.08` | `25152000000.0000` | 18,036.00 USD | 62,097.40 USD | `1 orders` | `+0.03%` | `-` |
| `ASK` | `717.10` | `902000000.0000` | 646.82 USD | 62,744.22 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `717.13` | `15000000.0000` | 10.76 USD | 62,754.98 USD | `1 orders` | `+0.04%` | `-` |
| `ASK` | `717.14` | `18592000000.0000` | 13,333.07 USD | 76,088.05 USD | `1 orders` | `+0.04%` | `-` |

- **Hyperdash Verified Whale Orders & Resting Book (12_Hyperdash.parquet)**:
| Section | Side / Type | Price (USD) | Size | Notional (USD) | Detail | Wallet / Address | Timestamp (IST) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `UNIVERSE_FLOW` | `NEUTRAL` | `0.000000` | `0.00` | 0.00 USD | `Delta: +0` | `None` | `2026-10-30 11:24:14 IST` |

- **Hyperliquid Analysis Trader Leaderboard & Leveraged Positions (4_Hyperliquid_Analysis.parquet)**:
| Rank | User Display | Side | Position (USD) | Size (Tokens) | Entry Price | Current Price | Liq Price | PnL (USD) | PnL (%) | Leverage |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `781` | `0xea00...a918` | `LONG` | 2,936,196.50 USD | `4,098,429,000,000.00` | `787.24` | `716.30` | `0.000000` | -290,230.28 USD | `-9.88%` | `5X Cross` |
| `898` | `0xfe7c...b7ae` | `LONG` | 2,501,713.49 USD | `3,491,575,000,000.00` | `686.05` | `716.30` | `0.000000` | 106,302.63 USD | `+4.25%` | `10X Cross` |
| `1056` | `0x7d0c...1b28` | `LONG` | 2,056,278.17 USD | `2,870,654,000,000.00` | `703.77` | `716.30` | `0.000000` | 35,999.99 USD | `+1.75%` | `10X Cross` |
| `1089` | `0x27c9...d65d` | `LONG` | 2,001,345.07 USD | `2,794,004,000,000.00` | `700.84` | `716.30` | `153.64` | 43,186.69 USD | `+2.16%` | `10X Cross` |
| `1169` | `0x7737...bf66` | `SHORT` | 1,896,886.95 USD | `2,646,179,000,000.00` | `752.73` | `716.30` | `6846.94` | 94,983.63 USD | `+5.01%` | `10X Cross` |
| `1343` | `0x51f6...2b39` | `LONG` | 1,605,021.29 USD | `2,240,711,000,000.00` | `703.00` | `716.30` | `100.54` | 29,811.64 USD | `+1.86%` | `10X Cross` |
| `1465` | `0xc675...795d` | `LONG` | 1,473,280.16 USD | `2,055,214,000,000.00` | `706.91` | `716.30` | `640.91` | 20,435.49 USD | `+1.39%` | `10X Cross` |
| `1489` | `0x2edd...8179` | `LONG` | 1,446,472.58 USD | `2,019,367,000,000.00` | `714.56` | `716.30` | `0.000000` | 3,511.19 USD | `+0.24%` | `10X Cross` |
| `1554` | `0x325e...9564` | `LONG` | 1,385,495.40 USD | `1,934,212,000,000.00` | `707.43` | `716.30` | `0.000000` | 17,169.63 USD | `+1.24%` | `10X Cross` |
| `1611` | `0xecb6...2b00` | `SHORT` | 1,310,118.43 USD | `1,829,008,000,000.00` | `715.32` | `716.30` | `16439.74` | -1,789.72 USD | `-0.14%` | `5X Cross` |
| `1696` | `0x07fd...689d` | `LONG` | 1,238,074.50 USD | `1,728,406,000,000.00` | `714.40` | `716.30` | `0.000000` | 3,291.52 USD | `+0.27%` | `10X Cross` |
| `1701` | `0x645b...87b8` | `LONG` | 1,233,461.44 USD | `1,721,990,000,000.00` | `747.34` | `716.30` | `0.000000` | -53,445.98 USD | `-4.33%` | `10X Cross` |
| `1778` | `0xa4a6...46cf` | `SHORT` | 1,164,304.10 USD | `1,625,442,000,000.00` | `711.86` | `716.30` | `1626.16` | -7,211.73 USD | `-0.62%` | `10X Cross` |
| `1859` | `0xfc27...9d9d` | `LONG` | 1,101,321.66 USD | `1,537,536,000,000.00` | `701.02` | `716.30` | `0.000000` | 23,474.12 USD | `+2.13%` | `10X Cross` |
| `1873` | `0x4420...4c4b` | `LONG` | 1,089,729.71 USD | `1,520,143,000,000.00` | `704.02` | `716.30` | `211.71` | 19,519.15 USD | `+1.79%` | `10X Cross` |
| `1887` | `0x14c6...b280` | `SHORT` | 1,074,465.00 USD | `1,500,000,000,000.00` | `712.51` | `716.30` | `1467.40` | -5,703.30 USD | `-0.53%` | `10X Cross` |
| `1991` | `0x646b...01dc` | `SHORT` | 1,012,051.48 USD | `1,412,868,000,000.00` | `699.26` | `716.30` | `1276.46` | -24,082.48 USD | `-2.38%` | `10X Cross` |

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
| `Live` | `Long Liquidation` | `143.50` | 3,740.00 USD | 5,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `144.50` | 2,710.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `147.50` | 88,500.00 USD | 5,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `177.50` | 6,020.00 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `178.50` | 239.90 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `184.50` | 712.17 USD | 5,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `191.50` | 538,940.00 USD | 5,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `199.50` | 19,950.00 USD | 5,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `204.50` | 1,470.00 USD | 4,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `205.50` | 252.56 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `206.50` | 253.38 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `216.50` | 216,500.00 USD | 4,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `219.50` | 191.18 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `221.50` | 7,560.00 USD | 4,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `237.50` | 378,440.00 USD | 4,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `249.50` | 998.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `254.50` | 1,340.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `262.50` | 4,660.00 USD | 4,380,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `265.50` | 18,440.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `266.50` | 18,440.00 USD | 4,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `267.50` | 21,200.00 USD | 4,340,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `270.50` | 814.20 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `284.50` | 11,380.00 USD | 4,320,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `292.50` | 7,270.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `303.50` | 150,800.00 USD | 4,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `312.50` | 500.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `316.50` | 126,600.00 USD | 4,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `326.50` | 500.85 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `327.50` | 314.07 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `332.50` | 150.29 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `333.50` | 226.45 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `337.50` | 1,060.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `339.50` | 9,350.00 USD | 4,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `340.50` | 120.20 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `342.50` | 1,600.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `348.50` | 6,130.00 USD | 4,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `356.50` | 3,570.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `359.50` | 212.10 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `363.50` | 340.60 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `364.50` | 1,640.00 USD | 4,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `366.50` | 549.75 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `367.50` | 146.63 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `368.50` | 15,810.00 USD | 3,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `369.50` | 16,630.00 USD | 3,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `371.50` | 146.37 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `372.50` | 10,510.00 USD | 3,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `373.50` | 15,910.00 USD | 3,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `374.50` | 1,820.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `377.50` | 3,260.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `378.50` | 643.45 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `381.50` | 1,910.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `383.50` | 10,900.00 USD | 3,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `384.50` | 1,060.00 USD | 3,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `385.50` | 1,800.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `386.50` | 531.44 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `387.50` | 392.54 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `393.50` | 536.73 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `394.50` | 29,460.00 USD | 3,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `395.50` | 2,110.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `396.50` | 317.20 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `398.50` | 523.63 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `399.50` | 603.64 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `404.50` | 102.34 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `405.50` | 7,700.00 USD | 3,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `409.50` | 613.02 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `410.50` | 105.91 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `411.50` | 5,810.00 USD | 3,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `412.50` | 3,490.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `413.50` | 11,400.00 USD | 3,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `414.50` | 1,890.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `415.50` | 1,810.00 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `416.50` | 644.33 USD | 3,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `417.50` | 7,140.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `418.50` | 318.06 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `419.50` | 2,650.00 USD | 3,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `420.50` | 29,430.00 USD | 3,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `421.50` | 2,320.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `422.50` | 5,270.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `426.50` | 183.40 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `429.50` | 846.12 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `430.50` | 910.51 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `431.50` | 612.73 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `434.50` | 622.20 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `436.50` | 133.13 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `437.50` | 1,430.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `438.50` | 1,790.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `448.50` | 3,350.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `451.50` | 647.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `456.50` | 4,730.00 USD | 3,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `464.50` | 396.68 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `468.50` | 7,030.00 USD | 3,780,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `469.50` | 4,370.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `475.50` | 5,320.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `478.50` | 2,600.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `481.50` | 615.36 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `482.50` | 8,140.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `484.50` | 3,330.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `485.50` | 2,400.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `487.50` | 464.59 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `488.50` | 2,300.00 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `492.50` | 281.22 USD | 3,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `493.50` | 1,840.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `494.50` | 857.46 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `498.50` | 1,820.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `499.50` | 13,880.00 USD | 3,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `501.50` | 7,760.00 USD | 3,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `502.50` | 60,380.00 USD | 3,720,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `505.50` | 5,760.00 USD | 3,660,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `507.50` | 2,380.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `508.50` | 53,270.00 USD | 3,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `509.50` | 3,100.00 USD | 3,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `510.50` | 4,080.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `511.50` | 5,180.00 USD | 3,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `512.50` | 41,220.00 USD | 3,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `513.50` | 2,520.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `514.50` | 701.78 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `515.50` | 5,990.00 USD | 3,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `516.50` | 481.89 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `517.50` | 22,650.00 USD | 3,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `519.50` | 968.35 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `520.50` | 272.22 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `521.50` | 75,990.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `522.50` | 2,090.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `524.50` | 833.43 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `526.50` | 3,320.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `527.50` | 179,790.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `529.50` | 42,820.00 USD | 3,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `530.50` | 18,050.00 USD | 3,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `531.50` | 484.73 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `532.50` | 422.81 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `534.50` | 555.35 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `535.50` | 100.14 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `539.50` | 490.94 USD | 3,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `540.50` | 471.32 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `543.50` | 2,680.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `544.50` | 210,830.00 USD | 3,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `545.50` | 1,580.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `546.50` | 530.11 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `548.50` | 1,980.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `549.50` | 1,370.00 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `550.50` | 633.63 USD | 2,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `551.50` | 1,250.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `552.50` | 24,120.00 USD | 2,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `553.50` | 3,080.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `556.50` | 5,670.00 USD | 2,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `557.50` | 10,020.00 USD | 2,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `558.50` | 212.23 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `560.50` | 582.36 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `568.50` | 454.80 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `569.50` | 144.08 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `571.50` | 712,740.00 USD | 2,920,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `572.50` | 8,800.00 USD | 2,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `574.50` | 163,310.00 USD | 2,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `576.50` | 4,810.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `578.50` | 7,640.00 USD | 2,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `580.50` | 35,850.00 USD | 2,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `581.50` | 580.34 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `582.50` | 1,540.00 USD | 1,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `583.50` | 3,470.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `585.50` | 210.19 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `586.50` | 2,360.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `587.50` | 5,340.00 USD | 1,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `588.50` | 397.24 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `589.50` | 10,820.00 USD | 1,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `590.50` | 2,560.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `591.50` | 619.30 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `592.50` | 840.76 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `593.50` | 53,660.00 USD | 1,960,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `594.50` | 8,860.00 USD | 1,900,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `595.50` | 3,000.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `596.50` | 8,910.00 USD | 1,890,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `597.50` | 2,390.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `598.50` | 1,100.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `600.50` | 945.19 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `601.50` | 16,880.00 USD | 1,880,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `602.50` | 418.13 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `603.50` | 23,410.00 USD | 1,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `604.50` | 256.91 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `605.50` | 4,240.00 USD | 1,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `606.50` | 1,880.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `607.50` | 58,610.00 USD | 1,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `609.50` | 213.32 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `611.50` | 1,580.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `612.50` | 12,250.00 USD | 1,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `613.50` | 120.25 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `614.50` | 4,280.00 USD | 1,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `616.50` | 1,540.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `617.50` | 156.23 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `618.50` | 932.70 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `619.50` | 1,410.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `620.50` | 6,520.00 USD | 1,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `621.50` | 13,930.00 USD | 1,740,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `624.50` | 3,690.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `625.50` | 14,200.00 USD | 1,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `626.50` | 964.81 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `627.50` | 104.17 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `630.50` | 9,600.00 USD | 1,710,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `631.50` | 2,900.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `632.50` | 3,560.00 USD | 1,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `634.50` | 6,660.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `635.50` | 155.06 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `636.50` | 1,110.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `637.50` | 305.36 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `638.50` | 6,710.00 USD | 1,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `639.50` | 127.26 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `640.50` | 1,320,000.00 USD | 1,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `642.50` | 8,480.00 USD | 360,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Long Liquidation` | `643.50` | 339.12 USD | 351,850.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `643.80` | 46,500,000.00 USD | 46,500,000.00 USD | 78,500.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `644.60` | 46,420,000.00 USD | 46,420,000.00 USD | 359,170.00 USD | 10,420.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `645.40` | 45,710,000.00 USD | 45,710,000.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `646.20` | 45,690,000.00 USD | 45,690,000.00 USD | 132,600.00 USD | 11,780.00 USD | 184,540.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `646.50` | 463.54 USD | 351,510.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `647.00` | 45,360,000.00 USD | 45,360,000.00 USD | 204,530.00 USD | 2,560.00 USD | 33,810.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `647.80` | 45,120,000.00 USD | 45,120,000.00 USD | 136,750.00 USD | 33,700.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `648.50` | 1,940.00 USD | 351,050.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `648.60` | 44,940,000.00 USD | 44,940,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `649.40` | 44,850,000.00 USD | 44,850,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `649.50` | 1,620.00 USD | 349,110.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `650.20` | 44,800,000.00 USD | 44,800,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `650.50` | 2,090.00 USD | 347,480.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.00` | 44,730,000.00 USD | 44,730,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `651.50` | 9,650.00 USD | 345,390.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `651.80` | 44,550,000.00 USD | 44,550,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `652.50` | 652.50 USD | 335,740.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `652.60` | 44,450,000.00 USD | 44,450,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `653.40` | 44,420,000.00 USD | 44,420,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `653.50` | 97,380.00 USD | 335,090.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `654.20` | 44,350,000.00 USD | 44,350,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `654.50` | 100.14 USD | 237,710.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.00` | 44,280,000.00 USD | 44,280,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `655.50` | 437.87 USD | 237,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `655.80` | 44,190,000.00 USD | 44,190,000.00 USD | 184,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `656.60` | 44,010,000.00 USD | 44,010,000.00 USD | 121,760.00 USD | 40,970.00 USD | 825,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `657.40` | 43,020,000.00 USD | 43,020,000.00 USD | 264,960.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `658.20` | 42,730,000.00 USD | 42,730,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `658.50` | 15,090.00 USD | 237,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.00` | 41,920,000.00 USD | 41,920,000.00 USD | 119,820.00 USD | 0.00 USD | 81,440.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `659.50` | 46,450.00 USD | 222,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `659.80` | 41,720,000.00 USD | 41,720,000.00 USD | 69,270.00 USD | 7,460.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `660.50` | 3,410.00 USD | 175,630.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `660.60` | 41,630,000.00 USD | 41,630,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `661.40` | 41,450,000.00 USD | 41,450,000.00 USD | 462,080.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `661.50` | 20,140.00 USD | 172,220.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `662.20` | 40,990,000.00 USD | 40,990,000.00 USD | 149,020.00 USD | 155,800.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `662.50` | 2,850.00 USD | 152,080.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.00` | 40,690,000.00 USD | 40,690,000.00 USD | 264,780.00 USD | 0.00 USD | 44,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `663.50` | 9,230.00 USD | 149,230.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `663.80` | 40,380,000.00 USD | 40,380,000.00 USD | 62,940.00 USD | 69,400.00 USD | 64,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `664.10` | 87,050,000.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `664.50` | 24,100.00 USD | 140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `664.60` | 40,180,000.00 USD | 40,180,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `665.00` | 86,910,000.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `665.40` | 38,790,000.00 USD | 38,790,000.00 USD | 696,240.00 USD | 4,540.00 USD | 11,460.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `665.50` | 10,950.00 USD | 115,900.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `665.90` | 86,760,000.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `666.20` | 38,080,000.00 USD | 38,080,000.00 USD | 235,820.00 USD | 88,780.00 USD | 750,630.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `666.50` | 1,930.00 USD | 104,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `666.80` | 86,360,000.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.00` | 37,010,000.00 USD | 37,010,000.00 USD | 938,620.00 USD | 26,880.00 USD | 40,700.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `667.50` | 1,380.00 USD | 103,030.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `667.70` | 86,070,000.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `667.80` | 36,000,000.00 USD | 36,000,000.00 USD | 393,190.00 USD | 154,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `668.50` | 1,450.00 USD | 101,650.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `668.60` | 35,450,000.00 USD | 35,450,000.00 USD | 744,740.00 USD | 39,300.00 USD | 3,620.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `668.60` | 85,770,000.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `669.40` | 34,660,000.00 USD | 34,660,000.00 USD | 470,820.00 USD | 61,020.00 USD | 29,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `669.50` | 85,240,000.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `669.50` | 2,930.00 USD | 100,200.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `670.20` | 34,100,000.00 USD | 34,100,000.00 USD | 625,160.00 USD | 39,310.00 USD | 1,500,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `670.40` | 84,750,000.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `670.50` | 6,110.00 USD | 97,280.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.00` | 31,940,000.00 USD | 31,940,000.00 USD | 299,200.00 USD | 21,410.00 USD | 2,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `671.30` | 84,260,000.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `671.50` | 832.66 USD | 91,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `671.80` | 31,620,000.00 USD | 31,620,000.00 USD | 2,290,000.00 USD | 21,250.00 USD | 46,180.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `672.20` | 83,830,000.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `672.50` | 6,920.00 USD | 90,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `672.60` | 29,260,000.00 USD | 29,260,000.00 USD | 134,640.00 USD | 38,560.00 USD | 702,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `673.10` | 83,510,000.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `673.40` | 28,390,000.00 USD | 28,390,000.00 USD | 332,930.00 USD | 301,900.00 USD | 1,650,000.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `673.50` | 41,240.00 USD | 83,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.00` | 83,010,000.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `674.20` | 26,100,000.00 USD | 26,100,000.00 USD | 358,110.00 USD | 241,130.00 USD | 170,020.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `674.50` | 4,310.00 USD | 42,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `674.90` | 82,490,000.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `675.00` | 25,330,000.00 USD | 25,330,000.00 USD | 1,210,000.00 USD | 258,700.00 USD | 400,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `675.50` | 9,430.00 USD | 37,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `675.80` | 23,460,000.00 USD | 23,460,000.00 USD | 1,450,000.00 USD | 196,370.00 USD | 152,240.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `675.80` | 82,160,000.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `676.50` | 1,660.00 USD | 28,430.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `676.60` | 21,670,000.00 USD | 21,670,000.00 USD | 355,620.00 USD | 363,790.00 USD | 353,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `676.70` | 81,670,000.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `677.40` | 20,590,000.00 USD | 20,590,000.00 USD | 317,920.00 USD | 49,130.00 USD | 250,200.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `677.50` | 438.34 USD | 26,770.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `677.60` | 81,000,000.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `678.20` | 19,980,000.00 USD | 19,980,000.00 USD | 254,050.00 USD | 236,970.00 USD | 137,470.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `678.50` | 80,530,000.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `678.50` | 417.96 USD | 26,330.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.00` | 19,350,000.00 USD | 19,350,000.00 USD | 1,170,000.00 USD | 0.00 USD | 71,540.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `679.40` | 80,380,000.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `679.50` | 3,510.00 USD | 25,920.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `679.80` | 18,100,000.00 USD | 18,100,000.00 USD | 1,450,000.00 USD | 220,780.00 USD | 298,080.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `680.30` | 80,210,000.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `680.50` | 21,460.00 USD | 22,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `680.60` | 16,140,000.00 USD | 16,140,000.00 USD | 13,020.00 USD | 153,320.00 USD | 143,090.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `681.20` | 80,030,000.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `681.40` | 15,830,000.00 USD | 15,830,000.00 USD | 616,620.00 USD | 414,700.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Long Liquidation` | `681.50` | 939.79 USD | 939.79 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `682.10` | 79,880,000.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `682.20` | 14,750,000.00 USD | 14,750,000.00 USD | 294,680.00 USD | 16,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `682.50` | 345.35 USD | 345.35 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Long Liquidation` | `683.00` | 14,440,000.00 USD | 14,440,000.00 USD | 690,810.00 USD | 59,430.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.00` | 79,830,000.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `683.80` | 13,650,000.00 USD | 13,650,000.00 USD | 405,890.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `683.90` | 79,620,000.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `684.60` | 13,210,000.00 USD | 13,210,000.00 USD | 138,250.00 USD | 37,350.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `684.80` | 79,490,000.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `685.40` | 13,030,000.00 USD | 13,030,000.00 USD | 406,260.00 USD | 54,190.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `685.70` | 79,200,000.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `686.20` | 12,570,000.00 USD | 12,570,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `686.60` | 79,000,000.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.00` | 11,520,000.00 USD | 11,520,000.00 USD | 130,820.00 USD | 96,690.00 USD | 98,790.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `687.50` | 78,940,000.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `687.80` | 11,190,000.00 USD | 11,190,000.00 USD | 840,870.00 USD | 75,260.00 USD | 172,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `688.40` | 78,790,000.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `688.60` | 10,110,000.00 USD | 10,110,000.00 USD | 420,000.00 USD | 84,090.00 USD | 444,740.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `689.30` | 78,720,000.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `689.40` | 9,160,000.00 USD | 9,160,000.00 USD | 19,470.00 USD | 60,350.00 USD | 813,820.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `690.20` | 8,260,000.00 USD | 8,260,000.00 USD | 31,110.00 USD | 52,210.00 USD | 212,990.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `690.20` | 78,640,000.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.00` | 7,970,000.00 USD | 7,970,000.00 USD | 0.00 USD | 141,060.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `691.10` | 78,210,000.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `691.80` | 7,810,000.00 USD | 7,810,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.00` | 77,700,000.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `692.90` | 77,300,000.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `693.40` | 7,780,000.00 USD | 7,780,000.00 USD | 0.00 USD | 60,140.00 USD | 273,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `693.80` | 77,000,000.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `694.20` | 7,450,000.00 USD | 7,450,000.00 USD | 0.00 USD | 117,630.00 USD | 180,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `694.70` | 76,660,000.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.00` | 7,150,000.00 USD | 7,150,000.00 USD | 239,550.00 USD | 64,240.00 USD | 175,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `695.60` | 76,300,000.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `695.80` | 6,670,000.00 USD | 6,670,000.00 USD | 0.00 USD | 34,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `696.50` | 76,160,000.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `696.60` | 6,640,000.00 USD | 6,640,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `697.40` | 76,020,000.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `698.20` | 6,540,000.00 USD | 6,540,000.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `698.30` | 75,810,000.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `699.00` | 6,340,000.00 USD | 6,340,000.00 USD | 276,500.00 USD | 31,670.00 USD | 42,650.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `699.20` | 75,450,000.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `700.10` | 75,150,000.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `700.60` | 5,990,000.00 USD | 5,990,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.00` | 74,860,000.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `701.40` | 5,800,000.00 USD | 5,800,000.00 USD | 0.00 USD | 59,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `701.90` | 74,620,000.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `702.20` | 5,740,000.00 USD | 5,740,000.00 USD | 138,970.00 USD | 91,260.00 USD | 52,230.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `702.80` | 74,360,000.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.00` | 5,460,000.00 USD | 5,460,000.00 USD | 232,220.00 USD | 12,930.00 USD | 208,020.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `703.70` | 73,840,000.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `703.80` | 5,000,000.00 USD | 5,000,000.00 USD | 240,730.00 USD | 45,990.00 USD | 468,050.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `704.60` | 4,250,000.00 USD | 4,250,000.00 USD | 62,230.00 USD | 12,800.00 USD | 247,060.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `704.60` | 73,490,000.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `705.40` | 3,930,000.00 USD | 3,930,000.00 USD | 0.00 USD | 23,130.00 USD | 121,600.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `705.50` | 72,620,000.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `706.20` | 3,780,000.00 USD | 3,780,000.00 USD | 237,450.00 USD | 0.00 USD | 123,170.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `706.40` | 71,300,000.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `707.30` | 70,440,000.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `707.80` | 3,420,000.00 USD | 3,420,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `708.20` | 69,690,000.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `708.60` | 3,220,000.00 USD | 3,220,000.00 USD | 109,380.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `709.10` | 68,710,000.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `709.40` | 3,110,000.00 USD | 3,110,000.00 USD | 272,730.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `709.50` | 1,400.00 USD | 1,750.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `710.00` | 67,970,000.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `710.90` | 67,180,000.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.00` | 2,840,000.00 USD | 2,840,000.00 USD | 694,090.00 USD | 0.00 USD | 37,900.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `711.80` | 2,110,000.00 USD | 2,110,000.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `711.80` | 65,860,000.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `712.60` | 1,820,000.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `712.70` | 64,900,000.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `713.60` | 63,260,000.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `714.50` | 60,410,000.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.00` | 1,800,000.00 USD | 1,800,000.00 USD | 0.00 USD | 317,060.00 USD | 415,380.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `715.40` | 59,400,000.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD | `Tier 1 CEX` |
| `1D` | `Long Liquidation` | `715.80` | 1,060,000.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 1,060,000.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `716.30` | 57,600,000.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `717.20` | 55,960,000.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `718.10` | 54,590,000.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.00` | 82,030.00 USD | 82,030.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.00` | 52,510,000.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `719.80` | 166,220.00 USD | 166,220.00 USD | 60,590.00 USD | 23,600.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `719.90` | 51,490,000.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `720.50` | 161.39 USD | 1,910.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `720.60` | 578,690.00 USD | 578,690.00 USD | 207,940.00 USD | 204,540.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `720.80` | 50,510,000.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `721.40` | 816,230.00 USD | 816,230.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `721.50` | 33,260.00 USD | 35,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `721.70` | 49,260,000.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `722.20` | 1,360,000.00 USD | 1,360,000.00 USD | 28,010.00 USD | 123,420.00 USD | 391,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `722.50` | 566.44 USD | 35,730.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `722.60` | 46,430,000.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `723.00` | 1,980,000.00 USD | 1,980,000.00 USD | 191,050.00 USD | 250,670.00 USD | 176,360.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `723.50` | 44,160,000.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `723.50` | 3,560.00 USD | 39,290.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `723.80` | 2,840,000.00 USD | 2,840,000.00 USD | 380,140.00 USD | 392,010.00 USD | 88,480.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `724.40` | 43,080,000.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `724.50` | 525.26 USD | 39,810.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `724.60` | 3,060,000.00 USD | 3,060,000.00 USD | 173,300.00 USD | 45,850.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `725.30` | 42,100,000.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `725.40` | 3,680,000.00 USD | 3,680,000.00 USD | 461,100.00 USD | 120,790.00 USD | 38,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `725.50` | 1,530.00 USD | 41,340.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `726.20` | 3,940,000.00 USD | 3,940,000.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `726.20` | 39,520,000.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `726.50` | 3,840.00 USD | 45,180.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.00` | 4,320,000.00 USD | 4,320,000.00 USD | 299,310.00 USD | 75,120.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `727.10` | 37,690,000.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `727.50` | 1,030.00 USD | 46,210.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `727.80` | 4,710,000.00 USD | 4,710,000.00 USD | 339,770.00 USD | 48,110.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.00` | 35,890,000.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `728.50` | 41,940.00 USD | 88,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `728.60` | 4,800,000.00 USD | 4,800,000.00 USD | 23,160.00 USD | 23,030.00 USD | 49,400.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `728.90` | 31,610,000.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `729.40` | 6,040,000.00 USD | 6,040,000.00 USD | 359,560.00 USD | 259,230.00 USD | 616,880.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `729.50` | 174,370.00 USD | 262,520.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `729.80` | 28,320,000.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `730.20` | 8,040,000.00 USD | 8,040,000.00 USD | 1,720,000.00 USD | 213,600.00 USD | 73,220.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `730.50` | 24,090.00 USD | 286,610.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `730.70` | 26,230,000.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.00` | 11,470,000.00 USD | 11,470,000.00 USD | 1,250,000.00 USD | 230,860.00 USD | 1,950,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `731.50` | 7,340.00 USD | 293,950.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `731.60` | 22,530,000.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `731.80` | 12,560,000.00 USD | 12,560,000.00 USD | 276,840.00 USD | 171,500.00 USD | 645,890.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `732.50` | 20,610,000.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `732.50` | 136,920.00 USD | 430,870.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `732.60` | 14,800,000.00 USD | 14,800,000.00 USD | 747,600.00 USD | 107,040.00 USD | 1,380,000.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `733.40` | 16,260,000.00 USD | 16,260,000.00 USD | 808,610.00 USD | 306,960.00 USD | 350,110.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `733.40` | 19,820,000.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `733.50` | 86,060.00 USD | 516,930.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `734.20` | 16,890,000.00 USD | 16,890,000.00 USD | 460,390.00 USD | 34,930.00 USD | 132,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `734.30` | 17,420,000.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `734.50` | 152,470.00 USD | 669,410.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.00` | 17,560,000.00 USD | 17,560,000.00 USD | 481,620.00 USD | 183,770.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `735.20` | 15,310,000.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `735.50` | 22,990.00 USD | 692,400.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `735.80` | 19,110,000.00 USD | 19,110,000.00 USD | 875,750.00 USD | 84,090.00 USD | 590,930.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `736.10` | 13,370,000.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `736.50` | 13,550.00 USD | 705,960.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `736.60` | 19,820,000.00 USD | 19,820,000.00 USD | 476,310.00 USD | 58,820.00 USD | 181,870.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `737.00` | 10,570,000.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `737.40` | 20,150,000.00 USD | 20,150,000.00 USD | 115,170.00 USD | 126,150.00 USD | 88,180.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `737.50` | 3,010.00 USD | 708,970.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `737.90` | 7,400,000.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `738.20` | 20,590,000.00 USD | 20,590,000.00 USD | 305,260.00 USD | 85,790.00 USD | 44,240.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `738.50` | 6,210.00 USD | 715,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `738.80` | 3,530,000.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.00` | 22,260,000.00 USD | 22,260,000.00 USD | 720,770.00 USD | 16,030.00 USD | 934,700.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `739.50` | 8,000.00 USD | 723,170.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Long Liquidation` | `739.70` | 2,830,000.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `739.80` | 22,710,000.00 USD | 22,710,000.00 USD | 421,830.00 USD | 31,860.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `740.50` | 3,980.00 USD | 727,150.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `740.60` | 23,060,000.00 USD | 23,060,000.00 USD | 211,010.00 USD | 134,150.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `740.60` | 2,280,000.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `741.40` | 23,540,000.00 USD | 23,540,000.00 USD | 451,230.00 USD | 32,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `741.50` | 1,160,000.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `741.50` | 8,790.00 USD | 735,940.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `742.20` | 23,850,000.00 USD | 23,850,000.00 USD | 291,160.00 USD | 15,840.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `742.40` | 689,850.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `742.50` | 11,610.00 USD | 747,550.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.00` | 24,080,000.00 USD | 24,080,000.00 USD | 233,270.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `743.30` | 505,930.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `743.50` | 103,120.00 USD | 850,670.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `743.80` | 24,540,000.00 USD | 24,540,000.00 USD | 17,370.00 USD | 0.00 USD | 436,560.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `744.20` | 448,350.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `744.50` | 117,700.00 USD | 968,370.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `744.60` | 25,630,000.00 USD | 25,630,000.00 USD | 926,810.00 USD | 162,260.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Long Liquidation` | `745.10` | 48,980.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `745.40` | 26,990,000.00 USD | 26,990,000.00 USD | 461,360.00 USD | 19,580.00 USD | 887,910.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `745.50` | 67,820.00 USD | 1,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.00` | 999,320.00 USD | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `746.20` | 27,910,000.00 USD | 27,910,000.00 USD | 563,040.00 USD | 135,740.00 USD | 221,170.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `746.50` | 182,880.00 USD | 1,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.00` | 29,300,000.00 USD | 29,300,000.00 USD | 463,290.00 USD | 43,680.00 USD | 875,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `747.80` | 29,710,000.00 USD | 29,710,000.00 USD | 145,680.00 USD | 103,400.00 USD | 164,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `748.50` | 44,170.00 USD | 1,260,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `748.60` | 30,120,000.00 USD | 30,120,000.00 USD | 377,840.00 USD | 11,570.00 USD | 17,880.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `749.40` | 30,440,000.00 USD | 30,440,000.00 USD | 321,760.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `749.50` | 3,230.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `750.20` | 30,610,000.00 USD | 30,610,000.00 USD | 171,230.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `750.50` | 9,570.00 USD | 1,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.00` | 30,680,000.00 USD | 30,680,000.00 USD | 71,910.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `751.50` | 593,520.00 USD | 1,870,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `751.80` | 31,200,000.00 USD | 31,200,000.00 USD | 103,120.00 USD | 25,010.00 USD | 393,600.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `752.50` | 57,710.00 USD | 1,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `752.60` | 31,680,000.00 USD | 31,680,000.00 USD | 334,780.00 USD | 0.00 USD | 146,020.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `753.40` | 32,050,000.00 USD | 32,050,000.00 USD | 113,650.00 USD | 3,810.00 USD | 248,870.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `754.20` | 32,510,000.00 USD | 32,510,000.00 USD | 349,560.00 USD | 50,610.00 USD | 57,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `754.50` | 863,250.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.00` | 32,960,000.00 USD | 32,960,000.00 USD | 235,060.00 USD | 178,540.00 USD | 37,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `755.50` | 336.20 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `755.80` | 33,340,000.00 USD | 33,340,000.00 USD | 263,490.00 USD | 96,170.00 USD | 19,780.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `756.50` | 3,750.00 USD | 2,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `756.60` | 33,860,000.00 USD | 33,860,000.00 USD | 399,730.00 USD | 24,970.00 USD | 95,500.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `757.40` | 34,200,000.00 USD | 34,200,000.00 USD | 164,750.00 USD | 139,150.00 USD | 32,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `757.50` | 3,050.00 USD | 2,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `758.20` | 35,240,000.00 USD | 35,240,000.00 USD | 755,970.00 USD | 75,210.00 USD | 218,280.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `758.50` | 180,270.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `759.00` | 36,250,000.00 USD | 36,250,000.00 USD | 832,020.00 USD | 117,910.00 USD | 54,810.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `759.50` | 3,830.00 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `759.80` | 36,670,000.00 USD | 36,670,000.00 USD | 383,590.00 USD | 21,070.00 USD | 15,370.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `760.50` | 540.72 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `760.60` | 37,030,000.00 USD | 37,030,000.00 USD | 268,390.00 USD | 52,630.00 USD | 35,930.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `761.40` | 38,040,000.00 USD | 38,040,000.00 USD | 756,450.00 USD | 8,690.00 USD | 250,520.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `762.20` | 38,370,000.00 USD | 38,370,000.00 USD | 101,750.00 USD | 124,370.00 USD | 98,750.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `762.50` | 367.52 USD | 2,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.00` | 40,980,000.00 USD | 40,980,000.00 USD | 1,950,000.00 USD | 138,090.00 USD | 523,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `763.50` | 445,300.00 USD | 3,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `763.80` | 42,270,000.00 USD | 42,270,000.00 USD | 996,680.00 USD | 109,500.00 USD | 178,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `764.50` | 76,450.00 USD | 3,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `764.60` | 43,720,000.00 USD | 43,720,000.00 USD | 1,110,000.00 USD | 136,310.00 USD | 199,800.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `765.40` | 44,590,000.00 USD | 44,590,000.00 USD | 614,150.00 USD | 150,770.00 USD | 110,720.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `766.20` | 45,770,000.00 USD | 45,770,000.00 USD | 630,970.00 USD | 218,550.00 USD | 330,960.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `766.50` | 2,850.00 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.00` | 48,220,000.00 USD | 48,220,000.00 USD | 2,090,000.00 USD | 67,550.00 USD | 286,770.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `767.80` | 50,030,000.00 USD | 50,030,000.00 USD | 1,450,000.00 USD | 100,820.00 USD | 254,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `768.50` | 156.77 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `768.60` | 50,890,000.00 USD | 50,890,000.00 USD | 731,220.00 USD | 45,390.00 USD | 84,280.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `769.40` | 51,230,000.00 USD | 51,230,000.00 USD | 291,010.00 USD | 38,990.00 USD | 8,460.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `770.20` | 51,640,000.00 USD | 51,640,000.00 USD | 288,220.00 USD | 97,130.00 USD | 28,450.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `770.50` | 881.45 USD | 3,510,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.00` | 52,250,000.00 USD | 52,250,000.00 USD | 156,280.00 USD | 52,310.00 USD | 397,910.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `771.50` | 10,380.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `771.80` | 53,220,000.00 USD | 53,220,000.00 USD | 331,470.00 USD | 60,980.00 USD | 582,120.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `772.50` | 849.75 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `772.60` | 53,670,000.00 USD | 53,670,000.00 USD | 286,150.00 USD | 150,000.00 USD | 16,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `773.40` | 54,370,000.00 USD | 54,370,000.00 USD | 618,270.00 USD | 10,490.00 USD | 68,320.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `773.50` | 3,800.00 USD | 3,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `774.20` | 54,960,000.00 USD | 54,960,000.00 USD | 568,370.00 USD | 19,250.00 USD | 1,360.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.00` | 55,140,000.00 USD | 55,140,000.00 USD | 54,760.00 USD | 34,120.00 USD | 86,160.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `775.80` | 55,340,000.00 USD | 55,340,000.00 USD | 126,750.00 USD | 24,070.00 USD | 49,120.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `776.50` | 100,020.00 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `776.60` | 55,540,000.00 USD | 55,540,000.00 USD | 123,900.00 USD | 4,350.00 USD | 73,050.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `777.40` | 55,730,000.00 USD | 55,730,000.00 USD | 62,060.00 USD | 109,840.00 USD | 22,680.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `777.50` | 209.15 USD | 3,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `778.20` | 57,100,000.00 USD | 57,100,000.00 USD | 959,690.00 USD | 52,290.00 USD | 361,010.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `778.50` | 3,200.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `779.00` | 57,900,000.00 USD | 57,900,000.00 USD | 630,640.00 USD | 76,100.00 USD | 87,260.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `779.80` | 58,500,000.00 USD | 58,500,000.00 USD | 477,090.00 USD | 47,380.00 USD | 77,860.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `780.50` | 6,200.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `780.60` | 59,040,000.00 USD | 59,040,000.00 USD | 373,710.00 USD | 78,310.00 USD | 84,520.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `781.40` | 59,660,000.00 USD | 59,660,000.00 USD | 363,950.00 USD | 110,320.00 USD | 143,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `781.50` | 1,830.00 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `782.20` | 60,920,000.00 USD | 60,920,000.00 USD | 987,130.00 USD | 15,380.00 USD | 263,560.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.00` | 61,730,000.00 USD | 61,730,000.00 USD | 617,080.00 USD | 50,410.00 USD | 137,740.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `783.80` | 62,000,000.00 USD | 62,000,000.00 USD | 247,150.00 USD | 14,770.00 USD | 8,400.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `784.60` | 62,430,000.00 USD | 62,430,000.00 USD | 433,980.00 USD | 2,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `785.40` | 62,530,000.00 USD | 62,530,000.00 USD | 93,760.00 USD | 4,490.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `785.50` | 129.61 USD | 3,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `786.20` | 62,670,000.00 USD | 62,670,000.00 USD | 117,250.00 USD | 0.00 USD | 18,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `786.50` | 126,920.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `787.00` | 62,790,000.00 USD | 62,790,000.00 USD | 120,340.00 USD | 3,620.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `787.80` | 63,500,000.00 USD | 63,500,000.00 USD | 361,020.00 USD | 10,420.00 USD | 341,610.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `788.50` | 2,320.00 USD | 3,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `1D` | `Short Liquidation` | `788.60` | 63,550,000.00 USD | 63,550,000.00 USD | 43,780.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `789.40` | 63,760,000.00 USD | 63,760,000.00 USD | 164,090.00 USD | 11,780.00 USD | 34,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `790.20` | 64,190,000.00 USD | 64,190,000.00 USD | 261,950.00 USD | 2,560.00 USD | 162,050.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.00` | 64,330,000.00 USD | 64,330,000.00 USD | 85,520.00 USD | 33,700.00 USD | 21,390.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `791.80` | 64,480,000.00 USD | 64,480,000.00 USD | 141,380.00 USD | 0.00 USD | 7,150.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `792.60` | 64,610,000.00 USD | 64,610,000.00 USD | 135,050.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD | `Tier 1 CEX` |
| `1D` | `Short Liquidation` | `793.40` | 64,640,000.00 USD | 64,640,000.00 USD | 31,240.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `793.50` | 3,690.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `793.70` | 63,430,000.00 USD | 63,430,000.00 USD | 184,960.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `794.60` | 63,750,000.00 USD | 63,750,000.00 USD | 302,280.00 USD | 15,690.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `795.50` | 63,890,000.00 USD | 63,890,000.00 USD | 109,640.00 USD | 14,650.00 USD | 14,200.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `795.50` | 518.67 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `796.40` | 64,030,000.00 USD | 64,030,000.00 USD | 139,030.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `796.50` | 567.11 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `797.30` | 64,090,000.00 USD | 64,090,000.00 USD | 64,670.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `797.50` | 1,090.00 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `798.20` | 64,250,000.00 USD | 64,250,000.00 USD | 155,890.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `799.10` | 64,290,000.00 USD | 64,290,000.00 USD | 42,660.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `799.50` | 610.02 USD | 3,770,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.00` | 64,400,000.00 USD | 64,400,000.00 USD | 113,540.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `800.50` | 28,250.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `800.90` | 64,510,000.00 USD | 64,510,000.00 USD | 77,580.00 USD | 8,370.00 USD | 21,920.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `801.50` | 3,680.00 USD | 3,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `801.80` | 64,720,000.00 USD | 64,720,000.00 USD | 179,900.00 USD | 16,330.00 USD | 10,970.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `802.50` | 778,380.00 USD | 4,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `802.70` | 64,730,000.00 USD | 64,730,000.00 USD | 11,220.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `803.50` | 4,560.00 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `803.60` | 64,760,000.00 USD | 64,760,000.00 USD | 27,360.00 USD | 0.00 USD | 0.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `804.50` | 64,840,000.00 USD | 64,840,000.00 USD | 32,340.00 USD | 18,260.00 USD | 32,980.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `804.50` | 105.39 USD | 4,590,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `805.40` | 64,910,000.00 USD | 64,910,000.00 USD | 56,700.00 USD | 8,140.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `805.50` | 15,370.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `806.30` | 64,920,000.00 USD | 64,920,000.00 USD | 3,270.00 USD | 12,000.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `806.50` | 2,890.00 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `807.20` | 64,970,000.00 USD | 64,970,000.00 USD | 39,190.00 USD | 0.00 USD | 11,830.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `807.50` | 738.06 USD | 4,600,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `808.10` | 65,030,000.00 USD | 65,030,000.00 USD | 17,980.00 USD | 5,360.00 USD | 29,800.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `808.50` | 11,780.00 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.00` | 65,110,000.00 USD | 65,110,000.00 USD | 58,620.00 USD | 13,120.00 USD | 13,000.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `809.50` | 173.23 USD | 4,620,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `809.90` | 65,330,000.00 USD | 65,330,000.00 USD | 178,130.00 USD | 9,760.00 USD | 36,490.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `810.80` | 65,420,000.00 USD | 65,420,000.00 USD | 78,030.00 USD | 6,630.00 USD | 5,340.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `811.50` | 519,680.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `811.70` | 65,480,000.00 USD | 65,480,000.00 USD | 19,210.00 USD | 12,110.00 USD | 29,380.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `812.50` | 853.94 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `812.60` | 65,600,000.00 USD | 65,600,000.00 USD | 68,390.00 USD | 17,450.00 USD | 31,430.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `813.50` | 65,860,000.00 USD | 65,860,000.00 USD | 147,480.00 USD | 59,640.00 USD | 45,810.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `814.40` | 66,180,000.00 USD | 66,180,000.00 USD | 218,130.00 USD | 32,770.00 USD | 74,730.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `814.50` | 1,960.00 USD | 5,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `815.30` | 66,390,000.00 USD | 66,390,000.00 USD | 171,100.00 USD | 24,290.00 USD | 10,150.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `815.50` | 6,020.00 USD | 5,150,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `816.20` | 66,690,000.00 USD | 66,690,000.00 USD | 203,680.00 USD | 44,470.00 USD | 59,870.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `816.50` | 15,410.00 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `817.10` | 67,090,000.00 USD | 67,090,000.00 USD | 278,420.00 USD | 76,830.00 USD | 42,530.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `817.50` | 325.37 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.00` | 67,550,000.00 USD | 67,550,000.00 USD | 346,550.00 USD | 48,360.00 USD | 67,950.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `818.50` | 572.13 USD | 5,160,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `818.90` | 67,790,000.00 USD | 67,790,000.00 USD | 180,470.00 USD | 8,160.00 USD | 47,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `819.80` | 68,300,000.00 USD | 68,300,000.00 USD | 295,510.00 USD | 101,950.00 USD | 107,190.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `820.70` | 68,600,000.00 USD | 68,600,000.00 USD | 235,990.00 USD | 41,190.00 USD | 24,080.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `821.50` | 11,710.00 USD | 5,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `821.60` | 68,800,000.00 USD | 68,800,000.00 USD | 86,380.00 USD | 62,620.00 USD | 55,540.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `822.50` | 69,300,000.00 USD | 69,300,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `822.50` | 3,540.00 USD | 5,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `823.40` | 69,630,000.00 USD | 69,630,000.00 USD | 213,450.00 USD | 68,530.00 USD | 45,900.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `824.30` | 69,980,000.00 USD | 69,980,000.00 USD | 248,860.00 USD | 58,170.00 USD | 43,880.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `825.20` | 70,340,000.00 USD | 70,340,000.00 USD | 277,990.00 USD | 21,630.00 USD | 61,140.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `826.10` | 70,650,000.00 USD | 70,650,000.00 USD | 223,810.00 USD | 27,390.00 USD | 53,050.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `826.50` | 11,640.00 USD | 5,190,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `827.00` | 71,290,000.00 USD | 71,290,000.00 USD | 494,310.00 USD | 23,200.00 USD | 126,570.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `827.90` | 71,650,000.00 USD | 71,650,000.00 USD | 297,880.00 USD | 0.00 USD | 63,990.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `828.50` | 84,000.00 USD | 5,270,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `7D` | `Short Liquidation` | `828.80` | 71,840,000.00 USD | 71,840,000.00 USD | 184,280.00 USD | 0.00 USD | 5,970.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `829.70` | 71,930,000.00 USD | 71,930,000.00 USD | 43,760.00 USD | 5,190.00 USD | 33,310.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `830.60` | 72,180,000.00 USD | 72,180,000.00 USD | 221,150.00 USD | 5,300.00 USD | 28,320.00 USD | `Tier 1 CEX` |
| `7D` | `Short Liquidation` | `831.50` | 72,220,000.00 USD | 72,220,000.00 USD | 37,200.00 USD | 5,500.00 USD | 0.00 USD | `Tier 1 CEX` |
| `Live` | `Short Liquidation` | `833.50` | 79,150.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `834.50` | 1,010.00 USD | 5,350,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `837.50` | 11,450.00 USD | 5,360,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `838.50` | 21,840.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `841.50` | 2,830.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `842.50` | 2,900.00 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `843.50` | 227.75 USD | 5,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `848.50` | 34,550.00 USD | 5,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `850.50` | 10,930.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `851.50` | 285.25 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `854.50` | 5,030.00 USD | 5,440,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `858.50` | 523,680.00 USD | 5,970,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `859.50` | 16,380.00 USD | 5,980,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `865.50` | 18,900.00 USD | 6,000,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `870.50` | 6,090.00 USD | 6,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `871.50` | 292,000.00 USD | 6,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `877.50` | 614,250.00 USD | 6,910,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `878.50` | 93,100.00 USD | 7,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `880.50` | 14,740.00 USD | 7,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `883.50` | 22,840.00 USD | 7,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `885.50` | 1,770.00 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `886.50` | 812.92 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `887.50` | 385.18 USD | 7,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `890.50` | 89,050.00 USD | 7,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `891.50` | 40,420.00 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `893.50` | 173.34 USD | 7,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `894.50` | 26,840.00 USD | 7,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `895.50` | 258,570.00 USD | 7,460,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `896.50` | 224,120.00 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `898.50` | 127.59 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `902.50` | 305.05 USD | 7,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `904.50` | 63,930.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `906.50` | 2,130.00 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `908.50` | 901.23 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `909.50` | 890.40 USD | 7,750,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `910.50` | 3,010.00 USD | 7,760,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `911.50` | 63,160.00 USD | 7,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `912.50` | 7,520.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `913.50` | 116.93 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `914.50` | 3,920.00 USD | 7,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `916.50` | 3,060.00 USD | 7,840,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `917.50` | 13,990.00 USD | 7,850,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `918.50` | 163,540.00 USD | 8,010,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `921.50` | 12,910.00 USD | 8,030,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `925.50` | 9,260.00 USD | 8,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `928.50` | 449,690.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `932.50` | 1,610.00 USD | 8,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `935.50` | 65,480.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `939.50` | 2,670.00 USD | 8,550,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `940.50` | 57,750.00 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `942.50` | 112.16 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `951.50` | 600.40 USD | 8,610,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `955.50` | 18,910.00 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `956.50` | 409.38 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `961.50` | 224.03 USD | 8,630,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `967.50` | 7,250.00 USD | 8,640,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `969.50` | 5,780.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `970.50` | 1,940.00 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `971.50` | 119.49 USD | 8,650,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `975.50` | 829,170.00 USD | 9,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `981.50` | 14,480.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `986.50` | 1,100.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `989.50` | 1,470.00 USD | 9,490,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `990.50` | 28,300.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `992.50` | 2,140.00 USD | 9,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `993.50` | 15,420.00 USD | 9,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `994.50` | 285,520.00 USD | 9,830,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `995.50` | 108,080.00 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `996.50` | 989.52 USD | 9,930,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `997.50` | 7,300.00 USD | 9,940,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `998.50` | 9,550.00 USD | 9,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `999.50` | 36,850.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1003.50` | 838.93 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1005.50` | 4,050.00 USD | 9,990,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1008.50` | 28,800.00 USD | 10,020,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1009.50` | 51,680.00 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1015.50` | 630.63 USD | 10,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1019.50` | 297,250.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1024.50` | 3,340.00 USD | 10,370,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1037.50` | 723,770.00 USD | 11,100,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1039.50` | 31,180.00 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1050.50` | 500.04 USD | 11,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1051.50` | 65,720.00 USD | 11,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1062.50` | 15,300.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1064.50` | 1,600.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1073.50` | 1,610.00 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1079.50` | 120.90 USD | 11,210,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1087.50` | 75,280.00 USD | 11,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1088.50` | 15,780.00 USD | 11,310,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1093.50` | 120,790.00 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1095.50` | 809.57 USD | 11,430,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1097.50` | 74,900.00 USD | 11,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1098.50` | 19,580.00 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1118.50` | 149.88 USD | 11,520,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1119.50` | 60,530.00 USD | 11,580,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1120.50` | 116,530.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1133.50` | 1,520.00 USD | 11,700,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1137.50` | 341,610.00 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1145.50` | 119.13 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1148.50` | 153.90 USD | 12,040,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1152.50` | 11,700.00 USD | 12,050,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1178.50` | 66,060.00 USD | 12,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1188.50` | 57,420.00 USD | 12,180,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1192.50` | 107,330.00 USD | 12,280,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1194.50` | 168.42 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1197.50` | 463.43 USD | 12,290,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1204.50` | 118,960.00 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1207.50` | 385.19 USD | 12,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1212.50` | 42,440.00 USD | 12,450,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1214.50` | 30,340.00 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1218.50` | 704.29 USD | 12,480,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1222.50` | 21,230.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1224.50` | 1,030.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1225.50` | 3,720.00 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1239.50` | 198.32 USD | 12,500,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1241.50` | 26,600.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1248.50` | 1,250.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1249.50` | 2,050.00 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1251.50` | 100.12 USD | 12,530,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1252.50` | 5,000.00 USD | 12,540,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1253.50` | 24,340.00 USD | 12,560,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1263.50` | 113,720.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1265.50` | 2,700.00 USD | 12,680,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1269.50` | 6,880.00 USD | 12,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1278.50` | 38,620.00 USD | 12,730,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1281.50` | 61,670.00 USD | 12,790,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1283.50` | 77,010.00 USD | 12,860,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1290.50` | 1,820,000.00 USD | 14,690,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1293.50` | 110,340.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1294.50` | 4,000.00 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1295.50` | 181.37 USD | 14,800,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1296.50` | 19,370.00 USD | 14,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1300.50` | 130,050.00 USD | 14,950,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1309.50` | 166,150.00 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1313.50` | 227.24 USD | 15,120,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1316.50` | 7,580.00 USD | 15,130,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1319.50` | 14,130.00 USD | 15,140,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1322.50` | 32,870.00 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1327.50` | 138.06 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1328.50` | 289.61 USD | 15,170,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1330.50` | 23,470.00 USD | 15,200,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1333.50` | 18,760.00 USD | 15,220,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1339.50` | 30,810.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1352.50` | 347.59 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1365.50` | 4,100.00 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1366.50` | 194.04 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1367.50` | 761.70 USD | 15,250,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1369.50` | 51,620.00 USD | 15,300,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1371.50` | 89,150.00 USD | 15,390,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1379.50` | 2,760.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1383.50` | 2,460.00 USD | 15,400,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1392.50` | 1,420,000.00 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1401.50` | 177.99 USD | 16,820,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1403.50` | 252,630.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1405.50` | 4,770.00 USD | 17,070,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |
| `Live` | `Short Liquidation` | `1431.50` | 360.74 USD | 17,080,000.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | `Tier 2 DEX` |

- **Hyperdash Liquidation Clusters Profile Table (14_Hyperdash_Liq_Map.parquet)**:
| Window | Side | Strike Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Distance (%) | Size (Coins) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Live` | `Long` | `143.50` | 5,650,000.00 USD | 0.00 USD | 3,740.00 USD | `-79.98%` | `26,050,000,000.00` |
| `Live` | `Long` | `144.50` | 5,640,000.00 USD | 0.00 USD | 2,710.00 USD | `-79.84%` | `18,763,000,000.00` |
| `Live` | `Long` | `147.50` | 5,640,000.00 USD | 0.00 USD | 88,500.00 USD | `-79.42%` | `600,000,000,000.00` |
| `Live` | `Long` | `177.50` | 5,550,000.00 USD | 0.00 USD | 6,020.00 USD | `-75.24%` | `33,907,000,000.00` |
| `Live` | `Long` | `178.50` | 5,550,000.00 USD | 0.00 USD | 239.90 USD | `-75.10%` | `1,344,000,000.00` |
| `Live` | `Long` | `184.50` | 5,550,000.00 USD | 0.00 USD | 712.17 USD | `-74.26%` | `3,860,000,000.00` |
| `Live` | `Long` | `191.50` | 5,540,000.00 USD | 0.00 USD | 538,940.00 USD | `-73.29%` | `2,814,325,000,000.00` |
| `Live` | `Long` | `199.50` | 5,010,000.00 USD | 0.00 USD | 19,950.00 USD | `-72.17%` | `100,000,000,000.00` |
| `Live` | `Long` | `204.50` | 4,990,000.00 USD | 0.00 USD | 1,470.00 USD | `-71.47%` | `7,186,000,000.00` |
| `Live` | `Long` | `205.50` | 4,980,000.00 USD | 0.00 USD | 252.56 USD | `-71.33%` | `1,229,000,000.00` |
| `Live` | `Long` | `206.50` | 4,980,000.00 USD | 0.00 USD | 253.38 USD | `-71.19%` | `1,227,000,000.00` |
| `Live` | `Long` | `216.50` | 4,980,000.00 USD | 0.00 USD | 216,500.00 USD | `-69.80%` | `1,000,000,000,000.00` |
| `Live` | `Long` | `219.50` | 4,770,000.00 USD | 0.00 USD | 191.18 USD | `-69.38%` | `871,000,000.00` |
| `Live` | `Long` | `221.50` | 4,770,000.00 USD | 0.00 USD | 7,560.00 USD | `-69.10%` | `34,129,000,000.00` |
| `Live` | `Long` | `237.50` | 4,760,000.00 USD | 0.00 USD | 378,440.00 USD | `-66.87%` | `1,593,422,000,000.00` |
| `Live` | `Long` | `249.50` | 4,380,000.00 USD | 0.00 USD | 998.00 USD | `-65.20%` | `4,000,000,000.00` |
| `Live` | `Long` | `254.50` | 4,380,000.00 USD | 0.00 USD | 1,340.00 USD | `-64.50%` | `5,281,000,000.00` |
| `Live` | `Long` | `262.50` | 4,380,000.00 USD | 0.00 USD | 4,660.00 USD | `-63.38%` | `17,770,000,000.00` |
| `Live` | `Long` | `265.50` | 4,370,000.00 USD | 0.00 USD | 18,440.00 USD | `-62.96%` | `69,447,000,000.00` |
| `Live` | `Long` | `266.50` | 4,360,000.00 USD | 0.00 USD | 18,440.00 USD | `-62.83%` | `69,189,000,000.00` |
| `Live` | `Long` | `267.50` | 4,340,000.00 USD | 0.00 USD | 21,200.00 USD | `-62.69%` | `79,269,000,000.00` |
| `Live` | `Long` | `270.50` | 4,320,000.00 USD | 0.00 USD | 814.20 USD | `-62.27%` | `3,010,000,000.00` |
| `Live` | `Long` | `284.50` | 4,320,000.00 USD | 0.00 USD | 11,380.00 USD | `-60.31%` | `40,000,000,000.00` |
| `Live` | `Long` | `292.50` | 4,300,000.00 USD | 0.00 USD | 7,270.00 USD | `-59.20%` | `24,863,000,000.00` |
| `Live` | `Long` | `303.50` | 4,300,000.00 USD | 0.00 USD | 150,800.00 USD | `-57.66%` | `496,876,000,000.00` |
| `Live` | `Long` | `312.50` | 4,150,000.00 USD | 0.00 USD | 500.00 USD | `-56.41%` | `1,600,000,000.00` |
| `Live` | `Long` | `316.50` | 4,150,000.00 USD | 0.00 USD | 126,600.00 USD | `-55.85%` | `400,000,000,000.00` |
| `Live` | `Long` | `326.50` | 4,020,000.00 USD | 0.00 USD | 500.85 USD | `-54.46%` | `1,534,000,000.00` |
| `Live` | `Long` | `327.50` | 4,020,000.00 USD | 0.00 USD | 314.07 USD | `-54.32%` | `959,000,000.00` |
| `Live` | `Long` | `332.50` | 4,020,000.00 USD | 0.00 USD | 150.29 USD | `-53.62%` | `452,000,000.00` |
| `Live` | `Long` | `333.50` | 4,020,000.00 USD | 0.00 USD | 226.45 USD | `-53.48%` | `679,000,000.00` |
| `Live` | `Long` | `337.50` | 4,020,000.00 USD | 0.00 USD | 1,060.00 USD | `-52.92%` | `3,147,000,000.00` |
| `Live` | `Long` | `339.50` | 4,020,000.00 USD | 0.00 USD | 9,350.00 USD | `-52.64%` | `27,554,000,000.00` |
| `Live` | `Long` | `340.50` | 4,010,000.00 USD | 0.00 USD | 120.20 USD | `-52.50%` | `353,000,000.00` |
| `Live` | `Long` | `342.50` | 4,010,000.00 USD | 0.00 USD | 1,600.00 USD | `-52.22%` | `4,667,000,000.00` |
| `Live` | `Long` | `348.50` | 4,010,000.00 USD | 0.00 USD | 6,130.00 USD | `-51.39%` | `17,576,000,000.00` |
| `Live` | `Long` | `356.50` | 4,000,000.00 USD | 0.00 USD | 3,570.00 USD | `-50.27%` | `10,019,000,000.00` |
| `Live` | `Long` | `359.50` | 4,000,000.00 USD | 0.00 USD | 212.10 USD | `-49.85%` | `590,000,000.00` |
| `Live` | `Long` | `363.50` | 4,000,000.00 USD | 0.00 USD | 340.60 USD | `-49.29%` | `937,000,000.00` |
| `Live` | `Long` | `364.50` | 4,000,000.00 USD | 0.00 USD | 1,640.00 USD | `-49.15%` | `4,504,000,000.00` |
| `Live` | `Long` | `366.50` | 3,990,000.00 USD | 0.00 USD | 549.75 USD | `-48.88%` | `1,500,000,000.00` |
| `Live` | `Long` | `367.50` | 3,990,000.00 USD | 0.00 USD | 146.63 USD | `-48.74%` | `399,000,000.00` |
| `Live` | `Long` | `368.50` | 3,990,000.00 USD | 0.00 USD | 15,810.00 USD | `-48.60%` | `42,904,000,000.00` |
| `Live` | `Long` | `369.50` | 3,980,000.00 USD | 0.00 USD | 16,630.00 USD | `-48.46%` | `45,000,000,000.00` |
| `Live` | `Long` | `371.50` | 3,960,000.00 USD | 0.00 USD | 146.37 USD | `-48.18%` | `394,000,000.00` |
| `Live` | `Long` | `372.50` | 3,960,000.00 USD | 0.00 USD | 10,510.00 USD | `-48.04%` | `28,204,000,000.00` |
| `Live` | `Long` | `373.50` | 3,950,000.00 USD | 0.00 USD | 15,910.00 USD | `-47.90%` | `42,597,000,000.00` |
| `Live` | `Long` | `374.50` | 3,930,000.00 USD | 0.00 USD | 1,820.00 USD | `-47.76%` | `4,868,000,000.00` |
| `Live` | `Long` | `377.50` | 3,930,000.00 USD | 0.00 USD | 3,260.00 USD | `-47.34%` | `8,631,000,000.00` |
| `Live` | `Long` | `378.50` | 3,930,000.00 USD | 0.00 USD | 643.45 USD | `-47.20%` | `1,700,000,000.00` |
| `Live` | `Long` | `381.50` | 3,930,000.00 USD | 0.00 USD | 1,910.00 USD | `-46.78%` | `5,000,000,000.00` |
| `Live` | `Long` | `383.50` | 3,930,000.00 USD | 0.00 USD | 10,900.00 USD | `-46.50%` | `28,414,000,000.00` |
| `Live` | `Long` | `384.50` | 3,920,000.00 USD | 0.00 USD | 1,060.00 USD | `-46.36%` | `2,746,000,000.00` |
| `Live` | `Long` | `385.50` | 3,910,000.00 USD | 0.00 USD | 1,800.00 USD | `-46.23%` | `4,675,000,000.00` |
| `Live` | `Long` | `386.50` | 3,910,000.00 USD | 0.00 USD | 531.44 USD | `-46.09%` | `1,375,000,000.00` |
| `Live` | `Long` | `387.50` | 3,910,000.00 USD | 0.00 USD | 392.54 USD | `-45.95%` | `1,013,000,000.00` |
| `Live` | `Long` | `393.50` | 3,910,000.00 USD | 0.00 USD | 536.73 USD | `-45.11%` | `1,364,000,000.00` |
| `Live` | `Long` | `394.50` | 3,910,000.00 USD | 0.00 USD | 29,460.00 USD | `-44.97%` | `74,671,000,000.00` |
| `Live` | `Long` | `395.50` | 3,880,000.00 USD | 0.00 USD | 2,110.00 USD | `-44.83%` | `5,347,000,000.00` |
| `Live` | `Long` | `396.50` | 3,880,000.00 USD | 0.00 USD | 317.20 USD | `-44.69%` | `800,000,000.00` |
| `Live` | `Long` | `398.50` | 3,880,000.00 USD | 0.00 USD | 523.63 USD | `-44.41%` | `1,314,000,000.00` |
| `Live` | `Long` | `399.50` | 3,880,000.00 USD | 0.00 USD | 603.64 USD | `-44.27%` | `1,511,000,000.00` |
| `Live` | `Long` | `404.50` | 3,880,000.00 USD | 0.00 USD | 102.34 USD | `-43.57%` | `253,000,000.00` |
| `Live` | `Long` | `405.50` | 3,880,000.00 USD | 0.00 USD | 7,700.00 USD | `-43.44%` | `19,000,000,000.00` |
| `Live` | `Long` | `409.50` | 3,870,000.00 USD | 0.00 USD | 613.02 USD | `-42.88%` | `1,497,000,000.00` |
| `Live` | `Long` | `410.50` | 3,870,000.00 USD | 0.00 USD | 105.91 USD | `-42.74%` | `258,000,000.00` |
| `Live` | `Long` | `411.50` | 3,870,000.00 USD | 0.00 USD | 5,810.00 USD | `-42.60%` | `14,117,000,000.00` |
| `Live` | `Long` | `412.50` | 3,860,000.00 USD | 0.00 USD | 3,490.00 USD | `-42.46%` | `8,455,000,000.00` |
| `Live` | `Long` | `413.50` | 3,860,000.00 USD | 0.00 USD | 11,400.00 USD | `-42.32%` | `27,562,000,000.00` |
| `Live` | `Long` | `414.50` | 3,850,000.00 USD | 0.00 USD | 1,890.00 USD | `-42.18%` | `4,566,000,000.00` |
| `Live` | `Long` | `415.50` | 3,850,000.00 USD | 0.00 USD | 1,810.00 USD | `-42.04%` | `4,368,000,000.00` |
| `Live` | `Long` | `416.50` | 3,850,000.00 USD | 0.00 USD | 644.33 USD | `-41.90%` | `1,547,000,000.00` |
| `Live` | `Long` | `417.50` | 3,840,000.00 USD | 0.00 USD | 7,140.00 USD | `-41.76%` | `17,092,000,000.00` |
| `Live` | `Long` | `418.50` | 3,840,000.00 USD | 0.00 USD | 318.06 USD | `-41.62%` | `760,000,000.00` |
| `Live` | `Long` | `419.50` | 3,840,000.00 USD | 0.00 USD | 2,650.00 USD | `-41.48%` | `6,316,000,000.00` |
| `Live` | `Long` | `420.50` | 3,830,000.00 USD | 0.00 USD | 29,430.00 USD | `-41.34%` | `70,000,000,000.00` |
| `Live` | `Long` | `421.50` | 3,800,000.00 USD | 0.00 USD | 2,320.00 USD | `-41.20%` | `5,496,000,000.00` |
| `Live` | `Long` | `422.50` | 3,800,000.00 USD | 0.00 USD | 5,270.00 USD | `-41.06%` | `12,484,000,000.00` |
| `Live` | `Long` | `426.50` | 3,800,000.00 USD | 0.00 USD | 183.40 USD | `-40.51%` | `430,000,000.00` |
| `Live` | `Long` | `429.50` | 3,800,000.00 USD | 0.00 USD | 846.12 USD | `-40.09%` | `1,970,000,000.00` |
| `Live` | `Long` | `430.50` | 3,800,000.00 USD | 0.00 USD | 910.51 USD | `-39.95%` | `2,115,000,000.00` |
| `Live` | `Long` | `431.50` | 3,800,000.00 USD | 0.00 USD | 612.73 USD | `-39.81%` | `1,420,000,000.00` |
| `Live` | `Long` | `434.50` | 3,790,000.00 USD | 0.00 USD | 622.20 USD | `-39.39%` | `1,432,000,000.00` |
| `Live` | `Long` | `436.50` | 3,790,000.00 USD | 0.00 USD | 133.13 USD | `-39.11%` | `305,000,000.00` |
| `Live` | `Long` | `437.50` | 3,790,000.00 USD | 0.00 USD | 1,430.00 USD | `-38.97%` | `3,259,000,000.00` |
| `Live` | `Long` | `438.50` | 3,790,000.00 USD | 0.00 USD | 1,790.00 USD | `-38.83%` | `4,087,000,000.00` |
| `Live` | `Long` | `448.50` | 3,790,000.00 USD | 0.00 USD | 3,350.00 USD | `-37.44%` | `7,470,000,000.00` |
| `Live` | `Long` | `451.50` | 3,790,000.00 USD | 0.00 USD | 647.00 USD | `-37.02%` | `1,433,000,000.00` |
| `Live` | `Long` | `456.50` | 3,790,000.00 USD | 0.00 USD | 4,730.00 USD | `-36.32%` | `10,359,000,000.00` |
| `Live` | `Long` | `464.50` | 3,780,000.00 USD | 0.00 USD | 396.68 USD | `-35.21%` | `854,000,000.00` |
| `Live` | `Long` | `468.50` | 3,780,000.00 USD | 0.00 USD | 7,030.00 USD | `-34.65%` | `15,000,000,000.00` |
| `Live` | `Long` | `469.50` | 3,770,000.00 USD | 0.00 USD | 4,370.00 USD | `-34.51%` | `9,301,000,000.00` |
| `Live` | `Long` | `475.50` | 3,770,000.00 USD | 0.00 USD | 5,320.00 USD | `-33.67%` | `11,182,000,000.00` |
| `Live` | `Long` | `478.50` | 3,770,000.00 USD | 0.00 USD | 2,600.00 USD | `-33.25%` | `5,431,000,000.00` |
| `Live` | `Long` | `481.50` | 3,760,000.00 USD | 0.00 USD | 615.36 USD | `-32.83%` | `1,278,000,000.00` |
| `Live` | `Long` | `482.50` | 3,760,000.00 USD | 0.00 USD | 8,140.00 USD | `-32.69%` | `16,866,000,000.00` |
| `Live` | `Long` | `484.50` | 3,750,000.00 USD | 0.00 USD | 3,330.00 USD | `-32.42%` | `6,864,000,000.00` |
| `Live` | `Long` | `485.50` | 3,750,000.00 USD | 0.00 USD | 2,400.00 USD | `-32.28%` | `4,947,000,000.00` |
| `Live` | `Long` | `487.50` | 3,750,000.00 USD | 0.00 USD | 464.59 USD | `-32.00%` | `953,000,000.00` |
| `Live` | `Long` | `488.50` | 3,750,000.00 USD | 0.00 USD | 2,300.00 USD | `-31.86%` | `4,712,000,000.00` |
| `Live` | `Long` | `492.50` | 3,750,000.00 USD | 0.00 USD | 281.22 USD | `-31.30%` | `571,000,000.00` |
| `Live` | `Long` | `493.50` | 3,740,000.00 USD | 0.00 USD | 1,840.00 USD | `-31.16%` | `3,720,000,000.00` |
| `Live` | `Long` | `494.50` | 3,740,000.00 USD | 0.00 USD | 857.46 USD | `-31.02%` | `1,734,000,000.00` |
| `Live` | `Long` | `498.50` | 3,740,000.00 USD | 0.00 USD | 1,820.00 USD | `-30.46%` | `3,656,000,000.00` |
| `Live` | `Long` | `499.50` | 3,740,000.00 USD | 0.00 USD | 13,880.00 USD | `-30.32%` | `27,793,000,000.00` |
| `Live` | `Long` | `501.50` | 3,730,000.00 USD | 0.00 USD | 7,760.00 USD | `-30.04%` | `15,482,000,000.00` |
| `Live` | `Long` | `502.50` | 3,720,000.00 USD | 0.00 USD | 60,380.00 USD | `-29.90%` | `120,157,000,000.00` |
| `Live` | `Long` | `505.50` | 3,660,000.00 USD | 0.00 USD | 5,760.00 USD | `-29.49%` | `11,387,000,000.00` |
| `Live` | `Long` | `507.50` | 3,650,000.00 USD | 0.00 USD | 2,380.00 USD | `-29.21%` | `4,692,000,000.00` |
| `Live` | `Long` | `508.50` | 3,650,000.00 USD | 0.00 USD | 53,270.00 USD | `-29.07%` | `104,762,000,000.00` |
| `Live` | `Long` | `509.50` | 3,600,000.00 USD | 0.00 USD | 3,100.00 USD | `-28.93%` | `6,091,000,000.00` |
| `Live` | `Long` | `510.50` | 3,590,000.00 USD | 0.00 USD | 4,080.00 USD | `-28.79%` | `8,000,000,000.00` |
| `Live` | `Long` | `511.50` | 3,590,000.00 USD | 0.00 USD | 5,180.00 USD | `-28.65%` | `10,118,000,000.00` |
| `Live` | `Long` | `512.50` | 3,580,000.00 USD | 0.00 USD | 41,220.00 USD | `-28.51%` | `80,432,000,000.00` |
| `Live` | `Long` | `513.50` | 3,540,000.00 USD | 0.00 USD | 2,520.00 USD | `-28.37%` | `4,914,000,000.00` |
| `Live` | `Long` | `514.50` | 3,540,000.00 USD | 0.00 USD | 701.78 USD | `-28.23%` | `1,364,000,000.00` |
| `Live` | `Long` | `515.50` | 3,540,000.00 USD | 0.00 USD | 5,990.00 USD | `-28.09%` | `11,621,000,000.00` |
| `Live` | `Long` | `516.50` | 3,530,000.00 USD | 0.00 USD | 481.89 USD | `-27.95%` | `933,000,000.00` |
| `Live` | `Long` | `517.50` | 3,530,000.00 USD | 0.00 USD | 22,650.00 USD | `-27.81%` | `43,765,000,000.00` |
| `Live` | `Long` | `519.50` | 3,510,000.00 USD | 0.00 USD | 968.35 USD | `-27.53%` | `1,864,000,000.00` |
| `Live` | `Long` | `520.50` | 3,510,000.00 USD | 0.00 USD | 272.22 USD | `-27.39%` | `523,000,000.00` |
| `Live` | `Long` | `521.50` | 3,510,000.00 USD | 0.00 USD | 75,990.00 USD | `-27.25%` | `145,717,000,000.00` |
| `Live` | `Long` | `522.50` | 3,430,000.00 USD | 0.00 USD | 2,090.00 USD | `-27.11%` | `3,993,000,000.00` |
| `Live` | `Long` | `524.50` | 3,430,000.00 USD | 0.00 USD | 833.43 USD | `-26.84%` | `1,589,000,000.00` |
| `Live` | `Long` | `526.50` | 3,430,000.00 USD | 0.00 USD | 3,320.00 USD | `-26.56%` | `6,306,000,000.00` |
| `Live` | `Long` | `527.50` | 3,430,000.00 USD | 0.00 USD | 179,790.00 USD | `-26.42%` | `340,839,000,000.00` |
| `Live` | `Long` | `529.50` | 3,250,000.00 USD | 0.00 USD | 42,820.00 USD | `-26.14%` | `80,869,000,000.00` |
| `Live` | `Long` | `530.50` | 3,200,000.00 USD | 0.00 USD | 18,050.00 USD | `-26.00%` | `34,028,000,000.00` |
| `Live` | `Long` | `531.50` | 3,190,000.00 USD | 0.00 USD | 484.73 USD | `-25.86%` | `912,000,000.00` |
| `Live` | `Long` | `532.50` | 3,190,000.00 USD | 0.00 USD | 422.81 USD | `-25.72%` | `794,000,000.00` |
| `Live` | `Long` | `534.50` | 3,190,000.00 USD | 0.00 USD | 555.35 USD | `-25.44%` | `1,039,000,000.00` |
| `Live` | `Long` | `535.50` | 3,190,000.00 USD | 0.00 USD | 100.14 USD | `-25.30%` | `187,000,000.00` |
| `Live` | `Long` | `539.50` | 3,190,000.00 USD | 0.00 USD | 490.94 USD | `-24.74%` | `910,000,000.00` |
| `Live` | `Long` | `540.50` | 3,180,000.00 USD | 0.00 USD | 471.32 USD | `-24.60%` | `872,000,000.00` |
| `Live` | `Long` | `543.50` | 3,180,000.00 USD | 0.00 USD | 2,680.00 USD | `-24.19%` | `4,927,000,000.00` |
| `Live` | `Long` | `544.50` | 3,180,000.00 USD | 0.00 USD | 210,830.00 USD | `-24.05%` | `387,204,000,000.00` |
| `Live` | `Long` | `545.50` | 2,970,000.00 USD | 0.00 USD | 1,580.00 USD | `-23.91%` | `2,900,000,000.00` |
| `Live` | `Long` | `546.50` | 2,970,000.00 USD | 0.00 USD | 530.11 USD | `-23.77%` | `970,000,000.00` |
| `Live` | `Long` | `548.50` | 2,970,000.00 USD | 0.00 USD | 1,980.00 USD | `-23.49%` | `3,611,000,000.00` |
| `Live` | `Long` | `549.50` | 2,970,000.00 USD | 0.00 USD | 1,370.00 USD | `-23.35%` | `2,496,000,000.00` |
| `Live` | `Long` | `550.50` | 2,970,000.00 USD | 0.00 USD | 633.63 USD | `-23.21%` | `1,151,000,000.00` |
| `Live` | `Long` | `551.50` | 2,960,000.00 USD | 0.00 USD | 1,250.00 USD | `-23.07%` | `2,271,000,000.00` |
| `Live` | `Long` | `552.50` | 2,960,000.00 USD | 0.00 USD | 24,120.00 USD | `-22.93%` | `43,665,000,000.00` |
| `Live` | `Long` | `553.50` | 2,940,000.00 USD | 0.00 USD | 3,080.00 USD | `-22.79%` | `5,565,000,000.00` |
| `Live` | `Long` | `556.50` | 2,940,000.00 USD | 0.00 USD | 5,670.00 USD | `-22.37%` | `10,193,000,000.00` |
| `Live` | `Long` | `557.50` | 2,930,000.00 USD | 0.00 USD | 10,020.00 USD | `-22.23%` | `17,967,000,000.00` |
| `Live` | `Long` | `558.50` | 2,920,000.00 USD | 0.00 USD | 212.23 USD | `-22.09%` | `380,000,000.00` |
| `Live` | `Long` | `560.50` | 2,920,000.00 USD | 0.00 USD | 582.36 USD | `-21.81%` | `1,039,000,000.00` |
| `Live` | `Long` | `568.50` | 2,920,000.00 USD | 0.00 USD | 454.80 USD | `-20.70%` | `800,000,000.00` |
| `Live` | `Long` | `569.50` | 2,920,000.00 USD | 0.00 USD | 144.08 USD | `-20.56%` | `253,000,000.00` |
| `Live` | `Long` | `571.50` | 2,920,000.00 USD | 0.00 USD | 712,740.00 USD | `-20.28%` | `1,247,135,000,000.00` |
| `Live` | `Long` | `572.50` | 2,210,000.00 USD | 0.00 USD | 8,800.00 USD | `-20.14%` | `15,374,000,000.00` |
| `Live` | `Long` | `574.50` | 2,200,000.00 USD | 0.00 USD | 163,310.00 USD | `-19.86%` | `284,263,000,000.00` |
| `Live` | `Long` | `576.50` | 2,030,000.00 USD | 0.00 USD | 4,810.00 USD | `-19.58%` | `8,349,000,000.00` |
| `Live` | `Long` | `578.50` | 2,030,000.00 USD | 0.00 USD | 7,640.00 USD | `-19.30%` | `13,202,000,000.00` |
| `Live` | `Long` | `580.50` | 2,020,000.00 USD | 0.00 USD | 35,850.00 USD | `-19.02%` | `61,765,000,000.00` |
| `Live` | `Long` | `581.50` | 1,990,000.00 USD | 0.00 USD | 580.34 USD | `-18.88%` | `998,000,000.00` |
| `Live` | `Long` | `582.50` | 1,990,000.00 USD | 0.00 USD | 1,540.00 USD | `-18.75%` | `2,646,000,000.00` |
| `Live` | `Long` | `583.50` | 1,980,000.00 USD | 0.00 USD | 3,470.00 USD | `-18.61%` | `5,952,000,000.00` |
| `Live` | `Long` | `585.50` | 1,980,000.00 USD | 0.00 USD | 210.19 USD | `-18.33%` | `359,000,000.00` |
| `Live` | `Long` | `586.50` | 1,980,000.00 USD | 0.00 USD | 2,360.00 USD | `-18.19%` | `4,022,000,000.00` |
| `Live` | `Long` | `587.50` | 1,980,000.00 USD | 0.00 USD | 5,340.00 USD | `-18.05%` | `9,096,000,000.00` |
| `Live` | `Long` | `588.50` | 1,970,000.00 USD | 0.00 USD | 397.24 USD | `-17.91%` | `675,000,000.00` |
| `Live` | `Long` | `589.50` | 1,970,000.00 USD | 0.00 USD | 10,820.00 USD | `-17.77%` | `18,352,000,000.00` |
| `Live` | `Long` | `590.50` | 1,960,000.00 USD | 0.00 USD | 2,560.00 USD | `-17.63%` | `4,334,000,000.00` |
| `Live` | `Long` | `591.50` | 1,960,000.00 USD | 0.00 USD | 619.30 USD | `-17.49%` | `1,047,000,000.00` |
| `Live` | `Long` | `592.50` | 1,960,000.00 USD | 0.00 USD | 840.76 USD | `-17.35%` | `1,419,000,000.00` |
| `Live` | `Long` | `593.50` | 1,960,000.00 USD | 0.00 USD | 53,660.00 USD | `-17.21%` | `90,410,000,000.00` |
| `Live` | `Long` | `594.50` | 1,900,000.00 USD | 0.00 USD | 8,860.00 USD | `-17.07%` | `14,906,000,000.00` |
| `Live` | `Long` | `595.50` | 1,890,000.00 USD | 0.00 USD | 3,000.00 USD | `-16.93%` | `5,043,000,000.00` |
| `Live` | `Long` | `596.50` | 1,890,000.00 USD | 0.00 USD | 8,910.00 USD | `-16.79%` | `14,934,000,000.00` |
| `Live` | `Long` | `597.50` | 1,880,000.00 USD | 0.00 USD | 2,390.00 USD | `-16.65%` | `3,998,000,000.00` |
| `Live` | `Long` | `598.50` | 1,880,000.00 USD | 0.00 USD | 1,100.00 USD | `-16.51%` | `1,832,000,000.00` |
| `Live` | `Long` | `600.50` | 1,880,000.00 USD | 0.00 USD | 945.19 USD | `-16.23%` | `1,574,000,000.00` |
| `Live` | `Long` | `601.50` | 1,880,000.00 USD | 0.00 USD | 16,880.00 USD | `-16.09%` | `28,061,000,000.00` |
| `Live` | `Long` | `602.50` | 1,860,000.00 USD | 0.00 USD | 418.13 USD | `-15.96%` | `694,000,000.00` |
| `Live` | `Long` | `603.50` | 1,860,000.00 USD | 0.00 USD | 23,410.00 USD | `-15.82%` | `38,785,000,000.00` |
| `Live` | `Long` | `604.50` | 1,840,000.00 USD | 0.00 USD | 256.91 USD | `-15.68%` | `425,000,000.00` |
| `Live` | `Long` | `605.50` | 1,840,000.00 USD | 0.00 USD | 4,240.00 USD | `-15.54%` | `7,002,000,000.00` |
| `Live` | `Long` | `606.50` | 1,830,000.00 USD | 0.00 USD | 1,880.00 USD | `-15.40%` | `3,092,000,000.00` |
| `Live` | `Long` | `607.50` | 1,830,000.00 USD | 0.00 USD | 58,610.00 USD | `-15.26%` | `96,477,000,000.00` |
| `Live` | `Long` | `609.50` | 1,770,000.00 USD | 0.00 USD | 213.32 USD | `-14.98%` | `350,000,000.00` |
| `Live` | `Long` | `611.50` | 1,770,000.00 USD | 0.00 USD | 1,580.00 USD | `-14.70%` | `2,584,000,000.00` |
| `Live` | `Long` | `612.50` | 1,770,000.00 USD | 0.00 USD | 12,250.00 USD | `-14.56%` | `20,000,000,000.00` |
| `Live` | `Long` | `613.50` | 1,760,000.00 USD | 0.00 USD | 120.25 USD | `-14.42%` | `196,000,000.00` |
| `Live` | `Long` | `614.50` | 1,760,000.00 USD | 0.00 USD | 4,280.00 USD | `-14.28%` | `6,973,000,000.00` |
| `Live` | `Long` | `616.50` | 1,750,000.00 USD | 0.00 USD | 1,540.00 USD | `-14.00%` | `2,500,000,000.00` |
| `Live` | `Long` | `617.50` | 1,750,000.00 USD | 0.00 USD | 156.23 USD | `-13.86%` | `253,000,000.00` |
| `Live` | `Long` | `618.50` | 1,750,000.00 USD | 0.00 USD | 932.70 USD | `-13.72%` | `1,508,000,000.00` |
| `Live` | `Long` | `619.50` | 1,750,000.00 USD | 0.00 USD | 1,410.00 USD | `-13.58%` | `2,279,000,000.00` |
| `Live` | `Long` | `620.50` | 1,750,000.00 USD | 0.00 USD | 6,520.00 USD | `-13.44%` | `10,506,000,000.00` |
| `Live` | `Long` | `621.50` | 1,740,000.00 USD | 0.00 USD | 13,930.00 USD | `-13.30%` | `22,412,000,000.00` |
| `Live` | `Long` | `624.50` | 1,730,000.00 USD | 0.00 USD | 3,690.00 USD | `-12.89%` | `5,905,000,000.00` |
| `Live` | `Long` | `625.50` | 1,730,000.00 USD | 0.00 USD | 14,200.00 USD | `-12.75%` | `22,702,000,000.00` |
| `Live` | `Long` | `626.50` | 1,710,000.00 USD | 0.00 USD | 964.81 USD | `-12.61%` | `1,540,000,000.00` |
| `Live` | `Long` | `627.50` | 1,710,000.00 USD | 0.00 USD | 104.17 USD | `-12.47%` | `166,000,000.00` |
| `Live` | `Long` | `630.50` | 1,710,000.00 USD | 0.00 USD | 9,600.00 USD | `-12.05%` | `15,225,000,000.00` |
| `Live` | `Long` | `631.50` | 1,700,000.00 USD | 0.00 USD | 2,900.00 USD | `-11.91%` | `4,587,000,000.00` |
| `Live` | `Long` | `632.50` | 1,700,000.00 USD | 0.00 USD | 3,560.00 USD | `-11.77%` | `5,633,000,000.00` |
| `Live` | `Long` | `634.50` | 1,690,000.00 USD | 0.00 USD | 6,660.00 USD | `-11.49%` | `10,489,000,000.00` |
| `Live` | `Long` | `635.50` | 1,690,000.00 USD | 0.00 USD | 155.06 USD | `-11.35%` | `244,000,000.00` |
| `Live` | `Long` | `636.50` | 1,690,000.00 USD | 0.00 USD | 1,110.00 USD | `-11.21%` | `1,743,000,000.00` |
| `Live` | `Long` | `637.50` | 1,690,000.00 USD | 0.00 USD | 305.36 USD | `-11.07%` | `479,000,000.00` |
| `Live` | `Long` | `638.50` | 1,690,000.00 USD | 0.00 USD | 6,710.00 USD | `-10.93%` | `10,515,000,000.00` |
| `Live` | `Long` | `639.50` | 1,680,000.00 USD | 0.00 USD | 127.26 USD | `-10.79%` | `199,000,000.00` |
| `Live` | `Long` | `640.50` | 1,680,000.00 USD | 0.00 USD | 1,320,000.00 USD | `-10.65%` | `2,059,954,000,000.00` |
| `Live` | `Long` | `642.50` | 360,330.00 USD | 0.00 USD | 8,480.00 USD | `-10.38%` | `13,199,000,000.00` |
| `Live` | `Long` | `643.50` | 351,850.00 USD | 0.00 USD | 339.12 USD | `-10.24%` | `527,000,000.00` |
| `Live` | `Long` | `646.50` | 351,510.00 USD | 0.00 USD | 463.54 USD | `-9.82%` | `717,000,000.00` |
| `Live` | `Long` | `648.50` | 351,050.00 USD | 0.00 USD | 1,940.00 USD | `-9.54%` | `2,988,000,000.00` |
| `Live` | `Long` | `649.50` | 349,110.00 USD | 0.00 USD | 1,620.00 USD | `-9.40%` | `2,501,000,000.00` |
| `Live` | `Long` | `650.50` | 347,480.00 USD | 0.00 USD | 2,090.00 USD | `-9.26%` | `3,218,000,000.00` |
| `Live` | `Long` | `651.50` | 345,390.00 USD | 0.00 USD | 9,650.00 USD | `-9.12%` | `14,806,000,000.00` |
| `Live` | `Long` | `652.50` | 335,740.00 USD | 0.00 USD | 652.50 USD | `-8.98%` | `1,000,000,000.00` |
| `Live` | `Long` | `653.50` | 335,090.00 USD | 0.00 USD | 97,380.00 USD | `-8.84%` | `149,014,000,000.00` |
| `Live` | `Long` | `654.50` | 237,710.00 USD | 0.00 USD | 100.14 USD | `-8.70%` | `153,000,000.00` |
| `Live` | `Long` | `655.50` | 237,610.00 USD | 0.00 USD | 437.87 USD | `-8.56%` | `668,000,000.00` |
| `Live` | `Long` | `658.50` | 237,170.00 USD | 0.00 USD | 15,090.00 USD | `-8.14%` | `22,916,000,000.00` |
| `Live` | `Long` | `659.50` | 222,080.00 USD | 0.00 USD | 46,450.00 USD | `-8.00%` | `70,433,000,000.00` |
| `Live` | `Long` | `660.50` | 175,630.00 USD | 0.00 USD | 3,410.00 USD | `-7.86%` | `5,167,000,000.00` |
| `Live` | `Long` | `661.50` | 172,220.00 USD | 0.00 USD | 20,140.00 USD | `-7.73%` | `30,450,000,000.00` |
| `Live` | `Long` | `662.50` | 152,080.00 USD | 0.00 USD | 2,850.00 USD | `-7.59%` | `4,297,000,000.00` |
| `Live` | `Long` | `663.50` | 149,230.00 USD | 0.00 USD | 9,230.00 USD | `-7.45%` | `13,911,000,000.00` |
| `Live` | `Long` | `664.50` | 140,000.00 USD | 0.00 USD | 24,100.00 USD | `-7.31%` | `36,261,000,000.00` |
| `Live` | `Long` | `665.50` | 115,900.00 USD | 0.00 USD | 10,950.00 USD | `-7.17%` | `16,447,000,000.00` |
| `Live` | `Long` | `666.50` | 104,960.00 USD | 0.00 USD | 1,930.00 USD | `-7.03%` | `2,894,000,000.00` |
| `Live` | `Long` | `667.50` | 103,030.00 USD | 0.00 USD | 1,380.00 USD | `-6.89%` | `2,067,000,000.00` |
| `Live` | `Long` | `668.50` | 101,650.00 USD | 0.00 USD | 1,450.00 USD | `-6.75%` | `2,164,000,000.00` |
| `Live` | `Long` | `669.50` | 100,200.00 USD | 0.00 USD | 2,930.00 USD | `-6.61%` | `4,371,000,000.00` |
| `Live` | `Long` | `670.50` | 97,280.00 USD | 0.00 USD | 6,110.00 USD | `-6.47%` | `9,113,000,000.00` |
| `Live` | `Long` | `671.50` | 91,170.00 USD | 0.00 USD | 832.66 USD | `-6.33%` | `1,240,000,000.00` |
| `Live` | `Long` | `672.50` | 90,330.00 USD | 0.00 USD | 6,920.00 USD | `-6.19%` | `10,292,000,000.00` |
| `Live` | `Long` | `673.50` | 83,410.00 USD | 0.00 USD | 41,240.00 USD | `-6.05%` | `61,234,000,000.00` |
| `Live` | `Long` | `674.50` | 42,170.00 USD | 0.00 USD | 4,310.00 USD | `-5.91%` | `6,384,000,000.00` |
| `Live` | `Long` | `675.50` | 37,870.00 USD | 0.00 USD | 9,430.00 USD | `-5.77%` | `13,967,000,000.00` |
| `Live` | `Long` | `676.50` | 28,430.00 USD | 0.00 USD | 1,660.00 USD | `-5.63%` | `2,453,000,000.00` |
| `Live` | `Long` | `677.50` | 26,770.00 USD | 0.00 USD | 438.34 USD | `-5.49%` | `647,000,000.00` |
| `Live` | `Long` | `678.50` | 26,330.00 USD | 0.00 USD | 417.96 USD | `-5.35%` | `616,000,000.00` |
| `Live` | `Long` | `679.50` | 25,920.00 USD | 0.00 USD | 3,510.00 USD | `-5.21%` | `5,171,000,000.00` |
| `Live` | `Long` | `680.50` | 22,400.00 USD | 0.00 USD | 21,460.00 USD | `-5.07%` | `31,539,000,000.00` |
| `Live` | `Long` | `681.50` | 939.79 USD | 0.00 USD | 939.79 USD | `-4.94%` | `1,379,000,000.00` |
| `Live` | `Short` | `682.50` | 345.35 USD | 345.35 USD | 0.00 USD | `-4.80%` | `506,000,000.00` |
| `Live` | `Short` | `709.50` | 1,750.00 USD | 1,400.00 USD | 0.00 USD | `-1.03%` | `1,973,000,000.00` |
| `Live` | `Short` | `720.50` | 1,910.00 USD | 161.39 USD | 0.00 USD | `+0.50%` | `224,000,000.00` |
| `Live` | `Short` | `721.50` | 35,170.00 USD | 33,260.00 USD | 0.00 USD | `+0.64%` | `46,099,000,000.00` |
| `Live` | `Short` | `722.50` | 35,730.00 USD | 566.44 USD | 0.00 USD | `+0.78%` | `784,000,000.00` |
| `Live` | `Short` | `723.50` | 39,290.00 USD | 3,560.00 USD | 0.00 USD | `+0.92%` | `4,914,000,000.00` |
| `Live` | `Short` | `724.50` | 39,810.00 USD | 525.26 USD | 0.00 USD | `+1.06%` | `725,000,000.00` |
| `Live` | `Short` | `725.50` | 41,340.00 USD | 1,530.00 USD | 0.00 USD | `+1.20%` | `2,108,000,000.00` |
| `Live` | `Short` | `726.50` | 45,180.00 USD | 3,840.00 USD | 0.00 USD | `+1.34%` | `5,285,000,000.00` |
| `Live` | `Short` | `727.50` | 46,210.00 USD | 1,030.00 USD | 0.00 USD | `+1.48%` | `1,418,000,000.00` |
| `Live` | `Short` | `728.50` | 88,150.00 USD | 41,940.00 USD | 0.00 USD | `+1.62%` | `57,570,000,000.00` |
| `Live` | `Short` | `729.50` | 262,520.00 USD | 174,370.00 USD | 0.00 USD | `+1.76%` | `239,020,000,000.00` |
| `Live` | `Short` | `730.50` | 286,610.00 USD | 24,090.00 USD | 0.00 USD | `+1.90%` | `32,978,000,000.00` |
| `Live` | `Short` | `731.50` | 293,950.00 USD | 7,340.00 USD | 0.00 USD | `+2.04%` | `10,036,000,000.00` |
| `Live` | `Short` | `732.50` | 430,870.00 USD | 136,920.00 USD | 0.00 USD | `+2.18%` | `186,920,000,000.00` |
| `Live` | `Short` | `733.50` | 516,930.00 USD | 86,060.00 USD | 0.00 USD | `+2.32%` | `117,333,000,000.00` |
| `Live` | `Short` | `734.50` | 669,410.00 USD | 152,470.00 USD | 0.00 USD | `+2.46%` | `207,590,000,000.00` |
| `Live` | `Short` | `735.50` | 692,400.00 USD | 22,990.00 USD | 0.00 USD | `+2.60%` | `31,262,000,000.00` |
| `Live` | `Short` | `736.50` | 705,960.00 USD | 13,550.00 USD | 0.00 USD | `+2.74%` | `18,404,000,000.00` |
| `Live` | `Short` | `737.50` | 708,970.00 USD | 3,010.00 USD | 0.00 USD | `+2.88%` | `4,082,000,000.00` |
| `Live` | `Short` | `738.50` | 715,170.00 USD | 6,210.00 USD | 0.00 USD | `+3.02%` | `8,405,000,000.00` |
| `Live` | `Short` | `739.50` | 723,170.00 USD | 8,000.00 USD | 0.00 USD | `+3.16%` | `10,816,000,000.00` |
| `Live` | `Short` | `740.50` | 727,150.00 USD | 3,980.00 USD | 0.00 USD | `+3.29%` | `5,376,000,000.00` |
| `Live` | `Short` | `741.50` | 735,940.00 USD | 8,790.00 USD | 0.00 USD | `+3.43%` | `11,850,000,000.00` |
| `Live` | `Short` | `742.50` | 747,550.00 USD | 11,610.00 USD | 0.00 USD | `+3.57%` | `15,634,000,000.00` |
| `Live` | `Short` | `743.50` | 850,670.00 USD | 103,120.00 USD | 0.00 USD | `+3.71%` | `138,696,000,000.00` |
| `Live` | `Short` | `744.50` | 968,370.00 USD | 117,700.00 USD | 0.00 USD | `+3.85%` | `158,091,000,000.00` |
| `Live` | `Short` | `745.50` | 1,040,000.00 USD | 67,820.00 USD | 0.00 USD | `+3.99%` | `90,974,000,000.00` |
| `Live` | `Short` | `746.50` | 1,220,000.00 USD | 182,880.00 USD | 0.00 USD | `+4.13%` | `244,988,000,000.00` |
| `Live` | `Short` | `748.50` | 1,260,000.00 USD | 44,170.00 USD | 0.00 USD | `+4.41%` | `59,012,000,000.00` |
| `Live` | `Short` | `749.50` | 1,270,000.00 USD | 3,230.00 USD | 0.00 USD | `+4.55%` | `4,312,000,000.00` |
| `Live` | `Short` | `750.50` | 1,280,000.00 USD | 9,570.00 USD | 0.00 USD | `+4.69%` | `12,745,000,000.00` |
| `Live` | `Short` | `751.50` | 1,870,000.00 USD | 593,520.00 USD | 0.00 USD | `+4.83%` | `789,786,000,000.00` |
| `Live` | `Short` | `752.50` | 1,930,000.00 USD | 57,710.00 USD | 0.00 USD | `+4.97%` | `76,692,000,000.00` |
| `Live` | `Short` | `754.50` | 2,790,000.00 USD | 863,250.00 USD | 0.00 USD | `+5.25%` | `1,144,139,000,000.00` |
| `Live` | `Short` | `755.50` | 2,790,000.00 USD | 336.20 USD | 0.00 USD | `+5.39%` | `445,000,000.00` |
| `Live` | `Short` | `756.50` | 2,790,000.00 USD | 3,750.00 USD | 0.00 USD | `+5.53%` | `4,960,000,000.00` |
| `Live` | `Short` | `757.50` | 2,800,000.00 USD | 3,050.00 USD | 0.00 USD | `+5.67%` | `4,020,000,000.00` |
| `Live` | `Short` | `758.50` | 2,980,000.00 USD | 180,270.00 USD | 0.00 USD | `+5.81%` | `237,673,000,000.00` |
| `Live` | `Short` | `759.50` | 2,980,000.00 USD | 3,830.00 USD | 0.00 USD | `+5.95%` | `5,039,000,000.00` |
| `Live` | `Short` | `760.50` | 2,980,000.00 USD | 540.72 USD | 0.00 USD | `+6.08%` | `711,000,000.00` |
| `Live` | `Short` | `762.50` | 2,980,000.00 USD | 367.52 USD | 0.00 USD | `+6.36%` | `482,000,000.00` |
| `Live` | `Short` | `763.50` | 3,430,000.00 USD | 445,300.00 USD | 0.00 USD | `+6.50%` | `583,234,000,000.00` |
| `Live` | `Short` | `764.50` | 3,500,000.00 USD | 76,450.00 USD | 0.00 USD | `+6.64%` | `100,000,000,000.00` |
| `Live` | `Short` | `766.50` | 3,510,000.00 USD | 2,850.00 USD | 0.00 USD | `+6.92%` | `3,719,000,000.00` |
| `Live` | `Short` | `768.50` | 3,510,000.00 USD | 156.77 USD | 0.00 USD | `+7.20%` | `204,000,000.00` |
| `Live` | `Short` | `770.50` | 3,510,000.00 USD | 881.45 USD | 0.00 USD | `+7.48%` | `1,144,000,000.00` |
| `Live` | `Short` | `771.50` | 3,520,000.00 USD | 10,380.00 USD | 0.00 USD | `+7.62%` | `13,458,000,000.00` |
| `Live` | `Short` | `772.50` | 3,520,000.00 USD | 849.75 USD | 0.00 USD | `+7.76%` | `1,100,000,000.00` |
| `Live` | `Short` | `773.50` | 3,520,000.00 USD | 3,800.00 USD | 0.00 USD | `+7.90%` | `4,915,000,000.00` |
| `Live` | `Short` | `776.50` | 3,620,000.00 USD | 100,020.00 USD | 0.00 USD | `+8.32%` | `128,807,000,000.00` |
| `Live` | `Short` | `777.50` | 3,620,000.00 USD | 209.15 USD | 0.00 USD | `+8.46%` | `269,000,000.00` |
| `Live` | `Short` | `778.50` | 3,630,000.00 USD | 3,200.00 USD | 0.00 USD | `+8.60%` | `4,107,000,000.00` |
| `Live` | `Short` | `780.50` | 3,630,000.00 USD | 6,200.00 USD | 0.00 USD | `+8.87%` | `7,942,000,000.00` |
| `Live` | `Short` | `781.50` | 3,630,000.00 USD | 1,830.00 USD | 0.00 USD | `+9.01%` | `2,337,000,000.00` |
| `Live` | `Short` | `785.50` | 3,630,000.00 USD | 129.61 USD | 0.00 USD | `+9.57%` | `165,000,000.00` |
| `Live` | `Short` | `786.50` | 3,760,000.00 USD | 126,920.00 USD | 0.00 USD | `+9.71%` | `161,372,000,000.00` |
| `Live` | `Short` | `788.50` | 3,760,000.00 USD | 2,320.00 USD | 0.00 USD | `+9.99%` | `2,936,000,000.00` |
| `Live` | `Short` | `793.50` | 3,770,000.00 USD | 3,690.00 USD | 0.00 USD | `+10.69%` | `4,645,000,000.00` |
| `Live` | `Short` | `795.50` | 3,770,000.00 USD | 518.67 USD | 0.00 USD | `+10.97%` | `652,000,000.00` |
| `Live` | `Short` | `796.50` | 3,770,000.00 USD | 567.11 USD | 0.00 USD | `+11.11%` | `712,000,000.00` |
| `Live` | `Short` | `797.50` | 3,770,000.00 USD | 1,090.00 USD | 0.00 USD | `+11.25%` | `1,367,000,000.00` |
| `Live` | `Short` | `799.50` | 3,770,000.00 USD | 610.02 USD | 0.00 USD | `+11.52%` | `763,000,000.00` |
| `Live` | `Short` | `800.50` | 3,800,000.00 USD | 28,250.00 USD | 0.00 USD | `+11.66%` | `35,287,000,000.00` |
| `Live` | `Short` | `801.50` | 3,800,000.00 USD | 3,680.00 USD | 0.00 USD | `+11.80%` | `4,594,000,000.00` |
| `Live` | `Short` | `802.50` | 4,580,000.00 USD | 778,380.00 USD | 0.00 USD | `+11.94%` | `969,946,000,000.00` |
| `Live` | `Short` | `803.50` | 4,590,000.00 USD | 4,560.00 USD | 0.00 USD | `+12.08%` | `5,679,000,000.00` |
| `Live` | `Short` | `804.50` | 4,590,000.00 USD | 105.39 USD | 0.00 USD | `+12.22%` | `131,000,000.00` |
| `Live` | `Short` | `805.50` | 4,600,000.00 USD | 15,370.00 USD | 0.00 USD | `+12.36%` | `19,085,000,000.00` |
| `Live` | `Short` | `806.50` | 4,600,000.00 USD | 2,890.00 USD | 0.00 USD | `+12.50%` | `3,580,000,000.00` |
| `Live` | `Short` | `807.50` | 4,600,000.00 USD | 738.06 USD | 0.00 USD | `+12.64%` | `914,000,000.00` |
| `Live` | `Short` | `808.50` | 4,620,000.00 USD | 11,780.00 USD | 0.00 USD | `+12.78%` | `14,574,000,000.00` |
| `Live` | `Short` | `809.50` | 4,620,000.00 USD | 173.23 USD | 0.00 USD | `+12.92%` | `214,000,000.00` |
| `Live` | `Short` | `811.50` | 5,140,000.00 USD | 519,680.00 USD | 0.00 USD | `+13.20%` | `640,389,000,000.00` |
| `Live` | `Short` | `812.50` | 5,140,000.00 USD | 853.94 USD | 0.00 USD | `+13.34%` | `1,051,000,000.00` |
| `Live` | `Short` | `814.50` | 5,140,000.00 USD | 1,960.00 USD | 0.00 USD | `+13.62%` | `2,401,000,000.00` |
| `Live` | `Short` | `815.50` | 5,150,000.00 USD | 6,020.00 USD | 0.00 USD | `+13.76%` | `7,383,000,000.00` |
| `Live` | `Short` | `816.50` | 5,160,000.00 USD | 15,410.00 USD | 0.00 USD | `+13.90%` | `18,879,000,000.00` |
| `Live` | `Short` | `817.50` | 5,160,000.00 USD | 325.37 USD | 0.00 USD | `+14.04%` | `398,000,000.00` |
| `Live` | `Short` | `818.50` | 5,160,000.00 USD | 572.13 USD | 0.00 USD | `+14.18%` | `699,000,000.00` |
| `Live` | `Short` | `821.50` | 5,170,000.00 USD | 11,710.00 USD | 0.00 USD | `+14.59%` | `14,252,000,000.00` |
| `Live` | `Short` | `822.50` | 5,180,000.00 USD | 3,540.00 USD | 0.00 USD | `+14.73%` | `4,302,000,000.00` |
| `Live` | `Short` | `826.50` | 5,190,000.00 USD | 11,640.00 USD | 0.00 USD | `+15.29%` | `14,084,000,000.00` |
| `Live` | `Short` | `828.50` | 5,270,000.00 USD | 84,000.00 USD | 0.00 USD | `+15.57%` | `101,384,000,000.00` |
| `Live` | `Short` | `833.50` | 5,350,000.00 USD | 79,150.00 USD | 0.00 USD | `+16.27%` | `94,960,000,000.00` |
| `Live` | `Short` | `834.50` | 5,350,000.00 USD | 1,010.00 USD | 0.00 USD | `+16.41%` | `1,206,000,000.00` |
| `Live` | `Short` | `837.50` | 5,360,000.00 USD | 11,450.00 USD | 0.00 USD | `+16.83%` | `13,676,000,000.00` |
| `Live` | `Short` | `838.50` | 5,390,000.00 USD | 21,840.00 USD | 0.00 USD | `+16.97%` | `26,046,000,000.00` |
| `Live` | `Short` | `841.50` | 5,390,000.00 USD | 2,830.00 USD | 0.00 USD | `+17.38%` | `3,364,000,000.00` |
| `Live` | `Short` | `842.50` | 5,390,000.00 USD | 2,900.00 USD | 0.00 USD | `+17.52%` | `3,445,000,000.00` |
| `Live` | `Short` | `843.50` | 5,390,000.00 USD | 227.75 USD | 0.00 USD | `+17.66%` | `270,000,000.00` |
| `Live` | `Short` | `848.50` | 5,430,000.00 USD | 34,550.00 USD | 0.00 USD | `+18.36%` | `40,719,000,000.00` |
| `Live` | `Short` | `850.50` | 5,440,000.00 USD | 10,930.00 USD | 0.00 USD | `+18.64%` | `12,851,000,000.00` |
| `Live` | `Short` | `851.50` | 5,440,000.00 USD | 285.25 USD | 0.00 USD | `+18.78%` | `335,000,000.00` |
| `Live` | `Short` | `854.50` | 5,440,000.00 USD | 5,030.00 USD | 0.00 USD | `+19.20%` | `5,884,000,000.00` |
| `Live` | `Short` | `858.50` | 5,970,000.00 USD | 523,680.00 USD | 0.00 USD | `+19.76%` | `610,000,000,000.00` |
| `Live` | `Short` | `859.50` | 5,980,000.00 USD | 16,380.00 USD | 0.00 USD | `+19.89%` | `19,059,000,000.00` |
| `Live` | `Short` | `865.50` | 6,000,000.00 USD | 18,900.00 USD | 0.00 USD | `+20.73%` | `21,832,000,000.00` |
| `Live` | `Short` | `870.50` | 6,010,000.00 USD | 6,090.00 USD | 0.00 USD | `+21.43%` | `7,000,000,000.00` |
| `Live` | `Short` | `871.50` | 6,300,000.00 USD | 292,000.00 USD | 0.00 USD | `+21.57%` | `335,051,000,000.00` |
| `Live` | `Short` | `877.50` | 6,910,000.00 USD | 614,250.00 USD | 0.00 USD | `+22.41%` | `700,000,000,000.00` |
| `Live` | `Short` | `878.50` | 7,010,000.00 USD | 93,100.00 USD | 0.00 USD | `+22.54%` | `105,974,000,000.00` |
| `Live` | `Short` | `880.50` | 7,020,000.00 USD | 14,740.00 USD | 0.00 USD | `+22.82%` | `16,745,000,000.00` |
| `Live` | `Short` | `883.50` | 7,040,000.00 USD | 22,840.00 USD | 0.00 USD | `+23.24%` | `25,848,000,000.00` |
| `Live` | `Short` | `885.50` | 7,050,000.00 USD | 1,770.00 USD | 0.00 USD | `+23.52%` | `2,000,000,000.00` |
| `Live` | `Short` | `886.50` | 7,050,000.00 USD | 812.92 USD | 0.00 USD | `+23.66%` | `917,000,000.00` |
| `Live` | `Short` | `887.50` | 7,050,000.00 USD | 385.18 USD | 0.00 USD | `+23.80%` | `434,000,000.00` |
| `Live` | `Short` | `890.50` | 7,140,000.00 USD | 89,050.00 USD | 0.00 USD | `+24.22%` | `100,000,000,000.00` |
| `Live` | `Short` | `891.50` | 7,180,000.00 USD | 40,420.00 USD | 0.00 USD | `+24.36%` | `45,338,000,000.00` |
| `Live` | `Short` | `893.50` | 7,180,000.00 USD | 173.34 USD | 0.00 USD | `+24.64%` | `194,000,000.00` |
| `Live` | `Short` | `894.50` | 7,200,000.00 USD | 26,840.00 USD | 0.00 USD | `+24.78%` | `30,000,000,000.00` |
| `Live` | `Short` | `895.50` | 7,460,000.00 USD | 258,570.00 USD | 0.00 USD | `+24.92%` | `288,749,000,000.00` |
| `Live` | `Short` | `896.50` | 7,690,000.00 USD | 224,120.00 USD | 0.00 USD | `+25.06%` | `250,000,000,000.00` |
| `Live` | `Short` | `898.50` | 7,690,000.00 USD | 127.59 USD | 0.00 USD | `+25.33%` | `142,000,000.00` |
| `Live` | `Short` | `902.50` | 7,690,000.00 USD | 305.05 USD | 0.00 USD | `+25.89%` | `338,000,000.00` |
| `Live` | `Short` | `904.50` | 7,750,000.00 USD | 63,930.00 USD | 0.00 USD | `+26.17%` | `70,678,000,000.00` |
| `Live` | `Short` | `906.50` | 7,750,000.00 USD | 2,130.00 USD | 0.00 USD | `+26.45%` | `2,346,000,000.00` |
| `Live` | `Short` | `908.50` | 7,750,000.00 USD | 901.23 USD | 0.00 USD | `+26.73%` | `992,000,000.00` |
| `Live` | `Short` | `909.50` | 7,750,000.00 USD | 890.40 USD | 0.00 USD | `+26.87%` | `979,000,000.00` |
| `Live` | `Short` | `910.50` | 7,760,000.00 USD | 3,010.00 USD | 0.00 USD | `+27.01%` | `3,310,000,000.00` |
| `Live` | `Short` | `911.50` | 7,820,000.00 USD | 63,160.00 USD | 0.00 USD | `+27.15%` | `69,287,000,000.00` |
| `Live` | `Short` | `912.50` | 7,830,000.00 USD | 7,520.00 USD | 0.00 USD | `+27.29%` | `8,244,000,000.00` |
| `Live` | `Short` | `913.50` | 7,830,000.00 USD | 116.93 USD | 0.00 USD | `+27.43%` | `128,000,000.00` |
| `Live` | `Short` | `914.50` | 7,830,000.00 USD | 3,920.00 USD | 0.00 USD | `+27.57%` | `4,284,000,000.00` |
| `Live` | `Short` | `916.50` | 7,840,000.00 USD | 3,060.00 USD | 0.00 USD | `+27.85%` | `3,344,000,000.00` |
| `Live` | `Short` | `917.50` | 7,850,000.00 USD | 13,990.00 USD | 0.00 USD | `+27.99%` | `15,247,000,000.00` |
| `Live` | `Short` | `918.50` | 8,010,000.00 USD | 163,540.00 USD | 0.00 USD | `+28.12%` | `178,055,000,000.00` |
| `Live` | `Short` | `921.50` | 8,030,000.00 USD | 12,910.00 USD | 0.00 USD | `+28.54%` | `14,008,000,000.00` |
| `Live` | `Short` | `925.50` | 8,040,000.00 USD | 9,260.00 USD | 0.00 USD | `+29.10%` | `10,000,000,000.00` |
| `Live` | `Short` | `928.50` | 8,490,000.00 USD | 449,690.00 USD | 0.00 USD | `+29.52%` | `484,314,000,000.00` |
| `Live` | `Short` | `932.50` | 8,490,000.00 USD | 1,610.00 USD | 0.00 USD | `+30.08%` | `1,724,000,000.00` |
| `Live` | `Short` | `935.50` | 8,550,000.00 USD | 65,480.00 USD | 0.00 USD | `+30.50%` | `70,000,000,000.00` |
| `Live` | `Short` | `939.50` | 8,550,000.00 USD | 2,670.00 USD | 0.00 USD | `+31.05%` | `2,846,000,000.00` |
| `Live` | `Short` | `940.50` | 8,610,000.00 USD | 57,750.00 USD | 0.00 USD | `+31.19%` | `61,406,000,000.00` |
| `Live` | `Short` | `942.50` | 8,610,000.00 USD | 112.16 USD | 0.00 USD | `+31.47%` | `119,000,000.00` |
| `Live` | `Short` | `951.50` | 8,610,000.00 USD | 600.40 USD | 0.00 USD | `+32.73%` | `631,000,000.00` |
| `Live` | `Short` | `955.50` | 8,630,000.00 USD | 18,910.00 USD | 0.00 USD | `+33.29%` | `19,788,000,000.00` |
| `Live` | `Short` | `956.50` | 8,630,000.00 USD | 409.38 USD | 0.00 USD | `+33.43%` | `428,000,000.00` |
| `Live` | `Short` | `961.50` | 8,630,000.00 USD | 224.03 USD | 0.00 USD | `+34.12%` | `233,000,000.00` |
| `Live` | `Short` | `967.50` | 8,640,000.00 USD | 7,250.00 USD | 0.00 USD | `+34.96%` | `7,498,000,000.00` |
| `Live` | `Short` | `969.50` | 8,650,000.00 USD | 5,780.00 USD | 0.00 USD | `+35.24%` | `5,960,000,000.00` |
| `Live` | `Short` | `970.50` | 8,650,000.00 USD | 1,940.00 USD | 0.00 USD | `+35.38%` | `2,000,000,000.00` |
| `Live` | `Short` | `971.50` | 8,650,000.00 USD | 119.49 USD | 0.00 USD | `+35.52%` | `123,000,000.00` |
| `Live` | `Short` | `975.50` | 9,480,000.00 USD | 829,170.00 USD | 0.00 USD | `+36.08%` | `850,000,000,000.00` |
| `Live` | `Short` | `981.50` | 9,490,000.00 USD | 14,480.00 USD | 0.00 USD | `+36.91%` | `14,758,000,000.00` |
| `Live` | `Short` | `986.50` | 9,490,000.00 USD | 1,100.00 USD | 0.00 USD | `+37.61%` | `1,112,000,000.00` |
| `Live` | `Short` | `989.50` | 9,490,000.00 USD | 1,470.00 USD | 0.00 USD | `+38.03%` | `1,482,000,000.00` |
| `Live` | `Short` | `990.50` | 9,520,000.00 USD | 28,300.00 USD | 0.00 USD | `+38.17%` | `28,570,000,000.00` |
| `Live` | `Short` | `992.50` | 9,520,000.00 USD | 2,140.00 USD | 0.00 USD | `+38.45%` | `2,154,000,000.00` |
| `Live` | `Short` | `993.50` | 9,540,000.00 USD | 15,420.00 USD | 0.00 USD | `+38.59%` | `15,523,000,000.00` |
| `Live` | `Short` | `994.50` | 9,830,000.00 USD | 285,520.00 USD | 0.00 USD | `+38.73%` | `287,098,000,000.00` |
| `Live` | `Short` | `995.50` | 9,930,000.00 USD | 108,080.00 USD | 0.00 USD | `+38.87%` | `108,568,000,000.00` |
| `Live` | `Short` | `996.50` | 9,930,000.00 USD | 989.52 USD | 0.00 USD | `+39.01%` | `993,000,000.00` |
| `Live` | `Short` | `997.50` | 9,940,000.00 USD | 7,300.00 USD | 0.00 USD | `+39.14%` | `7,316,000,000.00` |
| `Live` | `Short` | `998.50` | 9,950,000.00 USD | 9,550.00 USD | 0.00 USD | `+39.28%` | `9,569,000,000.00` |
| `Live` | `Short` | `999.50` | 9,990,000.00 USD | 36,850.00 USD | 0.00 USD | `+39.42%` | `36,870,000,000.00` |
| `Live` | `Short` | `1003.50` | 9,990,000.00 USD | 838.93 USD | 0.00 USD | `+39.98%` | `836,000,000.00` |
| `Live` | `Short` | `1005.50` | 9,990,000.00 USD | 4,050.00 USD | 0.00 USD | `+40.26%` | `4,024,000,000.00` |
| `Live` | `Short` | `1008.50` | 10,020,000.00 USD | 28,800.00 USD | 0.00 USD | `+40.68%` | `28,558,000,000.00` |
| `Live` | `Short` | `1009.50` | 10,070,000.00 USD | 51,680.00 USD | 0.00 USD | `+40.82%` | `51,191,000,000.00` |
| `Live` | `Short` | `1015.50` | 10,070,000.00 USD | 630.63 USD | 0.00 USD | `+41.66%` | `621,000,000.00` |
| `Live` | `Short` | `1019.50` | 10,370,000.00 USD | 297,250.00 USD | 0.00 USD | `+42.21%` | `291,563,000,000.00` |
| `Live` | `Short` | `1024.50` | 10,370,000.00 USD | 3,340.00 USD | 0.00 USD | `+42.91%` | `3,259,000,000.00` |
| `Live` | `Short` | `1037.50` | 11,100,000.00 USD | 723,770.00 USD | 0.00 USD | `+44.72%` | `697,611,000,000.00` |
| `Live` | `Short` | `1039.50` | 11,130,000.00 USD | 31,180.00 USD | 0.00 USD | `+45.00%` | `30,000,000,000.00` |
| `Live` | `Short` | `1050.50` | 11,130,000.00 USD | 500.04 USD | 0.00 USD | `+46.54%` | `476,000,000.00` |
| `Live` | `Short` | `1051.50` | 11,200,000.00 USD | 65,720.00 USD | 0.00 USD | `+46.68%` | `62,500,000,000.00` |
| `Live` | `Short` | `1062.50` | 11,210,000.00 USD | 15,300.00 USD | 0.00 USD | `+48.21%` | `14,403,000,000.00` |
| `Live` | `Short` | `1064.50` | 11,210,000.00 USD | 1,600.00 USD | 0.00 USD | `+48.49%` | `1,500,000,000.00` |
| `Live` | `Short` | `1073.50` | 11,210,000.00 USD | 1,610.00 USD | 0.00 USD | `+49.75%` | `1,500,000,000.00` |
| `Live` | `Short` | `1079.50` | 11,210,000.00 USD | 120.90 USD | 0.00 USD | `+50.58%` | `112,000,000.00` |
| `Live` | `Short` | `1087.50` | 11,290,000.00 USD | 75,280.00 USD | 0.00 USD | `+51.70%` | `69,226,000,000.00` |
| `Live` | `Short` | `1088.50` | 11,310,000.00 USD | 15,780.00 USD | 0.00 USD | `+51.84%` | `14,495,000,000.00` |
| `Live` | `Short` | `1093.50` | 11,430,000.00 USD | 120,790.00 USD | 0.00 USD | `+52.54%` | `110,460,000,000.00` |
| `Live` | `Short` | `1095.50` | 11,430,000.00 USD | 809.57 USD | 0.00 USD | `+52.81%` | `739,000,000.00` |
| `Live` | `Short` | `1097.50` | 11,500,000.00 USD | 74,900.00 USD | 0.00 USD | `+53.09%` | `68,249,000,000.00` |
| `Live` | `Short` | `1098.50` | 11,520,000.00 USD | 19,580.00 USD | 0.00 USD | `+53.23%` | `17,826,000,000.00` |
| `Live` | `Short` | `1118.50` | 11,520,000.00 USD | 149.88 USD | 0.00 USD | `+56.02%` | `134,000,000.00` |
| `Live` | `Short` | `1119.50` | 11,580,000.00 USD | 60,530.00 USD | 0.00 USD | `+56.16%` | `54,065,000,000.00` |
| `Live` | `Short` | `1120.50` | 11,700,000.00 USD | 116,530.00 USD | 0.00 USD | `+56.30%` | `104,000,000,000.00` |
| `Live` | `Short` | `1133.50` | 11,700,000.00 USD | 1,520.00 USD | 0.00 USD | `+58.12%` | `1,337,000,000.00` |
| `Live` | `Short` | `1137.50` | 12,040,000.00 USD | 341,610.00 USD | 0.00 USD | `+58.67%` | `300,314,000,000.00` |
| `Live` | `Short` | `1145.50` | 12,040,000.00 USD | 119.13 USD | 0.00 USD | `+59.79%` | `104,000,000.00` |
| `Live` | `Short` | `1148.50` | 12,040,000.00 USD | 153.90 USD | 0.00 USD | `+60.21%` | `134,000,000.00` |
| `Live` | `Short` | `1152.50` | 12,050,000.00 USD | 11,700.00 USD | 0.00 USD | `+60.77%` | `10,154,000,000.00` |
| `Live` | `Short` | `1178.50` | 12,120,000.00 USD | 66,060.00 USD | 0.00 USD | `+64.39%` | `56,055,000,000.00` |
| `Live` | `Short` | `1188.50` | 12,180,000.00 USD | 57,420.00 USD | 0.00 USD | `+65.79%` | `48,311,000,000.00` |
| `Live` | `Short` | `1192.50` | 12,280,000.00 USD | 107,330.00 USD | 0.00 USD | `+66.35%` | `90,000,000,000.00` |
| `Live` | `Short` | `1194.50` | 12,290,000.00 USD | 168.42 USD | 0.00 USD | `+66.62%` | `141,000,000.00` |
| `Live` | `Short` | `1197.50` | 12,290,000.00 USD | 463.43 USD | 0.00 USD | `+67.04%` | `387,000,000.00` |
| `Live` | `Short` | `1204.50` | 12,400,000.00 USD | 118,960.00 USD | 0.00 USD | `+68.02%` | `98,764,000,000.00` |
| `Live` | `Short` | `1207.50` | 12,400,000.00 USD | 385.19 USD | 0.00 USD | `+68.44%` | `319,000,000.00` |
| `Live` | `Short` | `1212.50` | 12,450,000.00 USD | 42,440.00 USD | 0.00 USD | `+69.14%` | `35,000,000,000.00` |
| `Live` | `Short` | `1214.50` | 12,480,000.00 USD | 30,340.00 USD | 0.00 USD | `+69.41%` | `24,982,000,000.00` |
| `Live` | `Short` | `1218.50` | 12,480,000.00 USD | 704.29 USD | 0.00 USD | `+69.97%` | `578,000,000.00` |
| `Live` | `Short` | `1222.50` | 12,500,000.00 USD | 21,230.00 USD | 0.00 USD | `+70.53%` | `17,363,000,000.00` |
| `Live` | `Short` | `1224.50` | 12,500,000.00 USD | 1,030.00 USD | 0.00 USD | `+70.81%` | `841,000,000.00` |
| `Live` | `Short` | `1225.50` | 12,500,000.00 USD | 3,720.00 USD | 0.00 USD | `+70.95%` | `3,035,000,000.00` |
| `Live` | `Short` | `1239.50` | 12,500,000.00 USD | 198.32 USD | 0.00 USD | `+72.90%` | `160,000,000.00` |
| `Live` | `Short` | `1241.50` | 12,530,000.00 USD | 26,600.00 USD | 0.00 USD | `+73.18%` | `21,429,000,000.00` |
| `Live` | `Short` | `1248.50` | 12,530,000.00 USD | 1,250.00 USD | 0.00 USD | `+74.16%` | `1,000,000,000.00` |
| `Live` | `Short` | `1249.50` | 12,530,000.00 USD | 2,050.00 USD | 0.00 USD | `+74.30%` | `1,644,000,000.00` |
| `Live` | `Short` | `1251.50` | 12,530,000.00 USD | 100.12 USD | 0.00 USD | `+74.58%` | `80,000,000.00` |
| `Live` | `Short` | `1252.50` | 12,540,000.00 USD | 5,000.00 USD | 0.00 USD | `+74.72%` | `3,994,000,000.00` |
| `Live` | `Short` | `1253.50` | 12,560,000.00 USD | 24,340.00 USD | 0.00 USD | `+74.85%` | `19,414,000,000.00` |
| `Live` | `Short` | `1263.50` | 12,680,000.00 USD | 113,720.00 USD | 0.00 USD | `+76.25%` | `90,000,000,000.00` |
| `Live` | `Short` | `1265.50` | 12,680,000.00 USD | 2,700.00 USD | 0.00 USD | `+76.53%` | `2,134,000,000.00` |
| `Live` | `Short` | `1269.50` | 12,690,000.00 USD | 6,880.00 USD | 0.00 USD | `+77.09%` | `5,419,000,000.00` |
| `Live` | `Short` | `1278.50` | 12,730,000.00 USD | 38,620.00 USD | 0.00 USD | `+78.34%` | `30,209,000,000.00` |
| `Live` | `Short` | `1281.50` | 12,790,000.00 USD | 61,670.00 USD | 0.00 USD | `+78.76%` | `48,123,000,000.00` |
| `Live` | `Short` | `1283.50` | 12,860,000.00 USD | 77,010.00 USD | 0.00 USD | `+79.04%` | `60,002,000,000.00` |
| `Live` | `Short` | `1290.50` | 14,690,000.00 USD | 1,820,000.00 USD | 0.00 USD | `+80.02%` | `1,412,868,000,000.00` |
| `Live` | `Short` | `1293.50` | 14,800,000.00 USD | 110,340.00 USD | 0.00 USD | `+80.43%` | `85,305,000,000.00` |
| `Live` | `Short` | `1294.50` | 14,800,000.00 USD | 4,000.00 USD | 0.00 USD | `+80.57%` | `3,092,000,000.00` |
| `Live` | `Short` | `1295.50` | 14,800,000.00 USD | 181.37 USD | 0.00 USD | `+80.71%` | `140,000,000.00` |
| `Live` | `Short` | `1296.50` | 14,820,000.00 USD | 19,370.00 USD | 0.00 USD | `+80.85%` | `14,939,000,000.00` |
| `Live` | `Short` | `1300.50` | 14,950,000.00 USD | 130,050.00 USD | 0.00 USD | `+81.41%` | `100,000,000,000.00` |
| `Live` | `Short` | `1309.50` | 15,120,000.00 USD | 166,150.00 USD | 0.00 USD | `+82.67%` | `126,881,000,000.00` |
| `Live` | `Short` | `1313.50` | 15,120,000.00 USD | 227.24 USD | 0.00 USD | `+83.22%` | `173,000,000.00` |
| `Live` | `Short` | `1316.50` | 15,130,000.00 USD | 7,580.00 USD | 0.00 USD | `+83.64%` | `5,758,000,000.00` |
| `Live` | `Short` | `1319.50` | 15,140,000.00 USD | 14,130.00 USD | 0.00 USD | `+84.06%` | `10,710,000,000.00` |
| `Live` | `Short` | `1322.50` | 15,170,000.00 USD | 32,870.00 USD | 0.00 USD | `+84.48%` | `24,853,000,000.00` |
| `Live` | `Short` | `1327.50` | 15,170,000.00 USD | 138.06 USD | 0.00 USD | `+85.18%` | `104,000,000.00` |
| `Live` | `Short` | `1328.50` | 15,170,000.00 USD | 289.61 USD | 0.00 USD | `+85.32%` | `218,000,000.00` |
| `Live` | `Short` | `1330.50` | 15,200,000.00 USD | 23,470.00 USD | 0.00 USD | `+85.60%` | `17,640,000,000.00` |
| `Live` | `Short` | `1333.50` | 15,220,000.00 USD | 18,760.00 USD | 0.00 USD | `+86.01%` | `14,070,000,000.00` |
| `Live` | `Short` | `1339.50` | 15,250,000.00 USD | 30,810.00 USD | 0.00 USD | `+86.85%` | `23,000,000,000.00` |
| `Live` | `Short` | `1352.50` | 15,250,000.00 USD | 347.59 USD | 0.00 USD | `+88.66%` | `257,000,000.00` |
| `Live` | `Short` | `1365.50` | 15,250,000.00 USD | 4,100.00 USD | 0.00 USD | `+90.48%` | `3,000,000,000.00` |
| `Live` | `Short` | `1366.50` | 15,250,000.00 USD | 194.04 USD | 0.00 USD | `+90.62%` | `142,000,000.00` |
| `Live` | `Short` | `1367.50` | 15,250,000.00 USD | 761.70 USD | 0.00 USD | `+90.76%` | `557,000,000.00` |
| `Live` | `Short` | `1369.50` | 15,300,000.00 USD | 51,620.00 USD | 0.00 USD | `+91.04%` | `37,689,000,000.00` |
| `Live` | `Short` | `1371.50` | 15,390,000.00 USD | 89,150.00 USD | 0.00 USD | `+91.32%` | `65,000,000,000.00` |
| `Live` | `Short` | `1379.50` | 15,400,000.00 USD | 2,760.00 USD | 0.00 USD | `+92.43%` | `2,000,000,000.00` |
| `Live` | `Short` | `1383.50` | 15,400,000.00 USD | 2,460.00 USD | 0.00 USD | `+92.99%` | `1,776,000,000.00` |
| `Live` | `Short` | `1392.50` | 16,820,000.00 USD | 1,420,000.00 USD | 0.00 USD | `+94.24%` | `1,019,445,000,000.00` |
| `Live` | `Short` | `1401.50` | 16,820,000.00 USD | 177.99 USD | 0.00 USD | `+95.50%` | `127,000,000.00` |
| `Live` | `Short` | `1403.50` | 17,070,000.00 USD | 252,630.00 USD | 0.00 USD | `+95.78%` | `180,000,000,000.00` |
| `Live` | `Short` | `1405.50` | 17,070,000.00 USD | 4,770.00 USD | 0.00 USD | `+96.06%` | `3,392,000,000.00` |
| `Live` | `Short` | `1431.50` | 17,080,000.00 USD | 360.74 USD | 0.00 USD | `+99.68%` | `252,000,000.00` |

- **Near-Money Retail Stop-Loss Cascade Map Table (15_Hyperdash_Stops_Map.parquet)**:
| Stop Type | Price Level (USD) | Cumulative Stops (USD) | Buy Stops (USD) | Sell Stops (USD) | Distance (%) | Cascade Risk Tier |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `Sell Stop` | `150.50` | 4,720,000.00 USD | 0.00 USD | 475.73 USD | `-79.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `300.50` | 4,720,000.00 USD | 0.00 USD | 2,400.00 USD | `-58.08%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `333.50` | 4,710,000.00 USD | 0.00 USD | 333.50 USD | `-53.48%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `360.50` | 4,710,000.00 USD | 0.00 USD | 8,140.00 USD | `-49.71%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `369.50` | 4,710,000.00 USD | 0.00 USD | 5,170.00 USD | `-48.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `400.50` | 4,700,000.00 USD | 0.00 USD | 17,290.00 USD | `-44.13%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `410.50` | 4,680,000.00 USD | 0.00 USD | 25,210.00 USD | `-42.74%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `412.50` | 4,660,000.00 USD | 0.00 USD | 4,550.00 USD | `-42.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `424.50` | 4,650,000.00 USD | 0.00 USD | 8,180.00 USD | `-40.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `433.50` | 4,650,000.00 USD | 0.00 USD | 173.83 USD | `-39.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `445.50` | 4,650,000.00 USD | 0.00 USD | 2,210.00 USD | `-37.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `455.50` | 4,640,000.00 USD | 0.00 USD | 698.74 USD | `-36.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `456.50` | 4,640,000.00 USD | 0.00 USD | 2,270.00 USD | `-36.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `458.50` | 4,640,000.00 USD | 0.00 USD | 1,750.00 USD | `-36.04%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `469.50` | 4,640,000.00 USD | 0.00 USD | 3,550.00 USD | `-34.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `486.50` | 4,630,000.00 USD | 0.00 USD | 100.71 USD | `-32.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `487.50` | 4,630,000.00 USD | 0.00 USD | 6,600.00 USD | `-32.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `488.50` | 4,630,000.00 USD | 0.00 USD | 125.06 USD | `-31.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `492.50` | 4,630,000.00 USD | 0.00 USD | 2,450.00 USD | `-31.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `498.50` | 4,630,000.00 USD | 0.00 USD | 163.01 USD | `-30.46%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `499.50` | 4,630,000.00 USD | 0.00 USD | 214.78 USD | `-30.32%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `500.50` | 4,630,000.00 USD | 0.00 USD | 12,610.00 USD | `-30.18%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `503.50` | 4,610,000.00 USD | 0.00 USD | 42,600.00 USD | `-29.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `506.50` | 4,570,000.00 USD | 0.00 USD | 138.78 USD | `-29.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `509.50` | 4,570,000.00 USD | 0.00 USD | 185.97 USD | `-28.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `515.50` | 4,570,000.00 USD | 0.00 USD | 1,030.00 USD | `-28.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `516.50` | 4,570,000.00 USD | 0.00 USD | 125.51 USD | `-27.95%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `517.50` | 4,570,000.00 USD | 0.00 USD | 280.49 USD | `-27.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `521.50` | 4,570,000.00 USD | 0.00 USD | 258.14 USD | `-27.25%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `524.50` | 4,570,000.00 USD | 0.00 USD | 8,170.00 USD | `-26.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `528.50` | 4,560,000.00 USD | 0.00 USD | 485.16 USD | `-26.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `534.50` | 4,560,000.00 USD | 0.00 USD | 4,650.00 USD | `-25.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `538.50` | 4,550,000.00 USD | 0.00 USD | 1,680.00 USD | `-24.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `540.50` | 4,550,000.00 USD | 0.00 USD | 864.80 USD | `-24.60%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `550.50` | 4,550,000.00 USD | 0.00 USD | 4,130.00 USD | `-23.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `552.50` | 4,550,000.00 USD | 0.00 USD | 366,230.00 USD | `-22.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `554.50` | 4,180,000.00 USD | 0.00 USD | 1,190.00 USD | `-22.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `555.50` | 4,180,000.00 USD | 0.00 USD | 611.05 USD | `-22.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `557.50` | 4,180,000.00 USD | 0.00 USD | 213.52 USD | `-22.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `558.50` | 4,180,000.00 USD | 0.00 USD | 51,260.00 USD | `-22.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `560.50` | 4,130,000.00 USD | 0.00 USD | 292.02 USD | `-21.81%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `561.50` | 4,130,000.00 USD | 0.00 USD | 748.48 USD | `-21.67%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `562.50` | 4,130,000.00 USD | 0.00 USD | 199.12 USD | `-21.53%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `563.50` | 4,130,000.00 USD | 0.00 USD | 808.06 USD | `-21.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `566.50` | 4,130,000.00 USD | 0.00 USD | 566.50 USD | `-20.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `567.50` | 4,130,000.00 USD | 0.00 USD | 330.85 USD | `-20.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `568.50` | 4,130,000.00 USD | 0.00 USD | 5,680.00 USD | `-20.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `569.50` | 4,120,000.00 USD | 0.00 USD | 569.50 USD | `-20.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `570.50` | 4,120,000.00 USD | 0.00 USD | 774.17 USD | `-20.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `571.50` | 4,120,000.00 USD | 0.00 USD | 1,700.00 USD | `-20.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `573.50` | 4,120,000.00 USD | 0.00 USD | 291.91 USD | `-20.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `575.50` | 4,120,000.00 USD | 0.00 USD | 469.61 USD | `-19.72%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `576.50` | 4,120,000.00 USD | 0.00 USD | 289.98 USD | `-19.58%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `577.50` | 4,120,000.00 USD | 0.00 USD | 285.86 USD | `-19.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `579.50` | 4,120,000.00 USD | 0.00 USD | 289.17 USD | `-19.16%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `580.50` | 4,120,000.00 USD | 0.00 USD | 6,750.00 USD | `-19.02%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `581.50` | 4,110,000.00 USD | 0.00 USD | 1,240.00 USD | `-18.88%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `582.50` | 4,110,000.00 USD | 0.00 USD | 6,980.00 USD | `-18.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `583.50` | 4,100,000.00 USD | 0.00 USD | 287.67 USD | `-18.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `584.50` | 4,100,000.00 USD | 0.00 USD | 763.94 USD | `-18.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `585.50` | 4,100,000.00 USD | 0.00 USD | 542.76 USD | `-18.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `586.50` | 4,100,000.00 USD | 0.00 USD | 34,020.00 USD | `-18.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `587.50` | 4,060,000.00 USD | 0.00 USD | 830,190.00 USD | `-18.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `588.50` | 3,230,000.00 USD | 0.00 USD | 287.78 USD | `-17.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `589.50` | 3,230,000.00 USD | 0.00 USD | 252.31 USD | `-17.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `590.50` | 3,230,000.00 USD | 0.00 USD | 540.31 USD | `-17.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `592.50` | 3,230,000.00 USD | 0.00 USD | 698.56 USD | `-17.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `593.50` | 3,230,000.00 USD | 0.00 USD | 1,160.00 USD | `-17.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `596.50` | 3,230,000.00 USD | 0.00 USD | 119.30 USD | `-16.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `597.50` | 3,230,000.00 USD | 0.00 USD | 222.87 USD | `-16.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `598.50` | 3,230,000.00 USD | 0.00 USD | 244.79 USD | `-16.51%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `600.50` | 3,230,000.00 USD | 0.00 USD | 43,310.00 USD | `-16.23%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `601.50` | 3,190,000.00 USD | 0.00 USD | 1,590.00 USD | `-16.09%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `602.50` | 3,190,000.00 USD | 0.00 USD | 46,760.00 USD | `-15.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `603.50` | 3,140,000.00 USD | 0.00 USD | 123,870.00 USD | `-15.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `604.50` | 3,020,000.00 USD | 0.00 USD | 1,870.00 USD | `-15.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `605.50` | 3,010,000.00 USD | 0.00 USD | 2,610.00 USD | `-15.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `608.50` | 3,010,000.00 USD | 0.00 USD | 18,380.00 USD | `-15.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `609.50` | 2,990,000.00 USD | 0.00 USD | 30,480.00 USD | `-14.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `610.50` | 2,960,000.00 USD | 0.00 USD | 11,650.00 USD | `-14.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `611.50` | 2,950,000.00 USD | 0.00 USD | 4,470.00 USD | `-14.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `612.50` | 2,950,000.00 USD | 0.00 USD | 1,380.00 USD | `-14.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `614.50` | 2,940,000.00 USD | 0.00 USD | 269.15 USD | `-14.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `615.50` | 2,940,000.00 USD | 0.00 USD | 1,740.00 USD | `-14.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `616.50` | 2,940,000.00 USD | 0.00 USD | 120.83 USD | `-14.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `620.50` | 2,940,000.00 USD | 0.00 USD | 13,170.00 USD | `-13.44%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `621.50` | 2,930,000.00 USD | 0.00 USD | 2,150.00 USD | `-13.30%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `623.50` | 2,930,000.00 USD | 0.00 USD | 219.47 USD | `-13.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `624.50` | 2,930,000.00 USD | 0.00 USD | 445.27 USD | `-12.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `625.50` | 2,930,000.00 USD | 0.00 USD | 445.98 USD | `-12.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `626.50` | 2,930,000.00 USD | 0.00 USD | 694.79 USD | `-12.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `627.50` | 2,930,000.00 USD | 0.00 USD | 916.15 USD | `-12.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `628.50` | 2,920,000.00 USD | 0.00 USD | 746.03 USD | `-12.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `629.50` | 2,920,000.00 USD | 0.00 USD | 2,740.00 USD | `-12.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `630.50` | 2,920,000.00 USD | 0.00 USD | 861.26 USD | `-12.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `631.50` | 2,920,000.00 USD | 0.00 USD | 179.98 USD | `-11.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `632.50` | 2,920,000.00 USD | 0.00 USD | 1,100.00 USD | `-11.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `633.50` | 2,920,000.00 USD | 0.00 USD | 164.08 USD | `-11.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `634.50` | 2,920,000.00 USD | 0.00 USD | 2,550.00 USD | `-11.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `636.50` | 2,920,000.00 USD | 0.00 USD | 6,760.00 USD | `-11.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `637.50` | 2,910,000.00 USD | 0.00 USD | 2,730.00 USD | `-11.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `638.50` | 2,910,000.00 USD | 0.00 USD | 3,640.00 USD | `-10.93%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `639.50` | 2,900,000.00 USD | 0.00 USD | 384.98 USD | `-10.79%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `640.50` | 2,900,000.00 USD | 0.00 USD | 429.78 USD | `-10.65%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `641.50` | 2,900,000.00 USD | 0.00 USD | 352.18 USD | `-10.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `642.50` | 2,900,000.00 USD | 0.00 USD | 357.87 USD | `-10.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `643.50` | 2,900,000.00 USD | 0.00 USD | 1,830.00 USD | `-10.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `644.50` | 2,900,000.00 USD | 0.00 USD | 3,790.00 USD | `-10.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `645.50` | 2,900,000.00 USD | 0.00 USD | 10,640.00 USD | `-9.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `646.50` | 2,890,000.00 USD | 0.00 USD | 971.04 USD | `-9.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `648.50` | 2,880,000.00 USD | 0.00 USD | 1,800.00 USD | `-9.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `649.50` | 2,880,000.00 USD | 0.00 USD | 107.17 USD | `-9.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `650.50` | 2,880,000.00 USD | 0.00 USD | 30,840.00 USD | `-9.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `651.50` | 2,850,000.00 USD | 0.00 USD | 201.31 USD | `-9.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `653.50` | 2,850,000.00 USD | 0.00 USD | 2,020.00 USD | `-8.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `654.50` | 2,850,000.00 USD | 0.00 USD | 308.92 USD | `-8.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `655.50` | 2,850,000.00 USD | 0.00 USD | 165.84 USD | `-8.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `656.50` | 2,850,000.00 USD | 0.00 USD | 2,330.00 USD | `-8.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `657.50` | 2,850,000.00 USD | 0.00 USD | 110.46 USD | `-8.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `658.50` | 2,850,000.00 USD | 0.00 USD | 1,320.00 USD | `-8.14%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `659.50` | 2,840,000.00 USD | 0.00 USD | 13,060.00 USD | `-8.00%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `660.50` | 2,830,000.00 USD | 0.00 USD | 11,090.00 USD | `-7.86%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `661.50` | 2,820,000.00 USD | 0.00 USD | 11,310.00 USD | `-7.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `662.50` | 2,810,000.00 USD | 0.00 USD | 7,780.00 USD | `-7.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `663.50` | 2,800,000.00 USD | 0.00 USD | 2,840.00 USD | `-7.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `664.50` | 2,800,000.00 USD | 0.00 USD | 864.51 USD | `-7.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `665.50` | 2,800,000.00 USD | 0.00 USD | 12,180.00 USD | `-7.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `666.50` | 2,790,000.00 USD | 0.00 USD | 24,530.00 USD | `-7.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `667.50` | 2,760,000.00 USD | 0.00 USD | 10,740.00 USD | `-6.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `668.50` | 2,750,000.00 USD | 0.00 USD | 760.75 USD | `-6.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `669.50` | 2,750,000.00 USD | 0.00 USD | 2,390.00 USD | `-6.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `670.50` | 2,750,000.00 USD | 0.00 USD | 126,240.00 USD | `-6.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `671.50` | 2,620,000.00 USD | 0.00 USD | 19,600.00 USD | `-6.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `672.50` | 2,600,000.00 USD | 0.00 USD | 1,500.00 USD | `-6.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `673.50` | 2,600,000.00 USD | 0.00 USD | 7,790.00 USD | `-6.05%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `674.50` | 2,590,000.00 USD | 0.00 USD | 1,470.00 USD | `-5.91%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `675.50` | 2,590,000.00 USD | 0.00 USD | 10,640.00 USD | `-5.77%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `676.50` | 2,580,000.00 USD | 0.00 USD | 56,290.00 USD | `-5.63%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `677.50` | 2,520,000.00 USD | 0.00 USD | 39,650.00 USD | `-5.49%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `678.50` | 2,480,000.00 USD | 0.00 USD | 825.73 USD | `-5.35%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `679.50` | 2,480,000.00 USD | 0.00 USD | 5,250.00 USD | `-5.21%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `680.50` | 2,480,000.00 USD | 0.00 USD | 297,550.00 USD | `-5.07%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `681.50` | 2,180,000.00 USD | 0.00 USD | 146.52 USD | `-4.94%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `682.50` | 2,180,000.00 USD | 0.00 USD | 1,160,000.00 USD | `-4.80%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `683.50` | 1,020,000.00 USD | 0.00 USD | 171,850.00 USD | `-4.66%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `684.50` | 849,300.00 USD | 0.00 USD | 171,120.00 USD | `-4.52%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `685.50` | 678,180.00 USD | 0.00 USD | 11,030.00 USD | `-4.38%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `686.50` | 667,150.00 USD | 0.00 USD | 530.66 USD | `-4.24%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `687.50` | 666,620.00 USD | 0.00 USD | 653.81 USD | `-4.10%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `688.50` | 665,970.00 USD | 0.00 USD | 364.22 USD | `-3.96%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `689.50` | 665,600.00 USD | 0.00 USD | 532.98 USD | `-3.82%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `690.50` | 665,070.00 USD | 0.00 USD | 3,860.00 USD | `-3.68%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `691.50` | 661,210.00 USD | 0.00 USD | 173,590.00 USD | `-3.54%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `692.50` | 487,610.00 USD | 0.00 USD | 2,420.00 USD | `-3.40%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `693.50` | 485,200.00 USD | 0.00 USD | 7,180.00 USD | `-3.26%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `694.50` | 478,020.00 USD | 0.00 USD | 815.34 USD | `-3.12%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `695.50` | 477,200.00 USD | 0.00 USD | 166.92 USD | `-2.98%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `696.50` | 477,030.00 USD | 0.00 USD | 2,200.00 USD | `-2.84%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `697.50` | 474,830.00 USD | 0.00 USD | 47,550.00 USD | `-2.70%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `698.50` | 427,280.00 USD | 0.00 USD | 15,500.00 USD | `-2.56%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `699.50` | 411,780.00 USD | 0.00 USD | 38,470.00 USD | `-2.42%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `700.50` | 373,310.00 USD | 0.00 USD | 41,530.00 USD | `-2.28%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `701.50` | 331,780.00 USD | 0.00 USD | 329.70 USD | `-2.15%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `702.50` | 331,450.00 USD | 0.00 USD | 29,960.00 USD | `-2.01%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `703.50` | 301,490.00 USD | 0.00 USD | 3,850.00 USD | `-1.87%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `704.50` | 297,640.00 USD | 0.00 USD | 86,660.00 USD | `-1.73%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `705.50` | 210,980.00 USD | 0.00 USD | 640.59 USD | `-1.59%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `706.50` | 210,340.00 USD | 0.00 USD | 10,430.00 USD | `-1.45%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `707.50` | 199,910.00 USD | 0.00 USD | 182.53 USD | `-1.31%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `708.50` | 199,730.00 USD | 0.00 USD | 10,760.00 USD | `-1.17%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `709.50` | 188,970.00 USD | 0.00 USD | 247.62 USD | `-1.03%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `710.50` | 188,730.00 USD | 0.00 USD | 7,940.00 USD | `-0.89%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `711.50` | 180,780.00 USD | 0.00 USD | 6,700.00 USD | `-0.75%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `712.50` | 174,080.00 USD | 0.00 USD | 473.81 USD | `-0.61%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `713.50` | 173,610.00 USD | 0.00 USD | 150.55 USD | `-0.47%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `714.50` | 173,450.00 USD | 0.00 USD | 1,660.00 USD | `-0.33%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `715.50` | 171,790.00 USD | 0.00 USD | 3,100.00 USD | `-0.19%` | `TACTICAL (Retail Cluster)` |
| `Sell Stop` | `716.50` | 168,690.00 USD | 0.00 USD | 168,690.00 USD | `-0.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `717.50` | 1,050.00 USD | 1,050.00 USD | 0.00 USD | `+0.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `718.50` | 81,910.00 USD | 80,870.00 USD | 0.00 USD | `+0.23%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `719.50` | 152,150.00 USD | 70,240.00 USD | 0.00 USD | `+0.37%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `720.50` | 176,190.00 USD | 24,040.00 USD | 0.00 USD | `+0.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `721.50` | 221,960.00 USD | 45,770.00 USD | 0.00 USD | `+0.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `722.50` | 223,840.00 USD | 1,880.00 USD | 0.00 USD | `+0.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `723.50` | 230,770.00 USD | 6,930.00 USD | 0.00 USD | `+0.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `724.50` | 256,470.00 USD | 25,700.00 USD | 0.00 USD | `+1.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `725.50` | 348,150.00 USD | 91,680.00 USD | 0.00 USD | `+1.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `726.50` | 348,660.00 USD | 501.28 USD | 0.00 USD | `+1.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `727.50` | 369,730.00 USD | 21,070.00 USD | 0.00 USD | `+1.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `728.50` | 406,560.00 USD | 36,830.00 USD | 0.00 USD | `+1.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `729.50` | 547,370.00 USD | 140,810.00 USD | 0.00 USD | `+1.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `730.50` | 550,830.00 USD | 3,460.00 USD | 0.00 USD | `+1.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `731.50` | 770,790.00 USD | 219,960.00 USD | 0.00 USD | `+2.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `732.50` | 771,370.00 USD | 587.47 USD | 0.00 USD | `+2.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `733.50` | 1,260,000.00 USD | 487,020.00 USD | 0.00 USD | `+2.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `734.50` | 1,270,000.00 USD | 7,640.00 USD | 0.00 USD | `+2.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `735.50` | 1,290,000.00 USD | 23,710.00 USD | 0.00 USD | `+2.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `736.50` | 1,300,000.00 USD | 6,860.00 USD | 0.00 USD | `+2.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `737.50` | 1,300,000.00 USD | 3,970.00 USD | 0.00 USD | `+2.88%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `738.50` | 1,310,000.00 USD | 12,620.00 USD | 0.00 USD | `+3.02%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `739.50` | 1,310,000.00 USD | 790.53 USD | 0.00 USD | `+3.16%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `740.50` | 1,320,000.00 USD | 7,380.00 USD | 0.00 USD | `+3.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `741.50` | 1,330,000.00 USD | 3,840.00 USD | 0.00 USD | `+3.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `742.50` | 1,330,000.00 USD | 4,540.00 USD | 0.00 USD | `+3.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `743.50` | 1,330,000.00 USD | 2,600.00 USD | 0.00 USD | `+3.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `744.50` | 1,540,000.00 USD | 203,810.00 USD | 0.00 USD | `+3.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `745.50` | 1,550,000.00 USD | 15,800.00 USD | 0.00 USD | `+3.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `746.50` | 1,550,000.00 USD | 672.60 USD | 0.00 USD | `+4.13%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `747.50` | 1,550,000.00 USD | 1,070.00 USD | 0.00 USD | `+4.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `748.50` | 1,550,000.00 USD | 279.19 USD | 0.00 USD | `+4.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `749.50` | 1,550,000.00 USD | 704.53 USD | 0.00 USD | `+4.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `750.50` | 1,550,000.00 USD | 123.83 USD | 0.00 USD | `+4.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `751.50` | 1,570,000.00 USD | 13,550.00 USD | 0.00 USD | `+4.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `752.50` | 1,570,000.00 USD | 2,730.00 USD | 0.00 USD | `+4.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `753.50` | 1,570,000.00 USD | 629.17 USD | 0.00 USD | `+5.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `754.50` | 1,620,000.00 USD | 47,160.00 USD | 0.00 USD | `+5.25%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `755.50` | 1,620,000.00 USD | 4,420.00 USD | 0.00 USD | `+5.39%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `756.50` | 1,640,000.00 USD | 13,030.00 USD | 0.00 USD | `+5.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `757.50` | 1,780,000.00 USD | 142,940.00 USD | 0.00 USD | `+5.67%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `758.50` | 1,780,000.00 USD | 2,920.00 USD | 0.00 USD | `+5.81%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `759.50` | 1,780,000.00 USD | 325.07 USD | 0.00 USD | `+5.95%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `760.50` | 2,070,000.00 USD | 288,360.00 USD | 0.00 USD | `+6.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `761.50` | 2,080,000.00 USD | 11,460.00 USD | 0.00 USD | `+6.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `762.50` | 2,080,000.00 USD | 274.50 USD | 0.00 USD | `+6.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `763.50` | 2,130,000.00 USD | 45,960.00 USD | 0.00 USD | `+6.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `764.50` | 2,130,000.00 USD | 323.38 USD | 0.00 USD | `+6.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `765.50` | 2,170,000.00 USD | 41,050.00 USD | 0.00 USD | `+6.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `766.50` | 2,170,000.00 USD | 600.94 USD | 0.00 USD | `+6.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `767.50` | 2,640,000.00 USD | 468,310.00 USD | 0.00 USD | `+7.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `768.50` | 2,640,000.00 USD | 180.60 USD | 0.00 USD | `+7.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `769.50` | 2,640,000.00 USD | 171.60 USD | 0.00 USD | `+7.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `770.50` | 2,640,000.00 USD | 1,540.00 USD | 0.00 USD | `+7.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `771.50` | 2,640,000.00 USD | 242.25 USD | 0.00 USD | `+7.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `772.50` | 2,650,000.00 USD | 12,050.00 USD | 0.00 USD | `+7.76%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `773.50` | 2,650,000.00 USD | 656.70 USD | 0.00 USD | `+7.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `774.50` | 2,660,000.00 USD | 9,680.00 USD | 0.00 USD | `+8.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `775.50` | 2,670,000.00 USD | 4,570.00 USD | 0.00 USD | `+8.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `776.50` | 2,680,000.00 USD | 14,230.00 USD | 0.00 USD | `+8.32%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `777.50` | 2,700,000.00 USD | 15,690.00 USD | 0.00 USD | `+8.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `778.50` | 2,700,000.00 USD | 4,580.00 USD | 0.00 USD | `+8.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `779.50` | 2,700,000.00 USD | 132.52 USD | 0.00 USD | `+8.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `780.50` | 2,730,000.00 USD | 24,280.00 USD | 0.00 USD | `+8.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `781.50` | 2,730,000.00 USD | 2,050.00 USD | 0.00 USD | `+9.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `782.50` | 2,730,000.00 USD | 1,900.00 USD | 0.00 USD | `+9.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `783.50` | 2,730,000.00 USD | 101.07 USD | 0.00 USD | `+9.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `784.50` | 2,730,000.00 USD | 102.77 USD | 0.00 USD | `+9.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `785.50` | 2,730,000.00 USD | 559.28 USD | 0.00 USD | `+9.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `786.50` | 2,740,000.00 USD | 11,990.00 USD | 0.00 USD | `+9.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `787.50` | 2,750,000.00 USD | 2,260.00 USD | 0.00 USD | `+9.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `788.50` | 2,750,000.00 USD | 133.26 USD | 0.00 USD | `+9.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `790.50` | 2,750,000.00 USD | 4,190.00 USD | 0.00 USD | `+10.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `791.50` | 2,750,000.00 USD | 704.44 USD | 0.00 USD | `+10.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `792.50` | 2,760,000.00 USD | 4,360.00 USD | 0.00 USD | `+10.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `793.50` | 2,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+10.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `794.50` | 2,760,000.00 USD | 3,630.00 USD | 0.00 USD | `+10.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `795.50` | 2,760,000.00 USD | 3,040.00 USD | 0.00 USD | `+10.97%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `796.50` | 2,760,000.00 USD | 154.52 USD | 0.00 USD | `+11.11%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `799.50` | 2,760,000.00 USD | 1,450.00 USD | 0.00 USD | `+11.52%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `800.50` | 2,780,000.00 USD | 12,890.00 USD | 0.00 USD | `+11.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `801.50` | 2,780,000.00 USD | 120.22 USD | 0.00 USD | `+11.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `803.50` | 2,780,000.00 USD | 803.50 USD | 0.00 USD | `+12.08%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `805.50` | 2,780,000.00 USD | 120.02 USD | 0.00 USD | `+12.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `806.50` | 2,780,000.00 USD | 1,300.00 USD | 0.00 USD | `+12.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `808.50` | 2,790,000.00 USD | 5,010.00 USD | 0.00 USD | `+12.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `809.50` | 2,790,000.00 USD | 242.04 USD | 0.00 USD | `+12.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `810.50` | 2,800,000.00 USD | 15,790.00 USD | 0.00 USD | `+13.06%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `811.50` | 2,810,000.00 USD | 6,050.00 USD | 0.00 USD | `+13.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `812.50` | 2,810,000.00 USD | 844.19 USD | 0.00 USD | `+13.34%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `813.50` | 2,810,000.00 USD | 109.82 USD | 0.00 USD | `+13.48%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `814.50` | 2,810,000.00 USD | 3,390.00 USD | 0.00 USD | `+13.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `816.50` | 2,810,000.00 USD | 984.70 USD | 0.00 USD | `+13.90%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `817.50` | 2,810,000.00 USD | 162.68 USD | 0.00 USD | `+14.04%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `818.50` | 2,820,000.00 USD | 5,990.00 USD | 0.00 USD | `+14.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `820.50` | 2,830,000.00 USD | 8,230.00 USD | 0.00 USD | `+14.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `824.50` | 2,830,000.00 USD | 408.13 USD | 0.00 USD | `+15.01%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `826.50` | 2,830,000.00 USD | 672.77 USD | 0.00 USD | `+15.29%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `827.50` | 2,830,000.00 USD | 276.38 USD | 0.00 USD | `+15.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `828.50` | 2,830,000.00 USD | 1,800.00 USD | 0.00 USD | `+15.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `830.50` | 2,870,000.00 USD | 35,850.00 USD | 0.00 USD | `+15.85%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `833.50` | 2,870,000.00 USD | 1,050.00 USD | 0.00 USD | `+16.27%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `835.50` | 2,870,000.00 USD | 187.15 USD | 0.00 USD | `+16.55%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `836.50` | 2,870,000.00 USD | 372.24 USD | 0.00 USD | `+16.69%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `837.50` | 2,870,000.00 USD | 326.62 USD | 0.00 USD | `+16.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `839.50` | 2,870,000.00 USD | 296.34 USD | 0.00 USD | `+17.10%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `840.50` | 2,870,000.00 USD | 441.26 USD | 0.00 USD | `+17.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `841.50` | 2,870,000.00 USD | 329.87 USD | 0.00 USD | `+17.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `843.50` | 2,870,000.00 USD | 425.97 USD | 0.00 USD | `+17.66%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `844.50` | 2,870,000.00 USD | 1,770.00 USD | 0.00 USD | `+17.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `850.50` | 2,870,000.00 USD | 2,550.00 USD | 0.00 USD | `+18.64%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `851.50` | 2,890,000.00 USD | 11,650.00 USD | 0.00 USD | `+18.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `852.50` | 2,890,000.00 USD | 102.30 USD | 0.00 USD | `+18.92%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `854.50` | 2,890,000.00 USD | 137.57 USD | 0.00 USD | `+19.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `857.50` | 2,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+19.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `860.50` | 2,890,000.00 USD | 1,160.00 USD | 0.00 USD | `+20.03%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `862.50` | 2,890,000.00 USD | 1,200.00 USD | 0.00 USD | `+20.31%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `863.50` | 2,890,000.00 USD | 874.73 USD | 0.00 USD | `+20.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `864.50` | 2,890,000.00 USD | 2,970.00 USD | 0.00 USD | `+20.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `865.50` | 2,900,000.00 USD | 3,460.00 USD | 0.00 USD | `+20.73%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `868.50` | 2,900,000.00 USD | 2,610.00 USD | 0.00 USD | `+21.15%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `870.50` | 2,900,000.00 USD | 228.07 USD | 0.00 USD | `+21.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `872.50` | 2,900,000.00 USD | 1,110.00 USD | 0.00 USD | `+21.71%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `884.50` | 2,960,000.00 USD | 54,820.00 USD | 0.00 USD | `+23.38%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `888.50` | 2,960,000.00 USD | 266.55 USD | 0.00 USD | `+23.94%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `890.50` | 2,960,000.00 USD | 690.14 USD | 0.00 USD | `+24.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `891.50` | 2,960,000.00 USD | 605.33 USD | 0.00 USD | `+24.36%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `900.50` | 3,090,000.00 USD | 132,720.00 USD | 0.00 USD | `+25.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `904.50` | 3,090,000.00 USD | 167.33 USD | 0.00 USD | `+26.17%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `907.50` | 3,090,000.00 USD | 1,640.00 USD | 0.00 USD | `+26.59%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `913.50` | 3,090,000.00 USD | 908.02 USD | 0.00 USD | `+27.43%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `914.50` | 3,100,000.00 USD | 4,150.00 USD | 0.00 USD | `+27.57%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `917.50` | 3,100,000.00 USD | 533.99 USD | 0.00 USD | `+27.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `919.50` | 3,100,000.00 USD | 166.43 USD | 0.00 USD | `+28.26%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `920.50` | 3,100,000.00 USD | 463.01 USD | 0.00 USD | `+28.40%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `926.50` | 3,100,000.00 USD | 320.57 USD | 0.00 USD | `+29.24%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `930.50` | 3,100,000.00 USD | 552.72 USD | 0.00 USD | `+29.80%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `933.50` | 3,100,000.00 USD | 196.03 USD | 0.00 USD | `+30.22%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `935.50` | 3,100,000.00 USD | 287.20 USD | 0.00 USD | `+30.50%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `958.50` | 3,100,000.00 USD | 782.14 USD | 0.00 USD | `+33.70%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `959.50` | 3,100,000.00 USD | 498.94 USD | 0.00 USD | `+33.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `964.50` | 3,100,000.00 USD | 964.50 USD | 0.00 USD | `+34.54%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `965.50` | 3,100,000.00 USD | 1,930.00 USD | 0.00 USD | `+34.68%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `977.50` | 3,100,000.00 USD | 293.25 USD | 0.00 USD | `+36.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `980.50` | 3,100,000.00 USD | 1,300.00 USD | 0.00 USD | `+36.77%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `981.50` | 3,100,000.00 USD | 109.93 USD | 0.00 USD | `+36.91%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `984.50` | 3,110,000.00 USD | 439.09 USD | 0.00 USD | `+37.33%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `987.50` | 3,110,000.00 USD | 2,590.00 USD | 0.00 USD | `+37.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `995.50` | 3,110,000.00 USD | 145.34 USD | 0.00 USD | `+38.87%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `997.50` | 3,110,000.00 USD | 1,840.00 USD | 0.00 USD | `+39.14%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `998.50` | 3,110,000.00 USD | 3,990.00 USD | 0.00 USD | `+39.28%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `999.50` | 3,110,000.00 USD | 938.53 USD | 0.00 USD | `+39.42%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1000.50` | 3,130,000.00 USD | 11,810.00 USD | 0.00 USD | `+39.56%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1017.50` | 3,130,000.00 USD | 203.50 USD | 0.00 USD | `+41.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1020.50` | 3,130,000.00 USD | 148.99 USD | 0.00 USD | `+42.35%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1026.50` | 3,130,000.00 USD | 149.87 USD | 0.00 USD | `+43.19%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1030.50` | 3,130,000.00 USD | 150.45 USD | 0.00 USD | `+43.75%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1045.50` | 3,130,000.00 USD | 195.51 USD | 0.00 USD | `+45.84%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1053.50` | 3,130,000.00 USD | 149.60 USD | 0.00 USD | `+46.96%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1072.50` | 3,130,000.00 USD | 156.58 USD | 0.00 USD | `+49.61%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1100.50` | 3,130,000.00 USD | 278.43 USD | 0.00 USD | `+53.51%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1111.50` | 3,130,000.00 USD | 555.75 USD | 0.00 USD | `+55.05%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1136.50` | 3,130,000.00 USD | 165.93 USD | 0.00 USD | `+58.53%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1146.50` | 3,130,000.00 USD | 167.39 USD | 0.00 USD | `+59.93%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1200.50` | 3,190,000.00 USD | 62,330.00 USD | 0.00 USD | `+67.46%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1202.50` | 3,190,000.00 USD | 1,250.00 USD | 0.00 USD | `+67.74%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1226.50` | 3,190,000.00 USD | 235.49 USD | 0.00 USD | `+71.09%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1230.50` | 3,200,000.00 USD | 3,580.00 USD | 0.00 USD | `+71.65%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1250.50` | 3,200,000.00 USD | 421.42 USD | 0.00 USD | `+74.44%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1280.50` | 3,200,000.00 USD | 3,750.00 USD | 0.00 USD | `+78.62%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1297.50` | 3,200,000.00 USD | 133.64 USD | 0.00 USD | `+80.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1300.50` | 3,200,000.00 USD | 685.36 USD | 0.00 USD | `+81.41%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1330.50` | 3,260,000.00 USD | 58,230.00 USD | 0.00 USD | `+85.60%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1340.50` | 3,340,000.00 USD | 80,850.00 USD | 0.00 USD | `+86.99%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1360.50` | 3,350,000.00 USD | 6,210.00 USD | 0.00 USD | `+89.78%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1363.50` | 3,350,000.00 USD | 349.06 USD | 0.00 USD | `+90.20%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1370.50` | 3,350,000.00 USD | 1,060.00 USD | 0.00 USD | `+91.18%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1372.50` | 3,370,000.00 USD | 19,210.00 USD | 0.00 USD | `+91.45%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1389.50` | 3,370,000.00 USD | 425.19 USD | 0.00 USD | `+93.83%` | `TACTICAL (Retail Cluster)` |
| `Buy Stop` | `1400.50` | 3,370,000.00 USD | 3,850.00 USD | 0.00 USD | `+95.36%` | `TACTICAL (Retail Cluster)` |

- **Exchange Multi-Horizon Liquidation Density Map Table (8_Exchange_Liquidation_Map_1D/7D.parquet)**:
| Horizon | Price (USD) | Cumulative Liq (USD) | Short Liq (USD) | Long Liq (USD) | Binance (USD) | OKX (USD) | Bybit (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `1D` | `643.80` | 46,750,000.00 USD | 0.00 USD | 46,750,000.00 USD | 78,500.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `644.60` | 46,670,000.00 USD | 0.00 USD | 46,670,000.00 USD | 364,070.00 USD | 10,420.00 USD | 341,610.00 USD |
| `1D` | `645.40` | 45,960,000.00 USD | 0.00 USD | 45,960,000.00 USD | 23,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `646.20` | 45,930,000.00 USD | 0.00 USD | 45,930,000.00 USD | 156,000.00 USD | 11,780.00 USD | 184,540.00 USD |
| `1D` | `647.00` | 45,580,000.00 USD | 0.00 USD | 45,580,000.00 USD | 204,530.00 USD | 2,560.00 USD | 33,810.00 USD |
| `1D` | `647.80` | 45,340,000.00 USD | 0.00 USD | 45,340,000.00 USD | 136,750.00 USD | 33,700.00 USD | 7,150.00 USD |
| `1D` | `648.60` | 45,160,000.00 USD | 0.00 USD | 45,160,000.00 USD | 92,180.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `649.40` | 45,070,000.00 USD | 0.00 USD | 45,070,000.00 USD | 46,360.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `650.20` | 45,020,000.00 USD | 0.00 USD | 45,020,000.00 USD | 67,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.00` | 44,960,000.00 USD | 0.00 USD | 44,960,000.00 USD | 184,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `651.80` | 44,770,000.00 USD | 0.00 USD | 44,770,000.00 USD | 0.00 USD | 0.00 USD | 94,590.00 USD |
| `1D` | `652.60` | 44,680,000.00 USD | 0.00 USD | 44,680,000.00 USD | 30,730.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `653.40` | 44,650,000.00 USD | 0.00 USD | 44,650,000.00 USD | 43,630.00 USD | 26,830.00 USD | 0.00 USD |
| `1D` | `654.20` | 44,580,000.00 USD | 0.00 USD | 44,580,000.00 USD | 73,900.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.00` | 44,500,000.00 USD | 0.00 USD | 44,500,000.00 USD | 88,130.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `655.80` | 44,420,000.00 USD | 0.00 USD | 44,420,000.00 USD | 184,590.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `656.60` | 44,230,000.00 USD | 0.00 USD | 44,230,000.00 USD | 121,760.00 USD | 40,970.00 USD | 825,700.00 USD |
| `1D` | `657.40` | 43,240,000.00 USD | 0.00 USD | 43,240,000.00 USD | 264,960.00 USD | 0.00 USD | 21,320.00 USD |
| `1D` | `658.20` | 42,960,000.00 USD | 0.00 USD | 42,960,000.00 USD | 795,080.00 USD | 14,920.00 USD | 0.00 USD |
| `1D` | `659.00` | 42,150,000.00 USD | 0.00 USD | 42,150,000.00 USD | 119,820.00 USD | 0.00 USD | 81,440.00 USD |
| `1D` | `659.80` | 41,940,000.00 USD | 0.00 USD | 41,940,000.00 USD | 69,270.00 USD | 7,460.00 USD | 14,670.00 USD |
| `1D` | `660.60` | 41,850,000.00 USD | 0.00 USD | 41,850,000.00 USD | 90,670.00 USD | 83,170.00 USD | 0.00 USD |
| `1D` | `661.40` | 41,680,000.00 USD | 0.00 USD | 41,680,000.00 USD | 462,080.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `662.20` | 41,220,000.00 USD | 0.00 USD | 41,220,000.00 USD | 149,020.00 USD | 155,800.00 USD | 0.00 USD |
| `1D` | `663.00` | 40,910,000.00 USD | 0.00 USD | 40,910,000.00 USD | 264,780.00 USD | 0.00 USD | 44,630.00 USD |
| `1D` | `663.80` | 40,600,000.00 USD | 0.00 USD | 40,600,000.00 USD | 62,940.00 USD | 69,400.00 USD | 64,090.00 USD |
| `7D` | `664.10` | 87,050,000.00 USD | 0.00 USD | 87,050,000.00 USD | 78,740.00 USD | 18,740.00 USD | 39,340.00 USD |
| `1D` | `664.60` | 40,410,000.00 USD | 0.00 USD | 40,410,000.00 USD | 1,330,000.00 USD | 0.00 USD | 61,580.00 USD |
| `7D` | `665.00` | 86,910,000.00 USD | 0.00 USD | 86,910,000.00 USD | 92,030.00 USD | 22,990.00 USD | 37,000.00 USD |
| `1D` | `665.40` | 39,020,000.00 USD | 0.00 USD | 39,020,000.00 USD | 696,240.00 USD | 4,540.00 USD | 11,460.00 USD |
| `7D` | `665.90` | 86,760,000.00 USD | 0.00 USD | 86,760,000.00 USD | 264,020.00 USD | 71,380.00 USD | 63,410.00 USD |
| `1D` | `666.20` | 38,310,000.00 USD | 0.00 USD | 38,310,000.00 USD | 235,820.00 USD | 88,780.00 USD | 750,630.00 USD |
| `7D` | `666.80` | 86,360,000.00 USD | 0.00 USD | 86,360,000.00 USD | 198,550.00 USD | 33,320.00 USD | 61,710.00 USD |
| `1D` | `667.00` | 37,230,000.00 USD | 0.00 USD | 37,230,000.00 USD | 938,620.00 USD | 26,880.00 USD | 40,700.00 USD |
| `7D` | `667.70` | 86,070,000.00 USD | 0.00 USD | 86,070,000.00 USD | 199,690.00 USD | 45,130.00 USD | 51,340.00 USD |
| `1D` | `667.80` | 36,220,000.00 USD | 0.00 USD | 36,220,000.00 USD | 393,190.00 USD | 154,140.00 USD | 0.00 USD |
| `1D` | `668.60` | 35,680,000.00 USD | 0.00 USD | 35,680,000.00 USD | 755,760.00 USD | 39,300.00 USD | 3,620.00 USD |
| `7D` | `668.60` | 85,770,000.00 USD | 0.00 USD | 85,770,000.00 USD | 387,530.00 USD | 92,860.00 USD | 51,060.00 USD |
| `1D` | `669.40` | 34,880,000.00 USD | 0.00 USD | 34,880,000.00 USD | 481,100.00 USD | 61,020.00 USD | 29,910.00 USD |
| `7D` | `669.50` | 85,240,000.00 USD | 0.00 USD | 85,240,000.00 USD | 341,150.00 USD | 38,130.00 USD | 108,970.00 USD |
| `1D` | `670.20` | 34,310,000.00 USD | 0.00 USD | 34,310,000.00 USD | 625,160.00 USD | 39,310.00 USD | 1,500,000.00 USD |
| `7D` | `670.40` | 84,750,000.00 USD | 0.00 USD | 84,750,000.00 USD | 319,660.00 USD | 93,800.00 USD | 77,380.00 USD |
| `1D` | `671.00` | 32,140,000.00 USD | 0.00 USD | 32,140,000.00 USD | 299,200.00 USD | 21,410.00 USD | 2,650.00 USD |
| `7D` | `671.30` | 84,260,000.00 USD | 0.00 USD | 84,260,000.00 USD | 335,750.00 USD | 57,500.00 USD | 42,050.00 USD |
| `1D` | `671.80` | 31,820,000.00 USD | 0.00 USD | 31,820,000.00 USD | 2,290,000.00 USD | 21,250.00 USD | 46,180.00 USD |
| `7D` | `672.20` | 83,830,000.00 USD | 0.00 USD | 83,830,000.00 USD | 180,230.00 USD | 62,620.00 USD | 74,250.00 USD |
| `1D` | `672.60` | 29,470,000.00 USD | 0.00 USD | 29,470,000.00 USD | 134,640.00 USD | 38,560.00 USD | 702,240.00 USD |
| `7D` | `673.10` | 83,510,000.00 USD | 0.00 USD | 83,510,000.00 USD | 394,120.00 USD | 64,970.00 USD | 42,710.00 USD |
| `1D` | `673.40` | 28,590,000.00 USD | 0.00 USD | 28,590,000.00 USD | 332,930.00 USD | 301,900.00 USD | 1,650,000.00 USD |
| `7D` | `674.00` | 83,010,000.00 USD | 0.00 USD | 83,010,000.00 USD | 335,670.00 USD | 105,910.00 USD | 80,360.00 USD |
| `1D` | `674.20` | 26,310,000.00 USD | 0.00 USD | 26,310,000.00 USD | 358,110.00 USD | 241,130.00 USD | 170,020.00 USD |
| `7D` | `674.90` | 82,490,000.00 USD | 0.00 USD | 82,490,000.00 USD | 247,070.00 USD | 31,490.00 USD | 44,420.00 USD |
| `1D` | `675.00` | 25,540,000.00 USD | 0.00 USD | 25,540,000.00 USD | 1,210,000.00 USD | 258,700.00 USD | 400,190.00 USD |
| `1D` | `675.80` | 23,670,000.00 USD | 0.00 USD | 23,670,000.00 USD | 1,450,000.00 USD | 196,370.00 USD | 152,240.00 USD |
| `7D` | `675.80` | 82,160,000.00 USD | 0.00 USD | 82,160,000.00 USD | 387,400.00 USD | 26,020.00 USD | 79,190.00 USD |
| `1D` | `676.60` | 21,870,000.00 USD | 0.00 USD | 21,870,000.00 USD | 355,620.00 USD | 363,790.00 USD | 353,090.00 USD |
| `7D` | `676.70` | 81,670,000.00 USD | 0.00 USD | 81,670,000.00 USD | 509,100.00 USD | 35,490.00 USD | 126,570.00 USD |
| `1D` | `677.40` | 20,800,000.00 USD | 0.00 USD | 20,800,000.00 USD | 317,920.00 USD | 49,130.00 USD | 250,200.00 USD |
| `7D` | `677.60` | 81,000,000.00 USD | 0.00 USD | 81,000,000.00 USD | 409,810.00 USD | 0.00 USD | 63,990.00 USD |
| `1D` | `678.20` | 20,180,000.00 USD | 0.00 USD | 20,180,000.00 USD | 254,050.00 USD | 236,970.00 USD | 137,470.00 USD |
| `7D` | `678.50` | 80,530,000.00 USD | 0.00 USD | 80,530,000.00 USD | 120,190.00 USD | 0.00 USD | 26,990.00 USD |
| `1D` | `679.00` | 19,550,000.00 USD | 0.00 USD | 19,550,000.00 USD | 1,170,000.00 USD | 0.00 USD | 71,540.00 USD |
| `7D` | `679.40` | 80,380,000.00 USD | 0.00 USD | 80,380,000.00 USD | 116,510.00 USD | 10,480.00 USD | 40,610.00 USD |
| `1D` | `679.80` | 18,310,000.00 USD | 0.00 USD | 18,310,000.00 USD | 1,450,000.00 USD | 220,780.00 USD | 298,080.00 USD |
| `7D` | `680.30` | 80,210,000.00 USD | 0.00 USD | 80,210,000.00 USD | 166,780.00 USD | 13,510.00 USD | 0.00 USD |
| `1D` | `680.60` | 16,340,000.00 USD | 0.00 USD | 16,340,000.00 USD | 27,720.00 USD | 153,320.00 USD | 143,090.00 USD |
| `7D` | `681.20` | 80,030,000.00 USD | 0.00 USD | 80,030,000.00 USD | 106,280.00 USD | 7,050.00 USD | 35,170.00 USD |
| `1D` | `681.40` | 16,020,000.00 USD | 0.00 USD | 16,020,000.00 USD | 616,620.00 USD | 414,700.00 USD | 44,240.00 USD |
| `7D` | `682.10` | 79,880,000.00 USD | 0.00 USD | 79,880,000.00 USD | 0.00 USD | 23,360.00 USD | 27,620.00 USD |
| `1D` | `682.20` | 14,940,000.00 USD | 0.00 USD | 14,940,000.00 USD | 308,390.00 USD | 16,030.00 USD | 0.00 USD |
| `1D` | `683.00` | 14,620,000.00 USD | 0.00 USD | 14,620,000.00 USD | 690,810.00 USD | 59,430.00 USD | 37,900.00 USD |
| `7D` | `683.00` | 79,830,000.00 USD | 0.00 USD | 79,830,000.00 USD | 175,930.00 USD | 28,470.00 USD | 11,520.00 USD |
| `1D` | `683.80` | 13,830,000.00 USD | 0.00 USD | 13,830,000.00 USD | 405,890.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `683.90` | 79,620,000.00 USD | 0.00 USD | 79,620,000.00 USD | 77,000.00 USD | 29,510.00 USD | 17,480.00 USD |
| `1D` | `684.60` | 13,390,000.00 USD | 0.00 USD | 13,390,000.00 USD | 138,250.00 USD | 37,350.00 USD | 0.00 USD |
| `7D` | `684.80` | 79,490,000.00 USD | 0.00 USD | 79,490,000.00 USD | 246,080.00 USD | 9,850.00 USD | 39,550.00 USD |
| `1D` | `685.40` | 13,210,000.00 USD | 0.00 USD | 13,210,000.00 USD | 406,260.00 USD | 54,190.00 USD | 0.00 USD |
| `7D` | `685.70` | 79,200,000.00 USD | 0.00 USD | 79,200,000.00 USD | 197,040.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `686.20` | 12,750,000.00 USD | 0.00 USD | 12,750,000.00 USD | 1,050,000.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `686.60` | 79,000,000.00 USD | 0.00 USD | 79,000,000.00 USD | 62,990.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.00` | 11,700,000.00 USD | 0.00 USD | 11,700,000.00 USD | 130,820.00 USD | 96,690.00 USD | 98,790.00 USD |
| `7D` | `687.50` | 78,940,000.00 USD | 0.00 USD | 78,940,000.00 USD | 148,480.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `687.80` | 11,370,000.00 USD | 0.00 USD | 11,370,000.00 USD | 840,870.00 USD | 75,260.00 USD | 172,560.00 USD |
| `7D` | `688.40` | 78,790,000.00 USD | 0.00 USD | 78,790,000.00 USD | 67,880.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `688.60` | 10,280,000.00 USD | 0.00 USD | 10,280,000.00 USD | 420,000.00 USD | 84,090.00 USD | 444,740.00 USD |
| `7D` | `689.30` | 78,720,000.00 USD | 0.00 USD | 78,720,000.00 USD | 84,620.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `689.40` | 9,330,000.00 USD | 0.00 USD | 9,330,000.00 USD | 77,980.00 USD | 60,350.00 USD | 813,820.00 USD |
| `1D` | `690.20` | 8,380,000.00 USD | 0.00 USD | 8,380,000.00 USD | 31,110.00 USD | 52,210.00 USD | 212,990.00 USD |
| `7D` | `690.20` | 78,640,000.00 USD | 0.00 USD | 78,640,000.00 USD | 283,920.00 USD | 63,230.00 USD | 82,450.00 USD |
| `1D` | `691.00` | 8,080,000.00 USD | 0.00 USD | 8,080,000.00 USD | 0.00 USD | 141,060.00 USD | 17,880.00 USD |
| `7D` | `691.10` | 78,210,000.00 USD | 0.00 USD | 78,210,000.00 USD | 362,020.00 USD | 61,370.00 USD | 81,090.00 USD |
| `1D` | `691.80` | 7,920,000.00 USD | 0.00 USD | 7,920,000.00 USD | 0.00 USD | 23,600.00 USD | 0.00 USD |
| `7D` | `692.00` | 77,700,000.00 USD | 0.00 USD | 77,700,000.00 USD | 322,430.00 USD | 18,850.00 USD | 58,910.00 USD |
| `7D` | `692.90` | 77,300,000.00 USD | 0.00 USD | 77,300,000.00 USD | 280,830.00 USD | 19,470.00 USD | 0.00 USD |
| `1D` | `693.40` | 7,900,000.00 USD | 0.00 USD | 7,900,000.00 USD | 0.00 USD | 60,140.00 USD | 273,200.00 USD |
| `7D` | `693.80` | 77,000,000.00 USD | 0.00 USD | 77,000,000.00 USD | 305,720.00 USD | 39,210.00 USD | 0.00 USD |
| `1D` | `694.20` | 7,570,000.00 USD | 0.00 USD | 7,570,000.00 USD | 0.00 USD | 117,630.00 USD | 180,380.00 USD |
| `7D` | `694.70` | 76,660,000.00 USD | 0.00 USD | 76,660,000.00 USD | 279,840.00 USD | 36,640.00 USD | 35,490.00 USD |
| `1D` | `695.00` | 7,270,000.00 USD | 0.00 USD | 7,270,000.00 USD | 239,550.00 USD | 64,240.00 USD | 175,000.00 USD |
| `7D` | `695.60` | 76,300,000.00 USD | 0.00 USD | 76,300,000.00 USD | 120,440.00 USD | 0.00 USD | 21,670.00 USD |
| `1D` | `695.80` | 6,790,000.00 USD | 0.00 USD | 6,790,000.00 USD | 0.00 USD | 34,140.00 USD | 0.00 USD |
| `7D` | `696.50` | 76,160,000.00 USD | 0.00 USD | 76,160,000.00 USD | 140,370.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `696.60` | 6,760,000.00 USD | 0.00 USD | 6,760,000.00 USD | 0.00 USD | 95,780.00 USD | 0.00 USD |
| `7D` | `697.40` | 76,020,000.00 USD | 0.00 USD | 76,020,000.00 USD | 189,100.00 USD | 19,230.00 USD | 0.00 USD |
| `1D` | `698.20` | 6,660,000.00 USD | 0.00 USD | 6,660,000.00 USD | 203,360.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `698.30` | 75,810,000.00 USD | 0.00 USD | 75,810,000.00 USD | 273,520.00 USD | 33,120.00 USD | 54,800.00 USD |
| `1D` | `699.00` | 6,460,000.00 USD | 0.00 USD | 6,460,000.00 USD | 276,500.00 USD | 31,670.00 USD | 42,650.00 USD |
| `7D` | `699.20` | 75,450,000.00 USD | 0.00 USD | 75,450,000.00 USD | 274,810.00 USD | 12,670.00 USD | 11,820.00 USD |
| `7D` | `700.10` | 75,150,000.00 USD | 0.00 USD | 75,150,000.00 USD | 225,450.00 USD | 40,820.00 USD | 27,440.00 USD |
| `1D` | `700.60` | 6,110,000.00 USD | 0.00 USD | 6,110,000.00 USD | 190,120.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `701.00` | 74,860,000.00 USD | 0.00 USD | 74,860,000.00 USD | 237,800.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `701.40` | 5,920,000.00 USD | 0.00 USD | 5,920,000.00 USD | 0.00 USD | 59,260.00 USD | 0.00 USD |
| `7D` | `701.90` | 74,620,000.00 USD | 0.00 USD | 74,620,000.00 USD | 135,260.00 USD | 41,260.00 USD | 89,700.00 USD |
| `1D` | `702.20` | 5,860,000.00 USD | 0.00 USD | 5,860,000.00 USD | 138,970.00 USD | 91,260.00 USD | 52,230.00 USD |
| `7D` | `702.80` | 74,360,000.00 USD | 0.00 USD | 74,360,000.00 USD | 416,820.00 USD | 57,470.00 USD | 36,720.00 USD |
| `1D` | `703.00` | 5,570,000.00 USD | 0.00 USD | 5,570,000.00 USD | 232,220.00 USD | 12,930.00 USD | 208,020.00 USD |
| `7D` | `703.70` | 73,840,000.00 USD | 0.00 USD | 73,840,000.00 USD | 311,800.00 USD | 44,990.00 USD | 0.00 USD |
| `1D` | `703.80` | 5,120,000.00 USD | 0.00 USD | 5,120,000.00 USD | 357,750.00 USD | 45,990.00 USD | 468,050.00 USD |
| `1D` | `704.60` | 4,250,000.00 USD | 0.00 USD | 4,250,000.00 USD | 62,230.00 USD | 12,800.00 USD | 247,060.00 USD |
| `7D` | `704.60` | 73,490,000.00 USD | 0.00 USD | 73,490,000.00 USD | 537,050.00 USD | 136,550.00 USD | 194,460.00 USD |
| `1D` | `705.40` | 3,930,000.00 USD | 0.00 USD | 3,930,000.00 USD | 0.00 USD | 23,130.00 USD | 121,600.00 USD |
| `7D` | `705.50` | 72,620,000.00 USD | 0.00 USD | 72,620,000.00 USD | 920,340.00 USD | 162,820.00 USD | 236,670.00 USD |
| `1D` | `706.20` | 3,780,000.00 USD | 0.00 USD | 3,780,000.00 USD | 237,450.00 USD | 0.00 USD | 123,170.00 USD |
| `7D` | `706.40` | 71,300,000.00 USD | 0.00 USD | 71,300,000.00 USD | 523,540.00 USD | 104,380.00 USD | 231,200.00 USD |
| `7D` | `707.30` | 70,440,000.00 USD | 0.00 USD | 70,440,000.00 USD | 604,060.00 USD | 90,200.00 USD | 53,960.00 USD |
| `1D` | `707.80` | 3,420,000.00 USD | 0.00 USD | 3,420,000.00 USD | 201,590.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `708.20` | 69,690,000.00 USD | 0.00 USD | 69,690,000.00 USD | 796,640.00 USD | 138,200.00 USD | 42,800.00 USD |
| `1D` | `708.60` | 3,220,000.00 USD | 0.00 USD | 3,220,000.00 USD | 109,380.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `709.10` | 68,710,000.00 USD | 0.00 USD | 68,710,000.00 USD | 392,150.00 USD | 156,040.00 USD | 195,500.00 USD |
| `1D` | `709.40` | 3,110,000.00 USD | 0.00 USD | 3,110,000.00 USD | 272,730.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `710.00` | 67,970,000.00 USD | 0.00 USD | 67,970,000.00 USD | 450,480.00 USD | 167,090.00 USD | 176,960.00 USD |
| `7D` | `710.90` | 67,180,000.00 USD | 0.00 USD | 67,180,000.00 USD | 922,450.00 USD | 160,040.00 USD | 236,990.00 USD |
| `1D` | `711.00` | 2,840,000.00 USD | 0.00 USD | 2,840,000.00 USD | 694,090.00 USD | 0.00 USD | 37,900.00 USD |
| `1D` | `711.80` | 2,110,000.00 USD | 0.00 USD | 2,110,000.00 USD | 250,690.00 USD | 0.00 USD | 38,770.00 USD |
| `7D` | `711.80` | 65,860,000.00 USD | 0.00 USD | 65,860,000.00 USD | 608,910.00 USD | 232,130.00 USD | 114,740.00 USD |
| `1D` | `712.60` | 1,820,000.00 USD | 0.00 USD | 1,820,000.00 USD | 0.00 USD | 0.00 USD | 21,320.00 USD |
| `7D` | `712.70` | 64,900,000.00 USD | 0.00 USD | 64,900,000.00 USD | 1,190,000.00 USD | 217,390.00 USD | 236,970.00 USD |
| `7D` | `713.60` | 63,260,000.00 USD | 0.00 USD | 63,260,000.00 USD | 2,250,000.00 USD | 279,180.00 USD | 308,960.00 USD |
| `7D` | `714.50` | 60,410,000.00 USD | 0.00 USD | 60,410,000.00 USD | 508,400.00 USD | 209,320.00 USD | 292,980.00 USD |
| `1D` | `715.00` | 1,800,000.00 USD | 0.00 USD | 1,800,000.00 USD | 0.00 USD | 317,060.00 USD | 415,380.00 USD |
| `7D` | `715.40` | 59,400,000.00 USD | 0.00 USD | 59,400,000.00 USD | 1,050,000.00 USD | 419,310.00 USD | 329,730.00 USD |
| `1D` | `715.80` | 1,060,000.00 USD | 0.00 USD | 1,060,000.00 USD | 0.00 USD | 0.00 USD | 1,060,000.00 USD |
| `7D` | `716.30` | 57,600,000.00 USD | 0.00 USD | 57,600,000.00 USD | 1,080,000.00 USD | 324,540.00 USD | 233,140.00 USD |
| `1D` | `716.40` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `717.20` | 55,960,000.00 USD | 0.00 USD | 55,960,000.00 USD | 581,610.00 USD | 398,030.00 USD | 387,120.00 USD |
| `7D` | `718.10` | 54,590,000.00 USD | 0.00 USD | 54,590,000.00 USD | 1,690,000.00 USD | 246,320.00 USD | 151,880.00 USD |
| `1D` | `719.00` | 82,030.00 USD | 82,030.00 USD | 0.00 USD | 0.00 USD | 82,030.00 USD | 0.00 USD |
| `7D` | `719.00` | 52,510,000.00 USD | 0.00 USD | 52,510,000.00 USD | 670,390.00 USD | 137,460.00 USD | 211,490.00 USD |
| `1D` | `719.80` | 166,220.00 USD | 166,220.00 USD | 0.00 USD | 60,590.00 USD | 23,600.00 USD | 0.00 USD |
| `7D` | `719.90` | 51,490,000.00 USD | 0.00 USD | 51,490,000.00 USD | 618,020.00 USD | 173,240.00 USD | 186,780.00 USD |
| `1D` | `720.60` | 578,690.00 USD | 578,690.00 USD | 0.00 USD | 207,940.00 USD | 204,540.00 USD | 0.00 USD |
| `7D` | `720.80` | 50,510,000.00 USD | 0.00 USD | 50,510,000.00 USD | 1,010,000.00 USD | 52,490.00 USD | 180,370.00 USD |
| `1D` | `721.40` | 816,230.00 USD | 816,230.00 USD | 0.00 USD | 100,790.00 USD | 78,640.00 USD | 58,100.00 USD |
| `7D` | `721.70` | 49,260,000.00 USD | 0.00 USD | 49,260,000.00 USD | 1,950,000.00 USD | 237,690.00 USD | 653,400.00 USD |
| `1D` | `722.20` | 1,360,000.00 USD | 1,360,000.00 USD | 0.00 USD | 28,010.00 USD | 123,420.00 USD | 391,200.00 USD |
| `7D` | `722.60` | 46,430,000.00 USD | 0.00 USD | 46,430,000.00 USD | 1,930,000.00 USD | 108,200.00 USD | 229,380.00 USD |
| `1D` | `723.00` | 1,980,000.00 USD | 1,980,000.00 USD | 0.00 USD | 191,050.00 USD | 250,670.00 USD | 176,360.00 USD |
| `7D` | `723.50` | 44,160,000.00 USD | 0.00 USD | 44,160,000.00 USD | 640,550.00 USD | 140,550.00 USD | 293,670.00 USD |
| `1D` | `723.80` | 2,840,000.00 USD | 2,840,000.00 USD | 0.00 USD | 380,140.00 USD | 392,010.00 USD | 88,480.00 USD |
| `7D` | `724.40` | 43,080,000.00 USD | 0.00 USD | 43,080,000.00 USD | 663,550.00 USD | 186,780.00 USD | 130,770.00 USD |
| `1D` | `724.60` | 3,060,000.00 USD | 3,060,000.00 USD | 0.00 USD | 173,300.00 USD | 45,850.00 USD | 0.00 USD |
| `7D` | `725.30` | 42,100,000.00 USD | 0.00 USD | 42,100,000.00 USD | 1,760,000.00 USD | 418,390.00 USD | 396,690.00 USD |
| `1D` | `725.40` | 3,680,000.00 USD | 3,680,000.00 USD | 0.00 USD | 461,100.00 USD | 120,790.00 USD | 38,340.00 USD |
| `1D` | `726.20` | 3,940,000.00 USD | 3,940,000.00 USD | 0.00 USD | 256,420.00 USD | 10,760.00 USD | 0.00 USD |
| `7D` | `726.20` | 39,520,000.00 USD | 0.00 USD | 39,520,000.00 USD | 1,060,000.00 USD | 311,550.00 USD | 460,020.00 USD |
| `1D` | `727.00` | 4,320,000.00 USD | 4,320,000.00 USD | 0.00 USD | 299,310.00 USD | 75,120.00 USD | 0.00 USD |
| `7D` | `727.10` | 37,690,000.00 USD | 0.00 USD | 37,690,000.00 USD | 1,230,000.00 USD | 331,980.00 USD | 241,010.00 USD |
| `1D` | `727.80` | 4,710,000.00 USD | 4,710,000.00 USD | 0.00 USD | 339,770.00 USD | 48,110.00 USD | 0.00 USD |
| `7D` | `728.00` | 35,890,000.00 USD | 0.00 USD | 35,890,000.00 USD | 3,110,000.00 USD | 778,750.00 USD | 388,930.00 USD |
| `1D` | `728.60` | 4,800,000.00 USD | 4,800,000.00 USD | 0.00 USD | 23,160.00 USD | 23,030.00 USD | 49,400.00 USD |
| `7D` | `728.90` | 31,610,000.00 USD | 0.00 USD | 31,610,000.00 USD | 2,330,000.00 USD | 317,590.00 USD | 644,150.00 USD |
| `1D` | `729.40` | 6,040,000.00 USD | 6,040,000.00 USD | 0.00 USD | 359,560.00 USD | 259,230.00 USD | 616,880.00 USD |
| `7D` | `729.80` | 28,320,000.00 USD | 0.00 USD | 28,320,000.00 USD | 1,320,000.00 USD | 430,010.00 USD | 339,140.00 USD |
| `1D` | `730.20` | 8,040,000.00 USD | 8,040,000.00 USD | 0.00 USD | 1,720,000.00 USD | 213,600.00 USD | 73,220.00 USD |
| `7D` | `730.70` | 26,230,000.00 USD | 0.00 USD | 26,230,000.00 USD | 2,760,000.00 USD | 351,520.00 USD | 587,010.00 USD |
| `1D` | `731.00` | 11,470,000.00 USD | 11,470,000.00 USD | 0.00 USD | 1,250,000.00 USD | 230,860.00 USD | 1,950,000.00 USD |
| `7D` | `731.60` | 22,530,000.00 USD | 0.00 USD | 22,530,000.00 USD | 1,530,000.00 USD | 133,980.00 USD | 261,910.00 USD |
| `1D` | `731.80` | 12,560,000.00 USD | 12,560,000.00 USD | 0.00 USD | 276,840.00 USD | 171,500.00 USD | 645,890.00 USD |
| `7D` | `732.50` | 20,610,000.00 USD | 0.00 USD | 20,610,000.00 USD | 465,880.00 USD | 221,510.00 USD | 96,400.00 USD |
| `1D` | `732.60` | 14,910,000.00 USD | 14,910,000.00 USD | 0.00 USD | 864,610.00 USD | 107,040.00 USD | 1,380,000.00 USD |
| `1D` | `733.40` | 16,380,000.00 USD | 16,380,000.00 USD | 0.00 USD | 808,610.00 USD | 306,960.00 USD | 350,110.00 USD |
| `7D` | `733.40` | 19,820,000.00 USD | 0.00 USD | 19,820,000.00 USD | 1,910,000.00 USD | 158,310.00 USD | 338,540.00 USD |
| `1D` | `734.20` | 17,010,000.00 USD | 17,010,000.00 USD | 0.00 USD | 460,390.00 USD | 34,930.00 USD | 132,930.00 USD |
| `7D` | `734.30` | 17,420,000.00 USD | 0.00 USD | 17,420,000.00 USD | 1,580,000.00 USD | 288,470.00 USD | 244,940.00 USD |
| `1D` | `735.00` | 17,670,000.00 USD | 17,670,000.00 USD | 0.00 USD | 481,620.00 USD | 183,770.00 USD | 0.00 USD |
| `7D` | `735.20` | 15,310,000.00 USD | 0.00 USD | 15,310,000.00 USD | 1,330,000.00 USD | 172,940.00 USD | 437,510.00 USD |
| `1D` | `735.80` | 19,220,000.00 USD | 19,220,000.00 USD | 0.00 USD | 875,750.00 USD | 84,090.00 USD | 590,930.00 USD |
| `7D` | `736.10` | 13,370,000.00 USD | 0.00 USD | 13,370,000.00 USD | 2,130,000.00 USD | 181,990.00 USD | 484,910.00 USD |
| `1D` | `736.60` | 19,940,000.00 USD | 19,940,000.00 USD | 0.00 USD | 476,310.00 USD | 58,820.00 USD | 181,870.00 USD |
| `7D` | `737.00` | 10,570,000.00 USD | 0.00 USD | 10,570,000.00 USD | 2,360,000.00 USD | 175,330.00 USD | 633,690.00 USD |
| `1D` | `737.40` | 20,270,000.00 USD | 20,270,000.00 USD | 0.00 USD | 115,170.00 USD | 126,150.00 USD | 88,180.00 USD |
| `7D` | `737.90` | 7,400,000.00 USD | 0.00 USD | 7,400,000.00 USD | 3,420,000.00 USD | 72,280.00 USD | 374,090.00 USD |
| `1D` | `738.20` | 20,710,000.00 USD | 20,710,000.00 USD | 0.00 USD | 305,260.00 USD | 85,790.00 USD | 44,240.00 USD |
| `7D` | `738.80` | 3,530,000.00 USD | 0.00 USD | 3,530,000.00 USD | 522,950.00 USD | 20,210.00 USD | 155,300.00 USD |
| `1D` | `739.00` | 22,380,000.00 USD | 22,380,000.00 USD | 0.00 USD | 720,770.00 USD | 16,030.00 USD | 934,700.00 USD |
| `7D` | `739.70` | 2,830,000.00 USD | 0.00 USD | 2,830,000.00 USD | 352,500.00 USD | 0.00 USD | 203,030.00 USD |
| `1D` | `739.80` | 22,830,000.00 USD | 22,830,000.00 USD | 0.00 USD | 421,830.00 USD | 31,860.00 USD | 0.00 USD |
| `1D` | `740.60` | 23,180,000.00 USD | 23,180,000.00 USD | 0.00 USD | 211,010.00 USD | 134,150.00 USD | 0.00 USD |
| `7D` | `740.60` | 2,280,000.00 USD | 0.00 USD | 2,280,000.00 USD | 1,090,000.00 USD | 0.00 USD | 33,390.00 USD |
| `1D` | `741.40` | 23,570,000.00 USD | 23,570,000.00 USD | 0.00 USD | 366,560.00 USD | 32,240.00 USD | 0.00 USD |
| `7D` | `741.50` | 1,160,000.00 USD | 0.00 USD | 1,160,000.00 USD | 257,630.00 USD | 0.00 USD | 208,590.00 USD |
| `1D` | `742.20` | 23,880,000.00 USD | 23,880,000.00 USD | 0.00 USD | 291,160.00 USD | 15,840.00 USD | 0.00 USD |
| `7D` | `742.40` | 689,850.00 USD | 0.00 USD | 689,850.00 USD | 0.00 USD | 0.00 USD | 183,920.00 USD |
| `1D` | `743.00` | 24,110,000.00 USD | 24,110,000.00 USD | 0.00 USD | 233,270.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `743.30` | 505,930.00 USD | 0.00 USD | 505,930.00 USD | 0.00 USD | 0.00 USD | 57,580.00 USD |
| `1D` | `743.80` | 24,570,000.00 USD | 24,570,000.00 USD | 0.00 USD | 17,370.00 USD | 0.00 USD | 436,560.00 USD |
| `7D` | `744.20` | 448,350.00 USD | 0.00 USD | 448,350.00 USD | 0.00 USD | 257,580.00 USD | 141,790.00 USD |
| `1D` | `744.60` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 926,810.00 USD | 162,260.00 USD | 0.00 USD |
| `7D` | `745.10` | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD | 48,980.00 USD | 0.00 USD |
| `7D` | `745.20` | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `745.40` | 27,030,000.00 USD | 27,030,000.00 USD | 0.00 USD | 461,360.00 USD | 19,580.00 USD | 887,910.00 USD |
| `7D` | `746.00` | 999,320.00 USD | 999,320.00 USD | 0.00 USD | 999,320.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `746.20` | 27,950,000.00 USD | 27,950,000.00 USD | 0.00 USD | 563,040.00 USD | 135,740.00 USD | 221,170.00 USD |
| `7D` | `746.90` | 1,210,000.00 USD | 1,210,000.00 USD | 0.00 USD | 215,540.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `747.00` | 29,390,000.00 USD | 29,390,000.00 USD | 0.00 USD | 521,800.00 USD | 43,680.00 USD | 875,450.00 USD |
| `1D` | `747.80` | 29,800,000.00 USD | 29,800,000.00 USD | 0.00 USD | 145,680.00 USD | 103,400.00 USD | 164,280.00 USD |
| `1D` | `748.60` | 30,210,000.00 USD | 30,210,000.00 USD | 0.00 USD | 377,840.00 USD | 11,570.00 USD | 17,880.00 USD |
| `1D` | `749.40` | 30,530,000.00 USD | 30,530,000.00 USD | 0.00 USD | 321,760.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `750.20` | 30,700,000.00 USD | 30,700,000.00 USD | 0.00 USD | 171,230.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.00` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 71,910.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `751.80` | 31,290,000.00 USD | 31,290,000.00 USD | 0.00 USD | 103,120.00 USD | 25,010.00 USD | 393,600.00 USD |
| `1D` | `752.60` | 31,790,000.00 USD | 31,790,000.00 USD | 0.00 USD | 349,490.00 USD | 0.00 USD | 146,020.00 USD |
| `1D` | `753.40` | 32,170,000.00 USD | 32,170,000.00 USD | 0.00 USD | 127,360.00 USD | 3,810.00 USD | 248,870.00 USD |
| `1D` | `754.20` | 32,630,000.00 USD | 32,630,000.00 USD | 0.00 USD | 349,560.00 USD | 50,610.00 USD | 57,280.00 USD |
| `1D` | `755.00` | 33,080,000.00 USD | 33,080,000.00 USD | 0.00 USD | 235,060.00 USD | 178,540.00 USD | 37,120.00 USD |
| `7D` | `755.00` | 1,270,000.00 USD | 1,270,000.00 USD | 0.00 USD | 0.00 USD | 59,560.00 USD | 0.00 USD |
| `1D` | `755.80` | 33,460,000.00 USD | 33,460,000.00 USD | 0.00 USD | 263,490.00 USD | 96,170.00 USD | 19,780.00 USD |
| `1D` | `756.60` | 33,980,000.00 USD | 33,980,000.00 USD | 0.00 USD | 399,730.00 USD | 24,970.00 USD | 95,500.00 USD |
| `7D` | `756.80` | 1,320,000.00 USD | 1,320,000.00 USD | 0.00 USD | 0.00 USD | 47,340.00 USD | 0.00 USD |
| `1D` | `757.40` | 34,310,000.00 USD | 34,310,000.00 USD | 0.00 USD | 164,750.00 USD | 139,150.00 USD | 32,720.00 USD |
| `7D` | `757.70` | 1,910,000.00 USD | 1,910,000.00 USD | 0.00 USD | 475,510.00 USD | 113,240.00 USD | 0.00 USD |
| `1D` | `758.20` | 35,360,000.00 USD | 35,360,000.00 USD | 0.00 USD | 755,970.00 USD | 75,210.00 USD | 218,280.00 USD |
| `7D` | `758.60` | 3,100,000.00 USD | 3,100,000.00 USD | 0.00 USD | 1,190,000.00 USD | 0.00 USD | 0.00 USD |
| `1D` | `759.00` | 36,370,000.00 USD | 36,370,000.00 USD | 0.00 USD | 832,020.00 USD | 117,910.00 USD | 54,810.00 USD |
| `1D` | `759.80` | 36,790,000.00 USD | 36,790,000.00 USD | 0.00 USD | 383,590.00 USD | 21,070.00 USD | 15,370.00 USD |
| `7D` | `760.40` | 3,170,000.00 USD | 3,170,000.00 USD | 0.00 USD | 0.00 USD | 27,650.00 USD | 42,540.00 USD |
| `1D` | `760.60` | 37,150,000.00 USD | 37,150,000.00 USD | 0.00 USD | 268,390.00 USD | 52,630.00 USD | 35,930.00 USD |
| `7D` | `761.30` | 3,490,000.00 USD | 3,490,000.00 USD | 0.00 USD | 10,750.00 USD | 211,960.00 USD | 100,630.00 USD |
| `1D` | `761.40` | 38,160,000.00 USD | 38,160,000.00 USD | 0.00 USD | 756,450.00 USD | 8,690.00 USD | 250,520.00 USD |
| `1D` | `762.20` | 38,490,000.00 USD | 38,490,000.00 USD | 0.00 USD | 101,750.00 USD | 124,370.00 USD | 98,750.00 USD |
| `7D` | `762.20` | 4,370,000.00 USD | 4,370,000.00 USD | 0.00 USD | 0.00 USD | 699,820.00 USD | 179,270.00 USD |
| `1D` | `763.00` | 41,100,000.00 USD | 41,100,000.00 USD | 0.00 USD | 1,950,000.00 USD | 138,090.00 USD | 523,900.00 USD |
| `7D` | `763.10` | 7,830,000.00 USD | 7,830,000.00 USD | 0.00 USD | 2,460,000.00 USD | 590,460.00 USD | 404,720.00 USD |
| `1D` | `763.80` | 42,390,000.00 USD | 42,390,000.00 USD | 0.00 USD | 996,680.00 USD | 109,500.00 USD | 178,120.00 USD |
| `7D` | `764.00` | 10,270,000.00 USD | 10,270,000.00 USD | 0.00 USD | 1,590,000.00 USD | 441,980.00 USD | 402,300.00 USD |
| `1D` | `764.60` | 43,850,000.00 USD | 43,850,000.00 USD | 0.00 USD | 1,120,000.00 USD | 136,310.00 USD | 199,800.00 USD |
| `7D` | `764.90` | 12,470,000.00 USD | 12,470,000.00 USD | 0.00 USD | 1,450,000.00 USD | 352,570.00 USD | 395,630.00 USD |
| `1D` | `765.40` | 44,720,000.00 USD | 44,720,000.00 USD | 0.00 USD | 614,150.00 USD | 150,770.00 USD | 110,720.00 USD |
| `7D` | `765.80` | 15,460,000.00 USD | 15,460,000.00 USD | 0.00 USD | 2,470,000.00 USD | 107,550.00 USD | 416,290.00 USD |
| `1D` | `766.20` | 45,910,000.00 USD | 45,910,000.00 USD | 0.00 USD | 641,250.00 USD | 218,550.00 USD | 330,960.00 USD |
| `7D` | `766.70` | 20,050,000.00 USD | 20,050,000.00 USD | 0.00 USD | 3,330,000.00 USD | 416,530.00 USD | 842,330.00 USD |
| `1D` | `767.00` | 48,360,000.00 USD | 48,360,000.00 USD | 0.00 USD | 2,090,000.00 USD | 67,550.00 USD | 286,770.00 USD |
| `7D` | `767.60` | 23,430,000.00 USD | 23,430,000.00 USD | 0.00 USD | 2,790,000.00 USD | 123,530.00 USD | 467,840.00 USD |
| `1D` | `767.80` | 50,170,000.00 USD | 50,170,000.00 USD | 0.00 USD | 1,450,000.00 USD | 100,820.00 USD | 254,400.00 USD |
| `7D` | `768.50` | 25,660,000.00 USD | 25,660,000.00 USD | 0.00 USD | 1,840,000.00 USD | 95,830.00 USD | 281,920.00 USD |
| `1D` | `768.60` | 51,030,000.00 USD | 51,030,000.00 USD | 0.00 USD | 731,220.00 USD | 45,390.00 USD | 84,280.00 USD |
| `1D` | `769.40` | 51,370,000.00 USD | 51,370,000.00 USD | 0.00 USD | 291,010.00 USD | 38,990.00 USD | 8,460.00 USD |
| `7D` | `769.40` | 26,810,000.00 USD | 26,810,000.00 USD | 0.00 USD | 565,780.00 USD | 249,950.00 USD | 333,550.00 USD |
| `1D` | `770.20` | 51,780,000.00 USD | 51,780,000.00 USD | 0.00 USD | 288,220.00 USD | 97,130.00 USD | 28,450.00 USD |
| `7D` | `770.30` | 29,310,000.00 USD | 29,310,000.00 USD | 0.00 USD | 1,900,000.00 USD | 240,530.00 USD | 364,650.00 USD |
| `1D` | `771.00` | 52,390,000.00 USD | 52,390,000.00 USD | 0.00 USD | 156,280.00 USD | 52,310.00 USD | 397,910.00 USD |
| `7D` | `771.20` | 30,770,000.00 USD | 30,770,000.00 USD | 0.00 USD | 1,050,000.00 USD | 242,570.00 USD | 162,680.00 USD |
| `1D` | `771.80` | 53,270,000.00 USD | 53,270,000.00 USD | 0.00 USD | 246,790.00 USD | 53,740.00 USD | 582,120.00 USD |
| `7D` | `772.10` | 33,190,000.00 USD | 33,190,000.00 USD | 0.00 USD | 1,750,000.00 USD | 252,650.00 USD | 419,070.00 USD |
| `1D` | `772.60` | 53,720,000.00 USD | 53,720,000.00 USD | 0.00 USD | 286,150.00 USD | 150,000.00 USD | 16,360.00 USD |
| `7D` | `773.00` | 35,800,000.00 USD | 35,800,000.00 USD | 0.00 USD | 1,950,000.00 USD | 325,680.00 USD | 338,170.00 USD |
| `1D` | `773.40` | 54,420,000.00 USD | 54,420,000.00 USD | 0.00 USD | 618,270.00 USD | 10,490.00 USD | 68,320.00 USD |
| `7D` | `773.90` | 37,600,000.00 USD | 37,600,000.00 USD | 0.00 USD | 1,220,000.00 USD | 276,760.00 USD | 293,960.00 USD |
| `1D` | `774.20` | 55,010,000.00 USD | 55,010,000.00 USD | 0.00 USD | 568,370.00 USD | 19,250.00 USD | 1,360.00 USD |
| `7D` | `774.80` | 39,980,000.00 USD | 39,980,000.00 USD | 0.00 USD | 1,310,000.00 USD | 568,930.00 USD | 502,710.00 USD |
| `1D` | `775.00` | 55,180,000.00 USD | 55,180,000.00 USD | 0.00 USD | 54,760.00 USD | 34,120.00 USD | 86,160.00 USD |
| `7D` | `775.70` | 42,470,000.00 USD | 42,470,000.00 USD | 0.00 USD | 1,830,000.00 USD | 470,960.00 USD | 187,170.00 USD |
| `1D` | `775.80` | 55,380,000.00 USD | 55,380,000.00 USD | 0.00 USD | 126,750.00 USD | 24,070.00 USD | 49,120.00 USD |
| `1D` | `776.60` | 55,590,000.00 USD | 55,590,000.00 USD | 0.00 USD | 123,900.00 USD | 4,350.00 USD | 73,050.00 USD |
| `7D` | `776.60` | 44,740,000.00 USD | 44,740,000.00 USD | 0.00 USD | 1,630,000.00 USD | 269,050.00 USD | 378,590.00 USD |
| `1D` | `777.40` | 55,780,000.00 USD | 55,780,000.00 USD | 0.00 USD | 62,060.00 USD | 109,840.00 USD | 22,680.00 USD |
| `7D` | `777.50` | 46,480,000.00 USD | 46,480,000.00 USD | 0.00 USD | 1,350,000.00 USD | 243,990.00 USD | 148,450.00 USD |
| `1D` | `778.20` | 57,150,000.00 USD | 57,150,000.00 USD | 0.00 USD | 959,690.00 USD | 52,290.00 USD | 361,010.00 USD |
| `7D` | `778.40` | 48,170,000.00 USD | 48,170,000.00 USD | 0.00 USD | 1,180,000.00 USD | 307,370.00 USD | 206,530.00 USD |
| `1D` | `779.00` | 57,950,000.00 USD | 57,950,000.00 USD | 0.00 USD | 630,640.00 USD | 76,100.00 USD | 87,260.00 USD |
| `7D` | `779.30` | 49,730,000.00 USD | 49,730,000.00 USD | 0.00 USD | 1,240,000.00 USD | 188,170.00 USD | 123,650.00 USD |
| `1D` | `779.80` | 58,550,000.00 USD | 58,550,000.00 USD | 0.00 USD | 477,090.00 USD | 47,380.00 USD | 77,860.00 USD |
| `7D` | `780.20` | 51,100,000.00 USD | 51,100,000.00 USD | 0.00 USD | 1,070,000.00 USD | 86,470.00 USD | 218,750.00 USD |
| `1D` | `780.60` | 59,090,000.00 USD | 59,090,000.00 USD | 0.00 USD | 373,710.00 USD | 78,310.00 USD | 84,520.00 USD |
| `7D` | `781.10` | 52,710,000.00 USD | 52,710,000.00 USD | 0.00 USD | 1,270,000.00 USD | 90,990.00 USD | 242,450.00 USD |
| `1D` | `781.40` | 59,700,000.00 USD | 59,700,000.00 USD | 0.00 USD | 363,950.00 USD | 110,320.00 USD | 143,980.00 USD |
| `7D` | `782.00` | 54,610,000.00 USD | 54,610,000.00 USD | 0.00 USD | 1,510,000.00 USD | 87,670.00 USD | 301,190.00 USD |
| `1D` | `782.20` | 60,970,000.00 USD | 60,970,000.00 USD | 0.00 USD | 987,130.00 USD | 15,380.00 USD | 263,560.00 USD |
| `7D` | `782.90` | 56,600,000.00 USD | 56,600,000.00 USD | 0.00 USD | 1,750,000.00 USD | 36,140.00 USD | 202,700.00 USD |
| `1D` | `783.00` | 61,780,000.00 USD | 61,780,000.00 USD | 0.00 USD | 617,080.00 USD | 50,410.00 USD | 137,740.00 USD |
| `1D` | `783.80` | 62,050,000.00 USD | 62,050,000.00 USD | 0.00 USD | 247,150.00 USD | 14,770.00 USD | 8,400.00 USD |
| `7D` | `783.80` | 57,170,000.00 USD | 57,170,000.00 USD | 0.00 USD | 508,000.00 USD | 10,100.00 USD | 54,380.00 USD |
| `1D` | `784.60` | 62,480,000.00 USD | 62,480,000.00 USD | 0.00 USD | 433,980.00 USD | 2,690.00 USD | 0.00 USD |
| `7D` | `784.70` | 57,480,000.00 USD | 57,480,000.00 USD | 0.00 USD | 208,380.00 USD | 28,260.00 USD | 70,300.00 USD |
| `1D` | `785.40` | 62,580,000.00 USD | 62,580,000.00 USD | 0.00 USD | 93,760.00 USD | 4,490.00 USD | 0.00 USD |
| `7D` | `785.60` | 58,610,000.00 USD | 58,610,000.00 USD | 0.00 USD | 1,010,000.00 USD | 54,140.00 USD | 71,180.00 USD |
| `1D` | `786.20` | 62,670,000.00 USD | 62,670,000.00 USD | 0.00 USD | 74,920.00 USD | 0.00 USD | 18,430.00 USD |
| `7D` | `786.50` | 59,000,000.00 USD | 59,000,000.00 USD | 0.00 USD | 329,230.00 USD | 30,660.00 USD | 23,970.00 USD |
| `1D` | `787.00` | 62,790,000.00 USD | 62,790,000.00 USD | 0.00 USD | 120,340.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `787.40` | 59,580,000.00 USD | 59,580,000.00 USD | 0.00 USD | 470,050.00 USD | 17,630.00 USD | 91,050.00 USD |
| `1D` | `787.80` | 63,510,000.00 USD | 63,510,000.00 USD | 0.00 USD | 365,920.00 USD | 10,420.00 USD | 341,610.00 USD |
| `7D` | `788.30` | 59,940,000.00 USD | 59,940,000.00 USD | 0.00 USD | 202,630.00 USD | 82,380.00 USD | 81,230.00 USD |
| `1D` | `788.60` | 63,560,000.00 USD | 63,560,000.00 USD | 0.00 USD | 43,780.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `789.20` | 60,780,000.00 USD | 60,780,000.00 USD | 0.00 USD | 698,830.00 USD | 81,250.00 USD | 55,990.00 USD |
| `1D` | `789.40` | 63,770,000.00 USD | 63,770,000.00 USD | 0.00 USD | 164,090.00 USD | 11,780.00 USD | 34,900.00 USD |
| `7D` | `790.10` | 61,270,000.00 USD | 61,270,000.00 USD | 0.00 USD | 299,250.00 USD | 104,360.00 USD | 88,890.00 USD |
| `1D` | `790.20` | 64,220,000.00 USD | 64,220,000.00 USD | 0.00 USD | 285,360.00 USD | 2,560.00 USD | 162,050.00 USD |
| `1D` | `791.00` | 64,360,000.00 USD | 64,360,000.00 USD | 0.00 USD | 85,520.00 USD | 33,700.00 USD | 21,390.00 USD |
| `7D` | `791.00` | 62,150,000.00 USD | 62,150,000.00 USD | 0.00 USD | 693,290.00 USD | 82,870.00 USD | 100,420.00 USD |
| `1D` | `791.80` | 64,510,000.00 USD | 64,510,000.00 USD | 0.00 USD | 141,380.00 USD | 0.00 USD | 7,150.00 USD |
| `7D` | `791.90` | 63,030,000.00 USD | 63,030,000.00 USD | 0.00 USD | 816,380.00 USD | 16,830.00 USD | 46,300.00 USD |
| `1D` | `792.60` | 64,640,000.00 USD | 64,640,000.00 USD | 0.00 USD | 135,050.00 USD | 0.00 USD | 0.00 USD |
| `7D` | `792.80` | 63,250,000.00 USD | 63,250,000.00 USD | 0.00 USD | 205,450.00 USD | 0.00 USD | 14,670.00 USD |
| `1D` | `793.40` | 64,670,000.00 USD | 64,670,000.00 USD | 0.00 USD | 31,240.00 USD | 0.00 USD | 0.00 USD |
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
  * Total Open Interest: `1.32B` | Total OI Tokens: `1,846,236.4 BNB`
  * 1h OI Change: `+0.10%` | 4h OI Change: `-1.37%` | 24h OI Change: `+5.30%`
  * Exchange Breakdown: Binance=`573.59M` | Bybit=`138.31M` | OKX=`65.38M` | Hyperliquid=`70.62M`
- **Funding Settlement Yield (6_Funding_Fee_Settlement.parquet)**:
  * Current Rate: `-140.89K` | Last 24h: `-51.15K` | Last 3d: `142.23K` | Last 7d: `346.08K`
- **12-Venue Comprehensive Funding Rates Matrix (5_Funding_Rate.parquet)**:
| Venue | Funding Rate | Venue | Funding Rate |
|:---|:---:|:---|:---:|
| **USDT Binance** | `0.0000%` | **USDT OKX** | `-0.0616%` |
| **USDT Bybit** | `-0.0725%` | **USDT KuCoin** | `-0.0106%` |
| **USDT MEXC** | `0.0000%` | **USDT BingX** | `0.0050%` |
| **USDT Gate** | `-0.0161%` | **USDT Bitget** | `-0.0079%` |
| **CoinM Binance** | `0.1188%` | **CoinM OKX** | `-` |

- **Multi-Horizon Long/Short Ratio Positioning Table (3_Exchanges_LS_Ratio_*.parquet)**:
| Horizon | Exchange | Long % | Short % | L/S Ratio | Total Volume (USD) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `15M` | `BNB` | `34.88%` | `65.12%` | `0.54` | 13,980,000.00 USD |
| `15M` | `Binance` | `33.29%` | `66.71%` | `0.50` | 7,860,000.00 USD |
| `15M` | `OKX` | `42.33%` | `57.67%` | `0.73` | 637,560.00 USD |
| `15M` | `Bybit` | `63.53%` | `36.47%` | `1.74` | 1,670,000.00 USD |
| `15M` | `KuCoin` | `40.4%` | `59.6%` | `0.68` | 169,270.00 USD |
| `15M` | `Gate` | `33.56%` | `66.44%` | `0.51` | 615,490.00 USD |
| `15M` | `Bitget` | `8.49%` | `91.51%` | `0.09` | 1,040,000.00 USD |
| `15M` | `BingX` | `16.08%` | `83.92%` | `0.19` | 811,350.00 USD |
| `15M` | `MEXC` | `11.16%` | `88.84%` | `0.13` | 226,300.00 USD |
| `15M` | `Bitunix` | `37.15%` | `62.85%` | `0.59` | 295,340.00 USD |
| `15M` | `Hyperliquid` | `57.61%` | `42.39%` | `1.36` | 216,920.00 USD |
| `15M` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `LBank` | `49.86%` | `50.14%` | `0.99` | 126,080.00 USD |
| `15M` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `WhiteBIT` | `0%` | `100%` | `0.00` | 15,550.00 USD |
| `15M` | `HTX` | `35.83%` | `64.17%` | `0.56` | 160,910.00 USD |
| `15M` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Aster` | `51.86%` | `48.14%` | `1.08` | 99,920.00 USD |
| `15M` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `15M` | `Lighter` | `14.64%` | `85.36%` | `0.17` | 38,810.00 USD |
| `15M` | `Whale Positions` | `33.29%` | `66.71%` | `0.50` | 7,860,000.00 USD |
| `15M` | `Global Accounts` | `34.88%` | `65.12%` | `0.54` | 13,980,000.00 USD |
| `1H` | `BNB` | `49.87%` | `50.13%` | `0.99` | 331,950,000.00 USD |
| `1H` | `Binance` | `48.75%` | `51.25%` | `0.95` | 93,720,000.00 USD |
| `1H` | `OKX` | `51.56%` | `48.44%` | `1.06` | 70,560,000.00 USD |
| `1H` | `Bybit` | `44.76%` | `55.24%` | `0.81` | 45,760,000.00 USD |
| `1H` | `KuCoin` | `52.46%` | `47.54%` | `1.10` | 1,440,000.00 USD |
| `1H` | `Gate` | `54.57%` | `45.43%` | `1.20` | 22,740,000.00 USD |
| `1H` | `Bitget` | `47.11%` | `52.89%` | `0.89` | 14,350,000.00 USD |
| `1H` | `BingX` | `51.48%` | `48.52%` | `1.06` | 13,520,000.00 USD |
| `1H` | `MEXC` | `39.17%` | `60.83%` | `0.64` | 24,250,000.00 USD |
| `1H` | `Bitunix` | `51.59%` | `48.41%` | `1.07` | 20,840,000.00 USD |
| `1H` | `Hyperliquid` | `58.59%` | `41.41%` | `1.41` | 13,590,000.00 USD |
| `1H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `LBank` | `52.1%` | `47.9%` | `1.09` | 1,320,000.00 USD |
| `1H` | `Crypto.com` | `54.38%` | `45.62%` | `1.19` | 457,290.00 USD |
| `1H` | `WhiteBIT` | `96.71%` | `3.29%` | `29.40` | 3,760,000.00 USD |
| `1H` | `HTX` | `69.16%` | `30.84%` | `2.24` | 824,470.00 USD |
| `1H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Kraken` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Aster` | `50.34%` | `49.66%` | `1.01` | 2,020,000.00 USD |
| `1H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `1H` | `Lighter` | `62.41%` | `37.59%` | `1.66` | 2,790,000.00 USD |
| `1H` | `Whale Positions` | `48.75%` | `51.25%` | `0.95` | 93,720,000.00 USD |
| `1H` | `Global Accounts` | `49.87%` | `50.13%` | `0.99` | 331,950,000.00 USD |
| `4H` | `BNB` | `49.14%` | `50.86%` | `0.97` | 475,330,000.00 USD |
| `4H` | `Binance` | `47.71%` | `52.29%` | `0.91` | 291,250,000.00 USD |
| `4H` | `OKX` | `46.14%` | `53.86%` | `0.86` | 46,880,000.00 USD |
| `4H` | `Bybit` | `60.68%` | `39.32%` | `1.54` | 38,740,000.00 USD |
| `4H` | `KuCoin` | `57.9%` | `42.1%` | `1.38` | 3,320,000.00 USD |
| `4H` | `Gate` | `48.05%` | `51.95%` | `0.92` | 15,960,000.00 USD |
| `4H` | `Bitget` | `43.02%` | `56.98%` | `0.76` | 10,110,000.00 USD |
| `4H` | `BingX` | `35.39%` | `64.61%` | `0.55` | 10,230,000.00 USD |
| `4H` | `MEXC` | `53.76%` | `46.24%` | `1.16` | 4,030,000.00 USD |
| `4H` | `Bitunix` | `51.51%` | `48.49%` | `1.06` | 11,160,000.00 USD |
| `4H` | `Hyperliquid` | `61%` | `39%` | `1.56` | 20,560,000.00 USD |
| `4H` | `tradeXYZ` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `LBank` | `48.77%` | `51.23%` | `0.95` | 2,980,000.00 USD |
| `4H` | `Crypto.com` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `WhiteBIT` | `30.95%` | `69.05%` | `0.45` | 422,230.00 USD |
| `4H` | `HTX` | `27.56%` | `72.44%` | `0.38` | 3,560,000.00 USD |
| `4H` | `dYdX` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Deribit` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Bitfinex` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Kraken` | `75.73%` | `24.27%` | `3.12` | 3,050,000.00 USD |
| `4H` | `Aster` | `52.54%` | `47.46%` | `1.11` | 9,140,000.00 USD |
| `4H` | `Coinbase` | `0%` | `0%` | `1.00` | 0.00 USD |
| `4H` | `Lighter` | `45.54%` | `54.46%` | `0.84` | 3,950,000.00 USD |
| `4H` | `Whale Positions` | `47.71%` | `52.29%` | `0.91` | 291,250,000.00 USD |
| `4H` | `Global Accounts` | `49.14%` | `50.86%` | `0.97` | 475,330,000.00 USD |


---

## 8. Microstructure Footprint Bars, Tape Imbalances & Macro Capital Netflows
*(Sources: 26_Aggregated_Footprint_Bar_Metrics.parquet, 25_CoinGlass_Footprint_Signals.parquet, 2_Spot_Netflow_S.parquet, 2_Future_Netflow.parquet, 1_Crypto_ETF_Flows.parquet, 19_Calendar.parquet, 19_News.parquet)*
- **Recent Completed 15m Footprint Bars Profile Table (26_Aggregated_Footprint_Bar_Metrics.parquet)**:
| Bar Time (UTC) | Close | VWAP | POC | VAH | VAL | Volume (USD) | Buy Vol | Sell Vol | Delta (USD) | Delta % | Imbalances (B/S) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| `0:00 UTC` | `717.15` | `715.03` | `717.15` | `717.45` | `709.35` | 18,001,107.25 USD | 10,590,792.94 USD | 7,410,314.32 USD | 3,180,478.62 USD | `+17.67%` | `10B / 0S` |
| `5:00 UTC` | `718.65` | `718.30` | `718.65` | `719.85` | `716.85` | 14,406,892.83 USD | 6,892,738.14 USD | 7,514,154.69 USD | -621,416.55 USD | `-4.31%` | `1B / 0S` |
| `0:00 UTC` | `716.85` | `716.98` | `716.85` | `719.55` | `715.05` | 10,882,676.97 USD | 3,981,765.95 USD | 6,900,911.02 USD | -2,919,145.07 USD | `-26.82%` | `0B / 0S` |
| `5:00 UTC` | `717.15` | `717.39` | `717.15` | `718.65` | `716.25` | 6,978,599.94 USD | 3,350,532.71 USD | 3,628,067.23 USD | -277,534.53 USD | `-3.98%` | `0B / 0S` |
| `0:00 UTC` | `717.45` | `717.74` | `717.45` | `719.55` | `716.55` | 5,355,538.86 USD | 2,861,377.69 USD | 2,494,161.17 USD | 367,216.51 USD | `+6.86%` | `2B / 1S` |
| `5:00 UTC` | `717.45` | `717.28` | `717.45` | `718.05` | `716.55` | 4,945,586.67 USD | 2,313,018.42 USD | 2,632,568.25 USD | -319,549.83 USD | `-6.46%` | `0B / 2S` |
| `0:00 UTC` | `719.85` | `719.92` | `719.85` | `721.65` | `716.55` | 8,783,632.79 USD | 5,084,805.58 USD | 3,698,827.21 USD | 1,385,978.37 USD | `+15.78%` | `3B / 1S` |
| `5:00 UTC` | `718.65` | `718.49` | `718.65` | `719.55` | `717.45` | 6,099,294.65 USD | 2,396,548.55 USD | 3,702,746.10 USD | -1,306,197.54 USD | `-21.42%` | `0B / 1S` |
| `0:00 UTC` | `718.95` | `718.35` | `718.95` | `719.55` | `716.85` | 4,905,756.58 USD | 2,037,050.94 USD | 2,868,705.64 USD | -831,654.70 USD | `-16.95%` | `0B / 3S` |
| `5:00 UTC` | `718.35` | `718.21` | `718.35` | `718.95` | `717.45` | 1,515,872.89 USD | 851,793.20 USD | 664,079.68 USD | 187,713.52 USD | `+12.38%` | `1B / 0S` |

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
| `5m` | -16,150.00 USD | 54,490.00 USD | **`ACCUMULATION`** |
| `15m` | -38,390.00 USD | 129,670.00 USD | **`ACCUMULATION`** |
| `30m` | -495,650.00 USD | 334,440.00 USD | **`DISTRIBUTION`** |
| `1h` | -226,620.00 USD | 1,370,000.00 USD | **`ACCUMULATION`** |
| `2h` | -272,990.00 USD | -5,620,000.00 USD | **`DISTRIBUTION`** |
| `4h` | -1,950,000.00 USD | -6,050,000.00 USD | **`DISTRIBUTION`** |
| `6h` | -12,260,000.00 USD | -14,490,000.00 USD | **`DISTRIBUTION`** |
| `8h` | -11,250,000.00 USD | -26,770,000.00 USD | **`DISTRIBUTION`** |
| `12h` | -28,600,000.00 USD | -60,120,000.00 USD | **`DISTRIBUTION`** |
| `24h` | -31,680,000.00 USD | -82,570,000.00 USD | **`DISTRIBUTION`** |
| `1w` | -57,820,000.00 USD | -107,280,000.00 USD | **`DISTRIBUTION`** |
| `30d` | -157,000,000.00 USD | -436,810,000.00 USD | **`DISTRIBUTION`** |

* Spot Capital Netflows: 5m=`-16.15K` | 15m=`-38.39K` | 1h=`-226.62K` | 24h=`-31.68M`
* Futures Capital Netflows: 5m=`+54.49K` | 15m=`+129.67K` | 1h=`+1.37M` | 24h=`-82.57M`
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
  * `2026-10-30 11:03:23 IST`: [kitco.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:19:23 IST`: [cnbc.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [forex.com] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 11:18:23 IST`: [boj.or.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 08:20:23 IST`: [financemagnates.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [finance.yahoo.com] - (Sentiment: `Neutral`)
  * `2026-10-30 07:20:23 IST`: [kathleenhays.substack.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [rba.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [abs.gov.au] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [think.ing.com] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [@NodeWire] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 06:20:23 IST`: [meti.go.jp] - (Sentiment: `Neutral`)
  * `2026-10-30 05:20:23 IST`: [@financialjuice] - (Sentiment: `Neutral`)


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
  * Spread-Padded Stop Loss: `687.82` (Risk Distance: `11.13` pts)
  * +2.5R Take Profit: `726.77`
  * Mathematical Lot Sizing: **`0.89 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)
- **Candidate Short Setup (Model 1 / Model 2 VAH Sweep Fade)**:
  * Order Type: `SELL_LIMIT`
  * Execution Entry: `715.55` (Daily VAH sweep / Bearish OTE)
  * Spread-Padded Stop Loss: `726.68` (Risk Distance: `11.13` pts)
  * +2.5R Take Profit: `687.73`
  * Mathematical Lot Sizing: **`0.89 lots`** (Nominal Risk = `0.10 USD <= 10.00 USD`)

### ⚡ Sovereign Autonomous Execution Decision:
**Postured Action**: **`STAND_ASIDE_MONITOR`**
- Invalidation Rule: Cancel all resting orders if price penetrates beyond 0.786 Fibonacci level (`721.22`) or if 21:15 UTC rollover blackout begins.
- Monotone Non-Loosening Ratchet: At +0.80R unrealized profit, lock stop to Entry ± 0.15R; at +1.65R profit, lock stop to Entry ± 0.80R.
